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

We can derive all of these from **two reference triangles** (the $30$–$60$–$90$ and the $45$–$45$–$90$) plus the unit-circle definitions for $0°, 90°, 180°$.

### 中文锚点

把一张正方形纸沿对角线折一下，两条直角边一样长，折痕则是边长的根号二倍。计算器显示1.414……，可纸上的几何关系并没有变成“大概如此”。看那个45度的角，边长与折痕长度之比就是准确的 $1/\sqrt{2}$。三角函数的特殊值，留住的就是这种由形状确定的关系；小数可以方便测量，根号则让我们不用提前把它截短。

---

## Why "Exact"?

A decimal like $0.5$ *is* exactly equal to $\dfrac{1}{2}$ — no precision lost. But $0.866$ is *not* exactly $\dfrac{\sqrt 3}{2}$; it's a 3-decimal approximation, and using it propagates a small error through the rest of the calculation.

When the answer is meant to be exact (e.g., "Show that the area is $9\sqrt 3$"), substituting rounded decimal trig values loses the exact equality needed for the proof. Cambridge 0580/0606 use the word "**exact**" specifically to signal "leave surds and fractions as they are."

> [!tip] When to use exact, when to use decimal
> - "Find the **exact** value" / "Show that $\ldots = \dfrac{\sqrt 3}{2}$" / "Give your answer in **surd form**" → use the table; *no* calculator-decimal substitution.
> - "Calculate the angle correct to 1 decimal place" → calculator. Exact values aren't required.
>
> An exact-answer instruction selects exact arithmetic: use the triangle or unit-circle values and keep fractions and surds through the working.

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

**Construction.** Start with a unit square (side $1$). Cut along one diagonal. The diagonal has length $\sqrt{1^2 + 1^2} = \sqrt 2$ (Pythagoras), and the two halves are isosceles right triangles with two $45°$ angles.

![[exact-trig-45-45-90.svg]]

Each half-triangle has:
- Two equal legs of length $1$
- Hypotenuse $\sqrt 2$
- Angles $45°, 45°, 90°$

**Reading off trig values.** With the angle at the $45°$ corner:
$$\sin 45° = \cos 45° = \frac{1}{\sqrt 2} = \frac{\sqrt 2}{2}, \quad \tan 45° = \frac{1}{1} = 1.$$

Both legs are equal, so $\sin 45° = \cos 45°$ — the symmetry of the square is what enforces this.

> [!info] Rationalising $\dfrac{1}{\sqrt 2}$
> $\dfrac{1}{\sqrt 2}$ and $\dfrac{\sqrt 2}{2}$ are the same value — the *rationalised* form $\dfrac{\sqrt 2}{2}$ has no surd in the denominator. Use the form requested by the question; rationalising changes presentation, not exactness. To convert: multiply numerator and denominator by $\sqrt 2$. See [[Surds]] for the rationalisation rule.

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

> [!warning] $\tan 90°$ is undefined
> $\tan\theta = \sin\theta / \cos\theta$, and $\cos 90° = 0$. The bare expression $\dfrac{1}{0}$ has no value (see [[Reciprocals (Vocab)]]).
> - The "$\tan 90° = \infty$" claim comes from a *different* question: not "what is $\tan 90°$?" but "what does $\tan\theta$ do as $\theta$ approaches $90°$?" That's a **limit**, and like all limits the answer depends on which side: $\tan\theta \to +\infty$ as $\theta \to 90°^-$, but $\tan\theta \to -\infty$ as $\theta \to 90°^+$. Same approach to $90°$, *opposite* limits — because the function is doing different things on the two sides.
> - **Keep the two questions separate:** the function is undefined at $90°$. A one-sided limit describes nearby values and does not assign a value there.
> - In an exam: write "undefined" or "$\tan 90°$ does not exist." Never write "$\tan 90° = \infty$" — that's a limit statement masquerading as an equation.

---

## The "$\dfrac{\sqrt n}{2}$" Memory Trick

