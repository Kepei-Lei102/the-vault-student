---
chinese: 行波 (xíngbō)
prerequisites:
  - "[[Simple Harmonic Motion]]"
  - "[[Hooke's Law for Springs]]"
  - "[[Stress, Strain and Young Modulus]]"
  - "[[Trigonometric Graphs]]"
leads_to:
  - "[[Stationary Waves]]"
  - "[[Superposition and Interference]]"
  - "[[Doppler Effect]]"
  - "[[Electromagnetic Spectrum]]"
  - "[[Polarisation]]"
  - "[[Sound Encoding]]"
tags:
  - subject/physics
  - domain/waves
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-7-1
  - syllabus/9702-7-2
  - syllabus/0625-3-1
  - syllabus/IB-Physics-C-2-1
  - syllabus/IB-Physics-C-2-2
  - syllabus/AP-Physics-2-14-1
  - syllabus/AP-Physics-2-14-2
  - type/deep
  - type/definition
  - misconception/the-particles-travel-with-the-wave
  - misconception/a-longitudinal-graph-shows-a-transverse-wave
  - misconception/frequency-changes-at-a-boundary
  - misconception/intensity-is-proportional-to-amplitude
  - misconception/wave-speed-depends-on-the-source
  - misconception/wavelength-is-crest-to-trough
---

# Progressive Waves 行波

> *Shake one end of a rope and a hump runs to the other end. Nothing ran. Every piece of rope went up and came back down where it started, and yet something arrived at the far end with enough energy to knock a cup off a table. That "something" is a wave: not a thing that travels but a **pattern of motion that is handed on**, each piece of the medium dragging its neighbour into the same oscillation a moment later. Everything on this card — wavelength, frequency, the equation $v = f\lambda$, phase, intensity, the two graphs the examiners never tire of — follows from taking that handing-on seriously.*

## Definition

### Formal

A **progressive (travelling) wave** is a disturbance that transfers **energy** from one place to another **without any net transfer of matter**: each particle of the medium oscillates about a fixed equilibrium position, and the *pattern* of those oscillations moves through the medium at the **wave speed** $v$.

- **Displacement** $x$ (or $y$) — the distance of a particle from its equilibrium position, with sign.
- **Amplitude** $A$ — the maximum displacement.
- **Wavelength** $\lambda$ — the distance between two adjacent points that are in phase (crest to next crest).
- **Period** $T$ — the time for one particle to complete one oscillation; **frequency** $f = 1/T$ — oscillations per second.
- **Phase difference** $\Delta\phi$ — how far through its cycle one oscillation is compared with another, in degrees or radians: $\Delta\phi = 360^\circ \times \Delta x/\lambda$ for two points $\Delta x$ apart on one wave.
- **Wave speed** $v = f\lambda = \lambda/T$.
- **Transverse** — particles oscillate at right angles to the direction of energy transfer; **longitudinal** — parallel to it.
- **Intensity** $I$ — power transferred per unit area normal to the wave, $I = P/A_{\text{area}}$, with $I \propto A^2$.

### Intuitive

A stadium wave. The crowd's wave sweeps round the ground at a definite speed; not one spectator moves a metre from their seat. Each person stands and sits *once per wave* — that is their oscillation — and does it a moment after the person on their left, which is the only thing that makes the pattern travel. The wave has a *length* (how many seats from one standing peak to the next), a *frequency* (how often you have to stand if waves keep coming), and a *speed* set by how quickly each person reacts to their neighbour — not by how enthusiastically anyone jumps. **The source decides the frequency; the medium decides the speed; the wavelength is what those two settle on between them.**

### 中文锚点

体育场里的**人浪**：一波"浪"绕场一圈，速度很快，可没有一个观众离开过座位——每个人只是**站起来再坐下**，比左边的人**晚一点**。这个"晚一点"就是行波的全部秘密：**传出去的是动作的模式，不是人**。举个手边的例子：抖动晾衣绳的一端，绳上跑过去一个"包"，绳子本身哪儿也没去；一只手一次一次地抖，是**波源**，它决定**频率**（一秒抖几次）；绳子多紧多重，是**介质**，它决定**波速**；两者合起来定出**波长**——相邻两个波峰的距离。**波速 = 频率 × 波长**，就是"每秒过去几个波峰"乘"每个波峰多长"。绳子在"包"经过的地方上下起伏，"包"却沿绳往前跑，这是**横波**；从一端一推一拉弹簧，一疏一密的形状就沿着弹簧传过去，这是**纵波**——声音就是空气里的纵波。考试最爱考的两张图要分清："**照片**"（某一刻整根绳子的形状，横轴是距离，读出波长）和"**录像**"（某一点随时间上下的记录，横轴是时间，读出周期）。

