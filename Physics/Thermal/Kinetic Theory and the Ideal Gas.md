---
chinese: 气体动理论与理想气体 (qìtǐ dònglǐlùn yǔ lǐxiǎng qìtǐ)
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Linear Momentum]]"
  - "[[Work, Energy and Power]]"
  - "[[Vectors in Physics]]"
leads_to:
  - "[[Internal Energy]]"
  - "[[First Law of Thermodynamics]]"
  - "[[Specific Heat Capacity]]"
  - "[[Entropy and the Second Law]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/thermal-physics
  - level/A-Level
  - level/IGCSE-extension
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/A-Level
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
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

> *Temperature feels like a primitive thing — a number on a thermometer. Kinetic theory says it is nothing of the kind. Temperature is bookkeeping for a single hidden quantity: the average kinetic energy of one molecule. Heat the gas and you are, literally, speeding up the molecules. This card derives that claim from nothing but Newton's laws and a box of bouncing balls — and out of it falls the same constant $k$ carved on [[Stories/Boltzmann's Tombstone|Boltzmann's gravestone]].*

## Definition

An **ideal gas** is a gas that obeys the **equation of state**

$$pV = nRT = NkT$$

exactly, where $p$ is pressure, $V$ volume, $T$ the **absolute** (Kelvin) temperature, $n$ the number of **moles**, $N$ the number of **molecules**, $R = 8.31\,\text{J mol}^{-1}\text{K}^{-1}$ the **molar gas constant**, and $k = 1.38 \times 10^{-23}\,\text{J K}^{-1}$ the **Boltzmann constant**. **Kinetic theory** is the microscopic model — molecules as tiny, fast, randomly-moving particles — that *derives* this macroscopic law and, in doing so, reveals what temperature actually is.

### 中文锚点

**理想气体**（lǐxiǎng qìtǐ）：严格满足状态方程 $pV = nRT = NkT$ 的气体。$T$ 必须是**绝对温度**（开尔文 Kelvin），$n$ 是**摩尔数**，$N$ 是**分子数**，$R$ 是**摩尔气体常数**，$k$ 是**玻尔兹曼常数**（Boltzmann constant）。

**气体动理论**（qìtǐ dònglǐlùn, kinetic theory）：把气体看成大量做无规则运动的小分子，用**牛顿力学**推导出宏观的气体定律。核心结论惊人地简单：

$$\tfrac{1}{2}m\langle c^2\rangle = \tfrac{3}{2}kT$$

—— **温度就是分子平均平动动能的度量**。加热气体，本质上就是让分子跑得更快。绝对零度（$T=0$）对应分子平动动能为零。

