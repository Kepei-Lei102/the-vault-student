---
chinese: 积分夹逼 (jīfēn jiābī)
prerequisites:
  - "[[Integration]]"
  - "[[Summation of Series]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/calculus
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/AP
  - syllabus/9231-2-4
  - type/technique
  - notation/integral
  - misconception/endpoint-direction
---

# Bounding Sums with Integrals 积分夹逼

> *A staircase and a ramp climb the same hill. The staircase is the sum — discrete, one block per step; the ramp is the integral — smooth, effortless to measure. Slide the staircase half a step and it swaps from hugging the ramp's underside to riding on top: the sum is **trapped between two integrals**, and the integral between two sums. When one side is easy and the other impossible, the trap is the answer.*

## The picture, and the two directions

Take $f$ **increasing** on the interval, and rectangles of unit width sitting on $[r-1, r]$-style bases. A rectangle whose height is the *left* endpoint's value fits **under** the curve; height from the *right* endpoint pokes **over** it. Summing:

$$\sum_{r=m}^{n-1} f(r) \;\leq\; \int_m^{n} f(x)\,dx \;\leq\; \sum_{r=m+1}^{n} f(r) \qquad (f \text{ increasing}).$$

For $f$ **decreasing** the two sums swap roles. That single picture is used in both directions:

- **Bound a sum by integrals** — when the sum has no closed form but the integral does (the harmonic series below).
- **Bound an integral by sums** — when the sum *can* be evaluated (via the $\sum r$, $\sum r^2$ formulas of [[Summation of Series]]) and squeezes the integral, or, with width $\to 0$, *becomes* it.

![[sum-integral-staircase.svg|760]]

### 中文锚点 (Chinese Anchor)

台阶和坡道爬同一座山。**和式是台阶**，一格一格；**积分是坡道**，好算得多。把取点从左端换成右端，台阶就从贴着坡道下面变成骑在坡道上面——于是**和被两个积分夹住**（或者反过来，积分被两个和夹住）。这就是夹逼的思想，跟你熟悉的夹逼定理是一个精神，只是夹的东西换成了"求不出来的和"。用法两个方向：和式求不动、积分好算，就用积分夹和（比如调和级数 $\sum \frac1r$ 的部分和被 $\ln$ 夹住）；和式能用 $\sum r$、$\sum r^2$ 公式算出来，就反过来用和夹积分——考题常让矩形宽度取 $\frac1n$，先把两边的和式算出来，再让 $n \to \infty$，上下界收拢到同一个数，这其实就是**定积分的定义**现场表演。方向别记反：函数**递增**时左端点矩形在曲线下方、右端点在上方；**递减**时正好交换。判断方法不是背，是画一格看一眼。

## Worked — a real Paper 2 question, both barrels

*The interval $[0, 1]$ is split into $n$ strips of width $\frac1n$, and rectangles are drawn under $y = 2x + x^2$. Let $U_n$ be the total area of the $n$ rectangles whose heights are taken at the **right-hand** end of each strip, and $L_n$ the total when the heights are taken at the **left-hand** end. (a) Show that $U_n = \frac43 + \frac{3}{2n} + \frac{1}{6n^2}$. (b) Find $L_n$ in the same form. (c) Show that $U_n - L_n \to 0$ as $n \to \infty$, and deduce the value of $\displaystyle\int_0^1 (2x + x^2)\,dx$.*

**Which rectangles are which — read it off one strip before any algebra.** The $r$-th strip runs from $x = \frac{r-1}{n}$ to $x = \frac{r}{n}$. It offers two heights: the curve's value at its *left* edge, $f\!\left(\frac{r-1}{n}\right)$, and at its *right* edge, $f\!\left(\frac{r}{n}\right)$. Because $f$ is increasing, the left-edge rectangle sits **under** the curve and the right-edge rectangle pokes **over** it — which settles, with nothing memorised, which sum is the lower bound and which the upper:

| | heights read at | the $n$ heights are | so the sum runs over | the staircase sits | and it is the |
|---|---|---|---|---|---|
| $U_n$ | the right edge, $x = \frac{r}{n}$ | $f(\tfrac1n),\ f(\tfrac2n),\ \dots,\ f(\tfrac{n}{n})$ | $r = 1$ to $n$ | **over** the curve | upper bound — the **right-hand side** of the squeeze |
| $L_n$ | the left edge, $x = \frac{r-1}{n}$ | $f(0),\ f(\tfrac1n),\ \dots,\ f(\tfrac{n-1}{n})$ | $r = 0$ to $n-1$ | **under** the curve | lower bound — the **left-hand side** |

Same heights, shifted by one: $U_n$ owns $f(1)$ at the top end, $L_n$ owns $f(0)$ at the bottom end, and every other term is shared. That one-term difference is the whole story of part (c).

