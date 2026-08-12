---
chinese: 极限 (jíxiàn)
prerequisites:
  - "[[Arithmetic and Geometric Progressions]]"
leads_to:
  - "[[Differentiation]]"
  - "[[Integration]]"
  - "[[Fundamental Theorem of Calculus]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - syllabus/0606-14-1
  - type/definition
  - type/vocabulary
  - notation/limit
---

# Limit 极限

## Definition

### Formal

We say that

$$\lim_{x \to a} f(x) = L$$

if for every $\varepsilon > 0$ (no matter how small), there exists a $\delta > 0$ such that

$$0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \varepsilon$$

Read this as: "$f(x)$ can be made **arbitrarily close** to $L$ by taking $x$ sufficiently close to $a$ (but not equal to $a$)."

### Intuitive

A limit answers the question: **"What value is $f(x)$ approaching as $x$ gets closer and closer to $a$?"**

The key word is *approaching* — we never ask what happens *at* $a$, only what happens *near* $a$. This is what makes limits powerful: they let us talk about behaviour at points where the function might not even be defined.

Think of walking toward a cliff edge. The limit describes where you're *heading*, not where you *are*. You can talk about the edge without stepping off it.

### 中文锚点 (Chinese Anchor)

极限："无限接近但不一定到达。"

核心问题：当$x$越来越接近$a$时，$f(x)$越来越接近哪个值？

关键词：**任意**（arbitrary）。不是"很近"，不是"非常近"，而是"想要多近就有多近"——这就是$\varepsilon$-$\delta$定义的精髓。

$$\lvert f(x) - L \rvert < \varepsilon$$

翻译：$f(x)$和$L$之间的距离小于$\varepsilon$。而$\varepsilon$可以是**任意小**的正数。

> [!tip] 为什么叫"极限"？
> "极"是极端、极致的意思——取到极端的边界值。英文 limit 也是"边界"的意思。名字本身就在说：我们在看一个过程走到极端时会趋近什么值。

## Notation

| Convention | Example | Read as | Notes |
|---|---|---|---|
| Limit notation | $\lim_{x \to a} f(x) = L$ | "the limit of $f(x)$ as $x$ approaches $a$ is $L$" | Standard notation across all curricula |
| One-sided (left) | $\lim_{x \to a^-} f(x)$ | "the limit as $x$ approaches $a$ from the left" | The superscript minus means from below |
| One-sided (right) | $\lim_{x \to a^+} f(x)$ | "the limit as $x$ approaches $a$ from the right" | The superscript plus means from above |
| Informal delta notation | $\dfrac{\delta y}{\delta x} \to \dfrac{dy}{dx}$ as $\delta x \to 0$ | "delta-$y$ over delta-$x$ approaches $dy$-over-$dx$" | 0606 uses this to introduce derivatives |

> [!warning] $\delta$ vs $d$
> $\delta x$ (or $\Delta x$) means a **small but finite** change in $x$ — a real number you can measure. $dx$ is what $\delta x$ becomes in the limit: an **infinitesimally small** change, formalised at university level as a **differential form**. The key difference: $\delta x$ is a gap you can point to on a graph; $dx$ is a mathematical object that only makes rigorous sense through the machinery of limits. $\dfrac{dy}{dx}$ is genuinely the ratio of $dy$ to $dx$ — see [[Differentiation]] for the full story.

## The Word "Arbitrary" 任意

The word **arbitrary** appears throughout higher mathematics. It means "any — with no restriction on which one." When we say "for every $\varepsilon > 0$", we mean:

- $\varepsilon = 1$? Sure.
- $\varepsilon = 0.001$? Sure.
- $\varepsilon = 0.000000001$? Still yes.

No matter how absurdly small you choose $\varepsilon$, I can find a $\delta$ that works. This is what "arbitrarily close" means — there is no lower bound on how close we can get. The opponent picks the challenge ($\varepsilon$), and we must answer it ($\delta$).

