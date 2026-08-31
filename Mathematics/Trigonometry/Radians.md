---
chinese: 弧度 (hú dù)
prerequisites:
  - "[[Circle Vocabulary (Vocab)]]"
  - "[[Circles Arcs and Sectors (Vocab)]]"
  - "[[Trigonometric Ratios]]"
  - "[[Trigonometric Functions]]"
leads_to:
  - "[[Differentiation]]"
  - "[[Integration]]"
  - "[[Euler's Number]]"
  - "[[Complex Numbers]]"
  - "[[Taylor Series]]"
  - "[[Simple Harmonic Motion]]"
  - "[[Differentiation Rules]]"
  - "[[Euler's Formula and De Moivre's Theorem]]"
  - "[[Squeeze Theorem]]"
  - "[[Trigonometric Equations]]"
  - "[[Trigonometric Graphs]]"
  - "[[Trigonometric Identities]]"
  - "[[Polar Coordinates]]"
  - "[[Circular Motion]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - domain/geometry
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/AP
  - syllabus/0606-9-1
  - syllabus/9709-1-4
  - type/definition
  - type/proof
  - notation/radian
  - notation/pi
  - misconception/degree-vs-radian-mode
  - misconception/radian-as-unit
  - misconception/small-angle-approx
---

# Radians 弧度

## Definition

### Formal

A **radian** is the angle at the centre of a circle subtended by an arc whose length equals the radius. Equivalently, for any circle of radius $r$:

$$\theta \text{ (in radians)} = \frac{\text{arc length}}{\text{radius}} = \frac{s}{r}$$

A full revolution traces the entire circumference $2\pi r$, so a full turn measures $s/r = 2\pi r / r = 2\pi$ radians.

$$2\pi \text{ rad} = 360°$$

### Intuitive

A radian asks the most natural question about an angle: *how many radius-lengths does the arc span?* Once you phrase it that way, the formulas collapse — arc length is literally $r\theta$ because $\theta$ *is* the count of radii along the arc. No fractions of $360$ to track, no unit conversion hidden in your formulas. Radians are what the circle would have chosen for itself.

The name itself reads the definition out loud: a **rad**ian is a **rad**ius-worth of arc.

### 中文锚点

中国学生从初中开始接触**弧度制**，英文考试里就是 radian measure。定义是一模一样的：弧长除以半径。
$$\theta = \frac{s}{r} \qquad \text{(} s \text{ 弧长, } r \text{ 半径)}$$
只是英文里要会说：

- *one radian* = 一弧度
- *π radians* = π 弧度 = $180°$
- *in radians* = 以弧度为单位

考试常踩的坑是 **"radian" 是一个纯数比值，没有实际单位**（弧长的米除以半径的米，米抵消了），但计算器上 DEG / RAD 两种模式的切换会直接影响 $\sin, \cos, \tan$ 的数值。在 0606 及以上的所有考试里，弧度是**默认**的角度单位。

## Bridge — Degrees and Radians Side by Side

You already know the degree-based arc/sector formulas from [[Circles Arcs and Sectors (Vocab)]]. Radians are a **new representation of the same geometry**, not a new topic. The radian formulas are what you get when you write the old ones using $\theta/(2\pi)$ instead of $\theta/360°$ as the fraction-of-circle, then cancel.

| Quantity | Degrees | Radians | Why the radian version is cleaner |
|---|---|---|---|
| Full turn | $360°$ | $2\pi$ | Radian value is intrinsic — $2\pi$ radii fit around |
| Straight line | $180°$ | $\pi$ | Half a turn |
| Right angle | $90°$ | $\pi/2$ | Quarter turn |
| Arc length | $s = \dfrac{\theta}{360°} \cdot 2\pi r$ | $s = r\theta$ | Fraction-of-circle vanishes |
| Sector area | $A = \dfrac{\theta}{360°} \cdot \pi r^2$ | $A = \dfrac{1}{2} r^2 \theta$ | Same cleanup |
| Derivative of $\sin$ | $(\sin x°)' = \dfrac{\pi}{180}\cos(x°)$ | $(\sin x)' = \cos x$ | The single biggest reason radians exist |

The right column is the reason every calculus course in the world switches to radians — the formulas become structural rather than cluttered with $\pi/180$ factors.

![[radian-definition.svg|697]]

Left: one radian is the angle for which the arc equals the radius. Right: the unit circle marked with the standard radian values — $\pi/6, \pi/4, \pi/3, \pi/2, \pi, 3\pi/2, 2\pi$. Memorise these; they appear in every 0606/A-Level/IB trig question.

## Conversion

