---
chinese: 极坐标 (jí zuòbiāo)
prerequisites:
  - "[[Radians]]"
  - "[[Trigonometric Identities]]"
  - "[[Complex Numbers]]"
  - "[[Integration]]"
leads_to:
  - "[[Arc Length and Surfaces of Revolution]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/A-Level
  - curriculum/A-Level
  - curriculum/Cambridge-9231
  - curriculum/AP
  - syllabus/9231-1-5
  - syllabus/AP-Calculus-BC-9
  - type/deep
  - type/definition
  - type/proof
  - notation/polar
  - misconception/petal-counting
  - misconception/arctan-quadrant
  - misconception/pole-not-in-simultaneous-solution
  - misconception/forgetting-double-angle-in-area
---

# Polar Coordinates 极坐标

> *Point at something in the room and say where it is. You will not produce a pair of distances from two walls — you will say "over there, about three metres", an angle and a distance. That is a polar coordinate, and it is how every human being has located things since before anyone drew a grid: the lookout's "ship, two points off the starboard bow", the pilot's "bandit at two o'clock, five miles", the radar screen with its sweeping arm.*
>
> *Cartesian coordinates are the strange invention; polar is the native tongue. This page makes the native tongue precise — and then does something with it that Cartesian coordinates find almost impossible: describe a flower petal, a heart-shaped loop or a spiral in one short equation, sketch it by **reading a graph you already know how to read**, and find its exact area with one integral.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| polar coordinates | 极坐标 | position given as (distance, direction) — $(r, \theta)$ |
| pole | 极点 | the fixed centre everything is measured from |
| initial line | 极轴 | the fixed direction $\theta = 0$, drawn horizontally to the right |
| half-line | 射线 | the ray $\theta = \alpha$ — one *direction* out of the pole, not a full line |
| polar equation | 极坐标方程 | a curve written as $r = f(\theta)$ |
| cardioid | 心脏线 | the heart-shaped curve $r = a(1+\cos\theta)$ |
| limaçon | 蜗牛线 | the dented loop $r = a + b\sin\theta$ |
| rose / petal curve | 玫瑰线 | curves like $r = \sin 3\theta$ |
| sector | 扇形 | a pie-slice region swept between two half-lines |

## The two coordinates, and the dictionary

A point's polar coordinates are $(r, \theta)$: its **distance from the pole**, and the **angle from the initial line to the ray it sits on**, measured anticlockwise in [[Radians]].

Overlay the two systems — pole on the origin, initial line along the positive $x$-axis — and the right-angled triangle at every point translates between them:

$$\boxed{\ x = r\cos\theta, \qquad y = r\sin\theta\ } \qquad\qquad \boxed{\ r^2 = x^2 + y^2, \qquad \tan\theta = \frac{y}{x}\ }$$

The left pair (polar → Cartesian) is always safe. The right pair needs one care: $\tan\theta = y/x$ does **not** mean $\theta = \tan^{-1}(y/x)$, because $\tan^{-1}$ only answers between $-\frac{\pi}{2}$ and $\frac{\pi}{2}$ — a point in the second quadrant needs $\pi$ added. Draw the point, read the quadrant, then decide. This is *precisely* the argument-finding discipline from [[Complex Numbers]], because —

> [!note] You have been using polar coordinates for some time already
> The modulus–argument form of a complex number **is** polar coordinates on the Argand diagram: $\lvert z \rvert$ is $r$, $\arg z$ is $\theta$, and $z = r(\cos\theta + i\sin\theta)$ is the dictionary above written as one equation. Everything here about quadrants, angle conventions and the pole transfers both ways — including the mistakes.

### The $r \geqslant 0$ convention

The syllabus states it in so many words: **the convention $r \geqslant 0$ will be used.** A polar equation $r = f(\theta)$ therefore only draws a curve **where $f(\theta) \geqslant 0$**; on any interval where $f(\theta)$ goes negative, there is simply *no curve* — not a curve reflected through the pole, nothing.

This sounds like small print. It is not: it changes what curves look like, it decides how many petals a rose has, and graphing software mostly *ignores* it. What would negative $r$ even mean? **The arm reversing through the pole** — at angle $\theta$, walk distance $\lvert r\rvert$ *backwards*. Here is the same equation under both readings:

![[polar-negative-r.svg|860]]

For $r = \sin 2\theta$ the two conventions genuinely disagree — two petals or four — and this is exactly where the memorised petal rule ("odd $n$: $n$ petals, even $n$: $2n$") comes from: it is *correct in the negative-$r$ world* and wrong in Cambridge's. (For odd $n$ the counts happen to coincide, because the backwards arm retraces petals that already exist — an accident of symmetry, not a vindication of the rule.)

> [!note] Is $r < 0$ a real thing anywhere, or just a convention?
> A fair question, and the answer is *not* "arbitrary, like distancing rules". The split runs along a real seam:
>
> - **Physics and engineering essentially always take $r \geqslant 0$**, because there $r$ *is* something — a radar range, a microphone's sensitivity, an antenna's gain, a LIDAR distance. A negative range is not a convention violation; it is meaningless, the way a negative length is.
> - **Parts of pure mathematics (and the American AP tradition) allow $r < 0$** as an algebraic convenience: formulas stay whole, every $(r,\theta)$ pair plots *somewhere*, and some curves get tidier equations.
>
> Cambridge's convention is the physical one. Since the places a student will actually meet polar plots after the exam are the physical ones — the pickup-pattern diagram on a microphone box, a radar display, an antenna datasheet — the exam convention and the real world agree here, and it is Desmos that is doing something slightly exotic.

## Converting equations — both directions

**Cartesian → polar** is pure substitution, then tidy with a [[Trigonometric Identities|trig identity]]. A real paper's version (November 2024):

*Show that the curve $(x^2+y^2)^2 = 6xy$ has polar equation $r^2 = 3\sin 2\theta$.* [2]

**Tool: the dictionary, then a double angle.** Substitute $x = r\cos\theta$, $y = r\sin\theta$, and spot $x^2+y^2 = r^2$ before expanding anything:

$$\left(r^2\right)^2 = 6\,(r\cos\theta)(r\sin\theta) \quad\Longrightarrow\quad r^4 = 6r^2\sin\theta\cos\theta = 3r^2\sin 2\theta$$

Divide by $r^2$ (fine away from the pole) and the result drops out: $r^2 = 3\sin 2\theta$. Two marks, and both are for exactly the two moves named: substituting the dictionary, and recognising $2\sin\theta\cos\theta$.

**Polar → Cartesian** has one signature move worth naming out loud: **multiply both sides by $r$ first**, so that every term becomes one of the translatable shapes $r^2$, $r\cos\theta$ or $r\sin\theta$. Another real paper's curve (November 2024, Paper 12):

*Find a Cartesian equation for $r = a(\cos\theta + \sin\theta)$.*

**Tool: multiply by $r$, then translate.**

$$r^2 = ar\cos\theta + ar\sin\theta \quad\Longrightarrow\quad x^2 + y^2 = ax + ay$$

**Tool: complete the square** to name the curve:

$$\left(x - \tfrac{a}{2}\right)^2 + \left(y - \tfrac{a}{2}\right)^2 = \tfrac{a^2}{2}$$

— a circle, centre $\left(\tfrac{a}{2}, \tfrac{a}{2}\right)$, radius $\tfrac{a}{\sqrt 2}$, which is what the question went on to ask for. The simplest case of the same move: $r = \cos\theta$ becomes $r^2 = r\cos\theta$, i.e. $x^2+y^2 = x$ — a circle of radius $\tfrac12$ through the pole. Small circles through the pole hide inside innocent-looking polar equations, and multiplying by $r$ is what flushes them out.

## Sketching — read the graph, then wrap it

Here is the whole skill, and it is not a new one.

> **A polar curve is an ordinary graph of $r$ against $\theta$, read while turning.** Sketch $r = f(\theta)$ the way you would sketch any function — where is it zero, where is it biggest, where is it increasing — and then *wrap* that reading around the pole: $\theta$ is how far you have turned, $r$ is how far out you are.

![[polar-read-then-wrap.svg|880]]

![[polar-radar-sweep.mp4]]

*The sweep, live: the arm turns, its length read off the graph at every instant — and in the second beat, $r = \sin 3\theta$ shows the $r \geqslant 0$ convention in action, the arm collapsing to the pole through every negative arch while no curve appears.*

