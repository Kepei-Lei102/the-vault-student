---
chinese: 夹逼定理 (jiā bī dìnglǐ)
prerequisites:
  - "[[Limit]]"
  - "[[Trigonometric Functions]]"
  - "[[Radians]]"
  - "[[Inequalities (Vocab)]]"
  - "[[L'Hôpital's Rule]]"
leads_to:
  - "[[Differentiation Rules]]"
  - "[[Sequences and Series]]"
  - "[[Multivariable Limits]]"
tags:
  - subject/mathematics
  - domain/calculus
  - domain/limits
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/IB-AA
  - curriculum/AP-Calculus-BC
  - syllabus/AP-Calculus-BC-1-8
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/inequality-chain
  - misconception/squeeze-needs-only-one-bound
  - misconception/bounds-can-converge-to-different-limits
  - misconception/f-must-be-defined-at-the-point
  - misconception/squeeze-and-sandwich-different-theorems
---

# Squeeze Theorem 夹逼定理

## Definition

The **Squeeze Theorem** is a tool for proving that a function has a particular limit by **bounding it between two functions that share that limit**.

Formally: if $g(x) \leq f(x) \leq h(x)$ for all $x$ near a point $a$ (but possibly not at $a$ itself), and

$$\lim_{x \to a} g(x) \;=\; \lim_{x \to a} h(x) \;=\; L,$$

then

$$\boxed{\;\lim_{x \to a} f(x) \;=\; L.\;}$$

The function $f$ is "squeezed" or "sandwiched" between $g$ and $h$, both of which converge to the same value $L$. Since $f$ is trapped between them and the trap is closing on $L$, **$f$ has nowhere else to go.**

Three things to notice:

- The function $f$ **doesn't need a closed form** at $a$. It doesn't even need to be defined at $a$. All that matters is the inequality $g \leq f \leq h$ in a neighbourhood of $a$, plus the convergence of $g$ and $h$.
- The bounds $g$ and $h$ must converge to **the same** limit $L$. If $g \to L_1$ and $h \to L_2$ with $L_1 \neq L_2$, the theorem says nothing — $f$ could oscillate forever between them.
- The squeeze is a **proof tool**, not a computational shortcut. You still need to *find* the bounds $g$ and $h$ and prove they converge. The art is in the choice.

### 中文锚点

**夹逼定理 (jiā bī dìnglǐ)** = 如果 $g(x) \leq f(x) \leq h(x)$ 并且 $g$ 与 $h$ 都收敛到同一个极限 $L$，那么夹在中间的 $f$ 也必然收敛到 $L$。

| English | 中文 | Note |
|---|---|---|
| Squeeze Theorem | 夹逼定理 | The standard Chinese name |
| Sandwich Theorem | 三明治定理 (sānmíngzhì dìnglǐ) | Western nickname; same theorem |
| Pinching Theorem | 钳逼定理 (qián bī dìnglǐ) | Older Western name |
| Lower bound | 下界 (xià jiè) | The $g(x)$ |
| Upper bound | 上界 (shàng jiè) | The $h(x)$ |
| Trapped between | 夹在中间 / 介于…之间 | The inequality $g \leq f \leq h$ |

中文数学教材标准用「夹逼定理」这个名字，**这是英文 "Squeeze Theorem" 的直译**。少数旧教材会写「夹逼准则」(zhǔn zé, "criterion")，意思一样。中文常常配合「三明治」这个口语化的比喻——函数 $f$ 像三明治里的火腿，被上下两片面包夹住。

考试角度：
- 9709 Cambridge A-Level **不直接考夹逼定理**，但 §3.4 的 $(\sin x)' = \cos x$ 推导依赖于 $\sin h / h \to 1$，而这个极限的标准证明就是夹逼。
- IB AA HL 显式包含这个定理。
- AP Calculus BC §1.8 显式名为 "Squeeze Theorem"。

---

## Why the squeeze works — and why this matters

Many limits cannot be computed directly because the function doesn't have a meaningful value at $a$. The most famous example is $\lim_{h \to 0} \frac{\sin h}{h}$: plugging in $h = 0$ gives the indeterminate $0/0$, and there's no algebraic trick to simplify the expression. We *need* a different approach.

The Squeeze Theorem provides one: **find a simpler function below $f$ and a simpler function above $f$, both with limits you CAN compute, and let geometry close the trap.** The "simpler" bounds are often inequalities that come from geometry, algebra, or just the boundedness of one piece of the expression.

