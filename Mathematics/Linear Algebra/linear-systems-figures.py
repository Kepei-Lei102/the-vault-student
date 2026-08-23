"""Figures for the Linear Systems in 3D card.

Regenerate:  python3 linear-systems-figures.py
Writes, beside this file:
  linear-systems-configurations.svg — four tall panels, one per fate of three
      planes: the corner (det != 0, unique point), the sheaf (common line),
      the triangular prism (three parallel edges, no common point), and
      parallel planes. 3-D patches, axis chrome off, vault palette.

Vault palette: all text #888, transparent background, byte-stable output.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AX = "#888888"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GREEN = "#059669"
RED = "#dc2626"
AMBER = "#f59e0b"
TEAL = "#0891b2"

plt.rcParams.update({
    "text.color": AX, "axes.labelcolor": AX, "axes.edgecolor": AX,
    "xtick.color": AX, "ytick.color": AX, "font.size": 13,
    "font.family": "sans-serif", "svg.fonttype": "none", "svg.hashsalt": "vault",
})

fig = plt.figure(figsize=(8.6, 21.5))

PLANE_COLORS = [BLUE, PURPLE, TEAL]


def panel(idx, title, subtitle):
    ax = fig.add_subplot(4, 1, idx, projection="3d")
    ax.set_axis_off()
    ax.set_title(title, fontsize=16, color=AX, pad=2)
    ax.text2D(0.5, 0.94, subtitle, transform=ax.transAxes, fontsize=13,
              color=AX, ha="center")
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_zlim(-1.2, 1.2)
    return ax


def patch(ax, point, u, v, color, half=1.0):
    """Draw a plane patch centred at `point` spanned by u, v."""
    s = np.linspace(-half, half, 2)
    S, T = np.meshgrid(s, s)
    P = (np.asarray(point)[:, None, None]
         + np.asarray(u)[:, None, None] * S
         + np.asarray(v)[:, None, None] * T)
    ax.plot_surface(P[0], P[1], P[2], color=color, alpha=0.20,
                    edgecolor=color, linewidth=1.2, shade=False)


# --- Panel 1: the corner (det != 0) — three coordinate planes pin the origin
ax = panel(1, "det A ≠ 0 — the corner", "three planes pin exactly one point")
patch(ax, (0, 0, 0), (1, 0, 0), (0, 1, 0), BLUE)     # floor z = 0
patch(ax, (0, 0, 0), (0, 1, 0), (0, 0, 1), PURPLE)   # wall x = 0
patch(ax, (0, 0, 0), (1, 0, 0), (0, 0, 1), TEAL)     # wall y = 0
for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:          # the pairwise meet-lines
    d = np.asarray(d, dtype=float)
    ax.plot(*zip(-1.05 * d, 1.05 * d), color=AX, lw=1.0, alpha=0.6)
ax.scatter([0], [0], [0], color=GREEN, s=90, zorder=10)
ax.text(0.12, 0.05, 0.15, "the unique solution", color=GREEN, fontsize=13)

# --- Panel 2: the sheaf — three planes through the z-axis
ax = panel(2, "det A = 0, eliminations agree — the sheaf",
           "three pages, one spine: infinitely many solutions on a line")
for ang, c in zip([0, 55, 115], PLANE_COLORS):
    t = np.deg2rad(ang)
    patch(ax, (0, 0, 0), (np.cos(t), np.sin(t), 0), (0, 0, 1), c)
ax.plot([0, 0], [0, 0], [-1.05, 1.05], color=GREEN, lw=3.5, zorder=10)
ax.text(0.08, 0.08, 0.9, "the common line", color=GREEN, fontsize=13)

# --- Panel 3: the prism — three vertical planes, triangular cross-section
ax = panel(3, "det A = 0, eliminations contradict — the prism",
           "each pair meets; the three edges are parallel; no common point")
ax.view_init(elev=32, azim=-55)
tri = [np.array([-0.7, -0.5, 0]), np.array([0.7, -0.5, 0]),
       np.array([0.0, 0.7, 0])]
for i, c in enumerate(PLANE_COLORS):
    p, q = tri[i], tri[(i + 1) % 3]
    mid = (p + q) / 2
    u = (q - p) / np.linalg.norm(q - p)
    patch(ax, mid, u * 0.95, (0, 0, 0.9), c)
for zc in (-0.9, 0.9):                                # cross-section outline
    ring = tri + [tri[0]]
    ax.plot([p[0] for p in ring], [p[1] for p in ring], [zc] * 4,
            color=AX, lw=1.2, alpha=0.8)
for p in tri:
    ax.plot([p[0], p[0]], [p[1], p[1]], [-1.0, 1.0], color=RED,
            lw=2.5, ls="--", zorder=9)
ax.text(0.85, -0.4, 0.8, "three parallel edges,\nnever meeting", color=RED,
        fontsize=13)

# --- Panel 4: parallel planes
ax = panel(4, "det A = 0, eliminations contradict — parallel planes",
           "proportional normals, right-hand sides breaking the proportion")
for z0, c in zip([-0.7, 0.0, 0.7], PLANE_COLORS):
    patch(ax, (0, 0, z0), (1, 0, 0), (0, 1, 0), c)
ax.text2D(0.80, 0.78, "no two ever meet", transform=ax.transAxes,
          color=RED, fontsize=13)

fig.tight_layout(h_pad=1.6)
fig.savefig("linear-systems-configurations.svg", transparent=True,
            bbox_inches="tight", metadata={"Date": None})
print("wrote linear-systems-configurations.svg")
