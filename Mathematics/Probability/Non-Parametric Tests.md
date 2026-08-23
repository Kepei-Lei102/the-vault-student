---
chinese: 非参数检验 (fēi cānshù jiǎnyàn) — 符号检验与 Wilcoxon 秩检验
prerequisites:
  - "[[Hypothesis Tests]]"
  - "[[t-Tests]]"
  - "[[Chi-Squared Tests]]"
  - "[[Discrete Random Variables]]"
  - "[[Normal Distribution]]"
  - "[[Averages and Spread]]"
leads_to:
  - "[[The Lady Tasting Tea]]"
tags:
  - subject/mathematics
  - domain/statistics
  - domain/probability
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/A-Level
  - syllabus/9231-4-4
  - type/deep
  - type/technique
  - notation/signed-rank-T
  - notation/rank-sum-W
  - misconception/hypotheses-about-means-in-a-median-test
  - misconception/T-must-be-the-smaller-rank-sum
  - misconception/wilcoxon-table-rejects-below
  - misconception/wilcoxon-needs-normality
---

# Non-Parametric Tests 非参数检验

> *Fifteen salaries, one of them $\$125{,}000$. A $t$-test on that sample is mostly a $t$-test on that one salary. These are the tests that refuse to be bullied by a number: throw away the distances and keep only the **signs**, or keep the **order** of the distances but not their size — and the price of that refusal is paid in exactly one currency, the assumptions you no longer need. When you cannot trust the shape of the population, trust the order.*

## Definition

### Formal

A **non-parametric** (distribution-free) test makes no assumption that the population belongs to a named family — normal, binomial, anything. Its test statistic is built from **signs** or **ranks**, and its null distribution follows from symmetry and counting alone, so the critical values are exact for *any* continuous population that satisfies the (much weaker) hypothesis. The three tests on this syllabus:

| Test | Statistic | Assumes under $H_0$ | Null distribution |
|---|---|---|---|
| **Sign test** | $S$ = number of observations (or paired differences) above the hypothesised median $m_0$ (or above $0$) | nothing beyond independence | $S \sim B(n, \tfrac12)$ |
| **Wilcoxon signed-rank test** | rank the $\lvert x_i - m_0 \rvert$ (or $\lvert d_i \rvert$) $1..n$; $P$ = sum of ranks with $+$ sign, $Q$ = sum with $-$; $T = \min(P, Q)$ | the population (of differences) is **symmetric** about $m_0$ (about $0$) | each rank $+$ or $-$ with probability $\tfrac12$: $2^n$ equally likely sign patterns; MF19 tabulates the largest $T$ that rejects |
| **Wilcoxon rank-sum test** | pool the two samples (sizes $m \le n$), rank $1..m{+}n$; $R_m$ = rank sum of the smaller sample; $W = \min\!\big(R_m,\ m(m+n+1) - R_m\big)$ | the two populations are **identical** | the $m$ ranks are a random subset of $\{1..m{+}n\}$: $\binom{m+n}{m}$ equally likely hands; MF19 tabulates the largest $W$ that rejects |

The hypotheses are about the **population median** (single-sample and paired designs) or the **identity of two populations** (rank-sum). For large samples $P$, $Q$ and $R_m$ are approximately normal:

$$P,\ Q \;\approx\; N\!\Big(\tfrac{n(n+1)}{4},\ \tfrac{n(n+1)(2n+1)}{24}\Big), \qquad R_m \;\approx\; N\!\Big(\tfrac{m(m+n+1)}{2},\ \tfrac{mn(m+n+1)}{12}\Big),$$

with a continuity correction of $\pm\tfrac12$ because the statistics are integers.

### Intuitive

Three referees watch the same fifteen salaries against the company's claim "the median is $\$32{,}500$". They differ in what they *see* — and therefore in what they are allowed to *say*.

- The **sign referee** only sees which side of the line each salary fell — eleven below, four above — and asks whether a fair coin gives eleven tails in fifteen. She cannot be bribed by the size of any salary: $\$125{,}000$ is one "above", exactly like $\$33{,}000$. **What she can tell you:** whether the *population median* is $\$32{,}500$ ($H_0$) or not ($H_1$: it is not / it is lower / it is higher, as the claim directs). Nothing about the mean, nothing about spread — and she needs no promise about the population's shape at all.
- The **rank referee** sees which side *and how far, in order*: the nearest salary to the line is rank $1$, the farthest is rank $15$, and she adds the ranks on each side. She hears more than the first referee — a side that keeps getting the *big* ranks is suspicious even when the count is even. **What she can tell you:** the same thing — is the population median $\$32{,}500$ ($H_0$) or not ($H_1$)? — but with sharper hearing, *provided the population is symmetric about its median*. That is her one condition, and it is not something she tests; it is something you must be able to grant her before she speaks. If the population is skewed, one side is *supposed* to get the big ranks, and her verdict is worthless.
- The **distance referee** — the $t$-test — hears everything, including that one salary is $\$92{,}500$ above the line. **What she can tell you:** whether the population *mean* is $\$32{,}500$ ($H_0$: $\mu = 32\,500$) — a different question, and one that needs a normal population (or a large sample). On a normal population that is the sharpest hearing of all; on salaries it means one employee decides the verdict, about a mean that the same employee has already dragged.

And when there are **two separate groups** rather than one sample against a claim — six people over 50 and eight under 25 — the rank referee's cousin, the **rank-sum referee**, pools everyone, ranks them, and asks whether one group's ranks sit at one end. **What she can tell you:** whether the two populations are the same ($H_0$: identical populations, equal medians) or whether one lies above the other ($H_1$). She needs the two groups to be *different people* — pairing is information she throws away — and the two populations to have the same shape.

![[nonparametric-information-ladder.svg|860]]

Each rung up the ladder uses more of the data and demands more of the population. The syllabus's own words: use a non-parametric test *"when sampling from a population which cannot be assumed to be normally distributed"* — and the Wilcoxon tests *"are valid only for symmetrical distributions"*.

### 中文锚点 (Chinese Anchor)

一句话：数据长得不像正态、或者带着离谱的极端值时，别硬用 $t$ 检验——改用只看"在哪一边"或"排第几名"的检验。三个工具，各自**能说什么、要什么、差在哪**：

