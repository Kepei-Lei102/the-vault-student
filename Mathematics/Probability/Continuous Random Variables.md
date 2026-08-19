---
chinese: 连续随机变量 (liánxù suíjī biànliàng)
prerequisites:
  - "[[Discrete Random Variables]]"
  - "[[Integration]]"
  - "[[Poisson Distribution]]"
  - "[[Linear Combinations of Random Variables]]"
  - "[[Normal Distribution]]"
leads_to:
  - "[[Sampling and Estimation]]"
  - "[[Hypothesis Tests]]"
  - "[[Chi-Squared Tests]]"
tags:
  - subject/mathematics
  - domain/probability
  - domain/statistics
  - domain/calculus
  - level/A-Level
  - curriculum/Cambridge-9709
  - curriculum/Cambridge-9231
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/9709-6-3
  - syllabus/9231-4-1
  - type/definition
  - type/technique
  - notation/pdf
  - notation/cdf
  - misconception/density-is-not-probability
  - misconception/probability-zero-not-impossible
  - misconception/strict-vs-inclusive
  - misconception/transform-pdf-by-substitution
---

# Continuous Random Variables 连续随机变量

> *Ask the strangest question in the statistics course: what is the probability that a randomly chosen student is **exactly** 170 cm tall — not 170.0001, not 169.9999, but 170 point zero zero zero, forever? The honest answer is **zero**: an interval of heights holds infinitely many values, and no single exact one can claim a share. And yet somebody* is *that tall — zero-probability things happen all day. The way out of the paradox is the biggest change of viewpoint in the course: for continuous quantities, probability stops living at points and moves into **intervals**. It stops being a count and becomes an **area** — and the curve whose area it is, the probability density function, runs the rest of P6. If you have ever looked at a histogram's y-axis and wondered why it says frequency* density*, you have already met the idea.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| continuous random variable | 连续随机变量 | a random quantity taking values from an interval of $\mathbb{R}$, not a list |
| probability density function (pdf) | 概率密度函数 | the curve $f(x)$ whose **area** over an interval is the probability of landing there |
| cumulative distribution function (cdf) | 累积分布函数 | the running total $F(x) = P(X \leqslant x)$ — area accumulated so far |
| median / percentile | 中位数 / 百分位数 | the value splitting the area 50/50 (or $p$ / $1-p$) |
| mode | 众数 | where the density curve peaks — the most crowded neighbourhood |
| expectation $E(X)$ | 期望 | the balance point of the density curve |
| variance $\mathrm{Var}(X)$ | 方差 | the spread of the chance-mass about its balance point |
| uniform (rectangular) distribution | 均匀分布（矩形分布） | constant density — "completely random in $[a,b]$" made precise |
| support | 支撑集 | the interval where $f(x) > 0$ — where the variable actually lives |

## The dictionary — every discrete formula survives

You already own this subject. [[Discrete Random Variables]] built the whole machine — table, total 1, expectation, variance — and the continuous version is the *same machine* with one translation applied everywhere: **sums become integrals, and probabilities $p_k$ become slivers of area $f(x)\,dx$.**

| Discrete (a list of values) | Continuous (an interval of values) |
|---|---|
| probability table: $P(X = k) = p_k$ | density curve: $f(x)$ |
| $\sum_k p_k = 1$ | $\int_{\text{all }x} f(x)\,dx = 1$ |
| $P(a \leqslant X \leqslant b) = \sum_{a \leqslant k \leqslant b} p_k$ | $P(a \leqslant X \leqslant b) = \int_a^b f(x)\,dx$ |
| $E(X) = \sum k\,p_k$ | $E(X) = \int x\,f(x)\,dx$ |
| $\mathrm{Var}(X) = \sum k^2 p_k - \mu^2$ | $\mathrm{Var}(X) = \int x^2 f(x)\,dx - \mu^2$ |
| $E(g(X)) = \sum g(k)\,p_k$ | $E(g(X)) = \int g(x)\,f(x)\,dx$ |

