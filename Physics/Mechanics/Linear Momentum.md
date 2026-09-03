---
chinese: 线动量 / 动量 (xiàn dòngliàng / dòngliàng)
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Vectors]]"
  - "[[Vectors in Physics]]"
  - "[[Kinematics Calculus]]"
  - "[[Area Under a Graph (Vocab)]]"
leads_to:
  - "[[Newton's Law of Restitution]]"
  - "[[Impulse]]"
  - "[[Centre of Mass]]"
  - "[[Rocket Equation]]"
  - "[[Two-Body Problem]]"
  - "[[Angular Momentum]]"
  - "[[Choosing Effective Equations]]"
  - "[[Kinetic Theory and the Ideal Gas]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - level/IGCSE-extension
  - curriculum/Cambridge-9709
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9709-4-3
  - syllabus/9702-3-1
  - syllabus/9702-3-3
  - syllabus/0625-1-6
  - syllabus/IB-Physics-A-2-3
  - syllabus/AP-Physics-1-4-1
  - syllabus/AP-Physics-1-4-2
  - syllabus/AP-Physics-1-4-3
  - syllabus/AP-Physics-C-Mech-4-1
  - syllabus/AP-Physics-C-Mech-4-2
  - syllabus/AP-Physics-C-Mech-4-3
  - syllabus/AP-Physics-C-Mech-4-4
  - syllabus/9231-3-6
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/momentum-p
  - notation/impulse-J
  - notation/delta-p
  - misconception/momentum-equals-energy
  - misconception/conservation-needs-equilibrium
  - misconception/equal-and-opposite-velocities-after-collision
  - misconception/heavy-always-has-more-momentum
---

# Linear Momentum 动量

## Definition

The **linear momentum** of a body is its mass times its velocity:

$$
\boxed{\;\mathbf{p} \;=\; m\mathbf{v}\;}
$$

It is a **vector** — same direction as the velocity, magnitude $\lvert \mathbf{p} \rvert = m \lvert \mathbf{v} \rvert$. SI units are $\text{kg} \cdot \text{m/s}$ (no special name; sometimes written $\text{N} \cdot \text{s}$, since $\text{kg} \cdot \text{m/s}^2 \cdot \text{s} = \text{kg} \cdot \text{m/s}$).

The word "linear" distinguishes it from **angular momentum** $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ — the rotational analogue. When this card says "momentum" without qualifier, it means *linear* momentum specifically. See [[Angular Momentum]] for the rotational story: rigid-body rotation, conservation under central forces, and why an ice-skater spins faster when she pulls her arms in.

### 中文锚点

**线动量 (xiàn dòngliàng)** — 通常简称为 **动量 (dòngliàng)**。

$$
\mathbf{p} \;=\; m\mathbf{v}\,, \qquad \text{单位：} \text{kg} \cdot \text{m/s}
$$

- $\mathbf{p}$ 是**矢量**，方向与速度相同
- 大小 $\lvert \mathbf{p} \rvert = m \lvert \mathbf{v} \rvert$（质量 × 速率）
- "Linear" 用来与**角动量 (jiǎo dòngliàng)** $\mathbf{L} = \mathbf{r} \times \mathbf{p}$ 区分。本卡片里"momentum"默认指线动量；旋转的情形见 [[Angular Momentum]]

考试关键判断：
- 动量是**矢量**，方向重要；速率（scalar）只看大小
- "Conservation of momentum" 守恒条件：**外力的合力为零**（不等于 equilibrium！）
- 碰撞后两物体**速度未必相等**；只有"完全非弹性碰撞"（粘在一起）才共速

### Why momentum deserves its own concept (and not just "mass times velocity")

Mass and velocity already exist as separate things; multiplying them feels like notation, not physics. The reason momentum is a *named quantity* is that it shows up in three places where neither $m$ nor $\mathbf{v}$ alone would:

1. **Newton's 2nd law in its general form** — $\mathbf{F} = d\mathbf{p}/dt$. The most natural state-variable for "what a force changes" is $\mathbf{p}$, not $\mathbf{v}$. (See [[Newton's Laws of Motion#The Second Law — F = ma is the *Definition* of Force|N2 unit-algebra check]] for why the two forms are equivalent for constant mass.)

2. **A conservation law** — total momentum of an isolated system is constant in time. Mass and velocity have no equivalent statement: total mass is conserved separately (and trivially, in non-relativistic physics), and total velocity has no defined meaning at all.

