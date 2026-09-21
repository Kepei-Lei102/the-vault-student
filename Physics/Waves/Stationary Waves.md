---
chinese: 驻波 (zhùbō)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Resonance]]"
  - "[[Simple Harmonic Motion]]"
  - "[[Sound]]"
leads_to:
  - "[[Quantum States and the Schrödinger Equation]]"
  - "[[Energy Levels and Line Spectra]]"
  - "[[Superposition and Interference]]"
  - "[[Diffraction]]"
  - "[[Sound Waves]]"
tags:
  - subject/physics
  - domain/waves
  - level/A-Level
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/9702-8-1
  - syllabus/IB-Physics-C-4-1
  - syllabus/AP-Physics-2-14-6
  - type/deep
  - type/definition
  - misconception/node-to-antinode-is-half-a-wavelength
  - misconception/a-stationary-wave-transfers-energy
  - misconception/phase-on-a-stationary-wave-grows-with-distance
  - misconception/the-string-bounces-off-the-wall
  - misconception/amplitude-is-the-same-everywhere
---

# Stationary Waves 驻波

> *Send a wave down a rope tied to a wall and it comes back. Keep sending, and for most frequencies the rope just writhes. At a few special frequencies something else happens: the rope settles into a fixed set of loops that swing in place — some points never move at all, others swing twice as far as the hand ever did, and nothing travels anywhere. Every stringed instrument, every pipe, every microwave oven, every laser cavity and every electron in an atom is doing this. It is what two identical waves do when they are made to run through each other in opposite directions, and the whole card is one identity: $\sin(kx - \omega t) + \sin(kx + \omega t) = 2\sin kx\cos\omega t$.*

## Definition

### Formal

The **principle of superposition**: when two or more waves meet at a point, the resultant displacement is the vector sum of the individual displacements.

A **stationary (standing) wave** is the pattern formed when two progressive waves of the **same frequency, wavelength and amplitude** travel through each other in **opposite directions** and superpose. The result is a wave profile that does not travel:

$$y(x,t) = 2A\sin(kx)\cos(\omega t),$$

whose **amplitude varies with position** — $2A\lvert\sin kx\rvert$ — and whose shape stays put.

- **Node**: a point where the amplitude is always zero. Adjacent nodes are **$\lambda/2$ apart**.
- **Antinode**: a point where the amplitude is a maximum, $2A$. Adjacent antinodes are $\lambda/2$ apart; a node and the next antinode are $\lambda/4$ apart.
- **Phase**: every point between two adjacent nodes oscillates **in phase**; points on opposite sides of a node are in **antiphase** ($180^\circ$).
- **Energy** is not transferred along a stationary wave; it is stored, swapping between kinetic and potential within each loop.

The wavelength of the underlying progressive waves can therefore be read from the pattern: **$\lambda = 2 \times$ (node-to-node distance)**, and the speed of those waves is still $v = f\lambda$.

### Intuitive

A skipping rope turned by two children is one loop of a stationary wave: the ends (their hands) are nodes, the middle is an antinode, and the rope goes up and down without going anywhere. Turn it faster and, with practice, you get two loops with a still point in the middle — the rope's second harmonic. The rope is not "vibrating at that frequency because you turn it at that frequency": it is vibrating at that frequency because that is one of the few frequencies at which a wave sent down the rope comes back *in step with itself*. Everything else cancels out. A stationary wave is [[Resonance]] with a shape.

### 中文锚点

两个人甩跳绳：绳子中间上下翻飞，握在手里的两端却几乎不动。这个波哪儿也没去，它就站在原地振动。原因是，沿着绳子跑过去的波在对面那只手那里被反射回来，去的波和回来的波叠加在一起，"跑"的部分互相抵消，上下振动的部分留了下来。现在把绳子甩得快一些。大多数速度下绳子只是乱抖；可是恰好甩到原来的两倍快时，绳子突然稳稳地分成两段，中间有一个不动的点；三倍快时分成三段。只有这些特殊的频率才行，因为两端被手固定住，整个波形必须正好装进这根绳子：整数个半波长，不多也不少。吉他弦就是这样选定音高的：弦长决定哪些波长装得下，其中最长的那个决定你听到的音高；手指把弦按在品上，弦变短了，只有更短的波装得下，音就高了。

### 术语对照 (Terms)

