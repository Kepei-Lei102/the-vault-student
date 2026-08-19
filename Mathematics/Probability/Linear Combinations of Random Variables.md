---
chinese: 随机变量的线性组合 (suíjī biànliàng de xiànxìng zǔhé)
prerequisites:
  - "[[Discrete Random Variables]]"
  - "[[Normal Distribution]]"
  - "[[Poisson Distribution]]"
leads_to:
  - "[[Continuous Random Variables]]"
  - "[[Sampling and Estimation]]"
  - "[[Stories/Inventing Variance]]"
  - "[[Inventing Variance]]"
  - "[[Probability Generating Functions]]"
tags:
  - subject/mathematics
  - domain/probability
  - domain/statistics
  - level/A-Level
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/9709-6-2
  - type/theorem
  - type/methodology
  - misconception/variances-never-subtract
  - misconception/sd-adds-linearly
  - misconception/nx-vs-n-copies
  - misconception/independence-forgotten
---

# Linear Combinations of Random Variables 随机变量的线性组合

> *Here is the strangest plus sign in the course. Take two random quantities and **subtract** them — the length of a bolt minus the depth of its hole, battery A's life minus battery B's. The average behaves politely: it subtracts. The uncertainty does not. **It adds.** Two shaky hands do not steady each other; a wobbly bolt in a wobbly hole is doubly uncertain to fit. This card is about the two currencies of randomness — the mean and the variance — and the exchange rules they obey when variables combine: means add like lengths along a line, but independent noises add like **perpendicular arrows**. Once you see the right triangle hiding in that sentence, the whole topic is four rules and one famous trap.*

![[lincomb-shaky-hands-comic.png|640]]

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| linear combination | 线性组合 | an expression $aX + bY + c$ built from random variables with fixed numbers |
| expectation / mean | 期望 / 均值 | the long-run average $E(X)$ — where the distribution balances |
| variance | 方差 | $\text{Var}(X) = E\big[(X-\mu)^2\big]$ — the average *squared* distance from the mean |
| standard deviation | 标准差 | $\sigma = \sqrt{\text{Var}}$ — spread in the variable's own units |
| shift | 平移 | adding a constant: $X + b$ — moves the distribution, shape unchanged |
| scaling | 缩放 | multiplying by a constant: $aX$ — stretches the distribution |
| independent | 独立 | one variable's outcome tells you nothing about the other's |
| identically distributed | 同分布 | drawn from the same distribution — clones in law, not in outcome |
| in quadrature | 平方相加（勾股式） | combining by squares: $\sqrt{\sigma_1^2 + \sigma_2^2}$ — Pythagoras for noise |

## The two currencies

Recall from [[Discrete Random Variables]] that a random variable carries two headline numbers: $E(X) = \mu$, where its distribution balances, and $\text{Var}(X) = E\big[(X-\mu)^2\big] = \sigma^2$, the average *squared* deviation from that balance point. This card answers one question: **when you build a new variable out of old ones — scale it, shift it, add two together, subtract them — what happens to those two numbers?**

The answer splits cleanly. The mean is obedient: it does exactly what the algebra does. The variance has rules of its own — and its rules are where every mark on this topic is won or lost.

## One variable: stretch and shift

Take $X$ and build $aX + b$ — a temperature in °F from one in °C ($F = 1.8C + 32$), a cost from a quantity ($C = 0.05X + 20$).

$$\boxed{E(aX+b) = a\,E(X) + b \qquad \text{Var}(aX+b) = a^2\,\text{Var}(X)}$$

**Why the mean obeys.** Expectation is a weighted sum, and multiplying-then-adding inside a sum factors straight out:
$$E(aX+b) = \sum_x (ax+b)\,P(X=x) = a\sum_x x\,P(X=x) + b\sum_x P(X=x) = aE(X) + b,$$
using $\sum P = 1$ for the last step. The mean rides along with any linear recipe.

**Why the shift vanishes from the variance.** Variance measures deviations *from the mean* — and shifting everything by $b$ shifts the mean by $b$ too, so every deviation $x - \mu$ is untouched. Moving the whole class three seats to the left changes nobody's distance from the class average. Formally, the deviations of $aX+b$ are
$$(ax + b) - (a\mu + b) = a(x - \mu),$$
and squaring pulls out $a^2$:
$$\text{Var}(aX+b) = E\big[a^2 (X-\mu)^2\big] = a^2\,\text{Var}(X).$$

