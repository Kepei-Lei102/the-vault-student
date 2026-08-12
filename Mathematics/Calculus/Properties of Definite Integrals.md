---
chinese: 定积分的性质 (dìngjīfēn de xìngzhì)
prerequisites:
  - "[[Integration]]"
  - "[[Mean Value Theorem]]"
leads_to:
  - "[[Fundamental Theorem of Calculus]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/AP-Calculus-BC-6-6
  - type/deep
  - type/theorem
  - type/proof
  - notation/definite-integral
  - misconception/swapping-limits
  - misconception/comparison-without-bounds
---

# Properties of Definite Integrals 定积分的性质

## Definition

This card collects the **algebraic and order properties** of the definite integral — the rules that let you split, combine, scale, sign-flip, and bound integrals without computing them. They are the elementary corollaries of the integral's definition as a limit of Riemann sums, and every one of them is used routinely in [[Fundamental Theorem of Calculus]] proofs and in computations downstream.

The seven properties below are AP Calculus Topic 6.6 ("Applying Properties of Definite Integrals") in full.

### 中文锚点

定积分的性质 = 不需要算出具体值就可以使用的代数和不等式规则。线性、可加性、上下限交换变号、空区间为零、比较不等式、平均值定理 — 它们都是黎曼和定义的直接推论，证明只需要把性质翻译到求和上，然后取极限。这些性质在 FTC 的推导和绝大多数定积分计算中反复出现。

---

## 1. Linearity

For continuous (or Riemann-integrable) $f, g$ and constants $\alpha, \beta$:

$$
\int_a^b \bigl[\alpha f(x) + \beta g(x)\bigr]\, dx = \alpha\int_a^b f(x)\, dx + \beta\int_a^b g(x)\, dx.
$$

In words: integration commutes with constant multiples and is distributive over addition.

**Proof.** Take a Riemann sum for the left-hand side:

$$
\sum_{i=1}^{n}\bigl[\alpha f(x_i^*) + \beta g(x_i^*)\bigr]\Delta x = \alpha\sum_{i=1}^n f(x_i^*)\Delta x + \beta\sum_{i=1}^n g(x_i^*)\Delta x,
$$

by ordinary algebraic distribution. Take the limit $n \to \infty$ on both sides — the right-hand side becomes $\alpha\int_a^b f + \beta\int_a^b g$. $\;\boxed{}$

---

## 2. Additivity over intervals

For continuous $f$ and any $c \in [a, b]$:

$$
\int_a^b f(x)\, dx = \int_a^c f(x)\, dx + \int_c^b f(x)\, dx.
$$

In words: chopping an interval into two pieces splits the integral into two pieces. The relation extends to any number of break points $c_1 < c_2 < \cdots$ by induction.

**Proof.** Choose a Riemann partition that includes $c$ as one of the partition points (we can do this without loss of generality because the limit defining the integral is independent of the partition once mesh size $\to 0$). Then the Riemann sum for $\int_a^b$ splits naturally as the sum from $a$ to $c$ plus the sum from $c$ to $b$:

$$
\sum_{i: x_i \le c} f(x_i^*)\Delta x_i + \sum_{i: x_i > c} f(x_i^*)\Delta x_i.
$$

Taking the limit $\text{mesh} \to 0$, the two pieces converge to $\int_a^c f$ and $\int_c^b f$ respectively. $\;\boxed{}$

The additivity property is what's used inside the [[Fundamental Theorem of Calculus]] FTC1 derivation: $\int_a^{x+h} = \int_a^x + \int_x^{x+h}$ is *exactly* this property, applied with $b = x+h$ and the inner break at $c = x$.

> [!tip] Additivity also works when $c$ is OUTSIDE $[a, b]$
> The extended form $\int_a^b f = \int_a^c f + \int_c^b f$ holds for any real $c$, not just $c \in [a, b]$ — even when $c > b$ or $c < a$. The "extra" piece on the wrong side cancels correctly by the sign-flip property below. Powerful when manipulating piecewise integrals or shifting limits algebraically.

---

## 3. Sign-flip when reversing the limits

$$
\int_a^b f(x)\, dx = -\int_b^a f(x)\, dx.
$$

