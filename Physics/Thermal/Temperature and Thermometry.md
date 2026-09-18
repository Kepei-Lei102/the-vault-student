---
chinese: 温度与测温 (wēndù yǔ cèwēn)
aliases:
  - Thermometry
  - Thermometers
  - Thermal Equilibrium
prerequisites:
  - "[[Physical Quantities and Units]]"
  - "[[Kinetic Theory and the Ideal Gas]]"
leads_to:
  - "[[Heat Transfer]]"
teach_together:
  - "[[Calibration of Instruments]]"
  - "[[Specific Heat Capacity]]"
tags:
  - subject/physics
  - domain/thermal-physics
  - level/IGCSE
  - level/A-Level
  - level/university
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-14-1
  - syllabus/9702-14-2
  - type/deep
  - type/derivation
  - notation/thermometric-property
  - misconception/temperature-is-total-energy
  - misconception/two-points-guarantee-linearity
  - misconception/thermometer-instantaneous
---

# Temperature and Thermometry 温度与测温

> *A glass column grows longer. A metal wire becomes harder to drive current through. Two unlike wires produce a voltage. How can three different events all mean “50 degrees”?*

## Definition — temperature decides the direction

**Temperature** is a state quantity that determines the direction of spontaneous net thermal energy transfer: from higher temperature to lower temperature. Bodies in **thermal equilibrium** have equal temperatures and no net thermal energy transfer between them.

**Thermometry** is temperature measurement. A thermometer observes a **thermometric property**—a measurable quantity that changes reproducibly with temperature—and uses an established relation to turn that signal into a temperature reading.

The property is not the temperature itself. A resistance is measured in ohms, a liquid column in millimetres, an e.m.f. in volts; **calibration is the bridge from the signal to the temperature**. [[Calibration of Instruments]] explains how that bridge is checked against references and assigned an uncertainty.

### 中文锚点

把温度计刚放进温水，读数还在往上爬，并不一定是水越来越热，也可能是温度计自己还没暖过来。它不是隔空“看见”温度，而是等自己的液柱、电阻等性质随冷热改变，再把这种变化换成读数。所以测体温要等一会儿，烤箱探头也得放对位置：我们真正想知道的是被测物的温度，却只能先读到探头自己的状态。让两者足够接近，测量才有意义。

## 1. Why a third object can tell us about the first two

Suppose body A is in thermal equilibrium with a small thermometer C. You then find that body B is also in thermal equilibrium with C at the same reading. **A and B are in thermal equilibrium with each other.** This transitive property is the **zeroth law of thermodynamics**: it makes temperature a consistent label shared by different bodies.

Without it, a thermometer could agree with your water bath and your metal block while the bath and block disagreed with each other. Temperature would fail to be a usable common scale.

**No net transfer** does not mean that microscopic energy exchanges stop. At equilibrium, opposing transfers balance statistically. Nor does equal temperature mean equal internal energy: a bathtub and a teaspoon at 40 °C have different masses and energies. [[Internal Energy]] distinguishes the stored energy from the temperature.

For a classical ideal gas, [[Kinetic Theory and the Ideal Gas]] derives

$$\langle E_{k,\mathrm{translation}}\rangle=\frac32k_BT.$$

This connects temperature with molecular motion. It is not a universal definition that says every particle in every material owns the same total energy at a given temperature.

### A steady reading is not automatically equilibrium

A probe can settle to a constant reading while heat continuously enters from a heater and leaves through its stem. That is a **steady state**, possibly with a temperature gradient. A stable display is evidence worth checking; it is not proof that the probe and the target have the same temperature.

## 2. How a scale is attached to a signal

Let $X$ be a thermometric property. Suppose reference temperatures $\theta_1,\theta_2$ produce signals $X_1,X_2$. If the response is adequately linear over that interval,

$$X=X_1+m(\theta-\theta_1),\qquad m=\frac{X_2-X_1}{\theta_2-\theta_1}.$$

**Tool: the straight-line gradient. Trigger: two references and an assumed linear response.** Rearranging gives

