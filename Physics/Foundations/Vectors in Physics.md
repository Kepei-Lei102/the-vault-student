---
chinese: 物理中的向量 (wùlǐ zhōng de xiàngliàng)
prerequisites:
  - "[[Vectors]]"
  - "[[Magnitude of a Vector (Vocab)]]"
  - "[[Physical Quantities and Units]]"
  - "[[Pythagoras Theorem]]"
  - "[[Trigonometric Ratios]]"
leads_to:
  - "[[Newton's Law of Restitution]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Forces and Equilibrium]]"
  - "[[Torque]]"
  - "[[SUVAT]]"
  - "[[Linear Momentum]]"
  - "[[Stories/Aristotle to Apollo]]"
  - "[[Aristotle to Apollo]]"
  - "[[Kinetic Theory and the Ideal Gas]]"
  - "[[Circular Motion]]"
  - "[[Gravitational Fields]]"
  - "[[Projectile Motion]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/foundations
  - domain/mechanics
  - level/A-Level
  - level/IB
  - level/AP
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-Mechanics
  - curriculum/AP-Physics-C-EM
  - syllabus/9702-1-4
  - syllabus/0625-1-1
  - syllabus/IB-Physics-A-1
  - syllabus/AP-Physics-1-1-1
  - syllabus/AP-Physics-C-Mechanics-1-1
  - type/deep
  - type/definition
  - notation/bold-vector
  - notation/arrow-vector
  - misconception/vector-vs-scalar
  - misconception/components-change-vector
  - misconception/axes-pick-themselves
  - misconception/magnitude-only-thinking
---

# Vectors in Physics 物理中的向量

## Hunter trace — why is breaking a vector apart "allowed"?

Open any physics textbook to a problem with an inclined plane. The first move every teacher makes — without comment, as if it were the most obvious thing in the world — is to take gravity, $m\mathbf{g}$, which points straight down, and *break it into two pieces*: one along the slope ($mg\sin\theta$) and one perpendicular to the slope ($mg\cos\theta$). The original "straight-down" arrow gets relabelled as the *sum* of two perpendicular arrows along a tilted set of axes that wasn't even present in the problem before someone drew it.

This is the most-used technique in mechanics. Every block-on-a-slope problem starts here. Every projectile motion problem starts here. Every "resolve the force horizontally and vertically" instruction asks you to do it. And yet: ***why is this allowed?***

The slope's angle has not changed gravity. There is no physical thing acting on the block in the "along the slope" direction that wasn't already there before you drew the dashed lines. The block is being pulled down by gravity — one vector, one cause — and somehow we are now claiming it is being pulled by *two* vectors at right angles, neither of which points "down." Where did the second arrow come from?

The answer is the deep idea this card exists to teach: **a vector doesn't *have* components. You *choose* them.** The vector itself — the physical "thing" doing the pulling — is invariant. It does not know or care which coordinate system you picked. When you change axes, the *numbers* change; what they describe does not. This is the same symmetry idea from [[Physical Quantities and Units]] §"Dimensional homogeneity" — the laws of physics shouldn't depend on a representational choice that was up to you. Decomposing $m\mathbf{g}$ into $mg\sin\theta$ + $mg\cos\theta$ in slope-aligned axes is *equivalent* to leaving it as $(0, -mg)$ in horizontal-vertical axes; both describe the same arrow. **You pick the axes that make the problem easy.**

That choice is the central skill of mechanics. This card teaches it.

## Definition — scalar vs vector, the physicist's taxonomy

The elementary quantities considered here are **scalars** (no spatial direction) or **vectors** (magnitude and direction). More general physical quantities can require tensors; a scalar can also be signed, as electric charge is.

The test is exactly one question: ***if I add direction to this quantity, does the meaning change?*** If yes, it's a vector. If no, it's a scalar.

- "5 kg of flour" — adding a direction makes no sense ("5 kg of flour pointing north"?). Mass is a scalar.
- "5 m/s to the east" — adding a direction changes the meaning (versus "5 m/s to the west"). Velocity is a vector.

The table below is the working physicist's cheat sheet. The [[Vectors]] card has a smaller version; this one is exhaustive for AS-level mechanics.

