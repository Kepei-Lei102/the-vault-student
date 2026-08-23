---
chinese: 假设检验 (jiǎshè jiǎnyàn)
prerequisites:
  - "[[Sampling and Estimation]]"
  - "[[Normal Distribution]]"
  - "[[Discrete Random Variables]]"
  - "[[Poisson Distribution]]"
  - "[[Continuous Random Variables]]"
  - "[[Inventing Variance]]"
leads_to:
  - "[[t-Tests]]"
  - "[[Chi-Squared Tests]]"
  - "[[Non-Parametric Tests]]"
  - "[[The Lady Tasting Tea]]"
tags:
  - subject/mathematics
  - domain/statistics
  - domain/probability
  - level/A-Level
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/AP-Statistics
  - syllabus/9709-6-5
  - type/deep
  - type/methodology
  - misconception/accepting-h0-proves-it
  - misconception/p-value-is-prob-h0-true
  - misconception/significant-means-important
  - misconception/tail-chosen-after-data
---
# Hypothesis Tests 假设检验

> *Cambridge, the 1920s. At an afternoon tea, a lady — Dr Muriel Bristol, an algae biologist — declares she can taste whether the milk was poured before or after the tea. The bearded man beside her doesn't scoff; he starts designing. Eight cups, four each way, randomised order: how many must she get right before "she's just guessing" becomes unbelievable? The man is R. A. Fisher, the same Fisher who named variance — and the little tea experiment in his 1935 book became the template for every drug trial, quality check, and A/B test since. The idea is a courtroom: the boring explanation is* presumed innocent, *and evidence convicts only when it would be absurdly unlikely under that presumption. This card is the ritual, its two ways of being wrong — convicting the innocent and acquitting the guilty — and the see-saw that forever trades one against the other. (She got them all right.)*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| hypothesis test | 假设检验 | a courtroom procedure for deciding between two claims about a population |
| null hypothesis $H_0$ | 原假设（零假设） | the presumed-innocent default: *nothing has changed, no effect, pure chance* |
| alternative hypothesis $H_1$ | 备择假设 | the claim seeking a conviction: *something has changed* |
| significance level $\alpha$ | 显著性水平 | how unlikely the evidence must be (under $H_0$) before we convict — the standard of proof |
| test statistic | 检验统计量 | the number computed from the data that the verdict turns on |
| rejection / critical region | 拒绝域 | the set of outcomes extreme enough to convict |
| acceptance region | 接受域 | everything else — the verdict stays "not guilty" |
| one-tailed / two-tailed | 单尾 / 双尾 | is the suspicion directional ("increased") or open ("changed")? |
| Type I error | 第一类错误 | convicting the innocent: rejecting a true $H_0$ |
| Type II error | 第二类错误 | acquitting the guilty: failing to reject a false $H_0$ |

## The logic — a courtroom for claims

Every hypothesis test is the same trial, and naming the roles correctly is half the marks:

- **$H_0$, the null hypothesis, is the defendant** — and it is *presumed true*. It is always the boring explanation: the coin is fair, the machine still fills 500 g, the new drug does nothing, the lady is guessing. In symbols it always pins the parameter to a specific value: $H_0: p = 0.5$, $\;H_0: \mu = 500$, $\;H_0: \lambda = 3$.
- **$H_1$, the alternative, is the prosecution's claim** — what the question suspects: $p > 0.5$, $\mu \neq 500$, $\lambda < 3$. Its wording sets the tails (next section).
- **The evidence is your sample**, and the standard of proof is the **significance level** $\alpha$: we convict only if evidence *this extreme* would occur with probability below $\alpha$ **assuming the defendant is innocent**. At $\alpha = 5\%$, we demand a coincidence rarer than one-in-twenty before rejecting the presumption.

Two asymmetries follow, and both are exam marks. First, the burden of proof is entirely on $H_1$: weak evidence doesn't *prove* $H_0$ any more than an acquittal proves innocence — the verdict is "not guilty", never "innocent", so we say *"insufficient evidence to reject $H_0$"*, never "$H_0$ is true". Second, the conclusion must be delivered **in context and without over-claiming**: *"there is significant evidence, at the 5% level, that the machine under-fills"* — not "this proves the machine under-fills."