**(a)** *Tool: the sum of the rectangle areas — width $\frac1n$, heights read at $x = \frac{r}{n}$ for $r = 1, \dots, n$* (the scheme's first M1 is for the *right number* of rectangles):

$$U_n = \frac1n\sum_{r=1}^{n} \left(\frac{2r}{n} + \frac{r^2}{n^2}\right) = \frac{2}{n^2}\sum_{r=1}^n r + \frac{1}{n^3}\sum_{r=1}^n r^2.$$

*Tool: the standard sums — $\sum_{r=1}^n r = \frac12 n(n+1)$ and $\sum_{r=1}^n r^2 = \frac16 n(n+1)(2n+1)$, both printed on MF19.*

$$U_n = \frac{2}{n^2}\cdot\frac{n(n+1)}{2} + \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6} = \left(1 + \frac1n\right) + \frac16\left(1 + \frac1n\right)\left(2 + \frac1n\right) = \frac43 + \frac{3}{2n} + \frac{1}{6n^2}. \qquad\blacksquare$$

**(b)** *Tool: the same sum, heights now read at $x = \frac{r}{n}$ for $r = 0, \dots, n-1$* (the scheme's M1 here is for "the correct height of the **last** rectangle", $f(\frac{n-1}{n})$ — the term students most often lose):

$$L_n = \frac1n\sum_{r=0}^{n-1} \left(\frac{2r}{n} + \frac{r^2}{n^2}\right) = \frac{2}{n^2}\sum_{r=1}^{n-1} r + \frac{1}{n^3}\sum_{r=1}^{n-1} r^2$$

— the $r = 0$ term is zero, so the sums may start at $1$; what changes is that they now **stop at $n-1$**.

*Tool: the MF19 formulas with $n-1$ in place of $n$* — $\sum_{r=1}^{n-1} r = \frac12 (n-1)n$ and $\sum_{r=1}^{n-1} r^2 = \frac16 (n-1)n(2n-1)$ (the scheme's A mark is precisely for these *correct limits*):

$$L_n = \frac{2}{n^2}\cdot\frac{(n-1)n}{2} + \frac{1}{n^3}\cdot\frac{(n-1)n(2n-1)}{6} = \left(1 - \frac1n\right) + \frac16\left(1 - \frac1n\right)\left(2 - \frac1n\right) = \frac43 - \frac{3}{2n} + \frac{1}{6n^2}.$$

Set it beside $U_n$: **$L_n$ is $U_n$ with the sign of every $\frac1n$ flipped** — the left staircase lands exactly as far below $\frac43$ as the right one lands above. And the pair brackets the integral because of the *picture*, not the algebra:

$$L_n \;\leq\; \int_0^1 (2x + x^2)\,dx \;\leq\; U_n.$$

**(c)** *Tool: subtract.* $U_n - L_n = \dfrac{3}{n} \to 0$ as $n \to \infty$. (Check it against the picture: the two staircases differ by exactly one rectangle's worth at each end, $\frac1n\,[f(1) - f(0)] = \frac1n \cdot 3$ — if your difference is anything else, a limit is wrong.) Both bounds therefore close onto the same number, $\frac43$, and the integral trapped between them **is** $\frac43$ — which the antiderivative $\left[x^2 + \tfrac13 x^3\right]_0^1$ confirms in one line, and that is the point: the squeeze computed an integral using nothing but rectangle areas and the $\sum r$ formulas. You have just watched the definition of the definite integral operate.

## The other direction — the harmonic series trapped

The syllabus's own example: bound $\displaystyle\sum_{r=1}^{n} \frac1r$, which has no closed form. $f(x) = \frac1x$ is *decreasing*, so on each base $[r, r+1]$ the rectangle of height $\frac1r$ (left endpoint) covers the curve:

$$\sum_{r=1}^{n} \frac1r \;\geq\; \int_1^{n+1} \frac{dx}{x} = \ln(n+1), \qquad\text{and, shifting one step,}\qquad \sum_{r=1}^{n} \frac1r \;\leq\; 1 + \int_1^{n} \frac{dx}{x} = 1 + \ln n.$$

Two payoffs, one small and one famous. The exam one: numerical bounds on an unsummable sum ("show that the sum of the first million reciprocals lies between $13.8$ and $14.9$"). The famous one: since $\ln(n+1) \to \infty$, **the harmonic series diverges** — it grows without bound, but only like $\ln n$: glacially. The trap doesn't just bound the sum; it reveals the sum's whole personality.

> [!info] Beyond syllabus — $\ln(n!)$ and why sorting costs $n \log n$
> Trap $\ln(n!) = \sum_{r=1}^n \ln r$ (increasing $f$) between $\int_1^n \ln x\, dx$ and its shifted twin, and out falls $\ln(n!) \approx n\ln n - n$ — the heart of **Stirling's approximation**. Now the payoff: a comparison sort must distinguish all $n!$ possible orderings, and each comparison answers one yes/no question, so at least $\log_2(n!)$ comparisons are unavoidable — and by this trap $\log_2(n!) = \Theta(n\log n)$. The "comparison-sort floor" that [[Big-O Notation]] tables and [[Sorting]] lives under is *these rectangles, run on logarithms*. One picture, from FP2 to the reason your database index exists.

## The width-to-zero limit — sums that become integrals

The rectangles' width need not be $1$; let it be $\frac1n$ and shrink. The syllabus's example:

$$\frac1n\sum_{r=1}^{n} \left(1 + \frac{r}{n}\right)^{-1} \;\longrightarrow\; \int_0^1 \frac{dx}{1+x} = \ln 2 \qquad (n \to \infty),$$

because the left side *is* the right-endpoint rectangle estimate of that integral, and the sandwich gap ($\leq$ width × total rise) vanishes. Exam recognition skill: a limit of the form $\frac1n\sum f\left(\frac{r}{n}\right)$ **is an integral in disguise** — read off $f$, integrate over $[0,1]$, done.

## Common Misconceptions (Teaching Notes)

### 1. Endpoint direction memorised, not seen

"Left endpoints give the lower bound" — true for increasing $f$, exactly backwards for decreasing $f$ (the harmonic case!).

**Fix:** never recite; draw one rectangle on one interval and look. Ten seconds, error impossible.

### 2. Off-by-one in the limits

The upper and lower sums differ only by *one term at each end* — $\sum_{r=1}^{n}$ against $\sum_{r=0}^{n-1}$, $\int_1^{n+1}$ against $\int_1^n$. Sloppy limits silently break the AG.

**Fix:** the two bounds always differ by exactly $f(\text{one end}) - f(\text{other end})$ times the width; if yours differ by anything else, recount.

### 3. Bounds treated as approximations

Writing $\approx$ where the question demands $\leq$ — the entire content of the mark is the *direction* of the inequality, justified by which rectangles cover what.

**Fix:** every bound comes with its one-line justification: "$f$ increasing, right-endpoint rectangles lie above the curve, so…".

## Exam Notes

### Cambridge 9231 (Further Pure 2, Paper 2 — §2.4)

- Both flavours are named by the syllabus: unit-width rectangles (bounding sums, deriving inequalities) and width-$\frac1n$ rectangles (bounding, then squeezing, an integral — the real question above spends its A marks on the $\sum r$/$\sum r^2$ substitutions and the AG algebra).
- **The rare formula-sheet good news: $\sum r$, $\sum r^2$, $\sum r^3$ *are* printed on MF19** — the scheme even says "applies formulae from MF19". The picture and the inequality directions are yours to carry; the sums are handed to you.

### AP Calculus BC / AB

Left/right Riemann sums, their over/under-estimate behaviour for monotone functions, and the limit definition of the definite integral are core (Unit 6) — the width-$\frac1n$ half of the topic, tested with tables and calculator-active parts. The bounding-a-series half is BC's integral test for convergence in Unit 10, the same picture used to decide whether a series converges at all.

### Where it is *not* examined

Not on Cambridge 9709 or OxAQA 9660 (definite integrals arrive there fully formed, never as rectangle limits), not on Edexcel IAL (its FP units skip it), not in IB AA/AI (Riemann sums appear only informally, unexamined).

## Connections

- **Parent:** [[Integration]] — the width-to-zero limit *is* the definition of the definite integral; this topic is that definition kept alive as a working tool.
- **Machinery:** [[Summation of Series]] — supplies $\sum r$, $\sum r^2$ for the squeeze direction; the trap repays it with bounds for the sums that have no closed form.
- **Application:** [[Big-O Notation]] and [[Sorting]] — the $n\log n$ lower bound on comparison sorting is $\ln(n!)$ trapped by these rectangles.
- **Kinship:** [[Squeeze Theorem]] — the same trap-the-unknown-between-two-knowns instinct, here built out of rectangles; the $n \to \infty$ collapse of the two staircases *is* a squeeze-theorem finish.
- **For 9231 students:** [[MF19 Reference (9231)]] — $\sum r$, $\sum r^2$, $\sum r^3$ are on the sheet; the picture is not.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\displaystyle\sum_{r=1}^{n} f(r)$ | `\sum_{r=1}^{n} f(r)` | the staircase |
| $\displaystyle\int_m^n f(x)\,dx$ | `\int_m^n f(x)\,dx` | the ramp |
| $\frac1n\sum f\left(\frac{r}{n}\right)$ | `\frac1n\sum f(\frac{r}{n})` | an integral in disguise |
| $\ln(n!)$ | `\ln(n!)` | Stirling's doorway |
| $\Theta(n\log n)$ | `\Theta(n\log n)` | the sorting bound this picture proves |