> [!info] The hunter trace this card teaches
> When you can't compute a limit directly, **find bounds**. This is the general strategy. The Squeeze Theorem formalises *"if it's trapped between two things converging to the same place, it converges to that place."* Once you've internalised this move, you start using it everywhere — in defining $e$, in proving convergence of series, in higher-dimensional limits, in measure theory. The squeeze is the analyst's universal hammer.

### A moment of visual intuition

Watch the bounds close in. The particle wants to be free — but as $g$ and $h$ converge to the same value, the *room* the particle is allowed to live in shrinks to a single point. When the two bounds meet, "left bound" and "right bound" are no longer two things; they are one and the same point. The particle has no choice — it *is* that point.

![[squeeze-theorem-vise.svg|697]]

That is the whole theorem in one image. Everything below — the $\epsilon$-$\delta$ machinery, the canonical $\sin h / h$ application, the dominated convergence generalisation — is just careful bookkeeping for what your eye already understands. The bounds shrank to zero width; "between them" became "exactly them"; $f$ inherited their shared value.

---

## Proof of the theorem

The proof is a clean two-step $\epsilon$-$\delta$ argument. Given any $\epsilon > 0$, we must produce a $\delta > 0$ such that $|f(x) - L| < \epsilon$ whenever $0 < |x - a| < \delta$.

Since $g(x) \to L$ as $x \to a$, there exists $\delta_1 > 0$ such that

$$|g(x) - L| < \epsilon \quad \text{whenever} \quad 0 < |x - a| < \delta_1.$$

Similarly, since $h(x) \to L$, there exists $\delta_2 > 0$ such that

$$|h(x) - L| < \epsilon \quad \text{whenever} \quad 0 < |x - a| < \delta_2.$$

Choose $\delta = \min(\delta_1, \delta_2)$. Then for any $x$ with $0 < |x - a| < \delta$, both inequalities hold simultaneously, which means

$$L - \epsilon \;<\; g(x) \;\leq\; f(x) \;\leq\; h(x) \;<\; L + \epsilon.$$

Reading off the outer terms: $L - \epsilon < f(x) < L + \epsilon$, which is the same as $|f(x) - L| < \epsilon$. We've produced the required $\delta$, so $\lim_{x \to a} f(x) = L$. $\blacksquare$

The proof is **short** because the work is done by the squeeze inequality itself. Once $f$ is trapped between two things both converging to $L$, there's almost nothing left to say — the $\epsilon$-$\delta$ formalism just packages the obvious geometric truth.

---

## The canonical application — $\sin h / h \to 1$ as $h \to 0$

This is THE foundational trigonometric limit. Every derivative of every trig function ultimately depends on it. Without this limit, $(\sin x)' = \cos x$ has no proof; and without that derivative, the rest of calculus on trig functions falls apart.

The Squeeze Theorem is how we prove it. The bounds come from a beautiful geometric argument on the unit circle: for $0 < h < \pi/2$, the area of a small triangle is less than the area of the corresponding circular sector, which is less than the area of a larger tangent triangle.

![[squeeze-theorem-unit-circle.svg|697]]

The three regions (each containing the previous) have areas:

| Region | Area |
|---|---|
| Triangle $OAP$ (where $A = (1,0)$, $P = (\cos h, \sin h)$) | $\tfrac{1}{2}\sin h$ |
| Circular sector $OAP$ (angle $h$ in a unit circle) | $\tfrac{1}{2}h$ |
| Triangle $OAT$ (where $T = (1, \tan h)$) | $\tfrac{1}{2}\tan h$ |

The containment gives:

$$\tfrac{1}{2}\sin h \;\leq\; \tfrac{1}{2}h \;\leq\; \tfrac{1}{2}\tan h \quad \Longrightarrow \quad \sin h \;\leq\; h \;\leq\; \frac{\sin h}{\cos h}.$$

Divide through by $\sin h$ (positive for $0 < h < \pi/2$):

$$1 \;\leq\; \frac{h}{\sin h} \;\leq\; \frac{1}{\cos h}.$$

Take reciprocals (all positive, so the inequalities reverse):

$$\cos h \;\leq\; \frac{\sin h}{h} \;\leq\; 1.$$

This is the squeeze setup. As $h \to 0^+$, $\cos h \to 1$ and the constant $1$ stays at $1$. The Squeeze Theorem yields

$$\lim_{h \to 0^+} \frac{\sin h}{h} \;=\; 1.$$

