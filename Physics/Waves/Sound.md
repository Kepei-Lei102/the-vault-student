---
chinese: 声音 (shēngyīn)
prerequisites:
  - "[[Progressive Waves]]"
  - "[[Simple Harmonic Motion]]"
  - "[[Density and Pressure]]"
  - "[[Planning an Experiment]]"
leads_to:
  - "[[Ultrasound]]"
  - "[[Doppler Effect]]"
  - "[[Stationary Waves]]"
tags:
  - subject/physics
  - domain/waves
  - domain/acoustics
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-2
  - syllabus/0625-3-4
  - type/deep
  - misconception/sound-travels-in-vacuum
  - misconception/louder-means-higher
  - misconception/particles-travel-with-the-wave
  - misconception/denser-means-slower
---

# Sound 声音

> *In November 1826 two young men sat in rowing boats at opposite ends of Lake Geneva, thirteen and a half kilometres apart. In one boat Jean-Daniel Colladon had hung a church bell under the water, rigged so that the lever which struck it also touched a match to a pan of gunpowder on deck. In the other, Charles Sturm pressed his ear to a long tin trumpet dipped into the lake and watched the dark horizon. A flash; he started his watch. A little over nine seconds later the bell arrived through the water. Sound in water, they announced, travels at 1435 metres per second, more than four times faster than in the air above it. They had measured a speed with a bell, a match and a watch, and the answer holds up today.*

## Definition

### Formal

**Sound** is a **longitudinal mechanical wave**: a vibrating source pushes on the medium beside it, and the disturbance is handed on from particle to particle as alternating regions of raised pressure (**compressions**, where particles are closer together than normal) and lowered pressure (**rarefactions**, where they are further apart). The particles oscillate **parallel** to the direction of travel and do not travel with the wave. Sound **needs a medium**; it cannot cross a vacuum. In air its speed is approximately **330–350 m/s**; in general it is faster in liquids and faster still in solids. The human ear responds to frequencies from about **20 Hz to 20 000 Hz**. The **amplitude** of the wave sets the **loudness** heard; its **frequency** sets the **pitch**.

### Intuitive

Hit a drum and the skin jumps outward, shoving the layer of air against it. That layer, squeezed, shoves the next, and relaxes; the next shoves the one after. No air crosses the room. What crosses the room is the *shove*, the way a nudge travels down a queue of people without anyone leaving their place. Everything else about sound follows from that one picture. It needs something to shove, so there is silence in space. The hand-over takes time, so thunder trails lightning. The hand-over is quicker when neighbours are stiffly connected, so steel carries sound fifteen times faster than air. A bigger shove is a louder sound; shoves arriving more often are a higher note.

### 中文锚点

雷雨夜里，闪电一亮，你会下意识地数：一、二、三……轰。光几乎是立刻到的，雷声却要走上好几秒，因为声音不是"飞"过来的，而是靠空气一层推一层**传**过来的：闪电把身边的空气猛地撑开，这层空气挤了旁边一层，自己弹回原处；旁边一层再去挤下一层。空气并没有从云那边跑到你耳边，跑过来的只是那一下"挤"。一层推一层需要时间，在空气里大约每秒传三百四十米，所以每数三秒，雷就在一公里之外。也正因为它靠"推"，没有东西可推的地方就没有声音——太阳上惊天动地，我们一点也听不见。

---

## Part I — A vibration, and something to carry it

**Every sound starts with something vibrating.** A guitar string, a loudspeaker cone, the prongs of a tuning fork, your vocal cords, the column of air in a flute. Touch a ringing bell and you feel the vibration; stop the vibration and the sound stops. The frequency of the vibration *is* the frequency of the sound.

**The vibration needs a medium.** Put an electric bell inside a glass jar and pump the air out: the hammer still strikes and the sound fades to almost nothing, then returns as the air is let back in. (A faint sound remains, carried by the wires and the base, which makes the same point.) Light from the Sun crosses 150 million kilometres of near-vacuum; the Sun's sound does not, because there is nothing between to push.

**The wave is longitudinal.** Recall from [[Progressive Waves]] that a wave is longitudinal when the particles oscillate along the line the wave travels. In sound each air particle shuttles to and fro about a fixed position, typically by less than a hair's breadth, while the pattern of crowding moves on at 340 m/s.

![[sound-manim.mp4]]

*Two films. First, rows of air particles: the marked one goes nowhere, while the crowded band marked C crosses the screen and the pressure graph beneath keeps step. Then an oscilloscope trace made louder, then higher, one at a time.*

