---
chinese: 叠加与干涉 (diéjiā yǔ gānshè)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Stationary Waves]]"
leads_to:
  - "[[Diffraction]]"
  - "[[Sound Waves]]"
  - "[[Electromagnetic Spectrum]]"
  - "[[Wave-Particle Duality]]"
tags:
  - subject/physics
  - domain/waves
  - domain/optics
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-8-3
  - syllabus/IB-Physics-C-3-3
  - syllabus/IB-Physics-C-3-4
  - syllabus/AP-Physics-2-14-6
  - syllabus/AP-Physics-2-14-8
  - syllabus/AP-Physics-2-14-9
  - misconception/coherence-means-same-frequency
  - misconception/fringe-spacing-bright-to-dark
  - misconception/dark-fringes-get-darker
  - misconception/interference-destroys-energy
  - type/deep
---

# Superposition and Interference 叠加与干涉

> *Two waves arrive at the same point. The medium does both. Where they arrive in step it moves twice as far; where they arrive half a cycle apart it does not move at all. Everything in this card is that one sentence, asked at many points at once.*

![[superposition-interference-manim.mp4]]

## Definition

### Formal

**Superposition:** when two or more waves meet at a point, the resultant displacement is the sum of the displacements each wave would produce there alone.

**Interference** is the pattern that superposition produces when two waves overlap over a region: places of **constructive interference**, where the waves arrive in phase and the amplitudes add, and places of **destructive interference**, where they arrive in antiphase and the amplitudes subtract. For two sources emitting in phase, a point at distances $r_1$ and $r_2$ from them has **path difference** $\Delta = \lvert r_2 - r_1\rvert$ and phase difference

$$\Delta\phi = 2\pi\,\frac{\Delta}{\lambda},$$

so the point is a maximum when $\Delta = n\lambda$ and a minimum when $\Delta = (n + \tfrac12)\lambda$, for whole numbers $n$.

Two sources are **coherent** if the phase difference between their waves is **constant in time**. A stable interference pattern can be observed only from coherent sources.

**Young's double slit:** two narrow slits a distance $a$ apart, lit by the same coherent light of wavelength $\lambda$, throw equally spaced bright fringes on a screen a distance $D \gg a$ away, with spacing

$$x = \frac{\lambda D}{a} \qquad\text{equivalently}\qquad \lambda = \frac{ax}{D}.$$

### Intuitive

Drop two stones into a pond at once. Each makes rings; where the rings cross, the water does both motions, and along certain lines it heaves double while along others it lies flat. Those lines do not move: they are the places where the two sets of rings are permanently in step or permanently out of step, and they are fixed by geometry alone, by how much further one stone is than the other. Young's experiment is the same pond with light, and the fringe spacing is the pond's line spacing, scaled by $\lambda D/a$. The word "coherent" is the promise that the two stones keep time with each other; two lamps do not, so two lamps make no fringes.

### 中文锚点

叠加原理：两列波在同一点相遇，该点的位移是两列波各自单独引起的位移之和。干涉是叠加在一片区域里留下的图样：两波同相到达的地方振幅相加（相长干涉），反相到达的地方振幅相减（相消干涉）。对两个同相波源，一点到两波源的**路程差** $\Delta$ 决定了**相位差** $\Delta\phi = 2\pi\Delta/\lambda$：$\Delta = n\lambda$ 是极大，$\Delta = (n+\tfrac12)\lambda$ 是极小。**相干**指两波的相位差**不随时间改变**——只有相干波源才能给出稳定的、看得见的干涉图样，两盏独立的灯永远不行。杨氏双缝：缝距 $a$，屏距 $D$，波长 $\lambda$，则亮条纹等间距，间距 $x = \lambda D/a$。三件容易记反的事：相干说的不是"频率相同"而是"相位差恒定"；$x$ 是相邻**亮**纹之间的距离，亮纹到相邻暗纹只有它的一半；光源变亮时亮纹更亮、暗纹仍然是暗的、间距不变。这张卡把这些全部用代码算一遍：两波源的水波图样、杨氏条纹间距、相干与不相干波源时间平均的对比、拍频、以及肥皂膜的彩色。

---

## Part I — Two waves in one place

[[Stationary Waves]] stated the principle and said why it holds: the restoring force in a medium is proportional to displacement, a proportional law adds, so two disturbances travel through each other and the medium simply does both. This card asks the next question. If the two waves come from *different places*, where does the sum come out large and where does it come out zero?

Take two pulses on a rope first, because a pulse shows the arithmetic without any wavelength to think about. A crest meeting a crest passes through as a double-height crest for the instant they overlap, then each goes on its way unchanged. A crest meeting a trough of the same size passes through as a moment of *flat rope*, and then both reappear. Nothing was destroyed in that flat instant: every particle of the rope was at zero displacement but moving fast, and the energy was all kinetic. That is worth holding onto, because "the waves cancel" is a sentence students later read as "the energy vanishes", and it never does.

