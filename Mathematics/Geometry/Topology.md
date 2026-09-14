---
chinese: 拓扑 (tuòpū) — 拉伸不撕裂的几何
prerequisites:
  - "[[Graphs]]"
  - "[[Solids (Vocab)]]"
leads_to:
  - "[[Four Colour Theorem]]"
  - "[[Knot Theory]]"
  - "[[Hilbert vs Brouwer]]"
tags:
  - subject/mathematics
  - subject/physics
  - subject/computer-science
  - domain/geometry
  - domain/topology
  - level/enrichment
  - level/university
  - type/deep
  - type/cross-domain
  - misconception/topology-is-about-shape
  - misconception/a-mobius-strip-has-two-sides
  - misconception/network-topology-is-a-different-word
---

# Topology 拓扑

> *Throw away the ruler and the protractor. Keep only what survives stretching. What is left is not nothing: it is the number of holes, the order of the stops, which bridges touch which island, whether a loop can be undone. This is the geometry the metro map is drawn in, the geometry your earphone cable knots itself in, and the geometry that won a Nobel Prize in physics for saying that the material does not matter, only its holes.*

## Definition

### Formal

**Topology** is the study of the properties of a shape that are unchanged by **continuous deformation** — stretching, bending, squashing, twisting — but not by tearing or gluing. Two shapes that can be deformed into each other this way are **homeomorphic** ("the same shape" to a topologist). The properties that survive are called **topological invariants**; the simplest is the number of **holes**, captured for a surface by the **Euler characteristic** $\chi = V - E + F$ of any mesh drawn on it, which equals $2 - 2g$ for a closed surface with $g$ holes (its **genus**). A **graph** is a topological object — vertices and the connections between them, with the drawing free — and the subject was founded on one: Euler's 1736 proof that Königsberg's seven bridges cannot be walked in a single tour.

### Intuitive

Geometry asks *how big, how far, what angle*. Topology asks *how connected*. Imagine every object is made of infinitely stretchy rubber that you may pull, but never cut and never glue: a square becomes a circle becomes a blob, so they are one shape; a mug's handle becomes a doughnut's hole, so they are one shape; but no amount of pulling turns a ball into a ring, because a hole cannot be made without tearing. What you are allowed to forget — lengths, angles, straightness — is exactly what a metro map forgets, and what you must keep — which is joined to which — is exactly what it keeps.

### 中文锚点

看一眼地铁站墙上那张线路图：图上每一段距离都是错的，每一处连接都是对的。线被拉直了，弯道没有了，站与站之间画得一样远——不管实际是八百米还是三公里——而且没人介意，因为换乘时你只需要知道站的先后顺序和线在哪里相交。那张图就是一件**拓扑**作品：把尺子扔掉的几何。拓扑问的是：一样东西被拉伸、压扁、弯折——但不撕开、不粘合——之后，什么还留着。一根皮筋拉成方的还是拉成一团，它都是一个圈；**马克杯就是甜甜圈**，因为把手上那个洞，是拉伸怎么都抹不掉的唯一特征；一张纸、一个球、一把勺子是同一个形状；字母 A、D、O、P、Q、R 是同一个字母。**洞有几个**，是怎么拉伸都变不了的那件事，这张卡就把它数了出来：欧拉公式 $V - E + F$，没有洞的立体都等于 2，甜甜圈等于 0——用程序在一张三角形网格上算的。这门学问 1736 年诞生于欧拉的一道题：柯尼斯堡的市民能不能把城里七座桥各走一次、一次走完？不能——而理由跟地图上的距离毫无关系，只跟每块陆地连着几座桥有关。这是历史上第一个说出"形状是连接，不是度量"的证明。上一张卡你已经碰到过同一个想法：网络的**拓扑**——总线、星形、网状——就是把每根网线拉直之后它长什么样。同一个想法还解释了：耳机线为什么在口袋里自己打结，而且那个结是真的（拉是拉不开的）；DNA 为什么专门有一种酶干拓扑的活（把链剪开、从自己中间穿过去、再接上，双螺旋才能解开）；**莫比乌斯带**做的传送带为什么两面磨损均匀（它只有一面——这张卡在动画里把一条沿中线剪开，它不会断成两条）；地球上的风为什么总有一处是静止的（**毛球定理**）；2016 年的诺贝尔物理学奖为什么颁给了三个人——他们发现，一块晶体的边缘导不导电，起决定作用的不是材料，而是洞的个数。考试从来不考这些。这才是重点：这是这本册子里第一张任何考试局都不考的数学卡，也是能解释地铁图的那一张。

