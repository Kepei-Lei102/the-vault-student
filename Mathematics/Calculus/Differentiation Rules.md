---
chinese: 微分法则 (wēifēn fǎzé)
prerequisites:
  - "[[Differentiation]]"
  - "[[Power Rule]]"
  - "[[Product Rule]]"
  - "[[Chain Rule]]"
  - "[[Trigonometric Identities]]"
  - "[[Trigonometric Functions]]"
  - "[[Exponential Function]]"
  - "[[Logarithms]]"
  - "[[Radians]]"
  - "[[Limit]]"
  - "[[Quotient Rule]]"
  - "[[Squeeze Theorem]]"
leads_to:
  - "[[Standard Integrals]]"
  - "[[Implicit Differentiation]]"
  - "[[Logarithmic Differentiation]]"
  - "[[L'Hôpital's Rule]]"
  - "[[Binomial Series]]"
  - "[[Fundamental Theorem of Calculus]]"
  - "[[Maclaurin Series]]"
  - "[[Numerical Methods]]"
  - "[[Parametric Differentiation]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-14-3
  - syllabus/9709-1-7
  - syllabus/9709-2-4
  - syllabus/9709-3-4
  - syllabus/9231-2-3
  - type/deep
  - type/proof
  - type/reference-table
  - notation/derivative
  - misconception/d-dx-not-fraction
  - misconception/sin-x-derivative-cos-x-only-in-radians
---

# Differentiation Rules 微分法则

## Definition

This card is the **derivative table for the elementary functions** — trigonometric, exponential, logarithmic, and (beyond syllabus) inverse-trigonometric. Together with [[Power Rule]], [[Product Rule]], and [[Chain Rule]], the entries in this table let you differentiate every closed-form expression you'll meet in 0606 / A-Level / IB / AP.

Every row in the table comes with a **proof** — not a "memorise this." Each derivative is a logical consequence of (a) the unit-circle definition of the trig functions, (b) the limit $\lim_{h \to 0}\sin h / h = 1$ (proved in [[Radians]]), (c) the power-series definition of $e^x$ (proved in [[Exponential Function]]), and (d) the differentiation rules from earlier cards. Memorise the table for speed on exam day; understand the proofs so you can rebuild any forgotten row from scratch.

### 中文锚点

微分法则 = 把 $\sin, \cos, \tan, e^x, \ln x$ 等基本函数的导数列成表。每一条都有证明，不是死记硬背。导数的来源：单位圆定义（三角函数）、极限 $\sin h / h \to 1$（弧度的关键极限）、$e^x$ 的幂级数定义、以及链式法则 / 乘法法则等更基础的微分工具。背表可以提速度，理解证明可以保证万一忘了能现场重建。

> [!tip] All trig derivatives assume RADIANS
> The clean table $\frac{d}{dx}\sin x = \cos x$ etc. is **only true if $x$ is measured in radians**. In degree mode, $\frac{d}{dx}\sin x^\circ = \frac{\pi}{180}\cos x^\circ$ — every derivative picks up a factor of $\pi/180$. This is one of the deep reasons radians are the "natural" unit for calculus; see [[Radians]] for the squeeze-theorem proof of $\lim_{h \to 0}\sin h / h = 1$ that depends on radian measure for sector area.

---

## The Reference Table

| Function $f(x)$ | Derivative $f'(x)$ | How proved |
|---|---|---|
| $\sin x$ | $\cos x$ | first principles + sum formula + $\sin h/h \to 1$ |
| $\cos x$ | $-\sin x$ | co-function identity $\cos x = \sin(\pi/2 - x)$ + chain rule |
| $\tan x$ | $\sec^2 x$ | quotient rule on $\sin x / \cos x$ |
| $\sec x$ | $\sec x\tan x$ | chain rule on $(\cos x)^{-1}$ |
| $\csc x$ | $-\csc x\cot x$ | chain rule on $(\sin x)^{-1}$ |
| $\cot x$ | $-\csc^2 x$ | quotient rule on $\cos x / \sin x$ |
| $e^x$ | $e^x$ | power-series of $e^x$ — see [[Exponential Function]] |
| $a^x$ | $a^x \ln a$ | rewrite as $e^{x \ln a}$ + chain rule |
| $\ln x$ | $\dfrac{1}{x}$ | inverse function rule — see [[Exponential Function]] |
| $\log_a x$ | $\dfrac{1}{x \ln a}$ | change of base $\log_a x = \ln x / \ln a$ |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1 - x^2}}$ | implicit differentiation (beyond 0606) |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1 - x^2}}$ | $\arccos x = \pi/2 - \arcsin x$ |
| $\arctan x$ | $\dfrac{1}{1 + x^2}$ | implicit differentiation + $\sec^2 = 1 + \tan^2$ |

