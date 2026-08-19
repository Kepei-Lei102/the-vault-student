---
chinese: 二项级数 (èrxiàng jíshù)
prerequisites:
  - "[[Binomial Theorem]]"
  - "[[Partial Fractions]]"
  - "[[Differentiation Rules]]"
  - "[[Power Rule]]"
  - "[[Factorial Notation]]"
  - "[[Sequences]]"
  - "[[Polynomial Division]]"
leads_to:
  - "[[Differential Equations]]"
  - "[[Maclaurin Series]]"
  - "[[Probability Generating Functions]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/A-Level
  - curriculum/Edexcel-IAL
  - curriculum/OxAQA-9660
  - curriculum/IB-AA
  - curriculum/AP-Calculus-BC
  - syllabus/9709-3-1
  - type/theorem
  - type/technique
  - notation/binomial-coefficient
  - notation/power-series
  - misconception/forgetting-convergence-condition
  - misconception/integer-vs-noninteger-treatment
  - misconception/inside-coefficient-sign-error
  - misconception/early-truncation
---

# Binomial Series 二项级数

## Definition

### Formal

For any real number $n$ and any real $x$ with $\lvert x \rvert < 1$:

$$\boxed{\;(1 + x)^n = 1 + nx + \dfrac{n(n-1)}{2!}\,x^2 + \dfrac{n(n-1)(n-2)}{3!}\,x^3 + \dfrac{n(n-1)(n-2)(n-3)}{4!}\,x^4 + \ldots\;}$$

The $k$-th term is

$$\binom{n}{k}\,x^k \;=\; \dfrac{n(n-1)(n-2)\cdots(n - k + 1)}{k!}\,x^k,$$

where $\binom{n}{k}$ is the **generalized binomial coefficient** — defined for any real $n$ (not just positive integers) by the above falling-factorial-over-$k!$ formula.

**Convergence:** the series converges to $(1 + x)^n$ on the open interval $\lvert x \rvert < 1$. At $\lvert x \rvert = 1$ the behaviour depends on $n$; outside $\lvert x \rvert > 1$ the series diverges.

### Intuitive

You already know the **finite** binomial theorem from [[Binomial Theorem|IGCSE]]: for positive integer $n$,

$$(1 + x)^n = 1 + nx + \binom{n}{2}x^2 + \ldots + \binom{n}{n}x^n.$$

The series *terminates* at the $x^n$ term, because $\binom{n}{n+1}$ involves a factor of $(n - n) = 0$, which kills every subsequent term.

The **binomial series** at A-Level extends this to **non-integer $n$**. Replace $n$ with $\tfrac{1}{2}$, or $-1$, or $-\tfrac{2}{3}$, or any real number: the falling-factorial $n(n-1)(n-2)\cdots$ *never reaches zero* because $n$ isn't a positive integer. The series doesn't terminate — it goes on forever. So instead of a finite expansion, you get an **infinite power series**.

That sounds like a problem ("how do you compute an infinite sum?"), but in practice it isn't: provided $\lvert x \rvert < 1$, the terms shrink fast enough that the first 3–5 give an excellent approximation. **You truncate.** A 4-term expansion of $\sqrt{1.04} = (1 + 0.04)^{1/2}$ gives $1.019804\ldots$ accurate to six decimal places.

The headline applications at 9709 P3 §3.1:

1. **Numerical approximation** of $\sqrt{\,}$, $\sqrt[3]{\,}$, $(\text{something})^{\text{fraction}}$, etc.
2. **Expanding a [[Partial Fractions|partial-fraction]] decomposition** term by term — the most common §3.1 exam question shape *"express $\dfrac{P(x)}{D(x)}$ in partial fractions, then expand each as a series up to $x^3$"*.
3. **Integrating functions with no closed-form antiderivative** by expanding, integrating term by term, and truncating. (Beyond P3 strictly, but standard at IB AA HL.)

### 中文锚点

**二项级数**（èrxiàng jíshù）：把熟悉的二项展开式 $(1+x)^n$ 从**正整数 $n$ 推广到任意实数 $n$**（包括分数、负数、无理数）。

IGCSE 学的 [[Binomial Theorem|二项定理]]：$n$ 为正整数时展开有 $n+1$ 项，**有限**。如 $(1+x)^3 = 1 + 3x + 3x^2 + x^3$。

A-Level 推广：$n$ 不再要求是正整数。展开式变成**无穷级数**：

$$(1+x)^n = 1 + nx + \dfrac{n(n-1)}{2!}x^2 + \dfrac{n(n-1)(n-2)}{3!}x^3 + \ldots$$

但要求 $\lvert x \rvert < 1$（**收敛条件**）。这个条件是新的、必须记住的。如果 $\lvert x \rvert \geq 1$，级数发散，公式失效。

**核心用法**（9709 P3 §3.1）：
1. 数值近似（$\sqrt{1.04}$, $\sqrt[3]{8.1}$ 等）
2. 配合[[Partial Fractions|部分分式]]做有理函数的级数展开
3. (IB HL) 用级数项-逐项积分处理"积不出来"的函数

---

## §1 The Bridge from $n$-Integer to $n$-Real

The IGCSE [[Binomial Theorem|binomial theorem]] for positive integer $n$ is:

$$(1 + x)^n = \sum_{k=0}^{n} \binom{n}{k} x^k = 1 + nx + \binom{n}{2}x^2 + \ldots + x^n.$$

with $\binom{n}{k} = \dfrac{n!}{k!(n-k)!}$ — the standard combinatorial binomial coefficient.

**Why does the series terminate at $k = n$?** Because $\binom{n}{n+1} = \dfrac{n!}{(n+1)!(-1)!}$ involves $(-1)!$, which is undefined — or, looking at the falling-factorial form,

$$\binom{n}{n+1} = \dfrac{n(n-1)(n-2)\cdots(n-n)(n-(n+1)+1)}{(n+1)!} = \dfrac{\cdots \cdot 0 \cdot \cdots}{(n+1)!} = 0.$$

The factor of $(n - n) = 0$ kills every term from $k = n+1$ onward. The series stops.

### When $n$ isn't a positive integer, the zero never appears

Now substitute $n = \tfrac{1}{2}$ (or any non-positive-integer real number). The falling factorial becomes:

$$\dfrac{1}{2} \cdot \left(\dfrac{1}{2} - 1\right) \cdot \left(\dfrac{1}{2} - 2\right) \cdot \left(\dfrac{1}{2} - 3\right) \cdot \ldots = \dfrac{1}{2} \cdot \left(-\dfrac{1}{2}\right) \cdot \left(-\dfrac{3}{2}\right) \cdot \left(-\dfrac{5}{2}\right) \cdot \ldots$$

Each factor is non-zero. The series **doesn't terminate**. We've gone from a finite polynomial to an infinite power series, and the question becomes: *does it converge to anything meaningful?*

The answer is yes, with a condition: **$\lvert x \rvert < 1$**. We'll see why in §4.

> [!info] Two algebraic regimes, one formula
> The same expression $(1 + x)^n = \sum_{k=0}^\infty \binom{n}{k} x^k$ now describes both:
> - **Positive-integer $n$**: the sum is finite (terminating at $k = n$), no convergence condition needed — works for any $x \in \mathbb{R}$.
> - **Non-integer real $n$**: the sum is infinite, converges only for $\lvert x \rvert < 1$.
>
> *That's why the A-Level form is called the "binomial series" rather than the "binomial theorem" — to distinguish the infinite-sum regime from the IGCSE finite regime.*

---

## §2 The Generalized Binomial Coefficient

For any real $n$ and non-negative integer $k$:

$$\boxed{\;\binom{n}{k} = \dfrac{n(n-1)(n-2)\cdots(n - k + 1)}{k!}\;}$$

The numerator is a **falling factorial**: $k$ factors starting at $n$ and decreasing by $1$. The denominator is the usual $k! = 1 \cdot 2 \cdot 3 \cdots k$.

**By convention** $\binom{n}{0} = 1$ for any $n$ (the "empty product" in the numerator equals $1$).

### Examples

$$\binom{1/2}{2} = \dfrac{\frac{1}{2}\cdot(-\frac{1}{2})}{2!} = \dfrac{-1/4}{2} = -\dfrac{1}{8}.$$

$$\binom{-1}{3} = \dfrac{(-1)(-2)(-3)}{3!} = \dfrac{-6}{6} = -1.$$

$$\binom{-1}{k} = \dfrac{(-1)(-2)(-3)\cdots(-k)}{k!} = (-1)^k \cdot \dfrac{k!}{k!} = (-1)^k.$$

The last one is worth memorising: **$\binom{-1}{k} = (-1)^k$**. It gives $(1 + x)^{-1} = 1 - x + x^2 - x^3 + x^4 - \ldots$, the geometric series.

### Sanity check — positive integer $n$ matches the IGCSE form

For $n = 4$, $k = 2$: $\binom{4}{2}_{\text{generalized}} = \dfrac{4 \cdot 3}{2!} = 6$, which equals the standard $\dfrac{4!}{2!\,2!} = 6$. ✓

For $n = 4$, $k = 5$: $\binom{4}{5} = \dfrac{4 \cdot 3 \cdot 2 \cdot 1 \cdot 0}{5!} = 0$. The factor of $0$ (when $k - 1 \geq n$) is what makes the series terminate for integer $n$. ✓

> [!tip] Mental computation shortcut
> When computing $\binom{n}{k}$ for non-integer $n$, write the $k$ numerator factors explicitly *with their signs*, then simplify. The pattern $n, n-1, n-2, \ldots, n-k+1$ has $k$ factors total — count them.
>
> For $n = -\tfrac{2}{3}$, $k = 3$: $\binom{-2/3}{3} = \dfrac{(-2/3)(-5/3)(-8/3)}{3!} = \dfrac{-80/27}{6} = -\dfrac{40}{81}$. *(Three negative factors → negative result; three thirds in numerator → denominator $27$; multiply across.)*

---

## §3 Derivation — Maclaurin Series of $(1 + x)^n$

Where does the binomial series come from? It's the [[Differentiation|Maclaurin]] expansion of $f(x) = (1 + x)^n$ around $x = 0$.

The Maclaurin series of a function $f$ that is infinitely differentiable at $x = 0$ is:

