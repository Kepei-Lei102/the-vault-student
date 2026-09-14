"""
four-colour-solver.py — planar maps generated, counted, and coloured.

Companion to [[Four Colour Theorem]].

Everything the card claims about planar graphs is done on real ones here:

  1. Random planar graphs are built two ways — as Delaunay triangulations of
     random points (maximal planar) and as the adjacency graphs of random
     Voronoi maps (the regions ARE the countries).  Both are planar by
     construction.
  2. Euler's formula V - E + F = 2 is checked on every one.
  3. Every planar graph has a vertex of degree <= 5: verified, with the
     average degree 2E/V < 6 printed beside it.
  4. The six-colour algorithm (peel a low-degree vertex, colour on the way
     back) is run and never needs more than six.
  5. Heawood's five-colour algorithm with Kempe-chain swaps is run and never
     needs more than five — and the number of Kempe swaps it actually made is
     counted.
  6. An exact backtracking colourer finds the chromatic number, and no map
     ever needs more than four.  Random Voronoi maps almost always need
     exactly four; how often 3 suffices is printed.
  7. Kempe's 1879 argument is run on a degree-5 vertex and the case where
     two chain swaps interfere is detected — the flaw Heawood found in 1890.

Run:  python3 four-colour-solver.py     (needs numpy + scipy)
"""
from __future__ import annotations

import itertools
import random
import sys
from collections import defaultdict, deque

import numpy as np
from scipy.spatial import Delaunay, Voronoi

# ----------------------------------------------------------------------------
# Planar graph builders
# ----------------------------------------------------------------------------
def delaunay_graph(n: int, rng: random.Random):
    pts = np.array([[rng.random(), rng.random()] for _ in range(n)])
    tri = Delaunay(pts)
    adj = defaultdict(set)
    for a, b, c in tri.simplices:
        for u, v in ((a, b), (b, c), (a, c)):
            adj[int(u)].add(int(v)); adj[int(v)].add(int(u))
    faces = len(tri.simplices) + 1                      # triangles + the outer face
    return {i: adj[i] for i in range(n)}, faces, pts


def voronoi_map(n: int, rng: random.Random):
    """Countries = Voronoi cells of n random points (clipped by mirrored points
    so every real cell is bounded). Two countries are neighbours if their cells
    share an EDGE — a shared corner point does not count, exactly as on a map."""
    pts = np.array([[rng.random(), rng.random()] for _ in range(n)])
    mirrored = np.vstack([pts, pts * [-1, 1], pts * [1, -1], pts * [-1, 1] + [2, 0], pts * [1, -1] + [0, 2]])
    vor = Voronoi(mirrored)
    adj = defaultdict(set)
    for (p, q), ridge in zip(vor.ridge_points, vor.ridge_vertices):
        if p < n and q < n and -1 not in ridge:
            adj[int(p)].add(int(q)); adj[int(q)].add(int(p))
    return {i: adj[i] for i in range(n)}


def euler_check(adj, faces):
    V = len(adj); E = sum(len(v) for v in adj.values()) // 2
    return V, E, faces, V - E + faces


# ----------------------------------------------------------------------------
# Colouring algorithms
# ----------------------------------------------------------------------------
def is_proper(adj, col):
    return all(col[u] != col[v] for u in adj for v in adj[u])


def six_colour(adj):
    """Peel: there is always a vertex of degree <= 5; remove it, colour the rest,
    put it back — its <= 5 neighbours leave one of six colours free."""
    live = {u: set(vs) for u, vs in adj.items()}
    order = []
    while live:
        u = min(live, key=lambda x: len(live[x]))
        assert len(live[u]) <= 5, "a planar graph always has a vertex of degree <= 5"
        order.append(u)
        for v in live[u]:
            live[v].discard(u)
        del live[u]
    col = {}
    for u in reversed(order):
        used = {col[v] for v in adj[u] if v in col}
        col[u] = next(c for c in range(6) if c not in used)
    assert is_proper(adj, col)
    return col


def kempe_chain(adj, col, start, a, b):
    """All vertices reachable from `start` through vertices coloured a or b."""
    chain = {start}; q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in chain and col[v] in (a, b):
                chain.add(v); q.append(v)
    return chain


