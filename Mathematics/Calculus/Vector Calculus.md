---
chinese: 向量微积分 (xiàngliàng wēijīfēn)
prerequisites:
  - "[[Partial Derivatives and the Gradient]]"
  - "[[Multiple Integrals]]"
  - "[[Cross Product]]"
  - "[[Fundamental Theorem of Calculus]]"
leads_to:
  - "[[Maxwell's Equations]]"
tags:
  - subject/mathematics
  - subject/physics
  - domain/calculus
  - level/university
  - type/definition
  - type/theorem
  - type/proof
  - type/visual-tool
  - notation/nabla
  - notation/line-integral
  - notation/surface-integral
  - misconception/curl-means-the-field-goes-round-in-circles
  - misconception/divergence-means-the-arrows-point-outward
  - misconception/the-work-along-a-path-is-always-path-independent
  - misconception/flux-through-a-closed-surface-is-always-zero
---

# Vector Calculus 向量微积分

> [[Maxwell's Equations]] are four sentences about flux through bags and circulation round loops. Physics students learn them in that form and then meet the same four laws written as $\nabla\cdot\mathbf E = \rho/\varepsilon_0$ and $\nabla\times\mathbf B = \dots$, and are told they are the same.
>
> They are. What lies between the two forms is the subject here: two derivatives that act on fields, two integrals that add fields up along curves and over surfaces, and three theorems that say the derivatives and the integrals are one thing.

## The question — what can you ask of an arrow at every point?

A **vector field** assigns an arrow to every point: the wind over a map, the current in a river, the electric field round a charge, the velocity of water in a pipe. [[Partial Derivatives and the Gradient]] made one kind of field, $\nabla f$, out of a scalar $f$. Now take the field as given and ask two local questions at each point.

- **Is something being made here, or swallowed?** Water leaves a tap and enters a drain. Put a tiny closed bag round a point and count what flows out minus what flows in.
- **Is it spinning here?** Put a tiny paddle wheel at the point and see whether it turns.

The first question is answered by the **divergence**, the second by the **curl**, and each is a limit of an integral over a shrinking shape, exactly as a derivative is a limit of a difference quotient. What follows builds the two integrals first, then the two derivatives from them, then the theorems that tie each derivative back to its integral.

![[vector-calculus-three-fields.svg|820]]

## 中文锚点

站在河里，把一个小小的叶轮放到水下。轮子两边的水流一样快的地方，轮子会顺水漂，但不会转。靠近河岸的时候，轮子外侧的水比内侧的水流得快，轮子就转起来了，尽管河水是直着往前流的，并没有什么东西在打转。再把双手拢成碗状，放到水龙头下面：水落在手心中央，从手掌的每一条边沿流走；除了水龙头这个唯一的源头，没有哪个地方流走的比进来的多。向量微积分做的，就是在流动的每一个点上问这两个问题：这里在打转吗？这里有东西凭空冒出来，或者被吞掉吗？两个答案分别叫作旋度和散度。跟它们配套的定理讲的是一件你在河里就能验证的事：一个圈里打转的总量，等于你沿着这个圈走一圈、一路上水流推你的劲儿加起来的总和；一个袋子里面造出来的总量，等于从袋子表面漏出去的量，因为中间的一切都互相抵消了。

## Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $\mathbf F(x, y, z) = (P, Q, R)$ | "the field F" | three functions, one for each component |
| $\nabla$ | "del" or "nabla" | the operator $\left(\dfrac{\partial}{\partial x}, \dfrac{\partial}{\partial y}, \dfrac{\partial}{\partial z}\right)$, waiting for something to act on |
| $\nabla f$ | "grad f" | a vector from a scalar: the direction and rate of steepest increase |
| $\nabla\cdot\mathbf F$ | "div F" | a scalar from a vector: outflow per unit volume |
| $\nabla\times\mathbf F$ | "curl F" | a vector from a vector: twice the local spin rate, along the axis of the spin |
| $\displaystyle\int_C \mathbf F\cdot d\mathbf l$ | "the line integral of F along C" | the field's push, added up along a curve; a circle on the sign means $C$ is closed |
| $\displaystyle\iint_S \mathbf F\cdot d\mathbf A$ | "the flux of F through S" | the field's crossing, added up over a surface; a circle means $S$ is closed |

The dot and cross in $\nabla\cdot$ and $\nabla\times$ are not decoration: they are the [[3D Vectors and the Scalar Product]] and [[Cross Product]] applied formally to the operator, and that is how to remember which is which.

## Line integrals — adding a field along a path

Push a box along a path, and the work done is force times distance only when the force is constant and along the path. In general, chop the path into steps $d\mathbf l$ and add the push along each step:

$$W = \int_C \mathbf F\cdot d\mathbf l .$$

To compute it, describe the curve by a parameter, $\mathbf r(t)$ for $a \le t \le b$, so that $d\mathbf l = \mathbf r'(t)\,dt$ and the integral is an ordinary one in $t$. For $\mathbf F = (y, x)$ along the straight line from $(0,0)$ to $(1,1)$, $\mathbf r = (t, t)$:

$$\int_0^1 (t, t)\cdot(1, 1)\,dt = \int_0^1 2t\,dt = 1 .$$

Along the parabola $\mathbf r = (t, t^2)$ the integrand is $t^2 \cdot 1 + t \cdot 2t = 3t^2$ and the integral is again $1$. Along two straight legs, first east then north, it is $0 + 1 = 1$. Three paths, one answer.

Now do the same for $\mathbf G = (-y, x)$: the line gives $0$, the parabola $\tfrac13$, the two legs $1$. Three paths, three answers.

### Conservative fields

The difference is that $\mathbf F$ is a gradient, $\mathbf F = \nabla(xy)$, and $\mathbf G$ is not. For a gradient field the line integral is the change in the potential, by the chain rule:

$$\int_C \nabla f\cdot d\mathbf l = \int_a^b \frac{d}{dt} f(\mathbf r(t))\,dt = f(\text{end}) - f(\text{start}) .$$

This is the [[Fundamental Theorem of Calculus]] for a curve: the derivative inside, the endpoints outside. Such fields are **conservative**, the work depends only on where you start and end, and round any closed loop it is zero. Gravity is one, which is why lifting 1 kg by 3 m costs $29.4$ J along a ladder, a ramp or a spiral. $\mathbf G$ is not: round the circle of radius $R$ its integral is $2\pi R^2$, twice the area. That number is about to become the curl.

## Flux — adding a field through a surface

Rain falls on a tilted roof. What lands per second is the rain's velocity times the roof's area times the cosine of the angle between them, which is a dot product with the roof's normal. Chop any surface into tiles $d\mathbf A$, each an arrow of size the tile's area pointing along its normal, and add:

$$\Phi = \iint_S \mathbf F\cdot d\mathbf A .$$

For a closed surface the normal points outward and the flux counts what leaves minus what enters.

Two fluxes to know by heart. The field $\mathbf F = (x, y, z)$ through the unit cube: on the face $x = 1$ the outward normal is $+\mathbf i$ and $\mathbf F\cdot\mathbf n = 1$, giving $1$; on $x = 0$ it is $0$; the same for the other pairs, total $3$. And the field of a point charge, $\hat{\mathbf r}/r^2$, through a sphere of radius $R$: the field is radial with size $1/R^2$, the area is $4\pi R^2$, so the flux is $4\pi$ **for every $R$**. That is Gauss's law in [[Electric Field]] before the constants are put in.

## Divergence — outflow per unit volume

Take a small box of volume $\Delta V$ round a point and compute the flux out of it. The field entering through the left face at $x$ and leaving through the right face at $x + \Delta x$ contributes $[P(x + \Delta x) - P(x)]\,\Delta y\,\Delta z \approx \dfrac{\partial P}{\partial x}\Delta V$, and the other two pairs of faces do the same. So

$$\nabla\cdot\mathbf F = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} = \lim_{\Delta V\to 0}\frac{\text{flux out of the box}}{\Delta V} .$$

The definition on the right is the meaning; the formula on the left is how to compute it. `vector-calculus-model.py` does the limit numerically for $\mathbf F = (x^3, \sin y)$ at $(1, 2)$: the flux out of a square of side $0.5$, divided by its area, is $2.6507$; side $0.1$ gives $2.5865$; side $0.01$ gives $2.58388$; and $3x^2 + \cos y$ at the point is $2.58385$.

For the three fields in the figure: the spreading field has divergence $2$ everywhere, the rotating field and the shear have divergence $0$. So does the point-charge field away from the charge, $\nabla\cdot(\hat{\mathbf r}/r^2) = 0$: the flux through every sphere was the same because nothing is created between one sphere and the next. Positive divergence is a **source**, negative is a **sink**, zero means whatever comes in goes out.

**Divergence is not "the arrows point outward."** The arrows of $\hat{\mathbf r}/r^2$ point outward everywhere and its divergence is zero everywhere but the origin. The arrows spread, but they also weaken, and the two effects cancel exactly.

## Curl — circulation per unit area

Take a small loop of area $\Delta A$ round a point in the $xy$-plane, walk round it anticlockwise, and add up $\mathbf F\cdot d\mathbf l$. The bottom edge at $y$ contributes $P(y)\,\Delta x$ going east and the top edge at $y + \Delta y$ contributes $-P(y + \Delta y)\,\Delta x$ going west, together $-\dfrac{\partial P}{\partial y}\Delta A$; the two vertical edges give $+\dfrac{\partial Q}{\partial x}\Delta A$. So the $z$-component of the curl is

$$(\nabla\times\mathbf F)_z = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = \lim_{\Delta A\to 0}\frac{\text{circulation round the loop}}{\Delta A},$$

and the other two components come from loops in the other two planes. Written as a formal cross product,

$$\nabla\times\mathbf F = \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \\[1mm] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[2mm] P & Q & R \end{vmatrix} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z},\; \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x},\; \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right).$$

