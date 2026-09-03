"""Figures for Centres of Mass by Integration (vault style: #888 text,
semantic colors, transparent background, verified on light and dark).

Run from this folder:  python3 com-integration-figures.py
Outputs: com-integration-laminae.svg, com-integration-solids.svg

Each panel shows the body, the SLICE the derivation uses (amber), and the
resulting centre of mass (star). CM positions are computed, not guessed,
and asserted against the closed forms at the bottom.

Tofu list: no \\tfrac, \\vec, \\to, \\Rightarrow, \\perp, \\propto, \\leq,
\\circ, literal arrows.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Wedge, Arc, Ellipse

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

BLUE_RGBA = (37 / 255, 99 / 255, 235 / 255, 0.14)
STAR = dict(marker="*", ms=17, color=AMBER, zorder=8)


def setup(ax, title):
    ax.set_title(title, color=GREY, pad=8, fontsize=11.5)
    ax.set_aspect("equal")
    ax.axis("off")


# ============================ Fig 1: laminae and curves ============================
fig = plt.figure(figsize=(10.8, 9.0))
gs = fig.add_gridspec(2, 2)
axes = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, :])]

# --- (a) triangle, strips parallel to the base -------------------------------
ax = axes[0]
h_tri = 3.4
apex = np.array([0, h_tri])
b1, b2 = np.array([-1.9, 0]), np.array([1.9, 0])
ax.add_patch(Polygon([apex, b1, b2], closed=True, facecolor=BLUE_RGBA,
                     edgecolor=BLUE, lw=1.6, zorder=2))
# the slice: a strip at depth x from the apex
x_s = 1.9                                    # depth below apex
frac = x_s / h_tri
p1 = apex + frac * (b1 - apex)
p2 = apex + frac * (b2 - apex)
th = 0.16
ax.add_patch(Polygon([p1 + [0, th], p2 + [0, th], p2 - [0, th], p1 - [0, th]],
                     closed=True, facecolor=AMBER, alpha=0.55, edgecolor=AMBER,
                     lw=1.2, zorder=4))
ax.annotate("strip at depth $x$:\nwidth grows like $x$,\nCM at its midpoint",
            xy=((p1 + p2) / 2), xytext=(2.15, 2.6), color=AMBER, fontsize=9.6,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.8, shrinkB=6))
# median + CM
mid_base = (b1 + b2) / 2
ax.plot(*zip(apex, mid_base), color=GREY, lw=1.0, ls=":", zorder=3)
cm = apex + (2 / 3) * (mid_base - apex)
assert np.isclose(cm[1], h_tri / 3)
ax.plot(*cm, **STAR)
ax.annotate("2/3 down the median", xy=cm, xytext=(-3.4, 0.55), color=AMBER,
            fontsize=10, arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.9,
                                         shrinkB=8))
ax.set_xlim(-3.7, 4.5); ax.set_ylim(-2.2, 4.4)
setup(ax, "triangle:  $dm$ grows like $x$")

# --- (b) circular arc, bead elements -----------------------------------------
ax = axes[1]
r, al = 3.0, np.radians(55)
tt = np.linspace(-al, al, 120)
ax.plot(r * np.cos(tt), r * np.sin(tt), color=BLUE, lw=3.0, zorder=3)
ax.plot([0, r * np.cos(al)], [0, r * np.sin(al)], color=GREY, lw=0.9, ls=":")
ax.plot([0, r * np.cos(al)], [0, -r * np.sin(al)], color=GREY, lw=0.9, ls=":")
ax.plot(0, 0, marker="o", ms=4, color=GREY)
ax.add_patch(Arc((0, 0), 1.7, 1.7, theta1=-np.degrees(al), theta2=np.degrees(al),
                 color=GREY, lw=1.0))
ax.text(1.06, 0.62, r"$2\alpha$", color=GREY, fontsize=11)
# bead element
tb = np.radians(30)
bead = np.array([r * np.cos(tb), r * np.sin(tb)])
ax.plot(*bead, marker="o", ms=9, color=AMBER, zorder=5)
ax.annotate(r"bead $r\,d\theta$ at $x = r\cos\theta$", xy=bead,
            xytext=(0.4, 3.15), color=AMBER, fontsize=9.6,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.8, shrinkB=7))
cm_arc = np.array([r * np.sin(al) / al, 0])
ax.plot(*cm_arc, **STAR)
ax.annotate(r"$\dfrac{r\sin\alpha}{\alpha}$", xy=cm_arc, xytext=(1.15, -1.9),
            color=AMBER, fontsize=12,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.9, shrinkB=9))
ax.set_xlim(-2.0, 6.2); ax.set_ylim(-2.9, 3.7)
setup(ax, "arc:  beads on a wire")

# --- (c) sector as a fan of thin triangles ------------------------------------
ax = axes[2]
ax.add_patch(Wedge((0, 0), r, -np.degrees(al), np.degrees(al),
                   facecolor=BLUE_RGBA, edgecolor=BLUE, lw=1.6, zorder=2))
# the fan
for tf in np.linspace(-al, al, 9):
    ax.plot([0, r * np.cos(tf)], [0, r * np.sin(tf)], color=BLUE, lw=0.6,
            alpha=0.5, zorder=3)
# one thin triangle highlighted, its CM at 2r/3
tf = np.radians(18)
dtf = np.radians(6.5)
ax.add_patch(Wedge((0, 0), r, np.degrees(tf - dtf), np.degrees(tf + dtf),
                   facecolor=AMBER, alpha=0.5, edgecolor=AMBER, lw=1.0, zorder=4))
tri_cm = (2 * r / 3) * np.array([np.cos(tf), np.sin(tf)])
ax.plot(*tri_cm, marker="o", ms=6, color=RED, zorder=6)
ax.annotate("each thin triangle:\nCM at  $2r/3$", xy=tri_cm, xytext=(0.5, 3.05),
            color=RED, fontsize=9.6,
            arrowprops=dict(arrowstyle="-", color=RED, lw=0.8, shrinkB=6))
# the equivalent arc at 2r/3
r23 = 2 * r / 3
ax.plot(r23 * np.cos(tt), r23 * np.sin(tt), color=RED, lw=1.6,
        ls=(0, (4, 3)), zorder=5)
ax.text(3.05, 0.9, "so the sector is an arc\nof radius  $2r/3$",
        color=RED, fontsize=9.6)
cm_sec = np.array([(2 * r / 3) * np.sin(al) / al, 0])
ax.plot(*cm_sec, **STAR)
ax.annotate(r"$\dfrac{2r\sin\alpha}{3\alpha}$", xy=cm_sec, xytext=(3.3, -1.9),
            color=AMBER, fontsize=12,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.9, shrinkB=9))
ax.set_xlim(-4.6, 8.8); ax.set_ylim(-2.9, 3.7)
setup(ax, "sector:  a fan of triangles — no integral")

fig.suptitle("slice so that each slice's own centre of mass is known",
             color=GREY, fontsize=12.5, y=0.985)
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig("com-integration-laminae.svg", transparent=True, metadata={"Date": None})
plt.close(fig)


# ============================ Fig 2: the solids ============================
fig = plt.figure(figsize=(10.8, 9.0))
gs = fig.add_gridspec(2, 2)
axes = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, :])]


def ellipse_disc(ax, y, half_w, color, alpha, lw=1.2, ec=None, z=4):
    ax.add_patch(Ellipse((0, y), 2 * half_w, 0.42, facecolor=color, alpha=alpha,
                         edgecolor=ec or color, lw=lw, zorder=z))


# --- (a) cone, discs ----------------------------------------------------------
ax = axes[0]
H = 3.6; Rb = 1.8
apex = np.array([0, H])
ax.plot([0, -Rb], [H, 0], color=BLUE, lw=1.6)
ax.plot([0, Rb], [H, 0], color=BLUE, lw=1.6)
ax.add_patch(Ellipse((0, 0), 2 * Rb, 0.55, facecolor=BLUE_RGBA,
                     edgecolor=BLUE, lw=1.4, zorder=2))
x_s = 2.15                                    # depth from apex
w_s = Rb * x_s / H
ellipse_disc(ax, H - x_s, w_s, AMBER, 0.55, ec=AMBER)
ax.annotate("disc at depth $x$:\nradius grows like $x$,\nmass like $x^2$",
            xy=(w_s * 0.8, H - x_s), xytext=(2.0, 2.7), color=AMBER, fontsize=9.6,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.8, shrinkB=6))
cm_y = H - 3 * H / 4
ax.plot(0, cm_y, **STAR)
ax.annotate("$3h/4$ from the vertex", xy=(0, cm_y), xytext=(-3.55, 0.35),
            color=AMBER, fontsize=10,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.9, shrinkB=8))
ax.plot([0, 0], [0, H], color=GREY, lw=0.8, ls=":")
ax.set_xlim(-3.8, 4.6); ax.set_ylim(-1.2, 4.3)
setup(ax, "cone:  mass grows like $x^2$")

# --- (b) solid hemisphere, discs ---------------------------------------------
ax = axes[1]
r = 2.6
tt = np.linspace(0, np.pi, 120)
ax.plot(r * np.cos(tt), r * np.sin(tt), color=BLUE, lw=1.6, zorder=3)
ax.add_patch(Ellipse((0, 0), 2 * r, 0.55, facecolor=BLUE_RGBA,
                     edgecolor=BLUE, lw=1.4, zorder=2))
x_s = 1.5
w_s = np.sqrt(r ** 2 - x_s ** 2)
ellipse_disc(ax, x_s, w_s, AMBER, 0.55, ec=AMBER)
ax.annotate("disc at height $x$:\nradius $\\sqrt{r^2 - x^2}$",
            xy=(w_s * 0.75, x_s), xytext=(2.05, 2.55), color=AMBER, fontsize=9.6,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.8, shrinkB=6))
ax.plot(0, 3 * r / 8, **STAR)
ax.annotate("$3r/8$", xy=(0, 3 * r / 8), xytext=(-3.3, 1.75), color=AMBER,
            fontsize=11,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.9, shrinkB=8))
ax.plot([0, 0], [0, r], color=GREY, lw=0.8, ls=":")
ax.set_xlim(-3.8, 4.6); ax.set_ylim(-2.0, 3.5)
setup(ax, "solid hemisphere:  fat discs sit low")

# --- (c) hemispherical shell, hat-box ----------------------------------------
ax = axes[2]
ax.plot(r * np.cos(tt), r * np.sin(tt), color=BLUE, lw=2.6, zorder=3)
ax.add_patch(Ellipse((0, 0), 2 * r, 0.55, facecolor="none",
                     edgecolor=BLUE, lw=1.2, ls=(0, (4, 3)), zorder=2))
# equal-height bands, equal areas: shade three bands of equal dh
band_edges = [0.20, 0.95, 1.70, 2.45]
for y0, y1 in zip(band_edges[:-1], band_edges[1:]):
    ts = np.linspace(np.arcsin(y0 / r), np.arcsin(y1 / r), 40)
    for sgn, col in ((1, TEAL),):
        xs = np.concatenate([r * np.cos(ts), -r * np.cos(ts[::-1])])
        ys = np.concatenate([r * np.sin(ts), r * np.sin(ts[::-1])])
        ax.fill(xs, ys, color=col, alpha=0.18, zorder=1)
for y in band_edges:
    w = np.sqrt(max(r ** 2 - y ** 2, 1e-9))
    ax.plot([-w, w], [y, y], color=TEAL, lw=0.9, ls=":", zorder=2)
ax.text(2.35, 1.55, "equal heights,\nequal areas\n(the hat-box theorem)",
        color=TEAL, fontsize=9.6)
ax.plot(0, r / 2, **STAR)
ax.annotate("mass uniform in height,\nso the CM is at  $r/2$", xy=(0, r / 2),
            xytext=(-3.7, -1.55), color=AMBER, fontsize=9.8,
            arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.9, shrinkB=8))
ax.set_xlim(-6.4, 7.2); ax.set_ylim(-2.0, 3.5)
setup(ax, "shell:  Archimedes beats the integral")

fig.suptitle("the solids — and the one result that needs no integral at all",
             color=GREY, fontsize=12.5, y=0.985)
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig("com-integration-solids.svg", transparent=True, metadata={"Date": None})
plt.close(fig)

# ---- assertions: closed forms vs quadrature ----
from scipy import integrate as si  # noqa: E402  (only for verification)
al_v = np.radians(55)
arc = si.quad(lambda t: np.cos(t), -al_v, al_v)[0] / (2 * al_v)
assert np.isclose(arc, np.sin(al_v) / al_v)
hemi = si.quad(lambda x: x * (1 - x ** 2), 0, 1)[0] / si.quad(lambda x: 1 - x ** 2, 0, 1)[0]
assert np.isclose(hemi, 3 / 8)
cone = si.quad(lambda x: x * x ** 2, 0, 1)[0] / si.quad(lambda x: x ** 2, 0, 1)[0]
assert np.isclose(cone, 3 / 4)
shell = si.quad(lambda t: np.cos(t) * np.sin(t), 0, np.pi / 2)[0] / si.quad(np.sin, 0, np.pi / 2)[0]
assert np.isclose(shell, 1 / 2)
print("closed forms verified by quadrature; both SVGs written.")
