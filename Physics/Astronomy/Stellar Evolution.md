---
chinese: 恒星演化 (héngxīng yǎnhuà)
aliases:
  - Life Cycle of a Star
  - Hertzsprung–Russell Diagram
  - HR Diagram
  - Stellar Parallax
prerequisites:
  - "[[Stellar Luminosity and Size]]"
  - "[[Nuclear Physics]]"
  - "[[Gravitational Fields]]"
  - "[[Kinetic Theory and the Ideal Gas]]"
leads_to:
  - "[[General Relativity]]"
teach_together:
  - "[[Pauli Exclusion Principle]]"
tags:
  - subject/physics
  - domain/astronomy
  - domain/nuclear-physics
  - level/IGCSE
  - level/IB
  - level/university
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - syllabus/0625-6-2
  - type/deep
  - type/derivation
  - notation/parsec
  - misconception/the-sun-burns
  - misconception/big-stars-live-longer
  - misconception/the-sun-will-explode
  - misconception/red-giants-are-cool-inside
  - misconception/stars-slide-along-the-main-sequence
---

# Stellar Evolution 恒星演化

> *On 4 July 1054 the astronomers of the Song court recorded a **guest star** (客星) beside the star Tianguan, in what we call Taurus. It was bright enough to see in daylight for twenty-three days and stayed visible at night for nearly two years; then it faded, and the record was filed. Point a telescope at that spot today and there is a tangled cloud of glowing gas, the Crab Nebula, eleven light-years across and still flying apart at 1500 km/s. Run the expansion backwards and it shrinks to a point in the middle of the eleventh century. At its centre is an object about 20 km wide, heavier than the Sun, spinning thirty times a second. The court astronomers had watched a star die, and written down the date.*

## Definition

### Formal

**Stellar evolution** is the sequence of changes in a star's structure, size, surface temperature and luminosity over its life, from the collapse of an interstellar cloud to a compact remnant. A star is a ball of gas held in **equilibrium**: at every depth, the inward pull of gravity on the layers above is balanced by the outward push of the pressure of the hot gas below. Energy leaks from the surface as light, and for most of a star's life **nuclear fusion** in the core replaces it exactly. A star is on the **main sequence** while it fuses hydrogen to helium in its core. Evolution happens because each fuel runs out, and the star's **mass** decides how many fuels it can light and how it ends: as a **white dwarf**, a **neutron star** or a **black hole**.

### Intuitive

A star spends its life not collapsing. Gravity never switches off, so something must hold the star up every second for billions of years, and that something is heat. Heat leaks away, so it has to be paid for. Everything a star does (shine, swell, shrink, explode) is one of two things: a fuel paying the bill, or gravity collecting when the payment stops.

### 中文锚点

给自行车打气，打气筒会发烫：气体被压缩就会升温。恒星就是引力拿一团直径上百万公里的气体做的同一个实验。引力往里压，气体变热，热气体往外顶；顶的力和压的力一样大时，气团不再收缩，这种僵持，就是一颗恒星。可是热的东西会发光，发光就是在散热，引力每天都会多赢一点，除非有谁一直替它付账。恒星中心热到氢核可以聚变成氦，聚变放出的能量正好补上散掉的热，一付就是几十亿年。等中心的氢用完，账没人付了，引力就把核心再压紧一步，核心因此更热（还是打气筒的道理），直到下一种燃料氦被点着。恒星的一生就是这个循环反复上演：燃料用完，引力压紧，核心更热，点燃新燃料。循环能走几轮，由恒星有多重决定。太阳只烧得动两种燃料，最后剩下一颗地球大小、慢慢变凉的余烬；比太阳重十几二十倍的恒星会一路烧到铁，铁的聚变不再放能，核心在一秒之内塌下去。随后的爆炸把新造出的元素抛进太空，你呼吸的氧、血液里的铁，都是这样来的。

### 术语对照 (Terms)

恒星 star · 星际云 interstellar cloud · 原恒星 protostar · 主序星 main-sequence star · 红巨星 red giant · 红超巨星 red supergiant · 行星状星云 planetary nebula · 白矮星 white dwarf · 超新星 supernova · 中子星 neutron star · 黑洞 black hole · 光年 light-year · 秒差距 parsec · 视差 parallax · 赫罗图 Hertzsprung–Russell diagram · 核聚变 nuclear fusion · 流体静力平衡 hydrostatic equilibrium

---

## Notation

| Symbol | Meaning | Value or unit |
|---|---|---|
| $M_\odot$, $R_\odot$, $L_\odot$ | mass, radius, luminosity of the Sun | $1.99\times10^{30}$ kg, $6.96\times10^{8}$ m, $3.83\times10^{26}$ W |
| ly | light-year: the distance light travels in vacuum in one year | $9.5\times10^{15}$ m |
| AU | astronomical unit: mean Earth–Sun distance | $1.50\times10^{11}$ m |
| pc | parsec: the distance at which 1 AU subtends one arcsecond | $3.09\times10^{16}$ m = 3.26 ly |
| $p$ | parallax angle | arcseconds ($1'' = 1/3600$ of a degree) |
| $L$, $T$, $R$ | luminosity, surface temperature, radius, tied by $L = 4\pi R^2\sigma T^4$ | W, K, m |

Every number below is computed in `stellar-evolution-model.py`, which sits beside this page; run it and change the inputs.

---

## Part I — The Sun is a star, and the stars are far away

The Sun is a star of medium size. By mass it is 73 % hydrogen, 25 % helium and 2 % everything else, a recipe first read from its spectrum by Cecilia Payne in 1925 (the lines are explained in [[Energy Levels and Line Spectra]]). Its surface is at 5772 K, and a body at that temperature radiates most of its energy in three neighbouring regions of the [[Electromagnetic Spectrum]]: **infrared** (51 % of the power), **visible light** (37 %) and **ultraviolet** (12 %), with the peak at 500 nm, in the green. Those percentages are the areas under the blackbody curve of [[Stellar Luminosity and Size]], integrated numerically.

