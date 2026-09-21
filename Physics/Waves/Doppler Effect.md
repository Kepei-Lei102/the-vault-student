---
chinese: 多普勒效应 (duōpǔlè xiàoyìng)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Energy Levels and Line Spectra]]"
  - "[[Sound]]"
leads_to:
  - "[[Special Relativity]]"
  - "[[Hubble's Law and the Expanding Universe]]"
teach_together:
  - "[[Ultrasound]]"
tags:
  - subject/physics
  - domain/waves
  - domain/astronomy
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-7-3
  - syllabus/9702-25-3
  - syllabus/0625-6-2
  - syllabus/IB-Physics-C-5-1
  - syllabus/IB-Physics-C-5-2
  - syllabus/AP-Physics-2-14-5
  - type/deep
  - type/derivation
  - misconception/moving-source-makes-sound-faster
  - misconception/doppler-measures-total-speed
  - misconception/redshift-means-visibly-red
---

# Doppler Effect 多普勒效应

> A siren can keep playing the same note while you hear its pitch fall as it passes. The driver did not change the note: the journey between one vibration and your ear changed. The same idea lets us measure blood flow without opening a vessel, read winds inside a storm, and detect a planet through its star's wobble.

## Definition

### Formal

The **Doppler effect** is a change in the observed frequency of a wave caused by motion of the source or observer. For sound in a uniform, stationary medium, a source moving directly towards a stationary observer with speed $u_s<v$ gives

$$\boxed{f_o=f_s\frac{v}{v-u_s}},$$

where $f_s$ is the source frequency, $f_o$ the observed frequency and $v$ the sound speed **relative to the medium**. Recession changes the denominator to $v+u_s$. These are source-motion formulas for mechanical waves, not universal formulas for light.

### Intuitive

Frequency counts arrivals per second. You can increase the arrival rate in two ways: **put wavefronts closer together**, or **move into them faster**. A moving source does the first; a moving observer does the second. The vibration rate at the source need not change.

### 中文锚点

救护车驶近时，警笛听起来尖一些；驶过以后，声音一下低了。司机不必换一种警笛：车向你开来时，下一道声波从更靠近你的位置出发，相邻波面之间的距离变小，你每秒收到的波更多；车远去时，波与波拉开距离，你每秒收到的就少了。这就是多普勒效应——变的是你接收到的节奏，不一定是声源自己的振动节奏，也不只是声音变大或变小。

## Notation and assumptions

| Symbol | Meaning | Keep separate |
|---|---|---|
| $f_s$, $T_s=1/f_s$ | Emitted frequency and period | What the source produces |
| $f_o$, $T_o=1/f_o$ | Received frequency and period | What the observer measures |
| $v$ | Mechanical-wave speed relative to the medium | Not $v+u_s$ just because the source moves |
| $u_s$, $u_o$ | Source speed, observer speed relative to the medium | Nonnegative magnitudes in the approach/recession formulas |
| $\lambda$ | Wavefront spacing measured in the medium | Changes ahead/behind a moving source |
| $c$ | Light speed in vacuum | Invariant in inertial frames |
| $v_r$ | Radial velocity, positive for recession | Component along the line of sight |
| $z$ | $(\lambda_o-\lambda_0)/\lambda_0$ | Dimensionless redshift; negative for blueshift |

Start with a still, uniform medium, constant source frequency, and motion along the source–observer line. Source speeds are subsonic. We will relax the line-of-sight restriction later. For a longitudinal sound wave, a wavefront can represent a surface of equal compression phase; the circles in a diagram are not material rings carried outwards by the source.

## 1. A stationary source: one cycle, one wavelength

![[doppler-see-it-move.mp4]]

Watch each crest expand from its emission point. Then compare a moving source, which changes the spacing, with a moving observer, which changes the encounter rate.

[[Progressive Waves]] gives $v=f\lambda$. In one source period $T_s$, a crest travels $vT_s$. The next crest starts at the same location, so their separation is

$$\lambda_0=vT_s=\frac{v}{f_s}.$$

A stationary observer receives $v/\lambda_0=f_s$ crests each second. Now keep the vibration clock unchanged and move the source.

## 2. A moving source changes the spacing

### Derive the approaching-source result

**Step 1 — trigger: two consecutive emissions. Tool: distance = speed × time.** During one period $T_s$, the first crest advances $vT_s$. The source advances $u_sT_s$ in the same direction before releasing the next crest.

