---
chinese: 能级与线状光谱 (néngjí yǔ xiànzhuàng guāngpǔ)
prerequisites:
  - "[[Electric Potential]]"
  - "[[Wave-Particle Duality]]"
  - "[[Stationary Waves]]"
  - "[[Circular Motion]]"
leads_to:
  - "[[X-rays and CT]]"
  - "[[Nuclear Physics]]"
  - "[[Doppler Effect]]"
  - "[[Pauli Exclusion Principle]]"
  - "[[Quantum Tunnelling]]"
teach_together:
  - "[[Stellar Luminosity and Size]]"
tags:
  - subject/physics
  - domain/quantum
  - domain/atomic-physics
  - domain/spectroscopy
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-22-4
  - syllabus/IB-Physics-E-1-2
  - syllabus/IB-Physics-E-1-4
  - syllabus/IB-Physics-E-5-4
  - syllabus/AP-Physics-2-15-2
  - syllabus/AP-Physics-2-15-3
  - type/deep
  - misconception/level-energy-is-photon-energy
  - misconception/absorption-means-faster-electron
  - misconception/atomic-spectrum-is-nuclear-decay
---

# Energy Levels and Line Spectra 能级与线状光谱

> *You cannot scoop a sample out of a star. You can spread its light out and read the missing colours. The remarkable part is not that the light crossed space: it is that an atom on the other side of the galaxy obeys the same energy rules as an atom in a laboratory lamp.*

## Definition

### Formal

An **energy level** is an allowed energy of a stationary state of a system. The bound states of an isolated atom have **discrete** energies: separated allowed values, not every value in between. A **line spectrum** contains narrow emission peaks or absorption dips at particular frequencies. In a single-photon transition between two bound levels,

$$\boxed{E_\gamma=hf=\frac{hc}{\lambda}=E_{\rm upper}-E_{\rm lower}>0.}$$

Here $\lambda$ is the photon's **vacuum wavelength**. The atom loses this energy in emission and gains it in absorption. Atomic recoil is negligible at the precision used below. The **gap**, not either level separately, sets the photon energy.

### Intuitive

The levels are permitted balances in the atom's energy account; the photon is the transaction. A transaction can go out or come in, but its size must match the change in the balance. The spectrum is a list of the transaction sizes the atom can make. Different atoms have different lists.

### 中文锚点

同样是小小一颗 LED，为什么有的发红光，有的发蓝光？颜色背后是每个光子带走的能量：电子与空穴复合时释放能量，蓝光光子比红光光子需要更多能量，对应的能量差也更大。孤立原子的能量只能在某些台阶之间变化，所以会留下特定的谱线。LED 用的是半导体能带，不能与原子能级混为一谈；两者共同提醒我们：光的颜色，能透露物质内部发生了多大的能量变化。

## Notation — keep three energies separate

| Symbol / term | Meaning | Watch for |
|---|---|---|
| $E_n$ | Total energy of the atom in level $n$ | Usually negative for a bound state; not the electron's kinetic energy |
| $E_\gamma$ | Photon energy $hf$ | Positive for both emitted and absorbed photons |
| $\Delta E_{\rm atom}=E_f-E_i$ | Change in the atom's energy | Positive for absorption, negative for emission |
| Ground / excited state | Lowest-energy state / any higher bound state | “Ground” does not mean zero energy |
| Excitation / ionisation | Raise the bound-state energy / remove an electron | Ionisation reaches the continuum, not just the next rung |
| $1\ \mathrm{eV}=1.602176634\times10^{-19}\ \mathrm J$ | Electronvolt, a unit of energy | Convert eV to J before using $h$ in J s |
| $n=1,2,3,\ldots$; $Z$ | Principal quantum number; proton number | $n$ labels a level, not how many electrons there are |

## The atom first: what is changing?

A nucleus contains $Z$ protons and $N$ neutrons, surrounded by electrons. Nuclear notation ${}^{A}_{Z}X$ gives $A=Z+N$. The proton number identifies the **element**; the neutron number distinguishes its **isotopes**. Nearly all the mass is in the nucleus. A neutral atom has $Z$ electrons; changing the electron count makes an **ion**, not a different element. Electron arrangement controls much of its chemistry.

