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

The **torque** of a force $\mathbf{F}$ applied at a point with position vector $\mathbf{r}$ (measured from a chosen origin $O$) is the vector

$$\boxed{\;\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}, \qquad |\boldsymbol{\tau}| = rF\sin\theta = Fd\;}$$

where $\theta$ is the angle between $\mathbf{r}$ and $\mathbf{F}$, and $d = r\sin\theta$ is the **moment arm** (perpendicular distance from $O$ to the line of action of $\mathbf{F}$). The direction of $\boldsymbol{\tau}$ is perpendicular to $\mathbf r$ and $\mathbf F$, given by the right-hand rule (curl the fingers from $\mathbf{r}$ toward $\mathbf{F}$; the thumb points along $\boldsymbol{\tau}$). Units: newton-metres, $\text{N·m}$.

For a specified axis through $O$ with unit direction $\hat{\mathbf n}$, the turning component is $\tau_{\mathrm{axis}}=\hat{\mathbf n}\cdot(\mathbf r\times\mathbf F)$. In the usual planar problems, $\mathbf r$ and $\mathbf F$ lie perpendicular to that axis, so its magnitude is $Fd$.

Torque is the **rotational analogue of force**. A force changes a body's linear motion; a torque changes its rotational motion.

### Intuitive

Everyone has met torque through doors. To open a heavy door you push **far from the hinge** and **perpendicular to the door** — never near the hinge, never along the door toward or away from it. Three things make a force good at turning something:

1. **How hard you push** — the force $F$.
2. **How far from the pivot you push** — the distance $r$.
3. **The angle you push at** — only the part of the force *perpendicular* to the lever does any turning. Pushing straight toward the hinge ($\theta = 0$) does nothing; pushing square-on ($\theta = 90°$) does the most.

Multiply those together and you get $\tau = rF\sin\theta$. The $\sin\theta$ is the angle factor, and it is exactly why torque is a **cross product** rather than a dot product: it peaks when $\mathbf{r}$ and $\mathbf{F}$ are perpendicular and vanishes when they're parallel — the signature of $\mathbf{r}\times\mathbf{F}$ (see [[Cross Product]]).

### 中文锚点

推一扇重门时，你会自然地去推门把手附近，而不是紧挨着合页。同样使劲，离合页远一点就更容易把门推开；如果顺着门板朝合页挤，手上很用力，门却不怎么转。**力矩**说的就是这个力让门绕合页转动的本事有多大：不光看你用了多大力，还要看你推在哪里、朝哪个方向推。

## The naming bridge — "moment" vs "torque"

> [!warning] Same quantity, two English names — one Chinese word
> This trips up every student who takes Cambridge mechanics *and* a physics course at the same time.
>
> - **"Moment of a force"** — Cambridge A-Level Mathematics/Further, UK physics, [[Forces and Equilibrium]]. Usually used in a *statics* context ("take moments about the pivot").
> - **"Torque"** — physics generally, IB Physics, AP Physics, engineering. Usually used in a *dynamics* context ("the torque spins the wheel up").
>
> **They are the identical quantity**, $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$, magnitude $Fd$. Chinese sidesteps the whole mess with one word, **力矩**. Whenever a problem says "moment," mentally substitute "torque" and vice versa — there is no difference to learn, only a vocabulary swap.

## Bridge — from the 2D moment to the 3D vector torque

The statics half of this story already lives in [[Forces and Equilibrium]]: the scalar moment $\tau = Fd$, the anticlockwise-positive sign convention, the principle of moments, couples, and the strategic-pivot trick. The extension here is the **vector and dynamics view**. The two views line up exactly:

| 2D scalar moment (statics, [[Forces and Equilibrium]]) | 3D vector torque (vector form) |
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
| $\mathbf{r}$ | position vector | From the chosen origin/pivot to the point where $\mathbf{F}$ acts |
| $d = r\sin\theta$ | moment arm / lever arm | Perpendicular distance, origin to line of action |
| $\tau = rF\sin\theta$ | magnitude | $\text{N·m}$ — *never* joules (see misconception 3) |
| $\sum\boldsymbol{\tau} = \mathbf{0}$ | rotational equilibrium | The rotational form of Newton's first law |

