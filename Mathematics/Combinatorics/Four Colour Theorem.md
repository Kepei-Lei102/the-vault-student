---
chinese: 四色定理 (sì sè dìnglǐ)
prerequisites:
  - "[[Topology]]"
  - "[[Graphs]]"
  - "[[Proof by Induction]]"
leads_to:
  - "[[Learning as Verification]]"
  - "[[Compilers and Interpreters]]"
  - "[[P vs NP]]"
tags:
  - subject/mathematics
  - subject/computer-science
  - domain/combinatorics
  - domain/graph-theory
  - level/enrichment
  - level/university
  - type/deep
  - type/theorem
  - type/cross-domain
  - misconception/touching-at-a-point-counts-as-adjacent
  - misconception/four-colours-are-needed-because-of-k4
  - misconception/a-computer-proof-is-not-a-proof
  - misconception/greedy-colouring-uses-four
  - misconception/the-theorem-holds-for-any-map
---

# Four Colour Theorem 四色定理

> *In 1852 a student colouring a map of the English counties noticed that four colours were enough to keep every pair of neighbouring counties different, and wondered whether four would always do. The question could be stated to a child. It took 124 years to answer, the answer needed a computer, and the mathematical world spent the next thirty years arguing about whether an answer no human could read counted as a proof. Along the way it produced a beautiful wrong proof that stood for eleven years, a right proof of a weaker theorem that every student can follow, and the first serious quarrel about what "proof" means in the age of machines — which is why this card ends where [[Learning as Verification]] begins.*

## Definition

### Formal

**The Four Colour Theorem.** Every map drawn in the plane (or on a sphere) can be coloured with at most **four** colours so that no two regions sharing a boundary *line* receive the same colour.

The fine print is the whole theorem:

- A **region** is connected — one piece. A country with an overseas territory counts as two regions.
- Two regions are **adjacent** only if they share a boundary of positive length. Meeting at a single point (like four states at the Four Corners) does not count.
- The map may have any number of regions, any shapes; the outside "ocean" is a region too.

In the language of [[Graphs]]: replace each region by a vertex and join two vertices when their regions are adjacent. The result is a **planar graph** — one that can be drawn with no edges crossing — and colouring the map is colouring the vertices so that no edge joins two vertices of the same colour. The **chromatic number** $\chi(G)$ is the fewest colours that achieve this. The theorem says: **every planar graph has $\chi \leq 4$.**

### Intuitive

Some maps need four colours — the figure below has four countries that all touch one another, and no three colours can separate four mutual neighbours. So four is *necessary*. The theorem is the other direction: four is always *sufficient*, however many countries and however cunningly they wrap round one another. That direction is hard because a fifth colour is never forced by a small local obstruction — five countries cannot all touch one another in the plane — but only, if at all, by some vast conspiracy across the whole map. Proving that no such conspiracy exists is what took 124 years.

### 中文锚点

翻开地图册看中国的省份图：相邻两个省颜色不同，整张图只用了四种颜色。这不是画图的人省颜料，而是**任何**画在平面上的地图，四种颜色都够——这就是四色定理。"够"分两层：有些地图**必须**四种（画四块两两相邻的地，三种颜色一定撞色，这很容易），但没有任何地图需要第五种（这很难，难了 124 年）。理解它的钥匙是把地图翻译成一张**图**：每个国家缩成一个点，接壤的两国之间连一条线——注意只在一点相碰不算接壤，就像四个小区只在一个路口相遇。这张图画在纸上不会有线相交，叫**平面图**，欧拉公式 $V - E + F = 2$ 管着它，从它能推出：任何一张平面图里，总有一个点的邻居不超过 5 个。于是**六色**很容易证（把那个点先拿掉，剩下的图先染好，再放回去，六种颜色里总有一种它的邻居没用过），**五色**用一个"换色链"的巧招也能证，而**四色**——1879 年肯普正是用这个思路给出了一个漂亮的证明，全世界信了 11 年，1890 年希伍德发现它错了；真正的证明要等到 1976 年，阿佩尔和哈肯用计算机检验了近两千种"不可避免的局部构型"，算了一千二百小时。这是数学史上第一个人类读不完的证明，也因此引出了一个新问题：**读不完的证明，算不算证明？**

