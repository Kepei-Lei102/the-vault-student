---
chinese: 三角函数 (sānjiǎo hánshù)
prerequisites:
  - "[[Trigonometric Ratios]]"
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Function]]"
leads_to:
  - "[[Sine and Cosine Rules]]"
  - "[[Trigonometric Identities]]"
  - "[[Trigonometric Equations]]"
  - "[[Radians]]"
  - "[[Graph Transformations]]"
  - "[[Integration]]"
  - "[[Second-Order Differential Equations]]"
  - "[[Differentiation Rules]]"
  - "[[Simple Harmonic Motion]]"
  - "[[Squeeze Theorem]]"
  - "[[Trigonometric Graphs]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - level/IGCSE-extension
  - level/pre-AP
  - level/pre-IB
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0606
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9260-A12
  - syllabus/0606-10-1
  - syllabus/9709-1-5
  - syllabus/0580-E6-4
  - type/concept
  - notation/sin-cos-tan
  - notation/unit-circle
  - misconception/three-views-disconnect
---

# Trigonometric Functions 三角函数

## The Big Idea

Sine, cosine, and tangent start life as **ratios** inside a right-angled triangle (see [[Trigonometric Ratios]]). But ratios are limited — they only work for angles between $0°$ and $90°$. What happens at $0°$ exactly? At $150°$? At $-30°$? At $1000°$?

To answer these questions, mathematicians upgraded the ratios into **functions** — machines that accept *any* angle and return a number. This card shows the three ways to see the same function:

| View | What you see | Best for |
|------|-------------|----------|
| **Ratio** (triangle) | $\dfrac{\text{opp}}{\text{hyp}}$, $\dfrac{\text{adj}}{\text{hyp}}$, $\dfrac{\text{opp}}{\text{adj}}$ | Solving right-angled triangles |
| **Unit circle** (coordinate) | A point rotating on a circle of radius 1 | Understanding any angle, sign rules, identities |
| **Wave** (graph) | A periodic curve that repeats every $360°$ | Reading amplitude, period, phase; modelling oscillation |

These are **not** three different topics. They are **three windows into the same object**. Every property you discover in one view has a counterpart in the other two.

### 中文锚点

三角函数 = 三角比升级为函数。比值只在直角三角形中有效 ($0°$–$90°$)；函数对**任意角度**都有定义。理解三角函数的关键是三种视角——三角形、单位圆、波形——它们描述的是**同一个东西**。

---

## Where the Names Come From — A History of Beautiful Accidents

Every trig function is named after something you can literally **see** on the unit circle. The names are a mix of Sanskrit, Arabic, and Latin — with one famous mistranslation baked in forever.

### Sine 正弦 — a bowstring, mistranslated through three languages

The Sanskrit word **jyā** (ज्या) meant "bowstring" — and described the **half-chord** of a circle, exactly the line segment we now call sine. Indian astronomers (Aryabhata, ~500 CE) used this to compute planetary positions.

When Arab scholars translated the Sanskrit texts, they transliterated *jyā* as **jiba** (جيبا). But Arabic is normally written without vowels, so *jiba* looked like **jayb** (جيب) — a completely different word meaning "bay," "fold," or "pocket of a garment."

In the 12th century, Gerard of Cremona translated the Arabic into Latin. He saw *jayb* and translated it literally as **sinus** — Latin for "bay" or "fold of a toga." English inherited it as **sine**.

So our word for the most important ratio in mathematics is a **translation error preserved for 800 years**. The original meaning — a bowstring stretched across a circle — is actually a perfect description of what sine measures.

### Cosine 余弦 — the sine of the complement

**Co-sine** = *complementi sinus* = "sine of the **complementary** angle." Because $\cos\theta = \sin(90° - \theta)$: the cosine of an angle is the sine of its complement. The "co-" prefix means "of the complement."

This "co-" pattern repeats: **co**tangent = tangent of the complement, **co**secant = secant of the complement.

### Tangent 正切 — the line that touches

Latin *tangere* = "to touch." On the unit circle, $\tan\theta$ is literally the length of the segment along the **tangent line** that touches the circle at $(1, 0)$ — the line from the foot to where the extended radius hits it. You'll see this construction in the diagram below. The line *touches* the circle at one point; the name describes the geometry.

### Secant 正割 — the line that cuts

