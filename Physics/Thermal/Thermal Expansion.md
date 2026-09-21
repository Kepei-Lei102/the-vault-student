---
chinese: 热膨胀 (rè péngzhàng)
aliases:
  - Expansion of Solids, Liquids and Gases
  - Bimetallic Strip
prerequisites:
  - "[[Kinetic Theory and the Ideal Gas]]"
  - "[[Internal Energy]]"
  - "[[Temperature and Thermometry]]"
leads_to: []
tags:
  - subject/physics
  - domain/thermal-physics
  - level/IGCSE
  - level/university
  - curriculum/Cambridge-0625
  - syllabus/0625-2-2
  - type/deep
  - misconception/particles-expand
  - misconception/holes-shrink-when-heated
  - misconception/expansion-is-too-small-to-matter
---

# Thermal Expansion 热膨胀

> *The Eiffel Tower is about fourteen centimetres taller on a hot August afternoon than on a freezing January night, and its top leans a few centimetres away from the Sun, because the sunlit side has grown more than the shaded side. Nobody adds or removes any iron. Three hundred metres of metal, warmed by forty degrees, simply takes up more room. Every bridge, railway, power line, pipeline and thermometer on Earth is designed around that fact, and the ones that were not are the ones in the photographs of buckled track.*

## Definition

### Formal

**Thermal expansion** is the increase in the size of a body when its temperature rises, at constant pressure. Nearly all solids, liquids and gases expand when heated and contract when cooled. The particles themselves do not change size: their **average separation** increases. For the same rise in temperature, **gases expand most, liquids less, and solids least**.

### Intuitive

Heating makes particles move more vigorously, and particles that move more vigorously need more room. How much more depends on how firmly they are held: in a solid they are held tightly and gain very little room, in a liquid less tightly, and in a gas they are hardly held at all.

### 中文锚点

玻璃罐头的铁盖拧不开，放到热水龙头下冲十几秒，一拧就开了。盖子没有变软，是铁受热后整体长大了一点点，比玻璃瓶口长得还多，盖子就松了。为什么受热会长大？固体里的原子像被弹簧连着，不停地抖；越热抖得越厉害。关键在于这根"弹簧"两头不一样：两个原子想靠得更近，会被狠狠顶回来；想离得更远，拉回来的力却软得多。所以抖得越厉害，原子往外荡得越远，往里却几乎挤不进去，平均下来彼此的距离就变大了。每对原子只多出一点点，可一根铁轨里排着几十亿对，加起来就是夏天能把铁轨挤弯的那几厘米。原子自己并没有变大，变大的是它们之间的空隙。

### 术语对照 (Terms)

热膨胀 thermal expansion · 收缩 contraction · 平均间距 average separation · 膨胀缝（伸缩缝） expansion gap / joint · 双金属片 bimetallic strip · 恒温器 thermostat · 线膨胀系数 coefficient of linear expansion · 热应力 thermal stress · 反常膨胀 anomalous expansion (of water)

---

## Part I — What happens, and in what order

Heat a metal rod and it gets longer, wider and thicker, all by the same fraction. Heat a liquid in a flask with a narrow tube and the level climbs the tube: that is a liquid-in-glass thermometer, described in [[Temperature and Thermometry]]. Warm a gas that is free to push a piston back, so that its pressure stays constant, and its volume grows in proportion to its kelvin temperature, as [[Kinetic Theory and the Ideal Gas]] derives.

The sizes of the three effects are very different:

![[thermal-expansion-magnitudes.svg|820]]

For each kelvin, steel grows by about 36 parts in a million by volume, water by about 210, and any gas near room temperature by 3400. The ratio **solid : liquid : gas is roughly 1 : 6 : 100**. That ordering is the thing to remember, and it has a particle explanation:

- In a **solid**, strong forces hold each particle in a fixed position. Heating makes the particles vibrate with larger amplitude about those positions, and the average separation increases only slightly.
- In a **liquid**, the forces are weaker and the particles are not fixed in place, so the same extra energy lets them move apart more.
- In a **gas**, the particles are far apart and the forces between them are negligible. Faster particles hit the walls harder and more often; if the pressure is to stay the same, the container must get bigger so that the collisions become less frequent. With nothing holding the particles together, the volume simply follows the temperature.

All gases expand by the same fraction, because no property of the particular gas is involved. Solids and liquids each have their own value, because each has its own forces.

---

## Part II — Why more vibration means more room

"The particles vibrate more, so they take up more space" is the accepted answer and it is true, but it hides a good question. A pendulum that swings wider is, on average, still in the middle. Why should a wider vibration move the *average* position at all?

The answer is in the shape of the force between two neighbouring particles, the potential well of [[Internal Energy]]. Push two atoms closer than their natural spacing and they resist ferociously: the wall of the well on the near side is almost vertical. Pull them apart and the restoring force is much gentler: the far side of the well is a long slope. The well is **lopsided**.

![[thermal-expansion-manim.mp4]]
*A particle in the well of a real bond, its motion computed from the force. Each rise in energy widens the swing, mostly outward, and the red marker (the average spacing) drifts to the right. In a perfectly symmetric well the swing widens equally both ways and the average does not move.*

![[thermal-expansion-well.svg|820]]

A particle with little energy rattles about near the bottom, where the well is nearly symmetric. Give it more energy and it climbs higher, where it can travel a long way out along the gentle slope and hardly any further in against the wall. It also moves slowly on the gentle side and so spends more time there. The time-averaged separation therefore shifts outward: in the computed well above by 1.6 %, 5 %, 11 % and 20 % at the four energies drawn. Do the same in a perfectly symmetric well, a perfect spring, and the average does not move at all (to within 0.03 %, the numerical error).

**Thermal expansion exists because the forces between atoms are lopsided.** A world of perfect springs would have heat, temperature and vibration, and nothing in it would expand.

---

## Part III — Putting numbers on it

*The 0625 syllabus asks for description and explanation only. This section is for anyone who wants to predict a size.*

For a solid, the change in length is proportional to the original length and to the temperature change:

$$\Delta L = \alpha L_0\,\Delta\theta,$$

where $\alpha$, the **coefficient of linear expansion**, is a property of the material: $12\times10^{-6}$ K⁻¹ for steel and for concrete, $19\times10^{-6}$ for brass, $23\times10^{-6}$ for aluminium, $9\times10^{-6}$ for ordinary glass, $3.3\times10^{-6}$ for Pyrex. Each side of a cube grows by the factor $(1+\alpha\Delta\theta)$, so its volume grows by $(1+\alpha\Delta\theta)^3 \approx 1 + 3\alpha\Delta\theta$, since $\alpha\Delta\theta$ is tiny and its square and cube can be dropped. The volume coefficient is therefore $3\alpha$, and the area coefficient $2\alpha$.

| Case | Calculation | Result |
|---|---|---|
| Eiffel Tower, 300 m of iron, −5 °C to 35 °C | $300 \times 12\times10^{-6} \times 40$ | 14 cm |
| 100 m steel bridge deck, same range | $100 \times 12\times10^{-6} \times 40$ | 48 mm: the width of its expansion joint |
| 300 m aluminium power line | $300 \times 23\times10^{-6} \times 40$ | 28 cm longer, which deepens the sag from 6.0 m to 8.2 m |

**What if the expansion is prevented?** Then the material is, in effect, compressed by the amount it wanted to grow, and pushes back. With the Young modulus $E$ of [[Stress, Strain and Young Modulus]], the stress is $\sigma = E\alpha\,\Delta\theta$. For a steel rail heated by 40 K this is $(2.0\times10^{11})(12\times10^{-6})(40) = 96$ MPa, a force of about 740 kN in a standard rail: the weight of seventy-five tonnes, pushing along the track. Expansion is small and the forces behind it are enormous, which is exactly why it matters.

---

## Where it is the working tool