One physical metaphor carries the whole card: **the density function is a mass density for chance.** Think of a thin steel rod whose thickness varies along its length. No single *point* of the rod weighs anything — yet every *stretch* of it has weight, and the whole rod weighs exactly 1. Wherever the rod is thick, the random variable lands often; where it is thin, rarely.

## Where the discrete machinery breaks

Why can't we keep the table? Because there is no table. The values in an interval like $[160, 190]$ cannot be listed — not even with an infinite list (the reals are *uncountable*, the deep fact behind [[Countability]]). And if every one of those values had some positive probability $p > 0$, any list of more than $1/p$ of them would already push the total past 1. The conclusion is forced, not chosen:

$$P(X = a) = 0 \quad \text{for every single value } a.$$

Individual values are ruined as carriers of probability — so the *interval* takes over the job, and the natural bookkeeping for "how much stuff sits over an interval" is exactly what [[Integration]] was built for.

## The pdf — probability as area

First, a collision to defuse: **pdf** on this card is short for *probability density function* — nothing to do with the document format, which borrowed the letters in 1993 while statisticians had been writing "p.d.f." in textbooks for decades. Every pdf below is a curve, not a file.

A function $f(x)$ is a **probability density function** for $X$ if:

1. $f(x) \geqslant 0$ everywhere — no negative chance anywhere, and
2. $\displaystyle\int_{\text{all }x} f(x)\,dx = 1$ — the whole rod weighs 1,

and then probabilities are read as areas:

$$\boxed{\;P(a \leqslant X \leqslant b) = \int_a^b f(x)\,dx\;}$$

![[continuous-rv-sum-vs-area.svg|660]]

Three consequences fall out immediately, and each one is exam-relevant:

- **$P(X = a) = 0$** — an area of width zero. Probability zero, note, is *not* the same as impossible (more below).
- **Strict and inclusive inequalities agree:** $P(X < a) = P(X \leqslant a)$, because the endpoint contributes zero area. The $<$ vs $\leqslant$ paranoia you drilled for the binomial *dissolves* here — a genuine relief. (Do not export the relief backwards: in discrete land the distinction still costs marks.)
- **The density can exceed 1.** $f(x)$ is not a probability — it is probability *per unit length*, and $f(x)\,dx$, density × width, is the probability. The uniform density on $[0, \tfrac12]$ is $f(x) = 2$ and breaks no rules: tall × narrow can still have area 1. You met this exact idea on a histogram's y-axis: frequency **density** × class width = frequency ([[Histograms]] — a histogram is an empirical pdf wearing data).

### Finding $k$ — the invariant that never changes

Nearly every exam question opens with a density carrying an unknown constant, $f(x) = kx^2$ on $[0, 3]$, and asks for $k$. Read forward for the invariant ("what doesn't change?"): *the total area is always 1.* That single fact prices $k$:

$$\int_0^3 kx^2\,dx = k\left[\tfrac{x^3}{3}\right]_0^3 = 9k = 1 \;\Rightarrow\; k = \tfrac{1}{9}.$$

## Mean and variance — the balance point and the wobble

$$E(X) = \int x\,f(x)\,dx = \mu, \qquad \mathrm{Var}(X) = \int x^2 f(x)\,dx - \mu^2.$$

**Why the first formula:** $E(X)$ is a weighted average — each location $x$, weighted by the sliver of chance $f(x)\,dx$ sitting there. Physically it is the **centre of mass** of the chance-rod: the point where the rod balances on a fingertip. That is why a symmetric pdf has its mean at the centre line with no integration needed.

**Why the second:** same computational shortcut as the discrete case — $\mathrm{Var}(X) = E(X^2) - [E(X)]^2$, "mean of the square minus square of the mean," proved in [[Discrete Random Variables]] by algebra that never cared whether the expectation was a sum or an integral. And the physics reading goes one step deeper: $\int (x-\mu)^2 f\,dx$ is precisely the **moment of inertia** of the chance-mass about its balance point ([[Moment of Inertia]] — same integral, same meaning: how hard the distribution is to spin about its centre, i.e. how far its mass sprawls).