驻波 stationary (standing) wave · 反射 reflection · 叠加 superposition · 波节 node · 波腹 antinode · 半波长 half-wavelength · 基频 fundamental frequency · 谐波 harmonic · 闭管 closed pipe · 开管 open pipe

> [!info] Symbols in this card
> | Symbol | Meaning | 中文 |
> |---|---|---|
> | $A$ | amplitude of each progressive wave; the antinode swings $2A$ | 单个行波的振幅 |
> | $\lambda$, $f$, $v$ | wavelength, frequency, speed of the progressive waves | 波长、频率、波速 |
> | $L$ | length of the string or air column | 弦长、气柱长 |
> | $n$ | harmonic number; $f_n = n f_1$ | 谐波次数 |
> | $k$, $\omega$ | $2\pi/\lambda$, $2\pi f$ | 波数、角频率 |

## Part I — Superposition: the one rule

Two waves in the same medium do not bounce off each other. They pass *through* each other, and while they overlap the medium does both motions at once: **the displacement at any point is the sum of the displacements each wave would have produced alone.** That is the principle of superposition, and it holds for any waves of the same type — two sound waves, two ripples, two waves on one string. Nothing is required of their frequency, phase or amplitude for superposition *to happen*; those conditions matter only for what the sum *looks like*. The examiners have twice pointed out that candidates state the principle "in the specific context of a stationary wave" or confuse it with the conditions for interference: the principle is general, and it should be stated generally.

Why is it true? Because the restoring force on a particle of the medium is proportional to its displacement (that is what made every particle an SHM oscillator in [[Progressive Waves]]), and a proportional law adds: force from disturbance 1 plus force from disturbance 2 is the force of the sum. Superposition is linearity, and it fails exactly where the medium stops being linear — a wave on a beach, a shock in air — which is why it is stated as a principle and not a theorem.

## Part II — Two waves in, one pattern out

![[stationary-waves-formation.svg|1200]]

The syllabus asks for the formation *by a graphical method*, and the figure is that method: draw the wave travelling right at some instant, draw the identical wave travelling left, add them point by point, and repeat a fraction of a period later. Watch the grey dots. At $t = 0$ the two waves coincide and the sum is $2A$ high; at $T/4$ they are exactly out of step everywhere and the sum is flat; at $T/2$ the sum is $2A$ again but upside down. Through all of it the grey dots stay at zero — those are the **nodes** — and the pattern between them swings without sliding. **The sum never travels.**

The algebra says the same thing in one line, from the addition formula $\sin P + \sin Q = 2\sin\frac{P+Q}{2}\cos\frac{P-Q}{2}$:

$$A\sin(kx - \omega t) + A\sin(kx + \omega t) = 2A\,\sin(kx)\,\cos(\omega t).$$

The two factors are the whole physics. $\cos\omega t$ says every point oscillates in time at the original frequency; $2A\sin kx$ says how *much* each point oscillates, and it is fixed by position: zero where $\sin kx = 0$, i.e. every $\lambda/2$ (nodes), and $2A$ halfway between (antinodes). The product has no $(x - vt)$ in it, so no profile moves. `stationary-waves-sim.py` adds the two travelling waves numerically and compares with the product over a full period: the largest difference is $4 \times 10^{-15}$, the arithmetic's own rounding.

![[stationary-waves-manim.mp4]]

Where does the second wave come from in practice? From **reflection**. A wave reaching a fixed end — the wall, the bridge of a guitar, the closed end of a pipe — cannot move that point, so it comes back **inverted**, travelling the other way with the same frequency and wavelength. The simulation clamps the far bead of a driven string to zero and programs nothing else: Newton's law on the beads produces the reflected wave, the two superpose, and nodes appear every $0.499$ m on a string carrying a $1.00$ m wavelength. The examiners' word for what happens at the wall is *reflect*; "bounce", "rebound" and "deflect" lose the mark, and so does any explanation that names the reflection without saying that the incident and reflected waves *superpose*, or the superposition without saying the waves travel in *opposite directions*.

## Part III — Reading the pattern

| | Progressive wave | Stationary wave |
|---|---|---|
| does the profile move? | yes, at $v$ | no |
| energy | transferred along the wave | stored; none transferred |
| amplitude | the same at every point | varies with position: $0$ at nodes, $2A$ at antinodes |
| phase of neighbouring points | changes steadily, $360^\circ \times \Delta x/\lambda$ | all points within a loop in phase; adjacent loops in antiphase |
| what $\lambda$ means | crest-to-crest distance | twice the node-to-node distance |

