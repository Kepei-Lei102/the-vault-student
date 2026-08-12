---
chinese: 单利与复利 (dānlì yǔ fùlì)
prerequisites:
  - "[[Percentage Calculations (Vocab)]]"
  - "[[Percentages (Vocab)]]"
  - "[[Laws of Indices]]"
leads_to:
  - "[[Exponential Growth and Decay]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Additional Financial Literacy — Australia (Life)]]"
  - "[[Additional Financial Literacy — UK (Life)]]"
  - "[[Additional Financial Literacy — US (Life)]]"
  - "[[Financial Literacy (Life)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - syllabus/9260-N15
  - syllabus/0580-E1-13
  - type/vocabulary
  - misconception/simple-vs-compound
  - misconception/rate-as-decimal-vs-percent
---

# Simple and Compound Interest 单利与复利

## Definition

**Interest** (利息) is a payment for the use of borrowed or invested money. **Simple interest** (单利) is calculated on the *original* principal every year — growth is linear. **Compound interest** (复利) is calculated on the *current balance* each year, so each year's interest is itself interest-bearing the next year — growth is exponential. At the same rate and over more than one year, compound interest always exceeds simple interest, and the gap widens with time.

### 中文锚点

单利：每年利息固定，利息不再生利息，总额呈 *线性* 增长。
复利：每年利息 *加入本金*，利息生利息，总额呈 *指数* 增长。复利公式：$A = P\left(1 + \dfrac{r}{100}\right)^n$。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| interest | 利息 (lìxī) | The payment; the amount that grows on top of the principal |
| principal | 本金 (běnjīn) | The starting amount; $P$ in formulas |
| interest rate | 利率 (lìlǜ) | The percentage charged or earned per period; $r$ or $r\%$ |
| annual rate | 年利率 | Most exam rates are annual unless stated otherwise |
| term / period | 期 / 期限 (qīxiàn) | Number of periods, usually years; $n$ or $t$ |
| simple interest | 单利 (dānlì) | Interest on the *original* principal only |
| compound interest | 复利 (fùlì) | Interest on principal *plus* accumulated interest |
| amount | 本利和 (běnlìhé) | Principal plus interest — the final balance $A$ |
| per annum / p.a. | 每年 (měi nián) | Latin for "each year" — standard exam phrasing |
| invest / deposit | 投资 / 存入 | The customer's action; money enters the account |
| borrow / loan | 借入 / 贷款 | The customer owes interest instead of earning it |

> [!warning] Rate as a *decimal* vs a *percentage*
> Interest formulas appear in two equivalent forms. $I = Prt$ assumes $r$ is already a decimal ($5\% \to 0.05$). $I = \dfrac{Prn}{100}$ assumes $r$ is a percentage number ($5\% \to 5$). Identical mathematically; mismatching them makes the answer $100\times$ too big or too small. This vault uses the **percentage form** in worked examples to match Cambridge / OxAQA convention.

## Simple Interest 单利

Interest is calculated on the **original principal** every year. Interest does not itself earn interest.

$$I \;=\; \frac{Prn}{100} \qquad\qquad A \;=\; P + I \;=\; P\left(1 + \frac{rn}{100}\right)$$

- $P$ = principal (starting amount)
- $r$ = annual interest rate, in percent
- $n$ = number of years
- $I$ = interest earned
- $A$ = total amount (principal + interest)

**Worked example.** A savings account holds $\$2000$ at $3\%$ simple interest per annum. After 5 years:

$$I \;=\; \frac{2000 \times 3 \times 5}{100} \;=\; \$300 \qquad A \;=\; \$2300$$

The interest *per year* is $\$60$, every year, unchanged — the hallmark of linear growth.

## Compound Interest 复利

Interest is calculated on the **current balance** each year: each year's interest joins the principal and earns interest the next year. Two equivalent ways to compute it.

**Iterative (year-by-year).** Multiply the balance by the growth factor $\left(1 + \dfrac{r}{100}\right)$ once per year. For $\$1000$ at $5\%$ over 4 years:

| End of year | Calculation | Balance |
|------------:|-------------|--------:|
| 0 (start) | — | $\$1000.00$ |
| 1 | $1000 \times 1.05$ | $\$1050.00$ |
| 2 | $1050 \times 1.05$ | $\$1102.50$ |
| 3 | $1102.50 \times 1.05$ | $\$1157.63$ |
| 4 | $1157.63 \times 1.05$ | $\$1215.51$ |

**Closed-form formula** (9260 N15 Extension, 0580 E1.13). Applying the growth factor $n$ times is the same as multiplying by it $n$ times, i.e. raising it to the power $n$:

$$\boxed{A \;=\; P\left(1 + \frac{r}{100}\right)^n}$$

Interest earned: $I = A - P$.

**Worked example.** $\$2000$ at $3\%$ compound interest per annum, 5 years:

$$A \;=\; 2000 \times 1.03^5 \;=\; 2000 \times 1.15927\ldots \;\approx\; \$2318.55$$

$$I \;=\; A - P \;\approx\; \$318.55$$

