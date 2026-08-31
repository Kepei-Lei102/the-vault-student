---
chinese: 图 (tú)
prerequisites:
  - "[[Binary Trees]]"
  - "[[Hash Tables]]"
  - "[[Stacks and Queues]]"
  - "[[Big-O Notation]]"
leads_to:
  - "[[Heaps and Priority Queues]]"
tags:
  - subject/computer-science
  - domain/data-structures
  - domain/algorithms
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-19-1
  - syllabus/9618-18-1
  - type/deep
  - misconception/graph-means-chart
  - misconception/tree-versus-graph
  - misconception/dijkstra-handles-negative-weights
  - misconception/astar-any-heuristic
---

# Graphs 图

> *Open the map app on your phone and ask for a route. In the half-second before the blue line appears, the phone has run everything on this card: a city stored as vertices and edges, and a shortest-path search racing across it. Every structure in this bay restricted who may connect to whom. Delete every restriction, and what remains — anything may connect to anything — is the last structure, the one the world itself is shaped like.*

## 中文锚点

打开手机地图，点"导航"，蓝色路线弹出来之前的那半秒钟，手机跑完的正是这张卡片。先看一张你早就烂熟的图：**地铁线路图**——站点是**顶点**，站与站之间的线是**边**，这就是"图"的全部含义：一堆点，加上点与点之间的连接。微信好友是**无向**的（互为好友），微博关注是**有向**的（你关注他，他未必关注你）；给每条边标上距离或时间，就是**带权**的图——导航要的正是这种。这个字有个陷阱：**这里的"图"不是统计图表**（不是柱状图、折线图），是图论的图——离散数学里"点与连接"的那个图。回头看这一整个卡组，你会发现它们全是戴着镣铐的图：链表是"每个点只准连下一个"的图，二叉树是"每个点只准有一个父亲、不许绕圈"的图——**把所有限制都松开，就得到图本身**。图怎么存？两条路：**邻接矩阵**（一张二维表，第 $i$ 行第 $j$ 列记录 $i$ 到 $j$ 有没有边/多重）或**邻接表**（一本字典：每个顶点名下挂一串它的邻居——[[Hash Tables|哈希表]]上一张卡末尾的预告，在这里兑现）。图怎么走？**宽度优先**用队列，一圈圈往外漾，像水波；**深度优先**用栈，一条路走到黑再回头——[[Stacks and Queues|栈和队列]]的两种纪律在这里毕业。最短路怎么找？**Dijkstra**：从起点出发，把"已确定最短距离"的领地一圈圈往外扩，每次吞并当前最近的顶点；**A\***：Dijkstra 加一个指南针——每个顶点再配一个"离终点估计还有多远"的**启发值** $h$，按 $f = g + h$（已走 + 预估）挑下一步，于是搜索不再四面八方漫开，而是朝着终点冲。考试只考**手动执行**这两个算法（画表格、填数字），不考写代码——但代码见过一遍，表格就再也不神秘了。

| English | 中文 | one-line meaning |
|---|---|---|
| graph | 图 | vertices plus edges — things plus connections |
| vertex / node | 顶点 / 节点 | one of the things |
| edge | 边 | one connection between two vertices |
| directed / undirected | 有向 / 无向 | one-way follow vs mutual friendship |
| weighted | 带权的 | each edge carries a number — distance, time, cost |
| adjacency matrix | 邻接矩阵 | the 2D-array representation: cell $(i,j)$ describes edge $i\!-\!j$ |
| adjacency list | 邻接表 | the dictionary-of-neighbours representation |
| path / cycle | 路径 / 环 | a walk along edges / one that returns to its start |
| breadth-first (BFS) | 宽度优先 | explore in rings, powered by a queue |
| depth-first (DFS) | 深度优先 | explore one road to its end, powered by a stack |
| heuristic $h$ | 启发值 | A*'s compass: estimated distance still to go |
| $f = g + h$ | — | A*'s ranking: cost so far plus estimate remaining |

## The problem, before the tool

