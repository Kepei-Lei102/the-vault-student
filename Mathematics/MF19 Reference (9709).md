---
chinese: MF19 公式表对照 (gōngshì biǎo duìzhào)
prerequisites: []
leads_to: []
tags:
  - subject/mathematics
  - domain/exam-strategy
  - level/A-Level
  - curriculum/Cambridge-9709
  - type/reference
  - type/exam-technique
---

# MF19 Reference (9709) — what to memorise, what's free

## What this card is for

The Cambridge 9709 exam gives you **List MF19** — a printed booklet of formulas, distributed with every exam paper. You will have it in front of you for every question.

This card is the **map** of MF19 against the vault's content for Papers 1, 3, 4, 5 and 6. (Paper 2 is the AS-only route — Paper 3 is the A Level one — so it gets no separate treatment here.) The booklet's Further pages, which serve 9231, are audited in [[MF19 Reference (9231)]]. For every formula you'd learn from a vault card, this card tells you:

- ✅ **Given** — it's on MF19. Don't memorise it; just be familiar with how to use it.
- ❌ **Not given** — *if you're taking 9709, you need to memorise this* (or be able to re-derive it quickly). The exam room has no internet, no AI, no notes.

The pedagogical point: studying for an exam is not memorising every formula in every card. It's *understanding* every formula in every card, then memorising the small subset that the formula sheet doesn't carry. This document tells you which subset that is.

> [!info] Other boards have different sheets
> **MF19 is for Cambridge 9709 + 9231 only.** Edexcel, AQA, OCR, IB AA SL/HL, AP Calculus AB/BC, AP Statistics each have their own formula booklets — sometimes more generous, sometimes less. *Always check the booklet for your specific exam board.* What's free here may need memorising on a different paper, and what you have to memorise here may be free elsewhere.

### 中文锚点

**MF19** 是 Cambridge 9709 + 9231 考试用的公式表，考试时会发给你。

- ✅ **表上有的** — 不用背，但要熟练地用。
- ❌ **表上没有的** — 如果你考的是 9709，**这部分必须背下来**（或者考场上能现推出来）。

老师 / AI / 网络在考场都用不上，能用的就是这张 MF19 + 你自己的脑子。这张卡片的作用：把每个 vault 卡片里的公式与 MF19 对照，告诉你哪些必须记，哪些不用记。

---

## How to use this card

For each paper section below:

1. **Read the "given on MF19" list first.** These are formulas you should *understand*, *be familiar with*, and *practice with* — but you don't need to memorise them. The exam will hand them to you on the day.
2. **Read the "must memorise" list second.** These are the formulas, identities, and definitions that 9709 expects you to bring into the exam room. Memorise or re-derive — your choice, but they have to come from somewhere.
3. **Spend more practice time on the must-memorise list.** Rote-recall problems on those formulas are pure marks if you can summon them on demand.

> [!tip] The vault's role
> Vault cards explain the *why* and the *how* of every formula — derivations, intuitions, worked examples. The *what* (the formula itself) is on MF19 if it's there. So:
>
> - For a free-on-MF19 formula: read the card to understand *why* it's true and *when* to use it. Don't rote-memorise; you have the sheet.
> - For a not-on-MF19 formula: read the card to understand it, then commit it to memory (or commit a derivation strategy to memory). The vault card usually contains the derivation, so re-deriving is your fallback.

---

## Pure Mathematics — Papers 1 and 3

### Mensuration ✅ (all given)

MF19 gives you everything in the mensuration zone:

| Formula | MF19 | Vault card |
|---|---|---|
| Volume of sphere $\tfrac{4}{3}\pi r^3$ | ✅ | [[Surface Area and Volume (Vocab)]] |
| Surface area of sphere $4\pi r^2$ | ✅ | [[Surface Area and Volume (Vocab)]] |
| Volume of cone or pyramid $\tfrac{1}{3}\times \text{base} \times \text{height}$ | ✅ | [[Surface Area and Volume (Vocab)]] |
| Curved surface of cone $\pi r \times \text{slant}$ | ✅ | [[Surface Area and Volume (Vocab)]] |
| Arc length $r\theta$ (radians) | ✅ | [[Radians]], [[Circles Arcs and Sectors (Vocab)]] |
| Sector area $\tfrac{1}{2} r^2 \theta$ (radians) | ✅ | [[Radians]], [[Circles Arcs and Sectors (Vocab)]] |

