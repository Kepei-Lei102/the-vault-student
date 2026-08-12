---
chinese: 几何术语 (jǐhé shùyǔ)
prerequisites: []
leads_to:
  - "[[Triangles (Vocab)]]"
  - "[[Quadrilaterals (Vocab)]]"
  - "[[Polygon Angles (Vocab)]]"
  - "[[Solids (Vocab)]]"
  - "[[Geometrical Constructions (Vocab)]]"
  - "[[Angle Properties (Vocab)]]"
  - "[[Area and Perimeter (Vocab)]]"
  - "[[Nets (Vocab)]]"
  - "[[Symmetry (Vocab)]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-G1
  - syllabus/0580-E4-1
  - type/vocabulary
  - misconception/line-vs-segment
  - misconception/edge-vs-side
---

# Geometrical Terms 几何术语

## Definition

**Geometrical terms** are the basic vocabulary every later geometry card uses — point, line, plane, vertex, edge, face, parallel, perpendicular, polygon, and so on. They are the *grammar* of geometry. A student who is unsure whether a "side" of a triangle and an "edge" of a cube are the same kind of thing will read every geometry question more slowly than they need to.

This card is a **vocabulary anchor**. The deeper geometry cards (triangles, quadrilaterals, circles, solids, transformations) all assume these terms; a single source of truth keeps them consistent and saves later cards from re-defining the basics.

### 中文锚点

几何术语 = 几何里的基本词汇。点 (point)、线 (line)、面 (plane)、顶点 (vertex)、棱/边 (edge)、面 (face)、平行 (parallel)、垂直 (perpendicular)、多边形 (polygon) 等等。这些是其他几何卡的"地基"。考试题用英文出，中文术语在脑子里，所以这张卡的目的就是建立中英对照，让后面的几何题读起来更快。

---

## The Building Blocks: Points, Lines, Planes

| English | 中文 | What it is |
|---------|------|------------|
| point | 点 (diǎn) | a location with no size — usually drawn as a dot, labelled $P$, $A$, $B$, … |
| line | 直线 (zhíxiàn) | extends infinitely in **both** directions; symbol $\overleftrightarrow{AB}$ (rare) |
| ray | 射线 (shèxiàn) | extends infinitely from a point in **one** direction; symbol $\overrightarrow{AB}$ |
| line segment | 线段 (xiànduàn) | the part of a line **between** two endpoints; symbol $\overline{AB}$ |
| plane | 平面 (píngmiàn) | a flat 2D surface extending infinitely in all directions |
| solid | 立体 (lìtǐ) | a 3D region — see [[Solids (Vocab)]] |

> [!tip] Line vs segment vs ray — exam wording
> When a Cambridge question says "the line $AB$" it usually means the **line segment** $AB$ (with endpoints $A$ and $B$). When it says "the line through $A$ and $B$" it means the full infinite line. The shorter form is the more common one — but watch for "produced" or "extended", which mean *extend the segment* into a longer one (or into a ray).

---

## Polygon Family

A **polygon** (多边形) is a closed plane figure made of line segments — every side is a straight line. The pieces:

| English | 中文 | Notes |
|---------|------|-------|
| polygon | 多边形 | closed figure with straight sides |
| side | 边 (biān) | one of the line segments forming the polygon |
| vertex (pl. vertices) | 顶点 (dǐngdiǎn) | a corner where two sides meet |
| interior angle | 内角 | angle inside the polygon at a vertex |
| exterior angle | 外角 | angle between one side and the *extension* of the next side |
| diagonal | 对角线 | line segment joining two non-adjacent vertices |
| regular polygon | 正多边形 | all sides equal AND all angles equal |
| convex | 凸 (tū) | every interior angle $< 180°$; no "dents" |
| concave / re-entrant | 凹 (āo) / 凹的 | at least one interior angle $> 180°$ |

The polygon-name table for sides $n = 3, 4, 5, \dots$ is in [[Polygon Angles (Vocab)]] (triangle, quadrilateral, pentagon, hexagon, …). For the special families see [[Triangles (Vocab)]] and [[Quadrilaterals (Vocab)]].

> [!tip] "Side" vs "edge" — this is the first thing students mix up
> In **2D** (a polygon), the line segments are called **sides**. In **3D** (a polyhedron), the line segments where two faces meet are called **edges**. A triangle has three *sides*; a tetrahedron has six *edges*. Same word in Chinese (边/棱) sometimes — different word in English. See [[Solids (Vocab)]].

---

## Parallel, Perpendicular, and Right Angles

| English | 中文 | Symbol | Meaning |
|---------|------|--------|---------|
| parallel | 平行 (píngxíng) | $\parallel$ | two lines that never meet (same direction) |
| perpendicular | 垂直 (chuízhí) | $\perp$ | two lines meeting at $90°$ |
| right angle | 直角 (zhíjiǎo) | small square at the corner | exactly $90°$ |
| acute angle | 锐角 (ruìjiǎo) | — | $< 90°$ |
| obtuse angle | 钝角 (dùnjiǎo) | — | between $90°$ and $180°$ |
| reflex angle | 优角 (yōujiǎo) | — | between $180°$ and $360°$ |

