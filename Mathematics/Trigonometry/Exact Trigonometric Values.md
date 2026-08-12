---
chinese: 三角函数特殊值 (sānjiǎo hánshù tèshū zhí)
prerequisites:
  - "[[Trigonometric Ratios]]"
  - "[[Pythagoras Theorem]]"
  - "[[Surds]]"
leads_to:
  - "[[Trigonometric Equations]]"
  - "[[Trigonometric Identities]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/0580-E6-3
  - type/synthesis
  - type/reference
  - misconception/decimal-vs-exact
---

# Exact Trigonometric Values 三角函数特殊值

## Definition

For a small handful of "special" angles — namely $0°, 30°, 45°, 60°, 90°, 180°$ (and their multiples) — the values of $\sin$, $\cos$, and $\tan$ are *exact* rational, surd, or zero/one expressions. **Memorising these** (or being able to derive them in 30 seconds) is essential at IGCSE and beyond, because exam questions routinely require *exact* answers — leaving $\sin 60° = \dfrac{\sqrt 3}{2}$ rather than $0.866$.

The full table:

| $\theta$ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|---|---|---|---|
| $0°$ | $0$ | $1$ | $0$ |
| $30°$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3}$ |
| $45°$ | $\dfrac{\sqrt{2}}{2} = \dfrac{1}{\sqrt 2}$ | $\dfrac{\sqrt{2}}{2}$ | $1$ |
| $60°$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}$ | $\sqrt{3}$ |
| $90°$ | $1$ | $0$ | undefined |
| $180°$ | $0$ | $-1$ | $0$ |

This card derives all of these from **two reference triangles** (the $30$–$60$–$90$ and the $45$–$45$–$90$) plus the unit-circle definitions for $0°, 90°, 180°$.

### 中文锚点

**三角函数特殊值** = 在 $0°, 30°, 45°, 60°, 90°, 180°$ 这几个"特殊角"上，三角函数值是**精确的** (jīngquè) 有理数或带根号的表达式 —— 不是小数。

考试常见要求："Find the **exact** value of $\sin 60°$" → 写 $\dfrac{\sqrt{3}}{2}$，**不要**写 $0.866$。

来源：两个**参考三角形** (cānkǎo sānjiǎoxíng)：
- **30-60-90 三角形**：从等边三角形对半剪开
- **45-45-90 三角形**：从正方形沿对角线剪开

加上**单位圆 (dānwèi yuán)** 上 $0°, 90°, 180°$ 的直接读取。

---

## Why "Exact"?

A decimal like $0.5$ *is* exactly equal to $\dfrac{1}{2}$ — no precision lost. But $0.866$ is *not* exactly $\dfrac{\sqrt 3}{2}$; it's a 3-decimal approximation, and using it propagates a small error through the rest of the calculation.

When the answer is meant to be exact (e.g., "Show that the area is $9\sqrt 3$"), substituting decimal trig values *guarantees* the proof fails. Cambridge 0580/0606 use the word "**exact**" specifically to signal "leave surds and fractions as they are."

> [!tip] When to use exact, when to use decimal
> - "Find the **exact** value" / "Show that $\ldots = \dfrac{\sqrt 3}{2}$" / "Give your answer in **surd form**" → use the table; *no* calculator-decimal substitution.
> - "Calculate the angle correct to 1 decimal place" → calculator. Exact values aren't required.
>
> Read the question's last line. If it says "exact" or specifies surd form, the special-value table is non-negotiable.

---

## Reference Triangle 1 — the 30-60-90 (from the equilateral)

**Construction.** Start with an equilateral triangle of side $2$. Drop a perpendicular from the apex to the base. The base is bisected (by the symmetry of the equilateral), so the perpendicular foots at the midpoint, splitting the equilateral into two congruent right triangles.

![[exact-trig-30-60-90.svg]]

