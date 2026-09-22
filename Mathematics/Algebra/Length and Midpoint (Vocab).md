---
chinese: 距离与中点 (jùlí yǔ zhōngdiǎn)
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Pythagoras Theorem]]"
leads_to:
  - "[[Coordinate Geometry of the Circle]]"
tags:
  - subject/mathematics
  - domain/algebra
  - domain/geometry
  - level/IGCSE
  - curriculum/Cambridge-0580
  - curriculum/OxAQA-9260
  - syllabus/0580-E3-4
  - syllabus/0606-7-3
  - syllabus/9709-1-3
  - type/vocabulary
  - type/formula
  - notation/distance-formula
  - notation/midpoint-formula
  - misconception/distance-vs-displacement
---

# Length and Midpoint 距离与中点

## Definition

Given two points $A(x_1, y_1)$ and $B(x_2, y_2)$ in the Cartesian plane, this card collects the two formulas you need most often:

> **Length** (distance between $A$ and $B$):
> $$|AB| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}.$$
>
> **Midpoint** of segment $AB$:
> $$M = \left(\dfrac{x_1 + x_2}{2},\ \dfrac{y_1 + y_2}{2}\right).$$

Both follow directly from elementary geometry — the distance formula is **Pythagoras** in disguise, and the midpoint formula is the **component-wise average**.

### 中文锚点

两个朋友住在一座棋盘式城市的两个街角。直线距离有多远？在半路碰头应该约在哪里？从一家走到另一家：往东走若干街区，再往北走若干街区。这两段路就是一个直角三角形的两条直角边，而直线距离是斜边，所以勾股定理直接给出答案：东西方向的差平方，加上南北方向的差平方，再开方。距离公式不过是把坐标填进勾股定理。中点更简单：向东走一半、向北走一半，也就是两个横坐标取平均、两个纵坐标取平均。只要脑子里留着"两段路"这幅图，公式本身根本不用背。

---

## Why the Distance Formula Is Pythagoras

Plot $A$ and $B$ on a coordinate grid. Draw the right triangle with:
- horizontal leg from $A$ to $(x_2, y_1)$ — length $|x_2 - x_1|$
- vertical leg from $(x_2, y_1)$ to $B$ — length $|y_2 - y_1|$
- hypotenuse from $A$ to $B$ — length $|AB|$

By [[Pythagoras Theorem]]:

$$
|AB|^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2 \;\;\Longrightarrow\;\; |AB| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}.
$$

The squaring inside the radical means the formula is **symmetric in the order of points** — $|AB| = |BA|$, as it should be (distance has no direction).

---

## Why the Midpoint Formula Works

The midpoint $M$ is the point equidistant from $A$ and $B$, *on the segment $AB$*. Equivalently, $M$ is the *average position*. Since position has independent $x$- and $y$-components, take the average of each:

$$
M = \left(\dfrac{x_1 + x_2}{2},\ \dfrac{y_1 + y_2}{2}\right).
$$

A clean sanity check: $M$ is the same distance from $A$ as from $B$ — apply the distance formula to verify $|AM| = |MB|$.

---

## Worked Examples

**Example 1 — distance.** Points $A(2, -1)$ and $B(7, 11)$.

$$|AB| = \sqrt{(7-2)^2 + (11-(-1))^2} = \sqrt{25 + 144} = \sqrt{169} = 13.$$

**Example 2 — midpoint.** Same points: $M = \left(\dfrac{2+7}{2}, \dfrac{-1+11}{2}\right) = (4.5, 5)$.

**Example 3 — find the missing endpoint.** $M(3, -2)$ is the midpoint of segment $AB$, with $A(1, 4)$. Find $B$.

Use the midpoint formula and solve for $B(x, y)$:

$$3 = \dfrac{1 + x}{2} \;\Longrightarrow\; x = 5; \qquad -2 = \dfrac{4 + y}{2} \;\Longrightarrow\; y = -8.$$

