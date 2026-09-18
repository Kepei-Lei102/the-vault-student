---
chinese: 核物理 (hé wùlǐ)
prerequisites:
  - "[[Wave-Particle Duality]]"
  - "[[Energy Levels and Line Spectra]]"
  - "[[Exponential Growth and Decay]]"
leads_to:
  - "[[PET Scanning]]"
  - "[[Quantum Tunnelling]]"
  - "[[Particle Physics]]"
  - "[[Energy Resources]]"
tags:
  - subject/physics
  - domain/nuclear-physics
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/0625-5-1
  - syllabus/0625-5-2
  - syllabus/9702-11-1
  - syllabus/9702-11-2
  - syllabus/9702-23-1
  - syllabus/9702-23-2
  - syllabus/IB-Physics-E-1-1
  - syllabus/IB-Physics-E-1-3
  - syllabus/IB-Physics-E-3-1
  - syllabus/IB-Physics-E-3-2
  - syllabus/IB-Physics-E-3-3
  - syllabus/IB-Physics-E-3-4
  - syllabus/IB-Physics-E-4-1
  - syllabus/IB-Physics-E-4-2
  - syllabus/IB-Physics-E-5-1
  - syllabus/AP-Physics-2-15-7
  - syllabus/AP-Physics-2-15-8
  - type/deep
  - misconception/half-life-is-an-expiry-date
  - misconception/breaking-bonds-releases-energy
  - misconception/count-rate-equals-activity
---

# Nuclear Physics 核物理

> An ionisation smoke alarm keeps watch by letting atoms fall apart. A hospital can follow a substance through a body because its nuclei announce where they are. The Sun shines because the nuclei it makes have less rest mass than the particles it started with. Nuclear physics is already in the house, the hospital and the daylight.

## Definition

### Formal

**Nuclear physics** studies atomic nuclei: their composition, interactions, energy states and transformations. A nucleus contains protons and neutrons, collectively **nucleons**. **Radioactive decay** is a spontaneous transformation of an unstable nucleus; a **nuclear reaction** can also be induced by an incoming particle. Both obey conservation of electric charge, energy and momentum; ordinary nuclear reactions also conserve total nucleon number.

### Intuitive

Two questions organise the subject: **what can the nucleus become, and how much energy can it give up on the way?** Conservation laws constrain the possible changes. Nuclear forces and quantum mechanics determine which changes occur and how quickly. The uncertainty of a single decay does not prevent precise predictions for a large population.

### 中文锚点

有一种烟雾报警器，里面竟藏着少量放射性物质。它衰变时放出的粒子让空气中有了能移动的电荷，形成微弱电流；烟雾进入后干扰这股电流，报警器就能察觉。奇妙的是，我们说不准某一个原子核何时衰变，但大量原子核的整体表现却有稳定的规律。核物理离生活并不远：一个个无法预报的小事件，合在一起，竟能帮我们可靠地发现烟雾。

## Notation — count the right thing

| Symbol / particle | Meaning | Charge / mass |
|---|---|---|
| ${}^{A}_{Z}X$ | Element $X$, proton number $Z$, nucleon number $A$ | Nucleus has charge $+Ze$; neutron number $A-Z$ |
| Proton $p$ / neutron $n$ | Two kinds of nucleon | $+e$ / zero; each has mass approximately $1\,\mathrm u$ |
| Electron $e^-$ / positron $e^+$ | A particle and its antiparticle | $-e$ / $+e$; equal masses, about $1/1836$ of a proton |
| $N(t)$ | Number of undecayed parent nuclei | A count; do not confuse it with $A-Z$ |
| $\mathcal A$ / $C$ | Activity / detected count rate | Bq = decays s$^{-1}$ / counts s$^{-1}$ |
| $\lambda$ / $T_{1/2}$ | Decay constant / half-life | Reciprocal time / time, using matching units |
| $B$ / $B/A$ / $Q$ | Binding energy / binding energy per nucleon / reaction energy release | Usually J or MeV |
| $\mathrm u$ / MeV | Unified atomic mass unit / energy unit | $1\,\mathrm u\approx1.66054\times10^{-27}$ kg; $1$ MeV $\approx1.60218\times10^{-13}$ J |

One unified atomic mass unit is one twelfth of the mass of a neutral carbon-12 atom in its ground state. Thus $1\,\mathrm u\,c^2\approx931.5$ MeV. **MeV is energy; MeV/$c^2$ is mass.** The activity symbol $\mathcal A$ avoids confusing activity with nucleon number $A$.

