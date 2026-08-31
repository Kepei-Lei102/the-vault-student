"""Graphs — verify everything on the card, seeded by TODAY'S date.

Run it yourself, any day:

    python3 graphs-verify.py

The random seed is today's date (YYYYMMDD), so each day tests fresh graphs —
and the guarantees hold every day, because they are theorems, not luck.

What it checks:
  1. The two REAL exam questions, reproduced by the card's own code:
     November 2025 Paper 33's Dijkstra answers (T6 V10 W13 X18 Y21 Z28) and
     June 2026 Paper 33's A* path (W-N2-N5-N6-E, cost 18) — including the
     mark scheme's table rows.
  2. Dijkstra vs brute force: on hundreds of random weighted graphs, the
     empire-of-certainty answer equals the answer found by trying EVERY
     simple path (only feasible on small graphs — which is the point).
  3. A* honesty, in full: with a CONSISTENT heuristic (one that never drops
     faster than the edge you cross — straight-line distance is like this)
     the card's settle-once A* is always optimal; with h = 0 it IS Dijkstra.
     And the fine print made visible: a merely ADMISSIBLE heuristic (never
     overestimates, but jumpy) can fool the settle-once variant — while a
     patient A* that allows re-expansion still gets the optimum. The harness
     hunts for exactly such a case each day and shows both behaviours.
  4. BFS visits vertices in non-decreasing edge-count order; DFS visits
     everything reachable; both terminate on cyclic graphs (the visited-set
     discipline doing its job).

One caution the card repeats: exam graphs are tiny so every method looks
fast. Real road networks have millions of vertices — that is where the
priority queue and the compass stop being decoration.
"""
import heapq
import itertools
import random
import datetime
from collections import deque

SEED = int(datetime.date.today().strftime("%Y%m%d"))
random.seed(SEED)
print(f"seed = {SEED}  (today's date — run me tomorrow and I test different graphs)\n")


# ---------------------------------------------------------------- the card's engines
def bfs(graph, start):
    visited = [start]
    frontier = deque([start])
    while frontier:
        node = frontier.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                frontier.append(neighbour)
    return visited


def dfs(graph, start):
    visited = []
    frontier = [start]
    while frontier:
        node = frontier.pop()
        if node not in visited:
            visited.append(node)
            frontier.extend(n for n in graph[node] if n not in visited)
    return visited


def dijkstra(graph, start):
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    frontier = [(0, start)]
    settled = set()
    while frontier:
        d, node = heapq.heappop(frontier)
        if node in settled:
            continue
        settled.add(node)
        for neighbour, w in graph[node].items():
            if d + w < dist[neighbour]:
                dist[neighbour] = d + w
                heapq.heappush(frontier, (dist[neighbour], neighbour))
    return dist


def astar(graph, h, start, goal):
    """Returns (path, cost, table_rows) - rows in mark-scheme format."""
    frontier = [(h[start], 0, start, [start])]
    settled = set()
    rows = []
    while frontier:
        f, g, node, path = heapq.heappop(frontier)
        if node in settled:
            continue
        settled.add(node)
        if node == goal:
            return path, g, rows
        for neighbour, w in graph[node].items():
            if neighbour not in settled:
                rows.append((path + [neighbour], g + w, h[neighbour], g + w + h[neighbour]))
                heapq.heappush(frontier, (g + w + h[neighbour], g + w,
                                          neighbour, path + [neighbour]))
    return None, float("inf"), rows


# ---------------------------------------------------------------- 1. the real papers
N25 = {"Start": {"T": 6, "Y": 22}, "T": {"Start": 6, "V": 4},
       "V": {"T": 4, "W": 3, "X": 9}, "W": {"V": 3, "X": 5},
       "X": {"V": 9, "W": 5, "Y": 3, "Z": 10}, "Y": {"Start": 22, "X": 3, "Z": 8},
       "Z": {"X": 10, "Y": 8}}
d = dijkstra(N25, "Start")
assert [d[k] for k in "TVWXYZ"] == [6, 10, 13, 18, 21, 28]
print("N25/33 Dijkstra: T6 V10 W13 X18 Y21 Z28 — matches the published mark scheme")

J26 = {"W": {"N1": 6, "N2": 4, "N3": 7}, "N1": {"W": 6},
       "N2": {"W": 4, "N5": 7}, "N3": {"W": 7},
       "N5": {"N2": 7, "N4": 2, "N6": 4, "E": 11}, "N4": {"N5": 2},
       "N6": {"N5": 4, "E": 3}, "E": {"N5": 11, "N6": 3}}
H26 = {"W": 18, "N1": 15, "N2": 14, "N3": 13, "N5": 7, "N4": 9, "N6": 3, "E": 0}
path, cost, rows = astar(J26, H26, "W", "E")
assert path == ["W", "N2", "N5", "N6", "E"] and cost == 18
ms_rows = [(["W", "N1"], 6, 15, 21), (["W", "N2"], 4, 14, 18), (["W", "N3"], 7, 13, 20),
           (["W", "N2", "N5"], 11, 7, 18), (["W", "N2", "N5", "N4"], 13, 9, 22),
           (["W", "N2", "N5", "N6"], 15, 3, 18), (["W", "N2", "N5", "E"], 22, 0, 22),
           (["W", "N2", "N5", "N6", "E"], 18, 0, 18)]
assert rows == ms_rows, "A* table rows drifted from the mark scheme"
print("J26/33 A*: W-N2-N5-N6-E at 18 — and all 8 working rows match the scheme's table\n")