> [!info] Symbols in this card
> | Symbol | Meaning | 中文 |
> |---|---|---|
> | $V$, $E$, $F$ | vertices, edges, faces of a planar drawing | 顶点、边、面 |
> | $\chi(G)$ | chromatic number — fewest colours for a proper colouring | 色数 |
> | $\deg(v)$ | degree — number of edges at vertex $v$ | 度 |
> | $K_n$ | the complete graph: $n$ vertices, every pair joined | 完全图 |
> | Kempe chain | a maximal connected set of vertices using only two given colours | 肯普链 |

## Part I — A question a child could ask (1852–1878)

Francis Guthrie was colouring a map of England's counties when he noticed that four colours sufficed, and that he could not find a map needing five. He asked his brother Frederick, a student of Augustus De Morgan at University College London, and on 23 October 1852 De Morgan wrote to William Rowan Hamilton in Dublin: a student had asked him whether four colours always suffice, and he could neither prove it nor find a counterexample. Hamilton replied that he was unlikely to attempt it "very soon". Nobody else did either. The question surfaced in print only in 1878, when Arthur Cayley asked the London Mathematical Society whether it had been solved, and confessed he could not see how to do it.

Notice what Cayley could see. The difficulty is not that five colours might be needed by some small cluster — five regions cannot all touch one another, as the next part proves. The difficulty is that a colouring is a *global* commitment: a choice made in Cornwall may, through a long chain of forced choices, run out of options in Northumberland. Any proof has to show that no map, however large, can force that.

## Part II — From map to graph, and what Euler forbids

![[four-colour-dual.svg|1000]]

Shrink each country to a point and draw a line between two points when their countries share a border. Because the borders lie in the plane and do not cross, neither do the lines: the **dual graph** of a map is always **planar**. A colouring of the map is exactly a colouring of the dual graph's vertices with no edge monochromatic, so from here on the theorem is about planar graphs and the maps can be forgotten.

Planar graphs obey [[Topology]]'s **Euler formula**. Draw one with $V$ vertices and $E$ edges; the drawing cuts the plane into $F$ faces, counting the unbounded outside as one; then for a connected planar graph

$$V - E + F = 2 .$$

That single identity has two consequences that carry the whole subject.

**Planar graphs are sparse: $E \leq 3V - 6$ (for $V \geq 3$).** Every face is bounded by at least three edges, and every edge borders at most two faces, so $3F \leq 2E$. Substitute $F = 2 - V + E$: $3(2 - V + E) \leq 2E$, i.e. $E \leq 3V - 6$. In the figure, seven countries have twelve borders, and $3 \times 7 - 6 = 15$ leaves room; a triangulation uses the room up exactly.

**Every planar graph has a vertex of degree at most 5.** The degrees add up to twice the number of edges (each edge has two ends), so the *average* degree is $2E/V \leq (6V - 12)/V < 6$. An average below six means some vertex has degree 5 or less. This is the lever every proof in this card pulls.

![[four-colour-k4-k5.svg|1000]]

The same inequality shows why five mutual neighbours are impossible. Five countries that all touch would give the complete graph $K_5$: five vertices, ten edges. But $3V - 6 = 9$ for five vertices, so $K_5$ is not planar — one border would have to cross another. Four mutual neighbours ($K_4$: six edges, allowed) are the most the plane permits, which is why four colours are *necessary* for some maps and why nobody could ever draw a map that obviously needed five. `four-colour-solver.py` builds hundreds of random planar graphs, checks $V - E + F = 2$ on every one, and confirms the average degree is always below six and the minimum degree at most five.

## Part III — Six colours: a proof you can give in a minute

*Claim: every planar graph can be properly coloured with six colours.*

*Tool: [[Proof by Induction]] on the number of vertices. Trigger: the lever — a vertex with at most five neighbours always exists, and removing a vertex keeps a graph planar.*

