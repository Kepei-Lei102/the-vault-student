---
chinese: 泊松分布 (bósōng fēnbù)
prerequisites:
  - "[[Discrete Random Variables]]"
  - "[[Exponential Function]]"
  - "[[Normal Distribution]]"
  - "[[Euler's Number]]"
  - "[[Why Probability and Statistics]]"
leads_to:
  - "[[Continuous Random Variables]]"
  - "[[Hypothesis Tests]]"
  - "[[Linear Combinations of Random Variables]]"
  - "[[Probability Generating Functions]]"
tags:
  - subject/mathematics
  - domain/probability
  - level/A-Level
  - curriculum/Cambridge-9709
  - syllabus/9709-6-1
  - type/deep
  - misconception/lambda-not-rescaled
  - misconception/poisson-vs-binomial
  - misconception/mean-equals-variance-proves-poisson
  - misconception/rare-means-small-lambda
---

# Poisson Distribution 泊松分布

> *How many typos on this page? Calls to a helpline in the next minute? Goals in Saturday's match? Clicks of a Geiger counter in a second? These questions share a shape: **counting arrivals in a window** — no fixed number of trials, no cap, just events dropping onto a timeline. One distribution answers all of them, and it needs only a single number to do it: the average rate. It is the mathematics of "things that just happen," and — sharper than that — it is the **null model of pure chance**: the honest baseline that tells you whether a cluster needs a cause at all.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| Poisson distribution | 泊松分布 | the count-of-events-in-a-window distribution, $X \sim \text{Po}(\lambda)$ |
| rate / mean rate | 平均发生率 | the single parameter $\lambda$: average events per window |
| occurrence / arrival | 事件发生 | one event landing in the window |
| singly | 逐个发生 | events arrive one at a time, never two at the exact same instant |
| uniform (constant) rate | 速率恒定 | the average rate doesn't drift across the window |
| approximation | 近似 | swapping one distribution for a close, easier one |
| continuity correction | 连续性修正 | the $\pm 0.5$ adjustment when a discrete count borrows a continuous curve |
| law of rare events | 稀有事件定律 | many tiny chances, added up, always produce this same shape |

## Meet it in the wild first

A helpline receives on average **3 calls per minute**. Nobody schedules the calls; they just arrive. In any given minute you might get 0, or 2, or 7. Here is what the Poisson model $X \sim \text{Po}(3)$ predicts:

| calls $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| $P(X=x)$ | .050 | .149 | .224 | .224 | .168 | .101 | .050 | .034 |

Notice what the model *didn't need*: no number of trials, no probability-per-trial — just the rate, 3. That is the whole signature. A [[Discrete Random Variables|binomial]] question hands you $n$ and $p$ ("20 shots, each scores with probability 0.3"); a Poisson question hands you a **rate in a window** ("3 per minute") and no ceiling on how many could arrive.

**Definition.** A random variable $X$ follows the **Poisson distribution** with parameter $\lambda > 0$, written $X \sim \text{Po}(\lambda)$, if

$$P(X = x) = e^{-\lambda}\,\frac{\lambda^x}{x!}, \qquad x = 0, 1, 2, \dots$$

The model is appropriate when events occur

1. **singly** — one at a time, never two at the same instant;
2. **independently** — one arrival tells you nothing about the next;
3. **at a constant average rate** — $\lambda$ per window, not drifting;
4. **randomly** — no schedule, no pattern.

These four conditions are examinable *in words*, and the exam's favourite trick is a scenario that breaks one: calls to a pizza shop are **not** constant-rate across a whole day (dinner rush), and infections are **not** independent (they cluster). Quoting the formula never substitutes for checking the conditions.

## Where the formula comes from — many small chances

The Poisson is not a new axiom; it is the [[Discrete Random Variables|binomial]] pushed to a beautiful limit. *Tool: slice the window.*