"Medium" needs a caution. The Sun sits in the middle of the *range* of stellar masses, which runs from 0.08 to over 100 $M_\odot$, but most stars are small red dwarfs, and the Sun outweighs about nine stars in ten.

A **galaxy** is a system of many billions of stars held together by gravity. The Sun is one of several hundred billion stars in the galaxy called the **Milky Way**, and the other stars of the Milky Way are vastly further from us than the Sun is. Light from the Sun arrives in 500 s. Light from the next nearest star, Proxima Centauri, takes 4.2 years. Because metres are hopeless at this scale, distances are given in **light-years**:

$$1\ \text{ly} = (3.0\times10^{8}\ \text{m/s}) \times (365.25 \times 24 \times 3600\ \text{s}) = 9.5\times10^{15}\ \text{m}.$$

A light-year is a **distance**. If the Sun were a table-tennis ball in Chengdu, Proxima would be another ball in Guangzhou, 1200 km away, with nothing in between.

### How the distance is measured: parallax

Hold a thumb at arm's length and look at it with one eye and then the other: it jumps against the far wall. The nearer the thumb, the bigger the jump. Astronomers use the Earth's orbit as the two eyes. A nearby star, photographed in January and again in July, shifts against the very distant stars behind it.

![[stellar-evolution-parallax.svg|820]]

The **parallax angle** $p$ is *half* the total shift: the angle that the 1 AU radius of the Earth's orbit subtends at the star. From the right-angled triangle, $\tan p = 1\ \text{AU}/d$, and for angles this tiny $\tan p = p$ in radians, so $d = 1\ \text{AU}/p$. Astronomers then choose the unit of distance that makes the constant disappear: the **parsec** is *defined* as the distance at which $p$ is exactly one arcsecond. Hence

$$d\,(\text{parsec}) = \frac{1}{p\,(\text{arcsecond})}, \qquad 1\ \text{pc} = \frac{1\ \text{AU}}{\tan 1''} = 206\,265\ \text{AU} = 3.09\times10^{16}\ \text{m} = 3.26\ \text{ly}.$$

Proxima has $p = 0.768''$, so $d = 1/0.768 = 1.30$ pc $= 4.2$ ly. An arcsecond is the width of a one-yuan coin seen from 5 km, and no star has a parallax that large, which is why the first one was not measured until 1838 (Bessel, 61 Cygni). Halve the parallax and the distance doubles; once $p$ falls below the smallest angle the telescope can measure, the method stops, and the standard candles of [[Stellar Luminosity and Size]] take over. Parallax matters here because it turns *apparent brightness* into *luminosity* through $b = L/4\pi d^2$, and luminosity is one of the two axes of the diagram in Part IV.

---

## Part II — What holds a star up, and what pays for it

### The balance

Take any layer inside a star. The weight of everything above presses down on it; the gas below, being hotter and denser, presses up harder than the gas above presses down. The star is stable when that pressure difference equals the weight, at every depth. This is **hydrostatic equilibrium**, the same balance that sets the pressure at the bottom of a swimming pool in [[Density and Pressure]], except that here the fluid is a gas at millions of kelvin and the pressure comes from the furious thermal motion of its particles, $P = nkT$ from [[Kinetic Theory and the Ideal Gas]]. The outward force is a consequence of the **high temperature** at the centre.

The balance alone tells us how hot the centre must be. To hold up a ball of mass $M$ and radius $R$, a particle at the centre needs thermal energy comparable to the gravitational energy it would gain by falling there, $kT \sim GMm_p/R$:

$$T_c \sim \frac{GMm_p}{kR} = \frac{(6.67\times10^{-11})(1.99\times10^{30})(1.67\times10^{-27})}{(1.38\times10^{-23})(6.96\times10^{8})} = 2.3\times10^{7}\ \text{K}.$$

Detailed models give $1.57\times10^{7}$ K. A temperature of fifteen million kelvin has been read off from the Sun's mass and radius alone, with no nuclear physics at all. Gravity sets the core temperature, and the core temperature then decides which nuclear reactions can run.

### The bill

A hot ball shines, and the light carries energy away. Something must replace $3.83\times10^{26}$ J every second or the Sun would cool, lose pressure, and shrink. Three candidates were taken seriously, and one calculation each settles them:

![[stellar-evolution-lifetimes.svg|820]]

- **Burning.** The best chemical fuel gives about 30 MJ/kg. A Sun made entirely of coal and oxygen lasts $(3\times10^{7})(1.99\times10^{30})/(3.83\times10^{26}) = 1.6\times10^{11}$ s, about **5000 years**, less than recorded history.
- **Shrinking.** Kelvin and Helmholtz proposed that the Sun shines by slowly contracting, turning gravitational potential energy into heat. The store is about $GM^2/R = 3.8\times10^{41}$ J, good for **30 million years**. In the 1860s this was the accepted answer, and it collided head-on with the geologists and with Darwin, whose rocks and fossils needed far longer.
- **Fusion.** In 1920 Aston's new mass spectrograph showed that four hydrogen nuclei weigh 0.7 % more than one helium nucleus. Eddington saw at once what that meant: if stars turn hydrogen into helium, the missing mass appears as energy, $E = \Delta m\,c^2$ (the binding-energy bookkeeping of [[Nuclear Physics]]). Convert 0.7 % of the central tenth of the Sun and the supply lasts **10 billion years**.

Only the third survives the age of the Earth, 4.57 billion years. In **stable stars the nuclear reactions are the fusion of hydrogen into helium**, and the Sun pays its bill by turning $4.3\times10^{9}$ kg of mass into light every second, fusing $6\times10^{11}$ kg of hydrogen to do it.

