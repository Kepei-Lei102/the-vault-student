---
chinese: 准确度与精确度 (zhǔnquèdù yǔ jīngquèdù)
prerequisites:
  - "[[Upper and Lower Bounds]]"
  - "[[Physical Quantities and Units]]"
leads_to:
  - "[[Significant Figures]]"
  - "[[Repeated Measurements]]"
  - "[[Calibration of Instruments]]"
  - "[[Stories/The 1919 Eclipse]]"
  - "[[The 1919 Eclipse]]"
teach_together:
  - "[[Error Propagation]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/experimental-physics
  - domain/measurement
  - level/A-Level
  - level/IB
  - level/AP
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-2
  - syllabus/9702-1-3
  - syllabus/0625-P5
  - syllabus/0625-P6
  - syllabus/0625-P7
  - syllabus/IB-Physics-PRAC-2
  - syllabus/AP-Physics-1-SP-1
  - type/deep
  - type/definition
  - type/vocabulary
  - notation/sigma-uncertainty
  - notation/Delta
  - misconception/accuracy-equals-precision
  - misconception/more-decimals-means-more-accurate
  - misconception/averaging-removes-systematic-error
  - misconception/precision-is-instrument-specification
---

# Accuracy vs Precision 准确度与精确度

## Hunter trace — why do we need two words for one thing?

Imagine four students measure the boiling point of water in a school lab. They each take five readings, average them, and report:

| Student | Mean | Spread between readings |
|---|---|---|
| A | $100.0~^\circ\text{C}$ | $\pm 0.2~^\circ\text{C}$ |
| B | $100.1~^\circ\text{C}$ | $\pm 5.0~^\circ\text{C}$ |
| C | $98.3~^\circ\text{C}$ | $\pm 0.2~^\circ\text{C}$ |
| D | $97.0~^\circ\text{C}$ | $\pm 5.0~^\circ\text{C}$ |

Whose measurement is "best"? A is obviously the winner. But which of B, C, D is the *worst*? They are all wrong in different ways:

- **B** averages near the correct value but cannot reproduce the reading.
- **C** can reproduce the reading exactly — but the reading itself is wrong.
- **D** is both wrong on average *and* unable to reproduce.

The English language gives us two words — **accuracy** and **precision** — because there are *two independent ways a measurement can fail*. One word would lump B and C together, and lumping them together makes you fix the wrong problem. A student in B's situation needs a steadier hand or a more reproducible setup. A student in C's situation needs a *different thermometer* — a steadier hand will only get them more consistently wrong.

This is a card about **factoring** the single word "uncertainty" into two orthogonal pieces. Get that factorisation right, and "how do I improve this measurement?" stops being a guess and starts being a recipe.

## Definition

**Accuracy** (准确度 zhǔnquèdù) is how close the measured value is to the *true value*. A measurement is accurate when the average of many readings sits on top of the real answer. The opposite of accurate is **biased** — there is a systematic offset between what we measure and what is true.

**Precision** (精确度 jīngquèdù) is how close repeated measurements are to *each other*. A measurement is precise when, repeating the same procedure five times, you get five answers that cluster tightly together. The opposite of precise is **noisy** or **scattered**.

These are independent. A measurement can be:

- **Accurate and precise** — the gold standard. Average is right, spread is tight.
- **Accurate but imprecise** — the average is right, but no single reading lands close to it.
- **Inaccurate but precise** — the readings agree with each other, but they all agree on the *wrong* answer. Often the most dangerous case, because the agreement *looks* like quality.
- **Inaccurate and imprecise** — junk.

### The canonical dartboard analogy

Every Physics teacher draws this. Four targets, each with five "shot" markers:

![[accuracy-vs-precision-dartboard.svg]]

The bullseye is the true value; the shots are the measurements. **Accuracy** is "how close to the bullseye?" **Precision** is "how tightly grouped?" The two axes are independent — you can have one without the other, both, or neither.

### 中文锚点

中文物理教材通常将这两个概念翻译为：

| English | 中文 | 含义 |
|---|---|---|
| Accuracy (accurate) | 准确度 (准确) | 测量值与真值的接近程度 |
| Precision (precise) | 精确度 (精确) / 精密度 | 重复测量值之间的接近程度 |
| Systematic error | 系统误差 (xìtǒng wùchā) | 总是偏向一侧的偏差 — 影响**准确度** |
| Random error | 随机误差 (suíjī wùchā) | 测量间无规律的散布 — 影响**精确度** |
| True value | 真值 (zhēnzhí) | 我们想测出的"那个数" |
| Bias | 偏倚 / 系统偏差 | 系统误差的总和 — 平均值与真值的固定差距 |
| Calibration | 校准 (xiàozhǔn) | 修正系统误差 — 用已知标准重新对零 |
| Zero error | 零点误差 (língdiǎn wùchā) | 仪器未受外力时不读零 — 典型系统误差 |
| Parallax | 视差 (shìchā) | 读数时视线与刻度不垂直 |

