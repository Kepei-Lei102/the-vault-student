---
chinese: 麦克劳林与泰勒级数 (Màikèláolín yǔ Tàilè jíshù)
prerequisites:
  - "[[Differentiation]]"
  - "[[Differentiation Rules]]"
  - "[[Power Rule]]"
  - "[[Factorial Notation]]"
  - "[[Sequences]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Limit]]"
  - "[[Binomial Series]]"
  - "[[L'Hôpital's Rule]]"
  - "[[Summation of Series]]"
leads_to:
  - "[[Numerical Methods]]"
  - "[[Differential Equations]]"
  - "[[Standard Integrals]]"
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[Complex Numbers]]"
  - "[[Mean Value Theorem]]"
  - "[[Stories/Stigler's Law of Eponymy]]"
  - "[[Hooke's Law for Springs]]"
  - "[[Simple Harmonic Motion]]"
tags:
  - subject/mathematics
  - domain/calculus
  - domain/analysis
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/IB-AA-HL-5-19
  - syllabus/AP-Calculus-BC-10
  - syllabus/9231-2-3
  - type/theorem
  - type/definition
  - type/technique
  - notation/sigma
  - notation/factorial
  - notation/derivative
  - misconception/forgetting-factorial
  - misconception/maclaurin-vs-taylor-confusion
  - misconception/analytic-equals-smooth
  - misconception/blind-truncation
---

# Maclaurin and Taylor Series 麦克劳林与泰勒级数

## Definition

### Formal

If a function $f$ is infinitely differentiable at a point $a$, its **Taylor series** centred at $a$ is

$$\boxed{\;f(x) \;=\; \sum_{k=0}^{\infty} \dfrac{f^{(k)}(a)}{k!}\,(x - a)^{k} \;=\; f(a) + f'(a)(x-a) + \dfrac{f''(a)}{2!}(x-a)^{2} + \dfrac{f'''(a)}{3!}(x-a)^{3} + \cdots\;}$$

The **Maclaurin series** is the special case $a = 0$:

$$f(x) \;=\; \sum_{k=0}^{\infty} \dfrac{f^{(k)}(0)}{k!}\,x^{k} \;=\; f(0) + f'(0)\,x + \dfrac{f''(0)}{2!}x^{2} + \dfrac{f'''(0)}{3!}x^{3} + \cdots$$

The equality holds for $x$ inside the **interval of convergence**, an open interval around $a$ on which the infinite sum actually converges to the function value. Outside it, the series diverges and the equation is meaningless.

### Intuitive

A polynomial is a finite linear combination of powers $1, x, x^2, x^3, \ldots$. Polynomials are *easy* — easy to evaluate, easy to differentiate, easy to integrate, easy to put in a computer.

The Taylor series is the answer to a daring question: *can we represent any well-behaved function as an infinite polynomial?* The answer is almost yes — for the functions you actually care about (exponentials, sines, logarithms, roots, rational functions), yes, on some interval around the chosen expansion point.

**The recipe.** Match the function's value at $a$, then its first derivative at $a$, then its second derivative at $a$, and so on. Each derivative pins down one more coefficient. The result is a polynomial-of-infinite-degree that agrees with $f$ at $a$ in every possible way a smooth function can agree.

**Three uses, all load-bearing.**
1. **Approximation.** Computers compute $\sin(0.7)$ via the first 5–6 terms of the Maclaurin series, not by some geometric construction.
2. **Theory.** Proofs of L'Hôpital's rule, Newton-Raphson's quadratic convergence, and Picard-Lindelöf's existence theorem for ODEs all flow through Taylor expansions.
3. **Unification.** Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ — the single most beautiful identity in mathematics — is *just* the observation that the Maclaurin series of $e^x$, $\cos x$, and $\sin x$ slot together when $x$ is imaginary. (See [[Euler's Formula and De Moivre's Theorem]].)

### 中文锚点 (Chinese Anchor)

**泰勒级数** 和 **麦克劳林级数** 是中国大学一年级 *微积分* 课程的核心内容，属于高等数学的基础。绝大多数中国国际学校的学生都见过公式本身，但有三点是英语考试体系特别看重、而国内课本经常一带而过的：

1. **收敛区间必须写出来。** 国内课本经常把 "对 $\lvert x \rvert < R$ 成立" 当作脚注；但 Cambridge、IB、AP 的评分员会真的扣分。**每一道泰勒/麦克劳林题的答案都要以一个明确的收敛限制条件收尾**，例如 "valid for $\lvert x \rvert < 1$" 或 "for all $x \in \mathbb{R}$"。

2. **拉格朗日余项 $R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$。** 国内学生通常学过这个公式，但很少在考试中实际用它做误差估计。**AP BC 和 IB AA HL 考试会明确要求用拉格朗日余项给出近似的误差上界** —— 如果答完一道近似题没有这一步，整道题最多拿一半分。这是中国留学生最常丢分的位置。

3. **"Maclaurin"（麦克劳林）只是 $a = 0$ 时的 Taylor（泰勒）。** 英联邦教育体系习惯把 $a = 0$ 这个特例单独命名为 "Maclaurin 级数"；中文教材一般不区分两者。**如果英语考题说 "find the Maclaurin series"，意思就是 "中心取 $a = 0$ 的 Taylor 展开"。** 同一台机器，只是参数 $a$ 默认设为 $0$。

中英文术语对照：

