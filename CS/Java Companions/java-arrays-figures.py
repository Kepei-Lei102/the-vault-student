"""Figure for [[Java Arrays and ArrayList]].

Regenerate:  python3 java-arrays-figures.py
  java-arrays-list-shift.svg   what add(index, obj) and remove(index) do to the indices of everything after them
Vault palette: all text #888, transparent background.
"""
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

AX, BLUE, PURPLE, GREEN, RED, AMBER = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"
RGBA = {BLUE: (37/255, 99/255, 235/255, 0.13), GREEN: (5/255, 150/255, 105/255, 0.2), RED: (220/255, 38/255, 38/255, 0.15), AMBER: (245/255, 158/255, 11/255, 0.2)}
plt.rcParams.update({"text.color": AX, "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s); plt.close(fig)


def row(ax, y, items, cols, label, code):
    ax.text(-0.3, y + 0.35, label, ha="right", va="center", fontsize=12.5)
    ax.text(-0.3, y - 0.05, code, ha="right", va="center", fontsize=12, family="monospace", color=PURPLE)
    for k, (it, col) in enumerate(zip(items, cols)):
        ax.add_patch(FancyBboxPatch((k * 1.15, y), 1.0, 0.7, boxstyle="round,pad=0.02,rounding_size=0.08", fc=RGBA[col], ec=col, lw=1.8))
        ax.text(k * 1.15 + 0.5, y + 0.35, it, ha="center", va="center", fontsize=13, family="monospace")
        ax.text(k * 1.15 + 0.5, y - 0.22, str(k), ha="center", va="center", fontsize=11)


def fig_shift():
    fig, ax = plt.subplots(figsize=(11.5, 5.4))
    ax.set_xlim(-4.2, 5.2); ax.set_ylim(-0.6, 4.6); ax.axis("off")
    row(ax, 3.6, ["Ada", "Bob", "Cyd"], [BLUE] * 3, "start", "size() = 3")
    row(ax, 2.2, ["Ada", "Dee", "Bob", "Cyd"], [BLUE, GREEN, AMBER, AMBER], "insert at 1", 'add(1, "Dee")')
    row(ax, 0.8, ["Dee", "Bob", "Cyd"], [AMBER, AMBER, AMBER], "remove index 0", "remove(0)  returns \"Ada\"")
    for k in (1, 2):
        ax.add_patch(FancyArrowPatch((k * 1.15 + 0.5, 3.55), ((k + 1) * 1.15 + 0.5, 2.95), arrowstyle="-|>", mutation_scale=12, lw=1.5, color=AMBER))
    for k in (1, 2, 3):
        ax.add_patch(FancyArrowPatch((k * 1.15 + 0.5, 2.15), ((k - 1) * 1.15 + 0.5, 1.55), arrowstyle="-|>", mutation_scale=12, lw=1.5, color=AMBER))
    ax.text(0.2, -0.5, "amber: an element whose index changed.  A note saying \"index 2\" now points at someone else.", fontsize=12.5)
    save(fig, "java-arrays-list-shift.svg")


if __name__ == "__main__":
    fig_shift()