> [!info] Symbols in this card
> | Symbol | Meaning | 中文 | Unit |
> |---|---|---|---|
> | $x$, $y$ | displacement of a particle from equilibrium | 位移 | m |
> | $A$ | amplitude | 振幅 | m |
> | $\lambda$ | wavelength | 波长 | m |
> | $T$, $f$ | period, frequency $= 1/T$ | 周期、频率 | s, Hz |
> | $v$ | wave speed | 波速 | m s⁻¹ |
> | $\phi$, $\Delta\phi$ | phase, phase difference | 相位、相位差 | rad or ° |
> | $I$ | intensity $= P/\text{area}$ | 强度 | W m⁻² |
> | $\omega$ | angular frequency $= 2\pi f$ | 角频率 | rad s⁻¹ |
> | $T_{\text{s}}$, $\mu$ | string tension, mass per unit length | 张力、线密度 | N, kg m⁻¹ |

## Part I — What travels, and why it has a speed

Take the rope and look closely at one small piece of it. It is pulled on by its two neighbours, and only by them. When the piece on the left rises, the rope between them tilts and the tension lifts *this* piece; when this piece rises, it lifts the next. Every piece is a mass on a spring made of its neighbours — [[Simple Harmonic Motion]] with the restoring force supplied by the rope's tension instead of a coil — and the whole rope is a chain of them, each coupled to the next. A wave is **coupled SHM**: one oscillation handed down a line of oscillators.

That picture explains three things at once.

- **Why the particles stay home.** Each piece is tied to its equilibrium position by the neighbours on both sides; it can oscillate about that position but has nothing to carry it along the rope. The *motion* travels; the *matter* does not.
- **Why energy travels.** A piece in motion does work on the next piece as it drags it into oscillation; that piece does work on the one after. Energy passes down the line at the rate the neighbours can pass it, with no piece keeping it.
- **Why there is a definite speed, and what sets it.** The handing-on takes time: a piece must be pulled before it moves, and how fast it responds depends on how hard the rope pulls (the tension $T_{\text{s}}$) against how much mass must be got moving (the mass per metre $\mu$). Tighter and lighter is faster. The result, derived in the Beyond-syllabus section, is $v = \sqrt{T_{\text{s}}/\mu}$ — and the thing to notice is that **nothing about the source appears in it**. Shake harder or faster and the wave goes at the same speed. The medium owns $v$.

`progressive-waves-sim.py` builds exactly this — three thousand beads on a string, joined by tension, the first bead driven in SHM, Newton's second law integrated bead by bead with no wave physics put in — and measures what emerges: a disturbance travelling at $20.0\ \text{m s}^{-1}$ on a string with $\sqrt{T_{\text{s}}/\mu} = 20$; a bead far down the string oscillating with the driver's amplitude and period, just later; a bead a quarter wavelength further on lagging by a quarter period. Doubling the driving frequency halves the wavelength and leaves the speed untouched. Doubling the amplitude quadruples the power the driver has to supply — the $I \propto A^2$ of Part IV, measured rather than asserted.

![[progressive-waves-manim.mp4]]

## Part II — The vocabulary, and the two graphs that carry it

A wave can be recorded two ways, and the exam expects you to read either and know which you are holding.

![[progressive-waves-two-graphs.svg|1000]]

**The photograph** — a **displacement–distance** graph — freezes time and shows every particle's displacement along the medium at one instant. Its horizontal axis is *position*, and the repeat distance you read off it is the **wavelength** $\lambda$: crest to crest, trough to trough, or any point to the next point doing the same thing. The vertical extreme is the **amplitude**.

**The film at one point** — a **displacement–time** graph — fixes one particle and shows how its displacement changes as the wave passes through it. Its horizontal axis is *time*, and the repeat you read off it is the **period** $T$; its reciprocal is the **frequency** $f$. The shape is the SHM graph from [[Simple Harmonic Motion]], because that is what one particle does.

The two graphs have the same shape and mean different things, which is why the axes must be read before anything else. The commonest lost mark in this topic is the wavelength read off a time axis.

### Deriving $v = f\lambda$

The syllabus asks for the derivation, and it is three lines from the definitions. In one period $T$, every particle completes one oscillation — so the whole pattern has moved on by exactly one repeat, one wavelength. Speed is distance over time:

$$v = \frac{\text{distance the pattern moves in one period}}{\text{one period}} = \frac{\lambda}{T} = f\lambda .$$

Read it as a sentence: **$f$ crests pass a fixed point every second, each crest is $\lambda$ long, so $f\lambda$ metres of wave go past per second.** The equation is not a law of nature; it is what "wavelength", "frequency" and "speed" *mean*, arranged.

### Phase, and phase difference

![[progressive-waves-phase.svg|900]]

Two particles on the same wave do the same oscillation at different moments. Their **phase difference** measures the lag as a fraction of a cycle, scaled to $360^\circ$ or $2\pi$ rad:

$$\Delta\phi = 2\pi\,\frac{\Delta x}{\lambda} \qquad (\text{or } 360^\circ \times \Delta x/\lambda).$$

Half a wavelength apart means half a cycle apart — $180^\circ$, **antiphase**: one at a crest while the other is at a trough. A whole wavelength apart means a whole cycle apart, which is no difference at all — **in phase**. A quarter wavelength gives $90^\circ$, the lag the simulation measured. The word *difference* matters: phase difference is a comparison **between two oscillations**, never a property one wave has on its own — a slip the examiners have named in print.

The single expression that carries all of this is the equation of a sinusoidal wave travelling in the $+x$ direction:

$$y(x,t) = A\sin\!\left(2\pi f t - \frac{2\pi x}{\lambda}\right) = A\sin(\omega t - kx),$$

with $k = 2\pi/\lambda$. Fix $t$ and it is the photograph; fix $x$ and it is the film; the $-kx$ is the phase lag of the particle at $x$ behind the one at the origin.

## Part III — Transverse and longitudinal

![[progressive-waves-long-trans.svg|700]]

The direction of travel is fixed by where the energy goes. The particles can oscillate **across** that direction or **along** it, and that is the whole distinction:

| | Transverse 横波 | Longitudinal 纵波 |
|---|---|---|
| particle motion | perpendicular to energy transfer | parallel to energy transfer |
| what the pattern looks like | crests and troughs | compressions (particles crowded) and rarefactions (particles spread) |
| examples | waves on a rope or string, ripples on water, all electromagnetic waves, seismic S-waves | sound in any medium, a pushed spring (slinky), seismic P-waves |
| can it be polarised? | yes — the oscillation has a direction to restrict | no — the oscillation is already fixed along the travel |

Both are drawn with the same graph, and that is the trap. A **displacement–distance graph of a longitudinal wave** plots each particle's displacement *along* the direction of travel on the vertical axis, so it looks exactly like a transverse wave. It is not a picture of the medium. On that graph a **compression** sits where the displacement crosses zero going *down* — particles to the left displaced right, particles to the right displaced left, all crowding in — and a **rarefaction** where it crosses zero going *up*. The crests of the graph are not compressions; they are the particles displaced furthest forward. The bottom panel of the figure above shows the same wave both ways.

Sound is the longitudinal wave that matters most: a loudspeaker cone pushes the air in front of it, that layer pushes the next, and a train of compressions and rarefactions travels out at about $340\ \text{m s}^{-1}$ in air while each parcel of air merely oscillates in place. Its intensity is what the ear calls loudness and its frequency what the ear calls pitch. [[Sound Encoding]] takes the story from the microphone diaphragm — which does exactly this oscillation — into the digital world.

## Part IV — Energy and intensity

A wave carries energy because every particle in it is oscillating, and an oscillating particle has energy. [[Simple Harmonic Motion]] gives the amount: a particle of mass $m$ with amplitude $A$ and angular frequency $\omega$ carries total energy $\tfrac12 m\omega^2 A^2$. The wave delivers that energy onward at speed $v$, so the **power** it transports — and therefore the energy crossing any surface per second — is proportional to $A^2$ (and, for a given medium, to $f^2$ as well).

**Intensity** is that power spread over the area it crosses:

$$I = \frac{P}{\text{area}}, \qquad I \propto A^2 .$$

Two consequences are examined, and the first is where marks are lost:

![[progressive-waves-intensity.svg|1000]]

- **Amplitude and intensity are not the same thing.** Tripling the intensity of a sound multiplies its amplitude by $\sqrt{3} \approx 1.7$, not by 3. Doubling the amplitude of a wave quadruples its intensity. The mark schemes are written to catch the linear guess.
- **A point source spreads its power over a sphere.** At distance $r$ the area is $4\pi r^2$, so $I = P/4\pi r^2$: the **inverse-square law**, and with it $A \propto 1/r$. The Sun at Earth delivers about $1.4\ \text{kW m}^{-2}$ from $3.8 \times 10^{26}\ \text{W}$ spread over a sphere of radius $1.5 \times 10^{11}\ \text{m}$ — the arithmetic works.

