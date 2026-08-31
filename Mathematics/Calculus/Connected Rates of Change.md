---
chinese: 相关变化率 (xiāngguān biànhuàlǜ)
prerequisites:
  - "[[Differentiation]]"
  - "[[Chain Rule]]"
  - "[[Similarity]]"
  - "[[Implicit Differentiation]]"
  - "[[Parametric Differentiation]]"
  - "[[Rates (Vocab)]]"
  - "[[Tangents and Normals]]"
leads_to:
  - "[[Differential Equations]]"
teach_together:
  - "[[Optimisation]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-14-7
  - type/deep
  - type/technique
  - type/application
  - misconception/forgot-time-variable
  - misconception/wrong-direction-of-chain
  - misconception/dropped-similar-triangles
---

# Connected Rates of Change 相关变化率

## Definition

A **connected-rates problem** asks: *if quantity $X$ depends on quantity $Y$, and $Y$ varies with time, how fast does $X$ vary with time?* The chain rule answers it in one line:

$$\boxed{\;\frac{dX}{dt} = \frac{dX}{dY} \cdot \frac{dY}{dt}.\;}$$

Read it out loud: "the rate of $X$ with time = the rate of $X$ with $Y$, times the rate of $Y$ with time." If you know two of the three rates, the third one is forced.

The standard exam form: a balloon is inflated, a ladder slides, water fills a tank, a shadow lengthens. Some quantity (volume, height, length) is varying at a *given* rate, and you must find the rate of a *related* quantity. The relationship between them is geometric (volume formula, Pythagoras, similar triangles) and the chain rule converts the geometry into rates.

This is the chain rule in its most physical disguise — applied to **time** as the chained variable instead of an algebraic substitution.

### 中文锚点

**相关变化率 (xiāngguān biànhuàlǜ)** = 多个量同时随时间变化，已知一个量的变化速率，求另一个量的变化速率。

核心公式（链式法则的时间版本）：

$$\frac{dX}{dt} = \frac{dX}{dY} \cdot \frac{dY}{dt}.$$

考试三步法：
1. **写出几何关系** — 把两个量用一个等式连起来（体积公式、勾股、相似三角形）
2. **两边同时对 $t$ 求导** — 用链式法则展开
3. **代入数值**，解出未知的速率

注意：**几何关系是不随时间变的**（球的体积永远是 $V = \tfrac{4}{3}\pi r^3$），但 $V$ 和 $r$ 都是 $t$ 的函数。求导时把 $V, r$ 都当作 $t$ 的函数来对待。

---

## The Three-Step Recipe

Every connected-rates problem follows the same template:

**Step 1 — write the geometric relationship.** Find an equation that links the two quantities. Common shapes:

| Setup | Relation |
|---|---|
| Sphere | $V = \tfrac{4}{3}\pi r^3$, $A = 4\pi r^2$ |
| Cube | $V = s^3$, $A = 6s^2$ |
| Cone (water tank) | $V = \tfrac{1}{3}\pi r^2 h$, plus similar-triangle ratio $r/h = $ constant |
| Cylinder | $V = \pi r^2 h$, $A = 2\pi r^2 + 2\pi r h$ |
| Right triangle (ladder, shadow) | $x^2 + y^2 = L^2$ (Pythagoras) |

**Step 2 — differentiate both sides with respect to $t$.** Treat *every* letter as a function of $t$ and apply the chain rule. For example, $V = \tfrac{4}{3}\pi r^3$ becomes

$$\frac{dV}{dt} = 4\pi r^2 \cdot \frac{dr}{dt}.$$

The $r^3 \to 3r^2 \cdot \frac{dr}{dt}$ step is the chain rule in action: $r$ is a function of $t$, so the inside-derivative $\frac{dr}{dt}$ comes out.

**Step 3 — substitute the known values and solve.** Plug in the *current* values of $r$ (or whatever variables) and the *given* rate, then solve for the unknown rate.

> [!warning] Substitute *after* differentiating, not before
> A common trap: students plug in $r = 5$ (say) *before* differentiating $V = \tfrac{4}{3}\pi r^3$. That gives $V = \tfrac{500\pi}{3}$, a constant — and $dV/dt = 0$, which is wrong. The relationship $V = \tfrac{4}{3}\pi r^3$ holds for *all* values of $r$, not just $r = 5$. Differentiate the formula *first* (as a function of $r$), then plug in specific values *after* getting the rate equation. The radius is at $r = 5$ *right now*, but the derivative captures how things change *as $r$ varies*.

