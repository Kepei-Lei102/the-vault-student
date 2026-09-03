---
chinese: 胡克定律 (Húkè dìnglǜ)
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Work, Energy and Power]]"
  - "[[Differentiation]]"
  - "[[Maclaurin Series]]"
  - "[[Vectors]]"
  - "[[Stories/Newton vs Hooke]]"
leads_to:
  - "[[Simple Harmonic Motion]]"
  - "[[Stress, Strain and Young Modulus]]"
  - "[[Waves I: The Wave Equation]]"
  - "[[The Quantum Harmonic Oscillator]]"
  - "[[Stories/The Pendulum Story]]"
  - "[[The Pendulum Story]]"
  - "[[Circular Motion]]"
  - "[[Elastic Strings and Springs]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - domain/oscillations
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9702-6-2
  - syllabus/0625-1-5
  - syllabus/IB-Physics-A-2-2
  - syllabus/IB-Physics-C-1-1
  - syllabus/AP-Physics-1-2-8
  - syllabus/AP-Physics-1-7-1
  - syllabus/AP-Physics-1-7-2
  - syllabus/AP-Physics-C-Mech-2-8
  - syllabus/AP-Physics-C-Mech-7-1
  - syllabus/AP-Physics-C-Mech-7-2
  - syllabus/9231-3-4
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/F-equals-kx
  - notation/spring-constant
  - notation/elastic-PE
  - misconception/hookes-law-is-a-property-of-springs
  - misconception/k-depends-only-on-material
  - misconception/sign-of-restoring-force
  - misconception/elastic-limit-equals-breaking-point
---

# Hooke's Law for Springs 胡克定律

## Definition

**Hooke's Law** says that when you stretch or compress a spring by a small displacement $x$ from its natural length, the spring pulls or pushes back with a force proportional to that displacement and directed *back toward equilibrium*:

$$\boxed{\; F \;=\; -kx \;}$$

The quantities:

- $F$ — the restoring force exerted **by the spring on whatever is stretching it**. Newtons.
- $x$ — the **extension** (or compression, if negative): the displacement from the spring's natural, unloaded length. Metres.
- $k$ — the **spring constant** or **stiffness**. Newtons per metre, $\text{N m}^{-1}$. Positive.
- The minus sign — the force is *opposite* to the displacement. Pull right, spring pulls left. Push down, spring pushes up.

> [!info] Sign-convention warning
> Cambridge syllabuses (9702 §6.2, 0625 §1.5) write Hooke's Law as $F = kx$ — relating the *magnitude* of the applied force to the *magnitude* of the extension. The minus sign disappears because both quantities are taken as positive scalars.
>
> IB Physics, AP Physics, and every dynamics treatment beyond the first chapter write $F = -kx$ — the *vector* statement, with $F$ now the **restoring force exerted by the spring** and $x$ the signed displacement. **This is the version we will use everywhere except the formula-sheet section**, because the minus sign is the entire reason oscillations happen at all.

### 中文锚点

**胡克定律 (Húkè dìnglǜ)** = 弹簧 (或任何线性弹性系统) 被拉伸或压缩时，**恢复力与位移成正比、方向相反**。

| English | 中文 | 数学 |
|---|---|---|
| Extension | 伸长量 / 位移 (shēncháng liàng) | $x$ |
| Restoring force | 恢复力 (huīfù lì) | $F = -kx$ |
| Spring constant / stiffness | 弹簧常数 / 劲度系数 (jìndù xìshù) | $k > 0$, 单位 $\text{N m}^{-1}$ |
| Elastic potential energy | 弹性势能 (tánxìng shìnéng) | $\tfrac{1}{2} k x^2$ |
| Elastic limit | 弹性极限 (tánxìng jíxiàn) | 弹簧超过此点后不再服从 $F = -kx$ |
| Equilibrium (natural length) | 自然长度 / 平衡位置 (zìrán chángdù / pínghéng wèizhi) | $x = 0$ |

中文物理早就介绍过 $F = kx$，但**英语物理体系把这条定律的地位看得比中国课本高得多** —— 它不只是"弹簧的性质"，而是**所有"靠近平衡位置的小振动"的统一形式**。本卡的核心任务，就是把"为什么宇宙中所有的振动看起来都像弹簧"讲清楚。

---

## Why the minus sign is the whole point

Forget springs for a moment. Imagine a ball resting at the bottom of a smooth bowl. Nudge it a little to the left. What does the bowl do?

