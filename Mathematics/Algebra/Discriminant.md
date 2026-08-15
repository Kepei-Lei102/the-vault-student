---
chinese: 判别式 (pànbiéshì)
prerequisites:
  - "[[Quadratic Equations]]"
  - "[[Completing the Square]]"
leads_to:
  - "[[Complex Numbers]]"
  - "[[Quadratic Inequalities]]"
teach_together:
  - "[[Coordinate Geometry of the Circle]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-2-3
  - type/deep
  - type/criterion
  - type/proof
  - notation/discriminant-delta
  - misconception/discriminant-vs-roots
  - misconception/equal-roots-counted-twice
---

# Discriminant 判别式

## Definition

For the quadratic equation $ax^2 + bx + c = 0$ (with $a \ne 0$), the **discriminant** is

$$
\boxed{\;\Delta = b^2 - 4ac.\;}
$$

The discriminant's value tells you — *without solving* — exactly how many real roots the equation has, and equivalently how many times the parabola $y = ax^2 + bx + c$ crosses the $x$-axis:

| $\Delta$ | Roots of $ax^2 + bx + c = 0$ | Parabola behaviour |
|---|---|---|
| $\Delta > 0$ | **two distinct real roots** | crosses the $x$-axis at two points |
| $\Delta = 0$ | **one repeated (double) root** | *touches* the $x$-axis (tangent — apex on the axis) |
| $\Delta < 0$ | **no real roots** | misses the $x$-axis entirely |

A single number — born from $b^2 - 4ac$ — answers every "how many solutions?" question for any quadratic. This card states the criterion, derives it from completing the square, links it to line-curve tangency (the connection cashed in by [[Coordinate Geometry of the Circle]]), and works through the standard "find $k$ such that …" exam form.

### 中文锚点

判别式 $\Delta = b^2 - 4ac$ 用来判断二次方程 $ax^2 + bx + c = 0$ 有几个实根，**不需要解出来**：
- $\Delta > 0$ → 两个不同的实根（抛物线与 $x$ 轴相交两次）
- $\Delta = 0$ → 一个重根（抛物线与 $x$ 轴相切）
- $\Delta < 0$ → 没有实根（抛物线与 $x$ 轴不相交）

考试常见问法：
- "Find the values of $k$ for which the equation has two real roots" → 解 $\Delta > 0$
- "Show that the line is tangent to the curve" → 代入消元后的二次方程，证 $\Delta = 0$
- "Find the values of $k$ for which the line meets the curve in two distinct points" → $\Delta > 0$

---

## Where the Formula Comes From

The discriminant *is* the radical inside the quadratic formula. Start from $ax^2 + bx + c = 0$ and complete the square (see [[Completing the Square]]):

$$
ax^2 + bx + c = 0 \;\;\Longrightarrow\;\; a\!\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a}.
$$

Solving for $x$:

$$
\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2} \;\;\Longrightarrow\;\; x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
$$

The quantity inside the square root is exactly $\Delta = b^2 - 4ac$. Now the three cases follow from **what the square root does**:

- $\Delta > 0$: $\sqrt{\Delta}$ is a positive real number; the $\pm$ produces *two distinct* solutions.
- $\Delta = 0$: $\sqrt{\Delta} = 0$; the $\pm$ collapses to a single value — *one repeated root* $x = -\dfrac{b}{2a}$.
- $\Delta < 0$: $\sqrt{\Delta}$ has no real value; *no real solutions*.

The discriminant isn't a separate fact to memorise — it's the *part of the quadratic formula that decides the answer's nature*.

> [!info] Beyond syllabus — complex roots come in conjugate pairs
> When $\Delta < 0$, the quadratic still has *two* roots — but they live in the complex numbers $\mathbb{C}$ rather than $\mathbb{R}$. They take the form $x = -\dfrac{b}{2a} \pm \dfrac{i\sqrt{|\Delta|}}{2a}$, a *complex conjugate pair*. The "no real roots" framing of the $\Delta < 0$ case is shorthand for "two complex roots, no real roots." The Fundamental Theorem of Algebra guarantees every degree-$n$ polynomial has exactly $n$ roots in $\mathbb{C}$ counted with multiplicity — quadratics always have two, even when both are imaginary. A-Level Further and IB AA HL formalise this; see future card *Complex Numbers*.

---

## Geometric Interpretation

![[discriminant-three-cases.svg]]

The parabola $y = ax^2 + bx + c$ has its **vertex** at $\left(-\dfrac{b}{2a}, -\dfrac{\Delta}{4a}\right)$ — and the $y$-coordinate of the vertex is exactly $-\Delta / (4a)$, hidden inside the discriminant. Whether the parabola crosses the $x$-axis depends on whether the vertex is above or below the axis (and whether the parabola opens up or down):

- **Upward parabola** ($a > 0$): vertex below the axis $\Leftrightarrow$ $\Delta > 0$ $\Leftrightarrow$ **two roots**.
- **Upward parabola, vertex on the axis**: $\Delta = 0$, **one repeated root**.
- **Upward parabola, vertex above the axis**: $\Delta < 0$, **no real roots**.

