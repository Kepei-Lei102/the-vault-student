---
chinese: 二次不等式 (èrcì bùděngshì)
prerequisites:
  - "[[Quadratic Equations]]"
  - "[[Discriminant]]"
  - "[[Linear Inequalities (Vocab)]]"
  - "[[Sketching Curves (Vocab)]]"
  - "[[Ordering and Inequalities Notation (Vocab)]]"
leads_to:
  - "[[Cubic Graphs]]"
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
  - syllabus/0606-2-5
  - type/deep
  - type/technique
  - misconception/inequality-direction-by-leading-coeff
  - misconception/dropped-discriminant-case
  - misconception/strict-vs-nonstrict-at-repeated-root
---

# Quadratic Inequalities 二次不等式

## Definition

A **quadratic inequality** asks for the set of $x$ values that make a quadratic expression positive, negative, or zero:

$$ax^2 + bx + c > 0, \qquad ax^2 + bx + c < 0, \qquad ax^2 + bx + c \ge 0, \qquad ax^2 + bx + c \le 0.$$

The answer is almost never a single number — it's an *interval* (or union of intervals). The technique: find where $f(x) = 0$ (the roots), then use the parabola's shape to determine where it's above or below the axis.

The geometry tells the whole story. A parabola is either:
- **Smiling** ($a > 0$, $\smile$): below the axis *between* the roots, above the axis *outside* the roots.
- **Frowning** ($a < 0$, $\frown$): above the axis *between* the roots, below the axis *outside* the roots.

If you remember the parabola's shape and where the roots are, the answer falls out.

### 中文锚点

**二次不等式 (èrcì bùděngshì)** = 求满足 $ax^2 + bx + c > 0$（或别的方向）的 $x$ 的集合。

两步法：
1. **求 $f(x) = 0$ 的根** — 即抛物线与 $x$ 轴的交点
2. **用抛物线形状读区间**：
   - **$a > 0$（开口向上 / 笑脸）**：根之外 $f > 0$，根之间 $f < 0$
   - **$a < 0$（开口向下 / 哭脸）**：根之间 $f > 0$，根之外 $f < 0$

口诀：**"同号取两边，异号取中间"** — 当 $a$ 与不等号方向**同号**时取根的**两侧**；**异号**时取**根之间**。

特殊情况看判别式 $\Delta$（详见 [[Discriminant]]）：
- $\Delta > 0$：两个相异实根，正常情况
- $\Delta = 0$：一个重根，开口向上时 $f \ge 0$ 处处成立（除根处 $f = 0$），$f > 0$ 处处成立**除了根这一点**
- $\Delta < 0$：没有实根，抛物线**完全在 $x$ 轴上方**（$a > 0$）或**完全下方**（$a < 0$），不等式不是恒成立就是恒不成立

---

## Two Methods, Same Answer

### Method 1 — Factor and Sign Chart

1. **Factor** $ax^2 + bx + c$ into two linear factors.
2. **Find the roots** (where each factor is zero).
3. **Mark the roots on a number line**, dividing $\mathbb{R}$ into three intervals.
4. **Test the sign** of each factor (and hence the product) in each interval.
5. **Read off** the intervals where the inequality holds.

This is the same machinery as cubic inequalities ([[Cubic Graphs]]), one factor smaller.

### Method 2 — Sketch the Parabola

1. **Sketch the parabola** $y = ax^2 + bx + c$.
2. **Mark the $x$-intercepts** (the roots).
3. **Read off** the intervals where the curve is above or below the axis, depending on the inequality.

For 0606, both methods earn full marks. Method 2 is faster once you've internalised parabola shapes; Method 1 is more mechanical and harder to mess up.

![[quadratic-inequality-sign-pattern.svg]]

Above: the same two roots $r_1$ and $r_2$, but the *direction* of the parabola flips the inequality answer entirely. Smiling parabola ($a > 0$) → the *outside* of the roots is positive. Frowning parabola ($a < 0$) → the *inside* of the roots is positive. Read the leading coefficient *first*; it controls everything.

---

## Worked Examples

### Example 1 — direct factor (Method 1)

> Solve $x^2 - 5x + 6 > 0$.

**Factor.** $x^2 - 5x + 6 = (x - 2)(x - 3)$. Roots: $x = 2$ and $x = 3$.

**Sign chart.** Leading coefficient is $+1$ (smiling parabola).

| Interval | $(x-2)$ | $(x-3)$ | Product |
|---|---|---|---|
| $x < 2$ | $-$ | $-$ | $+$ |
| $2 < x < 3$ | $+$ | $-$ | $-$ |
| $x > 3$ | $+$ | $+$ | $+$ |

The product is positive on $x < 2$ or $x > 3$.

