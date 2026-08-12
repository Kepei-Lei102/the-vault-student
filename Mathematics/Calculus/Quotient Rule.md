---
chinese: 商法则 (shāng fǎzé)
prerequisites:
  - "[[Product Rule]]"
  - "[[Chain Rule]]"
  - "[[Power Rule]]"
  - "[[Differentiation]]"
leads_to:
  - "[[Differentiation Rules]]"
  - "[[Implicit Differentiation]]"
  - "[[Logarithmic Differentiation]]"
  - "[[Tangents and Normals]]"
  - "[[Parametric Differentiation]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/pre-IB
  - level/pre-AP
  - level/A-Level
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/AP
  - syllabus/0606-14-4
  - syllabus/9709-2-4
  - syllabus/9709-3-4
  - type/theorem
  - type/proof
  - type/corollary
  - notation/derivative
  - misconception/quotient-sign-flip
  - misconception/quotient-rule-when-product-is-cleaner
---

# Quotient Rule 商法则

## The Rule

If $u$ and $v$ are differentiable functions of $x$ with $v(x) \neq 0$, then

$$\boxed{\;\dfrac{d}{dx}\!\left(\dfrac{u}{v}\right) \;=\; \dfrac{v\,\dfrac{du}{dx} \;-\; u\,\dfrac{dv}{dx}}{v^2}\;}$$

In prime notation: $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$.

Two things to notice straight away:

1. The numerator has a **minus sign**, so the rule is *not* symmetric in $u$ and $v$ the way the [[Product Rule]] is. Order matters.
2. The denominator is **squared**. The original $v$ on the bottom comes back as $v^2$ — that $v^2$ is a fingerprint of where the rule comes from.

Both fingerprints — the minus sign and the squared denominator — drop out of *one* underlying fact: differentiating $1/v$ gives $-v'/v^2$. The whole Quotient Rule is the [[Product Rule]] applied to $u \cdot v^{-1}$, with the chain rule running on $v^{-1}$ to produce the $-1/v^2$. That's the principle. Memorise the rule for speed; understand the principle so the sign never goes wrong.

> [!warning] The sign trap (and how the principle catches it)
> Many students lose marks by writing $\dfrac{uv' - u'v}{v^2}$ — the numerator flipped. The mnemonic *"low d-high minus high d-low"* helps, but the more reliable check is the principle: the term $u' \cdot v^{-1} = u'v / v^2$ comes from differentiating *the numerator factor* $u$, so it has to come *first* in the difference. The chain-rule term on $v^{-1}$ produces $-uv'/v^2$, which has to be *subtracted*. **First $u$, then $v$, with the minus sign tied to the chain rule on the reciprocal.** Once you've seen the principle once, the sign is no longer a memory test.

## 中文锚点

**商法则**：两个函数相除的导数。

$$\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}, \qquad v \neq 0$$

读法：「**分子的导数 × 分母 减去 分子 × 分母的导数，全部除以分母的平方**」。

为什么是这个形状？因为 $\dfrac{u}{v} = u \cdot v^{-1}$。这是一个乘积，可以直接套乘法法则；只是第二个因子 $v^{-1}$ 在求导时要再用一次链式法则，得到 $-v'/v^2$。所以：

- 减号 —— 来自 $\dfrac{d}{dx}(v^{-1}) = -v^{-2} \cdot v' = -\dfrac{v'}{v^2}$；负指数求导自带的负号。
- $v^2$ —— 同一个原因；$v^{-1}$ 的导数把分母升到了平方。

**核心断言：商法则不是新公理，而是乘法法则 + 链式法则的推论。**

> 万一记不住：$u/v = u \cdot v^{-1}$，套乘法法则 + 链式法则即可。这条退路永远成立。

---

## Why It Works — Two Derivations

### Derivation 1 — From Product Rule + Chain Rule (the principle)

This is the derivation worth keeping in your head. Write the quotient as a product:

$$\dfrac{u}{v} = u \cdot v^{-1}$$

Apply the [[Product Rule]] $(fg)' = f'g + fg'$ with $f = u$, $g = v^{-1}$:

$$\left(\dfrac{u}{v}\right)' \;=\; u' \cdot v^{-1} \;+\; u \cdot (v^{-1})'$$

