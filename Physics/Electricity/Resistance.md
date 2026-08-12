---
chinese: 电阻 (diànzǔ)
prerequisites:
  - "[[Electric Current]]"
leads_to:
  - "[[Kirchhoff's Laws]]"
  - "[[Potential Dividers]]"
  - "[[Internal Resistance]]"
tags:
  - subject/physics
  - domain/electromagnetism
  - level/IGCSE
  - level/A-Level
  - level/AP
  - syllabus/9702-9-2
  - syllabus/9702-9-3
  - syllabus/0625-4-2
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - curriculum/IB-Physics
  - type/deep
  - misconception/ohms-law-is-v-equals-ir
  - misconception/resistance-is-a-material-property
  - misconception/gradient-of-iv-graph-is-resistance
  - misconception/heating-always-raises-resistance
  - misconception/biggest-resistor-gets-hottest
---

# Resistance 电阻

> *Wire up a torch bulb, turn the supply up in steps, and plot current against voltage. Every textbook has promised you a straight line through the origin — Ohm's law. What you get is a line that bends over and flattens. Nothing is broken: not your circuit, not your meters, and not Ohm's law, because the lamp was never obeying it in the first place. Hidden in that bend is one sentence that reorganises the whole topic — **$V = IR$ is a definition and cannot be false; Ohm's law is a claim about materials, and it is false more often than it is true.** Hold those two apart and four graphs you were told to memorise stop being four graphs. They become four answers to a single question: when you push harder, what does this component do to its own resistance?*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| potential difference (p.d.) | 电势差 / 电压 | energy handed over per unit charge crossing a component |
| volt (V) | 伏特 | one joule per coulomb |
| electromotive force (e.m.f.) | 电动势 | energy *supplied* per unit charge by a source — not a force |
| voltmeter | 电压表 | meter connected **across** a component |
| resistance | 电阻 | the p.d. needed per unit current, $R = V/I$ |
| ohm (Ω) | 欧姆 | one volt per ampere |
| Ohm's law | 欧姆定律 | the claim that $R$ stays constant — an experimental fact, not a definition |
| ohmic / non-ohmic | 欧姆导体 / 非欧姆导体 | obeys that claim / doesn't |
| I–V characteristic | 伏安特性曲线 | the graph of current against p.d. for one component |
| filament lamp | 白炽灯 | the classic non-ohmic component — it heats itself |
| semiconductor diode | 半导体二极管 | a one-way valve: tiny $R$ forwards, huge $R$ backwards |
| thermistor (NTC) | 热敏电阻 | resistance falls as temperature rises |
| light-dependent resistor (LDR) | 光敏电阻 | resistance falls as light gets brighter |
| resistivity $\rho$ | 电阻率 | the material's own share of the resistance, in Ω m |
| electrical power | 电功率 | energy per second delivered to a component |
| kilowatt-hour (kW h) | 千瓦时 / 度 | the billing unit — one 度 is 3.6 MJ |
| Joule heating | 焦耳热 | the heat those collisions dump into the lattice |

## The price of passage — potential difference

[[Electric Current]] left one debt unpaid. It showed that the same current flows into and out of every component — nobody joins the parade, nobody leaves it — and then said that what *does* get spent is energy. Here is the accounting.

A charge crossing a component arrives with energy and leaves with less. **Potential difference is the energy transferred per unit charge:**

$$V = \frac{W}{Q}$$

One **volt** is one joule per coulomb. So "a 6 V lamp" is a promise about a rate of exchange: every coulomb that gets through hands over six joules. Multiply by how many coulombs go through per second and you have the power — which is the next section, and is really the only reason p.d. matters.

Notice what this fixes. Current is the thing that is *conserved* around a loop; p.d. is the thing that is *spent*. A student's stubborn feeling that "current gets used up" is the right instinct pointed at the wrong quantity: something certainly gets used up, and it is joules per coulomb, not coulombs per second.

> [!tip] The water cycle says it better than any pipe
> Rain falls, rivers run to the sea, the sea evaporates, cloud forms, rain falls again. Almost none of that water is ever *used up* — the same molecules have been going round for billions of years, and the sea does not slowly empty. What gets spent on each lap is **energy**, in two instalments: the gravitational potential energy the water gives away as it runs downhill, and the latent heat that has to be paid all over again to lift it back into the air as vapour. The loop keeps turning only because something outside it keeps paying — the Sun, with a little help from geothermal heat.
>
> A circuit is that cycle with charge in place of water. The carriers go round and round and are never consumed. What is spent on each lap is energy per unit charge — the potential *drop* across each component, exactly as the river spends its height. And the loop only keeps turning because the cell keeps paying, which is precisely what an e.m.f. is: the Sun of the circuit. The analogy is unusually honest here, because electric potential really *is* potential — the volt is a height, and the p.d. across a lamp is the waterfall.

**The source-side twin — e.m.f.** A cell does the opposite job: it *gives* each coulomb energy and sends it back out. The **electromotive force** of a source is the electrical work it does per unit charge driving that charge all the way round a complete circuit:

$$E = \frac{W}{Q}$$

Same units — volts — same shape of definition, opposite direction of energy flow. The name is a nineteenth-century misnomer that stuck. **An e.m.f. is not a force.** It is measured in volts, not newtons; it is an energy per unit charge, dimensionally identical to p.d. and dimensionally unlike anything in $F = ma$. Nothing in the definition, the units or the physics has any business being called a force — only the nineteenth century does. A 1.5 V cell hands 1.5 joules to every coulomb it pushes round the loop; a 1.5 V lamp takes them back. (In a real cell some of that energy is spent inside the cell itself before the charge ever reaches the terminals — that shortfall is [[Internal Resistance]].)

**Measuring it.** [[Electric Current]] put the ammeter *in* the parade — in series, built with as little resistance as possible so joining the line doesn't slow it. The voltmeter is its mirror image. It compares the energy per coulomb at two points, so it goes **in parallel**, connected *across* the component, and it must have as **high** a resistance as possible so that almost no current is diverted through it. One principle, two opposite designs:

> [!tip] The meter must not change what it measures
> An ammeter joins the traffic, so it is built not to obstruct: series, low resistance. A voltmeter taps the pressure, so it is built not to leak: parallel, high resistance. Get the pairing backwards — a voltmeter in series, an ammeter across a battery — and you read nothing and blow the fuse respectively. Analogue meters need a sensible range chosen so the needle swings wide; digital meters range themselves.

## Resistance — the definition that cannot be false

Push a given p.d. across a component and some current results. Some components let a lot through, some very little. The ratio is the number that says which:

$$\boxed{\,R = \frac{V}{I}\,} \qquad\Longleftrightarrow\qquad V = IR$$

**Resistance is the potential difference required per unit current.** One **ohm** is one volt per ampere: a component has a resistance of 1 Ω if 1 V across it drives 1 A through it.

This is a *definition*. You can always divide the voltage you measured by the current you measured, and the quotient is always the resistance at that operating point — the way you can always divide a distance by a time and call the quotient an average speed. Definitions do not fail experimental tests, because they are not making any claim.

**Why there is anything to divide.** [[Electric Current]] found the carriers crawling at fractions of a millimetre per second while their thermal speed is a thousand kilometres per second. That gap is what resistance *is*. The field accelerates each free electron — and then it collides with the vibrating lattice, and whatever forward drift it had gained is thrown away and it starts again. Accelerate, crash, accelerate, crash. The drift velocity is not the speed of a free fall; it is a **terminal velocity**, the balance point where the field's push equals what the collisions take back.

![[resistance-collision-sawtooth.svg|697]]

That single picture carries most of what follows. The *steepness of each ramp* is the field. The *frequency of the crashes* is the resistance. Heat the lattice so its ions vibrate through wider arcs, and the crashes come sooner: same push, less drift, less current — a larger $R$.

Say that last step in symbols, because it is the whole link and it is one line. Substitute the parade formula into the definition:

$$R = \frac{V}{I} = \frac{V}{nAvq}$$

For a given wire pushed by a given p.d., everything on the right is fixed except the drift velocity — so **$R \propto 1/v$**. More drift for the same push *is* less resistance; less drift for the same push *is* more resistance. The two panels of the figure are not an illustration of resistance, they are a measurement of it.

Watch it happen. The field is identical in all three beats below and so is the clock, so the only thing that differs is how often the electron is stopped — which means **how far it gets across the lattice in the same ten seconds is the resistance**, with no readout needed.

![[resistance-lattice.mp4]]

The third beat is the one that should bother you, and it is answered at the end.

**Ohm's law — the claim.** Georg Ohm measured his way to a genuine discovery in 1827: for a metal wire held at a steady temperature, the current is *proportional* to the p.d. — double the volts, exactly double the amps, so the ratio $V/I$ doesn't budge.

> **Ohm's law:** the current in a metallic conductor is directly proportional to the potential difference across it, provided the temperature and other physical conditions stay constant.

Read the sentence twice, because everything is in the fine print. It names a class of materials (metals), it attaches a condition (constant temperature), and its whole content is the word *proportional*. It is an empirical fact about how certain stuff behaves — checkable, and often false.

So the split is:

| | what it is | can it be false? |
|---|---|---|
| $R = V/I$ | the **definition** of resistance | no — it defines the symbol |
| Ohm's law | the **claim** that $R$ is constant | yes, and usually is |

The analogy that makes it stick: "average speed $=$ distance $\div$ time" is a definition, and no journey can violate it. "This car travels at constant speed" is a claim about the journey, and most journeys break it. Ohm's law is the second kind of statement. A component that keeps its promise is called **ohmic**; one that doesn't is **non-ohmic** — and outside a plain wire held cool, non-ohmic is the normal case.

**On the bench.** To measure $R$: put the component in series with an ammeter and a variable supply, and a voltmeter across the component. Take pairs of readings as you turn the supply up, and compute $V/I$ at each. Better than any single pair: plot $I$ against $V$ and take the gradient of the best-fit line, which is $1/R$ — a line through many points averages away the random scatter that one reading carries in full, which is the discipline of [[Repeated Measurements]] applied to a graph. And the graph does something a single number can't: it tells you whether $R$ was constant at all.

If the definition is just a division, why is measuring resistance a whole discipline? Because that innocent instruction — *measure $V$, measure $I$* — leaks in about five places at once:

> [!warning] Why an honest $R$ is harder to get than $R = V/I$ makes it look
> - **The measurement heats the sample.** Driving current through a resistance *is* power, $I^2R$, so the act of measuring raises the temperature and moves the very thing you are measuring. Careful work uses the smallest current that still gives a readable signal, or short pulses with cooling gaps between them.
> - **The meters load the circuit.** No ammeter has zero resistance and no voltmeter has infinite resistance, so one of them always corrupts the reading. Put the voltmeter across the component alone and the ammeter also counts the current leaking through the voltmeter; put it across component-and-ammeter and the voltmeter also counts the ammeter's own drop. There is no wiring that escapes both — you choose whichever error is smaller for the resistance in front of you, which is why the choice depends on whether $R$ is large or small.
> - **The leads have resistance too.** Trying to measure $0.01\ \Omega$ through leads and contacts worth $0.1\ \Omega$ measures the leads. The fix is the **four-terminal (Kelvin) method**: two wires carry the current, two *separate* wires sense the voltage right at the sample's own surface, and because the sense wires carry essentially no current their resistance drops essentially nothing. Every serious low-resistance measurement in the world is made this way.
> - **Junctions of dissimilar metals make their own small voltages** — the thermocouple effect, the same physics as a temperature probe — which add a fixed offset to the reading. The standard cure is to reverse the current and average the two results: the offset cancels, the real drop doesn't.
> - **And the answer is only true at the temperature it was taken at**, which is why every resistivity table in existence carries a temperature at the top.
>
> None of this contradicts $R = V/I$. It is all the price of getting an honest $V$ and an honest $I$ — and it is a good reminder that a definition being unfalsifiable does not make it easy.