## The ritual — five steps, every time

1. **State** $H_0$ and $H_1$ in symbols, defining the parameter in words ("$\mu$ = population mean fill in grams").
2. **Read the tails off $H_1$'s wording.** "Increased" / "decreased" / "more effective" → **one-tailed**, all of $\alpha$ in that one tail. "Changed" / "different" / "affected" → **two-tailed**, $\alpha$ split half-and-half ($2.5\%$ in each tail at the 5% level). The choice comes from the *question's claim*, decided before the data is examined — never from peeking at which side the sample fell.
3. **Compute** the test statistic — a tail probability by direct evaluation (discrete), or a $z$-value (means).
4. **Compare** against $\alpha$ (or the critical region).
5. **Conclude in context**, with the careful non-assertive wording above.

## Discrete tests — binomial and Poisson, by direct evaluation

The cleanest tests come first historically and on the paper: a **single observation** from a binomial or Poisson population, judged by directly computing how extreme it is.

*The coin on trial.* A coin is suspected of favouring heads. It is tossed 15 times: **12 heads**. Test at the 5% level. $H_0: p = 0.5$, $H_1: p > 0.5$ (one tail — the suspicion is directional). Under $H_0$, $X \sim B(15, 0.5)$.

*Tool: the binomial pmf from [[Discrete Random Variables]],* $P(X = k) = \dbinom{n}{k}p^k(1-p)^{n-k}$ — and with $p = 1 - p = 0.5$ every term collapses to $\dbinom{15}{k}(0.5)^{15}$. The evidence's extremeness is the probability of *what happened or anything more extreme*, each term priced by that formula:

$$P(X \geqslant 12) = \sum_{k=12}^{15}\binom{15}{k}(0.5)^{15} = \frac{455 + 105 + 15 + 1}{32768} \approx 0.0176 = 1.76\%.$$

$1.76\% < 5\%$: reject $H_0$ — significant evidence, at the 5% level, that the coin favours heads. Note the shape of the computation: **never** $P(X = 12)$ alone (any exact outcome is individually rare; that proves nothing) — always the *tail*, the outcome **or worse**.

![[hypothesis-binomial-region.svg|680]]

**The actual significance level.** Discreteness means you cannot have exactly 5% even if you want it. The **critical region** is the largest tail with probability $\leqslant \alpha$ — here $\{12, 13, 14, 15\}$, since $P(X \geqslant 12) = 1.76\%$ but $P(X \geqslant 11) = 5.92\% > 5\%$. The region's true probability, $1.76\%$, is called the **actual significance level**: the test's real convict-the-innocent rate, and a standard exam ask.

**Poisson, same recipe.** A junction averages 3 accidents per month; after a redesign, one month shows **0 accidents**. $H_0: \lambda = 3$, $H_1: \lambda < 3$. *Tool: the Poisson pmf from [[Poisson Distribution]],* $P(X = k) = \dfrac{e^{-\lambda}\lambda^k}{k!}$:

$$P(X \leqslant 0) = P(X = 0) = \frac{e^{-3}\,3^0}{0!} = e^{-3} \approx 0.0498 < 5\%$$