关键术语：$\langle c^2 \rangle$ 是**均方速率**（mean-square speed），$c_{\text{rms}} = \sqrt{\langle c^2\rangle}$ 是**均方根速率**（root-mean-square speed）。本卡片推导 $pV = \tfrac{1}{3}Nm\langle c^2\rangle$，并把它和 $pV = NkT$ 对比，得到上面那条"温度即动能"的结论。这正是 [[Stories/Boltzmann's Tombstone|玻尔兹曼]] 统计力学的物理基石。

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

A box of molecules obeying exactly the five assumptions above: random directions, elastic bounces, no forces between collisions. Watch three things. First, the **net-momentum arrow stays near zero** even though every molecule is screaming along — random directions cancel, which is *why a room full of 500 m/s nitrogen feels like nothing*. Second, the **wall lights up on every impact**: that drumbeat of collisions, summed, *is* the pressure. Third, when the gas is **heated**, every molecule speeds up and the **speed histogram** (right) slides rightward and flattens into the Maxwell–Boltzmann shape — the same curve plotted later in this card, now built one molecule at a time.

## The derivation — pressure from molecular chaos

![[kinetic-theory-box-derivation.svg|697]]

Here is the heart of the card: getting a macroscopic pressure out of microscopic collisions, using only momentum. Put $N$ molecules, each of mass $m$, in a cubical box of side $L$ (so volume $V = L^3$).

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

This is a purely mechanical result — no thermometer has appeared yet. It says pressure is set by how many molecules there are, how heavy they are, and how fast they move (mean-square).

## Temperature *is* average kinetic energy

Now lay the mechanical result beside the experimental equation of state. We have, from mechanics,

$$pV = \tfrac{1}{3}Nm\langle c^2\rangle,$$

and from experiment (per molecule form, since $n R = N k$),

$$pV = NkT.$$

Two expressions for the same $pV$ must be equal:

$$\tfrac{1}{3}Nm\langle c^2\rangle = NkT \;\;\Longrightarrow\;\; \tfrac{1}{3}m\langle c^2\rangle = kT.$$

Multiply both sides by $\tfrac{3}{2}$ and the left side becomes the average translational kinetic energy of a molecule, $\tfrac{1}{2}m\langle c^2\rangle$:

$$\boxed{\;\langle E_k\rangle = \tfrac{1}{2}m\langle c^2\rangle = \tfrac{3}{2}kT\;}$$

This is one of the most quietly profound equations in physics. **The absolute temperature of a gas is, up to the constant $\tfrac{3}{2}k$, nothing but the average translational kinetic energy of one of its molecules.** A thermometer is a (very indirect) molecular speedometer. Consequences:

- **Temperature is *intensive*.** It depends on the energy *per molecule*, not the total. A spark at 1000 °C and a bathtub of warm water carry wildly different *amounts* of thermal energy, but the spark's molecules are individually more energetic.
- **Absolute zero has meaning.** At $T = 0$, $\langle E_k\rangle = 0$: classically, all molecular translation ceases. This is *why* the Kelvin scale starts where it does — it is the temperature scale on which $T$ is directly proportional to molecular KE. (Quantum mechanics adds an unremovable *zero-point* energy, and the third law makes $T=0$ unreachable — see beyond-syllabus.)
- **At the same temperature, every gas has the same average molecular KE.** Hydrogen and xenon at 300 K share $\langle E_k\rangle$ — which immediately tells you the light molecules must be moving *faster* (next section).

## The two faces of the gas constant — why $k$ is Boltzmann's

The equation of state comes in two equivalent forms:

$$pV = \underbrace{nRT}_{\text{per mole}} = \underbrace{NkT}_{\text{per molecule}}.$$

They are linked by **Avogadro's number** $N_A = 6.02\times10^{23}\,\text{mol}^{-1}$, the number of molecules in one mole. Since $N = nN_A$,

$$nRT = NkT \;\Longrightarrow\; nRT = nN_A kT \;\Longrightarrow\; \boxed{k = \frac{R}{N_A}}.$$

So the **Boltzmann constant is just the gas constant *per molecule*** — you take the per-mole bookkeeping constant $R$ and divide out Avogadro's number to get the per-molecule version. Numerically $k = 8.31 / (6.02\times10^{23}) = 1.38\times10^{-23}\,\text{J K}^{-1}$.

This is the same $k$ that appears in **[[Stories/Boltzmann's Tombstone|Boltzmann's entropy formula]]** $S = k\ln W$ and in the [[Information Theory|noise floor]] $k_B T$ of every communication channel. It is the universal conversion factor between **temperature and energy** — "how many joules is one kelvin worth, per molecule." Encountering the same $k$ in the pressure of a gas, the entropy of a black hole, and the thermal noise in a wire is not a coincidence: all three are statements about molecules (or microstates) carrying energy $\sim kT$ apiece.

## r.m.s. speed and the spread of speeds

Rearranging $\tfrac{1}{2}m\langle c^2\rangle = \tfrac{3}{2}kT$ for the **root-mean-square speed**:

$$c_{\text{rms}} = \sqrt{\langle c^2\rangle} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M}},$$

where $M = mN_A$ is the **molar mass**. Two readings fall straight out:

- $c_{\text{rms}} \propto \sqrt{T}$ — to *double* the typical molecular speed you must *quadruple* the absolute temperature.
- $c_{\text{rms}} \propto 1/\sqrt{m}$ — at a given temperature, **lighter molecules move faster**. (This is why hydrogen and helium leak out of the atmosphere over geological time, and why a helium balloon deflates faster than an air-filled one: the fast little molecules find the gaps.)

> [!example] How fast is the air in this room?
> Nitrogen, $M = 0.028\,\text{kg mol}^{-1}$, at $T = 300\,\text{K}$:
> $$c_{\text{rms}} = \sqrt{\frac{3(8.31)(300)}{0.028}} \approx 517\,\text{m s}^{-1}.$$
> The molecules around you are moving at roughly **1.5 times the speed of sound** — which is no accident, since sound *is* a disturbance carried by those same colliding molecules.

