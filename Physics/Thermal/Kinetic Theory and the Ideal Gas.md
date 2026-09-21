---
chinese: 气体动理论与理想气体 (qìtǐ dònglǐlùn yǔ lǐxiǎng qìtǐ)
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Linear Momentum]]"
  - "[[Work, Energy and Power]]"
  - "[[Vectors in Physics]]"
  - "[[Density and Pressure]]"
leads_to:
  - "[[Temperature and Thermometry]]"
  - "[[Internal Energy]]"
  - "[[First Law of Thermodynamics]]"
  - "[[Specific Heat Capacity]]"
  - "[[Entropy and the Second Law]]"
  - "[[Stellar Evolution]]"
  - "[[Thermal Expansion]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/thermal-physics
  - level/A-Level
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/A-Level
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/0625-2-1
  - syllabus/9702-14-2
  - syllabus/9702-15-1
  - syllabus/9702-15-2
  - syllabus/9702-15-3
  - type/derivation
  - type/definition
  - notation/langle-c-squared-rangle
  - notation/k-boltzmann
  - misconception/temperature-is-heat
  - misconception/heavy-molecules-faster
  - misconception/gas-molecules-same-speed
  - misconception/pressure-is-intermolecular
  - misconception/absolute-zero-reachable
---

# Kinetic Theory and the Ideal Gas 气体动理论与理想气体

> *Push the plunger of a sealed syringe full of air and it pushes back. Fill it with water and it barely moves. The difference is mostly empty space: gas molecules have room to come closer; liquid molecules are already close. Follow those invisible particles and pressure, temperature and the gas laws become consequences of motion — with the same constant $k$ carved on [[Stories/Boltzmann's Tombstone|Boltzmann's gravestone]].*

## Definition

An **ideal gas** is a gas that obeys the **equation of state**

$$pV = nRT = NkT$$

exactly, where $p$ is pressure, $V$ volume, $T$ the **absolute** (Kelvin) temperature, $n$ the number of **moles**, $N$ the number of **molecules**, $R = 8.31\,\text{J mol}^{-1}\text{K}^{-1}$ the **molar gas constant**, and $k = 1.38 \times 10^{-23}\,\text{J K}^{-1}$ the **Boltzmann constant**. **Kinetic theory** is the microscopic model — molecules as tiny, fast, randomly-moving particles — that *derives* this macroscopic law and, in doing so, reveals what temperature actually is.

### 中文锚点

把不带针头的注射器抽满空气，用手指堵住出口，再慢慢推活塞，你会感觉它越来越顶手；如果里面装满水、没有气泡，活塞就几乎推不动了。空气里的分子隔得很远，挤一挤，主要是把它们之间的空隙变小，并不是把分子压扁。空间越小，分子撞上活塞就越频繁，你的手便要更用力，才能顶住这些细小撞击合起来的推力。水里的分子本来就挨得很近，留给你压缩的余地很少。

## Start with matter you can hold

A **particle model** explains a material's large-scale behaviour using its small constituents: atoms, molecules, ions and electrons. Which constituents matter depends on the material — a salt crystal is not a pile of salt molecules, and a metal contains mobile electrons as well as ions. The simple dots below stand for constituent particles, not tiny copies of the whole object.

![[particle-model-states.svg|760]]

| State | Arrangement, separation and motion | What you can observe — and why |
|---|---|---|
| **Solid** | Close particles; in a crystal, a regular arrangement. They vibrate about fixed positions. | Fixed shape and approximately fixed volume: strong interactions resist changing neighbours and spacing. Non-crystalline solids need not have regular order. |
| **Liquid** | Close particles, irregular arrangement; particles move past one another. | Approximately fixed volume but takes the container's shape: neighbours can rearrange without becoming widely separated. |
| **Gas** | Widely separated particles, no fixed arrangement; rapid random motion between collisions. | No fixed shape or volume: particles spread through the available space. Large gaps make compression easy. |

**Why not squeeze water like air?** With a needle-free syringe, seal the outlet and gently press the plunger. Air compresses readily because the particles can come closer together. Water with no trapped air compresses very little: its particles are already close, and forcing them closer encounters strong resistance. Liquids and solids are *slightly* compressible; “incompressible” is a useful approximation. **Particles do not shrink when the sample is compressed.**