Full angle vocabulary, including supplementary, complementary, and the angles in parallel lines (corresponding, alternate, co-interior), lives in [[Angle Properties (Vocab)]] and [[Angles in Parallel Lines (Vocab)]].

---

## 3D: Faces, Edges, Vertices

The 3D analogues of the polygon vocabulary:

| English | 中文 | Where it lives |
|---------|------|---------------|
| face | 面 (miàn) | a flat polygonal surface of a solid |
| edge | 棱 (léng) | a line segment where two faces meet |
| vertex (pl. vertices) | 顶点 | a corner where three or more edges meet |
| cross-section | 截面 (jiémiàn) | the 2D shape you get by slicing a solid with a plane |

For a **cube**: $6$ faces, $12$ edges, $8$ vertices. For a **tetrahedron** ($4$-faced pyramid): $4$ faces, $6$ edges, $4$ vertices.

> [!info] Beyond syllabus — Euler's polyhedron formula
> For *any* convex polyhedron (a 3D solid with flat polygonal faces, no holes), Euler's formula says
> $$V - E + F = 2$$
> where $V$, $E$, $F$ are the counts of vertices, edges, and faces. Cube: $8 - 12 + 6 = 2$ ✓. Tetrahedron: $4 - 6 + 4 = 2$ ✓. Discovered by Euler in 1750, this is the entry point to topology — the deeper observation that $V - E + F$ is the **Euler characteristic** of the surface, and it's $2$ for every shape topologically equivalent to a sphere. Donuts give $0$, double-donuts $-2$, and so on. See [[Solids (Vocab)]] for the standard polyhedra.

---

## Common Mistakes

1. **Confusing "side" (2D) with "edge" (3D).** A polygon has *sides*; a polyhedron has *edges*. Don't write "the cube has six sides" — that confuses *sides* with *faces*.
2. **Calling a line segment a "line".** A line extends forever; a segment has two endpoints. Most exam phrasing is loose, but a precise answer to "find the length of line $AB$" is "$AB$ has no finite length — perhaps you mean segment $AB$?" (Don't actually write that on the exam — solve the segment.)
3. **Reflex vs obtuse confusion.** Obtuse is $90° < \theta < 180°$. Reflex is $180° < \theta < 360°$. The latter is the "outside" angle — a Pac-Man mouth has reflex angle at its vertex.
4. **"Parallel lines have equal gradients" — except vertical lines.** Two vertical lines are parallel but their gradient is *undefined*, not equal. The full statement: parallel lines either have equal gradients or are both vertical. See [[Equation of a Straight Line (Vocab)|Equation of a Straight Line]].

---

## Exam Notes

### OxAQA 9260

**Syllabus ref:** G1. The 9260 syllabus lists "points, lines, vertices, edges, planes, parallel, perpendicular, right angles, polygons" as required vocabulary. These terms are tested *implicitly* — they appear in question wording rather than as standalone questions. A student who has to pause to decode the vocab loses time.

### Cambridge 0580

**Syllabus ref:** E4.1. Same vocabulary as 9260 G1, examined the same way — embedded in geometry problems. Cambridge typically uses concise wording: "$ABCD$ is a quadrilateral with vertex $A$ at the origin and side $AB$ parallel to the $x$-axis."

---

## Connections

- **Leads to:** [[Triangles (Vocab)]], [[Quadrilaterals (Vocab)]], [[Polygon Angles (Vocab)]] — specific polygon families
- **Leads to:** [[Solids (Vocab)]] — 3D extension of the polygon family
- **Leads to:** [[Geometrical Constructions (Vocab)]] and [[Loci (Vocab)]] — every construction begins with points and lines
- **Leads to:** [[Angle Properties (Vocab)]] — full angle classification and parallel-lines theorems
- **Sibling:** [[Cartesian Coordinates (Vocab)]] — the algebraic side; coordinates label the points
- **Beyond high school:** *topology* — the study of properties (like Euler's $V - E + F = 2$) that survive any continuous deformation; a sphere and a cube are topologically the same

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\parallel$ | `\parallel` | parallel |
| $\perp$ | `\perp` | perpendicular |
| $\overline{AB}$ | `\overline{AB}` | segment $AB$ |
| $\overrightarrow{AB}$ | `\overrightarrow{AB}` | ray from $A$ through $B$ |
| $\overleftrightarrow{AB}$ | `\overleftrightarrow{AB}` | full line through $A$ and $B$ (rarely used) |
| $\angle ABC$ | `\angle ABC` | angle at vertex $B$ |
| $V - E + F$ | `V - E + F` | Euler characteristic |