Latin *secare* = "to cut." On the same diagram, the **secant** is the line from the origin through $P$ that **cuts** across the circle and continues to the tangent line. The length from the origin to that intersection point is $\sec\theta = \dfrac{1}{\cos\theta}$. The line *cuts through* the circle; the name describes the geometry.

### Cotangent 余切 and Cosecant 余割

The "co-" versions. If you drew the tangent line at $(0, 1)$ (the top of the circle) instead of $(1, 0)$, and extended the radius to hit *that* line, you'd get **cotangent** and **cosecant**. They are literally the tangent and secant constructions for the complementary angle — hence "co-tangent" and "co-secant."

> [!tip] The naming system is coherent
> All six functions — sin, cos, tan, cot, sec, csc — are named after **geometric objects on the unit circle**: a half-chord (sine), a tangent line (tangent), and a cutting line (secant), plus their complements. The names aren't arbitrary. Every one tells you what to look for in the picture.

---

## View 1 — The Ratio (Triangle)

You already know this from [[Trigonometric Ratios]]:

$$\sin\theta = \dfrac{\text{opp}}{\text{hyp}}, \qquad \cos\theta = \dfrac{\text{adj}}{\text{hyp}}, \qquad \tan\theta = \dfrac{\text{opp}}{\text{adj}}$$

**Domain:** $0° < \theta < 90°$ only. The triangle simply does not exist at $\theta = 0°$ (it collapses to a line), at $\theta = 90°$ (no second acute angle), or beyond.

**What this view is good at:** Solving real-world problems — find a side, find an angle, elevation/depression. This is the exam workhorse.

**What this view cannot do:** Tell you what $\sin 150°$ is, or why $\cos(-30°) = \cos 30°$, or what the graph looks like.

To break past $90°$, we need a new definition that *agrees with the ratio when the angle is acute* but *extends to all angles*. Enter the unit circle.

---

## View 2 — The Unit Circle

### Construction

Draw a circle of **radius 1** centred at the origin. Place a point $P$ on the circle. Measure the angle $\theta$ **anticlockwise from the positive $x$-axis** to the radius $OP$.

Then **define**:

$$\cos\theta = \text{the } x\text{-coordinate of } P, \qquad \sin\theta = \text{the } y\text{-coordinate of } P$$

![[trig-unit-circle.svg|697]]

### WHY this agrees with the ratio

In the first quadrant ($0° < \theta < 90°$), drop a perpendicular from $P$ to the $x$-axis. You get a right triangle with hypotenuse $= 1$ (the radius), adjacent $= x$-coordinate, opposite $= y$-coordinate. So:
$$\cos\theta = \frac{\text{adj}}{1} = x, \qquad \sin\theta = \frac{\text{opp}}{1} = y$$
The unit-circle definition and the ratio definition give the **same answer** whenever both exist. But the circle keeps going — $P$ can rotate into quadrant II, III, IV, past $360°$, or backwards (negative angles). The coordinates always exist; therefore $\sin$ and $\cos$ are always defined.

### Signs by Quadrant — Just Read the Coordinates

There is no mnemonic to memorise. Just think about **where the point $P$ is**:

| Quadrant | Angle range | $x$-coordinate | $y$-coordinate | Therefore |
|----------|-------------|----------------|----------------|-----------|
| I | $0°$–$90°$ | $x > 0$ | $y > 0$ | $\cos > 0$, $\sin > 0$, $\tan > 0$ |
| II | $90°$–$180°$ | $x < 0$ | $y > 0$ | $\cos < 0$, $\sin > 0$, $\tan < 0$ |
| III | $180°$–$270°$ | $x < 0$ | $y < 0$ | $\cos < 0$, $\sin < 0$, $\tan > 0$ |
| IV | $270°$–$360°$ | $x > 0$ | $y < 0$ | $\cos > 0$, $\sin < 0$, $\tan < 0$ |

That's it. $\cos\theta = x$, so ask "is $x$ positive or negative?" $\sin\theta = y$, so ask "is $y$ positive or negative?" $\tan\theta = y/x$, so ask "do $x$ and $y$ have the same sign?" No mnemonics, no special rules — just coordinates.

### Key Angles from the Unit Circle

| $\theta$ | $P = (\cos\theta, \sin\theta)$ | Geometric picture |
|-----------|-------------------------------|-------------------|
| $0°$ | $(1, 0)$ | Right on the positive $x$-axis |
| $90°$ | $(0, 1)$ | Top of the circle |
| $180°$ | $(-1, 0)$ | Leftmost point |
| $270°$ | $(0, -1)$ | Bottom of the circle |
| $360°$ | $(1, 0)$ | Back where we started |