### If the air is moving at 517 m/s, why don't we feel a gale?

This is the right question to ask, and it has two answers — the second is the beautiful one.

**The motion is random, so there is no *net* flow.** For every molecule slamming into you from the left at 517 m/s, one hits from the right just as hard. The momentum transfers cancel, so there is **no net push** — no wind. A breeze is what you feel when the entire swarm picks up a small *bulk drift* (a few m s⁻¹) *on top of* the random 517 — the whole crowd walking one way at once. Still air has zero drift, hence zero wind, no matter how furious the underlying thermal motion. (It is also why the thermal speed and the speed of sound are the same order of magnitude: sound is exactly a small organised ripple riding on that random sea.)

**You *do* feel it — as pressure, not wind.** The sum of those $\sim 10^{23}$ tiny impacts per second on every square centimetre *is* atmospheric pressure — about **10 tonnes** pressing on your body right now. You don't notice because it is perfectly balanced: equal from every direction, and matched by the pressure inside you (lungs, blood, tissues) pushing back out. The body only registers pressure **differences** — ears popping as a plane climbs, suction on a straw, the shove of a moving swarm. One molecule is far too light, and the impacts far too frequent, for your senses to resolve individually; they blur into the two steady averages your senses *can* read — **pressure** and **temperature**. The 517 m/s is hiding in plain sight, as "1 atmosphere" and "room temperature."

**Not all molecules move at $c_{\text{rms}}$.** That is just the speed whose square is the average. The actual speeds are spread out in the **Maxwell–Boltzmann distribution**:

![[kinetic-theory-maxwell-boltzmann.svg|520]]

The distribution is skewed — a hard floor at zero, a long tail toward high speeds — so the three "typical" speeds are slightly different and always in the same order:

$$c_{\text{mp}} \;<\; \bar c \;<\; c_{\text{rms}},$$

the most-probable (peak), the mean, and the root-mean-square. Heating the gas slides the whole curve right and flattens it (the molecules spread over a wider band of speeds). There is a beautiful link to statistics here: each *velocity component* $c_x, c_y, c_z$ is **[[Normal Distribution|normally distributed]]** about zero, and the *speed* $c = \sqrt{c_x^2+c_y^2+c_z^2}$ — the length of a 3-D vector of three independent normals — is exactly what produces the Maxwell–Boltzmann shape.

## Worked Examples

**Example 1 — Boyle's law from the model (9702 §15.2).** A fixed mass of ideal gas at $1.0\times10^5\,\text{Pa}$ occupies $2.0\times10^{-3}\,\text{m}^3$. It is compressed isothermally to $5.0\times10^{-4}\,\text{m}^3$. Find the new pressure.
*Constant $T$, fixed $N$, so $pV = NkT$ is constant: $p_1V_1 = p_2V_2$.*
$$p_2 = \frac{p_1V_1}{V_2} = \frac{(1.0\times10^5)(2.0\times10^{-3})}{5.0\times10^{-4}} = 4.0\times10^5\,\text{Pa}.$$

