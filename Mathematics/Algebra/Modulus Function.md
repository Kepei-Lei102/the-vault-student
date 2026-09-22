---
chinese: 绝对值函数 (juéduìzhí hánshù) / 模函数 (mó hánshù)
prerequisites:
  - "[[Graphs of Functions]]"
  - "[[Quadratic Equations]]"
  - "[[Linear Equations (Vocab)]]"
  - "[[Linear Inequalities (Vocab)]]"
leads_to:
  - "[[Cubic Graphs]]"
  - "[[Rational Functions and Graphs]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-1-4
  - syllabus/0606-4-1
  - syllabus/0606-4-2
  - syllabus/9709-2-1
  - syllabus/9709-3-1
  - syllabus/9231-1-2
  - type/deep
  - type/function
  - notation/absolute-value
  - misconception/modulus-inequality-direction
  - misconception/modulus-equation-extraneous-roots
  - misconception/f-of-mod-x-vs-mod-of-f
---

# Modulus Function 绝对值函数

## Definition

The **modulus** (or **absolute value**) of a real number $x$ is its distance from $0$ on the number line — always non-negative:

$$
|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}
$$

Equivalently:

$$
|x| = \sqrt{x^2}.
$$

(Both definitions agree because $\sqrt{}$ returns the *non-negative* root.) The **modulus function** is $y = |x|$ — a V-shaped graph reflecting the negative half of $y = x$ above the $x$-axis.

This card covers what you need for 0606 §1.4 (the relationship between $y = f(x)$ and $y = |f(x)|$), §4.1 (solving $|ax + b| = c$), and §4.2 (modulus inequalities — and the *direction-flip* trap that makes them hard).

### 中文锚点

问一座城离家多远，没有人会因为它在西边而回答"负十二公里"。距离没有正负。绝对值 $|x|$ 就是数轴上的这个意思：$x$ 离 0 有多远，不管它在哪一边，所以 $|-7| = 7$，$|7| = 7$。$y = |x|$ 的图像是一个 V 形：把直线 $y = x$ 左边那一半沿 $x$ 轴折到上面去，关于绝对值的所有道理，都藏在这一折里。$|x - 3|$ 是 $x$ 到 3 的距离。像 $|x - 3| = 2$ 这样的方程有两个解，1 和 5，因为离 3 距离为 2 的点有两个。像 $|x - 3| < 2$ 这样的不等式，说的是离 3 不到 2 的所有数，也就是从 1 到 5 这一段；而 $|x - 3| > 2$ 说的是外面的两条尾巴。心里装着"离……的距离"这个念头，分两种情况、折起来的图像、不等式的"里面还是外面"，就全都成了同一幅画。

### 术语对照 (Terms)

从门口沿直线向东走三米，或向西走三米，你站的位置不同，离门口却一样远。带正负号的位置记着你在哪一边，绝对值只问“隔了多远”。往门口走，距离越来越小；走到门口是零，再继续穿过去，距离又开始变大。把这段路上各个位置对应的距离画出来，就是一个V形：方向可以变，距离不会因此变成负数。

---

## Properties of |x|

The defining properties — every modulus manipulation reduces to these:

| Property | Statement |
|---|---|
| Non-negativity | $\lvert x \rvert \ge 0$ always; $\lvert x \rvert = 0$ iff $x = 0$ |
| Even | $\lvert -x \rvert = \lvert x \rvert$ |
| Multiplicative | $\lvert xy \rvert = \lvert x \rvert \cdot \lvert y \rvert$ |
| Quotient | $\left\lvert \dfrac{x}{y} \right\rvert = \dfrac{\lvert x \rvert}{\lvert y \rvert}$ ($y \ne 0$) |
| Triangle inequality | $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$ |
| Reverse triangle | $\bigl\lvert \lvert x \rvert - \lvert y \rvert \bigr\rvert \le \lvert x - y \rvert$ |
| **Squaring** | $\lvert x \rvert^2 = x^2$  —  the "remove the modulus" lever |

The triangle inequality is the most-cited beyond-syllabus fact — it generalises to vectors, complex numbers, and metric spaces. For 0606, the key three are: non-negativity, $|-x| = |x|$ (even), and $|x|^2 = x^2$ (squaring removes the modulus).

---

## Graph Transformations — Two Different Things

Cambridge 0606 §1.4 distinguishes between two transformations that look superficially similar but produce different graphs:

![[modulus-graph-transformations.svg]]

