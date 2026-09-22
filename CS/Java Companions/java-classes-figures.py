"""Figure for [[Java Classes]].

Regenerate:  python3 java-classes-figures.py
  java-classes-scope.svg   two BankAccount objects, the one class variable they share, and the local variables of a method call
Vault palette: all text #888, transparent background.
"""
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

AX, BLUE, PURPLE, GREEN, RED, AMBER = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b"
RGBA = {BLUE: (37/255, 99/255, 235/255, 0.12), PURPLE: (124/255, 58/255, 237/255, 0.12), GREEN: (5/255, 150/255, 105/255, 0.12), AMBER: (245/255, 158/255, 11/255, 0.15)}
plt.rcParams.update({"text.color": AX, "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})
MONO = {"family": "monospace"}


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s); plt.close(fig)


def box(ax, x, y, w, h, col, title, lines, mono_lines=True):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc=RGBA[col], ec=col, lw=2))
    ax.text(x + w / 2, y + h - 0.32, title, ha="center", va="center", fontsize=12.5, color=col)
    for k, l in enumerate(lines):
        ax.text(x + 0.25, y + h - 0.75 - 0.4 * k, l, ha="left", va="center", fontsize=12.5, **(MONO if mono_lines else {}))


def fig_scope():
    fig, ax = plt.subplots(figsize=(11.5, 5.6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis("off")
    box(ax, 0.3, 3.3, 3.8, 2.4, GREEN, "the class   (one copy)", ["static accountsOpened = 2", "static final OVERDRAFT_FEE", "", "the methods' code"])
    box(ax, 4.5, 3.3, 3.4, 2.4, BLUE, "object 1   (ada)", ["owner = \"Ada\"", "balance = 100.0", "withdrawals = 0"])
    box(ax, 8.2, 3.3, 3.4, 2.4, BLUE, "object 2   (bob)", ["owner = \"Bob\"", "balance = 0.0", "withdrawals = 0"])
    box(ax, 4.5, 0.3, 7.1, 2.3, AMBER, "one call:  ada.withdraw(30.0)   (lives only while the call runs)",
        ["this  ->  object 1", "amount = 30.0       (a parameter is a local variable)", "", "in reach: class variables, this object's fields, these locals"])
    ax.add_patch(FancyArrowPatch((6.2, 2.6), (6.1, 3.3), arrowstyle="-|>", mutation_scale=16, lw=2, color=PURPLE))
    ax.text(0.3, 2.45, "class scope", fontsize=12.5, color=GREEN); ax.text(0.3, 2.1, "shared by every object; reached\nthrough the class name", fontsize=11.5, va="top")
    ax.text(0.3, 1.15, "instance scope", fontsize=12.5, color=BLUE); ax.text(0.3, 0.8, "one copy per object; the method\nsees the copy belonging to this", fontsize=11.5, va="top")
    save(fig, "java-classes-scope.svg")


if __name__ == "__main__":
    fig_scope()