$$f(x) = f(0) + f'(0)\,x + \dfrac{f''(0)}{2!}\,x^2 + \dfrac{f'''(0)}{3!}\,x^3 + \ldots = \sum_{k=0}^\infty \dfrac{f^{(k)}(0)}{k!}\,x^k.$$

> [!info] Maclaurin is Taylor centred at zero
> A **Taylor series** of $f$ around a point $a$ is the more general expansion
> $$f(x) = \sum_{k=0}^\infty \dfrac{f^{(k)}(a)}{k!}\,(x - a)^k.$$
> Setting $a = 0$ recovers the Maclaurin form above. So "Maclaurin" is a special case of "Taylor" — the special case where the expansion point is the origin. Some textbooks use only the word "Taylor"; the British / Commonwealth tradition (and 9709 + IB AA) keeps the separate name "Maclaurin" for the $a = 0$ case as a useful shorthand, since most exam-level expansions are around zero. *Throughout this card, when we say "Maclaurin" you can read "Taylor with $a = 0$" — they're the same operation.*

For $f(x) = (1 + x)^n$:

$$f(x) = (1+x)^n \qquad f(0) = 1$$
$$f'(x) = n(1+x)^{n-1} \qquad f'(0) = n$$
$$f''(x) = n(n-1)(1+x)^{n-2} \qquad f''(0) = n(n-1)$$
$$f'''(x) = n(n-1)(n-2)(1+x)^{n-3} \qquad f'''(0) = n(n-1)(n-2)$$
$$\vdots$$
$$f^{(k)}(x) = n(n-1)(n-2)\cdots(n - k + 1)\,(1+x)^{n-k} \qquad f^{(k)}(0) = n(n-1)\cdots(n-k+1).$$

Substituting into the Maclaurin formula:

$$(1 + x)^n = \sum_{k=0}^\infty \dfrac{n(n-1)(n-2)\cdots(n - k + 1)}{k!}\,x^k = \sum_{k=0}^\infty \binom{n}{k}\,x^k.$$

That's the binomial series. The derivation works **for any real $n$** — positive integer, negative integer, fraction, irrational — because the differentiation rule $\frac{d}{dx}(1+x)^n = n(1+x)^{n-1}$ holds for any $n \in \mathbb{R}$ (Power Rule). The only thing that distinguishes integer from non-integer $n$ is whether the $f^{(k)}(0)$ sequence eventually becomes zero (integer case) or never does (non-integer case).

Historically this derivation runs backwards. Newton had the series in **1665**, seventy-seven years before Maclaurin's framework existed to derive it from — he reached it by interpolating the coefficient pattern instead, and the full account of how is at the end of this card.

---

## §4 Convergence — Why $\lvert x \rvert < 1$ is Required

For non-integer $n$, the binomial series is an infinite sum. It converges to $(1+x)^n$ if and only if $\lvert x \rvert < 1$ (with boundary behavior depending on $n$).

### The ratio test

The standard convergence test for a power series $\sum a_k x^k$ is the **ratio test**: the series converges if $\lim_{k \to \infty} \left\lvert \dfrac{a_{k+1} x^{k+1}}{a_k x^k} \right\rvert < 1$.

For the binomial series, $a_k = \binom{n}{k}$, so

$$\dfrac{a_{k+1}}{a_k} = \dfrac{\binom{n}{k+1}}{\binom{n}{k}} = \dfrac{n - k}{k + 1}.$$

(Each step adds one more falling-factorial factor in the numerator and one more $k+1$ in the denominator.) Therefore

$$\left\lvert \dfrac{a_{k+1} x^{k+1}}{a_k x^k} \right\rvert = \left\lvert \dfrac{n - k}{k + 1} \right\rvert \cdot \lvert x \rvert \xrightarrow{k \to \infty} \lvert x \rvert.$$

The series converges if this limit is $< 1$, i.e., if **$\lvert x \rvert < 1$**. ✓

### Intuition — terms must shrink

In the binomial series, the $k$-th term is $\binom{n}{k} x^k$. The coefficient $\binom{n}{k}$ grows polynomially with $k$ (for fixed $n$), while $\lvert x \rvert^k$ shrinks exponentially when $\lvert x \rvert < 1$. *Exponential decay beats polynomial growth.* The terms shrink to zero, and the sum converges.

When $\lvert x \rvert \geq 1$, $\lvert x \rvert^k$ doesn't shrink, and the polynomial growth of $\binom{n}{k}$ takes over. Terms grow; the sum diverges.

### Worked check — $(1 + 0.5)^{1/2}$ vs $(1 + 2)^{1/2}$

For $x = 0.5$ ($\lvert x \rvert < 1$): the series should converge to $\sqrt{1.5} \approx 1.2247$. First few terms:
$1 + 0.5 \cdot 0.5 = 1.25$; add $-0.125 \cdot 0.25 = -0.03125$ → $1.21875$; add $0.0625 \cdot 0.125 = 0.0078125$ → $1.22656$. Converging to $\sqrt{1.5}$. ✓

For $x = 2$ ($\lvert x \rvert \geq 1$): the "series" should give $\sqrt{3} \approx 1.732$ but instead the terms grow:
$1 + 0.5 \cdot 2 = 2$; add $-0.125 \cdot 4 = -0.5$ → $1.5$; add $0.0625 \cdot 8 = 0.5$ → $2$; add $-0.0390625 \cdot 16 = -0.625$ → $1.375$… The partial sums oscillate without settling. The series **does not converge** to $\sqrt{3}$. *You must rewrite the expression to bring it into the $\lvert x \rvert < 1$ regime before expanding.*

