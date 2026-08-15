---
chinese: 三次函数图像 (sāncì hánshù túxiàng) / 三次不等式
prerequisites:
  - "[[Sketching Curves (Vocab)]]"
  - "[[Remainder and Factor Theorems]]"
  - "[[Quadratic Inequalities]]"
  - "[[Modulus Function]]"
  - "[[Graphs of Functions]]"
leads_to:
  - "[[Differentiation]]"
  - "[[Complex Numbers]]"
  - "[[Abel the Other Boy Who Died Young]]"
  - "[[Galois at Twenty]]"
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
  - syllabus/0606-4-4
  - syllabus/0606-4-5
  - syllabus/9231-1-2
  - type/deep
  - type/technique
  - notation/cubic
  - misconception/repeated-root-doesnt-cross
  - misconception/inequality-direction-by-leading-coeff
---

# Cubic Graphs and Cubic Inequalities 三次函数图像与三次不等式

## Definition

A **cubic** is a polynomial of degree $3$:

$$y = ax^3 + bx^2 + cx + d, \qquad a \neq 0.$$

Cubics are the first polynomial family with a distinctive *S-shape* — they always have an **inflection point** (where curvature flips) and *up to two* turning points. Compared to quadratics (one parabola, exactly one extremum), cubics double the visual vocabulary: rising and falling segments, multiple roots, and the new geometric move of *touching* the $x$-axis without crossing.

Cubics also unlock a piece of **mathematical history**: the cubic formula (Cardano, 1545) was the discovery that *forced* mathematicians to accept negative numbers under square roots — the first appearance of **complex numbers**. The shapes you sketch on 0606 §4.4 are the visible tip of a 500-year-old story (see Beyond Syllabus).

This card covers two syllabus rows in one place: **§4.4** sketching cubic graphs and their moduli, and **§4.5** solving cubic inequalities. Both rest on the same foundation — *the factored form*.

### 中文锚点

**三次函数 (sāncì hánshù)** = 形如 $y = ax^3 + bx^2 + cx + d$ 的多项式（$a \neq 0$）。

形状关键：
- $a > 0$：图像从左下到右上（"rising S")
- $a < 0$：图像从左上到右下（"falling S"，整体反过来）
- 三次方程**至多三个实根**（与 $x$ 轴的交点）
- **重根 (chóng gēn)**：图像在该点**与 $x$ 轴相切**（不穿过），不是穿过
- **三重根**：图像在根处呈**水平切线**（$y'$ 和 $y''$ 都等于零）

考试套路：
- "**Sketch** $y = a(x-r_1)(x-r_2)(x-r_3)$" → 标 $y$ 截距、三个 $x$ 截距、确定首项符号、画 S 形
- "**Solve** $f(x) > 0$ 或 $f(x) < 0$" → 用根分割数轴，**符号交替** + 检验首项

---

## The Factored Form Tells You Everything

The most useful representation of a cubic is its **factored form**:

$$y = a(x - r_1)(x - r_2)(x - r_3),$$

where $r_1, r_2, r_3$ are the roots (some possibly equal, some possibly complex). From the factored form, sketching is mechanical:

1. **Roots** = the $r_i$ values directly. Plot them as $x$-intercepts.
2. **$y$-intercept** = $y(0) = a(-r_1)(-r_2)(-r_3) = -ar_1 r_2 r_3$.
3. **Direction** = sign of $a$. For $a > 0$, the curve rises from bottom-left and exits to top-right. For $a < 0$, the opposite (top-left to bottom-right).
4. **Sign in each interval** — the polynomial alternates sign between consecutive roots. Pick a test point, then alternate.
5. **Repeated roots** = curve *touches* (doesn't cross) the axis there.

This recipe handles every cubic the 0606 syllabus throws at you.

---

## The Four Canonical Shapes

![[cubic-canonical-shapes.svg]]

Above: the four canonical cubic shapes on 0606. Each one has its own root structure and exam-trap.

| Shape | Roots | Behaviour |
|---|---|---|
| **(a)** Three distinct real roots, $a > 0$ | $r_1 < r_2 < r_3$ | S-curve crosses axis at all three; positive on the right of $r_3$ |
| **(b)** Three distinct real roots, $a < 0$ | $r_1 < r_2 < r_3$ | Mirror of (a) — negative on the right of $r_3$; positive on the left of $r_1$ |
| **(c)** Repeated root + simple root | one double root, one single | Curve *touches* the axis at the double root, *crosses* at the single |
| **(d)** One real root + complex pair | one real, two non-real | S-curve crosses axis once; no second turn back to the axis |

> [!warning] A repeated root **does not cross** the $x$-axis
> The most common 0606 sketch error: drawing $y = (x-1)^2(x+3)$ as if it crosses the axis at $x = 1$. It doesn't — the squared factor *forces* the curve to *touch* the axis at $x = 1$ and bounce back. This is the same "tangent" behaviour you see in [[Discriminant]] when $\Delta = 0$ for a quadratic, generalised to a cubic. Algebraic test: if you substitute slightly above and slightly below the repeated root, the squared factor stays positive on both sides — so the sign of $y$ doesn't flip.

> [!info] A *triple* root is even more extreme — flat tangent at the axis
> $y = (x-1)^3$ has a triple root at $x = 1$. The curve *crosses* the axis (because the factor $(x-1)^3$ flips sign at $x = 1$), but does so with a **horizontal tangent** ($y' = 0$ at $x = 1$). It's the cubic equivalent of "kissing the axis on the way through" — a flat moment of inflection sitting exactly on the axis. You'll meet this geometry again in [[Stationary Points]] as a *horizontal point of inflection*.

---

## Modulus of a Cubic

The transformation $y = \lvert f(x) \rvert$ reflects every part of $f(x)$ that's *below* the $x$-axis to be *above* it. For a cubic with three real roots, this folds the curve into a "WW" shape (or "MM" if $a < 0$): wherever the cubic dipped below, you now have an upside-down cubic-bump above.

**Example.** Sketch $y = \lvert (x+2)(x-1)(x-3) \rvert$.

The underlying cubic $f(x) = (x+2)(x-1)(x-3)$ has three real roots and crosses the axis at each. Its sign by interval (taking $a = +1$):

- $x < -2$: $(-)(-)(-) = -$  → below axis
- $-2 < x < 1$: $(+)(-)(-) = +$ → above axis
- $1 < x < 3$: $(+)(+)(-) = -$ → below axis
- $x > 3$: $(+)(+)(+) = +$ → above axis

For $\lvert f \rvert$, the negative regions ($x < -2$ and $1 < x < 3$) flip to positive. The result has *four* "humps" (alternating up-bump and down-original-up) all sitting on or above the axis, meeting at the three roots $\{-2, 1, 3\}$ where they all touch the axis. The roots become *cusps* (sharp corners) — the modulus function is not differentiable at zero-crossings of the original.

> [!info] $\lvert f(x) \rvert$ vs $f(\lvert x \rvert)$ — two different transformations
> [[Modulus Function]] makes this distinction precisely. $\lvert f(x) \rvert$ takes the cubic and reflects its *negative parts* upward (operates on the $y$-output). $f(\lvert x \rvert)$ takes the cubic on $x \ge 0$ and *mirrors it across the $y$-axis* (operates on the $x$-input). For a cubic, these two transformations look completely different. The 0606 syllabus tests *both* — read the question carefully.

---

## Cubic Inequalities (§4.5)

To solve $f(x) > 0$ (or $< 0$) for a cubic, two equivalent methods:

### Method 1 — sign chart on the number line

1. **Factor** $f(x)$ into linear factors (use [[Remainder and Factor Theorems]] if needed).
2. **Mark roots** on a number line in increasing order.
3. **Test one point** in any interval to find the sign there.
4. **Alternate signs** between consecutive roots — *but watch repeated roots*: a *double* root does not flip the sign (the squared factor stays positive across it).
5. **Read off** the intervals where the sign matches what you want.

### Method 2 — sketch and read

1. **Sketch the cubic** using the canonical-shape rules above.
2. **Read** the intervals where the curve is above (for $> 0$) or below (for $< 0$) the axis.

For 0606, either method earns full marks. Method 1 is faster for clean factored cubics; Method 2 is more reliable when roots are awkward or you've sketched the curve already.

### Worked example — $f(x) > 0$

> Solve $(x+2)(x-1)(x-3) > 0$.

**Roots:** $x = -2, 1, 3$. **Leading coefficient:** $+1$, so far-right is positive.

Sign chart:

| Interval | $(x+2)$ | $(x-1)$ | $(x-3)$ | Product |
|---|---|---|---|---|
| $x < -2$ | $-$ | $-$ | $-$ | $-$ |
| $-2 < x < 1$ | $+$ | $-$ | $-$ | $+$ |
| $1 < x < 3$ | $+$ | $+$ | $-$ | $-$ |
| $x > 3$ | $+$ | $+$ | $+$ | $+$ |

The product is positive on $(-2, 1) \cup (3, \infty)$.

**Final answer.** $\boxed{-2 < x < 1 \;\text{ or }\; x > 3}$.

### Worked example with repeated root — $f(x) \le 0$

> Solve $(x-2)^2 (x+1) \le 0$.

**Roots:** $x = 2$ (double), $x = -1$ (single).

The factor $(x-2)^2$ is $\ge 0$ for *all* $x$. So the sign of the product is controlled entirely by $(x+1)$ — *except* at $x = 2$ where the whole thing equals zero.

| Interval | $(x-2)^2$ | $(x+1)$ | Product |
|---|---|---|---|
| $x < -1$ | $+$ | $-$ | $-$ |
| $-1 < x < 2$ | $+$ | $+$ | $+$ |
| $x > 2$ | $+$ | $+$ | $+$ |

The product is $\le 0$ when $x \le -1$ (negative or zero from the $(x+1)$ factor) **or** at $x = 2$ (where the squared factor makes the product zero).

**Final answer.** $\boxed{x \le -1 \;\text{ or }\; x = 2}$.

The isolated point $x = 2$ in the answer is the geometric signature of the *touch* — the curve dips down to the axis there but doesn't cross, so $f \le 0$ is satisfied at exactly that one point.

> [!warning] Always check leading coefficient — a sign-flip changes everything
> If a problem asks "solve $-(x+2)(x-1)(x-3) > 0$," the sign chart from the example above flips: the answer becomes $x < -2$ or $1 < x < 3$. The leading coefficient is the *direction* of the cubic; never read off intervals without first checking which way the curve is travelling.

---

## Sketching a Cubic — the full workflow

Combining everything: when asked to *sketch* a cubic, use this checklist:

1. **Factor** if not already factored.
2. **Note the leading coefficient $a$** — direction (rising or falling).
3. **Plot the $x$-intercepts** (roots).
4. **Plot the $y$-intercept** ($y(0) = $ constant term).
5. **Identify repeated roots** and mark them as *touch* points, not *cross* points.
6. **Sketch the S-shape** — connect the points smoothly, respecting direction and touch behaviour.

You don't need turning points or inflection points for a *sketch* on 0606 — the question only asks for *qualitative* shape with intercepts. (For A-Level, [[Stationary Points]] adds the quantitative refinement.)

### Worked example — sketch in full

> Sketch $y = (x+1)(x-2)^2$.

- Leading coeff: $+1$ → rising S.
- Roots: $x = -1$ (simple), $x = 2$ (double).
- $y$-intercept: $y(0) = (1)(4) = 4$.
- At $x = -1$: curve *crosses* the axis (sign flips).
- At $x = 2$: curve *touches* the axis (squared factor — no sign flip).

The curve comes up from bottom-left, crosses the axis at $x = -1$, rises to a turning point, falls to *touch* the axis at $x = 2$, then rises back up to the right. Two turning points: one local max between $x = -1$ and $x = 2$, one local min at $x = 2$ (the touch point itself, since the curve dips down and back up).

---

## Common Mistakes

1. **Drawing a repeated root as a crossing.** The squared factor $(x-r)^2$ forces a *touch*, not a cross. Triple roots cross with a horizontal tangent.
2. **Wrong direction from the leading coefficient.** $a > 0$ rises; $a < 0$ falls. Negative $a$ means the *whole* shape is upside-down compared to the canonical rising S.
3. **Forgetting the $y$-intercept.** Many sketches show roots accurately but miss where the curve actually crosses the $y$-axis. $y(0)$ is just the constant term — easy mark.
4. **Sign-chart errors at repeated roots.** A double root does *not* flip the sign of the polynomial; a triple root *does*. Test by writing each factor's sign in each interval and multiplying.
5. **Forgetting to flip when leading coefficient is negative.** If solving $-(x-1)(x-2)(x-3) > 0$, multiply by $-1$ first (and *flip the inequality*) to get $(x-1)(x-2)(x-3) < 0$, then run the standard sign chart.
6. **Treating $\lvert f(x) \rvert$ inequalities the wrong way.** $\lvert f(x) \rvert > 0$ is satisfied *everywhere except at the roots* (since modulus is non-negative). $\lvert f(x) \rvert < c$ for $c > 0$ requires $-c < f(x) < c$ — different from the un-modulus version.

---

## Exam Notes

### Cambridge 0606

**Syllabus refs:** §4.4 sketching cubics + their moduli, §4.5 solving cubic inequalities. Common patterns:

- **Pattern A — sketch from factored form.** "Sketch $y = (x+2)(x-1)(x-3)$, marking the coordinates of any intercepts." Use the canonical-shape recipe.
- **Pattern B — sketch a cubic and its modulus.** "On the same axes, sketch $y = (x-1)(x+2)^2$ and $y = \lvert (x-1)(x+2)^2 \rvert$." Cubic first, then reflect negative parts.
- **Pattern C — find roots and then sketch.** "Show that $x = 2$ is a root of $f(x) = x^3 - 4x^2 + x + 6$, then factorise and sketch." Use [[Remainder and Factor Theorems]] to find the linear factor, then quadratic factor by polynomial division, then sketch from the result.
- **Pattern D — solve $f(x) > 0$ graphically.** Sketch first, read intervals from the sketch.
- **Pattern E — number of solutions of $f(x) = k$.** Translate horizontal line $y = k$ on the sketch, count intersections — typically gives a piecewise answer ($1$, $2$, or $3$ solutions depending on $k$).

> [!tip] Pattern E is the cubic version of the discriminant question
> When 0606 asks "for what values of $k$ does $f(x) = k$ have exactly two solutions?", they're testing whether you can *read horizontal-line intersections* off your sketch. The answer is "$k$ equals the $y$-coordinate of a turning point" — that's where the horizontal line is tangent to the curve, giving a double-root + simple-root configuration. (For 0606 this is read off the sketch; A-Level brings calculus.)

### A-Level / 9709 / IB AA / AP

A-Level extends to:
- **Stationary points** of cubics via $f'(x) = 0$ — **at most** two, since $f'$ is a quadratic and a quadratic has two, one or no real roots: two turning points in the classic S-shape, one stationary inflection when $f'$ has a double root ($y = x^3$ at the origin), or none at all when $f' > 0$ throughout ($y = x^3 + x$, strictly increasing). Classified using $f''$.
- **Inflection point** at $x = -b/(3a)$ — every cubic has exactly one, located by solving $f''(x) = 0$.
- **Curve sketching from scratch** — given coefficients, find roots (rational-root theorem if integers, [[Remainder and Factor Theorems]]), turning points, inflection, and asymptotes (none for a polynomial), then sketch.
- **Connection to integration** — areas under cubics, signed-area considerations when the curve crosses the axis.

IB AA HL treats polynomial equations in general — factor and remainder theorems, and the sum-and-product-of-roots results that [[Symmetric Functions of Roots]] develops in full. Cardano's formula itself is on no board's syllabus, which is exactly why it lives below in Beyond Syllabus. AP Calculus tests cubic shapes via concavity arguments.

---

## Beyond Syllabus

### Cardano's Formula and the Birth of Complex Numbers

For a depressed cubic $y = x^3 + px + q$ (i.e. with no $x^2$ term — any cubic can be brought to this form by a substitution $x \to x - \frac{b}{3a}$), Cardano's formula (1545) gives the roots:

$$x = \sqrt[3]{-\frac{q}{2} + \sqrt{\frac{q^2}{4} + \frac{p^3}{27}}} + \sqrt[3]{-\frac{q}{2} - \sqrt{\frac{q^2}{4} + \frac{p^3}{27}}}.$$

The thing under the inner square root, $\dfrac{q^2}{4} + \dfrac{p^3}{27}$, is the **discriminant of the cubic**. When it's negative, you'd be taking the square root of a negative number — and yet Cardano knew (because he could verify numerically) that the cubic had *three real roots* in this case. The formula was demanding *imaginary numbers* to produce *real answers*.

This was the birth of $i = \sqrt{-1}$. Bombelli, Cardano's intellectual successor, worked out how to compute with these "impossible" numbers in the 1560s. By Euler's time (1740s) they had a name (*imaginary*), an algebra, and a place in mathematics. By Gauss (1799) they had an interpretation (the complex plane). The cubic formula *forced* mathematicians to take complex numbers seriously a century before anyone could explain them.

The historical sequence is poetic: real numbers came from counting and measuring, *negative numbers* came from accounting (debts), *complex numbers came from sketching a cubic*. Geometry and arithmetic each demanded their own number system, and the cubic was where that demand became inescapable.

### The Tartaglia–Cardano–Ferrari Story (1535–1545)

Niccolò Tartaglia (a poor stutterer from Brescia) discovered the cubic formula in 1535 while preparing for a mathematical duel against del Ferro's student Fior. He kept it secret. Cardano (a Milanese physician and gambler) extracted the formula from Tartaglia under oath of secrecy in 1539, then *broke the oath* and published it in *Ars Magna* (1545) — sparking a public feud. Lodovico Ferrari (Cardano's student) extended the technique to **quartics** (degree 4) in the same book.

The story has everything: poverty, a stutterer-vs-aristocrat duel, a broken oath, a duel of mathematicians staged as public theater. Mathematicians don't usually get this much drama. Ferrari ended Tartaglia's career in a 1548 public mathematics duel that Tartaglia, broken, refused to finish.

### The Galois Bombshell — degree 5 has no formula

The natural next question: is there a *quintic* formula (for degree 5)? For 250 years after Cardano, mathematicians searched. In 1824, **Niels Henrik Abel** proved that *no general algebraic formula in radicals exists* for quintics. In the 1830s **Évariste Galois** (dead at age 20 in a duel — for real this time, not mathematical) explained *why*: the *symmetry group* of a polynomial's roots determines whether the polynomial is solvable by radicals, and the symmetric group $S_5$ is "too complicated" — non-abelian and simple in its alternating subgroup $A_5$. This launched **Galois theory**, one of the foundations of modern algebra.

So the cubic is the *last* general polynomial with a formula in radicals. Quartics: yes (Ferrari 1545). Quintics and higher: no. The cubic formula isn't just a quaint historical fact — it's the boundary of what's algorithmically solvable in elementary algebra.

> [!info] The human story — [[Stories/Galois at Twenty]]
> The boy who explained *why* was dead at twenty, in a duel, his manuscripts lost by Cauchy, buried with Fourier, and rejected by Poisson as "incomprehensible." Group theory — the mathematics of symmetry itself — sat unread for eleven years before Liouville opened the envelope. The full drama lives there; the intuition ("study the equation's symmetries, not the equation") is worth carrying back here.
> And the man who proved the quintic *impossible* — Abel, 1824 — has his own tragedy, a near-twin of Galois's: [[Stories/Abel the Other Boy Who Died Young|dead at twenty-six]] of tuberculosis, his masterpiece also mislaid by Cauchy, a Berlin professorship arriving two days after he was buried.

### Cubics in the Real World

- **Bezier curves and computer graphics** — cubic Bezier curves $B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t)t^2 P_2 + t^3 P_3$ are the building block of all vector graphics (PostScript, SVG, PDF, font rendering). Every glyph you see on a screen is made of cubics.
- **Spline interpolation** — cubic splines are the standard for smooth interpolation between data points (smoother than linear, less wiggly than higher-degree).
- **Economics** — cost functions $C(Q) = aQ^3 + bQ^2 + cQ + d$ are the textbook model: high fixed cost, decreasing marginal returns initially, then increasing marginal cost (the "S-curve of returns"). The cubic shape captures the economic story exactly.
- **Population dynamics** — logistic-with-Allee-effect models are cubics, capturing populations that struggle below a critical threshold.
- **Traffic flow** — the Greenshields model gives a cubic relationship between flow and density on a road.

