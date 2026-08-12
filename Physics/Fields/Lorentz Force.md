---
chinese: 洛伦兹力 (luòlúnzī lì)
prerequisites:
  - "[[Cross Product]]"
  - "[[Electric Field]]"
  - "[[Electric Current]]"
  - "[[Stories/The War of the Currents]]"
  - "[[The War of the Currents]]"
leads_to:
  - "[[Electromagnetic Induction]]"
  - "[[Maxwell's Equations]]"
  - "[[Stories/Franklin's Coin Flip]]"
  - "[[Franklin's Coin Flip]]"
tags:
  - subject/physics
  - domain/electromagnetism
  - level/IGCSE
  - level/A-Level
  - level/AP
  - syllabus/9702-20-1
  - syllabus/9702-20-2
  - syllabus/9702-20-3
  - syllabus/9702-20-4
  - syllabus/0625-4-5
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - curriculum/IB-Physics
  - type/deep
  - misconception/magnetic-force-does-work
  - misconception/force-along-field-lines
  - misconception/stationary-charge-feels-b
  - misconception/one-hand-fits-all
---

# Lorentz Force 洛伦兹力

> *Every force you met in mechanics pushes along something sensible — along the string, down the slope, toward the planet. The magnetic force refuses all of that. It ignores charges that stand still, it pushes **sideways** — perpendicular to the velocity and* to the field at once — and it never does a joule of work. Three strange rules; and out of them come electric motors, mass spectrometers, the aurora, your old tube TV, and the magnetic bottles that hold star-hot plasma. The sideways force is the [[Cross Product]] made flesh:
> $$\mathbf{F} = q\,\mathbf{E} + q\,\mathbf{v} \times \mathbf{B}.$$
## 中文锚点

| English                          | 中文            | one-line meaning                                                                                                       |
| -------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Lorentz force                    | 洛伦兹力          | the full force on a charge: electric part + magnetic part                                                              |
| force on a current-carrying wire | 安培力           | Chinese textbooks give the wire's force its own name — this card shows it is the *same* force, summed over the charges |
| magnetic flux density $B$        | 磁通密度 / 磁感应强度  | the field's strength, defined by the force it exerts; unit tesla                                                       |
| tesla (T)                        | 特斯拉           | $1\ \text{T} = 1\ \text{N}\,\text{A}^{-1}\,\text{m}^{-1}$                                                              |
| Fleming's left-hand rule         | 左手定则          | thu**M**b = **M**otion (force), **F**irst finger = **F**ield, se**C**ond finger = **C**urrent                          |
| right-hand grip rule             | 右手螺旋定则 / 安培定则 | thumb along the current, fingers curl along the field circles                                                          |
| velocity selector                | 速度选择器         | crossed $E$ and $B$: only one speed passes straight through                                                            |
| Hall effect / Hall voltage       | 霍尔效应 / 霍尔电压   | charges shoved sideways inside a conductor pile up and reveal both $B$ and their own sign                              |
| solenoid                         | 螺线管           | a coil whose field is a bar magnet you can switch off                                                                  |
| commutator                       | 换向器           | the split ring that flips a motor coil's current every half turn                                                       |

## The field first — and how we measure its strength

A magnetic field $\mathbf{B}$ is drawn with field lines exactly as an [[Electric Field]] is — direction along the line, strength in their crowding — but its *sources* are different: **currents** (and the intrinsic magnetism of materials, which is atomic currents in disguise). The exam's three drawings, all made with the right-hand grip rule (thumb = current, curling fingers = field):

- **A long straight wire:** concentric circles around the wire, spacing out with distance.
- **A flat coil:** through the middle in one direction, looping around outside.
- **A solenoid:** a bar magnet's field, made of wire — nearly uniform inside, weak outside, with a north face and a south face. Slide an iron core in and the field strengthens dramatically: that is the electromagnet, and the reason a scrapyard crane can *switch off* its magnetism.

![[lorentz-field-patterns.svg|697]]

How strong is a field? Physics answers operationally: **by the force it produces.** Put a wire of length $L$ carrying current $I$ perpendicular to the field and measure the force $F$ on it; the **magnetic flux density** is

$$B = \frac{F}{IL},$$

the *force per unit current per unit length* — that sentence, verbatim, is the 9702 definition. Its unit, the **tesla**, is one newton on one ampere-metre. A tesla is enormous: Earth's field is ${\sim}50\ \mu\text{T}$, a fridge magnet ${\sim}5\ \text{mT}$, an MRI bore a few T.

## Force on a current — the motor's heartbeat

A wire carrying current $I$, with length $L$ inside a field $B$, at angle $\theta$ to the field, feels

