---
chinese: 数字音频工作站 (shùzì yīnpín gōngzuòzhàn)
prerequisites:
  - "[[Sound Encoding]]"
  - "[[Fourier Transform]]"
  - "[[Arrays]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/data-representation
  - domain/digital-signal-processing
  - level/university
  - type/deep
  - type/visual-tool
  - misconception/midi-is-recorded-sound
  - misconception/float-prevents-all-clipping
  - misconception/smaller-buffer-always-better
---

# Digital Audio Workstation 数字音频工作站

## Definition — the studio is a program

A **digital audio workstation (DAW)** is software for arranging, recording, generating, processing and mixing audio. Its timeline says *when* things happen; its routing graph says *where* their signals go. Behind the coloured rectangles is a stream of numbers, and behind the Play button is a deadline.

[[One Take, Many Tracks]] explains the historical leap from cutting tape to editing references to recordings. [[Sound Encoding]] explains how a waveform becomes samples. Now follow those samples through a small working studio: **mix → shape → control → place in a room → export**.

### 中文锚点

给朋友录一首生日歌，你发现吉他盖住了人声。用手机把合唱录成一个文件，再调小音量，人声也跟着小了；如果人声和吉他分别录在两条轨道上，你就能只把吉他调轻一点，再把它们合起来。数字音频工作站把这件事变成了电脑里的日常操作：每条轨道各自存着一串表示声音的数字，推低吉他的推子，就是先把它那串数缩小，再和人声对应时刻的数相加。屏幕上的推子看起来像录音棚的设备，背后做的却是我们熟悉的乘法和加法。

## 1. A track is an array; a mix is a sum

A mono recording can be represented by $x[n]$, the sample at index $n$. At sample rate $f_s$, its time is $n/f_s$ seconds. Stereo needs two sequences, often stored as an array of shape `(number_of_samples, 2)`. Tracks can contain several clips, instruments and effects; their **rendered output**, rather than the entire track object, is the array being mixed.

If track $i$ starts at sample $s_i$, its gain is $g_i[n]$, and absent samples are zero, a mono mix is

$$\boxed{y[n]=\sum_i g_i[n]x_i[n-s_i].}$$

Why add? In a linear acoustic approximation, sound pressures from different sources superpose at the listener. Digital mixing constructs the electrical signal that asks a speaker to reproduce that sum. Phase matters: $x+x=2x$, but $x+(-x)=0$. Two tracks are not two independent loudness readings that can simply be added in decibels.

**Gain is multiplication.** An amplitude gain of $g>0$ is $G=20\log_{10}g$ dB, so $g=10^{G/20}$. The factor 20 comes from power being proportional to amplitude squared at fixed impedance: $10\log_{10}(g^2)=20\log_{10}g$. Thus +6.02 dB doubles amplitude; −6.02 dB halves it. This does not say perceived loudness doubles.

**dBFS** compares a digital level with full scale. For normalised sample peaks, 1 corresponds to 0 dBFS, .5 to −6.02 dBFS. State whether a meter measures sample peak, RMS, true peak or loudness: they answer different questions. RMS involves averaging squared samples; LUFS adds frequency weighting and specified integration/gating. Two signals with equal RMS can still sound differently loud.

### Pan: divide one signal between two speakers

For a mono signal and pan position $p\in[-1,1]$, one equal-power law is

$$\theta=\frac{\pi(p+1)}4,\qquad L=x\cos\theta,\quad R=x\sin\theta.$$

Since $L^2+R^2=x^2$, the sum of channel powers stays constant. At centre, each channel is $x/\sqrt2$, or −3.01 dB. This is a **panning convention**, not a guarantee of constant perceived loudness in every room. Correlated channels add differently when folded to mono; other pan laws make different compromises. A stereo balance control is also different from panning one mono source.

### Headroom: the number 1 is not always a wall

IEEE 754 **32-bit floating point** can represent numbers much larger than 1, with roughly 24 significant binary digits for normal values. A floating-point mixer can store 1.6 and later multiply by .5 to recover .8 without having clipped that peak. It still rounds: it is neither exact arithmetic nor infinite headroom. Many engines also use 64-bit accumulation at mix points.