### $y = |f(x)|$ — reflect negative parts above the $x$-axis

Take any graph $y = f(x)$. Wherever $f(x) \ge 0$, leave it alone. Wherever $f(x) < 0$, **flip that piece across the $x$-axis** (negate the $y$-coordinate). The result is always above (or on) the $x$-axis.

**Example.** $y = x^2 - 3$ dips below the $x$-axis between $x = -\sqrt{3}$ and $x = \sqrt{3}$. The graph $y = |x^2 - 3|$ has that dip *flipped up* — it becomes a "tent" between the two roots, joined smoothly to the parabola arms outside.

The corners (where $f$ crosses zero) become **kinks** in the modulus graph — the function is continuous but not differentiable there. Sharp V-shapes at the zeros of $f$.

### $y = f(|x|)$ — make it even by mirroring the right half

Take $y = f(x)$. Throw away the *left half* of the graph (everything with $x < 0$). Then **mirror** the *right half* (which lives at $x \ge 0$) across the $y$-axis to fill in $x < 0$. The result is always **even** — symmetric about the $y$-axis.

**Example.** $y = x - 1$ is a straight line. $y = |x| - 1$: keep the right-half ray $y = x - 1$ for $x \ge 0$; mirror it to give the left-half ray $y = -x - 1$ for $x < 0$. Result: a V with vertex at $(0, -1)$.

The two transformations are different operations and give different graphs in general. **Do not confuse $|f(x)|$ with $f(|x|)$** — they coincide only when $f$ is itself an even function.

---

## Solving $|ax + b| = c$ — Split Into Two Cases

For $c \ge 0$, the equation $|ax + b| = c$ has the same solutions as

$$
ax + b = c \quad \text{or} \quad ax + b = -c.
$$

(For $c < 0$: no solutions, since $|x| \ge 0$ always.)

**Worked example 1.** Solve $|2x - 5| = 7$.

$2x - 5 = 7 \Rightarrow x = 6$, or $2x - 5 = -7 \Rightarrow x = -1$. **Two solutions: $x = 6, -1$.**

**Worked example 2 — both sides modular.** Solve $|2x + 1| = |x - 4|$.

Squaring both sides (since $|u|^2 = u^2$):

$$(2x + 1)^2 = (x - 4)^2 \;\Longrightarrow\; (2x + 1)^2 - (x - 4)^2 = 0.$$

Difference of squares: $\bigl((2x+1) + (x-4)\bigr)\bigl((2x+1) - (x-4)\bigr) = 0$, i.e., $(3x - 3)(x + 5) = 0$. **Solutions: $x = 1, -5$.**

(The squaring trick is reusable whenever both sides of an equation are modular; it converts the equation into a polynomial equation. Always *check* the answers in the original — squaring can introduce extraneous roots, though here both work.)

> [!tip] The squaring trick extends to inequalities
> Squaring preserves the direction of an inequality **whenever both sides are non-negative** — and $|f|, |g|$ always are. So:
> $$\lvert f \rvert < \lvert g \rvert \;\;\Longleftrightarrow\;\; f^2 < g^2 \;\;\Longleftrightarrow\;\; f^2 - g^2 < 0.$$
> The same factoring as the equation case applies, but now you read the result as a *polynomial inequality* — "between roots" for $<$, "outside roots" for $>$ (the [[Quadratic Equations]] / sign-chart pattern).
>
> **Worked example.** Solve $|2x + 1| < |x - 4|$ — same $f, g$ as Example 2.
>
> Square: $(2x+1)^2 < (x-4)^2$, so $(2x+1)^2 - (x-4)^2 < 0$, factor as $(3x - 3)(x + 5) < 0$, divide out the positive constant: $(x - 1)(x + 5) < 0$. Roots are $x = 1, -5$; the parabola is below the axis *between* the roots:
> $$\boxed{-5 < x < 1.}$$
>
> The corresponding "$>$" inequality $|2x+1| > |x-4|$ has solutions $x < -5$ or $x > 1$ — *outside* the roots. The equation case ($x = 1$ or $x = -5$) is exactly the boundary between the two inequality cases. Three problems, one piece of algebra: factor the polynomial $f^2 - g^2$, then read off depending on whether you want "$<$, $=$, or $>$".
>
> **Caveat:** the squaring trick requires *both* sides to be non-negative. $|f| < g$ where $g$ could be negative is *not* equivalent to $f^2 < g^2$ — handle directly with the case-split rule from the next section.

