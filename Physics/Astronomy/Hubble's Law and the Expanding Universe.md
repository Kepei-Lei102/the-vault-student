---
chinese: 哈勃定律与膨胀的宇宙 (Hābó dìnglǜ yǔ péngzhàng de yǔzhòu)
aliases:
  - Hubble's Law
  - Hubble–Lemaître Law
  - Big Bang Theory
prerequisites:
  - "[[Doppler Effect]]"
  - "[[Stellar Luminosity and Size]]"
leads_to: []
teach_together:
  - "[[Henrietta Leavitt and the Cosmic Yardstick]]"
tags:
  - subject/physics
  - domain/astronomy
  - level/IGCSE
  - level/A-Level
  - level/university
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - syllabus/9702-25-3
  - syllabus/0625-6-2
  - type/deep
  - type/derivation
  - notation/hubble-constant
  - misconception/earth-is-expansion-centre
  - misconception/hubble-time-is-exact-age
  - misconception/big-bang-is-explosion-in-space
---

# Hubble's Law and the Expanding Universe 哈勃定律与膨胀的宇宙

> *A galaxy supplies two clues: how far away it is, and how its light has changed. Put the clues on the same graph, and the history of the universe begins to become measurable.*

## Definition

**Hubble's law**, also called the **Hubble–Lemaître law**, relates a galaxy's recession due to cosmic expansion to its distance:

$$\boxed{v_{\rm rec}=H_0d.}$$

Here $d$ is distance, $v_{\rm rec}$ is recession speed and $H_0$ is the **present expansion rate per unit distance**. On a graph of recession speed vertically against distance horizontally, $H_0$ is the gradient. Its SI unit is $\mathrm{s^{-1}}$: $(\mathrm{m\,s^{-1}})/\mathrm m$.

For the nearby-universe observational application, use recession speeds inferred from small spectral redshifts. More generally, in a homogeneous expanding model, $v=H(t)d$ describes the growth of **proper distance measured at the same cosmic time** between comoving objects. A distant galaxy is seen in the past; its measured redshift is not an exact instantaneous speedometer reading.

**The core intuition:** equal *fractional* growth produces unequal *absolute* growth. If every gap grows by 10%, a 10-unit gap gains 1 unit while a 100-unit gap gains 10. Over the same time interval, the farther pair separates faster.

### 中文锚点

一团葡萄干面团发起来时，相隔越远的两颗葡萄干，在同一会儿里增加的距离也越多。不是远处那颗格外卖力地跑，而是它们之间有更多面团在一起膨胀。换一颗葡萄干来看，也会看到类似的关系，并不需要谁站在正中心。宇宙的大尺度膨胀可以借这个画面来想：越远的星系，退行通常越快。不过比喻到这里就该停下——宇宙不必有面团外面的厨房，星系内部和我们手里的尺子也不会简单地跟着变大。

## 1. Two measurements that must be earned separately

### Distance: the Leavitt side of the graph

A faint galaxy need not be far away; it might be intrinsically faint. [[Stellar Luminosity and Size]] derives $F=L/(4\pi d^2)$ and explains why a **calibrated standard candle** supplies the missing luminosity. Cepheid variables provide one step; standardised Type Ia supernovae extend the reach.

A **light-year is a distance**, the distance light travels in vacuum in one year. With a Julian year of 365.25 days,

$$1\ \mathrm{ly}=c\times(365.25\times86400\ \mathrm s)\approx9.46\times10^{15}\ \mathrm m.$$

Our Milky Way is one of billions of galaxies; its stellar disc is roughly 100,000 light-years across. That is a scale of one galaxy, not the size of the universe.

A parsec is about 3.26 light-years; a megaparsec (Mpc) is a million parsecs, about $3.086\times10^{22}$ m. Astronomy often reports $H_0$ in $\mathrm{km\,s^{-1}\,Mpc^{-1}}$.

### Spectral shift: the wavelength side

Identify a pattern of emission or absorption lines, compare with the same transitions measured in the laboratory, and calculate