## Four characteristics, one question

Sweep the p.d. across a component both ways and plot the current. The shape of the graph *is* the answer to: **when you push harder, what happens to this component's own resistance?**

![[resistance-iv-characteristics.svg|780]]

**1 — Metallic conductor at constant temperature.** $R$ doesn't change. The graph is a straight line through the origin, identical in both directions, and its gradient is $1/R$. This is the one panel that obeys Ohm's law, and it does so only because "at constant temperature" has been arranged — a thin wire in a water bath, or currents kept small enough that self-heating is negligible.

**2 — Filament lamp.** $R$ climbs. The chain of cause is the examinable part, and it runs in one direction only:

> larger current → more power dissipated ($P = I^2R$) → filament temperature rises, to around 2500 °C → lattice ions vibrate through wider arcs → electrons are scattered more often → drift falls per unit push → **$R$ increases** → the curve bends towards the $V$ axis.

The dashed line on that panel is what the lamp would have done if it had stayed cold. The gap between the dashed line and the real curve is the heating, drawn.

**3 — Semiconductor diode.** $R$ depends on *direction*. Forward-biased, almost nothing flows until about 0.6 V for silicon; past that knee the current climbs almost vertically and $R$ collapses to a few ohms. Reverse-biased, $R$ is enormous and effectively nothing gets through. This is a one-way valve, and it is what turns a.c. into d.c. in every power adapter you own. Make it out of the right compound and each carrier that crosses pays its energy out as a photon instead of as heat, which is the [[Stories/The Blue LED]] story. What the junction is actually doing to earn that asymmetry — two differently doped regions, the depletion layer between them, and a barrier that one direction of push demolishes and the other reinforces — is [[Diodes]].

**4 — Thermistor and LDR.** These are components whose resistance answers to the *world* rather than to the circuit. An NTC **thermistor**'s resistance falls as it gets hotter; an **LDR**'s resistance falls as the light on it gets brighter. Both are the opposite of the metal, and the fourth panel shows the two temperature curves crossing.

Here is the reason, and it is the best idea in the topic. Go back to $I = nAvq$ from [[Electric Current]]. Heat attacks *different factors* in the two materials:

- In a **metal**, $n$ is fixed — roughly one free electron per atom, whatever you do to it. Heating can only shorten the free flights, so $v$ falls and **$R$ rises**.
- In a **semiconductor**, heating shortens the free flights too — but it also *frees new carriers*, tearing electrons loose from bonds that were holding them. $n$ climbs **exponentially**, and that swamps the loss in $v$ completely. So **$R$ falls**, steeply.

The LDR is the same sentence with photons doing the liberating instead of heat: a photon of sufficient energy frees a bound electron, $n$ rises, $R$ falls. (Light knocking electrons free is the same physics as the [[Photoelectric Effect]].)

**What the two components physically are**, because "a resistance that answers to the world" is abstract until you have held one. A **thermistor** — *thermal resistor* — is a bead, disc or thin chip of **sintered metal-oxide ceramic**: a pressed and fired mixture of manganese, nickel, cobalt, iron and copper oxides, with two wires embedded in it and the whole thing sealed under glass or epoxy. That ceramic is a semiconductor, which is the entire point of choosing it — heating frees carriers in it. Beads can be under a millimetre across, so there is very little of it to warm up and it responds in a fraction of a second, which is why the same component reads a car's coolant, a 3D printer's nozzle and a hospital thermometer. An **LDR** is a *light-dependent resistor* in full — also sold as a **photoresistor** or *photoconductive cell* — and is a zig-zag track of **cadmium sulfide** printed on a ceramic disc behind a clear window. The serpentine shape is not decorative: it packs a long, thin track into a small illuminated area, which is $\rho L/A$ being deliberately maximised. Cadmium sulfide is chosen because its band gap happens to sit in the visible range, so it responds to roughly the light a human eye responds to — and it is being designed out of new products for exactly the reason you would guess, since cadmium is a restricted heavy metal and photodiodes now do the job.

> [!question] Does a thermistor's resistance just keep falling forever?
> No — and the reason is the same $I = nAvq$ bookkeeping, read one step further. The exponential fall happens because heat is *liberating carriers*, so $n$ climbs. But there is a finite supply: once essentially every carrier the material has to give has been freed, $n$ **saturates** and stops helping. Heat is still shortening the free flights, though, so the $v$ term keeps getting worse — and with nothing left to offset it the resistance flattens out, bottoms, and then **rises with temperature exactly like a metal**. Every NTC thermistor therefore has a minimum resistance somewhere past the top of its useful range, which is why its datasheet specifies one (typically −55 °C to around +150 °C, some grades to 300 °C) and promises nothing beyond.
>
> That turning point is the tidiest possible summary of this whole section: a semiconductor behaves like a semiconductor only while $n$ is still winning, and once $n$ runs out it behaves like a metal — because *metal* is precisely the case where $n$ was fixed from the start. The two curves in the figure are not two rules. They are the same rule at two stages.
>
> One practical consequence, because it destroys components. Below that turning point an NTC is a **positive feedback loop**: more current → more $I^2R$ heating → lower resistance → more current still. Unchecked, that is thermal runaway and the device cooks itself, which is why every thermistor circuit limits the current through it. Harnessed deliberately, the same runaway makes an NTC an excellent **inrush-current limiter** — cold and resistive at the instant of switch-on when the surge would happen, hot and nearly invisible a second later.

A metal and a semiconductor respond to heat in opposite directions not because they are mysteriously different, but because the same equation has more than one factor in it, and heat gets hold of a different one in each.

