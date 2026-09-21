---
chinese: 偏导数与梯度 (piān dǎoshù yǔ tīdù)
prerequisites:
  - "[[Differentiation]]"
  - "[[Chain Rule]]"
  - "[[Vectors]]"
  - "[[3D Vectors and the Scalar Product]]"
  - "[[Stationary Points]]"
leads_to:
  - "[[Multiple Integrals]]"
  - "[[Vector Calculus]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/university
  - type/definition
  - type/theorem
  - type/proof
  - type/visual-tool
  - notation/partial-derivative
  - notation/nabla
  - misconception/gradient-points-at-the-summit
  - misconception/partials-cancel-like-fractions
  - misconception/zero-partials-means-extremum
  - misconception/partials-exist-means-differentiable
  - misconception/steepest-descent-is-fastest
---

# Partial Derivatives and the Gradient 偏导数与梯度

## The question — how steep is a hillside?

A curve has one slope at each point, and [[Differentiation]] finds it. A hillside does not. Stand at one spot and walk along the path that circles the hill: the ground is level. Turn and face straight up the slope: it is as steep as it gets. Every direction in between gives something in between. "The slope here" is not a number until you say which way you are walking.

Almost every quantity worth studying is like the hillside, because it depends on more than one thing. The height of the ground depends on how far east and how far north you are. The pressure of a gas depends on its temperature and its volume. The error of a neural network depends on millions of weights. For all of them the question "how fast does it change?" needs the same repair.

The repair is in two steps. First, ask the easy question several times: change **one** input, hold the others still, and take an ordinary derivative. Those are the **partial derivatives**. Second, discover that these few numbers, collected into one arrow called the **gradient**, already contain the slope in *every* direction, and point the steepest way up.

## Definition

### Formal

Let $f(x, y)$ be a function of two variables. Its **partial derivatives** at the point $(a, b)$ are

$$\frac{\partial f}{\partial x}(a, b) = \lim_{s \to 0} \frac{f(a + s,\, b) - f(a, b)}{s}, \qquad \frac{\partial f}{\partial y}(a, b) = \lim_{s \to 0} \frac{f(a,\, b + s) - f(a, b)}{s},$$

when the limits exist. The **gradient** of $f$ is the vector made of them:

$$\nabla f = \begin{pmatrix} \partial f/\partial x \\ \partial f/\partial y \end{pmatrix}.$$

The **directional derivative** of $f$ at $(a,b)$ in the direction of a **unit** vector $\mathbf u = (u_1, u_2)$ is the rate of change of $f$ per unit distance travelled along $\mathbf u$:

$$D_{\mathbf u} f(a, b) = \lim_{s \to 0} \frac{f(a + s u_1,\, b + s u_2) - f(a, b)}{s}.$$

With three or more variables nothing changes except the number of components.

### Intuitive

Look at the first limit. Only $x$ moves; $y$ is stuck at $b$. So $\partial f/\partial x$ is the ordinary derivative of the one-variable function $x \mapsto f(x, b)$. Geometrically, you have cut the surface with a vertical plane running east–west and are measuring the slope of the curve where the plane meets it.

**That is the whole computing rule: to find $\partial f/\partial x$, treat every other variable as a constant and differentiate as usual.** It is not a trick. Holding $y$ still is exactly what the definition says.

One hill serves as the running example from here to the end. Its height in metres, at a point $x$ metres east and $y$ metres north of the summit, is

$$h(x, y) = 400 - 0.001x^2 - 0.002y^2,$$

and a hiker stands at $P(100, 50)$, where $h = 400 - 10 - 5 = 385$ m. Holding $y$ still, $\partial h/\partial x = -0.002x$, which is $-0.2$ at $P$: walking east, the ground falls 0.2 m for every metre walked. Holding $x$ still, $\partial h/\partial y = -0.004y$, also $-0.2$ at $P$.