> [!warning] Always check the convergence condition first
> Before writing down a binomial series, **identify what's in the "$x$" slot** and check $\lvert x \rvert < 1$. The "$x$" slot is the entire thing being raised to the power — including coefficients. For $(1 + 3x)^{1/2}$, the condition is $\lvert 3x \rvert < 1$, i.e., $\lvert x \rvert < \tfrac{1}{3}$. For $(2 + x)^{1/2}$, you must first factor out the $2$: $(2 + x)^{1/2} = 2^{1/2}\,(1 + x/2)^{1/2}$, and now expand in $u = x/2$ requiring $\lvert x \rvert < 2$.
>
> Missing the condition or applying it to the wrong variable is the single most common P3 §3.1 error.

---

## §5 Worked Example — $(1 + x)^{1/2}$

Find the first four terms of the expansion of $(1 + x)^{1/2}$ in ascending powers of $x$, and state the values of $x$ for which the expansion is valid.

**Step 1 — identify $n$:** $n = \tfrac{1}{2}$.

**Step 2 — compute the generalized binomial coefficients up to $k = 3$:**

$$\binom{1/2}{0} = 1, \qquad \binom{1/2}{1} = \dfrac{1}{2},$$
$$\binom{1/2}{2} = \dfrac{(1/2)(1/2 - 1)}{2!} = \dfrac{(1/2)(-1/2)}{2} = -\dfrac{1}{8},$$
$$\binom{1/2}{3} = \dfrac{(1/2)(-1/2)(-3/2)}{3!} = \dfrac{3/8}{6} = \dfrac{1}{16}.$$

**Step 3 — assemble the expansion:**

$$(1 + x)^{1/2} = 1 + \dfrac{1}{2}\,x - \dfrac{1}{8}\,x^2 + \dfrac{1}{16}\,x^3 + \ldots$$

**Step 4 — convergence condition:** $\lvert x \rvert < 1$.

### Sanity check at $x = 0.04$

$\sqrt{1.04}$ true value: $1.019803902\ldots$. Series: $1 + 0.5(0.04) - 0.125(0.04)^2 + 0.0625(0.04)^3 = 1 + 0.02 - 0.0002 + 0.000004 = 1.019804$. Matches to 6 decimal places after only 4 terms. ✓

That's the practical power of the binomial series — *fast-converging numerical approximation for small $x$*.

---

## §6 Worked Example — $(1 - 2x)^{-3}$

Find the first four terms of the expansion of $\dfrac{1}{(1 - 2x)^3}$ in ascending powers of $x$, and state the values of $x$ for which the expansion is valid.

**Step 1 — rewrite as $(1 + u)^n$:** $\dfrac{1}{(1-2x)^3} = (1 - 2x)^{-3} = (1 + (-2x))^{-3}$. So $u = -2x$ and $n = -3$.

**Step 2 — compute coefficients in $u$:**

$$\binom{-3}{0} = 1, \qquad \binom{-3}{1} = -3,$$
$$\binom{-3}{2} = \dfrac{(-3)(-4)}{2!} = \dfrac{12}{2} = 6,$$
$$\binom{-3}{3} = \dfrac{(-3)(-4)(-5)}{3!} = \dfrac{-60}{6} = -10.$$

**Step 3 — assemble in $u$:**

$$(1 + u)^{-3} = 1 + (-3)u + 6u^2 + (-10)u^3 + \ldots = 1 - 3u + 6u^2 - 10u^3 + \ldots$$

**Step 4 — substitute back $u = -2x$:**

$$(1 - 2x)^{-3} = 1 - 3(-2x) + 6(-2x)^2 - 10(-2x)^3 + \ldots = 1 + 6x + 24x^2 + 80x^3 + \ldots$$

**Step 5 — convergence:** $\lvert u \rvert < 1 \Leftrightarrow \lvert -2x \rvert < 1 \Leftrightarrow \lvert x \rvert < \tfrac{1}{2}$.

> [!warning] The sign trap on negative-inside coefficients
> When the inside coefficient is negative (like the $-2$ in $-2x$), keeping track of signs in the $(-2x)^k$ substitution is the single biggest source of arithmetic errors. $(-2x)^2 = +4x^2$, but $(-2x)^3 = -8x^3$. Always expand the powers fully and carry the signs.
>
> *Fix:* substitute $u = -2x$ explicitly as a first step, work the expansion in $u$ alone, then re-substitute at the end. Don't try to expand "in $x$" directly — that's how signs get lost. (See misconception 3.)

---

## §7 Worked Example — Partial Fractions + Binomial Series Together

*This is the canonical 9709 P3 §3.1 question.* The setup is always the same: a rational function whose denominator factors, expand it as a power series up to some specified term.

**Problem.** Express $\dfrac{1}{(1 - 2x)(1 + x)}$ in partial fractions, and hence find the first four terms of its expansion in ascending powers of $x$.

**Step 1 — Partial-fraction decomposition.** (See [[Partial Fractions]] §4 for the cover-up method.)

