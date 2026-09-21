---
chinese: 量子态与薛定谔方程 (liàngzǐ tài yǔ Xuēdìng'è fāngchéng)
aliases:
  - Quantum States
  - Schrödinger Equation
  - Wavefunction
  - Particle in a Box
prerequisites:
  - "[[Wave-Particle Duality]]"
  - "[[Stationary Waves]]"
  - "[[Complex Numbers]]"
  - "[[Integration]]"
leads_to:
  - "[[Quantum Tunnelling]]"
  - "[[Pauli Exclusion Principle]]"
tags:
  - subject/physics
  - domain/quantum
  - level/university
  - type/deep
  - type/derivation
  - notation/wavefunction
  - misconception/amplitude-is-probability
  - misconception/superposition-is-mixture
  - misconception/stationary-means-motionless
---

# Quantum States and the Schrödinger Equation 量子态与薛定谔方程

> *A wavefunction is a recipe for probabilities. Keep its phase until the very last step.*

## Definition

### Formal

For one nonrelativistic particle moving along one coordinate, ignoring spin, a **pure quantum state** can be represented by a complex wavefunction $\psi(x,t)$. The **Born rule** converts it into a position probability density:

$$\rho(x,t)=|\psi(x,t)|^2=\psi^*(x,t)\psi(x,t),\qquad P(a<x<b)=\int_a^b|\psi(x,t)|^2\,dx.$$

A physical state is **normalised**: $\int_{-\infty}^{\infty}|\psi|^2dx=1$. Between measurements, for a particle with mass $m$ and prescribed scalar potential energy $V(x,t)$, its evolution obeys

$$\boxed{i\hbar\frac{\partial\psi}{\partial t}=\hat H\psi
=\left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x,t)\right]\psi,\qquad \hbar=\frac{h}{2\pi}.}$$

This is the **Schrödinger equation**. The hat means an *operator*: a rule acting on a function. Here $\hat H$ differentiates twice, scales the result and adds $V\psi$. Magnetic vector potentials, relativistic particles, spin and many-particle states require a broader formulation.

### Intuitive — the string is a bridge, not an electron photograph

A string fixed at both ends cannot vibrate in any shape at one frequency. Its boundary conditions select modes. A confined electron has a related mathematical problem: which wavefunctions obey both the dynamical equation and the boundaries?

The crucial difference is what the curve means. String displacement is a physical distance. An electron wavefunction is a **probability amplitude**. Squaring its modulus gives a density; integrating that density predicts the fraction of identically prepared position measurements landing in a region. Each detection still produces a local result.

| Familiar idea | Quantum counterpart | What changes |
|---|---|---|
| String mode | Stationary wavefunction | The curve is an amplitude, not a material string |
| Adding waves | Superposing states | Add complex amplitudes before finding probabilities |
| Classical energy $p^2/2m+V$ | Hamiltonian $\hat H$ | Momentum becomes a derivative operator |
| Frequency content | Momentum distribution | Wavenumber corresponds to $p=\hbar k$ |

### 中文锚点

戴上降噪耳机，耳机明明又发出了声音，耳边反而安静了：两股声波的起伏恰好错开，一个的峰正好对着另一个的谷，就能互相抵消。理解量子态，也要先保留这种“怎样起伏”的信息。不能一上来就把每一部分换成概率再相加；要先把振幅合起来，再算概率，才不会漏掉相消的效果。耳机里的声波不是电子的波函数，但它提醒我们：只记“有多强”，丢掉彼此的节奏关系，就会算错合在一起的效果。

## Notation

| Symbol | Meaning | Units in this one-dimensional model |
|---|---|---|
| $\psi$ | wavefunction / probability amplitude | $\mathrm{m^{-1/2}}$ |
| $\psi^*$ | complex conjugate | $\mathrm{m^{-1/2}}$ |
| $\rho=\lvert\psi\rvert^2$ | position probability density | $\mathrm{m^{-1}}$ |
| $\phi_n$ | normalised energy eigenfunction | $\mathrm{m^{-1/2}}$ |
| $c_n$ | amplitude for energy state $n$ | dimensionless |
| $\langle A\rangle$ | expectation value of observable $A$ | same as $A$ |
| $\Delta A$ | standard deviation of outcomes of $A$ | same as $A$ |
| $\hbar$ | reduced Planck constant, $h/(2\pi)$ | $\mathrm{J\,s}$ |