The vector points along the axis of the spin, by the right-hand rule, and its size is twice the angular velocity a small paddle wheel would have. For the rotating field $\mathbf G = (-y, x)$, $\nabla\times\mathbf G = (0, 0, 2)$: the whole plane turns like a disc at one radian per second, and the paddle wheel turns with it wherever it sits.

![[vector-calculus-paddle-wheel.mp4]]

**Curl is not "the field goes round in circles."** The shear $\mathbf H = (y, 0)$ flows in straight lines and has curl $-1$: the paddle above the wheel's centre is pushed harder than the paddle below, so the wheel turns clockwise. And a field can circle a point with zero curl away from it: $(-y, x)/(x^2 + y^2)$ goes round the origin and its curl is zero everywhere else, which is the magnetic field of a straight wire. Curl is about the *difference* in push across a small wheel, not about the shape of the streamlines.

Two identities follow from the formulas by cancelling mixed partials, and both are the shape of physics: **the curl of a gradient is zero** (a hill has no whirlpools, which is why gravity is conservative), and **the divergence of a curl is zero** (spin makes no sources, which is why magnetic field lines never end).

## The three theorems — the boundary knows what is inside

The [[Fundamental Theorem of Calculus]] says $\int_a^b f'(x)\,dx = f(b) - f(a)$: integrate a derivative over a region and you get the function's values on the region's boundary, the two endpoints. Each of the three theorems below is that sentence with a different derivative, a different region and a different boundary.