### How hydrogen becomes helium

Four protons cannot meet at once. In stars like the Sun the work is done in three two-body steps, the **proton–proton chain**:

$$^1_1\text{H} + {}^1_1\text{H} \to {}^2_1\text{H} + {}^0_{+1}e + \nu \qquad\quad {}^2_1\text{H} + {}^1_1\text{H} \to {}^3_2\text{He} + \gamma \qquad\quad {}^3_2\text{He} + {}^3_2\text{He} \to {}^4_2\text{He} + 2\,{}^1_1\text{H}$$

The first two steps run twice for each third step, so the net result is $4\,{}^1_1\text{H} \to {}^4_2\text{He}$ with 26.7 MeV released, 0.71 % of the rest mass. Two conditions are needed, and both are met only near the centre:

- **High temperature**, so that nuclei move fast enough to approach closely against their electrostatic repulsion, to the $10^{-15}$ m range where the strong nuclear force can bind them.
- **High density**, so that such collisions happen often enough.

The first step is the bottleneck, because it needs a proton to turn into a neutron during the brief collision, a weak-interaction process. An average proton in the Sun's core waits about nine billion years for it. That reluctance is the reason the Sun is a slow fire and not a bomb: its core releases about 17 W per cubic metre, whereas a resting human body releases about 1400 W per cubic metre. The Sun is bright because it is enormous.

### The thermostat

Fusion rates depend very steeply on temperature, which makes the balance self-correcting. Suppose the core fuses a little too fast. It heats, the pressure rises, the core **expands**, and expansion cools it (the reverse of the bicycle pump), so the rate falls back. Too slow, and the core loses pressure, contracts, heats, and the rate rises. This negative feedback holds a main-sequence star steady for billions of years. It also carries the rule that drives everything in Part III: **a core that loses its energy supply contracts, and a core that contracts gets hotter.**

---

## Part III — The life cycle

![[stellar-evolution-lifecycle.svg|860]]

**1. A cloud collapses.** Stars form from **interstellar clouds of gas and dust** that contain hydrogen. Such a cloud is cold, about 10 K, and its feeble pressure normally holds it up. If a region becomes dense enough (squeezed by a passing shock wave, for example) its own gravity overcomes the pressure and it falls inward. The Orion Nebula, the fuzzy middle "star" of Orion's sword, is such a nursery, visible to the naked eye.

**2. A protostar heats up.** A **protostar** is an interstellar cloud collapsing and **increasing in temperature as a result of its internal gravitational attraction**: gravitational potential energy becomes kinetic energy of the infalling gas, and collisions turn that into random thermal motion. No fusion is happening yet; a protostar shines by the Kelvin–Helmholtz mechanism, which fails as an account of the Sun and is exactly right for a protostar. For the Sun this stage lasted about 30 million years, the number computed above.

**3. A stable star.** When the centre reaches about $10^{7}$ K, hydrogen fusion begins. The energy released stops the contraction, and the protostar **becomes a stable star when the inward force of gravitational attraction is balanced by an outward force due to the high temperature in the centre of the star**. It is now on the main sequence, where it spends about 90 % of its life. A ball below $0.08\,M_\odot$ never gets hot enough and becomes a **brown dwarf**, a failed star.

**4. The hydrogen runs out.** Fusion happens only in the hot core, and the core does not mix with the rest of a Sun-like star, so **all stars eventually run out of hydrogen** *in the core* while most of the star is still hydrogen. The core is now helium, inert at $10^7$ K because helium nuclei carry twice the charge and repel four times as strongly. With no energy supply the core contracts and heats. Hydrogen goes on fusing in a thin shell around the core, and as the core beneath it shrinks and heats, that shell burns ever more fiercely. The extra energy pushes the outer layers outward; they expand enormously and cool. The star is now brighter, far larger, and red: **most stars expand to form red giants, and more massive stars expand to form red supergiants**. The surface cools to about 3000 K while the core climbs towards $10^{8}$ K. "Red giant" describes the outside only.

![[stellar-evolution-manim.mp4]]
*First scene: the core of a Sun-like star shrinks and heats while the envelope swells and cools, with the star's point moving on the luminosity–temperature diagram; the envelope then drifts away and leaves a white dwarf. Second scene: a 25-solar-mass star lights six fuels in turn, each lasting a shorter time than the last, until iron ends the sequence.*

**5a. A star like the Sun.** At $10^{8}$ K helium fuses to carbon and oxygen, and the star settles for about a hundred million years, smaller and hotter than at its red-giant peak. Then the helium in the core runs out too. The core contracts again, but a star of this mass cannot squeeze it to the 600 million kelvin that carbon needs. The swollen outer layers, only loosely held, drift off into space as a glowing shell called a **planetary nebula**, and the exposed core is a **white dwarf at its centre**: about $0.5\,M_\odot$ packed into the size of the Earth, with no fuel, cooling for ever. (The name is an accident: in an eighteenth-century telescope the shells looked like the discs of planets. They have nothing to do with planets.)

**5b. A star above about eight solar masses.** Gravity is strong enough to keep going. Each time a fuel runs out the core contracts, heats, and lights the ash of the previous stage: helium to carbon, carbon to neon, then oxygen, then silicon, until the star is layered like an onion with an iron core. Each stage releases less energy per kilogram and runs hotter, so each is shorter. For a $25\,M_\odot$ star: hydrogen lasts 7 million years, helium 800 000 years, carbon 500 years, neon one year, oxygen five months, silicon **one day**. Iron is the end, because iron sits at the peak of the binding-energy curve in [[Nuclear Physics]] and fusing it *absorbs* energy. The iron core now has gravity and no income. When it passes about $1.4\,M_\odot$ it collapses from the size of the Earth to a ball 25 km across in a fraction of a second. The infalling outer layers rebound off this suddenly rigid core and are blown away, helped by a flood of neutrinos: the **red supergiant explodes as a supernova**, for a few weeks outshining a whole galaxy. It leaves **a nebula containing hydrogen and new heavier elements**, with **a neutron star or a black hole at its centre**. The guest star of 1054 was this.