**Final answer.** $\boxed{x < 2 \;\text{ or }\; x > 3}$.

### Example 2 — sketch method, negative leading coefficient

> Solve $-x^2 + 3x + 4 \le 0$.

**Sketch.** Factor: $-x^2 + 3x + 4 = -(x^2 - 3x - 4) = -(x-4)(x+1)$. Roots at $x = -1$ and $x = 4$. Leading coefficient is $-1$ — **frowning** parabola.

The parabola sits above the axis between the roots ($-1 < x < 4$) and below the axis outside ($x < -1$ or $x > 4$).

For $f(x) \le 0$, we want where the parabola is below or on the axis: $x \le -1$ or $x \ge 4$ (including the roots themselves because of $\le$).

**Final answer.** $\boxed{x \le -1 \;\text{ or }\; x \ge 4}$.

> [!tip] Multiply by $-1$ trick — flip the inequality, then standard recipe
> Some students prefer to multiply through by $-1$ first to get a positive leading coefficient. For Example 2: $-x^2 + 3x + 4 \le 0$ becomes $x^2 - 3x - 4 \ge 0$ (note the *flipped* inequality, since multiplying by $-1$ reverses direction). Then it's a smiling parabola with the standard "outside the roots" answer. Same final answer; less mental gymnastics if you're tired.

### Example 3 — repeated root, watch strict vs non-strict

> Solve $x^2 - 4x + 4 > 0$.

**Factor.** $x^2 - 4x + 4 = (x - 2)^2$. Repeated root at $x = 2$. Discriminant $= 0$.

The parabola touches the $x$-axis at $x = 2$ and sits *above* it everywhere else (smiling parabola, $a > 0$). So $f(x) \ge 0$ for all $x$, with equality only at $x = 2$.

For the *strict* inequality $f(x) > 0$, we need to *exclude* $x = 2$:

**Final answer.** $\boxed{x \neq 2}$ (or equivalently, $x \in \mathbb{R}, x \neq 2$).

For comparison: if the question asked $f(x) \ge 0$ instead, the answer would be **all real $x$**.

> [!warning] Strict vs non-strict at a repeated root — the lone-point trap
> When $\Delta = 0$ the parabola *just barely* touches the axis. Whether the touch point is included in the answer depends on whether the inequality is strict ($>$, $<$) or not ($\ge$, $\le$). This is exactly the situation that bites students on cubic-inequality questions with double roots ([[Cubic Graphs]]). Watch which version of the inequality the question is asking.

### Example 4 — range-of-$k$ problem (the discriminant cash-in)

> Find the values of $k$ for which $x^2 + kx + 9 > 0$ for **all** real $x$.

**Setup.** "For all $x$" means the parabola never touches or dips below the axis. Two conditions are required:
1. Leading coefficient is positive (here it is — $a = 1 > 0$, so the parabola smiles).
2. **The parabola has no real roots** — otherwise, between the roots, $f(x) \le 0$ and the inequality fails.

"No real roots" $\iff \Delta < 0$:

$$\Delta = k^2 - 4(1)(9) < 0 \;\;\Longrightarrow\;\; k^2 < 36 \;\;\Longrightarrow\;\; -6 < k < 6.$$

**Final answer.** $\boxed{-6 < k < 6}$.

> [!info] Why this question reveals the discriminant's true purpose
> "$f(x) > 0$ for all $x$" is the *positive-definite* condition on the quadratic — and the discriminant's job is to *detect* whether that's the case. $\Delta < 0$ with $a > 0$ → strictly positive everywhere. $\Delta < 0$ with $a < 0$ → strictly negative everywhere. $\Delta = 0$ → touches zero at one point. $\Delta > 0$ → crosses through both signs. The discriminant is the algebraic "is-this-quadratic-everywhere-positive?" test, and range-of-$k$ problems are how 0606 tests whether you've internalised it.

### Example 5 — disguised quadratic inequality

> Solve $x^4 - 5x^2 + 4 < 0$.

**Substitute** $u = x^2$, so the inequality becomes $u^2 - 5u + 4 < 0$.

**Factor.** $u^2 - 5u + 4 = (u-1)(u-4)$. Roots: $u = 1, u = 4$.

**Solve in $u$.** Smiling parabola, want it below the axis → between the roots: $1 < u < 4$.

**Translate back to $x$.** $u = x^2$, so $1 < x^2 < 4$, which means $x^2 > 1$ AND $x^2 < 4$.

- $x^2 > 1$ → $x < -1$ or $x > 1$
- $x^2 < 4$ → $-2 < x < 2$

**Intersection.** $\boxed{-2 < x < -1 \;\text{ or }\; 1 < x < 2}$.

(This kind of disguised-quadratic problem is the bridge to [[Substitution Equations]], 0606 §4.3 — same trick on equations rather than inequalities.)