| Theorem | Region | Its boundary | Statement |
|---|---|---|---|
| Green | a flat region $D$ | the closed curve $C$ round it | $\displaystyle\oint_C \mathbf F\cdot d\mathbf l = \iint_D (\nabla\times\mathbf F)_z\, dA$ |
| Stokes | a surface $S$ in space | its rim $C$ | $\displaystyle\oint_C \mathbf F\cdot d\mathbf l = \iint_S (\nabla\times\mathbf F)\cdot d\mathbf A$ |
| Gauss (divergence) | a solid $V$ | the closed surface $S$ round it | $\displaystyle\oiint_S \mathbf F\cdot d\mathbf A = \iiint_V \nabla\cdot\mathbf F\, dV$ |

Green's theorem is Stokes' for a flat surface. The proof of all three is one picture.

![[vector-calculus-cancelling.svg|820]]

Cut the region into small cells. Round each cell, the circulation is (curl) $\times$ (cell area), by the definition of curl. Add over all cells: the right-hand side becomes $\iint \text{curl}\,dA$. On the left, every edge shared by two cells is walked once in each direction, so its two contributions cancel, and what survives is the rim. **The interior cancels; the boundary is what is left.** For the divergence theorem, replace cells by small boxes and circulation by flux: every interior face is crossed outward by one box and inward by its neighbour.

