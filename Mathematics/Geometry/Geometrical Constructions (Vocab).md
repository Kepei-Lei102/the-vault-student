---
chinese: 几何作图 (jǐhé zuòtú)
prerequisites:
  - "[[Triangles (Vocab)]]"
  - "[[Angle Properties (Vocab)]]"
  - "[[Circle Vocabulary (Vocab)]]"
  - "[[Geometrical Terms (Vocab)]]"
leads_to:
  - "[[Loci (Vocab)]]"
  - "[[Heptadecagon]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-G13
  - syllabus/0580-E4-2
  - type/vocabulary
  - misconception/measure-vs-construct
---

# Geometrical Constructions 几何作图

## Definition

A **geometrical construction** (几何作图) is a drawing made using **only a straight edge (ruler) and a pair of compasses** — no protractor, no measuring of angles, no marked rulers used as measuring devices. The point is to produce an exact figure whose correctness is guaranteed by geometry, not by the precision of the ruler markings.

The phrase "**construct**" (作图) on an exam paper is a technical instruction. It means: *do not measure*. Show the construction arcs. Leave them in.

### 中文锚点

几何作图 = 仅用**直尺**和**圆规**画出几何图形。这里的"直尺"只是直边（不用刻度），"圆规"用来画圆和弧。这是从欧几里得开始的传统：图形的正确性由几何原理保证，而不是依赖于刻度的精度。考试中看到 "construct"（作图）就意味着：不要量，要画弧。

---

## Why "Ruler and Compass" Only

This restriction goes back to Euclid (c. 300 BC). A ruler can extend a line; a compass can draw a circle of any radius. From these two tools alone, the Greeks could produce equilateral triangles, regular polygons (3, 4, 5, 6, 8, 10, ...), perpendicular and angle bisectors — all *exactly*, without ever measuring anything.

The deep reason: every construction step corresponds to a **logical guarantee** from the geometry. Drawing two arcs of equal radius from two points and joining their intersections doesn't just *look like* a perpendicular bisector — it *is* one, because the four points form a rhombus and the diagonals of a rhombus bisect each other at right angles. The arcs are the proof.

> [!info] What about the protractor?
> A protractor measures angles to the nearest degree, but the answer is approximate — try drawing a $60°$ angle with a protractor versus constructing it with compasses, and the constructed angle is exact while the protractor angle has a small error. Exam markers will reject a "constructed" answer that was actually measured. **If construction arcs are missing, no marks.**

---

## The Tools

| English | 中文 | What it does |
|---------|------|--------------|
| straight edge / ruler | 直尺 (zhíchǐ) | Draws straight lines; the markings are *not* used for measurement during construction |
| pair of compasses | 圆规 (yuánguī) | Draws circles and arcs of a given radius |
| compass point | 圆规针脚 | The fixed end — placed at the centre of the arc |
| pencil end | 铅笔端 | The drawing end — must be sharp for accurate arcs |
| arc | 弧 (hú) | A portion of a circle; the visible mark of a compass sweep |

> [!tip] Construction marks are the working
> Examiners look for the arcs as evidence that the figure was *constructed*, not measured. Never erase your arcs after finishing — they are part of the answer.

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| construct | 作图 | Build using ruler and compasses only — no measuring |
| perpendicular bisector | 垂直平分线 (chuízhí píngfēnxiàn) | Line that cuts a segment in half at $90°$ |
| angle bisector | 角平分线 (jiǎo píngfēnxiàn) | Line that cuts an angle into two equal halves |
| perpendicular from a point | 由点向直线作垂线 | Drop a perpendicular from a point *not on* a line |
| perpendicular at a point | 在直线上作垂线 | Erect a perpendicular *at* a given point on a line |
| equidistant | 等距 (děngjù) | At equal distance from two or more reference objects |
| radius | 半径 | The compass setting — fixed throughout one arc-pair |

---

## The Standard Constructions (9260 G13)

All five share the same idea: **two arcs of equal radius cross at points equidistant from the reference set.** The line through those crossings is forced to be perpendicular or bisecting by symmetry.

### 1. Perpendicular bisector of a segment $AB$

Open the compass to a radius **bigger than half of $AB$**. Draw arcs from $A$ and from $B$. They cross at two points (one above, one below). Join them — that line is the perpendicular bisector.

![[construction-perpendicular-bisector.svg]]

*Why it works:* Both crossing points are equidistant from $A$ and $B$, so they lie on the locus *equidistant from $A$ and $B$*, which is exactly the perpendicular bisector. Equivalently: the four points $A$, top-crossing, $B$, bottom-crossing form a rhombus, and the diagonals of a rhombus bisect each other at right angles.

### 2. Angle bisector of $\angle ABC$

Place the compass at $B$, draw an arc cutting $BA$ at $P$ and $BC$ at $Q$. Then with the same (or any) radius, draw arcs from $P$ and $Q$ — they cross at $R$. Join $BR$.

![[construction-angle-bisector.svg|697]]

*Why it works:* $BPRQ$ is a kite (two pairs of equal adjacent sides: $BP = BQ$ from the first arc, $PR = QR$ from the second pair), and the diagonal $BR$ of a kite bisects the vertex angle.

