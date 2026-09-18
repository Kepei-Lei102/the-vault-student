---
chinese: 仪器校准 (yíqì xiàozhǔn)
prerequisites:
  - "[[Accuracy vs Precision]]"
  - "[[Physical Quantities and Units]]"
  - "[[Repeated Measurements]]"
  - "[[Upper and Lower Bounds]]"
  - "[[The Pendulum Story]]"
teach_together:
  - "[[Temperature and Thermometry]]"
leads_to:
  - "[[Significant Figures]]"
  - "[[Error Propagation]]"
  - "[[Stories/The Pendulum Story]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/experimental-physics
  - domain/measurement
  - domain/metrology
  - domain/foundations
  - level/A-Level
  - level/IB
  - level/AP
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-Mechanics
  - curriculum/AP-Physics-C-EM
  - syllabus/9702-1-3
  - syllabus/0625-P4
  - syllabus/0625-P6
  - type/deep
  - type/definition
  - notation/zero-error
  - notation/correction-factor
  - misconception/calibration-equals-averaging
  - misconception/calibrate-once-forever
  - misconception/standard-mass-is-exact
  - misconception/precision-implies-accuracy
---

# Calibration of Instruments 仪器校准

## Hunter trace — Hubble's first light, April 1990

The Hubble Space Telescope launched on **24 April 1990** carrying what was meant to be the most precisely figured optical mirror humans had ever made — a 2.4-metre primary, polished by Perkin-Elmer for $\$350$ million over six years to a tolerance roughly **one fifty-thousandth** of a human hair. The mission promised the universe at unprecedented sharpness; the entire science community held its breath through commissioning.

The first images came back **blurred**.

Stars were not points. They sat inside soft halos that no amount of refocusing could remove. The telescope had spherical aberration — the centre of the mirror focused light to one point and the edge focused it to another, $40~\text{mm}$ apart along the optical axis. By June 1990 the inquiry board had its answer. The mirror was *not* miscut by accident. It had been polished — precisely, methodically, beautifully — *to the wrong shape*. The figure was off by roughly $2~\mu\text{m}$ at the edges; a tiny error by the standards of any other engineering, a catastrophe at this scale.

How does that happen? Perkin-Elmer's main test instrument was a **reflective null corrector** — a device that produces an interference pattern showing where the mirror's actual curvature deviates from the designed optical figure. The null corrector contained a small metering rod whose length set the device's reference. During assembly in 1981, a technician had set the rod's position using a measuring tool that *was itself uncalibrated*: a tiny chip of anti-reflective coating on a lens had been mistaken for the actual lens edge, and the rod ended up positioned $1.3~\text{mm}$ wrong.

**Every subsequent measurement of the mirror's shape used a reference that was off by 1.3 mm.** The mirror was then polished, repeatedly and accurately, to match what the null corrector said was correct. The aberration was not introduced during polishing; the aberration was *defined* by the null corrector before polishing began. The mirror was a perfect realisation of an imperfect target.

Worse: Perkin-Elmer *had* two other null correctors, both of which would have caught the error if anyone had cross-checked. Those instruments were considered less precise and weren't used in the final verification. **The most precise instrument was trusted absolutely**, and its calibration error propagated downstream undetected. The mirror was launched in 1990 with the imprinted memory of a 1981 calibration failure.

The fix arrived three and a half years later. **December 1993, Servicing Mission 1**: astronauts installed COSTAR (the Corrective Optics Space Telescope Axial Replacement) — a set of compensating mirrors that effectively gave Hubble a pair of corrective glasses. The science programme finally began. Total cost of the calibration error: roughly $\$1.5$ billion in additional missions, hardware, and lost productivity.

The lesson is unforgiving and pedagogically permanent. **Repeating the same biased measurement does not by itself reveal the calibration error**, because the instrument that does the repeating is the instrument with the error. The mirror was polished a thousand times against the same null corrector; every check said it was perfect; every check was based on the same lie. The fix had to come from *outside the chain* — a different instrument, a different test rig, a different observer. Independent reference checks help prevent this failure.

## Definition

**Calibration** establishes the relationship between reference values and an instrument's indications, including the associated uncertainties. That relationship lets a later indication be converted into a measurement result. **Adjustment** physically or electronically changes the instrument; it is a different operation and should be followed by a calibration check. [International Vocabulary of Metrology](https://jcgm.bipm.org/vim/en/2.39.html)

