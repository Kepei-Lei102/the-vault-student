"""How a Language Model Works — the lab. Every number, sample and curve in the card comes from this file.

Run:  python3 language-model-lab.py            (about three minutes on a laptop; writes language-model-lab.json)
      python3 language-model-lab.py --quick    (a tenth of the training, for a smoke test)

Corpus: the sixty Story cards in ../../Stories, with their front matter, links and Chinese anchors stripped, so the
model learns from about a million characters of English prose written for this vault. No download, no library beyond
numpy: the counting models are dictionaries, the tokeniser is thirty lines, and the neural model, one layer of causal
self-attention and one small MLP, has its forward pass AND its backward pass written out by hand and checked against
finite differences before any training starts. Nothing here is a black box.
"""
import json, math, pathlib, re, sys, time
from collections import Counter, defaultdict
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
QUICK = "--quick" in sys.argv
rng = np.random.default_rng(1)

# ── 1. the corpus ─────────────────────────────────────────────────────────────────────────────────────────────
def load_corpus():
    text = []
    for p in sorted((HERE.parent.parent / "Stories").glob("*.md")):
        s = p.read_text(encoding="utf-8")
        if s.startswith("---"):
            s = s.split("---", 2)[2]
        s = re.sub(r"!\[\[[^\]]*\]\]", "", s)                    # embeds
        s = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", s)     # [[link|alias]] -> alias
        s = re.sub(r"\$[^$\n]*\$", "", s)                          # inline maths
        s = re.sub(r"[#>*_`|]", "", s)                             # markdown marks
        s = re.sub(r"^\s*-{3,}\s*$", "", s, flags=re.M)               # horizontal rules
        lines = [l for l in s.splitlines() if l.strip() and not re.search(r"[一-鿿]", l)]
        text.append("\n".join(lines))
    text = "\n".join(text)
    text = "".join(ch for ch in text if ch == "\n" or 32 <= ord(ch) < 127 or ch in "—–‘’“”…é")
    return re.sub(r"\n{2,}", "\n", text)

corpus = load_corpus()
n = len(corpus); split = int(0.9 * n)
train_text, held_text = corpus[:split], corpus[split:]
chars = sorted(set(corpus)); V = len(chars)
stoi = {c: i for i, c in enumerate(chars)}; itos = {i: c for c, i in stoi.items()}
print(f"corpus: {n:,} characters from the Stories, {V} distinct; train {split:,}, held out {n - split:,}")
out = {"corpus_chars": n, "vocab": V, "train_chars": split, "held_chars": n - split}

# ── 2. counting models: predict the next character from the last k ───────────────────────────────────────────
def ngram_counts(text, k):
    counts = defaultdict(Counter)
    for i in range(k, len(text)):
        counts[text[i - k:i]][text[i]] += 1
    return counts

def ngram_bits(counts, text, k, alpha=0.05):
    """Average bits per character on text, with add-alpha smoothing so an unseen continuation is not infinite."""
    total = 0.0
    for i in range(k, len(text)):
        c = counts.get(text[i - k:i]); n_ctx = sum(c.values()) if c else 0
        p = ((c[text[i]] if c else 0) + alpha) / (n_ctx + alpha * V)
        total -= math.log2(p)
    return total / (len(text) - k)

def ngram_sample(counts, k, length, seed):
    ctx = seed[-k:] if k else ""; s = seed
    for _ in range(length):
        c = counts.get(ctx)
        if not c:                                   # unseen context: back off to a shorter one
            for j in sorted((j for j in counts_by_k if j < k), reverse=True):
                c = counts_by_k[j].get(ctx[k - j:] if j else "")
                if c: break
        keys, w = zip(*c.items()); nxt = rng.choice(keys, p=np.array(w) / sum(w))
        s += nxt; ctx = (ctx + nxt)[-k:] if k else ""
    return s

