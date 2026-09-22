"""Figure for [[Java Control Flow]].

Regenerate:  python3 java-control-flow-figures.py
  java-control-flow-for-order.svg   the order in which the three parts of a for header and the body run
Vault palette: all text #888, transparent background.
"""
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

AX, BLUE, PURPLE, GREEN, RED, AMBER = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"
plt.rcParams.update({"text.color": AX, "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})
RGBA = {BLUE: (37/255, 99/255, 235/255, 0.13), PURPLE: (124/255, 58/255, 237/255, 0.13), GREEN: (5/255, 150/255, 105/255, 0.13),
        AMBER: (245/255, 158/255, 11/255, 0.16), RED: (220/255, 38/255, 38/255, 0.12)}


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s); plt.close(fig)


def box(ax, x, y, w, h, col, title, code):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc=RGBA[col], ec=col, lw=2))
    ax.text(x + w / 2, y + h * 0.68, title, ha="center", va="center", fontsize=12)
    ax.text(x + w / 2, y + h * 0.28, code, ha="center", va="center", fontsize=14, family="monospace")


def arrow(ax, p, q, col=AX, rad=0.0, label=None, lpos=None):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=18, lw=2, color=col, connectionstyle=f"arc3,rad={rad}", shrinkA=3, shrinkB=3))
    if label:
        ax.text(lpos[0], lpos[1], label, ha="center", va="center", fontsize=12, color=col)


def fig_for():
    fig, ax = plt.subplots(figsize=(11.5, 5.2))
    ax.set_xlim(0, 12.1); ax.set_ylim(0, 5.6); ax.axis("off")
    ax.text(6, 5.25, "for (int i = 0;  i < 4;  i++) { body }", ha="center", va="center", fontsize=16, family="monospace")
    box(ax, 0.2, 2.9, 3.0, 1.3, BLUE, "1  initialise, once", "int i = 0")
    box(ax, 4.2, 2.9, 3.2, 1.3, AMBER, "2  test, before every pass", "i < 4")
    box(ax, 8.6, 2.9, 3.2, 1.3, GREEN, "3  the body", "{ ... }")
    box(ax, 8.6, 0.4, 3.2, 1.3, PURPLE, "4  update, after the body", "i++")
    box(ax, 4.2, 0.4, 3.2, 1.3, RED, "the loop is over", "i no longer exists")
    arrow(ax, (3.2, 3.55), (4.2, 3.55))
    arrow(ax, (7.4, 3.55), (8.6, 3.55), GREEN, label="true", lpos=(8.0, 3.85))
    arrow(ax, (10.2, 2.9), (10.2, 1.7))
    arrow(ax, (8.6, 1.05), (6.9, 2.9), PURPLE, label="back to the test", lpos=(8.75, 2.25))
    arrow(ax, (5.2, 2.9), (5.2, 1.7), RED, label="false", lpos=(4.72, 2.3))
    ax.text(1.7, 1.2, "the test runs 5 times,\nthe body 4 times", ha="center", va="center", fontsize=12.5)
    save(fig, "java-control-flow-for-order.svg")


if __name__ == "__main__":
    fig_for()
