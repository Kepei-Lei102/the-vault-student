---
chinese: 数值方法 (shùzhí fāngfǎ) — 根的逼近
prerequisites:
  - "[[Differentiation]]"
  - "[[Differentiation Rules]]"
  - "[[Tangents and Normals]]"
  - "[[Sequences]]"
  - "[[Function]]"
  - "[[Maclaurin Series]]"
leads_to: []
teach_together:
  - "[[Differential Equations]]"
tags:
  - subject/mathematics
  - domain/calculus
  - domain/algebra
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-3-6
  - syllabus/9709-2-6
  - type/algorithm
  - type/technique
  - notation/iteration
  - misconception/forgetting-sign-change
  - misconception/wrong-rearrangement
  - misconception/newton-raphson-trap
  - misconception/insufficient-precision
---

# Numerical Methods 数值方法

## Definition

### Formal

A **numerical method** is an algorithm that produces a sequence $(x_0, x_1, x_2, \ldots)$ converging to a solution of an equation $f(x) = 0$ when no closed-form solution exists or is impractical to compute. At 9709 P3 §3.6 we cover three:

- **Bisection** — halve a sign-change interval repeatedly. Always converges (slowly).
- **Fixed-point iteration** — rewrite $f(x) = 0$ as $x = g(x)$, then iterate $x_{n+1} = g(x_n)$. Converges if $\lvert g'(\alpha) \rvert < 1$ at the root $\alpha$.
- **Newton-Raphson** — iterate $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$. **Quadratically convergent** when it works — the number of correct digits *doubles* each step.

### Intuitive

Most equations in real life don't have closed-form roots. **$\cos x = x$** has a perfectly real solution (about $0.7390851\ldots$) but you can't write it as a finite combination of standard functions — no $\sqrt{\,}$, no $\ln$, no algebraic trick will pin it down exactly. So instead of *solving* the equation, you *approximate* the answer. You generate a sequence of guesses, each better than the last, until the digits stabilise to the precision you need.

That's the whole subject. Three workhorses, each with its own personality:

- **Bisection** is the tortoise. Slow but guaranteed. If you can find two $x$-values bracketing a sign change of $f$, you halve the interval each step. You gain one bit per iteration. To get six decimal places: about 20 iterations.
- **Fixed-point iteration** is the medium-pace runner. Rewrite the equation, iterate, hope $g'$ is small enough at the root. Convergence is linear — error shrinks by a constant factor each step. Sometimes fast, sometimes slow, sometimes diverges entirely.
- **Newton-Raphson** is the cheetah. Geometrically: draw the tangent at $(x_n, f(x_n))$, see where it crosses the $x$-axis, that's $x_{n+1}$. When it works, it's *spectacular* — each step roughly doubles the number of correct decimal places. From 3 digits to 6 digits in one step; from 6 to 12 in the next. Six decimal places: 4–5 iterations.

The hidden subject is **fixed-point theory**. All three methods are special cases of "iterate a function and look for fixed points." When the iteration is contractive enough, it converges. When it isn't, you fail. Understanding *why* and *when* is more important than the specific formulas.

### 中文锚点

**数值方法**（shùzhí fāngfǎ）/ 数值逼近：当方程 $f(x) = 0$ 没有解析解（或解析解太复杂）时，用迭代算法生成一系列逐步逼近真解的近似值。9709 P3 §3.6 覆盖三种：

1. **二分法**（bisection / 折半法）— 找一个区间 $[a, b]$ 使 $f(a)$ 和 $f(b)$ 异号，反复取中点，每次区间长度减半。慢但保证收敛。
2. **不动点迭代**（fixed-point iteration / 迭代法）— 把 $f(x) = 0$ 改写为 $x = g(x)$，然后 $x_{n+1} = g(x_n)$。收敛条件：$\lvert g'(\alpha) \rvert < 1$ 在根 $\alpha$ 附近成立。
3. **牛顿法 / 牛顿-拉夫森**（Newton-Raphson）— $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$。**收敛速度极快**（二阶收敛——正确小数位数每步翻倍），但有时会"跑飞"。

**深层主题**：以上三种方法都是"迭代+寻找不动点"的特例。理解 *为什么* 收敛（Banach 不动点定理）比记住具体公式重要得多。

中文教材里这一章通常叫"非线性方程的数值解"，侧重计算技巧。本卡兼顾计算技巧 + 收敛分析 + 几何直觉 + 跨学科应用（数值分析 / 控制论 / 机器学习里的优化都建立在这之上）。

---

## §1 Why We Need Numerical Methods

Most equations encountered in physics, engineering, and applied mathematics **do not have closed-form roots**. Examples:

- $\cos x = x$ — fundamental in iteration theory, no algebraic solution.
- $x^5 - x + 1 = 0$ — quintic with no formula (Abel–Ruffini 1824, see [[Substitution Equations]] beyond-syllabus).
- $e^x = 3x$ — transcendental equation appearing in radiation physics.
- $\tan x = x$ — eigenvalue equations in quantum wells and waveguides.
- *Almost any equation arising from a real-world model with three or more terms.*

The closed-form-solvable equations you learned in IGCSE and AS-level (linears, quadratics, factorable cubics) are the rare special cases. **The vast majority of equations are solved numerically in practice.**

This is true even outside mathematics: every time your calculator computes $\sqrt{2}$ or $\sin(1.3)$ or $\log(7)$, it is running a numerical iteration (typically Newton-Raphson or CORDIC) under the hood. The button labelled "$\sqrt{\,}$" hides an algorithm that converges in 5–10 steps to 16-digit precision. Floating-point standards specify the algorithms.

So numerical methods are not a niche topic — they are *how computation happens everywhere*. 9709 P3 covers the three foundational methods. Everything in numerical analysis is built on this base.

> [!info] Closed-form solvability is the exception, not the rule
> **Abel–Ruffini (1824)** proved no general algebraic formula exists for polynomial equations of degree $\geq 5$. **Liouville (1840s)** extended this: most integrals lack elementary antiderivatives (see [[Standard Integrals]] beyond-syllabus). **Almost no transcendental equations** ($e^x = x + 2$, etc.) have closed-form roots. Numerical methods aren't *fall-back* — they're *primary*.

---

## §2 The Bisection Method

The simplest method, and the most reliable. Based on the **Intermediate Value Theorem**: if $f$ is continuous on $[a, b]$ and $f(a)$ and $f(b)$ have *opposite signs*, then $f$ has a root in $(a, b)$.

### Algorithm

1. **Locate.** Find an interval $[a, b]$ with $f(a) \cdot f(b) < 0$ (i.e., a sign change). Often done by tabulation: compute $f$ at integer values, look for the change.
2. **Halve.** Compute the midpoint $m = \tfrac{a + b}{2}$ and evaluate $f(m)$.
3. **Pick the half with the sign change.** If $f(a) \cdot f(m) < 0$, the root lies in $[a, m]$ — set $b := m$. Otherwise it lies in $[m, b]$ — set $a := m$.
4. **Repeat** until $b - a < \epsilon$ (your desired precision).

### Worked example — root of $x^3 - x - 1 = 0$

Tabulate $f(x) = x^3 - x - 1$:
- $f(1) = 1 - 1 - 1 = -1$
- $f(2) = 8 - 2 - 1 = 5$ ← sign change in $[1, 2]$

| Iteration | $a$ | $b$ | $m$ | $f(m)$ | sign |
|---|---|---|---|---|---|
| 1 | $1.000$ | $2.000$ | $1.500$ | $0.875$ | $+$ → root in $[1, 1.5]$ |
| 2 | $1.000$ | $1.500$ | $1.250$ | $-0.297$ | $-$ → root in $[1.25, 1.5]$ |
| 3 | $1.250$ | $1.500$ | $1.375$ | $0.224$ | $+$ → root in $[1.25, 1.375]$ |
| 4 | $1.250$ | $1.375$ | $1.3125$ | $-0.052$ | $-$ → root in $[1.3125, 1.375]$ |
| 5 | $1.3125$ | $1.375$ | $1.3438$ | $0.083$ | $+$ → root in $[1.3125, 1.3438]$ |

After 5 iterations, the root is in an interval of width $\approx 0.031$. To reach width $10^{-6}$, you need about 20 iterations (since $2^{20} \approx 10^6$).

True value: $1.32472\ldots$ (the **plastic ratio**, a famous algebraic number).

![[bisection-interval-halving.svg|697]]
*Bisection visualised. Starting bracket $[1, 2]$ halves every iteration, locking onto whichever half contains the sign change. After 7 iterations the bracket width is $1/128 \approx 0.0078$. The cascade of progressively shorter blue brackets, each with its amber midpoint, makes the **one-bit-per-step** convergence rate visible. Slow but bulletproof — bisection cannot fail if you start with a valid sign change.*

### Convergence rate

The interval width is halved each step: $b_n - a_n = (b_0 - a_0) / 2^n$. So to reach precision $\epsilon$ requires $n \geq \log_2\dfrac{b_0 - a_0}{\epsilon}$ iterations. **Linear convergence with rate $1/2$.** Reliable, slow.

