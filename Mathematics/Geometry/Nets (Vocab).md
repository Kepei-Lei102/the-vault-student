---
chinese: 展开图 (zhǎnkāitú)
prerequisites:
  - "[[Solids (Vocab)]]"
  - "[[Geometrical Terms (Vocab)]]"
leads_to:
  - "[[Surface Area and Volume (Vocab)]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E4-2
  - type/vocabulary
  - misconception/wrong-net-folding
---

# Nets 展开图

## Definition

A **net** is the *2D layout* of a 3D solid — what you'd see if you "unfolded" the solid flat onto a piece of paper. Cut along certain edges, fold the pieces flat, and you get the net. Reverse: cut out the net, fold along the dashed edge-lines, glue together, and you reconstruct the solid.

![[nets-cube-cylinder-cone.svg]]

Above: three canonical nets. **(a)** A cube net in the "cross" / "1-4-1" layout — one of *eleven* distinct nets for the cube. Fold along the dashed amber edges; the four central squares form a band around the cube while top and bottom caps fold to close it. **(b)** Cylinder net: 2 circles (top and bottom) plus a rectangle whose width $= 2\pi r$ (base circumference) and height $= h$ — and that rectangle area, $2\pi r h$, *is* the curved surface area. **(c)** Cone net: 1 circle (base) plus a *sector* of radius $\ell$ (slant height) whose arc length matches the base circumference $2\pi r$. The sector's angle is $\dfrac{r}{\ell} \times 360°$ and its area $\pi r \ell$ is the cone's curved surface area.

Cubes actually have **11 distinct nets** (excluding rotations and reflections). It's a beautiful exercise to enumerate them all — but exam-relevant only at "recognise" level.

### 中文锚点

**展开图 (zhǎnkāitú)** = 把一个 3D 立体沿着某些棱剪开，平铺到平面上得到的二维图形。也叫**平面展开图**。

正方体的展开图共有 **11 种**（不计旋转和翻折）。考试常考"哪些是合法的展开图"和"哪个面在哪个位置"。

---

## Standard Nets — quick reference

