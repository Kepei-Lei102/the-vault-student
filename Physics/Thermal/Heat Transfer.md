---
chinese: 热传递 (rè chuándì)
aliases:
  - Thermal Energy Transfer
  - Conduction Convection and Radiation
prerequisites:
  - "[[Internal Energy]]"
  - "[[Temperature and Thermometry]]"
leads_to: []
teach_together:
  - "[[Specific Heat Capacity]]"
tags:
  - subject/physics
  - domain/thermal-physics
  - level/IGCSE
  - level/A-Level
  - level/university
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/0625-2-3
  - type/deep
  - type/derivation
  - notation/thermal-conductivity
  - misconception/metal-is-colder
  - misconception/heat-rises
---

# Heat Transfer 热传递

*A metal chair and a wooden chair have stood in the same room all night. Touch them: the metal feels colder. Put a thermometer on each and wait: nearly the same temperature. Your hand is noticing a journey, not just a destination.*

## Definition — follow the energy, then ask what carries it

**Heat transfer** is energy transfer driven by a temperature difference. Without external intervention, its net direction is from hotter to colder. **Internal energy** is the store; **heat** describes a transfer. A cup does not contain a quantity of “heat waiting to escape”.

The routes differ in **what transports the energy**:

| Route | What happens | Does matter travel across the gap? |
|---|---|---|
| **Conduction** | Microscopic interactions transfer energy through a material | No bulk flow is required |
| **Convection** | Moving fluid carries internal energy from place to place | Yes: the fluid moves |
| **Radiation** | Electromagnetic waves carry energy | No material medium is required |

Several routes can operate at once. A radiator's name does not tell you which route dominates its heat output.

### 中文锚点

同一个房间里，金属椅子摸着比木椅子凉，难道它们的温度真的不同？放了一整夜后，两者通常已经接近同一温度；不同的是，它们从你手里带走能量的快慢。金属传得快，接触处不容易被手捂暖，你便觉得更凉。手感不只是在回答“它有多冷”，也在回答“我的能量流走得有多快”。理解热传递，就从追踪这股流动开始。

## 1. Conduction — a relay without a marching crowd

At the hot end of a solid, particles have greater average vibrational energy. Through interactions with their neighbours they transfer energy. The neighbours interact with their neighbours, and a net flow develops down the temperature gradient. The particles mostly remain near their equilibrium positions: a spoon can conduct energy towards your hand without its atoms streaming up the handle.

**Metals have a second, often very effective carrier: mobile electrons.** Their random motion transports energy between regions, with scattering exchanging energy with the lattice. This is not a claim that thermal conduction requires a net electric current.

In gases, particles are widely separated and transfer energy less effectively by these local interactions than good metallic conductors. Most liquids also conduct poorly compared with metals; their impressive ability to carry energy in a saucepan largely comes from **bulk motion**. There are exceptions: liquid metals conduct well. “Solid” does not mean “good conductor”: glass, stone and plastics differ greatly, and conductivity is a continuum rather than two boxes.

### Why the chair feels cold

Your skin starts warmer than both chairs. Energy leaves your skin through the contact. Metal conducts the incoming energy away from the contact rapidly, keeping a larger temperature difference there; wood lets its contact region warm more readily. Your skin therefore cools faster against metal.

For a short touch, conductivity alone is not the entire story: density, heat capacity and contact quality matter too. The enrichment quantity **thermal effusivity**, $e=\sqrt{k\rho c}$, combines a material's ability to conduct and store energy. Do not use touch as a thermometer. Reverse the situation—objects hotter than your skin—and rapid transfer makes the better conductor feel hotter.

### Deriving the slab law from its dependencies

Consider a uniform slab, thickness $L$, cross-sectional area $A$, with faces held at $T_h$ and $T_c$. Wait until its temperature profile stops changing. Neglect side losses and assume constant conductivity.

- Double $A$: two identical paths operate side by side, so the rate doubles.
- Double $L$ at fixed end temperatures: the same temperature drop is spread over twice the distance, so the gradient and rate halve.
- Double the temperature difference: in the linear conduction regime the rate doubles.

The material property that sets the proportionality is **thermal conductivity** $k$:

