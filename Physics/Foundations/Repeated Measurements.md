---
chinese: 重复测量 (chóngfù cèliáng)
prerequisites:
  - "[[Accuracy vs Precision]]"
  - "[[Error Propagation]]"
  - "[[Physical Quantities and Units]]"
  - "[[Normal Distribution]]"
  - "[[Discrete Random Variables]]"
leads_to:
  - "[[Calibration of Instruments]]"
  - "[[Stories/The 1919 Eclipse]]"
teach_together:
  - "[[Significant Figures]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/experimental-physics
  - domain/measurement
  - domain/statistics
  - domain/foundations
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
  - syllabus/0625-1-1
  - syllabus/0625-P4
  - syllabus/0625-P7
  - syllabus/IB-Physics-PRAC-2
  - syllabus/AP-Physics-1-SP-1
  - type/deep
  - type/theorem
  - notation/standard-error
  - misconception/averaging-removes-systematic
  - misconception/doubling-N-halves-uncertainty
  - misconception/timing-N-oscillations-is-the-same-as-averaging
---

# Repeated Measurements 重复测量

## Hunter trace — Galton at Plymouth Fair, 1906

In the autumn of 1906, the polymath **Francis Galton** wandered around an English country fair in Plymouth and stopped at a stall where the prize was an ox. For sixpence, anyone could buy a numbered ticket and write down their best guess at the weight of the ox (dressed and slaughtered, as it would be sold to a butcher). At the end of the fair, 800 tickets had been bought; the closest guess won.

Galton — who was 84, deeply suspicious of crowds, and quietly hostile to democratic intuitions — collected the 800 tickets after the contest closed and analysed them. The actual dressed weight of the ox was **1198 lb**. The *individual* guesses ranged wildly from the absurdly low (a few hundred pounds, from people who had clearly never seen a cow) to the absurdly high (several thousand pounds, from optimists). Any single guess, picked at random, was almost certainly wrong.

But **the median of the 800 guesses was 1207 lb** — within 0.8% of the truth. And the *mean* (Galton later recomputed it more carefully) was **1197 lb**, within 0.1%.

Galton was so surprised that he wrote it up for *Nature* — "*Vox Populi*," published 7 March 1907. The conclusion, in his words: *"The result seems more creditable to the trustworthiness of a democratic judgment than might have been expected."* No individual butcher, no expert farmer, was that accurate. *The crowd, mechanically averaged, was.*

Why does it work? *Because if individual errors are random and roughly symmetric around the true value, they cancel out as you add more of them.* Some people guess too high, some too low, and the further you go from the truth the rarer the guess. Add up 800 independent errors with mean zero, divide by 800, and the mean error of the average is **smaller than any individual error by a factor of $\sqrt{N} = \sqrt{800} \approx 28$**.

This card is about that factor of $\sqrt{N}$. It applies to a country-fair contest, an opinion poll, a school pendulum experiment, and the photographic plates that confirmed general relativity in 1919. **The same mathematics governs all of them.** Once you have it, "should I take another measurement?" becomes a calculable trade rather than a guess.

## Definition

The **standard error of the mean** (often *SEM* or *standard error*) is the spread you should expect in the *average* of $N$ independent measurements, given the spread $\sigma$ of each individual measurement:

$$\boxed{\;\;\mathrm{SEM} \;=\; \dfrac{\sigma}{\sqrt{N}}\;\;}$$

In words: averaging $N$ independent readings of the same quantity divides the random uncertainty by $\sqrt{N}$. This is not a useful rule of thumb — it is *exact* (in the limit of large $N$, by the Central Limit Theorem; almost-exact even for modest $N$).

The formula has three things every Foundations student should hold:

1. **The numerator is $\sigma$, not $|\text{error}|$.** $\sigma$ is the *spread* of single readings — the standard deviation of the underlying random-error distribution. You typically estimate it by computing the standard deviation of your readings themselves (see [[Discrete Random Variables]] §"Variance and standard deviation" for the formula).
2. **The denominator is $\sqrt{N}$, not $N$.** This is the part that surprises every student. Averaging is *not* free precision — you need quadratically more data to halve your uncertainty.
3. **"Independent" is doing real work.** If your measurements are correlated — taken with the same systematically miscalibrated instrument, or by the same biased observer — averaging does *not* divide the error by $\sqrt{N}$. Independence is the load-bearing assumption, and it is more often violated than students notice. See [[Stories/The 1919 Eclipse]] §"Throwing out data" for what happens when independence fails (the Sobral astrographic plates were correlated by a shared focus-drift, so averaging them with the good plates would have *contaminated* the result rather than improving it).

### 中文锚点

**重复测量** (chóngfù cèliáng) = repeated measurements. 物理实验中最古老、最朴素也最强大的降噪手段：**多测几次，取平均**。

| English | 中文 | 含义 |
|---|---|---|
| Repeated measurements | 重复测量 (chóngfù cèliáng) | 多次独立测量同一个量 |
| Mean / average | 平均值 (píngjūn zhí) | 多次测量的算术平均 |
| Standard deviation | 标准差 (biāozhǔn chà) — $\sigma$ | 单次测量的散布程度 |
| Standard error of the mean | 平均值的标准误 (píngjūn zhí de biāozhǔn wù) | 平均值本身的不确定度，$\sigma/\sqrt{N}$ |
| Independent | 独立的 (dúlì de) | 测量之间没有共同的偏差源 |
| Central Limit Theorem | 中心极限定理 (zhōngxīn jíxiàn dìnglǐ) | 独立同分布变量之和趋近正态分布 |
| Diminishing returns | 边际递减 (biānjì dìjiǎn) | 多测一倍数据，精度只提高 $\sqrt{2}$ 倍 |

**核心公式**: 平均值的不确定度 = 单次测量的不确定度 / $\sqrt{N}$。

**核心警告**: 这只能消除 **随机误差** (random error)，对 **系统误差** (systematic error) 完全没用。系统偏差在平均后还在那里 — 无论你测多少次。这点见 [[Accuracy vs Precision]] §"Misconception 3 — averaging removes systematic error."

## Proof — variance additivity gives the $\sqrt{N}$ law

The SEM formula is *exact*, not asymptotic. The proof is three lines of algebra plus one theorem (variance additivity under independence), and it lives here in full — the formula does **not** need the Central Limit Theorem.

Let $X_1, X_2, \dots, X_N$ be independent random variables, each with mean $\mu$ (the *true value* we want to measure) and variance $\sigma^2$ (the spread of any single reading). Define the sample mean:

$$\bar X \;=\; \dfrac{1}{N}\sum_{i=1}^N X_i$$

**Step 1 — the mean of $\bar X$ is $\mu$ (averaging is unbiased).** By linearity of expectation:

$$E(\bar X) \;=\; \dfrac{1}{N}\sum E(X_i) \;=\; \dfrac{1}{N}\cdot N\mu \;=\; \mu$$

So averaging doesn't shift the result; it only sharpens it.

**Step 2 — the variance of $\bar X$ is $\sigma^2/N$.** Apply $\operatorname{Var}(cX) = c^2 \operatorname{Var}(X)$ for the scalar $1/N$, then variance additivity for the sum of independents:

$$\operatorname{Var}(\bar X) \;=\; \operatorname{Var}\!\left(\dfrac{1}{N}\sum X_i\right) \;=\; \dfrac{1}{N^2}\operatorname{Var}\!\left(\sum X_i\right) \;=\; \dfrac{1}{N^2}\cdot N\sigma^2 \;=\; \dfrac{\sigma^2}{N}$$

The middle equality is the load-bearing one: **the variance of a sum of independent variables is the sum of variances**. We do *not* take this on faith — it is itself a one-line consequence of the covariance identity. For any two random variables $X, Y$:

$$\operatorname{Var}(X+Y) \;=\; \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y)$$