A note on Chinese terminology: 精确度 and 精密度 (jīngmìdù) are used interchangeably in school physics for "precision." University texts sometimes distinguish them (精密度 = repeatability under identical conditions; 精确度 = a looser combined notion). Cambridge / IB / AP all use one word: *precision*.

> [!warning] The everyday-English trap
> In casual English, "accurate" and "precise" are nearly synonymous — "an accurate watch" usually means "a precise watch that also keeps the right time." In Physics, **the words are technical** and **independent**, exactly as 准确 vs 精确 are kept distinct in Chinese 物理教科书. Don't import the everyday looseness.

---

## Two sources of error, two repairs

The accuracy/precision split mirrors a deeper split in *where the error came from* and *what you do about it*. Every uncertainty in a measurement has both a **systematic** component (which damages accuracy) and a **random** component (which damages precision). The two are reduced by completely different techniques.

### Systematic error — the persistent offset

A **systematic error** (系统误差) is one that affects every reading in the same way. The measurement is biased: shifted by some fixed amount, or always too high / too low by a fixed *fraction*, regardless of how many times you repeat.

**Canonical sources:**

- **Zero error / offset.** A balance reads $0.04~\text{g}$ when nothing is on it; every reading is then $0.04~\text{g}$ too high. A voltmeter's needle doesn't return to zero after a measurement. A digital pH meter that hasn't been calibrated since last semester reads $7.2$ in pure water.
- **Calibration error.** The instrument's scale is mis-marked. Every value is then *proportionally* off — e.g. the ruler was printed at $98\%$ of true scale, so all lengths come out $2\%$ low. This is a "slope" error rather than an "offset" error, but it is systematic in the same sense.
- **Parallax (one form of it).** When you consistently read a scale from above rather than directly in front, you consistently get the same biased number.
- **Reaction-time bias in timing.** If you always start your stopwatch a bit *late*, every reading is consistently short. If you start late and stop early, the bias is even larger.
- **Environmental drift in the same direction.** Resistance measurements taken on a hot afternoon are systematically lower than the standard $20^\circ\text{C}$ values, because the resistor's temperature coefficient is positive.

![[systematic-error-sources.png]]
*Five faces of the same underlying property. The balance reads non-zero with nothing on it; the ruler disagrees with a known standard; the pencil's length depends on viewing angle; the stopwatch press is always a moment late; the resistor's value drifts in the heat of the lamp. Surface details differ; the structural failure is identical — and in every case, **averaging does not help.***

**The defining feature:** *averaging does not help.* If you take 100 readings and the zero error is $+0.04~\text{g}$, your mean is *also* $+0.04~\text{g}$ high. The bias is in every single reading, so it survives the mean.

**The fix:** **calibration.** Find a known standard (a $100.0~\text{g}$ calibration mass; an ice-water bath at $0^\circ\text{C}$; a known voltage source) and measure it with your instrument. The discrepancy tells you the systematic error; subtract it from every subsequent reading. For a slope error, calibrate at two or more known points and fit a correction.

> [!tip] Why a zero check is the first thing you do
> Every careful experimentalist, before recording any data, takes a reading with the instrument's input *set to zero*. Balance with nothing on the pan: should read $0.00~\text{g}$. Voltmeter shorted across its own terminals: should read $0~\text{V}$. Stopwatch unstarted: ditto. Any nonzero reading is the **zero error**, and you either subtract it from every later measurement or you re-zero the instrument before continuing. This is the cheapest way to defeat the most common systematic error in any school lab.

### Random error — the irreducible spread

A **random error** (随机误差) is one that varies unpredictably from reading to reading, sometimes high and sometimes low, with no consistent direction.

**Canonical sources:**

- **Reading-the-last-digit estimation.** Vernier calipers' last vernier mark, a ruler's nearest half-millimetre, a thermometer's nearest $0.5^\circ\text{C}$ — the experimenter is *estimating* in the gap between scale marks and that estimate is noisy.
- **Reaction time spread.** Even after you've calibrated out your average reaction-time *bias*, the timing of an event still varies trial-to-trial by $\pm 0.1$–$0.2~\text{s}$ at human-finger speed.
- **Environmental jitter.** Small unpredictable air currents perturbing a pendulum; voltage fluctuations on the mains; tiny temperature drifts during a long measurement.
- **Genuine physical fluctuation.** A radioactive count rate, the brightness of an LED, the count of bubbles per second in an electrolysis cell — many real Physics quantities are *intrinsically* noisy because the underlying process is statistical (Poisson, Brownian, thermal).

