---
chinese: MF19 公式表对照（进阶数学）(gōngshì biǎo duìzhào — jìnjiē shùxué)
prerequisites: []
leads_to: []
tags:
  - subject/mathematics
  - domain/exam-strategy
  - level/A-Level
  - curriculum/A-Level
  - curriculum/Cambridge-9231
  - type/reference
  - type/exam-technique
---

# MF19 Reference (9231) — the Further half of the booklet

## What this card is for

MF19 is **one booklet serving two qualifications**, and in the exam room it is one physical object with no partition in it. There is no "your half". A 9231 candidate reads the Pure pages exactly as freely as the Further ones; a 9709 candidate can turn to the Further pages too, and simply finds nothing examinable there. The split below is about *which syllabus rows the formulas serve*, never about which pages anyone is permitted to open.

[[MF19 Reference (9709)]] audits the first half. This card audits the rest, formula by formula, against the printed booklet:

- ✅ **Given** — printed somewhere in the booklet. Don't memorise it; know what it looks like and roughly where it lives.
- ❌ **Not given** — memorise it, or be able to re-derive it under time pressure.

The point is not to memorise less for its own sake. It is to spend memorisation effort where it buys marks, and understanding effort everywhere.

> [!warning] Every ❌ here means absent from the *whole booklet*
> Not absent from the Further pages — absent from all of it, checked. The distinction is the one that makes this card usable: a formula printed in the Pure half is **yours**, and marking it ❌ merely because it sits under a different heading would send you off to memorise something you already have in your hand. Three entries below exist precisely because that trap is easy to fall into — the $\tan^{-1}$ derivative, the scalar product, and the binomial series are all printed, all in the Pure half, and all serve Further rows.

### 中文锚点

| English | 中文 | note |
|---|---|---|
| formula booklet | 公式表 | handed out with every paper — you do not bring your own |
| given / printed | 给出 | on the sheet; be familiar, don't memorise |
| must memorise | 需背诵 | not on the sheet |
| critical value | 临界值 | the cut-off read from a statistical table |
| degrees of freedom | 自由度 | the parameter that selects a row of the $t$ or $\chi^2$ table |

## The shape of the booklet

| Pages | Serves | Audited in |
|---|---|---|
| Pure Mathematics · Mechanics · Probability & Statistics | 9709 — **and 9231 candidates too** | [[MF19 Reference (9709)]] |
| **Further Pure Mathematics** | 9231 Papers 1 and 2 | below |
| **Further Mechanics** | 9231 Paper 3 | below |
| **Further Probability & Statistics** | 9231 Paper 4 | below |
| Normal · $t$ · $\chi^2$ · Wilcoxon $T$ · Wilcoxon $W$ tables | 9709 Papers 5–6 and 9231 Paper 4 | below |

> [!tip] Do not hunt in the wrong half
> The Further tables deliberately **omit** anything already printed in the Pure half. $\dfrac{d}{dx}\tan^{-1}x$ and $\displaystyle\int\frac{dx}{a^2+x^2}$ are *not* missing from the booklet — they sit in the Pure differentiation and integration tables, several pages earlier. A candidate who looks only at the Further pages and finds no $\tan^{-1}$ concludes it must be memorised, and wastes the effort.

## Further Pure Mathematics — Papers 1 and 2

### Summations — §1.3, see [[Summation of Series]]

| Formula | On MF19? | Notes |
|---|---|---|
| $\sum_{r=1}^{n} r = \tfrac12 n(n+1)$ | ✅ | |
| $\sum_{r=1}^{n} r^2 = \tfrac16 n(n+1)(2n+1)$ | ✅ | |
| $\sum_{r=1}^{n} r^3 = \tfrac14 n^2(n+1)^2$ | ✅ | |
| The method of differences | ❌ | a technique, not a formula |
| Anything about convergence or sums to infinity | ❌ | §1.3 wants it read off your own $S_n$ |
| $\sum r^4$ and beyond | ❌ | not printed, not examined |

Papers still ask candidates to **derive** all three, from a difference the question supplies — worth 4, 5 and 6 marks in recent series. Being handed the destination is exactly why the marks are in the journey.

