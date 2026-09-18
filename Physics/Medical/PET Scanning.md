---
chinese: 正电子发射断层成像 (zhèng diànzǐ fāshè duàncéng chéngxiàng)
prerequisites:
  - "[[Nuclear Physics]]"
  - "[[Wave-Particle Duality]]"
leads_to: []
teach_together:
  - "[[X-rays and CT]]"
tags:
  - subject/physics
  - domain/medical-physics
  - domain/nuclear-physics
  - level/A-Level
  - level/university
  - curriculum/Cambridge-9702
  - syllabus/9702-24-3
  - type/deep
  - type/derivation
  - misconception/pet-detects-positrons
  - misconception/coincidence-means-identical-arrival-times
  - misconception/one-pair-locates-a-point
  - misconception/tracer-uptake-means-cancer
---

# PET Scanning 正电子发射断层成像

> *Antimatter sounds like something a spaceship runs on. In a hospital, it helps answer a quieter question: **where did this molecule go?** Chemistry delivers a radioactive label; a positron meets an electron; two photons escape with the evidence. The scanner turns their arrivals into a map.*

## Definition

### Formal

**Positron emission tomography (PET)** reconstructs the spatial distribution of a positron-emitting radiotracer from detected pairs of annihilation gamma photons. A **tracer** is a substance introduced into a system to follow a process; a **radiotracer** contains radioactive nuclei whose emissions make it detectable.

The **radiopharmaceutical** is the complete substance used in the body, not just the isotope's name. The biological behaviour depends on its chemical form. Labelling two different molecules with the same radionuclide does not make them follow the same route.

### Intuitive — change where the signal starts

| Method | Where the signal starts | What the measurement mainly probes |
|---|---|---|
| [[Ultrasound]] | External transducer sends sound; echoes return | Acoustic boundaries and travel times |
| [[X-rays and CT]] | External X-ray tube; transmitted photons are detected | Attenuation along paths through anatomy |
| PET | Radioactive tracer inside the body | Distribution of the tracer and the process it follows |

PET makes the **source distribution** unknown. CT makes the **attenuation distribution** unknown. Both need reconstruction, but the measured quantities and physical models differ.

### 中文锚点

想知道一种物质在身体里去了哪里，可以给它带上一个能被探测到的“标记”。PET 用的示踪剂就是这个思路：它的化学性质决定它往哪儿走，放射性标记则让仪器有机会追踪它。体内发生的湮灭会发出一对近乎反向的光子，仪器汇集许多这样的信号，才逐渐算出示踪剂的分布。图上亮的地方表示摄取较多，但仅凭这一点还不能下诊断。它让我们看到的，是身体里某种活动留下的踪迹。

## Notation

| Symbol | Meaning | Unit / convention |
|---|---|---|
| $e^+,e^-$ | Positron, electron | Equal rest masses $m_e$; charges $+e,-e$ |
| $\gamma$ | Gamma photon | Energy $E=hf$; momentum magnitude $p=E/c$ |
| $A=\lambda N$ | Activity of $N$ radioactive nuclei | Bq = decays per second |
| $T_{1/2}$ | Physical half-life | Same time unit as $1/\lambda$ |
| LOR | Line of response joining a detector pair | A position constraint, not a visible track |
| $\Delta t=t_L-t_R$ | Difference in photon arrival times | Positive means L detects later |
| $x$ | Position along LOR relative to its midpoint | Positive towards R |

## Key Facts — follow the causal chain

### 1. Chemistry chooses the destination

A label alone does not “seek disease”. A suitable molecule participates in, binds to, or travels with the process being studied. The radionuclide makes that molecule's distribution measurable. The amount must provide enough detected events while avoiding unnecessary exposure and, for a tracer study, should not materially alter the process being observed.

**Fluorine-18 fluorodeoxyglucose (FDG)** is a familiar example: a radiolabelled glucose analogue whose uptake and retention provide information related to glucose metabolism. Its physical half-life is about 110 minutes ([IAEA radiopharmaceutical reference](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1344_web.pdf)). Metabolically active tissue can produce a strong signal; normal brain activity and inflammatory processes can also produce uptake. The molecule's behaviour, scan conditions and anatomical context matter. **The detector measures radiation; interpretation supplies the biological meaning.** [NIH overview](https://www.nibib.nih.gov/science-education/science-topics/nuclear-medicine), [EANM/SNMMI guideline](https://jnm.snmjournals.org/content/54/4/647).

