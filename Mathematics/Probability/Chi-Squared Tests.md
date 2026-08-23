---
chinese: 卡方检验 (kǎfāng jiǎnyàn) — 拟合优度与独立性
prerequisites:
  - "[[Hypothesis Tests]]"
  - "[[t-Tests]]"
  - "[[Discrete Random Variables]]"
  - "[[Continuous Random Variables]]"
  - "[[Normal Distribution]]"
leads_to:
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
  - curriculum/Edexcel-IAL
  - syllabus/9231-4-3
  - type/deep
  - type/technique
  - notation/chi-squared
  - notation/degrees-of-freedom
  - misconception/chi-squared-on-percentages
  - misconception/degrees-of-freedom-ignores-estimated-parameters
  - misconception/small-expected-frequencies-not-combined
  - misconception/contingency-dof-cells-minus-one
---

# Chi-Squared Tests 卡方检验

> *So far every test has put one number on trial — a mean, a difference of means. This card puts a whole shape on trial: is this die fair? are these accidents Poisson? do these frog masses follow a normal curve? does what a customer buys depend on who sold it? The answer comes from one idea — measure every cell's miss in units of its own expected wobble, square, add — and one curve that Pearson invented in 1900 to catch a rigged roulette wheel.*

## Definition

### Formal

Data are sorted into $k$ **cells** (categories, classes, or the cells of a table) with **observed frequencies** $O_1, \dots, O_k$. A hypothesis $H_0$ prescribes the probability of each cell and hence an **expected frequency** $E_i = N p_i$, where $N = \sum O_i$. Pearson's statistic is

$$X^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i},$$

and under $H_0$ — provided every $E_i$ is at least about $5$ — it has approximately a **chi-squared distribution with $\nu$ degrees of freedom**, written $\chi^2_\nu$, where

$$\nu = (\text{number of cells}) - 1 - (\text{number of parameters estimated from the data})$$

for a **goodness-of-fit** test, and $\nu = (r-1)(c-1)$ for a test of **independence** in an $r \times c$ contingency table. Large $X^2$ is evidence against $H_0$; the test is always one-tailed to the right.

### Intuitive

You are a fairness inspector for a die. Roll it $60$ times: a fair die "expects" $10$ of each face, but nobody expects *exactly* $10$ — counts wobble. So for each face ask *how far is the count from $10$, in units of a normal-sized wobble?*, square it so that too-many and too-few both count as misses, and add up the six. That total is $X^2$. If the die is fair the total is usually small — about one unit of miss per free face — and if the die is loaded one face's term is huge. The $\chi^2$ table is simply the record of how big the total gets *for an honest die*, so that you can tell an unusual total from an ordinary one.

