---
chinese: 洛必达法则 (luò bì dá fǎzé)
prerequisites:
  - "[[Mean Value Theorem]]"
  - "[[Differentiation]]"
  - "[[Limit]]"
  - "[[Differentiation Rules]]"
leads_to:
  - "[[Squeeze Theorem]]"
  - "[[Taylor Series]]"
  - "[[Stories/The Bernoulli Family]]"
  - "[[Maclaurin Series]]"
  - "[[The Bernoulli Family]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/IB-HL
  - level/AP-BC
  - level/university
  - curriculum/IB-AA
  - curriculum/AP
  - curriculum/A-Level-Further
  - type/theorem
  - type/proof
  - type/technique
  - notation/limit
  - notation/derivative
  - misconception/lhopital-circular-on-sinh-over-h
  - misconception/lhopital-when-not-indeterminate
  - misconception/lhopital-converse-failure
---

# L'Hôpital's Rule 洛必达法则

> *L'Hôpital's Rule converts a stuck limit into a stretchier limit by replacing it with the ratio of derivatives.*
>
> *It is fast, powerful, and dangerous: it depends on derivatives existing, so you cannot use it to prove the limits that derivatives are defined by.*

## What this card is for

When you meet $\lim\limits_{x\to a} \dfrac{f(x)}{g(x)}$ and substituting $x = a$ gives the meaningless $\dfrac{0}{0}$ or $\dfrac{\infty}{\infty}$, the *standard* tactics from earlier calculus stop working. **L'Hôpital's Rule** replaces the limit of the ratio with the limit of the ratio of derivatives — and most of the time, the new limit is the one you can actually evaluate.

The rule is a workhorse for IB AA HL, AP Calculus BC, A-Level Further, and university analysis. It is not on the standard 9709 syllabus, but knowing it is a useful sanity check (and a fast verification tool when the answer is otherwise opaque). The deepest payoff isn't the speed — it's the *honest* understanding of what the rule depends on, which is also what makes the **circular-application trap on $\sin h / h$** so instructive. We'll meet that trap as the pedagogical jewel of this card.

## The Rule

**L'Hôpital's Rule.** Suppose $f$ and $g$ are differentiable on an open interval containing $a$ (except possibly at $a$ itself), $g'(x) \neq 0$ near $a$, and either

$$\lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0 \qquad \text{(the } \tfrac{0}{0} \text{ case)}$$

or

$$\lim_{x \to a} \lvert f(x) \rvert = \lim_{x \to a} \lvert g(x) \rvert = \infty \qquad \text{(the } \tfrac{\infty}{\infty} \text{ case)}.$$

If $\displaystyle\lim_{x \to a} \dfrac{f'(x)}{g'(x)}$ exists (or equals $\pm\infty$), then

$$\boxed{\;\lim_{x \to a} \dfrac{f(x)}{g(x)} \;=\; \lim_{x \to a} \dfrac{f'(x)}{g'(x)}.\;}$$

The rule also holds for one-sided limits and for $a = \pm\infty$ (with appropriate adjustments — see below).

