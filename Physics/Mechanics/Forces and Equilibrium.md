---
chinese: 力与平衡 / 力的平衡 (lì yǔ pínghéng / lì de pínghéng)
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Vectors]]"
  - "[[Vectors in Physics]]"
  - "[[Force (Vocab)]]"
  - "[[Normal Force (Vocab)]]"
  - "[[Friction (Vocab)]]"
  - "[[Tension (Vocab)]]"
leads_to:
  - "[[Centre of Mass]]"
  - "[[The Friction Limit]]"
  - "[[Statics]]"
  - "[[Lami's Theorem]]"
  - "[[Choosing Effective Equations]]"
  - "[[Torque]]"
  - "[[Braking Systems]]"
  - "[[Stress, Strain and Young Modulus]]"
  - "[[Circular Motion]]"
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
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9709-4-1
  - syllabus/9702-4-1
  - syllabus/9702-4-2
  - syllabus/0625-1-3
  - syllabus/0625-1-5
  - syllabus/IB-Physics-A-2-1
  - syllabus/AP-Physics-1-2-2
  - syllabus/AP-Physics-1-2-3
  - syllabus/AP-Physics-1-2-4
  - syllabus/AP-Physics-C-Mech-2-2
  - syllabus/AP-Physics-C-Mech-2-3
  - syllabus/AP-Physics-C-Mech-2-4
  - syllabus/9231-3-2
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/Sigma-F
  - notation/Sigma-tau
  - notation/moment-arm
  - misconception/equilibrium-is-just-no-net-force
  - misconception/centre-of-gravity-equals-centre-of-mass
  - misconception/pivot-must-be-the-real-pivot
---

# Forces and Equilibrium 力与平衡

## Definition

A body is in **equilibrium** when *both* of the following are true:

1. **Translational equilibrium:** the resultant force is zero.
   $$\sum \mathbf{F} \;=\; \mathbf{0}$$
2. **Rotational equilibrium:** the resultant moment (torque) about *any* point is zero.
   $$\sum \boldsymbol{\tau} \;=\; \mathbf{0}$$

A body satisfying both has **zero linear acceleration AND zero angular acceleration**. Stationary bodies are the most familiar case; a rocket coasting through deep space without spinning is also in equilibrium. Equilibrium is a property of the *forces and their arrangement*, not of motion itself.

> [!warning] Equilibrium needs *both* halves
> Many students learn "equilibrium = forces balance" and stop there. That's only half. The forces can sum to zero and still produce **rotation** if they don't act through the same point.
>
> Picture two equal-and-opposite horizontal forces applied to opposite ends of a rod. Sum of forces = 0. Sum of moments about the centre = $F \cdot L \neq 0$. The rod spins. This is called a **couple** — pure torque, zero net force, definitely not equilibrium.
>
> Real equilibrium needs *both* $\sum \mathbf{F} = \mathbf{0}$ *and* $\sum \boldsymbol{\tau} = \mathbf{0}$.

### 中文锚点

**平衡 (pínghéng)** = 物体既**不平动**也**不转动**。

