---
chinese: 直线方程 (zhíxiàn fāngchéng)
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Linear Graphs (Vocab)]]"
  - "[[Gradient (Vocab)]]"
  - "[[Linear Equations (Vocab)]]"
leads_to:
  - "[[Simultaneous Equations (Vocab)]]"
  - "[[Sketching Curves (Vocab)]]"
  - "[[Tangents and Normals]]"
  - "[[Graphical Inequalities (Vocab)]]"
  - "[[Linearisation]]"
  - "[[Parallel Lines (Vocab)]]"
  - "[[Perpendicular Lines (Vocab)]]"
  - "[[Transformations (Vocab)]]"
tags:
  - subject/mathematics
  - domain/algebra
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A11
  - syllabus/0580-E3-5
  - syllabus/0606-7-1
  - syllabus/9709-1-3
  - type/vocabulary
  - notation/mx-plus-c
  - misconception/parallel-vs-perpendicular
---

# Equation of a Straight Line 直线方程

## Definition

Every straight line in the plane has an **equation** — an algebraic relationship that every point $(x, y)$ on the line satisfies, and that no point off the line satisfies. The standard form in the UK curriculum is:

$$y = mx + c$$

where $m$ is the **gradient** (how steep) and $c$ is the **$y$-intercept** (where the line crosses the $y$-axis).

### 中文锚点

直线方程 = 用代数表示一条直线。最常见的形式 $y = mx + c$：$m$ 是斜率（陡度），$c$ 是 $y$ 截距（直线与 $y$ 轴的交点）。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| gradient-intercept form | 斜截式 | $y = mx + c$ — the standard UK form |
| slope-intercept form | 斜截式 | American name, same thing |
| point-slope form | 点斜式 | $y - y_1 = m(x - x_1)$ |
| gradient $m$ | 斜率 $m$ | The coefficient of $x$ in $y = mx + c$ |
| $y$-intercept $c$ | $y$ 截距 $c$ | The constant term in $y = mx + c$ |
| parallel lines | 平行线 (píngxíng xiàn) | Same gradient, never meet |
| perpendicular lines | 垂直线 (chuízhí xiàn) | Gradients multiply to $-1$ |

> [!tip] Why $m$ and $c$?
> The letters are a British convention — $m$ may come from French *monter* ("to climb") or simply be the letter after $l$ (which was already used for "line length"). $c$ stands for **constant**. Americans use $y = mx + b$ instead. The maths is identical; only the letters differ.

---

## Three Standard Forms

### 1. Gradient-intercept form: $y = mx + c$
Most common. Read off gradient and $y$-intercept directly.
- Example: $y = 3x - 2$ has gradient $3$ and $y$-intercept $(0, -2)$.

### 2. Point-slope form: $y - y_1 = m(x - x_1)$
Use when you know one point $(x_1, y_1)$ and the gradient.
- Example: line through $(2, 5)$ with gradient $4$: $y - 5 = 4(x - 2)$.