> [!warning] "Arbitrarily close" ≠ "infinitely close"
> Every $\varepsilon$ you pick is a **finite**, positive number. "Arbitrarily close" means "as close as you *choose*" — you can always choose a smaller $\varepsilon$, but each one is still a real, finite distance. There is no $\varepsilon = 0$ and no "infinitely small" $\varepsilon$.
>
> "Infinitely close" implies some actual infinite quantity exists. It doesn't — that's exactly the vague thinking the ε-δ definition was invented to replace. The power of the definition is that it only ever uses finite numbers, yet captures the idea of "no gap remaining."

> [!info] The ε-δ game
> Think of the ε-δ definition as a game between two players:
>
> 1. **Opponent** picks $\varepsilon > 0$ (how close to $L$ they demand $f(x)$ must be)
> 2. **You** must find $\delta > 0$ (how close to $a$ you need $x$ to be) so that $f(x)$ lands within $\varepsilon$ of $L$
>
> If you can win **every round** regardless of how small the opponent picks $\varepsilon$, then the limit exists and equals $L$.

## Key Facts / Properties

### Why Limits are the Foundation of Calculus

Every major concept in calculus is defined using limits:

| Concept | Defined as | The limit is... |
|---|---|---|
| **Derivative** | $\displaystyle\lim_{\delta x \to 0} \dfrac{f(x + \delta x) - f(x)}{\delta x}$ | ...of the gradient of a shrinking chord |
| **Definite integral** | $\displaystyle\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x$ | ...of a sum of shrinking rectangles |
| **Continuity** | $\displaystyle\lim_{x \to a} f(x) = f(a)$ | ...equals the actual value |

Without limits, we cannot make "getting closer" precise. Limits turn hand-waving into proof.

### Limit Laws

If $\lim_{x \to a} f(x) = L$ and $\lim_{x \to a} g(x) = M$, then:

| Law | Statement |
|---|---|
| Sum | $\lim_{x \to a} [f(x) + g(x)] = L + M$ |
| Difference | $\lim_{x \to a} [f(x) - g(x)] = L - M$ |
| Product | $\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M$ |
| Quotient | $\lim_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{L}{M}$, provided $M \neq 0$ |
| Scalar | $\lim_{x \to a} [k \cdot f(x)] = k \cdot L$ |
| Power | $\lim_{x \to a} [f(x)]^n = L^n$ |

These laws are why we can "plug in" for most well-behaved functions: if $f$ is a polynomial, then $\lim_{x \to a} f(x) = f(a)$.

### When Limits Don't Exist

A limit $\lim_{x \to a} f(x)$ **does not exist** if:

1. **Left ≠ Right.** The function approaches different values from each side:
   $\lim_{x \to a^-} f(x) \neq \lim_{x \to a^+} f(x)$

2. **Unbounded.** The function grows without bound (e.g., $\lim_{x \to 0} \dfrac{1}{x^2} = +\infty$). We write $\to \infty$ as a shorthand but the limit does not exist as a real number.

3. **Oscillation.** The function oscillates indefinitely (e.g., $\lim_{x \to 0} \sin\dfrac{1}{x}$).

## Common Misconceptions (Teaching Notes)

### 1. "The limit is the value of the function at that point"

Students confuse $\lim_{x \to a} f(x)$ with $f(a)$. These are often equal (for continuous functions), but the whole point of limits is that they work even when $f(a)$ is undefined.

**Fix:** Show $f(x) = \dfrac{x^2 - 1}{x - 1}$ at $x = 1$. The function is undefined at $x = 1$ (division by zero), but:

$$\dfrac{x^2 - 1}{x - 1} = \dfrac{(x-1)(x+1)}{x-1} = x + 1 \quad (x \neq 1)$$

So $\lim_{x \to 1} f(x) = 2$, even though $f(1)$ doesn't exist.

### 2. "Approaching means never getting there"

Some students think limits describe processes that "never finish." In reality, the limit is a precise value — $L$ — that we can pin down exactly. The process of approaching is just the intuition; the ε-δ definition is the rigorous statement.

### 3. "Infinity is a number"

When we write $\lim_{x \to \infty}$ or $\lim_{x \to 0} \dfrac{1}{x^2} = \infty$, students treat $\infty$ as a real number. It isn't — it's a shorthand for "grows without bound."

