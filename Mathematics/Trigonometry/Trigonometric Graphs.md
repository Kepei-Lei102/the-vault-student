---
chinese: 三角函数图像 (sānjiǎo hánshù túxiàng)
prerequisites:
  - "[[Trigonometric Functions]]"
  - "[[Radians]]"
  - "[[Graphs of Functions]]"
leads_to:
  - "[[Trigonometric Equations]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-10-2
  - syllabus/0606-10-3
  - syllabus/9260-A12
  - type/deep
  - type/visualization
  - notation/amplitude
  - notation/period
  - misconception/period-formula-direction
  - misconception/tan-amplitude
---

# Trigonometric Graphs 三角函数图像

## Definition

A **trigonometric graph** is the plot of a function like $y = a\sin(bx) + c$, $y = a\cos(bx) + c$, or $y = a\tan(bx) + c$ — a *transformed* version of one of the three parent graphs $y = \sin x$, $y = \cos x$, $y = \tan x$.

This card teaches you to:
- **Sketch** a trig graph from its equation (forward problem)
- **Identify** the equation from a sketch (reverse problem)
- **Recognize** the three transformations — *amplitude*, *period*, *vertical shift* — that the parameters $a$, $b$, $c$ control

The skill matters because trig functions model every periodic phenomenon — oscillation, waves, AC current, planetary motion, daylight hours through the year. Reading and writing their graphs is reading and writing the language of periodicity.

### 中文锚点

三角函数图像 = $y = a\sin(bx) + c$ 等等的图像，在三个"母函数" $\sin x, \cos x, \tan x$ 上做三种变换：

- **振幅 (amplitude)** $a$：纵向拉伸 — 控制曲线的"高度"
- **周期 (period)** $b$：横向压缩 — 周期 $T = \dfrac{2\pi}{b}$（sin/cos）或 $\dfrac{\pi}{b}$（tan）
- **垂直平移 (vertical shift)** $c$：上下整体移动

考试两个方向：（1）给方程画图（forward），（2）给图找方程（reverse）。两边都要会。

---

## The Three Parent Graphs

Before learning transformations, anchor the parent graphs cold.

![[trig-graphs-parents.svg]]

| Function | Domain | Range | Period | Key features |
|---|---|---|---|---|
| $y = \sin x$ | all real $x$ | $[-1, 1]$ | $2\pi$ | passes through origin; first max at $x = \pi/2$ |
| $y = \cos x$ | all real $x$ | $[-1, 1]$ | $2\pi$ | starts at maximum $(0, 1)$; *cosine is sine shifted left by $\pi/2$* |
| $y = \tan x$ | $x \neq \frac{\pi}{2} + n\pi$ | all real | $\pi$ | passes through origin; **vertical asymptotes** at $x = \pi/2, 3\pi/2, \dots$ |

**Sin and cos look like waves; tan looks like a stack of slanted strips with vertical asymptotes between them.** That distinction matters — tan's transformations behave differently because of the asymptotes.

> [!tip] Why $\cos$ is just $\sin$ shifted
> $\cos x = \sin(x + \pi/2)$ — see the co-function identity in [[Trigonometric Identities]]. Geometrically, the cosine of the angle is the sine of the *complement*. So everything you can do to $\sin$ you can do to $\cos$ by replacing $x$ with $x + \pi/2$. Many "is this graph $\sin$ or $\cos$?" questions reduce to "where does the curve start?" — at $0$ → sin; at the maximum → cos.

---

## The Three Transformations

For $y = a\sin(bx) + c$ (and analogously for $\cos$ and $\tan$), each parameter has a single, *separable* effect.

![[trig-graphs-transformations.svg]]

### Amplitude — $a$

The **amplitude** of $y = a\sin(bx) + c$ is $|a|$. It is *half* the vertical distance from the maximum to the minimum:

$$
\text{amplitude} = \frac{\text{max} - \text{min}}{2}.
$$

For $y = 3\sin x$: maximum $3$, minimum $-3$, amplitude $3$. The curve stretches vertically by a factor of $|a|$ — same shape, $|a|$ times taller. **Negative $a$ flips the curve upside-down**.

> [!warning] Tan has no amplitude
> $y = a\tan(bx)$ doesn't have an amplitude in the usual sense — tan goes to $\pm\infty$ at its asymptotes regardless of $a$. The parameter $a$ scales tan's *steepness* (how fast it climbs toward the asymptote) but doesn't bound it. Amplitude is a sin/cos concept; for tan, $a$ is just a "vertical stretch factor" with no clean name.

### Period — $b$

The **period** is the horizontal distance over which the graph completes one full cycle before repeating. For $y = a\sin(bx) + c$:

$$
\text{period} = \frac{2\pi}{|b|}, \qquad \text{(for sin and cos)}.
$$

For tan, the parent period is already $\pi$, so:

$$
\text{period} = \frac{\pi}{|b|}, \qquad \text{(for tan)}.
$$

**Larger $b$ means shorter period**: $y = \sin(2x)$ completes a full cycle in $\pi$, *half* of $\sin x$'s $2\pi$. The graph is *horizontally compressed* by factor $b$. A useful sanity check: count cycles. $\sin(2x)$ on $[0, 2\pi]$ should show **two** complete sine waves — twice as many as $\sin x$.