**Step 2 — tool: subtract positions along the ray.** The second crest begins closer to the first, leaving

$$\lambda_{\rm ahead}=vT_s-u_sT_s=(v-u_s)T_s=\frac{v-u_s}{f_s}.$$

**Step 3 — trigger: the observer is stationary in the medium. Tool: arrival rate = wave speed / spacing.**

$$f_o=\frac{v}{\lambda_{\rm ahead}}=\boxed{f_s\frac{v}{v-u_s}}.$$

Since the denominator is smaller than $v$, $f_o>f_s$. The source did not produce extra crests; the travel time decreases for successive crests, so they arrive closer together in time.

### Behind the source

The source moves away from the previous backward-going crest. The spacing is now

$$\lambda_{\rm behind}=(v+u_s)T_s,\qquad \boxed{f_o=f_s\frac{v}{v+u_s}<f_s}.$$

**The useful sign rule is the physics:** approaching means compressed wavefronts, hence a smaller denominator and a higher received frequency. Receding means stretched wavefronts. Only after that reasoning does “minus for approach” become a mnemonic worth keeping.

![[doppler-wavefronts.svg|720]]

Every circle is centred on the source's position **when that crest was emitted**. A crest already travelling through the medium does not keep following the source. Drawing all circles around the source's present position erases the mechanism you are trying to explain.

### The same derivation without a wavefront picture

Let consecutive emissions occur at times $t_e$ and $t_e+T_s$. If their travel distances are $R$ and $R-u_sT_s$, their arrival-time separation is

$$T_o=\left(t_e+T_s+\frac{R-u_sT_s}{v}\right)-\left(t_e+\frac Rv\right)=T_s\left(1-\frac{u_s}{v}\right).$$

Taking reciprocals gives the same frequency formula. This version explains *why distance itself is not the Doppler cause*: a constant extra distance delays every crest equally. A changing distance changes the spacing between arrivals.

## 3. A moving observer changes the encounter rate

Keep the source stationary. The wavefront spacing stays $\lambda_0=v/f_s$. An observer moving towards the source at speed $u_o$ meets the advancing wavefronts at speed $v+u_o$ relative to themselves. Therefore

$$\boxed{f_o=\frac{v+u_o}{\lambda_0}=f_s\frac{v+u_o}{v}}.$$

Moving away instead gives $f_o=f_s(v-u_o)/v$, assuming the observer is slower than the waves and the usual arrival ordering holds. The observer's motion has not compressed the sound field in the medium; it has changed which wavefronts the observer encounters per second.

| Change, same approach speed $u$ | Formula | What changed physically? |
|---|---|---|
| Source approaches; observer fixed | $f_o/f_s=1/(1-u/v)$ | Spatial wavefront spacing |
| Observer approaches; source fixed | $f_o/f_s=1+u/v$ | Wavefront encounter speed |

At $u=0.10v$, these ratios are $1.111\ldots$ and $1.100$. Same closing speed, slightly different answers. **For sound, closing speed alone is not enough** because the medium supplies a distinguished frame. At small $u/v$ the difference is second order, which is why the two can seem interchangeable in everyday experience.

### Both moving — extension, with a sign convention that survives

Choose the positive $x$ direction along the travelling wave from source to observer. Let $V_s$ and $V_o$ be **signed velocity components along that direction**, measured relative to the medium. Then

$$\boxed{f_o=f_s\frac{v-V_o}{v-V_s}}.$$

The denominator constructs the spacing; the numerator counts encounters. A source travelling towards the observer has $V_s>0$; an observer travelling towards the source has $V_o<0$. If $V_s=V_o$, numerator and denominator match and there is no shift. Do not insert unsigned “speeds towards each other” into this signed formula.

A uniform wind is handled by working in the air's frame: subtract the wind velocity from both ground velocities. A stationary source and observer in the same uniform wind still have equal velocities relative to the air, hence no Doppler shift. Wind can change travel time; nonuniform or time-dependent flow needs a more detailed model.

## 4. Worked examples — select the mechanism first

### A train's horn tells you its speed

*Cambridge 9702/23, October/November 2023, Q6(a), paraphrased; checked against the published mark scheme.* A train approaches a stationary observer. Its horn emits $251$ Hz, the observer hears $291$ Hz, and sound travels at $340$ m s$^{-1}$. Find the train's speed in the question's direct-approach model.