**Changing state changes the arrangement.** Solid → liquid is **melting**; liquid → solid is **freezing**; liquid → gas is **vaporisation** (evaporation at a surface, or boiling throughout a liquid); gas → liquid is **condensation**. Ice melting does not turn individual water molecules into “liquid molecules”: the same molecules can now rearrange. Energy supplied during melting or boiling changes the interactions and separation rather than simply increasing temperature; see [[Internal Energy]] and [[Specific Heat Capacity]].

## Brownian motion — watching the invisible through what it hits

Under a microscope, tiny suspended smoke particles in still air or fine particles in water jiggle irregularly. This is **Brownian motion**. The visible speck is a microscopic particle containing many atoms or molecules; it is **not** an individual air or water molecule.

Much smaller, light, fast-moving molecules strike the speck from all sides. In a short interval their impacts do not balance exactly: one side happens to get the larger total impulse, so the speck changes its velocity. A moment later the imbalance points elsewhere. The resulting jitter is evidence that the surrounding molecules are continually moving even when the fluid has no bulk flow.

**Observation → inference:** a wandering speck is visible; the molecular collisions that cause it are inferred. Do not label the speck's traced path “the path of a molecule.” A whole cloud drifting one way because of a current is bulk flow, not by itself evidence of Brownian motion. See [[Stories/Boltzmann's Tombstone]] for why this distinction helped settle the argument about atoms.

![[particle-model-motion.mp4]]

Follow the same 24 dots through a solid, a liquid and a gas; then watch compression reduce spacing without changing dot size. The final scene separates the large amber speck from the much smaller teal molecules delivering kicks. This is a teaching schematic: phase rearrangements, compression and collision timing are illustrative, and particle sizes are greatly exaggerated. The compression comparison holds temperature fixed; it does not simulate the warming of a rapidly compressed gas.

## Pressure and temperature — the particle explanation first

**A collision delivers a push.** A gas particle approaching a wall reverses its normal velocity component when it rebounds. Its momentum changes, so the wall must exert a force on it. The particle exerts an equal and opposite force on the wall. Many impacts produce an average force; **pressure is that normal force per unit area**, $p=F/A$.

- **Heat a fixed mass at constant volume:** mean particle kinetic energy increases. Faster particles strike the wall more often and transfer more momentum per collision on average. Both changes raise pressure.
- **Compress a fixed mass at constant temperature:** the average kinetic energy and speed distribution stay the same. Shorter trips across the container mean more frequent impacts per unit area, so pressure rises. It is the spacing, not the molecular size, that changes.
- **Heat a gas at constant pressure:** it must expand to offset the stronger bombardment. A freely moving piston provides this situation; a rigid sealed can does not.

Temperature tracks the energy associated with random particle motion. **Absolute zero**, $0\,\mathrm K=-273.15\,^\circ\mathrm C$, is the lower limit of temperature: particles have their least possible energy, not a universal promise that all quantum motion stops. The school particle picture says hotter particles move more vigorously. The precise classical ideal-gas relation between temperature and mean *translational* kinetic energy is derived below.

Convert using $T/\mathrm K=\theta/^\circ\mathrm C+273.15$ (usually rounded to **+273** at IGCSE). Thus $27\,^\circ\mathrm C\approx300\,\mathrm K$. Doubling from $300\,\mathrm K$ to $600\,\mathrm K$ doubles ideal-gas pressure at fixed volume; doubling the Celsius number does not. A kelvin is the same size interval as a Celsius degree, but the zero is different — see [[Temperature and Thermometry]].

## The empirical story first — three gas laws and one equation

Long before anyone believed in molecules, experimenters found three regularities in how a fixed amount of gas behaves:

- **Boyle's law** (1662): at constant $T$, $\;p \propto \dfrac{1}{V}$ — squeeze a gas and the pressure rises.
- **Charles's law** (1787): at constant $p$, $\;V \propto T$ — heat a gas and it expands.
- **Gay-Lussac's law**: at constant $V$, $\;p \propto T$ — heat a sealed gas and the pressure climbs.

Stitch the three together and you get the **combined gas law** $\dfrac{pV}{T} = \text{const}$, and fixing the constant per mole gives the **ideal gas equation** $pV = nRT$. This is the *macroscopic* truth: measured with a pressure gauge, a ruler, and a thermometer, knowing nothing about what a gas is made of.