$$z=\frac{\lambda_{\rm obs}-\lambda_{\rm emit}}{\lambda_{\rm emit}}.$$

Positive $z$ means longer wavelengths. It does not mean that the object looks visibly red. For small redshifts, with local motions treated appropriately,

$$\boxed{v\approx cz.}$$

The denominator is the **emitted/rest wavelength**, not the observed one. Since $f=c/\lambda$, a redshift is a decrease in frequency: $\Delta f/f_{\rm emit}=-z/(1+z)\approx-z$. The wavelength and frequency changes have opposite signs; formulas equating their fractional changes mean magnitudes.

These are independent measurement chains. **To measure $H_0$, do not first use an assumed $H_0$ to obtain the distances.** That would put your answer into your input. Once the relation is calibrated, it can instead be used to estimate distance from a suitable galaxy's redshift.

## 2. Why expansion gives a straight line

Imagine marks on an elastic strip. A pair starts at separation $d$; over a short interval $\Delta t$, every separation grows by the same fraction $\epsilon$.

**Tool: change divided by time. Trigger: the fractional growth is shared.**

$$\Delta d=\epsilon d\quad\Longrightarrow\quad
v\approx\frac{\Delta d}{\Delta t}=\frac{\epsilon}{\Delta t}d.$$

Thus $v/d$ is common to every pair. The relation follows from a uniform change of scale, not a force aimed directly away from Earth.

### Scale factor: turn the picture into a definition

Let $a(t)$ be the **scale factor**, normalised so that $a(t_0)=1$ today. Let $\chi$ be a fixed comoving separation: a coordinate gap whose occupants participate in the average expansion. Then

$$d(t)=a(t)\chi.$$

Differentiate while holding $\chi$ fixed:

$$v_{\rm rec}=\frac{\mathrm dd}{\mathrm dt}=\frac{\mathrm da}{\mathrm dt}\chi
=\underbrace{\frac1a\frac{\mathrm da}{\mathrm dt}}_{H(t)}d.$$

Therefore

$$\boxed{H(t)=\frac1{a(t)}\frac{\mathrm da}{\mathrm dt}},\qquad H_0=H(t_0).$$

“Hubble constant” means the common proportionality factor **at the present epoch**. It need not remain constant through cosmic history. A constant $\mathrm da/\mathrm dt$ gives a growing $a$ and a decreasing $H$; a constant $H$ instead gives exponential growth of $a$.

### Change the observer: the relation survives

In a flat schematic model, write positions as $\mathbf r_i=a\mathbf q_i$. Relative to any chosen galaxy $j$,

$$\mathbf v_i-\mathbf v_j=H(t)(\mathbf r_i-\mathbf r_j).$$

Subtracting the observer's position and velocity leaves the same law. Every comoving observer sees the same large-scale pattern. **Seeing recession in every direction does not make you the centre.**

![[hubble-expansion.mp4]]

*The first two scenes use the schematic model $a=1+0.1t$ in arbitrary units, then change observer. Graph points can overlap when galaxies have equal distances. The finite grid is a sample, not the universe's edge; galaxy symbols retain their size. The final scene compares three idealised histories with identical present $H_0$ and different ages.*

### Where the analogy stops

The raisin loaf has an outside and an edge; neither is required by cosmic expansion. An expanding balloon's **surface** has no preferred point on that surface; its centre in a surrounding three-dimensional room is not a place in the model universe. Neither analogy determines the universe's global size or curvature.