| English term | 中文 | Pinyin |
|---|---|---|
| Taylor series | 泰勒级数 | Tàilè jíshù |
| Maclaurin series | 麦克劳林级数 | Màikèláolín jíshù |
| radius of convergence | 收敛半径 | shōuliǎn bànjìng |
| interval of convergence | 收敛区间 | shōuliǎn qūjiān |
| Lagrange remainder | 拉格朗日余项 | Lāgélǎngrì yúxiàng |
| infinitely differentiable | 无限可微 | wúxiàn kěwēi |
| analytic function | 解析函数 | jiěxī hánshù |
| smooth function ($C^\infty$) | 光滑函数 | guānghuá hánshù |
| power series | 幂级数 | mì jíshù |

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Taylor series | $\sum_{k=0}^\infty \frac{f^{(k)}(a)}{k!}(x-a)^k$ | "Taylor series of $f$ around $a$" | The expansion point $a$ matters; specify it |
| Maclaurin series | $\sum_{k=0}^\infty \frac{f^{(k)}(0)}{k!}x^k$ | "Maclaurin series of $f$" | Always at $a = 0$; same formula, $a = 0$ baked in |
| $n$-th Taylor polynomial | $T_n(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!}(x-a)^k$ | "$n$-th Taylor polynomial" | The truncation; a degree-$n$ approximation |
| Lagrange remainder | $R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$ | "remainder after $n$ terms" | $\xi$ is some unknown point between $a$ and $x$ |
| Radius of convergence | $R$ | "the radius" | Series converges for $\lvert x - a \rvert < R$ |
| $k$-th derivative | $f^{(k)}(a)$ | "$f$-$k$ of $a$" | $f^{(0)}(a) = f(a)$, $f^{(1)} = f'$, etc. |