> [!warning] Three things students get wrong about the statement
> 1. **The original limit must be indeterminate.** L'Hôpital is for $\tfrac{0}{0}$ and $\tfrac{\infty}{\infty}$ *only*. If $\lim_{x\to 1} \dfrac{x+1}{x+2} = \tfrac{2}{3}$ by direct substitution, applying L'Hôpital gives $\tfrac{1}{1} = 1$, which is *wrong*. Always check that the form is genuinely indeterminate before applying the rule.
> 2. **It's the ratio of derivatives, not the derivative of the ratio.** $\dfrac{f'(x)}{g'(x)}$, not $\left(\dfrac{f}{g}\right)'$. The Quotient Rule is a different machine.
> 3. **The converse is false.** If $\lim f/g$ exists, that does *not* mean $\lim f'/g'$ exists. (Example: $f(x) = x + \sin x$, $g(x) = x$ as $x \to \infty$; the ratio $\to 1$ but the derivative-ratio $1 + \cos x$ has no limit.) The rule is one-way: derivative-ratio limit existing $\Rightarrow$ original-ratio limit equals it.

## 中文锚点

**洛必达法则**：如果 $\lim_{x \to a}\dfrac{f(x)}{g(x)}$ 是 $\dfrac{0}{0}$ 或 $\dfrac{\infty}{\infty}$ 的不定式，并且 $f'/g'$ 的极限存在，那么

$$\lim_{x \to a}\dfrac{f(x)}{g(x)} = \lim_{x \to a}\dfrac{f'(x)}{g'(x)}.$$

它是用 *导数比* 替换 *函数比*。条件很关键：**原极限必须真的是不定式**，不然不能套；并且替换后的极限要存在（或为 $\pm\infty$），否则也不能下结论。

七种不定式：

- $\dfrac{0}{0}$, $\dfrac{\infty}{\infty}$ —— 直接套用。
- $0 \cdot \infty$ —— 改写成 $\dfrac{f}{1/g}$ 或 $\dfrac{g}{1/f}$。
- $\infty - \infty$ —— 通分成单一分式。
- $1^\infty$, $0^0$, $\infty^0$ —— 取对数 $y = f^g \Rightarrow \ln y = g \ln f$，把指数形式变成乘积，再处理 $0 \cdot \infty$。

**核心警告**：**不能用洛必达去证明 $\lim_{h \to 0}\dfrac{\sin h}{h} = 1$。** 因为 $(\sin h)' = \cos h$ 的证明本身就需要这个极限 —— 这是循环论证。这条限制是这张卡片最重要的一课。

---

## Why It Works — Proof via Cauchy's MVT

L'Hôpital's Rule is *not* an axiom; it follows from **Cauchy's Mean Value Theorem** (proved in [[Mean Value Theorem]]).

> **Cauchy's MVT.** If $f$ and $g$ are continuous on $[a, b]$ and differentiable on $(a, b)$, with $g'(x) \neq 0$ on $(a, b)$, then there exists $c \in (a, b)$ such that
> $$\dfrac{f'(c)}{g'(c)} = \dfrac{f(b) - f(a)}{g(b) - g(a)}.$$

### Proof of L'Hôpital (the $0/0$ case at finite $a$)

Suppose $\lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0$, both functions are differentiable near $a$, and $g'(x) \neq 0$ near $a$. **Define $f(a) = g(a) = 0$** (extending continuously — there's no conflict with the original limit). Then $f$ and $g$ are continuous at $a$.

For $x$ close to $a$ (say $x > a$, the other side is symmetric), by Cauchy's MVT applied to the interval $[a, x]$, there exists $c \in (a, x)$ with

$$\dfrac{f(x)}{g(x)} \;=\; \dfrac{f(x) - f(a)}{g(x) - g(a)} \;=\; \dfrac{f'(c)}{g'(c)}.$$