---

## Worked Examples

![[connected-rates-three-setups.svg]]

Above: the three canonical setups — spherical balloon, sliding ladder, conical tank. Each has its own geometric relation that the chain rule converts into a rate equation.

### Example 1 — Spherical balloon (the simplest case)

> A spherical balloon is being inflated at a constant rate of $20$ cm³/s. Find the rate at which the radius is increasing when $r = 5$ cm.

**Step 1 — relation.** $V = \tfrac{4}{3}\pi r^3$.

**Step 2 — differentiate w.r.t. $t$.** Apply the chain rule (with $V$ and $r$ both functions of $t$):

$$\frac{dV}{dt} = 4\pi r^2 \cdot \frac{dr}{dt}.$$

**Step 3 — substitute.** Given $\dfrac{dV}{dt} = 20$ cm³/s and $r = 5$ cm:

$$20 = 4\pi (5)^2 \cdot \frac{dr}{dt} = 100\pi \cdot \frac{dr}{dt} \;\;\Longrightarrow\;\; \frac{dr}{dt} = \frac{20}{100\pi} = \frac{1}{5\pi} \approx 0.0637 \text{ cm/s.}$$

**Final answer.** The radius is increasing at $\boxed{\dfrac{1}{5\pi} \approx 0.064 \text{ cm/s}}$.

> [!info] Notice the answer depends on $r$
> If we asked the same question when $r = 10$, we'd get $\dfrac{dr}{dt} = \dfrac{20}{4\pi(100)} = \dfrac{1}{20\pi} \approx 0.016$ cm/s — *four times slower*. The volume rate is constant, but the radius slows down as the balloon gets bigger because the same $20$ cm³ of air now spreads over a larger surface area. This is why *long-distance* balloon flights (weather balloons that grow as they rise) accelerate their radius growth slowly even as the volume keeps inflating linearly with altitude. Connected rates capture this geometric "diluting" effect for free.

### Example 2 — The sliding ladder (the trick case)

> A $10$-metre ladder is leaning against a vertical wall. The bottom slides away from the wall at $0.5$ m/s. Find the rate at which the top is sliding *down* the wall when the bottom is $6$ m from the wall.

**Step 1 — relation.** Let $x$ = distance of bottom from wall, $y$ = height of top above ground. Pythagoras: $x^2 + y^2 = 100$.

**Step 2 — differentiate w.r.t. $t$.**

$$2x \cdot \frac{dx}{dt} + 2y \cdot \frac{dy}{dt} = 0.$$

**Step 3 — substitute.** When $x = 6$, $y = \sqrt{100 - 36} = 8$. Given $\dfrac{dx}{dt} = 0.5$ m/s:

$$2(6)(0.5) + 2(8) \cdot \frac{dy}{dt} = 0 \;\;\Longrightarrow\;\; 6 + 16 \cdot \frac{dy}{dt} = 0 \;\;\Longrightarrow\;\; \frac{dy}{dt} = -\frac{6}{16} = -\frac{3}{8} \text{ m/s.}$$

**Final answer.** The top is sliding *down* at $\boxed{\dfrac{3}{8} = 0.375 \text{ m/s}}$. (The negative sign confirms $y$ is decreasing — the top is falling.)

> [!tip] The sign tells you the direction
> When $\dfrac{dy}{dt} < 0$, $y$ is decreasing — the top is falling. When $\dfrac{dy}{dt} > 0$, $y$ is rising. *Always interpret the sign* in the final answer. "The top descends at $0.375$ m/s" is the right phrasing; "$\dfrac{dy}{dt} = -0.375$ m/s" is the calculus output, but the answer to the *question* is in plain English about direction.

> [!info] The sliding ladder paradox — when the rate goes infinite
> Watch what happens as $x \to 10$ (ladder almost flat on the ground): $y \to 0$, so $2y \cdot \frac{dy}{dt} = -2x \cdot \frac{dx}{dt}$ forces $\frac{dy}{dt} \to -\infty$. The top of the ladder, in the model, falls *infinitely fast* the moment it hits the ground.
>
> Of course, real ladders don't do this. The model breaks down because (a) the ladder lifts off the wall before $y = 0$, (b) the contact-with-the-wall assumption fails, (c) inertia and gravity matter. The "infinity" is the maths cleanly telling you "your model is no longer physical here." This is a recurring feature of mathematical modelling — the formal answer often contains a *signal* about where the model breaks.