Check Green's theorem on $\mathbf G = (-y, x)$ round the unit square. The four legs give $0 + 1 + 1 + 0 = 2$. The curl is $2$ and the area is $1$, so the double integral is $2$. Check the divergence theorem on $\mathbf F = (x, y, z)$ and the unit cube: the flux was $3$, and $\nabla\cdot\mathbf F = 3$ integrated over volume $1$ is $3$.

### The theorem that lets you choose your surface

Stokes' theorem says the surface integral of a curl depends only on the rim. So for $\mathbf G = (-y, x, 0)$, whose curl is $(0, 0, 2)$, the flux of the curl through the flat unit disc is $2\pi$, through the upper unit hemisphere it is also $2\pi$ (the model script does the spherical integral), and through any dome or dent with the same rim it is still $2\pi$, because the rim integral is $\oint \mathbf G\cdot d\mathbf l = 2\pi$ and there is only one rim.

## Where this is the working tool

- **Maxwell's equations, both ways.** The integral forms in [[Maxwell's Equations]] become the differential forms by these theorems and nothing else: Gauss's law $\oiint \mathbf E\cdot d\mathbf A = Q/\varepsilon_0$ over every bag is $\nabla\cdot\mathbf E = \rho/\varepsilon_0$ at every point, and Faraday's law round every loop is $\nabla\times\mathbf E = -\partial\mathbf B/\partial t$. The two magnetic laws say $\nabla\cdot\mathbf B = 0$, so the field of every magnet is a curl and its lines never end.
- **Weather and flow.** A meteorologist's vorticity is the curl of the wind, and a region of strong vorticity is a storm; the divergence of the wind tells where air is rising, since air leaving a patch of ground horizontally must be replaced from above. Every fluid-dynamics code computes both on a grid, by the small-box and small-loop definitions above.
- **Conservation, stated once.** If $\rho$ is the density of anything conserved and $\mathbf J$ its flow, then the mass in a bag can change only by flow through the skin. By the divergence theorem that is $\partial\rho/\partial t + \nabla\cdot\mathbf J = 0$, the continuity equation, and it governs water, charge, probability in quantum mechanics and traffic.
- **The planimeter.** A brass instrument that measures the area of any region on a map by tracing its outline. It works because Green's theorem with $\mathbf F = \tfrac12(-y, x)$ gives $\text{Area} = \tfrac12\oint (x\,dy - y\,dx)$: an area is a line integral round its edge. The model script checks it on an ellipse and gets $\pi ab$.
- **Rendering and games.** The lighting on a surface uses its normal, and the normal of a surface given as a level set $f = 0$ is $\nabla f$; the flow fields that drive smoke and water in a game engine are kept divergence-free by solving for a pressure whose gradient removes the divergence at every step.

## Worked Examples

### Example 1: compute all three

> For $\mathbf F = (x^2 y,\; yz,\; xz^2)$, find $\nabla\cdot\mathbf F$ and $\nabla\times\mathbf F$.

*Trigger: a field given by components. Tool: the two formulas, one term at a time.*

$\nabla\cdot\mathbf F = 2xy + z + 2xz$. For the curl, $R_y - Q_z = 0 - y = -y$, $P_z - R_x = 0 - z^2 = -z^2$, $Q_x - P_y = 0 - x^2 = -x^2$, so $\nabla\times\mathbf F = (-y, -z^2, -x^2)$.

### Example 2: is it conservative, and what is the potential?

> Is $\mathbf F = (2xy + z^3,\; x^2,\; 3xz^2)$ conservative? If so find $f$ with $\nabla f = \mathbf F$ and the work from $(0,0,0)$ to $(1,2,1)$.

*Trigger: the words "conservative" or "path-independent". Tool: curl is zero if and only if a potential exists (on all of space); then integrate one component at a time.*

