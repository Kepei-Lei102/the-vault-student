---
chinese: 复合图形 (fùhé túxíng)
prerequisites:
  - "[[Area and Perimeter (Vocab)]]"
  - "[[Surface Area and Volume (Vocab)]]"
  - "[[Circles Arcs and Sectors (Vocab)]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE-extension
  - curriculum/Cambridge-0580
  - syllabus/0580-E5-5
  - type/vocabulary
  - misconception/double-counting
---

# Compound Shapes 复合图形

## Definition

A **compound shape** (or *composite shape*) is a 2D or 3D figure built from simpler shapes — rectangles, triangles, semicircles, prisms, hemispheres — joined along edges or faces. To find its area or volume, *decompose* it into the simple pieces, compute each piece's contribution, then add (or subtract for "missing" parts).

The strategy:
- **Add** when pieces sit *next to* each other (an L-shape = big rectangle + small rectangle).
- **Subtract** when one piece is *removed* from another (a washer = big disk − small disk).

Both work; pick whichever splits the shape into simpler sub-pieces.

### 中文锚点

**复合图形 (fùhé túxíng)** = 由几个基本形状（矩形、三角形、半圆、棱柱、半球等）拼接而成的图形。

求面积/体积的方法：
1. **拆分** (chāi fēn) — 把复合图形分成基本图形
2. **加** (jiā) 各部分面积/体积，或 **减** (jiǎn) 掉被挖掉的部分
3. 检查重复计算 (chóngfù jìsuàn) 和遗漏 (yílòu)

---

## Two Strategies

### Strategy 1 — additive decomposition

Cut the compound shape with imaginary lines into pieces whose areas / volumes you know.

**L-shape** (10 × 8 minus 3 × 4 corner):

```
┌──────────┐
│          │
│          │   ← top half: 7 × 8 rectangle
│          │
├────┬─────┘   ← cut here
│    │
│    │         ← bottom half: 7 × 4 rectangle
└────┘
        wait, that doesn't match the L. Let me redo:

Original 10×8 with 3×4 corner removed (top-right):
┌──────┬───┐
│      │   ↑
│  big │ × │  ← × = removed corner (3 × 4)
│      │   │
│      ├───┘
│      │
│ rect │  ← rest of bottom (= 10 × 4 strip from y=0 to y=4)
│      │
└──────┘
```

Decomposition: top strip $7 \times 4$ (after the corner is removed from the upper part) plus bottom strip $10 \times 4$. Total area: $28 + 40 = 68$ cm². Same answer as $80 - 12$ subtraction.

### Strategy 2 — subtractive decomposition

Compute the area of the *enclosing* simple shape, then subtract the missing parts.

**Annulus / washer** (disk with a smaller disk removed): outer disk area − inner disk area.

For an annulus with outer radius $R = 5$ cm and inner radius $r = 3$ cm:
$$A = \pi R^2 - \pi r^2 = \pi(25 - 9) = 16\pi \approx 50.27 \text{ cm}^2.$$

> [!tip] Pick the strategy with fewer pieces
> Both strategies always give the same answer. The faster one is usually whichever requires *fewer* sub-pieces. For an L-shape: 1 piece minus 1 piece (subtractive, 2 operations) is often quicker than 2 pieces added (additive, 2 operations + a cut decision).

---

## 3D Compound Solids

The same logic in three dimensions.

### Pencil with cone tip (cylinder + cone)

A pencil-shaped solid: a cylinder of radius $r$, length $h_1$, plus a cone of the same radius $r$, height $h_2$ glued to one end.

**Volume:** $V = \pi r^2 h_1 + \tfrac{1}{3}\pi r^2 h_2 = \pi r^2 (h_1 + \tfrac{h_2}{3})$.

**Surface area:** sides of cylinder + curved surface of cone + circular base of cylinder (the other end is the cone tip).

$$S = 2\pi r h_1 + \pi r \ell + \pi r^2$$
where $\ell = \sqrt{r^2 + h_2^2}$ is the cone's slant height.

### Capsule (cylinder + 2 hemispheres)

A capsule: cylinder of radius $r$, length $h$, with two hemispheres of radius $r$ on the ends.

**Volume:** $V = \pi r^2 h + 2 \cdot \tfrac{2}{3}\pi r^3 = \pi r^2 h + \tfrac{4}{3}\pi r^3$.

(Two hemispheres of radius $r$ make one full sphere of radius $r$, with volume $\tfrac{4}{3}\pi r^3$.)