![[partial-derivatives-slices.svg|820]]
*The hill from above, as a contour map: each closed curve joins points of equal height. The blue line is the walk due east through $P$ and the purple line the walk due north. Below, the ground profile along each walk. Each profile is an ordinary curve, and its tangent slope at $P$ is a partial derivative.*

### 中文锚点 (Chinese Anchor)

拿着地图站在山坡上，问一句“这里有多陡”，其实没有唯一的答案：沿着绕山的小路走，脚下是平的；转身正对着坡往上走，陡到不能再陡；朝其他方向走，陡的程度就在两者之间。所以曲面上的“坡度”不是一个数。办法其实很简单，把一个容易的问题问两遍：只往正东走，地面升得多快？只往正北走，又升得多快？这两个都是普通的斜率，因为每次只有一样东西在变，这就是**偏导数**。把这两个数并在一起，在地图上画成一支箭头，这就是**梯度**，它已经知道了一切：箭头指的是最陡的上坡方向，箭头的长度就是那个方向有多陡，朝别的方向走时，坡度有多大，就看你这一步有多少落在箭头的方向上。水不用学微积分也懂这个道理：它永远逆着箭头的方向流，所以溪流穿过等高线时总是与它垂直。

## Notation

| Written | Read | Meaning |
|---|---|---|
| $\dfrac{\partial f}{\partial x}$, $f_x$ | "partial $f$ by partial $x$", "$f$ sub $x$" | derivative in $x$, all other variables held still |
| $\partial$ | "partial", or "curly d" | used instead of $d$ whenever there is more than one variable to choose from |
| $\nabla f$, $\operatorname{grad} f$ | "grad $f$", "del $f$" | the vector of partial derivatives |
| $D_{\mathbf u} f$ | "the derivative of $f$ along $\mathbf u$" | slope in the direction of the unit vector $\mathbf u$ |
| $f_{xy}$, $\dfrac{\partial^2 f}{\partial y\, \partial x}$ | "$f$ sub $x$ $y$" | differentiate in $x$ first, then in $y$ |

The curly $\partial$ carries a warning that the straight $d$ does not: *something else was held still, and the answer depends on what.* Thermodynamics makes this explicit by writing the held variable outside a bracket, as in $\left(\dfrac{\partial P}{\partial V}\right)_T$.

## The small-change formula

Everything that follows is a consequence of one formula. Move from $(x, y)$ to $(x + \Delta x,\, y + \Delta y)$. Then

$$\boxed{\Delta f \approx \frac{\partial f}{\partial x}\,\Delta x + \frac{\partial f}{\partial y}\,\Delta y}$$

with an error that shrinks faster than the step itself. In words: **the effects of the separate changes add.**

**Why it is true.** Make the move in two legs, east first and then north:

$$\Delta f = \underbrace{\big[f(x + \Delta x,\, y) - f(x, y)\big]}_{\text{east leg: only } x \text{ changes}} + \underbrace{\big[f(x + \Delta x,\, y + \Delta y) - f(x + \Delta x,\, y)\big]}_{\text{north leg: only } y \text{ changes}}.$$

On each leg only one variable changes, so each bracket is a one-variable problem, and the [[Mean Value Theorem]] applies to it: the east leg equals $f_x$ evaluated somewhere along that leg, times $\Delta x$, and the north leg equals $f_y$ evaluated somewhere along that leg, times $\Delta y$. If $f_x$ and $f_y$ are **continuous**, then "somewhere along a short leg" differs from "at the starting point" by an amount that vanishes as the step shrinks. Replace both by their values at $(x, y)$ and the boxed formula appears, with an error that is a vanishing fraction of the step length.

**What it is worth, on the hill.** From $P$ walk 3 m east and 4 m north. The formula predicts $\Delta h \approx (-0.2)(3) + (-0.2)(4) = -1.40$ m. The exact change is $-1.441$ m. Now take a step ten times longer, 30 m east and 40 m north: the formula says $-14.0$ m, the truth is $-18.1$ m. The step grew tenfold and the error a hundredfold, from 0.041 m to 4.1 m. The formula is a statement about small steps, and it says so.

