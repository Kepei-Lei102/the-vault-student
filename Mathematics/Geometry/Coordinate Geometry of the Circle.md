---
chinese: 圆的解析几何 (yuán de jiěxī jǐhé)
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Pythagoras Theorem]]"
  - "[[Loci (Vocab)]]"
  - "[[Circle Vocabulary (Vocab)]]"
  - "[[Quadratic Equations]]"
  - "[[Completing the Square]]"
  - "[[Circle Theorems II]]"
  - "[[Length and Midpoint (Vocab)]]"
leads_to:
  - "[[Trigonometric Identities]]"
teach_together:
  - "[[Discriminant]]"
tags:
  - subject/mathematics
  - domain/geometry
  - domain/algebra
  - level/IGCSE
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-8-1
  - syllabus/0606-8-2
  - syllabus/0606-8-3
  - syllabus/0606-8-4
  - syllabus/9709-1-3
  - type/deep
  - type/equation
  - type/proof
  - notation/standard-form-circle
  - notation/general-form-circle
  - misconception/centre-sign-flip
  - misconception/radius-not-squared
---

# Coordinate Geometry of the Circle 圆的解析几何

## Definition

A **circle in the Cartesian plane** is the set of all points $(x, y)$ at a fixed distance $r$ from a fixed point $(a, b)$. Algebraically:

$$
\boxed{(x - a)^2 + (y - b)^2 = r^2}
$$

This is the **standard form** of a circle — centre $(a, b)$, radius $r > 0$. It is nothing more than the **algebraic transcription of the locus rule**: "distance from $(a, b)$ equals $r$." The whole subject of analytic geometry begins with that single move — write a geometric condition as an equation, and then geometric questions become algebraic computations.

### 中文锚点

圆的解析几何 = 把圆这个几何对象用方程描述出来。圆的定义是 *"到定点距离为定长的所有点的集合"* — 把这个集合关系翻译成方程，就是 $(x-a)^2 + (y-b)^2 = r^2$，其中 $(a,b)$ 是圆心，$r$ 是半径。这一步从几何走向代数，是解析几何的精髓。一旦圆变成了方程，所有几何问题都变成了代数题：相交、相切、求切线，全部用代数解。

---

## Why It Matters — From Locus to Equation

The previous card, [[Loci (Vocab)]], framed every geometric shape as a *set of points satisfying a rule*. A circle, in that framing, is the locus "all points at distance $r$ from centre $(a, b)$." This card cashes that into algebra.

The pivot is **Descartes' analytic geometry** (1637): once you put coordinates on the plane, every geometric object has an equation, every equation cuts out a curve, and the geometric–algebraic dictionary becomes a two-way translation. A line-circle intersection problem stops being "where do I draw the line?" and becomes "solve a quadratic." A tangent problem stops being "what's perpendicular to the radius?" and becomes "solve the quadratic with a repeated root." Geometry without coordinates is Euclid; geometry *with* coordinates is everything that came after.

> [!info] Beyond syllabus — the founding move of analytic geometry
> Descartes published *La Géométrie* in 1637 as an appendix to his philosophical *Discourse on the Method*. His central claim was that **every geometric problem is reducible to algebra by introducing coordinates**. A circle becomes $(x-a)^2 + (y-b)^2 = r^2$; a line becomes $y = mx + c$; their intersection becomes a system of two equations. Three centuries later, the same move underlies computer graphics, physics simulations, neural network optimisers (loss landscapes are surfaces in coordinate space), and GPS trilateration. Once you can write a curve as an equation, a computer can manipulate it.

---

## The Standard Form — Derivation

Let $C = (a, b)$ be the centre and $P = (x, y)$ a point on the circle. By definition $|CP| = r$.

The distance formula (which is just [[Pythagoras Theorem]] applied to the right triangle with legs $|x - a|$ and $|y - b|$) gives:

$$
|CP| = \sqrt{(x - a)^2 + (y - b)^2}
$$

Setting $|CP| = r$ and squaring both sides:

$$
(x - a)^2 + (y - b)^2 = r^2
$$

That's it. The squaring is harmless because both sides are non-negative. The equation says exactly what the locus rule said — every solution $(x, y)$ is precisely the points at distance $r$ from $(a, b)$.

