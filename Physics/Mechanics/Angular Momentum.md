---
chinese: 角动量 (jiǎo dòngliàng)
prerequisites:
  - "[[Torque]]"
  - "[[Moment of Inertia]]"
  - "[[Cross Product]]"
  - "[[Linear Momentum]]"
  - "[[Work, Energy and Power]]"
  - "[[Circular Motion]]"
  - "[[Gravitational Fields]]"
leads_to:
  - "[[Laws and Theorems]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - level/pre-AP
  - curriculum/A-Level-Further
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/IB-Physics-A-4-4
  - syllabus/AP-Physics-1-6-3
  - syllabus/AP-Physics-1-6-4
  - syllabus/AP-Physics-C-Mech-6-3
  - syllabus/AP-Physics-C-Mech-6-4
  - type/deep
  - type/definition
  - type/theorem
  - notation/angular-momentum
  - misconception/L-always-conserved
  - misconception/two-forms-of-L
  - misconception/conservation-means-omega-constant
  - misconception/KE-conserved-in-skater
---

# Angular Momentum 角动量

## Definition

### Formal

The **angular momentum** of a particle about a chosen origin is

$$\mathbf{L} = \mathbf{r} \times \mathbf{p} = \mathbf{r} \times m\mathbf{v},$$

a vector (a cross product — see [[Cross Product]]). Reading the symbols:

- $\mathbf{L}$ — the **angular momentum** vector (what we're defining), in $\text{kg·m}^2\text{s}^{-1}$;
- $\mathbf{r}$ — the **position vector** from the chosen origin (or axis) to the particle;
- $\mathbf{p} = m\mathbf{v}$ — the particle's **linear momentum**, i.e. mass $m$ times velocity $\mathbf{v}$;
- $\times$ — the **cross product** (so $\mathbf{L}$ is perpendicular to both $\mathbf{r}$ and $\mathbf{p}$, with magnitude $rp\sin\theta$).

Note that $\mathbf{L}$ depends on the origin you measure $\mathbf{r}$ from — angular momentum, like torque, is always "about a point." For a **rigid body** rotating about a fixed axis it collapses to the clean scalar form

$$\boxed{\;\mathbf{L} = I\boldsymbol{\omega}.\;}$$

It is the rotational analogue of linear momentum, and it obeys the rotational form of Newton's second law in its truest version:

$$\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}.$$

When the net external torque is zero, $\mathbf{L}$ is **conserved**. Units: $\text{kg·m}^2\,\text{s}^{-1}$.

### Intuitive

Linear momentum $\mathbf{p} = m\mathbf{v}$ measures how hard it is to *stop something moving in a straight line*. Angular momentum measures how hard it is to *stop something spinning* — and for a rigid body it is built the same way, **rotational mass times rotational velocity**, $L = I\omega$, exactly mirroring $p = mv$.

The headline is the conservation law. With no external torque, $L = I\omega$ stays fixed — so if the body's **moment of inertia changes**, its spin rate *must* change to compensate. Pull your arms in and your $I$ drops, so $\omega$ shoots up. That is the figure skater, the diver's tuck, and the collapsing star, all the same one-line statement: $I\omega$ is constant.

### 中文锚点

**角动量**（jiǎo dòngliàng）：转动版的动量。粒子 $\mathbf{L} = \mathbf{r}\times\mathbf{p}$；刚体绕定轴 $\mathbf{L} = I\boldsymbol{\omega}$。

转动版牛顿第二定律最本质的形式是 $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$。**无外力矩时，$L$ 守恒**（jiǎo dòngliàng shǒuhéng）。

核心直觉：因为 $L = I\omega$，外力矩为零时 $I\omega$ 不变——所以**收缩质量分布（$I$ 减小）会让转速 $\omega$ 增大**。花样滑冰收手臂、跳水团身、恒星塌缩成脉冲星，都是同一句话。平动 $p = mv$ ↔ 转动 $L = I\omega$；$\mathbf{F} = d\mathbf{p}/dt$ ↔ $\boldsymbol{\tau} = d\mathbf{L}/dt$；动量守恒（无外力）↔ 角动量守恒（无外力矩）。

## The analogy, completed

Torque gave the rotational *cause*, moment of inertia gave the rotational *resistance*; angular momentum supplies the rotational *quantity of motion* — and with it the linear-to-rotational dictionary is complete:

| Linear | Rotational |
|---|---|
| momentum $\mathbf{p} = m\mathbf{v}$ | angular momentum $\mathbf{L} = I\boldsymbol{\omega}$ |
| $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$ | $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$ |
| impulse $\int \mathbf{F}\,dt = \Delta\mathbf{p}$ | angular impulse $\int \boldsymbol{\tau}\,dt = \Delta\mathbf{L}$ |
| $\mathbf{p}$ conserved if no external **force** | $\mathbf{L}$ conserved if no external **torque** |