> [!warning] $R$ is the chord, not the tangent
> On a curved $I$–$V$ characteristic, the resistance at a point is $V/I$ — the gradient of the line from **the origin** to that point. It is *not* the gradient of the curve there. Two separate errors hide in "the gradient gives the resistance": on an $I$–$V$ graph even a straight line's gradient is $1/R$, not $R$; and on a curve, the tangent gives $\mathrm{d}V/\mathrm{d}I$, a genuinely useful quantity called the *dynamic* resistance, but not the $R$ that $R = V/I$ defines. Always drop back to the two numbers on the axes and divide.
>
> The tangent is not useless, though — it answers a *different* question. The **dynamic** (or small-signal) resistance $r_d = \mathrm{d}V/\mathrm{d}I$ says: with the component sitting at this operating point, if you wiggle the voltage a little, how much does the current wiggle? That is the number every radio detector, voltage reference and transistor amplifier is designed with, because a diode held at a fixed bias behaves, *to small signals*, exactly like an ordinary resistor of $r_d$ ohms. Just never call it $R$: at a filament lamp's normal operating point $r_d$ runs to roughly **twice** the chord value, and the two are answers to two different questions. [[Diodes]] is where the distinction really earns its keep, because past the knee a diode's chord resistance and its tangent resistance differ by orders of magnitude.

## Resistivity — geometry × material

A copper wire in a lamp cord and a copper busbar in a substation are the same metal with wildly different resistances. So resistance is a property of an **object**, not of a substance. To get at the substance you have to divide the geometry out — the hunter's move of separating what changes from what doesn't.

Two pieces of reasoning do it, and neither needs any new physics:

- **Double the length.** The carriers now run twice the gauntlet — two identical wires end to end, which is two resistances in a row. $R$ doubles. So $R \propto L$.
- **Double the cross-sectional area.** Now there are two identical lanes side by side, each taking its own share of the current at the same p.d. $R$ halves. So $R \propto 1/A$.

![[resistance-geometry.svg|760]]

Put them together and the constant of proportionality is everything the geometry has left behind — the material itself. That constant is the **resistivity** $\rho$:

$$\boxed{\,R = \frac{\rho L}{A}\,} \qquad\Longleftrightarrow\qquad \rho = \frac{RA}{L}$$

Units follow from the rearrangement: $\Omega \cdot \text{m}^2 / \text{m} = \Omega\ \text{m}$. ✓ Read it as a price: $\rho$ is what the material charges per metre-of-length per square-metre-of-width, and $L/A$ is how much of that you bought.

> [!info] Where $\rho$ actually comes from — and yes, $I = nAvq$ hands it to you
> The series-and-parallel argument proves $R \propto L/A$ but leaves $\rho$ as a black box labelled *whatever the material contributes*. Open the box with the formula already in hand. Start from the definition and substitute the parade:
> $$R = \frac{V}{I} = \frac{V}{nAvq}$$
> One physical input is needed, and it is the only genuinely new idea: **the drift velocity is set by the field**. Write $v = \mu E$, where the constant $\mu$ is the material's **carrier mobility** — how much drift you get per unit field, in m² V⁻¹ s⁻¹. For a uniform wire the field is just the p.d. spread along the length, $E = V/L$, so $v = \mu V / L$. Substitute that in:
> $$R = \frac{V}{nAq \cdot \dfrac{\mu V}{L}} = \frac{1}{nq\mu} \cdot \frac{L}{A}$$
> Two things happen at once, and both are worth pausing on. **The $V$ cancels** — so $R$ comes out independent of the p.d. applied, which is Ohm's law arriving as a *consequence* rather than an assumption, and it holds exactly as long as $\mu$ itself doesn't depend on the field. And **the geometry separates itself from the material** with no help from us, leaving $L/A$ on one side and, on the other,
> $$\boxed{\;\rho = \frac{1}{nq\mu}\;}$$
> Resistivity is *nothing but* the carrier count and how freely those carriers move. Copper's $\rho$ is tiny because $n$ is enormous. Pure silicon's is huge because $n$ is minute — and falls when you heat it because $n$ climbs. Nichrome's is sixty times copper's because alloying scatters carriers and cuts $\mu$, without changing $n$ much at all. Every row of the ladder below is one of those two numbers, or both. (And $\mu$ opens one level further still — see the relaxation-time box near the end, which gives $\mu = q\tau/m$ and therefore $\rho = m/nq^2\tau$.)

**The trap worth learning once.** Wires are specified by *diameter*, not area, and $A = \pi d^2/4$. Doubling a wire's diameter does not halve its resistance — it **quarters** it. Halving the diameter quadruples it. More exam marks are lost here than to any concept in the topic.

**The range is the headline.**

![[resistance-resistivity-ladder.svg|760]]

Twenty-six powers of ten separate copper from fused quartz. No other everyday property of matter — density, strength, heat capacity, refractive index — ranges over anything remotely like that, and it is precisely why electrical engineering is possible at all: a wire and its insulation can sit a millimetre apart and do opposite jobs with total reliability. Notice also the doped-versus-pure silicon pair. Six decades apart, same element. In a metal the carrier density is whatever nature handed you; in a semiconductor it is *specified*, deliberately seeded atom by atom, and that single fact is the entire semiconductor industry.

**Choosing a material is choosing a $\rho$.** Copper wires the house because its $\rho$ is nearly the lowest available and it is far cheaper than silver. Overhead transmission lines are aluminium even though its $\rho$ is about 60% higher — because aluminium is a third the density, and a cable hung between pylons is paying for every kilogram it asks the towers to hold. A kettle element or a toaster is **nichrome**, whose $\rho$ is some sixty times copper's: you want a wire that resists, because resisting is exactly how it heats. And an appliance flex has a copper core inside a PVC sleeve some $10^{20}$ times more resistive — the same wire assembly, carrying and blocking at once.

