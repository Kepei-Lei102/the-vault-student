---
chinese: 密度与压强 (mìdù yǔ yāqiáng)
prerequisites:
  - "[[Newton's Laws of Motion]]"
  - "[[Forces and Equilibrium]]"
  - "[[Physical Quantities and Units]]"
  - "[[Error Propagation]]"
leads_to:
  - "[[Kinetic Theory and the Ideal Gas]]"
  - "[[Drag and Terminal Velocity]]"
  - "[[Braking Systems]]"
  - "[[Archimedes and the Soldier]]"
  - "[[Sound]]"
  - "[[The Solar System]]"
tags:
  - subject/physics
  - domain/fluids
  - domain/mechanics
  - level/IGCSE
  - level/A-Level
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/AP-Physics-1
  - syllabus/9702-4-3
  - syllabus/0625-1-4
  - syllabus/0625-1-8
  - syllabus/AP-Physics-1-8-1
  - syllabus/AP-Physics-1-8-2
  - syllabus/AP-Physics-1-8-3
  - syllabus/AP-Physics-1-8-4
  - type/deep
  - type/definition
  - type/proof
  - notation/rho-density
  - notation/p-pressure
  - misconception/pressure-has-a-direction
  - misconception/upthrust-grows-with-depth
  - misconception/heavy-things-sink
  - misconception/wide-tanks-press-harder
  - misconception/equal-transit-time-lift
---

# Density and Pressure 密度与压强

## Definition

### Formal

**Density** (密度) is mass per unit volume, $\rho = m/V$, in $\text{kg m}^{-3}$: a property of the *material*, not of the piece. **Pressure** (压强) is the normal force per unit area, $p = F/A$, in pascals ($1\ \text{Pa} = 1\ \text{N m}^{-2}$): a *scalar*, with no direction of its own, which makes a force on any surface it meets, at right angles to that surface.

In a fluid at rest the pressure rises with depth because each layer carries the weight of all the fluid above it. From the two definitions,

$$\Delta p = \rho\,g\,\Delta h,$$

the **hydrostatic pressure** difference between two points a height $\Delta h$ apart. And because the bottom of any submerged object is deeper than its top, the fluid pushes up on the bottom harder than it pushes down on the top; the difference is the **upthrust** (浮力), and it equals the weight of the fluid the object displaces:

$$F = \rho_{\text{fluid}}\,g\,V \qquad\text{(Archimedes' principle)}.$$

An object floats when its own weight can be matched by the upthrust from a *part* of its volume — that is, when its average density is less than the fluid's.

### Intuitive

Dive to the bottom of a three-metre pool and your ears hurt. Nothing is pressing on your ears but water, and the water is not squeezing you on purpose; it is simply being pressed down by the water above it, and it presses back on everything — including sideways and upwards, which is why a bubble you let go rises. Every extra ten metres of water is another whole atmosphere of push.

Put an ice cube in a glass. It floats with about a tenth showing. Put a steel spoon in and it goes straight to the bottom. Yet a container ship — a hundred thousand tonnes of steel — floats. What decides is not the material but the *average density of the whole shape, air included*: the ship's hull encloses so much air that ship-plus-air is lighter than the water it pushes aside. Watch the pressure grow with depth, the block feel more push on its bottom than on its top, and the same steel sink as a cube and float as a hull:

![[density-pressure-manim.mp4]]

### 中文锚点

**密度 (mìdù)** = 单位体积的质量，$\rho = m/V$，是**材料**的性质而不是某一块东西的性质。**压强 (yāqiáng)** = 单位面积上受到的垂直压力，$p = F/A$，单位帕斯卡；它是一个**标量**，本身没有方向，却会对碰到的任何表面产生垂直于该表面的力。

潜到三米深的泳池底，耳朵会疼。压你耳朵的只有水，而水并不是在故意挤你——它只是被**上面的水压着**，于是也朝各个方向压回去——朝侧面、朝上都是，所以你松开的气泡会往上跑。每往下十米，就多整整一个大气压。往杯子里放一块冰，它浮着，露出大约十分之一；放一把钢勺，直接沉底。可一艘十万吨钢铁的集装箱船却浮在海上——决定沉浮的不是**材料**，而是**整个形状连同里面空气的平均密度**：船壳裹住了那么多空气，"船加空气"比它排开的水轻。这张卡的三个等式一脉相承：**静水压强** $\Delta p = \rho g \Delta h$ 是把液柱切成薄片、一层层加上重量得来的（这张卡真的用十万片算了一遍）；**浮力** $F = \rho g V$ 不是新定律，只是同一条式子分别用在物体的底面和顶面——底面更深、被推得更狠，差值就是浮力，而且跟物体浸在多深没有关系；**漂浮**则是浮力和重力的平衡，物体下沉到"排开的水恰好和自己一样重"为止。所以海里的冰山露出 11%，肺里吸满气的人只露出 2%，热气球靠的是热空气比冷空气轻。压强不看容器的宽窄——只看深度和密度，这是很多人第一次听时不肯信的一点。

| English | 中文 | Symbol / idea |
|---|---|---|
| Density | 密度 (mìdù) | $\rho = m/V$, $\text{kg m}^{-3}$ |
| Pressure | 压强 (yāqiáng) | $p = F/A$, Pa; a scalar |
| Hydrostatic pressure | 静水压强 (jìngshuǐ yāqiáng) | $\Delta p = \rho g \Delta h$ |
| Atmospheric pressure | 大气压 (dàqìyā) | $p_0 \approx 1.01 \times 10^5$ Pa, about 10 m of water |
| Gauge / absolute pressure | 表压 / 绝对压强 | above atmospheric / above vacuum |
| Upthrust (buoyant force) | 浮力 (fúlì) | $F = \rho_{\text{fluid}} g V_{\text{submerged}}$ |
| Archimedes' principle | 阿基米德原理 | upthrust = weight of fluid displaced |
| Displacement (volume) | 排水法 (páishuǐ fǎ) | measuring an irregular solid's volume |
| Continuity | 连续性方程 | $A_1 v_1 = A_2 v_2$ |
| Bernoulli's equation | 伯努利方程 | $p + \tfrac12\rho v^2 + \rho g h$ constant |

---

## Part I — Density: the material, not the piece

Cut a gold bar in half and each half has half the mass and half the volume; the ratio is untouched. That is what makes density a fingerprint: $19\,300\ \text{kg m}^{-3}$ is gold whether it is a ring or an ingot, and Archimedes' famous test of the crown was a density test — the same mass of gold and of gold-and-silver displace different volumes of water ([[Archimedes and the Soldier]] tells what became of him).

**Measuring it** is the 0625 practical: mass on a balance every time; volume by *shape* for a regular solid (a cube's side cubed), by *reading* for a liquid (a measuring cylinder, and subtract the empty cylinder's mass), and by **displacement** for an irregular solid that sinks — drop it into a measuring cylinder of water, and the rise in the reading *is* its volume, because it pushes aside exactly its own volume of water. The A-Level version adds the uncertainty: the November 2023 question gives a cylinder's $D$, $L$ and $M$ with their errors and asks for the density *and* its percentage uncertainty, which is [[Error Propagation]]'s product-and-power rule — $D$ appears squared, so its percentage error counts twice.

**Floating from density data** needs no calculation: an object whose density is less than the liquid's floats; one whose density is greater sinks; and two liquids that do not mix layer with the denser below (oil on water, water on mercury — the syllabus's Supplement line). Part IV says *why*.

| Material | $\rho$ / kg m$^{-3}$ | | Material | $\rho$ / kg m$^{-3}$ |
|---|---|---|---|---|
| air (sea level, 15 °C) | 1.2 | | ice | 917 |
| cork | 240 | | fresh water (4 °C) | 1000 |
| oak | 750 | | sea water | 1025 |
| petrol | 720 | | human body (lungs full) | ≈ 985 |
| olive oil | 910 | | steel | 7 900 |
| the Sun (mean) | 1 410 | | mercury | 13 600 |

Water is the reference: $1\ \text{g cm}^{-3}$, which is $1000\ \text{kg m}^{-3}$ — the unit conversion every paper sets a trap with. A gram per cubic centimetre is a thousand kilograms per cubic metre, because a cubic metre holds a *million* cubic centimetres and a kilogram is only a thousand grams.

---

## Part II — Pressure: force spread over area

A nail goes into wood and a thumb does not, with the same push: the nail's point puts the force on a tiny area, and it is the force *per area* that the wood must resist. Snowshoes, tractor tyres and a polar bear's paws spread weight to lower the pressure; knives, needles and studs concentrate it. The March 2026 IGCSE question asks for exactly this — a polar bear's weight divided by the area of its paws, then a comparison with a person.

Three things about pressure that separate the A grade:

- **It is a scalar.** A pressure of $10^5$ Pa at a point is not "downwards"; it is a number. What has a direction is the *force* the pressure produces on a surface, and that force is always normal to the surface — which is why the pressure in a fluid pushes *up* on the underside of a boat and *sideways* on the wall of a dam.
- **In a fluid at rest it acts equally in all directions** at a point. If it did not, the fluid at that point would accelerate sideways, and it is at rest.
- **The atmosphere is a fluid too.** The air above every square metre of ground weighs about ten tonnes, so it presses with $1.01 \times 10^5$ Pa on everything — including you, from all sides, which is why you do not notice. Remove it from one side and you do: a sucker sticks, a straw works, and a can with the air pumped out crumples.

---

## Part III — Hydrostatic pressure: the weight of what is above you

![[density-pressure-column.svg|1000]]

The derivation the syllabus asks for is three lines. Take a vertical column of fluid of cross-section $A$ and height $\Delta h$. Its volume is $A\,\Delta h$, its mass $\rho A \Delta h$, its weight $\rho A \Delta h\, g$. The column is at rest, so the fluid beneath it pushes up with a force equal to the weight of the column plus whatever pushes down on its top. Pressure is force over area, so

$$p_{\text{bottom}} A = p_{\text{top}} A + \rho A \Delta h\, g \quad\Longrightarrow\quad \boxed{\,\Delta p = \rho g \Delta h\,}.$$

$A$ cancelled. That is the fact people refuse to believe on first hearing: the pressure at the bottom of a lake does not depend on how wide the lake is, only on how deep, and a thin tube of water ten metres tall presses on its base exactly as hard as an ocean ten metres deep. `density-pressure-hydrostatic.py` builds the pressure at the bottom of the Challenger Deep from a hundred thousand slabs and gets $108$ MPa, about $1\,065$ atmospheres, the same as $\rho g h$ in one line.

Two readings of the number:

- **Ten metres of water is one atmosphere.** $1000 \times 9.81 \times 10 \approx 10^5$ Pa. A diver at 30 m is under four atmospheres in total (three of water, one of air); the *Titan* submersible that imploded in 2023 was at about 3 800 m, some 380 atmospheres, 38 MPa — the weight of a small car on every square centimetre.
- **Air is a fluid whose density falls as it thins.** Because $\rho \propto p$ for a gas at fixed temperature, the same slab-by-slab sum gives an exponential instead of a line: $p = p_0 e^{-h/H}$ with a scale height $H \approx 8.4$ km. The script integrates it and matches the closed form; the summit of Everest sits at $35$ kPa, a third of sea level, which is why climbers carry oxygen and water boils there at 70 °C.

**Gauge and absolute.** A tyre gauge reading $200$ kPa means $200$ kPa *above* the atmosphere; the absolute pressure inside is $300$ kPa. The two instruments on the next figure read the two kinds:

![[density-pressure-manometer.svg|1000]]

The U-tube **manometer** reads a *difference*: the gas on one side pushes its liquid surface down until the height difference $h$ of liquid balances it, $p - p_0 = \rho g h$. The mercury **barometer** is a manometer with a vacuum on one side, so its height reads the absolute atmospheric pressure — $760$ mm of mercury, which is where the unit "mmHg" on a blood-pressure cuff comes from: a reading of 120/80 is a manometer height, in millimetres of mercury, of your blood's gauge pressure at the peak and trough of each heartbeat.

**Pascal's principle** is the same equation with $\Delta h$ negligible: a pressure applied to an enclosed fluid is transmitted undiminished to every part of it. Push a small piston with force $F_1$ on area $A_1$, and a large piston of area $A_2$ in the same fluid pushes out with $F_2 = F_1 A_2/A_1$. That multiplication is a car's hydraulic brakes ([[Braking Systems]]), a mechanic's jack, and the reason a garage lift needs only a foot pump.

---

## Part IV — Upthrust: Archimedes without magic

![[density-pressure-upthrust.svg|1000]]

Archimedes' principle sounds like a separate law. It is not; it is Part III applied to the top and bottom of an object. Submerge a block of height $H$ and base area $A$ with its top at depth $h_1$. The fluid pushes down on the top with $p_1 A = \rho g h_1 A$ and up on the bottom with $p_2 A = \rho g (h_1 + H) A$. The sideways pushes on opposite faces are equal at every depth and cancel. The net force is upward:

$$F = \rho g (h_1 + H) A - \rho g h_1 A = \rho g\,(HA) = \rho g V.$$

The depth $h_1$ cancelled — **the upthrust does not depend on how deep the object is** — and $HA$ is the object's volume, so the upthrust equals the weight of fluid that would have filled the space the object occupies: *the weight of the fluid displaced*. Any shape can be cut into thin vertical columns and the same argument applied to each. `density-pressure-archimedes.py` computes the pressure force on every face of a cube at three depths, summing the sides strip by strip, and gets $78.48$ N every time — exactly $\rho g V$.

**Floating.** Lower an object of density $\rho_o$ into a fluid of density $\rho_f$. Fully submerged, the upthrust is $\rho_f g V$ and the weight is $\rho_o g V$: if $\rho_o > \rho_f$ it sinks; if $\rho_o < \rho_f$ the upthrust wins, it rises, and as it breaks the surface the submerged volume — and with it the upthrust — falls, until the submerged part displaces exactly its own weight:

$$\rho_f\, g\, V_{\text{sub}} = \rho_o\, g\, V \quad\Longrightarrow\quad \frac{V_{\text{sub}}}{V} = \frac{\rho_o}{\rho_f}.$$

Ice at $917$ in sea water at $1025$: $89\%$ under, the iceberg's famous nine-tenths. A person with lungs full, $985$: $98\%$ under, which is why floating on your back is possible and easy breathing is not. Oak, $75\%$. The steel cube, $7\,900$ against $1\,030$: sinks. The steel ship, hull plus the air inside it, average density a few hundred: floats, sitting at the depth where the hull displaces its full weight of water — the Plimsoll line on its side marks that depth, and marks it *higher* for fresh water than for salt, because fresh water is less dense and the ship must sink further to displace the same weight.

The same balance lifts a **hot-air balloon**: air at 100 °C has density $0.95$ against the surrounding $1.2\ \text{kg m}^{-3}$, so a $2\,500\ \text{m}^3$ envelope gets about $6.8$ kN of net lift, seven hundred kilograms for basket, burner and people. A **submarine** does it in reverse, flooding ballast tanks to raise its average density above the sea's and blowing them with compressed air to fall below it again. And an **airship** — the November 2023 question — floats in air the way a ship floats in water: the upthrust of $93$ kN on it is the weight of $7\,900\ \text{m}^3$ of the air it pushes aside.

> [!info] Why a submerged object's *apparent* weight is less
> Hang a stone on a newton-meter and lower it into water: the reading drops by $\rho_{\text{water}} g V$. Nothing happened to the stone's weight; the water is now carrying part of it. That drop *is* the upthrust, and dividing the stone's real weight by the drop gives the stone's density relative to water — the reading Archimedes needed for the crown.

---

## Part V — Fluids in motion: continuity and Bernoulli

![[density-pressure-venturi.svg|1000]]

Two more ideas, both bookkeeping, close the AP unit and explain the everyday things statics cannot.

**Continuity.** An incompressible fluid cannot pile up inside a pipe, so the volume passing every cross-section per second is the same: $A_1 v_1 = A_2 v_2$. Narrow the pipe and the fluid speeds up in the same ratio — thumb over the end of a hose, the water leaves faster.

**Bernoulli.** Follow a small parcel of fluid along a streamline and apply the work–energy theorem *per unit volume*. The pressure behind it does work $p_1$ per unit volume pushing it in; the pressure ahead does work $-p_2$ per unit volume as it pushes out; the difference is its gain in kinetic energy per volume, $\tfrac12\rho v^2$, plus its gain in gravitational potential energy per volume, $\rho g h$. So along the streamline,

$$p + \tfrac12\rho v^2 + \rho g h = \text{constant},$$

each term an energy per unit volume, each in pascals. Where the fluid is fast the pressure is low: that is the **Venturi effect**, and it drives the carburettor, the perfume atomiser, the chimney draught, and the reading of a Venturi meter, which measures flow rate from the pressure drop across a constriction. `density-pressure-bernoulli.py` runs a pipe that narrows and climbs, takes the speed from continuity and the pressure from Bernoulli at twenty stations, and prints the sum: constant to the last digit. Two corollaries fall out. **Torricelli**: water leaving a hole a depth $h$ below the surface of an open tank has $v = \sqrt{2gh}$, the speed of free fall through $h$, because at the surface $p = p_0$ and $v \approx 0$ and at the hole $p = p_0$ again. And the hose: a $15$ mm hose at $2\ \text{m s}^{-1}$ with a thumb leaving a $6$ mm gap sends the water out at $12\ \text{m s}^{-1}$.

Bernoulli's equation assumes steady, incompressible, non-viscous flow along one streamline. Real pipes lose pressure to friction and real wings are not explained by "the air over the top must arrive at the same time" — it does not, and the honest account of lift is in the misconceptions below.

---

## Where it earns its keep

- **The Plimsoll line, 1876.** Samuel Plimsoll's load line, painted on every merchant hull, is Part IV as maritime law: the ship may be loaded until the mark meets the water and no further, with separate marks for fresh water, tropical seas and the winter North Atlantic, because $\rho_f$ differs and so does how deep the same cargo sinks the ship. Overloaded "coffin ships" had been sinking with their crews for the insurance; the line ended it.
- **A diver's tables.** Every ten metres adds an atmosphere; at 30 m a diver breathes air at four atmospheres, dissolving four times the nitrogen into the blood. Surface too fast and it comes out as bubbles: decompression sickness. The tables are hydrostatics plus the gas laws of [[Kinetic Theory and the Ideal Gas]], and the first rule of diving — *never hold your breath on the way up* — is Boyle's law: air that filled the lungs at four atmospheres wants to be four times the volume at one.
- **Blood pressure.** 120/80 mmHg is a manometer reading, and it is why a giraffe needs a heart that generates 280 mmHg: its brain is two metres above that heart, and $\rho g \Delta h$ for two metres of blood is 150 mmHg that must be overcome before a drop reaches the head.
- **Hydraulics.** The excavator arm, the aircraft's landing gear, the car's brake pedal that stops two tonnes with a foot: Pascal's principle turning a small force on a small piston into a large force on a large one, at the price of moving the small piston further — [[Braking Systems]] has the pedal-to-caliper ratio.
- **Weather.** A barometer falling is the weight of the air column above you decreasing; the isobars on a forecast map are Part III drawn across a continent, and wind is air moving from high pressure to low.

---

## Worked examples — every tool named

### Example 1 — density with its uncertainty (Cambridge 9702, November 2023 Paper 23, Q1(b))

> *A uniform cylinder has diameter $D = (26.2 \pm 0.1)$ mm, length $L = (162 \pm 1)$ mm and mass $M = (247 \pm 1)$ g, with $\rho = 4M/(\pi D^2 L)$. (i) Calculate the percentage uncertainties in $D$ and $L$. [1] (ii) Calculate the density to three significant figures. [2] (iii) Calculate the percentage uncertainty in the density.* [2]

**(i) Tool: percentage uncertainty = absolute ÷ value.** $0.1/26.2 = 0.4\%$; $1/162 = 0.6\%$ [1]. **(ii) Tool: the given formula, in SI.** Trigger: millimetres and grams in the data, kilograms per cubic metre wanted. $\rho = 4 \times 0.247 / (\pi \times (26.2 \times 10^{-3})^2 \times 0.162) = 2.83 \times 10^3\ \text{kg m}^{-3}$ [C1 A1]. **(iii) Tool: [[Error Propagation]]'s product rule — powers multiply the percentage.** $\%\rho = \%M + 2\,\%D + \%L = 0.4 + 0.8 + 0.6 = 1.8\%$ [C1 A1]. The trap is the square: $D$ counts twice. The script recomputes both to the scheme's figures.

### Example 2 — the airship (Cambridge 9702, November 2023 Paper 23, Q3(b))

> *The upthrust on an airship is 93 000 N; the density of the surrounding air is 1.2 kg m$^{-3}$. (i) Calculate the volume of air displaced. [1] (ii) Fully loaded, the airship's weight exceeds the upthrust; the fans provide 3.0 kN upward for level flight. Calculate the mass of the airship.* [2]

**(i) Tool: $F = \rho g V$, rearranged.** Trigger: an upthrust and a fluid density given → the displaced volume is what is asked. $V = 93\,000/(1.2 \times 9.81) = 7\,900\ \text{m}^3$ [A1]. **(ii) Tool: equilibrium of three vertical forces, from [[Forces and Equilibrium]].** Trigger: "level flight" = no vertical acceleration. Weight $= $ upthrust $+$ fan force $= 93\,000 + 3\,000 = 96\,000$ N [C1]; $m = 96\,000/9.81 = 9\,800$ kg [A1]. A ship floats in air by the same equation it would in water.

### Example 3 — held under by a beam (Cambridge 9702, March 2025 Paper 22, Q2(b))

> *A cylinder of mass 11 kg and diameter 0.78 m is held with its bottom submerged to a depth $y$ by a beam pushing down with 1300 N; it is in equilibrium. (ii) Show that the upthrust is 1400 N. [1] (iii) The water's density is 990 kg m$^{-3}$. Calculate $y$.* [2]

**(ii) Tool: equilibrium — up equals down.** Upthrust $= 11 \times 9.81 + 1300 = 1\,408 \approx 1400$ N [A1]. **(iii) Tool: the upthrust as a pressure force on the base, $F = \rho g y A$.** Trigger: only the bottom face is under water, so the upthrust *is* the water pressure at depth $y$ times the base area. $y = 1400/(990 \times 9.81 \times \pi \times 0.39^2) = 0.30$ m [C1 A1]. The scheme also accepts $p = F/A = 2\,930$ Pa then $y = p/\rho g$ — the same two ideas in the other order. Notice that $F = \rho g V$ with $V = Ay$ is the identical calculation: Archimedes *is* the pressure on the base.

### Example 4 — a sphere in a liquid, and the liquid's density (Cambridge 9702, March 2022 Paper 22, Q1)

> *A sphere of radius 2.1 mm and weight $7.2 \times 10^{-4}$ N falls at constant velocity through a liquid; the upthrust on it is $4.8 \times 10^{-4}$ N and the viscous force is $F_V = krv$ with $k = 17$ in SI units. (a) Determine the base units of $k$. (b) Use the upthrust to calculate the density of the liquid. [3] (c)(ii) Determine the terminal velocity.* [2]

**(a) Tool: dimensional homogeneity, [[Physical Quantities and Units]].** $k = F/(rv)$: $\text{kg m s}^{-2} / (\text{m} \cdot \text{m s}^{-1}) = \text{kg m}^{-1}\text{ s}^{-1}$. **(b) Tool: $F = \rho g V$ with a sphere's volume.** $V = \tfrac43\pi(2.1 \times 10^{-3})^3 = 3.88 \times 10^{-8}\ \text{m}^3$; $\rho = 4.8 \times 10^{-4}/(9.81 \times 3.88 \times 10^{-8}) = 1\,300\ \text{kg m}^{-3}$ [C1 C1 A1]. **(c)(ii) Tool: constant velocity → forces balance.** Trigger: "constant velocity" is the whole hint. $F_V = W - U = 2.4 \times 10^{-4}$ N; $v = F_V/(kr) = 2.4 \times 10^{-4}/(17 \times 2.1 \times 10^{-3}) = 6.7 \times 10^{-3}\ \text{m s}^{-1}$ [C1 A1]. The rest of that story — why the viscous force grows with speed until it balances — is [[Drag and Terminal Velocity]]'s.

### Example 5 — a window, a pressure difference, a vacuum tube (Cambridge 0625, March 2021 Paper 42, Q1)

> *A glass pane 2.0 cm thick and 0.15 m$^2$ in area has density $2.6 \times 10^3$ kg/m$^3$. (a) Calculate its weight. [3] (b) As an aquarium window, the outside pressure is $1.0 \times 10^5$ Pa and the average inside pressure $1.3 \times 10^5$ Pa. Calculate the resultant force on the window and state its direction. [4] (c) A vacuum pump reduces the pressure above a 12 m column of liquid to zero; the pressure at the base of the column is $9.6 \times 10^4$ Pa. Calculate the liquid's density.* [3]

**(a) Tool: $m = \rho V$ then $W = mg$ with $g = 10$** (IGCSE's value). $m = 2600 \times 0.02 \times 0.15 = 7.8$ kg; $W = 78$ N [C1 C1 A1]. **(b) Tool: force from a pressure *difference*, $F = \Delta p\,A$.** Trigger: two pressures on one pane — only the difference pushes. $\Delta p = 3 \times 10^4$ Pa; $F = 4.5 \times 10^3$ N, **outwards** [C1 C1 A1 B1]. **(c) Tool: $p = \rho g h$ with $p_0 = 0$ above.** Trigger: "reduces the pressure above the column to zero" removes the atmosphere from the equation. $\rho = 9.6 \times 10^4/(10 \times 12) = 800\ \text{kg m}^{-3}$ [C1 C1 A1] — a light oil.

### Example 6 — why the ship floats (Cambridge 0625, March 2026 Paper 42, Q2(a))

> *Steel has density 7900 kg/m$^3$. (ii) Calculate the volume of a solid steel cube of mass 110 kg. [1] (iii) Sea water has density 1030 kg/m$^3$. State why the cube sinks. [1] (iv) Explain why a steel ship floats.* [2]

**(ii) Tool: $V = m/\rho$.** $0.014\ \text{m}^3$ [B1]. **(iii) Tool: compare densities.** Steel is denser than sea water [B1]. **(iv) Tool: average density of the whole shape.** The ship's volume includes a great deal of air, which lowers the *average* density of ship-plus-air [B1] below that of sea water [B1]. The scheme wants both halves: the air, and the comparison. The second scene of the clip above is this question.

### Example 7 — the best question from another board: the swimmer's block (AP Physics 1, 2025 Free Response Q4)

> *A swimmer releases a block of mass $m$ from rest, fully submerged, first in fresh water (density $\rho_1$) and then in salt water ($\rho_2 > \rho_1$); it accelerates upward with $a_1$ and $a_2$. (A) Is $a_1$ greater than, less than or equal to $a_2$? Justify in terms of all forces, qualitatively. (B) Starting from Newton's second law, derive the initial upward acceleration $a$ of a block of mass $m$ and volume $V$ submerged in a fluid of density $\rho$. (C) Is your expression consistent with your claim in A?*

**(A) Tool: Part IV — upthrust $\propto \rho_f$, weight the same.** The weight $mg$ is identical in both tanks; the upthrust $\rho V g$ is larger in salt water; so the net upward force, and the acceleration, is larger: $a_1 < a_2$ [3 points: identifies the forces, same weight, larger buoyant force in salt water]. **(B) Tool: [[Newton's Laws of Motion]] with the upthrust substituted.** $\sum F = ma$: $\rho V g - mg = ma$, so $a = \rho V g/m - g$ [B1 for N2, B2 for $\rho V g$, B3 for the expression]. **(C) Tool: functional dependence.** $a$ increases with $\rho$ through the $\rho V g/m$ term, consistent with A [C1 C2]. What this question tests that Cambridge's do not is the *reasoning* — the scoring guidelines award the point for saying *proportional to the density*, not for the number.

---

## Hands-on

1. **Density of a key.** Kitchen scale for the mass; a measuring jug with water for the volume by displacement (read the rise). Steel or brass? The table above decides. Then a potato, which floats or sinks depending on the variety, and an egg — fresh sinks, old floats, and salt in the water makes both float, all Part IV.
2. **Make a manometer.** A metre of clear tubing bent into a U, half filled with water, taped to a ruler. Blow gently into one end and read $h$; $\rho g h$ is your lung's gauge pressure — a few kilopascals, a few per cent of an atmosphere. Then put the open end at the bottom of a jug of water and watch $h$ track the depth.
3. **Ten metres in a bottle.** Tie a balloon over a bottle with a hole low on its side, fill it, and measure how far the jet reaches from holes at two heights: Torricelli says the speed goes as $\sqrt{h}$.
4. **Run the three scripts.** Change the cube's depth in `density-pressure-archimedes.py` and watch the upthrust refuse to change; change the fluid to mercury and watch the steel float; run the atmosphere in `density-pressure-hydrostatic.py` with a warmer $T$ and see the scale height grow.

---

## Common Misconceptions (Teaching Notes)

### 1. "Pressure acts downwards"

Pressure is a scalar; at a point in a fluid it is the same in every direction, and the force it makes is perpendicular to whatever surface is there — upward on the bottom of a boat, sideways on a dam. Only the *weight* that causes it acts downwards.

### 2. "Upthrust increases with depth"

The pressure on the top and bottom both increase with depth; their *difference* does not, because it depends only on the object's height. A submerged object feels the same upthrust one metre down and a hundred metres down (until the water's compressibility matters, see Beyond Syllabus). `density-pressure-archimedes.py` shows $78.48$ N at three depths.

### 3. "Heavy things sink, light things float"

An aircraft carrier is heavier than a pebble and floats. Density decides, and for a hollow object the *average* density of the whole shape including its air. A kilogram of steel sinks; the same kilogram beaten into a bowl floats.

### 4. "A wider tank presses harder on its base" / "the pressure depends on the amount of water"

$\Delta p = \rho g \Delta h$: only depth and density. A narrow tube and a wide lake of the same depth press equally on their floors — the hydrostatic paradox — and a dam is built thicker at its base for the same reason it is not built thicker for a bigger reservoir.

### 5. "The air over a wing goes faster because it must meet the air underneath at the trailing edge"

It does not meet it; the air over the top arrives *earlier*. The equal-transit-time story is false, and Bernoulli applied to it gives the wrong lift. Lift is real and Bernoulli holds along real streamlines, but the speed difference comes from the wing turning the airflow downward — Newton's third law and circulation, not a race to the trailing edge.

### 6. "g = 9.81 in every paper"

0625 uses $g = 10\ \text{N kg}^{-1}$ and its schemes are computed with it (Example 5); 9702 uses $9.81$. Using the wrong one costs the answer mark on a "show that".

---

## Exam Notes

### Cambridge 9702 (§4.3 — AS Paper 2, and Paper 1 multiple choice)

- **Six learning objectives:** define and use density; define and use pressure; *derive* $\Delta p = \rho g \Delta h$ from the two definitions (Part III's three lines — learn them, it is a 2–3 mark question); use it; understand that upthrust is due to a difference in hydrostatic pressure (Part IV's argument, in words); calculate upthrust with $F = \rho g V$.
- **Formula sheet:** $\Delta p = \rho g \Delta h$ and $F = \rho g V$ **are printed**; $\rho = m/V$ and $p = F/A$ are not, and are asked as definitions ("mass per unit volume", "force per unit area — normal to the surface").
- **Question shapes:** density from measured dimensions with its percentage uncertainty (November 2023 — the square counts twice); a floating or held object in equilibrium where the upthrust is one of three forces (March 2025's beam, November 2023's airship with fans); an object at terminal velocity with weight, upthrust and viscous force (March 2022); pressure differences across a surface; the derivation itself. Always $g = 9.81$.

### Cambridge 0625 (§1.4 Density, §1.8 Pressure — Papers 2 and 4; the density experiment in Paper 6)

- **§1.4 Core:** define density; recall and use $\rho = m/V$; *describe* how to determine the density of a liquid, a regular solid and an irregular solid that sinks (displacement), with the calculations; predict floating from density data. **Supplement:** whether one liquid floats on another (denser below).
- **§1.8 Core:** define pressure; recall and use $p = F/A$; everyday examples of force and area (the polar bear's paws, March 2026); *qualitatively*, how pressure beneath a liquid surface changes with depth and density. **Supplement:** recall and use $\Delta p = \rho g \Delta h$. The 2026–28 syllabus does not name barometers and manometers; they remain the natural context and Part III's figure is worth knowing.
- **Question shapes:** weight from density and dimensions; force from a pressure *difference* on a window (March 2021); density from a vacuum-topped column; the steel-cube-versus-ship explanation (March 2026) — say *air* and *average density*; $\Delta p$ for a stated depth of sea water. Always $g = 10$.

### AP Physics 1 (Unit 8 Fluids, 10–15 % of the exam)

- **8.1** density and the internal structure of fluids; **8.2** pressure, $P = P_0 + \rho g h$, gauge versus absolute, Pascal's principle; **8.3** buoyancy and Newton's laws — $F_b = \rho V g$ inside $\sum F = ma$; **8.4** conservation laws — continuity $A_1 v_1 = A_2 v_2$ and Bernoulli's equation. All four equations are on the AP equation sheet.
- AP asks for *reasoning*: the 2025 Q4 awards its points for identifying that the weight is unchanged and the buoyant force scales with density, for starting a derivation from Newton's second law, and for reading the functional dependence off the result. Write the argument, not just the number.

### Where it is *not* examined

- **9709 and 9231:** no fluids; density appears only as a word in mechanics questions.
- **IB Physics (2025):** density is defined in B.1.1 and buoyancy is named as a contact force in A.2.2, but hydrostatic pressure, Archimedes and Bernoulli are not examined.
- **AP Physics 2 (2025 redesign):** fluids moved *out* of Physics 2 into Physics 1; only the thermodynamic pressure of a gas remains.

---

## Connections

- **Parents:**
   - [[Newton's Laws of Motion]] — every upthrust problem is $\sum F = ma$ with one more force in the list.
   - [[Forces and Equilibrium]] — the three-force balance of the airship and the held cylinder.
   - [[Physical Quantities and Units]] — the units of $k$ in Example 4; pascals as newtons per square metre; the $\text{g cm}^{-3}$ trap.
   - [[Error Propagation]] — the density uncertainty with $D$ squared.

- **Children:**
  - [[The Solar System]] — average density, computed from mass and radius, is what sorts the planets into rock and gas.
   - [[Kinetic Theory and the Ideal Gas]] — pressure again, now from molecular impacts; the atmosphere's exponential in Part III is the gas law meeting hydrostatics.
   - [[Drag and Terminal Velocity]] — Example 4's viscous force, and why it grows until the three forces balance.
   - [[Braking Systems]] — Pascal's principle at the pedal.
   - [[Archimedes and the Soldier]] — the crown, the bath, and Syracuse in 212 BC.

- **Cross-domain:** [[Work, Energy and Power]] — Bernoulli is the work–energy theorem per unit volume; [[Gravitational Fields]] — the $g$ in every formula here, and why the same equations run on Mars with $3.7$; [[Internal Energy]] — density in the particle model of solids, liquids and gases.

- **Misconception traps cleared:** pressure has no direction; upthrust is depth-independent; density decides floating, not mass; width does not change hydrostatic pressure; equal transit time is not how wings work; $g$ differs between the two Cambridge boards.

---

## Beyond Syllabus

### The water is not quite incompressible

Recall that $\Delta p = \rho g \Delta h$ assumed $\rho$ constant. Water's bulk modulus is about $2.2$ GPa, so at the $108$ MPa of the Challenger Deep it is compressed by about $5\%$; the true pressure at the bottom is a few per cent higher than the constant-density estimate, and the upthrust on a submersible really does change slightly with depth. For gases the assumption fails completely, which is why Part III's atmosphere needed the exponential.

### Viscosity: Stokes' law and Example 4's constant

The viscous force on a slow sphere is Stokes' law, $F = 6\pi\eta r v$, so the exam's $k = 17$ is $6\pi\eta$ and the liquid's viscosity is $\eta = 17/6\pi = 0.90\ \text{Pa s}$ — glycerol at room temperature, which is exactly what a "sphere falling slowly through a liquid of density 1300" experiment uses. Terminal velocity, and the drag that does *not* obey Stokes at speed, is [[Drag and Terminal Velocity]].

### Surface tension: the exception to Archimedes

A steel needle laid gently on water floats, at $7\,900\ \text{kg m}^{-3}$, and a water strider walks on it. Neither is displacing its weight of water; both are held by **surface tension**, the energy cost of stretching the water's surface, which acts like a skin that can support a force of about $0.07$ N per metre of contact line. For anything larger than a few millimetres the skin is negligible against $\rho g V$ and Archimedes rules again.

### Lift, honestly

A wing produces lift because it deflects air downward; by Newton's third law the air pushes the wing up, and the pressure difference between the surfaces (lower on top, where the flow is faster) is the same fact seen through Bernoulli. Both descriptions are correct; the false one is the *reason* usually given for the faster flow. The full account is the circulation theory of Kutta and Joukowski, in which the wing sheds a starting vortex and keeps an equal and opposite circulation around itself.
