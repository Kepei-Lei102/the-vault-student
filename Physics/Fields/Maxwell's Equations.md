---
chinese: 麦克斯韦方程组 (Màikèsīwéi fāngchéngzǔ)
prerequisites:
  - "[[Electromagnetic Induction]]"
  - "[[Lorentz Force]]"
  - "[[Capacitors]]"
  - "[[Cross Product]]"
  - "[[The Bookbinder's Apprentice]]"
  - "[[The War of the Currents]]"
leads_to:
  - "[[Electromagnetic Spectrum]]"
  - "[[Special Relativity]]"
tags:
  - subject/physics
  - domain/electromagnetism
  - level/A-Level
  - curriculum/A-Level
  - curriculum/AP-Physics-C-EM
  - type/deep
  - type/theorem
  - misconception/new-physics-on-top
  - misconception/displacement-current-is-charges
  - misconception/light-needs-a-medium
  - misconception/e-and-b-take-turns
---

# Maxwell's Equations 麦克斯韦方程组

> *Four sentences. That is the entire constitution of electricity, magnetism, and — as fell out of the algebra, to everyone's astonishment — light. You have already met each sentence separately, wearing a different chapter's costume: field lines, the unsplittable magnet, Faraday's flux law, the compass twitching beside a wire. This card gathers the four, adds the one patch Maxwell himself supplied — and then does the most famous calculation in physics: two constants measured on a lab bench, one square root, and out comes the speed of light. The bookbinder drew the pictures; the young Scot translated them into mathematics; and the mathematics knew something nobody had told it.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| Maxwell's equations | 麦克斯韦方程组 | the four laws every electric and magnetic field must obey |
| flux (of a field) | 通量 | field × area threaded, counted perpendicular — how much field crosses a surface |
| closed surface | 闭合曲面 | a surface with an inside and outside (a bag); nothing crosses without being counted |
| loop integral / circulation | 环路积分 | walk a closed loop, summing the field's push along your steps |
| displacement current | 位移电流 | Maxwell's patch: a *changing electric field* acts like a current in making B |
| permittivity of free space $\varepsilon_0$ | 真空介电常数 | electricity's bench constant — how easily E-fields thread the vacuum |
| permeability of free space $\mu_0$ | 真空磁导率 | magnetism's bench constant — how strongly currents wrap B around themselves |
| electromagnetic wave | 电磁波 | E and B sustaining each other through empty space — light |

## The four sentences — each one a chapter you have already read

Everything below is written in the **integral** ("count over a surface / walk around a loop") language, because that is the version whose pictures you already own. Two of the sentences count flux through a **closed bag**; two walk a **closed loop**. Two are about E, two about B — and the symmetry of what they say, and where it breaks, is the whole story.

### First, learn to read a sentence

The notation is doing real work, so decode it once and the four laws become sayable out loud:

| Symbol | read as | what it actually is |
|---|---|---|
| $\mathbf{E}$ | the electric field | force per coulomb (N/C = V/m): *what a $+1$ C test charge parked at that point would feel* — the $q\mathbf{E}$ half of [[Lorentz Force]]. An arrow at every point of space. |
| $\mathbf{B}$ | the magnetic field | what a **moving** charge feels — defined by the other Lorentz half, $q\mathbf{v}\times\mathbf{B}$ (units: tesla). Also an arrow at every point. |
| $d\mathbf{A}$ | a tile of surface | "$d$" = *a tiny piece of*. One little tile of the surface, carried as an arrow pointing outward, of size equal to the tile's area. |
| $\mathbf{E}\cdot d\mathbf{A}$ | flux through the tile | the dot product keeps only the part of $\mathbf{E}$ that actually **crosses** the tile — one tile's worth of thread-count ([[Electromagnetic Induction]]'s $\Phi$, tile by tile). |
| $d\mathbf{l}$ | a step of path | one tiny step along a walk; $\mathbf{E}\cdot d\mathbf{l}$ = the field's **push along that step** (work per coulomb for that step). |
| $\oint$ | "the closed integral" | the ordinary "sum the little pieces" $\int$, with **a circle promising the domain closes**: a closed *surface* (a bag with no rim — inside and outside well-defined) for the flux pair; a closed *loop* (you end where you began) for the circulation pair. The closure is load-bearing — only a closed bag can count what is *inside*. |