Gravitationally bound systems do not simply follow the average expansion. The Solar System and a bound galaxy keep their own dynamics; your ruler does not stretch along with $a(t)$. [[Gravitational Fields]] supplies the local orbital picture. [OpenStax: expanding-universe models](https://openstax.org/books/astronomy-2e/pages/29-2-a-model-of-the-universe)

## 3. Read the graph before reading its gradient

![[hubble-axes-and-scatter.svg|850]]

*Left: synthetic observations with deliberately added velocity scatter around a model of 70 km s⁻¹ Mpc⁻¹. Right: the exact model on log–log axes. These are teaching data, not Hubble's historical observations or a measurement of today's constant.*

On **linear axes**, $v=H_0d$ has gradient $H_0$. On **log–log axes**, using numerical values in fixed stated units,

$$\log v=\log H_0+\log d.$$

The gradient is **1**, while the intercept encodes the numerical value of $H_0$. Logging the axes does not make $H_0$ the gradient, nor does it automatically remove scatter. See [[Linearisation]].

### Peculiar velocities: galaxies have local lives

Galaxies also move relative to the smooth cosmic flow because of gravity. In a low-redshift approximation,

$$v_{\rm observed}\approx H_0d+v_{\rm peculiar,radial},$$

after correcting the observer's motion. A nearby galaxy can approach us while the universe expands on larger scales. The approximation applies to radial velocities; it is not a relativistic addition formula for distant objects.

For example, a 300 km/s local motion is 43% of the 700 km/s Hubble-flow speed at 10 Mpc if $H_0=70$ km s⁻¹ Mpc⁻¹. At 100 Mpc the same local motion is about 4.3%. One close galaxy is a poor basis for measuring the cosmic rate.

A real fit must handle uncertainties in both distance and velocity, calibration correlations and sample selection. Averaging helps random scatter; it does not remove a shared error in the distance scale. [Distance-ladder analysis of peculiar velocities and systematic uncertainty](https://arxiv.org/abs/2204.10866)

## 4. Rewind the expansion: what does the age estimate mean?

If a galaxy had moved away at its **present separation speed throughout the past**, the time to grow from negligible separation to $d$ would be

$$t\approx\frac d v=\frac d{H_0d}=\boxed{\frac1{H_0}}.$$

This **Hubble time** has units of time, as it must. The cancellation of $d$ is why the same estimate emerges from different galaxies in the ideal flow.

Use an illustrative $H_0=70$ km s⁻¹ Mpc⁻¹:

$$H_0=\frac{70\times10^3}{3.086\times10^{22}}\approx2.27\times10^{-18}\ \mathrm{s^{-1}},$$

$$H_0^{-1}\approx4.41\times10^{17}\ \mathrm s\approx14.0\ \text{billion years}.$$

That is an estimate under an assumed history, not an exact age measurement. **Extrapolating a present speed backward assumes the history you are trying to discover.**

![[hubble-time-and-age.svg|700]]

*All curves pass through today's $a=1$ with the same tangent slope and hence the same $H_0$. Their beginnings occur at different times. Radiation-only and matter-only flat universes are idealised models, not successive whole-universe age estimates to add together.*

For $a(t)=(t/t_0)^p$, direct differentiation gives $H=p/t$ and therefore $t_0=p/H_0$. Coasting ($p=1$), flat matter-only ($p=2/3$) and flat radiation-only ($p=1/2$) give different ages despite the same present $H_0$. The actual universe changed its dominant components over time. The familiar age of about **13.8 billion years** comes from a fitted cosmological history, not a universal identity $t_0=H_0^{-1}$. [ESA: Planck results](https://www.esa.int/Science_Exploration/Space_Science/Planck/Planck_science_highlights)

## 5. The hot Big Bang: several clues must agree

Rewinding a growing scale factor gives smaller separations and higher matter density. For a fixed number of particles in an expanding comoving volume, volume grows as $a^3$, so number density falls as $a^{-3}$.

**Expansion alone does not establish every part of the hot Big Bang model.** The evidence also includes a relic thermal radiation field and the abundances of light elements. The model describes an early hot, dense universe evolving into the one we observe. It does not require an explosion from a special location into pre-existing empty space, and these observations do not settle what happened at a literal mathematical singularity.

### Cosmological redshift: the travelling wave remembers expansion

For light propagating between comoving emitter and observer in the expanding model,

$$\boxed{1+z=\frac{a_{\rm observed}}{a_{\rm emitted}}}.$$

If the scale factor doubles while the light travels, its wavelength doubles and its photon energy $E=hc/\lambda$ halves. A photon population also becomes more dilute: number per volume falls as $a^{-3}$. Radiation energy per volume therefore falls as $a^{-4}$.

For an expanding thermal photon distribution, $T\propto1/a$. Cooling an initially hot radiation bath by expansion preserves its blackbody form. This connects [[Energy Levels and Line Spectra]]'s photon energy with [[Stellar Luminosity and Size]]'s thermal spectrum.

### The cosmic microwave background

The **CMB/CMBR** is radiation arriving from all sky directions with a nearly thermal spectrum at about **2.725 K**, with small temperature variations. It is a **spectrum of frequencies**, not one monochromatic microwave. COBE's FIRAS instrument compared it with a calibrated blackbody and found extremely close agreement. [NASA: FIRAS overview](https://lambda.gsfc.nasa.gov/product/cobe/firas_overview.html)

Early in cosmic history, radiation scattered frequently in an ionised plasma. About 380,000 years after the Big Bang, the formation of neutral atoms greatly reduced scattering and the photons could travel freely. Expansion has stretched that radiation to much longer wavelengths. Thus the CMB is a view of an early transparent universe, not a photograph of the instant $t=0$. [ESA: release of the CMB](https://www.esa.int/Science_Exploration/Space_Science/Planck/The_cosmic_microwave_background_and_inflation)

Its broad sky coverage and thermal spectrum support a hot early state. The small variations matter too: they constrain the conditions from which structure developed. Instrument noise, foreground radiation from our galaxy and our own motion must be separated from the cosmological signal.

### Light elements: a second thermometer for the past

An early hot universe permits nuclear reactions among protons and neutrons. As expansion cools it, reaction rates fall and primordial abundances become effectively fixed. The hot Big Bang predicts mostly hydrogen and helium, with smaller amounts of deuterium and other light nuclei. Comparing these predictions with observations tests the thermal history independently of the distance–redshift graph. Most heavy elements require later stellar processes; primordial nucleosynthesis did not manufacture everything. [[Nuclear Physics]] supplies the reaction and binding-energy principles. [NASA: early-universe nucleosynthesis](https://science.nasa.gov/universe/overview/)

## 6. Where the law earns its keep

**Turning a spectrum into a rough place on a map.** After calibrating $H_0$, a suitable low-redshift galaxy with $z=0.020$ has $v\approx6000$ km/s and $d\approx86$ Mpc for $H_0=70$ km s⁻¹ Mpc⁻¹. This is useful astronomical inference when individual standard candles are unavailable; peculiar motion and the model set its limitations. The image tells you a direction, while the redshift supplies distance information.

**Testing the expansion history.** Astronomers compare standardised supernova brightnesses and redshifts across cosmic time. Differences from a simple coasting history let them investigate changing expansion. Present-day distance-ladder measurements and values inferred from early-universe observations do not agree as closely as their quoted uncertainties would suggest—the **Hubble tension**. It motivates checks of calibration and cosmological assumptions; it is not, by itself, proof of a particular new physics explanation. [NASA: Hubble constant and tension](https://science.nasa.gov/mission/hubble/science/science-behind-the-discoveries/hubble-constant-and-tension/)

**The people in the measurement chain.** Leavitt established the period–luminosity relationship; Slipher obtained pioneering galaxy spectra; Lemaître derived an expanding solution and a distance–velocity relation in 1927; Hubble published the observational relation in 1929. In 2018 the IAU recommended the name Hubble–Lemaître law. [[Henrietta Leavitt and the Cosmic Yardstick]] follows the plate work behind the distance scale. [IAU: naming and historical evidence](https://iauarchive.eso.org/news/pressreleases/detail/iau1812/)

## 7. Worked examples — choose the inference, then the equation

### A. A shifted spectrum changes two inferred quantities

**Cambridge 9702/41/M/J/25 Q10(b)(ii–iii), (c)**, paraphrased. A star's emitted peak is $4.62\times10^{-7}$ m; its observed peak is $4.91\times10^{-7}$ m. Use $c=3.00\times10^8$ m/s and $H_0=2.3\times10^{-18}$ s⁻¹. Infer speed and distance, and explain the effect of using the observed peak to infer surface temperature.

**Trigger: compare emitted and observed versions of the same feature. Tool: fractional wavelength shift.**

$$z=\frac{4.91-4.62}{4.62}=0.06277\ldots,\qquad v\approx cz=1.883\times10^7\ \mathrm{m\,s^{-1}}.$$

**Trigger: a specified Hubble constant and recession speed. Tool: $d=v/H_0$.**

$$d=\frac{1.883\times10^7}{2.3\times10^{-18}}=8.19\times10^{24}\ \mathrm m\approx8.2\times10^{24}\ \mathrm m.$$

The published scheme obtains **$8.3\times10^{24}$ m** using its rounded $v=1.9\times10^7$ m/s. The small difference is intermediate rounding, not a different physical method. Keep guard digits in your own calculation. This example uses the stipulated low-speed model; it is not an exact high-redshift inversion.

**Trigger: a longer peak wavelength enters Wien's law. Tool: $T=b_W/\lambda_{\max}$.** The inferred temperature is **too low**. Indeed $T_{\rm inferred}/T_{\rm true}=4.62/4.91\approx0.941$. Correct the redshift before interpreting the source's rest-frame thermal spectrum.

### B. Read the best-fit line and its units

**Cambridge 0625/43/M/J/25 Q10(c)**, paraphrased. The supplied graph plots recession speed in units of $10^4$ km/s against distance in units of $10^{20}$ km. Its best-fit line passes approximately through $(0,0)$ and $(100,2.5)$ in those plotted coordinates.

**Trigger: speed vertically, distance horizontally. Tool: $H_0=\Delta v/\Delta d$.**

$$H_0=\frac{2.5\times10^4\ \mathrm{km\,s^{-1}}}{100\times10^{20}\ \mathrm{km}}=\boxed{2.5\times10^{-18}\ \mathrm{s^{-1}}}.$$

Kilometres cancel because both quantities use kilometres. Converting both to metres gives the same result; converting only one produces a factor-of-1,000 error. Use well-separated points **on the supplied line**, not whichever noisy observations look convenient. This matches the three-mark scheme.

**Original extension:** $H_0^{-1}=4.0\times10^{17}$ s, about $1.3\times10^{10}$ years. The graph supplied a present gradient; a cosmic age still requires the history assumption.

### C. Explain a relic rather than just naming it

**Cambridge 0625/43/O/N/25 Q9(a)(i–ii)**, paraphrased: identify the early origin of CMBR and explain how its wavelength has changed.

**Trigger: radiation has travelled through an expanding universe. Tool: $\lambda\propto a$.** It comes from the early universe after the Big Bang, and its wavelength has **increased as the universe expanded**. The scheme awards the origin statement, the increase, and the expansion explanation. The more precise physical account distinguishes the early radiation bath from the later epoch when photons began to travel freely.

### D. A calibration error that averaging will not cure

**Original model problem.** Every distance in an otherwise exact Hubble dataset is overestimated by 10%; velocities are correct. What happens to the fitted $H_0$ and its reciprocal?

**Trigger: one common multiplicative distance error. Tool: substitute into the measured ratio.**

$$H_{\rm fit}=\frac{v}{1.10d}=\frac{H_{\rm true}}{1.10},\qquad H_{\rm fit}^{-1}=1.10H_{\rm true}^{-1}.$$

The inferred rate is about 9.1% too low; the Hubble-time estimate is 10% too high. More galaxies do not fix a calibration error shared by them all. [[Accuracy vs Precision]] explains this distinction.

## 8. Try it: move the observer, then change the history

Run the adjacent reproducible model:

```bash
python3 hubble-model.py
```

It checks 100 changes of observer, the distance-calibration effect, the log–log gradient, and independently integrates four cosmological age models. The data are synthetic; passing the checks verifies the implementation of the assumptions, not that those assumptions fit the universe.

Predict before changing the code:

1. Double every galaxy's comoving coordinate. What happens to $d$, $v$, and $v/d$?
2. Add a fixed radial peculiar velocity to one close galaxy. Does its individual $v/d$ still estimate the cosmic rate well?
3. Hold $H_0$ fixed but change the matter fraction in `flat_matter_lambda_age`. Must the age stay fixed?

**Check:** (1) $d$ and $v$ both double; $H$ stays fixed. (2) No; fractional contamination grows as $1/d$. (3) No; today's fractional expansion rate does not specify the past history.

## 9. Beyond syllabus — the integral behind the cosmic clock

Recall that $H=(1/a)(\mathrm da/\mathrm dt)$. Rearrange it to $\mathrm dt=\mathrm da/[aH(a)]$. For a model evolving from $a=0$ to $a=1$ today,

$$\boxed{t_0=\int_0^1\frac{\mathrm da}{aH(a)}}.$$

The entire function $H(a)$ matters, not merely its value at $a=1$. In a spatially flat model containing nonrelativistic matter and a cosmological constant, neglecting radiation, the Friedmann equation gives

$$H(a)=H_0\sqrt{\Omega_m a^{-3}+\Omega_\Lambda},\qquad\Omega_m+\Omega_\Lambda=1.$$

The $\Omega$ values are present density fractions relative to the critical density $3H_0^2/(8\pi G)$. Matter dilutes as volume increases; the cosmological constant contributes a constant energy density. This is a supplied general-relativistic model, not a consequence of Hubble's straight-line graph alone.

To integrate, rewrite the integrand as $a^{1/2}/[H_0\sqrt{\Omega_m+\Omega_\Lambda a^3}]$. Substitute $u=a^{3/2}$, so $\mathrm du=(3/2)a^{1/2}\mathrm da$. The remaining integral is of $1/\sqrt{\Omega_m+\Omega_\Lambda u^2}$, whose antiderivative is an inverse hyperbolic sine. For $0<\Omega_m<1$, this gives

$$t_0=\frac{2}{3H_0\sqrt{\Omega_\Lambda}}\operatorname{arsinh}\!\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}.$$

With the illustrative $H_0=70$ km s⁻¹ Mpc⁻¹ and $\Omega_m=0.3$, the result is about **13.47 billion years**; matter-only gives **9.31 billion years**. Neither is asserted as the measured age of our universe. The runnable model compares the analytic result with direct numerical integration.

### Farther away: distance becomes a choice of question

Recall that $1+z=a_0/a_{\rm emitted}$. Light takes time to arrive, during which separation changes. **Light-travel distance**, **proper distance today**, and the **luminosity distance** inferred from flux need not be equal. In a flat model with $a_0=1$,

$$\chi(z)=c\int_0^z\frac{\mathrm dz'}{H(z')},\qquad d_L=(1+z)\chi,\qquad d_A=\frac{\chi}{1+z}.$$

Here $d_A$ relates transverse size at emission to observed angle. The integral needs an expansion model. This is why $d=cz/H_0$ cannot be extended arbitrarily far: it is the first nearby approximation, not a universal distance calculator. Recession defined by growing proper separation can exceed $c$ without an object locally outrunning a light beam; special relativity limits local relative motion. [Hogg: cosmological distance measures](https://arxiv.org/abs/astro-ph/9905116)

## Common mistakes

| Mistake | Repair |
|---|---|
| “Everything recedes from us, so we are the centre.” | Subtract any other comoving observer's position and velocity; the same relation survives |
| “Every galaxy must be redshifted.” | Local peculiar motion can dominate nearby; the law describes the large-scale flow |
| “$H_0$ is the speed of the universe.” | It is speed **per unit distance**, with dimension inverse time |
| “The Hubble constant never changes.” | $H_0$ labels today; $H(t)$ evolves |
| “$1/H_0$ is the exact age.” | It extrapolates an assumed history; integrate $1/[aH(a)]$ for a specified model |
| “A log–log Hubble plot has gradient $H_0$.” | Its gradient is 1 for the ideal law; intercept encodes the coefficient in stated units |
| “The CMB is one microwave frequency, emitted at $t=0$.” | It is a thermal spectrum; freely travelling relic photons date from the early transparent universe |
| “The Big Bang was a bomb at one place.” | It describes an early hot, dense state and expansion of the spatial scale throughout the model |

## Exam Notes

### Cambridge 9702 — A-Level §25.3, not AS

The 2028–2030 syllabus is canonical; 2025–2027 has the same outcomes. **§25.3.1–4:** identify shifted emission/absorption lines; use fractional wavelength/frequency-shift magnitudes and $v/c$; explain the expansion inference; recall and use $v=H_0d$ and connect expansion to the Big Bang. The syllabus requires **SI units only** for the Hubble calculations. This is Paper 4 content; Paper 5 can assess generic graph/uncertainty skills in a supplied context.

State what both variables mean when defining the law: **a galaxy's recession speed is proportional to its distance from the observer**. An equation alone need not earn the full definition credit. For signed shifts, wavelength increases while frequency decreases; the printed equal-magnitude mnemonic must not reverse the physics. The inverse-age estimate, detailed CMB/nucleosynthesis, scale-factor calculus and Friedmann models extend the four listed outcomes.

### Cambridge 0625 — §6.2.3, Universe

**Core:** the Milky Way's approximate diameter is **100,000 light-years**; define redshift, recognise distant-galaxy spectral redshift, and explain how it supports expansion and the Big Bang. **Supplement:** CMBR and its expansion history; redshift-based recession speed; supernova brightness as a distance indicator; $H_0=v/d$; and $d/v=1/H_0$ as an age estimate. **Outcome 10 specifies $H_0=2.2\times10^{-18}$ s⁻¹**; know that syllabus value and use a question’s supplied value when given. The illustrative 70 km s⁻¹ Mpc⁻¹ above is not a replacement for the prescribed recall value. The light-year definition also belongs to §6.2.2. Core is assessed in Papers 1/3, Supplement in Papers 2/4.

The syllabus's shorthand “a specific frequency” refers to the characteristic microwave radiation: physically the CMB has a blackbody **spectrum**. Its “single point” rewind language expresses an early extremely compact, dense state; do not draw a privileged explosion site in an otherwise empty universe. This treatment completes the cosmology portion; it does not supply the separate stellar-evolution and Solar-System requirements.

### IB Physics and AP Physics — scope boundary

**Current IB Physics (first assessment 2025):** C.5 covers Doppler shifts and E.5 stellar evolution, but the guide does **not** prescribe Hubble's law, CMB cosmology or an expansion-age calculation as named content. Do not import the old optional astrophysics syllabus into the current course. This is enrichment beyond the related wave/stellar outcomes.

**AP Physics 1, AP Physics 2, AP Physics C: Mechanics, AP Physics C: Electricity and Magnetism:** Hubble/cosmology is not a named requirement in the current course and exam descriptions. Related wave, radiation, gravitation and data-analysis skills do not create a cosmology coverage claim. No AP/IB completion credit is assigned solely for this treatment.

## Connections

- **Prerequisites:** [[Doppler Effect]] — spectral shifts and the small-speed approximation; [[Stellar Luminosity and Size]] — independent distance measurements and blackbody radiation.
- **Historical companion:** [[Henrietta Leavitt and the Cosmic Yardstick]] — the work behind calibrated stellar distances.
- **Graph discipline:** [[Linearisation]] — why a change of axes changes the meaning of a gradient; [[Accuracy vs Precision]] — shared calibration errors.
- **Physical foundations:** [[Gravitational Fields]] — local bound systems; [[Nuclear Physics]] — early light-element reactions; [[Energy Levels and Line Spectra]] — identifying spectral lines.
- **Mathematics:** [[Differential Equations]] — an expansion rate is a differential law; [[Integration]] — age accumulates across the history.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $v=H_0d$ | `v=H_0d` | present Hubble flow |
| $H=a^{-1}\mathrm da/\mathrm dt$ | `H=a^{-1}\mathrm da/\mathrm dt` | fractional expansion rate |
| $1+z=a_0/a_e$ | `1+z=a_0/a_e` | cosmological wavelength stretch |
| $t_0=\int_0^1\mathrm da/[aH(a)]$ | `t_0=\int_0^1\mathrm da/[aH(a)]` | age for a specified history |