## Part V — Reading a wave off an oscilloscope

A cathode-ray oscilloscope draws a displacement–time graph live: the microphone's signal drives the spot up and down while the **time-base** sweeps it across the screen at a set number of seconds per centimetre, and the **Y-gain** sets how many volts each centimetre of height represents.

![[progressive-waves-cro.svg|760]]

The two settings turn a picture into numbers. Count the centimetres for one complete cycle and multiply by the time-base to get the **period**; invert for the frequency. Measure the height of a peak above the centre line and multiply by the Y-gain to get the **amplitude** as a voltage. The trace above — one cycle in $4.0$ cm at $0.50\ \text{ms cm}^{-1}$ — is a $500$ Hz signal; a peak of $2.5$ cm at $2.0\ \text{V cm}^{-1}$ is $5.0$ V. Exam questions run the calculation both ways: given the trace, find the settings; given a new intensity, redraw the trace. Note what the CRO does *not* show: distance. A wavelength never comes off a screen without a speed to multiply the period by.

## Part VI — Waves meeting things: the ripple tank

A tray of water, a motor-driven bar dipping at its edge, a lamp above and a screen below: the shadows of the wavefronts make a wave visible. A **wavefront** is a line joining points that are in phase — one crest, say — and the direction of travel is always at right angles to it. The tank shows the three things every wave does when it meets an obstacle, and the IGCSE examines them as descriptions:

- **Reflection** at a plane barrier: the wavefronts bounce off with the angle of reflection equal to the angle of incidence, exactly as for a ray of light. Wavelength, speed and frequency are unchanged.
- **Refraction** where the depth changes: water waves travel more slowly in shallow water. Frequency cannot change at the boundary — the crests arrive at the same rate they leave — so by $v = f\lambda$ the **wavelength shortens** with the speed, and wavefronts that cross the boundary at an angle **bend** towards the normal. Deep to shallow: speed down, wavelength down, frequency the same. It is the same physics as light entering glass.
- **Diffraction** through a gap or round an edge: the wavefronts spread out beyond the obstacle. The effect is strongest when the gap is about the same size as the wavelength — narrow the gap, or lengthen the wave, and the emerging wavefronts curve more; a gap many wavelengths wide passes the wave almost straight. At an edge, the longer the wavelength the further the wave bends round it, which is why bass passes round a door and treble does not.

The middle bullet carries the one rule that transfers everywhere: **at a boundary, frequency is fixed by the source and does not change; speed changes with the medium; wavelength follows.**

## Worked examples — every tool named

### Example 1 — the CRO, twice (Cambridge 9702, March 2023 Paper 22, Q5(a))

> A microphone and CRO analyse a sound wave of frequency $5000$ Hz; the trace shows $1.5$ cycles across $6.0$ cm with amplitude $1.0$ cm. (i) Determine the time-base setting. (ii) The intensity is increased from $I$ to $3I$ at the same frequency; sketch the new trace.

*Tool: period from frequency, then time-base = time per centimetre. Trigger: a trace with a known frequency and a measured width.* $T = 1/5000 = 2.0 \times 10^{-4}$ s. Six centimetres hold $1.5$ periods, i.e. $3.0 \times 10^{-4}$ s, so the time-base is $3.0 \times 10^{-4}/6.0 = 5.0 \times 10^{-5}\ \text{s cm}^{-1}$.

*Tool: $I \propto A^2$, so $A \propto \sqrt{I}$. Trigger: "intensity increased by a factor of 3" — the question is testing whether you triple the amplitude.* New amplitude $= 1.0 \times \sqrt{3} = 1.7$ cm; same period, so the same $1.5$ cycles across the screen. The examiners' report for this paper records that a large number drew $3.0$ cm.

### Example 2 — a wavelength from a time-base (Cambridge 9702, March 2024 Paper 22, Q5(c))

> A detected electromagnetic wave is displayed on an oscilloscope; one cycle spans $6.0$ cm with the time-base at $5.0 \times 10^{-15}\ \text{s cm}^{-1}$. Calculate the wavelength.