A pattern that simplifies memorising the sine row:

| $\theta$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ |
|---|---|---|---|---|---|
| $\sin\theta$ | $\dfrac{\sqrt 0}{2}$ | $\dfrac{\sqrt 1}{2}$ | $\dfrac{\sqrt 2}{2}$ | $\dfrac{\sqrt 3}{2}$ | $\dfrac{\sqrt 4}{2}$ |
| simplified | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt 2}{2}$ | $\dfrac{\sqrt 3}{2}$ | $1$ |

The triangle and circle derivations are the reason these values hold; this pattern is only a recall aid. If it becomes ambiguous, return to the geometry.

So $\sin$ at the five common angles is $\dfrac{\sqrt n}{2}$ for $n = 0, 1, 2, 3, 4$ in order.

**Cosine row is the *reverse*:** $\cos\theta = \sin(90° - \theta)$, so $\cos$ runs $1, \dfrac{\sqrt 3}{2}, \dfrac{\sqrt 2}{2}, \dfrac{1}{2}, 0$ — the same sequence backwards.

> [!tip] Co-function identity in disguise
> $\sin\theta = \cos(90° - \theta)$ and $\cos\theta = \sin(90° - \theta)$ — that's the *co* in *co*sine ("complementary sine"). The $\sin$ and $\cos$ rows of the table are mirror images for this reason. If you know one row, you immediately know the other.

---

## Worked Examples

### Example 1 — exact area

> Find the exact area of an equilateral triangle with side length $6$ cm.

**Trigger:** an equilateral triangle supplies a $60°$ angle and a known side. **Tool: sine in the right triangle** formed by dropping a perpendicular. The height has length $6 \cdot \sin 60° = 6 \cdot \dfrac{\sqrt 3}{2} = 3\sqrt 3$ cm. **Tool: triangle area, $A=\tfrac12 bh$.** Hence $A = \tfrac{1}{2}(6)(3\sqrt 3) = 9\sqrt 3$ cm².

(Alternatively, the formula $A = \tfrac{\sqrt 3}{4} s^2$ gives the same result for any equilateral triangle.)

### Example 2 — finding a side using exact trig

> A right triangle has hypotenuse $10$ cm and one of its acute angles is $30°$. Find the *exact* lengths of the other two sides.

**Trigger:** the hypotenuse and a special angle are known. **Tool: sine = opposite/hypotenuse.** Side opposite $30°$: $10 \sin 30° = 10 \cdot \tfrac{1}{2} = 5$ cm.
**Tool: cosine = adjacent/hypotenuse.** Side adjacent to $30°$: $10 \cos 30° = 10 \cdot \dfrac{\sqrt 3}{2} = 5\sqrt 3$ cm.

### Example 3 — exact value of a trig combination

> Find the exact value of $2\sin 60° \cos 30°$.

**Trigger:** both factors have known exact values. **Tool: direct substitution and multiplication of surds.**

$2 \cdot \dfrac{\sqrt 3}{2} \cdot \dfrac{\sqrt 3}{2} = 2 \cdot \dfrac{3}{4} = \dfrac{3}{2}$.

**Why not the double-angle formula?** $\sin(2\theta)=2\sin\theta\cos\theta$ needs the *same* angle in both factors. Here they are $60°$ and $30°$, so that pattern does not apply. Using $\cos30°=\sin60°$, a valid check is $2(\sin60°)^2=2(3/4)=3/2$.

---

## Common Mistakes

