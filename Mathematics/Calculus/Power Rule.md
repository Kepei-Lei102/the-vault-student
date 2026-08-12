---
chinese: 幂法则 (mì fǎzé)
prerequisites:
  - "[[Differentiation]]"
  - "[[Limit]]"
  - "[[Laws of Indices]]"
  - "[[Binomial Theorem]]"
leads_to:
  - "[[Tangents and Normals]]"
  - "[[Stationary Points]]"
  - "[[Integration]]"
  - "[[Chain Rule]]"
  - "[[Error Propagation]]"
  - "[[Binomial Series]]"
  - "[[Differentiation Rules]]"
  - "[[Maclaurin Series]]"
  - "[[Product Rule]]"
  - "[[Quotient Rule]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-A13
  - syllabus/0580-E2-12
  - syllabus/0606-14-1
  - syllabus/0606-14-3
  - syllabus/9709-1-7
  - type/definition
  - type/proof
  - notation/derivative
---

# Power Rule 幂法则

## The Rule

$$\dfrac{d}{dx}\left(x^n\right) = nx^{n-1}$$

With a constant multiplier:

$$\dfrac{d}{dx}\left(kx^n\right) = knx^{n-1}$$

Read it as: **"bring the power down as a multiplier, then reduce the power by one."**

## Scope by Syllabus

| Syllabus | What $n$ can be | Examples |
|---|---|---|
| OxAQA 9260 | Positive integers and 0 | $x^3$, $x^5$, $7$ |
| Cambridge 0606 | Any rational number | $x^{-2}$, $x^{1/2}$, $x^{-3/4}$ |
| AP / IB / A-Level | Any real number | $x^{\pi}$, $x^{\sqrt{2}}$ |

The proof below covers positive integers first, then extends to all rationals.

## 中文锚点 (Chinese Anchor)

幂法则：**指数降下来当系数，指数减一**。

$$x^n \to nx^{n-1}$$

例如：$x^5 \to 5x^4$，$3x^2 \to 6x$，$7 = 7x^0 \to 0$（常数的导数为零）

为什么指数会"降下来"？因为$(x+h)^n$展开后，$x^n$消掉了，剩下的最大项是$nx^{n-1}h$，除以$h$就得到$nx^{n-1}$。这就是证明的核心——下面有完整推导。

## Proof — Positive Integer Case

This is the proof your student needs to understand *why* the power rule works. It uses first principles from [[Differentiation]].

### Step 1: Set up the limit

$$\dfrac{d}{dx}(x^n) = \lim_{h \to 0} \dfrac{(x+h)^n - x^n}{h}$$

### Step 2: Expand $(x+h)^n$ using the Binomial Theorem

$$(x+h)^n = x^n + nx^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \binom{n}{3}x^{n-3}h^3 + \cdots + h^n$$

### Step 3: Subtract $x^n$

$$(x+h)^n - x^n = nx^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \cdots + h^n$$

Every term on the right has at least one factor of $h$.

### Step 4: Divide by $h$

$$\dfrac{(x+h)^n - x^n}{h} = nx^{n-1} + \binom{n}{2}x^{n-2}h + \cdots + h^{n-1}$$

### Step 5: Take the limit $h \to 0$

Every term except $nx^{n-1}$ contains a factor of $h$, so they all vanish:

$$\lim_{h \to 0} \left[nx^{n-1} + \binom{n}{2}x^{n-2}h + \cdots + h^{n-1}\right] = nx^{n-1}$$

$$\boxed{\dfrac{d}{dx}(x^n) = nx^{n-1}} \qquad \text{for } n \in \mathbb{Z}^+$$

> [!tip] A second road — induction and the product rule
> The proof above needs the [[Binomial Theorem]] to expand $(x+h)^n$. There is a shorter route that expands nothing at all: write $x^{k+1} = x \cdot x^{k}$, apply the [[Product Rule]], and let [[Proof by Induction]] carry the result up the integers.
>
> $$\frac{d}{dx}\left(x^{k+1}\right) = 1 \cdot x^{k} + x \cdot kx^{k-1} = (k+1)x^{k}$$
>
> with base case $\frac{d}{dx}(x) = 1$. Three lines, and nothing circular — the product rule is itself proved from first principles, so it never borrows the rule being proved. Two independent proofs is exactly the reassurance a theorem this load-bearing deserves.

