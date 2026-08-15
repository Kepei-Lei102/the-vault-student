"""Figures for the Invariant Points and Lines card.

Regenerate:  python3 invariant-figures.py
Writes stretch-shear-invariants.svg and invariant-lines-vs-points.svg
beside this file.

Figure 1 — stretch and shear on the unit square, with their pins (line of
invariant points) and rails (invariant lines) marked.
Figure 2 — pins vs rails on real matrices: (4 -1; 2 1) has two rails and an
escaping line; (6 5; 2 3) has a pinned line AND a rail, in one picture.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
import re

AX = "#888888"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
RED = "#dc2626"
AMBER = "#f59e0b"
TEAL = "#0891b2"

plt.rcParams.update({
    "text.color": AX,
    "axes.labelcolor": AX,
    "axes.edgecolor": AX,
    "xtick.color": AX,
    "ytick.color": AX,
    "font.size": 11,
    "font.family": "sans-serif",
    "svg.fonttype": "none",
    "svg.hashsalt": "vault",
})

SQUARE = np.array([(0, 0), (1, 0), (1, 1), (0, 1)])


def origin_axes(ax, o_dx=-0.10, o_dy=-0.12):
    """House rule: bold lines on x = 0 and y = 0, labelled O at the origin."""
    ax.axhline(0, color=AX, lw=1.6, zorder=1)
    ax.axvline(0, color=AX, lw=1.6, zorder=1)
    ax.text(o_dx, o_dy, "$O$", color=AX, fontsize=12, ha="right", va="top")


def arrow(ax, p, q, color, lw=2.0, z=6, ms=15):
    ax.add_patch(FancyArrowPatch(p, q, color=color, lw=lw, zorder=z,
                                 arrowstyle="-|>", mutation_scale=ms,
                                 shrinkA=0, shrinkB=0))


def rgba(hexcol, a):
    r, g, b = (int(hexcol[i:i+2], 16) for i in (1, 3, 5))
    return (r/255, g/255, b/255, a)


# ---------------------------------------------------------------- figure 1
def fig_stretch_shear():
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.8, 4.7))

    # ---- panel A: stretch parallel to the x-axis, factor 2 ----
    M = np.array([[2.0, 0.0], [0.0, 1.0]])
    axA.set_xlim(-0.75, 2.65)
    axA.set_ylim(-0.55, 1.75)
    axA.set_aspect("equal")
    axA.axis("off")
    origin_axes(axA)
    axA.add_patch(Polygon(SQUARE, closed=True, facecolor="none", edgecolor=AX,
                          lw=1.1, ls=(0, (4, 3)), zorder=2))
    axA.add_patch(Polygon(SQUARE @ M.T, closed=True, facecolor=rgba(BLUE, 0.12),
                          edgecolor=BLUE, lw=2.0, zorder=3))
    # pins: the y-axis is a line of invariant points
    for y in (0.25, 0.5, 0.75, 1.0, 1.25):
        axA.plot([0], [y], "o", color=AMBER, ms=6.5, zorder=7)
    axA.text(-0.13, 1.44, "pins:  $x = 0$ fixed\npoint by point", color=AMBER,
             fontsize=9.8, ha="right", va="top")
    # rails: horizontal lines slide along themselves
    for y, x0 in ((0.5, 0.55), (1.0, 0.55)):
        axA.axhline(y, color=AX, lw=0.9, ls=(0, (2, 2)), alpha=0.55, zorder=2)
        arrow(axA, (x0, y), (2*x0, y), BLUE, lw=2.0)
    axA.text(2.16, 0.62, "rails: every $y = n$\nslides onto itself", color=BLUE,
             fontsize=9.8, ha="right", va="bottom")
    axA.set_title(r"stretch  $\binom{2\ \ 0}{0\ \ 1}$:   $\det = 2$",
                  color=AX, fontsize=11.5, pad=10)

    # ---- panel B: shear, x-axis fixed, (0,1) -> (1,1) ----
    S = np.array([[1.0, 1.0], [0.0, 1.0]])
    axB.set_xlim(-0.75, 2.65)
    axB.set_ylim(-0.55, 1.75)
    axB.set_aspect("equal")
    axB.axis("off")
    origin_axes(axB)
    axB.add_patch(Polygon(SQUARE, closed=True, facecolor="none", edgecolor=AX,
                          lw=1.1, ls=(0, (4, 3)), zorder=2))
    axB.add_patch(Polygon(SQUARE @ S.T, closed=True, facecolor=rgba(PURPLE, 0.12),
                          edgecolor=PURPLE, lw=2.0, zorder=3))
    for x in (0.25, 0.5, 0.75, 1.0, 1.25):
        axB.plot([x], [0], "o", color=AMBER, ms=6.5, zorder=7)
    axB.text(1.62, -0.34, "pins: the baseline — italic text never leaves its line",
             color=AMBER, fontsize=9.8, ha="center")
    # rails slide further the higher they sit
    for y in (0.5, 1.0):
        axB.axhline(y, color=AX, lw=0.9, ls=(0, (2, 2)), alpha=0.55, zorder=2)
        arrow(axB, (0.45, y), (0.45 + y, y), PURPLE, lw=2.0)
    axB.text(2.16, 1.14, "rails slide further\nthe higher they sit", color=PURPLE,
             fontsize=9.8, ha="right", va="bottom")
    axB.set_title(r"shear  $\binom{1\ \ 1}{0\ \ 1}$:   $\det = 1$ — area unchanged",
                  color=AX, fontsize=11.5, pad=10)

    fig.suptitle("what each machine refuses to move", color=AX,
                 fontsize=12.5, y=0.045)
    fig.tight_layout(rect=[0, 0.08, 1, 1])
    fig.savefig("stretch-shear-invariants.svg", transparent=True,
                bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- figure 2
def fig_pins_vs_rails():
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.8, 5.1))

    # ---- panel A: rails of (4 -1; 2 1) ----
    axA.set_xlim(-2.1, 5.6)
    axA.set_ylim(-2.5, 4.7)
    axA.set_aspect("equal")
    axA.axis("off")
    origin_axes(axA, o_dx=-0.16, o_dy=-0.18)
    t = np.array([-1.8, 4.4])
    axA.plot(t, t, color=GREEN, lw=1.8, zorder=3)
    t2 = np.array([-1.15, 2.25])
    axA.plot(t2, 2*t2, color=TEAL, lw=1.8, zorder=3)
    t3 = np.array([-1.6, 2.4])
    axA.plot(t3, -t3, color=RED, lw=1.5, ls=(0, (5, 4)), zorder=3)
    # sliding arrows along the rails
    arrow(axA, (1, 1), (3, 3), GREEN, lw=2.2)
    arrow(axA, (1, 2), (2, 4), TEAL, lw=2.2)
    for p in ((1, 1), (1, 2), (1, -1)):
        axA.plot([p[0]], [p[1]], "o", color=AX, ms=4.5, zorder=7)
    # the escaping point of the non-invariant line
    arrow(axA, (1, -1), (5, 1), RED, lw=1.8)
    axA.text(2.55, 3.15, r"$y = x$  ($\times 3$)", color=GREEN, fontsize=10.5)
    axA.text(-0.18, 3.55, r"$y = 2x$  ($\times 2$)", color=TEAL, fontsize=10.5,
             ha="right")
    axA.text(2.55, -1.72, "$y = -x$:  $(1,-1)$ lands\nat $(5,1)$ — escapes",
             color=RED, fontsize=9.8, va="top")
    axA.set_title(r"rails of  $\binom{4\ \ {-1}}{2\ \ \ \ 1}$:"
                  "  points slide, lines stay",
                  color=AX, fontsize=11.5, pad=10)

    # ---- panel B: pins AND a rail of (6 5; 2 3) ----
    axB.set_xlim(-2.6, 4.8)
    axB.set_ylim(-2.6, 2.9)
    axB.set_aspect("equal")
    axB.axis("off")
    origin_axes(axB, o_dx=-0.16, o_dy=-0.18)
    t = np.array([-2.3, 2.3])
    axB.plot(t, -t, color=AMBER, lw=2.0, zorder=3)
    for x in (-1.8, -1.2, -0.6, 0.6, 1.2, 1.8):
        axB.plot([x], [-x], "o", color=AMBER, ms=6.0, zorder=7)
    t2 = np.array([-1.9, 4.55])
    axB.plot(t2, 0.4*t2, color=BLUE, lw=1.8, zorder=3)
    arrow(axB, (0.5, 0.2), (4, 1.6), BLUE, lw=2.2)
    axB.plot([0.5], [0.2], "o", color=AX, ms=4.5, zorder=7)
    axB.text(-2.45, -1.45, "$y = -x$ — every point fixed:\na line of invariant points",
             color=AMBER, fontsize=9.8, va="top")
    axB.text(4.6, 0.78, r"$y = \frac{2}{5}x$ — invariant line:"
             "\nslides along itself ($\\times 8$)",
             color=BLUE, fontsize=9.8, ha="right", va="top")
    axB.set_title(r"one matrix, both kinds:  $\binom{6\ \ 5}{2\ \ 3}$",
                  color=AX, fontsize=11.5, pad=10)

    fig.suptitle("pins hold every point still; rails only promise you stay on the track",
                 color=AX, fontsize=12.5, y=0.045)
    fig.tight_layout(rect=[0, 0.08, 1, 1])
    fig.savefig("invariant-lines-vs-points.svg", transparent=True,
                bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


def responsive(path):
    """Vault rule: root <svg> keeps its viewBox but scales — width 100%, no height."""
    s = open(path).read()
    s = re.sub(r'(<svg[^>]*?)\swidth="[^"]*"', r"\1", s, count=1)
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]*"', r"\1", s, count=1)
    s = s.replace("<svg ", '<svg width="100%" ', 1)
    open(path, "w").write(s)


if __name__ == "__main__":
    fig_stretch_shear()
    fig_pins_vs_rails()
    for f in ("stretch-shear-invariants.svg", "invariant-lines-vs-points.svg"):
        responsive(f)
    # numeric sanity for the arrows drawn above
    M = np.array([[4, -1], [2, 1]])
    print("M(1,1) =", M @ (1, 1), "  M(1,2) =", M @ (1, 2), "  M(1,-1) =", M @ (1, -1))
    N = np.array([[6, 5], [2, 3]])
    print("N(1,-1) =", N @ (1, -1), "  N(0.5,0.2) =", N @ (0.5, 0.2))