**Example 2 — Counting molecules (9702 §15.1–15.2).** How many molecules are in $25\,\text{cm}^3$ of an ideal gas at $1.0\times10^5\,\text{Pa}$ and $300\,\text{K}$?
$$N = \frac{pV}{kT} = \frac{(1.0\times10^5)(25\times10^{-6})}{(1.38\times10^{-23})(300)} \approx 6.0\times10^{20}\ \text{molecules.}$$
(That's about a milli-mole — reassuringly, $6.0\times10^{20}/6.02\times10^{23} \approx 1.0\times10^{-3}\,\text{mol}$.)

**Example 3 — Temperature to speed (9702 §15.3).** Find $c_{\text{rms}}$ for helium ($M = 4.0\times10^{-3}\,\text{kg mol}^{-1}$) at $300\,\text{K}$, and compare with the nitrogen result above.
$$c_{\text{rms}} = \sqrt{\frac{3(8.31)(300)}{4.0\times10^{-3}}} \approx 1370\,\text{m s}^{-1}.$$
Helium is about $\sqrt{28/4} = \sqrt{7} \approx 2.6$ times faster than nitrogen at the same temperature — exactly the $1/\sqrt{m}$ law, since both share the same average KE.

**Example 4 — Average KE is gas-independent (IB B.3, AP-2 §9.1).** What is the average translational kinetic energy of *any* ideal-gas molecule at room temperature, $T = 293\,\text{K}$?
$$\langle E_k\rangle = \tfrac{3}{2}kT = \tfrac{3}{2}(1.38\times10^{-23})(293) \approx 6.1\times10^{-21}\,\text{J}.$$
The same for helium, nitrogen, or uranium hexafluoride — temperature fixes the energy per molecule, not the speed.

## Common Misconceptions

### 1. "Temperature measures heat / total energy"
Temperature measures the **average kinetic energy per molecule** — it is *intensive*. A cup of boiling water and a swimming pool at the same temperature have the same molecular KE, but the pool holds vastly more total thermal energy. Heat (energy transferred) and temperature (energy per molecule) are different quantities; conflating them is the single most common thermal error.

### 2. "Heavier gas molecules move faster"
The opposite. At a given temperature **all** gases share the same average KE, so $\tfrac{1}{2}m\langle c^2\rangle$ is fixed — which means larger $m$ forces *smaller* $\langle c^2\rangle$. Heavy molecules are **slower** ($c_{\text{rms}}\propto 1/\sqrt m$).

### 3. "All the molecules move at the same speed"
There is a whole **distribution** of speeds (Maxwell–Boltzmann), from near-zero to several times $c_{\text{rms}}$. $c_{\text{rms}}$ is a single representative value, not a universal molecular speed.

### 4. "Gas pressure is molecules pushing on each other"
In the ideal model molecules exert **no forces on each other** at all. The pressure on a container wall comes entirely from molecules **colliding with the wall** and reversing momentum — the derivation above never once used a molecule–molecule force.

### 5. "You can reach absolute zero / molecules truly stop"
Classically $T=0$ would mean zero molecular motion, but the **third law of thermodynamics** makes absolute zero unreachable in a finite number of steps, and **quantum mechanics** leaves an irreducible *zero-point* energy even at $T=0$. Absolute zero is a limit you approach, not a place you arrive.

## Exam Notes

### Cambridge 9702 (A-Level Physics) — §14, §15, §16
The core home of this card. **§14.2** Kelvin scale, $T/\text{K} = \theta/^\circ\text{C} + 273.15$ — always convert to Kelvin before using any gas equation. **§15.1** the mole and $N_A$. **§15.2** equation of state $pV = nRT = NkT$. **§15.3** the kinetic-theory derivation of $pV = \tfrac{1}{3}Nm\langle c^2\rangle$ (you may be asked to reproduce it), r.m.s. speed, and $\tfrac{1}{2}m\langle c^2\rangle = \tfrac{3}{2}kT$. **§16.1** internal energy as the sum of random molecular KE + PE — for an ideal gas there is no intermolecular PE, so internal energy is *purely* kinetic, $U = N\langle E_k\rangle = \tfrac{3}{2}NkT$. The derivation is a standard structured-question target; learn the five steps (one molecule → one wall → frequency → sum → randomness).

### Cambridge 0625 (IGCSE Physics)
Covered **qualitatively**: the particle model of matter, gas pressure as molecular bombardment of the walls, and the $p$–$V$–$T$ relationships described in words and simple proportion (Boyle's law graphs). The $pV = \tfrac{1}{3}Nm\langle c^2\rangle$ derivation and the constant $k$ are **not** at IGCSE — they are AS-level extensions. IGCSE students should leave with the *picture* (fast random molecules hitting walls) and the three proportionalities.

### IB Physics — Theme B (B.1, B.3)
**B.1.1** molecular model, the Kelvin scale, internal energy. **B.3.1** kinetic-theory assumptions, conditions for the ideal-gas approximation (low $p$, moderate $T$, low density), pressure $p = F/A$, Avogadro's constant. **B.3.2** the equation of state $pV = nRT = NkT$, isothermal/isobaric/isochoric changes and their $pV$ diagrams, and the central relation $\langle E_k\rangle = \tfrac{3}{2}kT$. HL extends into the first and second laws (a later card).

### AP Physics 2 — Unit 9 (Thermodynamics)
**9.1** kinetic theory of temperature and pressure (the $\langle E_k\rangle = \tfrac{3}{2}kT$ result and the molecular origin of pressure). **9.2** the ideal gas law $pV = nRT$. Algebra-based: AP does not require reproducing the calculus-free derivation in full, but expects the conceptual chain "molecular collisions → pressure → temperature as average KE," and fluent use of $pV=nRT$ and $c_{\text{rms}} = \sqrt{3kT/m}$.

## Why Kinetic Theory Matters — College and Beyond

> [!info] Beyond syllabus — equipartition, real gases, and the bridge to statistical mechanics
> **Equipartition.** The factor of 3 in $\tfrac{3}{2}kT$ is really "$\tfrac{1}{2}kT$ per degree of freedom," and a point molecule has 3 translational ones $(c_x,c_y,c_z)$. This is the **equipartition theorem**: each quadratic degree of freedom holds $\tfrac{1}{2}kT$ of energy on average. A *diatomic* molecule can also rotate (and at high $T$ vibrate), adding degrees of freedom — which is exactly why diatomic gases have larger heat capacities than monatomic ones. (Recall that internal energy is the total of all these molecular energies — the [[Internal Energy]] card picks this up.)
>
> **Real gases.** Drop assumptions 2 and 3 (molecules have size; they attract weakly) and you get the **van der Waals equation** $\left(p + \dfrac{a n^2}{V^2}\right)(V - nb) = nRT$: the $a$ term corrects for attraction (lowering pressure), the $b$ term for molecular volume. Ideal-gas behaviour is the dilute, hot limit where $a$ and $b$ stop mattering.
>
> **The statistical-mechanics bridge.** Kinetic theory is the gateway drug to **statistical mechanics**, where Boltzmann replaced "average over molecules" with "average over microstates" and wrote $S = k\ln W$ — the same $k$, now counting arrangements instead of collisions. The probability a molecule has energy $E$ falls off as the **Boltzmann factor** $e^{-E/kT}$, the single most important exponential in physical chemistry (reaction rates, atmospheres, semiconductors all run on it). The human story of how that constant came to bear Boltzmann's name — and the tragedy behind it — is in [[Stories/Boltzmann's Tombstone]].
>
> **Quantum coda.** When molecules get cold and crowded enough that their de Broglie waves overlap, classical counting fails and you must ask whether the particles are distinguishable: Maxwell–Boltzmann statistics splits into **Bose–Einstein** (photons, helium-4) and **Fermi–Dirac** (electrons) statistics. Planck cracked this open in 1900 using Boltzmann's own counting method — the move that started quantum mechanics.