## Key Facts / Properties

### 1. Torque is a cross product

Because $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$, everything proved in [[Cross Product]] applies directly:

- **Magnitude** $rF\sin\theta$ — maximal at $\theta = 90°$ (push square-on), zero at $\theta = 0°$ or $180°$ (push along the lever — a tug toward or away from the pivot can't rotate anything).
- **Direction** normal to the plane of $\mathbf r$ and $\mathbf F$ by the right-hand rule, so torque is an *axial vector* (pseudovector) — explored just below.
- **Anticommutativity** $\mathbf{r}\times\mathbf{F} = -\,\mathbf{F}\times\mathbf{r}$ — the order is $\mathbf{r}$ *then* $\mathbf{F}$; swapping them reverses the spin direction.

### Direction — and why torque is a "pseudovector"

The direction of $\boldsymbol{\tau}$ is the strangest thing about it. In a planar turning problem it points along the **rotation axis** — perpendicular to the plane of the force and lever — so the torque vector points in a direction where *nothing is actually moving*. That is the right-hand rule at work, inherited wholesale from [[Cross Product]].

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
| $\mathbf{F} = m\mathbf{a}$ | $\tau = I\alpha$ |
| momentum $\mathbf{p} = m\mathbf{v}$ | axial angular momentum $L_{\mathrm{axis}} = I\omega$ — see [[Angular Momentum]] |
| $\mathbf{F} = \dfrac{d\mathbf{p}}{dt}$ | $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$ |

Torque is the **cause** of changes in angular momentum. *How much* a body resists being spun up — the moment of inertia $I$ that turns $\tau = I\alpha$ from a shape into a number — is developed in [[Moment of Inertia]]. The deepest form, $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$ (the true rotational Newton's second law, and the home of conservation of angular momentum), is the third, [[Angular Momentum]].

### 4. Net torque and rotational equilibrium

The torques on a body add as vectors. A body is in **rotational equilibrium** when

$$\sum \boldsymbol{\tau} = \mathbf{0},$$

the rotational form of Newton's first law. In 2D this is the principle of moments — anticlockwise moments balance clockwise moments — developed with worked beam/ladder examples in [[Forces and Equilibrium]]. The powerful trick proved there carries over: **you may take torques about *any* axis**, so choose the axis that kills the most unknowns (a force through your chosen axis has zero moment arm and drops out).

### 5. A couple — torque with no net force

Two equal, opposite, parallel forces with different lines of action sum to $\mathbf{0}$ (no push) but produce a net torque (pure spin) of magnitude $Fs$, where $s$ is the perpendicular separation. A couple's torque is a **free vector** — it is the *same about every point*, because with zero net force there is no special pivot. Turning a tap with two fingers, or a steering wheel with two hands, is a couple. (The statics treatment is in [[Forces and Equilibrium]]; the free-vector fact is the vector-era sharpening.)

## Worked Examples

### Example 1 (foundational): the wrench

A mechanic pushes with $F = 80\ \text{N}$ at the end of a spanner $r = 0.25\ \text{m}$ long, at $\theta = 60°$ to the spanner.

*Trigger: force at a known angle to a lever. Tool: $\tau=rF\sin\theta$; keep the perpendicular force component.*

$$\tau = rF\sin\theta = (0.25)(80)\sin 60° = 20 \times 0.866 = 17.3\ \text{N·m}.$$

To get the *most* torque from the same push, hold the force at $90°$: $\tau_{\max} = (0.25)(80) = 20\ \text{N·m}$. Pushing at $60°$ wastes about 13% of the effort — the radial component $F\cos 60°$ just tries to bend or stretch the spanner, not turn the bolt.

### Example 2 (statics): the see-saw

A uniform plank pivots at its centre. A $30\ \text{N}$ weight sits $1.2\ \text{m}$ left of the pivot. Where must a $45\ \text{N}$ weight sit to balance?

*Trigger: a balanced plank and an unknown pivot reaction. Tool: $\sum\tau=0$ about the pivot, eliminating that reaction and the plank’s own weight.*

$$\underbrace{30 \times 1.2}_{\text{anticlockwise}} = \underbrace{45 \times x}_{\text{clockwise}} \;\Rightarrow\; x = \frac{36}{45} = 0.80\ \text{m to the right.}$$

### Example 3 (constructed vector enrichment): full 3D torque

A force $\mathbf{F} = (0, 0, 12)\ \text{N}$ acts at $\mathbf{r} = (0.4, 0.3, 0)\ \text{m}$ from the chosen origin.

*Trigger: three-dimensional components are supplied. Tool: $\mathbf r\times\mathbf F$, evaluated component by component.*

$$\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F} = \det\!\begin{pmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ 0.4&0.3&0\\ 0&0&12\end{pmatrix} = (0.3\cdot12 - 0)\,\mathbf{i} - (0.4\cdot12 - 0)\,\mathbf{j} + 0\,\mathbf{k} = (3.6,\,-4.8,\,0)\ \text{N·m}.$$

Magnitude $|\boldsymbol{\tau}| = \sqrt{3.6^2 + 4.8^2} = 6.0\ \text{N·m}$, lying in the $xy$-plane (perpendicular to the force, as every cross product must be).

## Common Misconceptions (Teaching Notes)

### 1. "Moment and torque are different quantities"

Students meeting “moment” in mechanics and “torque” in physics sometimes assume they are learning two quantities.

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

### Cambridge 0625 — §1.5.2 Turning effect of forces

**Core (Papers 1/3):** describe everyday turning effects; use moment = force × perpendicular distance; balance one force on each side of a pivot; state that equilibrium needs zero resultant force and moment. **Supplement (Papers 2/4):** extend the balance to other situations, including several forces per side, and describe an experiment demonstrating zero resultant moment. No vector cross-product treatment is required. [[Forces and Equilibrium]] is the main statics companion.

### Cambridge 9702 — §4.1 and §4.2 (AS content, Papers 1/2)

§4.1 names centre of gravity, moments, couples and torque of a couple; §4.2 carries the principle of moments and equilibrium. Draw force lines and use perpendicular distances. Rotational dynamics with $\tau=I\alpha$ is not a prescribed 9702 topic. “Torque” in this syllabus does not imply the full university vector treatment.

### Cambridge 9231 — Further Mechanics §3.2 (Paper 3)

Moments and equilibrium of a rigid body under **coplanar** forces, including toppling and sliding. The syllabus explicitly says that understanding the vector nature of moments is not required. The three-dimensional determinant example above is enrichment, not a required 9231 method. Moment of inertia and rotational dynamics are not listed in this Further Mechanics syllabus.

### Pearson Edexcel IAL Mathematics/Further Mathematics — M1/M2/M3

**M1 §6.1:** moments and equilibrium with coplanar parallel forces. **M2 §5.1–5.2:** parallel and non-parallel coplanar forces, including rods and ladders. **M3 §5.2:** simple rigid-body equilibrium, including suspension and placement on a plane. Select a pivot that eliminates inconvenient reactions, while keeping the separate force-balance equations. These requirements concern statics; do not infer a rotational-dynamics requirement from the word “Further”.

### IB Physics — A.4 Rigid body mechanics, HL only

Torque $\tau=Fr\sin\theta$, rotational equilibrium, and angular acceleration under an unbalanced torque are explicit. The guide says the **vector nature need not be addressed**, but clockwise/anticlockwise sense must be included. $I$, $\tau=I\alpha$ and angular momentum are also HL outcomes, developed in [[Moment of Inertia]] and [[Angular Momentum]]. There is no SL content in A.4.

### AP Physics 1 and AP Physics C: Mechanics — Topic 5.3

Both require torques, lever arms and diagrams showing **where** forces act. Physics 1 uses the algebraic magnitude and rotation sense. C: Mechanics explicitly gives $\boldsymbol\tau=\mathbf r\times\mathbf F$, its magnitude and the right-hand rule; its Topic 5.3 does not prescribe determinant expansion as a required technique. Both proceed to rotational equilibrium (5.5) and Newton's second law for rotation (5.6). The latter is not exclusive to AP C. The brief rotational-work result below supports Unit 6 but is not a complete work-and-energy treatment.

### Where this treatment is not prescribed

**Cambridge 9709 Paper 4** treats particles and does not prescribe moments of rigid bodies. **IB Physics SL** has no A.4 rigid-body content. **AP Physics 2 and AP Physics C: Electricity and Magnetism** do not have a standalone rigid-body torque unit in their current frameworks; mechanics and qualitative turning effects can still supply context for electromagnetism. The dipole formula below is enrichment here, not a claim that those courses prescribe it. Pseudovectors and general three-dimensional determinant calculations are mathematical extensions beyond the scalar statics requirements above.

## Connections

- **Mathematical prerequisite:** [[Cross Product]] — torque *is* a cross product; the magnitude rule, right-hand rule, and pseudovector nature all come from there.
- **Prerequisite / statics home:** [[Forces and Equilibrium]] — the scalar moment, principle of moments, couples, and strategic-pivot trick; the vector formulation lifts that to a vector and into dynamics.
- **Prerequisite:** [[Vectors in Physics]] — torque sits in the vector column of the scalar/vector taxonomy. [[Newton's Laws of Motion]] — torque is the rotational analogue of the force in $\mathbf{F}=m\mathbf{a}$.
- **Next in the trio:** [[Moment of Inertia]] — the rotational mass $I$ that makes $\tau=I\alpha$ a number; then [[Angular Momentum]] — $\mathbf{L}=\mathbf{r}\times\mathbf{p}$, $\boldsymbol{\tau}=\dfrac{d\mathbf{L}}{dt}$, and conservation.
- **Application:** [[Simple Harmonic Motion]] — the pendulum's restoring torque $\tau = -mgL\sin\theta$ is the gravitational torque defined above; that derivation currently borrows $\tau$ and $I$ and points here for the justification.

---

## Beyond Syllabus

### The truer definition: $\boldsymbol{\tau} = d\mathbf{L}/dt$

$\tau = I\alpha$ is the fixed-axis form for a rigid body with constant $I$; $\tau$ is the torque component along that axis. About a fixed inertial origin, the exact law for the net external torque is $\boldsymbol{\tau} = \dfrac{d\mathbf{L}}{dt}$ — torque is the *rate of change of angular momentum*, just as force is the rate of change of momentum. When $I$ can change (a figure skater pulling in their arms), only the $d\mathbf{L}/dt$ form survives, and it is what makes conservation of angular momentum and gyroscopic precession work. Full story in [[Angular Momentum]].

### Torque in electromagnetism — the motor

A current loop with magnetic moment $\mathbf{m}$ in a field $\mathbf{B}$ feels a torque $\boldsymbol{\tau} = \mathbf{m}\times\mathbf{B}$ — the same cross-product shape, and the reason every electric **motor** turns. It is a close cousin of the [[Lorentz Force]] $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, and the alignment torque on a dipole appears throughout [[Maxwell's Equations]]-era electromagnetism (compass needles, NMR/MRI spins, electric dipoles in fields). The right-hand rule you use for the motor torque is the same orientation convention as for a mechanical lever.

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
| $\tau=I\alpha$ | `\tau=I\alpha` | Newton's 2nd law for rotation fixed-axis form |
| $\boldsymbol{\tau}=\dfrac{d\mathbf{L}}{dt}$ | `\dfrac{d\mathbf{L}}{dt}` | Exact form — rate of change of angular momentum |
| $\boldsymbol{\tau}=\mathbf{m}\times\mathbf{B}$ | `\mathbf{m}\times\mathbf{B}` | Torque on a magnetic dipole (motor) |
