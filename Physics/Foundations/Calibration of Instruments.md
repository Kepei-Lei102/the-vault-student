---
chinese: 仪器校准 (yíqì xiàozhǔn)
prerequisites:
  - "[[Accuracy vs Precision]]"
  - "[[Physical Quantities and Units]]"
  - "[[Repeated Measurements]]"
  - "[[Upper and Lower Bounds]]"
  - "[[The Pendulum Story]]"
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
  - syllabus/9702-1-3
  - syllabus/0625-P4
  - syllabus/0625-P6
  - syllabus/IB-Physics-PRAC-1
  - syllabus/AP-Physics-1-SP-3
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

How does that happen? Perkin-Elmer's main test instrument was a **reflective null corrector** — a device that produces an interference pattern showing where the mirror's actual curvature deviates from the designed parabolic shape. The null corrector contained a small metering rod whose length set the device's reference. During assembly in 1981, a technician had set the rod's position using a measuring tool that *was itself uncalibrated*: a tiny chip of anti-reflective coating on a lens had been mistaken for the actual lens edge, and the rod ended up positioned $1.3~\text{mm}$ wrong.

**Every subsequent measurement of the mirror's shape used a reference that was off by 1.3 mm.** The mirror was then polished, repeatedly and accurately, to match what the null corrector said was correct. The aberration was not introduced during polishing; the aberration was *defined* by the null corrector before polishing began. The mirror was a perfect realisation of an imperfect target.

Worse: Perkin-Elmer *had* two other null correctors, both of which would have caught the error if anyone had cross-checked. Those instruments were considered less precise and weren't used in the final verification. **The most precise instrument was trusted absolutely**, and its calibration error propagated downstream undetected. The mirror was launched in 1990 with the imprinted memory of a 1981 calibration failure.

The fix arrived three and a half years later. **December 1993, Servicing Mission 1**: astronauts installed COSTAR (the Corrective Optics Space Telescope Axial Replacement) — a set of compensating mirrors that effectively gave Hubble a pair of corrective glasses. The science programme finally began. Total cost of the calibration error: roughly $\$1.5$ billion in additional missions, hardware, and lost productivity.

The lesson is unforgiving and pedagogically permanent. **Calibration error is the one error you cannot detect by repeating the measurement**, because the instrument that does the repeating is the instrument with the error. The mirror was polished a thousand times against the same null corrector; every check said it was perfect; every check was based on the same lie. The fix had to come from *outside the chain* — a different instrument, a different test rig, a different observer. This card is about the protocols that prevent this.

## Definition

**Calibration** (仪器校准 yíqì xiàozhǔn) is the process of comparing an instrument's reading against a known reference value, called a *standard*, and either:

- (a) recording the discrepancy as a **correction** to apply to all future readings, *or*
- (b) physically **adjusting** the instrument until its reading matches the standard.

Both modes leave a *calibration certificate*: a written record stating the calibration date, the reference used, the discrepancy found, and the uncertainty in the standard itself.

The crucial constraint: **the standard must be more accurate than the instrument being calibrated**. Calibrating a kitchen scale against another kitchen scale is theatre. Calibration requires a *more trusted reference* — and that reference has, in turn, been calibrated against something even more trusted, and so on up the chain.

### 中文锚点

**仪器校准** (yíqì xiàozhǔn) = calibration of instruments. 测量界最严肃的一道工序，因为这是 **唯一能消除系统误差 (systematic error)** 的方法。重复测量 (Repeated Measurements) 消除随机误差，校准消除系统误差，两者正交，缺一不可。

| English | 中文 | 含义 |
|---|---|---|
| Calibration | 校准 / 标定 (xiàozhǔn / biāodìng) | 用已知标准检查或调整仪器 |
| Reference standard | 参考标准 (cānkǎo biāozhǔn) | 已知精确值的物体或信号 |
| Traceability | 可追溯性 (kě zhuīsù xìng) | 一条从仪器到基本常数的校准链 |
| Zero error | 零点误差 (língdiǎn wùchā) | 仪器在零状态时读数不为零 |
| Correction factor | 修正系数 (xiūzhèng xìshù) | 应用到所有后续读数上的偏差修正 |
| Drift | 漂移 (piāoyí) | 校准后仪器读数随时间逐渐偏离 |
| Recalibration interval | 校准周期 (xiàozhǔn zhōuqī) | 两次校准之间的时间间隔 |
| Primary standard | 基准 (jīzhǔn) | 国家级或国际级的最高参考标准 |