The proofs follow.

### Memorise? — per board

The companion table for exam strategy. Same legend as [[Standard Integrals]]: ✅ given on booklet, 📝 must memorise, 🛠 derive (e.g. via chain rule on a base form), ⚪ off-syllabus on this board. Sources of truth: [[MF19 Reference (9709)]], [[Edexcel IAL Reference]], [[OxAQA 9660 Reference]], [[AP Calculus Reference]].

| $f(x)$ | $f'(x)$ | 9709 | IAL | 9660 | AP |
|---|---|:---:|:---:|:---:|:---:|
| $x^n$ | $n x^{n-1}$ | ✅ | 📝 | 📝 | 📝 |
| $\sin x$ | $\cos x$ | ✅ | 📝 | 📝 | 📝 |
| $\cos x$ | $-\sin x$ | ✅ | 📝 | 📝 | 📝 |
| $\tan x$ | $\sec^2 x$ | ✅ | ✅ ($\tan kx$ given) | ✅ ($\tan kx$ given) | 📝 |
| $\sec x$ | $\sec x \tan x$ | ✅ | ✅ | ✅ | 📝 |
| $\csc x$ | $-\csc x \cot x$ | ✅ | ✅ | ✅ | 📝 |
| $\cot x$ | $-\csc^2 x$ | ✅ | ✅ | ✅ | 📝 |
| $e^x$ | $e^x$ | ✅ | 📝 | 📝 | 📝 |
| $a^x$ | $a^x \ln a$ | 🛠 | 🛠 | 🛠 | 📝 |
| $\ln x$ | $\dfrac{1}{x}$ | ✅ | 📝 | 📝 | 📝 |
| $\log_a x$ | $\dfrac{1}{x \ln a}$ | 🛠 | 🛠 | 🛠 | 📝 |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1 - x^2}}$ | ⚪ 9231 only | ⚪ FP3 | ✅ | 📝 |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1 - x^2}}$ | ⚪ 9231 only | ⚪ FP3 | ✅ | 📝 |
| $\arctan x$ | $\dfrac{1}{1 + x^2}$ | ✅ | 📝 | ✅ | 📝 |
| $\sinh x, \cosh x, \tanh x$ | $\cosh x, \sinh x, \mathrm{sech}^2 x$ | ⚪ 9231 | ⚪ FP3 | ✅ | ⚪ off-syllabus |
| $\sinh^{-1} x$ | $\dfrac{1}{\sqrt{1 + x^2}}$ | ⚪ 9231 | ⚪ FP3 | ✅ | ⚪ off-syllabus |
| $\cosh^{-1} x$ | $\dfrac{1}{\sqrt{x^2 - 1}}$ | ⚪ 9231 | ⚪ FP3 | ✅ | ⚪ off-syllabus |
| $\tanh^{-1} x$ | $\dfrac{1}{1 - x^2}$ | ⚪ 9231 | ⚪ FP3 | ✅ | ⚪ off-syllabus |

### Differentiation rules — per board

| Rule | 9709 | IAL | 9660 | AP |
|---|:---:|:---:|:---:|:---:|
| **Chain rule** $\dfrac{d}{dx}f(g(x)) = f'(g(x))g'(x)$ | 📝 | 📝 | 📝 | 📝 |
| **Product rule** $(uv)' = u'v + uv'$ | ✅ | 📝 | 📝 | 📝 |
| **Quotient rule** $(u/v)' = \dfrac{u'v - uv'}{v^2}$ | ✅ | ✅ | ✅ | 📝 |
| **Parametric chain** $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ | ✅ | 📝 | 📝 | 📝 |
| **Implicit differentiation** (technique, not formula) | 🛠 | 🛠 | 🛠 | 🛠 |
| **Inverse-function rule** $(f^{-1})'(y) = 1/f'(x)$ | 📝 | 📝 | 📝 | 📝 |