### Maclaurin's series — §2.3, see [[Maclaurin Series]]

| Formula | On MF19? | Notes |
|---|---|---|
| The general form $f(x) = f(0) + xf'(0) + \frac{x^2}{2!}f''(0) + \cdots$ | ✅ | |
| $e^x$ | ✅ | valid for all $x$ |
| $\ln(1+x)$ | ✅ | with $-1 < x \leqslant 1$ printed |
| $\sin x$, $\cos x$ | ✅ | all $x$ |
| $\tan^{-1}x$ | ✅ | with $-1 \leqslant x \leqslant 1$ |
| $\sinh x$, $\cosh x$ | ✅ | all $x$ |
| $\tanh^{-1}x$ | ✅ | with $\lvert x\rvert < 1$ |
| $\tan x$, $\sec x$, $(1+x)^n$ | ❌ | the binomial series is in the **Pure** Algebra block |

**Every printed expansion carries its interval of validity.** Quoting the series and omitting the interval is a standard lost mark, and the booklet is showing you the habit.

### Trigonometry — the $t$-substitution, §2.4

| Formula | On MF19? | Notes |
|---|---|---|
| $t = \tan\tfrac12 x \Rightarrow \sin x = \dfrac{2t}{1+t^2}$, $\cos x = \dfrac{1-t^2}{1+t^2}$ | ✅ | |
| $\tan x = \dfrac{2t}{1-t^2}$ | ❌ | one division away from the two that are given |
| $dx = \dfrac{2}{1+t^2}\,dt$ | ❌ | **memorise** — the substitution is useless without it, and it is the half the booklet withholds |

### Hyperbolic functions — §2.1, see [[Hyperbolic Functions]]

| Formula | On MF19? | Notes |
|---|---|---|
| $\cosh^2x - \sinh^2x \equiv 1$ | ✅ | |
| $\sinh 2x \equiv 2\sinh x\cosh x$ | ✅ | |
| $\cosh 2x \equiv \cosh^2x + \sinh^2x$ | ✅ | |
| $\sinh^{-1}x = \ln\!\left(x+\sqrt{x^2+1}\right)$ | ✅ | |
| $\cosh^{-1}x = \ln\!\left(x+\sqrt{x^2-1}\right)$ | ✅ | with $x \geqslant 1$ |
| $\tanh^{-1}x = \tfrac12\ln\!\left(\frac{1+x}{1-x}\right)$ | ✅ | with $\lvert x\rvert < 1$ |
| **The definitions in terms of $e^x$** | ❌ | **memorise** — everything above is built from these |
| $\operatorname{sech}$, $\operatorname{cosech}$, $\coth$ | ❌ | not printed at all |
| Osborn's rule | ❌ | a technique |

The syllabus verb is *derive and use* the logarithmic forms, so a *show that* question still wants the $u = e^y$ quadratic worked with the branch justified.

### Differentiation — §2.3

Printed as a table: $\sin^{-1}x$, $\cos^{-1}x$, $\sinh x$, $\cosh x$, $\tanh x$, $\sinh^{-1}x$, $\cosh^{-1}x$, $\tanh^{-1}x$.

| Formula | On MF19? | Notes |
|---|---|---|
| $\frac{d}{dx}\sin^{-1}x = \frac{1}{\sqrt{1-x^2}}$, $\frac{d}{dx}\cos^{-1}x = -\frac{1}{\sqrt{1-x^2}}$ | ✅ | |
| $\frac{d}{dx}\sinh x = \cosh x$, $\frac{d}{dx}\cosh x = \sinh x$, $\frac{d}{dx}\tanh x = \operatorname{sech}^2x$ | ✅ | |
| $\frac{d}{dx}\sinh^{-1}x$, $\frac{d}{dx}\cosh^{-1}x$, $\frac{d}{dx}\tanh^{-1}x$ | ✅ | all three |
| $\frac{d}{dx}\tan^{-1}x = \frac{1}{1+x^2}$ | ✅ | in the **Pure** table, not this one |
| Implicit, parametric and second derivatives | ❌ | techniques; see [[Implicit Differentiation]], [[Parametric Differentiation]] |