The same limit holds from the left by symmetry: $\sin(-h)/(-h) = \sin h / h$ since both $\sin$ and the denominator change sign together. Combining: $\lim_{h \to 0} \sin h / h = 1$. $\blacksquare$

> [!info] Why the proof requires radians
> The sector area formula $\frac{1}{2}r^2 \theta$ used above is **only valid when $\theta$ is in radians**. In degrees, the sector area is $\frac{\pi r^2 \theta}{360}$, and the proof above produces $\lim_{h^\circ \to 0} \sin(h^\circ)/h = \pi/180$, not $1$. The deeper reason — *that the radian is a pure number while the degree is a unit* — lives in [[Radians]] §"The deepest reason — degree is a unit, radian is a pure number." The full radian-vs-degree calculus comparison is in [[Radians]] §"Why Calculus Demands Radians." *Together these two sections are the most intuitive answer to why every calculus textbook insists on radians.*

The geometric proof in full — with the figure construction, the area calculations, and the subsequent derivation of $(\sin x)' = \cos x$ — lives in [[Radians]] §"Proof that $\lim_{h \to 0} \sin h / h = 1$". This card states the squeeze theorem in general; Radians applies it to the specific trig case.

---

## Other classic applications

The squeeze theorem's versatility comes from how many ways you can bound things. Here are the canonical other examples.

### Bounded times something going to zero

$$\lim_{x \to 0} x \sin\!\left(\frac{1}{x}\right) \;=\; 0.$$

The function $\sin(1/x)$ oscillates wildly between $-1$ and $1$ as $x \to 0$ — it does **not** have a limit at zero. But the function $x \sin(1/x)$ does, because the $x$ factor crushes the oscillation toward zero. To prove this rigorously:

Since $-1 \leq \sin(1/x) \leq 1$ for every $x \neq 0$, multiplying by $|x|$ (which is $\geq 0$) preserves inequalities:

$$-|x| \;\leq\; x \sin\!\left(\frac{1}{x}\right) \;\leq\; |x|.$$

(Technical note: we have $-|x| \leq x \sin(1/x) \leq |x|$ regardless of the sign of $x$, because $x \sin(1/x)$ is bounded by $|x \sin(1/x)| \leq |x| \cdot 1 = |x|$.)

As $x \to 0$, both $-|x|$ and $|x|$ go to $0$. By the Squeeze Theorem, $x \sin(1/x) \to 0$. $\blacksquare$

**This is the canonical "use squeeze when oscillation is bounded by a vanishing factor" example.** The same pattern handles $x \cos(1/x)$, $x^2 \sin(1/x^3)$, and any product of a vanishing function times a bounded one.

### Sequence version — used in defining $e$

$$\lim_{n \to \infty} \frac{\sin n}{n} \;=\; 0.$$

For any positive integer $n$: $-1 \leq \sin n \leq 1$, so $-1/n \leq (\sin n)/n \leq 1/n$. Both bounds go to $0$. Done.