The single identity $\pi \text{ rad} = 180°$ generates every conversion:

$$\boxed{1 \text{ rad} = \frac{180°}{\pi} \approx 57.2958°, \qquad 1° = \frac{\pi}{180} \text{ rad} \approx 0.01745 \text{ rad}}$$

### Working conversions

To convert **degrees → radians**, multiply by $\pi/180$:
$$60° \times \frac{\pi}{180} = \frac{60\pi}{180} = \frac{\pi}{3} \text{ rad}$$

To convert **radians → degrees**, multiply by $180/\pi$:
$$\frac{5\pi}{6} \times \frac{180°}{\pi} = \frac{5 \cdot 180°}{6} = 150°$$

### Canonical table

These are the values every 0606/A-Level student must know on sight. Say them aloud until the degree-radian pairs become reflexive.

| Degrees | Radians | Arc-per-radius |
|---|---|---|
| $0°$ | $0$ | $0$ |
| $30°$ | $\pi/6$ | $\approx 0.524$ |
| $45°$ | $\pi/4$ | $\approx 0.785$ |
| $60°$ | $\pi/3$ | $\approx 1.047$ |
| $90°$ | $\pi/2$ | $\approx 1.571$ |
| $120°$ | $2\pi/3$ | $\approx 2.094$ |
| $135°$ | $3\pi/4$ | $\approx 2.356$ |
| $150°$ | $5\pi/6$ | $\approx 2.618$ |
| $180°$ | $\pi$ | $\approx 3.142$ |
| $270°$ | $3\pi/2$ | $\approx 4.712$ |
| $360°$ | $2\pi$ | $\approx 6.283$ |

## Notation

| Convention | Symbol / style | Notes |
|---|---|---|
| Explicit unit | $\theta = \pi/3 \text{ rad}$ | Clearest, but rarely needed after the first line of a problem |
| No unit | $\theta = \pi/3$ | Standard in 0606/A-Level/IB — if $\pi$ appears, radians is assumed |
| Degree mark | $\theta = 60°$ | The small circle is **mandatory** for degrees — no mark means radians |
| Revolutions | $\tfrac{1}{6}$ turn | Rare in exams; common in engineering and CS (rotation matrices) |

> [!warning] Omitting the $°$ is not a choice — it changes the answer
> Writing $\sin 30$ without a degree mark means $\sin(30 \text{ rad})$ — and $30$ radians is about $4.77$ full turns, giving $\sin 30 \approx -0.988$, not $0.5$. This is the single most common calculator-mode error in the 0606 exam.

> [!info] Why radians have "no unit"
> Radians are defined as arc length divided by radius — length over length, so the unit cancels to a pure number. That's why angular speed in rad/s looks dimensionally the same as a frequency 1/s, and why $\sin\theta$ for small $\theta$ in radians can equal $\theta$ itself (you can't sensibly add a dimensional quantity to $1$). The $°$ symbol, by contrast, carries the conversion factor $\pi/180$ inside it — $\sin(x°)$ secretly means $\sin(x \cdot \pi/180)$.

## The deepest reason — degree is a unit, radian is a pure number

Of all the answers to *"why do mathematicians prefer radians?"* this one is the most intuitive, and it doesn't require any calculus to land:

**A degree is a unit. A radian is not.** A radian is a *pure number* — the dimensionless ratio of two lengths.

When you write "60 degrees," the $°$ is a real unit, like *metres* or *seconds* or *kilograms*. It says: *"I have divided one full revolution into 360 equal parts and I am counting 60 of them."* The choice of 360 is arbitrary — Babylonian, base-60, historically baked in. A Martian civilisation that divided the circle into 400 parts (the *gradian*, which actually exists on some scientific calculators) would have its own perfectly valid "degree-like" unit. There's nothing privileged about 360.

When you write "$\pi/3$ radians," there is no unit at all. By definition, $\theta = \text{arc}/\text{radius}$ — *length divided by length*. The dimensions cancel. What remains is a pure number, exactly like $2$ or $e$ or $\pi$ itself. **The word "radian" is a label, not a unit** — it's a reminder of what kind of ratio we're talking about, the way you might say "this is a strain" or "this is a probability" or "this is a Mach number." All of those things are pure numbers with names.