An integer PCM destination, an analogue circuit or a converter has a finite range. Once a peak has been flattened, turning it down cannot recover the missing shape. Plugins can also saturate deliberately, or have their own internal limits. “32-bit float recording” does not by itself rescue an overloaded microphone or analogue input stage. [[Floating-Point Representation]] explains the number format; [Audacity's digital-audio documentation](https://manual.audacityteam.org/man/digital_audio.html) distinguishes stored float peaks from output clipping.

Leave output margin: the reconstructed continuous waveform can peak above every stored sample (**intersample peaks**). A sample-peak check is useful but is not a true-peak certification.

## 2. The routing graph is function composition

An insert chain applies operations in order:

$$x\longmapsto E(x)\longmapsto C(E(x))\longmapsto g\,C(E(x)),$$

where $E$ might be an EQ and $C$ a compressor. A **send** copies a proportion into another path; the return is added back. Several tracks can share one reverberation return, sounding as though they occupy the same space. A bus sums tracks before processing them together.

Order is part of the sound. A bass boost **before** a compressor can make low notes trigger more gain reduction; the same boost **after** the compressor cannot change what its detector already saw. Generally, $C(E(x))$ and $E(C(x))$ give different outputs. Two fixed linear time-invariant filters commute under ideal conditions; that special case should not be generalised to every effect.

Effects have memory. A filter remembers old samples, a compressor remembers its level envelope, a delay remembers a whole section of sound. A more honest block interface is

```python
output_block, next_state = effect(input_block, previous_state, parameters)
```

Resetting that state at every block creates a different signal, often with boundary artifacts. The supplied EQ and compressor give **bit-identical output** whether run once on a test array or in successive 128-sample blocks, because the same objects retain their state.

## 3. Real time: finish before the queue empties

An audio interface consumes samples at a steady rate. The operating system calls the audio engine to prepare the next block of $B$ samples while already prepared sound plays. In a simplified one-block scheduling model, the budget is

$$\boxed{T_B=\frac{B}{f_s}.}$$

At 48 kHz, 128 samples span 2.667 ms; 512 span 10.667 ms. A smaller block shortens one source of waiting but demands more frequent callbacks. Fixed callback overhead consumes a larger fraction of the budget; scheduling delays and sudden workload peaks matter. Average CPU utilisation can look comfortable while a single callback misses its deadline.

An **underrun** means the output has no valid next block when needed. The recovery behaviour depends on the system: silence, repeated samples or a discontinuity may result. A buffer is a time cushion, not a source of extra computing power. A bigger buffer cannot cure a workload whose sustained processing rate exceeds the machine's capacity.

![[daw-manim.mp4]]

*Follow the moving playback cursor and the CPU's next-block work. First the calculation finishes early; then a callback misses its deadline. The second half separates this failure from intentional plugin delay. Motion is slowed for reading; the displayed millisecond values describe audio time.*

**Do not label $B/f_s$ “round-trip latency”.** Microphone-to-headphone delay also includes input buffering, output buffering, converters, drivers, scheduling and algorithmic delay. Measure the complete path if that is the question. Hardware direct monitoring can bypass the software round trip, at the cost of bypassing some software processing. [Ableton: how latency works](https://help.ableton.com/hc/en-us/articles/360010545559-How-Latency-Works)

### Plugin delay compensation: align arrivals, not CPU percentages

A lookahead compressor intentionally holds audio so it can inspect what is about to arrive. An FFT effect may require a window of future samples. This **algorithmic latency** differs from how many CPU instructions the plugin executes. A computationally expensive plugin can report zero sample delay; a cheap delay line can report a long one.

Suppose one branch delays a signal by 240 samples and another by zero. At their sum, matching events arrive 5 ms apart at 48 kHz. **Plugin delay compensation (PDC)** inserts 240 samples of waiting into the earlier branch. On a general graph, the host aligns the relevant accumulated path delays, using information reported by plugins. Playback can sometimes be scheduled ahead; a newly played live note cannot be fetched from the future. Compensation therefore preserves alignment without necessarily making monitoring immediate. [Ableton: instruments, effects and delay compensation](https://www.ableton.com/en/manual/working-with-instruments-and-effects/)

## 4. EQ: remember a little, reshape the spectrum

An **equaliser** changes the relative strength of frequency regions. Its simplest useful building block is often a **biquad**, a second-order recursive filter:

$$y[n]=b_0x[n]+b_1x[n-1]+b_2x[n-2]-a_1y[n-1]-a_2y[n-2].$$

The two old inputs and two old outputs are its state. Why does this change frequency balance? Feed in a complex oscillation $x[n]=e^{j\omega n}$. A one-sample delay multiplies it by $e^{-j\omega}$, and a two-sample delay by $e^{-2j\omega}$. In steady state, substitute $y[n]=H(e^{j\omega})e^{j\omega n}$ and collect terms:

$$\boxed{H(e^{j\omega})=\frac{b_0+b_1e^{-j\omega}+b_2e^{-2j\omega}}{1+a_1e^{-j\omega}+a_2e^{-2j\omega}}.}$$

Different frequencies cause different constructive and destructive combinations of the delayed copies. The magnitude gives gain; the argument gives phase shift. EQ is not merely repainting a spectrum display.

For a peaking bell with centre $f_0$, width parameter $Q>0$ and centre gain $G$ dB, set $A=10^{G/40}$, $\omega_0=2\pi f_0/f_s$, $\alpha=\sin\omega_0/(2Q)$. One standard design is

$$\begin{aligned}
(b_0,b_1,b_2)&=(1+\alpha A,\;-2\cos\omega_0,\;1-\alpha A),\\
(a_0,a_1,a_2)&=(1+\alpha/A,\;-2\cos\omega_0,\;1-\alpha/A).
\end{aligned}$$

Divide **all six coefficients by $a_0$** before using the recurrence above. Larger $Q$ gives a narrower bell for fixed gain. These are the peaking-EQ coefficients from [Robert Bristow-Johnson's Audio EQ Cookbook, published by W3C](https://www.w3.org/TR/audio-eq-cookbook/). The lab computes the recurrence directly, rather than calling a black-box EQ.

![[daw-eq.svg|740]]

*Purple: the coefficient formula predicts the response. Green: an FFT measures the output after a unit impulse passes through our implementation. Agreement checks the implemented filter, not just the attractiveness of the curve.*

![[daw-eq-ab.wav]]

*First four seconds: original keys. After 0.6 s silence: a 1.2 kHz bell cut, −9 dB, $Q=0.8$. The processed excerpt is RMS-matched to the original before one common safety gain. This controls average electrical level, not perceived loudness; listen for the changed balance of harmonics.*

## 5. Compression: change gain according to the signal

An audio **dynamic-range compressor** is not file compression. It reduces the gain of sufficiently strong passages relative to weaker ones. The detector may observe a peak estimate, RMS or a filtered sidechain; it need not observe exactly the audio being turned down.

For detector level $L$ dBFS, threshold $T$ and ratio $R\ge1$, a hard-knee static rule is

$$L_{\rm out}=\begin{cases}L,&L\le T,\\T+(L-T)/R,&L>T.\end{cases}$$

**Why the ratio?** Above threshold, each $R$ dB increase at the input produces only 1 dB more output. With $T=-20$ dBFS and $R=4$, a steady −8 dBFS input is 12 dB above threshold; the output should be 3 dB above it, or −17 dBFS. Required gain reduction: −9 dB, a multiplier $10^{-9/20}\approx0.355$.

An instantaneous detector would track each oscillation and can distort the waveform severely. The lab smooths rectified amplitude:

$$e[n]=a e[n-1]+(1-a)|x[n]|,\qquad a=e^{-1/(f_s\tau)}.$$

Use an **attack** time constant when $|x[n]|>e[n-1]$ and a **release** constant otherwise. For a step to a constant target, the remaining error multiplies by $a$ each sample; after $f_s\tau$ samples it has fallen to $e^{-1}$ of its initial value. That derives the coefficient and explains this particular time-constant convention. Plugin definitions vary.

Convert $e[n]$ to dB, apply the static rule, then multiply the original sample by the resulting gain. A short attack catches peaks more quickly; a longer attack lets a transient through. Release governs how gain recovers. This simple feed-forward peak detector has no lookahead, soft knee or makeup gain. A production stereo compressor commonly links its detectors so unequal gain changes do not pull the stereo image around.

![[daw-compressor.svg|760]]

![[daw-compressor-ab.wav]]

*Original keys, then compressed keys: −20 dBFS threshold, 4:1 ratio, 5 ms attack and 120 ms release. Each excerpt lasts four seconds, separated by 0.6 s; the second is RMS-matched before common attenuation. Compare the initial strike with the body of each note. Matching level is not the compressor itself “making things louder”.*

## 6. Delay and reverb: the past keeps contributing

A simple feedback delay obeys

$$y[n]=x[n]+\beta y[n-D],\qquad |\beta|<1.$$

Substitute the equation into itself: $y[n]=x[n]+\beta x[n-D]+\beta^2x[n-2D]+\cdots$. Every repeat is another $D$ samples later and another factor $\beta$ smaller. At 48 kHz, a quarter-second echo needs $D=12{,}000$ samples. The condition $|\beta|<1$ makes the ideal repeats decay. Exporting a finite file also requires a chosen tail duration.

![[daw-delay-ab.wav]]

*Two seconds dry, 0.6 s gap, then the same phrase with 250 ms feedback delay and a two-second tail. Feedback is 0.35. One common gain is applied to both; the delayed version is not RMS-matched.*

A room has thousands of reflection paths rather than one tidy echo. Let $h[k]$ be its **impulse response**: the recorded response to a very short excitation, or an estimate recovered from a known test signal. Under a linear, time-invariant approximation, each input sample launches a scaled and shifted copy of that response:

$$\boxed{y[n]=\sum_k h[k]x[n-k]=(h*x)[n].}$$

This follows from superposition. Write the input as a sum of shifted unit impulses; the room responds to each in the same shifted way; add their responses. Move the microphone, change the room or drive a nonlinear speaker too hard, and the same fixed response no longer describes the situation.

The supplied stereo recording is **Engineering II Atrium, University of Central Florida**, contributed by **Liam G** to **Conner's Impulse Response Library**. It is a clap-based creative response, not a calibrated measurement of the building: the excitation and recording chain colour it too. The original 96 kHz file is retained; the lab resamples it to 48 kHz and applies an explicit energy scale before choosing the wet-return level. [Pinned source and MIT licence](https://github.com/itsmusician/IR-Library/tree/07cbb6f8779a4a448d02355c355f0cef8916b78d) · [local licence](daw-room-ir-LICENSE.txt)

![[daw-room.svg|760]]

![[daw-room-ab.wav]]

*First: a two-second phrase followed by silence. After the comparison gap: the same phrase plus the stereo room return, with its tail retained. Each half is about 6.55 s. The wet return is set to 35% of the padded dry signal's RMS, then both halves share one safety gain. This is an artistic balance, not a physical distance calibration.*

Direct convolution with an $M$-sample response costs roughly $M$ multiplications per output sample. By the convolution theorem in [[Fourier Transform]], FFTs can multiply spectra instead. **Pad to at least $N+M-1$** for two finite sequences; otherwise the FFT computes circular convolution and wraps the tail into the beginning. Real-time reverbs use partitioned convolution to balance work against latency. The lab uses one offline, zero-padded FFT and checks it against direct convolution on a short case.

## 7. MIDI and automation: instructions are not pressure samples

A MIDI note event might say “note 69, velocity 90, on now”; a later event says to release it. An instrument decides what samples to produce. The same events can drive a piano sampler, a synthesiser or drums. MIDI 1.0 channel messages include note on/off, control changes and pitch bend; a Standard MIDI File or host supplies musical timing. MIDI velocity is a performance parameter whose audible meaning depends on the instrument, not a universally defined gain in dB. [MIDI Association: message summary](https://midi.org/summary-of-midi-1-0-messages)

For conventional equal temperament with A4 = 440 Hz, note number $m$ corresponds to $f=440\,2^{(m-69)/12}$. The lab's note list uses that mapping to synthesise keys; it is an event schedule, **not a MIDI-file parser**. Rendering freezes a particular instrument's interpretation into audio. Editing note events afterwards is different from trying to separate notes already mixed into a waveform.

**Automation** makes a parameter a function of time. For a two-second fade from −12 dB to 0 dB, interpolate the dB value, then compute $g[n]=10^{G[n]/20}$. Interpolating linear amplitude instead produces a different fade. Smooth changes matter: multiplying by an abruptly jumping gain introduces a discontinuity and extra high-frequency content. A DAW may interpolate between sparse control points or smooth block-rate parameter updates.

## 8. Bounce: finish the calculation and choose a destination

A **bounce** renders the routing graph to an audio file, in real time or offline. Offline rendering can take longer than the audio's duration without an underrun; it still must handle instruments, automation, random state and effect tails correctly. A ten-second arrangement can need a longer export so its last reverb is not cut off.

### Sample-rate conversion is filtering plus new sample positions

To convert 48 kHz to 44.1 kHz while preserving duration and pitch, use ratio $147/160$. Conceptually, insert intermediate samples, low-pass filter away images and frequencies the new rate cannot carry, then keep every 160th sample of the expanded stream. Efficient **polyphase** implementations avoid calculating values that will be discarded. The lab uses [SciPy's `resample_poly`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.resample_poly.html).

Changing the WAV header alone does something else: the same samples play at a different speed and pitch. Downsampling without filtering can fold high frequencies into false lower ones. A lab check converts a 12 kHz sine from 48 to 16 kHz; correct filtering suppresses it instead of turning it into an audible 4 kHz impostor.

### Dither: exchange signal-shaped error for a small noise floor

Rounding to integer PCM creates an error dependent on the input. A very quiet repeating waveform can stick to a few code values, making the error repeat with it. Before a final quantisation, adding appropriately distributed noise breaks that regular relationship.

For 16-bit normalised PCM, one least significant bit is $\Delta=1/32768$. The lab adds **TPDF dither**, $(U_1-U_2)\Delta$, where $U_1,U_2$ are independent uniform draws on $[0,1)$. The difference has a triangular distribution spanning approximately $[-\Delta,\Delta]$. Then it rounds once. This is non-subtractive dither: the noise stays in the exported file. Under the usual independence and no-overload assumptions, it removes signal dependence from the first two moments of quantisation error; it does not make the error vanish.

Dither belongs immediately before a required reduction to a fixed quantisation grid, after processing and resampling. Do not accumulate gratuitous dither at every insert; preserve floating-point intermediates when appropriate. It cannot cure clipping or aliasing. Noise-shaped dither redistributes noise across frequencies and is a separate design choice. [Ableton's audio fact sheet](https://www.ableton.com/en/manual/audio-fact-sheet/) describes its own engine and export behaviour; other DAWs need not use the same precision or algorithms.

## 9. Beyond syllabus — stretch time without lowering the note

Recall that the [[Fourier Transform#7. A spectrogram — ask locally, then move|short-time Fourier transform]] measures magnitude and phase in overlapping windows. Playing samples more slowly stretches time **and** lowers pitch. To separate the two, a **phase vocoder** estimates how rapidly each frequency component's phase is actually advancing.

For FFT bin $k$, window length $N$ and analysis hop $H$, a bin-centred oscillation advances by $2\pi kH/N$ between frames. Let measured frame phases be $\phi_m[k]$. Subtract that expected advance and wrap the residual into $[-\pi,\pi)$:

$$\delta_m[k]=\operatorname{wrap}\left(\phi_{m+1}[k]-\phi_m[k]-\frac{2\pi kH}{N}\right),\qquad
\widehat\omega_m[k]=\frac{2\pi k}{N}+\frac{\delta_m[k]}H.$$

The residual tells us how far the oscillation is from the bin centre. To synthesise at hop $H_s$, advance output phase by $\widehat\omega_m[k]H_s$; using a different number or spacing of output frames changes duration while retaining the estimated oscillation rate. Inverse FFT each frame, window again, overlap-add and normalise the accumulated window weights. Simply repeating frames with their old phases generally creates discontinuities at joins.

The implementation uses a fixed synthesis hop and interpolates magnitudes at fractional analysis-frame positions. It accumulates corrected phase advances rather than copying the original phases. This is a **basic mono teaching implementation**: attacks can smear; independent stereo processing can disrupt the image; moving partials and weak bins challenge the model. Commercial processors add transient handling, phase locking, source models and other strategies. [Julius O. Smith: phase-vocoder principles](https://ccrma.stanford.edu/~jos/sasp/Phase_Vocoder.html)

![[daw-stretch-ab.wav]]

*Two-second original phrase, 0.6 s gap, then a three-second version: 1.5× duration at approximately the same pitches. One common gain; no RMS matching. Listen especially to the strikes, where this simple algorithm is least convincing.*

![[daw-pitch-ab.wav]]

*Original, gap, then +3 semitones at the original duration. To raise pitch by factor $p=2^{3/12}$, first stretch duration by $p$, then resample the result to its original sample count at the same playback rate. A 440 Hz verification tone becomes approximately 523.25 Hz. This is a fixed pitch shift, not automatic correction.*

**Pitch correction adds another decision:** estimate a performed fundamental, select a target note, then vary the shift ratio over time. Note choice, correction speed, vibrato retention and formants all affect the result. A phase vocoder alone does not know what note the singer intended. Whether correction repairs a take or creates a new performance is an artistic judgement; explain the processing honestly rather than treating either choice as automatic fraud or automatic improvement.

## Worked examples — read the requirement before choosing the tool

### A. A mix clips although neither track clips

Two aligned copies of a signal each peak at 0.8. How much attenuation makes their sum peak at 0.8 again?

1. **Trigger: identical, aligned waveforms → add amplitudes.** The peak is $0.8+0.8=1.6$, not the sum of two dB readings.
2. **Tool: gain ratio.** $g=0.8/1.6=0.5$; attenuate the sum by $20\log_{10}(0.5)=-6.02$ dB.
3. **Trigger: ask where the overload occurred.** In a float bus retaining 1.6, this works. After hard clipping to 1, scaling gives a flattened peak of .5, not the original .8 shape. Prevention and repair are different operations.

### B. A comfortable average CPU meter, but audible dropouts

A 128-sample callback at 48 kHz occasionally takes 3.1 ms. The common case takes 1.2 ms. Is the occasional callback safe in a one-block budget?

1. **Trigger: a deadline question → use block duration, not average CPU.** $128/48000=2.667$ ms.
2. **Tool: compare worst observed execution with budget.** $3.1>2.667$; the excess is .433 ms. The simplified engine can underrun.
3. **Trigger: a monitoring task → count the latency trade-off.** 256 samples span 5.333 ms. That offers more time, but the 256-sample workload must be measured again; processing time is not guaranteed to stay at 3.1 ms. Reducing plugin load or fixing a scheduling spike may be preferable while recording.

### C. Two routes from one snare cancel badly

One route is delayed by 240 samples at 48 kHz. The second is undelayed. Why can summing them colour the snare?

1. **Trigger: delayed copies of one source → interference.** The difference is $240/48000=5$ ms.
2. **Tool: phase difference $2\pi f\tau$.** At 100 Hz the difference is $\pi$: equal-amplitude copies cancel that sinusoidal component. At 200 Hz they add. Repetition produces a **comb filter**, not simply a louder snare.
3. **Trigger: unwanted path misalignment → delay the earlier path.** Align both before the sum, provided the delay is known. This repairs timing, not other phase changes an EQ may introduce.

## Hands-on — a small studio you can inspect

Run these from the directory containing the files, with Python, NumPy, SciPy and Matplotlib installed:

```bash
python3 daw-lab.py
python3 daw-mixer.py
```

The first command creates three original eight-second stems and the effect comparisons, then checks the DSP. The second loads those WAV files, processes the keys, automates gain, pans all three tracks, adds a room return and writes stereo PCM16 at 48 kHz, plus a filtered 44.1 kHz version. Comparison clips use 5 ms edge fades so their edit boundaries do not become the demonstration. No commercial recording or DAW installation is required. Sources: [DSP and asset generator](daw-lab.py) · [small mixer](daw-mixer.py) · [Manim source](daw-manim.py).

The mixer's central operations are ordinary Python:

```python
keys_eq = dsp.Biquad(b, a).process(keys)
keys_comp, _ = dsp.Compressor().process(keys_eq)
automation_db = np.interp(t, [0, 2, 6, 8], [-3, 0, 0, -12])
keys_comp *= dsp.db_gain(automation_db)
mix = dsp.pan(keys_comp, -.3) + dsp.pan(bass, 0) + dsp.pan(drums, .25)
wet = dsp.convolution(keys_comp, dsp.room_ir())
# The complete mixer scales the return, pads for its tail, then adds it.
```

![[daw-mix-ab.wav]]

*Dry mix first, then processed mix, with 0.6 s between them. Each half lasts about 12.55 s including tail space. Both share the same gain; no loudness matching is claimed for this whole-chain demonstration. Individual EQ and compressor comparisons above isolate those changes more carefully.*

Try three predictions before rerunning: move the EQ after the compressor; pan the bass hard left and then fold to mono; export only eight seconds and find what disappears. The experiment is not “which preset sounds expensive?” It is **which operation caused the audible change?** The scripts render offline; they do not implement an audio driver or demonstrate a measured real-time performance guarantee.

## Common misconceptions

| Claim | What to keep straight |
|---|---|
| “A WAV is a song; MIDI is another audio format.” | WAV commonly stores samples; MIDI carries performance/control messages interpreted by an instrument. |
| “A 32-bit float project cannot clip.” | Intermediate values may survive above 1; converters, integer exports and plugins still have limits. |
| “A lower buffer setting improves sound quality.” | It mainly changes timing and scheduling demands; missed deadlines can make it worse. |
| “Compression makes every quiet sound louder.” | Gain reduction acts on louder passages; makeup gain is an additional operation. |
| “Reverb is just many quiet copies with no tonal effect.” | Reflections also interfere and absorb frequencies differently; the response has a spectrum. |
| “Dither is a mastering enhancer to add repeatedly.” | It manages a particular quantisation step by adding noise; it is not a general improvement button. |

## Exam Notes

### Cambridge 0478 and 9618

**DAW engineering is enrichment.** 0478 §1.2 and 9618 §1.2 examine sound sampling, resolution and file-size relationships, taught in [[Sound Encoding]]. 9618 §3.1 also asks about buffers; the audio deadline is a concrete application, not a new requirement to derive DSP algorithms. Do not substitute compressor ratios for lossy/lossless file compression or equate buffer length with sample resolution.

### IB Computer Science — first assessment 2027

A1.2.2 includes mechanisms for representing data including audio. That is a representation link, not a syllabus demand for biquads, phase vocoders or mastering. Use the corresponding representation concepts when answering; this production chain is an extension.

### Where it is not examined

The DAW algorithms, PDC and production decisions developed here are not specified outcomes in Cambridge 0478 (2026–28), 9618 (2027–29), IB CS (2027) or AP Computer Science A (current course description). AP CSA's arrays, iteration and methods can express a simplified mixer, but that does not make audio engineering an AP topic. No new mapped syllabus row is closed by this treatment.

## Connections

- **[[Sound Encoding]] → here:** samples and formats become something to compute with.
- **[[Arrays]] → here:** index by time; keep channels and sample rate explicit.
- **[[Fourier Transform]] → here:** frequency response, convolution and the moving-window analysis behind stretching.
- **[[Floating-Point Representation]]:** headroom and precision are different properties of a number format.
- **[[Operating Systems]]:** an audio callback is a scheduling obligation with a deadline.
- **[[One Take, Many Tracks]]:** editing and mixing changed what a performance could mean.
- **[[The Loudness War]]:** a louder comparison is persuasive even when it hides lost dynamics; level-aware listening is part of honest evaluation.

## LaTeX Reference

| Idea | LaTeX |
|---|---|
| Mix | `y[n]=\sum_i g_i[n]x_i[n-s_i]` |
| Gain | `G=20\log_{10}g` |
| Block time | `T_B=B/f_s` |
| Convolution | `y[n]=\sum_k h[k]x[n-k]` |
| Envelope coefficient | `a=e^{-1/(f_s\tau)}` |
| Pitch ratio | `p=2^{s/12}` |