**Fix:** Ask: "What is $\infty + 1$? Is it bigger than $\infty$?" If these questions feel nonsensical, that's because $\infty$ isn't a number.

### 4. "Arbitrarily close means infinitely close"

Students hear "arbitrarily close" and picture some kind of infinite or magical closeness. But every $\varepsilon$ in the definition is a **finite** positive number — $0.01$, $0.0001$, never $0$, never "infinity small." The trick is that *no finite distance is small enough to escape* — for any $\varepsilon$ you name, we can still get closer than that. That's not infinity; that's the power of "for all."

**Fix:** Ask the student: "Give me a distance, any distance." Whatever they say ($0.001$, $10^{-100}$, anything), show them you can find a $\delta$ that works. Then ask: "Can you pick one where I *can't* answer?" They can't — and that's the whole definition, no infinity needed.

### 5. Confusing δx and dx

Students see $\dfrac{\delta y}{\delta x}$ and $\dfrac{dy}{dx}$ as interchangeable. The first is a ratio of two actual (small) numbers. The second is the *limit* of that ratio — a single object, the derivative. The transition from $\delta$ to $d$ is exactly where limits happen.

## Exam Notes

### Cambridge 0606

- 14.1 requires understanding the "idea of a derived function" and an "informal limit concept"
- First principles derivation is **not required** at 0606
- The $\delta$-notation ($\dfrac{\delta y}{\delta x} \to \dfrac{dy}{dx}$ as $\delta x \to 0$) appears in the syllabus description (14.2)
- Students should understand that the derivative is the limit of a gradient — they are not expected to write ε-δ proofs

### OxAQA 9260

- Limits are **not explicitly in the spec**
- However, A13 says "gradient function" which implicitly requires the limit idea
- Understanding limits helps students see why the power rule works — see [[Power Rule]]

### AP / IB / A-Level

- **AP Calculus AB/BC:** requires formal limit definition and evaluation
- **IB Mathematics AA HL:** includes limits and the squeeze theorem
- **A-Level Further Mathematics:** includes ε-δ definitions
- The ε-δ definition in this note is college-level — it's here because understanding *why* calculus works makes the rules unforgettable

## Connections

- **Leads to:** [[Differentiation]] — the derivative is a limit of $\dfrac{\delta y}{\delta x}$
- **Leads to:** [[Integration]] — the definite integral is a limit of Riemann sums
- **Leads to:** [[Fundamental Theorem of Calculus]] — connects derivatives and integrals, both defined via limits
- **Key example:** [[Power Rule]] — proved by taking a limit after binomial expansion
- **Related:** [[Tangents and Normals]] — the tangent gradient is the limit of chord gradients

> [!info] Beyond syllabus — Why calculus needed 150 years to become rigorous
> Newton and Leibniz invented calculus in the 1660s–1680s, but their arguments relied on vague ideas like "infinitely small quantities." Mathematicians argued about whether this was valid for over a century. It wasn't until the 1820s that Cauchy and Weierstrass finally defined limits with the ε-δ framework, putting calculus on solid logical ground. The definition you see above is the result of 150 years of mathematicians trying to answer: "What *exactly* do we mean by 'getting closer'?"

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\lim_{x \to a} f(x) = L$ | `\lim_{x \to a} f(x) = L` | Standard limit notation |
| $\lim_{x \to a^+}$ | `\lim_{x \to a^+}` | Right-hand limit |
| $\lim_{x \to a^-}$ | `\lim_{x \to a^-}` | Left-hand limit |
| $\varepsilon$ | `\varepsilon` | Epsilon — the "closeness" challenge |
| $\delta$ | `\delta` | Delta — the "nearness" response |
| $\lvert x - a \rvert < \delta$ | `\lvert x - a \rvert < \delta` | Distance from $x$ to $a$ is less than $\delta$ |
| $\dfrac{\delta y}{\delta x}$ | `\frac{\delta y}{\delta x}` or `\dfrac{\delta y}{\delta x}` | Finite difference ratio (`\dfrac` for inline) |
| $\dfrac{dy}{dx}$ | `\frac{dy}{dx}` or `\dfrac{dy}{dx}` | Derivative (`\dfrac` for inline) |