---

## Modulus Inequalities — The Direction Trap

This is **the** failure mode in modulus problems. The two cases look symmetric but use opposite rules:

> **$|ax + b| < c$ (small modulus)** $\Longleftrightarrow$ **$-c < ax + b < c$**
> The variable is *sandwiched* between $-c$ and $c$.
>
> **$|ax + b| > c$ (large modulus)** $\Longleftrightarrow$ **$ax + b > c$ OR $ax + b < -c$**
> The variable is *outside* the interval $[-c, c]$ — solutions are *two rays*.

The geometric intuition: $|x|$ is distance from $0$. "Distance less than $c$" means inside the interval $(-c, c)$. "Distance greater than $c$" means outside, in two pieces $(-\infty, -c) \cup (c, \infty)$.

![[modulus-inequality-numberline.svg]]

**Worked example 3.** Solve $|3x - 1| < 5$.

$$-5 < 3x - 1 < 5 \;\Longrightarrow\; -4 < 3x < 6 \;\Longrightarrow\; -\dfrac{4}{3} < x < 2.$$

A single interval. ✓

**Worked example 4.** Solve $|2x + 3| \ge 7$.

$$2x + 3 \ge 7 \;\text{or}\; 2x + 3 \le -7 \;\Longrightarrow\; x \ge 2 \;\text{or}\; x \le -5.$$

Two rays. ✓ (Note the "$\le$" partner of "$\ge$" — keep the same inequality direction within each branch.)

> [!tip] Mnemonic for direction
> "$<$ becomes between, $>$ becomes branches" — both start with the same letter as their geometric outcome. **B**etween for **B**ounded; **B**ranches for **B**eyond.

---

## Modulus Equations and Inequalities Combined With Graphs

The **graphical interpretation** is often the fastest route. To solve $|f(x)| = c$ or $|f(x)| > c$:

1. Sketch $y = |f(x)|$ (using the reflect-up transformation above).
2. Draw the horizontal line $y = c$.
3. Read intersection points (for equation) or shaded $x$-regions (for inequality) directly off the sketch.

**Worked example 5 — graphical.** Solve $|x^2 - 4| = 3$.

Sketch $y = |x^2 - 4|$: parabola flipped up between $x = -2$ and $x = 2$, normal parabola outside. The horizontal line $y = 3$ meets this graph at:

- $x^2 - 4 = 3$ on the outer arms: $x^2 = 7 \Rightarrow x = \pm\sqrt{7}$
- $-(x^2 - 4) = 3$ on the flipped middle: $x^2 = 1 \Rightarrow x = \pm 1$

**Four solutions: $x = \pm\sqrt{7}, \pm 1$.**

Algebraically the same answer comes from $|x^2 - 4| = 3 \Leftrightarrow x^2 - 4 = 3 \text{ or } x^2 - 4 = -3$.

---

## Common Mistakes

1. **The inequality direction trap.** $|x| < c$ is *not* "$x < c$ or $x < -c$" (which is trivially $x < c$). It's *both* $x > -c$ AND $x < c$. Conversely, $|x| > c$ is *not* $-c < x < c$ (which is the wrong direction). Mixing these up is the most common modulus error in exams.
2. **$|f(x)| \neq f(|x|)$ in general.** $|x^2 - 4|$ flips the dip up; $(|x|)^2 - 4 = x^2 - 4$ does nothing (because $x^2$ is already even). Different transformations, often different results.
3. **Forgetting the negative case for $c < 0$.** $|x| = -3$ has *no* solutions; $|x| < -3$ has *no* solutions; $|x| > -3$ is true for *all* $x$. The right-hand side's sign matters.
4. **Squaring without checking.** Squaring an equation can introduce extraneous roots. After solving via squaring, always substitute back into the *original* (modular) equation.
5. **Modulus distributing over addition.** $|x + y| \neq |x| + |y|$ in general — the triangle inequality says only $\le$. Counter-example: $|3 + (-3)| = 0 \neq 6 = |3| + |-3|$.
6. **Treating $|x| = x$ universally.** $|x| = x$ only when $x \ge 0$. For $x < 0$, $|x| = -x$ (positive). Don't drop the modulus signs without case-splitting on the sign of the inside.
7. **Sketching $y = |f(x)|$ as if $f$ itself doesn't dip below.** If $f$ has no roots in the domain, then $|f(x)| = f(x)$ — nothing changes. The transformation only does work where $f < 0$.