> [!info] The cross-board patterns this table makes visible
>
> **Pattern 1 — Cambridge MF19 wins on the foundational table.** All six basic trig + exp + log derivatives ($\sin', \cos', e^x, \ln'$) are on MF19. IAL, 9660, and AP all leave them as memorise. *Cambridge students have the easiest exam-day for foundational lookups.*
>
> **Pattern 2 — IAL and 9660 win on extended trig.** $\sec', \csc', \cot', \tan kx$ all given on both. Cambridge MF19 also has $\sec', \csc', \cot'$ but not $\tan kx$ explicitly. AP has none.
>
> **Pattern 3 — 9660 dominates the inverse-trig and hyperbolic rows.** Six rows where 9660 is the only ✅ — all $\arcsin / \arccos$ (Cambridge has these only on the 9231 Further page; IAL on FP3) and the entire hyperbolic + inverse-hyperbolic family. *9660 is the only standard-Pure board that hands you these.*
>
> **Pattern 4 — Chain rule is universal memorisation.** No board prints the general chain-rule formula on the booklet. Every student internalises it. The parametric chain ($\dfrac{dy}{dx} = \frac{dy/dt}{dx/dt}$) is on MF19 but not the others — *9709 is the unique board where parametric students don't have to derive the chain rule for time-parametrised motion*.
>
> **Pattern 5 — Product rule asymmetry.** Quotient rule is on every booklet; product rule is on MF19 only. The other three boards make you memorise it (interesting, since product rule is *easier* than quotient — the asymmetry suggests booklet-design history rather than pedagogical principle).

---

## Trigonometric Derivatives

### $\dfrac{d}{dx}\sin x = \cos x$ — the cornerstone

This is the only trig derivative that genuinely needs first principles; the rest follow from chain rule, quotient rule, or co-function identities.

By the definition of the derivative:

$$
\frac{d}{dx}\sin x = \lim_{h \to 0}\frac{\sin(x + h) - \sin x}{h}.
$$

Apply the sum formula for $\sin(A + B)$ from [[Trigonometric Identities]]:

$$
\sin(x + h) = \sin x\cos h + \cos x\sin h.
$$

Substitute and rearrange:

$$
\frac{\sin(x + h) - \sin x}{h} = \frac{\sin x\cos h + \cos x\sin h - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}.
$$

Now take the limit. Two key limits do the work:

- $\displaystyle\lim_{h \to 0}\frac{\sin h}{h} = 1$ — proved by squeeze theorem in [[Radians]]
- $\displaystyle\lim_{h \to 0}\frac{\cos h - 1}{h} = 0$ — derived below

Therefore:

$$
\frac{d}{dx}\sin x = \sin x \cdot 0 + \cos x \cdot 1 = \cos x. \;\boxed{}
$$

> [!info] Why $\lim_{h \to 0}(\cos h - 1)/h = 0$
> Multiply top and bottom by $\cos h + 1$ (the conjugate trick):
> $$\frac{\cos h - 1}{h} = \frac{(\cos h - 1)(\cos h + 1)}{h(\cos h + 1)} = \frac{\cos^2 h - 1}{h(\cos h + 1)} = \frac{-\sin^2 h}{h(\cos h + 1)} = -\frac{\sin h}{h} \cdot \frac{\sin h}{\cos h + 1}.$$
> As $h \to 0$: the first factor goes to $1$, the second factor goes to $0/2 = 0$, so the whole thing goes to $0$. The Pythagorean identity $\cos^2 h - 1 = -\sin^2 h$ is the key move.

> [!warning] Beyond syllabus — L'Hôpital is the obvious tool, and it's circular here
> A student who already knows **L'Hôpital's rule** will spot $\sin h / h$ as a textbook $0/0$ indeterminate form and reach for it instinctively: differentiate top and bottom → $\cos h / 1$ → take the limit → $1$. The answer is correct. The *reasoning is circular*. L'Hôpital relies on knowing $\frac{d}{dh}\sin h = \cos h$ — but **that derivative is exactly what we're proving**, and the proof depends on $\lim_{h\to 0}\sin h / h$. Using L'Hôpital here assumes the conclusion in step one.
>
> This is the most famous "order of dependence" trap in early calculus. The clean order is:
> 1. Prove $\lim_{h\to 0}\sin h / h = 1$ by squeeze theorem on the unit circle (see [[Radians]]) — pure geometry, no derivatives needed.
> 2. Prove $\frac{d}{dx}\sin x = \cos x$ from first principles using that limit (this card, above).
> 3. Now L'Hôpital is unlocked — apply it freely to *other* $0/0$ limits like $\lim_{x\to 0}(\tan x)/x$, $\lim_{x\to 0}(1 - \cos x)/x^2$, etc.
>
> The takeaway: *what you can prove with L'Hôpital depends on what derivatives you already have*. L'Hôpital is a powerful theorem, not a magic wand. (See [[L'Hôpital's Rule]] for the full statement, the Cauchy-mean-value-theorem proof, and the standard tricks for converting $\infty - \infty$, $0\cdot\infty$, $1^\infty$, $0^0$, $\infty^0$ forms into $0/0$ or $\infty/\infty$.)

### $\dfrac{d}{dx}\cos x = -\sin x$ — the co-function trick

Use the co-function identity $\cos x = \sin\!\left(\tfrac{\pi}{2} - x\right)$ and chain rule:

$$
\frac{d}{dx}\cos x = \frac{d}{dx}\sin\!\left(\tfrac{\pi}{2} - x\right)=\cos\!\left(\tfrac{\pi}{2} - x\right) \cdot (-1) = -\sin x. \;\boxed{}
$$

(The inner derivative $\frac{d}{dx}(\tfrac{\pi}{2} - x) = -1$ is what supplies the negative sign — and that's *the* reason the derivative of $\cos$ is *negative* sin. The "co" in cosine carries through to the derivative as a sign flip.)

### $\dfrac{d}{dx}\tan x = \sec^2 x$ — quotient rule

Write $\tan x = \dfrac{\sin x}{\cos x}$ and apply the quotient rule (a corollary of [[Product Rule]]):

$$
\frac{d}{dx}\tan x = \frac{\cos x\cos x - \sin x(-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x. \;\boxed{}
$$

The numerator collapses to $1$ via the Pythagorean identity. Beautiful.

### $\sec x$, $\csc x$, $\cot x$ — chain rule on reciprocals

Each is a reciprocal of a known function; chain rule does the work.

$$
\frac{d}{dx}\sec x = \frac{d}{dx}(\cos x)^{-1} = -(\cos x)^{-2}\cdot (-\sin x) = \frac{\sin x}{\cos^2 x} = \sec x\tan x.
$$

$$
\frac{d}{dx}\csc x = \frac{d}{dx}(\sin x)^{-1} = -(\sin x)^{-2}\cdot \cos x = -\frac{\cos x}{\sin^2 x} = -\csc x\cot x.
$$

$$
\frac{d}{dx}\cot x = \frac{d}{dx}\frac{\cos x}{\sin x} = \frac{-\sin x\cdot\sin x - \cos x\cdot\cos x}{\sin^2 x} = -\frac{1}{\sin^2 x} = -\csc^2 x.
$$

> [!tip] The "co-pattern" in trig derivatives
> Notice the symmetry: $\sin'$, $\tan'$, $\sec'$ are all positive; $\cos'$, $\cot'$, $\csc'$ all carry a negative sign. The "co-" in *co*sine, *co*tangent, *co*secant signals "complement" — and the negative sign in the derivative is the algebraic shadow of that complement (chain rule on $\pi/2 - x$ supplies the $-1$). Once you internalise this, you'll never misremember the signs.

### Visualizing $\sin' = \cos$ — the $\pi/2$ shift

The graph of $\cos x$ is the graph of $\sin x$ shifted left by $\pi/2$. The derivative reads off slopes — at every $x$, the slope of $\sin x$ equals the height of $\cos x$ at the same $x$. Concretely: $\sin x$ has its maximum slope (steepest upward) at $x = 0$ where $\cos 0 = 1$; horizontal tangents at $x = \pi/2$ and $x = -\pi/2$ where $\cos(\pm\pi/2) = 0$; steepest downward at $x = \pi$ where $\cos\pi = -1$. Every feature of $\sin$'s slope behaviour matches $\cos$'s height.

![[differentiation-rules-sin-cos.svg]]

---

## Exponential Derivatives

### $\dfrac{d}{dx}e^x = e^x$ — the function that is its own derivative

[[Exponential Function]] proves this in detail using the power-series definition $e^x = \sum_{n=0}^\infty \frac{x^n}{n!}$. The argument: differentiate term by term, and the index shift on the sum recovers the same series. The shortest version:

$$
\frac{d}{dx}\sum_{n=0}^\infty \frac{x^n}{n!} = \sum_{n=1}^\infty \frac{n x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^\infty \frac{x^m}{m!} = e^x.
$$

The substitution $m = n - 1$ does the magic. This is the *only* function (up to a constant multiplier $f(x) = Ce^x$) that satisfies $f' = f$ — a uniqueness statement proved in [[Exponential Function]].

### $\dfrac{d}{dx}a^x = a^x \ln a$ — rewrite as $e^{x \ln a}$

By the change-of-base identity $a = e^{\ln a}$:

$$
a^x = (e^{\ln a})^x = e^{x \ln a}.
$$

Now apply chain rule with outer $e^u$ and inner $u = x \ln a$ (where $\ln a$ is a constant):

$$
\frac{d}{dx}a^x = e^{x \ln a} \cdot \ln a = a^x \ln a. \;\boxed{}
$$

> [!info] Beyond syllabus — why $e$ is "the" base
> Among all exponential functions $a^x$, the derivative is $a^x \ln a$ — there's a "constant of nature" $\ln a$ floating around. *The* base where this constant equals $1$ — i.e., where the function is its own derivative without any nuisance factor — is $a = e$. This is the deep reason $e$ is the natural choice for calculus, not just convention. (See [[Euler's Number]] for the full story.)

---

## Logarithmic Derivatives

### $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$ — attack the defining equation

The slick proof from [[Exponential Function]] (which closes the log–exp loop):

Let $y = \ln x$. By definition $e^y = x$. Differentiate both sides with respect to $x$:

$$
e^y \cdot \frac{dy}{dx} = 1 \;\;\Longrightarrow\;\; \frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}. \;\boxed{}
$$

The trick — *attack the defining equation* — is reusable. It's the same move that gives $\frac{d}{dx}\arcsin x$ below.

### $\dfrac{d}{dx}\log_a x = \dfrac{1}{x \ln a}$ — change of base

Use the change-of-base identity from [[Logarithms]]: $\log_a x = \dfrac{\ln x}{\ln a}$. Then:

$$
\frac{d}{dx}\log_a x = \frac{1}{\ln a} \cdot \frac{1}{x} = \frac{1}{x \ln a}. \;\boxed{}
$$

When $a = e$ this reduces to $1/x$ as expected.

> [!tip] Logarithmic differentiation — a beyond-syllabus tactic
> When you face $y = x^x$ or $y = (\sin x)^{\cos x}$ — *neither* power rule (exponent isn't constant) nor exponential rule (base isn't constant) applies — take $\ln$ of both sides first. From $y = x^x$, $\ln y = x \ln x$. Differentiate implicitly: $y'/y = \ln x + 1$, so $y' = x^x(\ln x + 1)$. The technique is called **logarithmic differentiation**. Standard in IB HL and AP BC.

---

## Inverse Trig Derivatives (beyond 0606 — IB HL / AP BC)

These three derivatives complete the calculus toolkit. The proof technique — *implicit differentiation on the defining equation* — is the same one that gave us $\ln'$ and $a^{x'}$. It generalises to any inverse function (the **inverse function rule**: if $f(g(x)) = x$ then $g'(x) = 1/f'(g(x))$).

