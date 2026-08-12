---
chinese: 相对频率与期望频率 (xiāngduì pínlǜ yǔ qīwàng pínlǜ)
prerequisites:
  - "[[Probability Basics]]"
leads_to:
  - "[[Classifying Data]]"
  - "[[Statistical Charts]]"
tags:
  - subject/mathematics
  - domain/probability
  - domain/statistics
  - level/GCSE
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-S10
  - syllabus/9260-S11
  - syllabus/9260-S12
  - syllabus/9260-S13
  - syllabus/0580-E8-2
  - type/concept
  - misconception/relative-frequency-equals-probability
---

# Relative and Expected Frequency

## Definition

### Formal

**Relative frequency** of an event $A$ after $n$ trials:

$$\text{Relative frequency of } A = \dfrac{\text{number of times } A \text{ occurred}}{n}$$

**Expected frequency** of an event $A$ in $n$ trials:

$$\text{Expected frequency of } A = P(A) \times n$$

### Intuitive

Relative frequency answers: **"What fraction of the time did it actually happen?"** — it's probability estimated from real data.

Expected frequency answers: **"How many times should it happen?"** — it's the theoretical prediction for a given number of trials.

They approach each other as the number of trials grows. This is the bridge between theory and experiment.

> [!tip] Verify it yourself (Python)
> If you know some programming, you can simulate this in a few lines:
> ```python
> import random
> n = 10000
> heads = sum(random.choice([0, 1]) for _ in range(n))
> print(f"Relative frequency: {heads/n}")
> ```
> Run it a few times — you'll see the relative frequency hover close to 0.5, and get closer as you increase `n`.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| relative frequency | 相对频率 | xiāngduì pínlǜ |
| expected frequency | 期望频率 | qīwàng pínlǜ |
| experimental probability | 实验概率 | shíyàn gàilǜ |
| theoretical probability | 理论概率 | lǐlùn gàilǜ |
| trial | 试验 | shìyàn |
| fair | 公平的 | gōngpíng de |
| biased | 有偏的 | yǒupiān de |

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of trials |
| $P(A)$ | Theoretical probability of event $A$ |
| $\dfrac{f}{n}$ | Relative frequency — observed frequency $f$ out of $n$ trials |
| $P(A) \times n$ | Expected frequency — theoretical prediction |

---

## Key Facts / Properties

### Theoretical vs Experimental Probability

| | Theoretical probability | Experimental probability (relative frequency) |
|---|---|---|
| **How** | Calculated from reasoning about the situation | Calculated from data — actually doing the experiment |
| **Formula** | $P(A) = \dfrac{\text{favourable outcomes}}{\text{total equally likely outcomes}}$ | $P(A) \approx \dfrac{\text{times } A \text{ occurred}}{n}$ |
| **Requires** | A model where you can count or reason about outcomes | Real trials — no assumption about fairness needed |
| **Example** | $P(\text{heads}) = \dfrac{1}{2}$ for a fair coin | Flipped 200 times, got 112 heads → $\dfrac{112}{200} = 0.56$ |
| **Precision** | Exact | Estimate — improves with more trials |

> [!warning] "Equally likely outcomes" — be careful what you're counting
> A die with faces labelled 1, 2, 3, 3, 3, 6 is still **fair** — each face has the same $\dfrac{1}{6}$ chance of landing up. But the **results** are not equally likely: $P(3) = \dfrac{3}{6} = \dfrac{1}{2}$, while $P(1) = \dfrac{1}{6}$.
>
> The theoretical formula $P(A) = \dfrac{\text{favourable}}{\text{total}}$ counts **equally likely outcomes** — here, the 6 individual faces, not the 4 distinct numbers. This is a crucial difference from [[Set|set theory]], where $\{1, 2, 3, 6\}$ would be the set of possible results (4 elements) but says nothing about how likely each one is. In probability, each outcome can carry a different weight.

> [!info] When theoretical probability is impossible
> Some situations have no model to reason from at all. What is the probability that a drawing pin lands point-up? There's no symmetry argument — the only way to find out is to drop it many times and measure the relative frequency. Experimental probability is the **only** option when theory can't help.