## From the atom to the nucleus

### The foil that answered back

Geiger and Marsden, working with Rutherford, directed alpha particles at a thin metal foil. A fluorescent screen registered arrivals. Most passed almost straight through; some deflected; a very small fraction turned through very large angles, even backwards.

| Observation | Inference — and why |
|---|---|
| Most pass through with little deflection | The region producing large deflections occupies only a tiny part of the atom |
| Some positively charged alpha particles deflect | Electric repulsion reveals concentrated positive charge |
| A few turn back | A small, massive centre can exert a large force; light electrons cannot reverse such massive projectiles |

The atom is mostly space around a tiny nucleus containing almost all its mass. Its radius is of order $10^{-10}$ m, versus roughly $10^{-15}$–$10^{-14}$ m for nuclei. Electrons occupy quantum states around it; the planetary-orbit picture is only a simple model. A neutral atom has $Z$ electrons. Losing electrons makes a positive **ion**; gaining electrons makes a negative ion. Neither changes the element. **Isotopes** share $Z$ but have different neutron numbers: carbon-12 and carbon-14 both have six protons, but six and eight neutrons respectively.

### How close did the projectile get? — IB HL extension

**Trigger: a head-on approach slows a positive alpha particle to a momentary stop. Tool: conservation of energy.** Treat a heavy target nucleus as stationary and both charges as point charges while they remain separated. Starting far away with kinetic energy $K$,

$$K=\frac{1}{4\pi\varepsilon_0}\frac{(2e)(Ze)}{r_{\min}}\quad\Longrightarrow\quad r_{\min}=\frac{2kZe^2}{K},\qquad k=\frac{1}{4\pi\varepsilon_0}.$$

The lost kinetic energy becomes electric potential energy. For a 5.0 MeV alpha particle approaching gold ($Z=79$), $r_{\min}\approx4.6\times10^{-14}$ m. This is a **closest-approach distance**, not a measured nuclear radius. If the scattering remains purely Coulomb-like down to this distance, it places an upper bound on the size probed. At higher energies, finite nuclear size and short-range nuclear interactions cause departures from the point-charge Rutherford prediction.

Measured radii approximately obey $R=R_0A^{1/3}$, with $R_0\approx1.2$ fm and $1$ fm $=10^{-15}$ m. Why a cube root? Nuclear volume is roughly proportional to the number of nucleons. Indeed,

$$\rho\approx\frac{A m_{\rm nucleon}}{\tfrac43\pi R_0^3 A}=\frac{3m_{\rm nucleon}}{4\pi R_0^3}\approx2.3\times10^{17}\ \mathrm{kg\,m^{-3}}.$$

The $A$ cancels: nuclei have approximately the same density. Doubling $A$ multiplies the radius by $2^{1/3}$, not by two.

## Why nuclei hold together — and why some do not

Protons repel electrically. Gravity between nucleons is far too weak to hold a nucleus together, yet stable nuclei exist: there must be another interaction. The **strong nuclear force between nucleons** is attractive over distances of order a femtometre, much stronger there than electric repulsion, and approximately independent of whether the nucleons are protons or neutrons. It becomes strongly repulsive at very small separations. Its short range means each nucleon binds mainly to near neighbours; adding a nucleon does not bind it equally to every nucleon already present.

Electric repulsion, however, reaches across the whole nucleus. As $Z$ grows, stable nuclei generally need progressively more neutrons than protons: neutrons contribute nuclear attraction without adding electric repulsion. Light stable nuclei tend to have neutron-to-proton ratios near one; heavy stable nuclei have ratios above one. **Too many neutrons can also make a nucleus unstable.** Stability depends on the whole quantum state, not a rule that “more neutrons is always better”.

A nucleus can move to a lower-energy arrangement by emitting particles or photons. An energetically possible change need not happen promptly: quantum barriers can make the lifetime enormous. Binding energy measures resistance to complete separation; half-life measures the rate of a particular allowed decay. They are different questions.

## What leaves the nucleus?

### Four transformations, with the bookkeeping visible

The upper and lower numbers balance separately: nucleon number and charge. An electron's lower number $-1$ records charge; it does not mean “minus one proton inside the electron”. The emitted electron or positron is created in beta decay, not pulled out of the atom's electron cloud.

