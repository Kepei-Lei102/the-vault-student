---
chinese: 为什么要学概率统计 (wèishéme yào xué gàilǜ tǒngjì)
prerequisites:
  - "[[Probability Basics]]"
  - "[[Discrete Random Variables]]"
  - "[[Forward Reading and Problem Discovery]]"
leads_to:
  - "[[Normal Distribution]]"
  - "[[Poisson Distribution]]"
  - "[[Stories/Inventing Variance]]"
  - "[[Inventing Variance]]"
  - "[[The Lady Tasting Tea]]"
tags:
  - subject/mathematics
  - subject/philosophy
  - domain/probability
  - domain/statistics
  - domain/epistemology
  - level/A-Level
  - level/IB
  - level/AP
  - level/life
  - type/methodology
  - type/meta
  - type/philosophical
  - misconception/numbers-dont-lie
  - misconception/normal-distribution-as-belief
  - misconception/correlation-implies-causation
---

# Why Probability and Statistics? 为什么要学概率统计？

> *"Numbers don't lie." Wrong — numbers lie all the time. Statistics lie even more.*
>
> *That's not a reason to abandon them. It's the reason to learn them well.*

## What this card is for

Every probability or statistics card you'll meet in the vault — [[Probability Basics]], [[Discrete Random Variables]], [[Normal Distribution]], the works — teaches you a *tool*. This card is the meta-card that asks the dual question:

1. **Why do these tools matter?** What problem do they solve, and why did human beings invent them in the form we now study?
2. **When don't they matter — or worse, when do they lie?** Statistics is famously the discipline most likely to mislead, and a hunter (in the sense of [[Forward Reading and Problem Discovery]]) needs to know when to trust the summary and when to ignore it in favour of a causal trace.

The point isn't to argue *for* or *against* probability and statistics. They're indispensable — you cannot reason about uncertain worlds without them. The point is to hold them as **tools**, not **beliefs**, and to know which mode you're in at any given moment.

> [!info] Connection to the hunter card
> [[Forward Reading and Problem Discovery]] argued that *a hunter is someone who can constantly trace causality.* Statistics often *replaces* causal tracing with summarised data — which is wonderful when data is what you have, and dangerous when it makes you forget the trace. The deepest insight of statistical literacy is knowing the difference. Stats lie; causality tends not to. But you cannot learn causality without prob and stats — they are the language for talking about uncertain causes and their effects in a world full of noise.

### 中文锚点

**概率与统计** = 处理「不确定事件」的两件工具。

- **概率 (gàilǜ)** — 在 *知道* 事情怎么发生的前提下，计算各种结果的可能性。"假设硬币是公平的，连续投十次中正面出现 7 次的概率是多少？"
- **统计 (tǒngjì)** — 反过来：从 *观察到的数据* 推断事情怎么发生的。"我看到这枚硬币十次有七次正面，它公平吗？"

为什么要学：

- **它们让我们能在不确定中讲清道理。** 不学，就只能凭直觉。直觉错的次数比你以为的多得多。

为什么也要警惕：

- **统计可能撒谎，因果通常不会。** 一个聪明的猎人（[[Forward Reading and Problem Discovery]]）会问：「这个统计数字有没有把信息扔了？参考系是什么？我看不到的数据在哪里？」
- **是工具，不是信仰。** 该用就用，不该用就放下。

---

# Part I — Why they matter

## The invention of variance — and why it took 200 years to land

The mean $E(X)$ tells you the average of a distribution. Average isn't enough. Two distributions can have the *same average* and feel completely different — one tightly clustered around the mean, the other wildly spread.

> **Two distributions, same mean, very different spreads.**
>
> Distribution A: $X \in \{4, 5, 6\}$, each with probability $\tfrac{1}{3}$. $E(X) = 5$.
>
> Distribution B: $X \in \{0, 5, 10\}$, each with probability $\tfrac{1}{3}$. $E(X) = 5$.
>
> Same mean. Wildly different feel. Whatever number you build to capture *that* difference is what statistics calls **variance**.

The natural candidates for "spread" are:

1. **Range** = $\max - \min$. Cheap, but throws away everything between the extremes and is hostage to outliers.
2. **Mean absolute deviation** = $E(|X - \mu|)$. Conceptually clean — average distance from the mean.
3. **Mean squared deviation** = $E((X-\mu)^2)$ — the **variance**.

Why did statistics settle on the third? Two structural reasons that took a century to crystallise:

**1. Differentiability.** $|x|$ has a kink at $x = 0$ where the derivative is undefined. $x^2$ is smooth everywhere. The moment you start *optimising* anything — fitting a line to data, finding the maximum-likelihood estimator, training a neural network — you'll be differentiating. Squared deviation differentiates cleanly; absolute deviation breaks. The whole edifice of regression, machine learning, and statistical inference is built on the differentiability of squared error.

**2. Additivity under independence.** Variances *add*: for independent $X$ and $Y$,
$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y).$$
Mean absolute deviations *don't* add — there's no clean rule for $E(|X + Y - \mu_X - \mu_Y|)$. The additivity-under-independence is what powers the **Central Limit Theorem** (sums of independent variables → normal) and pretty much all of statistical inference. Variance is the right currency precisely *because* it adds.

### A short history

- **Gauss (1809)** and **Laplace (1810)**, working on astronomical orbit fitting, settled on minimising the *sum of squared errors*. Squared errors weren't picked for philosophical reasons — they were picked because the resulting equations (the **normal equations**) were *solvable in closed form*. The choice was pragmatic, and it stuck.
- **Karl Pearson (1893)** coined the term **"standard deviation"** — the square-rooted version. The point of the square root: $\sigma = \sqrt{\text{Var}(X)}$ has the same units as $X$, which makes it interpretable. Variance lives in $X^2$ units (variance of "heads count" is "(heads)²" — meaningless physically), but standard deviation is back in heads.
- **R. A. Fisher (1918)** then formally named the squared quantity **"variance"** in *Studies in Crop Variation*, and made it the central object of his theory of estimation.

So: **variance is what you compute, standard deviation is what you report.** Variance is the load-bearing object — it adds under independence, it differentiates cleanly. Standard deviation is the human-readable output — it has the right units, it's interpretable as "typical deviation from the mean".

The fact that the right quantity wasn't obvious — and took ~110 years from Gauss to Fisher to crystallise — is the lesson. Even seemingly fundamental statistical concepts are *engineered*, with multiple plausible candidates, and the winner is the one that proves most useful downstream. Variance won because it played nicely with calculus and it added.

> [!tip] The full drama
> Ceres lost and found, the wounded Frenchman, the threepenny measuring lab and its shadow, the Pearson–Fisher war — the human story behind this section lives at [[Stories/Inventing Variance]].

---

## The binomial is the English of probability

The **binomial distribution** $B(n, p)$ counts successes in $n$ independent trials each with success probability $p$. See [[Discrete Random Variables]] for the formal treatment. The question this section asks is: *why does it deserve its central place in every introductory probability course, given that its four conditions* (fixed $n$, two outcomes, constant $p$, independence) *are restrictive in the real world?*

**1. It's the simplest non-trivial DRV.** Once you have a distribution with parameters, you want to know its mean and variance. The binomial is where those concepts get their first non-trivial workout. Anything subsequent (Poisson, geometric, normal) is taught by *contrast* with the binomial — "this is what you do when condition X fails" — so the binomial is the *reference point*. You can't really understand "what makes Poisson different" until you understand what binomial *is*.

**2. It's the building block for everything else.** Many of the distributions you'll meet in P5, P6, IB AA, and AP Statistics are limits or extensions of the binomial:

- **Poisson** = binomial with $n \to \infty$, $p \to 0$, $np = \lambda$ fixed. Models event counts when there's no natural $n$. (See *Euler's number on the doorstep* below — this limit is where $e$ shows up.)
- **Normal approximation to binomial** = binomial with large $n$, by the Central Limit Theorem. The normal-distribution approximation is itself a P5/P6 topic, and the binomial is the test case where you first meet it.
- **Geometric** is the "until the first success" reframing of the same Bernoulli trials.
- **Negative binomial** (beyond syllabus) is the "until the $r$-th success" extension.