### Integration — §2.4, see [[Standard Integrals]]

| Formula | On MF19? | Notes |
|---|---|---|
| $\int\sec x\,dx$, $\int\operatorname{cosec}x\,dx$ | ✅ | both given in two equivalent forms |
| $\int\sinh x$, $\int\cosh x$, $\int\operatorname{sech}^2x$ | ✅ | |
| $\int\frac{dx}{\sqrt{a^2-x^2}} = \sin^{-1}\frac{x}{a}$ | ✅ | $\lvert x\rvert < a$ |
| $\int\frac{dx}{\sqrt{x^2-a^2}} = \cosh^{-1}\frac{x}{a}$ | ✅ | $x > a$ |
| $\int\frac{dx}{\sqrt{a^2+x^2}} = \sinh^{-1}\frac{x}{a}$ | ✅ | |
| $\int\frac{dx}{a^2+x^2} = \frac1a\tan^{-1}\frac{x}{a}$ | ✅ | in the **Pure** table |
| Reduction formulae, **calculus** arc length, surface of revolution | ❌ | **memorise** — all three are examined in §2.4 and none is printed. Do not be misled by *arc length of circle* $= r\theta$ in the Mensuration block: that is the constant-radius case, not $\int\sqrt{1+(dy/dx)^2}\,dx$ |

> [!warning] The §2.4 gap worth knowing about
> Arc length of a *curve* and surface area of revolution — in both Cartesian and parametric form — are examined and **nowhere on the booklet**. (The Mensuration block's $r\theta$ is a circle's arc, a different object.) Neither are reduction formulae, which are derived per-question anyway. The integration table looks generous, and then stops exactly where the harder half of §2.4 begins.

### The Further Pure rows the booklet barely touches

| Row | Printed anywhere in the booklet? |
|---|---|
| §1.1 Roots of polynomial equations | ❌ nothing — no Vieta relations, no symmetric-function identities |
| §1.2 Rational functions and graphs | ❌ nothing |
| §1.4 · §2.2 Matrices | ❌ nothing — no determinant, inverse, eigenvalue or diagonalisation formula |
| §1.5 Polar coordinates | ❌ for the polar sector area $\tfrac12\int r^2\,d\theta$ — **but** the Mensuration block prints *area of a sector of a circle* $= \tfrac12 r^2\theta$, which is the same formula frozen at constant $r$ |
| §1.6 Vectors | ✅ **scalar product** $\mathbf{a}\cdot\mathbf{b} = a_1b_1+a_2b_2+a_3b_3 = \lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\cos\theta$, printed in the Pure Vectors block · ❌ **vector product**, which appears nowhere at all |
| §1.7 Proof by induction | ❌ nothing, and nothing could be — it is a method |
| §2.5 Complex numbers | ❌ nothing — no de Moivre, no roots of unity, no $e^{i\theta}$ form |
| §2.6 Differential equations | ❌ nothing — auxiliary equation, complementary function and every particular-integral trial are yours |

**Paper 1 is 30% of the A Level and the booklet gives it three summation results plus one scalar product.** Everything else on that paper is memorise-and-derive. Budget revision accordingly: this is the reverse of the 9709 experience, where the sheet carries most of Pure 1.

> [!tip] The sector formula is worth two minutes of a lesson
> A student meeting §1.5 will see $\tfrac12 r^2\theta$ on the sheet and reasonably ask whether it is the polar formula. It is its ancestor. A circular sector has one fixed radius, so its area is $\tfrac12 r^2$ times the angle swept; a polar curve's radius changes as it sweeps, so you add up $\tfrac12 r(\theta)^2\,d\theta$ over the sweep instead. Printed formula, unprinted generalisation — and seeing that relationship is worth more than either of them alone.

## Further Mechanics — Paper 3

