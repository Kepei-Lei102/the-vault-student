---
chinese: 波粒二象性 (bō lì èr xiàng xìng)
prerequisites:
  - "[[Superposition and Interference]]"
  - "[[Diffraction]]"
  - "[[Work, Energy and Power]]"
  - "[[Linear Momentum]]"
leads_to:
  - "[[Quantum States and the Schrödinger Equation]]"
  - "[[PET Scanning]]"
  - "[[Energy Levels and Line Spectra]]"
  - "[[Pauli Exclusion Principle]]"
  - "[[Nuclear Physics]]"
tags:
  - subject/physics
  - domain/quantum
  - domain/waves
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-22-1
  - syllabus/9702-22-2
  - syllabus/9702-22-3
  - syllabus/IB-Physics-E-2-1
  - syllabus/IB-Physics-E-2-2
  - syllabus/IB-Physics-E-2-3
  - syllabus/AP-Physics-2-15-1
  - syllabus/AP-Physics-2-15-5
  - misconception/brighter-light-faster-electrons
  - misconception/photons-pool-their-energy
  - misconception/de-broglie-is-a-formula
  - type/deep
---

# Wave-Particle Duality 波粒二象性

> *Send light through two slits and it draws fringes; that is a wave. Send it onto a metal and it knocks out electrons one photon at a time, each with an energy set by the colour and not the brightness; that is a particle. Send electrons through a crystal and they draw rings. Nothing in physics before 1905 allowed both, and everything after 1927 requires it.*

## Definition

### Formal

Electromagnetic radiation has a **particulate nature** as well as a wave nature: its energy comes in **photons**, each a quantum of electromagnetic energy

$$E = hf = \frac{hc}{\lambda}, \qquad h = 6.63 \times 10^{-34}\ \text{J s},$$

and each photon carries momentum $p = E/c = h/\lambda$. The **electronvolt**, $1\ \text{eV} = 1.60 \times 10^{-19}$ J, is the energy an electron gains through one volt, and the natural unit for photons and electrons.

The **photoelectric effect** is the emission of electrons from a metal surface illuminated by electromagnetic radiation. A metal has a **work function** $\Phi$, the minimum energy needed to remove an electron from its surface. An electron absorbs one photon or none, so emission needs $hf \ge \Phi$: there is a **threshold frequency** $f_0 = \Phi/h$ (a **threshold wavelength** $\lambda_0 = hc/\Phi$) below which no electrons leave however intense the light, and above it the fastest electrons obey

$$hf = \Phi + \tfrac12 m v_{\max}^2.$$

The maximum kinetic energy depends on frequency and not on intensity; the photoelectric *current* is proportional to intensity, because intensity is photons per second.

**Wave–particle duality:** the photoelectric effect is evidence for the particle nature of electromagnetic radiation; interference and diffraction are evidence for its wave nature. Matter shows the same duality: a moving particle has a **de Broglie wavelength**

$$\lambda = \frac{h}{p} = \frac{h}{mv},$$

and **electron diffraction**, a beam of electrons through a thin crystal producing rings, is the evidence.

### Intuitive

A wave spreads its energy thinly over a whole wavefront; a particle carries it all in one place. Light manages both by arriving as *countable* parcels whose *probability* of landing anywhere is what the wave describes: dim the light until one photon is in flight at a time and the fringes still build up, dot by dot, over hours. That is the whole of duality in one experiment, and the photoelectric effect is the same fact from the metal's side: an electron cannot save up a fraction of a photon, so red light never frees it and violet always does, and a brighter lamp only sends more parcels of the same size. Electrons return the compliment. Give one enough speed and its wavelength shrinks to the spacing of atoms, and a crystal diffracts it like a grating diffracts light.

### 中文锚点

光和电子都具有**波粒二象性**：传播时会出现干涉和衍射，探测时又表现为一次次局部的能量交换。双缝实验中，单个光子只留下一个点，许多光子的落点累积起来却形成条纹。光子的能量为 $E=hf$；在通常的单光子光电效应中，光子能量必须达到金属的逸出功，才能释放电子，超过阈值后最快电子的动能满足 $K_{\max}=hf-\Phi$。因此，在这个条件下，频率太低的光并不能靠增加亮度来替代足够的单个光子能量。电子也有德布罗意波长 $\lambda=h/p$。**电子显微镜**正利用这一点：加速后的电子波长比可见光短得多，这让电子显微镜有可能分辨远小于普通光学显微镜分辨极限的结构；实际能看多细，还受透镜、样品和像差等因素限制。所谓二象性，不是粒子随意切换身份，而是同一个量子对象的行为不能只靠经典的“波”或“粒子”之一来描述。