- **符号检验**（sign test）：只数每个数据落在假设中位数的**哪一边**。要求几乎没有——只要"高于/低于"说得清就行，工资、房价、排队时间都能用。能说的是：中位数是不是这个值（配对数据：两次测量的差是不是没有偏向）。代价是最不灵敏——它把"差多少"全扔了，十对数据里要九对同向它才肯开口。
- **Wilcoxon 符号秩检验**（signed-rank）：既看哪一边，也看**差多远——但只按名次**。要求：总体要**对称**（不必正态）。能说的还是中位数，但灵敏得多——拼图那道题，符号检验说"证据不够"，它说"够了"，因为它听见了两个反例恰好是差得最小的两个。缺点：数据一歪（工资、房价这种一头长尾的），名次大的会天然堆到长尾那边，它就会冤枉一个其实成立的中位数——所以考题问"为什么 Wilcoxon 不合适"，答案是"数据有偏/有极端值，总体不一定对称"。
- **Wilcoxon 秩和检验**（rank-sum）：两组**不同的人**（不是同一批人测两次），混在一起排名次，看小组的名次是不是集中在一头。要求：两组分布形状一样，同样不要正态。能说的是：两组是不是同一个总体（中位数是否相同）。缺点：如果数据本来是配对的，用它等于把配对信息扔掉了。

样本大到表里查不到临界值时用正态近似，别忘了 ±½ 的修正。考纲承诺不会出现并列名次、也不会出现恰好等于中位数的观测。考试里另一句常问的话："为什么配对 $t$ 检验不合适？"——因为差值的总体不一定正态。

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Hypothesised median | $m_0$ | "m nought" | Hypotheses are about the **population median** $m$ — never the mean |
| Sign count | $S$ | | number of $+$ (or $-$) signs; $S \sim B(n, \tfrac12)$ under $H_0$ |
| Signed-rank sums | $P$, $Q$ | | sums of ranks of $\lvert d \rvert$ carrying $+$ / $-$ signs; $P + Q = \tfrac12 n(n+1)$ always |
| Signed-rank statistic | $T = \min(P, Q)$ | | MF19 gives the **largest $T$ that rejects**: reject when $T \le$ table value |
| Rank sum | $R_m$ | | rank sum of the **smaller** sample ($m \le n$) in the pooled ranking |
| Rank-sum statistic | $W = \min\!\big(R_m,\ m(m+n+1)-R_m\big)$ | | the second term is what $R_m$ would be if the ranking ran backwards; reject when $W \le$ table value |
| Continuity correction | $\pm\tfrac12$ | | $P(T \le t) \approx \Phi\!\big(\tfrac{t + 0.5 - \mu}{\sigma}\big)$ |

> [!warning] Reading the two MF19 tables — the sign is the opposite of every other table
> Every table you have used so far — $z$, $t$, $\chi^2$ — rejects when **the value you calculated is larger than the value you read from the table**. The Wilcoxon tables work the other way round: you reject when **your calculated $T$ (or $W$) is smaller than or equal to the value you read from the table**. The table itself says so — it prints *"the largest value of $T$ which will lead to rejection"* — so the test is: calculated $T \le$ table value → reject; calculated $T >$ table value → do not. Read the row by $n$ (signed-rank; $6 \le n \le 20$) or by the pair $(m, n)$ with $m \le n \le 10$ (rank-sum); read the column by the level **and by tails** — the table has a one-tailed row and a two-tailed row, so a 5% one-tailed test and a 10% two-tailed test share a column. A dash means *no rejection is possible at that level with that few observations* (there simply is no rare enough outcome). Beyond the table's range, use the normal approximation.

## Why it works — count the ways an honest sample could have come out

**The referee who sees only the side of the line.** If the population median really is $m_0$, every observation lands above it with probability $\tfrac12$ — that is what *median* means. Nothing else about the population enters. So the number above is a count of heads in $n$ fair coin tosses, $S \sim B(n, \tfrac12)$, and the sign test is exactly the binomial test of [[Hypothesis Tests]] with $p = \tfrac12$. It needs no symmetry, no shape, no scale: only that "above" is well defined. That is why, when the data are visibly skewed (salaries, house prices, waiting times, item counts), the mark scheme's expected answer is the sign test — the Wilcoxon has lost its licence but the sign test never had one to lose.

Watch the claim come true. Take a population of $400$ numbers — skewed on purpose, like salaries — and find *its own* median, so that "the median is here" is true by construction: exactly $200$ above, $200$ below. Now draw a random sample of ten and count the split. It comes out $6$–$4$, then $5$–$5$, then $4$–$6$ — it dangles around the middle — and only once in a thousand samples does it reach $10$–$0$. Pile up the counts and the pile is $B(10, \tfrac12)$: ten fair coins, exactly what the sign test uses to price a split. That is the whole test in one picture — an $8$–$2$ split or worse in one direction is what a fair coin does $5.5\%$ of the time, so at 5% it is *not quite* surprising enough (that is the jigsaw children in Case 2B), while a $10$–$0$ split is one sample in a thousand.

![[sign-test-median-coin.mp4]]

**The tables are not measured — they are counted.** Suppose the population is symmetric about $m_0$ and you rank the six distances $\lvert x_i - m_0\rvert$ from $1$ to $6$. Symmetry says each rank is equally likely to belong to an observation above the line as below it, independently of the others. So there are $2^6 = 64$ equally likely sign patterns, and the sum $Q$ of the ranks that came out negative has a distribution you can *count*: $Q = 0$ in one pattern (all positive), $Q = 1$ in one, $Q = 2$ in one, $Q = 3$ in two ($\{3\}$ or $\{1,2\}$), … Three patterns of $64$ give $Q \le 2$: $4.7\%$. Five give $Q \le 3$: $7.8\%$. So the largest $T$ that rejects at $5\%$ one-tailed for $n = 6$ is **2** — and that is the number printed in MF19. The rank-sum table is the same idea with a different count: if two populations are identical, the pooled ranks are dealt at random to the two samples, so every hand of $m$ ranks from $m+n$ is equally likely — $\binom{6}{3} = 20$ hands for $m = n = 3$, and only $\{1, 2, 3\}$ gives $R_3 = 6$: one in twenty, $5\%$. That is why the one-tailed $5\%$ entry is $6$, and why the two-tailed entry is a dash — no hand is rare enough for $2.5\%$.

![[nonparametric-tables-by-hand.svg|860]]

That is the whole engine. Nothing was fitted, nothing was assumed about the population's shape; the tables are exact for *any* continuous symmetric population (signed-rank) or *any* pair of identical continuous populations (rank-sum). It is also why the syllabus rules out ties and observations exactly equal to $m_0$: they break the clean count.