Both boxed formulas are printed on MF19, and every rule from [[Linear Combinations of Random Variables]] — $E(aX+b)$, $\mathrm{Var}(aX+b) = a^2\mathrm{Var}(X)$, the perpendicular-arrows addition for independent variables — carries over to continuous variables *unchanged*: those proofs only ever used the linearity of expectation, which integrals supply as happily as sums.

## Median, percentiles, mode — reading the area directly

The **median** $m$ is the value that splits the area in half:

$$\int_{\text{lower end}}^{m} f(x)\,dx = \tfrac12,$$

and the $p$-th percentile is the same equation with $\tfrac{p}{100}$ on the right. No new theory — you write the area as an integral in $m$, set it equal to the target, and solve the resulting equation. The **mode** is simply where $f$ peaks: differentiate and set $f'(x) = 0$, or read it off a monotone or vertex shape by eye.

Take the syllabus's own specimen, $f(x) = \dfrac{3}{x^4}$ for $x \geqslant 1$ — a density on an *infinite* domain (allowed, as long as the total area converges to 1):

![[continuous-rv-median-mean.svg|660]]

Mode $1$ (the curve only ever falls), median $\sqrt[3]{2} \approx 1.26$ (solve $1 - m^{-3} = \tfrac12$), mean $\tfrac32$ (worked below). The ordering **mode < median < mean** is the fingerprint of a right-skewed density: the long tail can't outvote the crowd for the median (which only counts *how much* area is out there), but it *drags the mean*, which weights area by how far away it sits.

## The cdf — the running total

Everything above reads areas one interval at a time. There is a tidier bookkeeping: accumulate the area **once**, from the left, and keep the running total as a function:

$$F(x) = P(X \leqslant x) = \int_{\text{lower end}}^{x} f(t)\,dt.$$

$F$ is the **cumulative distribution function** — the odometer to the pdf's speedometer. It starts at 0, never decreases, and ends at 1. Probabilities become subtractions, $P(a < X \leqslant b) = F(b) - F(a)$, and the median is just $F(m) = \tfrac12$ — no fresh integral each time.

And the way back down is the Fundamental Theorem of Calculus wearing a probability costume:

$$\boxed{\;F'(x) = f(x)\;}$$

— *the slope of the accumulated area is the height of the curve.* Differentiate the odometer, recover the speedometer. Here is the whole relationship run live — the scanning line sweeps, the area pours in, and $F$ climbs to 1:

![[continuous-rv-cdf-odometer.mp4]]

![[continuous-rv-pdf-cdf.svg|660]]

> [!info] Who examines what
> **9709 P6 never requires the cdf** — the syllabus asks for medians and percentiles "by direct consideration of an area", and every P6 answer can be a plain definite integral. Use $F$ as understanding, not as required notation. **9231 Paper 4 examines the relationship in both directions**: pdf → cdf by integrating, cdf → pdf by differentiating, and either one as the route to probabilities and percentiles. If you are headed to Further Maths, make the odometer picture second nature now.

## Two residents you will keep meeting

**The uniform (rectangular) distribution** on $[a, b]$: $f(x) = \dfrac{1}{b-a}$ — constant density, the phrase "a point is chosen at random in the interval" made precise. By symmetry $E(X) = \dfrac{a+b}{2}$; one integral gives $\mathrm{Var}(X) = \dfrac{(b-a)^2}{12}$. It is the simplest possible pdf, and the secret engine of every computer simulation (see Beyond).

**The exponential distribution** — the bridge [[Poisson Distribution]] promised. If arrivals happen at rate $\lambda$ per unit time, ask not *how many arrive* (Poisson) but *how long until the next one*. Call the waiting time $T$, and read $P(T > t)$ as plain English: *the probability that the wait is longer than $t$.* Now the key observation: "the wait is longer than $t$" and "the window $[0,t]$ contains **zero** arrivals" are the *same event* — so the Poisson formula with $k = 0$ prices it:

$$P(T > t) = P(\text{zero arrivals in } [0,t]) = \frac{e^{-\lambda t}(\lambda t)^0}{0!} = e^{-\lambda t}.$$

That is the complement of the odometer, $1 - F(t)$, so $F(t) = 1 - e^{-\lambda t}$ — and differentiating recovers the pdf:

$$f(t) = \lambda e^{-\lambda t}, \quad t \geqslant 0.$$

![[continuous-rv-exponential.svg|660]]

Same phenomenon, read by a clock instead of a counter — and notice the cdf arrived *first*, with the pdf recovered by differentiating: the odometer relationship earning its keep on day one. $E(T) = 1/\lambda$ (rate 3 per hour → mean wait 20 minutes — the bus stop of Example 4), and the distribution is **memoryless**: having already waited ten minutes makes the bus no more due — the continuous twin of the geometric memorylessness in [[Discrete Random Variables]].

## Changing variable — always walk through the cdf

The 9231 question: $X$ has a known distribution, $Y = g(X)$ — find the distribution of $Y$. The discipline that always works: **transform the event, not the formula.**

$$F_Y(y) = P(Y \leqslant y) = P(g(X) \leqslant y) = P(X \leqslant g^{-1}(y)) = F_X(g^{-1}(y)),$$

then differentiate at the end if the pdf is wanted. (For a *decreasing* $g$ the inequality flips when you undo it — solve the event honestly each time rather than memorising a formula.)

*Worked — on something you can hold.* A sweet factory's cutter produces sugar cubes of random side $X$ cm, with pdf $f_X(x) = 3x^2$ on $[0,1]$ — the machine favours large cubes (density piled toward 1). What the packaging line *cares* about is the **volume**, $Y = X^3$ cm³ — which is exactly the syllabus's own transform pattern, now with sugar on it. First, the odometer of $X$: $F_X(x) = \int_0^x 3t^2\,dt = x^3$. Then transform the event, for $0 \leqslant y \leqslant 1$:

$$F_Y(y) = P(Y \leqslant y) = P(X^3 \leqslant y) = P(X \leqslant y^{1/3}) = F_X(y^{1/3}) = (y^{1/3})^3 = y.$$

So $F_Y(y) = y$ and $f_Y(y) = 1$ on $[0,1]$: the volume is **uniform** — every volume from 0 to 1 cm³ equally likely, a perfectly flat answer out of a lopsided input. (No accident, as Beyond reveals.)

What you may **not** do is substitute into the pdf: $f_Y(y) \neq f_X(y^{1/3})$. The pdf is a density — a rate of area per unit length — and stretching the axis by $g$ changes the lengths, so a stretch-factor (the derivative of $g^{-1}$, arriving automatically via the chain rule when you differentiate $F_Y$) must appear. Route through the cdf and the bookkeeping does itself.

And this is a working tool, not exam furniture — **real measurement chains are transforms.** You *measure* a ball bearing's radius but *care* about its volume ($\propto X^3$); you measure a pipe's bore but care about its flow capacity ($\propto X^4$); a pendulum's length, but its period ($\propto \sqrt{X}$). Cubing a variable roughly *triples its relative wobble* — a 1% spread in radius is a 3% spread in volume — which is why a machinist quotes tolerances on the dimension they can actually control, and why [[Error Propagation]] in the physics lab is this section's twin: the same chain rule, pointed at uncertainties instead of pdfs.

## Worked examples

### Example 1 (9709 P6 — the standard five-parter)

> $f(x) = k(2x+1)$ on $0 \leqslant x \leqslant 2$, and $0$ otherwise. Find $k$, $P(X < 1)$, $E(X)$, $\mathrm{Var}(X)$, and the median.

*Tool: the invariant — total area 1.*
$$\int_0^2 k(2x+1)\,dx = k\big[x^2+x\big]_0^2 = 6k = 1 \;\Rightarrow\; k = \tfrac16.$$

*Tool: probability is area.*
$$P(X < 1) = \tfrac16\big[x^2+x\big]_0^1 = \tfrac{2}{6} = \tfrac13.$$

*Tool: $E(X) = \int x f$ (on MF19).*
$$E(X) = \tfrac16\int_0^2 (2x^2+x)\,dx = \tfrac16\left[\tfrac{2x^3}{3}+\tfrac{x^2}{2}\right]_0^2 = \tfrac16\cdot\tfrac{22}{3} = \tfrac{11}{9}.$$

*Tool: $\mathrm{Var} = E(X^2) - \mu^2$ (on MF19).*
$$E(X^2) = \tfrac16\int_0^2 (2x^3+x^2)\,dx = \tfrac16\left[\tfrac{x^4}{2}+\tfrac{x^3}{3}\right]_0^2 = \tfrac{16}{9}, \qquad \mathrm{Var}(X) = \tfrac{16}{9} - \left(\tfrac{11}{9}\right)^2 = \tfrac{23}{81}.$$

*Tool: median splits the area — set the running area to $\tfrac12$.*
$$\tfrac16(m^2+m) = \tfrac12 \;\Rightarrow\; m^2+m-3 = 0 \;\Rightarrow\; m = \tfrac{-1+\sqrt{13}}{2} \approx 1.30,$$
taking the root inside $[0,2]$. Sanity check: the density *rises* across the interval, so the chance-mass piles up on the right and the short tail is on the left — mean $\tfrac{11}{9} \approx 1.22$ sits *below* the median, the left-skew fingerprint, and both sit right of the midpoint 1.

### Example 2 (9709 P6 — infinite domain, the syllabus's specimen)

> $f(x) = \dfrac{3}{x^4}$ for $x \geqslant 1$. Find $P(X > 2)$, $E(X)$, $\mathrm{Var}(X)$ and the median.

*Tool: probability is area (to infinity — take the limit).*
$$P(X > 2) = \int_2^\infty 3x^{-4}\,dx = \big[-x^{-3}\big]_2^\infty = \tfrac18.$$

*Tool: $E(X) = \int x f$.*
$$E(X) = \int_1^\infty 3x^{-3}\,dx = \left[-\tfrac{3}{2}x^{-2}\right]_1^\infty = \tfrac32, \qquad E(X^2) = \int_1^\infty 3x^{-2}\,dx = 3, \qquad \mathrm{Var}(X) = 3 - \tfrac94 = \tfrac34.$$

*Tool: median — running area equals $\tfrac12$.*
$$\int_1^m 3x^{-4}\,dx = 1 - m^{-3} = \tfrac12 \;\Rightarrow\; m = \sqrt[3]{2} \approx 1.26.$$

Mode 1, median 1.26, mean 1.5: the right tail drags the mean, exactly the ordering in the figure above.

### Example 3 (9231 — piecewise pdf and the cdf)

> $f(x) = \dfrac{x}{4}$ on $[0,2]$, $\dfrac{4-x}{4}$ on $[2,4]$, $0$ otherwise (a triangle). Find $F(x)$, the lower quartile, and $P(X > 3)$.

*Tool: the cdf is accumulated area — integrate piece by piece, carrying the running total across the join.*
For $0 \leqslant x \leqslant 2$: $F(x) = \int_0^x \tfrac{t}{4}\,dt = \tfrac{x^2}{8}$. At the join, $F(2) = \tfrac12$ (by the symmetry of the triangle — a free check). For $2 \leqslant x \leqslant 4$:
$$F(x) = \tfrac12 + \int_2^x \tfrac{4-t}{4}\,dt = 1 - \tfrac{(4-x)^2}{8}.$$
(Neat habit: verify $F(4) = 1$ — the odometer must end at 1.)

*Tool: quartile — set $F = \tfrac14$, choosing the correct piece.*
$\tfrac14 < F(2) = \tfrac12$, so the lower quartile lives on the first piece: $\tfrac{q^2}{8} = \tfrac14 \Rightarrow q = \sqrt{2} \approx 1.41$.

*Tool: complement through the cdf.*
$$P(X > 3) = 1 - F(3) = 1 - \left(1 - \tfrac{1}{8}\right) = \tfrac18.$$

### Example 4 (real world — the 20-minute bus)

> Buses pass a stop at an average rate of 3 per hour, at random (Poisson) times. You walk up at a random moment. (i) Find the probability you wait more than 30 minutes. (ii) Find the median wait. (iii) You have already waited 10 minutes; find the probability you wait at least 30 minutes *more*.

*Tool: the exponential cdf, $F(t) = 1 - e^{-\lambda t}$, with $\lambda = 3/60 = 0.05$ per minute.*
$$\text{(i)}\quad P(T > 30) = e^{-0.05 \times 30} = e^{-1.5} \approx 0.223.$$
Better than a one-in-five chance of a miserable wait, at a stop whose *average* is twenty minutes — the tail is fatter than intuition expects.

*Tool: median — set the odometer to $\tfrac12$.*
$$\text{(ii)}\quad 1 - e^{-0.05m} = \tfrac12 \;\Rightarrow\; m = \frac{\ln 2}{0.05} \approx 13.9 \text{ minutes}.$$
Median 13.9 < mean 20 — the right-skew fingerprint from the figure above: *most* waits are short, but the occasional stranding drags the mean.

*Tool: memorylessness.*
$$\text{(iii)}\quad P(T > 40 \mid T > 10) = \frac{P(T > 40)}{P(T > 10)} = \frac{e^{-2}}{e^{-0.5}} = e^{-1.5} \approx 0.223$$
— identical to (i). The ten minutes already served count for nothing; the bus does not know you are waiting.

## Common Misconceptions (Teaching Notes)

### 1. "The height of the curve is the probability"

A student reads $f(2) = 0.75$ and writes $P(X=2) = 0.75$. **Fix:** the rod. Density is weight *per centimetre*, not weight — a point of the rod weighs nothing, and only density × width means anything. Then show a legal pdf with $f > 1$ (uniform on $[0, \tfrac12]$: $f = 2$) — if height were probability, that curve would be a scandal; as a density it is innocent.

### 2. "Probability zero means it can't happen"

$P(X = 170) = 0$, yet someone is exactly 170 cm tall. **Fix:** throw a dart at a board — it certainly lands *somewhere*, yet every individual point had probability zero. Zero probability means "no share of the area", not "excluded from the world". The exam consequence is the useful part: endpoints never matter, so $P(X < a) = P(X \leqslant a)$, always.

### 3. "I must fuss over $<$ versus $\leqslant$ here too"

The reverse error — the discrete drill exported forward. Continuous: endpoints carry no area, so the two are equal and no continuity-correction-style adjustment ever applies to a genuine continuous variable. **Fix:** the fuss belongs to *discrete* variables (and to discrete variables being *approximated* by continuous ones — that is what the continuity correction in [[Normal Distribution]] is for). Ask "is the variable itself discrete or continuous?" before deciding whether the endpoint fuss applies.

### 4. "To get the pdf of $Y = X^3$, substitute into the pdf of $X$"

Writing $f_Y(y) = f_X(y^{1/3})$ — no. Densities are *rates*, and changing variable stretches the axis, so a stretch-factor must appear. **Fix:** forbid formula-substitution entirely; the only sanctioned route is through the *event*: $F_Y(y) = P(g(X) \leqslant y)$, solve the inequality, express via $F_X$, differentiate last. The chain rule then produces the stretch-factor automatically — the method is self-correcting.

## Exam Notes

### Cambridge 9709 — P6 §6.3

- **What is asked:** properties of a pdf (non-negative, area 1 — the "find $k$" opener); probabilities as areas; $E(X)$ and $\mathrm{Var}(X)$; median and percentiles **by direct consideration of an area**. Densities are defined **over a single interval only**, but the domain may be infinite (the syllabus's own example is $\tfrac{3}{x^4}$ for $x \geqslant 1$ — Example 2 above).
- **The cdf is explicitly not required** ("explicit knowledge of the cumulative distribution function is not included"). Every P6 answer can be a plain definite integral with $m$ in the limit.
- **MF19 gives** both $E(X) = \int x f\,dx$ and $\mathrm{Var}(X) = \int x^2 f\,dx - \mu^2$; the median/mode definitions and the area-equals-1 normalisation live in your head.
- **Habits that earn marks:** state the support and integrate over it (if the support is $[1, 2]$, then $P(X < 3) = 1$ — the exam does set this trap); when solving for a median, reject roots outside the support *with a reason*; quote answers to 3 s.f. per the front cover.

### Cambridge 9231 — Further Probability & Statistics §4.1

- Everything in P6 §6.3 is assumed, then extended: pdfs **defined piecewise** (Example 3); the general $E(g(X)) = \int g(x) f(x)\,dx$; the **pdf ↔ cdf relationship in both directions**, with either usable for probabilities and percentiles; and **cdfs of related variables** — the syllabus's own instance is $Y = X^3$ (worked above). The always-through-the-cdf discipline is the whole game.
- Piecewise cdfs must carry the accumulated total across each join (the $F(2) = \tfrac12$ move in Example 3) — forgetting the carried constant is the standard error.

### IB AA HL

- Continuous random variables with an explicit pdf — $E(X)$, variance, median, mode from the density — are **HL** territory (SL and AI meet only the normal distribution, as a calculator object). The methods on this card transfer directly; IB phrasing leans on GDC integration, so practise both the exact-integral and calculator routes.

### AP Statistics

- Density curves appear *conceptually* — area = probability, the uniform and normal as the stock examples — but with **no calculus**: no finding $k$, no integral formulas for mean or variance. The normal distribution carries the entire continuous story.

## Beyond the syllabus

> [!info] Dice before darts — which probability came first?
> The discrete came first, by nearly two centuries. Probability was born at the gambling table — Cardano's manual on games of chance (c. 1564), then the Pascal–Fermat letters of 1654 on how to split the stakes of an interrupted game — and everything in it was countable: dice faces, cards, wins. The continuous was invented later, and for an ironic reason: **as a shortcut through the discrete.** In 1733 Abraham de Moivre, facing binomial sums like $\sum \binom{1000}{k} p^k q^{1000-k}$ that nobody could add by hand, drew a smooth curve through the tops of the probability sticks and *integrated instead of adding* — and that curve was the normal distribution, the first pdf in history, born as an approximation device. So the historical arrow points opposite to the pedagogical one: this card teaches discrete → continuous as a *generalisation*, but history built the continuous to **avoid adding up** the discrete. Laplace and Gauss then made the smooth curve the foundation of error theory ([[Normal Distribution]], and the naming saga in [[Stories/The Naming of Normal]]), and only in 1933 did Kolmogorov put both kinds under one roof, with sums and integrals as two faces of one measure. A living fossil of the birth is still on your syllabus: the **continuity correction** — that $\pm 0.5$ you apply when a normal approximates a binomial is de Moivre's 1733 move run in reverse, every single time.

> [!info] The computer's dice — inverse transform sampling
> The sugar-cube surprise ($Y = X^3$ turning out uniform) is a special case of a lovely general fact: for any continuous $X$ with cdf $F$, the variable $U = F(X)$ is **uniform on $[0,1]$** — run any random quantity through its own odometer and you get pure flat randomness. Read backwards, this is a machine: take a uniform random number $u$ (which computers generate cheaply) and compute $X = F^{-1}(u)$ — you have manufactured a random variable with *any* cdf you like. One line, $-\tfrac{1}{\lambda}\ln(1-u)$, turns flat noise into exponential waiting times. Every simulation, every game's loot-drop timer, every Monte Carlo model breathes through this trick.

> [!info] Heavy tails — when the mean stops existing
> Meet the family $f(x) = \tfrac{c}{x^n}$ on $x \geqslant 1$. Our specimen $n = 4$ has a mean and a variance. Drop to $n = 3$: the mean exists but $E(X^2) = \int 2x^{-1}dx$ diverges — **finite mean, infinite variance**. Drop to $n = 2$: not even the mean survives. These are the *Pareto* tails — income distributions, city sizes, insurance claims, market crashes — where "average" behaviour is dominated by rare enormous values, and the 80/20 rule lives. The small print this exposes: the Central Limit Theorem that will power [[Sampling and Estimation]] *demands finite variance* — heavy-tailed reality is exactly where naive averaging fails.

> [!info] What "probability zero" really means
> "Possible but probability zero" bothered mathematicians too. The modern resolution (Kolmogorov, 1933) defines probability as a *measure* — a generalised area — and areas simply ignore individual points, or even any countable set of points ([[Countability]] is the load-bearing wall: the rationals in $[0,1]$, infinitely many of them, still carry total probability zero under a uniform density). Events of probability 1 are said to happen *almost surely* — the "almost" being the measure-zero escape hatch. It is the same mathematics that makes "the area under a single point of a curve" zero in [[Integration]].

## Connections

- **Builds on:** [[Discrete Random Variables]] — the parallel story this card translates, sum by sum, into integrals; [[Integration]] — the engine: every probability on this card is a definite integral, and $F' = f$ is the Fundamental Theorem in costume; [[Poisson Distribution]] — whose arrival counts hand us the exponential waiting time, the first natural pdf; [[Linear Combinations of Random Variables]] — the $E$/$\mathrm{Var}$ exchange rules, proved by linearity, carrying over unchanged.
- **Leads to:** [[Sampling and Estimation]] — $\bar{X}$ is a continuous random variable, and the CLT is a statement about its pdf; [[Hypothesis Tests]] — p-values are tail areas under these curves.
- **Kindred:** [[Normal Distribution]] — the most famous pdf of all, met before this card existed; its density has no elementary antiderivative, which is *why* the z-table exists — the cdf tabulated by hand; [[Histograms]] — frequency density is the empirical pdf, area = frequency; [[Moment of Inertia]] — variance is the moment of inertia of the chance-mass about its balance point, the same integral in two sciences; [[Error Propagation]] — the changing-variable section's physics twin: the same chain rule, pointed at lab uncertainties instead of pdfs.
- **For 9709/9231 students:** [[MF19 Reference (9709)]] — the two continuous-RV integral formulas are on the sheet; median/mode definitions and the area-1 normalisation are not.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $f(x)$ | `f(x)` | probability density function |
| $F(x)$ | `F(x)` | cumulative distribution function $P(X \leqslant x)$ |
| $\int_a^b f(x)\,dx$ | `\int_a^b f(x)\,dx` | probability as area; `\,` for the thin space before $dx$ |
| $\leqslant$ | `\leqslant` | Cambridge's slanted ≤ (interchangeable with `\le`) |
| $\mu$, $\sigma^2$ | `\mu`, `\sigma^2` | mean, variance |
| $E(g(X))$ | `E(g(X))` | expectation of a function of $X$ (9231) |
| $\sqrt[3]{2}$ | `\sqrt[3]{2}` | the specimen median |
| $\mathrm{Var}(X)$ | `\mathrm{Var}(X)` | upright Var per house style |
| $\lambda e^{-\lambda t}$ | `\lambda e^{-\lambda t}` | exponential pdf |