> [!question] Then why are good connectors gold-plated?
> Not for conductivity: gold's resistivity, $2.4 \times 10^{-8}\ \Omega$ m, is *worse* than copper's. The reason is what happens at the surface. Copper doesn't rust — that is iron — but it does **tarnish**, growing a film of oxide and sulfide in ordinary air, and that film is a poor conductor. Along the *body* of a cable the film is irrelevant, because the current runs through the metal underneath it. At a **contact**, where two surfaces merely touch, that film *is* the path, and a tarnished plug can develop more resistance in its last micrometre than in the whole cable behind it. Gold is the one common metal that does not oxidise at all, and it is soft enough to flatten into intimate contact under spring pressure. So the sensible design is exactly the one you see on a good connector: copper for the metres, two microns of gold flash at each end. Gold-plated *cable* is marketing; a gold-plated *contact* is engineering.

**And when you cannot lower $\rho$, you buy $A$.** There is a ceiling on material choice — copper and aluminium are essentially as good as affordable metals get — so at extreme currents the only lever left in $R = \rho L/A$ is the denominator, and engineers pull it hard enough to be funny. An aluminium smelter is electrolysis at industrial scale, and a single potline runs **hundreds of kiloamps**; at those currents $I^2R$ would destroy anything sensible, so the busbars are aluminium slabs a person could lie down on. At a power station the link from the turbine generator to its step-up transformer carries tens of kiloamps as *isolated-phase busduct* — an aluminium tube as thick as your torso, inside a housing wider than you are. It is the least glamorous hardware in the building, and it is nothing but $\rho L/A$ read backwards: you cannot change what aluminium charges, and you cannot shorten a wire that has to reach the transformer, so the only thing left to do is make it enormous.

![[resistance-busbar-comic.png|760]]

(Two footnotes on the table. Pure water is a genuinely poor conductor, around $10^5\ \Omega$ m — it is the dissolved ions in tap water, sweat and seawater that make wet hands dangerous, not the water. And $\rho$ itself is temperature-dependent: the value quoted for any material is a value *at a stated temperature*, which is the loose thread the filament lamp pulls on.)

## Power — and where the energy actually goes

Every coulomb crossing a component hands over $V$ joules, and $I$ coulombs cross every second. So joules per second — **power** — is the product:

$$\boxed{\,P = VI\,}$$

That is the whole derivation: energy-per-charge times charge-per-second. Now substitute the definition of resistance in each direction. Putting $V = IR$ into $P = VI$ gives one form; putting $I = V/R$ gives the other:

$$P = VI = I^2R = \frac{V^2}{R}$$

Three formulas, one equation. Over a time $t$ the energy delivered is $E = Pt = VIt$.

> [!warning] All three are true — of the *same component*
> The trio only holds when every symbol belongs to the one component you are talking about. The classic disaster is feeding a transmission line's resistance the grid's 400 kV, which is the voltage across the whole line-and-load, not across the cable. [[Electromagnetic Induction]] works that exact case through in full. The habit that prevents it: **reach for the formula whose symbols you actually know for this component.** If the current through it is what you're sure of (anything in series, any cable), use $I^2R$. If the voltage across it is what you're sure of (anything across the mains), use $V^2/R$.

**A number that makes the trap concrete.** Take a 2 m kettle flex of 1.5 mm² copper — that is 4.0 m of conductor, out and back. Its own resistance is $R = \rho L/A = (1.7\times10^{-8})(4.0)/(1.5\times10^{-6}) = 0.045\ \Omega$. At the kettle's 10 A, the p.d. **across the flex itself** is $V = IR = 0.45$ V — half a volt out of 220, which is exactly why nobody ever notices it. Now watch all three forms agree, because all three are being fed the *flex's own* numbers:

$$I^2R = (10)^2(0.045) = 4.5\ \text{W}, \qquad \frac{V^2}{R} = \frac{(0.45)^2}{0.045} = 4.5\ \text{W}, \qquad VI = (0.45)(10) = 4.5\ \text{W}$$

Four and a half watts, quietly warming your kitchen floor. Feed that last expression 220 V instead of 0.45 V and you get 2200 W — a perfectly correct answer to a completely different question, namely how much power the *kettle* takes. Same equation, different component. That is the entire trap, and the flex's own half-volt is what tells you which numbers belong to it.

That habit immediately settles a question students find genuinely confusing — *which resistor gets hottest?*

- **In series**, every component carries the same $I$, so $P = I^2R$ says the **largest** resistance dissipates the most. This is why a fuse works: it is deliberately the thinnest, highest-resistance link in the chain, so it is the first thing to melt.
- **In parallel**, every component has the same $V$ across it, so $P = V^2/R$ says the **smallest** resistance dissipates the most. Your 2 kW kettle has a *lower* resistance than your 10 W phone charger, not a higher one.

Same components, opposite answers, because the circuit decided which quantity they share.

**Where the joules land.** Straight back into the lattice. The collisions that cap the drift velocity are the collisions that hand the carriers' energy to the vibrating ions — as heat. Resistance and heating are not two effects of electricity; they are one process counted twice, once as an obstruction and once as a bill. That is why it is called **Joule heating**, and why every resistor in existence is quietly a small heater.

> [!info] The bill counts 度, not joules
> A joule is a small unit for a household, so electricity is sold in **kilowatt-hours**: one kilowatt sustained for one hour, $1\ \text{kW h} = 1000 \times 3600 = 3.6 \times 10^6\ \text{J}$. On a Chinese bill the same unit is written **度** — one 度 *is* one kilowatt-hour. So the meter on the wall is not counting electrons (they never leave your walls) and it is not counting coulombs either. It is counting $VIt$: the energy the field delivered, priced by the megajoule.

## Worked examples — every tool named

### Example 1 (0625 Core + Supplement) — the kettle, end to end

> A 2.2 kW electric kettle runs from a 220 V supply. Find (a) the current it draws, (b) its resistance while working, (c) the energy used in a 3.0 minute boil, and (d) the cost at ¥0.60 per 度.

*Tool: $P = VI$, rearranged for the unknown.*
$I = P/V = 2200/220 = 10\ \text{A}$.

