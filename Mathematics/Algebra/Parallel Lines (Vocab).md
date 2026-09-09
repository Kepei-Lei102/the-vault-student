---
chinese: 平行直线 (píngxíng zhíxiàn)
prerequisites:
  - "[[Gradient (Vocab)]]"
  - "[[Equation of a Straight Line (Vocab)]]"
leads_to:
  - "[[Perpendicular Lines (Vocab)]]"
tags:
  - subject/mathematics
  - domain/algebra
  - domain/geometry
  - level/IGCSE
  - curriculum/Cambridge-0580
  - curriculum/OxAQA-9260
  - syllabus/0580-E3-6
  - syllabus/0606-7-2
  - syllabus/9260-A11
  - type/vocabulary
  - type/criterion
  - notation/parallel
  - misconception/parallel-vertical-lines
---

# Parallel Lines 平行直线

## Definition

Two lines in the Cartesian plane are **parallel** ($\parallel$) when they never meet — they keep the same direction across the plane. The algebraic test:

> **Non-vertical lines are parallel iff they have equal gradients.**
> $$\ell_1 \parallel \ell_2 \;\;\Longleftrightarrow\;\; m_1 = m_2.$$
>
> **Vertical lines** ($x = a$) are all parallel to each other; the test above doesn't apply because their gradient is undefined.

This card covers the algebraic criterion for parallelism, the vertical-line edge case, and how parallel-line problems show up on 0580 / 9260 papers.

### 中文锚点

两条直线**平行**（永不相交）当且仅当它们的**斜率相等**：$m_1 = m_2$。
- 例：$y = 2x + 3$ 和 $y = 2x - 7$ 平行（斜率都是 $2$）
- 例外：竖直线 $x = a$（如 $x = 1$ 和 $x = 5$）的斜率是无定义的，但它们彼此平行——属于"两条都是竖直"这种特殊情况。

---

## Why Equal Gradient Means Parallel

Two non-vertical lines

$$
\ell_1: y = m_1 x + c_1, \qquad \ell_2: y = m_2 x + c_2
$$

intersect when $m_1 x + c_1 = m_2 x + c_2$, i.e., $(m_1 - m_2)x = c_2 - c_1$.

- If $m_1 \neq m_2$, this has the unique solution $x = \dfrac{c_2 - c_1}{m_1 - m_2}$ — the lines cross at exactly one point.
- If $m_1 = m_2$ and $c_1 \neq c_2$, there is *no* solution — the lines never meet (parallel and distinct).
- If $m_1 = m_2$ and $c_1 = c_2$, the equations are identical — same line (parallel and coincident).

So $m_1 = m_2$ is exactly the algebraic condition for "no intersection or coincident" — i.e., parallel.

---

## Worked Examples

**Example 1 — verify parallel.** Are $\ell_1: 2x - 3y = 6$ and $\ell_2: 4x - 6y = 5$ parallel?

Rearrange to slope-intercept form:
- $\ell_1$: $y = \tfrac{2}{3}x - 2$
- $\ell_2$: $y = \tfrac{2}{3}x - \tfrac{5}{6}$

Both have gradient $\tfrac{2}{3}$ and different $y$-intercepts. **Parallel and distinct.** ✓

**Example 2 — find the parallel line through a point.** Find the equation of the line parallel to $y = 4x - 7$ through the point $(2, -1)$.

Same gradient $m = 4$. Use the point-gradient form:

$$y - (-1) = 4(x - 2) \;\;\Longrightarrow\;\; y = 4x - 9.$$

**Example 3 — find the unknown coefficient.** For what value of $k$ is $y = kx + 1$ parallel to $3x + 2y = 5$?

Rearrange the second equation: $y = -\tfrac{3}{2}x + \tfrac{5}{2}$, so its gradient is $-\tfrac{3}{2}$. For parallelism, $k = -\tfrac{3}{2}$.

---

## Common Mistakes

1. **Forgetting the vertical-line case.** "Parallel ↔ $m_1 = m_2$" works for non-vertical lines. Two vertical lines $x = 1$ and $x = 5$ are also parallel, but their gradients are *undefined*, not equal. The full statement: lines are parallel iff *both have the same gradient* OR *both are vertical*.
2. **Mistaking parallel for "perpendicular distance is constant."** That's a *consequence* of being parallel, not the definition. The definition is "never meet" (or equivalently "same direction").
3. **Confusing $y = mx + c_1$ and $y = mx + c_2$ as "the same line if $c_1$ and $c_2$ are close."** Parallel and distinct lines never meet, no matter how close the $y$-intercepts. They're forever a fixed perpendicular distance apart.
4. **Dropping the same-gradient requirement when finding an equation.** "Find the line through $(2, -1)$ parallel to $y = 4x - 7$" — the new line *must* have gradient $4$. Substituting some other gradient defeats the purpose.

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E3.6. Direct: "show that lines $\ell_1$ and $\ell_2$ are parallel" (compare gradients). Most often appears combined with [[Equation of a Straight Line (Vocab)|Equation of a Straight Line]]: "Find the line parallel to … passing through …".

### Cambridge 0606 Additional Maths

**Syllabus ref:** §7.2 — *conditions for parallel or perpendicular lines*, examined as the setup for a line equation ("find the equation of the line through $P$ parallel to $\ell$") and inside perpendicular-bisector and coordinate-geometry problems.

### OxAQA 9660 (International A-Level)

P1.2 names parallel and perpendicular conditions with the straight line; same gradient test, same two-line answer.

### Edexcel IAL

P1.2.2 — *parallel and perpendicular conditions* — one of the first coordinate-geometry rows on P1; the gradient comparison is usually a one-mark step inside a longer question.

---

## Connections

- **Prerequisite:** [[Gradient (Vocab)|Gradient]] — what $m$ measures
- **Prerequisite:** [[Equation of a Straight Line (Vocab)|Equation of a Straight Line]] — point-gradient and slope-intercept forms
- **Sibling:** [[Perpendicular Lines (Vocab)]] — parallelism is "same gradient", perpendicularity is "negative reciprocal gradient" — read both as conditions on $m$
- **Application:** [[Quadrilaterals (Vocab)]] — parallelograms / trapeziums defined by parallel sides
- **Application:** [[Vectors]] — parallel vectors satisfy $\mathbf{u} = k\mathbf{v}$ for some scalar $k$ (gradient analogue)
- **Geometry sibling:** [[Angles in Parallel Lines (Vocab)]] — corresponding, alternate, co-interior angles all assume parallelism

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\parallel$ | `\parallel` | "is parallel to" |
| $m_1 = m_2$ | `m_1 = m_2` | parallelism criterion (non-vertical) |
| $y = mx + c$ | `y = mx + c` | slope-intercept form |