### $\dfrac{d}{dx}\arcsin x = \dfrac{1}{\sqrt{1 - x^2}}$

Let $y = \arcsin x$ with $y \in [-\pi/2, \pi/2]$. By definition $\sin y = x$. Differentiate both sides:

$$
\cos y \cdot \frac{dy}{dx} = 1 \;\;\Longrightarrow\;\; \frac{dy}{dx} = \frac{1}{\cos y}.
$$

Use the Pythagorean identity to express $\cos y$ in terms of $x$: $\cos y = \sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}$. (The positive square root is correct because $y \in [-\pi/2, \pi/2]$ means $\cos y \geq 0$.) Therefore:

$$
\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1 - x^2}}. \;\boxed{}
$$

### $\dfrac{d}{dx}\arccos x = -\dfrac{1}{\sqrt{1 - x^2}}$

The cleanest proof uses the identity $\arccos x = \dfrac{\pi}{2} - \arcsin x$ (a co-function identity for the inverse functions). Differentiating:

$$
\frac{d}{dx}\arccos x = 0 - \frac{1}{\sqrt{1 - x^2}} = -\frac{1}{\sqrt{1 - x^2}}. \;\boxed{}
$$

The negative sign is the inverse-trig analogue of the negative sign in $\cos' x = -\sin x$. The "co-" pattern is preserved across the inverse.