| Formula | On MF19? | Syllabus row |
|---|---|---|
| Equation of trajectory $y = x\tan\theta - \dfrac{gx^2}{2V^2\cos^2\theta}$ | ✅ | §3.1 |
| Elastic string/spring: $T = \dfrac{\lambda x}{l}$, $E = \dfrac{\lambda x^2}{2l}$ | ✅ | §3.4 Hooke's law |
| Uniform circular motion: acceleration towards the centre, magnitude $\omega^2 r$ or $\dfrac{v^2}{r}$ | ✅ | §3.3 |
| Centres of mass: triangular lamina $\tfrac23$ along the median; solid hemisphere $\tfrac38 r$; hemispherical shell $\tfrac12 r$; circular arc $\dfrac{r\sin\alpha}{\alpha}$; circular sector $\dfrac{2r\sin\alpha}{3\alpha}$; cone or pyramid $\tfrac34 h$ from vertex | ✅ | §3.2 |
| SUVAT | ✅ ×4 | in the **Mechanics** (9709) block — and only four of the five, as [[MF19 Reference (9709)]] records |
| §3.5 Linear motion under a variable force | ❌ | nothing — including $a = v\dfrac{dv}{dx}$, which is the whole section |
| §3.6 Momentum | ❌ | nothing — impulse, restitution, the coefficient $e$ |

> [!tip] The centres-of-mass list is the single most generous entry on the Further pages
> Six standard results printed outright. What is *not* printed is the composite-body method that uses them — $\bar{x}\sum m = \sum m\bar{x}_i$ — and that is where the marks are. Know the method cold; look the six shapes up.

## Further Probability & Statistics — Paper 4

**Start with what the shared pages already give you.** These sit in the main Probability & Statistics block and 9231 candidates get them too:

| Formula | On MF19? | Used by |
|---|---|---|
| $\bar{x}$ and standard deviation, ungrouped and grouped | ✅ | throughout |
| $E(X) = \Sigma xp$, $\operatorname{Var}(X) = \Sigma x^2p - \{E(X)\}^2$ | ✅ | [[Discrete Random Variables]] |
| Binomial, **geometric** and Poisson $p_r$, $\mu$, $\sigma^2$ | ✅ | geometric **variance is not printed** — see the 9709 card |
| $E(X) = \int x\,f(x)\,dx$, $\operatorname{Var}(X) = \int x^2 f(x)\,dx - \{E(X)\}^2$ | ✅ | §4.1, [[Continuous Random Variables]] |
| Unbiased estimators $\bar{x}$ and $s^2$, both forms | ✅ | §4.2, [[Sampling and Estimation]] |
| Central Limit Theorem, and the sample-proportion distribution | ✅ | §4.2 |

**Then the Further block and the tables:**

