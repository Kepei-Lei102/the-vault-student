---
chinese: 电流 (diànliú)
prerequisites:
  - "[[Physical Quantities and Units]]"
  - "[[Stories/Franklin's Coin Flip]]"
  - "[[Franklin's Coin Flip]]"
leads_to:
  - "[[Resistance]]"
  - "[[Capacitors]]"
  - "[[Lorentz Force]]"
tags:
  - subject/physics
  - domain/electromagnetism
  - level/IGCSE
  - level/A-Level
  - level/AP
  - syllabus/9702-9-1
  - syllabus/0625-4-2
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - curriculum/IB-Physics
  - type/deep
  - misconception/electrons-at-light-speed
  - misconception/current-used-up
  - misconception/conventional-current-is-wrong
  - misconception/power-station-sends-electrons
  - misconception/ion-streams-cancel
---

# Electric Current 电流

> *Flip the switch and the lamp answers instantly. Now the shock: inside that cord, the electrons are crawling at about a tenth of a millimetre per second — slower than the tip of your wall clock's minute hand. An electron setting out from the switch would need over four hours to reach the bulb. Something in that wire does move at nearly the speed of light, but it is not the electrons — and by the end of this card, "the current is 2 amperes" will unpack into a full picture: how many carriers, carrying how much charge each, marching how fast, through what gate. The picture is one formula, $I = nAvq$, and it is the microscopic engine underneath everything electrical that follows.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| electric charge | 电荷 | the conserved, quantised property that feels electric force |
| coulomb (C) | 库仑 | the SI unit of charge — one ampere-second |
| elementary charge $e$ | 基本电荷 | the quantum of charge, $1.60 \times 10^{-19}$ C |
| electric current | 电流 | the rate at which charge flows past a point |
| ampere (A) | 安培 | one coulomb per second — an SI **base** unit |
| charge carrier | 载流子 | whatever mobile thing carries the charge: electron, ion, hole |
| free electron | 自由电子 | a metal's delocalised outer electron — the carrier sea |
| number density $n$ | 数密度 | carriers per cubic metre of material |
| drift velocity $v$ | 漂移速度 | the carriers' tiny average march speed |
| conventional current | 常规电流方向 | the direction positive charge moves (or would move) |
| electron flow | 电子流 | the electrons' actual direction — opposite the arrow |
| direct / alternating current | 直流 / 交流 | one fixed direction vs direction reversing periodically |

## The bottom of the tower — charge

Everything electrical is defined in terms of something else. Magnetic flux density is force per unit current ([[Lorentz Force]]); potential difference is energy per unit charge; resistance is voltage over current. Chase the definitions down and it can feel circular — until you hit the floor. The floor is **charge**: the one electrical quantity that is not defined through the others but simply *possessed* by matter, the way mass is. Every other quantity in the tower is built from it. Three properties do all the work:

- **Charge comes in two signs.** Like signs repel, unlike attract. The names *positive* and *negative* are inherited labels — [[Stories/Franklin's Coin Flip]] tells how they were assigned, by a fair guess, 150 years before anyone could check it.

> [!question] The hunter's two follow-ups — ask them now, they're excellent
> That one sentence should bother you twice. **If unlike signs attract, why don't the electrons crash into the nucleus?** By 19th-century physics they *must* — an orbiting (accelerating) charge radiates energy away, and the calculated death spiral takes about 16 picoseconds; every atom in the universe should have collapsed at once. It doesn't, because the electron is not a tiny planet but a wave, and a wave wrapped around a nucleus has a **lowest rung it cannot fall below** — [[Wave–Particle Duality]] is that story, and this paradox is precisely what forced quantum mechanics into existence. **And if like signs repel, how does a nucleus hold dozens of protons a femtometre apart?** It can't — not with these two forces. There is a third one: the **strong force**, which ignores charge, outmuscles the electric repulsion at nuclear range, and vanishes beyond it — [[Particle Physics]] carries it. Both questions are the right instinct: a rule this simple should be interrogated until it cracks, and each crack opens a new floor of physics.
- **Charge is conserved.** The total charge of an isolated system never changes — not in chemistry, not in nuclear decay, not anywhere yet observed. When charge seems to appear (rubbing a balloon), it has only *moved*: friction transfers electrons from one surface to the other; nothing is created. This is the deepest conservation law in the card, and it is the reason current entering a junction must equal current leaving ([[Kirchhoff's Laws]]).
- **Charge is quantised.** It comes in whole-number multiples of the **elementary charge** $e = 1.60 \times 10^{-19}\ \text{C}$ — the charge of a proton, and (with a minus sign) of an electron. Millikan's oil-drop experiment measured it in 1909 by balancing charged droplets against gravity and finding their charges always stepped by the same amount. No free particle with a fraction of $e$ has ever been caught. (Quarks carry $\pm\tfrac{1}{3}e$ and $\pm\tfrac{2}{3}e$, but they are permanently confined inside protons and neutrons — the fractions never walk alone.) And yes — *quantised* is the same word as in **quantum physics**: Latin *quantus*, "how much", turned into a noun for the smallest indivisible lump. The name of the whole field honours Planck's 1900 discovery that **energy**, too, is exchanged in lumps ([[Photoelectric Effect]] is where that lump becomes undeniable) — charge got there first, but energy got the naming rights.

> [!info] A coulomb is literally a count
> Since the 2019 redefinition of the SI, the elementary charge is *fixed by definition*: $e = 1.602\,176\,634 \times 10^{-19}$ C **exactly**. Run that backwards and one coulomb is exactly $6.241\,509\ldots \times 10^{18}$ elementary charges — about six and a quarter billion billion electrons. The unit of charge is no longer measured against a standard; it *is* a tally of particles. ([[Physical Quantities and Units]] carries the full 2019 story: the ampere is the SI base unit, and the coulomb is one ampere-second.)

**Who gets to move.** In a metal, roughly one outer electron per atom abandons its home atom and joins a shared, delocalised sea — these **free electrons** are why metals conduct. In an insulator every electron is held tightly to its own atom: nothing is free to march, so almost no current flows however hard you push. (Semiconductors sit between — a sparse population of freed carriers, roughly a million times thinner than a metal's, and that thinness will matter later in this card.)

## Current — the rate at the gate

Stand at one cross-section of a wire — a tollgate — and count the charge going past. **Electric current is the rate of flow of charge**:

$$I = \frac{\Delta Q}{\Delta t} \qquad\Longleftrightarrow\qquad Q = It$$

One **ampere** is one coulomb per second through the gate. Orders of magnitude to calibrate your intuition: an LED runs on a few *milli*amps, a laptop charger a couple of amps, a kettle around ten, a lightning stroke around thirty *thousand* — for a millisecond.

Current has a *direction* (which way along the wire) but it is **not a vector** — currents at a junction add by plain arithmetic of in-and-out, not by components. The arrow on a circuit diagram is bookkeeping, not geometry.

**d.c. and a.c.** A battery drives **direct current** — one fixed direction. The mains drives **alternating current** — the direction reverses periodically, 50 times a second in China and the UK (50 Hz, 220 V in China). Everything in this card applies to both; a.c. simply means the parade about-faces a hundred times a second, and this card's final section makes that surprisingly vivid.

**Measuring it.** An ammeter counts the parade, so it must stand *in* the parade: always connected **in series**, and built with as little resistance as possible so that joining the line doesn't slow the line. Analogue meters (a needle over a scale) come with switchable ranges — pick the smallest range that fits the expected current, so the needle swings wide and reads precisely; digital meters do the ranging for you.

## Who carries it — and which way the arrow points

A current is not a substance; it is a *headcount*. Anything charged and mobile can carry it:

| where | carriers | note |
|---|---|---|
| metal wire | free electrons | the everyday case |
| electrolyte (salt solution, battery acid) | positive **and** negative ions | both signs at once, moving opposite ways |
| ionised gas (lightning, the door-handle zap, a neon sign) | electrons and positive ions | gas becomes a conductor once torn apart |
| semiconductor | electrons and holes | sparse but engineerable — [[Stories/The Blue LED]] |

That third row deserves its picture, because the classic example has quietly gone extinct. A **neon sign** is not an LED strip bent into letters: it is a glass tube of thin neon gas with a high voltage across its ends — high enough to tear electrons off the atoms — and the current through the tube is carried by the torn-apart gas itself, electrons one way, positive ions the other. The glow *is* the traffic: ions recapturing electrons and paying the reunion out as light. Today's "neon" shopfronts are almost all LED imitations — the gas parade retired, but lightning and every spark you've ever been zapped by still run on it.

![[electric-current-neon-comic.png|700]]

The electrolyte row hides a classic trap: the two ion streams move in *opposite directions* — do they cancel? No — they **add**. A positive ion moving right and a negative ion moving left both shift positive charge rightwards; both count the same way at the gate. Watch the signs, not the traffic.

**Conventional current** is defined as the direction *positive* charge moves, or would move — from the + terminal through the circuit to the −. In a metal the actual carriers are electrons, so the **electron flow is opposite the current arrow**. This is not an error to fix but a convention to keep: a negative charge moving left *is* a positive current to the right — the two descriptions are algebraically identical, and every formula in physics ($F = BIL$, $V = W/Q$, Kirchhoff's laws) works consistently in the conventional direction. The arrow points the "wrong" way for one purely historical reason: Franklin had to guess which kind of charge was the mobile one a century and a half before Thomson found the electron, and the coin landed on the other side — [[Stories/Franklin's Coin Flip]] is that story, lightning rod, Leyden jars and all.

## The parade formula — $I = nAvq$, derived

Now open the wire and *count*. The current picture: a wire of cross-sectional area $A$, filled with carriers of charge $q$ at **number density** $n$ (carriers per cubic metre), all drifting along at average speed $v$. How much charge passes the gate per second?

![[electric-current-navq-corridor.svg|700]]

*Tool: count who reaches the gate in time $\Delta t$.* A carrier crosses the gate within the next $\Delta t$ exactly when it is currently within a distance $v\,\Delta t$ upstream of it. Those carriers fill a cylinder of volume $A \times v\,\Delta t$, so there are

$$N = n \cdot A\,v\,\Delta t$$

of them, together carrying charge $\Delta Q = nAv\,\Delta t \cdot q$. Divide by $\Delta t$:

$$\boxed{\,I = nAvq\,}$$

(The 9702 formula sheet prints it as $I = Anvq$ — same four factors, alphabetical accident.) Each factor is a knob, and the formula is just proportionality four times over: double the carrier density, the pipe's area, the march speed, or the charge per marcher, and you double the current. The units agree: $\text{m}^{-3} \cdot \text{m}^2 \cdot \text{m s}^{-1} \cdot \text{C} = \text{C s}^{-1} = \text{A}$. ✓

This formula is the bridge between the circuit world and the particle world — and it has already been *spent* once in this vault: [[Lorentz Force]] sums the magnetic force on each of the $nAL$ carriers in a wire and needs $I = nAvq$ to collapse the sum into $F = BIL$. This card is where that borrowed step is honestly earned.

## The shock — how slowly the parade marches

Put numbers in. Copper has $n = 8.5 \times 10^{28}$ free electrons per cubic metre (about one per atom). Take a lamp cord of cross-section $A = 1.0\ \text{mm}^2 = 1.0 \times 10^{-6}\ \text{m}^2$ carrying $I = 1.0$ A:

$$v = \frac{I}{nAq} = \frac{1.0}{(8.5 \times 10^{28})(1.0 \times 10^{-6})(1.60 \times 10^{-19})} \approx 7.4 \times 10^{-5}\ \text{m s}^{-1}$$

**Seven hundredths of a millimetre per second.** The tip of a wall clock's minute hand moves about three times faster. An electron entering a 1.2 m lamp cord takes $1.2 / (7.4\times10^{-5}) \approx 16{,}000$ s — **four and a half hours** — to reach the other end. Yet the lamp lights the instant you flip the switch. Where does the speed ladder actually put everyone?

![[electric-current-speed-ladder.svg|700]]

Three speeds live in the same wire, five orders of magnitude apart each:

1. **Thermal speed, ~$10^6$ m/s.** The free electrons are never still — they rattle among the ions at around a thousand kilometres per second, in *random* directions that cancel to nothing. This is the same picture as [[Kinetic Theory and the Ideal Gas]]: gas molecules scream around at hundreds of m/s, yet the *wind* — their average drift — can be a gentle stroll.
2. **Drift speed, ~$10^{-4}$ m/s.** Switch the field on and the whole rattling crowd acquires a tiny *bias* — the drift. Current is carried by this whisper of net motion on top of the thermal roar.
3. **Signal speed, ~$10^8$ m/s.** The electric field that issues the marching orders spreads along the cable at an appreciable fraction of the speed of light.

And that resolves the shock. **The wire is a pipe already full.** The circuit is packed with free electrons end to end before you touch the switch; closing it sends the *field* sweeping around the loop at near light-speed, and every electron everywhere — in the switch, in the cord, in the filament — starts drifting *at essentially the same moment*. The lamp lights when the news arrives, not when the messengers do. Push a full hose and water leaves the far end at once; push a bicycle chain's bottom link and the top link moves now, not when your link gets there.

![[electric-current-drift.mp4]]

> [!info] The a.c. twist — the electrons never leave your lamp cord
> Mains current reverses 50 times a second, so the carriers never even complete their crawl — they *shuffle in place*. At a drift speed of $7.4\times10^{-5}$ m/s reversing at 50 Hz, each electron sways back and forth by about $v/(2\pi f) \approx 0.2\ \mu\text{m}$ — a quarter of a *micrometre*, a fiftieth of a hair's width. The electrons lighting your room tonight have been in your walls for years and are going nowhere — the same quarter-micrometre clip, replayed fifty times a second, forever: your house wiring is running a 鬼畜 loop. What the power station sells you is not electrons but the *push* — energy, delivered by the field. That is also why the a.c.-vs-d.c. choice ([[Stories/The War of the Currents]]) was never about which way electrons travel: they barely travel at all.

## Worked examples — every tool named

### Example 1 (0625 Supplement / 9702) — charge is a total, current is a rate

> A phone fast-charges at a steady 2.0 A for 90 minutes. How much charge passes into the battery, and how many electrons carry it?

*Tool: $Q = It$ — with time in seconds.*
$Q = It = 2.0 \times (90 \times 60) = 1.1 \times 10^4\ \text{C}$ (10 800 C).
*Tool: quantisation — divide by the charge per carrier.*
$N = Q/e = 10\,800 / (1.60 \times 10^{-19}) \approx 6.8 \times 10^{22}$ electrons — about seventy thousand billion billion, and the battery's mass changes by less than a nanogram of electron mass. Charge is easy to move in astonishing counts.

### Example 2 (9702, the banker) — use $I = Anvq$

> A copper wire of cross-sectional area $2.0\ \text{mm}^2$ carries a current of $3.2$ A. Copper has $8.5 \times 10^{28}$ free electrons per m³. Calculate the drift velocity of the electrons.

*Tool: the parade formula, rearranged for the one unknown.*
$$v = \frac{I}{nAq} = \frac{3.2}{(8.5\times10^{28})(2.0\times10^{-6})(1.60\times10^{-19})} = 1.2 \times 10^{-4}\ \text{m s}^{-1}$$
About a tenth of a millimetre per second. *Sanity check the exponents first* — $10^{28} \times 10^{-6} \times 10^{-19} = 10^{3}$ — this question is lost to powers of ten far more often than to physics. (And the marks are in the **use**: the formula itself is printed on the 9702 sheet.)

### Example 3 (9702 reasoning) — read it as an invariant

> (a) The wire in Example 2 narrows to half its cross-sectional area. What happens to the drift velocity in the narrow section? (b) A semiconductor sample carries the same current with the same area, but its carrier density is a million times smaller. Compare the drift velocities.

*Tool: forward-read $I = nAvq$ — ask what does not change.* The narrow section carries the **same current** (charge cannot pile up or vanish mid-wire — conservation again), and $n$ and $q$ are fixed by the material.
(a) Same $I$, half the $A$ → $v$ **doubles**. The corridor narrows, so the parade must quick-march — exactly a river speeding up through a gorge.
(b) Same $I$ and $A$, $n$ a million times smaller → $v$ a **million times larger**. Semiconductor carriers genuinely sprint where copper's crawl — which is why Hall probes are made of semiconductor: [[Lorentz Force]]'s Hall voltage grows with $v$, so the sparse-carrier material gives the loud signal.

## Common Misconceptions (Teaching Notes)

### 1. "Electrons travel through the wires at the speed of light"

They crawl — fractions of a millimetre per second (Example 2). What moves at near light-speed is the **field**, which starts every carrier in the circuit drifting almost simultaneously. **Fix:** the pipe already full — the lamp lights when the *news* arrives, not the messengers. If electron speed set the pace, your lamp would take half a day to warm up.

### 2. "Current gets used up as it goes around the circuit"

The current entering any component equals the current leaving it; in a series loop the same $I$ flows everywhere. Charge is conserved and has nowhere else to go — what gets spent is *energy* (that story belongs to potential difference and [[Resistance]]). **Fix:** count the parade at two gates — nobody joins, nobody leaves, so the headcount per second must match.

### 3. "Conventional current points the wrong way, so the physics must be wrong somewhere"

The physics is sign-consistent: a negative charge moving left *is* a positive current to the right, and every law gives identical answers either way. The arrow is a historical convention, not a claim about the carriers. **Fix:** [[Stories/Franklin's Coin Flip]] — one fair guess, made 150 years too early to check, fossilised into every circuit diagram; annoying, but never incorrect.

### 4. "The power station sends electrons to my house"

On a.c. mains the carriers shuffle in place by a fraction of a micrometre — the electrons in your cord have never seen the power station. What travels is energy, carried by the field. **Fix:** you buy the push, not the particles — the electricity bill counts joules, not electrons.

### 5. "In an electrolyte the opposite ion flows cancel out"

Positive ions one way and negative ions the other are currents in the **same** direction — both shift positive charge the same way, so they add. **Fix:** track charge crossing the gate, not bodies crossing the gate; sign times direction is what counts.

## Exam Notes

### Cambridge 9702 — §9.1 (AS)

- Four LOs: current is a flow of **charge carriers**; charge is **quantised**; *recall and use* $Q = It$; *use* $I = Anvq$ with $n$ the **number density** of carriers. The verbs match the formula sheet exactly: $I = Anvq$ **is printed on the Papers 1/2/4 formulae page** (so the marks are in using it — rearranging, ratio reasoning as in Example 3, explaining drift changes), while $Q = It$ is **not on the sheet** — the basic one is yours to recall. The data page hands you $e = 1.60 \times 10^{-19}$ C.
- Favourite question shapes: compute drift velocity and be shocked (Example 2 — powers of ten are the real test); "the wire narrows / the material changes — what happens to $v$?" (Example 3); count electrons via $N = Q/e$; explain why a metal conducts and an insulator doesn't (free-electron model, one sentence each).
- §9.2 (potential difference, power) and §9.3 (resistance, resistivity) build directly on this card via $V = W/Q$ and $V = IR$ — [[Resistance]] territory.

### Cambridge 0625 IGCSE — §4.2.1–4.2.2

- **Core:** electric current is *related to the flow of charge*; conduction in metals described through **free electrons**; use of **ammeters** (analogue and digital, connected in series, choosing a sensible range); know the difference between **d.c. and a.c.** (direction fixed vs periodically reversing).
- **Supplement:** *define* current as charge per unit time and use $I = Q/t$; charge measured in **coulombs**; state that **conventional current runs + to −** while the free-electron flow runs − to + — a two-mark statement pair that must be given *both* halves.
- From §4.2.1, this card carries the charge basics: two signs, like repels unlike attracts, friction transfers **electrons only**, and the electron-model distinction between conductors and insulators. (The electrostatics experiments and field patterns of §4.2.1 belong with [[Electric Field]]; PD, resistance, and electrical power complete §4.2 via [[Resistance]].)

### AP Physics 2 / AP Physics C E&M

- **AP-2:** conventional current defined by positive-charge direction is stated explicitly in the CED ("current is not a vector, but it has a direction"); the microscopic carrier-drift picture is used qualitatively; charge conservation at junctions is a core reasoning skill.
- **AP-C E&M:** the same physics dressed as **current density** $\mathbf{J} = nq\mathbf{v}_d$ with $I = \int \mathbf{J} \cdot d\mathbf{A}$ — the Beyond callout below is the exact bridge.

### IB Physics

- Theme B.5 (current and circuits) works at the circuit level; this card is the microscopic depth behind its current and charge definitions.

## Beyond the syllabus

> [!info] Current density — the field-theoretic upgrade
> Recall that $I = nAvq$ counts the whole parade through one gate. Divide out the area and you get a *local*, directional quantity: the **current density** $\mathbf{J} = nq\mathbf{v}_d$ (units A m⁻²), with the total current through any surface $I = \int \mathbf{J}\cdot d\mathbf{A}$. This is the version physics keeps: $\mathbf{J}$ is a vector field defined at every point, it handles wires of varying width and currents spread through 3-D conductors, and it is the $I$ that [[Maxwell's Equations]]' Ampère–Maxwell law actually wants on its right-hand side. A-Level's formula is the uniform-wire special case: $J$ constant over the cross-section gives $I = JA = nAvq$.

> [!info] Where does $n = 8.5 \times 10^{28}$ come from?
> Not from a table of magic numbers — from chemistry you already own. Copper donates about **one free electron per atom**, so $n$ is just the number density of copper atoms: $n = \dfrac{\rho N_A}{M} = \dfrac{8960 \times 6.02\times10^{23}}{0.0635} \approx 8.5 \times 10^{28}\ \text{m}^{-3}$ — density over molar mass gives moles per cubic metre, times Avogadro gives atoms. Every constant in that line is on the 9702 data page. Semiconductors sit around $10^{16}$–$10^{22}$: it is *doping* — deliberately seeding carriers — that sets $n$, which is why their $n$ is engineerable and a metal's is not.

> [!info] Why is there a magnetic force at all?
> One more debt note: [[Lorentz Force]]'s Beyond section shows that magnetism itself is what the electric force of these *crawling* charges looks like after relativity corrects the bookkeeping — length contraction at a tenth of a millimetre per second is absurdly small, but so is the residual force, and it is exactly what we measure as magnetism. The slowest parade in physics powers the field that runs every motor. And yes, that is Einstein's relativity — specifically **[[Special Relativity]]**, the 1905 theory of fast things and moving viewpoints (length contraction, time dilation, $E = mc^2$), which is a different theory from **[[General Relativity]]**, the 1915 theory of gravity as curved spacetime. Magnetism needs only the special one.

## Connections

- **Builds on:** [[Physical Quantities and Units]] — the ampere is the SI base unit this card's coulomb hangs from, and the 2019 fixed-$e$ redefinition lives there; [[Stories/Franklin's Coin Flip]] — the human reason the arrow points against the electrons.
- **Leads to:** [[Resistance]] — what the wire charges for the passage: $V = IR$, Ohm's law, resistivity; [[Capacitors]] — a charging or discharging capacitor is this card's $I = \Delta Q/\Delta t$ read as calculus, $I = dQ/dt$; [[Lorentz Force]] — sums this card's parade, one $Bqv$ per carrier, into $F = BIL$: the debt this card was written to pay.
- **Kindred:** [[Kinetic Theory and the Ideal Gas]] — thermal roar vs drift whisper is exactly molecular speed vs wind speed; [[Maxwell's Equations]] — current is the source term that makes magnetic fields; [[Stories/The War of the Currents]] — the a.c./d.c. war, fought over transmission, not over which way electrons go; [[Stories/The Blue LED]] — carrier engineering as a Nobel-winning craft.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $I = \dfrac{\Delta Q}{\Delta t}$ | `I = \dfrac{\Delta Q}{\Delta t}` | current as rate of charge flow |
| $Q = It$ | `Q = It` | recall form — not on the 9702 sheet |
| $I = nAvq$ | `I = nAvq` | the parade formula (sheet prints $Anvq$) |
| $e$ | `e` | elementary charge, $1.60\times10^{-19}$ C |
| $n$ | `n` | number density of carriers, m⁻³ |
| $\mathbf{J} = nq\mathbf{v}_d$ | `\mathbf{J} = nq\mathbf{v}_d` | current density (beyond syllabus) |
| $\mu$m | `\mu\text{m}` | micrometre — the a.c. shuffle scale |