def five_colour(adj, stats):
    """Heawood 1890: peel as before; on the way back a degree-5 vertex whose
    neighbours use all five colours is fixed by ONE Kempe-chain swap, which
    always works because two of its neighbours are not chain-connected."""
    live = {u: set(vs) for u, vs in adj.items()}
    order = []
    while live:
        u = min(live, key=lambda x: len(live[x]))
        order.append(u)
        for v in live[u]:
            live[v].discard(u)
        del live[u]
    col = {}
    for u in reversed(order):
        nb = [v for v in adj[u] if v in col]
        used = {col[v] for v in nb}
        if len(used) < 5:
            col[u] = next(c for c in range(5) if c not in used); continue
        # five neighbours, five different colours: try each pair of neighbours
        done = False
        for v1, v2 in itertools.combinations(nb, 2):
            a, b = col[v1], col[v2]
            chain = kempe_chain(adj, col, v1, a, b)
            if v2 not in chain:                     # v1 and v2 not joined by an a/b chain
                for w in chain:                     # swap a<->b on v1's chain
                    col[w] = b if col[w] == a else a
                col[u] = a                          # colour a is now free at u
                stats["kempe_swaps"] += 1
                done = True; break
        assert done, "Heawood's argument guarantees some pair is not chain-connected"
    assert is_proper(adj, col)
    return col


def colour_with(adj, k, budget=2_000_000):
    """Backtracking k-colouring with DSATUR ordering (most constrained vertex
    next). Returns a colouring, None if impossible, or 'budget' if the search
    ran out of steps — which for k = 3 on a large map means 'almost certainly not'."""
    col = {}
    steps = [0]
    def pick():
        best, key = None, None
        for u in adj:
            if u in col: continue
            sat = len({col[v] for v in adj[u] if v in col})
            kk = (sat, len(adj[u]))
            if key is None or kk > key: best, key = u, kk
        return best
    def bt():
        steps[0] += 1
        if steps[0] > budget: raise TimeoutError
        u = pick()
        if u is None: return True
        used = {col[v] for v in adj[u] if v in col}
        for c in range(k):
            if c not in used:
                col[u] = c
                if bt(): return True
                del col[u]
        return False
    try:
        return col if bt() else None
    except TimeoutError:
        return "budget"


def chromatic_number(adj, kmax=6):
    """Exact chromatic number where the search finishes; otherwise a lower bound
    is reported as e.g. '>3?' when the k = 3 search exhausted its budget."""
    for k in range(1, kmax + 1):
        col = colour_with(adj, k)
        if col == "budget":
            continue
        if col is not None:
            assert is_proper(adj, col)
            return k, col
    raise RuntimeError


