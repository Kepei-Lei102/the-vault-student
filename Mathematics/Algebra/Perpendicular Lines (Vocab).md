---
chinese: 垂直直线 (chuízhí zhíxiàn)
prerequisites:
  - "[[Gradient (Vocab)]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Parallel Lines (Vocab)]]"
leads_to:
  - "[[Tangents and Normals]]"
tags:
  - subject/mathematics
  - domain/algebra
  - domain/geometry
  - level/IGCSE
  - curriculum/Cambridge-0580
  - curriculum/OxAQA-9260
  - syllabus/0580-E3-7
  - syllabus/0606-7-2
  - syllabus/9260-A11
  - type/vocabulary
  - type/criterion
  - notation/perpendicular
  - misconception/perpendicular-horizontal-vertical
  - misconception/negative-reciprocal-vs-negative
---

# Perpendicular Lines 垂直直线

## Definition

Two lines in the Cartesian plane are **perpendicular** ($\perp$) when they meet at a right angle ($90°$). The algebraic test:

> **Two non-vertical, non-horizontal lines are perpendicular iff the product of their gradients is $-1$:**
> $$\ell_1 \perp \ell_2 \;\;\Longleftrightarrow\;\; m_1 \cdot m_2 = -1 \;\;\Longleftrightarrow\;\; m_2 = -\dfrac{1}{m_1}.$$
>
> **Edge case:** a horizontal line ($m = 0$) and a vertical line (undefined $m$) are perpendicular by inspection — the formula breaks because of the $0$ and undefined gradients, but the geometry is clear.

The "$-1$" is the algebraic signature of a $90°$ rotation. This card states the criterion, gives the geometric reason, and works through the standard exam patterns.

### 中文锚点

两条直线**垂直**（夹角为 $90°$）当且仅当它们的斜率乘积等于 $-1$：

$$m_1 \cdot m_2 = -1, \qquad \text{即} \quad m_2 = -\dfrac{1}{m_1}.$$

中文常见的说法："斜率互为负倒数"。
- 例：$y = 2x + 1$ 和 $y = -\tfrac{1}{2}x + 3$ 垂直（$2 \times (-\tfrac{1}{2}) = -1$）
- 特殊情况：水平线 $y = c$ 和竖直线 $x = a$ 也垂直，但公式 $m_1 m_2 = -1$ 不适用（因为一个斜率是 $0$，另一个无定义）。直接看图即可。

---

## Why "Negative Reciprocal" Is the Right Algebraic Signature

A line of gradient $m$ rises $m$ units for every $1$ unit of horizontal travel. Its direction vector is $(1, m)$.

A perpendicular line — rotated by $90°$ — has direction vector $(-m, 1)$ (the standard $90°$-rotation $(x, y) \to (-y, x)$). The gradient of a line with direction $(-m, 1)$ is

$$\frac{\text{rise}}{\text{run}} = \frac{1}{-m} = -\frac{1}{m}.$$

So the perpendicular gradient is $-1/m$, and the product $m \cdot (-1/m) = -1$. The "$-1$" comes from the rotation algebra; it's not arbitrary.

> [!info] Beyond syllabus — perpendicularity as dot product = 0
> In vector language, two lines are perpendicular iff their direction vectors have **dot product zero**: $(1, m_1) \cdot (1, m_2) = 1 + m_1 m_2 = 0$, so $m_1 m_2 = -1$. The "negative reciprocal" rule is the dot-product condition translated into gradient language. See [[Vectors]] for the dot-product side; this connection makes the rule memorable in 3D too, where "negative reciprocal" doesn't generalise but "dot product zero" does.

---

## Worked Examples

**Example 1 — verify perpendicular.** Are $\ell_1: y = 3x - 2$ and $\ell_2: y = -\tfrac{1}{3}x + 5$ perpendicular?

$m_1 \cdot m_2 = 3 \cdot (-\tfrac{1}{3}) = -1$. **Yes — perpendicular.** ✓

**Example 2 — find the perpendicular through a point.** Find the line perpendicular to $y = 2x + 1$ passing through $(4, 3)$.

Negative reciprocal of $2$ is $-\tfrac{1}{2}$. Use point-gradient form:

$$y - 3 = -\tfrac{1}{2}(x - 4) \;\;\Longrightarrow\;\; y = -\tfrac{1}{2}x + 5.$$

**Example 3 — find the unknown coefficient.** For what $k$ is $y = kx - 1$ perpendicular to $2x + 3y = 6$?

Rearrange the second: $y = -\tfrac{2}{3}x + 2$, gradient $-\tfrac{2}{3}$. Perpendicularity: $k \cdot (-\tfrac{2}{3}) = -1$, so $k = \tfrac{3}{2}$.