| Process | Nuclear equation | What changes? |
|---|---|---|
| Alpha | ${}^{A}_{Z}X\to{}^{A-4}_{Z-2}Y+{}^4_2\mathrm{He}$ | Loses two protons and two neutrons |
| Beta-minus | ${}^{A}_{Z}X\to{}^{A}_{Z+1}Y+{}^0_{-1}e+\bar\nu_e$ | A neutron becomes a proton; an electron and electron antineutrino leave |
| Beta-plus | ${}^{A}_{Z}X\to{}^{A}_{Z-1}Y+{}^0_{+1}e+\nu_e$ | A proton in a suitable nucleus becomes a neutron; a positron and electron neutrino leave |
| Gamma | ${}^{A}_{Z}X^*\to{}^{A}_{Z}X+\gamma$ | An excited nucleus loses energy; $A$ and $Z$ stay the same |

An alpha particle is a helium **nucleus**, charge $+2e$, mass about $4\,\mathrm u$. Beta particles have electron mass. Gamma rays are photons: no electric charge or rest mass, but nonzero energy and momentum. A positron has the electron's mass and opposite charge. Neutrinos and antineutrinos are electrically neutral, have extremely small masses, and interact so weakly with matter that most escape detection. Neutral does **not** mean a particle is its own antiparticle.

For example, ${}^{238}_{92}\mathrm U\to{}^{234}_{90}\mathrm{Th}+{}^4_2\mathrm{He}$ and ${}^{14}_{6}\mathrm C\to{}^{14}_{7}\mathrm N+e^-+\bar\nu_e$. Alpha and beta decay change the element; gamma emission does not. A daughter can remain unstable and decay again: one step is not necessarily the end of a decay chain.

### A neutron is not elementary

Protons and neutrons are composite **hadrons**. Hadrons comprise **baryons** (three quarks; antibaryons have three antiquarks) and **mesons** (a quark–antiquark pair). Quarks have six flavours:

| Charge | Flavours | Corresponding antiquark charge |
|---|---|---|
| $+\tfrac23e$ | up $u$, charm $c$, top $t$ | $-\tfrac23e$ |
| $-\tfrac13e$ | down $d$, strange $s$, bottom $b$ | $+\tfrac13e$ |

A proton is $uud$: $2/3+2/3-1/3=+1$. A neutron is $udd$: $2/3-1/3-1/3=0$. A meson example is $u\bar d$, with charge $+e$. Electrons and neutrinos are elementary **leptons**, not hadrons; they contain no quarks.

Beta decay is a weak-interaction transformation of a quark:

$$\begin{aligned}n(udd)&\to p(uud)+e^-+\bar\nu_e,&d&\to u+e^-+\bar\nu_e,\\p(uud)&\to n(udd)+e^++\nu_e,&u&\to d+e^++\nu_e.\end{aligned}$$

Check charge at the quark level: $-1/3=2/3-1$ and $2/3=-1/3+1$. A free proton cannot simply undergo the second reaction: it lacks the required energy. Within a suitable nucleus the change in the **whole system's** energy can permit it. Lepton number also balances: assign $+1$ to leptons and $-1$ to antileptons. Beta-minus creates $+1-1=0$; beta-plus creates $-1+1=0$. Antimatter is not negative mass.

### The missing energy that was not missing

For a fixed alpha-decay branch, two-body energy and momentum conservation fix the alpha energy and daughter recoil. Different daughter energy levels give distinct alpha lines. Gamma transitions also give discrete energies: the nucleus has levels just as an atom does, typically with much larger gaps.

Beta particles instead have a **continuous energy spectrum**, even for a fixed decay branch. A three-body final state lets the electron or positron and the (anti)neutrino share the available energy in varying proportions, with some daughter recoil. The energy “missing” from the beta particle goes elsewhere; it is not a failure of conservation. Do not give the beta particle the entire mass-difference energy in every decay.

## Detecting radiation: the click is not the decay

| Radiation | Typical penetration | Ionisation and field behaviour |
|---|---|---|
| Alpha | A few cm of air; stopped by paper or outer skin | Dense ionisation along a short track; bends as a positive charge |
| Beta | Further through air; a few mm of aluminium can stop typical beta particles | Less dense ionisation; beta-minus bends opposite to alpha, beta-plus in the same sense |
| Gamma | Much more penetrating; attenuated by thick lead/concrete | Indirect ionisation through secondary charged particles; no electric or magnetic deflection |

