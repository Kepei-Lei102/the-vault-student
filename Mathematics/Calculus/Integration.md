---
chinese: 积分 (jīfēn)
prerequisites:
  - "[[Differentiation]]"
  - "[[Power Rule]]"
  - "[[Exponential Function]]"
  - "[[Logarithms]]"
  - "[[Trigonometric Functions]]"
  - "[[Chain Rule]]"
leads_to:
  - "[[Fundamental Theorem of Calculus]]"
  - "[[Integration by Substitution]]"
  - "[[Integration by Parts]]"
  - "[[Standard Integrals]]"
  - "[[Kinematics Calculus]]"
  - "[[Differential Equations]]"
  - "[[Continuous Random Variables]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/AS-Level
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - syllabus/0606-14-10
  - syllabus/0606-14-11
  - syllabus/0606-14-12
  - syllabus/0606-14-13
  - syllabus/9709-1-8
  - syllabus/9709-2-5
  - syllabus/9231-2-4
  - syllabus/9709-3-5
  - type/definition
  - type/theorem
  - type/technique
  - notation/integral
  - notation/definite-integral
  - misconception/forget-plus-c
  - misconception/linear-inside-coefficient
  - misconception/area-vs-signed-integral
---

# Integration 积分

## Definition

**Integration** is the reverse process of [[Differentiation]]. If $F$ is a function whose derivative is $f$ — that is, $F'(x) = f(x)$ — then we call $F$ an **antiderivative** (or **primitive**) of $f$, and we write

$$\int f(x) \, dx = F(x) + C.$$

The elongated-S symbol $\int$ is read **"integral of"**; the $dx$ tells us the variable we are integrating with respect to; the arbitrary constant $C$ is the **constant of integration**.

> 反向导数 — "reverse derivative." That is the whole idea in two words.

---

## Intuition — Two Faces of Integration

Integration wears two hats, and a huge part of understanding it is seeing why they are the same hat.

**Face 1 — Undo differentiation.** Differentiating $x^3$ gives $3x^2$. So integrating $3x^2$ should give us back $x^3$ (plus a constant, because the derivative forgets constants). This is the algebraic face: *integration is an inverse operation.*

**Face 2 — Sum up infinitesimals.** Cut the area under a curve $y = f(x)$ into thin vertical strips of width $dx$ and height $f(x)$. Each strip has area $f(x) \, dx$. Add them all up — that is the "$\int$" (from Latin *summa*, a sum) — to get the total area. This is the geometric face: *integration is a summation.*

