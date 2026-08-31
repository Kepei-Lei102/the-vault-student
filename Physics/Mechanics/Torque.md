---
chinese: 力矩 (lìjǔ)
prerequisites:
  - "[[Cross Product]]"
  - "[[Forces and Equilibrium]]"
  - "[[Vectors in Physics]]"
  - "[[Newton's Laws of Motion]]"
leads_to:
  - "[[Centre of Mass]]"
  - "[[Moment of Inertia]]"
  - "[[Angular Momentum]]"
  - "[[Laws and Theorems]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - level/A-Level
  - level/pre-AP
  - curriculum/Cambridge-9702
  - curriculum/A-Level-Further
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9702-4-1
  - syllabus/IB-Physics-A-4-1
  - syllabus/AP-Physics-1-5-3
  - syllabus/AP-Physics-C-Mech-5-3
  - syllabus/9231-3-2
  - type/deep
  - type/definition
  - type/theorem
  - notation/tau
  - notation/cross-product
  - notation/moment-arm
  - misconception/torque-and-moment-are-different
  - misconception/use-full-force-not-perpendicular
  - misconception/torque-newton-metres-are-joules
  - misconception/torque-needs-the-real-pivot
---

# Torque 力矩

## Definition

### Formal

The **torque** of a force $\mathbf{F}$ applied at a point with position vector $\mathbf{r}$ (measured from the chosen axis or pivot) is the vector

$$\boxed{\;\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}, \qquad |\boldsymbol{\tau}| = rF\sin\theta = Fd\;}$$

where $\theta$ is the angle between $\mathbf{r}$ and $\mathbf{F}$, and $d = r\sin\theta$ is the **moment arm** (perpendicular distance from the axis to the line of action of $\mathbf{F}$). The direction of $\boldsymbol{\tau}$ is along the rotation axis, given by the right-hand rule (curl the fingers from $\mathbf{r}$ toward $\mathbf{F}$; the thumb points along $\boldsymbol{\tau}$). Units: newton-metres, $\text{N·m}$.

Torque is the **rotational analogue of force**. A force changes a body's linear motion; a torque changes its rotational motion.

### Intuitive

Everyone has met torque through doors. To open a heavy door you push **far from the hinge** and **perpendicular to the door** — never near the hinge, never along the door toward or away from it. Three things make a force good at turning something:

1. **How hard you push** — the force $F$.
2. **How far from the pivot you push** — the distance $r$.
3. **The angle you push at** — only the part of the force *perpendicular* to the lever does any turning. Pushing straight toward the hinge ($\theta = 0$) does nothing; pushing square-on ($\theta = 90°$) does the most.

Multiply those together and you get $\tau = rF\sin\theta$. The $\sin\theta$ is the angle factor, and it is exactly why torque is a **cross product** rather than a dot product: it peaks when $\mathbf{r}$ and $\mathbf{F}$ are perpendicular and vanishes when they're parallel — the signature of $\mathbf{r}\times\mathbf{F}$ (see [[Cross Product]]).

### 中文锚点

**力矩**（lìjǔ）：力使物体绕某轴**转动**的本领。定义 $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$，大小 $\tau = rF\sin\theta = Fd$，其中 $d = r\sin\theta$ 是**力臂**（lìbì，pivot 到力作用线的垂直距离）。方向由**右手定则**（yòushǒu dìngzé）决定，沿转动轴。

**核心直觉（开门）**：开一扇重门，你会推在**离合页最远**的地方，而且**垂直于门面**推。三个因素：力多大、离轴多远、推的角度——只有**垂直分量**才产生转动效果。三者相乘就是 $\tau = rF\sin\theta$。

**一个重要的语言陷阱**：英文里**同一个量有两个名字**——剑桥数学/力学和英式物理叫 **moment**（"moment of a force"，力矩），美式物理 / IB / AP 叫 **torque**。**它们完全是同一个东西。** 中文只有一个干净的词：**力矩**。看到 moment 或 torque，脑子里都换成 $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$ 就行。平动（translation）的因是力 $\mathbf{F}$；转动（rotation）的因是力矩 $\boldsymbol{\tau}$。

## The naming bridge — "moment" vs "torque"