These are comparisons at typical radioactive-source energies, not universal stopping thicknesses. Alpha particles' double charge and relatively low speeds produce many ionising interactions per unit track length; they lose their kinetic energy over a short path. Gamma attenuation is gradual, so “a sheet stops all gamma rays” is wrong. In an electric field $F=qE$; in a magnetic field moving charges feel a sideways force, with $r=p/(\lvert q\rvert B)$ for perpendicular motion. Therefore curvature depends on momentum as well as charge; gamma rays travel undeflected.

A Geiger–Müller tube uses ionisation in gas to trigger an electrical pulse; a counter records pulses and a timer gives count rate. A scintillation detector converts deposited energy into light and then an electrical signal. Even with a source removed, a detector records **background radiation**: cosmic rays, rocks and building materials, airborne radon, and naturally radioactive substances in food and our bodies contribute.

Measure background for a known time, then measure source plus background in the same geometry. Subtract **rates**, especially if the counting times differ:

$$C_{\rm source}=\frac{n_{\rm total}}{t_{\rm total}}-\frac{n_{\rm background}}{t_{\rm background}}.$$

**Activity** $\mathcal A$ counts decays everywhere in the sample per second. A detector intercepts only some emitted radiation; air, the source itself and the detector window absorb some; not every arrival registers. In a simple fixed arrangement, $C_{\rm measured}=\epsilon\mathcal A+C_b$, where $\epsilon$ includes geometry, emission yield and detector response. For one counted emission per decay it is less than one. Keep geometry unchanged when comparing decay rates, and keep rates low enough that detector dead time is negligible.

Ionising radiation can damage cells, cause mutations and increase cancer risk; sufficient exposure kills cells. **Irradiation** is exposure to radiation; **contamination** is radioactive material on or inside something. An alpha source is especially damaging inside tissue despite being easy to shield externally. Shorten exposure time, increase distance, use appropriate shielding, handle laboratory sources with tools, and return them to their designated shielded storage. Contamination additionally requires containment and prevention of ingestion/inhalation. Bq measures decay rate, not biological harm: particle energy, absorbed fraction and tissue matter too.

## Why a random process makes a predictable curve

![[nuclear-decay-see-it-happen.mp4]]

Watch 160 independently decaying nuclei beside their expected decay curve. The half-life is 4 s; the particular sample fluctuates around the expectation. Daughter decays and background counts are excluded.

### A nucleus has no expiry date

**Random** means the precise decay time of a particular nucleus cannot be predicted; emission directions are also random for an unpolarised source. **Spontaneous** means no external trigger is required. Ordinary changes of temperature, pressure or chemical state do not appreciably change the alpha/beta/gamma decay rates considered here. The microscopic reason is that rearranging electron energies usually barely perturbs nuclear energy scales.

Suppose each surviving nucleus has the same, constant decay probability per short interval: approximately $\lambda\,\Delta t$. Among $N$ survivors, the expected loss is $\lambda N\Delta t$. This explains both the differential equation and activity:

$$\frac{dN}{dt}=-\lambda N,\qquad \boxed{\mathcal A=-\frac{dN}{dt}=\lambda N}.$$

**Tool: separation of variables, selected because rate is proportional to amount remaining.** Integrate from $N_0$ to $N$ and from $0$ to $t$:

$$\int_{N_0}^{N}\frac{dN'}{N'}=-\lambda\int_0^t dt'\quad\Rightarrow\quad\ln\frac{N}{N_0}=-\lambda t\quad\Rightarrow\quad\boxed{N=N_0e^{-\lambda t}}.$$

Hence $\mathcal A=\mathcal A_0e^{-\lambda t}$; background-corrected count rate has the same shape if the detection arrangement stays fixed. Half-life is the time for the expected undecayed population, or activity, to halve:

$$\frac12=e^{-\lambda T_{1/2}}\quad\Rightarrow\quad\boxed{T_{1/2}=\frac{\ln2}{\lambda}},\qquad \boxed{N=N_0\left(\frac12\right)^{t/T_{1/2}}}.$$

The second form needs no calculus: every half-life multiplies the survivors by $1/2$. The **fraction** lost in each equal interval is the same; the **number** lost gets smaller. A surviving nucleus does not become “overdue”. For a finite interval the probability of decay is $1-e^{-\lambda t}$, not $\lambda t$; the latter is only a small-$\lambda t$ approximation.

![[nuclear-decay-background.svg|680]]

The graph is an expectation for many nuclei. Individual readings fluctuate; repeated equal-time counts at fixed geometry reveal the randomness. For independent counts with a steady mean, a Poisson approximation gives uncertainty about $\sqrt n$ for $n$ recorded counts. Collecting four times as many counts roughly halves the relative uncertainty. Background subtraction does not subtract its uncertainty: independent counting variances add.

