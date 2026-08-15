"""Figures for the Determinants and Inverses card.

Regenerate:  python3 determinant-figures.py
Writes determinant-area-derivation.svg, determinant-sign-and-collapse.svg and
determinant-minors-crossout.svg beside this file.

Figure 1 — the bounding-box derivation of ad - bc (a=3, c=1, b=1, d=2, det = 5).
Figure 2 — three panels: det = 2 (area doubled), det = -1 (flipped),
det = 0 (collapsed). An "F" glyph rides along because a letter is the
cheapest orientation detector: a mirrored F is unmistakable.
Figure 3 — three minors of the worked-example matrix, each as a strike-out:
the deleted row and column in red, the surviving 2x2 boxed in blue.

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


def origin_axes(ax, o_dx=-0.12, o_dy=-0.14):
    """House rule: bold lines on x = 0 and y = 0, labelled O at the origin."""
    ax.axhline(0, color=AX, lw=1.6, zorder=1)
    ax.axvline(0, color=AX, lw=1.6, zorder=1)
    ax.text(o_dx, o_dy, "$O$", color=AX, fontsize=12, ha="right", va="top")


def poly(ax, pts, face, edge=None, lw=1.4, ls="-", z=2):
    ax.add_patch(Polygon(pts, closed=True, facecolor=face,
                         edgecolor=edge if edge else "none", lw=lw, ls=ls, zorder=z))


def arrow(ax, p, q, color, lw=2.0, z=5, style="-|>", ms=16):
    ax.add_patch(FancyArrowPatch(p, q, color=color, lw=lw, zorder=z,
                                 arrowstyle=style, mutation_scale=ms,
                                 shrinkA=0, shrinkB=0))


# ---------------------------------------------------------------- figure 1
def fig_area_derivation():
    a, c = 3.0, 1.0     # first column  (a, c)
    b, d = 1.0, 2.0     # second column (b, d)

    fig, ax = plt.subplots(figsize=(8.6, 6.4))
    ax.set_xlim(-0.55, 4.55)
    ax.set_ylim(-0.55, 3.75)
    ax.set_aspect("equal")
    ax.axis("off")
    origin_axes(ax)

    # bounding rectangle (a+b) x (c+d)
    ax.add_patch(Polygon([(0, 0), (a + b, 0), (a + b, c + d), (0, c + d)],
                         closed=True, facecolor="none", edgecolor=AX,
                         lw=1.2, ls=(0, (5, 4)), zorder=2))

    # the parallelogram itself
    poly(ax, [(0, 0), (a, c), (a + b, c + d), (b, d)],
         (124/255, 58/255, 237/255, 0.15), edge=PURPLE, lw=2.0, z=3)

    # leftovers: two ac/2 triangles (blue), two bc rectangles (red), two bd/2 (teal)
    leftovers = [
        ([(0, 0), (a, 0), (a, c)], BLUE),                              # T1
        ([(a + b, c + d), (b, c + d), (b, d)], BLUE),                  # T1 mirrored
        ([(a, 0), (a + b, 0), (a + b, c), (a, c)], RED),               # R1
        ([(0, c + d), (0, d), (b, d), (b, c + d)], RED),               # R1 mirrored
        ([(a, c), (a + b, c), (a + b, c + d)], TEAL),                  # T2
        ([(0, 0), (b, d), (0, d)], TEAL),                              # T2 mirrored
    ]
    rgba = {BLUE: (37/255, 99/255, 235/255, 0.13),
            RED: (220/255, 38/255, 38/255, 0.13),
            TEAL: (8/255, 145/255, 178/255, 0.13)}
    for pts, col in leftovers:
        p = Polygon(pts, closed=True, facecolor=rgba[col], edgecolor=col,
                    lw=0.9, zorder=2)
        ax.add_patch(p)

    # region labels
    ax.text(2.35, 0.30, r"$\frac{1}{2}ac$", color=BLUE, fontsize=12, ha="center")
    ax.text(1.70, 2.62, r"$\frac{1}{2}ac$", color=BLUE, fontsize=12, ha="center")
    ax.text(3.50, 0.46, r"$bc$", color=RED, fontsize=12, ha="center")
    ax.text(0.50, 2.46, r"$bc$", color=RED, fontsize=12, ha="center")
    ax.text(3.72, 1.78, r"$\frac{1}{2}bd$", color=TEAL, fontsize=12, ha="center")
    ax.text(0.27, 1.22, r"$\frac{1}{2}bd$", color=TEAL, fontsize=12, ha="center")
    ax.text(2.0, 1.52, r"$ad - bc$", color=PURPLE, fontsize=15, ha="center",
            va="center", fontweight="bold")

    # the two column vectors
    arrow(ax, (0, 0), (a, c), BLUE, lw=2.4, z=6)
    arrow(ax, (0, 0), (b, d), TEAL, lw=2.4, z=6)
    ax.text(1.62, 0.78, r"$\binom{a}{c}$", color=BLUE, fontsize=13, ha="center")
    ax.text(0.86, 1.06, r"$\binom{b}{d}$", color=TEAL, fontsize=13, ha="center")

    # bounding-box dimension labels
    ax.text(2.0, 3.42, r"$a + b$", color=AX, fontsize=11.5, ha="center")
    ax.text(4.28, 1.5, r"$c + d$", color=AX, fontsize=11.5, va="center")

    ax.set_title("why $ad - bc$:  the bounding box, minus the leftovers",
                 color=AX, fontsize=13, pad=14)
    fig.text(0.5, 0.035,
             r"$(a+b)(c+d) \;-\; 2\,bc \;-\; ac \;-\; bd \;=\; ad - bc$",
             color=AX, fontsize=12.5, ha="center")
    fig.tight_layout(rect=[0, 0.06, 1, 1])
    fig.savefig("determinant-area-derivation.svg", transparent=True,
                bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- figure 2
F_GLYPH = np.array([
    (0.25, 0.10), (0.45, 0.10), (0.45, 0.42), (0.62, 0.42), (0.62, 0.58),
    (0.45, 0.58), (0.45, 0.70), (0.72, 0.70), (0.72, 0.88), (0.25, 0.88),
])
SQUARE = np.array([(0, 0), (1, 0), (1, 1), (0, 1)])


def draw_panel(ax, M, face_col, title, note):
    ax.set_xlim(-0.55, 3.65)
    ax.set_ylim(-0.62, 1.95)
    ax.set_aspect("equal")
    ax.axis("off")
    origin_axes(ax, o_dx=-0.10, o_dy=-0.12)

    # original square + F, ghosted
    ax.add_patch(Polygon(SQUARE, closed=True, facecolor="none", edgecolor=AX,
                         lw=1.1, ls=(0, (4, 3)), zorder=2))
    ax.add_patch(Polygon(F_GLYPH, closed=True, facecolor="none", edgecolor=AX,
                         lw=1.0, ls=(0, (2, 2)), zorder=2))

    img_sq = SQUARE @ M.T
    img_f = F_GLYPH @ M.T
    r, g, bl = tuple(int(face_col[i:i+2], 16) for i in (1, 3, 5))
    if abs(np.linalg.det(M)) > 1e-9:
        ax.add_patch(Polygon(img_sq, closed=True,
                             facecolor=(r/255, g/255, bl/255, 0.12),
                             edgecolor=face_col, lw=2.0, zorder=3))
        ax.add_patch(Polygon(img_f, closed=True,
                             facecolor=(r/255, g/255, bl/255, 0.30),
                             edgecolor=face_col, lw=1.2, zorder=4))
    else:
        # the collapse: every image point lies on one segment
        s = img_sq  # endpoints of the crushed square
        tvals = s[:, 0]
        lo, hi = s[np.argmin(tvals)], s[np.argmax(tvals)]
        ax.plot([lo[0], hi[0]], [lo[1], hi[1]], color=AMBER, lw=5.0,
                zorder=3, solid_capstyle="round", alpha=0.85)
        tf = img_f[:, 0]
        flo, fhi = img_f[np.argmin(tf)], img_f[np.argmax(tf)]
        ax.plot([flo[0], fhi[0]], [flo[1], fhi[1]], color=face_col, lw=7.0,
                zorder=4, solid_capstyle="round", alpha=0.9)
    ax.set_title(title, color=AX, fontsize=11.5, pad=10)
    ax.text(1.85, -0.52, note, color=AX, fontsize=9.8, ha="center")


def fig_sign_and_collapse():
    fig, axes = plt.subplots(1, 3, figsize=(12.8, 4.5))
    draw_panel(axes[0], np.array([[2.0, 1.0], [0.0, 1.0]]), GREEN,
               r"$\det = 2$  —  area doubled",
               "the F is sheared and stretched, but still reads as an F")
    draw_panel(axes[1], np.array([[0.0, 1.0], [1.0, 0.0]]), RED,
               r"$\det = -1$  —  area kept, plane flipped",
               "same square back — but the F is written mirror-wise")
    draw_panel(axes[2], np.array([[1.0, 2.0], [0.5, 1.0]]), RED,
               r"$\det = 0$  —  collapsed",
               "the whole plane lands on one line: no undo exists")
    fig.suptitle("the determinant: area scale factor, with a sign — "
                 "and zero is the point of no return",
                 color=AX, fontsize=12.5, y=0.045)
    fig.tight_layout(rect=[0, 0.08, 1, 1])
    fig.savefig("determinant-sign-and-collapse.svg", transparent=True,
                bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- figure 3
A_ENTRIES = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]


def draw_minor_panel(ax, i, j, value_text):
    """3x3 grid of A; strike row i and column j (1-based); box the survivors."""
    ax.set_xlim(-0.9, 2.9)
    ax.set_ylim(-1.15, 2.75)
    ax.set_aspect("equal")
    ax.axis("off")
    # brackets
    for x, sgn in ((-0.62, 1), (2.62, -1)):
        ax.plot([x, x], [-0.5, 2.5], color=AX, lw=1.6)
        ax.plot([x, x + sgn * 0.14], [2.5, 2.5], color=AX, lw=1.6)
        ax.plot([x, x + sgn * 0.14], [-0.5, -0.5], color=AX, lw=1.6)
    # survivors highlighted first (under the text)
    for r in range(3):
        for c in range(3):
            if r != i - 1 and c != j - 1:
                ax.add_patch(Polygon([(c - 0.34, 2 - r - 0.34), (c + 0.34, 2 - r - 0.34),
                                      (c + 0.34, 2 - r + 0.34), (c - 0.34, 2 - r + 0.34)],
                                     closed=True, facecolor=(37/255, 99/255, 235/255, 0.16),
                                     edgecolor=BLUE, lw=1.2, zorder=2))
    # the strike-out
    ax.plot([-0.5, 2.5], [2 - (i - 1)] * 2, color=RED, lw=3.2, alpha=0.55, zorder=3)
    ax.plot([j - 1] * 2, [-0.5, 2.5], color=RED, lw=3.2, alpha=0.55, zorder=3)
    # entries
    for r in range(3):
        for c in range(3):
            struck = (r == i - 1) or (c == j - 1)
            ax.text(c, 2 - r, str(A_ENTRIES[r][c]), color=RED if struck else BLUE,
                    fontsize=15, ha="center", va="center", zorder=4,
                    alpha=0.9 if struck else 1.0,
                    fontweight="normal" if struck else "bold")
    ax.set_title(f"strike row {i} and column {j}", color=AX, fontsize=11.5, pad=8)
    ax.text(1.0, -0.92, value_text, color=BLUE, fontsize=12, ha="center")


def fig_minors_crossout():
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.1))
    draw_minor_panel(axes[0], 1, 1, r"$M_{11} = 1\times 0 - 4\times 6 = -24$")
    draw_minor_panel(axes[1], 2, 3, r"$M_{23} = 1\times 6 - 2\times 5 = -4$")
    draw_minor_panel(axes[2], 3, 2, r"$M_{32} = 1\times 4 - 3\times 0 = 4$")
    fig.suptitle("a minor is what survives the strike-out — "
                 "the $2\\times2$ determinant of the four entries left standing",
                 color=AX, fontsize=12.5, y=0.045)
    fig.tight_layout(rect=[0, 0.08, 1, 1])
    fig.savefig("determinant-minors-crossout.svg", transparent=True,
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
    fig_area_derivation()
    fig_sign_and_collapse()
    fig_minors_crossout()
    for f in ("determinant-area-derivation.svg", "determinant-sign-and-collapse.svg",
              "determinant-minors-crossout.svg"):
        responsive(f)
    # minors sanity: every 2x2 the figure claims
    A = np.array(A_ENTRIES)
    for (i, j) in ((1, 1), (2, 3), (3, 2)):
        sub = np.delete(np.delete(A, i - 1, 0), j - 1, 1)
        print(f"M{i}{j} =", int(round(np.linalg.det(sub))))
    # numeric sanity: the derivation figure's numbers
    a, c, b, d = 3, 1, 1, 2
    print("det =", a*d - b*c, "; box - leftovers =",
          (a+b)*(c+d) - 2*b*c - a*c - b*d)
