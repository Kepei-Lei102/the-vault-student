"""Figures for [[Vector Calculus]].

Regenerate:  python3 vector-calculus-figures.py
  vector-calculus-three-fields.svg   spreading, rotating and shearing fields, with their divergence and curl
  vector-calculus-cancelling.svg     Green's theorem: circulations round small cells add up; interior edges cancel, the rim survives
  vector-calculus-flux-bag.svg       the divergence theorem in one picture: a closed surface, outward tiles, and the sources inside
Vault palette: all text #888, transparent background.
"""
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

AX, BLUE, PURPLE, GREEN, RED, AMBER, TEAL = "#888888", "#2563eb", "#7c3aed", "#059669", "#dc2626", "#f59e0b", "#0891b2"
plt.rcParams.update({"text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX, "xtick.color": AX, "ytick.color": AX,
                     "font.size": 13, "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault"})


def save(fig, name):
    fig.savefig(name, format="svg", transparent=True, bbox_inches="tight")
    s = open(name, encoding="utf-8").read()
    s = re.sub(r'<svg ([^>]*?)width="[^"]*" height="[^"]*"', r'<svg \1width="100%"', s, count=1)
    open(name, "w", encoding="utf-8").write(s); plt.close(fig)


def fig_three():
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.6))
    g = np.linspace(-1, 1, 7); X, Y = np.meshgrid(g, g)
    fields = [("spreading   F = (x, y)", X, Y, "div F = 2,   curl F = 0", BLUE),
              ("rotating   G = (−y, x)", -Y, X, "div G = 0,   curl G = 2", PURPLE),
              ("shearing   H = (y, 0)", Y, 0 * X, "div H = 0,   curl H = −1", AMBER)]
    for ax, (title, U, V, sub, col) in zip(axes, fields):
        ax.quiver(X, Y, U, V, color=col, angles="xy", scale_units="xy", scale=3.2, width=0.007)
        ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.85, 1.35); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values(): s.set_alpha(0.3)
        ax.set_title(title, color=col, fontsize=13); ax.text(0, -1.62, sub, ha="center", fontsize=12.5)
    fig.text(0.5, -0.03, "a tiny paddle wheel would sit still in the first, spin anticlockwise in the second, and spin clockwise in the third, wherever it is put", ha="center", fontsize=12.5)
    save(fig, "vector-calculus-three-fields.svg")


def fig_cancel():
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.2))
    n = 3
    for ax in axes:
        ax.set_xlim(-0.55, n + 0.55); ax.set_ylim(-0.6, n + 0.5); ax.set_aspect("equal"); ax.axis("off")
    ax = axes[0]
    for r in range(n):
        for c in range(n):
            x0, y0 = c, r; pts = [(x0 + 0.12, y0 + 0.12), (x0 + 0.88, y0 + 0.12), (x0 + 0.88, y0 + 0.88), (x0 + 0.12, y0 + 0.88)]
            for p, q in zip(pts, pts[1:] + pts[:1]):
                ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=10, lw=1.6, color=PURPLE, shrinkA=0, shrinkB=0))
    for k in range(n + 1):
        ax.plot([k, k], [0, n], color=AX, lw=0.8, alpha=0.5); ax.plot([0, n], [k, k], color=AX, lw=0.8, alpha=0.5)
    ax.set_title("walk anticlockwise round every small cell", color=AX, fontsize=13)
    ax.text(n / 2, -0.42, "each cell's circulation ≈ curl × its area", ha="center", fontsize=12.5)
    ax = axes[1]
    for k in range(n + 1):
        ax.plot([k, k], [0, n], color=AX, lw=0.8, alpha=0.25); ax.plot([0, n], [k, k], color=AX, lw=0.8, alpha=0.25)
    # interior edges: two opposite arrows, faded
    for r in range(n):
        for c in range(1, n):
            ax.add_patch(FancyArrowPatch((c - 0.02, r + 0.2), (c - 0.02, r + 0.8), arrowstyle="-|>", mutation_scale=9, lw=1.2, color=RED, alpha=0.45))
            ax.add_patch(FancyArrowPatch((c + 0.02, r + 0.8), (c + 0.02, r + 0.2), arrowstyle="-|>", mutation_scale=9, lw=1.2, color=RED, alpha=0.45))
    for r in range(1, n):
        for c in range(n):
            ax.add_patch(FancyArrowPatch((c + 0.2, r + 0.02), (c + 0.8, r + 0.02), arrowstyle="-|>", mutation_scale=9, lw=1.2, color=RED, alpha=0.45))
            ax.add_patch(FancyArrowPatch((c + 0.8, r - 0.02), (c + 0.2, r - 0.02), arrowstyle="-|>", mutation_scale=9, lw=1.2, color=RED, alpha=0.45))
    rim = [(0, 0), (n, 0), (n, n), (0, n)]
    for p, q in zip(rim, rim[1:] + rim[:1]):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=16, lw=3, color=GREEN, shrinkA=0, shrinkB=0))
    ax.set_title("add them: every inside edge is walked both ways", color=AX, fontsize=13)
    ax.text(n / 2, -0.42, "the inside cancels; only the rim is left: circulation round the rim = total curl inside", ha="center", fontsize=12.5)
    save(fig, "vector-calculus-cancelling.svg")


def fig_bag():
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.set_xlim(-2.6, 4.4); ax.set_ylim(-2.35, 2.35); ax.set_aspect("equal"); ax.axis("off")
    th = np.linspace(0, 2 * np.pi, 200); rr = 1.45 + 0.22 * np.cos(3 * th) + 0.1 * np.sin(5 * th)
    bx, by = rr * np.cos(th), rr * np.sin(th)
    ax.fill(bx, by, color=(37/255, 99/255, 235/255, 0.08)); ax.plot(bx, by, color=BLUE, lw=2.5)
    for tt in np.linspace(0, 2 * np.pi, 14, endpoint=False):
        r0 = 1.45 + 0.22 * np.cos(3 * tt) + 0.1 * np.sin(5 * tt)
        dr = -0.66 * np.sin(3 * tt) + 0.5 * np.cos(5 * tt)
        px, py = r0 * np.cos(tt), r0 * np.sin(tt)
        tx, ty = dr * np.cos(tt) - r0 * np.sin(tt), dr * np.sin(tt) + r0 * np.cos(tt)
        nx, ny = ty, -tx; L = np.hypot(nx, ny); nx, ny = nx / L, ny / L
        ax.add_patch(FancyArrowPatch((px, py), (px + 0.45 * nx, py + 0.45 * ny), arrowstyle="-|>", mutation_scale=12, lw=1.8, color=BLUE))
    for (sx, sy, col, lab) in ((-0.6, 0.2, RED, "+"), (0.35, -0.55, RED, "+"), (-0.1, 0.75, TEAL, "−")):
        ax.add_patch(Circle((sx, sy), 0.16, fc=col, ec=col)); ax.text(sx + 0.3, sy + 0.05, "source" if lab == "+" else "sink", ha="left", va="center", fontsize=11.5)
    ax.text(0.0, -2.05, "inside: the total divergence, the sources minus the sinks", ha="center", fontsize=12.5)
    ax.text(2.35, 1.2, "outward tiles dA", fontsize=12.5, color=BLUE); ax.text(2.35, 0.85, "flux out through the skin", fontsize=12.5, color=BLUE)
    ax.text(0.9, 2.2, "what leaves through the skin equals what is made inside", ha="center", fontsize=13)
    save(fig, "vector-calculus-flux-bag.svg")


if __name__ == "__main__":
    fig_three(); fig_cancel(); fig_bag()