> [!tip] Bisection is the locate-step for fancier methods
> In practice you rarely run bisection alone — it's the *bracketing* step. Find a sign-change interval via tabulation or bisection, get one or two correct digits, *then* switch to Newton-Raphson for the rapid finish. Bisection's job is to get you close enough that the faster methods don't fly off.

---

## §3 Fixed-Point Iteration

Rewrite $f(x) = 0$ as $x = g(x)$ for some function $g$. A root of $f$ is then a **fixed point** of $g$ — a value $\alpha$ with $g(\alpha) = \alpha$.

The iteration: pick a starting guess $x_0$, then

$$\boxed{\;x_{n+1} = g(x_n)\;}$$

If the sequence $x_0, x_1, x_2, \ldots$ converges to some limit $\alpha$, then by continuity $\alpha = g(\alpha)$ — and $\alpha$ is a root of the original equation. Whether it converges depends on $g$ and on $x_0$.

### The convergence criterion

The iteration $x_{n+1} = g(x_n)$ converges to $\alpha$ (from a starting point sufficiently close to $\alpha$) **if and only if**

$$\boxed{\;\lvert g'(\alpha) \rvert < 1\;}$$

When this holds, the error contracts at a rate roughly $\lvert g'(\alpha) \rvert$ per step. **Linear convergence.**

**Proof sketch.** Let $e_n = x_n - \alpha$. Then $x_{n+1} = g(x_n) = g(\alpha + e_n) \approx g(\alpha) + g'(\alpha) e_n = \alpha + g'(\alpha) e_n$ (Taylor). So $e_{n+1} \approx g'(\alpha) e_n$. If $\lvert g'(\alpha) \rvert < 1$, errors shrink; if $\lvert g'(\alpha) \rvert > 1$, errors grow.

### Worked example — $\cos x = x$

Rearrange as $x = \cos x$, so $g(x) = \cos x$. Starting from $x_0 = 1$:

| $n$ | $x_n$ |
|---|---|
| 0 | $1.0000$ |
| 1 | $\cos 1 = 0.5403$ |
| 2 | $\cos 0.5403 = 0.8576$ |
| 3 | $\cos 0.8576 = 0.6543$ |
| 4 | $\cos 0.6543 = 0.7935$ |
| 5 | $\cos 0.7935 = 0.7014$ |
| ... | (continuing) |
| 50 | $0.7390851\ldots$ |

It works! Slowly. Convergence rate: $g'(\alpha) = -\sin\alpha \approx -\sin(0.739) \approx -0.674$. So errors shrink by a factor of $\approx 0.67$ per step. About 50 iterations for 6 decimal places.

### Worked example — choosing the right rearrangement

For $x^3 - x - 1 = 0$, there are several ways to rearrange into $x = g(x)$:

| Rearrangement | $g(x)$ | $g'(\alpha)$ at $\alpha \approx 1.3247$ | Converges? |
|---|---|---|---|
| $x = x^3 - 1$ | $x^3 - 1$ | $3\alpha^2 \approx 5.26$ | **No** (rate $> 1$) |
| $x = \sqrt[3]{x + 1}$ | $(x+1)^{1/3}$ | $\tfrac{1}{3}(x+1)^{-2/3} \approx 0.190$ | **Yes** (fast) |
| $x = 1/(x^2 - 1)$ | $1/(x^2-1)$ | $-2x/(x^2-1)^2 \approx -4.78$ | **No** (rate $> 1$) |

The same equation, three rearrangements, *two of them diverge*. **The choice of $g$ is the whole strategy.** A good rearrangement is one where $\lvert g'(\alpha) \rvert$ is small, ideally near $0$.

![[cobweb-fixed-point-iteration.svg|697]]
*The cobweb diagram visualises why. Left: $g_1(x) = \sqrt[3]{x+1}$ with $|g'(\alpha)| \approx 0.19 < 1$ — the cobweb staircase **shrinks** each step, spiralling inward toward the fixed point at the intersection of $y = g(x)$ and $y = x$. Right: $g_2(x) = x^3 - 1$ with $|g'(\alpha)| \approx 5.26 > 1$ — the cobweb staircase **grows** each step, marching away from the same fixed point and off the chart. **Same equation, same root, opposite behaviour — entirely because of the slope of $g$ at $\alpha$.***

This is the §3.6 trap on 9709 P3: a question will give you a rearrangement $x = g(x)$ and ask you to verify it converges (compute $g'$ at the root or in a small neighbourhood, show $\lvert g' \rvert < 1$) **before** iterating. Forgetting the verification step costs marks.

> [!warning] Always check $\lvert g' \rvert < 1$ before iterating
> A rearrangement $x = g(x)$ does *not automatically converge*. You must verify $\lvert g'(\alpha) \rvert < 1$ at the root (or, more practically, on the interval containing the root). If the verification fails, the iteration will diverge no matter how close you start. *Always show this verification step on the exam; it is worth 1–2 marks.*

---

## §4 Newton-Raphson

The fastest of the three. Each iteration computes:

$$\boxed{\;x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}\;}$$