Three of these rows are marks on real papers.

- **Node to node is $\lambda/2$; node to the next antinode is $\lambda/4$.** The June 2023 examiners' report names "node to adjacent antinode $= \lambda/2$" as *the* common misconception on the microphone-in-a-tube question. Count the loops: each loop is half a wavelength.
- **Phase on a stationary wave does not grow with distance.** Two points in the same loop are in phase however far apart; two points in adjacent loops are $180^\circ$ apart however close. The June 2024 candidates who answered $135^\circ$ for two points $0.30$ m apart on a $0.80$ m wavelength were reading the diagram as a progressive wave. On the stationary wave the answer was $180^\circ$: the points were in neighbouring loops. `stationary-waves-sim.py` measures it — the correlation between two beads in one loop is $+0.99$, across a node $-1.00$.
- **The pattern a moment later.** Because every point moves as $\cos\omega t$, the whole string passes through zero at once (a straight line, at $T/4$ after maximum displacement) and reaches the mirror-image shape at $T/2$. The June 2024 sketch — "at $t = 0.24$ s, period $0.16$ s" — is $1.5$ periods on, so the string is the original reflected in the axis, same wavelength, same amplitude, crossing zero at the same nodes. The June 2022 sketch — "a quarter of a cycle after the string is straight, with P moving downwards" — is a sinusoid with maximum *downward* displacement at P and zero at every node.

## Part IV — Strings: why only some frequencies

![[stationary-waves-string.svg|900]]

A string fixed at both ends must have a node at each end. Between two nodes there is a whole number of loops, each $\lambda/2$ long, so the only wavelengths that fit are

$$L = n\frac{\lambda_n}{2} \quad\Longrightarrow\quad \lambda_n = \frac{2L}{n}, \qquad f_n = \frac{v}{\lambda_n} = n\,\frac{v}{2L} = n f_1, \qquad n = 1, 2, 3, \dots$$

These are the string's **harmonics**: the **first harmonic** (the fundamental) with one loop, the second with two, and so on, all integer multiples of $f_1$. The speed $v = \sqrt{T_{\text{s}}/\mu}$ is the medium's, from [[Progressive Waves]], so a guitarist has three controls: shorten $L$ with a finger (higher pitch), tighten the string (higher $v$, higher pitch), or use a heavier string (lower $v$, lower pitch). A finger at $L/3$ from the bridge sounds a string whose first harmonic is three times the open string's — the IB question below.

Drive the string at any *other* frequency and the reflected waves come back out of step with the new ones; the superposition averages to nearly nothing. This is why a stationary wave is a resonance: the string is a [[Resonance|driven oscillator]] with many natural frequencies, one per harmonic, and it responds only near them. The simulation sweeps a $1$ m string from $6$ to $44$ Hz: the antinode amplitude is about $2\times$ the driver's off-resonance and $35\times$ at $10$, $20$, $30$ and $40$ Hz exactly, with $1$, $2$, $3$ and $4$ loops respectively — $f_n = nv/2L$ read straight off the response.

**Melde's experiment** is the school version: a vibration generator at one end, the string over a pulley with a hanging mass setting the tension, and the frequency tuned until loops appear. It demonstrates every relation above — more loops at higher frequency, fewer at higher tension — and it is the "stretched strings" experiment the syllabus names.

## Part V — Air columns: pipes, and the odd harmonics

![[stationary-waves-pipes.svg|1200]]

Sound in a pipe is a longitudinal stationary wave, and the figure draws it the way the exam does: as an envelope of **displacement** amplitude, even though the air moves along the pipe rather than across it. The boundary conditions are the whole story:

- A **closed end** cannot move: displacement **node**.
- An **open end** is free to move: displacement **antinode** (the air there swings in and out against the open room).

A pipe **open at both ends** has an antinode at each end — the same spacing rule as the string, $L = n\lambda/2$, all harmonics $f_n = nv/2L$. A pipe **closed at one end** has a node at the closed end and an antinode at the open end, a quarter wavelength minimum: $L = \lambda/4, 3\lambda/4, 5\lambda/4, \dots$, so

