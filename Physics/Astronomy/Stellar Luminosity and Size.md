---
chinese: 恒星的光度与大小 (héngxīng de guāngdù yǔ dàxiǎo)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Electromagnetic Spectrum]]"
leads_to:
  - "[[Hubble's Law and the Expanding Universe]]"
teach_together:
  - "[[Henrietta Leavitt and the Cosmic Yardstick]]"
  - "[[Energy Levels and Line Spectra]]"
tags:
  - subject/physics
  - domain/astronomy
  - domain/thermal-physics
  - level/A-Level
  - level/IB
  - level/AP
  - level/university
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-25-1
  - syllabus/9702-25-2
  - type/deep
  - type/derivation
  - notation/luminosity
  - notation/radiant-flux-intensity
  - misconception/brightness-is-luminosity
  - misconception/red-stars-are-hotter
  - misconception/peak-height-is-total-power
---

# Stellar Luminosity and Size 恒星的光度与大小

> *A star arrives as a dot. No ruler reaches it, no thermometer touches it, and a brighter dot might simply be closer. Yet its light lets us infer its temperature, power output and radius. The trick is to ask which part of the measurement each unknown can change.*

## Definition

### Formal — distinguish the source from the measurement

**Luminosity $L$** is the total radiant power emitted by a source: energy per second, summed over all wavelengths and directions. Its unit is the **watt**, not watts per square metre.

**Radiant flux intensity $F$**, or **apparent brightness**, is the radiant power received per unit area perpendicular to the incoming light. Its unit is $\mathrm{W\,m^{-2}}$. Here it is integrated over all wavelengths: **bolometric** flux. A measurement through one optical filter is a different, restricted quantity.

A **standard candle** is an object whose luminosity is known or can be inferred from a calibrated property. Comparing that luminosity with received flux gives a distance under the propagation model.

### Intuitive — three independent controls

- **Distance:** move the same star farther away. The same power spreads over more area; received flux falls.
- **Radius:** enlarge a star at the same surface temperature. More emitting area produces more luminosity.
- **Temperature:** heat a star of the same radius. Each square metre emits more power, and its spectrum changes shape.

A distant stadium floodlight can look fainter than a nearby torch. Brightness alone does not decide which source is more powerful. For stars, a spectrum supplies information that a single brightness number cannot.

### 中文锚点

夜里看远处的灯，一盏显得暗，可能是灯本身功率小，也可能只是离你远。看恒星也是一样：眼睛收到的亮，不等于它本来发出的多。光一路向外散开，同一颗星离我们越远，分到每平方米上的能量就越少。若能先弄清它本身发光有多强，就能反过来估算距离。天文学家的本事之一，就是从“看起来亮不亮”里，把天体自身的性质和远近分开。

## Notation

| Symbol | Meaning | SI unit / caution |
|---|---|---|
| $L$ | Total luminosity | W; all wavelengths unless a band is specified |
| $F$ | Received bolometric flux | W m$^{-2}$; IB often writes $b$ |
| $R$ | Stellar radius | m; do not confuse with distance $d$ |
| $d$ | Distance from star's centre to observer | m in the basic inverse-square model |
| $T$ | Surface/effective temperature | **Kelvin**, not Celsius |
| $\lambda_{\max}$ | Peak of power **per unit wavelength** | m; not an absorption-line wavelength |
| $b_W$ | Wien displacement constant | $2.898\times10^{-3}\ \mathrm{m\,K}$; distinct from IB brightness $b$ |
| $\sigma$ | Stefan–Boltzmann constant | $5.670\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$ |
| $M_\lambda$ | Emitted surface power per area per wavelength | W m$^{-3}$ when wavelength is in metres |

## Key Facts — turn light into measurements

### 1. Inverse square is conservation plus geometry

Imagine surrounding an isolated, isotropically radiating star with a transparent sphere of radius $d$. In a steady state, with no intervening absorption, the full luminosity crosses that sphere. Its area is $4\pi d^2$, so

$$L=F(4\pi d^2)\quad\Longrightarrow\quad\boxed{F=\frac{L}{4\pi d^2}.}$$

The photons have not each become four times less energetic when $d$ doubles. Four times the area shares the same outgoing power. [[Progressive Waves]] gives the same geometric argument for a point source.