$R_y - Q_z = 0$, $P_z - R_x = 3z^2 - 3z^2 = 0$, $Q_x - P_y = 2x - 2x = 0$. Conservative. From $f_x = 2xy + z^3$, $f = x^2 y + xz^3 + g(y, z)$; then $f_y = x^2 + g_y = x^2$ gives $g_y = 0$; and $f_z = 3xz^2 + g_z = 3xz^2$ gives $g_z = 0$. So $f = x^2 y + xz^3$ and the work is $f(1,2,1) - f(0,0,0) = 2 + 1 = 3$, along any path.

### Example 3: a line integral by Green's theorem

> Evaluate $\oint_C (x^2 - y)\,dx + (x + y^2)\,dy$ anticlockwise round the circle $x^2 + y^2 = 4$.

*Trigger: a closed curve and an integrand that is a mess to parametrise. Tool: Green's theorem turns it into a double integral of $Q_x - P_y$.*

$Q_x - P_y = 1 - (-1) = 2$, a constant, so the integral is $2 \times$ (area) $= 2 \times 4\pi = 8\pi$. Parametrising the circle would have taken half a page.

### Example 4: a flux by the divergence theorem

> Find the flux of $\mathbf F = (x^3, y^3, z^3)$ out of the sphere of radius $a$.

*Trigger: a closed surface and a field whose divergence is simple in spherical coordinates. Tool: the divergence theorem, then [[Multiple Integrals]] in spherical coordinates.*

$\nabla\cdot\mathbf F = 3(x^2 + y^2 + z^2) = 3\rho^2$. So the flux is $\iiint 3\rho^2\,dV = 3\int_0^{2\pi}\!\int_0^{\pi}\!\int_0^a \rho^2\cdot\rho^2\sin\phi\,d\rho\,d\phi\,d\theta = 3\cdot 2\pi\cdot 2\cdot\dfrac{a^5}{5} = \dfrac{12\pi a^5}{5}$.

### Example 5: from Gauss's law in integral form to a differential equation

> Gauss's law says the flux of $\mathbf E$ out of any closed surface is $Q_{\text{enc}}/\varepsilon_0$. Derive the local form.

*Trigger: a law stated "for every closed surface". Tool: the divergence theorem on the left, the definition of density on the right, and the fact that the two agree for every region.*

$\oiint_S \mathbf E\cdot d\mathbf A = \iiint_V \nabla\cdot\mathbf E\,dV$ by the theorem, and $Q_{\text{enc}} = \iiint_V \rho\,dV$ by the meaning of charge density. So $\iiint_V (\nabla\cdot\mathbf E - \rho/\varepsilon_0)\,dV = 0$ for **every** volume $V$. A continuous function whose integral over every region is zero is zero, so $\nabla\cdot\mathbf E = \rho/\varepsilon_0$. The other three Maxwell equations go the same way, two by Gauss and two by Stokes.

## Common Misconceptions (Teaching Notes)

### 1. "Curl means the field goes round in circles"
The straight-line shear $(y, 0)$ has curl $-1$; the circling field $(-y, x)/(x^2 + y^2)$ has curl $0$ off the origin. Curl compares the push on two sides of a small wheel.

### 2. "Divergence means the arrows point outward"
$\hat{\mathbf r}/r^2$ points outward everywhere and has zero divergence everywhere but the origin. Spreading out and weakening cancel.

### 3. "The work along a path is always path-independent"
Only for conservative fields, which are exactly the curl-free ones on a region with no holes. $(-y, x)$ gives three answers for three paths.

### 4. "The flux out of a closed surface is always zero"
It is zero when there is no source inside. A charge inside gives $q/\varepsilon_0$, whatever the surface.

### 5. "Curl-free means conservative, full stop"
On a region with a hole it can fail: $(-y, x)/(x^2 + y^2)$ is curl-free where it is defined and has circulation $2\pi$ round the origin. The potential (the angle $\theta$) exists but cannot be made single-valued.

### 6. "$\nabla\cdot$ and $\nabla\times$ are just notation"
They are a dot product and a cross product with the operator $\nabla$, and the identities $\nabla\times\nabla f = 0$ and $\nabla\cdot(\nabla\times\mathbf F) = 0$ are the two facts that $\mathbf a\times\mathbf a = 0$ and $\mathbf a\cdot(\mathbf a\times\mathbf b) = 0$, in disguise.