$$L = (2m - 1)\frac{\lambda}{4}, \qquad f = (2m-1)\,\frac{v}{4L}: \quad \text{only the odd harmonics.}$$

The **longest wavelength** a closed pipe can hold is $4L$ — the June 2023 question's last part, which the report says most candidates guessed at. The syllabus says end corrections are to be ignored: the antinode is taken to sit exactly at the open end.

**The resonance tube** is the air-column experiment: a tuning fork of known frequency held over a tube whose air-column length is set by a water level. Lower the water and the tube sings first at $L_1 = \lambda/4$ and again at $L_2 = 3\lambda/4$; then $\lambda = 2(L_2 - L_1)$, which cancels the end correction without anyone having to know it, and $v = f\lambda$ gives the speed of sound to a few per cent with a metre rule and a fork.

## Part VI — Microwaves: the same pattern you cannot see

![[stationary-waves-experiments.svg|1200]]

A microwave transmitter facing a metal plate makes a stationary wave in the air between them: the reflected wave superposes with the incident one, and a probe moved along the line reads a signal that rises and falls, with minima (nodes) every $\lambda/2$. For a school $10.7$ GHz set the minima are about $1.4$ cm apart, giving $\lambda \approx 2.8$ cm and, with $v = f\lambda$, the speed of light. The MCQ trap the March 2021 report describes: the plate itself is a node, so four detected nodes plus the plate span $4 \times \lambda/2$, not $3$. A microwave oven with the turntable removed does the same experiment in chocolate — the melted spots are antinodes, $\lambda/2$ apart, about $6$ cm for $2.45$ GHz, and multiplying by the frequency on the oven's label gives $c$ to within a few per cent.

## Worked examples — every tool named

### Example 1 — the string between generator and wall (Cambridge 9702, June 2024 Paper 21, Q5)

> A string $1.2$ m long runs from a vibration generator at P to a wall at Q; a stationary wave with three loops is shown. (a) Explain how it forms [2]. (b) Find the wavelength [1]. (c) At $t = 0$ every point is at maximum displacement; the period is $0.16$ s; sketch the string at $t = 0.24$ s [2]. (d) R and T are $0.30$ m apart in adjacent loops; state their phase difference [1]. (e) Find the speed of the progressive waves [2].

*Tools: the formation sentence; loops $= \lambda/2$; the $\cos\omega t$ time dependence; the phase rule; $v = f\lambda = \lambda/T$.* **(a)** Waves from the generator travel along the string and **reflect at the wall** (Q); the incident and reflected waves **superpose**. Both halves are needed, and the report says answers that described stationary waves "in general" scored nothing. **(b)** Three loops in $1.2$ m: each is $0.40$ m $= \lambda/2$, so $\lambda = 0.80$ m. **(c)** $0.24/0.16 = 1.5$ periods: the string is the given shape **reflected in the axis** — same wavelength, same amplitude, passing through zero at the same nodes. **(d)** Adjacent loops: $180^\circ$. **(e)** $v = \lambda/T = 0.80/0.16 = 5.0\ \text{m s}^{-1}$. The report's common error was mixing distances with times in speed $=$ distance/time.

### Example 2 — the string at two later instants (Cambridge 9702, November 2022 Paper 22, Q5)

> (a) Two progressive sound waves of the same amplitude, wavelength, frequency and speed meet to form a stationary wave; state the other condition they must satisfy [1]. (b) A string is stretched between fixed points A and B, $0.80$ m apart; the figure shows it at $t = 0$, every point at maximum displacement, with **four loops** between A and B. The period is $0.016$ s. (i) Sketch the string at $t = 0.004$ s (label it P) and at $t = 0.024$ s (label it Q) [2]. (ii) Determine the speed of a progressive wave along the string [3].

*Tools: the opposite-directions condition; the $\cos\omega t$ clock; loops $= \lambda/2$; $v = \lambda/T$.* **(a)** They travel in **opposite directions**. **(b)(i)** $0.004$ s is $T/4$: every point is passing through zero, so P is the **straight line** from A to B. $0.024$ s is $1.5T$: Q is the **mirror image** of the given shape in the axis. **(ii)** Four loops in $0.80$ m make each loop $0.20$ m, so $\lambda = 0.40$ m — the scheme writes it as $0.80/2$, two whole wavelengths across AB. Then $v = \lambda/T = 0.40/0.016 = 25\ \text{m s}^{-1}$. The whole question turns on counting the loops on the printed figure: a shape half-remembered from a similar question, with a different loop count, gives a different wavelength and loses all three marks.

