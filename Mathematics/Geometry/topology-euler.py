"""Topology, counted: four things you can check on a laptop.

1. Euler's formula V - E + F on the five Platonic solids (all give 2) and on a torus
   built as a grid of triangles (gives 0): the number depends only on the shape's holes.
2. Königsberg 1736: an Euler walk exists only if every land mass has an even number of
   bridges, or exactly two have an odd number. Count the degrees.
3. Planarity: a graph drawable on a page without crossings obeys E <= 3V - 6; the
   "three houses, three utilities" graph K(3,3) and the pentagram-with-everything K5 fail.
4. Kirchhoff's independent loops: for a connected circuit the number of independent
   loop equations is E - V + 1 — a topological count, the same for every drawing.

Run:  python3 topology-euler.py
"""
from itertools import combinations
platonic = {"tetrahedron": (4, 6, 4), "cube": (8, 12, 6), "octahedron": (6, 12, 8), "dodecahedron": (20, 30, 12), "icosahedron": (12, 30, 20)}
print("Euler's formula on the Platonic solids:")
for name, (V, E, F) in platonic.items(): print(f"  {name:13s} V={V:2d} E={E:2d} F={F:2d}   V - E + F = {V-E+F}")

def torus_mesh(m, n):
    """m x n grid of vertices with the top glued to the bottom and left to right; each cell cut into two triangles"""
    V = m*n; E = 3*m*n; F = 2*m*n          # every vertex owns one horizontal, one vertical and one diagonal edge
    return V, E, F
for m, n in [(3, 3), (10, 10), (40, 25)]:
    V, E, F = torus_mesh(m, n); print(f"  torus mesh {m}x{n}: V={V} E={E} F={F}   V - E + F = {V-E+F}")
print("  a sphere-like solid gives 2, a doughnut gives 0, whatever the mesh: chi = 2 - 2 x (number of holes)\n")

bridges = [("A","B"),("A","B"),("A","C"),("A","C"),("A","D"),("B","D"),("C","D")]   # A = Kneiphof island, B/C = banks, D = east island
deg = {}
for u, v in bridges: deg[u] = deg.get(u, 0)+1; deg[v] = deg.get(v, 0)+1
odd = [k for k, d in deg.items() if d % 2]
print("Königsberg 1736, bridges per land mass:", dict(sorted(deg.items())))
print(f"  land masses with an odd number of bridges: {len(odd)} ({', '.join(sorted(odd))}) -> a walk crossing every bridge once needs 0 or 2 -> impossible")
print("  remove one bridge (say A-B):", end=" ")
deg2 = dict(deg); deg2["A"] -= 1; deg2["B"] -= 1; odd2 = [k for k, d in deg2.items() if d % 2]
print(f"odd vertices {sorted(odd2)} -> now a walk exists, starting at one and ending at the other\n")

def planar_bound(V, E): return E <= 3*V - 6
def bipartite_bound(V, E): return E <= 2*V - 4
print("Planarity by Euler's inequality:")
for name, V, E, bip in [("K4 (tetrahedron skeleton)", 4, 6, False), ("K5 (five points all joined)", 5, 10, False), ("K3,3 (three houses, three utilities)", 6, 9, True), ("cube skeleton", 8, 12, True)]:
    ok = (bipartite_bound if bip else planar_bound)(V, E)
    print(f"  {name:38s} V={V} E={E}  {'passes' if ok else 'FAILS'} {'E <= 2V-4' if bip else 'E <= 3V-6'} -> {'can be' if ok else 'cannot be'} drawn without crossings")
print("  (Kuratowski 1930: a graph is planar exactly when it contains no stretched copy of K5 or K3,3)\n")

print("Kirchhoff's loop count is topological:")
for name, V, E in [("one battery, one bulb", 2, 2), ("the Wheatstone bridge", 4, 6), ("a 3x3 grid of resistors", 16, 24), ("two loops sharing one branch", 2, 3)]:
    print(f"  {name:36s} junctions V={V:2d} branches E={E:2d} -> independent loops = E - V + 1 = {E-V+1}")
print("  redraw the circuit any way you like: the count does not change, because it never depended on the drawing")
