---
chinese: t 检验 (t jiǎnyàn) — 小样本下的均值推断
prerequisites:
  - "[[Hypothesis Tests]]"
  - "[[Sampling and Estimation]]"
  - "[[Normal Distribution]]"
leads_to:
  - "[[Chi-Squared Tests]]"
  - "[[Non-Parametric Tests]]"
  - "[[The Lady Tasting Tea]]"
tags:
  - subject/mathematics
  - domain/statistics
  - domain/probability
  - level/A-Level
  - level/AP
  - level/IB
  - curriculum/Cambridge-9231
  - curriculum/A-Level
  - curriculum/AP-Statistics
  - curriculum/IB-AI
  - syllabus/9231-4-2
  - type/deep
  - type/technique
  - notation/t-distribution
  - notation/degrees-of-freedom
  - misconception/z-when-sigma-unknown
  - misconception/two-sample-on-paired-data
  - misconception/degrees-of-freedom-equals-n
  - misconception/pooling-unequal-variances
---

# t-Tests t 检验

> *Every test of a mean you have met so far quietly assumed you knew the population's spread, or had so much data that guessing it cost nothing. A brewer with four barrels has neither. This card is what he did about it — and it turns out that almost every real experiment is the brewer's situation, not the textbook's.*

## Definition

### Formal

Let $X_1, \dots, X_n$ be a random sample from a normal population with mean $\mu$ and **unknown** variance, with sample mean $\bar{X}$ and unbiased sample variance $S^2 = \dfrac{1}{n-1}\sum (X_i - \bar{X})^2$. Then

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}}$$

has **Student's $t$-distribution with $\nu = n - 1$ degrees of freedom**, written $t_{n-1}$: a symmetric bell centred on $0$, **fatter in the tails than the standard normal**, and tending to $N(0,1)$ as $\nu \to \infty$.

A **$t$-test** is a hypothesis test whose statistic has this distribution under $H_0$; a **$t$-interval** is a confidence interval built from its critical values. Both are the [[Hypothesis Tests]] and [[Sampling and Estimation]] machinery with one substitution — the unknown $\sigma$ replaced by its estimate $s$ — and the honest price of that substitution paid.

### Intuitive

Recall from [[Sampling and Estimation]] that $\bar{X}$ has standard error $\sigma/\sqrt{n}$, and that when $\sigma$ is known (or $n$ is large) the standardised $\dfrac{\bar{X}-\mu}{\sigma/\sqrt{n}}$ is exactly (or nearly) $N(0,1)$. Now take $\sigma$ away. You must divide by $s/\sqrt{n}$ instead — and **$s$ is itself a random quantity**, computed from the same few numbers as $\bar{x}$. On a small sample $s$ can come out badly low by pure luck, and when it does, dividing by it *inflates* the statistic. So the ratio wanders further from zero, more often, than a normal variable would: the tails fatten. **The $t$-distribution is the normal, with the wobble of $s$ priced in.** How much wobble depends on how few numbers $s$ was built from — which is why there is one $t$ curve for each sample size, indexed by $\nu = n - 1$.

The whole subject then reduces to a swap: wherever the $z$-machinery of the parent cards said "look up $1.96$", you now look up $t_{n-1}$'s value instead — larger, by an amount that shrinks as $n$ grows.

### 中文锚点 (Chinese Anchor)

**t 检验**（也叫**学生 t 检验**，Student's t-test）解决的是：总体方差**未知**、样本又**小**的时候，怎样对均值下结论。中国教材里这一节通常就排在正态分布 z 检验后面，关键差别只有一个：把未知的 $\sigma$ 换成样本标准差 $s$ 之后，统计量不再服从标准正态，而服从**自由度**为 $n-1$ 的 t 分布——尾巴更厚，临界值更大，样本越小差得越多。

术语对照：**自由度**（degrees of freedom, $\nu$）；**单样本 t 检验**（one-sample）；**双样本 t 检验**（two-sample，独立样本）；**配对 t 检验**（paired，同一对象前后两次）；**合并方差**（pooled variance, $s_p^2$）；**置信区间**（confidence interval）。中文的"配对"二字比英文 *paired* 更直白：一对一对地比，而不是两堆一起比——这正是本卡最大的考点。

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| $t$-distribution | $t_\nu$ or $t(\nu)$ | "t with nu degrees of freedom" | $\nu = n-1$ for one sample; $n_1 + n_2 - 2$ pooled |
| Degrees of freedom | $\nu$ (nu) | "degrees of freedom" | The number of *free* deviations once $\bar{x}$ is fixed |
| Sample variance | $s^2 = \dfrac{1}{n-1}\left(\sum x^2 - \dfrac{(\sum x)^2}{n}\right)$ | "s squared" | The unbiased estimate — the $n-1$ of [[Sampling and Estimation]] |
| Pooled variance | $s_p^2$ | "s p squared" | Two samples' evidence about one common $\sigma^2$, combined |
| Differences | $d_i = x_i - y_i$, $\bar{d}$, $s_d$ | "d bar", "s d" | The paired design turns two columns into one |
| Critical value | $t_\nu(p)$ | "the $p$-point of $t_\nu$" | MF19 tabulates $t$ with $P(T \le t) = p$ |