> [!tip] The parallel that makes this click — strain in materials science
> The clearest parallel from physics is **strain** in [[Stress, Strain and Young Modulus]]. Strain is defined as $\varepsilon = \Delta L / L_0$ — change in length over original length. Both numerator and denominator have units of metres, so the ratio is a *pure number*. You can write $\varepsilon = 0.002$ or $\varepsilon = 0.2\%$, but the $\%$ is just a "divide by 100" notation; there's no real unit involved.
>
> Compare this to *stress* in the same card: $\sigma = F/A$ has units of pascals (N/m²) — a real unit, not a pure number. The Young modulus $E = \sigma/\varepsilon$ inherits stress's units (pascals) because dividing by a pure number doesn't introduce dimensions.
>
> **Radian is to degree as strain is to … well, nothing, because strain doesn't have a competing unit.** That's actually the deeper point: the most natural physical quantities (strain, refractive index, probability, Mach number, π, e, the fine-structure constant) are pure numbers. Units are useful but added — by humans, for convenience. The radian is the angle measurement that nature picked; degrees are what 4000-year-old Babylonian astronomers picked.

This framing immediately explains every "why radians" puzzle without any calculus machinery:

- **Why does $\sin x \approx x$ for small $x$?** Because if $x$ is a pure number (radian), the comparison $\sin x \approx x$ is dimensionally consistent — pure number on both sides. If $x$ were in degrees, $\sin(30°)$ and $30°$ would have different "kinds" — one a pure number, one a unit-carrying quantity — and the approximation would need an explicit conversion: $\sin(x°) \approx x \cdot \pi/180$.

- **Why is the conversion factor exactly $\pi/180$?** Because converting a unit to a pure number means dividing by the unit's *size*. One degree corresponds to $\pi/180$ of a radian (i.e., the arc-over-radius ratio of $\pi/180$). The $\pi/180$ is literally "how big one degree is as a pure number."

- **Why does $(\sin x)' = \cos x$ only when $x$ is in radians?** Because the derivative is the slope of $\sin$ at $0$, which the proof in the next section shows equals $1$ — *but only when the input is a pure number*. If $x$ is in degrees, the slope at $0$ is $\pi/180$, and you'd need to write $(\sin(x°))' = (\pi/180)\cos(x°)$, dragging the conversion factor through every derivative forever.

The full Taylor-series justification of $\sin x \approx x - x^3/6 + \ldots$ (see [[Maclaurin Series]]) deepens the point further — but the unit-vs-pure-number framing above already answers *"why radians?"* completely, without needing any calculus.

## Key Facts

### Arc length

$$\boxed{s = r\theta \qquad (\theta \text{ in radians})}$$

**Why:** This is the *definition* rewritten. $\theta = s/r$ is how radians are defined; multiply both sides by $r$ and you have arc length. No fraction-of-circle, no $\pi/180$, just "arc = angle × radius".

### Sector area

$$\boxed{A_{\text{sec}} = \tfrac{1}{2} r^2 \theta \qquad (\theta \text{ in radians})}$$

**Why (fraction argument):** A full circle has area $\pi r^2$ and subtends $2\pi$ radians at the centre. A sector at angle $\theta$ is the fraction $\theta / (2\pi)$ of the whole, so its area is

$$\frac{\theta}{2\pi} \cdot \pi r^2 = \frac{1}{2} r^2 \theta. \qquad \blacksquare$$

> [!info] Beyond syllabus — derivation by polar integration
> Once you know integration, the sector area falls out of the polar area integral
> $$A = \int_0^\theta \tfrac{1}{2} r^2 \, d\phi = \tfrac{1}{2} r^2 \theta$$
> because $r$ is constant along the arc of a circle. For non-circular polar curves $r = f(\phi)$, the formula generalises to $A = \tfrac{1}{2} \int [f(\phi)]^2 \, d\phi$, which you meet in IB AA HL and A-Level Further Maths.

### Perimeter of a sector

$$P_{\text{sec}} = r\theta + 2r = r(\theta + 2)$$

The arc length plus the two radii. A common lost mark is forgetting the $2r$.

### Length of chord (beyond 9.1, but useful)

The chord joining the two ends of a sector of angle $\theta$ has length

$$\ell = 2r \sin\!\tfrac{\theta}{2}$$

which gives the **segment area** $A_{\text{seg}} = \tfrac{1}{2} r^2(\theta - \sin\theta)$ after a bit of algebra. This is the standard 0606 compound-shape setup.

## Why Calculus Demands Radians

This is the deepest reason radians exist, and the punchline of the card. Starting from the definition of the derivative,

$$\frac{d}{dx}\sin x = \lim_{h \to 0} \frac{\sin(x+h) - \sin x}{h}$$

expand using the angle-addition formula $\sin(x+h) = \sin x \cos h + \cos x \sin h$:

$$= \lim_{h \to 0} \frac{\sin x \cos h + \cos x \sin h - \sin x}{h} = \sin x \cdot \lim_{h \to 0} \frac{\cos h - 1}{h} + \cos x \cdot \lim_{h \to 0} \frac{\sin h}{h}$$