Master the binomial and the rest mostly fall out by adapting the same indicator-variable / linearity machinery.

**3. The four conditions are pedagogical, not just computational.** They force you to *think* about whether the binomial model is appropriate before you apply the formula. The single most common mistake on real probability problems is *not* arithmetic — it's applying binomial when independence has already broken. Cambridge dwells on the binomial first because it teaches the discipline of "stop and check the conditions." Years later, when you're modelling a real-world process, the four-conditions check is the habit that saves you.

**4. Real-world applications dominate, despite the restrictions.**

- **A/B testing in tech.** $n$ users see version A or B; each independently has probability $p$ of converting. Independence is *exactly true* under random assignment. Every product team that ever ran a feature experiment used a binomial.
- **Opinion polling.** $n$ people sampled, each with probability $p$ of voting Yes. When the sample is small relative to the population, "without replacement" is approximately independent — the difference from binomial is negligible.
- **Manufacturing quality control.** $n$ items inspected, constant defect rate $p$. The four conditions hold *exactly*. The whole field of statistical quality control was built on the binomial.
- **Drug efficacy trials.** $n$ patients, each independently has probability $p$ of responding to treatment. The binomial sets the null-hypothesis baseline against which the drug effect is measured.
- **Genetics.** Number of offspring inheriting a recessive allele — exact Bernoulli trials.

The four conditions are restrictive in *theory*; in *practice* an enormous slice of real problems either fits them exactly, fits them well-enough-to-be-useful, or motivates the next-level distribution by failing one specific condition (with the binomial as the reference point for that failure).

> [!tip] Pedagogical bottom line
> The binomial is the **English of probability** — not the most expressive language, but the one everyone speaks first, the one that opens the door to every other distribution, and the one that handles a startling fraction of real-world problems exactly. Spend time with it. The four conditions are not bureaucratic; they're the calibration of your real-world modelling instinct.

---

## Euler's number on the doorstep

Here's a fact that connects the binomial section above to [[Euler's Number]]: *the most fundamental constant in calculus shows up at the centre of probability, and it does so via the binomial distribution.*

Start with a binomial $B(n, p)$ where $n$ is large and $p$ is small, and let $\lambda = np$ stay fixed as $n$ grows. Then the probability of zero successes is:
$$P(X = 0) = (1 - p)^n = \left(1 - \frac{\lambda}{n}\right)^n$$

Take the limit as $n \to \infty$ with $\lambda$ fixed. This is one of the standard limit-definitions of $e$:
$$\lim_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^n = e^{-\lambda}$$

So as the binomial gets large-$n$, small-$p$, fixed-$np$, the probability of zero successes converges to $e^{-\lambda}$ — and the same calculation for *any* $k$ gives:
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \xrightarrow{n \to \infty} \frac{\lambda^k}{k!} e^{-\lambda}$$

That right-hand side is the **Poisson distribution** — and it carries Euler's number $e$ in its very PMF. The Poisson is what the binomial *becomes* in the limit of "many independent trials with low probability each". $e$ shows up because the limit definition $e = \lim_n (1 + 1/n)^n$ is hidden inside the binomial's $(1-p)^n$ factor.

