---
chinese: 匀加速运动公式 (yún jiā sù yùn dòng gōngshì)
prerequisites:
  - "[[Kinematics Calculus]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Vectors in Physics]]"
  - "[[Travel Graphs (Vocab)]]"
  - "[[Area Under a Graph (Vocab)]]"
leads_to:
  - "[[Projectile Motion]]"
  - "[[Free Fall]]"
  - "[[Choosing Effective Equations]]"
  - "[[Braking Systems]]"
  - "[[Work, Energy and Power]]"
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
  - syllabus/9709-4-2
  - syllabus/9702-2-1
  - syllabus/0625-1-2
  - syllabus/IB-Physics-A-1-1
  - syllabus/AP-Physics-1-1-1
  - syllabus/AP-Physics-1-1-2
  - syllabus/AP-Physics-C-Mech-1-1
  - syllabus/AP-Physics-C-Mech-1-2
  - type/deep
  - type/theorem
  - type/proof
  - notation/u-initial-velocity
  - notation/v-final-velocity
  - notation/SUVAT
  - misconception/suvat-applies-with-variable-a
  - misconception/v-squared-formula-as-independent
  - misconception/sign-convention-mid-problem
---

# SUVAT 匀加速运动公式

## Definition

**SUVAT** is the set of five formulae that govern motion in a straight line with **constant acceleration**. The name is a mnemonic for the five quantities involved:

| Letter | Meaning | 中文 | Units |
|---|---|---|---|
| **s** | displacement (signed) | 位移 (wèiyí) | m |
| **u** | initial velocity (at $t=0$) | 初速度 (chū sùdù) | m/s |
| **v** | final velocity (at time $t$) | 末速度 (mò sùdù) | m/s |
| **a** | (constant) acceleration | 加速度 (jiāsùdù) | m/s² |
| **t** | elapsed time | 时间 (shíjiān) | s |

Five quantities, four equations, one quantity always absent from each. **Every SUVAT problem is "given three of {s, u, v, a, t}, find the other two"** — the trick is recognising which equation has the four you care about and not the one you don't.

> [!warning] SUVAT requires *constant* $a$
> If acceleration varies with time (e.g. $a = kt^2$ from a non-uniform force) or with position (e.g. SHM, gravitational fall over large distances), **SUVAT fails** and you must use the calculus version: integrate $a(t)$ to get $v(t)$, integrate again for $s(t)$. See [[Kinematics Calculus]] for the general method.
>
> 9709 Paper 4 examines SUVAT *and* calculus kinematics — the question wording tells you which: "constant acceleration" or "starts from rest, accelerates uniformly" → SUVAT; "$v =$ polynomial in $t$" → calculus.

### 中文锚点

**SUVAT** 是英文力学里**匀加速直线运动 (yún jiā sù zhí xiàn yùn dòng)** 的五个公式的简称，对应五个字母：

- **s** = 位移 (signed; 不一定等于路程)
- **u** = 初速度
- **v** = 末速度
- **a** = 加速度 (must be **constant** for SUVAT to apply)
- **t** = 时间

考试关键：**给定三个量，求另外两个**。挑公式的窍门 — 选**含有那三个已知量、且含有所求量、但不含你不关心的第五个量**的那条公式。

---

## The Five Formulas

Listed in order of which variable is missing:

| # | Formula | Missing | When to use |
|---|---|---|---|
| 1 | $v = u + at$ | $s$ | given any 3 of u, v, a, t — find the 4th |
| 2 | $s = ut + \tfrac{1}{2} a t^2$ | $v$ | starting velocity known, want displacement at time $t$ |
| 3 | $s = vt - \tfrac{1}{2} a t^2$ | $u$ | final velocity known, displacement at time $t$ |
| 4 | $v^2 = u^2 + 2as$ | $t$ | distance/displacement given, time not — the **energy form** |
| 5 | $s = \tfrac{1}{2}(u + v)t$ | $a$ | average-velocity form — useful when $a$ unknown |

Equations 4 and 5 are derived by eliminating $t$ (or $a$) from the first two — they are *not* independent equations. Some textbooks list only the first two; Cambridge / A-Level lists all five for convenience.

### Where do they come from? — calculus in three lines

Constant acceleration means $a(t) = a$ for all $t$. Integrate:

$$v(t) = \int a \, dt + C_1 = at + C_1.$$

At $t=0$, $v(0) = u$, so $C_1 = u$ and $v = u + at$ ✓ (formula 1).

Integrate again:

$$s(t) = \int (u + at) \, dt + C_2 = ut + \tfrac{1}{2} a t^2 + C_2.$$

At $t=0$, $s(0) = 0$ (the standard convention), so $C_2 = 0$ and $s = ut + \tfrac{1}{2} a t^2$ ✓ (formula 2).

The other three follow by algebra alone. The "energy form" $v^2 = u^2 + 2as$ comes from squaring formula 1 and substituting formula 2 — and it really *is* a disguised energy statement: multiply through by $\tfrac{1}{2}m$ and you get $\tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2 = mas$, the work-energy theorem with $F = ma$ as the constant force.

> [!info] SUVAT is calculus in disguise
> Physics teaches SUVAT as five formulae to memorise. Calculus teaches them as *one fact*: "constant $a$, integrate twice, apply initial conditions." Once you know the calculus, the formulae are forced; you don't need to memorise them. (And once $a$ stops being constant — drag, oscillation, gravity at high altitude — the formulae *fail* and only the calculus survives.) See [[Kinematics Calculus]] for the calculus side.

---

## Picking the Right Formula — the decision tree

The trick that distinguishes a fast SUVAT solver: **before writing anything, list which 3 of {s, u, v, a, t} are given and circle which one you want.** That tells you which equation to pick — the one whose **missing variable is the fifth (the one you neither have nor want)**.

```
Given:    {s, u, v}    →  use formula 4    (missing t)
Given:    {s, u, t}    →  use formula 2    (missing v)  …or formula 5 if a is what you want
Given:    {s, v, t}    →  use formula 3    (missing u)
Given:    {u, v, a}    →  use formula 1    (missing s)
Given:    {u, v, t}    →  use formula 5    (missing a) …or formula 1 if a is what you want
Given:    {u, a, t}    →  use formula 2    (missing v)
Given:    {v, a, t}    →  use formula 3    (missing u)
Given:    {s, u, a}    →  use formula 4    (missing t / find v) …or formula 2 (find t)
…etc.
```

Spend 10 seconds on this *before* writing any equation. Most students who freeze on a SUVAT problem are skipping this step.

---

## Sign Conventions — pick once, stick to it

SUVAT is a *vector* statement in disguise. In 1D the vectors collapse to *signed* scalars, but the signs still matter:

- $s$, $u$, $v$, $a$ are **signed** quantities along a chosen positive direction.
- The most common convention for vertical motion: **upward = positive**. Then $g = -10$ m/s² (gravity pulls down, in the negative direction).
- Some textbooks invert it ("downward positive" for falling-body problems). Then $g = +10$ m/s².

