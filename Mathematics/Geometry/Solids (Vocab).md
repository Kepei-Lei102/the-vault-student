---
chinese: 立体 (lìtǐ)
prerequisites:
  - "[[Geometrical Terms (Vocab)]]"
  - "[[Polygon Angles (Vocab)]]"
leads_to:
  - "[[Surface Area and Volume (Vocab)]]"
  - "[[3D Trigonometry]]"
  - "[[Nets (Vocab)]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-G10
  - syllabus/0580-E4-1
  - type/vocabulary
  - misconception/cylinder-is-not-a-prism
  - misconception/cone-vs-pyramid
---

# Solids 立体

## Definition

A **solid** (立体) is a 3D region bounded by surfaces — the 3D analogue of a polygon. The surfaces can be flat (then we have a **polyhedron**, 多面体) or curved (cylinder, cone, sphere). This card names the standard solids and gives the vocabulary for talking about them; the formulas for surface area and volume are in [[Surface Area and Volume (Vocab)]].

### 中文锚点

立体 = 三维空间中由曲面或平面围成的图形。把多边形 (polygon) 推广到三维，就得到立体。**多面体 (polyhedron)** 是所有面都平的特殊情形（如立方体、棱柱、棱锥），其他常见立体 (圆柱、圆锥、球) 有曲面。这张卡只列名称和词汇；具体公式见 Surface Area and Volume 卡。

---

## The Standard Solids

### Polyhedra (flat-faced)

| English | 中文 | Description |
|---------|------|-------------|
| cube | 立方体 (lìfāngtǐ) | 6 equal square faces, 12 equal edges, 8 vertices |
| cuboid | 长方体 (chángfāngtǐ) | 6 rectangular faces (opposite pairs equal); a "rectangular box" |
| prism | 棱柱 (léngzhù) | two parallel congruent polygon ends joined by rectangles; named for its cross-section ("triangular prism", "hexagonal prism") |
| pyramid | 棱锥 (léngzhuī) / 金字塔 (jīnzìtǎ) | one polygon base, all other faces are triangles meeting at an apex |
| tetrahedron | 四面体 (sìmiàntǐ) | a triangular pyramid — 4 triangular faces, 6 edges, 4 vertices |

A **prism** has a *constant cross-section*: any slice parallel to the ends gives the same polygon. A **pyramid** does not — the cross-section shrinks as you move toward the apex.


### Solids with curved surfaces

| English | 中文 | Description |
|---------|------|-------------|
| cylinder | 圆柱 (yuánzhù) | two parallel circular ends joined by a curved surface; like a "circular prism" |
| cone | 圆锥 (yuánzhuī) | a circular base with a curved surface meeting at an apex; like a "circular pyramid" |
| sphere | 球 (qiú) | every point on the surface is the same distance from the centre |
| hemisphere | 半球 (bànqiú) | half a sphere — flat circular face plus the curved hemisphere |
| frustum | 截头锥 (jiétóu zhuī) | a cone or pyramid with the top cut off parallel to the base — looks like a bucket or a lampshade |

![[solids-tetrahedron-frustum.svg]]

The **tetrahedron** (left) is the simplest pyramid — four triangular faces, all vertices identical. The **frustum of a cone** (right) is what's left after cutting the top off a cone parallel to its base; the dashed lines mark where the missing apex would be, and the labels $R$, $r$, $h$ are exactly the parameters in the volume formula $V = \tfrac{1}{3}\pi h(R^2 + Rr + r^2)$ — see [[Surface Area and Volume (Vocab)]] for the derivation.

> [!tip] "Cylinder is a prism, cone is a pyramid" — informal but useful
> Strictly speaking, a *prism* and a *pyramid* must have polygon bases, so a cylinder is *not* a prism and a cone is *not* a pyramid. **But** all the volume formulas behave the same way: for a prism-or-cylinder, $V = (\text{base area}) \times (\text{height})$; for a pyramid-or-cone, $V = \tfrac{1}{3}(\text{base area}) \times (\text{height})$. Treating the cylinder as a "circular prism" and the cone as a "circular pyramid" makes the formulas memorable. See [[Surface Area and Volume (Vocab)]] for the proper formulas.

---

## Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| face | 面 (miàn) | a flat or curved surface of the solid |
| edge | 棱 (léng) | a line segment where two faces meet |
| vertex (pl. vertices) | 顶点 (dǐngdiǎn) | a corner where three or more edges meet |
| apex | 顶点 / 顶 | the "top" vertex of a pyramid or cone |
| base | 底 (dǐ) / 底面 | the "bottom" face — usually the polygon you build the solid on |
| cross-section | 截面 (jiémiàn) | the 2D shape made by slicing the solid with a plane |
| net | 展开图 (zhǎnkāitú) | the flat 2D pattern you get by unfolding the solid; cutting along edges |
| composite solid | 复合立体 (fùhé lìtǐ) | a solid built by combining standard ones (e.g., cylinder + hemisphere = test tube) |

> [!tip] Nets are the bridge to surface area
> The **net** of a solid is what you get by unfolding it flat — like flattening a cardboard box. The total area of the net equals the surface area of the solid. So "find the surface area of a cube of side $5$" reduces to "find the area of the cross-shaped net of six $5 \times 5$ squares." See [[Surface Area and Volume (Vocab)]].

---

## Counting Faces, Edges, and Vertices

For the standard polyhedra:

| Solid | Faces | Edges | Vertices | $V - E + F$ |
|---|---|---|---|---|
| tetrahedron | 4 | 6 | 4 | 2 |
| cube | 6 | 12 | 8 | 2 |
| octahedron | 8 | 12 | 6 | 2 |
| dodecahedron | 12 | 30 | 20 | 2 |
| icosahedron | 20 | 30 | 12 | 2 |
| triangular prism | 5 | 9 | 6 | 2 |
| square pyramid | 5 | 8 | 5 | 2 |

The last column is always $2$ — that's **Euler's polyhedron formula** $V - E + F = 2$ (see [[Geometrical Terms (Vocab)]]). It works for any *convex* polyhedron (no holes, no self-intersections).

> [!info] Beyond syllabus — the five Platonic solids
> A **regular polyhedron** has every face the same regular polygon and every vertex looking the same. There are exactly **five** of them — the *Platonic solids*: tetrahedron (4 triangles), cube (6 squares), octahedron (8 triangles), dodecahedron (12 pentagons), icosahedron (20 triangles).
>
> ![[solids-platonic-five.svg]]
>
> Plato (c. 360 BC) associated them with the four classical elements plus the cosmos; modern proof of "exactly five" uses Euler's formula plus the constraint that interior angles at a vertex must sum to less than $360°$. The proof is short and beautiful — a one-page argument that there are *exactly* these five and no more.

> [!info] Beyond syllabus — why D&D / Call of Cthulhu use exactly these dice
> The standard polyhedral dice — **D4, D6, D8, D12, D20** — are the five Platonic solids in disguise. That is *not* a coincidence; it's the **defining property of a fair die**. A die is fair when every face has the same probability of landing up, which requires every face to be **identical and identically positioned** — what mathematicians call **face-transitive**. Among convex polyhedra, the only shapes whose faces are all identical *and* whose vertices all look the same are exactly Plato's five. Any other shape would weight some outcomes over others.
>
> The d10 is the rebel: it's a **decagonal trapezohedron**, not a Platonic solid, added to the standard set because percentile rolls (00–99) need a 10-sided die. It *is* face-transitive (the kite-shaped faces are all identical), so it's still fair — but it falls outside the Platonic family because its faces are kites, not regular polygons.
>
> So the next time you roll a d20 for initiative, you're rolling on the *icosahedron* — the same shape Plato in 360 BC associated with water, the chemist Buckminster Fuller in 1948 used for geodesic domes, and the virologist who classified adenoviruses in 1959 found in their protein capsids. Geometry, dice, and DNA-delivery vehicles all share the same regular 20-faced shape because there's literally only one way to be a fair 20-sided thing.

🌍 *"科学，这就是科学的力量！"* —多面体《快乐星球》(2004)

---

## Common Mistakes

1. **"Cylinder has 3 faces, 2 edges, 0 vertices."** The two circular ends are *faces*; the curved surface is *one* face; the two circles where curved meets flat are *edges*; there are no *vertices* in the polyhedron sense. (Some sources count differently — Cambridge usually accepts $3$ faces, $2$ edges, $0$ vertices, but watch the question's exact phrasing.)
2. **Calling every pointy 3D shape a "pyramid."** A cone is *not* a pyramid; it has a curved surface, not flat triangular faces. A pyramid has polygon base + flat triangular sides.
3. **Counting the curved surface as zero faces.** A sphere has *one* curved face (its surface) and no edges or vertices. A cone has *two* faces (the circular base + the curved lateral surface), one edge (the circle), and one vertex (the apex).
4. **Frustum vs prism confusion.** A **frustum** is *not* a prism — its two ends are parallel but *different sizes*. A prism has *congruent* (equal-size) ends. A frustum is what's left of a cone or pyramid after the top is cut off.

---

## Exam Notes

### OxAQA 9260

**Syllabus ref:** G10. The 9260 syllabus lists "faces, surfaces, edges, vertices of cubes, cuboids, prisms, cylinders, pyramids, cones, spheres" as required vocabulary. Most G10 questions test *application* (find the volume) using formulas from [[Surface Area and Volume (Vocab)]], but the language matters for reading the question.

### Cambridge 0580

**Syllabus ref:** E4.3. Same content as 9260 G10. 0580 Extended adds frustums and composite solids in E5.4.

### A-Level / IB / AP

Used as set-up vocabulary for harder geometry — solid of revolution (Calculus), 3D vectors (Mechanics), parametric solids. Anyone going to engineering or physics needs this list cold.

---

## Connections

- **Prerequisite:** [[Geometrical Terms (Vocab)]] — face, edge, vertex defined here
- **Prerequisite:** [[Polygon Angles (Vocab)]] — the polygon faces of a polyhedron
- **Leads to:** [[Surface Area and Volume (Vocab)]] — the formulas for each shape on this list
- **Application:** [[Pythagoras Theorem]] — finding diagonals through 3D space (e.g., space diagonal of a cube $= s\sqrt{3}$)
- **Application:** [[Vectors]] — 3D coordinate geometry; vertices of a cube as position vectors
- **Beyond high school:** *topology* (Euler characteristic), *crystallography* (regular tilings of 3D space), *Platonic solids* in chemistry (carbon-60 fullerene is an icosahedral cage)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $V - E + F = 2$ | `V - E + F = 2` | Euler's polyhedron formula |
| $V$, $E$, $F$ | `V, E, F` | vertex, edge, face counts |
| $s\sqrt{3}$ | `s\sqrt{3}` | space diagonal of a cube of side $s$ |
| $\tfrac{1}{3}$ | `\tfrac{1}{3}` | the famous $\tfrac{1}{3}$ in cone and pyramid volumes |