And one tempting misreading to kill early: $\oint dA$ does **not** "integrate area into volume", and $\oint dl$ does not build an area. The $d$ never means *go up a dimension* here — it means *chop into pieces*. $d\mathbf{A}$ is one tile of a surface you were given, $d\mathbf{l}$ one step of a path you chose, and the integral just re-assembles the pieces after each has been weighted by the field crossing it. Sum plain tiles and you recover the surface's area; sum $\mathbf{E}\cdot d\mathbf{A}$ and you get the field's total **flux** through it — a thread-count, not a geometric volume. The dot product is where the physics lives.

![[maxwell-equations-constitution.svg|700]]

**1 — Gauss's law: charges are where E-lines are born.**

$$\oint \mathbf{E}\cdot d\mathbf{A} = \frac{Q_{\text{inside}}}{\varepsilon_0}$$

Count the electric field threading *out* of any closed bag, and you have counted the charge inside — nothing else. Field lines begin on positive charge and end on negative charge, full stop. This is the field-line bookkeeping you have been drawing since [[Lorentz Force]]'s pattern diagrams, promoted to law — and it *contains* the inverse square: around a point charge the same line-count spreads over a sphere of area $4\pi r^2$, so the field per unit area must fall as $1/r^2$. Coulomb's law is Gauss's law plus geometry.

**2 — Gauss's law for B: there are no magnetic charges.**

$$\oint \mathbf{B}\cdot d\mathbf{A} = 0$$

The same bag-count for the magnetic field always returns *zero*: B-lines never begin and never end — they only close into loops. This is the law behind a demonstration every student has done: saw a bar magnet in half hoping to isolate a north pole, and get two complete magnets. As far as every experiment can tell, the magnetic version of "charge" does not exist — the deepest *asymmetry* in the set (and Beyond tells you what would happen if one monopole were ever found).

**3 — Faraday's law: changing B stirs E into loops.**

$$\oint \mathbf{E}\cdot d\mathbf{l} = -\frac{d\Phi_B}{dt}$$

This is [[Electromagnetic Induction]] — the whole card — compressed to one line: walk any closed loop, and the E-field's total push around it (the e.m.f.) equals the rate at which magnetic flux through the loop is changing. The minus sign *is* Lenz's law, energy conservation in a single character. And notice the quiet upgrade: an electrostatic field (sentence 1) never pushes you round a loop — start and end at the same point and the work is zero. An *induced* E-field does. Change makes things happen — and it makes a genuinely different kind of field: one with circulation.

**4 — Ampère–Maxwell: currents make B loops — and so does changing E.**

$$\oint \mathbf{B}\cdot d\mathbf{l} = \mu_0\left(I_{\text{through}} + \varepsilon_0\frac{d\Phi_E}{dt}\right)$$

The first term is Ørsted's compass twitching beside a wire, promoted to law: walk a loop around a current and B's circulation counts the current through your loop. The second term is Maxwell's own addition — the patch that completed physics — and it deserves its own section.

## The patch — a capacitor breaks Ampère's law

Take Ampère's law as Ørsted and Ampère left it (no second term) and aim it at a charging [[Capacitors|capacitor]]:

![[maxwell-displacement-current.svg|680]]

Draw a loop around the wire. The law says: B's circulation around the loop = $\mu_0 \times$ (current through *any* surface bounded by the loop). And there is the trap — **"any surface" is a promise the old law can't keep.** Stretch the surface flat like a drumskin and the wire punches through it: current $I$. Balloon the same surface sideways so it passes through the capacitor's *gap*: no charge crosses a capacitor gap — current zero. One loop, two legal surfaces, two answers. The law contradicts itself the moment a circuit contains a capacitor.