**Why the Wilcoxon needs symmetry and the sign test does not.** Picture salaries with median $\$32{,}500$ exactly — the company's claim true. The distribution has a long right tail: the salaries above the median can be *far* above it, the ones below can only be a little below (nobody earns $-\$60{,}000$). So the ranks of the distances are not dealt fairly: the big ranks belong systematically to the "above" side even though the median is right where the claim says. The signed-rank test would see $P \gg Q$ and reject a true hypothesis. Symmetry is exactly the condition that makes "which side" and "how far" independent, and it is the only extra thing the Wilcoxon needs — not normality. The sign test never looks at "how far", so it never needs the promise.

**Why ranks beat signs — and when distances beat ranks.** The sign test throws away everything but $n$ bits, and pays for it in power: with $n = 10$ pairs it needs $9$ of $10$ to go the same way before it will speak at $5\%$ (Case 2B below has $8$ of $10$ and stays silent). The signed-rank test also *hears* that the two dissenters were the two smallest differences, and does speak. The $t$-test hears the differences themselves and, on a normal population, is the most powerful of the three — but only slightly: on normal data the Wilcoxon signed-rank test needs about $5\%$ more observations to match it, and on heavy-tailed data it can need *fewer* observations than the $t$, sometimes far fewer, because a single wild value costs it one rank, not the whole verdict.

**Where the normal approximation's mean and variance come from — coins taped to weights, and cards dealt from a deck.**

*The signed-rank picture.* Imagine the ranks $1, 2, \dots, n$ as brass weights of $1, 2, \dots, n$ grams, each with a fair coin taped to it. Toss all the coins: heads, the weight goes into the $P$ pan; tails, into the $Q$ pan. (Under $H_0$ that is exactly what symmetry does — every rank is as likely to belong to a positive difference as a negative one.) On average half of *every* weight lands in $P$, so the expected load in the $P$ pan is half the total: $E(P) = \tfrac12(1 + 2 + \dots + n) = \tfrac{n(n+1)}{4}$. The wobble comes from each coin separately: the $i$-gram weight is either all in $P$ or not at all, a $50$–$50$ swing of size $i$, whose variance is $\tfrac{i^2}{4}$ — the $\tfrac14$ is the coin's own variance, $\tfrac12 \times \tfrac12$ (a fair coin scored $0$/$1$ has variance $p(1-p) = \tfrac14$), and the weight $i$ scales it by $i^2$: a coin that pays $0$ or $i$ has mean $\tfrac i2$ and standard deviation $\tfrac i2$. Independent coins add their variances: $\operatorname{Var}(P) = \tfrac14(1^2 + 2^2 + \dots + n^2) = \tfrac{n(n+1)(2n+1)}{24}$ — the last step is the standard result $\sum_{r=1}^{n} r^2 = \tfrac16 n(n+1)(2n+1)$ (printed on MF19; derived by telescoping $(2r+1)^3 - (2r-1)^3 = 24r^2 + 2$ in [[Summation of Series]]), just as $E(P)$ used $\sum r = \tfrac12 n(n+1)$. Because $P$ is a sum of many independent bounded pieces, [[Normal Distribution]] takes over by the central limit theorem — in practice by $n \approx 20$, which is exactly where the MF19 table stops and the normal approximation begins. (And $P + Q$ is always the whole set of weights, $\tfrac12 n(n+1)$, so $Q$ has the same mean and variance, mirrored.)

*The rank-sum picture.* Now imagine a deck of $N = m + n$ cards numbered $1$ to $N$, and deal $m$ of them to the smaller sample. Under $H_0$ every hand is equally likely — that is what "identical populations" does to the ranks. One card, drawn at random, is on average the middle card, $\tfrac{N+1}{2}$; a hand of $m$ cards therefore averages $E(R_m) = \tfrac{m(N+1)}{2}$. One card's spread is $\tfrac{N^2 - 1}{12}$ — the variance of a fair $N$-sided die, and you can check it on the die you know: $N = 6$ gives $\tfrac{35}{12}$, the textbook variance of a fair die. If the $m$ cards were drawn *with* replacement they would be independent and the hand's variance would be $m$ times that; dealt *without* replacement, once a high card is in your hand it cannot come again, so the hand is a little less spread — by the finite-population factor $\tfrac{N-m}{N-1}$. Multiply out: $\operatorname{Var}(R_m) = m \cdot \tfrac{(N-1)(N+1)}{12} \cdot \tfrac{N-m}{N-1} = \tfrac{mn(m+n+1)}{12}$.

Both means and both variances are printed on MF19; the $\pm\tfrac12$ continuity correction is not, and it is a marked step — the statistics are whole numbers, and the smooth curve is being asked to price a whole-number tail.

## The three engines — each with the real cases it exists for

The five-step ritual of [[Hypothesis Tests]] does not change — **state** $H_0, H_1$ (about the **population median**, or the identity of the populations); **read** the tail from the claim; **compute** the statistic; **compare** with the table or the normal approximation; **conclude in context** with a level of uncertainty in the language. What changes is the statistic and the direction of the comparison. Each engine below is stated in a few lines and then run on real Paper 4 questions, worked with the mark-scheme values.

### Engine 1 — the sign test: which side of the median?

**The tool.**
1. $H_0$: population median $= m_0$; $H_1$: $\neq$, $>$ or $<$ as the claim says. (Paired data: median of the differences $= 0$.)
2. Count the observations above $m_0$ (or positive differences): $S$. Under $H_0$, $S \sim B(n, \tfrac12)$. (An observation exactly equal to $m_0$ — a zero difference — carries no sign: drop it and test the remaining $n - 1$. The syllabus promises none will appear.)
3. Find the tail probability of a result at least as extreme as $S$ — for a two-tailed test compare the *one-tail* probability with $\tfrac{\alpha}{2}$ (or double it and compare with $\alpha$).
4. Large $n$: $S \approx N(\tfrac n2, \tfrac n4)$ with continuity correction.
5. Compare; conclude in context.

**Why this engine, in the examiner's words.** Whenever the data are visibly skewed or carry an outlier — and the question asks *"why might a Wilcoxon signed-rank test not be appropriate?"* — the marked answer is *the population may not be symmetric*, and the sign test is what remains.

**Case 1A — two-tailed, and the outlier that disqualifies the Wilcoxon: 9231/42 November 2025 Q1.**