> [!info] Recall — where the computing form $\sum x^2 - \frac{(\sum x)^2}{n}$ comes from
> The definition of spread is $\sum(x - \bar{x})^2$; the form you compute with is $\sum x^2 - \dfrac{(\sum x)^2}{n}$. They are the same number, and the reason is two lines: expand the square and use $\sum x = n\bar{x}$.
> $$\sum(x-\bar{x})^2 = \sum\left(x^2 - 2\bar{x}x + \bar{x}^2\right) = \sum x^2 - 2\bar{x}\,n\bar{x} + n\bar{x}^2 = \sum x^2 - n\bar{x}^2 = \sum x^2 - \frac{(\sum x)^2}{n}.$$
> Same identity as $\operatorname{Var}(X) = E(X^2) - \mu^2$ in [[Discrete Random Variables]] — the cross term collapses because the mean is what makes the deviations sum to zero. Summarised exam data hand you $\sum x$ and $\sum x^2$, so this is the form every case below uses.

> [!warning] Reading the MF19 table — the column is a *cumulative* probability
> The printed table gives, for each $\nu$ and each $p$, the $t$ with $P(T \le t) = p$. So a **two-tailed 5%** test wants $2.5\%$ in the upper tail — read the **$p = 0.975$** column ($\nu = 9$: $2.262$). A **one-tailed 5%** test reads $p = 0.95$ ($\nu = 8$: $1.860$). A 95% interval uses the two-tailed value. The mark scheme awards a **B1 for the correct $t$-value seen** — reading the wrong column is a mark lost before any arithmetic happens.

## Why the normal is wrong for small samples — and by how much

Two things happen as $\nu$ grows, and both are visible in one figure:

![[t-vs-normal.svg|880]]

The tails start grotesquely fat — with $\nu = 1$ the 2.5% point is at $12.7$, six times the normal's — and collapse toward the normal quickly: by $\nu = 30$ the difference is a few hundredths. Read the ladder of two-tailed 5% critical values as the **tax for not knowing $\sigma$**, and watch it shrink:

| $\nu$ | 1 | 2 | 4 | 9 | 16 | 30 | 100 | $\infty$ (normal) |
|---|---|---|---|---|---|---|---|---|
| $t_\nu(0.975)$ | 12.71 | 4.30 | 2.78 | 2.26 | 2.12 | 2.04 | 1.98 | 1.96 |

So a sample of five pays a 40% surcharge on its interval width; a sample of thirty pays 4%. This is exactly why the parent cards' fine print said "$\sigma$ known, or $n$ large": for large $n$ the normal *is* the $t$, near enough, and the surcharge is not worth a table.

![[t-tail-shrinks.mp4]]

> [!info] Why $n - 1$ — the one line worth carrying
> The deviations $x_i - \bar{x}$ are constrained to sum to zero (that is what $\bar{x}$ *means*), so once $n-1$ of them are known the last is forced. Only $n-1$ of them are free to wobble, and $s^2$ is built from those $n-1$ free directions — the same fact that makes $s^2$ unbiased in [[Sampling and Estimation]] fixes the $t$-curve's index here, and it is the "$(n-1)$-dimensional space" of the next section.

## Why it works — the $\sigma$ that cancels, and the theorem behind the guess

The honest question to ask before trusting any of the engines below: *why should a ratio computed from five numbers follow a curve printed in a book?* Not because Gosset tried things until they fitted. Because of two facts — one small and one deep — and each has a plain-life version worth holding onto before its formula.

**The small fact: the ratio measures in the sample's own units, so $\sigma$ never enters.** Weigh the bananas of engine 4's case in grams instead of kilograms. Every observation is a thousand times bigger, so $\bar{x}$ is, and so is $s$ — and $t$ does not move, because it asks a question that has no units: *how many of the sample's own standard errors away from $\mu_0$ did the mean land?* Any statistic that gave a different verdict in grams than in kilograms would be a broken statistic; $t$ passes that test by construction. And that same indifference is the whole trick, because "the population's spread" is nothing but a choice of scale too — a population with $\sigma = 20$ *is* a population with $\sigma = 1$ measured in different units. So the distribution of $t$ cannot depend on $\sigma$. In symbols:

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{\;\dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}\;}{\;S/\sigma\;} = \frac{Z}{\,S/\sigma\,},$$

a standard normal on top, and underneath the sample spread *measured in units of the true spread* — a pure number whose behaviour depends only on how many values went into $S$. $\mu$ was subtracted away, $\sigma$ has cancelled, and what is left depends on $n$ alone. **That is why one table, one row per $\nu$, serves every normal population there is** — the brewer's yeast counts and a physicist's timings alike. (The grown-up name for such a quantity is a *pivot*.) The parent card's $z$ had this property only when someone handed you $\sigma$; Gosset's move was to build a ratio that has it when nobody does.

