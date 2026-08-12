---
chinese: 轨迹 (guǐjì)
prerequisites:
  - "[[Geometrical Constructions (Vocab)]]"
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Circle Vocabulary (Vocab)]]"
leads_to:
  - "[[Coordinate Geometry of the Circle]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - syllabus/9260-G13
  - type/vocabulary
  - misconception/locus-as-set-not-path
---

# Loci 轨迹

## Definition

A **locus** (plural: **loci**, 轨迹) is the **set of all points that satisfy a given geometric rule**. Not "the path one point takes" — it's the *collection* of every position where the rule holds. A locus can be a line, a curve, a region, or even a single point.

The Latin word *locus* means "place." The plural is *loci* (pronounced "low-sigh," not "low-key"). In Chinese, 轨迹 captures the idea of a "track" left by a moving point — but mathematically the locus is the **whole set of valid positions**, not the motion itself.

### 中文锚点

轨迹 = 满足某个几何条件的所有点的集合。注意：是**集合**，不是路径。比如"到点 $A$ 距离为 $3$ 的所有点"是一个圆——这个圆就是这个条件的轨迹。轨迹可以是线、曲线、区域，甚至单点。

---

## Why Loci Matter

Loci are the **geometric language for "everywhere that satisfies a rule."** A circle isn't fundamentally "a round shape" — it's *the locus of points equidistant from a centre*. This shift from "shape" to "rule" is what unlocks coordinate geometry: once a locus is described by a rule like "distance from $(0,0)$ equals $5$," you can write the equation $x^2 + y^2 = 25$ — and the geometric problem becomes algebraic.

This is exactly the bridge to [[Coordinate Geometry of the Circle]] (0606 §8) and to all of analytic geometry. Loci are also why GPS works: a satellite measures your distance from itself, and you must lie on the *locus* of points at that distance — a sphere. Three satellites give three spheres; the intersection (a single point, by trilateration) is your location.

> [!info] Locus thinking is everywhere
> In physics, the **wavefront** is the locus of points reached by a wave at the same time. In epidemiology, an **isobar** is the locus of equal-pressure points on a weather map. The framework — "all points satisfying a condition" — is one of the most reusable ideas in mathematics.

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| locus (sing.) / loci (pl.) | 轨迹 | "Set of points satisfying a rule" |
| equidistant | 等距 (děngjù) | At equal distance from two or more reference objects |
| region | 区域 (qūyù) | A 2D area, often shaded; bounded by loci |
| boundary | 边界 (biānjiè) | The locus that separates the inside of a region from the outside |
| within / less than | 在内 / 小于 | Strictly less than the given distance — open boundary, dashed line |
| at most / no more than | 至多 / 不超过 | Less than *or equal to* — closed boundary, solid line |
| perpendicular distance | 垂直距离 | Shortest distance from a point to a line — the perpendicular |

> [!tip] "Shortest distance to a line = perpendicular distance"
> This single fact is the engine behind every line-locus problem. The locus "all points at distance $d$ from line $\ell$" means perpendicular distance — so you measure perpendicular to $\ell$, not along it. Two parallel lines, each $d$ away from $\ell$, are the answer.

---

## The Four Standard Loci

These four come up in nearly every 9260 G13 question. Memorize the rule, the picture, and the construction.

### 1. Locus of points at fixed distance from a single point

**Rule:** "All points exactly $d$ away from point $A$."

**Locus:** A **circle** of radius $d$ centred at $A$.

**Construction:** Compass at $A$, radius $d$, draw the circle.

![[locus-circle.svg|697]]

The animation makes the "set of points" framing visible: each amber dot is *one* point that satisfies the rule (distance from $A$ equals $d$), and the green circle is the **integral** of all such points. The circle isn't a path traced by motion — it's the collection of every valid position, drawn all at once.

### 2. Locus of points at fixed distance from a line

**Rule:** "All points exactly $d$ away from line $\ell$."

**Locus:** **Two parallel lines**, each at perpendicular distance $d$ from $\ell$ (one on each side).

**Construction:** Erect perpendiculars to $\ell$ at any two points; mark off distance $d$ on each side; join.

![[locus-parallel-lines.svg|697]]

Each amber dot is a point at perpendicular distance $d$ from $\ell$ (the dashed grey segments on the first two dots make the perpendicular measurement explicit). The locus is **two** parallel lines, not one — every point on either side of $\ell$ at distance $d$ qualifies.

> [!tip] Distance from a *segment* (not a full line) is different
> If the question says "distance $d$ from segment $AB$" rather than "from line $AB$," the locus has two straight parts (parallel to $AB$, distance $d$ above and below) joined by **two semicircular caps** of radius $d$ centred at $A$ and $B$. The result looks like a stadium / racetrack shape.

### 3. Locus of points equidistant from two points

**Rule:** "All points the same distance from $A$ as from $B$."

**Locus:** The **perpendicular bisector** of segment $AB$.

**Construction:** From [[Geometrical Constructions (Vocab)]] §1 — arc-pair from $A$ and $B$, join the crossings.

![[locus-perpendicular-bisector.svg|697]]