$$\dfrac{1}{(1 - 2x)(1 + x)} = \dfrac{A}{1 - 2x} + \dfrac{B}{1 + x}.$$

Cover-up: $A = \dfrac{1}{1 + 1/2} = \dfrac{2}{3}$ (substitute $x = 1/2$ into $\dfrac{1}{1+x}$); $B = \dfrac{1}{1 - 2(-1)} = \dfrac{1}{3}$ (substitute $x = -1$ into $\dfrac{1}{1-2x}$).

$$\dfrac{1}{(1 - 2x)(1 + x)} = \dfrac{2/3}{1 - 2x} + \dfrac{1/3}{1 + x}.$$

**Step 2 — Expand each piece via binomial series.**

Piece 1: $\dfrac{2/3}{1 - 2x} = \dfrac{2}{3}(1 - 2x)^{-1} = \dfrac{2}{3}\bigl[1 + 2x + 4x^2 + 8x^3 + \ldots\bigr] = \dfrac{2}{3} + \dfrac{4}{3}x + \dfrac{8}{3}x^2 + \dfrac{16}{3}x^3 + \ldots$

*(Used $(1 - 2x)^{-1} = (1 + (-2x))^{-1} = \sum (-1)^k(-2x)^k = \sum 2^k x^k$, the geometric series with ratio $2x$.)*

Piece 2: $\dfrac{1/3}{1 + x} = \dfrac{1}{3}(1 + x)^{-1} = \dfrac{1}{3}\bigl[1 - x + x^2 - x^3 + \ldots\bigr] = \dfrac{1}{3} - \dfrac{1}{3}x + \dfrac{1}{3}x^2 - \dfrac{1}{3}x^3 + \ldots$

**Step 3 — Add the two series term by term.**

| Power | Piece 1 | Piece 2 | Sum |
|---|---|---|---|
| $x^0$ | $2/3$ | $1/3$ | $1$ |
| $x^1$ | $4/3$ | $-1/3$ | $1$ |
| $x^2$ | $8/3$ | $1/3$ | $3$ |
| $x^3$ | $16/3$ | $-1/3$ | $5$ |

**Answer.** $\dfrac{1}{(1 - 2x)(1 + x)} = 1 + x + 3x^2 + 5x^3 + \ldots$

**Step 4 — Convergence.** Piece 1 needs $\lvert 2x \rvert < 1$, i.e., $\lvert x \rvert < \tfrac{1}{2}$. Piece 2 needs $\lvert x \rvert < 1$. The *combined* expansion is valid where **both** converge: $\lvert x \rvert < \tfrac{1}{2}$.

> [!tip] Convergence interval is the intersection
> When you decompose into partial fractions and expand each piece, every piece has its own convergence interval. The combined series is valid only on the **intersection** — i.e., where every piece converges. Usually this is the tighter of the conditions; always identify which factor binds.

### Sanity check at $x = 0.1$

LHS: $\dfrac{1}{(1 - 0.2)(1 + 0.1)} = \dfrac{1}{0.8 \cdot 1.1} = \dfrac{1}{0.88} = 1.1364\ldots$

RHS (first four terms): $1 + 0.1 + 0.03 + 0.005 = 1.135$. The fifth term would be about $0.0007$, bringing us closer. Series is correct. ✓

---

## §8 Application — Numerical Approximations

The binomial series gives **fast-converging approximations** to $\sqrt{\,}$, $\sqrt[3]{\,}$, $1/(\,)$, and more, for inputs close to convenient reference points.

### Example 1 — $\sqrt{1.04}$

$\sqrt{1.04} = (1 + 0.04)^{1/2}$, with $x = 0.04$ comfortably inside $\lvert x \rvert < 1$. From §5:

$$\sqrt{1.04} \approx 1 + 0.5(0.04) - 0.125(0.04)^2 + 0.0625(0.04)^3 = 1.019804$$

Compare to true value $1.01980390\ldots$: accurate to 6 decimal places after 4 terms.

### Example 2 — $\sqrt[3]{8.1}$

Rewrite as $\sqrt[3]{8.1} = \sqrt[3]{8 \cdot 1.0125} = 2 \cdot (1 + 0.0125)^{1/3}$. Expand $(1 + x)^{1/3}$ with $x = 0.0125$:

$$\binom{1/3}{1} = \dfrac{1}{3}, \quad \binom{1/3}{2} = \dfrac{(1/3)(-2/3)}{2} = -\dfrac{1}{9}, \quad \binom{1/3}{3} = \dfrac{(1/3)(-2/3)(-5/3)}{6} = \dfrac{5}{81}.$$

$$(1 + 0.0125)^{1/3} \approx 1 + \tfrac{1}{3}(0.0125) - \tfrac{1}{9}(0.0125)^2 + \tfrac{5}{81}(0.0125)^3$$
$$= 1 + 0.004167 - 0.0000174 + \text{tiny} \approx 1.004149$$

So $\sqrt[3]{8.1} \approx 2 \times 1.004149 = 2.00830$. True value: $2.00831\ldots$. ✓ Accurate to 5 decimal places.

### Example 3 — Inverse without long division

$\dfrac{1}{1.02} = (1 + 0.02)^{-1} \approx 1 - 0.02 + 0.0004 - 0.000008 + \ldots = 0.980392$. True value: $0.980392\ldots$. ✓

