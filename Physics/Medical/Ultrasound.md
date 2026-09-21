---
chinese: 超声波 (chāoshēngbō)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Resonance]]"
  - "[[Sound]]"
leads_to: []
teach_together:
  - "[[X-rays and CT]]"
  - "[[Doppler Effect]]"
tags:
  - subject/physics
  - domain/medical-physics
  - level/IGCSE
  - level/A-Level
  - level/university
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - syllabus/0625-3-4
  - syllabus/9702-24-1
  - type/deep
  - type/derivation
  - notation/acoustic-impedance
  - misconception/echo-distance-is-ct
  - misconception/reflection-is-attenuation
---

# Ultrasound 超声波

> *Before the first image appears, someone puts gel on your skin. That small, slightly cold detail is doing serious physics: without it, an air gap would send almost all the sound straight back. The scanner first has to persuade a wave to enter your body. Then it listens.*

## Definition — a picture made from waiting

**Ultrasound** is sound with frequency **greater than 20 kHz**, above the conventional upper limit of human hearing. It is a mechanical wave: in soft tissue it travels as longitudinal compressions and rarefactions, and it needs a material medium. “Ultra” means high frequency, not high loudness or an electromagnetic wave.

**Pulse–echo imaging** sends a short burst of ultrasound into a material, measures the returning echoes, and infers the positions of reflecting structures from their return times. An echo is a reflected sound wave. The pulse carries energy; particles of tissue oscillate locally rather than travelling from the probe to an organ.

Three questions build the image:

1. **When did the echo arrive?** This gives distance along the beam, if the wave speed is known.
2. **How strong was it?** This depends on reflection, path losses and the receiver's processing.
3. **Which way was the beam pointing?** This places that distance on an image.

The result is a reconstruction from measurements, not a photograph taken with sound-coloured light.

### 中文锚点

做 B 超时，探头上那层凉凉的凝胶，不只是为了滑得顺。探头与皮肤之间若夹着空气，大部分声波还没进身体就会被反射回来；凝胶帮它们跨过这一关。接下来，探头发声、等回声：回得越晚，反射位置通常越深，因为声音得走过去再回来。屏幕上的图像，就是这样由一次次回声拼出来的，并不是把一台小相机伸进了身体。

## Notation

| Quantity | Symbol | Unit / meaning |
|---|---|---|
| Frequency and wavelength | $f,\lambda$ | Hz, m; $c=f\lambda$ |
| Sound speed in the medium | $c$ | $\mathrm{m\,s^{-1}}$; here $c$ is **not** the speed of light |
| One-way depth; echo delay | $d,t$ | m, s; $t$ is measured from emission to reception |
| Density; acoustic impedance | $\rho,Z$ | $\mathrm{kg\,m^{-3}}$, $\mathrm{kg\,m^{-2}\,s^{-1}}$ |
| Incident / reflected intensity | $I_0,I_R$ | $\mathrm{W\,m^{-2}}$ |
| Intensity reflection fraction | $R=I_R/I_0$ | Dimensionless; distinct from pressure-amplitude ratio $r$ |
| Intensity attenuation coefficient | $\mu$ | Inverse length, e.g. $\mathrm{m^{-1}}$ |

## Key Ideas — follow the pulse

### 1. One crystal, two directions of energy conversion

A **piezoelectric** material links mechanical deformation to electrical polarisation. Applying a potential difference changes its shape; changing its shape produces an electrical signal across it.

- **Transmit:** a rapidly alternating p.d. makes the element expand and contract. These vibrations drive pressure changes in the surrounding material.
- **Resonance:** driving near a suitable natural vibration frequency gives a large response. For ultrasonic emission, that frequency must be ultrasonic; simply using an alternating voltage does not guarantee ultrasound.
- **Receive:** a returning pressure pulse deforms the element and generates a small alternating electrical signal. The electronics amplify and record it.

A pulse–echo probe switches between transmitting and listening. It needs a **brief burst**, not an indefinitely ringing crystal: a long outgoing pulse would hide closely spaced echoes and delay the start of useful reception. Backing material damps the vibration after the drive stops. This is a practical compromise between the strong response of [[Resonance]] and the fast settling of a damped oscillator.

### 2. Time becomes depth — why the factor of two exists

For one stationary reflector at depth $d$ in a uniform medium, the outward path is $d$ and the return path is $d$:

$$t=\frac{d}{c}+\frac{d}{c}=\frac{2d}{c},\qquad \boxed{d=\frac{ct}{2}}.$$

The instrument measures **round-trip time**; the image labels **one-way depth**. For two successive echoes separated by $\Delta t$, the separation of their reflectors along the same uniform-speed beam is $c\Delta t/2$.

Soft-tissue scanners commonly use a nominal speed near $1540\ \mathrm{m\,s^{-1}}$. Actual tissue speeds vary, so this assumption can introduce positioning errors. For layers of thickness $d_i$ and speed $c_i$, travelling out and back along the same path gives

$$t=2\sum_i\frac{d_i}{c_i}.$$

Do not replace this with a simple arithmetic average of the speeds. Add the times spent in the layers.

![[ultrasound-echo-depth.svg|720]]

*An illustrative pair of echoes becomes two positions. Their amplitudes were chosen for visibility; these are synthetic reflectors, not a measured patient trace.*

### 3. From trace to slice

An **A-mode** display plots echo amplitude against time or depth. A **B-mode** display converts echo strength into brightness at the inferred depth. Repeating the measurement along many beams constructs a two-dimensional slice; acquiring slices through a volume can support a three-dimensional reconstruction.

The receiver starts with an oscillating electrical waveform. It can extract its **envelope**—the outline of its amplitude—then apply gain and compress a large dynamic range into the screen's limited brightness range. Late echoes may receive more amplification to compensate partly for their longer attenuating paths.

Therefore **bright does not simply mean dense**, and dark does not simply mean empty. Reflection depends on an *impedance change*; brightness also depends on depth, beam angle, scattering and processing. Real tissue contains many small scatterers, whose interfering echoes produce the granular pattern called **speckle**.

![[ultrasound-pulse-to-image.mp4]]

*Follow a pulse to two reflectors, watch the return times become depths, then watch successive beams build a slice. The final scene adds attenuation on both legs. Motion is greatly slowed; the synthetic scan omits scattering, refraction and other real-image complications.*

### 4. Why a boundary reflects — acoustic impedance

**Specific acoustic impedance** for a plane progressive wave in a simple medium is

$$\boxed{Z=\rho c}.$$

It relates pressure amplitude to particle-velocity amplitude: $p=Zu$ for a forward-travelling plane wave. Here $u$ is the tiny back-and-forth material velocity, not the wave speed $c$. A large $Z$ means more pressure is needed for a given particle velocity. This is not the same property as “how quickly sound dies away”.

At a boundary, pressure and normal particle velocity must fit together. The incident wave alone generally cannot satisfy both conditions in the new medium. A reflected wave supplies the missing adjustment.

**Derivation — normal incidence, a lossless boundary, real positive impedances.** Treat the media as supporting longitudinal plane waves; in solids, oblique incidence can also produce mode conversion, outside this model.

1. **Pressure continuity:** $p_i+p_r=p_t$.
2. **Particle-velocity continuity:** the reflected wave travels backwards, so $(p_i-p_r)/Z_1=p_t/Z_2$.
3. **Eliminate $p_t$:** $Z_2(p_i-p_r)=Z_1(p_i+p_r)$, hence

$$r=\frac{p_r}{p_i}=\frac{Z_2-Z_1}{Z_2+Z_1}.$$

4. **Convert amplitude to intensity:** incident and reflected waves are in the *same medium*, where intensity is proportional to pressure amplitude squared. Therefore

$$\boxed{R=\frac{I_R}{I_0}=\left(\frac{Z_2-Z_1}{Z_2+Z_1}\right)^2}.$$

5. **Conserve energy across the interface:** with no interface absorption, the transmitted intensity fraction is

$$\boxed{T=1-R=\frac{4Z_1Z_2}{(Z_1+Z_2)^2}}.$$

The pressure transmission ratio is $p_t/p_i=2Z_2/(Z_1+Z_2)$. It can exceed 1 without creating energy: for a travelling wave, $I=p_{\mathrm{rms}}^2/Z$, so the transmitted intensity must also account for the changed impedance. Squaring the transmitted pressure ratio alone is wrong.

### 5. Why the gel matters

For an illustrative air–soft-tissue boundary, take $Z_{\rm air}\approx430$ and $Z_{\rm tissue}\approx1.6\times10^6\ \mathrm{kg\,m^{-2}\,s^{-1}}$. The reflection model gives $R\approx0.9989$: about **99.9% reflected**. An air pocket is almost an acoustic mirror.