> A large company claims the median salary of its employees is $\$32{,}500$. Fifteen randomly selected salaries (in dollars): 18 750, 30 500, 125 000, 42 500, 25 000, 26 000, 52 500, 23 000, 27 500, 19 500, 25 500, 33 000, 30 000, 21 500, 29 000.
> **(a)** Explain why a Wilcoxon signed-rank test may not be appropriate here. **[1]** **(b)** Carry out a sign test at the 10% level to investigate the claim. **[5]**

**(a)** The sample has an outlier ($125\,000$) and is skewed to the right, suggesting the population of salaries is **not symmetric** — the Wilcoxon signed-rank test is valid only for symmetric distributions. *(In context, one sentence: B1.)*

**(b)** *Why this engine.* One sample, one hypothesised median, a population that cannot be assumed symmetric: the sign test is the only test left standing. The claim is "the median **is** $32\,500$", so the test is two-tailed.

$H_0$: population median $= 32\,500$; $H_1$: population median $\neq 32\,500$.

*Tool: count the signs.* Above $32\,500$: $125\,000,\ 42\,500,\ 52\,500,\ 33\,000$ — four; below: eleven. Test statistic $S = 4$ (or $11$).

*Tool: the binomial tail, [[Discrete Random Variables]].* $S \sim B(15, \tfrac12)$, so every one of the $2^{15}$ sign patterns is equally likely and $P(S \le 4)$ just counts the patterns with at most four "above": $P(S \le 4) = \dfrac{\binom{15}{0} + \binom{15}{1} + \binom{15}{2} + \binom{15}{3} + \binom{15}{4}}{2^{15}} = \dfrac{1 + 15 + 105 + 455 + 1365}{32\,768} = 0.0592$. (A salary exactly equal to $32\,500$ would carry no sign; the convention drops it and tests the remaining $14$ — the syllabus promises it will not arise.)

*Table read — none: compare the one-tail probability with half the level.* $0.0592 > 0.05$ (equivalently the two-tailed $p = 0.118 > 0.10$): do **not** reject $H_0$. Insufficient evidence at 10% that the median salary is not $\$32{,}500$. (The normal route earns the same marks: $z = \dfrac{4.5 - 7.5}{\sqrt{3.75}} = -1.549$ against $\pm 1.645$.)

> [!info] Why a *two*-tailed test is settled with a *one*-tail number — and what a stricter level would do
> "Two-tailed" means the surprise could have come on either side: four-or-fewer above is exactly as surprising as four-or-fewer *below*, and the total surprise is both tails. Because $B(15, \tfrac12)$ is symmetric, the two tails are equal — $P(S \le 4) = P(S \ge 11) = 0.0592$ — so "$2 \times 0.0592$ against $10\%$" and "$0.0592$ against $5\%$" are the same comparison, and the scheme accepts either.
> A stricter level only makes rejection *harder*: at 5% two-tailed the bar is $0.025$ and the verdict is the same, more comfortably. It is the *looser* direction that flips — at 15% the bar is $0.075$, and this very sample would reject. That is not a paradox; it is what a significance level *is*: the amount of coincidence you are willing to call "not a coincidence".

Notice what happened to the outlier: it counted as one "above". A $t$-test here would have worked with $\bar x = 35\,283$ — against $28\,875$ for the other fourteen employees, so one salary moved the mean by more than $\$6{,}000$ — and an $s$ inflated to match.

**Case 1B — one-tailed, with the normal approximation as an alternative: 9231/41 June 2026 Q1.**

> From past records the median number of items bought per customer at a village store was $8$. The manager believes it has increased. A random sample of $15$ customers buys $6, 6, 7, 9, 9, 10, 15, 17, 17, 23, 26, 34, 40, 56, 74$ items.
> **(a)** Suggest why a Wilcoxon signed-rank test might not be appropriate. **[1]** **(b)** Use a sign test at the 5% level to investigate the manager's belief. **[6]**

**(a)** The data are strongly skewed (a tail out to $74$), so the population may not be symmetric. *(The scheme also accepts: there are tied values, which the Wilcoxon ranking cannot handle.)*

**(b)** *Why this engine.* One sample against a known previous median, skewed data, and a directional belief ("has increased"): sign test, one-tailed.

$H_0$: population median $= 8$; $H_1$: population median $> 8$.

One-tailed means the test only listens in the *claimed* direction: a lopsided count *above* $8$ is evidence, a lopsided count *below* $8$ is not — had $12$ of the $15$ customers bought fewer than $8$ items, the conclusion would still be "insufficient evidence that the median has increased", because the test does not switch sides mid-question. Two-tailed (Case 1A) listens on both sides: reject as soon as it seems to have moved at all.

*Tool: count.* Below $8$: $6, 6, 7$ — three; above: twelve. If the median were still $8$, three-or-fewer below is the extreme outcome to price.

*Tool: the binomial tail.* $P(S \le 3) = \dfrac{\binom{15}{0} + \binom{15}{1} + \binom{15}{2} + \binom{15}{3}}{2^{15}} = \dfrac{1 + 15 + 105 + 455}{32\,768} = 0.0176$.

$0.0176 < 0.05$: reject $H_0$. Sufficient evidence at 5% that the median number of items has increased. (Say it exactly like that. A test never learns that the median *is* $12$ or *is not* $8$; it learns that this sample would be a $1.8\%$ coincidence if the median were still $8$, and $1.8\%$ is below the coincidence you agreed to tolerate. "Sufficient evidence that…" is the honest sentence, and the words that lose the mark — *prove*, *accept*, *the median is now* — all claim more than the test knows.) (Normal route: $z = \dfrac{3.5 - 7.5}{\sqrt{3.75}} = -2.07$, beyond $-1.645$ — the $0.5$ is the continuity correction, and without it $z = -2.32$ still gets the M1 but not the A1.)

---

### Engine 2 — the Wilcoxon signed-rank test: which side, and how far in rank

**The tool.**
1. $H_0$: population median $= m_0$ (paired: median difference $= 0$); $H_1$ from the claim.
2. Differences $d_i = x_i - m_0$ (paired: $x_i - y_i$). Rank $\lvert d_i \rvert$ from $1$ (smallest) to $n$ (largest), *ignoring sign*.
3. $P$ = sum of ranks of positive $d$; $Q$ = sum of ranks of negative $d$. Check $P + Q = \tfrac12 n(n+1)$. $T = \min(P, Q)$.
4. $n \le 20$: MF19 row $n$, column by level and tails; **reject if $T \le$ table value.** $n > 20$: $P$ (or $Q$) $\approx N\!\big(\tfrac{n(n+1)}{4}, \tfrac{n(n+1)(2n+1)}{24}\big)$ with continuity correction.
5. Conclude in context.