Maxwell's repair is pure bookkeeping, and it is beautiful. While the capacitor charges, the field between the plates is *growing*. For plates of area $A$ holding charge $Q$, [[Capacitors]] gave $E = Q/(\varepsilon_0 A)$, so the electric flux through the gap surface is

$$\Phi_E = EA = \frac{Q}{\varepsilon_0} \quad\Rightarrow\quad \varepsilon_0\frac{d\Phi_E}{dt} = \frac{dQ}{dt} = I.$$

The changing E-field in the gap is *exactly the same size* as the current in the wire — the books balance to the ampere. Give the changing flux the same B-making rights as a real current, and every surface now agrees. Maxwell called the new term the **displacement current** — a genuinely bad name (nothing displaces, no charge moves in the gap; the honest reading is simply *changing electric flux acts like a current*) — but the physics it encodes is the missing symmetry: **Faraday: changing B makes E. Maxwell: changing E makes B.**

## And then: light

Now put the four sentences in empty space — no charges, no currents, nothing but field — and watch what the two curl laws do to each other:

- a changing **B** creates a curling **E** (sentence 3),
- that **E** is itself changing, so it creates a curling **B** (sentence 4),
- which is changing, so it creates a curling **E** …

A disturbance in the field can *carry itself*, each field regenerating the other, with no medium and no charges anywhere. Combining the two laws (the differential forms in Beyond make this a three-line calculation) yields the standard wave equation, and the wave's speed is locked by the two constants sitting in the equations:

$$v = \frac{1}{\sqrt{\mu_0\,\varepsilon_0}}.$$

Here is the most famous arithmetic in physics. $\mu_0$ and $\varepsilon_0$ were **bench-top numbers** — measured with charged spheres, current balances, and torsion wires, in experiments that had nothing whatever to do with optics:

$$v = \frac{1}{\sqrt{(4\pi\times10^{-7})\,(8.854\times10^{-12})}} = 3.00\times10^{8}\ \text{m s}^{-1}.$$

The measured speed of light. Maxwell, calculating this in the early 1860s against Fizeau's optical measurements, allowed himself one of science's great understatements:

> *"We can scarcely avoid the inference that light consists in the transverse undulations of the same medium which is the cause of electric and magnetic phenomena."* — Maxwell, 1862

Light is not *like* an electromagnetic wave. Light **is** the fields' own ripple — E and B perpendicular to each other and to the direction of travel, in phase, forever handing existence back and forth:

![[maxwell-em-wave.mp4]]

Two decades later (1887) Heinrich Hertz built a spark-gap circuit that *made* these waves at metre wavelengths and caught them across his lab — reflection, refraction, polarisation, all of it, at the predicted speed. Asked what his ripples were for, he reportedly answered "Nothing, I guess — this just proves Maxwell was right" (the quote is a later reconstruction — flag it as folklore, keep the sentiment, which is well documented: Hertz saw no application). Within a decade Marconi was selling the application, and the [[Electromagnetic Spectrum]] — radio to gamma, one law, one speed, different wavelengths — became the century's infrastructure.

> [!info] If these waves are everywhere, why can't you feel them?
> You can — two of your senses are electromagnetic detectors. **Sight** is the direct one: the retina's pigment molecules are tuned receivers for the 400–700 nm band, so every colour you have ever seen was a Maxwell wave being *detected*. **Warmth** is the other: sunshine on your face is infrared being absorbed by the water in your skin — feeling the sun literally is feeling EM waves. What you can't feel is everything else — the wifi, radio and phone signals passing through your body right now — for two honest reasons. First, **feeling requires absorbing**, and at those wavelengths your body is nearly transparent: the waves mostly pass through without depositing energy, the same trick glass plays with visible light. Second, **the fields are feeble and far too fast**: a wifi signal's electric field is around a millivolt per metre, billions of times weaker than anything your nerves register — and it reverses a billion times a second, hopelessly beyond a nerve that counts in milliseconds. The microwave oven is the exception that proves the rule: pick a frequency water absorbs well, push kilowatts instead of milliwatts, and EM waves become extremely feelable.

