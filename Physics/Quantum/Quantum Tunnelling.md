---
chinese: 量子隧穿 (liàngzǐ suìchuān)
aliases:
  - Quantum Tunneling
  - Barrier Penetration
prerequisites:
  - "[[Quantum States and the Schrödinger Equation]]"
  - "[[Second-Order Differential Equations]]"
  - "[[Energy Levels and Line Spectra]]"
  - "[[Nuclear Physics]]"
leads_to: []
tags:
  - subject/physics
  - domain/quantum
  - level/university
  - type/deep
  - type/derivation
  - notation/transmission-coefficient
  - misconception/tunnelling-borrows-energy
  - misconception/insulators-are-perfect
---

# Quantum Tunnelling 量子隧穿

> *The CPU designer wants electrons to stay behind the barrier. The SSD designer wants to let them through—then keep them there.*

## Definition

### Formal

**Quantum tunnelling** is transmission through a region where a particle's energy $E$ lies below the potential energy $V(x)$: a region that classical mechanics would forbid it to cross. For a finite barrier separating two classically allowed regions, the Schrödinger equation can give a nonzero transmitted probability current even when $E<V$ throughout the barrier.

We begin with one nonrelativistic particle, constant mass $m$, a real, time-independent potential and no absorption. These assumptions make both energy and total probability conserved. A semiconductor device requires additional ingredients; the simple barrier teaches the mechanism before we add them.

### Intuitive

A classical ball that cannot climb a hill turns back. A quantum particle is described by a wavefunction: the amplitude need not become zero as soon as it reaches a classically forbidden region. Inside a simple barrier it has exponential solutions. If another allowed region begins before the amplitude has become negligible, the full boundary-value problem can connect to a travelling wave on the far side.

The wall has no secret hole. The particle has not secretly acquired enough energy to climb over it. **The classical rule that forbids passage is no longer the rule governing the state.**

### 中文锚点

关掉电脑，明天再开机，昨天存的照片还在。固态硬盘能记住它们，靠的是把电子留在储存区里，并用一层绝缘材料把它同周围隔开。可电子既然能进去，为什么不会马上跑出来？关键在于，写入时和断电后，它面对的不是同一道势垒：写入电压改变了势垒的形状，让隧穿容易得多；撤掉电压后，电子逃出的机会又变得极小。绝缘层并不是一道永远过不去的墙，而是一道难易程度可以调节的关口。照片能在断电后留下来，正是因为我们能把这道关口调到很难通过——但“很难”终究不是“永远不可能”。

## Notation

| Symbol / term | Meaning | Keep separate |
|---|---|---|
| $V(x)$ | potential **energy**, in J or eV | not electrical voltage |
| $E$ | conserved energy of a stationary scattering state | not the barrier height |
| $a$ | barrier width | physical distance |
| $k=\sqrt{2mE}/\hbar$ | wavenumber outside a zero-potential barrier | oscillation scale |
| $\kappa=\sqrt{2m(V_0-E)}/\hbar$ | decay constant inside it | inverse length |
| $j$ | probability current | probability crossing per unit time in 1D |
| $r,t$ | reflection/transmission **amplitudes** | generally complex |
| $R,T$ | reflection/transmission **probabilities** | real numbers between 0 and 1 |

For an electron, $1\ \mathrm{eV}=1.602\times10^{-19}\ \mathrm J$ and $m_e=9.109\times10^{-31}\ \mathrm{kg}$. Here $\hbar=h/(2\pi)$.

## 1. Why a forbidden region does not force zero amplitude

Recall the stationary equation from [[Quantum States and the Schrödinger Equation]]:

$$-\frac{\hbar^2}{2m}\phi''+V\phi=E\phi,
\qquad \psi(x,t)=\phi(x)e^{-iEt/\hbar}.$$

**Tool: rearrange a constant-coefficient differential equation. Trigger: $V$ is constant within each region.**

Outside a barrier where $V=0$ and $E>0$,

$$\phi''=-k^2\phi\quad\Rightarrow\quad \phi=Ae^{ikx}+Be^{-ikx}.$$

