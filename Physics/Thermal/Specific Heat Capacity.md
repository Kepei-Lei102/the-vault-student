---
chinese: 比热容与潜热 (bǐrèróng yǔ qiánrè)
prerequisites:
  - "[[Internal Energy]]"
  - "[[Kinetic Theory and the Ideal Gas]]"
leads_to:
  - "[[First Law of Thermodynamics]]"
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
  - syllabus/9702-14-3
  - syllabus/0625-2-2
  - type/definition
  - type/derivation
  - notation/specific-heat-c
  - notation/latent-heat-L
  - misconception/heat-capacity-is-temperature
  - misconception/boiling-water-gets-hotter
  - misconception/latent-heat-raises-temperature
  - misconception/specific-heat-is-extensive
  - misconception/all-substances-heat-equally
---

# Specific Heat Capacity 比热容

> *[[Internal Energy|Internal energy]] said what is stored inside a substance. This card asks the practical question: how much energy does it take to actually warm something up — or melt it, or boil it? The answer splits cleanly in two. Pour energy into a substance and either its temperature climbs (specific heat capacity, the molecules speeding up) or its temperature stalls while it changes phase (latent heat, the bonds breaking). The same potential well from the last card decides which: heating raises the kinetic term; melting and boiling pay the potential term. And one substance — water — is so stubborn about both that it runs the planet's climate.*

## Definition

**Specific heat capacity** $c$ is the energy needed to raise the temperature of **1 kg** of a substance by **1 K** (= 1 °C):

$$\boxed{\,Q = mc\,\Delta T\,}$$

where $Q$ is the energy transferred, $m$ the mass, and $\Delta T$ the temperature change. Units of $c$: $\text{J kg}^{-1}\text{K}^{-1}$.

**Specific latent heat** $L$ is the energy needed to change the **phase** of 1 kg of a substance **at constant temperature** (no $\Delta T$):

$$\boxed{\,Q = mL\,}$$

with $L_f$ the specific latent heat of **fusion** (melting/freezing) and $L_v$ the specific latent heat of **vaporisation** (boiling/condensing). Units of $L$: $\text{J kg}^{-1}$.

A note on *capacity* vs *specific capacity*: the **heat capacity** $C = mc$ of a whole object (units $\text{J K}^{-1}$) is the energy to warm *that object* by 1 K, so $Q = C\,\Delta T$. The **specific** heat capacity divides that by mass — it is a property of the *material*, not the lump.

### 中文锚点

**比热容**（bǐrèróng, specific heat capacity）$c$：使 **1 kg** 物质温度升高 **1 K** 所需的能量，$Q = mc\Delta T$，单位 $\text{J kg}^{-1}\text{K}^{-1}$。

**比潜热**（bǐ qiánrè, specific latent heat）$L$：在**恒定温度**下改变 1 kg 物质**物态**所需的能量，$Q = mL$。$L_f$ 是**熔化**（rónghuà, fusion）潜热，$L_v$ 是**汽化**（qìhuà, vaporisation）潜热。单位 $\text{J kg}^{-1}$。

核心区分：加热物质时，能量要么让温度上升（**比热容**——分子动能增加），要么在物态变化时让温度**停滞不动**（**潜热**——分子间键断裂，势能增加）。这正是 [[Internal Energy|内能]] 卡片那口"势能井"的两种去向：升温填的是动能项，熔化/汽化填的是势能项。

## Why it works — heat capacity is internal energy per kelvin

Specific heat capacity is not a new mystery; it is the **macroscopic price tag on [[Internal Energy|internal energy]]**. Raising a substance's temperature by $\Delta T$ means raising its internal energy, and $c$ just measures how many joules per kilogram per kelvin that costs. So the *reason* one material has a larger $c$ than another is the reason from the last card: **how many places a molecule has to put energy.**

![[degrees-of-freedom.svg|697]]

For an ideal gas we can turn that picture into an exact number. Each molecule stores energy in a fixed set of **degrees of freedom** $f$ — the independent ways it can move. A single atom has just 3 (translation along $x$, $y$, $z$); a diatomic molecule adds 2 rotations, giving $f = 5$ at room temperature. Equipartition (see [[Internal Energy]]) hands each degree of freedom $\tfrac12 kT$, so the internal energy is

