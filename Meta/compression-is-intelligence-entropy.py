"""Compression is prediction, measured on this vault's own prose.
(1) The entropy ladder: how many bits per character English costs a predictor that knows the previous k characters
    (k = 0..5), estimated by counting on ~1 MB of the vault's English; beside it, what gzip, bzip2 and xz actually
    achieve, and the reference points — Shannon's 1951 human guessers (~1 bit/char) and a large language model
    (Chinchilla 70B, 8.3 % of raw size on Wikipedia = 0.66 bits/char).
(2) Normalised compression distance (Cilibrasi & Vitányi 2005): NCD(x, y) = (C(xy) − min(C(x), C(y))) / max(C(x), C(y)).
    Zip six cards pairwise and the distances sort them by subject with no notion of "physics" in the code.
Run: python3 compression-is-intelligence-entropy.py"""
import glob, math, re, zlib, bz2, lzma, collections, os
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def english_of(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"^---.*?---\s*", "", t, flags=re.S)                # frontmatter
    t = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$", " ", t, flags=re.S)        # maths
    t = re.sub(r"!\[\[.*?\]\]|\[\[|\]\]|[#*>|`_]", " ", t)          # markup
    t = re.sub(r"[^\x20-\x7e\n]", "", t)                            # keep printable ASCII
    return re.sub(r"[ \t]+", " ", t)

files = sorted(glob.glob(f"{VAULT}/Physics/**/*.md", recursive=True) + glob.glob(f"{VAULT}/CS/**/*.md", recursive=True))
files = [f for f in files if not f.endswith("Directory.md")]
corpus = "\n".join(english_of(f) for f in files)[:1_000_000]
data = corpus.encode()
print(f"corpus: {len(corpus):,} characters of the vault's English, from {len(files)} cards\n")

print("== (1) bits per character, by how much the predictor knows ==")
for k in range(0, 6):
    ctx = collections.defaultdict(collections.Counter)
    for i in range(k, len(corpus)):
        ctx[corpus[i-k:i]][corpus[i]] += 1
    H = 0.0; n = len(corpus) - k
    for c, cnt in ctx.items():
        tot = sum(cnt.values())
        H += sum(v * math.log2(tot / v) for v in cnt.values())
    print(f"  order-{k} model (knows the previous {k} chars): {H/n:.2f} bits/char  [{len(ctx):,} contexts seen]")
for name, fn in [("gzip -9", lambda b: zlib.compress(b, 9)), ("bzip2", lambda b: bz2.compress(b, 9)), ("xz", lambda b: lzma.compress(b, preset=9 | lzma.PRESET_EXTREME))]:
    print(f"  {name:10s}: {8*len(fn(data))/len(data):.2f} bits/char")
print("  Shannon 1951, human guessers on English : about 1 bit/char")
print("  Chinchilla 70B on Wikipedia (2023)      : 0.66 bits/char  (8.3 % of raw)\n")
print("  (the order-4/5 counts are over-fitted on 1 MB — a real compressor blends orders and pays to learn them; the trend is the point)\n")

print("== (2) compression distance: which cards are 'close'? ==")
names = ["Kirchhoff's Laws", "Internal Resistance", "Potential Dividers", "SQL", "Relational Databases", "Erdős the Wandering Mathematician"]
def find(n): return [f for f in glob.glob(f"{VAULT}/**/{n}.md", recursive=True) if "_meta" not in f][0]
texts = {n: english_of(find(n)).encode() for n in names}
C = lambda b: len(lzma.compress(b, preset=9 | lzma.PRESET_EXTREME))
def ncd(a, b): return (C(a + b) - min(C(a), C(b))) / max(C(a), C(b))
short = [n.split()[0] for n in names]
print("  " + " " * 12 + "".join(f"{s:>12s}" for s in short))
for a in names:
    print(f"  {a.split()[0]:>12s}" + "".join(f"{ncd(texts[a], texts[b]):12.3f}" for b in names))
print("\n  smaller = closer. The three circuit cards sit near each other, the two database cards likewise; Erdős is far from all of them.")
