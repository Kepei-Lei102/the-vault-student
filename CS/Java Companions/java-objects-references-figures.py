"""Figures for [[Java Objects, References and Strings]].

Regenerate:  python3 java-objects-references-figures.py
  java-references-copy-and-alias.svg   copying an int copies the value; copying a reference gives one object two names
  java-references-string-cuts.svg      the indices of "computer" as cuts between characters, so substring(3, 6) is "put"
Vault palette: all text #888, transparent background.
"""
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

AX, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": AX, "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})
MONO = {"family": "monospace"}


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s); plt.close(fig)


def var(ax, x, y, name, content=None, col=BLUE):
    """A variable: a small box with its name on the left.  Returns the point an arrow should start from."""
    ax.add_patch(FancyBboxPatch((x, y), 1.0, 0.62, boxstyle="round,pad=0.02,rounding_size=0.06", fc=(37/255, 99/255, 235/255, 0.12), ec=col, lw=1.8))
    ax.text(x - 0.14, y + 0.31, name, ha="right", va="center", fontsize=14, **MONO)
    if content is not None:
        ax.text(x + 0.5, y + 0.31, content, ha="center", va="center", fontsize=14, **MONO)
    else:
        ax.plot(x + 0.5, y + 0.31, "o", color=col, ms=7)
    return (x + 0.5, y + 0.31)


def obj(ax, x, y, label, count, col=GREEN, faded=False):
    a = 0.06 if faded else 0.14
    ax.add_patch(FancyBboxPatch((x, y), 2.4, 0.9, boxstyle="round,pad=0.02,rounding_size=0.1", fc=(5/255, 150/255, 105/255, a), ec=col, lw=1.8, ls="--" if faded else "-"))
    ax.text(x + 1.2, y + 1.12, label, ha="center", va="center", fontsize=12)
    ax.text(x + 1.2, y + 0.45, f"count  {count}", ha="center", va="center", fontsize=14, **MONO)
    return (x, y + 0.45)


def arrow(ax, p, q, col=BLUE, rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=18, lw=2, color=col, connectionstyle=f"arc3,rad={rad}", shrinkA=4, shrinkB=3))


def fig_alias():
    fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.3))
    for ax in axes:
        ax.set_xlim(-0.9, 5.7); ax.set_ylim(-0.6, 4.0); ax.axis("off"); ax.set_aspect("equal")
    ax = axes[0]
    ax.text(2.2, 3.55, "int q = p;   q++;", ha="center", fontsize=14, **MONO)
    var(ax, 0.3, 2.0, "p", "5"); var(ax, 0.3, 0.8, "q", "6")
    ax.text(2.2, -0.2, "the value was copied: two boxes, two numbers", ha="center", fontsize=12)
    ax = axes[1]
    ax.text(2.2, 3.55, "Counter b = a;   b.click();", ha="center", fontsize=14, **MONO)
    pa = var(ax, 0.3, 2.0, "a"); pb = var(ax, 0.3, 0.8, "b")
    o = obj(ax, 3.0, 1.25, "a Counter object", 1)
    arrow(ax, pa, (o[0], o[1] + 0.2), rad=-0.15); arrow(ax, pb, (o[0], o[1] - 0.2), rad=0.15)
    ax.text(2.2, -0.2, "the reference was copied: two names, one object", ha="center", fontsize=12)
    ax = axes[2]
    ax.text(2.2, 3.55, "b = new Counter(99);", ha="center", fontsize=14, **MONO)
    pa = var(ax, 0.3, 2.1, "a"); pb = var(ax, 0.3, 0.5, "b")
    o1 = obj(ax, 3.0, 1.95, "the first object", 1); o2 = obj(ax, 3.0, 0.35, "a new object", 99, col=AMBER)
    arrow(ax, pa, o1); arrow(ax, pb, o2, col=AMBER)
    ax.text(2.2, -0.2, "b was re-pointed; a never noticed", ha="center", fontsize=12)
    save(fig, "java-references-copy-and-alias.svg")


def fig_cuts():
    fig, ax = plt.subplots(figsize=(10.4, 3.5))
    ax.set_xlim(-1.2, 9.0); ax.set_ylim(-1.75, 2.25); ax.axis("off")
    word = "computer"
    for i, ch in enumerate(word):
        inside = 3 <= i < 6
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, fc=(245/255, 158/255, 11/255, 0.22) if inside else (37/255, 99/255, 235/255, 0.08), ec=AX, lw=1.4))
        ax.text(i + 0.5, 0.5, ch, ha="center", va="center", fontsize=22, **MONO)
        ax.text(i + 0.5, 1.28, str(i), ha="center", va="center", fontsize=13)
    ax.text(-0.4, 1.28, "index of each character", ha="right", va="center", fontsize=11.5)
    for k in range(9):
        ax.plot([k, k], [-0.34, -0.05], color=AX, lw=1.2)
        ax.text(k, -0.62, str(k), ha="center", va="center", fontsize=13, color=AMBER if k in (3, 6) else AX)
    ax.text(-0.4, -0.62, "the same numbers, read as cuts", ha="right", va="center", fontsize=11.5)
    ax.annotate("", xy=(6, -1.05), xytext=(3, -1.05), arrowprops=dict(arrowstyle="<->", color=AMBER, lw=2))
    ax.text(4.5, -1.45, 's.substring(3, 6)  is  "put":  cut at 3, cut at 6, and  6 − 3 = 3  characters', ha="center", va="center", fontsize=13)
    ax.text(4.0, 1.95, 'String s = "computer";      s.length() is 8, and 8 is a legal cut but not a legal character', ha="center", va="center", fontsize=12.5)
    save(fig, "java-references-string-cuts.svg")


if __name__ == "__main__":
    fig_alias(); fig_cuts()