| Vector quantities (magnitude + direction) | Scalar quantities (magnitude only) |
|---|---|
| Displacement $\mathbf{s}$ | Distance $d$ |
| Velocity $\mathbf{v}$ | Speed $\lvert \mathbf{v} \rvert$ |
| Acceleration $\mathbf{a}$ | Time $t$ |
| Force $\mathbf{F}$ | Mass $m$ |
| Weight $\mathbf{W} = m\mathbf{g}$ | Energy $E$ (KE, GPE, EPE all scalar) |
| Momentum $\mathbf{p} = m\mathbf{v}$ | Power $P$ |
| Impulse $\mathbf{J} = \mathbf{F}\Delta t$ | Work $W = \mathbf{F} \cdot \mathbf{s}$ (a scalar — the *dot product* of two vectors) |
| Electric field $\mathbf{E}$, magnetic field $\mathbf{B}$ | Temperature $T$, pressure $p$, density $\rho$ |
| Torque $\boldsymbol{\tau}$ | Charge $q$ (the *field* is a vector; the *charge itself* is a scalar) |
| Angular velocity $\boldsymbol{\omega}$ | Frequency $f$, period $T$ |

The pairs **distance vs displacement** and **speed vs velocity** are the most exam-tested distinction at IGCSE/AS level. Distance and speed are the *path lengths*; displacement and velocity are *straight-line vectors from start to finish*. A runner who completes a $400~\text{m}$ track and returns to the starting line has *distance* $400~\text{m}$ but *displacement* $\mathbf{0}$. Their *average speed* is non-zero; their *average velocity* is $\mathbf{0}$.

### Notation

| Convention | Example | Used by |
|---|---|---|
| Bold non-italic | $\mathbf{F}$ | Most physics texts, this vault, university maths |
| Arrow above | $\vec{F}$ | Chinese high-school textbooks, some IB resources |
| Underline | $\underline{F}$ | Some UK secondary texts |
| Italic, no decoration | $F$ | Used when context makes 1D-ness obvious (e.g. inside an integral along one axis); *sloppy* when used for a true vector |

The bold ($\mathbf{F}$) and arrow ($\vec{F}$) conventions mean the same thing. A Chinese student trained with 矢量 $\vec{F}$ should read $\mathbf{F}$ as identical. This vault uses bold consistently.

### 中文锚点

斜拉着行李箱走时，你的手只施加了一股拉力，却既把箱子往前拉，又稍稍向上提。把这股力“分解”，就是分别看它在向前和向上两个方向上起多大作用，并没有凭空多出两股力。换一套方向来描述，分量的数值会变，手上的拉力却没变。向量——物理里也叫矢量——记住的就是这股作用有多大、朝哪里。

## Key Vocabulary

| English | 中文 | 含义 |
|---|---|---|
| Scalar | 标量 (biāoliàng) | 只有大小，没有方向 |
| Vector | 矢量 / 向量 (shǐliàng / xiàngliàng) | 有大小有方向 |
| Resultant | 合矢量 / 合力 (héshǐliàng / hélì) | 多个矢量相加的结果 |
| Resolve (a vector) | 分解 (fēnjiě) | 把一个矢量拆成两个分量 |
| Component | 分量 (fēnliàng) | 矢量在某方向上的投影 |
| Perpendicular | 垂直 (chuízhí) | 互相成 90° |
| Parallelogram law | 平行四边形法则 (píngxíng sìbiānxíng fǎzé) | 矢量加法的几何方法 |
| Triangle of forces | 三力平衡三角形 (sānlì pínghéng sānjiǎoxíng) | 三力平衡时依次从上一箭头的终点接到下一箭头的起点，组成闭合三角形 |

## The choice-of-axes principle

Take any vector $\mathbf{F}$ in a plane. Pick a pair of perpendicular axes — call them $x$ and $y$. The vector now has two **components**:

$$F_x = F\cos\alpha, \qquad F_y = F\sin\alpha$$

where $\alpha$ is the angle between the vector and the $x$-axis. The numbers $F_x$ and $F_y$ depend entirely on *which $x$-axis you picked*. Rotate your axes by $30°$; both numbers change. Rotate by $90°$; they swap (and one flips sign). Rotate to align $x$ with the vector itself; $F_x = F$ and $F_y = 0$.

