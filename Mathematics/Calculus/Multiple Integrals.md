---
chinese: 多重积分 (duōchóng jīfēn)
prerequisites:
  - "[[Integration]]"
  - "[[Partial Derivatives and the Gradient]]"
  - "[[Integration by Substitution]]"
  - "[[Polar Coordinates]]"
  - "[[Determinants and Inverses]]"
leads_to:
  - "[[Vector Calculus]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/university
  - type/definition
  - type/theorem
  - type/proof
  - type/visual-tool
  - notation/double-integral
  - notation/jacobian
  - misconception/forgetting-the-r-in-polar
  - misconception/outer-limits-may-contain-variables
  - misconception/changing-order-means-swapping-the-limits
  - misconception/a-double-integral-is-always-a-volume
  - misconception/the-jacobian-can-be-negative
---

# Multiple Integrals 多重积分

> [[Partial Derivatives and the Gradient]] asked how steep a hillside is, and found that the honest answer is an arrow. Here is the next question about the same hill: **how much earth is in it?**
>
> A single integral adds up along a line. A hill stands on a patch of ground, so the adding has to cover an area.

## The question — how much earth is in a hill?

The hill's height above a flat plain, in metres, is

$$h(x, y) = 400 - 0.001x^2 - 0.002y^2 .$$

Cover the ground with a grid of small squares of area $\Delta A$. Over each square stands a column of earth, roughly a box, of height $h$ and volume $h \, \Delta A$. Add the columns. Shrink the squares and the staircase top closes in on the true surface.

![[multiple-integrals-columns.svg|820]]

The figure does this for a simpler surface, $z = 4 - x^2 - y^2$ over the unit square, where the exact answer can be found. With $2 \times 2$ columns the total is $3.3750$; with $10 \times 10$ it is $3.3350$; with $1000 \times 1000$, a million columns, it is $3.333334$. The value it settles on is $\tfrac{10}{3}$, and that value is what the symbol $\iint$ means. The hill itself is finished in Example 5.

Two things remain. One is a way to get $\tfrac{10}{3}$ without a million additions. The other is what to do when the ground underneath is not a square.

## Definition

### Formal

Let $f$ be continuous on a bounded region $R$ of the plane. Cut $R$ into $n$ small pieces of areas $\Delta A_1, \dots, \Delta A_n$ and choose a point $(x_i, y_i)$ in each. The **double integral** of $f$ over $R$ is

$$\iint_R f(x, y) \, dA \;=\; \lim_{\max \Delta A_i \to 0} \; \sum_{i=1}^{n} f(x_i, y_i) \, \Delta A_i ,$$

and for continuous $f$ the limit exists and does not depend on how the cutting is done. A **triple integral** $\iiint_V f \, dV$ is the same construction with small volumes.

### Intuitive

**A quantity that varies from place to place, added up over the whole place.**

| If $f(x, y)$ is | then $\iint_R f \, dA$ is |
|---|---|
| height of a surface | volume under it |
| $1$ | the area of $R$ |
| mass per unit area | total mass |
| rainfall depth | total volume of water |
| probability density of $(X, Y)$ | the probability that $(X, Y)$ lands in $R$ |

Only the first row is a volume. The double integral is the sum; "volume" is one reading of it.

### 中文锚点 (Chinese Anchor)

天气预报说昨天下了五十毫米的雨。这说的是一个深度，是某一个雨量计测出来的。那么整座城市到底落下了多少水？如果各处的雨下得一样大，拿深度乘以城市的面积就完事了。可从来不是这样：城西大雨倾盆，城东几乎没落几滴。于是你把地图切成许多小方格，每一格小到格子里的雨差不多是均匀的，把每一格的深度乘以它的面积，再全部加起来。格子切得越细，这个和就越接近真实的水量，它最后稳下来的那个值，就是二重积分。把一整张地图的格子加起来，听上去没完没了，其实你会像数礼堂里的座位那样去做：先顺着一排数完，得到这一排的总数，再把各排的总数加起来。积分里面套一个积分，说的就是这件事：先沿着一条长条加到底，再把一条条的总数加起来。

## Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $\iint_R f \, dA$ | "the double integral of $f$ over $R$" | the limit of sums above; no order of integration implied |
| $dA$ | "dee A" | a small piece of area: $dx\,dy$ in Cartesian, $r\,dr\,d\theta$ in polar |
| $\displaystyle\int_a^b \!\! \int_{g(x)}^{h(x)} f \, dy \, dx$ | "integrate in $y$ first, then in $x$" | an **iterated** integral; work from the inside out |
| $dV$ | "dee V" | a small piece of volume |
| $\dfrac{\partial(x, y)}{\partial(u, v)}$ or $J$ | "the Jacobian" | the determinant of the four partial derivatives of $x, y$ with respect to $u, v$ |

The differentials are read from the inside out and the integral signs from the outside in, so in $\int_a^b \int_c^d f \, dy \, dx$ the limits $c, d$ belong to $y$ and $a, b$ belong to $x$.

## Slicing — a double integral is two single integrals

A loaf of bread has a volume you can find by slicing: if the slice at position $x$ has face area $A(x)$, then $V = \int A(x)\,dx$. That is the ordinary idea of [[Integration]]. Now look at one slice of the solid under $z = f(x, y)$. Holding $x$ fixed, its face is the region under the curve $z = f(x, y)$ regarded as a function of $y$ alone, so

$$A(x) = \int_c^d f(x, y) \, dy, \qquad\text{and therefore}\qquad \iint_R f \, dA = \int_a^b \left( \int_c^d f(x, y)\,dy \right) dx .$$

The inner integral treats $x$ as a constant, exactly as a partial derivative does. This is **partial integration**, the reverse of the partial differentiation you already know.

For the surface in the figure:

$$A(x) = \int_0^1 (4 - x^2 - y^2)\,dy = \Big[ 4y - x^2 y - \tfrac13 y^3 \Big]_0^1 = \tfrac{11}{3} - x^2, \qquad \int_0^1 \left(\tfrac{11}{3} - x^2\right) dx = \tfrac{11}{3} - \tfrac13 = \tfrac{10}{3}.$$

Two lines, against a million columns. Slicing the other way, with $y$ fixed first, must give the same volume, since it is the same loaf. That is **Fubini's theorem**: for a continuous function on a bounded region, the two iterated integrals are equal, and both equal the double integral.

## When the ground is not a rectangle

Most regions are not rectangles, and then the limits carry the shape. Take the triangle with corners $(0,0)$, $(1,1)$ and $(0,1)$, the part of the unit square above the line $y = x$.

![[multiple-integrals-two-orders.svg|820]]

**Vertical strips.** Fix $x$ and let $y$ run. The strip enters the region at the line, $y = x$, and leaves at the top edge, $y = 1$. Those are the inner limits. The strips themselves are needed for every $x$ from $0$ to $1$:

$$\iint_R f \, dA = \int_0^1 \!\! \int_x^1 f(x, y) \, dy \, dx .$$

**Horizontal strips.** Fix $y$ and let $x$ run. The strip enters at $x = 0$ and leaves at the line, where $x = y$:

$$\iint_R f \, dA = \int_0^1 \!\! \int_0^y f(x, y) \, dx \, dy .$$

Three rules come out of the picture, and they never fail.

1. **Draw the region first.** Limits are read off a sketch, never off the algebra.
2. **The outer limits are numbers.** The final answer is a number, so the last integration cannot leave a variable behind.
3. **The inner limits may depend on the outer variable, and on nothing else.** They are where the strip enters and where it leaves.

![[multiple-integrals-sweep-two-ways.mp4]]

