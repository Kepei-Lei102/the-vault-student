---
chinese: 面积与周长 (miànjī yǔ zhōucháng)
prerequisites:
  - "[[Geometrical Terms (Vocab)]]"
  - "[[Quadrilaterals (Vocab)]]"
  - "[[Triangles (Vocab)]]"
  - "[[Circles Arcs and Sectors (Vocab)]]"
  - "[[Units of Measure (Vocab)]]"
leads_to:
  - "[[Compound Shapes (Vocab)]]"
  - "[[Surface Area and Volume (Vocab)]]"
  - "[[Integration]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E5-2
  - syllabus/9260-G15
  - type/vocabulary
  - notation/perpendicular-height
  - misconception/slant-vs-perpendicular-height
---

# Area and Perimeter 面积与周长

## Definition

- **Perimeter** = the *total length around the boundary* of a 2D shape (the same units as length, e.g., cm).
- **Area** = the *amount of 2D space enclosed* by a shape (units of length-squared, e.g., cm²).

For special shapes, both have closed-form formulas:

| Shape | Perimeter | Area |
|---|---|---|
| **Rectangle** ($l \times w$) | $2l + 2w$ | $l \cdot w$ |
| **Square** (side $s$) | $4s$ | $s^2$ |
| **Triangle** (base $b$, height $h$, sides $a, b, c$) | $a + b + c$ | $\tfrac{1}{2} b h$ |
| **Parallelogram** (base $b$, perpendicular height $h$, slant $s$) | $2b + 2s$ | $b \cdot h$ |
| **Trapezium** (parallel sides $a, b$, perp height $h$) | sum of all 4 sides | $\tfrac{1}{2}(a + b) h$ |
| **Rhombus** (diagonals $d_1, d_2$) | $4 \times$ side | $\tfrac{1}{2} d_1 d_2$ |
| **Kite** (diagonals $d_1, d_2$) | $2 \times $ (long pair) + $2 \times$ (short pair) | $\tfrac{1}{2} d_1 d_2$ |
| **Circle** (radius $r$) | $C = 2\pi r$ | $A = \pi r^2$ |

**The "$h$" in every formula is the *perpendicular* height** — the distance measured at right angles to the base, *not* the slanted-side length. This is the most-tested 0580 trap.

### 中文锚点

| 形状 | 周长 (zhōucháng) | 面积 (miànjī) |
|---|---|---|
| 长方形 | $2l + 2w$ | $l \cdot w$ |
| 正方形 | $4s$ | $s^2$ |
| 三角形 | $a + b + c$ | $\tfrac{1}{2} b h$（**$h$ 是垂直高 (chuízhí gāo)**） |
| 平行四边形 | $2b + 2s$ | $b \cdot h$ |
| 梯形 (tīxíng) | 四边之和 | $\tfrac{1}{2}(a+b) h$ |
| 圆 | $C = 2\pi r$ | $A = \pi r^2$ |

考试关键：**$h$ 永远指垂直于底的高**，不是斜边的长。这是 0580 最经典的错误。

---

## The Perpendicular-Height Trap

Triangle area is $\tfrac{1}{2} b h$ where $h$ is the perpendicular distance from the *opposite vertex* to the base — *not* the length of one of the slanted sides.

**Right triangle:** the two legs ARE the base and height (one is perpendicular to the other). Easy.

**Obtuse triangle:** the perpendicular height might fall *outside* the triangle (on the extension of the base line). Still use it.

**Equilateral triangle with side $s$:** perpendicular height = $s\dfrac{\sqrt{3}}{2}$ (from $30$-$60$-$90$ triangle). Area = $\tfrac{1}{2} \cdot s \cdot \dfrac{s\sqrt 3}{2} = \dfrac{s^2 \sqrt 3}{4}$.

> [!warning] Slanted side ≠ height in area formulas
> A common 0580 mistake: a parallelogram with base $b$ and slant side $s$ — students compute area as $b \cdot s$. Wrong: area is $b \cdot h$ where $h$ is the *perpendicular* distance between the two parallel base sides. The slant length is irrelevant to area; it only matters for *perimeter*. Read the diagram carefully and use the perpendicular height even if it requires Pythagoras to find.

---

## Worked Examples

### Example 1 — triangle with given dimensions

> Find the area of a triangle with base $8$ cm and perpendicular height $6$ cm.

$A = \tfrac{1}{2}(8)(6) = 24$ cm². ✓

### Example 2 — perimeter of an L-shape

> An L-shape is made by removing a $3 \times 4$ rectangle from one corner of a $10 \times 8$ rectangle. Find the perimeter and area.