counts_by_k = {k: ngram_counts(train_text, k) for k in (0, 1, 2, 3, 5, 8)}
counts_by_k[0] = defaultdict(Counter, {"": Counter(train_text)})
out["ngram"] = []
print("\n== counting models (bits per character on held-out text; lower is better; 8 bits is ASCII, ln V is", f"{math.log2(V):.2f})")
for k in (0, 1, 2, 3, 5, 8):
    bits = ngram_bits(counts_by_k[k], held_text, k) if k else -sum(math.log2((counts_by_k[0][""][c] + 0.05) / (split + 0.05 * V)) for c in held_text) / len(held_text)
    contexts = len(counts_by_k[k]); sample = ngram_sample(counts_by_k[k], k, 160, "The ")
    print(f"  {k}-char context: {bits:.2f} bits/char, {contexts:,} contexts seen\n     sample: {sample[:160]!r}")
    out["ngram"].append({"k": k, "bits": bits, "contexts": contexts, "sample": sample})

# ── 3. a tokeniser: byte-pair encoding, the first merges ─────────────────────────────────────────────────────
def bpe_merges(text, n_merges):
    words = Counter(tuple(w) + ("</w>",) for w in re.findall(r"[a-z]+", text.lower()))
    merges = []
    for _ in range(n_merges):
        pairs = Counter()
        for w, c in words.items():
            for a, b in zip(w, w[1:]): pairs[(a, b)] += c
        if not pairs: break
        (a, b), c = pairs.most_common(1)[0]; merges.append((a + b, c))
        new = {}
        for w, cnt in words.items():
            i, ww = 0, []
            while i < len(w):
                if i < len(w) - 1 and w[i] == a and w[i + 1] == b: ww.append(a + b); i += 2
                else: ww.append(w[i]); i += 1
            new[tuple(ww)] = new.get(tuple(ww), 0) + cnt
        words = new
    return merges
merges = bpe_merges(train_text[:400_000], 24)
out["bpe"] = [{"token": t.replace("</w>", "_"), "count": c} for t, c in merges]
print("\n== byte-pair encoding, first 24 merges (an underscore marks the end of a word):", ", ".join(t.replace("</w>", "_") for t, _ in merges))

# ── 4. the neural model: embeddings → one causal self-attention layer → MLP → next-character logits ─────────
def init_params(V, T, d, seed=0):
    r = np.random.default_rng(seed); s = 0.02
    return {"E": r.normal(0, s, (V, d)), "P": r.normal(0, s, (T, d)),
            "Wq": r.normal(0, s, (d, d)), "Wk": r.normal(0, s, (d, d)), "Wv": r.normal(0, s, (d, d)),
            "W1": r.normal(0, s, (d, 4 * d)), "b1": np.zeros(4 * d), "W2": r.normal(0, s, (4 * d, d)), "b2": np.zeros(d),
            "Wo": r.normal(0, s, (d, V)), "bo": np.zeros(V)}

def forward(p, tok, targets=None):
    B, T = tok.shape; d = p["E"].shape[1]
    x = p["E"][tok] + p["P"][:T]                                   # who am I, and where am I
    q, k, v = x @ p["Wq"], x @ p["Wk"], x @ p["Wv"]                # what I am looking for, what I offer, what I pass on
    scores = q @ k.transpose(0, 2, 1) / math.sqrt(d)               # (B,T,T): how much each position wants each earlier one
    mask = np.triu(np.ones((T, T), dtype=bool), 1)                 # no looking at the future
    scores = np.where(mask, -1e9, scores)
    scores -= scores.max(-1, keepdims=True); A = np.exp(scores); A /= A.sum(-1, keepdims=True)
    att = A @ v                                                    # each position: a weighted mix of earlier values
    h1 = x + att
    pre = h1 @ p["W1"] + p["b1"]; m = np.maximum(pre, 0); h2 = h1 + m @ p["W2"] + p["b2"]
    logits = h2 @ p["Wo"] + p["bo"]
    cache = (tok, x, q, k, v, A, att, h1, pre, m, h2)
    if targets is None: return logits, A, None, cache
    z = logits - logits.max(-1, keepdims=True); ez = np.exp(z); probs = ez / ez.sum(-1, keepdims=True)
    loss = -np.mean(np.log(probs[np.arange(B)[:, None], np.arange(T)[None, :], targets] + 1e-12))
    return logits, A, loss, (cache, probs, targets)