**Example 4 — perpendicular bisector.** Find the perpendicular bisector of segment $AB$ where $A(1, 2)$ and $B(5, 6)$.

- Midpoint of $AB$ (from [[Length and Midpoint (Vocab)]]): $M = (3, 4)$
- Gradient of $AB$: $\dfrac{6 - 2}{5 - 1} = 1$
- Perpendicular gradient: $-1$
- Equation: $y - 4 = -1(x - 3) \Rightarrow y = -x + 7$.

The perpendicular bisector is the line through the midpoint, perpendicular to the segment — see [[Geometrical Constructions (Vocab)]] for the geometric construction.

---

## Common Mistakes

1. **Negative-reciprocal vs negative.** $m_2 = -m_1$ is *not* perpendicular — it's a reflection. Perpendicular is $m_2 = -1/m_1$ (note the **reciprocal**). Example: $y = 2x$ is *not* perpendicular to $y = -2x$; it's perpendicular to $y = -\tfrac{1}{2}x$.
2. **Forgetting the horizontal/vertical edge case.** $y = 3$ (horizontal, $m = 0$) and $x = 7$ (vertical, $m$ undefined) are perpendicular — but $m_1 m_2$ is "$0 \times \text{undefined}$", which the formula can't handle. Recognise the case directly.
3. **Reciprocal without the negative.** $m_1 = 4$, $m_2 = \tfrac{1}{4}$ is *not* perpendicular — that's a different relation (reflection across $y = x$). Perpendicular requires the *negative* reciprocal: $m_2 = -\tfrac{1}{4}$.
4. **Sign drift on the reciprocal.** $m_1 = -3$ → perpendicular gradient is $+\tfrac{1}{3}$, not $-\tfrac{1}{3}$. Take negative *of* the reciprocal: $-(1/m_1) = -(1/(-3)) = +\tfrac{1}{3}$. Two minus signs cancel.
5. **Treating perpendicularity as transitive.** If $\ell_1 \perp \ell_2$ and $\ell_2 \perp \ell_3$, then $\ell_1 \parallel \ell_3$, *not* $\ell_1 \perp \ell_3$. Two right angles add to a straight line.

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E3.7. Tested directly. Common patterns:

- "Show that $\ell_1$ and $\ell_2$ are perpendicular." (Compute $m_1 m_2$.)
- "Find the equation of the line perpendicular to $\ldots$ through the point $\ldots$"
- "Find the equation of the perpendicular bisector of $AB$" (combines this card with [[Length and Midpoint (Vocab)]]).

### Cambridge 0606 / 9260

Same content within §7 (Straight-Line Graphs); appears in coordinate-geometry-of-the-circle problems where the **tangent is perpendicular to the radius** (see [[Coordinate Geometry of the Circle]]).

### A-Level / IB / AP

The criterion extends to vectors via the dot product (see beyond-syllabus callout above). 3D and higher-dimensional perpendicularity uses the dot product directly — the "$-1$" rule doesn't generalise.

---

## Connections

- **Prerequisite:** [[Gradient (Vocab)|Gradient]] — the $m$ in the criterion
- **Prerequisite:** [[Equation of a Straight Line (Vocab)|Equation of a Straight Line]] — point-gradient form for finding the perpendicular line through a point
- **Sibling:** [[Parallel Lines (Vocab)]] — same-gradient is parallelism, negative-reciprocal-gradient is perpendicularity; mirror images
- **Application:** [[Length and Midpoint (Vocab)]] — perpendicular bisector problems combine this card with the midpoint formula
- **Application:** [[Coordinate Geometry of the Circle]] — tangent-line problems use "tangent ⊥ radius" via this rule
- **Application:** [[Geometrical Constructions (Vocab)]] — the *perpendicular bisector* construction with arcs is the geometric counterpart of the algebraic procedure here
- **Beyond high school:** *vector dot product* — "$\mathbf{u} \cdot \mathbf{v} = 0$" is the $n$-dimensional generalisation; the $-1$ rule lives only in 2D

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\perp$ | `\perp` | "is perpendicular to" |
| $m_1 \cdot m_2 = -1$ | `m_1 \cdot m_2 = -1` | perpendicularity criterion |
| $m_2 = -\dfrac{1}{m_1}$ | `m_2 = -\dfrac{1}{m_1}` | negative-reciprocal form |
| $\mathbf{u} \cdot \mathbf{v} = 0$ | `\mathbf{u} \cdot \mathbf{v} = 0` | vector form (beyond syllabus) |