$$\boxed{P=\frac{\Delta Q}{\Delta t}=\frac{kA(T_h-T_c)}{L}.}$$

This is **Fourier's empirical law**, not a consequence of conservation alone. Its units follow from the equation:

$$[k]=\mathrm{W\,m^{-1}\,K^{-1}}.$$

A difference of $20\,\mathrm K$ is the same size as a difference of 20 °C. Absolute temperatures in radiation laws are a different matter.

In a coordinate increasing from hot to cold,

$$P_x=-kA\frac{dT}{dx}.$$

The minus sign makes energy flow towards lower temperature. $P_x$ is a signed rate along an axis; the positive slab formula above gives the hot-to-cold magnitude.

### Two layers — conserve the rate, add the drops

In a steady wall with no internal sources or side losses, energy cannot accumulate at an interface. **The same power passes through each layer.** Define a thermal resistance

$$R_{\rm th}=\frac{L}{kA},\qquad \Delta T=PR_{\rm th}.$$

Two layers then give

$$\Delta T_{\rm total}=P(R_1+R_2),\qquad P=\frac{T_h-T_c}{R_1+R_2}.$$

The poorer-conducting layer takes the larger temperature drop. This resembles resistors in series, but **temperature difference** plays the role of voltage and **power transfer** plays the role of current. $R_{\rm th}$ has units $\mathrm{K/W}$, not ohms.

## 2. Convection — move the carrier

Heat a small region at the bottom of water well above 4 °C:

1. The water there warms and expands.
2. The same mass occupies more volume, so its density falls.
3. At the same height, the surrounding denser water provides a buoyant force greater than the parcel's weight.
4. The warmer parcel rises; other water moves in to replace it.
5. Cooling elsewhere can complete a circulating flow.

The energy is now travelling with the fluid. The causal chain is **heating → expansion → density difference → buoyancy → circulation**, not “heat wants to rise”. Conduction still transfers energy at the hot surface and between neighbouring parcels.

The density condition matters. Water between $0$ and 4 °C does not follow the ordinary warming-and-expanding rule. Heating from above can produce a stable warm layer rather than the vigorous circulation produced by heating below.

**Natural convection** uses buoyancy. **Forced convection** uses a fan or pump: a computer fan moves air even when buoyancy would be weak. Solids cannot support this bulk circulation; a vacuum has no fluid to circulate.

A useful engineering model for heat transfer between a surface and moving fluid is

$$P=hA(T_s-T_f).$$

Unlike $k$, the coefficient $h$ depends strongly on flow speed, geometry and the fluid. It is not a fixed universal property of aluminium or air. This is a modelling relation, not a recipe for calculating every convection flow.

![[heat-transfer-animation.mp4]]

*Follow what moves. The particle and fluid motions are schematic, not a molecular-dynamics or fluid-flow simulation. The final flask blocks several routes separately.*

## 3. Radiation — energy can cross empty space

Sunlight reaches Earth across nearly empty space. Conduction and convection cannot explain that journey. Matter emits **thermal electromagnetic radiation** because of its temperature; every body above absolute zero emits, including one that feels cold to your hand.

Near room temperature, most thermal emission is infrared. Very hot bodies also emit appreciable visible light: an incandescent filament is the familiar counterexample to “thermal radiation is always invisible”. [[Stellar Luminosity and Size]] explains the continuous spectrum and its temperature-dependent peak.

### Emitting is not the same as cooling

A body both emits radiation and absorbs radiation arriving from its surroundings. For an ideal blackbody,

$$P_{\rm emitted}=\sigma AT^4,\qquad \sigma\approx5.67\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}.$$

For a grey surface with emissivity $\varepsilon$ facing much larger, uniform surroundings, and with matching absorption/emission assumptions,

$$\boxed{P_{\rm net,out}=\varepsilon\sigma A(T^4-T_{\rm surroundings}^4).}$$

Use **kelvin**. The emitted power is never negative; the **net outward** power can be negative if the surroundings are hotter. At equal temperatures both sides still radiate, but the two transfers balance.

The simple net formula is not a universal exchange law for two small arbitrary objects. Geometry, view factors and wavelength-dependent surface properties can matter.