### The Law of Large Numbers — Why More Trials Help

As the number of trials increases, the relative frequency gets closer to the true probability.

| Trials ($n$) | Heads | Relative frequency |
|---|---|---|
| 10 | 7 | 0.700 |
| 50 | 28 | 0.560 |
| 200 | 112 | 0.560 |
| 1000 | 513 | 0.513 |
| 10000 | 5021 | 0.502 |

The relative frequency **fluctuates** — especially with small $n$. But it **settles down** toward the theoretical value as $n$ grows. This is called the **law of large numbers**.

> [!info] Why does this happen?
> With a small number of trials, a few unusual results can dominate: 7 heads in 10 flips isn't that surprising. But with 10,000 trials, the unusual results get drowned out by the mass of typical results. The random "noise" averages out.
>
> This is not a guarantee — it's a tendency. You could theoretically flip 10,000 heads in a row. The probability of that is $\left(\dfrac{1}{2}\right)^{10000}$ — a number so small that no analogy can capture it. But "unimaginably unlikely" is not the same as "impossible." When you study astrophysics, you'll encounter the idea that the universe existing *at all* required an extraordinary chain of unlikely events. Mathematics gives us the tools to reason precisely about these extremes, even when our intuition fails.

### Expected Frequency

If you know the probability, you can predict how many times an event **should** happen:

$$\text{Expected frequency} = P(A) \times n$$

**Example:** A fair die is rolled 300 times. How many sixes do you expect?

$$\text{Expected sixes} = \dfrac{1}{6} \times 300 = 50$$

This does **not** mean you will get exactly 50 sixes. It means 50 is the **long-run average** — the number you'd get if the experiment were repeated many times and you averaged the results.

> [!warning] "Expected" doesn't mean "guaranteed"
> Expected frequency is a prediction, not a promise. In 300 rolls, getting 42 sixes or 58 sixes is perfectly normal. Getting 10 sixes or 100 sixes would be surprising and might suggest the die is biased.
>
> Why is it called "expected"? If you repeated the 300-roll experiment thousands of times and plotted how many sixes you got each time, you'd see a bell-shaped curve — a **normal distribution** — centred on 50. The expected value sits at the **peak** of that bell curve: it's the single most likely neighbourhood of outcomes. Values close to 50 are common; values far from 50 are rare. The further you go from the centre, the less likely the result. This is the beginning of the idea behind the **central limit theorem** — see AP / IB / A-Level notes below.

### Using Relative Frequency to Test Fairness

If the relative frequency is far from the theoretical probability, the object might be **biased**.

**Strategy:**

1. Calculate the theoretical probability (assuming fair)
2. Run the experiment many times
3. Calculate the relative frequency
4. Compare — if there's a large difference with a large sample size, suspect bias

**Example:** A coin is flipped 500 times and lands heads 312 times.

Relative frequency of heads: $\dfrac{312}{500} = 0.624$

Theoretical (if fair): $0.5$

The relative frequency is 0.624, noticeably above 0.5. With 500 trials, this is a large enough sample to suggest the coin is **biased** toward heads.

But if the coin were flipped only 10 times and got 7 heads (relative frequency 0.7), that's not strong evidence of bias — small samples produce noisy results.

### Repeated Experiments Give Different Results

Two students each flip the same fair coin 50 times. Student A gets 23 heads. Student B gets 28 heads. This is **expected** — randomness means each run of an experiment gives slightly different results.

The key insight: **variability decreases as sample size increases**. With 50 flips, outcomes can vary a lot. With 10,000 flips, both students would get relative frequencies very close to 0.5.

---

## Worked Examples

### Example 1: Relative frequency from data

A spinner is spun 80 times with these results:

| Colour | Red | Blue | Green | Yellow |
|--------|-----|------|-------|--------|
| Frequency | 24 | 18 | 22 | 16 |

(a) Find the relative frequency of landing on red.

$$\text{Relative frequency of red} = \dfrac{24}{80} = 0.3$$