Everything hinges on the two limits

$$L_1 = \lim_{h \to 0} \frac{\sin h}{h}, \qquad L_2 = \lim_{h \to 0} \frac{\cos h - 1}{h}.$$

**In radians**, $L_1 = 1$ and $L_2 = 0$ (proofs below), giving the clean

$$\boxed{(\sin x)' = \cos x, \qquad (\cos x)' = -\sin x.}$$

### Why the same limit becomes $\pi/180$ in degrees

Writing "$\sin(x°)$" is a disguise. There is really only one sine function — the one that lives on the unit circle and takes an *arc length* (= radian) as input. The degree version secretly converts first:

$$\sin(x°) \;\equiv\; \sin\!\left(x \cdot \tfrac{\pi}{180}\right).$$

That conversion factor $\pi/180$ is baked into the function the moment you write the degree mark. Now watch what happens to $L_1$ when $h$ is measured in degrees. Let $u = h \cdot \pi/180$ be the radian equivalent, so $h = u \cdot 180/\pi$:

$$\frac{\sin(h°)}{h} \;=\; \frac{\sin\!\big(h \cdot \tfrac{\pi}{180}\big)}{h} \;=\; \frac{\pi}{180} \cdot \underbrace{\frac{\sin u}{u}}_{\to\, 1}.$$

As $h \to 0$, $u \to 0$ too, so the limit is $\pi/180 \cdot 1 = \pi/180$, not $1$. The conversion factor doesn't cancel — it survives as a permanent multiplier.

Propagating through the derivative calculation:

$$(\sin x°)' = \frac{\pi}{180} \cos(x°).$$

Every chain-rule differentiation stacks another factor: $(\sin(kx°))' = \frac{k\pi}{180}\cos(kx°)$, $(\sin^2 x°)' = \frac{\pi}{90}\sin(x°)\cos(x°)$, and so on. Each $\pi/180$ has to be carried through every integration too, polluting every antiderivative with a constant that should not logically be there.

Radians are the angle unit in which the conversion factor *is* $1$ — because the radian measure was *defined* to make arc length equal angle times radius. Calculus picked radians because the circle's own geometry enters the sine function without a unit conversion sitting in front. Radians don't make trig derivatives *possible*; they make them *clean*.

> [!tip] Structural summary
> The $\pi/180$ factor enters because the squeeze-theorem proof below depends on the step "sector area $= \tfrac12 h$", which is only true when $h$ is in radians. In degrees, the same sector has area $\pi h / 360$, and that $\pi/180$ factor propagates into $L_1$ and then into every trig derivative.

### Proof that $\lim_{h \to 0} \frac{\sin h}{h} = 1$ (squeeze argument)

![[squeeze-theorem-unit-circle.svg|640]]

The whole proof is this picture. On the unit circle, the tiny pink "$h$" wedge at the origin is the central angle, and because the radius is $1$, the arc labelled "arc $= h$" has length exactly $h$. The inner blue triangle $OAP$, the pink sector $OAP$, and the outer triangle $OAT$ (blue + pink + amber together) are *nested by area* — strictly in that order. Writing that nesting as an inequality and squeezing is the entire argument.

For $0 < h < \pi/2$, draw the unit circle and mark the point $P = (\cos h, \sin h)$ on the arc from $(1, 0)$. Three regions emerge, nested by area:

| Region | Area |
|---|---|
| Triangle $OAP$ (where $A = (1,0)$) | $\tfrac{1}{2} \sin h$ |
| Circular sector $OAP$ | $\tfrac{1}{2} h$ (radians!) |
| Triangle $OAT$ (where $T = (1, \tan h)$ is the tangent intersection) | $\tfrac{1}{2} \tan h$ |

The sector sits strictly between the two triangles, so

$$\tfrac{1}{2} \sin h < \tfrac{1}{2} h < \tfrac{1}{2} \tan h \quad \Longrightarrow \quad \sin h < h < \frac{\sin h}{\cos h}.$$

Divide through by $\sin h$ (positive for small $h > 0$):

$$1 < \frac{h}{\sin h} < \frac{1}{\cos h}.$$

Invert (all three terms positive):

$$\cos h < \frac{\sin h}{h} < 1.$$

As $h \to 0^+$, $\cos h \to 1$, so by the squeeze theorem $\sin h / h \to 1$. The same limit holds from the left by evenness of $\cos$ and oddness of $\sin$. $\blacksquare$

