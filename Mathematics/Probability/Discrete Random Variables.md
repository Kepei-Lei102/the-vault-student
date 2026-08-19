---
chinese: 离散随机变量 (lísàn suíjī biànliàng)
prerequisites:
  - "[[Probability Basics]]"
  - "[[Combined Probability]]"
  - "[[Conditional Probability]]"
  - "[[Permutations and Combinations]]"
  - "[[Arithmetic and Geometric Progressions]]"
leads_to:
  - "[[Normal Distribution]]"
  - "[[Poisson Distribution]]"
  - "[[Repeated Measurements]]"
  - "[[Linear Combinations of Random Variables]]"
  - "[[Continuous Random Variables]]"
  - "[[Hypothesis Tests]]"
  - "[[Why Probability and Statistics]]"
  - "[[Chi-Squared Tests]]"
  - "[[Non-Parametric Tests]]"
  - "[[Probability Generating Functions]]"
tags:
  - subject/mathematics
  - domain/probability
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/9709-5-4
  - type/definition
  - type/methodology
  - type/distribution
  - notation/random-variable
  - misconception/expected-value-as-likely-value
  - misconception/binomial-without-independence
  - misconception/geometric-counts-failures
---

# Discrete Random Variables 离散随机变量

## What this card is for

So far in the probability cluster ([[Probability Basics]], [[Combined Probability]], [[Conditional Probability]]) we've answered "how likely is this *event*?" We've been computing $P(A)$ for a single event $A$.

The leap this card makes is small but transformative: instead of asking *whether* an outcome happens, ask *what numerical value the outcome takes* — and treat that value as the variable.

> "The number rolled on a die" is a quantity that takes values $1, 2, 3, 4, 5, 6$ — each with probability $\tfrac{1}{6}$.
>
> "The number of heads in 5 coin flips" is a quantity that takes values $0, 1, 2, 3, 4, 5$ — each with some probability.
>
> "The number of tosses until the first head" is a quantity that takes values $1, 2, 3, \dots$ — each with some probability.

Each of those phrases names a **discrete random variable**. The whole P5 §5.4 syllabus row — expectation, variance, the binomial distribution, the geometric distribution — is a tour of what you can compute *about* such a variable.

> [!info] What's discrete vs. what's continuous
> *Discrete* means the values are *separated* — you can list them: $\{1, 2, 3, \dots\}$ or $\{0, 1, 2, \dots, n\}$. The number of cars passing in an hour is discrete. The number of phone calls a help desk receives is discrete. *Continuous* random variables (height, weight, time-until-failure) take values from an interval of $\mathbb{R}$ and are handled by [[Continuous Random Variables]] (P6 §6.3) — that card uses integrals where this one uses sums. The two stories run in parallel.

### 中文锚点

**离散** (lísàn) = 离散的、可数的（一个一个数得出来的）。
**随机** (suíjī) = 随机的（结果不固定）。
**变量** (biànliàng) = 变量（一个数值，取值会变）。

把三件事并起来：**离散随机变量**就是「一个会随机取离散值的数」。例如：

- 掷一颗骰子，结果是 1 到 6 中的某一个 — 一个离散随机变量 $X$。
- 投硬币 5 次，正面次数是 0 到 5 中的某一个 — 一个离散随机变量。
- 连续投硬币，直到第一次出现正面，所用次数是 $1, 2, 3, \dots$ 中的某一个 — 也是一个离散随机变量。

考点四件套：**概率分布表 → 期望 $E(X)$ → 方差 $\text{Var}(X)$ → 两种命名分布（二项 + 几何）**。

---

## Discrete Random Variables — the framework

A **discrete random variable** $X$ is a function from outcomes to numbers, taking *separated* values $x_1, x_2, x_3, \dots$ — usually written with capital $X$ for the variable itself and lowercase $x$ for a particular value it takes.

The full description of $X$ is its **probability distribution**, which lists every value $x_i$ together with the probability $P(X = x_i)$.

### The probability distribution table

For a finite-valued $X$, write the distribution as a table:

| $x$ | $x_1$ | $x_2$ | $x_3$ | $\cdots$ | $x_n$ |
|---|---|---|---|---|---|
| $P(X = x)$ | $p_1$ | $p_2$ | $p_3$ | $\cdots$ | $p_n$ |

Two non-negotiable conditions:

1. **Each $p_i \geq 0$** — probabilities can't be negative.
2. **The $p_i$ sum to 1** — *something* has to happen. $\sum_{i} p_i = 1$.

Cambridge problems often start with a table where one entry is missing, and you fix it by enforcing the sum-to-1 constraint. Always check this first; an exam table with $\sum p_i \neq 1$ is broken (or you've miscopied it).

> [!example] Worked — fair die
> Roll a fair six-sided die. Let $X$ be the number shown.
>
> | $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
> |---|---|---|---|---|---|---|
> | $P(X=x)$ | $\tfrac{1}{6}$ | $\tfrac{1}{6}$ | $\tfrac{1}{6}$ | $\tfrac{1}{6}$ | $\tfrac{1}{6}$ | $\tfrac{1}{6}$ |
>
> Sum: $6 \times \tfrac{1}{6} = 1$. ✓

> [!example] Worked — find a missing probability
> Suppose $X$ takes values $1, 2, 3, 4$ with probabilities $0.1, 0.3, k, 0.4$. Find $k$.
>
> Forward read: distribution must sum to 1. So $0.1 + 0.3 + k + 0.4 = 1 \Rightarrow k = 0.2$. ✓

### Forward-reading invariants for DRV problems

In the spirit of [[Forward Reading and Problem Discovery]] — every clause in a DRV problem locks something down. A short cheat-sheet:

| Phrasing | Invariant it gives you |
|---|---|
| "$X$ takes values $\{x_1, \dots, x_n\}$" | The sample space of $X$ |
| "with probabilities $\{p_1, \dots, p_n\}$" | The full distribution (assuming they sum to 1) |
| "fair die / fair coin" | All listed outcomes are equally likely |
| "with replacement" | Trials are independent |
| "without replacement" | Trials are *not* independent — binomial may not apply |
| "$n$ trials" | The number of trials is fixed |
| "until the first success" | Geometric setup, not binomial |
| "find $E(X)$" / "find the expected value" | Compute $\sum x \cdot P(X=x)$ |
| "find $\text{Var}(X)$" | Compute $E(X^2) - (E(X))^2$ |

---

## Expected Value $E(X)$

The **expected value** (or **mean**) of a discrete random variable $X$ is

$$E(X) = \sum_{i} x_i \cdot P(X = x_i)$$

Read it as: *take each value $X$ can be, multiply by how likely it is, and add them up.*

### Why "expected"?

It's a slightly misleading name — $E(X)$ is *not necessarily* a value $X$ ever actually takes. Roll a fair die: $E(X) = \tfrac{1+2+3+4+5+6}{6} = 3.5$, but no roll ever lands on 3.5.

The name comes from the **long-run average** interpretation: if you observe $X$ over many independent trials and average the results, the average converges to $E(X)$. Roll the die a million times, average the results, and you'll see something extremely close to 3.5. This is the **Law of Large Numbers** (a beyond-syllabus theorem, but worth knowing as the meaning that makes "expected" sensible).

> [!info] Connection to weighted average
> $E(X)$ is the *weighted average* of the possible values, where the weights are the probabilities. If all outcomes are equally likely (each $p_i = 1/n$), it reduces to the ordinary mean $\tfrac{1}{n}\sum x_i$.

### Linearity of expectation

For constants $a, b$ and any DRV $X$:

$$E(aX + b) = a\,E(X) + b$$

**Proof.** $E(aX + b) = \sum (a x_i + b) p_i = a \sum x_i p_i + b \sum p_i = a\,E(X) + b \cdot 1 = a\,E(X) + b.$ ∎

The simple but **deeper** version of linearity — applies even when the variables are *not independent*:

$$E(X + Y) = E(X) + E(Y) \qquad \text{(any two DRVs)}$$

This is one of the most useful identities in probability. The binomial mean derivation below is essentially a single application of it.

> [!example] Worked — fair die expectation
> $X$ = number shown on a fair die.
>
> $E(X) = 1 \cdot \tfrac{1}{6} + 2 \cdot \tfrac{1}{6} + 3 \cdot \tfrac{1}{6} + 4 \cdot \tfrac{1}{6} + 5 \cdot \tfrac{1}{6} + 6 \cdot \tfrac{1}{6} = \tfrac{21}{6} = 3.5$

> [!example] Worked — winnings expectation
> A game pays £10 if you roll a 6, costs £2 otherwise. Let $W$ = winnings.
>
> | $w$ | +10 | −2 |
> |---|---|---|
> | $P(W=w)$ | $\tfrac{1}{6}$ | $\tfrac{5}{6}$ |
>
> $E(W) = 10 \cdot \tfrac{1}{6} + (-2) \cdot \tfrac{5}{6} = \tfrac{10 - 10}{6} = 0$.
>
> The game is *fair* — long-run average winnings are zero. Bumping the prize to £12 would tilt it in your favour: $E(W) = \tfrac{12 - 10}{6} \approx 0.33$ per game.

---

## Variance $\text{Var}(X)$ and Standard Deviation

The **variance** of $X$ is the expected squared deviation from the mean:

$$\text{Var}(X) = E\big((X - \mu)^2\big) \qquad \text{where } \mu = E(X)$$

It measures how *spread out* the distribution is. A near-constant variable has variance near zero; a wildly variable one has large variance.

> [!info] Why squared, why root, why this exists at all
> *Why* statistics settled on **squared** deviations rather than absolute ones, and *why* we then take the square root to call it the **standard deviation** — both questions have answers, and the answers connect to differentiability, the Central Limit Theorem, and a 100-year history (Gauss 1809 → Pearson 1893 → Fisher 1918). See [[Why Probability and Statistics]] for the full story; here we take the formula as given and use it.

### The computational form

The defining formula above is conceptually clean but tedious to compute. The **computational form** is the one you'll actually use:

$$\boxed{\;\text{Var}(X) = E(X^2) - (E(X))^2\;}$$

Read aloud: *"variance is the mean of the squares minus the square of the mean."*

**Proof.**
$$
\text{Var}(X) = E\big((X-\mu)^2\big) = E(X^2 - 2\mu X + \mu^2)
$$
By linearity: $= E(X^2) - 2\mu E(X) + \mu^2 = E(X^2) - 2\mu^2 + \mu^2 = E(X^2) - \mu^2$. ∎

The trick: expand the square, distribute the expectation linearly, recognize $E(X) = \mu$, simplify. The result is much friendlier computationally — you only need to know $E(X)$ and $E(X^2)$, both of which come straight from the distribution table.

### Standard deviation

The **standard deviation** is

$$\sigma = \sqrt{\text{Var}(X)}$$

It's the variance back in the original units of $X$ (variance has units of $X^2$, which often makes no physical sense — variance of "number of heads" is "(heads)²"; standard deviation is "heads", which does).

### Properties under linear transformation

For constants $a, b$:

$$\text{Var}(aX + b) = a^2\,\text{Var}(X)$$

**Proof.** Let $Y = aX + b$. Then $E(Y) = a\mu + b$, so
$$\text{Var}(Y) = E\big((Y - (a\mu + b))^2\big) = E\big((aX - a\mu)^2\big) = a^2\,E\big((X - \mu)^2\big) = a^2\,\text{Var}(X). \quad\blacksquare$$

Notice: the **shift $b$ disappears** (a constant shift doesn't change spread), and the **scale $a$ comes out squared** (variance scales as the square because it's a squared quantity).

> [!example] Worked — die variance
> Continuing the fair-die example with $\mu = 3.5$.
>
> $E(X^2) = 1 \cdot \tfrac{1}{6} + 4 \cdot \tfrac{1}{6} + 9 \cdot \tfrac{1}{6} + 16 \cdot \tfrac{1}{6} + 25 \cdot \tfrac{1}{6} + 36 \cdot \tfrac{1}{6} = \tfrac{91}{6} \approx 15.17$
>
> $\text{Var}(X) = E(X^2) - \mu^2 = \tfrac{91}{6} - \tfrac{49}{4} = \tfrac{182 - 147}{12} = \tfrac{35}{12} \approx 2.917$
>
> $\sigma = \sqrt{35/12} \approx 1.71$.

> [!tip] Always compute $E(X)$ first, then $E(X^2)$, then $\text{Var}(X)$
> In Cambridge problems, the routine is always: build the distribution table → compute $E(X)$ from the table → add an $X^2$ row to the table → compute $E(X^2)$ → subtract. Don't compute $E((X-\mu)^2)$ directly; the computational form is shorter.

---

## The Binomial Distribution $X \sim B(n, p)$

The first named distribution. Used when the experiment has a precise structure:

### The four conditions (all required)

1. **Fixed number $n$ of trials.** ($n$ is decided in advance.)
2. **Each trial has exactly two outcomes** — call them *success* and *failure*. ($p$ = probability of success on a single trial.)
3. **The probability $p$ of success is the same on every trial.** (Constant.)
4. **The trials are independent.** (Each trial's outcome doesn't affect the others.)

If all four hold and $X$ counts the number of successes in the $n$ trials, then $X \sim B(n, p)$ — read "$X$ is binomially distributed with parameters $n$ and $p$".

### The probability mass function

$$P(X = r) = \binom{n}{r} p^r (1 - p)^{n - r} \qquad \text{for } r = 0, 1, 2, \dots, n$$

**Why this formula** (forward derivation):

- Pick which $r$ of the $n$ trials are the successes: $\binom{n}{r}$ ways.
- For each such choice, the probability of *that exact pattern* of successes and failures is $p^r \cdot (1-p)^{n-r}$ (by independence — each trial's probability multiplies).
- Sum over all $\binom{n}{r}$ patterns (they're disjoint): $\binom{n}{r} p^r (1-p)^{n-r}$.

Distinct from picking *which* trials succeed (the $\binom{n}{r}$ factor) is the probability of *each pattern* (the $p^r (1-p)^{n-r}$ factor). The combinatorial structure of [[Permutations and Combinations]] meets the multiplicative structure of [[Combined Probability]] under the independence assumption.

### Mean and variance — clean derivation via indicator variables

The Cambridge formulae:

$$E(X) = np \qquad \text{Var}(X) = np(1 - p)$$

The slick proof is via **indicator variables**. Define

$$X_i = \begin{cases} 1 & \text{if trial } i \text{ is a success} \\ 0 & \text{otherwise} \end{cases}$$

Then $X = X_1 + X_2 + \cdots + X_n$ (the count of successes is the sum of the indicators).

Each $X_i$ has the simplest possible distribution:

| $x$ | 0 | 1 |
|---|---|---|
| $P(X_i = x)$ | $1-p$ | $p$ |

So $E(X_i) = 0 \cdot (1-p) + 1 \cdot p = p$ and $E(X_i^2) = 0^2 \cdot (1-p) + 1^2 \cdot p = p$, giving $\text{Var}(X_i) = E(X_i^2) - (E(X_i))^2 = p - p^2 = p(1-p)$.

Now use linearity:

- **Mean:** $E(X) = E(X_1) + E(X_2) + \cdots + E(X_n) = np$. ✓ (Linearity holds for *any* sum, no independence needed.)
- **Variance:** because the trials are independent, $\text{Var}(X) = \text{Var}(X_1) + \cdots + \text{Var}(X_n) = np(1-p)$. ✓ (Independence *is* needed for variance to add.)

This proof is a beautiful example of forward reading: define the right indicator decomposition, and the means and variances fall out by linearity in two lines each. Trying to compute $E(X) = \sum_{r=0}^{n} r \binom{n}{r} p^r (1-p)^{n-r}$ directly is a manipulation nightmare; via indicators, it's two lines.

> [!example] Worked — binomial calculation
> A biased coin lands heads with probability $0.3$. Toss it 10 times. Let $X$ be the number of heads.
>
> Forward read: 10 trials (fixed $n$), heads/tails (two outcomes), probability $0.3$ (constant), independent tosses. **All four conditions hold** ⟹ $X \sim B(10, 0.3)$.
>
> - $P(X = 3) = \binom{10}{3}(0.3)^3 (0.7)^7 = 120 \cdot 0.027 \cdot 0.0824 \approx 0.267$
> - $E(X) = 10 \cdot 0.3 = 3$
> - $\text{Var}(X) = 10 \cdot 0.3 \cdot 0.7 = 2.1$
> - $\sigma = \sqrt{2.1} \approx 1.45$

> [!warning] When binomial *doesn't* apply
> The four conditions are non-negotiable. If even one fails, the binomial formula gives wrong answers.
>
> - **"Drawing 3 cards from a deck without replacement, count the aces."** Trials are *not* independent — the probability of an ace on draw 2 depends on whether draw 1 was an ace. Not binomial. (This is the *hypergeometric* distribution — beyond P5.)
> - **"Number of phone calls in an hour."** No fixed $n$. (This is *Poisson* — see [[Poisson Distribution]] in P6 §6.1.)
> - **"Number of attempts until first success."** Counting "until" rather than "in $n$ trials" — not binomial; this is **geometric** (next section).

> [!info] Why the binomial earns its place despite the restrictions
> The four conditions are restrictive on paper. So why is the binomial the first distribution every probability course teaches, and the reference point for every distribution that follows? Short answer: it's the simplest non-trivial DRV; it's the building block for Poisson (via Euler's number), Normal (via the CLT), and Geometric (via reframing); and despite the conditions it still fits an enormous slice of real problems exactly (A/B testing, polling, QA, drug trials). See [[Why Probability and Statistics]] for the full case.

---

## The Geometric Distribution $X \sim \text{Geo}(p)$

The second named distribution. Used when the experiment has the structure:

### The setup

You repeat independent trials, each with success probability $p$, **until you get a success**. $X$ is the number of trials needed (including the successful one).

If $X = r$, that means: trials $1, 2, \dots, r-1$ all failed, and trial $r$ succeeded. By independence:

$$\boxed{\;P(X = r) = (1 - p)^{r - 1}\,p \qquad \text{for } r = 1, 2, 3, \dots\;}$$

This is a **geometric series** in $r$ — hence the distribution's name. Check that probabilities sum to 1:

$$\sum_{r=1}^{\infty} (1-p)^{r-1} p = p \cdot \frac{1}{1 - (1-p)} = p \cdot \frac{1}{p} = 1 \quad ✓$$

(Geometric series sum from [[Arithmetic and Geometric Progressions]]; first term $p$, ratio $1-p$, since $|1-p| < 1$.)

### Mean and variance

$$E(X) = \frac{1}{p} \qquad \text{Var}(X) = \frac{1 - p}{p^2}$$

**Heuristic for $E(X) = 1/p$.** If success has probability $p$ per trial, then on average you'd expect 1 success per $1/p$ trials — so the *average wait* until the first success is $1/p$. Confirmation by direct calculation:

$$E(X) = \sum_{r=1}^{\infty} r \cdot p (1-p)^{r-1}$$

Let $q = 1 - p$. The standard geometric-series trick: from $\sum_{r=0}^{\infty} q^r = \frac{1}{1-q}$, differentiate both sides with respect to $q$:

$$\sum_{r=1}^{\infty} r q^{r-1} = \frac{1}{(1-q)^2} = \frac{1}{p^2}$$

So $E(X) = p \cdot \frac{1}{p^2} = \frac{1}{p}$. ✓

(The variance derivation uses the second derivative — same flavor of trick.)

### Memoryless property — beyond syllabus, beautiful

A property unique to the geometric distribution among discrete distributions:

$$P(X > m + n \mid X > m) = P(X > n)$$

In words: "given that you've already failed $m$ times, the additional number of trials needed to get a success is distributed exactly as if you were starting fresh." The distribution **forgets** how many failures came before. (The exponential distribution is the continuous analog with the same property.)

This sounds suspicious — surely after many failures you're "due" for a success? — but no, that intuition is the **gambler's fallacy**. Independent trials are independent. Each failure tells you literally nothing about whether the next trial will succeed.

> [!example] Worked — geometric calculation
> A factory line produces an item; 4% of items are defective, 96% are good. An inspector picks items one at a time **until they find a defective**. Let $X$ be the number inspected (including the defective one).
>
> Forward read: independent trials (each item is independent), constant $p = 0.04$ (defect rate), trials continue **until first success**. ⟹ $X \sim \text{Geo}(0.04)$.
>
> - $P(X = 5) = (0.96)^4 \cdot 0.04 \approx 0.0339$ (probability the 5th item is the first defective)
> - $E(X) = \frac{1}{0.04} = 25$ (on average, 25 items inspected to find a defect)
> - $\text{Var}(X) = \frac{0.96}{0.04^2} = 600$
> - $\sigma = \sqrt{600} \approx 24.5$ (huge spread — geometric distributions have heavy tails)

> [!warning] What does $X$ count?
> Cambridge geometric problems use $X$ = *trials including the success*. Some textbooks define $Y$ = *failures before the first success*, in which case $Y = X - 1$, $E(Y) = (1-p)/p$, and $P(Y = k) = (1-p)^k p$. Read carefully — the convention matters.

---

## Common Failure Modes

### 1. "I'll use binomial without checking independence"

The most common DRV mistake. *Without replacement* problems often look binomial-flavored but aren't:

- **Binomial:** flip a coin 10 times → $X \sim B(10, 0.5)$. ✓
- **Not binomial:** draw 3 cards from a deck without replacement, $X$ = number of aces. ✗ (Probability of ace on draw 2 depends on draw 1 — hypergeometric, not binomial.)

The four conditions are a checklist, not a vibe.

### 2. "Expected value $E(X)$ is the most likely value"

No. $E(X)$ is the *long-run average*, not the *mode*. For a fair die, $E(X) = 3.5$, but every value is equally likely (no mode). For a binomial $B(10, 0.5)$, $E(X) = 5$ which happens to be the mode — coincidence, not law. Don't conflate them.

### 3. "Variance has the same units as $X$"

No — variance has units of $X^2$. This is why standard deviation $\sigma = \sqrt{\text{Var}(X)}$ is more interpretable; it's in the original units. (If $X$ is in metres, $\text{Var}(X)$ is in m², and $\sigma$ is in m.)

### 4. "Geometric distribution counts the failures"

By the Cambridge convention used in 9709 P5, $X$ counts the *trials including the success* — so $X \geq 1$, and $E(X) = 1/p$. If you accidentally apply the failures-before-success version, your mean comes out as $(1-p)/p$, off by 1. Read the question carefully — usually it says "the number of attempts" or "the number of throws" (including the successful one).

### 5. "Forgetting the sum-to-1 check"

Probability tables in exam questions often have one missing entry to be filled in by enforcing $\sum p_i = 1$. Always check the sum first; it's both a verification step (catches typos) and the answer to the "find $k$" problem.

### 6. "Confusing $E(X^2)$ with $(E(X))^2$"

These are different in general, and the difference *is* the variance:

$$\text{Var}(X) = E(X^2) - (E(X))^2 \geq 0$$

(With equality iff $X$ is constant.) The inequality is sometimes called the *non-negativity of variance* — a beautiful instance of $E(g(X))^2 \leq E(g(X)^2)$ for the function $g(X) = X$ (a shadow of Jensen's inequality, beyond syllabus).

---

## Cross-Domain Bridge — DRVs everywhere

The DRV framework with its $E(X), \text{Var}(X), B(n,p), \text{Geo}(p)$ vocabulary shows up across applied subjects:

| Domain | A discrete random variable in the wild |
|---|---|
| **Quality control** | Number of defective items in a batch — binomial |
| **Genetics** | Number of recessive alleles a child inherits — binomial |
| **Networking** | Number of dropped packets in $n$ transmissions — binomial |
| **Software testing** | Number of test cases failing in a regression suite — binomial |
| **Customer service** | Number of customers in a queue arriving in fixed window — binomial / Poisson |
| **Manufacturing** | Number of items inspected before finding a defect — geometric |
| **Telecommunications** | Number of retries before a successful transmission — geometric |
| **Sports analytics** | Number of free throws taken before a miss — geometric |
| **Cryptography** | Expected number of guesses to crack a passcode — geometric |
| **Quantum mechanics** | Number of photons detected in a fixed time — Poisson (related; P6) |
| **Physics — Statistical mechanics** | Number of particles in an energy state — discrete distributions everywhere |
| **Computer Science — algorithms** | Expected runtime of a randomised algorithm — direct $E(X)$ calculation |

A randomised algorithm in CS — quicksort with random pivots, randomised primality testing, hash tables under random hashing — is *literally* an experiment producing a DRV (the runtime), and the analyst's job is to compute $E(\text{runtime})$. Same act, different terrain.

> [!info] Beyond syllabus — the moment-generating function
> Both $E(X)$ and $\text{Var}(X)$ are **moments** of $X$ ($E(X)$ is the first moment, $E(X^2)$ is the second moment; variance is the *second central moment*). The full sequence $E(X), E(X^2), E(X^3), \dots$ characterises a distribution under mild conditions, and is packaged in the **moment-generating function** $M_X(t) = E(e^{tX})$. For binomial: $M_X(t) = (1 - p + pe^t)^n$. For geometric: $M_X(t) = \frac{pe^t}{1 - (1-p)e^t}$. Sums of independent variables become products of MGFs — the formula machinery that proves the Central Limit Theorem.

---

## Exam Notes

### Cambridge 9709 Paper 5 (P&S 1) — §5.4

- **The table is the machine:** draw up the probability distribution table, use $\sum p = 1$ to find the unknown (almost always the first mark), then $E(X) = \sum xp$ and $\text{Var}(X) = \sum x^2 p - \mu^2$ — the computing form, and the minus-$\mu^2$ is the classic dropped step.
- **Binomial:** justify the model *in the scenario's words* (fixed $n$, two outcomes, constant $p$, independent trials), compute $P(X = x)$ from the pmf, and use $E(X) = np$, $\text{Var}(X) = npq$.
- **Geometric:** "number of trials up to and including the first success" — $P(X = x) = q^{x-1}p$, $E(X) = 1/p$; the give-away phrase is *"until the first…"*, and $P(X > x) = q^x$ saves long sums.
- The binomial pmf is on MF19; the geometric results and $\text{Var} = \sum x^2p - \mu^2$ are **not** — know them cold.
- The linear-combination rules that build on these two numbers — $E(aX+b)$, sums, differences — are Paper 6 territory: [[Linear Combinations of Random Variables]].

### IB AA / AP

- **IB AA (SL 4.7–4.8):** distribution tables, $E(X)$ (fair-game questions are the favourite costume), and the binomial with its mean and variance — GDC-first culture, so table lookups become calculator syntax. The geometric distribution is not an AA statement.
- **AP Statistics** examines discrete RVs, binomial and geometric alike; AP Calculus does not touch them.

## Connections

- **Prerequisites:** [[Probability Basics]] (the probability framework), [[Combined Probability]] (independence and multiplication for the binomial PMF), [[Conditional Probability]] (memoryless property), [[Permutations and Combinations]] (the $\binom{n}{r}$ in the binomial), [[Arithmetic and Geometric Progressions]] (the geometric series sum used to verify $\sum P(X=r) = 1$ for $\text{Geo}(p)$ and to derive $E(X) = 1/p$).
- **Companion (philosophy):** [[Why Probability and Statistics]] — *why* statistics built variance the way it did, *why* the binomial earns its place despite four restrictive conditions, where Euler's number sneaks in via the Poisson limit, and (the harder half) when *not* to trust statistical thinking. The case for the tools and the case against the belief.
- **Leads to — directly next on P5:** [[Normal Distribution]] (P5 §5.5) — continuous distribution, also has $E$ and $\text{Var}$, also has a "standard form" (the standard normal $Z$). The normal distribution **approximates** the binomial when $n$ is large (CLT preview).
- **Leads to — P6:** [[Poisson Distribution]] (P6 §6.1) — third named discrete distribution, models event counts when there's no natural "$n$ trials" framing. Linked to binomial as a limit ($n \to \infty, p \to 0$, $np = \lambda$ fixed). [[Continuous Random Variables]] (P6 §6.3) — the integral version of this card.
- **Application across the vault:** every place where "expected number of X" or "long-run average" matters — [[Relative and Expected Frequency]] is the freshman version of $E(X)$; this card is the calculus.
- **Cross-domain (formal):** sums of independent DRVs (linearity + variance-addition) is the discrete version of the same machinery that runs through statistical inference, signal processing (where the DRV is a noise sample), queueing theory, randomized algorithms.

---

## What's on the formula sheet — and what isn't

> [!info] Formula-sheet status — Cambridge 9709 (List MF19)
> The 9709 exam gives you **List MF19**, a printed booklet of formulas. Anything in MF19 you do **not** need to memorise — be familiar with how to use it, and treat the sheet as your in-exam reference. Anything **not** in MF19, *if you're taking 9709, you need to memorise it* (or be able to re-derive it under exam time).
>
> **From this card, MF19 gives you (P&S 1 section):**
>
> - $E(X) = \Sigma xp$
> - $\text{Var}(X) = \Sigma x^2 p - \{E(X)\}^2$ — the **computational form** (the one you'll actually use)
> - **Binomial $B(n,p)$:** $p_r = \binom{n}{r} p^r (1-p)^{n-r}$, $\mu = np$, $\sigma^2 = np(1-p)$
> - **Geometric $\text{Geo}(p)$:** $p_r = p(1-p)^{r-1}$, $\mu = 1/p$
> - $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ (in the algebra section of MF19, used for the binomial PMF)
>
> **From this card, MF19 does NOT give you:**
>
> - **Geometric variance $\sigma^2 = \dfrac{1-p}{p^2}$** — *if you're taking 9709, memorise this.* It's the one variance the formula sheet leaves out from the discrete-distribution suite. The mean is given but the variance isn't. Cambridge has been known to ask for it.
> - **Linearity properties:** $E(aX+b) = aE(X) + b$, $E(X+Y) = E(X) + E(Y)$, $\text{Var}(aX+b) = a^2\,\text{Var}(X)$ — *not on the sheet, but understand them well.* The exam may ask you to apply them without ever stating the rule.
> - $\text{Var}(X) = E((X-\mu)^2)$ — the *defining* form of variance. The computational form $E(X^2) - (E(X))^2$ is what's on the sheet; this is the form you understand the meaning by.
> - **The four conditions for the binomial.** Not formulas, but a checklist you absolutely have to know.
>
> **Other exam boards have different formula booklets.** IB AA SL/HL, AP Statistics, A-Level (Edexcel/AQA/OCR) each provide their own. *Always check the formula booklet for your specific exam — what's free here may need memorising on a different paper, and vice versa.* See [[MF19 Reference (9709)]] for the full audit across 9709 P1, P4, P5.

---

## LaTeX Reference

| Symbol | Meaning |
|---|---|
| $X, Y, Z$ (capitals) | Random variables themselves |
| $x, y, z$ (lowercase) | Particular values they take |
| $P(X = x)$ | Probability that $X$ takes value $x$ |
| $E(X) = \sum x_i\,p_i$ | Expected value (mean) |
| $E(X^2) = \sum x_i^2\,p_i$ | Mean of the squares |
| $\text{Var}(X) = E(X^2) - (E(X))^2$ | Variance — the computational form (use this) |
| $\sigma = \sqrt{\text{Var}(X)}$ | Standard deviation |
| $\mu = E(X)$ | Common shorthand for the mean |
| $X \sim B(n, p)$ | $X$ is binomially distributed with parameters $n, p$ |
| $\binom{n}{r} p^r (1-p)^{n-r}$ | Binomial PMF: $P(X = r)$ |
| $E(X) = np$ | Binomial mean |
| $\text{Var}(X) = np(1-p)$ | Binomial variance |
| $X \sim \text{Geo}(p)$ | $X$ is geometrically distributed |
| $(1-p)^{r-1} p$ | Geometric PMF: $P(X = r)$ |
| $E(X) = 1/p$ | Geometric mean |
| $\text{Var}(X) = (1-p)/p^2$ | Geometric variance |