The "unit of wobble" is $\sqrt{E}$: a count that is expected to be $E$ has a spread of about $\sqrt{E}$ (a Poisson-like count's variance is its mean). That is why the denominator is $E$ and not $E^2$ or $1$ — each cell's miss is standardised by its own natural spread before it is squared. Cells with tiny $E$ break that approximation, which is why the rule says *combine until every expected frequency is at least $5$*.

### 中文锚点 (Chinese Anchor)

**卡方检验**（$\chi^2$ test）检验的不是一个数，而是一个**形状**：数据是否服从某个给定的分布（**拟合优度检验**，goodness of fit），或者两个分类变量是否**独立**（**独立性检验**，用**列联表** contingency table）。统计量 $\sum\frac{(O-E)^2}{E}$：每格取**观察频数** $O$ 与**期望频数** $E$ 的差，平方后除以 $E$（每格自己的"正常波动"尺度），再求和。中国教材通常把独立性检验（$2\times2$ 表）放在高中，把拟合优度放在大学；剑桥两者同考。**自由度**的规则是本卡最大的考点：格数减一，再减去**从数据估计的参数个数**——估了一个 $p$ 减一，估了 $\mu$ 和 $\sigma$ 减二；列联表则是 $(r-1)(c-1)$。**期望频数不足 5 的格要合并**。

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Observed, expected frequency | $O_i$, $E_i$ | "O i, E i" — yes, *oui*: the observed count is the one that says what actually happened | $E_i = N p_i$ under $H_0$; expected values need not be whole numbers |
| Pearson's statistic | $X^2 = \sum \dfrac{(O-E)^2}{E}$ | "chi-squared statistic" | Written $X^2$ (or $\chi^2_{\text{calc}}$) to keep it apart from the distribution |
| The distribution | $\chi^2_\nu$ | "chi-squared with nu degrees of freedom" | The subscript **is** $\nu$: $\chi^2_1, \chi^2_2, \chi^2_5$ are one family, one curve per number of free cells. Right-skewed, non-negative, mean $\nu$ |
| Degrees of freedom | $\nu$ | "nu" | cells $- 1 -$ parameters estimated; or $(r-1)(c-1)$ |
| Critical value | $\chi^2_\nu(p)$ | "the $p$-point" | MF19 tabulates $x$ with $P(X \le x) = p$ |
| Computing form | $\sum \dfrac{O^2}{E} - N$ | | Algebraically identical; mark schemes accept either |

> [!warning] Reading the MF19 table — always the upper tail, always one-tailed
> The $\chi^2$ table gives $x$ with $P(X \le x) = p$ for each $\nu$. Because a bad fit can only make $X^2$ *large*, the test is always one-tailed to the right, so a 5% test reads the **$p = 0.95$** column ($\nu = 2$: $5.991$; $\nu = 4$: $9.488$), a 10% test the $0.90$ column ($\nu = 4$: $7.779$), and a 0.5% test the $0.995$ column ($\nu = 1$: $7.879$). Never halve the level here — there is no "two-tailed" $\chi^2$ test on this syllabus. The right *row* is the whole degrees-of-freedom skill below.

> [!info] Recall — the computing form $\sum \frac{O^2}{E} - N$
> Expand: $\sum \frac{(O-E)^2}{E} = \sum \frac{O^2}{E} - 2\sum O + \sum E = \sum \frac{O^2}{E} - 2N + N = \sum\frac{O^2}{E} - N$, since both $O$ and $E$ total $N$. Handy on a calculator; the long form shows the examiner which cells you combined, so use that one when combining is part of the question.

## Why it works — one unit of miss per free cell

**The scenario: how much misfit is *normal*?** Roll a genuinely fair die 60 times and compute $X^2$. Do it again; and again. The totals pile up — most near $5$, some near $2$, occasionally one above $11$ — and that pile *is* the $\chi^2_5$ curve. It is not a curve about dice; it is the curve of how much a six-cell tally naturally misfits its own expectation when nothing is wrong. Pearson worked out its exact shape in 1900, and the exam table records it. A test then asks one question: is *my* misfit the size an honest experiment produces, or too big to be honest?

Watch it happen. One die, sixty rolls, the tally, the six terms $(O-10)^2/10$ added by hand into one $X^2$ — then a second die, a tenth, a hundredth, a thousandth, each dropping its own misfit onto the axis until the pile has a shape, and Pearson's curve is laid over it. Every roll is a real random draw, seeded by the date on the frame; rerun it tomorrow and every count changes but the curve does not.

![[chi-squared-honest-die.mp4]]

**What the subscript means.** $\chi^2_5$ is not "chi-squared to the fifth of something": the subscript is $\nu$, the number of *free cells* whose misses were added — one curve for each $\nu$, one family. A die has six cells but a fixed total of 60 rolls, so five are free: $\chi^2_5$. Two cells (heads/tails) with a fixed total have one free: $\chi^2_1$. The left panel below shows the family — $\chi^2_1$ piles up hard against zero (a single squared miss is usually small), $\chi^2_8$ has spread out and moved right — and each curve's mean sits exactly at its own $\nu$. The right panel is the die experiment run twenty thousand times.

![[chi-squared-die-experiment.svg|900]]

**Why the curve has that shape.** Each cell's standardised miss $\dfrac{O - E}{\sqrt{E}}$ is approximately a standard normal variable when $E$ is not tiny (a count is a sum of many yes/no draws, and [[Normal Distribution]] takes over — the same CLT as always). Square it and add over the cells, and you have a **sum of squared standard normals** — which is the definition of a chi-squared variable, the same $\chi^2$ family that sits inside the $t$-statistic's denominator in [[t-Tests]]. A sum of $\nu$ such squares has mean $\nu$: hence the rule of thumb that an honest fit shows **about one unit of miss per free cell**, and the curve's centre sits at $\nu$. It is skewed to the right and never negative because it is a sum of squares.

**Why "free" cells — count the equations the misses must obey.** A degree of freedom is a miss the data was *free to make*. Six faces, sixty rolls: the six misses $O_i - E_i$ are not six independent numbers, because the counts must total $60$ and so must the expecteds — the misses **sum to zero**. Once five are known the sixth is forced (if five faces are $+2, -1, +3, -2, +1$ over, the last is $-3$). Six cells, one equation, five free misses — $\nu = 6 - 1$. The same seesaw as the $n-1$ of [[t-Tests]]: a fixed total takes one freedom away.

**And estimating a parameter from the data takes another — because it adds another equation.** Fit a binomial with $p$ read off the data and you have let the suspect help set the ruler: $\hat p$ is chosen so that the model's expected number of successes *equals* the observed number exactly. That is a second equation the misses now satisfy (in Case 1A below: the total broken eggs, $\sum i\,O_i$, equals the fitted total, $\sum i\,E_i$, by construction). Two equations tie the misses together, so two of them are forced by the rest — cells $- 1 - 1$. Each parameter estimated from the data is one more direction in which the model was allowed to chase the data, one more equation the misses must obey, one more degree of freedom gone — that is the *"appropriate number of degrees of freedom"* the syllabus keeps repeating. Fit a normal with $\bar{x}$ and $s^2$ from the data: two parameters, two more equations, two more freedoms gone. And a misfit that was allowed to shrink along those directions is compared against the *smaller* $\chi^2$ curve — the honest ruler for a model that has already been fitted.

**Why $E \geq 5$.** The normal approximation to each cell's count is what makes the sum a $\chi^2$; a cell expected to hold $0.1$ of a frog is nowhere near normal, and one lucky observation there contributes $\dfrac{(1 - 0.1)^2}{0.1} = 8.1$ on its own — a rigged jury. Combining sparse cells until each expects at least $5$ keeps every term honest. Note the arithmetic that follows: **combining cells changes the number of cells, and therefore $\nu$** — count the cells *after* combining.

**The history is honest about who was right.** Pearson invented the statistic in 1900 — his worked example was Monte Carlo roulette, whose published spins misfit a fair wheel so badly he declared the tables rigged (they were more likely just misrecorded). But he got the degrees of freedom wrong for contingency tables and for fitted parameters; R. A. Fisher corrected both in 1922 — the $(r-1)(c-1)$ and the "minus one per estimated parameter" you use — and Pearson, twenty-five years his senior and editor of the journal, never accepted it. The rule on your formula sheet is the younger man's, and it took a decade to be believed.

## The two engines — each with the real cases it exists for

Recall the five-step ritual of [[Hypothesis Tests]] — **state** $H_0, H_1$; **read** the tail (always the upper one here); **compute**; **compare**; **conclude in context**. Two engines run it. Each is stated in a few lines and then run on real Paper 4 questions, worked with the mark-scheme values.

### Engine 1 — goodness of fit: does this distribution describe the data?

**The tool.**
1. **State** $H_0$: *the named distribution is a satisfactory model for the data*; $H_1$: it is not. (Mark schemes require both the *distribution* and the *data* to be named.)
2. **Expected frequencies**: $E_i = N p_i$, with $p_i$ from the hypothesised distribution — a formula (binomial, Poisson, uniform), a table (normal), or an integral (a given pdf, [[Continuous Random Variables]]). Any parameter not given must be **estimated from the data** ($p$ from the sample proportion, $\lambda$ from the sample mean, $\mu, \sigma^2$ from $\bar{x}, s^2$) — and each one estimated costs a degree of freedom.
3. **Combine** adjacent cells until every $E_i \geq 5$; count the cells that remain.
4. $X^2 = \sum \dfrac{(O-E)^2}{E}$ over the combined cells; $\nu = \text{cells} - 1 - \text{parameters estimated}$.
5. **Compare** with $\chi^2_\nu$'s upper-tail value at the stated level; conclude in context.

The three cases below differ in exactly one respect each — the parameter count — and together they *are* the degrees-of-freedom rule.

**Case 1A — one parameter estimated: 9231/41 June 2025 Q3.**

> Eggs are sold in boxes of six. In a random sample of $2000$ boxes the number of broken eggs per box was: $0$: $1844$; $1$: $143$; $2$: $11$; $3$: $0$; $4$: $1$; $5$: $0$; $6$: $1$.
> **(a)** Use the data to estimate the probability that an egg is broken, to 4 s.f. **[1]**
> A goodness-of-fit test at the **0.5%** level is to decide whether a binomial distribution fits. Expected frequencies: $1831.3,\ a,\ 6.016,\ 0.119,\ 0.001,\ 0.000,\ 0.000$.
> **(b)** Find $a$. **[1]** **(c)** Carry out the test. **[6]**

**Why this engine, and why $\nu = 1$.** One variable (broken eggs per box) against one named distribution — goodness of fit. The binomial needs $n = 6$ (given) and $p$ (**not** given: it must come from the data), so one parameter is estimated. And the tail cells are far below $5$, so they will be combined.

**(a)** *Tool: $p$ from the data — total broken eggs over total eggs.* $\hat{p} = \dfrac{0 \cdot 1844 + 1 \cdot 143 + 2 \cdot 11 + 4 \cdot 1 + 6 \cdot 1}{2000 \times 6} = \dfrac{175}{12000} = 0.01458$.

**(b)** *Tool: expected frequencies sum to $N$.* $a = 2000 - (1831.3 + 6.016 + 0.119 + 0.001) = 162.6$ (or directly, $2000 \times 6\hat{p}(1-\hat{p})^5$).

**(c)** $H_0$: a binomial distribution is a satisfactory model for the data; $H_1$: it is not.

*Tool: combine until $E \geq 5$.* Cells for $2, 3, 4, 5, 6$ have expected $6.016 + 0.119 + 0.001 + 0 + 0 = 6.136$ together — so the table becomes three cells: $O = 1844, 143, 13$ against $E = 1831.3, 162.6, 6.136$.

*Tool: the statistic.*
$$X^2 = \frac{(1844 - 1831.3)^2}{1831.3} + \frac{(143 - 162.6)^2}{162.6} + \frac{(13 - 6.136)^2}{6.136} = 0.088 + 2.363 + 7.678 = 10.1.$$

*Tool: degrees of freedom — count after combining, then pay for the estimate.* $3$ cells $- 1 - 1$ (for $\hat{p}$) $= 1$. **Table read:** row $\nu = 1$, column $p = 0.995$ (a 0.5% test, upper tail) → **$7.879$**.

> [!info] Why $1$, and not $3$ or $2$ — the three misses obey two equations
> The three misses are $O - E = +12.7,\ -19.6,\ +6.9$. They are not three free numbers.
> **Equation 1 (the total):** observed and expected both sum to $2000$, so the misses sum to $0$: $12.7 - 19.6 + 6.9 = 0$ (to the rounding of the printed $E$'s). Know two, and the third is forced. That is the $-1$ every goodness-of-fit test pays.
> **Equation 2 (the estimate):** $\hat p$ was chosen from *these* data — $175$ broken eggs out of $12000$ — so the fitted binomial's expected number of broken eggs is $2000 \times 6\hat p = 175$: exactly the observed number. The model was tuned to match the data on that count, which is a second relation between the $O$'s and the $E$'s (in the uncombined table, $\sum i\,O_i = \sum i\,E_i$). Had the question *given* $p = 0.015$, that equation would not exist and $\nu$ would be $2$.
> Three misses, two equations, **one free miss** — so the honest ruler is $\chi^2_1$, the tightest curve in the family, and $10.1$ against $7.879$ is a clear rejection.

$10.1 > 7.879$: reject $H_0$. Even at 0.5%, the binomial is not a satisfactory model — and the contributions say *where*: $7.68$ of the $10.1$ comes from the "$2$ or more" cell. There are more multiply-broken boxes than independent breakage predicts, which is what you would expect if broken eggs cluster (a dropped box breaks several). The test found the physics.

**Case 1B — no parameter estimated: 9231/43 June 2026 Q4.**

> $200$ observations of a continuous variable $X$: $[1, 1.5)$: $97$; $[1.5, 2)$: $35$; $[2, 2.5)$: $23$; $[2.5, 3)$: $15$; $[3, 3.5)$: $10$; $[3.5, 4)$: $6$; $x \geq 4$: $14$. Test the goodness of fit of the pdf $f(x) = 2/x^3$ for $x \geq 1$ (zero otherwise). Expected frequencies given: $111.11,\ a,\ 18.00,\ 9.78,\ b,\ 3.83,\ 12.50$.
> **(a)** Show that $a = 38.89$ and find $b$. **[3]** **(b)** Test at the 10% level. **[7]**

**Why this engine, and why $\nu = 5$.** One variable against one fully specified pdf — nothing to estimate, so no parameter is charged. Expected frequencies come from *integrating* the pdf over each class ([[Continuous Random Variables]]). Two cells ($5.90$ and $3.83$) sit at or below $5$ → combine.

**(a)** *Tool: $E = N \times \int_{\text{class}} f$.* $\displaystyle a = 200\int_{1.5}^{2} \frac{2}{x^3}\,dx = 200\left[-\frac{1}{x^2}\right]_{1.5}^{2} = 200\left(\frac{1}{2.25} - \frac{1}{4}\right) = 200 \times \frac{7}{36} = 38.89$; $\ b = 200\left(\frac{1}{9} - \frac{1}{12.25}\right) = 5.90$.

**(b)** $H_0$: $f$ is a good fit for the data; $H_1$: it is not.

*Tool: combine.* The $[3.5, 4)$ cell expects $3.83 < 5$: merge it with $[3, 3.5)$ to give $O = 16$, $E = 9.72$ (the mark scheme equally accepts merging it with $x \geq 4$: $O = 20$, $E = 16.33$). Six cells remain.

$$X^2 = \frac{(97-111.11)^2}{111.11} + \frac{(35-38.89)^2}{38.89} + \frac{(23-18)^2}{18} + \frac{(15-9.78)^2}{9.78} + \frac{(16-9.72)^2}{9.72} + \frac{(14-12.5)^2}{12.5} = 1.79 + 0.39 + 1.39 + 2.79 + 4.06 + 0.18 = 10.6.$$

*Degrees of freedom:* $6 - 1 - 0 = 5$. **Table read:** row $5$, column $0.90$ → **$9.236$**. $10.6 > 9.236$: reject $H_0$; sufficient evidence at 10% that $f$ is not a good fit. (Note the mark scheme's warning: an answer computed *without* combining is capped — the combining is a marked step, and $\nu$ moves with it.)

**Case 1C — two parameters estimated: 9231/44 June 2026 Q3.**

> A biologist believes the masses of a species of frog are normal. $120$ frogs: $<210$: $2$; $[210,220)$: $9$; $[220,230)$: $20$; $[230,240)$: $39$; $[240,250)$: $40$; $[250,260)$: $8$; $\geq 260$: $2$. From these data he estimates $\mu = 236.5$ g and $\sigma^2 = 134.56$ g². Expected frequencies: $1.34,\ 7.94,\ 25.22,\ 39.73,\ 31.11,\ c,\ d$.
> **(a)** Find $c$ and $d$. **[2]** **(b)** Test at the 5% level whether a normal distribution is a suitable model. **[7]**

**Why this engine, and why $\nu = 2$.** One variable against a normal model whose *both* parameters came from the data — so two are charged. Both end cells are below $5$ → combine at each end.

**(a)** *Tool: normal probabilities with $\mu = 236.5$, $\sigma = 11.6$ ([[Normal Distribution]]).* $c = 120\,P(250 \leq X < 260) = 120\left[\Phi\!\left(\tfrac{260-236.5}{11.6}\right) - \Phi\!\left(\tfrac{250-236.5}{11.6}\right)\right] = 120\,[\Phi(2.026) - \Phi(1.164)] = 12.10$; $\ d = 120\,[1 - \Phi(2.026)] = 2.57$.

**(b)** $H_0$: a normal distribution is a suitable model for the masses; $H_1$: it is not.

*Tool: combine both ends.* $\{<210, [210,220)\}$: $O = 11$, $E = 9.28$; $\{[250,260), \geq 260\}$: $O = 10$, $E = 14.67$. Five cells remain.

$$X^2 = \frac{(11-9.28)^2}{9.28} + \frac{(20-25.22)^2}{25.22} + \frac{(39-39.73)^2}{39.73} + \frac{(40-31.11)^2}{31.11} + \frac{(10-14.67)^2}{14.67} = 0.319 + 1.080 + 0.013 + 2.540 + 1.487 = 5.44.$$

*Degrees of freedom:* $5 - 1 - 2 = 2$. **Table read:** row $2$, column $0.95$ → **$5.991$**. $5.44 < 5.991$: do not reject $H_0$; the normal model is consistent with the data at 5%. (Had the two parameters not been charged — $\nu = 4$, critical $9.488$ — the verdict is the same here, but the mark for the critical value is not: the scheme awards the B1 for $5.991$ *with both ends combined*.)

---

### Engine 2 — independence in a contingency table: does one thing depend on another?

**The tool.** Two categorical variables cross-tabulated in $r$ rows and $c$ columns.
1. $H_0$: the two variables are **independent** (no association); $H_1$: they are not.
2. **Expected count** in each cell *if independent*: $E = \dfrac{\text{row total} \times \text{column total}}{N}$ — because independence means the row's share of the grand total is the same in every column ($P(A \cap B) = P(A)P(B)$, [[Probability Basics]] doing statistics).
3. Combine rows or columns if any $E < 5$.
4. $X^2 = \sum \dfrac{(O-E)^2}{E}$ over all cells; $\nu = (r-1)(c-1)$.
5. Compare with $\chi^2_{(r-1)(c-1)}$'s upper tail; conclude in terms of association.

**Why $(r-1)(c-1)$.** Every row total and column total is fixed by the data, so once $r-1$ entries of each of $c-1$ columns are filled in, the rest of the table is forced. No parameter is "estimated" — the marginal totals do that job — so nothing further is subtracted.

**The case — 9231/44 June 2025 Q3.**

> Three salespeople, three item types, a random sample of $250$ sales:
>
> ![[chi-squared-salespeople-table.svg|520]]
>
> Test at the 10% level whether there is independence between the type of item sold and the salesperson. **[7]**

**Why this engine, and why $\nu = 4$.** Two categorical variables — *who sold* and *what* — and the question is association, not fit to a named distribution: a contingency table. $3 \times 3$ gives $\nu = 2 \times 2 = 4$. Every expected count will turn out above $5$, so nothing is combined.

$H_0$: type of item sold is independent of salesperson; $H_1$: it is not.

*Tool: expected counts, row × column ÷ total.* Avril–Laptop: $\dfrac{95 \times 75}{250} = 28.5$; Avril–Camera $41.8$; Avril–TV $24.7$; Ben: $29.1$, $42.68$, $25.22$; Charlie: $17.4$, $25.52$, $15.08$. (Check: each row and column of $E$ still sums to the observed totals — it always must.)

![[chi-squared-contingency-cells.svg|880]]

*Tool: the statistic, all nine cells.*
$$X^2 = \frac{(31-28.5)^2}{28.5} + \frac{(40-41.8)^2}{41.8} + \cdots + \frac{(12-15.08)^2}{15.08} = 3.67.$$

**Table read:** row $\nu = 4$, column $0.90$ → **$7.779$**. $3.67 < 7.779$: do not reject $H_0$. No evidence at 10% of association between item type and salesperson — the three sell the same *mix*, whatever their totals. (Charlie sells fewest, but the test is blind to that on purpose: row totals are absorbed into $E$. It asks about the *pattern*, not the volume.)

## Choosing the engine

| The question is about… | Data look like… | Engine | $\nu$ |
|---|---|---|---|
| whether **one variable** follows a **named distribution** (fair die, binomial, Poisson, normal, a given pdf, a stated ratio) | one row of counts by value or class, with a model to fit | goodness of fit | cells $- 1 -$ parameters estimated |
| whether **two categorical variables** are **associated** | a two-way table of counts | independence | $(r-1)(c-1)$ |

Then the two housekeeping questions that carry marks: *which parameters did I take from the data?* and *did I combine every cell below 5 — and recount?*

## Where the chi-squared test meets the world

- **Forensic accounting — Benford's law.** In most naturally occurring numbers (invoices, populations, river lengths) the leading digit is $1$ about $30\%$ of the time and $9$ about $5\%$ — a logarithmic law, not a uniform one. Auditors run a goodness-of-fit test of a ledger's leading digits against Benford's expected frequencies; fabricated figures, made up by people who think "random" means "uniform", fail it. It has been admitted as evidence in fraud cases. Engine 1, nine cells, $\nu = 8$.
- **Genetics.** Mendel's $3:1$ and $9:3:3:1$ ratios are goodness-of-fit hypotheses, and every genetics lab tests a cross against them with $\chi^2$. The honest edge is famous: in 1936 Fisher ran the test on Mendel's own published data and found the fit *too good* — $X^2$ so small, so consistently, that the chance of honest data agreeing that well was about one in thirty thousand. Whether Mendel, a gardener, or a well-meaning assistant tidied the counts is still argued; the point for us is that the $\chi^2$ curve has a *lower* tail too, and data that never misfit are as suspicious as data that always do.
- **Every "does A depend on B" question with categories.** Treatment × outcome in a clinical trial; smoker × disease; version A/B × converted-or-not; region × vote — all $2\times2$ or $r \times c$ contingency tables, all engine 2. It is the most-run test in medicine and the social sciences because most real variables are categories, not measurements.
- **Machine learning's feature filter.** Before training a spam filter, which words are worth keeping? For each word, cross-tabulate *word present?* against *spam?* and compute $X^2$; the words with the largest values are the ones whose presence is least independent of the label. "Chi-squared feature selection" is a standard function in every ML library — engine 2 run once per word over a vocabulary of a hundred thousand.

## Common Misconceptions (Teaching Notes)

### 1. Running the test on percentages

$X^2$ compares *counts*; feed it percentages and every term is scaled by $100/N$, so the statistic is wrong by that factor and the verdict with it.

**Fix:** convert to frequencies first — the $E$'s must total $N$, and a $2\%$ cell in $50$ observations is one observation, not two.

### 2. Forgetting to charge for estimated parameters

$\nu = \text{cells} - 1$ is only right when the model was fully specified in the question.

**Fix:** before reading the table, ask *what did I take from the data?* — a $p$, a $\lambda$, a $\mu$ and $\sigma$ — and subtract one for each. Cases 1A/1B/1C are the same test with charges of $1$, $0$, $2$.

### 3. Not combining (or combining $O$ but not $E$)

A cell expecting $0.1$ contributes wildly, and the mark scheme caps an uncombined answer.

**Fix:** combine *both* rows of the table — observed and expected — into the merged cell, then recount the cells for $\nu$. In a contingency table, combine whole rows or columns, never a single cell.

### 4. Contingency degrees of freedom as "cells − 1"

$3 \times 3$ has nine cells; $\nu$ is $4$, not $8$.

**Fix:** the row and column totals are fixed; only an $(r-1) \times (c-1)$ block is free. Draw the table and shade the last row and column — they are determined.

### 5. Hypotheses that name neither the model nor the data

"$H_0$: the data are binomial" or "$H_0$: no difference" both lose the mark.

**Fix:** the scheme's own phrasing — *a [named] distribution is a satisfactory model for [the named data]*; for tables, *[variable] is independent of / not associated with [variable]*.

### 6. Stopping at "reject"

The verdict is one mark; the *reason* is where the understanding is.

**Fix:** look at the contributions. Case 1A's $7.68$ from the "$2$ or more" cell says the eggs break in clusters; a table's biggest cell says which combination is over-represented. A $\chi^2$ test that ends at a number has thrown away its best sentence.

## Exam Notes

### Cambridge 9231 — Further Probability & Statistics, §4.3

Three learning objectives, and a $\chi^2$ question appears on every recent Paper 4, usually 7–10 marks:

- **Fit a theoretical distribution prescribed by a hypothesis** — binomial, Poisson, normal, uniform, a given ratio, or a given pdf by integration; the syllabus promises *"questions will not involve lengthy calculations"*, so most expected frequencies are printed and you compute one or two (the *"find $a$ / show that $b = \dots$"* parts of Cases 1A–1C). Estimating a parameter from the data ($\hat{p} = 175/12000$; $\bar{x}, s^2$ for the normal) is itself a marked step.
- **Goodness of fit with the appropriate degrees of freedom** — the syllabus's own note: *"classes should be combined so that each expected frequency is at least 5"*. Combining is a B1/M1 on its own; the critical value B1 depends on the *combined* cell count and the parameter charge.
- **Independence in a contingency table** — *"Yates' correction is not required"*; expected values must be *seen* (M1 for at least four correct); $\nu = (r-1)(c-1)$; the conclusion phrased as association/independence in context.
- Hypotheses must name the distribution/model *and* the data ("must mention binomial and data"); the test is one-tailed upper — read the $0.95$ / $0.90$ / $0.995$ column directly.

### AP Statistics — Unit 8, Inference for Categorical Data: Chi-Square

The same two engines plus a third name: AP distinguishes the test of **homogeneity** (several populations, one categorical variable — did the samples come from populations with the same distribution?) from **independence** (one population, two variables), though the arithmetic is identical. Conditions are stated every time — random, 10% condition, all expected counts $\geq 5$ ("large counts") — and $\chi^2$ tests are calculator procedures with $p$-values reported. Degrees of freedom for goodness of fit are $k - 1$: AP does not go into charging for estimated parameters.

### Edexcel IAL — Statistics 3, §4

Examined in full: goodness of fit to *"the discrete uniform, binomial, Normal, Poisson and continuous uniform (rectangular) distributions"*, with degrees of freedom *"when one or more parameters are estimated from the data"* — the same charge as 9231 — and contingency tables. (The one thing IAL S3 does *not* require is the $t$-distribution; here the two boards agree.)

### IB Mathematics: Applications and Interpretation

$\chi^2$ goodness of fit and the $\chi^2$ test for independence are **SL** content in AI (4.11), GDC-driven with $p$-values; expected frequencies $\geq 5$ and the $(r-1)(c-1)$ rule are the same. AA has no hypothesis testing.

### Where it is *not* examined

**Cambridge 9709** stops before any distribution-fitting test; **0580**, **0606**, **OxAQA 9660** and **IB AA** have none of it.

### Beyond high school — University

The two engines are the front door of *categorical data analysis*: Fisher's exact test for tables too small to combine, the likelihood-ratio ($G$) test that Pearson's statistic approximates, log-linear models for three-way tables, and — everywhere in modern genetics — association tests that are engine 2 run millions of times across a genome.

> [!info] Beyond syllabus — the Pearson–Fisher quarrel, and why the young man was right
> Pearson's 1900 paper counted degrees of freedom as $k - 1$ always. Fisher showed in 1922 that a fitted parameter reduces the effective dimension of the misfit — the model has been *allowed to move toward the data* along one direction per parameter — and that a contingency table's fixed margins leave only $(r-1)(c-1)$ free cells. Pearson refused the correction, and as editor of *Biometrika* refused to print it; Fisher published elsewhere and the dispute poisoned the two men's relations for life. Modern textbooks (and MF19) use Fisher's counts without comment. It is worth knowing that the "appropriate number of degrees of freedom" the syllabus stresses is precisely the point that took the discipline a decade to settle.

> [!info] Beyond syllabus — Yates, and the small-table problem
> For a $2\times2$ table with small counts, the smooth $\chi^2$ curve approximates a lumpy discrete reality badly, and Pearson's statistic runs slightly *too large*. Yates' 1934 correction subtracts $\tfrac12$ from each $|O - E|$ before squaring; the syllabus tells you it is not required. When counts are very small the honest tool is Fisher's exact test, which computes the table's probability directly from the hypergeometric distribution — no approximation, no curve.

## Connections

- **Parent:** [[Hypothesis Tests]] — the ritual, the tail from the claim, the conclusion discipline; here the tail is always the upper one.
- **The family, seen before:** [[t-Tests]] — the $\chi^2$ distribution already lived in the $t$-statistic's denominator as $(n-1)S^2/\sigma^2$; this card examines it in its own right, and reuses the seesaw for degrees of freedom.
- **What gets fitted:** [[Discrete Random Variables]] (binomial pmf for Case 1A), [[Poisson Distribution]] (the other classic fit — $\lambda$ from the sample mean, one parameter charged), [[Normal Distribution]] (Case 1C's probabilities), [[Continuous Random Variables]] (Case 1B — expected frequencies by integrating a pdf).
- **The rule underneath engine 2:** [[Probability Basics]] — $P(A \cap B) = P(A)P(B)$ under independence is the whole of the row × column ÷ total formula.
- **Continues in:** [[Non-Parametric Tests]] — the third kind of test on this paper, for when even the shape of the population is off the table.
- **For 9231 students:** [[MF19 Reference (9231)]] — the $\chi^2$ table is printed; the statistic $\sum\frac{(O-E)^2}{E}$ and the degrees-of-freedom rule are **not** — those are the two things to carry in your head.
- **Story partner:** [[Stories/The Lady Tasting Tea|The Lady Tasting Tea]] — the Pearson–Fisher quarrel from the human side, and the eight-cups test that is Fisher's exact test in its first form.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\chi^2_\nu$ | `\chi^2_\nu` | the distribution |
| $\sum \dfrac{(O-E)^2}{E}$ | `\sum \dfrac{(O-E)^2}{E}` | Pearson's statistic |
| $\sum \dfrac{O^2}{E} - N$ | `\sum \dfrac{O^2}{E} - N` | computing form |
| $(r-1)(c-1)$ | `(r-1)(c-1)` | contingency degrees of freedom |
| $E = \dfrac{\text{row} \times \text{col}}{N}$ | `E = \dfrac{\text{row} \times \text{col}}{N}` | expected count under independence |
| $\Phi(z)$ | `\Phi(z)` | normal cdf, for normal-fit probabilities |