| Formula or table | On MF19? | Syllabus row |
|---|---|---|
| Two-sample estimate of a common variance $s^2 = \dfrac{\Sigma(x_1-\bar{x}_1)^2 + \Sigma(x_2-\bar{x}_2)^2}{n_1+n_2-2}$ | ✅ | §4.2 |
| **Critical values for the $t$-distribution** | ✅ table | §4.2 |
| **Critical values for the $\chi^2$-distribution** | ✅ table | §4.3 |
| **Wilcoxon signed-rank test — critical values of $T$** | ✅ table | §4.4 |
| **Wilcoxon rank-sum test — critical values of $W$** | ✅ table | §4.4 |
| Wilcoxon normal approximations — $P, Q \approx N\!\big(\tfrac14 n(n+1),\ \tfrac1{24}n(n+1)(2n+1)\big)$ and $R_m \approx N\!\big(\tfrac12 m(m+n+1),\ \tfrac1{12}mn(m+n+1)\big)$ | ✅ printed under each table | §4.4 — the $\pm\tfrac12$ continuity correction is **not** |
| PGFs: $G_X(t) = E(t^X)$, $E(X) = G_X'(1)$, $\operatorname{Var}(X) = G_X''(1) + G_X'(1) - \{G_X'(1)\}^2$ | ✅ | §4.5 |
| The normal distribution function $\Phi(z)$ and its critical values | ✅ table | §4.2 |
| The $\chi^2$ test statistic $\sum\frac{(O-E)^2}{E}$ | ❌ | **memorise** — the table is given, the statistic is not |
| Which Wilcoxon test to use, how to rank, $T = \min(P,Q)$ and $W = \min\!\big(R_m,\ m(m+n+1)-R_m\big)$ | ❌ | technique — the *rules* for $T$ and $W$ are printed above the tables, but the ranking procedure and the reject-when-**small** direction are yours; see [[Non-Parametric Tests]] |
| The PGF of any *named* distribution | ❌ | derive from $G_X(t) = E(t^X)$ |

> [!info] Paper 4 is the best-supported paper on the whole qualification
> Four statistical tables and a formula block, against Paper 1's three printed lines. The pattern is consistent and worth naming: **MF19 gives away numbers you could not possibly compute in an exam room, and withholds anything you could derive.** Nobody can evaluate a $t$ critical value by hand, so it is printed; everybody can write down $\sum\frac{(O-E)^2}{E}$, so it is not.
>
> That is also the reason Further Statistics is a *cheaper* paper to prepare than its reputation suggests. The arithmetic is supported; the marks are in choosing the right test, stating hypotheses properly, and reading the right row of the right table.

## Summary — what to memorise, by paper

**Paper 1 (Further Pure 1)** — everything except the three summation results and the scalar product. In particular: the relations between roots and coefficients, the method of differences, all matrix and determinant work, the polar sector area $\tfrac12\int r^2\,d\theta$ and polar curve-sketching, the **vector product** and every distance formula built on it, and the structure of an induction proof.

**Paper 2 (Further Pure 2)** — the $e^x$ definitions of $\sinh$ and $\cosh$; $\operatorname{sech}$, $\operatorname{cosech}$, $\coth$; Osborn's rule; $dx = \frac{2}{1+t^2}dt$ for the $t$-substitution; reduction formulae; arc length and surface of revolution; everything about matrices, eigenvalues and diagonalisation; de Moivre and roots of unity; the auxiliary equation and every particular-integral trial.

**Paper 3 (Further Mechanics)** — the composite-body centre-of-mass method; $a = v\frac{dv}{dx}$ and the whole of variable-force motion; impulse, momentum and restitution; and the fifth SUVAT equation $s = vt - \tfrac12 at^2$, which the booklet omits.

**Paper 4 (Further Probability & Statistics)** — the $\chi^2$ statistic; the ranking procedure for both Wilcoxon tests and the tie convention; how to build a PGF for a given distribution; the geometric variance $\frac{1-p}{p^2}$; and, as always, the *structure* of a hypothesis test, which no booklet will ever carry.

## Connections

- **Companion:** [[MF19 Reference (9709)]] — the first half of the same booklet, and the place to look for anything Pure or single-maths Mechanics/Statistics, since 9231 candidates use those pages too.
- **Audited against:** the cards named in each table above — [[Summation of Series]], [[Hyperbolic Functions]], [[Maclaurin Series]], [[Standard Integrals]], [[Continuous Random Variables]], [[Sampling and Estimation]], [[Discrete Random Variables]].
- **Other boards:** [[Edexcel IAL Reference]] and [[OxAQA 9660 Reference]] — different booklets with genuinely different generosity; 9660 prints the summation results too, Edexcel keeps them for its own FP1.
- **The philosophy:** understanding is for every formula; memorisation is for the subset a booklet will not carry. Everything above exists to identify that subset precisely, so revision time goes where it earns marks.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\operatorname{sech}^2 x$ | `\operatorname{sech}^2 x` | `\sech` is undefined in KaTeX |
| $\sinh^{-1}x$ | `\sinh^{-1}x` | the booklet uses this, not $\operatorname{arsinh}$ |
| $\chi^2$ | `\chi^2` | the test and its table |
| $G_X(t)$ | `G_X(t)` | probability generating function |
| $\nu$ | `\nu` | degrees of freedom, the row selector on the $t$ and $\chi^2$ tables |
| $\lambda$ | `\lambda` | modulus of elasticity in $T = \lambda x / l$ — not a Poisson mean here |