**Why the tail is fat — the four-shot marksman.** Judge a rifle's precision from four shots. Most of the time the four scatter about as much as the rifle really scatters, and your estimate $s$ is fair. But now and then four shots happen to land in a tight bunch by pure luck — and you conclude the rifle is far more precise than it is. Now measure how far the group's centre sits from the bullseye *in units of that too-small $s$*: an ordinary offset looks like an enormous miss. That is what the ratio does. **$t$ is a fraction, and a fraction blows up when its bottom comes out small; with few numbers, $s$ comes out small by luck often enough to matter.** Those unlucky bunches are the fat tail. Give the marksman thirty shots and a lucky bunch of all thirty is essentially impossible — $s$ can no longer be tiny by accident, the fraction can no longer explode, and the tail thins toward the normal's. This is the whole ladder ($12.7 \to 2.8 \to 2.3 \to 2.0$) in one story.

**The deep fact: the shape is a theorem, not a fit.** For a normal population two things are true, and Fisher proved both with a piece of geometry:

- **Where the sample sits and how scattered it is are independent** — knowing a class's average height tells you nothing about how spread out its heights are; a tall class can be tight or scattered. Geometrically: write the $n$ data values as one point in $n$-dimensional space; the mean is that point's shadow on the diagonal direction $(1, 1, \dots, 1)$, the deviations $x_i - \bar{x}$ are the perpendicular part, and for normal data the shadow and the perpendicular part are independent.
- **The scatter lives in $n - 1$ dimensions.** The deviations sum to zero — the data balance on the mean like children on a seesaw — so once $n-1$ of them are known, the last is forced. Their squared length $(n-1)S^2/\sigma^2$ is therefore a sum of $n-1$ squared standard normals, a **chi-squared with $n-1$ degrees of freedom** — the family [[Chi-Squared Tests]] examines in its own right.

Put together, $T = Z\big/\sqrt{\chi^2_{n-1}/(n-1)}$ with independent parts, and that ratio has an exact density that can be written down:

$$f(t) \;\propto\; \left(1 + \frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}}, \qquad \nu = n - 1.$$

Read the marksman off it: it decays like a *power* of $t$, not like $e^{-t^2/2}$ — that is the fat tail in symbols. And as $\nu \to \infty$, $\left(1 + \frac{t^2}{\nu}\right)^{-\nu/2} \to e^{-t^2/2}$ — the limit $\left(1 + \frac{x}{n}\right)^n \to e^x$ from [[Exponential Function]] in disguise — which *is* the standard normal. The collapse you watched in the animation is that limit happening.

**So was it Gosset's trial and error?** Half. In 1908 he worked out the first four moments of $S^2$, matched them to a curve, and — with no proof that $\bar{X}$ and $S$ were independent, which he admitted — **checked it by hand simulation**: three thousand measurements written on cards, shuffled, dealt into 750 samples of four, the ratio computed for each and tallied against his curve. It fitted. Fisher supplied the proof (1912, in a letter; in print by 1925), gave the exact density, and christened the letter $t$. So for a normal population the $t$-test is **not an approximation — it is exact**, a theorem about a ratio. The only approximation anywhere in this card enters when the population is *not* normal, and that is a separate question (robustness, in the Beyond notes).

**Check it yourself — Gosset's experiment, rerun on a laptop.** Twenty thousand samples of four from a normal population, the ratio computed for each:

![[t-gosset-experiment.svg|900]]

The tally follows $t_3$, not the normal — and the tail is not a nuance: about one ratio in seven lands beyond $\pm 1.96$, where the normal table promised one in twenty. A student who used $1.96$ on samples of four would be wrong nearly three times as often as they believed. That is the experiment Gosset ran with a deck of cards, and it is why the table exists.

## The four engines — each with the real case it was built for

Recall the five-step ritual of [[Hypothesis Tests]]: **state** $H_0, H_1$ with the parameter defined in words; **read the tails** off $H_1$'s wording; **compute** the statistic; **compare** with the critical value; **conclude in context** without over-claiming. Nothing about the ritual changes across this card. What changes is the engine in step 3 and the table in step 4 — and there are four engines. Each is stated below in a few lines and then **immediately run on the real Paper 4 question it exists for**, worked with the mark-scheme values, so no formula floats free of a case. Read tool, then case, then move on; the four together are the whole section.

### Engine 1 — one sample, $\sigma$ unknown, $n$ small: the $t$-test and $t$-interval

**The tool.** Assumptions: the population is normal, the sample random. Under $H_0: \mu = \mu_0$,

$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}, \qquad \nu = n - 1,$$

and the matching interval — the parent card's $\bar{x} \pm z\,\sigma/\sqrt{n}$ with the two swaps made ($s$ for $\sigma$, $t_{n-1}$ for $z$):

$$\bar{x} \;\pm\; t_{n-1}(p)\,\frac{s}{\sqrt{n}}.$$

**The case — 9231/41 November 2025 Q1.**

> Ten school children estimate the size of an angle $\theta°$ in a given acute-angled triangle: $84, 85, 77, 85, 84, 87, 86, 88, 83, 85$.
> **(a)** Stating any assumptions you make, calculate a 95% confidence interval for $\theta$. **[5]**

