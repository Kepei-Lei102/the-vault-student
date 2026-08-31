"""Figures for Graphs (vault style: #888 text, semantic colors, transparent
background, verified on light and dark).

Run from this folder:  python3 graphs-figures.py
Outputs: graphs-family-reveal.svg, graphs-matrix-vs-list.svg

Fig 1: the bay retrospective — the same seven vertices wearing a list's
straitjacket, a tree's, and then no constraints at all.
Fig 2: one four-vertex graph stored both ways — adjacency matrix and
dictionary-of-neighbours — with the same edge highlighted in both.

Tofu list: no \\tfrac, \\vec, \\to, \\Rightarrow, \\perp, \\propto, \\leq,
\\circ, literal arrows.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

GREY = "#888888"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
TEAL = "#0891b2"

plt.rcParams.update({
    "text.color": GREY, "axes.edgecolor": GREY, "axes.labelcolor": GREY,
    "xtick.color": GREY, "ytick.color": GREY, "font.size": 11,
    "axes.titlesize": 12, "svg.fonttype": "none", "svg.hashsalt": "vault",
    "font.family": ["Helvetica Neue", "Arial", "sans-serif"],
})


def node(ax, xy, label, color=BLUE, r=0.34):
    rgb = tuple(int(color[i:i + 2], 16) / 255 for i in (1, 3, 5))
    ax.add_patch(Circle(xy, r, facecolor=rgb + (0.18,), edgecolor=color,
                        lw=1.6, zorder=5))
    ax.text(*xy, label, color=GREY, fontsize=10.5, ha="center", va="center",
            zorder=6)


def edge(ax, a, b, color=GREY, lw=1.6, ls="-", z=3):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls, zorder=z)


# ============================ Fig 1: the family reveal ============================
fig = plt.figure(figsize=(10.6, 8.2))
gs = fig.add_gridspec(2, 2, height_ratios=[0.62, 1.38])
axes = [fig.add_subplot(gs[0, :]), fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])]

labels = list("ABCDEFG")

# (a) the list: a path graph — the wide, short panel gets the whole top row
ax = axes[0]
pos = {l: (i * 1.15 - 3.45, 0.0) for i, l in enumerate(labels)}
for a, b in zip(labels, labels[1:]):
    edge(ax, pos[a], pos[b])
for l in labels:
    node(ax, pos[l], l)
ax.text(0, -1.55, 'the constraint: "one next each, no cycles"',
        color=GREY, fontsize=10.5, ha="center")
ax.set_title("a linked list is a graph in a straitjacket", color=GREY, pad=8,
             fontsize=11.5)

# (b) the tree
ax = axes[1]
pos = {"A": (0, 1.6), "B": (-1.8, 0.3), "C": (1.8, 0.3),
       "D": (-2.7, -1.0), "E": (-0.9, -1.0), "F": (0.9, -1.0), "G": (2.7, -1.0)}
for a, b in [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("C", "G")]:
    edge(ax, pos[a], pos[b])
for l in labels:
    node(ax, pos[l], l)
ax.text(0, -2.15, 'the constraint: "one parent each, no cycles"',
        color=GREY, fontsize=10.5, ha="center")
ax.set_title("a tree is a graph in a looser one", color=GREY, pad=8,
             fontsize=11.5)

# (c) the graph: same vertices, constraints deleted
ax = axes[2]
rng = {"A": (0, 1.7), "B": (-2.1, 0.75), "C": (2.1, 0.75), "D": (-2.5, -0.9),
       "E": (-0.4, -0.35), "F": (1.0, -1.35), "G": (2.6, -1.0)}
graph_edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("A", "E"),
               ("C", "E"), ("C", "G"), ("E", "F"), ("F", "G"), ("D", "E")]
cycle = {("A", "B"), ("B", "E"), ("A", "E")}
for a, b in graph_edges:
    col = AMBER if (a, b) in cycle or (b, a) in cycle else GREY
    edge(ax, rng[a], rng[b], color=col, lw=2.0 if col == AMBER else 1.6)
for l in labels:
    node(ax, rng[l], l, color=TEAL)
ax.text(0, -2.15, "no constraints: many-to-many, cycles allowed",
        color=GREY, fontsize=10.5, ha="center")
ax.text(-2.35, 1.55, "a cycle —\nfinally legal", color=AMBER, fontsize=9.6,
        ha="center")
ax.set_title("delete every rule and the graph remains", color=GREY, pad=8,
             fontsize=11.5)

axes[0].set_xlim(-4.4, 4.4); axes[0].set_ylim(-2.1, 1.1)
for ax in axes[1:]:
    ax.set_xlim(-4.0, 4.0)
    ax.set_ylim(-2.6, 2.4)
for ax in axes:
    ax.set_aspect("equal")
    ax.axis("off")

fig.suptitle("the whole bay was graphs all along — each structure is a graph plus restrictions",
             color=GREY, fontsize=13, y=0.985)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig("graphs-family-reveal.svg", transparent=True, metadata={"Date": None})
plt.close(fig)


# ============================ Fig 2: matrix vs list ============================
fig = plt.figure(figsize=(10.6, 8.6))
gs = fig.add_gridspec(2, 2, height_ratios=[0.92, 1.08])
axes = [fig.add_subplot(gs[0, :]), fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])]

# the graph itself: 4 vertices, weighted, undirected
ax = axes[0]
P = {"A": (-1.4, 1.1), "B": (1.4, 1.1), "C": (-1.4, -1.3), "D": (1.4, -1.3)}
W = {("A", "B"): 5, ("A", "C"): 2, ("B", "D"): 4, ("C", "D"): 7, ("B", "C"): 3}
for (a, b), w in W.items():
    hl = (a, b) == ("B", "C")
    edge(ax, P[a], P[b], color=AMBER if hl else GREY, lw=2.2 if hl else 1.6)
    mid = ((P[a][0] + P[b][0]) / 2, (P[a][1] + P[b][1]) / 2)
    off = (0.28, 0.12) if not hl else (0.34, 0.18)
    ax.text(mid[0] + off[0], mid[1] + off[1], str(w),
            color=AMBER if hl else GREY, fontsize=10.5)
for l, xy in P.items():
    node(ax, xy, l)
ax.set_title("one weighted graph", color=GREY, pad=8, fontsize=12)
ax.set_xlim(-4.6, 4.6); ax.set_ylim(-2.3, 2.0)

# the matrix
ax = axes[1]
order = "ABCD"
M = [["", "5", "2", ""], ["5", "", "3", "4"], ["2", "3", "", "7"], ["", "4", "7", ""]]
x0, y0, dx, dy = -1.5, 1.25, 0.95, 0.95
for j, l in enumerate(order):
    ax.text(x0 + (j + 1) * dx, y0 + 0.55, l, color=BLUE, fontsize=11, ha="center")
    ax.text(x0 - 0.55, y0 - j * dy, l, color=BLUE, fontsize=11, ha="center",
            va="center")
for i in range(4):
    for j in range(4):
        v = M[i][j]
        hl = {i, j} == {1, 2}
        if hl:
            ax.add_patch(plt.Rectangle((x0 + (j + 1) * dx - 0.42,
                                        y0 - i * dy - 0.42), 0.84, 0.84,
                                       facecolor=(245/255, 158/255, 11/255, 0.20),
                                       edgecolor=AMBER, lw=1.2, zorder=2))
        ax.text(x0 + (j + 1) * dx, y0 - i * dy, v if v else "–",
                color=AMBER if hl else GREY, fontsize=11, ha="center", va="center")
ax.text(0, -2.30, "$V^2$ cells, blanks included\nsymmetric, because undirected",
        color=GREY, fontsize=9.8, ha="center", va="top")
ax.set_title("adjacency matrix — a 2D array", color=GREY, pad=8, fontsize=12)
ax.set_xlim(-3.2, 3.6); ax.set_ylim(-3.7, 2.2)

# the dictionary
ax = axes[2]
lines = ['graph = {',
         '  "A": {"B": 5, "C": 2},',
         '  "B": {"A": 5, "C": 3, "D": 4},',
         '  "C": {"A": 2, "B": 3, "D": 7},',
         '  "D": {"B": 4, "C": 7},',
         '}']
for k, ln in enumerate(lines):
    ax.text(-2.9, 1.55 - k * 0.62, ln, color=GREY, fontsize=10.3,
            family="monospace", ha="left")
for k in (2, 3):                                   # the B and C lines
    y = 1.55 - k * 0.62
    ax.annotate("", xy=(-3.0, y), xytext=(-3.75, y),
                arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=1.8))
ax.text(-3.8, 1.55 - 2.5 * 0.62, "the B–C edge,\nonce per side", color=AMBER,
        fontsize=9.6, ha="right", va="center")
ax.text(0, -2.30, "only real edges stored — the same\nB–C edge appears twice, once per side",
        color=GREY, fontsize=9.8, ha="center", va="top")
ax.set_title("adjacency list — a dictionary of neighbours", color=GREY, pad=8,
             fontsize=12)
ax.set_xlim(-6.0, 3.2); ax.set_ylim(-3.7, 2.2)

for ax in axes:
    ax.set_aspect("equal")
    ax.axis("off")

fig.suptitle("the same graph, stored both ways — the highlighted cell IS the highlighted edge",
             color=GREY, fontsize=13, y=0.985)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig("graphs-matrix-vs-list.svg", transparent=True, metadata={"Date": None})
plt.close(fig)

# consistency assertions: matrix mirrors the edge dict exactly
idx = {l: i for i, l in enumerate(order)}
for (a, b), w in W.items():
    assert M[idx[a]][idx[b]] == str(w) and M[idx[b]][idx[a]] == str(w), (a, b)
blank = sum(1 for i in range(4) for j in range(4) if M[i][j] == "")
assert blank == 16 - 2 * len(W)
print("matrix matches edge list; both SVGs written.")
