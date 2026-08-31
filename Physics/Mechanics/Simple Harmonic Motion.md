---
chinese: 简谐运动 (jiǎn xié yùndòng)
prerequisites:
  - "[[Hooke's Law for Springs]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Work, Energy and Power]]"
  - "[[Differentiation]]"
  - "[[Differential Equations]]"
  - "[[Second-Order Differential Equations]]"
  - "[[Trigonometric Functions]]"
  - "[[Maclaurin Series]]"
  - "[[Radians]]"
  - "[[Circular Motion]]"
leads_to:
  - "[[Damped Oscillations]]"
  - "[[Resonance]]"
  - "[[Coupled Oscillators]]"
  - "[[Pendulums]]"
  - "[[Waves I: The Wave Equation]]"
  - "[[The Quantum Harmonic Oscillator]]"
  - "[[The Pendulum Story]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - domain/oscillations
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/9702-17-1
  - syllabus/9702-17-2
  - syllabus/IB-Physics-C-1-1
  - syllabus/IB-Physics-C-1-2
  - syllabus/IB-Physics-C-1-3
  - syllabus/AP-Physics-1-7-1
  - syllabus/AP-Physics-1-7-2
  - syllabus/AP-Physics-1-7-3
  - syllabus/AP-Physics-1-7-4
  - syllabus/AP-Physics-C-Mech-7-1
  - syllabus/AP-Physics-C-Mech-7-2
  - syllabus/AP-Physics-C-Mech-7-3
  - syllabus/AP-Physics-C-Mech-7-4
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/omega-angular-frequency
  - notation/phase-angle-phi
  - notation/period-T
  - misconception/period-depends-on-amplitude
  - misconception/SHM-needs-springs
  - misconception/v-and-x-are-in-phase
  - misconception/pendulum-is-always-SHM
---

# Simple Harmonic Motion 简谐运动

## Definition

A body undergoes **simple harmonic motion (SHM)** when its acceleration is *directly proportional* to its displacement from a fixed equilibrium point, and *directed back* toward that point:

$$\boxed{\; a = -\omega^2 x \;}$$

The four letters in that one line:

- $a$ — the body's **acceleration** (units: $\text{m s}^{-2}$). The second time-derivative of position, $a = \dfrac{d^2 x}{dt^2}$.
- $x$ — the body's **displacement from equilibrium** (units: $\text{m}$). Signed: positive on one side, negative on the other.
- $\omega$ — a positive constant called the **angular frequency** (units: $\text{rad s}^{-1}$). For a mass-on-spring it equals $\sqrt{k/m}$; in general it equals $\sqrt{U''(x_0)/m}$ where $U''(x_0)$ is the curvature of the potential at the stable equilibrium.
- The **minus sign** — the entire story. It's what makes the motion oscillatory rather than runaway, exactly as in [[Hooke's Law for Springs]].

> [!info] Full symbol glossary in the 中文锚点 below
> The table immediately below lists *every* symbol in this card (amplitude $A$, period $T$, frequency $f$, phase $\phi$, spring constant $k$, mass $m$, etc.) with units and bilingual names. Glance there before continuing — the card refers back to these symbols constantly.