***The numbers depend on your choice. The vector does not.*** This is the most important idea in elementary vector physics.

> [!tip] The vector is the arrow; the components are its shadow
> Imagine the vector as a real arrow held in space. Components are the shadows it casts on two perpendicular walls. Move the walls (rotate the axes) and the shadows change shape; the arrow itself is unchanged. *You can describe an arrow by its shadows, but the shadows don't define the arrow — the arrow defines the shadows.*

### The inclined-plane decomposition

The canonical worked example. A block of mass $m$ sits on a slope inclined at angle $\theta$ to the horizontal. Gravity pulls it down with weight $m\mathbf{g}$.

Two natural choices of axes:

1. **Horizontal/vertical** — the "world frame." In this frame the weight has components $(0, -mg)$. Simple. But the slope itself is at an awkward angle, and the *normal force* from the slope is at an awkward angle, and friction (along the slope) is at an awkward angle. Every force *except* gravity has both an $x$- and a $y$-component. Two equations, multiple unknowns each. Painful.
2. **Slope-aligned** — rotate the axes by $\theta$ so one axis runs *along the slope* and the other runs *perpendicular to the slope*. Now the normal force is purely along one axis, friction is purely along the other, but $m\mathbf{g}$ — which was simple in the world frame — splits into two components:
   - Along the slope (down-slope): $mg\sin\theta$
   - Perpendicular to the slope (into the slope): $mg\cos\theta$

![[vectors-inclined-plane-decomposition.svg]]

*Left: slope-aligned axes give clean components for the weight and trivial components for the normal and friction forces. The dotted parallelogram completes the vector-addition rectangle. Right: horizontal/vertical axes leave the weight clean but tangle every other force with the slope angle.*

The slope-aligned frame is *better* because almost every other force in the problem (normal $\mathbf{N}$, friction $\mathbf{f}$) already lives along those axes — only gravity has to be decomposed. The world-frame is *worse* because every force except gravity has to be decomposed. **Pick axes that match the geometry of the problem; decompose the awkward vector once and the equations will be tidy.**

The Foundations card stops here at the principle. The full worked μ = tan θ derivation for limiting equilibrium on a slope lives in [[Forces and Equilibrium]] §"Limiting equilibrium on a rough slope" — go there for the marks.

## Vector addition (refresher)

The mathematics-side [[Vectors]] card carries the full machinery. Here is the physics-side compact version, two equivalent geometric pictures:

1. **Start-to-end / triangle method.** To compute $\mathbf{a} + \mathbf{b}$: draw $\mathbf{a}$, then start $\mathbf{b}$ at the end of $\mathbf{a}$, then draw the resultant from the start of $\mathbf{a}$ to the end of $\mathbf{b}$. The three vectors form a triangle.
2. **Parallelogram method.** To compute $\mathbf{a} + \mathbf{b}$: draw both starting from the same point, complete the parallelogram, the resultant is the diagonal from the common start to the opposite corner. Equivalent to start-to-end because the parallelogram contains two copies of the triangle.

Cambridge 9702 §1.4 lists both methods. Most exam mark schemes will accept either — *some* questions explicitly call for the parallelogram law, in which case use it. For *calculation*, both reduce to: resolve each vector into components, add the components separately ($x$ with $x$, $y$ with $y$), then recombine using Pythagoras (for magnitude) and arctangent (for direction).

$$\mathbf{a} + \mathbf{b} \;=\; (a_x + b_x, \; a_y + b_y), \qquad |\mathbf{a}+\mathbf{b}| = \sqrt{(a_x+b_x)^2 + (a_y+b_y)^2}$$

For three or more vectors in equilibrium, the start-to-end method gives the **triangle of forces** (three vectors) or **polygon of forces** (more), in which the vectors close up into a closed shape because their sum is zero. This is the geometric statement of $\sum \mathbf{F} = \mathbf{0}$. Lami's theorem and the sine rule give algebraic shortcuts; see [[Forces and Equilibrium]] §"Triangle of forces and Lami's theorem."