Every row is the same Newtonian statement with "push in a line" swapped for "twist about an axis." (See [[Linear Momentum]] for the left column — this card is its mirror.)

## Notation

| Symbol | Read as | Notes |
|---|---|---|
| $\mathbf{L}$ | angular momentum | $\mathbf{r}\times\mathbf{p}$ (particle) or $I\boldsymbol{\omega}$ (rigid body); $\text{kg·m}^2\text{s}^{-1}$ |
| $\boldsymbol{\tau} = d\mathbf{L}/dt$ | "torque is the rate of change of $\mathbf{L}$" | the exact rotational $\mathbf{F} = d\mathbf{p}/dt$ |
| $\int\boldsymbol{\tau}\,dt$ | angular impulse | equals $\Delta\mathbf{L}$ |
| $I_1\omega_1 = I_2\omega_2$ | conservation (fixed axis) | the working form when $\tau_{\text{ext}} = 0$ |

> [!warning] $L$ is overloaded
> Physics writes $L$ for angular momentum *and* often for a length (a pendulum or rod length). Context disambiguates; where both appear, this card keeps $L$ for angular momentum and spells out lengths.

## Key Facts / Properties

### 1. The two forms agree

For a particle of mass $m$ moving in a circle of radius $r$ at speed $v = r\omega$, the cross-product definition gives a vector along the axis of magnitude

$$L = rp = r(mv) = r\,m(r\omega) = (mr^2)\,\omega = I\omega,$$

since $I = mr^2$ for a point mass (from [[Moment of Inertia]]). Add up the particles of a rigid body and the same step gives $L = I\omega$ for the whole body. So $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ and $\mathbf{L} = I\boldsymbol{\omega}$ are the particle-level and body-level views of one quantity.

### 2. $\boldsymbol{\tau} = d\mathbf{L}/dt$ is the *real* rotational second law

Differentiate $\mathbf{L} = I\boldsymbol{\omega}$. **If $I$ is constant**, $\dfrac{d\mathbf{L}}{dt} = I\dfrac{d\boldsymbol{\omega}}{dt} = I\boldsymbol{\alpha} = \boldsymbol{\tau}$ — recovering the $\boldsymbol{\tau} = I\alpha$ of [[Moment of Inertia]]. But when $I$ can change, $\boldsymbol{\tau} = I\alpha$ breaks and only

$$\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}$$

survives. This is the deeper law — exactly as $\mathbf{F} = d\mathbf{p}/dt$ is deeper than $\mathbf{F} = m\mathbf{a}$ when mass changes (rockets). It is also what makes the next two facts work.

### 3. Conservation of angular momentum

Set the external torque to zero in $\boldsymbol{\tau} = d\mathbf{L}/dt$:

$$\boldsymbol{\tau}_{\text{ext}} = \mathbf{0} \;\Longrightarrow\; \mathbf{L} = \text{constant}.$$

For a body that rearranges its own mass about a fixed axis, this reads $I_1\omega_1 = I_2\omega_2$. Because $L$ is fixed, **shrinking $I$ forces $\omega$ up** — the figure skater, the tucking diver, and the star that collapses into a millisecond-period pulsar are the same equation at three scales. It is *internal* rearrangement: the skater's muscles supply no external torque, so $L$ can't change, only its split between $I$ and $\omega$.

![[angular-momentum-skater.png]]
*Conservation in one picture. Arms out, the skater has a large moment of inertia $I_1$ and turns slowly at $\omega_1$. Pulling the arms in drops the moment of inertia to $I_2 < I_1$; with no external torque, $L = I\omega$ can't change, so the spin rate jumps to $\omega_2 = (I_1/I_2)\,\omega_1$. Same $L$, traded between $I$ and $\omega$.*

### 4. Angular impulse

Integrating $\boldsymbol{\tau} = d\mathbf{L}/dt$ over time gives the **angular impulse–momentum theorem**,

$$\int \boldsymbol{\tau}\,dt = \Delta\mathbf{L},$$

the rotational copy of $\int\mathbf{F}\,dt = \Delta\mathbf{p}$ from [[Linear Momentum]]. A short, hard torque (a push on a flywheel, a cue striking a ball off-centre) changes $L$ by the area under the torque–time graph.

### 5. Gyroscopic precession — why a spinning top doesn't fall

Stand a spinning top at a tilt and gravity exerts a torque about the contact point. For a *non*-spinning top that torque just topples it. But a spinning top already has a large $\mathbf{L}$ along its axis, and gravity's torque is **perpendicular** to $\mathbf{L}$. By $\boldsymbol{\tau} = d\mathbf{L}/dt$, a perpendicular torque doesn't lengthen or shorten $\mathbf{L}$ — it *rotates its direction*. So the axis sweeps round in a slow horizontal circle instead of falling: **precession** (进动, jìndòng). The top isn't defying gravity; it's obeying $\boldsymbol{\tau} = d\mathbf{L}/dt$ in the one way that changes direction without changing magnitude.