Written about a fixed point $(a, b)$, the approximation reads $f(x, y) \approx f(a,b) + f_x\,(x - a) + f_y\,(y - b)$, and its right-hand side is the equation of a plane: the **tangent plane**, the flat sheet that best fits the surface at the point, exactly as a tangent line best fits a curve in [[Tangents and Normals]].

> [!info] This is the master rule of error propagation
> Read $\Delta x$ and $\Delta y$ as the uncertainties in two measurements and the formula tells you the uncertainty in anything computed from them. [[Error Propagation]] is built on exactly this line, with absolute values added so that the errors cannot cancel.

## Every direction at once — the directional derivative

Walk a small distance $s$ from $(x, y)$ in the direction of a unit vector $\mathbf u = (u_1, u_2)$. Then $\Delta x = s u_1$ and $\Delta y = s u_2$, so by the small-change formula

$$\Delta f \approx f_x\, s u_1 + f_y\, s u_2 .$$

Divide by $s$ and let $s \to 0$:

$$\boxed{D_{\mathbf u} f = f_x u_1 + f_y u_2 = \nabla f \cdot \mathbf u}$$

Two numbers, measured along east and north only, give the slope in all 360 degrees. The right-hand side is a scalar product from [[3D Vectors and the Scalar Product]], and that is where the geometry comes from.

## The gradient — what the arrow means

Since $\mathbf u$ has length 1, the scalar product is

$$D_{\mathbf u} f = \lvert \nabla f \rvert \cos\theta,$$

where $\theta$ is the angle between your walking direction and $\nabla f$. Read off three facts:

1. **The slope is greatest when $\theta = 0$.** The gradient points in the direction of steepest ascent.
2. **That greatest slope equals $\lvert \nabla f \rvert$.** The length of the arrow is how steep the steepest way is.
3. **The slope is zero when $\theta = 90°$.** Perpendicular to the gradient, $f$ is not changing: you are walking along a contour. So **the gradient is perpendicular to the contour through the point.**

On the hill, $\nabla h = (-0.2, -0.2)$ at $P$. It points south-west, its length is $\sqrt{0.08} = 0.283$, so the steepest climb from $P$ rises 0.283 m per metre, an angle of $\tan^{-1} 0.283 = 15.8°$. Walking north-east, directly against the arrow, is the steepest way down, at $-0.283$. Walking north-west or south-east, at right angles to it, keeps you level.

![[partial-derivatives-directional.svg|820]]
*The slope a walker feels at $P$ as the walking direction turns through a full circle. It is a cosine curve: greatest along $\nabla h$, equally negative against it, zero at right angles, and $-0.2$ in the two directions where the partial derivatives were measured.*

**A second proof of fact 3**, which does not need the cosine. Let $\mathbf r(t) = (x(t), y(t))$ be any path that stays on one contour, so $f(x(t), y(t)) = c$ for all $t$. Differentiate both sides with respect to $t$, using the chain rule for several variables, derived just below: $f_x x' + f_y y' = 0$, which says $\nabla f \cdot \mathbf r'(t) = 0$. The velocity $\mathbf r'$ is tangent to the contour, so the gradient is perpendicular to it.

![[partial-derivatives-gradient-field.svg|820]]
*The gradient drawn at a grid of points on the hill. Every arrow meets its contour at a right angle, and the arrows are longer where the contours are crowded, which is where the ground is steep. The red arrow is $\nabla h$ at $P$. It does not aim at the summit.*

That last sentence of the caption deserves a second look. From $P$ the summit lies in the direction $(-100, -50)$, but the gradient points along $(-1, -1)$, which is $18°$ away. The gradient knows nothing about where the summit is. It reports only which way is steepest *right here*, and on a hill whose contours are ellipses those are different directions. A walker who always follows the gradient does reach the top, by a curved path that crosses every contour squarely.

![[partial-derivatives-compass.mp4]]
*A walking direction turns through a full circle at $P$ while a bar shows the slope felt in that direction. The bar is longest when the direction lines up with the gradient, drops to nothing as the direction swings along the contour, and goes negative beyond it. One arrow, fixed on the map, accounts for every reading.*