**6. Again.** The nebula spreads into the surrounding clouds and enriches them. **The nebula from a supernova may form new stars with orbiting planets**, and those planets can be made of rock and iron only because earlier stars manufactured the elements. The Sun is such a later-generation star. The calcium in bone, the oxygen in water and the iron in blood were made inside stars that died before the Sun formed.

---

## Part IV — Mass decides, and the diagram that shows it

A more massive star has more fuel and a hotter, denser core, and fusion is so sensitive to temperature that the luminosity climbs far faster than the mass, roughly $L \propto M^{3.5}$. Lifetime is fuel divided by spending rate:

$$t \propto \frac{M}{L} \propto M^{-2.5}, \qquad t \approx 10\ \text{billion years} \times \left(\frac{M}{M_\odot}\right)^{-2.5}.$$

| Mass / $M_\odot$ | Luminosity / $L_\odot$ | Surface temperature | Main-sequence lifetime | Example |
|---|---|---|---|---|
| 0.1 | 0.002 | 3000 K, red | over 500 billion years | Proxima Centauri |
| 1 | 1 | 5800 K, yellow-white | 10 billion years | the Sun |
| 2 | 11 | 9000 K, white | 1.8 billion years | Sirius A |
| 10 | 3000 | 25 000 K, blue-white | 30 million years | Spica |
| 25 | 80 000 | 38 000 K, blue | 3 million years | the stars of Orion's belt |

Ten times the fuel is spent three thousand times faster. A blue supergiant seen tonight formed after the dinosaurs died out; no red dwarf that has ever formed has yet died, because the Universe is not old enough. (Luminosities and lifetimes come from the scaling laws, good to about a factor of two; temperatures are typical measured values.)

### The Hertzsprung–Russell diagram

Around 1910 Ejnar Hertzsprung and Henry Norris Russell independently plotted stars' **luminosity** against their **surface temperature**. By a historical accident that everyone has kept, **temperature increases to the left**; both axes are logarithmic.

![[stellar-evolution-hr-diagram.svg|900]]

If any temperature could go with any luminosity the plot would be a uniform scatter. It is not. About 90 % of stars lie on one diagonal band, the **main sequence**, running from hot and bright (upper left) to cool and dim (lower right). The main sequence is a sequence in **mass**, with heavy stars at the top. It is not a path: a star arrives at a point on it, set by its mass, and stays near that point for its whole hydrogen-burning life.

The other regions are read with one equation from [[Stellar Luminosity and Size]], $L = 4\pi R^2\sigma T^4$. At a fixed temperature each square metre of surface emits the same power, so the only way to be more luminous is to be bigger. The dotted lines of **constant radius** make this visible:

- **Red giants** (upper right): cool *and* luminous, so very large, 10 to 100 $R_\odot$.
- **Supergiants** (top): up to 1000 $R_\odot$. Put Betelgeuse where the Sun is and its surface lies beyond the orbit of Mars.
- **White dwarfs** (lower left): hot *and* dim, so tiny, about $0.01\,R_\odot$, the size of the Earth.
- The **instability strip**: a band where stars pulsate, which is where the variable stars of [[Henrietta Leavitt and the Cosmic Yardstick]] live.

The number of stars in a region tells how long stars spend there: crowded means slow, sparse means quick. That is why the main sequence holds nine stars in ten.

### The Sun's own path

![[stellar-evolution-sun-track.svg|860]]

The Sun arrived on the main sequence 4.57 billion years ago at 70 % of its present luminosity, and it brightens slowly as helium accumulates in the core. At about 10.9 billion years the core hydrogen is gone. It climbs to the tip of the red-giant branch at 12.2 billion years: 2300 times its present luminosity and 166 times its present radius, which is 0.77 AU, enough to swallow Mercury and Venus and probably the Earth. Helium ignites, the Sun drops back to 10 $R_\odot$ for a hundred million years, climbs a second time, sheds its envelope, crosses the diagram to the hot side in about ten thousand years as a bare core, and slides down the white-dwarf region, cooling at constant radius. It never explodes: it has a quarter of the mass that needs.

---

## Where it is the working tool

