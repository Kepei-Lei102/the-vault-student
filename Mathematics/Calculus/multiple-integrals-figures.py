"""Figures for [[Multiple Integrals]].

Regenerate:  python3 multiple-integrals-figures.py
  multiple-integrals-columns.svg       columns under z = 4 - x^2 - y^2 on the unit square, 4 x 4 and 10 x 10
  multiple-integrals-two-orders.svg    one triangular region swept by vertical strips and by horizontal strips
  multiple-integrals-polar-patch.svg   the polar grid, and why a patch has area r dr dtheta
  multiple-integrals-jacobian.svg      a grid of unit squares in (u, v) and its image in (x, y): every cell is halved
Vault palette: all text #888, transparent background.
"""
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Wedge

AX, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX, "xtick.color": AX, "ytick.color": AX,
                     "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s); plt.close(fig)


def bare(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def fig_columns():
    fig = plt.figure(figsize=(12, 5.2))
    for k, n in enumerate((4, 10)):
        ax = fig.add_subplot(1, 2, k + 1, projection="3d")
        c = (np.arange(n) + 0.5) / n
        X, Y = np.meshgrid(c, c); H = 4 - X**2 - Y**2
        ax.bar3d((X - 0.5 / n).ravel(), (Y - 0.5 / n).ravel(), 0, 1 / n, 1 / n, H.ravel(), color=(37/255, 99/255, 235/255, 0.35), edgecolor=BLUE, linewidth=0.5, shade=False)
        ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlim(0, 4.2); ax.view_init(24, -58)
        ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1]); ax.set_zticks([0, 2, 4])
        for a in (ax.xaxis, ax.yaxis, ax.zaxis):
            a.pane.set_alpha(0); a.line.set_color(AX); a._axinfo["grid"]["color"] = (0.53, 0.53, 0.53, 0.3)
        total = H.sum() / n**2
        ax.set_title(f"{n} × {n} columns:  total {total:.4f}", color=AX, fontsize=13, pad=0)
    fig.text(0.5, 0.02, "each column: height f(x, y) × base ΔA.   Exact volume 10/3 = 3.3333…", ha="center", fontsize=13)
    save(fig, "multiple-integrals-columns.svg")


def fig_orders():
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5))
    tri = [(0, 0), (1, 1), (0, 1)]
    for ax in axes:
        ax.add_patch(Polygon(tri, closed=True, fc=(37/255, 99/255, 235/255, 0.10), ec=BLUE, lw=2))
        ax.plot([0, 1.08], [0, 1.08], color=AX, lw=1, ls=":"); ax.text(1.02, 0.94, "y = x", fontsize=12)
        ax.set_xlim(-0.12, 1.3); ax.set_ylim(-0.12, 1.25); ax.set_aspect("equal"); bare(ax)
        ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel("x"); ax.set_ylabel("y", rotation=0, labelpad=10)
    ax = axes[0]; xs = 0.38
    ax.add_patch(Polygon([(xs - 0.035, xs - 0.035), (xs + 0.035, xs + 0.035), (xs + 0.035, 1), (xs - 0.035, 1)], closed=True, fc=(245/255, 158/255, 11/255, 0.45), ec=AMBER, lw=1.5))
    ax.plot([xs], [xs], "o", color=RED, ms=7); ax.plot([xs], [1], "o", color=GREEN, ms=7)
    ax.text(xs + 0.08, xs - 0.07, "enters at y = x", fontsize=12, color=RED); ax.text(xs + 0.06, 1.05, "leaves at y = 1", fontsize=12, color=GREEN)
    ax.set_title("vertical strips:  x fixed, y runs first", color=AX, fontsize=13)
    ax.text(0.6, -0.42, "inner: y from x to 1      outer: x from 0 to 1", fontsize=13, ha="center")
    ax = axes[1]; ys = 0.62
    ax.add_patch(Polygon([(0, ys - 0.035), (ys - 0.035, ys - 0.035), (ys + 0.035, ys + 0.035), (0, ys + 0.035)], closed=True, fc=(124/255, 58/255, 237/255, 0.40), ec=PURPLE, lw=1.5))
    ax.plot([0], [ys], "o", color=RED, ms=7); ax.plot([ys], [ys], "o", color=GREEN, ms=7)
    ax.text(0.03, ys + 0.08, "enters at x = 0", fontsize=12, color=RED); ax.text(ys + 0.06, ys - 0.03, "leaves at x = y", fontsize=12, color=GREEN)
    ax.set_title("horizontal strips:  y fixed, x runs first", color=AX, fontsize=13)
    ax.text(0.6, -0.42, "inner: x from 0 to y      outer: y from 0 to 1", fontsize=13, ha="center")
    save(fig, "multiple-integrals-two-orders.svg")