This is a *convention*, but a forced one — it is the *only* convention that keeps additivity (Property 2) algebraically consistent across all real $a, b, c$. (Setting $c = a$ in additivity gives $\int_a^b f = \int_a^a f + \int_a^b f$, which forces $\int_a^a f = 0$. Setting $b = a$ in additivity gives $0 = \int_a^c f + \int_c^a f$, which forces the sign-flip.)

In Riemann-sum terms: reversing the integration direction reverses the sign of every $\Delta x = (b - a)/n$, and the limit picks up the overall minus sign.

---

## 4. Zero-length interval

$$
\int_a^a f(x)\, dx = 0.
$$

Forced by Property 3 (set $b = a$ in the sign-flip: $\int_a^a = -\int_a^a$, so $\int_a^a = 0$).

---

## 5. Comparison theorem

If $f(x) \le g(x)$ for all $x \in [a, b]$, then

$$
\int_a^b f(x)\, dx \le \int_a^b g(x)\, dx.
$$

Inequality between functions becomes inequality between their definite integrals, *provided you integrate in the positive direction* ($a < b$).

**Proof.** Apply Riemann sums: $f(x_i^*) \le g(x_i^*)$ for each sample point, so $\sum f(x_i^*)\Delta x \le \sum g(x_i^*)\Delta x$ (because $\Delta x > 0$ when $a < b$). Take the limit. $\;\boxed{}$

**Special case (estimation).** If $m \le f(x) \le M$ on $[a, b]$, integrating over $[a, b]$:

$$
m(b - a) \le \int_a^b f(x)\, dx \le M(b - a).
$$

This is the *bound* used in the average-value argument that proves the Mean Value Theorem for integrals.

> [!tip] The direction of integration matters
> If $a > b$ and $f \le g$ on $[b, a]$, then $\int_a^b f \ge \int_a^b g$ (inequality flips!) — because the sign-flip in Property 3 reverses the direction of inequality. **Always integrate from smaller to larger** when applying the comparison theorem in the standard form, and only flip if you've explicitly invoked Property 3.

---

## 6. Mean Value Theorem for Integrals

If $f$ is continuous on $[a, b]$, there exists $c \in [a, b]$ with

$$
\int_a^b f(x)\, dx = f(c)(b - a).
$$

The integrand attains its **average value** $\bar f = \dfrac{1}{b - a}\int_a^b f$ at some point $c$ inside the interval.

For the proof, see [[Mean Value Theorem]]. The key inputs are the comparison theorem (Property 5) and the Intermediate Value Theorem applied to the continuous integrand.

---

## 7. Average value of a function

The **average value** of $f$ on $[a, b]$ is defined by

$$
\bar f = \frac{1}{b - a}\int_a^b f(x)\, dx.
$$

It is the height of the rectangle on $[a, b]$ that has the same area as $\int_a^b f$. By Property 6 (MVT for integrals), $\bar f = f(c)$ for some $c \in [a, b]$ — *the function actually achieves its average value somewhere*.

**Worked example.** Average value of $f(x) = x^2$ on $[0, 3]$:

$$
\bar f = \frac{1}{3}\int_0^3 x^2\, dx = \frac{1}{3}\cdot\frac{27}{3} = 3.
$$

By the MVT for integrals, there's some $c \in [0, 3]$ with $c^2 = 3$, namely $c = \sqrt{3} \approx 1.73$. This is concrete: at $x = \sqrt 3$, the parabola's height is exactly its average over the interval.

---

## A Worked Example Combining Multiple Properties

Given $\int_0^4 f(x)\, dx = 10$, $\int_0^4 g(x)\, dx = 6$, and $\int_2^4 f(x)\, dx = 7$. Find $\int_2^0 \bigl[3f(x) - 2g(x)\bigr]\, dx$.

**Step 1** — additivity: $\int_0^4 f = \int_0^2 f + \int_2^4 f$, so $\int_0^2 f = 10 - 7 = 3$.

**Step 2** — sign-flip: $\int_2^0 \cdot = -\int_0^2 \cdot$.

**Step 3** — linearity: $\int_0^2 \bigl[3f - 2g\bigr] = 3\int_0^2 f - 2\int_0^2 g$.