> [!warning] Magnitude does NOT add unless vectors are parallel
> If $|\mathbf{a}| = 3$ and $|\mathbf{b}| = 4$, you cannot say $|\mathbf{a} + \mathbf{b}| = 7$. The resultant magnitude depends on the angle between them. Examples:
> - Same direction (angle 0°): $|\mathbf{a}+\mathbf{b}| = 7$
> - Perpendicular (90°): $|\mathbf{a}+\mathbf{b}| = \sqrt{3^2 + 4^2} = 5$
> - Opposite (180°): $|\mathbf{a}+\mathbf{b}| = 1$
>
> The magnitude is bounded: $\big| |\mathbf{a}| - |\mathbf{b}| \big| \le |\mathbf{a}+\mathbf{b}| \le |\mathbf{a}|+|\mathbf{b}|$. This is the **triangle inequality**, which has the same name and same content in geometry, real analysis, and physics — it lives [[Magnitude of a Vector (Vocab)]].

### Signed components and unit vectors

Choose east as positive. A 5 N force east and a 3 N force west sum to $+5+(-3)=+2$ N: 2 N east. The sign describes direction along the chosen axis; it is not an extra magnitude.

In three dimensions, write $\mathbf{F}=F_x\hat{\mathbf{i}}+F_y\hat{\mathbf{j}}+F_z\hat{\mathbf{k}}$, where each hatted basis vector has unit length along its axis. Add vectors by adding matching components. For position $\mathbf{r}=3\hat{\mathbf{i}}+4\hat{\mathbf{j}}$ metres, $r=5$ m and the dimensionless radial unit vector is $\hat{\mathbf{r}}=\mathbf{r}/r=(3/5)\hat{\mathbf{i}}+(4/5)\hat{\mathbf{j}}$. It preserves direction while stripping away length.

## Worked Example — the swimmer across the river

A swimmer can swim at $v_s = 1.2~\text{m·s}^{-1}$ in still water. They enter a river that flows east at $v_r = 0.5~\text{m·s}^{-1}$. They point themselves due north.

**(a) Velocity relative to the ground?** Vector addition of the swimmer's velocity (north) and the river's velocity (east):

$$\mathbf{v}_{\text{ground}} = \mathbf{v}_s + \mathbf{v}_r = (0.5, 1.2)~\text{m·s}^{-1}$$

Magnitude:

$$|\mathbf{v}_{\text{ground}}| = \sqrt{0.5^2 + 1.2^2} = \sqrt{1.69} = 1.30~\text{m·s}^{-1}$$

Direction: $\tan^{-1}(0.5/1.2) = 22.6°$ east of north. The swimmer makes the crossing faster than expected (1.30 vs 1.20 m·s⁻¹ "straight across" speed) but lands considerably downstream.

**(b) If the river is $30~\text{m}$ wide, how long does the crossing take and how far downstream do they land?**

Crossing time depends only on the *north* component of the swimmer's velocity (since the river is east-flowing — east motion doesn't help cross). North component of $\mathbf{v}_{\text{ground}}$ is $1.2~\text{m·s}^{-1}$ (the swimmer's own velocity; the river contributes nothing north). Time: $t = 30 / 1.2 = 25~\text{s}$.

Downstream displacement: east component of $\mathbf{v}_{\text{ground}}$ is $0.5~\text{m·s}^{-1}$, sustained for $25~\text{s}$. Distance east: $0.5 \times 25 = 12.5~\text{m}$.

**(c) If the swimmer wants to land directly across, at what angle should they point upstream?**

Now the *resultant* must point due north, which means the east component of the resultant must equal zero. The river contributes $+0.5$ east; the swimmer must contribute $-0.5$ east. The swimmer's speed is fixed at $1.2$. So $v_{s,\text{east}} = -1.2 \sin\alpha = -0.5$, giving $\sin\alpha = 0.5/1.2 = 0.417$, so $\alpha = 24.6°$ west of north. The resultant northward speed is then $v_{s,\text{north}} = 1.2 \cos\alpha = 1.2 \times 0.909 = 1.09~\text{m·s}^{-1}$ (slower than swimming straight across because some of the swimmer's effort now fights the current).

This is the canonical Cambridge / AP / IB exam scenario. **Same calculation pattern: choose axes (east-north here, slope-aligned in the inclined plane), decompose each vector, add componentwise.**