(The first equality is because $f(a) = g(a) = 0$. The second is Cauchy's MVT.)

As $x \to a$, the intermediate point $c \in (a, x)$ is squeezed: $a < c < x$, so $c \to a$ as well. Therefore

$$\lim_{x \to a} \dfrac{f(x)}{g(x)} \;=\; \lim_{c \to a} \dfrac{f'(c)}{g'(c)} \;=\; \lim_{x \to a} \dfrac{f'(x)}{g'(x)}.\qquad\blacksquare$$

That's the heart of it. The other cases ($x \to \infty$, the $\infty/\infty$ case) require slightly more delicate arguments — the $\infty/\infty$ proof uses an $\varepsilon$–$\delta$ trick that's standard in real analysis but skipped here. The $\tfrac{0}{0}$ case at finite $a$ is the cleanest version, and it shows exactly why Cauchy's MVT is the right machinery: the theorem talks about a ratio of derivatives in terms of a ratio of function-differences, and L'Hôpital is the limiting form of that statement.

> [!info] Why not just use Lagrange's MVT?
> Lagrange's MVT gives $f(x) - f(a) = f'(c)(x - a)$ for some $c$. So $\dfrac{f(x) - f(a)}{x - a} = f'(c)$, and similarly $\dfrac{g(x) - g(a)}{x - a} = g'(c')$ — but the $c$ for $f$ and the $c'$ for $g$ are *different* in general. Cauchy's MVT is the upgrade that gives you a *single* $c$ for both functions simultaneously, and that's exactly what's needed for the ratio $f'(c)/g'(c)$ to make sense as a single object. The genius of Cauchy's MVT is producing the same $c$ for both, and L'Hôpital is what that genius pays for.

---

## The Seven Indeterminate Forms

Direct substitution into a limit can yield any of seven *indeterminate* forms — expressions that don't have a single fixed value but depend on the specific functions involved. L'Hôpital handles two of them directly; the other five convert into one of those two.

| Form | Example | Conversion to $\tfrac{0}{0}$ or $\tfrac{\infty}{\infty}$ |
|---|---|---|
| $\dfrac{0}{0}$ | $\lim_{x\to 0} \dfrac{\sin x}{x}$ ⚠ (circular — see below) | Direct. |
| $\dfrac{\infty}{\infty}$ | $\lim_{x\to\infty} \dfrac{\ln x}{x}$ | Direct. |
| $0 \cdot \infty$ | $\lim_{x\to 0^+} x \ln x$ | Rewrite $f \cdot g$ as $\dfrac{f}{1/g}$ or $\dfrac{g}{1/f}$. |
| $\infty - \infty$ | $\lim_{x\to 0^+}\left(\dfrac{1}{x} - \dfrac{1}{\sin x}\right)$ | Combine into a single fraction. |
| $1^\infty$ | $\lim_{x\to\infty}\left(1 + \dfrac{1}{x}\right)^x$ | Take $\ln$: $\lim x \ln(1 + 1/x)$ → $0\cdot\infty$. Final answer = $\exp(\text{this limit})$. |
| $0^0$ | $\lim_{x\to 0^+} x^x$ | Take $\ln$: $\lim x \ln x$ → $0\cdot\infty$. |
| $\infty^0$ | $\lim_{x\to\infty} x^{1/x}$ | Take $\ln$: $\lim \dfrac{\ln x}{x}$ → $\tfrac{\infty}{\infty}$. |

The pattern across the last three (the *exponential* indeterminate forms) is the same: take logs to convert exponent-times-base into product-of-functions, evaluate the resulting product limit (often by another conversion to a fraction), then exponentiate the answer at the end.

> [!tip] When the limit is *not* indeterminate
> Forms like $\dfrac{1}{0}$, $\dfrac{0}{\infty}$, $0 + \infty$, $0^\infty$, $\infty^\infty$ are *determinate* — they have unambiguous values ($\pm\infty$, $0$, $\infty$, $0$, $\infty$ respectively). L'Hôpital is forbidden here. If your form is determinate, just read off the value.

---

## The Circular-Application Trap — The Pedagogical Jewel

This is the most important callout in the card. **L'Hôpital cannot be used to prove $\displaystyle\lim_{h\to 0} \dfrac{\sin h}{h} = 1$.**

### The "proof" that doesn't work

A confident student reaches for L'Hôpital:

1. The limit is $\tfrac{0}{0}$ ✓
2. Differentiate top and bottom: $\dfrac{(\sin h)'}{h'} = \dfrac{\cos h}{1}$
3. Take the limit: $\lim_{h \to 0} \dfrac{\cos h}{1} = \cos 0 = 1$ ✓

The answer is correct. The reasoning is fatally circular.

### Why it's circular

To use step 2, the student needed to know $(\sin h)' = \cos h$. Where does that come from? From the limit definition of the derivative:

$$(\sin h)' = \lim_{k \to 0} \dfrac{\sin(h + k) - \sin h}{k}$$

Expanding via the angle-sum formula $\sin(h + k) = \sin h \cos k + \cos h \sin k$:

$$= \lim_{k \to 0} \dfrac{\sin h \cos k + \cos h \sin k - \sin h}{k} = \sin h \cdot \lim_{k\to 0} \dfrac{\cos k - 1}{k} + \cos h \cdot \lim_{k \to 0} \dfrac{\sin k}{k}.$$

The result $(\sin h)' = \cos h$ requires:
- $\lim_{k \to 0} \dfrac{\sin k}{k} = 1$ (the very limit we were trying to prove!)
- $\lim_{k \to 0} \dfrac{\cos k - 1}{k} = 0$ (which itself follows from the first).

So step 2 of the "proof" *assumed* the conclusion of step 3. The argument is logically equivalent to *"I know $\lim \sin h / h = 1$ because I know $(\sin h)' = \cos h$, which I know because $\lim \sin h / h = 1$."* Round and round.

### The honest proof (forward link)

The honest way to establish $\lim_{h \to 0} \sin h / h = 1$ is via the **[[Squeeze Theorem]]** applied to a unit-circle geometric inequality:

$$\sin h \;\leq\; h \;\leq\; \tan h \qquad \text{for } 0 < h < \tfrac{\pi}{2}.$$

(This comes from comparing the area of a triangle, an arc-sector, and a larger triangle in the unit circle.) Dividing through by $\sin h$ and taking reciprocals gives $\cos h \leq \dfrac{\sin h}{h} \leq 1$, and $\cos h \to 1$ as $h \to 0$, so by Squeeze Theorem $\dfrac{\sin h}{h} \to 1$. **No derivatives are used in this proof — that is the whole point.** The geometry is the foundation; the calculus is built on top of it.

Once $\lim \sin h / h = 1$ is in hand (geometrically, by Squeeze), $(\sin h)' = \cos h$ is unlocked, and L'Hôpital is unlocked, and you can apply the rule to *other* trig $\tfrac{0}{0}$ limits like $\lim_{x\to 0}\dfrac{\tan x}{x}$ or $\lim_{x \to 0}\dfrac{1 - \cos x}{x^2}$ — none of those are circular, because they're not the foundation under L'Hôpital itself.

> [!info] The general principle
> **L'Hôpital depends on derivatives existing. So you cannot use L'Hôpital to prove a limit that's needed to define a derivative.** The set of limits that L'Hôpital is allowed to evaluate is *all* indeterminate-form limits *except those that appear in the derivation of the differentiation rules themselves*. This is a foundational/recursive constraint — the same shape as why a self-hosting compiler can't bootstrap from nothing (cf. [[Inertia and Bootstrapping]]'s aside on self-hosting compilers as a cold-start problem). You need a *prior* tool — geometry, Squeeze, or Taylor series — to start the engine. Once it's running, L'Hôpital is fast and powerful.

> [!tip] Two safe and unsafe limits, side by side
> | Limit | L'Hôpital safe? | Why |
> |---|---|---|
> | $\lim_{h\to 0} \dfrac{\sin h}{h}$ | ❌ Circular | Used to *define* $(\sin h)'$. |
> | $\lim_{h\to 0} \dfrac{1 - \cos h}{h^2}$ | ⚠ Circular if you'd haven't proved $\sin'$ yet | Same family — uses $(\cos h)' = -\sin h$, which depends on $\sin'$. |
> | $\lim_{x\to 0} \dfrac{e^x - 1}{x}$ | ⚠ Circular if your definition of $e$ is "the number with $(e^x)' = e^x$" | The "answer = 1" is exactly $(e^x)'$ at $x = 0$. Safe if you defined $e$ via $\lim (1 + 1/n)^n$ or via series. |
> | $\lim_{x\to 0} \dfrac{\tan x}{x}$ | ✅ Safe | Once $\sin'$ and $\cos'$ are known (from Squeeze), Quotient Rule gives $\tan' = \sec^2$ — and $\tan x / x$ is downstream. |
> | $\lim_{x\to 0} \dfrac{x - \sin x}{x^3}$ | ✅ Safe | Three applications of L'Hôpital give $\tfrac{1}{6}$, all using already-established derivatives. |
>
> The cardinal question every time: *did the derivatives I'm about to use depend on the limit I'm trying to evaluate?* If yes, find a non-derivative tool (Squeeze, geometry, series). If no, L'Hôpital away.

---

## Worked Examples

### Example 1 — Standard $\tfrac{0}{0}$: $\lim_{x\to 0}\dfrac{e^x - 1}{x}$

Direct substitution: $\dfrac{0}{0}$. Apply L'Hôpital:

$$\lim_{x\to 0} \dfrac{e^x - 1}{x} = \lim_{x\to 0} \dfrac{e^x}{1} = e^0 = 1.$$

(Safe assuming $(e^x)' = e^x$ was established from the series definition or from the limit definition $e = \lim_n(1 + 1/n)^n$, not by circular self-reference.)

### Example 2 — Standard $\tfrac{\infty}{\infty}$: $\lim_{x \to \infty}\dfrac{\ln x}{x}$

Direct: $\dfrac{\infty}{\infty}$.

$$\lim_{x\to\infty} \dfrac{\ln x}{x} = \lim_{x\to\infty} \dfrac{1/x}{1} = \lim_{x\to\infty} \dfrac{1}{x} = 0.$$

This is a load-bearing fact: **logarithms grow slower than any positive power of $x$.** A small generalisation: $\lim_{x\to\infty} \dfrac{\ln x}{x^p} = 0$ for any $p > 0$, via the same one-step L'Hôpital.

### Example 3 — Iterated L'Hôpital: $\lim_{x\to\infty}\dfrac{x^n}{e^x}$

For any positive integer $n$. Direct: $\dfrac{\infty}{\infty}$. Apply L'Hôpital $n$ times:

$$\lim_{x\to\infty}\dfrac{x^n}{e^x} = \lim_{x\to\infty}\dfrac{n x^{n-1}}{e^x} = \lim_{x\to\infty}\dfrac{n(n-1)x^{n-2}}{e^x} = \cdots = \lim_{x\to\infty}\dfrac{n!}{e^x} = 0.$$

The numerator gets stripped one power at a time; the denominator never gives an inch. **Exponentials beat polynomials.**

### Example 4 — $0 \cdot \infty$: $\lim_{x\to 0^+} x \ln x$

Direct: $0 \cdot (-\infty)$, indeterminate. Convert to a fraction by writing the log over the reciprocal of $x$:

$$\lim_{x\to 0^+} x \ln x = \lim_{x\to 0^+} \dfrac{\ln x}{1/x} = \dfrac{-\infty}{+\infty}.$$

Apply L'Hôpital:

$$= \lim_{x\to 0^+} \dfrac{1/x}{-1/x^2} = \lim_{x\to 0^+} (-x) = 0.$$

So $x \ln x \to 0$ as $x \to 0^+$. (Even though $\ln x \to -\infty$, the $x$ shrinks faster.)

### Example 5 — $1^\infty$: $\lim_{x\to\infty}(1 + 1/x)^x$

The famous limit. Direct: $1^\infty$. Take logs:

$$y = \left(1 + \dfrac{1}{x}\right)^x \;\Longrightarrow\; \ln y = x \ln\!\left(1 + \dfrac{1}{x}\right).$$

This is $\infty \cdot 0$. Convert to a fraction:

$$\ln y = \dfrac{\ln(1 + 1/x)}{1/x} \;\to\; \dfrac{0}{0}.$$

L'Hôpital. Differentiate top: $\dfrac{d}{dx}\ln(1 + 1/x) = \dfrac{1}{1 + 1/x} \cdot (-1/x^2) = \dfrac{-1/x^2}{1 + 1/x}$. Differentiate bottom: $\dfrac{d}{dx}(1/x) = -1/x^2$. Ratio:

$$\dfrac{-1/x^2}{(1 + 1/x)(-1/x^2)} = \dfrac{1}{1 + 1/x} \;\to\; 1 \quad \text{as } x \to \infty.$$

So $\ln y \to 1$, hence $y \to e^1 = e$:

$$\boxed{\;\lim_{x\to\infty}\left(1 + \dfrac{1}{x}\right)^x = e.\;}$$

A two-line L'Hôpital proof of one of the standard definitions of [[Euler's Number]]. Beautiful.