def fig_polar():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.4))
    ax = axes[0]
    for rr in np.arange(0.5, 3.01, 0.5):
        ax.add_patch(plt.Circle((0, 0), rr, fill=False, ec=AX, lw=0.8, alpha=0.6))
    for th in np.arange(0, 360, 15):
        ax.plot([0, 3 * np.cos(np.radians(th))], [0, 3 * np.sin(np.radians(th))], color=AX, lw=0.8, alpha=0.6)
    ax.add_patch(Wedge((0, 0), 1.0, 30, 45, width=0.5, fc=(37/255, 99/255, 235/255, 0.55), ec=BLUE, lw=1.5))
    ax.add_patch(Wedge((0, 0), 3.0, 30, 45, width=0.5, fc=(245/255, 158/255, 11/255, 0.55), ec=AMBER, lw=1.5))
    ax.set_xlim(-0.05, 3.15); ax.set_ylim(-0.05, 3.15); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("same dr, same dθ:  the outer patch is 3.7 times the area", color=AX, fontsize=13)
    ax = axes[1]
    r0, dr, t0, dt = 2.0, 0.9, 25, 28
    ax.add_patch(Wedge((0, 0), r0 + dr, t0, t0 + dt, width=dr, fc=(5/255, 150/255, 105/255, 0.25), ec=GREEN, lw=2))
    for th in (t0, t0 + dt):
        ax.plot([0, (r0 + dr + 0.3) * np.cos(np.radians(th))], [0, (r0 + dr + 0.3) * np.sin(np.radians(th))], color=AX, lw=1)
    ax.add_patch(Wedge((0, 0), 0.7, t0, t0 + dt, width=0.001, ec=AX, fill=False, lw=1)); ax.text(0.95, 0.62, "dθ", fontsize=14)
    m = np.radians(t0 - 4)
    ax.annotate("", xy=((r0 + dr) * np.cos(m), (r0 + dr) * np.sin(m)), xytext=(r0 * np.cos(m), r0 * np.sin(m)), arrowprops=dict(arrowstyle="<->", color=BLUE, lw=2))
    ax.text((r0 + dr / 2) * np.cos(m) + 0.05, (r0 + dr / 2) * np.sin(m) - 0.28, "dr", fontsize=15, color=BLUE)
    ax.text(0.95, 1.28, "r dθ", fontsize=15, color=AMBER)
    arc = np.radians(np.linspace(t0, t0 + dt, 30)); ax.plot(r0 * np.cos(arc), r0 * np.sin(arc), color=AMBER, lw=3)
    ax.annotate("", xy=(r0 * np.cos(np.radians(t0)) * 0.98, r0 * np.sin(np.radians(t0)) * 0.98), xytext=(0, 0), arrowprops=dict(arrowstyle="-", color=AX, lw=0))
    ax.text(0.95, 0.18, "r", fontsize=14)
    ax.text(1.75, -0.45, "area ≈ (r dθ) × dr  =  r dr dθ", fontsize=14, ha="center")
    ax.set_xlim(-0.2, 3.4); ax.set_ylim(-0.7, 2.9); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("one patch: nearly a rectangle, sides dr and r dθ", color=AX, fontsize=13)
    save(fig, "multiple-integrals-polar-patch.svg")


def fig_jacobian():
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.2))
    T = lambda U, V: ((U + V) / 2, (U - V) / 2)
    us, vs = np.arange(1, 3.01, 0.5), np.arange(-1, 1.01, 0.5)
    ax = axes[0]
    for uu in us: ax.plot([uu, uu], [-1, 1], color=BLUE, lw=1.2)
    for vv in vs: ax.plot([1, 3], [vv, vv], color=PURPLE, lw=1.2)
    ax.add_patch(Polygon([(2, 0), (2.5, 0), (2.5, 0.5), (2, 0.5)], closed=True, fc=(245/255, 158/255, 11/255, 0.6), ec=AMBER))
    ax.set_xlim(0.5, 3.5); ax.set_ylim(-1.5, 1.5); ax.set_aspect("equal"); bare(ax); ax.set_xlabel("u = x + y"); ax.set_ylabel("v = x − y")
    ax.set_title("in (u, v): a rectangle, area 4", color=AX, fontsize=13)
    ax = axes[1]
    for uu in us:
        p, q = T(uu, -1), T(uu, 1); ax.plot([p[0], q[0]], [p[1], q[1]], color=BLUE, lw=1.2)
    for vv in vs:
        p, q = T(1, vv), T(3, vv); ax.plot([p[0], q[0]], [p[1], q[1]], color=PURPLE, lw=1.2)
    ax.add_patch(Polygon([T(2, 0), T(2.5, 0), T(2.5, 0.5), T(2, 0.5)], closed=True, fc=(245/255, 158/255, 11/255, 0.6), ec=AMBER))
    ax.set_xlim(-0.5, 2.5); ax.set_ylim(-0.5, 2.5); ax.set_aspect("equal"); bare(ax); ax.set_xlabel("x"); ax.set_ylabel("y", rotation=0, labelpad=10)
    ax.set_title("in (x, y): a diamond, area 2", color=AX, fontsize=13)
    fig.text(0.5, -0.07, "every cell shrinks by the same factor |J| = 1/2, so  dx dy = ½ du dv", ha="center", fontsize=13.5)
    save(fig, "multiple-integrals-jacobian.svg")


if __name__ == "__main__":
    fig_columns(); fig_orders(); fig_polar(); fig_jacobian()