### 3. General/standard form: $ax + by + c = 0$
Rearranged so everything is on one side. Useful for algebraic manipulation and for vertical lines (which have no gradient, so can't be written as $y = mx + c$).

---

## Finding the Equation

**Given two points** $A(x_1, y_1)$ and $B(x_2, y_2)$:

1. Find the gradient: $m = \dfrac{y_2 - y_1}{x_2 - x_1}$
2. Substitute into point-slope form: $y - y_1 = m(x - x_1)$
3. Rearrange to $y = mx + c$.

**Example:** Line through $(1, 3)$ and $(4, 9)$.
$m = \dfrac{9-3}{4-1} = 2$. Then $y - 3 = 2(x - 1)$ gives $y = 2x + 1$.

---

## Parallel and Perpendicular

Two lines with gradients $m_1$ and $m_2$:

| Relationship | Condition | Example |
|--------------|-----------|---------|
| **Parallel** (平行) | $m_1 = m_2$ | $y = 3x + 1$ and $y = 3x - 7$ |
| **Perpendicular** (垂直) | $m_1 \cdot m_2 = -1$ | $y = 2x$ and $y = -\dfrac{1}{2}x$ |

> [!warning] The $-1$ rule — WHY it works
> If one line has gradient $m$, rotating it 90° swaps rise and run (turning the right triangle on its side) **and** flips one sign. So the new gradient is $-\dfrac{1}{m}$, and $m \cdot \left(-\dfrac{1}{m}\right) = -1$. Horizontal and vertical lines are the edge case: horizontal has $m = 0$, vertical is undefined, and they're clearly perpendicular but the formula breaks down (division by zero).

> [!warning] Perpendicular ≠ "negative gradient"
> A line with gradient $-2$ is **not** perpendicular to a line with gradient $2$ — it's just sloping the other way. For perpendicularity, the gradients must multiply to $-1$. The perpendicular to $y = 2x$ is $y = -\dfrac{1}{2}x$.

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** three rows, not one — **E3.5** (Equations of linear graphs): "interpret and obtain the equation of a straight-line graph", with questions using and requesting lines in different forms; **E3.6** (Parallel lines): gradient and equation of a line parallel to a given line; **E3.7** (Perpendicular lines): the same for perpendicular. The parallel/perpendicular skills are their own examined rows, not sub-clauses.

**Typical phrasing:** "Find the equation of the line passing through $A(2, 1)$ and $B(6, 9)$." "Find the equation of the line parallel to $y = 3x - 2$ passing through $(1, 4)$." "Find the gradient of a line perpendicular to $2y = 3x + 1$."

### OxAQA 9260

**Syllabus ref:** A11 — equation of a straight line from sufficient information (two points, or point and gradient), with parallel and perpendicular gradients.

### Cambridge 0606

**Syllabus ref:** §7 (Straight-line graphs) — the same vocabulary at Additional level: equations in the forms $y = mx + c$ and $ax + by = c$, parallel/perpendicular conditions, plus midpoint and length feeding the coordinate-geometry questions.

### Cambridge 9709 (A-Level)

**Syllabus ref:** P1 §1.3 (Coordinate geometry) — the equation of a line remains directly examined at A-Level: forms $y = mx+c$, $y - y_1 = m(x - x_1)$ and $ax+by+c=0$, parallel/perpendicular gradients, intersections. The vocabulary of this card is assumed instantly.

### Where it is *not* examined

Beyond these, never standalone: Edexcel IAL P1 and IB both fold it silently into calculus (tangents and normals *are* straight-line equations, every time).

---

## Beyond the Syllabus

**Vector form.** At A-Level, lines are written as $\mathbf{r} = \mathbf{a} + t\mathbf{d}$, where $\mathbf{a}$ is a point on the line and $\mathbf{d}$ is a direction vector. This form generalises effortlessly to 3D and beyond, where $y = mx + c$ no longer works.

**Normal form.** $x\cos\theta + y\sin\theta = p$, where $\theta$ is the angle of the perpendicular from the origin and $p$ is its length. Used in computer graphics and physics.

**Linear regression.** In statistics, the "line of best fit" through noisy data is the equation $y = mx + c$ whose $m$ and $c$ are chosen to minimise squared error. This is the cornerstone of empirical science and, eventually, of machine learning.

## Connections

- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — the plane we work in
- **Prerequisite:** [[Linear Graphs (Vocab)]] — visualises the equation
- **Prerequisite:** [[Gradient (Vocab)]] — $m$ is the gradient
- **Leads to:** [[Simultaneous Equations (Vocab)|Simultaneous Equations]] — solving two line equations finds their intersection
- **Leads to:** [[Sketching Curves (Vocab)\|Sketching Curves]] — extends beyond linear to quadratics and higher
- **Leads to:** [[Tangents and Normals]] — tangent lines to curves use the same equation forms