> [!tip] Two ways the equation can lie
> If the right-hand side comes out **negative** in an equation that's *supposed* to be a circle, there are no real solutions — the "circle" is empty (the geometric statement was inconsistent). If the right-hand side comes out **zero**, the locus is just the single point $(a, b)$ — a degenerate "circle of radius 0." Examiners sometimes plant these to test whether you actually checked. Always verify $r^2 > 0$ after extracting the centre and radius.

---

## The General Form

Expanding the standard form:

$$
\begin{aligned}
(x - a)^2 + (y - b)^2 &= r^2 \\
x^2 - 2ax + a^2 + y^2 - 2by + b^2 &= r^2 \\
x^2 + y^2 - 2ax - 2by + (a^2 + b^2 - r^2) &= 0
\end{aligned}
$$

The Cambridge 0606 specification calls this the **general form**, written

$$
\boxed{x^2 + y^2 + 2gx + 2fy + c = 0}
$$

with $g = -a$, $f = -b$, $c = a^2 + b^2 - r^2$. So:

$$
\text{centre} = (-g, -f), \qquad \text{radius} = \sqrt{g^2 + f^2 - c}.
$$

The signs flip — that's the most-failed point in the whole card. If the equation has $+6x$, then $2g = 6$, so $g = 3$, and the centre's $x$-coordinate is $-g = -3$, *not* $+3$. Always remember: the centre coordinates are the **opposite of half the linear coefficients**.

> [!tip] Memorise the radius formula as "negative of the constant"
> $r^2 = g^2 + f^2 - c$. A clean way to remember the sign: take the centre $(-g, -f)$, plug it back into the LHS of the general form, and the result is $-r^2$. (Because $(-g)^2 + (-f)^2 + 2g(-g) + 2f(-f) + c = g^2 + f^2 - 2g^2 - 2f^2 + c = -(g^2 + f^2 - c) = -r^2$.) The centre is the only point where the LHS is exactly $-r^2$.

---

## Recovering the Centre and Radius — Completing the Square

When the equation is given in general form, the standard recipe is **completing the square** twice (once in $x$, once in $y$). See [[Completing the Square]] for the algebra.

**Worked example.** Find the centre and radius of $x^2 + y^2 + 6x - 4y + 4 = 0$.

$$
\begin{aligned}
x^2 + 6x + y^2 - 4y + 4 &= 0 \\
(x^2 + 6x + 9) - 9 + (y^2 - 4y + 4) - 4 + 4 &= 0 \\
(x + 3)^2 + (y - 2)^2 &= 9
\end{aligned}
$$

So centre $(-3, 2)$, radius $3$. Cross-check via the formula: $g = 3$, $f = -2$, $c = 4$, giving centre $(-g, -f) = (-3, 2)$ ✓ and $r = \sqrt{9 + 4 - 4} = 3$ ✓.

**Worked example with a twist.** Find the centre and radius of $2x^2 + 2y^2 - 8x + 12y - 6 = 0$.

The leading coefficient is not 1 — divide first: $x^2 + y^2 - 4x + 6y - 3 = 0$. Now complete the square:

$$
(x - 2)^2 + (y + 3)^2 = 16, \qquad \text{centre } (2, -3), \quad r = 4.
$$

> [!tip] Examiners love this trap
> If $x^2$ and $y^2$ have a coefficient other than 1, **divide everything by that coefficient first**. Otherwise the formulas $(-g, -f)$ and $\sqrt{g^2+f^2-c}$ give the wrong answer. The general form always assumes a leading coefficient of 1.

---

## Tangent at a Given Point on the Circle

A tangent to a circle at point $P$ is the line through $P$ that is **perpendicular to the radius** $CP$ — see [[Circle Theorems II]] for the geometric proof. In coordinate geometry this becomes a slick algebraic move.

**Standard method:** find the gradient of the radius, then take the negative reciprocal.

Let $P = (x_0, y_0)$ be the point on the circle with centre $C = (a, b)$. The gradient of $CP$ is $\dfrac{y_0 - b}{x_0 - a}$, so the tangent gradient is $-\dfrac{x_0 - a}{y_0 - b}$. The tangent line:

$$
y - y_0 = -\frac{x_0 - a}{y_0 - b}\,(x - x_0).
$$

**Elegant shortcut.** Working in vectors, the tangent at $P$ is the locus of points $X$ such that $(X - P) \perp (P - C)$, i.e. $(X - P) \cdot (P - C) = 0$.

![[coord-geom-circle-tangent-shortcut.svg]]

The diagram makes the perpendicularity claim visible: the green vector $P - C$ is the radius; the purple vector $X - P$ runs from $P$ along the tangent to any chosen test point $X$. The right-angle marker at $P$ is the geometric statement that these two vectors are perpendicular, which is *exactly* the algebraic statement that their dot product is zero. Expanding $(X - P) \cdot (P - C) = 0$ and using the fact that $P$ is on the circle (so $(x_0 - a)^2 + (y_0 - b)^2 = r^2$) gives:

$$
\boxed{(x - a)(x_0 - a) + (y - b)(y_0 - b) = r^2}
$$

This is the **tangent equation in standard form** — beautifully symmetric, no fractions. Memorise this as "replace one factor of $(x-a)^2$ with $(x_0-a)$, and one of $(y-b)^2$ with $(y_0-b)$, and the equation of the *circle* becomes the equation of the *tangent at* $(x_0, y_0)$."

> [!info] Beyond syllabus — this is the polar line in disguise
> The same "splitting" trick works for any conic: the line $\frac{(x-a)(x_0-a)}{r^2} + \frac{(y-b)(y_0-b)}{r^2} = 1$ is called the **polar line** of $P$ with respect to the circle. When $P$ is *on* the circle, the polar is the tangent at $P$. When $P$ is *outside* the circle, the polar is the chord joining the two tangent points from $P$ — the *chord of contact*. When $P$ is the centre, the polar is the line at infinity. This is the entry point to projective geometry; see *Pole and polar* in any university-level geometry text.

---

## Line–Circle Intersection — and the Discriminant

To find where a line meets a circle, **substitute the line equation into the circle equation** and solve the resulting quadratic.

**Worked example.** Where does the line $y = x + 1$ meet the circle $x^2 + y^2 = 25$?

Substitute: $x^2 + (x + 1)^2 = 25 \Rightarrow 2x^2 + 2x - 24 = 0 \Rightarrow x^2 + x - 12 = 0 \Rightarrow (x - 3)(x + 4) = 0$.

So $x = 3$ (giving $y = 4$) or $x = -4$ (giving $y = -3$). Two intersection points: $(3, 4)$ and $(-4, -3)$.

**The discriminant tells the geometric story.** The substitution always produces a quadratic in $x$ (or in $y$, depending on which variable you eliminated). Its discriminant $\Delta = b^2 - 4ac$ has three cases (see [[Discriminant]] for the underlying theory):

| Discriminant | Number of solutions | Geometric meaning |
|---|---|---|
| $\Delta > 0$ | two | line crosses the circle (a *secant* — see [[Circle Vocabulary (Vocab)]]) |
| $\Delta = 0$ | one (repeated) | line is **tangent** to the circle |
| $\Delta < 0$ | none | line misses the circle entirely |

This is one of the cleanest demonstrations of the algebra–geometry dictionary: the algebraic property "discriminant equals zero" matches the geometric property "tangent." The two perspectives reinforce each other.

![[coord-geom-circle-line-intersection.svg]]

**Worked example (tangent via $\Delta = 0$).** For what value of $k$ is the line $y = 2x + k$ tangent to the circle $x^2 + y^2 = 5$?

Substitute: $x^2 + (2x + k)^2 = 5 \Rightarrow 5x^2 + 4kx + (k^2 - 5) = 0$.

For tangency, $\Delta = 0$: $(4k)^2 - 4 \cdot 5 \cdot (k^2 - 5) = 0 \Rightarrow 16k^2 - 20k^2 + 100 = 0 \Rightarrow -4k^2 = -100 \Rightarrow k = \pm 5$.

Two values — one for each of the two parallel tangents on opposite sides of the circle.

---

## Two Circles — Five Configurations