| English | 中文 | 数学条件 |
|---|---|---|
| Translational equilibrium | 平动平衡 | $\sum \mathbf{F} = \mathbf{0}$ |
| Rotational equilibrium | 转动平衡 | $\sum \boldsymbol{\tau} = \mathbf{0}$ |
| Both at once | 力的平衡 / equilibrium proper | 两者**同时**成立 |
| Couple | 力偶 (lì'ǒu) | $\sum \mathbf{F} = \mathbf{0}$ 但 $\sum \boldsymbol{\tau} \neq \mathbf{0}$ |

考试关键：
- 9702 / 0625 / IB / AP **都要求**两个条件同时成立
- 9709 P4 §4.1 **不考力矩**（moment），只考 $\sum \mathbf{F} = \mathbf{0}$ — 但理解力矩对其他考纲都是必要的
- "Take moments about a point" 是英文力学的核心解题技巧 — 选对支点能消去未知力

---

## The Rock Climber — equilibrium as a lived experience

![[forces-three-point-balance-climber.png]]

If you want to understand equilibrium *in your bones*, find a climbing wall.

A rock climber pinned mid-route is a four-point body in static equilibrium: two hands on holds, two feet on holds (or sometimes three contacts). Every contact provides a contact force decomposable into normal + friction. The climber's weight pulls them down. Their hold positions and body angles determine the magnitudes and directions of every contact force. *They can read all of this without writing an equation.*

What experienced climbers internalise:

- **Sum of forces** — to stay in place, the four contact forces must vector-sum to $-\mathbf{W}$ (cancel gravity). Lean too far away from the wall: the friction at the contact patches has to grow, eventually exceeding $\mu N$, and you peel off. Lean *into* the wall (more $N$) and the available friction grows; you stick.
- **Sum of moments** — the climber's centre of gravity, projected onto the floor, must lie within the support footprint. Rotate the upper body too far out: the centre of gravity exits the footprint, gravity's moment about the foothold can no longer be balanced, and the climber tips off the wall — even if friction was holding fine a moment before.
- **The force triangle** — when only three contacts dominate (typical of a tricky move), the three contact forces must form a closed triangle (force diagram). Climbers learn to feel which contact is "doing more work" by where their weight is hanging.
- **Limiting friction** — every grip is one slip away from kinetic friction (the slip = the fall). Climbers operate near $F = \mu N$ at every hold, all the time. That's why the [[The Friction Limit]] card gets to claim climbing as the static-side anchor — the dynamic-side anchor is F1.

A climber doesn't compute these consciously. They feel them. The vault's job is to give a Cambridge student the equations that describe what a climber *already knows*.

![[forces-rock-climber-equilibrium.svg|525]]

---

## Translational Equilibrium — $\sum \mathbf{F} = \mathbf{0}$

Already familiar from [[Newton's Laws of Motion]] (the special case of N2 with $\mathbf{a} = \mathbf{0}$). The technique: pick perpendicular axes, resolve every force into components along those axes, write one scalar equilibrium equation per axis.

For a planar problem, two equations:

$$\sum F_x = 0 \qquad \sum F_y = 0$$

Choose axes that *minimise* the algebra — usually horizontal/vertical for a flat problem, or along/perpendicular to a slope when one's involved. Some forces (like the normal force on a slope) align with one axis and zero out of the other; that's the saving you're chasing when you tilt your axes.

### Triangle of forces — three coplanar forces in equilibrium

A body acted on by exactly **three coplanar forces** in equilibrium has a special property: drawn nose-to-tail (head-to-tail in old notation; *start-to-end* per the vault convention from [[Vectors]]), the three force vectors form a **closed triangle**.

This is just $\mathbf{F}_1 + \mathbf{F}_2 + \mathbf{F}_3 = \mathbf{0}$ drawn pictorially. Closing the triangle is the geometric statement of force balance.

Two practical consequences:
- **Sine rule** on the triangle gives **Lami's theorem**: $\dfrac{F_1}{\sin\alpha_1} = \dfrac{F_2}{\sin\alpha_2} = \dfrac{F_3}{\sin\alpha_3}$, where each $\alpha_i$ is the angle *between the other two forces*. Mentioned in 9709 P4 syllabus as an acceptable alternative to resolving — Cambridge says it's "not required knowledge, and will not be referred to in questions" but is allowed.
- **Concurrent forces** — for three coplanar forces in equilibrium on a rigid body, the lines of action of all three must pass through a common point (otherwise they'd form a couple of the type "no resultant force, but a moment"). This is a useful sanity-check on a force diagram.

---

## Moments / Torques — the rotational half

A **moment** (also called **torque** in physics; same thing, different convention by region) measures a force's tendency to rotate a body about a chosen pivot point. Definition for a force in 2D:

$$\boxed{\;\tau \;=\; F \cdot d \;=\; F \cdot r \sin\theta\;}$$

where:
- $F$ is the force magnitude;
- $d$ is the **perpendicular distance** from the pivot to the line of action of the force (called the *moment arm* or *lever arm*);
- equivalently, $d = r \sin\theta$ where $r$ is the distance from pivot to the force's point of application and $\theta$ is the angle between $\mathbf{r}$ and $\mathbf{F}$.

Units: newton-metres (N·m). *Not* joules, even though the units look identical — moments and energy are physically distinct. Cambridge writes "N·m" or "Nm" for moments, "J" for energy.

![[forces-moment-of-a-force.svg]]

### Sign convention

Cambridge convention: **anticlockwise (counter-clockwise) is positive**, clockwise is negative. (The convention is arbitrary; what matters is consistency within a problem.) Some textbooks reverse it; pick one and stick to it.

### Couple — pure torque, no net force

Two equal-and-opposite parallel forces *not* sharing a line of action form a **couple** (force pair). The two forces sum to $\mathbf{0}$ — no net translational effect. But each contributes a moment in the *same direction* (both clockwise or both anticlockwise — the equal-and-opposite cancellation only happens for forces, not for their moments). Total moment of a couple:

$$\tau_{\text{couple}} \;=\; F \cdot s$$

where $s$ is the perpendicular distance between the two lines of action.

A couple is therefore a *pure rotation* effect. Examples: turning a tap with two fingers (one pushing, one pulling), wringing out a wet towel, the moment a screwdriver applies. Cambridge 9702 §4.1 examines couples explicitly.

### Principle of moments

For a body in rotational equilibrium about *any* chosen pivot:

$$\sum (\text{anticlockwise moments}) \;=\; \sum (\text{clockwise moments})$$

Or equivalently, the signed sum of all moments equals zero. The principle of moments is the rotational analogue of "forces balance."

> [!info] You can pick *any* point as the pivot
> A subtle and powerful fact: the principle of moments holds about *any* point, not just the "actual" pivot of the system. So when you're solving a beam problem, choose your pivot to *eliminate the most unknowns*. If a force you don't care about acts at point $P$, take moments about $P$ and that force vanishes from the equation (its moment arm is zero).
>
> Strategic pivot-choice cuts a four-unknown problem down to one or two equations. This is the single biggest technique-saving in 9702 / IB statics.

---

## Centre of Gravity — and stability

The **centre of gravity** (重心, zhòngxīn) of a body is the point where its **total weight** can be considered to act. For a uniform body in a uniform gravitational field, this coincides with the **centre of mass** (质心, zhìxīn) — the mass-weighted average position. The two are formally distinct but practically identical for everything you'll meet at A-Level. [[Centre of Mass]] proves why the replacement is legitimate and shows how to *locate* the point when it isn't obvious — composite shapes, laminae with pieces removed, and the toppling-versus-sliding comparison in numbers.

### Stability — the toppling test

Place a body on a flat surface. The vertical line through its centre of gravity is the **line of action of weight**. If that line passes *inside* the body's **base of support** (the convex hull of its contact points with the ground), the body is **stable**: small disturbances produce a restoring moment that returns it to upright.

If the line passes *outside* the base, the body **topples**. The boundary case — line of weight exactly at the edge of the base — is the **toppling condition**, and Cambridge problems often ask "find the angle at which the block first topples."

![[forces-centre-of-gravity-toppling.svg]]

A real-life calibration: when you stand and lean forward, you can feel your stability decreasing because your weight-line is moving toward your toes. Lean too far and you fall. Walking is *controlled toppling* — each step deliberately moves the centre of gravity outside the standing-foot base, and the new foot catches it before you fall.

---

## Worked Examples

### Example 1 — Block in equilibrium on a rough horizontal surface (9709 P4 §4.1)

A 5 kg block rests on a rough horizontal table ($\mu = 0.4$). A horizontal force $P$ is applied. Find:
(a) the largest $P$ for which the block remains stationary; (b) the friction force when $P = 10$ N.

Use $g = 10$ m/s². Weight $mg = 50$ N; vertical equilibrium gives $N = 50$ N. Maximum static friction $F_{\max} = \mu N = 0.4 \times 50 = 20$ N.

(a) **Largest $P$ for which the block stays put** — this is **limiting equilibrium**: $P = F_{\max} = \boxed{20 \text{ N}}$.

(b) **At $P = 10$ N**, the block is well below the limit, so static friction *adjusts* to balance the applied force: $F = P = \boxed{10 \text{ N}}$. Notice friction is *not* $\mu N = 20$ N here — that's only at the limit. (See [[Friction (Vocab)]] for the static-friction-as-inequality reminder.)

### Example 2 — Block in limiting equilibrium on a rough slope

A block is placed on a rough plane inclined at angle $\theta$. The angle is increased until the block is just on the point of sliding. Show that $\mu = \tan\theta$ at this critical angle.

**FBD on the block.** Three forces: weight $mg$ down (vertical), normal $N$ perpendicular to slope (outward), friction $F$ along slope (uphill, opposing the tendency to slide).

Resolve $mg$ along and perpendicular to the slope:
- Down-slope component: $mg \sin\theta$.
- Into-slope component: $mg \cos\theta$.

Equilibrium perpendicular to slope: $N = mg \cos\theta$.
Equilibrium along slope: $F = mg \sin\theta$.

At the *limit*, $F = \mu N$:

$$mg \sin\theta = \mu \cdot mg \cos\theta \;\Longrightarrow\; \mu \;=\; \dfrac{\sin\theta}{\cos\theta} \;=\; \boxed{\tan\theta}.$$

This is **the angle of friction** (also angle of repose, 摩擦角): the steepest angle at which a body of any mass can rest on the slope without sliding. The mass cancels — only the surface-pair coefficient matters. Mountains of dry sand always rest at the same maximum slope angle (about 34° for sand), regardless of how much sand is piled up. The angle of repose is a *material property*.

### Example 3 — A beam with two supports and a walker (moments)

A uniform plank of mass 20 kg and length 4 m rests horizontally on two supports, $A$ at the left end and $B$ at 3 m from $A$ (so 1 m from the right end). A 60 kg person stands on the plank at distance $x$ from $A$. Find the reaction force at each support as a function of $x$. For what range of $x$ does the plank remain in contact with both supports?

Use $g = 10$ m/s² for clean arithmetic.

**Forces on the plank:**
- Weight of plank $= 200$ N, acting at the centre (2 m from $A$ — uniform plank).
- Weight of person $= 600$ N, acting at $x$ from $A$.
- Normal reactions $R_A$ at $A$ and $R_B$ at $B$ (3 m from $A$), both upward.

**Translational equilibrium (vertical):**
$$R_A + R_B = 200 + 600 = 800 \text{ N.}$$

**Take moments about $A$** (eliminates $R_A$):
$$R_B \times 3 = 200 \times 2 + 600 \times x$$
$$R_B = \dfrac{400 + 600x}{3} \text{ N.}$$

Substituting back:
$$R_A = 800 - R_B = 800 - \dfrac{400 + 600x}{3} = \dfrac{2000 - 600x}{3} \text{ N.}$$

**Contact at both supports** requires $R_A \geq 0$ and $R_B \geq 0$.

$R_A \geq 0$: $2000 - 600 x \geq 0 \;\Rightarrow\; x \leq 10/3 \approx 3.33$ m. (Beyond this, the plank tips off support $A$.)
$R_B \geq 0$: $400 + 600 x \geq 0$ — always true for $x \geq 0$.

So the plank remains in contact with both supports for $\boxed{0 \leq x \leq 3.33 \text{ m}}$. At $x = 3.33$ m, $R_A = 0$ (on the verge of lifting off); beyond, the plank pivots about $B$.

> [!tip] Why moments about $A$?
> $R_A$ acts *at* $A$, so its moment about $A$ is zero (moment arm = 0). Taking moments about $A$ removes $R_A$ from the equation — leaving $R_B$ as the only unknown. We then get $R_A$ from the translational-equilibrium equation. This pivot-choice trick saves one equation's worth of algebra on every beam problem.

### Example 4 — Ladder against a wall (the classic combined problem)

A uniform ladder of mass 30 kg and length 5 m leans against a smooth vertical wall, with its foot on rough ground (coefficient $\mu = 0.4$). It makes angle $\alpha$ with the vertical. Find the smallest $\alpha$ for which the ladder doesn't slip.

(Use $g = 10$ m/s²; weight $= 300$ N at centre = 2.5 m up the ladder.)

**Forces on the ladder:**
- Weight $W = 300$ N, downward, at the centre.
- $N_{\text{wall}}$ from the wall, horizontal (smooth wall — no friction), pushing the ladder away.
- $N_{\text{ground}}$ from the ground, vertical, pushing up.
- $F_{\text{ground}}$ from the ground, horizontal, friction (preventing the foot from sliding outward).

The ladder slips when the ground friction reaches its limit: $F_{\text{ground}} = \mu N_{\text{ground}}$.

**Equilibrium equations:**

Vertical: $N_{\text{ground}} = W = 300$ N.
Horizontal: $F_{\text{ground}} = N_{\text{wall}}$.

**Take moments about the foot of the ladder** (eliminates $N_{\text{ground}}$ and $F_{\text{ground}}$ — both act at the foot):

$$W \times (2.5 \sin\alpha) \;=\; N_{\text{wall}} \times (5 \cos\alpha)$$
$$300 \times 2.5 \sin\alpha = N_{\text{wall}} \times 5 \cos\alpha$$
$$N_{\text{wall}} = 150 \tan\alpha.$$

So $F_{\text{ground}} = N_{\text{wall}} = 150 \tan\alpha$. At the slip-point:

$$150 \tan\alpha = \mu \times 300 \;\Longrightarrow\; \tan\alpha = 2\mu = 0.8 \;\Longrightarrow\; \alpha = \tan^{-1}(0.8) \approx \boxed{38.7°}.$$

The ladder must be *at least* this angle from vertical (or equivalently, no more steep than $90° - 38.7° = 51.3°$ from horizontal, i.e. fairly upright is bad — it slides). Real ladders have safer angles around 60–70° from horizontal, with margin.

---

## Common Misconceptions

### 1. "Equilibrium just means $\sum \mathbf{F} = \mathbf{0}$"

Addressed at length above. The forces can sum to zero and the body still rotate (couple). Real equilibrium needs **both** $\sum \mathbf{F} = \mathbf{0}$ AND $\sum \boldsymbol{\tau} = \mathbf{0}$.

### 2. "I have to take moments about the actual pivot"

The principle of moments holds about *any* point. Strategic pivot-choice (usually a point where an unknown force acts) eliminates that force from the equation. The "real" pivot of the system has no special privilege.

### 3. "Static friction equals $\mu N$"

Only at the limit. Static friction takes whatever value the equilibrium equations require, up to $\mu_s N$. See [[Friction (Vocab)]] §"The Formula That's Not a Formula."

### 4. "The centre of gravity is always at the geometric centre"

Only for *uniform* bodies. A non-uniform body has its centre of gravity wherever the mass is concentrated. A pencil with a heavy eraser has its centre of gravity well toward the eraser end — that's why it stands up best on the eraser. (Try it.) Cambridge questions sometimes specify "uniform" to fix the centre of gravity at the geometric middle; if the word *uniform* is missing, *don't assume*.

### 5. "Centre of gravity equals centre of mass"

For all everyday gravitational fields, yes — they coincide. The two differ when the gravitational field varies across the body (e.g. a very long object in a non-uniform field — relevant only at planetary scales). At Cambridge / A-Level scope, treat them as the same point, but know the technical distinction exists.

---

## Exam Notes

### Cambridge 9709 Paper 4 (Mechanics, AS) — §4.1

**In scope:**
- Identify the forces acting in a given situation; force diagrams.
- Vector nature of force; resolve into components and find resultants.
- Equilibrium $\sum \mathbf{F} = \mathbf{0}$, including via component-equations.
- Triangle of forces / Lami's theorem accepted as alternatives but not required.
- Smooth/rough contact split; limiting friction $F = \mu R$ at the limit.
- Newton's 3rd law applied to contact problems.

**NOT in scope (despite appearing in 9702 and 0625):**
- Moments / torques. *9709 P4 does not examine moments.* If a question hints at rotational effects, it's outside the syllabus.

So 9709 students should master the translational half of this card and skip the moments / centre-of-gravity sections (return to them when bridging to 9702 or A-Level Mechanics 2).

### Cambridge 9702 (A-Level Physics) — §4.1, §4.2

§4.1 covers turning effects: moment of a force; couple; torque of a couple; principle of moments. Vector notation appears explicitly.

§4.2 covers full equilibrium ($\sum \mathbf{F} = \mathbf{0}$ and $\sum \boldsymbol{\tau} = \mathbf{0}$), triangle of forces, centre of gravity. *Both* halves are examinable.

> [!info] On the 9702 data sheet
> No formulas given. $\tau = Fd$, $W = mg$, principle of moments — all language-to-memorise.

### Cambridge 0625 (IGCSE Physics) — §1.3, §1.5

§1.3: mass vs weight, $W = mg$ with $g$ as gravitational field strength ([[Gravitational Fields]] carries the field itself). §1.5 Core: resultant force, $F = ma$, friction qualitative, turning effect of a force qualitative, equilibrium, centre of gravity (toppling). Extended: principle of moments quantitative; circular motion qualitative ([[Circular Motion]]).

### Cambridge 9231 (Further Mechanics, Paper 3 — §3.2)

Equilibrium of a rigid body: moment of a force about a point, coplanar forces in equilibrium, and **toppling vs sliding** — the concept and the toppling test are here; the syllabus also wants **centres of mass of uniform laminae and composite bodies** (triangular lamina, standard shapes by symmetry, MF19's list), which this card states but does not compute. $g = 10$.

### IB Physics (A.2.1)

Free-body diagrams for one- and two-dimensional situations, the resultant force, and Newton's first law applied to translational equilibrium; forces labelled with their accepted names. The moments half is not in A.2 (rigid-body rotation lives in A.4).

### AP Physics 1 / C: Mechanics (§2.2–2.4)

2.2 forces and free-body diagrams, 2.3 Newton's third law (the contact-pair reasoning on this page), 2.4 Newton's first law as translational equilibrium; AP Physics 1 keeps static equilibrium qualitative-plus-simple, AP C adds the centre-of-mass integral and rotational equilibrium with calculus.

### Edexcel IAL (M1 statics of a particle; M2 rigid bodies) · OxAQA 9660 (M1.3, M2.3)

The particle half — resolving, $\sum F = 0$, limiting friction — is M1 on both boards; the rigid-body half (moments, centres of mass of laminae, suspension and toppling) is IAL M2 / 9660 M2.3, where again the computations of centres of mass are the piece still owed.

### Where it is *not* examined

Not on Cambridge 0580 / 0606 or OxAQA 9260 (no mechanics), not in IB AA / AI (no mechanics option since 2019); and 9709 P4 examines only the particle half — see the top of this section.

---

## Why Forces and Equilibrium Matters — College and Beyond

- **Civil engineering** — bridges, buildings, cranes, scaffolding, dams. Civil structures are designed to be permanently in equilibrium (a building that isn't is a building that's *fallen down*). The design is mostly $\sum \mathbf{F} = \mathbf{0}$ + $\sum \boldsymbol{\tau} = \mathbf{0}$ with appropriate safety margins. Truss analysis, beam-bending stress calculations, and tower stability all start from these two equations.
- **Mechanical engineering** — every machine has *some* equilibrium configurations and the engineering question is which they are and how stable. Robot-arm positioning, vehicle suspension geometry, and crane reach all use moment balance.
- **Climbing and parkour** — the lived-equilibrium examples already discussed. Top-tier athletes have an internal force-and-moment intuition that surpasses naive computation; it's *also* the kind of intuition that emerges from doing physics well.
- **Statics as a university course** — Engineering Statics is the standard first-year university course that takes this card and runs with it for an entire semester: 3D equilibrium, frictionless and frictional pin joints, internal forces in trusses and frames, distributed loads, hydrostatic pressure on submerged bodies. Every result starts from $\sum \mathbf{F} = \mathbf{0}$ and $\sum \boldsymbol{\tau} = \mathbf{0}$.
- **Variational mechanics** — the whole alternative-formulation of Lagrangian mechanics arrived at by replacing equilibrium-of-forces with the *principle of virtual work*: a body is in equilibrium if and only if no infinitesimal allowed displacement does any net work. Same answer, deeper structure. The Lagrangian's generalisation goes on to power quantum mechanics and general relativity. (Wild that "things don't move" leads to "Schrödinger's equation," but it does.)

> [!info] Equilibrium is a *generic* concept — not just for mechanics
> The pattern *"a system minimises some quantity, and all forces / influences balance at the minimum"* shows up *everywhere*:
>
> | Domain | Quantity at the minimum | Equilibrium condition |
> |---|---|---|
> | Mechanics | Potential energy | $\sum \mathbf{F} = \mathbf{0}$ |
> | Thermodynamics | Free energy | $\Delta G = 0$ |
> | Chemistry | Free energy of reaction | $K = $ const at equilibrium |
> | Economics | Cost / price-mismatch | Supply = demand |
> | Game theory | Loss function | Nash equilibrium ($\nabla L = 0$) |
> | Optimisation in ML | Training loss | Gradient $= 0$ |
> | Biology (homeostasis) | Some metabolic cost function | "Stable" body temperature, blood pH, etc. |
>
> Equilibrium-of-forces is the *first* example of a much bigger pattern. When this card says "the resultant force is zero," what it's *really* saying is "we're at a minimum of potential energy and any small displacement increases it." That re-framing — equilibrium as energy minimisation — is the doorway to all of variational physics.

---

## Connections

- **Prerequisite:** [[Newton's Laws of Motion]] — equilibrium is the special case $\mathbf{a} = \mathbf{0}$ of N2; the technique of summing forces uses N2 component-wise.
- **Prerequisite:** [[Vectors]] — every force is a vector; resolution into components is vector decomposition.
- **Prerequisite:** [[Force (Vocab)]], [[Normal Force (Vocab)]], [[Friction (Vocab)]], [[Tension (Vocab)]] — the named contact forces appearing in every FBD.
- **Component:** [[Centre of Mass]] — the point where the gravitational force can be considered to act; foundation of stability.
- **Component:** [[Lami's Theorem]] — the sine-rule statement of three-coplanar-force equilibrium.
- **Application:** [[The Friction Limit]] — climbing as the static-side limit-finding example; pulls forward the rock-climbing thread of this card into an F1 + climbing + motorcycles cross-cutting card.
- **Application:** [[Statics]] (planned, university-level) — extends this card to 3D rigid-body equilibrium, distributed loads, and engineering structures.
- **Cross-domain bridge:** equilibrium as energy minimisation → variational mechanics → Lagrangian/Hamiltonian formulations → quantum mechanics. Mechanics's deepest re-framing starts here.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\sum \mathbf{F}$ | `\sum \mathbf{F}` | Resultant / sum of forces |
| $\sum \boldsymbol{\tau}$ | `\sum \boldsymbol{\tau}` | Sum of moments / torques |
| $\tau$ | `\tau` | Moment / torque magnitude |
| $\tau = Fd$ | `\tau = Fd` | Moment as force × perpendicular distance |
| $\tau = Fr\sin\theta$ | `\tau = Fr\sin\theta` | Moment with the angle form |
| $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$ | `\mathbf{r} \times \mathbf{F}` | Vector cross-product form (university level) |
| $\alpha$ | `\alpha` | Angle to vertical (ladder problems) |
| $\theta$ | `\theta` | Angle of inclination (slope problems) |
| $\mu = \tan\theta$ | `\mu = \tan\theta` | Angle of friction at limiting equilibrium |
| $R, N$ | `R, N` | Normal force (interchangeable in Cambridge usage) |
