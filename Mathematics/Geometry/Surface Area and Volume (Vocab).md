---
chinese: 表面积与体积 (biǎomiànjī yǔ tǐjī)
prerequisites:
  - "[[Solids (Vocab)]]"
  - "[[Circles Arcs and Sectors (Vocab)]]"
  - "[[Pythagoras Theorem]]"
  - "[[Area and Perimeter (Vocab)]]"
  - "[[Nets (Vocab)]]"
  - "[[Units of Measure (Vocab)]]"
leads_to:
  - "[[Compound Shapes (Vocab)]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE-extension
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-G16
  - syllabus/0580-E5-4
  - type/vocabulary
  - type/reference-table
  - misconception/forgetting-third-in-cone-pyramid
  - misconception/units-cubed-vs-squared
---

# Surface Area and Volume 表面积与体积

## Definition

The **surface area** (表面积) of a solid is the total area of all its faces — what you'd need to wrap it in paper. The **volume** (体积) is the amount of space it encloses — what you'd need to fill it with water. This card is the **formula reference table** for all the standard solids in [[Solids (Vocab)]].

### 中文锚点

表面积 = 所有面的面积之和（用纸包住一个立体所需的纸）。体积 = 立体所占空间的大小（用水装满需要多少）。这张卡是常见立体（棱柱、圆柱、棱锥、圆锥、球、半球、截头锥）的表面积和体积公式表。**单位很重要**：长度 cm，面积 cm²，体积 cm³。

---

## Volume Formulas

| Solid | Volume | Notes |
|---|---|---|
| cube | $V = s^3$ | side length $s$ |
| cuboid | $V = l \cdot w \cdot h$ | length × width × height |
| **prism** (any) | $V = (\text{base area}) \times (\text{length})$ | length is the dimension perpendicular to the base |
| **cylinder** | $V = \pi r^2 h$ | "circular prism": base area $\pi r^2$ × height $h$ |
| **pyramid** (any) | $V = \tfrac{1}{3}(\text{base area}) \times (\text{height})$ | the famous $\tfrac{1}{3}$ |
| **cone** | $V = \tfrac{1}{3}\pi r^2 h$ | "circular pyramid": $\tfrac{1}{3}$ × base area × height |
| **sphere** | $V = \tfrac{4}{3}\pi r^3$ | $r$ = radius |
| **hemisphere** | $V = \tfrac{2}{3}\pi r^3$ | half of a sphere |
| **frustum of a cone** | $V = \tfrac{1}{3}\pi h(R^2 + Rr + r^2)$ | $R$ = bottom radius, $r$ = top radius, $h$ = height between (derivation below) |

> [!tip] Two patterns unify the table
> (1) **Prism family**: volume = base area × height. Cylinder is a "circular prism" — same formula, base is a circle so base area is $\pi r^2$. (2) **Pyramid family**: volume = $\tfrac{1}{3}$ × base area × height. Cone is a "circular pyramid" — same factor of $\tfrac{1}{3}$. The $\tfrac{1}{3}$ comes from calculus: integrate the shrinking cross-sections from base to apex; the average is $\tfrac{1}{3}$ of the base area. (Beyond syllabus — but the *fact* of the $\tfrac{1}{3}$ is examinable; the proof is not.)

### Where the frustum formula comes from

The frustum is what's left of a cone after a smaller cone is sliced off the top — so the frustum's volume is **(full cone) minus (top cone)**, and the algebra works out beautifully.

Set up the picture: bottom radius $R$, top radius $r$, frustum height $h$. Imagine extending the slanted side of the frustum upward to a point — that recovers the full original cone. Let $H$ be the *full* cone's height (apex to bottom). The top cone (the one we cut off) has height $H - h$ and radius $r$.

**Step 1 — find $H$ from similar triangles.** The full cone and the top cone are similar (same apex angle), so

$$
\frac{r}{R} = \frac{H - h}{H} \;\;\Longrightarrow\;\; H = \frac{Rh}{R - r}.
$$

**Step 2 — full cone volume.** $V_{\text{full}} = \tfrac{1}{3}\pi R^2 H = \tfrac{1}{3}\pi R^2 \cdot \dfrac{Rh}{R - r} = \tfrac{1}{3}\pi \cdot \dfrac{R^3 h}{R - r}$.

**Step 3 — top cone volume.** Its height is $H - h = \dfrac{Rh}{R - r} - h = \dfrac{rh}{R - r}$, and its radius is $r$, so $V_{\text{top}} = \tfrac{1}{3}\pi r^2 \cdot \dfrac{rh}{R - r} = \tfrac{1}{3}\pi \cdot \dfrac{r^3 h}{R - r}$.

**Step 4 — subtract.**