*Tool: $T$ from the screen, then $\lambda = cT$ (which is $v = f\lambda$ with $f = 1/T$). Trigger: an electromagnetic wave — the speed is $c$ and needs no measuring.* $T = 6.0 \times 5.0 \times 10^{-15} = 3.0 \times 10^{-14}$ s; $\lambda = 3.0 \times 10^8 \times 3.0 \times 10^{-14} = 9.0 \times 10^{-6}$ m — $9\ \mu$m, in the infrared, which is what the previous part had asked you to identify.

### Example 3 — directions, and a wavelength from a speed (Cambridge 9702, June 2023 Paper 22, Q5(a)–(b))

> A progressive wave makes a particle vibrate along line P while the energy propagates along line Q. Compare the directions of P and Q for (i) a transverse and (ii) a longitudinal wave. (b) Sound of frequency $1700$ Hz travels at $340\ \text{m s}^{-1}$; find its wavelength.

*Tool: the definitions.* Transverse: P perpendicular to Q. Longitudinal: P parallel to Q. *Tool: $\lambda = v/f$.* $\lambda = 340/1700 = 0.20$ m.

### Example 4 — the ripple tank (Cambridge 0625, June 2026 Paper 43, Q5)

> (a) Complete: in a longitudinal wave the vibration is ___ to the direction of propagation; give an example. (b) A ripple-tank wave has wavelength $0.016$ m and speed $0.12\ \text{m s}^{-1}$; find its frequency with unit. The wave passes from shallow to deep water — say what happens to wavelength, frequency and speed. (c) The wave passes through a small gap in a barrier: name the effect, and state two changes that each increase the curvature of the emerging wavefronts.

*Tool: the definitions, then $f = v/\lambda$, then the boundary rule.* Parallel; sound (or seismic P-waves). $f = 0.12/0.016 = 7.5$ **Hz**. Shallow to deep: wavelength *increases* (given), frequency *stays the same*, speed *increases* — the frequency row is the one that tests understanding. (c) Diffraction; make the gap narrower, or make the wavelength longer (a gap comparable to the wavelength gives the most spreading).

### Example 5 — the best question from another board: a longitudinal wave from its film (IB Physics HL, November 2021 Paper 2, Q2)

> A longitudinal wave travels at $340\ \text{m s}^{-1}$. A graph shows the displacement $x$ of one particle P against time: a sinusoid of amplitude $6\ \mu$m and period $4.0$ ms; positive displacement means "to the right". (a) Calculate the wavelength. (b) Determine the magnitude and direction of P's acceleration at $t = 2.0$ ms, when $x = -6\ \mu$m.

*Tool: the graph is a film, so it gives $T$; then $\lambda = vT$. Trigger: the axis is time and the speed is given — the wavelength must be built, not read.* $T = 4.0 \times 10^{-3}$ s, $f = 250$ Hz, $\lambda = 340 \times 4.0 \times 10^{-3} = 1.36 \approx 1.4$ m.

*Tool: the particle is in SHM, so $a = -\omega^2 x$. Trigger: "acceleration of the particle" — a wave question that is really an SHM question.* $\omega = 2\pi/T = 1.57 \times 10^3\ \text{s}^{-1}$; $a = \omega^2 x_0 = (1.57 \times 10^3)^2 \times 6 \times 10^{-6} = 14.8 \approx 15\ \text{m s}^{-2}$, directed **to the right** — opposite to the displacement, which at that instant is to the left. Nothing about the *wave* travelling right or left enters part (b): the particle's acceleration is the SHM restoring acceleration, full stop.

### Example 6 — two corks on a water wave (IB Physics HL, May 2023 TZ1 Paper 2, Q3(a))

> A transverse water wave travels to the right; the diagram shows the surface at $t = 0$ with corks P and Q floating $8$ m apart, one on a crest and the other in the trough, and a wavelength of $16$ m read from the axes. (i) State what is meant by a transverse wave. (ii) The frequency is $0.50$ Hz; calculate the speed. (iii) Plot P's position at $t = 0.50$ s. (iv) Show the phase difference between the corks is $\pi$ rad.

*Tools, in order: the definition (particles oscillate perpendicular to the direction of energy transfer); $v = f\lambda = 0.50 \times 16 = 8.0\ \text{m s}^{-1}$; the particle stays at its own $x$ — after $0.50$ s, a quarter of the $2.0$ s period, P has moved a quarter cycle vertically and not at all horizontally (the scheme's point is at P's original $x$, $8$ m, with the new height); and $\Delta\phi = 2\pi\,\Delta x/\lambda = 2\pi \times 8/16 = \pi$.* Part (iii) is the one that separates candidates: a cork on a travelling wave does not travel.

## Hands-on