— just significant: evidence the redesign reduced the rate ([[Poisson Distribution]]'s model, now standing trial). And when the numbers grow large — $B(200, 0.5)$, $\text{Po}(40)$ — the syllabus permits running the same test through the **normal approximation** (with the continuity correction from [[Normal Distribution]]), the approximation machinery finally earning its exam keep.

## Testing a mean — the $z$-test

For a population mean, the machinery is [[Sampling and Estimation]] verbatim: under $H_0: \mu = \mu_0$, the sample mean is $\bar{X} \approx N(\mu_0, \sigma^2/n)$ (exactly, if the population is normal with known $\sigma$; approximately by the CLT for a large sample, with $s$ standing in). So standardise the evidence:

$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$$

and compare with the critical value: one-tailed 5% → $1.645$; two-tailed 5% → $\pm 1.96$; one-tailed 1% → $2.326$; two-tailed 1% → $\pm 2.576$ (all from [[Normal Distribution]]'s percentage points, and worth knowing cold).

*Worked.* A machine fills bags with $\mu = 500$ g, $\sigma = 12$ g. After maintenance, a sample of 36 bags has $\bar{x} = 495.5$ g. Has the mean **changed**? Test at 5%.

*Tool: the ritual.* $H_0: \mu = 500$, $H_1: \mu \neq 500$ — "changed" → **two-tailed**, $2.5\%$ each side, critical values $\pm 1.96$.

*Tool: standardise with the standard error.*
$$z = \frac{495.5 - 500}{12/\sqrt{36}} = \frac{-4.5}{2} = -2.25.$$

$|-2.25| > 1.96$: reject $H_0$ — significant evidence at the 5% level that the mean fill has changed. (One-tailed at 5% the cut would be $-1.645$; the two-tailed test is *harder to convict* on the same side — the price of an undirected suspicion.)

## The two ways to be wrong — and the see-saw

A verdict procedure can fail in exactly two ways, and the courtroom names write themselves:

| | $H_0$ actually true | $H_0$ actually false |
|---|---|---|
| **reject $H_0$** | **Type I error** — convicted the innocent | correct ✓ |
| **do not reject** | correct ✓ | **Type II error** — the guilty walked free |

- **$P(\text{Type I})$** = the probability the evidence lands in the rejection region *when $H_0$ is true* — which is the significance level itself: $\alpha$ for continuous tests, the **actual** significance level for discrete ones (the $1.76\%$ above). You chose this risk when you chose $\alpha$.
- **$P(\text{Type II})$**, written $\beta$, needs more information: a *specific* true alternative. "The coin actually has $p = 0.8$"; "the true mean is actually $497$ g". Then $\beta = P(\text{evidence lands in the acceptance region} \mid \text{that truth})$ — the guilty defendant producing evidence too mild to convict.

![[hypothesis-type1-type2.svg|690]]

The two risks **trade against each other**: demand stronger proof (smaller $\alpha$, cut line pushed outward) and you convict fewer innocents but acquit more guilty ($\beta$ grows). With a fixed sample there is no free lunch — the only way to shrink *both* errors is **more evidence**: bigger $n$ narrows both bells until they barely overlap. Watch the see-saw, then watch $n$ beat it:

![[hypothesis-tradeoff.mp4]]

*Worked (the standard Type II ask).* For the filling machine above (two-tailed, $n = 36$, cut values $500 \pm 1.96 \times 2 = 496.08$ and $503.92$): suppose the true mean is actually $497$ g. Then

$$\beta = P(496.08 < \bar{X} < 503.92 \mid \mu = 497) = P\!\left(\frac{496.08 - 497}{2} < Z < \frac{503.92 - 497}{2}\right) = P(-0.46 < Z < 3.46) \approx 0.677.$$

A two-in-three chance the drifted machine escapes detection — the sample is simply too small to see a 3-gram drift reliably. (That number is why real quality control *designs* $n$ before testing; see Beyond.)

## Common Misconceptions (Teaching Notes)

### 1. "We accept $H_0$ — so $H_0$ is true"

An acquittal is not a certificate of innocence; it means the evidence didn't clear the bar. **Fix:** ban "accept" from conclusions entirely — write *"insufficient evidence to reject $H_0$"* and keep the burden of proof where it belongs. (This is also why $H_0$ must carry the *specific* value: you cannot presume a vague defendant.)

### 2. "The p-value is the probability $H_0$ is true"

The tail probability is $P(\text{evidence this extreme} \mid H_0 \text{ true})$ — the direction of the conditional matters totally. $P(\text{evidence} \mid \text{innocent})$ is not $P(\text{innocent} \mid \text{evidence})$: the first is this card; the second would need [[Conditional Probability]]'s Bayes machinery and a prior. **Fix:** read every tail probability aloud with its "if $H_0$ were true…" preamble attached.

### 3. "Significant means important"

"Significant at 5%" is a statement about *detectability*, not *size*. With $n$ huge, a 0.1-gram drift becomes "highly significant" while mattering to nobody; with $n$ tiny, a huge effect can fail to clear the bar (the $\beta = 0.677$ above). **Fix:** report the effect itself alongside the verdict — the exam's "interpret in context" instruction is this point in disguise.

### 4. "Twelve heads came up, so I'll test $p > 0.5$"

Choosing the tail *after* seeing which way the data leans is testifying after reading the verdict — it silently doubles the convict-the-innocent rate. **Fix:** the tails come from the *question's suspicion* ("the dealer claims the die favours sixes" → one-tailed, stated before the throw). If the suspicion is genuinely undirected, it's two-tailed, and conviction is rightly harder.

### 5. "Compare $P(X = 12)$ with 5%"

Any exact outcome is rare — $P(X = 12)$ being small proves nothing. The evidence's extremeness is the whole tail: *this outcome or worse for $H_0$*. **Fix:** the phrase "or more extreme" belongs in every discrete test's working line.

## "We accept" — where causality actually comes from

The vault's problem-solving philosophy calls a hunter *someone who can constantly trace causality* ([[Forward Reading and Problem Discovery]]). This card is where the hunter learns the trade's honest secret: **in the probabilistic world, causality is never traced to the end — it is accepted.** No experiment ever shows you the arrow from cause to effect. What it shows you is evidence so unlikely under "there is no arrow" that continuing to believe in coincidence becomes the crazier position. "Smoking causes cancer," "this drug works," "the redesigned junction is safer" — every causal sentence civilisation acts on is a hypothesis that survived tests hard enough that we agreed to stop doubting *for now*. Rejection at 5% is not a discovery of causality; it is a **decision to treat a pattern as real enough to move on** — which is exactly what the careful courtroom wording has been protecting all along.

And the 5% itself is a comfort, not a law of nature. Real decisions do not always grant it: a doctor reads an ambiguous scan and must treat or not treat *today*; an engineer sees a worrying-but-not-yet-significant vibration and must ground the fleet or fly; a public-health office watches an outbreak curve that has cleared no textbook threshold and must act or wait. **Waiting for 95% is also a choice, and it has its own price** — that is precisely what $\beta$ measures: the guilty walking free while you demand more proof. When the two errors' costs are wildly unequal, the rational act may be to convict at 80%, or 60%. The see-saw's real lesson was never "find certainty" — it was **choose which mistake you can afford**. Both errors are real. Both sides of every threshold are real. Statistics does not remove the leap; it measures the cliff — and then we still move.

## Exam Notes

### Cambridge 9709 — P6 §6.5

- **The LO list:** the vocabulary in full (null/alternative hypothesis, significance level, rejection/critical region, acceptance region, test statistic, one- vs two-tailed — outcomes *interpreted in context* is stated in the syllabus itself); tests on a **single observation** from a binomial or Poisson population by **direct evaluation** *or by the normal approximation where appropriate* (continuity correction!); tests on a **mean** (normal population with known variance, or large sample); **Type I and Type II** understood *and their probabilities calculated* — normal-based or by direct binomial/Poisson evaluation.
- **The marks live in the wording:** hypotheses in symbols with the parameter defined; "or more extreme" in discrete tails; the **actual significance level** for discrete critical regions; conclusions non-assertive and in context. A correct calculation with a bald "reject" often drops the final mark.
- **MF19 gives** the binomial and Poisson formulas and the normal table — the critical $z$-values (1.645, 1.96, 2.326, 2.576), the tail discipline, and every scrap of interpretation live in your head.

### Cambridge 9231 — Further Probability & Statistics (forward)

- The FS paper is this ritual with new engines: §4.2 swaps $z$ for Student's $t$ (small $n$, unknown $\sigma$) and tests *differences* of means; §4.3 sends whole distributions to trial ($\chi^2$ goodness-of-fit and contingency tables — Pearson's 1900 invention, with Fisher's degrees-of-freedom correction from their war); §4.4 drops the normality assumption entirely — [[Non-Parametric Tests]]: the sign test *is* this card's binomial test with $p = \tfrac12$, and the Wilcoxon tests replace values by ranks. Master the five-step ritual here and Further Stats is variations on the theme.

### AP Statistics

- The second half of AP Stats is exactly this card at scale: significance tests for proportions and means (Units 6–7), Type I/II errors and **power** named explicitly (9709 stops at the errors; AP names $1 - \beta$), plus χ² and slopes (Units 8–9). AP's conclusion discipline ("compare, decide, contextualise") is the same three closing marks.

### IB

- Formal hypothesis testing lives in **AA's sibling course AI** ($\chi^2$, $t$-tests, SL and HL) — AA itself stops short. For an AA student this card is enrichment that AI classmates sit exams on.

## Beyond the syllabus

> [!info] The 5% that conquered the world — and the crisis it caused
> Why 5%? No theorem: Fisher simply suggested one-in-twenty was "convenient", and a century of science calcified the convenience into a gate. The gate created gamesmanship — **p-hacking**: test twenty things and one will clear 5% by pure chance (the hunter's gallery from [[Sampling and Estimation]], now inside the analysis itself — the tilted spoon is *which results get reported*). The reckoning arrived as the **replication crisis** (mid-2010s: large fractions of published psychology and medical findings failing to replicate), and the American Statistical Association took the rare step of issuing a formal statement warning against bright-line use of p-values. The fix in modern practice: pre-registration (state $H_0$, $H_1$, $\alpha$ and $n$ *before* the data — the exam's "tails from the claim, not the data" rule, made law), effect sizes reported alongside verdicts, and replication treated as the real test.

> [!info] Power — designing the courtroom before the trial
> The $\beta = 0.677$ in the worked example is not a nuisance; inverted, it is a *design tool*. **Power** $= 1 - \beta$ is the probability of catching a guilty defendant, and real experimenters choose $n$ to hit a target power (conventionally 80–90%) against the smallest effect worth detecting — that is why clinical trials announce sample sizes before recruiting a single patient. Power analysis is the engineering discipline hiding behind "how big should my sample be?", and the first thing statistics courses add after this syllabus ends.

> [!info] Two rival courtrooms, one textbook
> The ritual on this card is a historical fusion that its inventors would each half-disown. **Fisher** wanted the tail probability as a continuous *measure of surprise* (report it, weigh it); **Neyman and Pearson** — Egon Pearson, Karl's son, in a rare cross-generational peace — built the rigid decision machine: fix $\alpha$ and $\beta$, define the rejection region (their lemma finds the best one), act, never "conclude". The two camps fought bitterly — Fisher called their approach worthy of "Soviet five-year plans" — and textbooks quietly welded the frameworks together after everyone died. The cast is [[Stories/Inventing Variance]]'s, one generation on, still feuding.

## Connections

- **Builds on:** [[Sampling and Estimation]] — the sampling distribution of $\bar{X}$ is the entire engine of the $z$-test, and the fisherman's-net logic becomes a verdict; [[Normal Distribution]] — critical values, tails, and the approximation route for large discrete tests; [[Discrete Random Variables]] — the binomial on trial; [[Poisson Distribution]] — the promised test on a Poisson mean, delivered.
- **Kindred:** [[Conditional Probability]] — misconception 2 is a conditional-direction error, and the Bayesian road not taken here; [[Stories/Inventing Variance]] — Fisher, the Pearsons, and the human history behind both the tea party and the feud; [[Forward Reading and Problem Discovery]] — "what would this look like if nothing were going on?" is the hunter's null model, the same instinct as [[Poisson Distribution]]'s clustering illusion.
- **For 9709 students:** [[MF19 Reference (9709)]] — distribution formulas and the normal table are on the sheet; critical $z$-values, the tail discipline, and all interpretation are not.
- **Story partner:** [[Stories/The Lady Tasting Tea|The Lady Tasting Tea]] — the afternoon in the 1920s when the five-step ritual was invented over eight cups of tea: randomisation, the null hypothesis, and why the 5% line is a *convenience* and not a law.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $H_0$, $H_1$ | `H_0`, `H_1` | null and alternative hypotheses |
| $\alpha$ | `\alpha` | significance level; also $P(\text{Type I})$ for continuous tests |
| $\beta$ | `\beta` | $P(\text{Type II})$ against a stated true alternative |
| $z = \dfrac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ | `z = \dfrac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}` | the mean's test statistic |
| $P(X \geqslant 12)$ | `P(X \geqslant 12)` | a discrete tail — "or more extreme" |
| $\mu_0$ | `\mu_0` | the value $H_0$ pins the parameter to |
| $\neq$ | `\neq` | the two-tailed alternative's signature |
| $\mid$ | `\mid` | "given that" — the conditional bar in $P(\text{evidence} \mid H_0)$ |