### Example 3 — the closed tube (Cambridge 9702, June 2023 Paper 22, Q5(b))

> A tube closed at one end, loudspeaker at the open end emitting $1.7$ kHz, speed of sound $340\ \text{m s}^{-1}$. A stationary wave has an antinode at the open end and one other antinode inside. Determine (i) the wavelength, (ii) the length $L$, (iii) the maximum wavelength that can produce a stationary wave in the tube.

*Tools: $\lambda = v/f$; the closed-pipe pattern node–antinode–node–antinode $= 3\lambda/4$; the longest mode $L = \lambda/4$.* **(i)** $\lambda = 340/1700 = 0.20$ m. **(ii)** Closed end (node) to the first antinode is $\lambda/4$, to the second $3\lambda/4$: $L = 0.15$ m. **(iii)** The longest wavelength has a node at the closed end and the first antinode at the open end: $L = \lambda/4$, so $\lambda_{\max} = 4L = 0.60$ m. The report: many candidates could not turn the pattern into a fraction of $\lambda$, and (iii) was widely guessed.

### Example 4 — the piston (Cambridge 9702, November 2024 Paper 22, Q4(b))

> A pipe open at one end is closed by a piston $4.5 \times 10^{-2}$ m from the open end; a loudspeaker at the open end sets up the simplest stationary wave. (i) Mark an antinode [1]. (ii) Find the frequency, with $v = 340\ \text{m s}^{-1}$ [3]. (iii) The piston is moved left and the frequency changed to keep the same number of antinodes: state and explain the change [2].

**(i)** At the open end. **(ii)** $L = \lambda/4 \Rightarrow \lambda = 0.18$ m; $f = 340/0.18 = 1900$ Hz. **(iii)** The node–antinode distance, hence the wavelength, is longer; the speed of sound is unchanged, so by $v = f\lambda$ the frequency is **lower**. State the change *and* the reason — the second mark is the reasoning.

### Example 5 — the straight string and the distance travelled (Cambridge 9702, June 2022 Paper 21, Q5)

> A stationary wave on a string between A and B; at one instant the string is straight with the nodes marked and point P moving downwards; $v = 35\ \text{m s}^{-1}$, $T = 0.040$ s. (c) Find the distance AB, given the figure shows five nodes including the ends [3]. (d) A particle with zero displacement at $t = 0$ travels a total distance of $72$ mm by $t = 0.060$ s; find its amplitude [2].

**(c)** $\lambda = vT = 35 \times 0.040 = 1.4$ m; the figure shows $2.5$ wavelengths (five loops), so AB $= 3.5$ m. Weaker candidates, the report says, set the string length equal to $vT$ — one wavelength — without counting. **(d)** $0.060/0.040 = 1.5$ cycles; a particle covers $4A$ per cycle, so $6A = 72$ mm and $A = 12$ mm. A pure [[Simple Harmonic Motion]] fact wearing a wave's clothes.

### Example 6 — the best question from another board: the guitar (IB Physics HL, May 2021 TZ1 Paper 2, Q8)

> A guitar string vibrates between the bridge and a finger; sounding length $62$ cm, first harmonic $195$ Hz, point P displaced $0.4$ cm. (a) Outline how the standing wave is produced [2]. (b)(i) Show the wave speed is about $240\ \text{m s}^{-1}$ [2]. (iii) Find P's maximum velocity [2]. (c) Where must the finger go for the third harmonic's frequency as the *first* harmonic of the shortened string?

**(a)** A travelling wave moves along the string and reflects at the fixed ends; the incident and reflected waves superpose, reinforcing only for wavelengths that fit. **(b)(i)** First harmonic: $\lambda = 2L = 1.24$ m; $v = f\lambda = 195 \times 1.24 = 242\ \text{m s}^{-1}$. **(iii)** P is in SHM at $195$ Hz with amplitude $0.4$ cm: $v_{\max} = \omega A = 2\pi \times 195 \times 0.004 = 4.9\ \text{m s}^{-1}$. **(c)** The same $v$ with $f$ tripled needs $L/3 = 21$ cm — the fret a third of the way along. IB pushes the wave question into SHM deliberately; the [[Simple Harmonic Motion]] tools travel with this card.