The clip sweeps both kinds of strip across the region between $y = x^2$ and $y = x$. Watch the two ends: they ride along the boundary curves, and the curves they ride on are the inner limits.

If you program, you have met this already. In a nested loop the inner loop's range may depend on the outer counter and never the other way round, and a triangular loop `for i in range(n): for j in range(i + 1)` runs $\tfrac12 n(n+1)$ times, which for large $n$ is the area of a triangle, $\tfrac12 n^2$. For $n = 1000$ the two differ by one part in a thousand. **A nested loop is a double sum, and a double integral is what the double sum becomes when the steps shrink to nothing.**

## Changing the order

Since both orders give the same number, you may pick the easier one, and sometimes only one of them can be done at all.

$$I = \int_0^1 \!\! \int_x^1 e^{y^2} \, dy \, dx$$

The inner integral asks for an antiderivative of $e^{y^2}$, and there is none among the elementary functions. But the limits describe exactly the triangle above: $x \le y \le 1$ for $0 \le x \le 1$. Describe it by horizontal strips instead:

$$I = \int_0^1 \!\! \int_0^y e^{y^2} \, dx \, dy = \int_0^1 y \, e^{y^2} \, dy = \Big[ \tfrac12 e^{y^2} \Big]_0^1 = \frac{e - 1}{2} \approx 0.8591 .$$

Integrating in $x$ first supplied the factor $y$ that the substitution $u = y^2$ needed. A numerical integration in the *original* order gives $0.8591409142$, the same to ten figures.

**Changing the order is not swapping the limits.** $\int_0^1 \int_x^1 \dots dy\,dx$ does not become $\int_x^1 \int_0^1 \dots dx\,dy$, which has a variable in an outer limit and is meaningless. The procedure is always: turn the limits into a picture, then read the picture the other way.

## Polar coordinates, and where the extra $r$ comes from

A disc is awkward in $x$ and $y$: its limits are $\pm\sqrt{R^2 - x^2}$. In [[Polar Coordinates]] it is a rectangle, $0 \le r \le R$ and $0 \le \theta \le 2\pi$. The price is that a polar grid is not made of equal pieces.

![[multiple-integrals-polar-patch.svg|820]]

A patch between $r$ and $r + dr$, and between $\theta$ and $\theta + d\theta$, is nearly a rectangle. One side is $dr$. The other is an arc of radius $r$ and angle $d\theta$, which has length $r\,d\theta$. So

$$dA = r \, dr \, d\theta .$$

This can be checked exactly. The patch is the difference of two sectors: $\tfrac12 (r + dr)^2 d\theta - \tfrac12 r^2 d\theta = r\,dr\,d\theta + \tfrac12 (dr)^2 d\theta$. The second term is a product of three small quantities and vanishes in the limit.

**The $r$ is not optional.** Without it, $\int_0^{2\pi}\!\int_0^R dr\,d\theta = 2\pi R$, a length, where the area of a disc should be. With it, $\int_0^{2\pi}\!\int_0^R r\,dr\,d\theta = \pi R^2$.

### The integral that cannot be done, done

The bell curve of the [[Normal Distribution]] needs the value of $I = \int_{-\infty}^{\infty} e^{-x^2}\,dx$, and $e^{-x^2}$ has no elementary antiderivative. Recall that [[Normal Distribution]] sketches the way round; here is the whole of it. Multiply $I$ by a copy of itself written with a different letter:

$$I^2 = \int_{-\infty}^{\infty} e^{-x^2}dx \int_{-\infty}^{\infty} e^{-y^2}dy = \iint_{\text{plane}} e^{-(x^2 + y^2)} \, dA .$$

The integrand depends on $x^2 + y^2 = r^2$ alone, so go to polar, and the Jacobian's $r$ is precisely the factor that was missing:

$$I^2 = \int_0^{2\pi}\!\! \int_0^{\infty} e^{-r^2} \, r \, dr \, d\theta = 2\pi \Big[ -\tfrac12 e^{-r^2} \Big]_0^{\infty} = \pi, \qquad\text{so}\qquad \int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi} \approx 1.7725 .$$