### $\dfrac{d}{dx}\arctan x = \dfrac{1}{1 + x^2}$

Let $y = \arctan x$ with $y \in (-\pi/2, \pi/2)$. By definition $\tan y = x$. Differentiate:

$$
\sec^2 y \cdot \frac{dy}{dx} = 1 \;\;\Longrightarrow\;\; \frac{dy}{dx} = \frac{1}{\sec^2 y} = \frac{1}{1 + \tan^2 y} = \frac{1}{1 + x^2}. \;\boxed{}
$$

The middle step uses the Pythagorean corollary $\sec^2 y = 1 + \tan^2 y$ from [[Trigonometric Identities]].

> [!info] Beyond 0606 — but in scope for 9709 P3 / IB / AP — the integral side
> Reading these derivatives backwards gives two of the most useful integrals in calculus:
> $$\int \frac{dx}{\sqrt{1 - x^2}} = \arcsin x + C, \qquad \int \frac{dx}{1 + x^2} = \arctan x + C.$$
> These integrals are **explicitly in the 9709 Paper 3 §3.5 syllabus** ("integration of $1/(x^2 + a^2)$ giving $\tan^{-1}$") and on the A-Level / IB AA / AP BC formula sheets. The *derivatives* of inverse trig on this card aren't required at A-Level (only at IB HL / AP BC), but the integrals — the same formulas read backwards — are 9709 P3 standard. They will land in the [[Standard Integrals]] reference table. The $\arctan$ integral is particularly important — it's the model for "complete-the-square + trig substitution" on integrals like $\int \frac{dx}{x^2 + 4x + 13}$.