### Worked example — a background trap you can hear

*Constructed measurement example.* A detector records 920 counts in 100 s with a source present, and later 320 in 100 s. A background run gives 360 counts in 300 s. The source readings are 12 minutes apart.

**Trigger: a detector counts background too. Tool: subtract rates first.** Background is $360/300=1.2$ counts s$^{-1}$. Source rates are $9.2-1.2=8.0$ and $3.2-1.2=2.0$ counts s$^{-1}$.

**Trigger: the corrected rate fell by a factor of four. Tool: count halvings.** $8\to4\to2$ is two half-lives; $T_{1/2}=12/2=6$ min. Halving the raw rate would give a false result because the background does not decay with the source.

### Worked example — when two activities cross

*Cambridge 9702/42, May/June 2025, Q10(b–c), paraphrased; checked against the published scheme.* The graph gives half-lives $2T$ and $3T$ for X and Y, whose initial activities are $4a$ and $a$. Here $a$ is the question's activity scale, not nucleon number.

**Trigger: different half-lives. Tool: $\lambda=\ln2/T_{1/2}$, then $N_0=\mathcal A_0/\lambda$.**

| Sample | $\lambda$ | $N_0$ |
|---|---|---|
| X | $\ln2/(2T)$ | $8aT/\ln2$ |
| Y | $\ln2/(3T)$ | $3aT/\ln2$ |

**Trigger: equal activities, not equal populations. Tool: equate the two exponential laws.**

$$4a\,e^{-t\ln2/(2T)}=a\,e^{-t\ln2/(3T)}\quad\Rightarrow\quad\ln4=\frac{t\ln2}{6T}\quad\Rightarrow\quad\boxed{t=12T}.$$

Check without logs: at $12T$, X has halved six times, giving $4a/64=a/16$; Y has halved four times, giving $a/16$. Their populations are still different because their decay constants differ. The detector undercounts activity because radiation goes in all directions, some is absorbed before arrival, and some arrivals are not registered.

## Binding energy: a lighter object can be harder to dismantle

**Binding energy $B$** is the energy required to separate a nucleus completely into its constituent free protons and neutrons at rest, infinitely far apart. The separated nucleons have more rest energy, and therefore more total rest mass, than the bound nucleus:

$$\boxed{\Delta m=Zm_p+(A-Z)m_n-m_{\rm nucleus}},\qquad \boxed{B=\Delta m\,c^2}.$$

The mass defect is not a batch of missing particles. Forming the bound system releases energy; once that energy has left, the remaining system has less rest mass. Supplying $B$ reverses the separation energy account. **Breaking a bound system costs energy.** A reaction releases energy when the final arrangement has still lower rest energy than the initial one.

For a general reaction,

$$\boxed{Q=\left(\sum m_{\rm initial}-\sum m_{\rm final}\right)c^2}.$$

For $Q>0$, the rest-energy decrease becomes kinetic energy and/or radiation. For $Q<0$, external energy must be supplied; a collision's threshold may exceed $\lvert Q\rvert$ because momentum must also balance. Total energy and momentum are conserved; the sum of the particles' rest masses need not be.

**Check which masses were supplied.** Nuclear masses exclude electrons. Neutral-atom masses include them. For binding energy, neutral atomic masses can be paired with hydrogen-atom masses via $\Delta m\approx Zm_{\rm H}+(A-Z)m_n-m_{\rm atom}$, neglecting small electronic binding corrections. For beta-plus decay using neutral atomic masses, $Q\approx(M_X-M_Y-2m_e)c^2$: creating the positron and accounting for the changed electron inventory costs two electron masses. Do not mix conventions in one subtraction.

### Worked example — polonium's mass ledger

*Cambridge 9702/42, May/June 2024, Q9(a–b), paraphrased; checked against the published scheme.* For ${}^{212}_{84}\mathrm{Po}$ use $m_p=1.007276\,\mathrm u$, $m_n=1.008665\,\mathrm u$, and **nuclear** mass $211.942749\,\mathrm u$.

**Trigger: assemble a nucleus from separated nucleons. Tool: count constituents before subtracting masses.** There are $84$ protons and $212-84=128$ neutrons:

$$\Delta m=[84(1.007276)+128(1.008665)-211.942749]\,\mathrm u=1.777555\,\mathrm u\approx2.95\times10^{-27}\ \mathrm{kg}.$$