The general squeeze theorem — its formal $\epsilon$-$\delta$ proof, its applicability to bounded-oscillation cases like $x\sin(1/x) \to 0$, and the broader analyst's-hammer story — lives in [[Squeeze Theorem]]. The argument above is its canonical first application.

The load-bearing step is **"sector area $= \tfrac{1}{2} h$"** — which is only true when $h$ is in radians. Swap in degrees and the sector has area $\tfrac{1}{2} \cdot h \cdot \pi/180$, and the limit becomes $\pi/180$ instead of $1$. So radians appear in the calculus the moment you commit to the sector-area formula, which means they appear the moment you commit to the definition of a radian.

### Proof that $\lim_{h \to 0} \frac{\cos h - 1}{h} = 0$

Multiply top and bottom by $\cos h + 1$:

$$\frac{\cos h - 1}{h} = \frac{\cos^2 h - 1}{h(\cos h + 1)} = \frac{-\sin^2 h}{h(\cos h + 1)} = -\frac{\sin h}{h} \cdot \frac{\sin h}{\cos h + 1}.$$

As $h \to 0$, the first factor $\to 1$, the numerator of the second $\to 0$, and the denominator $\to 2$. So the whole expression $\to -1 \cdot 0/2 = 0$. $\blacksquare$

## Small-Angle Approximations

From $\sin h / h \to 1$ and $(\cos h - 1)/h \to 0$ we get the three workhorse approximations valid for $\theta$ *small and in radians*:

$$\sin\theta \approx \theta, \qquad \tan\theta \approx \theta, \qquad \cos\theta \approx 1 - \tfrac{1}{2}\theta^2.$$

### Why the cosine approximation is quadratic

The [[Taylor Series|Taylor expansions]] (beyond 0606, standard at A-Level/IB) are

$$\sin\theta = \theta - \tfrac{\theta^3}{6} + \tfrac{\theta^5}{120} - \cdots, \qquad \cos\theta = 1 - \tfrac{\theta^2}{2} + \tfrac{\theta^4}{24} - \cdots$$

At small $\theta$, $\sin$ starts linearly (leading term $\theta$) while $\cos$ starts quadratically (leading $1 - \theta^2/2$). Keep the second-order term for $\cos$; the linear one is just $1$ and gives no information. Trigonometry is the first place students meet Taylor series in action — any power-series identity you've seen for $\sin$, $\cos$, or $e^x$ is a Taylor expansion in disguise.

> [!tip] Physics bridge — simple pendulum and SHM
> The small-angle approximation $\sin\theta \approx \theta$ is the reason a pendulum's period is *independent of amplitude* (for small swings). The equation of motion $\ddot\theta + (g/L)\sin\theta = 0$ is a nightmare non-linear ODE; swap $\sin\theta$ for $\theta$ and it becomes simple harmonic motion with period $T = 2\pi\sqrt{L/g}$. Every grandfather clock depends on this approximation — and on radians. See [[Simple Harmonic Motion]] when the physics folder opens.

## Worked Examples

### Example 1 (0606 §9.1): arc length and sector area

A sector has radius $r = 10\text{ cm}$ and central angle $\theta = \pi/3$ rad. Find the arc length, the sector area, and the perimeter of the sector.

$$s = r\theta = 10 \cdot \tfrac{\pi}{3} = \tfrac{10\pi}{3}\text{ cm}$$
$$A = \tfrac{1}{2} r^2 \theta = \tfrac{1}{2}(100)\tfrac{\pi}{3} = \tfrac{50\pi}{3}\text{ cm}^2$$
$$P = s + 2r = \tfrac{10\pi}{3} + 20\text{ cm}$$

Leave in exact form. A follow-up question might ask for 3 significant figures — then $s \approx 10.47\text{ cm}$, $A \approx 52.36\text{ cm}^2$.

### Example 2 (0606 §9.1): find the angle given arc length

An arc of length $12\text{ cm}$ lies on a circle of radius $8\text{ cm}$. Find the central angle in radians and in degrees.

$$\theta = \frac{s}{r} = \frac{12}{8} = \frac{3}{2}\text{ rad}$$

In degrees: $\tfrac{3}{2} \cdot \tfrac{180°}{\pi} = \tfrac{270°}{\pi} \approx 85.94°$.

The 0606 mark scheme typically accepts either form unless the question specifies. If a later part asks for the sector area, use the radian value:
$$A = \tfrac{1}{2}(8)^2 \cdot \tfrac{3}{2} = 48\text{ cm}^2.$$

### Example 3 (0606 §9.1): segment area — the classic compound-shape question