---

## Worked Examples — Combining the Table with Chain / Product / Quotient

The reference table gives derivatives of *single* elementary functions. Most exam questions need at least one combination rule on top.

**Example 1.** Differentiate $f(x) = e^{\sin x}$.

Chain rule with outer $e^u$ and inner $u = \sin x$:

$$
f'(x) = e^{\sin x} \cdot \cos x.
$$

**Example 2.** Differentiate $g(x) = \ln(\sec x)$.

Chain rule with outer $\ln u$ and inner $u = \sec x$:

$$
g'(x) = \frac{1}{\sec x} \cdot \sec x\tan x = \tan x.
$$

(Useful for integration: this means $\int \tan x \, dx = \ln|\sec x| + C$ — see [[Standard Integrals]].)

**Example 3.** Differentiate $h(x) = x^2 \cos x$.

Product rule:

$$
h'(x) = 2x\cos x + x^2(-\sin x) = 2x\cos x - x^2\sin x.
$$

**Example 4.** Find $\dfrac{dy}{dx}$ when $y = \sin(3x^2 + 1)$.

Chain rule with outer $\sin u$ and inner $u = 3x^2 + 1$:

$$
\frac{dy}{dx} = \cos(3x^2 + 1) \cdot 6x = 6x\cos(3x^2 + 1).
$$