### 2. The nucleus supplies a positron

In beta-plus decay, a proton in a suitable nucleus becomes a neutron:

$$p\longrightarrow n+e^++\nu_e.$$

This describes a nuclear transformation, not spontaneous decay of a free proton. For fluorine-18,

$${}^{18}_{9}\mathrm F\longrightarrow{}^{18}_{8}\mathrm O+{}^{0}_{+1}e+\nu_e.$$

**Check the conserved quantities:** nucleon number is $18=18+0$; charge is $9=8+1$. The electron neutrino carries away some energy and momentum. The positron is created during the decay; it was not an atomic electron with its sign reversed. [[Nuclear Physics]] develops the decay bookkeeping and continuous beta spectrum.

The positron travels a short, nonzero distance through tissue, losing energy through interactions. Therefore the eventual annihilation position is close to, but not identical to, the original nucleus's position. This **positron range** contributes to image blur.

### 3. Annihilation preserves energy and momentum

A slowed positron encounters an electron. The standard PET model is

$$e^++e^-\longrightarrow\gamma+\gamma.$$

Take the electron–positron pair as approximately at rest before annihilation. Its total initial energy is approximately $2m_ec^2$, and its total momentum approximately zero. After annihilation,

$$E_1+E_2=2m_ec^2,\qquad \mathbf p_1+\mathbf p_2=0.$$

Two vectors sum to zero only if they are equal in magnitude and opposite in direction. Since photons obey $p=E/c$, the photon energies must also be equal:

$$\boxed{E_1=E_2=m_ec^2\approx8.19\times10^{-14}\ \mathrm J=511\ \mathrm{keV}.}$$

**Why two?** A single photon has momentum $E/c\ne0$, so it cannot carry away the pair's energy while also leaving total momentum zero in an isolated two-particle annihilation. Two opposite photons can. “Energy is conserved” alone does not explain the directions; **momentum conservation** does.

The pair's total photon energy is $1.022\ \mathrm{MeV}$, not $511\ \mathrm{keV}$. The latter belongs to **each** photon. The neutrino and energy already deposited while the positron slowed are not extra energy that must all reappear in these two photons.

> [!info] The approximation has a boundary
> Recall that the opposite/equal conclusion assumed negligible initial total momentum. Real electron motion and residual positron motion produce slight non-collinearity and energy shifts. Annihilation in flight and multi-photon channels exist; the dominant near-rest two-photon channel supplies conventional PET's useful signal. The schematic is an idealisation, not a claim that every annihilation produces two perfectly opposite photons.

### 4. Detect photons, not positrons

Some gamma photons escape the body and interact in detector crystals around it. A **scintillator** converts deposited gamma energy into a burst of visible light; a photosensor converts that light into an electrical signal. Electronics estimate the detector position, deposited energy and arrival time.

Not every photon escapes, strikes a detector, deposits enough energy or passes the event-selection criteria. One positron decay therefore does **not** guarantee one recorded pair. Energy selection near the expected annihilation energy helps reject unwanted events, but cannot eliminate every scattered or accidental pair.

The source is inside; the measurable evidence reaches the outside. That is why penetrating gamma photons are useful here, while the charged positron's short tissue path is not what the external scanner directly images.

### 5. Coincidence identifies a line

Electronics group suitable detections arriving within a short **coincidence window** as a candidate pair. If both photons came from the same annihilation and neither changed direction, the annihilation lies on the line connecting their detection positions: the **line of response**.

![[pet-line-and-time.svg|750]]

**Coincident does not mean exactly simultaneous at the detectors.** The photons were produced together; one can have a shorter path. A finite window also accommodates timing uncertainty. Conversely, two unrelated photons can happen to arrive within that window: an accidental or **random coincidence**.

A line has many points. Detector positions alone cannot tell which point produced this pair. Nor do all pairs from a scan cross at a single point: the tracer occupies an extended distribution, so different events originate at different locations.