def backward(p, cache_all):
    (tok, x, q, k, v, A, att, h1, pre, m, h2), probs, targets = cache_all
    B, T, V = probs.shape; d = x.shape[-1]; g = {}
    dlog = probs.copy(); dlog[np.arange(B)[:, None], np.arange(T)[None, :], targets] -= 1; dlog /= B * T
    g["Wo"] = h2.reshape(-1, d).T @ dlog.reshape(-1, V); g["bo"] = dlog.sum((0, 1))
    dh2 = dlog @ p["Wo"].T
    dm = dh2 @ p["W2"].T; g["W2"] = m.reshape(-1, 4 * d).T @ dh2.reshape(-1, d); g["b2"] = dh2.sum((0, 1))
    dpre = dm * (pre > 0); g["W1"] = h1.reshape(-1, d).T @ dpre.reshape(-1, 4 * d); g["b1"] = dpre.sum((0, 1))
    dh1 = dh2 + dpre @ p["W1"].T
    datt = dh1
    dA = datt @ v.transpose(0, 2, 1); dv = A.transpose(0, 2, 1) @ datt
    dscores = A * (dA - (dA * A).sum(-1, keepdims=True)) / math.sqrt(d)
    dq = dscores @ k; dk = dscores.transpose(0, 2, 1) @ q
    g["Wq"] = x.reshape(-1, d).T @ dq.reshape(-1, d); g["Wk"] = x.reshape(-1, d).T @ dk.reshape(-1, d); g["Wv"] = x.reshape(-1, d).T @ dv.reshape(-1, d)
    dx = dh1 + dq @ p["Wq"].T + dk @ p["Wk"].T + dv @ p["Wv"].T
    g["E"] = np.zeros_like(p["E"]); np.add.at(g["E"], tok, dx)
    g["P"] = np.zeros_like(p["P"]); g["P"][:T] = dx.sum(0)
    return g

def gradient_check():
    """Finite differences against the hand-written backward pass, on a toy model in float64."""
    Vt, Tt, dt, Bt = 7, 5, 6, 2
    p = {k_: v_.astype(np.float64) for k_, v_ in init_params(Vt, Tt, dt, seed=3).items()}
    for k_ in p: p[k_] = np.random.default_rng(4).normal(0, 0.3, p[k_].shape)
    tok = np.random.default_rng(5).integers(0, Vt, (Bt, Tt)); tgt = np.random.default_rng(6).integers(0, Vt, (Bt, Tt))
    _, _, _, cache = forward(p, tok, tgt); g = backward(p, cache); worst = 0.0
    for name, W in p.items():
        for _ in range(6):
            idx = tuple(np.random.default_rng().integers(0, s) for s in W.shape); eps = 1e-5
            W[idx] += eps; lp = forward(p, tok, tgt)[2]; W[idx] -= 2 * eps; lm = forward(p, tok, tgt)[2]; W[idx] += eps
            num = (lp - lm) / (2 * eps); ana = g[name][idx]
            worst = max(worst, abs(num - ana) / max(1e-8, abs(num) + abs(ana)))
    return worst

worst = gradient_check()
print(f"\n== gradient check: worst relative error between finite differences and the hand-written backward pass = {worst:.1e}")
assert worst < 1e-5, "the backward pass is wrong; nothing below can be trusted"
out["gradient_check"] = worst

# ── 5. training ──────────────────────────────────────────────────────────────────────────────────────────────
T, d, B = 64, 96, 32
steps = 400 if QUICK else 20000
train_ids = np.array([stoi[c] for c in train_text], dtype=np.int64); held_ids = np.array([stoi[c] for c in held_text], dtype=np.int64)
p = init_params(V, T, d)
n_params = sum(w.size for w in p.values())
print(f"\n== neural model: context {T}, width {d}, one attention head, {n_params:,} parameters, {steps} steps of {B}×{T} characters")
mom = {k_: np.zeros_like(v_) for k_, v_ in p.items()}; vel = {k_: np.zeros_like(v_) for k_, v_ in p.items()}
b1, b2, lr = 0.9, 0.99, 3e-3

