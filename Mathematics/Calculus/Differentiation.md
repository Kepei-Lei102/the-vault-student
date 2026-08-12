---
chinese: 微分 / 求导 (wēifēn / qiúdǎo)
prerequisites:
  - "[[Limit]]"
  - "[[Function]]"
  - "[[Radians]]"
leads_to:
  - "[[Power Rule]]"
  - "[[Product Rule]]"
  - "[[Chain Rule]]"
  - "[[Tangents and Normals]]"
  - "[[Stationary Points]]"
  - "[[Exponential Function]]"
  - "[[Integration]]"
  - "[[Error Propagation]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-A13
  - syllabus/9260-A14
  - syllabus/0580-E2-12
  - syllabus/0606-14-1
  - syllabus/0606-14-2
  - syllabus/9709-1-7
  - type/definition
  - type/vocabulary
  - notation/derivative
  - misconception/dy-dx-is-a-fraction
---

# Differentiation 微分 / 求导

## Definition

### Formal

The **derivative** of $f(x)$ is defined as:

$$f'(x) = \lim_{\delta x \to 0} \dfrac{f(x + \delta x) - f(x)}{\delta x}$$

Equivalently, using $h$ instead of $\delta x$:

$$f'(x) = \lim_{h \to 0} \dfrac{f(x + h) - f(x)}{h}$$

This limit, if it exists, gives the **instantaneous rate of change** of $f$ at $x$, which is the **gradient of the tangent** to the curve at that point.

### Intuitive

Imagine zooming in on a curve at a point. The more you zoom, the more the curve looks like a straight line. The derivative is the gradient of that straight line — the gradient the curve "wants to be" at that exact point.

![[differentiation-zoom-intuition.svg|900]]

More concretely: take two points on the curve, close together. Draw the line between them (a **chord**). Its gradient is $\dfrac{\delta y}{\delta x}$. Now slide the second point closer and closer to the first. The chord rotates and settles into the **tangent**. The derivative is the gradient the chord approaches — the [[Limit]] of $\dfrac{\delta y}{\delta x}$ as $\delta x \to 0$.

### 中文锚点 (Chinese Anchor)

微分有两个常用中文名，对应两个不同视角：

- **微分** (wēifēn)："微"是微小，"分"是分割——把变化切成微小的碎片来分析。
- **求导** (qiúdǎo)："求"是寻找，"导"是导数（derivative）——寻找导数的过程。

$\dfrac{dy}{dx}$到底是什么？当$x$变化极小量$dx$时，$y$也会有对应的变化极小量$dy$。$\dfrac{dy}{dx}$就是这两个极小量变化的比值——所以它确实是一个分数。

直觉上：在曲线上取两个很近的点，连一条线（割线），看斜率。两点越来越近，割线变成切线。切线的斜率就是导数。

## Notation — Why So Many Symbols?

Calculus was invented independently by Newton and Leibniz in the 1660s–1680s. They used different notation, and both systems (plus a third by Lagrange) survived. Each reveals something different.

| Notation         | Example          | Named after           | What it emphasises                                                                                         |
| ---------------- | ---------------- | --------------------- | ---------------------------------------------------------------------------------------------------------- |
| Leibniz          | $\dfrac{dy}{dx}$ | Gottfried Leibniz     | The derivative as a ratio of infinitesimal changes — reminds you it came from $\dfrac{\delta y}{\delta x}$ |
| Lagrange (prime) | $f'(x)$          | Joseph-Louis Lagrange | The derivative as a new *function* — feed in $x$, get out the gradient at $x$                              |
| Newton (dot)     | $\dot{y}$        | Isaac Newton          | Rate of change with respect to *time* — used in physics (velocity, acceleration)                           |

### Why the prime (′) symbol?

Lagrange's $f'(x)$ means "the function *derived from* $f$" — hence the name **derivative**. The prime mark is just a shorthand for "the next one in the sequence": $f$ → $f'$ → $f''$ → $f'''$. It keeps the notation compact when you differentiate multiple times.