![[sound-compressions.svg|900]]

- A **compression** is a region where particles are closer together than normal, so the pressure is higher than atmospheric.
- A **rarefaction** is a region where particles are further apart than normal, so the pressure is lower.
- The **wavelength** is the distance from one compression to the next.

Because the easiest thing to measure is pressure, sound is usually drawn as a **pressure graph**, and the graph looks like a transverse wave. It is not a picture of particles going up and down: the vertical axis is pressure. Compressions are its peaks, rarefactions its troughs. And read the horizontal axis before using it: on a pressure–**distance** graph, peak to peak is a wavelength; on a pressure–**time** graph of one place, peak to peak is a **period**, and no wavelength can be read from it at all.

## Part II — How fast, and why

**In air: 330–350 m/s**, which is about a kilometre every three seconds, or a million times slower than light. The reason for a range is temperature: sound is carried by molecular collisions, and warmer molecules move faster. The ideal-gas result is $v = 331\sqrt{1 + \theta/273}$ with $\theta$ in °C, giving 331 m/s at 0 °C, 343 m/s at 20 °C and 352 m/s at 35 °C. Pressure does not appear: thin air at the same temperature carries sound at the same speed, and sound is slower on a mountain top only because it is colder there.

**Solids faster than liquids, liquids faster than gases.** Students expect the opposite, since denser things seem harder to move. The speed of any mechanical wave is set by a contest,

$$v = \sqrt{\frac{\text{stiffness}}{\text{density}}},$$

where stiffness measures how hard the medium pushes back when squeezed. Density slows the wave; stiffness speeds it; and stiffness wins by a landslide.

![[sound-speeds.svg|820]]

| Medium | Stiffness / Pa | Density / kg m⁻³ | Speed / m s⁻¹ |
|---|---|---|---|
| air at 20 °C | $1.4 \times 10^5$ | 1.2 | **343** |
| water | $2.2 \times 10^9$ | 998 | **1485** |
| steel | $2.0 \times 10^{11}$ | 7850 | **5050** |

Steel is 6 500 times denser than air and 1.4 million times stiffer. In a solid the particles are bonded to their neighbours, so a push is handed on almost at once; in a gas a particle must fly across a gap and collide before the neighbour hears about it. This is why you hear a train in the rails before you hear it in the air, and why Colladon's bell reached Sturm in nine seconds when a shout, had it survived the distance, would have taken forty.

**Echoes.** Sound reflects from hard surfaces, and a reflected sound heard separately from the original is an **echo**. The sound has gone there and back, so a wall at distance $d$ returns the echo after $t = 2d/v$. The factor of two is the whole difficulty of every echo calculation. [[Ultrasound]] turns this into an instrument.

## Part III — Measuring the speed of sound

Every method measures a **distance** and a **time** and divides. What separates a good method from a bad one is the timing, because a hand on a stopwatch is wrong by about a tenth of a second at the start and again at the stop, whatever is being timed. The script beside this note runs each method twenty thousand times with that error built in.

![[sound-measure.svg|820]]

1. **See it, then hear it.** One person clashes two metal plates; another, a measured distance away, starts the watch at the sight and stops it at the sound. Over 60 m the true time is 0.175 s and the timing error is ±0.14 s: the result is uncertain by **80 %** and is mostly a measurement of the student's reactions. Over 500 m the time is 1.46 s and the uncertainty falls to **10 %**. *Make the distance large.*
2. **Clap in time with your own echo.** Stand 50 m from a large wall and clap, adjusting your rhythm until each clap lands exactly on the echo of the one before. The interval between claps is then the there-and-back time $2d/v$. Time twenty claps and divide: one pair of reaction errors is shared between twenty intervals, giving about **4 %**. This is the many-and-divide technique of [[Planning an Experiment]].
3. **Two microphones and an electronic timer.** Place two microphones a measured distance apart in line with a sharp sound (a hammer on a metal plate). The first microphone starts a timer, the second stops it. With microphones 1.00 m apart and a timer reading to 0.1 ms the uncertainty is **1 %**; at 3.00 m it is **0.3 %**. *Take the human out.*

A full description for any of them names the distance and how it is measured (tape measure, trundle wheel), the two events that start and stop the timing, the instrument, the calculation $v = d/t$ (or $2d/t$ for an echo), and one improvement: a larger distance, repeats and an average, and doing the experiment in both directions to cancel the wind.