> [!info] The 37% rule
> The simplest non-trivial case: take $\lambda = 1$, so $p = 1/n$. Then the probability of *zero* successes in $n$ trials each with probability $1/n$ is approximately $1/e \approx 0.368$. **About 37%, regardless of $n$, for large $n$.**
>
> This number appears all over the place:
>
> - **Derangements.** If $n$ people put their hats in a pile and a random person picks one, the probability that *nobody* gets their own hat back is $\to 1/e$ as $n$ grows. (Try this with friends; it's surprisingly close to $1/e$ even for small $n$.)
> - **The secretary problem.** Optimal stopping rule: interview the first $n/e$ candidates as a benchmark, then take the first one who beats them all. The 37% threshold.
> - **Marriage / job-hunt versions of the secretary problem** — same answer.
>
> Whenever you see $1/e$ in probability, there's a hidden binomial-becoming-Poisson somewhere underneath.

This is the kind of fact that makes the *delight* case for probability: a constant from calculus, the most fundamental number after $\pi$, *lives* in probability. It didn't have to. It does because the structure of "many small chances" is mathematically the same as the structure of "smooth continuous growth" — and $e$ is the bridge.

---

# Part II — Why they don't always matter

If statistics were a perfect tool, the previous section would be the whole card. But they're not; they're a tool with sharp edges, and a hunter ([[Forward Reading and Problem Discovery]]) needs to know where the edges are.

## The hunter test — stats lie, causality tends not to

A statistic is a **summary** — a single number (or a small set of numbers) that has thrown away most of the information in the data. The throwing-away is the *point* (you can't carry the whole dataset in your head), but the throwing-away is also where the lying happens. The summary always loses something, and what it loses is sometimes exactly what mattered.

A causal trace is a **reading** — a step-by-step accounting of what produced what. It throws away less; it carries more of the structure. A reading is harder to construct (you need to actually understand the mechanism, not just measure outcomes), but once you have it, it tends not to lie. You can check it against new evidence; you can extend it to new cases; you can be wrong about it but you can also be *demonstrably* wrong, which is itself a kind of strength.

So the rule:

> **A statistic is a summary; it has thrown information away. A causal reading is a trace; it carries the structure. Stats lie when the discarded information was the load-bearing piece. Causal readings lie much less often — and when they do, they're easier to falsify.**

This is the hunter's bias. Be skeptical of any number stripped of its generating process. Ask: *what was thrown away to produce this summary?*

> [!info] Further reading — Judea Pearl's *The Book of Why* (2018)
> If the stats-lie / causality-doesn't framing lands for you, the next book to read is **Judea Pearl and Dana Mackenzie, *The Book of Why* (2018)** — a popular-science introduction to *causal inference*, the branch of statistics that tries to do exactly what this section is asking for. Pearl's central idea is the **ladder of causation**: three rungs of increasingly strong claims about uncertain worlds.
>
> 1. **Association** — what statistical correlation finds. *"People with feature X also tend to have outcome Y."* Most undergraduate statistics never leaves rung one.
> 2. **Intervention** — what would happen *if I changed* something. *"If I gave people drug X, would Y happen?"* This is what randomised controlled trials answer; correlation alone can't.
> 3. **Counterfactual** — what *would have* happened in a world that didn't occur. *"Would patient A have recovered if they hadn't taken drug X?"* The hardest rung; the one that requires explicit causal models.
>
> The Book of Why argues that ordinary statistics has been stuck on rung one for almost a century — and that almost every claim that "correlation isn't causation, so don't say anything" was a giving-up rather than a *technical limit*. Pearl developed **do-calculus** as the formal machinery for climbing the ladder. *The Book of Why* makes the case accessibly; the formal proof of do-calculus and the mathematical machinery live in his earlier book *Causality* (2000) — referenced from [[Forward Reading and Problem Discovery]] as the technical companion. Read *The Book of Why* first; it gives you the language. *Causality* is where the language gets formal.

> [!info] Beyond syllabus — what counts as "causal"?
> *Recall that conditional probability $P(Y \mid X)$ from [[Conditional Probability]] reads as "the probability of $Y$ given that we have observed $X$"* — passive observation, not action. Pearl's framework adds two new objects that look similar but are mathematically distinct from this conditional:
>
> - $P(Y \mid X)$ — **conditional probability**: what we observe in the data when $X$ happens to occur. *Standard probability theory has only this.*
> - $P(Y \mid \text{do}(X))$ — **interventional probability**: what would happen *if we intervened* and set $X$ ourselves. The do-operator is what randomised controlled trials measure.
> - **Counterfactual probability**: what *would have* happened in a world where $X$ had taken a different value, holding everything else fixed. The hardest object; requires explicit causal models.
>
> The do-operator and counterfactual operators are the formal additions Pearl built. **Most "stats lie" cases reduce to confusing $P(Y \mid X)$ with $P(Y \mid \text{do}(X))$.** Simpson's paradox in the Berkeley admissions case (next section) is exactly this confusion: the conditional $P(\text{admitted} \mid \text{female})$ disagreed with the interventional $P(\text{admitted} \mid \text{do}(\text{female}))$ — because gender was correlated with department choice, which was the actual driver. The math is now in textbooks; it took 60 years for statistics to catch up to that distinction.

---

## The reference-frame problem — human height as a normal distribution

Here's a question that breaks people's faith in normal distributions:

> *"Are humans of average height? Or are we tall, or short?"*

The naive answer: humans are roughly in the middle of a normal distribution centred around ~1.7 m, so we're near average.

The correct answer: **it depends entirely on what reference class you're including.**

- Among **all adult humans**: yes, you're somewhere on a roughly-normal distribution centred at ~1.7 m. Most people are within 10 cm of the mean. Normal-distribution intuition is fine.
- Among **all mammals**: humans are a bit on the taller side of the mammal distribution (mice and shrews pulling the mass to the small end), but still recognisably "in the spread".
- Among **all life including bacteria, viruses, single-celled organisms**: humans are *extreme outliers on the right*. Most life on Earth is microscopic. By count of organisms or by count of species, the typical "living thing" is microscopic. A human is *gigantic* on this distribution — many orders of magnitude beyond the mean.

Three different "shapes of the distribution", three different positions for the *exact same datapoint* (a human). The shape did not change because of any property of humans; it changed because of *what you decided to include in the reference class*.

> [!info] The lesson
> **A normal-distribution claim is a claim about a specific reference frame. It does not survive a change of frame.** When someone tells you "this is normally distributed", the next question is *"distributed across what?"*. If they can't answer, the claim is empty. If they can, you've learned the actual structure of the situation.
>
> This is the hunter's instinct again: trace the causality of *which reference class produced this distribution*. The distribution is downstream of the framing. The framing is the load-bearing decision.

This problem is most lethal when the reference frame is *implicit*. Most claims of the form "X is normally distributed" silently assume a reference class, and that assumption — not the math — is what's actually being claimed. Examples in the wild:

- **"IQ is normally distributed."** — In which population? Across what test? IQ is *constructed* to be normally distributed by design (the test is calibrated against a reference population), so the normality is not a discovery but a definition. Change the population, change the calibration, and the shape changes.
- **"Heights are normally distributed."** — Across which population? Adult males, adult females, all adults, all humans worldwide, including children, including stunting? Each gives a different distribution.
- **"Stock returns are normally distributed."** — Famously not. They have **fat tails** (more extreme events than a normal predicts). The 2008 financial crisis happened in part because risk models *assumed* normality, and the tail events that destroyed those models were dismissed as "10-sigma events" (which under a true normal would happen once in the lifetime of the universe). The claim survived; the assumption didn't.

When a stat is presented stripped of its reference frame, it has hidden a critical piece of information. *That* is when stats lie.

---

## Three classic stats lies

A short tour of cases where a perfectly correct statistical statement misleads, because a hunter wasn't watching what got thrown away.

### Lie 1 — Survivorship bias (Wald's bombers)

In World War II, Allied bombers came back from missions with bullet holes concentrated in certain areas of the fuselage and wings. The naive engineer's instinct: *armour those areas, that's where the planes are getting hit.*

**Abraham Wald** (1943) pointed out the lie: the data was from planes that *came back*. The planes that didn't come back — the ones that got shot down — had been hit elsewhere (engines, cockpit). The "bullet holes" data was from a heavily filtered sample, and the conclusion was the *opposite* of what the data appeared to suggest. **Armour the areas with no bullet holes**, because that's where the lethal hits land.

The lie: a perfectly accurate count of bullet holes, applied without thinking about the *generating process*, gave the wrong answer. The hunter's question — *whose data is this, and whose data am I missing?* — would have caught it.

### Lie 2 — Simpson's paradox (Berkeley admissions)

In 1973, the University of California, Berkeley graduate program admissions data showed a striking pattern: **men were admitted at a higher rate than women** overall, raising allegations of gender bias.

When the data was broken down by department, however, the pattern reversed: **in most individual departments, women were admitted at equal or higher rates than men.** How can both be true?

The answer: women applied disproportionately to *more competitive* departments (lower acceptance rates for everyone), while men applied disproportionately to less competitive ones. The aggregate "men > women" was a confound — averaging over the structure of departmental competitiveness. The within-department comparison (which is the causally meaningful one) showed no bias against women.

This is **Simpson's paradox**: an aggregate trend can reverse when you condition on a relevant subgroup. Both numbers were statistically correct; the lie was in *which one you took as causally meaningful*. The aggregate was a summary that had thrown away the department-choice information, which was the load-bearing piece.

### Lie 3 — The mean is not the typical

A statistician walks into a bar. The bar's average customer income is $250,000. Then Jeff Bezos walks in. The average customer income is now $5 billion. Has the bar gotten richer? **No — most customers are still poor.** The mean has shifted, but the *typical* customer is unchanged.

This is the lie of **the mean as a summary of the typical**. Means are easy to compute and easy to interpret as *the average person*, but for distributions that are skewed (income, wealth, city sizes, paper citations, internet-user attention spans, online video views), the mean is dominated by the right tail and tells you almost nothing about the typical case. The **median** is much better as a "typical" — half are above, half below, and a single billionaire walking in doesn't move it.

The "average person has 1.99 testicles" line is a comedic version. Real cases include:

- "Average household income" in the US is misleading because of the long right tail. The *median* household income is much lower and is what most households experience.
- "Average paper citation count" in a field is dominated by a handful of mega-cited papers; the *median* paper has a small fraction of the citations.
- "Average video view count on YouTube" is dominated by viral hits; the median is approximately zero views.

A hunter asks not "what's the average?" but "what's the *shape* of the distribution? what's the median? what does the long tail look like?" Then the average becomes interpretable, instead of misleading.

---

## Tools, not beliefs

The summary of all of this:

> **Probability and statistics are tools. Use them when they help. Set them down when they don't. Never confuse fluency with the tool for *belief* in what the tool produced.**

Statistical literacy is *not* the same as statistical worship. The literate person:

- Uses stats as the right hammer for many nails — election forecasting, A/B testing, drug efficacy, quality control.
- Demands the reference frame be made explicit before believing a distributional claim.
- Asks "what was thrown away to produce this summary?" before trusting it.
- Distinguishes a stat (which lies in predictable ways) from a causal trace (which usually doesn't).
- Knows which mode they're in. Sometimes data is what you have; lean on stats. Sometimes the causal mechanism is what you have; lean on the trace. Sometimes both; use them together.

The illiterate person believes the number because it has decimal places.

---

# When to use which — a pragmatic decision rule

A short decision tree for when to reach for stats and when to reach for a causal trace:

| Situation | Lead with | Why |
|---|---|---|
| You have lots of data, no clear mechanism | **Statistics** | Stats can find the regularities first; mechanism comes later. |
| You have a clear mechanism, sparse data | **Causal trace** | The mechanism predicts the data; verify against what data you have, but the trace leads. |
| You have both | **Both, in conversation** | Use the trace to predict; use the stats to test. This is the scientific method in its strongest form. |
| You have neither | **Don't make the claim.** | "I don't know" is the only honest answer. Most armchair pundits skip this option. |

The hunter's preference in any of these cells is to **read forward** — collect every clue (data, mechanism, structural detail), grab every invariant, and let the answer light up. Statistics is one of the most powerful clue-collection tools ever built. It is also one of the most easily turned into a confidently-wrong-sounding belief. The discipline is *the same* as in [[Forward Reading and Problem Discovery]] — read what is, not what you wish was, and audit the wish whenever the answer is suspiciously convenient.

---

## The trace and the threshold — acting before causality is complete

There is a harder truth under all of the above, and it is worth saying plainly because it is where the hunter's spirit actually lives.

**Causality is traced, not possessed.** [[Forward Reading and Problem Discovery]] says a hunter is someone who can constantly trace causality — and every hunter knows the trace is never finished. You do not *have* the causal chain of a coin, a patient, a market or a jigsaw-solving child; you have a sample of what they did, and a story that fits it better or worse. Whether the world underneath is a dice game (as quantum mechanics says) or a clockwork you cannot see all of, your situation is the same: finite data, finite time, and a decision that will not wait for the trace to close. Possibility is not a defect a better theory will remove. It is the shape of *knowing from a sample*.

**And yet you act.** That is the second half of the sentence, and it is what a hypothesis test actually is. Look at what a significance level *does* in [[Hypothesis Tests]] and its descendants: it does not tell you the median salary *is* or *is not* $\$32{,}500$; it names the amount of coincidence you are willing to act on. In [[Non-Parametric Tests]] the same fifteen salaries are "not surprising enough" at 10% and would be "surprising enough" at 15% — nothing about the evidence changed between those two sentences ($0.0592$ both times); only the price you set on being fooled. Students meet that seam and ask *but which is the real answer?* — and the honest reply is that the question has two parts they have been taught to fuse: what the data show (fixed) and what you will do about it (chosen). Neyman and Pearson built the whole theory of testing on exactly this, and were disliked for it: a test is a *rule for acting* that behaves well over the long run of decisions, not an oracle for any one of them.

**"Fail to reject" is awkward on purpose.** English does not have a graceful verb for "I looked, and I am not yet surprised". The clumsy phrase, and the exam's *sufficient / insufficient evidence at 5% that…*, are awkward because they refuse to claim what the test does not know. The words that feel better — *prove*, *accept*, *the median is now* — all claim more, and every board's mark scheme penalises them for the same reason a hunter would: they end the trace early. Medicine, courts and engineering tolerances all end up speaking in this clumsy dialect, because they all act on samples of a world they cannot fully see. A student who finds *likely* and *seems* uncomfortable in a conclusion has understood the epistemics; the discomfort is not a vocabulary problem to fix but the correct feeling to keep.

So the hunter's spirit is not "find the cause and then act". It is: **trace as far as the evidence goes, price how far it does not, act on the trace anyway — and keep tracing.** The significance level is that spirit written as a number.

---

## Counted, not measured — the statistics paper is thermodynamics for people

Walk the five Further Statistics cards in the order an exam board lists them — [[Continuous Random Variables]], [[t-Tests]], [[Chi-Squared Tests]], [[Non-Parametric Tests]], [[Probability Generating Functions]] — and something shows up that no syllabus put there. Each card, asked *why does this work?*, gives the same answer in a different costume: **count the ways an honest sample could have come out.**

- The $\chi^2$ curve is the pile of misfits that a *fair* die makes when you roll it sixty times, twenty thousand times over — it is not a law about dice, it is a record of how much honest data naturally misfit themselves.
- The Wilcoxon tables are not measured; they are counted — $2^6 = 64$ sign patterns, $\binom{6}{3} = 20$ hands, $\binom{14}{6} = 3003$ deals — every one equally likely under the hypothesis, so the critical value is a tally, not a fit.
- The sign test is $n$ fair coins, and the sample-of-ten split *dangles around five–five* because most of the $2^{10}$ patterns are near the middle.
- The PGF does the count by algebra: multiply two polynomials and the coefficient of $t^7$ has collected, without your help, the six ways two dice make seven.

That sentence — *the probability of a shape is the number of ways it can happen, out of all the ways there are* — is Boltzmann's tombstone with the constant removed: $S = k \ln W$, entropy as the logarithm of the count of microstates ([[Stories/Boltzmann's Tombstone]], [[Entropy and the Second Law]]). The "honest die" pile smoothing into Pearson's curve as the trials climb is the same fact seen from the other end: repetition does not create disorder, it reveals the one shape that almost all the ways share. A gas relaxes to the Maxwell–Boltzmann curve and a thousand fair dice relax to $\chi^2_5$ for the same reason — not because anything pushes them there, but because that is where nearly every arrangement already is. *Heat* is the name physics gives to the count; *the null distribution* is the name statistics gives to it; the count is the same.