### What $\dfrac{dy}{dx}$ actually means

$\dfrac{dy}{dx}$ looks like a fraction — and that's deliberate. It evolved from the genuine fraction $\dfrac{\delta y}{\delta x}$:

$$\dfrac{\delta y}{\delta x} = \dfrac{f(x + \delta x) - f(x)}{\delta x} \xrightarrow{\delta x \to 0} \dfrac{dy}{dx}$$

$\dfrac{dy}{dx}$ evolved from the fraction $\dfrac{\delta y}{\delta x}$, and at university level it *is* made rigorous as a ratio of differential forms — $dy$ and $dx$ are real objects, and $\dfrac{dy}{dx}$ is their ratio. So it's fair to call it a fraction, as long as you understand what $dy$ and $dx$ are.

> [!info] Is dy/dx a fraction? — The full story
> At IGCSE/GCSE: yes, treat it as one. It behaves like a fraction and you'll get correct answers.
> At A-Level/IB/AP: teachers say "not really" — because at this level, $dy$ and $dx$ haven't been formally defined yet, so calling it a fraction feels hand-wavy. The chain rule *looks* like cancelling ($\dfrac{dy}{du} \cdot \dfrac{du}{dx} = \dfrac{dy}{dx}$), but the proof uses limits, not fraction cancellation.
> At university: yes, it is a fraction again — $dy$ and $dx$ are defined as **differential forms**, and $\dfrac{dy}{dx}$ is genuinely their ratio.
>
> The journey: fraction → "not a fraction" → fraction again, but deeper. This vault takes the university view: $dy$ and $dx$ are tiny changes, $\dfrac{dy}{dx}$ is their ratio.

### Second derivative

| Leibniz              | Lagrange | Meaning                                                           |
| -------------------- | -------- | ----------------------------------------------------------------- |
| $\dfrac{d^2y}{dx^2}$ | $f''(x)$ | The derivative of the derivative — rate of change of the gradient |

> [!warning] Why $\dfrac{d^2y}{dx^2}$ and not $\dfrac{d^2y}{d^2x}$? — The notation's one honest crack
> We just committed to the view that $\dfrac{dy}{dx}$ is a genuine fraction. But the second derivative notation **breaks this**. If you actually try to differentiate $\dfrac{dy}{dx}$ as a fraction of differentials, you get:
>
> $$\dfrac{d\left(\dfrac{dy}{dx}\right)}{dx} = \dfrac{d^2y \cdot dx - dy \cdot d^2x}{(dx)^3}$$
>
> That's not $\dfrac{d^2y}{dx^2}$. The real second derivative (as a ratio of differentials) has an extra $\dfrac{dy \cdot d^2x}{(dx)^3}$ term.
>
> So what is $\dfrac{d^2y}{dx^2}$? It's **operator notation**, not fraction notation. It means "apply $\dfrac{d}{dx}$ twice":
>
> $$\left(\dfrac{d}{dx}\right)^2 y = \dfrac{d}{dx}\left(\dfrac{d}{dx}(y)\right)$$
>
> The "2" in $d^2y$ counts how many times you differentiate. The $dx^2$ is shorthand for $(dx)^2$ in the denominator of the operator. It's a notational convenience that *looks* like a fraction but isn't one.
>
> **This is the one place where the fraction metaphor genuinely fails.** The first derivative $\dfrac{dy}{dx}$? Real fraction. The second derivative $\dfrac{d^2y}{dx^2}$? Operator shorthand. Lagrange's $f''(x)$ is cleaner here — it just says "differentiate twice" without pretending to be a fraction.

## First Principles — Differentiation from the Definition

"First principles" means going back to the limit definition. Here's how it works for $f(x) = x^2$:

$$f'(x) = \lim_{h \to 0} \dfrac{(x+h)^2 - x^2}{h} = \lim_{h \to 0} \dfrac{x^2 + 2xh + h^2 - x^2}{h} = \lim_{h \to 0} \dfrac{2xh + h^2}{h}$$