(b) Is the spinner fair? A fair spinner with 4 equal sections would give $P(\text{each colour}) = 0.25$, so the expected frequency of each colour is $0.25 \times 80 = 20$.

| Colour | Observed | Expected (if fair) |
|--------|----------|-------------------|
| Red | 24 | 20 |
| Blue | 18 | 20 |
| Green | 22 | 20 |
| Yellow | 16 | 20 |

The differences are small (at most 4 away from 20). With only 80 trials, this variation is normal — **not enough evidence to say the spinner is biased**.

### Example 2: Expected frequency

The probability that a bus arrives late is 0.15. Over the next 60 days, how many days would you expect the bus to be late?

$$\text{Expected late days} = 0.15 \times 60 = 9$$

### Example 3: Estimating probability from relative frequency

A factory tests light bulbs. Out of 2000 bulbs tested, 34 are defective.

(a) Estimate the probability that a randomly chosen bulb is defective.

$$P(\text{defective}) \approx \dfrac{34}{2000} = 0.017$$

(b) The factory produces 50,000 bulbs. How many defective bulbs should they expect?

$$\text{Expected defective} = 0.017 \times 50{,}000 = 850$$

### Example 4: Comparing theoretical and experimental

A die is rolled 600 times. The results are:

| Score | 1 | 2 | 3 | 4 | 5 | 6 |
|-------|---|---|---|---|---|---|
| Frequency | 95 | 108 | 97 | 103 | 92 | 105 |

(a) What is the expected frequency of each score if the die is fair?

$$\dfrac{1}{6} \times 600 = 100$$

(b) Does the data suggest the die is biased?

The frequencies range from 92 to 108 — all within about 8 of the expected 100. For 600 trials, this variation is normal. **No strong evidence of bias.**

(c) If instead the 6 appeared 150 times:

$$\text{Relative frequency of 6} = \dfrac{150}{600} = 0.25$$

This is significantly higher than $\dfrac{1}{6} \approx 0.167$. With 600 trials, this would suggest the die **is biased** toward 6.

---

## Common Misconceptions

### 1. "The relative frequency IS the probability"

"I flipped a coin 10 times and got 7 heads, so $P(\text{heads}) = 0.7$." ✗

**Fix:** Relative frequency is an **estimate** of probability, not the probability itself. With 10 trials, the estimate is unreliable. The theoretical probability of heads for a fair coin is still $0.5$ — the experiment just happened to give an unusual result. With more trials, the relative frequency would settle closer to $0.5$.

### 2. The gambler's fallacy

"I've flipped 5 tails in a row, so the next flip must be heads." ✗

**Fix:** Each coin flip is **independent** — the coin has no memory. After 5 tails, $P(\text{heads on next flip})$ is still exactly $\dfrac{1}{2}$. The law of large numbers says the **overall proportion** approaches 0.5 over many trials — it does not say individual results will "balance out."

### 3. Small samples prove bias

"I rolled a die 12 times and got four 6s. The die must be loaded!" ✗

**Fix:** With only 12 trials, getting four 6s (relative frequency $\dfrac{4}{12} = 0.33$, vs expected $\dfrac{1}{6} \approx 0.17$) is unusual but not impossible. Small samples are **noisy**. You need many trials (hundreds or thousands) before you can confidently claim bias.

### 4. Expected frequency means exact frequency

"$P(\text{heads}) = 0.5$ and I flip 100 times, so I'll get exactly 50 heads." ✗

**Fix:** Expected frequency is a **long-run average**, not a guarantee for any single experiment. Getting 45 or 55 heads in 100 flips is perfectly normal. The expected value tells you what happens **on average across many experiments**, not what happens in one specific experiment.

### 5. Confusing frequency with relative frequency

Students sometimes give the frequency (count) when asked for relative frequency (proportion).

"The relative frequency of red is 24." ✗

**Fix:** Relative frequency is always a fraction or decimal between 0 and 1:

$$\text{Relative frequency} = \dfrac{f}{n} = \dfrac{24}{80} = 0.3$$

