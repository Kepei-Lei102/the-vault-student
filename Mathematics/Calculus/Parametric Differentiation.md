---
chinese: 参数方程求导 (cānshù fāngchéng qiúdǎo)
prerequisites:
  - "[[Chain Rule]]"
  - "[[Quotient Rule]]"
  - "[[Implicit Differentiation]]"
  - "[[Differentiation Rules]]"
leads_to:
  - "[[Tangents and Normals]]"
  - "[[Connected Rates of Change]]"
  - "[[Arc Length and Surfaces of Revolution]]"
teach_together:
  - "[[Kinematics Calculus]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/IB-HL
  - level/AP
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-3-4
  - syllabus/9231-2-3
  - type/theorem
  - type/technique
  - notation/derivative
  - notation/leibniz
  - misconception/parametric-second-derivative
  - misconception/parametric-as-fraction-of-second-derivatives
---

# Parametric Differentiation 参数方程求导

> *Some curves are most naturally described not by $y = f(x)$ or $F(x, y) = 0$, but by giving both $x$ and $y$ as functions of a third variable — a* **parameter** *— that does the moving.*
>
> *A point on a circle: $x = r\cos t$, $y = r\sin t$. A bead rolling: $x = a(t - \sin t)$, $y = a(1 - \cos t)$. The position of a planet, the trajectory of a projectile, the path of a robotic arm — all are most naturally written as $(x(t), y(t))$.*
>
> *Parametric Differentiation is the calculus of finding* $\dfrac{dy}{dx}$ *along such a curve, without ever solving for $y$ in terms of $x$.*

## What this card is for

[[Implicit Differentiation]] handles curves given by $F(x, y) = 0$ — equations relating $x$ and $y$. **Parametric Differentiation** handles curves given by $x = f(t)$ and $y = g(t)$ — *both* coordinates as functions of a parameter $t$. The two formats appear interchangeably in 9709 P3 §3.4, IB AA HL, AP Calc BC, and university single-variable calculus.

The parametric format dominates whenever a curve has a *natural motion* (planetary orbits, projectile trajectories, parametrically-traced figures like cycloids and helices) or when one of $x, y$ is multi-valued in the other (the upper and lower halves of a circle are *one* continuous parametric curve, but two separate explicit functions). Once you have the parametric form, the chain rule supplies $\dfrac{dy}{dx}$ in one step:

$$\boxed{\;\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}\;}$$

provided $\dfrac{dx}{dt} \neq 0$. The whole technique is one fraction; the depth lives in *higher derivatives* (where the obvious-looking generalisation is wrong, in a way examiners love to test) and in the connection to motion, where parametric differentiation is the calculus underneath every velocity calculation.

This card closes 9709 P3 §3.4 by completing the trio with [[Quotient Rule]] and [[Implicit Differentiation]].

## The Rule

Suppose $x$ and $y$ are both differentiable functions of a parameter $t$:

$$x = f(t), \qquad y = g(t).$$

If $\dfrac{dx}{dt} \neq 0$ in some neighbourhood of $t = t_0$, then $y$ is locally a function of $x$ near that point, and

$$\boxed{\;\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}\;}$$

Or in dot notation (Newton, for time): $\dfrac{dy}{dx} = \dfrac{\dot{y}}{\dot{x}}$.

> [!tip] Watch x(t) and y(t) trace the curve
> The clearest way to *see* parametric differentiation is to watch $x(t)$ and $y(t)$ moving in lockstep with the parameter $t$. The animation below shows three synchronised panels — $x(t)$ as a sine wave, the $(x, y)$ trajectory tracing out the curve, and $y(t)$ as a cosine wave — first for the unit circle (calibration) and then for the cycloid (cusps where $\dot{x} = 0$).

![[parametric-trajectory.mp4]]

## 中文锚点

**参数方程求导**：当曲线由 $x = f(t)$ 和 $y = g(t)$ 同时给出（即 $x$ 和 $y$ 都是参数 $t$ 的函数）时，求 $\dfrac{dy}{dx}$ 的方法。

**核心公式**：

$$\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}.$$

**口诀**：**「参数求导，分子分母都对 $t$ 求一遍，再相除」。** 不需要把 $y$ 解出来当 $x$ 的函数。

**核心警告 —— 二阶导数有陷阱**：