**Why this engine, in the examiner's words.** Paired or single-sample data whose population **cannot be assumed normal** — the *"why might a paired $t$-test be inappropriate?"* B1 is *the population of differences may not be normally distributed* — but which *can* be taken as symmetric. It hears the sizes of the differences in rank order, so it is sharper than the sign test.

**Case 2A — matched pairs, two-tailed, and why not the $t$: 9231/43 June 2026 Q2.**

> Two teachers independently mark the same ten scripts:
> Teacher 1: $42, 73, 53, 21, 61, 83, 63, 37, 46, 55$; Teacher 2: $46, 81, 68, 24, 60, 81, 68, 30, 57, 61$.
> **(a)** Give a reason why a Wilcoxon matched-pairs signed-rank test might be more appropriate than a paired-sample $t$-test. **[1]** **(b)** Carry out the test at the 5% level to investigate whether, on average, the two teachers' marks differ. **[7]**

**(a)** The population of **differences** may not be normally distributed. *(Not "the marks may not be normal", and not "the mean may not be normal" — the scheme rejects both.)*

**(b)** *Why this engine.* Each script is marked twice — **paired** by script, so the natural data are the ten differences. No normality is claimed, but marks on the same script differing by a few points either way is a symmetric-enough situation for the ranks to be dealt fairly. "Differ" is two-tailed.

$H_0$: the population median difference is $0$; $H_1$: it is not $0$.

*Tool: differences, then ranks of $\lvert d \rvert$.* Teacher 2 $-$ Teacher 1: $4, 8, 15, 3, -1, -2, 5, -7, 11, 6$. **Now rank them yourself before reading on** — write the ten sizes in order, number them $1$ to $10$, put each sign back — and check your $P$, $Q$ and $T$ against the next line. If they match, you own the procedure; if not, the mismatch is worth more than the answer.

*Tool: $P$, $Q$, $T$.* The negatives $-1, -2, -7$ are the smallest, second-smallest and seventh-smallest sizes, so $Q = 1 + 2 + 7 = 10$; $P = 55 - 10 = 45$ (check: $\tfrac12 \cdot 10 \cdot 11 = 55$); $T = 10$.

**Table read:** signed-rank table, row $n = 10$, column *two-tailed $0.05$* → **$8$**. $T = 10 > 8$: do **not** reject $H_0$. Insufficient evidence at 5% that, on average, the two teachers' marks differ. (Note the scheme's own warning: *do not accept "no evidence"* — there is some; it is insufficient.)

*What the $8$ means.* If the two teachers really were interchangeable, the ten ranks would fall $+$ or $-$ by fair coins, and the smaller of the two pans would usually be fairly heavy — near $27$, half of $55$. It comes out at $8$ or less in only $5\%$ of those coin-tosses (both tails counted). So a $T$ of $8$ or below is the surprise; a $T$ of $10$ is *close* to surprising, but not there — the small pan still holds too much for the split to be called lopsided. And notice how close: at **10%** two-tailed the same row reads $10$, and this very $T = 10$ would reject. Exam levels are chosen to sit on that edge on purpose — the question is testing whether you read the right column, not whether you can guess the verdict.

**Case 2B — matched pairs, one-tailed, and the sign test that disagrees: 9231/41 June 2025 Q5.**

> Ten children each complete two jigsaws — a seaside picture and a cartoon — and a researcher believes children finish the cartoon faster. Times (s):
> Seaside: $182, 130, 193, 181, 192, 204, 184, 192, 180, 189$; Cartoon: $161, 111, 195, 159, 202, 200, 168, 165, 145, 160$.
> **(a)** Carry out a Wilcoxon matched-pairs signed-rank test at the 5% level. **[6]** **(b)** Show that a paired-sample sign test at 5% gives the opposite conclusion. **[3]**

**(a)** *Why this engine.* Paired by child; the claim is directional (cartoon faster → seaside $-$ cartoon $> 0$), so one-tailed.

$H_0$: median difference (seaside $-$ cartoon) $= 0$; $H_1$: median difference $> 0$.

*Tool: differences and signed ranks.* $d = 21, 19, -2, 22, -10, 4, 16, 27, 35, 29$; sizes ranked $2 \to 1,\ 4 \to 2,\ 10 \to 3,\ 16 \to 4,\ 19 \to 5,\ 21 \to 6,\ 22 \to 7,\ 27 \to 8,\ 29 \to 9,\ 35 \to 10$; signed ranks $6, 5, -1, 7, -3, 2, 4, 8, 10, 9$.

$Q = 1 + 3 = 4$, $P = 51$, $T = 4$. **Table read:** row $10$, column *one-tailed $0.05$* → **$10$**. $4 \le 10$: reject $H_0$. Sufficient evidence at 5% that children complete the cartoon puzzle more quickly.

*What if $P$ had been the tiny one?* Then most children were *slower* on the cartoon — the opposite of the researcher's belief. In a **one-tailed** test the small pan has to be on the side $H_1$ predicts (here the negatives, $Q$): a tiny $P$ is a lopsided split in the *wrong* direction, which is evidence *against* $H_1$, and you do not reject — write "the sample contradicts the direction of the belief; insufficient evidence that the cartoon is faster", not "$T$ is small so reject". Only in a **two-tailed** test does either pan count, which is why $T = \min(P, Q)$ is the statistic and the table's two-tailed row prices both sides at once.

**(b)** *Tool: the sign count.* Eight of the ten differences are positive. $S \sim B(10, \tfrac12)$: $P(S \ge 8) = \dfrac{45 + 10 + 1}{1024} = 0.0547 > 0.05$: do **not** reject $H_0$ — the opposite conclusion.

![[nonparametric-jigsaw-two-verdicts.svg|860]]

*Read the two verdicts together.* The sign test saw $8$ against $2$ and found it not quite rare enough. The signed-rank test saw that the two dissenting children were the ones whose times differed by $2$ s and $10$ s — the smallest and third-smallest gaps of all — while the eight who agreed with the researcher did so by $16$–$35$ s. Same data; the second test simply listened to more of it. This is the power argument in one picture, and it is why the syllabus asks you to use the Wilcoxon *"as appropriate"*: when symmetry can be assumed, it is the better instrument.

**Case 2C — beyond the table: the normal approximation, run backwards: 9231/41 November 2025 Q4.**

