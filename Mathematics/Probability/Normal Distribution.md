---
chinese: 正态分布 (zhèngtài fēnbù)
prerequisites:
  - "[[Probability Basics]]"
  - "[[Discrete Random Variables]]"
  - "[[Why Probability and Statistics]]"
  - "[[Averages and Spread]]"
  - "[[Euler's Number]]"
leads_to:
  - "[[Poisson Distribution]]"
  - "[[Repeated Measurements]]"
  - "[[Linear Combinations of Random Variables]]"
  - "[[Continuous Random Variables]]"
  - "[[t-Tests]]"
  - "[[Chi-Squared Tests]]"
  - "[[Sampling and Estimation]]"
  - "[[Hypothesis Tests]]"
  - "[[Inventing Variance]]"
  - "[[The Naming of Normal]]"
  - "[[Non-Parametric Tests]]"
tags:
  - subject/mathematics
  - domain/probability
  - domain/statistics
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-5-5
  - type/distribution
  - type/methodology
  - notation/normal
  - misconception/normal-distribution-as-belief
  - misconception/standardisation-direction
  - misconception/forgetting-continuity-correction
---

# Normal Distribution 正态分布

> *The most-used and most-misused distribution in the world.*

## What this card is for

After [[Discrete Random Variables]] gave you the *discrete* count distributions (binomial and geometric), the next move is the **continuous** distribution that dominates statistical thinking — the **normal distribution**. The bell curve. The shape that shows up wherever many small independent influences add together.

This card teaches you the four exam-essential moves for 9709 P5 §5.5:

1. **Standardise** an $X \sim N(\mu, \sigma^2)$ to the standard normal $Z \sim N(0, 1)$.
2. **Compute probabilities** by reading the standard-normal CDF table $\Phi(z)$ — given to you on List MF19, page 10.
3. **Invert** — find $z$ from a given probability (also tabled on MF19).
4. **Approximate the binomial** with a normal when $n$ is large, applying the continuity correction.

This card also carries the warning from [[Why Probability and Statistics]]: the normal distribution is a *model*, not a *belief*. Many things are approximately normal; many things that everyone *thinks* are normal aren't. Knowing the difference is the difference between using the tool and being used by it.

> [!info] Where the normal lives in the syllabus
> 9709 P5 §5.5 is one row, but it's the row most students lose marks on — partly because the standardisation $Z = (X-\mu)/\sigma$ is *not* on MF19 (the table is, but not the formula that gets you to the table) and partly because the continuity correction in the binomial approximation is easy to forget. Both are flagged below.

### 中文锚点

**正态分布 (zhèngtài fēnbù)** = 正态分布、钟形曲线 (bell curve)。

**核心 4 步法** (P5 §5.5)：

1. **标准化 (biāozhǔnhuà)**：把 $X \sim N(\mu, \sigma^2)$ 化为 $Z \sim N(0, 1)$，公式：$Z = \dfrac{X - \mu}{\sigma}$。
2. **查表算概率**：用 MF19 上的 $\Phi(z)$ 表查出 $P(Z \le z)$。
3. **反查**：给出概率求 $z$，用 MF19 上的临界值表。
4. **二项近似**：$n$ 大时，$B(n, p) \approx N(np, np(1-p))$，连续性修正 ($\pm 0.5$)。

**警告**：正态分布是一个*模型*，不是*真理*。请配合 [[Why Probability and Statistics]] 一起看。

---

## The bell curve

The **probability density function** of the standard normal $Z \sim N(0, 1)$ is

$$\varphi(z) = \frac{1}{\sqrt{2\pi}}\,e^{-z^2/2}$$

For a general normal $X \sim N(\mu, \sigma^2)$:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

You don't compute with the PDF directly in the 9709 exam — the *cumulative* version $\Phi(z) = P(Z \le z)$ is what you'll actually use, via the MF19 table. But the PDF formula is worth knowing as the *shape* you're integrating under.

### Two parameters: $\mu$ (location) and $\sigma$ (spread)

The normal distribution is fully described by exactly two numbers:

- **$\mu$** — the **mean**, which is also the **median** and the **mode**. Sets the location of the peak.
- **$\sigma^2$** — the **variance** (and $\sigma$ is the **standard deviation**). Sets the spread.

Properties that fall out of the formula:

- **Symmetric about $\mu$.** $f(\mu + a) = f(\mu - a)$ for any $a$.
- **Inflection points at $\mu \pm \sigma$.** The curve flips from concave-down to concave-up exactly one standard deviation from the mean.
- **Total area = 1.** The normalising constant $\dfrac{1}{\sigma\sqrt{2\pi}}$ is exactly what's needed to make $\int_{-\infty}^{\infty} f(x)\,dx = 1$.