**Tool: $B=\Delta mc^2$, using the paper's rounded constants.** $B\approx(2.95\times10^{-27})(3.00\times10^8)^2=2.66\times10^{-10}$ J. **Trigger: compare nuclei of different sizes. Tool: divide by nucleon number.** $B/A=2.66\times10^{-10}/212=1.25\times10^{-12}$ J per nucleon, about $7.8$ MeV per nucleon. Do not divide by $Z$: neutrons are bound too.

### One curve explains both fission and fusion

![[nuclear-binding-energy.svg|680]]

The binding energy **per nucleon** rises steeply among light nuclei, peaks broadly in the iron/nickel region around $A\sim56$–62, then decreases gently for heavy nuclei. The short-range force gives each nucleon a limited set of neighbours; the growing electric repulsion increasingly opposes binding in heavy nuclei. The curve stays roughly level at several MeV per nucleon over much of the heavy range, not a steep plunge to zero.

For reactions with unchanged total proton and neutron counts, $Q=B_{\rm products,total}-B_{\rm reactants,total}$. An increase in total binding means a decrease in rest energy. When using a per-nucleon graph, multiply by each nucleus's $A$ before adding energies. A sketch suggests favourable reactions; exact masses determine a particular $Q$.

**Fission:** a heavy nucleus splits into smaller nuclei, usually with neutrons. An illustrative channel is ${}^{235}_{92}\mathrm U+{}^1_0n\to{}^{141}_{56}\mathrm{Ba}+{}^{92}_{36}\mathrm{Kr}+3{}^1_0n$. Count $236$ nucleons and charge $92e$ on each side. The medium-mass products bind more strongly per nucleon, releasing energy mainly as fragment kinetic energy, later converted to heat. Other product pairs are possible. Fission may be spontaneous or neutron-induced; an energy barrier can require an initiating interaction even when $Q>0$.

**Fusion:** light nuclei join to produce more tightly bound products. For example, ${}^2_1\mathrm H+{}^3_1\mathrm H\to{}^4_2\mathrm{He}+{}^1_0n$ releases about $17.6$ MeV. Using rounded neutral-atom masses $2.014102$, $3.016049$, $4.002603$ and neutron mass $1.008665$ in u gives $\Delta m=0.018883\,\mathrm u$ and $Q\approx0.018883(931.5)=17.59$ MeV; the electron counts cancel. The alpha particle and neutron recoil in opposite directions. With negligible initial momentum, equal momentum magnitudes imply $K=p^2/(2m)$: the lighter neutron takes roughly four fifths of the kinetic energy.

Why must fusion fuel be hot? Positive nuclei repel before they get close enough for nuclear attraction. High temperature supplies collision energy; high density and confinement increase encounters. [[Quantum Tunnelling]] lets some reactions occur below the classical electric barrier. In the Sun, a sequence of reactions converts hydrogen into helium; stellar fusion is not simply the laboratory deuterium–tritium reaction above. Fusing nuclei beyond the iron/nickel region does not generally supply stellar energy.

## Where this physics does real work

### An alarm listening to a tiny electric current

In an **ionisation** smoke alarm, americium-241 alpha particles ionise the air between electrodes. The ions carry a small current. Smoke changes charge collection, reducing the current and triggering the alarm. The short alpha range keeps the ionisation local; the long half-life (about 432 years) makes the source output nearly constant during the device's service life. This is a different sensing method from an optical smoke alarm. The radioactive source's half-life is not the alarm's replacement interval. [NRC: smoke detectors](https://www.nrc.gov/reading-rm/doc-collections/fact-sheets/smoke-detectors)

### Choose the radiation for the job

| Application | Why this radiation / half-life? |
|---|---|
| Paper or foil thickness gauge | Put a beta source opposite a detector: thicker material gives fewer counts. Alpha would be stopped too readily; gamma could pass through thin material with too little change. Choose a sufficiently long half-life for steady output |
| Food irradiation / equipment sterilisation | Penetrating gamma radiation reaches microbes throughout suitable packaged material. A long-lived source avoids frequent replacement; controlled irradiation does not itself leave radioactive source material in the product |
| Medical tracer | Attach a detectable radionuclide to a substance following the process of interest. Escaping photons allow external imaging; the half-life must allow preparation and measurement while limiting lingering activity |
| Gamma radiotherapy | Collimated or converging radiation deposits a planned damaging dose in a tumour while limiting exposure elsewhere. Penetration enables treatment of internal targets; treatment and diagnostic imaging use different dose objectives |
| Underground pipe leak | A suitable tracer follows the fluid; escaping radiation identifies an unexpected location. Half-life must allow measurement, then limit persistent contamination; an authorised procedure is essential |