## Exam Notes

### Where this is *not* examined
No school syllabus in these notes examines vector calculus. A text search of the Cambridge 9709 and 9231 syllabuses and of the AP Calculus AB and BC course description for "divergence", "curl", "line integral", "Stokes" and "Green" finds none of them. AP Physics C: Electricity and Magnetism states Maxwell's equations in integral form and works Gauss's and Ampère's laws with symmetry; it does not use $\nabla$.

### Where school courses lean on it without naming it
- **Gauss's law and Ampère's law** (AP Physics C: E&M, 9702 in the special case of a point charge): flux through a closed surface and circulation round a closed loop, computed by symmetry. The theorems here are why those computations give local fields.
- **Work done by a force** (9709 Mechanics, AP Physics C: Mechanics): $W = \int \mathbf F\cdot d\mathbf r$ along a straight line, and the statement that gravitational and spring forces are conservative.
- **Flux linkage and Faraday's law** (9702, AP Physics C: E&M): $\Phi = BA\cos\theta$ is one tile of a surface integral.

### Beyond high school — University
This is the third topic of a multivariable calculus course, after [[Partial Derivatives and the Gradient]] and [[Multiple Integrals]], and the mathematics that every electromagnetism and fluid-dynamics course assumes from its first lecture.

## Beyond the syllabus

> [!info] One theorem, not three
> Recall the table of three theorems. In the language of differential forms they are one statement, $\int_{\partial M}\omega = \int_M d\omega$: the integral of a form over the boundary of a region equals the integral of its derivative over the region. The Fundamental Theorem of Calculus is the case where the region is an interval and the boundary is two points. Green, Stokes and Gauss are the cases of dimension two and three. The pattern continues in every dimension, and the cancelling-cells proof is the proof in every case.

> [!info] Helmholtz: a field is a gradient plus a curl
> Recall that a gradient has no curl and a curl has no divergence. The converse is a theorem: any well-behaved field on all of space that dies away at infinity can be written as $\mathbf F = -\nabla\phi + \nabla\times\mathbf A$, one part with all the divergence and none of the curl, one part with all the curl and none of the divergence. So a field is determined by its sources and its vortices, which is exactly what Maxwell's four equations supply for $\mathbf E$ and $\mathbf B$.

## Connections

- **Prerequisites:** [[Partial Derivatives and the Gradient]] (the gradient, $\nabla$, the chain rule along a curve), [[Multiple Integrals]] (double and triple integrals, spherical coordinates), [[Cross Product]] and [[3D Vectors and the Scalar Product]] (what $\nabla\times$ and $\nabla\cdot$ mean), [[Fundamental Theorem of Calculus]] (the one-dimensional case of every theorem here), [[Determinants and Inverses]] (the curl as a determinant).
- **Physics that is vector calculus in other words:** [[Maxwell's Equations]], [[Electric Field]] (Gauss's law), [[Electromagnetic Induction]] (Faraday's law), [[Work, Energy and Power]] (conservative forces), [[Gravitational Fields]] and [[Electric Potential]] (potentials).
- **Numerical:** [[Numerical Methods]].

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\nabla f$ | `\nabla f` | Gradient |
| $\nabla\cdot\mathbf F$ | `\nabla\cdot\mathbf F` | Divergence |
| $\nabla\times\mathbf F$ | `\nabla\times\mathbf F` | Curl |
| $\displaystyle\oint_C \mathbf F\cdot d\mathbf l$ | `\oint_C \mathbf F\cdot d\mathbf l` | Closed line integral |
| $\displaystyle\oiint_S \mathbf F\cdot d\mathbf A$ | `\oiint_S \mathbf F\cdot d\mathbf A` | Closed surface integral; needs `esint` or `mathjax`; `\iint_S` with the word "closed" is the fallback |
| $\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}$ | `\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}` | The $z$-component of the curl |
| $\begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \\ \partial_x & \partial_y & \partial_z \\ P & Q & R \end{vmatrix}$ | `\begin{vmatrix} ... \end{vmatrix}` | The curl as a determinant |