One more seed, planted here on purpose: the speed $1/\sqrt{\mu_0\varepsilon_0}$ comes out of the equations as a *constant of nature* — the equations do not say relative to **whom**. That innocent-looking omission bothered a patent clerk enough that his 1905 paper was titled "On the Electrodynamics of Moving Bodies" — the thread [[Electromagnetic Induction]]'s Beyond already pulled, and where [[Special Relativity]] begins.

## Worked examples

### Example 1 (AP-C style — Gauss's law earning its keep)

> A solid metal sphere of radius $R$ carries total charge $+Q$. Find the electric field at distance $r > R$ from the centre.

*Tool: Gauss's law — choose the bag to match the symmetry.*
By symmetry the field points radially and has the same size everywhere on a concentric sphere of radius $r$. Choose that sphere as the Gaussian bag: the flux count is $E \times 4\pi r^2$ (field constant, everywhere perpendicular to the bag), and the charge inside is $Q$:

$$E \cdot 4\pi r^2 = \frac{Q}{\varepsilon_0} \;\Rightarrow\; E = \frac{Q}{4\pi\varepsilon_0 r^2}.$$

The sphere behaves, outside itself, exactly like a point charge — the $1/r^2$ arriving as pure geometry, no integration over the sphere's surface required. *That* is why Gauss's law is loved: symmetry does the work.

### Example 2 (the displacement current, priced)

> A parallel-plate capacitor with circular plates of radius $5.0$ cm is charged so that the field between the plates grows at $dE/dt = 2.0\times10^{12}\ \text{V m}^{-1}\text{s}^{-1}$. Find the displacement current.

*Tool: Maxwell's term $I_d = \varepsilon_0\, d\Phi_E/dt$ with $\Phi_E = EA$.*
$$I_d = \varepsilon_0 A \frac{dE}{dt} = (8.854\times10^{-12})(\pi \times 0.050^2)(2.0\times10^{12}) \approx 0.14\ \text{A}.$$

A seventh of an ampere of "current" flowing through a gap containing nothing — and the B-field it generates in the gap is measurably real. The bookkeeping term has physical muscle.

## Common Misconceptions (Teaching Notes)

### 1. "Maxwell's equations are new physics stacked on what I learned"

They are the *same* physics, written tight: sentence 1 is the field-line rules, sentence 2 is the unsplittable magnet, sentence 3 is the [[Electromagnetic Induction]] card entire, sentence 4 is the wire-and-compass fact plus one patch. **Fix:** go sentence by sentence and name the chapter each one compresses. The achievement is the *unification*, not new ingredients — and unification had one genuinely new consequence: light.

### 2. "Displacement current means charges move across the gap"

Nothing crosses the gap — that is the point of a capacitor. **Fix:** rename it in your head: *changing-flux term*. It is a changing E-field that has been granted a current's B-making rights, because the accounting ($\varepsilon_0\,d\Phi_E/dt = I$, shown above) balances exactly. The name is historical baggage from Maxwell's mechanical aether models; keep the term, drop the imagery.

### 3. "A wave needs a medium — so what waves?"

The Victorians agreed with you and invented the *luminiferous aether* to be the medium; Michelson and Morley (1887) went looking for the Earth's motion through it and found, famously, nothing. **Fix:** the field itself is the physical object — [[Capacitors]] already showed it storing energy in empty space ($\tfrac12\varepsilon_0E^2$ per cubic metre). A thing that holds energy can carry a wave. E and B are not ripples *in* something; they are the something.

### 4. "E creates B, then B creates E, taking turns like dominoes"

The leapfrog is *causal bookkeeping*, not a time-sequence — in a travelling light wave E and B peak **together**, in phase, perpendicular to each other and to the motion. **Fix:** watch the animation frame by frame: nowhere does one field wait for the other. The regeneration story explains why the wave *can* sustain itself; the solution the equations actually pick has both fields riding the same crest.

## Exam Notes

### Cambridge 9702 / 0625