Line the bay up and look at what each structure *forbids*. [[Arrays]]: every element has a numbered position, and "connection" means nothing more than sitting one index apart. [[Linked List]]: each node may point to exactly **one** next. [[Binary Trees]]: each node may have children, but exactly one parent, and no route may ever circle back. Every card bought its speed by *restricting who may connect to whom*.

Now try to store a road network. Chengdu connects to Chongqing *and* to Mianyang *and* to Ya'an; Chongqing connects onward and also *back* — routes circle, junctions branch and merge, and no vertex is anyone's "parent". Try to store friendships, or flight routes, or the web's pages and links, or this vault's own cards and their wiki-links: the same refusal everywhere. **Reality is many-to-many, and it loops.** The restrictions that made the bay's structures fast make them unable to even *say* these shapes.

So the last structure is made by subtraction. Keep vertices; keep edges; delete every rule about how many and no-cycles and who-owns-whom. What remains is the **graph** — and the reveal worth pausing on is that the whole bay was graphs all along: a linked list is a graph wearing a "one outgoing edge each, no cycles" straitjacket, and a tree is a graph wearing "connected, no cycles, one parent". Loosen every constraint and only connections remain.

## The definition — letters first

A graph $G$ has two ingredients: a set $V$ of **vertices** (the things — stations, cities, people, web pages) and a set $E$ of **edges** (the connections between pairs of them). That is the entire definition; everything else is a property an edge may or may not have:

- **Undirected vs directed.** If an edge works both ways (WeChat friendship, a two-way street), the graph is undirected. If it has a direction (a Weibo follow, a one-way street, a web link), it is a **directed graph**, and the edge is drawn as an arrow.
- **Unweighted vs weighted.** If each edge carries a number — distance, travel time, cost, bandwidth — the graph is **weighted**, and questions like "shortest route" become meaningful.
- A **path** is a sequence of edges leading from one vertex to another; a **cycle** is a path that returns to its start. Trees forbade cycles; graphs shrug at them.

That's the vocabulary the examiner means by "the key features of a graph," and it is deliberately small. A graph promises almost nothing — which is precisely why it can describe almost anything.

![[graphs-family-reveal.svg|760]]

## Storing one — the matrix and the dictionary

A graph is an idea; to compute with it you must lay it into memory, and the bay's earlier cards supply both standard layouts.

**The adjacency matrix** is a 2D array ([[Arrays]]) with one row and one column per vertex: cell $(i, j)$ holds whether — or at what weight — an edge runs from $i$ to $j$. An undirected graph gives a symmetric matrix (the mirror-image cells agree); a directed one need not.

**The adjacency list** stores, for each vertex, just the collection of its neighbours — and the natural build is **a dictionary mapping each vertex to its neighbours with weights**, which is [[Hash Tables]]' closing promise cashed. This card's own exam graph, stored that way in real Python:

```python
graph = {                                 # N25/33's graph, as a dictionary
    "Start": {"T": 6, "Y": 22},
    "T":     {"Start": 6, "V": 4},
    "V":     {"T": 4, "W": 3, "X": 9},
    "W":     {"V": 3, "X": 5},
    "X":     {"V": 9, "W": 5, "Y": 3, "Z": 10},
    "Y":     {"Start": 22, "X": 3, "Z": 8},
    "Z":     {"X": 10, "Y": 8},
}
```

The trade between the two is the bay's usual merchandise:

| | adjacency matrix | adjacency list |
|---|---|---|
| space | $O(V^2)$ — even for absent edges | $O(V + E)$ — only real edges |
| "is there an edge $i\!-\!j$?" | $O(1)$ — one cell | walk $i$'s neighbours |
| "give me all neighbours of $i$" | walk a whole row of $V$ cells | already sitting in one list |
| best for | **dense** graphs, edge-lookup-heavy work | **sparse** graphs — which real networks almost always are |

![[graphs-matrix-vs-list.svg|760]]

A road network with millions of junctions averages three or four roads each: the matrix would be a trillion mostly-empty cells, the list a few million entries. Sparse wins in the wild, which is why the dictionary-of-neighbours is the default in practice.

## Walking one — the twin disciplines graduate

Traversal — visit every vertex reachable from a start — is where [[Stacks and Queues]]' two disciplines stop being canteen furniture and become search strategies. Both algorithms are *identical* except for one data structure:

- **Breadth-first search (BFS)** keeps the to-visit vertices in a **queue**: first found, first explored. The search spreads in rings — everything one edge away, then everything two away — like a ripple. Because it explores in distance order, BFS finds shortest paths *when every edge counts as 1*.
- **Depth-first search (DFS)** keeps them on a **stack** (or equivalently uses recursion — [[Recursion]]'s call stack doing the pushing): last found, first explored. The search dives down one road to its dead end, then backtracks. It's the maze-runner's left-hand-on-the-wall strategy, and the natural shape for "explore everything" and "is there any route at all?"

```python
from collections import deque

def bfs(graph, start):
    visited = [start]
    frontier = deque([start])             # a queue: FIFO
    while frontier:
        node = frontier.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour) # marked when discovered,
                frontier.append(neighbour)  # so nothing joins twice
    return visited

def dfs(graph, start):
    visited = []
    frontier = [start]                    # a stack: LIFO
    while frontier:
        node = frontier.pop()
        if node not in visited:
            visited.append(node)
            frontier.extend(n for n in graph[node] if n not in visited)
    return visited
```

Change `popleft()` to `pop()` and BFS becomes DFS. One line — the entire difference between a ripple and a dive is *which end of the line you serve first*, exactly the LIFO/FIFO split the bay opened with.

> [!warning] The `visited` set is the cycle-killer
> Trees never needed a visited list: no cycles means no way to meet the same node twice. Graphs loop, so an unguarded traversal orbits a cycle forever. The marked-when-*discovered* discipline (not when explored) is what keeps each vertex in the frontier at most once. Forgetting `visited` is the classic dead graph-traversal — and the first thing to check when one hangs.

![[graphs-see-it-run.mp4]]

*Three acts: the bay's constraints dissolving — list to tree to graph; BFS's ripple against DFS's dive on the same graph; then Dijkstra's settled frontier spreading over the real November 2025 exam graph while A* beelines through the June 2026 one.*

## Dijkstra — the expanding empire of certainty

Weighted edges break BFS's shortest-path guarantee (two short edges can beat one long one), and **Dijkstra's algorithm** is the repair. The idea deserves to be stated as a picture: grow an **empire of settled vertices** — vertices whose shortest distance from the start is *known for certain* — one vertex per round:

1. **Initialise:** the start's distance is $0$; every other vertex's is $\infty$ ("no route found yet").
2. **Settle:** among the unsettled vertices, take the one with the **smallest current distance**. Its value can never improve — any other route to it would have to leave the empire through a vertex already further away — so mark it settled (*visited*).
3. **Relax:** for each neighbour of the newly settled vertex, check whether going *through* it beats the neighbour's current value; if so, update.
4. Repeat until the target is settled (or all vertices are).

Those four sentences are exactly what the mark scheme pays for — the November 2025 scheme's own marking points are "initialisation: setting Start to 0 **and the rest to ∞**", "values at nodes being updated", "visited nodes shown", "more than one route calculated". The examiner is grading the empire-growing, step by step.

```python
import heapq

def dijkstra(graph, start):
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    frontier = [(0, start)]               # priority queue: nearest first
    settled = set()
    while frontier:
        d, node = heapq.heappop(frontier)
        if node in settled:
            continue
        settled.add(node)                 # its distance is now certain
        for neighbour, w in graph[node].items():
            if d + w < dist[neighbour]:   # found a better route through node
                dist[neighbour] = d + w
                heapq.heappush(frontier, (dist[neighbour], neighbour))
    return dist
```

The "give me the nearest unsettled vertex" step wants a structure that serves the minimum fast — a **priority queue**, which is [[Heaps and Priority Queues]]' whole reason to exist; a plain list works for exam-sized graphs.

### Worked example — the real November 2025 Paper 33 question

> Calculate the shortest distance between the Start node and each node in the graph, using Dijkstra's algorithm. Show your working. [5]

*The graph is the dictionary printed above.* Run the empire, one settlement per row — settled distances in bold as they lock:

| round | settled | how | distances now (S T V W X Y Z) |
|---|---|---|---|
| 0 | **Start** = 0 | initialise: Start 0, rest $\infty$ | **0** 6 $\infty$ $\infty$ $\infty$ 22 $\infty$ |
| 1 | **T** = 6 | nearest unsettled; relax T's neighbours: V ← 6+4 | 0 **6** 10 $\infty$ $\infty$ 22 $\infty$ |
| 2 | **V** = 10 | relax: W ← 10+3, X ← 10+9 | 0 6 **10** 13 19 22 $\infty$ |
| 3 | **W** = 13 | relax: X ← 13+5 = 18, *beats 19* | 0 6 10 **13** 18 22 $\infty$ |
| 4 | **X** = 18 | relax: Y ← 18+3 = 21 *beats 22*, Z ← 18+10 = 28 | 0 6 10 13 **18** 21 28 |
| 5 | **Y** = 21 | relax: Z via Y = 21+8 = 29 — worse, keep 28 | 0 6 10 13 18 **21** 28 |
| 6 | **Z** = 28 | nothing left to improve | 0 6 10 13 18 21 **28** |

Final answers **T 6 · V 10 · W 13 · X 18 · Y 21 · Z 28** — the published mark scheme's exact six values, and this card's committed code reproduces them.

![[graphs-dijkstra-walkthrough.mp4]]

*The same trace at exam pace — one settlement per beat, every relaxation spoken as arithmetic, and the Start–Y trap given its slow-motion moment.* Two teaching moments hide in the table: X is *improved twice* (19 → 18 — the scheme explicitly rewards showing more than one route to a town), and the direct Start–Y road of 22 **loses by one** to the long way round (21) — the examiner's quiet trap for anyone who stops relaxing too early.

## A* — Dijkstra with a compass

Dijkstra explores in *every* direction — its empire is a circle, even when the target lies due east. **A\*** fixes the wastefulness by giving each vertex a second number: a **heuristic** $h$, an *estimate of the distance still to go* to the target (on a map: the straight-line distance). Vertices are then ranked not by distance-so-far $g$ alone, but by

$$f = g + h \qquad \text{(spent so far} + \text{estimated remaining)}$$

and the search always expands the frontier vertex with the smallest $f$. The effect: routes pointing *away* from the target get large $h$, sink down the ranking, and are simply never explored — the circle collapses into a beam. One honesty condition props the whole thing up: $h$ must **never overestimate** the true remaining distance — straight-line distance qualifies, since no road is shorter than the crow flies. Distance-like heuristics of that kind are also *well-behaved* in a second way (the estimate never drops faster than the road you actually drive), and with such an $h$ the first time the target is settled the route is guaranteed optimal, for Dijkstra's own reason. Overestimate, and the guarantee dies outright — A* may return a plausible-looking wrong answer. And with $h = 0$ everywhere, $f = g$ and A* *is* Dijkstra: one algorithm, with and without a compass. (There is finer print between those two conditions, made visible in this card's harness — the Beyond section tells it.)