In an ordinary atomic line, the electron system changes state while the nucleus retains its internal state. Hydrogen is especially clean: one proton and one electron. Hydrogen-like ions such as $\mathrm{He}^+$ also have just one electron, but a stronger nuclear charge. Neutral helium, with two electrons, is a different problem.

| System changing state | Typical energy scale | Example |
|---|---|---|
| Atomic electron system | eV for many outer-electron transitions | Visible/UV atomic lines; inner-shell transitions can produce X-rays |
| Molecule's rotation or vibration | Often smaller gaps | Microwave or infrared spectra |
| Nucleus | Often keV–MeV | Gamma emission from an excited nucleus |

**All three are quantum systems.** “Quantum” names the rules; “atomic” or “nuclear” names the system. X-rays and gamma rays are distinguished by origin, not by an absolute energy boundary. A gamma transition need not change the element either: the nucleus can lose excitation energy while keeping the same $A$ and $Z$.

## Why discrete levels appear

A guitar string does not accept every stationary-wave shape. Its boundary conditions select the modes that fit. [[Stationary Waves]] gives the mechanical version; [[Wave-Particle Duality]] supplies the new ingredient, an electron's wavelength $\lambda=h/p$.

For an atom, the allowed electron waves must also be self-consistent. Solving the quantum wave equation with the attraction to the nucleus and the correct boundary conditions selects a set of bound-state energies. Quantisation is not a machine rounding a continuous energy to the nearest allowed value; it is a restriction on which stationary states exist.

**A useful historical model, with an honest boundary.** Bohr's hydrogen model puts an electron in a circular orbit, permits only selected orbits, and postulates that these stationary orbits do not radiate. The later de Broglie picture makes the selection tangible: a wave fitted around a loop must join back onto itself,

$$2\pi r=n\lambda=\frac{nh}{mv}\quad\Longrightarrow\quad mvr=n\hbar,\qquad \hbar=\frac{h}{2\pi}.$$

An incomplete number of wavelengths returns with the wrong phase. This is a bridge to quantisation, **not a literal photograph of an electron orbit**. Modern stationary states are wavefunctions, not miniature planets on tracks. A classical orbiting charge would radiate and spiral inward; Bohr's no-radiation postulate was an additional rule, not a consequence of classical mechanics.

### Deriving hydrogen's energy ladder

**Trigger: one electron held by an inverse-square attraction. Tool: Coulomb's force supplies the centripetal acceleration.** Let $k=1/(4\pi\varepsilon_0)$, let $m$ be the electron mass, and initially take the nucleus as fixed:

$$\frac{kZe^2}{r^2}=\frac{mv^2}{r}\quad\Longrightarrow\quad K=\frac12mv^2=\frac{kZe^2}{2r}.$$

**Tool: potential energy measured from infinite separation.** The attractive force has potential energy $U=-kZe^2/r$. Its slope gives the force: $-dU/dr=-kZe^2/r^2$. Therefore

$$E=K+U=\frac{kZe^2}{2r}-\frac{kZe^2}{r}=-\frac{kZe^2}{2r}.$$

**Trigger: only wave patterns that close are allowed. Tool: $mvr=n\hbar$.** Substitute $v=n\hbar/(mr)$ into the force equation:

$$r_n=\frac{n^2\hbar^2}{mkZe^2}=\frac{n^2}{Z}a_0,\qquad a_0\approx5.29\times10^{-11}\ \mathrm m,$$

$$\boxed{E_n=-\frac{mk^2Z^2e^4}{2\hbar^2n^2}\approx-\frac{13.6Z^2}{n^2}\ \mathrm{eV}.}$$

For hydrogen, $Z=1$: $E_1=-13.6$, $E_2=-3.40$, $E_3=-1.51$, $E_4=-0.850$ eV. The rungs crowd together as $n$ grows; they approach zero from below. They are **not equally spaced**. For a one-electron $\mathrm{He}^+$ ion, $Z=2$ makes the corresponding gaps four times larger, and their photon wavelengths four times shorter.