$$
V_{\text{frustum}} = V_{\text{full}} - V_{\text{top}} = \frac{\pi h}{3(R - r)}\,(R^3 - r^3).
$$

Now factor $R^3 - r^3 = (R - r)(R^2 + Rr + r^2)$ — the difference-of-cubes identity. The $(R - r)$ in the numerator cancels the $(R - r)$ in the denominator, leaving:

$$
\boxed{V_{\text{frustum}} = \tfrac{1}{3}\pi h\,(R^2 + Rr + r^2)}.
$$

The cancellation is the beautiful step. The middle term $Rr$ comes for free from the algebraic identity — it isn't an arbitrary average, it's *forced* by the difference-of-cubes factorisation. As a sanity check, set $r \to 0$ (top closes to a point — the frustum becomes a full cone): the formula gives $\tfrac{1}{3}\pi h R^2$, the cone volume. Set $r \to R$ (top equals base — the frustum becomes a cylinder of height $h$): the formula gives $\tfrac{1}{3}\pi h(3R^2) = \pi R^2 h$, the cylinder volume. Both limits check.

> [!info] Beyond syllabus — Archimedes' proof for the sphere
> The formula $V = \tfrac{4}{3}\pi r^3$ is **Archimedes' theorem** (c. 250 BC). His proof — discovered by him as the cleverest thing he ever did, and engraved on his tomb — used the fact that a sphere of radius $r$ inscribed in a cylinder of radius $r$ and height $2r$ has *exactly two-thirds* the volume of the cylinder: $\tfrac{2}{3}(\pi r^2)(2r) = \tfrac{4}{3}\pi r^3$. The cylinder–sphere–cone trio (sphere = cone × 2 for the right configuration) was Archimedes' proudest result. We now derive it in seconds via $V = \int_0^r 4\pi x^2\, dx$ — see [[Integration]] (volume of revolution).

---

## Surface Area Formulas

| Solid | Surface area | Notes |
|---|---|---|
| cube | $A = 6s^2$ | 6 square faces |
| cuboid | $A = 2(lw + lh + wh)$ | 3 pairs of opposite rectangles |
| **prism** (any) | $A = 2(\text{base area}) + (\text{perimeter}) \times (\text{length})$ | two ends + the unfolded "lateral" rectangle |
| **cylinder** | $A = 2\pi r^2 + 2\pi r h$ | two circles + lateral rectangle of width $2\pi r$ and height $h$ |
| **cone** (closed) | $A = \pi r^2 + \pi r \ell$ | base + curved surface ($\ell$ = slant height) |
| **cone** (open / lateral only) | $A = \pi r \ell$ | curved surface only (no base) |
| **sphere** | $A = 4\pi r^2$ | exactly $4$ great-circle areas |
| **hemisphere** (closed) | $A = 3\pi r^2$ | half-sphere $2\pi r^2$ + circular flat face $\pi r^2$ |
| **hemisphere** (curved only) | $A = 2\pi r^2$ | curved surface only |

The **slant height** $\ell$ of a cone (with vertical height $h$ and base radius $r$) comes from Pythagoras:

$$
\ell = \sqrt{r^2 + h^2}.
$$

(Inside the cone, the right triangle has legs $r$ and $h$ and hypotenuse $\ell$ — see [[Pythagoras Theorem]].)

> [!tip] Why the cylinder lateral surface is a rectangle of width $2\pi r$
> Imagine cutting the cylinder along one vertical edge and unrolling it flat. The result is a rectangle. Its **height** is the cylinder's height $h$. Its **width** is whatever was originally the circumference of the circular end — exactly $2\pi r$ (the circumference of a circle of radius $r$, see [[Circles Arcs and Sectors (Vocab)]]). So the lateral area is $2\pi r \cdot h$. The same unrolling trick shows why the cone's lateral surface (a sector of a circle of radius $\ell$) has area $\pi r \ell$ — it's a fun beyond-syllabus exercise to derive.

---

## Composite Solids

A **composite solid** (复合立体) is two or more standard shapes joined together — a cylinder topped with a hemisphere (test tube), a cone on a cylinder (rocket), a cube with a hemispherical hole. Strategy:

1. **Decompose** into named shapes.
2. **Compute volumes / surface areas** of each separately.
3. **For volume**: add (or subtract for cavities).
4. **For surface area**: add the *external* faces only — the hidden interface where two shapes meet does *not* count toward the total surface area.

**Worked example.** A solid is a cylinder of radius $5\,\text{cm}$ and height $10\,\text{cm}$ topped with a hemisphere of the same radius. Find the total surface area.