The triumph of kinetic theory is that it **derives this same equation from the picture of molecules as bouncing balls** — and tells you what the thermometer was secretly measuring all along.

## What "ideal" means — the assumptions

The model is a deliberate idealisation. A gas is **ideal** when:

1. The gas contains a **large number** $N$ of identical molecules in **continuous, random motion** (random directions, a spread of speeds).
2. Molecules are **points** — their own volume is negligible compared with the volume of the container.
3. **No intermolecular forces** except during collisions — molecules don't attract or repel at a distance, so between collisions they travel in straight lines at constant velocity (Newton's first law).
4. Collisions (with the walls and with each other) are **perfectly elastic** and take **negligible time** compared with the time between collisions.
5. **Newtonian mechanics applies** to every collision.

Real gases obey this best when they are **dilute and hot** — low pressure (molecules far apart, so their own size and mutual forces don't matter) and well above their boiling point (fast enough that the weak attractions are irrelevant). The honest limits are in the beyond-syllabus section.

## See it move — a molecular-dynamics simulation

![[kinetic-theory-gas-simulation.mp4]]

A **two-dimensional hard-disc simulation**: elastic collisions, wall-impact flashes and a speed histogram. The momentum arrow illustrates the difference between rapid random motion and a small bulk drift; finite samples fluctuate rather than cancelling exactly. Heating raises the speed scale and broadens the histogram. The two-dimensional distribution is not the three-dimensional Maxwell–Boltzmann curve below; the simulation illustrates collisions and averaging, not a literal three-dimensional gas.

## The derivation — pressure from molecular chaos

![[kinetic-theory-box-derivation.svg|697]]

The central task is getting a macroscopic pressure out of microscopic collisions, using only momentum. Put $N$ molecules, each of mass $m$, in a cubical box of side $L$ (so volume $V = L^3$).

**One molecule, one wall.** Take a single molecule and look only at the $x$-component of its velocity, $c_x$. When it strikes the right-hand wall it bounces back elastically, so its $x$-momentum reverses from $+mc_x$ to $-mc_x$. The momentum *given to the wall* in that one collision is

$$\Delta p_{\text{coll}} = mc_x - (-mc_x) = 2mc_x.$$

**How often?** Between successive hits on that *same* wall the molecule must travel across the box and back, a distance $2L$, at speed $c_x$. So the time between collisions is $\Delta t = \dfrac{2L}{c_x}$.

**Average force from one molecule** (Newton's second law as rate of change of momentum — see [[Linear Momentum]]):

$$F_1 = \frac{\Delta p_{\text{coll}}}{\Delta t} = \frac{2mc_x}{2L/c_x} = \frac{mc_x^2}{L}.$$

**Sum over all molecules.** The total force on the wall is the sum of $mc_x^2/L$ over all $N$ molecules. Writing $\langle c_x^2\rangle$ for the *average* of $c_x^2$ across the population,

$$F = \frac{m}{L}\sum c_x^2 = \frac{Nm\langle c_x^2\rangle}{L}.$$

Pressure is force per unit area, and the wall has area $L^2$:

$$p = \frac{F}{L^2} = \frac{Nm\langle c_x^2\rangle}{L^3} = \frac{Nm\langle c_x^2\rangle}{V}.$$

**Use the randomness.** Motion is random, so no direction is special: $\langle c_x^2\rangle = \langle c_y^2\rangle = \langle c_z^2\rangle$. Since a molecule's speed satisfies $c^2 = c_x^2 + c_y^2 + c_z^2$, averaging gives $\langle c^2\rangle = 3\langle c_x^2\rangle$, i.e. $\langle c_x^2\rangle = \tfrac{1}{3}\langle c^2\rangle$. Substituting:

$$\boxed{\,pV = \tfrac{1}{3}Nm\langle c^2\rangle\,}$$

Since gas density is $\rho=Nm/V$, the same result is $p=\tfrac13\rho\langle c^2\rangle$. This is a purely mechanical result — no thermometer has appeared yet. It says pressure is set by how many molecules there are, how heavy they are, and how fast they move (mean-square).

## Ideal-gas temperature measures average translational kinetic energy

Now lay the mechanical result beside the experimental equation of state. We have, from mechanics,

$$pV = \tfrac{1}{3}Nm\langle c^2\rangle,$$

and from experiment (per molecule form, since $n R = N k$),

$$pV = NkT.$$

Two expressions for the same $pV$ must be equal:

$$\tfrac{1}{3}Nm\langle c^2\rangle = NkT \;\;\Longrightarrow\;\; \tfrac{1}{3}m\langle c^2\rangle = kT.$$

Multiply both sides by $\tfrac{3}{2}$ and the left side becomes the average translational kinetic energy of a molecule, $\tfrac{1}{2}m\langle c^2\rangle$:

$$\boxed{\;\langle E_k\rangle = \tfrac{1}{2}m\langle c^2\rangle = \tfrac{3}{2}kT\;}$$

This is one of the most quietly profound equations in physics. **For a classical ideal gas, absolute temperature is, up to the constant $\tfrac{3}{2}k$, nothing but the average translational kinetic energy of one of its molecules.** A thermometer is a (very indirect) molecular speedometer. Consequences:

- **Temperature is *intensive*.** It does not scale with the amount of gas. Divide a gas sample at equilibrium into two identical containers: each half keeps the same temperature, although each contains half the total molecular energy.
- **Absolute zero is a limit.** The classical expression extrapolates to zero translational kinetic energy at $T=0$. Real systems require quantum mechanics at sufficiently low temperature; do not use that extrapolation to claim every particle becomes motionless.
- **Different classical ideal gases at the same temperature have the same mean translational KE.** Hydrogen and xenon at 300 K share this mean energy, so lighter molecules must move faster. Rotational and vibrational energies are separate contributions, when available.
- **Internal energy needs one extra distinction.** For an ideal **monatomic** gas, only the three translational degrees of freedom contribute in this model, so $U=N\langle E_k\rangle=\tfrac32NkT$. Diatomic molecules can also rotate and vibrate; $\tfrac32NkT$ is not their total internal energy in general.

## The two faces of the gas constant — why $k$ is Boltzmann's

The equation of state comes in two equivalent forms:

$$pV = \underbrace{nRT}_{\text{per mole}} = \underbrace{NkT}_{\text{per molecule}}.$$

They are linked by **Avogadro's number** $N_A = 6.02\times10^{23}\,\text{mol}^{-1}$, the number of molecules in one mole. Since $N = nN_A$,

$$nRT = NkT \;\Longrightarrow\; nRT = nN_A kT \;\Longrightarrow\; \boxed{k = \frac{R}{N_A}}.$$

So the **Boltzmann constant is just the gas constant *per molecule*** — you take the per-mole bookkeeping constant $R$ and divide out Avogadro's number to get the per-molecule version. Numerically $k = 8.31 / (6.02\times10^{23}) = 1.38\times10^{-23}\,\text{J K}^{-1}$.

This is the same $k$ that appears in **[[Stories/Boltzmann's Tombstone|Boltzmann's entropy formula]]** $S = k\ln W$ and in the thermal-energy scale $k_B T$ underlying noise in electrical systems (see [[Information Theory]]). It is the universal conversion factor between **temperature and energy** — "how many joules is one kelvin worth, per molecule." Encountering the same $k$ in the pressure of a gas, the entropy of a black hole, and the thermal noise in a wire is not a coincidence: all three are statements about molecules (or microstates) carrying energy $\sim kT$ apiece.

## r.m.s. speed and the spread of speeds

Rearranging $\tfrac{1}{2}m\langle c^2\rangle = \tfrac{3}{2}kT$ for the **root-mean-square speed**:

$$c_{\text{rms}} = \sqrt{\langle c^2\rangle} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M}},$$

