---
chinese: 多边形的角 (duōbiānxíng de jiǎo)
prerequisites:
  - "[[Angle Properties (Vocab)]]"
  - "[[Angles in Parallel Lines (Vocab)]]"
  - "[[Geometrical Terms (Vocab)]]"
leads_to:
  - "[[Circle Theorems I]]"
  - "[[Similarity]]"
  - "[[Geometrical Proof]]"
  - "[[Solids (Vocab)]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-G4
  - syllabus/0580-E4-1
  - syllabus/0580-E4-6
  - type/vocabulary
  - misconception/interior-exterior-confusion
---

# Polygon Angles 多边形的角

## Definition

A **polygon** (多边形 duōbiānxíng) is a closed shape with straight sides. The angle relationships inside and outside polygons follow from one fact: the angles of a triangle sum to $180°$.

### 中文锚点

多边形的角 = 内角之和 $= (n-2) \times 180°$，外角之和永远 $= 360°$。正多边形的每个内角 $= \dfrac{(n-2) \times 180°}{n}$。

---

## Key Vocabulary

| English | 中文 | Definition |
|---------|------|------------|
| **polygon** | 多边形 | Closed figure with $n$ straight sides |
| **regular polygon** | 正多边形 | All sides equal AND all angles equal |
| **irregular polygon** | 不规则多边形 | Not all sides or angles are equal |
| **interior angle** | 内角 (nèijiǎo) | The angle inside the polygon at a vertex |
| **exterior angle** | 外角 (wàijiǎo) | The angle between one side and the extension of the adjacent side |
| **convex** | 凸多边形 | All interior angles $< 180°$; no "dents" |
| **concave** | 凹多边形 | At least one interior angle $> 180°$; has a "dent" |

---

## The Two Formulas

![[polygon-angles.svg|697]]

### Interior angle sum $= (n - 2) \times 180°$

**WHY (proof by triangle decomposition).** Pick any vertex of an $n$-sided polygon and draw diagonals to all non-adjacent vertices. This splits the polygon into $(n - 2)$ non-overlapping triangles (see left panel above). Since each triangle's angles sum to $180°$, and together these triangles account for every interior angle of the polygon:

$$\text{interior angle sum} = (n - 2) \times 180°$$

The base case is a triangle ($n = 3$, one triangle, $180°$). Each additional side adds one more triangle and one more $180°$.

| Polygon | $n$ | Triangles | Interior angle sum |
|---------|-----|-----------|-------------------|
| Triangle | 3 | 1 | $180°$ |
| Quadrilateral | 4 | 2 | $360°$ |
| Pentagon | 5 | 3 | $540°$ |
| Hexagon | 6 | 4 | $720°$ |
| $n$-gon | $n$ | $n-2$ | $(n-2) \times 180°$ |

### Exterior angle sum $= 360°$ (always)

**WHY (proof by walking).** Stand at any vertex, facing along one side. Walk the perimeter (see right panel above). At each vertex, you turn through the **exterior angle** before continuing along the next side. After visiting all $n$ vertices, you're back where you started, facing the same direction. You've made exactly **one full rotation** — $360°$.

This works for **every** convex polygon, regardless of shape or number of sides. The proof doesn't use the interior angle sum at all — it's an independent fact.

**Alternative proof (from the interior sum).** At each vertex, interior $+$ exterior $= 180°$ (straight line). Summing over all $n$ vertices:

$$\text{interior sum} + \text{exterior sum} = n \times 180°$$
$$(n-2) \times 180° + \text{exterior sum} = n \times 180°$$
$$\text{exterior sum} = n \times 180° - (n-2) \times 180° = 2 \times 180° = 360°$$

### For a regular polygon

All angles are equal, so:

$$\text{each interior angle} = \dfrac{(n-2) \times 180°}{n}, \qquad \text{each exterior angle} = \dfrac{360°}{n}$$

And at every vertex: interior $+$ exterior $= 180°$ (they're supplementary — angles on a straight line).

---

## Common Mistakes

1. **Confusing interior and exterior angle sums.** Interior sum depends on $n$. Exterior sum is always $360°$.
2. **Using the regular-polygon formula on an irregular polygon.** $\dfrac{(n-2) \times 180°}{n}$ only gives each angle when the polygon is **regular**.
3. **Forgetting that interior $+$ exterior $= 180°$ at each vertex.** This is the quickest way to switch between the two.

---

## Exam Notes

**9260 G4 / 0580 E4.3.** "Calculate unknown angles using properties of regular and irregular polygons." Common question types: "The interior angle of a regular polygon is $156°$. How many sides does it have?" Method: exterior $= 180° - 156° = 24°$, so $n = 360° / 24° = 15$ sides.

---

## Beyond the Syllabus

**Tessellation.** A regular polygon tessellates the plane (tiles with no gaps) if and only if its interior angle divides $360°$ evenly. Only three regular polygons work: the equilateral triangle ($60°$), the square ($90°$), and the regular hexagon ($120°$). This connects to crystallography, Islamic geometric art, and the honeycomb conjecture (proved by Hales in 1999: hexagons are the most efficient way to partition a plane into equal areas).

## Connections

- **Prerequisite:** [[Angle Properties (Vocab)]] — supplementary angles at each vertex
- **Prerequisite:** [[Angles in Parallel Lines (Vocab)]] — alternate angles appear in the triangle-sum proof
- **Leads to:** [[Circle Theorems I]] — cyclic quadrilateral theorem uses interior angle sum
- **Leads to:** [[Similarity]] — similar polygons have equal angles