Reading $r = 3 + 2\sin\theta$ as a graph says everything before any plotting: $r$ runs from $3$ up to $5$ (at $\theta = \tfrac{\pi}{2}$), back through $3$, down to $1$ (at $\theta = -\tfrac{\pi}{2}$) — and **never reaches zero**, so the curve never visits the pole. Wrapped, that is a loop that bulges upward to distance 5 and flattens below to distance 1: the limaçon, sketched by reading.

The syllabus lists exactly what a sketch must show, and each item is one read of the $r$–$\theta$ graph:

| Syllabus feature | How you read it off $r = f(\theta)$ |
|---|---|
| **least / greatest $r$** | the minimum and maximum of the graph — mark the value *and* the $\theta$ where it happens |
| **intersections with the initial line** | evaluate $f(0)$ (and $f(\pi)$ if in range) |
| **form at the pole** | where $f(\alpha) = 0$, the curve comes *into the pole along the direction $\theta = \alpha$* — the zeros of the graph are the tangent directions at the pole |
| **symmetry** | $f(-\theta) = f(\theta)$ → mirror in the initial line; $f(\pi - \theta) = f(\theta)$ → mirror in the vertical $\theta = \tfrac{\pi}{2}$ |

That third row deserves its sentence: a polar curve does not cross the pole at random. It arrives there precisely when $r$ hits zero, and the *direction* it arrives from is the $\theta$ that killed $r$. On the rose below, each petal leaves the pole along one zero of $\sin 3\theta$ and returns along the next — the zeros of the graph *are* the petal edges.

### The petal question, answered by reading

Roses are where memorised rules go to die. The reading method needs no rule at all:

![[polar-r-nonnegative.svg|880]]

$\sin 3\theta$ completes three full waves on $[0, 2\pi)$: three arches above the axis, three below. Above the axis, petal; below the axis, **no curve at all**. Three petals — one per non-negative arch, each entering and leaving the pole at consecutive zeros. If a question restricts the domain, the same reading handles it instantly: on $0 \leqslant \theta \leqslant \tfrac{\pi}{3}$ (a real November 2025 question) there is exactly one arch, so exactly one petal, symmetric about its midline $\theta = \tfrac{\pi}{6}$ — which is the "state the line of symmetry" answer.

## The area of a polar region

The syllabus asks you to *recall* $\tfrac12\int r^2\,\mathrm d\theta$. Recall is cheap once you have seen where it comes from — and its ancestor is already printed on your formula sheet.

**Slice the region into thin sectors.** A sliver between $\theta$ and $\theta + \delta\theta$ is, to first order, a *circular* sector: radius $r(\theta)$, angle $\delta\theta$. Its area is the [[Radians]] sector formula — $\tfrac12 r^2 \theta$ with $\theta$ replaced by the tiny angle $\delta\theta$:

$$\delta A \approx \tfrac12\,r^2\,\delta\theta$$

Add the slices and refine, exactly the passage from sum to integral in [[Integration]]:

$$\boxed{\ A = \int_{\alpha}^{\beta} \tfrac12\,r^2 \,\mathrm d\theta\ }$$

![[polar-sector-slices.svg|880]]

**The printed sector formula $\tfrac12 r^2\theta$ is this integral frozen at constant $r$.** MF19 gives you the frozen version (in the Mensuration block) and not the integral — the one formula on this topic you must genuinely carry in your head, and now you can rebuild it from its printed ancestor in one line.

Two practical notes that hold in nearly every question:

- **The integrand is $r^2$, so squaring happens first** — and squaring a trig expression breeds $\cos^2$ and $\sin^2$, which integrate via the double-angle rewrites $\cos^2\theta = \tfrac12(1+\cos 2\theta)$, $\sin^2\theta = \tfrac12(1 - \cos 2\theta)$. Expect this almost every time; curves set as $r^2 = f(\theta)$ are the examiner being merciful, since the squaring is pre-done.
- **The limits are the arches, and the convention is doing real bookkeeping here.** Because the integrand is $r^2$, it is blind to sign — integrate $\tfrac12\int r^2$ over an interval where $f(\theta) < 0$ and you silently add area swept by *no curve*. Concretely: the three petals of $r = \sin 3\theta$ have total area $\tfrac{\pi}{4}$, but $\tfrac12\int_0^{2\pi}\sin^2 3\theta\,\mathrm d\theta = \tfrac{\pi}{2}$ — blind integration over the whole interval gives **exactly double**, phantom petals included. Integrate only over an interval where the curve actually exists — that is, over $[\alpha, \beta]$ with $f(\theta) \geqslant 0$ throughout. For a single loop or petal, $\alpha$ and $\beta$ are **consecutive zeros of $f$**: the $\theta$-values with $f(\alpha) = 0$ and $f(\beta) = 0$ and $f \geqslant 0$ between them — the two moments the curve leaves the pole and returns to it. (If the question's stated domain cuts the arch short, its endpoints take over as limits.)
- **Area between two curves is $\tfrac12\int (r_1^2 - r_2^2)\,\mathrm d\theta$** — the outer sector minus the inner sector, slice by slice. It is *not* $\tfrac12\int (r_1 - r_2)^2\,\mathrm d\theta$: the region between two arcs at the same $\theta$ is a sector ring, not a sector of the difference.

## Where the sweep meets the world

The exam is a guide, not the destination — so it is fair to ask where $r = f(\theta)$ and its area integral actually live. The answer is: anywhere a measurement is made *by direction*.

**The polar curves you already own.** Every microphone's box carries one: the **pickup pattern**, a polar plot where $r(\theta)$ is how sensitively the mic hears from direction $\theta$. The workhorse studio pattern is literally called the **cardioid** — the heart-shaped $r = a(1+\cos\theta)$ from the vocabulary table, chosen because its $r = 0$ point faces straight backwards, which is where the monitor speaker sits. Antenna gain diagrams, stage-light beam profiles and loudspeaker dispersion charts are the same object. Nobody in those rooms calls it Further Pure; everybody reads it the way this page does — where is $r$ biggest, where does it die.

**The area integral, computed live.** A robot vacuum's spinning LIDAR is a radar sweep in miniature: one rotation returns a range $r(\theta)$ for every direction — the distance to the nearest obstacle. The floor the robot has just certified as clear is *exactly* $\tfrac12\int r^2\,\mathrm d\theta$, and the machine evaluates it the honest way, as the Riemann sum $\tfrac12\sum r_i^2\,\delta\theta$ over the few hundred samples of the sweep — thin sectors, added up, precisely the derivation above. The same computation prices radar and sonar coverage, sprinkler throw, and cell-tower footprints. When a question asks for the area bounded by a curve and two half-lines, it is asking the robot's question in exam dress.

And one sweep is running overhead: a planet's line to the Sun sweeps area at a constant rate — but that one deserves its own telling, at the end of the page.

## Worked example — one real question, all three objectives

**9231 Paper 13, November 2024, Q5** — the same paper whose Q3 is worked in [[Symmetric Functions of Roots]]. Its four parts cover the full syllabus row in order, plus the hardest recurring twist.

> *(a) Show that the curve with Cartesian equation $(x^2+y^2)^2 = 6xy$ has polar equation $r^2 = 3\sin 2\theta$.* [2]

Done above — dictionary in, double angle out.

> *The curve $C$ has polar equation $r^2 = 3\sin 2\theta$, for $0 \leqslant \theta \leqslant \tfrac{\pi}{2}$.*
> *(b) Sketch $C$ and state the maximum distance of a point on $C$ from the pole.* [3]

**Tool: read $r^2$ as a graph of $\theta$.** $\sin 2\theta$ rises from $0$ to $1$ as $\theta$ goes $0 \to \tfrac{\pi}{4}$, then falls back to $0$ at $\tfrac{\pi}{2}$. So $r$ starts at the pole, swells to its maximum at $\theta = \tfrac{\pi}{4}$, and returns to the pole: **a single loop in the first quadrant**, entering the pole along $\theta = 0$ and leaving along $\theta = \tfrac{\pi}{2}$ (the two zeros — the "form at the pole"), symmetric about $\theta = \tfrac{\pi}{4}$ because $\sin 2\theta$ is symmetric about it.

**Tool: greatest $r$ from the graph's maximum.** $r^2_{\max} = 3$, so the maximum distance is $\sqrt 3$. The mark scheme accepts the polar point $\left(\sqrt3, \tfrac{\pi}{4}\right)$ — and pointedly *not* $\left(\tfrac{\pi}{4}, \sqrt3\right)$: polar coordinates are $(r, \theta)$, distance first.

> *(c) Find the area of the region enclosed by $C$.* [2]

**Tool: the sector integral, limits from the zeros.**

$$A = \frac12\int_0^{\pi/2} 3\sin 2\theta \,\mathrm d\theta = \frac32\Bigl[-\tfrac12\cos 2\theta\Bigr]_0^{\pi/2} = \frac32\left(\tfrac12 + \tfrac12\right) = \boxed{\frac32}$$

No double angle needed — the curve was given as $r^2$, so the squaring came pre-done.

> *(d) Find the maximum distance of a point on $C$ from the initial line.* [6]

The twist, and the part that separates candidates. Distance from the *initial line* is not $r$ — it is the **height** $y = r\sin\theta$. Maximising it is calculus on the parametrisation.

**Tool: write the height, square to clear the root.** $y = r\sin\theta$ with $r = \sqrt{3\sin 2\theta}$, so it is cleaner to maximise

$$y^2 = 3\sin 2\theta \sin^2\theta$$

**Tool: differentiate and set to zero.** By the product rule,

$$\frac{\mathrm d(y^2)}{\mathrm d\theta} = 3\left(2\cos 2\theta\,\sin^2\theta + \sin 2\theta \cdot 2\sin\theta\cos\theta\right) = 6\sin\theta\left(\cos 2\theta\,\sin\theta + \sin 2\theta\,\cos\theta\right)$$

**Tool: recognise a compound angle.** The bracket is $\sin(2\theta + \theta) = \sin 3\theta$ — the addition formula read right-to-left. So away from $\sin\theta = 0$:

$$\sin 3\theta = 0 \quad\Longrightarrow\quad \theta = \frac{\pi}{3} \ \text{ in range}$$

**Tool: evaluate.** $y^2 = 3\sin\tfrac{2\pi}{3}\,\sin^2\tfrac{\pi}{3} = 3 \cdot \tfrac{\sqrt3}{2} \cdot \tfrac34 = \tfrac{9\sqrt3}{8}$, so

$$y_{\max} = \frac{3\,\sqrt[4]{3}}{2\sqrt 2} \approx 1.40$$

Worth noticing what part (d) really was: $x = r\cos\theta$, $y = r\sin\theta$ makes every polar curve a **parametric curve with parameter $\theta$** — so the whole toolkit of [[Parametric Differentiation]] applies unchanged. "Furthest from the pole" reads off the $r$-graph; "furthest from a *line*" is parametric calculus. Knowing which question you have been asked is most of the six marks.

## Common misconceptions (teaching notes)

### 1. "A rose $r = \sin n\theta$ has $n$ petals if $n$ is odd, $2n$ if even"

Folklore from textbooks that allow negative $r$, imported by students who met polar curves on YouTube or Desmos. Under Cambridge's $r \geqslant 0$ it gives wrong sketches.

**Fix:** ban the rule; teach the read. Sketch $f(\theta)$ flat, shade the sub-axis arches red, and ask "how many arches survive?" That number is the petal count, on any interval, under any convention — because it is not a rule, it is the definition being read.

### 2. $\theta = \tan^{-1}(y/x)$, no questions asked

The second-quadrant point $(-1, 1)$ gets $\theta = -\tfrac{\pi}{4}$ instead of $\tfrac{3\pi}{4}$.

**Fix:** the same fix as in [[Complex Numbers]], because it is the same error: *plot first, then compute*. $\tan^{-1}$ narrates only the right half-plane; a sketch of the point tells you whether to add $\pi$ before the calculator gets a say.

### 3. Finding intersections of two curves by solving $r_1(\theta) = r_2(\theta)$ — and stopping

The algebra finds every crossing where the two curves arrive *at the same point at the same $\theta$*. But the **pole is reached at different $\theta$ on different curves** — $r = \cos\theta$ dies at $\theta = \tfrac{\pi}{2}$, $r = \sin 2\theta$ dies at $\theta = 0$ — so a shared pole never shows up in the simultaneous equations. A real November 2023 question hinges on exactly this: the curves meet "at the pole *and* at another point $P$", and only $P$ comes from algebra.

**Fix:** make the check mechanical. After solving $r_1 = r_2$, ask separately: *does each curve pass through the pole anywhere in range?* If both do, the pole is an intersection, found by inspection rather than by equations.

### 4. Dropping the $\tfrac12$, or integrating $\cos^2$ as if it were $\cos$

The two standard area slips. The first comes from half-remembering; the second from squaring the curve and then integrating on autopilot.

**Fix:** for the $\tfrac12$, re-derive against the frozen ancestor — a full circle must give $\tfrac12 r^2 (2\pi) = \pi r^2$, which it does only with the half. For $\cos^2$: the double-angle rewrite is not optional decoration, it is *the* route — no antiderivative of $\cos^2\theta$ exists that skips it.

### 5. "The area between the curves is $\tfrac12\int(r_1 - r_2)^2\,\mathrm d\theta$"

Pattern-matched from "area between graphs is the integral of the difference" — but the polar area formula squares *before* subtracting, and $(r_1-r_2)^2 \ne r_1^2 - r_2^2$.

**Fix:** slice it. One sliver of the in-between region is an outer sector minus an inner sector: $\tfrac12 r_1^2\,\delta\theta - \tfrac12 r_2^2\,\delta\theta$. The subtraction happens between *areas*, and areas carry squares already.

## Exam Notes

### Cambridge 9231 Further Mathematics — **Further Pure 1, Paper 1**

**§1.5** is as reliable as §1.3: a polar question has appeared on **every Paper 1 variant from 2021 through 2026**, June and November, usually as Q5–Q7 and worth 8–14 marks. Three learning objectives:

- **Understand the Cartesian–polar relations and convert equations both ways** — with the syllabus stating outright that *the convention $r \geqslant 0$ will be used*.
- **Sketch simple polar curves** on $0 \leqslant \theta < 2\pi$ or $-\pi < \theta \leqslant \pi$ or a subset — and the syllabus itemises what sketches must show: *symmetry, intersections with the initial line, the form of the curve at the pole, and least/greatest values of $r$*. It also promises that *detailed plotting will not be required* — the reading above is genuinely all that is asked.
- **Recall and use $\tfrac12\int r^2\,\mathrm d\theta$** in simple cases. *Recall* — it is not printed.

**The recurring question shapes:**

| Shape | Looks like | Marks |
|---|---|---|
| convert, Cartesian → polar | *"Show that the curve … has polar equation …"* | 2–3 |
| sketch + extreme distance | *"Sketch $C$ and state the greatest distance of a point on $C$ from the pole"* | 2–3 |
| area | *"Find the exact value of the area of the region bounded by $C$, the initial line and the half-line $\theta = \dots$"* | 4–7 |
| convert, polar → Cartesian | *"Find a Cartesian equation for $C$"* — multiply by $r$ first | 3–4 |
| max distance from the **initial line** | maximise $y = r\sin\theta$ by differentiation | 5–6 |
| two curves | intersections (mind the pole), then area split across the crossing | 5–8 |

**What the recent papers actually set** — a deliberately wide net: limaçons, roses, lemniscate-type $r^2 = a\cos 2\theta$ loops, circles in disguise, the Archimedean spiral $r = a\theta$, and exponential-flavoured curves like $r = \theta e^{\theta/8}$ or $r = e^{-\theta} - e^{-2\pi}$ whose areas need [[Integration by Parts|parts]] or a substitution the question supplies. The *reading* method is curve-agnostic, which is the point of learning it rather than a catalogue of named shapes.

- **"Exact value" means exact** — answers arrive as things like $\tfrac{3 - 4\ln 2}{4\pi}$; a decimal scores nothing.
- **State extreme distances as distances**, and polar points in the order $(r, \theta)$ — the N24 mark scheme explicitly refuses $\left(\tfrac{\pi}{4}, \sqrt3\right)$.
- **MF19 prints nothing for this section.** The sector formula $\tfrac12 r^2\theta$ in the Mensuration block is the constant-$r$ ancestor of the integral — recognise it, rebuild from it, and see [[MF19 Reference (9231)]] for the full audit.

### AP Calculus BC

Polar lives in **Unit 9** (§9.7–9.9): polar functions, $\tfrac{\mathrm dy}{\mathrm dx}$ on polar curves via the parametric route, and area — including area between curves. Two genuine differences from 9231: AP allows negative $r$ (so rose petal counts differ — the folklore rule is *correct* there), and AP asks for slopes of tangent lines, which Cambridge does not. The area formula and its derivation are identical.

### Where this is *not* examined

**Not on Cambridge 9709** — no polar coordinates anywhere in single maths; the closest encounter is the modulus–argument form in [[Complex Numbers]]. **Not on IB AA** at SL or HL. So a Further student is meeting genuinely new geometry, with the Argand diagram as the one familiar landmark.

> [!info] Beyond syllabus — Kepler's equal areas, or why planets do this integral
> The second of Kepler's laws says a planet's line to the Sun **sweeps equal areas in equal times**. "Area swept" is exactly this page's integral, and its time-derivative is
> $$\frac{\mathrm dA}{\mathrm dt} = \tfrac12 r^2 \frac{\mathrm d\theta}{\mathrm dt}$$
> Kepler's law is the statement that this quantity is constant — and multiplying by $2m$ reveals what is really being conserved: $m r^2 \dot\theta$ is the planet's [[Angular Momentum]]. Equal areas in equal times *is* conservation of angular momentum, seen through a polar area integral, three centuries before anyone had the word for it. Orbits are the native habitat of polar coordinates: a force pointing always at one centre makes $(r, \theta)$ the honest description and $(x, y)$ the clumsy one.

> [!info] Beyond syllabus — the two great spirals
> ![[polar-two-spirals-comic.png|760]]
>
> The **Archimedean spiral** $r = a\theta$ grows by *adding* — each turn the same step further out, the shape of everything humans roll: rope, carpet, the groove of a record. The **logarithmic spiral** $r = ae^{b\theta}$ grows by *multiplying* — each turn the same factor further out, identical at every scale, the shape of everything that *grows*: the nautilus, the hurricane, the galaxy. Nature prefers the second because living and swirling things grow in proportion to their current size, which is the defining property of [[Exponential Function|the exponential]].
>
> Jacob Bernoulli asked for a logarithmic spiral on his tombstone, with the motto *eadem mutata resurgo* — "though changed, I rise again the same." The mason carved an Archimedean one. Even tombstones have error rates.

## Connections

- **Parent:** [[Radians]] — the angle language everything here is written in, and the source of the frozen sector formula $\tfrac12 r^2\theta$ that the area integral generalises.
- **Already met as:** [[Complex Numbers]] — the modulus–argument form is polar coordinates on the Argand diagram, quadrant discipline included.
- **Tools used:** [[Trigonometric Identities]] — double angles for both conversion and every $\int r^2$; [[Integration]] — the slice-and-refine passage from $\delta A$ to the integral; [[Integration by Parts]] — for the exponential-flavoured curves recent papers favour.
- **Same machinery:** [[Parametric Differentiation]] — $x = r\cos\theta$, $y = r\sin\theta$ makes every polar curve parametric in $\theta$, which is exactly how "furthest from the initial line" is done.
- **Where it leads in physics:** [[Angular Momentum]] — $\tfrac12 r^2\dot\theta$ constant is Kepler's second law; [[Circular Motion]] — the $r$-constant special case that mechanics lives in.
- **For 9231 students:** [[MF19 Reference (9231)]] — nothing printed for §1.5; the Mensuration sector formula is the ancestor to rebuild from.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $(r, \theta)$ | `(r, \theta)` | distance first, angle second — mark schemes enforce the order |
| $r = f(\theta)$ | `r = f(\theta)` | a polar equation |
| $\tfrac12\int_\alpha^\beta r^2\,\mathrm d\theta$ | `\tfrac12\int_\alpha^\beta r^2\,\mathrm d\theta` | the sector area |
| $\theta = \alpha$ | `\theta = \alpha` | a half-line: one ray, not a full line |
| $\sqrt[4]{3}$ | `\sqrt[4]{3}` | fourth root, as in the N24 answer |
| $\dot\theta$ | `\dot\theta` | time-derivative, Kepler note only — table-only per house style |