Given two circles with centres $C_1, C_2$ and radii $r_1, r_2$. Let $d = |C_1 C_2|$ (the distance between centres). The relative size of $d$ versus $r_1 + r_2$ and $|r_1 - r_2|$ determines the configuration completely:

| Relation | Configuration | Common points |
|---|---|---|
| $d > r_1 + r_2$ | separate, externally apart | 0 |
| $d = r_1 + r_2$ | externally tangent | 1 |
| $\lvert r_1 - r_2 \rvert < d < r_1 + r_2$ | overlapping (two intersections) | 2 |
| $d = \lvert r_1 - r_2 \rvert$ | internally tangent | 1 |
| $d < \lvert r_1 - r_2 \rvert$ | one inside the other, disjoint | 0 |

![[coord-geom-circle-two-circles.svg]]

> [!info] Beyond syllabus — the radical axis
> When two circles intersect at two points, the line through those two points is called the **radical axis**. There's a beautiful trick to find it: subtract the two circle equations. The $x^2$ and $y^2$ terms cancel (both have coefficient 1), leaving a linear equation — the radical axis. This works even when the circles *don't* intersect — the radical axis still exists as a line, perpendicular to the line of centres, with the property that any point on it has equal "power" with respect to both circles ($d^2 - r^2$, the same algebraic quantity for both). Used in mechanics for finding the locus of equal-tension points between two springs.

---

## Parametric Form (Beyond Syllabus, Bridges to Trig)

The circle $(x - a)^2 + (y - b)^2 = r^2$ also has a **parametric** description:

$$
\begin{cases}
x = a + r\cos\theta \\
y = b + r\sin\theta
\end{cases}
\qquad \theta \in [0, 2\pi).
$$

You can verify by substituting: $(r\cos\theta)^2 + (r\sin\theta)^2 = r^2(\cos^2\theta + \sin^2\theta) = r^2$ — the Pythagorean trig identity. (See [[Trigonometric Identities]] for the proof of $\cos^2 + \sin^2 = 1$, which is itself just Pythagoras applied to the unit-circle right triangle.)

The parametric form is a **moving-point** view of the circle: as $\theta$ sweeps from $0$ to $2\pi$, the point $(x, y)$ traces the circle counter-clockwise. This is the bridge to:

- **Velocity around a circle** in physics (uniform circular motion, $\theta = \omega t$)
- **Plotting circles in software** (every graphics library uses this internally)
- **Conic sections** more generally — ellipse $x = a\cos\theta$, $y = b\sin\theta$; parabola $x = at^2$, $y = 2at$; hyperbola $x = a\sec\theta$, $y = b\tan\theta$.

A locus, after all, doesn't *have* to be a path traced in time (we made that point in [[Loci (Vocab)]]) — but it *can be*, when that's the more useful description. Coordinate geometry lets you choose either lens.

---

## Common Mistakes

1. **Sign flip on the centre.** The general form $x^2 + y^2 + 2gx + 2fy + c = 0$ has centre $(-g, -f)$, not $(g, f)$. Always do the standard-form conversion to double-check.
2. **Forgetting to take $\sqrt{}$.** The standard form gives $r^2$, not $r$. If $(x - 2)^2 + (y + 1)^2 = 16$, the radius is $4$, not $16$.
3. **Leading coefficient ≠ 1 in general form.** $2x^2 + 2y^2 + \ldots = 0$ is *not* in general form — divide by 2 first. The formulas $(-g, -f)$ and $\sqrt{g^2 + f^2 - c}$ assume a leading coefficient of 1.
4. **Tangent gradient at a vertical radius.** If the radius $CP$ is vertical, the gradient is undefined and the tangent is horizontal: $y = y_0$. If horizontal, the tangent is vertical: $x = x_0$. The negative-reciprocal formula breaks at these special cases. The vector-form tangent equation $(x - a)(x_0 - a) + (y - b)(y_0 - b) = r^2$ handles both gracefully.
5. **Forgetting $r^2 > 0$.** If completing the square gives $(x - 1)^2 + (y - 2)^2 = -3$, the equation has no real solutions — there is no circle. Treating this as "radius $\sqrt{-3}$" loses marks.
6. **Confusing line-circle and circle-circle.** Two circles have **at most two** intersection points (use the radical-axis trick), not four. Two distinct conics in general can meet in up to four points (Bézout), but two circles always degenerate to a line × line.