> A researcher believes the median $m$ of a population has changed from its known previous value $m_0$. She takes a random sample of size $28$, ranks the data and computes $T$ for a Wilcoxon signed-rank test. At the 1% level the conclusion is that there is not sufficient evidence to support her belief. Using a normal approximation, find the least possible value of $T$. **[5]**

*Why this engine, and why the normal.* Single sample against $m_0$, Wilcoxon named; $n = 28$ is off the table ($n \le 20$), so the approximation is compulsory. "Changed" is two-tailed at 1%: $z$-boundary $\pm 2.576$.

*Tool: MF19's mean and variance — the coins-on-weights picture with $n = 28$.* The ranks $1$ to $28$ total $\tfrac{28 \cdot 29}{2} = 406$; half of that is the expected load in either pan, $\mu = \tfrac{28 \cdot 29}{4} = 203$. The squares $1^2 + \dots + 28^2 = \tfrac{28 \cdot 29 \cdot 57}{6} = 7714$ (the standard $\sum r^2 = \tfrac16 n(n+1)(2n+1)$ from [[Summation of Series]] — check it by adding the squares if you doubt it); a quarter of that (the coin's $\tfrac12 \times \tfrac12$) is the variance, $\sigma^2 = \tfrac{28 \cdot 29 \cdot 57}{24} = 1928.5$, so $\sigma = 43.91$. Both formulas are printed on MF19 under the table; the numbers are yours to plug.

*Tool: not rejecting means the small tail is not small enough — with continuity correction on the side of $T$.* $T$ is the *smaller* rank sum, so its tail is the lower one; "not rejected" means $P(\text{sum} \le T) > 0.005$. And the $+0.5$: a rank sum is a whole number, so "$\le T$" means the histogram bar at $T$ and everything left of it — and the bar at $T$ stretches from $T - \tfrac12$ to $T + \tfrac12$. The smooth curve has to be read up to the bar's *right* edge, $T + 0.5$, to cover it; read to $T$ itself and you have thrown away half a bar. So:
$$\frac{T + 0.5 - 203}{43.91} > -2.576 \;\Longrightarrow\; T > 203 - 0.5 - 113.1 = 89.4 .$$
Least integer $T = \mathbf{90}$. (Dropping the $+0.5$, or using $-0.5$, keeps the method mark and loses the final answer.)

---

### Engine 3 — the Wilcoxon rank-sum test: are these two samples from the same population?

**The tool.** Two **independent** samples of sizes $m \le n$ (label the smaller one $m$).
1. $H_0$: the two populations are identical (equal population medians); $H_1$: one lies above the other, or they differ.
2. Pool the $m + n$ values and rank them $1$ (smallest) to $m + n$. $R_m$ = sum of the ranks belonging to the smaller sample.
3. $W = \min\!\big(R_m,\ m(m+n+1) - R_m\big)$ — MF19 prints this rule (*"W is the smaller of $R_m$ and $m(n+m+1) - R_m$"*) but not the reason, which is one line: rank the pooled data **backwards** (largest $= 1$) and every rank $r$ becomes $N + 1 - r$, where $N = m + n$; the smaller sample's $m$ ranks then add to $m(N+1) - R_m = m(m+n+1) - R_m$. So the second term is simply $R_m$ under the reversed ranking, and $W$ is small whenever the smaller sample sits at *either* end of the pool. (Check on the reaction times below: backwards, the over-50 ranks $5, 8, 9, 11, 13, 14$ become $10, 7, 6, 4, 2, 1$, which add to $30 = 6 \times 15 - 60$.)
4. $m \le n \le 10$: MF19 rank-sum table, entry $(m, n)$, column by level and tails; **reject if $W \le$ table value.** Larger: $R_m \approx N\!\big(\tfrac{m(m+n+1)}{2}, \tfrac{mn(m+n+1)}{12}\big)$ with continuity correction.
5. Conclude in context.

**Why this engine, in the examiner's words.** Two *separate* groups — different people, not the same people twice — with no normality on offer: the rank-sum test. If the same subjects are measured twice, it is the wrong tool (pairing is information the rank-sum test throws away).

**The case — 9231/43 June 2025 Q4.**

> A researcher claims older people take longer to react to a sudden loud noise. Reaction times (ms) — six people over 50: $198, 212, 217, 229, 235, 242$; eight people under 25: $178, 181, 183, 192, 203, 209, 223, 231$. Carry out a Wilcoxon rank-sum test at the 5% level. **[8]**

*Why this engine.* Two independent groups of different people, unequal sizes, no distribution assumed, a directional claim: rank-sum, one-tailed. The smaller sample is the over-50s, $m = 6$, $n = 8$.

$H_0$: the population median reaction times of over-50s and under-25s are equal; $H_1$: the over-50 median is greater. *(The B1 needs the word **population** — "the medians are equal" alone is B0.)*

*Tool: pool and rank all fourteen.* Sorted: $178_1, 181_2, 183_3, 192_4, \mathbf{198_5}, 203_6, 209_7, \mathbf{212_8}, \mathbf{217_9}, 223_{10}, \mathbf{229_{11}}, 231_{12}, \mathbf{235_{13}}, \mathbf{242_{14}}$. Over-50 ranks: $5, 8, 9, 11, 13, 14$ → $R_6 = 60$.

*Tool: $W$.* $m(m+n+1) - R_m = 6 \times 15 - 60 = 30$; $W = \min(60, 30) = 30$.

**Table read:** rank-sum table, block $m = 6$, row $n = 8$, column *one-tailed $0.05$* → **$31$**. $30 \le 31$: reject $H_0$. Sufficient evidence at 5% that older people take longer to react. (Knife-edge: one rank swapped and the verdict flips — which is exactly what "5%" buys you.)

Watch the null distribution assemble itself: the fourteen ranks dealt at random to "over 50" a thousand times, and then all $3003$ possible hands counted — $89$ of them reach $60$ or more.

![[wilcoxon-rank-shuffle.mp4]]

*If the samples were larger* — say $m = 12$, $n = 15$, off the table — the same $R_m$ would be standardised: $z = \dfrac{R_m \pm 0.5 - \tfrac{12 \cdot 28}{2}}{\sqrt{12 \cdot 15 \cdot 28 / 12}} = \dfrac{R_m \pm 0.5 - 168}{\sqrt{420}}$, with the $\mp 0.5$ chosen toward the centre, and compared with $1.645$ / $1.96$ as the tails demand.

## Choosing the engine

