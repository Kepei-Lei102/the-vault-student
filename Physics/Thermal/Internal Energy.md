---
chinese: 内能 (nèinéng)
prerequisites:
  - "[[Kinetic Theory and the Ideal Gas]]"
  - "[[Work, Energy and Power]]"
leads_to:
  - "[[First Law of Thermodynamics]]"
  - "[[Specific Heat Capacity]]"
  - "[[Entropy and the Second Law]]"
tags:
  - subject/physics
  - domain/thermal-physics
  - level/A-Level
  - level/IGCSE-extension
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/A-Level
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-16-1
  - type/definition
  - type/derivation
  - notation/U-internal-energy
  - notation/k-boltzmann
  - notation/degrees-of-freedom
  - misconception/internal-energy-is-heat
  - misconception/internal-energy-equals-temperature
  - misconception/bulk-motion-is-internal-energy
  - misconception/ideal-gas-internal-energy-depends-on-pressure
  - misconception/temperature-always-rises-with-energy
---

# Internal Energy 内能

> *A hot object does not "contain heat." Heat is energy on the move — a transaction, not a balance. What the object holds is **internal energy**: the summed, invisible energy of $10^{23}$ molecules jiggling, spinning, and tugging on one another. This card opens the box that [[Kinetic Theory and the Ideal Gas|kinetic theory]] built. It takes the single-molecule result $\langle E_k\rangle = \tfrac{3}{2}kT$, adds it up over the whole population, splits the total into the part that is **motion** (kinetic) and the part that is **bonds** (potential), and arrives at the quantity $U$ that the [[First Law of Thermodynamics|first law]] will spend. For an ideal gas the answer is startlingly clean: $U = \tfrac{3}{2}NkT$ — internal energy is temperature, and nothing else.*

## Definition

The **internal energy** $U$ of a body is the **total of all the microscopic energies of its molecules** — the sum of

- their **random kinetic energy** (translation, and for non-point molecules also rotation and vibration), plus
- the **potential energy** stored in the forces *between* the molecules.

$$U = \underbrace{\sum_i (E_k)_i}_{\text{random molecular motion}} \;+\; \underbrace{\sum_{i<j} (E_p)_{ij}}_{\text{intermolecular bonds}}$$

The word **internal** is doing real work. $U$ is measured in the **rest frame of the body**, and it excludes two things you might expect: the ordered kinetic energy of the body moving *as a whole*, and the gravitational potential energy of the body sitting in an external field. A cricket ball in flight has bulk kinetic energy $\tfrac{1}{2}Mv^2$ and gravitational PE $Mgh$, but its *internal* energy is the molecular chaos sealed inside — the **same** whether the ball is screaming through the air or resting on the grass at the same temperature.

![[internal-energy-decomposition.svg|640]]

$U$ is a **state function**: it depends only on the present state of the body (for a gas, on $T$ and $V$), never on the route taken to get there. That single property is what makes the [[First Law of Thermodynamics|first law]] work, and it gets its own section below.

### 中文锚点

**内能**（nèinéng, internal energy）：物体内部**所有分子微观能量的总和** —— 分子**无规则运动的动能**（平动 + 转动 + 振动）加上分子间作用力的**势能**。

关键限定词是"内"：内能在物体**自身参考系**中度量，**不包括**整体平动的机械动能 $\tfrac{1}{2}Mv^2$，也**不包括**重力势能 $Mgh$。飞行中的板球，它的整体动能和重力势能都**不算**内能；内能是球**内部**分子的杂乱运动 —— 飞行还是静止，只要温度相同，内能就相同。

对**理想气体**：分子间无作用力（势能项为零），内能**全部是动能**：

$$U = N\langle E_k\rangle = \tfrac{3}{2}NkT = \tfrac{3}{2}nRT$$

—— 理想气体内能**只取决于温度**（与体积、压强无关）。这是本卡片的核心结论，直接来自 [[Kinetic Theory and the Ideal Gas|气体动理论]] 的 $\langle E_k\rangle = \tfrac{3}{2}kT$。

## The two ingredients — motion and bonds

**The kinetic part** is the one [[Kinetic Theory and the Ideal Gas|kinetic theory]] already measured: molecules fly, spin, and (at high temperature) vibrate, and the average translational share is $\langle E_k\rangle = \tfrac{3}{2}kT$ per molecule. This is the part **temperature reads** — heat the body and this term grows.

