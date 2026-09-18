"""
paradigms-figures.py — three figures for [[Programming Paradigms]].

  paradigms-map.svg        the four syllabus paradigms placed on one axis (how ↔ what) with each
                           one's unit of thought and its exam language
  paradigms-prolog-tree.svg   the search Prolog runs for grandparent(tom, Who): goals, bindings,
                           backtracking, two answers
  paradigms-machine.svg    the register machine's memory during the low-level run, with each
                           addressing mode's operand pointing where it reads
Vault style: text #888, no background rect, width="100%" + viewBox.
"""
import re, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
GREY = "#888888"; BLUE, RED, GREEN, AMBER, PURPLE, TEAL = "#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"
def style(ax):
    for sp in ax.spines.values(): sp.set_color(GREY)
    ax.tick_params(colors=GREY, labelcolor=GREY); ax.set_facecolor("none")
def save(fig, name):
    fig.patch.set_alpha(0); fig.savefig(name, format="svg", bbox_inches="tight", transparent=True)
    s = open(name).read().replace('<svg ', '<svg width="100%" ', 1)
    s = re.sub(r' height="[^"]*pt"', '', s, count=1); s = re.sub(r' width="[^"]*pt"', '', s, count=1)
    open(name, "w").write(s); print("wrote", name)
def box(ax, x, y, w, h, text, col, fs=8.5, mono=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc=col, ec=col, alpha=0.16, lw=0))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc="none", ec=col, lw=1.2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=GREY, family="monospace" if mono else None)

# ---------------------------------------------------------------- 1. the map
fig, ax = plt.subplots(figsize=(11, 5.2)); style(ax); ax.axis("off"); ax.set_xlim(0, 11); ax.set_ylim(0, 5.2)
ax.add_patch(FancyArrowPatch((0.6, 4.75), (10.4, 4.75), arrowstyle="<->", color=GREY, lw=1.4, mutation_scale=14))
ax.text(0.6, 4.95, "HOW — you write every step", fontsize=9, color=GREY, ha="left")
ax.text(10.4, 4.95, "WHAT — you state the result, the engine finds the steps", fontsize=9, color=GREY, ha="right")
cols = [("Low-level", BLUE, "unit of thought:\nthe instruction\nand the address", "LDX 0,IX\nSUB (12)\nJLT ADDIT", "registers, memory cells,\nfive addressing modes"),
        ("Imperative\n(procedural)", TEAL, "unit of thought:\nthe statement\nthat changes state", "for name, price in items:\n    if price < 6:\n        total += price", "variables, sequence,\nselection, iteration,\nprocedures, functions"),
        ("Object-oriented", PURPLE, "unit of thought:\nthe object — data\nwith its behaviour", "class Item:\n    def is_cheap(self):\n        return self.__price < 6", "classes, instances,\nencapsulation, inheritance,\npolymorphism, containment"),
        ("Declarative", GREEN, "unit of thought:\nthe fact, the rule,\nthe goal", "cheap(I) :- item(I, P),\n            P < 6.\n?- cheap(What).", "facts and rules;\nqueries that satisfy goals;\nSQL is one too")]
for i, (name, col, unit, code, words) in enumerate(cols):
    x = 0.5 + i * 2.65
    box(ax, x, 3.35, 2.4, 1.05, name, col, fs=11)
    ax.text(x + 1.2, 2.95, unit, ha="center", va="top", fontsize=8, color=col)
    box(ax, x, 0.95, 2.4, 1.2, code, col, fs=6.6, mono=True)
    ax.text(x + 1.2, 0.75, words, ha="center", va="top", fontsize=7.4, color=GREY)
ax.set_title("Four paradigms, one problem (add up the prices under 6): the same answer, four different things to think in", fontsize=10, color=GREY)
save(fig, "paradigms-map.svg")

# ---------------------------------------------------------------- 2. the Prolog search tree
fig, ax = plt.subplots(figsize=(11, 6)); style(ax); ax.axis("off"); ax.set_xlim(0, 11); ax.set_ylim(0, 6)
def node(x, y, text, col, w=2.6, h=0.62, fs=8):
    box(ax, x - w / 2, y - h / 2, w, h, text, col, fs=fs, mono=True)
def edge(a, b, col=GREY, text=None, dx=0.15):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", color=col, lw=1.0, mutation_scale=10))
    if text: ax.text((a[0] + b[0]) / 2 + dx, (a[1] + b[1]) / 2, text, fontsize=7.2, color=col)