These are right- and left-travelling components with our $e^{-iEt/\hbar}$ time convention. Inside a barrier with $V_0>E$,

$$\phi''=\kappa^2\phi\quad\Rightarrow\quad\boxed{\phi=Ce^{\kappa x}+De^{-\kappa x}.}$$

It is the same ODE machinery as [[Second-Order Differential Equations]], with the sign changed. Exponential does **not** mean zero. Nor is this an oscillation with an imaginary physical velocity: the classical expression $mv^2/2=E-V$ does not define a trajectory inside the forbidden region.

For a barrier extending to $+\infty$, discard the growing exponential to keep the solution bounded. For a **finite** barrier, keep both terms: each is finite there, and both boundaries matter. Discarding the growing term prematurely prevents the correct transmitted-current solution.

A decaying tail alone is not proof of transmission. A particle incident below an infinitely long step has a penetration tail but **zero transmitted current**. Tunnelling through a finite barrier requires the far-side connection.

## 2. Match the two boundaries

Take the rectangular barrier

$$V(x)=\begin{cases}0,&x<0,\\V_0,&0\le x\le a,\\0,&x>a,\end{cases}
\qquad 0<E<V_0.$$

Send a wave from the left and none from the right. Set the incident amplitude to 1:

$$\phi(x)=\begin{cases}
e^{ikx}+r e^{-ikx},&x<0,\\
Ce^{\kappa x}+De^{-\kappa x},&0\le x\le a,\\
t e^{ikx},&x>a.
\end{cases}$$

These stationary plane waves describe a steady scattering experiment; they are not a normalisable single-particle packet on the whole line. Ratios of their currents give the scattering probabilities. A normalisable packet comes in §4.

**Tool: continuity of $\phi$ and $\phi'$. Trigger: finite potential jumps, constant mass, no delta-function potential.** Integrating the Schrödinger equation over a vanishingly short interval across a boundary shows that $\phi'$ has no jump. A discontinuity of $\phi$ would introduce singular derivatives not balanced by this finite potential.

Thus

$$\begin{aligned}
1+r&=C+D, & ik(1-r)&=\kappa(C-D),\\
Ce^{\kappa a}+De^{-\kappa a}&=te^{ika}, &
\kappa(Ce^{\kappa a}-De^{-\kappa a})&=ik te^{ika}.
\end{aligned}$$

Four equations fix four amplitudes. To see the algebra without hiding it in a matrix, write the interior solution backwards from its known right-edge value and slope:

$$\phi(x)=te^{ika}\left[\cosh\kappa(a-x)-i\frac{k}{\kappa}\sinh\kappa(a-x)\right].$$

At $x=0$, set $c=\cosh\kappa a$, $s=\sinh\kappa a$. Matching gives

$$1+r=te^{ika}(c-i(k/\kappa)s),\qquad
1-r=te^{ika}(c+i(\kappa/k)s).$$

Add them, then divide:

$$\boxed{t=\frac{e^{-ika}}{\cosh\kappa a+i\dfrac{\kappa^2-k^2}{2k\kappa}\sinh\kappa a}.}$$

Hyperbolic functions are just the two exponentials repackaged: $\cosh u=(e^u+e^{-u})/2$ and $\sinh u=(e^u-e^{-u})/2$.

![[quantum-tunnelling-barrier.svg|740]]

*Top: energy landscape. Bottom: the exact matched wavefunction for $E=2$, $V_0=3$, $a=1$, in units $\hbar=m=1$. Its real part is a snapshot at $t=0$; the modulus is an envelope. The left-hand oscillations include incident–reflected interference. Neither curve is a particle's path, and their vertical scale is not energy.*

## 3. Count what crosses: probability current

A large amplitude is not automatically a large flow. The appropriate conserved quantity is the **probability current**:

$$j=\frac{\hbar}{m}\operatorname{Im}\left(\psi^*\frac{\partial\psi}{\partial x}\right).$$