$$U = \tfrac{f}{2}nRT,$$

where $n$ is the number of moles. Heat capacity is simply **how fast $U$ climbs as $T$ rises** — and now we can compute it.

### One gas, two heat capacities

Here is the one subtlety, and it is the source of most confusion. For a gas it matters **how you hold it while you heat it**, because a gas can push back on its container. So we track **two** *molar* heat capacities. "Molar" means *per mole*, so the defining recipe is "divide the heat $Q$ by both the number of moles $n$ and the temperature rise $\Delta T$":

$$C = \frac{Q}{n\,\Delta T} \qquad\text{(the energy to warm \textbf{one mole} by \textbf{one kelvin}).}$$

- $C_V$ — **at constant Volume**: the gas is sealed in a rigid box and cannot expand.
- $C_p$ — **at constant pressure**: the gas is free to expand (think of a sliding, weightless piston) as it warms.

**Constant volume — finding $C_V$.** A rigid box means the gas cannot move its walls, so it does **no work**; every joule of heat goes straight into internal energy. Hence $Q = \Delta U = \tfrac{f}{2}nR\,\Delta T$. Drop that into the definition of $C$ and watch the clutter cancel:

$$C_V = \frac{Q}{n\,\Delta T} = \frac{\tfrac{f}{2}\,nR\,\Delta T}{n\,\Delta T} = \boxed{\tfrac{f}{2}R}.$$

The $n$ cancels (it appears top and bottom) and the $\Delta T$ cancels (top and bottom too) — and that cancellation is the *whole point* of dividing by them. It means **how much** gas you took and **how big** a temperature step you chose both drop out, leaving a number that depends only on the *kind* of gas, through $f$. A **monatomic** gas ($f=3$) has $C_V = \tfrac{3}{2}R$; a **diatomic** gas ($f=5$) has $C_V = \tfrac{5}{2}R$ — more pockets to fill, more energy per kelvin. This is the promise the Internal Energy card made, now paid.

**Constant pressure — finding $C_p$.** Now let the gas expand as it warms. It must *still* raise its internal energy by the same $\tfrac{f}{2}nR\,\Delta T$ — but on top of that it must do **work** pushing its surroundings back. From the ideal-gas law $pV = nRT$ at constant pressure, $p\,\Delta V = nR\,\Delta T$, so that work is $W = p\,\Delta V = nR\,\Delta T$. Energy conservation now reads $Q = \Delta U + W$, and we divide by $n\,\Delta T$ exactly as before:

$$C_p = \frac{Q}{n\,\Delta T} = \frac{\Delta U + W}{n\,\Delta T} = \frac{\tfrac{f}{2}nR\,\Delta T + nR\,\Delta T}{n\,\Delta T} = \tfrac{f}{2}R + R = C_V + R.$$

Same cancellation of $n$ and $\Delta T$, one extra term. This is **Mayer's relation**:

$$\boxed{\,C_p = C_V + R\,}$$

Heating at constant pressure always costs exactly $R$ more per mole per kelvin than at constant volume, and that extra $R$ *is* the work of expansion — nothing else. (Their ratio $\gamma = C_p / C_V$, the *adiabatic index*, sets the speed of sound in the gas and the behaviour of adiabatic changes; for a monatomic gas $\gamma = \tfrac{5/2}{3/2} = \tfrac{5}{3}$.) The full machinery of $Q$, $W$, and $\Delta U$ is the [[First Law of Thermodynamics]] card; this is its appetiser. The rest of this card returns to the solids and liquids of the exam syllabus.

## Latent heat — the energy that doesn't warm anything

Now the second channel. Keep heating ice and its temperature climbs — until it hits $0\,^\circ\text{C}$. There it **stops**, dead, even though energy is still pouring in, and stays at $0\,^\circ\text{C}$ until the last of the ice has melted. Only then does the temperature move again. Where did the energy go?