First an honest note about the exam. **The question names the test for you** — every recent Paper 4 question says *carry out a Wilcoxon rank-sum test*, *use a sign test*, *carry out a Wilcoxon matched-pairs signed-rank test* — so you are never asked to pick the engine cold. What the paper *does* examine about choosing is the one-mark justification: *why might a Wilcoxon signed-rank test not be appropriate here?*, *why might it be more appropriate than a paired $t$-test?*, *show that a sign test gives the opposite conclusion*. The table below is for those one-markers, and for the world outside the paper, where nobody names the test for you.

| The design | The population can be taken as… | Engine | Reject when |
|---|---|---|---|
| one sample vs a hypothesised median $m_0$ | anything (skewed, outliers) | **sign test** on the signs of $x - m_0$ | binomial tail $< \alpha$ (or $\alpha/2$) |
| one sample vs $m_0$ | symmetric | **Wilcoxon signed-rank** on $\lvert x - m_0\rvert$ | $T \le$ table |
| paired data (same subjects twice) | differences skewed | **paired-sample sign test** | binomial tail |
| paired data | differences symmetric | **Wilcoxon matched-pairs signed-rank** | $T \le$ table |
| paired data | differences normal | paired $t$ ([[t-Tests]]) | $\lvert t \rvert >$ table |
| two independent samples | anything, identical shape under $H_0$ | **Wilcoxon rank-sum** | $W \le$ table |
| two independent samples | both normal | two-sample $t$ ([[t-Tests]]) | $\lvert t \rvert >$ table |

Two questions decide it: **is the data paired or two separate groups?** and **what may I assume about the population — nothing, symmetry, or normality?** Then the housekeeping that carries marks: is $n$ (or $m, n$) inside the table's range, and if not, have I applied the continuity correction toward the centre?

> [!tip] The three "why not…?" sentences, in the words the scheme pays for
> - *Why not a (paired) $t$-test?* — **The population (of differences) may not be normally distributed.**
> - *Why not a Wilcoxon signed-rank test?* — **The data are skewed / have an outlier, suggesting the population may not be symmetric.** (Or: there are ties, which the ranking cannot handle.)
> - *Why is the sign test weaker?* — **It uses only the signs and ignores the sizes of the differences.**

## Where the non-parametric tests meet the world

- **Medicine's default two-group test.** Pain scores $0$–$10$, disease-severity grades, "how much better do you feel" on a five-point scale — these are *ordinal*: rank $7$ is above rank $5$, but nobody believes the gap between them is a fixed number of anything. Ranks are the only honest arithmetic, and the Wilcoxon rank-sum test (called the **Mann–Whitney $U$ test** in every clinical paper — the same test with $U = R_m - \tfrac12 m(m+1)$) is the workhorse of comparing two treatment groups on such scales. Survival times, hospital stays and viral loads are so skewed that the rank-sum test is preferred there too.
- **Comparing two algorithms across many datasets.** Machine-learning papers that claim "our model beats the baseline" on twenty benchmark datasets face exactly Case 2B: twenty paired scores, no reason to think the differences are normal, and a couple of datasets where the improvement is huge. The recommended test in the field's standard methodology paper is the **Wilcoxon signed-rank test** over the datasets, precisely because a $t$-test would let one dataset with a large gain carry the verdict, and a sign test would waste the sizes.
- **A/B tests on money.** Revenue per user, time on site, order value — right-skewed, zero-heavy, with occasional whales. Product-analytics teams test *medians* with sign and rank tests (and their bootstrap cousins) because a $t$-test on the mean is a test on whichever whale showed up this week.
- **Robustness as a design principle.** One corrupted sensor reading, one mistyped salary, one child who stopped to tie a shoelace: in a rank test that observation moves by *one rank* at most, and the verdict barely notices. In a $t$-test it can *become* the verdict. Every branch of statistics that meets messy data — environmental monitoring, psychology, economics of income — leans on ranks for exactly this reason.

## Common Misconceptions (Teaching Notes)

### 1. Hypotheses about the mean

"$H_0: \mu = 32\,500$" in a sign or Wilcoxon test loses the B1 outright.

**Fix:** these tests are about the **population median** $m$ (or the median difference), and the scheme wants the word *population*. Write "population median" every time; never "average".

### 2. $T$ is not the smaller sum, or $W$ is just $R_m$

Reporting $T = P = 51$ in Case 2B, or $W = R_6 = 60$ in the rank-sum case, and comparing that with the table.

**Fix:** $T = \min(P, Q)$, and $W = \min\!\big(R_m,\ m(m+n+1) - R_m\big)$. Compute both, take the smaller. Check $P + Q = \tfrac12 n(n+1)$ before you do.

### 3. Rejecting when $T$ is *large*

Habit from every other table: "$10 > 8$, so reject".

**Fix:** the Wilcoxon tables print the largest statistic that *rejects*; small is significant. $T \le$ table → reject; $T >$ table → do not. Say the sentence "a tiny minority rank sum is the surprise" before you compare.

### 4. Ranking the wrong thing

Ranking the raw $x$ values instead of $\lvert x - m_0 \rvert$ in a signed-rank test; ranking each sample separately instead of the pooled data in a rank-sum test; ranking the *signed* differences so the negatives come first.

**Fix:** signed-rank = rank the **sizes** of the differences, then reattach the signs. Rank-sum = one ranking of **all** $m + n$ values together.

### 5. Reading the wrong tails row

Using the two-tailed $0.05$ column ($n = 10$: $8$) for a one-tailed 5% test (correct: $10$).

**Fix:** the tables carry both a one-tailed and a two-tailed heading over each column. Find the level in the row that matches your $H_1$.

### 6. "The Wilcoxon needs normality" / "the sign test needs symmetry"

Both wrong, in opposite directions.

**Fix:** the sign test needs nothing beyond a well-defined median; the Wilcoxon tests need **symmetry** (signed-rank) or **identical shapes** (rank-sum) — never normality. The $t$-test is the one that needs normality. Three tests, three assumptions, one ladder.

### 7. Continuity correction the wrong way

$T - 0.5$ instead of $T + 0.5$ in Case 2C.

**Fix:** you are approximating $P(\text{integer statistic} \le t)$ by a continuous curve, so extend the region to $t + \tfrac12$; for $P(\ge t)$ use $t - \tfrac12$. Always toward the centre from the tail you are pricing.

## Exam Notes

### Cambridge 9231 — Further Probability & Statistics, §4.4

