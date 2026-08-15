---
chinese: 指数函数 (zhǐshù hánshù)
prerequisites:
  - "[[Laws of Indices]]"
  - "[[Euler's Number]]"
  - "[[Exponential Graphs (Vocab)]]"
  - "[[Differentiation]]"
  - "[[Exponential Growth and Decay]]"
leads_to:
  - "[[Hyperbolic Functions]]"
  - "[[Poisson Distribution]]"
  - "[[Integration]]"
  - "[[Differential Equations]]"
  - "[[Complex Numbers]]"
  - "[[Second-Order Differential Equations]]"
  - "[[Differentiation Rules]]"
  - "[[The Hidden Number]]"
teach_together:
  - "[[Logarithms]]"
tags:
  - subject/mathematics
  - domain/number
  - domain/analysis
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/0606-6-1
  - syllabus/0606-6-3
  - syllabus/9709-2-2
  - syllabus/9709-3-2
  - type/deep
  - type/definition
  - type/proof
  - notation/e
  - notation/exp
  - misconception/e-x-is-polynomial
  - misconception/exp-of-sum-splits
  - misconception/solving-by-cancellation
---

# Exponential Function 指数函数

## Definition

The **exponential function** is the function

$$\boxed{\;y = e^x\;}$$

where $e \approx 2.71828\ldots$ is the constant from [[Euler's Number]]. It is defined for every real number $x$, and it is the companion to [[Logarithms]]: the function $\ln x$ *undoes* $e^x$, and $e^x$ *undoes* $\ln x$ — they are **inverse functions**.

Three things make $e^x$ the most important function in calculus, physics, and applied mathematics — and the reason it deserves its own card separate from the general shape $y = b^x$ covered in [[Exponential Graphs (Vocab)]]:

1. **It is its own derivative.** $\dfrac{d}{dx} e^x = e^x$. No other function (up to a constant multiple) has this property, and the proof is the centrepiece of this card.
2. **It turns addition in the exponent into multiplication of outputs.** $e^{a+b} = e^a \cdot e^b$. This is the only algebra law you ever need for $e^x$ — and it comes for free from the index laws.
3. **Every other exponential $b^x$ is just $e^x$ in disguise.** The identity $b^x = e^{x \ln b}$ lets you reduce every exponential calculation to an $e^x$ calculation, which is why base $e$ is called the "natural" base of calculus.

### Intuition

Think of $e^x$ as "the growth that keeps up with itself." If $y = e^x$ is the amount you have at time $x$, then the *rate at which $y$ is changing* at any moment is equal to $y$ itself — the more you have, the faster you grow. No other smooth, well-behaved function can do this without a correction factor stapled on (see §4 below for base $b$; see [[Euler's Number]] §3 for why this uniqueness pins $e$ down).

### 中文锚点

**指数函数 $y = e^x$** 是数学中最重要的函数之一。它的核心特征：**自身的导数等于自身**，即 $\dfrac{d}{dx}e^x = e^x$。

三个关键事实：
- **定义域** (domain): 全体实数 $\mathbb{R}$
- **值域** (range): $y > 0$（永远为正）
- **特殊值**: $e^0 = 1$, $e^1 = e$, $\lim_{x \to -\infty} e^x = 0$, $\lim_{x \to +\infty} e^x = \infty$

它与[[Logarithms|自然对数]] $\ln x$ 互为**反函数** (inverse functions)：$\ln(e^x) = x$，$e^{\ln x} = x$。这张卡片讲 $e^x$ 作为一个**函数对象**——它的性质、它的图像、它的导数证明、以及为什么它在微积分中无处不在。

## Notation

| Symbol | Reads as | Notes |
|--------|----------|-------|
| $e^x$ | "e to the x" | The standard notation; always preferred |
| $\exp(x)$ | "exp of x" | Alternative — common in computer code and when the exponent is a long expression, e.g. $\exp\!\left(-\tfrac{x^2}{2}\right)$ is cleaner than $e^{-x^2/2}$ |
| $e^{f(x)}$ | "e to the f of x" | Compose with any function; the whole expression $f(x)$ sits in the exponent |

> [!info] When to prefer $\exp(\cdot)$ over $e^{(\cdot)}$
> Use $\exp$ when the exponent is bulky. Compare
> $e^{-\tfrac{(x-\mu)^2}{2\sigma^2}}$ vs $\exp\!\left(-\dfrac{(x-\mu)^2}{2\sigma^2}\right)$ — the second form is much easier to read and is the standard in statistics texts. On exams, $e^x$ is fine for simple exponents; switch to $\exp$ only if the superscript becomes unreadable.

## Key properties — the exp laws

Every one of these is an **index law** (from [[Laws of Indices]]) applied to the specific base $e$. There is nothing new to memorise — just confirm that $e$ obeys the same rules as any other positive base.

Let $a, b \in \mathbb{R}$.

| Property | Identity | Name |
|----------|----------|------|
| Exponent of zero | $e^0 = 1$ | Anything non-zero to the zeroth power is 1 |
| Exponent of one | $e^1 = e$ | The definition |
| Sum in exponent | $e^{a+b} = e^a \cdot e^b$ | **Product law** — addition splits into multiplication |
| Difference in exponent | $e^{a-b} = \dfrac{e^a}{e^b}$ | **Quotient law** |
| Product in exponent | $e^{ab} = (e^a)^b = (e^b)^a$ | **Power law** |
| Negative exponent | $e^{-a} = \dfrac{1}{e^a}$ | Special case of the quotient law with $b = 0$ swapped |
| Always positive | $e^x > 0$ for every real $x$ | No exponent makes a positive base zero or negative |

The product law $e^{a+b} = e^a \cdot e^b$ is the one to internalise — it is the reason $e^x$ shows up any time a quantity changes by a *factor* per unit time (see [[Exponential Growth and Decay]]).

> [!warning] $e^{a+b} \neq e^a + e^b$
> The most common algebra mistake. The sum $a+b$ in the *exponent* becomes a *product* $e^a \cdot e^b$ — not a sum. Numerical check: $e^{1+1} = e^2 \approx 7.39$, but $e^1 + e^1 = 2e \approx 5.44$. Very different numbers. If you find yourself splitting $e^{a+b}$ into $e^a + e^b$, stop and rewrite using $e^a \cdot e^b$.

## The graph of $y = e^x$

![[exp-function-growth-decay.svg|697]]

Above: $y = e^x$ (growth, solid blue) and $y = e^{-x}$ (decay, solid pink), both passing through $(0, 1)$ and both asymptotic to $y = 0$. The decay curve is the reflection of the growth curve across the $y$-axis — because $e^{-x} = \tfrac{1}{e^x}$, which means raising $e$ to $-x$ is the same as inverting the output for $+x$.

| Feature | $y = e^x$ | $y = e^{-x}$ |
|---------|-----------|--------------|
| Domain | all real $x$ | all real $x$ |
| Range | $y > 0$ | $y > 0$ |
| $y$-intercept | $(0, 1)$ | $(0, 1)$ |
| Passes through | $(1, e) \approx (1, 2.718)$ | $(1, 1/e) \approx (1, 0.368)$ |
| As $x \to +\infty$ | $y \to \infty$ | $y \to 0^+$ |
| As $x \to -\infty$ | $y \to 0^+$ | $y \to \infty$ |
| Asymptote | horizontal $y = 0$ | horizontal $y = 0$ |
| Shape | rising, concave up | falling, concave up |

> [!tip] $e^x$ is never zero, never negative
> For every real $x$ — no matter how large and negative — $e^x$ is strictly positive. This is the same fact that makes $\log$ of zero or a negative number undefined (see [[Logarithms]] §"You cannot take the log of zero"). If an exam answer leads to $e^x = 0$ or $e^x = -4$, there is no solution — write "no real solution" rather than trying to force one.

## The headline property: $\dfrac{d}{dx} e^x = e^x$

This is *the* reason base $e$ is called the natural base. Here is a complete proof.

### The setup — $e^x$ as a power series

From [[Euler's Number]] §3, the function $e^x$ has a power-series definition:

$$e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

This is one of three equivalent definitions of $e^x$; the other two (the compound-interest limit and the calculus characterization) agree with it. For the proof below, this is the form we need.

### The proof — differentiate term by term

Differentiate each term of the series using the power rule (from [[Power Rule]]):

$$\frac{d}{dx} \frac{x^k}{k!} = \frac{k \cdot x^{k-1}}{k!} = \frac{x^{k-1}}{(k-1)!} \qquad (\text{for } k \geq 1)$$

The $k = 0$ term is the constant $1$, whose derivative is $0$.

So the derivative of the whole series is:

$$\frac{d}{dx} e^x = 0 + \frac{d}{dx}\!\left(x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots\right) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

The right-hand side is exactly the original series — the same $e^x$ we started with. So

$$\boxed{\;\frac{d}{dx} e^x = e^x\;}$$

$\blacksquare$

### Why this works — the shift argument in one sentence

Every term $\dfrac{x^k}{k!}$ differentiates down to the *previous* term $\dfrac{x^{k-1}}{(k-1)!}$. Differentiating the whole infinite sum shifts every term down by one index — and the sum is infinite, so shifting every term down leaves it unchanged. The $(k-1)!$ in the denominator exactly swallows the factor of $k$ that the power rule pulls out. That cancellation is a silent consequence of the factorials; it doesn't happen for any other series.

> [!info] Why no other base self-differentiates
> For a general base $b$, $\dfrac{d}{dx} b^x = b^x \ln b$. Base $2$ picks up a factor of $\ln 2 \approx 0.693$; base $10$ picks up $\ln 10 \approx 2.303$. Only when $b = e$ does $\ln b = 1$, making the correction vanish. $e$ is *defined* (equivalently, pinned down) by this very property: $e$ is the unique base whose exponential is its own derivative. See [[Euler's Number]] §3 for the three-way equivalence.

## Closing the loop — the derivative of $\ln$

The Logarithms card left this promise open: once $(e^x)' = e^x$ is established, the derivative of $\ln x$ falls out in one step via the **inverse function rule**.

**Claim.** $\dfrac{d}{dx} \ln x = \dfrac{1}{x}$.

**Proof (inverse function rule).** Set $y = \ln x$. By the definition of $\ln$ as the inverse of $e^x$:

$$e^y = x.$$

Differentiate both sides with respect to $x$. The right side is $1$. The left side uses the chain rule: $\dfrac{d}{dx} e^y = e^y \cdot \dfrac{dy}{dx}$

$$e^y \cdot \frac{dy}{dx} = 1 \quad\Rightarrow\quad \frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}$$

(Using $e^y = x$ in the last step.) So $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$ $\blacksquare$

> [!tip] The symmetric identity
> $(e^x)' = e^x$ and $(\ln x)' = 1/x$ are the **same theorem** stated twice — once with the roles of input and output on $y = e^x$, once with those roles swapped on $y = \ln x$. They are forced to be consistent by the chain rule, and they are what makes $e$ and $\ln$ the pair calculus cannot live without.

## General base: $y = b^x$ as a disguised $e^x$

For any positive base $b$, we can rewrite $b^x$ entirely in terms of $e$.

**The identity.** $b^x = e^{x \ln b}$.

**Why.** By the definition of $\ln$, $b = e^{\ln b}$. Raise both sides to the $x$:

$$b^x = \left(e^{\ln b}\right)^x = e^{x \ln b}.$$

This is the **fundamental reduction** — every exponential with any base is secretly an $e$-exponential with a constant stretch applied to the exponent. Once you see this, results about $e^x$ transfer immediately:

**Derivative of $b^x$.** Apply the chain rule to $e^{x \ln b}$:

$$\frac{d}{dx} b^x = \frac{d}{dx} e^{x \ln b} = e^{x \ln b} \cdot \ln b = b^x \ln b.$$

So $\dfrac{d}{dx}b^x = b^x \ln b$ — the "stapled-on" factor $\ln b$ that every non-$e$ base picks up, and that Euler's Number §5 uses to argue $e$ is the "right" base for calculus.

**Concrete check at $b = e$.** $\ln e = 1$, so $(e^x)' = e^x \cdot 1 = e^x$. ✓

## Worked examples

### Example 1 — Solving $e^x = k$ (0606 §6.3)

> **Solve $e^{2x} = 7$, giving your answer correct to 3 significant figures.**

Take $\ln$ of both sides:

$$\ln(e^{2x}) = \ln 7 \quad\Rightarrow\quad 2x = \ln 7 \quad\Rightarrow\quad x = \frac{\ln 7}{2} \approx \frac{1.9459}{2} \approx 0.973.$$

### Example 2 — A disguised quadratic (0606 §6.3)

> **Solve $e^{2x} - 5 e^x + 6 = 0$.**

The expression *looks* like an exponential equation, but the structure is hidden. Let $u = e^x$. Then $e^{2x} = (e^x)^2 = u^2$, and the equation becomes:

$$u^2 - 5u + 6 = 0.$$

Factorise:

$$(u - 2)(u - 3) = 0 \quad\Rightarrow\quad u = 2 \text{ or } u = 3.$$

Substitute back: $e^x = 2$ or $e^x = 3$. Take $\ln$:

$$x = \ln 2 \approx 0.693 \quad\text{or}\quad x = \ln 3 \approx 1.099.$$

**Check.** Both $u$ values are positive, so both give valid real $x$. (If a $u$ value were zero or negative, we'd reject it — $e^x$ is always positive.) $\boxed{x = \ln 2 \text{ or } x = \ln 3}$.

### Example 3 — Derivative with chain rule (A-Level gateway)

> **Find $\dfrac{dy}{dx}$ for $y = e^{3x^2 - 1}$.**

Use the chain rule. If $u = 3x^2 - 1$, then $y = e^u$ and $\dfrac{du}{dx} = 6x$:

$$\frac{dy}{dx} = e^u \cdot \frac{du}{dx} = e^{3x^2 - 1} \cdot 6x = 6x \, e^{3x^2 - 1}.$$

### Example 4 — Sketching a transformed exponential (0606 §6.1)

> **Sketch $y = 3 - e^{-x}$, showing any asymptotes and intercepts.**

Break the expression into transformations of $e^{-x}$:
- Start with $y = e^{-x}$ — decay curve, passes through $(0, 1)$, asymptote $y = 0$.
- Negate: $y = -e^{-x}$ — reflect across the $x$-axis, passes through $(0, -1)$, asymptote $y = 0$.
- Add $3$: $y = 3 - e^{-x}$ — shift up $3$ units, passes through $(0, 2)$, asymptote $y = 3$.

$y$-intercept: $y = 3 - e^0 = 3 - 1 = 2$, so the curve crosses the $y$-axis at $(0, 2)$.

$x$-intercept: set $3 - e^{-x} = 0 \Rightarrow e^{-x} = 3 \Rightarrow -x = \ln 3 \Rightarrow x = -\ln 3 \approx -1.10$.

As $x \to \infty$, $e^{-x} \to 0$, so $y \to 3$ from below. As $x \to -\infty$, $e^{-x} \to \infty$, so $y \to -\infty$.

The curve rises from $-\infty$, crosses the $x$-axis at $x = -\ln 3$, crosses the $y$-axis at $(0, 2)$, and approaches the horizontal asymptote $y = 3$.

## Common misconceptions

### 1. "$e^x$ grows like a polynomial."

Wrong — and the failure is eventual, not immediate. For small $x$, a polynomial like $y = x^5$ may overshoot $y = e^x$; at $x = 5$, $x^5 = 3125$ while $e^5 \approx 148$. But **every** polynomial loses to $e^x$ as $x \to \infty$: at $x = 20$, $x^5 = 3.2 \times 10^6$ but $e^{20} \approx 4.85 \times 10^8$ — roughly 150 times bigger. At $x = 50$, $e^x$ dwarfs $x^{100}$ by a wide margin. This is the **exponential beats polynomial** fact, and every computer-science analysis of algorithm running time uses it.

**Fix.** Show the student a numerical table: $x = 1, 5, 10, 20, 50$, columns for $x^2$, $x^5$, $e^x$. Watch $e^x$ overtake and leave every polynomial behind. Connects directly to [[Exponential Graphs (Vocab)]] and the $y = 2^x$ vs $y = x^2$ comparison.

### 2. "$e^{a+b} = e^a + e^b$."

Wrong — see the warning callout above. Addition in the exponent becomes *multiplication* of outputs, never addition.

**Fix.** Plug in $a = b = 1$: $e^2 \approx 7.39$, $e^1 + e^1 \approx 5.44$. Then $e^1 \cdot e^1 = e^2 \approx 7.39$. ✓. The correct splitting is into a product.

### 3. "To solve $e^{2x} = e^x + 6$, divide both sides by $e^x$."

Tempting but wrong — dividing is only fine if you know the term you are dividing by is non-zero. (It is here, since $e^x > 0$ always, but the method still leaves a messy result.) The *right* move is to treat it as a disguised quadratic by substituting $u = e^x$. See Example 2 above.

**Fix.** Any equation where the same "base-to-the-power-of-something" appears in both places — $e^{2x}$ alongside $e^x$, or $4^x$ alongside $2^x$ (since $4^x = (2^x)^2$) — is almost certainly a disguised quadratic. Trigger: *see the same building block twice*.

### 4. "$e^x$ is a constant."

Wrong — and this comes from misreading notation. $e$ by itself is the constant $2.71828\ldots$; $e^x$ is a *function of $x$*. The constant $e$ is to the exponential function $e^x$ as the constant $2$ is to the function $2^x$. If someone says "the value of $e$ at $x = 3$," they mean $e^3$, the function evaluated at $3$.

**Fix.** Write $f(x) = e^x$ on the board and emphasize the argument $x$. Compare $f(0) = 1$, $f(1) = e \approx 2.718$, $f(2) = e^2 \approx 7.389$.

### 5. "You can't take $\ln$ of a negative number, so you can't take $e$ of a negative number either."

Wrong — these are opposites. $\ln$ is undefined for $x \leq 0$ (because $e^y > 0$ always). But $e^x$ is defined for every real $x$ — including negatives — and $e^{\text{negative}}$ just gives a small positive number: $e^{-1} = 1/e \approx 0.368$, $e^{-10} \approx 0.0000454$. The student is confusing the *output* restriction of $\ln$ with an imagined *input* restriction on $e^x$.

**Fix.** $e^x$'s domain is all real numbers; its range is $(0, \infty)$. $\ln x$'s domain is $(0, \infty)$; its range is all real numbers. The two domains and ranges swap because $\ln$ and $e^x$ are inverses.

## Beyond the syllabus

### $e^x$ as the unique solution to $f' = f$

Suppose a function $f$ satisfies $f'(x) = f(x)$ for every $x$ and $f(0) = 1$. Then $f(x) = e^x$ — the exponential is the *only* function with these two properties.

**Sketch of why.** Consider the ratio $g(x) = \dfrac{f(x)}{e^x}$. Differentiating (quotient or product rule):

$$g'(x) = \frac{f'(x) \cdot e^x - f(x) \cdot e^x}{e^{2x}} = \frac{f(x) - f(x)}{e^x} = 0,$$

using $f'(x) = f(x)$ and $(e^x)' = e^x$. So $g$ is constant. At $x = 0$: $g(0) = f(0)/e^0 = 1/1 = 1$. So $g(x) = 1$ everywhere, meaning $f(x) = e^x$. $\blacksquare$

This is the cleanest way to characterise $e^x$: "the function that is its own derivative, normalised to pass through $(0, 1)$." Every physical process governed by "rate of change ∝ current amount" — radioactive decay, compound interest, Newton's cooling — has $e^{kt}$ as its solution *because* of this uniqueness (see [[Exponential Growth and Decay]] §6).

### Euler's formula — $e^x$ visits the complex plane

Extending $e^x$ to complex inputs gives the most famous identity in mathematics:

$$e^{i\theta} = \cos\theta + i\sin\theta \qquad (i = \sqrt{-1})$$

At $\theta = \pi$: $e^{i\pi} = -1$, equivalently $e^{i\pi} + 1 = 0$ — **Euler's identity**, combining $e$, $i$, $\pi$, $1$, and $0$ in one line. See [[Complex Numbers]] for the derivation from the power series (substitute $i\theta$ for $x$ in $\sum x^k/k!$ and separate real and imaginary parts).

This is not idle prettiness. Every electrical engineer analysing alternating current writes circuit voltages as $V(t) = V_0 e^{i\omega t}$, takes derivatives (multiplication by $i\omega$), integrates (division by $i\omega$), and reads off the physical voltage as the real part. The same $e^x$ that powers compound interest powers every phone charger and power grid on the planet.

### The natural exponential in probability

$e^x$ hides inside two of the most important distributions in statistics:

- **Normal distribution**: $\phi(x) = \dfrac{1}{\sqrt{2\pi}} e^{-x^2/2}$. The bell curve. Its shape is a $e^{-x^2/2}$ under a normalising constant; see [[Normal Distribution]].
- **Poisson distribution**: $P(X = k) = \dfrac{\mu^k e^{-\mu}}{k!}$. Counts of rare, independent events; see [[Poisson Distribution]].

Both contain $e$ for the same deep reason: they are the unique distributions that satisfy certain "naturalness" conditions, and naturalness forces $e$ to appear. The full story is in [[Euler's Number]] §4.

## Exam Notes

### Cambridge 0606

**§6.1 Properties and graphs of $y = e^x$ and $y = \ln x$.** Sketching is a common 2–3 mark task. Expected features:
- Shape (rising, concave up for $e^x$; rising, concave down for $\ln x$)
- Asymptote — state the *equation*, not just "the axis." For $e^x$: $y = 0$. For $\ln x$: $x = 0$.
- $y$-intercept for $e^x$: $(0, 1)$. $x$-intercept for $\ln x$: $(1, 0)$.
- Values $e^0 = 1$, $\ln 1 = 0$, $\ln e = 1$.

**§6.3 Solving $e^x = k$ and $\ln x = k$.** Technique: take $\ln$ (for $e^x$) or raise $e$ to the power (for $\ln x$). Expect disguised-quadratic problems as in Example 2. "Giving your answer correct to 3 s.f." → leave the exact form $\ln 2$, $\ln 3$ only if the question allows it; otherwise convert.

**Common 0606 exam styles:**
- "Sketch $y = 2 + e^{-x}$, stating clearly any asymptotes and intercepts." — transformation on top of $e^{-x}$.
- "Solve $3 e^{2x} - 7 e^x - 6 = 0$." — disguised quadratic in $u = e^x$.
- "The population of a town is modelled by $P = 5000 e^{0.03t}$. Find the value of $t$ when the population reaches 7500." — $e^{kt}$ application, same machinery as [[Exponential Growth and Decay]] §5.

### A-Level

$e^x$ is the workhorse of A-Level calculus:
- **Year 1 (Core Pure):** differentiate $e^{f(x)}$ using the chain rule; integrate $e^{ax+b}$ as $\tfrac{1}{a} e^{ax+b} + C$.
- **Year 2:** logarithmic differentiation for $y = x^x$ and $y = (f(x))^{g(x)}$; solving first-order separable differential equations ending in $\ln$ and $e$.
- **Further Maths:** complex extension $e^{i\theta} = \cos\theta + i\sin\theta$; Taylor series $e^x = \sum x^k/k!$ treated rigorously; hyperbolic functions $\cosh x = \tfrac{e^x + e^{-x}}{2}$, $\sinh x = \tfrac{e^x - e^{-x}}{2}$.

The proof that $(e^x)' = e^x$ is usually stated rather than proved on A-Level syllabuses — but the power-series argument above is exactly what appears in Further Maths / AA HL / BC.

### IB AA

**SL** — Uses $e^x$ and $\ln x$ as standard functions; expected to differentiate and integrate them without derivation. **HL** — Includes the power series (Topic 5), the differential equation $\tfrac{dy}{dx} = ky$ with solution $y = Ae^{kx}$ (Topic 5), and complex exponentials via Euler's formula (Topic 1.12).

### AP Calculus

**AB** — Derivative and integral of $e^x$ listed as named rules. Separable differential equations with exponential solutions appear in Unit 7. **BC** — Adds the Taylor series $e^x = \sum x^k/k!$ with radius of convergence $R = \infty$ (Unit 10).

## Connections

- **Inverse of:** [[Logarithms]] — $e^x$ and $\ln x$ are inverse functions; the derivative of $\ln$ falls out of the derivative of $e^x$ via the inverse function rule (proved above).
- **Prerequisite:** [[Laws of Indices]] — every exp law in this card is an index law specialised to base $e$.
- **Prerequisite:** [[Euler's Number]] — the constant $e$ and its three equivalent definitions (compound-interest limit, power series, self-derivative). The power series definition is what makes the $(e^x)' = e^x$ proof work.
- **Prerequisite:** [[Differentiation]] — the derivative machinery (power rule on each term, chain rule) used in the proofs.
- **Catalogue-counterpart:** [[Exponential Graphs (Vocab)]] — the shape-recognition vocab card for $y = a \cdot b^x$; this card is the function-as-object deep dive.
- **Application:** [[Exponential Growth and Decay]] — $e^{kt}$ as the model for every process where rate ∝ current amount. That card uses $e^x$ operationally; this card builds it from the ground up.
- **Leads to:** [[Integration]] — $\int e^x \, dx = e^x + C$; $\int e^{ax+b} \, dx = \tfrac{1}{a} e^{ax+b} + C$.
- **Leads to:** [[Differential Equations]] — $e^{kt}$ solves $\tfrac{dy}{dt} = ky$; every linear first-order ODE lives on this family.
- **Leads to:** [[Complex Numbers]] — Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$; Euler's identity $e^{i\pi} + 1 = 0$.
- **Appears in probability:** [[Normal Distribution]], [[Poisson Distribution]] — both use $e^{-\text{something}}$ as their core shape.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $e^x$ | `e^x` | Standard form — preferred for simple exponents |
| $e^{f(x)}$ | `e^{f(x)}` | Braces required when the exponent is more than one character |
| $\exp(x)$ | `\exp(x)` | Alternative — use when the exponent is bulky |
| $e^{a+b} = e^a e^b$ | `e^{a+b} = e^a e^b` | Product law (the key exp identity) |
| $e^{-x}$ | `e^{-x}` | Decay form |
| $\dfrac{d}{dx} e^x = e^x$ | `\dfrac{d}{dx} e^x = e^x` | The headline identity |
| $\dfrac{d}{dx} e^{f(x)} = f'(x) e^{f(x)}$ | `\dfrac{d}{dx} e^{f(x)} = f'(x) e^{f(x)}` | Chain rule with $e$ |
| $\displaystyle\sum_{k=0}^{\infty} \dfrac{x^k}{k!}$ | `\sum_{k=0}^{\infty} \dfrac{x^k}{k!}` | Power series definition |
| $e^{i\theta} = \cos\theta + i \sin\theta$ | `e^{i\theta} = \cos\theta + i \sin\theta` | Euler's formula |
| $b^x = e^{x \ln b}$ | `b^x = e^{x \ln b}` | General-base reduction |