# ---------------------------------------------------------------- 2. Dijkstra vs brute force
def brute_shortest(graph, start, goal):
    best = float("inf")
    verts = [v for v in graph if v not in (start,)]
    for r in range(len(verts) + 1):
        for mid in itertools.permutations(verts, r):
            path = (start,) + mid
            if path[-1] != goal:
                continue
            total, ok = 0, True
            for a, b in zip(path, path[1:]):
                if b not in graph[a]:
                    ok = False
                    break
                total += graph[a][b]
            if ok:
                best = min(best, total)
    return best


TRIALS = 250
for _ in range(TRIALS):
    n = random.randint(4, 7)                       # brute force explodes past this
    names = [chr(65 + i) for i in range(n)]
    g = {v: {} for v in names}
    for a, b in itertools.combinations(names, 2):
        if random.random() < 0.55:
            w = random.randint(1, 20)
            g[a][b] = w
            g[b][a] = w
    d = dijkstra(g, "A")
    for target in names[1:]:
        assert d[target] == brute_shortest(g, "A", target), (g, target)
print(f"Dijkstra vs try-every-path: {TRIALS} random graphs, every distance identical")
print("     (brute force needed factorial time on 7 vertices — the empire needed V rounds)\n")

# ---------------------------------------------------------------- 3. A* honesty checks
checked = 0
for _ in range(120):
    n = random.randint(5, 8)
    names = [chr(65 + i) for i in range(n)]
    g = {v: {} for v in names}
    for a, b in itertools.combinations(names, 2):
        if random.random() < 0.6:
            w = random.randint(1, 15)
            g[a][b] = w
            g[b][a] = w
    d_true = dijkstra(g, "A")
    goal = names[-1]
    if d_true[goal] == float("inf"):
        continue
    # consistent heuristic: the true remaining distance, scaled by one factor
    # c in [0,1] — scaling by a constant keeps the triangle inequality, which
    # is exactly the never-drops-faster-than-the-road property
    from_goal = dijkstra(g, goal)
    c = random.random()
    h = {v: (0 if from_goal[v] == float("inf") else c * from_goal[v]) for v in names}
    _, cost, _ = astar(g, h, "A", goal)
    assert cost == d_true[goal], "consistent A* missed the optimum"
    _, cost0, _ = astar(g, {v: 0 for v in names}, "A", goal)
    assert cost0 == d_true[goal], "h = 0 should be plain Dijkstra"
    checked += 1
print(f"A*: {checked} random graphs — consistent heuristics always optimal; h = 0 is Dijkstra")


def astar_reexpand(graph, h, start, goal):
    """The patient variant: no settled set — re-expand whenever g improves."""
    best_g = {start: 0}
    frontier = [(h[start], 0, start)]
    while frontier:
        f, g_here, node = heapq.heappop(frontier)
        if node == goal:
            return g_here
        if g_here > best_g.get(node, float("inf")):
            continue
        for neighbour, w in graph[node].items():
            if g_here + w < best_g.get(neighbour, float("inf")):
                best_g[neighbour] = g_here + w
                heapq.heappush(frontier, (g_here + w + h[neighbour], g_here + w, neighbour))
    return float("inf")


# the fine print, demonstrated: hunt for an admissible-but-jumpy heuristic
# that fools settle-once A* — the patient variant must still be optimal
fooled = 0
for _ in range(4000):
    n = random.randint(4, 6)
    names = [chr(65 + i) for i in range(n)]
    g = {v: {} for v in names}
    for a, b in itertools.combinations(names, 2):
        if random.random() < 0.6:
            w = random.randint(1, 15)
            g[a][b] = w
            g[b][a] = w
    goal = names[-1]
    d_true = dijkstra(g, "A")
    if d_true[goal] == float("inf"):
        continue
    from_goal = dijkstra(g, goal)
    h = {v: (0 if from_goal[v] == float("inf")
             else random.randint(0, int(from_goal[v]))) for v in names}   # admissible, jumpy
    h[goal] = 0
    _, cost_fast, _ = astar(g, h, "A", goal)
    cost_patient = astar_reexpand(g, h, "A", goal)
    assert cost_patient == d_true[goal], "re-expanding A* must stay optimal when admissible"
    if cost_fast > d_true[goal]:
        fooled += 1
print(f"     the fine print: {fooled} jumpy-but-admissible heuristics fooled settle-once A*")
print("     while the re-expanding variant stayed optimal every single time —")
print("     which is why real heuristics are chosen distance-like (consistent)\n")

# ---------------------------------------------------------------- 4. traversal discipline
for _ in range(200):
    n = random.randint(3, 9)
    names = [chr(65 + i) for i in range(n)]
    g = {v: {} for v in names}
    for a, b in itertools.combinations(names, 2):
        if random.random() < 0.5:
            g[a][b] = 1
            g[b][a] = 1
    reach_b, reach_d = set(bfs(g, "A")), set(dfs(g, "A"))
    assert reach_b == reach_d, "BFS and DFS must agree on reachability"
    hop = dijkstra(g, "A")                       # unit weights: hop counts
    order = [hop[v] for v in bfs(g, "A")]
    assert order == sorted(order), "BFS must visit in ring order"
print("BFS/DFS: 200 cyclic graphs — same reachable set, BFS in ring order, no hangs")
print("     (delete the visited set and either loop orbits the first cycle forever)\n")

print("every claim on the card held. run me again tomorrow — different graphs, same theorems.")
