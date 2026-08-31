---
chinese: 牛顿运动定律 (Niúdùn yùndòng dìnglǜ)
prerequisites:
  - "[[Vectors]]"
  - "[[Vectors in Physics]]"
  - "[[Kinematics Calculus]]"
  - "[[Differentiation]]"
  - "[[Travel Graphs (Vocab)]]"
leads_to:
  - "[[Equilibrium]]"
  - "[[Friction (Vocab)]]"
  - "[[Linear Momentum]]"
  - "[[Work, Energy and Power]]"
  - "[[Connected Particles]]"
  - "[[Inclined Plane Motion]]"
  - "[[Inertia and Bootstrapping]]"
  - "[[Choosing Effective Equations]]"
  - "[[Torque]]"
  - "[[Laws and Theorems]]"
  - "[[Stories/The 1919 Eclipse]]"
  - "[[Stories/Aristotle to Apollo]]"
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
  - syllabus/9709-4-4
  - syllabus/9702-3-1
  - syllabus/0625-1-3
  - syllabus/0625-1-5
  - syllabus/IB-Physics-A-2-1
  - syllabus/AP-Physics-1-2-1
  - syllabus/AP-Physics-1-2-2
  - syllabus/AP-Physics-1-2-3
  - syllabus/AP-Physics-1-2-4
  - syllabus/AP-Physics-1-2-5
  - syllabus/AP-Physics-1-2-6
  - syllabus/AP-Physics-C-Mech-2-1
  - syllabus/AP-Physics-C-Mech-2-2
  - syllabus/AP-Physics-C-Mech-2-3
  - syllabus/AP-Physics-C-Mech-2-4
  - syllabus/AP-Physics-C-Mech-2-5
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/F-equals-ma
  - notation/dp-dt
  - notation/Newton-N
  - notation/dot-derivative
  - misconception/action-reaction-on-same-body
  - misconception/no-force-no-motion
  - misconception/equal-and-opposite-means-equilibrium
  - misconception/inertia-is-mass
---

# Newton's Laws of Motion 牛顿运动定律

## Definition

Newton's three laws of motion are the **operating manual of classical mechanics**. They tell you what motion is, what changes it, and how forces come in pairs. Stated together they take three short sentences:

> [!quote] Newton's Laws of Motion (Principia, 1687)
> **First Law.** A body remains at rest, or in uniform motion in a straight line, unless acted on by a resultant force.
>
> **Second Law.** The resultant force on a body equals the rate of change of its momentum: $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$. For a body of constant mass, this becomes $\mathbf{F} = m\mathbf{a}$.
>
> **Third Law.** When body A exerts a force on body B, body B exerts an equal-magnitude, opposite-direction force on A. *These two forces act on different bodies.*

Three laws, three different jobs:

- **N1** says what motion looks like *when nothing is pushing*. (It is *not* obvious — humanity got it wrong for two thousand years.)
- **N2** is the *operational definition of force* — force is whatever changes momentum.
- **N3** says forces always come in pairs that act on *different bodies*. The most-misunderstood law.

### 中文锚点

**牛顿运动定律 (Niúdùn yùndòng dìnglǜ)** = the three laws governing how bodies move.

| 定律 | English | 一句话总结 |
|---|---|---|
| 牛顿第一定律 (惯性定律) | First Law (Law of Inertia) | 没有合力 → 速度不变 (静止或匀速直线运动) |
| 牛顿第二定律 | Second Law | $\mathbf{F} = m\mathbf{a}$；合力 = 动量的变化率 |
| 牛顿第三定律 | Third Law | 作用力与反作用力大小相等、方向相反、**作用在不同物体上** |

中文物理已经学过这三条定律 — vault 的工作是把物理直觉翻译成 Cambridge / A-Level 的英语考题语言，并解决两个最常见的英语理解陷阱：N3 不是 equilibrium，inertia 不等于 mass。

---

## Why N1 was Revolutionary — Aristotle vs Galileo vs Newton

![[galileo-pisa-cannonballs.png]]