A graph with six or fewer vertices is trivially six-colourable — give each vertex its own colour. Now suppose every planar graph with fewer than $n$ vertices is six-colourable, and take a planar graph $G$ with $n$ vertices. Find a vertex $v$ with $\deg(v) \leq 5$; it exists by Part II. Delete $v$. What remains is planar with $n - 1$ vertices, so by the induction hypothesis it has a proper six-colouring. Put $v$ back. Its neighbours — at most five of them — use at most five colours between them, so one of the six colours is unused among them; give $v$ that colour. Every edge is now properly coloured. $\blacksquare$

That is the *whole* proof, and it is an algorithm: **peel** the graph by repeatedly removing a minimum-degree vertex, then **paint** the vertices back in reverse order, each taking a free colour. The animation below runs it, and `four-colour-solver.py` runs it on triangulations of 250 vertices — where in practice it never needed more than five.

![[four-colour-manim.mp4]]

## Part IV — Five colours: Heawood's chain trick (1890)

*Claim: every planar graph can be properly coloured with five colours.*

Run the same induction with five colours. Delete a vertex $v$ of degree at most 5, five-colour the rest, put $v$ back. If $\deg(v) \leq 4$, or if its five neighbours happen to repeat a colour, there is a free colour and we are done as before. The only hard case: **$v$ has exactly five neighbours and they use all five colours.** Call them $v_1, \dots, v_5$ in order round $v$, coloured $c_1, \dots, c_5$.

![[four-colour-kempe.svg|1000]]

Look at $v_1$ (colour $c_1$) and $v_3$ (colour $c_3$), which are not next to each other round $v$. Consider the **Kempe chain** from $v_1$: the set of all vertices reachable from $v_1$ by walking only through vertices coloured $c_1$ or $c_3$. Two cases.

- **$v_3$ is not in the chain.** Then swap $c_1 \leftrightarrow c_3$ throughout the chain. Every edge inside the chain stays two-coloured; every edge leaving the chain still joins a $c_1/c_3$ vertex to a vertex of some other colour, because if a neighbour had colour $c_1$ or $c_3$ it would be *in* the chain. So the colouring stays proper — and now $v_1$ is coloured $c_3$, no neighbour of $v$ has colour $c_1$, and $v$ takes $c_1$. Done.
- **$v_3$ is in the chain.** Then a path of $c_1/c_3$ vertices runs from $v_1$ round to $v_3$. Together with $v$ it forms a closed curve, and — this is where planarity is used, and it is the only place — the curve separates $v_2$ (inside it) from $v_4$ (outside it). So the $c_2/c_4$ Kempe chain from $v_2$ cannot reach $v_4$: to do so it would have to cross the $c_1/c_3$ curve, and the crossing vertex would have to carry two colours at once. Swap $c_2 \leftrightarrow c_4$ on $v_2$'s chain instead; $c_2$ is freed at $v$, and $v$ takes it. $\blacksquare$

The swap is the engine. `four-colour-solver.py` implements it exactly — peel, paint, swap when stuck — and counts how often the swap was actually needed. The animation's second scene traces one.

## Part V — The proof that was wrong for eleven years (1879–1890)

Alfred Kempe, a barrister and amateur mathematician, published a proof of the *four* colour theorem in 1879. It was celebrated; he was elected a Fellow of the Royal Society; the theorem was considered settled. His method was Part IV's, pushed one colour further. With four colours, the only hard case is a vertex $v$ of degree 5 whose neighbours use all four colours — so one colour appears twice, say $c_1, c_2, c_3, c_4, c_2$ round the circle. Kempe found two Kempe chains — from the $c_1$ neighbour and from the $c_3$ neighbour, each against the colour on the far side — and argued that if both were blocked by encircling chains, a *double* swap frees a colour.

In 1890 Percy Heawood found the hole. Kempe's two swaps are each fine on their own, but the second is carried out on a colouring that the first has already changed — and the second chain can run through vertices the first swap recoloured, so that after both swaps two adjacent vertices can share a colour. Heawood exhibited a map on which Kempe's procedure fails. He could not repair it. What he *could* salvage was that a single swap always works when there are five colours to play with — Part IV, which is called the Five Colour Theorem for that reason and is Heawood's, not Kempe's.