### Intuition: Why does $n$ "come down"?

When you expand $(x+h)^n$, you're choosing which of the $n$ brackets contributes the $h$. There are $n$ ways to pick exactly one bracket to contribute $h$ (and the rest contribute $x$). Each such choice gives $x^{n-1} \cdot h$. So the coefficient of $h$ is $nx^{n-1}$ — that's the $n$ "coming down."

> [!tip] The combinatorial view
> $(x+h)^n = (x+h)(x+h)\cdots(x+h)$ — $n$ identical brackets multiplied together.
>
> To get the term with exactly one $h$:
> - Pick which bracket gives $h$ → $n$ choices
> - The other $n-1$ brackets give $x$ → contributes $x^{n-1}$
> - Total: $n \cdot x^{n-1} \cdot h$
>
> After dividing by $h$ and letting $h \to 0$, all you're left with is $nx^{n-1}$.

## Special Cases

### Constant: $\dfrac{d}{dx}(c) = 0$

A constant $c = cx^0$. Applying the power rule: $0 \cdot cx^{-1} = 0$.

**Intuition:** A horizontal line has zero gradient everywhere.

### Linear: $\dfrac{d}{dx}(x) = 1$

$x = x^1$. Applying the power rule: $1 \cdot x^0 = 1$.

**Intuition:** The line $y = x$ has gradient 1 everywhere.

### Negative powers (0606 and above): $\dfrac{d}{dx}(x^{-n}) = -nx^{-n-1}$

Example: $\dfrac{d}{dx}\left(\dfrac{1}{x^3}\right) = \dfrac{d}{dx}(x^{-3}) = -3x^{-4} = -\dfrac{3}{x^4}$

> [!warning] Common rewriting step
> Before differentiating, always rewrite fractions and roots as powers:
> - $\dfrac{1}{x^2} = x^{-2}$
> - $\sqrt{x} = x^{1/2}$
> - $\dfrac{1}{\sqrt[3]{x}} = x^{-1/3}$
>
> The power rule only works when the expression is in the form $kx^n$.

### Fractional powers (0606 and above): $\dfrac{d}{dx}(x^{p/q}) = \dfrac{p}{q}x^{p/q - 1}$

Example: $\dfrac{d}{dx}(\sqrt{x}) = \dfrac{d}{dx}(x^{1/2}) = \dfrac{1}{2}x^{-1/2} = \dfrac{1}{2\sqrt{x}}$

## Proof Extension — Rational Exponents

The positive integer proof above doesn't cover $x^{-3}$ or $x^{1/2}$. Here's how to extend it.

### Negative integers: use the quotient rule

If $n$ is a negative integer, write $x^n = \dfrac{1}{x^{-n}}$ where $-n$ is a positive integer. Differentiating using the quotient rule (a corollary inside [[Product Rule]]):

$$\dfrac{d}{dx}\left(\dfrac{1}{x^m}\right) = \dfrac{0 \cdot x^m - 1 \cdot mx^{m-1}}{(x^m)^2} = \dfrac{-mx^{m-1}}{x^{2m}} = -mx^{-m-1}$$

This matches $nx^{n-1}$ with $n = -m$. ✓

### Fractional exponents: use the chain rule

If $n = \dfrac{p}{q}$, let $y = x^{p/q}$, so $y^q = x^p$. Differentiate both sides implicitly:

$$qy^{q-1} \cdot \dfrac{dy}{dx} = px^{p-1}$$

$$\dfrac{dy}{dx} = \dfrac{px^{p-1}}{qy^{q-1}} = \dfrac{px^{p-1}}{q(x^{p/q})^{q-1}} = \dfrac{px^{p-1}}{qx^{p(q-1)/q}} = \dfrac{p}{q}x^{p-1-p(q-1)/q}$$