Each half-triangle has:
- Hypotenuse $= 2$ (a side of the original equilateral)
- Short leg $= 1$ (half of the bisected base)
- Long leg $= \sqrt{2^2 - 1^2} = \sqrt 3$ (Pythagoras)
- Angles: $30°$ (at the apex of the equilateral, because $60° / 2 = 30°$), $60°$ (the original equilateral's base angle), and $90°$ (the perpendicular foot).

So the **30-60-90 triangle** has side ratios $1 : \sqrt 3 : 2$, with the smallest side opposite the smallest angle ($30°$).

**Reading off trig values.** From this triangle (using SOH-CAH-TOA on the $30°$ angle):
$$\sin 30° = \frac{\text{opp}}{\text{hyp}} = \frac{1}{2}, \quad \cos 30° = \frac{\text{adj}}{\text{hyp}} = \frac{\sqrt 3}{2}, \quad \tan 30° = \frac{\text{opp}}{\text{adj}} = \frac{1}{\sqrt 3}.$$

For the $60°$ angle, "opposite" and "adjacent" swap (since the angle is the *other* acute one):
$$\sin 60° = \frac{\sqrt 3}{2}, \quad \cos 60° = \frac{1}{2}, \quad \tan 60° = \sqrt 3.$$

So $\sin 30° = \cos 60° = \tfrac{1}{2}$ and $\sin 60° = \cos 30° = \tfrac{\sqrt 3}{2}$ — the **co-function relationship** $\sin\theta = \cos(90° - \theta)$ visible directly on the triangle.

---

## Reference Triangle 2 — the 45-45-90 (from the unit square)

**Construction.** Start with a unit square (side $1$). Cut along one diagonal. The diagonal has length $\sqrt{1^2 + 1^2} = \sqrt 2$ (Pythagoras), and the two halves are isoceles right triangles with two $45°$ angles.

![[exact-trig-45-45-90.svg]]

Each half-triangle has:
- Two equal legs of length $1$
- Hypotenuse $\sqrt 2$
- Angles $45°, 45°, 90°$

**Reading off trig values.** With the angle at the $45°$ corner:
$$\sin 45° = \cos 45° = \frac{1}{\sqrt 2} = \frac{\sqrt 2}{2}, \quad \tan 45° = \frac{1}{1} = 1.$$

Both legs are equal, so $\sin 45° = \cos 45°$ — the symmetry of the square is what enforces this.

> [!info] Rationalising $\dfrac{1}{\sqrt 2}$
> $\dfrac{1}{\sqrt 2}$ and $\dfrac{\sqrt 2}{2}$ are the same value — but the *rationalised* form $\dfrac{\sqrt 2}{2}$ has no surd in the denominator, which is the conventional Cambridge format. To convert: multiply numerator and denominator by $\sqrt 2$. See [[Surds]] for the rationalisation rule.

---

## The Unit Circle for 0°, 90°, 180°, 270°

The unit circle (radius 1, centred at origin) gives the *cleanest* derivation of the **cardinal-angle** values. By definition,

$$(x, y) = (\cos\theta, \sin\theta)$$

is the point on the unit circle at angle $\theta$ measured anticlockwise from the positive $x$-axis.

![[exact-trig-unit-circle.svg]]

So:

| $\theta$ | Point on circle | $\cos\theta$ | $\sin\theta$ | $\tan\theta$ |
|---|---|---|---|---|
| $0°$ | $(1, 0)$ | $1$ | $0$ | $0$ |
| $90°$ | $(0, 1)$ | $0$ | $1$ | undefined |
| $180°$ | $(-1, 0)$ | $-1$ | $0$ | $0$ |
| $270°$ | $(0, -1)$ | $0$ | $-1$ | undefined |
| $360°$ | $(1, 0)$ (same as $0°$) | $1$ | $0$ | $0$ |

> [!warning] $\tan 90°$ is **undefined, period**
> $\tan\theta = \sin\theta / \cos\theta$, and $\cos 90° = 0$. The bare expression $\dfrac{1}{0}$ has no value (see [[Reciprocals (Vocab)]] for the full discussion).
> - The "$\tan 90° = \infty$" claim comes from a *different* question: not "what is $\tan 90°$?" but "what does $\tan\theta$ do as $\theta$ approaches $90°$?" That's a **limit**, and like all limits the answer depends on which side: $\tan\theta \to +\infty$ as $\theta \to 90°^-$, but $\tan\theta \to -\infty$ as $\theta \to 90°^+$. Same approach to $90°$, *opposite* limits — because the function is doing different things on the two sides.
> - **Lesson.** A bare expression like $\tan 90°$ has no inherent meaning; meaning lives in context. At 0580 there's no context, so $\tan 90°$ is **undefined, period**. Calculus brings the context (a function and a limit), and even then the "answer" depends on which direction you approach from.
> - In an exam: write "undefined" or "$\tan 90°$ does not exist." Never write "$\tan 90° = \infty$" — that's a limit statement masquerading as an equation.

---

## The "$\dfrac{\sqrt n}{2}$" Memory Trick

A pattern that simplifies memorising the sine row:

| $\theta$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ |
|---|---|---|---|---|---|
| $\sin\theta$ | $\dfrac{\sqrt 0}{2}$ | $\dfrac{\sqrt 1}{2}$ | $\dfrac{\sqrt 2}{2}$ | $\dfrac{\sqrt 3}{2}$ | $\dfrac{\sqrt 4}{2}$ |
| simplified | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt 2}{2}$ | $\dfrac{\sqrt 3}{2}$ | $1$ |