## The chain rule with several variables

Suppose the inputs are themselves moving: $x = x(t)$ and $y = y(t)$, so that $f$ becomes a function of $t$ alone. Over a short time $\Delta t$, the small-change formula gives $\Delta f \approx f_x \Delta x + f_y \Delta y$. Divide by $\Delta t$ and let it shrink:

$$\boxed{\frac{df}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} = \nabla f \cdot \mathbf v}$$

where $\mathbf v$ is the velocity of the moving point. This is the [[Chain Rule]] with one extra term per extra variable: $f$ depends on $t$ through two channels, and **the contributions of the channels add**. The final form says the rate of change you experience is your velocity's component along the gradient, times the gradient's length.

**Implicit differentiation falls out.** If a curve is given by $F(x, y) = 0$, then along it $F$ does not change, so $F_x\,dx + F_y\,dy = 0$ and

$$\frac{dy}{dx} = -\frac{F_x}{F_y}.$$

[[Implicit Differentiation]] derives the same formula and uses it as a shortcut; here it is one line.

## Second derivatives, and telling a valley from a pass

Each partial derivative is itself a function of $x$ and $y$, so it can be differentiated again, in either variable. That gives four second derivatives: $f_{xx}$, $f_{yy}$, and the mixed pair $f_{xy}$ and $f_{yx}$.

> [!info] The mixed partials agree
> **Clairaut's theorem.** If $f_{xy}$ and $f_{yx}$ are both continuous near a point, they are equal there. The order in which you differentiate does not matter. For every function built from polynomials, exponentials, logarithms and trigonometric functions, away from points where the formula breaks down, the condition holds. Example 1 checks it on a function where it is not obvious.

At the top of a hill or the bottom of a valley the ground is level in every direction, so $D_{\mathbf u} f = 0$ for every $\mathbf u$, which forces $\nabla f = \mathbf 0$. Points where both partial derivatives vanish are **critical points**. As with [[Stationary Points]] in one variable, a critical point need not be a maximum or a minimum. With two variables there is a new possibility that one variable cannot show: a **saddle**, like a mountain pass, which is a minimum along one direction and a maximum along another.

**The second-derivative test.** At a critical point compute

$$D = f_{xx} f_{yy} - (f_{xy})^2.$$

| | Conclusion |
|---|---|
| $D > 0$ and $f_{xx} > 0$ | local minimum |
| $D > 0$ and $f_{xx} < 0$ | local maximum |
| $D < 0$ | saddle point |
| $D = 0$ | the test cannot decide |

**Why $D$ is the right quantity.** At a critical point the first-order terms are zero, so the change in $f$ for a small step $(a, b)$ is governed by the second-order terms:

$$\Delta f \approx \tfrac12\left(f_{xx}\,a^2 + 2 f_{xy}\,ab + f_{yy}\,b^2\right).$$

Complete the square in $a$ (assuming $f_{xx} \ne 0$):

$$\Delta f \approx \tfrac12 f_{xx}\left[\left(a + \frac{f_{xy}}{f_{xx}}\,b\right)^2 + \frac{D}{f_{xx}^{\,2}}\,b^2\right].$$

If $D > 0$ the bracket is a sum of two squares, positive for every step, so $\Delta f$ has the sign of $f_{xx}$ in every direction: a minimum or a maximum. If $D < 0$ the bracket is a difference of squares, positive for some steps and negative for others: up one way, down another, a saddle.

![[partial-derivatives-critical-points.svg|820]]
*The contours of $f = x^3 - 3x + y^2$ (Example 5). Closed loops surround the minimum. At the saddle the contour through the point crosses itself, and $f$ rises along one axis while falling along the other.*

## Where this is the working tool

