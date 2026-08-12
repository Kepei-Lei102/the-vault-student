---
chinese: 中值定理 (zhōngzhí dìnglǐ)
prerequisites:
  - "[[Differentiation]]"
  - "[[Limit]]"
  - "[[Stationary Points]]"
  - "[[Maclaurin Series]]"
leads_to:
  - "[[Fundamental Theorem of Calculus]]"
  - "[[Properties of Definite Integrals]]"
  - "[[L'Hôpital's Rule]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/AP-Calculus-BC-5-1
  - type/deep
  - type/theorem
  - type/proof
  - notation/derivative
  - misconception/MVT-vs-IVT
  - misconception/MVT-needs-differentiability-on-open-interval
---

# Mean Value Theorem 中值定理

## Definition

The **Mean Value Theorem** (MVT) is the calculus statement that *somewhere on a smooth curve, the slope of the tangent matches the slope of the chord*. The two most important versions:

> **MVT for derivatives** (Lagrange's MVT). If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then there exists $c \in (a, b)$ such that
> $$f'(c) = \frac{f(b) - f(a)}{b - a}.$$
>
> **MVT for integrals**. If $f$ is continuous on $[a, b]$, then there exists $c \in [a, b]$ such that
> $$\int_a^b f(x)\, dx = f(c)(b - a).$$

Both say the same kind of thing: an *average* (the chord slope, or the average value of an integrand) equals a *pointwise value* (the tangent slope at $c$, or the function value at $c$). Continuity is what makes "the function takes its average value somewhere" honest — and that's exactly what the Intermediate Value Theorem buys you.

### 中文锚点

中值定理 = "在光滑曲线上某处，切线斜率 = 弦的斜率"。两个版本：

- **微分中值定理 (Lagrange)**：如果 $f$ 在 $[a, b]$ 连续、$(a, b)$ 可导，那么存在 $c \in (a, b)$ 使得 $f'(c) = \dfrac{f(b) - f(a)}{b - a}$。直观：跑 100 米花了 10 秒，*某一瞬间* 你的速度恰好等于平均速度 10 m/s。
- **积分中值定理**：如果 $f$ 在 $[a, b]$ 连续，那么存在 $c \in [a, b]$ 使得 $\int_a^b f\,dx = f(c)(b - a)$。直观：曲线下面积等于一个"等高矩形"的面积，矩形的高 $f(c)$ 是 $f$ 在某点取的真值。

两个版本本质上都在说：**连续函数会在区间内某处取到它的平均值**。

---

## Geometric Picture — MVT for Derivatives

Draw the chord from $(a, f(a))$ to $(b, f(b))$. Its slope is $\dfrac{f(b) - f(a)}{b - a}$ — the average rate of change. The MVT says: somewhere on the curve between $a$ and $b$ there's a point $c$ where the **tangent line is parallel to the chord**. If you slide a ruler down from above so it stays parallel to the chord, the first place it touches the curve is exactly at $x = c$ — that point has the matching tangent slope.

This makes the speed-limit version of the MVT obvious. If your average speed over a 60-mile stretch is 80 mph, then *at some instant during that stretch* your instantaneous speed was exactly 80 mph. (Useful in court, occasionally.)

---

## Rolle's Theorem — the Special Case

**Rolle's theorem.** If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, then there exists $c \in (a, b)$ with $f'(c) = 0$.

Geometrically: if a smooth curve starts and ends at the same height, somewhere in between it has a horizontal tangent (a stationary point — see [[Stationary Points]]). This is the special case of the MVT where the chord slope is $0$.

**Proof sketch.** $f$ is continuous on a closed interval, so by the **Extreme Value Theorem** it attains its maximum $M$ and minimum $m$ somewhere on $[a, b]$. Two cases:

1. If $M = m$ then $f$ is constant on $[a, b]$, so $f'(c) = 0$ for *every* $c$.
2. Otherwise, since $f(a) = f(b)$, at least one of $M, m$ is attained at an interior point $c \in (a, b)$. At that interior extremum, $f'(c) = 0$ (a calculus 101 result: *interior extrema of differentiable functions are critical points*).

Either way, some $c \in (a, b)$ has $f'(c) = 0$. $\;\boxed{}$

---

## Proof of the MVT for Derivatives — The Tilt Trick

**Strategy.** The MVT is what Rolle's theorem becomes after you "tilt" the chord to be horizontal.

Define an auxiliary function:

$$
g(x) = f(x) - \underbrace{\left[f(a) + \frac{f(b) - f(a)}{b - a}(x - a)\right]}_{\text{the chord}}.
$$

In words: $g(x)$ is $f(x)$ with the chord subtracted off. The chord is a straight line from $(a, f(a))$ to $(b, f(b))$, so $g(a) = 0$ and $g(b) = 0$. Also $g$ is continuous on $[a, b]$ and differentiable on $(a, b)$ (it's $f$ minus a linear function — both operations preserve those).

By Rolle's theorem applied to $g$, there exists $c \in (a, b)$ with $g'(c) = 0$. Differentiating:

$$
g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}.
$$

Setting $g'(c) = 0$ gives

$$
f'(c) = \frac{f(b) - f(a)}{b - a}. \qquad\boxed{}
$$

**The tilt trick is reusable.** Whenever you have a "non-horizontal" version of a theorem ($f(a) \neq f(b)$), subtract off the linear piece to reduce it to a horizontal version, then apply the simpler theorem. We'll see the same trick in *Cauchy's MVT* below.

---

## Proof of the MVT for Integrals

If $f$ is continuous on $[a, b]$, then by the **Extreme Value Theorem** $f$ attains a minimum $m$ and a maximum $M$ on $[a, b]$. Integrating $m \le f(x) \le M$ over $[a, b]$:

$$
m(b - a) \le \int_a^b f(x)\, dx \le M(b - a),
$$

so the **average value** $\bar f = \dfrac{1}{b - a}\int_a^b f\, dx$ lies in $[m, M]$. By the **Intermediate Value Theorem** (a continuous function on a closed interval takes every value between its min and max), there exists $c \in [a, b]$ with $f(c) = \bar f$. Multiplying by $(b - a)$:

$$
\int_a^b f(x)\, dx = f(c)(b - a). \qquad\boxed{}
$$

This is the lemma used inside the proof of [[Fundamental Theorem of Calculus]] (FTC1). The MVT for integrals is what lets the FTC1 proof "see" $f$'s value at a single point inside the integration interval, which is exactly what's needed to conclude $F'(x) = f(x)$.

---

## Cauchy's Mean Value Theorem (Generalised MVT)

Beyond the AP/IB syllabus level, but worth knowing for first-year university analysis: **Cauchy's MVT** generalises the standard MVT to a *pair* of functions.

> **Cauchy's MVT.** If $f$ and $g$ are continuous on $[a, b]$ and differentiable on $(a, b)$, with $g'(x) \ne 0$ throughout $(a, b)$, then there exists $c \in (a, b)$ with
> $$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}.$$