**Why this engine.** One column of numbers, one population — nothing is paired and there is no second group. Nothing tells us $\sigma$: the only spread we have is the ten estimates' own. And $n = 10$ is small, so the Central Limit Theorem gives no cover for using $1.96$. Unknown $\sigma$ + small $n$ + one sample = engine 1, and since the question asks for an interval, the $t$-interval with $\nu = 9$.

*Tool: the unbiased estimates.* $\sum x = 844$, $\sum x^2 = 71314$, $n = 10$:

$$\bar{x} = 84.4, \qquad s^2 = \frac{1}{9}\left(71314 - \frac{844^2}{10}\right) = \frac{134}{15} = 8.933.$$

*Tool: the $t$-interval — small $n$, $\sigma$ unknown, so $t_9$.* **Table read:** MF19's $t$-table, row $\nu = 9$, column $p = 0.975$ (95% two-tailed leaves $2.5\%$ above) → **$2.262$**. That is where the number comes from — nothing is computed, it is looked up, and the B1 is for looking it up in the right row and column.

$$84.4 \pm 2.262\sqrt{\frac{8.933}{10}} = 84.4 \pm 2.14 \quad\Longrightarrow\quad [82.3,\ 86.5].$$

**Assumption (a mark on its own):** the estimates are a random sample from a **normal** population — that is what licenses $t$ at $n = 10$. (The mark scheme accepts "the distribution of estimates is normal", "the estimates are independent" or "a random sample from some population".) Note what it refuses: writing $84.4 \pm 2.1$ and stopping — an interval is two numbers, and the mark is for stating them.

---

### Engine 2 — paired samples: engine 1 in disguise

**The tool.** When each observation in one sample has a natural partner in the other — the *same* athlete before and after, the *same* patient on two drugs, the *same* field under two fertilisers — form the differences $d_i = x_i - y_i$ and run engine 1 on them:

$$t = \frac{\bar{d} - \delta_0}{s_d/\sqrt{n}}, \qquad \nu = n - 1 \ (\text{$n$ = number of pairs}),$$

where $\bar{d}$ is the **mean of the differences** (the average change per pair), $s_d$ their sample standard deviation, and $\delta_0$ the value $H_0$ claims for the *population* mean difference $\mu_d$ — almost always $0$, "no change", which is why the numerator usually reads just $\bar{d}$. The assumption is now that the **population of differences** is normal, and the interval is $\bar{d} \pm t_{n-1}(p)\, s_d/\sqrt{n}$.

**The case — 9231/41 November 2025 Q6.**

> Nine athletes complete a 1500 m time trial before and after a new training programme their coach believes will **reduce** their times (seconds):
> before — $250, 251, 252, 267, 276, 291, 310, 320, 335$; after — $245, 251, 253, 261, 275, 293, 302, 313, 320$.
> **(a)** Carry out a paired $t$-test at the 5% level to test the coach's belief. **[7]**
> **(b)** Further research suggests the programme reduces the times of slower athletes by more than those of faster ones. Suggest a reason why the paired $t$-test may not have been appropriate. **[1]**
> **(c)** Name a more appropriate test. **[1]**

**Why this engine.** The same nine athletes, each measured twice — every "after" belongs to one specific "before". That is the paired signature, so the two columns are *not* two independent samples: they are nine differences. (The question happens to say "paired" here; the November 2025 paper's own Q1 did not say "one-sample", and most papers leave the design for you to see — the tell is *same individuals, two measurements*.) Nine differences, spread unknown, $n = 9$ small → engine 1 run on the differences, which is engine 2, $\nu = 8$. "Reduce" is a direction → one-tailed.

**(a)** *Tool: the ritual, on the population of differences.* Let $\mu_d$ be the population mean of (before $-$ after). $H_0: \mu_d = 0$ (so $\delta_0 = 0$ — the coach's programme changes nothing); $H_1: \mu_d > 0$ — "reduce" is a direction, so **one-tailed**. **Table read:** row $\nu = 8$, column $p = 0.95$ (all $5\%$ in one tail) → **$1.860$**. (The mark scheme insists the hypotheses name the *population*.)

*Tool: differences first, then engine 1.* $d = 5, 0, -1, 6, 1, -2, 8, 7, 15$; $\sum d = 39$, $\sum d^2 = 405$:

$$\bar{d} = \frac{39}{9} = 4.333, \qquad s_d^2 = \frac{1}{8}\left(405 - \frac{39^2}{9}\right) = 29.5, \qquad t = \frac{4.333}{\sqrt{29.5/9}} = 2.39.$$

$2.39 > 1.860$: reject $H_0$. There is evidence at the 5% level that the programme reduces times.

**(b)** *Tool: check the assumption the test rests on.* The paired $t$ assumes the **population of differences is normal** — in particular, that every athlete's improvement is a draw from one common distribution around $\mu_d$. If slower athletes improve systematically more, the differences depend on the athlete's speed and are not draws from one normal population (nor even symmetric). The assumption fails; the test's $t_8$ reference curve is the wrong ruler.

**(c)** A test that does not need normality: the **Wilcoxon matched-pairs signed-rank test** (or the paired-sample sign test) — [[Non-Parametric Tests]], the next paper section, and the reason it exists.

**Why pair at all — the same case, done wrong.** A two-sample test measures a difference *against the spread within each group*, and these nine runners differ from one another by eighty-five seconds while the training changed each by a few. Pairing subtracts each athlete from himself, and the between-athlete spread vanishes from the denominator:

![[t-paired-vs-unpaired.svg|900]]

Same nine athletes, same numbers: treated as two independent samples the improvement is invisible ($t = 0.30$); treated as nine differences it is clear ($t = 2.39$). **The design decides what the data can say** — which is why the syllabus lists "the ability to select the test appropriate to the circumstances" as a learning objective in its own right.

---

### Engine 3 — two independent samples, common variance: the pooled $t$

**The tool.** Two samples of sizes $n_1, n_2$ from normal populations **assumed to share one variance $\sigma^2$** — the question will say so: *"you should assume the two distributions are normal and have the same population variance"*. Each sample carries evidence about that one $\sigma^2$; combine it, weighting by degrees of freedom:

$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2} = \frac{\sum(x - \bar{x})^2 + \sum(y - \bar{y})^2}{n_1 + n_2 - 2}.$$

The second form is the one MF19 prints, and the one summarised data hands you: $\sum(x-\bar{x})^2 = \sum x^2 - \dfrac{(\sum x)^2}{n_1}$. Then, since $\operatorname{Var}(\bar{X} - \bar{Y}) = \sigma^2\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)$ for independent samples ([[Linear Combinations of Random Variables]] — variances of independent things add):

