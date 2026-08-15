---
chinese: 微分方程 (wēifēn fāngchéng)
prerequisites:
  - "[[Integration]]"
  - "[[Standard Integrals]]"
  - "[[Differentiation]]"
  - "[[Partial Fractions]]"
  - "[[Exponential Function]]"
  - "[[Logarithms]]"
  - "[[Exponential Growth and Decay]]"
leads_to:
  - "[[Second-Order Differential Equations]]"
teach_together:
  - "[[Numerical Methods]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-3-8
  - syllabus/9231-2-6
  - syllabus/9231-3-5
  - type/technique
  - type/algorithm
  - notation/derivative
  - notation/ode
  - misconception/forgetting-constant-of-integration
  - misconception/missing-trivial-solution
  - misconception/integrating-factor-sign-error
  - misconception/general-vs-particular
---

# Differential Equations 微分方程

## Definition

### Formal

A **differential equation** is an equation involving an unknown function and one or more of its derivatives. An equation of the form

$$F\!\left(x,\, y,\, \dfrac{dy}{dx},\, \dfrac{d^2y}{dx^2},\, \ldots\right) = 0$$

is called an **ordinary differential equation (ODE)** — "ordinary" because it involves derivatives with respect to a single variable $x$. (Partial differential equations involve derivatives with respect to multiple variables; see beyond-syllabus.)

The **order** of an ODE is the order of the highest derivative appearing. **First-order:** $dy/dx$ only. **Second-order:** $d^2 y / dx^2$ at most. Higher orders rarer at A-Level.

A **solution** is any function $y(x)$ satisfying the equation. ODEs typically have a *family* of solutions parametrised by constants of integration — the **general solution**. Fixing those constants via **initial conditions** (e.g. $y(0) = 5$) selects one **particular solution**.

### Intuitive

A differential equation is *a relationship between a function and its rate of change*. The unknown isn't a number — it's a function. The equation says how the function and its derivatives are tied together. Solving the ODE means finding the actual function (or family of functions) that makes the relationship true.