Setting $g(x) = x$ recovers Lagrange's MVT. Cauchy's MVT is the mechanism behind the rigorous proof of [[L'Hôpital's Rule]] — *that* is where it earns its keep.

---

## Applications

### Applying MVT to existence questions

The classic AP question pattern: "Show that there exists $c \in (1, 4)$ such that $f'(c) = 2$." Strategy: identify a chord whose slope is $2$, then invoke MVT. Often the data given is $f(1) = 3$ and $f(4) = 9$, so $\frac{f(4) - f(1)}{4 - 1} = 2$ and the MVT supplies the required $c$.

### Speed-limit problems

If you cover 200 km in 2 hours, your average speed is 100 km/h. By the MVT applied to position $s(t)$, your *instantaneous* speed $s'(t)$ equalled 100 km/h at some moment. Police cars have used this argument since at least the 1970s — the MVT has stood up in court.

### Sign-of-derivative ⇒ monotonicity

If $f'(x) > 0$ on $(a, b)$ then $f$ is strictly increasing on $[a, b]$. Proof: take any $a \le x_1 < x_2 \le b$; by MVT, $f(x_2) - f(x_1) = f'(c)(x_2 - x_1)$ for some $c \in (x_1, x_2)$. Since $f'(c) > 0$ and $x_2 - x_1 > 0$, the right side is positive, so $f(x_2) > f(x_1)$. The "sign of $f'$ tells you whether $f$ is increasing/decreasing" rule is the MVT in disguise — see [[Stationary Points]] for the practical use.

### "Functions with the same derivative differ by a constant"

If $f'(x) = g'(x)$ for all $x \in (a, b)$, then $f - g$ is constant on $(a, b)$. Proof: let $h = f - g$, so $h' = 0$. By MVT applied to $h$ on any sub-interval $[x_1, x_2]$, $h(x_2) - h(x_1) = h'(c)(x_2 - x_1) = 0$. So $h(x_2) = h(x_1)$ — $h$ is constant. This is the result behind every "$+C$" in indefinite integration, and it's the lemma in the proof of [[Fundamental Theorem of Calculus]] FTC2.

---

## Common Mistakes