---

## When the Discriminant Decides Everything

The full case-split for $f(x) = ax^2 + bx + c$ with $a > 0$:

| $\Delta$ | Real roots | Sign of $f$ |
|---|---|---|
| $\Delta > 0$ | two distinct roots $r_1, r_2$ | $f > 0$ outside $[r_1, r_2]$, $f < 0$ between |
| $\Delta = 0$ | one repeated root $r$ | $f \ge 0$ everywhere, $f = 0$ only at $r$ |
| $\Delta < 0$ | no real roots | $f > 0$ everywhere |

For $a < 0$, every "$> 0$" and "$< 0$" in the table flips. The discriminant is the *single* number that tells you which row you're in.

This is why the same 0606 paper that asks "find the value of $k$ for which $f(x)$ has equal roots" (a [[Discriminant]] question) often turns around and asks "find the range of $k$ for which $f(x) > 0$ for all $x$" (a quadratic-inequality question). They're the *same algebraic question* phrased two ways: "where does the parabola touch or cross the axis?" The discriminant decides.

> [!info] The same discriminant powers three apparently-different questions
> 1. **Number of solutions:** $\Delta$ counts real roots ($> 0$: two distinct, $= 0$: one repeated, $< 0$: none).
> 2. **Always-positive (or always-negative) test:** "$f(x) > 0$ for all $x$" means $\Delta < 0$ with $a > 0$.
> 3. **Tangency condition:** "line is tangent to curve" means after substituting, $\Delta = 0$ for the resulting quadratic.
>
> All three are answered by inspecting one number. The discriminant is the most-tested concept in 0606 §2 and §4 because it pulls triple duty.

---

## Common Mistakes

1. **Forgetting the leading coefficient determines direction.** Reading "between the roots" off a frowning parabola when you meant a smiling one. Always check the sign of $a$ first.
2. **Treating "or" as "and".** Quadratic inequalities like "$x < 2$ or $x > 3$" describe the *union* of two intervals — write it with "or," not "and." (The intersection "$x < 2$ AND $x > 3$" is the empty set.)
3. **Strict vs non-strict at a repeated root.** $f(x) \ge 0$ at a double root *includes* the root; $f(x) > 0$ *excludes* it. Read the inequality direction carefully.
4. **Missing the $\Delta < 0$ case in range-of-$k$ problems.** "For all $x$" requires *no* real roots — which means $\Delta < 0$, not $\Delta \le 0$. The boundary case $\Delta = 0$ would let $f$ touch zero at one point, violating *strict* positivity.
5. **Forgetting to flip the inequality when multiplying by $-1$.** $-x^2 + 1 > 0$ becomes $x^2 - 1 < 0$ (note the flip), *not* $x^2 - 1 > 0$.
6. **Solving for $u$ but forgetting to solve for $x$.** In disguised-quadratic problems, the answer-in-$u$ is *not* the answer to the question. Substitute $u = x^2$ (or whatever) back and solve the resulting inequality in $x$.

---

## Exam Notes

### Cambridge 0606

**Syllabus ref:** §2.5 — find solution sets for quadratic inequalities, graphically or algebraically. Standard exam patterns:

- **Pattern A — direct quadratic inequality.** "Solve $x^2 - 7x + 12 > 0$." Factor, sign chart (or sketch), state intervals.
- **Pattern B — range-of-$k$ for "always positive" / "always negative".** "Find the values of $k$ for which $f(x) > 0$ for all real $x$." Use $\Delta < 0$ and check leading coefficient.
- **Pattern C — disguised quadratic.** "Solve $2x^4 - 5x^2 + 2 \le 0$." Substitute $u = x^2$, solve in $u$, translate back to $x$.
- **Pattern D — combined with another method.** "Solve $f(x) g(x) > 0$ where $f, g$ are linear or quadratic." Sign chart on each factor, multiply signs, read intervals.

> [!tip] State both pieces of the "always positive" condition
> 0606 markschemes typically award separate marks for: (i) noticing $a > 0$ (the parabola opens upward), and (ii) requiring $\Delta < 0$ (the parabola misses the $x$-axis). Forgetting either loses marks even with the right final answer.

### A-Level / 9709 / IB AA / AP

A-Level extends to:
- **Inequality manipulations involving fractions** — "$\dfrac{x-1}{x+2} > 1$" requires multiplying by $(x+2)^2$ (always positive) to clear the denominator without inequality flips.
- **Modulus inequalities** — solved via squaring (both sides) when both sides are non-negative; otherwise via case-split. See [[Modulus Function]].
- **Two-variable inequalities** ($ax^2 + bxy + cy^2 > 0$ for all $(x, y)$) — the *positive-definite quadratic form* test, requiring both $a > 0$ AND $b^2 - 4ac < 0$. This is the doorway to multivariable optimisation and matrix algebra (eigenvalues of a symmetric matrix).