$$\boxed{\theta=\theta_1+\frac{X-X_1}{X_2-X_1}(\theta_2-\theta_1).}$$

The fraction tells you how far through the signal interval you are; multiply by the temperature interval. For nominal 0 °C and 100 °C references,

$$\theta=100\frac{X-X_0}{X_{100}-X_0}\quad\text{in °C}.$$

The formula also works for a decreasing property: both numerator and denominator change sign. It fails if the reference signals are indistinguishable. Never silently extrapolate a fitted straight line beyond its verified range.

### Two points determine a line, not whether nature follows it

Consider the following **synthetic teaching sensors**, with $\theta$ the numerical Celsius temperature:

| Sensor | Signal law over 0–100 °C | Signal at 50 °C | Two-point linear indication |
|---|---|---|---|
| Liquid column | $L=10+0.4\theta$ mm | 30 mm | 50 °C |
| Metal resistance | $R=100+0.385\theta$ Ω | 119.25 Ω | 50 °C |
| Curved e.m.f. response | $E=0.04\theta+0.00008\theta(\theta-100)$ mV | 1.8 mV | 45 °C |

All three give the correct endpoint readings after linear calibration. The third fails between them because its curvature survives. These coefficients illustrate the issue; they are not a thermocouple reference table or a certified platinum sensor model.

![[thermometry-calibration.svg|800]]

*Endpoint-normalised signals share the same scale. The curved sensor passes both reference points but reads 5 °C low at the midpoint. An intermediate reference reveals the error; repeating either endpoint does not.*

A nonlinear response can still make an excellent thermometer. Use a verified calibration curve, lookup table or inverse function. **Nonlinear is not the same as inaccurate.** It means a straight-line conversion is inadequate.

## 3. The physical mechanisms — what actually changes?

### Liquid-in-glass: expansion converted into length

A fixed mass of liquid usually occupies a larger volume when warmed, so its density decreases. In a narrow capillary, a small extra volume becomes an easily visible column rise. Approximately,

$$\Delta V\approx\beta_{\mathrm{effective}}V_b\Delta\theta,\qquad
\Delta L=\frac{\Delta V}{A_c},$$

where $V_b$ is bulb liquid volume and $A_c$ is the capillary cross-sectional area. The **effective** expansion accounts for the glass expanding too; using only the liquid's expansion coefficient neglects that correction.

A larger bulb or narrower bore gives a larger length change per degree. But a larger bulb may take longer to reach equilibrium, while a narrower bore limits the temperature range fitting on a given stem. Uniform bore and a reproducible liquid response matter to the scale.

This is not “particles becoming bigger.” In liquids and solids, heating changes the average arrangement/separation through intermolecular interactions. In a dilute gas at constant pressure, higher molecular motion requires a larger volume to maintain that pressure. The detailed solid/liquid expansion coefficients depend on the material; water near freezing is a familiar exception to simple monotonic expansion.

### Gas thermometer: specify what you hold fixed

For fixed amount $n$, the ideal-gas equation gives

$$pV=nRT.$$

- **Constant pressure:** $V\propto T$. Measure volume.
- **Constant volume:** $p\propto T$. Measure pressure.

Both require **absolute temperature in kelvin**. Keep the amount of gas fixed too. A pressure reading in a leaking bulb is not a temperature measurement under this model.

Real gases depart from ideal behaviour, particularly near condensation. Dilute-gas measurements and extrapolation toward the low-density limit connect the method to a substance-independent thermodynamic scale; one finite-pressure gas bulb is not magically exact.

### Metal resistance thermometer: hotter lattice, altered scattering

For many metals near ordinary temperatures, warming increases the lattice vibrations and electrical resistance. Over a limited interval one may approximate

$$R(\theta)=R_0(1+\alpha\theta),$$

where $R_0$ is resistance at 0 °C and $\alpha$ has units °C⁻¹. Platinum's stable, reproducible response makes it useful for reference and industrial thermometry. A real calibrated resistance–temperature curve is more precise than treating this approximation as exact over every temperature.