### Example 6 — $0^0$: $\lim_{x\to 0^+} x^x$

Direct: $0^0$. Take logs: $\ln y = x \ln x$, which from Example 4 is $\to 0$. So $y \to e^0 = 1$:

$$\lim_{x\to 0^+} x^x = 1.$$

Counter-intuitive but real. The "$0^0$" form is genuinely indeterminate — different functions of the form $f(x)^{g(x)}$ with $f, g \to 0$ give different limits. This one happens to be 1.

### Example 7 — $\infty - \infty$: $\lim_{x\to 0^+}\!\left(\dfrac{1}{x} - \dfrac{1}{\sin x}\right)$

Direct: $\infty - \infty$. Combine into one fraction:

$$\dfrac{1}{x} - \dfrac{1}{\sin x} = \dfrac{\sin x - x}{x \sin x}.$$

Now $\dfrac{0}{0}$. L'Hôpital once:

$$\to \lim_{x\to 0^+} \dfrac{\cos x - 1}{\sin x + x \cos x}.$$

Still $\dfrac{0}{0}$. L'Hôpital again:

$$\to \lim_{x\to 0^+} \dfrac{-\sin x}{\cos x + \cos x - x\sin x} = \dfrac{0}{2} = 0.$$

So the limit is $0$. Two iterations and an algebraic combine; the trick is keeping the indeterminate-form check at every step.