*Tool: the definition of resistance, $R = V/I$.*
$R = 220/10 = 22\ \Omega$.

*Tool: energy is power × time — with time in seconds.*
$E = Pt = 2200 \times (3.0 \times 60) = 4.0 \times 10^5\ \text{J}$.

*Tool: convert to the billing unit — kilowatts × hours.*
$E = 2.2\ \text{kW} \times 0.050\ \text{h} = 0.11\ \text{kW h}$, so the cost is $0.11 \times 0.60 \approx$ **¥0.066** — about seven fen to boil a kettle.

One honest caveat: the 22 Ω is the element's resistance *when hot*. The element is a metal, so cold it is lower, and the kettle draws a brief surge above 10 A in its first second. Nothing here is wrong; $R = V/I$ simply returns the resistance at the operating point you measured, which is what it has always promised to do.

### Example 2 (9702) — resistivity, and an invariant hiding in the question

> A nichrome wire ($\rho = 1.1 \times 10^{-6}\ \Omega$ m) is 1.5 m long and 0.40 mm in diameter. (a) Calculate its resistance. (b) The wire is then drawn out to twice its original length without losing any metal. Calculate its new resistance.

*Tool: cross-sectional area from diameter — $A = \pi d^2/4$, not $\pi d^2$.*
$A = \pi (4.0\times10^{-4})^2 / 4 = 1.26 \times 10^{-7}\ \text{m}^2$.

*Tool: $R = \rho L / A$.*
$$R = \frac{(1.1\times10^{-6})(1.5)}{1.26\times10^{-7}} = 13\ \Omega$$

(b) *Tool: forward-read for the invariant — what does drawing a wire leave unchanged?* Not the length and not the area: the **volume**, since no metal is lost. So if $L$ doubles, $A$ must halve.

$$R_{\text{new}} = \frac{\rho(2L)}{A/2} = 4 \cdot \frac{\rho L}{A} = 4R = 53\ \Omega$$

Both geometric factors move, and both move the same way — the length term doubles it and the area term doubles it again. Answering "twice the length, so twice the resistance" is the single most common way to lose this mark, and it comes from reading the question backwards from the unknown instead of forwards from what is conserved.

### Example 3 (9702) — reading a non-ohmic characteristic

> From the filament-lamp characteristic: at 1.0 V the current is 0.16 A; at 6.0 V it is 0.30 A. (a) Find the resistance at each point. (b) A student says the resistance is the gradient of the graph. Correct them. (c) Explain the change in resistance.

*Tool: $R = V/I$ at each operating point — the chord from the origin.*
At 1.0 V: $R = 1.0/0.16 = 6.3\ \Omega$. At 6.0 V: $R = 6.0/0.30 = 20\ \Omega$. The resistance has more than **tripled**.

(b) Two things are wrong with "the gradient is the resistance". On an $I$–$V$ graph the gradient is $1/R$, not $R$ — inverted. And on a *curve* neither the gradient nor its reciprocal is the resistance at all: the tangent gives the dynamic resistance $\mathrm{d}V/\mathrm{d}I$, which is a different quantity. The resistance at a point on any characteristic is the chord: divide the two coordinates.

(c) Raising the p.d. raises the current, so the power $I^2R$ dissipated in the filament rises and its temperature climbs towards 2500 °C. The hotter lattice vibrates more violently, so conduction electrons are scattered after shorter free flights; the drift velocity per unit field falls, and the resistance rises. Note that nothing about Ohm's law has been violated — the lamp is simply not a component that Ohm's law was ever about, because its physical conditions did not stay constant.

## Common Misconceptions (Teaching Notes)

### 1. "Ohm's law is $V = IR$"

The most widespread error in the topic, repeated by textbooks. $V = IR$ is the *definition* of resistance and is true of everything — filament lamps, diodes, thermistors, your own body. Ohm's law is the separate, empirical claim that $R$ stays constant as $V$ changes, and it is only true for a restricted class of conductors under restricted conditions. **Fix:** ask "could an experiment ever show this to be false?" If no, it's a definition. If yes, it's a law — and this one fails on three of the four panels.

### 2. "Resistance is a property of the material"

Resistance belongs to the **object**: change its length or thickness and $R$ changes while the substance is untouched. The material property is **resistivity** $\rho$, which is what remains after the geometry is divided out, and it is the same for every copper wire in the world at a given temperature. **Fix:** two wires, same spool, different lengths — same $\rho$, different $R$. If a quantity changes when you cut something in half, it wasn't a property of the stuff.

### 3. "The resistance is the gradient of the $I$–$V$ graph"

Inverted and, on a curve, wrong twice. The gradient of an $I$–$V$ line is $1/R$; and on a curved characteristic the resistance at a point is the chord from the origin, $V/I$, not the tangent. **Fix:** never read $R$ off a slope. Read the two coordinates and divide — a habit that survives every graph orientation an exam can throw at you (some boards plot $V$ against $I$, which flips what the gradient means all over again).

### 4. "Heating always increases resistance"

True of metals, false of semiconductors, and the exception is not a curiosity — thermistors, LDRs and every temperature sensor in a greenhouse depend on it. $I = nAvq$ explains both at once: heat shortens the free flights in *any* material (hurting $v$), but in a semiconductor it also liberates new carriers, and the exponential rise in $n$ overwhelms the loss in $v$. **Fix:** ask which factor of $nAvq$ the heat gets hold of. In a metal, only $v$. In a semiconductor, $n$ — and $n$ wins.

### 5. "The biggest resistor always gets the hottest"

Only in series. In series the shared quantity is current, so $P = I^2R$ makes the largest $R$ the hottest — the principle behind a fuse. In parallel the shared quantity is p.d., so $P = V^2/R$ makes the **smallest** $R$ the hottest, which is why a 2 kW kettle has a lower resistance than a 10 W charger. **Fix:** decide first what the components *share*, then pick the form of $P$ built from that shared quantity.

## Exam Notes