def batch(ids):
    ix = rng.integers(0, len(ids) - T - 1, B)
    return np.stack([ids[i:i + T] for i in ix]), np.stack([ids[i + 1:i + T + 1] for i in ix])

def held_bits(p, n_batches=20):
    r = np.random.default_rng(0); tot = 0.0
    for _ in range(n_batches):
        ix = r.integers(0, len(held_ids) - T - 1, B)
        xb = np.stack([held_ids[i:i + T] for i in ix]); yb = np.stack([held_ids[i + 1:i + T + 1] for i in ix])
        tot += forward(p, xb, yb)[2]
    return tot / n_batches / math.log(2)

def sample(p, seed_text, length, temperature=1.0, r=None):
    r = r or np.random.default_rng(7); ids = [stoi.get(c, 0) for c in seed_text]
    for _ in range(length):
        ctx = np.array([ids[-T:]]); logits = forward(p, ctx)[0][0, -1]
        if temperature == 0: nxt = int(np.argmax(logits))
        else:
            z = logits / temperature; z -= z.max(); pr = np.exp(z); pr /= pr.sum(); nxt = int(r.choice(V, p=pr))
        ids.append(nxt)
    return "".join(itos[i] for i in ids)

curve, samples, t0 = [], {}, time.time()
for step in range(steps + 1):
    if step % (steps // 10) == 0 or step == steps:
        hb = held_bits(p); curve.append({"step": step, "held_bits": hb}); samples[step] = sample(p, "The ", 200)
        print(f"  step {step:5d}  held-out {hb:.2f} bits/char  ({time.time() - t0:.0f} s)\n     sample: {samples[step][:120]!r}")
    if step == steps: break
    xb, yb = batch(train_ids); _, _, loss, cache = forward(p, xb, yb); g = backward(p, cache)
    t = step + 1
    lr_t = 1e-4 + (lr - 1e-4) * 0.5 * (1 + math.cos(math.pi * step / steps))    # cosine decay: big steps early, fine steps late
    for k_ in p:
        mom[k_] = b1 * mom[k_] + (1 - b1) * g[k_]; vel[k_] = b2 * vel[k_] + (1 - b2) * g[k_] ** 2
        p[k_] -= lr_t * (mom[k_] / (1 - b1 ** t)) / (np.sqrt(vel[k_] / (1 - b2 ** t)) + 1e-8)
out["neural"] = {"T": T, "d": d, "params": int(n_params), "steps": steps, "curve": curve, "samples": {str(k_): v_ for k_, v_ in samples.items()}}

# ── 6. what the trained model does ───────────────────────────────────────────────────────────────────────────
print("\n== temperature: the same seed, three ways")
out["temperature"] = {}
for temp in (0.0, 0.7, 1.5):
    s = sample(p, "Newton ", 120, temp); out["temperature"][str(temp)] = s; print(f"  T = {temp}: {s!r}")

probe = "the letter that she wrote"
ids = np.array([[stoi[c] for c in probe]]); _, A, _, _ = forward(p, ids)
out["attention"] = {"probe": probe, "weights": A[0].round(4).tolist()}
last = A[0, -1]; top = np.argsort(last)[::-1][:5]
print(f"\n== attention of the last character of {probe!r} on the characters before it: top five")
for i in top: print(f"   position {i:2d} {probe[i]!r}: {last[i]:.3f}")

# next-character distribution after a seed, for the card's worked example
seed = "The theore"; ids = np.array([[stoi[c] for c in seed]]); logits = forward(p, ids)[0][0, -1]
z = logits - logits.max(); pr = np.exp(z); pr /= pr.sum(); top = np.argsort(pr)[::-1][:6]
out["next_char"] = {"seed": seed, "top": [{"char": itos[i], "p": float(pr[i])} for i in top]}
print(f"\n== after {seed!r} the model's next-character probabilities: " + ", ".join(f"{itos[i]!r} {pr[i]:.2f}" for i in top))

(HERE / "language-model-lab.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("\nwrote language-model-lab.json")