## Connections

- **Prerequisites:** [[Newton's Laws of Motion]] (the wall collision is N2 as rate of change of momentum), [[Linear Momentum]] ($\Delta p = 2mc_x$ at each bounce — the engine of the derivation), [[Work, Energy and Power]] (the $\tfrac{1}{2}mv^2$ kinetic energy that temperature turns out to measure), [[Vectors in Physics]] (resolving velocity into independent $c_x, c_y, c_z$ components).
- **Components:** the empirical gas laws (Boyle, Charles, Gay-Lussac) combined into $pV=nRT$; the kinetic model's five assumptions.
- **Extensions:** [[Internal Energy]] ($U = \tfrac{3}{2}NkT$ for an ideal gas), [[First Law of Thermodynamics]] ($\Delta U = Q + W$), [[Specific Heat Capacity]] (why diatomic > monatomic, via degrees of freedom) — the rest of the Thermal bay.
- **Cross-domain — mathematics:** [[Normal Distribution]] (each velocity component is Gaussian; the speed is the length of a 3-D normal vector → Maxwell–Boltzmann), [[Why Probability and Statistics]] (the whole model is "average over a population," and Maxwell–Boltzmann/Bose–Einstein/Fermi–Dirac statistics are combinatorial counting).
- **Story partner:** [[Stories/Boltzmann's Tombstone]] — the same constant $k$, statistical mechanics, and the man who argued atoms were real while this very model still needed defending.
- **The same $k$ elsewhere:** [[Information Theory]] — Boltzmann's $S = k\ln W$ is Shannon's entropy in physics units, and the thermal-noise floor $k_BT$ caps every communication channel.
- **For 9702 / A-Level Physics students:** the gas equations and constants ($R$, $k$, $N_A$) are given in the 9702 data-and-formulae sheet; the *derivation* of $pV=\tfrac{1}{3}Nm\langle c^2\rangle$ is not — you must be able to reproduce it.

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
