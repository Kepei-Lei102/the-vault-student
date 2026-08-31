"""Figures for Centre of Mass (vault style: #888 text, semantic colors,
transparent background, verified on light and dark).

Run from this folder:  python3 centre-of-mass-figures.py
Outputs: centre-of-mass-composite.svg, centre-of-mass-topple-vs-slide.svg

Fig 1 reproduces 9231 June 2025 Paper 34 Q5 with a = 1, h = 2, drawn three
times because the published mark scheme accepts three different cuts. All
three land on the same point (14/9, 8/3) - asserted at the bottom of this file.

Tofu list (matplotlib mathtext + Helvetica Neue + cairosvg): no \\tfrac, \\vec,
\\to, \\Rightarrow, \\perp, \\propto, \\leq, \\circ (degree sign renders
as tofu - write "deg"), literal arrows.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Arc

GREY = "#888888"
BLUE = "#2563eb"
GREEN = "#059669"
AMBER = "#f59e0b"
RED = "#dc2626"
TEAL = "#0891b2"
PURPLE = "#7c3aed"

plt.rcParams.update({
    "text.color": GREY, "axes.edgecolor": GREY, "axes.labelcolor": GREY,
    "xtick.color": GREY, "ytick.color": GREY, "font.size": 11,
    "axes.titlesize": 12, "svg.fonttype": "none", "svg.hashsalt": "vault",
    "font.family": ["Helvetica Neue", "Arial", "sans-serif"],
})


def centroid(pts):
    """Centroid + signed area of a simple polygon."""
    p = np.asarray(pts, dtype=float)
    x, y = p[:, 0], p[:, 1]
    xn, yn = np.roll(x, -1), np.roll(y, -1)
    cross = x * yn - xn * y
    A = cross.sum() / 2.0
    cx = ((x + xn) * cross).sum() / (6 * A)
    cy = ((y + yn) * cross).sum() / (6 * A)
    return np.array([cx, cy]), A


# ============================ Fig 1: composite, three ways ============================
a, h = 1.0, 2.0
A_, F_, E_, D_ = (0, 0), (6 * a - h, 0), (h, 6 * a), (0, 6 * a)
G_, H_ = (h, 0), (6 * a - h, 6 * a)
TARGET, _ = centroid([A_, F_, E_, D_])

# label side: "L" parks the label left of the shape, "R" right of it
panels = [
    ("add: rectangle + triangle",
     [("rect $AGED$", [A_, G_, E_, D_], BLUE, +1, "L"),
      ("tri $GFE$", [G_, F_, E_], GREEN, +1, "R")]),
    ("add: two triangles",
     [("tri $AED$", [A_, E_, D_], BLUE, +1, "L"),
      ("tri $AEF$", [A_, E_, F_], GREEN, +1, "R")]),
    ("subtract: rectangle $-$ triangle",
     [("rect $AFHD$", [A_, F_, H_, D_], BLUE, +1, "L"),
      ("tri $EFH$ taken away", [E_, F_, H_], RED, -1, "R")]),
]

fig, axes = plt.subplots(1, 3, figsize=(12.6, 5.0))
for ax, (title, pieces) in zip(axes, panels):
    # the trapezium itself, always drawn as the outline
    ax.add_patch(Polygon([A_, F_, E_, D_], closed=True, facecolor="none",
                         edgecolor=GREY, lw=2.0, zorder=4))
    check = np.zeros(2)
    tot = 0.0
    for label, pts, colour, sign, side in pieces:
        c, area = centroid(pts)
        area = abs(area)
        rgb = tuple(int(colour[i:i + 2], 16) / 255 for i in (1, 3, 5))
        ax.add_patch(Polygon(pts, closed=True,
                             facecolor=rgb + (0.16,) if sign > 0 else "none",
                             edgecolor=colour, lw=1.5,
                             hatch=None if sign > 0 else "///",
                             ls="-" if sign > 0 else (0, (4, 2)), zorder=3))
        ax.plot(*c, marker="o", ms=6, color=colour, zorder=6)
        lx, ha = (-0.75, "right") if side == "L" else (4.75, "left")
        ax.annotate(label, xy=c, xytext=(lx, c[1]), color=colour, fontsize=10,
                    ha=ha, va="center",
                    arrowprops=dict(arrowstyle="-", color=colour, lw=0.8,
                                    shrinkA=2, shrinkB=6))
        check += sign * area * c
        tot += sign * area
    assert np.allclose(check / tot, TARGET, atol=1e-9), title

    # the answer, identical in every panel
    ax.plot(*TARGET, marker="*", ms=18, color=AMBER, zorder=7)
    ax.annotate("centre of mass\n(14/9, 8/3)", xy=TARGET,
                xytext=(2.0, -1.45), color=AMBER, fontsize=10.5, ha="center", va="top",
                arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.9,
                                shrinkA=2, shrinkB=8))

    for pt, name, dx, dy in [(A_, "$A$", -0.34, -0.42), (F_, "$F$", 0.12, -0.44),
                             (E_, "$E$", -0.05, 0.18), (D_, "$D$", -0.36, 0.16)]:
        ax.plot(*pt, marker="o", ms=3.5, color=GREY, zorder=6)
        ax.text(pt[0] + dx, pt[1] + dy, name, color=GREY, fontsize=10.5)
    ax.set_title(title, color=GREY, pad=9)
    ax.set_xlim(-3.4, 8.2)
    ax.set_ylim(-3.0, 7.2)
    ax.set_aspect("equal")
    ax.axis("off")

fig.suptitle("one shape, three legal cuts, one answer  —  the decomposition is never unique",
             color=GREY, fontsize=12.5, y=0.975)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig("centre-of-mass-composite.svg", transparent=True, metadata={"Date": None})
plt.close(fig)


# ============================ Fig 2: topple vs slide ============================
def draw_block(ax, theta_deg, w, H, mu, base_u, verdict, colour):
    th = np.radians(theta_deg)
    down = np.array([np.cos(th), -np.sin(th)])      # downhill along the plane
    norm = np.array([np.sin(th), np.cos(th)])       # out of the plane
    origin = np.array([-3.4, 1.55])

    # the incline
    surf = np.array([origin, origin + down * 7.2])
    ax.plot(surf[:, 0], surf[:, 1], color=GREY, lw=2.0, zorder=2)
    ax.plot([origin[0], origin[0] + 7.2], [origin[1], origin[1]],
            color=GREY, lw=0.9, ls=":", alpha=0.7, zorder=1)
    ax.add_patch(Arc(origin, 3.2, 3.2, theta1=-theta_deg, theta2=0,
                     color=GREY, lw=1.0))
    ax.text(origin[0] + 0.30, origin[1] - 1.30,
            f"$\\theta$ = {theta_deg:.1f} deg", color=GREY, fontsize=10.5)

    base = origin + down * base_u
    corners = [base, base + down * w, base + down * w + norm * H, base + norm * H]
    rgb = tuple(int(colour[i:i + 2], 16) / 255 for i in (1, 3, 5))
    ax.add_patch(Polygon(corners, closed=True, facecolor=rgb + (0.16,),
                         edgecolor=colour, lw=1.8, zorder=4))

    cm = base + down * (w / 2) + norm * (H / 2)
    ax.plot(*cm, marker="o", ms=7, color=AMBER, zorder=6)
    ax.text(cm[0] - 0.26, cm[1] + 0.30, "CM", color=AMBER, fontsize=11,
            ha="right", zorder=6)
    # weight line, straight down from the CM (long enough to clear the plane)
    wl = 2.5 if verdict == "topple" else 1.5
    ax.plot([cm[0], cm[0]], [cm[1], cm[1] - wl], color=AMBER, lw=1.3,
            ls=(0, (5, 3)), zorder=5)
    # park the label away from whatever else that panel puts near the base
    ldx, lha = (0.18, "left") if verdict == "topple" else (-0.16, "right")
    ax.text(cm[0] + ldx, cm[1] - wl + 0.06, "weight line", color=AMBER,
            fontsize=10, ha=lha)

    dl = base + down * w          # downhill base corner: the pivot
    ax.plot(*dl, marker="o", ms=6, color=RED if verdict == "topple" else GREY, zorder=7)
    if verdict == "topple":     # only the tipping case has a pivot worth naming
        ax.annotate("pivot edge", xy=dl, xytext=(dl[0] - 1.5, dl[1] - 0.95),
                    color=RED, fontsize=10, ha="right",
                    arrowprops=dict(arrowstyle="-", color=RED, lw=0.8,
                                    shrinkA=2, shrinkB=5))
    if verdict == "slide":
        s0 = base + down * (w + 0.35)
        ax.annotate("", xy=s0 + down * 1.5, xytext=s0,
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.0))
        ax.text(*(s0 + down * 1.7 + norm * 0.28), "slides", color=GREEN, fontsize=11)
    else:
        ax.annotate("", xy=dl + np.array([0.95, 0.62]), xytext=dl + np.array([0.25, 1.15]),
                    arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0,
                                    connectionstyle="arc3,rad=-0.45"))
        ax.text(dl[0] + 1.0, dl[1] + 0.78, "topples", color=RED, fontsize=11)
    return cm, dl


fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.3))

# (a) tall cupboard: w/H = 0.3 < mu = 0.5, so it topples first
cm, dl = draw_block(axes[0], np.degrees(np.arctan(0.3)), 0.9, 3.0, 0.5, 2.2, "topple", BLUE)
assert abs(cm[0] - dl[0]) < 1e-9, "at the critical angle the weight line hits the pivot"
axes[0].set_title("tall and narrow  ($w/H = 0.3$)", color=GREY, pad=10)
axes[0].text(-3.5, -1.62,
             "topple needs  $\\tan\\theta = w/H = 0.30$,  giving  16.7 deg\n"
             "slide needs  $\\tan\\theta = \\mu = 0.50$,  giving  26.6 deg\n"
             "16.7 deg comes first: it goes over before friction is ever beaten",
             color=GREY, fontsize=10.2, va="top")

# (b) squat crate: w/H = 1.0 > mu = 0.5, so it slides first
draw_block(axes[1], np.degrees(np.arctan(0.5)), 1.9, 1.9, 0.5, 3.3, "slide", TEAL)
axes[1].set_title("short and wide  ($w/H = 1.0$)", color=GREY, pad=10)
axes[1].text(-3.5, -1.62,
             "slide needs  $\\tan\\theta = \\mu = 0.50$,  giving  26.6 deg\n"
             "topple needs  $\\tan\\theta = w/H = 1.00$,  giving  45.0 deg\n"
             "26.6 deg comes first: it slides away and never tips",
             color=GREY, fontsize=10.2, va="top")

for ax in axes:
    ax.set_xlim(-4.6, 5.4)
    ax.set_ylim(-3.7, 5.0)
    ax.set_aspect("equal")
    ax.axis("off")

fig.suptitle("same surface, same material, opposite failure  —  the winner is whichever "
             "critical angle is smaller", color=GREY, fontsize=12.5, y=0.98)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig("centre-of-mass-topple-vs-slide.svg", transparent=True, metadata={"Date": None})
plt.close(fig)

print("centre of mass of AFED (a=1, h=2):", TARGET, " expected [14/9, 8/3] =",
      [14 / 9, 8 / 3])
print("all three decompositions agreed; both SVGs written.")