(Mirror the same logic for downward parabolas with $a < 0$.) The discriminant is the algebraic shadow of the geometric question "how does the parabola interact with the $x$-axis?".

---

## Worked Examples

**Example 1 — count roots without solving.**

$2x^2 + 3x - 4 = 0$. Compute $\Delta = 3^2 - 4(2)(-4) = 9 + 32 = 41 > 0$. **Two distinct real roots.** (Specifically, $x = \dfrac{-3 \pm \sqrt{41}}{4}$, but the count is settled before computing.)

**Example 2 — find the value of $k$ for equal roots.**

For what value of $k$ does $x^2 + kx + 9 = 0$ have a repeated root?

Equal roots $\Leftrightarrow$ $\Delta = 0$:

$$k^2 - 4(1)(9) = 0 \;\Longrightarrow\; k^2 = 36 \;\Longrightarrow\; k = \pm 6.$$

**Two values of $k$.** When $k = 6$: $x^2 + 6x + 9 = (x+3)^2 = 0$, so $x = -3$ (double). When $k = -6$: $x^2 - 6x + 9 = (x-3)^2 = 0$, so $x = 3$ (double).

**Example 3 — find the range of $k$ for two real roots.**

For what values of $k$ does $kx^2 + 4x + 1 = 0$ have two real roots?

Two cases to consider — first, $k = 0$ would make the equation linear, not quadratic. Assume $k \ne 0$ and require $\Delta > 0$:

$$4^2 - 4(k)(1) > 0 \;\Longrightarrow\; 16 - 4k > 0 \;\Longrightarrow\; k < 4.$$

Combined with $k \ne 0$: **$k < 4$ and $k \ne 0$**.

> [!tip] Don't forget to check $a \ne 0$ in "find the range of $k$" problems
> When the leading coefficient itself is $k$ (or contains $k$), $a = 0$ would make the equation linear — *outside* the quadratic-equation domain. Always exclude that value separately. A common exam trap.

---

## Line-Curve Intersection — Discriminant of the Substitution

To find where a line $y = mx + c$ meets a curve, **substitute** the line equation into the curve equation. The result is typically a quadratic in $x$ (or in $y$), and *its* discriminant tells you how many intersections:

| Discriminant of substitution | Geometric meaning |
|---|---|
| $\Delta > 0$ | line crosses the curve at two points (a *secant*) |
| $\Delta = 0$ | line is **tangent** to the curve |
| $\Delta < 0$ | line misses the curve entirely |

**Example 4 — show that a line is tangent.**

Show that the line $y = 2x - 3$ is tangent to the curve $y = x^2 - 2x + 1$.

Substitute: $2x - 3 = x^2 - 2x + 1$, i.e., $x^2 - 4x + 4 = 0$. Discriminant: $\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0$. **Tangent.** ✓ (Repeated root at $x = 2$, confirming the line touches at the single point $(2, 1)$.)

**Example 5 — find the line-circle tangent (forward link to Coord Geom).**

For what values of $k$ is $y = 3x + k$ tangent to the circle $x^2 + y^2 = 10$?

Substitute: $x^2 + (3x + k)^2 = 10$, i.e., $10x^2 + 6kx + (k^2 - 10) = 0$. For tangency, $\Delta = 0$:

$$(6k)^2 - 4(10)(k^2 - 10) = 0 \;\Longrightarrow\; 36k^2 - 40k^2 + 400 = 0 \;\Longrightarrow\; -4k^2 = -400 \;\Longrightarrow\; k = \pm 10.$$

**Two values: $k = \pm 10$** — corresponding to the two parallel tangents on opposite sides of the circle. See [[Coordinate Geometry of the Circle]] §"Line–Circle Intersection" for the broader treatment.

---

## Common Mistakes

1. **Sign errors in computing $b^2 - 4ac$.** A negative $a$ or $c$ makes $-4ac$ positive. For $-x^2 + 3x + 2 = 0$: $a = -1$, $b = 3$, $c = 2$, so $\Delta = 9 - 4(-1)(2) = 9 + 8 = 17$. Triple-check signs on $-4ac$.
2. **Counting equal roots as "one root" everywhere.** $\Delta = 0$ gives **one** *value* of $x$, but it's a *repeated* root — algebraically the polynomial factors as $a(x - r)^2$, so it's "two equal roots" in the multiplicity sense. Both phrasings appear; "one repeated root" or "equal roots" is unambiguous.
3. **Forgetting $a \ne 0$.** If the coefficient of $x^2$ involves a parameter, the case where that coefficient is $0$ converts the equation from quadratic to linear — and the discriminant criterion no longer applies. Treat that case separately.
4. **Confusing "two roots" with "two distinct roots."** Cambridge phrasing: "two real roots" usually means *distinct*. "Two equal roots" or "a repeated root" is the $\Delta = 0$ case. If a question says simply "two real roots," $\Delta > 0$.
5. **Sketching the parabola wrong.** The parabola's *direction* (opens up or down) depends on the sign of $a$, not the discriminant. The discriminant only decides *whether* the parabola meets the $x$-axis. Both pieces of information are needed for a sketch.
6. **Solving $\Delta < 0$ with the quadratic formula and getting confused.** $\Delta < 0$ means no real solutions — *don't* try to compute $\sqrt{\text{negative}}$ at 0606 level. Just state "no real roots" and stop.