The sequence form of the Squeeze Theorem is what makes the convergence proof for $\big(1 + \tfrac{1}{n}\big)^n \to e$ work — the proof has four steps (binomial expansion → monotonicity → boundedness → squeeze-style two-sided bound to identify the limit value), with the squeeze theorem doing the work in Step 4. Full proof at [[Euler's Number]] §3 Definition 1; historical setup in [[Stories/The Hidden Number]].

### A trickier example — the cusp

$$\lim_{x \to 0} \frac{x^2 + x^4 \sin(1/x)}{x^2 + x^2 \cos(1/x)} \;=\; ?$$

This one looks impossible. Both numerator and denominator have wildly oscillating parts. But factor an $x^2$ out of each:

$$\frac{x^2 + x^4 \sin(1/x)}{x^2 + x^2 \cos(1/x)} \;=\; \frac{x^2(1 + x^2 \sin(1/x))}{x^2(1 + \cos(1/x))} \;=\; \frac{1 + x^2 \sin(1/x)}{1 + \cos(1/x)}.$$

The numerator $\to 1 + 0 = 1$ by the squeeze argument from earlier ($x^2 \sin(1/x) \to 0$). The denominator $1 + \cos(1/x)$ oscillates between $0$ and $2$ — **it does not converge.** So the limit does *not* exist.

**The lesson:** squeeze only works when the bounds converge. If you tried to apply squeeze to the denominator alone, you'd notice that $\cos(1/x)$ has bounds $-1 \leq \cos(1/x) \leq 1$ that *don't* converge to the same value. The theorem refuses to apply, and the underlying limit really doesn't exist.

---

## Worked examples

### Example 1 — squeeze on a power

Find $\lim_{x \to 0} x^2 \cos\!\left(\frac{1}{x^2}\right)$.

**Solution.** $\cos(1/x^2)$ is bounded: $-1 \leq \cos(1/x^2) \leq 1$. Multiplying by $x^2 \geq 0$:

$$-x^2 \;\leq\; x^2 \cos\!\left(\frac{1}{x^2}\right) \;\leq\; x^2.$$

Both bounds $\to 0$ as $x \to 0$. By Squeeze: limit $= 0$.

### Example 2 — sequence with bounded perturbation

Find $\lim_{n \to \infty} \frac{n + \sin n}{n}$.

**Solution.** Simplify: $\frac{n + \sin n}{n} = 1 + \frac{\sin n}{n}$. We already showed $(\sin n)/n \to 0$. So the limit is $1 + 0 = 1$.

(Alternative direct squeeze: $\frac{n - 1}{n} \leq \frac{n + \sin n}{n} \leq \frac{n + 1}{n}$, both bounds $\to 1$. Same conclusion.)

### Example 3 — the linear-multiplier generalisation

Prove that for any constant $a$:

$$\lim_{x \to 0} \frac{\sin(ax)}{x} \;=\; a.$$

**Solution.** Substitute $u = ax$. As $x \to 0$, $u \to 0$ (assuming $a \neq 0$; the $a = 0$ case is trivial since $\sin 0 / x = 0$). Then $x = u/a$ and

$$\frac{\sin(ax)}{x} \;=\; \frac{\sin u}{u/a} \;=\; a \cdot \frac{\sin u}{u} \;\to\; a \cdot 1 \;=\; a.$$

(Squeeze isn't directly used here — we leveraged the canonical result $\sin u / u \to 1$ derived from squeeze.)

### Example 4 — squeeze with absolute values

Suppose $|f(x) - 3| \leq (x - 2)^2$ for all $x$ near $2$. Find $\lim_{x \to 2} f(x)$.

**Solution.** The condition says $-(x-2)^2 \leq f(x) - 3 \leq (x-2)^2$, i.e. 

$$3 - (x - 2)^2 \;\leq\; f(x) \;\leq\; 3 + (x - 2)^2.$$

Both bounds $\to 3$ as $x \to 2$ (since $(x-2)^2 \to 0$). By Squeeze: $\lim_{x \to 2} f(x) = 3$.

*This is the canonical "we don't know $f$ exactly, but we know how fast it approaches the limit" pattern.* The bound $|f(x) - L| \leq (x - a)^k$ is sometimes called a *rate of convergence* statement.

---

## When the Squeeze Theorem doesn't help

Knowing when a tool *doesn't* apply is as important as knowing when it does. Squeeze fails in three classic situations:

1. **The bounds converge to different limits.** If $-1 \leq f(x) \leq 1$ and $f$ doesn't decide which way to settle, no amount of squeezing helps. Example: $f(x) = \sin(1/x)$ as $x \to 0$ — bounded by $\pm 1$, but oscillates infinitely fast and has no limit at $0$.

2. **You can't find tight enough bounds.** Sometimes the natural bounds are too loose. For $\lim_{x \to 0^+} x \ln x$, the bound $-\infty \leq x \ln x \leq 0$ tells you nothing useful. You need a sharper tool: rewrite as $\ln x / (1/x)$ and apply [[L'Hôpital's Rule]] to get $0$.

3. **The function has discontinuities mixing into your inequality.** If $g$ and $h$ both go to $L$, but somewhere near $a$ they violate $g \leq f \leq h$ (because $f$ has a removable singularity, say), the theorem doesn't apply. Always check the inequality holds *in a neighbourhood* of $a$, not just at scattered points.

> [!tip] Squeeze vs L'Hôpital
> The two main tools for computing limits of indeterminate forms are the Squeeze Theorem and [[L'Hôpital's Rule]]. They divide the labour:
>
> - **L'Hôpital** handles smooth-function quotients of the form $0/0$ or $\infty/\infty$ where both numerator and denominator are differentiable. The technique: differentiate top and bottom, take the limit.
> - **Squeeze** handles cases where the function has a bounded oscillating piece (sin, cos, $(-1)^n$, etc.) multiplying a vanishing factor. The technique: bound the oscillating piece and let the vanishing factor crush it.
>
> Generally: if you can see a sin/cos that doesn't simplify, reach for squeeze. If you see two smooth functions sharing a $0$ or an $\infty$, reach for L'Hôpital. *They rarely overlap; they almost never substitute for each other.*

---

## Exam Notes

### AP Calculus AB / BC — Unit 1.8

- The squeeze theorem is a **named topic**: Unit 1.8, "Determining Limits Using the Squeeze Theorem" (AB and BC alike). The stock exam shape is the bounded-oscillator pattern of Examples 1 and 4 — $x^2\sin(1/x)$ and relatives — plus questions that *hand you* the sandwich inequality and ask you to conclude the limit. Full credit wants both ingredients stated: the two-sided bound holding near the point, *and* the outer limits agreeing.
- $\lim_{h\to 0}\tfrac{\sin h}{h} = 1$ itself is quotable on AP without proof; this card's geometric squeeze is the *why* behind the quoted fact.

### IB AA HL

- The squeeze theorem is **not a named statement** in the AA guide — limits appear informally (5.12) and via l'Hôpital / Maclaurin series (AHL 5.13). A squeeze argument is accepted where valid but never demanded; for IB purposes this card is the honest foundation under the trig limits that first-principles differentiation of $\sin x$ quietly uses.

### Cambridge 9709 / 9231

- **Not examined.** 9709 supplies the trig derivatives ready-made and develops no limit theory; 9231 doesn't either. The theorem's role for Cambridge students is structural — it is the missing step under "$\tfrac{\sin h}{h} \to 1$", without which the first-principles derivative of $\sin x$ is circular.

---

## Beyond syllabus

### The squeeze theorem for sequences and series

The continuous-variable Squeeze Theorem stated above has a sequence version: if $a_n \leq b_n \leq c_n$ for all sufficiently large $n$, and $a_n, c_n \to L$, then $b_n \to L$. This is the workhorse of convergence proofs in real analysis. It's used to prove:

- $\big(1 + \tfrac{1}{n}\big)^n \to e$ — see [[The Hidden Number]] / [[Euler's Number]].
- $\sqrt[n]{n} \to 1$ — the bound $1 \leq \sqrt[n]{n} \leq 1 + \sqrt{2/n}$ (from a clever binomial argument) squeezes both ways to $1$.
- $n!^{1/n} / n \to 1/e$ — Stirling's approximation, more advanced but still a squeeze under the hood.

For series, the **comparison test** is essentially the squeeze theorem in disguise: if $0 \leq a_n \leq b_n$ and $\sum b_n$ converges, then $\sum a_n$ also converges. The bounds-and-trap structure is identical.

### Multivariable limits — squeeze in polar coordinates

In two variables, $\lim_{(x,y) \to (0,0)} f(x, y)$ is *much* harder than its one-variable cousin, because you can approach $(0,0)$ from infinitely many directions. The Squeeze Theorem becomes essential. Common pattern: switch to polar coordinates $(x, y) = (r\cos\theta, r\sin\theta)$, then bound $|f(x, y)|$ by some $g(r)$ that doesn't depend on $\theta$.

For example, to show $\lim_{(x,y) \to (0,0)} \frac{x^2 y}{x^2 + y^2} = 0$:

In polar: $f = r^3 \cos^2 \theta \sin \theta / r^2 = r \cos^2 \theta \sin \theta$. We have $|f| \leq r \cdot 1 \cdot 1 = r$. As $(x, y) \to (0, 0)$, $r \to 0$, so $|f| \to 0$. By squeeze, $f \to 0$. $\blacksquare$

The squeeze provides the *single* bound (uniform in $\theta$) that lets the multivariable limit exist. This is the foundational technique for any 2D or 3D limit calculation in vector calculus, complex analysis, or general relativity.

### Dominated convergence — the squeeze in measure theory

In measure theory, the **Dominated Convergence Theorem** (Lebesgue, 1908) is the squeeze theorem applied to integrals of sequences of functions: if $f_n(x) \to f(x)$ pointwise, and there exists an integrable function $g$ with $|f_n(x)| \leq g(x)$ for all $n$ and all $x$, then $\int f_n \to \int f$. The function $g$ is the "dominating" function — the upper-bound envelope that lets you exchange the limit with the integral.

This theorem is foundational to modern probability theory (used in proving the law of large numbers), to Fourier analysis (used in justifying interchange of integration and summation), and to quantum field theory (used in regularising path integrals). **At its heart, it is the squeeze theorem.** The trapping bound $|f_n| \leq g$ is the trap; the convergence $f_n \to f$ tells you what's being trapped; the integral version follows by Lebesgue's machinery.

### Why squeeze keeps generalising

The Squeeze Theorem is one of those rare results that **generalises perfectly to higher abstractions**. It works for:

- Real-valued functions of one variable (this card)
- Real-valued sequences (the sequence version)
- Series and the comparison test
- Multivariable limits (polar squeeze)
- Sequences of measurable functions (dominated convergence)
- Bounded operators on Banach spaces (functional analysis)
- Distributions and weak limits

Each generalisation has the same shape: **a thing trapped between two things converging to the same place must itself converge there.** The reason is the same in every setting — convergence is a *topological* property, and trapping respects topology. Mathematics has very few tools that scale across so many domains with the same intuition; squeeze is one of them.

---

## Formula sheet status

| Board | Squeeze Theorem in syllabus? | Tested how? |
|---|---|---|
| Cambridge 9709 (Pure 1, 2, 3) | Not named explicitly | Implicit only — the $\sin h/h$ result used in §3.4 differentiation is taken on faith |
| Cambridge 9709 Further Pure | Sometimes named | Beyond A-Level Pure 3 |
| IB Mathematics AA HL | **Yes, named explicitly** | Tested in proof-style questions and applied-limits problems |
| AP Calculus AB | Sometimes named (depends on textbook) | Implicit on the AP exam |
| AP Calculus BC §1.8 | **Yes, named explicitly** | Tested in multiple-choice and FRQ contexts |

**Takeaway.** If you're studying for IB AA HL or AP Calculus BC, the Squeeze Theorem is in your syllabus and you should be able to *state* it, *apply* it, and *explain why the bounds converging matters.* If you're studying for plain 9709 A-Level, you'll never see it named on the exam — but you depend on it the moment you write $(\sin x)' = \cos x$.

---

## Connections

- **Mathematical prerequisites:**
   - [[Limit]] — the foundational definition of convergence; squeeze is one of the main tools for proving limits exist.
   - [[Trigonometric Functions]] — the canonical application is the $\sin h/h$ limit.
   - [[Radians]] — the geometric setup for the unit-circle proof of $\sin h/h \to 1$, including the radians-vs-degrees subtlety.
   - [[Inequalities (Vocab)]] — the chain $g \leq f \leq h$ is the entire structure; comfort with inequality manipulation is essential.

- **Children / forward applications:**
   - [[Differentiation Rules]] — $(\sin x)' = \cos x$ derivation depends on the $\sin h/h$ limit, which depends on this theorem.
   - [[L'Hôpital's Rule]] — the complementary tool for $0/0$ and $\infty/\infty$ limits. Squeeze handles bounded-oscillation cases L'Hôpital can't.
   - [[Sequences and Series]] — the sequence form is used in proving Bolzano-Weierstrass and the convergence of $(1+1/n)^n$ to $e$.
   - [[The Hidden Number]] / [[Euler's Number]] — squeeze on a sequence is one of the standard routes to defining $e$.
   - [[Multivariable Limits]] — polar-coordinate squeeze is the workhorse of vector-calculus limit calculations.

- **Cross-domain bridges:**
   - **Probability theory** — the Dominated Convergence Theorem is the squeeze applied to sequences of integrable functions; foundational for the law of large numbers.
   - **Fourier analysis** — squeeze-style bounds let you exchange limit and integral.
   - **Numerical analysis** — error bounds of the form $|f_n - f| \leq C \cdot r^n$ (with $r < 1$) are squeeze-with-explicit-rate-of-convergence.

- **Misconceptions cleared:** Squeeze requires **two** bounds, not one. The bounds must converge to **the same** limit, not just both converge. $f$ does **not** need to be defined at the limit point $a$. "Sandwich" and "Pinching" are just nicknames; they're all the **same** theorem.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $g(x) \leq f(x) \leq h(x)$ | `g(x) \leq f(x) \leq h(x)` | The squeeze inequality chain |
| $\lim_{x \to a} f(x) = L$ | `\lim_{x \to a} f(x) = L` | Standard limit notation |
| $\lim_{h \to 0} \frac{\sin h}{h} = 1$ | `\lim_{h \to 0} \frac{\sin h}{h} = 1` | The canonical application |
| $\lim_{x \to 0} x \sin(1/x) = 0$ | `\lim_{x \to 0} x \sin(1/x) = 0` | The bounded-oscillation classic |
| $\blacksquare$ | `\blacksquare` | End-of-proof marker |
| $\epsilon, \delta$ | `\epsilon, \delta` | Standard analysis variables |
