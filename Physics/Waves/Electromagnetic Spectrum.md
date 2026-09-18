---
chinese: 电磁波谱 (diàncí bōpǔ)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Maxwell's Equations]]"
  - "[[Superposition and Interference]]"
  - "[[Diffraction]]"
leads_to:
  - "[[Stellar Luminosity and Size]]"
  - "[[X-rays and CT]]"
  - "[[Polarisation]]"
tags:
  - subject/physics
  - domain/waves
  - domain/electromagnetism
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - syllabus/0625-3-3
  - syllabus/9702-7-4
  - type/deep
  - type/definition
  - type/cross-domain
  - misconception/higher-frequency-faster
  - misconception/radiation-means-radioactive
  - misconception/digital-means-no-errors
---

# Electromagnetic Spectrum 电磁波谱

> Your room is full of light you cannot see. Your router transmits some of it. Your remote controller flashes some of it. Your body emits some of it even when every lamp is off.
>
> Your eyes are tuned to one very small interval. The universe did not stop at the edges of the rainbow.

## Definition

### Formal

The **electromagnetic spectrum** is the continuous range of electromagnetic radiation, arranged by frequency $f$ or vacuum wavelength $\lambda_0$. Its named regions—radio, microwave, infrared, visible, ultraviolet, X-ray and gamma—are useful divisions of one physical family.

For a freely travelling electromagnetic wave in vacuum, the electric and magnetic fields oscillate perpendicular to each other and to the direction of propagation. It is a **transverse wave**, needs no material medium, and travels at

$$\boxed{c=f\lambda_0\approx3.00\times10^8\ \text{m s}^{-1}.}$$

The exact defined value of $c$ is $299\,792\,458\ \text{m s}^{-1}$; the rounded value above is sufficient for the calculations here.

### Intuitive — one instrument, many notes

Low and high notes are both sound. Low- and high-frequency electromagnetic waves are likewise members of one family—but unlike sound, their travelling disturbance is in the fields rather than the compression of a material.

Changing the frequency changes what the radiation can interact with. A metre-scale aerial, a vibrating molecular bond, an electron in an atom and an excited nucleus do not all respond in the same way. The spectrum becomes useful when you connect **wavelength → interaction → application**.

The boundaries are conventions, not fences in nature. Nothing discontinuous happens to an electromagnetic wave because a table changes its label from infrared to visible. What changes is whether a particular detector—your eye, for example—responds strongly enough to register it.

### 中文锚点 (Chinese Anchor)

按下遥控器，电视有了反应，你却没看见有什么东西飞过去。其实遥控器常用人眼看不见的红外光传递指令；可见光只是电磁波的一小段。换一段波长，物质吸收它、让它通过或探测到它的方式也会不同，于是同一个家族能有很不一样的用途。热成像仪把收到的红外信息换成屏幕上的颜色：它帮眼睛“翻译”了看不见的信号，并不是发现人体真的在发红光。

## Notation

| Quantity | Symbol / unit | Meaning |
|---|---|---|
| Vacuum wavelength | $\lambda_0$, m | Distance between successive equal-phase points in vacuum |
| Frequency | $f$, Hz | Oscillations per second |
| Period | $T$, s | Time per oscillation; $T=1/f$ |
| Vacuum speed | $c$, m s$^{-1}$ | The common speed of all electromagnetic radiation in vacuum |
| Photon energy | $E_\gamma$, J or eV | Energy per photon, not the energy of the entire beam |
| Intensity | $I$, W m$^{-2}$ | Energy arriving per second per unit area |

$1\ \text{GHz}=10^9\ \text{Hz}$; $1\ \mu\text{m}=10^{-6}\ \text{m}$; $1\ \text{nm}=10^{-9}\ \text{m}$; $1\ \text{pm}=10^{-12}\ \text{m}$.

## Key Facts — what changes, what stays fixed

![[electromagnetic-spectrum-see-it-change.mp4]]

Watch the wavelength change while the travelling wave keeps the same speed, then compare red and blue beams of equal power. More energy per photon means fewer photons per second at the same power.

### 1. Frequency changes the spacing, not the vacuum speed

Recall the derivation in [[Progressive Waves]]: in one period $T$, the pattern advances one wavelength. Thus $v=\lambda/T=f\lambda$. In vacuum $v=c$, so

$$\lambda_0=\frac{c}{f}.$$

Double the frequency and the wavelength halves. The wave does **not** overtake a lower-frequency wave travelling alongside it through vacuum.