Coupling gel replaces that poorly transmitting air gap with a medium much better matched to tissue. It does not need to be a perfect match to make an enormous difference. Soft-tissue boundaries can return a small useful echo while transmitting most of the energy onward. A strong reflector can instead leave an **acoustic shadow** behind it: too little energy reaches deeper structures or returns from them.

Matching, rather than simply maximising reflection, is the design problem. We need sound to enter the body, then a little of it to come back from the boundaries of interest. [OpenStax, Ultrasound](https://openstax.org/books/college-physics-2e/pages/17-7-ultrasound)

### 6. Attenuation — each centimetre takes a fraction

**Attenuation** is the reduction of beam intensity along its path, for example through absorption and scattering out of the beam. Absorption transfers energy into internal energy; scattering redirects it. Geometrical spreading can also reduce intensity, but is excluded from the simple parallel-beam law below.

For a homogeneous medium at a fixed frequency, suppose each thin layer removes a fraction proportional to its thickness:

$$\mathrm dI=-\mu I\,\mathrm dx.$$

Divide by $I$, integrate from $I_0$ to $I$ and from 0 to $x$:

$$\ln\frac{I}{I_0}=-\mu x,\qquad \boxed{I=I_0e^{-\mu x}}.$$

The intensity approaches zero continuously; it does not lose a fixed number of watts per square metre in every centimetre. The coefficient has inverse-length units because $\mu x$ must be dimensionless. Distance $1/\mu$ leaves a fraction $1/e$ of the initial intensity.

For a reflector at depth $d$, count the events in order:

$$I_0\ \xrightarrow{\text{outward path}}\ I_0e^{-\mu d}
\ \xrightarrow{\text{reflection}}\ RI_0e^{-\mu d}
\ \xrightarrow{\text{return path}}\ \boxed{I_{\rm echo}=RI_0e^{-2\mu d}}.$$

This assumes a single reflector, identical outward/return paths, and no spreading or intervening interfaces. If the beam crosses another lossless boundary with transmission fraction $T$ on the way out and again on return, multiply by **$T^2$**. For several layers, multiply the relevant transmissions and use $\exp(-2\sum_i\mu_i d_i)$.

![[ultrasound-reflection-attenuation.svg|720]]

*Top: impedance matching suppresses reflection. Bottom: attenuation acts on the total path, so an echo loses more than a one-way beam. These are separate physical effects.*

## Special Cases — useful checks before calculating

- **$Z_1=Z_2$:** $R=0$. A perfectly matched ideal boundary gives no reflected echo even if it separates differently named materials.
- **Very large impedance ratio:** $R\rightarrow1$. Little energy crosses the boundary.
- **Reverse the direction:** $R$ is unchanged, but $r$ changes sign. Reflected pressure can invert; intensity cannot be negative.
- **$\mu=0$:** no path attenuation, but a boundary can still reflect. Conversely, matched impedances do not imply zero absorption inside either medium.
- **Amplitude versus intensity:** if pressure amplitude decays as $e^{-\alpha x}$ in a uniform medium, intensity decays as $e^{-2\alpha x}$. Thus the intensity coefficient is $\mu=2\alpha$.

## Worked Examples — name the event before the equation

### 1. How much gets through bone? — 9702/42/F/M/25 Q4(d)(ii), 3 marks

**Source data, paraphrased:** muscle has density $1100\ \mathrm{kg\,m^{-3}}$ and sound speed $1600\ \mathrm{m\,s^{-1}}$; bone has density $1900\ \mathrm{kg\,m^{-3}}$ and sound speed $4100\ \mathrm{m\,s^{-1}}$. Find the percentage of incident intensity transmitted at the boundary. Use the ideal normal-incidence model.

**Tool: $Z=\rho c$ — the question supplies material properties rather than impedances.**

$$Z_m=1100(1600)=1.76\times10^6,\qquad Z_b=1900(4100)=7.79\times10^6.$$

Both have units $\mathrm{kg\,m^{-2}\,s^{-1}}$.

**Tool: boundary reflection — a change of medium, not a length of travel.**

$$R=\left(\frac{7.79-1.76}{7.79+1.76}\right)^2=0.398684\ldots$$

**Tool: energy conservation — the requested quantity is transmitted.**

$$\boxed{100T=100(1-R)=60.1\%\approx60\%.}$$

The published scheme credits impedance, reflection fraction, and the final transmitted percentage. Stopping at 40% answers a different question. No attenuation coefficient or thickness is supplied; do not invent a path loss.

### 2. A fading beam — 9702/44/M/J/25 Q10(c), 2 marks

**Source data, paraphrased:** after travelling $2.1\ \mathrm{cm}$ through soft tissue, a parallel ultrasound beam has $0.62$ of its original intensity. Find the attenuation coefficient, with a unit.

**Tool: exponential attenuation — a known path length and surviving fraction.**

$$0.62=e^{-\mu(0.021)}.$$

**Tool: logarithms — the unknown is in the exponent.**

$$\ln(0.62)=-0.021\mu,\qquad
\boxed{\mu=22.76\ldots\ \mathrm{m^{-1}}\approx23\ \mathrm{m^{-1}}.}$$

Equivalently, using centimetres throughout gives $\boxed{0.23\ \mathrm{cm^{-1}}}$, the scheme's form. The given $2.1\ \mathrm{cm}$ is the beam's travelled distance; it is **not automatically doubled** merely because the context is ultrasound.

**Original extension:** if a reflector were instead at depth $2.1\ \mathrm{cm}$, the outward and return survival fractions would multiply: $0.62^2=0.3844$. Including its reflection fraction gives $I_{\rm echo}/I_0=0.3844R$.

### 3. One clock, three applications — original examples

**A tissue echo returns after $78\ \mu\mathrm{s}$; use $c=1540\ \mathrm{m\,s^{-1}}$.**

**Tool: path accounting — the pulse has gone out and back.**

$$d=\frac{1540(78\times10^{-6})}{2}=0.06006\ \mathrm m\approx\boxed{6.0\ \mathrm{cm}}.$$

**A downward sonar echo returns after $0.16\ \mathrm s$ in water of speed $1500\ \mathrm{m\,s^{-1}}$.** The same tool gives $d=1500(0.16)/2=\boxed{120\ \mathrm m}$ below the transducer. Add any transducer depth below the water surface only if the requested reference level requires it.

**A test pulse in a metal returns from a crack after $8.0\ \mu\mathrm s$, with wave speed $5900\ \mathrm{m\,s^{-1}}$.** For a direct normal path, $d=5900(8.0\times10^{-6})/2=\boxed{2.36\ \mathrm{cm}}$. An early echo before the expected back-wall echo can reveal an internal discontinuity without cutting the object open.

## Real Life — seeing, measuring, inspecting

**Medical imaging:** pulse echoes locate structures in soft tissue; cardiac imaging follows moving heart structures, while Doppler measurements add blood-flow information. The same transducer can turn electrical energy into sound and the returning sound into electrical measurements. [NIH/NIBIB, Ultrasound](https://www.nibib.nih.gov/science-education/science-topics/ultrasound)

**Non-destructive testing:** an internal crack creates an impedance discontinuity. Measure its echo delay to estimate position, compare with the back-wall return, and examine different probe positions. Reflection angle and crack orientation matter: failure to receive an echo is not proof that an object has no crack.

**Sonar and ranging:** boats measure depth by waiting for echoes from the seabed. Ultrasonic rangefinders use the same timing idea in air. The appropriate sound speed belongs to the medium and conditions, not to the instrument's name.

**Energy still matters:** ultrasound uses no ionising radiation, but sound can transfer energy to tissue and produce heating or mechanical effects. “Not ionising” does not mean “incapable of biological effects”; diagnostic equipment and exposure are chosen accordingly. [FDA, Ultrasound Imaging](https://www.fda.gov/radiation-emitting-products/medical-imaging/ultrasound-imaging)

## Hands-on — predict, then run the echo model

Open `ultrasound-model.py`, which uses only Python's standard library. Before running it, predict what doubling reflector depth will change: the delay doubles, but the received intensity is multiplied by a further $e^{-2\mu d}$ rather than simply halved.

```python
from math import exp
c, d = 1540.0, 0.060       # m/s, one-way metres
mu, R = 23.0, 0.02        # inverse metres, reflected intensity fraction
delay = 2 * d / c
echo_fraction = R * exp(-2 * mu * d)
print(delay * 1e6, echo_fraction)  # about 77.9 microseconds, 0.00127
```

The companion checks the two published-question calculations, reciprocity of $R$, conservation at a boundary, and an independent small-step approximation to attenuation. Change an impedance to match its neighbour; then change $\mu$ while keeping the impedances fixed. One switch changes **reflection**, the other **path loss**.

## Common Misconceptions

- **“Depth is $ct$.”** Draw arrows for both legs before using speed × time; the total distance is $2d$.
- **“A brighter patch is denser.”** Compare two equal impedances with different densities and sound speeds, then add attenuation. Brightness is a processed echo measurement.
- **“The reflection formula gives transmission.”** Label the event and the fraction before substituting; in the lossless model $T=1-R$.
- **“Bigger $Z$ means faster attenuation.”** $Z$ controls pressure/velocity matching; $\mu$ controls intensity loss per length. Neither determines the other by definition.
- **“Ultrasound must be loud.”** Frequency determines the name; amplitude and intensity describe different properties.
- **“A faint deep echo proves a weak reflector.”** It may instead have suffered strong outward and return attenuation or been partly blocked by another interface.

## Exam Notes

### Cambridge A-Level Physics 9702 — §24.1, all six outcomes

The 2028–2030 syllabus requires the piezoelectric effect in both directions, ultrasound generation/detection, imaging with reflected pulses, $Z=\rho c$, the normal-incidence intensity reflection ratio, and $I=I_0e^{-\mu x}$. The 2025–2027 outcomes are the same. The boundary derivation and image-processing extensions explain the equations beyond the stated calculation requirements.

- **Describe a working transducer:** alternating p.d. → alternating deformation → vibrations; suitable natural frequency and resonant drive; returning pressure variations deform the crystal → electrical signal. Q10(a) of 9702/44/M/J/25 explicitly credits the resonant drive and ultrasonic natural frequency.
- **Identify what the clock times:** use $2d$ for a round trip, but do not double a distance already stated as the travelled path.
- **Use the correct fraction:** $I_R/I_0$ is reflected; transmitted fraction is $1-R$ under the lossless boundary model.
- **Track units:** density in $\mathrm{kg\,m^{-3}}$, speed in $\mathrm{m\,s^{-1}}$; pair $\mu$ in $\mathrm{cm^{-1}}$ with $x$ in cm, or convert both to SI.
- **Formula sheet:** the supplied formula list in the verified 2025 papers includes the intensity reflection ratio, but not $Z=\rho c$ or the ultrasound attenuation law. Knowing which physical event each formula describes is still essential.

Worked sources: **9702/42/F/M/25 Q4(d)(ii)** (QP p.13; MS Q4(d)(ii)) and **9702/44/M/J/25 Q10(c)** (QP p.21; MS p.18). Both calculations were checked against their published mark schemes; Example 3 and the extension after Example 2 are original.

### Cambridge IGCSE Physics 0625 — §3.4 Sound

Core outcome 9 defines ultrasound as frequency above 20 kHz. Supplement outcome 12 names non-destructive testing, medical soft-tissue scanning and sonar, including distance/depth from time and wave speed. The echo explanation also supports Core outcome 8. The impedance and exponential-attenuation calculations belong to the A-Level extension, not this IGCSE requirement. General sound—including an air-speed experiment, loudness/pitch and the other §3.4 outcomes—remains a broader topic.

### IB and AP — adjacent physics, with a clear boundary

- **IB Physics, first assessment 2025:** C.5 asks students to consider Doppler applications in medical physics and radar; Additional HL includes quantitative sound Doppler calculations for one moving source or observer. The two-stage blood-flow reflection below is an application/extension. The guide does **not** specify a separate medical-ultrasound imaging unit or the impedance/attenuation formula set taught here.
- **AP Physics 2:** Unit 14.3 supplies general wave reflection/transmission principles. Medical pulse–echo imaging and these acoustic-impedance/attenuation calculations are not named learning requirements.
- **Not a medical-ultrasound topic in AP Physics 1, AP Physics C: Mechanics or AP Physics C: Electricity and Magnetism.** An ultrasonic motion sensor appearing in a laboratory equipment list does not make the scanner's internal physics a course requirement. Their relevant mechanics/waves ideas can still support the explanation.

## Connections

- **Imaging companion:** [[X-rays and CT]] — measured projections become constraints on an unknown interior.

- **Foundation:** [[Progressive Waves]] — longitudinal waves, intensity, $c=f\lambda$ and the plane-wave intensity relation.
- **Transducer:** [[Resonance]] — why a periodic electrical drive produces a strong mechanical response near a natural frequency.
- **Companion measurement:** [[Doppler Effect]] — moving reflectors add information about blood velocity to the position information from pulse timing.
- **Shared mathematical structure:** [[Exponential Growth and Decay]] — equal fractional loss per equal distance becomes exponential decay.
- **Contrast in imaging:** [[Electromagnetic Spectrum]] — ultrasound is mechanical sound, unlike X-rays; different probes interact with matter differently.

## Beyond Syllabus — what makes a useful scanner?

### Short pulses separate close reflectors

Recall that a pulse must travel to a reflector and back. If its duration is $\tau$, two echoes separated by less than roughly $\tau$ overlap. Their minimum axial separation is therefore approximately

$$\boxed{\Delta d_{\rm axial}\approx\frac{c\tau}{2}=\frac{N\lambda}{2}},$$

where $N$ is the number of cycles in the pulse. At $5.0\ \mathrm{MHz}$ and $c=1540\ \mathrm{m\,s^{-1}}$, $\lambda=0.308\ \mathrm{mm}$; a two-cycle pulse gives an ideal axial separation scale near $0.31\ \mathrm{mm}$. Real resolution also depends on bandwidth and signal processing. **Lateral** resolution depends on beam width and focusing, not this formula alone.

Higher frequency means shorter wavelength and potentially finer detail, but soft-tissue attenuation generally increases with frequency. A deep target may therefore need a lower frequency than a shallow one. Strong damping shortens the pulse but changes sensitivity and bandwidth: the sharpest resonance is not automatically the best imaging transducer.

### Waiting limits frame rate

Recall that a reflector at maximum depth $d_{\max}$ returns after $2d_{\max}/c$. To avoid confusing an old pulse's echo with a new pulse, a simple pulse–echo system needs

$$\mathrm{PRF}\lesssim\frac{c}{2d_{\max}},$$

where PRF is the **pulse repetition frequency**, not the megahertz frequency *inside* each pulse. At 15 cm and $1540\ \mathrm{m\,s^{-1}}$, the ideal ceiling is about $5.1\ \mathrm{kHz}$. With 128 sequential beams per frame and one transmission per beam, this alone limits the frame rate to roughly 40 frames per second; processing, multiple focal zones and additional transmissions can reduce it.

### Steering and Doppler — choose a direction, then measure motion

Recall that sound waves superpose. An array of small elements can fire with controlled delays so their waves reinforce along a chosen direction. Adjusting those delays steers/focuses the beam electronically; appropriately delayed receive signals can likewise reinforce echoes from a chosen location. This is beamforming, rather than physically rotating the whole probe for each image line.

A moving blood cell first receives the incident sound and then acts as a moving source of the reflected sound. For speed $u\ll c$, the magnitude of the shift is approximately

$$\lvert\Delta f\rvert\approx\frac{2f_0u\lvert\cos\theta\rvert}{c}.$$

The two Doppler stages produce the factor of two; the cosine selects velocity along the beam. This is **not** the same factor of two as the geometric round trip in $d=ct/2$. Near $90^\circ$, the shift becomes small and inferred speed becomes highly sensitive to angle error. [[Doppler Effect]] develops this measurement and the colour-map conventions.

### Decibels — the same exponential in another language

Recall that the intensity law is $I/I_0=e^{-\mu x}$. Express the positive intensity loss in decibels:

$$L=10\log_{10}\frac{I_0}{I}=\frac{10\mu x}{\ln10}.$$

Thus a loss coefficient $a$ in dB per unit length corresponds to $\mu=a\ln10/10$ in the matching inverse-length unit. Decibel loss adds along successive path segments because intensity survival fractions multiply. A stated dB loss over an echo path already includes whichever legs its definition names; count the path before converting.

## LaTeX Reference

| Expression | LaTeX | Reminder |
|---|---|---|
| $Z=\rho c$ | `Z=\rho c` | Specific acoustic impedance |
| $R=((Z_2-Z_1)/(Z_2+Z_1))^2$ | `\left(\frac{Z_2-Z_1}{Z_2+Z_1}\right)^2` | Intensity fraction at normal incidence |
| $I=I_0e^{-\mu x}$ | `I=I_0e^{-\mu x}` | $x$ is travelled distance |
| $d=ct/2$ | `d=\frac{ct}{2}` | $t$ is the round-trip time |