---

## Common Errors

### 1. Applying L'Hôpital when the limit isn't indeterminate

The single most common error. $\lim_{x\to 1}\dfrac{x^2 + 1}{x + 1} = \dfrac{2}{2} = 1$ by direct substitution. A student who reaches for L'Hôpital would compute $\dfrac{2x}{1} \to 2$ and submit the wrong answer.

**Mitigation.** Always check the form before applying. If direct substitution gives a real number, you have a number — done.

### 2. Not re-checking the indeterminate form at each iteration

After one application, the new limit might *not* still be indeterminate. Don't apply L'Hôpital a second time without checking — you'll typically get the wrong answer if you do.

### 3. Confusing ratio of derivatives with derivative of ratio

Quotient Rule produces $\dfrac{u'v - uv'}{v^2}$; L'Hôpital uses $\dfrac{u'}{v'}$. These are different operations on different limits, easily confused under exam pressure.

### 4. The converse trap

If $\lim f'/g'$ does not exist, you cannot conclude $\lim f/g$ doesn't exist. The textbook example is $f(x) = x + \sin x$, $g(x) = x$, with $x \to \infty$: the ratio $f/g \to 1$, but $f'/g' = 1 + \cos x$ has no limit. **L'Hôpital is one-way; the converse fails.**

### 5. The circular trap (already discussed)

Don't use L'Hôpital on $\sin h/h$, $(1 - \cos h)/h^2$, or any limit that was needed to define a derivative you're now using. Find a non-derivative tool — Squeeze, geometry, or Taylor series.

---

## Beyond Syllabus

### Bernoulli, not L'Hôpital

The rule was discovered by **Johann Bernoulli** around 1694 and communicated to the Marquis de **L'Hôpital** as part of a paid arrangement: L'Hôpital had hired Bernoulli to teach him calculus, and one clause of their contract gave L'Hôpital exclusive rights to publish Bernoulli's results. So when L'Hôpital published *Analyse des Infiniment Petits* (1696, the first calculus textbook), the rule appeared under L'Hôpital's name. Bernoulli protested for the rest of his life.

The naming injustice was finally documented by historians in the 1920s when Bernoulli's correspondence was rediscovered. Most modern textbooks now include a footnote acknowledging Bernoulli, but the name **L'Hôpital's Rule** has stuck. (The French *L'Hôpital* is sometimes written *L'Hospital* — both spellings are correct for the same person; the silent *s* fell out of French between his lifetime and ours.)

> [!info] Full Bernoulli–L'Hôpital story
> See [[Stories/The Bernoulli Family]] §"The L'Hôpital paid contract (1694)" for the full Renaissance soap opera — including the surviving 17 March 1694 letter where L'Hôpital offers Johann a 300-livre pension *"asking you not to mention any of them to others"*. The rule is the founding example of **Stigler's Law of Eponymy**: no scientific discovery is named after its original discoverer.

### The Taylor-series view

There's a faster way to see why L'Hôpital works for $\tfrac{0}{0}$: write Taylor series. If $f(a) = g(a) = 0$ and we expand around $a$:

$$f(x) = f'(a)(x - a) + \tfrac{1}{2}f''(a)(x - a)^2 + \cdots$$
$$g(x) = g'(a)(x - a) + \tfrac{1}{2}g''(a)(x - a)^2 + \cdots$$

Then $\dfrac{f(x)}{g(x)} = \dfrac{f'(a)(x-a) + O((x-a)^2)}{g'(a)(x-a) + O((x-a)^2)} = \dfrac{f'(a) + O(x - a)}{g'(a) + O(x - a)} \to \dfrac{f'(a)}{g'(a)}$ as $x \to a$.

The $(x - a)$ factor in numerator and denominator cancels — that's the *whole reason* the limit becomes $f'(a)/g'(a)$. Taylor series makes this transparent. (See [[Taylor Series]] for the full machinery; it's the upgrade path from L'Hôpital to a tool that handles iterated indeterminate forms in one step.)

> [!info] When Taylor beats L'Hôpital
> For higher-order $\tfrac{0}{0}$ limits, applying L'Hôpital iteratively is correct but slow. Example: $\lim_{x\to 0}\dfrac{x - \sin x}{x^3}$. L'Hôpital takes three iterations:
> $$\to \dfrac{1 - \cos x}{3x^2} \to \dfrac{\sin x}{6x} \to \dfrac{\cos x}{6} = \dfrac{1}{6}.$$
> Taylor does it in one line: $\sin x = x - x^3/6 + O(x^5)$, so $x - \sin x = x^3/6 + O(x^5)$, and the ratio → $1/6$. For limits past first order, *Taylor is faster*.

### Asymptotic comparison rates — the limit catalogue

L'Hôpital makes the *growth-rate ranking* of standard functions provable in one line each:

$$\boxed{\;1 \;\ll\; \ln x \;\ll\; x^p \;\ll\; e^x \;\ll\; x^x \quad (\text{as } x \to \infty)\;}$$

Where $f \ll g$ means $\lim_{x\to\infty} f/g = 0$. Each comparison is a single L'Hôpital (or, for the last one, a $\ln$-rewrite plus L'Hôpital). The whole hierarchy is one of the most useful facts in asymptotic analysis, real-analysis qualifying exams, and theoretical CS (algorithmic complexity classes are essentially this list, transposed).