node(5.5, 5.55, "?- grandparent(tom, Who).", AMBER, w=3.4)
node(5.5, 4.55, "rule: grandparent(X,Z) :- parent(X,Y), parent(Y,Z).\nunify: X = tom, Z = Who", PURPLE, w=6.2, h=0.72, fs=7.4)
node(5.5, 3.55, "goals: parent(tom, Y), parent(Y, Who)", BLUE, w=4.2)
edge((5.5, 5.24), (5.5, 4.91)); edge((5.5, 4.19), (5.5, 3.86))
node(2.6, 2.5, "parent(tom, bob)  ✓  Y = bob", GREEN, w=3.2)
node(8.4, 2.5, "parent(tom, liz)  ✓  Y = liz", GREEN, w=3.2)
edge((4.2, 3.25), (2.9, 2.81), GREEN, "first matching fact", dx=-1.9); edge((6.8, 3.25), (8.1, 2.81), RED, "backtrack: try the next fact", dx=0.1)
node(2.6, 1.55, "parent(bob, Who)", BLUE, w=2.6)
node(8.4, 1.55, "parent(liz, Who)", BLUE, w=2.6)
edge((2.6, 2.19), (2.6, 1.86)); edge((8.4, 2.19), (8.4, 1.86))
node(1.3, 0.55, "Who = ann  ✓", GREEN, w=2.0); node(3.9, 0.55, "Who = pat  ✓", GREEN, w=2.0)
node(8.4, 0.55, "no fact matches  ✗", RED, w=2.6)
edge((2.2, 1.24), (1.5, 0.86), GREEN); edge((3.0, 1.24), (3.7, 0.86), GREEN, "backtrack again", dx=0.1); edge((8.4, 1.24), (8.4, 0.86), RED)
ax.set_title("What the engine does with one goal: depth-first, left to right, backtracking to the next fact when a branch dies — two answers, in this order", fontsize=9.5, color=GREY)
save(fig, "paradigms-prolog-tree.svg")

# ---------------------------------------------------------------- 3. the machine
fig, ax = plt.subplots(figsize=(11, 4.2)); style(ax); ax.axis("off"); ax.set_xlim(0, 11); ax.set_ylim(0, 4.2)
cells = [2, 12, 1, 5, 30, 0, "", "", "", "", 5, 0, 13, 6]
labels = ["price[0]", "price[1]", "price[2]", "price[3]", "price[4]", "scratch", "", "", "", "", "counter", "total", "ptr→13", "limit"]
for i, (v, lab) in enumerate(zip(cells, labels)):
    x = 0.4 + i * 0.75
    col = AMBER if i <= 4 else (TEAL if i in (10, 11) else (PURPLE if i == 12 else (GREEN if i == 13 else GREY)))
    box(ax, x, 2.2, 0.68, 0.62, str(v), col, fs=9, mono=True)
    ax.text(x + 0.34, 2.05, str(i), ha="center", va="top", fontsize=7.5, color=GREY)
    if lab: ax.text(x + 0.34, 3.0, lab, ha="center", va="bottom", fontsize=7, color=col, rotation=45)
ax.text(0.4, 1.8, "address", fontsize=7.5, color=GREY)
# operands and where they read
ops = [("LDM #0", "immediate: the 0 is the value — reads no cell", RED, None),
       ("STO 11", "direct: cell 11", TEAL, 11),
       ("LDX 0,IX", "indexed: cell 0 + IX (IX = 3 → cell 3)", AMBER, 3),
       ("SUB (12)", "indirect: cell 12 holds 13 → reads cell 13", PURPLE, 12)]
for k, (op, why, col, cell) in enumerate(ops):
    y = 1.25 - k * 0.32
    ax.text(0.4, y, op, fontsize=8.5, color=col, family="monospace"); ax.text(2.2, y, why, fontsize=8, color=GREY)
    if cell is not None:
        ax.add_patch(FancyArrowPatch((6.9 if k == 3 else 4.2, y + 0.08), (0.4 + cell * 0.75 + 0.34, 2.18), arrowstyle="-|>", color=col, lw=0.9, mutation_scale=9, connectionstyle="arc3,rad=0.15"))
ax.add_patch(FancyArrowPatch((0.4 + 12 * 0.75 + 0.34, 2.9), (0.4 + 13 * 0.75 + 0.34, 2.9), arrowstyle="-|>", color=PURPLE, lw=1.0, mutation_scale=9, connectionstyle="arc3,rad=-0.6"))
ax.set_title("The low-level run's memory, and where each addressing mode sends the machine to look", fontsize=10, color=GREY)
save(fig, "paradigms-machine.svg")
