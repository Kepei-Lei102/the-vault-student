---
chinese: 抽样与估计 (chōuyàng yǔ gūjì)
prerequisites:
  - "[[Linear Combinations of Random Variables]]"
  - "[[Normal Distribution]]"
  - "[[Continuous Random Variables]]"
  - "[[Inventing Variance]]"
leads_to:
  - "[[Hypothesis Tests]]"
  - "[[t-Tests]]"
tags:
  - subject/mathematics
  - domain/statistics
  - domain/probability
  - level/A-Level
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/AP-Statistics
  - curriculum/IB-AA
  - syllabus/9709-6-4
  - type/deep
  - type/methodology
  - misconception/confidence-about-method
  - misconception/size-cures-bias
  - misconception/population-becomes-normal
  - misconception/sigma-forgets-root-n
---

# Sampling and Estimation 抽样与估计

> *A cook stirs the pot, tastes one spoonful, and knows the whole soup. A pollster asks a thousand voters and speaks for a country of fifty million. The miracle is not the spoon — it is the **stirring**: make the sample random, and a tiny taste carries the truth of the whole pot. This card is the mathematics of the spoonful: why it works ($\mathrm{Var}(\bar{X}) = \sigma^2/n$, the two-line theorem that makes statistics possible), when it lies spectacularly (a magazine once polled 2.4 million people and got the answer wrong by 19 points), and the crowning move of the subject — attaching an honest* price tag of doubt *to every estimate: "$\pm 3\%$, 19 times out of 20."*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| population | 总体 | the whole pot — every member of the group you care about |
| sample | 样本 | the spoonful — the members you actually measure |
| random sample | 随机样本 | every member equally likely to be chosen; the stirring |
| bias (of a method) | 偏倚 | a sampling method that systematically favours part of the pot |
| sampling distribution | 抽样分布 | the distribution of a statistic (like $\bar{X}$) across imagined re-runs |
| standard error | 标准误 | the standard deviation *of the sample mean*: $\sigma/\sqrt{n}$ |
| Central Limit Theorem | 中心极限定理 | means of large samples are approximately normal, whatever the population |
| unbiased estimator | 无偏估计量 | a recipe that is right **on average** across re-runs |
| confidence interval | 置信区间 | an interval built so the *method* catches the truth a stated fraction of the time |

## Population, sample, and the stirring

The **population** is every member of the group under study — every voter, every bolt off the production line, every fish in the lake. Measuring all of it is usually impossible or absurd (test *every* match to see how long matches burn and you have no matches left). So we take a **sample** — and immediately the whole subject turns on one question: *does the spoonful taste like the pot?*