When $X$ and $Y$ are independent, $\operatorname{Cov}(X, Y) = 0$ (the joint expectation factors), so $\operatorname{Var}(X+Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ exactly. Apply this inductively to $N$ independent terms; each has variance $\sigma^2$; the sum has variance $N\sigma^2$.

**Step 3 — take the square root.** Standard deviation is the square root of variance, so:

$$\boxed{\;\;\sigma_{\bar X} \;=\; \sqrt{\operatorname{Var}(\bar X)} \;=\; \dfrac{\sigma}{\sqrt{N}}\;\;}$$

**This is the formal proof of the SEM formula.** Three lines, valid at *any* $N$ (not just large $N$), conditional only on independence and finite variance. The $\sqrt{N}$ comes out of taking the square root of a variance that scaled as $1/N$. If you forget the formula but remember "variance adds, divide by $N^2$, square-root," you can re-derive it on the spot.

### What the CLT adds — and what it doesn't

The proof above gives you the *standard deviation* of $\bar X$. The **Central Limit Theorem** gives you something stronger and different: the *distribution shape* of $\bar X$. Specifically:

- *This card's proof:* $\sigma_{\bar X} = \sigma/\sqrt{N}$. Exact at all $N \geq 1$. No assumption about distribution shape.
- *CLT:* as $N \to \infty$, the *standardised* $(\bar X - \mu)/(\sigma/\sqrt{N})$ converges in distribution to $N(0, 1)$. The full distribution becomes approximately normal regardless of the per-reading distribution.

You need the CLT when you want to compute *probabilities* about $\bar X$ — confidence intervals, hypothesis tests, "the probability the mean is within $2$ SEM of $\mu$." You do *not* need the CLT for the SEM formula itself. The card's proof is complete; the CLT is the related-but-stronger theorem on the next floor up.

The CLT statement (Lindeberg–Lévy form) lives at [[Normal Distribution]] §"Central Limit Theorem (the why)" with a meta-callout noting that the formal proof uses characteristic functions, Lévy's continuity theorem, and a Taylor expansion of $\varphi(t)$ around $t = 0$ — beautiful but requiring measure-theoretic probability and Fourier theory, so it's deferred to graduate texts (Billingsley's *Probability and Measure*, Durrett's *Probability: Theory and Examples*). The CLT proof is *not* in this vault. The SEM proof, above, is.

> [!info] Beyond syllabus — averaging and error propagation are the same theorem
> The covariance identity $\operatorname{Var}(X+Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y)$ underwrites *both* this card's proof and the addition-in-quadrature rule from [[Error Propagation]] §"Rule 1 — sums and differences." Errors that are independent add via $\sigma_z^2 = \sigma_x^2 + \sigma_y^2$ rather than $\sigma_z = \sigma_x + \sigma_y$ — same identity, same independence assumption. **Repeated-measurements averaging and error propagation are the same mathematical principle, applied in opposite directions** — propagation grows variance through a calculation; averaging shrinks variance by stacking samples. Both are downstream of $\operatorname{Var}(X+Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ under independence.

## Visualisation — diminishing returns

The $\sqrt{N}$ relationship is *much* less rewarding than students hope. Each additional measurement helps, but it helps by less than the one before:

![[repeated-measurements-sem-curve.svg]]

*The SEM as a fraction of the per-reading $\sigma$, plotted against $N$. Quadrupling the number of measurements only halves the uncertainty. Going from $N=4$ to $N=400$ takes **a hundred times more measurements** for **a ten times improvement** in uncertainty. There is a practical floor below which doing more measurements is just not worth the time.*

The key numbers to internalise:

| $N$ | $\mathrm{SEM}/\sigma$ | Cost / benefit |
|---|---|---|
| 1 | 100% | one reading — baseline |
| 4 | 50% | 4× the data, 2× the precision — fair trade |
| 25 | 20% | 25× the data, 5× the precision — clearly diminishing |
| 100 | 10% | starting to feel pointless if $\sigma$ is large |
| 400 | 5% | nearly always wasted in a school lab |
| 10,000 | 1% | the regime where Eddington's plate stacking lived |

**The practical rule:** in school physics, 5 to 10 measurements is usually the sweet spot. Going from $N=1$ to $N=5$ cuts the SEM by more than half; going from $N=5$ to $N=10$ cuts it by another 30%; going from $N=10$ to $N=20$ buys you another 30% but doubles the time spent. **Twenty is rarely worth it; a hundred almost never is** — at that point any *systematic* error in your apparatus dominates whatever's left of the random part, and no amount of averaging will help.

## The systematic-error trap

The single most important thing to remember about repeated measurements is that **they only fix random error**. If your ruler is mis-printed by 1 mm everywhere, taking 1000 readings with that ruler gives you a *very precisely known* mismeasurement. The mean of your 1000 readings will be off by 1 mm, just as a single reading was off by 1 mm. The SEM of that mean will be tiny — perhaps $0.03~\text{mm}$ — but the *accuracy* is still terrible.

This is exactly the diagnostic from [[Accuracy vs Precision]] §"Misconception 3 — averaging removes systematic error." The dartboard analogy says the same thing visually: averaging tightens the cluster (precision improves) but does *not* move the cluster's centre toward the bullseye (accuracy is unaffected). **Calibration ≠ averaging**, and they target orthogonal axes of uncertainty.

> [!warning] The Eddington test
> Before you average a set of readings, ask: *are these readings correlated through a shared error source?* If yes, you are not gaining $\sqrt{N}$ improvement; you may be gaining nothing, or even *making it worse*. The 1919 eclipse Sobral astrographic plates were a textbook example: 19 plates, all taken through the same telescope tube which was thermally distorting during totality. Averaging the 19 plates would have given you a very precise number with a built-in systematic offset. Eddington's correct move was to **exclude** them on the grounds that their errors were not independent of one another. See [[Stories/The 1919 Eclipse]] §"Throwing out data" for the full story.

## Two techniques students confuse

Real lab work uses two related but mathematically distinct techniques. Students routinely conflate them; teachers rarely flag the difference.

### Technique 1 — Average $N$ independent measurements

The technique this card is about. Take $N$ separate measurements of the same quantity, compute the mean, report $\sigma/\sqrt{N}$ as the uncertainty in the mean.

*Use when:* the random error is per-reading (reaction time when starting/stopping a stopwatch; reading a meter at the limit of its scale; visual judgement of a meniscus level).

### Technique 2 — Make ONE measurement over a longer interval

The technique a Cambridge 9702 student meets in the first practical lab when timing a pendulum. **Instead of timing one oscillation $N$ times, time $N$ oscillations once and divide by $N$.** This reduces the *fractional uncertainty* by a factor of $N$ — much better than $\sqrt{N}$. But you don't get $N$ independent measurements; you get *one* measurement of a long interval.

The mechanism is different. If your reaction-time uncertainty on the stopwatch is $\pm 0.2~\text{s}$, then:

- *Time 1 oscillation, repeated 10 times:* each reading is $T \pm 0.2~\text{s}$ where $T$ is the period. Mean is $T \pm 0.2/\sqrt{10}~\text{s} = T \pm 0.063~\text{s}$. **Improvement: $\sqrt{10} \approx 3.2$.**
- *Time 10 oscillations once:* reading is $10T \pm 0.2~\text{s}$. Divide by 10: $T \pm 0.02~\text{s}$. **Improvement: $10$.**

The longer-interval technique is *better by a factor of $\sqrt{N}$* for the same total experimental time. Why is it better? Because you've measured something the stopwatch can resolve more precisely (10 oscillations is a longer interval than 1 oscillation, so the same reaction-time uncertainty is a smaller *fraction* of it). You're not benefitting from averaging; you're benefitting from *measuring a larger denominator*.

This is why every 9702 practical paper that involves timing says *"time 10 oscillations and divide"*. It's exam-specific advice that hides a real piece of pedagogy: **if you can measure a quantity that's $N$ times larger and divide, you beat averaging by a factor of $\sqrt{N}$**. The catch is that this trick only works when the underlying quantity is *additive* over multiple repetitions — period works (every oscillation takes the same time), but a one-off length measurement does not (you can't measure "10 lengths" of the same object).

> [!tip] When you can use both
> In a really good practical, you do both. *Time 10 oscillations, repeat that measurement 5 times, average the 5 timings.* You gain a factor of 10 from the longer interval, and a factor of $\sqrt{5}$ from averaging — combined uncertainty $\sigma/(10\sqrt{5}) \approx \sigma/22$ for the cost of 50 oscillations total (about $50T$ seconds of lab time). This is the technique Cambridge mark schemes love to see and the technique that good lab partners use without anyone teaching it explicitly.

## Worked example — pendulum period in a school lab

A student measures the period of a simple pendulum (length $\ell = 1.00~\text{m}$, expected $T = 2\pi\sqrt{\ell/g} \approx 2.01~\text{s}$). Stopwatch reaction-time uncertainty per reading: $\sigma_{\text{reaction}} = 0.18~\text{s}$.

**Approach A — single-oscillation timings, repeated.** The student times one oscillation, then another, etc. Collects 10 readings:
$$2.05,\ 1.93,\ 2.18,\ 1.85,\ 2.02,\ 2.10,\ 1.96,\ 2.21,\ 1.88,\ 2.07~\text{s}$$
Mean: $\bar T_A = 2.025~\text{s}$. Standard deviation: $\sigma \approx 0.122~\text{s}$. SEM: $\sigma/\sqrt{10} = 0.039~\text{s}$. Report: $T_A = (2.03 \pm 0.04)~\text{s}$.

**Approach B — time 10 oscillations once.** Student times 10 full oscillations: reading is $20.15~\text{s}$, with uncertainty $\pm 0.18~\text{s}$ (single stopwatch action). Divide: $T_B = 20.15/10 = 2.015~\text{s}$, uncertainty $0.18/10 = 0.018~\text{s}$. Report: $T_B = (2.02 \pm 0.02)~\text{s}$.

**Approach C — time 10 oscillations, repeat 5 times.** Suppose readings are:
$$20.15,\ 20.20,\ 19.94,\ 20.05,\ 20.08~\text{s}$$
Mean: $20.084~\text{s}$. SD: $0.099~\text{s}$. SEM: $0.099/\sqrt{5} = 0.044~\text{s}$. Divide by 10: $T_C = (2.0084 \pm 0.0044)~\text{s}$. Report: $T = (2.008 \pm 0.004)~\text{s}$.

The progression — A (uncertainty $\pm 0.04~\text{s}$) → B (uncertainty $\pm 0.02~\text{s}$, half) → C (uncertainty $\pm 0.004~\text{s}$, an order of magnitude better) — shows the two techniques compounding. **Notice that even Approach C cannot fix a systematic bias in $g$, in the length measurement, or in the stopwatch's calibration. Random uncertainty has been crushed; systematic uncertainty is what remains.**

## Real-world anchor — Eddington's plate stacking, 1919

Sir Arthur Eddington photographed the same field of stars during totality at Príncipe on 29 May 1919, six times. (See [[Stories/The 1919 Eclipse]] for the full mission context.) Each plate had random noise from atmospheric scintillation, photographic-emulsion grain, focus drift, and plate-development variability. The *positional* uncertainty of a single star image on a single plate was roughly $\pm 0.3''$ — comparable to the predicted deflection itself.

By measuring star positions on all six plates and *averaging the position of each star*, Eddington reduced the per-star uncertainty by $\sqrt{6} \approx 2.4$. The deflection signal stayed; the random noise shrank. This is the SEM trick applied to imaging data, more than a century before the same technique would become standard in astrophotography software (any backyard astronomer in 2026 with a stack of long-exposure DSLR frames is running Eddington's procedure).

**The Sobral 4-inch lens contributed *seven* useful plates** — even higher $\sqrt{N}$ gain, and a tighter reported uncertainty ($\pm 0.18''$) as a result. The Sobral astrographic plates, by contrast, were *correlated* through their shared focus drift — Eddington correctly excluded them rather than averaging them in.

## Common Mistakes

### 1. "Doubling N halves the uncertainty"

A standard intuition error. $N \to 2N$ gives $\sqrt{2N} = \sqrt{2}\sqrt{N}$ — an improvement factor of $\sqrt{2} \approx 1.41$, *not* $2$. To halve the uncertainty, you need to **quadruple** $N$. Drilling this fixes the "I'll take twice as many measurements to be twice as accurate" misconception that ends every first-year lab in disappointment.

### 2. "Averaging fixes my zero error"

It does not. **No amount of averaging cures a systematic bias.** Zero error, calibration offset, parallax in a consistently-tilted observer's line of sight — all survive averaging untouched. If you suspect systematic error, *calibrate* (compare against a known standard, swap apparatus, swap observers); do not just take more readings. The dartboard analogy from [[Accuracy vs Precision]] makes the orthogonality visible: averaging tightens the cluster, calibration moves the cluster toward the bullseye, and they are independent operations.

### 3. "Timing $N$ oscillations is the same as averaging"

Mathematically distinct, as developed in the *Two techniques* section above. The longer-interval technique improves by $N$, not $\sqrt{N}$ — much better when applicable. Conflating them leads to over-reporting precision (claiming $\sqrt{10}$ improvement when you measured 10 oscillations and divided — you actually got $10$) or under-reporting (treating 10 independent readings as if they gave you the longer-interval benefit). Be explicit about which technique you used in your lab write-up.

### 4. "More data is always better"

Two limits make this false:
- *Below the systematic floor.* Once SEM drops below the systematic uncertainty in your apparatus, additional measurements buy you nothing — the result is dominated by bias.
- *Below the practical floor.* Lab time is finite. Going from $N=10$ to $N=100$ costs ten times the time for only $\sqrt{10} \approx 3.2\times$ improvement. The tradeoff usually favours *more diverse* measurements (different apparatus, different observers, different times of day) over *more identical* measurements (same setup, same observer, same hour).

### 5. "Independence is automatic"

Independence is the load-bearing assumption of the $\sqrt{N}$ law, and students rarely check it. Two readings taken back-to-back by the same fatigued observer using the same drifting apparatus are *not* independent. The 1919 Sobral astrographic disaster is the canonical case. When in doubt, *vary something* between readings (the observer, the apparatus alignment, the time of day) to break correlations.

## Exam Notes

### Cambridge 9702 (AS Level)

**Syllabus ref:** 1.3 — uncertainty propagation by addition of absolute/percentage uncertainties; the *taking and processing of measurements* expected throughout Paper 3 (Practical) and Paper 5 (Planning, Analysis, Evaluation).

What 9702 actually expects:
- **Practical Paper 3:** Always take *multiple* readings and report a mean; always *time 10 oscillations* (or 20, or 50) and divide rather than time one oscillation; quote uncertainty as the *spread of repeated readings* (often half-the-range as a quick approximation, $\sigma/\sqrt{N}$ in the more careful version).
- **Paper 5 (P5):** Explicitly tests *experimental design* — "describe the procedure" questions reward an answer that includes (a) repeat the measurement at least 5 times, (b) compute the mean, (c) compute the uncertainty as the range divided by 2 or as the standard error. Marks are *given* for naming this technique.
- **Common P5 question template:** "*describe how you would investigate the relationship between [X] and [Y]*". The mark scheme always includes a bullet for "*repeat each measurement and take the mean to reduce random uncertainty*" — worth one mark per practical question, and easy to miss if a student is rushing.

> [!tip] The 9702 half-range shortcut
> For small $N$ (typically $N \leq 5$), Cambridge papers accept the **half-range** approximation: uncertainty $\approx (X_{\max} - X_{\min})/2$. This is *not* the same as $\sigma/\sqrt{N}$ — it's an upper-bound rule of thumb — but it's the formula Cambridge mark schemes expect for low-$N$ practicals. For $N \geq 10$, $\sigma/\sqrt{N}$ becomes the correct quote.

### Cambridge 0625 (IGCSE Physics)

This card sits on both sides of 0625. **§1.1** asks for an average value for a *small distance* or a *short time interval* by measuring **multiples** — twenty swings of a pendulum timed together and divided by twenty, ten sheets of paper measured and divided by ten — which beats the ruler's or the reflex's resolution without any statistics at all. On the **practical papers** the same instinct is marked as *take sufficient observations to be reliable* and *repeat observations where appropriate*, alongside the term **repeatability**: the same result on repeating under the same conditions, same method, same experiment.

What is *not* on 0625 is the $\sigma/\sqrt{N}$ formula. Students are expected to take three readings of a length, time or temperature, compute the mean, and use it as the more reliable estimate. The jump to a formal standard error happens in AS year 1.

### IB Physics

**Theme A / PRAC.2** — uncertainty types, error propagation, repeated measurements. IB explicitly tests:
- *Half-range* as the standard uncertainty quote for small $N$ (same as Cambridge).
- For larger $N$, *standard deviation* of the readings, with $\sigma/\sqrt{N}$ as the SEM. (IB writes this as $u(\bar x) = \sigma/\sqrt{N}$ in the data booklet.)
- The Internal Assessment (20% of total grade) rewards explicit error analysis including the SEM derivation; markers look for a student who knows *why* they're dividing by $\sqrt{N}$, not just that they should.

### AP Physics 1 & 2

Science Practice 3 (Experimental Design and Analysis) explicitly tests:
- Selecting the right *number of trials* for a measurement (FRQ 3 frequently).
- Recognising that *more trials* reduce random but not systematic uncertainty.
- The $\sqrt{N}$ scaling is rarely tested in formula form but is expected as a *concept* in justifying experimental designs.

### A-Level (other boards)

Edexcel, AQA, OCR all expect: take multiple readings, compute mean, quote uncertainty as half-range (small $N$) or SEM (large $N$). The 9702 formal treatment is the gold standard; other boards converge on the same content with minor notation differences.

## Connections

- **Prerequisite:** [[Accuracy vs Precision]] — defines the random-vs-systematic factorisation that this card extends. Averaging is the mechanism that *acts on the random axis*; the systematic axis is invariant under averaging.
- **Prerequisite:** [[Error Propagation]] — variance additivity under independence is the shared engine. *Error propagation grows variance through a calculation; this card shrinks variance by stacking samples.* Two directions of the same principle.
- **Prerequisite:** [[Physical Quantities and Units]] — the SEM has the same units as the original measurement; the unit travels through averaging untouched.
- **Prerequisite:** [[Normal Distribution]] — the formal CLT statement, with full proof outline, lives there. This card uses the result without re-deriving.
- **Prerequisite:** [[Discrete Random Variables]] — defines mean and variance for individual measurements; the sample-mean variance derivation above re-uses that machinery.
- **Leads to:** [[Significant Figures]] — once SEM is known, the number of significant figures the final answer deserves is determined. *"Quote the mean to one more s.f. than the SEM"* is the practical rule.
- **Leads to:** [[Calibration of Instruments]] — what to do when averaging has hit the systematic floor.
- **Anchored by:** [[Stories/The 1919 Eclipse]] — Eddington's six-plate Príncipe averaging and the seven-plate Sobral 4-inch averaging are real-world SEM applications; the Sobral astrographic exclusion is the canonical "independence broke" case.
- **Sibling Foundations card:** the bay closure is one card away — [[Calibration of Instruments]] is the only remaining planned card.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\bar X$ | `\bar X` | Sample mean of $N$ readings |
| $\mu$ | `\mu` | True value (the population mean) |
| $\sigma$ | `\sigma` | Spread of a single reading (population standard deviation) |
| $\sigma_{\bar X}$ | `\sigma_{\bar X}` | Standard error of the mean — spread of $\bar X$ |
| $\sigma/\sqrt{N}$ | `\sigma/\sqrt{N}` | SEM formula |
| $\operatorname{Var}(X)$ | `\operatorname{Var}(X)` | Variance — the square of standard deviation |
| $E(X)$ | `E(X)` | Expected value of $X$ |
| $\operatorname{Cov}(X, Y)$ | `\operatorname{Cov}(X, Y)` | Covariance — zero for independent variables |