Rescaling, $\int_{-\infty}^{\infty} e^{-z^2/2}\,dz = \sqrt{2\pi}$, which is why the standard normal density carries $\dfrac{1}{\sqrt{2\pi}}$. **The $\pi$ in every statistics table is there because of a circle in a plane that the original problem never mentioned.**

## Any change of variables — the Jacobian

Polar coordinates are one example of a general move. Suppose new variables are introduced by $x = x(u, v)$, $y = y(u, v)$. A small rectangle $du \times dv$ in the $uv$-plane is carried to a small, nearly parallelogram-shaped patch in the $xy$-plane. Its sides are the vectors $\left(\tfrac{\partial x}{\partial u}, \tfrac{\partial y}{\partial u}\right) du$ and $\left(\tfrac{\partial x}{\partial v}, \tfrac{\partial y}{\partial v}\right) dv$, by the small-change formula. The area of a parallelogram is the absolute value of the determinant of its side vectors, which is what [[Determinants and Inverses]] shows a determinant *is*. Hence

$$dA = \lvert J \rvert \, du \, dv, \qquad J = \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\[2mm] \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{vmatrix},$$

$$\iint_R f(x, y)\,dx\,dy = \iint_{R'} f\big(x(u,v),\, y(u,v)\big)\, \lvert J \rvert \, du\,dv .$$

**The Jacobian is the local area-scale factor of the map.** It is the two-dimensional form of the $\dfrac{dx}{du}$ in [[Integration by Substitution]].

- **Polar:** $x = r\cos\theta$, $y = r\sin\theta$ gives $J = \cos\theta \cdot r\cos\theta - (-r\sin\theta)\sin\theta = r$. The picture and the determinant agree.
- **Stretching:** $x = au$, $y = bv$ gives $J = ab$, a constant. The unit disc $u^2 + v^2 \le 1$ maps to the ellipse $\tfrac{x^2}{a^2} + \tfrac{y^2}{b^2} \le 1$, so **the area of an ellipse is $\pi ab$**, with no integration at all.
- **Rotating and shrinking:** $u = x + y$, $v = x - y$, that is $x = \tfrac12(u + v)$, $y = \tfrac12(u - v)$, gives $J = -\tfrac12$ and $\lvert J \rvert = \tfrac12$.

![[multiple-integrals-jacobian.svg|820]]

The absolute value matters. A negative determinant means the map flips orientation, as a mirror does. Area is still positive.

## Three dimensions

A triple integral adds a quantity over a solid, and it is evaluated as three nested single integrals by the same rules: draw the solid, outer limits are numbers, each inner limit may depend only on the variables outside it. Two coordinate systems do most of the work.

| System | Variables | $dV$ | Use when |
|---|---|---|---|
| Cartesian | $x, y, z$ | $dx\,dy\,dz$ | boxes, regions between planes |
| Cylindrical | $r, \theta, z$ | $r\,dr\,d\theta\,dz$ | symmetry about an axis: pipes, cones, discs |
| Spherical | $\rho, \phi, \theta$ | $\rho^2 \sin\phi \, d\rho\, d\phi\, d\theta$ | symmetry about a point: balls, stars, atoms |

Here $\rho$ is the distance from the origin, $\phi$ is the angle down from the positive $z$-axis ($0$ to $\pi$), and $\theta$ is the angle round the $z$-axis ($0$ to $2\pi$). **Physics texts usually swap the two Greek letters.** Check which angle is measured from the axis before using anyone's formula. The factor comes from a small box with sides $d\rho$, $\rho\,d\phi$ and $\rho\sin\phi\,d\theta$; the last is an arc of a circle of radius $\rho\sin\phi$, the distance from the axis. The $3 \times 3$ Jacobian determinant gives the same $\rho^2\sin\phi$.

The volume of a ball is then three separate one-line integrals:

$$V = \int_0^{2\pi}\!\! d\theta \int_0^{\pi}\! \sin\phi \, d\phi \int_0^R \rho^2 \, d\rho = 2\pi \cdot 2 \cdot \frac{R^3}{3} = \frac{4}{3}\pi R^3 .$$

## Where this is the working tool

- **Every normal-distribution table.** The constant $\tfrac{1}{\sqrt{2\pi}}$ was computed above by a double integral, and there is no other elementary way to get it.
- **How much a catchment collected.** Hydrologists turn point readings from rain gauges into a total volume over a river basin, which is a double integral of depth over the basin's area, done numerically on a grid. Flood warnings depend on the result.
- **Mass properties in engineering.** A CAD package reports the mass, centre of mass and moments of inertia of a part. Each is a triple integral of density, or density times position, or density times distance squared, over the part. [[Centres of Mass by Integration]] and [[Moment of Inertia]] do the versions that symmetry reduces to a single integral; Examples 4 and 6 do two of them directly.
- **Two uncertain quantities at once.** If $X$ and $Y$ have joint density $f(x, y)$, every probability about them is a double integral over a region. For two independent random numbers between $0$ and $1$, $P(X + Y < 1)$ is the area of a triangle, $\tfrac12$, and $P(XY < \tfrac12) = \tfrac12 + \tfrac12\ln 2 \approx 0.847$, the area under a hyperbola. [[Continuous Random Variables]] is the one-variable case.
- **Rendering.** The brightness of one pixel in a film-quality image is an integral of incoming light over a hemisphere of directions, nested inside integrals over the lens and over time. Nobody does these exactly; see the last section.

## Worked Examples

### Example 1: a rectangle, both ways

> Evaluate $\displaystyle\iint_R x y^2 \, dA$ over $0 \le x \le 2$, $1 \le y \le 3$.

*Trigger: a rectangle, and an integrand that is a product of a function of $x$ and a function of $y$. Tool: iterated integration; on a rectangle such a product separates.*

$$\int_0^2 \!\! \int_1^3 x y^2 \, dy\, dx = \int_0^2 x \Big[ \tfrac13 y^3 \Big]_1^3 dx = \frac{26}{3} \int_0^2 x \, dx = \frac{26}{3} \cdot 2 = \frac{52}{3} .$$

The other order gives $\int_1^3 y^2 \big[\tfrac12 x^2\big]_0^2 \, dy = 2 \cdot \tfrac{26}{3} = \tfrac{52}{3}$. In fact $\iint g(x)h(y)\,dA = \int g \cdot \int h$ whenever the region is a rectangle. It is false for any other region.

### Example 2: limits from a sketch

> Evaluate $\displaystyle\iint_R (x + 2y) \, dA$ over the triangle with corners $(0,0)$, $(1,0)$ and $(0,2)$.

*Trigger: a region bounded by a sloping line. Tool: sketch, choose a strip direction, read the entry and exit.*

The sloping side is $y = 2 - 2x$. A vertical strip at $x$ enters at $y = 0$ and leaves at $y = 2 - 2x$:

$$\int_0^1 \!\! \int_0^{2 - 2x} (x + 2y) \, dy \, dx = \int_0^1 \Big[ xy + y^2 \Big]_0^{2-2x} dx = \int_0^1 (2x^2 - 6x + 4)\,dx = \frac23 - 3 + 4 = \frac53 .$$

Horizontal strips run from $x = 0$ to $x = 1 - \tfrac12 y$ for $0 \le y \le 2$, and also give $\tfrac53$. As a check on the limits alone, integrating $1$ over the same limits gives $1$, the triangle's area.

### Example 3: the order that works

> Evaluate $\displaystyle\int_0^{\pi} \!\! \int_y^{\pi} \frac{\sin x}{x} \, dx \, dy$.

*Trigger: an inner integral with no elementary antiderivative. Tool: change the order.*

The limits say $y \le x \le \pi$ for $0 \le y \le \pi$: the triangle below the line $y = x$, out to $x = \pi$. By vertical strips, $y$ runs from $0$ to $x$:

$$\int_0^{\pi} \!\! \int_0^{x} \frac{\sin x}{x} \, dy \, dx = \int_0^{\pi} \frac{\sin x}{x} \cdot x \, dx = \int_0^{\pi} \sin x \, dx = 2 .$$

### Example 4: a disc, and the moment of inertia

> A uniform disc has mass $M$ and radius $R$. Find its moment of inertia about the axis through its centre, perpendicular to its plane.

*Trigger: a circular region, and an integrand, distance squared from the centre, that is $r^2$. Tool: polar coordinates with $dA = r\,dr\,d\theta$.*

The mass per unit area is $\sigma = M / \pi R^2$. Each patch contributes (its mass) $\times$ (distance)$^2 = \sigma\,dA \cdot r^2$:

$$I = \int_0^{2\pi}\!\! \int_0^R \sigma \, r^2 \cdot r \, dr \, d\theta = 2\pi\sigma \cdot \frac{R^4}{4} = \frac{M}{\pi R^2}\cdot\frac{\pi R^4}{2} = \frac12 M R^2 ,$$

as [[Moment of Inertia]] finds with rings. A ring *is* the inner integral over $\theta$ done in your head. The same method gives the centre of mass of a semicircular plate: $\bar y = \dfrac{1}{\frac12\pi R^2}\int_0^{\pi}\!\int_0^R (r\sin\theta)\, r\,dr\,d\theta = \dfrac{4R}{3\pi} \approx 0.424R$.

### Example 5: the hill

> Find the volume of the hill $h = 400 - 0.001x^2 - 0.002y^2$ above the plain $h = 0$.

*Trigger: an elliptical footprint. Tool: a stretch to turn the ellipse into a circle, then polar.*

The footprint $h \ge 0$ is the ellipse $\dfrac{x^2}{A^2} + \dfrac{y^2}{B^2} \le 1$ with $A = \sqrt{400/0.001} \approx 632.5$ m and $B = \sqrt{400/0.002} \approx 447.2$ m. Put $x = Au$, $y = Bv$. Then $\lvert J \rvert = AB$, the footprint becomes the unit disc, and the height becomes $400(1 - u^2 - v^2)$. In polar coordinates on the $uv$-plane:

$$V = AB \int_0^{2\pi}\!\! \int_0^1 400(1 - r^2)\, r \, dr \, d\theta = AB \cdot 2\pi \cdot 400\left(\tfrac12 - \tfrac14\right) = 200\pi AB \approx 1.78 \times 10^8 \text{ m}^3 .$$

Two changes of variable were composed, and their Jacobians multiplied. The answer is half of (base area $\times$ height): the footprint covers $0.889$ km$^2$, the mean height is $200$ m, and at $1.8$ tonnes per cubic metre the hill weighs about $320$ million tonnes. A direct numerical integration in $x$ and $y$ over the ellipse gives the same $1.7772 \times 10^8$.

### Example 6: a solid sphere

> Find the moment of inertia of a uniform solid sphere of mass $M$ and radius $R$ about a diameter.

*Trigger: a ball. Tool: spherical coordinates, taking care that the distance that matters is from the **axis**, not from the centre.*

Take the $z$-axis as the diameter. A point's distance from that axis is $\rho\sin\phi$. With density $\delta = M / \tfrac43\pi R^3$:

$$I = \int_0^{2\pi}\!\! \int_0^{\pi}\!\! \int_0^R \delta \, (\rho\sin\phi)^2 \, \rho^2 \sin\phi \, d\rho\, d\phi\, d\theta = \delta \cdot 2\pi \cdot \int_0^{\pi}\sin^3\phi\,d\phi \cdot \frac{R^5}{5} .$$

Since $\int_0^{\pi}\sin^3\phi\,d\phi = \tfrac43$, this is $\delta \cdot \dfrac{8\pi R^5}{15} = \dfrac{3M}{4\pi R^3}\cdot\dfrac{8\pi R^5}{15} = \dfrac25 MR^2$. Using $\rho^2$ in place of $(\rho\sin\phi)^2$ gives $\tfrac35 MR^2$, which is a common wrong answer and measures something else.

## Common Misconceptions (Teaching Notes)

### 1. Forgetting the $r$
$dx\,dy$ does not become $dr\,d\theta$. The pieces of a polar grid grow with $r$, and $dA = r\,dr\,d\theta$. The quickest test is the units: $dr\,d\theta$ is a length, not an area.

### 2. A variable in an outer limit
$\int_0^x \int_0^1 f \, dy\,dx$ cannot be right, because its value would still contain $x$. Outer limits are numbers. Inner limits may involve outer variables, and never the reverse.

### 3. "To change the order, swap the integral signs and their limits"
That works only for a rectangle. For any other region the limits change completely, and they are found from a sketch: see the triangle above, where $\int_0^1\!\int_x^1$ became $\int_0^1\!\int_0^y$.

### 4. "A double integral is a volume"
It is a sum of $f \, dA$. It is a volume when $f$ is a height, a mass when $f$ is a density, a probability when $f$ is a probability density, and an area when $f = 1$. Where $f$ is negative the contribution is negative, exactly as for a single integral.

### 5. "The Jacobian can come out negative, so the area is negative"
The determinant can be negative; the scale factor is its absolute value. Dropping the bars turns a correct answer into its negative.

### 6. Using the wrong distance in spherical coordinates
$\rho$ is the distance from the origin. The distance from the $z$-axis is $\rho\sin\phi$. Moments of inertia need the second, gravitational potential at the centre needs the first.

### 7. "The order never matters"
For continuous functions on bounded regions it never does. It can matter for integrals that are improper in a way that is not absolutely convergent; the last section has the standard example. Every integral a physics or statistics course meets is safe.

## Exam Notes

### Where this is *not* examined
No school syllabus in these notes examines multiple integrals. A text search of the Cambridge 9709 and 9231 syllabuses and of the AP Calculus AB and BC course description for "double integral", "multiple integral", "iterated" and "Jacobian" finds nothing in any of them. The IB Mathematics: Analysis and Approaches guide is not held on file for the same search; its calculus topics are single-variable. AP Physics C sets up integrals over extended bodies, and reduces every one to a single integral by symmetry.

### Where school courses lean on it without naming it
- **Volumes of revolution** (9709 Pure 1, AP Calculus): the disc formula $\pi\int y^2\,dx$ is a triple integral in cylindrical coordinates with the two inner integrals, over $\theta$ and $r$, already done.
- **Centres of mass of laminas** (9231 Further Mechanics, which quotes the standard results and states that proofs are not required) and **moments of inertia** (AP Physics C: Mechanics): the strips, rings and shells are inner integrals done by symmetry.
- **The normal distribution** (9709 Probability and Statistics 1, AP Statistics): the constant $\tfrac{1}{\sqrt{2\pi}}$.
- **Polar areas** (9231 Further Pure 1): $\tfrac12\int r^2\,d\theta$ is $\iint r\,dr\,d\theta$ with the inner integral done.

### Beyond high school — University
This is the second topic of any multivariable calculus course, directly after partial derivatives. What follows it is [[Vector Calculus]], where integrals are taken along curves and over curved surfaces, and the theorems of Green, Stokes and Gauss relate them to the double and triple integrals here.

## Beyond the syllabus

> [!info] When the order does matter
> Recall Fubini's theorem: the two iterated integrals agree for a continuous function on a bounded region. Drop the hypothesis and it can fail. On the unit square, $f(x, y) = \dfrac{x^2 - y^2}{(x^2 + y^2)^2}$ is unbounded near the origin, and
> $$\int_0^1\!\!\int_0^1 f \, dy\,dx = \frac{\pi}{4}, \qquad \int_0^1\!\!\int_0^1 f \, dx\,dy = -\frac{\pi}{4}.$$
> Swapping $x$ and $y$ changes the sign of $f$, which is why the two answers are negatives of each other. The safe condition is that $\iint \lvert f \rvert \, dA$ be finite, and here it is not: the positive and negative parts are each infinite.

> [!info] Integrals nobody can do: throw darts
> Recall that an integral is an average value times the size of the region. So estimate the average by sampling. Scatter $N$ random points over the square $-1 \le x, y \le 1$ and count the fraction inside the unit circle; that fraction times $4$ estimates $\pi$. With $1{,}000$ points one run gave $3.116$; with $100{,}000$, $3.150$; with ten million, $3.1409$. The error shrinks like $1/\sqrt{N}$, which is slow, but **it does not depend on the number of dimensions**, and a grid does: ten points per axis is $10^d$ points in $d$ dimensions. A rendered frame of film is an integral over dozens of dimensions per pixel, and this **Monte Carlo** method is the only one that works.

> [!info] The ball that disappears
> Recall the volume of a ball from the triple integral above. The same calculation in $n$ dimensions gives the unit ball a volume of $\dfrac{\pi^{n/2}}{\Gamma(n/2 + 1)}$: $2$, $3.14$, $4.19$, $4.93$, **$5.26$ at $n = 5$**, then $5.17$, $4.72$, and down to $0.026$ at $n = 20$. The ball's share of the cube that just contains it falls from $79\,\%$ in the plane to $0.25\,\%$ in ten dimensions and $2.5 \times 10^{-8}$ in twenty. In high dimensions nearly all of a cube is in its corners, which is one reason data with many features behaves so strangely.

## Connections

- **Prerequisites:** [[Integration]], [[Partial Derivatives and the Gradient]] (holding one variable fixed; the small-change formula), [[Integration by Substitution]] (the one-dimensional Jacobian), [[Polar Coordinates]], [[Determinants and Inverses]] (a determinant as an area-scale factor), [[Matrix Transformations]].
- **The single-integral versions:** [[Centres of Mass by Integration]], [[Moment of Inertia]], [[Continuous Random Variables]], [[Normal Distribution]].
- **The discrete version:** [[Summation of Series]] (double sums), [[Big-O Notation]] (counting the runs of nested loops).
- **Extensions:** [[Vector Calculus]], [[Maxwell's Equations]] (whose integral forms are surface and volume integrals), [[Gravitational Fields]] and [[Electric Field]] (the field of an extended body is a triple integral over it).

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\iint_R f \, dA$ | `\iint_R f \, dA` | Double integral over a region |
| $\iiint_V f \, dV$ | `\iiint_V f \, dV` | Triple integral |
| $\int_a^b \!\! \int_{g(x)}^{h(x)} f \, dy\, dx$ | `\int_a^b \!\! \int_{g(x)}^{h(x)} f \, dy\, dx` | Iterated integral; `\!\!` closes the gap between the signs |
| $r \, dr \, d\theta$ | `r \, dr \, d\theta` | Polar area element |
| $\rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$ | `\rho^2 \sin\phi \, d\rho \, d\phi \, d\theta` | Spherical volume element |
| $\dfrac{\partial(x, y)}{\partial(u, v)}$ | `\dfrac{\partial(x, y)}{\partial(u, v)}` | Jacobian determinant |
| $\lvert J \rvert$ | `\lvert J \rvert` | Its absolute value; use `\lvert` inside tables |
| $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ | `\begin{vmatrix} a & b \\ c & d \end{vmatrix}` | Determinant bars |