---

## Part I — One photon at a time

[[Superposition and Interference]] ended with the sentence that opens quantum physics: send light through Young's slits so faintly that only one photon is in flight at once, and the fringes still appear. G. I. Taylor did it in 1909 with a gas flame behind smoked glass and a three-month exposure; Akira Tonomura filmed it with electrons in 1989, one arriving every few milliseconds, and the film is the most-watched piece of evidence in the subject.

![[wave-particle-duality-dots.svg|700]]

`wave-particle-duality-sim.py` reproduces the logic rather than the apparatus. It takes the two-slit intensity from [[Diffraction]], two slits of finite width, treats it as a **probability density**, and draws photons from it one at a time. Each photon lands at one point, as a particle must. After ten photons the dots are noise: their correlation with the interference pattern is $0.22$. After a hundred, $0.64$; after a thousand, $0.95$; after twenty thousand, $1.00$, and the fringes are exact. Cover one slit and the same twenty thousand photons land in a smooth single-slit blur, correlation $0.29$ with the two-slit pattern and $0.97$ with the one-slit envelope.

That last line is the strange one, and worth slowing down for. Every photon in the two-slit run went through *a* slit, landed at *a* point, and never met another photon. Yet where it was allowed to land depended on whether the *other* slit was open. The wave is not a crowd effect; it belongs to each photon on its own. Each photon interferes with itself.

**And if you watch which slit?** The natural next experiment is to put a detector at one slit, so that each photon's path is known, and keep both slits open. Do that and the fringes vanish: the dots fall in two overlapping single-slit blurs, as if the photons had been sent through one slit or the other and never both. This is measured fact, not folklore, and it is the sharpest statement of duality there is. The wave belongs to a photon whose path is *undetermined*; the moment the apparatus records a path, the photon has one, and a thing with one path cannot interfere with itself. It is not about a person looking, and not about disturbance in the ordinary sense: any physical record of the path does it, however gently, and erasing that record before the photon lands brings the fringes back (the "quantum eraser" experiments of the 1990s). [[Quantum Mechanics]] is where the rule behind this is written down; here it is enough to know that "which slit?" and "which fringe?" are questions the same photon cannot answer both of.

![[wave-particle-duality-manim.mp4]]

*The two films: the dots arriving one at a time; then photons of rising frequency hitting sodium, which is Part II.*

Each photon of the 600 nm light in the simulation carries $E = hc/\lambda = 3.31 \times 10^{-19}$ J, which is $2.07$ eV, and a one-milliwatt laser pointer emits three thousand million million of them a second. That is why the wave picture works so well in daily life: the parcels are tiny and absurdly numerous, and a smooth wave is what a great many small dots look like from a distance. The parcel only shows itself when a single one has to do something, which is Part II.

---

## Part II — The photoelectric effect: what the wave theory cannot explain

Shine light on a clean metal in a vacuum and electrons come off. That much was known in 1887 (Hertz noticed it while discovering radio waves). The details, measured carefully by Lenard in 1902 and Millikan in 1916, were the problem:

1. Below a certain frequency, the **threshold frequency** $f_0$, no electrons are emitted **at any intensity**. Above it, emission is immediate at any intensity, however faint.
2. The **maximum kinetic energy** of the electrons increases with the light's frequency and **does not depend on its intensity**.
3. The **number** of electrons per second, the photoelectric current, **is** proportional to intensity.

A wave carries energy spread over its front, and the wave theory predicts the opposite of all three. Energy should pile up gradually, so dim light should work after a delay: the simulation does the arithmetic, and at one microwatt per square metre an atom-sized target collects the $2.28$ eV sodium needs in about 135 days. Emission is observed within nanoseconds. Brighter light delivers more energy per second, so it should give faster electrons: it does not. And any frequency should do, given time: it does not.

Einstein's 1905 answer, the paper his Nobel prize named, was to take Planck's quantum seriously as a thing that travels. Light arrives in **photons** of energy $hf$; an electron in the metal absorbs one photon whole or none; a fixed **work function** $\Phi$ is the price of leaving the surface; whatever is left is the electron's kinetic energy:

$$hf = \Phi + \tfrac12 m v_{\max}^2.$$