It pushes the ball back to the right — *toward where it came from*. Nudge it to the right; the bowl pushes left. The bowl provides a **restoring force**: a force that always points back toward equilibrium, regardless of which side the displacement is on.

That sign-flipping property — "displacement to the right ⇒ force to the left" — is exactly what the minus sign in $F = -kx$ encodes. It's the difference between:

- A ball in a bowl (stable; oscillates if disturbed)
- A ball balanced on top of an inverted bowl (unstable; runs away if disturbed)

> [!tip] Diagnostic: stable vs unstable
> Given a force law $F(x)$, equilibrium is wherever $F(x_0) = 0$. Disturb the body by a small $\delta x$. If the force that appears points *back toward* $x_0$ (sign opposite to $\delta x$), equilibrium is **stable** and the system will oscillate. If the force points *away from* $x_0$ (sign matches $\delta x$), equilibrium is **unstable** and the system runs off.
>
> Hooke's Law $F = -kx$ is the canonical small-displacement form of a *stable* equilibrium. The $k > 0$ requirement is the stability condition. A spring with "$k < 0$" is not a spring; it's a system about to fall apart.

This framing is the load-bearing one for the rest of the card: **Hooke's Law is the universal small-displacement signature of every stable equilibrium in nature.** It is not a fact about springs. Springs are the example that gave it its name.

---

## A two-sentence history

Robert Hooke published this law in 1676 — as the anagram **ceiiinosssttuv**, which he decoded two years later as the Latin *ut tensio sic vis*: "as the extension, so the force." He encrypted it because he was already at war with Newton (see [[Stories/Newton vs Hooke]]) and didn't want to lose another priority fight by publishing prematurely. The encryption worked; the law stuck; the war went badly anyway.

The deep irony, recorded in the eponymy thread, is that medieval bow-makers and Renaissance gunsmiths almost certainly already *used* the linear-extension relation by feel to tune crossbow prods and lock-springs — they just never wrote it down in a citable place. Hooke gets the name not because he discovered the law but because his anagram-and-decode put it on the bibliographic record. Standard [[Stories/Stigler's Law of Eponymy]] story.

---

## The deep claim — every oscillation in nature is Hooke-like

This is the hunter's target.

**Claim.** Consider *any* one-dimensional system whose force law $F(x)$ is smooth (continuously differentiable) and has an equilibrium at $x_0$, i.e. $F(x_0) = 0$. For small displacements $x = x_0 + \xi$ with $\xi$ small, the force is

$$F(x_0 + \xi) \;\approx\; -k \xi$$

for some constant $k$ that depends on the system. *Every* stable oscillation in nature — pendulum, atomic vibration, molecular bond, water-wave on a pond, sound-wave in air, electron in a parabolic trap, photon as a quantum of the electromagnetic field — emerges from this single fact.

The proof is one line, and it is the deep reason [[Maclaurin Series]] is load-bearing in physics.

### Proof by Taylor expansion

Recall that any smooth function $F(x)$ can be expanded about a point $x_0$ as a Taylor series:

$$F(x_0 + \xi) \;=\; F(x_0) \;+\; F'(x_0)\,\xi \;+\; \tfrac{1}{2}\,F''(x_0)\,\xi^2 \;+\; \tfrac{1}{6}\,F'''(x_0)\,\xi^3 \;+\; \cdots$$

(See [[Maclaurin Series]] for the derivation and the convergence story.)

Two facts simplify this dramatically:

1. **At equilibrium**, $F(x_0) = 0$ by definition of equilibrium. The constant term vanishes.
2. **For small $\xi$**, the $\xi^2$ term is much smaller than the $\xi$ term, the $\xi^3$ term is much smaller still, and so on. To **leading order** — meaning, ignoring terms small compared to the leading one — only the $\xi$ term survives.

Defining $k = -F'(x_0)$ — the *negative slope of the force at equilibrium* — we recover

$$F(x_0 + \xi) \;\approx\; -k\xi.$$

The minus sign isn't put in by hand; it falls out of the **stability condition**. If $x_0$ is a stable equilibrium, then $F$ must be *decreasing* as we cross through $x_0$ (force pushes right just below equilibrium, force pushes left just above) — so $F'(x_0) < 0$, and $k = -F'(x_0) > 0$.

That's it. *Every* smooth stable equilibrium gives Hooke's Law as its leading-order behaviour. The "spring constant" $k$ is just the slope-magnitude of the restoring force at the equilibrium point.

![[hooke-taylor-potential-well.svg|680]]

> [!info] The same statement in energy language
> Equivalently: at a stable equilibrium, the potential energy $U(x)$ has a **local minimum**. So $U'(x_0) = 0$ (that's what "minimum" means in calculus). Expanding $U$ in Taylor series about $x_0$:
> $$U(x_0 + \xi) \;=\; U(x_0) \;+\; U'(x_0)\,\xi \;+\; \tfrac{1}{2}\,U''(x_0)\,\xi^2 \;+\; \cdots \;\approx\; U(x_0) \;+\; \tfrac{1}{2}\,U''(x_0)\,\xi^2.$$
>
> The constant $U(x_0)$ shifts only the zero of energy and doesn't affect dynamics. The leading term is **quadratic in $\xi$**, with coefficient $\tfrac{1}{2} k$ where $k = U''(x_0) > 0$ (positive because it's a minimum — second derivative test from [[Differentiation]]).
>
> Then $F = -dU/dx = -k\xi$, recovering Hooke's Law from the energy side.
>
> *Both routes give the same answer.* This is the deep reason: stable equilibrium ⇒ parabolic potential near the minimum ⇒ linear restoring force ⇒ sinusoidal oscillation. **One fact, three faces.**