> [!warning] Density is not probability
> A density can exceed $1\ \mathrm{m^{-1}}$; an integrated probability cannot exceed 1. For a continuous position distribution, a single exact point has zero probability because it has zero width. A detector has a finite-sized pixel or bin. Do not infer that an outcome is forbidden just because its singleton has probability zero. [[Continuous Random Variables]] uses the same density-versus-area distinction.

## 1. Normalisation and phase — what information is in the state?

Write $\psi=R e^{i\theta}$, with $R\geq0$. Then $|\psi|^2=R^2$: the local phase $\theta$ disappears from a position-density plot. It does **not** disappear from the whole physics. Two amplitudes can reinforce or cancel when added.

For a complex number $a+ib$, use $|a+ib|^2=a^2+b^2$, not $(a+ib)^2$. Negative real amplitudes are allowed; negative probabilities are not.

![[quantum-states-amplitude-density.svg|760]]

*The dimensionless horizontal coordinate is $x/L$. Amplitudes are scaled by $\sqrt L$ and densities by $L$, so both plotted densities integrate to one over $x/L$. The shaded area is the probability in the middle half; it is not the height of the curve. The sign change in the $n=2$ amplitude becomes a node in its density.*

### Global phase versus relative phase

Multiplying the **entire state** by one constant $e^{i\alpha}$ changes no measurement probability: in $\langle A\rangle=\int\psi^*\hat A\psi\,dx$, the two constant phase factors cancel. Thus $\psi$ and $-\psi$ describe the same pure state.

But $\phi_1+\phi_2$ and $\phi_1-\phi_2$ generally do not. Only one component changed sign; their **relative phase** changed. The cross term in the squared modulus changes sign with it.

A position density by itself is therefore insufficient to specify a state. For example, multiplying a wavepacket by $e^{ik_0x}$ preserves its position density but shifts its momentum distribution. This phase depends on position; it is not a global constant.

### Worked example 1 — normalise before predicting

Suppose $\psi(x)=A\sin(\pi x/L)$ for $0<x<L$, and zero outside. Find $A$ and the probability of detecting the particle in $0<x<L/4$.

**Tool: total probability equals one. Trigger: an unknown amplitude multiplies a known shape.**

$$1=|A|^2\int_0^L\sin^2(\pi x/L)\,dx=|A|^2\frac L2.$$

Choose the irrelevant global phase so $A$ is positive: $A=\sqrt{2/L}$.

**Tool: integrate density over the requested interval. Trigger: a range of positions, not a single point.** With $\sin^2u=(1-\cos2u)/2$,

$$P(0<x<L/4)=\frac2L\int_0^{L/4}\sin^2(\pi x/L)\,dx
=\boxed{\frac14-\frac1{2\pi}\approx0.09085}.$$

The left quarter contains only about 9.1% of detections. Equal lengths do not imply equal probabilities when the density varies.

## 2. Why this differential equation?

The Schrödinger equation is a **physical postulate**, supported by experiments in its domain. We can motivate its form; we cannot prove quantum dynamics from classical mechanics alone.

**Tool: test an operator on a plane wave. Trigger: de Broglie connects wavelength with momentum.** For $\psi=e^{i(kx-\omega t)}$,

$$-i\hbar\frac{\partial\psi}{\partial x}=\hbar k\psi=p\psi,
\qquad i\hbar\frac{\partial\psi}{\partial t}=\hbar\omega\psi=E\psi.$$

Thus $\hat p=-i\hbar\partial_x$ and $\hat E=i\hbar\partial_t$ reproduce $p=\hbar k$ and $E=\hbar\omega$. Putting the kinetic-energy operator $\hat p^2/(2m)$ beside the potential energy gives the equation above. A plane wave over the entire real line is an idealised momentum eigenstate, not a normalisable localised particle; finite wavepackets combine many such waves.

The equation is **linear**: if $\psi_1$ and $\psi_2$ solve the same equation, a constant-coefficient combination solves it too. Its normalisation must still be checked. The Born rule and the measurement rules are additional physical ingredients, not deductions from linearity.

### Probability is conserved

For a real scalar potential, multiply the equation by $\psi^*$ and subtract its complex conjugate multiplied by $\psi$. The $V|\psi|^2$ terms cancel. Rearranging the derivative terms gives