$$t = \frac{(\bar{x} - \bar{y}) - \delta_0}{s_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}}, \qquad \nu = n_1 + n_2 - 2,$$

with $\delta_0$ the hypothesised difference (usually $0$), and the interval $(\bar{x} - \bar{y}) \pm t_{n_1+n_2-2}(p)\, s_p\sqrt{\tfrac{1}{n_1} + \tfrac{1}{n_2}}$. **Why $n_1 + n_2 - 2$:** two sample means were estimated, so two constraints were spent — $n_1 - 1$ free deviations from the first sample plus $n_2 - 1$ from the second.

**The case — 9231/41 June 2025 Q4.**

> Ten students from school $X$ and eight from school $Y$ sit the same English test: $\sum x = 612$, $\sum x^2 = 40104$, $\sum y = 444$, $\sum y^2 = 27460$. Assume both distributions are normal with the same population variance.
> **(a)** Find a 95% confidence interval for the difference in mean scores. **[6]**
> **(b)** Use it to explain why there is insufficient evidence at 5% that the scores differ. **[1]**

**Why this engine.** Two *different* groups of students — ten from one school, eight from another — so no student has a partner in the other column and pairing is impossible (the unequal sizes, $10 \neq 8$, are the giveaway: paired data always come in equal numbers). Both samples are small, so no CLT and no $z$: a $t$-engine. And the question grants the one thing that decides between the two-sample $t$-engines: *"assume … the same population variance"* — so pool. Engine 3, $\nu = 10 + 8 - 2 = 16$; the question asks for the interval for the difference.

**(a)** *Tool: pooled variance from summarised data — the MF19 form.*

$$\sum(x-\bar{x})^2 = 40104 - \frac{612^2}{10} = 2649.6, \qquad \sum(y-\bar{y})^2 = 27460 - \frac{444^2}{8} = 2818,$$

$$s_p^2 = \frac{2649.6 + 2818}{10 + 8 - 2} = 341.725.$$

*Tool: the two-sample $t$-interval, $\nu = 16$.* **Table read:** row $\nu = 16$, column $p = 0.975$ → **$2.120$**. With $\bar{x} - \bar{y} = 61.2 - 55.5 = 5.7$:

$$5.7 \pm 2.120\sqrt{341.725\left(\frac{1}{10} + \frac{1}{8}\right)} = 5.7 \pm 2.120 \times 8.769 = 5.7 \pm 18.6 \quad\Longrightarrow\quad [-12.9,\ 24.3].$$

In words: **we are 95% confident that the true difference in mean scores, $\mu_X - \mu_Y$, lies between $-12.9$ and $24.3$.** Say it carefully — the 95% belongs to the *method*: intervals built this way capture the true difference in 95% of repeated samplings, and this one either did or did not (misconception 6 below). What it certainly says is that every difference from $-12.9$ to $24.3$ is compatible with the data at this level — including $0$.

**(b)** *Tool: an interval is a test read backwards.* A 95% interval for $\mu_X - \mu_Y$ contains every value of the difference that a two-tailed 5% test would *not* reject. Zero lies inside $[-12.9, 24.3]$, so $H_0: \mu_X = \mu_Y$ is not rejected at 5%. One sentence, one mark — and worth understanding rather than memorising, because the same reading works for every interval on this card.

---

### Engine 4 — two samples, the normal engine: large samples, or known variances

**The tool.** When both samples are **large**, the Central Limit Theorem takes over and the population variances need not be equal or known: each is estimated by its own $s^2$, and

$$z = \frac{(\bar{x} - \bar{y}) - \delta_0}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$$