## Worked Examples

### Example 1 (the figure skater) — and the energy twist

A skater spins at $\omega_1 = 2\ \text{rev s}^{-1}$ with arms out, moment of inertia $I_1$. She pulls her arms in, halving her moment of inertia to $I_2 = \tfrac12 I_1$. No external torque acts, so $L$ is conserved:

$$I_1\omega_1 = I_2\omega_2 \;\Rightarrow\; \omega_2 = \frac{I_1}{I_2}\,\omega_1 = 2\omega_1 = 4\ \text{rev s}^{-1}.$$

She spins **twice as fast**. Now check the kinetic energy:

$$\text{KE}_2 = \tfrac12 I_2\omega_2^2 = \tfrac12\big(\tfrac12 I_1\big)(2\omega_1)^2 = 2\cdot\tfrac12 I_1\omega_1^2 = 2\,\text{KE}_1.$$

The rotational KE **doubles** — energy is *not* conserved here, even though angular momentum is. Where did it come from? **The skater did work** pulling her arms inward against the outward pull they feel while circling; that muscular work is exactly the extra KE. The lesson: conservation of $L$ and conservation of energy are different statements, and a problem can honour one while breaking the other.

### Example 2 (Kepler's second law) — orbits run on conservation of $L$

A planet orbits the Sun under gravity, which always points *along* the line from planet to Sun. The torque about the Sun is $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F} = \mathbf{0}$, because $\mathbf{r}$ and $\mathbf{F}$ are parallel (a radial force has zero moment arm — see [[Cross Product]]). So the planet's angular momentum about the Sun is conserved, which is exactly **Kepler's second law**: the line from Sun to planet sweeps out equal areas in equal times (the areal speed is $\tfrac{1}{2}L/m$). A planet speeds up near the Sun and slows far away for the same reason the skater speeds up with arms in — $L$ is fixed and $r$ has shrunk.

## Common Misconceptions (Teaching Notes)

### 1. "Angular momentum is always conserved"

It's conserved only when the **net external torque is zero** — exactly parallel to linear momentum needing zero net external *force*.