> [!tip] Period formula direction trap
> Students sometimes write *period = $b/2\pi$* (inverted). The correct formula is **$2\pi/b$** for sin/cos. Sanity check: $b = 1$ should give the parent-graph period $2\pi$, not $1/(2\pi)$. The bigger $b$, the *more* compressed the graph, so the *shorter* the period — bigger $b$ → smaller period — division goes that way.

### Vertical shift — $c$

The **midline** (the horizontal line through the centre of the wave, where $\sin$ would be zero) is shifted up by $c$. The maximum becomes $|a| + c$ and the minimum becomes $-|a| + c$.

For $y = \sin x + 2$: midline $y = 2$, max $3$, min $1$. Same wave, just lifted up by $2$. **Negative $c$ shifts down.**

The midline is often the easiest feature to identify when reading a graph backwards: $c = (\text{max} + \text{min})/2$.

---

## Combining the Three — Worked Example

**Sketch $y = 3\sin(2x) - 1$ on $0 \le x \le 2\pi$.**

Identify the parameters:
- $a = 3$ → amplitude $3$
- $b = 2$ → period $\dfrac{2\pi}{2} = \pi$
- $c = -1$ → midline $y = -1$, max $3 - 1 = 2$, min $-3 - 1 = -4$

So the graph oscillates between $y = 2$ and $y = -4$, completing two full cycles on $[0, 2\pi]$ (period $\pi$ × 2 = $2\pi$).

![[trig-graphs-worked-example.svg]]

**Step-by-step sketching procedure:**

1. **Draw the midline** $y = c$ as a dashed horizontal reference.
2. **Mark max and min** $y = c + |a|$ and $y = c - |a|$ as horizontal dotted bounds.
3. **Mark $x$-intercepts of the parent on the new period.** For $\sin(2x)$, zeros are at $x = 0, \pi/2, \pi, 3\pi/2, 2\pi$ — every quarter-period.
4. **Sketch the wave** between the bounds, passing through the midline at the marked $x$'s, peaking at quarter-periods.

The two-cycle visual is the sanity check that you've handled the period correctly.

---

## Reverse Problem — Finding the Equation from a Graph

Given a sin/cos graph, recover $a$, $b$, $c$ in this order:

1. **Find $c$** — the midline $y$-value. Use $c = (\max + \min)/2$.
2. **Find $a$** — the amplitude. Use $a = (\max - \min)/2$. (Sign of $a$: positive if the graph rises from the midline at $x = 0$ for sin, or starts at maximum for cos; negative if reflected.)
3. **Find $b$** — the period $T$. Then $b = 2\pi/T$ (sin/cos) or $\pi/T$ (tan). Read $T$ off the graph as the $x$-distance between two consecutive maxima (or minima, or rising-zero crossings).
4. **Choose between sin and cos** by where $y = c$ vs $y = c + a$ at $x = 0$:
   - Graph passes through midline rising at $x = 0$ → use $\sin$
   - Graph at maximum at $x = 0$ → use $\cos$
   - Graph at minimum at $x = 0$ → use $-\cos$
   - Graph passes through midline falling at $x = 0$ → use $-\sin$

