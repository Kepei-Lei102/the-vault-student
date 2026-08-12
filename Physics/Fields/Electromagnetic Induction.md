---
chinese: 电磁感应 (diàncí gǎnyìng)
prerequisites:
  - "[[Lorentz Force]]"
leads_to:
  - "[[Maxwell's Equations]]"
  - "[[Alternating Current]]"
  - "[[Stories/The Bookbinder's Apprentice]]"
  - "[[The Bookbinder's Apprentice]]"
tags:
  - subject/physics
  - domain/electromagnetism
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/A-Level
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - syllabus/9702-20-5
  - syllabus/9702-21-1
  - syllabus/0625-4-5
  - type/deep
  - misconception/flux-itself-induces
  - misconception/emf-peaks-when-flux-peaks
  - misconception/transformer-works-on-dc
  - misconception/emf-always-drives-current
---

# Electromagnetic Induction 电磁感应

> *Nearly every joule of electricity you have ever used — this screen, the lamp above you, the kettle downstairs — was made in exactly one way: **by moving a magnet near a coil of wire.** Coal plants, gas plants, nuclear plants, dams, wind turbines: they differ only in what does the pushing. The thing being pushed is always the same — a coil turning in a magnetic field — and the physics that turns that motion into current was found in 1831 by a bookbinder's apprentice who kept asking one stubborn question. Oersted had shown that electricity makes magnetism. Faraday spent a decade hunting the converse — and the answer turned out to carry a twist: magnetism does make electricity, **but only while it is changing**. Nature does not sell steady-state electricity. You must keep moving, and you must pay for every coulomb — and the law that presents the bill is the reason your lights are on.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| electromagnetic induction | 电磁感应 | a changing magnetic flux inducing an e.m.f. in a conductor |
| magnetic flux $\Phi$ | 磁通量 | field threading a loop: $\Phi = BA$ (area ⊥ to $B$), unit **weber** (Wb) |
| magnetic flux density $B$ | 磁通密度 | flux per unit area — the "strength of threading", in tesla ($1\,\text{T} = 1\,\text{Wb m}^{-2}$) |
| flux linkage $N\Phi$ | 磁链 | total flux threaded through all $N$ turns of a coil |
| induced e.m.f. | 感应电动势 | the voltage created by changing flux — exists even with no current flowing |
| Faraday's law | 法拉第电磁感应定律 | e.m.f. = rate of change of flux linkage |
| Lenz's law | 楞次定律 | the induced effect opposes the change that causes it |
| eddy currents | 涡流 | induced current swirling inside a solid conductor |
| a.c. generator | 交流发电机 | a coil spun in a field — the motor run backwards |
| slip rings | 滑环 | the generator's continuous contacts (the commutator's honest siblings) |
| transformer | 变压器 | two coils sharing changing flux through an iron core — a.c. voltage exchanged for current |
| primary / secondary | 原线圈 / 副线圈 | the driven coil / the coil the changed voltage comes out of |

## The symmetric question

[[Lorentz Force]] told the first half of the story: a **current makes a magnetic field** (Oersted, 1820), and a field pushes on a current — which gave us the motor. The symmetric question practically asks itself: *if electricity makes magnetism, can magnetism make electricity?* Faraday chased that question for a decade, wrapping coils on iron rings, staring at a galvanometer needle that refused to move while his strongest magnets sat obediently beside his circuits.

The needle finally moved in 1831 — and it moved **only at the moments something changed**: at the instant he connected or broke the primary circuit, at the instant a magnet entered or left a coil. Steady magnetism next to a wire, forever, does nothing. That is the twist that hides in every question on this topic: **flux induces nothing; *changing* flux induces everything.**

## Flux — counting the threads through a window

Before the law, its currency. Picture a loop of wire as a **window**, and the magnetic field as threads passing through it. **Magnetic flux** measures the total threading:

$$\boxed{\Phi = BA} \qquad \text{(} A \text{ the area perpendicular to } B\text{)} \qquad [\Phi] = \text{weber, } 1\,\text{Wb} = 1\,\text{T m}^2$$