### Black, white, dull and shiny — which wavelengths?

For ordinary classroom comparisons in the infrared, a dull black surface is generally a better absorber **and** emitter than a polished metallic one. A polished metal reflects much of the incident infrared and emits relatively little at the same temperature.

Absorption and emission are linked **at the same wavelength and under the corresponding conditions**. Visible colour alone does not determine infrared behaviour: a visibly white paint can still emit thermal infrared efficiently. A mirror is not cold because it has “no heat”; its surface interacts differently with radiation.

With surface and surroundings otherwise unchanged:

- More emitting area increases emitted power.
- Higher absolute temperature greatly increases emitted power.
- An object gains internal energy if its total incoming power exceeds its total outgoing power, and loses it if the reverse is true.
- Constant temperature in a fixed-state object requires balanced power, not an absence of transfers. A phase change can also hold temperature steady while energy is stored, so state the condition.

## 4. Designing the paths — the actual devices

### A saucepan and a room heater

A metal pan spreads energy from its heated base by conduction; water circulation redistributes it through the contents; a low-conductivity handle slows conduction towards your hand. A flame supplies energy through hot moving gases and radiation, not just through a mysterious “heat touching the pan”.

Air warmed near a room heater expands, becomes less dense and rises. Cooler air replaces it. The heater also emits radiation towards people and objects. Warm air rises; radiant energy can travel sideways towards your legs.

### The vacuum flask

| Feature | Route it limits | What still remains |
|---|---|---|
| Evacuated gap | Bulk convection; greatly reduces gas conduction | Radiation across the gap; solid connections |
| Reflective facing surfaces | Radiative exchange | Imperfect reflection/emission |
| Insulating stopper and narrow supports | Conduction through solid bridges; air exchange at opening | Finite leakage through real materials |
| Closed lid | Bulk air exchange and evaporation | Other routes through the walls |

A vacuum flask slows **both** cooling of a hot drink and warming of a cold one. Insulation does not manufacture warmth; it resists transfer in either direction.

### Double glazing, clothes and laptop cooling