> [!tip] You have already solved this — in Breath of the Wild
> *The Legend of Zelda: Breath of the Wild* puts Link in rivers whose current pushes him downstream while he swims. To land where you actually want to go, you have to angle the analog stick *upstream* — pointing the swim direction at a calculated angle into the current, not at the target. The game's physics engine is running exactly the calculation in part (c): given the swimmer's max speed $v_s$ and the current $v_r$, solve $v_s \sin\alpha = v_r$ for the upstream angle, and the resultant velocity carries you straight across. Every BOTW player has *internalised* the vector triangle long before seeing it written down; the equation just labels the muscle memory. The same logic governs every river-crossing in every open-world game with a current — and every actual canoe trip, sailing tack, and aircraft crosswind landing.

![[vectors-river-crossing-aim.png]]

*Same river, same current, two different aims. **Left:** the traveller points straight across; the current bows the trajectory downstream to "actual arrival," well east of the target. **Right:** the traveller aims upstream by exactly the angle $\alpha$ where $v_s\sin\alpha = v_r$; the upstream component of swim cancels the current, the resultant points due north, and the trajectory goes straight to the target. The vector triangle inset in each panel makes the algebra explicit — the right-panel triangle has the "swim aim" arrow tilted upstream so that the resultant is vertical.*



## Common Mistakes

### 1. Treating a vector as just its magnitude

A student computing the resultant of three forces of magnitudes $4~\text{N}, 3~\text{N}, 5~\text{N}$ writes $|\mathbf{R}| = 4 + 3 + 5 = 12~\text{N}$. **Wrong** unless all three are parallel and same-direction. Direction has to be accounted for. The correct workflow is always: resolve each force into components along chosen axes, add the components, recombine. **No shortcut survives the angle problem.**

### 2. Thinking the components are "what's really there"

After decomposing $m\mathbf{g}$ into $mg\sin\theta$ and $mg\cos\theta$ on a slope, students sometimes conclude that the block now has *two* forces on it (the down-slope one and the perpendicular one) — and that the original weight has somehow been "used up." This is wrong: there is still *one* force, gravity. The two components are just a more useful **description** of that one force, chosen because the geometry is nicer. **Decomposition is a notational change, not a physical change.**

### 3. Picking the wrong axes