(In A-Level / IB / AP, *phase shift* lets you write any sinusoid as $a\sin(b(x - h)) + c$ for some $h$, so the choice of sin vs cos becomes a choice of $h$. 0606 doesn't have phase shift, so you pick the parent that matches at $x = 0$.)

**Example.** A graph oscillates between $y = 5$ and $y = -1$, completing one cycle every $\pi/2$ units of $x$, and passes through the midline rising at $x = 0$. Find the equation.

- $c = (5 + (-1))/2 = 2$
- $a = (5 - (-1))/2 = 3$
- $T = \pi/2$, so $b = 2\pi / T = 4$
- Rising through midline at $x = 0$ → sin

$\boxed{y = 3\sin(4x) + 2}$. ✓

---

## Tan and Its Asymptotes

The tangent transformation $y = a\tan(bx) + c$ behaves differently because:

- **No amplitude.** $a$ scales steepness, not max/min (those don't exist).
- **Period $\pi/b$**, not $2\pi/b$.
- **Asymptotes at $x = \dfrac{\pi/2 + n\pi}{b}$.** Smaller $b$ → asymptotes spread out; larger $b$ → asymptotes squeezed together.
- **Vertical shift $c$** moves the *zeros* (where the graph crosses its centre) but not the asymptote positions.

For example, $y = \tan(2x)$ has asymptotes at $x = \pi/4, 3\pi/4, 5\pi/4, \dots$ — half the spacing of the parent. Sketching tan starts with **plotting the asymptotes first** (vertical dashed lines), then drawing the rising branches between them.

---

## Common Mistakes

1. **Amplitude formula direction.** Amplitude is $(\max - \min)/2$, not $(\max - \min)$. The full vertical span of the wave is *twice* the amplitude.
2. **Period formula inverted.** $T = 2\pi/b$ for sin/cos, not $b/(2\pi)$. Bigger $b$ → shorter period.
3. **Calling the period of $\tan$ as $2\pi$.** Tan's period is **$\pi$**, half that of sin/cos. So $\tan(bx)$ has period $\pi/b$, not $2\pi/b$.
4. **Forgetting to count cycles.** $y = \sin(3x)$ on $[0, 2\pi]$ should show **three** complete sine waves. If your sketch shows one (or six), $b$ is wrong.
5. **Confusing amplitude with vertical shift.** Both are vertical things, but: amplitude controls *how tall* the wave is, vertical shift controls *where the wave's centre sits*. A wave from $y = -3$ to $y = 5$ has amplitude $4$ and vertical shift $1$, *not* amplitude $5$ or vertical shift $4$.
6. **Treating tan like sin/cos for amplitude.** $a$ in $y = a\tan(bx)$ doesn't give a "max" — tan never has a max. Don't write "amplitude $= a$" for tan.
7. **Sketching tan without asymptotes.** Drawing the tan graph as a smooth curve through everywhere misses its defining feature. Always plot the asymptotes (dashed vertical lines) before sketching the curve.

---

## Exam Notes

### Cambridge 0606

**Syllabus refs:** §10.2 (relationship between related trig graphs; amplitude and period) and §10.3 (sketch and use $y = a\sin(bx) + c$, $y = a\cos(bx) + c$, $y = a\tan(bx) + c$). The Cambridge form is **without phase shift** — vertical shift only. Expect 4–6 mark questions covering:

- "Sketch $y = 2\cos(3x) + 1$ for $0° \le x \le 360°$, marking key features."
- "The graph shows $y = a\sin(bx) + c$. Find $a$, $b$, $c$."
- Combination with [[Trigonometric Equations]]: "Hence solve $a\sin(bx) + c = 0$ on the given domain" — read the $x$-intercepts off the sketch.

> [!tip] Cambridge degrees vs radians
> 0606 problems mix degrees and radians. The setup ($y = a\sin(bx) + c$, $-180° \le x \le 180°$) determines which to use. **In radians, $T = 2\pi/b$. In degrees, $T = 360°/b$.** The formula structure is identical; only the unit-of-a-full-cycle changes ($2\pi$ vs $360°$).

### A-Level / 9709

A-Level extends to **phase shift**: $y = a\sin(b(x - h)) + k$. The horizontal translation $h$ shifts the graph right by $h$ units (note: *inside* the function in the form $b(x - h)$, *outside* in the form $bx + c$ where $c = -bh$ and the shift is $-c/b$). The "inside-is-backwards" rule from [[Graphs of Functions]] applies.

### IB AA HL & AP Calculus

Same content as A-Level, plus *phase shift questions* are exam-standard. AP also tests trig graphs in the context of differentiation (where do max/min occur? what's $f'(x_0)$ on the graph?) and integration (signed area between the graph and $x$-axis).

---

## Connections

- **Prerequisite:** [[Trigonometric Functions]] — the unit-circle definition of $\sin, \cos, \tan$ that gives the parent graphs their shape
- **Prerequisite:** [[Radians]] — the natural unit for trig graphs in calculus contexts
- **Prerequisite:** [[Graphs of Functions]] — the general "$y = af(b(x-c))+d$" framework; this card is its trig instance
- **Sibling:** [[Trigonometric Identities]] — co-function identities explain why $\cos$ is just $\sin$ shifted; double-angle identities relate $\sin(2x)$ to $2\sin x\cos x$
- **Application:** [[Trigonometric Equations]] — graph–intersection interpretation of solving $a\sin(bx) + c = k$ (count the intersections of $y = a\sin(bx) + c$ with the horizontal $y = k$)
- **Application:** *physics* — simple harmonic motion is $x(t) = A\cos(\omega t + \phi)$; the parameters here are exactly amplitude, angular frequency, and phase
- **Application:** *AC circuits* — $V(t) = V_0\sin(\omega t)$ for sinusoidal voltage; the graph's peak is the *peak voltage* and the period is $2\pi/\omega$
- **Application:** *signal processing* — every periodic signal can be decomposed into sums of sinusoids (Fourier series); each sinusoid has its own amplitude, period, and phase
- **Bridge to physics:** *waves* — wavelength and frequency are spatial and temporal periods; the wave equation has solutions of the form $\sin(kx - \omega t)$, a sinusoid in two variables

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $y = a\sin(bx) + c$ | `y = a\sin(bx) + c` | Cambridge 0606 form |
| $y = a\sin(b(x-h)) + k$ | `y = a\sin(b(x-h)) + k` | A-Level / IB form with phase shift |
| $T = \dfrac{2\pi}{b}$ | `T = \dfrac{2\pi}{b}` | period of sin/cos |
| $T = \dfrac{\pi}{b}$ | `T = \dfrac{\pi}{b}` | period of tan |
| $\frac{\pi}{2} + n\pi$ | `\frac{\pi}{2} + n\pi` | tan asymptote locations |
| $|a|$ | `\lvert a \rvert` | amplitude (modulus to handle negative $a$) |