**Must memorise — none in mensuration.** If you're taking 9709, every mensuration formula you need is on the sheet.

### Algebra

| Formula | MF19 | Vault card |
|---|---|---|
| Quadratic formula $x = \tfrac{-b \pm \sqrt{b^2-4ac}}{2a}$ | ✅ | [[Quadratic Equations]], [[Discriminant]] |
| Arithmetic series $u_n = a + (n-1)d$, $S_n$ formulas | ✅ | [[Arithmetic and Geometric Progressions]] |
| Geometric series $u_n = ar^{n-1}$, $S_n$, $S_\infty$ | ✅ | [[Arithmetic and Geometric Progressions]] |
| Binomial theorem $(a+b)^n$ for positive integer $n$ | ✅ | [[Binomial Theorem]] |
| $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ | ✅ | [[Permutations and Combinations]], [[Factorial Notation]] |
| Binomial series $(1+x)^n$ for rational $n$, $\lvert x \rvert < 1$ | ✅ | (planned for P3 §3.1: [[Binomial Series]]) |

**Must memorise (not on MF19) — for 9709 P1/P3:**

- **Discriminant cases** ($\Delta > 0$, $= 0$, $< 0$ → real distinct, repeated, complex roots). The formula $b^2 - 4ac$ is implicit in the quadratic formula; the *interpretation* isn't.
- **Laws of indices, laws of logarithms.** Not on the sheet. Memorise the three log laws: $\log(ab) = \log a + \log b$; $\log(a/b) = \log a - \log b$; $\log(a^n) = n\log a$. And change of base $\log_a x = \ln x / \ln a$.
- **Recurring-decimal trick** ($10x - x$) — that's a method, not a formula.
- **Modulus inequality strategies** (squaring trick, $|f| < g \Leftrightarrow -g < f < g$).
- **Polynomial division technique** (long division setup) — method, not formula.
- **Partial fraction decomposition** for the standard cases — methods.
- **Sum-formula derivations.** Cambridge sometimes asks you to *derive* the AP/GP sum from scratch; the formula is given but the proof technique (Gauss-pair for AP, shift-and-subtract for GP) isn't.

### Trigonometry — almost everything is given

| Formula | MF19 | Vault card |
|---|---|---|
| $\tan\theta = \sin\theta / \cos\theta$ | ✅ | [[Trigonometric Ratios]], [[Trigonometric Identities]] |
| $\sin^2\theta + \cos^2\theta \equiv 1$ | ✅ | [[Trigonometric Identities]] |
| $1 + \tan^2\theta \equiv \sec^2\theta$ | ✅ | [[Trigonometric Identities]] |
| $\cot^2\theta + 1 \equiv \csc^2\theta$ | ✅ | [[Trigonometric Identities]] |
| Compound angle $\sin(A\pm B)$, $\cos(A\pm B)$, $\tan(A\pm B)$ | ✅ | [[Trigonometric Identities]] |
| Double angle $\sin 2A$, $\cos 2A$ (all 3 forms), $\tan 2A$ | ✅ | [[Trigonometric Identities]] |
| Principal value ranges for $\sin^{-1}, \cos^{-1}, \tan^{-1}$ | ✅ | [[Trigonometric Functions]], [[Inverse Function]] |

**Must memorise (not on MF19) — for 9709 P1/P3:**

- **Exact special-angle values** for $\sin, \cos, \tan$ at $0°, 30°, 45°, 60°, 90°, 180°$. These are not on MF19 and are constantly needed. Memorise the special-angle table.
- **Sine and cosine rules** for triangles ($\dfrac{a}{\sin A} = \dfrac{b}{\sin B}$, $a^2 = b^2 + c^2 - 2bc\cos A$). Not on MF19 — must memorise. Same for area $\tfrac{1}{2}ab\sin C$.
- **R-formula / harmonic form**: $a\sin x + b\cos x = R\sin(x + \alpha)$ with $R = \sqrt{a^2+b^2}$, $\tan\alpha = b/a$. Not on the sheet — derive from compound-angle if needed.
- **General-solution form** for trigonometric equations ($\sin x = k$ has solutions $x = \alpha + 2k\pi$ and $x = \pi - \alpha + 2k\pi$, etc.). Not on the sheet, but derivable from the principal-value ranges and graph behaviour.
- **Small-angle approximations** $\sin x \approx x$, $\cos x \approx 1 - x^2/2$, $\tan x \approx x$ — useful for P3 limit-style problems; not on the sheet.