Now compute $(v^{-1})'$ using the [[Chain Rule]] (or equivalently the [[Power Rule]] applied to $v^{-1}$, treating $v$ as the inner function):

$$(v^{-1})' = -1 \cdot v^{-2} \cdot v' = -\dfrac{v'}{v^2}$$

Substitute back:

$$\left(\dfrac{u}{v}\right)' \;=\; \dfrac{u'}{v} \;-\; \dfrac{uv'}{v^2}$$

Put both terms over the common denominator $v^2$:

$$\left(\dfrac{u}{v}\right)' \;=\; \dfrac{u'v}{v^2} \;-\; \dfrac{uv'}{v^2} \;=\; \dfrac{u'v - uv'}{v^2}.\qquad\blacksquare$$

This is the whole story. Three lines of algebra, no tricks. The minus sign and the squared denominator are not arbitrary features of "the Quotient Rule" — they're the chain rule on $v^{-1}$ wearing a costume.

> [!tip] If you forget the rule in an exam
> Rewrite $u/v$ as $u \cdot v^{-1}$ and use Product Rule + Chain Rule. You will arrive at the right formula in three lines and the markers will give full credit. The Quotient Rule is a *shortcut*, not a separate machine.

### Derivation 2 — From first principles (the limit definition)

For a strong student who wants to see the rule emerge directly from $\dfrac{d}{dx}f(x) = \lim\limits_{h\to 0}\dfrac{f(x+h) - f(x)}{h}$.

**Step 1 — Write the difference quotient.**

$$\dfrac{d}{dx}\!\left[\dfrac{u(x)}{v(x)}\right] \;=\; \lim_{h\to 0}\;\dfrac{1}{h}\!\left[\dfrac{u(x+h)}{v(x+h)} \;-\; \dfrac{u(x)}{v(x)}\right]$$

**Step 2 — Common denominator.** Combine the two fractions inside the brackets:

$$\dfrac{u(x+h)}{v(x+h)} - \dfrac{u(x)}{v(x)} \;=\; \dfrac{u(x+h)v(x) - u(x)v(x+h)}{v(x+h)\,v(x)}$$

**Step 3 — The add-subtract trick.** The numerator is a difference of products; we want it to factor into "change in $u$ times $v$" plus "$u$ times change in $v$". Insert $u(x)v(x)$ — add and subtract:

$$u(x+h)v(x) - u(x)v(x+h) \;=\; \bigl[u(x+h) - u(x)\bigr]\,v(x) \;-\; u(x)\,\bigl[v(x+h) - v(x)\bigr]$$

(Check this by expanding — the inserted $u(x)v(x)$ cancels.)

**Step 4 — Divide by $h$ and take the limit.**

$$\dfrac{1}{h}\!\left[\dfrac{u(x+h)}{v(x+h)} - \dfrac{u(x)}{v(x)}\right] \;=\; \dfrac{1}{v(x+h)\,v(x)}\!\left[\dfrac{u(x+h) - u(x)}{h}\,v(x) \;-\; u(x)\,\dfrac{v(x+h) - v(x)}{h}\right]$$

As $h \to 0$:
- $\dfrac{u(x+h) - u(x)}{h} \to u'(x)$
- $\dfrac{v(x+h) - v(x)}{h} \to v'(x)$
- $v(x+h) \to v(x)$ (since $v$ is differentiable, hence continuous)

So the limit is

$$\dfrac{1}{v(x)\,v(x)}\,\bigl[u'(x)\,v(x) - u(x)\,v'(x)\bigr] \;=\; \dfrac{u'v - uv'}{v^2}.\qquad\blacksquare$$

The first-principles version is structurally identical to the [[Product Rule]] proof, just one add-subtract step different (and forced to divide by $v(x+h)v(x)$ to combine the fractions). Both derivations prove the same theorem — pick the one whose feel matches your memory.

> [!info] Beyond syllabus — a third proof, via logarithmic differentiation
> *Recall that $\ln(a/b) = \ln a - \ln b$* — the log of a quotient is a difference. Take logs of both sides of $y = u/v$:
>
> $$\ln y = \ln u - \ln v$$
>
> Differentiate both sides implicitly with respect to $x$:
>
> $$\dfrac{1}{y}\,\dfrac{dy}{dx} = \dfrac{u'}{u} - \dfrac{v'}{v} = \dfrac{u'v - uv'}{uv}$$
>
> Multiply both sides by $y = u/v$:
>
> $$\dfrac{dy}{dx} = \dfrac{u}{v} \cdot \dfrac{u'v - uv'}{uv} = \dfrac{u'v - uv'}{v^2}.$$
>
> Same result, in three lines, using nothing but $\ln(a/b) = \ln a - \ln b$ and the chain rule on $\ln$. The technique generalises beautifully — products of three or more factors, exponents that depend on $x$, anything where multiplication and division dominate. The card to read for the technique itself is [[Logarithmic Differentiation]].

---

## The Mnemonic — Principle First, Chant Second

The standard chant for the Quotient Rule is:

> ***Low d-high, minus high d-low, square the low and away we go.***

Decoded:
- *Low* = denominator $v$
- *High* = numerator $u$
- *d-high* = derivative of the high, i.e. $u'$
- *d-low* = derivative of the low, i.e. $v'$
- *Square the low* = denominator $v^2$

Putting it together: $\dfrac{v \cdot u' - u \cdot v'}{v^2} = \dfrac{u'v - uv'}{v^2}$. ✓

**The principle this chant pre-sorts:** the Quotient Rule is Product Rule + Chain Rule on $u v^{-1}$. The chant just remembers (a) which factor's derivative comes first (the *high*'s, because that's the Product-Rule term that did *not* go through the chain rule), (b) which sign attaches to which (minus, because the chain rule on $v^{-1}$ produced one), and (c) the $v^2$ in the denominator (the chain rule on $v^{-1}$ again).

> [!tip] When the chant feels ambiguous, fall back on the principle
> If you ever blank on whether it's "low d-high" or "high d-low", rewrite the quotient as $u \cdot v^{-1}$, apply Product Rule, and let the chain rule on $v^{-1}$ supply the sign. The principle takes ten extra seconds and is *never* wrong; the chant takes one second and occasionally is.

---

## Worked Examples

### Example 1 — A rational function

Differentiate $y = \dfrac{x^2 + 1}{x - 1}$.

Identify $u = x^2 + 1$ so $u' = 2x$, and $v = x - 1$ so $v' = 1$. Apply the rule:

$$\dfrac{dy}{dx} = \dfrac{(2x)(x - 1) - (x^2 + 1)(1)}{(x - 1)^2} = \dfrac{2x^2 - 2x - x^2 - 1}{(x - 1)^2} = \dfrac{x^2 - 2x - 1}{(x - 1)^2}.$$

The denominator is the squared $v$; the numerator is "low d-high minus high d-low", expanded.

### Example 2 — Deriving $(\tan x)' = \sec^2 x$

Write $\tan x = \dfrac{\sin x}{\cos x}$. So $u = \sin x$ and $v = \cos x$, giving $u' = \cos x$ and $v' = -\sin x$.

$$(\tan x)' = \dfrac{(\cos x)(\cos x) - (\sin x)(-\sin x)}{\cos^2 x} = \dfrac{\cos^2 x + \sin^2 x}{\cos^2 x} = \dfrac{1}{\cos^2 x} = \sec^2 x.\qquad\blacksquare$$

The Pythagorean identity $\sin^2 x + \cos^2 x = 1$ collapses the numerator beautifully. This derivation is a 9709 P3 / IB AA HL / AP Calc favourite — being able to derive $(\tan x)'$ in two lines from the Quotient Rule (rather than memorising it as a separate formula) is the kind of fluency examiners reward.

### Example 3 — Deriving $(\sec x)' = \sec x \tan x$

Write $\sec x = \dfrac{1}{\cos x}$. So $u = 1$ (constant, $u' = 0$) and $v = \cos x$ ($v' = -\sin x$).

$$(\sec x)' = \dfrac{(0)(\cos x) - (1)(-\sin x)}{\cos^2 x} = \dfrac{\sin x}{\cos^2 x} = \dfrac{1}{\cos x}\cdot\dfrac{\sin x}{\cos x} = \sec x \tan x.\qquad\blacksquare$$

The $u' = 0$ kills the first term, leaving the chain-rule term to do all the work — and it turns into the elegant $\sec x \tan x$ via one factorisation.

> [!info] When *not* to use the Quotient Rule
> Example 3 is a case where the Quotient Rule works but the [[Chain Rule]] alone (writing $\sec x = (\cos x)^{-1}$ and applying Power Rule + Chain Rule) is cleaner and faster. **Rule of thumb: if the numerator is a constant, use Chain Rule; if the denominator is a constant, just multiply by $1/v$ and skip the rule entirely.** The Quotient Rule earns its keep when *both* $u$ and $v$ are non-trivial functions of $x$.

### Example 4 — A 9709 P3-style problem

Differentiate $y = \dfrac{e^{2x}}{x^2 + 1}$.

So $u = e^{2x}$, $u' = 2e^{2x}$ (chain rule on the exponent), $v = x^2 + 1$, $v' = 2x$.

$$\dfrac{dy}{dx} = \dfrac{(2e^{2x})(x^2 + 1) - (e^{2x})(2x)}{(x^2 + 1)^2} = \dfrac{2e^{2x}(x^2 + 1) - 2x\,e^{2x}}{(x^2 + 1)^2} = \dfrac{2e^{2x}(x^2 - x + 1)}{(x^2 + 1)^2}.$$

The factor $2e^{2x}$ is common to both numerator terms and was extracted in the last step. P3 examiners often mark factorisation explicitly — leaving an unfactorised numerator can cost a method mark even if the algebra is otherwise correct.

---

## Common Pitfalls

### 1. Sign flipped — $uv' - u'v$ instead of $u'v - uv'$

The single most common error. Mitigation: rewrite as $u v^{-1}$ once a term and watch the chain-rule sign appear; or chant *low d-high minus high d-low* and remember that *low* (the denominator) gets paired with the *first* derivative-of-the-other term — same order as Product Rule's first term, just adapted.

### 2. Forgetting to square the denominator

You differentiate the numerator carefully, get the sign right, then write $v$ (not $v^2$) in the denominator. Mitigation: the denominator's *job* in the rule is to remember "this came from $1/v^2$, the chain-rule fingerprint." If your answer has $v$ on the bottom, you've lost the chain rule somewhere.

### 3. Using the Quotient Rule when the Product Rule is cleaner

If $v$ is a polynomial of low degree (or a single power of $x$), often $u/v = u \cdot v^{-1}$ is faster as a Product Rule application. Example: $\dfrac{e^x}{x}$ as $e^x \cdot x^{-1}$ gives $e^x \cdot x^{-1} + e^x \cdot (-x^{-2}) = \dfrac{e^x(x - 1)}{x^2}$ in two lines. Same answer, less algebra, one less place to drop a sign.

### 4. Forgetting to apply the chain rule *inside* $u'$ or $v'$

If $u$ or $v$ is itself a composition (e.g. $u = \sin(2x)$, $u' = 2\cos(2x)$), the chain rule applies *inside* the Quotient Rule's $u'$ slot. Forgetting this is a layer-confusion error: students apply the Quotient Rule but skip the chain rule on the inner functions. Sketch the structure first: identify $u$, $v$, and any nested compositions, then differentiate piece-by-piece.

---

## Exam Notes

### Cambridge 0606 (Additional Mathematics)

The Quotient Rule is on the formula list. Examined directly in §14.4 (differentiation of products and quotients), and used implicitly in stationary-point and tangent-and-normal questions throughout Paper 2. Sign mistakes are penalised at the algebra stage even when the method is right — write $u'v - uv'$ slowly.

### Cambridge 9709 — A-Level Mathematics

**Paper 3 (§3.4)** examines the Quotient Rule on rational functions, trig quotients, and combinations involving $e^x$ and $\ln x$. The Quotient Rule formula is **given on the MF19 reference sheet** (under Differentiation), so memorisation is for speed only — the formula is in the room with you.

**Paper 1** (§1.7) covers the Chain and Product Rules; Quotient Rule typically appears at Paper 2 / Paper 3 level.

### A-Level (Edexcel / AQA / OCR)

Quotient Rule is on the standard A-Level formula booklets. Examined in pure-mathematics differentiation questions and in mechanics where $v(t)$ or $a(t)$ is a quotient.

### IB AA SL / HL

SL: Topic 5 (calculus). HL: Topic 5 with the additional implicit-differentiation and logarithmic-differentiation extensions. Quotient Rule is on the IB AA formula booklet. HL students should be comfortable deriving it from Product + Chain.

### AP Calculus AB / BC

Quotient Rule appears in Unit 2 (Differentiation: Definitions and Fundamental Properties). It is on the AP Calculus reference sheet. AP graders care about clean notation — $\dfrac{u'v - uv'}{v^2}$ written precisely, no missing parentheses, no skipped factorisations.

### Beyond high school — University

The Quotient Rule extends naturally to:
- **Multivariable calculus** — partial derivatives of $f/g$ where $f$ and $g$ are functions of several variables follow exactly the same shape (with $\partial / \partial x_i$ in place of $d/dx$).
- **Complex analysis** — for holomorphic $f, g$ on an open set with $g \neq 0$, $(f/g)' = (f'g - fg')/g^2$ is identical.
- **Operator calculus / Lie algebras** — the "derivation" property $D(fg) = (Df)g + f(Dg)$ is the *definition* of a derivation, and the quotient rule is its straightforward consequence whenever multiplicative inverses make sense.

---

## Connections

- **Parent rules:** [[Product Rule]] (the rule we derived from), [[Chain Rule]] (supplies the $-1/v^2$ on the reciprocal), [[Power Rule]] (covers $v^{-1}$ as a power).
- **Sibling differentiation rules:** [[Differentiation Rules]] (the master table of standard derivatives — pair the table with the Quotient Rule for full-strength rational-function differentiation).
- **Direct extensions:** [[Logarithmic Differentiation]] (the "third proof" technique — $\ln(u/v) = \ln u - \ln v$ converts every quotient into a sum, sidestepping the rule entirely for messy products-and-quotients), [[Implicit Differentiation]] (uses the Quotient Rule whenever the implicit equation involves $y/f(x)$).
- **Direct applications:** [[Tangents and Normals]] (rational-function tangents), [[Stationary Points]] (set $\dfrac{u'v - uv'}{v^2} = 0$, so the *numerator* is zero — the denominator never makes a stationary point), [[Optimisation]] (rate-of-change problems with quotient structure), [[Connected Rates of Change]] (related rates with a quotient).
- **Reverse:** [[Integration]] — there is no "quotient rule" for integration; quotients of polynomials integrate via [[Partial Fractions]], and other quotients via substitution or by-parts. Differentiation has more closed-form rules than integration; that asymmetry first becomes visible here.
- **Where this gets used:** every $\dfrac{dy}{dx}$ exam question involving $\tan x$, $\sec x$, $\csc x$, $\cot x$ uses the Quotient Rule under the hood (or — once the standard derivatives are memorised — uses the Chain Rule on the implicit reciprocal). [[Differentiation Rules]] tabulates the resulting standard derivatives.
- **For 9709 students:** [[MF19 Reference (9709)]] — Quotient Rule formula is given on the sheet (Differentiation table). The Chain and Product rules are also given. Memorisation effort goes to *applying* the rules quickly under exam pressure; the formulas themselves are in the room.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\left(\dfrac{u}{v}\right)'$ | `\left(\dfrac{u}{v}\right)'` | The thing being differentiated; outer parentheses size to the fraction. |
| $u'v - uv'$ | `u'v - uv'` | Numerator. Order matters: $u'v$ first, $uv'$ second, **minus** in between. |
| $v^2$ | `v^2` | Denominator squared — fingerprint of the chain rule on $v^{-1}$. |
| $v^{-1}$ | `v^{-1}` | The reciprocal form used in Derivation 1; key to the Product+Chain proof. |
| $(\tan x)' = \sec^2 x$ | `(\tan x)' = \sec^2 x` | Worked Example 2 — derived in two lines from the Quotient Rule. |
| $(\sec x)' = \sec x \tan x$ | `(\sec x)' = \sec x \tan x` | Worked Example 3 — Quotient Rule with $u = 1$. |
| $\ln(a/b) = \ln a - \ln b$ | `\ln(a/b) = \ln a - \ln b` | The log-quotient identity behind the third (logarithmic-differentiation) proof. |
