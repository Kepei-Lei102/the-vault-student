"""Figures for Newton's Law of Restitution (vault style: #888 text, semantic
colors, transparent background, verified on light and dark).

Run from this folder:  python3 restitution-figures.py
Outputs: restitution-direct-impact.svg, restitution-oblique.svg

Fig 1 (two rows): the direct-impact machine — before/after with the sign
convention — above the drop test, whose bounce heights are drawn to the true
e^2 scaling (e = 0.7, asserted).
Fig 2 (two rows): oblique sphere-sphere impact with the line-of-centres
component split, above the oblique wall rebound tan(beta) = e tan(alpha),
angles drawn from computed vectors, never guessed.

Tofu list: no \\tfrac, \\vec, \\to, \\Rightarrow, \\perp, \\propto, \\leq,
\\circ, literal arrows.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Arc

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


def ball(ax, xy, r, color, label=None, z=5):
    rgb = tuple(int(color[i:i + 2], 16) / 255 for i in (1, 3, 5))
    ax.add_patch(Circle(xy, r, facecolor=rgb + (0.20,), edgecolor=color,
                        lw=1.7, zorder=z))
    if label:
        ax.text(*xy, label, color=GREY, fontsize=11, ha="center", va="center",
                zorder=z + 1)


def arrow(ax, a, b, color, lw=2.0, z=6):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", color=color,
                                 lw=lw, mutation_scale=14, zorder=z))


# ============================ Fig 1: the machine + the drop test ============================
fig = plt.figure(figsize=(10.6, 8.0))
gs = fig.add_gridspec(2, 1, height_ratios=[0.95, 1.05])
ax1, ax2 = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])

# ---- top: before / after with the sign convention ----
ax = ax1
# positive direction banner
arrow(ax, (-4.3, 2.05), (-2.6, 2.05), GREY, lw=1.6)
ax.text(-2.45, 2.05, "positive direction — chosen ONCE, used in BOTH equations",
        color=GREY, fontsize=9.8, va="center")

ax.text(-4.6, 1.05, "before", color=GREY, fontsize=11)
ball(ax, (-2.9, 0.55), 0.42, BLUE, "$m_1$")
arrow(ax, (-2.35, 0.55), (-1.15, 0.55), BLUE)
ax.text(-1.7, 0.92, "$u_1$", color=BLUE, fontsize=12)
ball(ax, (0.6, 0.55), 0.42, TEAL, "$m_2$")
arrow(ax, (1.15, 0.55), (1.85, 0.55), TEAL)
ax.text(1.55, 0.92, "$u_2$", color=TEAL, fontsize=12)
ax.text(3.05, 0.55, "approach speed\n$u_1 - u_2$", color=AMBER, fontsize=10,
        va="center")

ax.text(-4.6, -0.75, "after", color=GREY, fontsize=11)
ball(ax, (-2.0, -1.25), 0.42, BLUE, "$m_1$")
arrow(ax, (-1.45, -1.25), (-0.75, -1.25), BLUE)
ax.text(-1.15, -0.88, "$v_1$", color=BLUE, fontsize=12)
ball(ax, (1.4, -1.25), 0.42, TEAL, "$m_2$")
arrow(ax, (1.95, -1.25), (3.15, -1.25), TEAL)
ax.text(2.5, -0.88, "$v_2$", color=TEAL, fontsize=12)
ax.text(3.6, -1.25, "separation speed\n$v_2 - v_1$", color=AMBER, fontsize=10,
        va="center")

ax.text(0.0, -2.35,
        "momentum:  $m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2$        "
        "NEL:  $v_2 - v_1 = e\\,(u_1 - u_2)$",
        color=GREY, fontsize=11.5, ha="center")
ax.set_xlim(-5.4, 6.2); ax.set_ylim(-2.9, 2.5)
ax.set_title("direct impact — two equations, two unknowns, one sign convention",
             color=GREY, pad=8, fontsize=12)

# ---- bottom: the drop test, true e^2 scaling ----
ax = ax2
E = 0.7
h0 = 3.0
heights = [h0 * E ** (2 * k) for k in range(4)]
assert np.isclose(heights[1] / heights[0], E ** 2)
xs = [-4.2, -1.6, 0.55, 2.3]
ax.plot([-5.2, 5.6], [0, 0], color=GREY, lw=2.0)
# drop line
ax.plot([xs[0], xs[0]], [0.06, heights[0]], color=BLUE, lw=1.6, ls=(0, (4, 3)))
ball(ax, (xs[0], heights[0] + 0.16), 0.16, BLUE)
ax.text(xs[0] - 0.32, heights[0] / 2, "$h_0$", color=BLUE, fontsize=12,
        ha="right")
# bounce arcs
for k in range(1, 4):
    x_prev, x_here = xs[k - 1], xs[k]
    tt = np.linspace(0, 1, 60)
    xarc = x_prev + (x_here - x_prev) * tt
    yarc = heights[k] * 4 * tt * (1 - tt)          # parabola peaking at h_k
    ax.plot(xarc, yarc, color=AMBER, lw=1.8)
    ax.plot([ (x_prev+x_here)/2 ]*2, [0.05, heights[k]], color=GREY, lw=0.8,
            ls=":", alpha=0.7)
    ax.text((x_prev + x_here) / 2 + 0.12, heights[k] + 0.14,
            f"$e^{{{2*k}}}h_0$", color=AMBER, fontsize=10.5)
ax.text(4.0, 1.9, "heights shrink by $e^2$\nevery bounce, so\n$e = \\sqrt{h_1/h_0}$",
        color=GREY, fontsize=11)
ax.text(-5.1, 2.7, "the drop test (drawn to scale, $e = 0.7$)", color=GREY,
        fontsize=10.5)
ax.set_xlim(-5.4, 6.2); ax.set_ylim(-0.5, 3.6)
ax.set_title("the wall case — rebound speed $e\\,v$, so rebound height $e^2 h$",
             color=GREY, pad=8, fontsize=12)

for ax in (ax1, ax2):
    ax.set_aspect("equal")
    ax.axis("off")
fig.suptitle("Newton's experimental law — the materials' contribution to every collision",
             color=GREY, fontsize=13, y=0.985)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig("restitution-direct-impact.svg", transparent=True, metadata={"Date": None})
plt.close(fig)


# ============================ Fig 2: oblique — spheres, then the wall ============================
fig = plt.figure(figsize=(10.6, 8.6))
gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.0])
ax1, ax2 = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])

# ---- top: two spheres at the moment of contact ----
ax = ax1
cA, cB = np.array([-0.85, 0.0]), np.array([0.85, 0.0])
ball(ax, cA, 0.85, BLUE, "$A$")
ball(ax, cB, 0.85, TEAL, "$B$")
ax.plot([-4.6, 4.6], [0, 0], color=GREY, lw=1.2, ls=(0, (5, 3)))
ax.text(4.7, 0, "line of centres", color=GREY, fontsize=10.5, va="center")
# A's incoming velocity at angle alpha, decomposed (arrives from lower-left)
al = np.radians(35)
vend = np.array([-1.85, -0.40])                # just left-below sphere A
vstart = vend - 2.6 * np.array([np.cos(al), np.sin(al)])
arrow(ax, tuple(vstart), tuple(vend), GREY, lw=2.2)
# components: along the line of centres (amber), perpendicular to it (green)
arrow(ax, tuple(vstart), (vend[0], vstart[1]), AMBER, lw=1.8)
arrow(ax, (vend[0], vstart[1]), tuple(vend), GREEN, lw=1.8)
ax.text((vstart[0] + vend[0]) / 2 - 0.15, vstart[1] - 0.62,
        "along the line of centres:\nthe machine runs here",
        color=AMBER, fontsize=9.8, ha="center")
ax.text(vend[0] + 0.18, (vstart[1] + vend[1]) / 2 + 0.05,
        "perpendicular:\nsmooth = untouched", color=GREEN, fontsize=9.8, va="center")
ax.add_patch(Arc(tuple(vstart), 1.5, 1.5, theta1=0, theta2=np.degrees(al),
                 color=GREY, lw=1.0))
ax.text(vstart[0] + 0.92, vstart[1] + 0.26, "$\\alpha$", color=GREY, fontsize=11)
ax.text(1.3, -2.55, 'the word "smooth" is load-bearing: no friction means no force\n'
                  'perpendicular to the line of centres — that component cannot change',
        color=GREY, fontsize=10, ha="center")
ax.set_xlim(-5.4, 6.2); ax.set_ylim(-3.2, 1.6)
ax.set_title("oblique sphere impact — resolve at the moment of contact",
             color=GREY, pad=8, fontsize=12)

# ---- bottom: the wall rebound, angles computed ----
ax = ax2
E = 0.55
ax.plot([-5.0, 5.8], [0, 0], color=GREY, lw=2.5)
for xw in np.arange(-4.8, 5.7, 0.55):
    ax.plot([xw, xw - 0.28], [0, -0.28], color=GREY, lw=0.8, alpha=0.6)
P = np.array([0.0, 0.0])
al = np.radians(50)                       # angle to the WALL, incoming
vin = 3.2
inc_start = P + vin * np.array([-np.cos(al), np.sin(al)])   # from upper-left
arrow(ax, tuple(inc_start), tuple(P), BLUE, lw=2.2)
# outgoing: parallel component preserved, perpendicular scaled by e
v_par, v_perp = vin * np.cos(al), E * vin * np.sin(al)
out_end = P + np.array([v_par, v_perp])
arrow(ax, tuple(P), tuple(out_end), AMBER, lw=2.2)
be = np.arctan2(v_perp, v_par)
assert np.isclose(np.tan(be), E * np.tan(al))
ax.add_patch(Arc(tuple(P), 2.1, 2.1, theta1=180 - np.degrees(al), theta2=180,
                 color=BLUE, lw=1.1))
# (incoming arrow now arrives from above the wall, matching the arc)
ax.add_patch(Arc(tuple(P), 2.4, 2.4, theta1=0, theta2=np.degrees(be),
                 color=AMBER, lw=1.1))
ax.text(-1.5, 0.42, "$\\alpha$", color=BLUE, fontsize=12)
ax.text(1.45, 0.24, "$\\beta$", color=AMBER, fontsize=12)
ax.text(-4.8, 2.45, "in at $\\alpha$ (to the wall)", color=BLUE, fontsize=10.5)
ax.text(2.2, 2.45, "out at $\\beta$:  $\\tan\\beta = e\\tan\\alpha$",
        color=AMBER, fontsize=10.5)
ax.text(0.3, -1.15, "parallel component kept — perpendicular reversed and scaled by $e$\n"
                    f"(drawn to scale, $e = {E}$: the rebound hugs the wall)",
        color=GREY, fontsize=10, ha="center")
ax.set_xlim(-5.4, 6.2); ax.set_ylim(-1.8, 3.2)
ax.set_title("the cushion shot — why the ball comes off flatter than it went in",
             color=GREY, pad=8, fontsize=12)

for ax in (ax1, ax2):
    ax.set_aspect("equal")
    ax.axis("off")
fig.suptitle("oblique impact — one new idea, and it is the word smooth",
             color=GREY, fontsize=13, y=0.985)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig("restitution-oblique.svg", transparent=True, metadata={"Date": None})
plt.close(fig)

print("both SVGs written; e^2 ladder and tan(beta) = e tan(alpha) asserted.")