> [!tip] Try it — the "perfect 1 second" challenge
> Open the stopwatch on your phone. Start it, then try to stop it at *exactly* $1.00$ seconds. Do this ten times in a row and write down each result.
>
> You will not hit $1.00$ every time. Your readings will scatter somewhere around it — probably between about $0.85$ and $1.15$ seconds, with some high and some low and no pattern as to which way the next one will go.
>
> That spread *is* random error, made by your own fingers in real time. Three things to notice:
>
> - The **scatter** of your ten readings is your reaction-time noise — the random component of every timing measurement you will ever take by hand.
> - The **mean** of the ten readings is much closer to $1.00~\text{s}$ than any single attempt was. Averaging ate the noise.
> - The mean is still not exactly $1.00$ — only as close as $\sigma / \sqrt{10}$, where $\sigma$ is your per-attempt spread (see [[Repeated Measurements]] for the $\sqrt{N}$ derivation).
>
> No instrument, no calibration, no environment — *you* are the source of the noise, and you cannot make yourself stop being noisy. You can only outvote yourself by averaging.

![[random-error-sources.png]]
*Four faces of noise. Estimating between scale marks, finger-pressing a stopwatch, a pendulum stirred by stray air currents, a radioactive count rate that refuses to sit still — the surface details differ but the structural property is the same: each reading lands in a slightly different place from the last, with **no preferred direction**. And that is exactly why averaging $N$ readings shrinks the noise by $\sqrt{N}$.*

**The defining feature:** *averaging helps.* If you take $N$ independent readings, the mean has a standard error of $\sigma / \sqrt{N}$ where $\sigma$ is the per-reading spread. Quadrupling the number of readings *halves* the random uncertainty in the mean. (See [[Repeated Measurements]] for the proof — it follows from the central limit theorem applied to the sum of independent random samples.)

**The fix:** **average more readings.** Cannot remove the per-reading noise from any single measurement, but can shrink the noise in the *mean* by sampling more often. The price is your lab time.

### The two-axis picture

| | Low random (precise) | High random (imprecise) |
|---|---|---|
| **Low systematic (accurate)** | gold standard | average is right; readings noisy |
| **High systematic (inaccurate)** | bias hides as quality | both kinds of failure |

This is exactly the dartboard above, but with the source-of-error names attached. The "shot scatter" measures random error; the "displacement of the cluster centre from the bullseye" measures systematic error.

> [!info] Beyond syllabus — total uncertainty
> When both are present, the **total uncertainty** in a single reading is roughly $\sigma_{\text{tot}} \approx \sqrt{\sigma_{\text{sys}}^2 + \sigma_{\text{rand}}^2}$ — the in-quadrature combination of the two. This already foreshadows the quadrature convention discussed in [[Error Propagation]] §"Two conventions for combining errors": independent error sources combine in quadrature, not by direct addition. For school-level work, just report random uncertainty (from your scatter) and *separately* note the systematic source you couldn't get rid of, rather than trying to combine them into one number.

---

## A worked diagnosis

Real lab data rarely arrives labelled "systematic" or "random." You have to read the symptoms and work backwards.

> A class measures the spring constant $k$ of an identical spring using $F = kx$. Eight pairs of students each take five readings of extension at a fixed load and report a mean and a spread. The results:

| Pair | Mean $k$ (N/m) | Spread (N/m) |
|---|---|---|
| 1 | $48.2$ | $\pm 0.3$ |
| 2 | $48.5$ | $\pm 0.4$ |
| 3 | $48.1$ | $\pm 0.2$ |
| 4 | $47.9$ | $\pm 0.3$ |
| 5 | $48.4$ | $\pm 0.3$ |
| 6 | $48.0$ | $\pm 0.4$ |
| 7 | $48.3$ | $\pm 0.3$ |
| 8 | $48.2$ | $\pm 0.4$ |

The manufacturer's quoted spring constant is $\;\boxed{50.0~\text{N/m}}\;$.

**Diagnosis.** The eight pairs *agree with each other* — they cluster between $47.9$ and $48.5$, a spread of $0.6~\text{N/m}$, and their internal per-pair spreads are similar at $\pm 0.3$–$0.4$. **High precision, both within each pair and across pairs.** But the class average is around $48.2~\text{N/m}$, which is $1.8~\text{N/m}$ low — *every single pair* is below the quoted value. **Low accuracy.**