### 6. Arrival-time difference adds a position constraint

Put detector L at $-D/2$, detector R at $+D/2$, and an annihilation at position $x$ along their connecting line. Let its unknown emission time be $t_0$:

$$t_L=t_0+\frac{D/2+x}{c},\qquad t_R=t_0+\frac{D/2-x}{c}.$$

**Trigger: the emission time is unknown but shared → tool: subtract the equations.** The nuisance $t_0$ cancels:

$$\Delta t=t_L-t_R=\frac{2x}{c}\quad\Longrightarrow\quad\boxed{x=\frac{c\Delta t}{2}.}$$

The factor of two has a physical reason: moving towards R increases the left path by $x$ **and** decreases the right path by $x$. A path difference of $2x$ results.

For $\Delta t=+200\ \mathrm{ps}$, $x\approx+3.0\ \mathrm{cm}$: R records earlier, so the source is nearer R. If the time-difference uncertainty is $\delta(\Delta t)$, the corresponding positional uncertainty is

$$\delta x=\frac{c}{2}\,\delta(\Delta t).$$

Use like-for-like widths: a 400 ps **FWHM** (full width at half maximum) timing spread corresponds to approximately 6.0 cm FWHM along the line. It is not a 6.0 cm hard error bound, and it is not automatically the final reconstructed image resolution. Time-of-flight PET contributes a probability region along each line, which many events refine collectively. [Time-of-flight detector study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5526073/).

## From counts to an image

The scanner records many detector pairs and their timings. Reconstruction seeks a nonnegative spatial distribution whose predicted measurements agree with these data. A basic binned model is

$$y_i\sim\operatorname{Poisson}(\mu_i),\qquad\mu_i=\sum_j H_{ij}q_j+b_i.$$

- $q_j$ describes the source strength in voxel $j$ under the chosen units and scan duration.
- $H_{ij}$ describes how activity there contributes to measurement bin $i$: geometry, detection efficiency and, in realistic models, attenuation and other response effects.
- $b_i$ represents additional expected counts such as random/scattered contributions when modelled additively.
- $y_i$ is the actual integer count. Repeating the same scan conditions need not reproduce the same $y_i$.

A **voxel** is a three-dimensional image cell. A two-dimensional slice uses pixels. The data constrain their values jointly; reconstruction is not photographing the gamma rays or drawing all lines and choosing one common intersection.

![[pet-imaging.mp4]]

The animation first follows the photon pair, then separate events from different places. Its reconstruction uses a **synthetic 16×16 source**, 36 projection angles and 35 detector-offset bins: the same noisy dataset is fitted over 1, 5, 20 and 80 iterations. More iterations means more computation on the same counts, **not** more photons collected. The model idealises away tissue attenuation, scatter, random pairs, motion and positron range.

![[pet-reconstruction.svg|750]]

The true source is shown only because this is a simulation. A scanner does not possess that reference image. Agreement with synthetic truth checks an implementation under its assumptions; it does not validate clinical performance.

## Worked Examples — follow the information

### 1. Annihilation energy — original calculation

An electron and a positron annihilate with negligible total initial kinetic energy. Find each photon's energy and wavelength.

1. **Trigger: particle rest mass disappears → tool: energy conservation.** Total available energy is $2m_ec^2$.
2. **Trigger: zero initial total momentum, two photons → tool: momentum conservation.** They have equal energies and opposite momenta, so each carries $m_ec^2$.
3. **Tool: substitute constants.** With $m_e=9.11\times10^{-31}\ \mathrm{kg}$ and $c=3.00\times10^8\ \mathrm{m\,s^{-1}}$, $E=8.20\times10^{-14}\ \mathrm J\approx0.512\ \mathrm{MeV}$. More precise constants give the conventional 511 keV value.
4. **Trigger: photon energy to wavelength → tool: $E=hc/\lambda$.** Using $h=6.63\times10^{-34}\ \mathrm{J\,s}$ gives $\lambda\approx2.43\times10^{-12}\ \mathrm m$.