### Differentiation — table of standard derivatives is given

The full standard-derivatives table is on MF19:

| $f(x)$ | $f'(x)$ — **all on MF19** |
|---|---|
| $x^n$ | $n x^{n-1}$ |
| $\ln x$ | $1/x$ |
| $e^x$ | $e^x$ |
| $\sin x$, $\cos x$, $\tan x$ | $\cos x$, $-\sin x$, $\sec^2 x$ |
| $\sec x$, $\csc x$, $\cot x$ | $\sec x \tan x$, $-\csc x \cot x$, $-\csc^2 x$ |
| $\tan^{-1} x$ | $1/(1+x^2)$ |
| $uv$ (product rule) | $v\tfrac{du}{dx} + u\tfrac{dv}{dx}$ |
| $u/v$ (quotient rule) | $\dfrac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^2}$ |
| Parametric chain | $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ |

**Must memorise (not on MF19) — for 9709 P3:**

- **Chain rule** $\dfrac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$. Surprisingly, *not* on the sheet — the parametric form is given, but the general chain rule isn't. Memorise.
- **Implicit differentiation** as a *technique* (apply $\tfrac{d}{dx}$ to both sides, treat $y$ as a function of $x$, solve for $\tfrac{dy}{dx}$). Method, not formula.
- **First-derivative test, second-derivative test** for stationary points. Methods.
- **Inverse-function differentiation** $(f^{-1})'(y) = 1/f'(x)$. Not on MF19 — useful for deriving $(\ln x)' = 1/x$ from $(e^x)' = e^x$.
- **$\sin^{-1}$ and $\cos^{-1}$ derivatives** $\dfrac{1}{\sqrt{1-x^2}}$ and $-\dfrac{1}{\sqrt{1-x^2}}$ — these are on the *Further* MF19 page (page 6), not the main P1/P3 page. **For 9709 P3, memorise these.**

### Integration — large standard-integrals table is given