`four-colour-solver.py` re-enacts the failure: it deletes each degree-5 vertex of a random triangulation, four-colours the rest, and where the neighbours show the $c_1 c_2 c_3 c_4 c_2$ pattern it runs Kempe's argument exactly as he wrote it — one swap if a chain is blocked, the double swap if both are. In 120 triangulations of forty vertices the double swap was needed 75 times and **broke the colouring 27 of them**. Kempe's step fails about a third of the times it is invoked; the flaw hid for eleven years only because nobody ran it.

Kempe's idea was not wasted. The *shape* of his argument — show that every planar graph must contain one of a short list of local configurations (an **unavoidable set**), then show that each configuration can be recoloured away (each is **reducible**) — is precisely the shape of the proof that eventually worked. He had the right plan with a list that was too short and a reducibility argument that was too optimistic.

## Part VI — Four colours suffice (1976), and the argument about what a proof is

![[four-colour-appel-haken-comic.png|640]]

For eighty years after Heawood the strategy was clear and the arithmetic was not. Heinrich Heesch, working from the 1930s, developed the two ideas that made it feasible: **discharging**, a bookkeeping method in which each vertex is given a "charge" $6 - \deg(v)$ (which sums, by Euler, to exactly $12$) and the charges are moved around by rules so that a positive charge must end up on one of a listed set of configurations — proving the set unavoidable — and computer tests for **reducibility**. The list, though, ran to thousands of configurations, and checking each by hand was hopeless.

In 1976 Kenneth Appel and Wolfgang Haken at the University of Illinois, with John Koch's programming, completed it: an unavoidable set of **1,936 configurations** (later trimmed to 1,482), each shown reducible by computer, after some **1,200 hours** of machine time on an IBM 370. Every planar graph contains one of the configurations; none of them can appear in a minimal counterexample; so there is no counterexample. The Illinois mathematics department's postage meter stamped outgoing mail *FOUR COLORS SUFFICE.*

And the argument began. The proof's unavoidability part was a 50-page discharging argument with hundreds of hand-checked cases; its reducibility part was a computer output nobody could read. The philosopher Thomas Tymoczko asked in 1979 whether a theorem whose proof cannot be surveyed by a human is known in the same sense as other theorems, or is more like an experimental result. Mathematicians found small errors in the hand part for years, each repaired. In 1997 Neil Robertson, Daniel Sanders, Paul Seymour and Robin Thomas gave a cleaner proof — 633 configurations, a simpler discharging procedure, and a program short enough to publish — but still a computer proof. The last word, so far, came in 2005: Georges Gonthier formalised the whole argument inside the proof assistant Coq, so that every step, human and machine, is checked by a small trusted kernel. The proof is still unreadable by a person. The *checker* is not.

That is the resolution that matters beyond this theorem, and [[Learning as Verification]] builds on it: you do not need to be able to *produce* a proof to *know* a theorem — you need a checker you trust, and the checker can be small even when the proof is enormous. Nobody has found a short proof. It is possible there is none.

## Where it is the working tool

- **Register allocation in compilers.** A program's variables are vertices; two are joined if they are live at the same time; the CPU's registers are the colours. Colouring the *interference graph* with $k$ colours assigns $k$ registers with no clash, and when the graph will not $k$-colour, a variable is spilled to memory. Chaitin's 1981 allocator is graph colouring, and it is the optimisation that makes compiled code fast — [[Compilers and Interpreters]]' code-generation stage is doing Part III's peel-and-paint on every function you compile.
- **Radio frequencies.** Transmitters are vertices, joined when they are close enough to interfere; frequencies are colours. Mobile networks, Wi-Fi channels and broadcast licences are all colouring problems, and the planar-ish structure of a map is why a handful of channels serve a whole country.
- **Timetables.** Exams are vertices, joined when a student sits both; time slots are colours. Every school's exam timetable is a chromatic number computed by a person with a spreadsheet.
- **Sudoku** is a 9-colouring problem on a graph of 81 vertices (joined when in the same row, column or box), with 17 or more vertices pre-coloured.
- **Cartographers never needed the theorem.** Four colours were enough in practice long before 1852 and printers used more anyway, for the ocean and for clarity. The theorem's importance was never the maps; it was the method — and the quarrel.