Two habits worth wiring in now: the constant $b$ **never** touches the variance, and the factor comes out **squared** — so it cannot make a variance negative ($a = -2$ gives $\times 4$, not $\times(-2)$), and the standard deviation scales by $\lvert a \rvert$.

## Two variables: means on a line, noises at right angles

Now combine two variables: $aX + bY$.

$$\boxed{E(aX + bY) = a\,E(X) + b\,E(Y)} \qquad \text{always, no conditions}$$

$$\boxed{\text{Var}(aX + bY) = a^2\,\text{Var}(X) + b^2\,\text{Var}(Y)} \qquad \textbf{for independent } X, Y$$

The asymmetry in the small print is the deep fact of this card. Expectation is *linear* unconditionally — even for dependent variables, means combine like ordinary numbers. Variance demands **independence**, and here is why. Write $D_X = X - \mu_X$ and $D_Y = Y - \mu_Y$ for the deviations, and expand for the sum:

$$\text{Var}(X+Y) = E\big[(D_X + D_Y)^2\big] = E\big[D_X^2\big] + E\big[D_Y^2\big] + 2\,E\big[D_X D_Y\big].$$

The first two terms are $\text{Var}(X)$ and $\text{Var}(Y)$. The third — the **cross term** — asks: *do the two deviations lean the same way at the same time?* If $X$ and $Y$ are independent, $D_X$ is as likely to be positive as negative regardless of what $D_Y$ is doing, and the products cancel out on average: $E[D_X D_Y] = 0$. The cross term dies, and variances simply add.

![[lincomb-pythagoras.svg|697]]

That is exactly the geometry of perpendicular vectors, and the analogy is precise: **independent noises are at right angles**, and their standard deviations combine by Pythagoras. If $\sigma_X = 3$ and $\sigma_Y = 4$, then $\sigma_{X+Y} = \sqrt{9+16} = 5$ — never $7$. The variance rule *is* $c^2 = a^2 + b^2$, dressed in probability. (When the variables are *not* independent, the cross term survives with a name of its own — see Beyond.)

And you do not have to take the algebra's word for it. Below, the cross term is put on trial with **genuinely random data** — drawn fresh on the date stamped in the corner, using that date as the seed. Rerun the script on another day and every dot moves; the two squared terms stay fat and the cross term starves to zero again. *The draw changes; the law does not* — which is the entire subject, in one production detail.

![[lincomb-cross-term.mp4]]

## The star of the show: the minus that becomes plus

Apply the rules to a **difference**, $X - Y$, which is just $aX + bY$ with $a = 1,\ b = -1$:

$$E(X - Y) = \mu_X - \mu_Y \qquad \text{but} \qquad \text{Var}(X-Y) = 1^2\,\sigma_X^2 + (-1)^2\,\sigma_Y^2 = \boxed{\sigma_X^2 + \sigma_Y^2}.$$

The mean subtracts; the variance **still adds**, because $(-1)^2 = 1$. And it *must*: subtracting an uncertain quantity cannot make you more certain. Whether $Y$ is added to $X$ or removed from it, its wobble comes along. A bolt of uncertain length in a hole of uncertain depth has a doubly uncertain clearance — the two wobbles compound, they never cancel.

![[lincomb-distributions.svg]]

The picture is worth staring at: $X + Y$ and $X - Y$ are **equally wide**. The minus sign moved the center and did nothing else. If you remember one image from this card, make it this one — Paper 6 asks for the distribution of a *difference* more often than a sum, precisely to see who writes $\sigma_X^2 - \sigma_Y^2$ (which can go negative — an impossibility that should set off alarms, since a variance is an average of squares).

## The famous trap: $3X$ is not $X_1 + X_2 + X_3$

Here is the distinction that decides more §6.2 marks than any other. Let a coffee machine dispense $X$ ml per cup, with mean $\mu$ and variance $\sigma^2$.

- **$3X$ means one cup, tripled** — one random pour, photocopied three times. Whatever wobble the single pour had, tripling magnifies it: $E(3X) = 3\mu$, $\text{Var}(3X) = 9\sigma^2$.
- **$X_1 + X_2 + X_3$ means three cups** — three *independent* pours, each wobbling on its own. Same mean, $3\mu$, but the wobbles partly cancel (one pour runs heavy, another light): $\text{Var} = \sigma^2 + \sigma^2 + \sigma^2 = 3\sigma^2$.