---

## Exam Notes

### Cambridge 9709 (A-Level Mathematics)

**L'Hôpital's Rule is *not* on the 9709 syllabus.** P3 limits are handled by direct substitution, factoring (e.g. $\lim \dfrac{x^2 - 1}{x - 1} = \lim (x + 1) = 2$), or standard limits ($\lim \sin x/x = 1$ stated without proof). Knowing L'Hôpital is *not* a substitute for these techniques on 9709 — examiners want to see the syllabus method.

That said, knowing L'Hôpital is a useful **verification tool** when the textbook method gives an answer you doubt. Compute by both routes; if they agree, ship.

### Cambridge 0580 / 0606

**Not examined** — neither syllabus has limits at all; the nearest 0606 gets is the derivative's definition used informally.

### Cambridge 9231 · Edexcel IAL · OxAQA 9660

**L'Hôpital is not named on any of the three** (checked against the topic maps: no row exists on 9231, IAL FP1–FP3, or 9660). The Further-Maths route to indeterminate limits is **Maclaurin series** — a 9231 FP2 limit question expects the first few series terms substituted and the leading power read off, not a derivative quotient. L'Hôpital remains the private verification tool here exactly as at 9709: compute by the syllabus method, confirm by the rule, ship the syllabus method.

### IB AA HL