Every observation falls out. Below $f_0 = \Phi/h$ a photon cannot pay the exit fee, and no number of them can club together, so nothing leaves at any intensity. Above it the most energetic electron, the one from the surface itself, gets $hf - \Phi$, fixed by frequency alone. Intensity is photons per second, so it sets the current and nothing else. And since each photon is absorbed whole, the first photon to arrive frees the first electron: no delay.

![[wave-particle-duality-photoelectric.svg|700]]

The script runs the bookkeeping for three metals. At $700$ nm ($1.77$ eV) none of sodium, zinc or caesium emits; at $400$ nm ($3.10$ eV) sodium's electrons leave with $0.82$ eV and zinc's not at all, because zinc's work function is $4.31$ eV; at $250$ nm everything emits, and the fastest sodium electron has $2.68$ eV. The thresholds are $544$ nm for sodium, $288$ nm for zinc, which is why zinc needs ultraviolet in the school demonstration and a caesium cell works in visible light.

**Measuring $h$.** Hold the collector at a negative potential until even the fastest electrons cannot reach it: at that **stopping voltage** $V_s$, $eV_s = \tfrac12 m v_{\max}^2$, so $eV_s = hf - \Phi$. Plot $V_s$ against $f$ and the line has gradient $h/e$ and cuts the frequency axis at $f_0$. Millikan did this for sodium in 1916, expecting to refute Einstein, and measured $h = 6.57 \times 10^{-34}$ J s. The figure's right panel is that line drawn from the modern constants, gradient $4.14 \times 10^{-15}$ V s.

![[wave-particle-duality-current.svg|700]]

The current–voltage graph is the one the exam draws. Two curves at the same frequency and different intensities have the *same* stopping voltage and different plateaus; two at different frequencies and the same intensity have the same plateau and different stopping voltages. If you can explain why each pair differs in exactly one way, you have the whole of §22.2.

---

## Part III — Duality, and the electronvolt

So light is a wave in Part I and a particle in Part II, and the honest statement is that it is neither in the everyday sense: it is something that *propagates* as a wave and *exchanges energy* as a particle. Interference and diffraction are evidence for the wave; the photoelectric effect is evidence for the particle; the syllabus asks for exactly that sentence and the June 2026 paper set it as a table with four boxes.