The measuring current is a possible disturbance: $P=I^2R$ heats the sensor. Leads contribute resistance too. Small excitation currents and suitable lead-compensation arrangements reduce these errors. [BIPM/NIST guide: industrial platinum resistance thermometers](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=932587)

A **thermistor** is a different resistive sensor. A common negative-temperature-coefficient semiconductor thermistor has decreasing resistance with increasing temperature: the increase in available charge carriers dominates. Its strong, curved response can be useful for sensitive electronic measurements. [[Potential Dividers]] explains how a changing resistance can become a voltage for an electronic controller.

### Thermocouple: the reference end matters

Two dissimilar conductors spanning a temperature difference produce a net thermoelectric e.m.f. The signal depends on both measuring and reference temperatures. Over a restricted interval,

$$E\approx S(\theta_{\mathrm{hot}}-\theta_{\mathrm{ref}}),$$

where $S$ is the effective Seebeck coefficient for the pair. It is not generally constant over a broad range; actual instruments use appropriate reference functions.

The reference need not sit in ice: electronics can measure the terminal temperature and apply **reference-junction compensation**. But ignoring the reference altogether makes the inference incomplete. A hot junction alone is not an absolute-temperature voltage source. Small junctions can respond quickly; protective sheaths and installation change the response time. [NIST: thermocouple mechanism and reference temperature](https://www.nist.gov/pml/sensor-science/thermodynamic-metrology/mercury-thermometer-alternatives/mercury-thermometer-5)

### Radiation thermometer: no contact does not mean no assumptions

An infrared thermometer infers temperature from radiation received in its spectral band. This is valuable for moving or inaccessible surfaces, but emissivity, reflected surroundings, viewing geometry and the instrument's wavelength band matter. It usually measures a **surface**, not the interior temperature of an object. [[Stellar Luminosity and Size]] develops the blackbody spectrum; [[Electromagnetic Spectrum]] places infrared radiation in that picture.

## 4. Sensitivity, resolution, response and disturbance

These answer different questions:

| Quantity | Question | Example |
|---|---|---|
| Sensitivity $\mathrm dX/\mathrm d\theta$ | How much does the signal change per degree? | 0.4 mm per °C |
| Resolution | What is the smallest distinguishable change? | A display increments by 0.1 °C |
| Accuracy | How close is the result to the reference/true value? | Requires calibration and uncertainty, not just many digits |
| Response time | How quickly does the sensor follow a change? | A probe needs time to warm through |
| Measurement disturbance | How much does measuring change the target? | A cold probe cools a small warm sample |

If the signal uncertainty is $u_X$, local propagation gives $u_\theta\approx u_X/\lvert\mathrm dX/\mathrm d\theta\rvert$. A steeper response can improve temperature resolution for a given signal resolution, but it does not remove reference uncertainty or bias.

### Why the display needs time

In a simple **lumped thermal model**, the probe is nearly uniform internally, the bath is large and steady, the probe heat capacity is $C$ and its thermal conductance to the bath is $G$. Energy balance gives

$$C\frac{\mathrm dT_p}{\mathrm dt}=G(T_b-T_p).$$

**Trigger: the remaining temperature difference drives the rate. Tool: exponential relaxation.** With $\tau=C/G$,

$$\boxed{T_p(t)=T_b+[T_p(0)-T_b]e^{-t/\tau}.}$$

At one time constant, the remaining difference is $1/e\approx37\%$ of its initial value; after three, about 5% remains. A tolerance must specify what error is acceptable. Geometry, thermal contact, immersion and fluid movement affect $G$; sensor construction affects $C$. These assumptions fail for a probe with important internal gradients or a strongly changing environment.

![[thermometry-animation.mp4]]

*First: three synthetic signals, with the two linear responses overlapping after endpoint normalisation. Second: ideal probes initially at 20 °C enter a large 80 °C bath; illustrative time constants are 2, 6 and 10 s. These are model parameters, not a ranking of real thermometer technologies.*

### The probe can change what it measures

For an isolated sample and probe with constant heat capacities $C_s,C_p$, energy conservation gives

$$C_s(T_f-T_s)+C_p(T_f-T_p)=0,$$

$$\boxed{T_f=\frac{C_sT_s+C_pT_p}{C_s+C_p}.}$$

A 60 °C sample with heat capacity 4.2 J/K and a 20 °C probe with heat capacity 0.42 J/K equilibrate at **56.36 °C**. The probe correctly reports the disturbed final temperature, not the sample's original 60 °C. A small probe relative to the sample reduces this loading error. [[Specific Heat Capacity]]'s mixture calculation explains why.

## 5. Kelvin: a common scale beyond a particular substance

An empirical scale can depend on which property you declared linear. Thermodynamic temperature supplies a common physical scale independent of a chosen thermometer substance. Modern SI defines the kelvin by fixing

$$k_B=1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}\quad\text{exactly}.$$