**Trigger: moving source, fixed observer, frequency increased. Tool: the compressed-spacing formula.**

$$291=251\frac{340}{340-u_s}.$$

**Tool: rearrange before substituting further.**

$$u_s=v\left(1-\frac{f_s}{f_o}\right)=340\left(1-\frac{251}{291}\right)=46.74\ldots\approx\boxed{47\ \mathrm{m\,s^{-1}}}.$$

**Check:** $u_s<v$, and the inferred motion is towards the observer. A negative result would contradict the stated approach or reveal a reversed frequency ratio. The question's intensity/amplitude continuation tests a separate idea: louder is not the same as higher-pitched.

### A rotating source: constant speed does not mean constant shift

*Cambridge 9702/23, October/November 2024, Q5(b)(i), paraphrased; checked against the published mark scheme.* A source on a rotating platform emits $780$ Hz and moves at speed $39$ m s$^{-1}$. A distant observer hears it through air with sound speed $320$ m s$^{-1}$. Find the maximum received frequency.

**Trigger: a maximum over one orbit. Tool: project velocity onto the line of sight.** The greatest approach component is $39$ m s$^{-1}$, when the source's tangent points towards the distant observer.

$$f_{\max}=780\frac{320}{320-39}=888.26\ldots\approx\boxed{890\ \mathrm{Hz}}.$$

As a constructed extension, maximum recession gives $f_{\min}=780(320)/(320+39)\approx695$ Hz. Transverse source motion at emission gives zero radial component and $f_o=f_s$ in this classical stationary-observer model. Over a rotation, the frequency varies above and below $780$ Hz. It is approximately sinusoidal only when the shift is small; the exact extrema are not equally spaced around $780$ Hz.

### Change who moves

*Constructed comparison.* A stationary loudspeaker emits $600$ Hz in air with $v=340$ m s$^{-1}$. A listener approaches at $20$ m s$^{-1}$.

**Trigger: the observer moves while wave spacing stays fixed. Tool: encounter-rate formula.** $f_o=600(340+20)/340\approx635$ Hz. If the speaker instead approached a stationary listener at $20$ m s$^{-1}$, $f_o=600(340)/(340-20)=638$ Hz to the nearest hertz. The mechanism decides the formula.

## 5. Passing by: use the line of sight, and remember the delay

A siren on a straight road generally does not drive directly into your ear. Its speed along the line from the **emission position** to you is the relevant component. For a stationary observer and a moving source,

$$f_o=\frac{f_s}{1-u_s\cos\theta/v},$$

where $\theta$ is the angle between the source velocity at emission and the ray from that position to the observer. Direct approach has $\cos\theta=1$; direct recession has $\cos\theta=-1$. Sideways motion has zero component along the ray.

At a nonzero distance from the road, the radial component changes smoothly: the pitch changes smoothly too. The familiar idealised “high note, sudden jump, low note” approximates a close pass; an exact discontinuity belongs to the limiting straight-line point-source geometry. Nor does the pitch cross the emitted frequency at the instant you *see* the source at its closest point: sound emitted there still needs time to reach you.

**Pitch versus loudness.** Pitch follows frequency; loudness depends strongly on intensity and perception. A distant approaching siren can be quiet and high-pitched, while a nearby receding siren is loud and lower-pitched. The Doppler formula does not calculate its loudness.

## 6. Light: keep the arrival idea, change the physics

Light in vacuum has no air-like propagation frame. Every inertial observer measures its speed as $c$. Replacing $v$ by $c$ in one of the sound formulas would give different answers depending on who you called the moving object; relativity requires a different relation.

For a source and observer separating directly along their line of sight at constant relative speed $v_r$, define $\beta=v_r/c>0$. The relativistic longitudinal result is

$$\boxed{\frac{f_o}{f_0}=\sqrt{\frac{1-\beta}{1+\beta}}},\qquad \boxed{\frac{\lambda_o}{\lambda_0}=\sqrt{\frac{1+\beta}{1-\beta}}}.$$

**Why the square root?** Take $T_0$ as the period in the source's rest frame. In the observer's frame, time dilation makes the interval between emissions $\gamma T_0$, where $\gamma=1/\sqrt{1-\beta^2}$. During that interval the receding source adds $v_r\gamma T_0$ to the next crest's journey, adding another $\beta\gamma T_0$ to its travel time. Thus