> [!info] Why science is designed the way it is
> Every misconception above — treating small samples as proof, expecting exact results, assuming the next outcome will "balance out" — is a mistake that humans naturally make. Scientific research methods were designed specifically to guard against these errors:
>
> - **Large sample sizes** combat the noise in small samples (misconception 3)
> - **Replication** (repeating experiments) checks that results aren't one-off flukes (misconception 1)
> - **Control groups** prevent us from confusing correlation with causation — see [[Conditional Probability#4. Assuming conditional probability means causation|conditional probability misconception 4]]
> - **Statistical significance testing** formalises "is this difference real or just random variation?"
>
> The entire framework of modern science — from clinical drug trials to particle physics — exists because probability is unintuitive and our brains are bad at it. Understanding these misconceptions doesn't just help with exams; it helps you think clearly about evidence in the real world.

---

## Exam Notes

### OxAQA 9260

- S10: estimate probabilities from equally likely outcomes (theoretical) or from relative frequency (experimental); calculate expected frequency
- S11: compare experimental data with theoretical probabilities — students should be able to say whether results are "consistent" with a fair model
- S12: understand that repeated experiments may give different outcomes — randomness produces variation
- S13: understand that increasing sample size generally leads to better estimates of probability
- Expect questions combining all four: "Here's data from 200 trials. Calculate the relative frequency. Is it consistent with a fair spinner? How would the estimate change with 2000 trials?"

### Cambridge 0580

- E8.2: estimate probabilities from relative frequency; calculate expected frequency from given probability
- Expect combined questions: calculate relative frequency from a table, then use it to predict future outcomes
- Both Paper 2 and Paper 4

### AP / IB / A-Level

- **AP Statistics:** law of large numbers formally stated; simulation and sampling distributions; the **central limit theorem** (CLT) — the sampling distribution of sample means is approximately normal for large $n$, regardless of the population shape
- **IB Mathematics AA HL:** CLT and its applications; confidence intervals; experimental vs theoretical probability with convergence
- **A-Level Further Mathematics (FS1):** CLT applied to approximate sample means from Geometric, Poisson, Binomial, and Negative Binomial distributions; chi-squared ($\chi^2$) test formalises the "is it biased?" question
- The CLT explains *how fast* relative frequency converges: the standard deviation of the sample mean is $\dfrac{\sigma}{\sqrt{n}}$, which is why **quadrupling the sample size only halves the error**

### Beyond high school — University

- The law of large numbers has two versions: the **weak** law (convergence in probability) and the **strong** law (almost sure convergence) — proving them requires measure theory
- Frequentist statistics is built entirely on relative frequency — probability *is* the long-run proportion. Bayesian statistics offers an alternative: probability as degree of belief

---

## Connections

- **Foundation:** [[Probability Basics]] — theoretical probability, sample space, equally likely outcomes
- **Application:** [[Combined Probability]] — expected frequency often uses combined probability to find $P(A)$ first
- **Testing fairness:** [[Conditional Probability]] — comparing observed vs expected connects to the idea of evidence and updating beliefs
- **Data collection:** [[Classifying Data]] — relative frequency tables are a key way to summarise experimental data
- **Visualisation:** [[Statistical Charts]] — relative frequency can be displayed as bar charts or pie charts
- **For 9709 students:** [[MF19 Reference (9709)]] — which formulas on this card are on the MF19 exam sheet vs need memorising. (Other boards have their own sheets.)

> [!info] Beyond syllabus — Why casinos always win
> Casino games are designed so the house has a tiny edge — say $P(\text{house wins}) = 0.513$ in blackjack. On any single hand, the player might win. But the law of large numbers guarantees that over thousands of hands, the casino's relative frequency of winning will be very close to 0.513. That tiny edge, multiplied by millions of games, produces a reliable profit. Casinos don't gamble — they do maths.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{f}{n}$ | `\dfrac{f}{n}` | Relative frequency |
| $P(A) \times n$ | `P(A) \times n` | Expected frequency |
| $\left(\dfrac{1}{2}\right)^{10000}$ | `\left(\dfrac{1}{2}\right)^{10000}` | Probability of extreme run |