> [!note] Recall — the binomial in one line
> $X \sim B(n, p)$ says: $X$ counts the successes in $n$ independent trials, each succeeding with probability $p$, and
> $$P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}$$
> — choose *which* $x$ trials succeed, then multiply the chances. Full treatment in [[Discrete Random Variables]].

Cut the minute into $n$ tiny slices. If arrivals are random at rate $\lambda$ per minute, each slice independently contains an arrival with probability $p = \lambda/n$ (for huge $n$, slices are so thin that "two arrivals in one slice" becomes negligible — that is what *singly* buys us). So the count is binomial:

$$X \approx B\!\left(n, \tfrac{\lambda}{n}\right), \qquad P(X=x) = \binom{n}{x}\left(\frac{\lambda}{n}\right)^{x}\left(1-\frac{\lambda}{n}\right)^{n-x}.$$

Now let the slices shrink: $n \to \infty$. Take the three pieces one at a time:

$$\binom{n}{x}\frac{1}{n^x} = \frac{n(n-1)\cdots(n-x+1)}{x!\,n^x} \;\longrightarrow\; \frac{1}{x!}, \qquad
\left(1-\frac{\lambda}{n}\right)^{n} \;\longrightarrow\; e^{-\lambda}, \qquad
\left(1-\frac{\lambda}{n}\right)^{-x} \;\longrightarrow\; 1.$$

The first limit: for fixed $x$, each factor $\frac{n-k}{n} \to 1$. The second is the definition of $e$ from [[Exponential Function]] — the compound-interest limit $\left(1+\frac{t}{n}\right)^n \to e^{t}$ with $t = -\lambda$. Multiply the survivors:

$$P(X=x) \longrightarrow \frac{\lambda^x}{x!}\,e^{-\lambda}.$$

This derivation is the card's soul: **the Poisson is what "many independent small chances" always becomes.** It is why the same curve fits typos (many words, each with a tiny error chance), radioactive decay (astronomically many nuclei, each with a minuscule chance per second), and traffic accidents on a stretch of road. Nature runs this limit constantly; the distribution is just its fixed point — which is why the old name is the **law of rare events**. ("Rare" describes the per-slice chance $\lambda/n$, *not* the count: $\lambda = 100$ is a perfectly good Poisson.)

## Mean = variance = $\lambda$ — one number does both jobs

Both facts can be inherited from the binomial limit, one at a time:

- The binomial mean is $E(X) = np$. In our limit $p = \dfrac{\lambda}{n}$, so $E(X) = n \cdot \dfrac{\lambda}{n} = \lambda$ — true for *every* $n$, before the limit is even taken.
- The binomial variance is $\text{Var}(X) = np(1-p) = \lambda\left(1 - \dfrac{\lambda}{n}\right)$. As $n \to \infty$, the bracket $\to 1$, so $\text{Var}(X) \to \lambda$.

**A direct check from the definition** — walked slowly, because its two moves (shift the index, recognise a known series) are moves you will reuse for the rest of A-Level:

$$E(X) = \sum_{x=0}^{\infty} x \cdot P(X=x) = \sum_{x=0}^{\infty} x\, e^{-\lambda}\frac{\lambda^x}{x!}.$$

*Step 1 — drop the $x = 0$ term.* It contributes $0 \times P(X=0) = 0$, so the sum may start at $x = 1$ with nothing lost.

*Step 2 — cancel the $x$ into the factorial.* For $x \ge 1$, since $x! = x \cdot (x-1)!$, we have $\dfrac{x}{x!} = \dfrac{1}{(x-1)!}$. The sum becomes

$$E(X) = \sum_{x=1}^{\infty} e^{-\lambda}\,\frac{\lambda^{x}}{(x-1)!}.$$

*Step 3 — factor out everything that ignores the summation index.* The constant $e^{-\lambda}$, and one copy of $\lambda$ (writing $\lambda^x = \lambda \cdot \lambda^{x-1}$):