The simplest example: $\dfrac{dy}{dx} = y$. *"The function equals its own derivative."* The solution is $y = Ce^x$ — *any* constant multiple of $e^x$. This is the defining property of the exponential (see [[Euler's Number]] and [[Exponential Growth and Decay]]).

Real-world appearance is everywhere:

- **Population dynamics**: rate of change of population is proportional to current population, $\dot N = kN$ → exponential. Add a carrying capacity → logistic.
- **Radioactive decay**: $\dot N = -\lambda N$ → exponential decay.
- **Newton's cooling**: $\dot T = -k(T - T_{\text{room}})$ → exponential approach to ambient.
- **Falling under gravity with air resistance**: $m\dot v = mg - bv$ → first-order linear ODE, integrable factor, terminal-velocity behaviour.
- **RC circuit charging**: $\dot Q = (V - Q/C)/R$ → exponential approach to fully-charged.
- **Newton's laws**: $m\ddot{x} = F(x, \dot x, t)$ → second-order ODE, the foundation of classical mechanics.

The 9709 P3 §3.8 scope is **first-order ODEs**, specifically separable equations. Edexcel / AQA A-Level Pure adds **first-order linear** (integrating-factor technique). IB AA HL covers both. We'll cover both in this card.

### 中文锚点

**微分方程**（wēifēn fāngchéng）：未知量是**函数**，方程里既有这个未知函数，也有它的**导数**（一阶或更高阶）。

**阶**（order）：方程里最高阶导数的阶数。一阶 ODE 只含 $dy/dx$，二阶含 $d^2y/dx^2$。

**解**（solution）：使方程成立的函数 $y(x)$。通常解不是唯一的，而是含**积分常数**的"通解"（general solution）。给定**初值条件**（如 $y(0)=5$）后可定唯一的"特解"（particular solution）。

**9709 P3 §3.8 重点：**
1. **可分离变量**（separable）：$\dfrac{dy}{dx} = f(x)g(y)$。重排为 $\dfrac{dy}{g(y)} = f(x)\,dx$，两边积分。
2. **指数增长/衰减**：[[Exponential Growth and Decay|指数增长卡]]已经详尽覆盖 $\dot y = ky \to y = Ae^{kt}$ 这一特例。
3. **一阶线性**（first-order linear，IB/A-Level extra）：$\dfrac{dy}{dx} + P(x)y = Q(x)$，用**积分因子**（integrating factor）$\mu = e^{\int P\,dx}$ 求解。

中文教材里这一章通常和"物理建模"挂钩：弹簧振子、电路、化学反应速率、生物种群——全是 ODE。理解的关键是**把"变化率正比于现状"的语言翻译成方程**。

---

## §1 ODE Terminology — Order, Linearity, Homogeneity

Before solving anything, classify the equation. The standard ODE taxonomy:

### Order

The highest derivative appearing. Sort examples:

| ODE | Order |
|---|---|
| $\dfrac{dy}{dx} = ky$ | 1 |
| $\dfrac{dy}{dx} + xy = e^x$ | 1 |
| $\dfrac{d^2y}{dx^2} + 4y = 0$ | 2 |
| $\dfrac{d^3y}{dx^3} = \sin x$ | 3 |
| $\left(\dfrac{dy}{dx}\right)^2 + y^2 = 1$ | 1 (still — order is *highest* derivative, not its *power*) |

9709 P3 §3.8 stays at order 1. Order 2 enters at A-Level Further / IB HL.

### Linearity

A first-order ODE is **linear** if it can be written as

$$\dfrac{dy}{dx} + P(x)\,y = Q(x)$$

with $y$ and $dy/dx$ appearing only to the first power, not multiplied together, no functions of $y$ besides $y$ itself.

| ODE | Linear? |
|---|---|
| $\dot y + 2y = e^x$ | **Yes** |
| $\dot y = ky$ | **Yes** ($Q = 0$, $P = -k$) |
| $\dot y + y = y^2$ | No ($y^2$) |
| $\dot y = \sin(y)$ | No ($\sin y$ is nonlinear in $y$) |
| $\dot y = xy^{1/2}$ | No ($y^{1/2}$) |

Linearity matters: linear ODEs have the **superposition property** — sums and scalar multiples of solutions are solutions of related linear equations. Most physical phenomena that produce *simple oscillations* (no chaos, no shock waves) come from linear ODEs. Nonlinear ODEs are where the interesting strange behaviour lives — turbulence, weather, predator-prey cycles, the three-body problem.

### Homogeneity

A linear ODE with $Q(x) = 0$ is **homogeneous**: $\dot y + P(x) y = 0$. With $Q(x) \neq 0$, it's **inhomogeneous** (sometimes "non-homogeneous"). The distinction matters because the homogeneous case has only the trivial structure $\dot y / y = -P$ (separable), while the inhomogeneous case needs the integrating-factor technique (§3).

---

## §2 Separable ODEs

The headline 9709 P3 §3.8 technique. A first-order ODE is **separable** if it can be written as

$$\boxed{\;\dfrac{dy}{dx} = f(x)\,g(y)\;}$$

— the right side factors as a function of $x$ times a function of $y$.

**Technique.** Rearrange so all $y$-dependence is on the left, all $x$-dependence on the right:

$$\dfrac{dy}{g(y)} = f(x)\,dx.$$

Then integrate both sides:

$$\int \dfrac{dy}{g(y)} = \int f(x)\,dx + C.$$

That's a single constant $C$ (combining the two integration constants from the two sides; absorb into one). Solve the resulting equation for $y$ in terms of $x$ if possible. The constant $C$ is determined by an initial condition $y(x_0) = y_0$ if one is given.

> [!warning] Don't lose the trivial solution
> If $g(y) = 0$ has a solution $y = y_*$, then the *constant function* $y(x) = y_*$ is *also* a solution of the original ODE — but the separation step divides by $g(y)$, which is undefined at $y = y_*$. So the separation method *misses* the constant solution. **Always check whether $g(y) = 0$ produces a forgotten solution before reporting your answer.**

### Worked example 1 — exponential growth/decay (the canonical case)

Solve $\dfrac{dy}{dx} = ky$ with $y(0) = y_0$.

**Separate.** $\dfrac{dy}{y} = k\,dx$ (assuming $y \neq 0$).

**Integrate both sides.** $\ln \lvert y \rvert = kx + C_1$.

**Solve for $y$.** $\lvert y \rvert = e^{C_1} e^{kx}$, so $y = \pm e^{C_1} e^{kx} = Ce^{kx}$ where $C = \pm e^{C_1}$ is an arbitrary nonzero constant. The case $y = 0$ (which the separation step missed) is also a solution — it corresponds to $C = 0$.

**Apply initial condition.** $y(0) = C = y_0$, so $y(x) = y_0 e^{kx}$.

This is the foundational example covered in detail in [[Exponential Growth and Decay]]. The card here introduces the *general* separable technique, of which this is the simplest case.

### Worked example 2 — non-exponential separable

Solve $\dfrac{dy}{dx} = \dfrac{x}{y}$, $y(0) = 2$.

**Separate.** $y\,dy = x\,dx$.

**Integrate.** $\dfrac{y^2}{2} = \dfrac{x^2}{2} + C_1$, i.e. $y^2 = x^2 + C$ (absorb $2C_1 = C$).

**Apply initial condition.** $y(0) = 2$ gives $4 = 0 + C$, so $C = 4$.

**Solve for $y$.** $y^2 = x^2 + 4$, so $y = \sqrt{x^2 + 4}$ (taking positive root since $y(0) = +2 > 0$).

The solution curves $y^2 - x^2 = C$ are *hyperbolas* — implicit solutions are sometimes the right form, especially when an explicit $y(x)$ would require choosing branches.

### Worked example 3 — separable with partial fractions

Solve the **logistic equation** $\dfrac{dy}{dt} = ky(1 - y)$ with $y(0) = y_0$, $0 < y_0 < 1$.

**Separate.** $\dfrac{dy}{y(1-y)} = k\,dt$.

**Apply partial fractions** to the left:

$$\dfrac{1}{y(1-y)} = \dfrac{1}{y} + \dfrac{1}{1-y}.$$

(Cover-up method on $y$ gives $A = 1$, on $1 - y$ gives $B = 1$. See [[Partial Fractions]].)

**Integrate.**

$$\int \!\left(\dfrac{1}{y} + \dfrac{1}{1-y}\right)dy = kt + C_1$$
$$\ln \lvert y \rvert - \ln \lvert 1-y \rvert = kt + C_1$$
$$\ln \!\left\lvert\dfrac{y}{1-y}\right\rvert = kt + C_1.$$

**Exponentiate.** $\dfrac{y}{1-y} = A e^{kt}$ where $A = \pm e^{C_1}$.

**Apply IC.** At $t = 0$: $A = \dfrac{y_0}{1 - y_0}$.

**Solve for $y(t)$.** Algebra gives the famous **logistic curve**:

$$\boxed{\;y(t) = \dfrac{1}{1 + \!\left(\dfrac{1 - y_0}{y_0}\right) e^{-kt}}\;}$$

S-shaped: starts at $y_0$, grows almost exponentially while $y$ is small, saturates at $y = 1$ as $t \to \infty$. The canonical model for *any* growth bounded by a carrying capacity — populations under resource limits, viral spread before containment, market penetration of new technology, neural-network sigmoid activation.

> [!tip] When the integrand on the $y$-side needs partial fractions
> Whenever the $y$-side of a separable ODE involves a fraction like $\dfrac{1}{y(y - a)}$ or $\dfrac{1}{y^2 - 1}$, **the integration step needs [[Partial Fractions]] before it can proceed**. This is the most common chain rule in 9709 P3 / IB AA HL: partial fractions + ODE integration combine into a single multi-mark question. Recognise the pattern: *non-trivial denominator on the $y$-side → partial-fraction-decompose before integrating*.

---

## §3 First-Order Linear ODEs — The Integrating Factor

A first-order linear ODE has the form

$$\boxed{\;\dfrac{dy}{dx} + P(x)\,y = Q(x)\;}$$

When $Q(x) = 0$, this is just $\dot y = -P(x)\,y$, separable. The interesting case is $Q(x) \neq 0$ — *inhomogeneous*. Here separation doesn't work, but a beautiful trick called the **integrating factor** does.

### The integrating-factor technique

**The trick.** Multiply both sides of $\dot y + Py = Q$ by a function $\mu(x)$ chosen so that the left side becomes the derivative of a product:

$$\mu \dot y + \mu P y = \mu Q.$$

We want the left side to equal $\dfrac{d}{dx}(\mu y) = \mu \dot y + \dot\mu \, y$. Comparing: $\mu P = \dot\mu$, i.e.

$$\dfrac{d\mu}{dx} = P(x)\,\mu.$$

This is itself a (separable) ODE for $\mu$. Solving: $\mu = e^{\int P\,dx}$.

That's the **integrating factor**:

$$\boxed{\;\mu(x) = e^{\int P(x)\,dx}\;}$$

Once you have $\mu$, the original ODE becomes

$$\dfrac{d}{dx}(\mu y) = \mu Q,$$

and integrating both sides gives

$$\mu y = \int \mu Q\,dx + C,$$

then solve for $y$: $y(x) = \dfrac{1}{\mu(x)}\!\left[\int \mu(x) Q(x)\,dx + C\right]$.

### Worked example 1 — basic integrating factor

Solve $\dfrac{dy}{dx} + 2y = e^x$ with $y(0) = 1$.

**Identify $P, Q$.** $P(x) = 2$, $Q(x) = e^x$.

**Compute integrating factor.** $\mu = e^{\int 2\,dx} = e^{2x}$.

**Multiply through.** $e^{2x}\dot y + 2e^{2x} y = e^{2x} \cdot e^x = e^{3x}$. Left side is $\dfrac{d}{dx}(e^{2x} y)$.

**Integrate.** $e^{2x} y = \int e^{3x}\,dx + C = \dfrac{e^{3x}}{3} + C$.

**Solve for $y$.** $y = \dfrac{e^x}{3} + C e^{-2x}$.

**Apply IC.** $y(0) = \dfrac{1}{3} + C = 1$, so $C = \dfrac{2}{3}$.

**Answer.** $y(x) = \dfrac{e^x}{3} + \dfrac{2 e^{-2x}}{3}$.

The structure $y = (\text{particular solution forced by } Q) + (\text{decay from the homogeneous part})$ is universal for inhomogeneous linear ODEs — a *transient* term ($Ce^{-2x}$, the homogeneous solution) plus a *steady forced* term ($e^x/3$, the particular solution).

### Worked example 2 — variable coefficient

Solve $\dfrac{dy}{dx} + \dfrac{y}{x} = x^2$ for $x > 0$, with $y(1) = 0$.

**Identify $P, Q$.** $P(x) = 1/x$, $Q(x) = x^2$.

**Compute integrating factor.** $\mu = e^{\int (1/x)\,dx} = e^{\ln x} = x$.

**Multiply through.** $x\dot y + y = x^3$. Left side is $\dfrac{d}{dx}(xy)$.

**Integrate.** $xy = \int x^3\,dx + C = \dfrac{x^4}{4} + C$.

**Solve for $y$.** $y = \dfrac{x^3}{4} + \dfrac{C}{x}$.

**Apply IC.** $y(1) = \dfrac{1}{4} + C = 0$, so $C = -\dfrac{1}{4}$.

**Answer.** $y(x) = \dfrac{x^3}{4} - \dfrac{1}{4x} = \dfrac{x^4 - 1}{4x}$.

> [!info] Why this trick works — the structure
> The integrating factor turns a *non-exact* differential into an *exact* one. Without $\mu$, the left side $\dot y + Py$ doesn't equal a single derivative; with $\mu$, it does. This is the same trick that appears in thermodynamics (chemical-potential treatment of free energy) and in symplectic geometry (Liouville's theorem). The integrating factor is a *fundamental* algebraic operation, not a hack.

---

## §4 Initial Conditions and Particular Solutions

A first-order ODE has a **one-parameter family** of solutions (one constant of integration). Specifying $y(x_0) = y_0$ — an **initial condition** — pins down the constant and selects the unique particular solution.

### Why one IC for first order, two for second order

Each integration adds one constant. Solving a first-order ODE requires one integration → one constant. Second-order requires two integrations → two constants → need two ICs (e.g. $y(0)$ and $y'(0)$).

### Existence and uniqueness

For a first-order ODE $\dot y = F(x, y)$ with initial condition $y(x_0) = y_0$, the **Picard-Lindelöf theorem** guarantees a unique solution exists in some interval around $x_0$ provided $F$ is continuous and $\partial F / \partial y$ is bounded near $(x_0, y_0)$. This is the existence-and-uniqueness theorem for ODEs; beyond 9709 syllabus but standard at university.

Practical consequence: for the well-behaved ODEs in 9709 P3, the solution is always unique once you have an initial condition. You don't have to worry about multiple particular solutions matching the same IC.

### Boundary conditions vs initial conditions

Some problems specify the value of $y$ at *two* points (e.g. $y(0) = 1, y(1) = 5$) — these are **boundary conditions**, not initial conditions. Boundary-value problems are more delicate (existence and uniqueness can fail). 9709 P3 stays with initial-value problems; boundary problems appear in IB AA HL and university-level methods.

---

## §5 Modelling with ODEs

The reason ODEs matter outside pure math: they're the *language* in which physical laws are written. The translation from a verbal description to an ODE is itself the hardest part.

### Pattern — *"rate of change of X is proportional to..."*

The standard modelling cue. "Rate of change of population is proportional to current population" → $\dot N = kN$. "Rate of change of temperature is proportional to the difference from ambient" → $\dot T = -k(T - T_{\text{room}})$. **The phrase "is proportional to" becomes an equality with $k$**; the noun before "rate of change of" becomes the dependent variable; the dependence on the right side becomes the function on the right side of the ODE.

### Example — Newton's law of cooling (rewritten)

A cup of coffee at $90°\text{C}$ cools in a room at $20°\text{C}$. After 10 minutes it's at $60°\text{C}$. Find the temperature as a function of time.

**Set up.** $\dfrac{dT}{dt} = -k(T - 20)$, with $T(0) = 90$ and $T(10) = 60$.

**Solve** (separable, or recognise the structure). $T(t) = 20 + Ae^{-kt}$. From $T(0) = 90$: $A = 70$. From $T(10) = 60$: $40 = 70 e^{-10k}$, so $k = \dfrac{\ln(7/4)}{10} \approx 0.0560$.

**Answer.** $T(t) = 20 + 70 e^{-0.0560 t}$, with $t$ in minutes. (Cross-link: [[Exponential Growth and Decay]] §4.)

### Example — falling object with linear drag

A ball of mass $m$ falls from rest. Drag is proportional to speed: $F_{\text{drag}} = -bv$. Find $v(t)$.

**Set up.** Newton's second law: $m\dot v = mg - bv$, i.e. $\dot v + \dfrac{b}{m}v = g$.

**Solve.** First-order linear. $P = b/m$, $Q = g$. Integrating factor $\mu = e^{(b/m)t}$. After the integrating-factor procedure:

$$v(t) = \dfrac{mg}{b} + Ae^{-(b/m)t}.$$

With $v(0) = 0$: $A = -mg/b$. So $v(t) = \dfrac{mg}{b}\!\left[1 - e^{-(b/m)t}\right]$.

**Interpret.** As $t \to \infty$, $v \to mg/b$ — the **terminal velocity**. The ball *asymptotically* approaches terminal velocity but never quite reaches it, with characteristic time $m/b$.

This pattern — "approach to equilibrium exponentially" — appears in RC circuits, drug elimination, thermal relaxation, capacitor discharge, viscoelastic stress relaxation. Same ODE, dozens of physical realisations.

### Example — population with carrying capacity (the logistic)

Solved in full at §2 example 3, and repeated here on purpose: there it was an integration exercise, here it is the modelling pattern, and you should be able to meet it from either direction. Set up: $\dot N = kN(1 - N/L)$ where $L$ is the carrying capacity. Solution: the logistic curve. Models: cane toads in Australia, COVID infection rate before containment, market saturation, sigmoid neural activation. *One ODE, four different fields use it daily.*

---

## §6 Common Misconceptions

### 1. Forgetting the constant of integration

Solving $\dot y = 2x$ by integrating once and writing $y = x^2$ instead of $y = x^2 + C$. The general solution requires the constant; only after applying an initial condition can you drop it.

**Fix.** *Every integration step adds a constant.* A first-order ODE generates one. A second-order ODE generates two. Count: number of integrations = number of constants in the general solution = number of initial conditions needed.

### 2. Losing the trivial solution in separation

Solving $\dot y = ky$ by separation gives $y = Ce^{kx}$ — but the separation step divides by $y$, missing the constant solution $y = 0$. The constant solution corresponds to $C = 0$, which is technically included if you allow $C$ to be any real (including zero), but with negative sign considerations you can miss it.

**Fix.** Before separating, *identify any constant solutions* by setting $g(y) = 0$. These are equilibria of the ODE. Then proceed with separation, knowing the equilibria are valid solutions even if the technique technically misses them.

### 3. Sign errors in the integrating factor

Computing $\mu = e^{\int P\,dx}$ but with the wrong sign on $P$. The ODE $\dot y - 2y = e^x$ has $P = -2$ (note the minus); $\mu = e^{-2x}$, not $e^{2x}$.

**Fix.** *Write the ODE in standard form $\dot y + P(x)y = Q(x)$ first.* That tells you what $P$ is, with the correct sign. Only then compute $\mu$.

### 4. Confusing general and particular solutions

The student writes down the general solution $y = Ce^{kx}$ and reports it as the final answer to a question that gave initial conditions. The marker wants the *particular* solution with $C$ determined.

**Fix.** *If the question gives an initial condition, apply it.* The final answer should have no arbitrary constants left.

### 5. Treating non-separable as separable

The student tries to separate $\dot y = x + y$ as $\dfrac{dy}{y} = (x + ?)\,dx$. But $x + y$ is a sum, not a product — the equation is *not* separable. Force-fitting separation doesn't work.

**Fix.** *Check separability before applying the technique.* The equation $\dot y = f(x)g(y)$ must have the right side genuinely factor as $x$-only × $y$-only. If you see $x + y$, $x - y$, or $\sin(xy)$, separation isn't the technique. Try integrating factor (if linear) or some other method.

### 6. Wrong choice of integrating factor for non-linear ODEs

Trying to apply the integrating-factor technique to $\dot y + y^2 = x$ (nonlinear because of $y^2$). The technique only works for *linear* first-order equations.

**Fix.** *Check linearity first.* If $y$ appears in any way other than first-power, multiplied by a function of $x$ only, the integrating-factor technique doesn't apply. Some nonlinear ODEs have their own tricks (Bernoulli substitution $u = y^{1-n}$ converts $\dot y + Py = Qy^n$ to linear), but those are beyond 9709 P3.

---

## §7 Exam Notes

### Cambridge 9709 (A-Level)

**Syllabus refs:** Paper 3 §3.8 — *first-order differential equations*. Specifically:
- Forming a differential equation from a verbal/contextual problem.
- Solving first-order *separable* equations by integration, including the use of partial fractions where appropriate.
- Applying initial conditions to find particular solutions.
- Interpreting solutions in context (e.g. "what is the long-term behaviour?", "at what time does $y$ reach a specified value?").

**Not on 9709 P3:** The integrating-factor technique for first-order *linear* equations is **not** part of 9709 P3. Cambridge examines it one board up, in **9231 FP2 §2.6** (see below); it's also part of Edexcel/AQA A-Level Pure, IB AA HL, and AP BC, and it elegantly extends the separable case.

**Typical question shape (8–12 marks):**
1. *Formulate the ODE from a word problem.* (2–3 marks)
2. *Solve the ODE by separation.* (4–6 marks, often involving partial fractions)
3. *Apply initial conditions.* (1–2 marks)
4. *Interpret in context.* (1–2 marks — "find $t$ when $y = 5$", "find the limiting value", etc.)

**Tip.** When the question describes a physical scenario, *write down the ODE explicitly before doing any integration*. The translation from words to equation is itself worth marks — usually 2 marks before any actual calculus happens. Don't skip to integration in your working.

### Cambridge 9231 (Further Mathematics)

- **FP2 §2.6** examines the **integrating factor** directly — find $\mu$ for a first-order linear equation and use it for the general solution, with syllabus specimens like $y' + y\coth x = \cosh x$ (hyperbolic-flavoured coefficients are fair game at FP2). The same subsection carries the second-order machinery — complementary function + particular integral — treated in full at [[Second-Order Differential Equations]].
- **Paper 3 (Further Mechanics) §3.5** uses *separable* first-order equations for linear motion under a variable force, including $v\frac{dv}{dx}$ as the acceleration — the calculus is this page's, wearing a mechanics costume.

### Cambridge 0606

**Not on 0606.** ODEs are A-Level material; 0606 stops at antiderivatives and applications to motion under constant acceleration.

### A-Level (Edexcel / AQA / OCR / MEI)

Edexcel A-Level Pure A2 includes both separable ODEs **and** the integrating-factor technique. AQA covers the same. OCR's Further Mathematics adds second-order linear ODEs with constant coefficients. All boards cover the formulation-from-word-problems portion.

### IB AA HL

**Topic refs:** AA HL Topic 5 (Calculus). Includes separable ODEs, integrating factors, Euler's method for numerical solution (cross-link to [[Numerical Methods]]), and the slope-field / direction-field representation.

The IB AA HL formula booklet does **not** give the integrating-factor formula. You must remember $\mu = e^{\int P\,dx}$.

### AP Calculus

**AP Calculus BC**: separable ODEs are central. The BC syllabus includes:
- Separable equations (Topic 7.6–7.8 in current CED).
- **Slope fields** (Topic 7.3): graphical representation $\dot y = F(x, y)$ as a field of tiny slope-arrows at each $(x, y)$. Helps visualise solution curves without solving.
- **Euler's method** (Topic 7.5): $y_{n+1} = y_n + h \cdot F(x_n, y_n)$ — the simplest numerical ODE solver. This is fixed-point iteration applied to ODEs (cross-link to [[Numerical Methods]]).
- Logistic differential equations (Topic 7.9) — the $\dot N = kN(1 - N/L)$ model.

The integrating-factor technique is **not** AP BC content; it appears in undergraduate differential equations courses. **AP Calculus AB** does not test ODEs at all.

### Beyond high school — University

Differential equations is a full one-to-two-semester undergraduate subject. Three of the standard extensions of §3.8 — second-order linear equations and the complex eigenvalues that put oscillation into them, systems $\dot{\mathbf x} = A\mathbf{x}$ and their phase portraits, and the nonlinear-and-chaotic regime — are taken up in the Beyond Syllabus section, with the full second-order machinery (CF + PI, all three root cases, resonance, reduction by substitution) at [[Second-Order Differential Equations]]. The rest:

- **Partial differential equations (PDEs)** — derivatives with respect to multiple variables: the heat equation, wave equation, Laplace equation, Schrödinger equation (see [[Stories/The Argument for i]] Act V). Far harder than ODEs.
- **Numerical methods for ODEs**: Euler, Runge-Kutta (RK4 is the workhorse), implicit methods, stiff ODEs.
- **Lie symmetry methods**: a symmetry-based unifying framework for analytic ODE solving.

---

## Connections

- **Direct prerequisite:** [[Integration]] + [[Standard Integrals]] — solving an ODE *is* integrating it. Every technique in this card terminates in an integral.
- **Direct prerequisite:** [[Partial Fractions]] — required for separating ODEs whose $y$-side has a non-trivial denominator (the logistic equation is the canonical example).
- **Direct prerequisite:** [[Differentiation]] + [[Differentiation Rules]] — to recognise and manipulate derivatives.
- **Direct prerequisite:** [[Exponential Function]] + [[Logarithms]] — the natural language of $\dot y = ky$ solutions.
- **Headline special case:** [[Exponential Growth and Decay]] — covers $\dot y = ky$ in extensive detail with five canonical applications (radioactive decay, Newton's cooling, population, drugs, compound interest). This card here generalises beyond exponential.
- **Application — numerical:** [[Numerical Methods]] — when an ODE has no closed-form solution, Euler's method ($y_{n+1} = y_n + h \cdot F(x_n, y_n)$) and Runge-Kutta methods step through it numerically. The fixed-point iteration framework of Numerical Methods extends directly to ODEs.
- **Closes:** 9709 P3 §3.8 (separable ODEs); brings the yellow row to green.
- **Cashes in:** All the prereq cards' forward-pointers to [[Differential Equations]] (Standard Integrals, Partial Fractions, Numerical Methods, Complex Numbers, Integration, Integration by Substitution, Integration by Parts).
- **Beyond syllabus — physics bridge:** Every classical-mechanics problem is a second-order ODE ($m\ddot x = F$). Every quantum-mechanics problem is a (linear) PDE. ODEs are the *grammar* of physics.
- **Beyond syllabus — story bridge:** [[Stories/The Bernoulli Family]] — Jakob Bernoulli's brachistochrone solution (1697) invented the *calculus of variations*, which is now the standard technique for finding the ODE that minimises an action. Daniel Bernoulli's *Hydrodynamica* (1738) is a sustained application of conservation-law ODEs to fluid flow.
- **For 9709 students:** [[MF19 Reference (9709)]] — no ODE-specific formulas given on the MF19 sheet. Standard integrals (which solve most §3.8 ODEs) *are* there.

---

## Beyond Syllabus

### Why exponentials show up everywhere

Almost every "natural process described by a first-order linear ODE with constant coefficients" produces an exponential time-evolution. The reason is structural: the ODE $\dot y = -ky$ (decay) or $\dot y = ky$ (growth) is precisely the statement "the function is proportional to its own rate of change," and the unique solution is $y(t) = y_0 e^{\pm kt}$.

So whenever a physical system has the property "the larger it is, the faster it changes" (linearly), you get an exponential. This shows up in:

- Radioactive decay (decay rate ∝ remaining atoms)
- RC discharge (current ∝ remaining charge)
- Bacterial growth in unlimited resources
- Newton's law of cooling
- Compound interest in the continuous-time limit
- Atmospheric pressure with altitude
- Beer-Lambert law (light intensity through a medium)

The *unifying observation* is that they all satisfy the same first-order linear ODE with constant coefficient — and that ODE has a unique solution-shape.

### Slope fields and qualitative analysis without solving

Even when an ODE can't be solved analytically (which is most of them), you can often understand its qualitative behaviour by drawing a **slope field**: at each point $(x, y)$ in the plane, draw a tiny segment with slope $F(x, y)$ (the ODE's right side). The solution curves follow these slopes.

For $\dot y = y(1 - y)$ (logistic): horizontal slopes at $y = 0$ and $y = 1$ (equilibria); positive slopes for $0 < y < 1$ (growth); negative for $y > 1$ (decline back to 1). The phase-portrait reveals the long-term behaviour without ever solving the equation.

This is the entry point to **qualitative theory of ODEs** — a 20th-century framework largely due to Poincaré, where you study the *topology* of the solution flow rather than chasing closed-form solutions.

### Picard-Lindelöf as a fixed-point theorem

Recall the existence-and-uniqueness theorem from §4. It is a *consequence* of the Banach Fixed-Point Theorem. Define the **Picard operator**

$$\mathcal{T}[y](x) = y_0 + \int_{x_0}^x F(t, y(t))\,dt,$$

and a fixed point of $\mathcal{T}$ — a $y$ with $y = \mathcal{T}[y]$ — is exactly a solution of the ODE. Under mild conditions on $F$, $\mathcal{T}$ is a contraction on a space of continuous functions, and Banach hands you a unique fixed point. *That's the proof.*

Cross-link to [[Numerical Methods]] beyond-syllabus: Banach is the master framework, ODE existence is one instance, fixed-point iteration is another, and Newton-Raphson is a third.

### Second-order linear: oscillation enters via complex eigenvalues

The simplest non-trivial second-order ODE is $\ddot y + \omega^2 y = 0$ — simple harmonic motion. Solutions: $y(t) = A\cos(\omega t) + B\sin(\omega t)$, or equivalently $y(t) = \Re(Ce^{i\omega t})$ (real part of a complex exponential).

The complex-exponential form is *not* a convenience — it's the natural language. The characteristic equation $\lambda^2 + \omega^2 = 0$ has roots $\lambda = \pm i\omega$, and the general solution is built from $e^{\lambda t}$ for those $\lambda$'s. *Without complex numbers, you'd have separate real-valued $\cos$ and $\sin$ pieces; with complex numbers, you have one unified $e^{i\omega t}$ structure.*

This is the deepest reason [[Complex Numbers|complex numbers]] are unavoidable in physics: as soon as you have second-order linear ODEs (which is essentially all of classical mechanics, all of electrical engineering, all of quantum mechanics), complex eigenvalues are the natural eigenvalues, and complex exponentials are the natural solution basis.

### Phase portraits and dynamical systems

A system of ODEs in two variables — $\dot x = f(x, y)$, $\dot y = g(x, y)$ — defines a *flow* on the $(x, y)$-plane. Trajectories of the flow can be:
- **Limit cycles** (closed orbits — Poincaré-Bendixson for 2D systems)
- **Attractors** (sets toward which trajectories converge)
- **Saddles** (unstable equilibria)
- **Strange attractors** in 3D systems (Lorenz attractor, the founding example of chaos)

The *geometric* theory of ODEs — what trajectories look like rather than what they equal — is the 20th-century synthesis of differential equations. It's the basis of modern **dynamical systems theory**, a subject with applications across physics, biology, economics, neuroscience, and climate science.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{dy}{dx}$ | `\dfrac{dy}{dx}` | First derivative |
| $\dfrac{d^2y}{dx^2}$ | `\dfrac{d^2y}{dx^2}` | Second derivative |
| $\dot y, \ddot y$ | `\dot y, \ddot y` | Newton's dot notation — common for time derivatives |
| $y'$ | `y'` | Lagrange's prime notation — common for $x$ derivatives |
| $\dfrac{dy}{dx} + P(x)y = Q(x)$ | (as written) | Standard form of first-order linear ODE |
| $\mu = e^{\int P(x)\,dx}$ | `\mu = e^{\int P(x)\,dx}` | Integrating factor |
| $\dfrac{dy}{dx} = f(x)g(y)$ | (as written) | Separable form |
| $y(x_0) = y_0$ | `y(x_0) = y_0` | Initial condition |
| $\dot y = ky$ | `\dot y = ky` | Exponential growth (decay if $k < 0$) |
| $\dot N = kN(1 - N/L)$ | `\dot N = kN(1 - N/L)` | Logistic equation |
| $\lambda^2 + a\lambda + b = 0$ | (as written) | Characteristic equation (beyond syllabus, 2nd-order ODE) |