The exponent simplifies: $p - 1 - \dfrac{p(q-1)}{q} = p - 1 - p + \dfrac{p}{q} = \dfrac{p}{q} - 1$.

$$\boxed{\dfrac{d}{dx}(x^{p/q}) = \dfrac{p}{q}x^{p/q - 1}} \qquad \text{✓}$$

> [!info] Why show these proofs?
> The power rule for positive integers is elegant and self-contained. The extensions to negative and fractional exponents rely on the quotient rule and chain rule — which are proved in their own notes. This means the *full* power rule is actually a theorem that rests on all four differentiation rules working together. You don't need these proofs for 9260 or even 0606, but seeing them reveals how interconnected calculus is.

### Irrational exponents: requires $e^x$ and $\ln x$

What about $x^\pi$ or $x^{\sqrt{2}}$? We can't use the binomial theorem (it needs an integer $n$) or implicit differentiation (it needs a rational $p/q$).

The trick is to rewrite using $e$ and $\ln$:

$$x^\alpha = e^{\alpha \ln x}$$

This works for *any* real $\alpha$ — rational or irrational. Now differentiate using the chain rule:

$$\dfrac{d}{dx}(e^{\alpha \ln x}) = e^{\alpha \ln x} \cdot \dfrac{\alpha}{x} = x^\alpha \cdot \dfrac{\alpha}{x} = \alpha x^{\alpha - 1}$$

$$\boxed{\dfrac{d}{dx}(x^\alpha) = \alpha x^{\alpha - 1}} \qquad \text{for any } \alpha \in \mathbb{R} \text{ ✓}$$

> [!warning] Honest dependency
> This proof requires two results we haven't proved yet:
> - $\dfrac{d}{dx}(e^x) = e^x$ — see [[Differentiation Rules]]
> - $\dfrac{d}{dx}(\ln x) = \dfrac{1}{x}$ — see [[Differentiation Rules]]
>
> Without these, the irrational case *cannot* be proved. The power rule for irrational exponents is not a standalone fact — it depends on the exponential and logarithmic functions. We'll prove those results in [[Differentiation Rules]]; for now, trust that they work, and the power rule extends to all real numbers.

## Worked Examples

### Example 1 (9260 level): Differentiate $y = 3x^4 - 5x^2 + 7x - 2$

$$\dfrac{dy}{dx} = 3 \cdot 4x^3 - 5 \cdot 2x + 7 \cdot 1 - 0 = 12x^3 - 10x + 7$$

### Example 2 (0606 level): Differentiate $y = \dfrac{4}{x^2} + 3\sqrt{x}$

First rewrite: $y = 4x^{-2} + 3x^{1/2}$

$$\dfrac{dy}{dx} = 4(-2)x^{-3} + 3 \cdot \dfrac{1}{2}x^{-1/2} = -8x^{-3} + \dfrac{3}{2}x^{-1/2} = -\dfrac{8}{x^3} + \dfrac{3}{2\sqrt{x}}$$

## Common Misconceptions (Teaching Notes)

### 1. Forgetting the coefficient $n$

Students write $\dfrac{d}{dx}(x^5) = x^4$ instead of $5x^4$.

**Fix:** "Bring down the power" — physically write the $n$ first, then reduce. Some students benefit from arrows: draw an arrow from the exponent down to the front of the term.

### 2. Not rewriting before differentiating

Students try to differentiate $\dfrac{1}{x^2}$ directly without rewriting as $x^{-2}$, or they try $\sqrt{x}$ without writing $x^{1/2}$.

**Fix:** Make the rewrite a mandatory first step. "If it's not in the form $kx^n$, rewrite it first."

### 3. The constant term

Students write $\dfrac{d}{dx}(5) = 5$ or $\dfrac{d}{dx}(5) = 1$. The answer is $0$.

**Fix:** "Constants are flat lines. Flat lines have zero gradient."

### 4. Confusing the power rule with the exponential rule

$\dfrac{d}{dx}(x^3) = 3x^2$ (power rule — variable base, constant exponent)