## Hands-on

- **`four-colour-solver.py`** — random planar graphs from Delaunay triangulations and random Voronoi "maps"; Euler's formula and the degree-5 lever verified on each; the six-colour peel, Heawood's five-colour swap with the swaps counted, an exact colourer for the chromatic number, and Kempe's double swap reproduced until it fails. Change the seed; the theorem does not.
- **`four-colour-figures.py`** — the figures, including a forty-country map four-coloured by search. Set the seed to your own and see whether three colours would have done (for random maps, almost never).
- **`four-colour-manim.py`** — the peel-and-paint scene and the Kempe swap.
- **A map and four pencils.** Colour the provinces of China, or the counties of your own country, with four pencils and no plan. You will get stuck; back up two provinces and try again. The getting stuck is Cayley's difficulty; the backing up is what the exact colourer does thousands of times a second.

## Common Misconceptions (Teaching Notes)

### 1. "Regions that meet at a point are adjacent"
They are not, and the theorem would be false if they were: cut a pie into $n$ slices meeting at the centre and $n$ colours would be needed. Adjacency needs a shared boundary *line*.

### 2. "Four colours are needed *because* four countries can all touch"
That shows four are *necessary*, in one sentence. The theorem is that four are *sufficient*, for every map; it is a claim about the absence of a global obstruction, not a local one, which is why it is hard and why $K_5$'s non-planarity does not prove it.

### 3. "The theorem applies to any map"
A country with an exclave is two regions that must share a colour, and with enough such countries any number of colours can be forced. The theorem is for connected regions in the plane or on a sphere; on a torus the answer is seven (Heawood, proved by Ringel and Youngs in 1968).

### 4. "A computer proof is not a real proof" — and its opposite, "it has since been proved by hand"
Neither. The 1976 and 1997 proofs are valid proofs whose reducibility checks are machine computations, and Gonthier's 2005 formalisation is the most thoroughly *verified* proof of any major theorem. No human-readable proof exists. Both halves of the popular version are false.

### 5. "Colour greedily and you'll use at most four"
Greedy colouring — each vertex takes the lowest colour not used by its already-coloured neighbours — can use five or six on a planar graph in a bad order, and the peel order of Part III only guarantees six. Getting down to four requires the reducibility machinery or backtracking; there is no simple procedure, and `four-colour-solver.py` shows the exact colourer at work.

## Exam Notes

### Where it is examined — nowhere on the vault's boards

The Four Colour Theorem is not an examinable result on any Cambridge, IB or AP syllabus tracked here, and this card is enrichment. The neighbouring material that *is* examined:

- **IB Mathematics: Applications and Interpretation HL (3.15–3.16)** — graph theory as adjacency matrices, walks and trails, Eulerian and Hamiltonian graphs, minimum spanning trees, the Chinese postman and travelling salesman problems. Planarity and colouring are not on the list, but the vocabulary of vertices, edges, degrees and the handshaking lemma (the degrees sum to $2E$, used in Part II) is.
- **Edexcel Decision Mathematics (D1)** — algorithms on graphs, including whether a graph is planar; never colouring.
- **Cambridge 9618 §18.1 / §19.1c** — graphs as a data structure, Dijkstra and A*, in [[Graphs]]; no colouring.
- **Not examined at all:** Cambridge 0580, 0606, 9709, 9231; AP Calculus and AP Statistics; OxAQA 9260 and 9660.

## Connections

- **Built on:** [[Topology]] — Euler's formula $V - E + F = 2$ and the planarity it polices; [[Graphs]] — vertices, edges, adjacency, and Königsberg's degree count as the first argument of the same kind; [[Proof by Induction]] — the six- and five-colour proofs are inductions on $V$.
- **Same reasoning elsewhere:** [[Hilbert vs Brouwer]] — the constructive question of whether a proof that only *exists* counts, asked here of a proof that exists only inside a machine.
- **Extends into:** [[Learning as Verification]] — the small trusted checker as the answer to the unreadable proof; [[P vs NP]] — deciding whether a planar graph is 3-colourable is NP-complete, while a 4-colouring can always be *found* in polynomial time, the strangest gap between two consecutive integers in the subject; [[Compilers and Interpreters]] — register allocation as graph colouring.