So $\sin 180° = 0$, $\cos 180° = -1$, $\tan 180° = 0/-1 = 0$ — results that "triangle trig" cannot produce.

### Finding All Solutions — The Ruler Method

Suppose you know $\sin\theta = \dfrac{1}{2}$ and you've found $\theta = 30°$. Are there other angles in $0° \leq \theta < 360°$ with the same sine?

**The method:** On the unit circle, $\sin\theta = y$. So place a horizontal ruler at $y = \dfrac{1}{2}$ and see where it crosses the circle. It crosses **twice** — once in quadrant I ($\theta = 30°$) and once in quadrant II. By symmetry across the $y$-axis, the second crossing is at $\theta = 180° - 30° = 150°$.

This works identically for cosine: $\cos\theta = x$, so place a **vertical** ruler at $x =$ your value and find where it hits the circle.

**For tangent:** $\tan$ has period $180°$, so if $\theta$ is one solution, $\theta + 180°$ is always the other. No ruler needed — just add $180°$.

> [!important] This replaces all "symmetry identity" rules
> You do not need to memorise $\sin(180° - \theta) = \sin\theta$ or $\cos(360° - \theta) = \cos\theta$ as separate formulas. Every one of these follows from the ruler: a horizontal line at height $y$ crosses the circle twice, and you can read off both angles from the geometry. If you understand the circle, the identities write themselves.

### Tangent on the Unit Circle

$\tan\theta = \dfrac{\sin\theta}{\cos\theta} = \dfrac{y}{x}$. Geometrically, $\tan\theta$ is the **slope of the radius** $OP$.

But there is a beautiful literal meaning of the word "tangent" (Latin *tangere* = "to touch"). Draw the **vertical tangent line** to the circle at the point $(1, 0)$. Extend the radius $OP$ until it hits this line at a point $T$. The length $FT$ — from the foot $F = (1,0)$ to $T$ — **is** $\tan\theta$.

![[trig-tangent-line.svg|697]]

**WHY.** The triangle $OFT$ is right-angled at $F$, with $OF = 1$ (the radius to $(1,0)$) and angle $\theta$ at $O$. So $\tan\theta = \dfrac{FT}{OF} = \dfrac{FT}{1} = FT$.

When $\theta = 90°$, the radius is vertical and never hits the tangent line — $\tan 90°$ is **undefined** (the line segment would need to be infinitely long).

---

## View 3 — The Wave (Graph)

### $y = \sin\theta$ and $y = \cos\theta$

As $\theta$ increases from $0°$ to $360°$, the $y$-coordinate of $P$ traces the **sine wave**, and the $x$-coordinate traces the **cosine wave**:

![[trig-waves-sin-cos.svg|697]]

Both curves have the same shape — the cosine graph **is** the sine graph slid $90°$ to the left: $\cos\theta = \sin(\theta + 90°)$. On the unit circle this is obvious: the $x$-coordinate at angle $\theta$ equals the $y$-coordinate at angle $\theta + 90°$.

### $y = \tan\theta$

Tangent is a fundamentally different shape — it has no amplitude (it goes to $\pm\infty$), has vertical **asymptotes** where $\cos\theta = 0$, and repeats every $180°$ instead of $360°$:

![[trig-wave-tan.svg|697]]

### Key Wave Vocabulary

| Term | 中文 | Meaning for $y = \sin\theta$ |
|------|------|------------------------------|
| **amplitude** | 振幅 (zhènfú) | Maximum displacement from the centre line. For $\sin\theta$: amplitude = $1$ |
| **period** | 周期 (zhōuqī) | Length of one complete cycle. For $\sin\theta$: period = $360°$ |
| **frequency** | 频率 (pínlǜ) | Number of cycles per unit. $= \dfrac{1}{\text{period}}$ |
| **phase shift** | 相移 (xiāngyí) | Horizontal translation of the wave |
| **vertical shift** | 纵移 (zòngyí) | Moving the centre line up or down |
| **asymptote** | 渐近线 (jiànjìn xiàn) | A line the curve approaches but never reaches (tangent has these) |

### Summary: Three Graphs Compared