**Training a neural network is walking against a gradient.** A network's error $L$ depends on its weights, often billions of them. Training computes $\nabla L$ and moves every weight a small step *against* it, $\mathbf w \leftarrow \mathbf w - \eta \nabla L$, because that is the direction in which the error falls fastest. [[Artificial Intelligence]] runs this on a line fit with two weights and then on a network; the multi-variable chain rule, applied layer by layer, is what is there called back propagation. The step size $\eta$ matters as much as the direction:

![[partial-derivatives-descent.svg|820]]
*Thirty steps of gradient descent on $f = x^2 + 10y^2$, a long narrow valley, from the same start with three step sizes. Each step multiplies $x$ by $1 - 2\eta$ and $y$ by $1 - 20\eta$. At $\eta = 0.02$ both factors are safely below 1 and progress along the valley floor is slow. At $0.09$ the $y$ factor is $-0.8$: the path overshoots the floor each time, zigzags, and still arrives. At $0.11$ it is $-1.2$ and the path is thrown out of the valley.*

The zigzag is the perpendicularity fact at work. In a narrow valley the gradient points almost straight across, not along the floor, because that is where the contours are crowded. Steepest descent is the best *local* direction and can be a poor *global* route, which is why practical optimisers add momentum.

**A field is minus the gradient of a potential.** In [[Electric Potential]], $\mathbf E = -\nabla V$: the electric field points the way the potential falls fastest, and its strength is how fast. The contours of $V$ are the equipotentials, and the field lines cross them at right angles for exactly the reason proved above. Heat does the same: in [[Heat Transfer]], Fourier's law says heat flows along $-\nabla T$, from hot to cold by the steepest route. Water on a hillside runs along $-\nabla h$, which is why streams meet contour lines squarely on every map.

**Edges in a photograph are where the gradient is large.** A greyscale image is a function $I(x, y)$, brightness against position. Inside a plain region $\nabla I \approx \mathbf 0$. At the boundary of an object the brightness jumps, and $\lvert \nabla I \rvert$ is large. Edge detectors compute the two partial derivatives by subtracting neighbouring pixels and keep the places where the gradient is long. On a 200 × 200 test image of a disc and a rectangle, 2.4 % of the pixels have $\lvert \nabla I \rvert > 0.1$, and those pixels trace the two outlines and nothing else.

**Lighting in a game comes from the gradient of a height map.** A terrain is stored as heights $h(x, y)$. To shade it the engine needs the direction the surface faces at each point, its normal vector, and that is $(-h_x, -h_y, 1)$: two partial derivatives, again found by subtracting neighbouring heights. A normal map is this calculation baked into a texture.

**Hands-on.** Run `python3 partial-derivatives-model.py`, the script in the same folder. It computes every number quoted above. Then change the hill to $h = 400 - 0.001x^2 - 0.004y^2$ and predict, before running it, whether the angle between the gradient at $P$ and the line to the summit grows or shrinks.

## Worked Examples

### Example 1: computing partial derivatives, and checking the mixed pair

> Find all first partial derivatives of $f(x, y) = x^2 y + \sin(xy)$, evaluate them at $(1, \pi)$, and verify that $f_{xy} = f_{yx}$.

**Tool: the definition, which says hold the other variable constant.** Trigger: the question says "partial".

Treat $y$ as a constant. Then $x^2 y$ differentiates to $2xy$, and $\sin(xy)$ needs the [[Chain Rule]] with inner function $xy$, whose $x$-derivative is $y$: $f_x = 2xy + y\cos(xy)$.

Treat $x$ as a constant. $f_y = x^2 + x\cos(xy)$.

At $(1, \pi)$: $f_x = 2\pi + \pi\cos\pi = \pi$, and $f_y = 1 + \cos\pi = 0$.

**Tool: differentiate each first derivative in the other variable.**
$f_{xy} = \partial_y\big(2xy + y\cos(xy)\big) = 2x + \cos(xy) - xy\sin(xy)$, using the [[Product Rule]] on $y\cos(xy)$.
$f_{yx} = \partial_x\big(x^2 + x\cos(xy)\big) = 2x + \cos(xy) - xy\sin(xy)$. They agree, as Clairaut's theorem promised.