### Why this matters for the hunter

A hunter who has internalised the Taylor-expansion argument can now look at *any* stable oscillating system and immediately know:

1. The restoring force near equilibrium is approximately linear.
2. The potential energy near equilibrium is approximately parabolic.
3. The motion near equilibrium is therefore approximately **simple harmonic** (we'll prove the period formula in [[Simple Harmonic Motion]]).
4. The "spring constant" is whatever $-F'(x_0)$ or $U''(x_0)$ happens to be for the system — pendulum, molecule, quantum well, all the same.

That's the trace this card teaches. Every time you see oscillation, ask: *what is the local Hooke's Law?* The answer is the second derivative of the potential at the minimum.

---

## Elastic potential energy: deriving ½kx²

Push or pull a spring slowly from $x = 0$ to $x = X$. The external force you apply to overcome the spring's restoring force is $F_{\text{ext}}(x) = +kx$ (equal magnitude, opposite direction to the spring force). The work you do is

$$W_{\text{ext}} \;=\; \int_0^X F_{\text{ext}}(x)\,dx \;=\; \int_0^X kx\,dx \;=\; \tfrac{1}{2}\,k\,X^2.$$

Since the process is reversible (spring back when you let go), this work is stored as **elastic potential energy** in the spring:

$$\boxed{\; U_{\text{elastic}} \;=\; \tfrac{1}{2}\,k\,x^2 \;}$$

Units check: $\text{N m}^{-1} \cdot \text{m}^2 = \text{N m} = \text{J}$. Good.

![[hooke-force-extension.svg|640]]

**Two ways to see ½ visually:**

1. **Force-extension graph.** Plot $F_{\text{ext}}$ (y-axis) against $x$ (x-axis). The graph is a straight line from origin to $(X, kX)$. Work done = area under the curve = area of a right triangle with base $X$ and height $kX$, which is $\tfrac{1}{2} \cdot X \cdot kX = \tfrac{1}{2} k X^2$. The factor of $\tfrac{1}{2}$ is *the triangle factor*.

2. **Average force.** The force grows linearly from $0$ at $x=0$ to $kX$ at $x=X$, so the **average force** over the stretch is $\tfrac{1}{2}(0 + kX) = \tfrac{1}{2} k X$. Work = (average force) × (distance) = $\tfrac{1}{2} k X \cdot X = \tfrac{1}{2} k X^2$. Same answer; the average-force shortcut is the Cambridge / IGCSE-friendly version.

> [!warning] Don't write $W = F \cdot x = (kx) \cdot x = kx^2$.
> This is the most common student mistake on this row. The formula $W = F \cdot x$ assumes a *constant* force. The spring force is **not** constant — it grows from $0$ to $kx$ as you stretch. You must use the average force, or equivalently integrate. The factor of $\tfrac{1}{2}$ is non-negotiable.

---

## The force-extension graph

A standard experimental setup hangs masses from a vertical spring and records the extension. The graph of extension $x$ against applied force $F$ (or equivalently force against extension, depending on convention) is a **straight line through the origin** for small extensions. The gradient is $k$ (or $1/k$, depending on axes).

Three regions to know on the full force-extension curve, going from small to large extension:

1. **Linear / elastic region** — Hooke's Law holds: $F = kx$. Releasing the load returns the spring to its natural length. No energy is lost; all the work done went into recoverable elastic PE.

2. **Plastic region** (past the **elastic limit**) — the spring no longer obeys Hooke's Law. Releasing the load leaves a **permanent extension**; the spring doesn't return to its natural length. Some of the work done has gone into rearranging the metal's internal structure (dislocations moving, grains slipping) rather than into recoverable PE.

3. **Breaking point** — the wire snaps.

> [!warning] Elastic limit ≠ breaking point
> A common student trap: assuming the elastic limit and the breaking point are the same thing. They aren't. The elastic limit is where the *linearity* fails. The breaking point is where the wire *snaps*. Plastic deformation happens between them — the wire stretches, the wire stays stretched, the wire is still intact.

The microscopic reasons for all three regions are the subject of [[Stress, Strain and Young Modulus]]. For now, the experimental fact is enough: Hooke's Law is *empirically* a small-extension limit, with a measurable cut-off.

---

## Springs in series and parallel

These combinations come up constantly — IB Physics, A-Level mechanics, IGCSE Extended, AP Physics 1. They follow the same logic as electrical resistors, but with the formulas *swapped*. Memorise the result by deriving it once.

### Two springs in series (end-to-end)

Spring 1 (constant $k_1$) is attached to a wall; spring 2 (constant $k_2$) is attached to the free end of spring 1; a force $F$ is applied at the free end of spring 2.

**Key observation:** the same force $F$ runs through both springs (Newton's Third Law at every junction). So spring 1 stretches by $x_1 = F/k_1$, and spring 2 stretches by $x_2 = F/k_2$. The total extension is

$$x_{\text{total}} = x_1 + x_2 = \frac{F}{k_1} + \frac{F}{k_2} = F\left(\frac{1}{k_1} + \frac{1}{k_2}\right).$$

The effective spring constant $k_{\text{series}} = F / x_{\text{total}}$ then satisfies

$$\boxed{\; \frac{1}{k_{\text{series}}} \;=\; \frac{1}{k_1} \;+\; \frac{1}{k_2} \;}$$

**Series springs are softer** than either component. Intuition: longer springs stretch more for the same pull.

### Two springs in parallel (side by side)

Both springs are attached to the wall and to the same mass. When the mass is pulled by displacement $x$, *both* springs stretch by $x$, so each contributes a restoring force: $F_1 = k_1 x$ from spring 1, $F_2 = k_2 x$ from spring 2. Total restoring force

$$F_{\text{total}} = F_1 + F_2 = (k_1 + k_2)\,x.$$

So

$$\boxed{\; k_{\text{parallel}} \;=\; k_1 + k_2 \;}$$

**Parallel springs are stiffer** than either component. Intuition: more material resisting the same displacement.

> [!tip] Series-parallel rule of thumb
> Springs and resistors follow opposite rules:
>
> - **Resistors**: series adds, parallel adds reciprocally.
> - **Springs**: parallel adds, series adds reciprocally.
>
> The deep reason — current and force are the "shared" quantity in their respective series networks; voltage and extension are the "shared" quantity in their respective parallel networks. The duality is exact, but it's easier to derive it each time than to memorise which way round it goes.

---

## Worked examples

### Example 1 — Stretching a spring (Cambridge 9702 / 0625 level)

A spring of natural length $0.200~\text{m}$ extends to $0.260~\text{m}$ when a $1.5~\text{N}$ force is applied. Find (a) the spring constant, (b) the elastic PE stored.

**Solution.**

(a) Extension $x = 0.260 - 0.200 = 0.060~\text{m}$. Then
$$k = \frac{F}{x} = \frac{1.5}{0.060} = 25~\text{N m}^{-1}.$$

(b) Elastic PE
$$U = \tfrac{1}{2}\,k\,x^2 = \tfrac{1}{2}(25)(0.060)^2 = 0.045~\text{J} = 4.5 \times 10^{-2}~\text{J}.$$

*Pedagogy note.* Always work in SI units (metres, not centimetres). The mistake every IGCSE student makes once is leaving $x$ in cm and getting an answer $10^{-2}$ off.

### Example 2 — Spring hanging vertically (equilibrium shift)

A spring of constant $k = 40~\text{N m}^{-1}$ hangs vertically. A mass $m = 0.200~\text{kg}$ is attached and allowed to hang at rest. (a) By how much does the spring extend? (b) If the mass is then pulled down a further $0.050~\text{m}$ and released, write the equation of motion. (Take $g = 9.81~\text{m s}^{-2}$.)

**Solution.**

(a) At the new equilibrium, the spring's upward pull balances gravity:
$$k\,x_0 = m g \quad \Rightarrow \quad x_0 = \frac{mg}{k} = \frac{(0.200)(9.81)}{40} = 0.049~\text{m}.$$

(b) Let $\xi$ be the displacement *from the new equilibrium position* (not from the natural length). The forces on the mass are:
- Spring pulls up: $-k(x_0 + \xi)$ (with up positive, so the spring force is $+k(x_0 + \xi)$ when measured as a magnitude pointing up, but we'll keep sign convention $\xi > 0 \Rightarrow$ mass is below equilibrium, spring is more stretched, restoring force is up = negative)
- Gravity: $-mg$ (always down = negative).

Net force (taking up positive):
$$F = +k(x_0 + \xi) - mg = kx_0 + k\xi - mg.$$

But we *chose* $x_0$ so that $kx_0 = mg$. So those terms cancel and we are left with

$$F = -k\xi$$

— *exactly* Hooke's Law about the new equilibrium. Newton's Second Law gives

$$m\,\ddot{\xi} = -k\,\xi$$

which is the **simple harmonic motion equation** (the topic of [[Simple Harmonic Motion]]). Gravity has dropped out entirely; it only *shifted* the equilibrium position. The oscillation about the shifted equilibrium is governed by the spring alone.

> [!info] The deep pattern: equilibrium absorbs the constant force
> Whenever a constant force (like gravity) acts on a Hooke's-Law system, the *equilibrium position* shifts, but the *oscillation* about the new equilibrium is governed by the *same* spring constant $k$. The mathematical trick — re-defining the origin so the constant force vanishes — is identical to the Taylor-expansion trick of [[Maclaurin Series]]: we expand about wherever the linear term cancels.
>
> This is why a mass on a vertical spring oscillates at the *same* period as it would on a horizontal frictionless surface. Gravity is invisible to the dynamics; it only matters for the equilibrium.

### Example 3 — Period of a mass-spring oscillator (IB / AP preview)

A mass $m = 0.500~\text{kg}$ on a horizontal frictionless surface is attached to a spring of constant $k = 200~\text{N m}^{-1}$. Find the period of oscillation.

**Solution by Newton's Second Law.** With $\xi$ the displacement from equilibrium,
$$m \ddot{\xi} = -k\xi \quad \Leftrightarrow \quad \ddot{\xi} = -\frac{k}{m}\xi.$$

This is the SHM equation with angular frequency $\omega = \sqrt{k/m}$. The period is

$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}.$$

Substituting:
$$T = 2\pi\sqrt{\frac{0.500}{200}} = 2\pi\sqrt{0.0025} = 2\pi(0.050) \approx 0.314~\text{s}.$$

**Solution by energy conservation** (parallel route, no calculus). At maximum displacement $A$, the mass is momentarily at rest and all energy is elastic PE = $\tfrac{1}{2}kA^2$. At equilibrium, the spring is unstretched and all energy is kinetic = $\tfrac{1}{2}mv_{\max}^2$. Conservation:
$$\tfrac{1}{2}kA^2 = \tfrac{1}{2}m v_{\max}^2 \quad \Rightarrow \quad v_{\max} = A\sqrt{k/m} = A\omega.$$

This recovers $\omega = \sqrt{k/m}$ — the same answer by an entirely different route. *Both routes agree because they describe the same physics.*

The period formula $T = 2\pi\sqrt{m/k}$ is sitting on the IB Physics data sheet (Theme C.1.1) and the 9702 P4 formula sheet. It is also the *first* of many "$T = 2\pi\sqrt{\text{(stuff)}/\text{(more stuff)}}$" formulas you will meet — pendulum, LC circuit, physical pendulum, torsional oscillator. **All of them are Hooke's Law in disguise**, with $k$ replaced by whatever the local Hooke-constant happens to be.

---

## Where Hooke's Law actually breaks down

The Taylor-expansion argument is exact only in the limit $\xi \to 0$. For finite $\xi$, the next term in the expansion is

$$F(x_0 + \xi) \;=\; -k\xi \;+\; \tfrac{1}{2}\,F''(x_0)\,\xi^2 \;+\; \tfrac{1}{6}\,F'''(x_0)\,\xi^3 \;+\; \cdots$$

The correction is small when $\xi$ is small compared to whatever length-scale governs the system. Three regimes:

1. **Pure Hooke** ($\xi$ very small): only the linear term matters. Oscillation is exactly sinusoidal, period independent of amplitude.

2. **Mildly anharmonic** ($\xi$ moderate): the cubic correction (called the **anharmonic term**) matters. The oscillation is still oscillation, but its shape is slightly distorted from a pure sine wave, and the period now depends weakly on amplitude. Real pendulums for amplitudes above ~10° live here.

3. **Full nonlinear** ($\xi$ large): the linear term is no longer dominant; the system's behaviour can change qualitatively. Springs deform plastically; molecules dissociate; pendulums flip over the top. The Hooke description has failed and you need the full $F(x)$ or $U(x)$.

The cutoff between regimes 1 and 2 is what students should understand as the *practical* limit of Hooke's Law in a given experiment, *not* the elastic limit (which is the cutoff between 2 and 3 in steel and similar materials).

---

## Beyond syllabus — why every oscillation in nature is Hooke-like

### Atoms in a crystal

Recall that atoms in a solid sit in **potential wells** created by the surrounding atoms — each atom is in stable equilibrium at its lattice position. The potential energy $U(\xi)$ as a function of the atom's displacement from its equilibrium is smooth and has a minimum at $\xi = 0$.

Taylor-expanding $U(\xi)$ about the minimum (exactly the move we did above) gives

$$U(\xi) \;\approx\; U(0) \;+\; \tfrac{1}{2}\,U''(0)\,\xi^2 \;+\; \tfrac{1}{6}\,U'''(0)\,\xi^3 \;+\; \cdots$$

For small thermal vibrations at room temperature, the quadratic term dominates and **atoms vibrate exactly like masses on tiny springs**. This is the entire basis of:

- **Lattice vibrations** (phonons) — quantised vibrations of the atomic Hooke-springs in a crystal. Phonons carry sound and heat in solids.
- **Thermal expansion** — when the *cubic* (anharmonic) term in the potential becomes non-negligible at higher temperatures, the average atomic position shifts. The asymmetry is why solids expand when heated. *A purely Hookean solid would not expand at all.*
- **The Einstein and Debye models of specific heat** — both built on "each atom is a Hooke's Law oscillator."

The number $U''(0)$ for a typical interatomic potential gives spring constants of order $k \sim 10^2~\text{N m}^{-1}$ per atomic bond — close to the macroscopic spring you'd buy at a hardware store, multiplied by Avogadro's number across the bulk material. **Every macroscopic spring is a billion-billion atomic Hooke-springs in series and parallel.**

### Molecular vibrations and IR spectroscopy

Recall that the chemical bond between two atoms in a molecule is itself a Hooke spring near equilibrium. The classical period of vibration is $T = 2\pi\sqrt{\mu/k}$ where $\mu$ is the reduced mass and $k$ is the bond's force constant. Quantum mechanics restricts the vibrational energy to discrete levels separated by $h\nu = h/T$.

When you shine infrared light on a molecule, the photons whose frequency $\nu$ matches the vibrational frequency get absorbed — this is how **infrared spectroscopy** works. Every absorption peak in an IR spectrum is the universe singing back *"yes, that bond's Hooke constant is what you predicted."* The technique works because Hooke's Law is the leading-order behaviour of every chemical bond near equilibrium.

### The Lennard-Jones potential

The standard model of a noble-gas atom-atom interaction is the **Lennard-Jones potential**:

$$U(r) \;=\; 4\epsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^{6}\right]$$

This has a clear minimum at $r_0 = 2^{1/6}\sigma$. Taylor-expanding $U(r)$ about $r_0$ gives (after some algebra)

$$U(r) \;\approx\; -\epsilon \;+\; \tfrac{1}{2}\left(\frac{72\,\epsilon}{2^{1/3}\sigma^2}\right)(r-r_0)^2 \;+\; \cdots$$

— a Hooke's Law potential with effective spring constant $k = 72\,\epsilon/(2^{1/3}\,\sigma^2)$. Despite the fearsome $1/r^{12}$ structure of the original potential, the *small-vibration* dynamics are just $F = -k(r-r_0)$. The Taylor expansion erases all the complication near the bottom of the well.

### The quantum harmonic oscillator and photons as quanta

Recall from [[Stories/Newton vs Hooke]] §"wave-particle irony" that light is a quantum object whose classical projections are waves *and* particles. Here is the connection to Hooke.

**Maxwell's electromagnetic field is, at each point in space, a harmonic oscillator.** The electric and magnetic fields play the role of "position" and "momentum" of a Hooke-Law oscillator at every spatial frequency. When you quantise this — a step beyond IB Physics, but central to anything resembling modern physics — the *energy* of the oscillator is restricted to discrete levels:

$$E_n = \left(n + \tfrac{1}{2}\right)\hbar\omega, \qquad n = 0, 1, 2, \ldots$$

Each unit of energy $\hbar\omega$ at frequency $\omega$ is called a **photon**. Photons are quanta of a Hooke's Law oscillator — specifically, of the electromagnetic field. The wave/particle duality Hooke and Newton fought over for thirty years resolves like this: light is a *wave* in the classical-field description, and a *particle* in the quantised-oscillator description, and these are the same object viewed two ways. Newton called Hooke a "drudge" for working with springs. Three hundred years later we learned that *photons are quanta of springs.* The universe is fond of irony.

### The deep summary

Every oscillating system you will ever meet — pendulum, mass-spring, atom in a lattice, molecule absorbing IR light, electron in a parabolic trap, photon as an EM-field quantum, neutrino oscillation, vibration of a guitar string, vibration of a piano string, vibration of the LIGO mirror suspension, vibration of the cosmic microwave background as the universe was being born — gets its restoring force from the same Taylor-expansion argument. Hooke's Law is not a property of springs. It is **the universal small-displacement signature of every stable equilibrium**, and every oscillation in physics is the song of some local Hooke-constant.

That is what this card teaches the hunter to trace.

---

## Exam Notes

### Cambridge 9702 (§6.2 — AS, Paper 2)

- The row asks for: elastic vs plastic deformation, Hooke's law $F = kx$, and elastic potential energy $\tfrac12 Fx = \tfrac12 kx^2$ *within the limit of proportionality*.
- **Graph questions dominate.** On a force–extension graph the gradient is $k$ and the **area under the curve is the work done** (= stored EPE). The formula $\tfrac12 kx^2$ is only valid in the straight-line region — but the *area* reading works even beyond it, which is exactly how part (b) usually catches students who memorised the formula without the picture.
- **Two definition marks students conflate:** the *limit of proportionality* (where $F \propto x$ stops holding) and the *elastic limit* (beyond which deformation is permanent) are different points. Learn both sentences.
- Pairs with §6.1 — the material-level version lives in [[Stress, Strain and Young Modulus]].

### Cambridge 9231 Further Mechanics (§3.4) — the notation shift

- The same law in different clothes: an elastic string or spring of **natural length** $L$ and **modulus of elasticity** $\lambda$ obeys $T = \lambda x / L$, with stored energy $\lambda x^2/2L$. Translation: $k = \lambda/L$ — the modulus absorbs the length, making $\lambda$ a property of the material and cross-section rather than of the particular cut length. The full Further-Mechanics treatment — worked Paper 3 questions, the slack discipline, the bungee design — is [[Elastic Strings and Springs]].
- **Strings go slack.** Unlike a spring, an elastic string cannot push — before trusting any formula, check the extension is genuinely positive on the interval in question.
- Question style: work–energy problems (particle on an elastic string over an incline; the elastic conical pendulum), typically asking for the speed as the string reaches natural length.
- Note **9709 carries no Hooke's law at all** — for Cambridge maths students the elastic-energy machinery is entirely a 9231 topic.

### Cambridge 0625 IGCSE (§1.5)

- Load–extension graphs, the spring constant $k = F/x$, and the limit of proportionality — graph reading and sketching; the energy formula is not required.

### IB Physics (A.2.2 + C.1)

- Enters as one of the listed contact forces in A.2.2 ($F_H = -kx$ and $E_H = \tfrac12 k(\Delta x)^2$ are both on the data booklet), then returns as the engine of SHM in C.1 ([[Simple Harmonic Motion]]).

### AP Physics (1 §2.8 · C Mechanics)

- AP-1: spring force and $U_s = \tfrac12 kx^2$ are on the sheet; the staples are energy bar charts and the design-an-experiment-to-measure-$k$ FRQ. AP-C expects the integral derivation $U = \int kx\,dx$ and springs embedded in oscillation and energy problems.

---

## Formula sheet status

| Board | Hooke's Law $F=kx$ | Elastic PE $\tfrac{1}{2}kx^2$ | Mass-spring period $T = 2\pi\sqrt{m/k}$ |
|---|---|---|---|
| Cambridge IGCSE 0625 | Not on data sheet — must memorise | Not on data sheet — must memorise | Not in syllabus |
| Cambridge A-Level 9702 | Not on data sheet — must memorise | Not on data sheet — must memorise | Not on data sheet (A-Level oscillations §17) — must memorise |
| IB Physics | Not on data booklet — must memorise | Not on data booklet — must memorise | **On data booklet** (Theme C.1.1) |
| AP Physics 1 | **On formula sheet** ($F_s = -k \lvert x \rvert$ form) | **On formula sheet** ($U_s = \tfrac{1}{2}k x^2$) | **On formula sheet** ($T_s = 2\pi\sqrt{m/k}$) |

Two takeaways for exam strategy:

- **Hooke's Law itself ($F = kx$) is universally expected to be *memorised*** — no major board prints it on the data sheet. The reason is that the law is considered *definitional* of a spring, and so naming a quantity "$k$" without writing $F = kx$ would be circular.
- **AP Physics 1 is the most generous board** — formula, energy, and period are all printed. **IB Physics provides the period only**. The Cambridge boards print *neither* — students are expected to derive the period from $\ddot{x} = -(k/m)x$.

---

## Connections

- **Parents (already in vault):**
   - [[Newton's Laws of Motion]] — $F = ma$ is the engine that turns "force = $-kx$" into oscillating motion.
   - [[Work, Energy and Power]] — work as $\int F\,dx$ is what makes $\tfrac{1}{2}kx^2$ fall out as the integral of $-kx$.
   - [[Differentiation]] — the second-derivative test for stability and the linearisation of $F$ both live there.
   - [[Maclaurin Series]] — the Taylor expansion of $F$ or $U$ about equilibrium is the deep reason Hooke's Law is universal. The bridge runs both ways: Maclaurin/Taylor is the math machinery that makes Hooke's Law a *theorem*, not a hypothesis.
   - [[Vectors]] — the minus sign in $F = -kx$ is a vector statement.

- **Companion historical card:** [[Stories/Newton vs Hooke]] — the 1672–1703 priority war that gave Hooke this law (and Newton most of the rest of physics). The wave-particle irony at the end of that card connects directly to the QHO callout above: photons are quanta of Hooke-springs.

- **Children:**
   - [[Simple Harmonic Motion]] — solves $\ddot{x} = -(k/m)x$ explicitly, builds the full sin/cos solution, derives period and frequency rigorously.
   - [[Stress, Strain and Young Modulus]] — explains *why* a spring has the spring constant it does, in terms of the material's microscopic structure.
   - [[Waves I: The Wave Equation]] — the spatial generalisation of mass-spring → coupled mass-springs → wave equation.
   - [[The Quantum Harmonic Oscillator]] — the deepest payoff of the Taylor-expansion argument.

- **Cross-domain math bridges:**
   - [[Differential Equations]] — $m\ddot{x} = -kx$ is the prototypical second-order linear ODE; everything you ever learn about linear ODEs is calibrated against this equation.
   - [[Trigonometric Functions]] — sinusoidal motion is the solution; without trig there is no SHM.

- **Misconception traps cleared:** $F = -kx$ is **not** a property of springs; the minus sign **is** the point; the elastic limit is **not** the breaking point; $W = \tfrac{1}{2}kx^2$ **not** $W = kx^2$; gravity **shifts equilibrium** but does not change the oscillation period.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $F = -kx$ | `F = -kx` | Hooke's Law, vector form (IB / AP / dynamics) |
| $F = kx$ | `F = kx` | Hooke's Law, magnitude form (Cambridge 9702 / 0625) |
| $k$ | `k` | Spring constant / stiffness, units $\text{N m}^{-1}$ |
| $U = \tfrac{1}{2}kx^2$ | `U = \tfrac{1}{2}kx^2` | Elastic potential energy |
| $T = 2\pi\sqrt{m/k}$ | `T = 2\pi\sqrt{m/k}` | Period of mass on spring (SHM preview) |
| $\omega = \sqrt{k/m}$ | `\omega = \sqrt{k/m}` | Angular frequency of mass-spring |
| $\frac{1}{k_{\text{series}}} = \frac{1}{k_1} + \frac{1}{k_2}$ | `\frac{1}{k_{\text{series}}} = \frac{1}{k_1} + \frac{1}{k_2}` | Series combination |
| $k_{\text{parallel}} = k_1 + k_2$ | `k_{\text{parallel}} = k_1 + k_2` | Parallel combination |
| $U(x) \approx U(x_0) + \tfrac{1}{2}U''(x_0)(x-x_0)^2$ | (Taylor expansion form) | The deep reason for universality |
| *ut tensio sic vis* | (Latin) | Hooke's 1678 phrase: "as the extension, so the force" |
| ceiiinosssttuv | (anagram, 1676) | Hooke's encrypted publication of the law |