Same expectation, **different variance** — $9\sigma^2$ against $3\sigma^2$ — because one photocopied error is not three errors averaging out. *Tool: read the scenario for independence — "three cups" are three variables; "triple the cup" is one variable scaled.* The exam signals the difference with exactly those words.

![[lincomb-nx-vs-sum.svg]]

Again — real data, on trial. The same date-seeded random stream pours actual cups: the left strip triples one pour per trial, the right strip sums three independent pours. Watch the left strip sprawl to twice the width, and check the measured spreads against the predicted $\sqrt{9\sigma^2} = 12$ and $\sqrt{3\sigma^2} \approx 6.9$:

![[lincomb-3x-vs-sum.mp4]]

And hiding inside this trap is the reason statistics works at all. The **average** of $n$ independent copies is a linear combination too:
$$\bar{X} = \tfrac{1}{n}(X_1 + \cdots + X_n) \quad\Rightarrow\quad E(\bar{X}) = \mu, \qquad \text{Var}(\bar{X}) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}.$$
Averaging keeps the mean and **divides the variance by $n$** — noise shrinks like $1/\sqrt{n}$ while the signal stands still. Every lab that averages repeated readings ([[Repeated Measurements]]) and every poll that surveys a thousand people instead of ten is spending this one formula. It is the engine of [[Sampling and Estimation]], and you have just derived it in two lines.

## Which shapes survive combining

The rules above give the *numbers* of $aX + bY$. Two families also keep their *shape* — and Paper 6 leans on both:

- **Normal stays normal.** If $X$ is normal, so is $aX + b$; and if $X, Y$ are **independent** normals, then $aX + bY$ is normal too — with the mean and variance the boxed rules supply. Bell plus bell is bell: sums of independent bell curves never grow a second hump or a lopsided tail. (The honest proof needs machinery beyond the syllabus — see Beyond — but the payoff is immediate: any probability about a combination of normals is one standardisation away.)
- **Poisson sums stay Poisson.** Recall from [[Poisson Distribution]] that independent Poisson streams pool: $X \sim \text{Po}(\lambda)$ and $Y \sim \text{Po}(\mu)$ give $X + Y \sim \text{Po}(\lambda + \mu)$ — emails at 2 per hour plus texts at 5 per hour is messages at 7 per hour. But the **difference of two Poissons is *not* Poisson** — and be precise about what that means. Nothing is floored at zero: $X - Y$ is a perfectly legitimate random variable that simply takes values on *all* the integers, $\ldots, -2, -1, 0, 1, 2, \ldots$ — a football goal difference is exactly this, and a loss is a negative one. What $X - Y$ has stopped being is a **count**, and Poisson is a distribution *of counts* — its support starts at $0$, so no choice of parameter can ever describe a variable that goes negative. The difference has its own distribution, with its own name — see Beyond. The exam's version of all this: only the *sum* result is on the syllabus, and quoting a "Po$(\lambda - \mu)$" is an instant lost mark.

## Worked example 1 — stretch, shift, and read the units

> *A machine dispenses $X$ ml of juice per cup, where $E(X) = 249$ and $\text{Var}(X) = 16$. The cost of a cup, in cents, is $C = 0.3X + 15$. Find $E(C)$, and the standard deviation of $C$.*

*Tool: the single-variable rules — the mean rides the recipe; the shift never touches the spread.*

$$E(C) = 0.3 \times 249 + 15 = 89.7 \text{ cents}.$$
$$\text{Var}(C) = 0.3^2 \times 16 = 1.44 \quad\Rightarrow\quad \sigma_C = \sqrt{1.44} = 1.2 \text{ cents}.$$

The $15$ appears in the mean and nowhere else; the $0.3$ enters the variance squared and leaves the standard deviation as $0.3 \times 4$.

## Worked example 2 — the lift: a sum of copies, then a normal probability

> *The masses of adults are distributed as $N(75, 12^2)$ kg, independently. Four adults enter a lift with a safety limit of 340 kg. Find the probability their total mass exceeds the limit.*

*Tool: sum of independent copies (not $4X$!) — then normal-stays-normal, then standardise.*

Let $T = X_1 + X_2 + X_3 + X_4$, four **independent** masses:
$$E(T) = 4 \times 75 = 300, \qquad \text{Var}(T) = 4 \times 144 = 576, \qquad \sigma_T = 24.$$
$T$ is a linear combination of independent normals, so $T \sim N(300, 576)$. Then
$$P(T > 340) = P\!\left(Z > \frac{340 - 300}{24}\right) = P(Z > 1.667) = 1 - \Phi(1.667) \approx 0.0478.$$