So $\sin$ at the five common angles is $\dfrac{\sqrt n}{2}$ for $n = 0, 1, 2, 3, 4$ in order.

**Cosine row is the *reverse*:** $\cos\theta = \sin(90° - \theta)$, so $\cos$ runs $1, \dfrac{\sqrt 3}{2}, \dfrac{\sqrt 2}{2}, \dfrac{1}{2}, 0$ — the same sequence backwards.

> [!tip] Co-function identity in disguise
> $\sin\theta = \cos(90° - \theta)$ and $\cos\theta = \sin(90° - \theta)$ — that's the *co* in *co*sine ("complementary sine"). The $\sin$ and $\cos$ rows of the table are mirror images for this reason. If you know one row, you immediately know the other.

---

## Worked Examples

### Example 1 — exact area

> Find the exact area of an equilateral triangle with side length $6$ cm.

Drop a perpendicular: it has length $6 \cdot \sin 60° = 6 \cdot \dfrac{\sqrt 3}{2} = 3\sqrt 3$ cm. Area = $\tfrac{1}{2}(6)(3\sqrt 3) = 9\sqrt 3$ cm².

(Alternatively, the formula $A = \tfrac{\sqrt 3}{4} s^2$ gives the same result for any equilateral triangle.)

### Example 2 — finding a side using exact trig

> A right triangle has hypotenuse $10$ cm and one of its acute angles is $30°$. Find the *exact* lengths of the other two sides.

Side opposite $30°$: $10 \sin 30° = 10 \cdot \tfrac{1}{2} = 5$ cm.
Side adjacent to $30°$: $10 \cos 30° = 10 \cdot \dfrac{\sqrt 3}{2} = 5\sqrt 3$ cm.

### Example 3 — exact value of a trig combination

> Find the exact value of $2\sin 60° \cos 30°$.

$2 \cdot \dfrac{\sqrt 3}{2} \cdot \dfrac{\sqrt 3}{2} = 2 \cdot \dfrac{3}{4} = \dfrac{3}{2}$.