A chord joins two points $A, B$ on a circle of radius $6\text{ cm}$. The chord subtends an angle of $\tfrac{\pi}{2}$ at the centre. Find (i) the sector area $OAB$, (ii) the triangle area $OAB$, (iii) the minor segment area.

(i) Sector: $A_{\text{sec}} = \tfrac{1}{2}(36)\tfrac{\pi}{2} = 9\pi\text{ cm}^2$.

(ii) Triangle: the two radii are at right angles, so $A_{\triangle} = \tfrac{1}{2}(6)(6) = 18\text{ cm}^2$. More generally, $A_{\triangle} = \tfrac{1}{2} r^2 \sin\theta$.

(iii) Segment: sector minus triangle: $A_{\text{seg}} = 9\pi - 18\text{ cm}^2 \approx 10.27\text{ cm}^2$.

### Example 4 (A-Level, small-angle): physics approximation

Estimate $\sin(0.05)$ and $\cos(0.05)$ without a calculator, where $0.05$ is in radians.

$$\sin(0.05) \approx 0.05, \qquad \cos(0.05) \approx 1 - \tfrac{1}{2}(0.05)^2 = 1 - 0.00125 = 0.99875.$$

Calculator check: $\sin(0.05) = 0.04998\ldots$, $\cos(0.05) = 0.99875\ldots$. The approximations are accurate to four decimal places at this scale — and this is why pendulums work.

## Common Misconceptions

### 1. Calculator left in the wrong mode

Student writes $\sin(\pi/6) = \sin(0.524) \approx 0.500$ correctly, then on the next question computes $\sin 60 \approx -0.305$ — because the calculator is still in radian mode and $60$ radians is roughly $9.5$ full turns. Every calculator mistake in 0606 trigonometry traces to DEG/RAD confusion.

**Fix:** Teach a *mode-check reflex*. Before any trig calculation: look at the top of the calculator display for DEG or RAD. If the question uses $\pi$ or labels $\theta$ without a degree mark, set RAD. If it uses $°$, set DEG. Make students announce the mode out loud. Once they confuse themselves badly on a mock paper, the habit sticks forever.

### 2. Forgetting to convert in $s = r\theta$

Student applies $s = r\theta$ with $\theta = 60°$, getting $s = 10 \cdot 60 = 600\text{ cm}$ for a 10-cm-radius arc. The formula *requires* $\theta$ in radians.

**Fix:** Make the conversion the first line of working, always. "Given $\theta = 60°$. Convert: $\theta = 60 \cdot \pi/180 = \pi/3$ rad. Now $s = r\theta = 10 \cdot \pi/3 = 10\pi/3\text{ cm}$." Writing the conversion line explicitly earns partial credit even when the rest is wrong, and prevents the error in the first place.

### 3. Treating "radian" as a unit you can cancel or carry

Students sometimes see "rad/s" and try to write things like $\sin(5 \text{ rad}) = \sin(5) \text{ rad}$ — treating "rad" as a unit that sticks around like "m" or "s". It doesn't: $\sin(5)$ is a pure number, dimensionless.

**Fix:** Remind them that radians are *defined* as a ratio of two lengths, so the units cancelled at the source. Writing "rad" is a labelling convenience, not a dimensional tag. In physics formulas like $v = r\omega$, the radian doesn't show up on the length side because it already cancelled.

### 4. Using the small-angle approximation in degrees

Student writes "$\sin 5° \approx 5$" and gets a wildly wrong answer (true value is $\approx 0.0872$).

**Fix:** Drill the phrase "$\sin\theta \approx \theta$ **only when $\theta$ is in radians and small**". Convert first: $5° = \pi/36 \approx 0.0873$ rad, and then $\sin(5°) \approx 0.0873$, which matches. The approximation is a statement about the slope of $\sin$ at $0$ being $1$, which is only true in the calculus-native angle unit.

### 5. Confusing $2\pi$ and $\pi$ for a full turn

Roughly half of first-time radian users write "full circle = $\pi$" because $\pi \approx 3.14$ "feels like" the answer. A full circle is $2\pi$. Half a circle (a straight angle) is $\pi$.

**Fix:** Anchor on the identity $\pi \text{ rad} = 180°$. A straight line is half a turn, so it has half the radians of a full turn. From there, $2\pi = $ full turn is automatic.

## A Brief History — How Radians Came to Own Calculus

The companion card [[Trigonometric Functions]] tells the story of where the words *sine*, *cosine*, *tangent* came from — a 2000-year chain of Sanskrit, Arabic, and Latin, with one famous mistranslation preserved forever. That's the story of the **functions themselves**. What follows here is the other half: the story of their **input** — why trigonometry spoke degrees for nearly 4000 years before calculus quietly revealed that the circle had been speaking radians all along.

