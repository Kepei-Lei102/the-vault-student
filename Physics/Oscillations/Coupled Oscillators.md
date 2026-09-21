---
chinese: 耦合振子 (ǒuhé zhènzǐ)
prerequisites:
  - "[[Simple Harmonic Motion]]"
  - "[[Resonance]]"
  - "[[Differential Equations]]"
leads_to: []
tags:
  - subject/physics
  - domain/oscillations
  - level/university
  - type/deep
  - type/definition
  - type/proof
  - notation/normal-coordinate
  - notation/omega-angular-frequency
  - misconception/coupling-is-damping
  - misconception/each-body-is-a-normal-mode
  - misconception/energy-transfer-is-always-complete
---

# Coupled Oscillators 耦合振子

Pull one of two spring-linked pendulums aside and release it. Its neighbour starts moving. The first pendulum's swing shrinks while the second's grows; later, the motion comes back. Nobody keeps pushing. Nothing is making new energy.

**The connection lets each oscillator do work on the other.** The surprise is that this changing motion can be built from two patterns whose amplitudes never change.

![[coupled-oscillators-manim.mp4]]

*First move together, then move oppositely, then release only the left pendulum. The final scene tracks three energy stores: each pendulum and the coupling spring. Motion follows the linear small-angle model; no damping is included.*

## Definition

### Formal

**Coupled oscillators** are oscillating systems whose equations of motion depend on one another's coordinates or velocities. The coupling permits energy transfer between parts.

For a conservative linear system near a stable equilibrium, a **normal mode** is a motion in which every moving coordinate oscillates at one angular frequency with fixed relative amplitudes. In a real mode of the systems considered here, moving parts are in phase or in antiphase; some parts may remain still.

A mode is a pattern of the **whole system**, not the motion of one selected body. General motion is a superposition of modes, with their amplitudes and phases set by the initial conditions.

### Intuitive

Two people carrying opposite ends of a tray can move it sideways together, or move their ends in opposite directions and turn it. “Where is each person's hand?” is one description. “How far did the tray shift, and how far did it turn?” is another. The second description separates two kinds of motion that the first mixes together.

Normal coordinates do that for oscillators: choose collective motions in which the force law becomes simple.

### 中文锚点 (Chinese Anchor)

想象两只并排挂着的小摆，摆球之间连着一根软弹簧。你只拨动左边那只，右边本来没动，却也慢慢荡起来；左边反而越荡越小。能量没有凭空消失，是中间的弹簧一拉一推，把运动传给了邻居。过一会儿，右边又能把它传回来。**耦合**说的就是这种“你一动，也会牵动我”的联系：两只摆各自的动静会变，能量却可以留在它们和弹簧组成的整体里。

## Notation

| Symbol | Meaning | Units / convention |
|---|---|---|
| $x_1,x_2$ | displacements from equilibrium | metres; both positive to the right |
| $m$ | mass of each oscillator | kg; equal masses in the first model |
| $k$ | restoring stiffness of each uncoupled oscillator | N m$^{-1}$ |
| $\kappa$ | coupling-spring stiffness | N m$^{-1}$; distinct from $k$ |
| $q_+,q_-$ | together and opposite normal coordinates | metres; defined below |
| $\omega_+,\omega_-$ | together and opposite angular frequencies | rad s$^{-1}$; here $\omega_->\omega_+$ |
| $\Delta\omega$ | $\omega_--\omega_+$ | positive when $\kappa>0$ |

The subscripts $+$ and $-$ name **sums and differences**, not higher and lower frequency. Other books may number the same modes 1 and 2.

## Key Facts — two bodies, two simple patterns

### 1. Build the forces before guessing the motion

Use two equal masses on a frictionless line. Each has its own spring of stiffness $k$ connected to a fixed wall; a middle spring of stiffness $\kappa$ joins the masses. Measure displacements from the configuration in which all three springs are unstretched.

The middle spring's extension is $x_2-x_1$: moving the right mass right stretches it, but moving the left mass right shortens it. Its forces on the two masses are equal and opposite.

**Tool: Hooke's law, then Newton's second law.** The connection is the reason each equation needs both positions:

$$\boxed{m\frac{d^2x_1}{dt^2}=-kx_1+\kappa(x_2-x_1),\qquad
m\frac{d^2x_2}{dt^2}=-kx_2-\kappa(x_2-x_1).}$$

A displaced mass does not generally have acceleration proportional to **its own** displacement alone. Its neighbour matters. So neither mass must execute SHM by itself.

### 2. Let symmetry choose the coordinates

Identical masses and identical outer springs mean exchanging labels 1 and 2 leaves the apparatus unchanged. Try a sum, which survives the exchange, and a difference, which reverses sign:

$$q_+=\frac{x_1+x_2}{2},\qquad q_-=\frac{x_1-x_2}{2}.$$

These are invertible definitions:

$$x_1=q_++q_-,\qquad x_2=q_+-q_-.$$

**Add the two force equations.** The middle spring's forces cancel:

$$m\frac{d^2(x_1+x_2)}{dt^2}=-k(x_1+x_2)
\quad\Longrightarrow\quad\frac{d^2q_+}{dt^2}=-\frac{k}{m}q_+.$$

**Subtract the second equation from the first.** The middle spring's contributions reinforce:

$$m\frac{d^2(x_1-x_2)}{dt^2}=-(k+2\kappa)(x_1-x_2)
\quad\Longrightarrow\quad\frac{d^2q_-}{dt^2}=-\frac{k+2\kappa}{m}q_-.$$

We have replaced two coupled equations with **two independent SHM equations**:

$$\boxed{\omega_+=\sqrt{\frac{k}{m}},\qquad
\omega_-=\sqrt{\frac{k+2\kappa}{m}}.}$$

![[coupled-oscillators-modes.svg|750]]

*Arrows show displacements from the dotted equilibrium positions, not velocities. In the together mode the middle spring keeps its equilibrium length. In the opposite mode each mass feels extra restoring force.*

The factor $2\kappa$ has a physical explanation: if $x_1=x$ and $x_2=-x$, the middle spring changes length by $-2x$. There is only one coupling spring; its extension is twice one mass's displacement.

### 3. Recover every initial condition

Each normal coordinate has its own amplitude and phase:

$$q_+=A_+\cos(\omega_+t+\phi_+),\qquad
q_-=A_-\cos(\omega_-t+\phi_-).$$

There are four constants because two second-order equations need four initial values: two positions and two velocities. Equivalently write each mode as a cosine term plus a sine term; this avoids ambiguous phases when a mode's amplitude is zero.

For example, $q_+(0)=[x_1(0)+x_2(0)]/2$ and $dq_+/dt(0)=[v_1(0)+v_2(0)]/2$, with subtraction giving the other mode. Solve two ordinary SHM initial-value problems and transform back.

**A pure mode needs the velocities as well as the positions to match.** Setting $x_1=x_2$ at one instant is insufficient if $v_1\ne v_2$.

### 4. Why one pendulum seems to give its motion away

Release only oscillator 1:

$$x_1(0)=A,\qquad x_2(0)=0,\qquad v_1(0)=v_2(0)=0.$$

The initial normal coordinates are both $A/2$, with zero velocity. Therefore

$$x_1=\frac{A}{2}[\cos(\omega_+t)+\cos(\omega_-t)],\qquad
x_2=\frac{A}{2}[\cos(\omega_+t)-\cos(\omega_-t)].$$

Define $\bar\omega=(\omega_++\omega_-)/2$. The sum-to-product identities give

$$\boxed{x_1=A\cos(\bar\omega t)\cos\left(\frac{\Delta\omega t}{2}\right),\qquad
x_2=A\sin(\bar\omega t)\sin\left(\frac{\Delta\omega t}{2}\right).}$$