The small rounding difference is not another physical energy source. Keep sufficient working digits and follow the constants supplied in a question.

### 2. What actually reaches the scanner — real Cambridge question

**9702/44/O/N/25, Q8(a), Q8(d)(i–ii), pp.20–21; mark scheme p.16.** Paraphrased: explain a tracer, identify the detected particles, and explain how those particles form inside the body. [2 + 1 + 2 marks]

1. **Trigger: tracer definition → tool: identify both the label and destination.** A radioactive substance is introduced into the body and absorbed by the tissue under study. The scheme credits those two parts separately.
2. **Trigger: distinguish emitted beta particles from external detections → tool: follow the causal chain.** The detected particles are **gamma photons**.
3. **Trigger: explain their origin → tool: annihilation.** A positron encounters an electron in the body; annihilation converts the pair's mass–energy into photon energy. “The radioactive nucleus emits the two PET photons directly” skips the essential interaction.

### 3. Activity of a positron source — same real paper

**9702/44/O/N/25, Q8(c)(ii–iii), pp.20–21; mark scheme p.16.** Oxygen-15 has a half-life of 2.04 minutes. Calculate its decay constant, then the positron production rate for the stated $2.85\times10^{-6}\ \mathrm{kg}$ sample. [2 + 4 marks]

1. **Trigger: half-life to decay rate → tool: $\lambda=\ln2/T_{1/2}$.** Convert first: $T_{1/2}=122.4\ \mathrm s$, so $\lambda=5.66\times10^{-3}\ \mathrm{s^{-1}}$.
2. **Trigger: total isotope mass → tool: count nuclei.** With the supplied approximation $m_{\rm nucleus}=15u$ and $u=1.66\times10^{-27}\ \mathrm{kg}$,

$$N=\frac{2.85\times10^{-6}}{15(1.66\times10^{-27})}=1.14\times10^{20}.$$

3. **Trigger: independent nuclei each have decay rate $\lambda$ → tool: $A=\lambda N$.** The question's positron-decay model gives

$$\boxed{R_{e^+}=6.48\times10^{17}\ \mathrm{s^{-1}}.}$$

That is a **production rate**, not a detected coincidence rate. The supplied mass is an exam sample, not an injected-dose recommendation. For an isotope with positron branching fraction $f_+$ and effective pair-detection probability $\varepsilon$, the ideal true-pair rate would be $R_{\rm pair}=\varepsilon f_+A$ before additional counting losses.

### 4. Choosing a half-life — real Cambridge explanation

**9702/42/F/M/25, Q9(e)(ii), p.24; mark scheme p.13.** Explain the suitability of a tracer with a half-life of about two hours. [1 mark]

**Trigger: a process must be observed over time → tool: balance useful measurement against lingering activity.** The tracer must remain active long enough to carry out the investigation, while decaying sufficiently quickly afterwards to avoid unnecessary prolonged exposure. This is the scheme's two-sided explanation; “short half-life is safer” alone misses why it cannot be arbitrarily short.

Preparation, transport, uptake and acquisition all consume time. Different chemical tracers and biological processes therefore justify different radionuclides; two hours is not a universal PET specification.

## Where this is the working tool — chemistry with a location readout

PET can track molecular processes whose changes are not fully described by an anatomical outline. FDG studies glucose-related uptake; other tracers answer different questions, such as receptor binding or blood flow. A scan is therefore designed around **what the tracer follows**, not just around owning a machine that detects radiation.

In **PET/CT**, the CT image supplies anatomical context for the PET distribution and can also inform attenuation correction. The two measurements complement one another: a source map must be located in anatomy, and detected source intensity is affected by what photons pass through. They do not become the same measurement merely because the images are displayed together.

The real-world lesson reaches beyond medicine: **tag a process without substantially changing it, detect the tag, then infer the process from a model.** Radioactive tracers, fluorescent labels and packet identifiers use different physics but share that experimental logic.

## Try It — predict, run, change

Run `python3 pet-model.py` in the folder containing the companion. It requires NumPy and uses no patient data.