**核心原则**: 平均测量值 ($\bar X$) 之所以靠近真值，是因为 (1) 通过 [[Repeated Measurements]] 把随机误差 (random error) 通过 $\sigma/\sqrt{N}$ 压低 + (2) 通过校准把系统误差 (systematic error) 找出来并扣除。两个机制相互独立，无法互相替代。

## Why calibration is the *only* fix for systematic error

This card's load-bearing message is the same point [[Accuracy vs Precision]] makes from the *diagnosis* side: random and systematic errors live on orthogonal axes. The [[Repeated Measurements]] card showed that averaging $N$ readings divides the random uncertainty by $\sqrt{N}$ but **leaves systematic error untouched**. The student who takes 100 readings with a balance whose zero is offset by 0.5 g will report a mean that is *very precisely* 0.5 g wrong.

The reason is structural, not procedural. Random errors are zero-mean noise; their average tends to zero as $N$ grows because the central limit theorem says so (see [[Normal Distribution]] §"Central Limit Theorem (the why)" for the statement). Systematic errors are *non-zero-mean*; their average tends to the bias itself, not to zero. **There is no statistical operation that can move a bias to zero, because zero is not where the bias lives.** Bias has to be *found* — by comparison against an independent reference — and then either subtracted from future readings or eliminated at the source.

That is what calibration does. It introduces a measurement made with a *more trusted* instrument (the standard) and uses the discrepancy as the estimate of the bias. The bias then *becomes a known correction*, applied to all subsequent readings, and the instrument's *accuracy* improves to the standard's accuracy. (Its *precision* — the spread of its random noise — is unchanged.)

This is the third leg of the measurement stool. Repeated Measurements crushes random uncertainty; calibration crushes systematic uncertainty; together, they bring the *total* uncertainty in a measurement down to the level of *the calibration uncertainty itself* — the **systematic floor**, below which neither technique can dig further.

## The traceability chain

A school balance reading 0.01 g looks impressive. *In what sense* is it 0.01 g? In the sense that, at some point in the past, the balance was placed on a level surface and a small mass labelled "100.00 g" was placed on its pan, and the balance was either adjusted to read 100.00 g or its 0.08 g offset was recorded for future correction. The 100.00 g calibration mass had been weighed by a more accurate scale at the manufacturer's plant. That scale had been checked against a working reference mass certified by a regional metrology lab. That regional reference traces, ultimately, back to **the international prototype kilogram (IPK)** in Sèvres — and now, since the **2019 SI redefinition** (see [[Physical Quantities and Units]] §"Beyond syllabus — the 2019 SI redefinition"), back to **Planck's constant** $h$, fixed by definition at exactly $6.62607015 \times 10^{-34}~\text{J·s}$.

Every measurement, from school physics to particle physics, lives on a **traceability chain** that terminates at one of the seven SI base unit definitions. Break any link in the chain — a recalibration overdue, a reference mass dropped, a power supply mis-marked — and every measurement downstream silently inherits the break.

![[calibration-traceability-pyramid.svg]]

*The five-layer hierarchy. The top is rock: fundamental constants whose values are fixed by definition. The next layer down is the *realisation* of those definitions in physical apparatus (Kibble balances for the kilogram, optical clocks for the second, voltage references for the volt) maintained at national and international metrology labs — BIPM in Sèvres, NIST in Gaithersburg, NPL in Teddington, and a handful of others. Below that, accredited commercial labs (ISO 17025 / ILAC-MRA) issue calibration certificates traceable to the national lab. Below that, working standards in scientific and industrial labs. At the bottom: the instruments students actually use. **The whole chain is what makes "0.01 g" meaningful.**

The chain has two practical consequences students rarely see:

- **Even at the top, the standard has uncertainty.** Planck's constant is *defined* exactly, but its *physical realisation* by a Kibble balance has its own uncertainty — currently a few parts in $10^8$. So the IPK had its drift; the post-2019 anchor has its measurement noise. There is no zero-uncertainty calibration; there is only the smallest *achievable* uncertainty given the current state of physics.
- **The chain is fragile in the way long chains are fragile.** Each link adds its own uncertainty, and the lab at the bottom inherits all of them in quadrature (see [[Error Propagation]] §"Rule 1 — sums and differences" for why uncertainties add in quadrature when independent). A school balance reading 0.01 g typically has total uncertainty around 0.05 g once you walk back up the chain — because every transfer between labs added its bit.

## Calibration in the school physics lab

The 9702 / IB / AP practical syllabi all expect students to perform routine calibration moves before recording measurements. The three that come up every exam season:

### Zero-error correction

The single most common calibration mistake at AS-level. **Always read the instrument with no load before applying it**, and either reset the zero or *record the offset and subtract it from every reading*. The instruments where this bites hardest:

- **Vernier callipers / micrometer screw gauge** — close the jaws fully and check the scale reads zero. If it reads $+0.04~\text{mm}$, every reading is $0.04~\text{mm}$ too high.
- **Top-pan balance** — press the *tare* button with the pan empty. Many balances drift over the day with temperature; re-zero before each set of weighings.
- **Voltmeter / ammeter** — with no current flowing, the needle should rest on zero. Mechanical meters often have a small adjustment screw under the dial.
- **Thermometer** — at $0\,^{\circ}\text{C}$ in an ice-water bath, a calibrated thermometer reads zero. Mercury thermometers can lose accuracy if shocked.

### Two-point calibration

A more demanding move that catches *gain* errors (the instrument reads correctly at zero but wrong at full scale). Apply two known references that span the working range and check both:

- **Vernier calipers / micrometer:** check at $0$ mm (closed jaws) and against a certified **gauge block** of known thickness, often $25.000$ mm or $50.000$ mm. If closed jaws read $+0.04$ mm and the $50.000$ mm gauge reads $50.06$ mm, both the zero AND the gain are off. Gauge blocks are the school-lab gold standard for length calibration — manufactured to traceable tolerance, often class-1 or class-2 with stated uncertainty.
- **Balance:** check at zero (no load) and at a certified $100.00~\text{g}$ mass. If the reading at the certified mass is $99.92~\text{g}$, the correction is $+0.08~\text{g}$.
- **Voltmeter:** check at $0~\text{V}$ (shorted leads) and at a known voltage reference (a calibrated standard cell or a dedicated voltage-reference chip such as the LM399 or LTZ1000, certified at the millivolt level).

> [!warning] Why "boiling water at $100\,^{\circ}\text{C}$" is a tempting but unreliable reference
> Every textbook in the world suggests calibrating a thermometer at the boiling point of water. It *sounds* perfect: water boils at $100\,^{\circ}\text{C}$, you have a kettle, done. Try it in **Lhasa, Tibet** (altitude 3656 m, atmospheric pressure ≈ 64 kPa): water boils at $87\,^{\circ}\text{C}$. In **Denver, Colorado** (1600 m): $95\,^{\circ}\text{C}$. On **Everest summit** (8848 m, ≈ 31 kPa): $71\,^{\circ}\text{C}$. The boiling point of water depends on atmospheric pressure via the Clausius-Clapeyron relation $\mathrm{d}T/\mathrm{d}P \approx +28~\text{K/atm}$ near $100\,^{\circ}\text{C}$ — so a $50\%$ drop in pressure shifts the boil by $\sim 14\,^{\circ}\text{C}$. A Lhasa student who "calibrates" their thermometer against boiling water is calibrating it to *the wrong number*, and every subsequent measurement carries the offset.
>
> The freezing point of water is more forgiving — the solid-liquid transition has $\mathrm{d}T/\mathrm{d}P \approx -7.5~\text{mK/atm}$ (negative because ice expands when it freezes, a quirk we get to thank for floating icebergs), so altitude shifts the ice-water $0\,^{\circ}\text{C}$ point by mK at most. Ice-water is a robust zero reference; boiling water is *not* a robust $100\,^{\circ}\text{C}$ reference.
>
> **The meta-lesson is the entire point of this card.** Your calibration reference *itself* can have a hidden systematic error. If you don't know what physics governs your reference's uncertainty, you cannot bound your own measurement's accuracy. The honest fixed points for high-altitude thermometer calibration are the **triple point of water** ($273.16~\text{K}$, exact by definition, pressure-independent because it's a thermodynamic invariant) realised in a sealed cell, or a **NIST-traceable certified PRT** (platinum resistance thermometer). The textbook ice-and-boiling-water recipe assumes sea-level atmospheric pressure and is a great example of a hidden assumption that *only fails for some users*.