The cubic is everywhere reality has a *transition* between regimes — quadratic isn't enough flexibility, quartic is over-parameterised, but cubic is just right.

---

## Connections

- **Prerequisite:** [[Sketching Curves (Vocab)]] — qualitative-shape discipline applies to cubics
- **Prerequisite:** [[Remainder and Factor Theorems]] — finding roots of an unfactored cubic
- **Prerequisite:** [[Quadratic Inequalities]] — cubic inequalities use the same sign-chart machinery extended to one more factor
- **Prerequisite:** [[Modulus Function]] — for the $\lvert f(x) \rvert$ transformation
- **Sibling:** [[Discriminant]] — quadratic discriminant generalises to cubic; both classify root multiplicities
- **Application:** *computer graphics* — Bezier curves, splines, and font rendering all use cubics
- **Application:** *economics* — S-shaped cost functions, supply-and-demand models with diminishing returns
- **Beyond syllabus:** *Cardano's formula* + *complex numbers* (the historical birth) + *Galois theory* (why no quintic formula exists) + *resolvent cubic* of a quartic
- **Forward:** [[Stationary Points]] — cubic always has exactly one inflection point; up to two turning points
- **Forward:** [[Calculus of Cubics]] — cubics have particularly elegant integration and differentiation properties

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $y = ax^3 + bx^2 + cx + d$ | `y = ax^3 + bx^2 + cx + d` | General cubic |
| $y = a(x-r_1)(x-r_2)(x-r_3)$ | `y = a(x-r_1)(x-r_2)(x-r_3)` | Factored form |
| $y = (x-r)^3$ | `y = (x-r)^3` | Triple root |
| $y = (x-r)^2(x-s)$ | `y = (x-r)^2(x-s)` | Repeated + simple root |
| $\lvert f(x) \rvert$ | `\lvert f(x) \rvert` | Modulus of cubic |
| $f(x) > 0$ on $(a, b) \cup (c, \infty)$ | `f(x) > 0 on (a,b) \cup (c, \infty)` | Typical inequality answer (union form) |
