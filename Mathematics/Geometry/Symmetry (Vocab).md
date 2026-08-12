---
chinese: 对称 (duìchèn)
prerequisites:
  - "[[Geometrical Terms (Vocab)]]"
  - "[[Quadrilaterals (Vocab)]]"
leads_to:
  - "[[Transformations (Vocab)]]"
  - "[[Group Theory]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E4-5
  - syllabus/9260-G6
  - type/vocabulary
  - misconception/order-counting
---

# Symmetry 对称

## Definition

A shape has **symmetry** if a *rigid motion* (reflection or rotation) maps the shape exactly onto itself. Two flavours:

- **Line symmetry** (reflective / mirror symmetry): a *line* across which the shape reflects to itself. The line is called a **line of symmetry** (or *axis of symmetry*).
- **Rotational symmetry**: a *rotation* about a centre that maps the shape onto itself. The number of distinct rotations (in $[0°, 360°)$) that work is called the **order of rotational symmetry**.

Every shape has rotational order at least $1$ (the trivial $360°$ rotation). A shape with order exactly $1$ is said to have *no* rotational symmetry — the rotation that fixes it is the do-nothing one.

### 中文锚点

**对称 (duìchèn)** = symmetry. 两种：

| 类型 | 中文 | 描述 |
|---|---|---|
| 轴对称 | line / mirror symmetry | 沿一条**对称轴 (duìchèn zhóu)** 翻折后重合 |
| 旋转对称 | rotational symmetry | 绕一个中心**旋转 (xuánzhuǎn)** 后重合 |

**对称阶数 (duìchèn jiéshù) / 旋转对称阶数** = order of rotational symmetry — 在 $[0°, 360°)$ 内能让图形重合的旋转次数。

注意：阶 $= 1$ 表示**没有**旋转对称（只有 $360°$ 即"啥都不做"那一次）。

---

## Order of Rotational Symmetry — counting properly

The order is the number of *positions* (including the starting one) in which the shape looks the same as you rotate it through one full turn:

| Shape | Order | Why |
|---|---|---|
| Equilateral triangle | $3$ | $0°, 120°, 240°$ all map it to itself |
| Square | $4$ | $0°, 90°, 180°, 270°$ |
| Regular pentagon | $5$ | $0°, 72°, 144°, 216°, 288°$ |
| Regular $n$-gon | $n$ | rotations by $360°/n$ |
| Circle | $\infty$ | any angle works |
| Rectangle (non-square) | $2$ | $0°$ and $180°$; $90°$ doesn't map it to itself |
| Parallelogram (non-rectangle) | $2$ | $180°$ rotation works; reflection does not |
| Letter "S" | $2$ | $180°$ works, *no* mirror lines |
| Letter "T" | $1$ | only $0°$; one mirror line vertical |
| Scalene triangle | $1$ | no rotational symmetry, no mirror lines |

> [!warning] Order counts the starting position too
> The order of rotational symmetry is "how many positions in a full $360°$ turn give the same look" — and the starting position counts. An equilateral triangle has order $3$, *not* $2$ (which would only count $120°$ and $240°$). The "do nothing" rotation is always one of the matches.
>
> If a shape has *no* useful rotational symmetry, its order is $1$ (only the do-nothing rotation works) — *not* $0$.

---

## Lines of Symmetry — examples by polygon