$$F = BIL\sin\theta,$$

maximum when wire ⊥ field, zero when parallel. Direction: **Fleming's left hand** (左手定则) — first finger along the **F**ield, second finger along the **C**urrent, and the thumb reports the **M**otion the force wants. In vector language it is $\mathbf{F} = I\,\mathbf{L} \times \mathbf{B}$ — the same cross product, wearing a wire.
![[lorentz-hand-rules.png|697]]
**Where the formula comes from.** A current is not a new kind of object; it is a parade of drifting charges, and the wire's force is just their individual forces added up. *Tool: count the marchers.* In length $L$ of wire with $n$ carriers per unit volume, cross-section $A$, charge $q$, drift speed $v$: there are $N = nAL$ of them, each feeling $Bqv$ (next section). Total:

$$F = (nAL)(Bqv) = B\,(nAqv)\,L = BIL,$$

since $I = nAqv$ is precisely the current (the carrier-counting formula that [[Electric Current]] derives). The macroscopic 安培力 *is* the microscopic 洛伦兹力, summed — one force, two bookkeeping styles.

**The d.c. motor** is this force put on a pivot. A rectangular coil in the field: current runs *up* one side and *down* the other, so the two sides feel **opposite forces** — a couple, which turns the coil. Left alone it would swing to the vertical and stop; the **split-ring commutator** reverses the current every half turn, so the couple always torques the same way and the coil spins continuously. More turns, more current, stronger field → more torque. Every fan, drill, and windscreen wiper is this diagram; the industrial version of the idea is the war [[Stories/The War of the Currents]] was fought over.

Watch one revolution — the couple, the dead vertical moment, and the commutator's flip:

![[lorentz-motor.mp4]]

**Two parallel wires** attract when their currents agree and repel when they oppose (each sits in the circular field of the other — apply the left hand once per wire). This tidy force once *defined* the ampere; since 2019 the SI defines the ampere from the electron's charge instead, and the parallel-wire picture retires into an honest footnote.

## Force on a moving charge — the sideways law

Strip the wire away. A single charge $q$ moving at velocity $\mathbf{v}$ through a field $\mathbf{B}$ feels

$$\mathbf{F} = q\,\mathbf{v} \times \mathbf{B}, \qquad F = Bqv\sin\theta,$$

and the three strange rules follow straight from the [[Cross Product]]:

1. **No motion, no force.** $v = 0 \Rightarrow F = 0$. A magnetic field is invisible to a stationary charge.
2. **Sideways, always.** $\mathbf{F}$ is perpendicular to both $\mathbf{v}$ and $\mathbf{B}$. For a *negative* charge, flip the answer — an electron's force points opposite to the left-hand prediction (or keep the left hand and point the second finger against the electron's motion, along conventional current).
3. **No work, ever.** Because $\mathbf{F} \perp \mathbf{v}$ at every instant, the magnetic force changes a charge's *direction* but never its *speed*. Kinetic energy is untouchable. The magnetic field is nature's perfect steering wheel: all turning, no pushing.

![[lorentz-geometry.svg|697]]

**Rule 3 has a glorious consequence.** A steady sideways force of constant magnitude, always perpendicular to the motion — that is the exact recipe for **circular motion**. The magnetic force *is* the centripetal force:

$$Bqv = \frac{mv^2}{r} \quad\Longrightarrow\quad r = \frac{mv}{Bq}.$$

Fast or heavy particles curve gently (big $r$); strong fields and large charges curl them tight. And the period hides a miracle — *Tool: circumference over speed:*

$$T = \frac{2\pi r}{v} = \frac{2\pi}{v}\cdot\frac{mv}{Bq} = \frac{2\pi m}{Bq}$$

— **the speed cancels.** Every particle of a given type takes the same time per lap, fast or slow. That single cancellation is the working principle of the cyclotron: kick the particle twice per lap with an alternating voltage at this fixed frequency, and it spirals outward, always arriving at the gap exactly on beat.

If $\mathbf{v}$ also has a component *along* $\mathbf{B}$, that component sails on untouched (no perpendicular, no force) while the rest circles: the path is a **helix** winding along the field line. This is why charged particles from the Sun travel *along* Earth's field lines and funnel toward the poles — where they crash into the atmosphere and light it up as the **aurora**. The northern lights are the sideways law, drawn in the sky.

![[lorentz-helix-aurora.svg|697]]

![[lorentz-orbits.mp4]]

## Crossed fields — the velocity selector

Point an electric field down and a magnetic field into the page across the same region, and send charges through. The electric force $qE$ pushes one way; the magnetic force $Bqv$ pushes the other — but only the magnetic one cares about speed. The two balance for exactly one velocity:

$$qE = Bqv \quad\Longrightarrow\quad v = \frac{E}{B}.$$

Charges at that speed sail through dead straight; slower ones bend with the electric force, faster ones with the magnetic. A slit at the far end passes a single speed — a **velocity selector**, the front door of every mass spectrometer (select $v$ first, then let a second field's $r = mv/Bq$ sort the masses; the same crossed-field balance was how J. J. Thomson weighed the electron in 1897).

## The Hall effect — the sideways law caught indoors

Run a current through a flat slab with a field $\mathbf{B}$ through its face. The drifting carriers get shoved **sideways** (same law, indoors now) and pile up along one edge, leaving the opposite edge oppositely charged.

![[lorentz-hall.svg|697]]The pile-up builds an internal electric field that pushes back on later carriers, and it grows until the two forces balance — $qE_{\text{internal}} = Bqv$ — a steady-state that appears as a measurable voltage across the slab, the **Hall voltage**:

$$V_H = \frac{BI}{ntq}$$

($n$ = carrier density, $t$ = slab thickness along $\mathbf{B}$). Two gifts follow. Practically, $V_H \propto B$ makes the slab a **magnetometer** — the Hall probe is how a lab (and the magnetic-field sensor row of [[Sensors and Control Systems]], and the lid-closed sensor in a laptop) measures fields. Deeply, the *sign* of $V_H$ reveals the *sign of the carriers*: metals answer "negative, as expected" — and some semiconductors answer **positive**, forcing physics to take seriously the idea that missing electrons ("holes") flow as real positive carriers. A tabletop voltage, quietly reporting quantum mechanics. (Note why $V_H$ is tiny in copper but healthy in a semiconductor: $n$ sits in the denominator — fewer carriers must each drift *faster* to carry the same $I$, and faster drift means a bigger sideways shove.)

## Worked examples — every tool named

![[lorentz-worked.svg|697]]

**(a) The electron's circle (9702 style).** *An electron ($m = 9.11 \times 10^{-31}\ \text{kg}$, $q = 1.60 \times 10^{-19}\ \text{C}$) moves at $4.0 \times 10^{7}\ \text{m s}^{-1}$ perpendicular to a uniform field of $2.0\ \text{mT}$. Find the radius of its path, and state what happens to its speed.*

*Tool: the sideways force is the centripetal force — $r = mv/(Bq)$.*

$$r = \frac{mv}{Bq} = \frac{(9.11\times 10^{-31})(4.0\times 10^{7})}{(2.0\times 10^{-3})(1.60\times 10^{-19})} = 0.11\ \text{m}.$$

The speed is **unchanged** — the magnetic force is perpendicular to the velocity throughout, so it does no work on the electron. (Writing that *sentence*, not just the number, is what the last mark pays for.)

**(b) Which way does the wire jump?** *A horizontal wire carries current due north, in a region where the field points vertically downward. Find the direction and size of the force per metre if $B = 0.20\ \text{T}$ and $I = 3.0\ \text{A}$.*

*Tool: Fleming's left hand, then $F = BIL\sin\theta$ with $\theta = 90°$.*

First finger down (field), second finger north (current) → thumb points **west**. Magnitude per metre: $F/L = BI = 0.20 \times 3.0 = 0.60\ \text{N m}^{-1}$. State direction *and* magnitude — the direction mark is the one dropped.

**(c) Tuning the selector.** *A velocity selector must pass ions at $2.5 \times 10^{5}\ \text{m s}^{-1}$ using a magnetic field of $0.30\ \text{T}$. What electric field is needed, and what happens to slower ions?*

*Tool: the balance $qE = Bqv$ — charge cancels, so the answer is charge-blind.*

$E = Bv = 0.30 \times 2.5 \times 10^{5} = 7.5 \times 10^{4}\ \text{V m}^{-1}$. Slower ions feel the same electric force but a *weaker* magnetic force, so they bend toward the electric side and miss the slit. (Notice $q$ cancelled: the selector sorts by speed alone, for any charge — that is exactly why it is stage one of a mass spectrometer, not the whole machine.)

## Misconceptions

> [!warning] "The magnet did work — it lifted the nail!"
> On a *free moving charge*, the magnetic force does **no work, ever** — it is always perpendicular to the velocity, so speed and kinetic energy never change. (Lifting a nail is a subtler story involving the nail's internal magnetism and internal forces — at this level, hold the clean rule: in a pure magnetic field, a charge's speed is constant. Exam questions test exactly this sentence.)

> [!warning] "The force points along the field lines."
> Electric force does; magnetic force *never* does. $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$ is perpendicular to $\mathbf{B}$ (and to $\mathbf{v}$) by the nature of the [[Cross Product]]. Field lines are the *ingredient*, not the direction of the push.

> [!warning] "The field pushes the charge sitting on the bench."
> A stationary charge feels nothing from $\mathbf{B}$ — no $v$, no force. If a charge at rest accelerates, an *electric* field is present. This one distinction sorts most "which field is it?" exam parts.

> [!warning] "One hand fits all."
> Fleming's **left** hand serves force-on-current (and positive charges); the right-hand **grip** serves field-around-current; and electrons flip the left hand's answer (or: point the second finger along *conventional* current, opposite the electron flow). Chinese students meet 左手定则 for both wire and charge — consistent, as this card proves by summing the parade — but keep it away from 安培定则's right-hand curl.
>
> And why does conventional current point *against* the electrons at all? Because in the 1750s Benjamin Franklin, reasoning that electricity was one fluid that bodies could have too much or too little of, had to guess which side had the surplus — and named glass rubbed with silk "positive." It was a fair coin flip, made 150 years before anyone could check. When Thomson found the electron in 1897, the mobile carrier in metals turned out to be the *other* one. Every "current arrow opposite the electron flow" you will ever draw is the fossil of that guess ([[Stories/Franklin's Coin Flip]]).

> [!info] Beyond syllabus — where the sideways law leads
> - **Magnetism is relativity in disguise — and this answers "why sideways?".** Ride alongside the drifting electrons of a current-carrying wire and, in your frame, the wire's positive and negative charge densities **length-contract by different amounts** — the wire appears *charged*, and pulls on you *electrically*: a plain, honest pull **straight toward the wire**. Hop back to the lab frame and that same pull, re-bookkept for your motion, is what we call the magnetic force — and notice what "straight toward the wire" becomes: a force perpendicular to your velocity. **The sideways-ness is not a new mystery; it is an ordinary electric pull, seen from a moving seat.** Purcell's great reveal: $\mathbf{B}$ is not a second force of nature but the first one, relativity-corrected — the unification [[Maxwell's Equations]] completes.
>
> ![[lorentz-relativity.svg|660]]
>
> - **The magnetic bottle.** Since charges spiral *along* field lines, a clever field shape becomes a container with no walls: tokamaks hold $10^{8}$-kelvin fusion plasma on closed field lines, and Earth's own field bottles the Van Allen radiation belts — the same trick, planet-sized.
> - **Rule 3 as an engineering principle.** "All steering, no pushing" is why magnets guide and focus the beam in every particle accelerator — steering costs no beam energy — while *electric* fields must do all the accelerating. The **Large Hadron Collider** near Geneva is the extreme case: a 27 km ring of superconducting magnets whose entire job is to bend the protons around, while comparatively small electric-field cavities do every joule of the pushing.
> - **The quantum sequel.** Cool a thin Hall slab toward absolute zero in a huge field and something astonishing happens: the Hall resistance $V_H/I$ stops varying smoothly with $B$ and **locks onto exact plateaus** at $R = h/(ne^2)$ — Planck's constant over the electron charge squared, divided by a whole number. Flat to parts per billion, *regardless of the sample's shape, size, or dirt*. (The classical circles have become quantized orbits — Landau levels — and whole levels fill one at a time.) The steps are so exact that metrology adopted them as the world's resistance standard: the sideways voltage, discovered with a slab and a magnet, became a ruler built from fundamental constants. Two Nobel prizes and counting.

## Exam Notes

### Cambridge 9702 (A-Level) — §20.1–20.4 Magnetic fields

- **§20.1** — field as a region where a force acts on a current/moving charge/magnetic material; represent with field lines.
- **§20.2** — $F = BIL\sin\theta$; **define flux density as the force per unit current per unit length on a conductor perpendicular to the field** (the definition is asked verbatim); the tesla; Fleming's left hand for direction.
- **§20.3** — $F = BQv\sin\theta$; circular orbits with $r = mv/(BQ)$ *derived by equating to centripetal force* (show the equating step); **velocity selection** by crossed $E$ and $B$ ($v = E/B$); the **Hall voltage** $V_H = BI/(ntq)$ — given on the formula sheet, but *explain* the balance that produces it (sideways force piles carriers until the internal electric force cancels it) and why semiconductors make better probes (small $n$, large $V_H$).
- **§20.4** — sketch the three field patterns (wire / flat coil / solenoid); effect of a ferrous core; explain the **force between parallel currents** qualitatively (each wire sits in the other's field — no formula required).
- **§20.5 (electromagnetic induction) is deliberately not here** — flux, Faraday and Lenz live in [[Electromagnetic Induction]].

### Cambridge 0625 (IGCSE) — §4.5 electromagnetic effects (motor half)

- **Core:** describe the motor effect — a current-carrying conductor in a field experiences a force; recall the relative directions of force, field and current; describe the d.c. motor's turning effect.
- **Extended:** use $F = BIL$ quantitatively; sketch the wire/solenoid field patterns; explain the **split-ring commutator** (reverses the current each half turn so the couple keeps turning the same way) and how to increase the turning effect (current, turns, field strength).
- The generator and transformer belong to the induction half of §4.5 → [[Electromagnetic Induction]].

### AP Physics

- **AP Physics 2:** magnetic fields unit — $F = qvB\sin\theta$ and $F = BIL\sin\theta$, direction by right-hand rule (AP teaches RHR-with-palm-push rather than Fleming — same geometry, pick one and be consistent), circular motion of charges, qualitative field patterns.
- **AP Physics C: E&M:** full vector $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, cyclotron motion with derivations, velocity selector, and the Biot–Savart/Ampère field calculations that this card's sketches only gesture at.

### IB Physics — D.3 Motion in electromagnetic fields

- The named skills: force on a moving charge and on a current, circular paths of charges in uniform fields, and the crossed-field velocity selector — this card's §20.2–20.3 content under an IB heading.

## Connections

- **Parent:** [[Cross Product]] — this card cashes that card's electromagnetic foreshadow: $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$ is the cross product's flagship physical job, right-hand geometry and all.
- **Uses:** [[Electric Field]] — the $q\mathbf{E}$ half of the full Lorentz force, and the balancing act inside both the velocity selector and the Hall slab.
- **Leads to:** [[Electromagnetic Induction]] — move the *wire* instead of the charge and the same sideways force drives charges along it: Faraday's flux law is next; [[Maxwell's Equations]] — the four-line constitution that makes electric and magnetic fields one object.
- **Story:** [[Stories/The War of the Currents]] — the human prologue: every motor in that war spins on $F = BIL$.
- **CS bridge:** [[Sensors and Control Systems]] — the magnetic-field row's Hall probe and reed switch are this card's physics in a sensor's costume; a laptop's lid-closed detection is a Hall slab reading a magnet.
- **Mechanics bridge:** circular motion supplies the $mv^2/r$ that the sideways force equals — the orbit radius formula is one line of statics between two cards.

## What's on the formula sheet — and what isn't

**MF (9702) gives:** the Hall voltage $V_H = BI/(ntq)$.
**You supply:** $F = BIL\sin\theta$, $F = BQv\sin\theta$ *(both quoted in the syllabus statements — learn them)*, $B = F/IL$ as a definition in words, $r = mv/(BQ)$ *(derive it: equate $BQv$ to $mv^2/r$)*, $v = E/B$ *(derive it: balance the two forces)*, and every direction rule.

## Glossary

| term | 中文 | one-liner |
|---|---|---|
| magnetic flux density $B$ | 磁通密度 | force per unit current per unit length on a perpendicular wire |
| tesla | 特斯拉 | $\text{N}\,\text{A}^{-1}\,\text{m}^{-1}$; Earth's field is ~$50\ \mu$T |
| motor effect | 电动机效应 | a current-carrying conductor in a field feels a force |
| couple | 力偶 | equal and opposite forces on the coil's two sides — pure turning |
| split-ring commutator | 换向器 | flips the coil current every half turn to keep the torque one-way |
| cyclotron period | 回旋周期 | $2\pi m/(Bq)$ — speed cancels, every lap takes the same time |
| helix | 螺旋线 | circle across the field + free glide along it |
| Hall voltage | 霍尔电压 | the sideways pile-up's steady-state voltage, $BI/(ntq)$ |
| velocity selector | 速度选择器 | crossed fields pass only $v = E/B$ |

## LaTeX Reference

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathbf{F} = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$ | the full Lorentz force | electric part + magnetic part |
| $F = BIL\sin\theta$ | force on a current | maximum ⊥, zero ∥ |
| $F = BQv\sin\theta$ | force on a moving charge | the same law, one carrier at a time |
| $r = mv/(BQ)$ | orbit radius | from $BQv = mv^2/r$ |
| $T = 2\pi m/(BQ)$ | orbit period | speed-independent — the cyclotron's secret |
| $v = E/B$ | velocity selector | from $qE = BQv$; charge cancels |
| $V_H = BI/(ntq)$ | Hall voltage | on the 9702 formula sheet |