### ~2000 BCE — the Babylonians pick 360°

The first quantitative astronomy was Babylonian. Their calendar ran on a 360-day year (close enough to the true solar period to be useful), so the sun appeared to move about one "step" along the zodiac per day — a natural unit of angle. Their base-60 number system made 360 a spectacularly composite choice: it divides evenly by 2, 3, 4, 5, 6, 8, 9, 10, 12, and many more, which is a gift for any astronomer dividing a circle into fractions. Greek, Indian, Islamic, and European astronomers all inherited this framework. For roughly 3500 years the question "what unit is an angle?" simply wasn't asked — it was degrees, and that was that.

### 150 BCE – 150 CE — Hipparchus and Ptolemy build tables of chords, not sines

Hipparchus (~150 BCE) made the first systematic trigonometric table. Ptolemy refined it in the *Almagest* (~150 CE). But neither was tabulating sines. They tabulated **chords**: given a central angle $\theta$ on a circle of radius $R = 60$, the chord was the raw straight-line distance between the two endpoints of the arc. Values came out as lengths, not dimensionless ratios — "chord of $60°$ is $60$" on Ptolemy's unit circle. Trigonometry for its first five centuries was a ledger you looked up: degrees in, lengths out.

### ~500 CE — Aryabhata's half-chord becomes sine

In India, Aryabhata realised that instead of the full chord, it was cleaner to tabulate the **half-chord** — the vertical drop from one end of the chord to the diameter through the other. This half-chord is literally sine. The Sanskrit name was *jyā* (bowstring), and its journey through Arabic *jaib* and Latin *sinus* gave us the English word — the etymology is in [[Trigonometric Functions]]. Arab and Persian mathematicians then extended Aryabhata's work; by roughly 1000 CE, all six trigonometric functions — sine, cosine, tangent, cotangent, secant, cosecant — had been named and tabulated. Yet through all of this, **the angle was still in degrees**. A trig table was a lookup: enter $30°$, read off a length. There was no abstract trigonometric function in the modern sense, and no reason to consider any other angle unit.

### 1670s — Newton's sleepwalking radian

When Newton derived the power series

$$\sin x = x - \tfrac{x^3}{6} + \tfrac{x^5}{120} - \cdots$$

he obtained it by inverting the series for $\arcsin$, which came from a geometric integral on the unit circle. In that derivation $x$ **had to be** the arc length, not a fraction of $360°$. Newton used what we'd now call a radian, quietly, without naming it or defending the choice — the geometry had simply forced his hand. For nearly a century after Newton, calculus-on-trig proceeded in this nameless arc-length unit. The mathematical community was *already speaking radians* without realising it needed a word.

### 1748 — Euler sees the whole picture

The *Introductio in analysin infinitorum* was the decisive moment. Euler was not trying to reform trigonometry — he was building analysis, the new subject of infinite series and complex functions, as one unified edifice. In the process he plugged $z = i\theta$ into the exponential series

$$e^z = 1 + z + \tfrac{z^2}{2!} + \tfrac{z^3}{3!} + \cdots$$

and watched the real and imaginary parts separate cleanly into the series for $\cos\theta$ and $\sin\theta$:

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

This wasn't just an identity — it was an announcement that sine, cosine, and the exponential were three projections of a single complex-exponential object. Trigonometry, calculus, and complex analysis became one subject. But the identity only works clean if $\theta$ is arc length on the unit circle — plug in degrees and a rogue $\pi/180$ has to be carried around forever. After Euler, every trig function got reformulated as a true analytic function of a real (or complex) number, and the native input became the radian.

Euler, typically, didn't bother to name the unit. He just called it "the arc."

### 1873 — finally giving the unit a name

For 125 years after Euler, mathematicians used radians without naming them. The word *radian* wasn't coined until 1873, by James Thomson (brother of Lord Kelvin). The delay is telling: for that century and a quarter, the mathematical community so clearly took radians as *the* unit that contrasting it with anything else felt unnecessary. A name only became useful once engineers and applied scientists — still thinking in degrees — needed a vocabulary that could accommodate both.

### The punchline

For 3500 years, trigonometry lived in degrees because its job was astronomy, and astronomy is full of angles to read off the sky and report to another astronomer. Degrees were the *interface*. Radians only emerged when trigonometry's job changed — when it became an *input* to calculus. At that moment, degrees stopped being a neutral convenience and started being a conversion factor that polluted every derivative, every integral, every power series. Calculus revealed that the circle had always been speaking radians; degrees were a translator good enough that no one noticed until we started asking the circle a different kind of question.