### 3. Perpendicular from a point $P$ to a line $\ell$

With $P$ as centre, draw an arc cutting $\ell$ at $A$ and $B$. From $A$ and $B$ with the same radius, draw arcs that cross at $Q$ (on the opposite side from $P$). Join $PQ$.

![[construction-perpendicular-from-point.svg|697]]

*Why it works:* $PA = PB$ (radii of the first arc) and $QA = QB$ (radii of the second pair), so $PAQB$ is a rhombus. The diagonals of a rhombus meet at right angles, so $PQ \perp AB$ — and $AB$ lies on $\ell$.

### 4. Perpendicular at a point $P$ on a line $\ell$

With $P$ as centre, mark off equal distances $A$ and $B$ on $\ell$. From $A$ and $B$ with a larger radius, draw arcs that cross at $Q$. Join $PQ$.

![[construction-perpendicular-at-point.svg|697]]

*Why it works:* $Q$ lies on the perpendicular bisector of $AB$ (it is equidistant from $A$ and $B$), and the perpendicular bisector passes through the midpoint of $AB$. Since $PA = PB$ by construction, $P$ *is* the midpoint of $AB$ — so $PQ$ is the perpendicular bisector and lands on the line $\ell$ exactly at $P$.

### 5. Constructing $60°$ (equilateral triangle method)

Draw segment $AB$. With compass set to $AB$, draw an arc from $A$. With the same radius, draw an arc from $B$. They meet at $C$. Triangle $ABC$ is equilateral, so $\angle BAC = 60°$.

![[construction-60-degree-equilateral.svg|697]]

*Why it works:* All three sides are radii of equal-radius arcs ($AC$ from the arc centred at $A$, $BC$ from the arc centred at $B$, $AB$ the original segment), so $AB = AC = BC$ — the triangle is equilateral, and every angle in an equilateral triangle is $60°$ (see [[Triangles (Vocab)]]).

> [!tip] Combining $60°$ with bisection gives $30°$, $15°$, ...
> Construct $60°$, then bisect it for $30°$, bisect again for $15°$. You can also bisect $90°$ (from a perpendicular) for $45°$, and combine to get $75°$, $105°$, etc. Greek geometers called these **constructible angles**. (Famously, $20°$ — and therefore the regular nonagon — *cannot* be constructed.)

---

## Common Mistakes

1. **Measuring with a protractor instead of constructing.** No arcs = no marks. Even if the angle is correct.
2. **Erasing the construction arcs at the end.** They are the working — they prove you constructed rather than measured.
3. **Compass radius slipping during arc-pair.** For perpendicular bisectors and angle bisectors, the *two* arcs from each end must use the *same* radius. Hold the compass tightly.
4. **Radius too small for perpendicular bisector.** If the radius is less than half of $AB$, the arcs never cross. Open the compass wider than $\tfrac12 AB$.

---

## Exam Notes

### OxAQA 9260

**Syllabus ref:** G13. The 9260 syllabus explicitly requires the five compass constructions above: perpendicular bisector, perpendicular from a point, perpendicular at a point, angle bisector, and the $60°$ angle. Expect 2–4 mark questions: "Construct the perpendicular bisector of $AB$" or "Construct the angle bisector of $\angle PQR$." Always **leave arcs visible**.

### Cambridge 0580 Extended

**Syllabus ref:** E4.2. Cambridge 0580 is *less* demanding than 9260 here — it requires construction of triangles given specific dimensions and scale drawings, but does **not** require compass bisector constructions. If a 0580 paper says "construct the triangle with sides $5\,\text{cm}$, $6\,\text{cm}$, $7\,\text{cm}$," it means: draw one side with a ruler, then use compasses to swing arcs of $6\,\text{cm}$ and $7\,\text{cm}$ from the two endpoints — the intersection is the third vertex. That much *is* required. (The technique is the same one used in [[Congruence]] for SSS.)

---

## Connections

- **Prerequisite:** [[Triangles (Vocab)]] — equilateral construction depends on three equal radii forcing $60°$
- **Prerequisite:** [[Angle Properties (Vocab)]] — angle vocabulary
- **Prerequisite:** [[Circle Vocabulary (Vocab)|Circle Vocabulary]] — arc, radius
- **Application:** [[Loci (Vocab)]] — every standard locus is built from these constructions
- **Parallel:** [[Congruence]] — the SSS triangle construction with two arcs is exactly the SSS congruence diagram (same arcs, different question)
- **Beyond syllabus:** [[Heptadecagon]] — Gauss's regular 17-gon, the most famous non-trivial construction; uses the angle bisector from this card recursively four times in Richmond's procedure
- **Parent:** Classical Euclidean geometry — the "ruler and compass" tradition since Euclid's *Elements* Book I

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\angle ABC$ | `\angle ABC` | Named angle at vertex $B$ |
| $\overline{AB}$ | `\overline{AB}` | Segment $AB$ (alternative: $AB$) |
| $\perp$ | `\perp` | Perpendicular |
| $60°$ | `60°` or `60^\circ` | Degree symbol — exam-standard |