A useful record states the references, conditions, range, results and uncertainties. A certificate is evidence of a particular calibration, not a promise that the instrument is accurate forever. Choose references whose uncertainty is suitable for the intended measurement; comparing two uncharacterised instruments cannot establish which is correct.

### 中文锚点

厨房秤放上标着一百克的标准砝码，却显示九十五克，以后每次都加五克就行了吗？先别急，再换几个不同质量的砝码试试：它可能总少五克，也可能放得越多，偏得越多。校准就是拿可信的参考来比较，摸清仪器的读数究竟怎样对应实际量值、这个对应关系有多可靠。查清它怎么偏，和动手把它调准，是两件事；多称几遍，也不能自动把偏差称没。

## Why repetition alone cannot establish a correction

The central measurement lesson is the same point [[Accuracy vs Precision]] makes from the *diagnosis* side: random and systematic errors live on orthogonal axes. [[Repeated Measurements]] shows that averaging $N$ readings divides the random uncertainty by $\sqrt{N}$ but **leaves systematic error untouched**. The student who takes 100 readings with a balance whose zero is offset by 0.5 g will report a mean that is *very precisely* 0.5 g wrong.

Under independent, zero-mean noise of finite variance, averaging reduces random uncertainty approximately as $1/\sqrt N$. A shared bias survives that average. Reference measurements, a corrected physical model, reversal methods or redesign can reveal or reduce systematic effects; averaging the same biased setup cannot establish the correction by itself.

## The traceability chain

A school balance reading 0.01 g looks impressive. *In what sense* is it 0.01 g? In the sense that, at some point in the past, the balance was placed on a level surface and a small mass labelled "100.00 g" was placed on its pan, and the balance was either adjusted to read 100.00 g or its indication error at that load was recorded for correction. The 100.00 g calibration mass had been weighed by a more accurate scale at the manufacturer's plant. That scale had been checked against a working reference mass certified by a regional metrology lab. That regional reference traces, ultimately, back to **the international prototype kilogram (IPK)** in Sèvres — and now, since the **2019 SI redefinition** (see [[Physical Quantities and Units]] §"Beyond syllabus — the 2019 SI redefinition"), back to **Planck's constant** $h$, fixed by definition at exactly $6.62607015 \times 10^{-34}\,\mathrm{J\,s}$.

Every measurement, from school physics to particle physics, lives on a **traceability chain** that terminates at one of the seven SI base unit definitions. Break any link in the chain — a recalibration overdue, a reference mass dropped, a power supply mis-marked — and every measurement downstream silently inherits the break.

![[calibration-traceability-pyramid.svg]]

*The five-layer hierarchy. The top is rock: fundamental constants whose values are fixed by definition. The next layer down is the *realisation* of those definitions in physical apparatus (Kibble balances for the kilogram, optical clocks for the second, voltage references for the volt) maintained at national and international metrology labs — BIPM in Sèvres, NIST in Gaithersburg, NPL in Teddington, and a handful of others. Below that, accredited commercial labs (ISO 17025 / ILAC-MRA) issue calibration certificates traceable to the national lab. Below that, working standards in scientific and industrial labs. At the bottom: the instruments students actually use. **The whole chain is what makes "0.01 g" meaningful.**

The chain has two practical consequences students rarely see:

- **Even at the top, the standard has uncertainty.** Planck's constant is *defined* exactly, but its *physical realisation* by a Kibble balance has its own uncertainty — specified for the particular realisation. So the IPK had its drift; the post-2019 anchor has its measurement noise. There is no zero-uncertainty calibration; there is only the smallest *achievable* uncertainty given the current state of physics.
- **The chain is fragile in the way long chains are fragile.** Each link adds its own uncertainty, and the lab at the bottom inherits contributions that must be propagated, including correlations (see [[Error Propagation]] §"Rule 1 — sums and differences" for why uncertainties add in quadrature when independent). Display resolution alone does not determine the combined uncertainty of a school balance.

## Calibration in the school physics lab

The 9702 / IB / AP practical syllabi all expect students to perform routine calibration moves before recording measurements. The three that come up every exam season:

### Zero-error correction

The single most common calibration mistake at AS-level. **Always read the instrument with no load before applying it**, and either reset the zero or *record the offset and subtract it from every reading*. The instruments where this bites hardest:

- **Vernier callipers / micrometer screw gauge** — close the jaws fully and check the scale reads zero. If it reads $+0.04~\text{mm}$, every reading is $0.04~\text{mm}$ too high.
- **Top-pan balance** — press the *tare* button with the pan empty. Many balances drift over the day with temperature; re-zero before each set of weighings.
- **Voltmeter / ammeter** — with no current flowing, the needle should rest on zero. Mechanical meters often have a small adjustment screw under the dial.
- **Thermometer** — at 0 °C in an ice-water bath, a calibrated thermometer reads zero. Mercury thermometers can lose accuracy if shocked.

### Two-point calibration

A more demanding move that catches *gain* errors (the instrument reads correctly at zero but wrong at full scale). Apply two known references that span the working range and check both:

- **Vernier calipers / micrometer:** check at $0$ mm (closed jaws) and against a certified **gauge block** of known thickness, often $25.000$ mm or $50.000$ mm. If closed jaws read $+0.04$ mm and the $50.000$ mm gauge reads $50.06$ mm, both the zero AND the gain are off. Gauge blocks are the school-lab gold standard for length calibration — manufactured to traceable tolerance, often class-1 or class-2 with stated uncertainty.
- **Balance:** check at zero (no load) and at a certified $100.00~\text{g}$ mass. If the reading at the certified mass is $99.92~\text{g}$, the correction **at that load** is $+0.08~\text{g}$; do not apply it as a constant correction across the range without evidence.
- **Voltmeter:** check at $0~\text{V}$ (shorted leads) and at a known voltage reference (a calibrated standard cell or a dedicated voltage-reference chip such as the LM399 or LTZ1000, certified at the millivolt level).

> [!warning] Why "boiling water at 100 °C" is a tempting but unreliable reference
> Water boils when its saturation vapour pressure matches the surrounding pressure. At lower atmospheric pressure, it boils below 100 °C. Assigning 100 °C to an unmeasured local boiling point can build a systematic error into a thermometer's scale.
>
> A carefully prepared pure ice–water mixture near atmospheric pressure is a useful approximate 0 °C reference. Its realisation still depends on purity, preparation, immersion and heat exchange. Reference procedures and uncertainties matter.
>
> The triple point of water remains a valuable laboratory reference, but **273.16 K is no longer an exact SI definition of its thermodynamic temperature**: since 2019 the kelvin is defined through the fixed Boltzmann constant. A practical scale's assigned fixed-point value and a measured thermodynamic temperature are different concepts. [BIPM kelvin history](https://www.bipm.org/en/history-si/kelvin)

[[Temperature and Thermometry]] explains signal conversion, thermal equilibrium and response time.

### Recalibration intervals

**Calibrated does not mean calibrated forever.** Choose verification and recalibration intervals from instrument stability, use, environment, required uncertainty and reference-check history. There is no universal annual interval for every balance or thermometer. Check after damage, adjustment or suspicious drift; routine zero checks do not replace calibration across the working range.

## Worked example — calibrating a school balance

A student needs to find the density of a brass cylinder. They will weigh it on the lab's electronic balance (claimed precision $\pm 0.01~\text{g}$) and measure its dimensions with vernier callipers. Before any measurements:

**Step 1 — Zero check.** Pan empty, tare. Balance reads $0.00~\text{g}$. ✓
**Step 2 — Reference check.** Place a certified $100.000~\text{g}$ standard mass on the pan (the lab has one certified to $\pm 0.005~\text{g}$, calibration certificate on file). Balance reads $99.92~\text{g}$.

**Step 3 — diagnose the model before correcting.** Zero is right, but the 100.000 g reference reads 99.92 g. The discrepancy is −0.08 g **at that load**; it does not establish a constant offset for every load. If further reference points validate a pure gain model through zero, then

$$m_{\rm corrected}=m_{\rm indicated}\frac{100.000}{99.92}.$$

For an indicated 42.39 g this model gives 42.424 g before final rounding. A blanket +0.08 g would instead give 42.47 g and is unsupported by the evidence. A nonlinear response requires a different calibration function.

**Step 4 — report uncertainty honestly.** The quoted ±0.01 g specification and ±0.005 g certificate value cannot automatically be combined as if both were independent standard uncertainties. Establish what each means, include repeatability, resolution, calibration fit and relevant correlations, then propagate through the chosen model. Adjustment does not guarantee the same uncertainty as applying a correction; verify again afterward. [[Error Propagation]] supplies the mathematical framework.

> [!warning] The certified mass is not exact
> Its certificate has an uncertainty. That uncertainty contributes to the result alongside the instrument and method; successful calibration does not reduce every remaining error to zero.

## Following uncertainty through a measurement

A measurement requires several complementary decisions:

1. **[[Physical Quantities and Units]]** — every measurement is *number × unit*. The unit traces to a calibration standard. (The foundation.)
2. **[[Vectors in Physics]]** — for vector measurements, decompose along axes of the problem's geometry. (The foundation, vector-edition.)
3. **[[Accuracy vs Precision]]** — *diagnose* the uncertainty: random or systematic? They live on orthogonal axes.
4. **[[Error Propagation]]** — *track* uncertainty through downstream calculations using the variance-additivity machinery.
5. **[[Repeated Measurements]]** — *act on the random axis*: average $N$ readings, uncertainty in the mean shrinks as $\sigma/\sqrt{N}$.
6. **Calibration of Instruments** — *act on the systematic axis*: compare against a traceable reference, record the correction or adjust the instrument.
7. **[[Significant Figures]]** — *report* the final answer with the right precision: match the s.f. to the uncertainty.

The deep observation: independent standard-uncertainty contributions combine in quadrature; correlated contributions require covariance terms — and *both* can be driven down, but by different techniques. Random by averaging; systematic by calibration. *Once you've done as much as you can of each, what's left is the floor below which the present apparatus cannot dig*. That floor depends on the reference, instrument and measurement method together.

This is why metrology — the science of measurement itself — has been a thousand-year project. Every improvement in primary-standard calibration (Cavendish 1798 weighing the Earth, Michelson 1893 wavelength-of-light metre, the 1967 caesium-clock second, the 2019 SI redefinition pinning every base unit to a fixed fundamental constant) **moves the floor down** for every measurement that traces to it. Generations of progress are stored in your school balance reading $0.01~\text{g}$.

> [!info] Beyond syllabus — the 2019 SI redefinition as the universal calibration upgrade
> Recall from [[Physical Quantities and Units]] §"Beyond syllabus — the 2019 SI redefinition" that until **20 May 2019**, the kilogram traced back to a single physical artefact (the IPK in Sèvres) that was drifting against its sister copies. After 2019, the kilogram traces to a fixed value of Planck's constant, realisable anywhere with a Kibble balance and (in principle) without any artefact at all. The same applies to every SI base unit. **The traceability chain's top is now physical law, not metal.** Any well-equipped lab can realise the SI base units from physics without consulting Sèvres. This is the deepest calibration upgrade in two centuries — it replaces "trust this artefact" with "trust this constant of nature."

## Common Mistakes

### 1. "Averaging will fix it"

The single most persistent misconception, drilled in [[Accuracy vs Precision]] §3 "Averaging fixes everything" and again in [[Repeated Measurements]] §"The systematic-error trap." Averaging eats *random* noise; bias survives. Calibration can establish corrections; reversal, improved physical models and redesigned measurements can also reveal or reduce systematic effects. Repeating the same unchecked setup alone cannot.

### 2. "Calibrated once, calibrated forever"

Drift is real. Mechanical pivots flex; voltage references age; thermometers' fluid columns separate; balances pick up dust. A previous calibration is evidence for its stated conditions, not a guarantee against later drift. Use reference checks and a recalibration interval justified by stability, use and required uncertainty; recheck after adjustment or suspected damage.

### 3. "The certified mass is exact"

Every reference standard has its own uncertainty, stated on the calibration certificate. The reference uncertainty contributes to the final uncertainty through the measurement model; it must not be silently treated as zero. This bites in worked-example marking when students propagate the certified mass's uncertainty into their final result; many forget and report a final precision that the calibration chain can't deliver.

### 4. "Precise means accurate"

Hubble's mirror was *exquisitely precisely* polished to the *wrong shape*. Precision and accuracy are orthogonal (see [[Accuracy vs Precision]] §"The canonical dartboard analogy"). A student who *only* checks repeatability — "my readings all agree to 0.001 g!" — has not checked accuracy at all. The dartboard's most dangerous panel is *inaccurate but precise*: all the shots tightly grouped, none of them at the bullseye, and nothing in the readings themselves warning you of the offset. Only an independent reference can reveal it.

### 5. "Cross-checking is wasteful"

Hubble's institutional lesson. Perkin-Elmer had *two* additional null correctors that would have caught the 1.3 mm rod error if anyone had used them — but they were considered less precise and skipped to save time. **The most expensive lesson in modern optics: trust the most precise instrument, and verify with an independent less-precise one anyway.** When the cross-check disagrees with the primary, you have caught something. When it agrees, you have gained confidence at low cost. The independent check is *never* wasted; it is the only thing that catches the failure mode where the primary instrument is the source of the error.