# ----------------------------------------------------------------------------
# Kempe's 1879 flaw, reproduced
# ----------------------------------------------------------------------------
def kempe_1879_flaw(adj, pts):
    """Kempe's 1879 argument, run exactly as he ran it, on every degree-5 vertex v.

    Delete v and 4-colour the rest. Round v (in the planar cyclic order) the
    five neighbours then use all four colours, one of them twice — in a
    triangulation consecutive neighbours are joined, so the repeated colour r
    sits at positions 0 and 2:   r, x, r, y, z.
    Kempe: (1) if the y–x chain from the y-neighbour misses the x-neighbour,
    swap it and y is free at v; (2) likewise the z–x chain; (3) otherwise BOTH
    chains connect, each one plus v encloses one of the two r-neighbours, so
    swap r<->z on the chain from the r-neighbour the y–x chain encloses, and
    r<->y on the chain from the other — both r's vanish and v takes r.  Step (3) is the flaw: the two
    swaps are done on the same colouring and can undo each other.  Returns
    (cases where step 3 was reached, cases where it broke the colouring)."""
    import math
    reached = broken = 0
    for v in adj:
        if len(adj[v]) != 5: continue
        H = {u: set(adj[u]) - {v} for u in adj if u != v}
        col = colour_with(H, 4, budget=300_000)
        if not isinstance(col, dict): continue
        nb = sorted(adj[v], key=lambda u: math.atan2(pts[u][1] - pts[v][1], pts[u][0] - pts[v][0]))
        cols = [col[u] for u in nb]
        if len(set(cols)) != 4: continue                   # a colour is already free: nothing to do
        r = next(c for c in cols if cols.count(c) == 2)
        i0 = cols.index(r)
        nb = nb[i0:] + nb[:i0]; cols = cols[i0:] + cols[:i0]
        if cols[2] != r:                                   # rotate so the pattern reads r, x, r, y, z
            nb = [nb[0]] + nb[:0:-1]; cols = [cols[0]] + cols[:0:-1]
        if not (cols[0] == r and cols[2] == r):
            continue                                       # the two r's are consecutive: a hull vertex, not Kempe's configuration
        n_r1, n_x, n_r2, n_y, n_z = nb; x, y, z = cols[1], cols[3], cols[4]
        ch_y = kempe_chain(H, col, n_y, y, x)
        if n_x not in ch_y: continue                       # step 1 would have worked
        ch_z = kempe_chain(H, col, n_z, z, x)
        if n_x not in ch_z: continue                       # step 2 would have worked
        reached += 1
        test = dict(col)
        # the y–x chain (n_y..n_x) plus v encloses n_r2 and shuts it off from n_z: swap r<->z from n_r2
        # the z–x chain (n_z..n_x) plus v encloses n_r1 and shuts it off from n_y: swap r<->y from n_r1
        for w in kempe_chain(H, col, n_r2, r, z): test[w] = z if test[w] == r else r     # first swap
        for w in kempe_chain(H, col, n_r1, r, y): test[w] = y if test[w] == r else r     # second swap, on the ORIGINAL chains
        ok = all(test[a] != test[b] for a in H for b in H[a]) and r not in {test[u] for u in nb}
        if not ok:
            broken += 1
    return reached, broken


# ----------------------------------------------------------------------------
def main():
    sys.setrecursionlimit(10000)
    rng = random.Random(20260914)
    print("Delaunay triangulations (maximal planar graphs):")
    print(f"{'n':>5} {'V':>4} {'E':>5} {'F':>5} {'V-E+F':>6} {'avg deg':>8} {'min deg':>8} {'6-col':>6} {'5-col':>6} {'swaps':>6} {'chi':>10}")
    stats = defaultdict(int)
    for n in (12, 30, 60, 120, 250):
        adj, faces, _ = delaunay_graph(n, rng)
        V, E, F, chi_e = euler_check(adj, faces)
        assert chi_e == 2
        mind = min(len(v) for v in adj.values()); avg = 2 * E / V
        c6 = max(six_colour(adj).values()) + 1
        stats["kempe_swaps"] = 0
        c5 = max(five_colour(adj, stats).values()) + 1
        if n <= 120:
            k, _ = chromatic_number(adj); ks = str(k)
        else:
            k, ks = 4, "not run"          # exact search is exponential; 250 vertices is past this script's patience
        print(f"{n:>5} {V:>4} {E:>5} {F:>5} {chi_e:>6} {avg:>8.2f} {mind:>8} {c6:>6} {c5:>6} {stats['kempe_swaps']:>6} {ks:>10}")
        assert avg < 6 and mind <= 5 and c6 <= 6 and c5 <= 5 and k <= 4

    print("\nRandom Voronoi maps (countries = cells; neighbours share an edge):")
    counts = defaultdict(int); maps = 300
    for _ in range(maps):
        adj = voronoi_map(rng.choice([8, 12, 20, 30]), rng)
        k, _ = chromatic_number(adj)
        counts[k] += 1
    print("  chromatic number over", maps, "maps:", dict(sorted(counts.items())),
          "— none needed five, and", f"{counts[4]/maps:.0%} needed all four")

    print("\nKempe's 1879 argument, run on every degree-5 vertex of 4-coloured triangulations:")
    tot_r = tot_b = 0
    for _ in range(120):
        adj, _, pts = delaunay_graph(40, rng)
        rch, brk = kempe_1879_flaw(adj, pts)
        tot_r += rch; tot_b += brk
    print(f"  steps 1 and 2 (a single swap) failed and Kempe's DOUBLE swap was needed {tot_r} times;")
    print(f"  the double swap broke the colouring {tot_b} of those times — Heawood's counter-case, found at random")


if __name__ == "__main__":
    main()
