"""perceptron-and-move-78-timeline.py — the two lineages of AI, 1943–2025, with the winters shaded.
Companion to [[Stories/The Perceptron and Move 78]]. Vault style: text #888, no background, width="100%"."""
import re, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
GREY = "#888888"; BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"
fig, ax = plt.subplots(figsize=(14, 5.6))
for sp in ax.spines.values(): sp.set_color(GREY)
ax.tick_params(colors=GREY, labelcolor=GREY); ax.set_facecolor("none")
ax.set_xlim(1940, 2044); ax.set_ylim(-0.35, 3.2); ax.set_yticks([])
for sp in ("left", "right", "top"): ax.spines[sp].set_visible(False)
# winters
for a, b, lab in ((1969, 1980, "first winter\n(Perceptrons 1969, Lighthill 1973)"), (1987, 1993, "second winter\n(Lisp machines collapse)")):
    ax.axvspan(a, b, color=BLUE, alpha=0.07); ax.text((a + b) / 2, 3.05, lab, ha="center", va="top", fontsize=7.5, color=GREY)
# the two lanes
ax.text(1940.5, 2.45, "SYMBOLIC", fontsize=9.5, color=AMBER, weight="bold", va="bottom")
ax.text(1940.5, 0.32, "STATISTICAL", fontsize=9.5, color=PURPLE, weight="bold", va="top")
ax.axhline(2.2, color=AMBER, lw=1.0, alpha=0.5); ax.axhline(0.6, color=PURPLE, lw=1.0, alpha=0.5)
sym = [(1956, "Dartmouth summer:\n'artificial intelligence' named", 1), (1965, "expert systems begin\n(DENDRAL; MYCIN 1972)", -1), (1980, "XCON at DEC — the\nexpert-system boom", 1), (1997, "Deep Blue beats\nKasparov (search)", -1), (2006, "Monte Carlo tree search\n(Coulom; UCT)", 1)]
stat = [(1943, "McCulloch–Pitts\nneuron", 1), (1958, "Rosenblatt's perceptron;\nthe Navy press conference", -1), (1969, "Minsky & Papert:\nXOR", 1), (1986, "back propagation\n(Rumelhart, Hinton, Williams)", -1), (1995, "SVMs; random forests 2001\n— nets lose for a decade", 1), (2012, "AlexNet on two\ngaming GPUs", -1), (2017, "attention:\nthe transformer", 1)]
for yr, lab, sgn in sym:
    ax.plot(yr, 2.2, "o", color=AMBER, ms=5); ax.plot([yr, yr], [2.2, 2.2 + 0.28 * sgn], color=AMBER, lw=0.7)
    ax.text(yr, 2.2 + 0.32 * sgn, lab, ha="center", va="bottom" if sgn > 0 else "top", fontsize=7, color=GREY)
for yr, lab, sgn in stat:
    ax.plot(yr, 0.6, "o", color=PURPLE, ms=5); ax.plot([yr, yr], [0.6, 0.6 + 0.28 * sgn], color=PURPLE, lw=0.7)
    ax.text(yr, 0.6 + 0.32 * sgn, lab, ha="center", va="bottom" if sgn > 0 else "top", fontsize=7, color=GREY)
# the marriage
for yr, lab, y in ((2016, "AlphaGo 2016: deep nets + tree search + self-play — move 37 · move 78", 1.95), (2022, "LLMs 2022: transformer + next-word prediction + RL from feedback", 1.4), (2024, "reasoning models 2024: AlphaGo's recipe again", 0.85)):
    ax.plot([yr, yr], [0.6, 2.2], color=GREEN, lw=1.6, alpha=0.8); ax.plot(yr, y, "D", color=GREEN, ms=6)
    ax.plot([yr, 2026], [y, y], color=GREEN, lw=0.6, ls=":"); ax.text(2026.6, y, lab.replace(": ", ":\n"), ha="left", va="center", fontsize=7, color=GREEN)
ax.set_xlabel("year"); ax.set_title("Two lineages, not one ladder — symbolic (write the rules, search the space) above, statistical (learn the rules from data) below — and the three points where they married", fontsize=9.5, color=GREY)
fig.patch.set_alpha(0); name = "perceptron-and-move-78-timeline.svg"; fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
s = open(name).read().replace('<svg ', '<svg width="100%" ', 1); s = re.sub(r' height="[^"]*pt"', '', s, count=1); s = re.sub(r' width="[^"]*pt"', '', s, count=1); open(name, "w").write(s); print("wrote", name)