$$= \lim_{h \to 0} (2x + h) = 2x$$

So $\dfrac{d}{dx}(x^2) = 2x$.

**What happened step by step:**

1. Write $f(x+h) - f(x)$ — the change in $y$
2. Divide by $h$ — the change in $x$ → this gives the chord gradient
3. Simplify — cancel the $h$ in the denominator (this is the algebraic trick)
4. Take the limit $h \to 0$ — the chord becomes the tangent

> [!tip] Why "first principles" matters
> You won't use this method for every derivative — that's what the [[Power Rule]], [[Product Rule]] (which folds in the quotient rule as a corollary), and [[Chain Rule]] are for. But first principles is the *proof* that those rules work. Every differentiation rule can be derived by going back to this limit.

## Gradient of a Curve

### The Core Idea

A straight line has one gradient everywhere. A curve has a different gradient at every point. The derivative $f'(x)$ gives you the **gradient function** — plug in any $x$-value, get the gradient at that point.

| Concept | What it is | How to find it |
|---|---|---|
| Gradient of a straight line | Constant: $m = \dfrac{\Delta y}{\Delta x}$ | Rise over run |
| Gradient of a curve at a point | The gradient of the **tangent** at that point | Differentiate, then substitute the $x$-value |

### The Tangent Line

At 9260 (A14), you need to find the **equation of the tangent** to a curve at a given point.

**Method:**

1. Differentiate to find $f'(x)$
2. Substitute the $x$-coordinate to find the gradient: $m = f'(a)$
3. Use $y - y_1 = m(x - x_1)$ with the point $(a, f(a))$

**Worked example:** Find the equation of the tangent to $y = x^3 - 2x$ at $x = 1$.

1. $\dfrac{dy}{dx} = 3x^2 - 2$ (using [[Power Rule]])
2. At $x = 1$: gradient $= 3(1)^2 - 2 = 1$
3. At $x = 1$: $y = 1 - 2 = -1$, so the point is $(1, -1)$
4. Tangent: $y - (-1) = 1(x - 1)$ → $y = x - 2$

## Key Facts / Properties

### What Differentiation Tells You

| $f'(x)$ | Meaning | The curve is... |
|---|---|---|
| $f'(x) > 0$ | Gradient is positive | Increasing (going uphill left to right) |
| $f'(x) < 0$ | Gradient is negative | Decreasing (going downhill left to right) |
| $f'(x) = 0$ | Gradient is zero | Flat — possible [[Stationary Points]] |

### The Physics Parallel

If $f(t)$ describes **where** an object is at time $t$ (displacement), then its derivatives tell the rest of the story:

| Function | Meaning | Units (if distance in m, time in s) |
|---|---|---|
| $f(t)$ | Displacement — where you are | m |
| $f'(t)$ | Velocity — how fast you're moving | m/s |
| $f''(t)$ | Acceleration — how fast your speed is changing | m/s² |

This is why Newton used $\dot{y}$ (dot notation) — he was thinking about motion through time. When you differentiate displacement, you get velocity. Differentiate again, you get acceleration. The derivative always answers: **"how fast is the previous thing changing?"**

Example: if a ball is thrown upward and its height is $h(t) = 20t - 5t^2$ metres:
- $h'(t) = 20 - 10t$ m/s (velocity — positive means going up, negative means falling)
- $h''(t) = -10$ m/s² (acceleration — constant, downward, this is gravity)

### Basic Differentiation Results (Preview)

These all come from the [[Power Rule]], which is proved in that note:

| $f(x)$ | $f'(x)$ | In words |
|---|---|---|
| $c$ (constant) | $0$ | Constants don't change → zero rate of change |
| $x$ | $1$ | Straight line with gradient 1 |
| $x^2$ | $2x$ | |
| $x^3$ | $3x^2$ | |
| $x^n$ | $nx^{n-1}$ | **Power rule** — see [[Power Rule]] for proof |
| $kx^n$ | $knx^{n-1}$ | Scalar multiple rule — constants pull out |