- **The unified equations are not examined on either board.** What *is* examined is every ingredient: electric field lines and field strength (9702 Topic 18), magnetic field patterns and forces (Topic 20.1–20.4, [[Lorentz Force]]), electromagnetic induction (Topic 20.5, [[Electromagnetic Induction]]), and the electromagnetic spectrum with its one-speed-in-vacuum fact ($3.0\times10^8\ \text{m s}^{-1}$ — 9702's waves topics; 0625 §3.3, where the ordered spectrum and uses are required). This card is the capstone that shows why those chapters were one subject all along.

### AP Physics C: Electricity & Magnetism

- The one school-level course where this card is on-syllabus territory: **Gauss's law is assessed quantitatively** (Unit 8 — spherical/cylindrical/planar symmetry, Example 1's method), **Faraday's law in calculus form** (Unit 13), and **Ampère's law** with the displacement-current idea; the four as a unified set are *referenced but not assessed in depth*, and deriving the EM wave is explicitly out of scope. Know the capacitor paradox qualitatively — it is the standard motivation the course expects. (And yes: this mathematics is exactly why AP-C E&M carries its reputation as the hardest AP — it is the only school course that asks teenagers for surface and line integrals.)

### IB Physics

- Fields are covered (D.2–D.3) at integrated-forms level; Gauss's and Maxwell's equations are **not named**. Enrichment for the HL student who asks why $c$ appears in electricity.

## Beyond the syllabus

> [!info] The T-shirt — differential forms
> Recall that flux-through-a-bag and circulation-round-a-loop have *point-sized* versions: **divergence** (outflow per unit volume) and **curl** (circulation per unit area). In that language the four sentences shrink to: $\nabla\!\cdot\!\mathbf{E} = \rho/\varepsilon_0$, $\nabla\!\cdot\!\mathbf{B} = 0$, $\nabla\!\times\!\mathbf{E} = -\partial\mathbf{B}/\partial t$, $\nabla\!\times\!\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$ — the version printed on the T-shirts, and the version in which "combine the two curl equations, get the wave equation" is genuinely three lines. The machinery (vector calculus) is first-year university; every idea in it is already on this card in surface-and-loop costume.

> [!info] The missing monopole
> Sentence 2 is the odd one out: its right-hand side is the only hard zero. If a single magnetic charge — a **monopole** — existed anywhere, the set would become perfectly symmetric between E and B (magnetic charge density in sentence 2, a magnetic current term in sentence 3). Dirac showed in 1931 that even *one* monopole in the universe would explain why electric charge is quantised — one of physics' most elegant might-have-beens. Searches continue; the count so far stands at zero (one famous candidate event, Valentine's Day 1982, never repeated).

> [!info] E and B are one object
> [[Lorentz Force]]'s Beyond hinted at it with Purcell's argument: what one observer calls a magnetic force, an observer riding with the charge calls electric. Maxwell's equations are the reason the split is observer-dependent — the speed $c$ they contain is the same for everyone, and taking *that* seriously forces space and time to mix ([[Special Relativity]]), whereupon E and B reveal themselves as six components of a single electromagnetic field tensor. The equations were relativistic twenty years before relativity; nobody had noticed what they were saying.

## Connections

- **Builds on:** [[Electromagnetic Induction]] — sentence 3 *is* that card, minus sign and all; [[Lorentz Force]] — the field-pattern pictures behind sentences 1 and 4, and the fifth equation of electromagnetism ($\mathbf{F} = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}$ — how the fields the four sentences govern push back on matter); [[Capacitors]] — the gap where Ampère's law broke, the $E = Q/\varepsilon_0 A$ used in the repair, and the field-energy density that makes "the field is the medium" more than a slogan.
- **Leads to:** [[Electromagnetic Spectrum]] — one law, one speed, every wavelength from radio to gamma; [[Special Relativity]] — the constant $c$ with no "relative to whom" attached, and the 1905 paper named after electrodynamics.
- **Kindred:** [[Stories/The Bookbinder's Apprentice]] — Faraday drew the field pictures this card's mathematics translates; Maxwell's "in reality a mathematician of a very high order" is the verdict the four sentences vindicate; [[Stories/The War of the Currents]] — the industrial world built on sentence 3; [[Cross Product]] — the right-hand machinery underneath every circulation on this card.
