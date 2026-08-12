---
chinese: 声音编码 (shēngyīn biānmǎ)
prerequisites:
  - "[[Number Bases]]"
  - "[[Text Encoding]]"
  - "[[Storage Units (Vocab)]]"
  - "[[One Take, Many Tracks]]"
  - "[[The Loudness War]]"
leads_to:
  - "[[Compression]]"
tags:
  - subject/computer-science
  - domain/data-representation
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-1-2
  - syllabus/9618-1-2
  - type/deep
  - type/definition
  - notation/binary
  - misconception/digital-audio-is-stairsteps
  - misconception/sample-rate-confused-with-resolution
---

# Sound Encoding 声音编码

> *Sound is pressure changing in time. The computer's trick is a metronome and a ruler: at every tick, measure the height, write down the number. The whole subject is two questions — how fast the metronome ticks, and how fine the ruler is marked.*

Here is the strangest number in your pocket: **44,100**. Every CD, and most music you have ever streamed, is sound measured exactly $44{,}100$ times per second — not a round $40{,}000$, not $50{,}000$. Why *that* number? The answer involves the ceiling of your own hearing, one of the great theorems of engineering, and — of all things — a 1970s videotape recorder. By the end it will feel inevitable.

## 中文锚点

**声音编码 (shēngyīn biānmǎ)** = sound encoding：把连续的声波变成一串数字——

- **模拟 (analogue)** vs **数字 (digital)**：声音本身是*连续*的气压波（麦克风把它变成连续电压）；计算机只能存*离散*的数字，所以必须**测量**。
- **采样 (sampling)**：每隔固定时间量一次波形的**振幅**（高度）。**采样率 (sample / sampling rate)** = 每秒采样次数（单位 Hz）；CD 是 $44{,}100$ Hz。
- **采样精度 (sample / sampling resolution)** = 每个样本用几位二进制存（CD 是 $16$ 位）——决定振幅量得多准；量不准的误差叫**量化误差 (quantisation error)**。
- **奈奎斯特定理 (Nyquist)**：采样率只要**超过最高频率的两倍**，低于该频率的波形就*一点不丢*——所以 $2 \times 20\text{kHz（人耳上限）} < 44.1$ kHz。
- 文件大小 = 采样率 × 采样精度 × 声道数 × 时长。与图像完全平行：图像在**空间**采样，声音在**时间**采样。

---

## Analogue to digital — why sound must be measured

A sound is a **pressure wave**: air squeezed and released, hundreds or thousands of times a second. A microphone converts pressure into voltage, faithfully and *continuously* — the voltage is an **analogue** signal, a physical copy of the wave with infinitely fine detail at every instant. And that is exactly the problem: a computer cannot store "every instant." Like the photograph in [[Image Encoding]], the world offers no recipe here — a signal must be **measured**.

So the computer does the only thing it can: **sampling.** At perfectly regular time intervals — tick, tick, tick — it measures the wave's **amplitude** (its height at that instant) and stores each measurement as a binary number ([[Number Bases]]). A sound file is nothing but that list of measurements, plus a header stating the treaty ([[Text Encoding]]'s lesson, again: bytes don't announce their own meaning).

Two dials control everything — the exact twins of the image's two:

| | Sound 声音 (time) | Image 图像 (space) |
|---|---|---|
| How *often* to measure | **sample rate** (samples per second, Hz) | resolution (pixels) |
| How *finely* to measure | **sample resolution** (bits per sample) | colour depth (bits per pixel) |
| The failure mode | aliasing | jaggies, moiré |
| File size | rate × resolution × channels × time | width × height × depth |

![[sound-encoding-sampling.svg|700]]

---

## The first dial — sample rate, and the Nyquist theorem

**Sample rate** = the number of samples taken per second, in hertz. Intuition says: the faster you tick, the closer the dots trace the wave, and surely the wave *between* the dots is lost forever?

Here intuition is beautifully, provably wrong. The **Nyquist–Shannon sampling theorem** (Nyquist 1928, Shannon 1949 — the same Shannon of [[Information Theory]]) says:

> If a signal contains no frequency above $f$, then sampling at any rate **greater than $2f$** captures it *perfectly*. Not approximately — the smooth wave can be rebuilt **exactly** from the dots.

Why $2$? A sine wave is pinned down by hitting it at least twice per cycle — once to catch it up, once down. Sample slower than that and something worse than blur happens: the samples fit a *different, slower* sine wave equally well, and the reconstruction confidently produces **the wrong sound**. That impostor is called **aliasing**:

![[sound-encoding-aliasing.svg|697]]

You have seen aliasing your whole life: wheels in films spinning slowly backwards (24 frames per second undersamples the spokes' rotation — aliasing in *time*), and the moiré shimmer from [[Image Encoding]] (aliasing in *space*). One theorem, three costumes.

**Now 44,100 becomes inevitable.** Human hearing tops out near $20$ kHz (less as you age). Nyquist demands more than $2 \times 20{,}000 = 40{,}000$ samples per second to capture everything audible. Add a safety margin for the electronics, and you need something a little above $40$ kHz — and the *specific* number came from a hack: the first digital audio recorders stored their samples on **videotape**, the only medium fast enough in the late 1970s, and $44{,}100 = 245 \times 60 \times 3 = 294 \times 50 \times 3$ fits *exactly* onto the video lines of both the American (NTSC) and European (PAL) television standards. The strangest number in your pocket is your ear's ceiling, doubled by a theorem, rounded up by a videotape.

**Hear the first dial.** The same song at three sample rates — listen for the *highs* disappearing as Nyquist's ceiling drops (at $8$ kHz, nothing above $4$ kHz survives — the telephone sound):

![[sound-encoding-demo-24khz.m4a]]
![[sound-encoding-demo-12khz.m4a]]
![[sound-encoding-demo-8khz.m4a]]

> [!warning] The staircase myth
> Diagrams (including the one above) draw digital audio as dots or steps, so almost everyone believes digital sound *is* a staircase — jagged, missing the "smoothness between the samples." It is not. The reconstruction at playback produces a **smooth wave**, and below the Nyquist limit it is *the* wave, exactly. Digital audio done right does not approximate the analogue signal in the audible band — it equals it. (What is genuinely lost lives in the *other* dial.)

---

## The second dial — sample resolution and quantisation error

Each measurement must itself be stored in a finite number of bits: the **sample resolution** (also called bit depth). With $n$ bits there are $2^n$ possible amplitude values, and every true amplitude gets rounded to the nearest one. That rounding is **quantisation error** — the same disease as [[Floating-Point Representation]]'s rounding error, caught at the moment of measurement: the ruler has finitely many marks, so heights between marks are recorded wrongly by up to half a step.

![[sound-encoding-resolution.svg|700]]

- **$16$ bits** (CD): $65{,}536$ levels — the error is a whisper roughly $96$ dB below the music (each extra bit halves the step, adding $\approx 6$ dB of headroom), far below audibility in normal listening.
- **$8$ bits**: $256$ levels — the error becomes an audible hiss and crunch; the sound of early samplers, talking arcade chips, and cheap answering machines.
- **$24$ bits** (studios): not for the ear at playback, but working room — every edit and effect adds a little rounding ([[Floating-Point Representation]] again), so engineers start with error far below what anyone can hear.

**Hear the second dial.** Same song, same sample rate, three rulers — listen for the *noise floor* rising as the levels get coarser:

![[sound-encoding-demo-16bit.m4a]]
![[sound-encoding-demo-8bit.m4a]]
![[sound-encoding-demo-4bit.m4a]]

So the two dials fail differently, and this is the sharpest way to remember them: **too low a sample rate loses the *highs* (and invents aliases); too low a resolution buries the sound in *noise*.** Rate is about *which frequencies survive*; resolution is about *how clean each one is*.

> [!info] So what is "8-bit music," then?
> *Not* 8-bit sampling! The chiptune sound of the NES and Game Boy era is **synthesised**, not sampled — those consoles barely played recordings at all; a sound chip *generated* square, triangle and noise waveforms live, and the music was a score the chip performed. The "8" names the **era's CPUs** — processors whose registers and data bus were one byte wide ([[CPU Architecture and the Fetch-Execute Cycle]]) — and the aesthetic is the shadow of the whole machine's constraints: two square-wave voices, a triangle, and noise, because that is all the chip had. True 8-bit *sampling* — the crunchy hiss in the demo above — is a different sound entirely (early samplers, answering machines). Today "8-bit" is pure style, composed on 64-bit machines by people who choose the constraints on purpose.

---

## File size — the dials multiplied

$$\text{file size} \;=\; \text{sample rate} \times \text{sample resolution} \times \text{channels} \times \text{seconds}$$

**Worked (a real exam setup):** a $50$ kHz recording, $16$ bits per sample, mono, $20$ minutes: $50{,}000 \times 16 \times 1200$ s $= 960{,}000{,}000$ bits $= 120{,}000{,}000$ B $= 120$ MB (decimal, as the question's "MB" requests — read the unit: MB ÷1000s, MiB ÷1024s, [[Storage Units (Vocab)]]).

CD-quality stereo runs $44{,}100 \times 16 \times 2 = 1{,}411{,}200$ bits per second — about $10$ MiB per minute, the $30$ MiB three-minute song from [[Storage Units (Vocab)]]. Your streamed version is a tenth of that: [[Compression]] again, and for sound it can even throw away *real* data your ear would never have noticed — the perceptual trick that made the MP3 famous.

---

## Worked examples

**Example 1 — choose a sample rate.** Telephone speech only needs frequencies up to about $3.4$ kHz to stay intelligible. Nyquist: rate $> 2 \times 3400 = 6800$ Hz — and real telephone networks standardised on $8{,}000$ Hz, a comfortable margin. (This is why music on hold sounds so thin: everything above $4$ kHz never crosses the line.)

**Example 2 — effects of changes.** A recording's sample rate rises from $40$ kHz to $60$ kHz: accuracy **increases** (samples closer together — smaller gaps in the wave, smaller quantisation-in-time error) and file size increases proportionally. The recording's *duration* doubles: file size doubles, accuracy **unchanged** (the dials didn't move). Resolution drops $24 \to 16$ bits: file size falls by a third, accuracy **decreases** — fewer amplitude values available, larger quantisation errors.

**Example 3 — file size with unit discipline.** $44{,}100$ Hz, $16$-bit, stereo, $30$ s: $44{,}100 \times 16 \times 2 \times 30 = 42{,}336{,}000$ bits $= 5{,}292{,}000$ B $\approx 5.05$ MiB. Bits first, bytes next, ladder last.

**Example 4 — spot the alias.** A $30$ kHz ultrasonic tone leaks into a $44.1$ kHz recording. It is *above* Nyquist ($22.05$ kHz), so it does not disappear — it reflects to $44{,}100 - 30{,}000 = 14{,}100$ Hz: a loud, fully audible whistle that was never in the room. This is why every real recorder filters out ultrasonics *before* sampling (the "anti-aliasing filter").

---

## Exam Notes

### Cambridge 0478 (IGCSE)

**§1.2.2 — sound representation.** The three definitions, in the mark schemes' own shape: **sampling** — measuring the height/**amplitude** of the sound wave at regular time intervals; **sample rate** — the number of samples taken per second; **sample resolution** — the number of bits per sample. Expect "describe how sound is converted to digital" (microphone → wave sampled at set rate → each amplitude stored as binary at set resolution) and the benefits/drawbacks of raising either dial (closer to original vs bigger file).

### Cambridge 9618 (A-Level)

**§1.2 Sound.** Same machinery with sharper language: the terms appear as **sampling rate / sampling resolution** (the *sample-*/*sampling-* prefix varies freely across papers — the definitions never do), plus **analogue vs digital** explicitly, and the effects of changing each dial on **file size and accuracy** — two separate axes, and questions ask about one at a time.

> [!tip] What the examiner reports actually punish — the pattern from 2021–2025
> 1. **The #1 documented error, year after year: answering *rate* when asked *resolution*** (or vice versa). Lock the pairing: **rate → how often → time-axis; resolution → how many bits → amplitude-axis.** Reports also flag a second bleed: confusing *sampling* resolution with *image* resolution — the word "resolution" is overloaded, so name the axis in your answer.
> 2. **Circular definitions score zero at A-Level:** "the sampling rate is the rate of taking samples" was explicitly rejected. Say *number of samples per second*.
> 3. **Effect questions want the mechanism, not the definition restated.** "Higher rate → more accurate" repeats the question. The mark-scheme mechanisms: *smaller gaps between samples*, *more amplitude values available per sample*, **smaller quantisation errors**, *digital waveform closer to the analogue waveform*. Use those phrases — "quantisation error" is mark-scheme vocabulary at 9618.
> 4. **State the direction** (increase/decrease) explicitly, and answer the axis asked: accuracy statements don't score on a file-size question or vice versa.
> 5. **Calculations:** channels only if the question states them (past 9618 calculations have been mono); and read the target unit — a 9618 mark scheme has run "960,000,000 bits = 120,000,000 bytes = **120 MB**" in *decimal*, because the question said MB. MB ÷1000, MiB ÷1024, always bits→bytes first.

### IB CS (2027)

Sound representation is **not a named statement**: A1.2's published wording stops at binary/hexadecimal conversion and logic gates processing encoded data — sampling, sample rate and resolution are not listed. Treat this card as depth behind "encoded data", not examinable IB content.

---

## Connections

- **Prerequisite:** [[Number Bases]] — each sample is a plain binary number; the whole file is a list of them.
- **Prerequisite:** [[Text Encoding]] — the treaty-vs-signal split: text needed no measuring, sound is pure measurement; and the sound file's header declares its rate and resolution, or the bytes are noise.
- **Prerequisite:** [[Storage Units (Vocab)]] — the file-size formula and the MB/MiB discipline.
- **Sibling:** [[Image Encoding]] — the same two dials in space instead of time; aliasing ↔ moiré; sample resolution ↔ colour depth. Read the two cards as one idea, sampled twice.
- **Sequel:** [[Compression]] — sound is where compression gets *perceptual*: MP3 discards real data your ear masks anyway, the boldest version of "remove what won't be noticed."
- **Cross-domain:** [[Information Theory]] — Shannon of Nyquist–Shannon; the sampling theorem is the bridge between continuous physics and discrete bits, and bits-per-second here is literally his channel currency. [[Floating-Point Representation]] — quantisation error *is* rounding error, caught at the microphone instead of the ALU.
- **Physics:** [[Waves I: The Wave Equation]] and [[Sound Waves]] — amplitude, frequency, superposition: the physical thing every sample measures. The microphone's diaphragm is doing mechanics before the ADC does mathematics.
- **Mathematics:** [[Fourier Series]] — the theorem beneath the theorem: *every* wave decomposes into pure sines, which is why "contains no frequency above $f$" is even a meaningful sentence, and why Nyquist can promise perfection below it. [[Logarithms]] — the decibel is a log scale, which is why each bit of resolution adds a constant $6$ dB.
- **Story:** [[Stories/One Take, Many Tracks]] — a century of studios fighting for what these numbers finally delivered: random access to time. Wax discs allowed no mistakes; tape met the razor blade; Les Paul stacked a dozen guitars on parallel tracks; digital made every edit a reversible pointer. The reason samples-are-numbers mattered, told through the people who needed it.

---

## Notation Reference

| Notation | Meaning |
|---|---|
| $44.1$ kHz | sample rate — samples per second |
| $16$-bit | sample resolution — bits per sample ($2^{16} = 65{,}536$ levels) |
| $> 2f$ | the Nyquist condition — sample faster than twice the highest frequency |
| dB | decibel — logarithmic loudness ratio; each resolution bit buys $\approx 6$ dB over the error floor |
| kbps | kilobits per second — bit rate = rate × resolution × channels |