Compare with the simple-interest result at the same rate and term: $\$300$ interest vs $\$318.55$ — only $\$18.55$ more over 5 years. The advantage grows with the term.

## Simple vs Compound — the Divergence

Same setup for both: $P = \$1000$, $r = 5\%$ per annum. Amount $A$ after $n$ years:

| $n$ (years) | Simple: $P(1 + rn/100)$ | Compound: $P(1 + r/100)^n$ | Gap |
|------------:|------------------------:|---------------------------:|----:|
| 1 | $\$1050.00$ | $\$1050.00$ | $\$0.00$ |
| 5 | $\$1250.00$ | $\$1276.28$ | $\$26.28$ |
| 10 | $\$1500.00$ | $\$1628.89$ | $\$128.89$ |
| 20 | $\$2000.00$ | $\$2653.30$ | $\$653.30$ |
| 40 | $\$3000.00$ | $\$7039.99$ | $\$4039.99$ |

Simple interest plotted against time is a straight line; compound interest is an *exponential curve*. At short terms and small rates the two are close — a single-year $3\%$ question barely distinguishes them. The divergence is why long-term investing and long-term debt behave so differently from any one-off percentage change.

> [!tip] Exponential-growth bridge
> The factor $\left(1 + \dfrac{r}{100}\right)^n$ is the student's first encounter with an **exponential function**. When $n$ grows and interest is compounded more and more frequently, the formula limits to $A = Pe^{rt}$ — the continuous-growth form, where Euler's number $e$ first appears naturally. The full bridge is developed in [[Exponential Growth and Decay]].

## Exam Notes

### OxAQA 9260
**Syllabus ref:** N15 — simple and compound interest (**Core**); compound-interest formula $P(1 + r/100)^n$ (**Extension**). Expect a 3–5 mark question on either paper. Simple interest is usually a one-line calculation; compound interest on Core may use the iterative method, on Extension uses the closed form.

Common commands: *calculate*, *find the amount*, *find the interest*, *find the total value of the investment*. Read carefully — "total value" = amount $A$, "interest" = $A - P$.

### Cambridge 0580 Extended
**Syllabus ref:** E1.13 — simple and compound interest, including use of the formula $A = P(1 + r/100)^n$. Paper 4 often embeds compound interest in multi-part questions: one part asks for the amount after a fixed term, a later part asks for the term given a target amount. Students are not expected to use logs on 0580, so trial-and-improvement with the calculator is the accepted method.

### Cambridge 0606
Compound interest resurfaces as the canonical example inside logarithmic equations. $P(1 + r/100)^n = T$ is rearranged for $n$ using logs:
$$n \;=\; \frac{\ln(T/P)}{\ln(1 + r/100)}$$
This is the 0606 route to solving the "how many years until the investment reaches $\$X$?" question cleanly, without trial-and-improvement.

### A-Level
Financial maths uses the continuous-growth limit $A = Pe^{rt}$. The nominal-rate-vs-effective-rate distinction (APR vs APY in US notation; nominal vs AER in UK) also lives here. Not on IGCSE but worth knowing as the college-level follow-on.

> [!info] Beyond syllabus — the Rule of 72
> At an annual compound rate of $r\%$, money roughly doubles every $\dfrac{72}{r}$ years. At $6\%$, doubling takes about $12$ years; at $9\%$, about $8$ years. Derivation: $(1 + r/100)^n = 2 \Rightarrow n = \ln 2 / \ln(1 + r/100) \approx 69/r$ for small $r$; the round number $72$ is chosen because it has many factors ($1, 2, 3, 4, 6, 8, 9, 12$) for easy mental arithmetic. Used daily by investors and anyone estimating inflation's bite — not on any syllabus, widely useful.

## Connections

- **Prerequisite:** [[Percentage Calculations (Vocab)|Percentage Calculations]] — multiplier method; compound interest is the repeated application of the same multiplier
- **Prerequisite:** [[Percentages (Vocab)]] — percentage-as-operator
- **Prerequisite:** [[Laws of Indices]] — the closed form uses integer powers; 0606 extends to logs for solving for $n$
- **Leads to:** [[Exponential Growth and Decay]] — compound interest *is* discrete exponential growth; the deep card derives $e$ from the limit of ever-more-frequent compounding and develops the continuous form $A = Pe^{rt}$.
- **Used in:** [[Laws of Indices]] — compound-interest formulas are the exam's favourite indices-equation context
- **Real-world companion:** [[Financial Literacy (Life)]] — the *language* layer on top of the interest maths: APR vs APY, 年化, fees, 等额本息 vs 等额本金, and insurance product rates that hide the true IRR

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $P\left(1 + \dfrac{r}{100}\right)^n$ | `P\left(1 + \dfrac{r}{100}\right)^n` | Compound-interest closed form |
| $\dfrac{Prn}{100}$ | `\dfrac{Prn}{100}` | Simple-interest formula, percentage form |
| $e^{rt}$ | `e^{rt}` | Continuous-growth limit; link-only here |
| p.a. | `\text{p.a.}` | "per annum"; `\text{}` keeps it upright in math mode |
| $\boxed{\cdot}$ | `\boxed{\cdot}` | Used for the headline compound-interest formula |