---

## Beyond Syllabus

### Quadratic Forms — the higher-dimensional version

A *quadratic form* in $n$ variables is

$$Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} = \sum_{i,j} A_{ij} x_i x_j$$

for a symmetric matrix $A$. The question "is $Q(\mathbf{x}) > 0$ for all $\mathbf{x} \neq \mathbf{0}$?" — the *positive definiteness* test — generalises the 1D case on this card. Answer: *yes* iff all eigenvalues of $A$ are strictly positive. The 1D case has $A = (a)$, a $1 \times 1$ matrix, with eigenvalue $a$ — so the test reduces to $a > 0$, exactly the condition for an upward parabola.

This generalisation underlies:
- **Optimisation** — second-order optimality conditions (Hessian must be positive definite at a local minimum)
- **Statistics** — covariance matrices are positive semidefinite
- **Physics** — kinetic-energy quadratic forms are always positive definite (energy is non-negative)
- **Machine learning** — kernel methods (SVMs, Gaussian processes) require positive-definite kernel matrices

### Convex Optimisation — every quadratic inequality is a convex constraint (when $a > 0$)

A 1D quadratic inequality $ax^2 + bx + c \le 0$ with $a > 0$ defines a *convex* set — between two roots, an interval. With $a < 0$, the same inequality defines the *complement* of an interval — generally non-convex.

This is why **convex optimisation** prefers "$\le$" inequalities with positive leading coefficients (and their multivariable generalisations). The whole field of *quadratic programming* (QP) and *quadratically-constrained quadratic programming* (QCQP) hinges on this convexity check. Every Tesla autopilot model-predictive-control loop, every portfolio-optimisation calculation in finance, every robot-arm trajectory planner — they all set up a quadratic objective and a set of quadratic-inequality constraints, then call a QP solver.

The 0606 question "find the range of $k$ such that $f(x) > 0$ for all $x$" is, viewed from above, the question "for what $k$ is this constraint *vacuous*?" — and the answer is exactly the case where the constraint defines all of $\mathbb{R}$, the simplest of all convex sets.

### The Schur Complement and Block Inequalities

A small bonus from linear algebra: the *Schur complement* of a block matrix
$$\begin{pmatrix} A & B \\ B^T & C \end{pmatrix}$$
is positive definite iff $A$ is positive definite *and* $C - B^T A^{-1} B$ is positive definite. This block-decomposition test is the quadratic-inequality machinery on this card, applied to matrix blocks instead of scalars. It's the workhorse of *control theory* (Riccati equations) and *semidefinite programming*. Beautiful generalisation: 0606 §2.5 → linear algebra → control engineering, all the same logic at different scales.

---

## Connections

- **Prerequisite:** [[Quadratic Equations]] — finding the roots is step 1
- **Prerequisite:** [[Discriminant]] — $\Delta$ classifies the cases that drive every range-of-$k$ problem
- **Prerequisite:** [[Linear Inequalities (Vocab)]] — the basic inequality manipulation rules carry over (especially the "flip-when-multiplying-by-negative" rule)
- **Sibling:** [[Cubic Graphs]] — same sign-chart machinery extended to one more factor; the cubic inequality recipe is "this card, but cubic"
- **Application:** *physics — energy bounds* — kinetic energy $\frac{1}{2}mv^2 \ge 0$ is a trivial quadratic-inequality fact; potential-energy minima are quadratic minima
- **Application:** *statistics — variance positivity* — variance $\sigma^2 = \mathbb{E}[(X - \mu)^2] \ge 0$ is the quadratic-inequality reason why covariance matrices are positive semidefinite
- **Beyond syllabus:** *quadratic forms*, *positive-definite matrices*, *convex optimisation*, *quadratic programming*, *Schur complement* — the multivariable generalisation of every idea on this card

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $ax^2 + bx + c > 0$ | `ax^2 + bx + c > 0` | Standard quadratic-inequality form |
| $\Delta = b^2 - 4ac$ | `\Delta = b^2 - 4ac` | Discriminant — decides everything |
| $x \in (-\infty, r_1) \cup (r_2, \infty)$ | `x \in (-\infty, r_1) \cup (r_2, \infty)` | "Outside the roots" interval-union notation |
| $r_1 < x < r_2$ | `r_1 < x < r_2` | "Between the roots" — preferred 0606 notation |
| $f(x) > 0$ for all $x$ | `f(x) > 0 \text{ for all } x` | Positive-definite condition |
| $\smile, \frown$ | `\smile, \frown` | Smiling / frowning parabola mnemonics |