Four learning objectives; a non-parametric question appears on almost every Paper 4, typically 6–8 marks, often paired with a one-mark *"why is the other test inappropriate?"*:

- **Understand the idea of a non-parametric test and when it is useful** — *"when sampling from a population which cannot be assumed to be normally distributed"*; the B1 answers are the three sentences in the tip above. Note that the questions always **name** the test to run — the choosing is examined only through these one-mark *why (not) this test* parts, never as an open choice.
- **The basis of the sign test, the Wilcoxon signed-rank test and the Wilcoxon rank-sum test** — *"including knowledge that Wilcoxon tests are valid only for symmetrical distributions"*: expect a part asking you to say why (skew, outliers) — in context.
- **Single-sample sign test and single-sample Wilcoxon signed-rank test for a population median**, including normal approximations where appropriate; *"questions will not involve tied ranks or observations equal to the population median."*
- **Paired-sample sign test, Wilcoxon matched-pairs signed-rank test and Wilcoxon rank-sum test** for identity of populations, including normal approximations; *"no tied ranks or zero-difference pairs."*
- Mark-scheme habits: hypotheses must say **population median** (B0 for mean, B0 for "median" without "population"); the ranks M1 is awarded for *an attempt* — reversed rankings score it, so write your ranking out; the critical value is a separate B1 (row **and** tails); the comparison M1 needs your $T$ or $W$ *from rank sums only*; the final A1 wants context and *uncertainty* language — never "prove", and not "no evidence". Case 2C's shape (given the conclusion, find the least/greatest statistic) recurs.
- MF19 prints both tables ($T$ for $6 \le n \le 20$; $W$ for $m \le n \le 10$) and both normal approximations; the *rules for computing* $T$ and $W$ are printed above the tables, but the ranking procedure and the continuity correction are yours to know.

### Where it is *not* examined

Among the boards this vault covers, **9231 is the only one that examines these tests** — verified against the syllabus PDFs: **Cambridge 9709** never asks them (its formula booklet is the shared MF19, so the Wilcoxon tables are printed there — do not be misled); **Edexcel IAL** has no sign or Wilcoxon test (its formula book's "non-parametric tests" heading holds only the $\chi^2$ statistic, and S3's only rank method is Spearman's correlation); **OxAQA 9660**, **AP Statistics**, **IB AA / AI**, **0580** and **0606** have none of it. Outside the vault's boards, the UK OCR MEI Further Statistics option carries both Wilcoxon tests, so British textbooks are a good second source.

### Beyond high school — University

The rank-sum test is the same test as the **Mann–Whitney $U$** ($U = R_m - \tfrac12 m(m+1)$ counts how many of the $mn$ cross-pairs have the smaller sample's member on top); it generalises to $k$ groups as the **Kruskal–Wallis** test (the rank version of one-way ANOVA), and the signed-rank test to $k$ related samples as **Friedman's** test. All of them are special cases of **permutation tests** — "if $H_0$ were true, the labels are exchangeable, so shuffle them and see how extreme the real labelling is" — which computers now run directly on the raw data, no ranks needed. And the **Hodges–Lehmann estimator** (the median of the pairwise averages $\tfrac{x_i + x_j}{2}$) turns the signed-rank test into a confidence interval for the median, robust in exactly the way the test is.

> [!info] Beyond syllabus — how much do you pay for throwing away the distances?
> A precise answer exists: on *normal* data, the Wilcoxon signed-rank test needs about $\tfrac{\pi}{3} \approx 1.047$ times as many observations as the $t$-test to reach the same power (an *asymptotic relative efficiency* of $3/\pi \approx 0.955$) — a 5% tax. On heavier-tailed data the ratio flips: the Wilcoxon can need markedly *fewer*, and there is no data shape on which its efficiency against the $t$ falls below $0.864$. The sign test pays more — $2/\pi \approx 0.64$ against the $t$ on normal data — but it is the only one of the three whose licence can never be revoked. That is the trade the ladder above makes precise: robustness bought cheaply, at the price of a little power when the world happens to be normal.

## Connections

- **Parent:** [[Hypothesis Tests]] — the ritual, the tail from the claim, the binomial test that the sign test *is*.
- **What these replace:** [[t-Tests]] — the paired and two-sample $t$; the *"why inappropriate → non-parametric"* sting there is answered here, and the ladder sign → rank → distance is the same data heard three ways.
- **The paper's other engine:** [[Chi-Squared Tests]] — the third kind of test on this paper, also distribution-free in its own way (it tests a shape rather than assuming one); Fisher's exact test there is a permutation test in the same family as the rank-sum.
- **The counting underneath:** [[Discrete Random Variables]] (the binomial tail of the sign test), [[Permutations and Combinations]] ($2^n$ sign patterns; $\binom{m+n}{m}$ hands), [[Normal Distribution]] (the large-sample approximations and the continuity correction).
- **The median:** [[Averages and Spread]] — why the median resists an outlier that drags the mean; that resistance is what these tests inherit.
- **For 9231 students:** [[MF19 Reference (9231)]] — both Wilcoxon tables and both normal approximations are printed; the ranking procedure, the rule for $T$ and $W$, and the continuity correction are the parts to carry.
- **Story partner:** [[Stories/The Lady Tasting Tea|The Lady Tasting Tea]] — the first permutation test: eight cups, seventy arrangements, *only a perfect score will do*.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $S \sim B(n, \tfrac12)$ | `S \sim B(n, \tfrac12)` | sign-test statistic |
| $T = \min(P, Q)$ | `T = \min(P, Q)` | signed-rank statistic |
| $W = \min\!\big(R_m,\ m(m+n+1)-R_m\big)$ | `W = \min\!\big(R_m,\ m(m+n+1)-R_m\big)` | rank-sum statistic |
| $\tfrac{n(n+1)}{4},\ \tfrac{n(n+1)(2n+1)}{24}$ | `\tfrac{n(n+1)}{4},\ \tfrac{n(n+1)(2n+1)}{24}` | mean, variance of $P$ or $Q$ |
| $\tfrac{m(m+n+1)}{2},\ \tfrac{mn(m+n+1)}{12}$ | `\tfrac{m(m+n+1)}{2},\ \tfrac{mn(m+n+1)}{12}` | mean, variance of $R_m$ |
| $\lvert d_i \rvert$ | `\lvert d_i \rvert` | size of a difference (use `\lvert` in tables) |
| $\binom{m+n}{m}$ | `\binom{m+n}{m}` | number of equally likely hands |