| English | 中文 | 今天在哪碰到 |
|---|---|---|
| Topology | 拓扑（学） | 地铁图；上一张卡的网络拓扑 |
| Continuous deformation · homeomorphic | 连续形变 · 同胚 | 皮筋怎么拉都是一个圈 |
| Invariant · genus (number of holes) | 不变量 · 亏格（洞数） | 马克杯 = 甜甜圈 |
| Euler characteristic $V - E + F$ | 欧拉示性数 | 立体的顶点、棱、面 |
| Graph · planar graph | 图 · 平面图 | 柯尼斯堡的桥；电路板能不能一层印完 |
| Möbius strip | 莫比乌斯带 | 一面、一条边的传送带 |
| Knot | 纽结 | 口袋里的耳机线 |
| Fixed point | 不动点 | 搅一杯咖啡，总有一点回到原处 |

---

## Part I — The same shape: what a stretch cannot change

![[topology-mobius.mp4]]

*Scene 1, in three dimensions: a ball becomes a potato becomes a bowl with nothing torn, so they are one shape; a doughnut becomes a mug, and the doughnut's hole becomes the handle's. The only thing the topologist counts is holes. Scene 2 is the Möbius strip, below.*

Sort the objects on your desk the topologist's way and the boxes look strange:

![[topology-holes.svg|960]]

*Zero holes, one hole, two, many. The mug sits with the doughnut; a straw is a ring (a very long one); the letters are sorted by holes. The joke is old and it is also a theorem: genus is an invariant, and two closed surfaces with different genus can never be deformed into each other.*

The number is made precise by **Euler's formula**. Draw any mesh on a surface — corners, edges, faces — and compute $V - E + F$. On anything shaped like a ball it comes out **2**: the five Platonic solids ([[Solids (Vocab)]]) give $4-6+4$, $8-12+6$, $6-12+8$, $20-30+12$, $12-30+20$, all $2$. On a doughnut it comes out **0**, whatever mesh you draw — the script `topology-euler.py` builds a torus as a grid of triangles with the top glued to the bottom and the left to the right, and $9 - 27 + 18 = 0$, $100 - 300 + 200 = 0$, $1000 - 3000 + 2000 = 0$. In general

$$\chi = V - E + F = 2 - 2g,$$

with $g$ the number of holes. The mesh is yours to choose; the answer is the surface's. That is what "invariant" means, and it is why a topologist can tell a mug from a ball without a ruler: count.

> [!info] Why $V - E + F$ does not care about the mesh
> Add a vertex in the middle of an edge: $V$ goes up by one, $E$ goes up by one (the edge is now two), $F$ is unchanged — the sum is the same. Draw a new edge across a face between two existing vertices: $E$ up by one, $F$ up by one (the face is now two) — the same again. Every mesh on a surface can be reached from every other by such moves, so every mesh gives the same number. That number can therefore only depend on the surface itself.

---

## Part II — Königsberg, 1736: shape is connection, not distance

![[topology-konigsberg.svg|960]]

*The city had two islands, two banks and seven bridges, and a standing puzzle: walk the city crossing every bridge exactly once. Euler's move was to throw the map away — shrink each land mass to a dot and each bridge to a line — and count.*

Each time a walk passes *through* a land mass it uses one bridge in and one out, so a land mass visited in the middle of a walk needs an **even** number of bridges; only the start and the end may have an odd number. Königsberg's four land masses have 5, 3, 3 and 3 bridges: four odd counts, and two is the most a walk can accommodate. **No such walk exists**, and no amount of cleverness with the route can help, because the argument never looked at the route. Remove one bridge and two odd counts remain: a walk exists, from one of them to the other. This is the birth of graph theory ([[Graphs]]) and of topology in the same paper, and it is the first proof in history whose content is *connection, not measurement*. The script reproduces the count, and the "remove one bridge" repair.

The same idea, three hundred years later:

- **The circuit board.** Can a circuit be printed on one layer with no wire crossing another? A graph that can be drawn on a page without crossings is **planar**, and Euler's formula on the page ($V - E + F = 2$, counting the outside as a face) forces $E \le 3V - 6$. Five points all joined to each other have $E = 10 > 9$: not planar. Three houses each joined to gas, water and electricity have $E = 9 > 8$: not planar — the old puzzle has no solution, and the script says so in one line. Kuratowski proved in 1930 that these two graphs are the *only* obstacles: every non-planar graph contains a stretched copy of one of them.
- **Kirchhoff's loops.** In [[Kirchhoff's Laws]] you write one loop equation per independent loop, and the count of independent loops in a connected circuit is $E - V + 1$ — branches minus junctions plus one. Redraw the circuit any way you like, cross the wires, straighten them: the count does not change, because it was never a property of the drawing. It is the circuit's first topological invariant, and Kirchhoff proved it in 1847, a century before anyone called it that.
- **The network you drew last card.** Bus, star, mesh, hybrid ([[The Internet and the Web]]): a network's *topology* is what it looks like after every cable has been pulled straight and every distance forgotten. A star with the switch in a cupboard and a star with the switch on the desk are the same topology, and behave the same when a cable fails. The word is the same word, used in the same sense.

---

## Part III — The metro map: topology you use every week

![[topology-metro-map.svg|760]]

*Left, the line on the ground: it bends with the river and the stops are unevenly spaced. Right, the line on the wall: straightened, evenly spaced, wrong in every distance and right in every connection. Harry Beck, an electrical draughtsman, drew the London Underground this way in 1933, because a circuit diagram is a topological map too, and every metro on Earth has copied it since.*

To change trains you need the **order** of the stops and the **junctions** where lines meet; you do not need the distances, the bends or the compass directions. Beck's insight was that a map may throw those away, and be *better* for it. Every navigation app does the same thing in software: the road network is stored as a graph — junctions and the roads between them — and the route is found on the graph ([[Graphs]], Dijkstra and A*); the pretty picture is drawn afterwards.

Two more everyday cases of the same abstraction:

- **A knot is a real thing.** Take a loop of string with an overhand knot tied in it and a loop without. No stretching turns one into the other, because "can be undone without cutting" is a topological property — and it is a hard one: deciding whether a tangled loop is really knotted was only proved decidable in 1961, and fast algorithms are still research. Your earphone cable knots itself in a pocket for the same reason a random walk gets lost: with enough jostling, almost every long loose string ends up in a configuration it cannot stretch out of ([[Knot Theory]]).
- **DNA has a topology problem, and an enzyme for it.** The double helix is two strands wound around each other; to copy or read it the strands must be separated, and pulling two intertwined loops apart is topologically impossible without cutting. So the cell keeps **topoisomerases**: enzymes that cut a strand, pass the other through the gap, and reseal — a controlled tear and glue, the two operations topology forbids, performed billions of times a day so that the chemistry can proceed. Several antibiotics and chemotherapy drugs work by jamming them.

---

## Part IV — The Möbius strip: one side, one edge

Take a strip of paper, give one end a half twist, and glue the ends. The result, the **Möbius strip** (1858), has **one side**: start painting the "top" and you return to your starting point having painted everything, with no "bottom" left. It has **one edge**, for the same reason. The clip above walks a point along the middle line — after one lap it is underneath, after two it is home — and then cuts the strip along that line. It does not fall into two rings. It becomes **one** ring, twice as long, with two full twists, because the cut line, like the strip, has only one side to be on.

Where it earns its keep: a **conveyor belt** or a drive belt made as a Möbius strip wears both faces evenly, since it has only one face — a design patented in 1957 and used in continuous-loop recording tapes and typewriter ribbons. And it is the simplest **non-orientable** surface, the first of a family (the Klein bottle, the projective plane) on which "clockwise" cannot be defined globally — which is the kind of thing a physicist needs to know before trusting a coordinate system.

---

## Part V — Where topology decides: three theorems with consequences

**The hairy-ball theorem.** A sphere covered in hair cannot be combed flat with no parting and no tuft: every continuous tangent field on a sphere has a zero. So at every instant there is at least one point on Earth where the horizontal wind is exactly zero — not by weather, by topology. (On a doughnut it can be done, which is one reason tokamak fusion reactors are doughnuts: the confining magnetic field must be everywhere non-zero on the surface, and only a torus allows it.)

**The fixed-point theorem.** Stir a cup of coffee, however thoroughly, and let it settle: some point of the liquid is exactly where it started. Lay a map of Chengdu on the ground in Chengdu: some point of the map lies directly above the point it represents. Brouwer proved in 1911 that any continuous map of a disc (or a ball) to itself leaves at least one point fixed; economists used it to prove that markets have equilibrium prices, and game theorists to prove that every finite game has a Nash equilibrium. The same Brouwer who, in [[Hilbert vs Brouwer]], rejected proofs like this one for not *constructing* the point.