### Example 2: which measurement matters more?

> A drinks can has radius $r = 3.3$ cm and height $h = 11.5$ cm. Each is increased by 1 mm. Estimate the change in volume, and say which change is responsible for most of it.

**Tool: the small-change formula.** Trigger: small changes in several inputs, and a question about how much each one contributes. The formula answers both at once because its terms are the separate contributions.

$V = \pi r^2 h$, so $V_r = 2\pi r h = 238.4\ \text{cm}^2$ and $V_h = \pi r^2 = 34.2\ \text{cm}^2$.

$\Delta V \approx 238.4 \times 0.1 + 34.2 \times 0.1 = 23.84 + 3.42 = 27.3\ \text{cm}^3$. (The exact change is $27.8\ \text{cm}^3$.)

The radius accounts for $23.84/27.27 = 87\,\%$ of the change. The ratio $V_r / V_h = 2h/r \approx 7$ says a millimetre on the radius is worth seven on the height, which is why can makers control the diameter much more tightly than the height.

### Example 3: a direction on the hill

> On the hill $h = 400 - 0.001x^2 - 0.002y^2$, a path leaves $P(100, 50)$ heading straight for the summit. How steep is it at the start? Compare with the steepest possible climb from $P$.

**Tool: $D_{\mathbf u} h = \nabla h \cdot \mathbf u$.** Trigger: a slope is wanted in a named direction that is neither east nor north. The direction must be a **unit** vector, so normalise first.

$\nabla h = (-0.002x, -0.004y) = (-0.2, -0.2)$ at $P$. The summit is at the origin, so the direction is $(-100, -50)$, of length $\sqrt{12500} = 50\sqrt5$, giving $\mathbf u = \left(-\tfrac{2}{\sqrt5}, -\tfrac{1}{\sqrt5}\right)$.

$D_{\mathbf u} h = (-0.2)\left(-\tfrac{2}{\sqrt5}\right) + (-0.2)\left(-\tfrac{1}{\sqrt5}\right) = \dfrac{0.6}{\sqrt5} = 0.268.$

The steepest climb is $\lvert \nabla h \rvert = 0.283$. The direct path is slightly gentler, by the factor $\cos 18.4° = 0.949$, because it is not aimed along the gradient.

### Example 4: a drone in a temperature field

> The air temperature over a field is $T(x, y) = 20 + 0.0004xy - 0.0002y^2$ (°C, with $x$ and $y$ in metres). A drone flies along $x = 6t$, $y = t^2$ ($t$ in seconds). How fast is the temperature it records changing at $t = 5$?

**Tool: the multi-variable chain rule, $dT/dt = \nabla T \cdot \mathbf v$.** Trigger: the quantity depends on position, and position depends on time. Two channels, so two terms.

At $t = 5$ the drone is at $(30, 25)$ with velocity $\mathbf v = (6, 2t) = (6, 10)$ m s⁻¹.
$T_x = 0.0004y = 0.010$ and $T_y = 0.0004x - 0.0004y = 0.002$ °C per metre.

$\dfrac{dT}{dt} = (0.010)(6) + (0.002)(10) = 0.060 + 0.020 = 0.08$ °C per second.

**Check by substituting first.** $T(t) = 20 + 0.0024t^3 - 0.0002t^4$, so $T'(t) = 0.0072t^2 - 0.0008t^3$, and $T'(5) = 0.18 - 0.10 = 0.08$. The chain rule gives the same number and also says where it came from: three quarters from the eastward motion, one quarter from the northward.

### Example 5: classify the critical points

> Find and classify the critical points of $f(x, y) = x^3 - 3x + y^2$.

**Tool: $\nabla f = \mathbf 0$ to find them, then the sign of $D = f_{xx}f_{yy} - f_{xy}^2$ to classify them.** Trigger: "classify" with two variables. A saddle is possible, so the one-variable second-derivative test is not enough.

