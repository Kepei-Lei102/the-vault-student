"""The Grundlagenstreit as two tracks: the mathematics above the line, the quarrel below it.

Run:  python3 hilbert-brouwer-timeline.py   -> hilbert-brouwer-timeline.svg
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
G = "#888"
work = [
    (1890, "1890\nHilbert's basis\ntheorem: existence\nwithout construction"),
    (1899, "1899\nGrundlagen der\nGeometrie: axioms\nas rules of a game"),
    (1907, "1907–08\nBrouwer's thesis;\nexcluded middle\n'unreliable'"),
    (1911, "1911\nBrouwer: dimension\nis invariant;\nthe fixed point"),
    (1918, "1918\nintuitionist set\ntheory; choice\nsequences"),
    (1922, "1922–27\nHilbert's program:\nprove consistency\nby finite means"),
    (1931, "1931\nGödel: the\nprogram cannot\nfinish"),
]
feud = [
    (1890.5, "Gordan: 'this is\nnot mathematics,\nthis is theology'"),
    (1921, "Weyl: 'Brouwer —\nthat is the\nrevolution'"),
    (1922.6, "Hilbert: 'a Putsch\nwith old means'"),
    (1926, "'No one shall\nexpel us from\nthe paradise'"),
    (1928.4, "Bologna; the\nAnnalen affair:\nBrouwer removed"),
    (1930.7, "Königsberg:\n'We must know.\nWe will know.'"),
]
fig, ax = plt.subplots(figsize=(12, 4.8)); fig.patch.set_alpha(0); ax.set_facecolor("none")
ax.axhline(0, color=G, lw=1.5); ax.set_xlim(1886, 1940); ax.set_ylim(-2.6, 3.9)
heights = [1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 2.0]
for i, (x, lab) in enumerate(work):
    h = heights[i]
    ax.plot([x, x], [0, h], color="#2563eb", lw=1.2); ax.scatter([x], [0], s=40, color="#2563eb", zorder=3)
    ax.text(x, h + 0.1, lab, ha="center", va="bottom", fontsize=8, color="#2563eb")
fh = [-0.55, -1.45, -0.55, -1.45, -0.55, -1.45]
for i, (x, lab) in enumerate(feud):
    h = fh[i]
    ax.plot([x, x], [0, h], color="#f59e0b", lw=1.2); ax.text(x, h - 0.08, lab, ha="center", va="top", fontsize=8, color="#f59e0b")
# the day-before: Gödel's announcement, 7 Sept 1930, the day before Hilbert's broadcast
ax.annotate("7 Sept 1930, the day before the broadcast:\nGödel, 24, announces incompleteness\nin a discussion session across town",
            xy=(1930.68, 0), xytext=(1933.0, 0.55), fontsize=8, color="#dc2626", ha="left", va="bottom",
            arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1))
ax.scatter([1930.68], [0], s=60, color="#dc2626", zorder=4)
ax.set_yticks([]); ax.tick_params(colors=G); ax.set_xlabel("year", color=G)
for s in ax.spines.values(): s.set_color(G)
ax.spines["left"].set_visible(False); ax.spines["right"].set_visible(False); ax.spines["top"].set_visible(False)
ax.set_title("above the line, the mathematics; below it, the quarrel", color=G, fontsize=10)
fig.tight_layout(); fig.savefig("hilbert-brouwer-timeline.svg", transparent=True); print("wrote hilbert-brouwer-timeline.svg")