| Shape | Lines of symmetry |
|---|---|
| Equilateral triangle | $3$ (one per vertex through the opposite midpoint) |
| Isoceles triangle (non-equilateral) | $1$ (perpendicular bisector of the base) |
| Scalene triangle | $0$ |
| Square | $4$ (two diagonals + two perpendicular bisectors of sides) |
| Rectangle (non-square) | $2$ (perpendicular bisectors of sides only — diagonals don't count) |
| Rhombus (non-square) | $2$ (the two diagonals only) |
| Parallelogram (non-rhombus, non-rectangle) | $0$ |
| Regular $n$-gon | $n$ |
| Circle | $\infty$ (any diameter is a line of symmetry) |

> [!info] Lines of symmetry vs rotational order — they don't always agree
> The "S" letter has rotational order $2$ but *zero* lines of symmetry. A regular pentagon has both 5 lines and rotational order 5. Rectangle: 2 lines, order 2 — matching. Parallelogram: 0 lines, order 2 — mismatch. The two kinds of symmetry are *independent* in general; counting them separately is a 0580 mark-bait.

---

## 3D Symmetry — planes of symmetry

In 3D, the analogue of a *line* of symmetry is a **plane of symmetry**: a flat plane across which the solid reflects onto itself. A cuboid (non-cube) has 3 planes of symmetry; a sphere has infinitely many (every plane through the centre).

| Solid | Planes of symmetry | Rotational order (about main axis) |
|---|---|---|
| Cube | $9$ (3 + 6) | $4$ (about each face-axis) |
| Cuboid (non-cube) | $3$ (one perpendicular to each pair of opposite faces) | $2$ |
| Right cylinder (closed) | $\infty$ + $1$ ($\infty$ through the axis, $1$ perpendicular bisector of axis) | $\infty$ |
| Right cone | $\infty$ (every plane containing the axis) | $\infty$ (about its axis) |
| Sphere | $\infty$ (every plane through the centre) | $\infty$ (every axis through centre) |
| Tetrahedron (regular) | $6$ | $3$ |

> [!info] The cube has 9 planes — count them
> Cube planes of symmetry: 3 through pairs of opposite face-centres + 6 through pairs of opposite edges = 9 total. Counting them is a beautiful exercise (and the key to noticing that the cube's symmetry group has $48$ elements, but that's beyond 0580).

---

## Worked Examples

### Example 1 — find lines of symmetry and order

> A regular hexagon has how many lines of symmetry, and what is its order of rotational symmetry?

Regular $n$-gon: $n$ lines, order $n$. Hexagon: **$6$ lines of symmetry, order $6$**.

### Example 2 — letter symmetry

> Which capital letters of the alphabet have (a) at least one line of symmetry, (b) rotational symmetry of order $> 1$, (c) both?

(a) Lines of symmetry (vertical or horizontal):
A, B, C, D, E, H, I, M, O, T, U, V, W, X, Y (15 letters).
(b) Rotational symmetry order > 1:
H, I, N, O, S, X, Z (7 letters; the order is $2$ for each).
(c) Both: H, I, O, X (4 letters).

### Example 3 — 3D solid

> How many planes of symmetry does a regular hexagonal prism have?

A regular hexagon has 6 lines of symmetry → 6 planes of symmetry pass *through* the axis of the prism. Plus 1 plane perpendicular to the axis (cutting the prism in half horizontally). **Total: 7 planes.**

---

## Common Mistakes

1. **Counting the do-nothing rotation as separate from order = 1.** A scalene triangle has rotational order $1$ — meaning only the trivial rotation. Saying "order = 0" or "no rotational symmetry, so it's not in any order" is wrong.
2. **Confusing diagonal lines on rectangles with lines of symmetry.** A non-square rectangle's diagonals are *not* lines of symmetry — reflecting over a diagonal swaps the long and short sides, distorting the shape. Only the perpendicular bisectors of pairs of sides are lines of symmetry.
3. **Thinking "rotational symmetry = mirror symmetry."** Independent. The letter "S" has order 2 but zero mirror lines; the letter "T" has zero rotational symmetry but one mirror line.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E4.5 — recognise rotational and line symmetry (including order of rotational symmetry) in two and three dimensions; recognise symmetry properties of the prism, cylinder, cone, pyramid. Standard patterns:

- "State the number of lines of symmetry of an equilateral triangle." (3)
- "Write down the order of rotational symmetry of a parallelogram." (2)
- "Draw all the lines of symmetry on the diagram." (Mark them as solid lines on the figure.)
- "How many planes of symmetry does a cuboid (with all sides different) have?" (3)

---

## Connections

- **Prerequisite:** [[Geometrical Terms (Vocab)]] — polygon family vocabulary
- **Sibling:** [[Quadrilaterals (Vocab)]] — symmetry properties distinguish the quadrilateral family (parallelogram, rhombus, rectangle, square, kite, trapezium)
- **Forward:** [[Transformations (Vocab)]] — reflection and rotation as the *transformations* that detect symmetry
- **Extension:** [[Group Theory]] — the symmetries of a shape, collected, *are* a group ($D_n$ for the regular $n$-gon; $C_n$ for its rotations alone); the abstract theory where "count the symmetries" becomes an algebra
- **Beyond syllabus:** *symmetry groups* — the cube's $48$-element symmetry group; molecular symmetry in chemistry; Noether's theorem (every continuous symmetry corresponds to a conservation law in physics)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $D_n$ | `D_n` | dihedral group of order $2n$ — symmetry group of a regular $n$-gon (beyond syllabus) |