> [!warning] Don't switch sign conventions mid-problem
> A particle thrown straight up has $v_0 = +U$, $a = -g$, and reaches the top with $v = 0$. Coming back down, $v$ goes *negative* (because it's now moving in the negative direction); the displacement $s$ ends up at $0$ when it returns to its starting height. **None of those signs change** — they're all consistent under a single "up = +" convention.
>
> A common error: "the ball is now falling, so I'll switch to down = positive." This works only if you re-state $u$, $v$, $a$, $s$ in the new convention from the *start* of the new phase. Mid-problem switches are a recipe for sign errors. Pick once.

---

## v–t Graphs — the geometric picture

SUVAT is exactly the *algebra of v-t graphs with straight-line segments*:

![[suvat-vt-graph-areas.svg|697]]

For a constant-acceleration phase from $u$ at $t=0$ to $v$ at time $t$:
- The v-t graph is a straight line from $(0, u)$ to $(t, v)$.
- **Gradient** = $\dfrac{v - u}{t} = a$ ← this is formula 1.
- **Area under the graph** = trapezoid area = $\tfrac{1}{2}(u + v) \cdot t$ ← this is formula 5.

Multi-segment problems (constant accel → constant velocity → constant decel — exactly the J22 Q1 question on the recent paper) are stitched together by reading three trapezoid areas off the v-t graph and summing them. Cambridge questions often ask for the v-t graph *and* a numerical answer; sketching the graph first usually makes the algebra obvious.

---

## Vertical Motion Under Gravity — the most common SUVAT setup

A body in free fall (or projected) near Earth's surface has $a = g$ pointing downward. Numerically:

- **9709 Paper 4:** $g = 10$ m/s² (clean arithmetic).
- **9702 / 0625 Extended:** $g = 9.81$ m/s² (data-sheet value).

Three canonical setups, with sign convention "**up = positive**":

| Setup | Initial conditions | What changes |
|---|---|---|
| Dropped from rest | $u = 0$, $a = -g$ | $v$ becomes increasingly negative; $s$ becomes increasingly negative below release |
| Thrown upward | $u = +U$, $a = -g$ | $v$ decreases through 0 (apex), then negative; $s$ rises, peaks, falls |
| Thrown downward | $u = -U$, $a = -g$ | both $u$ and $a$ negative; speed increases monotonically |

> [!info] At the apex of upward throw, $v = 0$ but $a \neq 0$
> The instantaneous velocity at the highest point is zero — the body has stopped going up but hasn't yet started coming down. The acceleration, however, remains $-g$: gravity is still pulling. *This is the moment students misread most often.* "$v = 0$" doesn't mean "the body is in equilibrium" — it just means the velocity is instantaneously crossing zero on its way from positive to negative.

---

## Projectile Motion — 2D as Two Independent SUVATs

> [!info] Scope note
> This section is the *scoped summary*; the full treatment — the standard trio derived with its small print, the trajectory equation, real Further-Maths questions, the misconception set — is [[Projectile Motion]]. Projectiles are examined on **9702 §2.1**, **9231 §3.1**, **IAL M2 / OxAQA M2**, **IB Physics A.1.2** and **AP Physics 1/C**. They are **not in 9709 P4** — 9709 examines 1D SUVAT only. Skip this section if you're sitting only 9709.

A body launched at angle $\theta$ to the horizontal with speed $U$ has its motion *split into two independent components*:

- **Horizontal:** $u_x = U \cos\theta$, $a_x = 0$ (no horizontal force, ignoring air resistance). Pure constant-velocity motion. $x(t) = U\cos\theta \cdot t$.
- **Vertical:** $u_y = U \sin\theta$, $a_y = -g$ (gravity only). Standard SUVAT. $y(t) = U\sin\theta \cdot t - \tfrac{1}{2} g t^2$.

The two components evolve **independently** — which is the deep insight of Galileo's that made projectile motion solvable. Eliminating $t$ between the two gives the trajectory $y(x)$, a parabola.

Three quick standard results follow:

- **Time to apex:** $t_\text{apex} = \dfrac{U\sin\theta}{g}$ (from $v_y = 0$).
- **Maximum height:** $H = \dfrac{U^2 \sin^2\theta}{2g}$.
- **Range** (back to launch height): $R = \dfrac{U^2 \sin 2\theta}{g}$. Maximum range at $\theta = 45°$.

---

## Worked Examples — from recent Cambridge papers

### Example 1 — Three-phase motion (J22 P41 Q1, 6 marks)

A car starts from rest and moves in a straight line with constant acceleration for a distance of 200 m, reaching a speed of 25 m/s. The car then travels at this speed for 400 m, before decelerating uniformly to rest over a period of 5 s.

(a) Find the time for which the car is accelerating.
(b) Sketch the v-t graph.
(c) Find the average speed.

**(a) Phase 1: accelerating.** Given $u = 0$, $v = 25$, $s = 200$. We want $t$. Missing variable is $a$ — formula 5: $s = \tfrac{1}{2}(u + v) t$.
$$200 = \tfrac{1}{2}(0 + 25) t \;\Rightarrow\; t = \boxed{16 \text{ s}}.$$

**(b) v-t graph:** straight line from $(0, 0)$ to $(16, 25)$, then horizontal at $25$ until $t = 16 + 16 = 32$ s (since at 25 m/s for 400 m takes 16 s), then straight line down to $(37, 0)$.

**(c) Average speed = total distance / total time** = $\dfrac{200 + 400 + 62.5}{37} = \dfrac{662.5}{37} \approx \boxed{17.9 \text{ m/s}}$.
(Final-phase distance = $\tfrac{1}{2}(25 + 0) \times 5 = 62.5$ m using formula 5 again.)

> Notice the strategy: read off which 3 of {s, u, v, a, t} are given for each phase, pick the formula whose missing variable you don't care about, no algebra wasted.

### Example 2 — Vertical projection (M24 P42 Q2, 4 marks)

A particle is projected vertically upwards from horizontal ground. The speed of the particle 2 seconds after projection is 5 m/s and it is travelling downwards. (a) Find the speed of projection. (b) Find the distance travelled between the two times at which the speed is 10 m/s.

Sign convention: **up = positive**. So 2 s in, the velocity is $v = -5$ m/s (downward). $g$ acts downward, so $a = -10$ m/s².

**(a) Find $u$.** Given $v = -5$, $a = -10$, $t = 2$. Want $u$. Missing $s$ — formula 1: $v = u + at$.
$$-5 = u + (-10)(2) \;\Rightarrow\; u = \boxed{15 \text{ m/s upward}}.$$

**(b) Distance between speed = 10 m/s twice.** The speed is 10 m/s once on the way up (with $v = +10$) and once on the way down (with $v = -10$). The displacement *between these two events* tells us the distance travelled (the body is above the lower-speed-up height the whole time, so distance = displacement here).

Using formula 4 between $v = +10$ (initial) and $v = -10$ (final), with $a = -10$:
$$(-10)^2 = (10)^2 + 2(-10) s \;\Rightarrow\; 0 = -20 s \;\Rightarrow\; s = 0.$$

So the *displacement* between the two events is zero (it returns to the same height). The *distance travelled* is twice the rise from the moment $v = +10$ to the apex:
$$0^2 = 10^2 + 2(-10) h_{\text{rise}} \;\Rightarrow\; h_{\text{rise}} = 5 \text{ m}.$$
Total distance = $\boxed{10 \text{ m}}$.

This question is a classic test of the **distance vs displacement** distinction (covered in [[Kinematics Calculus]] §"The Three Graphs"). The displacement is 0, but the body actually travelled 10 m in total.

### Example 3 — Connected SUVAT and Newton's 2nd (M24 P42 Q7, abbreviated)

Particle P released from rest at A on a smooth slope of length 0.75 m at angle $\theta$ where $\sin\theta = 0.6$. Verify P reaches B with speed 3 m/s after 0.5 s.

**Step 1 — find acceleration (N2 on the slope):** $a = g\sin\theta = 10 \times 0.6 = 6$ m/s² down the slope. (See [[Newton's Laws of Motion]] Example 2 for this derivation.)

**Step 2 — apply SUVAT:** $u = 0$, $a = 6$, $s = 0.75$. Find $v$ and $t$.
$$v^2 = 0 + 2(6)(0.75) = 9 \;\Rightarrow\; v = 3 \text{ m/s} \;\;\checkmark$$
$$v = u + at \;\Rightarrow\; 3 = 0 + 6t \;\Rightarrow\; t = 0.5 \text{ s} \;\;\checkmark$$

This is the canonical **two-framework chain**: N2 gives the constant acceleration, SUVAT then gives the kinematics. Cambridge questions do this all the time — see [[Choosing Effective Equations]] for the general pattern.

---

## Common Misconceptions

### 1. "SUVAT works whenever there's an acceleration"

False. SUVAT requires **constant** acceleration. As soon as $a$ varies — drag, oscillation, gravity over a large height range, a body experiencing a varying force — SUVAT fails and only [[Kinematics Calculus]] works.

### 2. "$v^2 = u^2 + 2as$ is a separate physical law"

It's not — it's formula 1 squared with formula 2 substituted, then $t$ eliminated. *Or* it's the work-energy theorem in disguise (multiply by $\tfrac{1}{2}m$). It's *useful* when time is missing from the question; it's not *new physics*.

### 3. "Switching sign convention mid-problem is fine"

Avoid it. A particle thrown up has $u = +U$, $a = -g$; coming back down it still has $a = -g$ in the *same* convention. Re-defining "down = positive" mid-problem is the most common source of sign errors on M1 papers.

### 4. "At the apex of upward throw, the ball is in equilibrium"

No — its *velocity* is instantaneously zero, but the *acceleration* is still $-g$. (If gravity stopped at the apex, the ball would float there forever.) "Velocity zero at one instant" $\neq$ "in equilibrium."

### 5. "I can use SUVAT on a projectile by treating the speed as the velocity"

Only one component is constant-acceleration (vertical, with $a = -g$). The other (horizontal, with $a = 0$) is constant velocity. *Each component is its own SUVAT.* You don't run SUVAT on the resultant *speed* — that combines both axes and the acceleration of the resultant isn't constant in direction.

---

## Exam Notes

### Cambridge 9709 Paper 4 (Mechanics, AS) — §4.2

The five formulae are *listed but not given* on the formula sheet for Paper 4 — students must memorise them or derive them from the calculus.

**In scope:** 1D motion only; SUVAT for constant $a$; v-t and s-t graph reading; calculus kinematics for non-constant $a$.

**Not in scope:** projectile motion, 2D motion, vector forms.

> [!info] On the data sheet
> Paper 4 has no data sheet of its own. SUVAT formulae must be written from memory.

### Cambridge 9702 (A-Level Physics) — §2.1

Includes: SUVAT for 1D, projectile motion in 2D (as superposition), free-fall experiment to determine $g$, and the v-t graph relations explicitly tested.

> [!info] On the 9702 data sheet
> The data sheet **gives** $s = ut + \tfrac{1}{2}at^2$ and $v^2 = u^2 + 2as$. The other three SUVAT formulae are not given — but they're easily derived from these two plus formula 1.

### Cambridge 0625 (IGCSE Physics) — §1.2

**Core:** speed, distance, time; v-t graph reading; deceleration as a word.
**Extended:** SUVAT formulae (often only $v = u + at$ and $s = ut + \tfrac{1}{2} a t^2$); free-fall acceleration; very simple problems.

### A-Level Mathematics Mechanics, IB AA, AP Physics 1/C: Mechanics

A-Level Mechanics 1 covers 1D SUVAT and projectile motion in 2D as standard. IB AA Mechanics same. AP Physics 1 includes projectile motion; AP Physics C: Mechanics adds the calculus form (which is [[Kinematics Calculus]] territory).

---

## Why SUVAT Matters — College and Beyond

- **Civil engineering** — every elevator, conveyor belt, and railway timetable uses SUVAT for the constant-acceleration phases (start, run, stop). Train braking distances and runway-length calculations are straight SUVAT.
- **Sports analytics** — sprinters in the 100m have a constant-acceleration phase (~0–4s) followed by approximately constant velocity. Coaches use SUVAT to model the acceleration phase and identify where time is being lost.
- **Ballistics and motorsport** — projectile SUVAT models everything from artillery to long jumpers to cricket bowling. Range, max height, and time of flight are SUVAT outputs given launch conditions.
- **Robotics and motion planning** — robot arms move under "trapezoidal velocity profiles" (constant accel up, constant velocity, constant decel down) — exactly the J22 Q1 setup, but executed by a controller. Path planning algorithms use SUVAT to compute reach and timing.
- **The bridge to calculus and beyond** — once you let $a(t)$ be a function of time (rocket fuel burning, gravitational fall over astronomical distances, drag forces), SUVAT generalises to the ODE $\ddot s = a(s, \dot s, t)$ — the master equation of classical mechanics. SUVAT is the trivial case of that ODE; everything else is the same idea with calculus.

---

## Connections

- **Prerequisite:** [[Kinematics Calculus]] — SUVAT is the constant-$a$ special case of the calculus framework.
- **Prerequisite:** [[Newton's Laws of Motion]] — N2 ($F = ma$) provides the constant acceleration that SUVAT then turns into kinematics.
- **Prerequisite:** [[Travel Graphs (Vocab)]], [[Area Under a Graph (Vocab)]] — IGCSE-level v-t graph reading; SUVAT formalises that algebra.
- **Application:** [[Projectile Motion]] — 2D motion as the superposition of two independent SUVAT axes.
- **Application:** [[Free Fall]] — the canonical vertical-SUVAT setup.
- **Application:** [[Choosing Effective Equations]] — SUVAT is one of the major frameworks the M1 problem-recognition layer has to identify; a student who reads "constant acceleration" and immediately picks the right SUVAT formula gains real time on exam day.
- **Cross-domain bridge:** the trapezoidal velocity profile (constant accel → constant v → constant decel) is the canonical motion plan in robotics; SUVAT is the algebra that programs robots' joint motors.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $u$ | `u` | Initial velocity |
| $v$ | `v` | Final velocity (or velocity at time $t$) |
| $s$ | `s` | Displacement (signed) |
| $a$ | `a` | Constant acceleration |
| $t$ | `t` | Elapsed time |
| $v = u + at$ | `v = u + at` | SUVAT 1 — missing $s$ |
| $s = ut + \tfrac{1}{2} a t^2$ | `s = ut + \tfrac{1}{2} a t^2` | SUVAT 2 — missing $v$ |
| $s = vt - \tfrac{1}{2} a t^2$ | `s = vt - \tfrac{1}{2} a t^2` | SUVAT 3 — missing $u$ |
| $v^2 = u^2 + 2as$ | `v^2 = u^2 + 2as` | SUVAT 4 — missing $t$; energy form |
| $s = \tfrac{1}{2}(u + v) t$ | `s = \tfrac{1}{2}(u + v) t` | SUVAT 5 — missing $a$; average-velocity form |
| $g$ | `g` | $10$ m/s² (9709) or $9.81$ m/s² (9702) |
| $\theta$ | `\theta` | Launch angle (projectile) |
