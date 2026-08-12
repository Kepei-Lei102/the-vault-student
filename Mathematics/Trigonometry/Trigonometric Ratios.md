---
chinese: 三角比 (sānjiǎobǐ) / 三角函数 (sānjiǎo hánshù)
prerequisites:
  - "[[Pythagoras Theorem]]"
  - "[[Similarity]]"
  - "[[Surds]]"
  - "[[Powers and Roots (Vocab)]]"
  - "[[Triangles (Vocab)]]"
leads_to:
  - "[[Trigonometric Functions]]"
  - "[[Sine and Cosine Rules]]"
  - "[[3D Trigonometry]]"
  - "[[Circle Theorems I]]"
  - "[[Radians]]"
  - "[[Complex Numbers]]"
  - "[[Vectors in Physics]]"
  - "[[3D Vectors and the Scalar Product]]"
  - "[[Cross Product]]"
  - "[[Exact Trigonometric Values]]"
  - "[[The Friction Limit]]"
  - "[[Trigonometric Equations]]"
  - "[[Trigonometric Identities]]"
tags:
  - subject/mathematics
  - domain/geometry
  - domain/trigonometry
  - level/IGCSE
  - level/pre-AP
  - level/pre-IB
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/AP
  - syllabus/9260-G19
  - syllabus/0580-E6-2
  - syllabus/0606-10-1
  - syllabus/9709-1-5
  - type/technique
  - notation/sin-cos-tan
  - misconception/wrong-side-labels
  - misconception/calculator-mode
  - misconception/sin-inverse-vs-reciprocal
---

# Trigonometric Ratios 三角比

## Definition

In a **right-angled triangle**, fix one of the non-right angles and call it $\theta$ (theta). Label the three sides **relative to $\theta$**:

- **hypotenuse** (斜边 xiébiān) — the side opposite the right angle (always the longest)
- **opposite** (对边 duìbiān) — the side opposite to $\theta$
- **adjacent** (邻边 línbiān) — the remaining side, next to $\theta$

The three **trigonometric ratios** are:

$$\sin\theta = \dfrac{\text{opposite}}{\text{hypotenuse}} \qquad \cos\theta = \dfrac{\text{adjacent}}{\text{hypotenuse}} \qquad \tan\theta = \dfrac{\text{opposite}}{\text{adjacent}}$$

![[trig-right-triangle-labels.svg]]

### Mnemonic — SOH-CAH-TOA