---

## Exam Notes

### Cambridge 0606

**Syllabus refs:** §1.4 (relationship between $y = f(x)$ and $y = |f(x)|$ for linear, quadratic, cubic, and trig $f$), §4.1 (solve modulus equations), §4.2 (solve modulus inequalities). Expect 4–8 mark questions:

- "Sketch $y = |2x - 1|$" — the V-graph
- "Solve $|3x + 2| = 5$" — two-case algebra
- "Solve $|x - 4| < 6$" — sandwich form
- "Find the values of $x$ for which $|x^2 - 1| > 3$" — graphical or algebraic
- Combined with [[Trigonometric Graphs]]: "Sketch $y = |\sin x|$ for $0 \le x \le 2\pi$" (positive lobes stay; negative lobes reflect up — produces a row of arches with kinks at $x = 0, \pi, 2\pi$).

### Cambridge 9709 (P2 §2.1 and P3 §3.1)

Named in the algebra row of both papers: understand the meaning of $\lvert x\rvert$, sketch $y = \lvert ax + b\rvert$, and solve $\lvert ax+b\rvert = \lvert cx+d\rvert$ and $\lvert ax + b\rvert < c$ — the two-case and squaring methods above are exactly the P2/P3 marks; a modulus equation or inequality is a near-certain short question.

### Cambridge 9231 (FP1 §1.2)

The Further board wants the *graph relatives*: given $y = f(x)$, sketch $y = \lvert f(x)\rvert$ and $y = f(\lvert x\rvert)$ for rational and cubic $f$ — the reflect-the-negative-parts and mirror-the-right-half moves, worked on real papers in [[Rational Functions and Graphs]].

### Edexcel IAL (P3 §1.3; FP2 §1.1)

P3 §1.3 is the modulus function with the graphs of $\lvert f(x)\rvert$ and $f(\lvert x\rvert)$; FP2 §1.1 uses modulus inside inequalities alongside rational functions — the graphical-or-algebraic choice, with the squaring route needing the "both sides non-negative" check.

### Beyond the rows

$\lvert x - a\rvert < \epsilon$ is the language of *limits and convergence* (introductory analysis) — see [[Limit]].

### IB AA HL & AP

Same content. AP includes the modulus function as a piecewise example when defining continuity, differentiability ($|x|$ is continuous everywhere but *not* differentiable at $x = 0$), and as a stepping stone to absolute-value series in BC.

---

## Connections

- **Prerequisite:** [[Graphs of Functions]] — the $y = af(b(x-c))+d$ transformation framework; this card is the modulus instance
- **Prerequisite:** [[Quadratic Equations]] — the squaring trick for $|f| = |g|$ produces a polynomial equation
- **Prerequisite:** [[Linear Equations (Vocab)]] and [[Linear Inequalities (Vocab)]] — the linear cases of modulus problems
- **Sibling:** [[Sketching Curves (Vocab)|Sketching Curves]] — modulus is one of the standard transformations students sketch
- **Application:** [[Trigonometric Graphs]] — $y = |\sin x|$ is a 0606 staple modulus-of-trig sketching question
- **Application:** *limits* (A-Level / IB / AP) — $|x - a| < \epsilon$ is the formal definition of "$x$ is close to $a$"; "convergence to a limit" is a modulus-inequality statement
- **Application:** *physics* — magnitude of a vector $|\mathbf{v}|$ uses the modulus generalisation $|\mathbf{v}| = \sqrt{\mathbf{v}\cdot\mathbf{v}}$
- **Application:** *signal processing* — the *amplitude* of a complex signal $z(t) = a + bi$ is $|z| = \sqrt{a^2 + b^2}$ — direct modulus on $\mathbb{C}$
- **Beyond high school:** *metric spaces* — $|x - y|$ is the standard distance metric on $\mathbb{R}$; abstracting "$|\cdot|$" gives normed vector spaces; the triangle inequality is the defining axiom of every distance metric

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\lvert x \rvert$ | `\lvert x \rvert` | absolute value (preferred over `|x|` to avoid markdown-table column-pipe collisions) |
| $\sqrt{x^2}$ | `\sqrt{x^2}` | square-root form |
| $\lvert ax+b \rvert = c$ | `\lvert ax+b \rvert = c` | modulus equation |
| $\lvert ax+b \rvert < c$ | `\lvert ax+b \rvert < c` | sandwich-form inequality |
| $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$ | `\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert` | triangle inequality |