**Geometric interpretation.** At the current guess $(x_n, f(x_n))$, draw the [[Tangents and Normals|tangent line]] to the curve. The tangent has slope $f'(x_n)$, so it crosses the $x$-axis at $x_n - f(x_n)/f'(x_n)$. That's the next guess $x_{n+1}$. *Each step you replace the curve by its tangent and solve the linear equation exactly.*

### Worked example — $\sqrt{2}$ via Newton-Raphson

To compute $\sqrt{2}$, solve $f(x) = x^2 - 2 = 0$. Then $f'(x) = 2x$ and the iteration is:

$$x_{n+1} = x_n - \dfrac{x_n^2 - 2}{2x_n} = \dfrac{x_n + 2/x_n}{2}.$$

(This is the "average of $x$ and $2/x$" — the ancient Babylonian formula, in use since 1800 BC.)

Starting from $x_0 = 1$:

| $n$ | $x_n$ | digits correct |
|---|---|---|
| 0 | $1.000000000000000$ | 0 |
| 1 | $1.500000000000000$ | 1 |
| 2 | $1.416666666666667$ | 3 |
| 3 | $1.414215686274510$ | 5 |
| 4 | $1.414213562374690$ | 11 |
| 5 | $1.414213562373095$ | 16 (machine precision) |

**Five iterations gives machine precision.** This is **quadratic convergence**: the number of correct digits roughly doubles each step (1 → 3 → 5 → 11 → 16). That's the cheetah.

![[newton-raphson-tangent-iteration.svg|697]]
*The geometry, animated. **Left:** finding $\sqrt{2}$ via $f(x) = x^2 - 2$ starting from $x_0 = 2$. Each step draws the tangent at the current iterate, follows it down to the x-axis, that's the next iterate. The four iterates **pile up** at $\sqrt{2}$ — visually you can barely separate them, which is what quadratic convergence looks like (digit-doubling is visible as label-stacking). **Right:** the pathological case. Starting from $x_0 = 0$ on $f(x) = x^3 - 2x + 2$, the iteration produces $0 \to 1 \to 0 \to 1 \to \ldots$ forever. The tangent at $(0, 2)$ has slope $-2$ and points to $x = 1$; the tangent at $(1, 1)$ has slope $1$ and points back to $x = 0$. The iteration **cycles**, never approaching the true root (off to the left at $x \approx -1.769$). Newton-Raphson without bracketing can fall into periodic orbits — one of the classic failure modes.*

### Quadratic convergence — why it doubles

Let $e_n = x_n - \alpha$. A Taylor expansion of $f$ around $\alpha$ gives (with $f(\alpha) = 0$):

$$f(x_n) = f'(\alpha) e_n + \tfrac{1}{2} f''(\alpha) e_n^2 + O(e_n^3)$$
$$f'(x_n) = f'(\alpha) + f''(\alpha) e_n + O(e_n^2)$$

Newton-Raphson step:

$$e_{n+1} = e_n - \dfrac{f(x_n)}{f'(x_n)} = \dfrac{f''(\alpha)}{2 f'(\alpha)} \, e_n^2 + O(e_n^3).$$

**The error squared is the new error.** If $e_n = 10^{-3}$, then $e_{n+1} \sim 10^{-6}$. If $e_{n+1} = 10^{-6}$, then $e_{n+2} \sim 10^{-12}$. Number of correct digits doubles each step. *That's what makes Newton-Raphson devastatingly fast when it works.*