$$T_o=\gamma T_0(1+\beta),\qquad \frac{f_o}{f_0}=\frac1{\gamma(1+\beta)}=\sqrt{\frac{1-\beta}{1+\beta}}.$$

Time dilation is the additional input from [[Special Relativity]], not a result derived from classical waves. For approach, use negative signed $\beta$ in this longitudinal relation. Non-collinear relativistic motion has additional angular dependence; it is not handled by blindly inserting a radial component into the full longitudinal square-root formula.

### The low-speed result, with honest signs

For $\lvert v_r\rvert\ll c$, a first-order expansion gives

$$\boxed{\frac{\Delta\lambda}{\lambda_0}\approx\frac{v_r}{c}},\qquad \boxed{\frac{\Delta f}{f_0}\approx-\frac{v_r}{c}},$$

where $\Delta\lambda=\lambda_o-\lambda_0$ and $\Delta f=f_o-f_0$. Recession increases wavelength but decreases frequency. The positive fractional-shift equality often printed in school formulas refers to **magnitudes**. With signed changes, the minus sign matters. More exactly, $f_o/f_0=1/(1+z)$, so $\Delta f/f_0=-z/(1+z)$.

**Redshift** means a shift to longer wavelengths, not necessarily visible red light. A shifted ultraviolet line can remain ultraviolet. **Blueshift** means shorter wavelengths.

### Worked spectrum example

*Constructed data; use one consistent wavelength convention.* A known line has laboratory wavelength $500.0$ nm and is observed at $500.2$ nm.

**Trigger: identify a line before measuring its shift. Tool: compare corresponding line positions.**

$$z=\frac{500.2-500.0}{500.0}=4.0\times10^{-4}.$$

**Trigger: a small fractional shift. Tool: $v_r\approx cz$.** $v_r\approx(3.00\times10^8)(4.0\times10^{-4})=1.2\times10^5$ m s$^{-1}$, or **120 km s$^{-1}$ away**. This is radial velocity, not total space velocity. Several lines should show the same fractional shift; matching a whole pattern is more reliable than guessing one peak. Use either air or vacuum reference wavelengths consistently and account for the observer's motion in precision work.

### Cosmological redshift is a related measurement, not the same mechanism

For light travelling through an expanding universe, wavelength grows with the cosmic scale factor: $1+z=a_{\rm now}/a_{\rm emitted}$. This is not generally a single source moving through static space with a special-relativistic recession velocity. The familiar $v\approx cz$ is a useful nearby-universe approximation, not an exact speed calculator at large redshift.