$$E(X) = \lambda\, e^{-\lambda} \sum_{x=1}^{\infty} \frac{\lambda^{x-1}}{(x-1)!}.$$

*Step 4 — re-index.* Let $j = x - 1$. As $x$ runs through $1, 2, 3, \dots$, $j$ runs through $0, 1, 2, \dots$:

$$E(X) = \lambda\, e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^{j}}{j!}.$$

*Step 5 — recognise the series.* The sum is exactly the [[Exponential Function]] power series, $e^{\lambda} = \sum_{j \ge 0} \dfrac{\lambda^j}{j!}$. So

$$E(X) = \lambda\, e^{-\lambda} \cdot e^{\lambda} = \lambda. \qquad \blacksquare$$

(The same machinery applied to $E[X(X-1)]$ delivers the variance — a genuinely good exercise once these five steps feel routine.)

$$E(X) = \text{Var}(X) = \lambda.$$

This is both a formula and a **diagnostic**: given real count data, compare the sample mean with the sample variance. Close together → Poisson is a candidate model; variance much larger → the events are *clumping* (not independent), and the model is honestly wrong. Exam questions ask exactly this comparison and want exactly that reasoning.

## $\lambda$ lives on the window — always rescale first

The most-dropped mark in the topic is not the formula. It is this: **the parameter belongs to the interval you were asked about, not the interval you were told about.**

Calls arrive at 3 per minute. Questions about a 5-minute window use $\text{Po}(15)$. Questions about 20 seconds use $\text{Po}(1)$. Rescale *first*, then compute — every Poisson solution should begin with a sentence like "In 5 minutes, $X \sim \text{Po}(15)$."

Two useful facts ride along:

- **Additivity.** If $X \sim \text{Po}(\lambda)$ and $Y \sim \text{Po}(\mu)$ are independent, then $X + Y \sim \text{Po}(\lambda + \mu)$. Emails at 2 per hour plus texts at 5 per hour → messages at $\text{Po}(7)$ per hour. (Windows rescale for the same reason: a 5-minute count is the sum of five independent 1-minute counts.)
- **Consecutive probabilities are neighbours:** $\frac{P(X=x+1)}{P(X=x)} = \frac{\lambda}{x+1}$ — handy for quick tables and for seeing why the histogram rises while $x < \lambda$ and falls after.

## The two approximations — the traffic between distributions

![[poisson-approximations.svg|697]]

**Binomial → Poisson** (*when $n$ is large and $p$ is small*). If $X \sim B(n,p)$ with $n > 50$ and $np < 5$ (the 9709 rule of thumb), then $X \approx \text{Po}(np)$. This is just the limit above, used in reverse as a labour-saving device: $B(1000, 0.003)$ probabilities are miserable to compute directly; $\text{Po}(3)$ is two lines.

**Poisson → Normal** (*when $\lambda$ is large*). For $\lambda > 15$ or so, $\text{Po}(\lambda) \approx N(\lambda, \lambda)$ — mean $\lambda$, variance $\lambda$, the same number wearing both hats. Because a count is discrete and the [[Normal Distribution]] is continuous, apply the **continuity correction**: $P(X \ge 35)$ becomes $P(Y > 34.5)$. The picture to keep: as $\lambda$ grows the Poisson histogram loses its skew and settles into the bell — the same story the binomial told, one distribution downstream.

The full map of traffic: $B(n,p)$ flows to $\text{Po}(np)$ when $p$ is tiny, and everything flows to the normal when the numbers get large. The normal is the sea; the Poisson is one of the rivers.

## Worked examples — every tool named

**(a) Direct probabilities, with a rescale.** *A website receives errors at an average rate of 1.8 per hour. Find the probability of (i) exactly 3 errors in 2 hours, (ii) at least 2 errors in 2 hours.*

*Tool: rescale $\lambda$ to the question's window, then apply the pmf; "at least" goes through the complement.*