> [!warning] Notation trap
> The "$k!$" in the denominator is *not* optional. Forgetting the factorial is the single most common student error — see [[#Common Misconceptions (Teaching Notes)|Misconception 1]]. The factorial comes from differentiating $x^k$ exactly $k$ times: each differentiation pulls down a factor that, multiplied out, gives $k(k-1)(k-2)\cdots 1 = k!$.

## §1 — Where the formula comes from

The Taylor formula isn't a guess. It's *forced* on you the moment you ask for an "infinite polynomial" that matches $f$ and all its derivatives at the point $a$.

**Setup.** Suppose we *guess* that $f$ equals an infinite power series around $a$:
$$f(x) = a_0 + a_1(x-a) + a_2(x-a)^2 + a_3(x-a)^3 + \cdots$$

We don't yet know what the coefficients $a_0, a_1, a_2, \ldots$ are. Let's solve for them.

**Step 1 — Match $f(a)$.** Substitute $x = a$. Every $(x-a)^k$ term with $k \geq 1$ vanishes, leaving
$$f(a) = a_0 \quad \Longrightarrow \quad \boxed{a_0 = f(a)}.$$

**Step 2 — Match $f'(a)$.** Differentiate the series term-by-term (legal inside the radius of convergence — see [[Power Rule]] and the term-by-term differentiation lemma proved in [[Exponential Function]] §3):
$$f'(x) = a_1 + 2 a_2 (x-a) + 3 a_3 (x-a)^2 + 4 a_4 (x-a)^3 + \cdots$$
Substitute $x = a$: all terms with a positive power vanish, leaving $f'(a) = a_1$, so $\boxed{a_1 = f'(a)}$.

**Step 3 — Match $f''(a)$.** Differentiate again:
$$f''(x) = 2 a_2 + 3 \cdot 2 \, a_3 (x-a) + 4 \cdot 3 \, a_4 (x-a)^2 + \cdots$$
Substitute $x = a$: $f''(a) = 2 a_2$, so $\boxed{a_2 = \dfrac{f''(a)}{2!}}$. *The 2 came from $\dfrac{d}{dx} x^2 = 2x$ — and that's where the factorial pattern starts.*

**Step 4 — Match $f^{(k)}(a)$.** Differentiate $k$ times. The term $a_k (x-a)^k$ becomes, after $k$ differentiations, $a_k \cdot k \cdot (k-1) \cdot (k-2) \cdots 1 = a_k \cdot k!$, and all lower-degree terms vanish; all higher-degree terms still have factors of $(x-a)$, so they vanish on substituting $x = a$. The result:
$$f^{(k)}(a) = a_k \cdot k! \quad \Longrightarrow \quad \boxed{a_k = \dfrac{f^{(k)}(a)}{k!}}.$$

That's the entire derivation. The formula is the unique answer to "make every derivative match at $a$."

> [!tip] The polynomial view
> A polynomial $P(x) = a_0 + a_1(x-a) + \cdots + a_n(x-a)^n$ has exactly $n+1$ degrees of freedom: the coefficients $a_0, \ldots, a_n$. Specifying $f(a), f'(a), \ldots, f^{(n)}(a)$ is also exactly $n+1$ conditions. So there's a unique polynomial of degree $\leq n$ that matches $f$ and its first $n$ derivatives at $a$ — the **$n$-th Taylor polynomial** $T_n(x)$. The Taylor *series* is what happens when you let $n \to \infty$.

## §2 — Maclaurin is Taylor at zero (the most important callout)

The relationship is structural, not conventional:

$$\underbrace{f(x) = \sum_{k=0}^\infty \dfrac{f^{(k)}(a)}{k!}(x-a)^k}_{\text{Taylor at }a} \quad \xrightarrow{\;a \,=\, 0\;} \quad \underbrace{f(x) = \sum_{k=0}^\infty \dfrac{f^{(k)}(0)}{k!}x^k}_{\text{Maclaurin}}$$

Setting $a = 0$ collapses every $(x - a)^k$ to $x^k$ and every $f^{(k)}(a)$ to $f^{(k)}(0)$. *That's all "Maclaurin" means.*

**Why we keep both names.** Most exam-level expansions are around zero (the algebra is cleanest at $x = 0$), so the Commonwealth tradition keeps "Maclaurin" as a short name for that case. American textbooks often just say "Taylor series around 0." Either is fine. **If a 9709 / IB / AP question asks for a "Maclaurin series", give the Taylor expansion at $a = 0$.**

**When to use Taylor at $a \neq 0$ instead.**
- The function isn't defined at 0 (e.g. $\ln x$ — we'd need to expand around $a = 1$ instead, giving $\ln x = (x-1) - \tfrac{1}{2}(x-1)^2 + \tfrac{1}{3}(x-1)^3 - \cdots$).
- The function has a singularity at 0 (e.g. $1/(1-x)$ — Maclaurin works for $\lvert x \rvert < 1$, but if you want behaviour near $x = 5$, you'd expand around $a = 5$).
- You want fast convergence near a specific point.

## §3 — The Six Named Expansions (memorise these)

These six Maclaurin series come up *constantly* on IB AA HL, AP Calc BC, A-Level Further, and competition mathematics. Every other Maclaurin question can usually be derived from one of these by substitution, integration, differentiation, or multiplication. **Memorise them.**

| Function | Maclaurin Series | Interval of convergence | $k$-th term |
|---|---|---|---|
| $e^x$ | $1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \dfrac{x^4}{4!} + \cdots$ | $\mathbb{R}$ (all $x$) | $\dfrac{x^k}{k!}$ |
| $\sin x$ | $x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \dfrac{x^7}{7!} + \cdots$ | $\mathbb{R}$ | $\dfrac{(-1)^k x^{2k+1}}{(2k+1)!}$ |
| $\cos x$ | $1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \dfrac{x^6}{6!} + \cdots$ | $\mathbb{R}$ | $\dfrac{(-1)^k x^{2k}}{(2k)!}$ |
| $\ln(1 + x)$ | $x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dfrac{x^4}{4} + \cdots$ | $-1 < x \leq 1$ | $\dfrac{(-1)^{k+1} x^k}{k}$ |
| $\arctan x$ | $x - \dfrac{x^3}{3} + \dfrac{x^5}{5} - \dfrac{x^7}{7} + \cdots$ | $-1 \leq x \leq 1$ | $\dfrac{(-1)^k x^{2k+1}}{2k+1}$ |
| $(1+x)^n$ | $1 + nx + \dfrac{n(n-1)}{2!}x^2 + \dfrac{n(n-1)(n-2)}{3!}x^3 + \cdots$ | $\lvert x \rvert < 1$ (non-integer $n$) | $\binom{n}{k} x^k$ |

The binomial series is the subject of its own card — [[Binomial Series]].

> [!tip] Why these six
> They're the building blocks. Every other Maclaurin series in the standard course is a substitution, derivative, integral, or product of one of these. Examples:
> - $\sin(2x)$ → substitute $x \to 2x$ in the $\sin$ series
> - $\dfrac{e^x - 1}{x}$ → divide the $e^x$ series by $x$ (after subtracting 1)
> - $\dfrac{1}{1-x}$ → set $n = -1$ in the binomial series (with $x \to -x$); also = $1 + x + x^2 + x^3 + \cdots$ (geometric)
> - $\ln(1-x)$ → substitute $x \to -x$ in the $\ln(1+x)$ series
> - $\arcsin x$ → integrate the binomial series for $(1-x^2)^{-1/2}$
>
> Knowing the six unlocks all of them. The exam reward for memorising is enormous.

## §4 — Deriving one (worked: $\sin x$)

Take $f(x) = \sin x$ and expand around $a = 0$.

| $k$ | $f^{(k)}(x)$ | $f^{(k)}(0)$ |
|---|---|---|
| 0 | $\sin x$ | $0$ |
| 1 | $\cos x$ | $1$ |
| 2 | $-\sin x$ | $0$ |
| 3 | $-\cos x$ | $-1$ |
| 4 | $\sin x$ | $0$ |
| 5 | $\cos x$ | $1$ |

The pattern of $f^{(k)}(0)$ is $0, 1, 0, -1, 0, 1, 0, -1, \ldots$ — period 4. Only odd $k$ contribute, with alternating sign:

$$\sin x = 0 + 1 \cdot x + 0 \cdot \dfrac{x^2}{2!} + (-1)\dfrac{x^3}{3!} + 0 \cdot \dfrac{x^4}{4!} + 1 \cdot \dfrac{x^5}{5!} + \cdots = x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \dfrac{x^7}{7!} + \cdots$$

The series converges to $\sin x$ for **every** real $x$ — its radius of convergence is $\infty$. (This is because $\sin$ has no singularities anywhere in the complex plane — see §6.)

**Sanity check.** For $x = 0.1$ (radians):
- Exact: $\sin(0.1) = 0.09983341664\ldots$
- Three terms: $0.1 - \dfrac{0.001}{6} + \dfrac{0.00001}{120} \approx 0.0998334\ldots$ — six decimal places accurate.

That's why your calculator uses Taylor (or polynomial approximations derived from it) to compute $\sin$.

## §5 — The Lagrange Remainder

Truncating a Taylor series at $T_n(x)$ leaves an error. **How big?**

**Taylor's theorem (Lagrange form).** If $f$ is $(n+1)$-times differentiable on an open interval containing $a$ and $x$, then
$$f(x) = T_n(x) + R_n(x), \quad\text{where}\quad R_n(x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!}\,(x-a)^{n+1}$$
for some $\xi$ strictly between $a$ and $x$.

The remainder $R_n(x)$ looks *exactly* like the next term of the Taylor series — except the derivative is evaluated at the unknown $\xi$ rather than at $a$.

**How to use it for an error bound.** You don't know $\xi$, so you bound $\lvert f^{(n+1)} \rvert$ over the whole interval $[a, x]$. If $M$ is an upper bound on $\lvert f^{(n+1)}(t) \rvert$ for $t$ in $[a, x]$, then
$$\lvert R_n(x) \rvert \leq \dfrac{M}{(n+1)!}\,\lvert x - a \rvert^{n+1}.$$

> [!info] Beyond syllabus — why this looks like a generalised MVT
> The case $n = 0$ of Lagrange's remainder is
> $$f(x) - f(a) = f'(\xi)(x - a),$$
> which is exactly the **Mean Value Theorem** ([[Mean Value Theorem]]). Taylor's theorem with Lagrange remainder is the natural generalisation of the MVT to higher derivatives: the "average slope" of the MVT becomes "the next missing term, evaluated at *some* intermediate point." This is why the MVT keeps appearing in advanced calculus — it's the $n = 0$ baby case of Taylor's theorem.

### Worked example: bound the error in $\sin(0.5) \approx T_5(0.5)$

Use the Maclaurin series of $\sin$, truncated after the $x^5$ term:
$$T_5(x) = x - \dfrac{x^3}{6} + \dfrac{x^5}{120}.$$

The next nonzero term is $-\dfrac{x^7}{7!}$, so we want a bound on $R_6$ (or equivalently $R_5$, since the $x^6$ term has coefficient zero for $\sin$). The 7th derivative of $\sin$ is $\pm\cos x$ or $\pm\sin x$ — *whichever case*, $\lvert f^{(7)}(t) \rvert \leq 1$ for all real $t$. So $M = 1$, and

$$\lvert R_6(0.5) \rvert \leq \dfrac{1}{7!} \cdot (0.5)^7 = \dfrac{0.0078125}{5040} \approx 1.55 \times 10^{-6}.$$

So $T_5(0.5)$ is accurate to within $\sim 1.5 \times 10^{-6}$. (Actual: $\sin(0.5) = 0.479425\ldots$; $T_5(0.5) = 0.479427\ldots$. Difference $\approx 2 \times 10^{-6}$. The bound is correct.)

## §6 — Radius of Convergence (Cauchy's "distance to singularity")

A Taylor series at $a$ converges for $\lvert x - a \rvert < R$ and diverges for $\lvert x - a \rvert > R$, where $R$ is the **radius of convergence**. At the boundary $\lvert x - a \rvert = R$, behaviour is case-by-case.

**For polynomials of finite degree:** $R = \infty$ (trivially).

**For $e^x$, $\sin x$, $\cos x$:** $R = \infty$. These functions have no "trouble points" anywhere.

**For $\ln(1+x)$:** $R = 1$. There's a logarithmic singularity at $x = -1$ (where $1 + x = 0$).

**For $\arctan x$:** $R = 1$. *But wait* — $\arctan$ has no real-line singularities! Where does $R = 1$ come from?

> [!info] Beyond syllabus — Cauchy's theorem
> The full answer comes from complex analysis. **Cauchy's theorem on the radius of convergence of a power series:** the radius equals the distance, in the **complex plane**, from the expansion centre $a$ to the nearest singularity of the function.
>
> For $\arctan x$, the function (extended to complex numbers as $\arctan z$) has branch points at $z = \pm i$. The distance from the origin to $\pm i$ is exactly $1$. *That's* why the Maclaurin series of $\arctan$ has $R = 1$ — even though no singularity appears on the real line, the complex-plane singularity at $i$ is "watching" and limits the radius.
>
> Same story for $\dfrac{1}{1 + x^2}$: no real singularities, but $R = 1$ because of the complex roots at $\pm i$. **This is one of the deepest connections between calculus and complex analysis: real-line convergence is governed by complex-plane geometry.** See [[Complex Numbers]] for the rest of the story.

| Function | Radius of convergence at $a = 0$ | Reason |
|---|---|---|
| $e^x$ | $\infty$ | Entire function — no singularities anywhere |
| $\sin x$, $\cos x$ | $\infty$ | Entire |
| $\dfrac{1}{1-x}$ | $1$ | Pole at $x = 1$ |
| $\ln(1+x)$ | $1$ | Branch point at $x = -1$ |
| $\arctan x$ | $1$ | Complex branch points at $x = \pm i$ |
| $\dfrac{1}{1 + x^2}$ | $1$ | Complex poles at $\pm i$ |
| $(1+x)^n$ for non-integer $n$ | $1$ | Branch point at $x = -1$ |

## §7 — Worked Examples

### Example 1 (IB AA HL level): Find the Maclaurin series of $f(x) = e^{-x^2}$ up to the $x^6$ term.

**Strategy:** substitute, don't compute derivatives.

Start with the known $e^x$ series:
$$e^x = 1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \dfrac{x^4}{4!} + \cdots$$

Substitute $x \to -x^2$:
$$e^{-x^2} = 1 + (-x^2) + \dfrac{(-x^2)^2}{2!} + \dfrac{(-x^2)^3}{3!} + \cdots = 1 - x^2 + \dfrac{x^4}{2} - \dfrac{x^6}{6} + \cdots$$

That's it. Computing 7 derivatives of $e^{-x^2}$ from scratch is *brutal*; substituting into the known series is one line.

> [!info] Beyond syllabus — why this matters
> The function $e^{-x^2}$ is the **Gaussian bell curve** (up to normalisation), the foundation of probability, statistics, and the Normal distribution. Its antiderivative, $\int e^{-x^2}\,dx$, **does not have a closed form in elementary functions** (this is a theorem of Liouville — see [[Standard Integrals]]). But its Maclaurin series gives an exact integration:
> $$\int e^{-x^2}\,dx = C + x - \dfrac{x^3}{3} + \dfrac{x^5}{2 \cdot 5} - \dfrac{x^7}{6 \cdot 7} + \cdots$$
> — term-by-term, no closed form needed. This is how statistical-software libraries compute the error function $\mathrm{erf}(x) = \dfrac{2}{\sqrt{\pi}}\int_0^x e^{-t^2}\,dt$.

### Example 2 (AP BC level): Use the Maclaurin series of $\ln(1+x)$ to approximate $\ln(1.1)$ to four decimal places.

Series:
$$\ln(1 + x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dfrac{x^4}{4} + \dfrac{x^5}{5} - \cdots$$

Substitute $x = 0.1$:
$$\ln(1.1) \approx 0.1 - 0.005 + 0.000333\ldots - 0.000025 + 0.000002 - \cdots$$
$$\approx 0.09531\ldots$$

To bound the error: this is an alternating series with strictly decreasing terms, so the error after truncating at any term is bounded by the next term. After five terms ($x = 0.1$), the error is at most $\dfrac{0.1^6}{6} \approx 1.67 \times 10^{-7}$. So $\ln(1.1) \approx 0.0953$ to 4 d.p. — and indeed $\ln(1.1) = 0.09531017\ldots$.

### Example 3 (A-Level Further / IB AA HL): Use Maclaurin series to evaluate $\displaystyle\lim_{x \to 0} \dfrac{\sin x - x}{x^3}$.

**Strategy:** Taylor series is the **deeper L'Hôpital's Rule** — it tells you exactly how fast each piece of an indeterminate form vanishes.

Substitute the $\sin x$ series:
$$\sin x - x = \left( x - \dfrac{x^3}{6} + \dfrac{x^5}{120} - \cdots\right) - x = -\dfrac{x^3}{6} + \dfrac{x^5}{120} - \cdots$$

Divide by $x^3$:
$$\dfrac{\sin x - x}{x^3} = -\dfrac{1}{6} + \dfrac{x^2}{120} - \cdots$$

Take the limit as $x \to 0$:
$$\boxed{\lim_{x \to 0} \dfrac{\sin x - x}{x^3} = -\dfrac{1}{6}.}$$

> [!tip] Why Taylor beats L'Hôpital here
> L'Hôpital's rule on $\dfrac{\sin x - x}{x^3}$ would need *three* applications (it's $\tfrac{0}{0}$ each time until the third). Taylor series gives the answer in one substitution. The Taylor approach also explains *why* — it's the cubic term of $\sin$ that survives. L'Hôpital just spits out the number; Taylor shows the structure. See [[L'Hôpital's Rule]] §8 for the broader comparison.

### Example 4 (Cambridge 9231): the successive-differentiation route — $\tan x$ up to $x^3$

Some functions have no friendly known series to substitute into, and the syllabus's own example is $y = \tan x$. The technique: differentiate **successively**, feeding each derivative back into the ones after it, then evaluate everything at $0$ and assemble.

*Tool: the derivative that quotes itself.* $y' = \sec^2 x = 1 + \tan^2 x = 1 + y^2$ — the derivative written *in terms of $y$*, which is the whole trick, because now each further derivative comes by the chain rule with no new trigonometry:

$$y' = 1 + y^2 \quad\Longrightarrow\quad y'' = 2y\,y' \quad\Longrightarrow\quad y''' = 2(y')^2 + 2y\,y''.$$

*Tool: evaluate the chain at $x = 0$, bottom up.* $y(0) = 0$, so $y'(0) = 1 + 0 = 1$, then $y''(0) = 2 \cdot 0 \cdot 1 = 0$, then $y'''(0) = 2 \cdot 1 + 0 = 2$. Assemble:

$$\tan x = y(0) + x\,y'(0) + \frac{x^2}{2!}\,y''(0) + \frac{x^3}{3!}\,y'''(0) + \cdots = \boxed{\ x + \frac{x^3}{3} + \cdots\ } \qquad \left(\text{next term } \tfrac{2}{15}x^5\right)$$

> [!warning] The exam shape, and a one-mark trap
> On 9231 Paper 2 this technique usually arrives welded to the *other* differentiation LO: an earlier part makes you find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for an implicitly or parametrically defined relation ([[Implicit Differentiation]], [[Parametric Differentiation]]), and the last part says "hence find the first three terms of the Maclaurin series" — the assembly step is exactly the boxed formula with *your* computed values. A real recent scheme awards the method mark for $y(0), y'(0), y''(0)$ evaluated, and then **refuses the accuracy mark if $\frac{x^2}{2!}$ is left unsimplified** — write $\frac{x^2}{2}$, always.

## §8 — Beyond Syllabus

### Taylor's theorem with integral remainder

The Lagrange remainder uses the MVT-style "some unknown intermediate point $\xi$". A more powerful (and more explicit) formulation uses an integral:

$$f(x) = T_n(x) + \dfrac{1}{n!}\int_a^x f^{(n+1)}(t)\,(x - t)^n\,dt.$$

This is the **integral form of the remainder**, and it's what you reach for when you need quantitative error analysis (numerical analysis, approximation theory). Liouville and Cauchy worked in this language. **Proof sketch:** integration by parts on $\int_a^x f'(t)\,dt = f(x) - f(a)$, applied $n$ times, gives exactly the Taylor expansion with this remainder form. Try it for $n = 1$ to see the pattern.

### Analytic $\neq$ smooth — the $e^{-1/x^2}$ pathology

A function is **analytic** at $a$ if its Taylor series at $a$ converges to it in some neighbourhood. A function is **smooth** ($C^\infty$) if it has derivatives of all orders. *These are not the same thing.* Analytic implies smooth (obvious), but smooth does not imply analytic.

**The canonical counterexample:**
$$f(x) = \begin{cases} e^{-1/x^2} & x \neq 0 \\ 0 & x = 0 \end{cases}$$

This function is $C^\infty$ on all of $\mathbb{R}$ — every derivative exists, is continuous, and *every derivative at $x = 0$ equals zero* (an exercise in L'Hôpital and induction). So the Maclaurin series of $f$ is
$$0 + 0 \cdot x + 0 \cdot x^2 + 0 \cdot x^3 + \cdots = 0,$$
the zero series. But $f$ itself is *not* identically zero. **The Maclaurin series converges (to zero) but does not converge to $f$.**

> [!info] Why this matters
> Most of the functions you've ever computed with — $e^x$, $\sin$, $\cos$, $\ln(1+x)$, $\arctan$, polynomials, rational functions, $\sqrt{x}$ — are *analytic* where they're defined. The Taylor-series machinery feels universal because of this. But the $e^{-1/x^2}$ pathology reveals a gap: smooth functions are a strictly larger class than analytic ones. In **differential geometry** and **distribution theory**, this gap is load-bearing — the bump function used in partition-of-unity constructions is built from $e^{-1/x^2}$ pieces precisely because it's smooth-but-not-analytic, letting it be "turned off" in some regions while staying $C^\infty$.
>
> **Real-analytic vs complex-analytic.** In the complex setting, the analogous pathology *cannot happen*: a function $\mathbb{C} \to \mathbb{C}$ that is once differentiable is automatically infinitely differentiable AND equal to its Taylor series in some disc. This is one of the central miracles of complex analysis, and it's the deep reason why complex differentiation is "rigid" in a way real differentiation is not.

### Stigler's Law strikes again

> *"No scientific discovery is named after its original discoverer."* — **Stephen Stigler (1980)**, in a self-referential punchline that's itself a Stigler casualty (Robert Merton said it first).

Maclaurin and Taylor are both casualties.

**Taylor.** *Brook Taylor* published the formula in *Methodus Incrementorum Directa et Inversa* (1715). But James Gregory had it in 1670–71, in unpublished correspondence with John Collins. Newton had it independently — and earlier — in his 1671 *De Methodis Serierum et Fluxionum*. (Newton's version is sketchier and never quite reaches the general statement.) **Taylor's contribution is the general theorem; the special cases predate him by 40+ years.**

**Maclaurin.** *Colin Maclaurin* (1698–1746, Newton's friend and ally in the Calculus Priority Dispute) wrote the $a = 0$ case prominently in his *Treatise of Fluxions* (1742). But Brook Taylor himself had already noted this special case in 1715. And James Stirling had used it specifically in 1717. **Calling the $a = 0$ case "Maclaurin's series" is essentially honouring a textbook author for popularising a thirty-year-old result.**

Both names stick because both writers wrote clearly enough that their versions became *the* reference for the next generation.

> [!tip] Stories bridge — [[Stories/Stigler's Law of Eponymy]]
> The full eponymy pattern — and a dozen more casualties (Pythagoras's Theorem / Babylonian tablets, Pascal's Triangle / Yang Hui, Cardano's Formula / Tartaglia, Hooke's Law / medieval bowmakers, Pell's Equation / Brahmagupta, Newton's First Law / Galileo, Fibonacci / Pingala, Benford's Law / Newcomb, the Mandelbrot set / Brooks-Matelski) — lives in [[Stories/Stigler's Law of Eponymy]]. Two related drama threads already in the vault: [[Stories/The Bernoulli Family]] (the L'Hôpital paid contract) and [[Stories/The Calculus Priority Dispute]] (Newton vs Leibniz). The Hooke side of the eponymy pattern lives in [[Stories/Newton vs Hooke]].

### Why Newton-Raphson converges quadratically

The Newton-Raphson iteration $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$ converges *quadratically* — the error squares at each step — and the proof is a one-line Taylor expansion at the root $\alpha$:

$$0 = f(\alpha) = f(x_n + (\alpha - x_n)) = f(x_n) + f'(x_n)(\alpha - x_n) + \dfrac{f''(\xi)}{2}(\alpha - x_n)^2.$$

Rearranging gives $\alpha - x_{n+1} = -\dfrac{f''(\xi)}{2 f'(x_n)}(\alpha - x_n)^2$, i.e. the new error is proportional to the old error *squared*. This is the deep reason Newton-Raphson is fast — the second derivative term in the Taylor expansion is what gets dominated. See [[Numerical Methods]] §3 for the full derivation; the Taylor expansion is now justified by the present card.

### Power series of matrices

Once you trust the Maclaurin series of $e^x$ — i.e. it converges for *every* real $x$ — it converges for every complex $x$ (this is the radius-of-convergence claim for entire functions). More radically, **it converges for every square matrix $X$:**
$$e^X = I + X + \dfrac{X^2}{2!} + \dfrac{X^3}{3!} + \cdots$$
This is the **matrix exponential**, and it's load-bearing for the theory of differential equations (the solution of $\mathbf{y}' = A\mathbf{y}$ is $\mathbf{y}(t) = e^{tA}\mathbf{y}(0)$) and Lie groups (the exponential map). Same series, broader algebra. See [[Euler's Formula and De Moivre's Theorem]] §"Beyond syllabus" for the rotation-matrix case.

## Common Misconceptions (Teaching Notes)

### 1. Forgetting the factorial

Students write
$$f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2 + f'''(a)(x-a)^3 + \cdots$$
without the $\dfrac{1}{k!}$ factors. Wrong.

**Fix:** drill the derivation in §1. The factorial isn't decorative — it's what *makes the derivative matching work*. Remind students: differentiating $x^k$ produces $k(k-1)(k-2)\cdots = k!$ at the lead, so to cancel that and leave a clean $1$, we must put $1/k!$ in the original coefficient. The factorial is the "anti-derivative-of-the-derivative-pile-up."

### 2. Confusing Maclaurin with Taylor

Students who learned only the Taylor formula sometimes don't realise Maclaurin is the same thing with $a = 0$ — they panic when an exam says "find the Maclaurin series" as if it's a separate technique. Or worse: they substitute their Taylor centre back into a Maclaurin question and get a series in $(x - a)$ when the question wants a series in $x$.

**Fix:** §2 of this card is the antidote. Reinforce: *if the question says "Maclaurin", then $a = 0$; if it says "Taylor around $x = c$", then $a = c$.* Same machine; different setting on the dial.

### 3. Treating "smooth" and "analytic" as synonyms

Students see the $e^x$ series converge for all $x$, see the $\sin x$ series converge for all $x$, see the $\cos x$ series converge for all $x$, and conclude *every smooth function is its Taylor series*. This is false (§8).

**Fix:** introduce the $e^{-1/x^2}$ example by name even if not fully treated. Tell students: there exist $C^\infty$ functions whose Maclaurin series converges, but converges to *the wrong thing* (or to zero, for that function). For exam purposes you'll only meet analytic functions; for the rest of mathematics, the distinction matters.

### 4. Blind truncation without an error bound

Students keep 3 terms of a series and claim "good enough" without computing the Lagrange remainder. Examiners — especially on AP BC and IB AA HL — *will* ask for a justification.

**Fix:** when approximating $f(x)$, always finish with "Lagrange remainder bound: $\lvert R_n(x) \rvert \leq M \lvert x - a \rvert^{n+1} / (n+1)!$ where $M$ bounds $\lvert f^{(n+1)} \rvert$, giving error $\leq \ldots$". Make this a reflex.

### 5. Forgetting the interval of convergence

Students write down a Maclaurin series happily but don't state the range of $x$ for which it equals the function. The series for $\ln(1+x)$ converges for $-1 < x \leq 1$; it is *meaningless* outside that range. Exam mark schemes penalise this omission.

**Fix:** every Maclaurin / Taylor answer ends with "valid for $\lvert x \rvert < R$" (or whatever the relevant interval is). Make it part of the box around the final answer.

## Exam Notes

### IB AA HL (Topic 5 — Calculus, sub-topic 5.19)

Maclaurin series is a **core HL topic** (it does not appear on AA SL). Examiners expect:

1. The six named expansions (memorised).
2. Manipulating series: substitution, differentiation, integration, products (truncated to a stated order).
3. The Lagrange remainder for error bounds.
4. Interval of convergence (state it).

**Typical question shape:** "Given $f(x) = e^x \cos x$, find the Maclaurin series up to the $x^4$ term, and use it to approximate $f(0.2)$ with an upper bound on the error." This is a substitution + product + truncation + remainder question — a single problem touches the whole topic.

### AP Calculus BC (Unit 10 — Infinite Sequences and Series)

Maclaurin and Taylor series are **the entire final unit** of BC (and they appear heavily on the AP exam — typically one full FRQ and 6–10 MCQ).

Required mastery:
1. The six named expansions.
2. Term-by-term differentiation and integration of power series.
3. The ratio test for radius of convergence.
4. The Lagrange error bound (formal).
5. The alternating-series error bound (an alternative when applicable).
6. Knowing when to expand around $a \neq 0$ (the "Taylor centred at" question type).

The AP exam loves problems of the form: "the function $f$ has $f^{(n)}(0) = (-1)^n n!$ for all $n \geq 0$. (a) Find the Maclaurin series of $f$. (b) Find the interval of convergence. (c) Identify $f$ explicitly."

### A-Level Further (FP1 / Cambridge 9231)

Maclaurin series appears in the Cambridge **Further Pure 1** module. Standard expansions (the six) are required; the Lagrange remainder is sometimes asked. Less depth than IB AA HL or AP BC but the same shape.

### Cambridge 9709

**Not on 9709 P1–P6.** Standard 9709 Pure does *not* cover Maclaurin / Taylor explicitly. [[Binomial Series]] (which IS on 9709 P3 §3.1) is the only power-series-shaped object the standard 9709 student meets. **However**, every existing 9709 P3 card in the vault that mentions "Maclaurin" — [[Binomial Series]] §3, [[Numerical Methods]] §3, [[Euler's Formula and De Moivre's Theorem]] §1 — uses it for derivation, and this card is the foundation those derivations rest on. *9709 students don't sit Maclaurin questions but benefit from understanding it as the engine behind the binomial series.*

> [!info] Formula-sheet status — *what to memorise vs what's given*
> The answer varies dramatically by board, and **the variation itself is exam-relevant**. The summary below describes typical practice and **must be verified against the actual booklet for the year of the student's exam** (Cambridge has revised MF19 before; IB and AP booklets are also revisable — `_meta` tracks this as cross-cutting task M1 awaiting the actual booklets).
>
> **Cambridge 9709 (MF19):** Maclaurin/Taylor not tested → no entries on the sheet. The binomial series for general $n$ *is* on MF19 (see [[MF19 Reference (9709)]]). 9709 students don't need to memorise.
>
> **Cambridge 9231 (Further, MF19):** Standard expansions $e^x$, $\sin x$, $\cos x$, $\ln(1+x)$, $(1+x)^n$ are on MF19. The $\arctan$ Maclaurin is *not* listed — that one needs memorising.
>
> **IB AA HL:** The IB AA formula booklet provides $e^x$, $\sin x$, $\cos x$, $\ln(1+x)$, and the binomial. **The Maclaurin of $\arctan x$ is not given** — and HL questions test it (it's how IB introduces Gregory's series for $\pi$, which makes for clean exam problems).
>
> **AP Calculus BC:** The AP BC reference sheet provides $e^x$, $\sin x$, $\cos x$, and the **geometric series** $\dfrac{1}{1-x}$. It does **not** give $\ln(1+x)$, $\arctan x$, or the binomial series. AP BC students need to memorise those three — and the test loves all three.
>
> **The asymmetry that catches everyone:** the **$\arctan$ Maclaurin** is the expansion most heavily tested *and* least often given on the sheet (it's not on IB AA HL, AP BC, or 9709/9231's MF19 — only A-Level Further-via-Edexcel typically lists it). If you're going to memorise *one* expansion that isn't already on the formula booklet you're using, make it $\arctan x = x - \dfrac{x^3}{3} + \dfrac{x^5}{5} - \dfrac{x^7}{7} + \cdots$ (valid for $\lvert x \rvert \leq 1$).
>
> **The framing.** Students don't need to memorise formulas the exam will hand them — they need to *understand* them well enough to manipulate them. The boards that give the standard expansions are testing whether you can substitute, multiply, integrate, and bound errors. The boards that don't give them are also testing memory. **Always check what your board's current sheet provides** before deciding what to memorise.

## Connections

- **Parent:** [[Differentiation]] — the formula is built from derivatives evaluated at a point
- **Direct prerequisite:** [[Binomial Series]] — the special case of $(1+x)^n$; written first because it appears on 9709 P3; this card generalises it
- **Direct prerequisite:** [[L'Hôpital's Rule]] — same indeterminate-form territory; Taylor is the deeper L'Hôpital
- **Direct prerequisite:** [[Factorial Notation]] — the $k!$ in the denominator
- **Sister card:** [[Mean Value Theorem]] — Taylor with $n = 0$ remainder IS the MVT
- **Application:** [[Numerical Methods]] — Taylor expansion at the root proves Newton-Raphson's quadratic convergence (§3 of that card)
- **Application:** [[Standard Integrals]] — Maclaurin lets you integrate $e^{-x^2}$, $\sin(x^2)$, and other no-elementary-antiderivative functions term-by-term
- **Application:** [[Euler's Formula and De Moivre's Theorem]] — the power-series proof of $e^{i\theta} = \cos\theta + i\sin\theta$ uses the Maclaurin expansions of all three functions
- **Application:** [[Complex Numbers]] — analytic continuation; radius of convergence as complex-plane distance
- **Application:** [[Differential Equations]] — Picard-Lindelöf builds solutions by Taylor-like iteration
- **Stories sibling:** [[Stories/Stigler's Law of Eponymy]] — Taylor and Maclaurin are both Stigler casualties (Gregory and Newton had Taylor's formula 40+ years earlier; Stirling and Taylor had Maclaurin's case 30 years earlier). The meta-card pulling every vault eponymy thread together.
- **For 9709 students:** [[MF19 Reference (9709)]] — Maclaurin and Taylor are *not* on MF19 (9709 doesn't test them directly), but the binomial series with general $n$ is given. (Other boards have their own sheets.)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\displaystyle\sum_{k=0}^{\infty}$ | `\sum_{k=0}^{\infty}` | Sum from 0 to infinity |
| $f^{(k)}(a)$ | `f^{(k)}(a)` | $k$-th derivative at $a$; parentheses on the $k$ are mandatory (without them it's $f^k$ — a power) |
| $k!$ | `k!` | Factorial; see [[Factorial Notation]] |
| $T_n(x)$ | `T_n(x)` | $n$-th Taylor polynomial |
| $R_n(x)$ | `R_n(x)` | Remainder after $n$ terms |
| $\xi$ | `\xi` | "ksai" — Greek letter for the unknown intermediate point in Lagrange remainder |
| $\dfrac{f^{(k)}(a)}{k!}$ | `\dfrac{f^{(k)}(a)}{k!}` | Display-size fraction for tables |
| $\lvert x - a \rvert < R$ | `\lvert x - a \rvert < R` | Use `\lvert/\rvert` not `|` to avoid table-cell breakage |
| $C^{\infty}$ | `C^{\infty}` | Smooth functions class |
| $\mathbb{R}$, $\mathbb{C}$ | `\mathbb{R}, \mathbb{C}` | Reals, complex numbers |
| $e^{-1/x^2}$ | `e^{-1/x^2}` | The canonical smooth-but-not-analytic counterexample |