$f_x = 3x^2 - 3 = 0$ gives $x = \pm 1$. $f_y = 2y = 0$ gives $y = 0$. Critical points: $(1, 0)$ and $(-1, 0)$.

$f_{xx} = 6x$, $f_{yy} = 2$, $f_{xy} = 0$, so $D = 12x$.

At $(1, 0)$: $D = 12 > 0$ and $f_{xx} = 6 > 0$, a **local minimum**, with $f = -2$.
At $(-1, 0)$: $D = -12 < 0$, a **saddle**, with $f = 2$. Along the $x$-axis it is a maximum ($f_{xx} = -6$); along the $y$-direction it is a minimum ($f_{yy} = 2$).

## Common Misconceptions (Teaching Notes)

### 1. "The gradient points at the summit"

It points in the locally steepest direction. On the hill above, that is 18° away from the line to the summit. The two agree only when the contours are circles. **Fix:** draw the contour through the point and a line perpendicular to it. That is the gradient's line, and nothing about the summit entered.

### 2. "The gradient is an arrow lying on the surface"

For a function of two variables the gradient has two components. It lives in the $xy$-plane, on the *map*, not on the hillside. It tells a walker which compass bearing to take. **Fix:** count components. $\nabla f$ has as many as $f$ has inputs.

### 3. "$\partial$'s cancel like fractions"

In one variable, $\dfrac{dy}{dx}\cdot\dfrac{dx}{dy} = 1$, and the fraction picture is safe. With partial derivatives it is not. For three quantities tied by one equation, such as $P$, $V$ and $T$ in $PV = nRT$,

$$\left(\frac{\partial P}{\partial V}\right)_T \left(\frac{\partial V}{\partial T}\right)_P \left(\frac{\partial T}{\partial P}\right)_V = -1,$$

not $+1$. Check it: the three factors are $-\dfrac{nRT}{V^2}$, $\dfrac{nR}{P}$ and $\dfrac{V}{nR}$, and their product is $-\dfrac{nRT}{PV} = -1$. **Fix:** the three derivatives hold three *different* things constant, so they are not pieces of one fraction. Write the held variable outside the bracket and the temptation to cancel goes away.

### 4. "Both partial derivatives are zero, so it is a maximum or a minimum"

It may be a saddle. Example 5 has one. **Fix:** compute $D$. With one variable a stationary point can also be a point of inflection; with two, the usual third case is a pass between two peaks.

### 5. "If the partial derivatives exist, the surface has a tangent plane"

Let $f(x, y) = \dfrac{xy}{x^2 + y^2}$ away from the origin and $f(0,0) = 0$. Along both axes $f$ is identically zero, so $f_x(0,0) = f_y(0,0) = 0$. But along the line $y = x$ the function equals $\tfrac12$ however close to the origin you stand. It is not even continuous there. The partial derivatives probe two directions only and can miss what happens in between. **Fix:** the small-change formula was proved assuming the partial derivatives are *continuous*. That assumption is the one that makes two directions enough.

### 6. "Steepest descent is the fastest way down"

It is the best direction for the next small step. In the narrow valley of the descent figure it points across the valley rather than along it, and the path zigzags. **Fix:** "steepest" is a local word.

## Exam Notes

### Where this is *not* examined

Partial derivatives and the gradient are **first-year university material and are examined on none of the school boards**: not Cambridge 0580, 0606, 9709 or 9231 Further Mathematics; not OxfordAQA 9260 or 9660; and not AP Calculus AB or BC, whose course description has no multivariable content. Edexcel International A Level lists the symbol $\partial V/\partial x$ in its table of notation and sets no content on it. A text search of each of those syllabus documents for "partial derivative", "directional derivative", "gradient vector" and "several variables" finds nothing else. IB Mathematics Analysis and Approaches at higher level also stops at one variable.

### Where school courses lean on it without naming it