**S**in = **O**pp/**H**yp  **C**os = **A**dj/**H**yp  **T**an = **O**pp/**A**dj

Chinese classrooms often use the pattern: **"正弦对斜，余弦邻斜，正切对邻"**.

### 中文锚点

三角比 = 在直角三角形中，一个锐角 $\theta$ 所对应的边长之比。这个比值**只取决于角度 $\theta$**，与三角形的大小无关 — 这是整个三角学的根基。

---

## Why the Ratios Are Constant — The Similarity Argument

Here is the fact that makes trigonometry possible:

> **For any fixed angle $\theta$, the ratio opp/hyp is the same no matter how big the triangle is.**

### WHY (proof via similar triangles)

Take any right-angled triangle with acute angle $\theta$. Take another right-angled triangle, also with acute angle $\theta$, but scaled to a different size. Both have a right angle (90°) and angle $\theta$, so by the **angle sum** rule the third angles must also match. All three angles equal → the two triangles are **similar** (see [[Pythagoras Theorem]] §proof 3 for the similar-triangles argument).

Similar triangles have all pairs of corresponding sides in the **same ratio** $k$:
$$\frac{\text{opp}_2}{\text{opp}_1} = \frac{\text{hyp}_2}{\text{hyp}_1} = k$$
Rearranging: $\dfrac{\text{opp}_2}{\text{hyp}_2} = \dfrac{\text{opp}_1}{\text{hyp}_1}$. The ratio is size-invariant.

> [!important] This is the key insight
> $\sin\theta$, $\cos\theta$, $\tan\theta$ are **functions of the angle alone**. Once you know $\theta$, you know all three ratios forever — they are tabulated in your calculator and were once painstakingly tabulated by hand for centuries.

---

## Three Uses of the Ratios

In an exam, the ratios solve three classes of problem:

### 1. Find a side (angle + one side known)
You know $\theta$ and one side; you want another side.
- Pick the ratio containing **both** the known side and the unknown side.
- Rearrange and solve.

**Example.** In a right-angled triangle, $\theta = 35°$ and the hypotenuse is $12$ cm. Find the opposite side.
$\sin 35° = \dfrac{\text{opp}}{12} \implies \text{opp} = 12 \sin 35° \approx 6.88$ cm.

### 2. Find an angle (two sides known)
You know two sides; you want the angle.
- Pick the ratio using those two sides.
- Apply the **inverse** function $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$ (also written $\arcsin$, $\arccos$, $\arctan$).

**Example.** Opposite = $5$, hypotenuse = $13$.
$\sin\theta = \dfrac{5}{13} \implies \theta = \sin^{-1}\!\left(\dfrac{5}{13}\right) \approx 22.6°$.

> [!warning] $\sin^{-1}$ is NOT $\dfrac{1}{\sin}$
> The "$-1$" here is **function-inverse notation**, not an exponent. $\sin^{-1}(x)$ means "the angle whose sine is $x$". The reciprocal $\dfrac{1}{\sin\theta}$ is a different object called $\csc\theta$ (cosecant). This ambiguity is a historical accident; mathematicians often prefer $\arcsin$ to avoid the confusion.

### 3. Apply to real-world angles — elevation and depression
- **Angle of elevation** (仰角 yǎngjiǎo): the angle you look **up** from the horizontal.
- **Angle of depression** (俯角 fǔjiǎo): the angle you look **down** from the horizontal.

These angles always live in a right-angled triangle: the horizontal is one leg, the vertical (height or depth) is another, and the line of sight is the hypotenuse.

---

## Exact Values — the Two Special Triangles

You must know the exact values at $0°, 30°, 45°, 60°, 90°$ by heart. Derive them from two triangles you can reconstruct at will.

![[trig-special-triangles.svg]]

### The 45°–45°–90° triangle (half a square)

Cut a unit square along its diagonal. Each leg is $1$; by Pythagoras the hypotenuse is $\sqrt{1^2+1^2} = \sqrt{2}$.

$$\sin 45° = \cos 45° = \dfrac{1}{\sqrt{2}} = \dfrac{\sqrt{2}}{2}, \qquad \tan 45° = \dfrac{1}{1} = 1$$

### The 30°–60°–90° triangle (half an equilateral)

Take an equilateral triangle with side $2$. Drop an altitude to one side — it bisects the base (giving length $1$) and bisects the $60°$ apex (giving $30°$). The altitude has length $\sqrt{2^2-1^2} = \sqrt{3}$ by Pythagoras.

$$\sin 30° = \dfrac{1}{2}, \qquad \cos 30° = \dfrac{\sqrt{3}}{2}, \qquad \tan 30° = \dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3}$$
$$\sin 60° = \dfrac{\sqrt{3}}{2}, \qquad \cos 60° = \dfrac{1}{2}, \qquad \tan 60° = \sqrt{3}$$

### The master table

| $\theta$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ |
|----------|------|-------|-------|-------|-------|
| $\sin\theta$ | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ |
| $\cos\theta$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ |
| $\tan\theta$ | $0$ | $\dfrac{\sqrt{3}}{3}$ | $1$ | $\sqrt{3}$ | undefined |

> [!tip] Memory pattern — the "$\sqrt{n}/2$" trick
> Write sine as $\dfrac{\sqrt{0}}{2}, \dfrac{\sqrt{1}}{2}, \dfrac{\sqrt{2}}{2}, \dfrac{\sqrt{3}}{2}, \dfrac{\sqrt{4}}{2}$ for $\theta = 0°, 30°, 45°, 60°, 90°$. Cosine is the same sequence reversed. $\tan = \sin/\cos$. One pattern covers the whole table.

---

## Two Identities That Fall Out Immediately

### 1. $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$

**WHY.** $\dfrac{\sin\theta}{\cos\theta} = \dfrac{\text{opp}/\text{hyp}}{\text{adj}/\text{hyp}} = \dfrac{\text{opp}}{\text{adj}} = \tan\theta$. The hypotenuse cancels.

### 2. $\sin^2\theta + \cos^2\theta = 1$ (the Pythagorean identity)

**WHY.** Let the hypotenuse = $h$, opposite = $o$, adjacent = $a$. Pythagoras gives $o^2 + a^2 = h^2$. Divide by $h^2$:
$$\left(\dfrac{o}{h}\right)^2 + \left(\dfrac{a}{h}\right)^2 = 1 \implies \sin^2\theta + \cos^2\theta = 1$$

This is Pythagoras' Theorem wearing trigonometric clothing. Central to all of trigonometry from 0606 onwards.

> [!tip] Notation: $\sin^2\theta$ means $(\sin\theta)^2$
> The power is written on $\sin$ itself to distinguish it from $\sin(\theta^2)$, which would mean "sine of $\theta$ squared". This is a convention, not logic — it conflicts with the $\sin^{-1}$ convention above, where the $-1$ means inverse function, not reciprocal. Welcome to mathematical notation.

---

## Worked Examples

### Example 1 — Find a side

A ladder leans against a wall at $70°$ above the ground. The foot of the ladder is $2.5$ m from the wall. How high up the wall does it reach?

The ladder is the hypotenuse? No — **think carefully**. The known side (2.5 m) is **adjacent** to the $70°$ angle; the wall-height is **opposite**. The ratio linking opposite and adjacent is tan.

$\tan 70° = \dfrac{h}{2.5} \implies h = 2.5 \tan 70° \approx 6.87$ m.

### Example 2 — Find an angle

A right triangle has legs of $7$ and $24$. Find the smaller acute angle.

The smaller angle is opposite the shorter leg.
$\tan\theta = \dfrac{7}{24} \implies \theta = \tan^{-1}\!\left(\dfrac{7}{24}\right) \approx 16.3°$.

(Bonus: this is a Pythagorean triple — hyp = 25. See [[Pythagoras Theorem]].)

### Example 3 — Elevation

From a point $50$ m from the base of a vertical tower, the angle of elevation to the top is $32°$. Find the tower's height.

$\tan 32° = \dfrac{h}{50} \implies h = 50\tan 32° \approx 31.2$ m.

### Example 4 — Exact-value problem (typical 0606/9260 style)

In a right triangle, $\sin\theta = \dfrac{3}{5}$. Find $\cos\theta$ and $\tan\theta$ **without using a calculator**.

Set opp = $3$, hyp = $5$. Pythagoras: adj = $\sqrt{5^2 - 3^2} = \sqrt{16} = 4$. Therefore
$\cos\theta = \dfrac{4}{5}, \quad \tan\theta = \dfrac{3}{4}$.

(This is the 3-4-5 triangle again. You'll see it constantly.)

### Example 5 — Two-step problem

From the top of a $40$ m cliff, the angle of depression to a boat is $25°$. The boat moves directly away; two minutes later the angle of depression is $15°$. How far did the boat travel?

First position: $\tan 25° = \dfrac{40}{d_1} \implies d_1 = \dfrac{40}{\tan 25°} \approx 85.78$ m.
Second position: $d_2 = \dfrac{40}{\tan 15°} \approx 149.28$ m.
Distance travelled $= d_2 - d_1 \approx 63.5$ m.

### Example 6 — Surd answer (9260 Extension style)

In a right-angled triangle, $\tan\theta = \sqrt{3}$ and the adjacent side is $4$ cm. Find the hypotenuse in exact form.

$\tan\theta = \sqrt{3} \implies \theta = 60°$. Then $\cos 60° = \dfrac{1}{2} = \dfrac{4}{\text{hyp}} \implies \text{hyp} = 8$ cm.

---

## Common Mistakes

1. **Mislabelling sides.** "Opposite" and "adjacent" are **relative to the chosen angle** $\theta$ — they swap if you pick the other acute angle. The hypotenuse is fixed (opposite the right angle).
2. **Calculator in the wrong mode.** Degrees (DEG) vs radians (RAD) vs gradians (GRAD). A $30$ that should give $\dfrac{1}{2}$ but gives $-0.988$ means your calculator thinks $30$ means "30 radians". **Always check the mode indicator before trusting a trig answer.**
3. **Confusing $\sin^{-1}$ with $\dfrac{1}{\sin}$.** They are totally different functions. $\sin^{-1}(0.5) = 30°$, but $\dfrac{1}{\sin(0.5 \text{ rad})} \approx 2.086$.
4. **Rounding too early.** Keep full calculator precision through intermediate steps; round only at the end. Rounded intermediates accumulate into visible errors on final answers.
5. **Assuming the triangle is right-angled.** These ratios only apply to right-angled triangles. For general triangles you need the [[Sine and Cosine Rules]].
6. **Forgetting units.** If the sides are in metres, the answer for a side is in metres. Angles are in degrees (unless stated otherwise).
7. **Reporting a negative side.** If your calculator spits out a negative length, you swapped opposite and adjacent, or used inverse trig on an out-of-range argument.

---

## Exam Notes

### OxAQA 9260 (Core + Extension)

**Syllabus ref:** G19. Core: "Know and use $\sin$, $\cos$, $\tan$ in right-angled triangles, including angles of elevation/depression." Extension: exact values of trig ratios at $0°, 30°, 45°, 60°, 90°$; solve problems in 3D (see [[3D Trigonometry]]).

**Typical Paper 2/4 phrasing:**
- "Calculate the length of $AB$, giving your answer correct to 3 significant figures." (1–3 marks)
- "Find the angle of elevation of the top of the tower from the point $P$." (2–3 marks)
- "Show that $\tan\theta = \dfrac{\sqrt{3}}{3}$ and hence find $\theta$." (Extension, exact-value)

**Mark scheme watch:** "Show that" questions require an **exact** answer with working. A decimal approximation scores zero.

### Cambridge 0580 (Extended)

**Syllabus ref:** E6.2. Right-angled trig only in 0580 (no Sine/Cosine Rules at Core; those are Extended only at E6.4).

### Cambridge 0606 (Additional Mathematics)

**Syllabus ref:** 10.1 — three of the six functions the row names. Right-triangle SOH-CAH-TOA itself is assumed from 0580 §6.2; 0606 starts by extending it to the full circular definition (all angles, unit circle), adds the reciprocal functions, the three identities $\sin^2 + \cos^2 = 1$, $1 + \tan^2 = \sec^2$, $\cot^2 + 1 = \csc^2$, and trig graphs. This card is the foundation; **0606 Topic 10** is the superstructure.

### AP Precalculus / IB Mathematics AA & AI

All three curricula assume SOH-CAH-TOA as established knowledge in Year 1 and spend most of their trig time on the **unit circle**, **radian measure**, **reciprocal functions** ($\sec$, $\csc$, $\cot$), **trig identities**, and **trig equations**. The definitions you learn here are recycled — they just get extended beyond right-angled triangles to all angles.

---

## Beyond the Syllabus

### The Unit Circle — Trig for Any Angle

The right-triangle definitions work only for $0° < \theta < 90°$. Beyond that, nothing is "opposite" anything. To extend trig to all angles, mathematicians moved the setup onto a **unit circle**: place a point at angle $\theta$ measured from the positive $x$-axis on the circle of radius $1$ centred at the origin. Then **define** $\cos\theta = $ the point's $x$-coordinate and $\sin\theta = $ its $y$-coordinate. This gives $\sin$ and $\cos$ values for negative angles, for $\theta > 360°$, for every real number.

The right-triangle picture is a **special case** of the unit-circle picture when the angle lies in the first quadrant. This is the bridge from 0580/9260 trig to 0606/AP/IB trig.

### Radians — the Natural Angle Unit

Degrees ($360°$ per circle) are arbitrary — a Babylonian artefact of their base-60 number system and possibly of the year having $\approx 360$ days. The "natural" unit of angle is the **radian**: the angle subtended at the centre of a circle by an arc equal in length to the radius. A full circle has $2\pi$ radians.

Why bother? Because in radians:
$$\dfrac{d}{d\theta}\sin\theta = \cos\theta, \qquad \dfrac{d}{d\theta}\cos\theta = -\sin\theta$$
— the cleanest possible calculus. In degrees, derivatives pick up ugly $\dfrac{\pi}{180}$ factors. You'll switch to radians at 0606/AP-Calc/IB-AA and almost never look back.

### The Etymology — "Sine" is an 800-Year-Old Mistranslation

The word "sine" traces back from Sanskrit *jyā* ("bowstring") through Arabic *jayb* ("bay") to Latin *sinus* — a chain of mistranslations that stuck forever. Every trig function name — sine, cosine, tangent, secant, and their "co-" counterparts — refers to a geometric object you can see on the unit circle. The full story, including the "co-" naming system and the secant/cosecant constructions, is in [[Trigonometric Functions]].

### Trig in Complex Analysis — Euler's Formula

Once you have calculus on $\sin$ and $\cos$, you can derive their **Taylor series**:
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots, \qquad \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$$
Combined with the Taylor series for $e^x$, this produces **Euler's formula**:
$$e^{i\theta} = \cos\theta + i\sin\theta$$
(where $i = \sqrt{-1}$, the imaginary unit — see the discriminant discussion in [[Completing the Square]]). This single identity unites exponential growth, rotation, and oscillation into one object. Setting $\theta = \pi$ gives **Euler's identity** $e^{i\pi} + 1 = 0$, often called the most beautiful equation in mathematics. You will meet this in IB AA HL, AP Calculus BC, and first-year university.

### Fourier Analysis — Where Trig Takes Over the World

Every well-behaved periodic function can be written as a sum of sines and cosines:
$$f(t) = a_0 + \sum_{n=1}^{\infty} \left(a_n \cos(n\omega t) + b_n \sin(n\omega t)\right)$$
This is a **Fourier series**. Its continuous cousin, the **Fourier transform**, decomposes arbitrary signals into frequency components. Applications: audio compression (MP3), image compression (JPEG), medical imaging (MRI, CT), radio, WiFi, noise-cancelling headphones, quantum mechanics. Every time your phone plays a song, Fourier analysis runs a billion sines and cosines per second.

A triangle you can draw with a ruler and protractor leads to the mathematics that runs the modern world.

### Applications Beyond the Classroom

- **Surveying, navigation, astronomy.** How we measure the Earth, the distances to planets, and the positions of stars — literally the oldest application, going back to Hipparchus (c. 150 BCE) who tabulated chords of a circle.
- **Physics.** Simple harmonic motion (pendulums, springs, waves) is described by $\sin$ and $\cos$. AC electricity is sinusoidal. Light and sound are waves.
- **Engineering.** Structural analysis, fluid dynamics, signal processing — all lean heavily on trig.
- **Computer graphics.** Rotating a point by angle $\theta$ in 2D uses the rotation matrix $\begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$ — see [[Matrix Transformations]].
- **Machine learning.** Positional encodings in Transformer architectures (the model behind ChatGPT) use $\sin$ and $\cos$ at multiple frequencies to give tokens a sense of order.

---

## Connections

- **Prerequisite:** [[Pythagoras Theorem]] — identifies the hypotenuse; the similar-triangles argument that makes trig ratios well-defined; underlies $\sin^2 + \cos^2 = 1$.
- **Prerequisite:** [[Surds]] — exact values at $30°, 45°, 60°$ land in surd form.
- **Prerequisite:** [[Powers and Roots (Vocab)]] — the $\sin^2$ vs $\sin^{-1}$ notation clash.
- **Leads to:** [[Trigonometric Functions]] — the unit circle and wave views; extends trig to all angles.
- **Leads to:** [[Sine and Cosine Rules]] — generalises trig to any triangle, not just right-angled.
- **Leads to:** [[3D Trigonometry]] — applying trig to lines and planes in three dimensions.
- **Leads to:** [[Circle Theorems I]] — several theorems involve trig with the radius.
- **Parallel:** [[Gradient (Vocab)]] — for a line making angle $\theta$ with the $x$-axis, $m = \tan\theta$. Gradient and tangent are the same number.