where $M = mN_A$ is the **molar mass**. Two readings fall straight out:

- $c_{\text{rms}} \propto \sqrt{T}$ — to *double* the typical molecular speed you must *quadruple* the absolute temperature.
- $c_{\text{rms}} \propto 1/\sqrt{m}$ — at a given temperature, **lighter molecules move faster**. This helps explain why light gases escape planetary atmospheres more readily. Balloon leakage also depends on molecular size and the permeability of the balloon material; speed alone does not determine it.

> [!example] How fast is the air in this room?
> Nitrogen, $M = 0.028\,\text{kg mol}^{-1}$, at $T = 300\,\text{K}$:
> $$c_{\text{rms}} = \sqrt{\frac{3(8.31)(300)}{0.028}} \approx 517\,\text{m s}^{-1}.$$
> The molecules around you are moving at roughly **1.5 times the speed of sound** — which is no accident, since sound *is* a disturbance carried by those same colliding molecules.

### If the air is moving at 517 m/s, why don't we feel a gale?

This is the right question to ask, and it has two answers — the second is the beautiful one.

**The motion is random, so there is no average bulk flow.** Opposing momentum transfers balance *on average*, not molecule for molecule or instant by instant. The tiny fluctuations are precisely what cause Brownian motion. A breeze adds an organised bulk drift of a few metres per second on top of the much faster random motion.