- **Uncertainties** in 9702 and IB Physics practical work: the rules "add absolute uncertainties for a sum, add percentage uncertainties for a product" are the small-change formula, taught as rules. [[Error Propagation]] derives them.
- **Implicit differentiation** in 9709 P3, AP Calculus and IB AA HL: $dy/dx = -F_x/F_y$ is the one-line version.
- **Field and potential** in 9702 and AP Physics C: "field strength = minus potential gradient" is $\mathbf E = -\nabla V$ in one dimension.

### Beyond high school — University

This is the first topic of any multivariable calculus course. What follows it: [[Multiple Integrals]], then [[Vector Calculus]], where the same $\nabla$ symbol is used to build the divergence and the curl that [[Maxwell's Equations]] are written in.

## Beyond the syllabus

> [!info] Constrained optimisation — two gradients in line
> Recall that the gradient of $g$ is perpendicular to the curve $g(x, y) = c$. To find the largest value of $f$ *on* that curve, walk along it. While $\nabla f$ has any component along the curve you can still go uphill by continuing. You can stop only where $\nabla f$ has no such component, that is, where $\nabla f$ is also perpendicular to the curve, which makes it parallel to $\nabla g$: $\nabla f = \lambda \nabla g$. That is the method of Lagrange multipliers; [[Optimisation]] states it and lists where it is used.

> [!info] The derivative of a function with several outputs
> A function from the plane to the plane, $(x, y) \mapsto (u, v)$, has four partial derivatives, and the natural way to hold them is a matrix,
> $$J = \begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix},$$
> the **Jacobian**. The small-change formula becomes a matrix equation, $\Delta(u, v) \approx J\,\Delta(x, y)$: near any point, a smooth map looks like one of the [[Matrix Transformations]]. Its determinant is the local area-scaling factor, which is the $r$ in $dA = r\,dr\,d\theta$ and the reason [[Integration by Substitution]] in two variables carries a $\lvert J \rvert$.

> [!info] Equations built from partial derivatives
> Once a quantity depends on both position and time, its law of change involves partial derivatives in each. The vibrating string in [[Progressive Waves]] obeys $\partial^2 y/\partial t^2 = v^2\,\partial^2 y/\partial x^2$; the cooling rod in [[Heat Transfer]] obeys $\partial T/\partial t = \alpha\,\partial^2 T/\partial x^2$. Both cards derive their equation from a force or energy balance on a thin slice.

## Connections

- **Parent:** [[Differentiation]] — a partial derivative is an ordinary derivative taken along one slice.
- **Tools used:** [[Chain Rule]], [[Product Rule]], [[Mean Value Theorem]] (the proof of the small-change formula), [[3D Vectors and the Scalar Product]] (the $\cos\theta$ behind the gradient).
- **One-variable counterparts:** [[Tangents and Normals]] (tangent line → tangent plane), [[Stationary Points]] (second-derivative test → the $D$ test, with the saddle as the new case).
- **Applications:** [[Error Propagation]], [[Implicit Differentiation]], [[Electric Potential]], [[Heat Transfer]], [[Artificial Intelligence]], [[Optimisation]], [[Numerical Methods]] (Newton's method and gradient descent as relatives).
- **Extensions:** [[Multiple Integrals]], [[Vector Calculus]], [[Maxwell's Equations]].

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{\partial f}{\partial x}$ | `\dfrac{\partial f}{\partial x}` | Partial derivative |
| $f_{xy}$ | `f_{xy}` | Mixed second partial: $x$ first, then $y$ |
| $\nabla f$ | `\nabla f` | Gradient |
| $D_{\mathbf u} f$ | `D_{\mathbf u} f` | Directional derivative along the unit vector $\mathbf u$ |
| $\left(\dfrac{\partial P}{\partial V}\right)_T$ | `\left(\dfrac{\partial P}{\partial V}\right)_T` | Partial derivative with the held variable shown |
| $\lvert \nabla f \rvert$ | `\lvert \nabla f \rvert` | Length of the gradient; use `\lvert`, not a bare pipe, inside tables |
| $\mathbf w \leftarrow \mathbf w - \eta \nabla L$ | `\mathbf w \leftarrow \mathbf w - \eta \nabla L` | Gradient-descent update |