$$\dfrac{d^2 y}{dx^2} \;\neq\; \dfrac{d^2 y/dt^2}{d^2 x/dt^2}.$$

**这是错的。** 正确的做法是：把 $\dfrac{dy}{dx}$ 当作 $t$ 的函数，再用链式法则求一次导：

$$\dfrac{d^2 y}{dx^2} = \dfrac{d}{dx}\!\left(\dfrac{dy}{dx}\right) = \dfrac{1}{dx/dt}\cdot\dfrac{d}{dt}\!\left(\dfrac{dy}{dx}\right).$$

考试经常考这一点。**记住：参数化只在一阶导数上像分式相除；高阶导数要重新跑一遍链式法则。**

---

## Why It Works — One-Line Chain Rule

If $x = f(t)$ and $y = g(t)$, and $f$ is locally invertible (i.e. $f'(t) \neq 0$ near $t_0$), then *near* $t_0$ we can write $t = f^{-1}(x)$, and so $y = g(f^{-1}(x))$ is genuinely a function of $x$. Apply the chain rule:

$$\dfrac{dy}{dx} = \dfrac{dy}{dt}\cdot\dfrac{dt}{dx}.$$

By the inverse-function rule (see [[Implicit Differentiation]] §"Inverse Function Rule"):

$$\dfrac{dt}{dx} = \dfrac{1}{dx/dt}.$$

Substituting:

$$\dfrac{dy}{dx} = \dfrac{dy}{dt}\cdot\dfrac{1}{dx/dt} = \dfrac{dy/dt}{dx/dt}.\qquad\blacksquare$$

That's it. Two chain-rule moves and an inverse function. The formula isn't a definition or an axiom — it's the chain rule, applied to a curve whose $x$ and $y$ are both fed by the same parameter.

> [!info] The Leibniz suggestiveness in one line
> $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ is *exactly* the kind of "fraction-cancellation" suggestion that makes Leibniz notation pay off — the $dt$'s "cancel" if you treat the differentials algebraically. (See [[Stories/The Calculus Priority Dispute]] for the full notation-war story.) In Newton's dot notation: $\dfrac{dy}{dx} = \dfrac{\dot{y}}{\dot{x}}$ — same fraction-feel, since dots are time-derivatives. In Lagrange notation, the formula is the same content but uglier to write.

---

## Worked Examples

### Example 1 — The circle $x = r\cos t,\; y = r\sin t$

The standard circle parametrisation. Compute:

$$\dfrac{dx}{dt} = -r\sin t, \qquad \dfrac{dy}{dt} = r\cos t.$$

So:

$$\dfrac{dy}{dx} = \dfrac{r\cos t}{-r\sin t} = -\cot t = -\dfrac{\cos t}{\sin t}.$$

**Sanity check.** At the point $(0, r)$, where $t = \pi/2$: $\dfrac{dy}{dx} = -\cot(\pi/2) = 0$. The tangent at the top of the circle is horizontal. ✓

At the point $(r, 0)$, where $t = 0$: $\dfrac{dx}{dt} = 0$, so the formula breaks — and correctly. The tangent at $(r, 0)$ is *vertical*, not undefined. The formula's failure at $\dfrac{dx}{dt} = 0$ is exactly the parametric counterpart of the implicit-differentiation vertical-tangent detection.

**Cross-check with implicit.** The same circle is $x^2 + y^2 = r^2$ implicitly. Implicit differentiation gives $\dfrac{dy}{dx} = -\dfrac{x}{y} = -\dfrac{r\cos t}{r\sin t} = -\cot t$. ✓ Same answer, two routes.

### Example 2 — The ellipse $x = a\cos t,\; y = b\sin t$

Almost identical structure:

$$\dfrac{dx}{dt} = -a\sin t, \qquad \dfrac{dy}{dt} = b\cos t \;\Longrightarrow\; \dfrac{dy}{dx} = -\dfrac{b\cos t}{a\sin t} = -\dfrac{b}{a}\cot t.$$

The factor $b/a$ encodes the ellipse's eccentricity. At $t = \pi/4$: $\dfrac{dy}{dx} = -b/a$. The tangent's slope at the "45-degree parameter" depends only on the axis ratio.

### Example 3 — A 9709 P3-style problem

Let $x = t^2 + 1,\; y = t^3 - 3t$. Find the point(s) where the tangent is horizontal.

$$\dfrac{dx}{dt} = 2t, \qquad \dfrac{dy}{dt} = 3t^2 - 3 = 3(t^2 - 1).$$

So:

$$\dfrac{dy}{dx} = \dfrac{3(t^2 - 1)}{2t} \quad (t \neq 0).$$

Horizontal tangent when $\dfrac{dy}{dx} = 0$: numerator zero, denominator non-zero. So $t^2 - 1 = 0$, giving $t = \pm 1$.

At $t = 1$: $(x, y) = (2, -2)$. At $t = -1$: $(x, y) = (2, 2)$. Two points, both with $x = 2$, sitting symmetrically about the x-axis. The curve is a doubled-back loop with two horizontal tangents.

This is the canonical 9709 P3 §3.4 question shape: *given parametric $x(t), y(t)$, find tangent / normal / where tangent is horizontal or vertical / value of $\frac{dy}{dx}$ at a given $t$*. The technique is one move; the time pressure is in the algebra.

### Example 4 — The cycloid $x = a(t - \sin t),\; y = a(1 - \cos t)$

The path traced by a point on a rolling circle. Beautiful curve, named in [[Stories/The Bernoulli Family]] as the answer to the 1696 brachistochrone problem.

$$\dfrac{dx}{dt} = a(1 - \cos t), \qquad \dfrac{dy}{dt} = a\sin t.$$

So:

$$\dfrac{dy}{dx} = \dfrac{a\sin t}{a(1 - \cos t)} = \dfrac{\sin t}{1 - \cos t}.$$

Using the identities $\sin t = 2\sin(t/2)\cos(t/2)$ and $1 - \cos t = 2\sin^2(t/2)$:

$$\dfrac{dy}{dx} = \dfrac{2\sin(t/2)\cos(t/2)}{2\sin^2(t/2)} = \dfrac{\cos(t/2)}{\sin(t/2)} = \cot(t/2).$$

Cusps appear at $t = 0, 2\pi, 4\pi, \ldots$ where $\cot(t/2) \to \infty$ — those are the points where the rolling circle touches the ground and the tracing point is momentarily at rest. The vertical-tangent failure is the cusp.

> [!info] Beyond syllabus — the brachistochrone connection
> *Recall from [[Optimisation]] §"Calculus of Variations" that a bead released from rest slides from one point to another in shortest time along a* cycloid*, not a straight line.* Bernoulli proved this in 1696 by ingeniously parametrising. The cycloid's parametric form is what makes the calculation tractable — try doing the same problem with the cycloid in implicit form $x^2 + ?$ and you'll see why parametric won. *(See [[Stories/The Bernoulli Family]] for the historical drama of the brachistochrone challenge.)*

---

## Higher Derivatives — The Trap

The single most-tested misconception in parametric differentiation: **the second derivative is not the ratio of second derivatives.**

$$\boxed{\;\dfrac{d^2 y}{dx^2} \;\neq\; \dfrac{d^2 y/dt^2}{d^2 x/dt^2}\;}$$

Why not? Because $\dfrac{dy}{dx}$ is itself a function of $t$ (or of $x$, equivalently). To get $\dfrac{d^2 y}{dx^2}$, you must differentiate $\dfrac{dy}{dx}$ *with respect to $x$*, which by the chain rule means differentiating with respect to $t$ first and then dividing by $dx/dt$.

### The correct formula

Let $p(t) = \dfrac{dy}{dx}$ as a function of $t$. Then:

$$\dfrac{d^2 y}{dx^2} = \dfrac{d}{dx}p(t) = \dfrac{dp/dt}{dx/dt}.$$

Substituting $p = (dy/dt)/(dx/dt)$:

$$\boxed{\;\dfrac{d^2 y}{dx^2} = \dfrac{1}{dx/dt}\cdot\dfrac{d}{dt}\!\left(\dfrac{dy/dt}{dx/dt}\right)\;}$$

Notice the **outer factor** $1/(dx/dt)$ — it's the chain-rule correction that the wrong-formula version forgets. Without it, you're computing $\dfrac{d}{dt}\!\left(\dfrac{dy}{dx}\right)$, which is the *rate of change of slope with respect to time*, not with respect to $x$. Different physical quantity, different number.

### Worked example — the parametric circle, second derivative

From Example 1: $\dfrac{dy}{dx} = -\cot t$. Differentiate this with respect to $t$:

$$\dfrac{d}{dt}(-\cot t) = \csc^2 t = \dfrac{1}{\sin^2 t}.$$

Divide by $\dfrac{dx}{dt} = -r\sin t$:

$$\dfrac{d^2 y}{dx^2} = \dfrac{1/\sin^2 t}{-r\sin t} = -\dfrac{1}{r\sin^3 t}.$$

**Cross-check with implicit.** From [[Implicit Differentiation]] Example 5, $\dfrac{d^2 y}{dx^2} = -\dfrac{r^2}{y^3}$ for $x^2 + y^2 = r^2$. Substituting $y = r\sin t$:

$$-\dfrac{r^2}{(r\sin t)^3} = -\dfrac{r^2}{r^3 \sin^3 t} = -\dfrac{1}{r\sin^3 t}.\;\checkmark$$

Same answer. Both routes agree, as they must.

> [!warning] The wrong-formula version, debunked
> If you compute $\dfrac{d^2 y/dt^2}{d^2 x/dt^2}$ for the circle: $d^2 y/dt^2 = -r\sin t$, $d^2 x/dt^2 = -r\cos t$, ratio $= \tan t$. That is *not* equal to $-\dfrac{1}{r\sin^3 t}$. **The wrong formula gives a wrong answer.** Examiners know which formula students reach for under pressure.

---

## Tangents and Normals at a Parameter Value

For a parametric curve at the point corresponding to $t = t_0$:

1. Compute $x_0 = x(t_0)$ and $y_0 = y(t_0)$ — the point on the curve.
2. Compute $\dfrac{dy}{dx}\bigg|_{t_0}$ via the parametric formula. Call this slope $m$.
3. **Tangent line:** $y - y_0 = m(x - x_0)$.
4. **Normal line:** $y - y_0 = -\dfrac{1}{m}(x - x_0)$ (perpendicular gradient).
5. If $m = 0$: tangent is horizontal, normal is vertical ($x = x_0$).
6. If $\dfrac{dx}{dt} = 0$ at $t_0$: tangent is vertical ($x = x_0$), normal is horizontal.

This is identical to [[Tangents and Normals]] except that the slope is computed parametrically. The geometry is the same.

---

## Connection to Motion — Velocity and Speed

The richest cross-domain payoff. If $(x(t), y(t))$ is the *position* of a moving point at time $t$, then:

- **Velocity vector:** $\mathbf{v}(t) = (\dot{x}, \dot{y}) = \left(\dfrac{dx}{dt}, \dfrac{dy}{dt}\right)$.
- **Speed (scalar):** $\lvert \mathbf{v} \rvert = \sqrt{\dot{x}^2 + \dot{y}^2}$.
- **Direction of motion:** angle $\theta = \arctan(\dot{y}/\dot{x})$ — i.e. the slope of the velocity vector is *exactly* $\dfrac{dy}{dx}$ via the parametric formula.

So the parametric formula $\dfrac{dy}{dx} = \dfrac{\dot{y}}{\dot{x}}$ is also the formula for *the slope of the velocity vector* at any point along the trajectory. **The tangent line to the curve and the velocity vector point in the same direction.** This is geometrically obvious in retrospect — the velocity tells you which way the moving point is going, which is by definition along the tangent — but the parametric calculus is what makes it computable.

### Acceleration

$\mathbf{a}(t) = (\ddot{x}, \ddot{y})$ — the second-derivative-of-position vector. Speed and acceleration in 2D motion is a P4 mechanics topic; the parametric calculus is the underlying technique. See [[Kinematics Calculus]] for the 1D version and [[Newton's Laws of Motion]] for the physics.

> [!info] Why physics keeps Newton's notation
> Recall the [[Stories/The Calculus Priority Dispute|notation-war]] callout: Newton's $\dot{x}$, $\ddot{x}$ survives in physics specifically because *time is special* — physical motion has time as the natural parameter, and the dot is more compact than $\dfrac{dx}{dt}$ when you write equations of motion. Parametric differentiation is where the dot earns its keep: a 2D trajectory's instantaneous slope is just $\dot{y}/\dot{x}$, two characters and a slash, with no $dt$'s to track.

---

## Common Pitfalls

### 1. The second-derivative trap

Already discussed. **$\dfrac{d^2 y}{dx^2}$ is *not* $\dfrac{d^2 y/dt^2}{d^2 x/dt^2}$.** Always re-differentiate $\dfrac{dy}{dx}$ via the chain rule, with the outer $1/(dx/dt)$ factor.

### 2. Forgetting the chain-rule correction in differentiating $\dfrac{dy}{dx}$ with respect to $x$

The expression $\dfrac{dy}{dx}$ is a function of $t$. Differentiating it "with respect to $x$" requires the chain rule: $\dfrac{d}{dx} = \dfrac{1}{dx/dt} \cdot \dfrac{d}{dt}$.

### 3. Dividing by zero at a vertical tangent

When $\dfrac{dx}{dt} = 0$, the formula $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ is undefined. This isn't a flaw — it correctly signals that the tangent is *vertical* (or, in pathological cases, that the curve has a cusp). To find the tangent equation at such a point, the line is $x = x_0$ regardless of slope.

### 4. Choosing the wrong parameter range

A given curve can be parametrised in many ways, and different parametrisations cover different sub-arcs. The unit circle has $(\cos t, \sin t)$ for $t \in [0, 2\pi)$, but also $(\cos 2s, \sin 2s)$ for $s \in [0, \pi)$ — same curve, different speed. The slope $\dfrac{dy}{dx}$ at a *point* is parametrisation-independent; the time it takes to *reach* that point is parametrisation-dependent.

---

## Beyond Syllabus

### Polar and other coordinate systems

The parametric idea generalises massively. **Polar coordinates** $r = r(\theta)$ are a 1-parameter family; treating $\theta$ as the parameter, $x = r(\theta)\cos\theta$, $y = r(\theta)\sin\theta$, and parametric differentiation gives the slope of any polar curve. **Cylindrical and spherical** coordinates extend the idea to 3D. **Frenet frames** in differential geometry are the structured study of how parametric curves bend and twist in space.

### Higher-dimensional parametric

A space curve $(x(t), y(t), z(t))$ is the natural object for 3D motion (planetary orbits, galactic dynamics, spacecraft trajectories). Velocity is $(\dot{x}, \dot{y}, \dot{z})$; speed is $\sqrt{\dot{x}^2 + \dot{y}^2 + \dot{z}^2}$; acceleration is $(\ddot{x}, \ddot{y}, \ddot{z})$. All of multivariable calculus's vector-valued-function machinery (line integrals, arc length $\int \lvert \mathbf{v} \rvert\,dt$, the Frenet-Serret formulas) is built on parametric differentiation.

### Surfaces — two parameters

A surface in 3D is parametrised by two parameters: $(x(u, v), y(u, v), z(u, v))$. The partial derivatives $\partial/\partial u$ and $\partial/\partial v$ generalise $d/dt$. This is where parametric differentiation meets multivariable calculus and lays the foundation for differential geometry, computer graphics (every smooth surface in CGI is parametric), and CAD.

### Robotics

A robotic arm with $n$ joints has its end-effector position given by parametric functions of the $n$ joint angles. **Forward kinematics** (joint angles → position) is a parametric mapping; **inverse kinematics** (desired position → required joint angles) requires solving the parametric equations. Differentiating both gives **Jacobian** velocities that control the arm in real time.

---

## Exam Notes

### Cambridge 9709 (A-Level Mathematics)

**On Paper 3, §3.4** — examined directly. Typical questions: given $x(t), y(t)$, find $\dfrac{dy}{dx}$; find the tangent / normal at a given $t$; find points where tangent is horizontal or vertical.

**The syllabus is explicit: "find and use the *first* derivative of a function which is defined parametrically or implicitly."** **The second-derivative trap is *out of scope for 9709*.** A 9709 student does not need to compute $\dfrac{d^2 y}{dx^2}$ for a parametric curve — but learning the trap anyway is enrichment that pays off for other curricula and for the broader habit of *not trusting "ratio of operations" shortcuts*.

The §3.4 differentiation trio — Quotient, Implicit, Parametric — closes 9709 P3 §3.4 fully. Once those three plus Chain + Product are landed, every P3 differentiation question yields.

### Cambridge 0606 (Additional Mathematics)

**Not on the 0606 syllabus.** Parametric is an A-Level topic.

### A-Level (Edexcel / AQA / OCR)

**Standard A2 topic** in all three boards. Examined directly and often combined with [[Connected Rates of Change]] in physics-flavoured questions.

### IB AA HL

**On the syllabus** (Topic 5, Calculus). Includes second derivative of parametric form — the trap is genuine exam material here.

### IB AA SL

Not on SL.

### AP Calculus AB / BC

**On BC only** (Unit 9 — Parametric Equations, Polar Coordinates, and Vector-Valued Functions). AB does not cover parametric. **Topic 9.2: Second Derivatives of Parametric Equations** is *literally one of the named topics on the syllabus* (CED CHA-3.G.3).

That said: Unit 9 is ~11–12% of the BC exam, spread across 9 topics, so 9.2 alone averages ~1.2% of total exam weight. **In practice it's tested rarely as a standalone FRQ part** — when parametric appears in an FRQ, it's usually motion-in-the-plane (Topic 9.6) for the bulk of the marks. The second-derivative trap surfaces more commonly in MCQs than FRQs, and even there only a handful of times in the last decade of released exams. So: *learn the trap because it's pedagogically permanent, not because it's exam-frequent.*

### Beyond high school — University

Single-variable courses complete the technique; multivariable courses generalise it (partial derivatives, Jacobians, Frenet frames). Differential geometry, classical mechanics, robotics, computer graphics, and orbital mechanics all run on parametric differentiation as a foundational tool.

---

## Connections

- **Direct prerequisite:** [[Chain Rule]] — parametric differentiation is the chain rule applied to $y(t)$ via $t = f^{-1}(x)$. The whole technique is one chain-rule move.
- **Sibling techniques (the §3.4 trio):** [[Quotient Rule]], [[Implicit Differentiation]] — together with Parametric, these are the three tools that close 9709 P3 §3.4. Each handles a different "shape" of curve description; all reduce to the chain rule under the hood.
- **Direct application:** [[Tangents and Normals]] — parametric curves use the same tangent/normal geometry; only the slope formula changes. [[Connected Rates of Change]] — when one variable's rate of change is the parameter, parametric differentiation IS connected rates.
- **Cross-domain bridge — motion:** [[Kinematics Calculus]] — the 1D version of motion calculus. In 2D, parametric differentiation is exactly velocity-and-acceleration calculus. [[Newton's Laws of Motion]] uses parametric form whenever motion is in two or three dimensions, which is most of the time.
- **Cross-domain bridge — geometry:** the cycloid in Example 4 connects to [[Stories/The Bernoulli Family]] (the 1696 brachistochrone challenge) and to [[Optimisation]] §"Calculus of Variations." The cycloid is parametric calculus's most famous payoff.
- **For 9709 students:** [[MF19 Reference (9709)]] — *no formula given*; parametric differentiation is a *technique* (chain rule applied to a parametrisation), not a formula. Memorise the one-line shape $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ and the second-derivative trap.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ | `\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}` | The master formula. Chain rule + inverse-function rule. |
| $\dfrac{dy}{dx} = \dfrac{\dot{y}}{\dot{x}}$ | `\dfrac{dy}{dx} = \dfrac{\dot{y}}{\dot{x}}` | Newton's-dot version; standard in physics (time as parameter). |
| $\dfrac{d^2 y}{dx^2} = \dfrac{1}{dx/dt}\cdot\dfrac{d}{dt}\!\left(\dfrac{dy}{dx}\right)$ | `\dfrac{d^2 y}{dx^2} = \dfrac{1}{dx/dt}\cdot\dfrac{d}{dt}\!\left(\dfrac{dy}{dx}\right)` | Correct second derivative — the chain-rule version. |
| $\dfrac{d^2 y}{dx^2} \neq \dfrac{d^2 y/dt^2}{d^2 x/dt^2}$ | `\dfrac{d^2 y}{dx^2} \neq \dfrac{d^2 y/dt^2}{d^2 x/dt^2}` | The trap — most common parametric error. |
| $\mathbf{v}(t) = (\dot{x}, \dot{y})$ | `\mathbf{v}(t) = (\dot{x}, \dot{y})` | Velocity vector along a parametric trajectory. |
| $\lvert \mathbf{v} \rvert = \sqrt{\dot{x}^2 + \dot{y}^2}$ | `\lvert \mathbf{v} \rvert = \sqrt{\dot{x}^2 + \dot{y}^2}` | Speed (scalar magnitude of velocity). |
| $x = a(t - \sin t),\; y = a(1 - \cos t)$ | `x = a(t - \sin t),\; y = a(1 - \cos t)` | The cycloid — Example 4, the brachistochrone curve. |