And the verdict a test delivers — not "the median *is* 8" but "this sample is a $1.8\%$ coincidence if it were" — is the posture physics was forced into a century ago: the world answers in probabilities, the observer sets a threshold and acts (the section above). Statistics did not borrow this from quantum mechanics; both borrowed it from counting.

None of this was in the syllabus that ordered the cards. It emerged because each was written *full* — followed to where the idea actually lives rather than stopping at the mark scheme — and the idea, followed from five different doors, turned out to live in one room. That is the strongest argument there is for writing every topic full, whichever exam happened to ask for it: **exams decide the order in which things get learned, never the content.** Learn the content full, and the order stops mattering; the connections assemble themselves, the way the curve does.

---

## Connections

- **Sibling — also in Meta/:** [[Forward Reading and Problem Discovery]] (the meta-card on tracing causality — *that* card is the pure-causal-trace side; this card is the trace-meets-data side; pair them), [[Choosing Effective Equations]] (the M1-applied form of the same forward-reading skill), [[Chain of Thought]] (chain reasoning within a topic), [[Inertia and Bootstrapping]] (the execution-side companion — once you know *how* to think with stats and *what* a hunter does with them, you still have to start the act every morning; that card models the start as a Newton's First Law / activation-energy problem and offers the environmental-design corollary).
- **Foundational prerequisites:** [[Probability Basics]], [[Combined Probability]], [[Conditional Probability]], [[Permutations and Combinations]]. The basic axioms and combinatorics this card freely uses. (A note: these foundational cards are universal — even quantum mechanics uses the same probability axioms and combinatorial counting. Bose-Einstein, Fermi-Dirac, and Maxwell-Boltzmann statistics in physics are *literally* combinatorial counting under different distinguishability assumptions. The interpretation of *what probabilities mean* gets weird in QM, but the calculus of probability is the same. The whole of statistical mechanics is "count the ways" raised to a science — see [[Stories/Boltzmann's Tombstone]], where $S = k\log W$ is exactly that count.)
- **Where the threshold lives:** [[Hypothesis Tests]] (the five-step ritual and the significance level as the coincidence you agree to act on), [[Non-Parametric Tests]] (the salaries case whose verdict flips between 10% and 15% with the evidence unchanged — the trace-and-threshold seam made visible), [[t-Tests]] and [[Chi-Squared Tests]] (the same ritual with different engines).
- **Where the formulas this card philosophises about live:** [[Discrete Random Variables]] (variance, $E(X)$, binomial PMF, geometric PMF — the technical card), [[Normal Distribution]] (the most-cited and most-misused distribution in the world), [[Poisson Distribution]] (where Euler's number lives natively).
- **Where Euler's number lives:** [[Euler's Number]] (three definitions, irrationality proof, history), [[Exponential Function]] ($e^x$ as the function $f' = f$). The connection $\lim_n (1 - \lambda/n)^n = e^{-\lambda}$ in this card is the same limit definition shown in those cards, applied to probability.
- **For students taking 9709:** [[MF19 Reference (9709)]] — the formula-sheet audit. The technical formulas behind every statement in this card are listed there as "given" or "memorise" depending on the paper.
- **Cross-domain:** Survivorship bias, Simpson's paradox, mean-vs-typical confusions live everywhere data is summarised — public health, economics, sports analytics, AI evaluation, social science. The hunter's questions ("what was thrown away to produce this summary?", "what's the reference frame?") apply identically across all of them.
- **Story partner:** [[Stories/The Lady Tasting Tea|The Lady Tasting Tea]] — Fisher, Pearson, Gosset and Neyman: the people behind *the trace and the threshold*, and the Epilogue where the hunter stopped tracing.

---

## Coda — a teacher's note

I am a teacher, and I rarely memorise statistics. I use AI and the internet constantly. Students don't have those tools in the exam room — but they can learn the deeper habit, which is *not* memorising every formula, but *holding the tools loosely* and knowing when each one applies.

The vault's job, with respect to probability and statistics, is twofold:

1. **Build the technical fluency** — every distribution, every theorem, every worked example you'd need to pass the exam. (See [[Discrete Random Variables]], [[Normal Distribution]], the rest of the cluster.)
2. **Build the *philosophical immunity*** — the hunter's skepticism that prevents you from being misled by fluent statistics. *That* is what this card is for.

A student who finishes the cluster knowing the formulas but not this card will pass the exam, and then spend the rest of their life believing every number they read. A student who finishes knowing both will pass the exam *and* be able to read a research paper, a news article, a charts-and-numbers slide deck, a politician's claim, and ask the right question every time.

The exam is the smaller win.