The whole point of axis choice is to make the problem easy. A student who insists on horizontal/vertical axes for an inclined-plane problem is solving a harder version of the question for no reward. The rule: **align axes with the dominant geometric direction of the problem.** Slope → axes along/perpendicular to slope. Circular motion → axes radial/tangential. Projectile under gravity → axes horizontal/vertical (because gravity is vertical, and that's the dominant direction).

### 4. Forgetting that both components have signs

After resolving, $F_x$ and $F_y$ are *signed* scalars. A force at $135°$ above the $+x$-axis has $F_x = -F\cos 45°$ (negative, because it points in the $-x$ direction). A student who treats components as always positive will add when they should subtract and end up with the wrong resultant. **Decompose, then watch the signs.**

### 5. Magnitude is never negative; components can be

The *magnitude* $|\mathbf{F}|$ is the length of the arrow — always non-negative. A *component* $F_x$ can be negative (the vector pointing in the $-x$ direction). Mixing these up — writing $|\mathbf{F}| = -3~\text{N}$ — is a sign of muddled thinking. Magnitude positive, component signed.

## Exam Notes

### Cambridge 9702 — §1.4

The 2028–30 syllabus requires distinguishing scalars from vectors and giving examples, adding and subtracting coplanar vectors, and representing a vector as two perpendicular components. Use a scale diagram or component calculation as appropriate to the question. An explicit instruction to use a particular method takes precedence. The syllabus does not guarantee a question on every paper or a fixed mark allocation.

### Cambridge 0625 — §1.1 Supplement

Know the scalar/vector distinction and the named examples: scalars include distance, speed, time, mass, energy and temperature; vectors include force, weight, velocity, acceleration, momentum, electric field strength and gravitational field strength. Determine the resultant of two perpendicular forces or velocities by calculation or a scale drawing. General oblique resolution is beyond this particular outcome.

### IB Physics — shared mathematical skills, SL and HL

The guide's “Skills in the study of physics”, pp. 29–30, explicitly requires identifying scalars/vectors, drawing labelled vectors, coplanar addition/subtraction of up to three vectors, scalar multiplication and resolution into two perpendicular components. These skills support A.1/A.2 and field topics; they are not an HL-only extension. A.4's rotational treatment explicitly does not require the vector nature of torque or angular momentum. Do not infer an examined formal vector treatment merely because an angular quantity appears in a topic title.

### AP Physics 1 — 1.1 and 1.5

1.1 explicitly requires scalar/vector descriptions, magnitude-proportional arrows, opposite signs for opposite one-dimensional directions, and vector sums. 1.5 develops two-dimensional components and motion. Representations and mathematical routines are different science-practice categories; vector content is specified in these topic outcomes, not a standalone “SP1 vector syllabus”. [[Projectile Motion]] supplies the motion application.

### AP Physics C: Mechanics — 1.1

The current framework also specifies Cartesian unit-vector notation, position vectors and radial unit vectors, component sums, and signed one-dimensional directions. The short notation example below makes those conventions explicit. Calculus enters later kinematics; it is not needed merely to add vectors.

### AP Physics 2 and AP Physics C: Electricity and Magnetism

Vectors remain working tools: the current frameworks explicitly require electric-field vectors and vector superposition (AP2 10.3; AP-C E&M 8.3). Potential is scalar and superposes as a signed scalar. A general vector introduction supports those topics but does not by itself complete their field physics.

### Scope boundary

None of these inspected school frameworks requires general tensor calculus. Beyond the named examples, physical quantities need not all be scalars or vectors: stress, for example, requires a tensor description. Other exam boards' exact vector requirements have not been audited here.

## Connections

- **Prerequisite:** [[Vectors]] — the mathematics-side companion carrying the full machinery (definition, magnitude, addition, component form, position vectors, scalar multiplication). This card is the physics application; that card is the underlying maths.
- **Prerequisite:** [[Magnitude of a Vector (Vocab)]] — the Pythagorean magnitude formula and the triangle inequality.
- **Prerequisite:** [[Physical Quantities and Units]] — the §1.4 row comes immediately after §1.1 + §1.2 in 9702; this card extends the choice-of-axes invariance idea introduced in the dimensional-homogeneity section.
- **Prerequisite:** [[Trigonometric Ratios]] — every component is $F\cos\theta$ or $F\sin\theta$. SOHCAHTOA is the tool.
- **Leads to:** [[Newton's Laws of Motion]] — N2 is a vector equation $\mathbf{F} = m\mathbf{a}$; every free-body diagram is the decomposition technique on this card applied to all forces simultaneously.
- **Leads to:** [[Forces and Equilibrium]] — the full inclined-plane worked example ($\mu = \tan\theta$ at the angle of repose) and the triangle-of-forces / Lami's theorem machinery for three-force equilibrium live there.
- **Leads to:** [[SUVAT]] — projectile motion is the canonical "decompose into horizontal and vertical" application, with the two motions evolving independently.
- **Leads to:** [[Linear Momentum]] — $\mathbf{p} = m\mathbf{v}$ is a vector; conservation of momentum is conservation of each component independently.
- **Mathematics bridges:** [[Vector Geometry]], [[3D Vectors and the Scalar Product]] — the next steps after planar vectors, leading into A-Level / IB Higher pure mathematics. Force decomposition in 3D is exactly the same technique with one more axis to add.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\mathbf{F}$ | `\mathbf{F}` | Bold vector — preferred in this vault |
| $\vec{F}$ | `\vec{F}` | Arrow vector — Chinese / IB convention |
| $\lvert\mathbf{F}\rvert$ | `\lvert\mathbf{F}\rvert` | Magnitude (always non-negative) |
| $F_x$, $F_y$ | `F_x, F_y` | Components — signed scalars |
| $\hat{\mathbf{n}}$ | `\hat{\mathbf{n}}` | Unit vector (magnitude exactly 1) |
| $\theta$ | `\theta` | Angle, usually between vector and reference axis |
| $\cos\theta$ | `\cos\theta` | Component along the axis the angle is measured from |
| $\sin\theta$ | `\sin\theta` | Component perpendicular to that axis |
| $\sum \mathbf{F}$ | `\sum \mathbf{F}` | Net force (vector sum) |