### Worked example — the real June 2026 Paper 33 question

> The A* algorithm is used to perform searches on a graph. Calculate the best path between the W and E nodes. Show your working in the table provided; the first two rows have been done for you. [5]

The exam's table format *is* the algorithm's diary — each row records one frontier entry: the path, its cost $g$, the destination's $h$, and $f = g + h$. Reproduced in full (this is the published scheme's own table, and this card's code generates it row for row):

| | current path | destination | $g$ | $h$ | $f = g+h$ |
|---|---|---|---|---|---|
| 1 | W | W | 0 | 18 | 18 |
| 2 | W | N1 | 6 | 15 | 21 |
| 3 | W | N2 | 4 | 14 | **18** ← smallest $f$: expand N2 |
| 4 | W | N3 | 7 | 13 | 20 |
| 5 | W→N2 | N5 | 4+7 = 11 | 7 | **18** ← expand N5 |
| 6 | W→N2→N5 | N4 | 13 | 9 | 22 |
| 7 | W→N2→N5 | N6 | 15 | 3 | **18** ← expand N6 |
| 8 | W→N2→N5 | E | 22 | 0 | 22 |
| 9 | W→N2→N5→N6 | E | 18 | 0 | **18** — target, smallest $f$: done |

**Best path W → N2 → N5 → N6 → E, cost 18.** Read row 8 against row 9 and the compass earns its keep: the *direct* road N5→E costs 11 and gives $f = 22$; the detour through N6 totals 18 — and because row 8's 22 never becomes the smallest $f$, A* never wastes a step on it. Note also what the mark scheme's guidance says about order: rows 3–4 may swap, rows 6–8 may come in any order — *within* one expansion the relaxations are simultaneous; it is the choice of **which vertex to expand next** that is forced. That's the $f$-ranking, and it is where the marks live.