### The pattern

Pre-pocket-calculator (and pre-computer), the binomial series was *the* technique for computing fractional roots, reciprocals of near-unit numbers, and small corrections to large powers. Newton used it for $\pi$. Generations of astronomers, navigators, and engineers used it daily.

---

## §9 Common Misconceptions

### 1. Forgetting the convergence condition $\lvert x \rvert < 1$

Writing an expansion and applying it at $x = 2$ or $x = 5$. The series **doesn't equal $(1+x)^n$** there — it diverges.

**Fix.** Always state the convergence condition alongside the expansion. On the exam, *"valid for $\lvert x \rvert < 1$"* is usually worth a mark. Forgetting it costs the mark.

### 2. Treating non-integer $n$ as if the series terminates

After computing 4 terms of $(1 + x)^{1/2}$, writing $(1 + x)^{1/2} = 1 + \tfrac{1}{2}x - \tfrac{1}{8}x^2 + \tfrac{1}{16}x^3$ with an equals sign — implying these are *all* the terms.

**Fix.** For non-integer $n$, the series doesn't terminate. *Write $\approx$ or use "$\ldots$"*: $(1+x)^{1/2} = 1 + \tfrac{1}{2}x - \tfrac{1}{8}x^2 + \tfrac{1}{16}x^3 + \ldots$ — the dots are mandatory.

### 3. Sign errors on negative-coefficient inside

Expanding $(1 - 2x)^n$ as if it were $(1 + 2x)^n$, missing the minus signs on odd-power terms.

**Fix.** *Substitute $u = -2x$ explicitly*, expand in $u$ first, then re-substitute at the end. Don't try to track signs inline through the expansion. Two extra lines of working, saves the question.

### 4. Forgetting to factor out the leading coefficient

For $(2 + x)^{1/2}$, naively writing the series with $n = 1/2$ and the "$x$" being $x$. *Wrong* — the formula requires $(1 + \text{small})^n$, not $(2 + \text{small})^n$.

**Fix.** Factor out: $(2 + x)^{1/2} = 2^{1/2}(1 + x/2)^{1/2}$. Now expand $(1 + x/2)^{1/2}$ in $u = x/2$ with $\lvert x/2 \rvert < 1 \Leftrightarrow \lvert x \rvert < 2$. Multiply through by $\sqrt{2}$ at the end.

### 5. Stopping the expansion too early

The exam says "up to and including the term in $x^3$." A student writes the first three terms ($x^0, x^1, x^2$) and stops, missing the $x^3$ term.

**Fix.** *Up to and including $x^n$* means write all terms from $x^0$ through $x^n$ inclusive — i.e., **$n + 1$ terms**. Count carefully before submitting. The most-missed mark in §3.1.

### 6. Confusing the IGCSE form with the A-Level form

A student tries to apply $\binom{n}{k} = \dfrac{n!}{k!(n-k)!}$ to $n = 1/2$ — getting nonsense because $(1/2)!$ isn't elementary.

**Fix.** *Use the falling-factorial form*: $\binom{n}{k} = \dfrac{n(n-1)\cdots(n-k+1)}{k!}$. This form works for any real $n$. The factorial form only works for non-negative integers.

---

## §10 Exam Notes

### Cambridge 9709 (A-Level)

**Syllabus refs:** Paper 3 §3.1 — *algebra*. Lists "expansion of $(a + x)^n$ for any rational $n$" alongside polynomial division, partial fractions, and modulus.

**Typical question shape (5–8 marks):**
1. *Express $\dfrac{P(x)}{D(x)}$ in partial fractions.* (2–3 marks — see [[Partial Fractions]])
2. *Hence find the first $n$ terms of the expansion in ascending powers of $x$.* (3–4 marks)
3. *State the set of values of $x$ for which the expansion is valid.* (1 mark)

**Mark scheme patterns:**
- M1 for correctly identifying $n$ and the "$x$" in the $(1 + x)^n$ template.
- A1 for each correct coefficient (typically 4 terms = 4 marks).
- A1 for the convergence interval, *stated explicitly* — not implicit.

**Tip.** When the question says "up to and including the term in $x^n$", you need terms $x^0, x^1, \ldots, x^n$ — that's $n + 1$ terms total. Off-by-one is the most-missed mark.

### Edexcel IAL — Pure 4, §4.1

*"Binomial series for any rational $n$"*, with the validity condition written the IAL way: for $\lvert x \rvert < \tfrac{b}{a}$ students obtain the expansion of $(ax + b)^n$ — so factor out $b^n$ first — *and the expansion of rational functions by decomposition into partial fractions*, i.e. exactly the 9709 §7-shape above. Same marks, same off-by-one trap.

### OxAQA 9660 — Pure 2, §P2.2

*"Binomial series for any rational $n$ — expansion of $(1+x)^n$, $\lvert x \rvert < 1$"*, with the stated greatest level of difficulty $(2 + 3x)^{-2}$ — factor out $2^{-2}$ first, then expand $\left(1 + \tfrac{3x}{2}\right)^{-2}$ for $\lvert x \rvert < \tfrac23$ — and the series expansion of rational functions via partial fractions as a separate row. Identical content to 9709 P3 §3.1.