**The potential part** is new, and it lives in the **forces between molecules**. Two neutral molecules feel a force that depends on their separation $r$: a weak attraction when far apart, a violent repulsion when pushed too close, and a balance point in between. Plot the potential energy against $r$ and you get a **well**:

![[internal-energy-potential-well.svg|697]]

- at large $r$, $E_p \approx 0$ — molecules too far apart to feel each other (this is the chosen **zero reference**);
- as they approach, attraction *lowers* $E_p$ into the well (it goes **negative**);
- at the **equilibrium separation** $r_0$ the well bottoms out — where an undisturbed pair sits;
- forced closer than $r_0$, repulsion drives $E_p$ steeply **positive**.

> [!tip] Does potential energy have a direction? No — the sign is a *height*, not an arrow
> $E_p$ is a **scalar**; it has no direction. Its sign is only a comparison to a chosen **zero level** — here, two molecules infinitely far apart, not interacting.
> - **Attraction makes it negative.** Falling together from infinity, the attractive force does positive work and energy is released, dropping the pair *below* the reference, into the well. "Bound" literally means "below zero": you must *pay that energy back* to climb out to infinity again.
> - **Repulsion makes it positive.** Forcing the molecules closer than $r_0$ means doing work *against* the repulsion — like compressing a spring — lifting the energy *above* the reference.
>
> So the sign answers "bound, or compressed?", not "which way?". The direction lives in the **force**, which is the *slope* of this curve: $F = -\dfrac{dE_p}{dr}$. Force points "downhill" toward lower $E_p$ — outward on the steep left wall, inward on the gentle right slope, zero at the bottom $r_0$. (It is the same $F = -dE_p/dx$ that gives a stretched spring its restoring pull — see [[Hooke's Law for Springs]].)

Because the well is negative, a **bound** group of molecules carries *less* energy than the same molecules set free. That is the whole story of phase changes: a gas (molecules far apart, $E_p \approx 0$) sits *higher* than the liquid or solid it condensed from, so you must pour energy in to climb back out of the well.

**And the steep positive wall?** A molecule never *rests* up there — that region is visited only **briefly**, at the instant of closest approach in a collision. Two molecules rushing together trade kinetic energy for potential as they climb the wall; at the turning point their approach speed is momentarily zero and the energy is *all* potential; then the wall flings them back apart, turning it into kinetic energy again. This kinetic-to-potential-and-back exchange, over in about $10^{-13}\,\text{s}$, is exactly the **perfectly elastic collision** that [[Kinetic Theory and the Ideal Gas|kinetic theory]] assumed. The steepness of that wall is also why liquids and solids are nearly **incompressible** — squeezing $r$ below $r_0$ costs enormous energy — and, in the end, why your hand does not pass through a table.

> [!tip] The bond is a spring — that's why [[Hooke's Law for Springs|Hooke's law]] exists
> Near the bottom, every smooth potential well is approximately a **parabola** (the Taylor expansion of any minimum). So a molecule near $r_0$ feels a restoring force proportional to its displacement — it behaves like a tiny **spring**. This is the microscopic origin of [[Hooke's Law for Springs|Hooke's law]] and of why a heated solid's atoms perform [[Simple Harmonic Motion|simple harmonic motion]] about their lattice sites. The "spring constant" of the bond *is* the curvature of the well.

## The molecular model of the three states

The split into KE and PE is exactly what distinguishes a solid, a liquid, and a gas — same molecules, different shares of the two terms:

| State | Molecular picture | Kinetic energy | Potential energy |
|---|---|---|---|
| **Solid** | molecules locked in a lattice, vibrating about fixed sites | small | large and **negative** (deep in the well) |
| **Liquid** | molecules touching but mobile, sliding past one another | larger | still negative, but shallower |
| **Gas** | molecules far apart, nearly free | largest | $\approx 0$ (well escaped) |

Heating a substance pours energy into **both** terms — until you reach a **phase change**. During melting or boiling the temperature **stays constant** even as energy keeps flowing in: every joule goes into the **potential** term, dragging molecules up and out of the well (breaking bonds), with **none** left over to speed them up. That is why ice at $0\,^\circ\text{C}$ and the water it becomes at $0\,^\circ\text{C}$ are at the same temperature but the water holds more internal energy — the *latent heat* is pure $\Delta E_p$. (The bookkeeping of that hidden energy is the [[Specific Heat Capacity|specific & latent heat]] card.)

## The ideal gas — internal energy *is* temperature

For an **ideal gas** the model makes a clean amputation: assumption 3 of [[Kinetic Theory and the Ideal Gas|kinetic theory]] says there are **no intermolecular forces** except during collisions. No forces means **no intermolecular potential energy**, so the entire second term vanishes:

$$U = \sum_i (E_k)_i + \underbrace{\sum_{i<j}(E_p)_{ij}}_{=\,0} = N\langle E_k\rangle.$$

Substituting the kinetic-theory result $\langle E_k\rangle = \tfrac{3}{2}kT$ and using $Nk = nR$:

$$\boxed{\,U = \tfrac{3}{2}NkT = \tfrac{3}{2}nRT\,}\qquad\text{(monatomic ideal gas)}$$

Read what is — and is not — on the right-hand side. There is a $T$, and there is an amount ($N$ or $n$). There is **no $V$ and no $p$**. So:

> **The internal energy of an ideal gas depends on its temperature alone.**

This is **Joule's law**. Compress the gas, let it expand, change its pressure — as long as the temperature is unchanged, $U$ is unchanged. The reason is now transparent: $U$ is purely kinetic, the kinetic energy is set by $T$, and $T$ is the only lever. (Real gases break this slightly, because their $E_p$ term depends on how far apart the molecules are, i.e. on volume — see the beyond-syllabus section.)

## Degrees of freedom — where the $\tfrac{3}{2}$ comes from

Why $\tfrac{3}{2}$? Because a point molecule can move in **three independent directions** — $x$, $y$, $z$ — and randomness shares the energy equally among them: $\langle\tfrac{1}{2}mc_x^2\rangle = \langle\tfrac{1}{2}mc_y^2\rangle = \langle\tfrac{1}{2}mc_z^2\rangle = \tfrac{1}{2}kT$. Three of these makes $\tfrac{3}{2}kT$.

Each independent way a molecule can store energy is a **degree of freedom** (自由度, zìyóudù), and the rule generalises:

> **Equipartition theorem.** In thermal equilibrium, each *quadratic* degree of freedom holds, on average, $\tfrac{1}{2}kT$ of energy.

A *quadratic* degree of freedom is any energy term that looks like (constant)$\times$(variable)$^2$ — a $\tfrac{1}{2}mv^2$ for motion or a $\tfrac{1}{2}k x^2$ for a stretched bond. Count them and you get the internal energy:

![[internal-energy-degrees-of-freedom.svg|660]]

| Molecule | Degrees of freedom $f$ | Energy per molecule | Internal energy |
|---|---|---|---|
| **Monatomic** (He, Ar) | 3 translational | $\tfrac{3}{2}kT$ | $U = \tfrac{3}{2}nRT$ |
| **Diatomic** (N$_2$, O$_2$), room $T$ | 3 trans + 2 rotational | $\tfrac{5}{2}kT$ | $U = \tfrac{5}{2}nRT$ |
| **Diatomic**, high $T$ | 3 trans + 2 rot + 2 vibrational | $\tfrac{7}{2}kT$ | $U = \tfrac{7}{2}nRT$ |

A diatomic molecule is a tiny dumbbell: it can also **tumble** about the two axes perpendicular to its bond (spinning about the bond axis stores negligible energy), adding two rotational degrees of freedom. At high temperature the bond itself starts to **stretch and compress**, adding two more (one kinetic, one potential — a vibrating spring stores energy both ways). This is the deep reason diatomic gases have **larger heat capacities** than monatomic ones: there are simply more pockets to fill, so a given temperature rise demands more energy. ([[Specific Heat Capacity]] cashes this out as $C_V = \tfrac{f}{2}R$.)

> [!info] Beyond syllabus — the three faces of $c$, and why internal energy weighs something
> You have now met $c$ as a molecular **speed** in [[Kinetic Theory and the Ideal Gas|kinetic theory]] ($c_{\text{rms}}$); in the next card it returns as **specific heat capacity**; and you already know it as the **speed of light** in $E = mc^2$. Same letter, three jobs — read it from context. And that speed-of-light $c$ is quietly tied to *this* card.
> $E = mc^2$ says energy and mass are two views of one thing, so internal energy — being energy — **has mass**. A cooling cup of coffee literally loses mass as it radiates (about $10^{-12}$ of itself); a charged battery, a stretched spring, a hot poker are each immeasurably heavier than their cold, relaxed selves. Read it backwards through the potential well: a **bound** molecule, sitting at negative $E_p$, is *lighter* than its free atoms by (binding energy)$/c^2$. For chemical bonds that mass defect is about $10^{-10}$ — far too small to weigh. But shrink $r_0$ from molecular to **nuclear** scale and the binding energy per particle leaps a millionfold: the defect becomes about $1\%$, genuinely weighable, and it is the energy that lights the Sun. The internal energy you have been adding up *is* mass — you just cannot see it until you reach the nucleus. (A future Quantum & Nuclear bay picks up $E = mc^2$ and binding energy.)

## Internal energy is a state function

$U$ depends only on the **state** of the system, not on its **history**. Take a gas from state $A$ to state $B$ by any route — compress then heat, heat then compress, or some wandering path — and $\Delta U = U_B - U_A$ is the **same every time**. Around a closed cycle (back to where you started), $\Delta U = 0$.

This is not true of heat $Q$ or work $W$ separately: those are **path-dependent** — they measure *transfers along the way*, and different routes between $A$ and $B$ swap different amounts of heat and work. The miracle of the [[First Law of Thermodynamics|first law]] is that their **sum** is forced to be path-independent:

$$\Delta U = Q + W.$$

So $U$ is the **bank balance**; $Q$ and $W$ are **deposits and withdrawals**. You can reach a balance of \$100 by many sequences of transactions, but "\$100" describes the account, not how you got there. Heat and work are verbs; internal energy is a noun. (The full first law — sign conventions, $W = -p\,\Delta V$, and worked $pV$-cycles — is [[First Law of Thermodynamics]].)

## Worked Examples

**Example 1 — Internal energy of a monatomic gas (9702 §16.1).** Find the internal energy of $2.0\ \text{mol}$ of helium at $300\,\text{K}$, and the change when it is heated to $350\,\text{K}$.
$$U = \tfrac{3}{2}nRT = \tfrac{3}{2}(2.0)(8.31)(300) \approx 7.5\times10^3\,\text{J}.$$
$$\Delta U = \tfrac{3}{2}nR\,\Delta T = \tfrac{3}{2}(2.0)(8.31)(50) \approx 1.2\times10^3\,\text{J}.$$
Note $\Delta U$ needs only the temperature *change*, not the absolute temperature.

**Example 2 — Monatomic vs diatomic at the same temperature (IB B.1, equipartition).** One mole of helium and one mole of nitrogen are both at $300\,\text{K}$. Compare their internal energies.
$$U_{\text{He}} = \tfrac{3}{2}RT, \qquad U_{\text{N}_2} = \tfrac{5}{2}RT \;\Rightarrow\; \frac{U_{\text{N}_2}}{U_{\text{He}}} = \frac{5}{3}.$$
Both gases share the **same average translational KE** (same $T$, so the molecules have the same $\tfrac{3}{2}kT$ of flying-around energy), but nitrogen stockpiles extra energy in **rotation** — so at equal temperature it holds $\tfrac{5}{3}$ times the internal energy.

**Example 3 — Isothermal change: $\Delta U = 0$ (Joule's law).** An ideal gas is compressed slowly at constant temperature from $V_1$ to $V_2$. What is $\Delta U$?
Internal energy of an ideal gas is $U = \tfrac{3}{2}nRT$, a function of $T$ **only**. The temperature is unchanged, so
$$\Delta U = \tfrac{3}{2}nR\,\Delta T = 0.$$
Work *was* done on the gas and its volume *did* change — yet the internal energy did not move, because neither $V$ nor $p$ appears in $U$. (By the first law, the work done on the gas must have left as an equal quantity of heat: $Q = -W$.)

**Example 4 — Heating without warming (IB B.1.1; phase change).** A beaker of ice at $0\,^\circ\text{C}$ is heated steadily until it is all water at $0\,^\circ\text{C}$. The internal energy clearly rose (energy flowed in), yet the thermometer never moved. Where did the energy go?
Into the **potential** term. Melting drags molecules up out of their potential wells, breaking the rigid lattice — pure $\Delta E_p$, with the kinetic term (and hence the temperature) untouched. The temperature only climbs again once every bond that melting can break has broken.

## Common Misconceptions

### 1. "Internal energy is heat" / "a hot body contains heat"
Heat is energy *in transit* because of a temperature difference — it exists only while flowing, like a current. Internal energy is a *property the body owns* at every instant, flowing or not. A sealed flask of gas in equilibrium has a definite internal energy but exchanges **no** heat. Say "the gas has internal energy," never "the gas has heat."

### 2. "Internal energy is the same thing as temperature"
Temperature is **intensive** (energy *per molecule*, $\propto \langle E_k\rangle$); internal energy is **extensive** (the *total*, $\propto N$). Two identical kettles at $80\,^\circ\text{C}$ have the same temperature but **twice** the combined internal energy of one. And during a phase change $U$ rises while $T$ holds perfectly still — decisive proof they are different quantities.

### 3. "A fast-moving object has more internal energy"
Bulk, **ordered** kinetic energy is not internal energy. A flying bullet and an identical resting bullet at the same temperature have the **same** internal energy — $U$ is measured in the body's own rest frame. (Slamming the bullet to a stop *converts* its bulk KE into internal energy through friction, heating it — but that is a transfer, not a pre-existing store.)

### 4. "The internal energy of an ideal gas depends on its pressure or volume"
For an **ideal** gas, $U = \tfrac{3}{2}nRT$ — there is no $p$ and no $V$ in the formula. Squeeze it isothermally into half the volume at double the pressure and $U$ is **exactly unchanged**. Only $T$ matters (Joule's law). The trap is imagining a compressed gas is "more energetic"; it is only more energetic if it is also **hotter**.

### 5. "Adding energy always raises the temperature"
Not during a phase change. Latent heat raises internal energy while the temperature stays pinned, because the energy is spent entirely on **potential** energy — prising molecules apart — with nothing going to molecular speed. Temperature tracks the *kinetic* share only.

## Exam Notes

### Cambridge 9702 (A-Level Physics) — §16.1
The core home of this card. The syllabus wants three things: (i) internal energy is a **state function** determined by the state of the system; (ii) it is the **sum of the random distribution of kinetic and potential energies** of the molecules; (iii) a **rise in temperature raises the internal energy**. For an **ideal gas** there is no intermolecular PE, so $U$ is purely kinetic and $U = \tfrac{3}{2}NkT = \tfrac{3}{2}nRT$ (monatomic) — a standard result you should be able to state and use. Distinguish carefully from **§16.2** (the first law $\Delta U = q + W$ and sign conventions) in [[First Law of Thermodynamics]]; examiners love a structured question that defines internal energy in (a) and then applies the first law in (b).

### Cambridge 0625 (IGCSE Physics)
Covered **qualitatively** as the molecular model of matter: internal energy is the energy of the particles' motion (kinetic) and the energy of their separation/bonds (potential); heating a substance increases its internal energy; the three states differ in molecular spacing and motion; during melting/boiling the temperature stays constant while internal energy rises. No $\tfrac{3}{2}NkT$ and no degrees of freedom — those are AS/A-level extensions.

### IB Physics — Theme B (B.1.1)
**B.1.1** the molecular model of solids, liquids and gases; the Kelvin scale (done in [[Kinetic Theory and the Ideal Gas|kinetic theory]]); and **internal energy** as the total of the random kinetic and intermolecular potential energies of the particles. HL students use $U = \tfrac{3}{2}NkT$ for a monatomic ideal gas and the equipartition reasoning behind diatomic heat capacities. Phase changes as constant-temperature transfers of potential energy set up **B.1.2** (specific & latent heat).

### AP Physics 2 — Unit 9
Algebra-based. Internal energy of an ideal gas, $E_{\text{int}} = \tfrac{3}{2}nRT$ (often written $E_{\text{int}}$ rather than $U$), is the quantity that the **first law** $\Delta U = Q + W$ (**§9.4**) operates on, and that thermal-energy transfer (**§9.3**) changes. AP expects fluency with "internal energy of an ideal gas depends only on temperature" and the monatomic-vs-diatomic distinction, without the formal derivation.

## Why Internal Energy Matters — College and Beyond

> [!info] Beyond syllabus — frozen degrees of freedom, real gases, and the partition function
> **Quantum freeze-out.** Classical equipartition predicts a *fixed* $C_V = \tfrac{f}{2}R$, but measurements show hydrogen's molar heat capacity **climbs in steps** as it warms: $\tfrac{3}{2}R$ near $50\,\text{K}$, $\tfrac{5}{2}R$ by room temperature, approaching $\tfrac{7}{2}R$ only above $\sim1000\,\text{K}$. The reason is quantum: rotational and vibrational energy levels are **quantised**, and a mode stays "frozen" — unable to absorb energy — until $kT$ grows comparable to its level spacing. Equipartition is the *high-temperature* limit. Explaining the missing heat capacity of cold solids (Einstein 1907, Debye 1912) was one of the first triumphs of quantum theory, and it runs on the same Boltzmann factor $e^{-E/kT}$ that shaped the [[Kinetic Theory and the Ideal Gas|Maxwell–Boltzmann]] distribution.
>
> **Real gases.** Restore the intermolecular forces and the potential term returns: $U = U(T, V)$, no longer temperature alone. Let a real gas expand into a vacuum and it **cools**, because the molecules must climb out of their mutual potential wells, converting kinetic energy into potential — the **Joule–Thomson effect**, the principle behind every refrigerator and gas-liquefaction plant. The ideal-gas $U = U(T)$ is the dilute limit where the wells are too far apart to matter.
>
> **The statistical-mechanics shortcut.** In Boltzmann's framework the internal energy is not summed molecule by molecule but extracted from a single master function, the **partition function** $Z$: $\;U = -\dfrac{\partial \ln Z}{\partial \beta}$, with $\beta = 1/kT$. Every result on this card — the $\tfrac{3}{2}kT$, the equipartition $\tfrac{1}{2}kT$ per mode, the frozen degrees of freedom — drops out of that one expression. It is the engine room behind [[Stories/Boltzmann's Tombstone|Boltzmann's]] $S = k\ln W$.

## Connections

- **Parent:** [[Kinetic Theory and the Ideal Gas]] — supplies the per-molecule energy $\langle E_k\rangle = \tfrac{3}{2}kT$ that this card totals over the whole population.
- **Prerequisites:** [[Work, Energy and Power]] (the $\tfrac{1}{2}mv^2$ kinetic energy and the energy-accounting mindset), [[Kinetic Theory and the Ideal Gas]] (temperature as molecular KE; the ideal-gas assumptions that kill the PE term).
- **Components:** the random molecular **kinetic** energy (translation + rotation + vibration, counted by degrees of freedom) and the **intermolecular potential** energy (the bond well).
- **Extensions:** [[First Law of Thermodynamics]] ($\Delta U = Q + W$ — internal energy is the state function heat and work change), [[Specific Heat Capacity]] ($C_V = \tfrac{f}{2}R$ from degrees of freedom; latent heat as $\Delta E_p$) — the rest of the Thermal bay.
- **Cross-domain — mechanics:** [[Hooke's Law for Springs]] (the intermolecular well is parabolic near $r_0$, so bonds act as springs — the microscopic root of Hooke's law), [[Simple Harmonic Motion]] (atoms vibrating in a solid lattice).
- **Story partner:** [[Stories/Boltzmann's Tombstone]] — internal energy falls out of the partition function $Z$, the same statistical machinery behind $S = k\ln W$.
- **For 9702 / A-Level Physics students:** the constants ($R$, $k$, $N_A$) are on the 9702 data-and-formulae sheet; the relation $U = \tfrac{3}{2}NkT$ you apply, and the molecular model (internal energy = random KE + intermolecular PE) is bookwork you must be able to state.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $U$ | `U` | Internal energy (total of molecular KE + PE) |
| $U = \tfrac{3}{2}NkT$ | `U = \tfrac{3}{2}NkT` | Monatomic ideal gas, per-molecule form |
| $U = \tfrac{3}{2}nRT$ | `U = \tfrac{3}{2}nRT` | Same, per-mole form ($Nk = nR$) |
| $\langle E_k\rangle$ | `\langle E_k \rangle` | Mean molecular kinetic energy $=\tfrac{3}{2}kT$ |
| $E_p$ | `E_p` | Intermolecular potential energy (negative when bound) |
| $\Delta U = Q + W$ | `\Delta U = Q + W` | First law; $U$ is the state function |
| $f$ | `f` | Number of (quadratic) degrees of freedom |
| $\tfrac{1}{2}kT$ | `\tfrac{1}{2}kT` | Equipartition: energy per degree of freedom |
| $r_0$ | `r_0` | Equilibrium molecular separation (bottom of the well) |
| $F = -\dfrac{dE_p}{dr}$ | `F = -\dfrac{dE_p}{dr}` | Force is the negative slope of the PE curve |