It does **only if the pot is stirred**. A **random sample** is one where every member of the population has an equal chance of selection — in practice: number the population, then pick using **random numbers** (a table, a calculator's RNG), not human judgement. Anything less and the sample stops speaking for the population and starts speaking for *the convenient part of it*: ask about exercise habits outside a gym, survey opinions via a link people choose to click (the self-selected respond *because they feel strongly*), sample fish from the top of the lake (you learn about fish that swim near the surface). When an exam asks *why is this sampling method unsatisfactory?*, the answer is always the same shape: **name the group the method over- or under-represents, and say the sample is therefore biased — not random.**

> [!warning] The 2.4-million-person mistake
> In 1936 the *Literary Digest* mailed ten million ballots to predict the US presidential election and received **2.4 million back** — the largest poll ever taken. It predicted Landon over Roosevelt by a landslide; Roosevelt won 46 of 48 states. The mailing lists came from telephone directories and car registrations — in the Depression, a roster of the well-off — and the ballots came back disproportionately from those angry enough to reply. Meanwhile George Gallup called the election correctly with a sample **fifty times smaller**. The lesson is carved over the door of this subject: **a bigger biased sample is just a bigger bias.** Size cures *noise*; it does nothing for a tilted spoon.

## The pivot: the sample mean is itself a random variable

Here is the conceptual move the whole chapter rests on. You take one sample and compute one number, $\bar{x}$. But *imagine re-running the whole procedure* — new random sample, new mean. And again. The sample mean $\bar{X}$ is a **random variable**, with its own distribution across these imagined re-runs: the **sampling distribution**. Ask about its centre and its spread, and [[Linear Combinations of Random Variables]] has already done the work — $\bar{X} = \tfrac{1}{n}(X_1 + \dots + X_n)$ is a linear combination, so:

$$E(\bar{X}) = \mu, \qquad \mathrm{Var}(\bar{X}) = \frac{\sigma^2}{n}, \qquad \text{s.d.}(\bar{X}) = \frac{\sigma}{\sqrt{n}}.$$

The first equation says the sample mean points at the right target on average. The second is **the theorem that makes statistics possible**: averaging $n$ independent measurements shrinks the noise by $\sqrt{n}$ — the independent errors partly cancel, LinComb's perpendicular arrows refusing to line up. The quantity $\sigma/\sqrt{n}$ is important enough to own a name: the **standard error** of the mean.

Notice the square root's cruel economics: to *halve* your uncertainty you must *quadruple* your sample. That diminishing return is why national polls stop near a thousand people — and why the physics lab's habit of repeating a measurement ten times ([[Repeated Measurements]] — the same $\sigma/\sqrt{N}$, wearing a lab coat) buys real but bounded comfort.

## The Central Limit Theorem — the bell you didn't order

$E(\bar{X})$ and $\mathrm{Var}(\bar{X})$ hold for any population. The astonishing part is the **shape**:

- If the population $X$ is **normal**, then $\bar{X}$ is *exactly* normal — normals survive averaging ([[Linear Combinations of Random Variables]]'s shape-closure).
- If the population is **anything at all** — skewed, lumpy, discrete — then for large $n$ (rule of thumb $n \geqslant 30$), $\bar{X}$ is **approximately normal anyway**:

$$\bar{X} \;\approx\; N\!\left(\mu,\ \frac{\sigma^2}{n}\right).$$

That is the **Central Limit Theorem**, and it is why the [[Normal Distribution]] is everywhere: sums of many small independent contributions *become* normal regardless of their own shapes — the theorem Laplace supplied when Gauss's error-curve argument ran in a circle ([[Stories/Inventing Variance]] tells that story). The syllabus wants the informal understanding, and the honest informal statement is: **averaging manufactures the bell.** Watch it happen to real random data:

![[sampling-clt-live.mp4]]

![[sampling-clt-gallery.svg|690]]

## Unbiased estimates — and the famous $n-1$

We never know $\mu$ and $\sigma^2$; we estimate them from the sample. An estimator is **unbiased** if it is right *on average* across re-runs — individual estimates wobble, but the recipe has no systematic tilt. For the mean, the obvious recipe is already unbiased: $E(\bar{X}) = \mu$. For the variance, the obvious recipe is *not*, and the repair is the most-asked-about small formula in statistics:

$$s^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2 = \frac{1}{n-1}\left(\sum x^2 - \frac{(\sum x)^2}{n}\right).$$

> [!info] What the symbol $s^2$ is
> $s^2$ is **a number you compute from your sample** — Cambridge's phrase for it is *the unbiased estimate of the population variance*. Keep three variances apart: $\sigma^2$ is the **population's** true variance (unknown — the thing being hunted); the plain divide-by-$n$ variance from descriptive statistics is a **description of the sample itself**; and $s^2$, with its $n-1$, is the sample's **best guess at $\sigma^2$**. Same data as the descriptive version, different *job* — describing what you hold versus inferring what you don't.

**Why $n-1$?** Because the deviations are measured from $\bar{x}$, not from the true $\mu$ — and $\bar{x}$ *chased the data*. The sample mean sits, by construction, in the middle of the sample it came from, so the sample always looks a little tighter around $\bar{x}$ than the population is around $\mu$. Dividing by $n$ keeps that systematic under-estimate; dividing by $n-1$ inflates it back by exactly the right amount.

**Watch it fail, on a pot small enough to enumerate.** Take the tiny population $\{0, 3, 6\}$: $\mu = 3$, and $\sigma^2 = \tfrac{9 + 0 + 9}{3} = 6$. Now list **every** equally-likely sample of size $n = 2$ (with replacement — there are only nine) and run both recipes on each:

| samples | $\bar{x}$ | $\sum(x_i - \bar{x})^2$ | divide by $n$ (=2) | divide by $n-1$ (=1) |
|---|---|---|---|---|
| $(0,0)$, $(3,3)$, $(6,6)$ | — | $0$ | $0$ | $0$ |
| $(0,3)$, $(3,0)$ | $1.5$ | $4.5$ | $2.25$ | $4.5$ |
| $(3,6)$, $(6,3)$ | $4.5$ | $4.5$ | $2.25$ | $4.5$ |
| $(0,6)$, $(6,0)$ | $3$ | $18$ | $9$ | $18$ |
| **average over all nine** | | | $\mathbf{3}$ — *half* of $\sigma^2$ | $\mathbf{6} = \sigma^2$ exactly |

No randomness, no simulation — a complete enumeration you can check by hand. The divide-by-$n$ recipe averages to **3**, half the truth (a sample of two "sees" its own mean sitting between its two points, so half the spread hides); the $n-1$ recipe averages to exactly **6**. That is what "unbiased" means, made arithmetic:

![[sampling-nminus1-demo.svg|660]]

The bookkeeping behind "exactly": the $n$ deviations $x_i - \bar{x}$ are not free — they are chained by $\sum(x_i - \bar{x}) = 0$, so only $n-1$ of them carry independent information. (And the general two-line expectation proof: $E\left[\sum(X_i - \bar{X})^2\right] = \sum E(X_i^2) - nE(\bar{X}^2) = n(\sigma^2 + \mu^2) - n\left(\tfrac{\sigma^2}{n} + \mu^2\right) = (n-1)\sigma^2$ — the missing $\sigma^2$ is precisely the variance of $\bar{X}$ itself.)

> [!info] "Unbiased" is a property of the recipe, not a virtue of your answer
> Your particular $s^2$ is almost certainly wrong — unbiasedness only promises no *systematic* tilt across re-runs. And it is not everything: $s$ (the square root) is *not* an unbiased estimator of $\sigma$, and nobody minds. The syllabus wants the simple reading — "right on average" — and that is the honest one.

## Confidence intervals — pricing the doubt

Now the crown. An estimate alone ("$\bar{x} = 502.3$ g") is a guess with no warranty. The sampling distribution lets us attach one. Since $\bar{X} \approx N(\mu, \sigma^2/n)$, the standardised distance from $\bar{X}$ to $\mu$ is a $z$-score, and 95% of $z$-scores land within $\pm 1.96$:

$$P\!\left(\mu - 1.96\frac{\sigma}{\sqrt{n}} \;\leqslant\; \bar{X} \;\leqslant\; \mu + 1.96\frac{\sigma}{\sqrt{n}}\right) = 0.95
\;\;\Longleftrightarrow\;\;
\boxed{\;\bar{x} \pm 1.96\,\frac{\sigma}{\sqrt{n}}\;}$$

— the **95% confidence interval** for $\mu$ (use $\sigma$ if known; for a large sample, the estimate $s$ steps in). Other confidences just change the $z$: 90% → 1.645, 99% → 2.576, all read from [[Normal Distribution]]'s percentage points.

**What 95% actually promises** — the most misread number in science. The interval is the *fisherman's net*: the method, applied over and over to fresh samples, catches the true $\mu$ in 95% of throws. Any *one* interval either caught it or didn't — and $\mu$, a fixed number, does not "have a 95% chance of being inside." The confidence belongs to the **procedure**, not to your particular pair of endpoints. Here is the net, thrown at real random data:

![[sampling-ci-net.svg|690]]

**Proportions.** Polls estimate a fraction $p$ (support, defect rate) by the sample proportion $\hat{p}$. For large samples $\hat{p} \approx N\!\left(p, \tfrac{p(1-p)}{n}\right)$ (a binomial count wearing its normal approximation, divided by $n$), giving

$$\hat{p} \pm z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}.$$

This decodes the most familiar number in journalism: with $n = 1000$ and $\hat{p}$ near $\tfrac12$, the 95% margin is $1.96\sqrt{0.25/1000} \approx 0.031$ — **the "±3 points" of every national poll is just this formula evaluated once.**

## Worked examples

### Example 1 (9709 staple — unbiased estimates, then an interval)

> A machine fills bags of flour. A random sample of 50 bags has $\sum x = 25\,150$ g and $\sum x^2 = 12\,656\,000$ g². Find unbiased estimates of the population mean and variance, and a 95% confidence interval for the mean fill.

*Tool: the unbiased recipes (both on MF19 — note the $n-1$).*
$$\bar{x} = \frac{25\,150}{50} = 503.0 \text{ g}, \qquad s^2 = \frac{1}{49}\left(12\,656\,000 - \frac{25\,150^2}{50}\right) = \frac{1}{49}(12\,656\,000 - 12\,650\,450) = \frac{5550}{49} \approx 113.3 \text{ g}^2.$$

*Tool: large sample → CLT gives normality, $s$ stands in for $\sigma$.*
$$503.0 \pm 1.96\sqrt{\frac{113.3}{50}} = 503.0 \pm 1.96(1.505) = (500.05,\ 505.95) \text{ g}.$$

Interpretation for the mark: *we are 95% confident the population mean fill lies between about 500 g and 506 g* — meaning the method that produced this interval catches the truth 19 times in 20.

### Example 2 (the CLT earning its keep)

> Customers' spending at a shop has mean \$38 and standard deviation \$21 — **strongly right-skewed** (many small purchases, a few huge ones). Find the probability that the mean spend of the next 49 customers exceeds \$42.

*Tool: the sampling distribution — centre $\mu$, spread $\sigma/\sqrt{n}$, shape by CLT.*
$n = 49$ is large, so despite the skew, $\bar{X} \approx N\!\left(38,\ \tfrac{21^2}{49}\right) = N(38, 9)$ — standard error $3$.

*Tool: standardise ([[Normal Distribution]]'s $z$-discipline).*
$$P(\bar{X} > 42) = P\!\left(Z > \frac{42 - 38}{3}\right) = P(Z > 1.333) = 1 - 0.9088 \approx 0.091.$$

No individual customer is remotely normal; the *average of 49* very nearly is. That substitution — population shape irrelevant, only $\mu$, $\sigma$, $n$ needed — is the CLT doing exactly its job.

### Example 3 (the poll decoded — a proportion interval)

> In a random sample of 1000 voters, 520 support a proposal. Find a 95% confidence interval for the population proportion.

*Tool: the proportion interval, large sample.*
$$\hat{p} = 0.52, \qquad 0.52 \pm 1.96\sqrt{\frac{0.52 \times 0.48}{1000}} = 0.52 \pm 1.96(0.0158) = 0.52 \pm 0.031 = (0.489,\ 0.551).$$

The headline says "52% support, margin of error ±3 points" — and note what the interval quietly admits: **0.5 is inside**. On this sample, "majority support" is not a safe claim — which is precisely the kind of judgement [[Hypothesis Tests]] turns into a formal verdict.

## Common Misconceptions (Teaching Notes)

### 1. "There's a 95% chance the true mean is in this interval"

The most natural sentence in statistics, and wrong. $\mu$ is a fixed number; *this* interval either contains it or doesn't. The 95% describes the **method's** catch rate across re-runs (the net figure above: 19 of 20 throws). **Fix:** always attach the confidence to the procedure: "intervals built this way catch $\mu$ 95% of the time." An exam interpretation mark is earned by that phrasing.

### 2. "A bigger sample fixes everything"

Size fixes **noise** (the $\sqrt{n}$ shrinkage); it does nothing for **bias**. The *Literary Digest*'s 2.4 million answers lost to Gallup's fifty thousand because the spoon was tilted, not small. **Fix:** two separate diseases, two separate cures — randomness cures bias, size cures noise. Diagnose *which* problem a question describes before prescribing.

### 3. "For large $n$ the population becomes normal"

The population never changes — spending stays skewed, dice stay flat. What becomes normal is the distribution of the **sample mean** across re-runs. **Fix:** keep two pictures on the board: the population's histogram (fixed, any shape) and the sampling distribution of $\bar{X}$ (narrowing, normalising as $n$ grows). The CLT is a statement about the second picture only.

### 4. "Standard deviation $\sigma$… somewhere in the formula"

Using $\sigma$ where $\sigma/\sqrt{n}$ belongs — treating one draw's spread as the average's spread. **Fix:** ask *"is the question about one individual, or about a mean of $n$?"* before touching the table. One individual: $\sigma$. A mean: $\sigma/\sqrt{n}$, always smaller — averages are steadier than individuals, that is their entire point.

## The hunter's gallery — spot the tilted spoon

This card's deepest skill is not a formula. It is the hunter's question ([[Forward Reading and Problem Discovery]]) asked of every sample before trusting it: **"who could never end up in this spoonful?"** Whoever the method *cannot reach* is exactly where the bias hides — and no amount of data repairs it. A gallery to train the reflex:

| the scene | who the spoon can't reach | the bias, named |
|---|---|---|
| *Literary Digest*, 1936 — ballots via phone books and car registrations | Depression households with no phone and no car | **frame bias** — the list you sample from isn't the population |
| US election polls, 2016 — phone calls and online panels, answered by the willing | voters who hang up on pollsters, and communities living outside the pollsters' corner of the internet | **non-response bias** — the reachable differ from the unreachable |
| Wald's bombers, WWII — "armour the planes where the returners are riddled with holes" | the planes that never came back — hit in exactly the places the returners *weren't* | **survivorship bias** — Wald's fix: armour where the survivors are *clean* |
| a lake surveyed with a 5 cm-mesh net — "every fish here is over 5 cm!" | every fish smaller than the mesh | **observation selection** — the instrument edits the sample |
| website star-ratings | the quietly satisfied middle — only the delighted and the furious type reviews | **self-selection** — feeling strongly is the ticket in |
| "our customers report 95% satisfaction" | the ex-customers: the dissatisfied already left and can't be asked | **survivorship**, corporate edition |
| a landline survey at 2 pm on a Tuesday | everyone at work at 2 pm | **coverage/convenience** — sampling when and where it's easy |

Every row is the *Digest*'s disease in a different costume. Randomness is the only vaccine — and *"who's missing?"* is the diagnostic that works even when you can't vaccinate.

## Exam Notes

### Cambridge 9709 — P6 §6.4

- **The LO list:** sample vs population + the necessity of randomness; explain why a given method is unsatisfactory (name the over/under-represented group; elementary use of random numbers — quota/stratified vocabulary **not required**); $\bar{X}$ as a random variable with $E(\bar{X}) = \mu$, $\mathrm{Var}(\bar{X}) = \sigma^2/n$; $\bar{X}$ normal when $X$ is; the CLT **informally** for large samples; unbiased estimates of mean and variance from raw or summarised data; confidence intervals for a mean (normal population with known variance, *or* large sample) and, from a large sample, for a **proportion**.
- **MF19 gives** the unbiased $s^2$ with its $n-1$ (both algebraic forms) — the formula is handed to you; the *choice* to use $n-1$ and the interpretation marks are not.
- **Habits that earn marks:** say "unbiased estimate" when the question does; keep $z$ exact (1.96, 2.576 — from the percentage-points table); interpret intervals via the method's catch rate; for "why unsatisfactory" answers, name the excluded group *and* the word **biased**.

### Cambridge 9231 — Further Probability & Statistics (forward)

- §4.2 picks up exactly where this card's fine print stops: a **small** sample from a normal population with $\sigma$ **unknown** replaces $z$ by Student's $t$ — the brewer's problem ([[Stories/Inventing Variance]]'s Gosset cameo, formalised). The known-$\sigma$/large-$n$ interval here is the special case his $t$ collapses to as $n$ grows.

### AP Statistics

- This card is the *spine* of AP Stats: sampling design and bias (Unit 3), sampling distributions with $\sigma/\sqrt{n}$ and the CLT (Unit 5), confidence intervals for proportions and means (Units 6–7). AP goes further on survey design vocabulary (stratified, cluster, convenience — named there, not on 9709) and on checking conditions before intervals; the mathematics is this card's.

### IB AA

- SL/HL 4.x carries the concepts qualitatively — population vs sample, randomness, bias in sampling — without the confidence-interval machinery. The vocabulary and the Literary-Digest cautionary logic transfer whole.

## Beyond the syllabus

> [!info] The brewer's correction — Student's $t$
> Recall the fine print: our interval needs $\sigma$ known or $n$ large, because for small $n$, substituting the *estimate* $s$ adds extra wobble the normal table doesn't price. W. S. Gosset, quality-controlling stout at Guinness with samples of four and five, worked out the honest replacement distribution — fatter-tailed than the normal, approaching it as $n$ grows — and published it as **"Student"** ([[Stories/Inventing Variance]] has the alias story). His $t$ runs every small-sample lab result you will ever read, and is the opening act of 9231's Further Stats paper.

> [!info] The bootstrap — sampling from your own sample
> A thoroughly modern twist on this card's central idea. No formula for your statistic's standard error? **Resample your own sample** — draw $n$ values *from the sample itself* (with replacement), compute the statistic, repeat ten thousand times, and read the spread of the re-computed values as the sampling distribution. Efron's bootstrap (1979) turns the imagined re-runs of this card into *actual* re-runs a laptop performs in a second — statistics' answer to "what if theory is too hard: brute-force the re-running." It only became thinkable when computers made resampling free.

> [!info] Real polls, and the modern Literary Digests
> Real polling can't achieve the textbook's pure random sample (no list of all citizens exists; most people don't answer), so pollsters sample as randomly as they can, then **weight** the respondents to match the population's known shape — and the ±3% you see printed prices only the *sampling* noise, not the weighting model's judgement calls. When polls miss badly (2016's state-level misses came largely from under-weighting education), it is the *Digest*'s disease in modern dress: **non-response bias** — the people you couldn't reach differing from the people you could. The formulas on this card are exact; reaching the pot they describe is the eternally hard part.

## Connections

- **Builds on:** [[Linear Combinations of Random Variables]] — $E(\bar{X}) = \mu$ and $\mathrm{Var}(\bar{X}) = \sigma^2/n$ are its averaging theorem, promoted to main character; [[Normal Distribution]] — the $z$-machinery every interval runs on, and the shape the CLT manufactures; [[Continuous Random Variables]] — $\bar{X}$ is a continuous random variable, and the CLT is a statement about its pdf.
- **Leads to:** [[Hypothesis Tests]] — the same sampling distributions, pointed at a verdict: Example 3's "is 0.5 inside the interval?" becomes a formal test, and P6 closes there.
- **Kindred:** [[Repeated Measurements]] — the physics lab is this card in a lab coat: $N$ repeats, the mean, and the error of the mean $\sigma/\sqrt{N}$ (Galton's ox-weighting crowd lives there); [[Stories/Inventing Variance]] — Gosset, Fisher, and the human history of "unbiased"; [[Poisson Distribution]] — another population whose samples this machinery serves.
- **For 9709 students:** [[MF19 Reference (9709)]] — the unbiased $s^2$ (with its $n-1$) is printed on the sheet; the $z$-values live in the percentage-points table; the CLT and every interpretation live in your head.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\bar{X}$, $\bar{x}$ | `\bar{X}`, `\bar{x}` | the sample mean as RV / as computed value |
| $\mu$, $\sigma^2$ | `\mu`, `\sigma^2` | population mean, variance |
| $\sigma/\sqrt{n}$ | `\sigma/\sqrt{n}` | standard error of the mean |
| $s^2$ | `s^2` | unbiased estimate of $\sigma^2$ (denominator $n-1$) |
| $\hat{p}$ | `\hat{p}` | sample proportion |
| $\pm$ | `\pm` | the interval's honest wings |
| $N(\mu, \sigma^2/n)$ | `N(\mu, \sigma^2/n)` | the sampling distribution of $\bar{X}$ |
| $\leqslant$ | `\leqslant` | Cambridge's slanted ≤ |