| Function | Shape | Period | Amplitude | Range | Undefined at |
|----------|-------|--------|-----------|-------|-------------|
| $y = \sin\theta$ | Smooth wave | $360°$ | $1$ | $[-1, 1]$ | Never |
| $y = \cos\theta$ | Same wave, shifted $90°$ left | $360°$ | $1$ | $[-1, 1]$ | Never |
| $y = \tan\theta$ | Repeating S-curves | $180°$ | None (unbounded) | $(-\infty, \infty)$ | $90°, 270°, \ldots$ |

### Connecting the Circle to the Wave

Imagine "unrolling" the unit circle onto a number line:

1. Start at $\theta = 0°$. Point $P = (1, 0)$. Plot $y = \sin 0° = 0$.
2. Rotate to $\theta = 90°$. Point $P = (0, 1)$. Plot $y = \sin 90° = 1$.
3. Continue… $180°$ gives $y = 0$, $270°$ gives $y = -1$, $360°$ gives $y = 0$.

The $y$-coordinate of the rotating point, plotted against the angle, **is** the sine wave. The circle and the wave are the same motion — one shown as rotation, the other as oscillation.

---

## Transformations — the General Sine Function

### The formula

$$y = a\sin(b(\theta - c)) + d$$

| Parameter | Effect | Intuition |
|-----------|--------|-----------|
| $a$ | **Amplitude** $= \lvert a \rvert$. If $a < 0$, the wave flips vertically | Stretches the wave up/down |
| $b$ | **Period** $= \dfrac{360°}{\lvert b \rvert}$. Larger $b$ = faster oscillation | Compresses the wave left/right |
| $c$ | **Phase shift** $= c$ degrees right (positive $c$ shifts right) | Slides the wave sideways |
| $d$ | **Vertical shift**. Centre line moves to $y = d$ | Slides the wave up/down |

Amplitude, period, and vertical shift are intuitive — phase shift is not. Let's derive it.

### WHY the phase shift works

Start with $y = \sin\theta$. The sine wave has its first zero at $\theta = 0°$.

Now write $y = \sin(\theta - 30°)$. When does the "inside" equal zero? When $\theta - 30° = 0°$, i.e. $\theta = 30°$.

So the first zero has **moved from $0°$ to $30°$** — the whole wave slid $30°$ to the right. The wave "waits" an extra $30°$ before starting its cycle, because the input to sine is "delayed" by $30°$.

In general: $y = \sin(\theta - c)$ shifts the wave **$c$ units right** (positive $c$). $y = \sin(\theta + c)$ shifts it **$c$ units left** (negative $c$). The shift is always the **opposite sign** of what's inside the brackets.

**Derivation from the general form.** Given $y = a\sin(b\theta + k) + d$, factor: $y = a\sin\!\left(b\!\left(\theta + \dfrac{k}{b}\right)\right) + d$. The phase shift is $-\dfrac{k}{b}$ (rightward).

![[trig-transform-example.svg|697]]

### Order of Transformations Matters

Consider $y = \sin(2\theta - 60°)$. There are two ways to read this:

**Correct reading:** Factor first. $y = \sin(2(\theta - 30°))$. This means: compress horizontally by factor $2$ (period $= 180°$), **then** shift $30°$ right. The first zero is at $\theta = 30°$.

**Wrong reading:** "Shift $60°$ right, then compress by $2$." This would give $y = \sin(2(\theta - 60°)) = \sin(2\theta - 120°)$ — a completely different function. Its first zero is at $\theta = 60°$.

The difference is $30°$ — enough to cost you every mark on a graph question. **Always factor out the $b$ first**, then read the shift.

![[trig-order-matters.svg|697]]

> [!warning] The factoring rule
> $$y = a\sin(b\theta + k) + d \implies \text{factor as } y = a\sin\!\left(b\!\left(\theta - \left(-\dfrac{k}{b}\right)\right)\right) + d$$
> Phase shift $= -\dfrac{k}{b}$. Period $= \dfrac{360°}{|b|}$. Amplitude $= |a|$. Centre line $y = d$.

> [!tip] The same lesson appears in matrix transformations
> In [[Matrix Transformations]], you learn that matrix multiplication is not commutative: $AB \neq BA$. A rotation followed by a reflection is not the same as a reflection followed by a rotation. The underlying principle is identical: **the order of transformations matters** whenever the operations don't commute. Stretching then shifting gives a different result from shifting then stretching — whether you're transforming waves or transforming geometric shapes.

---

## The Reciprocal Functions

Three more trig functions arise by flipping the three ratios. Their names — secant ("the cutter"), cosecant ("the complement's cutter"), cotangent ("the complement's toucher") — all refer to line segments on the unit circle, as explained in the etymology section above.