## Beyond Syllabus

### Other surfaces: Heawood's formula
On a surface with $g$ holes the Euler characteristic is $2 - 2g$, the sparsity bound changes, and the number of colours that always suffices is $\left\lfloor \frac{7 + \sqrt{1 + 48g}}{2} \right\rfloor$: seven on a torus, eight on a two-holed surface. Heawood conjectured this in 1890 and Ringel and Youngs proved it in 1968 — *before* the plane's own case was settled, because the plane is the one surface where the formula's argument breaks down ($g = 0$ gives four, but the proof of sufficiency does not go through). The hardest case of the theorem was the one a child had asked about.

### Grötzsch, and colouring with fewer
A planar graph with no triangles is 3-colourable (Grötzsch, 1959). A planar graph is 2-colourable exactly when every face has an even number of edges — a checkerboard. Each step down in the colour count is a step up in the structure demanded.

### The chromatic polynomial
Count the proper colourings of a graph with $k$ colours and the answer is a polynomial in $k$: for a triangle, $k(k-1)(k-2)$; for a tree on $n$ vertices, $k(k-1)^{n-1}$. Birkhoff introduced it in 1912 hoping to prove the theorem by showing the polynomial of every planar graph is positive at $k = 4$. It never worked, but the polynomial became a subject of its own.

### What the computer actually checks
A configuration is *reducible* if any colouring of the ring of vertices surrounding it, in a minimal counterexample, could be extended inside — after Kempe-chain adjustments — to a four-colouring of the whole; showing this means enumerating the ring colourings (a ring of size 14 has several hundred thousand) and applying chain arguments to each. The 1997 proof's programs are a few thousand lines and are published; the point of Gonthier's 2005 work was that even those lines no longer have to be trusted, only Coq's kernel.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $V - E + F = 2$ | `V - E + F = 2` | Euler, connected planar graph, outer face counted |
| $E \leq 3V - 6$ | `E \leq 3V - 6` | planar sparsity, $V \geq 3$ |
| $\chi(G) \leq 4$ | `\chi(G) \leq 4` | the theorem for planar $G$ |
| $\left\lfloor \frac{7 + \sqrt{1 + 48g}}{2} \right\rfloor$ | `\left\lfloor \frac{7 + \sqrt{1 + 48g}}{2} \right\rfloor` | Heawood's bound on a surface of genus $g$ |
| $k(k-1)^{n-1}$ | `k(k-1)^{n-1}` | chromatic polynomial of a tree |

## Sources

- A. De Morgan to W. R. Hamilton, letter of 23 October 1852; A. Cayley, "On the colouring of maps", *Proc. Royal Geographical Society* 1 (1879).
- A. B. Kempe, "On the geographical problem of the four colours", *American Journal of Mathematics* 2 (1879); P. J. Heawood, "Map-colour theorem", *Quarterly Journal of Mathematics* 24 (1890).
- K. Appel and W. Haken, "Every planar map is four colorable", *Illinois Journal of Mathematics* 21 (1977), parts I and II (with J. Koch); T. Tymoczko, "The four-color problem and its philosophical significance", *Journal of Philosophy* 76 (1979).
- N. Robertson, D. Sanders, P. Seymour and R. Thomas, "The four-colour theorem", *Journal of Combinatorial Theory B* 70 (1997); G. Gonthier, "Formal proof — the four-color theorem", *Notices of the AMS* 55 (2008).
- R. Wilson, *Four Colours Suffice* (2002) — the full history, including the postmark.
- G. Chaitin et al., "Register allocation via coloring", *Computer Languages* 6 (1981).
- The scripts beside this card: `four-colour-solver.py`, `four-colour-figures.py`, `four-colour-manim.py`.