This is the most important second-order differential equation in physics. Newton's Second Law turns Hooke's Law into the SHM equation in one step. Writing $F = -kx$ for the spring (where $k$ is the **spring constant**, units $\text{N m}^{-1}$, and $m$ is the **oscillator's mass** in $\text{kg}$):

$$F = ma \quad \text{and} \quad F = -kx \quad \Rightarrow \quad m \cdot \frac{d^2 x}{dt^2} = -kx \quad \Rightarrow \quad \frac{d^2 x}{dt^2} = -\frac{k}{m}\,x.$$

Identifying $\omega^2 = k/m$, we have $\boxed{\omega = \sqrt{k/m}}$. **SHM is what Hooke's Law does over time.** The Hooke card was the *force law*; this card is the *motion* it produces.

> [!info] "Angular frequency" or "angular velocity"? — same quantity, two names
> The symbol $\omega$ wears two hats in physics:
>
> - In **rotational mechanics** (a wheel spinning, a planet orbiting), $\omega$ is called **angular velocity** — how fast an angle is sweeping out, $\omega = d\theta/dt$.
> - In **oscillations and waves** (SHM, AC circuits, light), $\omega$ is called **angular frequency** — how fast the phase of a sinusoid advances, $\omega = 2\pi f$.
>
> **They are the same quantity** (units $\text{rad s}^{-1}$ in both cases). The reason becomes clear in the circle-projection picture below: SHM is literally the shadow of uniform circular motion, so the "angular velocity" of the underlying rotation *becomes* the "angular frequency" of the SHM. Two names, one $\omega$. Chinese physics 课本 calls it 角速度 in rotation and 角频率 in oscillation — same distinction.
>
> This card uses "angular frequency" because SHM is its primary topic. When you meet $\omega$ in [[Newton's Laws of Motion]] applied to a rotating body, "angular velocity" is the right name for the same number.

### 中文锚点

**简谐运动 (jiǎn xié yùndòng)** = 物体加速度与位移成正比、方向相反的运动。中文教材也叫 **简谐振动 (jiǎn xié zhèndòng)**.

| English | 中文 | Symbol / formula |
|---|---|---|
| Amplitude | 振幅 (zhènfú) | $A$ — largest displacement from equilibrium |
| Period | 周期 (zhōuqī) | $T = 2\pi/\omega$ |
| Frequency | 频率 (pínlǜ) | $f = 1/T = \omega/(2\pi)$, units Hz |
| Angular frequency | 角频率 (jiǎo pínlǜ) | $\omega$, units $\text{rad s}^{-1}$ |
| Phase | 相位 (xiàngwèi) | $\omega t + \phi$ — argument of the sine/cosine |
| Phase angle | 初相位 / 相位常数 (chū xiàngwèi) | $\phi$ — sets where the motion starts in its cycle |
| Equilibrium position | 平衡位置 (pínghéng wèizhi) | $x = 0$ |
| Mass–spring oscillator | 弹簧振子 (tánhuáng zhènzi) | $T = 2\pi\sqrt{m/k}$ |
| Simple pendulum | 单摆 (dānbǎi) | $T = 2\pi\sqrt{L/g}$ for small angles |
| Damping | 阻尼 (zǔní) | energy leaks out; amplitude decays |
| Resonance | 共振 (gòng zhèn) | driving frequency = natural frequency → large amplitude |

中文物理早就学过弹簧振子和单摆，但英语 IB/AP/A-Level **要求学生把 $\ddot{x} = -\omega^2 x$ 当作核心方程**，并独立完成两件事：
1. **从微分方程推出 $x(t) = A\cos(\omega t + \phi)$** — 不能只是背公式
2. **从能量守恒推出 $\omega = \sqrt{k/m}$ 而不依赖运动学** — 这是 9702/IB HL/AP-C 的最常考路径

中文叫"角频率"，英文常常省略"角"字直接说 frequency $\omega$ — 这是英语物理的偷懒约定，看到 $\omega$ 出现在 oscillation/wave 的语境里都是 angular frequency。

---

## Why SHM is everywhere — the bridge to Hooke

Recall the deep claim from [[Hooke's Law for Springs]]: every smooth stable equilibrium gives $F \approx -k\xi$ to leading order, where $\xi$ is the small displacement from equilibrium and $k = U''(x_0)$ is the curvature of the potential at its minimum.

By Newton's Second Law this is *immediately* the SHM equation:

$$\frac{d^2 \xi}{dt^2} = -\frac{k}{m}\,\xi = -\omega^2 \xi.$$

So:

> **Theorem.** Every small oscillation about a stable equilibrium is *approximately* simple harmonic, with angular frequency $\omega = \sqrt{U''(x_0)/m}$.

Pendulum, atomic vibration in a crystal lattice, molecular bond, water wave, sound wave, electron in a quadratic trap, photon as a quantum of the electromagnetic field — *every* small oscillation in nature is SHM at the bottom. The card you're reading now describes what that motion *looks like* in time: the shape of the trajectory, the phase relationships, the period, the energy interchange.

---

## Solving the SHM equation — two routes to the same answer

The equation $\dfrac{d^2 x}{dt^2} = -\omega^2 x$ is a second-order linear differential equation. Its general solution is what we need.

### Route 1 — guess and verify

The minus sign and the second derivative both suggest **trigonometric** functions: $\sin$ and $\cos$ are the two functions that come back to themselves (with a sign flip) after two differentiations. Try

$$x(t) = A \cos(\omega t + \phi).$$

Differentiate once to get velocity, twice to get acceleration:

$$v = \frac{dx}{dt} = -A\omega \sin(\omega t + \phi), \qquad a = \frac{d^2 x}{dt^2} = -A\omega^2 \cos(\omega t + \phi) = -\omega^2 x. \quad\checkmark$$

It satisfies the equation. Two constants $A$ and $\phi$ are baked in — exactly the number of integration constants a second-order ODE expects. They are set by **initial conditions** (typically the position and velocity at $t=0$).

Equivalent alternative forms (all describing the same motion, just labelled differently):

$$x(t) = A\sin(\omega t + \phi'), \qquad x(t) = C\cos(\omega t) + D\sin(\omega t).$$

The third form has constants $C, D$ that combine into the same $A, \phi$ via $A = \sqrt{C^2 + D^2}$ and $\tan\phi = -D/C$. Use whichever form makes the initial conditions cleanest.

### Route 2 — energy conservation

A mass-spring oscillator's total mechanical energy is

$$E = \underbrace{\tfrac{1}{2}m v^2}_{\text{KE}} + \underbrace{\tfrac{1}{2}kx^2}_{\text{elastic PE}}.$$

If no energy leaves the system (no damping), $E$ is constant. Differentiating both sides with respect to time (chain rule on each piece):

$$0 = m v \frac{dv}{dt} + kx \frac{dx}{dt} = \frac{dx}{dt}\left(m \frac{dv}{dt} + kx\right) = v\,(m a + k x).$$

Either $v = 0$ (which only happens at the two turning points and lasts zero time) or $m a + k x = 0$, i.e. $a = -(k/m)x$. **Energy conservation is the SHM equation under another name.**

From this same expression we get the velocity-as-function-of-position formula. At the turning points, $v = 0$ and all energy is PE: $E = \tfrac{1}{2}kA^2$. At any other position $x$:

$$\tfrac{1}{2}m v^2 + \tfrac{1}{2}kx^2 = \tfrac{1}{2}kA^2 \quad \Rightarrow \quad v^2 = \frac{k}{m}(A^2 - x^2)$$

so

$$\boxed{\; v = \pm \omega \sqrt{A^2 - x^2} \;}.$$

The $\pm$ accounts for motion in either direction through the same position. **This formula is on the IB Physics data booklet and the 9702 Paper 4 formula sheet** — but you should now know exactly where it comes from.

### Why both routes are useful

Use Route 1 (ODE) when you want the **time-dependence** $x(t)$ and the period. Use Route 2 (energy) when you want **speed at a given position** without caring about time. Cambridge and IB problems lean on both; the energy route is faster for "find the speed at the half-amplitude point" questions, the ODE route is faster for "what's the period" questions.

---

## The period formula

From $\omega = \sqrt{k/m}$ and $T = 2\pi/\omega$ we have

$$\boxed{\; T = 2\pi \sqrt{\frac{m}{k}} \;}$$

for the mass-spring oscillator. **Notice what's absent: the amplitude $A$.** The period is independent of how far you pull the mass — small swings and big swings take the *same time*. This **isochronism** is the defining surprise of SHM, the property Galileo noticed watching the cathedral lamps in Pisa swing in 1582 and that made him invent the pendulum clock.

The frequency $f = 1/T$ has units of Hertz ($\text{Hz} = \text{s}^{-1}$, one cycle per second). The angular frequency $\omega = 2\pi f$ has units of $\text{rad s}^{-1}$.

> [!warning] $\omega$ is NOT the frequency
> Students mix up $\omega$ and $f$ all the time. $f$ counts cycles per second; $\omega$ counts *radians* per second. Since one cycle is $2\pi$ radians, $\omega = 2\pi f$. **In any formula involving $\omega$, the 2π is hiding inside.** When in doubt, look at units.

---

## The pendulum — and why "small angles" matters

A pendulum of length $L$ swinging with angular displacement $\theta$ from vertical experiences a restoring **torque** from gravity:

$$\tau = -mgL\sin\theta.$$

Using the rotational form of Newton's Second Law, $\tau = I\,\alpha = I \dfrac{d^2 \theta}{dt^2}$, with $I = mL^2$ for a point mass on a massless string:

$$mL^2 \frac{d^2 \theta}{dt^2} = -mgL\sin\theta \quad \Rightarrow \quad \frac{d^2 \theta}{dt^2} = -\frac{g}{L}\sin\theta.$$

> [!info] Quick sidebar — torque $\tau$, moment of inertia $I$, angular momentum $L_{\text{ang}}$
> The pendulum derivation borrows three quantities from **rotational dynamics**: torque $\tau$ (the angular analogue of force), moment of inertia $I$ (the angular analogue of mass), and the corresponding rotational form of Newton's Second Law. The static version of torque lives in [[Forces and Equilibrium]] (moments of a force, principle of moments); the full dynamical treatment — $\tau = I\alpha$ and $\tau = dL_{\text{ang}}/dt$, $L_{\text{ang}} = I\omega$, conservation of angular momentum, the parallel-axis theorem — now lives in the completed rotational-dynamics trio: [[Torque]], [[Moment of Inertia]], and [[Angular Momentum]]. Every quantity this pendulum step uses ($\tau$, $I$, and $I = mL^2$ for a point mass) is derived in full there — nothing here rests on faith any more.
>
> The notation conflict to watch: physics uses $L$ for both **length** (here, the pendulum length) AND **angular momentum** ($L_{\text{ang}} = I\omega$). Context disambiguates; this card uses $L$ for length only.

**This is not SHM.** The equation has $\sin\theta$, not $\theta$. *Strict* SHM requires the restoring acceleration to be linear in the displacement.

But for *small* $\theta$ — say, less than ~10° — we can use the small-angle approximation $\sin\theta \approx \theta$. This is the limit

$$\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1$$

which is **the** foundational trigonometric limit. It can be seen two ways:

- **As a Taylor expansion** (see [[Maclaurin Series]]): $\sin\theta = \theta - \tfrac{1}{6}\theta^3 + \tfrac{1}{120}\theta^5 - \cdots$ — for small $\theta$, the cubic and higher terms are tiny and the leading $\theta$ dominates.
- **As a squeeze-theorem proof** (see [[Radians]] §"Proof that $\lim_{h \to 0} \tfrac{\sin h}{h} = 1$"): the unit-circle area argument $\sin h < h < \tan h$ squeezes $\sin h / h$ between $\cos h$ and $1$, both tending to $1$. Geometric, elementary, no calculus required.

The squeeze proof comes first historically and logically (the Taylor expansion *uses* the derivative $(\sin)' = \cos$, whose derivation *needs* this very limit). The Maclaurin form is the polynomial-truncation view of the same fact. Either lens gets you the same approximation.

For small $\theta$, to **leading order** $\sin\theta \approx \theta$, and the pendulum equation becomes

$$\frac{d^2 \theta}{dt^2} \approx -\frac{g}{L}\,\theta.$$

*This* is SHM, with $\omega^2 = g/L$, giving the famous pendulum period

$$\boxed{\; T = 2\pi\sqrt{\frac{L}{g}} \;}.$$

> [!info] The "small-angle approximation" is Hooke's universality theorem in disguise
> Recall the Hooke's Law theorem: every smooth restoring force is approximately linear near equilibrium. The pendulum's restoring "force" is $-mgL\sin\theta$, which has a stable equilibrium at $\theta = 0$. Taylor-expanding (or applying the squeeze-theorem limit) gives $-mgL\theta$ to leading order — exactly the linear-restoring-force signature. So the pendulum's small-angle SHM isn't a separate physical phenomenon; it's the *same* universality theorem from [[Hooke's Law for Springs]] applied to gravity-on-a-string instead of a spring.
>
> The pendulum being approximately isochronous is the universality theorem made visible — Galileo's cathedral observation, in modern language, was an empirical demonstration that smooth restoring forces are locally linear.

**At larger angles the pendulum is anharmonic.** The period becomes weakly amplitude-dependent — a 30° pendulum's period is about 1.7% longer than the small-angle formula predicts; at 90° (the bob horizontal) it's about 18% longer. The exact period involves elliptic integrals and lives beyond the syllabus.

---

## Energy in SHM

The total mechanical energy $E = \frac{1}{2}kA^2$ is constant. Inside the cycle, energy passes back and forth between KE and PE:

$$\text{KE}(x) = \tfrac{1}{2}m v^2 = \tfrac{1}{2}k(A^2 - x^2), \qquad \text{PE}(x) = \tfrac{1}{2}kx^2.$$

The two add to $\frac{1}{2}kA^2$ at every $x$. Three key observations:

1. **At the turning points** ($x = \pm A$): all energy is PE, $v = 0$, momentarily at rest.
2. **At equilibrium** ($x = 0$): all energy is KE, speed is maximum: $v_{\max} = A\omega$.
3. **Halfway out** ($x = A/2$): PE is one-quarter of total, KE is three-quarters. So $v = \omega\sqrt{A^2 - (A/2)^2} = \tfrac{\sqrt{3}}{2}A\omega$ — still 87% of the maximum speed. **The bulk of an SHM cycle is spent near the equilibrium**, not the turning points.

**Time-averaged energies.** Over one full period, the *averages* of KE and PE are *equal*:

$$\langle \text{KE} \rangle = \langle \text{PE} \rangle = \tfrac{1}{4}kA^2.$$

This **equipartition** result anticipates a deep theorem in statistical mechanics: for any harmonic mode, on time-average (or thermal average), KE = PE = $\frac{1}{2}k_BT$. The card you're reading is the classical seed of the result.

---

## Phase relationships — x, v, a

If $x(t) = A\cos(\omega t)$ (taking $\phi = 0$ for the cleanest picture):

$$x(t) = A\cos(\omega t), \qquad v(t) = -A\omega\sin(\omega t), \qquad a(t) = -A\omega^2\cos(\omega t).$$

Three sinusoids, all at the same frequency $\omega$, but shifted in phase:

| Quantity | Function | Phase relative to $x$ |
|---|---|---|
| $x$ | $A\cos(\omega t)$ | reference |
| $v$ | $-A\omega\sin(\omega t) = A\omega\cos(\omega t + \pi/2)$ | leads $x$ by $90°$ |
| $a$ | $-A\omega^2\cos(\omega t) = A\omega^2\cos(\omega t + \pi)$ | $180°$ out of phase with $x$ |

**Intuition.** The velocity is fastest when the displacement is zero (equilibrium, all KE) and zero when the displacement is largest (turning points). That's the 90° offset. The acceleration always points opposite to $x$ — that's the 180° offset, encoded in the minus sign of $a = -\omega^2 x$.

**Maximum values:**

$$x_{\max} = A, \qquad v_{\max} = A\omega, \qquad a_{\max} = A\omega^2.$$

The pattern is "multiply by $\omega$ each time you differentiate" — a useful sanity check on units and numerical answers.

![[shm-phase-relationships.svg|720]]

The same picture, live — the bars on the right tick through the oscillation in real time as the mass moves left-right. Watch the energy exchange: KE and PE are always complementary (they sum to the constant total $\tfrac{1}{2}kA^2$), and $a$ mirrors $x$ through zero:

![[shm-live-quantities.svg|880]]

---

## Worked examples

### Example 1 — A simple spring-mass problem

A $0.250 ~\text{kg}$ mass on a spring of stiffness $k = 100 ~\text{N m}^{-1}$ is displaced $0.040~\text{m}$ from equilibrium and released from rest. Find (a) the angular frequency, (b) the period, (c) the maximum speed, (d) the speed when the displacement is $0.020~\text{m}$.

**Solution.**

(a) $\omega = \sqrt{k/m} = \sqrt{100/0.250} = 20 ~\text{rad s}^{-1}$.

(b) $T = 2\pi/\omega = 2\pi/20 = 0.314 ~\text{s}$.

(c) $v_{\max} = A\omega = 0.040 \times 20 = 0.80 ~\text{m s}^{-1}$.

(d) Use the velocity-position formula:
$$v = \omega\sqrt{A^2 - x^2} = 20\sqrt{0.040^2 - 0.020^2} = 20\sqrt{0.0012} = 0.69 ~\text{m s}^{-1}.$$

Sanity check: $0.69 / 0.80 \approx 0.87 = \frac{\sqrt{3}}{2}$. ✓ — exactly the halfway-out formula from the energy section.

### Example 2 — A pendulum

A pendulum has period $1.50~\text{s}$. Find its length. (Take $g = 9.81 ~\text{m s}^{-2}$.)

**Solution.** From $T = 2\pi\sqrt{L/g}$, square both sides: $T^2 = 4\pi^2 L/g$, so

$$L = \frac{g T^2}{4\pi^2} = \frac{9.81 \times 1.50^2}{4\pi^2} = \frac{22.07}{39.48} = 0.559 ~\text{m}.$$

(A pendulum of just over half a metre swings once every 1.5 seconds. The seconds-pendulum used in many old clocks has $L \approx 1.00 ~\text{m}$ and $T \approx 2.00 ~\text{s}$.)

### Example 3 — Initial conditions and phase

A mass on a spring with $\omega = 5 ~\text{rad s}^{-1}$ is at position $x = 0.30 ~\text{m}$ moving at velocity $v = +0.50 ~\text{m s}^{-1}$ at time $t = 0$. Find the amplitude $A$ and the phase angle $\phi$ in the form $x(t) = A\cos(\omega t + \phi)$.

**Solution.** From the velocity-position formula evaluated at $t = 0$:

$$v^2 = \omega^2(A^2 - x^2) \quad \Rightarrow \quad A^2 = x^2 + \frac{v^2}{\omega^2} = 0.30^2 + \frac{0.50^2}{25} = 0.09 + 0.01 = 0.10$$

so $A = 0.316 ~\text{m}$.

For the phase, we use both initial conditions at once. Writing $x(t) = A\cos(\omega t + \phi)$ and differentiating:

$$x(0) = A\cos\phi = 0.30, \qquad v(0) = -A\omega\sin\phi = +0.50.$$

Divide the second by the first: $-\omega\tan\phi = 0.50/0.30 = 5/3$, so $\tan\phi = -1/3$. The cosine is positive (since $x(0) > 0$) and the sine must be negative (so the velocity is positive). Both conditions agree with $\phi$ in the fourth quadrant: $\phi \approx -0.322 ~\text{rad}$ (or equivalently $-18.4°$).

So $x(t) = 0.316\cos(5t - 0.322)$ in metres and seconds.

---

## Beyond syllabus

### Damping — when energy leaks out

Real oscillators lose energy to friction, air resistance, internal heating. The equation becomes

$$m \frac{d^2 x}{dt^2} = -kx - b v$$

where $b > 0$ is the damping coefficient and $v = dx/dt$. The new term $-bv$ opposes motion (proportional to velocity, like air drag at low speed).

Three regimes, distinguished by the discriminant of the characteristic equation (see [[Differential Equations]]):

- **Light damping** ($b^2 < 4mk$) — oscillation continues but amplitude decays exponentially. Period is slightly longer than the undamped value. *This is the typical real-world case.*
- **Critical damping** ($b^2 = 4mk$) — fastest possible return to equilibrium with no overshoot. Used in car suspensions and door closers.
- **Heavy damping** ($b^2 > 4mk$) — slow exponential return, no oscillation at all. Like trying to push a spoon through honey.

The full treatment is in [[Damped Oscillations]]; for 9702 §17.3 and IB Theme C you just need to recognise the three regimes qualitatively.

### Driven oscillations and resonance

Now add an external sinusoidal force $F_0 \cos(\omega_d t)$ at driving frequency $\omega_d$:

$$m \frac{d^2 x}{dt^2} + b\,\frac{dx}{dt} + kx = F_0 \cos(\omega_d t).$$

After transients die out, the steady-state response is sinusoidal at the *driving* frequency $\omega_d$, with amplitude that depends on how close $\omega_d$ is to the natural frequency $\omega_0 = \sqrt{k/m}$.

**Resonance** is the peak: when $\omega_d \approx \omega_0$, the amplitude grows dramatically. With zero damping the amplitude would diverge. With light damping it peaks at $\omega_d = \omega_0$ at a height roughly $1/b$ times the static deflection — a small sustained push, in tune with the natural frequency, builds up to a large oscillation.

**Resonance is responsible for:**
- The Tacoma Narrows bridge collapse (1940) — wind drove the bridge at its torsional natural frequency.
- Why opera singers can shatter wine glasses with the right pitch.
- How tuned circuits in radios select one station out of all the others.
- Why pushing a child on a swing in time with the natural period makes them swing higher.
- How atomic clocks work — caesium atoms have a *very* sharp resonance at 9.192631770 GHz; locking an oscillator to that resonance gives the SI second.

The vault's full treatment lives in [[Resonance]].

### Coupled oscillators and normal modes

Two pendulums connected by a soft spring. Each one's natural frequency is altered by its neighbour; the result is **two coupled second-order ODEs** whose solutions decompose into **normal modes** — collective oscillations of definite frequency. For two identical pendulums coupled symmetrically, the two modes are *in-phase* (both swing together, frequency = pendulum frequency) and *anti-phase* (opposite, frequency = slightly higher because the spring also contributes restoring force).

Three pendulums give three modes; a million atoms in a crystal lattice give a million modes; a continuous string gives infinitely many — and that's how SHM generalises into **wave motion** (see [[Waves I: The Wave Equation]]). Every wave is a coupled SHM of infinitely many neighbours.

### The quantum harmonic oscillator

Recall from [[Hooke's Law for Springs]] §"why every oscillation in nature is Hooke-like" that the electromagnetic field at each spatial frequency behaves like a harmonic oscillator. Quantising the SHM equation $a = -\omega^2 x$ gives the **quantum harmonic oscillator** with energy levels

$$E_n = \left(n + \tfrac{1}{2}\right)\hbar\omega, \qquad n = 0, 1, 2, \ldots$$

The spacing $\hbar\omega$ between levels is the **photon energy** when the oscillator is an EM-field mode at frequency $\omega$. The lowest level $E_0 = \tfrac{1}{2}\hbar\omega$ is the famous **zero-point energy** — the oscillator cannot have *zero* energy even at absolute zero temperature, because the uncertainty principle forbids simultaneously specifying $x = 0$ and $v = 0$. Casimir's 1948 calculation that two metal plates feel a force from the difference in zero-point energies inside vs outside the gap is a measurable consequence of the QHO's existence.

The QHO is **the prototype of every quantum field theory**. Each mode of the electromagnetic field, the electron field, the quark fields, the Higgs field — every one is a quantum harmonic oscillator. SHM is the simplest non-trivial quantum system, and learning it well is learning the deep grammar of how the universe makes particles out of fields.

### Lagrangian view — SHM is the simplest non-trivial Lagrangian

The mass-spring Lagrangian is

$$\mathcal{L} = \tfrac{1}{2}m v^2 - \tfrac{1}{2}kx^2 = \text{KE} - \text{PE}.$$

(Lagrangian mechanics typically writes $\dot{x}$ instead of $v$ — Newton's dot earns its keep here because the Lagrangian is a function of position and velocity treated as independent variables. We'll use it just for this one section.) The Euler-Lagrange equation $\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{x}} = \frac{\partial \mathcal{L}}{\partial x}$ yields $m \dfrac{d^2 x}{dt^2} = -kx$ — the SHM equation, *automatically*. This is the cleanest example in classical mechanics of how the Lagrangian formulation reproduces Newton's laws. Field theories, general relativity, and the Standard Model all start from a Lagrangian; SHM is the training-wheels case.

---

## Exam Notes

### Cambridge 9702 (§17.1 + §17.2 — Paper 4)

- Topic 17 is A-Level-only content, examined on Paper 4 — the AS papers (P1–P3) never touch it. The two rows here: **§17.1** — define amplitude, period, frequency, angular frequency and phase difference; use $a = -\omega^2 x$, $x = x_0\sin\omega t$ (or $\cos$), and $v = \pm\omega\sqrt{x_0^2 - x^2}$; **§17.2** — energy in SHM (KE/PE/total against displacement *and* against time).
- **The definition mark needs both clauses.** "Acceleration is proportional to displacement" alone scores nothing — you must add the direction: *directed towards the fixed (equilibrium) point* / *opposite in direction to the displacement*. The minus sign in words.
- **Notation:** Cambridge writes the amplitude as $x_0$, not $A$ — the data sheet's velocity formula reads $v = \pm\omega\sqrt{x_0^2 - x^2}$. Same quantity, different letter; don't let it disguise a formula you know.
- Favourite question shapes: "show that the motion is simple harmonic" for a mass-spring (set up $F = -kx$, divide by $m$, identify $\omega^2$); read $\omega$, $T$, $x_0$ off a given $x$–$t$ graph; sketch KE/PE against $x$ (two parabolas summing to a constant) or against $t$ (both at *twice* the oscillation frequency — a classic trap); use the $v$–$x$ formula at a named displacement. The damping/resonance row §17.3 is the business of [[Damped Oscillations]] and [[Resonance]].

### IB Physics (C.1)

- **C.1.1 + C.1.2 (SL and HL):** conditions for SHM (restoring force proportional to displacement, directed to equilibrium), $T = 2\pi\sqrt{m/k}$ and $T = 2\pi\sqrt{L/g}$, energy interchange, and the $x(t)$, $v(t)$, $a(t)$ graph family. **C.1.3 (HL only):** the phase angle $\phi$, solving problems with $x = A\cos(\omega t + \phi)$ and the $v$–$x$ relation.
- The data booklet is generous (all the boxed formulas above are printed), so IB marks concentrate on *interpretation*: matching graphs to phases, energy reasoning, and the small-angle limit of the pendulum.

### AP Physics 1 (Unit 7)

- Algebra-based: §7.1–7.4 want the defining relation, the two period formulas, the graph family, and energy conservation — **no calculus derivations**. The velocity–position formula is *not* on the AP sheet; when a problem needs speed at a given displacement, derive it from energy conservation (the Route 2 argument above, which is fully algebra-safe).
- Classic FRQs: justify that period is independent of amplitude (isochronism); design a pendulum experiment to measure $g$ (pairs with [[Repeated Measurements]] — time many oscillations); energy bar charts across the cycle.

### AP Physics C: Mechanics (Unit 7)

- Calculus-based: verify by substitution that $x = A\cos(\omega t + \phi)$ satisfies $\frac{d^2x}{dt^2} = -\omega^2 x$; derive the period of a *physical* pendulum via $\tau = I\alpha$ (the rotational-dynamics trio supplies the machinery); derive the velocity–position relation. The derivations this card walks through in full are exactly the ones AP-C expects you to reproduce.

### Where it is *not* examined

- **9709:** no SHM anywhere in the current syllabus — Paper 4 mechanics stops at particle dynamics, energy and momentum.
- **9231:** the 2026–27 Further Mechanics paper covers projectiles, rigid-body equilibrium, circular motion, Hooke's law, variable-force motion and restitution — **no SHM section**; the closest it comes is elastic-string energy problems (see [[Hooke's Law for Springs]]).
- **0625 IGCSE:** the pendulum appears only in §1.1 measurement — timing a period by counting *multiples* of oscillations — never as SHM theory.

---

## Formula sheet status

| Board | $a = -\omega^2 x$ | $T = 2\pi/\omega$ | $T = 2\pi\sqrt{m/k}$ | $T = 2\pi\sqrt{L/g}$ | $v = \pm\omega\sqrt{A^2 - x^2}$ |
|---|---|---|---|---|---|
| Cambridge 9702 (P4) | On data sheet | On data sheet | On data sheet | On data sheet | **On data sheet** |
| IB Physics | On data booklet | On data booklet | On data booklet | On data booklet | On data booklet |
| AP Physics 1 | On formula sheet | On formula sheet | On formula sheet | On formula sheet | Not printed (derive) |
| AP Physics C Mech | On formula sheet | On formula sheet | On formula sheet | On formula sheet | Not printed (derive) |

**Takeaway.** Cambridge and IB are *unusually generous* — the velocity-position formula is rare to find on a formula sheet, and they print it. AP gives you the periods but expects derivation of the velocity-position relation. Practising the energy-conservation derivation is therefore *more* important for AP than for Cambridge/IB.

---

## Connections

- **Parent:** [[Hooke's Law for Springs]] — the force law whose dynamics this card resolves. Every claim about SHM's universality runs back through Hooke's Taylor-expansion theorem.

- **Mathematical prerequisites:**
   - [[Differentiation]] + [[Differential Equations]] — the ODE $\dfrac{d^2 x}{dt^2} = -\omega^2 x$ is the first second-order linear ODE most physics students meet; every later one (LC circuits, beam vibrations, Schrödinger's equation) is calibrated against it.
   - [[Trigonometric Functions]] — the sin/cos solutions, the phase relationships, the amplitude–phase identities.
   - [[Radians]] — the squeeze-theorem proof of $\lim_{h \to 0} \sin h / h = 1$ is the analytic backbone of the pendulum's small-angle approximation. Two equivalent lenses: that limit + the Maclaurin polynomial truncation.
   - [[Maclaurin Series]] — the small-angle approximation $\sin\theta \approx \theta$ is a one-term Taylor truncation; the bridge from non-SHM to SHM in the pendulum.
   - [[Work, Energy and Power]] — energy conservation is one of the two routes to the solution.

- **Rotational-dynamics siblings (referenced in the pendulum derivation):**
   - [[Forces and Equilibrium]] — moments of a force (the static side of torque) already lives here.
   - [[Torque]], [[Moment of Inertia]], [[Angular Momentum]] — the dynamical trio that powers the pendulum's $\tau = I\,\dfrac{d^2\theta}{dt^2}$ derivation. The full treatments live in those cards.

- **Children:**
   - [[Damped Oscillations]] — adds the $-bv$ term; three regimes (light, critical, heavy).
   - [[Resonance]] — driven oscillator with sinusoidal forcing; the peak at $\omega_d = \omega_0$.
   - [[Coupled Oscillators]] — two-pendulum normal-mode decomposition; the bridge to waves.
   - [[Pendulums]] — the simple pendulum, the physical pendulum, the conical pendulum; large-angle anharmonicity.
   - [[Waves I: The Wave Equation]] — coupled SHM of infinitely many neighbours; the spatial generalisation.
   - [[The Quantum Harmonic Oscillator]] — the quantum version; energy levels $(n + \tfrac{1}{2})\hbar\omega$; the prototype of quantum field theory.

- **Cross-domain bridges:**
   - [[Differential Equations]] — SHM is the canonical second-order linear homogeneous ODE.
   - [[Trigonometric Graphs]] — every SHM phase relationship is a graphical statement about sin and cos.
   - **Electrical analogue:** the LC circuit $L_{\text{ind}} \dfrac{d^2 Q}{dt^2} + Q/C = 0$ is mathematically identical to SHM, with inductance $L_{\text{ind}} \leftrightarrow m$ and inverse capacitance $1/C \leftrightarrow k$. The "mechanical" intuition transfers directly. (Note: in the LC equation $L_{\text{ind}}$ means inductance, *not* pendulum length.)

- **Misconceptions cleared:** period does **not** depend on amplitude (the isochronism that makes pendulum clocks work); SHM does **not** require springs (any smooth stable equilibrium produces SHM at small amplitude); velocity and displacement are **not** in phase (90° apart); a pendulum is **not** strictly SHM (the $\sin\theta$ approximation matters for large angles).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $a = -\omega^2 x$ | `a = -\omega^2 x` | The SHM equation — Cambridge/IB/AP all write it this way |
| $\dfrac{d^2 x}{dt^2} = -\omega^2 x$ | `\frac{d^2 x}{dt^2} = -\omega^2 x` | Same equation, Leibniz form — used when ODE structure matters |
| $\dot{x}, \ddot{x}$ | `\dot{x}, \ddot{x}` | Newton's compact dot shorthand for $dx/dt, d^2 x/dt^2$. Useful in Lagrangians; this card otherwise uses $v$, $a$, or Leibniz. |
| $\omega$ | `\omega` | Angular frequency in oscillation context; angular velocity in rotation context. Same number, two names. Units: $\text{rad s}^{-1}$ |
| $T = 2\pi/\omega$ | `T = 2\pi / \omega` | Period from angular frequency |
| $T = 2\pi\sqrt{m/k}$ | `T = 2\pi\sqrt{m/k}` | Mass-spring period |
| $T = 2\pi\sqrt{L/g}$ | `T = 2\pi\sqrt{L/g}` | Simple pendulum period (small angles) |
| $x(t) = A\cos(\omega t + \phi)$ | `x(t) = A\cos(\omega t + \phi)` | General SHM solution |
| $v = \pm\omega\sqrt{A^2 - x^2}$ | `v = \pm\omega\sqrt{A^2 - x^2}` | Velocity-position relation |
| $E = \tfrac{1}{2}kA^2$ | `E = \tfrac{1}{2}kA^2` | Total mechanical energy |
| $v_{\max} = A\omega$ | `v_{\max} = A\omega` | Max speed at equilibrium |
| $a_{\max} = A\omega^2$ | `a_{\max} = A\omega^2` | Max acceleration at turning points |
| $E_n = (n + \tfrac{1}{2})\hbar\omega$ | `E_n = (n + \tfrac{1}{2})\hbar\omega` | Quantum harmonic oscillator levels |