## Part IV — Loudness and pitch

A microphone turns the pressure variation into a voltage and an oscilloscope draws it against time.

![[sound-traces.svg|860]]

- **Amplitude → loudness.** A larger amplitude is a larger pressure swing, more energy delivered to the ear each second, and a louder sound. The trace grows taller and the peaks stay the same distance apart.
- **Frequency → pitch.** A higher frequency is more vibrations each second and a higher note. The peaks crowd together and the height stays the same. Doubling the frequency raises the pitch by one octave: concert A is 440 Hz, the A above it 880 Hz.
- **The two are independent.** Any note can be played at any volume, and the speed of the sound changes with neither: a loud high note and a quiet low one leave the stage together and arrive together, or no orchestra would survive the back row.

To read a **frequency from a trace**, count the divisions for one complete cycle, multiply by the time-base setting to get the period $T$, and take $f = 1/T$.

**The audible range is 20 Hz to 20 000 Hz** for a young, healthy human ear. Below it is **infrasound**, above it **ultrasound**, and the limits are facts about the listener and not about the wave: the upper limit falls steadily with age, to perhaps 12 kHz by sixty.

![[sound-hearing-ranges.svg|820]]

Listen for yourself. `sound-a440-quiet.wav` and `sound-a440-loud.wav` have the same frequency and amplitudes in the ratio 1 to 7. `sound-a880-octave.wav` doubles the frequency. `sound-a440-reedy.wav` is the same pitch and loudness with a different *shape* of wave, which is the third quality of a sound, its **timbre**. And `sound-15khz.wav` is a pure 15 kHz tone: most students hear it and many teachers cannot.

![[sound-a440-quiet.wav]] ![[sound-a440-loud.wav]] ![[sound-a880-octave.wav]] ![[sound-a440-reedy.wav]] ![[sound-15khz.wav]]

## Where it is the working tool

- **Counting the storm.** Three seconds a kilometre, from $1000/343 = 2.9$ s. If the gap between flash and thunder is shrinking, the storm is coming towards you. The light's own journey took three microseconds, which is why the flash counts as "now".
- **The mixing desk.** Doubling a signal's amplitude on a fader is $+6$ dB and four times the intensity, because intensity goes as amplitude squared ([[Progressive Waves]]). The two A-440 files differ by a factor of 7 in amplitude, 50 in intensity, **17 dB**, and the ear reports that as "much louder" and nowhere near fifty times louder: hearing is roughly logarithmic, which is why the decibel scale exists.
- **Noise-cancelling headphones.** A microphone on the outside of the cup samples the incoming pressure wave; the electronics play its mirror image, compressions where the noise has rarefactions, and the two superpose to near-silence ([[Superposition and Interference]]). It works best on steady low-frequency drone, because the electronics must produce the anti-wave before the wave arrives, and a long wavelength is forgiving about position.
- **Listening to the Earth and the rails.** A railway worker's ear on the rail, a doctor's stethoscope, a geologist's seismometer: all use the faster, less attenuated path through a solid. Earthquake **P-waves are sound waves in rock**, travelling at 6 km/s, and the delay before the slower S-waves arrive locates the quake exactly as the flash-to-thunder delay locates the storm.
- **The mosquito alarm.** A 17 kHz tone played outside a shop is inaudible to most people over twenty-five and unpleasant to teenagers. Teenagers returned the favour with ringtones their teachers could not hear.

## Hands-on

Run `sound-lab.py`. It prints the speed of sound against temperature, the three media from their stiffness and density, the simulated uncertainty of each measuring method, the thunder rule, and then writes the five WAV files above. Change `reaction` to see how much a better timekeeper helps the stopwatch methods (not much: the distance matters more), or change the harmonics in `sound-a440-reedy.wav` and hear timbre change while pitch and loudness do not.

Then measure it. **With one phone:** stand 50 m from a large building and do the clap-echo method, timing twenty claps. **With two phones** and a recording app: lay them a measured 3 m apart, clap once beyond one end on the line joining them, and compare the arrival times of the spike in the two recordings (synchronise the recordings with a first clap made exactly midway). A free oscilloscope or spectrum-analyser app will also show you the traces of Part IV for your own voice, and whistle a rising note to watch the peaks crowd together.

## Worked examples — every tool named

### Example 1 — compressions, the silent Sun, and a storm (Cambridge 0625, March 2023 Paper 42, Q6(a)–(c))