![[graphs-astar-walkthrough.mp4]]

*The exam's own table built row by row at exam pace — each expansion chosen by smallest $f$ before it happens, and the direct-road-versus-detour decision watched in real time.*

## Justifying a graph — §19.1c's ask

The syllabus's own sentence: *"Show understanding that a graph is an example of an ADT. Describe the key features of a graph and justify its use for a given situation."* The recipe, since this is a describe-and-justify mark pair:

- **Features** (pick the ones the scenario needs): a set of vertices/nodes; edges connecting pairs of them; edges may be directed or undirected; edges may be weighted; many-to-many connections and cycles are allowed.
- **Justification** = match the scenario's shape to those features. A road network: junctions are vertices, roads are edges, distances are weights, and junctions connect many-to-many with loops — a list or tree *cannot* represent that, a graph exists for exactly this. Social network: people/vertices, friendships/edges, undirected. Flight prices: airports, routes, directed (outbound ≠ return price) and weighted.

The pattern in every case: name the vertices, name the edges, say whether directed/weighted, and say *why the many-to-many shape rules out the simpler structures*. That last clause is the justification mark.

## Where this runs the world

**Navigation is this card verbatim** — the epigraph's half-second is an adjacency structure over a continent's road network and an A*-family search across it, run every time anyone taps 导航; the heuristics and the priority queues are heavily engineered, but what they compute is this page's two tables. **The internet routes by graph**: routers exchange link-state maps and each one runs shortest-path over the network graph — Dijkstra's algorithm is literally inside the OSPF protocol standard that much of the internet's internal routing runs on. **Search engines rank by graph**: PageRank models the web as a directed graph and scores each page by the structure of what links to it — a graph computation made one of the most valuable companies in history. **Social networks** are the name saying it out loud: friend suggestion is neighbours-of-neighbours, "6 degrees" is BFS depth. **Compilers and build tools** put dependencies in a directed graph and order the work by it — which is also how a spreadsheet knows what to recalculate first. And [[Binary Trees]]' database index, [[Linked List]]'s chain, the vault's own wiki-link web you are reading right now: vertices and edges, all the way down.

## Common Misconceptions (Teaching Notes)

### 1. "Graph = chart"

The English word collides, and 中文 keeps the two apart cleanly: 统计图表 (bar charts, line graphs) share nothing with 图论的图, the vertices-and-edges object of this card. On a CS paper "graph" *always* means this card's object. If a question mentions axes or plotting, it's the other one; if it mentions nodes or edges, it's this one.

### 2. "Trees and graphs are different things"

A tree *is* a graph — a connected one with no cycles (and, when rooted, a direction away from the root). That's not pedantry; it's the bay's architecture: every structure here is a graph plus restrictions, and each restriction bought speed. The exam-relevant edge of this: anything that walks a graph also walks a tree, but tree algorithms (like [[Binary Trees]]' one-comparison-per-level find) lean on the restrictions and die without them.

### 3. "Dijkstra works on any weighted graph"

Only with **non-negative weights**. The settle step's logic — "no other route can improve this vertex, since it would have to pass through something already further away" — silently assumes edges never *reduce* a path's cost. One negative edge and a settled vertex might have been improvable after all. (Road distances and travel times are safely non-negative, which is why navigation never notices; the fix for genuinely negative costs is a different algorithm, and beyond every syllabus here.)

### 4. "Any heuristic makes A* better"