**Topological phases of matter.** In 2016 the Nobel Prize in Physics went to Thouless, Haldane and Kosterlitz for showing that some properties of materials are governed by a topological invariant — an integer like the number of holes — rather than by the material's chemistry. The quantised Hall conductance of a two-dimensional electron gas is an integer times $e^2/h$ to one part in a billion, because it *is* an integer: a winding number of the electrons' quantum state, which cannot change by a small amount any more than a doughnut can grow half a hole. **Topological insulators** conduct on their surface and not in their bulk for the same reason, and the conduction survives dirt, defects and disorder that would kill any ordinary conductor, because the invariant does. That robustness is why they are candidates for quantum-computer components ([[Quantum Computing]]): a qubit whose state is a topological invariant does not lose it to noise.

---

## Where this surfaces in the vault

- **[[Graphs]]** — the Königsberg walk and its degree count are already the birthday of graph theory there; this card is the other half of the same paper.
- **[[Solids (Vocab)]]** and **[[Geometrical Terms (Vocab)]]** — Euler's polyhedron formula, stated there for convex solids; here it becomes $2 - 2g$ and stops needing convexity.
- **[[Kirchhoff's Laws]]** — the loop count $E - V + 1$ is topological; that is why "how many loop equations do I need?" has an answer before the circuit is drawn.
- **[[The Internet and the Web]]** and **[[Networks]]** — bus, star, mesh: topology in the same sense, on cables.
- **[[Complex Numbers]]** — the argument of a complex number winding round the origin is the first winding number a student meets, and the 2016 prize is a winding number.
- **[[Cantor vs Kronecker]]** — Cantor's square-equals-line pairing is *not* continuous; that topology can tell a line from a square where counting cannot is the resolution of "I see it but I do not believe it".

## Hands-on

- **Count.** `python3 topology-euler.py` — Euler's formula on the five Platonic solids and on a glued grid (a torus), the Königsberg degrees with the one-bridge repair, the planarity test on K5 and K3,3, and the loop count of four circuits.
- **Cut.** Make a Möbius strip from a strip of paper (one half twist), draw a line along the middle without lifting the pen until you meet your start, then cut along it. Then make another and cut it a third of the way in from the edge: two linked rings, one of them a Möbius strip.
- **Comb.** Try to comb a tennis ball with a felt pen — draw short arrows everywhere, all tangent, no gaps. Wherever you fail is the theorem.

## Misconceptions

- **"Topology is about the shape of things."** It is about what is *left* of the shape when size, distance and angle are removed: connection and holes. A topologist cannot tell a circle from a square, and does not want to.
- **"A Möbius strip has two sides, just twisted."** One side, one edge; the clip's point walks both "sides" without crossing the edge. The cut that should split it does not.
- **"Network topology is a different word."** It is the same word in the same sense: the shape of the connections with the cable lengths forgotten.
- **"Stretching a line into a square proves a line has as many points as a square."** Cantor proved the point-count is the same by a pairing that is not continuous; topology proves the *shapes* differ — a line and a square are not homeomorphic, because removing one point disconnects a line and never a square. Both are true; they answer different questions.

## Exam Notes

**Not examined on any board the vault covers.** Cambridge 0580, 0606, 9709 and 9231, OxfordAQA 9260 and 9660, Edexcel IAL, IB AA and AI, AP Calculus: none has a topology outcome. The nearest footholds are Euler's polyhedron formula (stated in some IGCSE textbooks, never set on 0580), graphs and shortest paths in 9618 §19 and IB CS B, and Kirchhoff's loop equations in 9702 §10.2. This card is enrichment in the sense the vault means it: mathematics a student will meet in the first year of any physics, computer science or mathematics degree, given early because it explains things they already use.

## Sources

- L. Euler, *Solutio problematis ad geometriam situs pertinentis* (1736) — the seven bridges; the phrase *geometria situs*, "geometry of position", is the subject's first name. L. Euler, the polyhedron formula (1758). A. F. Möbius (1858) and J. B. Listing (1858), the strip. K. Kuratowski (1930), planarity. G. Kirchhoff (1847), the loop count. L. E. J. Brouwer (1911), the fixed-point theorem. H. Beck, the London Underground diagram (1933).
- D. J. Thouless, F. D. M. Haldane, J. M. Kosterlitz — Nobel Prize in Physics 2016, "for theoretical discoveries of topological phase transitions and topological phases of matter"; the Nobel committee's popular and advanced information (2016).
- J. C. Wang, *DNA topoisomerases*, Annual Review of Biochemistry 65 (1996). W. Haken (1961), the unknotting problem is decidable.
- The script beside this card: `topology-euler.py`; the Manim source `topology-mobius.py`.
