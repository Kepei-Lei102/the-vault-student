---
chinese: 隐函数求导 (yǐn hánshù qiúdǎo)
prerequisites:
  - "[[Chain Rule]]"
  - "[[Quotient Rule]]"
  - "[[Differentiation Rules]]"
  - "[[Differentiation]]"
leads_to:
  - "[[Logarithmic Differentiation]]"
  - "[[Connected Rates of Change]]"
  - "[[Tangents and Normals]]"
  - "[[Parametric Differentiation]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/IB-HL
  - level/AP
  - level/university
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-3-4
  - syllabus/9231-2-3
  - syllabus/9709-2-4
  - type/technique
  - type/theorem
  - notation/derivative
  - notation/leibniz
  - misconception/implicit-forget-chain-rule
  - misconception/implicit-treat-y-as-constant
---

# Implicit Differentiation 隐函数求导

> *Most curves you'll meet aren't graphs of $y = f(x)$. Circles, ellipses, level sets, equations of state, $\sin(xy) = x$ — none of them solve cleanly for $y$. You need a tangent slope anyway.*
>
> *Implicit Differentiation is the calculus technique that says: **treat $y$ as a function of $x$ even when you can't write down the function**, apply the chain rule wherever $y$ appears, and solve the resulting equation for $\dfrac{dy}{dx}$.*

## What this card is for

Up to this point, every differentiation has assumed an explicit form $y = f(x)$ — you have the function, you apply the rules, you get $f'(x)$. But the most important curves in geometry, physics, and economics aren't given that way. Three quick examples:

- The **circle** $x^2 + y^2 = 25$. You *could* solve for $y = \pm\sqrt{25 - x^2}$, but you'd need two separate functions for the upper and lower halves, and the algebra at $x = \pm 5$ becomes singular.
- The **ellipse** $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$. Same situation. And ellipses appear everywhere — planetary orbits, cross-sections of cones, statistical confidence regions.
- The **folium of Descartes** $x^3 + y^3 = 6xy$. *Cannot* be solved for $y$ in elementary functions. Yet the curve has tangents at every regular point, and you can find them.

Implicit Differentiation handles all three uniformly. It's the technique that makes calculus work on curves you cannot solve. The cost is one piece of conceptual furniture: **whenever you differentiate an expression that contains $y$, you must apply the chain rule because $y$ is secretly a function of $x$.** That's it. The rest is bookkeeping.

## The Technique

Given an implicit relation $F(x, y) = 0$ (or any equation containing both $x$ and $y$):

1. **Differentiate both sides with respect to $x$**, treating every $y$ as a function $y(x)$.
2. **Whenever a $y$ is differentiated, apply the chain rule** — the derivative of any expression in $y$ is the derivative as if $y$ were the variable, multiplied by $\dfrac{dy}{dx}$.
3. **Collect all $\dfrac{dy}{dx}$ terms on one side**, factor, and solve for $\dfrac{dy}{dx}$.

The single rule that does all the work, in Leibniz form:

$$\boxed{\;\dfrac{d}{dx}\bigl[g(y)\bigr] = g'(y)\,\dfrac{dy}{dx}\;}$$

So $\dfrac{d}{dx}[y^2] = 2y \cdot \dfrac{dy}{dx}$, $\dfrac{d}{dx}[\sin y] = \cos y \cdot \dfrac{dy}{dx}$, $\dfrac{d}{dx}[\ln y] = \dfrac{1}{y} \cdot \dfrac{dy}{dx}$, and so on. Every entry in the [[Differentiation Rules]] table extends to its implicit version by appending the chain-rule factor $\dfrac{dy}{dx}$.

> [!warning] The single most common error
> Forgetting the chain-rule factor on the $y$-terms. A student who differentiates $x^2 + y^2 = 25$ and writes "$2x + 2y = 0$" has missed the chain rule. The correct line is $2x + 2y \cdot \dfrac{dy}{dx} = 0$. **Whenever a $y$ is differentiated, attach $\dfrac{dy}{dx}$ — every time, no exceptions.** The Leibniz notation $\dfrac{d}{dx}$ explicitly reminds you of this; "primes" notation tends to conceal it.

## An Equivalent Form — the Symmetric Differential

There is a beautiful and often-cleaner alternative to "differentiate both sides with respect to $x$": **take the differential of both sides.** The recipe is even simpler than the standard one:

> **When you differentiate an $x$, append $dx$. When you differentiate a $y$, append $dy$.**

That's it. Apply on $x^2 + y^2 = 25$:

$$2x\,dx + 2y\,dy = 0.$$

This single equation contains both derivatives at once. Solving for $\dfrac{dy}{dx}$:

$$\dfrac{dy}{dx} = -\dfrac{x}{y}. \quad \text{(divide both sides by } dx\text{)}$$

Solving for $\dfrac{dx}{dy}$:

$$\dfrac{dx}{dy} = -\dfrac{y}{x}. \quad \text{(divide both sides by } dy\text{)}$$

**One pass, two derivatives.** Useful for vertical-tangent problems (where $dy/dx \to \infty$ but $dx/dy = 0$ is finite and clean), for inverse functions, and as a stepping stone into multivariable calculus.

### Why it works — the total differential

The differential form is the **total differential** identity from multivariable calculus, applied to a constraint surface. For any smooth $F(x, y)$:

$$dF = \dfrac{\partial F}{\partial x}\,dx + \dfrac{\partial F}{\partial y}\,dy.$$

If $F(x, y) = 0$ along a curve, then $dF = 0$ along that curve, so

$$\dfrac{\partial F}{\partial x}\,dx + \dfrac{\partial F}{\partial y}\,dy = 0.$$

This is exactly the equation produced by "append $dx$ next to each $x$-derivative, $dy$ next to each $y$-derivative." From it you read

$$\dfrac{dy}{dx} = -\dfrac{\partial F / \partial x}{\partial F / \partial y}, \qquad \dfrac{dx}{dy} = -\dfrac{\partial F / \partial y}{\partial F / \partial x}$$

which is the closed-form Implicit Function Theorem (see the Beyond Syllabus section below). The differential form is the IFT, written one level less abstractly.

> [!info] When does the differential form work?
> **Always equivalent to standard implicit differentiation, with one shared caveat: at singular points** where *both* $\partial F/\partial x = 0$ and $\partial F/\partial y = 0$, the equation collapses to $0\,dx + 0\,dy = 0$ — true but uninformative. Both methods fail simultaneously and equivalently at such points (self-intersections, cusps, isolated points). Wherever one method gives a sensible answer, so does the other.
>
> One small ergonomic warning: for **higher derivatives** $\dfrac{d^2 y}{dx^2}$, the differential form needs second differentials and gets clunky. Standard $\dfrac{d}{dx}$ form is cleaner above first order. Use the differential form for first derivatives and switching between $dy/dx$ and $dx/dy$; switch to standard form for $y''$.

### Worked example via the differential form — the folium

Same curve as Example 2 below, by the differential method:

$$3x^2\,dx + 3y^2\,dy = 6y\,dx + 6x\,dy.$$

(Each $x$-derivative gained $dx$; each $y$-derivative gained $dy$; the product term $6xy$ produced $6y\,dx + 6x\,dy$ by the *symmetric* product-rule version $d(uv) = u\,dv + v\,du$.)

Collect:

$$(3y^2 - 6x)\,dy = (6y - 3x^2)\,dx \;\Longrightarrow\; \dfrac{dy}{dx} = \dfrac{6y - 3x^2}{3y^2 - 6x} = \dfrac{2y - x^2}{y^2 - 2x}.$$

Same answer as Example 2 below; arguably cleaner derivation. The differential form's symmetry — every $x$ and every $y$ playing equivalent roles until the very end — is its main pedagogical virtue.

> [!tip] Pedagogical bottom line
> If "treat $y$ as a function of $x$ and apply the chain rule" feels like a contortion, **try the differential form first**. It's symmetric, easier to remember, and gives both derivatives at once. If you're heading into multivariable calculus, differential geometry, or thermodynamics, the differential form is the dominant idiom — you'll meet it again as $dF = \nabla F \cdot d\mathbf{r}$, as Pfaffian forms, and as exact differentials. Learning it now saves a re-translation later.

## 中文锚点

**隐函数求导**：当方程 $F(x, y) = 0$ 不能（或者很难）显式解出 $y$ 时，仍然可以求 $\dfrac{dy}{dx}$ 的方法。

**核心思想**：把 $y$ 看作 $x$ 的（暗藏的）函数 $y(x)$，对方程两边同时关于 $x$ 求导。每当遇到含 $y$ 的项，按链式法则处理 —— 多乘一个 $\dfrac{dy}{dx}$。

**口诀**：

> **见 $y$ 求导，必带 $\dfrac{dy}{dx}$。**

三步走：

1. 两边对 $x$ 求导。
2. 含 $y$ 的项，链式法则补上 $\dfrac{dy}{dx}$。
3. 把 $\dfrac{dy}{dx}$ 集合到一边，解出。

经典例子：单位圆 $x^2 + y^2 = 1$，两边求导得 $2x + 2y\dfrac{dy}{dx} = 0$，所以 $\dfrac{dy}{dx} = -\dfrac{x}{y}$。这就是隐函数求导的全部精神。

> 反三角函数的导数（$\arcsin' = 1/\sqrt{1-x^2}$ 等）也是用这个技术从定义方程 $\sin y = x$ 推出来的 —— 见 [[Differentiation Rules]]。

---

## Why It Works — The Chain Rule, Wearing No Disguise

Implicit Differentiation is not a new theorem; it's the **chain rule with the costume off**. Here's the picture.

Suppose $F(x, y) = 0$ defines $y$ as a function of $x$ in some neighbourhood — call that function $y = y(x)$, even if we can't write it explicitly. Substitute back:

$$F(x, y(x)) = 0 \quad \text{for all } x \text{ in the neighbourhood}.$$

The left side is a function of $x$ alone (composition through $y(x)$), and it's identically zero. So its derivative is zero:

$$\dfrac{d}{dx}\bigl[F(x, y(x))\bigr] = 0.$$

Computing this derivative requires the chain rule, applied to every place $x$ appears (including the disguised place inside $y(x)$). Concretely, if $F(x, y) = x^2 + y^2 - 25$:

$$\dfrac{d}{dx}\bigl[x^2 + y(x)^2 - 25\bigr] = 2x + 2y(x) \cdot y'(x) = 0.$$

Solving: $y'(x) = -\dfrac{x}{y(x)} = -\dfrac{x}{y}$.

That's all there is. The "treat $y$ as a function of $x$" instruction is *literally* the substitution $y \mapsto y(x)$, and the "chain rule on $y$" instruction is *literally* the chain rule on the composition $y(x)$. Implicit Differentiation is what the chain rule looks like when you commit to the substitution but don't bother to write it down explicitly.

### When does $F(x, y) = 0$ even define $y$ as a function of $x$?

The procedure tacitly assumes there *is* a function $y(x)$. That assumption isn't free — and it's the depth this card preserves for the implicit-function-theorem callout below. For now, the practical rule is: at any point $(x_0, y_0)$ on the curve where $\dfrac{\partial F}{\partial y} \neq 0$, the curve is locally the graph of a function $y = y(x)$, and Implicit Differentiation works. Where $\dfrac{\partial F}{\partial y} = 0$, the curve has a vertical tangent (or worse — a singularity, like the self-intersection of the folium of Descartes at the origin) and implicit differentiation may fail or need extra care.

---

## Worked Examples

### Example 1 — The Circle $x^2 + y^2 = 25$

Differentiate both sides with respect to $x$:

$$2x + 2y\,\dfrac{dy}{dx} = 0 \;\Longrightarrow\; \dfrac{dy}{dx} = -\dfrac{x}{y}.$$

**Sanity check.** At $(3, 4)$ on the upper semicircle, $\dfrac{dy}{dx} = -\dfrac{3}{4}$. The radius from origin to $(3, 4)$ has slope $\tfrac{4}{3}$; the tangent should be perpendicular, with slope $-\tfrac{3}{4}$. ✓ The implicit answer matches the geometric one.

**Vertical tangents** at $(\pm 5, 0)$, where $y = 0$ makes the formula undefined. *That's the point* — at those locations, the tangent is genuinely vertical (slope $\pm\infty$), and the formula's failure is the formula being honest. Implicit Differentiation tells you *where* the bad points are, not just the slopes at the good points.

### Example 2 — The Folium of Descartes $x^3 + y^3 = 6xy$

A curve that *cannot* be solved for $y$ in elementary functions. Differentiate both sides:

$$3x^2 + 3y^2\,\dfrac{dy}{dx} = 6y + 6x\,\dfrac{dy}{dx}.$$

(The right-hand side $6xy$ is a product, so we used the [[Product Rule]]: $\tfrac{d}{dx}[6xy] = 6y + 6x \cdot \tfrac{dy}{dx}$ — first factor's derivative times second, plus first times second's derivative-with-chain-rule.)

Collect $\dfrac{dy}{dx}$ terms:

$$3y^2\,\dfrac{dy}{dx} - 6x\,\dfrac{dy}{dx} = 6y - 3x^2 \;\Longrightarrow\; \dfrac{dy}{dx} = \dfrac{6y - 3x^2}{3y^2 - 6x} = \dfrac{2y - x^2}{y^2 - 2x}.$$

**At the point $(3, 3)$**, which lies on the curve ($27 + 27 = 54 = 6 \cdot 3 \cdot 3$ ✓): $\dfrac{dy}{dx} = \dfrac{6 - 9}{9 - 6} = -1$. The tangent is the line $y - 3 = -(x - 3)$, i.e. $y = -x + 6$.

This curve has a famous self-intersection at the origin: $\dfrac{dy}{dx}$ is $\tfrac{0}{0}$ there. The origin is *not* a regular point of the curve, and implicit differentiation legitimately reports the singularity by failing.

### Example 3 — A Trigonometric Implicit Equation $\sin(xy) = x$

Differentiate both sides; the left side needs the chain rule on $\sin$ *and* the product rule on $xy$:

$$\cos(xy) \cdot \bigl(y + x\,\dfrac{dy}{dx}\bigr) = 1.$$

Solve:

$$y\cos(xy) + x\cos(xy)\,\dfrac{dy}{dx} = 1 \;\Longrightarrow\; \dfrac{dy}{dx} = \dfrac{1 - y\cos(xy)}{x\cos(xy)}.$$

The chain-rule factor $\dfrac{dy}{dx}$ appeared because $xy$ depends on $x$ both directly (the $x$ factor) and through $y(x)$ (the $y$ factor) — Product Rule does the bookkeeping. This is the kind of compound implicit differentiation that appears in 9709 P3 and IB AA HL.

### Example 4 — Deriving $(\arcsin x)' = \dfrac{1}{\sqrt{1 - x^2}}$

The most leveraged use of Implicit Differentiation: deriving the inverse-trig derivatives that fill out the [[Differentiation Rules]] table. The technique is short and self-contained.

Let $y = \arcsin x$ with $y \in [-\tfrac{\pi}{2}, \tfrac{\pi}{2}]$. By definition, $\sin y = x$. Differentiate both sides with respect to $x$:

$$\cos y \cdot \dfrac{dy}{dx} = 1 \;\Longrightarrow\; \dfrac{dy}{dx} = \dfrac{1}{\cos y}.$$

We need $\cos y$ in terms of $x$. From $\sin y = x$ and the Pythagorean identity $\sin^2 y + \cos^2 y = 1$, we get $\cos y = \sqrt{1 - x^2}$ (positive square root because $y \in [-\tfrac{\pi}{2}, \tfrac{\pi}{2}]$ where $\cos y \geq 0$).

$$\boxed{\;\dfrac{d}{dx}\arcsin x = \dfrac{1}{\sqrt{1 - x^2}}\;}$$

Identical technique gives $(\arccos x)' = -\dfrac{1}{\sqrt{1 - x^2}}$ (or by the cofunction identity $\arccos x = \tfrac{\pi}{2} - \arcsin x$) and $(\arctan x)' = \dfrac{1}{1 + x^2}$ (using $1 + \tan^2 y = \sec^2 y$). The whole inverse-trig family lives downstream of one Implicit Differentiation move.

> [!info] The general inverse-function rule
> *Recall that an inverse function $g = f^{-1}$ satisfies $f(g(x)) = x$ — the defining equation of the inverse.* Differentiate implicitly: $f'(g(x)) \cdot g'(x) = 1$, so
> $$g'(x) = \dfrac{1}{f'(g(x))} = \dfrac{1}{f'(y)}\bigg|_{y = g(x)}.$$
> This is the **Inverse Function Rule** — the universal formula for the derivative of an inverse, with implicit differentiation supplying the proof in two lines. Every entry on the inverse-trig and inverse-hyperbolic derivative table is one application of this rule.

### Example 5 — Higher-order: Finding $\dfrac{d^2 y}{dx^2}$ on the Circle

Sometimes you need the second derivative of an implicit relation. Continue from Example 1: $\dfrac{dy}{dx} = -\dfrac{x}{y}$. Differentiate again, using the [[Quotient Rule]] (and remembering $y$ depends on $x$):

$$\dfrac{d^2 y}{dx^2} = \dfrac{d}{dx}\!\left(-\dfrac{x}{y}\right) = -\dfrac{(1)(y) - (x)(dy/dx)}{y^2} = -\dfrac{y - x \cdot (-x/y)}{y^2} = -\dfrac{y + x^2/y}{y^2} = -\dfrac{y^2 + x^2}{y^3}.$$

Using $x^2 + y^2 = 25$:

$$\dfrac{d^2 y}{dx^2} = -\dfrac{25}{y^3}.$$

Concavity follows directly: for the upper semicircle ($y > 0$), $y'' < 0$ — concave down, as the geometry confirms. For the lower semicircle ($y < 0$), $y'' > 0$ — concave up. The formula contains both halves of the circle in one expression.

---

## Tangent Lines and Vertical Tangents

For an implicit curve, finding the tangent at a point $(x_0, y_0)$:

1. Differentiate implicitly to get $\dfrac{dy}{dx}$ as an expression in $x$ and $y$.
2. Substitute $(x_0, y_0)$ to get the slope $m$.
3. Write the tangent: $y - y_0 = m(x - x_0)$.

**Horizontal tangents** occur where $\dfrac{dy}{dx} = 0$ — i.e. the *numerator* of the implicit-derivative expression vanishes (with denominator non-zero).

**Vertical tangents** occur where $\dfrac{dy}{dx}$ is undefined in a controlled way — the *denominator* vanishes while the numerator doesn't. Geometrically, this means the curve is locally the graph of $x$ as a function of $y$, with the role of independent and dependent variables swapped. At those points, $\dfrac{dx}{dy} = 0$.

> [!tip] How to find vertical tangents systematically
> If $\dfrac{dy}{dx} = \dfrac{N(x, y)}{D(x, y)}$, vertical tangents are at points satisfying $D(x, y) = 0$ on the curve. Solve $\{F(x, y) = 0 \text{ AND } D(x, y) = 0\}$ as a system. Example: on the folium $x^3 + y^3 = 6xy$ with $\dfrac{dy}{dx} = \dfrac{2y - x^2}{y^2 - 2x}$, vertical tangents satisfy $y^2 = 2x$ together with the curve equation. Substitute and solve — the vertical tangent is at $(\sqrt[3]{4}\cdot \sqrt[3]{2}, \cdot)$ ... pleasant exercise in implicit-curve geometry.

---

## Common Pitfalls

### 1. Forgetting the chain rule on $y$-terms

The single most common error. *"$\dfrac{d}{dx}(y^2) = 2y$"* — wrong, missed the chain-rule factor. **The Leibniz notation $\dfrac{d}{dx}$ is a continuous reminder; primes notation hides the issue.** Use Leibniz when first learning, switch to primes only when the chain-rule habit is automatic.

### 2. Treating $y$ as a constant

Closely related. A student writes $\dfrac{d}{dx}(xy) = y$ — *forgetting* the second product-rule term. Correct: $\dfrac{d}{dx}(xy) = y + x\dfrac{dy}{dx}$. Whenever a *product* of $x$- and $y$-stuff appears, **two terms** come out.

### 3. Differentiating only one side

Implicit differentiation requires differentiating *both sides* of the equation. A subtle case: $x^2 + y^2 = 25$ — students sometimes "lose" the right side because $\dfrac{d}{dx}(25) = 0$ feels invisible. Always write the zero down: it's the "$=0$" that makes the whole equation work.

### 4. Mixing up implicit derivative and total derivative

If $z = F(x, y)$ where $y$ also depends on $x$, the *total* derivative of $z$ with respect to $x$ uses both partial derivatives: $\dfrac{dz}{dx} = \dfrac{\partial F}{\partial x} + \dfrac{\partial F}{\partial y}\dfrac{dy}{dx}$. Implicit differentiation is the special case where $z = 0$ (so $dz/dx = 0$) and you solve for $\dfrac{dy}{dx}$. This is multivariable territory, but it's worth knowing the connection — Implicit Differentiation is a one-equation special case of total derivatives.

### 5. Solving for $\dfrac{dy}{dx}$ before collecting terms

After implicit differentiation, the equation will typically have $\dfrac{dy}{dx}$ in *multiple* terms. Don't divide too early. **Collect all $\dfrac{dy}{dx}$ terms on one side first, then factor.** Common error: a student moves one term, divides, then realises another $\dfrac{dy}{dx}$ was hiding elsewhere.

---

## Beyond Syllabus — The Implicit Function Theorem

The technical question implicit differentiation tacitly assumed is: *when does an equation $F(x, y) = 0$ actually define $y$ as a function of $x$ near a given point?* The answer is one of the most elegant theorems in multivariable calculus.

> **Implicit Function Theorem (informal).** Let $F(x, y)$ be continuously differentiable near $(x_0, y_0)$, and suppose $F(x_0, y_0) = 0$. If $\dfrac{\partial F}{\partial y}(x_0, y_0) \neq 0$, then there exist a neighbourhood $U$ of $x_0$ and a continuously differentiable function $y = y(x)$ on $U$, such that $y(x_0) = y_0$ and $F(x, y(x)) = 0$ on $U$. Moreover,
> $$\dfrac{dy}{dx} = -\dfrac{\partial F / \partial x}{\partial F / \partial y}.$$

Three things this theorem does:

1. **Justifies implicit differentiation.** Wherever $\dfrac{\partial F}{\partial y} \neq 0$, the procedure is rigorously valid — $y(x)$ exists, it's differentiable, and the derivative is the formula we computed by hand.
2. **Locates the failures.** Wherever $\dfrac{\partial F}{\partial y} = 0$, the procedure may fail. Vertical tangents, self-intersections, cusps — all signalled by $\partial F / \partial y$ vanishing.
3. **Generalises massively.** The same theorem works for systems of equations and several "dependent" variables — it's the foundation of differential geometry (smooth manifolds defined by implicit equations), constrained optimisation (Lagrange multipliers), differential topology, and the theory of ordinary and partial differential equations (existence and uniqueness of solutions).

The closed formula $\dfrac{dy}{dx} = -\dfrac{\partial F / \partial x}{\partial F / \partial y}$ is a **shortcut** for implicit differentiation: instead of differentiating $F(x, y) = 0$ by hand, take the partial derivatives and divide. For the circle $F = x^2 + y^2 - 25$: $\partial F / \partial x = 2x$, $\partial F / \partial y = 2y$, so $\dfrac{dy}{dx} = -\dfrac{2x}{2y} = -\dfrac{x}{y}$. Same answer, two lines. (The shortcut requires multivariable partial-derivative notation, which is why it's saved for university — but the *method* is exactly what you've been doing on the implicit-differentiation problems.)

> [!info] Connection to constraint-counting
> *Recall from [[Forward Reading and Problem Discovery]] that "constraints reduce degrees of freedom"* — every invariant a hunter grabs is one constraint. The Implicit Function Theorem is the formal statement of that principle for smooth equations. A point in the plane has 2 degrees of freedom; the constraint $F(x, y) = 0$ removes one, leaving a 1-dimensional curve. Implicit differentiation is the calculus of moving along that 1-dimensional curve — a $\dfrac{dy}{dx}$ slope is the rate at which $y$ changes when $x$ moves by 1, *along the constraint*. The "constraints reduce degrees of freedom" framing makes implicit differentiation visible as the calculus of moving along constraints, not against them.

---

## Cross-Domain Applications

### Connected rates of change (time-derivative version)

[[Connected Rates of Change]] is *implicit differentiation with respect to time*. The geometric relation $V = \tfrac{4}{3}\pi r^3$ becomes, under $\dfrac{d}{dt}$, the relation $\dfrac{dV}{dt} = 4\pi r^2 \dfrac{dr}{dt}$ — the chain rule on $r(t)$ supplies the $\dfrac{dr}{dt}$. Same technique, time as the independent variable. Cambridge usually presents the time version as a separate topic; conceptually it's one move.

### Differential equations

Many ODEs are most naturally written implicitly. A separable ODE $\dfrac{dy}{dx} = g(x) h(y)$ separates to $\dfrac{1}{h(y)}\,dy = g(x)\,dx$ and integrates to an implicit relation $H(y) = G(x) + C$. To recover $\dfrac{dy}{dx}$ from this, you implicit-differentiate. The whole "first-order separable ODE" technique is a round trip through implicit form.

### Equations of state in physics

The ideal gas law $PV = nRT$ is an implicit relation among pressure, volume, and temperature. To find $\dfrac{\partial P}{\partial V}$ at fixed temperature (used in calculating bulk modulus, sound-wave speed, thermodynamic stability), implicit differentiation. The Van der Waals equation $\bigl(P + \tfrac{an^2}{V^2}\bigr)(V - nb) = nRT$ is more complicated and *only* yields to implicit differentiation — there's no clean explicit form for $P(V, T)$.

### Level sets and gradient geometry

In 2D, a level set $f(x, y) = c$ is an implicit curve. The gradient $\nabla f = (\partial f / \partial x, \partial f / \partial y)$ is **perpendicular** to the level set at every point — and this is *equivalent* to the implicit-differentiation formula $\dfrac{dy}{dx} = -\dfrac{\partial f / \partial x}{\partial f / \partial y}$ (the negative reciprocal of the gradient's slope). Level sets, gradient flow, optimisation under constraints — implicit differentiation is the bridge from one-variable calculus to all of them.

### Economics — indifference curves and budget constraints

A consumer's indifference curve is the level set of a utility function $U(x, y) = c$, where $x$ and $y$ are quantities of two goods. The marginal rate of substitution (MRS) — how much of $y$ you'd give up for one more $x$ at constant utility — is $-\dfrac{dy}{dx}$ along the indifference curve, computed by implicit differentiation. The whole microeconomic theory of consumer choice runs on this calculation.

---

## Exam Notes

### Cambridge 9709 (A-Level Mathematics)

**On Paper 3, §3.4** — examined directly. Typical questions: differentiate $x^2 + xy + y^3 = 7$ implicitly, find the tangent at a given point, find points where the tangent is horizontal/vertical. Sometimes combined with a related-rates twist. Examiners care about the chain-rule factor on $y$-terms — write $\dfrac{dy}{dx}$ explicitly every time.

**Not on Paper 1** — Paper 1 differentiation is explicit only.

### Cambridge 0606 (Additional Mathematics)

**Not on the syllabus.** 0606 covers explicit differentiation only. Implicit differentiation is an A-Level topic.

### Cambridge 0580

**Not examined** — Extended's calculus differentiates explicit polynomials only.

### Cambridge 9231 (Further Maths)

Assumed from P3 and then *worked harder*: FP2's differentiation row leans on **iterated implicit differentiation** as its Maclaurin engine — the real November 2025 shape asks for the series of $\tan x$ by differentiating $y' = 1 + y^2$ implicitly again and again ([[Maclaurin Series]] works it in full). No new rule; the P3 skill run at FP2 stamina.

### Edexcel IAL / OxAQA 9660

IAL examines implicit differentiation at **P4** (alongside parametric — the two arrive as a pair); OxAQA 9660 at **P2.6**, same pairing. Both map-checked; both set the standard tangent/normal and horizontal-tangent shapes, with related rates as the context twist.

### IB AA HL

**On the syllabus** (Topic 5). Examined directly; sometimes used as the proof technique for inverse-trig derivatives. Strong students should be able to derive $(\arcsin x)'$ on demand using implicit differentiation.

### IB AA SL

**Not formally on the SL syllabus**, but appears in some textbooks as enrichment. SL handles only explicit differentiation.

### AP Calculus AB / BC

**On both AB and BC syllabuses** (Unit 3 — Differentiation: Composite, Implicit, and Inverse Functions). One of the canonical AP topics; examined every year in the free-response section. AP graders want clean work — show $\dfrac{dy}{dx}$ explicitly in every step.

### Beyond high school — University

The Implicit Function Theorem (above) is the rigorous foundation. First-year multivariable calculus extends the technique to $F(x_1, \ldots, x_n, y_1, \ldots, y_m) = 0$ — systems of equations where several "dependent" variables are determined by several "independent" ones. The Jacobian determinant $\det\bigl[\partial F_i / \partial y_j\bigr]$ replaces the single $\partial F / \partial y$ as the non-vanishing condition; the whole apparatus of differential geometry, Lagrange multipliers, and constrained optimisation builds on it.

---

## Connections

- **Direct prerequisite:** [[Chain Rule]] — Implicit Differentiation is the chain rule applied to $y(x)$ inside $F(x, y) = 0$. Every implicit derivative is one chain-rule application per $y$-occurrence.
- **Sibling technique:** [[Logarithmic Differentiation]] — for $y = f(x)^{g(x)}$ where neither power rule nor exponential rule applies, take $\ln$ of both sides and *implicit-differentiate* the resulting $\ln y = g(x) \ln f(x)$. Logarithmic differentiation IS implicit differentiation, applied after a log-rewrite.
- **Twin technique:** [[Connected Rates of Change]] — implicit differentiation with respect to time. Same machinery, time as the independent variable, physical-quantity setting. The cards are the static and dynamic faces of one technique.
- **Parametric companion:** [[Parametric Differentiation]] — when $x$ and $y$ are *both* given as functions of a parameter $t$, $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$. Closes 9709 P3 §3.4 alongside Implicit and Quotient.
- **Inverse-trig derivations:** [[Differentiation Rules]] — the inverse-trig entries ($\arcsin'$, $\arccos'$, $\arctan'$) are derived on that card by implicit differentiation; this card now provides the canonical statement of the technique they used.
- **Application:** [[Tangents and Normals]] — implicit-curve tangents and normals work the same way as explicit ones; the only new thing is the implicit derivative formula. Vertical tangents are detected by denominator-vanishes-but-numerator-doesn't.
- **Cross-domain bridges:** the Implicit Function Theorem and gradient geometry connect implicit differentiation to differential geometry, constrained optimisation, level sets, equations of state in physics, and indifference curves in economics — see "Cross-Domain Applications" above.
- **Foundational principle:** [[Forward Reading and Problem Discovery]] — implicit differentiation is the calculus operationalisation of "constraints reduce degrees of freedom." A 2D plane plus a 1-dimensional constraint $F(x, y) = 0$ leaves a 1-dimensional curve, and $\dfrac{dy}{dx}$ is the rate of motion along that curve.
- **For 9709 students:** [[MF19 Reference (9709)]] — *no formula given*; implicit differentiation is a *technique*, not a formula. The differentiation table on MF19 supplies the $g'(y)$ part (e.g. $\sin' = \cos$); the chain-rule factor $\dfrac{dy}{dx}$ is your responsibility to remember.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{d}{dx}\bigl[g(y)\bigr] = g'(y)\,\dfrac{dy}{dx}$ | `\dfrac{d}{dx}\bigl[g(y)\bigr] = g'(y)\,\dfrac{dy}{dx}` | The master rule; chain rule applied to $y(x)$. |
| $dF = \dfrac{\partial F}{\partial x}\,dx + \dfrac{\partial F}{\partial y}\,dy$ | `dF = \dfrac{\partial F}{\partial x}\,dx + \dfrac{\partial F}{\partial y}\,dy` | Total differential — the symmetric form. Setting $dF = 0$ on the curve gives both $dy/dx$ and $dx/dy$ in one pass. |
| $d(uv) = u\,dv + v\,du$ | `d(uv) = u\,dv + v\,du` | Product rule, differential form — symmetric in $u$ and $v$. |
| $\dfrac{dy}{dx} = -\dfrac{\partial F / \partial x}{\partial F / \partial y}$ | `\dfrac{dy}{dx} = -\dfrac{\partial F / \partial x}{\partial F / \partial y}` | Implicit Function Theorem closed-form (multivariable / university-level). |
| $\partial F / \partial y$ | `\partial F / \partial y` | Partial derivative — used in IFT condition. The non-vanishing of this is the local-graph criterion. |
| $\sin y = x \;\Longrightarrow\; \dfrac{dy}{dx} = \dfrac{1}{\sqrt{1 - x^2}}$ | `\sin y = x \;\Longrightarrow\; \dfrac{dy}{dx} = \dfrac{1}{\sqrt{1 - x^2}}` | The implicit derivation of $(\arcsin x)'$, in one notational chain. |
| $x^2 + y^2 = 25 \;\Longrightarrow\; \dfrac{dy}{dx} = -\dfrac{x}{y}$ | `x^2 + y^2 = 25 \;\Longrightarrow\; \dfrac{dy}{dx} = -\dfrac{x}{y}` | The canonical circle example. |
| $\dfrac{d^2 y}{dx^2}$ | `\dfrac{d^2 y}{dx^2}` | Second derivative; computed by differentiating $\dfrac{dy}{dx}$ and using the implicit relation again. |