### Cambridge 0606

**Not on 0606.** The 0606 syllabus covers the [[Binomial Theorem|finite binomial theorem]] (positive-integer $n$) only. The infinite-series generalization is A-Level / 9709 P3 / IAL P4 / 9660 P2 / IB AA HL.

### IB AA HL

**Topic refs:** AA HL Topic 1 (Number and Algebra). Includes the binomial series for any real $n$, alongside the finite binomial theorem. The IB formula booklet *does not give* the generalized binomial coefficient formula explicitly; you're expected to know the falling-factorial form.

AA SL does **not** test the infinite generalization; it covers only the finite, positive-integer $n$ case.

**Typical IB HL question shape:** combines binomial series with [[Maclaurin Series]]-style power-series questions. May ask for the general term, the interval of convergence, or term-by-term integration.

### AP Calculus BC

The CED does **not** name the binomial series. What BC requires (Unit 10) is the general Taylor/Maclaurin machinery plus four series to know outright — $e^x$, $\sin x$, $\cos x$ and $\dfrac{1}{1-x}$ — and $(1+x)^n$ turns up only as a function whose Maclaurin series a student *derives* by repeated differentiation, or reaches from $\dfrac{1}{1-x}$ by substitution ($n = -1$). Where it does appear the surrounding questions are the usual BC ones: interval of convergence by the ratio test with endpoint checks, term-by-term integration, and error bounds. **AP Calculus AB** has no series unit at all.

### Where it is *not* examined

**Cambridge 9231** (its Further Pure Maclaurin work uses $e^x$, trig and log series and $(1+x)^n$ only as an example, never as its own topic), **0580**, **0606**, **IB AA SL** and **IB AI** — none set the infinite binomial series. Outside the vault's boards, UK Edexcel/AQA/OCR A2 Pure examine it in the 9709 shape.

### Beyond high school — University

The binomial series is the first non-trivial example in every undergraduate analysis or complex-analysis course of:

- A **power series with non-elementary coefficients** (the generalized binomial coefficients).
- A **convergent series whose region of convergence is bounded** (the unit disk in the complex plane, see below).
- An **analytic-function definition extended by continuation** — the formula $(1 + z)^n = \sum \binom{n}{k} z^k$ in fact extends to complex $z$ with $\lvert z \rvert < 1$ and (with care) onward, giving the complex-analytic version.

---

## Connections

- **Direct prerequisite:** [[Binomial Theorem]] — the IGCSE finite, positive-integer-$n$ version that this card generalizes. The bridge in §1 is the load-bearing one.
- **Direct prerequisite:** [[Partial Fractions]] — the headline 9709 P3 §3.1 question shape applies binomial series *to each piece of a partial-fraction decomposition*. Sections §7 of both cards interlock.
- **Direct prerequisite:** [[Differentiation Rules]] + [[Power Rule]] — used in the Maclaurin derivation of §3.
- **Direct prerequisite:** [[Factorial Notation]] — for the $k!$ in the denominator.
- **Direct prerequisite:** [[Sequences]] — the language of "first $n$ terms in ascending powers."
- **Headline application:** [[Partial Fractions]] §"Application 2 — Binomial Series Expansions" — explicitly cites this card; the cross-link is bidirectional.
- **Application:** Numerical approximation of fractional roots, reciprocals, and small corrections (§8).
- **Cashes in:** the closing item of 9709 P3 §3.1. Modulus + Polynomial Division + Partial Fractions + Binomial Series **closes §3.1 to 100%**.
- **Sibling:** [[Arithmetic and Geometric Progressions]] — geometric series $\sum r^k$ is the special case $n = -1$ via $\binom{-1}{k} = (-1)^k$, giving $(1 + x)^{-1} = 1 - x + x^2 - \ldots$ (geometric with $r = -x$).
- **Generalisation:** [[Maclaurin Series]] — the binomial series is the Maclaurin series of $(1+x)^n$, which is itself the Taylor series of $(1+x)^n$ centred at $a = 0$. Maclaurin is a special case of Taylor; the binomial series is a special case of Maclaurin. *The hierarchy goes:* **Taylor (any centre)** ⊃ **Maclaurin (centre = 0)** ⊃ **Binomial series (the specific function $(1+x)^n$)**. The derivation in §3 is a one-line corollary of the general Maclaurin formula proved in [[Maclaurin Series]].
- **Beyond syllabus:** Newton's 1665 discovery — the *first* power series in mathematical history, used by Newton to compute the first 16 digits of $\pi$.
- **For 9709 students:** [[MF19 Reference (9709)]] — the binomial-series formula **is** on the MF19 formula sheet (in a slightly compressed form). Identify it on the sheet during the exam; use the form there directly.

---

## Beyond Syllabus

### Newton's 1665 binomial series and $\pi$

The binomial series wasn't discovered as a corollary of Maclaurin's general framework — it came *first*, and the general framework came 77 years later. Newton, age 22, isolated at Woolsthorpe during the 1665 plague closure of Cambridge, was studying Wallis's *Arithmetica Infinitorum*. Wallis had given expressions for finite sums of integer powers. Newton noticed a pattern in the *coefficients* of $(1 - x^2)^n$ for $n = 0, 1, 2, 3, 4, \ldots$ — the coefficients formed Pascal's triangle.