Tilt the window and fewer threads pass through: in general $\Phi = BA\cos\theta$, with $\theta$ the angle between $B$ and the **normal** to the loop — face-on catches everything, edge-on catches nothing. And a coil of $N$ turns is $N$ windows stacked in series, each threaded by the same flux, so the quantity the law actually cares about is the **flux linkage** $N\Phi$.

![[emi-flux-window.svg|697]]

This definition is 9702's first two marks verbatim: *flux is the product of magnetic flux density and the cross-sectional area perpendicular to the field* — say "perpendicular" or say nothing.

## Faraday's law — the rate is the voltage

$$\boxed{\text{induced e.m.f.} = \frac{\Delta (N\Phi)}{\Delta t}} \qquad \text{(magnitude; the direction is Lenz's department)}$$

**The induced e.m.f. equals the rate of change of flux linkage.** Not the flux — its *rate of change*. All three classic bench demonstrations are this one sentence wearing different costumes, and the syllabus asks you to explain each:

![[emi-faraday-demos.svg|697]]

- **Magnet into coil:** the galvanometer kicks *while the magnet moves*, reads zero while it rests inside — flux high but unchanging. Push **faster** → bigger kick (same $\Delta\Phi$, smaller $\Delta t$); **more turns** → bigger kick (the $N$ in $N\Phi$); **stronger magnet** → bigger kick (more $\Delta\Phi$). Those are exactly the syllabus's "factors affecting the magnitude."
- **A rod sliding on rails** through a field: here you can see the *mechanism* with tools you already own. Every free electron in the moving rod is a moving charge in a field, so the [[Lorentz Force]] $F = Bqv$ pushes it **along the rod** — charge piles up at one end, and the rod becomes a battery of e.m.f. $E = BLv$ (force per charge $Bv$, times length $L$). Motional induction is not new physics; *it is the Lorentz force doing work by another name.*
- **A coil rotating in the field** — the window repeatedly turning face-on and edge-on, flux swinging sinusoidally. Hold that thought; it becomes the generator below.

And the three costumes in motion — for the rod, watch the view swing around: the flat diagram becomes a machine the moment you see it in three dimensions.

![[emi-demo-magnet-coil.mp4]]

![[emi-demo-rod-rails.mp4]]

![[emi-demo-rotating-coil.mp4]]

The stationary-coil, changing-field case (Faraday's iron ring, a transformer) is the one that *is* new physics: no charge is moving, yet an e.m.f. appears — a changing magnetic field creates an **electric field** outright. That upgrade of the law is the doorway to [[Maxwell's Equations]], and the strange fact that both mechanisms give the *same* answer is not a coincidence — see Beyond.

## Lenz's law — nature presents the bill

Faraday gives the size; **Lenz gives the direction: the induced e.m.f. drives effects that oppose the change producing it.** Push a magnet's north pole toward a coil, and the coil's near face becomes a north pole — it *pushes back*. Pull the magnet away, and the face flips to south — it *clings*. The coil is never on your side.

![[emi-lenz.svg|697]]

**And it must be so, or physics would be broke.** Suppose the coil *aided* the change instead: the incoming magnet would be sucked in, speeding up, inducing more current, sucking harder — free kinetic energy plus free electricity out of nothing. Lenz's law is nothing but **conservation of energy signing its name**: the induced current opposes your push *precisely so that the work you do against the opposition becomes the electrical energy you get out* — most of it, in a real machine: bearing friction and the windings' own resistance take their cuts, which is why generator efficiency is an engineering war fought in the high-90s percent. Nature does not refuse to make electricity; she refuses to make it *free*. Every power station on Earth is paying this exact bill — the turbine strains against Lenz's opposition, and the strain, joule for joule, is your electricity.

The bench version of the bill: drop a magnet down a **copper tube** and it descends in slow motion — the falling magnet's changing flux swirls **eddy currents** through the tube wall, and their fields brake the fall. No contact, no friction; pure Lenz. The same trick, engineered: induction cooktops (eddy currents heat the pan itself), magnetic brakes on rollercoasters and high-speed trains (no pads to wear out — and, pure Lenz again, the braking force conveniently *weakens as the train slows*).

For the direction of a motional current, 0625 offers **Fleming's right hand** (thumb **F**orce/motion, first finger **F**ield, second finger induced **C**urrent) — the left hand runs motors, the right hand runs generators, 左手电动机、右手发电机. As always: the hands are the principle *sorted* — when in doubt, return to Lenz and ask which direction *opposes*.

Both rules in full, side by side — the **fingers mean the same three things on either hand**; what changes is which one is the *input*:

| finger | **LEFT hand — motor effect** | **RIGHT hand — generator effect** |
|---|---|---|
| **F**irst finger | **F**ield (N to S) | **F**ield (N to S) |
| se**C**ond finger | **C**urrent — *you supply it* | induced **C**urrent — *the answer* |
| thu**M**b | **M**otion (the force produced) — *the answer* | **M**otion — *you supply it* |
| reach for it when | current is the cause, force the effect | motion is the cause, current the effect |

And here is the same wire under both hands — read the panels left to right and watch what the sign does:

![[emi-two-hand-rules.svg|700]]

Drive a current rightward (left panel) and the wire is pushed up. Push the *same* wire up (right panel) and the induced current comes out — **leftward, opposite the current that would have pushed it up**. Feed that induced current back through the left hand and its force points *down*, against your push. The two hands never contradict each other; they agree by always siding *against* whoever is doing the pushing, and that built-in sign flip **is Lenz's law**. If your two answers ever agree in direction, one hand is upside down.

And the two hands are not rival laws — **they are the same Lorentz force, and Lenz guarantees they agree.** Run a *motor* and, the moment it turns, its coil is sweeping through flux — a generator by geometry — inducing a **back-e.m.f.** whose direction (right hand) opposes the very current driving it: Lenz, operating inside the motor. Load a *generator* and its induced current, sitting in a magnetic field, feels a force (left hand) that opposes the rotation: Lenz, operating inside the generator. Every spinning electrical machine is both devices at once; which hand you reach for only records which quantity you called the cause. Engineering cashes this duality on demand: an F1 car's **KERS** and every EV's regenerative braking ([[Braking Systems]]) flip one machine between the two hands — motor while accelerating, generator while braking — with Lenz's drag *as* the brake pedal's bite and the recovered work banked in the battery.

The copper-tube race, run live — one magnet in free air, its twin inside the tube:

![[emi-lenz-tube.mp4]]

## The a.c. generator — the motor, run backwards

Take the d.c. motor from [[Lorentz Force]] and reverse the deal: instead of feeding current to get rotation, *supply the rotation* — a turbine, a crank, a bicycle wheel — and collect the current. A coil turning in a field is the rotating window: flux swings as $\cos$, so the e.m.f. — its rate of change — swings as $\sin$. The output is inherently **alternating**.

![[emi-generator.mp4]]

The animation's central skill is *the* examined skill — reading the two graphs against the coil's position:

| Coil position | Flux $\Phi$ | e.m.f. | why |
|---|---|---|---|
| **face-on** to the field (window full) | maximum | **zero** | flux is momentarily at a turning point — not changing |
| **edge-on** to the field (window empty) | zero | **maximum** | flux is sweeping through zero at its fastest |

**The e.m.f. graph is the slope of the flux graph** — peaks where flux crosses zero, zeros where flux peaks. If that feels backwards, you are feeling the derivative. And spin the coil **twice as fast** and two things happen at once: the peaks double *and* they come twice as often — amplitude ∝ speed (same flux swing in half the time) and frequency ∝ speed. Doubling speed does **not** just stretch the graph; it stretches it *up* while squeezing it *sideways*.

One piece of hardware distinguishes generator from motor at a glance: **slip rings** — two full, continuous rings, one per coil end — replace the motor's split-ring commutator. The commutator's job was to *flip* the connection every half-turn to force d.c. rotation; the slip rings' job is to *never flip anything*, handing out the honest alternating e.m.f. as-is. (Swap them for a commutator and you have a d.c. dynamo; keep the rings and let the current alternate.)

![[emi-generator-vs-motor.png|697]]

## The transformer — induction with no moving parts

Now remove the motion entirely. Wind two separate coils on one soft-iron core, drive the **primary** with *alternating* current, and its ever-changing flux — guided through the core — threads the **secondary**, whose flux linkage therefore never stops changing: Faraday's law runs continuously, with nothing mechanical at all.

![[emi-transformer.svg|697]]

Each turn of either coil is threaded by the *same* changing flux, so each turn receives the same slice of e.m.f. — the voltages simply count turns:

$$\boxed{\frac{V_p}{V_s} = \frac{N_p}{N_s}} \qquad\qquad \text{and for an ideal (100\% efficient) transformer:}\quad \boxed{I_p V_p = I_s V_s}$$

More secondary turns → **step-up** (voltage rises); fewer → **step-down**. But the second box is the honest one: power in equals power out, so whatever factor the voltage gains, **the current loses**. A transformer is not a free lunch; it is a *currency exchange* — volts for amps at par.

**Why that exchange runs civilisation:** cables waste power as heat at the rate $P_{\text{loss}} = I^2 R$ — the *square* of the current. Transmit a town's power at 256 times the voltage and you carry $\tfrac{1}{256}$ the current, cutting cable losses by a factor of $256^2 = 65{,}536$. So the grid steps **up** to hundreds of kilovolts at the power station, crosses the country thin-wired and cool, and steps back **down** to safe mains at your street. This one $I^2R$ argument is what decided [[Stories/The War of the Currents]] — a.c. won *because it could be transformed*, and the transformer only works because flux must keep changing.

Two housekeeping facts with marks attached. **First: the transformer's iron core is laminated** — built not from solid iron but from thin sheets, each varnish-insulated from its neighbours, stacked like a ream of lacquered paper. The reason is an unwanted guest you have already met: the core is itself a conductor sitting in relentlessly changing flux, so induction would happily drive the same swirling **eddy currents** that braked the magnet in the copper tube — except here they brake nothing useful and simply heat the iron. Slicing the core *across* the swirls' would-be path leaves them nowhere to run: the flux still travels freely *along* the sheets, but the eddies starve in loops a fraction of a millimetre wide.

![[emi-laminated-core.png|640]]

**Second: a transformer fed d.c. does nothing** — steady current, steady flux, no change, no induction. (Worse than nothing: with no induced back-e.m.f. to limit it, the primary overheats. A d.c. transformer is a slowly cooking paperweight.)

## Worked example 1 — Faraday's law, by the numbers

> *A flat coil of 200 turns and area $3.0 \times 10^{-3}\ \text{m}^2$ sits with its plane perpendicular to a uniform field of $0.15\ \text{T}$. The field is reduced steadily to zero in $0.30\ \text{s}$. Find the induced e.m.f.* **[3]**

*Tool: e.m.f. = rate of change of flux linkage — assemble $N\Phi$, then divide by time.*

Initial flux per turn: $\Phi = BA = 0.15 \times 3.0 \times 10^{-3} = 4.5 \times 10^{-4}$ Wb ✓.
Change of flux linkage: $\Delta(N\Phi) = 200 \times 4.5 \times 10^{-4} = 9.0 \times 10^{-2}$ Wb ✓.
$$\text{e.m.f.} = \frac{\Delta(N\Phi)}{\Delta t} = \frac{9.0 \times 10^{-2}}{0.30} = 0.30\ \text{V} ✓.$$

The $N$ forgotten is the mark most often lost — flux and flux *linkage* differ by exactly the factor the examiner is testing.

## Worked example 2 — the generator graphs

> *An a.c. generator's coil rotates at constant speed. (a) State the position of the coil when the e.m.f. is maximum, and explain why. (b) The rotation speed is doubled. Sketch the new e.m.f.–time graph on the same axes.* **[4]**

*Tool: e.m.f. reads the slope of the flux graph; amplitude ∝ speed, frequency ∝ speed.*

**(a)** The e.m.f. is maximum when the coil lies **edge-on to the field** (its plane parallel to $B$) ✓ — there the flux through the coil is passing through zero at its greatest rate, and e.m.f. is the *rate of change* of flux, not the flux ✓.
**(b)** New curve: **twice the peak height and twice the frequency** — peaks at $2E_0$, period halved ✓✓. (Sketches showing doubled amplitude at the *same* period earn half.)

## Worked example 3 — the transformer pays for the grid

> *A power station generates $2.0\ \text{MW}$ at $25\ \text{kV}$. The power is transmitted through cables of total resistance $4.0\ \Omega$, (a) directly, and (b) after a transformer steps the voltage up to $400\ \text{kV}$. Find the power lost in the cables in each case.* **[4]**

*Tool: current from $P = VI$, then loss from $P_{\mathrm{loss}} = I^2 R$ — the square is the whole story.*

**(a)** $I = \dfrac{2.0 \times 10^6}{25 \times 10^3} = 80\ \text{A}$ ✓; $\quad P_{\text{loss}} = 80^2 \times 4.0 = 2.6 \times 10^4\ \text{W} \approx 26\ \text{kW}$ ✓.
**(b)** $I = \dfrac{2.0 \times 10^6}{400 \times 10^3} = 5.0\ \text{A}$ ✓; $\quad P_{\text{loss}} = 5.0^2 \times 4.0 = 100\ \text{W}$ ✓.

Sixteen times the voltage, $16^2 = 256$ times less loss — from 26 kW of wasted heat to a light bulb's worth. That square is why pylons hum at 400 kV.

> [!tip] "But doesn't $P = V^2/R$ say more voltage means MORE loss?"
> The middle-school trio $P = VI = I^2R = V^2/R$ is genuinely all true — **provided every symbol belongs to the same component.** The 400 kV is the voltage across *the whole line-and-load*; it is not the voltage across the cable, so $V^2/R_{\text{cable}}$ fed with 400 kV computes nothing physical. What the cable actually owns is: the **current** through it ($I = P/V_{\text{transmit}}$ — fixed by how much power is being sent at what voltage) and its own small **drop** ($V_{\text{cable}} = IR_{\text{cable}}$ — a few hundred volts out of the 400 000). Feed any of the three formulas *the cable's own numbers* and they agree to the watt. The working habit: **choose the formula whose symbols you actually know for this component** — here that is the current, so $I^2R$ is the honest route, and stepping up the voltage wins because it shrinks that current.

## Misconceptions

> [!warning] "A strong field through a coil induces a large e.m.f."
> A *constant* field induces **nothing**, however strong — Faraday's needle sat still beside his best magnets for a decade. Only the **rate of change** of flux linkage matters: a weak field vanishing quickly can out-induce a monster field drifting slowly. Every exam sentence should contain the word *change* (or *rate*).

> [!warning] "The generator's e.m.f. peaks when the coil catches the most flux."
> Exactly backwards — that face-on moment is where the e.m.f. is **zero**, because the flux is at a turning point and momentarily unchanging. Peak e.m.f. comes at the *empty-window* position, where flux sweeps through zero fastest. The e.m.f. graph is the flux graph's **slope**, and a maximum's slope is zero.

> [!warning] "A transformer can step up d.c."
> Steady current → steady flux → no change → no induction: the secondary delivers precisely nothing (and the primary, missing its self-induced back-e.m.f., quietly cooks). Transformers are a.c.-only devices — which is, in one sentence, why a.c. won [[Stories/The War of the Currents|the War of the Currents]].

> [!warning] "Induced e.m.f. means induced current."
> The e.m.f. appears whenever flux linkage changes — circuit or no circuit — like a battery sitting in a drawer. **Current** (and hence Lenz's opposing *force*) flows only if the circuit is closed. An open-circuit rod on rails glides unbraked, e.m.f. and all; close the switch and you feel the drag at once. This is also why "e.m.f." is the right word on the exam, not "voltage across a component."

## Exam Notes

### Cambridge 9702 A-Level — §20.5 (closing Topic 20)

- **The five LOs verbatim:** define magnetic flux as $B \times$ perpendicular area (definition marks — the word *perpendicular* is load-bearing); recall/use $\Phi = BA$; use **flux linkage** $N\Phi$; *understand and explain the experiments* demonstrating that changing flux induces an e.m.f., that its direction opposes the change, and the factors setting its magnitude; recall and use **Faraday's and Lenz's laws**.
- Question patterns: the Worked-1 computation (with the $N$ trap); explain-the-demo in the scenario's words ("as the magnet enters, the flux linkage of the coil increases, so…"); graph questions pairing $\Phi(t)$ with e.m.f.$(t)$ — draw the derivative, not the copy; and Lenz-as-energy-conservation in two sentences (opposition → work done against it → electrical energy: the marking points in that order).
- **§21.1 note:** the transformer content here (turns ratio, $I_pV_p = I_sV_s$, transmission argument) covers §21.1's transformer bullet; the a.c. *characteristics* half — peak vs r.m.s., $V_{\text{rms}} = V_0/\sqrt{2}$, mean power — belongs to [[Alternating Current]].

### Cambridge 0625 IGCSE — §4.5.1, 4.5.2, 4.5.6

- **§4.5.1 Core:** conductor moving across a field *or* changing field linking a conductor induces an e.m.f.; describe the magnet-and-coil demo (galvanometer, kick on entry, reverse kick on exit, zero at rest); factors: speed, turns, field strength. **Supplement:** direction opposes the change; Fleming's right hand for force–field–current directions.
- **§4.5.2:** describe the simple a.c. generator (rotating coil *or* rotating magnet; **slip rings and brushes** where needed) and — the reliable question — sketch/interpret the e.m.f.–time graph, relating coil positions to peaks, troughs and zeros.
- **§4.5.6 Core:** transformer construction (two coils, soft-iron core), primary/secondary/step-up/step-down vocabulary, $V_p/V_s = N_p/N_s$, use in high-voltage transmission and its advantages. **Supplement:** principle of operation in full sentences (alternating primary current → changing flux in core → changing flux linkage of secondary → induced e.m.f.), $I_pV_p = I_sV_s$ at 100% efficiency, and the $P = I^2R$ cable-loss argument (Worked 3 is exam-shaped).

### AP / IB

- **AP Physics 2:** Faraday and Lenz qualitatively + simple $\Phi = BA\cos\theta$ computations; ranking tasks on "which change induces more." **AP Physics C (E&M):** the full calculus form $\mathcal{E} = -\,d\Phi_B/dt$ with flux integrals, motional e.m.f. derivations, and induced electric fields — this card's Beyond is that course's mainline.
- **IB Physics (HL):** induction sits in the electromagnetism AHL strand with the same Faraday/Lenz core; the existing IB material in the vault covers it incidentally — no IB-specific gaps introduced here.

## Beyond the syllabus

> [!info] Recall the two mechanisms — then notice they are one
> Recall that the rod-on-rails e.m.f. came from the Lorentz force on moving charges, while the transformer's came from a changing field creating an electric field with nothing moving at all. Two utterly different mechanisms, one formula — $\mathcal{E} = -\,d(N\Phi)/dt$ covers both exactly. That "coincidence" nagged at one Swiss patent clerk: the 1905 paper that introduced special relativity **opens with this very asymmetry** — magnet-moves-past-coil and coil-moves-past-magnet are physically identical situations, Einstein insisted, so a theory that explains them differently must be missing something. [[Lorentz Force]]'s Purcell section showed magnetism as relativity in disguise; induction is where Einstein first pulled that thread. The two mechanisms are one fact, seen from two reference frames.

> [!info] So what IS a magnetic field, really?
> A fair demand — the electric field we can picture (charges pushing charges), and gravity got Einstein's curved-geometry analogy. The honest modern answer: **there is no separate magnetic substance.** Recall the Purcell argument from [[Lorentz Force]]: watch moving charges from another seat and length contraction re-balances their charge densities — the "extra" push that appears is precisely what we call magnetism. Electric and magnetic fields are two faces of **one** object (relativity writes them as a single electromagnetic field; how it splits into $E$ and $B$ depends on the observer — a purely magnetic field in your seat is partly electric in your neighbour's). But none of that makes it a fiction: the field is as real as matter — it stores energy (that is what an MRI magnet's quench dumps), carries momentum, and, once [[Maxwell's Equations]] finish the story, travels on its own as light. So the ledger reads: gravity = geometry; electricity = charge pushing charge through a field; **magnetism = the same field, read from a moving seat.**