**Assumptions:** isotropic emission, unobstructed propagation, observer far enough away to treat the source as unresolved, and a consistent all-wavelength definition of $L$ and $F$. At cosmological distances the same-looking relation defines a **luminosity distance**; it is not automatically an ordinary Euclidean ruler distance.

For two observations,

$$\frac{F_2}{F_1}=\frac{L_2}{L_1}\left(\frac{d_1}{d_2}\right)^2.$$

Only when the luminosities match may brightness alone supply the distance ratio. Two equally bright stars need not be equally distant.

### 2. A standard candle supplies the missing information

One equation with unknown $L$ and $d$ cannot determine both. A calibrated standard candle supplies $L$, allowing

$$\boxed{d=\sqrt{\frac{L}{4\pi F}}.}$$

The observational chain is: identify a suitable object in the galaxy → infer its luminosity from a calibration → measure its received flux → correct relevant propagation/detector effects → solve for distance.

**Cepheid variables** make a useful example. They pulsate; a calibrated relation between pulsation period and luminosity makes the period informative about intrinsic output. “Standard” does not mean every Cepheid has identical luminosity or constant brightness. Nearby geometric distances calibrate the relation before it is applied farther away. Cepheids can in turn calibrate more luminous distance indicators such as Type Ia supernovae; actual supernova work standardises their light curves rather than assuming every explosion is identical. [ESA/Hubble's distance-ladder explanation](https://esahubble.org/images/opo1812a/).

A standard candle does not eliminate uncertainty. Dust can dim the light, several unresolved stars can blend together, and calibration may depend on the population and observing band.

### 3. What a blackbody actually means

A **blackbody** absorbs all radiation incident on it at every wavelength. In thermal equilibrium its emitted spectrum depends only on temperature. “Black” describes perfect absorption, not a promise that a hot blackbody looks dark.

A star's broad continuum can often be approximated by a blackbody, with spectral lines superimposed by its atmosphere. The approximation carries useful information without making a real stellar atmosphere an ideal surface. **Effective temperature** is defined by the total outgoing surface flux being $\sigma T_{\rm eff}^4$; a temperature fitted from a spectral colour or peak need not equal it exactly for a non-blackbody star.

The thermal spectrum is continuous: there is radiation across a range of wavelengths. The tallest point is not “the only colour emitted”. [[Energy Levels and Line Spectra]] explains the narrow lines; those lines identify transitions and species, while the broad continuum constrains temperature.

![[stellar-blackbody-spectra.svg|800]]

The vertical axis is power **per unit area per unit wavelength**. The area under the whole curve, not its peak height, gives total surface power per area. The three curves use the same units and scale.

### 4. Wien's law reads the horizontal position of the peak

For a blackbody spectrum expressed per unit wavelength,

$$\boxed{\lambda_{\max}T=b_W\approx2.898\times10^{-3}\ \mathrm{m\,K}.}$$

Hotter means a shorter peak wavelength. If temperature doubles, the peak wavelength halves. The model also predicts **more** radiation at every fixed wavelength, including red wavelengths: “bluer” does not mean the red part switches off.

The 5800 K Sun has a peak near 500 nm in this representation. That does not make sunlight monochromatic green. Its broad visible spectrum and the eye's combined response matter. Nor is the continuum peak the same thing as a shifted hydrogen line: Wien probes temperature; [[Doppler Effect]] probes relative motion or propagation-related wavelength shifts.

An object at 300 K peaks near $9.7\ \mu\mathrm m$, in the infrared. Thermal radiation is present even when an object does not visibly glow.

### 5. Stefan–Boltzmann reads the area under the spectrum

Integrating the blackbody spectrum over wavelength gives surface radiant exitance

$$M=\int_0^\infty M_\lambda\,d\lambda=\sigma T^4.$$

Multiply by the star's **whole emitting surface**, $4\pi R^2$:

$$\boxed{L=4\pi R^2\sigma T^4.}$$

It is not $\pi R^2$: that is the projected disc area, not the surface emitting into space. The fourth power means doubling absolute temperature multiplies surface emission by sixteen; doubling radius multiplies area and luminosity by four.

The $T^4$ is a physical radiation law, not a consequence of spherical geometry. The sphere supplies $4\pi R^2$; the spectrum supplies $\sigma T^4$. The quantum derivation of the scaling appears below.

![[stellar-three-controls.svg|800]]

For comparisons, divide by a reference star:

$$\boxed{\frac{L}{L_0}=\left(\frac{R}{R_0}\right)^2\left(\frac{T}{T_0}\right)^4.}$$

A star at half the reference temperature and 100 times its luminosity must have radius $\sqrt{100}/(1/2)^2=40$ times the reference radius. Cool can be luminous when the emitting area is large.

### 6. Combine the measurements to infer radius

Once $T$ and $L$ are known,

$$\boxed{R=\sqrt{\frac{L}{4\pi\sigma T^4}}.}$$

If the measured quantities are distance, bolometric flux and peak wavelength, combine the chain:

$$T=\frac{b_W}{\lambda_{\max}},\qquad L=4\pi d^2F,\qquad
\boxed{R=d\sqrt{\frac{F}{\sigma T^4}}.}$$

**What if distance is unknown?** Flux and temperature give $R/d=\sqrt{F/(\sigma T^4)}$, an angular-size scale, not a physical radius. Doubling both $R$ and $d$ at fixed $T$ leaves the observed flux unchanged. That degeneracy is a property of the information, not a failure of algebra.

![[stellar-controls.mp4]]

The animation changes one control at a time. Star colours are illustrative, not a calibrated visual-colour simulation; the luminosity/flux readouts and spectral curves follow the equations. Geometric distances and radii are represented schematically.

## Worked Examples — identify what each observation supplies

### 1. Standard-candle reasoning — Cambridge explanation

**9702/42/F/M/25, Q10(a)(i–ii), p.26; mark scheme p.14.** Paraphrased: define luminosity and explain how standard candles give the distance to a galaxy. [1 + 3 marks]

1. **Trigger: asks about the source → tool: luminosity definition.** Total radiant energy emitted per second, in watts.
2. **Trigger: distance is unknown → tool: calibrated intrinsic output.** A standard candle has known luminosity $L$.
3. **Tool: observation.** Measure radiant flux intensity $F$ at the observer.
4. **Tool: conservation and spherical spreading.** Use $F=L/(4\pi d^2)$ to calculate $d$.

The last three statements are separate scheme points. “It is bright, so we know how far away it is” leaves the calibration and measurement unstated.

### 2. Two graphs, three properties — Cambridge inference

**9702/41/O/N/25, Q9(a–b), p.20; mark scheme p.16.** The paper supplies an $F$ versus $d^{-2}$ graph for star X, plus emission spectra for X and the Sun. It asks for Wien's law and three conclusions about X. [2 + 3 marks]

The following values are approximate readings from those printed graphs: at $d^{-2}=3.0\times10^{-23}\ \mathrm{m^{-2}}$, $F\approx6.4\times10^3\ \mathrm{W\,m^{-2}}$; the peaks are about $4.5\times10^{-7}\ \mathrm m$ for X and $5.5\times10^{-7}\ \mathrm m$ for the Sun. The supplied solar surface temperature is 5770 K.

1. **Trigger: graph is $F$ against $d^{-2}$ → tool: straight-line gradient.** Since $F=[L/(4\pi)]d^{-2}$, the gradient is $L/(4\pi)$, not $L$:

$$L_X\approx4\pi\frac{6.4\times10^3}{3.0\times10^{-23}}=2.68\times10^{27}\ \mathrm W.$$

2. **Trigger: compare wavelength peaks → tool: Wien ratio.** $T_X/T_\odot=\lambda_{\max,\odot}/\lambda_{\max,X}$, giving $T_X\approx5770(5.5/4.5)\approx7.0\times10^3\ \mathrm K$. X is hotter than the Sun.
3. **Trigger: luminosity and temperature now known → tool: Stefan–Boltzmann inversion.** With graph-rounded $T_X=7000\ \mathrm K$,

$$R_X\approx\sqrt{\frac{2.68\times10^{27}}{4\pi(5.67\times10^{-8})(7000)^4}}\approx1.3\times10^9\ \mathrm m.$$

The scheme accepts temperature/hotter, greater luminosity, $L_X\approx2.7\times10^{27}$ W, and $R_X\approx1.3\times10^9$ m as possible conclusions. These are graph estimates; extra calculator digits do not create extra measurement precision. Total luminosity comes from an integrated spectrum or the inverse-square graph, not peak height alone.

### 3. Nuclear power becomes surface temperature — Cambridge transfer

**9702/42/O/N/25, Q9(c)(i–ii), p.21; mark scheme p.16.** Sirius has radius $1.19\times10^9$ m; the question gives a fusion mass-loss rate of $1.09\times10^{11}$ kg s$^{-1}$ and assumes this power equals radiated power. Find luminosity and surface temperature. [2 + 2 marks]

1. **Trigger: mass converted per second → tool: $E=mc^2$ per unit time.** $L=(1.09\times10^{11})(3.00\times10^8)^2=9.81\times10^{27}\ \mathrm W$.
2. **Trigger: $L$ and $R$ known → tool: solve the fourth-power law.**

$$T=\left[\frac{9.81\times10^{27}}{4\pi(5.67\times10^{-8})(1.19\times10^9)^2}\right]^{1/4}\approx9930\ \mathrm K.$$

Take a fourth root, not a square root. This uses the paper's stated energy-balance assumption; mass carried away by a stellar wind would not automatically turn into photon luminosity.

### 4. The Sun's peak — current IB question

**IB Physics HL, May 2025 TZ2, Paper 2, Q7(d), printed p.18 (PDF p.19); mark scheme p.17.** Given solar surface temperature 5800 K, determine the peak wavelength. [2 marks]

**Trigger: thermal continuum peak → tool: Wien's law.** $\lambda_{\max}=(2.9\times10^{-3})/5800=5.0\times10^{-7}\ \mathrm m=500\ \mathrm{nm}$. The scheme credits the relationship and the result. This is not the wavelength of a particular atomic transition.

### 5. A complete recovery — original synthetic observation

An ideal blackbody star is 20 pc away, has received bolometric flux $3.2\times10^{-10}$ W m$^{-2}$, and peaks at 500 nm. Use $1\ \mathrm{pc}=3.086\times10^{16}$ m.

**Tool sequence:** peak → temperature, distance plus flux → luminosity, luminosity plus temperature → radius. The result is $T\approx5800$ K, $L\approx1.53\times10^{27}$ W and $R\approx1.38\times10^9$ m. The adjacent Python model reproduces the calculation and generates different test stars instead of memorising this answer.

## Where this is the working tool

**Stellar surveys actually use this chain.** Gaia's DR2 parameter pipeline combined photometry and parallax to infer temperature and luminosity, then obtained radius using Stefan–Boltzmann. Its documentation also exposes a real limitation: colours can confuse a cooler star with a hotter star reddened by dust, and the available measurements do not always separate them reliably. This is a documented example from that release, not a claim that every Gaia product uses an identical method. [ESA Gaia DR2 processing description](https://gea.esac.esa.int/archive/documentation/GDR2/Data_analysis/chap_cu8par/sec_cu8par_intro/ssec_cu8par_intro_whatsdone.html).

**Non-contact thermometry uses the same radiation–temperature link.** A radiation thermometer measures in a chosen wavelength band and compares with a calibration; it need not locate the whole spectrum's peak. NIST calibrates such instruments against well-characterised blackbody sources. Real surfaces require attention to emissivity and reflected background radiation, so a shiny surface can mislead a naive temperature inference. [NIST radiance-temperature laboratory](https://www.nist.gov/laboratories/tools-instruments/radiance-temperature-calibration-laboratory), [NIST emissivity measurement facility](https://www.nist.gov/laboratories/tools-instruments/system-infrared-spectral-emittance-materials).

## Try It — change the hidden star

Run `python3 stellar-model.py` with NumPy 2 or later. The model uses SI units and no catalogue data.

- Predict the effect of doubling $d$, $R$ or $T$ separately; then call `flux(R,T,d)` and `luminosity(R,T)` to check.
- Invent a star, generate its flux and peak, then recover it with `infer(peak,flux,distance)`. Change all three inputs; the built-in test does this 1,000 times.
- Hold $T$ fixed and multiply both $R$ and $d$ by three. Explain why the same received spectrum cannot distinguish these stars without a separate distance measurement.
- Transmit only one quarter of the light through an ideal grey screen. If you ignore that screen and use a known luminosity, what distance will you infer? **Twice the true distance.** The code checks it.
- Integrate `spectrum(wavelength,T)` numerically and compare with $\sigma T^4$. A narrow wavelength interval misses power; changing units from per metre to per nanometre requires the corresponding factor $10^{-9}$ on the vertical axis.

## Common Misconceptions

- **“A brighter star is more luminous.”** Only after distance and relevant attenuation are accounted for.
- **“Use the star's radius in inverse square.”** At Earth, spreading uses the source–observer distance $d$; surface emission uses $R$.
- **“Red-hot means hotter than blue.”** Thermal red stars are cooler than blue stars; everyday colour symbolism reverses the physics.
- **“A blackbody does not emit.”** It is a perfect absorber and a thermal emitter; a hot one can glow.
- **“The graph's peak height is luminosity.”** Integrate over wavelength and account for what area the vertical axis refers to.
- **“Wien gives the core temperature.”** It concerns the emitting surface/continuum approximation; nuclear-burning cores are much hotter.
- **“Kelvin is optional in a ratio.”** $6000/3000=2$ is the temperature ratio; subtracting 273 from each first changes the physics.
- **“Flux and colour uniquely determine radius.”** They constrain $R/d$ under the model; physical size still needs distance.

## Exam Notes

### Cambridge 9702 — §25.1–25.2

The 2028–30 syllabus (printed p.38; same outcomes as 2025–27) requires luminosity, $F=L/(4\pi d^2)$, standard candles and galaxy distances; Wien's law, Stefan–Boltzmann and combined radius estimation. All seven outcomes are addressed. The syllabus says **recall and use** inverse square and Wien's proportionality; it says **use** Stefan–Boltzmann. Practise reconstructing the relationships instead of assuming a formula will be supplied.

A graph of $F$ against $d^{-2}$ has gradient $L/(4\pi)$. Read axis multipliers before using the gradient. Explain Wien using **absolute surface temperature** and the wavelength of **maximum spectral emission**, not any arbitrary wavelength. Detailed Planck calculus, magnitude systems and Cepheid calibration physics are extensions. Hubble expansion/age calculations belong to §25.3 and are not completed by these stellar measurements.

### IB Physics — first assessment 2025

**B.1 Thermal energy transfers** includes blackbody spectra, Wien, luminosity and apparent brightness. **E.5 Fusion and stars** includes stellar radii from luminosity and surface temperature and distances by parallax. The guide explicitly says Cepheid variables are not required. Its usual apparent-brightness symbol $b$ is our $F$; do not confuse it with $b_W$.

The radiation and radius outcomes are taught here; stellar evolution, full HR-diagram interpretation and parallax require their own treatment. Conduction and convection in B.1 are not automatically covered because radiation is.

### AP Physics 2 — §15.4 Blackbody Radiation

Includes thermal electromagnetic emission, ideal absorption, continuous temperature-dependent spectra, why classical physics fails and Planck's quantisation, Wien's peak shift and surface-area/$T^4$ dependence. The current CED lists the relevant equations and constants. The Planck calculus below explains the laws but is beyond the algebra-based calculation scope. Stellar distance-ladder calibration is not a named AP requirement.

### Cambridge 0625; AP Physics 1 and both AP Physics C courses

0625 §6 provides the Sun/stars/universe context and brightness-based supernova distance context, but does not prescribe quantitative Wien/Stefan–Boltzmann stellar-radius inference. Its thermal-radiation outcomes are qualitative. AP Physics 1 and AP Physics C Mechanics/E&M do not prescribe this blackbody/stellar-measurement topic.

**Not prescribed on these boards:** the full quantitative stellar chain on 0625, AP Physics 1, AP C Mechanics or AP C E&M. The complete 0625 astronomy row is not claimed from this treatment.

## Beyond Syllabus — why the laws fit together

### Planck's spectrum contains both scaling laws

Recall that $M_\lambda\,d\lambda$ is surface radiant power per unit area in a small wavelength interval. The blackbody result is

$$M_\lambda(T)=\frac{2\pi hc^2}{\lambda^5}\frac{1}{e^{hc/(\lambda k_BT)}-1}.$$

Here the hemisphere's angular integration is already included; spectral **radiance** $B_\lambda$ uses $2hc^2$ instead. Planck's quantised energy exchange supplies the denominator. Classical equipartition instead predicts excessive short-wavelength radiation and an infinite integrated output—the ultraviolet catastrophe. [OpenStax's blackbody treatment](https://openstax.org/books/university-physics-volume-3/pages/6-1-blackbody-radiation).

Set $x=hc/(\lambda k_BT)$. Then $\lambda=hc/(k_BTx)$ and $\lvert d\lambda\rvert=[hc/(k_BT)]x^{-2}dx$. Substitution gives

$$M=\frac{2\pi k_B^4T^4}{h^3c^2}\int_0^\infty\frac{x^3}{e^x-1}\,dx.$$

Everything inside the integral is dimensionless and temperature-independent: this is **why the total scales as $T^4$**. To evaluate it, expand $(e^x-1)^{-1}=\sum_{n=1}^\infty e^{-nx}$. Positive terms allow termwise integration; repeated integration by parts gives $\int_0^\infty x^3e^{-nx}dx=6/n^4$. Using $\sum n^{-4}=\pi^4/90$ yields the integral $\pi^4/15$ and

$$\sigma=\frac{2\pi^5k_B^4}{15h^3c^2}.$$

For the wavelength peak, maximising $x^5/(e^x-1)$ gives $5(1-e^{-x})=x$. Its positive interior root is $x\approx4.9651$; hence $\lambda_{\max}T=hc/(4.9651k_B)$, Wien's constant. The zero root is an endpoint limit, not the finite-temperature spectral peak.

**Representation matters.** A spectrum per unit frequency has a different vertical density and a different peak. Converting the wavelength peak with $f=c/\lambda_{\max}$ does not locate the maximum of the per-frequency spectrum: the Jacobian changes the weighting. Always read both axes.

### Missing light and uncertain temperatures

Recall $F=L/(4\pi d^2)$. With grey transmission $0<a<1$, $F_{\rm obs}=aL/(4\pi d^2)$. Ignoring attenuation gives $d_{\rm inferred}=d/\sqrt a$: dimming masquerades as distance. Wavelength-dependent extinction also changes colour and can bias temperature. A one-filter measurement requires a bolometric correction before being used as all-wavelength flux.

From $R=dF^{1/2}\sigma^{-1/2}T^{-2}$, logarithmic differentiation gives

$$\frac{dR}{R}=\frac{dd}{d}+\frac12\frac{dF}{F}-2\frac{dT}{T}.$$

These are signed small changes. For independent standard uncertainties, square the sensitivities and add variances; for worst-case bounds, add magnitudes. Correlated quantities need covariance. A temperature error of 1% alone produces an approximately 2% radius error in the opposite direction when $F,d$ are held fixed. [[Error Propagation]] explains the bookkeeping.

### Magnitudes encode ratios logarithmically

Recall that brightness ratios contain distance information once luminosity is known. Astronomers define a magnitude difference by $m_2-m_1=-2.5\log_{10}(F_2/F_1)$ in the same band. Five magnitudes corresponds to a factor 100 in flux. Defining absolute magnitude $M$ as the apparent magnitude at 10 pc gives, without extinction,

$$m-M=5\log_{10}\!\left(\frac{d}{10\ \mathrm{pc}}\right).$$

It is the inverse-square law written on a logarithmic scale, not an independent distance law. A band-specific extinction $A$ adds to the right side. Consistent observing bands, calibrations and luminosity definitions still matter.

## Connections

- **Historical companion:** [[Henrietta Leavitt and the Cosmic Yardstick]] — glass plates, the period–luminosity relation and the calibration that makes it a ruler.

- **Builds on:** [[Progressive Waves]] — power spread over area; [[Electromagnetic Spectrum]] — wavelength and thermal radiation.
- **Companion:** [[Energy Levels and Line Spectra]] — lines reveal composition; continuum shape constrains temperature.
- **Next inference:** [[Hubble's Law and the Expanding Universe]] — distances combined with redshifts; [[Doppler Effect]] supplies the spectral-shift measurement.
- **Energy source:** [[Nuclear Physics]] — fusion and mass–energy; surface temperature is not core temperature.
- **Mathematics:** [[Integration]] — area under a spectral density; [[Logarithms]] — magnitude ratios; [[Error Propagation]] — what uncertainty does to inferred size.
- **Experimental judgment:** [[Accuracy vs Precision]] — repeated measurements cannot remove an unmodelled calibration bias.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $F=L/(4\pi d^2)$ | `F=L/(4\pi d^2)` | emitted power spread over a sphere |
| $\lambda_{\max}T=b_W$ | `\lambda_{\max}T=b_W` | wavelength-peak temperature relation |
| $L=4\pi R^2\sigma T^4$ | `L=4\pi R^2\sigma T^4` | emitting area times surface power density |
| $R/d=\sqrt{F/(\sigma T^4)}$ | `R/d=\sqrt{F/(\sigma T^4)}` | angular-size constraint without a known distance |