### The 68 — 95 — 99.7 rule

For any normal distribution:

$$P(\mu - \sigma \le X \le \mu + \sigma) \approx 0.683$$
$$P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 0.954$$
$$P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 0.997$$

**About 68% of the data falls within 1σ of the mean, 95% within 2σ, and 99.7% within 3σ.** This is one of the few "rules of thumb" worth memorising. It's a sanity check during the exam (does my answer plausibly fit the 68/95/99.7 buckets?) and it gives you intuition for *how unusual* a particular value is.

> [!tip] When someone says "5-sigma event"
> *5-sigma* means "5 standard deviations from the mean" — under a normal distribution, the probability of a value being 5σ away or further is about $5.7 \times 10^{-7}$, or 1 in 1.7 million. The Higgs boson discovery in 2012 used a 5-sigma threshold. **But this calculation only holds if the data is actually normal.** When financial models in 2008 said the crisis was a "10-sigma event" (probability $10^{-23}$, basically impossible in the lifetime of the universe), the right reaction wasn't *"how rare!"* — it was *"the model is wrong."* See [[Why Probability and Statistics]] for the reference-frame caveat.

---

## Why "normal"? — historical and the Central Limit Theorem

The name *normal* is doing serious work. The bell curve isn't a special distribution chosen by convention; it's the **universal limit shape** that arises whenever you sum many independent random variables.

**Brief history:**