### Example 3 — Water in a conical tank (the similar-triangles trap)

> Water flows into an inverted cone-shaped tank at $4$ m³/min. The tank has total height $10$ m and top radius $5$ m. Find the rate at which the water level rises when the depth is $h = 6$ m.

**Step 1 — relation.** The water forms a smaller cone of height $h$ and radius $r$. The volume is $V = \tfrac{1}{3}\pi r^2 h$, but **$r$ and $h$ are not independent** — they are linked by similar triangles to the tank's full dimensions:

$$\frac{r}{h} = \frac{5}{10} = \frac{1}{2} \;\;\Longrightarrow\;\; r = \frac{h}{2}.$$

Substitute into $V$ to express it in **one variable**:

$$V = \frac{1}{3}\pi \left(\frac{h}{2}\right)^2 h = \frac{1}{3}\pi \cdot \frac{h^2}{4} \cdot h = \frac{\pi h^3}{12}.$$

**Step 2 — differentiate w.r.t. $t$.**

$$\frac{dV}{dt} = \frac{\pi}{12} \cdot 3h^2 \cdot \frac{dh}{dt} = \frac{\pi h^2}{4} \cdot \frac{dh}{dt}.$$

**Step 3 — substitute.** $\dfrac{dV}{dt} = 4$ m³/min, $h = 6$:

$$4 = \frac{\pi (6)^2}{4} \cdot \frac{dh}{dt} = 9\pi \cdot \frac{dh}{dt} \;\;\Longrightarrow\;\; \frac{dh}{dt} = \frac{4}{9\pi} \approx 0.141 \text{ m/min.}$$

**Final answer.** The water level rises at $\boxed{\dfrac{4}{9\pi} \approx 0.14 \text{ m/min}}$.

> [!warning] You *must* use similar triangles to eliminate $r$
> The classic mistake: differentiate $V = \tfrac{1}{3}\pi r^2 h$ directly without first eliminating $r$. Then you'd have *two* unknown rates ($\dfrac{dr}{dt}$ and $\dfrac{dh}{dt}$) and only one equation — unsolvable. The similar-triangles step is what reduces the geometric setup to one variable, exactly the way Optimisation needs an objective in one variable. Always check: how many unknowns does the relation contain, and do you have enough constraints to eliminate them?

---

## Small-Increment Approximation

A linear-approximation cousin of the chain rule: if $y$ depends on $x$, then for *small* changes,

$$\boxed{\;\delta y \approx \dfrac{dy}{dx} \cdot \delta x.\;}$$

This is exactly the chain rule's structure with $\delta$'s instead of $d$'s — a finite-difference approximation that becomes exact in the limit. It's how engineers do *quick error estimates* without solving exactly.

**Example.** A circle's radius is measured as $r = 4$ cm with an error of up to $\delta r = 0.05$ cm. Approximate the resulting error in the area $A = \pi r^2$.

$$\delta A \approx \frac{dA}{dr} \cdot \delta r = 2\pi r \cdot \delta r = 2\pi (4)(0.05) = 0.4\pi \approx 1.26 \text{ cm}^2.$$

Compare to the exact change: $A(4.05) - A(4) = \pi(4.05)^2 - \pi(4)^2 = \pi(16.4025 - 16) = 0.4025\pi \approx 1.264$ cm². Difference under $1\%$. The linear approximation is excellent for small $\delta r$.

This is the foundation of **error propagation** in physics: if a measurement has uncertainty $\delta x$, any quantity computed from it has uncertainty approximately $\left|\dfrac{dy}{dx}\right| \delta x$. Connected rates and error propagation are the *same calculus*, used in two different contexts.

---

## Common Mistakes

1. **Substituting before differentiating.** Plug values into the geometric formula *after* you've obtained the rate equation, not before. The formula must hold for all values, not just the current one.
2. **Forgetting that every letter is a function of $t$.** When you differentiate $V = \tfrac{4}{3}\pi r^3$, the $r^3$ becomes $3r^2 \cdot \frac{dr}{dt}$, *not* just $3r^2$. The chain-rule "inside derivative" is the entire point of the technique.
3. **Not eliminating extra variables.** If your relation has two geometric unknowns ($r$ and $h$ in a cone), find the constraint (similar triangles, fixed perimeter, geometry) that links them and reduce to *one* variable before differentiating.
4. **Sign errors and direction.** A negative rate means the quantity is decreasing. Phrase the answer in plain English: "the top descends at $0.375$ m/s," not just "the rate is $-0.375$."
5. **Wrong direction of the chain.** $\dfrac{dV}{dt} = \dfrac{dV}{dr} \cdot \dfrac{dr}{dt}$, *not* $\dfrac{dV}{dt} = \dfrac{dr}{dV} \cdot \dfrac{dr}{dt}$. The chain rule goes from outside to inside; the inside variable is the one differentiated last.
6. **Missing units.** Volumes are cm³, areas are cm², lengths are cm, rates are *per unit time*. Always tag the answer with the right unit ("cm/s," "m³/min," etc.) — markschemes deduct for missing or wrong units.