**Example 5.** Differentiate $\arctan(2x)$.

Chain rule with outer $\arctan u$ and inner $u = 2x$:

$$
\frac{d}{dx}\arctan(2x) = \frac{1}{1 + (2x)^2} \cdot 2 = \frac{2}{1 + 4x^2}.
$$

**Example 6 (logarithmic differentiation).** Differentiate $y = x^x$.

Take $\ln$ of both sides: $\ln y = x\ln x$. Differentiate implicitly:

$$
\frac{1}{y}\frac{dy}{dx} = \ln x + 1 \;\;\Longrightarrow\;\; \frac{dy}{dx} = x^x(\ln x + 1).
$$

---

## Common Mistakes

1. **Degree mode.** $\frac{d}{dx}\sin x = \cos x$ assumes radians. In degree mode, the derivative is $\frac{\pi}{180}\cos x^\circ$. Calculus uses radians — universally — for this reason.
2. **Sign on $\cos'$.** $\frac{d}{dx}\cos x = -\sin x$, *not* $\sin x$. The negative sign comes from the chain rule on the inner $\pi/2 - x$ in the co-function proof.
3. **Confusing $\sec^{-1}$ with $\sec$.** $\sec^{-1} x = \arccos(1/x)$ (the inverse), not $\cos x$ (the reciprocal). For the reciprocal write $1/\sec x = \cos x$.
4. **Treating $\frac{d}{dx}$ as a fraction.** It's a *notation* (Leibniz's), not a quotient. You can't multiply both sides by $dx$ as if $dx$ were a number — though many textbooks abuse this notation in practice (separation of variables, change of variables in integration). The justifications exist (differentials, non-standard analysis) but go beyond high-school scope. Treat $\frac{d}{dx}$ as a single operator.
5. **Forgetting the chain rule on the inside.** $\frac{d}{dx}\sin(2x) \neq \cos(2x)$ — it's $\cos(2x) \cdot 2 = 2\cos(2x)$. The inner function $2x$ contributes its derivative.
6. **Power rule on $a^x$.** $\frac{d}{dx}a^x \neq xa^{x-1}$ — that's the power rule, which applies when the *base* is the variable, not the exponent. For $a^x$ the rule is $a^x \ln a$.
7. **Mixing up $\ln$ and $\log_{10}$.** $\frac{d}{dx}\ln x = 1/x$, but $\frac{d}{dx}\log_{10} x = 1/(x\ln 10)$. The $\ln a$ factor only disappears when the base is $e$.

---

## Exam Notes

### Cambridge 0606

**Syllabus ref:** §14.3. The 0606 syllabus requires derivatives of polynomials (Power Rule), $\sin x$, $\cos x$, $\tan x$ in radians, $e^x$, $\ln x$. The reciprocal trig functions and inverse trig functions are *not* explicitly required for 0606 — but they appear in some questions through the back door (e.g., $\frac{d}{dx}\ln(\cos x) = -\tan x$, which a strong student should be comfortable with).

> [!tip] Formula-sheet status (placeholder — Queue M1)
> 0606 students typically get a small reference sheet listing the derivatives of $\sin, \cos, \tan, e^x, \ln x$. Reciprocal-trig and inverse-trig derivatives are A-Level / IB / AP only and may need to be memorised or re-derived. The full per-board breakdown varies by board. The safe play: **memorise the seven entries in the "Trigonometric" + "Exponential" + "Logarithmic" sections** of the reference table above. The inverse-trig three are nice-to-have for IB HL / AP BC.

### A-Level / 9709

**Syllabus refs:** 9709 **P1 §1.7** (basic differentiation, polynomials and trig), **P2 §2.4** (extends to log/exp/composite), **P3 §3.4** (full elementary function table including reciprocal trig). All derivatives in this card are A-Level Pure Maths content. *(Watch the numbering: differentiation is the seventh subsection of Paper 1 but the fourth of Papers 2 and 3 — §1.3 is coordinate geometry, and §2.3 / §3.3 are trigonometry.)*