$$\frac{\partial\rho}{\partial t}+\frac{\partial j}{\partial x}=0,
\qquad j=\frac{\hbar}{m}\operatorname{Im}\!\left(\psi^*\frac{\partial\psi}{\partial x}\right).$$

Here $j$ is **probability current**. Integration from $a$ to $b$ gives $dP(a<x<b)/dt=j(a)-j(b)$: probability inside changes by inflow minus outflow. For a closed well, or a normalisable state with vanishing flux at infinity, total probability remains one. It is the same local conservation structure as a fluid entering and leaving a region, without treating probability as a material liquid.

[MIT's operator and evolution lectures](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/pages/lecture-notes/) develop this formulation.

## 3. Stationary states — separate the clock from the shape

Suppose $V$ does not depend on time. Try $\psi(x,t)=\phi(x)T(t)$. Substitution and division where the factors are nonzero give

$$i\hbar\frac1T\frac{dT}{dt}
=-\frac{\hbar^2}{2m}\frac1\phi\frac{d^2\phi}{dx^2}+V(x).$$

The left side depends only on $t$ and the right only on $x$. To agree for every $x,t$, both equal a constant $E$. Therefore

$$\boxed{\hat H\phi=E\phi},\qquad T(t)=e^{-iEt/\hbar}.$$

The first equation is an **eigenvalue problem**: applying $\hat H$ leaves the shape unchanged and multiplies it by $E$. This is the function version of [[Eigenvalues and Eigenvectors]]. Boundary conditions decide which eigenvalues are allowed.

For one such state,

$$|\psi(x,t)|^2=|\phi(x)|^2|e^{-iEt/\hbar}|^2=|\phi(x)|^2.$$

Its density is stationary even though the wavefunction's phase turns. It has a definite energy; it need not have a definite position or momentum. “Stationary” does not mean a motionless classical particle. Nor does every quantum state have discrete energy: a free particle has a continuous energy spectrum.

## 4. Solve an infinite well — earn the energy ladder

Let $V=0$ for $0<x<L$, and impose impenetrable walls at $x=0,L$. In this idealisation $\phi(0)=\phi(L)=0$ and the wavefunction vanishes outside. Real confinement is finite; this is the simplest model whose boundary-value problem we can solve exactly.

**Step 1 — Tool: the constant-coefficient ODE. Trigger: constant potential inside the well.**

$$-\frac{\hbar^2}{2m}\phi''=E\phi
\quad\Rightarrow\quad\phi=A\sin kx+B\cos kx,\qquad k^2=\frac{2mE}{\hbar^2}.$$

**Step 2 — Tool: boundary conditions. Trigger: the two fixed walls.** At zero, $B=0$. At $L$, a nonzero solution needs $\sin(kL)=0$, so $kL=n\pi$.

**Step 3 — Tool: normalisation. Trigger: shape alone does not set total probability.** As in Example 1, $\int_0^L\sin^2(n\pi x/L)dx=L/2$. Hence

$$\boxed{\phi_n(x)=\sqrt{\frac2L}\sin\frac{n\pi x}{L},\qquad
E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}=\frac{n^2h^2}{8mL^2},\quad n=1,2,3,\ldots.}$$

Why no $n=0$? It gives the zero function, which cannot be normalised. Directly, the $E=0$ equation gives $\phi=Ax+B$; both boundary conditions force $A=B=0$. Negative $E$ gives exponentials and again no nonzero solution meeting both walls. Negative integers duplicate the positive-$n$ states up to a global sign.

The ground state has **zero-point energy** $E_1>0$. This is not energy borrowed from somewhere. A nonzero wavefunction forced to vanish at two walls must have curvature; the kinetic-energy operator detects that curvature. The energy zero was chosen as the potential inside the well.

The functions are orthonormal:

$$\int_0^L\phi_m^*\phi_n\,dx=\delta_{mn},$$