**The impacts still produce pressure.** At $100\,\mathrm{kPa}$, air exerts about $10\,\mathrm N$ on each square centimetre of a surface: $F=pA=(10^5)(10^{-4})$. Pressure acting on different sides largely balances; pressure *differences* produce the noticeable force — a syringe pushing back, suction through a straw, or ears popping as a plane climbs. The absence of wind does not mean the absence of molecular motion or pressure.

**Not all molecules move at $c_{\text{rms}}$.** That is just the speed whose square is the average. The actual speeds are spread out in the **Maxwell–Boltzmann distribution**:

![[kinetic-theory-maxwell-boltzmann.svg|520]]

The distribution is skewed — a hard floor at zero, a long tail toward high speeds — so the three "typical" speeds are slightly different and always in the same order:

$$c_{\text{mp}} \;<\; \bar c \;<\; c_{\text{rms}},$$

the most-probable (peak), the mean, and the root-mean-square. Heating the gas slides the whole curve right and flattens it (the molecules spread over a wider band of speeds). There is a beautiful link to statistics here: each *velocity component* $c_x, c_y, c_z$ is **[[Normal Distribution|normally distributed]]** about zero, and the *speed* $c = \sqrt{c_x^2+c_y^2+c_z^2}$ — the length of a 3-D vector of three independent normals — is exactly what produces the Maxwell–Boltzmann shape.

## Where the model does work — pumps and pressure gauges

A bicycle pump converts your push into gas pressure. Compressing air reduces its volume and raises its pressure; when the pressure exceeds the tyre pressure enough to open the valve, air enters the tyre. A fast stroke also warms the gas: work is transferred to its internal energy, so Boyle's constant-temperature law is not an exact description during that stroke. After cooling, the temperature effect changes again. **A real pump makes both restrictions matter: temperature may change, and molecules leave the cylinder when the valve opens.**

For a sealed syringe compressed slowly enough to exchange heat with the room, fixed amount and nearly fixed temperature are much better approximations. Measure pressure and volume and the prediction is a curve, not a straight line:

![[particle-model-boyle.svg|720]]

On a $p$–$V$ diagram, constant pressure (**isobaric**) is a horizontal line, constant volume (**isochoric**) is a vertical line, and constant temperature (**isothermal**) gives the curved path shown.

Each point has the same product $pV$. Halving $V$ doubles $p$; the $p$–$V$ graph is a **hyperbola**. Neither axis is crossed. At sufficiently high pressure the ideal model fails before zero volume can be approached. Plotting $p$ against $1/V$ instead produces a straight line through the origin for the ideal model.

## Worked Examples

*The examples below are original practice questions, labelled by relevant syllabus topic.*

**Example 1 — Boyle's law from the model (9702 §15.2).** A fixed mass of ideal gas at $1.0\times10^5\,\text{Pa}$ occupies $2.0\times10^{-3}\,\text{m}^3$. It is compressed isothermally to $5.0\times10^{-4}\,\text{m}^3$. Find the new pressure.
*Trigger: fixed amount and constant temperature. Tool: Boyle’s law, $p_1V_1=p_2V_2$.*
$$p_2 = \frac{p_1V_1}{V_2} = \frac{(1.0\times10^5)(2.0\times10^{-3})}{5.0\times10^{-4}} = 4.0\times10^5\,\text{Pa}.$$

