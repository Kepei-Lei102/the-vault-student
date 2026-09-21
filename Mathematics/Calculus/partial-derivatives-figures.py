"""Figures for [[Partial Derivatives and the Gradient]].

Regenerate:  python3 partial-derivatives-figures.py
Writes, beside this file:
  partial-derivatives-slices.svg          the hill as a contour map, cut east-west and north-south through P
  partial-derivatives-gradient-field.svg  gradient arrows cross every contour at right angles; the gradient at P does not aim at the summit
  partial-derivatives-directional.svg     the slope felt at P as the walking direction turns through 360 degrees
  partial-derivatives-critical-points.svg x^3 - 3x + y^2: a minimum and a saddle, by their contours
  partial-derivatives-descent.svg         gradient descent on x^2 + 10y^2 with three step sizes
Vault palette: all text #888, transparent background, no light colormaps.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AX, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX, "xtick.color": AX, "ytick.color": AX,
                     "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})

h = lambda x, y: 400 - 0.001 * x**2 - 0.002 * y**2
PX, PY = 100.0, 50.0
GX, GY = -0.2, -0.2
LEVELS = [330, 340, 350, 360, 370, 380, 390, 399]


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    import re
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s)
    plt.close(fig)


def hill_axes(ax, labels=True):
    xs, ys = np.meshgrid(np.linspace(-260, 260, 300), np.linspace(-190, 190, 300))
    cs = ax.contour(xs, ys, h(xs, ys), levels=LEVELS, colors=AX, linewidths=1.0)
    if labels:
        ax.clabel(cs, levels=[340, 360, 380], fmt="%d m", fontsize=10, colors=AX)
    ax.plot(0, 0, marker="^", color=GREEN, ms=11)
    ax.annotate("summit 400 m", (0, 0), xytext=(-98, -20), textcoords="offset points", color=GREEN, fontsize=11)
    ax.set_aspect("equal"); ax.set_xlabel("x, metres east"); ax.set_ylabel("y, metres north")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def slices():
    fig = plt.figure(figsize=(9.2, 11.2))
    gs = fig.add_gridspec(3, 1, height_ratios=[2.1, 1, 1], hspace=0.42)
    ax = fig.add_subplot(gs[0]); hill_axes(ax)
    ax.plot([-260, 260], [PY, PY], color=BLUE, lw=2.2); ax.plot([PX, PX], [-190, 190], color=PURPLE, lw=2.2)
    ax.plot(PX, PY, "o", color=AMBER, ms=10, zorder=6)
    ax.annotate("P (100, 50), height 385 m", (PX, PY), xytext=(12, 10), textcoords="offset points", color=AMBER, fontsize=12)
    ax.annotate("walk east: y stays 50", (-255, 165), xytext=(0, 0), textcoords="offset points", color=BLUE, fontsize=11)
    ax.annotate("walk north:\nx stays 100", (PX, -185), xytext=(8, 0), textcoords="offset points", color=PURPLE, fontsize=11)
    ax.set_title("The hill seen from above, with the two walks through P", color=AX, fontsize=13)

    a1 = fig.add_subplot(gs[1]); x = np.linspace(-260, 260, 300)
    a1.plot(x, h(x, PY), color=BLUE, lw=2.4); a1.plot(PX, 385, "o", color=AMBER, ms=9, zorder=6)
    tx = np.array([PX - 90, PX + 90]); a1.plot(tx, 385 + GX * (tx - PX), color=RED, lw=2, ls="--")
    a1.annotate("slope here = ∂h/∂x = −0.2", (PX + 60, 385 + GX * 60), xytext=(6, 8), textcoords="offset points", color=RED, fontsize=12)
    a1.set_xlabel("x, metres east (y fixed at 50)"); a1.set_ylabel("height, m")
    a1.set_title("The east–west cut is an ordinary curve of one variable", color=AX, fontsize=13)

    a2 = fig.add_subplot(gs[2]); y = np.linspace(-190, 190, 300)
    a2.plot(y, h(PX, y), color=PURPLE, lw=2.4); a2.plot(PY, 385, "o", color=AMBER, ms=9, zorder=6)
    ty = np.array([PY - 90, PY + 90]); a2.plot(ty, 385 + GY * (ty - PY), color=RED, lw=2, ls="--")
    a2.annotate("slope here = ∂h/∂y = −0.2", (PY + 60, 385 + GY * 60), xytext=(6, 8), textcoords="offset points", color=RED, fontsize=12)
    a2.set_xlabel("y, metres north (x fixed at 100)"); a2.set_ylabel("height, m")
    a2.set_title("So is the north–south cut", color=AX, fontsize=13)
    for a in (a1, a2):
        for s in ("top", "right"):
            a.spines[s].set_visible(False)
    save(fig, "partial-derivatives-slices.svg")


def gradient_field():
    fig, ax = plt.subplots(figsize=(9.2, 7.2)); hill_axes(ax, labels=False)
    gx, gy = np.meshgrid(np.arange(-200, 201, 100), np.arange(-150, 151, 75))
    u, v = -0.002 * gx, -0.004 * gy
    ax.quiver(gx, gy, u, v, color=TEAL, angles="xy", scale_units="xy", scale=0.016, width=0.0045)
    ax.quiver([PX], [PY], [GX], [GY], color=RED, angles="xy", scale_units="xy", scale=0.0055, width=0.008, zorder=7)
    ax.plot([PX, 0], [PY, 0], color=GREEN, lw=1.8, ls="--")
    ax.plot(PX, PY, "o", color=AMBER, ms=10, zorder=8)
    ax.set_ylim(-190, 262)
    ax.text(-255, 248, "Every gradient arrow crosses its contour at a right angle", color=AX, fontsize=13, va="top")
    ax.text(-255, 226, "red: ∇h at P = (−0.2, −0.2), the steepest way up, due south-west", color=RED, fontsize=12, va="top")
    ax.text(-255, 205, "green dashes: the straight line from P to the summit, 18° away from ∇h", color=GREEN, fontsize=12, va="top")
    save(fig, "partial-derivatives-gradient-field.svg")


def directional():
    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    th = np.linspace(0, 360, 721); d = GX * np.cos(np.radians(th)) + GY * np.sin(np.radians(th))
    ax.plot(th, d, color=BLUE, lw=2.6); ax.axhline(0, color=AX, lw=1)
    m = np.hypot(GX, GY)
    for ang, val, col, text, off in [(225, m, RED, "along ∇h: +0.283, the steepest climb", (-150, 8)), (45, -m, PURPLE, "against ∇h: −0.283, the steepest way down", (12, -4)),
                                     (135, 0, GREEN, "along the contour: 0", (-128, 10)), (315, 0, GREEN, "along the contour: 0", (-140, 10)),
                                     (0, GX, AMBER, "east: −0.2", (8, 8)), (90, GY, AMBER, "north: −0.2", (8, -18))]:
        ax.plot(ang, val, "o", color=col, ms=9, zorder=6)
        ax.annotate(text, (ang, val), xytext=off, textcoords="offset points", color=col, fontsize=11)
    ax.set_xticks(range(0, 361, 45)); ax.set_xlim(0, 360); ax.set_ylim(-0.36, 0.36)
    ax.set_xlabel("walking direction at P, degrees anticlockwise from east"); ax.set_ylabel("slope felt, metres up per metre walked")
    ax.set_title("One point, every direction: the slope is |∇h| cos θ", color=AX, fontsize=13)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "partial-derivatives-directional.svg")


def critical_points():
    fig, ax = plt.subplots(figsize=(9.2, 6.2))
    xs, ys = np.meshgrid(np.linspace(-2.3, 2.3, 400), np.linspace(-2.0, 2.0, 400)); f = xs**3 - 3 * xs + ys**2
    ax.contour(xs, ys, f, levels=[-1.8, -1.2, -0.4, 0.6, 1.4, 2.6, 3.6, 5.0], colors=AX, linewidths=1.0, linestyles="solid")
    ax.contour(xs, ys, f, levels=[2.0], colors=RED, linewidths=2.0)
    ax.plot(1, 0, "o", color=GREEN, ms=11, zorder=6); ax.plot(-1, 0, "X", color=RED, ms=12, zorder=6)
    ax.set_ylim(-2.0, 3.05)
    ax.text(-2.25, 2.98, "f = x³ − 3x + y²: both partial derivatives vanish at two points", color=AX, fontsize=13, va="top")
    ax.text(-2.25, 2.70, "green dot: minimum at (1, 0), f = −2; the contours close round it", color=GREEN, fontsize=12, va="top")
    ax.text(-2.25, 2.44, "red cross: saddle at (−1, 0), f = 2; the contour f = 2 (red) crosses itself there", color=RED, fontsize=12, va="top")
    ax.text(-2.25, 2.18, "blue arrows: f rises along y", color=BLUE, fontsize=12, va="top")
    ax.text(0.15, 2.18, "purple arrows: f falls along x", color=PURPLE, fontsize=12, va="top")
    ax.annotate("", (-1, 0.75), (-1, 0.2), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2)); ax.annotate("", (-1, -0.75), (-1, -0.2), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
    ax.annotate("", (-1.55, 0), (-1.12, 0), arrowprops=dict(arrowstyle="->", color=PURPLE, lw=2)); ax.annotate("", (-0.45, 0), (-0.88, 0), arrowprops=dict(arrowstyle="->", color=PURPLE, lw=2))
    ax.set_aspect("equal"); ax.set_xlabel("x"); ax.set_ylabel("y")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "partial-derivatives-critical-points.svg")


def descent():
    fig, axes = plt.subplots(3, 1, figsize=(9.2, 10.4))
    xs, ys = np.meshgrid(np.linspace(-11, 11, 300), np.linspace(-3.2, 3.2, 300)); f = xs**2 + 10 * ys**2
    for ax, eta, col, note in zip(axes, (0.02, 0.09, 0.11), (BLUE, AMBER, RED),
                                  ("step 0.02: safe and slow; after 30 steps still 2.9 from the bottom",
                                   "step 0.09: y is multiplied by −0.8 each step, so it zigzags, and arrives",
                                   "step 0.11: y is multiplied by −1.2 each step, so it flies apart")):
        ax.contour(xs, ys, f, levels=[1, 5, 15, 35, 65, 100], colors=AX, linewidths=0.9)
        p = np.array([10.0, 1.0]); path = [p.copy()]
        for _ in range(30):
            p = p - eta * np.array([2 * p[0], 20 * p[1]]); path.append(p.copy())
        path = np.array(path); keep = np.abs(path[:, 1]) < 3.2
        ax.plot(path[keep, 0], path[keep, 1], "-o", color=col, lw=1.6, ms=4)
        ax.plot(0, 0, marker="*", color=GREEN, ms=14); ax.set_xlim(-11, 11); ax.set_ylim(-3.2, 3.2)
        ax.set_title(note, color=col, fontsize=12, loc="left"); ax.set_ylabel("y")
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axes[-1].set_xlabel("x      (f = x² + 10y², a long narrow valley; start at (10, 1); each dot is one step against the gradient)")
    fig.tight_layout()
    save(fig, "partial-derivatives-descent.svg")


if __name__ == "__main__":
    slices(); gradient_field(); directional(); critical_points(); descent()
    print("wrote 5 SVGs")