**Fix.** Always name the system and check the external torque first. Internal forces (the skater's muscles, an explosion) can't change $L$; an external torque (friction at the axle, a hand on the rim) can.

### 2. Confusing the two forms of $L$

Using $L = I\omega$ for a single particle flying past, or $L = mvr$ for an extended spinning body.

**Fix.** $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ is the universal definition (any object, any origin); $L = I\omega$ is the specialisation for a *rigid body about a fixed axis*. When in doubt, fall back on $\mathbf{r}\times\mathbf{p}$.

### 3. "Conservation of $L$ means $\omega$ stays constant"

Students freeze $\omega$ when they should freeze $L$.

**Fix.** It's the *product* $I\omega$ that's conserved. If $I$ changes, $\omega$ changes the opposite way. The skater is the antidote image.

### 4. "Kinetic energy is conserved in the skater problem"

Assuming KE is fixed because "nothing was added."

**Fix.** Only $L$ is conserved. KE rises ($\text{KE} = \tfrac{L^2}{2I}$, so smaller $I$ means larger KE) because the skater does work pulling inward. Conservation of $L$ and conservation of energy are separate laws — don't assume both.

### 5. "A gyroscope defies gravity"

Treating precession as anti-gravity magic.

**Fix.** Gravity's torque is perpendicular to $\mathbf{L}$, so by $\boldsymbol{\tau} = d\mathbf{L}/dt$ it rotates $\mathbf{L}$ rather than dropping it. The top obeys the same law as everything else; the geometry just happens to turn "fall" into "precess."

## The symmetry–conservation trio — now complete (Noether)

This card closes a thread running through the whole mechanics bay. Emmy Noether's theorem (1915) says every continuous symmetry of the laws of physics yields a conserved quantity, and there are three headline cases:

| Symmetry of the laws | Conserved quantity | Card |
|---|---|---|
| Time-translation (laws don't change over time) | **Energy** | [[Work, Energy and Power]] |
| Space-translation (no special place) | **Linear momentum** | [[Linear Momentum]] |
| **Rotation (no special direction)** | **Angular momentum** | *this card* |

[[Linear Momentum]] and [[Work, Energy and Power]] each carry two-thirds of this table and point here for the third. **Angular momentum is conserved because space has no preferred direction** — orient your experiment any way you like and the physics is identical. The three great conservation laws of mechanics are not three separate facts about the world; they are one fact (Noether) seen through three windows. (Those continuous symmetries — rotate by *any* angle — themselves form a group; the mathematical home of "symmetry as an object" is [[Group Theory]].)

## Exam Notes

> Like the rest of the trio, angular momentum is **not** on Cambridge 9709, 9702, or 9231 (whose Further Mechanics stops at rigid-body statics), and not on plain IB AA. Its homes are below.

### IB Physics (A.4.4 — *HL only*)

Angular momentum $L = I\omega$, its conservation, and angular impulse. Pairs with A.4.1–A.4.3 ([[Torque]], [[Moment of Inertia]]) to make up the HL-only **Rigid body mechanics** topic. (A.4.2 angular *kinematics* — the $\theta,\omega,\alpha$ equations of motion — is the one A.4 sub-topic the trio doesn't cover.)

### AP Physics 1 (Unit 6.3, 6.4) & AP Physics C: Mechanics (Unit 6.3, 6.4)

Both examine **angular momentum and angular impulse** (6.3) and **conservation of angular momentum** (6.4); AP-C writes the particle definition $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ and angular impulse $\int\boldsymbol{\tau}\,dt$ explicitly. The classic prompts are the spinning-stool / pulled-in-arms problem and a person walking to the centre of a rotating platform.

### A-Level Further Mathematics (UK — Edexcel / AQA)

Conservation of angular momentum about a fixed axis appears in **Edexcel/AQA** A-Level Further Mechanics, alongside [[Moment of Inertia]]. (Not Cambridge 9231.)

## Connections

- **Prerequisites — the rest of the trio:** [[Torque]] ($\boldsymbol{\tau} = d\mathbf{L}/dt$) and [[Moment of Inertia]] ($L = I\omega$, and the figure-skater whose $I$ change this card cashes).
- **Mathematical prerequisite:** [[Cross Product]] — $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ is a cross product; the zero-torque-of-a-radial-force argument (Kepler) is its $\sin\theta = 0$ case.
- **The linear mirror:** [[Linear Momentum]] — every fact here is the rotational image of a fact there; together they hold two legs of the Noether trio.
- **Noether trio:** [[Work, Energy and Power]] — energy ↔ time symmetry; this card supplies angular momentum ↔ rotational symmetry, completing the set.
- **Application:** [[Simple Harmonic Motion]] — with the trio complete, the pendulum's $\tau = I\,\frac{d^2\theta}{dt^2}$ derivation no longer rests on faith; every piece now has a home.

---

## Beyond Syllabus

### Kepler's second law is just conservation of $L$

Worth stating plainly (it's Example 2's punchline): the "equal areas in equal times" law that Kepler extracted from Tycho Brahe's data in 1609 is nothing more than angular momentum conservation under a central force. Newton later showed *any* central force gives it; gravity's inverse-square nature is what fixes the *shape* (an ellipse), but the equal-areas sweep is pure $\mathbf{L} = \text{const}$.

### Quantised spin — angular momentum at the bottom

Angular momentum is one of the few classical quantities that survives into quantum mechanics essentially intact — but **quantised**. Orbital angular momentum comes in integer multiples of the reduced Planck constant $\hbar$; the Bohr model's quantisation condition is literally $L = n\hbar$. And particles carry an *intrinsic* angular momentum, **spin**, that has no classical rotating-ball picture at all — the electron's is $\tfrac12\hbar$. Conservation of angular momentum is exact and universal, from skaters to selection rules for atomic transitions.

### The falling cat

A dropped cat lands feet-down even when released with **zero** angular momentum and no way to push off anything — seemingly impossible if "no $L$" meant "can't turn." The resolution: a deformable body can *reorient* itself at zero total $L$ by changing its shape in a cyclic way (a "geometric phase"), bending and counter-rotating front and back halves. Conservation of $L$ forbids net *spin*, not net *turning* — a subtlety that took until 1969 (and high-speed photography) to settle, and that underlies how astronauts and divers reorient in free fall.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{L}$ | `\mathbf{L}` | Angular momentum vector |
| $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ | `\mathbf{r}\times\mathbf{p}` | Particle definition |
| $\mathbf{L} = I\boldsymbol{\omega}$ | `I\boldsymbol{\omega}` | Rigid body about a fixed axis |
| $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$ | `\dfrac{d\mathbf{L}}{dt}` | Exact rotational 2nd law |
| $\int\boldsymbol{\tau}\,dt = \Delta\mathbf{L}$ | `\int\boldsymbol{\tau}\,dt` | Angular impulse |
| $I_1\omega_1 = I_2\omega_2$ | `I_1\omega_1 = I_2\omega_2` | Conservation, fixed axis |
| $\hbar$ | `\hbar` | Reduced Planck constant (quantised spin) |