The modern hydrogen calculation recovers this leading energy formula without literal orbits. Finite nuclear mass introduces the reduced mass in place of $m$; relativity and other interactions split and shift the lines further. Do not apply $-13.6/n^2$ to an arbitrary many-electron atom. [The quantum hydrogen solution](https://farside.ph.utexas.edu/teaching/qm/Quantum/node44.html) distinguishes its bound ladder from the unbound continuum.

![[energy-levels-hydrogen.svg|720]]

*Both vertical axes are energy scales. The right panel enlarges the crowded excited levels; it is not a drawing of electron positions.*

### Why negative energy is useful

Set $E=0$ for an electron and nucleus separated infinitely far with no relative kinetic energy. A bound atom has less energy than that separated system, hence $E<0$. To ionise ground-state hydrogen requires $0-(-13.6)=13.6$ eV; to ionise it from $n=2$ requires only $3.40$ eV. This positive removal cost is the electron's **binding energy** in that state.

Above the ionisation threshold, the electron can carry a continuous range of kinetic energies. Neglecting recoil, an absorbed $15.0$ eV photon ionising ground-state hydrogen leaves $15.0-13.6=1.4$ eV of electron kinetic energy. **Discrete bound levels do not mean every possible atomic absorption is a line:** bound-to-free absorption has a threshold and a continuum.

## How the lines are made

![[energy-levels-see-it-jump.mp4]]

Watch three hydrogen transitions and compare a direct drop with a cascade. The dot marks energy, not an electron's position; ultraviolet photon colours are symbolic.

### Emission: read the energy leaving

An electric discharge or collisions can excite atoms. When an excited atom makes a radiative transition downwards, it emits a photon whose energy equals the lost atomic energy. A low-density excited gas therefore gives narrow **bright lines** against a weak background. Pass that light through a prism or a [[Diffraction|diffraction grating]] and its frequencies separate spatially.

The evidence runs forwards: definite frequencies $\rightarrow$ definite photon energies $hf$ $\rightarrow$ definite differences between atomic energy states. Together with the atomic model, the observed pattern supports discrete levels. Merely saying “electrons are excited” does not explain why there are lines instead of every colour.

### Absorption: read the energy missing

Put a suitable gas in front of a brighter continuous source. Photons that match upward transitions can be removed from the beam, leaving **dark absorption lines** on a continuous background. The gas must contain atoms in the relevant **lower** states. A ground-state hydrogen atom can absorb a Lyman photon to reach $n=2$; absorbing a Balmer photon requires an atom already in $n=2$.

The same pair of levels sets the same frequency in both directions. This does **not** guarantee that every emission line appears as an equally deep absorption line: level populations, transition probabilities, temperature and viewing geometry matter. After absorption, light can be re-emitted in other directions or through a cascade; the forward beam still loses photons at the original frequency. In a stellar atmosphere, the cooler overlying material and the temperature gradient make those deficits visible. [NASA's spectroscopy explanation](https://science.nasa.gov/mission/webb/science-overview/science-explainers/spectroscopy-101-how-absorption-and-emission-spectra-work/) shows the observing geometry.

![[energy-levels-spectra.svg|720]]

*Illustrative Balmer spectra: shared line centres, invented strengths and widths. The absorption panel assumes a population in $n=2$. These are teaching curves, not a measured stellar spectrum.*

### Photons must match; colliding electrons can keep change

For a bound-to-bound **single-photon** absorption, the photon energy must match a permitted gap within the line width. A $10.0$ eV photon cannot supply hydrogen's $10.2$ eV ground-to-first-excited gap. An $11.0$ eV photon cannot pay $10.2$ eV and retain $0.8$ eV as the same absorbed photon: the single-photon event absorbs it whole, and no bound level matches that energy.

A **colliding electron** is different. It can give the atom $10.2$ eV and depart with remaining kinetic energy. This explains why a discharge excites a gas even though its incoming electrons have a range of energies. Photons above the ionisation threshold are different again: the freed electron can carry the excess. Multi-photon processes exist at high light intensities; they are beyond this single-photon model.

## Hydrogen's series: many lines, one destination

For emission from $n_u$ to $n_l<n_u$,

$$\frac{hc}{\lambda}=13.6\left(\frac1{n_l^2}-\frac1{n_u^2}\right)\mathrm{eV}.$$

After converting the energy unit, this becomes the **Rydberg form**

$$\frac1\lambda=R_{\mathrm H}\left(\frac1{n_l^2}-\frac1{n_u^2}\right),\qquad R_{\mathrm H}\approx1.097\times10^7\ \mathrm{m^{-1}}.$$

| Series | Common lower level | Where the lines lie |
|---|---|---|
| Lyman | $n_l=1$ | Ultraviolet; $2\to1$ about $121.6$ nm |
| Balmer | $n_l=2$ | First lines visible: $3\to2$ about $656$ nm, $4\to2$ about $486$ nm; higher members extend into UV |
| Paschen | $n_l=3$ | Infrared |

**Why a series converges:** for fixed $n_l$, taking $n_u\to\infty$ makes $1/n_u^2\to0$. The photon energy approaches $13.6/n_l^2$ eV. The lines therefore approach a **short-wavelength limit**, about $364.7$ nm for Balmer. That is the ionisation energy from $n=2$ read backwards as a wavelength.

### Cascades: conserve energy, not wavelength or photon count

An atom in $n=3$ may return to $n=1$ directly, or through $n=2$ where allowed. The direct route emits one photon; the cascade emits two:

$$E_3-E_1=(E_3-E_2)+(E_2-E_1).$$

Thus $hf_{31}=hf_{32}+hf_{21}$, and

$$\frac1{\lambda_{31}}=\frac1{\lambda_{32}}+\frac1{\lambda_{21}}.$$

The photon frequency is a **level gap divided by $h$**, not the electron’s orbital revolution frequency. The wavelengths themselves do **not** add. One approximately $102.6$ nm photon carries the same total energy as a $656$ nm photon plus a $121.6$ nm photon. These are alternative paths across an ensemble, not a claim that one atom emits every possible line on each trip down.

![[energy-levels-cascades.svg|720]]

For $N$ distinct levels, there are $N(N-1)/2$ possible downward **pairs**. That is the maximum number of distinct lines if every pair can radiate, its upper level is populated, and all gaps differ. Equal gaps merge into one frequency; selection rules can suppress transitions. For a stated initial level, list reachable routes before counting.

## Worked Examples — real questions, tools and triggers

### 1. Reconstruct the invisible ladder — Cambridge 9702/42/O/N/25 Q8 [10]

**Given, paraphrased:** the three lowest-frequency lines ending at the ground state have frequencies $2.47$, $2.92$ and $3.09\times10^{15}$ Hz. The ground state is $-13.6$ eV. Explain the evidence for discrete levels and reconstruct the first four energies.

**(a) Trigger: explain a pattern, not calculate a number. Tool: photon energy conservation.** A downward transition emits a photon. Its energy $hf$ equals the difference between the two levels. The discrete frequencies therefore reveal discrete energy differences, supporting discrete atomic levels. The scheme awards three points from this explanatory chain. [3]

**(b)(i) Trigger: the required unit is J. Tool: the electronvolt conversion.**

$$E_1=(-13.6)(1.60\times10^{-19})=-2.18\times10^{-18}\ \mathrm J.\qquad[1]$$

**(ii) Trigger: all arrows end at the same level. Tool: smallest frequency = smallest upward gap from that level.** The $2.47\times10^{15}$ Hz line is $n=2\to1$:

$$E_2-E_1=hf=\frac{(6.63\times10^{-34})(2.47\times10^{15})}{1.60\times10^{-19}}=10.2\ \mathrm{eV}.\qquad[2]$$

**(iii) Tool: recover an absolute level by adding its gap to the known ground level.** $E_n=E_1+hf_{n1}$, never $E_n=hf_{n1}$.

| Level | Gap above ground / eV | Energy / eV |
|---|---:|---:|
| 1 | 0.0 | −13.6 |
| 2 | 10.2 | −3.4 |
| 3 | 12.1 | −1.5 |
| 4 | 12.8 | −0.8 |

These are the scheme's rounded values. [4] Use the **supplied frequencies and constants**; the reconstructed $n=4$ value is not the ideal-model value $-13.6/16=-0.850$ eV. Do not silently replace measurements supplied in a question with the theoretical ladder.

**Check:** each excited level is above $-13.6$ eV but below zero. A positive value would describe an unbound state, contradicting the given bound-level interpretation.

### 2. The longest photon — IB Physics HL, November 2025 TZ3, Paper 2 Q1 [4]

**Given, paraphrased:** three levels at $-13.6$, $-3.40$ and $-1.51$ eV. Count the downward transitions and find the largest emitted wavelength.

**(a) Trigger: three displayed levels. Tool: enumerate pairs.** $3\to2$, $3\to1$, $2\to1$: **three**. [1] One initially excited atom need not emit all three photons.

**(b) Trigger: “largest wavelength”. Tool: $\lambda=hc/\Delta E$ is an inverse relationship.** Choose the **smallest** gap, $(-1.51)-(-3.40)=1.89$ eV:

$$\lambda=\frac{hc}{\Delta E}\approx\frac{1240\ \mathrm{eV\,nm}}{1.89\ \mathrm{eV}}=656\ \mathrm{nm}.\qquad[3]$$

The scheme also accepts $658$ nm using the rounded J-based constants. The physics is the selected gap, the positive energy difference and the consistent units—not extra decimal places.

### 3. Absorbing energy, slowing down — AP Physics 2, 2022 FRQ 3(a–c), (d)(iii)

**Given, paraphrased:** use a circular-orbit model for hydrogen, then compare the atom before and after absorbing a photon that increases the orbital radius.

**(a) Trigger: attraction supplies circular motion. Tool: Coulomb + Newton.**

$$\frac{ke^2}{r^2}=\frac{mv^2}{r}\quad\Longrightarrow\quad v=\sqrt{\frac{ke^2}{mr}}.\qquad[2]$$

**(b) Trigger: “total”, not kinetic, energy. Tool: sum the two stores.**

$$U=-\frac{ke^2}{r},\qquad K=\frac{ke^2}{2r},\qquad E=K+U=-\frac{ke^2}{2r}.\qquad[3]$$

**(c) Tool: read the sign before the magnitude.** As $r$ increases, $-ke^2/(2r)$ becomes **less negative**, so the atom's energy increases, consistent with absorption. [2] At the same time, $v$ and $K$ decrease. The supplied energy raises $U$ by more than the fall in $K$.

**(d)(iii) Trigger: translate equations into bars. Tool: preserve the signs and compare magnitudes.** Draw a negative $U$ bar closer to zero and a smaller positive $K$ bar. [2] A consistent circular-orbit sketch retains $U=-2K$. The paper's other part (d) calculations concern photon energy and mass–energy; those are not needed for this comparison.

## Where it is the working tool

### The quantum physics in an LED bulb

A blue LED turns electrical energy into light through **transitions between allowed electronic energies**. In a solid, neighbouring atoms interact and their levels form **bands** of closely spaced states, separated by forbidden energy gaps. The isolated hydrogen ladder does not describe an LED, but the rule $E_\gamma=\Delta E$ still does.

A forward current supplies electrons and **holes**—unoccupied electron states—in the emitting region. An electron can fall into a lower-energy empty state, releasing a photon: **electron–hole recombination**. The photon energy is approximately the active material's band gap $E_g$:

$$E_\gamma\approx E_g,\qquad \lambda\approx\frac{hc}{E_g}.$$

Blue LEDs commonly use an **indium gallium nitride (InGaN)** emitting region; its composition helps set the gap and hence the colour. Making an efficient device also requires controlling defects and keeping electrons and holes together in that region. [Nakamura's Nobel lecture](https://www.nobelprize.org/uploads/2018/06/nakamura-lecture.pdf) explains the working structure.

**Tool and trigger:** specified colour → wavelength → photon energy, using $hc\approx1240\ \text{eV nm}$.

| Example light | Wavelength | Energy per photon |
|---|---|---|
| Red | $650$ nm | $1240/650\approx1.91$ eV |
| Blue | $450$ nm | $1240/450\approx2.76$ eV |

Blue requires a larger energy drop per photon. Turning up the current mainly increases the photon rate; it does not turn a red LED blue. These are representative wavelengths, and a real LED emits a range around its peak. Photon energy alone does not determine perceived brightness.

**Then how does a blue chip light a room white?** Many household LED bulbs put a **phosphor** over a blue LED. It absorbs some blue photons and emits a broader spread of longer-wavelength light; some energy becomes heat. That light mixes with the remaining blue to appear white. There is no single “white wavelength”. Other designs mix several coloured LEDs. The [US Department of Energy's LED guide](https://www.energy.gov/cmei/ssl/led-basics) explains these approaches; its [lighting research overview](https://www.energy.gov/sites/default/files/2022-02/ssl-rd22_hariyani_next-gen.pdf) shows the blue InGaN chip and phosphor combination.

The bulb over a desk is an everyday application of the same energy-gap bookkeeping used to read a star's spectrum. The material changes; energy conservation does not.

### Reading a star's chemistry

Record the intensity versus wavelength, calibrate the wavelength axis with a known lamp, and compare several line positions against laboratory data. A matching pattern identifies an element/ion in the emitting or absorbing material. The lines principally probe the material that produced them—often a stellar atmosphere—not a direct sample of the core. A shared shift in the pattern can reveal motion via [[Doppler Effect]]; strengths and widths also depend on temperature, population, density and instrument response. One missing or strong line alone is not a direct abundance measurement.

The four familiar visible Balmer lines are near $656.3$, $486.1$, $434.0$ and $410.2$ nm in air. The [NIST hydrogen table](https://physics.nist.gov/PhysRefData/Handbook/Tables/hydrogentable2.htm) resolves fine-structure components; these rounded centres are appropriate for a school spectrometer. The simple $13.6$ eV model predicts **vacuum** wavelengths, so do not mistake a small model/air difference for a redshift. The repeatable line pattern is why spectroscopy can identify material without touching it.

### A second is an energy gap counted repeatedly

An atomic clock locks an oscillator to an atomic transition. The caesium-133 transition used to define the second has frequency **9 192 631 770 Hz**: a microwave gap, about $3.80\times10^{-5}$ eV. It is a **hyperfine transition within the electronic ground state**, involving the coupling of nuclear and electronic angular momenta—not a gamma transition between excited nuclear states. This is a particularly useful boundary case for “atomic versus nuclear”: the nucleus influences the atomic levels without undergoing nuclear decay. [NIST's clock explanation](https://www.nist.gov/how-do-you-measure-it/how-do-you-measure-second/) describes the resonance measurement.

### A laser makes one transition amplify light

Spontaneous emission starts without an incident photon selecting its timing and mode. **Stimulated emission** occurs when radiation drives an excited atom down and adds light to the same radiation mode. Pumping a suitable medium creates a **population inversion** on a laser transition, so stimulated emission can outweigh absorption; feedback and gain select and amplify modes. A glowing discharge is not automatically a laser. The [Nobel laser explainer](https://educationalgames.nobelprize.org/educational/physics/laser/facts/index.html) traces the mechanism. Molecular and semiconductor lasers use different level structures, but the energy-gap bookkeeping survives.

## Hands-on — predict the spectrum, then change the atom

Run the companion script from this folder:

```bash
python3 energy-levels-spectra.py --upper 3 --lower 2
python3 energy-levels-spectra.py --upper 4 --lower 2
python3 energy-levels-spectra.py --upper 3 --lower 2 --charge 2
```

Before each run, predict which way the wavelength moves. The first two change the starting level; the third changes hydrogen into a **one-electron ion**, not neutral helium. The script prints the gap, frequency and vacuum wavelength, lists the possible downward pairs, and checks energy conservation across every descending route from the chosen upper level to the ground state. The route enumeration ignores selection rules; it makes no prediction about relative brightness.

**Try to break the interpretation:** compare the number of available lines with the number of photons along one route. Try adding the wavelengths along a cascade, then add their reciprocals. Explain why only one sum matches the direct transition.

**With a school spectrometer:** observe a teacher-operated low-pressure discharge lamp through a grating; compare several lines with the tabulated pattern. Compare with a broadband lamp. Do not use the Sun or look into a laser. A spectrometer's finite resolution makes each measured line a peak with width, not an infinitely thin ruler mark.

## Common Misconceptions

1. **“The level is −3.4 eV, so the photon has −3.4 eV.”** Specify the other level, subtract upper minus lower, and keep $E_\gamma>0$. A level value alone does not identify a transition.
2. **“The bigger drop gives the longer wavelength.”** A bigger drop gives a more energetic photon; $\lambda=hc/E_\gamma$ therefore gets smaller.
3. **“More absorbed energy means a faster electron.”** Compare $K$, $U$ and $E$ separately. In the Bohr model, the excited electron moves more slowly at a larger radius.
4. **“A hot gas emits every line equally; a cool gas absorbs them all.”** Ask which lower/upper states are populated and which transitions are allowed. Frequency positions and line strengths answer different questions.
5. **“Three levels means each atom emits three photons.”** Draw one descending path. Three is the number of possible pairs in the simple model; one path has at most two downward steps.
6. **“All spectra follow −13.6/n², and all radiation comes from the nucleus.”** Identify the system: hydrogen-like electron, many-electron atom, molecule or nucleus. Only the first has that simple hydrogenic ladder.

## Beyond the syllabus — what a thin line hides

Recall that a gap tells us the **possible photon energy**, not the probability of emission. The transition probability depends on how the initial and final wavefunctions couple to radiation. Symmetry produces **selection rules**: for the common electric-dipole transitions of hydrogen, $\Delta\ell=\pm1$, where $\ell$ labels orbital angular momentum. Some energetically possible lines are therefore weak or absent. “Forbidden” means forbidden for a specified mechanism, not impossible by every mechanism. [Fitzpatrick's derivation](https://farside.ph.utexas.edu/teaching/qmech/lectures/node121.html) develops the rule.

Real lines have widths. Finite lifetimes give natural broadening; moving atoms give Doppler broadening; collisions and surrounding fields can broaden or shift levels. A spectrometer contributes its own response. Resolving line widths and splittings reveals more than naming the element—temperature, fields and interactions leave measurable signatures. [NIST's line-shape reference](https://physics.nist.gov/Pubs/AtSpec/node20.html) explains the dominant broadening mechanisms.

In solids, interacting atoms produce **bands** containing huge numbers of closely spaced states; in molecules, rotational and vibrational structure produces bands of lines. Neither invalidates quantum mechanics. The isolated hydrogen ladder is a tractable example of its rules, not a template that every material must resemble.

## Exam Notes

### Cambridge 9702 AS & A Level Physics

**A Level §22.4, all three objectives:** discrete electron levels in isolated atoms; appearance and formation of emission/absorption line spectra; $hf=E_1-E_2$. The labels in Cambridge's formula mean the higher energy minus the lower energy: do not import an arbitrary “final minus initial” sign convention. Explain the photon → gap → discrete-frequency chain; read level diagrams, select a gap and convert eV/J. Q8 above is the real Paper 4 reconstruction format.

The 2028–30 syllabus is the canonical version; this topic is unchanged from 2025–27. It is **A2 content, not AS Paper 1/2 content**. Bohr's full derivation and the named hydrogen series go beyond the three listed §22.4 objectives. Stellar line shifts also appear in §25.3, but the redshift/distance treatment is separate.

**Formula provision:** the inspected Paper 4 supplies $h,c,e$ and the electric potential-energy formula. It does **not** print $hf=\Delta E$ or $E=hf$ in the formula list; recall those. Hydrogen's $-13.6/n^2$ formula is not a required §22.4 recall rule. Use the question's energies/frequencies when supplied.

### IB Physics — first assessment 2025

**E.1, SL and HL:** discrete levels, photon emission/absorption, $E=hf$, and chemical identification from spectra. **Additional HL:** the Bohr hydrogen ladder $E_n=-13.6/n^2$ eV and quantised angular momentum $mvr=nh/(2\pi)$. These correspond to the topic map's E.1.2 and E.1.4 rows. The booklet prints $E=hf$ and both HL formulae; interpret them rather than memorising the page.

The November 2025 Q1 above checks transition counting and the inverse wavelength–gap relationship. Composition from absorption lines also supports the stellar-properties strand of E.5; this does not by itself cover stellar temperatures, radii or evolution. Nuclear gamma/alpha energy evidence is a separate E.3 topic.

### AP Physics 2

**Topics 15.2 and 15.3:** atomic structure, the historical Bohr model, integer de Broglie wavelengths around an orbit, transitions, spectra as identifiers, and ionisation/binding energy. The current course limits energy-level diagrams to **single-electron atoms** and does not require orbitals, orbital shapes or probability functions. The 2022 FRQ is from the earlier course framework but tests the retained circular-model and energy reasoning.

The 2025 equation sheet prints $E=hf$, $\lambda=c/f$, Coulomb's law and electric potential energy. It does **not** print the Bohr $-13.6/n^2$ or angular-momentum quantisation formulae. Learn the standing-wave reasoning; do not assume every formula in the IB booklet appears on the AP sheet.

### Where this is not examined

The quantum explanation and atomic-line calculations are **not listed in Cambridge 0625 IGCSE Physics, AP Physics 1, AP Physics C: Mechanics, or AP Physics C: Electricity and Magnetism** in the inspected syllabi/CEDs. 0625 covers spectra as electromagnetic wavelength ranges and covers the nuclear atom/radiation; those are not §22.4-style atomic-transition calculations. Likewise, chemistry's electron shells and ionisation energies are related concepts, not automatic evidence of a line-spectra requirement on a physics board.

## Connections

- **Imaging application:** [[X-rays and CT]] — electron acceleration, photon energies and attenuation become an internal image.

- **Parents:** [[Wave-Particle Duality]] supplies photons and de Broglie waves; [[Stationary Waves]] supplies the boundary-condition intuition; [[Circular Motion]] supplies the force-to-orbit calculation.
- **Measurement:** [[Diffraction]] — gratings separate wavelengths so the transitions can be measured.
- **Next systems:** [[Nuclear Physics]] — energy changes in the nucleus; [[Pauli Exclusion Principle]] — the occupancy rules that complicate many-electron atoms; [[Quantum Tunnelling]] — what bound-state wavefunctions do outside a classical allowed region.
- **Applications:** [[Doppler Effect]] — use a shifted pattern to infer motion; [[The Feynman Technique]] — explain why the atom can gain energy while its electron slows down.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $E_\gamma=hf$ | `E_\gamma=hf` | Photon energy |
| $E_u-E_l$ | `E_u-E_l` | Positive level gap |
| $\lambda=hc/\Delta E$ | `\lambda=hc/\Delta E` | Vacuum wavelength from gap |
| $\hbar=h/(2\pi)$ | `\hbar=h/(2\pi)` | Reduced Planck constant |
| $mvr=n\hbar$ | `mvr=n\hbar` | Bohr angular-momentum rule |
| $E_n=-13.6Z^2/n^2\ \mathrm{eV}$ | `E_n=-13.6Z^2/n^2\ \mathrm{eV}` | Approximate hydrogenic ladder |
| ${}^{A}_{Z}X$ | `{}^{A}_{Z}X` | Nuclear notation: mass and proton numbers |