> [!info] Newton-Raphson is the ancestor of every machine-learning optimiser
> The Newton-Raphson update rule $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$ — *step from your current guess using local slope information* — is the foundational pattern behind **gradient descent** and every modern AI training algorithm. The connection runs through one observation: *finding a root of $f$ is the same problem as finding a critical point of $g$ where $g' = f$.* Apply NR to $g'(x) = 0$ and the iteration becomes
>
> $$x_{n+1} = x_n - \dfrac{g'(x_n)}{g''(x_n)}$$
>
> — **Newton's method for optimisation.** Each step jumps to the minimum of the *local quadratic approximation* (the parabola tangent to $g$ at $x_n$). Brilliant convergence; uses the second derivative $g''$.
>
> **Gradient descent is Newton's method with the second derivative *replaced by a constant*** (the learning rate $\eta$):
>
> $$\mathbf{x}_{n+1} = \mathbf{x}_n - \eta\, \nabla g(\mathbf{x}_n).$$
>
> You step in the direction of steepest descent. You don't need to know how curved the landscape is — you just take small steps. The tradeoff: simpler (no Hessian to compute), slower (linear instead of quadratic convergence), but *scalable to billions of parameters* because the inverse Hessian is impractical for neural networks. Every neural network in the world — GPT, Stable Diffusion, AlphaFold — is trained by a descendant of gradient descent: **Adam, RMSProp, AdaGrad, L-BFGS** all use the gradient $\nabla g$ in place of the Newton step, with various adaptive learning-rate schemes that try to recover *some* of the curvature information Newton's method would have used directly.
>
> So when you watch the Newton-Raphson tangent animation above, you're watching the geometric template of every modern ML training run — *one step from the current parameter values, in the direction the local slope suggests, hoping to land closer to the minimum.* The animation in the convergent panel — iterates piling up at the root — is what a successful AI training run looks like in one dimension. The animation in the pathological panel — cycling between 0 and 1 forever — is what happens when training fails to converge.
>
> The 1669 algorithm and the 2026 GPU compute cluster are *the same algorithm*, separated by 357 years and a Hessian approximation.

### When Newton-Raphson fails

The method requires $f'(x_n) \neq 0$ at every step. If the tangent at $x_n$ is nearly horizontal, the tangent line crosses the $x$-axis very far away — and the next iterate flies off into wildness. Failure modes:

- **Horizontal tangent.** $f'(x_n) = 0$: division by zero, iteration breaks.
- **Inflection-point neighbourhood.** Tangent is nearly horizontal: $x_{n+1}$ shoots far away.
- **Cycling.** The sequence enters a periodic orbit and never converges.
- **Wrong root.** With a far-away start, NR might converge to a *different* root than the one you wanted.

**Robust workflow:** locate the root by bisection or tabulation (get 1–2 digits), then switch to Newton-Raphson for the rapid finish. NR alone, without bracketing, is dangerous.

> [!info] Newton fractals — beyond syllabus, beautiful
> Apply Newton-Raphson to a complex polynomial like $f(z) = z^3 - 1$ (whose roots are the three [[Euler's Formula and De Moivre's Theorem|cube roots of unity]]: $1, e^{2\pi i/3}, e^{4\pi i/3}$). From each starting point $z_0 \in \mathbb{C}$, the iteration converges to *one* of the three roots. Colour each $z_0$ by which root it lands on. The resulting picture is the **Newton fractal** — a self-similar boundary structure between the three "basins of attraction," with detail at every scale. The boundary is *not* a smooth curve; it's a fractal of Hausdorff dimension between 1 and 2.
>
> The same beautiful divergence behaviour occurs in real Newton-Raphson too: change $x_0$ slightly, the iteration might converge to a different root. Just less visible.

---

## §5 Comparing the Three

| Method | Convergence | Reliability | Speed | When to use |
|---|---|---|---|---|
| Bisection | Linear, rate $1/2$ | Always (with sign change) | Slow ($\sim 20$ iter for 6dp) | Locate, then switch |
| Fixed-point | Linear, rate $\lvert g'(\alpha) \rvert$ | Conditional on $\lvert g' \rvert < 1$ | Medium | Common in P3 — check the rearrangement first |
| Newton-Raphson | **Quadratic** | Conditional on $f'$ non-vanishing | **Fast ($\sim 5$ iter for 6dp)** | After bracketing |

**The hidden hierarchy.** All three are instances of *fixed-point iteration*:

- Bisection: $g(a, b) = (a, m)$ or $(m, b)$ depending on signs (a fixed point of the bracket-narrowing map).
- Direct fixed-point: $g$ is the rearrangement function.
- Newton-Raphson: $g_{NR}(x) = x - f(x)/f'(x)$. At a simple root $\alpha$, you can verify $g_{NR}'(\alpha) = 0$ — which is *why* NR converges quadratically. Linear FPI is "$g'$ small at root"; NR sets $g'$ exactly to zero at root, getting a free order-of-magnitude.

This is the deepest single observation in P3 §3.6: *Newton-Raphson is a fixed-point iteration whose $g$ has been engineered to satisfy $g'(\alpha) = 0$, killing the linear error term and leaving quadratic.*

---

## §6 Common Misconceptions

### 1. Iterating without verifying convergence

The student is given $x = g(x)$ and immediately iterates from $x_0$. The sequence diverges. Marks lost.

**Fix.** Before iterating, *verify $\lvert g'(\alpha) \rvert < 1$* (or on the interval containing the root). If $\lvert g' \rvert > 1$ anywhere near the root, the iteration won't converge. Show the verification — usually 1–2 marks of the question.

### 2. Choosing the wrong rearrangement

Given $f(x) = 0$, the student picks the most algebraically obvious rearrangement (e.g., $x = $ leading-term-isolated) and ends up with a divergent $g$.

**Fix.** Different rearrangements have different $\lvert g'(\alpha) \rvert$. *Compute $g'$ for each candidate rearrangement, pick the one with $\lvert g'(\alpha) \rvert$ closest to $0$.* The rearrangement that isolates the *highest power* on the left usually gives small $g'$; the rearrangement that isolates the *lowest power* usually gives large $g'$.

### 3. Newton-Raphson without locating first

The student starts NR from a wild guess. The tangent slope is nearly zero. The iteration flies off and either diverges or converges to a wrong root.

**Fix.** *Bracket the root first* — use tabulation or one bisection step to get one good digit. Then switch to NR. NR alone is unreliable.

### 4. Insufficient precision in iteration

The student writes down each iterate to 3 decimal places, then iterates. The final answer is contaminated by accumulated round-off.

**Fix.** *Carry more decimal places than the question asks for.* If the final answer needs 4 decimal places of accuracy, carry 6–7 decimal places through every iteration. Round only at the end.

### 5. Confusing "sign change" with "monotone crossing"

The student finds $f(1) < 0$ and $f(2) > 0$, applies bisection, but the function has *two* roots in $[1, 2]$ — and the bisection finds *neither* because the midpoint values happen to match the wrong signs.

**Fix.** Bisection requires *exactly one* root in $[a, b]$ for guaranteed correctness. If the function is monotone (continuous + strictly increasing or strictly decreasing), this is automatic. Otherwise, *check by plotting* before assuming bisection will find your intended root.

### 6. Stopping criterion confusion

The student stops "when $x_n$ and $x_{n+1}$ agree to 4 decimal places" and thinks the answer is accurate to 4 decimal places. *Not always true* — for slow convergence, the iterates can creep along while the actual error is much larger than the step.

**Fix.** Use the *true* stopping criterion: $\lvert x_{n+1} - x_n \rvert < \epsilon \cdot (1 - r)$ where $r$ is the contraction rate. For exam purposes, just check that *several consecutive iterates* agree to your target precision, not just two.

---

## §7 Exam Notes

### Cambridge 9709 (A-Level)

**Syllabus refs:** P3 §3.6 — *numerical solution of equations*. Lists:
- Sign-change location and bisection (briefly).
- Fixed-point iteration $x_{n+1} = F(x_n)$ — checking convergence by considering $\lvert F'(\alpha) \rvert$ at or near the root.
- Newton-Raphson iteration $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$.
- Showing that an iteration converges to a stated root (and stating an interval where the iteration is valid).

**Typical question shape (8–12 marks):**
1. *Show that the equation $f(x) = 0$ has a root in $[a, b]$.* (1–2 marks: compute $f(a)$, $f(b)$, observe sign change, cite continuity.)
2. *Show that the equation can be rearranged as $x = g(x)$.* (1 mark — algebra.)
3. *Use the iteration $x_{n+1} = g(x_n)$ with starting value $x_0 = \ldots$ to find the root correct to $N$ decimal places.* (4–6 marks: tabulate iterates, identify when consecutive iterates agree.)
4. *Optionally: verify $\lvert g'(\alpha) \rvert < 1$ at the root.* (1–2 marks.)

**Or — Newton-Raphson variant:**
1. *Show that the Newton-Raphson iteration for $f(x) = 0$ gives $x_{n+1} = \ldots$.* (2 marks: substitute into the general formula.)
2. *Apply with starting value $x_0$.* (3–5 marks: iterate, identify when converged.)

**Tip.** *Always show enough iterates to be convincing that you've converged* — typically 4–5 iterates with the final two agreeing to the required precision. Showing only 2–3 iterates often loses a mark for "insufficient evidence of convergence."

### Cambridge 0606

**Not in the 0606 syllabus.** Numerical methods is A-Level material; the 0606 student stops at closed-form solving (quadratics, cubics via factor theorem, etc.).

### A-Level (Edexcel / AQA / OCR / MEI)

Edexcel and AQA A-Level Pure include numerical methods in **Year 13 (A2) Pure**. Edexcel covers bisection, fixed-point iteration, and Newton-Raphson explicitly; AQA covers fixed-point iteration and Newton-Raphson, with bisection as a brief introductory technique. OCR's MEI Further Pure adds the **Secant method** (approximate Newton-Raphson where $f'(x_n)$ is replaced by a difference quotient).