### Cambridge 9231 Further Mathematics — **Further Pure 2, Paper 2**

The per-board tables above mark eight rows as 9231 territory, but the section was missing until 2026-08-12. **§2.3 Differentiation** wants:

- the derivatives of $\sin^{-1} x$, $\cos^{-1} x$, $\tan^{-1} x$ **and the inverse hyperbolic functions** — every one of them **printed on MF19**, so the examinable skill is applying them inside a chain or quotient rule, not recalling them;
- $\dfrac{d^2y}{dx^2}$ for relations given **implicitly or parametrically** — see [[Implicit Differentiation]] and [[Parametric Differentiation]], where the parametric second derivative's extra $\dfrac{dt}{dx}$ factor is the standard mark-loser;
- the **first few terms of a Maclaurin series** — [[Maclaurin Series]].

Note the split with 9709: Cambridge deliberately keeps $\sin^{-1}$ and $\cos^{-1}$ derivatives *out* of single maths (P3 §3.4 says so explicitly) and hands them to Further, which is why the row here reads ⚪ for 9709 and why [[Standard Integrals]] has no $\arcsin$ integral on 9709. The hyperbolic derivatives are one line from the $e^x$ definitions — [[Hyperbolic Functions]] derives them, including why $\dfrac{d}{dx}\cosh x$ carries **no minus sign**.

### IB AA / AP

IB AA HL and AP Calculus AB/BC require all entries in the table including the inverse-trig three. AP BC additionally tests partial fraction integration and trig substitution (which use the $\arctan$ and $\arcsin$ rows of the table read backwards).

---

## Connections

- **Prerequisite:** [[Differentiation]] — what a derivative *is* and the formal definition $\lim_{h \to 0}(f(x+h) - f(x))/h$
- **Prerequisite:** [[Power Rule]] — $\frac{d}{dx}x^n = nx^{n-1}$, the polynomial side
- **Prerequisite:** [[Product Rule]] — and quotient rule as its corollary, used in $\tan'$, $\cot'$, etc.
- **Prerequisite:** [[Chain Rule]] — used in $\cos'$, $a^{x'}$, and every "function-of-a-function" derivative
- **Prerequisite:** [[Trigonometric Identities]] — Pythagorean identity collapses the quotient-rule numerator to $1$; sum formula drives the $\sin'$ first-principles proof
- **Prerequisite:** [[Radians]] — the limit $\lim_{h \to 0}\sin h / h = 1$ is *the* fact that makes $\sin' = \cos$ in the first place; works only in radian measure
- **Prerequisite:** [[Exponential Function]] — supplies the $e^{x'} = e^x$ and $\ln' x = 1/x$ proofs used by reference here
- **Sibling:** [[Standard Integrals]] — every derivative in this table reads backwards into an integral; see for the integral side
- **Application:** [[Integration by Substitution]] — uses the chain-rule reversed; the entries here become the antiderivative table
- **Application:** [[Integration by Parts]] — picks $u$ and $dv$ from this table; the LIATE heuristic is about which entries collapse fastest under differentiation
- **Application:** physics — every elementary function in motion / wave / oscillation problems differentiates via this table; SHM uses $\sin'$ and $\cos'$ extensively
- **Application:** ML / data science — gradient descent on neural networks uses chain rule + this table; back-propagation is just the chain rule applied to a long composition
- **Beyond high school:** *partial derivatives* (multivariable calculus); the reference table extends to functions of several variables term-by-term

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{d}{dx}f(x)$ | `\dfrac{d}{dx}f(x)` | Leibniz notation for differentiation |
| $f'(x)$ | `f'(x)` | Lagrange notation for derivative |
| $\sin h / h$ | `\sin h / h` | the key limit's setup |
| $\sec x \tan x$ | `\sec x \tan x` | derivative of $\sec x$ |
| $\arcsin x$ | `\arcsin x` | inverse sine; preferred over $\sin^{-1}$ in proofs |
| $\arctan x$ | `\arctan x` | inverse tangent |
| $a^x \ln a$ | `a^x \ln a` | derivative of general exponential |
| $\boxed{\;}$ | `\boxed{}` | end-of-proof marker (or QED with $\square$) |