is compared with the **normal** critical values ($1.645$, $\pm 1.96$, …). The same formula with the true $\sigma_1^2, \sigma_2^2$ in place of $s_1^2, s_2^2$ is the known-variance test, exact for normal populations at any $n$. The interval is $(\bar{x} - \bar{y}) \pm z\sqrt{s_1^2/n_1 + s_2^2/n_2}$.

**The case — 9231/43 June 2026 Q5.**

> Rhiannon claims the mean mass of bananas at supermarket $X$ is less than at $Y$. Random samples of $44$ from $X$ and $52$ from $Y$: $\sum x = 6.63$, $\sum x^2 = 1.21$, $\sum y = 8.56$, $\sum y^2 = 1.65$ (kg). Do **not** assume equal population variances. Test her claim at the 10% level.

**Why this engine.** Two different sets of bananas from two shops — no pairing ($44 \neq 52$ again). Both samples are **large**, so the Central Limit Theorem makes $\bar{X} - \bar{Y}$ close to normal whatever the populations, and each sample can estimate its own variance well enough that no $t$-table is needed. And the question forbids the pooling assumption in as many words — *"do not assume equal population variances"* — which closes the door on engine 3 even if the samples had been small. Large + unequal variances = engine 4: the normal engine with $s_x^2/n_x + s_y^2/n_y$. "Less than" is a direction → one-tailed.

$H_0: \mu_X = \mu_Y$; $H_1: \mu_X < \mu_Y$ — one-tailed, 10%. **Table read:** this engine uses the *normal* table, not the $t$-table — $\Phi(z) = 0.90$ gives $z = 1.282$, so reject if $z < -1.282$.

$$\bar{x} = 0.1507, \quad \bar{y} = 0.1646, \qquad s_x^2 = \frac{1}{43}\left(1.21 - \frac{6.63^2}{44}\right) = 4.907\times10^{-3}, \quad s_y^2 = \frac{1}{51}\left(1.65 - \frac{8.56^2}{52}\right) = 4.723\times10^{-3},$$

$$z = \frac{0.1507 - 0.1646}{\sqrt{\dfrac{4.907\times10^{-3}}{44} + \dfrac{4.723\times10^{-3}}{52}}} = \frac{-0.0139}{0.01422} = -0.98.$$

$-0.98 > -1.282$: do not reject $H_0$. Insufficient evidence at 10% that $X$'s bananas are lighter. (The mark scheme's own margin note: pooling here scores **A0** — the question told you the variances differ, and the pooled form is a different test.)

## Choosing the engine — the questions to ask, in order

Four engines, four cases — and in the exam the first mark is often for picking the right one. The questions, in the order that avoids the classic slip:

![[t-choose-the-test.svg|900]]