So $B = (5, -8)$.

---

## Common Mistakes

1. **Sign error inside the squares.** $(x_2 - x_1)^2 \neq x_2^2 - x_1^2$. Square the *difference*, not the difference of squares. With $A(3, 0)$ and $B(-2, 0)$: $|AB| = \sqrt{(-2-3)^2} = \sqrt{25} = 5$, not $\sqrt{(-2)^2 - 3^2} = \sqrt{-5}$.
2. **Forgetting the square root.** $|AB|^2 = 25$ does NOT mean $|AB| = 25$ — it means $|AB| = 5$. The formula gives $|AB|^2$ first; you take $\sqrt{}$ at the end.
3. **Mixing up midpoint with average distance.** Midpoint is the *point* halfway between $A$ and $B$ (a coordinate pair). Average distance is a single number. Don't confuse "$M = (4.5, 5)$" with a length.
4. **Adding instead of averaging.** Midpoint $\neq (x_1 + x_2, y_1 + y_2)$ — that's the *sum* of the position vectors. Divide by 2 to get the average.

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E3.4. Both formulas are tested directly. Expect 1–3 mark questions: "Find the length of segment $AB$", "Find the midpoint of $AB$", "Given $M$ and one endpoint, find the other endpoint."

### Cambridge 0606 Additional Maths

**Syllabus ref:** §7.3 — midpoint and length appear inside coordinate-geometry questions, most often as the setup for a **perpendicular bisector** (midpoint gives the point, length/gradient gives the direction). Rarely asked bare; usually the first two marks of a longer question.

### OxAQA 9660 (International A-Level)

Distance and midpoint are named at P1.2 (with the straight line) and distance again at P2.10 (extended to 3D alongside vectors) — same formulas, coordinates just grow a third entry.

### Edexcel IAL

P4.7.5 examines the distance between two points in **3D** — the Pythagorean extension $\sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}$, one square per axis.

### Beyond — used in every analytic-geometry card

Distance formula is the engine behind:
- [[Coordinate Geometry of the Circle]] — $(x-a)^2 + (y-b)^2 = r^2$ is "distance from $(a,b)$ equals $r$"
- The line equation in vector form
- Vector magnitude $|\mathbf{v}|$ — see [[Vectors]]
- The distance metric in higher dimensions

Midpoint formula extends to:
- $n$-th midpoint (centroid of $n$ points): $\left(\frac{1}{n}\sum x_i, \frac{1}{n}\sum y_i\right)$
- Centroid of a triangle: average of three vertices

---

## Connections

- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — the $(x, y)$ system both formulas live in
- **Prerequisite:** [[Pythagoras Theorem]] — the distance formula is Pythagoras applied in coordinates
- **Sibling:** [[Gradient (Vocab)|Gradient]] — slope of $AB$ is $\dfrac{y_2 - y_1}{x_2 - x_1}$ (length and gradient are the two key segment quantities)
- **Sibling:** [[Equation of a Straight Line (Vocab)|Equation of a Straight Line]] — uses both endpoints to find the line through them
- **Application:** [[Coordinate Geometry of the Circle]] — circle equation comes from the distance formula
- **Application:** [[Vectors]] — vector magnitude $|\mathbf{v}| = \sqrt{v_x^2 + v_y^2}$ is the distance formula with $\mathbf{v} = B - A$
- **Beyond high school:** *metric spaces* — the Euclidean distance formula generalises to $n$ dimensions and to non-Euclidean geometries (taxicab, Hamming, etc.)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\lvert AB \rvert$ | `\lvert AB \rvert` | length of segment $AB$ |
| $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ | `\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}` | distance formula |
| $M = \bigl(\tfrac{x_1+x_2}{2}, \tfrac{y_1+y_2}{2}\bigr)$ | `M = \bigl(\tfrac{x_1+x_2}{2}, \tfrac{y_1+y_2}{2}\bigr)` | midpoint formula |