---

## Exam Notes

### Cambridge 0606

**Syllabus ref:** §14.7 — connected rates of change, small increments, approximations. Standard exam patterns:

- **Pattern A — sphere/cube/cylinder rate.** Given $\dfrac{dV}{dt}$ (or $\dfrac{dA}{dt}$), find $\dfrac{dr}{dt}$ (or vice versa). Direct chain-rule application.
- **Pattern B — cone tank with similar triangles.** Same template, but with the similar-triangle reduction step. Easy 1-mark loss for skipping that step.
- **Pattern C — Pythagorean setup.** Sliding ladder, distance between two moving points, etc. Differentiating an implicit relation $x^2 + y^2 = c^2$ implicitly.
- **Pattern D — small-increment approximation.** "Use a small-change formula to estimate $\sqrt{16.1}$" or "estimate the change in volume when radius increases from $r$ to $r + \delta r$." Direct use of $\delta y \approx \frac{dy}{dx} \delta x$.

> [!tip] State the chain-rule identity first; don't go straight to numbers
> 0606 markscheme typically gives a method mark for *writing down* $\dfrac{dV}{dt} = \dfrac{dV}{dr} \cdot \dfrac{dr}{dt}$ before plugging in numbers. Even if your arithmetic later goes wrong, that mark is yours. Always show the chain-rule step explicitly as the first line of working.

### Cambridge 0580

**Not examined.** Extended's calculus (E2.12) differentiates single-variable polynomials for gradients and turning points — no time rates, no chained variables.

### Cambridge 9709

On **Paper 1 (AS), §1.7** — the syllabus's applications-of-differentiation row says, in its own notes, "Including connected rates of change, e.g. given the rate of increase of the radius of a circle, find the rate of increase of the area for a specific value of one of the variables." Exactly the 0606 patterns above, one calculus tier up. Paper 3 then supplies the grown-up forms the harder setups need — **implicit differentiation** (when the relation $F(x,y)=0$ won't solve for $y$: Pattern C's ladder, done properly) and **parametric differentiation** ($\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$ — itself a connected-rates statement about the parameter $t$).

### Cambridge 9231 (Further Maths)

Assumed, never re-examined — but the *shape* returns in Further Mechanics whenever a geometric constraint ties two moving quantities together.

### Edexcel IAL / OxAQA 9660

IAL leans on connected rates twice: **P3.4.3**'s reciprocal-derivative rule $\frac{dy}{dx} = 1\big/\frac{dx}{dy}$, and — the distinctive IAL habit — **P4.5.2**, where a connected-rates sentence is the *birth of a differential equation*: "the rate of change of $X$ is proportional to…" turns straight into $\frac{dX}{dt} = kX$. OxAQA 9660 examines the same material in its P2 calculus block. On both boards the method mark for writing the chain first (the 0606 tip above) carries over unchanged.

### IB AA

Related rates are **HL** (the AHL differentiation extension, alongside implicit differentiation) — an AA SL student is not asked them. HL Paper 2 recycles the classic setups: the cone tank, the sliding ladder, the moving shadow.

### AP Calculus AB/BC

Topics **4.4–4.5** — "related rates" is a named topic with its own FRQ tradition, using identical setups to the Cambridge patterns; AP's marking makes the same demand as 0606's: state the connecting equation *before* substituting numbers, because differentiating after plugging in a constant is the classic zero.

---

## Beyond Syllabus

### Connected Rates Are Everywhere in Engineering and Physics

Open any textbook in fluid dynamics, thermodynamics, optics, electromagnetics, or chemical engineering and the *same* chain-rule logic appears, dressed in different costumes:

- **Fluid flow** — the rate at which a tank empties depends on the height of fluid (Torricelli's law), which depends on volume, which depends on time. Three layers of chain rule.
- **Reaction kinetics** — $\dfrac{d[\text{product}]}{dt} = k \cdot \dfrac{d[\text{reactant}]}{dt}$ (with the right rate constants); differential equations born from chain-rule thinking.
- **Optics** — image-distance changes with object-distance via the lens equation $\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$; if you move the object at $\frac{du}{dt}$, the image moves at $\frac{dv}{dt}$, found by implicit differentiation.
- **Astronomy** — apparent angular size of a moving asteroid changes at a rate determined by its distance and velocity (chain rule with arctan).
- **Economics — marginal analysis** — total cost depends on production, production depends on time, so $\frac{dC}{dt} = \frac{dC}{dQ} \cdot \frac{dQ}{dt}$. Marginal cost ($\frac{dC}{dQ}$) is exactly the kind of derivative on this card, dressed in dollars.

The 0606 framework is **the universal grammar of "rates of related quantities."** Once you have it, every cross-rate problem in science is a vocabulary swap.

### Differential Equations — the infinite-limit cousin

If a connected-rates problem doesn't give you a *single* moment but a *whole equation* relating rates, you have a **differential equation**. The classic example: a tank drains so that the rate of volume decrease is proportional to the volume,

$$\frac{dV}{dt} = -kV.$$

This isn't a single-rate question — it's a *family* of rates, specified by $V$ at every moment. Solving it (separation of variables) gives $V(t) = V_0 e^{-kt}$, the exponential decay seen in [[Exponential Growth and Decay]].

Connected rates is the "snapshot" version. Differential equations are the "movie" version. Both rely on the same chain-rule machinery, applied at one point or across all time.

### Implicit Differentiation as the Constraint Generaliser

When the geometric relationship can't be solved for one variable explicitly — say $\sin(xy) + x^2 - y = 0$ — *implicit differentiation* lets you compute $\frac{dy}{dx}$ anyway. Differentiate both sides with respect to $x$, treating $y$ as $y(x)$, and apply the chain rule wherever $y$ appears. Solve the resulting equation for $\frac{dy}{dx}$.

Connected rates is implicit differentiation with respect to $t$. The difference is purely cosmetic: the chained variable is time, and the surrounding language is physical. The technique is the same.

---

## Connections

- **Prerequisite:** [[Differentiation]] — every step requires standard derivatives
- **Prerequisite:** [[Chain Rule]] — *the* tool of this card; connected rates is the chain rule applied to time
- **Prerequisite:** [[Similarity]] — the cone-tank setup uses similar triangles to reduce the geometric relation to one variable
- **Sibling:** [[Optimisation]] — same chain-rule machinery, but seeking $f' = 0$ instead of computing a rate
- **Sibling:** [[Kinematics Calculus]] — kinematics *is* the most physical connected-rates problem: position, velocity, acceleration are connected via $\dfrac{d}{dt}$
- **Application:** *physics — error propagation* — small-increment formula $\delta y \approx \frac{dy}{dx} \delta x$ underlies all uncertainty quantification in experimental science
- **Application:** *engineering* — fluid dynamics, reaction kinetics, optics, structural deformation — all rely on connecting rates of related quantities
- **Application:** *economics* — marginal analysis ($\frac{dC}{dQ}$, $\frac{dR}{dQ}$) generalises to time-rates of production and revenue
- **Leads to:** [[Differential Equations]] — when the rates obey a relationship at every moment (not just one), connected rates becomes a differential equation
- **Beyond high school:** *implicit differentiation* (the multi-variable version), *partial derivatives* (when there are several inputs varying simultaneously), *gradient flow* and the calculus of multi-variable systems

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{dV}{dt}$ | `\dfrac{dV}{dt}` | Rate of volume w.r.t. time |
| $\dfrac{dV}{dr} \cdot \dfrac{dr}{dt}$ | `\dfrac{dV}{dr} \cdot \dfrac{dr}{dt}` | Chain rule decomposition |
| $\delta y \approx \dfrac{dy}{dx} \delta x$ | `\delta y \approx \dfrac{dy}{dx} \delta x` | Small-increment approximation |
| $V = \tfrac{4}{3}\pi r^3$ | `V = \tfrac{4}{3}\pi r^3` | Sphere volume |
| $V = \tfrac{1}{3}\pi r^2 h$ | `V = \tfrac{1}{3}\pi r^2 h` | Cone volume (for water-tank problems) |
| $x^2 + y^2 = L^2$ | `x^2 + y^2 = L^2` | Pythagoras (for ladder problems) |