Back to the [[Internal Energy|potential well]] — and this time we have to ask *why that well is there at all*. **Recall that** it is the real graph of two molecules' shared potential energy against their separation $r$ (drawn in full on the [[Internal Energy]] card), and its shape is a tug-of-war between two effects. **Far apart**, the molecules feel a weak **attraction** — the electrons of one tug gently on the other — so letting them drift closer *releases* energy: the curve runs downhill. **Pushed too close**, their electron clouds **repel** fiercely, so the energy rockets back up: the steep wall on the left. Where the two balance sits a **minimum**, the comfortable separation $r_0$ — the floor of the well. A molecule with little energy just rocks back and forth across that floor, and *that is what it means to be bound* in a solid or liquid.

So what gets a molecule back **out**? The attraction is strong but **finite** — it holds the molecule by only the **depth of the well**. Give a molecule that much energy and it can climb the far slope all the way up to $E_p \approx 0$, where it no longer feels its neighbours: it has broken free. Melting and boiling *are* this escape, happening to molecule after molecule — and here is the crucial part: while bonds are breaking, the heat you supply goes **entirely into the climb** (raising potential energy) with **none** left over to speed the molecules up (raise kinetic energy, and so temperature). That is why the thermometer sits still. The hidden, temperature-less energy bill for the escape is the **latent** ("hidden") heat.

![[latent-heat-potential-well.svg|697]]

The animation traces one molecule through that escape: trapped and jiggling at the floor (solid), hauled partway up the wall (liquid), then all the way out to $E_p \approx 0$ (gas). The *height* it climbs is the latent heat — and notice that its speed, and so the temperature, never changes along the way.

This is why **vaporisation costs far more than fusion** ($L_v \gg L_f$): melting only *loosens* the lattice (the molecules stay in contact, climbing partway up the well), while boiling *fully separates* the molecules (climbing all the way out, to $E_p \approx 0$). For water, $L_f = 334\,\text{kJ kg}^{-1}$ but $L_v = 2260\,\text{kJ kg}^{-1}$ — nearly seven times more. It is also why a steam burn is so much worse than a hot-water burn: condensing steam dumps that entire $2260\,\text{kJ kg}^{-1}$ into your skin before the water has even begun to cool.

## The heating curve — the whole story in one graph

![[specific-heat-heating-curve.svg|640]]

Take a block of ice well below freezing and heat it at a steady rate, plotting temperature against energy supplied. The curve has **five segments**, alternating between the two channels:

1. **sloped** — warming the ice ($Q = mc_{\text{ice}}\Delta T$); slope $= 1/(mc_{\text{ice}})$,
2. **flat** — melting at $0\,^\circ\text{C}$ ($Q = mL_f$); temperature constant,
3. **sloped** — warming the water; gentler slope, because water's $c$ is large,
4. **flat** — boiling at $100\,^\circ\text{C}$ ($Q = mL_v$); a long plateau, because $L_v$ is huge,
5. **sloped** — superheating the steam.

The **slopes** are specific heat (steeper = smaller $c$); the **plateaus** are latent heat (longer = larger $L$). Read off the physics directly: the boiling plateau dwarfs the melting plateau because $L_v \gg L_f$, and the water segment is shallower than the ice segment because liquid water's $c$ is more than double ice's.

## Why water is the strangest coolant on Earth

Water's specific heat capacity, $c = 4200\,\text{J kg}^{-1}\text{K}^{-1}$, is enormous — about **five times** iron's ($450$) and ten times copper's ($385$). The reason is **hydrogen bonding**: water molecules are stitched into a shifting network of hydrogen bonds, and a large share of any energy you add goes into jostling and partly breaking that network rather than into raising molecular speed. More energy per kelvin to store $\Rightarrow$ a bigger $c$.

![[hydrogen-bond-network.svg|697]]

Each water molecule can hydrogen-bond to **four** neighbours (the dashed amber links above) — a far stiffer, more connected web than the simple molecular jostling of most liquids. Heating water means fighting that web as well as speeding the molecules up, and the web soaks up the lion's share. That single anomaly has outsized consequences:

- **Oceans run the climate.** Water's huge $c$ (and vast mass) lets the seas absorb and release colossal amounts of energy with small temperature swings, smoothing the planet's seasons and giving coastal regions their mild climates while inland deserts swing wildly between day and night.
- **You are water-cooled.** The body carries heat in its blood (mostly water) and dumps it by **sweating** — exploiting water's gigantic $L_v$ ($2260\,\text{kJ kg}^{-1}$), so evaporating even a little sweat removes a lot of heat. Car engines and power stations use water as coolant for the same reason.