1. Before running, predict the sign of $t_L-t_R$ for a source nearer R. Then check the chord/timing calculation in the source.
2. Change the random seed while keeping the synthetic source fixed. The count data and recovered pixels change; the underlying source does not. Identify which differences are statistical.
3. Change `total=30000` to a smaller positive expected count and compare repeated seeds. Keep the colour scale fixed. Why can individually noisy maps still reflect the same source distribution?
4. Move the synthetic spots using `shift`, then reconstruct again. A reconstruction that only reproduces the original picture has learned an example, not implemented a method.

The built-in checks compare three grid sizes, translated sources and different count levels, verify geometric identities and nonnegative estimates, and check that the Poisson objective does not worsen during the implemented updates. None of those tests proves that omitted detector or tissue effects are negligible in a real scan.

## Common Misconceptions

- **“PET detects positrons.”** Trace the charged particle until annihilation, then follow the escaping gamma photons to the detector.
- **“Each photon has $2m_ec^2$.”** Write the total energy first, then divide between the equal-energy pair.
- **“Gamma photons must come directly from a nucleus.”** Gamma radiation also arises from particle–antiparticle annihilation. The PET pair is produced after the nuclear decay.
- **“The photons arrive simultaneously.”** They are emitted together. Unequal paths produce unequal arrival times; the window accepts plausible near-coincidences.
- **“One pair pins down the source.”** Detector positions give a line; finite timing accuracy gives a region along it. The source distribution requires many events.
- **“The bright pixel is cancer.”** Brightness reflects reconstructed tracer uptake under a model and display scale. Physiology, inflammation and other causes must be considered.
- **“Twice the activity means twice the measured count rate forever.”** Detection inefficiency, dead time and random coincidences break that simple extrapolation.

## Exam Notes

### Cambridge 9702 — §24.3, 2028–30 (same learning outcomes as 2025–27)

All six outcomes are relevant: tracer introduction/uptake; beta-plus emitter; annihilation with mass–energy and momentum conservation; the opposed gamma pair; calculation of photon energy; escaping photons and arrival-time processing to image tracer concentration. The equation $x=c\Delta t/2$ is derived here as a quantitative explanation of the last outcome; it is not separately named in the syllabus.

Keep the two conservation arguments distinct. Explain **equal/opposite directions from momentum**, and **the photon energy from total mass–energy**. The near-rest approximation matters if a question supplies significant incoming kinetic energy or a moving pair.

The real questions above show both quantitative radioactive-source work and qualitative imaging explanations. They do not establish guaranteed future mark allocations or question frequency. The photon/mass–energy relations can be combined from the physics principles; the TOF expression is derived, not assumed to be supplied.

### Cambridge 0625

Topic 5 supplies radioactive decay, half-life, uses and safety foundations, but the checked 2026–28 syllabus does not prescribe PET's beta-plus/annihilation/coincidence reconstruction chain. Use [[Nuclear Physics]] for the specified nuclear outcomes. This treatment is enrichment for IGCSE.

### IB Physics — first assessment 2025

The current guide includes radioactive-decay and mass–energy foundations under Theme E, but does not name PET scanning as a required technique. Legacy medical-physics options are not current syllabus requirements. PET is an application of the nuclear principles, not an additional completed IB row.

### AP Physics

AP Physics 2 Unit 15 includes rest-mass energy, positrons and beta-plus decay (§15.8), but does not prescribe PET image reconstruction. AP Physics 1 and both AP Physics C courses do not prescribe PET or the nuclear-imaging chain. Their conservation/measurement tools can transfer without making this an examined application.

**Not a named required PET topic:** Cambridge 0625, current IB Physics, AP Physics 1/2/C Mechanics/C E&M. Cambridge 9702 §24.3 is the direct syllabus home.

## Beyond Syllabus — the image is an inference

### Imperfect evidence: attenuation, scatter and random pairs

Recall that the line of response assumes two photons from one event travelling straight to their detectors. **Scatter** can change one photon's direction, assigning the event to the wrong line. **Random coincidences** pair unrelated detections. **Attenuation** removes photons from the usable pair population; detector dead time loses counts when signals arrive too closely together.