The exact Celsius–kelvin offset is

$$\boxed{T/\mathrm K=\theta/{}^\circ\mathrm C+273.15.}$$

A temperature rise of 1 °C equals a rise of 1 K. But ratios require care: 40 °C is not twice the thermodynamic temperature of 20 °C; $313.15/293.15\approx1.068$. Write **K**, not °K.

Absolute zero is 0 K, or −273.15 °C. For the ordinary equilibrium systems considered here it is the lower limit. It is not a claim that every quantum system loses all motion or energy: ground-state energy can remain.

**The 2019 distinction:** the triple point of water formerly defined the kelvin. Today it remains a valuable reference, but its thermodynamic temperature is measured rather than fixed exactly by the SI definition. A fixed value assigned on a practical temperature scale must not be confused with exact knowledge of thermodynamic temperature. Definition and physical realisation are different jobs. [BIPM: kelvin definition history](https://www.bipm.org/en/history-si/kelvin)

### Why ice and boiling water need conditions

A well-prepared pure ice–water mixture near atmospheric pressure provides a useful approximate 0 °C reference. Boiling occurs when the saturation vapour pressure matches the surrounding pressure; at lower pressure it occurs at a lower temperature. “Boiling” does not automatically mean 100 °C.

Purity, pressure, immersion depth, heat leaks and equilibration affect a realised reference. For precision work, use the stated reference procedure and uncertainty. Calibration establishes a relation and its uncertainty; **adjustment** changes the instrument and may require recalibration. [International Vocabulary of Metrology: calibration](https://jcgm.bipm.org/vim/en/2.39.html)

## 6. Where it earns its keep

**An oven probe measures the probe first.** Put a room-temperature probe into a hot oven and its reading initially lags. Put it near a heating element and radiation can make its temperature differ from the surrounding air. Deciding whether you want air, surface or food-interior temperature comes before choosing and positioning the sensor.

**A temperature-controlled bath turns a voltage into a decision.** A controller reads a sensor, converts the signal through its calibration and adjusts heater power. An incorrect conversion shifts the actual bath temperature even if the display looks perfectly steady. [[Automated Systems and Robotics]] connects the measurement to feedback; the physical sensor and the software conversion are both part of the measurement chain.

**Industrial process measurements need the right compromise.** A fragile high-precision reference probe, a rugged thermocouple and a compact thermistor solve different problems. Range, chemical compatibility, drift, response and required uncertainty all matter. Choosing the most digits on the display is not an engineering specification. [NIST: industrial thermometer calibration](https://www.nist.gov/pml/sensor-science/thermodynamic-metrology/industrial-thermometer-calibrations)

## 7. Worked examples — the apparatus selects the equation

### A. Read what a gas thermometer actually measures

**Cambridge 9702/42/O/N/25 Q3(a), (b)(i–iv)**, paraphrased. A constant-volume gas bulb is connected to a liquid manometer with vacuum above the other liquid surface. The gas-side level X is restored to a fixed mark; the height difference measures gas pressure. X reads 2.31 cm; Y reads 8.69 cm at 0 °C, then 7.83 cm at an unknown temperature.

**Trigger: thermal contact and equilibrium. Tool: temperature equality.** The gas and its surroundings must reach the same temperature, with **no net thermal energy transfer** between them. The two clauses match the definition marks.

**Trigger: a column against vacuum. Tool: $p=\rho g\Delta h$.** The needed liquid property is **density**. Returning X to its mark holds gas volume fixed. If the other limb were open to atmosphere instead, its pressure would have to be included; $p=\rho g\Delta h$ alone would not be the absolute gas pressure.

**Trigger: fixed $n,V$. Tool: $p/T=\text{constant}$ in kelvin.** Here $p\propto\Delta h$, so

$$T=273.15\frac{7.83-2.31}{8.69-2.31}=236.33\ \mathrm K,$$

$$\theta=236.33-273.15=-36.82\,{}^\circ\mathrm C\approx\boxed{-37\,{}^\circ\mathrm C}.$$

The published scheme uses 273 K for the ice point and obtains the same rounded −37 °C. Using 7.83/8.69 would confuse scale readings with column-height differences; using a Celsius ratio would destroy the absolute-temperature relation.

**Apparatus judgment:** a bulky gas thermometer may respond slowly and significantly disturb a small sample. A large, steady-temperature environment or laboratory calibration is a more suitable use. These are alternatives accepted by the actual scheme, not universal properties of every temperature sensor.

### B. Equal temperatures do not require equal masses

**Cambridge 9702/42/F/M/25 Q3(a)(i)**, paraphrased. Two metal cuboids are in thermal contact and thermal equilibrium. What does this mean?

**Trigger: equilibrium, not equal dimensions or materials. Tool: the thermal-equilibrium definition.** They have the same temperature and no net thermal energy transfer between them. Their masses, heat capacities and internal energies need not match. The published scheme awards equal temperature and no net transfer.

### C. A correct signal, an incorrect conversion

**Original problem.** A signal reads 0 mV at 0 °C and 4 mV at 100 °C. It reads 1.8 mV in a reference bath known to be at 50 °C. What does a two-point linear conversion report?

**Trigger: endpoints define a line. Tool: interval fraction.** $\theta=100(1.8/4)=45$ °C, a −5 °C indication error. The endpoints alone cannot distinguish a straight response from a curved one. Use intermediate calibration evidence before blaming the reference bath or “correcting” all readings by a fixed 5 °C.

### D. How long until the probe is close enough?

**Original model problem.** A 20 °C probe with $\tau=6$ s enters a large 80 °C bath. When is its error below 1 °C?

**Trigger: a specified tolerance on an exponentially decaying gap. Tool: solve the inequality.**

$$60e^{-t/6}<1\quad\Longrightarrow\quad t>6\ln60\approx\boxed{24.6\ \mathrm s}.$$

“Wait one time constant” would leave about 22 °C of error here. A response-time specification is meaningful only together with its stated criterion and conditions.

## 8. Try it — predict the failure before running the model

Run the adjacent `thermometry-model.py` with Python and NumPy. It checks calibration endpoints and intermediate error, compares analytic sensor response with an independent numerical integration, and checks energy conservation for probe loading.

```bash
python3 thermometry-model.py
```

Before changing a parameter, predict:

1. Narrow the liquid capillary to half its cross-sectional area. What happens to length sensitivity? **It doubles**, under the stated expansion model.
2. Double probe heat capacity while keeping thermal conductance fixed. What happens to $\tau$? **It doubles**; the signal calibration need not change.
3. Check only the curved sensor's endpoints repeatedly. Will averaging reveal the midpoint bias? **No**; test an intermediate reference.
4. Warm both thermocouple ends by the same amount in the constant-$S$ approximation. What changes? **The e.m.f. stays the same**; it measures the difference in this model.

For a simple observation, place a digital probe in a stirred cup of comfortably warm water and record its approach to a stable reading. Keep the sensing part immersed as intended by the manufacturer. This tests response qualitatively; it does not calibrate absolute accuracy without a reference.

## Exam Notes

### Cambridge 9702 — A-Level §14.1–14.2

Canonical 2028–2030 syllabus, same content as 2025–2027. **§14.1.1–2:** net thermal transfer from hotter to colder regions and equal-temperature equilibrium. **§14.2.1–4:** properties varying with temperature—including liquid density, gas volume at constant pressure, metal resistance and thermocouple e.m.f.; substance-independent thermodynamic scale; Celsius/kelvin conversion; absolute zero. These are Paper 4 topics. The zeroth-law name, time-constant derivation and modern metrology are explanatory extensions.

When the question gives a different apparatus, derive its property relation: a **constant-volume** gas thermometer measures pressure even though the syllabus example names gas volume at **constant pressure**. State controlled variables. Use the supplied conversion precision; distinguish temperature changes from ratios.

### Cambridge 0625 — practical temperature measurement; related §2.2

The 2026–2028 syllabus lists thermal expansion at §2.2.1, specific heat capacity at §2.2.2, and melting/boiling/evaporation at §2.2.3. It does **not** prescribe the old standalone liquid-thermometer design/calibration unit or the detailed latent-heat equation as a named outcome. Temperature readings and apparatus choice remain practical skills for Papers 5/6. Thermocouple equations, Kelvin definition and gas-thermometer calculations here are enrichment beyond those IGCSE requirements.

The liquid-expansion mechanism supports §2.2.1, but does not by itself complete all its solid/liquid/gas applications or the broader phase-change outcomes. A thermometer may appear in an experiment without making every thermometer mechanism required knowledge.

### IB Physics — B.1 and coursewide skills

First assessment 2025: B.1 includes Kelvin/Celsius scales, equal-sized temperature changes on the two scales, microscopic temperature and the direction of resultant thermal transfer. Tools 1 includes temperature measurement and calibration of sensors. The detailed catalogue of thermometer mechanisms and SI realisation methods extends these requirements; it is not a separate compulsory thermometry unit.

### AP Physics

**AP Physics 2:** Topic 9.1 connects temperature with the kinetic model; Topic 9.3 covers thermal contact, hotter-to-colder net transfer and equilibrium. The complete 9.3 scope also names conduction, convection and radiation; a thermometer treatment alone does not replace those mechanisms. Calibration curves and response-time equations are extensions, not a separate thermometry topic.

**AP Physics 1, AP Physics C: Mechanics, AP Physics C: Electricity and Magnetism:** the current CEDs do not prescribe this thermal-physics/thermometer-mechanism treatment. Generic experimental reasoning or the use of resistance in a circuit does not create a thermometry content requirement.

## Connections

- **Prerequisites:** [[Physical Quantities and Units]] — quantity, unit and realisation; [[Kinetic Theory and the Ideal Gas]] — microscopic temperature and gas laws.
- **Teach together:** [[Calibration of Instruments]] — references, correction and traceability; [[Specific Heat Capacity]] — equilibration and measurement disturbance.
- **Sensor circuit:** [[Resistance]] and [[Potential Dividers]] — the physical response and its electrical readout.
- **Applications:** [[Automated Systems and Robotics]] — feedback depends on a meaningful measurement; [[Stellar Luminosity and Size]] — radiation as a non-contact thermometer.
- **Mathematics:** [[Exponential Growth and Decay]] — response time; [[Linearisation]] — distinguish a model from its plotted coordinates.

## LaTeX Reference

| Expression | LaTeX | Meaning |
|---|---|---|
| $T/\mathrm K=\theta/{}^\circ\mathrm C+273.15$ | `T/\mathrm K=\theta/{}^\circ\mathrm C+273.15` | Absolute scale conversion |
| $\theta=\theta_1+(X-X_1)(\theta_2-\theta_1)/(X_2-X_1)$ | `\theta=\theta_1+(X-X_1)(\theta_2-\theta_1)/(X_2-X_1)` | Linear calibration |
| $\tau=C/G$ | `\tau=C/G` | Lumped thermal time constant |
| $T_p=T_b+(T_i-T_b)e^{-t/\tau}$ | `T_p=T_b+(T_i-T_b)e^{-t/\tau}` | Probe response |