**Example 2 — Counting molecules (9702 §15.1–15.2).** How many molecules are in $25\,\text{cm}^3$ of an ideal gas at $1.0\times10^5\,\text{Pa}$ and $300\,\text{K}$?
*Trigger: molecule count rather than mole count. Tool: $pV=NkT$, with $1\,\mathrm{cm^3}=10^{-6}\,\mathrm{m^3}$.*
$$N = \frac{pV}{kT} = \frac{(1.0\times10^5)(25\times10^{-6})}{(1.38\times10^{-23})(300)} \approx 6.0\times10^{20}\ \text{molecules.}$$
(That's about a milli-mole — reassuringly, $6.0\times10^{20}/6.02\times10^{23} \approx 1.0\times10^{-3}\,\text{mol}$.)

**Example 3 — Temperature to speed (9702 §15.3).** Find $c_{\text{rms}}$ for helium ($M = 4.0\times10^{-3}\,\text{kg mol}^{-1}$) at $300\,\text{K}$, and compare with the nitrogen result above.
*Trigger: temperature and molar mass are given. Tool: $c_{\mathrm{rms}}=\sqrt{3RT/M}$, using $M$ in kilograms per mole.*
$$c_{\text{rms}} = \sqrt{\frac{3(8.31)(300)}{4.0\times10^{-3}}} \approx 1370\,\text{m s}^{-1}.$$
Helium is about $\sqrt{28/4} = \sqrt{7} \approx 2.6$ times faster than nitrogen at the same temperature — exactly the $1/\sqrt{m}$ law, since both share the same average KE.

**Example 4 — Average KE is gas-independent (IB B.3, AP-2 §9.1).** What is the average translational kinetic energy of *any* ideal-gas molecule at room temperature, $T = 293\,\text{K}$?
*Trigger: mean translational energy per molecule. Tool: $\langle E_k\rangle=\tfrac32kT$.*
$$\langle E_k\rangle = \tfrac{3}{2}kT = \tfrac{3}{2}(1.38\times10^{-23})(293) \approx 6.1\times10^{-21}\,\text{J}.$$
The same for helium, nitrogen, or uranium hexafluoride — temperature fixes the energy per molecule, not the speed.

## Common Misconceptions

### 1. "Temperature measures heat / total energy"
Temperature is **not an amount of energy** — it is *intensive*. For a classical ideal gas it is proportional to mean translational kinetic energy per molecule. A cup of boiling water and a swimming pool at the same temperature have the same molecular KE, but the pool holds vastly more total thermal energy. Heat (energy transferred) and temperature (energy per molecule) are different quantities; conflating them is the single most common thermal error.

### 2. "Heavier gas molecules move faster"
The opposite. At a given temperature **classical ideal** gases share the same mean translational KE, so $\tfrac{1}{2}m\langle c^2\rangle$ is fixed — which means larger $m$ forces *smaller* $\langle c^2\rangle$. Heavy molecules are **slower** ($c_{\text{rms}}\propto 1/\sqrt m$).

### 3. "All the molecules move at the same speed"
There is a whole **distribution** of speeds (Maxwell–Boltzmann), from near-zero to several times $c_{\text{rms}}$. $c_{\text{rms}}$ is a single representative value, not a universal molecular speed.

### 4. "Gas pressure is molecules pushing on each other"
In the ideal model there are **no intermolecular forces between collisions**; elastic collisions still transfer momentum. The pressure on a container wall comes entirely from molecules **colliding with the wall** and reversing momentum — the derivation above never once used a molecule–molecule force.

### 5. "You can reach absolute zero / molecules truly stop"
The classical translational-energy formula extrapolates to zero at $T=0$, but the **third law of thermodynamics** makes absolute zero unreachable in a finite cooling process, and quantum systems can retain **zero-point motion** in their lowest-energy state. Absolute zero is a limit you approach, not a place you arrive.

## Exam Notes

### Cambridge 0625 (IGCSE Physics) — §2.1
**§2.1.1:** distinguish solid/liquid/gas properties and name melting, freezing, vaporisation and condensation. **§2.1.2:** draw particle arrangements; explain separation, motion, temperature and absolute zero; explain gas pressure and Brownian motion. Supplement adds the role of particle forces/distances and the distinction between the visible microscopic speck and the light, fast-moving molecules that hit it. Pressure explanations must reach **force per unit area**.

**§2.1.3 Core:** explain pressure changes for a fixed mass when temperature changes at constant volume, or volume changes at constant temperature. Convert with $T/\mathrm K=\theta/^\circ\mathrm C+273$. **Supplement:** recall and calculate with $pV=\text{constant}$ for fixed mass at constant temperature, including the curved $p$–$V$ graph. The derivation of $pV=\tfrac13Nm\langle c^2\rangle$, moles and $k$ are extensions beyond 0625; they belong to the A-Level ideal-gas topic, not AS content.

### Cambridge 9702 (A-Level Physics) — §14.2 and §15
These are **A-Level-only topics**. **§14.2:** thermodynamic temperature and the Kelvin–Celsius conversion. **§15.1:** amount of substance, moles and $N_A$. **§15.2:** recall and use $pV=nRT=NkT$ and $k=R/N_A$. **§15.3:** assumptions, derive and use $pV=\tfrac13Nm\langle c^2\rangle$, distinguish mean-square and r.m.s. speeds, and deduce $\langle E_k\rangle=\tfrac32kT$ by comparison with the equation of state. The one-molecule → repeat collisions → sum → isotropy chain is explicitly required. §16.1's internal-energy definition includes molecular kinetic **and potential** energies; do not present $U=\tfrac32NkT$ as valid for every gas.

**Formula sheet:** the 2028–30 data pages give $R$, $k$ and $N_A$; the Paper 4 formula page supplies $p=\tfrac13(Nm/V)\langle c^2\rangle$. They do **not** supply $pV=nRT=NkT$ or $\langle E_k\rangle=\tfrac32kT$. A supplied pressure formula does not remove the requirement to derive it.

### IB Physics — B.1 Thermal energy transfers; B.3 Gas laws
Both SL and HL study the particle model, temperature and internal energy in B.1. B.3 requires $P=F/A$, $n=N/N_A$, ideal-gas assumptions and validity, the empirical gas laws, $PV=Nk_BT=nRT$, momentum transfer as the source of pressure and $P=\tfrac13\rho\langle v^2\rangle$. It explicitly includes **monatomic** internal energy $U=\tfrac32Nk_BT=\tfrac32nRT$ and pressure–volume representations. There is **no additional HL content in B.3**; thermodynamic processes and laws continue in B.4.

### AP Physics 2 — Unit 9, §9.1–9.2
§9.1 connects atomic collisions to pressure and mean kinetic energy to temperature, including $K_{\rm avg}=\tfrac32k_BT=\tfrac12mv_{\rm rms}^2$. Students interpret how a Maxwell–Boltzmann distribution changes with temperature; its functional form is **not required**. §9.2 covers ideal-gas assumptions and the gas law. Name the fixed variables before applying a proportionality; the course also expects quantitative work, not only verbal descriptions.

**Where it is not examined:** kinetic theory and thermodynamic gas laws are not topics in current AP Physics 1, AP Physics C: Mechanics or AP Physics C: Electricity and Magnetism. Cambridge 9709/9231 mechanics uses force, momentum and energy but does not prescribe this thermal model.

## Why Kinetic Theory Matters — College and Beyond

> [!info] Beyond syllabus — equipartition, real gases, and the bridge to statistical mechanics
> Recall that the translational energy of one classical ideal-gas molecule averages $\tfrac32kT$; this need not be its entire energy.
>
> **Equipartition.** The factor of 3 in $\tfrac{3}{2}kT$ is really "$\tfrac{1}{2}kT$ per degree of freedom," and a point molecule has 3 translational ones $(c_x,c_y,c_z)$. This is the **equipartition theorem**: each quadratic degree of freedom holds $\tfrac{1}{2}kT$ of energy on average. A *diatomic* molecule can also rotate (and at high $T$ vibrate), adding degrees of freedom — which is exactly why diatomic gases have larger heat capacities than monatomic ones. See [[Internal Energy]] for the total energy bookkeeping.
>
> **Real gases.** Drop assumptions 2 and 3 (molecules have size; they attract weakly) and you get the **van der Waals equation** $\left(p + \dfrac{a n^2}{V^2}\right)(V - nb) = nRT$: the $a$ term corrects for attraction (lowering pressure), the $b$ term for molecular volume. Ideal-gas behaviour is the dilute, hot limit where $a$ and $b$ stop mattering.
>
> **The statistical-mechanics bridge.** Kinetic theory is the gateway drug to **statistical mechanics**, where Boltzmann replaced "average over molecules" with "average over microstates" and wrote $S = k\ln W$ — the same $k$, now counting arrangements instead of collisions. The relative equilibrium weight of a microstate of energy $E$ contains the **Boltzmann factor** $e^{-E/kT}$; the probability of an energy range also depends on how many states have those energies, the single most important exponential in physical chemistry (reaction rates, atmospheres, semiconductors all run on it). The human story of how that constant came to bear Boltzmann's name — and the tragedy behind it — is in [[Stories/Boltzmann's Tombstone]].
>
> **Quantum coda.** When molecules get cold and crowded enough that their de Broglie waves overlap, classical counting fails and the indistinguishability and spin of identical particles determine their statistics: classical Maxwell–Boltzmann counting gives way to **Bose–Einstein** (photons, helium-4) and **Fermi–Dirac** (electrons) statistics. Planck cracked this open in 1900 using Boltzmann's own counting method — the move that started quantum mechanics.