**Gaps.** Bridges have toothed **expansion joints** at the ends of the deck, and one end of a long bridge rests on rollers. Older railway track has a small gap between sections of rail, which is what makes the clickety-clack; concrete roads and pavements are laid in slabs with soft filler between them; long pipelines carrying hot fluids have U-shaped loops that flex. **Overhead cables** are hung slack in summer so that they do not snap when they contract in winter. (Modern welded track has no gaps. The rail is stretched before it is fastened down, so that it sits in tension in winter and only mild compression in summer, and heavy sleepers hold it straight. When a heatwave beats the design, the 96 MPa calculated above wins and the track buckles.)

**The bimetallic strip.** Bond a strip of brass to a strip of steel. Heat the pair and the brass grows more, but it is fixed to the steel along its whole length, so the only way both lengths can fit is for the strip to **curve, with the brass on the outside**. The length difference is minute (35 micrometres for a 10 cm strip heated by 50 K) and the bending it produces is easy to see (the tip moves 2.6 mm).

![[thermal-expansion-bimetallic.svg|820]]

Used as a switch, the strip is a **thermostat**: as the room or the iron or the oven warms, the strip bends away from a contact and breaks the heater circuit; as it cools, it straightens and reconnects. The same strip closes a circuit in a fire alarm, flashes older car indicators, and turns the needle of an oven thermometer.

**Making things fit, and making them let go.** A steel tyre is heated until it slips over a train wheel and grips immovably once cold; rivets are driven hot and tighten as they shrink. In reverse, a jammed jar lid loosens under a hot tap because steel expands more than glass.

**Matching, so that nothing happens.** Reinforced concrete is possible only because steel and concrete happen to have the same coefficient, $12\times10^{-6}$ K⁻¹; if they differed, every summer would crack the building from inside. Dental fillings are chosen to match tooth enamel for the same reason. Ovenware is made of Pyrex because a material that barely expands is barely strained when one side is hot and the other cold, whereas thick ordinary glass cracks when boiling water is poured in.

**Gases.** Air heated by the burner of a **hot-air balloon** expands, so the same mass fills more volume, its density falls, and the balloon floats in the denser cold air around it ([[Density and Pressure]]). The same expansion drives every convection current in [[Heat Transfer]].

**The sea.** Warming the top 700 m of the ocean by 0.5 K raises it by 7 cm with no ice melted at all. Thermal expansion of seawater accounts for roughly a third to a half of the sea-level rise measured over the past century.

---

## Water breaks the rule

![[thermal-expansion-water.svg|820]]

Cool water and it contracts, like anything else, until it reaches **4 °C**. Below that it **expands** as it cools, and on freezing it expands by a further 9 %. The cause is the open, cage-like arrangement that hydrogen bonds force on water molecules as they slow down, which takes more room than the jumble of the warmer liquid.

Two consequences shape the planet. Ice floats. And a pond freezes from the top: as the surface cools towards 4 °C the water there becomes denser and sinks, but once it is colder than 4 °C it is *lighter* than the water below and stays on top, where it freezes into a lid that insulates the rest. The bottom of a deep lake stays at 4 °C all winter, and the fish live. The same expansion bursts water pipes and splits rocks.

---

## Hands-on

**The jar lid.** Run a hot tap over the metal lid of a stuck jar for fifteen seconds, keeping the glass as dry as you can, and open it. Then explain why heating the whole jar evenly in a bowl of hot water works less well.

**A gas thermometer.** Stretch a balloon over the neck of an empty bottle. Stand the bottle in a bowl of hot water and watch the balloon rise; then put it in the fridge. Nothing entered or left the bottle.

**The ball and ring**, if your school has one: a metal ball that just passes through a ring when cold will not pass when the ball is heated, and passes again if the ring is heated too. Predict, before trying, what happens to the *hole* in a heated ring.

**Run the model.** `python3 thermal-expansion-model.py` prints every number here. Change the well to a symmetric one, or change the rail temperature, and see which conclusions move.

