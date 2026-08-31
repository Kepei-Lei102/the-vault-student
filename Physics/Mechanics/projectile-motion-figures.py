"""Figures for Projectile Motion (vault style: #888 text, semantic colors,
transparent background, verified on light and dark).

Run from this folder:  python3 projectile-motion-figures.py
Outputs: projectile-motion-independence.svg, projectile-motion-family.svg,
         projectile-motion-velocity.svg

Tofu list (matplotlib mathtext + Helvetica Neue + cairosvg): no \\tfrac, \\vec,
\\to, \\Rightarrow, \\perp, \\propto, literal arrows; \\varphi not \\phi.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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
    "axes.titlesize": 12, "svg.fonttype": "none",
    "font.family": ["Helvetica Neue", "Arial", "sans-serif"],
})
g = 10.0

# ---------------- Fig 1: independence strobe ----------------
fig, ax = plt.subplots(figsize=(8.6, 4.6))
h0 = 20.0
ts = np.arange(0, 2.01, 0.25)
ys = h0 - 5 * ts**2
xs_drop = np.zeros_like(ts)
vx = 7.0
xs_fly = vx * ts
tt = np.linspace(0, 2, 200)
ax.plot(vx * tt, h0 - 5 * tt**2, color=BLUE, lw=1.6, alpha=0.8)
for t, y, xf in zip(ts, ys, xs_fly):
    ax.plot([0, xf], [y, y], color=GREY, lw=0.7, ls=":", alpha=0.65)
ax.scatter(xs_drop, ys, s=46, color=RED, zorder=5, label="dropped  ($u_x = 0$)")
ax.scatter(xs_fly, ys, s=46, color=BLUE, zorder=5, label="launched sideways  ($u_x = 7$ m/s)")
ax.annotate("equal time-flashes:\nsame height, every flash", xy=(7.2, 11.5),
            xytext=(8.6, 15.5), color=GREY, fontsize=10.5,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("horizontal spacing constant:\n$v_x$ never changes", xy=(10.5, 3.5),
            xytext=(1.2, 3.2), color=GREY, fontsize=10.5,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.set_xlabel("horizontal distance / m")
ax.set_ylabel("height / m")
ax.set_title("gravity does not care about sideways — the vertical stories are identical")
ax.legend(frameon=False, loc="upper right", fontsize=9.5, labelcolor=GREY)
ax.set_xlim(-1.2, 16.5); ax.set_ylim(0, 22)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("projectile-motion-independence.svg", transparent=True)
plt.close(fig)

# ---------------- Fig 2: family + envelope + range inset ----------------
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.6),
                              gridspec_kw={"width_ratios": [1.9, 1.0]})
V = 20.0
pairs = [(15, 75, TEAL), (30, 60, BLUE)]
for a1, a2, col in pairs:
    for adeg, ls in [(a1, "-"), (a2, "--")]:
        th = np.radians(adeg)
        tf = 2 * V * np.sin(th) / g
        t = np.linspace(0, tf, 160)
        ax.plot(V * np.cos(th) * t, V * np.sin(th) * t - 5 * t**2,
                color=col, lw=1.5, ls=ls, label=f"{adeg}°")
th = np.radians(45)
tf = 2 * V * np.sin(th) / g
t = np.linspace(0, tf, 160)
ax.plot(V * np.cos(th) * t, V * np.sin(th) * t - 5 * t**2, color=GREEN, lw=2.6, label="45°")
xe = np.linspace(-0.5, 41, 200)
ax.plot(xe, V**2 / (2 * g) - g * xe**2 / (2 * V**2), color=AMBER, lw=1.4, ls=":",
        label="bounding parabola")
ax.set_xlim(0, 42); ax.set_ylim(0, 22)
ax.set_xlabel("x / m"); ax.set_ylabel("y / m")
ax.set_title("same speed, five angles — complementary pairs share a landing point")
ax.legend(frameon=False, fontsize=9, labelcolor=GREY, ncol=2)
angles = np.linspace(0, 90, 300)
ax2.plot(angles, V**2 * np.sin(np.radians(2 * angles)) / g, color=GREEN, lw=1.8)
for a1, a2, col in pairs:
    R = V**2 * np.sin(np.radians(2 * a1)) / g
    ax2.plot([a1, a2], [R, R], "o", color=col, ms=5)
    ax2.plot([a1, a2], [R, R], color=col, lw=0.8, ls=":")
ax2.axvline(45, color=GREEN, lw=0.8, ls=":")
ax2.set_xlabel("launch angle / °"); ax2.set_ylabel("range / m")
ax2.set_title("range vs angle:\n$R = V^2 \\sin 2\\theta \\, / \\, g$", fontsize=10.5)
ax2.set_xlim(0, 90); ax2.set_ylim(0, 44)
for a in (ax, ax2):
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("projectile-motion-family.svg", transparent=True)
plt.close(fig)

# ---------------- Fig 3: velocity vectors along the path ----------------
fig, ax = plt.subplots(figsize=(8.6, 4.8))
V, adeg = 20.0, 60.0
th = np.radians(adeg)
tf = 2 * V * np.sin(th) / g
t = np.linspace(0, tf, 200)
X = V * np.cos(th) * t
Y = V * np.sin(th) * t - 5 * t**2
ax.plot(X, Y, color=GREY, lw=1.2, alpha=0.8)
S = 0.22  # arrow scale (m per m/s)
for tk in np.linspace(0.12 * tf, 0.88 * tf, 5):
    x0 = V * np.cos(th) * tk
    y0 = V * np.sin(th) * tk - 5 * tk**2
    vx = V * np.cos(th)
    vy = V * np.sin(th) - g * tk
    ax.annotate("", xy=(x0 + S * vx, y0), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.8))
    if abs(vy) > 0.4:
        ax.annotate("", xy=(x0, y0 + S * vy), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", color=RED, lw=1.8))
    ax.annotate("", xy=(x0 + S * vx, y0 + S * vy), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.4, alpha=0.75))
ax.annotate("$v_x$ — identical arrow at every point", xy=(23.5, 16.2), color=BLUE, fontsize=10.5)
ax.annotate("$v_y$ — drains, empties at the top,\nrefills downward", xy=(23.5, 13.6), color=RED, fontsize=10.5)
ax.annotate("velocity — always tangent to the path", xy=(23.5, 10.6), color=GREEN, fontsize=10.5)
ax.annotate("minimum speed here:\n$|v| = V\\cos\\theta$, not zero", xy=(V*np.cos(th)*tf/2, V**2*np.sin(th)**2/(2*g)),
            xytext=(2.0, 18.6), color=GREY, fontsize=10,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.set_xlim(-1, 42); ax.set_ylim(0, 21.5)
ax.set_xlabel("x / m"); ax.set_ylabel("y / m")
ax.set_title("the horizontal shadow keeps constant pace; only the vertical part changes")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("projectile-motion-velocity.svg", transparent=True)
plt.close(fig)
print("3 figures written")

# ---------------- Question diagrams ----------------
# Q1: J26/33 Q7 — two projectiles, collision at P's apex
fig, ax = plt.subplots(figsize=(8.2, 4.4))
t = np.linspace(0, 4, 240)
X, Y = 15 * t, 20 * t - 5 * t**2
ax.plot(X, Y, color=BLUE, lw=1.8)
ax.plot([30, 30], [0, 20], color=RED, lw=1.6, ls="--")
ax.annotate("", xy=(30, 9), xytext=(30, 3),
            arrowprops=dict(arrowstyle="->", color=RED, lw=2.2))
ax.plot(0, 0, "o", color=BLUE, ms=6); ax.plot(30, 0, "o", color=RED, ms=6)
ax.plot(30, 20, "*", color=AMBER, ms=17, zorder=6)
ax.annotate("P: $25$ m/s at $\\alpha$, $\\sin\\alpha = 4/5$\nlaunched at $t = 0$", xy=(0,0),
            xytext=(0.6, 16.0), color=BLUE, fontsize=10.5,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("Q: $25$ m/s straight up\nlaunched at $t = T$", xy=(30, 4.5), xytext=(37, 6.5),
            color=RED, fontsize=10.5, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("collision: at P's greatest height,\nQ still moving upwards", xy=(30, 20),
            xytext=(35.5, 17.5), color=GREY, fontsize=10.5,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("$O$", xy=(-0.5, -2.3), color=GREY, fontsize=11)
ax.axhline(0, color=GREY, lw=1.0)
ax.set_xlim(-2, 62); ax.set_ylim(-3, 23)
ax.set_xticks([]); ax.set_yticks([])
for s in ("top", "right", "left", "bottom"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("projectile-motion-q-collision.svg", transparent=True)
plt.close(fig)

# Q2: J25/33 Q7 — 45 deg up, later 60 deg below horizontal
fig, ax = plt.subplots(figsize=(8.2, 4.2))
V, th = 20.0, np.radians(45)
tf = 2 * V * np.sin(th) / g
t = np.linspace(0, 1.32 * tf, 240)
X = V * np.cos(th) * t; Y = V * np.sin(th) * t - 5 * t**2
ax.plot(X, Y, color=BLUE, lw=1.8)
ax.annotate("", xy=(7.5, 7.5), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.0))
ax.annotate("$U$ at $45°$", xy=(6.2, 8.4), color=GREEN, fontsize=11)
tk = 1.13 * tf   # a visible point on the descending branch (schematic, not to scale)
x0 = V*np.cos(th)*tk; y0 = V*np.sin(th)*tk - 5*tk**2
L = 7.0          # drawn arrow at 60 deg below horizontal
ax.annotate("", xy=(x0 + L*0.5, y0 - L*0.866), xytext=(x0, y0),
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=2.0))
ax.plot([x0, x0 + 6.5], [y0, y0], color=GREY, lw=0.9, ls=":")
from matplotlib.patches import Arc
ax.add_patch(Arc((x0, y0), 6.4, 6.4, theta1=-60, theta2=0, color=GREY, lw=0.9))
ax.annotate("$60°$", xy=(x0 + 3.6, y0 - 2.6), color=GREY, fontsize=10.5)
ax.annotate("direction of motion at time $T$", xy=(x0 - 21.5, y0 - 4.0), color=GREEN, fontsize=10.5)
ax.plot(0, 0, "o", color=BLUE, ms=6)
ax.annotate("$O$", xy=(-1.2, -2.4), color=GREY, fontsize=11)
ax.axhline(0, color=GREY, lw=1.0)
ax.set_xlim(-2.5, 60); ax.set_ylim(-13, 13.5)
ax.set_xticks([]); ax.set_yticks([])
for s in ("top", "right", "left", "bottom"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("projectile-motion-q-direction.svg", transparent=True)
plt.close(fig)

# Q3: N25/34 Q2 — trajectory through (8,12), 7 m barrier window
fig, ax = plt.subplots(figsize=(8.6, 4.4))
x = np.linspace(0, 32, 300)
y = x * (32 - x) / 16
ax.plot(x, y, color=BLUE, lw=1.8)
ax.plot(8, 12, "o", color=GREEN, ms=7, zorder=6)
ax.annotate("passes through $(8, 12)$", xy=(8, 12), xytext=(2.0, 14.6), color=GREEN,
            fontsize=10.5, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
for D, alpha in [(28.0, 1.0), (30.5, 0.5), (32.0, 0.5)]:
    ax.plot([D, D], [0, 7], color=RED, lw=3.2 if alpha == 1.0 else 2.0, alpha=alpha)
ax.axvspan(28, 32, ymin=0.0, ymax=0.04, color=AMBER, alpha=0.8)
ax.annotate("barrier: 7 m high, at distance $D$", xy=(28, 7), xytext=(15.5, 8.9),
            color=RED, fontsize=10.5, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("hits the face only for\n$28 \\leq D \\leq 32$", xy=(30, 0.6), xytext=(24.0, 3.8),
            color=GREY, fontsize=10.5, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("$y = 7$ again at $x = 28$;\nlands at $x = 32$", xy=(28, 0.0), xytext=(4.5, 5.2),
            color=GREY, fontsize=10)
ax.axhline(0, color=GREY, lw=1.0)
ax.axhline(7, color=GREY, lw=0.7, ls=":")
ax.annotate("$y = 7$", xy=(0.4, 7.3), color=GREY, fontsize=10)
ax.plot(0, 0, "o", color=BLUE, ms=6)
ax.annotate("$O$: $u$ at $\\theta$, $\\tan\\theta = 2$", xy=(0, 0), xytext=(0.5, 1.3),
            color=BLUE, fontsize=10.5)
ax.set_xlim(-1, 37); ax.set_ylim(-1.2, 17.5)
ax.set_xticks([0, 8, 16, 28, 32]); ax.set_yticks([0, 7, 12, 16])
ax.set_xlabel("x / m"); ax.set_ylabel("y / m")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("projectile-motion-q-barrier.svg", transparent=True)
plt.close(fig)
print("3 question diagrams written")