| Ask | If yes → | If no → |
|---|---|---|
| **Are the observations naturally paired?** (same subject, before/after; matched pairs) | **Engine 2**, paired $t$ on the differences | continue |
| **One sample or two?** | one: continue at the next row with that sample | two: skip to the fourth row |
| **Is $\sigma$ known, or is $n$ large?** | **$z$** — the parent cards' test | **Engine 1**, one-sample $t$, $\nu = n-1$ |
| **Two samples: are both large?** | **Engine 4**, normal with $s_1^2/n_1 + s_2^2/n_2$ | small: are you told to assume a common variance? — yes: **Engine 3**, pooled $t$, $\nu = n_1+n_2-2$; no: outside this syllabus (Welch's $t$, below) |

The paired question comes **first** because it is the one students skip: the data arrive as two columns and look like two samples, and the word "paired" is rarely printed in the question. Look for the same *individuals* measured twice.

## Where the $t$-test meets the world

This is one of the few techniques on the syllabus that was **invented at work, for the work**, and it is still the working tool it was built to be.

- **The brewery.** William Sealy Gosset joined Guinness in Dublin in 1899 as a chemist, and his problem was that a brewery cannot afford large samples: a trial of a barley strain is a handful of plots, a check on a batch of stout is a few casks. The $z$-machinery of the day needed $\sigma$ known, or thirty-plus observations; he had four. So he worked out — by hand, and by shuffling three thousand cards of measurements to simulate samples of four — what the ratio $(\bar{x}-\mu)/(s/\sqrt{n})$ actually does, and published the answer in 1908 under the name **"Student"** because Guinness would not let employees publish. Fisher later proved his guess exact and gave the curve its letter. The alias story is in [[Stories/Inventing Variance]]; the point here is that the small sample was not a textbook simplification — it was the *cost constraint of a real factory*.
- **Before and after — the paired design as medicine's workhorse.** Measure the same patients before and after a treatment, and the paired $t$ is the standard first analysis: blood pressure, reaction time, a symptom score. It works for exactly the reason engine 2's case shows — patients differ from one another far more than a treatment changes any one of them, and pairing removes that spread. Almost every "significant improvement" you read in a small clinical or psychology study is a $t$ statistic on differences.
- **A/B testing.** Every dashboard that reports whether version B of a web page beat version A is running a two-sample test on means (or proportions) — and the default engine in that industry is the *unequal-variance* form, Welch's $t$ (below), because nobody assumes two live populations share a variance. The nightly decision "ship B / keep A" is this card's engine 4, run millions of times a day, with the same one-tailed-versus-two-tailed discipline and the same temptation to peek at the data before choosing the tail that [[Hypothesis Tests]] warns about.
- **Benchmarking anything.** Two versions of a program timed on the same set of inputs; two models scored on the same test questions — that is a *paired* comparison, and the paired $t$ (or its non-parametric cousin) is the honest way to say whether one really beats the other rather than merely won a coin flip. Reporting an "improvement" without it is the most common statistical sin in technical writing.

The honest edge is the parent card's: a significant $t$ says the effect is *detectable*, not that it is *large*. Nine athletes improved by four seconds; whether four seconds matters is a coaching question, and no table answers it.

## Common Misconceptions (Teaching Notes)

### 1. Using $z$ (1.96) with $s$ on a small sample

The most common slip, and it is invisible in the working — the numbers look fine.

**Fix:** the flag is *"$\sigma$ unknown, $n$ small, normal population"* → $t$. And make the cost concrete: at $n = 5$ the honest critical value is $2.78$, not $1.96$ — a student using $1.96$ is claiming 95% confidence and delivering roughly 88%. The ladder table above is the antidote.

### 2. Running a two-sample test on paired data

Two columns of numbers *look* like two samples, and the two-sample formula is longer, so it feels more rigorous.

**Fix:** Engine 2's own case. The two-sample $t$ on the athletes gives $0.30$ (nothing); the paired $t$ gives $2.39$ (significant). Same data — the wrong design threw away the signal, because it compared a four-second change against an eighty-second spread between runners. Ask *"the same individuals twice?"* before touching a formula.

### 3. Degrees of freedom $= n$

**Fix:** one constraint per estimated mean. One sample: $n - 1$. Two pooled samples: $(n_1 - 1) + (n_2 - 1) = n_1 + n_2 - 2$. Paired: $n - 1$, where $n$ is the number of *pairs*, not the number of measurements. Then check it against the row you read from the table — reading $\nu = 10$ for a sample of ten is the classic version of this slip.

### 4. Pooling when the variances are not assumed equal

Pooling is a *claim*: that both samples estimate one common $\sigma^2$. Engine 4's case (the bananas) has a mark scheme that scored a pooled attempt **A0**.

**Fix:** the phrase to look for is in the question — *"assume … the same population variance"* licenses $s_p^2$; *"do not assume …"* forbids it and, for large samples, sends you to $s_1^2/n_1 + s_2^2/n_2$.

### 5. Forgetting to write the assumption

The normality assumption is a **B1 mark** in interval questions ("stating any assumptions"), and it is the thing that makes the $t$-table the right table.

**Fix:** write it as a sentence, in context, naming the *population*: "the population of estimates / differences is normally distributed". Not "the data are normal" — the sample is what it is; the assumption is about where it came from.

### 6. "There is a 95% probability that $\mu$ lies in $[82.3, 86.5]$"

The parent card's misconception, still alive here.

**Fix:** recall from [[Sampling and Estimation]] — the *method* catches $\mu$ 95% of the time; *this* interval either did or did not. The 95% belongs to the procedure, not to the interval you happen to hold.

## Exam Notes

### Cambridge 9231 — Further Probability & Statistics, §4.2

Five learning objectives, and every recent Paper 4 examines the section, typically 5–8 marks per part in one or two questions:

- **One-sample $t$-test and $t$-interval** — small sample, normal population, unknown variance. Intervals from *raw data* (engine 1's case) require the unbiased $s^2$ from $\sum x, \sum x^2$; the **$t$-value seen** earns its own B1, and **stating the assumption** (normal population / random sample) is a separately marked line when the question says "stating any assumptions".
- **Pooled estimate of variance** from two samples — the syllabus note says raw *or summarised* data; summarised is the norm (engine 3's case), and MF19 prints the $\sum(x-\bar{x})^2$ form.
- **Difference of means — select the test:** paired $t$, two-sample pooled $t$, or the normal engine. The syllabus states outright that "the ability to select the test appropriate to the circumstances of a problem is expected", and the papers test it by *telling* you the variance situation (engine 3's case says assume equal; engine 4's says do not) and by *not* telling you the data are paired (engine 2's case — you must see it).
- **Confidence intervals** for a mean and for a difference of means, by $t$ or by normal "as appropriate", and the one-mark follow-up that reads an interval as a test (zero inside → not significant at the matching level).
- **The follow-up sting** in engine 2's case — "why might this test be inappropriate, and what would you use instead" — bridges straight into §4.4: the answer is always *the population (of differences) may not be normal* → a sign or Wilcoxon test.
- **Hypotheses must name the population parameter** ($\mu$, $\mu_d$, $\mu_X - \mu_Y$); mark schemes note "if in words, must contain 'population'". Conclusions in context, non-assertively — the parent card's discipline, unchanged.

### AP Statistics — Unit 7, Inference for Quantitative Data: Means

The same tools with two cultural differences worth knowing. AP builds the one-sample $t$-interval and $t$-test, the two-sample $t$, and the paired $t$ ("a one-sample $t$ on the differences"), always with the **conditions** stated — random, the 10% condition for sampling without replacement, and normal population *or* $n \geq 30$ *or* a plot with no strong skew or outliers. And AP's two-sample procedure is the **unpooled** (Welch) form with technology-computed degrees of freedom; the College Board explicitly discourages pooling. So a Cambridge student switching boards should stop pooling, and an AP student switching to 9231 must learn to.

### IB Mathematics: Applications and Interpretation

$t$-tests live in **AI, at both SL and HL** — the two-sample $t$ with the $p$-value read from the GDC, hypotheses and tails set up by hand, and at HL the one-sample test for a mean with unknown variance. The calculator does the arithmetic; the marks are for hypotheses, tails, and the conclusion. **AA has no hypothesis testing at all** — for an AA student this card is enrichment their AI classmates sit exams on.

### Where it is *not* examined

**Cambridge 9709** stops at the parent cards' $z$-tests and large-sample intervals — its own fine print ("$\sigma$ known or $n$ large") is precisely the boundary this card crosses. **Edexcel IAL** states in its S3 unit that "a knowledge of the $t$-distribution is not required". **OxAQA 9660**, **0580**, **0606** and **IB AA** have none of it.

### Beyond high school — University

Every introductory statistics course runs on this card for a term; the additions are Welch's unequal-variance $t$ (below), the $F$-test for whether two variances are equal (which is why 9231 politely tells you to *assume* it), the ANOVA that generalises the two-sample $t$ to many groups, and — increasingly — the honest question of *effect size* alongside significance.

> [!info] Beyond syllabus — Welch's $t$: two small samples, variances not assumed equal
> Recall engine 4's statistic, $\dfrac{\bar{x}-\bar{y}}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$. For **large** samples it is normal. For **small** samples with unequal variances it is approximately $t$, but with a fractional number of degrees of freedom given by the Welch–Satterthwaite formula
> $$\nu \approx \frac{\left(\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1 - 1} + \dfrac{(s_2^2/n_2)^2}{n_2 - 1}},$$
> which lands somewhere between the smaller of $n_1 - 1$, $n_2 - 1$ and their sum. This is what every statistics package and every A/B-testing tool runs by default, and it is the AP procedure. Cambridge sidesteps it by always either *granting* equal variances (pool) or *granting* large samples (normal) — the two cases where no approximate $\nu$ is needed.

> [!info] Beyond syllabus — how robust is it, and what to do when it isn't
> The normality assumption is less fragile than it sounds: for moderate $n$ the sample mean is close to normal whatever the population (the CLT again), so the $t$-test tolerates mild skew. What breaks it is what broke engine 2's case — differences that are not draws from one distribution, heavy outliers, or a sample so small that no plot can reassure you. The escape routes are the rank-based tests of [[Non-Parametric Tests]], which trade some power for freedom from the normal assumption, and the bootstrap of [[Sampling and Estimation]]'s Beyond section, which builds the reference distribution from the sample itself.

## Connections

- **Parents:** [[Hypothesis Tests]] — the five-step ritual, tails from the claim, and the conclusion discipline, all reused verbatim; [[Sampling and Estimation]] — the standard error, the unbiased $s^2$ with its $n-1$, and the interval whose fine print this card removes.
- **Engine underneath:** [[Normal Distribution]] — the $t$-curve is the normal with the wobble of $s$ priced in, and returns to it as $\nu \to \infty$; [[Linear Combinations of Random Variables]] — why the two-sample standard error adds variances.
- **Continues in:** [[Chi-Squared Tests]] — the distribution already hiding in the $t$-statistic's denominator, examined in its own right; [[Non-Parametric Tests]] — the fallback the exam asks you to name when the normal assumption fails.
- **The story:** [[Stories/Inventing Variance]] — Gosset, the brewery, and the alias.
- **Neighbour:** [[Repeated Measurements]] — the physics lab is the one-sample $t$-interval in a lab coat: a few repeats, a mean, and an honest error bar.
- **For 9231 students:** [[MF19 Reference (9231)]] — everything *around* the tests is printed: the unbiased $s^2$, the pooled-variance formula, the $t$-table and the normal table. What is not printed is the test statistics themselves and the decision of which one to use — which is exactly where the marks are.
- **Story partner:** [[Stories/The Lady Tasting Tea|The Lady Tasting Tea]] — Gosset the brewer as the only man Pearson and Fisher would both listen to; Fisher's 1912 proof, and why the percentage-point table format exists at all.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $t_\nu$ | `t_\nu` | $t$-distribution with $\nu$ degrees of freedom |
| $\nu$ | `\nu` | degrees of freedom |
| $\bar{x} \pm t_{n-1}(p)\,\dfrac{s}{\sqrt{n}}$ | `\bar{x} \pm t_{n-1}(p)\,\dfrac{s}{\sqrt{n}}` | one-sample $t$-interval |
| $s_p^2$ | `s_p^2` | pooled variance |
| $\bar{d}$, $s_d$ | `\bar{d}`, `s_d` | mean and s.d. of paired differences |
| $\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$ | `\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}` | two-sample standard error, unpooled |
| $\mu_d$ | `\mu_d` | population mean difference |