> [!info] The coil that opposes itself: inductance
> A coil's own current threads its own turns — so when *that* current changes, the coil induces an e.m.f. **in itself**, opposing the change (Lenz, applied reflexively). This *self-induction* makes every coil a flywheel for current: hard to start, hard to stop — the third passive component, the inductor, joining the resistor and the [[Capacitors|capacitor]], and the reason switching an inductive circuit off can spark. It is also the "back-e.m.f." that protects a working transformer's primary — and whose absence is what cooks it on d.c.

> [!info] The secret sameness of power stations — and the 3000 rpm wheel
> Coal, gas, nuclear, geothermal: every one of them is a **kettle**. The fuel's only job is to boil water; the steam spins a turbine; the turbine spins the coil you have just studied. The old engineering joke holds up disturbingly well — *human technology is mostly boiling water more elegantly (the rest is throwing rocks harder)* — and a nuclear reactor is, by that accounting, a very fancy flame under the same kettle. Only hydro and wind skip the boiling (the fluid pushes the blades directly), and only **photovoltaics escapes Faraday entirely** — the one mainstream generator with no spinning coil anywhere inside. And yes, the wheel really does keep grid time: a standard two-pole steam turbine spins at exactly **3000 rpm to make 50 Hz** (3600 rpm for 60 Hz countries) — a fifty-times-a-second blur, which those long thin turbine rotors are built to survive. The two escapes from that breakneck pace: **more poles** — a hydro dam's water wheel ambles at 150 rpm, but with 20 pole-pairs every revolution delivers 20 a.c. cycles, slow wheel, same 50 Hz — and **power electronics**: a modern wind turbine generates at whatever frequency the wind grants, then rectifies and re-synthesises clean 50 Hz. Faraday first; silicon after.