$$\sec\theta = \dfrac{1}{\cos\theta} \quad \text{(secant 正割)}, \qquad \csc\theta = \dfrac{1}{\sin\theta} \quad \text{(cosecant 余割)}, \qquad \cot\theta = \dfrac{\cos\theta}{\sin\theta} \quad \text{(cotangent 余切)}$$

Each is undefined where its denominator is zero: $\sec$ at $90°, 270°, \ldots$; $\csc$ at $0°, 180°, \ldots$; $\cot$ at $0°, 180°, \ldots$.

### Two more Pythagorean identities

Start from $\sin^2\theta + \cos^2\theta = 1$ (proved in [[Trigonometric Ratios]]):

- **Divide by $\cos^2\theta$:** $\tan^2\theta + 1 = \sec^2\theta$
- **Divide by $\sin^2\theta$:** $1 + \cot^2\theta = \csc^2\theta$

These three identities are the foundation of all trig identity work at 0606 / A-Level / IB.

---

## Worked Examples

### Example 1 — Reading the unit circle

Find $\sin 210°$ and $\cos 210°$ exactly, without a calculator.

$210° = 180° + 30°$. On the circle, $P$ is in **quadrant III** — both $x$ and $y$ are negative. The angle past the negative $x$-axis is $30°$, so the coordinates have the same magnitude as $30°$ but both flipped:
$$\sin 210° = -\sin 30° = -\dfrac{1}{2}, \qquad \cos 210° = -\cos 30° = -\dfrac{\sqrt{3}}{2}$$

### Example 2 — The ruler method

Find all values of $\theta$ in $0° \leq \theta < 360°$ such that $\cos\theta = -\dfrac{\sqrt{3}}{2}$.

$\cos\theta = x$, so place a vertical ruler at $x = -\dfrac{\sqrt{3}}{2}$. This is in the left half-plane. The reference angle where $\cos = \dfrac{\sqrt{3}}{2}$ is $30°$. The ruler hits the circle at two points:
- Quadrant II: $\theta = 180° - 30° = 150°$
- Quadrant III: $\theta = 180° + 30° = 210°$

### Example 3 — Negative angle

Find $\cos(-120°)$ exactly.

$-120°$ means clockwise $120°$ from the positive $x$-axis. On the unit circle, $P$ lands in the same position as $240°$. The $x$-coordinate at $240°$: reference angle $60°$, quadrant III, $x < 0$:
$$\cos(-120°) = -\cos 60° = -\dfrac{1}{2}$$