We have $\int_0^2 f = 3$. We don't have $\int_0^2 g$ separately — only $\int_0^4 g = 6$. (The problem as stated is under-determined for the $g$ piece. *In a real exam*, you'd be told $\int_0^2 g$ separately, or asked for an answer that depends on it.) To finish: assume $\int_0^2 g = 4$ (say). Then $\int_0^2 [3f - 2g] = 9 - 8 = 1$, and the requested integral $\int_2^0 [3f - 2g] = -1$.

The general pattern: every property is a one-line manipulation; chaining them is the whole skill. AP-style "given some integrals, find another" problems are *exactly* this kind of chaining.

---

## Common Mistakes

1. **Swapping limits without flipping the sign.** $\int_b^a f \ne \int_a^b f$ — they differ by a sign. The bookkeeping is forced: write the swap and the minus sign in the same step.
2. **Comparison theorem applied to integrals over reversed directions.** $f \le g$ on $[a, b]$ implies $\int_a^b f \le \int_a^b g$ *only if $a < b$*. If you've reversed the limits to $\int_b^a$, the inequality reverses too.
3. **Linearity over multiplied integrands.** $\int_a^b f(x)g(x)\, dx \ne \int_a^b f(x)\, dx \cdot \int_a^b g(x)\, dx$ in general. Linearity covers *constants × functions*, not function × function. (For the latter, you need [[Integration by Parts]].)
4. **Additivity with the wrong break point.** $\int_a^b = \int_a^c + \int_c^b$ holds for *any* $c$, but it's most useful when $c$ is *between* $a$ and $b$ — otherwise one of the pieces is negative-direction and you have to flip its sign.
5. **Forgetting that "average value" needs continuity.** The MVT-for-integrals form ($\bar f = f(c)$ for some $c$) requires $f$ continuous on $[a, b]$. A function with a jump can have an average value that *no point of $f$ ever attains*.

---

## Exam Notes

### AP Calculus AB / BC — Topic 6.6

Examined directly. Common prompt: *"Given $\int_0^5 f(x)\, dx = 12$ and $\int_0^3 f(x)\, dx = 7$, find $\int_3^5 f(x)\, dx$."* Pure additivity; one-line answer ($12 - 7 = 5$). More advanced prompts mix linearity with sign-flip. The *average value* and *MVT for integrals* appear at least once per BC exam.

### IB AA HL & A-Level Further

Stated and applied. Average-value problems are common; comparison-theorem-as-bound is occasionally tested. MVT for integrals is in the curriculum at HL but rarely at SL.

### Cambridge 0606 / 9709

Linearity, additivity, and sign-flip are *used implicitly* — students apply them without naming them. Average value is not on either syllabus. The "bounded above and below" estimation form (Property 5 special case) shows up rarely.

---

## Connections

- **Prerequisite:** [[Integration]] — Riemann-sum definition is what every property reduces to
- **Prerequisite:** [[Mean Value Theorem]] — supplies the $c$ in Property 6
- **Used by:** [[Fundamental Theorem of Calculus]] — additivity (Property 2) is the splitting step in the FTC1 proof; the comparison theorem bounds the inner integral in the FTC1 squeeze
- **Used by:** [[Integration by Substitution]], [[Integration by Parts]] — both rely on linearity and additivity to manipulate definite integrals
- **Application:** *probability* — the expected value of a continuous random variable is an integral; properties 1, 2, 6 supply the algebra (linearity of expectation, average-value interpretation)
- **Application:** *physics* — average force, average velocity, average power are all average values of integrands; Property 6 says these averages are *attained* somewhere
- **Beyond high school:** Lebesgue integration extends every property here to a much larger class of functions (including discontinuous ones); the *Cauchy–Schwarz inequality* $\bigl(\int fg\bigr)^2 \le \int f^2 \cdot \int g^2$ is the direct analogue of the dot product inequality and lives in the same property family

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\int_a^b f(x)\, dx$ | `\int_a^b f(x)\, dx` | definite integral |
| $\bar f$ | `\bar f` | average value |
| $\sum_{i=1}^n f(x_i^*)\Delta x$ | `\sum_{i=1}^n f(x_i^*)\Delta x` | Riemann sum |
| $\le$ | `\le` | comparison theorem |
| $\boxed{}$ | `\boxed{}` | end-of-proof marker |
