# The Vault — Physics Directory

> **82 cards across 12 bays.** Last landed: [[Quantum Tunnelling]] — one barrier, opposite engineering goals: suppress CPU leakage, program SSD memory.
> One line per card: what it teaches and, where settled, which syllabus rows it closes. Open the card for the derivations, the worked papers, and the graph of what to read first.

**Reading the bays.** Bays follow the Cambridge 9702 chapter structure. *Closed* bays cover their stretch end to end; *open* bays are still growing, and the italic line under each names what comes next (a link that leads nowhere yet is a card still to be written). 💎 marks enrichment beyond every syllabus. Board codes: 0625 = Cambridge IGCSE, 9702 = Cambridge A Level, 9709/9231 = the Cambridge maths boards whose mechanics papers these cards also serve, IB = IB Physics, AP-1 / AP-2 / AP-C = the AP Physics courses.

See also: [[Mathematics/Directory|Mathematics]] · [[CS/Directory|Computer Science]] · [[Stories/Directory|Stories]] · [[Meta/Directory|Meta]].

---

## Mechanics (23)

*Newton's laws through collisions, statics, energy, rotation, and the Further-Mechanics extensions the maths boards examine.*

### Deep cards (19)

1. **[[Newton's Laws of Motion]]** — N1 as inertia (Aristotle vs Galileo), N2 as the operational definition of force, N3 on *different* bodies; free-body diagrams; the four canonical 9709 P4 problems.
2. **[[Linear Momentum]]** — $\mathbf{p} = m\mathbf{v}$ as the bookkeeping of motion; conservation derived from N3 + N2; elastic vs inelastic collisions; impulse as area under the $F$–$t$ graph.
3. **[[Forces and Equilibrium]]** — $\sum \mathbf{F} = \mathbf{0}$ *and* $\sum \boldsymbol{\tau} = \mathbf{0}$, both required; moments, couples, Lami's theorem, toppling; ladder and beam problems.
4. **[[SUVAT]]** — the five constant-acceleration formulae derived by calculus; the which-formula decision; $v$–$t$ graphs; vertical motion under gravity.
5. **[[Work, Energy and Power]]** — $W = Fs\cos\theta$, KE from integrating N2, the work–energy theorem, $P = Fv$, efficiency; when to use energy and when $F = ma$.
6. **[[Hooke's Law for Springs]]** — $F = -kx$ near any stable equilibrium; series and parallel springs; elastic PE $\tfrac12 kx^2$ as a work integral.
7. **[[Simple Harmonic Motion]]** — the universal small-oscillation equation $a = -\omega^2 x$; period $2\pi/\omega$; the pendulum and the mass-on-spring; energy in SHM.
8. **[[Stress, Strain and Young Modulus]]** — $\sigma = E\varepsilon$; $k = EA/L_0$ splits a spring's stiffness into a material part and a geometric part.
9. **[[The Friction Limit]]** — static $F \le \mu_s R$ vs kinetic $F = \mu_k R$; limiting equilibrium; $\mu = \tan\theta$ at the angle of repose.
10. **[[Braking Systems]]** — pedal → hydraulics → pad → wheel → tyre: brake fade, ABS as a slip-ratio controller, brake bias and weight transfer, regenerative braking. 💎
11. **[[Torque]]** — $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$ as rotational force; the moment arm; "moment" = "torque" = 力矩; couples as free vectors.
12. **[[Moment of Inertia]]** — $I = \sum m r^2$ as rotational mass, the $r^2$ forced by $\tau = I\alpha$; the standard-results table; parallel- and perpendicular-axis theorems.
13. **[[Angular Momentum]]** — $\mathbf{L} = \mathbf{r}\times\mathbf{p} = I\boldsymbol{\omega}$; $\boldsymbol{\tau} = d\mathbf{L}/dt$; conservation when external torque is zero (skater, diver, pulsar); precession.
14. **[[Projectile Motion]]** — one flight as two independent 1-D problems bridged by time; range and height with their small print; the trajectory as a quadratic in $\tan\theta$. *9231 §3.1*
15. **[[Centre of Mass]]** — the point that makes the particle model honest: internal forces cancel in pairs, so any system's centre of mass moves like one particle; composite bodies. *9231 §3.2*
16. **[[Centres of Mass by Integration]]** — the six standard results derived by slicing so each slice's own centre is known: triangle, arc, sector, cone, hemisphere, shell.
17. **[[Newton's Law of Restitution]]** — $e$ = separation ÷ approach as the second equation every collision needs; the $(1-e^2)$ energy loss; the drop test. *9231 §3.6*
18. **[[Elastic Strings and Springs]]** — $T = \lambda x/L$ with the modulus explained by the cut-in-half experiment; EPE $\lambda x^2/2L$; the slack discipline; the bungee jump. *9231 §3.4*
19. **[[Linear Motion under a Variable Force]]** — written upside down: five real Paper 3 questions solved first, then the method they share — when $F$ depends on $v$ or $x$, SUVAT dies and $ma = F$ becomes a differential equation: the three faces of $a$, terminal speed before integrating, the tanh fall, drag plus friction, an inverse-square resistance by energy; the coast-down test, the F1 lift-off, the takeoff roll and the rocket equation as where it lives. *9231 §3.5 · IAL M3.1, M3.3 · AP-C §2.9*

### Vocab cards (4)

1. **[[Force (Vocab)]]** — the cast of named forces (weight, normal, friction, tension, thrust, drag); the newton; exam phrasing for resultant and resolving.
2. **[[Tension (Vocab)]]** — "light inextensible string" decoded into two equations: $T$ uniform along the rope, equal accelerations for connected bodies; tension only pulls.
3. **[[Normal Force (Vocab)]]** — the perpendicular contact force as a constraint, not a formula: $N$ is whatever it takes, $N \ge 0$; the "reaction" terminology trap.
4. **[[Friction (Vocab)]]** — an inequality, not an equation; "limiting equilibrium"; direction opposes *relative* motion, which is how friction can propel.

## Circular Motion & Gravitation (2 — open)

1. **[[Circular Motion]]** — $a = v^2/r$ derived twice; centripetal force as a role, not a new force; conical pendulum, banked bends, loop-the-loop, vertical circles. *9702 Topic 12 · 9231 §3.3*
2. **[[Gravitational Fields]]** — Newton's law from Kepler + centripetal, $g = GM/r^2$, orbits and the geostationary case, the potential well, escape and orbital energy. *9702 Topic 13 · IB D.1 · AP-1 §2.6, §6.6 · AP-C §2.6*

*The 9231 §3.5 row rode the Mechanics bay ([[Linear Motion under a Variable Force]], 2026-09-02) — Further Mechanics is 6/6. The field-theoretic sibling [[Electric Field]] lives in Fields.*

## Oscillations (3 — open)

1. **[[Damped Oscillations]]** — SHM with the friction switched back on: light, critical and heavy damping as the three-case dial of a second-order ODE, with the decay envelope.
2. **[[Resonance]]** — the driven oscillator: steady state at the driver's frequency, maximum amplitude at the natural one; the quarter-cycle lag, peak height $Q\,F_0/k$, width $f_0/Q$, build-up in $Q/\pi$ cycles; six real questions from two boards.

3. **[[Coupled Oscillators]]** — two frequencies from symmetry; exact energy exchange, normal modes as eigenvectors, the chain-to-wave bridge and tuned mass dampers. 💎

## Fluids (1 — open)

*Statics first, then flow: density and pressure through Archimedes, continuity and Bernoulli; the bridge from Mechanics to Thermal's gas laws.*

1. **[[Density and Pressure]]** — ρ = m/V and p = F/A, the hydrostatic derivation from a column of slabs, upthrust as a pressure difference (Archimedes without magic), floating as the density balance, manometer and barometer, continuity and Bernoulli; seven real questions from 9702, 0625 and AP Physics 1. *9702 §4.3 · 0625 §1.4, §1.8 · AP-1 Unit 8*

*Related drag teaching: [[Linear Motion under a Variable Force]] and [[Density and Pressure]]; their coverage and repair work are tracked in the Hunter’s Notebook. Surface tension remains an enrichment candidate.*

## Waves (10 — open)

*The pattern travels, the medium stays: progressive waves first, then what happens when they meet each other and things.*

1. **[[Progressive Waves]]** — a wave as coupled SHM handed down a line; displacement, amplitude, wavelength, period, frequency, phase and the two graphs that carry them; v = fλ derived from the definitions; transverse vs longitudinal with the longitudinal graph decoded; I = P/A and I ∝ A²; the CRO; the ripple tank's reflection, refraction and diffraction. *9702 §7.1–7.2 · 0625 §3.1 · IB C.2 · AP-2 §14.1–14.2*

2. **[[Stationary Waves]]** — the superposition principle; two waves in opposite directions become 2A sin kx cos ωt, checked numerically and by a clamped simulated string; nodes, antinodes, phase within and across loops; strings (f_n = nv/2L, Melde), pipes (odd harmonics when closed, the resonance tube), microwaves; seven real questions. *9702 §8.1 · IB C.4.1–C.4.2 (C.4 complete) · AP-2 §14.6 half*

3. **[[Superposition and Interference]]** — path difference to phase difference, the hyperbolae of maxima in a summed ripple tank, coherence as constant phase difference (shown by time-averaging two independent lamps), Young's λ = ax/D derived and checked to the 67th fringe, the four syllabus demonstrations, beats, thin films and the anti-reflection coating; eight real questions across 9702, IB and AP.

4. **[[Diffraction]]** — diffraction as spreading past an edge, Huygens' reason, the gap-to-wavelength rule from a 2-D wave simulation; single-slit minima at a sin θ = mλ read out of summed wavelets; Young's fringes inside the single-slit envelope with the missing order; the grating's d sin θ = nλ with sharpness ∝ 1/N and brightness ∝ N² measured, n_max and 2n_max + 1; seven real questions across 9702, IB and the Paper 1 shapes.

5. **[[Doppler Effect]]** — moving sources change spacing, moving observers change encounters; sound formulas derived, light shifts separated from cosmological expansion, radar/ultrasound round trips and stellar wobble. *9702 §7.3 · IB C.5 · AP-2 §14.5; astronomy redshift contribution*

6. **[[Electromagnetic Spectrum]]** — the logarithmic family from radio to gamma, visible-band zoom, common vacuum speed, photons versus intensity, applications through absorption/detection, and analogue/digital signal regeneration. *9702 §7.4 · 0625 §3.3 · AP-2 §14.4; IB C.2 support*

7. **[[Polarisation]]** — field projection becomes Malus’s law; serial filters and the three-filter surprise, sunglasses/LCDs/photoelasticity, circular light, Brewster’s angle and projection matrices; three real Cambridge questions. *9702 §7.5; Topic 7 complete · AP-2 §14.3 polarisation portion*

8. **[[Reflection and Refraction]]** — mirror images, Snell from wavefronts, apparent depth, critical angle, fibres and dispersion. *0625 §3.2 partial · IB C.3.1 · AP-2 13.1/13.3*

9. **[[Lenses and Image Formation]]** — ray bundles, six image regimes, the lens equation derived, cameras, projectors and vision correction; four SVG sets and a rendered Manim. *0625 §3.2.3 · AP-2 13.4*

10. **[[Sound]]** — a longitudinal wave of compressions and rarefactions that needs a medium; 330–350 m/s and why temperature, not pressure, sets it; $v = \sqrt{\text{stiffness}/\text{density}}$ for air, water and steel; four speed experiments with their simulated uncertainties; amplitude → loudness, frequency → pitch, the audible range; five WAV files and a Manim; six real questions. *0625 §3.4 · AP-2 14.1–14.2 · IB C.2*

*9702 Topic 7 and 0625 Topic 3 complete. Remaining wave/optics scope: curved-mirror imaging for AP2, plus AP-2 §14.3 finite string-join reflection/transmission.*

---

## Quantum-Nuclear (5 — open)

*Where the wave picture and the particle picture are both true, and what that does to the atom and the nucleus.*

1. **[[Wave-Particle Duality]]** — photons as quanta with E = hf and p = E/c; the double slit run one photon at a time (fringes by a thousand dots, a blur with one slit shut); the photoelectric effect's three facts, Einstein's equation for three metals and Millikan's h/e line; de Broglie, the electron-diffraction tube and the ring-shrinking chain; seven real questions across 9702 Paper 4 and AP. *9702 §22.1–22.3 · IB E.2.1–E.2.3 · AP-2 §15.1 + §15.5*

2. **[[Energy Levels and Line Spectra]]** — quantised hydrogen energies derived from the Bohr model, photons as level gaps, absorption/emission and cascades, ionisation, stellar chemistry and atomic clocks; three real Cambridge/IB/AP questions and a runnable transition explorer. *9702 §22.4 · IB E.1.2/E.1.4 · AP-2 §15.2–15.3*

3. **[[Nuclear Physics]]** — why nuclei hold together and decay; Rutherford, quarks, random decay, binding energy and fission/fusion, with smoke alarms, tracers, dating and reactors. *9702 §11/§23 · 0625 §5 · IB E.1/E.3/E.4 · AP-2 §15.7–15.8*

4. **[[Quantum States and the Schrödinger Equation]]** — normalisation, phase and Schrödinger evolution; the infinite well, coherent preparation versus mixture, Fourier uncertainty and quantum-dot displays, with three SVGs and 4K Manim. *University enrichment*

5. **[[Quantum Tunnelling]]** — boundary matching, conserved probability current and exponential transmission; CPU gate leakage, SSD programming/retention and STM, with three SVGs and 4K Manim. *University enrichment*

*Cambridge quantum/nuclear/particle core complete. Enrichment shelf: [[Pauli Exclusion Principle]].*

## Thermal (8)

*The thermodynamics core, complete: kinetic theory → internal energy → specific heat → first law → entropy.*

1. **[[Kinetic Theory and the Ideal Gas]]** — states, syringe compression and Brownian motion; pressure and temperature derived from molecular collisions, with particle animation and Boyle graph. *0625 §2.1 · 9702 §15 · IB B.3 · AP-2 9.1–9.2*
2. **[[Internal Energy]]** — random KE + intermolecular PE; for a fixed amount of monatomic ideal gas $U = \tfrac32 nRT$ depends on temperature alone; degrees of freedom and equipartition.
3. **[[Specific Heat Capacity]]** — $Q = mc\Delta T$ and $Q = mL$: heating fills the kinetic term, phase change pays the potential term; $C_p = C_V + R$.
4. **[[First Law of Thermodynamics]]** — $\Delta U = Q + W$ with the sign convention taught principle-first; the four processes on the $p$–$V$ diagram.
5. **[[Entropy and the Second Law]]** — Clausius, Kelvin and entropy as three voices of one law; $S = k\ln W$; the second law as overwhelming odds, not decree.

6. **[[Temperature and Thermometry]]** — equilibrium, thermometric properties, Kelvin scale, calibration, response and probe loading. *9702 §14.1–14.2*

7. **[[Heat Transfer]]** — conduction, convection and radiation; thermal resistance, insulation, Earth’s balance and measured conductivity. *0625 §2.3 · IB B.1 · AP-2 9.3/9.5*
8. **[[Thermal Expansion]]** — the lopsided bond that makes matter grow when heated; solids, liquids and gases compared; expansion gaps, the bimetallic strip, thermal stress, water at 4 °C. *0625 §2.2.1*

*Cambridge Topic 14 and 0625 §2.1/§2.3 complete. Remaining: expansion applications and other IGCSE thermal outcomes; audit existing teaching before adding treatments.*

## Electricity (6 — closed)

1. **[[Electric Current]]** — charge as the bottom of the tower; current as a rate; $I = nAvq$ by the slab count and the drift-velocity shock. *9702 §9.1 · 0625 §4.2*
2. **[[Resistance]]** — $V = IR$ is a definition, Ohm's law is an empirical claim: the four $I$–$V$ characteristics, resistivity, p.d. vs e.m.f. *9702 Topic 9 closed*
3. **[[Kirchhoff's Laws]]** — the junction rule is charge conservation, the loop rule is energy conservation; series and parallel derived from them; six real exam circuits (Cambridge, AP C E&M, IGCSE); the coulomb walks the potential hill. *9702 §10.2 · 0625 §4.3.2 · AP-2/AP-C §11.5–11.7*

4. **[[Internal Resistance]]** — the source as a resistor: $V = \mathcal{E} - Ir$ derived from energy and from the loop rule, the $V$–$I$ line (intercept, gradient, short-circuit current), maximum power transfer at $R = r$ and its 50 % sting, the voltmeter as a load and the null method; six real questions (Cambridge P2 ×3, AP C 2015 linearised, IB ×2). *9702 §10.1 · AP-2/AP-C Unit 11 · IB B.5.4*
5. **[[Potential Dividers]]** — $V_{\text{out}} = E R_2/(R_1+R_2)$ from both Kirchhoff laws; thermistor and LDR dividers, the loading effect plotted, the potentiometer and the null method; mains safety for 0625 §4.4. *9702 Topic 10 closed · 0625 §4.3–4.4 · IB B.5.4*

6. **[[Alternating Current]]** — the tide, not the river: r.m.s. from the heating definition and ⟨sin²⟩ = ½, mean power half the peak, the bridge rectifier in both half-cycles, smoothing as an $RC$ discharge simulated against the schemes; beyond syllabus, phasors and complex impedance verified against the differential equation. *9702 Topic 21 closed · 0625 §4.2.2*

*Bay closed 2026-09-09: the planned run [[Electric Current]] → [[Alternating Current]] is complete; the field-theoretic side ([[Electric Field]], [[Energy Resources]]) belongs to Fields.*

## Fields (7 — open)

1. **[[Capacitors]]** — $C = Q/V$ as an electrical spring; the parallel-plate formula derived from the field; energy $\tfrac12 CV^2$; charging and discharging through a resistor.
2. **[[Lorentz Force]]** — $\mathbf{F} = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$: ignores stationary charge, pushes sideways, does no work; $F = BIL\sin\theta$ by the parade derivation.
3. **[[Electromagnetic Induction]]** — magnetism makes electricity only while it changes: flux, Faraday's law in three costumes, Lenz's law as energy conservation signing its name. *9702 Topic 20*
4. **[[Maxwell's Equations]]** — the constitution of E and B in four sentences; the capacitor that broke Ampère's law and the displacement current; light from two bench constants. 💎

5. **[[Electric Field]]** — charge transfer and induction, Coulomb’s law, vector superposition, conductor equilibrium and charged-particle parabolas; laser printers, continuous-charge integrals and Gauss-law symmetry. *9702 §18.1–18.4 · 0625 §4.2.1*

6. **[[Electric Potential]]** — potential as energy per charge; reference at infinity, signed work, equipotentials, pairwise assembly and continuous-source integrals; accelerating voltage as the electron microscope’s energy dial. *9702 §18.5 · IB D.2 HL · AP C Unit 9*

7. **[[Magnetism and Magnetic Materials]]** — poles, compass mapping, induced magnetism, domains, material response and hysteresis; relays/speakers and permeability. *0625 §4.1 + §4.5.3 · AP2/AP-C EM 12.1*

*9702 Topic 18 and IGCSE magnetism/electromagnetic effects complete at mapped-row granularity. Remaining brief: [[Energy Resources]]; verify its residual scope against existing teaching.*

## Modern (1 — open)

**[[Special Relativity]]** — two postulates; time dilation from a light clock and Pythagoras; length contraction; the relativity of simultaneity; the Lorentz transformation; the invariant interval; space-time diagrams; muons measured on a mountain; GPS. *IB A.5 HL*

*Next: [[General Relativity]], and [[Particle Physics]] beyond the quark introduction in [[Nuclear Physics]]. Cambridge §11/§22–23 and 0625 §5 are taught in Quantum-Nuclear above.*

## Astronomy (4 — open)

**[[Stellar Luminosity and Size]]** — inverse-square distance, calibrated candles, blackbody spectra and radius from light; three controls, distinct measurements. *9702 §25.1–25.2 · IB B.1/E.5 radiation and radius · AP-2 §15.4*

**[[Hubble's Law and the Expanding Universe]]** — why every observer sees the same expansion law; redshift, the cosmic clock and the hot Big Bang. *9702 §25.3 · 0625 §6.2.3*

**[[Stellar Evolution]]** — cloud to white dwarf, neutron star or black hole; the balance that holds a star up, fusion as the payer, the HR diagram, parallax. *0625 §6.2.1–6.2.2 · IB E.5*

**[[The Solar System]]** — day, seasons and Moon phases from one tilted spinning ball; the inventory and the planets' table; why rock inside and gas outside; speeds, ellipses and energy. *0625 §6.1*

*All mapped Cambridge astronomy rows are complete. Enrichment candidates: exoplanets, tides.*

## Medical (3 — closed)

Sound and radiation as probes of structure and function. 9702 Topic 24 complete.

**[[PET Scanning]]** — chemistry delivers the label; paired annihilation photons and timing constrain its distribution; noisy counts become an image.

**[[X-rays and CT]]** — an X-ray tube makes photons; many projections reconstruct a slice, without peeling the onion.

**[[Ultrasound]]** — the gel, the echo clock and the image; acoustic impedance, reflection and round-trip attenuation.

## Foundations (9 — closed)

*The measurement curriculum end to end: quantities and units → vectors → the two error axes → their remedies → honest reporting. 9702 Topic 1 · 0625 §1.1 · IB PRAC.*

1. **[[Physical Quantities and Units]]** — number × unit; the seven SI base units and the 2019 redefinition; dimensional homogeneity, with the pendulum period from dimensions alone.
2. **[[Vectors in Physics]]** — a vector doesn't *have* components, you choose them; the scalar/vector taxonomy; the swimmer across the river.
3. **[[Error Propagation]]** — $\Delta z \approx \lvert f'(x) \rvert \Delta x$ as the master rule: absolute errors add, percentage errors add, powers multiply them.
4. **[[Accuracy vs Precision]]** — systematic vs random as two orthogonal axes — calibrate one, average the other; the dartboard.
5. **[[Repeated Measurements]]** — Galton's ox and SEM $= \sigma/\sqrt N$; why averaging eats noise but not bias.
6. **[[Calibration of Instruments]]** — reference comparisons, corrections and their uncertainty; the Hubble mirror; the traceability pyramid.
7. **[[Significant Figures]]** — an honesty contract between writer and reader; rounding conventions motivated by error propagation, explicit uncertainties and board-specific reporting rules.
8. **[[Planning an Experiment]]** — independent, dependent and control variables; apparatus → method → enough data → table → analysis; why five spread values and repeats, simulated; techniques, hazards and matched improvements; the twelve practical contexts. *0625 practical skills P1–P3, P6–P7 · 9702 Paper 5 planning · AP experimental design*
9. **[[Recording and Analysing Experimental Data]]** — reading scales to half a division, tables, best-fit lines, the large gradient triangle, intercepts, anomalies and the 10 % test. *0625 P4–P5 · 9702 Papers 3/5*

---

## Mathematics cards that bridge into physics

These live in `Mathematics/` and carry `subject/physics` tags; they resolve physics rows without a physics-side twin.

| Card | Home | Physics rows it touches |
|------|------|-------------------------|
| [[Vectors]] | Geometry | 9702 §1.4 · 0625 §1.1 |
| [[Magnitude of a Vector (Vocab)]] | Geometry | 9702 §1.4 |
| [[Kinematics Calculus]] | Calculus | 9702 §2.1 · 9709 §4.2 |
| [[Travel Graphs (Vocab)]] | Algebra | 9702 §2.1 · 0625 §1.2 |
| [[Connected Rates of Change]] | Calculus | 9702 §2.1, §3.1 |
| [[Exponential Growth and Decay]] | Number | 9702 §23.2 (decay) · §16 (cooling) |

---

## How this directory stays honest

- **One line per card.** The hook says what the card teaches; the card carries everything else. If a line wants a second sentence, the second sentence belongs in the card.
- **Counts match the disk.** Each bay's number is the `.md` count in its folder and the total at the top is their sum; the linter checks both, and flags any line that has grown past a paragraph.
- **The landing story lives elsewhere.** What each card closed, and why it was built when it was, is recorded in the maintainer trackers at close-out — never here.