### Linearity of Differentiation

$$\dfrac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x) \qquad \dfrac{d}{dx}[kf(x)] = kf'(x)$$

You can differentiate term by term. This is why polynomials are straightforward: just apply the power rule to each term.

> [!info] Why does linearity work?
> Because limits are linear (see [[Limit]] — limit laws). Differentiation is defined as a limit, so it inherits the sum and scalar rules automatically:
>
> $$\lim_{h \to 0} \dfrac{[f(x+h) + g(x+h)] - [f(x) + g(x)]}{h} = \lim_{h \to 0} \dfrac{f(x+h) - f(x)}{h} + \lim_{h \to 0} \dfrac{g(x+h) - g(x)}{h}$$

## Common Misconceptions (Teaching Notes)

### 1. "$\dfrac{dy}{dx}$ is a fraction, so I can always separate $dy$ and $dx$"

At IGCSE level, treating $\dfrac{dy}{dx}$ as a fraction happens to give correct answers (e.g., in separation of variables). But students who internalise this as a rule rather than a coincidence will struggle at university.

**Fix:** Explain that $\dfrac{dy}{dx}$ is the *limit* of a fraction. It *behaves* like a fraction in specific situations (chain rule, separation of variables) because of how limits work, not because it literally is one.

### 2. Confusing the derivative with the function value

Students compute $f'(x)$ correctly but then forget to substitute the $x$-value when asked for "the gradient at $x = 3$." They give $f'(x) = 3x^2 - 1$ when the answer should be $f'(3) = 26$.

**Fix:** Emphasise the two-step process: differentiate (get the gradient *function*), then substitute (get the gradient *number*).

### 3. "The derivative of $x^n$ is $x^{n-1}$"

Forgetting the coefficient $n$. The power rule is $nx^{n-1}$, not just $x^{n-1}$.

**Fix:** Read it as "bring down the power, reduce by one." The $n$ comes down as a multiplier.

### 4. "Differentiation makes things smaller"

Students assume that because we're looking at "infinitely small" changes, the derivative must be small. It isn't — $f'(x)$ can be any value. The derivative of $1000x$ is $1000$.

**Fix:** The derivative measures the *rate* of change, not the *size* of change. A steep hill has a large gradient even if you only walk a tiny step.

### 5. "The tangent touches the curve at one point only"

True for circles, but not in general. A tangent to a curve may cross the curve elsewhere. What makes it a tangent is the *local* behaviour — it touches and has the same gradient at that specific point.

## Exam Notes

### OxAQA 9260

- A13: differentiate $kx^n$ where $n$ is a positive integer or 0; understand the gradient function $\dfrac{dy}{dx}$
- A14: gradient of a curve = gradient of the tangent; find the equation of the tangent at a given point
- Extension tier only
- First principles is **not required** (but understanding helps)
- Both Paper 1E and Paper 2E
- Questions typically: "Find $\dfrac{dy}{dx}$", "Find the gradient at $x = ...$", "Find the equation of the tangent at ..."
- Expect polynomials only (no trig, no $e^x$, no fractions of $x$)

### Cambridge 0606

- 14.1: idea of a derived function, informal concept of limit ($\dfrac{\delta y}{\delta x} \to \dfrac{dy}{dx}$)
- 14.2: notation — $f'(x)$, $f''(x)$, $\dfrac{dy}{dx}$, $\dfrac{d^2y}{dx^2}$
- First principles is **not required** at 0606
- 0606 goes further than 9260: rational powers, trig, $e^x$, $\ln x$ are all in scope — see [[Differentiation Rules]]
- Both Paper 1 and Paper 2

### AP / IB / A-Level