### Recalibration intervals

**Calibrated does not mean calibrated forever.** Every instrument drifts. Common rough intervals:

| Instrument | Typical recalibration interval |
|---|---|
| School analytical balance | Re-zero every use; full re-cal annually |
| Industrial thermometer | 6 months for safety-critical; 1 year otherwise |
| Multimeter | 1 year for precision work; 2-5 years for utility use |
| Surveyor's distance equipment | Annual against a baseline range |
| NIST primary standards | Continuous monitoring; cross-comparison every few months |

The drift mechanism depends on the instrument: thermal expansion of reference springs, ageing of voltage references, hysteresis in mechanical pivots, accumulation of contaminants on electrode surfaces. For school labs the practical rule is: *re-zero before each session; treat last year's calibration certificate as approximate; if the result looks wrong, suspect drift before suspecting your physics*.

## Worked example — calibrating a school balance

A student needs to find the density of a brass cylinder. They will weigh it on the lab's electronic balance (claimed precision $\pm 0.01~\text{g}$) and measure its dimensions with vernier callipers. Before any measurements:

**Step 1 — Zero check.** Pan empty, tare. Balance reads $0.00~\text{g}$. ✓
**Step 2 — Reference check.** Place a certified $100.000~\text{g}$ standard mass on the pan (the lab has one certified to $\pm 0.005~\text{g}$, calibration certificate on file). Balance reads $99.92~\text{g}$.

The balance shows a systematic offset of $-0.08~\text{g}$. The student now has a choice. Either:

- *Mode (a):* record the correction as $+0.08~\text{g}$, apply it to every brass measurement and report results with a *corrected* mass. The balance's working accuracy is now $\pm 0.01~\text{g}$ (random, from precision) + $\pm 0.005~\text{g}$ (systematic, from the calibration certificate) $= \pm 0.012~\text{g}$ in quadrature.
- *Mode (b):* adjust the balance's internal calibration (most digital balances have a CAL function that walks the user through this). After adjustment, the balance reads $100.00~\text{g}$ and the offset is zero. Working accuracy is $\pm 0.01~\text{g}$ random plus $\pm 0.005~\text{g}$ residual systematic.

**Both modes give the same total uncertainty.** Mode (a) is preferred in school labs where adjusting the instrument requires teacher authority; Mode (b) is preferred in research labs where adjustments are routine. Either way, the calibration certificate stays in a binder near the balance.

The student then weighs the brass cylinder and reports, say, $42.39 \pm 0.012~\text{g}$ (Mode (a), corrected) — with the certified mass's uncertainty propagating into the final density result via the rules in [[Error Propagation]].

> [!warning] The certified mass is not exact either
> A common student error is to treat the certified $100.000~\text{g}$ standard mass as if it were exactly $100.000~\text{g}$ with zero uncertainty. **It isn't.** The calibration certificate quotes an uncertainty (here, $\pm 0.005~\text{g}$) — and that uncertainty enters every measurement performed with the calibrated balance. The systematic floor is *the calibration mass's uncertainty*, not zero. You cannot measure with more accuracy than your most trusted reference.

## Where the systematic floor lives — the bay's synthesis

The Foundations bay is now complete. Together its seven cards lay out a coherent decision tree for handling uncertainty:

1. **[[Physical Quantities and Units]]** — every measurement is *number × unit*. The unit traces to a calibration standard. (The foundation.)
2. **[[Vectors in Physics]]** — for vector measurements, decompose along axes of the problem's geometry. (The foundation, vector-edition.)
3. **[[Accuracy vs Precision]]** — *diagnose* the uncertainty: random or systematic? They live on orthogonal axes.
4. **[[Error Propagation]]** — *track* uncertainty through downstream calculations using the variance-additivity machinery.
5. **[[Repeated Measurements]]** — *act on the random axis*: average $N$ readings, uncertainty in the mean shrinks as $\sigma/\sqrt{N}$.
6. **Calibration of Instruments** (this card) — *act on the systematic axis*: compare against a traceable reference, record the correction or adjust the instrument.
7. **[[Significant Figures]]** — *report* the final answer with the right precision: match the s.f. to the uncertainty.