A narrow sealed gas layer in double glazing slows conduction; the gap geometry limits circulation. Making the gap arbitrarily wider is not necessarily better because larger convection currents can develop. Low-emissivity coatings reduce radiative exchange. Frames and spacers can provide conducting bridges. These separate mechanisms explain why a window is a system, not just two panes. [US Department of Energy](https://www.energy.gov/energysaver/window-types-and-technologies)

Clothing traps relatively still air; a windproof outer layer reduces replacement by moving air. Compressing insulation or letting wind flush through it can weaken its effect. An ordinary blanket on an unpowered cold object does not make the object generate energy.

A laptop does the opposite: thermal interface material improves contact from chip to cooler; metal spreads energy; fins enlarge surface area; a fan maintains moving air. **A heat sink is a route to the environment, not a bottomless energy store.**

### Fire and a car's “radiator”

A wood or coal fire releases chemical energy. Radiation warms a person facing it; hot combustion gases carry energy upwards by convection; conduction warms the grate and nearby solid material. Stand beside a fire rather than above it to separate “radiation reaches me” from “hot gas rises”.

A car's coolant is pumped through engine passages and the radiator. Energy crosses solid walls by conduction, then transfers to moving air at the fins; the fan and the car's motion support forced convection. Thermal radiation also occurs, but the name *radiator* does not make it the sole mechanism.

## 5. Earth — an energy balance, not a sealed greenhouse box

At the top of the atmosphere, some incoming sunlight is reflected to space by clouds, air and the surface; the remainder is absorbed. Earth and its atmosphere emit thermal infrared to space. Over a steady long-term global average,

$$P_{\rm absorbed\ sunlight}=P_{\rm outgoing\ thermal\ radiation}.$$

Absorb more than escapes and the Earth system accumulates energy; lose more than it absorbs and it cools. Increasing reflectivity reduces absorbed sunlight. Greenhouse gases absorb and emit at infrared wavelengths, changing how effectively energy escapes for a given temperature structure. The surface and atmosphere adjust together; “all heat is permanently trapped” is the wrong picture. Clouds affect both reflection and infrared exchange. [NASA: Earth's radiation budget](https://science.nasa.gov/ems/13_radiationbudget/)

**Enrichment model.** A spherical planet intercepts sunlight over $\pi R^2$ but emits over $4\pi R^2$. With solar irradiance $S$, reflectivity $\alpha$ and ideal uniform emission,

$$(1-\alpha)S\pi R^2=4\pi R^2\sigma T_{\rm eff}^4.$$

$$T_{\rm eff}=\left[\frac{(1-\alpha)S}{4\sigma}\right]^{1/4}.$$

Using illustrative $S=1360\,\mathrm{W/m^2}$ and $\alpha=0.30$ gives about $255\,\mathrm K$. This is an **effective radiating temperature**, not a prediction of every place's surface temperature. The factor four is geometry, not an arbitrary correction. The model does not resolve atmospheric layers, weather or feedbacks.

## 6. Worked examples — choose the route before the formula

### A. Which routes does a vacuum remove? — Cambridge 0625/42, May/June 2024, Q4(b)(ii)

*Paraphrased task:* identify the two methods of thermal energy transfer prevented by a vacuum.

**Trigger: no particles. Tool: identify the carrier.** Conduction needs material interactions; convection needs moving fluid. The answer is **conduction and convection**. Radiation survives the absence of matter. The published scheme awards one mark for each named method. A real flask can still conduct through its stopper: distinguish a route **across the vacuum** from all routes through the whole object.

### B. Measure a plastic's conductivity — AP Physics 2, 2019, Q3

The experiment holds a plastic slab between boiling water at 100 °C and melting ice at 0 °C. Area $A=0.025\,\mathrm{m^2}$. The measured energy transfer rates are:

| Thickness $L$/m | $1/L$ / $\mathrm{m^{-1}}$ | Rate $P$/W |
|---|---|---|
| 0.010 | 100.0 | 97 |
| 0.020 | 50.0 | 53 |
| 0.030 | 33.3 | 31 |
| 0.040 | 25.0 | 27 |
| 0.050 | 20.0 | 18 |

**Trigger: the varied quantity is thickness, and Fourier's law contains $1/L$. Tool: linearisation.** Write

$$P=(kA\Delta T)\left(\frac1L\right).$$

Plot $P$ vertically against $1/L$ horizontally. The gradient $m$ is $kA\Delta T$, with units $\mathrm{W\,m}$. Do not take the gradient of $P$ against $L$ and call it conductivity.

![[heat-transfer-conductivity.svg|680]]

**Tool: a best-fit gradient, then solve for $k$.** The published hand-drawn line has a gradient near $1.0\,\mathrm{W\,m}$, giving

$$k=\frac{m}{A\Delta T}\approx\frac{1.0}{0.025\times100}=0.40\,\mathrm{W\,m^{-1}\,K^{-1}}.$$

The companion script's unconstrained least-squares fit gives approximately $0.389\,\mathrm{W\,m^{-1}\,K^{-1}}$; the difference reflects line fitting, not different physics. Do not demand a perfect line through every noisy point.

**Trigger: ice also meets room air. Tool: account for unwanted energy paths.** Extra energy from the surroundings can melt additional ice. If all this melting is attributed to conduction through the slab, a direct estimate of $k$ is too high. In a fitted graph a constant background instead produces an intercept; a slope bias depends on how that extra transfer varies across trials and on whether a zero intercept is forced. The scoring guideline's qualitative “too high” explanation does not remove that modelling distinction.

**Tool: microscopic conduction.** Energy flows upwards from the hot lower face to the ice. Particles at the lower face have greater average vibrational energy and exchange energy with neighbours; plastic does not need mobile conduction electrons to conduct at all.

**Transfer to touch:** Q3(e) compares the plastic with wood at room temperature. The material removing energy from skin faster feels cooler, even though the two objects started at the same temperature.

### C. A wall with two layers — original engineering model

A $10\,\mathrm{m^2}$ wall has $0.10\,\mathrm m$ of brick with $k=0.60\,\mathrm{W\,m^{-1}\,K^{-1}}$ and $0.050\,\mathrm m$ of insulation with $k=0.040\,\mathrm{W\,m^{-1}\,K^{-1}}$. Its outer faces are held $20\,\mathrm K$ apart. Ignore surface/contact resistances and thermal bridges.

**Trigger: steady layers in series. Tool: conserve power and add thermal resistances.**

$$R_b=\frac{0.10}{0.60\times10}=0.0167\,\mathrm{K/W},\qquad R_i=\frac{0.050}{0.040\times10}=0.125\,\mathrm{K/W}.$$

$$P=\frac{20}{0.1417}\approx141\,\mathrm W.$$

The drops are $PR_b\approx2.35\,\mathrm K$ and $PR_i\approx17.65\,\mathrm K$. Most of the temperature drop occurs across the insulation, while **the same power** crosses both layers. Without the insulation, this simplified model would give $1200\,\mathrm W$.

## 7. Experiments — make each comparison fair

**Conduction:** place equal-length, equal-cross-section rods of different materials with one end in the same warm-water bath. Measure temperatures at equal distances after equal times, or compare time to a chosen temperature. Control initial temperature and contact. A faster transient response depends on heat capacity and density as well as conductivity; do not claim it measures $k$ alone. A steady slab with known face temperatures gives the more direct method.

**Convection:** warm water locally from below and follow a small dye trace. The dye marks water motion, not “heat particles”. Move the heating region to the top and compare circulation. Use teacher-controlled heating; hot water and glass require care. In a room, compare temperatures at several heights rather than inferring circulation from a single reading.

**Emission:** fill otherwise matched dull-black and polished containers with equally hot water; compare infrared detector readings at the same distance and orientation while the surfaces are at the same measured temperature. Keep area and geometry equal. A Leslie cube offers differently finished faces at nearly the same temperature. Cooling curves alone mix radiation with convection and conduction.

**Absorption:** illuminate matched surfaces with the same infrared source at equal distance and angle. Compare initial temperature rise, with equal masses, heat capacities and initial temperatures. Keep other losses comparable; a temperature rise measures a net energy balance, not absorption in isolation.

**Hands-on: the cold-chair puzzle.** Leave a metal spoon and a wooden utensil in the same room. Predict the direction of transfer from your hand; compare their feel briefly, then compare equilibrated thermometer readings. Use room-temperature objects only. This distinguishes temperature from transient heat transfer without a dangerously hot demonstration.

## 8. Beyond syllabus — from one slab to a temperature field

Recall that Fourier's law specifies a local rate down a temperature gradient. In a thin slice of area $A$ and thickness $dx$, unequal incoming and outgoing rates change stored energy:

$$\rho cA\,dx\,\frac{\partial T}{\partial t}=P(x)-P(x+dx)\approx-\frac{\partial P}{\partial x}dx.$$

Substitute $P=-kA\,\partial T/\partial x$, with constant material properties and no internal heat sources:

$$\boxed{\frac{\partial T}{\partial t}=\alpha\frac{\partial^2T}{\partial x^2},\qquad \alpha=\frac{k}{\rho c}.}$$

Here $\alpha$ is **thermal diffusivity**, not the planetary reflectivity used earlier. A hot peak has negative curvature and cools; a cold dip has positive curvature and warms. Conservation plus a transport law produces the **heat equation**. A characteristic diffusion time scales as $L^2/\alpha$: doubling thickness makes this timescale roughly four times longer, not merely twice.

The adjacent `heat-transfer-model.py` fits the real AP data, verifies the wall calculation and solves this one-dimensional equation on an insulated rod. Change the initial temperature profile and watch it smooth while total discrete energy stays constant. Its explicit update needs $\alpha\Delta t/\Delta x^2\leq1/2$; violating that condition can create numerical explosions that are not physical heating.

## Common misconceptions

- **“Cold flows into my hand.”** Follow net energy leaving the warmer hand.
- **“Heat rises.”** Buoyant warm fluid may rise; conduction and radiation have no universal upward direction.
- **“A vacuum stops all heat transfer.”** It removes material routes across the gap, not radiation or solid bridges around it.
- **“A black body only absorbs.”** It also emits; thermal equilibrium balances rates.
- **“Higher conductivity means larger heat capacity.”** One describes transport, the other storage.
- **“An insulator stops heat forever.”** Real insulation reduces the rate; with no source, sufficient time usually allows equilibrium.

## Exam Notes

### Cambridge 0625 — §2.3.1–2.3.4

Core includes conductor/insulator demonstrations, density-driven convection, radiation without a medium, surface comparisons and everyday applications. Supplement includes lattice and free-electron mechanisms, weak conduction in gases/most liquids, intermediate conductors, emission/absorption experiments, power balance, Earth's radiative balance and combined mechanisms in fires and car radiators. Explain the full causal chain; naming “convection” alone does not explain it.

The syllabus uses infrared language for thermal radiation; room-temperature contexts justify it, but hot glowing bodies also emit visibly. Fourier calculations, thermal resistances, effusivity and the heat equation are enrichment for this qualification. Q4(b)(ii) above is a verified short-answer example, not a claim about typical mark allocations.

### IB Physics — B.1 Thermal Energy Transfers, SL and HL

The current guide explicitly includes microscopic conduction, quantitative $\Delta Q/\Delta t=kA\Delta T/\Delta x$, qualitative density-driven convection, blackbody Stefan–Boltzmann emission, apparent brightness and Wien's law. B.1 has no additional-HL-only content. The radiation-spectrum and stellar measurements are developed in [[Stellar Luminosity and Size]]. Series-layer reasoning is a useful application; general fluid dynamics and the heat equation go beyond the stated outcomes.

### AP Physics 2 — Topics 9.3 and 9.5

9.3 includes the three transfer mechanisms and equilibrium. 9.5.B includes conductivity, area, thickness and temperature-difference dependence. Use $Q/\Delta t=kA\Delta T/L$; the equation sheet supplies the conduction relation. The 2019 Q3 example predates the redesigned course, but its conductivity and experimental reasoning transfer to the current scope. Do not import all its historical learning-objective numbers into the current map.

### Where this is not a separate examined topic

Cambridge **9702** examines internal energy, thermometry and thermal bookkeeping but does not specify a general conduction/convection/Fourier-law unit; its §25.2 blackbody law is covered with astronomy. **AP Physics 1, AP Physics C: Mechanics and AP Physics C: Electricity and Magnetism** do not prescribe this heat-transfer unit in their inspected current course frameworks. Resistive electrical heating is not itself a requirement to derive heat conduction. The calculus extensions here are enrichment, not extra Cambridge or AP-C coverage.

## Connections

- **Builds on:** [[Internal Energy]] — distinguish the store from the transfer; [[Temperature and Thermometry]] — temperature difference and the limits of touch.
- **Teach together:** [[Specific Heat Capacity]] — energy received becomes a temperature change only after storage and phase changes are accounted for.
- **Radiation:** [[Stellar Luminosity and Size]] — spectra, Wien's law and emitted versus received power; [[Electromagnetic Spectrum]] — infrared among the electromagnetic family.
- **Buoyancy:** [[Density and Pressure]] — displaced fluid and the force driving natural convection.
- **Conservation:** [[First Law of Thermodynamics]] — the complete energy ledger; [[Kirchhoff's Laws]] — compare conserved flow through series paths.
- **Mathematics:** [[Linearisation]] — choose $1/L$ to reveal the conductivity; [[Differential Equations]] — transport plus conservation determines an evolving field.
- **Story:** [[Boltzmann's Tombstone]] — the microscopic motions underlying a macroscopic energy flow.

## LaTeX Reference

| Meaning | Expression | Units / condition |
|---|---|---|
| Slab conduction | $P=kA\Delta T/L$ | W; steady, uniform slab |
| Thermal resistance | $R_{\rm th}=L/(kA)$ | K/W |
| Surface convection model | $P=hA(T_s-T_f)$ | $h$ in W m⁻² K⁻¹ |
| Net grey-body radiation | $P=\varepsilon\sigma A(T^4-T_s^4)$ | Kelvin; large uniform surroundings |
| Thermal diffusivity | $\alpha=k/(\rho c)$ | m²/s |