The astonishing fact is that these two faces are the **same operation**. That is the content of the [[#Fundamental Theorem of Calculus|Fundamental Theorem of Calculus]], coming up below.

> [!info] Where the symbol comes from
> Leibniz, who invented the notation in the 1670s, wrote $\int$ as a stretched-out "S" for *summa* (sum). The $dx$ was his infinitesimal strip-width. Modern analysis has made all of this rigorous, but the notation is still Leibniz's, and it is still trying to tell you: *integration is adding up tiny things.*

---

## The Constant of Integration 积分常数

Every indefinite integral carries a **+C**. Here is why.

Differentiation kills constants: $\dfrac{d}{dx}(x^3) = 3x^2$ and $\dfrac{d}{dx}(x^3 + 7) = 3x^2$ and $\dfrac{d}{dx}(x^3 - \pi) = 3x^2$. All have the same derivative.

Graphically, adding a constant is a **vertical shift** — it slides the whole curve up or down without changing its *shape*. And the derivative measures shape (the gradient at each point). Slide the curve up: every tangent line slides up with it, but their slopes stay identical.

![[integration-constant-c-same-slope.svg|697]]

So when we go *backwards* from $3x^2$ to its antiderivative, we cannot recover the constant. The best we can say is

$$\int 3x^2 \, dx = x^3 + C.$$

The $+C$ is not decoration. It is the honest admission that an infinite family of functions all answer the question "what has derivative $3x^2$?" Any specific $C$ corresponds to one particular vertical shift of the curve $y = x^3$.

**When does $C$ get pinned down?** When you are given a **boundary condition** — a specific point the curve must pass through. For example: "find the curve with gradient $3x^2$ passing through $(1, 5)$." Then $y = x^3 + C$ with $1^3 + C = 5$ gives $C = 4$, so $y = x^3 + 4$.

> [!warning] Forgetting +C is the single most common mistake
> In an indefinite integral, a missing $+C$ loses marks every time. Drill it into muscle memory: $\int \cdots dx$ and $+C$ are two halves of the same line.

---

## Power Rule for Integration

For any rational $n \ne -1$,

$$\boxed{\int x^n \, dx = \frac{x^{n+1}}{n+1} + C.}$$

**Why it works.** Differentiate the right-hand side and we must get back $x^n$:

$$\frac{d}{dx}\left(\frac{x^{n+1}}{n+1}\right) = \frac{(n+1) x^{n}}{n+1} = x^n. \checkmark$$

**Reverse-the-differentiation mantra.** When differentiating we "bring down the power, then drop the power by one." Integration does the opposite: **raise the power by one, then divide by the new power.** Writing it as a side-by-side helps the muscle memory stick:

| Operation | On $x^n$ |
|---|---|
| Differentiate | $n \cdot x^{n-1}$ — power drops by 1, old power becomes coefficient |
| Integrate | $\dfrac{x^{n+1}}{n+1}$ — power rises by 1, new power becomes divisor |

### Why $n = -1$ is excluded

If we tried to use the formula with $n = -1$, we would write $\dfrac{x^{0}}{0}$ — division by zero. That is the formula's way of telling us $\int x^{-1} \, dx$ is a special case, not given by the power rule.

The answer is known separately. Since $\dfrac{d}{dx}\ln \lvert x \rvert = \dfrac{1}{x}$, we have

$$\int \frac{1}{x} \, dx = \ln \lvert x \rvert + C.$$

The absolute value matters: $\ln$ is only defined for positive inputs, but $1/x$ makes sense for negative $x$ too. Writing $\ln |x|$ covers both halves of the real line.

> [!info] Where does $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$ come from?
> See [[Logarithms]] for the derivation via the inverse-function rule — since $\ln x$ is the inverse of $e^x$, and $(e^x)' = e^x$ (see [[Exponential Function]]), the chain rule gives $(\ln x)' = 1/x$. That is the engine behind this exception to the power rule.

---

## Linearity — Integrating Sums

Integration is **linear**:

$$\int \bigl[a f(x) + b g(x)\bigr] \, dx = a \int f(x) \, dx + b \int g(x) \, dx.$$

Two rules in one: constants come outside, and the integral of a sum is the sum of the integrals. This lets you integrate any polynomial term-by-term.

> Example. $\int (3x^4 - 2x + 7) \, dx = \dfrac{3x^5}{5} - x^2 + 7x + C.$

---

## The Linear-Inside Rule — $(ax + b)^n$

A special case you will use constantly:

$$\boxed{\int (ax + b)^n \, dx = \frac{(ax + b)^{n+1}}{a(n+1)} + C \quad (n \ne -1).}$$

Notice the extra division by $a$. This is the [[Chain Rule]] running in reverse.

**Proof.** Differentiate the right-hand side using the chain rule:

$$\frac{d}{dx}\left(\frac{(ax + b)^{n+1}}{a(n+1)}\right) = \frac{(n+1)(ax + b)^n \cdot a}{a(n+1)} = (ax + b)^n. \checkmark$$

The $a$ from the chain rule and the $a$ in the denominator cancel — exactly as designed.

> [!tip] You are secretly doing integration by substitution
> The "linear-inside rule" is not a new trick — it is [[Integration by Substitution]] hiding under a baby name. Set $u = ax + b$, so $du = a \, dx$ and $dx = du/a$. Then
> $$\int (ax+b)^n \, dx = \int u^n \cdot \frac{du}{a} = \frac{1}{a} \cdot \frac{u^{n+1}}{n+1} + C = \frac{(ax+b)^{n+1}}{a(n+1)} + C.$$
> The mysterious $/a$ is exactly the factor that falls out of $du = a \, dx$. Once you see this, the general substitution technique will feel like a natural extension rather than a new topic.

> [!warning] The missing $/a$ is the second-most-common mistake
> $\int (2x + 5)^3 \, dx = \dfrac{(2x+5)^4}{\mathbf{2} \cdot 4} + C$, **not** $\dfrac{(2x+5)^4}{4} + C$. The $/2$ is how integration "undoes" the chain-rule factor of 2 that differentiation would have produced.

**$n = -1$ case.** Same spirit:

$$\int \frac{1}{ax + b} \, dx = \frac{1}{a} \ln \lvert ax + b \rvert + C.$$

> Example. $\int \dfrac{1}{2x - 7} \, dx = \dfrac{1}{2} \ln|2x - 7| + C.$

---

## Standard Integrals Table

This table is worth memorising. Everything on the left is differentiated and the right is the antiderivative. The $/a$ in the linear-inside rows is the chain-rule reversal.

| $f(x)$ | $\displaystyle \int f(x) \, dx$ |
|---|---|
| $x^n \; (n \ne -1)$ | $\dfrac{x^{n+1}}{n+1} + C$ |
| $\dfrac{1}{x}$ | $\ln \lvert x \rvert + C$ |
| $(ax + b)^n \; (n \ne -1)$ | $\dfrac{(ax + b)^{n+1}}{a(n+1)} + C$ |
| $\dfrac{1}{ax + b}$ | $\dfrac{1}{a} \ln \lvert ax + b \rvert + C$ |
| $e^x$ | $e^x + C$ |
| $e^{ax + b}$ | $\dfrac{1}{a} e^{ax + b} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\sin(ax + b)$ | $-\dfrac{1}{a} \cos(ax + b) + C$ |
| $\cos(ax + b)$ | $\dfrac{1}{a} \sin(ax + b) + C$ |
| $\sec^2(ax + b)$ | $\dfrac{1}{a} \tan(ax + b) + C$ |

> [!tip] The sign flip on sine
> $\int \sin x \, dx = -\cos x + C$ (note the minus), while $\int \cos x \, dx = +\sin x + C$. Way to remember: $\cos$ differentiates to $-\sin$, so integrating $\sin$ gives $-\cos$ to undo that sign.

---

## Definite Integrals — The Fundamental Theorem of Calculus

A **definite integral** evaluates an integral between two specific limits $a$ and $b$:

$$\int_a^b f(x) \, dx = \bigl[F(x)\bigr]_a^b = F(b) - F(a),$$

where $F$ is any antiderivative of $f$. This is the **Newton–Leibniz formula** — the practical half of the [[Fundamental Theorem of Calculus]]. The full theorem comes in *two* parts (FTC1 establishes that every continuous function *has* an antiderivative; FTC2 is the computation formula above), with proofs and the famous Newton-vs-Leibniz priority dispute treated in the dedicated card.

The formula is the bridge that fuses the two faces of integration: integration is fundamentally a summation (geometric face), differentiation is a limit of ratios (algebraic face), and the fact that the two operations are inverses of each other is a *theorem*, not a definition. Newton and Leibniz discovered it independently in the late 1600s; without it, you would compute areas one infinitesimal strip at a time forever.

**Why $+C$ disappears.** If $F(x) + C$ is another antiderivative, then $\bigl[F(x) + C\bigr]_a^b = (F(b) + C) - (F(a) + C) = F(b) - F(a)$. The $C$ cancels — it contributes nothing to a definite integral.

**Why it works geometrically.** The value $\int_a^b f(x) \, dx$ is the signed area between the curve $y = f(x)$ and the $x$-axis from $x = a$ to $x = b$. The FTC says this area equals $F(b) - F(a)$ — the *change* in an antiderivative over the interval. **Area is accumulation of a rate**, and the antiderivative is the accumulator.

> Example. $\displaystyle \int_1^3 2x \, dx = \bigl[x^2\bigr]_1^3 = 9 - 1 = 8.$ Geometrically this is the area of the trapezium under $y = 2x$ from $x=1$ to $x=3$, which is $\tfrac{1}{2}(2 + 6)(2) = 8$. ✓

### Properties of Definite Integrals

1. **Reversing limits flips the sign:** $\displaystyle \int_a^b f = -\int_b^a f.$
2. **Additivity:** $\displaystyle \int_a^b f + \int_b^c f = \int_a^c f.$
3. **Linearity** still holds, same as for indefinite.

---

## Area Under a Curve 曲线下的面积

For $f(x) \ge 0$ on $[a, b]$, the integral $\int_a^b f(x) \, dx$ is the **area** of the region bounded by:

- the curve $y = f(x)$,
- the $x$-axis,
- the vertical lines $x = a$ and $x = b$.

**Below the axis = negative contribution.** If $f$ dips below the $x$-axis on part of $[a, b]$, that part contributes *negative* area to the integral. So for total enclosed area (always positive), you must split the integral at each crossing point and take $\lvert \cdots \rvert$ of the parts that came out negative.

> [!warning] Signed integral $\ne$ enclosed area, in general
> $\displaystyle \int_{-\pi}^{\pi} \sin x \, dx = 0$ — because the positive and negative halves cancel. But the *enclosed area* is $4$. When a question asks for "area," check whether the curve crosses the axis, and split accordingly.

### Area Between Two Curves

For two curves $y = f(x)$ and $y = g(x)$ with $f(x) \ge g(x)$ on $[a, b]$:

$$\text{Area} = \int_a^b \bigl[f(x) - g(x)\bigr] \, dx = \int_a^b \bigl[\text{upper} - \text{lower}\bigr] \, dx.$$

Always subtract lower from upper. If the curves cross on $[a,b]$, split at each intersection.

---

## Improper Integrals

An **improper integral** is one where the integrand misbehaves at an endpoint (typically blowing up to infinity) but the integral may still converge to a finite value. Two flavours show up on exam papers:

- **Type I — infinite limit of integration:** $\displaystyle \int_1^{\infty} \frac{1}{x^2} \, dx$, $\displaystyle \int_{-\infty}^{0} e^x \, dx$, etc. Compute by taking the antiderivative and a limit.
- **Type II — integrand blows up at an endpoint:** $\displaystyle \int_0^1 \frac{1}{\sqrt{x}} \, dx$, $\displaystyle \int_0^1 \frac{1}{x} \, dx$, etc.

**Convergence vs divergence.** Some improper integrals give finite answers; some don't.

> Example (converges). $\displaystyle \int_0^1 x^{-1/2} \, dx = \bigl[2\sqrt{x}\bigr]_0^1 = 2 - 0 = 2.$ The integrand $1/\sqrt{x}$ is undefined at $x = 0$, but the antiderivative $2\sqrt{x}$ behaves perfectly well there.

> Example (diverges). $\displaystyle \int_0^1 x^{-1} \, dx = \bigl[\ln x\bigr]_0^1$ — but $\ln 0 = -\infty$, so the integral diverges (no finite area).

**The rough rule** for $\int_0^1 x^{-p} \, dx$: converges for $p < 1$, diverges for $p \ge 1$. The cutoff is exactly where the power rule breaks (at $p = 1$, i.e. $n = -1$) — not coincidence.

**Where this is required:**
- **9709 P1** — explicitly lists "simple improper integrals" as a learning objective. Expect problems like $\int_0^1 x^{-1/2} dx$ or $\int_1^\infty x^{-2} dx$.
- **AP Calculus BC** — improper integrals are a named topic (convergence tests, infinite bounds, vertical asymptotes). You must be able to evaluate and determine convergence.
- **IB AA HL** — improper integrals appear in the context of p-series convergence.

---

## Volume of Revolution 旋转体体积

Rotate a region bounded by $y = f(x)$, the $x$-axis, and $x = a$, $x = b$ fully around the $x$-axis. The solid that sweeps out has volume

$$\boxed{V = \pi \int_a^b y^2 \, dx = \pi \int_a^b [f(x)]^2 \, dx.}$$

**Why — the disc method.** Each thin vertical strip of width $dx$ at position $x$, height $f(x)$, sweeps out a thin **disc** of radius $f(x)$ and thickness $dx$. A disc has volume $\pi r^2 \, dx = \pi [f(x)]^2 \, dx$. Summing (integrating) over all discs from $a$ to $b$ gives the formula.

![[volume-of-revolution-disc-method.svg|697]]

The picture is everything. On the left, the flat region under $y = \sqrt{x}$. A single thin strip is highlighted. Spin that region around the $x$-axis. The highlighted strip sweeps out the red disc shown on the right — radius $f(x)$, thickness $dx$, volume $\pi [f(x)]^2 \, dx$. Every other strip does the same thing at its own $x$. Integration is the act of summing all those discs.

About the $y$-axis, the same reasoning with $x = g(y)$:

$$V = \pi \int_c^d x^2 \, dy = \pi \int_c^d [g(y)]^2 \, dy.$$

For a region between two curves (like a washer), rotating $\{(x, y) : g(x) \le y \le f(x)\}$ about the $x$-axis:

$$V = \pi \int_a^b \bigl([f(x)]^2 - [g(x)]^2\bigr) \, dx.$$

---

## Worked Examples

### Example 1 — Find the curve through a point

Find the curve with gradient $\dfrac{dy}{dx} = 4x - 3$ passing through $(2, 1)$.

$$y = \int (4x - 3) \, dx = 2x^2 - 3x + C.$$

Substitute the point: $1 = 2(4) - 3(2) + C = 8 - 6 + C$, so $C = -1$.

$$\boxed{y = 2x^2 - 3x - 1.}$$

### Example 2 — Linear-inside rule

Evaluate $\displaystyle \int (2x + 5)^3 \, dx.$

Using the linear-inside rule with $a = 2$, $n = 3$:

$$\int (2x + 5)^3 \, dx = \frac{(2x + 5)^4}{2 \cdot 4} + C = \frac{(2x + 5)^4}{8} + C.$$

**Check by differentiating:** $\dfrac{d}{dx}\left[\dfrac{(2x+5)^4}{8}\right] = \dfrac{4(2x+5)^3 \cdot 2}{8} = (2x+5)^3$. ✓

### Example 3 — Definite integral and area

Find the area between the curve $y = 4 - x^2$ and the $x$-axis.

First find where the curve meets the $x$-axis: $4 - x^2 = 0 \Rightarrow x = \pm 2$. The curve is positive between $-2$ and $2$, so

$$\text{Area} = \int_{-2}^{2} (4 - x^2) \, dx = \left[4x - \frac{x^3}{3}\right]_{-2}^{2} = \left(8 - \frac{8}{3}\right) - \left(-8 + \frac{8}{3}\right) = \frac{32}{3}.$$

### Example 4 — Volume of revolution

The region bounded by $y = \sqrt{x}$, $x = 0$, and $x = 4$ is rotated about the $x$-axis. Find the volume.

$$V = \pi \int_0^4 (\sqrt{x})^2 \, dx = \pi \int_0^4 x \, dx = \pi \left[\frac{x^2}{2}\right]_0^4 = \pi \cdot 8 = 8\pi.$$

### Example 5 — Exponential and trig combined (9709 P2)

Evaluate $\displaystyle \int \left(e^{3x + 1} + \cos(2x) - \frac{1}{5x - 2}\right) \, dx.$

Term by term:

$$= \frac{1}{3} e^{3x+1} + \frac{1}{2} \sin(2x) - \frac{1}{5} \ln|5x - 2| + C.$$

Each term carries its own $1/a$ from the linear-inside rule.

---

## Misconceptions

### 1. "The +C is optional"

**No.** An indefinite integral without $+C$ is **wrong**, not just informal. The $+C$ acknowledges the infinite family of antiderivatives — leaving it off says "the antiderivative is unique," which is false.

The only time $+C$ legitimately disappears is in a definite integral (where it cancels in the subtraction) or after a boundary condition has pinned it down to a specific value.

### 2. "$\int (ax + b)^n \, dx = \dfrac{(ax+b)^{n+1}}{n+1}$"

**No — the missing $/a$.** Correct form:

$$\int (ax + b)^n \, dx = \frac{(ax + b)^{n+1}}{a(n+1)} + C.$$

**Fix:** after every linear-inside integration, differentiate your answer mentally and confirm you get back what you started with. The chain rule pulls out a factor of $a$, so you must have divided by $a$ to cancel it.

### 3. "Signed integral equals area"

**No.** For a curve that dips below the $x$-axis, the signed integral adds negative contributions, while "area" in the geometric sense is always positive. When a question asks for "the area enclosed," you must check whether the curve crosses the axis and split if necessary.

### 4. "Integrate to get velocity from displacement"

**Backwards.** Displacement $s$ → velocity $v = \dfrac{ds}{dt}$ is a *derivative*. To get displacement from velocity you *integrate*: $s = \int v \, dt$. See [[Kinematics Calculus]].

### 5. "Volume about $y$-axis uses the same formula with $y$"

**Nearly — but you must express $x$ as a function of $y$ first.** The formula is $V = \pi \int_c^d [g(y)]^2 \, dy$ where $g(y)$ is $x$ written in terms of $y$, and the limits $c$, $d$ are $y$-values. Don't just swap letters in the $x$-axis formula.

---

## Exam Notes

### Cambridge 0606 — Additional Mathematics

Covered in §14.10–14.13:
- §14.10 — integration as reverse of differentiation.
- §14.11 — integrate sums of terms in powers of $x$ (including $\tfrac{1}{x}$, $\tfrac{1}{ax+b}$).
- §14.12 — integrate $(ax+b)^n$, $\sin(ax+b)$, $\cos(ax+b)$, $\sec^2(ax+b)$, $e^{ax+b}$.
- §14.13 — definite integrals; areas between a line and curve, between two curves, sum of areas.

0606 does **not** require substitution or integration by parts — those are A-Level only.

### Cambridge A-Level 9709 — Pure Mathematics 1 (Paper 1)

§1.8 — AS-level foundations:
- Integrate $(ax + b)^n$ for rational $n \ne -1$, with constant multiples, sums, differences.
- Solve problems involving the constant of integration (boundary-value problems).
- Evaluate definite integrals, including simple improper integrals such as $\int_0^1 x^{-1/2} dx$.
- Apply definite integration to find **areas** bounded by a curve and lines, between a curve and a line, or between two curves.
- Apply definite integration to find **volumes of revolution** about either axis.

### Cambridge A-Level 9709 — Pure Mathematics 2 (Paper 2)

§2.5 — extends P1:
- Integrate $e^{ax+b}$, $\dfrac{1}{ax+b}$, $\sin(ax+b)$, $\cos(ax+b)$, $\sec^2(ax+b)$.
- Use trig identities (e.g. double-angle formulae) to integrate $\sin^2 x$, $\cos^2(2x)$, etc.
- Trapezium rule for numerical estimation of definite integrals (including whether it over- or under-estimates).
- **Integration by substitution is NOT required on P2** — that is Paper 3 only.

### Cambridge A-Level 9709 — Pure Mathematics 3 (Paper 3)

§3.5 — full A-Level toolkit. See separate cards:
- [[Integration by Substitution]]
- [[Integration by Parts]]
- Partial fractions for rational integrands (covered in a future card).
- Recognition of $\dfrac{kf'(x)}{f(x)}$ form, giving $k \ln|f(x)| + C$.

### IB AA HL / AP Calculus

Both curricula include the foundations covered here plus substitution, by-parts, and numerical methods (trapezium, Simpson's). See paired cards.

> [!info] How AP introduces integration — via Riemann sums
> Cambridge (and most UK-style syllabuses) introduces integration as "the reverse of differentiation" and evaluates areas as a consequence. **AP Calculus takes the opposite road:** it introduces the definite integral *first*, as the limit of a Riemann sum,
> $$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \, \Delta x,$$
> where the interval $[a, b]$ is partitioned into $n$ strips of width $\Delta x = (b-a)/n$ and $x_i^*$ is any sample point in the $i$-th strip. **First** the student sums up infinitely many infinitesimals (the geometric face); **only then** does the FTC arrive to show that this sum equals $F(b) - F(a)$.
>
> AP students therefore meet left-, right-, midpoint- and trapezoidal-Riemann sums *before* they know any antiderivatives. This builds the "integration = summation" intuition into their bones. If your student is switching between Cambridge and AP, this shift in pedagogy is the main thing to flag. Same mathematics, opposite order of reveal.

### Beyond high school — University

- The formal definition of $\int_a^b f(x) \, dx$ **is** the Riemann integral — a rigorous version of the AP approach above, built from limits of partition sums and formalised by Riemann in the 1850s. Undergraduate analysis spends a chapter or two making the "limit of sums" precise via upper/lower Darboux sums and proving which functions are Riemann-integrable.
- For pathological functions (nowhere-continuous indicator functions, for example) the **Lebesgue integral** generalises Riemann's construction to a far wider class — the cornerstone of modern probability, Fourier analysis, and PDE.
- The Fundamental Theorem of Calculus generalises to multiple variables (Green's, Stokes's, and Divergence theorems), and to complex analysis (Cauchy's Integral Theorem).

---

## Connections

- **Parent:** [[Differentiation]] — integration is its inverse.
- **Prerequisite:** [[Power Rule]] — integration of $x^n$ is the reverse.
- **Prerequisite:** [[Exponential Function]] — $e^x$ is its own antiderivative.
- **Prerequisite:** [[Logarithms]] — $\int \tfrac{1}{x} dx = \ln|x| + C$.
- **Prerequisite:** [[Trigonometric Functions]] — standard trig integrals.
- **Prerequisite:** [[Chain Rule]] — the linear-inside rule is chain rule in reverse.
- **Extension:** [[Integration by Substitution]] — the general chain-rule reversal technique.
- **Extension:** [[Integration by Parts]] — the product rule in reverse.
- **Application:** [[Kinematics Calculus]] — $s = \int v \, dt$, $v = \int a \, dt$.
- **Application:** [[Differential Equations]] — first-order separable equations solved by integration.
- **Physics bridge — reserved:** [[Work and Energy]] — $W = \int F \, dx$; kinetic energy theorem.
- **Physics bridge — reserved:** [[Impulse and Momentum]] — $\Delta p = \int F \, dt$.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\displaystyle \int f(x) \, dx$ | `\int f(x) \, dx` | Indefinite integral. Thin space `\,` before $dx$. |
| $\displaystyle \int_a^b f(x) \, dx$ | `\int_a^b f(x) \, dx` | Definite integral. |
| $\bigl[F(x)\bigr]_a^b$ | `\bigl[F(x)\bigr]_a^b` | Evaluation notation for FTC. |
| $\lvert x \rvert$ | `\lvert x \rvert` | Absolute value inside tables (pipes break rows). |
| $+ C$ | `+ C` | Constant of integration — never forget. |
| $\dfrac{1}{ax+b}$ | `\dfrac{1}{ax+b}` | Display-size fraction. |