where $\delta_{mn}=1$ when $m=n$, and 0 otherwise. For $m\ne n$, the product-to-sum identity turns the integrand into cosines with integer numbers of half-waves; their integrals vanish. This is the same sine orthogonality used in [[Fourier Series]]. [A worked infinite-well treatment](https://farside.ph.utexas.edu/teaching/355/Surveyhtml/node180.html) provides another route through the calculation.

### Worked example 2 — an electron in a 1 nm well

Use $L=1.00\times10^{-9}\ \mathrm m$, $m_e=9.109\times10^{-31}\ \mathrm{kg}$.

**Tool: $E_n=n^2h^2/(8mL^2)$. Trigger: the stated infinite-well model.**

$$E_1=6.025\times10^{-20}\ \mathrm J=0.3760\ \mathrm{eV},\qquad E_2=4E_1=1.504\ \mathrm{eV}.$$

**Tool: photon energy equals the energy difference. Trigger: an allowed radiative transition from $n=2$ to $n=1$.**

$$\Delta E=3E_1=1.128\ \mathrm{eV},\qquad\lambda=\frac{hc}{\Delta E}=1.099\ \mathrm{\mu m}.$$

The photon is infrared. Do not use $E_2$ alone for its energy. A transition also requires a coupling to radiation; energy differences identify possible photon energies, not emission rates. The time-independent isolated well does not spontaneously change levels under its own Schrödinger evolution.

## 5. Superposition is not a lottery over pre-existing states

Expand a normalised state in the well's energy basis:

$$\psi(x,t)=\sum_{n=1}^{\infty}c_n\phi_n(x)e^{-iE_nt/\hbar},
\qquad\sum_n|c_n|^2=1.$$

Orthogonality makes the total probability the sum of the coefficient moduli squared. An ideal energy measurement returns $E_n$ with probability $|c_n|^2$; its average over many identical preparations is $\langle E\rangle=\sum_n|c_n|^2E_n$. The average need not itself be an allowed single outcome.

For an ideal projective energy measurement in this nondegenerate well, obtaining $E_n$ prepares $\phi_n$ (up to phase). Immediately repeating the energy measurement gives $E_n$ again. A position measurement instead changes the preparation differently. The deterministic evolution equation is not a promise of deterministic measurement results, and no conscious observer is required.

### Two preparations with the same energy statistics

**Coherent preparation:** every run starts in $(\phi_1+\phi_2)/\sqrt2$. Let $\omega_{21}=(E_2-E_1)/\hbar$. The real-valued well eigenfunctions give

$$\rho_{\rm coherent}(x,t)
=\frac12(\phi_1^2+\phi_2^2)+\phi_1\phi_2\cos(\omega_{21}t).$$

**Statistical mixture:** a random preparation produces $\phi_1$ in half the runs and $\phi_2$ in the rest, without retaining a coherent relative phase:

$$\rho_{\rm mixture}(x,t)=\frac12\phi_1^2+\frac12\phi_2^2.$$

The difference is the **interference cross term**. Coherent superposition adds amplitudes before squaring; the mixture averages probabilities from alternative preparations. Both give energy $E_1$ or $E_2$ with probability $1/2$, yet their position statistics differ. A general mixed state needs a density operator, not one wavefunction.

![[quantum-states-superposition-mixture.svg|730]]

*A relative phase of $\pi/2$ makes these particular position densities coincide at that instant. It does not turn the pure state into the mixture: their subsequent evolution differs.*

![[quantum-states-evolution.mp4]]

*Follow three changes: the phase of one eigenstate, the relative phase of two eigenstates, then the energy scale across different well widths. Curves show probability distributions across repeated preparations, never a tracked particle trajectory. The width sequence compares separate systems; it does not simulate suddenly moving a wall.*

### Worked example 3 — make the distinction measurable

Find the probability of detection in the left half for the coherent preparation above.

**Tool: integrate the expanded density. Trigger: the cross term is what differs from the mixture.** Each eigenstate gives half its probability to either half of the symmetric well. The cross integral is

$$\int_0^{L/2}\phi_1\phi_2\,dx
=\int_0^{1/2}2\sin(\pi u)\sin(2\pi u)\,du
=\left[\frac{\sin\pi u}{\pi}-\frac{\sin3\pi u}{3\pi}\right]_0^{1/2}
=\frac4{3\pi}.$$

Therefore

$$\boxed{P_{\rm left}(t)=\frac12+\frac4{3\pi}\cos(\omega_{21}t).}$$

It swings from $0.9244$ to $0.07559$, while the mixture stays at $0.5$. The period is $T=2\pi\hbar/(E_2-E_1)$. These are predictions for repeated preparations followed by a measurement at the chosen delay—not repeated undisturbing looks at one particle.

**Tool: weighted mean in the energy basis. Trigger: the energy outcomes are discrete.** Both preparations have $\langle E\rangle=(E_1+E_2)/2=2.5E_1$ throughout. The moving position density does not mean energy is being created or exchanged with the outside.

## 6. Where it works — a crystal's size changes its colour

Quantum dots are semiconductor crystals small enough for confinement to affect electronic energies. Dots of the same material can emit different colours when their sizes differ. Some displays use blue illumination and quantum dots to produce red and green light. [The Nobel committee's explanation](https://www.nobelprize.org/uploads/2024/08/Speakersmanuscript_All_Nobelprizes_2023_Nobelprizelessons.pdf) connects their size-dependent properties to real products.

The infinite-well result exposes the mechanism: reducing a confinement length increases the energy scale as $1/L^2$. A tighter spatial pattern requires larger wavenumbers, hence larger kinetic energies. That changes the energy available in an optical transition.

![[quantum-states-confinement.svg|740]]

*Same mass and ideal boundary model in both panels. Halving $L$ multiplies every energy and energy difference by four. This is a scaling comparison, not a calibrated colour chart for commercial quantum dots.*

Real dots are three-dimensional semiconductor systems with a band gap, electron and hole effective masses, finite barriers and interactions. Their emitted photon energy is **not** simply $E_2-E_1$ for a lone free electron in a 1D box. [[Energy Levels and Line Spectra]] distinguishes semiconductor bands from isolated atomic levels; the box model contributes the confinement intuition, not the whole device calculation.

There is a second useful surprise: in a finite region with constant $V>E$, the stationary equation produces exponential solutions rather than automatically forcing $\phi=0$. Matching a finite barrier to its surroundings can leave transmitted amplitude on the far side. That is the route to [[Quantum Tunnelling]], including flash-memory operation—not a violation of energy conservation.

## Hands-on — test the cross term

Run `quantum-states-model.py` to check normalisation, orthogonality, the differential equation and an independent finite-difference energy calculation. The following experiment uses only NumPy and compares the measured left-half fractions implied by the density:

```python
import numpy as np
x = np.linspace(0, 1, 20001)       # x/L
u = np.sqrt(2) * np.sin(np.pi*x)
v = np.sqrt(2) * np.sin(2*np.pi*x)
rng = np.random.default_rng(804)
for phase in [0, np.pi/2, np.pi]:
    density = np.abs((u + np.exp(-1j*phase)*v)/np.sqrt(2))**2
    cdf = np.cumsum(density)
    cdf /= cdf[-1]               # grid approximation to the integral
    detections = np.interp(rng.random(12000), cdf, x)
    print(round(phase, 3), np.mean(detections < 0.5))
```

Predict approximately $0.924$, $0.500$, $0.076$, with sampling fluctuations. Now replace the density by `(u**2 + v**2)/2`: all three results should be near $0.5$. The computer samples a model; it does not reproduce the physical apparatus or prove the Born rule.

## 7. Beyond — uncertainty as Fourier geometry

Recall that a position-dependent phase carries momentum information. With the symmetric Fourier convention,

$$\widetilde\psi(k)=\frac1{\sqrt{2\pi}}\int\psi(x)e^{-ikx}\,dx,\qquad p=\hbar k.$$

For a suitable normalised pure state, $\int|\widetilde\psi|^2dk=1$. The momentum density is $|\widetilde\psi(p/\hbar)|^2/\hbar$; the factor converts a density per wavenumber to a density per momentum.

For a Gaussian with position density of standard deviation $\sigma$,

$$\psi(x)=(2\pi\sigma^2)^{-1/4}e^{-x^2/(4\sigma^2)},$$

Fourier transformation gives a Gaussian momentum density with $\Delta p=\hbar/(2\sigma)$. Thus $\Delta x\Delta p=\hbar/2$. Narrowing one distribution widens the other.

Why is this a lower bound generally? For sufficiently smooth, decaying states with finite variances, shift the coordinate origin and remove the mean-momentum phase so $\langle x\rangle=\langle p\rangle=0$. Integration by parts gives $\operatorname{Re}\int x\psi^*\psi' dx=-1/2$. Cauchy–Schwarz then gives

$$\left(\int x^2|\psi|^2dx\right)\left(\int|\psi'|^2dx\right)
\geq\left|\int x\psi^*\psi'dx\right|^2\geq\frac14.$$

Since these factors are $(\Delta x)^2$ and $(\Delta p)^2/\hbar^2$, respectively,

$$\boxed{\Delta x\,\Delta p\geq\hbar/2.}$$

This concerns spreads in identically prepared measurement outcomes. It is not merely an instrument defect and does not permit borrowing energy for a short time. The Fourier mathematics in [[Fourier Transform]] is doing physical work.

## Common Misconceptions

- **“The wavefunction is a probability.”** It is a complex amplitude. Square its modulus, then integrate over an interval.
- **“A stationary state is a particle sitting still.”** The density is fixed; the state can have nonzero kinetic energy and a spread of momentum outcomes.
- **“A superposition means we do not know which eigenstate was prepared.”** That description fits the specified mixture. The coherent preparation retains relative phase and its cross term.
- **“Knowing $|\psi|^2$ tells us everything.”** It discards phase. Different momentum distributions can share one position density.
- **“Every energy is quantised.”** Boundary conditions select the spectrum. The free-particle spectrum is continuous; the well's bound spectrum is discrete.
- **“The box formula is the hydrogen formula.”** The potentials differ. Infinite-well energies scale as $n^2$; Coulomb bound-state energies scale as $-1/n^2$.
- **“Observation requires a mind.”** Measurement means a physical interaction producing an outcome; it does not require consciousness.

## Exam Notes

### Cambridge 9702 and 0625

**9702 §22** examines photons, the photoelectric effect, de Broglie wavelength and atomic energy levels/spectra. It does not prescribe solving Schrödinger's equation, normalising wavefunctions or distinguishing density operators from pure states. Use [[Wave-Particle Duality]] and [[Energy Levels and Line Spectra]] for those assessed outcomes; the present derivations are enrichment. **0625** has no wavefunction or Schrödinger-equation requirement.

### IB Physics, first assessment 2025

**E.1** includes atomic energy levels and spectra; **E.2 is HL-only** and includes the photoelectric effect, matter-wave diffraction and Compton scattering. The current guide does not require the normalised infinite well, the Schrödinger equation or the pure-state/mixture calculation above. Do not import a historical IB quantum-option requirement into this course.

### AP Physics

**AP Physics 2 Unit 15** contains related quantum/atomic physics, including bound-system energy levels. It does not specify this differential-equation treatment. **AP Physics 1, AP Physics C: Mechanics and AP Physics C: Electricity and Magnetism** do not examine quantum wavefunctions. Calculus-based mechanics is not synonymous with quantum mechanics.

### Scope and formula status

This is a university-level companion; no new school-syllabus outcome is claimed. The worked examples are original model problems, not past-paper questions. The Schrödinger equation, normalised well eigenfunctions and coherent/mixture formulas are not a memorisation requirement for the school physics courses listed above.

## Connections

- **Starting evidence:** [[Wave-Particle Duality]] — interference, photoelectric effect and matter waves.
- **Boundary conditions:** [[Stationary Waves]] — modes; [[Second-Order Differential Equations]] — oscillatory and exponential solutions.
- **Mathematical language:** [[Complex Numbers]], [[Integration]], [[Eigenvalues and Eigenvectors]], [[Fourier Series]], [[Fourier Transform]].
- **Probability:** [[Probability Basics]], [[Continuous Random Variables]] — outcomes, density and interval probability.
- **Applications:** [[Energy Levels and Line Spectra]] — atomic lines and semiconductor bands; [[Secondary Storage]] — flash-memory barriers.
- **Next mechanisms:** [[Quantum Tunnelling]], [[Pauli Exclusion Principle]].
- **Historical companion:** [[The Argument for i]] — complex numbers entering physical theory.
- **Further study:** [MIT 8.04 lectures 3–7](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/pages/lecture-notes/) — wavefunctions, operators and time evolution.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $\lvert\psi\rvert^2$ | `\lvert\psi\rvert^2` | probability density |
| $\psi^*$ | `\psi^*` | complex conjugate |
| $\hat H\phi=E\phi$ | `\hat H\phi=E\phi` | energy eigenvalue equation |
| $i\hbar\partial_t\psi$ | `i\hbar\partial_t\psi` | time-evolution term |
| $\langle E\rangle$ | `\langle E\rangle` | expected energy |
| $\delta_{mn}$ | `\delta_{mn}` | orthogonality indicator |