Alternatively: rotating clockwise by $120°$ and anticlockwise by $120°$ both give the **same $x$-coordinate** (reflect across the $x$-axis, $x$ doesn't change). So $\cos(-120°) = \cos(120°) = -\cos 60° = -\dfrac{1}{2}$.

### Example 4 — Sketching a transformed wave

Sketch $y = 3\sin(2\theta) + 1$ for $0° \leq \theta \leq 360°$.

- Amplitude $= 3$ (wave goes from $1 - 3 = -2$ to $1 + 3 = 4$)
- Period $= \dfrac{360°}{2} = 180°$ (two full cycles in $0°$–$360°$)
- Vertical shift $= 1$ (centre line at $y = 1$)
- No phase shift

Key points for the first cycle: $(0°, 1)$, $(45°, 4)$, $(90°, 1)$, $(135°, -2)$, $(180°, 1)$. Second cycle repeats.

### Example 5 — Phase shift with factoring

Sketch $y = \sin(2\theta - 60°)$.

**Factor:** $y = \sin(2(\theta - 30°))$. Period $= 180°$. Phase shift $= 30°$ right. Amplitude $= 1$.

First zero at $\theta = 30°$. Peak at $\theta = 30° + 45° = 75°$. Next zero at $\theta = 30° + 90° = 120°$. Trough at $\theta = 165°$. Back to zero at $\theta = 210°$.

If you had wrongly read the $60°$ directly as the shift, you'd plot the first zero at $60°$ — off by $30°$, and every subsequent point wrong.

### Example 6 — Which quadrant?

Given $\sin\theta = -0.6$ and $\cos\theta > 0$, state which quadrant $\theta$ is in.

$\sin < 0$ means $y < 0$: below the $x$-axis, so quadrant III or IV. $\cos > 0$ means $x > 0$: right of the $y$-axis, so quadrant I or IV. The intersection is **quadrant IV**.

---

## Common Mistakes

1. **Measuring the angle from the wrong axis.** The unit-circle angle is measured from the **positive $x$-axis**, anticlockwise. Not from the $y$-axis, not clockwise (unless negative).
2. **Forgetting that reference angles are always acute.** The reference angle for $210°$ is $30°$, not $210°$. It's the acute angle between the radius and the nearest $x$-axis arm.
3. **Period formula confusion.** Period $= \dfrac{360°}{b}$, not $360° \times b$. Larger $b$ makes the wave **faster** (shorter period), not slower.
4. **Reading amplitude from the graph wrong.** Amplitude is measured from the **centre line** to the peak, not from trough to peak. Trough-to-peak is $2a$, not $a$.
5. **Not factoring before reading phase shift.** In $y = \sin(2\theta - 60°)$, the phase shift is $30°$ right, not $60°$ right. Factor out the $b$ first.
6. **Treating $\tan$ like $\sin$ and $\cos$.** Tangent has period $180°$, no amplitude (it goes to $\pm\infty$), and vertical asymptotes. It's a fundamentally different shape.

---

## Exam Notes

### OxAQA 9260

**Syllabus ref:** G19 (Extension). The 9260 spec asks for exact values and right-triangle applications primarily. The unit-circle view appears implicitly when students must find obtuse-angle solutions (e.g. "Given $\sin\theta = 0.5$, find all values of $\theta$ in $0° \leq \theta \leq 360°$" — this requires knowing the ruler method to get both $\theta = 30°$ and $\theta = 150°$).

### Cambridge 0606 (Additional Mathematics)

**Syllabus ref:** 10.1 — *know and use the six trigonometric functions of angles of any magnitude*, naming all six explicitly (sine, cosine, tangent, secant, cosecant, cotangent). This is where the unit circle, reciprocal functions, and graph views become **examinable core content**. The spec explicitly requires: "amplitude, period and phase for $y = a\sin(bx) + c$", sketching and recognising transformed trig graphs, and solving trig equations using the general solution. The reciprocal functions $\sec$, $\csc$, $\cot$ and all three Pythagorean identities are examined.

### A-Level / IB Mathematics / AP Precalculus

All three curricula teach the unit circle in the first trig unit and assess graph transformations heavily. Radians replace degrees as the standard angle unit (see [[Radians]]). The reciprocal functions, identities, and trig equation solving are core A-Level/IB content — not "beyond syllabus" but the expected standard.

---

## Beyond the Syllabus

### Simple Harmonic Motion — the Sine Wave Runs Physics

The sine wave is the unique function satisfying $\dfrac{d^2y}{d\theta^2} = -y$ — acceleration proportional and opposite to displacement. This is the equation of **simple harmonic motion**, the single most important differential equation in physics. Every pendulum, every vibrating string, every photon obeys it. This is a university-level topic (differential equations), but the setup — "the wave that accelerates back toward zero" — is exactly what you see in the sine graph.

### Fourier Analysis — How Trig Takes Over the World

Any periodic function — no matter how jagged — can be decomposed into a sum of sine and cosine waves at different frequencies. This is Fourier's theorem, and it is the mathematical foundation of MP3 compression, JPEG images, MRI scans, noise cancellation, radio, WiFi, and virtually all signal processing. Every time your phone plays a song, Fourier analysis runs a billion sines and cosines per second.

A triangle you can draw with a ruler and protractor leads to the mathematics that runs the modern world.

---

## Connections

- **Prerequisite:** [[Trigonometric Ratios]] — the ratio view; this card extends it to all angles
- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — the coordinate plane the unit circle lives on
- **Prerequisite:** [[Function]] — trig ratios become trig *functions* (domain, range, notation)
- **Leads to:** [[Radians]] — the natural angle unit that makes calculus clean; radian measure replaces degrees at 0606/A-Level/IB
- **Leads to:** [[Sine and Cosine Rules]] — extending trig to non-right triangles
- **Leads to:** [[Trigonometric Identities]] — proving relationships between the functions (0606 §10.4, §10.6)
- **Leads to:** [[Trigonometric Equations]] — solving equations like $2\sin\theta - 1 = 0$ for multiple solutions (the ruler method in action)
- **Leads to:** [[Graph Transformations]] — the general $y = af(b(\theta - c)) + d$ form applied to any function
- **Parallel:** [[Completing the Square]] — discriminant's $\Delta < 0$ introduced $i = \sqrt{-1}$; Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ unites trig functions with complex exponentials
