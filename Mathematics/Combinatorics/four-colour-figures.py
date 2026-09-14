"""
four-colour-figures.py — the figures for [[Four Colour Theorem]].

  four-colour-map.svg          a random 40-country map, exactly four-coloured by the
                               backtracking colourer from four-colour-solver.py
  four-colour-dual.svg         the same idea small: a map, its dual graph, and V - E + F
  four-colour-k4-k5.svg        four countries that all touch (so four colours are needed)
                               and why five cannot all touch (K5 is not planar)
  four-colour-kempe.svg        the Kempe-chain swap that frees a colour at a degree-5 vertex

All text #888, transparent background, verified light and dark.
Run:  python3 four-colour-figures.py
"""
import importlib.util
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from scipy.spatial import Voronoi

spec = importlib.util.spec_from_file_location("fcs", "four-colour-solver.py")
fcs = importlib.util.module_from_spec(spec); spec.loader.exec_module(fcs)

GREY = "#888"
PALETTE = ["#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"]   # blue red green amber purple teal
ALPHA = 0.45


def style(ax, title=""):
    ax.set_facecolor("none"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(GREY)
    if title:
        ax.set_title(title, color=GREY, fontsize=10)


def voronoi_cells(n, rng):
    pts = np.array([[rng.random(), rng.random()] for _ in range(n)])
    mirrored = np.vstack([pts, pts * [-1, 1], pts * [1, -1], pts * [-1, 1] + [2, 0], pts * [1, -1] + [0, 2]])
    vor = Voronoi(mirrored)
    adj = {i: set() for i in range(n)}
    for (p, q), ridge in zip(vor.ridge_points, vor.ridge_vertices):
        if p < n and q < n and -1 not in ridge:
            adj[int(p)].add(int(q)); adj[int(q)].add(int(p))
    cells = [vor.vertices[vor.regions[vor.point_region[i]]] for i in range(n)]
    return pts, cells, adj


def big_map():
    rng = random.Random(4)
    pts, cells, adj = voronoi_cells(40, rng)
    k, col = fcs.chromatic_number(adj)
    fig, ax = plt.subplots(figsize=(7.5, 6.2), dpi=100); fig.patch.set_alpha(0)
    for i, poly in enumerate(cells):
        ax.add_patch(Polygon(poly, closed=True, facecolor=PALETTE[col[i]], alpha=ALPHA, edgecolor=GREY, lw=1.2))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect("equal")
    counts = {c: sum(1 for v in col.values() if v == c) for c in range(k)}
    style(ax, f"Forty random countries, {k} colours, no two neighbours alike\n"
              f"(colour counts {', '.join(str(counts[c]) for c in range(k))} — found by backtracking, and three would not do)")
    fig.tight_layout(); fig.savefig("four-colour-map.svg", format="svg", transparent=True)
    return k


def dual():
    rng = random.Random(11)
    pts, cells, adj = voronoi_cells(7, rng)
    k, col = fcs.chromatic_number(adj)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.6), dpi=100); fig.patch.set_alpha(0)
    for i, poly in enumerate(cells):
        a1.add_patch(Polygon(poly, closed=True, facecolor=PALETTE[col[i]], alpha=ALPHA, edgecolor=GREY, lw=1.2))
        a2.add_patch(Polygon(poly, closed=True, facecolor="none", edgecolor=GREY, lw=0.8, ls="--"))
    for ax in (a1, a2):
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect("equal")
    # dual graph on the right
    E = 0
    for u in adj:
        for v in adj[u]:
            if u < v:
                a2.plot([pts[u][0], pts[v][0]], [pts[u][1], pts[v][1]], color=GREY, lw=1.6); E += 1
    for i in range(7):
        a2.scatter([pts[i][0]], [pts[i][1]], s=180, color=PALETTE[col[i]], alpha=0.9, zorder=3, edgecolor=GREY)
        a2.text(pts[i][0] + 0.03, pts[i][1] + 0.05, chr(65 + i), ha="left", color=GREY, fontsize=10)
        a1.text(pts[i][0], pts[i][1], chr(65 + i), ha="center", va="center", color=GREY, fontsize=11)
    V = 7; F = E - V + 2
    style(a1, "The map: seven countries, three colours enough here")
    style(a2, f"Its dual graph: one vertex per country, one edge per shared border\nV = {V}, E = {E}, F = {F}  →  V − E + F = {V - E + F}")
    fig.tight_layout(); fig.savefig("four-colour-dual.svg", format="svg", transparent=True)