### Example 7 — the next harmonic (Cambridge 9702, June 2023 Paper 1, Q26)

> A string at frequency $f$ shows four loops. The frequency is increased until the next stationary wave appears. What is the new frequency?

*Tool: $v$ fixed by the medium; $L = n\lambda/2$.* Four loops: $\lambda = 2L/4 = L/2$, so $v = fL/2$. Five loops: $\lambda' = 2L/5$, $f' = v/\lambda' = (fL/2)/(2L/5) = 1.25f$. The report's key point: the speed of the waves on the string, "travelling to and fro and superposing", is constant.

## Hands-on

- **`stationary-waves-sim.py`** — superposition checked to $10^{-15}$; a driven string with a clamped end whose reflection is never programmed, node spacing measured at $\lambda/2$, in-phase and antiphase beads by correlation; the harmonic sweep with its four peaks and their loop counts. Change `L`, `T_S` or `MU` and watch $f_n = nv/2L$ follow.
- **`stationary-waves-figures.py`** — the graphical method at five instants, the string and pipe harmonics, the three syllabus experiments.
- **`stationary-waves-manim.py`** — two waves becoming one, then the string's modes with tracked beads.
- **A phone and a mug.** Play a tone generator into a mug and sweep the frequency; it hums at its air column's first harmonic near $v/4L$. Then a bottle, then a saucepan. Every one is Part V.

## Where it is the working tool

- **The luthier's rule of eighteen.** Every fret on a guitar is placed by $f_1 = v/2L$: shortening the vibrating length raises the first harmonic in proportion, and a semitone is a frequency ratio of $2^{1/12}$, so each fret sits $1/17.817$ of the *remaining* distance to the bridge from the last one. The twelfth fret lands at exactly $L/2$ — one octave — which is why it is the fret with the double dot. Guitar makers used "divide by eighteen" for centuries before anyone wrote $2^{1/12}$; the pipe organ, the flute's tone holes and the piano's string lengths are the same equation in other wood.
- **The cold spot in the microwave.** A microwave oven runs at $2.45\ \text{GHz}$, so $\lambda = 12.2\ \text{cm}$, and the metal walls set up Part VI's pattern in three dimensions: antinodes where the food cooks, nodes $6.1\ \text{cm}$ away where it stays cold. The turntable exists to drag the food through both. Take it out, lay a bar of chocolate on a plate, run ten seconds, and the melted patches are a ruler for $\lambda/2$ — multiply by the frequency printed on the back of the oven and you have measured the speed of light in a kitchen.
- **Inside a laser.** A laser is a stationary wave of light between two mirrors: only wavelengths with $L = n\lambda/2$ survive the round trip, and everything else cancels itself. With $L = 30\ \text{cm}$ the allowed frequencies are $c/2L = 500\ \text{MHz}$ apart — the "longitudinal modes" on a laser's datasheet are Part IV's harmonics with $n$ in the hundreds of thousands. Tuning a laser is choosing which loop of the string to keep.
- **Modes of a structure.** A bridge deck, an aircraft wing and a turbine blade have modes exactly as a string does, each with its own frequency, and the engineer's job is to keep every driving frequency the structure will meet away from every mode it has — the same $f_n$ ladder, measured with accelerometers instead of a signal generator. The 1940 film of the Tacoma Narrows deck twisting in a single torsional loop is what one antinode looks like at a hundred metres; the *mode* was a stationary wave, though what drove it was aeroelastic flutter rather than resonance, a distinction [[Resonance]] insists on.
- **The electron, briefly.** The reason atoms have discrete energy levels is Part IV with the string replaced by an electron wave: only whole numbers of loops fit, so only certain energies exist. The Beyond section below works the particle in a box; it is the same $L = n\lambda/2$.

---

## Common Misconceptions (Teaching Notes)

### 1. "Node to antinode is half a wavelength"
It is a quarter. Node to node, or antinode to antinode, is half. The examiners named this as the standing misconception on the microphone-in-a-tube question.

### 2. "A stationary wave carries energy along the string, just slowly"
It carries none along the string. Energy is stored in each loop and swaps between kinetic and potential; the two progressive waves carry equal energy in opposite directions and the net flow is zero.