So when a student asks "why radians, not degrees?" — the honest answer isn't "because radians are better." It's that **degrees were the language of astronomy, and radians were the language mathematics had been speaking quietly underneath for centuries**. The two never had to meet until calculus brought them into the same room.

## Exam Notes

### Cambridge 0606

**§9.1 (Circular Measure)** — "Solve problems involving arc length and sector area, including knowledge and use of radian measure." This is the *entire* syllabus content of §9 — one row, one card resolves the whole section. Typical questions:

- Give an angle in radians, ask for arc length, sector area, or perimeter.
- Give two of (arc, radius, angle), ask for the third.
- Compound shapes: sector combined with a triangle or a smaller sector (segment problems, crescents).

Radians appear throughout the rest of 0606 — every trig, differentiation, and integration question from §9 onwards assumes radian measure.

### A-Level (Pure 1)

**Edexcel P1 §5, AQA Pure §D** — includes radians, arc length, sector area, plus the **small-angle approximations** $\sin\theta \approx \theta$, $\cos\theta \approx 1 - \tfrac{1}{2}\theta^2$, $\tan\theta \approx \theta$ with applications to approximating expressions near $\theta = 0$. Often tested as "given $\theta$ is small, show that $\dfrac{\sin 3\theta + 2\cos\theta}{1 - \cos 2\theta}$ is approximately …".

Radian differentiation (§8 Pure 2) is the payoff — $(\sin x)' = \cos x$, $(\cos x)' = -\sin x$, $(\tan x)' = \sec^2 x$ all live in radians.

### IB AA (SL and HL)

**Topic 3 (Trigonometry)** — radian measure is the primary angle unit from day one. AA HL adds the derivation of the small-angle limits (Topic 5 Calculus) and the extension to $\sin(nx)$, $\cos(nx)$ derivatives under the chain rule.

### AP

**AP Precalculus / AP Calculus AB** — radians are assumed in AP Calculus. Derivatives and integrals of trig functions always in radians. The AP Precalculus framework introduces radian measure alongside unit-circle trig in Unit 3.

## Connections

- **Prerequisite:** [[Circle Vocabulary (Vocab)]] — radius, arc, sector, central angle defined here.
- **Prerequisite:** [[Circles Arcs and Sectors (Vocab)]] — degree-based formulas; this card is the cleanup.
- **Prerequisite:** [[Trigonometric Ratios]] — $\sin, \cos, \tan$ on the unit circle; already flagged radians in its enrichment section.
- **Prerequisite:** [[Trigonometric Functions]] — graphs of trig functions; radian domain makes the period $2\pi$ rather than $360$.
- **Leads to:** [[Differentiation]] — radian derivatives of $\sin, \cos, \tan$; the core payoff.
- **Leads to:** [[Integration]] — integrals of $\sin, \cos$ and their composites in the $(ax+b)$ form.
- **Leads to:** [[Euler's Number]] — the complex-exponential identity $e^{i\theta} = \cos\theta + i\sin\theta$ only makes sense with $\theta$ in radians.
- **Leads to:** [[Complex Numbers]] — modulus-argument form $r(\cos\theta + i\sin\theta)$ and polar form rely on radian $\theta$.
- **Leads to:** [[Taylor Series]] — the small-angle approximations $\sin\theta \approx \theta$, $\cos\theta \approx 1 - \theta^2/2$ are truncated Taylor expansions; trig is the first place they bite.
- **Physics bridge — reserved:** [[Simple Harmonic Motion]] — the small-angle approximation is the linearisation that turns the pendulum ODE into SHM with period $T = 2\pi\sqrt{L/g}$. Reserved for the Physics folder.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\theta$ | `\theta` | Standard angle variable |
| $\pi$ | `\pi` | Keep symbolic in radian answers |
| $2\pi$ | `2\pi` | A full revolution |
| $\pi/2, \pi/3, \pi/4, \pi/6$ | `\pi/2`, etc. | The memorise-on-sight angles |
| $s = r\theta$ | `s = r\theta` | Arc length in radians |
| $\tfrac{1}{2} r^2 \theta$ | `\tfrac{1}{2} r^2 \theta` | Sector area in radians |
| $\sin\theta \approx \theta$ | `\sin\theta \approx \theta` | Small-angle approximation (radians only) |
| $\cos\theta \approx 1 - \tfrac{\theta^2}{2}$ | `\cos\theta \approx 1 - \tfrac{\theta^2}{2}` | Second-order small-angle |
| $\text{rad}$ | `\text{rad}` | Unit tag when needed |
| $60°$ | `60°` | Degree mark — mandatory for degrees |