Technetium-99m illustrates the medical compromise: its roughly six-hour half-life allows imaging on a useful timescale, and its characteristic gamma radiation can be detected outside the body. The biological carrier decides where it goes; the nucleus supplies the signal. Physical decay and biological removal both reduce activity in an organ. For independent exponential removal rates, $\lambda_{\rm effective}=\lambda_{\rm physical}+\lambda_{\rm biological}$. [IAEA: technetium-99m production and use](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1405_web.pdf)

**Carbon dating** asks a different question: how long since a once-living sample stopped exchanging carbon with its surroundings? With a known initial carbon-14 activity per amount of carbon and a closed sample, $t=\ln(\mathcal A_0/\mathcal A)/\lambda$. One quarter of the initial activity means two half-lives, about $11\,460$ years using $5730$ years. This is an ideal-model calculation: real dating needs calibration of changing atmospheric carbon-14 and checks for contamination. A sample's total count rate alone is not its age; compare equivalent carbon quantities and subtract background. [NIST: radiocarbon dating](https://www.nist.gov/how-do-you-measure-it/how-do-you-know-age-fossils-and-other-old-things)

### A power station is a controlled chain reaction plus a heat engine

Some fission neutrons cause further fissions. If, on average, each fission leads to fewer than one next fission, the chain dies down; one sustains it; more than one makes it grow. The effective multiplication factor describes that balance, including neutron escape and non-fission absorption. In a thermal-neutron reactor:

| Component | Job — trace the cause |
|---|---|
| Fuel | Contains fissile nuclei; fragment kinetic energy becomes thermal energy |
| Moderator | Slows neutrons by collisions, increasing their chance of causing fission in suitable fuel; it is not the neutron-removal control |
| Control rods | Absorb neutrons; insertion reduces the multiplication factor |
| Coolant / heat exchanger | Removes heat and transfers it to another fluid circuit where the design uses one |
| Shielding / containment | Reduces radiation exposure / helps retain radioactive material |