---

## Worked examples — every tool named

### Example 1 — greatest and least (Cambridge 0625, June 2023 Paper 43, Q3(a))

*(i) State which state of matter, solid, liquid or gas, has the greatest thermal expansion and which has the least. [2] (ii) Describe, in terms of the motion and arrangement of particles, the structures of solids and gases. [3]*

**(i)** *Tool: the ordering of Part I.* Greatest: gas. Least: solid.

**(ii)** *Trigger: "motion and arrangement" names the two things each answer needs.* Solids: particles vibrate, in fixed, close-packed positions. Gases: particles move freely and quickly, randomly arranged and widely separated. Any three of these points score.

### Example 2 — the gaps in a railway (Cambridge 0625, November 2025 Paper 43, Q4(b))

*Small gaps are left between sections of a steel rail. State why the gaps are needed, and explain your answer in terms of particles. [2]*

*Trigger: "state" then "explain in terms of particles": one mark for the engineering reason, one for the particle reason.* **Statement:** the rail expands when it is heated, and the gap gives it room, which prevents the track from buckling. **Explanation:** the particles vibrate faster (they have more kinetic energy), and the average separation between them increases.

### Example 3 — a heated dish (Cambridge 0625, November 2024 Paper 41, Q4(b)(ii))

*Boiling water is poured into an aluminium dish at room temperature. Explain, in terms of its particles, why the aluminium expands. [2]*

*Tool: temperature rise means more kinetic energy; expansion means greater separation.* The particles gain kinetic energy as the temperature of the aluminium rises. The average separation of the particles increases. Writing "the particles expand" loses the mark: the published schemes flag it as wrong.

### Example 4 — why hot air rises (Cambridge 0625, June 2026 Paper 31, Q5(a))

*A flame heats the air in a hot-air balloon. Explain why the hot air rises. [2]*

*Trigger: "rises" is a density question; expansion is the step before it.* The heated air expands (its particles move further apart), so it is less dense than the cooler air around it.

### Example 5 — designing the gap (constructed)

*A steel bridge deck is 250 m long at 10 °C. The design temperatures are −15 °C and 45 °C. How wide must the joint be when the deck is installed at 10 °C, and how much may the deck shrink?*

*Trigger: a length and two temperature changes from the installed state. Tool: $\Delta L = \alpha L_0\Delta\theta$ with $\alpha = 12\times10^{-6}$ K⁻¹.* Expansion from 10 °C to 45 °C: $12\times10^{-6}\times250\times35 = 0.105$ m, so the joint must be at least **10.5 cm** open on installation day. Contraction from 10 °C to −15 °C: $12\times10^{-6}\times250\times25 = 0.075$ m, so in the coldest weather the gap opens to 18 cm, which is why the joint is made of interlocking steel fingers and not an open slot.

---

## Common Misconceptions (Teaching Notes)

### 1. "The particles expand"
The particles keep their size. Their average separation increases. This is the single most penalised sentence in the topic.

### 2. "A hole in a heated plate gets smaller, because the metal grows into it"
The hole gets **bigger**, by exactly the fraction the plate does. Imagine the plate without a hole and draw a circle on it: when the plate expands, the circle expands with it, and cutting out the disc changes nothing about where its edge goes. This is why heating the ring lets the ball through.

### 3. "Solids barely expand, so it doesn't matter"
The size is small and the force is huge. A rail that is not allowed its 0.05 % pushes back with seventy-five tonnes.

### 4. "Hot air rises because heat rises"
Energy has no tendency to go upward. Heated air expands, becomes less dense than its surroundings, and is pushed up by the denser air around it.

### 5. "A thermometer works because the liquid expands and the glass doesn't"
Both expand. The liquid expands several times more, and the reading is the difference.

---

## Exam Notes

### Cambridge 0625 (IGCSE) — §2.2.1 Thermal expansion of solids, liquids and gases (Papers 1–4)