| $f(x)$ | $\int f(x)\,dx$ — **all on MF19** |
|---|---|
| $x^n$ ($n \neq -1$) | $\dfrac{x^{n+1}}{n+1}$ |
| $1/x$ | $\ln \lvert x \rvert$ |
| $e^x$ | $e^x$ |
| $\sin x$, $\cos x$, $\sec^2 x$ | $-\cos x$, $\sin x$, $\tan x$ |
| $\dfrac{1}{x^2 + a^2}$ | $\dfrac{1}{a}\tan^{-1}(x/a)$ |
| $\dfrac{1}{x^2 - a^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x-a}{x+a}\right\rvert$ ($x > a$) |
| $\dfrac{1}{a^2 - x^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{a+x}{a-x}\right\rvert$ ($\lvert x \rvert < a$) |
| Integration by parts | $\int u \tfrac{dv}{dx}\,dx = uv - \int v\tfrac{du}{dx}\,dx$ |
| $\int \dfrac{f'(x)}{f(x)}\,dx$ | $\ln \lvert f(x) \rvert$ |

**Must memorise (not on MF19) — for 9709 P3:**

- **Integration by substitution as a method** — the LIATE / 5-step recipe is technique. The formulas are derived from the chain rule (which itself you have to memorise — see above).
- **Integration of $\sin^2 x$, $\cos^2 x$, $\tan^2 x$** via the double-angle / Pythagorean identities. The base identities are on the sheet (trig section), but the integration manoeuvre is technique.
- **Trigonometric substitution** ($x = a\sin\theta$ for $\sqrt{a^2 - x^2}$, $x = a\tan\theta$ for $a^2 + x^2$). The resulting standard integrals *are* on the sheet, but knowing *which substitution to use* is method, not formula.
- **Volume of revolution** $V = \pi\int y^2\,dx$ (about $x$-axis) and $\pi\int x^2\,dy$ (about $y$-axis). Not on MF19 — memorise.
- **Trapezium rule / Simpson's rule** for numerical integration — neither is on MF19, both must be memorised.

### Vectors

| Formula | MF19 | Vault card |
|---|---|---|
| Dot product $\mathbf{a}\cdot\mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 = \lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\cos\theta$ | ✅ | [[Vectors]], [[Vector Geometry]] |

**Must memorise (not on MF19) — for 9709 P3:**

- **Magnitude of a vector** $\lvert\mathbf{a}\rvert = \sqrt{a_1^2 + a_2^2 + a_3^2}$ — not on the sheet, but follows from the dot product (given) since $\mathbf{a}\cdot\mathbf{a} = \lvert\mathbf{a}\rvert^2$. Always re-derivable.
- **Vector equation of a line** $\mathbf{r} = \mathbf{a} + t\mathbf{d}$. Not on MF19 — memorise.
- **Angle between two lines** from the dot product (rearrangement of the formula given). Method.
- **Distance / shortest-distance formulas** for point-to-line and skew-line problems — methods built from the dot product.
- **Cross product** — *not on MF19, and not in the 9709 P3 syllabus.* Don't worry about it for 9709 (it's an A-Level Further / IB / AP topic).

---

## Mechanics — Paper 4

### Uniformly accelerated motion (SUVAT) — only 4 of 5 are given

| Formula | MF19 | Vault card |
|---|---|---|
| $v = u + at$ | ✅ | [[SUVAT]] |
| $s = \tfrac{1}{2}(u + v)t$ | ✅ | [[SUVAT]] |
| $s = ut + \tfrac{1}{2}at^2$ | ✅ | [[SUVAT]] |
| $v^2 = u^2 + 2as$ | ✅ | [[SUVAT]] |

**Must memorise (not on MF19) — for 9709 P4 SUVAT:**

- **The fifth SUVAT formula $s = vt - \tfrac{1}{2}at^2$.** *Yes, really — the symmetric one (final-velocity version) is the only SUVAT not on MF19.* Memorise it, or derive it on the spot by substituting $u = v - at$ into the third formula. The five-formula table in [[SUVAT]] gives the full set.

### Newton's Laws, Forces, Energy, Momentum — *nothing* on the sheet

This is the big surprise of MF19 for Paper 4 students. Apart from SUVAT, **the entire Mechanics syllabus has no formulas given on the sheet.** Everything below must be memorised.

**Must memorise (not on MF19) — for 9709 P4:**

| Formula | Vault card | What to bring to the exam |
|---|---|---|
| $F = ma$ (Newton's second law) | [[Newton's Laws of Motion]] | The whole P4 hangs on this. |
| $W = mg$ (weight as force) | [[Newton's Laws of Motion]], [[Force (Vocab)]] | Use $g = 10$ m/s² unless told otherwise. |
| $\mathbf{p} = m\mathbf{v}$ (momentum definition) | [[Linear Momentum]] | The conservation law is the whole point. |
| $m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$ (1D conservation of momentum) | [[Linear Momentum]] | Apply to every collision and coalescence. |
| Impulse $J = Ft = \Delta p$ | [[Linear Momentum]] | Connects force and momentum change. |
| $\Sigma F = 0$, $\Sigma \tau = 0$ (equilibrium) | [[Forces and Equilibrium]] | Translational + rotational. |
| $W = Fs\cos\theta$ (work done) | [[Work, Energy and Power]] | The $\cos\theta$ for non-aligned force/displacement. |
| $\text{KE} = \tfrac{1}{2}mv^2$ | [[Work, Energy and Power]] | Memorise by reflex. |
| $\text{PE} = mgh$ (gravitational) | [[Work, Energy and Power]] | Reference height matters. |
| $W_{\text{net}} = \Delta\text{KE}$ (work-energy theorem) | [[Work, Energy and Power]] | Often the cleanest path. |
| $P = Fv$ (power, instantaneous) | [[Work, Energy and Power]] | Constant-power problems live here. |
| $P = W/t$ (average power) | [[Work, Energy and Power]] | Used less often than $P=Fv$. |
| $F = \mu N$ (friction at the limit) | [[Friction (Vocab)]], [[Forces and Equilibrium]] | $\mu_s$ vs $\mu_k$ distinction. |
| Resolution of forces $F_x = F\cos\theta$, $F_y = F\sin\theta$ | [[Forces and Equilibrium]] | The trig comes from your trig knowledge. |

> [!tip] Mechanics is a memorise-heavy paper for 9709
> If you compare 9709 Paper 4 (Mechanics) to Paper 3 (Pure 3), Pure 3 has a vast standard-derivatives + standard-integrals + trig-identities table on MF19 and Mechanics has *just SUVAT*. **The mechanics formulas have to live in your head.** [[Choosing Effective Equations]] is the navigation skill that helps you pick the right one once you've memorised the whole toolkit; this card tells you what the toolkit is.

---

## Probability & Statistics 1 — Paper 5

### Summary statistics (P5 §5.1)

| Formula | MF19 | Vault card |
|---|---|---|
| Mean (ungrouped) $\bar{x} = \dfrac{\Sigma x}{n}$ | ✅ | [[Averages and Spread]] |
| Mean (grouped) $\bar{x} = \dfrac{\Sigma xf}{\Sigma f}$ | ✅ | [[Averages and Spread]] |
| Standard deviation (ungrouped) $\sigma = \sqrt{\dfrac{\Sigma(x-\bar{x})^2}{n}} = \sqrt{\dfrac{\Sigma x^2}{n} - \bar{x}^2}$ | ✅ | [[Averages and Spread]] |
| Standard deviation (grouped) — analogous formula with $f$ | ✅ | [[Averages and Spread]] |

**Must memorise (not on MF19) — for 9709 P5 summary statistics:**

- **Median + IQR computation** (the rank-based statistics) — methods, not formulas.
- **Histogram, box-plot, cumulative-frequency reading skills** — graphical, not formulaic. See [[Histograms]], [[Box Plots]], [[Cumulative Frequency]].

### Discrete Random Variables (P5 §5.4) — see [[Discrete Random Variables]]

| Formula | MF19 | Vault card |
|---|---|---|
| $E(X) = \Sigma xp$ | ✅ | [[Discrete Random Variables]] |
| $\text{Var}(X) = \Sigma x^2 p - \{E(X)\}^2$ | ✅ | [[Discrete Random Variables]] |
| **Binomial** $p_r = \binom{n}{r}p^r(1-p)^{n-r}$, $\mu = np$, $\sigma^2 = np(1-p)$ | ✅ all three | [[Discrete Random Variables]] |
| **Geometric** $p_r = p(1-p)^{r-1}$, $\mu = 1/p$ | ✅ both | [[Discrete Random Variables]] |

**Must memorise (not on MF19) — for 9709 P5 §5.4:**

- **Geometric variance $\sigma^2 = (1-p)/p^2$.** *The mean is given but the variance isn't.* The catch on the sheet for this section.
- **Linearity properties** $E(aX+b) = aE(X)+b$, $E(X+Y) = E(X) + E(Y)$, $\text{Var}(aX+b) = a^2\,\text{Var}(X)$. Not on MF19 — but used implicitly in many problems.
- **The four conditions for the binomial** (fixed $n$, two outcomes, constant $p$, independence). Not formulas — a checklist.
- **The defining form $\text{Var}(X) = E((X-\mu)^2)$.** The *computational* form is given, but the conceptual definition is what makes it interpretable.

### Normal Distribution (P5 §5.5) — see [[Normal Distribution]]

| Item | MF19 | Notes |
|---|---|---|
| $\Phi(z)$ table for the standard normal CDF | ✅ (full table on page 10 of MF19) | The table — your main exam tool. |
| Critical values for $\Phi$ at standard $p$-levels | ✅ (page 10) | For inverse-CDF / "find $z$ such that $P(Z \le z) = p$" questions. |
| $\Phi(-z) = 1 - \Phi(z)$ symmetry | ✅ (stated on page 10) | The symmetry rule for negative-$z$ lookups. |

**Must memorise (not on MF19) — for 9709 P5 §5.5:**

- **Standardisation $Z = \dfrac{X - \mu}{\sigma}$.** *Not on the sheet.* The single most-used formula in §5.5 — without it you can't use the $\Phi$ table at all.
- **The PDF $\phi(z) = \dfrac{1}{\sqrt{2\pi}}\,e^{-z^2/2}$** is *not* on MF19 *and* not on the 9709 syllabus. You don't need it for the exam — only the table.
- **Normal approximation to binomial — conditions** ($np \ge 5$ AND $n(1-p) \ge 5$) and the **continuity correction** ($\pm 0.5$ when going from discrete to continuous). Both *not on MF19* — memorise. Note that the *approximation formula itself*, $B(n,p) \approx N(np, np(1-p))$, is **re-assemblable from the sheet**: the binomial $\mu = np$ and $\sigma^2 = np(1-p)$ are both given in MF19's *Discrete random variables* section, and the move "build a normal with the same mean and variance" is the small bit from memory. So the formula is *partially there, just needs assembly* — it's the *conditions* and *continuity correction* that are entirely from your head.
- **The 68 / 95 / 99.7 rule** (proportions within $1\sigma, 2\sigma, 3\sigma$). Not on MF19 — useful as a sanity check.

### Probability laws (P5 §5.3 — background, not P5 specifically)

| Formula | MF19 | Vault card |
|---|---|---|
| $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | ❌ — not on MF19 | [[Combined Probability]] |
| $P(A \cap B) = P(A) \cdot P(B)$ for independent events | ❌ — not on MF19 | [[Combined Probability]] |
| $P(A \mid B) = P(A \cap B) / P(B)$ (conditional) | ❌ — not on MF19 | [[Conditional Probability]] |
| Tree-diagram methodology | ❌ — graphical | [[Combined Probability]] |
| Bayes' theorem $P(A\mid B) = P(B \mid A) P(A) / P(B)$ | ❌ — not on MF19 | [[Conditional Probability]] |

**The whole probability-laws core (§5.3) is not on MF19.** You're expected to bring all of it into the exam. Memorise.

### Permutations and combinations (P5 §5.2)

| Formula | MF19 | Vault card |
|---|---|---|
| $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ | ✅ (in algebra section) | [[Permutations and Combinations]] |

**Must memorise (not on MF19) — for 9709 P5 §5.2:**

- **Permutations $^nP_r = \dfrac{n!}{(n-r)!}$.** Not on MF19 — memorise.
- **Distinguishing permutations from combinations** ("does order matter?") — method, not formula.
- **Circular permutations** $(n-1)!$, **multinomial coefficients** $\dfrac{n!}{n_1!\,n_2!\,\cdots\,n_k!}$. Not on MF19.

---

## Probability & Statistics 2 — Paper 6

> P6 is complete in the vault: [[Poisson Distribution]], [[Linear Combinations of Random Variables]], [[Continuous Random Variables]], [[Sampling and Estimation]], and [[Hypothesis Tests]] — with it, every 9709 paper has full card coverage. The formulas below appear in MF19's *Sampling and testing* section.

### Sampling and estimation (P6 §6.4)

| Formula | MF19 | Notes |
|---|---|---|
| Sample mean $\bar{x} = \dfrac{\Sigma x}{n}$ | ✅ | Same formula as P5 — also given in MF19's general Summary Statistics block. |
| **Unbiased sample variance** $s^2 = \dfrac{\Sigma(x - \bar{x})^2}{n-1} = \dfrac{1}{n-1}\!\left(\Sigma x^2 - \dfrac{(\Sigma x)^2}{n}\right)$ | ✅ | *Crucial detail: the denominator is $n-1$, not $n$.* This is the **unbiased estimator** of the population variance from a sample. The version with denominator $n$ that appears in P5 is the *sample* variance (descriptive); the version here is the *unbiased estimator* (inferential). When the question asks for "an unbiased estimate of the population variance", use this formula with $n-1$. |
| **CLT formula for sample means** $\bar{X} \sim N\!\left(\mu, \dfrac{\sigma^2}{n}\right)$ | ✅ | The **sampling distribution** of the sample mean. *Exactly* normal if the underlying population is normal; *approximately* normal for large $n$ regardless of the population (this is the CLT — see [[Normal Distribution]] for the formal statement). The $\sigma^2/n$ is what shrinks as you collect more data: the **standard error** $\sigma/\sqrt{n}$ goes to 0 like $1/\sqrt{n}$. |
| **Sample proportion distribution** $\hat{p} \sim N\!\left(p, \dfrac{p(1-p)}{n}\right)$ | ✅ | Approximate sampling distribution of a sample proportion $\hat{p}$ from a Bernoulli/binomial population with true proportion $p$. Direct application of the CLT to Bernoulli variables (whose variance is $p(1-p)$). Used in proportion hypothesis tests and proportion confidence intervals. |

**Must memorise (not on MF19) — for 9709 P6 §6.4 / §6.5:**

- **Standard error** $\dfrac{\sigma}{\sqrt{n}}$ — the standard deviation of the sampling distribution; $\sqrt{}$ of the variance given on the sheet.
- **Confidence-interval construction.** $\bar{x} \pm z^* \cdot \dfrac{\sigma}{\sqrt{n}}$ (or $\bar{x} \pm z^* \cdot \dfrac{s}{\sqrt{n}}$ when population $\sigma$ is unknown and $n$ is large). The critical values $z^*$ are on MF19 (page 10), but the confidence-interval formula itself isn't.
- **Hypothesis-test structure.** $H_0$, $H_1$, test statistic, p-value or critical region, decision. The test-statistic formula varies by test — typically $z = (\bar{x} - \mu_0) / (\sigma/\sqrt{n})$ for a one-sample mean test — and is *not* on MF19.
- **One-tail vs two-tail thresholds**, $\alpha$ levels (1%, 5%, 10%) — conventions, not formulas.
- **Type I and Type II error definitions** — vocabulary, not formulas.

### Hypothesis testing (P6 §6.5)

MF19 does not give you any hypothesis-test formulas directly. The **z-test** for a single mean uses
$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$$
which is just the standardisation of $\bar{X}$ with mean $\mu_0$ (under $H_0$) and standard error $\sigma/\sqrt{n}$. Build it from the standardisation rule (memorised from P5 §5.5) and the sampling distribution given in MF19. **The z-test formula itself is not on MF19; the building blocks are.**

The **t-distribution critical values** for small-sample tests are on **MF19 page 11**. (9709 doesn't use the $t$-test directly, but Cambridge International Further Math 9231 does, and the table is in the booklet for that reason.)

### Other distributions on MF19 (P6 §6.1)

| Formula | MF19 | Notes |
|---|---|---|
| **Poisson distribution** $X \sim \text{Po}(\lambda)$: $p_r = e^{-\lambda} \dfrac{\lambda^r}{r!}$, $\mu = \lambda$, $\sigma^2 = \lambda$ | ✅ all three | The third named discrete distribution. Mean equals variance — diagnostic of Poisson. |
| **Continuous random variables**: $E(X) = \int x f(x)\,dx$, $\text{Var}(X) = \int x^2 f(x)\,dx - \{E(X)\}^2$ | ✅ both | Continuous analogues of the P5 §5.4 discrete formulas; integrals replace sums. The computational form for variance carries over. |

**Must memorise (not on MF19) — for 9709 P6 §6.1 / §6.3:**

- **Conditions for Poisson approximation to binomial** (large $n$, small $p$, fixed $np = \lambda$). The approximation itself ($B(n,p) \approx \text{Po}(np)$) is not on MF19.
- **PDF normalisation** $\int_{-\infty}^{\infty} f(x)\,dx = 1$ — the constraint that picks out a valid PDF.
- **CDF definition** $F(x) = \int_{-\infty}^x f(t)\,dt$ — the definite-integral form of "probability up to $x$".
- **Median, mode of a continuous distribution** — definitions, not formulas.

---

## The Further pages — handed over

MF19 is **one booklet serving two qualifications**: Cambridge 9709 *and* 9231. Its later pages carry Further Pure, Further Mechanics and Further Probability & Statistics sections, plus the $t$, $\chi^2$ and two Wilcoxon tables, and this card does not audit them.

**[[MF19 Reference (9231)]] does**, formula by formula, and a 9231 candidate should read both cards — because the booklet has no partition in it, and the Pure pages audited *here* serve Further rows too. The scalar product, the $\tan^{-1}$ derivative and the binomial series are all in this half and all examined over there.

A 9709 candidate needs nothing from those pages. Turning to them is allowed and simply finds material that is not on the 9709 syllabus.

## Summary — your memorise lists, by paper

> [!tip] Print this section and paste it on the exam-revision wall
> These are the formulas / facts that 9709 expects in your head when you walk into the exam room. Everything else is on MF19; *do not over-memorise*.

### Paper 1 / Paper 3 (Pure)

- **Discriminant interpretation** ($\Delta$ sign → root types)
- **Three log laws + change of base**
- **Sine rule, cosine rule, area $= \tfrac{1}{2}ab\sin C$**
- **Special-angle exact values** (all of $0°, 30°, 45°, 60°, 90°, 180°$)
- **R-formula** $a\sin\theta + b\cos\theta = R\sin(\theta + \alpha)$
- **General-solution forms** for $\sin x = k$, $\cos x = k$, $\tan x = k$
- **Chain rule** (the parametric form is given but not the general one)
- **$\sin^{-1}, \cos^{-1}$ derivatives** ($1/\sqrt{1-x^2}$, $-1/\sqrt{1-x^2}$)
- **Volume of revolution** ($\pi\int y^2\,dx$, $\pi\int x^2\,dy$)
- **Trapezium rule / Simpson's rule** for P3 §3.6 numerical methods
- **Magnitude of a vector** $\lvert\mathbf{a}\rvert = \sqrt{a_1^2 + a_2^2 + a_3^2}$ (or re-derive from the dot product)
- **Vector equation of a line** $\mathbf{r} = \mathbf{a} + t\mathbf{d}$

### Paper 4 (Mechanics)

- **Fifth SUVAT formula $s = vt - \tfrac{1}{2}at^2$** (the only one not on MF19)
- **$F = ma$, $W = mg$**
- **$\mathbf{p} = m\mathbf{v}$** + 1D conservation of momentum
- **Impulse $J = Ft = \Delta p$**
- **$\Sigma F = 0$, $\Sigma \tau = 0$** for equilibrium
- **$W = Fs\cos\theta$, $\text{KE} = \tfrac{1}{2}mv^2$, $\text{PE} = mgh$**
- **Work-energy theorem $W_{\text{net}} = \Delta\text{KE}$**
- **$P = Fv$, $P = W/t$**
- **$F = \mu N$ at limit**
- **Resolution of forces** $F_x = F\cos\theta$, $F_y = F\sin\theta$

(Mechanics is the most memorise-heavy 9709 paper. See [[Choosing Effective Equations]] for how to navigate the toolkit once you've memorised it.)

### Paper 5 (Probability & Statistics 1)

- **Geometric variance $\sigma^2 = (1-p)/p^2$** (the catch — geometric mean is given but variance isn't)
- **Linearity properties** $E(aX+b) = aE(X)+b$, $\text{Var}(aX+b) = a^2\,\text{Var}(X)$
- **The four binomial conditions** (a checklist, not a formula)
- **Standardisation $Z = (X-\mu)/\sigma$** (the bridge from $X$ to the $\Phi$ table)
- **Normal approximation to binomial + continuity correction** ($\pm 0.5$)
- **The probability laws** $P(A\cup B), P(A\cap B), P(A \mid B)$, Bayes
- **Permutations $^nP_r$** (combinations are derivable from MF19's $\binom{n}{r}$)
- **Circular permutations $(n-1)!$, multinomial coefficients**

### Paper 6 (Probability & Statistics 2)

- **Standard error** $\sigma / \sqrt{n}$ — square root of the variance MF19 gives for the sampling distribution
- **z-test formula** $z = (\bar{x} - \mu_0) / (\sigma / \sqrt{n})$ — the building blocks are on MF19, the assembly isn't
- **Confidence-interval form** $\bar{x} \pm z^* \cdot \sigma/\sqrt{n}$ — critical values $z^*$ are on MF19, the formula isn't
- **Conditions for Poisson approximation to binomial** (large $n$, small $p$, $np = \lambda$)
- **PDF normalisation** $\int_{-\infty}^{\infty} f(x)\,dx = 1$
- **CDF definition** $F(x) = \int_{-\infty}^x f(t)\,dt$
- **Median, mode of continuous distributions** (definitions)
- **Type I, Type II error definitions** (vocabulary)
- **One-tail vs two-tail tests, $\alpha$ levels**

(P6 coverage complete: [[Poisson Distribution]], [[Linear Combinations of Random Variables]], [[Continuous Random Variables]], [[Sampling and Estimation]], [[Hypothesis Tests]].)

---

## Connections

- **The active card this references most:** [[Discrete Random Variables]] (P5 §5.4) — has its own per-card MF19 callout pointing back here.
- **Related across the vault:** every card with a "LaTeX Reference" table touches MF19 in some way. This card is the index that maps card-formulas to MF19 pages.
- **Future companion cards (when other boards' formula sheets are imported):** IB AA SL/HL formula booklet reference, AP Calculus AB/BC formula reference, AP Statistics formula reference, A-Level Edexcel formula booklet reference. Each will follow the same template — given/not-given audit per paper, with the "if you're taking [board], you need to memorise" framing.
- **Methodology connection:** [[Forward Reading and Problem Discovery]] — *knowing what's on the formula sheet is itself a forward-reading skill*. The first thing the exam hands you is the sheet; treating it as a passive crutch wastes the moves it gives you.

---

## A note on philosophy

This card exists because — as a teacher — I use AI and the internet constantly, and I rarely memorise formulas. Students don't have those tools in the exam room. They have MF19 and their own brain.

So the question this card answers is: **"What's the smallest set of formulas you have to commit to memory to pass 9709 cleanly?"** Not "what should you understand" — that's every formula in every vault card, and *understanding* is non-negotiable. But *memorisation* is a finite, expensive operation, and the formula sheet means you don't have to spend that operation on items that are free.

Use the vault to build *understanding* (every card; every derivation). Use this card to direct your *memorisation effort* (the focused subset above). And use MF19 in the exam itself as the index you flip to under pressure.