[[Maxwell's Equations]] gives the deeper reason for the common speed: the electric and magnetic field equations combine into a wave equation with $c=1/\sqrt{\mu_0\varepsilon_0}$. The labels “radio” and “visible” do not occur in that result.

In matter, use $v=f\lambda$, not automatically $c=f\lambda$. At a stationary boundary the transmitted wave retains the driving frequency, while its speed and wavelength can change. Ordinary glass can give different visible frequencies different phase speeds: **dispersion**. This does not contradict the common speed in vacuum.

### 2. The spectrum is logarithmic country

![[electromagnetic-spectrum-map.svg|900]]

*Top: equal horizontal intervals represent factors of ten in wavelength. The full visible band is a sliver. Bottom: that sliver is expanded on its own linear scale; colour divisions are approximate. Wavelength decreases to the right, while frequency and photon energy increase.*

| Region | Useful approximate vacuum wavelengths | A representative scale |
|---|---|---|
| Radio, excluding the microwave subdivision | Longer than roughly $1\ \text{m}$ in this simplified division | $3\ \text{m}$: a 100 MHz broadcast |
| Microwave | Roughly $1\ \text{mm}$ to $1\ \text{m}$ | $0.125\ \text{m}$: 2.4 GHz |
| Infrared (IR) | Roughly $700\ \text{nm}$ to $1\ \text{mm}$ | $10\ \mu\text{m}$: thermal imaging |
| Visible | Approximately $400$–$700\ \text{nm}$ | $550\ \text{nm}$: green light |
| Ultraviolet (UV) | Roughly $10$–$400\ \text{nm}$ | $300\ \text{nm}$ |
| X-rays | Roughly $0.01$–$10\ \text{nm}$ | $0.1\ \text{nm}$: atomic-scale wavelength |
| Gamma rays | Conventionally the shortest-wavelength end; often below $0.01\ \text{nm}$ | $0.001\ \text{nm}$ |

Do not turn approximate boundaries into a claim of seven disjoint physical species. **Microwaves are a subset of radio-frequency radiation** in the broader engineering use of “radio”. Different charts draw that subdivision differently.

X-rays and gamma rays also overlap in energy. In atomic/nuclear work, X-rays are associated with electron processes, while gamma rays are associated with nuclear transitions and some particle processes. A hard X-ray need not have less energy than every gamma ray. The ordered seven-band diagram is a useful overview, not a universal source classifier. [IARC: X- and gamma-radiation](https://www.ncbi.nlm.nih.gov/books/NBK304365/)

Visible light runs **red → orange → yellow → green → blue → violet** as wavelength decreases and frequency increases. White light is a mixture of visible wavelengths; it is not an eighth region. [[Diffraction]] explains how a grating separates wavelengths, and [[Energy Levels and Line Spectra]] explains why particular sources supply only selected lines.

### 3. A brighter beam and a more energetic photon are different changes

Recall from [[Wave-Particle Duality]] that each photon has energy

$$E_\gamma=hf=\frac{hc}{\lambda_0}.$$

Here $h=6.626\times10^{-34}\ \text{J s}$. Higher frequency means more energy **per photon**. At a fixed frequency, a brighter beam instead carries more photons per second through a given area:

$$I=\Phi E_\gamma,$$

where $\Phi$ is the photon arrival rate per unit area. Wave amplitude and photon energy are not synonyms.

This explains why a high-power microwave oven can heat food while an individual microwave photon has far less energy than a visible photon. A huge number of low-energy photons can transfer a large total energy. It does not follow that any one of them can eject a tightly bound electron by single-photon absorption.

### 4. “Penetrating” means penetrating a particular material

Radiation may be **reflected**, **transmitted**, **absorbed** or scattered. Which happens depends on the material, wavelength, thickness and geometry.

Ordinary window glass transmits much visible light but blocks much of the long-wave infrared used by thermal cameras. Metal reflects radio-frequency waves well enough to make useful antenna reflectors and shielding. A wavelength that passes through one material may be strongly absorbed by another.

There is no rule “shorter wavelengths pass through everything better”. Your window is the counterexample: you see through it, while a typical long-wave thermal camera sees emission and reflection associated with the glass rather than a thermal view straight through it. [FLIR: what thermal imaging can see through](https://www.flir.com/discover/home-outdoor/can-thermal-imaging-see-through-walls/)

## Where it earns its keep — the mechanism behind the use

### Radio and microwaves: give the receiver a changing field

Accelerating charges in a transmitting aerial produce electromagnetic radiation. At the receiving aerial, the wave's electric field drives charges, producing an electrical signal. The receiver extracts information from controlled changes in that signal.

- **Radio and television broadcasting:** carry information over distance using a modulated carrier. Radio astronomy uses receiving systems to measure natural radio emission rather than an engineered message.
- **RFID:** a reader interrogates a tag, which returns identifying data. Some tags draw their operating energy from the reader's field; close-range inductive coupling and longer-range radiative systems are not identical mechanisms.
- **Mobile phones and wireless internet:** short wavelengths permit compact aerials. Microwaves can penetrate some walls, but losses depend strongly on the wall and frequency; metal or reinforced structures may block a link.
- **Satellite communication:** selected microwave bands can pass through the atmosphere and support directional links. A geostationary satellite stays approximately fixed in the sky for a ground observer; low-orbit satellites move across the sky and require changing links. The shorter path to low orbit reduces propagation delay. Some satellite-phone systems use low orbit, others geostationary orbit; direct-broadcast satellite television commonly uses geostationary satellites.

**Bluetooth is not a different substance from Wi-Fi.** Bluetooth uses the 2.4 GHz radio band, which also sits in the microwave range. A label using “radio” broadly and a diagram separating “microwave” narrowly can both be correct. [Bluetooth SIG: technology overview](https://www.bluetooth.com/learn-about-bluetooth/tech-overview/)

**Microwave ovens use absorption rather than information extraction.** The alternating electric field drives motion of polar molecules and ions in food; losses transfer energy into disordered molecular motion. The radiation is non-ionising, and heating the food this way does not make it radioactive. Absorption depth is finite, so “cooks everything uniformly from the inside out” is not a sound model. [FDA: microwave ovens](https://www.fda.gov/radiation-emitting-products/resources-you-radiation-emitting-products/microwave-ovens)

### Infrared: your remote is not your thermal camera

An infrared remote typically transmits coded pulses from an LED; the detector converts them into electrical signals. This is deliberately generated **near-infrared** light, not a picture of the remote's temperature.

A thermal camera detects longer-wavelength infrared emitted by objects. Human-temperature surfaces emit strongly around the ten-micrometre scale; a camera measures radiation in its detector band, then assigns visible colours to the measured signal. Temperature estimates also depend on emissivity and reflected surroundings. A shiny surface can mislead because it reflects radiation from elsewhere. The display's red, yellow or blue palette is a visual encoding, not the object's actual colour. [NASA: infrared waves](https://science.nasa.gov/ems/07_infraredwaves/)

A passive infrared intruder detector responds to changes in received infrared as a warm body moves across its sensing zones. An electric grill transfers energy partly by infrared radiation from its hot element; absorption raises the food's internal energy.

**Optical fibres** use visible light or selected near-infrared wavelengths where the fibre has low loss. In the ray model, a higher-index core and lower-index cladding guide light by total internal reflection. Signals can travel far before regeneration and can support large data rates with suitable sources, detectors and bandwidth. “Glass transmits infrared” must mean **some infrared bands**, not all: a fibre's useful near-IR window and a thermal camera's long-wave band are different intervals.

### Visible and ultraviolet: absorption can start chemistry

Visible photons are detected by photoreceptors in the eye and by photosensitive camera detectors. Illumination is useful because surfaces reflect different wavelength mixtures into our eyes; photography records that arriving distribution.

UV security marks and banknote features use **fluorescence**: a substance absorbs higher-energy radiation, loses part of that energy internally, and emits lower-energy visible light. You see the visible emission, not the incident UV itself.

Appropriate UV wavelengths can damage microbial genetic material, which is why UV is used to disinfect water. The effect depends on wavelength, delivered dose and whether the radiation reaches the microorganisms; “UV” is not a guarantee that every shadowed part has been treated.

### X-rays and gamma rays: images and deliberate energy deposition

An X-ray image measures **differential attenuation**: tissues and materials remove different fractions of the incident beam. A detector records the transmitted radiation. Bone commonly attenuates diagnostic X-rays more strongly than nearby soft tissue, creating contrast; airport baggage scanners exploit differences between materials too. “X-rays see through things” misses the useful part: an image exists because they do not pass through everything equally.

Gamma radiation can be used to sterilise medical equipment and food by damaging microorganisms. In nuclear imaging, radiation from an introduced tracer is detected outside the body; in radiotherapy, radiation deposits energy to damage targeted cells. Detection and treatment are different tasks—receiving a signal versus delivering a dose. [[Nuclear Physics]] explains the sources and decay processes; these uses do not make all electromagnetic radiation nuclear radiation.

### Astronomy: change the detector and a different sky appears

Cool material can be prominent in infrared, while very energetic processes can produce X-rays or gamma rays. Atmospheres transmit some wavelength ranges better than others, so a ground telescope and a space telescope have different windows. Much high-energy radiation is absorbed by Earth's atmosphere: to measure it directly from an astronomical source, put the detector above the absorbing atmosphere. [NASA: the electromagnetic spectrum](https://science.nasa.gov/ems/)

The Sun emits a broad spectrum, with most of its radiated power in infrared, visible and ultraviolet. A star's broad distribution and the narrow absorption lines laid over it carry different information: thermal radiation tells about temperature; lines identify species and, through [[Doppler Effect]], motion.

## Communication bridge — a continuous wave can carry digital information

**Analogue** information is represented by continuously varying signal values. **Digital** information is represented using a finite set of distinguishable symbols, commonly bits. Both are implemented by real physical signals; a digital transmission is not made of literal mathematical rectangles flying through space.

For sound, the chain is:

**air-pressure variation → microphone voltage → transmitted representation → received representation → loudspeaker motion.**

The voltage can modulate a carrier continuously (analogue). Alternatively, the transmitter can sample and quantise it, encode the samples as bits and modulate a carrier with those bits (digital). [[Sound Encoding]] explains sampling and quantisation; the electromagnetic carrier is what transports the encoded information.

### Why regeneration changes the distance you can communicate

Suppose a simplified digital link uses two received voltage levels, near 0 V and 1 V, with a decision threshold of 0.5 V.

| Intended bits | Received values / V | Regenerated symbols |
|---|---|---|
| `0 1 1 0` | `0.12 0.81 0.74 0.18` | `0 1 1 0` |
| `0 1 1 0` | `0.12 0.81 0.44 0.18` | `0 1 0 0` |

In the first case the receiver recognises each symbol and emits a fresh clean signal. It does not have to preserve the exact noisy voltage. In the second case the noise crossed a decision boundary, so regeneration confidently recreates the **wrong** bit.

An analogue amplifier amplifies the signal and the accumulated noise together. Digital regeneration can prevent small amplitude errors accumulating over successive links, extending the useful communication range. Error detection and correction can add protection, but digital does not mean infallible.

Digital systems can support high data rates through efficient coding, modulation and multiplexing. The engineering limits still include **bandwidth** (the frequency interval available) and signal-to-noise ratio. A higher carrier frequency is not itself a bit rate, and writing a sound in binary does not automatically make its transmission faster. [[Information Theory]] explains that limit; [[Error Detection and Correction]] explains how a receiver can notice corrupted data.

## Harmful effects — separate photon energy from total exposure

**Ionisation** means removing an electron from an atom or molecule. X-rays, gamma rays and sufficiently energetic UV photons can cause ionisation. There is no single UV wavelength that ionises every material: the threshold depends on what absorbs the photon. UV can also cause harmful photochemical changes without directly ionising the target. [NASA: introduction to the spectrum](https://science.nasa.gov/ems/01_intro/)

| Region | Mechanism relevant to excessive exposure |
|---|---|
| Microwaves | Absorbed energy can heat tissue internally |
| Infrared | Absorption can heat skin and cause burns |
| Ultraviolet | Photochemical damage to surface cells and eyes; associated skin and eye injury, including skin cancer |
| X-rays and gamma rays | Ionisation can damage cells and genetic material |

The lesson is neither “all radiation is dangerous” nor “non-ionising means harmless”. The consequences depend on wavelength, absorption, intensity, exposure time and tissue. Even visible light can damage an eye at sufficiently high intensity. **Radiation** is energy propagating outward; **radioactivity** is a property of unstable nuclei. A lamp emits radiation without being a radioactive source.

## Worked Examples — choose the tool from the feature

### 1. A telescope and its trace — Cambridge 9702/22/F/M/24, Q5

The paper gives a telescope's detection range as **12–28 μm** and asks for its spectral region. A second detector's oscilloscope trace has a full cycle spanning **6.0 cm** at **$5.0\times10^{-15}\ \text{s cm}^{-1}$**.

**Tool: scale comparison.** The input is a wavelength interval, so compare with the approximate boundaries: $12$–$28\ \mu\text{m}$ lies between visible and microwave wavelengths. It is **infrared**.

**Tool: period from a time axis.** The trace's horizontal scale is time, not distance travelled by the wave:

$$T=(6.0\ \text{cm})(5.0\times10^{-15}\ \text{s cm}^{-1})=3.0\times10^{-14}\ \text{s}.$$

**Tool: distance travelled in one period.** Electromagnetic propagation in free space selects $\lambda_0=cT$:

$$\boxed{\lambda_0=(3.0\times10^8)(3.0\times10^{-14})=9.0\times10^{-6}\ \text{m}.}$$

The scheme gives one mark for infrared and, for the calculation, credit for the period, the wave relationship and the answer. Its transverse-wave definition requires oscillations perpendicular to energy propagation. For electromagnetic waves, those oscillations are fields, not air particles.

### 2. Match the use—and explain the aerial — Cambridge 0625/43/O/N/25, Q5(a)

The paper pairs four uses with four regions. **Tool: identify the interaction before the label.**

| Use | Region in the question | Why it fits |
|---|---|---|
| Security marking | Ultraviolet | Absorption excites fluorescent material; visible emission reveals the mark |
| Bluetooth | Radio waves | Information is carried by a modulated radio signal |
| Optical fibres | Infrared | A suitable near-IR band has low loss in the fibre |
| Detection of cancer | Gamma rays | Emission from a tracer can be detected outside the body |

The published scheme awards two marks for all four matches, one for any two. For the mobile-phone advantage of microwaves, **a short aerial** is an accepted answer.

**Trigger → explanation:** a portable phone needs a compact receiving structure. At $2.4\ \text{GHz}$,

$$\lambda_0=\frac{3.0\times10^8}{2.4\times10^9}=0.125\ \text{m}.$$

A quarter wavelength is about $3.1\ \text{cm}$, showing why compact aerials are feasible. Real phone aerials are shaped and loaded structures, so this estimate is a scale argument, not a universal design formula. Bluetooth at that frequency is simultaneously radio-frequency radiation and microwave radiation; use the category the matching question supplies.

### 3. Same power, different photons — quantitative extension

Compare an idealised **1.0 W** monochromatic 2.4 GHz beam with a **1.0 W** monochromatic 500 nm beam. How many photons per second does each carry?

**Tool: energy per photon.** Frequency or wavelength is supplied, so use $E_\gamma=hf=hc/\lambda_0$:

- Microwave: $E_\gamma=(6.626\times10^{-34})(2.4\times10^9)=1.59\times10^{-24}\ \text{J}$.
- Visible: $E_\gamma=(6.626\times10^{-34})(3.0\times10^8)/(500\times10^{-9})=3.98\times10^{-19}\ \text{J}$.

**Tool: power as energy per second.** The supplied total power selects photon rate $R=P/E_\gamma$:

$$\boxed{\text{Microwave: }6.3\times10^{23}\ \text{photons/s};\qquad\text{visible: }2.5\times10^{18}\ \text{photons/s}.}$$

The visible photons individually carry about 250,000 times as much energy, but the beams deliver the same total energy per second. That is the distinction between photon energy and beam power made numerical.

## Common Misconceptions

1. **“Gamma rays are faster than radio waves.”** All travel at $c$ in vacuum. Higher frequency means more oscillations per second and shorter spacing. Check $f\lambda_0=c$.
2. **“Infrared is heat.”** Infrared is electromagnetic radiation. It can transfer energy by absorption; warm objects emit a spectrum, and hotter objects may emit substantial visible light too. A near-IR remote is not a thermal camera.
3. **“The band boundaries are exact.”** Visible sensitivity and naming conventions do not supply sharp universal walls. Learn useful orders of magnitude and the quoted visible range, then keep the approximation visible.
4. **“Higher frequency means greater intensity.”** Photon energy and photon arrival rate are separate factors. Example 3 holds power fixed while changing photon energy.
5. **“Digital signals cannot be corrupted.”** Regeneration works only when the receiver identifies the symbols correctly. A threshold-crossing error can survive regeneration.
6. **“Every transparent object is transparent to every wave.”** Transparency depends on wavelength and material. Compare a visible view through a window with a long-wave thermal view.

## Exam Notes

### Cambridge 9702 — AS §7.4

Three explicit objectives: all electromagnetic waves are transverse and share speed $c$ in free space; recall approximate wavelength ranges of the principal regions; recall **400–700 nm** for visible light. The boundary table and Example 1 address these directly. The numerical ranges are approximate, but the visible interval is the syllabus's stated range.

The photon-energy extension uses A-Level §22 ideas; it is not an extra AS §7.4 objective. **Polarisation and Malus's law are the separate §7.5**, treated in [[Polarisation]].

### Cambridge 0625 — §3.3 Core and Supplement

**Core:** spectrum order in both directions; common high speed in vacuum; the named uses and excessive-exposure effects; microwave links with low-orbit/geostationary satellites. **Supplement:** $3.0\times10^8\ \text{m s}^{-1}$ in vacuum, approximately the same in air; mobile/wireless aerials and wall penetration; Bluetooth radio signals weakened by walls; visible/IR optical fibres; analogue versus digital sound transmission and the benefits of digital signalling.

Give the mechanism when explaining a use: “short aerial”, “absorbed radiation heats food”, “different attenuation creates contrast”, “correctly recognised symbols are regenerated”. A list of gadgets alone does not explain why the wave is suitable. Cambridge's separate naming of Bluetooth radio and phone microwaves is compatible with the broader radio-frequency classification.

### IB Physics — C.2, SL and HL

C.2 includes the nature of electromagnetic waves and their differences from mechanical waves. Its guidance explicitly refers to the **data booklet** for approximate wavelength orders of magnitude across the seven regions. This supports the already-covered wave model; it is not a new quantum topic merely because photons are mentioned. Photon-energy and line-spectrum connections also meet the E.2/E.1 treatments in [[Wave-Particle Duality]] and [[Energy Levels and Line Spectra]].

### AP Physics 2 — Topic 14.4

Oscillating mutually perpendicular electric/magnetic fields; transverse propagation; no medium; wavelength classification; spectrum order and visible colour order. A **plane wave** has planar wavefronts: over a small patch of a distant wave, the fronts can be approximated as parallel planes. This is a local geometrical model, not a claim that every source emits an infinite flat sheet.

The CED explicitly says **exact wavelength ranges are not required**. Polarisation belongs to **14.3, Boundary Behavior of Waves and Polarization**, not 14.4. Do not attach a Malus-law memorisation requirement to 14.4; the 14.3 text specifies qualitative polarisation and possible intensity reduction.

### AP Physics C: Electricity & Magnetism — the narrower connection

**13.2.A.4** connects Maxwell's equations to electromagnetic waves and their constant free-space speed. The accompanying boundary explicitly excludes mathematically deriving that speed. This is relevant context, not an AP-C requirement to learn the seven-band applications table. The full wave-equation derivation remains enrichment in [[Maxwell's Equations]].

### Where it is not examined as this topic

**AP Physics 1 and AP Physics C: Mechanics** do not contain the electromagnetic-spectrum topic. Cambridge maths 0580/0606/9709/9231 do not examine this band taxonomy. The detailed molecular heating mechanism, antenna quarter-wavelength estimate and photon-rate comparison extend beyond the basic spectrum-recall objectives.

## Connections

- **Imaging application:** [[X-rays and CT]] — electron acceleration, photon energies and attenuation become an internal image.

- **Parents:** [[Progressive Waves]] supplies $v=f\lambda$; [[Maxwell's Equations]] explains why one field theory covers the whole spectrum; [[Superposition and Interference]] and [[Diffraction]] explain how wavelengths can be separated and measured.
- **Next:** [[Polarisation]] — select a direction of electric-field oscillation rather than a wavelength.
- **Quantum bridge:** [[Wave-Particle Duality]] gives $E_\gamma=hf$; [[Energy Levels and Line Spectra]] connects selected photon energies to atomic transitions; [[Nuclear Physics]] supplies nuclear gamma sources.
- **Information bridge:** [[Sound Encoding]] turns sound into samples and bits; [[Error Detection and Correction]] and [[Information Theory]] explain corruption, redundancy and capacity.
- **Astronomy bridge:** [[Doppler Effect]] uses shifts in a spectrum to reveal motion.

---

## LaTeX Reference

| Expression | LaTeX | Use |
|---|---|---|
| $c=f\lambda_0$ | `c=f\lambda_0` | Vacuum relation |
| $\lambda_0=cT$ | `\lambda_0=cT` | From a measured period |
| $E_\gamma=hc/\lambda_0$ | `E_\gamma=hc/\lambda_0` | Energy per photon |
| $I=\Phi E_\gamma$ | `I=\Phi E_\gamma` | Photon energy versus photon flux |