In 2 hours, $X \sim \text{Po}(3.6)$.

(i) $P(X=3) = e^{-3.6}\dfrac{3.6^3}{3!} = e^{-3.6}\cdot\dfrac{46.656}{6} \approx 0.212.$

(ii) $P(X \ge 2) = 1 - P(X=0) - P(X=1) = 1 - e^{-3.6}(1 + 3.6) \approx 1 - 0.1257 \approx 0.874.$

**(b) Poisson as a stand-in for binomial.** *A factory's items are defective independently with probability $0.004$. In a batch of 1000, find the probability of at most 2 defectives.*

*Tool: check the approximation conditions, then swap. $n = 1000 > 50$, $np = 4 < 5$ — approve. $X \approx \text{Po}(4)$.*

$$P(X \le 2) \approx e^{-4}\left(1 + 4 + \frac{4^2}{2}\right) = 13\,e^{-4} \approx 0.238.$$

State the check — "$n$ large, $np < 5$, so Po(4) is appropriate" — the sentence *is* a mark.

**(c) Normal as a stand-in for Poisson.** *A hospital ward admits patients at an average rate of 30 per week. Estimate the probability of at least 35 admissions next week.*

*Tool: $\lambda = 30 > 15$, so $X \approx N(30, 30)$; discrete-to-continuous demands the continuity correction.*

$$P(X \ge 35) \approx P\!\left(Z > \frac{34.5 - 30}{\sqrt{30}}\right) = P(Z > 0.8215) \approx 0.206.$$

The two danger spots: the variance is $30$ (not $30^2$ — the standard deviation is $\sqrt{30}$), and $34.5$ (not $35.5$: "at least 35" keeps 35 in, so the boundary slides *down* to 34.5).

> [!warning] The hospital example is a sandbox, not a claim about hospitals
> Real admissions are *not* independent and *not* constant-rate: flu seasons, weekend effects, one accident delivering five patients at once, a full ward diverting ambulances. Real hospital data usually shows exactly the overdispersion this card warns about — and real causality all the way down. The example exists to get your hands dirty with the mechanics; a working statistician's *first* job on real admissions data would be to test the Poisson's four conditions, not assume them. Exam scenarios grant the assumptions; the world does not.

## The clustering illusion — Poisson as the hunter's null model

During the V-1 flying-bomb attacks on London, the hits seemed to *cluster* — some districts struck again and again, others spared — and people inferred precision targeting, spies, causes. In 1946 the actuary R. D. Clarke divided south London into 576 half-kilometre squares, counted hits per square, and compared the counts with $\text{Po}(0.93)$. The fit was nearly perfect: **the clusters were exactly what pure chance produces.** Randomness is lumpy; uniformity is what design looks like.

Half a century earlier, Ladislaus Bortkiewicz had made the same point with a gentler dataset — deaths by horse-kick in Prussian cavalry corps, 0.61 per corps per year, Poisson to the decimal.

Keep this as a thinking tool — but state it *precisely*, because it is easy to overclaim in both directions. A good Poisson fit does **not** prove the events are causeless; no fit can prove that. What it licenses is sharper and humbler: **this data shows no clear evidence of any causality pushing the counts away from pure randomness.** Clarke's grid didn't prove the V-1s were unguided — it showed that the clustering *alone* could not support the targeting theory, because chance fully explains lumps of that size. Absence of evidence for a cause; never evidence of absence.

So the mature skill is two-sided. **One:** don't hunt causes that chance already explains — disease clusters, three shipment failures in a week, a fund manager's four good years in a row are all, on their own, within what "no cause at all" routinely produces. **Two:** don't *stop* hunting just because the first test comes back "consistent with random" — real causality often hides inside apparent noise, and extracting it is exactly what the hardest modern inference does (a diffusion model's entire job is to walk from what looks like pure noise back to the structure buried in it). Markets are the canonical two-sided case: chaotic enough that naive cause-hunting sees patterns everywhere, causal enough that "it's all random" is also wrong. The Poisson doesn't end the hunt — it **disciplines** it. The invariant ([[Forward Reading and Problem Discovery]]) is how much clustering "no cause" produces; only the excess above that baseline calls for the chase, and that is where your search effort should go.