> [!info] Inside your computer's power brick
> How does mains a.c. become the d.c. your PC's chips drink? The old way — the heavy "wall wart" — stepped down at 50 Hz through a big iron transformer, *then* rectified. The modern way is sneakier: **rectify first** to about 325 V d.c., then *chop* that into high-frequency a.c. at 50–150 kHz, push it through a **tiny** transformer, and rectify again to the 12 V and 5 V rails. Why the detour: Faraday's law pays per *rate of change* — raise the frequency a thousandfold and the same voltage needs a thousandth of the flux swing, so the core shrinks from a brick to a thumbnail. Your feather-light USB-C charger is not a transformer *bypass*; it is a transformer *victory* — the change was made to change faster. And this is no computer-only story: **every d.c. appliance you own** — phone charger, games console, router, LED lamp — **goes through this same chain.**

> [!info] Faraday in the kitchen
> An **induction cooktop** is a transformer whose secondary is your saucepan: a coil under the glass drives high-frequency flux, eddy currents swirl in the pan's iron base, and $I^2R$ heats the pan *itself* — the stove surface stays cool because it was never the conductor. **Wireless chargers** are transformers with an air gap (phone coil = secondary). The 1831 iron-ring experiment, verbatim, on your countertop.

## Connections

- **Builds on:** [[Lorentz Force]] — the motional half of induction *is* $F = Bqv$ working along a rod, and the d.c. motor this card runs backwards; the field patterns and $B$-as-flux-density language all carry over.
- **Leads to:** [[Maxwell's Equations]] — the stationary-coil case's "changing $B$ makes $E$" is one of the four equations, and the complete set repays the debt with light itself; [[Alternating Current]] — the generator's inherently alternating output, r.m.s. bookkeeping, and the rest of 9702 §21.
- **Story:** [[Stories/The Bookbinder's Apprentice]] — the man himself: the bindery university, the bound job application, the valet's humiliation, the decade-long notebook question, and the ten days of 1831 this card compresses into one law.
- **Kindred:** [[Capacitors]] — the field-energy sibling: capacitor stores energy in $E$, inductor in $B$, and the pair oscillates; [[Stories/The War of the Currents]] — the $I^2R$ transmission argument of this card is the plot of that story; [[Work, Energy and Power]] — Lenz's law is its signature on every generator crank.