### 3. "Phase difference is $360^\circ \times \Delta x/\lambda$, like any wave"
That is the progressive-wave rule. On a stationary wave the phase is the same throughout a loop and flips by $180^\circ$ across each node; distance within a loop is irrelevant. The $135^\circ$ answers on June 2024 came from applying the wrong rule.

### 4. "The wave bounces off the wall"
It *reflects*, inverted, at a fixed end — and the mark is for saying that the reflected wave then *superposes* with the incident wave travelling the opposite way. Reflection alone, or superposition alone, is one mark of two.

### 5. "Every point has the same amplitude"
The amplitude is a function of position, $2A\lvert\sin kx\rvert$: zero at nodes, $2A$ at antinodes. Sketches drawn with a uniform amplitude, or not passing through zero at the nodes, are the errors the June 2024 report describes.

### 6. "For a stationary wave the two waves must be coherent"
Coherence is a two-*source* condition from [[Superposition and Interference]]. Here there is one source and its reflection; the report says mentioning coherence or "constant phase difference" is not the answer and can cost the explanation mark.

## Exam Notes

### Cambridge 9702 (§8.1 Stationary waves — Paper 1 and Paper 2)

- **Four learning outcomes:** explain and use the **principle of superposition**; understand the experiments that demonstrate stationary waves using **microwaves, stretched strings and air columns** (end corrections assumed negligible and not required); explain the formation of a stationary wave **using a graphical method** and identify nodes and antinodes; determine **wavelength from the positions of nodes or antinodes**.
- **Paper 2's standing shapes**, all above: *explain how the stationary wave is formed* in the given apparatus — reflection at the named end, then incident and reflected waves superposing, travelling in opposite directions (June 2022, June 2024, and the November 2022 "other condition"); *wavelength from a figure* by counting loops; *sketch the string a stated time later* (a fraction of the period: straight at $T/4$, inverted at $T/2$ and $1.5T$); *phase difference between two labelled points* ($0^\circ$ or $180^\circ$, never anything else); *the closed tube* — $L = \lambda/4$ for the simplest mode, $3\lambda/4$ with one more antinode, longest $\lambda = 4L$; *the piston* — move it, keep the pattern, explain the frequency change through $v = f\lambda$; *speed of the progressive waves* from $\lambda/T$.
- **Paper 1** likes the next-harmonic ratio (loops $n \to n+1$ gives $f' = f(n+1)/n$), the microwave node count with the reflector itself a node, and node/antinode spacing.
- **Examiners' recurring notes:** general descriptions not tied to the apparatus; "bounce" for reflect; coherence mentioned; node–antinode taken as $\lambda/2$; string length equated to $vT$ without counting loops; sketches with wrong amplitudes or missing the nodes; the closed pipe's longest wavelength guessed.
- §8.2 diffraction and §8.3 interference (two-source, Young's slits) complete Topic 8 and are examined alongside this.

### IB Physics (C.4.1 — SL and HL)

- **C.4.1**: the nature and formation of standing waves from the superposition of two identical waves travelling in opposite directions; nodes and antinodes; the relative amplitude and phase difference of points along a standing wave; patterns in strings and pipes. The guide's vocabulary is fixed: **first harmonic**, never "fundamental" or "overtone"; boundary conditions named as two fixed / one fixed and one free / two free for strings and two closed / one closed and one open / two open for pipes; displacement nodes and antinodes only, pressure nodes not required; end corrections not required; no superposition of more than two waves.
- IB questions cross into SHM on purpose — P's maximum velocity and acceleration, energy $\propto A^2$ — so bring the [[Simple Harmonic Motion]] tools. C.4.2–C.4.3 (resonance and damping) are [[Resonance]] and [[Damped Oscillations]].

### AP Physics 2 (Unit 14.6 — the standing-wave half)

- **14.6.B**: standing waves from interference of two waves confined to a region and travelling in opposite directions; a node has amplitude always zero, an antinode always maximum; the possible wavelengths are set by the size and boundary conditions of the region — pipes with open or closed ends, strings with fixed or loose ends; the longest wavelength is the fundamental or first harmonic, and a region with a node at one end and an antinode at the other supports **only odd harmonics**; visual representations to relate length, wavelength, frequency, speed and harmonic. AP keeps "fundamental" as a name; IB forbids it. The interference half of 14.6 (14.6.A, constructive and destructive, beats) is [[Superposition and Interference]].

### Where it is *not* examined

**Cambridge 0625** has no stationary waves — its sound section (§3.4) stops at pitch, loudness, echoes and ultrasound. **AP Physics 1** has no waves since the 2024 redesign. **AP Physics C** examines no waves.

## Connections

- **Built on:** [[Progressive Waves]] — the two waves that make one, $v = f\lambda$, and $v = \sqrt{T_{\text{s}}/\mu}$ as the medium's contribution to $f_n = nv/2L$; [[Resonance]] — a stationary wave is a resonance with a shape, and the harmonic sweep is a resonance curve with several peaks; [[Simple Harmonic Motion]] — every point's $\cos\omega t$, and the $v_{\max} = \omega A$ questions.
- **Same idea elsewhere:** [[Trigonometric Identities]] — the sum-to-product formula that turns two travelling waves into $2A\sin kx\cos\omega t$; [[Fourier Series]] — any shape a string can take is a sum of its harmonics, which is why a plucked string sounds all of them at once.
- **Extends into:** [[Superposition and Interference]] — the same principle with two *sources*; [[Diffraction]] — a wave spreading past an edge, Topic 8's other half; [[Sound Waves]] — the pipes and strings as instruments; [[Electromagnetic Spectrum]] — the microwave experiment's wave.

## Beyond Syllabus

### Pressure and displacement are a quarter wavelength apart
In an air column the air is squashed hardest where it moves least: a displacement node is a **pressure antinode**, and the open end — a displacement antinode — is a pressure node, at atmospheric. A microphone measures pressure, so a microphone moved along a tube reads *loudest* at the displacement nodes. The exam draws displacement and says so; know which you are holding.

### The end correction
The antinode at an open end actually sits about $0.6r$ *outside* the pipe, $r$ its radius, because the air beyond the mouth is dragged along too. The resonance-tube method's $\lambda = 2(L_2 - L_1)$ cancels it, which is why it is the method; for a single length the correction adds to $L$. The syllabus says ignore it; a flute-maker cannot.

### Two dimensions: Chladni figures
Sprinkle sand on a metal plate and bow its edge: the sand jumps off the antinodes and collects on the **nodal lines**, drawing the plate's mode shape — Chladni's demonstration of 1787, which Napoleon paid to see. A drumhead's modes are the same thing on a circle, and they are not harmonics — their frequencies are not integer multiples, which is why a drum has a pitch you cannot quite name and a string has one you can.

Germain took up the prize competition to explain those plate patterns. [[Sophie Germain and the Borrowed Name]] follows the person doing the research. A plate bends, whereas tension supplies the restoring force in a stretched drum membrane; their similar-looking nodal patterns do not imply identical equations.

### The electron is a stationary wave
De Broglie's $\lambda = h/p$ turns an electron confined to a box of length $L$ into exactly Part IV: only $L = n\lambda/2$ fits, so only $p_n = nh/2L$ and only $E_n = n^2h^2/8mL^2$ are allowed. Quantised energy levels are the harmonics of a wave that cannot leave its box. Bohr's orbits are the circular version — a whole number of wavelengths round the ring — and the hydrogen atom is a three-dimensional resonance tube. The quantum harmonic oscillator in [[Simple Harmonic Motion]] is the same story with a spring for a box.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $y = 2A\sin(kx)\cos(\omega t)$ | `y = 2A\sin(kx)\cos(\omega t)` | the standing wave |
| $\sin P + \sin Q = 2\sin\frac{P+Q}{2}\cos\frac{P-Q}{2}$ | `\sin P + \sin Q = 2\sin\frac{P+Q}{2}\cos\frac{P-Q}{2}` | sum to product |
| $f_n = \dfrac{nv}{2L}$ | `f_n = \dfrac{nv}{2L}` | string fixed both ends; open–open pipe |
| $f = (2m-1)\dfrac{v}{4L}$ | `f = (2m-1)\dfrac{v}{4L}` | closed–open pipe, odd harmonics |
| $\lambda = 2(L_2 - L_1)$ | `\lambda = 2(L_2 - L_1)` | resonance tube |
| $E_n = \dfrac{n^2 h^2}{8mL^2}$ | `E_n = \dfrac{n^2 h^2}{8mL^2}` | particle in a box |