1. **Decimal substitution.** A rounded decimal such as $0.866$ is only an approximation to $\sin60°$. Write $\dfrac{\sqrt 3}{2}$.
2. **Confusing $\sin 30°$ and $\sin 60°$.** $\sin 30° = \tfrac{1}{2}$ (small angle, small sine). $\sin 60° = \dfrac{\sqrt 3}{2} \approx 0.866$ (bigger). This ordering holds for acute angles; sine is not increasing over all angles.
3. **$\tan 90°$ as "infinity."** Write *undefined*. (Beyond 0580: $\lim_{\theta \to 90°^-} \tan\theta = +\infty$, but that's a limit statement, not the value at $90°$.)
4. **Confusing a requested form with exactness.** $\tan30°=1/\sqrt3=\sqrt3/3$; both are exact. Rationalise when required by the question, and simplify without rounding.
5. **Wrong sign at $180°, 270°$, etc.** $\cos 180° = -1$ (not $1$); $\sin 270° = -1$ (not $1$). Use the unit circle to read off the sign.

---

## Exam Notes

### Cambridge 0580 — Extended E6.3

The 2025–2027 syllabus requires exact sine and cosine values at $0°,30°,45°,60°,90°$, and tangent at $0°,30°,45°,60°$. **C6.3 is Extended-only content**, so do not assign this recall list to Core. The table’s $180°$ values and unit-circle extensions support E6.4; they go beyond the literal E6.3 list. Paper 2 is non-calculator and Paper 4 allows a calculator; an exact-answer instruction still requires exact arithmetic on either.

### Cambridge 0606 — §10.1, §10.4–10.5 and assumed 0580 knowledge

The 2025–2027 syllabus assumes 0580 (or equivalent) subject knowledge. §10.1 covers all six trigonometric functions; §10.4 covers identities and §10.5 equations on a specified domain. **§10.4 is not an exact-value recall row.** Use the values inside identities and equations, converting degrees/radians as needed. Paper 1 is non-calculator; Paper 2 allows a calculator. The syllabus’s exact-answer guidance permits surds and constants rather than rounded decimal substitutes.

### Cambridge 9709 and 9231

**9709 Pure Mathematics 1 §1.5** explicitly requires exact sine, cosine and tangent values at $30°,45°,60°$ and related angles, in either angle unit. Unit-circle symmetry determines signs. Subsequent Pure Mathematics uses this knowledge in equations, identities and calculus.

**9231** assumes the relevant 9709 mathematics; the elementary table is prerequisite knowledge, not a separate Further Mathematics topic. Compound angles, complex numbers and other extensions can generate additional exact values.

### Edexcel IAL and OxfordAQA 9660

**Edexcel IAL P1 §3.3** covers sine, cosine and tangent functions, their graphs, symmetries and periodicity; **P2 §6.2** solves trigonometric equations in specified intervals. The exact table is supporting fluency for those tasks, not a separately enumerated recall list in those rows.

**OxfordAQA 9660 PP1.2** likewise covers the functions, identities and interval-restricted equations in degrees/radians. Use exact values when applicable; do not import Cambridge’s numbered recall list as an OxfordAQA quotation.

### IB Mathematics — AA and AI differ

**Analysis and Approaches, SL 3.5** (also required at HL) explicitly includes exact ratios at $0,\pi/6,\pi/4,\pi/3,\pi/2$ and their multiples, alongside the unit circle. This is not HL-only. [IB AA guide, first assessment 2021, p. 46](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf)

**Applications and Interpretation, AHL 3.8** explicitly excludes assessment of knowledge of exact trigonometric values, while noting their value for understanding. Do not transfer AA’s recall requirement to AI. [IB AI guide, first assessment 2021, p. 45](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-applications-interpretation-guide.pdf)

### AP Calculus AB/BC

The Course and Exam Description’s **Prerequisites** explicitly expects unit-circle definitions and trigonometric values at $0,\pi/6,\pi/4,\pi/3,\pi/2$ and their multiples. They support exact evaluation in calculus; the table is not a separate calculus unit. “AP” here means AB/BC, not every AP course.

### Where the standalone recall requirement does not apply

**0580 Core and IB AI** do not carry this requirement as above. **OxfordAQA 9260 G19–G20** covers right-triangle ratios and, at Extension, the sine/cosine rules and triangle area; it does not enumerate an exact-angle recall table. Exact answers can still be requested, and the geometry remains useful. **9231** inherits the skill through 9709 rather than adding a new recall topic.

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