## Misconceptions

> [!warning] "The rate was 2 per hour, the question asked about 3 hours, I used $\lambda = 2$."
> The single most-dropped mark. $\lambda$ belongs to the *question's* window: $\text{Po}(6)$. Begin every solution by declaring the rescaled distribution.

> [!warning] "Counting things, so it's binomial. Or Poisson. Whichever."
> One question decides: **is there a fixed number of trials with a built-in ceiling?** Twenty seeds, each germinating or not → $B(20, p)$; the count can't exceed 20. Cars passing a junction in a minute → no ceiling, only a rate → Poisson. Binomial counts successes *out of $n$*; Poisson counts arrivals *out of nowhere*.

> [!warning] "Sample mean ≈ sample variance, so the data is Poisson."
> The right direction, stated too strongly. Mean ≈ variance is *consistent with* Poisson (and mean ≪ variance genuinely rules it out — clumping), but other distributions can match too. It's a screening test, not a proof — say "consistent with", collect the mark, stay honest.

> [!warning] "Rare events — so $\lambda$ must be small."
> "Rare" lives in the derivation (each tiny slice of the window almost never fires), not in the count. $\text{Po}(100)$ is legitimate — and that is precisely when you reach for the normal approximation.

> [!info] Beyond syllabus — the Poisson's family
> - **The Poisson process, and the exponential gap.** Count arrivals and you get Poisson; ask instead *how long until the next arrival* and you get the exponential distribution with mean $1/\lambda$ — the same phenomenon read by a clock instead of a counter, and the bridge into [[Continuous Random Variables]]. The waiting time is **memoryless**: having already waited ten minutes makes the bus no more due — the continuous twin of the geometric memorylessness met in [[Discrete Random Variables]].
> - **Overdispersion — when reality clumps.** Real counts (website hits, insurance claims, goals when a red card changes everything) often show variance well above the mean, because arrivals *aren't* independent. Statisticians reach for the negative binomial; the Poisson stays valuable precisely as the baseline that made the clumping visible.
> - **Football and the betting markets.** Goals per match track Po(≈1.4 per side) closely enough that bookmakers' scoreline models are Poisson at heart (with correlation patches for 0–0 and 1–1). A worked reminder that "model of rare arrivals" prices real money.
> - **Radioactive decay is the physics-lab Poisson:** a Geiger counter's clicks in a fixed window are the textbook's cleanest real dataset — astronomically many nuclei, each with a minuscule chance per second: the limit derivation running live on a bench.
> - **The generating-function view (9231's angle):** $G_X(t) = e^{\lambda(t-1)}$, from which mean, variance, and additivity ($G_{X+Y} = G_X G_Y$) all fall out in one line each — the Further-Maths toolkit that turns this card's facts into corollaries.

## Exam Notes

### Cambridge 9709 Paper 6 (Probability & Statistics 2) — §6.1

- **The five jobs of the LO:** (1) recognise/justify the Poisson as a model — the four conditions *in the scenario's words* (singly, independently, constant average rate, at random); (2) compute probabilities with the pmf, including "at least/at most" via complements; (3) use $E(X) = \text{Var}(X) = \lambda$, including the mean-vs-variance model check on data; (4) **binomial → Poisson** approximation with the stated check ($n > 50$, $np < 5$, approximately); (5) **Poisson → normal** approximation ($\lambda > 15$, approximately) **with continuity correction** — the correction is a named marking point.
- **Rescaling $\lambda$ to the question's interval is the topic's #1 skill**, and combining independent Poisson streams (additivity) is examined explicitly.
- **The pmf is on MF19** (with $\mu = \lambda$, $\sigma^2 = \lambda$); the *conditions* and the *approximation thresholds* are **not** — memorise those.
- Hypothesis tests **on a Poisson mean** arrive in §6.5 ([[Hypothesis Tests]]) — the model here is the machine those tests run on.

### Cambridge 9231 Further Maths (Further Probability & Statistics)

- The Poisson returns twice: inside [[Probability Generating Functions]] (derive mean/variance/additivity from $e^{\lambda(t-1)}$) and as a target of **$\chi^2$ goodness-of-fit** — fitting Po($\bar{x}$) to observed counts and testing the fit, the formal version of this card's mean-vs-variance diagnostic.

### Other boards

- **Edexcel IAL (S2):** same core — model conditions, probabilities, additivity, approximations; the skills transfer verbatim.
- **IB:** Mathematics AI HL includes the Poisson (modelling emphasis); AA does not examine it.

## Connections

- **Parent:** [[Discrete Random Variables]] — the binomial whose $n\to\infty,\ p\to 0$ limit this card takes, and the geometric whose memorylessness the Poisson process inherits in continuous time.
- **Uses:** [[Exponential Function]] — the $\left(1-\frac{\lambda}{n}\right)^n \to e^{-\lambda}$ limit is the compound-interest definition of $e$ doing probability's work; [[Normal Distribution]] — the destination of the second approximation, continuity correction and all.
- **Leads to:** [[Continuous Random Variables]] — the exponential waiting time between Poisson arrivals is the natural first pdf; [[Hypothesis Tests]] — P6's tests on a Poisson mean run on this model.
- **Method:** [[Forward Reading and Problem Discovery]] — the clustering illusion section is that card's thesis pointed at randomness: establish the invariant (what pure chance produces) before hunting causes in the residue.
- **Physics bridge:** radioactive decay counts are Poisson — the Geiger counter is the cleanest laboratory instance of the limit derivation.

## What's on the formula sheet — and what isn't

**MF19 gives:** $p_r = e^{-\lambda}\dfrac{\lambda^r}{r!}$ with $\mu = \lambda$, $\sigma^2 = \lambda$.
**MF19 does not give:** the four model conditions; the approximation directions and thresholds ($n>50,\ np<5$ → Poisson; $\lambda > 15$ → normal); the continuity correction; additivity. Those live in your head.

## Glossary

| term | 中文 | one-liner |
|---|---|---|
| parameter $\lambda$ | 参数 λ | the average number of events in the window — mean *and* variance |
| rescaling | 区间换算 | converting $\lambda$ to the question's interval before anything else |
| additivity | 可加性 | independent Poisson counts add: $\text{Po}(\lambda)+\text{Po}(\mu)=\text{Po}(\lambda+\mu)$ |
| law of rare events | 稀有事件定律 | many tiny independent chances always sum to a Poisson |
| continuity correction | 连续性修正 | the $\pm 0.5$ boundary shift when a count borrows the normal curve |
| overdispersion | 过度离散 | variance $>$ mean: the data clumps and the model waves a flag |
| clustering illusion | 聚类错觉 | reading causes into the lumps that pure chance guarantees |

## LaTeX Reference

| Symbol | Meaning | Notes |
|---|---|---|
| $X \sim \text{Po}(\lambda)$ | Poisson with parameter $\lambda$ | one parameter carries mean and variance |
| $P(X=x) = e^{-\lambda}\lambda^x/x!$ | the pmf | on MF19 |
| $E(X) = \text{Var}(X) = \lambda$ | mean = variance | the model's fingerprint |
| $B(n,p) \approx \text{Po}(np)$ | binomial → Poisson | $n>50$, $np<5$, approximately |
| $\text{Po}(\lambda) \approx N(\lambda, \lambda)$ | Poisson → normal | $\lambda > 15$, continuity correction required |