The heuristic must never overestimate, or the optimality guarantee is gone — an inflated $h$ can bury the true best route so deep in the ranking that A* commits to a worse one first. And $h = 0$ is always *admissible*, just useless: it turns A* back into Dijkstra. The exam sidesteps the subtlety by printing the $h$ values on the diagram; your job is only to *spend* them via $f = g + h$, never to invent them.

### 5. "The matrix is the serious representation"

Neither representation is senior. The matrix wins on dense graphs and $O(1)$ edge tests; the list wins on the sparse graphs that real networks overwhelmingly are, and it iterates neighbours without scanning a row of blanks. The exam-ready one-liner: *choose by density*. (And the dictionary-of-neighbours build doubles as a §19.1d-style demonstration that big ADTs are made of smaller ones.)

## Beyond the syllabus

> [!info] Königsberg, 1736 — the whole subject in one walk
> Graph theory has a birthday. The Prussian city of Königsberg had seven bridges linking two islands and two banks, and a standing puzzle: can you stroll the city crossing every bridge exactly once? Euler answered by throwing away everything but the connections — landmasses became vertices, bridges edges, the first graph — and then *counting doors*: each visit to a landmass uses one bridge in and one out, so every vertex except possibly the start and end needs an **even** number of bridges. Königsberg's four vertices all had odd counts; the stroll is impossible, no trial and error required. The move that founded the field is the same move this bay closes on: abstract the connections, forget the geography.

> [!info] The frontier as a heap
> Every algorithm on this card keeps a **frontier** — the discovered-but-unfinished vertices — and the whole family falls out of *how the frontier serves*: a queue gives BFS, a stack gives DFS, a priority queue by $g$ gives Dijkstra, by $g+h$ gives A*. Four algorithms, one skeleton, and the priority queue's efficient engine — the array-packed tree with the vertical promise — is [[Heaps and Priority Queues]], the arithmetic gateway [[Binary Trees]] promised.

> [!info] The fine print between "never overestimates" and "well-behaved"
> Recall that A*'s guarantee was stated for *distance-like* heuristics. The precise fine print: an heuristic that never overestimates is called **admissible**, and one that also never drops faster than the edge you cross ($h(u) \le w + h(v)$, a triangle inequality) is called **consistent**. Straight-line distance is both. But an admissible heuristic that is *jumpy* — honest about totals, erratic between neighbours — can fool the efficient settle-once A* on this card into locking a vertex too early; a patient A* that re-expands whenever a better $g$ appears still finds the optimum. **`graphs-verify.py`, committed beside this card and seeded from today's date**, hunts down real examples every time it runs: today's seed found several jumpy heuristics that fooled the fast variant while the patient one never missed. Run it any morning — different graphs, same theorems — and remember the usual caution: random test graphs are tiny and kind, and real heuristics are *chosen* consistent precisely so the fast variant is safe.

> [!info] Two questions one click apart — where P meets NP on a map
> Recall Königsberg's question: cross every **bridge** (edge) exactly once. Euler solved it *in general* by counting doors — a polynomial check, feasible by hand in 1736. Now change one word: visit every **city** (vertex) exactly once. That is the Hamiltonian cycle problem, and with distances attached, the famous **Travelling Salesman Problem** — and no fast general method is known for either; they are NP-complete territory, the heart of [[P vs NP]]. Meanwhile the problem this card actually solves — *shortest route between two points* — is firmly in **P**: Dijkstra settles each vertex once, roughly $V$ rounds of cheap work, which is the entire miracle. Watch the costs grow: at 10 cities the salesman has $181{,}440$ tours to compare; at 20, about $6 \times 10^{16}$ — two *years* at a billion tours per second; at 25, ten million years — while Dijkstra on the same 25 vertices finishes in microseconds, and on a continent's road network in well under a second. **`graphs-verify.py` demonstrates the chasm every run**: its try-every-path checker has to stop at 7 vertices while the empire shrugs. Same map, three questions — every edge once (easy), shortest route (easy), every vertex once (nobody knows a fast way) — and the boundary between them is the deepest open problem in computer science.