The pattern — precise, biased low — points to **systematic error**, not random. Asking "where could the bias come from?" yields concrete candidates:

- The load weights might be lighter than labelled (a $1.00~\text{kg}$ mass that is actually $0.96~\text{kg}$ gives $k$ values about $4\%$ low).
- The ruler used to measure extension might be misaligned (parallax bias from the experiment design).
- The spring might be near its elastic limit at this load — see [[Stress, Strain and Young Modulus]] — making the apparent $k$ artificially low because the response is becoming nonlinear.
- The manufacturer's quoted value might itself be wrong for the population of springs shipped (don't rule it out — calibration disputes are real).

**Recipe to fix.** Average the eight pairs' readings together: the random part shrinks (now $\sigma / \sqrt{N \times \text{pairs}}$, perhaps $\pm 0.1~\text{N/m}$), but the mean *stays* at $48.2$ — confirming the gap is not random. Then **calibrate**: weigh one of the load masses on a known-good balance, check the ruler against a metre standard, replace the spring with a fresh one. Each calibration step targets a specific systematic candidate.

This is what *the accuracy/precision factorisation buys you.* "There's an error" is a guess; "there's a precise but inaccurate measurement" is a diagnosis with a treatment plan.

---

## Common misconceptions

### 1. "More decimal places means more accurate"

**The mistake:** A student writes $g = 9.81245~\text{m s}^{-2}$ from a calculator display and considers it "more accurate" than $g = 9.8~\text{m s}^{-2}$.

**Why it's wrong:** Decimal places encode **precision** of the *recording*, not accuracy of the *measurement*. If the measurement was made with a $\pm 0.1~\text{m s}^{-2}$ instrument, then $9.81245$ is just $9.8$ with four nonsense digits attached — *not* a better answer. Writing four extra digits implies you measured to four extra decimals, which is a false claim about your apparatus.

**Fix:** Always round the final answer to match the precision of your uncertainty. If $\Delta g = 0.1$, then $g = 9.8 \pm 0.1$ (not $9.81245 \pm 0.1$). See [[Significant Figures]] for the rounding rules — the central one is "the uncertainty governs the digits you are allowed to print."

### 2. "Accuracy and precision are the same thing"

**The mistake:** Using the words interchangeably; describing a precise-but-biased measurement as "accurate" because it has tight scatter; or interpreting "high precision" as "true value."

**Why it's wrong:** They are independent axes — the dartboard makes this visible. A precise inaccurate measurement is the most dangerous failure mode in experimental physics because the tight scatter masquerades as quality control: "look how reproducible we are!" — while the cluster sits a finger-width to the left of the bullseye.

**Fix:** Insist on *two numbers* when reporting a measurement: the mean (with uncertainty from scatter, addressing precision) *and* a comment about any unaddressed systematic source (addressing accuracy). "$T = 100.1 \pm 0.2~^\circ\text{C}$, no calibration correction applied" is a complete report; "$T = 100.1~^\circ\text{C}$" alone is not.

### 3. "Averaging fixes everything"

**The mistake:** "The reading was noisy, so I took 100 measurements and averaged. Now my answer is much more accurate."

**Why it's wrong:** Averaging reduces *random* error by a factor of $\sqrt{N}$. It does **nothing** to systematic error — every reading carries the same bias, so the mean carries the bias too. Take 100 readings on an instrument with a $+5\%$ calibration error and the mean is *also* $+5\%$ off, no matter how many readings you took.

**Fix:** Teach the diagnosis loop. Before averaging more, ask "what would averaging fix, and what would it not?" If the suspect is systematic (calibration, zero error, persistent parallax), no amount of averaging helps — you must calibrate or change apparatus.

### 4. "Precision is whatever the instrument's spec sheet says"

**The mistake:** "The vernier calipers are $\pm 0.02~\text{mm}$, so my measurement is precise to $0.02~\text{mm}$." A common companion mistake: assuming the manufacturer's quoted *resolution* is the same as the *uncertainty* in your reading.

**Why it's wrong:** The spec sheet gives a *best case* — assuming a perfectly steady hand, no parallax, no thermal expansion, no operator estimation. Your *actual* precision is whatever the **scatter of your own repeated readings** says it is. Five readings spanning $0.4~\text{mm}$ have $\pm 0.2~\text{mm}$ precision regardless of the instrument's spec being $\pm 0.02~\text{mm}$. The gap between the two is "operator + setup precision," and it usually dominates the instrument precision in school labs.

**Fix:** Always do at least 3–5 repeats and let the scatter of *your* readings define *your* precision. Quote the instrument resolution only as a sanity check: your scatter should never be *smaller* than the instrument resolution, but it is usually larger.