### IB AA HL

**Topic 5 (Calculus)** in the AA HL syllabus includes Newton-Raphson and fixed-point iteration as part of the broader differential-calculus toolkit. The IB formula booklet does **not** give the Newton-Raphson formula — you're expected to know it. AA SL does not test numerical methods.

### AP Calculus

**AP Calculus BC** explicitly tests:
- Tangent-line approximation (the *single-step* version of Newton-Raphson — using one tangent step to estimate $f(x_0 + h)$).
- Euler's method for differential equations (which is essentially fixed-point iteration for ODEs — see [[Differential Equations]]).

Bisection and full Newton-Raphson iteration are *not* AP topics. **AP Calculus AB** does not test any of this.

### Beyond high school — University

Numerical methods is its own full undergraduate subject (Numerical Analysis), typically a one-semester course. Standard topics extending §3.6:

- **Secant method** — Newton-Raphson with $f'(x_n)$ replaced by $\dfrac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$. **Superlinear convergence** (rate $\approx 1.618$, the golden ratio!). Useful when $f'$ is hard to compute.
- **Müller's method** — fits a quadratic through three points; handles complex roots.
- **Brent's method** — combines bisection (reliability) with secant/inverse-quadratic (speed). The default in `scipy.optimize.brentq`.
- **Householder methods** — higher-order generalizations of Newton (cubic, quartic convergence at higher computational cost).
- **Banach Fixed-Point Theorem** — the abstract framework: any contraction map on a complete metric space has a unique fixed point, found by iteration. The convergence statement for FPI is a special case.
- **Newton's method for systems** — $\mathbf{x}_{n+1} = \mathbf{x}_n - J^{-1}(\mathbf{x}_n) F(\mathbf{x}_n)$ using the Jacobian matrix. Foundation of nonlinear optimisation and machine learning training.