These effects alter the measurement model. More counts alone cannot fix a systematically wrong model. Positron range, slight photon non-collinearity, detector size, timing uncertainty and motion also limit localisation. CT-based attenuation correction must convert X-ray attenuation information to the appropriate gamma-photon energy; it is not simply pasting CT pixel values into a PET equation.

### Physical versus biological disappearance

Recall $A(t)=A_0e^{-\lambda t}$ for radioactive decay. A tracer can also leave a tissue biologically. If both removal processes are independent exponentials,

$$A_{\rm tissue}(t)\propto e^{-(\lambda_{\rm physical}+\lambda_{\rm biological})t},\qquad
\frac{1}{T_{\rm effective}}=\frac{1}{T_{\rm physical}}+\frac{1}{T_{\rm biological}}.$$

This is a model, not a universal uptake curve: blood delivery, trapping, exchange between compartments and metabolites can matter. Physical half-life is an isotope property; tissue retention depends on the molecule and biology. The observed curve need not be a single exponential.

### A reconstruction update you can inspect

Recall $\mu_i=\sum_jH_{ij}q_j$ in the simplified model with no additive background. For independent Poisson counts, maximising the log-likelihood means increasing

$$\ell(q)=\sum_i\left[y_i\ln\mu_i-\mu_i\right]+\text{constant}.$$

The companion uses a maximum-likelihood expectation-maximisation (MLEM) update ([Shepp and Vardi, 1982](https://pubmed.ncbi.nlm.nih.gov/18238264/))

$$q_j^{\rm new}=\frac{q_j}{\sum_iH_{ij}}\sum_iH_{ij}\frac{y_i}{\mu_i}.$$

The ratio $y_i/\mu_i$ says whether a bin was underpredicted or overpredicted. Weighting those ratios by $H_{ij}$ feeds the discrepancy back to contributing pixels; dividing by total sensitivity avoids favouring a pixel merely because more bins can see it. This motivates the update; its full likelihood-monotonicity proof belongs to the expectation-maximisation method.

The synthetic model normalises each system-matrix column to unit sensitivity, so $q_j$ represents expected detected counts contributed by that pixel across the dataset. It is not a calibrated Bq-per-volume image. Real quantitative PET requires calibration and corrections. More iterations can fit noise as well as structure; stopping rules and regularisation therefore matter.

## Connections

- **Builds on:** [[Nuclear Physics]] — beta-plus decay, mass–energy, activity and half-life; [[Wave-Particle Duality]] — photon energy and momentum.
- **Companion:** [[X-rays and CT]] — anatomical context and a contrasting inverse problem; [[Ultrasound]] — another route from travel times to an internal image.
- **Mathematical structure:** [[Linear Systems in 3D]] — measurements constrain unknowns; [[Poisson Distribution]] — random event counts; [[Exponential Growth and Decay]] — physical and biological removal rates.
- **Measurement:** [[Error Propagation]] — timing uncertainty mapped into position uncertainty.
- **Thinking:** [[Forward Reading and Problem Discovery]] — follow the carrier of information through every transformation.

## Sources and Further Reading

- [NIH/NIBIB — Nuclear Medicine](https://www.nibib.nih.gov/science-education/science-topics/nuclear-medicine): tracers, PET and complementary PET/CT use.
- [National Academies — Positron Emission Tomography](https://www.ncbi.nlm.nih.gov/books/NBK232475/): detector physics and reconstruction principles.
- [Monte Carlo simulations of time-of-flight PET](https://pmc.ncbi.nlm.nih.gov/articles/PMC5526073/): arrival-time resolution and corresponding localisation width.
- [EANM/SNMMI guideline on FDG in inflammation and infection](https://jnm.snmjournals.org/content/54/4/647): why uptake is not specific to malignancy.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $e^++e^-\to2\gamma$ | `e^++e^-\to2\gamma` | idealised two-photon annihilation |
| $m_ec^2$ | `m_ec^2` | one near-rest annihilation photon's energy |
| $x=c\Delta t/2$ | `x=c\Delta t/2` | signed TOF position along the detector line |
| $y_i\sim\operatorname{Poisson}(\mu_i)$ | `y_i\sim\operatorname{Poisson}(\mu_i)` | a count model, not an exact deterministic reading |