Each fast oscillation has a changing envelope. When coupling is weak, $\Delta\omega\ll\bar\omega$, so the slow rise and fall is easy to distinguish from the fast swings. This is the same interference arithmetic as [[Superposition and Interference#Part VI — Beats: interference in time instead of space|beats]].

The first zero of oscillator 1's envelope occurs at

$$t_{\mathrm{handover}}=\frac{\pi}{\Delta\omega};\qquad
T_{\mathrm{envelope}}=\frac{2\pi}{\Delta\omega}=\frac{1}{f_--f_+}.$$

The latter is the recurrence time of the **envelope magnitude**, not necessarily a return of the complete positions and velocities. Exact state recurrence also requires commensurate mode frequencies.

> [!warning] An envelope zero is not automatically zero energy
> At $t=\pi/\Delta\omega$, $x_1=0$, but differentiating the product gives $v_1=-(A\Delta\omega/2)\cos(\bar\omega t)$ there. That can be non-zero. Moreover, the coupling spring can still store energy. “Complete transfer” is usually a weak-coupling approximation, or a statement with a carefully specified energy convention.

### 5. Follow the energy through all three stores

With $v_i=dx_i/dt$, define the two local oscillator energies and the coupling energy:

$$E_1=\tfrac12mv_1^2+\tfrac12kx_1^2,\quad
E_2=\tfrac12mv_2^2+\tfrac12kx_2^2,\quad
E_c=\tfrac12\kappa(x_2-x_1)^2.$$

**Tool: power equals force times velocity.** Using the equations of motion,

$$\frac{dE_1}{dt}=\kappa(x_2-x_1)v_1,\quad
\frac{dE_2}{dt}=-\kappa(x_2-x_1)v_2,\quad
\frac{dE_c}{dt}=\kappa(x_2-x_1)(v_2-v_1).$$

Add them: every term cancels. Thus $E_1+E_2+E_c$ is constant although its parts change.

![[coupled-oscillators-exchange.svg|750]]

*Exact linear-model traces for $m=1$, $k=4$, $\kappa=0.42$, $A=0.40$ in SI units. Dashed curves are signed amplitude factors; their negatives complete the envelopes. The vertical dotted line marks the first envelope handover. Notice the purple energy store.*

Now substitute $x_1=q_++q_-$ and $x_2=q_+-q_-$ into the total energy. The cross terms cancel:

$$E=\underbrace{m\left(\frac{dq_+}{dt}\right)^2+kq_+^2}_{E_+}
+\underbrace{m\left(\frac{dq_-}{dt}\right)^2+(k+2\kappa)q_-^2}_{E_-}.$$

Each bracket is separately constant. **The bodies exchange energy; the ideal independent modes do not.** There is no contradiction: “body 1” and “mode +” divide the system in different ways.

## Special Cases — know the model's edges

- **No coupling, $\kappa=0$:** the frequencies coincide and there is no transfer. Sum and difference still work, but no longer pick unique preferred modes; any independent combination works.
- **Both masses displaced equally and released:** only the together mode is excited. A connection does not force energy to shuttle between the bodies.
- **Small-angle pendulums:** for equal bob masses and lengths $L$, gravity gives $F_x\approx-(mg/L)x$. Replace $k$ by $mg/L$. A light horizontal spring joining the bobs gives $\omega_+^2=g/L$ and $\omega_-^2=g/L+2\kappa/m$. A spring attached partway up each rod has a different effective coupling because its extension and torque arms change.
- **Unequal oscillators:** equal/opposite displacements generally cease to be the mode shapes. A large mismatch between uncoupled frequencies can greatly reduce energy exchange; solve for the actual shapes rather than assuming equal sharing.
- **Damping or forcing:** energy can leave or enter. Undamped normal modes remain a useful starting point, but generic damping need not separate in the same coordinates. Large-angle pendulums and nonlinear springs also break the exact linear superposition used above.

## Worked Examples

### 1. Predict the handover — and check the energy

Two $1.00\ \mathrm{kg}$ masses have $k=4.00\ \mathrm{N\,m^{-1}}$ and $\kappa=0.420\ \mathrm{N\,m^{-1}}$. Pull mass 1 to $0.400\ \mathrm m$, leave mass 2 at equilibrium, and release both from rest. These are ideal-model parameters, not instructions to stretch an arbitrary classroom spring.

**Step 1 — tool: symmetry-selected modes.** Equal masses and equal outer springs select the sum/difference coordinates:

$$\omega_+=2.00\ \mathrm{rad\,s^{-1}},\qquad
\omega_-=\sqrt{4.84}=2.20\ \mathrm{rad\,s^{-1}}.$$

**Step 2 — tool: frequency difference.** Only one mass is displaced, so both modes start with amplitude $0.200\ \mathrm m$. The first envelope handover is

$$t_h=\frac{\pi}{0.20}=5\pi\ \mathrm s\approx15.71\ \mathrm s.$$

**Step 3 — tool: substitute before claiming complete transfer.** Here $\omega_+t_h=10\pi$ and $\omega_-t_h=11\pi$, so

$$x_1=0,\quad x_2=0.400\ \mathrm m,\quad v_1=v_2=0.$$

This specially chosen frequency ratio makes both bodies instantaneously stationary at handover. Nevertheless,

$$E_1=0,\quad E_2=\tfrac12(4)(0.4)^2=0.3200\ \mathrm J,\quad
E_c=\tfrac12(0.42)(0.4)^2=0.0336\ \mathrm J.$$

The constant total is $0.3536\ \mathrm J$. The right oscillator holds about $90.5\%$, and the coupling spring holds the rest. “All the energy is in the right mass” would still be wrong.

### 2. A pure mode hiding inside four numbers

Use the same apparatus, but start with $x_1=0.030\ \mathrm m$, $x_2=-0.030\ \mathrm m$, $v_1=0.044\ \mathrm{m\,s^{-1}}$ and $v_2=-0.044\ \mathrm{m\,s^{-1}}$.

**Tool: transform the whole initial state.** Opposite positions **and** opposite velocities give $q_+(0)=dq_+/dt(0)=0$. Only $q_-$ survives:

$$q_-(t)=0.030\cos(2.20t)+\frac{0.044}{2.20}\sin(2.20t)
=0.030\cos(2.20t)+0.020\sin(2.20t).$$

**Tool: combine perpendicular sine/cosine coefficients.** The amplitude is $\sqrt{0.030^2+0.020^2}=0.0361\ \mathrm m$. The bodies remain opposite, $x_1=q_-$ and $x_2=-q_-$, at one frequency. There is no slow beating envelope.

## Where this actually works — protecting a skyscraper

Standing near the top of a tall building, a small sway can be unpleasant even if the structure is safe. Taipei 101 suspends a **660-tonne tuned mass damper** inside the tower, with hydraulic dampers connected to it. The building's own description identifies reducing wind-induced sway and improving comfort as its main purpose. [Taipei 101: wind damping ball](https://www.taipei-101.com.tw/en/observatory/feature).

Treat one building-sway mode as a large mass on an effective spring. Add the suspended mass: now there are **two coupled degrees of freedom**. The added mass changes the response near the troublesome frequency, and the hydraulic dampers dissipate mechanical energy as heat. An undamped companion would merely store and return energy.

A small ideal calculation explains the tuning. Let $X$ be building displacement, $Y$ absorber displacement, and let absorber mass $m_a$ be linked to the building by stiffness $k_a$. Under harmonic motion at driving frequency $\Omega$, the absorber's equation becomes

$$-m_a\Omega^2Y=-k_a(Y-X),\qquad
(k_a-m_a\Omega^2)Y=k_aX.$$

At $\Omega^2=k_a/m_a$, this equation permits a response with $X=0$: the absorber moves while its force balances the applied periodic load on the building. This is **antiresonance** in the ideal undamped two-degree-of-freedom model. Real damping, changing winds and multiple building modes mean engineers design a useful frequency range, not a magical all-frequency cancellation. The relative phase depends on frequency; “the ball always moves opposite the building” is too simple.

## Hands-on — make the model answer back

For a physical glimpse, hang two similar light pendulums from a taut horizontal string, give only one a small displacement, and watch their amplitudes. The flexible support supplies coupling; it is **not** the exact bob-to-bob spring used in the formulas. Keep the bobs light, the supports secure and the swings small. Unequal lengths and friction can spoil a neat transfer; that is evidence about the model, not a failed experiment.

For a reproducible numerical experiment, run this with Python and NumPy:

```python
import numpy as np
m, k, coupling, A = 1.0, 4.0, 0.42, 0.4
wp = np.sqrt(k / m)
wm = np.sqrt((k + 2 * coupling) / m)
t = np.linspace(0, 2 * np.pi / (wm - wp), 2001)
x1 = A / 2 * (np.cos(wp*t) + np.cos(wm*t))
x2 = A / 2 * (np.cos(wp*t) - np.cos(wm*t))
v1 = -A / 2 * (wp*np.sin(wp*t) + wm*np.sin(wm*t))
v2 = -A / 2 * (wp*np.sin(wp*t) - wm*np.sin(wm*t))
E1 = (m*v1**2 + k*x1**2) / 2
E2 = (m*v2**2 + k*x2**2) / 2
Ec = coupling * (x2-x1)**2 / 2
print("First envelope handover / s:", np.pi / (wm-wp))
print("Total-energy range / J:", np.ptp(E1+E2+Ec))
```

Expect about $15.71$ s and an energy range near floating-point round-off. Change the coupling to $0.10$: the handover slows to about $63.6$ s. **Predict before running:** why does a weaker connection need longer? For zero coupling, remove the time formula's division by zero and use any fixed time interval; oscillator 2 then remains still.

## Common Misconceptions

1. **“Each pendulum is one mode.”** Point to both masses in each mode picture. A mode specifies a displacement ratio across the entire system.
2. **“Smaller amplitude means energy was lost.”** Inspect all three stores. Coupling redistributes energy; [[Damped Oscillations]] describes loss from the mechanical system.
3. **“The coupling spring always raises both frequencies.”** Move both masses equally: the middle spring does not change length. That symmetry protects $\omega_+$ in this model.
4. **“Normal modes only exist because the masses are identical.”** Symmetry makes them easy to guess. Linear algebra finds them when guessing fails.
5. **“Beat period is the time to give the motion away.”** One-way envelope handover is half the envelope recurrence time. Neither guarantees exact recurrence of the complete state.

## Exam Notes

**Positioning: enrichment; coupled-mode calculations are not named requirements of the physics courses below.** Single-oscillator SHM, superposition and resonance supply examinable ingredients; the two-coordinate eigenmode calculation is an extension. A supplied unfamiliar model can still ask you to apply Newton's laws or solve given equations.

- **Cambridge 9702, 2028–2030, §17.1–17.3:** SHM, energy, damping and resonance. The syllabus does not prescribe deriving coupled-mode frequencies or exchange times. Use [[Simple Harmonic Motion]], [[Damped Oscillations]] and [[Resonance]] for that assessed core.
- **Cambridge 0625, 2026–2028:** timing repeated oscillations in §1.1 and wave properties in §3.1; no coupled-oscillator or normal-mode calculation is prescribed.
- **IB Physics, first assessment 2025, C.1–C.4:** SHM, waves, superposition, standing waves and resonance provide connections. Mechanical normal-mode diagonalisation is not a listed requirement. Standing-wave harmonics are modes, but deriving a two-mass eigenproblem is additional depth.
- **AP Physics 1 and AP Physics C: Mechanics, Unit 7:** oscillations, forces and energy are relevant foundations. The C course adds calculus and physical pendulums; neither CED names coupled-mode diagonalisation as required content. **AP Physics 2** examines waves/interference connections, not this mechanical eigenproblem. **AP Physics C: E&M** likewise does not prescribe it; electrical resonance analogies must not be mistaken for an extra course requirement.
- **Maths bridge:** Cambridge **9231 §2.2** examines eigenvalues/eigenvectors and **§2.6** differential equations, so the matrix reasoning below applies those tools. Cambridge 9709, 0580, 0606, OxfordAQA 9260/9660 and Edexcel IAL Mathematics do not name this mechanical normal-mode treatment as a required topic; a broader maths technique appearing there is not a claim that this physical application is separately examined.

**Formula-sheet consequence:** do not memorise a coupled-frequency pair as a universal rule. It depends on this apparatus. Derive its stiffness equations; use the single-oscillator formulas provided or required by your own course. The worked examples above are original teaching examples, not past-paper questions.

## Beyond Syllabus — eigenvectors that you can watch

### When symmetry is not enough

Recall that a normal mode keeps fixed displacement ratios. Put those ratios into a vector $\mathbf a$ and try $\mathbf x(t)=\mathbf a\cos(\omega t+\phi)$. For our equal pair,

$$m\frac{d^2\mathbf x}{dt^2}=-\mathbf K\mathbf x,\qquad
\mathbf K=\begin{pmatrix}k+\kappa&-\kappa\\-\kappa&k+\kappa\end{pmatrix}.$$

Substitution gives $\mathbf K\mathbf a=m\omega^2\mathbf a$. Thus $(1,1)^T$ and $(1,-1)^T$ are eigenvectors of the stiffness matrix; its eigenvalues are $k$ and $k+2\kappa$. **The eigenvector is the motion's shape; the eigenvalue divided by mass is its squared angular frequency.** This is the physical meaning behind [[Eigenvalues and Eigenvectors]].

With unequal masses, write the diagonal mass matrix $\mathbf M$. Then

$$\boxed{\mathbf K\mathbf a=\omega^2\mathbf M\mathbf a,\qquad
\det(\mathbf K-\omega^2\mathbf M)=0.}$$

The determinant must vanish because a nonsingular matrix would force $\mathbf a=0$, which is no motion. This is a **generalised eigenvalue problem**. Its eigenvalues are $\omega^2$, not $\omega$.

Why does a full set of real modes exist? For positive masses and conservative linear springs, $\mathbf M^{-1/2}\mathbf K\mathbf M^{-1/2}$ is real symmetric. It has an orthogonal eigenbasis. Transforming back gives mass-weighted orthogonality, $\mathbf a_i^T\mathbf M\mathbf a_j=0$ for distinct modes. With a positive-definite stiffness matrix all squared frequencies are positive; zero stiffness directions permit rigid motion, and negative ones indicate instability.

### From two neighbours to a wave

Recall that each spring responds to a **difference** of neighbouring displacements. For an infinite uniform chain with mass $m$, spacing $a$ and nearest-neighbour stiffness $\kappa$,

$$m\frac{d^2x_j}{dt^2}=\kappa(x_{j+1}-2x_j+x_{j-1}).$$

Try a travelling pattern $x_j=A\cos(qja-\omega t)$, where $q$ is wave number. Adding the neighbours gives $2\cos(qa)x_j$, hence

$$-m\omega^2x_j=2\kappa[\cos(qa)-1]x_j
\quad\Longrightarrow\quad
\boxed{\omega^2=\frac{4\kappa}{m}\sin^2\left(\frac{qa}{2}\right).}$$

For wavelengths much larger than $a$, $\sin(qa/2)\approx qa/2$, giving $\omega\approx a\sqrt{\kappa/m}\,|q|$. A long chain becomes the familiar wave equation in the continuum limit. At shorter wavelengths, frequency is no longer proportional to wave number: the chain is dispersive.

A finite chain's boundaries select allowed mode shapes. This links [[Progressive Waves]], [[Stationary Waves]] and [[Fourier Series]]: many local coordinates, a set of collective patterns, and general motion assembled from them. Count modes by independent coordinates: a three-dimensional collection of $N$ unconstrained point masses has $3N$ coordinates, not just $N$.

## Connections

- **Parents:** [[Simple Harmonic Motion]] supplies each separated equation; [[Differential Equations]] supplies initial-value reasoning; [[Resonance]] explains a system's response to a driver.
- **Mathematical lens:** [[Eigenvalues and Eigenvectors]] — mode shapes and squared frequencies; [[Trigonometric Identities]] — the sum-to-product step that exposes the envelope.
- **Compare:** [[Superposition and Interference]] — beats from nearby frequencies; [[Damped Oscillations]] — genuine loss rather than transfer.
- **Many-body extensions:** [[Progressive Waves]], [[Stationary Waves]], [[Fourier Series]] — collective patterns and their superposition.
- **Further demonstration and derivation:** [MIT 8.03, coupled oscillators and normal modes](https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/pages/part-i-mechanical-vibrations-and-waves/lecture-4/).

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\kappa$ | `\kappa` | coupling stiffness |
| $q_\pm$ | `q_\pm` | normal coordinates |
| $\Delta\omega$ | `\Delta\omega` | angular-frequency splitting |
| $\mathbf K\mathbf a=\omega^2\mathbf M\mathbf a$ | `\mathbf K\mathbf a=\omega^2\mathbf M\mathbf a` | generalised eigenvalue equation |
| $\det(\mathbf K-\omega^2\mathbf M)$ | `\det(\mathbf K-\omega^2\mathbf M)` | characteristic determinant |