- Cylinder lateral: $2\pi r h = 2\pi(5)(10) = 100\pi$
- Cylinder bottom: $\pi r^2 = 25\pi$
- Hemisphere curved: $2\pi r^2 = 50\pi$
- ❌ The cylinder *top* and the hemisphere *flat face* are **internal** — they meet each other and don't count toward the external surface.

Total: $100\pi + 25\pi + 50\pi = 175\pi \approx 549.8\,\text{cm}^2$.

---

## Common Mistakes

1. **Forgetting the $\tfrac{1}{3}$ in cones and pyramids.** Volume = $\tfrac{1}{3}\pi r^2 h$ for a cone, *not* $\pi r^2 h$. The factor of $\tfrac{1}{3}$ is the most-failed thing in the whole topic.
2. **Wrong unit power.** Length in cm → area in **cm²** → volume in **cm³**. Marks are lost when a volume is given as $80\,\text{cm}^2$ instead of $\text{cm}^3$.
3. **Slant vs vertical height of a cone.** $\ell$ (slant) is along the curved surface from the apex to the rim. $h$ (vertical height) is from the apex perpendicular to the base. Use $h$ in the *volume* formula and $\ell$ in the lateral *surface area* formula. They are related by $\ell = \sqrt{r^2 + h^2}$.
4. **Counting hidden faces in composite solids.** When two shapes join, the interface is *internal* and not part of the surface area. Subtract it from each shape's count, not just one.
5. **$\tfrac{4}{3}\pi r^3$ for a hemisphere.** A hemisphere has volume $\tfrac{2}{3}\pi r^3$ — half of a sphere's $\tfrac{4}{3}\pi r^3$. Don't use the full-sphere formula for a half-sphere.
6. **Frustum confusion.** A frustum has *two* parallel circular faces of *different* radii. Volume formula needs both radii: $V = \tfrac{1}{3}\pi h(R^2 + Rr + r^2)$. Note this reduces to the cone formula when $r = 0$ (the top closes to a point).

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E5.4. The 0580 Extended formula sheet *typically gives* the sphere, cone, and pyramid formulas — the prism, cylinder, cuboid, and cube formulas are expected to be known cold. Always check the front of the exam for the formula list.

> [!tip] Formula-sheet status (placeholder — Queue M1)
> The cone $\tfrac{1}{3}\pi r^2 h$, sphere $\tfrac{4}{3}\pi r^3$, and pyramid $\tfrac{1}{3}\times\text{base}\times h$ formulas are *typically* on the 0580 formula sheet. The cylinder ($\pi r^2 h$), cuboid, and "prism = base × length" must be memorised.

### OxAQA 9260

**Syllabus ref:** G16 Ext. Same content as 0580 E5.4. 9260 students should expect frustum-of-a-cone problems; these are explicitly listed.

### A-Level / IB / AP

The volume-by-integration approach (volume of revolution) is A-Level / IB / AP content and lives in [[Integration]]. Surface-area-by-integration ($A = \int 2\pi y \sqrt{1 + (dy/dx)^2}\, dx$) is AP BC / IB AA HL.

---

## Connections

- **Prerequisite:** [[Solids (Vocab)]] — names of every shape on this card
- **Prerequisite:** [[Circles Arcs and Sectors (Vocab)]] — circumference $2\pi r$ and area $\pi r^2$ of the circular base in cylinder/cone/sphere
- **Prerequisite:** [[Pythagoras Theorem]] — slant height of a cone
- **Application:** [[Similarity]] — when scaling a solid by factor $k$: lengths scale by $k$, areas by $k^2$, volumes by $k^3$ (the *square-cube law*)
- **Application:** [[Integration]] — volume of revolution derives many of these formulas
- **Beyond high school:** *Cavalieri's principle* (1635) — two solids with the same cross-sectional area at every height have the same volume; this is what really proves the prism/pyramid formulas without calculus
- **Bridge to physics:** density $= \text{mass}/\text{volume}$; pressure $= \text{force}/\text{area}$ — both depend on getting the volume / surface area right

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\pi r^2 h$ | `\pi r^2 h` | cylinder volume |
| $\tfrac{1}{3}\pi r^2 h$ | `\tfrac{1}{3}\pi r^2 h` | cone volume |
| $\tfrac{4}{3}\pi r^3$ | `\tfrac{4}{3}\pi r^3` | sphere volume |
| $4\pi r^2$ | `4\pi r^2` | sphere surface area |
| $2\pi r h$ | `2\pi r h` | cylinder lateral surface |
| $\pi r \ell$ | `\pi r \ell` | cone lateral surface (slant height $\ell$) |
| $\sqrt{r^2 + h^2}$ | `\sqrt{r^2 + h^2}` | slant height of cone |
| $\text{cm}^3$ | `\text{cm}^3` | volume units |