*(a) Sound waves have compressions and rarefactions. Explain what is meant by each. [2] (b) We can see light from the Sun but cannot hear any sound from it. State the reason. [1] (c) Thunder is heard 9.0 s after the lightning is seen. The speed of sound in air is 340 m/s. Calculate the distance to the storm. [2]*

**(a)** *Tool: the definitions, each with its comparison.* A compression is a region where the particles are **closer together than normal** (or the pressure is higher than normal); a rarefaction is a region where they are **further apart than normal** (or the pressure is lower). The words "than normal" carry the mark: "particles close together" describes all of a solid.
**(b)** *Tool: sound needs a medium.* There is no medium between the Sun and the Earth; light needs none.
**(c)** *Trigger: one-way journey, light's time negligible. Tool: $s = vt$.* $s = 340 \times 9.0 = 3060 \approx 3100$ m.

### Example 2 — reading a pressure graph (Cambridge 0625, June 2024 Paper 42, Q6)

*(a) A pressure–time graph for the air at one place as a sound passes. (i) Label a compression C and a rarefaction R. [2] (ii) Explain why this graph cannot be used to find the wavelength. [1] (iii) The sound becomes louder and of lower pitch. State what happens to the amplitude and to the frequency. [1] (b) A sound of frequency 13 kHz travels through water at 1500 m/s. Calculate its wavelength. [3] (c) State the approximate speed of sound in air. [1]*

