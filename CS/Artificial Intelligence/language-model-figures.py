"""Figures for How a Language Model Works — run after language-model-lab.py (reads language-model-lab.json)."""
import json, re, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TXT = "#888"; BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": TXT, "axes.labelcolor": TXT, "xtick.color": TXT, "ytick.color": TXT, "axes.edgecolor": TXT, "font.size": 11, "svg.fonttype": "none"})
D = json.load(open("language-model-lab.json"))

def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name).read(); m = re.search(r"<svg[^>]*>", s)
    tag = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)).replace("<svg", '<svg width="100%"', 1)
    open(name, "w").write(s[:m.start()] + tag + s[m.end():]); plt.close(fig)

# 1. bits per character: counting models against context length, and the neural model's curve
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
ks = [r["k"] for r in D["ngram"]]; bits = [r["bits"] for r in D["ngram"]]
a.plot(ks, bits, "o-", color=BLUE, lw=2)
for k, bt, r in zip(ks, bits, D["ngram"]): a.text(k, bt + 0.12, f"{bt:.2f}", ha="center", fontsize=9, color=BLUE)
a.axhline(math.log2(D["vocab"]), color=TXT, lw=0.8, ls="--"); a.text(ks[-1], math.log2(D["vocab"]) + 0.08, "every character equally likely", ha="right", fontsize=9, color=TXT)
a.set_xlabel("characters of context the counting model looks at"); a.set_ylabel("bits per character on unseen text"); a.set_title("Counting models: longer context helps, then the counts run out", fontsize=10)
a.grid(alpha=.25); a.set_ylim(1.5, 7)
for sp in ("top", "right"): a.spines[sp].set_visible(False)
c = D["neural"]["curve"]; b.plot([x["step"] for x in c], [x["held_bits"] for x in c], "o-", color=PURPLE, lw=2)
best_ng = min(bits); b.axhline(best_ng, color=BLUE, lw=1, ls="--"); b.text(c[-1]["step"], best_ng + 0.08, "best counting model", ha="right", fontsize=9, color=BLUE)
b.set_xlabel("training steps"); b.set_ylabel("bits per character on unseen text"); b.set_title(f"One attention layer, {D['neural']['params']:,} parameters, learning", fontsize=10)
b.grid(alpha=.25); b.set_ylim(1.5, 7)
for sp in ("top", "right"): b.spines[sp].set_visible(False)
save(fig, "language-model-bits.svg")

# 2. attention weights of the probe sentence
A = np.array(D["attention"]["weights"]); probe = D["attention"]["probe"]; n = len(probe)
fig, ax = plt.subplots(figsize=(7.5, 7))
im = ax.imshow(A, cmap="Purples", vmin=0, vmax=max(0.3, A.max()))
ax.set_xticks(range(n)); ax.set_xticklabels(list(probe), fontsize=10, family="monospace"); ax.set_yticks(range(n)); ax.set_yticklabels(list(probe), fontsize=10, family="monospace")
ax.set_xlabel("the character being attended to (earlier in the text)"); ax.set_ylabel("the character doing the attending")
ax.set_title(f"Attention weights inside the trained model for {probe!r}\neach row sums to one; the upper triangle is masked (no looking ahead)", fontsize=10)
for sp in ax.spines.values(): sp.set_visible(False)
cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02); cb.ax.yaxis.set_tick_params(color=TXT); cb.outline.set_visible(False)
save(fig, "language-model-attention.svg")

# 3. next-character distribution after the seed, at three temperatures
nc = D["next_char"]; chars = [t["char"].replace(" ", "␣").replace("\n", "↵") for t in nc["top"]]; ps = np.array([t["p"] for t in nc["top"]])
fig, ax = plt.subplots(figsize=(9, 3.8)); w = 0.26; x = np.arange(len(chars))
for i, (temp, col) in enumerate([(0.5, TEAL), (1.0, PURPLE), (2.0, AMBER)]):
    z = np.log(ps) / temp; q = np.exp(z - z.max()); q /= q.sum()
    ax.bar(x + (i - 1) * w, q, w, color=col, label=f"temperature {temp}")
ax.set_xticks(x); ax.set_xticklabels([f"'{c}'" for c in chars], family="monospace"); ax.set_ylabel("probability of the next character")
ax.set_title(f"After {nc['seed']!r}: the same six candidates, sharpened or flattened by temperature", fontsize=10)
ax.legend(frameon=False, fontsize=9); ax.grid(alpha=.25, axis="y")
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
save(fig, "language-model-temperature.svg")

# 4. the first byte-pair merges
fig, ax = plt.subplots(figsize=(10, 3.6)); toks = [b["token"] for b in D["bpe"]]; cnt = [b["count"] for b in D["bpe"]]
ax.bar(range(len(toks)), cnt, color=GREEN, alpha=.8); ax.set_xticks(range(len(toks))); ax.set_xticklabels(toks, rotation=45, ha="right", family="monospace", fontsize=10)
ax.set_ylabel("how often the pair appeared when merged"); ax.set_title("Byte-pair encoding on the Stories: the first 24 merges, in order (underscore = end of word)", fontsize=10)
ax.grid(alpha=.25, axis="y")
for sp in ("top", "right"): ax.spines[sp].set_visible(False)
save(fig, "language-model-bpe.svg")
print("wrote 4 SVGs")