The systematic redshift of distant galaxies, together with its distance trend, supports cosmic expansion. Interpreting the full distance–redshift relation and estimating cosmic history requires [[Hubble's Law and the Expanding Universe]]. A redshift alone does not establish a galaxy's distance. Motion in gravitational fields can also change photon frequency: Doppler, cosmological and gravitational shifts must be distinguished when interpreting precise spectra.

## 7. The real-world trick: make motion carry information

### Radar — the shift happens on the way out and back

A radar transmits a known frequency and receives radiation scattered by a moving target. The target first acts as a moving receiver, then as a moving source of the returned wave. For slow radial motion, the two first-order shifts add:

$$\boxed{\lvert\Delta f\rvert\approx\frac{2f_0\lvert v_r\rvert}{c}=\frac{2\lvert v_r\rvert}{\lambda_0}}.$$

For a collinear receding reflector the ideal exact electromagnetic frequency ratio is $(1-\beta)/(1+\beta)$: applying the one-way longitudinal shift twice gives the result. Expanding it yields $f_{\rm return}\approx f_0(1-2\beta)$. The factor of two belongs to the **round trip**, not to every Doppler problem.

Weather radar uses the motion of scattering precipitation to estimate its velocity component along the beam. Reflectivity and radial velocity answer different questions: how much energy returned, and how the scatterers move. Zero radial velocity can mean sideways motion, not still air. Pulsed systems commonly infer the shift from phase changes between pulses. [NOAA/NWS: radar and radial velocity](https://www.weather.gov/cle/Area_Radars)

*Constructed instrument example:* a $10$ GHz monostatic radar receives a $2.0$ kHz shift. **Trigger: reflected signal. Tool: the two-way low-speed relation.** $\lvert v_r\rvert=c\lvert\Delta f\rvert/(2f_0)=30$ m s$^{-1}$. The sign of the measured shift supplies direction. At an angle, this is the beam component; infer total speed only if the direction is known.

### Ultrasound — red blood cells become moving reflectors

A probe sends ultrasound into tissue and receives sound scattered by moving blood cells. For flow speed $u$ much smaller than sound speed $v$, the magnitude of the echo shift is approximately

$$\boxed{\lvert\Delta f\rvert\approx\frac{2f_0u\lvert\cos\theta\rvert}{v}},$$

where $\theta$ is the angle between the flow and the beam. Again, there are outward and return shifts. For direct approach, the classical two-step result is $f_{\rm return}=f_0(v+u)/(v-u)$; its small-$u/v$ expansion gives the factor of two. The angled expression is a first-order projection.

*Constructed example:* take $f_0=5.0$ MHz, $v=1540$ m s$^{-1}$, $u=0.20$ m s$^{-1}$ and $\theta=60^\circ$. **Tool: project the flow before applying the echo formula.** $\lvert\Delta f\rvert=2(5.0\times10^6)(0.20)(0.50)/1540\approx650$ Hz. A MHz carrier has encoded motion as a much smaller shift.

At $90^\circ$ the first-order shift vanishes. Near that angle, estimating speed by dividing by $\cos\theta$ magnifies angular error. Colour maps indicate motion according to the instrument's displayed convention; “red” does not automatically mean artery, and “blue” does not automatically mean vein. Doppler ultrasound measures and visualises blood flow; interpreting a scan also requires anatomy, instrument settings and clinical context. [NIH/NIBIB: ultrasound](https://www.nibib.nih.gov/science-education/science-topics/ultrasound)

### A planet you cannot see can move a star you can

A star and planet orbit their common centre of mass. The star's alternating approach and recession shift its spectral lines periodically. A time series of these shifts can reveal an unseen companion. The measured amplitude is a **line-of-sight** amplitude, so orbital inclination matters; without additional information, radial-velocity data commonly constrain a minimum planet mass rather than the full mass uniquely. Stellar activity can also alter spectra, so a periodic signal requires careful checking. [NASA: radial velocity and stellar wobble](https://science.nasa.gov/universe/exoplanets/whats-out-there-the-exoplanet-sky-so-far/)

[[Energy Levels and Line Spectra]] supplies the identifiable line pattern; Doppler physics turns its displacement into motion. The microscopic energy ladder becomes an astronomical speedometer.

## 8. Beyond the subsonic model: a shock is not an infinite note

As $u_s\to v$ in the forward sound formula, successive wavefronts pile up and the steady received-frequency model becomes singular. This does not predict a physically infinite audible pitch. The assumptions behind a smooth train of arriving crests have broken down.

For a supersonic source, $M=u_s/v>1$, wavefronts form a conical envelope. In time $t$, the source travels $u_st$ while a disturbance expands through $vt$. The geometry gives the Mach-cone half-angle

$$\sin\mu=\frac{vt}{u_st}=\frac1M.$$

A shock crossing the observer produces the abrupt pressure change heard as a sonic boom. The source generates the shock pattern throughout its supersonic travel; it is not a single noise made only at the instant it first crosses Mach 1. Shock structure and nonlinear acoustics go beyond the linear Doppler model.

## Common Misconceptions

| Claim | Repair the model |
|---|---|
| “The ambulance throws sound forwards faster.” | In uniform still air, the sound speed is fixed by the medium; the spacing changes |
| “Any nearby source sounds higher.” | Fixed distance changes delay and often intensity, not frequency; changing distance changes arrival spacing |
| “Use relative speed in either sound formula.” | Identify whose motion changes spacing and whose motion changes encounters |
| “Redshift means the object is visibly red.” | Compare a line with its rest wavelength, regardless of spectral region |
| “No shift means no motion.” | The measured component can be zero while sideways speed is large; relativistic corrections are a separate issue |
| “Radar speed is just $c\Delta f/f$.” | A reflected signal is shifted on both legs; the low-speed result needs the factor two |
| “Frequency and wavelength both increase.” | For vacuum light in the observer's frame, $c=f_o\lambda_o$; their signed shifts are opposite |

## Exam Notes

### Cambridge 9702 — AS §7.3; A Level §25.3 overlap

**§7.3** requires sound from a **moving source and stationary observer**, using $f_o=f_sv/(v\pm u_s)$. The moving-observer treatment is explicitly not required. The source formula is supplied in the inspected Paper 2 formula list; choosing the sign and interpreting source/observed frequency remain the student's job. The two verified worked anchors are **9702/23/O/N/23 Q6(a)** and **9702/23/O/N/24 Q5(b)(i)**. Wavefront explanations should say both that wavelength changes and that the wave speed in the medium does not.

**§25.3** also examines spectral redshift and the low-speed fractional-shift relation. It is A-Level astronomy content, assessed in Paper 4; do not confuse it with AS sound. Hubble's law and the Big Bang are additional requirements beyond the Doppler/spectral treatment here. The exact relativistic formula, moving-reflector derivations and shock geometry are enrichment.

### IB Physics — C.5

**SL and HL:** nature of Doppler for sound and electromagnetic waves, wavefront diagrams for source/observer motion, low-speed light shifts and spectral-line inference. **Additional HL:** quantitative sound problems with either a moving source **or** a moving observer, including finding their speed. The guide explicitly excludes problems with **both source and observer moving**. Medical ultrasound and radar are applications to consider. A formula written with positive fractional changes is a magnitude relation; keep signed frequency and wavelength changes distinct in explanations.

### AP Physics 2 — §14.5

The treatment is explicitly **qualitative**: compare observed/rest frequency for approach, recession and equal source/observer velocity, and explain with representations. Deriving and calculating with the formulas is useful enrichment, not a §14.5 numerical requirement. Equal velocities give no shift in the elementary model. Predictions about increasing relative speed assume the same approach/recession geometry; sideways motion must not be confused with greater radial speed.

### Cambridge 0625 — §6.2.3, redshift only

Core requires redshift as increased wavelength from receding stars/galaxies and its evidence for expansion/Big Bang. Supplement connects spectral changes to galaxy recession speed, then adds supernova distances, Hubble's constant and an age estimate. Sound Doppler formulas are not a 0625 requirement. This redshift explanation supplies only part of the astronomy topic; the rest needs the stellar/cosmological treatment.

**Where it is not examined:** Doppler effect is not a topic in AP Physics 1, AP Physics C: Mechanics or AP Physics C: Electricity and Magnetism. Cambridge 0625 does not examine the quantitative sound formulas. Relativistic Doppler, supersonic shocks and the combined moving-source/moving-observer formula exceed the named school requirements above.

## Connections

- **Imaging companion:** [[Ultrasound]] — echo delay supplies depth; Doppler shifts supply motion along the beam.

- **Parent:** [[Progressive Waves]] — frequency counts cycles and $v=f\lambda$ connects spacing with arrival rate.
- **Spectroscopic ingredient:** [[Energy Levels and Line Spectra]] — identify the same line before interpreting a displacement.
- **Extensions:** [[Special Relativity]] — time dilation changes the light-wave result; [[Hubble's Law and the Expanding Universe]] — redshift in an expanding spacetime.
- **Shared geometry:** [[Circular Motion]] — constant speed with a changing line-of-sight component; [[Vectors in Physics]] — projection onto the measurement direction.
- **Signal processing:** [[Superposition and Interference]] — beats provide a way to compare close frequencies; [[Sound Encoding]] — digitised recordings make frequency changes measurable.

## LaTeX Reference

| Expression | LaTeX | Use |
|---|---|---|
| $f_o=f_sv/(v-u_s)$ | `f_o=f_sv/(v-u_s)` | Approaching source, fixed observer |
| $f_o=f_s(v+u_o)/v$ | `f_o=f_s(v+u_o)/v` | Approaching observer, fixed source |
| $z=(\lambda_o-\lambda_0)/\lambda_0$ | `z=(\lambda_o-\lambda_0)/\lambda_0` | Signed wavelength shift |
| $v_r\approx cz$ | `v_r\approx cz` | Low-speed radial motion |
| $f_o/f_0=\sqrt{(1-\beta)/(1+\beta)}$ | `\sqrt{(1-\beta)/(1+\beta)}` | Longitudinal relativistic recession |
| $\lvert\Delta f\rvert\approx2f_0u\lvert\cos\theta\rvert/v$ | `2f_0u\lvert\cos\theta\rvert/v` | Low-speed reflected sound |