1. **Confusing MVT with IVT.** The Intermediate Value Theorem says *every value* between $f(a)$ and $f(b)$ is achieved by $f$ at some point. The MVT says the *average rate of change* between $a$ and $b$ is achieved by $f'$ at some point. Different theorems, different conclusions.
2. **Missing the differentiability hypothesis.** MVT requires *differentiability on the open interval $(a, b)$* and *continuity on the closed interval $[a, b]$*. If $f$ has a corner inside $(a, b)$ — e.g., $f(x) = |x|$ on $[-1, 1]$ — the MVT can fail. ($f(1) = 1$, $f(-1) = 1$, chord slope is $0$, but $f'$ is never zero where it exists; the issue is that $f'(0)$ doesn't exist.)
3. **"MVT gives a unique $c$."** It guarantees *at least one* $c$. There can be many. For $f(x) = \sin x$ on $[0, 2\pi]$, the chord slope is $0$ and $f'(c) = 0$ has *multiple* solutions in $(0, 2\pi)$ (at $\pi/2$ and $3\pi/2$).
4. **Setting up the wrong chord slope.** The chord goes from $(a, f(a))$ to $(b, f(b))$ — the slope is $\frac{f(b) - f(a)}{b - a}$, *function values* on top, *inputs* on bottom. Inverting these is a classic algebra slip.
5. **Applying the MVT to a function that isn't continuous on $[a, b]$.** If $f$ has a jump in $[a, b]$, the conclusion can fail. Always check: is $f$ continuous? Is it differentiable on the *open* interval?

---

## Exam Notes

### AP Calculus AB / BC — Topic 5.1

Core curriculum. AP gives MVT a full topic (FUN-1.B; ~15 class periods AB, ~10 BC). Expected skills:

- *State* the MVT precisely, including hypotheses (continuity + differentiability)
- *Verify* whether the MVT applies to a given function on a given interval
- *Compute* the value $c$ guaranteed by the MVT in routine cases
- *Justify* conclusions about a function's behaviour from MVT (existence of a horizontal tangent, of a particular slope, etc.)
- Common AP free-response prompt: *"Justify that there must exist a value $c$ in $(a, b)$ such that …"* — invariably an MVT (or IVT) application.

### IB AA HL

MVT is in the optional **Calculus** topic for HL. Stated and applied; proof not formally required but seen in textbooks. Cauchy's MVT is occasionally included as an aside before L'Hôpital's rule.

### A-Level Pure Mathematics

MVT is *not* on the standard A-Level Pure syllabus (Edexcel / OCR / AQA), but appears in Further Maths and STEP. The "average rate of change" reasoning underlies many A-Level problems implicitly.

### Cambridge 0606 / 9709

Not on the syllabus. The MVT is assumed silently when 9709 P3 uses "$f'(x) > 0 \Rightarrow f$ is increasing" or "two functions with the same derivative differ by a constant" — both are MVT in disguise.

---

## Connections

- **Prerequisite:** [[Differentiation]] — the derivative being the limit of slopes is the geometric setup
- **Prerequisite:** [[Limit]] — Extreme Value Theorem and Intermediate Value Theorem (used in both proofs) are limit-of-continuous-function results
- **Prerequisite:** [[Stationary Points]] — Rolle's theorem is "interior extrema of differentiable functions have $f' = 0$"
- **Used by:** [[Fundamental Theorem of Calculus]] — the MVT for integrals supplies the $f(c)$ in the FTC1 proof; the "same derivative implies same up to constant" lemma is used in FTC2
- **Used by:** [[Properties of Definite Integrals]] — MVT for integrals is one of the named properties
- **Used by:** [[L'Hôpital's Rule]] — Cauchy's generalised MVT is the engine of the rigorous L'Hôpital proof
- **Used by:** monotonicity tests in [[Stationary Points]] (sign of $f'$ tells you whether $f$ is increasing)
- **Application:** "average speed = instantaneous speed at some point" — the speed-limit interpretation
- **Application:** error bounds in numerical analysis — MVT supplies $|f(x_1) - f(x_2)| \le L|x_1 - x_2|$ when $|f'| \le L$ (Lipschitz continuity)
- **Beyond high school:** *Taylor's theorem with remainder* is iterated MVT; *the increment lemma* in multivariable calculus; *the mean value inequality* in $\mathbb{R}^n$

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $f'(c) = \dfrac{f(b)-f(a)}{b-a}$ | `f'(c) = \dfrac{f(b)-f(a)}{b-a}` | the MVT statement |
| $\int_a^b f(x)\,dx = f(c)(b-a)$ | `\int_a^b f(x)\,dx = f(c)(b-a)` | MVT for integrals |
| $\bar f$ | `\bar f` | average value of $f$ |
| $\boxed{}$ | `\boxed{}` | end-of-proof marker |