*Galileo's apocryphal Tower of Pisa demonstration — two cannonballs of different mass, dropped together, hit the ground simultaneously. The probable myth carries the right physics: with air resistance negligible, mass cancels out of the falling-body equation, and every object accelerates downward at the same $g$. The clean version of this experiment was performed on the Moon by Apollo 15's David Scott in 1971 with a hammer and a feather; the recording is on YouTube.*

For two thousand years before Newton, physics ran on Aristotle's intuition: *to keep something moving, you have to keep pushing it.* If a cart rolls and you stop pushing, the cart stops. Obvious. Aristotle wrote this around 350 BC and it became the consensus view in European universities until the 1600s.

It is also completely wrong.

The reason it *looks* right is that on Earth, friction is everywhere. The cart "needs constant pushing" only because friction keeps subtracting momentum. Remove the friction — say, send the cart out into deep space — and Aristotle's rule fails immediately: the cart coasts forever in a straight line, no push needed.

> [!info] Galileo's thought experiment (c. 1638)
> Galileo imagined a ball rolling down one ramp and up another. With low friction the ball nearly returns to its starting height. Make the second ramp shallower — it rolls farther, still reaching the same height. Make it horizontal — by the same logic, it should keep rolling *forever*, since it has no height to climb back to.
>
> Galileo couldn't quite let go of "circular natural motion" (he thought planets coast in circles, not straight lines). Newton finished the argument: **straight lines, not circles, are the natural state**, and curving requires a force.

![[newton-galileo-ramps.svg|697]]

This is the conceptual leap N1 makes. Bodies don't *want* to stop. They want to keep doing exactly what they're doing — moving in a straight line at constant speed (or sitting still, which is the same thing with $v = 0$). It takes a *force* to deviate. Friction, gravity, tension — all forces — are what make the universe *look* like Aristotle was right when he wasn't.

The technical name for "what bodies want to keep doing" is **inertia** (惯性, guànxìng). N1 is also called the **Law of Inertia** for that reason.

> [!warning] Inertia is not mass — and it's not momentum either
> Three closely-related ideas live in this neighbourhood. They are not the same.
>
> - **Inertia** is the *property* that bodies resist changes to their motion. It's a quality, not a number.
> - **Mass** is the *quantitative measure* of inertia — the bigger $m$ is, the harder it is to change the body's velocity. (This is the operational definition; see N2 below.)
> - **Momentum** $\mathbf{p} = m\mathbf{v}$ is the *current motion bookkeeping* — how much "moving" the body is doing right now.
>
> "A train has more inertia than a tennis ball" really means "a train has more mass." A train at rest still has tons of inertia — but zero momentum. A loose use of "inertia" for "momentum" (as in "the inertia of the markets") is metaphor, not physics.

> [!tip] Beyond physics — N1 in everyday life
> "Bodies want to keep doing exactly what they're doing" describes humans almost as well as it describes blocks on tables. Starting a new habit is hard because nothing is moving yet — you're fighting *static friction*, the version of friction that resists motion *from rest* and that turns out to be larger than the friction once you're moving (the "first day is the hardest" effect). Once you've taken the first step, kinetic-friction physics takes over and the daily activation cost is much smaller. The whole engineering trick of "set up the right environment, then let momentum carry you" is N1 plus a friction model, applied to a brain.
>
> This is its own meta-card territory — see [[Inertia and Bootstrapping]] for the cross-domain treatment that pulls in static vs kinetic friction (physics), activation energy (chemistry), executive function and habit research (psychology), and the cold-start problem (software). The vault's job is to point out that N1 is the *physical* statement of why setting up the working environment matters more than willpower.

---

## The Second Law — F = ma is the *Definition* of Force

This is where everything physical happens. N1 set up the picture; N2 quantifies it.

State it three ways, ascending in generality:

$$
\boxed{\;\mathbf{F}_{\text{net}} \;=\; m\mathbf{a} \;=\; m\dfrac{d\mathbf{v}}{dt} \;=\; \dfrac{d\mathbf{p}}{dt}\;}
$$