def k4_k5():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.6), dpi=100); fig.patch.set_alpha(0)
    # four mutually touching countries: a centre with three around it
    a1.add_patch(Polygon([[0, 0], [2, 0], [2, 2], [0, 2]], facecolor="none", edgecolor=GREY, lw=1.2))
    c = np.array([1, 1])
    angles = np.deg2rad([90, 210, 330])
    inner = [c + 0.45 * np.array([np.cos(t), np.sin(t)]) for t in angles]
    cols = ["#dc2626", "#059669", "#f59e0b"]
    corners = [[[0, 2], [2, 2]], [[0, 2], [0, 0], [2, 0]], [[2, 0], [2, 2]]]
    outer = [[[0, 2], [2, 2]], [[0, 2], [0, 0]], [[2, 0], [2, 2]]]
    # three outer regions as wedges from the centre triangle to the square's edges
    wedges = [
        [inner[0], inner[2], [2, 2], [0, 2]],
        [inner[0], [0, 2], [0, 0], inner[1]],
        [inner[1], [0, 0], [2, 0], [2, 2], inner[2]],
    ]
    for w, colr in zip(wedges, cols):
        a1.add_patch(Polygon(w, closed=True, facecolor=colr, alpha=ALPHA, edgecolor=GREY, lw=1.2))
    a1.add_patch(Polygon(inner, closed=True, facecolor="#2563eb", alpha=ALPHA, edgecolor=GREY, lw=1.2))
    a1.set_xlim(-0.1, 2.1); a1.set_ylim(-0.1, 2.1); a1.set_aspect("equal")
    a1.text(1, 1, "D", ha="center", va="center", color=GREY, fontsize=12)
    a1.text(1, 1.75, "A", ha="center", color=GREY, fontsize=12); a1.text(0.3, 0.9, "B", color=GREY, fontsize=12); a1.text(1.6, 0.3, "C", color=GREY, fontsize=12)
    style(a1, "Four countries that all touch: four colours are NEEDED\n(and no map needs more — that is the theorem)")
    # K5: five vertices, ten edges, one must cross
    th = np.deg2rad(90 + 72 * np.arange(5)); P = np.c_[np.cos(th), np.sin(th)]
    for i in range(5):
        for j in range(i + 1, 5):
            crossing = (j - i) in (2, 3)
            a2.plot([P[i][0], P[j][0]], [P[i][1], P[j][1]], color="#dc2626" if crossing else GREY, lw=1.6 if crossing else 1.2, alpha=0.9)
    for i in range(5):
        a2.scatter([P[i][0]], [P[i][1]], s=160, color="#2563eb", alpha=0.8, zorder=3, edgecolor=GREY)
    a2.set_xlim(-1.3, 1.3); a2.set_ylim(-1.3, 1.3); a2.set_aspect("equal")
    style(a2, "Five countries cannot all touch: K5 has 10 edges,\nbut a planar graph on 5 vertices allows 3V − 6 = 9")
    fig.tight_layout(); fig.savefig("four-colour-k4-k5.svg", format="svg", transparent=True)


def kempe():
    """A degree-5 vertex v whose five neighbours use all five colours; the
    red–green Kempe chain from neighbour 1 does not reach neighbour 3, so
    swapping it frees red for v."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=100); fig.patch.set_alpha(0)
    RED, GREEN, BLUE, AMBER, PURPLE = "#dc2626", "#059669", "#2563eb", "#f59e0b", "#7c3aed"
    v = np.array([0, 0]); th = np.deg2rad(90 + 72 * np.arange(5)); nb = np.c_[np.cos(th), np.sin(th)]
    nbcol = [RED, BLUE, GREEN, AMBER, PURPLE]
    # extra vertices forming a red–green chain from neighbour 0 outward, and a separate one near neighbour 2
    chain = [nb[0] + [0.0, 0.8], nb[0] + [0.7, 1.3], nb[0] + [1.4, 0.9]]
    chaincol = [GREEN, RED, GREEN]
    far = [nb[2] + [-0.9, -0.3]]; farcol = [RED]
    for ax, swapped in ((a1, False), (a2, True)):
        # edges
        for p in nb:
            ax.plot([v[0], p[0]], [v[1], p[1]], color=GREY, lw=1.2)
        for i in range(5):
            q = nb[(i + 1) % 5]; ax.plot([nb[i][0], q[0]], [nb[i][1], q[1]], color=GREY, lw=0.8, alpha=0.6)
        pts_chain = [nb[0]] + chain
        for a, b in zip(pts_chain, pts_chain[1:]):
            ax.plot([a[0], b[0]], [a[1], b[1]], color=GREY, lw=1.2)
        ax.plot([nb[2][0], far[0][0]], [nb[2][1], far[0][1]], color=GREY, lw=1.2)
        cols_nb = list(nbcol); cols_chain = list(chaincol)
        if swapped:
            cols_nb[0] = GREEN
            cols_chain = [RED if c == GREEN else GREEN for c in chaincol]
        for p, c in zip(nb, cols_nb):
            ax.scatter([p[0]], [p[1]], s=220, color=c, alpha=0.85, zorder=3, edgecolor=GREY)
        for p, c in zip(chain, cols_chain):
            ax.scatter([p[0]], [p[1]], s=170, color=c, alpha=0.85, zorder=3, edgecolor=GREY)
        for p, c in zip(far, farcol):
            ax.scatter([p[0]], [p[1]], s=170, color=c, alpha=0.85, zorder=3, edgecolor=GREY)
        ax.scatter([0], [0], s=300, color=(RED if swapped else "none"), alpha=0.85, zorder=4, edgecolor=GREY, lw=1.5)
        ax.text(0, -0.28, "v", ha="center", color=GREY, fontsize=11)
        ax.set_xlim(-2.0, 2.6); ax.set_ylim(-1.8, 2.6); ax.set_aspect("equal")
        # highlight the chain
        if not swapped:
            for a, b in zip(pts_chain, pts_chain[1:]):
                ax.plot([a[0], b[0]], [a[1], b[1]], color=AMBER, lw=4, alpha=0.35, zorder=1)
    style(a1, "v has five neighbours using all five colours. Follow the red–green\nchain from the red neighbour: it never reaches the green one")
    style(a2, "Swap red↔green along that chain only. Still a proper colouring,\nand now no neighbour of v is red — colour v red")
    fig.tight_layout(); fig.savefig("four-colour-kempe.svg", format="svg", transparent=True)


if __name__ == "__main__":
    k = big_map(); dual(); k4_k5(); kempe()
    print("wrote four SVGs; the 40-country map needed", k, "colours")