## Connections

- **Prerequisites:** [[Newton's Laws of Motion]] (the wall collision is N2 as rate of change of momentum), [[Linear Momentum]] ($\Delta p = 2mc_x$ at each bounce — the engine of the derivation), [[Work, Energy and Power]] (the $\tfrac{1}{2}mv^2$ kinetic energy that temperature turns out to measure), [[Vectors in Physics]] (resolving velocity into independent $c_x, c_y, c_z$ components).
- **Components:** the empirical gas laws (Boyle, Charles, Gay-Lussac) combined into $pV=nRT$; the kinetic model's five assumptions.
- **The three states, warmed:** [[Thermal Expansion]] — why gases expand a hundred times more than solids, from how firmly the particles are held.
- **Extensions:** [[Internal Energy]] ($U = \tfrac{3}{2}NkT$ for a monatomic ideal gas), [[First Law of Thermodynamics]] ($\Delta U = Q + W$), [[Specific Heat Capacity]] (why diatomic > monatomic, via degrees of freedom).
- **The same gas, a million kilometres across:** [[Stellar Evolution]] — $p = nkT$ is what holds a star up against its own gravity, and balancing the two gives the Sun's core temperature from its mass and radius.
- **Cross-domain — mathematics:** [[Normal Distribution]] (each velocity component is Gaussian; the speed is the length of a 3-D normal vector → Maxwell–Boltzmann), [[Why Probability and Statistics]] (the whole model is "average over a population," and Maxwell–Boltzmann/Bose–Einstein/Fermi–Dirac statistics are combinatorial counting).
- **Story partner:** [[Stories/Boltzmann's Tombstone]] — the same constant $k$, statistical mechanics, and the man who argued atoms were real while this very model still needed defending.
- **The same $k$ elsewhere:** [[Information Theory]] — Boltzmann's $S = k\ln W$ is Shannon's entropy in physics units, and $k_BT$ sets the thermal-energy scale behind electrical noise.
- **For 9702 students:** see the verified given-versus-recall distinction in Exam Notes; the kinetic-pressure formula is supplied on Paper 4, but its derivation remains required.

## Sources and further reading

- [OpenStax: kinetic theory, molecular pressure and Brownian motion](https://openstax.org/books/college-physics-2e/pages/13-4-kinetic-theory-atomic-and-molecular-explanation-of-pressure-and-temperature).
- [OpenStax: heat capacity and equipartition](https://openstax.org/books/university-physics-volume-2/pages/2-3-heat-capacity-and-equipartition-of-energy) — why molecular translation is not always the whole internal energy.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $pV = nRT$ | `pV = nRT` | Ideal gas equation, per-mole form |
| $pV = NkT$ | `pV = NkT` | Per-molecule form; $N$ = number of molecules |
| $\langle c^2\rangle$ | `\langle c^2 \rangle` | Mean-square speed (average of $c^2$) |
| $c_{\text{rms}}$ | `c_{\text{rms}}` | Root-mean-square speed $=\sqrt{\langle c^2\rangle}$ |
| $pV = \tfrac{1}{3}Nm\langle c^2\rangle$ | `pV = \tfrac{1}{3}Nm\langle c^2\rangle` | Kinetic-theory pressure result |
| $\tfrac{1}{2}m\langle c^2\rangle = \tfrac{3}{2}kT$ | `\tfrac{1}{2}m\langle c^2\rangle = \tfrac{3}{2}kT` | Mean translational KE per molecule |
| $k = R/N_A$ | `k = R/N_A` | Boltzmann constant = gas constant per molecule |
| $N_A$ | `N_A` | Avogadro's number, $6.02\times10^{23}\,\text{mol}^{-1}$ |
| $\theta,\ T$ | `\theta,\ T` | Celsius $\theta$ vs absolute (Kelvin) $T$ |
