"""Figure for the Roots of Polynomial Equations card — the Reed-Solomon locator.

Regenerate:  python3 reed-solomon-locator.py
Writes reed-solomon-locator.svg beside this file.

The decoder cannot see which symbols are damaged. It measures two power sums,
converts them to the elementary symmetric functions, and the quadratic built
from those has its roots exactly at the damaged positions.

Vault palette: all text #888, semi-transparent fills, transparent background.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import re

AX = "#888888"
TEAL = "#0891b2"      # data
PURPLE = "#7c3aed"    # the locator polynomial
RED = "#dc2626"       # damage
GREY = "#9ca3af"

plt.rcParams.update({
    "text.color": AX,
    "axes.labelcolor": AX,
    "axes.edgecolor": AX,
    "xtick.color": AX,
    "ytick.color": AX,
    "font.size": 11,
    "font.family": "sans-serif",
    "svg.fonttype": "none",
})

P = 11
RECEIVED = [3, 1, 5, 1, 5, 9, 3, 6, 7, 5]     # positions 3 and 7 each 1 too big
E1, E2 = 10, 10                                # from the two syndromes
LAM = [(x * x - E1 * x + E2) % P for x in range(1, 11)]
BAD = [i for i, v in enumerate(LAM, start=1) if v == 0]


def figure():
    fig, (ax0, ax1) = plt.subplots(
        2, 1, figsize=(11, 6.0), gridspec_kw={"height_ratios": [1, 2.0], "hspace": 0.30}
    )

    # ---------- top: the received block, every symbol equally suspect ----------
    ax0.set_xlim(0.3, 10.7)
    ax0.set_ylim(0.0, 1.0)
    ax0.axis("off")
    for i, v in enumerate(RECEIVED, start=1):
        flagged = i in BAD
        ax0.add_patch(FancyBboxPatch(
            (i - 0.36, 0.30), 0.72, 0.52,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=TEAL, alpha=0.15,
            edgecolor=(RED if flagged else TEAL),
            linestyle=((0, (3, 2)) if flagged else "solid"),
            linewidth=(2.0 if flagged else 1.3), zorder=2))
        ax0.text(i, 0.56, str(v), ha="center", va="center",
                 fontsize=15, color=AX, zorder=3)
        ax0.text(i, 0.95, str(i), ha="center", va="center",
                 fontsize=9.5, color=GREY)
    ax0.set_title("the block that arrived  —  ten symbols, and nothing in them "
                  "shows which two are wrong",
                  color=AX, fontsize=11.5, pad=22)

    # ---------- bottom: the locator polynomial evaluated everywhere ----------
    xs = list(range(1, 11))
    ax1.bar(xs, LAM, width=0.52, color=PURPLE, alpha=0.28,
            edgecolor=PURPLE, linewidth=1.3, zorder=2)
    ax1.axhline(0, color=AX, lw=1.2)

    for x, v in zip(xs, LAM):
        if v == 0:
            ax1.plot([x], [0], "o", color=RED, ms=11, zorder=5)
            ax1.text(x, -1.7, "0", ha="center", va="center",
                     fontsize=13, color=RED, zorder=5)
        else:
            ax1.text(x, v + 0.3, str(v), ha="center", va="bottom",
                     fontsize=10.5, color=AX)

    ax1.set_xlim(0.3, 10.7)
    ax1.set_ylim(-3.0, 12.4)
    ax1.set_xticks([])
    ax1.set_yticks([])
    for s in ("right", "top", "left", "bottom"):
        ax1.spines[s].set_visible(False)

    fig.text(0.5, 0.085,
             r"value of the locator  $x^2 + x + 10$  (mod 11)  at every position",
             color=AX, fontsize=12, ha="center", va="center")
    fig.text(0.5, 0.028,
             "Two power sums in, one quadratic out — and its roots are the damage.",
             color=AX, fontsize=12.5, ha="center", va="center")
    fig.tight_layout(rect=[0, 0.12, 1, 1])

    # each zero rises out of its own column — which is empty, so nothing is crossed
    for x in BAD:
        fig.add_artist(ConnectionPatch(
            xyA=(x, 0.9), coordsA=ax1.transData,
            xyB=(x, 0.285), coordsB=ax0.transData,
            color=RED, lw=1.4, linestyle=(0, (4, 3)), alpha=0.9,
            arrowstyle="-|>", mutation_scale=15, zorder=6))

    fig.savefig("reed-solomon-locator.svg", transparent=True, bbox_inches="tight")
    plt.close(fig)


def responsive(path):
    """Vault rule: root <svg> keeps its viewBox but scales — width 100%, no height."""
    s = open(path).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", s, count=1)
    s = s.replace("<svg ", '<svg width="100%" ', 1)
    open(path, "w").write(s)


if __name__ == "__main__":
    figure()
    responsive("reed-solomon-locator.svg")
    print("locator values:", dict(zip(range(1, 11), LAM)))
    print("zeros at:", BAD)