---

## Exam Notes

### Cambridge 9702 (A-Level Physics)

§1.3 (AS Level). Examined alongside [[Error Propagation]] every session. Standard question shapes:

- MCQ: classify a described error as systematic or random. ("A student starts a stopwatch slightly after releasing a falling ball each time and notes the time taken. Is this a random or systematic error?")
- Structured rider: given a graph of repeated readings, identify which point(s) are outliers, comment on whether the scatter suggests systematic or random error.
- P5 (Planning & Analysis): the "improvements" question — "suggest two changes to the procedure that would reduce systematic error and two that would reduce random error." Expects four distinct suggestions, each correctly classified.

The mark scheme is unforgiving of swapping the two terms — get "calibrate to remove random error" wrong and you lose the mark. Drill the asymmetry: **calibrate → systematic; average → random.**

### IB Physics (2025 syllabus)

Tools 1: PRAC.2 — explicitly named in the syllabus as "uncertainty types (random vs systematic); precision vs accuracy." Tested via:
- Paper 1B data analysis: identify which feature of a graph (scatter vs offset) corresponds to which error type.
- Internal Assessment (Scientific Investigation): the IA criterion *Evaluation* specifically asks for systematic error analysis — students who report only random scatter and ignore systematic bias lose marks here.

IB markers reward language like "the consistent offset from the accepted value suggests systematic error, possibly due to ___, which could be reduced by ___." Pattern is: identify offset → name systematic candidate → propose calibration step.

### AP Physics 1 / 2

Science Practice 1 (Modelling and Representations) + SP 3 (Argumentation). Distributed through the lab requirement (≥25% of instructional time). FRQ 3 (Experimental Design and Analysis) regularly asks:
- "Identify and explain one source of *systematic* error in the experiment."
- "How would you modify the procedure to reduce *random* error?"

AP rubrics explicitly award the systematic-vs-random distinction. Confusing them costs the entire sub-question's mark.

### Cambridge 0625 (IGCSE Physics)

This is **practical-paper** material — Paper 5 or Paper 6 — not one of the six numbered topics. 0625 supplies its own definitions and expects them used consistently through the course, though the wording itself is never asked for: a result is **accurate** if it is close to the true value, **precise** if repeated values are close to *each other*, and the **measurement error** is the gap between a measured value and the true value. The examinable moves built on that are recognising an **anomaly** — a result outside the general pattern — and taking appropriate action, and judging whether two results agree, where 0625 fixes the limit of experimental accuracy at **±10%**. Sources of error are named as *measurement, random and systematic*; the dartboard picture below is the fastest way to hold the random/systematic split.

---

## Connections

- **Parent:** [[Upper and Lower Bounds]] — the IGCSE bookkeeping for "how big could the true value be, given what we wrote down" is the algebra-side cousin of the systematic-error correction.
- **Sibling:** [[Error Propagation]] — once accuracy and precision are sorted, error propagation is what you do with the *random* part: the rules for combining percentage uncertainties downstream of arithmetic.
- **Component:** [[Repeated Measurements]] — the $\sigma / \sqrt{N}$ averaging mechanism that *reduces* random error. Companion theorem to this card.
- **Component:** [[Calibration of Instruments]] — the procedural mechanism that *reduces* systematic error.
- **Application:** [[Significant Figures]] — the rule "round the value to match the precision of the uncertainty" depends on knowing what your precision *is*. Significant figures are a coarse encoding of precision; the full uncertainty is the fine version.
- **Application — Stats bridge:** [[Standard Deviation]] — the formal way to *quantify* random spread, taking the dartboard's "tight cluster vs loose cluster" eyeball judgment and replacing it with a number ($\sigma$).
- **Cross-domain (Maths):** [[Mean and Variance]] — the per-reading random error is the random variable; its mean is the bias (systematic), its standard deviation is the precision (random).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\sigma$ | `\sigma` | Standard deviation — the formal measure of precision. |
| $\sigma / \sqrt{N}$ | `\sigma / \sqrt{N}` | Standard error of the mean. Random uncertainty after averaging $N$ readings. |
| $\Delta x$ | `\Delta x` | Absolute uncertainty in $x$ — usually quoted as the random spread $\pm \Delta x$. |
| $\bar{x}$ | `\bar{x}` | Mean of repeated readings. |
| $x_{\text{true}}$ | `x_{\text{true}}` | True value — for measuring accuracy. |
| $^\circ\text{C}$ | `^\circ\text{C}` | Degree Celsius. The degree symbol uses `^\circ`, not `\degree` (which is undefined in school-level LaTeX). |