**Surface area:** curved cylinder + full sphere surface (since the two hemispheres' bases are *internal* — replaced by the cylinder ends).

$$S = 2\pi r h + 4\pi r^2.$$

> [!info] Internal faces don't count
> When two solids are glued together, their *touching* faces become *internal* and don't contribute to surface area. The capsule's hemispheres each have a flat circular face, but those faces are glued to the cylinder's ends and disappear into the interior. Only *external* surfaces count.

---

## Worked Examples

![[compound-shapes-four-examples.svg]]

Above: four canonical compound-shape problems. **(a)** L-shape via additive decomposition (split into two rectangles). **(b)** house silhouette as rectangle + triangle, with the internal edge (dashed green) marked as *not* part of the perimeter. **(c)** semicircle on a square — the diameter where they meet is internal. **(d)** drilled cylinder via subtractive decomposition: outer cylinder minus the hole.

### Example 1 — house shape

> A house silhouette consists of a $6 \times 4$ rectangle (the body) topped by a triangle with base $6$ and perpendicular height $3$ (the roof). Find the silhouette's area and perimeter.

**Area.** Rectangle + triangle = $6 \times 4 + \tfrac{1}{2}(6)(3) = 24 + 9 = 33$ unit².

**Perimeter.** Walk around the outside. The roof has two slant sides each of length $\sqrt{3^2 + 3^2} = \sqrt{18} = 3\sqrt 2$. The body sides: bottom $= 6$, two verticals $= 4$ each, top is replaced by the roof.

Perimeter = $6 + 4 + 4 + 3\sqrt 2 + 3\sqrt 2 = 14 + 6\sqrt 2 \approx 22.49$ unit.

### Example 2 — semicircle on a square

> A figure consists of a semicircle of diameter $10$ on top of a square with side $10$. Find total area and total perimeter.

**Area.** Square + semicircle = $10^2 + \tfrac{1}{2}\pi(5)^2 = 100 + 12.5\pi \approx 139.27$ unit².

**Perimeter.** $3$ sides of the square (the top is replaced by the semicircle's diameter, which is *internal*) + the curved arc.
$3(10) + \pi(5) = 30 + 5\pi \approx 45.71$ unit.

> [!warning] The straight edge under the semicircle is internal — don't count it
> Where two pieces meet, that shared edge isn't part of the perimeter of the compound shape. The square's top side disappears into the semicircle. Same logic as 3D: internal faces don't count.

### Example 3 — drilled cylinder

> A solid cylinder of radius $5$ cm and height $12$ cm has a coaxial hole of radius $2$ cm drilled through it. Find the remaining volume.

Outer cylinder volume: $\pi(5)^2(12) = 300\pi$ cm³.
Hole (smaller cylinder): $\pi(2)^2(12) = 48\pi$ cm³.

Remaining volume: $300\pi - 48\pi = 252\pi \approx 791.68$ cm³.

This is essentially "volume = outer − hole," the same logic as the 2D washer scaled to 3D.

---

## Common Mistakes

1. **Counting an internal edge in perimeter.** When two pieces are glued, the shared edge / face becomes internal and shouldn't be included in compound perimeter / surface area.
2. **Forgetting to subtract removed pieces.** "An L-shape with a corner cut out" needs the corner's area subtracted.
3. **Adding perimeters of sub-pieces.** Sub-piece perimeters are *not* the compound shape's perimeter; pieces share edges that disappear in the compound. Always walk around the outside.
4. **Wrong slant height for the roof / cone.** When a triangle sits on a rectangle, the *slant* sides aren't the same as the perpendicular height. Use Pythagoras to find slant if needed.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E5.5 — find the surface area and volume of compound 3D shapes; find perimeter and area of compound 2D shapes. Standard patterns:

- "Find the area of the L-shape." (Decompose; show working.)
- "A water trough has the cross-section of a semicircle of radius $r$ on top of a rectangle of width $2r$ and height $h$. Find its volume in terms of $r$, $h$, and the trough's length $L$." (Cross-section area = $\tfrac{1}{2}\pi r^2 + 2rh$; volume = cross-section × $L$.)
- "A solid is made of a hemisphere of radius $4$ cm sitting on top of a cylinder of radius $4$ cm and height $10$ cm. Find its total surface area." (Bottom of cylinder + curved cylinder + hemisphere curved surface; the cylinder's top and the hemisphere's base disappear into the interior.)

> [!tip] Always sketch the decomposition explicitly
> 0580 markschemes typically award method marks for "shows the shape split into rectangle + triangle" or "computes outer minus inner." Don't compute the answer in your head and write only the final number — show the decomposition with a diagram if helpful.

---

## Connections

- **Prerequisite:** [[Area and Perimeter (Vocab)]] — basic shape formulas
- **Prerequisite:** [[Surface Area and Volume (Vocab)]] — 3D solid formulas
- **Application:** *real-life mensuration* — computing paint required for a wall with a window, calculating concrete for a foundation with a hole, fabric for a tent
- **Application:** *engineering and architecture* — every structural calculation involves compound shapes; cross-sectional areas of beams, volumes of foundations, surface areas for thermal insulation
- **Beyond syllabus:** *calculus* generalises "compound" to arbitrary regions via integration; complicated boundaries become $\int dA$ instead of decomposition

---

## LaTeX Reference

| Concept | Notes |
|---|---|
| Additive: $A_{\text{total}} = A_1 + A_2 + \ldots$ | sum of pieces |
| Subtractive: $A_{\text{compound}} = A_{\text{outer}} - A_{\text{hole}}$ | enclosing minus removed |
| Internal edge | not counted in perimeter |
| Internal face | not counted in surface area |