Subtract the Schrödinger equation multiplied by $\psi^*$ from its complex conjugate multiplied by $\psi$. Rearranging gives

$$\frac{\partial |\psi|^2}{\partial t}+\frac{\partial j}{\partial x}=0.$$

This is a continuity equation: probability can flow into or out of an interval, but the real potential does not create or destroy it. In a stationary state the density is time-independent, so $j$ is constant across the barrier.

For $Ae^{ikx}$, $j=(\hbar k/m)|A|^2$. The reflected component has the opposite sign. Therefore, with equal potential and mass on the two sides,

$$R=|r|^2,\qquad T=|t|^2,\qquad\boxed{R+T=1.}$$

If the two allowed regions have different wavenumbers, use $T=(k_{\rm right}/k_{\rm left})|t|^2$ for equal mass. It is a **flux ratio**, not always just an amplitude ratio squared.

**Tool: square the modulus of the matched amplitude. Trigger: transmission is a probability.** Since $\cosh^2u=1+\sinh^2u$ and $k^2+\kappa^2=2mV_0/\hbar^2$,

$$\boxed{T=\left[1+\frac{V_0^2\sinh^2(\kappa a)}{4E(V_0-E)}\right]^{-1}.}$$

The transmitted particles have the **same energy $E$** as the incident particles. A smaller transmitted amplitude means fewer transmissions, not a lower energy per transmitted particle. If the exterior potentials differ, the kinetic energies differ accordingly while total energy remains conserved. [MIT's tunnelling lecture](https://ocw.mit.edu/courses/6-007-electromagnetic-energy-from-motors-to-lasers-spring-2011/d9bc5d7be258ba20ccc652941d8f3e39_MIT6_007S11_lec42.pdf) develops the barrier and current viewpoint.

### Why thickness is such a powerful dial

For an opaque barrier, $\kappa a\gg1$, use $\sinh\kappa a\approx e^{\kappa a}/2$:

$$\boxed{T\approx \frac{16E(V_0-E)}{V_0^2}e^{-2\kappa a}.}$$

The exponential carries the dominant sensitivity. Its factor of **two** comes from squaring an amplitude. The prefactor matters for numerical estimates; $T=e^{-2\kappa a}$ is not the exact rectangular-barrier answer.

At fixed $E,V_0$, increasing width suppresses transmission. Increasing the mass also increases $\kappa$ and suppresses it. Raising the barrier at fixed incident energy has the same qualitative effect. This is why electron tunnelling can matter over atomic distances while your body does not walk through a door: the relevant mass and distance scales are vastly different, with many-body coherence adding further obstacles.

![[quantum-tunnelling-sensitivity.svg|740]]

### Worked example 1 — half a nanometre changes the odds

An electron of energy $1.00\ \mathrm{eV}$ meets a rectangular barrier of height $2.00\ \mathrm{eV}$. Compare widths $0.50\ \mathrm{nm}$ and $1.00\ \mathrm{nm}$.

**Tool: $\kappa=\sqrt{2m(V_0-E)}/\hbar$. Trigger: the missing classical energy is $V_0-E$, not $V_0$.** Convert the difference to joules:

$$\kappa=\frac{\sqrt{2(9.109\times10^{-31})(1.602\times10^{-19})}}{1.055\times10^{-34}}
\approx5.12\times10^9\ \mathrm{m^{-1}}=5.12\ \mathrm{nm^{-1}}.$$

**Tool: exact transmission formula. Trigger: a finite rectangular barrier with equal exterior potentials.** Here $V_0=2E$, so $T=1/(1+\sinh^2\kappa a)=\operatorname{sech}^2(\kappa a)$:

- $a=0.50\ \mathrm{nm}$: $\kappa a\approx2.56$, giving $T\approx0.0235$—about 2.35%.
- $a=1.00\ \mathrm{nm}$: $\kappa a\approx5.12$, giving $T\approx0.000142$—about 0.0142%.

Doubling this tiny width reduces transmission by roughly **166 times**. These are ideal free-electron model values, not a specification for a particular chip's oxide.

## 4. Watch one preparation meet the barrier

A localised packet is a superposition of travelling waves with different wavenumbers and hence different energies. Evolve it with the time-dependent Schrödinger equation: part of its probability distribution returns left and part emerges right.

![[quantum-tunnelling-explained.mp4]]

*First: a numerically evolved Gaussian packet, $\hbar=m=1$, mean momentum 2, position spread 6, encountering a height-3, width-1 barrier. Almost all its initial energy distribution lies below the barrier. The coloured readouts report probabilities to the left, inside and to the right, which sum to one; only after separation do the outer probabilities become reflection/transmission. Second: compare barriers of different widths at fixed incident energy. Third: an idealised energy-barrier sketch distinguishes writing from retention. The latter two sequences compare conditions, not the time evolution of the first packet.*

An eventual position detection finds the **whole particle** on one side, not a fraction of an electron on each. Repeating the same preparation establishes the predicted frequencies. The packet also changes shape: different energy components have different transmission amplitudes and phases. Its total transmission is an average over its incident energy distribution, not necessarily $T$ at its mean energy.

The animation is a solution of a simplified model, not experimental footage or a semiconductor-device simulation. It supplies no stopwatch measurement of an electron's route inside the barrier. Claims that tunnelling allows faster-than-light messages do not follow from these curves.

## 5. CPU leakage — when insulation becomes too thin

In a field-effect transistor, the **gate** controls conduction along a channel between source and drain. The gate's electric field must influence that channel through an insulating layer; electrons should not appreciably cross that insulation during ordinary switching.

Thinning the gate dielectric historically improved electrostatic control. But sufficiently thin barriers permit appreciable **direct tunnelling** between channel and gate. Unwanted gate current consumes power and contributes to heating. It is one scaling problem, not a complete explanation of CPU power or every off-state leakage current.

The engineering escape is a **high-permittivity (“high-k”) dielectric**. The elementary capacitance relation exposes the trade:

$$C\approx\frac{\epsilon A}{d}.$$

Increasing $\epsilon$ permits a larger physical thickness $d$ while retaining strong capacitive coupling. A physically thicker barrier can suppress tunnelling without sacrificing the same amount of gate control. Real stacks also depend on band offsets and interfaces; permittivity alone does not predict leakage. Intel's adoption of hafnium-based dielectrics illustrates this strategy. [Intel: high-k, tunnelling and gate leakage](https://www.intel.com/pressroom/kits/advancedtech/doodle/ref_HiK-MG/high-k.htm)

Keep three things distinct:

- **Gate leakage:** unwanted transport through the gate dielectric; tunnelling is important here.
- **Subthreshold channel current:** source–drain current when the transistor is nominally off; thermal carrier statistics and electrostatic control matter, so “all leakage is tunnelling” is false.
- **Very short channel limits:** direct source–drain tunnelling can also matter when the channel barrier becomes sufficiently short. It is a different route from gate leakage.

[MIT’s subthreshold lecture](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/resources/mit6_012f09_lec12/) explains the thermal-current regime; [Luisier and Schenk’s transistor simulations](https://iis-people.ee.ethz.ch/~schenk/jctn.pdf) distinguish source–drain tunnelling from gate leakage.

A process label such as “3 nm” is not a measurement of every transistor dimension or of its oxide thickness. The physical barrier and its energy profile are what enter the tunnelling calculation.

## 6. SSD flash — write through a barrier, then remember

An SSD's NAND flash stores information as charge that shifts a transistor's threshold voltage. The controller, error-correcting codes and file system build a reliable drive around those cells; the charge-storage mechanism itself is quantum engineering.

### Where the charge stays

A **floating gate** is a conducting island insulated from surrounding electrodes. A **charge-trap** cell instead stores charge in localised traps in an insulating storage layer, commonly silicon nitride. Many modern 3D NAND devices use charge trapping. The two structures share the useful idea—stored charge changes transistor behaviour—but they are not the same material arrangement. [Micron's charge-trap architecture](https://www.micron.com/products/storage/nand-flash/176-layer-nand)

### Write, retain, read, erase

**Write/program.** A strong applied field changes the electron's potential-energy landscape across the tunnel dielectric. Electrons can enter the storage region by field-assisted tunnelling. In a triangular-barrier regime this is called **Fowler–Nordheim tunnelling**; a thinner, trapezoidal barrier can instead support direct tunnelling. Geometry, field and materials determine the regime.

**Retain.** Remove the large programming voltage and the barrier changes again. Escape becomes much less likely. The charge persists without a continuous supply of power, but the insulation is not mathematically perfect and retention is not infinite.

**Read.** Use smaller sensing voltages and test channel conduction. Stored negative charge typically raises the gate voltage needed to turn on an n-channel cell. The drive therefore reads **threshold-voltage ranges**, not individual electrons spilling out into a counter. [KIOXIA's storage and readout explanation](https://www.kioxia.com/en-jp/rd/technology/nand-flash.html)

**Erase.** Apply a different bias to reset the stored charge, at block granularity in NAND. Depending on the cell architecture, this can involve electron removal and/or injection of holes that neutralise stored negative charge. It is not universally the same electron taking its exact writing route backwards. [Experiments on charge-trap and floating-gate arrays](https://re.public.polimi.it/bitstream/11311/1279424/1/mmc24.pdf) illustrate how architecture and carrier supply affect erase.

![[quantum-tunnelling-flash.svg|740]]

*Energy sketches, not cross-sections of a complete device. The programming field tilts a barrier and reduces its forbidden width at the illustrated electron energy. Removing that field restores a wider forbidden region. The small dot marks a representative occupied state in the storage region, not a classical trajectory or a promise of permanent confinement.*

This answers the apparent paradox: **the electron tunnels in under one barrier profile and is retained under another.** No one-way quantum law is needed. The voltage source changes the conditions and exchanges energy during programming; the conserved-energy scattering model applies to a fixed potential, not to an entire write pulse.

### More than one bit per cell

Two distinguishable threshold ranges encode one bit. Four, eight and sixteen ranges encode two, three and four bits respectively—MLC, TLC and QLC in common NAND terminology. More ranges squeeze the margins between decisions, so charge drift and noise become harder to tolerate. [KIOXIA: multi-level cells](https://www.kioxia.com/en-jp/rd/technology/multi-level-cell.html)

Program/erase stress creates defects in the dielectrics and interfaces. Those defects can alter thresholds and leakage paths; intentional storage traps are not the same thing as unwanted damage in the tunnel dielectric. Wear levelling spreads writes, while [[Error Detection and Correction]] helps recover data from imperfect readings. Retention depends on temperature, wear and device design, not one universal number of years. [KIOXIA's reliability handbook, §2-1-7](https://www.kioxia.com/content/dam/kioxia/en-jp/about/asset/reliability-handbook-e.pdf)

## 7. A microscope made from the same sensitivity

In a **scanning tunnelling microscope (STM)**, a sharp conducting tip approaches a conducting or semiconducting surface without normally touching it. A small bias produces tunnelling current across the gap. At approximately fixed electronic conditions,

$$I\propto e^{-2\kappa s},$$

where $s$ is tip–sample separation. A feedback loop moves the tip vertically to keep current constant as it scans. The required motion provides atomic-scale contrast. The signal also depends on available electronic states and bias, so an STM image is not simply a mechanical height map. [NIST's STM introduction](https://www.nist.gov/pml/scanning-tunneling-microscope/scanning-tunneling-microscope-introduction)

### Worked example 2 — an atomic-sized motion

Approximate the effective vacuum barrier by $V-E=4.0\ \mathrm{eV}$. How does current change if the gap increases by $0.10\ \mathrm{nm}$?

**Tool: $\kappa\propto\sqrt{V-E}$. Trigger: the same electron mass as Example 1, four times the energy difference.** Thus $\kappa\approx10.25\ \mathrm{nm^{-1}}$.

**Tool: divide two exponential current laws. Trigger: only the gap changes; hold bias, electronic states and prefactor fixed.**

$$\frac{I(s+\Delta s)}{I(s)}=e^{-2\kappa\Delta s}
=e^{-2(10.25)(0.10)}\approx0.129.$$

An extra tenth of a nanometre cuts the current to roughly **one eighth**. The sensitivity that makes tiny barriers troublesome in a CPU becomes the measuring tool in a microscope.

## Hands-on — make the width do the work

This runnable Python block uses SI constants and the exact sub-barrier formula. It needs only the standard library.

```python
from math import sqrt, sinh
hbar, m, eV = 1.054571817e-34, 9.1093837e-31, 1.602176634e-19
E, V0 = 1.0*eV, 2.0*eV
kappa = sqrt(2*m*(V0-E))/hbar
for width_nm in [0.25, 0.50, 0.75, 1.00]:
    a = width_nm*1e-9
    T = 1/(1 + V0**2*sinh(kappa*a)**2/(4*E*(V0-E)))
    print(f"{width_nm:.2f} nm: T={T:.6f}, R={1-T:.6f}")
```

Before running it, predict whether doubling the width halves $T$. Then change the mass while keeping $E$ and $V_0$ fixed. Explain the result through $\kappa$, not through “heavy things are slower”: the energy is fixed, and the wave equation is the tool.

`quantum-tunnelling-model.py` independently solves the four boundary equations, checks current conservation, and tests the packet evolution against the energy-averaged stationary prediction on successively finer grids.

## Beyond — curved barriers, nuclei and resonances

Recall that the rectangular result is dominated by the exponent $-2\kappa a$. For a smooth, sufficiently opaque barrier between turning points $x_1,x_2$, the semiclassical **WKB** approximation generalises it to

$$T\sim\exp\left[-2\int_{x_1}^{x_2}\frac{\sqrt{2m(V(x)-E)}}{\hbar}\,dx\right].$$

The symbol $\sim$ here signals the dominant exponential; connection factors also matter. WKB needs a potential varying slowly on the local wave scale away from turning points, with special matching near them. It is not a universal substitute for solving arbitrary sharp or resonant barriers.

- **Alpha decay:** a quasi-bound nuclear state can couple through an exterior Coulomb barrier to an outgoing alpha particle. The barrier exponent helps explain huge lifetime differences for modest alpha-energy changes; nuclear structure and alpha preformation also affect the rate. This extends [[Nuclear Physics]].
- **Fusion in stars:** tunnelling allows charged nuclei to react at collision energies below the classical Coulomb barrier. The thermal distribution supplies incident energies; the reaction rate combines that distribution, penetration probability and nuclear reaction physics. It is neither “every proton tunnels” nor energy borrowed to switch the Sun on. See [[Stellar Evolution]] and [MIT’s “Why Stars Shine” problem](https://ocw.mit.edu/courses/8-044-statistical-physics-i-spring-2013/e4738e6ad4244bd9b5ac0440238658b6_MIT8_044S13_ps8.pdf), which explicitly tests the classical high-energy tail.
- **Above-barrier reflection:** for $E>V_0$, the interior oscillates, but boundary matching can still reflect waves. In the rectangular result, replace the hyperbolic factor by $\sin^2(qa)/(E-V_0)$, with $q=\sqrt{2m(E-V_0)}/\hbar$. At $qa=n\pi$ ($n\ge1$), $T=1$.
- **Double-barrier resonance:** a well between two barriers can support resonant transmission. Interference can make an ideal symmetric pair highly transmitting at particular energies even when either barrier alone is opaque. “Always multiply the two independent probabilities” misses the coherent multiple reflections. [MIT’s transport notes](https://web.mit.edu/6.732/www/new_part1b.pdf) develop resonant barriers.

At exactly $E=V_0$, solve $\phi''=0$ inside or take the limit carefully: $T=[1+mV_0a^2/(2\hbar^2)]^{-1}$. Reaching the barrier height does not instantly guarantee transmission.

### A better model changes what is possible

In the classical model, sub-barrier transmission is forbidden; the quantum model predicts a nonzero value. This differs from the mathematical point in [[Probability Basics]] that a particular exact outcome can have probability zero in a continuous distribution. One comparison changes the physical model; the other concerns how probability works *within* a model.

## Common Misconceptions

- **“The particle borrows energy briefly.”** No: scattering from a static barrier conserves energy. The uncertainty principle grants no permission to violate it.
- **“The electron finds a tiny crack.”** The calculation assumes the barrier occupies the whole interval. It is the wavefunction that spans it.
- **“A tail means some particles get through.”** A semi-infinite step can have a tail with no transmitted current. Check the far-side region and the flux.
- **“Half the wave means half an electron.”** The wavefunction predicts outcomes; each detection transfers a whole electron's charge.
- **“The transmitted electron is exhausted.”** Lower transmission probability is not lost energy per particle.
- **“Flash remembers because tunnelling is one-way.”** Writing and retention use different potential profiles. The bias is the control knob.
- **“Every SSD uses floating gates.”** Charge-trap storage is a different implementation of the same threshold-shift principle.

## Exam Notes

### Cambridge Physics — 9702 and 0625

9702 Topics 22–23 examine quantum evidence, atomic energies and nuclear processes, but do not prescribe barrier matching, tunnelling coefficients or WKB. The 0625 nuclear topic does not require a tunnelling mechanism. These derivations are enrichment, not additional memorisation requirements for those courses.

### IB Physics — first assessment 2025

The current E.2 HL quantum section specifies the photoelectric effect, matter-wave diffraction and Compton scattering; E.3 covers radioactive decay. It does not prescribe the tunnelling calculation above. Do not import the old IB quantum-option scope into the current guide.

### AP Physics

AP Physics 2 Unit 15 examines related quantum, atomic and nuclear ideas, but does not prescribe this barrier-transmission treatment. AP Physics 1 and both AP Physics C courses do not examine quantum tunnelling. The transmission formulas and device physics are university enrichment.

### Computer Science connection

Cambridge **0478 §3.3** explicitly names control gates and floating gates in its solid-state storage guidance; **9618 §3.1** requires principal operations of solid-state flash memory. **IB CS 2027 A1.1.7** asks for secondary-storage devices and suitable uses. Those requirements are taught in [[Secondary Storage]]; the Schrödinger derivation is not required by them. AP CSA does not examine flash hardware.

**Formula status:** none of the barrier formulas above is a prescribed school formula to memorise for the named courses. Both worked examples are original model problems, not past-paper questions.

## Connections

- **Foundation:** [[Quantum States and the Schrödinger Equation]] — amplitude, density and conserved probability.
- **Mathematics:** [[Second-Order Differential Equations]] — oscillations and exponentials; [[Hyperbolic Functions]] — their compact notation.
- **Energy:** [[Energy Levels and Line Spectra]] — energy scales; [[Electric Potential]] — how applied voltage changes electron potential energy; [[Capacitors]] — dielectric coupling.
- **Working devices:** [[Secondary Storage]] — flash cells and controllers; [[Error Detection and Correction]] — recovering information from imperfect hardware; [[The Modern CPU vs the Textbook Model]] — physical limits beyond the logical model.
- **Nuclei and stars:** [[Nuclear Physics]], [[Stellar Evolution]] — escape and fusion through Coulomb barriers.
- **Microscopy:** [NIST: manipulating atoms with an STM](https://www.nist.gov/programs-projects/atom-manipulation-scanning-tunneling-microscope) — the same distance-sensitive interaction used as a tool.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $\kappa$ | `\kappa` | forbidden-region decay constant |
| $\sinh(\kappa a)$ | `\sinh(\kappa a)` | hyperbolic sine |
| $\operatorname{Im}(\phi^*\phi')$ | `\operatorname{Im}(\phi^*\phi')` | current's phase-sensitive factor |
| $\lvert t\rvert^2$ | `\lvert t\rvert^2` | transmission for equal exterior velocities |
| $e^{-2\kappa a}$ | `e^{-2\kappa a}` | dominant opaque-barrier suppression |