The hierarchy goes: 9709 §3.6 is the entry point. Numerical Analysis 101 builds the next layer. Optimisation, Numerical PDEs, Machine Learning training all sit on top.

---

## Connections

- **Direct prerequisite:** [[Differentiation]] + [[Differentiation Rules]] — needed for Newton-Raphson ($f'$) and for the convergence criterion of fixed-point iteration ($g'$).
- **Direct prerequisite:** [[Tangents and Normals]] — Newton-Raphson is geometrically a tangent-line construction.
- **Direct prerequisite:** [[Sequences]] — the iteration produces a sequence $x_0, x_1, x_2, \ldots$ whose limit is the root.
- **Direct prerequisite:** [[Function]] — fixed-point and root concepts depend on understanding $f : \mathbb{R} \to \mathbb{R}$.
- **Lemma:** *Intermediate Value Theorem* (planned card, W7 in queue) — the foundational result behind bisection. Stating "sign change implies a root exists" cites IVT.
- **Application:** [[Differential Equations]] — Euler's method for solving $y' = f(x, y)$ numerically is iterative; the algorithmic structure parallels fixed-point iteration. Many ODE solvers are descendants of the methods in this card.
- **Application:** [[Standard Integrals]] — Simpson's rule and other numerical integration methods are the integration counterparts of these root-finding methods.
- **Application — beyond syllabus:** Newton's method on complex polynomials gives the **Newton fractals** — basins of attraction with self-similar boundaries. Connects to [[Complex Numbers]] and [[Euler's Formula and De Moivre's Theorem]].
- **Application — beyond syllabus:** Every iterative optimisation algorithm in machine learning (gradient descent, Adam, L-BFGS) is a fixed-point iteration. Newton's method for systems is the foundational step.
- **Closes:** 9709 P3 §3.6 — the last 🔴 row in the P3 map.
- **For 9709 students:** [[MF19 Reference (9709)]] — the Newton-Raphson formula is *not* on the MF19 sheet. Memorise it.

---

## Beyond Syllabus

### Banach Fixed-Point Theorem — the abstract framework

All three numerical methods in this card are instances of one abstract result: the **Banach Fixed-Point Theorem (1922)**.

**Statement.** Let $(X, d)$ be a complete metric space and $T : X \to X$ be a *contraction map* — a function such that there exists a constant $0 \leq k < 1$ with $d(T(x), T(y)) \leq k \cdot d(x, y)$ for all $x, y \in X$. Then:
1. $T$ has a *unique* fixed point $\alpha$ (a point with $T(\alpha) = \alpha$).
2. For *any* starting point $x_0 \in X$, the sequence $x_n = T^n(x_0)$ converges to $\alpha$.
3. The convergence rate is at least $d(x_n, \alpha) \leq k^n d(x_0, \alpha)$.