(This is one application of the double-angle formula: $\sin(2\theta) = 2\sin\theta\cos\theta$, so the expression equals $\sin 120° = \dfrac{\sqrt 3}{2}$ — interesting cross-check, but you wouldn't need the formula at 0580 level.)

---

## Common Mistakes

1. **Decimal substitution.** $\sin 60° \ne 0.866$ when the question asks for *exact*. Write $\dfrac{\sqrt 3}{2}$.
2. **Confusing $\sin 30°$ and $\sin 60°$.** $\sin 30° = \tfrac{1}{2}$ (small angle, small sine). $\sin 60° = \dfrac{\sqrt 3}{2} \approx 0.866$ (bigger). The smaller-angle has the smaller sine.
3. **$\tan 90°$ as "infinity."** Write *undefined*. (Beyond 0580: $\lim_{\theta \to 90°^-} \tan\theta = +\infty$, but that's a limit statement, not the value at $90°$.)
4. **Forgetting to rationalise.** $\tan 30° = \dfrac{1}{\sqrt 3}$ should be written $\dfrac{\sqrt 3}{3}$ in formal answers — the standard convention is "no surd in the denominator."
5. **Wrong sign at $180°, 270°$, etc.** $\cos 180° = -1$ (not $1$); $\sin 270° = -1$ (not $1$). Use the unit circle to read off the sign.

---

## Exam Notes

### Cambridge 0580 / 0606

**Syllabus refs:** 0580 E6.3 (knowledge of exact trigonometric values), 0606 §10.4 (uses these inside trig identities and equations). Standard exam patterns:

- "Without using a calculator, find the exact value of $\sin 30° + \cos 60°$." ($\tfrac{1}{2} + \tfrac{1}{2} = 1$.)
- "An equilateral triangle has side $a$. Show that its area is $\tfrac{\sqrt 3}{4} a^2$." (Use $\sin 60° = \tfrac{\sqrt 3}{2}$.)
- "A right triangle has angles $30°$, $60°$, $90°$ and hypotenuse $h$. Find the exact lengths of the other two sides." ($h \sin 30° = h/2$ and $h \cos 30° = \tfrac{h\sqrt 3}{2}$.)

> [!tip] On 0580/0606 calculator papers, the question still might say "exact"
> Even on calculator-allowed papers, "exact value" or "in surd form" overrides the calculator. Don't use the calculator's decimal output for $\sin 60°$ — use the table value.

### A-Level / IB / AP

A-Level extends to:
- **Radians:** $\sin\dfrac{\pi}{6} = \tfrac{1}{2}$, $\sin\dfrac{\pi}{4} = \dfrac{\sqrt 2}{2}$, etc. The exact values are the *same numbers*; only the angle measure changes.
- **All four quadrants:** $\sin 150° = \tfrac{1}{2}$, $\cos 150° = -\dfrac{\sqrt 3}{2}$ (using $150° = 180° - 30°$ and the symmetry of the unit circle). The reference-triangle technique extends throughout the unit circle via signs and quadrant analysis (CAST diagram — see [[Trigonometric Equations]]).
- **Half-angle / double-angle formulas:** the $15°, 75°$ values come from $30°/2$ via half-angle.
- **Inverse trig values:** $\arcsin\tfrac{1}{2} = 30°$ (or $\dfrac{\pi}{6}$). The table works backwards too.

---

## Connections

- **Prerequisite:** [[Trigonometric Ratios]] — SOH-CAH-TOA gives the connection between angle and side ratios
- **Prerequisite:** [[Pythagoras Theorem]] — used in deriving the $\sqrt 3$ in the 30-60-90 and the $\sqrt 2$ in the 45-45-90
- **Prerequisite:** [[Surds]] — exact-form trig values are surd expressions
- **Sibling:** [[Trigonometric Functions]] — the unit-circle origin generalises this to all angles
- **Forward:** [[Trigonometric Equations]] — solving $\sin\theta = \tfrac{1}{2}$ uses these values directly
- **Forward:** [[Trigonometric Identities]] — $\sin^2 + \cos^2 = 1$ verified at every special angle

---

## LaTeX Reference

| Value | LaTeX | Notes |
|---|---|---|
| $\dfrac{\sqrt 3}{2}$ | `\dfrac{\sqrt 3}{2}` | $\sin 60°, \cos 30°$ |
| $\dfrac{\sqrt 2}{2}$ | `\dfrac{\sqrt 2}{2}` | $\sin 45°, \cos 45°$ (rationalised form) |
| $\dfrac{1}{\sqrt 2}$ | `\dfrac{1}{\sqrt 2}` | unrationalised form (= same value) |
| $\sqrt 3$ | `\sqrt 3` | $\tan 60°$ |
| $\dfrac{\sqrt 3}{3}$ | `\dfrac{\sqrt 3}{3}` | rationalised $\tan 30°$ |