The deep observation: the total uncertainty in any reported measurement is the **quadrature combination of the surviving random and systematic uncertainties** — and *both* can be driven down, but by different techniques. Random by averaging; systematic by calibration. *Once you've done as much as you can of each, what's left is the floor below which the present apparatus cannot dig*. That floor is set by the calibration uncertainty of the reference standard you used.

This is why metrology — the science of measurement itself — has been a thousand-year project. Every improvement in primary-standard calibration (Cavendish 1798 weighing the Earth, Michelson 1893 wavelength-of-light metre, the 1967 caesium-clock second, the 2019 SI redefinition pinning every base unit to a fixed fundamental constant) **moves the floor down** for every measurement that traces to it. Generations of progress are stored in your school balance reading $0.01~\text{g}$.

> [!info] Beyond syllabus — the 2019 SI redefinition as the universal calibration upgrade
> Recall from [[Physical Quantities and Units]] §"Beyond syllabus — the 2019 SI redefinition" that until **20 May 2019**, the kilogram traced back to a single physical artefact (the IPK in Sèvres) that was drifting against its sister copies. After 2019, the kilogram traces to a fixed value of Planck's constant, realisable anywhere with a Kibble balance and (in principle) without any artefact at all. The same applies to every SI base unit. **The traceability chain's top is now physical law, not metal.** Any well-equipped lab can realise the SI base units from physics without consulting Sèvres. This is the deepest calibration upgrade in two centuries — it replaces "trust this artefact" with "trust this constant of nature."

## Common Mistakes

### 1. "Averaging will fix it"

The single most persistent misconception, drilled in [[Accuracy vs Precision]] §3 "Averaging fixes everything" and again in [[Repeated Measurements]] §"The systematic-error trap." Averaging eats *random* noise; bias survives. Calibration is the only mechanism that targets the systematic axis. If you can't calibrate, you can't fix it.

### 2. "Calibrated once, calibrated forever"

Drift is real. Mechanical pivots flex; voltage references age; thermometers' fluid columns separate; balances pick up dust. **Every instrument's calibration is good for a stated interval, after which it must be repeated.** A school lab that never recalibrates its balances is silently accumulating offsets across the year. Re-zero every session; full recalibration on the lab's annual schedule.

### 3. "The certified mass is exact"

Every reference standard has its own uncertainty, stated on the calibration certificate. **You cannot measure with more accuracy than your most trusted reference.** The systematic floor is the certified-mass uncertainty, not zero. This bites in worked-example marking when students propagate the certified mass's uncertainty into their final result; many forget and report a final precision that the calibration chain can't deliver.

### 4. "Precise means accurate"

Hubble's mirror was *exquisitely precisely* polished to the *wrong shape*. Precision and accuracy are orthogonal (see [[Accuracy vs Precision]] §"The canonical dartboard analogy"). A student who *only* checks repeatability — "my readings all agree to 0.001 g!" — has not checked accuracy at all. The dartboard's most dangerous panel is *inaccurate but precise*: all the shots tightly grouped, none of them at the bullseye, and nothing in the readings themselves warning you of the offset. Only an independent reference can reveal it.

### 5. "Cross-checking is wasteful"

Hubble's institutional lesson. Perkin-Elmer had *two* additional null correctors that would have caught the 1.3 mm rod error if anyone had used them — but they were considered less precise and skipped to save time. **The most expensive lesson in modern optics: trust the most precise instrument, and verify with an independent less-precise one anyway.** When the cross-check disagrees with the primary, you have caught something. When it agrees, you have gained confidence at low cost. The independent check is *never* wasted; it is the only thing that catches the failure mode where the primary instrument is the source of the error.

## Exam Notes

### Cambridge 9702 (AS Level)

**Syllabus ref:** 1.3 — uncertainty types (random / systematic), *zero error* explicitly called out as a systematic-error example to identify and correct.