- **`progressive-waves-sim.py`** — the bead-and-tension string. Change `T` or `mu` and watch $\sqrt{T_{\text{s}}/\mu}$ reappear in the measured speed; change `f` and watch $\lambda$ adjust while $v$ does not; change `A` and watch the driver's power go as $A^2$. Every claim in Part I is a number this script prints.
- **`progressive-waves-figures.py`** — the five figures; the CRO panel takes a time-base and a Y-gain and redraws the trace, which is the March 2023 question in reverse.
- **`progressive-waves-manim.py`** — the two scenes: particles staying home while the pattern travels, and the photograph beside the film.
- **A phone and a rope.** Film a slow wave on a skipping rope at 240 fps; step through frames to see one knot in the rope rise and fall in place while the hump passes. It is the cheapest demonstration in physics and the most convincing.

## Common Misconceptions (Teaching Notes)

### 1. "The particles travel along with the wave"
They oscillate about a fixed point; the pattern travels. A cork on a water wave bobs and stays; a spectator in a stadium wave stands and sits. The examiners' report for June 2024 Paper 2 notes that the direction of *particle* motion "seemed to be poorly understood by candidates of all abilities" — arrows drawn along the wave instead of up or down.

### 2. "This graph shows a transverse wave" — of a displacement–distance graph for sound
A displacement–distance graph of a longitudinal wave looks identical to that of a transverse one; the vertical axis is displacement *along* the travel. Compressions are at the downward zero-crossings, not at the crests. Always ask what the vertical axis measures before deciding what kind of wave you are looking at.

### 3. "The frequency changes when the wave enters shallow water / glass"
The frequency is set by the source and is preserved across every boundary — crests cannot pile up or vanish at an interface. Speed changes; wavelength changes with it; frequency does not. The June 2026 IGCSE table above is built to catch exactly this.

### 4. "Triple the intensity, triple the amplitude"
$I \propto A^2$, so amplitude scales as $\sqrt{I}$: a factor $3$ in intensity is $1.7$ in amplitude; doubling amplitude quadruples intensity. This is the single most reliably lost mark on the topic.

### 5. "A louder or faster shake makes the wave go faster"
The medium sets the speed — tension and mass per length for a string, bulk properties and temperature for air. The source sets frequency and amplitude only; the wavelength is whatever $v/f$ comes to. The simulation doubles $f$ and $A$ and measures the same $20\ \text{m s}^{-1}$ each time.

### 6. "Wavelength is crest to trough"
Crest to trough is half a wavelength. Wavelength is the distance between adjacent points *in phase* — crest to the next crest, or any point to the next point at the same displacement moving the same way. Half-wavelengths read as wavelengths double every frequency on the paper.

## Exam Notes

### Cambridge 9702 (Topic 7.1 and 7.2 — Paper 1 and Paper 2)

- **§7.1** — describe wave motion via ropes, springs and ripple tanks; understand and use displacement, amplitude, phase difference, period, frequency, wavelength and speed; the **CRO** (time-base and Y-gain for frequency and amplitude); *derive* $v = f\lambda$ from the definitions and use it; energy transfer by a progressive wave; **intensity = power/area** and **intensity ∝ amplitude²**. **§7.2** — compare transverse and longitudinal waves and analyse their graphical representations.
- **Paper 2's standing shapes** are all above: the CRO with a given frequency (time-base out) or a given time-base (frequency or wavelength out); "intensity is increased by a factor of $n$, redraw the trace" (amplitude $\times\sqrt n$); phase difference between two labelled points on a displacement–distance graph, in degrees or radians; "compare the directions of the vibration and of the energy" for the two wave types; $\lambda = v/f$ for sound at $340\ \text{m s}^{-1}$.
- **Paper 1** likes the two graphs: which quantity can be read off which axis, the phase difference between two points, and a combined power–intensity–amplitude calculation that the June 2024 report describes as "challenging for all candidates".
- **Examiners' recurring notes:** the direction of particle motion is poorly drawn; "phase difference" treated as a property of one wave; $\sqrt{}$ forgotten between intensity and amplitude; a mixture of distances and times fed into speed = distance/time instead of $v = f\lambda$.
- The rest of Topic 7 — the Doppler effect (7.3), the electromagnetic spectrum (7.4) and polarisation with Malus's law (7.5) — and all of Topic 8 (stationary waves, diffraction, interference) build on this card and are examined with it.

### Cambridge 0625 (§3.1 General properties of waves — Papers 2 and 4)