## Exam Notes

### Cambridge 9702 — §1.3 and practical assessment

§1.3 names systematic errors (including zero errors), random errors and their effects. The practical-assessment guidance for Paper 5 explicitly includes obtaining calibration curves as a possible relevant procedural detail. Explain the reference, the comparison and the correction appropriate to the actual apparatus; naming “calibration” alone does not establish that the method works.

The syllabus does not award a universal mark for zeroing before every reading, nor a fixed mark for a memorised two-temperature sentence. Marks depend on the experiment and question. A boiling-water reference must account for pressure; simply assuming 100 °C is not generally valid.

### Cambridge 0625 — Papers 5 and 6, practical skills

The assessment guidance explicitly requires correcting for zero errors where required and identifying sources of measurement, random and systematic error. State a measured offset and apply the correct sign. Full traceability chains and certified-reference uncertainty budgets are enrichment, not separately named IGCSE outcomes. The bookkeeping map's P4/P6 labels denote practical-skill groups, not examination Paper 4/Paper 6.

### IB Physics — coursewide skills and scientific investigation

The current guide's **Tools 1: Experimental techniques** explicitly includes calibrating measuring apparatus, including sensors. Inquiry skills include considering random/systematic errors, limitations and realistic improvements. This is coursewide skills content, not invented “Theme A / PRAC.1 / PRAC.2” syllabus sections.

The scientific investigation is assessed through Research design, Data analysis, Conclusion and Evaluation. Appropriate consideration of uncertainties matters, but the rubric does not guarantee full marks for quoting a standard's uncertainty or automatically remove a band when that phrase is absent. Explain the uncertainty's actual significance to the investigation.

### AP Physics 1, 2, C: Mechanics and C: Electricity and Magnetism

The current CEDs use **Science Practice 3: Scientific Questioning and Argumentation** for experimental questions and evidence-based reasoning. “Experimental Design and Analysis” names an FRQ type, not Science Practice 3. A suitable reference/check can be part of a justified experimental method; there is no universal calibration sentence or automatic mark independent of the question.

### Boundary of these claims

Calibration is an experimental skill, not a separately examined mathematical theorem in Cambridge 0580/0606/9709/9231, IB mathematics or AP Calculus. Do not infer board-specific certification procedures or question frequencies from the metrology enrichment. Edexcel/AQA/OCR Physics placement is not mapped here; check the particular specification before attaching a paper or mark allocation.

## Connections

- **Prerequisite:** [[Accuracy vs Precision]] — defines the random-vs-systematic factorisation. Calibration checks the systematic part of the measurement; Repeated Measurements is the *technique that acts on the random axis*. Orthogonal, both required.
- **Prerequisite:** [[Physical Quantities and Units]] — every unit traces to a calibration standard. The 2019 SI redefinition discussion in that card's beyond-syllabus callout is the direct setup for the traceability chain section here.
- **Prerequisite:** [[Repeated Measurements]] — the companion technique. Closing one of the two uncertainty axes is necessary but not sufficient; the bay's value comes from doing both.
- **Prerequisite:** [[Upper and Lower Bounds]] — the mathematics-side card that first introduces "systematic errors require calibration" at IGCSE level.
- **Leads to:** [[Significant Figures]] — once the calibration uncertainty is known, the answer's reported significant figures must match it. A balance certified to $\pm 0.005~\text{g}$ cannot honestly report masses to four decimal places.
- **Leads to:** [[Error Propagation]] — the calibration uncertainty enters downstream calculations via the standard quadrature-addition rules.
- **Real-world anchor (Stories):** [[Stories/The 1919 Eclipse]] — Eddington's identification of the Sobral astrographic plates as systematically compromised (focus drift), and the decision to *exclude* rather than calibrate, is the canonical "what to do when calibration isn't possible" case study. *Calibrate if you can; exclude if you can't; never average bias.*

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\pm$ | `\pm` | Plus-or-minus for uncertainty |
| $\Delta$ | `\Delta` | Calibration correction or offset |
| $h$ | `h` | Planck's constant — kg-anchor since 2019 |
| $\Delta\nu_{\rm Cs}$ | `\Delta\nu_{\rm Cs}` | Caesium hyperfine frequency — second-anchor since 1967 |
| $c$ | `c` | Speed of light — metre-anchor since 1983 |
| °C | `{}^\circ\mathrm{C}` | Degrees Celsius |