---

## Exam Notes

### Cambridge 0606

**Syllabus refs:** §8.1, §8.2, §8.3, §8.4 — the entire 0606 §8 cluster. Expect 5–8 mark questions covering:

- (§8.1, §8.2) Convert between standard and general form. Find centre and radius from a given equation.
- (§8.3) Find the equation of a tangent at a given point. Find where a line meets a circle. Determine whether a line is a tangent (use the discriminant).
- (§8.4) Find the equation of a circle given specific information: three points, centre and one point, two ends of a diameter, etc.

> [!tip] 0606-specific tip
> Cambridge often phrases questions as "the line $y = mx + k$ is a tangent to the circle ... — find $k$." The standard solution is *substitute, set the discriminant to zero*. They love this template — practise it in both forms (line tangent to circle given, find $m$; or vice versa).

### A-Level (Edexcel / OCR / AQA)

A-Level Pure Mathematics extends the 0606 material with: equations of chord, perpendicular bisector of a chord (which always passes through the centre), intersection of two circles via simultaneous equations, and the use of the equation of a circle to solve geometric proofs.

### IB AA HL & AP Calculus / Precalculus

IB and AP cover circles as a special case of **conic sections**. The general second-degree equation $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ describes a conic, and a circle is the case $A = C \neq 0$, $B = 0$. The other cases give ellipses, parabolas, and hyperbolas — the same family that Apollonius classified in 200 BC. AP Calculus uses circles for *implicit differentiation* practice; IB HL uses them for *parametric differentiation* and to introduce *vector equations of curves*.

---

## Connections

- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — putting points into $(x, y)$ form
- **Prerequisite:** [[Pythagoras Theorem]] — the distance formula is Pythagoras
- **Prerequisite:** [[Loci (Vocab)]] — circle as locus, the rule the equation encodes
- **Prerequisite:** [[Circle Vocabulary (Vocab)]] — chord, tangent, secant, radius
- **Prerequisite:** [[Quadratic Equations]] — line-circle intersection produces a quadratic
- **Prerequisite:** [[Completing the Square]] — converts general form back to standard form
- **Sibling:** [[Circle Theorems I]] and [[Circle Theorems II]] — the geometric perspective on the same circle; "tangent ⊥ radius" (CT II) is what makes the tangent-equation derivation work
- **Leads to:** [[Discriminant]] — the line-circle intersection demands $b^2 - 4ac$ analysis
- **Leads to:** [[Trigonometric Identities]] — $\cos^2 + \sin^2 = 1$ is the parametric circle equation
- **Application:** GPS trilateration — three known points and three known distances to your position give three circles whose intersection is your location
- **Application:** computer graphics — circle, ellipse, and arc primitives all reduce to this equation
- **Bridge to physics:** uniform circular motion uses the parametric form $x = r\cos(\omega t)$, $y = r\sin(\omega t)$ for position; differentiating gives velocity (tangential) and acceleration (centripetal)
- **Beyond high school:** *Pole and polar* in projective geometry; *Apollonius circles* (locus where the ratio of distances to two points is constant — turns out to be another circle, surprisingly); *inversive geometry* (mapping circles to lines and vice versa)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $(x-a)^2 + (y-b)^2 = r^2$ | `(x-a)^2 + (y-b)^2 = r^2` | Standard form |
| $x^2 + y^2 + 2gx + 2fy + c = 0$ | `x^2 + y^2 + 2gx + 2fy + c = 0` | General form |
| $\sqrt{g^2 + f^2 - c}$ | `\sqrt{g^2 + f^2 - c}` | Radius from general form |
| $\Delta = b^2 - 4ac$ | `\Delta = b^2 - 4ac` | Discriminant |
| $r\cos\theta, r\sin\theta$ | `r\cos\theta, r\sin\theta` | Parametric coordinates |
| $\perp$ | `\perp` | Perpendicular |
| $\lvert C_1C_2 \rvert$ | `\lvert C_1C_2 \rvert` | Distance between centres |