where $\mathbf{p} = m\mathbf{v}$ is the body's **linear momentum** (动量, dòngliàng) — mass times velocity, the bookkeeping for "how much motion is happening." A separate card, [[Linear Momentum]], gives momentum its full treatment (definition, conservation, collisions); this card uses it as the operational handle that makes the most general form of N2 readable.

The **most general** form is $\mathbf{F} = d\mathbf{p}/dt$. For a body whose mass is constant (most exam scenarios), $\mathbf{p} = m\mathbf{v}$ and $d\mathbf{p}/dt = m \, d\mathbf{v}/dt = m\mathbf{a}$. The constant-mass corollary $\mathbf{F} = m\mathbf{a}$ is the form you'll use most days.

> [!info] Are F = ma and F = dp/dt really the same thing? — a unit-algebra check
> Tracking units through both forms shows they produce the same SI unit (the newton). This is the [[Histograms#Why "Area = Frequency" works — Unit Algebra (Dimensional Analysis 量纲分析)|unit-algebra technique]] used as a sanity check, the same one statistics uses to verify "area under a histogram = frequency."
>
> | Form | Unit algebra | Result |
> |---|---|---|
> | $\mathbf{F} = m\mathbf{a}$ | $\text{kg} \cdot \text{m/s}^2$ | $\text{N}$ |
> | $\mathbf{F} = d\mathbf{p}/dt$ | $\dfrac{\text{kg} \cdot \text{m/s}}{\text{s}} = \text{kg} \cdot \text{m/s}^2$ | $\text{N}$ |
>
> Both produce kg·m/s², which is *defined* to be the newton. The unit-check doesn't *prove* the two forms are equivalent — that needs the product-rule argument (when $m$ is constant, $d(mv)/dt = m \cdot dv/dt$). But it confirms they live in the same dimensional universe, and that's the first thing to verify whenever you suspect a formula is wrong. See [[Physical Quantities and Units]] §"Dimensional homogeneity — the central principle" for the systematic technique.

> [!info] The deeper claim — F = ma is how "force" is *defined*
> Read $\mathbf{F} = m\mathbf{a}$ slowly. There are no instruments measuring "force" on the left and "mass × acceleration" on the right. Force is *defined* by the right-hand side: the force on a body **is** what changes its momentum at the rate $m\mathbf{a}$. If a body is not accelerating, the *resultant* force on it is zero — by definition.
>
> This is what makes Newtonian mechanics a *theory* and not a tautology. The bet Newton placed in 1687 was: *for every observed motion in the universe, there is a force law $\mathbf{F}(\text{position, velocity, time, charges, masses})$ such that $\mathbf{F} = m\mathbf{a}$ predicts the motion correctly.* He spent the rest of *Principia* showing it works for gravity. Subsequent physicists showed it works for tension, friction, springs, electromagnetism (with one upgrade), and most of everyday experience. It eventually breaks for very small things (quantum mechanics) and very fast things (special relativity), but for a block on an incline, it's exact.

### Units forced by F = ma

The SI unit of force is the **newton (N)**. It's defined by $F = ma$ itself:

$$1 \text{ N} \;=\; 1 \text{ kg} \cdot 1 \text{ m/s}^2$$

A force of one newton is "what it takes to accelerate a one-kilogram mass at one metre per second squared." Roughly the weight of a small apple.

### Weight is a force: W = mg

A body of mass $m$ near Earth's surface feels a gravitational force $W = mg$ pointing **downward**. Numerically:

- Cambridge **9709** uses $g = 10$ m/s² for numerical convenience.
- Cambridge **9702** uses $g = 9.81$ m/s² (the data-sheet value).
- Cambridge **0625** uses either, problem-dependent (usually 10).

A 5 kg block has weight $W = 5 \times 10 = 50$ N (9709 convention) or $5 \times 9.81 = 49.05$ N (9702 convention). **Always check the paper** — using the wrong $g$ wastes marks even when the method is right.

> [!info] Mass vs weight — vocabulary trap
> *Mass* (质量) is in kilograms and is the same on Earth, the Moon, and in deep space. *Weight* (重量) is the **force** of gravity in newtons and changes with location: a 60 kg person weighs $\sim 600$ N on Earth and $\sim 100$ N on the Moon. English exam questions are strict about this; Chinese physics is sometimes looser. Do not say "the block weighs 5 kg" in an English exam — write "the block has mass 5 kg" or "the block weighs 50 N."

---

## The Third Law — and the Misconception Slot

Stated formally:

> When body A exerts a force $\mathbf{F}_{AB}$ on body B, body B exerts a force $\mathbf{F}_{BA} = -\mathbf{F}_{AB}$ on A.

The two forces are **equal in magnitude, opposite in direction, and act on different bodies**. The "different bodies" clause is the entire point of N3 and the source of every misunderstanding around it.

### The Misconception — "If forces are equal and opposite, doesn't everything cancel?"

The most common student error: *"You said action equals reaction. So when I push the desk, the desk pushes back equally. They cancel. So no net force. So nothing should move. But my hand still hurts. What gives?"*

The fall-back-on-principle answer: **the two forces in an action-reaction pair act on different bodies, so they cannot cancel each other in any single body's equation of motion.**

Take the example apart:

- Force on the desk: a push from the hand. *This is the only N3 partner relevant to the desk's motion.*
- Force on the hand: a push from the desk (Newton's 3rd law partner of the above). *This is the only N3 partner relevant to the hand's motion.*

The desk doesn't move because *other* forces on the desk (friction with the floor, the desk's own weight, the floor's normal force) cancel the push. The hand hurts because the desk really is pushing back on it.

> [!warning] N3 is not the same as equilibrium
> Equilibrium ($\Sigma \mathbf{F} = \mathbf{0}$) is a statement about *one* body: the *net* force on that body is zero, so its acceleration is zero. The forces in the sum all act on the same object.
>
> N3 is a statement about *two* bodies: when one pushes the other, the other pushes back equally. The two forces never appear in the same body's equation. **They cannot cancel each other.**
>
> If you ever see yourself writing $\mathbf{F}_{AB} + \mathbf{F}_{BA} = \mathbf{0}$ as part of an equilibrium equation for a single body — stop. That's the wrong law.

### Identifying N3 pairs — the "swap-the-nouns" test

Every action-reaction pair has the same form. To check if two forces are an N3 pair, swap the subject and object:

- "Earth pulls the apple down with force $W$" ↔ "Apple pulls Earth up with force $W$." ✅ N3 pair. (Yes, the apple really does pull Earth toward it; Earth's mass is so huge the resulting acceleration is invisible.)
- "Earth pulls the apple down with force $W$" ↔ "The table pushes the apple up with force $N$." ❌ *Not* an N3 pair. Both forces act on the apple. The fact that they're equal in magnitude (because the apple is in equilibrium) is N1, not N3.

The N3 partner of "Earth pulls apple down" is **not** "Table pushes apple up." It's **Apple pulls Earth up** — the partner force never lives in the apple's free-body diagram.

---

## Free-Body Diagrams — the Practice of N's Laws

A **free-body diagram (FBD)** isolates one body and draws every force *on that body*, with no internal stress arrows and no forces *from* that body. It is the engineering tool that makes N1, N2, N3 actually solvable on an exam.

The FBD recipe, four steps:

1. **Pick one body.** Just one. Draw a dot or a small box for it.
2. **Identify every force on that body** — gravity (weight $mg$), normal $N$, friction $f$, tension $T$ in any rope attached, applied push or pull. Skip anything inertial ("centrifugal force" is not a force in N1's frame); skip anything internal.
3. **Draw the arrows.** Tail at the body, length roughly proportional to magnitude (for sketches), labelled by symbol.
4. **Resolve into convenient axes** — usually horizontal/vertical, but on an inclined plane use *along the slope* and *perpendicular to the slope*. Apply N2 component-wise: $\Sigma F_x = ma_x$, $\Sigma F_y = ma_y$.

> [!tip] 9709 P4 convention
> The 9709 syllabus says: "Vector notation will not be used in the question papers." You'll resolve forces into perpendicular components by hand, never write a boldface $\mathbf{F}$. The FBD is exactly the technique that makes this work — pick axes, decompose every arrow into the chosen axes, write a scalar N2 equation per axis, solve.

For 9702, vector notation can appear; the technique is identical, the typography is different.

![[newton-fbd-incline-block.svg|697]]

*Figure: free-body diagram of a block on a frictionless inclined plane. Three forces — weight $mg$ vertically down, normal $N$ perpendicular to the slope, no friction. Resolved along (downhill) and perpendicular (away from slope) axes, $\Sigma F_\parallel = mg\sin\theta$ gives $a = g\sin\theta$ down the slope; $\Sigma F_\perp = N - mg\cos\theta = 0$ gives $N = mg\cos\theta$. The block accelerates down the slope at a rate that depends only on the angle, not on the mass — Galileo's discovery, derived in two lines.*

---

## Worked Examples — The Four Canonical 9709 P4 Scenarios

These four problem types account for almost every Paper 4 §4.4 question. Master the FBD and the rest is bookkeeping.

### Example 1 — Horizontal motion with friction

![[newton-fbd-horizontal-friction.svg|697]]

A 4 kg block sits on a horizontal surface. A horizontal force of 30 N is applied. The friction between block and surface is 10 N (constant). Find the acceleration. Use $g = 10$ m/s².

**FBD on the block** (one body, four forces):

- Weight $W = mg = 40$ N down.
- Normal $N$ up. Equilibrium vertically: $N = 40$ N.
- Applied force 30 N right.
- Friction 10 N left (always opposes motion).

**N2 horizontally:**

$$\Sigma F_x = ma_x \;\Rightarrow\; 30 - 10 = 4a \;\Rightarrow\; a = 5 \text{ m/s}^2 \text{ to the right.}$$

### Example 2 — Inclined plane (the workhorse)

*(Reuse the schematic FBD from the [[Newton's Laws of Motion#Free-Body Diagrams — the Practice of N's Laws|FBD section]] above — same picture, with $\theta = 30°$ and $m = 5$ kg.)*

A 5 kg block is released from rest on a smooth slope inclined at $30°$ to the horizontal. Find the acceleration down the slope. Use $g = 10$ m/s².

Resolve weight $mg = 50$ N into components:

- Component **along** (down the slope): $mg \sin 30° = 50 \times 0.5 = 25$ N.
- Component **perpendicular** (into the slope): $mg \cos 30° = 50 \times \tfrac{\sqrt{3}}{2} \approx 43.3$ N.

The perpendicular component is balanced by $N$ (slope is rigid). Along the slope, only the parallel weight component remains:

$$\Sigma F_\parallel = ma_\parallel \;\Rightarrow\; mg\sin\theta = ma \;\Rightarrow\; a = g\sin\theta = 5 \text{ m/s}^2 \text{ down the slope.}$$

Notice: the mass *cancels*. Every block on a smooth slope accelerates at $g\sin\theta$ regardless of mass — Galileo's discovery, falling out of N2 in one step.

### Example 3 — Connected particles over a smooth pulley

![[newton-fbd-pulley.svg|697]]

Two masses, $m_1 = 3$ kg and $m_2 = 2$ kg, are connected by a light inextensible string over a smooth peg. The string is taut. Find the acceleration of the system and the tension. Use $g = 10$ m/s².

The "light inextensible string" assumption gives us two crucial pieces:
- **Same tension** $T$ throughout (light = massless, so no net force is needed *along* the string).
- **Same speed and acceleration magnitude** for both masses (inextensible = constant length).

The 3 kg mass falls; the 2 kg mass rises. Take "downward for $m_1$, upward for $m_2$" as the positive direction (consistent around the pulley).

**FBD on $m_1$:** weight $30$ N down (positive), tension $T$ up (negative). N2:
$$30 - T = 3a.$$

**FBD on $m_2$:** weight $20$ N down (negative), tension $T$ up (positive). N2:
$$T - 20 = 2a.$$

Add the two equations:
$$30 - 20 = (3 + 2)a \;\Rightarrow\; a = 2 \text{ m/s}^2.$$

Substitute back: $T = 20 + 2(2) = 24$ N.

> [!tip] The "add the equations" trick
> When you add the two N2 equations, the tension cancels — because tension acts on $m_1$ in one direction and on $m_2$ in the opposite direction. What remains is a single equation: *(net external force on the system) = (total mass) × a*. You can write it down directly: $(m_1 - m_2)g = (m_1 + m_2)a$. It's a real labour-saver for connected systems and follows from N3 (the rope's pull on $m_1$ and on $m_2$ are an N3 pair across the pulley).

### Example 4 — Car towing a trailer

![[newton-fbd-towing.svg|697]]

A car of mass 1200 kg tows a trailer of mass 400 kg via a rigid tow-bar. The car engine produces a forward driving force of 2400 N. Air resistance on the car is 400 N; on the trailer, 200 N. Find the acceleration and the tension in the tow-bar.

Treat the system first to get $a$. External forces on the (car + trailer):
$$\Sigma F_{\text{ext}} = 2400 - 400 - 200 = 1800 \text{ N}, \qquad m_{\text{total}} = 1600 \text{ kg}.$$
$$a = \dfrac{1800}{1600} = 1.125 \text{ m/s}^2.$$

To get $T$, isolate the trailer (its FBD has only $T$ pulling forward and 200 N air resistance pulling backward):
$$T - 200 = 400 \times 1.125 \;\Rightarrow\; T = 200 + 450 = 650 \text{ N.}$$

The tow-bar is stretched at 650 N. (Cross-check: isolate the car. $2400 - 400 - T = 1200 \times 1.125 \;\Rightarrow\; T = 2000 - 1350 = 650$ N. ✓)

---

## Common Misconceptions

### 1. "No force, no motion" (Aristotle's ghost)

The most stubborn misconception, addressed at length above. *No force* means *no acceleration*, not *no motion*. A puck sliding on ice keeps sliding because the friction is small — N1 is asymptotically right.

### 2. "Action and reaction cancel"

Addressed in the N3 section. They act on different bodies. They **never** cancel.

### 3. "Heavy objects fall faster"

A direct consequence of misreading N2. On a smooth slope or in free fall, $a = g$ (or $g\sin\theta$) — independent of mass, because the gravitational force *and* the inertia both scale with $m$, and they cancel. Galileo's Pisa experiment (probably apocryphal but the physics is real) and the Apollo 15 hammer-and-feather demo on the Moon both verify it.

The reason a feather falls slowly *on Earth* is air resistance. In a vacuum, hammer and feather hit the ground simultaneously.

### 4. "Inertia is mass"

Mass is the **quantitative measure** of inertia (the bigger $m$, the more force needed to produce a given $a$). Inertia itself is the *property* — the tendency to keep doing what you're doing. Don't equate them.

### 5. "Tension differs at the two ends of a rope"

Only when the rope has mass. The standard exam phrase **light inextensible string** means: massless (so tension is the same everywhere along the rope) and unstretchable (so connected particles have the same speed and acceleration magnitude). Both assumptions matter; both are stated for a reason.

---

## Exam Notes

### Cambridge 9709 Paper 4 (Mechanics) — §4.4

The four examples above cover almost everything Paper 4 §4.4 asks for:
- $F = ma$ on a horizontal surface, with friction
- Motion on an inclined plane (smooth or rough — friction added later from §4.1)
- Connected particles over a smooth peg or pulley
- Connected particles via tow-bar or rope (car / trailer)

Use $g = 10$ m/s². Vector notation will not appear — use scalar resolved-component arithmetic. Air resistance is included only when explicitly mentioned.

> [!info] On the 9709 data sheet
> Paper 4 has no formula sheet of its own — every result must come from $F = ma$, $W = mg$, plus the SUVAT formulas and energy formulas covered in the relevant rows. *No equation in this card is given on Paper 4*; the laws and their derivatives are language to memorise.

### Cambridge 9702 (A-Level Physics) — §3.1

Same three laws, with two extras:
- $\mathbf{F} = d\mathbf{p}/dt$ is examined directly (variable-mass and impulse questions).
- Vector notation appears explicitly. Forces are bolded; resolution is into $\mathbf{i}, \mathbf{j}$ components on flat questions and along/perpendicular on inclines.
- $g = 9.81$ m/s² (data sheet).

> [!info] On the 9702 data sheet (page 2 of Papers 1, 2, 4)
> The data sheet gives $g = 9.81$ m/s² and the SUVAT formulas $s = ut + \tfrac12 at^2$, $v^2 = u^2 + 2as$. **It does NOT give $F = ma$ or $W = mg$** — those are language, you write them down.

### Cambridge 0625 (IGCSE Physics) — §1.5

IGCSE depth: Hooke's law, F = ma, weight = mg, terminal velocity (qualitative). N3 is in the Core syllabus as a phrase ("equal and opposite") without the misconception drill. Use the maths card lightly here — most 0625 mechanics questions are computational, not conceptual.

### A-Level Mathematics (9709, AQA, OCR, Edexcel) and IB AA HL

A-Level Maths Mechanics adds:
- **Variable-mass problems** (rocket equation): use $\mathbf{F} = d(m\mathbf{v})/dt$ in full, not the constant-mass corollary.
- **Impulse and momentum** (separate card: [[Linear Momentum]]).
- **Connected particles on a pulley with one mass on a slope** — combines this card with Friction.

IB AA HL also includes **simple harmonic motion** (Newton's 2nd applied to $-kx$), which becomes the entry point to oscillations.

### AP Physics 1 / C: Mechanics

AP Physics 1 examines all three laws qualitatively and through FBD problems. AP Physics C: Mechanics adds the differential form $\mathbf{F} = d\mathbf{p}/dt$ and momentum conservation as a full topic. The conceptual content is identical — only the mathematical sophistication differs.

---

## Why Newton's Laws Matter — College and Beyond

These three sentences run a *huge* fraction of physical science:

- **Engineering** — every bridge, building, vehicle, and rocket is designed using N2. Civil engineering is mostly equilibrium ($\Sigma \mathbf{F} = \mathbf{0}$, a special case of N2 with $\mathbf{a} = \mathbf{0}$); mechanical engineering is mostly $\mathbf{F} = m\mathbf{a}$ in motion.
- **Astronomy** — Newton applied N2 plus the inverse-square gravitational force law to derive Kepler's laws of planetary motion. Modern celestial mechanics, satellite orbits, and interplanetary trajectories all use the same equations Newton wrote in 1687, with computer-driven numerical integration in place of his hand calculus.
- **Lagrangian and Hamiltonian mechanics** (university physics) — recast Newton's laws in energy terms. The equations of motion become $\dfrac{d}{dt}\!\left(\dfrac{\partial L}{\partial \dot q}\right) - \dfrac{\partial L}{\partial q} = 0$, completely transforming our view of physics. Same predictions, deeper structure. Quantum mechanics and general relativity both grew out of the Lagrangian picture.
- **Game physics and animation** — every video game, animated film, and physics simulation uses numerical integration of $\mathbf{F} = m\mathbf{a}$ to update positions thirty or sixty times a second. Realistic-feeling motion is exactly what N1 + N2 produces.
- **Relativity (the limit of N2's reign)** — for speeds approaching $c$, $\mathbf{F} = d\mathbf{p}/dt$ remains correct *but* $\mathbf{p} = \gamma m \mathbf{v}$ with $\gamma = 1/\sqrt{1 - v^2/c^2}$. The constant-mass corollary $\mathbf{F} = m\mathbf{a}$ fails. Newton's 2nd law was a *guess* about how momentum changes; turns out it was almost right.

> [!info] Newton² — and the calculus-mechanics handshake
> The dot notation $\dot s, \ddot s$ for first and second time-derivatives belongs to Newton — invented for exactly this purpose. He needed a compact way to write "rate of change of position" because $F = m\ddot s$ is the statement of N2 in 1D Cartesian coordinates with constant mass. Newton-the-mathematician invented the calculus; Newton-the-physicist used it the next page over to predict planetary orbits. Two halves of the same brain, one century, one *Principia*. The maths card [[Kinematics Calculus]] tells the calculus side; this card tells the physics side. Same Newton, same handshake.

---

## Connections

- **Prerequisite:** [[Vectors]] — force, velocity, acceleration, momentum are all vectors; the FBD technique is vector decomposition by another name.
- **Prerequisite:** [[Kinematics Calculus]] — the s/v/a chain is *what* N2 acts on. N2 says: given the force, you get $a$, and integration gives $v$ and $s$.
- **Prerequisite:** [[Differentiation]] — $\mathbf{F} = d\mathbf{p}/dt$ is a derivative.
- **Prerequisite:** [[Travel Graphs (Vocab)]] — pre-calculus version of the same machinery.
- **Component:** [[Equilibrium]] — the special case $\mathbf{a} = \mathbf{0}$ of N2; "no acceleration" means "resultant force = 0."
- **Component:** [[The Friction Limit|Friction]] — one of the standard forces appearing in FBDs; limiting friction $F = \mu R$ is what closes 9709 §4.1.
- **Extension:** [[Linear Momentum]] — the integrated form of N2: impulse = change of momentum; conservation of momentum follows from N3 applied to a closed system.
- **Extension:** [[Work, Energy and Power]] — integrating $\mathbf{F} \cdot d\mathbf{s}$ gives the work-energy theorem, derived directly from N2.
- **Extension:** [[Connected Particles]] — Examples 3 and 4 generalised; pulleys, multiple masses, slopes.
- **Extension:** [[Inclined Plane Motion]] — Example 2 with friction added.
- **Application:** [[Circular Motion]] — for circular motion, $\mathbf{F} = m\mathbf{a}$ with $\mathbf{a}$ pointing toward the centre and magnitude $v^2/r$. (9702 §12.2)
- **Application:** [[Simple Harmonic Motion]] — N2 applied to a restoring force $F = -kx$ gives the SHM equation $\ddot x = -\omega^2 x$.
- **Reverse — historical:** Aristotle's *Physics* (~350 BC) and Galileo's *Dialogue* (1632); the long arc that made N1 possible.
- **Cross-domain bridge:** [[Inertia and Bootstrapping]] — N1 as a model for human productivity, static vs kinetic friction in habit formation, activation energy in chemistry, the cold-start problem in software.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{F}$ | `\mathbf{F}` | Force as a vector (9702, A-Level) |
| $F$ | `F` | Magnitude of force / scalar component (9709 P4 convention) |
| $\mathbf{F}_{\text{net}}$ | `\mathbf{F}_{\text{net}}` | Resultant / net force |
| $\Sigma \mathbf{F}$ | `\Sigma \mathbf{F}` | Sum of forces (same as $\mathbf{F}_{\text{net}}$) |
| $\mathbf{p}$ | `\mathbf{p}` | Linear momentum vector |
| $m$ | `m` | Mass (scalar) |
| $\mathbf{a}$ | `\mathbf{a}` | Acceleration vector |
| $\mathbf{F} = m\mathbf{a}$ | `\mathbf{F} = m\mathbf{a}` | Newton's 2nd, constant-mass form |
| $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$ | `\dfrac{d\mathbf{p}}{dt}` | Newton's 2nd, general form |
| $W = mg$ | `W = mg` | Weight as a force (units N) |
| $N$ | `N` | Normal contact force (also unit "newton" — context disambiguates) |
| $T$ | `T` | Tension in a rope or string |
| $\mathbf{F}_{AB}$ | `\mathbf{F}_{AB}` | Force on B due to A (N3 partner of $\mathbf{F}_{BA}$) |
| $\dot x, \ddot x$ | `\dot x, \ddot x` | Newton's dot notation for $dx/dt, d^2x/dt^2$ |
| $g$ | `g` | Gravitational field strength (10 in 9709, 9.81 in 9702) |
| $\mu$ | `\mu` | Coefficient of friction (limiting friction $F = \mu R$, see [[The Friction Limit]]) |