---

## Exam Notes

### Cambridge 0606

**Syllabus ref:** §2.3. Common patterns:

- "State, with reasons, how many real roots the equation $\ldots$ has." (Compute $\Delta$, state the case.)
- "Find the range of values of $k$ for which $\ldots$ has two distinct real roots." (Solve $\Delta > 0$, often as a quadratic inequality in $k$.)
- "Show that the line $\ldots$ is a tangent to the curve $\ldots$" (Substitute, then $\Delta = 0$.)
- Combined with [[Coordinate Geometry of the Circle]] §8: "For what values of $m$ does the line $y = mx + 5$ intersect the circle $x^2 + y^2 = 9$?" (Substitute, $\Delta > 0$.)

> [!tip] Discriminant inequalities are quadratic in $k$
> When you get to "$\Delta > 0$ in $k$", you typically face a *quadratic inequality in $k$*. Solve it the standard way: factorise, find roots in $k$, sketch a sign chart (see [[Quadratic Equations]]). The whole problem reduces to two layers of quadratic algebra — first in $x$ to set up the discriminant, then in $k$ to solve the inequality.

### Cambridge 9709 — Pure Mathematics 1, §1.1

The named learning objective: **find the discriminant of a quadratic polynomial $ax^2+bx+c$ and use the discriminant** — with the syllabus's own example being *to determine the number of real roots of $ax^2+bx+c = 0$*, and the explicit note that **knowledge of the term "repeated root" is included**. Use that exact phrase in answers: "repeated root" is the syllabus's word for the $\Delta = 0$ case, and examiners look for it.

In practice the 0606 patterns above carry over unchanged — tangency via $\Delta = 0$, ranges of $k$ via a quadratic inequality in $k$ — with P1's line-and-curve questions (§1.3 coordinate geometry) as the usual costume. When $\Delta < 0$ on Paper 3, the roots are a conjugate pair in [[Complex Numbers]].

### Cambridge 9231 Further Mathematics — the discriminant promoted to a mapping tool

Further Pure 1 §1.2 turns this page's tool onto a bigger target: for a rational function, setting $y$ equal to it and clearing the denominator gives **a quadratic in $x$ whose coefficients contain $y$** — and demanding $\Delta \geq 0$ maps out the *entire set of values the function takes*, with the band edges landing on the turning values. The full method, its degenerate case and a worked real-paper example live in [[Rational Functions and Graphs]]. Same $b^2-4ac$, promoted from answering "how many roots?" to charting where a curve can and cannot go.

### IB AA / AP

Same content. AP additionally introduces the discriminant of *general* conic sections ($B^2 - 4AC$ for $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$) which classifies the conic as ellipse, parabola, or hyperbola — a beautiful generalisation, beyond high school but the same algebra.

---

## Connections

- **Prerequisite:** [[Quadratic Equations]] — the formula $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ from which the discriminant is extracted
- **Prerequisite:** [[Completing the Square]] — the derivation route that *shows* where $b^2 - 4ac$ comes from
- **Sibling:** [[Quadratic Inequalities]] — solving $\Delta > 0$ as a quadratic inequality in $k$ uses the same sign-chart machinery
- **Used by:** [[Coordinate Geometry of the Circle]] — the line-circle tangency case explicitly cites the discriminant criterion
- **Application:** *physics* — projectile motion's "does the trajectory hit the wall?" reduces to a discriminant on the trajectory equation; "what's the maximum range?" is the boundary case $\Delta = 0$
- **Application:** *optimisation* — quadratic regression and parabolic fitting use $\Delta$ to detect when the optimisation problem has a unique solution
- **Beyond high school:** *resultants and discriminants of polynomials* (Galois theory) — the discriminant generalises to any-degree polynomial, classifying when roots are distinct vs repeated; the cubic and quartic discriminants are explicit (and infamous) formulas; the *general conic discriminant* $B^2 - 4AC$ classifies conic type

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\Delta$ | `\Delta` | the discriminant; conventional symbol |
| $b^2 - 4ac$ | `b^2 - 4ac` | the formula |
| $\Delta > 0,\;\Delta = 0,\;\Delta < 0$ | `\Delta > 0,\;\Delta = 0,\;\Delta < 0` | the three cases |
| $\dfrac{-b \pm \sqrt{\Delta}}{2a}$ | `\dfrac{-b \pm \sqrt{\Delta}}{2a}` | quadratic formula in terms of $\Delta$ |
| $\sqrt{b^2 - 4ac}$ | `\sqrt{b^2 - 4ac}` | the radical that "wraps" the discriminant |