**Core:** describe qualitatively the expansion of solids, liquids and gases **at constant pressure**; describe everyday applications and consequences (gaps in rails and bridges, the bimetallic strip and thermostat, liquid-in-glass thermometers, overhead cables, fitting and loosening, hot-air balloons). **Supplement:** explain, in terms of the motion and arrangement of particles, the relative order of magnitude of expansion: gases most, liquids next, solids least. The standard two-mark explanation pairs *particles gain kinetic energy / vibrate faster* with *average separation increases*. No formula and no coefficient is required. The anomalous expansion of water is not on the syllabus.

### Where it is *not* examined

**Cambridge 9702** meets expansion only as one example of a thermometric property in §14.2, with no quantitative treatment. The **IB Physics** guide (first assessment 2025) and the current **AP Physics 1, AP Physics 2 and AP Physics C** frameworks do not list thermal expansion of solids and liquids; gas expansion at constant pressure is part of the ideal-gas work in each. $\Delta L = \alpha L_0\Delta\theta$ belongs to first-year university physics and engineering.

---

## Connections

- **Builds on:** [[Kinetic Theory and the Ideal Gas]] — the three states in particles, and $V \propto T$ for a gas at constant pressure; [[Internal Energy]] — the lopsided potential well between two molecules; [[Temperature and Thermometry]] — expansion as the working property of a liquid-in-glass thermometer.
- **Same topic on the syllabus:** [[Specific Heat Capacity]] — how much energy a temperature rise costs, and melting, boiling and evaporation.
- **Extends into:** [[Heat Transfer]] — expansion makes a fluid less dense, and that drives convection; [[Density and Pressure]] — why the less dense air floats; [[Stress, Strain and Young Modulus]] — the force when expansion is prevented.
- **Mathematics:** [[Binomial Theorem]] — $(1+x)^3 \approx 1+3x$ for small $x$, the step that turns $\alpha$ into $3\alpha$.

---

## Beyond Syllabus

### The alloy that does not expand
Recall that expansion comes from the lopsided well. In 1896 Charles-Édouard Guillaume found an iron–nickel alloy, 36 % nickel, whose coefficient is a tenth of steel's: as it warms, a magnetic effect shrinks the lattice almost exactly as fast as the vibrations swell it. He called it **invar**, for invariable, and it earned him the 1920 Nobel Prize. Pendulum rods, surveying tapes, the shadow masks of old colour televisions and the inner tanks of ships that carry liquefied natural gas at −162 °C are made of it.

### Things that shrink when heated
A stretched rubber band gets *shorter* when warmed: heat makes its long chain molecules coil up more randomly, an effect of [[Entropy and the Second Law]] and not of the bond well at all. A few crystals, zirconium tungstate among them, contract over a wide range of temperatures because their lattice can fold as it vibrates. Water between 0 and 4 °C belongs to the same small family.

### How the average shifts, in one line
Near its minimum the well can be written $U = \tfrac12 kx^2 - gx^3$, where $x$ is the displacement from the cold spacing and the cubic term is the lopsidedness. Averaging over the thermal motion gives a mean displacement $\langle x\rangle = 3gk_BT/k^2$: proportional to the temperature, which is why $\Delta L \propto \Delta\theta$, and proportional to $g$, which is why a symmetric well ($g = 0$) gives none.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\Delta L = \alpha L_0\,\Delta\theta$ | `\Delta L = \alpha L_0\,\Delta\theta` | linear expansion |
| $\Delta V = 3\alpha V_0\,\Delta\theta$ | `\Delta V = 3\alpha V_0\,\Delta\theta` | volume expansion of a solid |
| $\sigma = E\alpha\,\Delta\theta$ | `\sigma = E\alpha\,\Delta\theta` | stress when expansion is prevented |
| $V \propto T$ | `V \propto T` | a gas at constant pressure |
| $\langle x\rangle = 3gk_BT/k^2$ | `\langle x\rangle = 3gk_BT/k^2` | mean displacement in a lopsided well |