What 9702 expects:
- **Paper 3 (Practical):** Routine zero-checks before every recorded measurement. Marks are awarded for the *act* of zeroing or stating the offset, not just for using the corrected value.
- **Paper 5 (PAE):** Design questions reward candidates who include "calibrate the instrument using a known reference" in their procedure. *"To minimise systematic error, the thermometer is calibrated at $0\,^{\circ}\text{C}$ and $100\,^{\circ}\text{C}$ using ice-water and boiling water"* is a one-mark answer to a P5 procedure question.
- **Common trap:** a question lists three sources of error and asks the candidate to classify each as random or systematic and propose a correction. *Random → repeat and average; Systematic → calibrate or replace the apparatus.* Getting the classification right is the gateway to the marks; offering "average more readings" for a systematic error is a guaranteed miss.

### Cambridge 0625 (IGCSE Physics)

This is **practical-paper** material — Paper 5 or Paper 6 — not one of the six numbered topics, and it is there in the syllabus's own words: *correct for zero errors where required*. The expectation is exactly that and no more — check the instrument reads zero before use; if it does not, subtract the offset from every reading. Zero error is also the cleanest example of a **systematic** error, the category the practical papers ask candidates to name and distinguish from random error. The full traceability discussion is not tested here; that lands at AS.

### IB Physics

**Theme A / PRAC.1** — apparatus selection includes calibration check; **PRAC.2** — systematic vs random errors. The Internal Assessment (20% of total grade) rewards an explicit calibration step in the procedure, including a statement of the reference's certified uncertainty. IB markschemes are explicit that a candidate who calibrates *and quotes the reference's uncertainty* earns full marks; one who calibrates without quoting the reference uncertainty loses one band.

### AP Physics 1 & 2

Science Practice 3 (Experimental Design and Analysis) — FRQ 3 frequently includes "describe how you would check your instrument is reading correctly" as an implicit requirement. The College Board's mark schemes accept "use a known standard, e.g. a certified mass / a known voltage reference" as the procedural answer.

### A-Level (other boards)

Edexcel, AQA, OCR all expect zero-error correction and traceable-reference calibration at the practical-coursework level. The 9702 framework is the gold standard; the others converge on the same content with notation variations.

## Connections

- **Prerequisite:** [[Accuracy vs Precision]] — defines the random-vs-systematic factorisation. This card is the *technique that acts on the systematic axis*; Repeated Measurements is the *technique that acts on the random axis*. Orthogonal, both required.
- **Prerequisite:** [[Physical Quantities and Units]] — every unit traces to a calibration standard. The 2019 SI redefinition discussion in that card's beyond-syllabus callout is the direct setup for the traceability chain section here.
- **Prerequisite:** [[Repeated Measurements]] — the companion technique. Closing one of the two uncertainty axes is necessary but not sufficient; the bay's value comes from doing both.
- **Prerequisite:** [[Upper and Lower Bounds]] — the mathematics-side card that first introduces "systematic errors require calibration" at IGCSE level.
- **Leads to:** [[Significant Figures]] — once the calibration uncertainty is known, the answer's reported significant figures must match it. A balance certified to $\pm 0.005~\text{g}$ cannot honestly report masses to four decimal places.
- **Leads to:** [[Error Propagation]] — the calibration uncertainty enters downstream calculations via the standard quadrature-addition rules.
- **Real-world anchor (Stories):** [[Stories/The 1919 Eclipse]] — Eddington's identification of the Sobral astrographic plates as systematically compromised (focus drift), and the decision to *exclude* rather than calibrate, is the canonical "what to do when calibration isn't possible" case study. *Calibrate if you can; exclude if you can't; never average bias.*
- **Bay closure:** With this card, **Physics/Foundations is complete at 7/7 deep cards** — the full measurement-foundations curriculum for AS Physics, IB Physics PRAC.1+PRAC.2, and AP Physics 1+2 Lab Requirement.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\pm$ | `\pm` | Plus-or-minus for uncertainty |
| $\Delta$ | `\Delta` | Calibration correction or offset |
| $h$ | `h` | Planck's constant — kg-anchor since 2019 |
| $\Delta\nu_{\rm Cs}$ | `\Delta\nu_{\rm Cs}` | Caesium hyperfine frequency — second-anchor since 1967 |
| $c$ | `c` | Speed of light — metre-anchor since 1983 |
| $\,^{\circ}\text{C}$ | `\,^{\circ}\text{C}` | Degrees Celsius (note the thin space) |