**Perimeter.** Walk around the outside. The L-shape has 6 sides total:
- Long sides: $10$, $8$, $7$ ($= 10-3$), $4$, $3$, $4$ ($= 8-4$).
- Sum: $10 + 8 + 7 + 4 + 3 + 4 = 36$ cm.

**Area.** Big rectangle minus removed corner: $10 \times 8 - 3 \times 4 = 80 - 12 = 68$ cm².

> [!tip] Composite-shape perimeter is *not* the sum of all sub-piece perimeters
> The L-shape's perimeter is *not* (perimeter of $10 \times 8$) - (perimeter of $3 \times 4$). The "removed" corner's edges that are *inside* the L don't contribute to perimeter; they don't exist. Just walk around the outside and add up the side lengths. Composite perimeter is geometry-by-walking; composite area is rectangles-by-decomposition (see [[Compound Shapes (Vocab)]]).

### Example 3 — circle area and circumference

> A circular pond has radius $3.5$ m. Find (a) its circumference, (b) its area.

(a) $C = 2\pi r = 2\pi(3.5) = 7\pi \approx 21.99$ m.
(b) $A = \pi r^2 = \pi(3.5)^2 = 12.25\pi \approx 38.48$ m².

When the answer must be *exact*, leave $\pi$ in: $C = 7\pi$ m, $A = 12.25\pi$ m². When asked for a *numerical* answer, use $\pi$ key on calculator and round to specified accuracy.

### Example 4 — trapezium

> A trapezium has parallel sides of length $5$ cm and $9$ cm, separated by perpendicular distance $4$ cm. Find its area.

$A = \tfrac{1}{2}(5 + 9)(4) = \tfrac{1}{2}(14)(4) = 28$ cm². ✓

---

## Common Mistakes

1. **Using slant length instead of perpendicular height.** Triangle, parallelogram, trapezium areas all need the *perpendicular* height. The slant side is for perimeter only.
2. **Forgetting $\tfrac{1}{2}$ for triangle area.** Triangle = $\tfrac{1}{2} b h$, not $bh$. Area of a parallelogram is $bh$ — the triangle is half a parallelogram.
3. **Confusing $C = 2\pi r$ with $A = \pi r^2$.** Circumference scales linearly with $r$; area scales as $r^2$. Doubling the radius doubles the circumference but *quadruples* the area.
4. **Using diameter instead of radius.** $C = 2\pi r = \pi d$. Both are correct, but $A = \pi r^2 = \pi (d/2)^2 = \tfrac{\pi d^2}{4}$ — *not* $\pi d^2$. Convert diameter to radius first if you're nervous.
5. **Unit mismatch.** Circle of radius $5$ m has area $25\pi$ *m²* — not just $25\pi$. Always carry units through.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E5.2 — find areas of triangles, parallelograms, trapezia, and circles; find perimeters of these shapes (including circumference of a circle). Standard patterns:

- "Find the area of a triangle with base $7$ cm and perpendicular height $5$ cm." ($17.5$ cm²)
- "Find the circumference of a circle with diameter $14$ cm." ($14\pi \approx 43.98$ cm)
- "A trapezium has parallel sides $a$ and $b$, perpendicular distance $h$ apart. Show that the area is $\tfrac{1}{2}(a+b)h$." (Geometric proof: cut and rearrange to a rectangle of width $\tfrac{a+b}{2}$ and height $h$.)
- "A circular sector has radius $8$ cm and arc length $10$ cm. Find the area of the sector." (Use [[Circles Arcs and Sectors (Vocab)]] formulas.)

---

## Connections

- **Prerequisite:** [[Geometrical Terms (Vocab)]] — base, height, perpendicular vocab
- **Prerequisite:** [[Triangles (Vocab)]], [[Quadrilaterals (Vocab)]] — the shape families
- **Prerequisite:** [[Circles Arcs and Sectors (Vocab)]] — circle formulas + sector partial-circle versions
- **Forward:** [[Compound Shapes (Vocab)]] — areas of L-shapes, T-shapes, donuts, etc., by decomposition
- **Forward:** [[Surface Area and Volume (Vocab)]] — surface area sums up the areas of the faces of a 3D solid
- **Forward:** [[Integration]] — calculus generalises "find the area under a curve" beyond the polygon family

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\tfrac{1}{2} b h$ | `\tfrac{1}{2} b h` | triangle area |
| $\pi r^2$ | `\pi r^2` | circle area |
| $2\pi r$ | `2\pi r` | circumference |
| $\tfrac{1}{2}(a+b)h$ | `\tfrac{1}{2}(a+b)h` | trapezium area |