The dashed grey segments on the first three dots show **both** distances $|PA|$ and $|PB|$ — they're equal by hypothesis. Every dot on the green vertical line satisfies $|PA|=|PB|$. The right-angle marker at the midpoint of $AB$ is the geometric signature of the perpendicular bisector.

*Why it works:* For any point $P$ on the perpendicular bisector, triangle $APM$ ≅ triangle $BPM$ (SAS, where $M$ is the midpoint), so $PA = PB$.

### 4. Locus of points equidistant from two lines

**Rule:** "All points the same perpendicular distance from line $\ell_1$ as from line $\ell_2$."

**Locus:** The **angle bisector** of the angle formed by $\ell_1$ and $\ell_2$. (If the lines cross, there are *two* bisectors at right angles to each other — both are part of the locus.)

**Construction:** From [[Geometrical Constructions (Vocab)]] §2 — arc from the vertex, then arc-pair from the two cut points, join to vertex.

![[locus-angle-bisector.svg|697]]

The dashed grey segments on the first three dots are the perpendicular drops from each test point $P$ to $\ell_1$ and to $\ell_2$ — equal in length, by hypothesis. Every dot on the green bisector line satisfies $d(P, \ell_1) = d(P, \ell_2)$.

---

## Combining Loci — Regions

Most exam questions give **two or more conditions** and ask for the region where *all* conditions hold simultaneously.

**Strategy:**

1. Draw each locus separately on the same diagram.
2. Identify the side of each locus where its condition is satisfied (e.g., "within $5\,\text{cm}$ of $A$" = inside the circle around $A$).
3. **Shade only the region where every condition holds** — the intersection.
4. Use a **solid line** for "$\leq$" boundaries (included), a **dashed line** for "$<$" boundaries (excluded). This convention matches [[Graphical Inequalities (Vocab)|Graphical Inequalities]].

**Example phrasing:** "Shade the region inside the rectangle that is closer to $A$ than to $B$ *and* within $4\,\text{cm}$ of side $PQ$."

This means: shade the intersection of (a) the rectangle, (b) the side of the perpendicular bisector of $AB$ containing $A$, and (c) the strip of width $4\,\text{cm}$ along $PQ$.

---

## Common Mistakes

1. **"Distance from a line" measured along the line, not perpendicular to it.** Always perpendicular. The shortest distance from a point to a line is the perpendicular distance.
2. **Confusing "equidistant from two points" with "equidistant from two lines."** Two points → perpendicular bisector. Two lines → angle bisector. Different constructions.
3. **Treating a locus as a path rather than a set.** A locus is *every* point satisfying the rule, not the trajectory of a moving point. A point can be on the locus without ever having "been" there.
4. **Forgetting the dashed-vs-solid boundary convention.** "Less than" → dashed; "at most" → solid. Same as graphing inequalities.
5. **Shading the wrong side.** Pick a test point inside one candidate region, check whether it satisfies the rule, then shade accordingly.

---

## Exam Notes

### OxAQA 9260

**Syllabus ref:** G13. Loci appear as 4–6 mark questions, almost always combined with [[Geometrical Constructions (Vocab)]]. The standard exam pattern: a diagram is given (a rectangular field, a triangle, a map of a town), and the candidate must construct two or three loci, then shade the region satisfying all conditions. Marks are awarded for: visible construction arcs, correct loci drawn accurately, correct boundary type (dashed/solid), and the right region shaded.

> [!tip] 9260 specifically tests "perpendicular distance = shortest distance"
> The G13 syllabus explicitly mentions this. Expect at least one phrase like "the locus of points whose shortest distance from line $AB$ is $3\,\text{cm}$" — translate immediately to "perpendicular distance $= 3\,\text{cm}$" and draw the two parallel lines.

### Cambridge 0580

Loci are **not explicitly required** in 0580 (Core or Extended). The syllabus comparison file confirms this is a 9260-only topic. If teaching a 0580-only student, this card is enrichment — but worth covering because the four standard loci appear naturally in any geometry problem involving "the set of points where..."

---

## Connections

- **Prerequisite:** [[Geometrical Constructions (Vocab)]] — every standard locus is built from a construction
- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — locus thinking generalises to "set of $(x,y)$ satisfying an equation"
- **Prerequisite:** [[Circle Vocabulary (Vocab)|Circle Vocabulary]] — circle = locus of points equidistant from a centre
- **Leads to:** [[Coordinate Geometry of the Circle]] — circle as $(x-a)^2 + (y-b)^2 = r^2$ is the algebraic statement of the locus rule
- **Parallel:** [[Vector Geometry]] — line and plane equations are loci in vector form
- **Parallel:** [[Graphical Inequalities (Vocab)|Graphical Inequalities]] — shading a region bounded by inequalities uses the same dashed-vs-solid convention

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\leq$ | `\leq` | "At most" — solid boundary |
| $<$ | `<` | "Less than" — dashed boundary |
| $\perp$ | `\perp` | Perpendicular distance |
| $\overline{AB}$ | `\overline{AB}` | Segment $AB$ |
| $d(P, \ell)$ | `d(P, \ell)` | Distance from point $P$ to line $\ell$ — beyond-syllabus notation |