**Why this is the master theorem.** Fixed-point iteration $x_{n+1} = g(x_n)$ is exactly the setup. The convergence criterion $\lvert g'(\alpha) \rvert < 1$ is the local form of "contraction" — for $x$ near $\alpha$, $\lvert g(x) - g(\alpha) \rvert \approx \lvert g'(\alpha) \rvert \cdot \lvert x - \alpha \rvert$, so $g$ contracts by factor $\lvert g'(\alpha) \rvert$. If that's less than $1$, Banach guarantees convergence.

Banach's theorem also underwrites:
- Existence and uniqueness of solutions to ODEs (Picard-Lindelöf theorem).
- Inverse Function Theorem.
- Existence of equilibrium prices in mathematical economics.
- Convergence proofs for most iterative algorithms.

It's one of the most-cited theorems in 20th-century mathematics.

### Newton's Method on Complex Polynomials — the Fractal

Apply Newton-Raphson in $\mathbb{C}$ to $f(z) = z^3 - 1$. The roots are the cube roots of unity: $1, \omega = e^{2\pi i / 3}, \omega^2 = e^{4\pi i / 3}$.

Starting from $z_0 \in \mathbb{C}$, the iteration converges to *one* of the three roots — but *which one* depends sensitively on $z_0$. Colour each starting point by its destination root, and you get the **Newton fractal**: three intricately interwoven basins of attraction, with fractal boundaries between them.

The boundaries have a beautiful self-similar property: arbitrarily close to any boundary point, you find regions belonging to *all three* basins. This is the **Wada property** — three open sets sharing a common boundary, despite being disjoint. Discovered by Cayley in 1879 (he conjectured the pattern; full understanding came in the 1980s with the development of complex dynamics by Sullivan, Douady, Hubbard).

Newton fractals were among the first computer-generated mathematical art (1980s). They remain a standard demonstration in graduate complex-dynamics courses.

### Why $g'(\alpha) = 0$ Buys You an Order of Magnitude

Linear fixed-point iteration: $\lvert e_{n+1} \rvert \approx \lvert g'(\alpha) \rvert \cdot \lvert e_n \rvert$. Errors shrink linearly.

Newton-Raphson has $g_{NR}(x) = x - f(x)/f'(x)$. Compute $g_{NR}'(\alpha)$ at a simple root:

$$g_{NR}'(x) = 1 - \dfrac{f'(x)^2 - f(x)f''(x)}{f'(x)^2} = \dfrac{f(x) f''(x)}{f'(x)^2}.$$

At a simple root $\alpha$ where $f(\alpha) = 0$ and $f'(\alpha) \neq 0$: **$g_{NR}'(\alpha) = 0$.**

This is the load-bearing fact. *Newton-Raphson is fixed-point iteration designed so that the derivative of the iteration function vanishes at the root.* The linear error term disappears; what's left is the quadratic. That's why each step doubles the digits.

There's also a higher-order variant (**Halley's method**) where $g'(\alpha) = g''(\alpha) = 0$ — cubic convergence, triples the digits each step. The cost: Halley uses $f''$, requiring an extra differentiation. Beyond 9709 syllabus, standard in graduate numerical analysis.

### The Babylonian Method for $\sqrt{a}$

The Newton-Raphson iteration for $x^2 - a = 0$ simplifies to $x_{n+1} = \dfrac{x_n + a/x_n}{2}$ — the average of $x_n$ and $a/x_n$. This was the algorithm Babylonian scribes used 4000 years ago to compute square roots. Clay tablets from c. 1800 BC show students working out $\sqrt{2}$ to 5 sexagesimal digits (about 7 decimal digits) using this exact formula.

The Babylonians had no calculus. They didn't know about tangent lines, didn't know about derivatives, didn't know about quadratic convergence. They had **the formula** and the empirical observation that it worked. *They were running Newton-Raphson 3300 years before Newton.*

When Newton "invented" his method in 1669, he was rediscovering a Babylonian special case in a general framework. The history of mathematics has more of this than you'd guess.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $x_{n+1} = g(x_n)$ | `x_{n+1} = g(x_n)` | Fixed-point iteration |
| $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$ | `x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}` | Newton-Raphson formula |
| $\lvert g'(\alpha) \rvert < 1$ | `\lvert g'(\alpha) \rvert < 1` | The convergence criterion for FPI |
| $f(a) \cdot f(b) < 0$ | `f(a) \cdot f(b) < 0` | Sign-change condition for bisection |
| $e_{n+1} \approx \dfrac{f''(\alpha)}{2f'(\alpha)} e_n^2$ | (as written) | Newton-Raphson quadratic-convergence formula |
| $T : X \to X$ | `T : X \to X` | Banach fixed-point setup (beyond syllabus) |