> [!info] Your neural network is an adjacency matrix
> A layer of a neural network *is* a weighted graph: inputs on one side, outputs on the other, a weighted edge for every connection — and the **weight matrix** the GPU multiplies is precisely that graph's adjacency matrix. A *dense* layer is a dense graph (every input connects to every output), so the matrix representation is exactly right, and "run the layer" means "walk every edge" — one matrix multiply. Prune a network — delete the near-zero weights — and it becomes a sparse graph, stored in compressed sparse formats that are the adjacency list wearing industrial clothes. And a **Mixture-of-Experts** model is sparsity one level up: the experts all exist (storage stays dense), but a router activates only a few per token — a sparse *walk* through a dense graph, spending compute like an adjacency list while paying memory like a matrix. The bay's density trade, at the scale of the biggest computations on Earth.

> [!info] Topological order — the graph the queue of your life runs on
> A directed graph with no cycles (a **DAG**) can be flattened into a line where every arrow points forward — a *topological order*. That's how build systems compile files before the files that import them, how spreadsheets recalculate, and how a university checks prerequisite chains. The vault's own `prerequisites` frontmatter is a DAG, and a sensible study order through it is a topological sort.

## Exam Notes

### Cambridge 9618

Graphs sit on the A2 theory side, in two places with one shared boundary — **no graph code is ever demanded**:

- **§19.1c (Paper 3):** "a graph is an example of an ADT — describe the key features and justify its use for a given situation. *Candidates will not be required to write code for a graph structure.*" This is the describe-and-justify recipe above: name vertices/edges, directed/weighted as the scenario demands, and close with why many-to-many rules out list and tree.
- **§18.1 (Paper 3), where the algorithms actually live:** "purpose and structure of a graph; **use A\* and Dijkstra's algorithms to perform searches on a graph**" — *use*, meaning trace by hand; "candidates will not be required to write algorithms to set up, access, or perform searches on graphs." The two question shapes on real papers, both worked above with their published schemes: the **A\* table** (June 2026 P33, June 2023 P32 — path, $g$, $h$, $f$, expand smallest $f$; the given first rows fix the format) and the **Dijkstra trace** (November 2025 P33 — the marks are for initialise 0/∞, visible updates, visited nodes, and evidence of *competing* routes, not just the six final numbers). Dijkstra living in the AI section rather than §19 is a genuine quirk of the 2027–29 syllabus — file it mentally under §18.
- Note the asymmetry against the rest of the bay: stacks, queues, lists and trees must be *written*; graphs are the one structure that is only ever *described, justified and traced*.

### Not examined

- **Cambridge 0478** — no graphs anywhere on the IGCSE.
- **AP CSA** — not in the tested subset; a CSA student meets graphs at university.
- **IB CS (2027)** — B4.1's ADT list names stacks, queues, linked lists and trees only; graphs are not named. Treat as enrichment there until real papers say otherwise.

## Connections

- **Builds on:** [[Binary Trees]] — the last constraint standing (one parent, no cycles), dropped here; [[Hash Tables]] — the dictionary-of-neighbours adjacency list, that card's closing promise cashed; [[Stacks and Queues]] — the queue and stack as BFS's and DFS's engines, the twin disciplines' graduation; [[Big-O Notation]] — the $O(V^2)$-vs-$O(V+E)$ representation trade; [[Recursion]] — DFS's other costume.
- **Leads to:** [[Heaps and Priority Queues]] — the frontier's efficient engine for Dijkstra and A*, and the bay's promised enrichment gateway.
- **Kindred:** [[Arrays]] — the adjacency matrix; [[Linked List]] — the path graph in a straitjacket, and chains as the other adjacency-list build; [[Compilers and Interpreters]] — dependency DAGs and evaluation order; [[Operating Systems]] — resource-allocation graphs and the deadlock cycle; [[P vs NP]] — every-edge-once against every-vertex-once, one click apart on the same map.

## LaTeX Reference

| symbol | LaTeX | meaning here |
|---|---|---|
| $G = (V, E)$ | `G = (V, E)` | a graph: vertices and edges |
| $O(V^2)$ vs $O(V+E)$ | `O(V^2)`, `O(V+E)` | matrix vs list storage |
| $f = g + h$ | `f = g + h` | A*'s ranking: spent + estimated remaining |
| $\infty$ | `\infty` | Dijkstra's "no route found yet" |