$\dfrac{d}{dx}(3^x) = 3^x \ln 3$ (exponential rule — constant base, variable exponent)

Students mix these up. At 9260, only the power rule appears. At 0606/AP, both appear — see [[Differentiation Rules]].

## Exam Notes

### OxAQA 9260

- A13: differentiate $kx^n$ where $n$ is a positive integer or 0
- This is the only differentiation rule at 9260 — no chain rule, no product rule, no trig
- Combined with linearity: differentiate any polynomial term by term
- Knowing the proof is not required but helps understanding

### Cambridge 0606

- 14.3 includes: $x^n$ for rational $n$
- Students must rewrite expressions before differentiating (fractions, roots)
- The power rule is one of many rules at 0606 — see [[Differentiation Rules]] for trig, $e^x$, $\ln x$

> [!tip] Physics bridge — the "$n$ times" rule for percentage uncertainties
> Every Physics student has memorised: *"the percentage uncertainty in $V = \tfrac{4}{3}\pi r^3$ is **three times** the percentage uncertainty in $r$."* Where does that 3 come from? Power rule.
>
> Take $z = x^n$ and differentiate: $dz = nx^{n-1}\,dx$. Divide both sides by $z = x^n$:
> $$\dfrac{dz}{z} = \dfrac{nx^{n-1}\,dx}{x^n} = n\,\dfrac{dx}{x}.$$
> Read this as fractional changes: a fractional change of size $\dfrac{\Delta x}{x}$ in $x$ produces a fractional change of size $n\dfrac{\Delta x}{x}$ in $z = x^n$. The exponent $n$ shows up *as a multiplier* on the percentage error.
>
> **Sphere volume.** $V = \tfrac{4}{3}\pi r^3$, so $n = 3$. If you measure $r$ to within $\pm 1\%$, the volume is uncertain to $\pm 3\%$. (The constant $\tfrac{4}{3}\pi$ doesn't enter — constants have zero percentage uncertainty: $\dfrac{d(\text{const})}{\text{const}} = 0$.)
>
> **Pendulum period.** $T = 2\pi\sqrt{L/g}$, so $T \propto L^{1/2}$ in $L$. A $4\%$ uncertainty in $L$ gives only $2\%$ uncertainty in $T$ — fractional powers *shrink* the percentage error.
>
> The general rule is the chain rule on $\ln$: $\ln z = n\ln x \;\Rightarrow\; \dfrac{dz}{z} = n\dfrac{dx}{x}$. See [[Error Propagation]] (Physics) for the full treatment, and [[Chain Rule]] for the master equation that includes products, quotients, and arbitrary $f(x)$.

## Connections

- **Parent:** [[Differentiation]] — the power rule is proved using the limit definition
- **Proof ingredient:** [[Binomial Theorem]] — needed for the positive integer proof
- **Extensions:** [[Chain Rule]] — needed for the fractional exponent proof
- **Extensions:** [[Product Rule]] — the quotient rule (a corollary inside that card) is what makes the negative-exponent proof go through
- **Reverse:** [[Integration]] — reversing the power rule gives $\int x^n\,dx = \dfrac{x^{n+1}}{n+1} + C$ (except $n = -1$)
- **Application:** [[Stationary Points]] — set the derivative (found via power rule) to zero
- **Application:** [[Tangents and Normals]] — gradient found via power rule
- **Application — Physics bridge:** [[Error Propagation]] — the "exponent $n$ multiplies the percentage uncertainty" rule (sphere volume, pendulum period) is one line of power-rule algebra divided through by $z$.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{d}{dx}(x^n) = nx^{n-1}$ | `\dfrac{d}{dx}(x^n) = nx^{n-1}` | The power rule |
| $\binom{n}{k}$ | `\binom{n}{k}` | Binomial coefficient — used in proof |
| $\mathbb{Z}^+$ | `\mathbb{Z}^+` | Positive integers |
| $\boxed{\text{result}}$ | `\boxed{\text{result}}` | Box for final answers |