### Cambridge 9702 — §9.2 and §9.3 (AS)

- **§9.2** is three LOs: *define* p.d. as energy transferred per unit charge; *recall and use* $V = W/Q$; *recall and use* $P = VI$, $P = I^2R$ and $P = V^2/R$. The definition is worth marks in words — "energy transferred per unit charge" — and the trio is examined by making you choose the right member for the quantities you were given.
- **§9.3** is eight LOs: *define* resistance; *recall and use* $V = IR$; *sketch* the $I$–$V$ characteristics of a metallic conductor at constant temperature, a semiconductor diode and a filament lamp; *explain* the filament lamp's rise in resistance via its temperature; *state* Ohm's law; *recall and use* $R = \rho L/A$; and understand that an LDR's resistance falls as light intensity rises and a thermistor's falls as temperature rises (NTC is assumed throughout).
- **Formula-sheet status, and it is a strange one.** The Paper 1/2 formulas page gives you the *combination* rules — $R = R_1 + R_2 + \cdots$ in series and $1/R = 1/R_1 + 1/R_2 + \cdots$ in parallel — and gives you *nothing* about a single resistor. $V = IR$, $R = \rho L/A$, $V = W/Q$ and all three power forms carry the verb **recall**: they are yours to memorise. The sheet hands you what to do with several resistors and assumes you already know what one of them is.
- Favourite question shapes: sketch-and-explain the three characteristics (the explanation is where the marks concentrate, and it must be a causal chain, not a description of the curve); the constant-volume stretch of Example 2; power comparisons in series versus parallel; and reading $R = V/I$ off two points of a curve rather than off its gradient.
- §10 builds directly on all of this: e.m.f. and terminal p.d. with [[Internal Resistance]], series and parallel combination with [[Kirchhoff's Laws]], and thermistor- or LDR-controlled [[Potential Dividers]].

### Cambridge 0625 IGCSE — §4.2.3 to §4.2.5

- **§4.2.3 Core:** define e.m.f. as the electrical work done by a source in moving unit charge round a complete circuit, and p.d. as the work done by unit charge passing through a component; both are measured in **volts**; describe the use of analogue and digital **voltmeters** with different ranges. **Supplement:** recall and use $E = W/Q$ and $V = W/Q$. Both definitions must name *unit charge* — that is where the mark is.
- **§4.2.4 Core:** recall and use $R = V/I$; **describe an experiment to determine resistance** using a voltmeter and an ammeter with the appropriate calculations (the bench method above — component in series with an ammeter, voltmeter across it, sweep the supply, and either average $V/I$ or take the gradient of the graph); state *qualitatively* how the resistance of a metallic wire depends on its length and cross-sectional area. **Supplement:** sketch **and explain** the $I$–$V$ graphs for a resistor of constant resistance, a filament lamp and a diode; and use the two proportionalities — resistance directly proportional to length, inversely proportional to cross-sectional area. Note that IGCSE stops at the proportionalities: the constant $\rho$ and the equation $R = \rho L/A$ are A-Level, but the reasoning behind them is identical and is worth having early.
- **§4.2.5 Core:** understand that circuits transfer energy from a source to the components and then to the surroundings; recall and use $P = IV$ and $E = IVt$; define the **kilowatt-hour** and calculate the cost of running appliances in kW h (Example 1 is exam-shaped).
- The rest of §4.2 — the electrostatics experiments and the field patterns of §4.2.1 — sits with [[Electric Field]]. Circuits proper (§4.3) follow with series and parallel rules, [[Potential Dividers]] and the action of circuit components.

### AP Physics 2 / AP Physics C: E&M

- **AP-2** §11.3–11.4 are exactly this material: $R = \rho L/A$, $V = IR$, and $P = IV = I^2R = V^2/R$, plus the ohmic/non-ohmic distinction. The CED leans hard on qualitative reasoning — "the wire is replaced by one of twice the diameter and the same length; describe the effect on the current" — which is Example 2 in words.
- **AP-C E&M** dresses the same physics in field language: resistivity is defined through **Ohm's law at a point**, $\mathbf{J} = \sigma \mathbf{E}$ with $\sigma = 1/\rho$, and $R = \rho L/A$ is derived from it for a uniform wire rather than assumed. The Beyond callout below is that derivation.

### IB Physics

- Theme B.5.1 and B.5.3 cover e.m.f. and p.d., ideal versus real meters, $R = V/I$, Ohm's law, the ohmic/non-ohmic characteristics and $\rho = RA/L$. B.5.4's potential dividers, combination rules and internal resistance follow from here.

## Beyond the syllabus

> [!info] Resistivity from the collision clock — where $\rho$ comes from
> Recall that between collisions each carrier is accelerated by the field with $a = qE/m$, and that a collision throws away whatever drift it had gained. If the average time between collisions — the **relaxation time** $\tau$ — is the same for all of them, the average drift works out to $v_d = qE\tau/m$: exactly the dashed mean line on the sawtooth figure. Feed that into the current density $\mathbf{J} = nq\mathbf{v}_d$ from [[Electric Current]] and the field drops out into a constant of proportionality:
> $$\mathbf{J} = \frac{nq^2\tau}{m}\,\mathbf{E} \equiv \sigma\mathbf{E}, \qquad \rho = \frac{1}{\sigma} = \frac{m}{nq^2\tau}$$
> This is **Ohm's law at a point** — the local, material-level statement, of which $V = IR$ for a uniform wire is the integrated special case. And every symbol in $\rho = m/nq^2\tau$ is now legible. More carriers, lower $\rho$. Longer free flights, lower $\rho$. Heat a metal: $n$ is fixed and $\tau$ falls, so $\rho$ rises. Heat a semiconductor: $\tau$ falls too, but $n$ climbs exponentially and wins outright, so $\rho$ falls. The two curves of the fourth panel come out of one formula, differing only in which factor the temperature can reach. This is Paul Drude's 1900 model, and it is wrong in its details — it treats electrons as a classical gas — yet it gets the structure of $\rho$ exactly right, which is why it survived the quantum revolution as the picture everyone still thinks in.

> [!info] Why does a wire resist at all? (The pinball picture is a lie that works)
> Push the collision story hard enough and it breaks. If electrons really bounced off the lattice ions like pinballs off pegs, a metal's resistivity would be enormous and would depend on temperature quite differently from how it does. The quantum answer is stranger and much more satisfying: an electron in a **perfectly periodic** lattice is a wave, and a wave in a perfectly periodic medium propagates without scattering *at all*. A flawless crystal at absolute zero would have **zero** resistance — which is the third beat of the animation earlier, where the frozen, perfectly periodic lattice lets the electron accelerate away without a single scattering event and there is no terminal drift for a resistance to be the ratio of. Every ohm you have ever measured comes from *departures* from perfection — thermal vibration of the ions (which is why $R$ rises with temperature in a metal), impurity atoms, and crystal defects. Their contributions simply add, which is **Matthiessen's rule**, $\rho = \rho_{\text{thermal}}(T) + \rho_{\text{residual}}$. Cool a pure metal towards 0 K and its resistivity does not go to zero; it flattens onto the residual value, which measures nothing but how dirty the sample is — metallurgists use exactly this as a purity assay. The ions do not obstruct the electrons. Only the ions' *imperfections* do.

> [!info] And then there is zero
> In 1911 Heike Kamerlingh Onnes, having just learned to liquefy helium, cooled a thread of mercury towards 4 K expecting it to flatten onto its residual resistivity. Instead, at 4.2 K, the resistance did not flatten — it *disappeared*, abruptly and completely. Not small: zero. A current started in a closed superconducting loop circulates for years with no measurable decay, which is a far stronger statement than any measurement of "very low resistance" could ever be. This is not a very good conductor; it is a different state of matter, in which electrons pair up and move as a single quantum entity that has no way to shed energy in small amounts. It is what lets an MRI scanner hold a several-tesla field with its power supply switched off, the current simply going round and round.
>
> **Is that a true zero, or only a resistance too small to measure?** Both halves of the answer are worth having, and they point the same way. *Experimentally*, a current set circulating in a superconducting ring has been watched for years without any detectable decay: the best measurements put the decay time constant above $10^{5}$ years and bound the resistivity below roughly $10^{-25}\ \Omega$ m — some seventeen orders of magnitude under copper, which is about as close to zero as any physical quantity has ever been pinned by an experiment. But an experiment can only ever hand you a bound. *Theoretically* the answer is stronger than "very small": the paired electrons occupy a single quantum state separated from every excited state by an energy gap, so for a steady current there is simply **no available way to shed energy in small amounts** — nothing to scatter into. The direct-current resistance is exactly zero, in the mathematical sense, and not by approximation. (Alternating current is a different story: wiggle the pairs and loss returns, which is why superconducting radio-frequency cavities are hard to build and a superconducting d.c. magnet is not.) That state of matter is [[Superconductivity]] — and everything above describes the ordinary world it is the exception to.

## Connections

- **Builds on:** [[Electric Current]] — the parade priced here. Its drift velocity is the terminal velocity that collisions impose, its $I = nAvq$ explains why metals and semiconductors respond to heat in opposite directions, and its "what gets used up is energy" is settled here as $V = W/Q$.
- **Leads to:** [[Kirchhoff's Laws]] — charge conservation at junctions and energy conservation round loops, giving the series and parallel combination rules; [[Internal Resistance]] — the e.m.f. a cell supplies versus the terminal p.d. it delivers; [[Potential Dividers]] — resistance ratios turned into a controllable output voltage, the standard way a thermistor or LDR is actually read.
- **Application:** [[Sensors and Control Systems]] — the computing side of the same thermistor and LDR: a resistance that answers to the world is the first link in every measurement chain; [[Electromagnetic Induction]] — the $I^2R$ transmission-loss argument that decided how the grid is built, and the same-component discipline worked through on a real cable.
- **Kindred:** [[Capacitors]] — pair a resistance with a capacitance and the exponential $\tau = RC$ appears; [[Kinetic Theory and the Ideal Gas]] — the lattice vibration that scatters the carriers is thermal motion in a solid, the same energy the gas card counts in a gas; [[Diodes]] — what the junction does to earn the one-way characteristic, and where dynamic resistance becomes the working number; [[Stories/The Blue LED]] — that same asymmetry turned into light; [[Electric Field]] — the field that drives the drift in the first place; [[Superconductivity]] — resistance not merely small but exactly zero.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $V = \dfrac{W}{Q}$ | `V = \dfrac{W}{Q}` | p.d. — energy transferred per unit charge |
| $E = \dfrac{W}{Q}$ | `E = \dfrac{W}{Q}` | e.m.f. — energy supplied per unit charge |
| $R = \dfrac{V}{I}$ | `R = \dfrac{V}{I}` | the definition of resistance |
| $\Omega$ | `\Omega` | ohm — one volt per ampere |
| $R = \dfrac{\rho L}{A}$ | `R = \dfrac{\rho L}{A}` | resistance split into material × geometry |
| $\rho$ | `\rho` | resistivity, in Ω m |
| $\sigma = 1/\rho$ | `\sigma = 1/\rho` | conductivity (beyond syllabus) |
| $P = VI = I^2R = \dfrac{V^2}{R}$ | `P = VI = I^2R = \dfrac{V^2}{R}` | one equation in three costumes |
| $E = VIt$ | `E = VIt` | electrical energy delivered |
| $\mathbf{J} = \sigma\mathbf{E}$ | `\mathbf{J} = \sigma\mathbf{E}` | Ohm's law at a point (beyond syllabus) |
| $\tau$ | `\tau` | relaxation time — mean time between collisions |
| $\mathrm{d}V/\mathrm{d}I$ | `\mathrm{d}V/\mathrm{d}I` | dynamic resistance — the tangent, not the chord |