| Solid | Description |
|---|---|
| **Cube** | 6 squares; 11 distinct nets total |
| **Cuboid** | 6 rectangles (3 pairs of identical opposite faces) |
| **Triangular prism** | 2 triangles + 3 rectangles |
| **Square pyramid** | 1 square base + 4 isoceles triangles |
| **Tetrahedron** | 4 equilateral triangles (or general triangles for a non-regular tetrahedron) |
| **Cylinder (open)** | 2 circles + 1 rectangle (the rectangle's length = circumference $2\pi r$) |
| **Cone (open)** | 1 circle (base) + 1 sector (curved surface — radius = slant height $\ell$, arc length = $2\pi r$) |

> [!info] Cylinder net — the rectangle dimensions
> When you "unroll" a cylinder of radius $r$ and height $h$, the curved surface becomes a rectangle. Its **height** is $h$. Its **width** is $2\pi r$ (the circle's circumference). This is why the curved surface area is $2\pi r h$ — it's literally the area of that rectangle. Same logic powers Surface Area and Volume formulas (see [[Surface Area and Volume (Vocab)]]).

> [!info] Cone net — the sector's angle
> A cone of slant height $\ell$ and base radius $r$ unrolls into a *sector* of a circle. The sector's radius is $\ell$. Its arc length matches the base circumference $2\pi r$. The sector's *angle* is $\dfrac{2\pi r}{\ell}$ radians, or $\dfrac{r}{\ell} \times 360°$ in degrees. This means the curved surface area is $\pi r \ell$ — a beautiful derivation that comes "for free" once you see the net.

---

## Reading and Drawing Nets

### Cambridge 0580 typical question

> Which of the following is a valid net of a cube?

Five candidate diagrams; you tick the ones that fold into a cube and cross out the rest. The mental check: visualise folding step-by-step. Two informal rules that help:

1. **No two squares can be on top of each other** when folded. (A "T-shape with all 6 squares stacked vertically" wouldn't work — three faces would land on the same position.)
2. **Each face must have a unique destination.** Trace where each square ends up on the cube; if two squares land on the same face, the net is invalid.

The 11 valid cube nets fall into rough categories:
- 6 nets in the "$1{-}4{-}1$" family (one cap, a row of 4, another cap)
- 3 nets in the "$1{-}3{-}2$" family (a tall T-shape)
- 1 net in the "$2{-}2{-}2$" family (zigzag staircase)
- 1 net in the "$3{-}3$" family (two rows of three, offset)

### Identifying opposite faces

When a net of a cube is given with letters labeled on the faces, you can tell *which two letters end up on opposite faces of the cube* by:

- Counting "two squares apart in a row" — those squares fold to opposite faces.
- An "L-shape" pair of squares folds to *adjacent* faces (sharing an edge), not opposite.

---

## Worked Examples

### Example 1 — surface area via the net

> A cuboid measures $3 \text{ cm} \times 4 \text{ cm} \times 5 \text{ cm}$. Find its surface area by drawing the net.

The net consists of $6$ rectangles, in three pairs:
- Two of $3 \times 4 = 12$ cm² (top and bottom)
- Two of $3 \times 5 = 15$ cm² (front and back)
- Two of $4 \times 5 = 20$ cm² (left and right)

Total surface area: $2(12) + 2(15) + 2(20) = 24 + 30 + 40 = 94$ cm². ✓

This is exactly what the formula $2(lw + lh + wh)$ computes, but the net makes it physically obvious: surface area = sum of the rectangle areas in the net.

### Example 2 — recognising a faulty net

> Is the following a valid net of a square-based pyramid? [Diagram: 1 square + 4 isoceles triangles, but two triangles are on the *same* side of the square.]

No. A square pyramid's net has each triangle on a *different* side of the central square — one per edge of the base. Two on the same edge would overlap when folded. The net is invalid.

### Example 3 — cylinder net dimensions

> A cylinder has radius $4$ cm and height $10$ cm. Find the dimensions of the rectangle in its net.

The rectangle's height is the cylinder's height: $10$ cm.
The rectangle's width is the base circumference: $2\pi r = 2\pi(4) = 8\pi \approx 25.13$ cm.

So the rectangle is $10 \text{ cm} \times 8\pi \text{ cm}$, area $80\pi \approx 251.3$ cm² — and that's the curved surface area of the cylinder.

---

## Common Mistakes

1. **Drawing the cube net as $2 \times 3$ when there's a hole.** A $2 \times 3$ grid of squares is not a valid cube net; folding leaves either a hole or overlapping faces. The valid arrangements all have specific shapes.
2. **Forgetting the bases on cylinder/cone nets.** A cylinder net needs *2* circles plus the rectangle. A cone needs *1* circle plus the sector. Drawing only the curved-surface part loses marks.
3. **Wrong rectangle width on the cylinder.** The rectangle's *width* is $2\pi r$, not $\pi r$ or $\pi d$ (well, $\pi d = 2\pi r$, so $\pi d$ also works — but $\pi r$ alone is wrong).
4. **Treating the cone's sector as a full circle.** The cone's curved surface is a *sector*, not the whole disk. The sector's arc length equals $2\pi r$ (base circumference), which is *less than* $2\pi \ell$ (full circumference of a circle of radius $\ell$).

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E4.2 — recognise nets of solids; sketch nets of simple solids. Standard patterns:

- "Sketch the net of a triangular prism with the given dimensions."
- "Which of these are valid nets of a cube? Tick all that apply."
- "On the net below, mark which face is opposite to the shaded face when folded into a cube."
- "A cylinder has radius $5$ cm and height $12$ cm. Calculate the area of the rectangle in its net." (Answer: $5 \times 2\pi \times 12 = 120\pi$ cm² — wait, that's not right — let me recompute: width = $2\pi(5) = 10\pi$, height = $12$, area = $120\pi$ cm².)

---

## Connections

- **Prerequisite:** [[Solids (Vocab)]] — recognise the 3D shape before drawing its net
- **Forward:** [[Surface Area and Volume (Vocab)]] — surface area = sum of net rectangle / triangle / sector areas
- **Application:** *packaging design* — every cardboard box you've ever opened is a net unfolded; minimum-material packaging is an optimisation problem on net layouts
- **Application:** *cartography* — map projections are 2D nets of the (curved) Earth; impossible to perfectly unfold a sphere, hence the various trade-offs (Mercator, equal-area, etc.)
- **Beyond syllabus:** *11 cube nets* enumeration, *4 tetrahedron nets*, *Cauchy's rigidity theorem* (every convex polyhedron is determined by its net structure)

---

## LaTeX Reference

| Term | Notes |
|---|---|
| $2\pi r$ | cylinder net rectangle width (= base circumference) |
| $2\pi r$ as arc length | cone net sector arc length |
| $\dfrac{r}{\ell} \times 360°$ | cone net sector angle |
| $\pi r \ell$ | curved surface area of cone (= sector area) |
