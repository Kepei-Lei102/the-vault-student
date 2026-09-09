"""How long a brute-force search takes, by password shape and by how the site stored it.
Guess rates: a single modern GPU tests roughly 1e11 MD5 hashes per second, but only ~1e5
bcrypt hashes per second (cost 12) — the slow hash is the whole point.
Regenerate: python3 data-security-crack-time.py"""
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

shapes = [("6 lowercase", 26**6), ("8 lowercase", 26**8), ("8 mixed + digits", 62**8),
          ("10 mixed + digits + symbols", 94**10), ("12 mixed + digits + symbols  —  \\$Iippery_F0x, attacker knows nothing", 94**12),
          ("4 random words (7776-word list)", 7776**4),
          ("\\$Iippery_F0x  —  attacker guesses the recipe (~1e13)", 10**13)]
rates = [("stored as MD5 (1e11 guesses/s)", 1e11, "#dc2626"), ("stored as bcrypt (1e5 guesses/s)", 1e5, "#059669")]
GREY = "#888888"
fig, ax = plt.subplots(figsize=(9, 5.4)); fig.patch.set_alpha(0); ax.set_facecolor("none")
y = list(range(len(shapes)))
for k, (label, rate, col) in enumerate(rates):
    secs = [n / 2 / rate for _, n in shapes]          # expected: half the space
    ax.barh([yy + (k - 0.5) * 0.36 for yy in y], secs, height=0.34, color=col, alpha=0.85, label=label)
ax.set_xscale("log"); ax.set_yticks(y); ax.set_yticklabels([s for s, _ in shapes], fontsize=9, color=GREY)
ax.set_xlabel("expected time to crack (seconds, log scale)", color=GREY)
marks = [(1, "1 s"), (60, "1 min"), (3600, "1 h"), (86400, "1 day"), (3.15e7, "1 year"), (3.15e9, "100 years"), (4.35e17, "age of universe")]
for x, t in marks:
    ax.axvline(x, color=GREY, lw=0.5, ls=":"); ax.text(x, len(shapes) - 0.35, t, rotation=90, fontsize=7.5, color=GREY, va="bottom", ha="right")
ax.set_xlim(1e-4, 1e24); ax.set_ylim(-0.6, len(shapes) + 1.4)
for s in ax.spines.values(): s.set_color(GREY)
ax.tick_params(colors=GREY, labelsize=8)
fig.suptitle("Brute force: length (yours) and the hash (the site's) each buy orders of magnitude", color=GREY, fontsize=10)
leg = ax.legend(frameon=False, fontsize=9, loc="lower right")
for t in leg.get_texts(): t.set_color(GREY)
fig.tight_layout(rect=(0, 0, 1, 0.97)); fig.savefig("data-security-crack-time.svg", transparent=True)
for (s, n) in shapes:
    print(f"{s:34s} space=2^{math.log2(n):5.1f}  MD5: {n/2/1e11:12.3g} s   bcrypt: {n/2/1e5:12.3g} s")
