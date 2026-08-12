---
chinese: 三角方程 (sānjiǎo fāngchéng)
prerequisites:
  - "[[Trigonometric Identities]]"
  - "[[Trigonometric Functions]]"
  - "[[Trigonometric Ratios]]"
  - "[[Radians]]"
  - "[[Quadratic Equations]]"
  - "[[Exact Trigonometric Values]]"
  - "[[Trigonometric Graphs]]"
leads_to:
  - "[[Substitution Equations]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-10-5
  - syllabus/9709-1-5
  - syllabus/9709-3-3
  - syllabus/9709-2-3
  - type/deep
  - type/technique
  - misconception/missing-second-solution
  - misconception/multiple-angle-domain
  - misconception/calculator-only-gives-principal-value
---

# Trigonometric Equations 三角方程

## Definition

A **trigonometric equation** is an equation involving trig functions of an unknown — and it asks for *specific* values of $x$ that make it true (vs. an *identity*, which is true for *all* $x$ — see [[Trigonometric Identities]] for the contrast).

Examples:

- $\sin x = \tfrac{1}{2}$ — true at $x = \pi/6, 5\pi/6, \pi/6 + 2\pi, \dots$ (infinitely many)
- $2\cos^2 x - 1 = \cos x$ — true at finitely many $x$ in any bounded interval
- $\sin 3x = \cos x$ — true at $x = \pi/8, 3\pi/8, \dots$

The skill is **reducing every trig equation to the standard form**

$$
\boxed{\,\text{(one trig function)}(\text{one argument}) = c\,}
$$

and then *systematically finding all solutions* of that standard form within a given domain.

### 中文锚点

三角方程 = 含未知数的三角函数等式，求满足等式的 $x$ 值。区别于"三角恒等式"（对所有 $x$ 成立）。解三角方程的核心技巧：把方程**变形为标准形式** *(一个三角函数)(一个角度) = 常数*，然后用单位圆 / CAST 图找出所有解。每个周期内一般有 *两个* 解（$\sin x = c$, $\cos x = c$）或 *一个* 解（$\tan x = c$，因为周期是 $\pi$）。最容易丢分的地方：**漏掉第二个解**。

---

## The Solving Template — Three Steps

Once an equation is in standard form $\text{trig}(x) = c$:

**Step 1 — Find the principal value.** Use $\arcsin$, $\arccos$, or $\arctan$ to get *one* solution $x_0$. (Calculators return this.)

**Step 2 — Find the second solution in the period.** Each function's symmetry gives the second:

| Equation | Principal $x_0$ | Second solution in $[0, 2\pi)$ |
|---|---|---|
| $\sin x = c$ | $\arcsin c \in [-\pi/2, \pi/2]$ | $\pi - x_0$ |
| $\cos x = c$ | $\arccos c \in [0, \pi]$ | $2\pi - x_0$ (or equivalently $-x_0$) |
| $\tan x = c$ | $\arctan c \in (-\pi/2, \pi/2)$ | $x_0 + \pi$ (and that's the *only* second one — period is $\pi$) |

**Step 3 — Add full periods.** Sin and cos repeat every $2\pi$; tan repeats every $\pi$. So the **general solution** is:

| Equation | General solution |
|---|---|
| $\sin x = c$ | $x = x_0 + 2\pi n$ or $x = (\pi - x_0) + 2\pi n$, $n \in \mathbb{Z}$ |
| $\cos x = c$ | $x = \pm x_0 + 2\pi n$, $n \in \mathbb{Z}$ |
| $\tan x = c$ | $x = x_0 + \pi n$, $n \in \mathbb{Z}$ |

Restrict to the given domain by picking the appropriate $n$.

![[trig-equations-unit-circle.svg]]

The diagram shows the "two solutions per period" geometry. For $\sin x = c$, the two solutions are the two $x$-values where the **horizontal line** $y = c$ meets the unit circle. For $\cos x = c$, the two solutions are the two $x$-values where the **vertical line** $x = c$ meets the unit circle. For $\tan x = c$, the two solutions are *diametrically opposite* — same line through the origin, intersecting the circle at antipodal points — which is why the period is $\pi$ instead of $2\pi$.

> [!tip] CAST diagram — the four-quadrant cheat sheet
> The unit circle, divided into four quadrants, tells you in which quadrants each trig function is positive: in **C**(quadrant IV: $\cos$), **A**(quadrant I: All), **S**(quadrant II: $\sin$), **T**(quadrant III: $\tan$). Once you know the principal value lives in the "All" quadrant, the second solution lives in the *partner quadrant* (S for sin, C for cos, T for tan). This is the same information as the table above, just packaged geometrically.

---

## Family 1 — Linear in One Trig Function

Standard form already. **Just apply the template.**

**Example.** Solve $2\sin x + 1 = 0$ on $0 \le x < 2\pi$.

Rearrange: $\sin x = -\tfrac{1}{2}$.

Principal: $x_0 = \arcsin(-\tfrac{1}{2}) = -\pi/6$. *Outside the given domain*, so add $2\pi$: $x_0 = 11\pi/6$. (Or recognise $\sin = -\tfrac{1}{2}$ at $x = 7\pi/6, 11\pi/6$ directly from CAST + special-angle table.)

Second solution in $[0, 2\pi)$: $\pi - (-\pi/6) = 7\pi/6$.

**Solutions: $x = 7\pi/6, 11\pi/6$.** ✓ (sin is negative in quadrants III and IV — matches CAST.)

---

## Family 2 — Quadratic in One Trig Function

Treat the trig function as the unknown and **factorise**.

**Example.** Solve $2\cos^2 x - \cos x - 1 = 0$ on $0 \le x < 2\pi$.

Let $u = \cos x$. The equation becomes $2u^2 - u - 1 = 0$, which factorises as $(2u + 1)(u - 1) = 0$, giving $u = -\tfrac{1}{2}$ or $u = 1$.

Now solve each:

- $\cos x = -\tfrac{1}{2}$: $x_0 = \arccos(-\tfrac{1}{2}) = 2\pi/3$; second solution $2\pi - 2\pi/3 = 4\pi/3$.
- $\cos x = 1$: $x_0 = 0$; second solution $2\pi - 0 = 2\pi$, *outside the domain* (open at $2\pi$). So just $x = 0$.

**Solutions: $x = 0, 2\pi/3, 4\pi/3$.**

> [!tip] Watch for "trig $\equiv u$" disguises
> $3\sin^2 x + 5\sin x = 2$ is a quadratic in $\sin x$ — substitute $u = \sin x$ first. If you don't make the substitution explicit, you're likely to write nonsense like "$\sin x = (-5 \pm \sqrt{49})/6$" and forget that $\sin x$ is constrained to $[-1, 1]$. The substitution makes the constraint visible — discard any $u$ outside $[-1, 1]$ as having no real solution.

---

## Family 3 — Mixed Functions, Reducible via Pythagorean Identity

When two different trig functions appear, use $\sin^2 x + \cos^2 x = 1$ (or its corollaries — see [[Trigonometric Identities]]) to **convert one function into the other**. The equation then reduces to Family 2.

**Example.** Solve $\sin^2 x + \cos x = 1$ on $0 \le x < 2\pi$.

Replace $\sin^2 x$ with $1 - \cos^2 x$:

$$
(1 - \cos^2 x) + \cos x = 1 \;\;\Longrightarrow\;\; \cos^2 x - \cos x = 0 \;\;\Longrightarrow\;\; \cos x(\cos x - 1) = 0.
$$

So $\cos x = 0$ or $\cos x = 1$:

- $\cos x = 0$: $x = \pi/2, 3\pi/2$.
- $\cos x = 1$: $x = 0$ (and $2\pi$, outside domain).

**Solutions: $x = 0, \pi/2, 3\pi/2$.**

The pattern: *eliminate the squared function* using Pythagoras. If you see $\sin^2$ alongside a stray $\cos$, convert the $\sin^2$ to $1 - \cos^2$. If you see $\sec^2$ with a stray $\tan$, convert $\sec^2$ to $1 + \tan^2$. The goal is to get a polynomial in **one** trig function.

---

## Family 4 — Multiple-Angle Equations

The trickiest family: arguments like $2x$, $3x$, $\frac{x}{2}$, or $x + \pi/4$. The strategy is **substitute $u$ for the inner expression, transform the domain accordingly, solve in $u$, then convert back**.

**Example.** Solve $\cos 3x = \tfrac{1}{2}$ on $0 \le x \le 2\pi$.

Let $u = 3x$. The original domain $0 \le x \le 2\pi$ becomes $0 \le u \le 6\pi$ (a *triple-length* domain — this is the trap).

Now solve $\cos u = \tfrac{1}{2}$ on $0 \le u \le 6\pi$:

Principal $u_0 = \pi/3$; second-in-period $5\pi/3$. Add $2\pi$ to each to fill $6\pi$:

$$
u = \tfrac{\pi}{3},\ \tfrac{5\pi}{3},\ \tfrac{\pi}{3} + 2\pi = \tfrac{7\pi}{3},\ \tfrac{5\pi}{3} + 2\pi = \tfrac{11\pi}{3},\ \tfrac{\pi}{3} + 4\pi = \tfrac{13\pi}{3},\ \tfrac{5\pi}{3} + 4\pi = \tfrac{17\pi}{3}.
$$

That's *six* values of $u$ — three pairs, since the period $2\pi$ in $u$ corresponds to period $2\pi/3$ in $x$, and the original domain is three full $x$-periods long.

Convert back: $x = u/3$. Solutions: $x = \tfrac{\pi}{9}, \tfrac{5\pi}{9}, \tfrac{7\pi}{9}, \tfrac{11\pi}{9}, \tfrac{13\pi}{9}, \tfrac{17\pi}{9}$.

> [!tip] The multiple-angle domain trap
> Equation $\sin nx = c$ on $0 \le x \le 2\pi$ has $2n$ solutions in general. **Don't solve for $u = nx$ on $[0, 2\pi]$** — that gives only the first $1/n$th of the solutions. Either expand the $u$-domain to $[0, 2n\pi]$ (cleanest, what we did above), or solve on $[0, 2\pi]$ and add multiples of $2\pi/n$ (also valid, but error-prone). Always cross-check the count: $\sin 2x = c$ has $4$ solutions in $[0, 2\pi]$ generically, $\cos 3x = c$ has $6$, etc.

---

## Family 4 (cont.) — Equations With Two Different Multiple Angles

When *both* $\sin nx$ and $\sin x$ (or similar) appear, expand the multiple angle using a **double-angle formula** (see [[Trigonometric Identities]]) to get a single argument. This is beyond 0606 but standard for **9709 Paper 3 §3.3**, A-Level Pure, IB AA, and AP.

**Example.** Solve $\sin 2x = \sin x$ on $0 \le x < 2\pi$.

Use $\sin 2x = 2\sin x \cos x$:

$$
2\sin x \cos x = \sin x \;\;\Longrightarrow\;\; \sin x(2\cos x - 1) = 0.
$$

So $\sin x = 0$ or $\cos x = \tfrac{1}{2}$:

- $\sin x = 0$: $x = 0, \pi$.
- $\cos x = \tfrac{1}{2}$: $x = \pi/3, 5\pi/3$.

**Solutions: $x = 0, \pi/3, \pi, 5\pi/3$.**

> [!warning] Don't divide by $\sin x$ in this kind of equation
> A natural-looking shortcut is to divide both sides by $\sin x$: $2\cos x = 1$, giving $\cos x = 1/2$, missing the $\sin x = 0$ solutions. **Never divide by something that could be zero in the variable's range** — instead, factor and apply the zero-product principle. This is the same trap as algebraically dividing $x^2 = x$ by $x$ to get $x = 1$ (and missing $x = 0$).

---

## $R\sin(x + \alpha)$ Form (A-Level / IB / AP — Beyond 0606)

For equations like $a\sin x + b\cos x = c$, the trick is to *combine the two trig terms into a single sinusoid*. This converts a Family-3-looking equation into Family 1.

The identity:

$$
a\sin x + b\cos x = R\sin(x + \alpha) \qquad \text{where}\quad R = \sqrt{a^2 + b^2},\;\;\tan\alpha = \frac{b}{a}.
$$

(Proof: expand $R\sin(x + \alpha) = R\sin x\cos\alpha + R\cos x\sin\alpha$ and match to $a\sin x + b\cos x$, giving $R\cos\alpha = a$, $R\sin\alpha = b$.)

**Example.** Solve $\sin x + \sqrt{3}\cos x = 1$ on $0 \le x < 2\pi$ (A-Level).

$R = \sqrt{1 + 3} = 2$, $\tan\alpha = \sqrt{3}/1 = \sqrt{3}$, so $\alpha = \pi/3$.

The equation becomes $2\sin(x + \pi/3) = 1$, i.e., $\sin(x + \pi/3) = 1/2$. Substitute $u = x + \pi/3$, with the domain shifting to $\pi/3 \le u < 7\pi/3$:

Solving $\sin u = 1/2$: $u = \pi/6, 5\pi/6$, plus their $+2\pi$ shifts: $13\pi/6, 17\pi/6$. Restrict to $[\pi/3, 7\pi/3)$: only $5\pi/6, 13\pi/6$ qualify.

Convert back: $x = u - \pi/3 = \pi/2, 11\pi/6$. ✓

The $R\sin$ trick also gives the **maximum** ($R$) and **minimum** ($-R$) of $a\sin x + b\cos x$ for free — useful for "find the largest possible value" exam questions.

> [!info] Beyond syllabus — why $R\sin(x+\alpha)$ works
> The identity is just the sum formula in reverse. Geometrically, $a\sin x + b\cos x$ is the *dot product* of two vectors: $(\sin x, \cos x)$ (a unit-circle point) with $(a, b)$ (a fixed vector). The dot product equals $|(a, b)|\cos(\text{angle between})$, and the angle between is exactly $\pi/2 - x - \alpha$ for the right $\alpha$. So the maximum is $|(a, b)| = R$, achieved when the two vectors align. See [[Vectors]] for the dot-product side; this connection between trig identities and dot products is one of the cleanest interfaces in mathematics.

---

## Common Mistakes

1. **Calculator gives only the principal value.** $\arcsin(0.5) = \pi/6$ on every calculator — *that's just one solution*. Always find the second-in-period (and any further-period shifts in the given domain). The single most common mistake.
2. **Forgetting to transform the domain in multiple-angle problems.** Solving $\sin 2x = c$ on $[0, 2\pi]$ requires solving $\sin u = c$ on $[0, 4\pi]$, not $[0, 2\pi]$. Halve the $u$-solutions back to $x$.
3. **Dividing by a trig term that could be zero.** $2\sin x\cos x = \sin x$ should be factored, not divided. Dividing by $\sin x$ silently discards the $\sin x = 0$ solutions.
4. **Squaring both sides without checking.** If you square an equation to eliminate radicals, *always* substitute solutions back into the original to discard extraneous roots. Squaring can introduce false solutions.
5. **Confusing $\sin^{-1}$ (inverse) with $1/\sin$ (reciprocal).** $\sin^{-1}(0.5) = \arcsin(0.5) = \pi/6$. $(\sin x)^{-1} = \csc x$. Notation is unfortunately overloaded.
6. **Solutions outside $[-1, 1]$ for $\sin/\cos$.** A quadratic in $\sin x$ might give $u = \sin x = 2$ as one root — *no real solution* (the sine function never exceeds $1$). Discard.
7. **Solving $\tan x = c$ and over-counting.** Tan has period $\pi$, not $2\pi$. So in $[0, 2\pi]$ there are *two* solutions of $\tan x = c$ — at $x_0$ and $x_0 + \pi$. Don't add a second solution per quadrant the way you would for sin/cos.

---

## Exam Notes

### Cambridge 0606

**Syllabus ref:** §10.5. Cambridge specifically lists the example types: $\sin^2 A = 1$, $\cos^2 A + \sin A = 1$, $\cos A = 2\sin A$ (which becomes $\tan A = 1/2$), $\sin^2 2A = 1/4$, $\cos 3A = 1/2$. Expect 4–6 mark questions, "*Solve … for $0° \le x \le 360°$*" or similar in radians. Always give *all* solutions in the stated interval; one missed solution typically costs one mark.

**0606 does NOT require:** sum/difference formulas, double-angle formulas (so the "Family 4 cont." example with $\sin 2x = \sin x$ is technically beyond — but the technique uses only what 0606 gives you in §10.4, so a strong student can do it).

### A-Level / 9709

A-Level extends to: sum/difference and double-angle equations (P2, P3), $R\sin(x + \alpha)$ form, and equations involving inverse trig functions. The above template still applies, with these additional algebraic moves on top.

### IB AA HL & AP Calculus

Same content as A-Level. AP also tests trig equations as part of *related rates* and *implicit differentiation* problems — the equation-solving step is just one stage of a longer problem.

### IB AA SL

Pythagorean reductions, double-angle, and basic equations — essentially A-Level Pure 2 scope.

---

## Connections

- **Prerequisite:** [[Trigonometric Identities]] — the identities used in Family 3 (Pythagorean reduction) and Family 4 (multiple angle to single angle)
- **Prerequisite:** [[Trigonometric Functions]] — the unit-circle definition that makes the "two solutions per period" geometry visible
- **Prerequisite:** [[Quadratic Equations]] — Family 2 is a quadratic in disguise
- **Prerequisite:** [[Radians]] — the natural unit for trig equations in calculus contexts
- **Sibling:** [[Trigonometric Identities]] — solve vs prove are the two skills in §10
- **Application:** *physics* — solving $\sin(\omega t + \phi) = c$ is the basic move in oscillator and wave problems (when does the pendulum return to position $X$?)
- **Application:** *AC circuits* — $V(t) = V_0\sin(\omega t)$ crossing a threshold is a trig equation
- **Application:** *astronomy* — when does the sun reach altitude $\theta$? When does a planet appear at position $\phi$ in its orbit? All trig equations
- **Beyond high school:** *Fourier analysis* — every periodic signal is a sum of sinusoids, and decomposing/recombining them reduces to families of trig equations

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\arcsin x$ | `\arcsin x` | inverse sine; preferred over $\sin^{-1}$ to avoid notation clash |
| $\arccos x$ | `\arccos x` | inverse cosine |
| $\arctan x$ | `\arctan x` | inverse tangent |
| $2\pi n$ | `2\pi n` | period offset for $\sin / \cos$ |
| $\pi n$ | `\pi n` | period offset for $\tan$ |
| $R\sin(x+\alpha)$ | `R\sin(x+\alpha)` | combined sinusoid form |
| $\le x \le 2\pi$ | `\le x \le 2\pi` | typical exam domain |
| $\,\square$ | `\,\square` | end-of-proof marker |