![[specific-heat-comparison.svg|560]]

## Calorimetry — the method of mixtures

When a hot body and a cold body are placed in thermal contact, energy flows from hot to cold until they reach a common temperature — **thermal equilibrium**. If the container loses no energy to its surroundings, energy conservation gives the workhorse of the school lab, the **method of mixtures**:

$$\text{energy lost by the hot body} = \text{energy gained by the cold body}.$$

Equating $mc\,\Delta T$ terms lets you solve for an unknown $c$, an unknown mass, or the final temperature. (The honest caveat — heat leaks to the surroundings, and the container itself absorbs some energy — is why real calorimeters are insulated and why the container's own heat capacity often has to be included.)

## Worked Examples

**Example 1 — Warming water (9702 §14.3 / 0625 §2.2).** How much energy heats $0.50\,\text{kg}$ of water from $20\,^\circ\text{C}$ to $100\,^\circ\text{C}$? ($c_{\text{water}} = 4200\,\text{J kg}^{-1}\text{K}^{-1}$.)
$$Q = mc\,\Delta T = (0.50)(4200)(80) = 1.7\times10^5\,\text{J} \;(168\,\text{kJ}).$$

**Example 2 — Then boiling it away (latent heat).** How much *additional* energy turns all that $100\,^\circ\text{C}$ water into steam? ($L_v = 2.26\times10^6\,\text{J kg}^{-1}$.)
$$Q = mL_v = (0.50)(2.26\times10^6) = 1.1\times10^6\,\text{J} \;(1130\,\text{kJ}).$$
Boiling the water away takes **almost seven times** the energy that heating it from 20 °C to boiling did — the latent-heat plateau is enormous.

**Example 3 — Method of mixtures (IB B.1.2).** A $0.20\,\text{kg}$ block of copper ($c = 385$) at $200\,^\circ\text{C}$ is dropped into $0.30\,\text{kg}$ of water ($c = 4200$) at $18\,^\circ\text{C}$, in an insulated cup. Find the final temperature $T$.
*Heat lost by copper = heat gained by water:*
$$m_{\text{Cu}}c_{\text{Cu}}(200 - T) = m_{\text{w}}c_{\text{w}}(T - 18)$$
$$(0.20)(385)(200 - T) = (0.30)(4200)(T - 18)$$
$$77(200 - T) = 1260(T - 18) \;\Longrightarrow\; 15400 - 77T = 1260T - 22680$$
$$38080 = 1337T \;\Longrightarrow\; T \approx 28\,^\circ\text{C}.$$
The water barely warms — its large $c$ and mass dominate the copper.

**Example 4 — Heat capacity of a gas from degrees of freedom (AP-2 / college).** How much energy raises the temperature of $2.0\,\text{mol}$ of helium (monatomic) by $50\,\text{K}$ **at constant volume**, and how does it compare with nitrogen (diatomic)?
$$Q_{\text{He}} = nC_V\Delta T = n\big(\tfrac{3}{2}R\big)\Delta T = (2.0)(\tfrac{3}{2})(8.31)(50) \approx 1.2\times10^3\,\text{J}.$$
For nitrogen, $C_V = \tfrac{5}{2}R$, so $Q_{\text{N}_2} = \tfrac{5}{3}Q_{\text{He}} \approx 2.1\times10^3\,\text{J}$ — the diatomic gas needs $\tfrac{5}{3}\times$ as much, because rotation gives it two more pockets to fill.

## Common Misconceptions

### 1. "Heat capacity is the same as temperature"
Temperature is the *state* of the substance (the average molecular KE); heat capacity is *how much energy it takes to change* that state. A bathtub of warm water and a spark have very different temperatures and very different heat capacities — independent quantities.

### 2. "Boiling water gets hotter the longer you heat it"
At a fixed pressure, boiling water stays at $100\,^\circ\text{C}$ no matter how hard you heat it. Extra energy makes it boil **faster** (more mass converted per second, $Q = mL_v$), not hotter. Turning the hob to maximum cooks pasta no faster once the water is boiling — it just wastes energy as steam.

### 3. "Latent heat raises the temperature"
The opposite: latent heat is exactly the energy that does **not** raise the temperature. During a phase change every joule goes into potential energy (breaking bonds), so the thermometer sits still until the change is complete.

### 4. "A bigger object has a bigger specific heat capacity"
Specific heat capacity is **intensive** — a property of the material, per kilogram. A swimming pool and a cup of the same water have the same *specific* heat capacity $c$; what differs is the **heat capacity** $C = mc$, the extensive total. Confusing $c$ with $C$ is the classic slip.

### 5. "All substances need the same energy to heat up"
Specific heat capacities vary by more than an order of magnitude — water $4200$, aluminium $900$, iron $450$, copper $385$, lead $130$ ($\text{J kg}^{-1}\text{K}^{-1}$). This is why a metal spoon in hot soup scalds your hand long before the soup cools, and why lead shot warms almost instantly while the same energy barely nudges water.

## Exam Notes

### Cambridge 9702 (A-Level Physics) — §14.3
The core home. Define and use **specific heat capacity** ($Q = mc\Delta T$) and **specific latent heat** of fusion and vaporisation ($Q = mL$); explain, in molecular terms, why melting and boiling occur at constant temperature (energy raises molecular PE, not KE). The **electrical method** for measuring $c$ (a heater of known power $P$ for time $t$ delivers $Q = Pt = mc\Delta T$) and the **method of mixtures** are standard practical questions; the heat lost to surroundings is the expected source of systematic error. The gas $C_V$/$C_p$ split is **not** required at 9702 (it belongs to §16 thermodynamics and beyond) but the molecular reasoning here sets it up.

### Cambridge 0625 (IGCSE Physics) — §2.2 (Extended)
$Q = mc\Delta T$ and (Extended) specific latent heat $Q = mL$; the particle explanation of constant-temperature melting and boiling; simple experiments to measure $c$. Thermal expansion, thermometers (the rest of §2.2) and conduction/convection/radiation (§2.3) are separate topics.

### IB Physics — Theme B (B.1.2)
**Thermal energy transfer** between bodies to a common temperature; **phase change at constant $T$**; **specific heat capacity** $c$ and **specific latent heat** $L$ (fusion and vaporisation), with $Q = mc\Delta T$ and $Q = mL$. HL builds the molecular picture (the constant-$T$ plateau as molecular PE) on the [[Internal Energy]] foundation. (Conduction, convection and radiation are B.1.3 — a later card.)

### AP Physics 2 — Unit 9 (§9.5, specific-heat half)
$Q = mc\Delta T$ and latent heat; the heating curve; calorimetry by energy conservation. AP often writes molar heat capacities for gases ($C_V = \tfrac{3}{2}R$ monatomic, $\tfrac{5}{2}R$ diatomic) and expects the constant-volume-vs-constant-pressure distinction. (The **thermal-conductivity** half of §9.5 — conduction, $H = kA\,\Delta T/L$ — is a separate strand, pending a conduction card.)

## Why Specific Heat Matters — College and Beyond

The deepest surprise is that **heat capacity is not even constant** — it *changes with temperature*, because a molecule's degrees of freedom switch on one at a time as it warms. Each mode that "unfreezes" adds its own step to $C_V$:

![[heat-capacity-staircase.svg|620]]

A cold hydrogen molecule can only translate ($C_V = \tfrac32 R$); warm it past ~100 K and rotation switches on ($\tfrac52 R$); only in the thousands of kelvin does the bond's vibration unfreeze ($\tfrac72 R$). Below each threshold the mode is **quantum-locked** — there isn't enough thermal energy ($kT$) to reach its first quantum level, so it stores nothing. This staircase is invisible to classical physics, and explaining it was one of quantum theory's first triumphs.

> [!info] Beyond syllabus — Dulong–Petit, the quantum collapse of heat capacity, and water's anomalies
> **Dulong–Petit law.** Treat a solid as a lattice of atoms each vibrating in 3 directions; each vibration is *two* quadratic degrees of freedom (kinetic + potential, like a spring), so $f = 6$ per atom and equipartition predicts a **molar** heat capacity $C = \tfrac{6}{2}R = 3R \approx 25\,\text{J mol}^{-1}\text{K}^{-1}$ for *every* solid. Astonishingly, most metals at room temperature obey this (Dulong and Petit, 1819) — copper, iron, lead, gold all cluster near $3R$ per mole, even though their *specific* (per-kg) heats differ wildly because their atoms differ in mass.
>
> **The quantum collapse.** Cool a solid toward absolute zero and its heat capacity does **not** stay at $3R$ — it falls to **zero**, as $T^3$. Classical equipartition cannot explain this; the resolution is quantum (Einstein 1907, Debye 1912): vibrational modes are quantised and **freeze out** when $kT$ drops below their quantum spacing, exactly as the rotational and vibrational modes of a gas freeze out in [[Internal Energy]]. A heat capacity that vanishes at $T=0$ is also a face of the **third law of thermodynamics**. Explaining the heat capacity of cold solids was one of the first hard wins for quantum theory.
>
> **Mayer and the first law.** $C_p - C_V = R$ is the cleanest possible appetiser for the [[First Law of Thermodynamics]]: the difference between heating at constant pressure and constant volume *is* the work of expansion, $W = R\,\Delta T$ per mole. Everything in this card is $\Delta U = Q$ (at constant volume) or $\Delta U = Q - W$ (otherwise) waiting to be named.
>
> **Water, again.** Hydrogen bonding makes water a thermodynamic outlier across the board — the highest $c$ of any common liquid, one of the highest $L_v$, *and* the famous expansion-on-freezing that makes ice float and lets fish survive winter. The same network that stores so much energy per kelvin is what life, and climate, are built around.

## Connections

- **Parent:** [[Internal Energy]] — specific heat is internal energy per kelvin made measurable; $C_V = \tfrac{f}{2}R$ is the degrees-of-freedom promise paid, and latent heat is the potential-well's $\Delta E_p$ given a name.
- **Prerequisites:** [[Internal Energy]] (the KE/PE split that becomes specific heat vs latent heat), [[Kinetic Theory and the Ideal Gas]] (temperature as molecular KE; the ideal-gas $U$).
- **Components:** specific heat capacity $c$ ($Q=mc\Delta T$); specific latent heat $L$ ($Q=mL$); molar heat capacities $C_V=\tfrac{f}{2}R$, $C_p = C_V + R$.
- **Extensions:** [[First Law of Thermodynamics]] ($\Delta U = Q + W$; $C_p - C_V = R$ is the work of expansion) — the next card.
- **Cross-domain — mechanics:** [[Hooke's Law for Springs]] (each atomic vibration is a spring with two quadratic degrees of freedom — the root of the Dulong–Petit $3R$), [[Simple Harmonic Motion]] (those lattice vibrations).
- **Story partner:** [[Stories/Boltzmann's Tombstone]] — the equipartition that fixes $C_V$, and its quantum failure at low $T$, are statistical mechanics in action.
- **For 9702 / A-Level Physics students:** $c$, $L$, $Q=mc\Delta T$ and $Q=mL$ are on the data-and-formulae sheet's adjacent territory; the molecular *explanation* of the constant-temperature plateau is the bookwork most often examined.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $Q = mc\,\Delta T$ | `Q = mc\,\Delta T` | Energy to change temperature by $\Delta T$ |
| $Q = mL$ | `Q = mL` | Energy to change phase at constant $T$ |
| $c$ | `c` | Specific heat capacity, $\text{J kg}^{-1}\text{K}^{-1}$ |
| $C = mc$ | `C = mc` | Heat capacity of an object, $\text{J K}^{-1}$ |
| $L_f,\ L_v$ | `L_f,\ L_v` | Specific latent heat of fusion / vaporisation |
| $C_V = \tfrac{f}{2}R$ | `C_V = \tfrac{f}{2}R` | Molar heat capacity at constant volume |
| $C_p = C_V + R$ | `C_p = C_V + R` | Mayer's relation (per mole) |
| $\gamma = C_p/C_V$ | `\gamma = C_p/C_V` | Adiabatic index (ratio of heat capacities) |