About a 5% chance — and note the trap dodged: $\text{Var}(4X) = 16 \times 144$ would have doubled $\sigma$ and roughly quadrupled the tail. Four passengers are four draws, not one passenger photocopied.

## Worked example 3 — the difference: does A beat B?

> *Brand A batteries last $X \sim N(52, 3^2)$ hours; Brand B batteries last $Y \sim N(50, 4^2)$ hours, independently. Find the probability that a randomly chosen A outlasts a randomly chosen B.*

*Tool: turn a comparison into a difference — then the minus-becomes-plus rule, then standardise.*

"A outlasts B" is $X > Y$, i.e. $D = X - Y > 0$. Build $D$'s distribution:
$$E(D) = 52 - 50 = 2, \qquad \text{Var}(D) = 3^2 + 4^2 = 25, \qquad D \sim N(2, 5^2).$$
$$P(D > 0) = P\!\left(Z > \frac{0 - 2}{5}\right) = P(Z > -0.4) = \Phi(0.4) \approx 0.655.$$

Two-thirds of head-to-heads go to A. The whole question turned on one move — variances **added** under the minus sign, giving $\sigma_D = 5$ by the 3-4-5 triangle of the Pythagoras picture.

## Misconceptions

> [!warning] "$\text{Var}(X-Y) = \text{Var}(X) - \text{Var}(Y)$."
> The single most-penalised line on Paper 6. Coefficients enter the variance **squared**, and $(-1)^2 = 1$: uncertainty compounds whether you add or subtract. The sanity check is built in — the subtraction version can output a *negative variance*, an average of squares that is somehow below zero. Alarm bells, always.

> [!warning] "Standard deviations add: $\sigma_{X+Y} = \sigma_X + \sigma_Y$."
> Only *variances* add. Standard deviations combine by Pythagoras: $3$ and $4$ make $5$, not $7$. Adding $\sigma$s linearly is the "worst-case" arithmetic of [[Error Propagation]]'s crude bounds — probability is kinder, because independent wobbles spend much of their time partially cancelling.

> [!warning] "$nX$ and $X_1 + \cdots + X_n$ are the same thing."
> Same mean, different worlds: $\text{Var}(nX) = n^2\sigma^2$ but $\text{Var}(X_1+\cdots+X_n) = n\sigma^2$. One scaled photocopy versus $n$ independent draws whose errors partly cancel. Read the scenario: *"the total of 5 bags"* is a sum of copies; *"5 times the weight of one bag"* is a scaling.

> [!warning] "The variance rule works for any $X$ and $Y$."
> $\text{Var}(aX+bY) = a^2\text{Var}(X) + b^2\text{Var}(Y)$ **requires independence** — that is what killed the cross term in the derivation. The exam supplies the word ("independently", "at random from separate populations"); your solution should *use* it, and examiners look for the word "independent" beside the variance line. (What happens when it fails — see Beyond.)

## Exam Notes

### Cambridge 9709 Paper 6 (Probability & Statistics 2) — §6.2

- **The six results, verbatim from the syllabus:** $E(aX+b) = aE(X)+b$ and $\text{Var}(aX+b) = a^2\text{Var}(X)$; $E(aX+bY) = aE(X)+bE(Y)$; $\text{Var}(aX+bY) = a^2\text{Var}(X)+b^2\text{Var}(Y)$ *for independent* $X, Y$; normal $X$ gives normal $aX+b$; independent normal $X, Y$ give normal $aX+bY$; independent Poisson $X, Y$ give Poisson $X+Y$. **Proofs are explicitly not required** — the derivations in this card are for understanding, not reproduction.
- **The standard question shapes:** (1) build the distribution of a sum/difference/combination and find a probability (Worked 2 and 3 — the *difference* version dominates); (2) the $nX$-vs-$n$-copies discrimination, often as "total contents of 6 tins" against "6 times one tin"; (3) a Poisson pooling step feeding a Poisson probability; (4) occasionally a two-stage build, e.g. $2X - 3Y$ with everything above at once.
- **Where marks leak:** $\sigma^2 - \sigma^2$ under a minus sign; forgetting to square coefficients; quoting $\sigma$ where $\text{Var}$ is needed (or vice versa — read which the question wants); dropping the independence justification; and treating "the mean of 4 observations" as anything other than $\bar{X}$ with variance $\sigma^2/4$.
- MF19 carries none of this — the rules live in your head.

### Cambridge 9231 Further Maths (Further Probability & Statistics)