- **De Moivre (1733)** discovered the bell curve as the limiting shape of the binomial distribution — the original "binomial → normal" approximation, predating the modern statement of CLT.
- **Laplace (1810)** generalised the result to sums of arbitrary independent random variables.
- **Gauss (1809)** rediscovered it in the context of measurement errors and the method of least squares (cf. [[Why Probability and Statistics]] for the variance-history connection). Hence the name *Gaussian* sometimes used synonymously with *normal*.
- **Adolphe Quetelet (1830s)** turned the error curve on *people* — his *average man* (*l'homme moyen*), with the mean treated as nature's ideal.
- **The name "normal"** was coined independently around 1875 — by Charles S. Peirce (1873), Wilhelm Lexis (1877), and Galton (1877) — and made standard by **Karl Pearson** in the 1890s. Pearson later regretted it, because calling one curve "normal" quietly implies every other distribution is "abnormal."

> [!info] The human story — [[Stories/The Naming of Normal]]
> How the curve went from a law of errors to a verdict on people — Quetelet's *average man* as ideal, Galton's inversion of it into "mediocrity" (and the regression-to-the-mean he found along the way), the loaded word "normal," and the eugenics shadow that the same statistical toolkit grew up inside — is told in [[Stories/The Naming of Normal]]. Honest-edges peer to [[Stories/Lewis Carroll the Mathematician]].

### Central Limit Theorem (the why)

> **CLT (Lindeberg–Lévy form, informal):** Let $X_1, X_2, \dots, X_n$ be independent and identically distributed random variables, each with finite mean $\mu$ and finite variance $\sigma^2$. Define the **sum** $S_n = X_1 + X_2 + \cdots + X_n$. Then as $n \to \infty$, the *standardised sum* $\dfrac{S_n - n\mu}{\sigma\sqrt{n}}$ converges in distribution to the standard normal $N(0, 1)$.

This is why the normal is "normal" — *it's the limit of almost everything*. Any process that is the sum of many small **independent** influences tends toward the bell curve.

- **Heights** — sum of many genetic and environmental factors → roughly normal within a population.
- **Measurement errors** — sum of many small independent error sources → roughly normal.
- **Sample means** — average of $n$ independent samples → normal as $n$ grows. *This is the foundation of all of statistical inference.*
- **Binomial counts for large $n$** — binomial is the sum of $n$ independent Bernoullis, so by CLT it tends to normal. (This is the §5.5 normal-approximation-to-binomial topic.)

The single word doing the load-bearing work in that statement is **independent**. CLT requires the summed variables to be independent (or near-independent — there are weaker theorems for "asymptotically independent" cases, but the spirit is the same). And here is the deep observation hiding in plain sight: **most of the world is *not* independent.**

- **Stock crashes** — when one stock falls hard, others fall too. The market is a network of correlated reactions. *Not independent.* This is why "this was a 10-sigma event" was the wrong reaction to 2008; the events weren't 10 independent samples from a normal, they were one big *correlated* movement.
- **Pandemics** — each infected case raises the probability of the next. *Not independent.* Hence exponential growth, not normal-distributed counts.
- **Power-grid failures** — one substation overloads, cascading to neighbours. *Not independent.* Cascades, not normals.
- **Social phenomena** — going viral, fashion trends, panic buying, bank runs. Each event makes the next more likely. *Not independent.* Power-law tails, not normal.
- **Anything with feedback loops** — the previous state of the system influences the current one. *Not independent.* Random walks, attractors, chaotic dynamics.

So the same line — *"normal is the limit of sums of independent influences"* — is *both* the case for the normal (when independence approximately holds, normal is the limit shape) *and* the case against (when independence fails, normal-distribution thinking fails too, often catastrophically). One sentence, two opposite conclusions, depending entirely on whether the *independent* assumption holds in your domain.

This is why a hunter — see [[Forward Reading and Problem Discovery]] — is constantly asking *"are these things actually independent, or do they affect each other?"* That question is what separates a domain where normal-distribution thinking works from one where it doesn't.

> [!info] Yes, CLT is a real theorem
> A common student worry is *"is CLT actually proven, or is it just a stated fact that everyone uses?"* The answer is **proven, and rigorously**. The standard proof uses **characteristic functions** $\varphi_X(t) = E(e^{itX})$ — the Fourier-transform analogue of moment-generating functions — plus **Lévy's continuity theorem** linking pointwise convergence of characteristic functions to convergence in distribution. The argument is short and beautiful: a Taylor expansion of $\varphi$ around $t = 0$ shows that the standardised sum's characteristic function tends to $e^{-t^2/2}$, which is the characteristic function of the standard normal. Lévy then converts that to convergence of distributions.
>
> *Why the proof is rarely shown in textbooks below graduate level:* you need measure-theoretic probability, complex analysis, and Fourier theory before the proof's symbols stop being magic. None of those are A-Level / IB / AP topics. So the result is *quoted* everywhere and *proven* at university — typically in a third- or fourth-year probability course (Billingsley's *Probability and Measure* or Durrett's *Probability: Theory and Examples* are the standard references). For 9709, take it as a theorem you can use; the proof is waiting for you when you get there.

> [!info] Beyond syllabus — what makes a distribution "non-normal"
> The CLT requires *finite variance*. Distributions with **infinite variance** — Cauchy, Pareto with shape $\alpha < 2$, some financial-return distributions — *don't* converge to normal. This is why fat-tailed real-world phenomena (stock crashes, city sizes, paper citation counts, internet attention) misbehave under normal-distribution thinking. The CLT doesn't apply when variance blows up. See [[Why Probability and Statistics]] for the reference-frame consequences.

---

## Standardisation — the bridge to the table

The general normal $X \sim N(\mu, \sigma^2)$ has infinitely many possible $(\mu, \sigma)$ combinations, so you can't possibly tabulate the CDF for each. The solution: **transform any normal into the standard normal $Z \sim N(0, 1)$**, and tabulate just one CDF.

The transformation is the **standardisation**:

$$\boxed{\;Z = \frac{X - \mu}{\sigma}\;}$$

This subtracts off the mean (so the distribution is centred at 0) and divides by the standard deviation (so the spread is 1). Algebraically:

$$X \sim N(\mu, \sigma^2) \quad\Longleftrightarrow\quad \frac{X - \mu}{\sigma} = Z \sim N(0, 1)$$

### Reading $z$ as a number of standard deviations

The **z-score** $z = (x - \mu)/\sigma$ has a clean interpretation: *how many standard deviations is $x$ above (or below) the mean?* A z-score of:

- $z = 0$: exactly at the mean.
- $z = 1$: one standard deviation above the mean. (≈ 84th percentile)
- $z = -1$: one standard deviation below the mean. (≈ 16th percentile)
- $z = 2$: two standard deviations above the mean. (≈ 97.5th percentile)
- $z = 3$: three standard deviations above the mean. (≈ 99.85th percentile)
- $z = -1.96$: the threshold for the lower 2.5% — used in 95% confidence intervals.

> [!warning] Standardisation direction
> Going from $X$ to $Z$: subtract the mean, divide by σ. Going from $Z$ to $X$ (when you're inverting): multiply by σ, add the mean: $X = \mu + Z\sigma$.
>
> A common mistake is to apply the formula in the wrong direction. Read the question forward: *what's given, what's asked?* If $X$ is given, standardise to find $Z$. If a probability is given and a value of $X$ is asked, find $Z$ from the inverse table, then de-standardise.

> [!warning] $\sigma$ vs $\sigma^2$ — the parameter notation gotcha
> Cambridge writes the normal distribution as $X \sim N(\mu, \sigma^2)$ — the **second parameter is the variance, not the standard deviation.** When the question says "$X \sim N(50, 16)$", it means $\mu = 50$ and $\sigma^2 = 16$, so $\sigma = 4$. Standardise with $z = (x - 50) / 4$, *not* $z = (x - 50) / 16$. This is a frequent mark-loss; read the parameters carefully.

---

## Computing probabilities — using $\Phi(z)$

The **standard-normal CDF** is

$$\Phi(z) = P(Z \le z)$$

It's tabulated in **List MF19, page 10** for $z \ge 0$ in steps of $0.01$. To use it:

### The four moves

**Move 1 — direct lookup.** $P(Z \le z) = \Phi(z)$ — read straight off the table.

> *Example.* $P(Z \le 1.43) = \Phi(1.43) = 0.9236$.

**Move 2 — complement.** $P(Z > z) = 1 - \Phi(z)$.

> *Example.* $P(Z > 1.43) = 1 - 0.9236 = 0.0764$.

**Move 3 — interval.** $P(a \le Z \le b) = \Phi(b) - \Phi(a)$.

> *Example.* $P(0.5 \le Z \le 1.5) = \Phi(1.5) - \Phi(0.5) = 0.9332 - 0.6915 = 0.2417$.

**Move 4 — symmetry for negative $z$.** The MF19 table only lists $z \ge 0$. Use the symmetry:

$$\Phi(-z) = 1 - \Phi(z)$$

> *Example.* $P(Z \le -1.43) = \Phi(-1.43) = 1 - \Phi(1.43) = 1 - 0.9236 = 0.0764$.
>
> *Example.* $P(-1 \le Z \le 1) = \Phi(1) - \Phi(-1) = \Phi(1) - (1 - \Phi(1)) = 2\Phi(1) - 1 = 2(0.8413) - 1 = 0.6826 \approx 68\%$. ✓ (The 68 in the 68/95/99.7 rule.)

### A worked example end-to-end

> *The heights of adult women in a population are normally distributed with mean $165$ cm and standard deviation $7$ cm. Find the probability that a randomly chosen woman is taller than $175$ cm.*

Forward read:
- *"normally distributed"* → the model is normal. (Watchful — see "Reference frame" below.)
- *"mean 165, standard deviation 7"* → $\mu = 165$, $\sigma = 7$. So $X \sim N(165, 49)$ (since $\sigma^2 = 49$).
- *"taller than 175 cm"* → $P(X > 175)$.
- *"find the probability"* → standardise + read table.

Standardise:
$$z = \frac{175 - 165}{7} = \frac{10}{7} \approx 1.43$$

Compute:
$$P(X > 175) = P(Z > 1.43) = 1 - \Phi(1.43) = 1 - 0.9236 = 0.0764 \approx 7.6\%$$

So about 7.6% of women in this population are over 175 cm tall.

### A two-bound interval example

> *The same population. Find the probability a randomly chosen woman is between $160$ and $172$ cm tall.*

Standardise both bounds:
$$z_1 = \frac{160 - 165}{7} \approx -0.71, \qquad z_2 = \frac{172 - 165}{7} = 1.00$$

Compute:
$$P(160 \le X \le 172) = \Phi(1.00) - \Phi(-0.71) = \Phi(1.00) - (1 - \Phi(0.71)) = 0.8413 - (1 - 0.7611) = 0.8413 - 0.2389 = 0.6024$$

About 60.2% of women are between 160 and 172 cm.

---

## The inverse — finding $z$ from $p$

Sometimes the question gives you a *probability* and asks for the corresponding *value*. This is the inverse direction.

The MF19 page 10 also includes a **critical-values table** for the standard normal:

| $p$ | 0.75 | 0.90 | 0.95 | 0.975 | 0.99 | 0.995 | 0.9975 | 0.999 | 0.9995 |
|---|---|---|---|---|---|---|---|---|---|
| $z$ such that $P(Z \le z) = p$ | 0.674 | 1.282 | 1.645 | 1.960 | 2.326 | 2.576 | 2.807 | 3.090 | 3.291 |

So if the question says *"find $z$ such that $P(Z \le z) = 0.95$"*, the answer is $z = 1.645$. (For exact $p$ values not on the table, you'd find the closest entry on the main $\Phi(z)$ table and interpolate.)

> [!tip] Memorise the few standard z-thresholds
> A few z-values are worth recalling without the table:
> - $z = 1.645$ for the 95% one-tail (use in 90% two-tail intervals)
> - $z = 1.96$ for the 97.5% one-tail (use in **95% two-tail confidence intervals** — the most-used number in inferential statistics)
> - $z = 2.576$ for the 99.5% one-tail (use in 99% two-tail intervals)
>
> They show up everywhere in the AP/IB/university statistics that builds on this card.

### Inverse worked example

> *Same population (μ = 165, σ = 7). The shortest 10% of women are below what height?*

Forward read: we want a height $h$ such that $P(X \le h) = 0.10$. So $\Phi(z) = 0.10$, meaning $z$ is the *negative* of the value where $\Phi(z) = 0.90$.

From the critical-values table: $\Phi(1.282) = 0.90$, so $\Phi(-1.282) = 0.10$. Thus $z = -1.282$.

De-standardise:
$$h = \mu + z\sigma = 165 + (-1.282)(7) \approx 165 - 8.97 \approx 156.0 \text{ cm}$$

The shortest 10% of women in this population are below about 156 cm.

---

## Normal approximation to the binomial

When $n$ is large, the binomial $B(n, p)$ is unwieldy — computing $\binom{n}{r}$ for big $n$ is painful, and you may need cumulative probabilities like $P(X \le k)$ that require summing many terms.

The **normal approximation** lets you replace the binomial with a normal of the same mean and variance:

$$X \sim B(n, p) \;\;\approx\;\; N\big(np,\; np(1-p)\big) \qquad \text{for large } n$$

Reading the symbols, left to right:

- $X$ — the count of successes (the random variable we're modelling).
- $B(n, p)$ — the **binomial distribution**: $n$ independent trials, each with success probability $p$.
- $n$ — the **number of trials** (fixed in advance).
- $p$ — the **probability of success** on a single trial (constant across trials).
- $N(\mu, \sigma^2)$ — the **normal distribution** with mean $\mu$ and variance $\sigma^2$ (Cambridge convention: second slot is variance, not standard deviation).
- $np$ — the **mean** of the binomial $B(n, p)$. *And the mean of the normal we're matching it to.*
- $np(1-p)$ — the **variance** of the binomial $B(n, p)$. *And the variance of the normal we're matching it to.*

So the approximation says: *the binomial and a particular normal share their first two moments; once $n$ is large, you can replace the discrete binomial with the continuous normal of identical mean and variance, and probabilities will match closely.*

**Why it works** — through CLT. A binomial $B(n, p)$ is the sum of $n$ independent **Bernoulli trials** $X_1, X_2, \dots, X_n$, each defined as
$$X_i = \begin{cases} 1 & \text{if trial } i \text{ is a success (probability } p\text{)} \\ 0 & \text{otherwise (probability } 1-p\text{)} \end{cases}$$
so $X = X_1 + X_2 + \cdots + X_n$. The CLT (above) says the sum of many independent identically distributed random variables tends to a normal distribution as $n$ grows — and the matching mean / variance gives the parameters of *which* normal. Bernoullis trivially have finite mean ($p$) and finite variance ($p(1-p)$), so CLT applies.

### When to use it — the conditions

The approximation is reasonable when **both** $np \ge 5$ and $n(1-p) \ge 5$.

(Some textbooks use $np \ge 10$ and $n(1-p) \ge 10$ for tighter accuracy — the 5-cutoff is the Cambridge convention, but if a problem looks borderline, the larger thresholds give better answers.)

The conditions ensure the binomial isn't *too skewed* — if $p$ is very close to 0 or very close to 1, the binomial pushes against the boundary and looks asymmetric, which the symmetric normal can't capture well. Both $np$ and $n(1-p)$ being reasonably large is the symmetric-enough check.

### The continuity correction (don't forget!)

The binomial is **discrete** ($X$ takes integer values 0, 1, 2, …), but the normal is **continuous**. To bridge the discrete-to-continuous gap, apply the **continuity correction**:

| Discrete event | Continuous approximation |
|---|---|
| $P(X = k)$ | $P(k - 0.5 \le X \le k + 0.5)$ |
| $P(X \le k)$ | $P(X \le k + 0.5)$ |
| $P(X < k)$ | $P(X \le k - 0.5)$ |
| $P(X \ge k)$ | $P(X \ge k - 0.5)$ |
| $P(X > k)$ | $P(X \ge k + 0.5)$ |

The intuition: each discrete point $k$ "owns" the interval $[k-0.5, k+0.5]$ when you smooth it to a continuous distribution. So a discrete $\le k$ becomes a continuous $\le k + 0.5$ to include the right half of point $k$'s territory.

> [!info] Strictly speaking, the territory is half-open
> Each integer $k$ owns the half-open interval $[k - 0.5, k + 0.5)$ (or equivalently $(k - 0.5, k + 0.5]$ — pick a convention). It has to be half-open, because otherwise both $k$ and $k+1$ would lay claim to the boundary point $k + 0.5$, which is a contradiction. *But* for a continuous distribution, single points have probability zero — the integral of the PDF over a single point is zero — so the boundary doesn't change any probability you compute. The closed form $[k-0.5, k+0.5]$ is what's used in practice for cleaner notation. Same reason $0.999\ldots = 1$ in the reals: the boundary is invisible to the measure. The half-open interval is *technically* correct; the closed interval is *practically* identical.

> [!warning] Continuity correction is the most-forgotten step
> Cambridge mark schemes flag this as the single most common loss-of-marks pattern in §5.5. *Always* ask: "discrete count → continuous approximation? Then ±0.5." Wrong direction is also penalised; double-check the inequality.

### Worked normal-approximation example

> *A biased coin lands heads with probability $0.4$. Toss it $50$ times. Find the probability of getting at least $25$ heads.*

Forward read:
- $X \sim B(50, 0.4)$.
- Conditions for normal approx: $np = 50 \times 0.4 = 20 \ge 5$ ✓ and $n(1-p) = 50 \times 0.6 = 30 \ge 5$ ✓. Good.
- Approximation: $X \approx N(20, 12)$ (mean $= 20$, variance $= np(1-p) = 12$, so $\sigma = \sqrt{12} \approx 3.46$).
- Asked: $P(X \ge 25)$. Discrete; **continuity correction:** $P(X \ge 25) \approx P(X' \ge 24.5)$ where $X'$ is the continuous normal approximation.

Standardise:
$$z = \frac{24.5 - 20}{\sqrt{12}} = \frac{4.5}{3.464} \approx 1.30$$

Compute:
$$P(X' \ge 24.5) = 1 - \Phi(1.30) = 1 - 0.9032 = 0.0968 \approx 9.7\%$$

So about a 9.7% chance of getting 25 or more heads in 50 tosses with $p = 0.4$.

---

## When NOT to trust the normal — the reference-frame caveat

Everything above assumes the underlying distribution *actually is* normal (or the binomial is well-approximated by a normal). The normal distribution is a *model*, and like all models it has assumptions. When the assumptions fail, the formulae above stop matching reality.

**The hunter's question** (cf. [[Forward Reading and Problem Discovery]]): *what reference frame is this normal-distribution claim being made over, and is that frame the right one?*

Examples where the normal is misapplied:

- **Stock returns.** Famously *not* normal. They have **fat tails** — extreme events are much more common than a normal distribution predicts. The 2008 financial crisis revealed risk models that assumed normality and ignored the fat-tail behaviour of real markets. "10-sigma events" don't happen in a true normal distribution; if you see one, the model is wrong.
- **Heights *across all of life*.** Within human adult populations, height is roughly normal. Across all life — including bacteria, viruses, single-celled organisms — height is *radically* skewed; humans are far-right outliers (cf. [[Why Probability and Statistics]] for this exact example). The normal applies only within the right reference frame.
- **Income / wealth.** Heavily right-skewed; the median is much less than the mean; a small number of high-earners pull the average. Normal is the wrong shape; lognormal or Pareto is closer.
- **Web-scale data** (citations, video views, audience attention). Power-law tails. Normal underestimates the long right tail by orders of magnitude.

> [!info] Connection to [[Why Probability and Statistics]]
> The "is this *actually* normal?" question is *the* place where statistical thinking gets confused with statistical *belief*. The normal distribution is the most-cited model in the world; it's also the most misapplied. Knowing both that it works (CLT, 68/95/99.7, the four moves above) and that it sometimes doesn't (fat tails, skewed populations, the wrong reference class) is what statistical literacy actually means.

---

## Common Failure Modes

### 1. Forgetting to standardise

The MF19 table only knows the standard normal. If you read off "$\Phi(175) =$ something" because the question said $X \le 175$, you've ignored the parameters $\mu, \sigma$ entirely. Always:

$$z = \frac{x - \mu}{\sigma}$$

then look up $\Phi(z)$.

### 2. Using $\sigma^2$ where you mean $\sigma$

$X \sim N(50, 16)$ means $\sigma^2 = 16$, so $\sigma = 4$. If you stand­ardise by dividing by $16$ instead of $4$, your z-score is wrong by a factor of 4. Read parameters carefully.

### 3. Negative-z confusion

The MF19 table only lists $z \ge 0$. For a negative z-score, use the symmetry $\Phi(-z) = 1 - \Phi(z)$. Don't try to read $\Phi(-0.71)$ off the main table; it's not there. Use $\Phi(-0.71) = 1 - \Phi(0.71) = 1 - 0.7611 = 0.2389$.

### 4. Forgetting the continuity correction

When approximating a discrete binomial with a continuous normal, the $\pm 0.5$ adjustment is essential. *"$P(X \le 25) \approx P(X' \le 25)$"* without correction loses marks; the correct version is $P(X' \le 25.5)$. A useful mnemonic: *expand the discrete event by half a unit on each side it should include.*

### 5. Applying the normal to clearly non-normal data

If the data is heavily skewed, has a hard boundary (e.g. cannot be negative), or is discrete with few values, the normal approximation isn't appropriate. Real-world warning signs: the mean and median differ a lot, there's a long tail on one side, extreme values appear "too often". See [[Why Probability and Statistics]] for the philosophical extension.

### 6. Reading the table wrong

The MF19 table rows are tens-and-units digit (e.g. 1.4); the columns 0–9 are the hundredths digit (e.g. 0.03). So $\Phi(1.43)$ is row 1.4, column 3 → $0.9236$. The "ADD" columns on the right are for further interpolation (rarely needed at 9709 level). Don't confuse row/column.

---

## Cross-Domain Bridge — the normal everywhere

The normal distribution is the most-encountered probability distribution in applied subjects, by an enormous margin. A walking tour:

| Domain | Where the normal lives |
|---|---|
| **Physics — measurement errors** | Noise, instrument readings, repeated measurements — Gauss's original application |
| **Physics — statistical mechanics** | Maxwell-Boltzmann velocity distribution; thermal fluctuations (each velocity component is normal → [[Kinetic Theory and the Ideal Gas]]; the man behind it: [[Stories/Boltzmann's Tombstone]]) |
| **Physics — diffusion** | Brownian motion: position of a particle after time $t$ is normal with variance $\propto t$ |
| **Biology** | Heights, weights, blood pressure within a population |
| **Quality control** | Manufacturing tolerances; control charts use $\mu \pm 3\sigma$ thresholds |
| **Inferential statistics** | Sample means $\bar{X} \sim N(\mu, \sigma^2/n)$ by CLT — the foundation of confidence intervals and hypothesis tests |
| **Finance** | Portfolio return models *assume* normal — careful, see fat-tails caveat |
| **Machine learning** | Loss functions; weight initialisation; the Gaussian process |
| **Signal processing** | Additive white Gaussian noise (AWGN) channel — fundamental in information theory |
| **Image processing** | Gaussian blur — convolving with a 2D normal kernel |

> [!info] Beyond syllabus — why the normal PDF has $2\pi$ in it
> *Recall the standard-normal PDF stated way back at the top of this card: $\varphi(z) = \dfrac{1}{\sqrt{2\pi}}\,e^{-z^2/2}$.* That $\dfrac{1}{\sqrt{2\pi}}$ out front looks like an arbitrary constant — but it isn't. It traces back to a deep identity: $\int_{-\infty}^{\infty} e^{-z^2/2}\,dz = \sqrt{2\pi}$, so the $\dfrac{1}{\sqrt{2\pi}}$ is exactly what you need to make the PDF integrate to 1.
>
> Where does the $2\pi$ come from? The famous trick: instead of evaluating $\int e^{-x^2}\,dx$ directly (impossible in elementary functions), evaluate the *square* of it, which is a 2D integral $\int\int e^{-(x^2+y^2)}\,dx\,dy$. Switch to polar coordinates, and the $2\pi$ is the angular sweep — a constant from *circles* showing up in the most-used probability distribution. So $\pi$ shows up in probability for the same reason it shows up in geometry: there's a hidden circular symmetry. Nature is connected in ways we keep being surprised by.

---

## Exam Notes

### Cambridge 9709 Paper 5 (P&S 1) — §5.5

- **The four question shapes:** (1) standardise and look up — $z = \frac{x-\mu}{\sigma}$, then $\Phi$; (2) **inverse** use — given a probability, read $z$ backwards and unwind to $x$; (3) **find $\mu$ and/or $\sigma$** from one or two stated probabilities — the simultaneous-equations staple, where sign errors in $z$ kill both equations; (4) **normal approximation to the binomial** — check $np > 5$ *and* $nq > 5$, use $N(np, npq)$, and apply the **continuity correction** (a named marking point; "at least 25" becomes 24.5, and the direction of the half is where marks die).
- Sketch the curve and shade — examiners explicitly credit a correct region diagram, and it catches wrong-tail errors before they cost three marks.
- $\Phi$ tables and the standardisation are MF19-supported; the $np, nq$ thresholds and the continuity correction are **not** — memorise them.
- Combining normal variables ($X \pm Y$, $aX + bY$) belongs to Paper 6: [[Linear Combinations of Random Variables]].

### IB AA / AP

- **IB AA (SL 4.9, 4.12):** normal probabilities and inverse-normal on the GDC (no tables), including finding $\mu, \sigma$ from probabilities; z-values appear as "standardised values" in HL reasoning questions.
- **AP Statistics** lives on this distribution (empirical rule, z-scores, normal probability plots); AP Calculus meets it only as an integrand.

## Connections

- **Prerequisites:** [[Probability Basics]], [[Discrete Random Variables]] (the discrete distributions this card extends to continuous), [[Why Probability and Statistics]] (the philosophical companion — when not to trust the normal), [[Averages and Spread]] (standard deviation as the spread parameter).
- **Companion (philosophy):** [[Why Probability and Statistics]] — *why* the normal distribution is so universal (CLT) and *when* to be skeptical of normal-distribution claims (reference frames, fat tails). Read in tandem with this card; the technical four-step procedure here is empty without the "is the model right?" question from there.
- **Leads to — P6:** [[Poisson Distribution]] — another distribution this card's binomial-approximation story connects to (Poisson is the "rare-event limit", normal is the "large-$n$ limit" of the binomial). [[Continuous Random Variables]] (P6 §6.3) — the integral version of the discrete distributions story; the normal is the most-used continuous DRV.
- **Application:** every place "$Z = (x-\mu)/\sigma$" or "z-score" appears — sample-mean inference (CLT), confidence intervals, hypothesis tests, control charts, financial risk models, machine learning loss functions, biology measurements, and on.
- **Hunter cross-reference:** [[Forward Reading and Problem Discovery]] — the reference-frame question ("is this *actually* normal in the relevant population?") is a forward-reading move applied to statistical models.

---

## What's on the formula sheet — and what isn't

> [!info] Formula-sheet status — Cambridge 9709 (List MF19) — high-surprise card
>
> **From this card, MF19 gives you (page 10):**
>
> - The full $\Phi(z)$ **CDF table** for $z \in [0, 2.99]$ in steps of $0.01$. *Your main exam tool.*
> - The **critical-values table** for standard probabilities ($p = 0.75, 0.90, 0.95, 0.975, 0.99, 0.995, 0.9975, 0.999, 0.9995$).
> - The **symmetry rule** $\Phi(-z) = 1 - \Phi(z)$ — printed under the table.
>
> **From this card, MF19 does NOT give you (memorise these for 9709):**
>
> - **The standardisation formula $Z = \dfrac{X - \mu}{\sigma}$.** *This is the most surprising omission on the entire sheet.* The whole §5.5 hangs on this formula — without it you can't use the table. **Memorise it.**
> - **De-standardisation $X = \mu + Z\sigma$** (the inverse direction).
> - **The PDF formula** $\varphi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ — *not on MF19, and not strictly required for §5.5*. You compute via the table, not the PDF. (P6 §6.3 will require working with general PDFs, but not this one.)
> - **The 68 — 95 — 99.7 rule** — not on MF19, useful as a sanity check.
> - **Normal approximation to binomial — the conditions** ($np \ge 5$ AND $n(1-p) \ge 5$). *Not on MF19; memorise.* (Note: the *approximation formula itself* $X \approx N(np, np(1-p))$ is **re-assemblable** from MF19 — the binomial $\mu = np$ and $\sigma^2 = np(1-p)$ are both given in the *Discrete random variables* section, and the move "use those to specify a normal of the same mean and variance" is the small bit you bring from your head. So the formula isn't strictly *not on the sheet* — it's *partially there*, just needs assembly.)
> - **Continuity correction** ($\pm 0.5$ when going from discrete to continuous) — *not on MF19, and the most-forgotten step in the entire P5 syllabus.*
>
> See [[MF19 Reference (9709)]] for the full audit. *Other boards have different sheets — IB AA SL/HL, AP Statistics, A-Level Edexcel/AQA/OCR each provide their own. Always check yours.*
>
> **The teacher's framing.** Cambridge gives you the table because looking up $\Phi(z)$ from a formula would require an integral that has no closed form (the **error function** is non-elementary). They cannot avoid the table. But they *can* expect you to know how to *get to* the table — which means the standardisation. The asymmetry "table given, standardisation memorised" is structural to the §5.5 exam: bring the formula, use the table.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $X \sim N(\mu, \sigma^2)$ | `X \sim N(\mu, \sigma^2)` | Normal with mean $\mu$, **variance $\sigma^2$** (not std dev) |
| $Z \sim N(0, 1)$ | `Z \sim N(0, 1)` | The standard normal |
| $\varphi(z)$ | `\varphi(z)` | Standard-normal PDF |
| $\Phi(z) = P(Z \le z)$ | `\Phi(z) = P(Z \le z)` | Standard-normal CDF; the MF19 table |
| $Z = \dfrac{X - \mu}{\sigma}$ | `Z = \dfrac{X - \mu}{\sigma}` | **Standardisation** — *not on MF19* |
| $X = \mu + Z\sigma$ | `X = \mu + Z\sigma` | De-standardisation |
| $\Phi(-z) = 1 - \Phi(z)$ | `\Phi(-z) = 1 - \Phi(z)` | Symmetry — used for negative z lookups |
| $X \approx N(np, np(1-p))$ | `X \approx N(np, np(1-p))` | Normal approximation to $B(n,p)$ |
| $\pm 0.5$ | continuity correction | When discrete → continuous |
| $z = 1.96$ | — | The 95% two-tail threshold (worth memorising) |