- **Core:** waves transfer energy without transferring matter; wave motion via ropes, springs and ripple-tank experiments; the features wavefront, wavelength, frequency, crest, trough, amplitude and wave speed; **recall and use $v = f\lambda$**; transverse (electromagnetic radiation, water waves, seismic S-waves) with vibration at right angles to propagation, longitudinal (sound, seismic P-waves) with vibration parallel; describe reflection at a plane surface, refraction due to a change of speed, and diffraction through a gap, and the ripple-tank demonstrations of each (including diffraction at an edge).
- **Supplement:** how wavelength and gap size affect diffraction through a gap, and how wavelength affects diffraction at an edge.
- **Paper 4 shapes:** complete-the-sentence definitions with an example; $f = v/\lambda$ with the unit for a mark; the shallow-to-deep table (frequency unchanged); wavefront sketches through a gap — wider spreading for the narrower gap or the longer wavelength, with three wavefronts drawn at the *same* spacing as before the gap; identify which marked lengths on a diagram are one wavelength (crest to crest and trough to trough, never crest to trough).
- Light (§3.2), the electromagnetic spectrum (§3.3) and sound (§3.4) are the section's other three rows and each takes this card as read.

### IB Physics (C.2 Wave model — SL and HL)

- **C.2.1** — transverse versus longitudinal particle motion; displacement–distance and displacement–time graphs. **C.2.2** — $\lambda$, $T$, $f$, $v$, $A$; derive $v = f\lambda = \lambda/T$; the nature of sound waves and of electromagnetic waves, and the differences between mechanical and electromagnetic waves (a medium required or not; speed $c$ in vacuum).
- IB questions cross into SHM on purpose — the acceleration of a particle in a wave (Example 5), a cork's position a quarter period later (Example 6) — so the [[Simple Harmonic Motion]] tools travel with this card.
- The linking questions in the guide (why intensity falls with the inverse square, how a wave can travel through a vacuum) are Parts IV and III respectively.

### AP Physics 2 (Unit 14.1 and 14.2)

- **14.1** — wave pulses and periodic waves transfer energy without matter; mechanical waves need a medium, electromagnetic waves do not; wave speed depends on the medium: $c$ in vacuum for light, $v = \sqrt{F_T/(m/\ell)}$ for a string (the Beyond-syllabus derivation), and the speed of sound rising with temperature. **14.2** — periodic waves, $v = f\lambda$, transverse versus longitudinal, graphs.
- AP asks for the string formula explicitly, which no Cambridge paper does; everything else here is shared ground.

### Where it is *not* examined

**AP Physics 1** has no wave content since the 2024 redesign — waves moved entirely to Physics 2. **AP Physics C** examines no waves in either paper. **Edexcel IAL Physics** and **OxAQA** are not tracked here. Sound *as* a topic (pitch, loudness, echoes, ultrasound) is 0625 §3.4; the electromagnetic spectrum's ranges and uses are 9702 §7.4 and 0625 §3.3.

## Connections