Photons also carry **momentum**. A wave of energy $E$ travelling at $c$ carries $p = E/c$, which is $h/\lambda$; a $3.11 \times 10^{-19}$ J photon (the March 2024 question's) carries $1.04 \times 10^{-27}$ N s. Absorb a beam of power $P$ and the surface receives momentum $P/c$ per second, a force $F = P/c$: light pushes. A $350$ mW laser pushes with about a nanonewton, which is nothing, and sunlight on a square kilometre of sail pushes with a few newtons forever, which is a spacecraft.

The **electronvolt** is worth a paragraph because it is where students lose marks. It is a unit of *energy*: the energy gained by one electron accelerated through one volt, $1.60 \times 10^{-19}$ J. Work functions are given in eV; photon energies at visible wavelengths are a few eV; a $5$ kV electron has $5$ keV. Convert to joules to use $hf = \Phi + \tfrac12 mv^2$ with $m$ in kilograms, or work entirely in eV and convert at the end. Never mix.

---

## Part IV — De Broglie: matter waves, and the tube

In 1924 Louis de Broglie's doctoral thesis asked the question in reverse: if waves come in particles, do particles come in waves? He proposed that any moving particle has a wavelength

$$\lambda = \frac{h}{p} = \frac{h}{mv},$$

the same relation photons obey, and his examiners sent the thesis to Einstein, who said it was more than a thesis. Three years later Davisson and Germer in New York and G. P. Thomson in Aberdeen diffracted electrons from crystals and measured the wavelength de Broglie had predicted. (Thomson's father, J. J., had won the Nobel prize for showing the electron was a particle; the son won it for showing it was a wave.)

![[wave-particle-duality-de-broglie.svg|700]]

The wavelength is what the numbers say it is. An electron accelerated through $5.0$ kV has $p = \sqrt{2m \cdot eV} = 3.8 \times 10^{-23}$ N s and $\lambda = 17$ pm, a tenth of an atom's width. A proton at the same energy, being 1836 times heavier, has a wavelength 43 times shorter. A tennis ball at $50$ m/s has $\lambda = 2 \times 10^{-34}$ m, twenty-four orders of magnitude smaller than the ball; no slit will ever diffract it, which is why cricket balls do not interfere and why nobody noticed matter waves for twenty-five centuries.

![[wave-particle-duality-tube.svg|700]]

**The electron-diffraction tube** is the experiment the syllabus asks you to describe and interpret. Electrons from a heated filament are accelerated through a few kilovolts to a thin film of graphite, whose carbon atoms lie in planes about $0.21$ nm apart, and then fly on to a fluorescent screen. If electrons were only particles, the screen would show a spot. It shows a **bright central spot surrounded by concentric rings**: the planes act as a grating, the electrons diffract at $\sin\theta = n\lambda/2d$, and because the film's tiny crystals point every way the maxima become rings. For the $5$ kV electron and the $0.213$ nm spacing the first-order angle is $2.3^\circ$, a ring a few centimetres across on the screen. **Raise the accelerating voltage** and the electrons' momentum rises, their wavelength falls, and the rings shrink toward the centre, which is the question the papers ask most: the June 2023 report notes candidates knew the rings shrank but could rarely say why. The chain is: higher p.d. → more momentum → shorter de Broglie wavelength → smaller diffraction angle for the same plane spacing → smaller rings.

The rings are the evidence, and the syllabus wants the reasoning in order: the pattern is a *diffraction* pattern; diffraction is a *wave* phenomenon; therefore the electrons are behaving as waves. The report is blunt about the common failure: candidates "were given credit for stating that electrons were behaving as waves but very rarely explained the pattern".

---

## Where it is the working tool

- **The electron microscope.** Conventional far-field light microscopy has a diffraction-limited resolution of order hundreds of nanometres. Electrons accelerated through $100$ kV have a wavelength of about $3.7$ pm, allowing much finer structures to be resolved. The short wavelength makes atomic-resolution imaging possible, but electron optics, aberrations, specimen preparation and stability also constrain the actual resolution. [JEOL: electron-microscope wavelengths](https://www.jeol.com/products/science/em.php)
- **Solar cells and camera sensors.** Absorbed photons can create electron–hole pairs inside a semiconductor; a junction separates or collects these carriers. This is an internal photoelectric process, distinct from ejecting an electron into vacuum. Silicon’s band gap is about $1.1$ eV: it can detect visible light and some near-infrared, with the long-wavelength response ending around $1100$ nm. For above-gap photons, excess energy can become heat; the entire blue photon is not simply wasted. Collection efficiency and wavelength affect the signal. [Hamamatsu: silicon photodiode spectral ranges](https://www.hamamatsu.com/us/en/product/optical-sensors/photodiodes/si-photodiodes.html)
- **Photomultipliers and night vision.** A caesium-coated cathode ($\Phi = 2.14$ eV) turns single visible photons into electrons, which are then multiplied a million-fold; the same tube detects the flashes in a particle detector and the faint light in a night-vision scope.
- **X-ray and neutron diffraction.** Crystallographers choose the probe by its wavelength: X-rays at $0.1$ nm, or thermal neutrons whose de Broglie wavelength is the same $0.1$ nm at room temperature and which see hydrogen atoms X-rays miss. Rosalind Franklin's photograph of DNA and every drug's crystal structure since are this.
- **Solar sails and laser cooling.** Photon momentum is tiny but real: the IKAROS sail flew on it in 2010, and laser cooling uses the recoil of absorbed photons to slow atoms to microkelvin, the technique behind atomic clocks.

---

## Worked examples — every tool named

### Example 1 — the definitions and the threshold (Cambridge 9702, November 2021 Paper 42, Q9)

*(a) State what is meant by (i) the photoelectric effect, (ii) work function energy.* — (i) The **emission of electrons** from a metal surface when **electromagnetic radiation is incident** on it. (ii) The **minimum energy required for an electron to leave the surface**. *(B1 B1; B1.)*

*(b) A polished calcium plate in a vacuum gives no photoelectric current when the light's frequency is below $6.93 \times 10^{14}$ Hz. (i) Name this frequency. (ii) Explain how the photon model accounts for it. (iii) Calculate calcium's work function in eV.* — (i) The **threshold frequency**. (ii) *Tool: Part II's three sentences.* Photons are **discrete packets of energy** whose energy **depends on frequency**; an electron can **absorb only a single photon**; emission is possible **only if the photon energy is at least the work function**. *(Two of the first three, plus the last, B2 + B1.)* (iii) *Tool: at threshold, $hf_0 = \Phi$:* $\Phi = 6.63 \times 10^{-34} \times 6.93 \times 10^{14} = 4.59 \times 10^{-19}$ J $= 4.59 \times 10^{-19}/1.60 \times 10^{-19} = 2.87$ eV. *(C1 A1. The June 2021 report on the same explanation: "many responses did not include the word 'photon'".)*

### Example 2 — the fastest electron, and the graph (Cambridge 9702, November 2024 Paper 41, Q8)

Magnesium emits electrons under ultraviolet of frequency at least $8.8 \times 10^{14}$ Hz. *(a) Name the phenomenon.* — The photoelectric effect. *(b)(i) The work function.* — $\Phi = hf_0 = 6.63 \times 10^{-34} \times 8.8 \times 10^{14} = 5.8 \times 10^{-19}$ J. *(ii) For radiation of $11 \times 10^{14}$ Hz, the maximum speed of the electrons.* — *Tool: $hf = \Phi + \tfrac12 m v_{\max}^2$, everything in joules:* $6.63 \times 10^{-34} \times 11 \times 10^{14} = 5.8 \times 10^{-19} + \tfrac12 \times 9.11 \times 10^{-31} v^2$, so $v_{\max} = 5.7 \times 10^5$ m s⁻¹. *(C1 C1 A1.)* *(c) Sketch $E_{\max}$ against $f$ from $8.0$ to $11 \times 10^{14}$ Hz.* — **Zero** from $8.0$ to $8.8$; then a **single straight line of positive gradient** from $(8.8, 0)$ passing through $(11, 1.45 \times 10^{-19}\ \text{J})$. *(Three B marks, one for each feature. The line does not start at the origin and is not curved.)*

### Example 3 — photon momentum, and light's push (Cambridge 9702, March 2024 Paper 42, Q7)

*(a) A photon has energy $3.11 \times 10^{-19}$ J. Calculate its momentum.* — *Tool: $p = E/c$* $= 3.11 \times 10^{-19}/3.00 \times 10^8 = 1.04 \times 10^{-27}$ N s. *(b) A $350$ mW laser at $640$ nm. (i) Photons per second.* — *Tool: $E = hc/\lambda$ per photon, then divide the power:* $N = 0.350/(6.63 \times 10^{-34} \times 3.00 \times 10^8/640 \times 10^{-9}) = 1.1 \times 10^{18}$ per second. *(ii) The beam is absorbed by a surface. Show that the force is $F = P/c$.* — *Tool: force is rate of change of momentum:* in time $t$ the beam delivers energy $Pt$, hence momentum $Pt/c$; $F = (Pt/c)/t = P/c$. *(M1 A1: the scheme wants $p = E/c$ and $E = Pt$ used explicitly.)* *(c) Tungsten, magnesium and potassium have work functions $4.49$, $3.68$ and $2.26$ eV. (i) Explain the term threshold wavelength. (ii) Calculate the largest threshold wavelength.* — (i) The **maximum wavelength** of radiation that causes electrons to be emitted from the surface. (ii) *Tool: the smallest work function gives the longest wavelength:* $\lambda_0 = hc/\Phi = 6.63 \times 10^{-34} \times 3.00 \times 10^8/(2.26 \times 1.60 \times 10^{-19}) = 5.50 \times 10^{-7}$ m. *(C1 A1.)*

### Example 4 — the tube (Cambridge 9702, June 2023 Paper 41, Q7)

*(a) State what is meant by the de Broglie wavelength.* — The wavelength associated with a **moving** particle. *(B1. The report: "the word 'moving' was frequently missing", and "a formula is not correct in this instance".)* *(b) Electrons accelerated through a high p.d. pass through a thin graphite crystal to a fluorescent screen, which shows a pattern of rings. (i) Name the phenomenon. (ii) What can be concluded about the nature of electrons?* — (i) Electron **diffraction**. (ii) The rings show the beam has **spread out** into light and dark regions, an **interference pattern**, so the electrons are **behaving as waves**. *(B1 B1: the pattern first, the conclusion second.)* *(c) The accelerating p.d. is increased. (i) Sketch the new pattern. (ii) Explain the change.* — (i) A central spot and concentric rings, **closer to the centre** than before. (ii) Greater p.d. gives the electrons **greater momentum**, so a **shorter de Broglie wavelength**; for the same crystal spacing, a shorter wavelength gives a **smaller diffraction angle**, so the rings shrink. *(B1 B1. "Candidates generally realised that an increase in p.d. would lead to a greater electron momentum and hence a shorter de Broglie wavelength, but they did not always explain why that changed the pattern.")*

### Example 5 — the four boxes (Cambridge 9702, June 2026 Paper 42, Q9)

*(a) State what is meant by the de Broglie wavelength.* — The wavelength associated with a moving particle. *(b) Complete the table: evidence for the wave nature and the particle nature of matter and of electromagnetic radiation.* — Matter, wave: **electron diffraction**. Matter, particle: any of Brownian motion, the states of matter, quantisation of charge, Rutherford scattering. Radiation, wave: **diffraction or interference** (Young's slits), polarisation. Radiation, particle: the **photoelectric effect** (or line spectra, or Compton scattering). *(Four B marks.)* *(c) An electron is accelerated through $3500$ V. (i) Its speed. (ii) Its de Broglie wavelength.* — *Tool: $eV = \tfrac12 mv^2$:* $v = \sqrt{2 \times 1.60 \times 10^{-19} \times 3500/9.11 \times 10^{-31}} = 3.5 \times 10^7$ m s⁻¹. *Tool: $\lambda = h/mv$* $= 6.63 \times 10^{-34}/(9.11 \times 10^{-31} \times 3.5 \times 10^7) = 2.1 \times 10^{-11}$ m. *(C1 C1 A1; C1 A1.)*

### Example 6 — the best question from another board: reading a table backwards (AP Physics 2, 2024 Free Response Q1)

Light of three frequencies is shone on two metals; for each trial the scientist records the *minimum de Broglie wavelength* of the ejected electrons. Frequency A gives $6.9 \times 10^{-10}$ m on metal 1 and $9.4 \times 10^{-10}$ m on metal 2; frequency B ejects nothing from either; frequency C gives $5.3$ and $6.3 \times 10^{-10}$ m. *(a) Which frequency is greatest and which least?* — *Tool: the fastest electron has the shortest wavelength, $\lambda = h/p$, and the fastest electron's energy is $hf - \Phi$.* Frequency B is the **least**: it is below both thresholds. Frequency C is the **greatest**: on each metal it gives the shorter wavelength, so the larger momentum, so the larger $hf - \Phi$, so the larger $f$. *(b) The maximum kinetic energy of the electrons from metal 1 in trial 1.* — *Tool: $p = h/\lambda$, then $KE = p^2/2m$:* $p = 6.63 \times 10^{-34}/6.9 \times 10^{-10} = 9.6 \times 10^{-25}$ N s; $KE = (9.6 \times 10^{-25})^2/(2 \times 9.11 \times 10^{-31}) = 5.1 \times 10^{-19}$ J, about $3.2$ eV. *(Scoring: one point each for $\lambda_e = h/mv$ or $K = p^2/2m$, for substituting $\lambda_e$ into a kinetic-energy expression, and for $K = 5 \times 10^{-19}$ J with units.)* *(c) Is metal 1's work function greater than, less than or equal to metal 2's?* — **Less.** For the same light, metal 1's electrons have the *shorter* wavelength, so the larger momentum and kinetic energy; $KE_{\max} = hf - \Phi$ with the same $hf$ means metal 1 has the smaller $\Phi$. *(The paragraph in (a) scores five points: B least and C greatest; $E = hf$; kinetic energy inversely related to $\lambda_e$; the threshold or energy argument; and a coherent paragraph.)* The question runs Parts II and IV in the same breath, which is why it is here.

### Example 7 — an electron's wavelength from its speed (Cambridge 9702, June 2025 Paper 41, Q8(a)–(b))

*(a) State what is meant by the de Broglie wavelength.* — The wavelength associated with a moving particle. *(b) Calculate the de Broglie wavelength of an electron moving at $4.9 \times 10^7$ m s⁻¹.* — *Tool: $\lambda = h/mv$* $= 6.63 \times 10^{-34}/(9.11 \times 10^{-31} \times 4.9 \times 10^7) = 1.5 \times 10^{-11}$ m. *(C1 A1.)* At sixteen per cent of the speed of light the classical momentum is about one per cent low; the syllabus, and the scheme, ignore it.

---

## Hands-on

- **`wave-particle-duality-sim.py`** — photons drawn one at a time from the two-slit pattern, with the correlation climbing from noise to certainty and one slit shut for comparison; the photoelectric bookkeeping for three metals and Millikan's line; de Broglie wavelengths for the tube's electron, a proton and a tennis ball, with the graphite Bragg angle. Change the wavelength in `double_slit_density` and watch the dots space out.
- **`wave-particle-duality-figures.py`**, **`wave-particle-duality-manim.py`** — the five figures, and the two films: the dots arriving, and photons of rising frequency hitting sodium.
- **A zinc plate and an electroscope.** Charge a clean zinc plate negatively on a gold-leaf electroscope, shine an ultraviolet lamp on it and the leaf falls; shine the brightest visible lamp you own and nothing happens; put a sheet of glass in the ultraviolet's path (glass absorbs UV) and the leaf stays up. That is Parts II's three facts in three minutes, and it is the demonstration the syllabus's "illuminated by electromagnetic radiation" has in mind.
- **A solar cell and coloured filters.** Compare photocurrent under filters with known transmission, accounting for incident photon flux rather than perceived brightness. Silicon can respond to near-infrared light such as $940$ nm, so a remote-control LED is not a below-threshold demonstration. To investigate the long-wavelength cutoff, use characterised illumination extending beyond roughly $1100$ nm and the device’s spectral-response data. A semiconductor band gap and a metal’s vacuum work function describe different transitions.

---

## Common Misconceptions (Teaching Notes)

### 1. "Brighter light gives faster electrons"
Intensity is photons per second. More photons free more electrons, so the current rises; each electron still gets $hf - \Phi$. Only frequency changes the maximum energy, and the reports mark this as the distinction the question is testing.

### 2. "Two weak photons can add up to free an electron"
An electron absorbs one photon or none. Below threshold, no intensity and no waiting time helps; the simulation's 135-day wave-theory delay is precisely the prediction the effect refutes.

### 3. "The de Broglie wavelength is $\lambda = h/mv$"
That is the formula. The *definition* is the wavelength associated with a **moving** particle, and the reports say the formula earns nothing when the definition is asked, and that "moving" is the word most often dropped.

### 4. "The rings shrink because the electrons hit harder"
Higher p.d. → more momentum → **shorter wavelength** → smaller diffraction angle. Every arrow is a mark; stopping at momentum loses the last one.

### 5. "The electronvolt is a voltage"
It is an energy, $1.60 \times 10^{-19}$ J. A work function of $2.26$ eV is $3.62 \times 10^{-19}$ J, and $\tfrac12 mv^2$ with $m$ in kilograms needs joules.

### 6. "The photoelectric effect shows light is only a particle"
It shows light *exchanges energy* as particles. Interference and diffraction, from the same light, show it *propagates* as a wave, and the June 2026 table asks for both columns.

---

## Exam Notes

### Cambridge 9702 (§22.1–22.3 — Paper 4, with the odd Paper 1 item)

§22.1: radiation has a particulate nature; a photon is a quantum of electromagnetic energy; $E = hf$; the electronvolt; photon momentum $p = E/c$. §22.2: photoelectrons; threshold frequency and wavelength; emission explained by photon energy and work function; $hf = \Phi + \tfrac12 m v_{\max}^2$; why $KE_{\max}$ is independent of intensity while the current is proportional to it. §22.3: the photoelectric effect as evidence for particles and interference/diffraction as evidence for waves; electron diffraction described and interpreted qualitatively; the de Broglie wavelength. Paper 4 sets one of these nearly every series, six to ten marks in the shapes of Examples 1–5, 7: definitions in the syllabus's words, a threshold or work-function calculation, the $E_{\max}$–$f$ sketch, photon momentum and $F = P/c$, the tube with its shrinking rings. **§22.4**, energy levels and line spectra, is [[Energy Levels and Line Spectra]]. The reports' standing errors are the misconceptions above.

### IB Physics (E.2.1–E.2.3 — HL)

E.2.1: the photon as a quantum of energy and momentum, $E = hf$, $p = h/\lambda$. E.2.2: the photoelectric effect with the work function, threshold frequency, $KE_{\max} = hf - \Phi$, the stopping voltage, and the **failure of the classical wave theory** stated explicitly, which Part II's three facts and the 135-day delay answer. E.2.3: wave–particle duality, $\lambda = h/p$, electron diffraction by Davisson–Germer or the graphite film. E.2.4, **Compton scattering**, is in the Beyond section: the May 2025 paper asked why Compton is *better* evidence for the particle nature than the photoelectric effect (it shows the photon's momentum, not only its energy), and IB will ask you to compute the scattered photon's energy from $\Delta\lambda$.

### AP Physics 2 (Units 15.1 and 15.5)

15.1: $E = hf$ and de Broglie $\lambda = h/p$, wave–particle duality. 15.5: the photoelectric effect with the work function, $KE_{\max} = hf - \Phi$ and the stopping voltage. AP's free-response questions run the two together, as Example 6 does, and want reasoning in paragraph form; 15.6, Compton scattering, is Beyond here.

### Where it is *not* examined

- **Cambridge 0625** has no photons and no photoelectric effect; its §5.1 is the nuclear atom, which is [[Nuclear Physics]].
- **AP Physics 1** and **AP Physics C** have no quantum physics.
- **9702 does not examine** Compton scattering, the uncertainty principle, or the relativistic correction to de Broglie's formula.

---

## Connections

- **Builds on:** [[Superposition and Interference]] — the two-slit pattern this card draws photons from, and its last paragraph; [[Diffraction]] — the grating that electrons turn into rings, and the finite-slit pattern used as the probability density; [[Work, Energy and Power]] — the electronvolt as work done by a field; [[Linear Momentum]] — $p = E/c$ and $F = P/c$.
- **Extends into:** [[Energy Levels and Line Spectra]] — photons absorbed and emitted whole by atoms; [[Pauli Exclusion Principle]] — the matter wave's other consequence; [[Nuclear Physics]] — the de Broglie wavelength as the ruler for the nucleus.
- **Bridges:** [[Probability Basics]] — the detection pattern as a probability density, and the dots as samples from it; [[Diffraction]]'s Beyond section on electrons through the same slits.

---

## Beyond Syllabus

### Compton scattering, and why IB prefers it
A photon can be scattered by an electron like a billiard ball, and the scattered photon's wavelength grows by $\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta)$, with $h/m_e c = 2.43$ pm. The photoelectric effect shows the photon has energy; Compton scattering (1923) shows it has **momentum**, delivered in a collision, which is the stronger claim. IB's May 2025 question: a $6.40$ pm photon of $0.194$ MeV scatters to $7.47$ pm; its energy falls to $hc/\lambda = 0.166$ MeV, and the electron recoils with the $0.028$ MeV difference.

### The uncertainty principle is duality's price
A wave with one wavelength fills all space; to localise a particle you must add wavelengths, and a spread of wavelengths is a spread of momentum: $\Delta x\,\Delta p \gtrsim h/4\pi$. Heisenberg's relation is not a limit on instruments; it is what "a particle that propagates as a wave" means.

### The Born rule, said plainly
Part I sampled detections from a density proportional to optical intensity. For a nonrelativistic particle, the Born rule gives the position probability density as $|\psi|^2$, where $\psi$ is a complex probability amplitude. Integrating over a region gives a probability; the wavefunction itself is not that density. Interference comes from adding amplitudes before squaring. Closing one slit changes the experimental preparation and the resulting pattern; the two-slit calculation does not assign each unmeasured particle a definite slit. [[Quantum States and the Schrödinger Equation]] develops normalisation, phase and time evolution.

### Relativity at the edges
$p = E/c$ for a photon is the massless case of $E^2 = p^2c^2 + m^2c^4$; de Broglie's $\lambda = h/mv$ is the low-speed case of $\lambda = h/\gamma mv$. At $5$ kV the electron's true momentum is $0.24\%$ above the classical value; at $100$ keV, the electron microscope's, it is $4.8\%$ and the wavelength is $3.7$ pm rather than $3.9$, and the instrument's designers use the exact form.

---

## LaTeX Reference

| Rendered | Source | Meaning |
|---|---|---|
| $E = hf = \dfrac{hc}{\lambda}$ | `E = hf = \dfrac{hc}{\lambda}` | photon energy |
| $p = \dfrac{E}{c} = \dfrac{h}{\lambda}$ | `p = \dfrac{E}{c} = \dfrac{h}{\lambda}` | photon momentum |
| $hf = \Phi + \tfrac12 m v_{\max}^2$ | `hf = \Phi + \tfrac12 m v_{\max}^2` | Einstein's photoelectric equation |
| $f_0 = \dfrac{\Phi}{h},\ \lambda_0 = \dfrac{hc}{\Phi}$ | `f_0 = \dfrac{\Phi}{h},\ \lambda_0 = \dfrac{hc}{\Phi}` | threshold frequency and wavelength |
| $eV_s = \tfrac12 m v_{\max}^2$ | `eV_s = \tfrac12 m v_{\max}^2` | stopping voltage |
| $\lambda = \dfrac{h}{p} = \dfrac{h}{mv}$ | `\lambda = \dfrac{h}{p} = \dfrac{h}{mv}` | de Broglie wavelength |
| $\Delta\lambda = \dfrac{h}{m_e c}(1 - \cos\theta)$ | `\Delta\lambda = \dfrac{h}{m_e c}(1 - \cos\theta)` | Compton shift (Beyond) |