Steam can then drive a turbine and generator: nuclear energy → thermal energy → mechanical work → electrical energy. At $200$ MeV per fission, a constructed $1.0$ GW **thermal** example requires $10^9/[200(1.602\times10^{-13})]\approx3.1\times10^{19}$ fissions per second. Electrical output is lower because a heat engine rejects heat. [DOE: how a nuclear reactor works](https://www.energy.gov/ne/articles/nuclear-101-how-does-nuclear-reactor-work)

Stopping the chain reaction does not instantly stop the heat: radioactive fission products continue to decay. Spent fuel therefore needs cooling and shielding initially, with containment and management appropriate to the radionuclides' half-lives thereafter. High initial activity and very long persistence are distinct waste-management issues. Reactor design also varies: fast reactors deliberately operate without a moderator. [NRC: spent fuel and decay heat](https://www.nrc.gov/waste/spent-fuel-storage/faqs)

## Common Misconceptions

| Claim | Repair the model |
|---|---|
| “After two half-lives, everything is gone.” | Track survivors: $1\to1/2\to1/4$. The same fraction of what remains decays |
| “Random means we cannot predict anything.” | Separate one nucleus from a population; a probability law predicts the population's statistics |
| “Gamma changes the element.” | Recount protons: gamma changes excitation, not $Z$ |
| “The beta electron was stored inside the nucleus.” | Track the weak transformation and the newly created leptons |
| “Greater binding energy means more energy ready to escape.” | Binding energy is a separation cost; calculate the difference between initial and final systems |
| “Fusion and fission contradict each other.” | Both can move toward greater binding per nucleon from opposite sides of the curve |
| “More counts proves more nuclei.” | Check background, geometry and $\lambda$: $\mathcal A=\lambda N$ |

## Exam Notes

### Cambridge 9702 — AS §11; A Level §23

**§11.1:** foil-scattering inference; nuclear atom; nuclide notation and isotopes; charge/nucleon conservation; alpha, beta-minus, beta-plus and gamma; antiparticles; neutrino/antineutrino assignment; discrete alpha versus continuous beta energies; unified atomic mass unit. **§11.2:** all six quark flavours and their charges, proton/neutron composition, baryons/mesons, beta changes at quark level, and leptons. Do not stop at the neutron-level beta equation if the question asks for quarks.

**§23.1–23.2:** mass–energy equivalence, nuclear equations, mass defect, binding energy per nucleon and its curve, fission/fusion, random versus spontaneous, activity, decay constant, half-life and exponential laws. Questions at AS are assessed through Papers 1/2; A-Level nuclear calculations appear in Paper 4. The 2028–30 syllabus is the reference; these outcomes match 2025–27. The worked published-paper anchors are **9702/42/M/J/24 Q9** and **9702/42/M/J/25 Q10**. State binding energy as complete separation to infinity; distinguish that from “energy emitted by a nucleus”. The radiation diagram/graph explains a claim; it does not replace the conserved-number equation.

### Cambridge 0625 — §5.1–5.2

Core includes nuclear composition, isotopes and notation, background sources and counts, alpha/beta/gamma properties, spontaneous random decay, elementary half-life and radiation safety. Supplement adds foil-scattering inference, nuclear fission/fusion with qualitative mass–energy changes, field deflections and ionisation reasoning, decay equations, background-corrected half-life, and radiation/half-life choices for the listed applications. **Beta means beta-minus here; beta-plus is not required.** Exponentials and quarks extend beyond this syllabus. Keep radioactive decay separate from ionisation of an atom.

### IB Physics — E.1, E.3, E.4; fusion bridge to E.5

**SL/HL:** E.1 nuclear evidence and notation; E.3 isotopes, mass defect/binding, strong force, decay modes including beta-plus and (anti)neutrinos, activity/counts/background and integer half-lives; E.4 spontaneous/induced fission, chain reactions, reactors and waste. **Additional HL:** nuclear radius/density, closest approach and deviations from Rutherford scattering (E.1); neutron/proton stability, nuclear energy spectra, continuous beta spectrum, decay constant and arbitrary-time exponential calculations (E.3). Quark flavour bookkeeping extends beyond the IB nuclear requirements. The fusion explanation supports E.5; stellar equilibrium, evolution and the HR diagram require their own astronomy treatment.

### AP Physics 2 — §15.7–15.8

§15.7 examines strong-force nuclear interactions, nucleon/energy/momentum conservation, mass–energy conversion, fission/fusion and decay probabilities, including $N=N_0e^{-\lambda t}$ and $\lambda=\ln2/T_{1/2}$. §15.8 examines alpha, beta-minus, beta-plus and gamma, plus charge, nucleon and lepton-number conservation. Specific isotope half-lives and decay modes are not memorisation requirements. Electron capture and neutron emission are explicitly outside the §15.8 framework; quark flavours and weak-interaction mechanisms are enrichment.

**Where it is not examined:** nuclear structure and radioactive decay are not topics in AP Physics 1, AP Physics C: Mechanics, or AP Physics C: Electricity and Magnetism. Their conservation laws provide tools, not a nuclear-physics syllabus. Cambridge maths can use exponential-decay contexts without examining nuclear mechanisms.

## Connections

- **Parents:** [[Wave-Particle Duality]] and [[Energy Levels and Line Spectra]] — quantum particles and allowed states, now inside nuclei.
- **Mathematical engine:** [[Exponential Growth and Decay]], [[Differential Equations]] and [[Poisson Distribution]] — population law and counting fluctuations.
- **Same equation, different cause:** [[Capacitors]] — charge leaks continuously; a radioactive population loses whole nuclei at random.
- **Extensions:** [[Quantum Tunnelling]] — how a nucleus can decay through a barrier; [[Particle Physics]] — deeper interactions and particle families.
- **Applications:** [[Energy Resources]], [[Entropy and the Second Law]] — nuclear heat still has to pass through a real heat engine.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| ${}^{A}_{Z}X$ | `{}^{A}_{Z}X` | Nuclide notation |
| $\mathcal A=\lambda N$ | `\mathcal A=\lambda N` | Activity |
| $N=N_0e^{-\lambda t}$ | `N=N_0e^{-\lambda t}` | Expected survivors |
| $T_{1/2}=\ln2/\lambda$ | `T_{1/2}=\ln2/\lambda` | Half-life |
| $\bar\nu_e$ | `\bar\nu_e` | Electron antineutrino |
| $B=\Delta mc^2$ | `B=\Delta mc^2` | Binding energy |
| $R=R_0A^{1/3}$ | `R=R_0A^{1/3}` | Approximate nuclear radius |