**On the syllabus** (Topic 5, Calculus). Stated and applied. The Cauchy-MVT proof is not formally required, but strong students are expected to recognise the dependence on it and the circular-application warning.

### IB AA SL / AI

Not on the syllabus. SL handles limits via direct substitution and standard rules.

### AP Calculus BC

**On the syllabus** (Unit 4 — Contextual Applications of Differentiation). Applied to the seven indeterminate forms. AP graders care about the *check-the-form* discipline — explicitly noting that direct substitution gives $0/0$ before applying the rule earns the method mark.

### AP Calculus AB

Not on the AB syllabus.

### Beyond high school — University

L'Hôpital is fundamental. First-year analysis courses prove it from Cauchy's MVT (as above), apply it to the asymptotic-comparison hierarchy, and discuss its limitations (the converse failure, the circular constraint). Real-analysis courses go further into the $\infty/\infty$ case and what happens when $g'$ has zeros.

---

## Connections

- **Direct prerequisite:** [[Mean Value Theorem]] — Cauchy's MVT is the engine. The L'Hôpital card is where the Cauchy-MVT preview in *that* card gets cashed in. (See its "Used by" line — pointing here.)
- **Honest-proof companion:** [[Squeeze Theorem]] — the *non-circular* tool for $\sin h / h \to 1$ and $(1 - \cos h)/h^2 \to 1/2$. Pair the two cards: L'Hôpital is fast and powerful *once derivatives are unlocked*; Squeeze is the geometric foundation that unlocks them. The pedagogical message of this card is that you need *both*, in the right order.
- **Preview from:** [[Differentiation Rules]] — its "Beyond syllabus — L'Hôpital is the obvious tool, and it's circular here" callout previewed the circular trap; this card is the full treatment.
- **Faster cousin:** [[Taylor Series]] — for higher-order indeterminate forms, Taylor beats iterated L'Hôpital. The two tools coexist: L'Hôpital for first-order $\tfrac{0}{0}$, Taylor for higher-order, both for sanity-checking each other.
- **Application:** asymptotic-comparison rates ($1 \ll \ln x \ll x^p \ll e^x \ll x^x$) — every comparison is a single L'Hôpital. This is the cross-domain payoff: every algorithmic-complexity argument in computer science, every "exponential beats polynomial" sentence in physics, every "logs are slow" argument in statistics, ultimately rests on these limits.
- **Bridge to philosophy:** [[Inertia and Bootstrapping]] — the foundational/recursive constraint *L'Hôpital depends on derivatives existing* is structurally the same as the bootstrap problem in compilers (you need an existing compiler to compile a compiler). Both are cold-start problems; both require an external geometric/manual tool to begin.
- **For 9709 students:** [[MF19 Reference (9709)]] — L'Hôpital is *not* on MF19 because it's not on the 9709 syllabus. P3 limits use direct substitution + factoring + standard limits. Knowing L'Hôpital is a verification tool, not a syllabus method.
- **Reverse:** there is no inverse operation — L'Hôpital is a one-way evaluation tool. The closest "reverse" is constructing limits whose derivative-ratio is a *known* limit, which is more puzzle than systematic technique.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\lim_{x \to a} \dfrac{f(x)}{g(x)}$ | `\lim_{x \to a} \dfrac{f(x)}{g(x)}` | The original limit. Subscript on `\lim` to specify the approach point. |
| $\dfrac{0}{0}$, $\dfrac{\infty}{\infty}$ | `\dfrac{0}{0}`, `\dfrac{\infty}{\infty}` | The two indeterminate forms L'Hôpital handles directly. |
| $\dfrac{f'(x)}{g'(x)}$ | `\dfrac{f'(x)}{g'(x)}` | The ratio of derivatives — *not* the derivative of the ratio. |
| $0 \cdot \infty$, $\infty - \infty$, $1^\infty$, $0^0$, $\infty^0$ | `0 \cdot \infty` etc. | The other five indeterminate forms; convertible by algebra or $\ln$. |
| $\lim_{n\to\infty}\!\left(1 + \dfrac{1}{n}\right)^n = e$ | `\lim_{n\to\infty}\left(1 + \dfrac{1}{n}\right)^n = e` | The classic $1^\infty$ limit, derived in Example 5. |
| $\lim_{h \to 0}\dfrac{\sin h}{h} = 1$ | `\lim_{h \to 0}\dfrac{\sin h}{h} = 1` | The limit you *cannot* prove with L'Hôpital. Squeeze Theorem only. |
| $f \ll g$ | `f \ll g` | "$f$ grows much slower than $g$" — $\lim f/g = 0$. The asymptotic-comparison hierarchy. |