- These rules are load-bearing background: [[Probability Generating Functions]] re-derive them in a line ($G_{X+Y} = G_X G_Y$ for independent variables — the Poisson pooling falls out instantly), and the estimation chapters lean on $\text{Var}(\bar{X}) = \sigma^2/n$ throughout.

### IB / AP

- **IB AA (HL)** examines the single-variable transform $E(aX+b)$, $\text{Var}(aX+b)$; combinations of *several* variables sit beyond AA (they appear on the AI HL side). The derivations here cover the AA statement with room to spare.
- **AP Statistics** tests exactly these combining rules (means and variances of sums and differences of independent variables), in calculator-flavoured dress; AP Calculus does not.

## Beyond the syllabus

> [!info] When independence fails: the cross term gets a name
> Recall the derivation: the cross term $2E[D_X D_Y]$ died *because* independence made the deviations uncorrelated. In general it lives, and it is called the **covariance**, $\text{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]$:
> $$\text{Var}(aX+bY) = a^2\text{Var}(X) + b^2\text{Var}(Y) + 2ab\,\text{Cov}(X,Y).$$
> Positive covariance — deviations leaning the same way — makes sums *more* volatile than Pythagoras predicts; negative covariance makes them calmer. This one term is the mathematical heart of **portfolio diversification**: hold two independent risks and returns add linearly while noise adds only in quadrature — a genuine free lunch — but let the assets become correlated (as they famously do in a crash, when everything falls together) and the $2ab\,\text{Cov}$ term hands the risk right back. The diversification the brochure promised was a statement about covariance, whether the brochure knew it or not.

> [!info] Why normal-plus-normal is normal
> The clean proof convolves the densities or multiplies **moment generating functions**: the normal's MGF is $e^{\mu t + \sigma^2 t^2/2}$, and multiplying two of them visibly produces a third with the means and variances added — three lines of algebra in the right notation. The deeper reason bells are everywhere is the **Central Limit Theorem**: sums of *many* independent variables drift toward normal *whatever* their shapes — the normal family is not just closed under addition, it is where addition ends up. That theorem is the main act of [[Sampling and Estimation]].

> [!info] The difference of two Poissons: the Skellam distribution
> The variable $D = X - Y$ for independent $X \sim \text{Po}(\lambda)$, $Y \sim \text{Po}(\mu)$ follows the **Skellam distribution**, living on every integer. This card's own rules still govern its headline numbers: $E(D) = \lambda - \mu$ and — minus-becomes-plus, one more time — $\text{Var}(D) = \lambda + \mu$. Its shape is a discrete near-bell centred at $\lambda - \mu$, leaning slightly toward the busier stream (the exact pmf needs Bessel functions, which is why it stays beyond every syllabus). The natural habitat is **football**: home goals and away goals are each nearly Poisson, so the *goal difference* — the thing the league table, the handicap market and your heart actually care about — is nearly Skellam, with $D = 0$ pricing the draw. The negative values aren't a defect to be floored away; they are the away wins.

> [!info] The $\sqrt{n}$ law, everywhere you look
> $\text{Var}(\bar{X}) = \sigma^2/n$ is the same fact as: a drunkard's walk of $n$ steps wanders only $\sim\sqrt{n}$ from the lamppost; $n$-fold repeated lab readings deserve error bars $\sigma/\sqrt{n}$ ([[Repeated Measurements]], [[Error Propagation]]); and doubling a poll's precision costs *four times* the sample. Signal grows like $n$, independent noise like $\sqrt{n}$ — most of applied statistics is arbitrage between those two growth rates.

## Connections

- **Builds on:** [[Discrete Random Variables]] — the $E$ and $\text{Var}$ machinery these rules run on; [[Normal Distribution]] — the shape that survives combining, and the standardisation that finishes every worked example; [[Poisson Distribution]] — whose additivity is the syllabus's third closure fact.
- **Leads to:** [[Sampling and Estimation]] — $\bar{X}$ with $\text{Var} = \sigma^2/n$ is this card's averaging result promoted to the main character, and the CLT crowns it; [[Continuous Random Variables]] — the pdf machinery that makes these statements precise beyond the discrete case.
- **Kindred:** [[Repeated Measurements]] — the lab-bench face of $\sigma/\sqrt{n}$; [[Error Propagation]] — this card in physics costume: quadrature for independent errors, and worst-case linear addition as the pessimist's bound; [[Vectors]] — perpendicular components combining by Pythagoras is literally the same picture.