- **Built on:** [[Simple Harmonic Motion]] — what every particle in a wave is doing, and the source of $\tfrac12 m\omega^2A^2$; [[Hooke's Law for Springs]] — the neighbours as springs, the coupled chain; [[Stress, Strain and Young Modulus]] — where $\sqrt{E/\rho}$ comes from as the speed of sound in a solid; [[Trigonometric Graphs]] — the sinusoid read two ways.
- **Same idea elsewhere:** [[Alternating Current]] — a displacement–time graph with volts on the vertical axis, read off the same CRO; [[Circular Motion]] — phase as an angle round a circle, and the radian measure $\Delta\phi$ is quoted in.
- **Extends into:** [[Stationary Waves]] — two progressive waves meeting head-on; [[Superposition and Interference]] — phase difference doing work, path difference and the two-source pattern; [[Doppler Effect]] — what happens to $f$ when the source moves; [[Electromagnetic Spectrum]] — the transverse waves that need no medium; [[Polarisation]] — the property only transverse waves have; [[Sound Encoding]] — the microphone diaphragm's oscillation sampled into bits.
- **Physics of the medium:** [[Kinetic Theory of Gases]] — why the speed of sound in air rises with temperature.

## Beyond Syllabus

### The wave equation, and where $v = \sqrt{T_{\text{s}}/\mu}$ comes from

Take a short piece of string of length $\delta x$ and mass $\mu\,\delta x$ under tension $T_{\text{s}}$, displaced transversely by $y(x,t)$. The tension pulls along the string at each end; for small slopes the vertical component at the right end is $T_{\text{s}}\,\partial y/\partial x$ evaluated there, and at the left end the same with the opposite sign. The net transverse force is the difference, $T_{\text{s}}\left[\partial y/\partial x\big|_{x+\delta x} - \partial y/\partial x\big|_{x}\right] \approx T_{\text{s}}\,\dfrac{\partial^2 y}{\partial x^2}\,\delta x$. Newton's second law for the piece:

$$\mu\,\delta x\,\frac{\partial^2 y}{\partial t^2} = T_{\text{s}}\,\frac{\partial^2 y}{\partial x^2}\,\delta x \quad\Longrightarrow\quad \frac{\partial^2 y}{\partial t^2} = \frac{T_{\text{s}}}{\mu}\,\frac{\partial^2 y}{\partial x^2}.$$

This is the **one-dimensional wave equation**, $\partial^2 y/\partial t^2 = v^2\,\partial^2 y/\partial x^2$. Substitute the travelling sinusoid $y = A\sin(\omega t - kx)$: the left side gives $-\omega^2 y$, the right gives $-v^2 k^2 y$, so $\omega = vk$ — which is $2\pi f = v \cdot 2\pi/\lambda$, i.e. $v = f\lambda$ again, now as a *consequence* of the dynamics — with $v = \sqrt{T_{\text{s}}/\mu}$. Any function of $(x - vt)$ whatever solves the equation: a pulse of any shape travels undistorted at the same $v$. This is the "spatial generalisation of coupled SHM" that the springs and SHM cards promise, and `progressive-waves-sim.py` is the discrete version of this derivation, run.

The same argument in a solid rod, with Young's modulus replacing tension per unit area, gives the speed of sound in a solid $v = \sqrt{E/\rho}$ — for steel about $5000\ \text{m s}^{-1}$; in a gas the compressibility takes the role and $v = \sqrt{\gamma p/\rho} = \sqrt{\gamma RT/M}$, which is why sound in air goes faster on a hot day ($\approx 331 + 0.6\,\theta\ \text{m s}^{-1}$ for $\theta$ in °C) and why it is the molecules' own speed in disguise.

### Dispersion — when the medium sets a different speed for every wavelength

A string obeys $v = \sqrt{T_{\text{s}}/\mu}$ for every frequency, so a pulse keeps its shape. Deep-water waves do not: $v = \sqrt{g\lambda/2\pi}$, long waves outrun short ones, and a storm's confused sea arrives at a distant shore sorted into a long slow swell followed by choppier waves days later. Light in glass does the same — blue slower than red — and the result is a prism's spectrum and a lens's colour fringes. A medium in which $v$ depends on $\lambda$ is called **dispersive**, and in it the speed of a *pattern* (phase velocity) and the speed of *energy* (group velocity) come apart — the reason "the wave speed" needs a footnote once you leave the string.

### Intensity as an energy flux, with the units checked

For a plane wave in a medium of density $\rho$, the energy per unit volume is $\tfrac12\rho\omega^2A^2$ (every particle's SHM energy per unit mass, times mass per volume), and it moves at $v$, so intensity — energy crossing unit area per second — is $I = \tfrac12\rho v\omega^2A^2$. Units: $\text{kg m}^{-3} \times \text{m s}^{-1} \times \text{s}^{-2} \times \text{m}^2 = \text{kg s}^{-3} = \text{W m}^{-2}$. The product $\rho v$ is the medium's **acoustic impedance**, the quantity that decides how much of a wave reflects at a boundary — and the reason an ultrasound scan needs gel between probe and skin.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $v = f\lambda$ | `v = f\lambda` | the definitions arranged |
| $\Delta\phi = 2\pi\,\Delta x/\lambda$ | `\Delta\phi = 2\pi\,\Delta x/\lambda` | phase difference from separation |
| $y = A\sin(\omega t - kx)$ | `y = A\sin(\omega t - kx)` | travelling wave, $k = 2\pi/\lambda$ |
| $I = P/A$, $I \propto A^2$ | `I = P/A,\ I \propto A^2` | intensity |
| $I = P/4\pi r^2$ | `I = P/4\pi r^2` | inverse square from a point source |
| $v = \sqrt{T_{\text{s}}/\mu}$ | `v = \sqrt{T_{\text{s}}/\mu}` | string; beyond 9702, on AP 2 |
| $\partial^2 y/\partial t^2 = v^2\,\partial^2 y/\partial x^2$ | `\partial^2 y/\partial t^2 = v^2\,\partial^2 y/\partial x^2` | the wave equation |