> [!warning] Same quantity, two English names — one Chinese word
> This trips up every student who takes Cambridge mechanics *and* a physics course at the same time.
>
> - **"Moment of a force"** — Cambridge A-Level Mathematics/Further, UK physics, [[Forces and Equilibrium]]. Usually used in a *statics* context ("take moments about the pivot").
> - **"Torque"** — physics generally, IB Physics, AP Physics, engineering. Usually used in a *dynamics* context ("the torque spins the wheel up").
>
> **They are the identical quantity**, $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$, magnitude $Fd$. Chinese sidesteps the whole mess with one word, **力矩**. Whenever a problem says "moment," mentally substitute "torque" and vice versa — there is no difference to learn, only a vocabulary swap.

## Bridge — from the 2D moment to the 3D vector torque

The statics half of this story already lives in [[Forces and Equilibrium]]: the scalar moment $\tau = Fd$, the anticlockwise-positive sign convention, the principle of moments, couples, and the strategic-pivot trick. This card is the **vector and dynamics upgrade**. The two views line up exactly:

| 2D scalar moment (statics, [[Forces and Equilibrium]]) | 3D vector torque (this card) |
|---|---|
| $\tau = Fd = Fr\sin\theta$, a signed number | $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$, a vector |
| Sign: $+$ anticlockwise, $-$ clockwise (a convention) | Direction: along the axis by the right-hand rule (built-in) |
| "anticlockwise/clockwise" in the plane of the page | the $\pm z$-component of $\boldsymbol{\tau}$ when the action is in the $xy$-plane |
| Used to balance beams, ladders, see-saws | Used for spin-up, gyroscopes, the full rotational $F=ma$ |

So the familiar $+$/$-$ sign of the school moment is not a separate idea — it is what the cross product's direction *collapses to* when everything happens in one plane. Step into 3D and the sign grows into a full axis vector.

## Notation

| Symbol | Read as | Notes |
|---|---|---|
| $\boldsymbol{\tau}$ | "tau" — torque | Vector. Some UK texts write $M$ or $G$ for moment |
| $\mathbf{r}$ | position vector | From the chosen axis/pivot to the point where $\mathbf{F}$ acts |
| $d = r\sin\theta$ | moment arm / lever arm | Perpendicular distance, axis to line of action |
| $\tau = rF\sin\theta$ | magnitude | $\text{N·m}$ — *never* joules (see misconception 3) |
| $\sum\boldsymbol{\tau} = \mathbf{0}$ | rotational equilibrium | The rotational form of Newton's first law |

## Key Facts / Properties

### 1. Torque is a cross product

Because $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$, everything proved in [[Cross Product]] applies directly:

- **Magnitude** $rF\sin\theta$ — maximal at $\theta = 90°$ (push square-on), zero at $\theta = 0°$ or $180°$ (push along the lever — a tug toward or away from the pivot can't rotate anything).
- **Direction** along the axis by the right-hand rule, so torque is an *axial vector* (pseudovector) — explored just below.
- **Anticommutativity** $\mathbf{r}\times\mathbf{F} = -\,\mathbf{F}\times\mathbf{r}$ — the order is $\mathbf{r}$ *then* $\mathbf{F}$; swapping them reverses the spin direction.

### Direction — and why torque is a "pseudovector"

The direction of $\boldsymbol{\tau}$ is the strangest thing about it. It points along the **rotation axis** — perpendicular to the plane everything is spinning in — so the torque vector points in a direction where *nothing is actually moving*. That is the right-hand rule at work, inherited wholesale from [[Cross Product]].

![[torque-direction-pseudovector.svg|697]]
*Left: a spin in the plane of the page gives a torque pointing straight out of the page, along the axis. Right: the mirror test. Reflect the spinning wheel and its rotation sense reverses, so the right-hand rule sends $\boldsymbol{\tau}$ from $\odot$ (out of page) to $\otimes$ (into page) — yet a genuine "polar" vector like a velocity $\mathbf{v}$ reflects the ordinary way. The torque vector picks up an **extra sign flip** under reflection that true vectors don't.*

That extra flip is exactly what **pseudovector** (or *axial vector*) means: a quantity that rotates like a vector but gains an opposite sign under reflection. Torque, angular velocity, angular momentum, and magnetic field are all pseudovectors — and every one of them is built from a cross product or a rotation sense. It changes nothing in ordinary calculations, but it is a real fingerprint of how the quantity is made: anything defined by $\mathbf{a}\times\mathbf{b}$ from two true vectors comes out a pseudovector (the same point flagged in [[Cross Product]]). It is also why a mirror image of a spinning gyroscope, taken literally, would disobey the naive reflection of its spin arrow.

### 2. Two ways to read the moment arm

The product $rF\sin\theta$ can be grouped two ways, and both are useful in problems:

$$\tau = \underbrace{(r\sin\theta)}_{\text{moment arm }d}\,F = r\,\underbrace{(F\sin\theta)}_{\text{perpendicular force}}.$$

Either *slide the force along its line of action to find the perpendicular distance* $d$ from the pivot, or *resolve the force into perpendicular and radial parts* and keep only the perpendicular one. Same answer; pick whichever the diagram makes easier.

![[torque-moment-arm.svg]]
*The two readings of $\tau = rF\sin\theta$. Resolve $\mathbf{F}$ at its point of application into a perpendicular part $F\sin\theta$ (green — the only part that turns) and a radial part $F\cos\theta$ (grey — pulls along the lever, turns nothing). Or extend the line of action of $\mathbf{F}$ and drop a perpendicular from the axis $O$ to it: that perpendicular distance is the moment arm $d = r\sin\theta$ (amber). Both groupings give the same torque, directed out of the page by the right-hand rule.*

### 3. Torque is the rotational analogue of force — the analogy that runs the whole trio

Every linear quantity has a rotational twin, and the laws have the same shape:

| Linear (translation) | Rotational (rotation) |
|---|---|
| force $\mathbf{F}$ | torque $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$ |
| mass $m$ (resistance to $\mathbf{a}$) | moment of inertia $I$ — see [[Moment of Inertia]] |
| acceleration $\mathbf{a}$ | angular acceleration $\alpha$ |
| $\mathbf{F} = m\mathbf{a}$ | $\boldsymbol{\tau} = I\alpha$ |
| momentum $\mathbf{p} = m\mathbf{v}$ | angular momentum $\mathbf{L} = I\boldsymbol{\omega}$ — see [[Angular Momentum]] |
| $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$ | $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$ |

This card owns the **cause** (torque). *How much* a body resists being spun up — the moment of inertia $I$ that turns $\boldsymbol{\tau} = I\alpha$ from a shape into a number — is the next card, [[Moment of Inertia]]. The deepest form, $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$ (the true rotational Newton's second law, and the home of conservation of angular momentum), is the third, [[Angular Momentum]].

### 4. Net torque and rotational equilibrium

The torques on a body add as vectors. A body is in **rotational equilibrium** when

$$\sum \boldsymbol{\tau} = \mathbf{0},$$

the rotational form of Newton's first law. In 2D this is the principle of moments — anticlockwise moments balance clockwise moments — developed with worked beam/ladder examples in [[Forces and Equilibrium]]. The powerful trick proved there carries over: **you may take torques about *any* axis**, so choose the axis that kills the most unknowns (a force through your chosen axis has zero moment arm and drops out).

### 5. A couple — torque with no net force

Two equal, opposite, parallel forces with different lines of action sum to $\mathbf{0}$ (no push) but produce a net torque (pure spin) of magnitude $Fs$, where $s$ is the perpendicular separation. A couple's torque is a **free vector** — it is the *same about every point*, because with zero net force there is no special pivot. Turning a tap with two fingers, or a steering wheel with two hands, is a couple. (The statics treatment is in [[Forces and Equilibrium]]; the free-vector fact is the vector-era sharpening.)

## Worked Examples

### Example 1 (foundational): the wrench

A mechanic pushes with $F = 80\ \text{N}$ at the end of a spanner $r = 0.25\ \text{m}$ long, at $\theta = 60°$ to the spanner.

$$\tau = rF\sin\theta = (0.25)(80)\sin 60° = 20 \times 0.866 = 17.3\ \text{N·m}.$$

To get the *most* torque from the same push, hold the force at $90°$: $\tau_{\max} = (0.25)(80) = 20\ \text{N·m}$. Pushing at $60°$ wastes about 13% of the effort — the radial component $F\cos 60°$ just tries to bend or stretch the spanner, not turn the bolt.

### Example 2 (statics): the see-saw

A uniform plank pivots at its centre. A $30\ \text{N}$ weight sits $1.2\ \text{m}$ left of the pivot. Where must a $45\ \text{N}$ weight sit to balance?

Take torques about the pivot (the plank's own weight acts *at* the pivot, so it drops out — strategic axis choice):

$$\underbrace{30 \times 1.2}_{\text{anticlockwise}} = \underbrace{45 \times x}_{\text{clockwise}} \;\Rightarrow\; x = \frac{36}{45} = 0.80\ \text{m to the right.}$$

### Example 3 (vector, AP-C / 9231): full 3D torque

A force $\mathbf{F} = (0, 0, 12)\ \text{N}$ acts at $\mathbf{r} = (0.4, 0.3, 0)\ \text{m}$ from the axis. Then

$$\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F} = \det\!\begin{pmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ 0.4&0.3&0\\ 0&0&12\end{pmatrix} = (0.3\cdot12 - 0)\,\mathbf{i} - (0.4\cdot12 - 0)\,\mathbf{j} + 0\,\mathbf{k} = (3.6,\,-4.8,\,0)\ \text{N·m}.$$

Magnitude $|\boldsymbol{\tau}| = \sqrt{3.6^2 + 4.8^2} = 6.0\ \text{N·m}$, lying in the $xy$-plane (perpendicular to the force, as every cross product must be).

## Common Misconceptions (Teaching Notes)

### 1. "Moment and torque are different quantities"

Students taking 9709/9231 mechanics ("moment") and a physics course ("torque") assume they're learning two things.

**Fix.** Write $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$ once and label it with *both* English words and the Chinese 力矩. One quantity, two names, one symbol.

### 2. Using the full force (or full distance) instead of the perpendicular part

Computing $\tau = rF$ when the force is at an angle, forgetting the $\sin\theta$.

**Fix.** Always ask "what is the perpendicular distance from the axis to the line of action?" — that's $d = r\sin\theta$. Or resolve the force and keep only the component at right angles to $\mathbf{r}$. If $\mathbf{r}$ and $\mathbf{F}$ are parallel, the torque is *zero*, no matter how large the force.

### 3. Treating N·m as joules

Torque has units $\text{N·m}$, identical-looking to the joule ($1\ \text{J} = 1\ \text{N·m}$ of *energy*). They are physically different — torque is a turning effect, energy is a capacity to do work.

**Fix.** Report torque in $\text{N·m}$, never $\text{J}$. The deeper reason they differ: energy is the *dot* product $\mathbf{F}\cdot\mathbf{d}$ (force along the motion), while torque is the *cross* product $\mathbf{r}\times\mathbf{F}$ (force across the lever) — different products of force and length, so different physical meaning despite identical units.

### 4. Thinking torque needs the "real" pivot

Students believe torque is only defined about the physical hinge.

**Fix.** Torque is defined about *any* axis you choose — the value changes with the choice, but the physics is consistent. For equilibrium ($\sum\boldsymbol{\tau} = \mathbf{0}$) you exploit this freedom: pick the axis that eliminates the forces you don't care about.

## Exam Notes

> Torque is **not** on Cambridge 9709 (Paper 4 Mechanics is particle-only — "vector notation will not be used", and extended bodies are modelled as particles, so moments never appear). It is also not on plain IB AA — there the object is the *mathematical* [[Cross Product]]. Below are the courses where torque is examined as physics.

### Cambridge 9702 (A-Level Physics)

**§4.1 — turning effects of forces:** moment of a force, couple, torque of a couple, and the principle of moments. This is the statics treatment, shared with [[Forces and Equilibrium]] (its primary home). 9702 stops at statics — it does **not** examine rotational dynamics ($\boldsymbol{\tau} = I\alpha$), which is Further/IB-HL/AP-C material.

### Cambridge 9231 (A-Level Further Mathematics)

**Further Mechanics, §3.2 — Equilibrium of a rigid body:** moments of coplanar forces, three-force problems, toppling vs sliding. That's where the torque/moment of a force lives on 9231. The *rotational-dynamics* extension (moment of inertia, $\boldsymbol{\tau}=I\alpha$, angular momentum) is **not** on Cambridge 9231 — its Further Mechanics is statics-and-particle-dynamics only — nor on 9702; those companions ([[Moment of Inertia]], [[Angular Momentum]]) are Edexcel/AQA Further + IB-Physics-HL + AP-C material.

### IB Physics (A.4.1 — *HL only*)

Rigid body mechanics is HL-only. **A.4.1:** torque $\tau = Fr\sin\theta$, rotational equilibrium $\sum\tau = 0$, and couples — exactly this card. A.4.2–A.4.4 (angular kinematics, $I$, $\boldsymbol{\tau}=I\alpha$, angular momentum) are the rest of the trio.

### AP Physics 1 (Unit 5.3) & AP Physics C: Mechanics (Unit 5.3)

Both list **5.3 Torque** as a standalone topic; AP-C writes it explicitly as $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$ and expects the vector/determinant computation. Both courses then build rotational equilibrium (5.5) and Newton's second law for rotation $\boldsymbol{\tau}=I\alpha$ (AP-C 5.6) on top — the next card.

## Connections

- **Mathematical prerequisite:** [[Cross Product]] — torque *is* a cross product; the magnitude rule, right-hand rule, and pseudovector nature all come from there.
- **Prerequisite / statics home:** [[Forces and Equilibrium]] — the scalar moment, principle of moments, couples, and strategic-pivot trick; this card lifts that to a vector and into dynamics.
- **Prerequisite:** [[Vectors in Physics]] — torque sits in the vector column of the scalar/vector taxonomy. [[Newton's Laws of Motion]] — torque is the rotational analogue of the force in $\mathbf{F}=m\mathbf{a}$.
- **Next in the trio:** [[Moment of Inertia]] — the rotational mass $I$ that makes $\boldsymbol{\tau}=I\alpha$ a number; then [[Angular Momentum]] — $\mathbf{L}=\mathbf{r}\times\mathbf{p}$, $\boldsymbol{\tau}=\dfrac{d\mathbf{L}}{dt}$, and conservation.
- **Application:** [[Simple Harmonic Motion]] — the pendulum's restoring torque $\tau = -mgL\sin\theta$ is the gravitational torque this card defines; that derivation currently borrows $\tau$ and $I$ and points here for the justification.

---

## Beyond Syllabus

### The truer definition: $\boldsymbol{\tau} = d\mathbf{L}/dt$

$\boldsymbol{\tau} = I\alpha$ is the beginner's form and assumes $I$ is constant. The exact law is $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$ — torque is the *rate of change of angular momentum*, just as force is the rate of change of momentum. When $I$ can change (a figure skater pulling in their arms), only the $d\mathbf{L}/dt$ form survives, and it is what makes conservation of angular momentum and gyroscopic precession work. Full story in [[Angular Momentum]].

### Torque in electromagnetism — the motor

A current loop with magnetic moment $\mathbf{m}$ in a field $\mathbf{B}$ feels a torque $\boldsymbol{\tau} = \mathbf{m}\times\mathbf{B}$ — the same cross-product shape, and the reason every electric **motor** turns. It is a close cousin of the [[Lorentz Force]] $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, and the alignment torque on a dipole appears throughout [[Maxwell's Equations]]-era electromagnetism (compass needles, NMR/MRI spins, electric dipoles in fields). The right-hand rule you use for the motor torque is the very same orientation convention as this card's.

### Why torque is the right "rotational cause" — it couples to angle

Why $\mathbf{r}\times\mathbf{F}$ and not some other combination? Because it is exactly the quantity that does **rotational work**: turning through a small angle $d\theta$ under torque $\tau$ does work $dW = \tau\, d\theta$ (the rotational mirror of $dW = F\,dx$). Power delivered is $P = \tau\omega$ — the rotational version of $P = Fv$, and how engine torque-and-RPM curves become horsepower. Torque is precisely the force-quantity that energy-accounting demands for rotation.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\boldsymbol{\tau}$ | `\boldsymbol{\tau}` | Torque vector |
| $\mathbf{r}\times\mathbf{F}$ | `\mathbf{r}\times\mathbf{F}` | Definition of torque |
| $rF\sin\theta$ | `rF\sin\theta` | Magnitude |
| $d = r\sin\theta$ | `d = r\sin\theta` | Moment arm |
| $\sum\boldsymbol{\tau}=\mathbf{0}$ | `\sum\boldsymbol{\tau}=\mathbf{0}` | Rotational equilibrium |
| $\boldsymbol{\tau}=I\alpha$ | `\boldsymbol{\tau}=I\alpha` | Newton's 2nd law for rotation (next card) |
| $\boldsymbol{\tau}=\dfrac{d\mathbf{L}}{dt}$ | `\dfrac{d\mathbf{L}}{dt}` | Exact form — rate of change of angular momentum |
| $\boldsymbol{\tau}=\mathbf{m}\times\mathbf{B}$ | `\mathbf{m}\times\mathbf{B}` | Torque on a magnetic dipole (motor) |