- **AP Calculus AB:** requires limit definition, first principles for simple cases
- **IB Mathematics AA HL:** formal definition, first principles proofs
- **A-Level Mathematics:** first principles required; differentiability vs continuity discussed
- The first principles derivation in this note is college-level preparation

## Connections

- **Foundation:** [[Limit]] — the derivative *is* a limit
- **Core rule:** [[Power Rule]] — the first and most important differentiation rule (with proof)
- **Extensions:** [[Product Rule]] (with the quotient rule as a corollary), [[Chain Rule]] — rules for differentiating combinations of functions
- **Applications:** [[Tangents and Normals]] — using the derivative to find equations of tangents and normals
- **Applications:** [[Stationary Points]] — where $f'(x) = 0$
- **Reverse:** [[Integration]] — the reverse process of differentiation
- **Bridge:** [[Fundamental Theorem of Calculus]] — connects differentiation and integration

> [!info] Beyond syllabus — How computers differentiate
> Computers can't "do algebra" the way you do on paper. So how do they find derivatives? There are three approaches, and each has trade-offs:
>
> **1. Numerical differentiation** — the brute-force way
> Pick a very small $h$ (like $10^{-8}$) and compute:
> $$f'(x) \approx \dfrac{f(x + h) - f(x)}{h}$$
> This is literally the first principles definition with a small-but-nonzero $h$. It works for *any* function — even one you can't write a formula for. But it has a fundamental problem: if $h$ is too large, the approximation is bad; if $h$ is too small, floating-point rounding errors dominate. There's a sweet spot, but it's never exact.
>
> **2. Symbolic differentiation** — the algebra way
> Computer algebra systems (Wolfram Alpha, GeoGebra, Mathematica) apply the same rules you learn: power rule, chain rule, product rule, etc. The input is a formula, the output is an exact formula. This is perfect for "find $\dfrac{dy}{dx}$" but can be slow for extremely complex expressions, and it can't handle functions defined by code rather than formulas.
>
> **3. Automatic differentiation (autodiff)** — how AI actually works
> This is the clever one. The computer breaks your function into tiny elementary steps (add, multiply, sin, exp...) and applies the chain rule through each step automatically. The result is **exact** (no approximation error) and **efficient** (scales to millions of variables).
>
> Autodiff is the engine behind training neural networks. When you hear "backpropagation" in machine learning, that *is* automatic differentiation — the chain rule applied backwards through a network of matrix operations. Every time ChatGPT was trained, it was doing calculus — specifically, the chain rule — trillions of times.

> [!info] Beyond syllabus — Leibniz vs Newton
> Newton and Leibniz both invented calculus independently in the 1660s–1680s, leading to one of the most famous priority disputes in mathematics. Newton called his method "fluxions" and used $\dot{y}$ notation. Leibniz called it "calculus" and used $\dfrac{dy}{dx}$. Lagrange came later (1797) and introduced $f'(x)$, wanting to free calculus from the controversy over infinitesimals.
>
> We use all three systems today because each is useful: Leibniz for chain rule and integration, Lagrange for function notation, Newton for physics. The fact that three different notations survived tells you how fundamental this idea is — it's too important for any one notation to own.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{dy}{dx}$ | `\frac{dy}{dx}` or `\dfrac{dy}{dx}` | Leibniz notation (`\dfrac` for inline) |
| $f'(x)$ | `f'(x)` | Lagrange (prime) notation |
| $\dot{y}$ | `\dot{y}` | Newton notation (time derivatives) |
| $\dfrac{d^2y}{dx^2}$ | `\frac{d^2y}{dx^2}` or `\dfrac{d^2y}{dx^2}` | Second derivative (Leibniz) |
| $f''(x)$ | `f''(x)` | Second derivative (Lagrange) |
| $\dfrac{d}{dx}$ | `\frac{d}{dx}` or `\dfrac{d}{dx}` | Differentiation operator |
| $\lim_{h \to 0}$ | `\lim_{h \to 0}` | Limit notation for first principles |
| $\delta x$ | `\delta x` | Small finite change in $x$ |