**(a)(i)** *Tool: compression = pressure peak.* C at a peak of the curve, R at a trough. **(ii)** *Trigger: read the axis.* The horizontal axis is time, so the graph shows the period; it does not show how anything varies with **distance** along the wave (the scheme's wording: the graph "does not show variation with displacement"). **(iii)** Amplitude increases **and** frequency decreases; both for the one mark.
**(b)** *Tool: $v = f\lambda$, with the kilo converted.* $\lambda = v/f = 1500/13\,000 = 0.12$ m.
**(c)** Any value from 330 to 350 m/s.

### Example 3 — a dolphin (Cambridge 0625, November 2025 Paper 41, Q5)

*A dolphin emits sounds in the range 7–15 kHz. (a) State the speed of sound in air and how the speed in water differs. [1] (b) State and explain whether humans with normal hearing can hear all of the dolphin's sounds. [2] (c) Complete a table for two sounds: 14 kHz with large amplitude, 8 kHz with small amplitude. [2]*

**(a)** 330–350 m/s, and sound is **faster** in water; both for the mark.
**(b)** *Tool: compare the range with 20 Hz – 20 kHz, in the same unit.* Yes: human hearing runs from 20 Hz to 20 kHz and 7–15 kHz lies wholly inside it. "Yes" with no range quoted earns one of the two marks.
**(c)** *Tool: amplitude → loudness, frequency → pitch, independently.* 14 kHz, large amplitude: **loud, high**. 8 kHz, small amplitude: **quiet, low**. One mark per correct column.

### Example 4 — why the students got the wrong answer (Cambridge 0625, March 2025 Paper 32, Q8(c))

*A girl 60 m from a boy starts a stopwatch when she sees him clash two metal plates and stops it when she hears the sound. Their value for the speed of sound differs from the true value. Explain why.* [1]

*Trigger: a hand stopwatch and a time much shorter than a second.* The time to be measured is $60/340 = 0.18$ s, which is about the size of a human **reaction time**, so the reaction-time error is a large fraction of the reading; equivalently, the **distance is too small**. Either earns the mark. Part III puts a number on it: ±0.14 s on 0.175 s, an 80 % uncertainty. The improvement is a much larger distance, or electronic timing.

### Example 5 — a whistle, and the range of hearing (Cambridge 0625, November 2023 Paper 32, Q7(b)(ii),(c))

*The time between steam leaving a whistle and a student hearing it is 1.6 s. The speed of sound in air is 340 m/s. Calculate the distance. State the range of audible frequencies for a healthy human ear, with the unit.*

*Tool: $d = vt$, one way.* $d = 340 \times 1.6 = 544 \approx 540$ m. The range is **20 Hz to 20 000 Hz** (or 20 kHz); the unit is part of the mark, and "20 to 20 000" without it is not an answer.

### Example 6 — the best question from another board: a frequency from a trace, a wavelength from nodes, and the speed from both (Cambridge 9702, June 2023 Paper 23, Q4(b),(d))

*A loudspeaker's sound is picked up by a microphone and shown on an oscilloscope with time-base 0.50 ms cm⁻¹; one cycle occupies 4.0 cm. (b)(i) Calculate the frequency. A metal sheet is then placed to reflect the sound, forming a stationary wave. Moving the microphone 1.05 m takes it from one amplitude minimum, through three maxima, to another minimum. (d)(ii) Determine the wavelength. (iii) Determine the speed of sound.*

*Tool: period from the time-base, then $f = 1/T$.* $T = 4.0 \times 0.50 = 2.0$ ms, so $f = 1/(2.0 \times 10^{-3}) = 500$ Hz.
*Trigger: minimum to minimum through three maxima is three node-to-node gaps. Tool: nodes are $\lambda/2$ apart, from [[Stationary Waves]].* $3 \times \lambda/2 = 1.05$ m, so $\lambda = 0.70$ m.
*Tool: $v = f\lambda$.* $v = 500 \times 0.70 = 350$ m/s, inside the expected range, which is the check. This is the most accurate school method of all, because both measurements are of things that hold still.

## Common Misconceptions (Teaching Notes)

### 1. "The air travels from the speaker to my ear"

**Fix:** the film in Part I, watching the red particle. Then the queue: a nudge passes down a line of people and nobody moves along. A wind is air travelling; a sound is a disturbance travelling *through* air that stays put.

### 2. "Louder sounds are higher" (or "higher sounds travel faster")

Students fuse the two qualities because a shouting voice also rises in pitch. **Fix:** the first three sound files, then the four traces. Loud-and-low and quiet-and-high both exist. And if speed depended on frequency, a distant band would arrive with the piccolo ahead of the tuba.

### 3. "Sound is slower in solids because they are dense"

**Fix:** the contest $v = \sqrt{\text{stiffness}/\text{density}}$ and the table: density up by thousands, stiffness up by a million. Then the ear on the desk while someone scratches the far end.

### 4. "The pressure graph shows the particles moving up and down"

**Fix:** read the axis aloud. Vertical is pressure, not position; the particles move along the direction of travel. Draw the dots above the graph, as in the figure, every time.

### 5. Forgetting the factor of two in an echo

**Fix:** sketch the path before writing a number. The sound went to the wall *and came back*; the distance to the wall is $vt/2$.

### 6. "20 to 20 000"

**Fix:** a range is two numbers and a unit. 20 Hz to 20 000 Hz, or 20 Hz to 20 kHz.

## Exam Notes

### Cambridge 0625 (IGCSE) — §3.4 Sound (Papers 1–4, and the speed experiment on Papers 5/6)

Core: (1) production of sound by vibrating sources; (2) its longitudinal nature; (3) the audible range **20 Hz to 20 000 Hz**; (4) a medium is needed; (5) the speed in air is approximately **330–350 m/s**; (6) a method for determining that speed from a measurement of distance and time; (7) how amplitude and frequency affect loudness and pitch; (8) an echo as a reflection of sound; (9) ultrasound as sound above 20 kHz. Supplement: (10) compression and rarefaction; (11) sound is in general faster in solids than liquids and in liquids than gases; (12) the uses of ultrasound. Outcomes 8, 9 and 12 are taught in full in [[Ultrasound]]. The questions are short and recurring: define compression and rarefaction (the comparison "than normal" is the mark), state the speed or the range (with unit), a one-way $s = vt$ for thunder, fireworks or a whistle, a there-and-back $2d = vt$ for an echo, $v = f\lambda$ with a kilohertz to convert, the loudness–pitch table, labelling C and R on a pressure graph, and "why is the students' value wrong" (reaction time; distance too small).

### Cambridge 9702 (A Level)

There is no separate sound section. Sound is the standing example of a longitudinal wave in §7.1, the subject of the oscilloscope frequency measurement, the wave in the air columns of §8.1 ([[Stationary Waves]]) and the wave of §7.3 ([[Doppler Effect]]). Example 6 is typical: a trace, a stationary wave and $v = f\lambda$ in one question. Audible range, loudness and pitch are assumed from IGCSE and not examined as such.

### IB Physics — C.2 Wave model

"The nature of sound waves" sits in C.2 beside electromagnetic waves: longitudinal, mechanical, compressions and rarefactions, speed depending on the medium. Sound intensity appears in the experimental-skills list, and the IB data booklet does not require the decibel.

### AP Physics 2 — Unit 14

14.1.A: sound waves are modelled as mechanical longitudinal waves; regions of high and low pressure are compressions and rarefactions; the amplitude of a pressure wave is the maximum change from equilibrium pressure; **loudness increases with amplitude**; in a given medium the speed of sound **increases with temperature**. 14.2.A: the frequency of a sound is related to its **pitch**. Beats and standing waves in pipes are 14.6.

### Where it is *not* examined

- **AP Physics 1 and AP Physics C** contain no waves or sound.
- **The decibel scale, timbre and harmonics of instruments** are not required on 0625; harmonics enter at A Level through stationary waves.
- **The formula $v = \sqrt{\text{stiffness}/\text{density}}$** is not required on 0625, which asks only for the ordering gas < liquid < solid.

---

## Connections

- **Builds on:** [[Progressive Waves]] — $v = f\lambda$, longitudinal against transverse, intensity as amplitude squared; [[Simple Harmonic Motion]] — what each air particle is doing; [[Density and Pressure]] — the pressure that a compression raises; [[Planning an Experiment]] — many-and-divide, and why the stopwatch fails over 60 m.
- **Extends into:** [[Ultrasound]] — echoes turned into sonar, scanning and flaw detection; [[Doppler Effect]] — what motion does to the pitch; [[Stationary Waves]] — the air columns of pipes and the harmonics that make timbre; [[Superposition and Interference]] — beats, and the anti-noise of a headphone.
- **Physics of the medium:** [[Kinetic Theory and the Ideal Gas]] — molecular speeds rise as $\sqrt{T}$, and the speed of sound rides on them; [[Stress, Strain and Young Modulus]] — the stiffness of a solid.
- **Story:** [[Laplace and Napoleon]] — the life of the man who found the missing factor in Newton's speed of sound.
- **CS bridge:** [[Sound Encoding]] — sampling the pressure graph 44 100 times a second, and why that number is just over twice 20 kHz.

---

## Beyond Syllabus

### Newton's famous wrong answer
Recall that the speed is $\sqrt{\text{stiffness}/\text{density}}$. Newton, in the *Principia*, took the stiffness of air to be its pressure, which is what Boyle's law gives if the air stays at constant temperature as it is squeezed: $v = \sqrt{P/\rho} = \sqrt{101\,325/1.204} = 290$ m/s. Measurements said about 340. The discrepancy stood for over a century, until Laplace saw that sound is far too quick for heat to flow between compressions and rarefactions: a compression warms, which makes it push back harder. The squeeze is **adiabatic**, the stiffness is $\gamma P$ with $\gamma = 1.4$ for air, and $\sqrt{1.4} \times 290 = 343$ m/s. Rewriting it with the ideal-gas law gives $v = \sqrt{\gamma R T / M}$, which is why temperature appears and pressure does not.

### The decibel, properly
Sound intensity level is $L = 10 \log_{10}(I/I_0)$ dB with $I_0 = 10^{-12}$ W m⁻², roughly the threshold of hearing at 1 kHz. Ten times the intensity is $+10$ dB and is heard as about *twice* as loud; doubling the amplitude is $+6$ dB. Conversation is near 60 dB, a rock concert 110 dB, and the ear covers a range of intensities of a million million, which is the reason for using a logarithm.

### Timbre is the recipe of harmonics
A flute and a violin playing the same A at the same loudness are told apart at once. Both waves repeat 440 times a second, and the *shape* of each repeat differs, which by Fourier's theorem means a different mixture of the harmonics 440, 880, 1320 Hz and so on. `sound-a440-reedy.wav` is the sine wave plus five harmonics in falling proportion. The start of the note (the attack) matters as much as the steady mixture: cut the first tenth of a second off a recorded piano note and it becomes hard to name the instrument.

### Faster than sound
An aircraft flying faster than 343 m/s outruns its own pressure waves, which pile up into a cone-shaped shock front; the sudden pressure jump as the cone sweeps past a listener is the **sonic boom**. It is continuous along the flight path, not a single event at "breaking the barrier". The crack of a whip is the same thing on a small scale: the tip exceeds the speed of sound.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $v = f\lambda$ | `v = f\lambda` | wave equation |
| $d = vt$, $2d = vt$ | `d = vt` | one-way journey; echo |
| $f = 1/T$ | `f = 1/T` | frequency from the period read off a trace |
| $v = \sqrt{\gamma P/\rho}$ | `v = \sqrt{\gamma P/\rho}` | speed of sound in a gas |
| $L = 10\log_{10}(I/I_0)$ | `L = 10\log_{10}(I/I_0)` | intensity level in decibels |