3. **The currency of collisions** — when bodies bounce, stick, or explode apart, what's *transferred* between them is momentum. Energy is also transferred but not always conserved (heat, sound, deformation drain it); momentum *is* always conserved across a collision.

So momentum is more than "mass × velocity." It's the bookkeeping unit for which Newtonian mechanics has a conservation law.

---

## Conservation of Linear Momentum — and where the law comes from

### Statement

> **Conservation of linear momentum.** For a system of bodies that experiences no net external force, the total linear momentum is constant in time:
>
> $$\sum_i \mathbf{p}_i \;=\; \text{const.}$$
>
> Equivalently, before and after any internal interaction (collision, explosion, rope tug, magnetic push), the *total* momentum vector is the same.

The phrase **isolated system** (or **closed system** when the boundary doesn't matter) means: no external forces from outside the system act on it, *or* those external forces sum to zero. Friction with the ground, gravity, an experimenter's push — all "external" if they come from outside the bodies you're tracking.

### Derivation — N3 + N2 = momentum conservation

This is one of the most beautiful single-page derivations in classical mechanics, and the reason your students should know **Newton's Third Law and Linear Momentum cannot be separated**.

**Setup.** Two bodies, $A$ and $B$, alone in the universe (no external forces). $A$ exerts a force $\mathbf{F}_{AB}$ on $B$; $B$ exerts a force $\mathbf{F}_{BA}$ on $A$.

**Step 1 — N3.** Newton's 3rd law says these two forces are an action-reaction pair:

$$\mathbf{F}_{AB} \;=\; -\mathbf{F}_{BA}.$$

**Step 2 — N2 on each body.** Each force changes the corresponding body's momentum:

$$\mathbf{F}_{AB} \;=\; \dfrac{d\mathbf{p}_B}{dt}\,, \qquad \mathbf{F}_{BA} \;=\; \dfrac{d\mathbf{p}_A}{dt}.$$

**Step 3 — Add them.** Substituting Step 2 into Step 1:

$$\dfrac{d\mathbf{p}_B}{dt} \;=\; -\dfrac{d\mathbf{p}_A}{dt} \;\Longleftrightarrow\; \dfrac{d}{dt}\!\left(\mathbf{p}_A + \mathbf{p}_B\right) \;=\; \mathbf{0}.$$

**Step 4 — Read it.** The total momentum $\mathbf{p}_A + \mathbf{p}_B$ has zero rate of change. So it is constant in time.

$$\boxed{\;\mathbf{p}_A + \mathbf{p}_B \;=\; \text{const.}\;}$$

That's the entire proof. Three lines of algebra: N3 says the forces are equal-and-opposite, N2 says each force is the rate of change of the corresponding body's momentum, addition gives a zero rate of change of the total. The conservation law is *forced* by N3.

![[newton-momentum-conservation-derivation.svg|697]]

*The picture in two panels. **(a)** The setup: $A$ pushes $B$ to the left, so by N3 $B$ pushes $A$ to the right with equal magnitude. By N2, each body's momentum changes at exactly the rate of the corresponding force — so the dp/dt arrows are equal-and-opposite for the same reason the forces are. **(b)** The bookkeeping: across the interaction, $p_A$ rises and $p_B$ falls by exactly matching amounts; their sum stays perfectly flat. The dashed green line is the conservation law in action — it's literally the time-axis of the total momentum, drawn at constant height.*

The same argument generalises to $n$ bodies — every internal pair cancels by N3, and what remains is the rate of change of the total, equal to the sum of *external* forces. If the external forces sum to zero, total momentum is conserved.

> [!info] Beyond syllabus — Noether's theorem
> The deeper reason momentum is conserved is **Noether's theorem (1915)**: every continuous symmetry of the laws of physics implies a conservation law. *Spatial translation symmetry* — the laws of physics are the same here as five metres to the left — implies *momentum conservation*. *Time translation symmetry* — laws don't change tomorrow — implies energy conservation. *Rotational symmetry* implies angular momentum conservation. Three rock-solid conservation laws, three obvious symmetries. This is the most beautiful structural fact in physics. (Emmy Noether's mathematical proof is graduate-level; the statement is high-school-comprehensible.)

---

## Collisions — the canonical application

A **collision** is a brief interaction between two (or more) bodies during which internal forces dominate and external forces are negligible. Within the collision window, momentum is conserved.

There are three flavours, distinguished by what happens to *kinetic energy*:

| Type | Momentum | Kinetic energy | Bodies after |
|---|---|---|---|
| **Perfectly inelastic** (coalescing) | conserved | partly lost (heat, sound, deformation) | stuck together — same velocity |
| **Inelastic** | conserved | partly lost | separate — different velocities |
| **Elastic** | conserved | also conserved | separate — special algebraic case |

> [!info] 9709 Paper 4 scope (AS Mechanics)
> The 9709 P4 syllabus restricts collisions to **direct impact in 1D, with coalescence**. That's the perfectly inelastic case — the simplest. Impulse and coefficient of restitution are *not* required at this level. Elastic collisions appear at full A-Level (9702 §3.3) and at IB / AP.

### Perfectly inelastic (coalescing) — the 9709 P4 case

Two bodies stick together on impact and move with a common velocity $\mathbf{v}'$. Conservation:

$$m_1 \mathbf{u}_1 + m_2 \mathbf{u}_2 \;=\; (m_1 + m_2)\, \mathbf{v}'.$$

Solving for the common velocity:

$$\mathbf{v}' \;=\; \dfrac{m_1 \mathbf{u}_1 + m_2 \mathbf{u}_2}{m_1 + m_2}.$$

This is also the formula for the **centre-of-mass velocity** of the two-body system, which doesn't change during the collision (no external force).

### Elastic — A-Level / IB / AP

Both momentum and kinetic energy are conserved:

$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 \qquad \text{(momentum)}$$
$$\tfrac{1}{2} m_1 u_1^2 + \tfrac{1}{2} m_2 u_2^2 = \tfrac{1}{2} m_1 v_1^2 + \tfrac{1}{2} m_2 v_2^2 \qquad \text{(KE)}$$

Two equations, two unknowns ($v_1, v_2$). The clean trick: subtract pairs algebraically and you get a famous identity:

$$\boxed{\;u_1 - u_2 \;=\; -(v_1 - v_2)\;}$$

> "In an elastic collision, the relative velocity of approach equals the relative velocity of separation, with sign reversed."

This is the *test* for elasticity (and the beating heart of the **coefficient of restitution** at A-Level: $e = -(v_1 - v_2)/(u_1 - u_2)$, with $e = 1$ elastic, $e = 0$ perfectly inelastic, $0 < e < 1$ partially elastic).

**Special case — equal masses, one initially at rest:** if $m_1 = m_2$ and $u_2 = 0$, the formula collapses to $v_1 = 0$ and $v_2 = u_1$. **The masses swap velocities.** This is what you see on a Newton's-cradle desk toy and the basis of many AP / IB problems.

### How can you tell which collision will happen in real life?

The maths above is symmetric: given any two objects, momentum conservation alone doesn't fix what fraction of kinetic energy is preserved. Whether a collision ends up elastic, partially inelastic, or perfectly inelastic depends on **what the bodies are made of and what they can do with kinetic energy**. The energy budget needs somewhere to go for the collision to be inelastic — and that "somewhere" is *physical*:

- **Sound waves** radiating into the surrounding air. (Loud collision = inelastic.)
- **Heat** in the material from internal friction. (Warm bodies after collision.)
- **Permanent deformation** — atoms displaced from their lattice positions. (Crumpled metal, broken glass.)
- **Vibration / oscillation** of the bodies themselves after impact.

If a material is *hard* and *highly elastic* (like steel ball bearings, glass marbles, snooker balls, billiard balls), almost all the kinetic energy is briefly stored as elastic compression of the material and released back as kinetic energy. The collision is *almost perfectly elastic* — coefficient of restitution close to 1. If the material is *soft* and *plastic* (clay, putty, lead), most of the kinetic energy goes into permanent deformation. The collision is highly inelastic — $e$ close to 0.

![[snooker-elastic-collision.png]]

> [!info] Snooker — a sport built on engineered elasticity
> Snooker (and pool, billiards) is the rare case where humans have learned to control the elasticity of a collision to a degree that looks like wizardry. The balls are precision-machined from phenolic resin (super-hard, $e \approx 0.95$ between balls), and the cushions on the table edges have a similar coefficient. *Almost* perfectly elastic.
>
> Skilled players exploit two things the simple equations don't capture:
> - **Spin (English)** — striking the cue ball off-centre adds angular momentum, which on impact transfers some kinetic energy into and out of the rotational degree of freedom. A player can make the cue ball stop dead, screw back, or follow through, just by where on the ball the cue strikes. (This is *why* the equal-mass elastic "stops dead" result of Example 2 is the *default* on a snooker table — and why mastering spin is the whole game.)
> - **Cushion angles** — the cushion surface isn't perfectly elastic, and balls travelling fast lose more energy on the rail than slow balls (the deformation gets nonlinear). World-class players carry an internal table of how much speed they lose off each rail at each angle. They are *integrating the coefficient of restitution* against the chosen trajectory.
>
> A snooker player has internalised, in their muscle memory, a richer model of collision than any equation we'll write at A-Level. The bridge between "$e = 0.95$" on paper and "I want the cue ball to come back to *here*" on the table is several years of practice.

![[car-crumple-zone.png]]

> [!info] Cars — engineered inelasticity, on purpose
> The opposite engineering goal: a car designer *wants* a collision to be **as inelastic as possible**, because the only way to lower the force on the passengers is to spread the change of momentum over a longer time:
>
> $$F = \dfrac{\Delta p}{\Delta t}.$$
>
> The driver's $\Delta p$ is fixed by their mass and the impact speed — there's no negotiating with that. So to reduce the force $F$, you stretch out $\Delta t$. **Crumple zones** are the engineering answer: front and rear sections of the car frame are designed to *deform* over a few tens of centimetres on impact, dissipating kinetic energy as plastic deformation (heat, twisted metal) and extending the deceleration window from ~1 ms (rigid impact) to ~100 ms. That's a hundred-fold reduction in peak force on whatever is behind the crumple zone — including you.
>
> The whole impact-engineering toolkit — crumple zones, airbags, seatbelts with pretensioners and load-limiters, motorcycle helmets, running shoes, gymnastics mats, even bubble wrap — is the same idea: *trade a lot of $\Delta t$ for a lot less $F$*. Momentum conservation says the change of momentum is forced; impulse $J = F\,\Delta t$ says how to negotiate the cost.

The two examples — snooker and crumple zones — sit at opposite ends of the elasticity spectrum, but they're solved by the *same* physics: $\Delta p$ is fixed by the input velocities; what you can control is how much energy is dissipated and how long the collision lasts.

---

## Worked Examples

![[newton-collisions-1d.svg|697]]

### Example 1 — Coalescing trolleys (9709 P4 §4.3)

A 3 kg trolley moves at 4 m/s and collides with a stationary 5 kg trolley. They couple together. Find the common velocity afterwards.

Take rightward as positive. Conservation of momentum:

$$(3)(4) + (5)(0) \;=\; (3 + 5)\, v' \;\Rightarrow\; 12 = 8 v' \;\Rightarrow\; v' = \boxed{1.5 \text{ m/s}}.$$

Sanity check: $v' = 1.5$ m/s is between 0 and 4 (it has to be — the moving trolley loses momentum to the stationary one), and closer to 0 because the stationary trolley is heavier.

> [!tip] Energy check (beyond 9709 P4)
> KE before: $\tfrac{1}{2}(3)(16) = 24$ J. KE after: $\tfrac{1}{2}(8)(1.5^2) = 9$ J. **15 J lost** to heat, sound, and deformation. The collision is *perfectly inelastic* — the maximum-energy-loss case consistent with momentum conservation. (Try any other split of velocities afterwards; you'll find the coalescing case is the one that *minimises* final KE.)

### Example 2 — Elastic collision, equal masses (9702 §3.3, AP, IB)

A 2 kg ball moves at 6 m/s and collides elastically with a stationary 2 kg ball. Find the velocities afterwards.

Equal masses + one at rest = velocity exchange (the clean special case from above):

$$v_1 = 0 \text{ m/s}, \qquad v_2 = 6 \text{ m/s}.$$

Verify both conservation laws:
- Momentum: $(2)(6) + 0 = 12 \;\;\checkmark\;\; (2)(0) + (2)(6) = 12$.
- KE: $\tfrac{1}{2}(2)(36) = 36 \text{ J} \;\;\checkmark\;\; \tfrac{1}{2}(2)(0) + \tfrac{1}{2}(2)(36) = 36 \text{ J}$.

The first ball *stops dead*. This violates everyone's first guess ("the first ball must keep going a bit") and is exactly what makes Newton's cradle work.

### Example 3 — Recoil (the gun, the rocket, and N3 in disguise)

A 0.02 kg bullet is fired at 400 m/s from a 4 kg rifle, initially at rest. Find the recoil velocity of the rifle.

The system (rifle + bullet) starts with total momentum $0$. No external horizontal force during firing (the explosion is internal). After firing, total momentum is *still* $0$:

$$m_{\text{bullet}} v_{\text{bullet}} + m_{\text{rifle}} v_{\text{rifle}} \;=\; 0.$$

$$0.02 \times 400 + 4 \times v_{\text{rifle}} \;=\; 0 \;\Rightarrow\; v_{\text{rifle}} = -2 \text{ m/s}.$$

The rifle moves backward at 2 m/s. Notice the *ratio*: the bullet is 200× lighter than the rifle, so its speed is 200× larger. This is the operating principle of every **rocket** (eject mass at high speed → vehicle gains opposite momentum) and the standard trap question on N3 ("if the rifle pushes the bullet, why doesn't the rifle move as fast?").

### Example 4 — Bullet embeds in block (9709 P4 §4.3 boundary case)

A 10 g bullet travelling at 500 m/s strikes a 2 kg wooden block at rest, embeds in it, and the block-with-bullet slides off together. Find the common speed.

This is Example 1 in disguise — a coalescing collision. Convert grams to kilograms:

$$(0.01)(500) + (2)(0) \;=\; (0.01 + 2)\, v' \;\Rightarrow\; 5 = 2.01 v' \;\Rightarrow\; v' \approx \boxed{2.49 \text{ m/s}}.$$

(Half a percent of the bullet's original speed. Heavy block; light, fast bullet; slow combined motion. This is exactly what's exploited in the **ballistic pendulum** — the classic experiment for measuring bullet speeds before electronic chronographs existed.)

---

## Impulse — the time integral of force

For 9702 (and 0625 Extended), Newton's 2nd law in integral form gives **impulse**:

$$\mathbf{J} \;=\; \int_{t_0}^{t_1} \mathbf{F}\, dt \;=\; \Delta \mathbf{p}.$$

**Statement in words:** the impulse delivered by a force is the *area under the force-time graph*, and equals the change in momentum it produces.

![[newton-impulse-Ft-graph.svg|697]]

For a **constant** force, the formula simplifies to $\mathbf{J} = \mathbf{F} \Delta t$. SI units: $\text{N} \cdot \text{s}$ — same units as momentum (we noted this above; this is *why*).

> [!info] Why "area under F-t = change in momentum" is just the FTC
> Newton's 2nd law in differential form is $\mathbf{F} = d\mathbf{p}/dt$. Integrating both sides from $t_0$ to $t_1$:
>
> $$\int_{t_0}^{t_1} \mathbf{F}\, dt \;=\; \int_{t_0}^{t_1} \dfrac{d\mathbf{p}}{dt}\, dt \;=\; \mathbf{p}(t_1) - \mathbf{p}(t_0) \;=\; \Delta \mathbf{p}.$$
>
> The right-hand side is the [[Fundamental Theorem of Calculus]] in action — antiderivatives evaluated at endpoints. Impulse-momentum theorem is FTC applied to N2. See [[Area Under a Graph (Vocab)]] for the IGCSE-level visual version of "area = change."

> [!warning] 9709 P4 does NOT examine impulse
> Cambridge 9709 Paper 4 (Mechanics, AS) explicitly *excludes* impulse and the coefficient of restitution. If your student is sitting only 9709, they don't need this section. It's required for 9702, 0625 Extended, A-Level (any board), IB, and AP.

---

## Common Misconceptions

### 1. "Heavy objects always have more momentum"

False — momentum depends on *both* mass and velocity. A 0.01 kg bullet at 500 m/s carries 5 kg·m/s of momentum; a 70 kg person walking at 1 m/s carries 70 kg·m/s. The walking person wins by mass; speed it up enough and the bullet wins. **Speed is the multiplier**, and high-speed light objects (bullets, photons, neutrons) are the standard counterexamples.

### 2. "Momentum and energy are the same thing"

Closely related, both bookkeeping quantities for "how much motion," but distinct:
- Momentum is a **vector** ($\mathbf{p} = m\mathbf{v}$), kg·m/s, conserved in *any* collision.
- Kinetic energy is a **scalar** ($\tfrac{1}{2}mv^2$), joules, conserved only in *elastic* collisions.

A coalescing collision conserves momentum (the rule that gave us $v' = 1.5$ m/s in Example 1) and *destroys* kinetic energy (15 J vanished). Keeping the two ideas separate is the pedagogical heart of A-Level mechanics.

### 3. "Conservation of momentum means equilibrium"

No. Equilibrium ($\Sigma \mathbf{F} = 0$) is a statement about *one body* having zero acceleration. Conservation of momentum is a statement about a *system of bodies* having constant total $\sum \mathbf{p}$. The system can be flying apart in opposite directions (rifle and bullet, fission products) — neither body is in equilibrium, but the *sum* of their momenta is unchanged.

The condition for momentum conservation is *no external net force on the system as a whole*. Internal forces between members of the system can be enormous (collisions, explosions) and conservation still holds.

### 4. "After a collision both bodies must move with equal speeds"

Only if they coalesce (perfectly inelastic). In any other collision, the bodies emerge with *different* velocities determined by both conservation of momentum and the elasticity (or coefficient of restitution).

### 5. "The bullet pushed harder, so it accelerated more"

The bullet and rifle exert *equal-magnitude* forces on each other (N3). What differs is the *acceleration*, because $a = F/m$ and the bullet has tiny $m$. Same force, different mass, vastly different acceleration. The recoil example is built around this.

---

## Exam Notes

### Cambridge 9709 Paper 4 (Mechanics, AS) — §4.3

**In scope:**
- Definition $\mathbf{p} = m\mathbf{v}$, vector nature.
- Conservation of momentum applied to direct impact in 1D.
- **Coalescence** (perfectly inelastic) only.

**Explicitly NOT in scope:**
- Impulse.
- Coefficient of restitution.
- Elastic collisions in 1D.
- 2D collisions or oblique impacts.

Use $g$ values from §4.4 conventions if weight enters (it usually doesn't for collision problems on a smooth horizontal surface). Vector notation will not appear; resolve into scalar components by direction.

### Cambridge 9702 (A-Level Physics) — §3.1, §3.3

§3.1 introduces $\mathbf{p}$ and $\mathbf{F} = d\mathbf{p}/dt$.
§3.3 covers conservation including **elastic and inelastic** 1D collisions. Use the *relative-velocity-reversal* test ($u_1 - u_2 = -(v_1 - v_2)$) to recognise elasticity. Vector notation appears explicitly. Impulse $\mathbf{J} = \Delta \mathbf{p}$ is examinable.

> [!info] On the 9702 data sheet
> **No momentum or impulse formulas are given.** $\mathbf{p} = m\mathbf{v}$ and $\mathbf{J} = \Delta \mathbf{p}$ are language to memorise. The relative-velocity-reversal identity is *not* given — you derive it on the spot from energy + momentum conservation.

### Cambridge 0625 (IGCSE Physics) — §1.6

**Core:** definition $p = mv$, conservation in collisions (qualitative + simple numerical).
**Extended only:** impulse $F = \Delta p / \Delta t$ as the rearranged N2; force-time graph reading.

### A-Level Mathematics Mechanics (9709 M2 / OCR / Edexcel) and IB AA

Includes elastic collisions in 1D, coefficient of restitution $e$, **2D oblique impacts** (resolve along and perpendicular to the line of impact; $e$ acts only along the line of impact). IB AA HL also covers 2D collisions.

### AP Physics 1 / C: Mechanics

**AP Physics 1:** conservation of momentum, impulse, 1D and 2D collisions, all qualitatively and through pictorial analysis.
**AP Physics C: Mechanics:** all of the above plus integral form $\mathbf{J} = \int \mathbf{F}\, dt$, variable-mass problems (rocket equation), and centre-of-mass treatment.

---

## Why Linear Momentum Matters — College and Beyond

- **Rocket science** — the *only* way to accelerate in the vacuum of space is to throw mass backward (no road to push against). The **Tsiolkovsky equation** $\Delta v = v_e \ln(m_0 / m_f)$ comes from integrating momentum conservation as the rocket loses mass over time. SpaceX's Falcon 9 follows this equation to the gram.
- **Particle physics** — every proton-proton collision at the LHC conserves total 4-momentum. Tracks emerging from a collision are reconstructed by *imposing* $\sum \mathbf{p}_i = \sum \mathbf{p}_f$ across hundreds of debris particles. The Higgs boson was discovered (2012) by spotting bumps in a momentum-balance plot.
- **Quantum mechanics** — momentum is one of the two fundamental observables (with position). de Broglie's $\lambda = h/p$ relates wavelength to momentum, and the Heisenberg uncertainty principle states $\Delta x \cdot \Delta p \geq \hbar/2$ — see [[Upper and Lower Bounds#Heisenberg's uncertainty principle|the ULB note]].
- **Special relativity** — the *non-relativistic* $\mathbf{p} = m\mathbf{v}$ is replaced by $\mathbf{p} = \gamma m \mathbf{v}$ where $\gamma = 1/\sqrt{1 - v^2/c^2}$. Newton's 2nd in the $\mathbf{F} = d\mathbf{p}/dt$ form *survives* — only the constant-mass corollary $\mathbf{F} = m\mathbf{a}$ fails. This is one reason the more general form is the "real" N2.
- **Symmetry and conservation laws** — Noether's theorem (1915) proves that conservation of momentum is exactly the mathematical consequence of *spatial translation invariance* of physical laws. Move your experiment one metre to the side; the laws are the same; therefore momentum is conserved. This connection between symmetry and conservation is the deepest organising principle in modern physics.

> [!tip] The conservation-law trio
> Three conservation laws govern almost all of classical and quantum mechanics:
>
> | Symmetry | Conservation law |
> |---|---|
> | Spatial translation | **Momentum** |
> | Time translation | **Energy** |
> | Rotation | **Angular momentum** |
>
> Each conservation law is a direct consequence (Noether) of the corresponding symmetry of physical law. This trio is the structural backbone of physics — and you've now met the first one.

---

## Connections

- **Prerequisite:** [[Newton's Laws of Motion]] — N2 in $\mathbf{F} = d\mathbf{p}/dt$ form; N3 is the *reason* momentum is conserved.
- **Prerequisite:** [[Vectors]] — momentum is a vector; collisions in 2D need vector decomposition.
- **Prerequisite:** [[Kinematics Calculus]] — momentum conservation over time as the integrated form of N2.
- **Prerequisite:** [[Area Under a Graph (Vocab)]] — the IGCSE-level reading of "area under F-t = impulse."
- **Component:** [[Impulse]] — the time integral $\mathbf{J} = \int \mathbf{F}\, dt = \Delta \mathbf{p}$.
- **Sibling:** [[Kinetic Energy]] — the *other* "how much motion" bookkeeping, scalar, conserved only in elastic collisions; together with momentum it determines collision outcomes uniquely.
- **Extension:** [[Centre of Mass]] — the system point that moves at $\mathbf{p}_{\text{total}} / m_{\text{total}}$; momentum conservation = "the centre of mass coasts."
- **Extension:** [[Rocket Equation]] — momentum conservation applied to a vehicle losing mass.
- **Extension:** [[Coefficient of Restitution]] — the elasticity parameter $e$ that interpolates between elastic ($e = 1$) and perfectly inelastic ($e = 0$).
- **Application:** [[Two-Body Problem]] — momentum conservation reduces a 6-coordinate problem to a 3-coordinate one.
- **Cross-domain bridge:** [[Symmetry and Conservation Laws]] — Noether's theorem; how spatial translation gives momentum conservation.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{p}$ | `\mathbf{p}` | Linear momentum vector |
| $p$ | `p` | Magnitude / 1D scalar component |
| $\mathbf{p} = m\mathbf{v}$ | `\mathbf{p} = m\mathbf{v}` | Definition |
| $\mathbf{J}$ | `\mathbf{J}` | Impulse vector |
| $\Delta \mathbf{p}$ | `\Delta \mathbf{p}` | Change in momentum |
| $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$ | `\dfrac{d\mathbf{p}}{dt}` | Newton's 2nd law, general form |
| $\mathbf{J} = \int \mathbf{F}\, dt$ | `\int \mathbf{F}\, dt` | Impulse as the time integral of force |
| $u, v$ | `u, v` | Velocities before / after a collision |
| $u_1, u_2, v_1, v_2$ | `u_1, u_2` etc. | Two-body collision velocities |
| $e$ | `e` | Coefficient of restitution; $e = -(v_1 - v_2)/(u_1 - u_2)$ |
| $\sum_i \mathbf{p}_i$ | `\sum_i \mathbf{p}_i` | Total momentum of a system |
| $\gamma$ | `\gamma` | Lorentz factor $1/\sqrt{1 - v^2/c^2}$ in relativistic momentum |