He asked: what if $n$ isn't an integer? He **interpolated** — guessed that the coefficient $\binom{n}{k}$ for $n = 1/2$ would lie between the integer values, following the same arithmetic pattern. Specifically, he conjectured that $\binom{n}{k}$ as a function of $n$ should be the unique polynomial in $n$ of degree $k$ that agrees with the combinatorial values at non-negative integer $n$.

This forced the formula $\binom{n}{k} = \dfrac{n(n-1)\cdots(n-k+1)}{k!}$ — the only $k$-th-degree polynomial in $n$ with that property.

Newton verified the conjecture by computing $\sqrt{1 + x}$ as a series, squaring it back, and checking the result equalled $1 + x$ termwise. *He had no rigorous proof.* He had numerical agreement, which was enough.

His first application: compute $\pi$. He took the circular segment under $y = \sqrt{x - x^2} = \sqrt{x}\,(1 - x)^{1/2}$, expanded the $(1-x)^{1/2}$ factor by his new series, and integrated term by term — but only from $0$ to $\tfrac{1}{4}$, not across the whole circle. Adding the triangle that completes the sector recovers $\pi$.

**The short interval is the whole trick, and it is §4's convergence lesson two centuries early.** Near $x = 0$ the terms collapse fast, so a handful of them pin many digits; integrating out towards $x = 1$, where the series crawls, would have bought him almost nothing for the same labour. Newton got 16 decimal digits — the most accurate value computed in Europe at that point. He never published it; the calculation circulated among friends in the unpublished *De Methodis Serierum et Fluxionum* (1671).

**Maclaurin's 1742 *Treatise of Fluxions* gave the general framework** (Taylor series, with the now-standard $f^{(k)}(0)/k!$ formula), which makes the binomial series a corollary. But Newton had it first.

### The complex-analytic extension

The same formula $(1 + z)^n = \sum \binom{n}{k} z^k$ extends to complex $z$ in the unit disk $\lvert z \rvert < 1$. The right-hand side defines a *holomorphic* function on the open unit disk, and for non-integer $n$ it has a *branch cut* along the negative real axis (because $z = -1$ would give $0^n$ which can be ill-defined for non-integer $n$).

In **complex analysis**, the binomial series is the *Taylor expansion at $z = 0$* of the *principal branch* of $(1 + z)^n$, and its radius of convergence ($= 1$) is the distance from $0$ to the nearest singularity of $(1 + z)^n$, which sits at $z = -1$. This is an example of the general principle: **the radius of convergence of a Taylor series equals the distance to the nearest singularity in the complex plane**. (A theorem due to Cauchy.)

Even when you're only working with real $x$, the convergence radius is set by what happens *over the complex numbers*. Hence $\lvert x \rvert < 1$ for real $x$, dictated by a singularity at $z = -1$ in the complex plane.

### Generalized binomial coefficients and the Gamma function

The falling-factorial formula extends to non-integer $k$ too, using the **Gamma function** $\Gamma(x)$ (which interpolates the factorial: $\Gamma(n + 1) = n!$ for non-negative integers):

$$\binom{n}{k} = \dfrac{\Gamma(n+1)}{\Gamma(k+1)\,\Gamma(n - k + 1)}.$$

This works for any real (or complex) $n$ and $k$, except where the Gamma function has poles. *Beyond A-Level; standard in special-functions courses at university.*

The Gamma function itself is a 17th-century invention (Euler, 1729 — yes, *that* Euler, see [[Stories/The Hidden Number]] for his story). The fact that you can put fractional values into "factorial" via $\Gamma$ is one of the earlier surprises in the development of analysis.

### Why the radius is exactly 1

It might seem arbitrary that the convergence condition is $\lvert x \rvert < 1$ rather than $\lvert x \rvert < 2$ or $\lvert x \rvert < 1/2$. The reason is structural: the function $(1 + x)^n$ for non-integer $n$ has a **branch point** at $x = -1$, where the function value is $0^n$, which is multivalued or singular. The Taylor series at $x = 0$ converges out to the nearest singularity — which is at distance $1$. Hence radius $1$.

This is *Cauchy's theorem on the radius of convergence*: the disk of convergence of a power series equals the disk around the expansion point containing no singularities of the function. The binomial series is the cleanest example of the principle at work.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $(1 + x)^n$ | `(1 + x)^n` | The thing being expanded |
| $\binom{n}{k}$ | `\binom{n}{k}` | Generalized binomial coefficient — falling-factorial form |
| $\dfrac{n(n-1)\cdots(n-k+1)}{k!}$ | `\dfrac{n(n-1)\cdots(n-k+1)}{k!}` | Explicit falling factorial — use this form for non-integer $n$ |
| $\sum_{k=0}^\infty$ | `\sum_{k=0}^\infty` | Infinite sum, ascending powers |
| $\lvert x \rvert < 1$ | `\lvert x \rvert < 1` | The convergence condition — *always state it* |
| $\Gamma(n)$ | `\Gamma(n)` | Gamma function (beyond syllabus) |
| $f^{(k)}(0)$ | `f^{(k)}(0)` | $k$-th derivative evaluated at $0$ — used in Maclaurin derivation |