**Dating the oldest things in the sky.** All the stars of a cluster formed together. Plot a cluster's HR diagram and the upper main sequence is missing: the massive stars have already left, and the point where the band now ends, the **turn-off**, is a clock, because the lifetime at that mass equals the cluster's age. The oldest globular clusters turn off below one solar mass, which dates them at 12 to 13 billion years. This measurement is independent of any cosmology, and it must come out smaller than the age obtained from the expansion in [[Hubble's Law and the Expanding Universe]], which it does.

**The standard bomb.** A white dwarf that gains mass from a companion approaches the $1.4\,M_\odot$ limit derived below and detonates as a Type Ia supernova. Because the limit is the same everywhere, every such explosion has nearly the same peak luminosity: a standard candle visible across billions of light-years. In 1998 two teams used these supernovae to measure distances to remote galaxies and found the expansion of the Universe is speeding up.

**A fusion reactor cannot copy the Sun.** The Sun gets away with 15 million kelvin and a nine-billion-year wait per proton because gravity confines its fuel for free and it has $10^{57}$ protons to draw on. A reactor on Earth has neither, so it must use the far more willing deuterium–tritium reaction *and* run ten times hotter than the Sun's core, at 150 million kelvin. Every design decision in a tokamak follows from the two conditions in Part II, temperature and density, plus the confinement time that a star gets from gravity.

**Reading a star you will never visit.** Mass and age are not observable. Temperature (from colour and spectrum) and luminosity (from brightness and parallax) are, and a star's position on the HR diagram converts them into radius, mass, age and future. The Gaia spacecraft has measured parallaxes for over a billion stars, to a precision equal to the width of a human hair seen from 1000 km.

---

## Hands-on

**Find the two ends of a massive star's life in one constellation.** Orion is up in the evening from December to March (before dawn in autumn). Betelgeuse, at the hunter's shoulder, is plainly orange; Rigel, at the opposite foot, is blue-white. The colour is surface temperature, exactly as on the HR diagram: 3600 K and 12 000 K. Both are supergiants of about 20 solar masses. Rigel is the younger stage, and Betelgeuse is within about 100 000 years of its supernova. Below the three belt stars, the misty patch in the sword is the Orion Nebula, where stars are forming now. The unexplained "Great Dimming" of Betelgeuse in 2019–20 turned out to be a cloud of dust it had thrown off.

**Measure a distance by parallax.** Hold a pencil upright at arm's length in front of a distant wall or building with marks you can measure (window frames will do). Close each eye in turn and note how far the pencil jumps along the wall, $s$. Measure the distance to the wall, $D$, and the separation of your pupils, $b$ (about 6.5 cm). Similar triangles give the distance to the pencil as $d = bD/(b+s)$. Compare with a ruler. Then move the pencil nearer and further and watch the jump change; then ask how long a baseline you would need if the "pencil" were a star.

**Run the model.** `python3 stellar-evolution-model.py` prints every number in this page. Change the mass in `main_sequence()`, the radius in `collapse()`, or the composition (`mu_e`) in `white_dwarfs()` and see which conclusions move.

---

## Worked examples — every tool named

### Example 1 — from cloud to stable star (Cambridge 0625, June 2024 Paper 41, Q9)

*The Sun is one of many billions of stars in the Milky Way. (a) State the three regions of the electromagnetic spectrum in which the Sun emits the most energy. [2] (b) Radiation from the Sun travels at $3.0\times10^8$ m/s and takes 500 s to reach the Earth. Calculate the distance. [2] (c)(i) Describe and explain what happens as an interstellar cloud of gas forms a protostar. [2] (ii) Describe and explain what happens as a protostar becomes a stable star. [3]*

**(a)** *Tool: recall, backed by the blackbody fractions in Part I.* Infrared, visible light, ultraviolet. All three are needed for both marks, and one wrong addition costs a mark.

**(b)** *Trigger: a constant speed and a time. Tool: $s = vt$.* $s = (3.0\times10^{8})(500) = 1.5\times10^{11}$ m. This is 1 AU, a useful check.

**(c)(i)** *Trigger: "describe and explain" wants what happens and why.* The cloud collapses (what) because of its own internal gravitational attraction (why), and its temperature increases as it does so. Any two of the three.

**(c)(ii)** *Tool: the balance of Part II.* The temperature at the centre becomes high enough for nuclear fusion of hydrogen to start. The star is stable when the forces on it are balanced: the gravitational force acts inwards, and the outward force is due to the high temperature at the centre. Three of these four points.

### Example 2 — the two endings (Cambridge 0625, November 2023 Paper 42, Q10, with June 2023 Paper 42, Q10(c))

*Complete the sentences. (a) Protostars are formed from … (b) A protostar becomes a stable star when … is balanced by … (c) The initial fuel used to power nuclear reactions in stars is … (d) Stars approximately the same size as the Sun become red giant stars, which then form a … with a white dwarf at its centre. Then, for a star much more massive than the Sun: the stage that follows the stable state is the … stage. It then explodes as a supernova to form a …; this leaves behind a … or a ….*

*Trigger: fill-the-gap questions are marked against the syllabus's own words, so the branch must match the mass.*

(a) interstellar clouds of gas and dust. (b) the inward force of gravitational attraction; an outward force due to the high temperature in the centre of the star. (c) hydrogen. (d) planetary nebula. For the massive star: **red supergiant** (not "red giant": the question said *much more massive*); **nebula**; **neutron star**; **black hole**. When asked what the supernova's nebula contains, the accepted answers are hydrogen and new heavier elements.

### Example 3 — metres to light-years (Cambridge 0625, June 2023 Paper 42, Q10(d))

*A galaxy is moving away from the Earth at 33 000 km/s. The Hubble constant is $2.2\times10^{-18}$ per second. Calculate the distance to the galaxy in light-years. [2]*

*Trigger: a recession speed and $H_0$. Tool: $H_0 = v/d$ from [[Hubble's Law and the Expanding Universe]], then the light-year as a unit conversion.* Convert first: $v = 3.3\times10^{7}$ m/s. Then $d = v/H_0 = (3.3\times10^{7})/(2.2\times10^{-18}) = 1.5\times10^{25}$ m. One light-year is $9.5\times10^{15}$ m, so $d = (1.5\times10^{25})/(9.5\times10^{15}) = 1.6\times10^{9}$ **light-years**. The light now arriving left 1.6 billion years ago. The two classic slips are leaving the speed in km/s and multiplying by the light-year where a division is needed; a distance in light-years must be a *smaller* number than the same distance in metres.

### Example 4 — how long the Sun will last (IB Physics HL, May 2025 TZ2 Paper 2, Q7(a)–(c))

*Data for the Sun when it entered the main sequence: mass $2.0\times10^{30}$ kg; radius $7.0\times10^{8}$ m; surface temperature 5800 K; core temperature $1.5\times10^{7}$ K; core density $1.6\times10^{5}$ kg m⁻³. (a)(i) State and explain which features make fusion possible. [3] (ii) Outline how the Sun maintains its equilibrium. [2] (b) For stage 1 of the chain, ${}^1_1\text{H}+{}^1_1\text{H}\to{}^2_1\text{H}+{}^0_{+1}e+\nu$, the nuclear masses are 1.007276 u and 2.013550 u. Estimate the energy released. [2] (c) The Sun leaves the main sequence when 10 % of its hydrogen is converted. Each full chain releases $4.3\times10^{-12}$ J; $L = 3.8\times10^{26}$ W; initial hydrogen mass $1.5\times10^{30}$ kg. (i) Show that the main-sequence lifetime is about $8\times10^{9}$ years. [3] (ii) State one assumption. [1] (iii) Estimate the mass lost by the Sun in this time. [2]*

**(a)(i)** *Trigger: five data are offered and only two are relevant; choosing is the first mark.* Core temperature and core density. High temperature means high kinetic energy, needed to overcome the electrostatic repulsion between nuclei. High density means frequent collisions. Mentioning the radius or the surface temperature loses the first mark.

**(a)(ii)** Inward gravitational force (or pressure) is balanced by outward thermal, gas or radiation pressure.

**(b)** *Trigger: the masses are nuclear, so the positron is not hidden inside an atomic mass and must be subtracted by hand. Tool: $\Delta m$, then 931.5 MeV per u.* $\Delta m = 2(1.007276) - 2.013550 - 0.000549 = 4.53\times10^{-4}$ u, so $E = 4.53\times10^{-4}\times931.5 = 0.42$ MeV $= 6.8\times10^{-14}$ J. Forgetting the positron gives 0.93 MeV and one mark of two.

**(c)(i)** *Trigger: a rate (W) and a quantity per event (J) give events per second. Tool: fuel over rate.* Hydrogen to be used: $0.10\times1.5\times10^{30} = 1.5\times10^{29}$ kg. Chains per second: $3.8\times10^{26}/4.3\times10^{-12} = 8.8\times10^{37}$. Each chain consumes four protons, $4\times1.67\times10^{-27} = 6.7\times10^{-27}$ kg, so hydrogen is used at $5.9\times10^{11}$ kg/s. Lifetime $= 1.5\times10^{29}/5.9\times10^{11} = 2.5\times10^{17}$ s $= 8.1\times10^{9}$ years.

**(c)(ii)** That the luminosity (the rate of fusion) stays constant over the whole time. It does not, quite: the Sun brightens by a factor of about three across its main-sequence life.

**(c)(iii)** *Trigger: "mass lost" by a shining object. Tool: $E = \Delta m\,c^2$ on the total energy radiated.* $E = Lt = (3.8\times10^{26})(2.5\times10^{17}) = 9.7\times10^{43}$ J, so $\Delta m = E/c^2 = 1.1\times10^{27}$ kg. That is 0.05 % of the Sun, or about 180 Earths. The hydrogen *used* ($1.5\times10^{29}$ kg) and the mass *lost* ($1.1\times10^{27}$ kg) differ by the factor 0.7 %: the rest of the hydrogen is still there, as helium.

### Example 5 — parallax to brightness (IB Physics HL, November 2025 TZ1 Paper 2, Q7(a)(iii), (b))

*Star A is a main-sequence star: surface temperature 5200 K (Sun: 5800 K), parallax angle 0.74 arcsec, radius $0.9R$ (Sun: $R$). (a)(iii) Outline why regions of convection form in Star A. [2] (b)(i) Calculate, in m, the distance to Star A. [1] (ii) Show that the luminosity of Star A is about half that of the Sun. [1] (iii) Deduce the apparent brightness of Star A compared with that of the Sun. [3]*

**(a)(iii)** *Tool: convection from [[Heat Transfer]].* The core is far hotter than the surface. Hot gas near the core is less dense and rises; cooler, denser gas near the surface sinks.

**(b)(i)** *Trigger: a parallax in arcseconds. Tool: $d = 1/p$, then the conversions.* $d = 1/0.74 = 1.35$ pc $= 1.35\times3.26 = 4.4$ ly $= 4.4\times9.46\times10^{15} = 4.2\times10^{16}$ m.

**(b)(ii)** *Trigger: radius and temperature given as ratios. Tool: $L \propto R^2T^4$, in ratio form so that $\sigma$ and $4\pi$ cancel.* $L_A/L_\odot = (0.9)^2(5200/5800)^4 = 0.81\times0.646 = 0.52$.

**(b)(iii)** *Tool: $b = L/4\pi d^2$, again as a ratio.* $b_A/b_\odot = (L_A/L_\odot)\,(d_\odot/d_A)^2 = 0.52\times(1.5\times10^{11}/4.2\times10^{16})^2 = 6.7\times10^{-12}$. A star half as luminous as the Sun appears a hundred and fifty billion times fainter, entirely because of distance. (The published answer leaves it as $b_A = 0.52L_\odot/4\pi(4.2\times10^{16})^2 = 2.4\times10^{-35}L_\odot$ W m⁻², which is the same statement.)

### Example 6 — reading a radius off the diagram (constructed from Betelgeuse's measured values)

*A star has surface temperature 3600 K and luminosity $1.26\times10^{5}\,L_\odot$. State its region of the HR diagram and find its radius in solar radii and in AU.*

*Trigger: cool but enormously luminous, the corner where temperature cannot explain the light. Tool: $L \propto R^2T^4$ rearranged for $R$.*

$$\frac{R}{R_\odot} = \sqrt{\frac{L}{L_\odot}}\left(\frac{T_\odot}{T}\right)^{2} = \sqrt{1.26\times10^{5}}\times\left(\frac{5772}{3600}\right)^{2} = 355\times2.57 = 910.$$

It is a red supergiant. In metres, $910\times6.96\times10^{8} = 6.3\times10^{11}$ m $= 4.2$ AU: centred on the Sun, its surface would lie between the orbits of Mars (1.5 AU) and Jupiter (5.2 AU). On the diagram the point sits just below the $1000\,R_\odot$ line, which is the check.

---

## Common Misconceptions (Teaching Notes)

### 1. "The Sun is burning"
Burning is a chemical reaction between a fuel and oxygen, rearranging electrons and releasing a few electronvolts per atom. The Sun fuses nuclei, releasing millions of electronvolts per nucleus, and it has no free oxygen to burn with. A coal Sun lasts 5000 years.

### 2. "A bigger star has more fuel, so it lives longer"
It has more fuel and spends it disproportionately faster: $t \propto M^{-2.5}$. The heaviest stars live a few million years, the lightest for longer than the Universe has existed.

### 3. "The Sun will explode" (or "become a black hole")
A supernova needs about eight solar masses. The Sun becomes a red giant, then a planetary nebula with a white dwarf at its centre.

### 4. "A red giant is a cool star"
Its *surface* is cool because the envelope has expanded. Its core is hotter than it has ever been, 100 million kelvin against the 15 million of the main sequence. In stellar evolution the core and the envelope do opposite things.

### 5. "Stars move along the main sequence as they age"
The main sequence is a line-up of different masses, not a track. A star sits at one point for its hydrogen-burning life and then leaves sideways, to the right.

### 6. "Fusion is the outward force"
Pressure holds a star up, and the pressure comes from high temperature. Fusion's job is to replace the energy that leaks out, so that the temperature does not fall. Protostars and white dwarfs have no fusion at all and are still held up by pressure. (The 0625 mark schemes accept "force due to fusion reactions" as well as "force due to the high temperature"; the second is the better physics and the syllabus's own wording.)

### 7. "A light-year measures time"
It is the *distance* light covers in a year, $9.5\times10^{15}$ m.

---

## Exam Notes

### Cambridge 0625 (IGCSE) — §6.2.1 The Sun as a star and §6.2.2 Stars (Papers 1–4)

**Core (Papers 1 and 3):** the Sun is a medium-sized star, mostly hydrogen and helium, radiating most of its energy as infrared, visible light and ultraviolet; galaxies contain many billions of stars; the Sun is in the Milky Way; other stars are much further away than the Sun; the light-year defined as a distance. **Supplement (Papers 2 and 4):** stars are powered by nuclear reactions, which in stable stars are the fusion of hydrogen into helium; one light-year $= 9.5\times10^{15}$ m; and the eight-step life cycle (a)–(h), which Part III reproduces in the syllabus's wording. Questions are nearly all sentence completion, flow-chart completion, or "describe and explain" for two or three marks. The marks go to the exact nouns: *interstellar cloud of gas and dust*, *protostar*, *red giant* against *red supergiant*, *planetary nebula*, *white dwarf*, *supernova*, *neutron star*, *black hole*, and *hydrogen and new heavier elements* for the contents of the supernova's nebula. The stability condition must name both forces and both directions. The HR diagram, parallax, the parsec and the proton–proton chain are not on this syllabus. §6.2.3 (redshift, the Hubble constant, the cosmic microwave background) is taught in [[Hubble's Law and the Expanding Universe]], and the same question often runs across both.

### IB Physics (first assessment 2025) — E.5 Fusion and stars (SL and HL)

Equilibrium between outward radiation (or gas) pressure and inward gravitational forces; fusion as the energy source, with **energy-release calculations required**; the temperature and density conditions for fusion; the effect of mass on a star's evolution; the HR diagram, sketched and interpreted, with the main sequence, red giants, supergiants, white dwarfs, the instability strip and lines of constant radius, always with luminosity on the vertical axis and temperature on the horizontal; stellar parallax with $d(\text{parsec}) = 1/p(\text{arcsecond})$ and conversions between AU, ly and pc; stellar radii from $L$ and $T$. Cepheid variables are explicitly not required. The guide says "radiation pressure"; mark schemes accept thermal, gas or radiation pressure, and in a star like the Sun it is mainly gas pressure. Surface temperature from Wien's law and composition from spectral lines belong to the same subtopic and are taught in [[Stellar Luminosity and Size]] and [[Energy Levels and Line Spectra]].

### Where it is *not* examined

**Cambridge 9702** Topic 25 covers luminosity, standard candles, Wien, Stefan–Boltzmann, stellar radii and Hubble's law, and stops there: no life cycle, no HR diagram, no parallax. **AP Physics 1, AP Physics 2 and both AP Physics C courses** name no stellar evolution; AP Physics 2 examines fusion and mass–energy (§15.7–15.8), for which the Sun's budget in Part II is a worked context. The Chandrasekhar limit, degeneracy pressure, neutron stars in any detail, and the Schwarzschild radius are beyond every board listed here.

---

## Connections

- **Builds on:** [[Stellar Luminosity and Size]] — $L = 4\pi R^2\sigma T^4$, Wien's law and $b = L/4\pi d^2$, the three equations that make the HR diagram readable; [[Nuclear Physics]] — mass defect, the binding-energy curve, and why iron is the end; [[Gravitational Fields]] — $GM^2/R$ as an energy store; [[Kinetic Theory and the Ideal Gas]] — pressure as the thermal motion of particles.
- **Same idea elsewhere:** [[Density and Pressure]] — hydrostatic balance in a liquid; [[Heat Transfer]] — convection, which carries energy through the outer third of the Sun; [[Internal Energy]] — heating a gas by compressing it.
- **Extends into:** [[Hubble's Law and the Expanding Universe]] — supernovae as the distance markers of cosmology; [[Pauli Exclusion Principle]] — the rule that holds up a white dwarf; [[Quantum Tunnelling]] — how protons fuse at a temperature 700 times too low; [[General Relativity]] — what a black hole is.
- **Stories:** [[Henrietta Leavitt and the Cosmic Yardstick]] — the variable stars of the instability strip; [[Wolfgang Pauli and the Number 137]] — the man whose principle sets the fate of dead stars; [[The 1919 Eclipse]] — Eddington, who guessed the Sun's fuel and later mocked Chandrasekhar's limit.

---

## Beyond Syllabus

### A star gets hotter as it loses energy
Recall the rule from Part II: a core without an energy supply contracts and heats. For a ball of gas in equilibrium the thermal kinetic energy $K$ and the gravitational potential energy $U$ are tied by the **virial theorem**, $2K + U = 0$, so the total energy is $E = K + U = -K$. When the star radiates, $E$ falls, so $K$ must *rise*: half the gravitational energy released by shrinking heats the gas, and the other half is radiated. A star has a negative heat capacity. Ordinary objects cool when they lose energy; self-gravitating ones heat up, and that single oddity is what drives every stage of Part III.

### How the Sun fuses at all
Recall that fusion needs nuclei within about $10^{-15}$ m. The electrostatic barrier at that separation is 1.4 MeV, which as a thermal energy corresponds to $10^{10}$ K. The Sun's core, at $1.57\times10^{7}$ K, has a mean thermal energy of 2 keV, too small by a factor of 700. The thermal distribution has no sharp energy ceiling, but classical over-barrier collisions are far too rare to explain the observed fusion rate. [[Quantum Tunnelling]] permits transmission below the Coulomb barrier. The dominant reacting energies balance two trends: penetration becomes more likely as collision energy rises, while the Maxwell–Boltzmann population becomes smaller. Nuclear reaction physics also matters; tunnelling is not the entire rate calculation.

### The Chandrasekhar limit, computed
A white dwarf has no fusion and yet does not collapse. Its electrons are packed so tightly that the [[Pauli Exclusion Principle]], which forbids two electrons from sharing a state, forces most of them into high-momentum states. In the strongly degenerate regime, this **degeneracy pressure** depends mainly on electron density and only weakly on temperature. Cooling therefore need not remove the main support; finite-temperature, composition and crystallisation effects still matter for real white dwarfs. Put that pressure law into the hydrostatic balance and integrate from the centre outwards, which is what `white_dwarfs()` in the model does:

![[stellar-evolution-white-dwarfs.svg|820]]

Adding mass makes a white dwarf *smaller*, and the three measured white dwarfs sit on the computed curve. A teaspoon of Sirius B has a mass of 12 tonnes. As the mass grows the electrons are pushed towards the speed of light, where their pressure rises too slowly with density to keep up with gravity, and this idealised sequence tends to zero radius near $1.43\,M_\odot$. Real stars encounter additional physics before that zero-radius limit; the result identifies the limiting mass of the model. Subrahmanyan Chandrasekhar found this in 1930, aged nineteen, on the ship from India to Cambridge. In 1935 Eddington, the most famous astronomer alive, ridiculed the result at the Royal Astronomical Society, and almost nobody defended the younger man in public. Chandrasekhar was right, and received the Nobel Prize in 1983.

### Beyond the limit
A collapsing iron core above the limit crushes electrons into protons, and what remains is a **neutron star**: 1.4 $M_\odot$ in a ball 12 km in radius, at $4\times10^{17}$ kg m⁻³, the density of an atomic nucleus. The collapse releases $3\times10^{46}$ J, two hundred times what the Sun radiates in its entire main-sequence life, and 99 % of it leaves as neutrinos. On 23 February 1987 detectors in Japan, the United States and the Soviet Union caught two dozen neutrinos from a supernova in a neighbouring galaxy, hours *before* the light arrived, because the neutrinos leave the core at once while the shock needs hours to reach the surface. Spinning neutron stars are seen as **pulsars**. Jocelyn Bell found the first in 1967 as a graduate student, in a trace of "scruff" a quarter-inch long on four hundred feet of chart paper; the 1974 Nobel Prize went to her supervisor. Above about two to three solar masses not even neutrons can hold, and the core becomes a **black hole**, a region whose escape speed exceeds $c$. Its size is the Schwarzschild radius $r_s = 2GM/c^2$, which is 3 km per solar mass. (Setting Newton's escape speed $\sqrt{2GM/r}$ equal to $c$ gives the same formula. The derivation is wrong, since light is not a Newtonian projectile, and the agreement is a coincidence; the real one needs [[General Relativity]].)

### Where the heaviest elements come from
Fusion stops at iron, so supernovae cannot be the whole story of the periodic table. Elements heavier than iron are built by capturing neutrons. On 17 August 2017 gravitational waves from two merging neutron stars arrived two seconds before a gamma-ray flash from the same spot, and the glow that followed carried the spectral signature of freshly made heavy elements, several Earth masses of gold and platinum among them. The gold in a wedding ring was very probably made in a collision of two dead stars.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $d = 1/p$ | `d = 1/p` | distance in parsecs from parallax in arcseconds |
| $L = 4\pi R^2 \sigma T^4$ | `L = 4\pi R^2 \sigma T^4` | luminosity, radius and surface temperature |
| $b = L/4\pi d^2$ | `b = L/4\pi d^2` | apparent brightness |
| $E = \Delta m\,c^2$ | `E = \Delta m\,c^2` | energy from mass defect |
| $t \propto M^{-2.5}$ | `t \propto M^{-2.5}` | main-sequence lifetime against mass |
| $T_c \sim GMm_p/kR$ | `T_c \sim GMm_p/kR` | central temperature from the balance |
| $r_s = 2GM/c^2$ | `r_s = 2GM/c^2` | Schwarzschild radius |
| $M_\odot$ | `M_\odot` | solar mass |