For continuous waves the same addition happens at every point and every instant, and the result depends on one thing: **the phase difference between the two waves at that point**. In phase, the resultant amplitude is $A_1 + A_2$; in antiphase, $\lvert A_1 - A_2\rvert$; anything else, somewhere between. If the two amplitudes are equal the antiphase sum is exactly zero, which is why the experiments below use equal sources: only then are the minima truly dark.

---

## Part II — Path difference: where the pattern comes from

Two sources $S_1$ and $S_2$ emit in phase with the same wavelength. Stand at a point $P$. The wave from $S_1$ has travelled $r_1$, the wave from $S_2$ has travelled $r_2$, and since each wave falls one cycle behind per wavelength travelled ([[Progressive Waves]]'s phase relation), the wave that travelled further arrives behind by

$$\Delta\phi = 2\pi\,\frac{r_2 - r_1}{\lambda} = 2\pi\,\frac{\Delta}{\lambda}.$$

Everything follows from reading this off:

- $\Delta = 0, \lambda, 2\lambda, \dots$ — a whole number of cycles behind is no lag at all: **in phase, constructive, a maximum**.
- $\Delta = \tfrac12\lambda, \tfrac32\lambda, \dots$ — half a cycle behind: **antiphase, destructive, a minimum**.

The set of points with $r_2 - r_1 = $ constant is a **hyperbola** with the sources as foci, so the maxima lie on a fan of hyperbolae spreading out from between the sources, with the minima on the hyperbolae between them. Far from the sources the hyperbolae straighten into lines, which is why a ripple tank shows a fan of still lines radiating from the two dippers. The central line, $\Delta = 0$, is the perpendicular bisector of $S_1S_2$: equidistant from both, always a maximum.

![[superposition-interference-ripple.svg|700]]

None of this was put into the figure. `superposition-interference-sim.py` adds the two circular waves point by point across the tank and then goes looking: along a line 30 cm from the dippers it finds maxima at $x = -10.7, 0, +10.7$ cm and measures the path difference there as $1.00, 0.00, 1.00$ wavelengths, and minima at $\pm 5.1$ and $\pm 17.4$ cm with path differences $0.50$ and $1.50$. The whole numbers landed on the maxima and the halves on the minima because the geometry made them, not because the script was told.

> [!tip] The exam's two questions
> Both boards ask the same pair over and over: *given the path difference, what is the phase difference?* ($\Delta\phi = 360^\circ \times \Delta/\lambda$, so $1.5\lambda \to 540^\circ$) and *is this point bright or dark?* (whole $\lambda$ bright, half $\lambda$ dark). Answer with the number, then the word.

---

## Part III — Coherence: why two lamps give no fringes

Everything above assumed the sources emit *in step*, or at least with a lag that never changes. That is the whole content of **coherence**: the phase difference between the two waves is **constant in time**. Same frequency is necessary but not the definition, because two sources of the same frequency can still drift: an ordinary lamp emits light in bursts about $10^{-8}$ s long, each burst starting at a random phase, so two lamps have a phase difference that jumps randomly a hundred million times a second.

What that does to the pattern is the point most students miss, and the simulation makes it plain. At **any single instant** two independent lamps produce a *perfect* set of fringes; the fringes are just in a different place each instant. Averaged over the response time of an eye or a camera the pattern washes out to uniform light.

![[superposition-interference-coherence.svg|800]]

The script measures the **visibility** $(I_{\max} - I_{\min})/(I_{\max} + I_{\min})$ of the time-averaged pattern: $1.000$ for a constant phase difference, $1.000$ at any single instant of two independent lamps, and $0.009$ for those same lamps averaged over two thousand random phase jumps. The fringes exist either way. Only a constant phase difference holds them still long enough to be seen.

This is why every two-source experiment derives both sources from **one**: two dippers on one vibrating bar, two loudspeakers on one signal generator, two slits lit by one laser or one lamp behind a single slit. Copies of one wave are coherent with each other by construction.

> [!warning] The examiners' wording
> "Coherent" earns the mark for **constant phase difference**. Cambridge's reports say the same frequency alone is insufficient, and that "*same* phase difference" is wrong because it treats phase difference as a property each wave has rather than a comparison between the two. Write *constant*, and say *between the two waves*. The same reports mark down candidates who mention coherence in a stationary-wave question: there is one source and its reflection there, and coherence is a two-source idea.

---

## Part IV — Young's double slit, and $\lambda = ax/D$

![[superposition-interference-young.svg|700]]

In 1801 Thomas Young let sunlight through a pinhole, then through two pinholes close together, and saw coloured fringes on the wall: two-source interference with light, which meant light was a wave, and the fringe spacing gave its wavelength, a length nobody had measured before. Newton's corpuscles took a century to die of it.

**The geometry.** Two slits $S_1$, $S_2$ a distance $a$ apart, a screen a distance $D$ away with $D \gg a$, a point $P$ on the screen a distance $x$ from the central point $O$. The two rays to $P$ are almost parallel, at an angle $\theta$ to the axis with $\tan\theta = x/D$. Drop a perpendicular from $S_1$ onto the ray from $S_2$; the little right triangle at the slits has hypotenuse $a$ and angle $\theta$, so the extra distance the lower ray travels is

$$\Delta = a\sin\theta.$$

For the small angles of any real double slit, $\sin\theta \approx \tan\theta = x/D$, so $\Delta \approx ax/D$. The $n$th bright fringe is where $\Delta = n\lambda$:

$$x_n = \frac{n\lambda D}{a}, \qquad\text{so adjacent fringes are}\qquad x = x_{n+1} - x_n = \frac{\lambda D}{a}.$$

The fringes are **equally spaced** because $\Delta$ grows linearly with $x$ under the small-angle approximation, and the approximation is very good: the simulation sums the two waves from the slits exactly, with no approximation, for $\lambda = 600$ nm, $a = 0.50$ mm, $D = 2.0$ m, and measures the spacing at $2.400$ mm against the formula's $2.400$ mm. It has to go out to the sixty-seventh fringe, $16$ cm off-axis at $4.6^\circ$, before the formula is one per cent out.

**What changes what.** Every exam variation is a reading of $x = \lambda D/a$:

| Change | Fringe spacing $x$ | Why |
|---|---|---|
| slits closer ($a$ halved) | doubles | the same path difference needs twice the angle |
| screen further ($D$ doubled) | doubles | the same angle reaches the screen twice as far out |
| red $\to$ blue ($\lambda$ smaller) | smaller | a whole wavelength of path difference comes sooner |
| brighter source | **unchanged** | bright fringes brighter; dark fringes stay dark |
| one slit covered | no fringes | one source cannot interfere with itself here |
| slits of unequal width | fringes never fully dark | the amplitudes differ, so antiphase leaves a remainder |

White light gives a white central fringe with coloured edges, because every colour has its maximum at $O$ but a different spacing outside it: red furthest, violet nearest. By the third or fourth fringe the colours overlap into white again, so a white-light pattern is short.

> [!tip] The trap that costs a factor of two
> $x$ is the distance between the centres of **adjacent bright fringes** (or adjacent dark ones). Bright-to-neighbouring-dark is $x/2$. And "the distance across $N$ fringes" contains $N - 1$ spacings: eight bright fringes spanning $22$ mm means $x = 22/8$? No: seven gaps, $x = 22/7 = 3.14$ mm. The Cambridge scheme for June 2023 takes $22/8$, so its figure's $22$ mm spans eight fringe *widths*, edge to edge, not eight centres; read what the marked distance actually spans, count, and say which you counted.

---

## Part V — The four demonstrations the syllabus names

Cambridge's second learning outcome asks for the *experiments*, and each is the same experiment with a different detector.

- **Water in a ripple tank.** Two dippers on one vibrating bar, so they are coherent. The lines of calm water are the minima; illuminate from above and the maxima show as moving bright and dark bands, the minima as steady grey. Change the frequency and the lines close up (shorter $\lambda$); move the dippers apart and they close up too (larger $a$): the ripple tank *is* $x = \lambda D/a$ made of water.
- **Sound.** Two loudspeakers a metre or two apart on one signal generator, and a listener or a microphone walking across the room in front of them: loud, quiet, loud, quiet. At $1$ kHz, $\lambda = 34$ cm, and the quiet lines are a few tens of centimetres apart at a few metres' distance. Turn the frequency up and they crowd together.
- **Microwaves.** A $3$ cm transmitter behind a metal plate with two slits, and a probe receiver moved along a line beyond: the meter reads maximum, minimum, maximum every few centimetres. The examiners note that these are *intensity maxima and minima*, not "bright and dark fringes": there is nothing to see.
- **Light.** A laser and a double slit, screen a few metres away, and the pattern is on the wall. Before lasers, a lamp behind a *single* slit first, to make one coherent source, then the double slit: Young's own arrangement, and still the one IB draws.

**The conditions** for the fringes to be *observable*, which is the syllabus's third outcome and a standard three-mark question: the sources must be **coherent**; the waves must have roughly **equal amplitude** at the screen, or the minima are not dark; for light the two waves must be **of the same polarisation** (unpolarised light through two slits satisfies this automatically); and the slit separation must be small enough, and the screen far enough, that the fringes are wide enough to see, which is $x = \lambda D/a$ again. Slit *width* matters too: each slit must be narrow enough to diffract its light across the region where the other's arrives, which is [[Diffraction]]'s business.

---

## Part VI — Beats: interference in time instead of space

Play two tones of nearly the same frequency together, $440$ Hz and $444$ Hz, and you hear one note whose loudness rises and falls four times a second. This is superposition again, but the phase difference is changing with *time* rather than with position: the two waves are in step, drift out of step, and come back into step $\lvert f_1 - f_2\rvert$ times per second. Adding them,

$$\sin(2\pi f_1 t) + \sin(2\pi f_2 t) = 2\cos\!\left(2\pi\,\tfrac{f_1 - f_2}{2}\,t\right)\,\sin\!\left(2\pi\,\tfrac{f_1 + f_2}{2}\,t\right),$$

a tone at the average frequency whose amplitude is the slow cosine. The amplitude passes through zero twice per cosine cycle, so the loudness pulses at

$$f_{\text{beat}} = \lvert f_1 - f_2\rvert.$$

![[superposition-interference-beats.svg|700]]

The simulation adds the two tones, finds the envelope's minima $0.250$ s apart, and reads off $4.00$ Hz. Tuning any instrument uses it: play the string against a reference, and the beats slow as the string comes into tune, stopping when it is there. Zero beats is a far finer test than a human ear's sense of pitch, which is why a piano tuner listens for the *wobble* rather than the note.

---

## Part VII — Thin films: the colours of a soap bubble

A soap film, an oil slick on a puddle, the purple tint on a camera lens: all two-source interference where the two sources are the film's **two surfaces**. Light reflects from the top surface and from the bottom; the second ray has travelled an extra $2t$ through the film of thickness $t$ (at normal incidence), where the wavelength is shorter, $\lambda/n$, so the extra path in *wavelengths* is $2nt/\lambda$. One more thing: a wave reflecting off a **denser** medium (higher $n$) is inverted, a phase change of $\pi$, exactly as a wave on a rope inverts at a fixed end ([[Stationary Waves]]). Reflecting off a *less* dense medium it is not. For a soap film in air the top reflection flips and the bottom does not, so the two reflected rays are in phase when

$$2nt = \left(m + \tfrac12\right)\lambda \quad\text{(bright)}, \qquad 2nt = m\lambda \quad\text{(dark)}.$$

![[superposition-interference-film.svg|700]]

Each colour has its own set of thicknesses at which it reflects, so a film of varying thickness shows bands of colour, and a film thinner than about $\lambda/20$ reflects *nothing* at any visible wavelength: the top of a draining soap bubble goes black just before it bursts. The simulation confirms the maxima at $2nt/\lambda = 0.50, 1.50, 2.50$ and the minima at $1.00, 2.00, 3.00$, and the reflectance going to zero as $t \to 0$.

An **anti-reflection coating** runs the argument backwards: a layer of magnesium fluoride ($n = 1.38$) on glass ($n = 1.5$). Now *both* reflections are off denser media, both flip, and the flips cancel; the rays are in antiphase when $2nt = \lambda/2$, so a quarter-wavelength coating, about $100$ nm for green light, kills the reflection of the colour the eye is most sensitive to. What is left, weakly reflected red and blue, is the purple sheen on every camera lens and pair of spectacles. Oil on water is the middle case: oil ($n \approx 1.5$) is denser than water ($1.33$), so only the top reflection flips, and the AP question below turns on exactly that.

---

## Where it is the working tool

- **The coating on every lens.** Part VII's quarter-wave layer is on your phone camera, your glasses and every element of a telescope; multi-layer versions reflect less than $0.1\%$ across the visible. A twelve-element zoom lens with no coatings would lose half its light to reflections and fill the image with ghosts.
- **LIGO.** The gravitational-wave detectors are two-source interferometers four kilometres on a side: one laser split into two beams, recombined so that they cancel; a passing gravitational wave changes one arm's length by less than a proton's width, the cancellation slips by a measurable fraction of a fringe, and the 2015 detection was a change in that light. It is Part II with a path difference of $10^{-18}$ m.
- **Radio telescopes the size of the Earth.** Two dishes thousands of kilometres apart record the same source; combining the signals with the right delay makes them a two-slit experiment with $a$ the baseline, so the angular resolution is $\lambda/a$ of a telescope that size. That is how the Event Horizon Telescope imaged a black hole's shadow in 2019.
- **Noise-cancelling headphones.** A microphone samples the sound arriving at your ear; the electronics emit the same wave in antiphase; Part I's flat rope, on purpose, tens of thousands of times a second. It works well below about $1$ kHz, where the wavelength is long compared with the ear cup and the phase can be matched.
- **Tuning by beats.** Every orchestra tunes to an oboe's A by listening for the beats to stop, and every guitar tuner that matches two strings by ear is Part VI.
- **Optical fibre and thin-film sensing.** Interferometric sensors measure strain, temperature and pressure by the fringe shift in a fibre loop; a Fabry–Pérot cavity, two parallel surfaces, is the film of Part VII used as a ruler with sub-nanometre resolution.

---

## Worked examples — every tool named

### Example 1 — the whole double-slit question (Cambridge 9702, June 2022 Paper 22, Q5)

Laser light of wavelength $660$ nm falls normally on two slits $0.44$ mm apart; a screen is $1.8$ m away. O is the central bright fringe, P the next dark fringe below it, Q the next bright, R the next dark.

*(a) State what is meant by coherent.* — **Constant phase difference** between the waves. *(The scheme: "constant phase difference (between the waves)", B1.)*

*(b) For the waves superposing at R, (i) the path difference in nm, (ii) the phase difference.* — *Tool: count fringes from the centre.* O is $\Delta = 0$, P is $\tfrac12\lambda$, Q is $\lambda$, R is $\tfrac32\lambda$: $\Delta = 1.5 \times 660 = 990$ nm. *Tool: $\Delta\phi = 360^\circ \times \Delta/\lambda$* $= 360^\circ \times 1.5 = 540^\circ$. *(Scheme: $990$ nm; $540^\circ$. It does not reduce $540^\circ$ to $180^\circ$, and neither should you unless asked.)*

*(c) The fringe spacing.* — *Tool: $x = \lambda D/a$, selected because the question gives all three and asks for the fourth* $= (660 \times 10^{-9})(1.8)/(0.44 \times 10^{-3}) = 2.7 \times 10^{-3}$ m. *(Scheme: $2.7$ mm.)*

*(d) The intensity of the light on the slits is increased. Compare the appearance of the fringes before and after.* — Bright fringes **brighter**; dark fringes **unchanged**; fringe **spacing unchanged**. *(Three B marks, one each. The report: most candidates got "brighter", a common misconception was that the dark fringes get darker, and only the stronger ones remembered to say what stayed the same. A comparison includes the unchanged.)*

*(e) Blue light replaces the red. State and explain how the slit separation must change to keep the same fringe spacing.* — Blue has the **shorter wavelength**; from $x = \lambda D/a$, to keep $x$ fixed, **decrease** $a$. *(M1 A1.)*

### Example 2 — eight fringes, seven gaps (Cambridge 9702, June 2023 Paper 21, Q5(b)–(c))

Light of wavelength $6.2 \times 10^{-7}$ m, slits $2.8$ m from the screen; the distance across eight bright fringes is $22$ mm. Find the slit separation, then the path difference and phase difference at the first dark fringe Q.

*Tool: read the figure for what "$22$ mm" spans.* The scheme takes $x = 22/8 = 2.75$ mm: the marked $22$ mm spans eight fringe widths, not eight centres. *Tool: $a = \lambda D/x$* $= (6.2 \times 10^{-7})(2.8)/(2.75 \times 10^{-3}) = 6.3 \times 10^{-4}$ m. *(Scheme: $x = 22/8$, C1; $a = 6.3 \times 10^{-4}$ m, A1.)* At Q, the first dark fringe: $\Delta = \lambda/2 = 3.1 \times 10^{-7}$ m; and at R, the first bright fringe beyond it, the phase difference is one full cycle, $360^\circ$. *(Scheme: $3.1 \times 10^{-7}$ m; $360^\circ$.)* Had the $22$ mm been centre-to-centre of the first and eighth fringes there would be seven gaps; the figure decides.

### Example 3 — why P is bright, and the sketch (Cambridge 9702, March 2023 Paper 22, Q5(b)–(c))

Wavelength $630$ nm, slits $3.6 \times 10^{-4}$ m apart, adjacent bright fringes $4.0 \times 10^{-3}$ m apart. *(i) Explain why a bright fringe forms at the central point P.* — P is equidistant from the two slits, so the **path difference is zero**, the waves arrive **in phase**, and interfere constructively. *(Scheme: path difference zero or phase difference zero, so constructive, B1.)* *(ii) Find $D$.* — *Tool: $D = ax/\lambda$* $= (3.6 \times 10^{-4})(4.0 \times 10^{-3})/(630 \times 10^{-9}) = 2.3$ m. *(Scheme: $2.3$ m.)* *(c) Sketch $x$ against $\lambda$ from $400$ to $700$ nm.* — $x = \lambda D/a$ is **proportional** to $\lambda$: a straight line of positive gradient, and since the axis starts at $400$ nm, not zero, the line starts from a **non-zero** $x$. *(Scheme: upward-sloping straight line starting from a non-zero value at $400$ nm, B1. Starting from the origin loses the mark: the origin of the graph is not $\lambda = 0$.)*

### Example 4 — nine dark fringes, and the curve (Cambridge 9702, June 2025 Paper 21, Q4)

*(a) State the principle of superposition.* — When two or more waves **meet at a point**, the resultant displacement is the **sum of the individual displacements**. *(Two B marks, one per idea.)*

*(b)* Wavelength $7.2 \times 10^{-7}$ m, slits $0.16$ mm apart; the distance between the centres of the first and ninth dark fringes is $3.2$ cm. *(i) Find $D$.* — *Tool: nine fringes, centre to centre, is eight spacings:* $x = 3.2 \times 10^{-2}/8 = 4.0 \times 10^{-3}$ m. *Tool: $D = ax/\lambda$* $= (0.16 \times 10^{-3})(4.0 \times 10^{-3})/(7.2 \times 10^{-7}) = 0.89$ m. *(Scheme: $x = 3.2 \times 10^{-2}/8$; $D = 0.89$ m.)* *(ii) The slit separation is decreased from $0.16$ mm to $0.04$ mm. Sketch the spacing $x$ against $a$.* — $x \propto 1/a$: a curve of **negative gradient whose magnitude decreases**, through $(0.16, 0.4)$, $(0.08, 0.8)$ and $(0.04, 1.6)$ cm. *(Three B marks: the shape, the end point, the two intermediate points, so the sketch must be quantitative: halving $a$ doubles $x$.)*

### Example 5 — the graph experiment (Cambridge 9702, November 2021 Paper 23, Q5(c))

The fringe spacing $x$ is measured for several screen distances $D$ and plotted; the gradient is $G$. *(i) Express $a$ in terms of $G$ and $\lambda$.* — *Tool: $x = \lambda D/a$ is a straight line through the origin with gradient $\lambda/a$*, so $G = \lambda/a$ and $a = \lambda/G$. *(ii) The slits are replaced by ones of separation $2a$; sketch the new line.* — Gradient halves: a straight line from the origin, everywhere below the first, at half its height at the largest $D$. *(Scheme: M1 A1.)*

### Example 6 — the best question from another board: the distant galaxy (IB Physics HL, May 2018 TZ1 Paper 2, Q3(a))

Coherent light from a distant galaxy, wavelength $633.0$ nm, on slits $0.300$ mm apart. *(i) Explain how a dark fringe is formed.* — The waves from the two slits arrive with a **path difference of $(n + \tfrac12)\lambda$**, so they are in **antiphase** and superpose to give (near) zero amplitude: destructive interference. *(ii) Outline why the beam must be coherent for the fringes to be visible.* — Only with a **constant phase difference** does each point on the screen keep the same path-difference condition over time; otherwise the pattern shifts randomly and averages to uniform illumination (Part III's simulation is the answer in numbers). *(iii) The separation between a dark and a bright fringe is $4.50$ mm; calculate $D$.* — *Tool: dark-to-bright is half a fringe spacing,* so $x = 9.00$ mm. *Tool: $D = ax/\lambda$* $= (0.300 \times 10^{-3})(9.00 \times 10^{-3})/(633.0 \times 10^{-9}) = 4.27$ m. The IB question plants the factor-of-two trap in the wording, which is why it is here.

### Example 7 — the oil slick (AP Physics 2, 2018 Free Response Q4(b))

Oil leaking from a boat forms a thin film on the water, and one area looks mostly green. Explain in detail how constructive interference contributes to the green appearance, given that oil has a higher refractive index than water. — Four scoring points, and the answer must hit each: the green is the **interference of two reflected waves**, one from the air–oil surface and one from the oil–water surface; there is a **phase change of $\pi$ at one reflection only** (air to oil, the denser medium; oil to water is denser to less dense, no flip); the wavelength of the light **inside the oil is shorter**, $\lambda/n$; and the two waves have a **path difference** of twice the film thickness, so for the film's thickness there the condition $2nt = (m + \tfrac12)\lambda$ is met for green and not for the other colours. *(Scoring guidelines: one point each for two-wave interference, the phase shift, the different wavelength in oil, and the path-length difference.)*

### Example 8 — slits under water (AP Physics 2, 2022 Free Response Q1(b))

A double slit is submerged in a tank of water and lit by a laser; the water is then replaced with a fluid of greater refractive index. Describe, in terms of speed, frequency and wavelength, how the pattern changes. — The light's **speed is lower** in the new fluid ($v = c/n$); its **frequency does not change** at a boundary; so by $v = f\lambda$ its **wavelength is shorter**; and by $x = \lambda D/a$ (AP writes $d\sin\theta = m\lambda$) the fringes are **closer together**. *(Five points: the speed relation, frequency unchanged, $v = f\lambda$, wavelength to fringe spacing, and a coherent paragraph. Frequency being fixed is the step candidates skip, and it is the one that makes the argument go.)*

---

## Hands-on

- **`superposition-interference-sim.py`** — the ripple tank summed and its maxima located; Young's fringes with the small-angle error tracked to the sixty-seventh fringe; the coherence experiment with visibilities; beats; the soap film. Change `a`, `D` or `lam` in `young()` and watch the table in Part IV come true.
- **`superposition-interference-figures.py`** — the five figures; **`superposition-interference-manim.py`** — the ripple tank live, then the fringes as $a$, $\lambda$ and $D$ change.
- **Two phones.** Play $440$ Hz on one and $444$ Hz on the other, side by side: four beats a second. Change the second to $441$ Hz: one beat a second, slow enough to count. Then set both to $440$ Hz and walk across the room in front of them: loud and quiet lines, Part V's loudspeaker experiment for free.
- **A bubble.** Blow a soap film on a loop of wire and hold it vertical in daylight. The film drains, thickest at the bottom, so the colour bands sweep downward, and the top goes **black** just before it breaks. That black is Part VII's $t \to 0$ line: the film is reflecting nothing.

---

## Common Misconceptions (Teaching Notes)

### 1. "Coherent means the same frequency"
Same frequency is necessary and not sufficient. Coherent means **constant phase difference**; two independent lamps of identical frequency are not coherent, because each restarts its phase at random every few nanoseconds. The Cambridge report is explicit that frequency alone earns nothing, and that "same phase difference" is also wrong.

### 2. "Fringe spacing is from a bright fringe to the next dark one"
It is bright to the **next bright** (or dark to dark). Bright-to-dark is half a spacing, and using it gives an answer a factor of two out, the single most common numerical error in the reports. Count gaps, not fringes: $N$ fringes centre to centre is $N - 1$ spacings.

### 3. "Make the light brighter and the dark fringes get darker"
The dark fringes are where equal amplitudes cancel; make both amplitudes bigger and they still cancel: **dark stays dark**. Bright fringes get brighter and the spacing does not move. State all three; the mark scheme has one mark for each.

### 4. "Destructive interference destroys the energy"
Energy is **redistributed**, not lost: the total over the screen is exactly the sum of what the two slits let through, the bright fringes carrying four times one slit's intensity and the dark ones none, averaging to twice. In the pulse picture the flat rope at the moment of cancellation is all kinetic energy.

### 5. "Slit separation and fringe separation are the same thing"
$a$ is on the slide, fractions of a millimetre; $x$ is on the screen, millimetres. The report names the confusion. In $\lambda = ax/D$ they multiply, so swapping them changes nothing numerically, which is exactly why the error survives to the "explain" parts, where it is fatal.

### 6. "Microwaves show bright and dark fringes"
They show **maxima and minima of the detector reading**. "Bright" is a word for light; the examiners note candidates "perhaps confusing microwaves with visible light".

### 7. "The graph of $x$ against $\lambda$ starts at the origin"
$x \propto \lambda$ does go through the origin, but when the axis starts at $400$ nm the drawn line must start at a non-zero $x$. The mark is for reading the axes, not for the proportionality.

---

## Exam Notes

### Cambridge 9702 (§8.3 Interference — Paper 1 and Paper 2)

Four learning outcomes: understand **interference** and **coherence**; understand experiments demonstrating two-source interference with **water in a ripple tank, sound, light and microwaves**; understand the **conditions** for two-source fringes to be observed; recall and use $\lambda = ax/D$. Paper 2 sets it roughly every other series as a six-to-nine-mark question of the Example 1 shape: define coherent (1), path difference and phase difference at a named fringe (1 + 1), $\lambda = ax/D$ (2–3), then a comparison or a sketch (2–3). The reports' standing complaints, all in the misconceptions above: coherence as frequency only; "same" for "constant"; bright-to-dark as $x$; dark fringes darkening; slit versus fringe separation. §8.2 and §8.4, single-slit diffraction and the grating, are [[Diffraction]]; a Paper 2 question sometimes runs §8.3 and §8.4 together, so know that the grating's maxima are at $d\sin\theta = n\lambda$ and are sharper and further apart.

### IB Physics (C.3.3 and C.3.4 — SL and HL)

C.3.3: superposition of waves and pulses; the conditions for two-source interference; constructive and destructive path-difference conditions. C.3.4: Young's double slit and $s = \lambda D/d$ (IB's letters: $s$ for spacing, $d$ for slit separation). IB asks "explain how a dark fringe is formed" and "why must the beam be coherent" as prose, and sets the data-booklet formula in traps like Example 6's dark-to-bright distance and May 2023's "nine successive fringes"; it also links the measurement to *uncertainty*: moving the screen closer makes the fringes narrower, the same absolute error in measuring $s$ becomes a larger fractional error, and $\lambda$ inherits it. C.3.5 and C.3.6 (single-slit envelope, gratings, HL) are [[Diffraction]].

### AP Physics 2 (Units 14.6, 14.8 and 14.9)

14.6.A: interference and superposition, constructive and destructive, **beats** with $f_{\text{beat}} = \lvert f_1 - f_2\rvert$ and tuning forks as the standard context; 14.6.B, standing waves, is [[Stationary Waves]]. 14.8: the double-slit pattern as diffraction plus interference, $\Delta L = d\sin\theta = m\lambda$, and the small-angle $y_m = m\lambda L/d$; the single-slit envelope on the pattern is [[Diffraction]]. 14.9: thin-film interference with $2nt = m\lambda$ or $(m + \tfrac12)\lambda$ depending on the phase changes, and the free-response questions want the reasoning in words, as Examples 7 and 8 show: the paragraph-length response is scored for the chain *speed → frequency fixed → wavelength → spacing*, not for a number.

### Where it is *not* examined

- **Cambridge 0625** has no interference: §3.1 stops at reflection, refraction and diffraction at openings, all of them qualitative. A double slit is the first thing the A-Level adds.
- **AP Physics 1** has no waves beyond sound and standing waves; **AP Physics C** has no waves at all.
- **9709 and 9231** do not touch it.

---

## Connections

- **Builds on:** [[Progressive Waves]] — phase difference $2\pi\Delta x/\lambda$, now applied to two waves from two places; [[Stationary Waves]] — the superposition principle and its reason, the $\pi$ phase change at a fixed end that Part VII reuses.
- **Extends into:** [[Diffraction]] — the single slit's own pattern, the envelope on Young's fringes, and the grating that sharpens them; [[Sound Waves]] — beats and loudspeaker interference with air as the medium; [[Electromagnetic Spectrum]] — the coatings and interferometers that measure light with itself.
- **Bridges:** [[Trigonometric Identities]] — the sum-to-product formula that turns two tones into a carrier and an envelope in Part VI; the hyperbola of Part II is the locus of points with a constant difference of distances to two foci, the same curve as in [[Hyperbolic Functions]]' name.
- **Extends into:** [[Wave-Particle Duality]] — the two-slit pattern as a probability density: photons drawn from it one at a time still draw the fringes.

---

## Beyond Syllabus

### The intensity is $\cos^2$, and the energy adds up
Two equal waves with phase difference $\Delta\phi$ have resultant amplitude $2A\cos(\Delta\phi/2)$, so the intensity along a Young's screen is $I = 4I_0\cos^2(\pi a x/\lambda D)$: peaks of $4I_0$, zeros between, average $2I_0$, which is the two slits' light exactly. Interference moves energy; it never loses any.

### Phasors
Add waves as arrows of length $A$ at angle $\phi$: the resultant is the vector sum. Two arrows at $180^\circ$ cancel; three equal sources at $120^\circ$ cancel; $N$ slits give $N$ arrows, and where they line up the intensity is $N^2 I_0$. That last one is the diffraction grating's whole secret, and [[Diffraction]] cashes it.

### One photon at a time
Send light through Young's slits so faintly that only one photon is in flight at once, and the fringes still build up, dot by dot, over hours. Each photon interferes with itself; block one slit and the fringes vanish even though every photon that arrives went through the other. Electrons, neutrons and molecules of several hundred atoms have been made to do the same. The double slit, Feynman said, contains the only mystery of quantum mechanics.

### Michelson, and why LIGO's arms are four kilometres
Split one beam, send the halves down two arms, bring them back to the same detector: the intensity depends on the arms' path difference to a fraction of a wavelength, and Michelson and Morley used it in 1887 to look for the aether wind and found none. LIGO is the same instrument with the arms folded to $1{,}120$ km of effective path and the mirrors' motion measured to $10^{-19}$ m.

---

## LaTeX Reference

| Rendered | Source | Meaning |
|---|---|---|
| $\Delta\phi = 2\pi\,\dfrac{\Delta}{\lambda}$ | `\Delta\phi = 2\pi\,\dfrac{\Delta}{\lambda}` | phase difference from path difference |
| $\Delta = n\lambda,\ (n+\tfrac12)\lambda$ | `\Delta = n\lambda,\ (n+\tfrac12)\lambda` | constructive, destructive |
| $x = \dfrac{\lambda D}{a}$ | `x = \dfrac{\lambda D}{a}` | Young's fringe spacing |
| $\Delta = a\sin\theta$ | `\Delta = a\sin\theta` | path difference at angle $\theta$ |
| $f_{\text{beat}} = \lvert f_1 - f_2\rvert$ | `f_{\text{beat}} = \lvert f_1 - f_2\rvert` | beat frequency |
| $2nt = (m+\tfrac12)\lambda$ | `2nt = (m+\tfrac12)\lambda` | thin-film bright (one phase flip) |
| $I = 4I_0\cos^2\!\left(\dfrac{\pi a x}{\lambda D}\right)$ | `I = 4I_0\cos^2\!\left(\dfrac{\pi a x}{\lambda D}\right)` | double-slit intensity |
