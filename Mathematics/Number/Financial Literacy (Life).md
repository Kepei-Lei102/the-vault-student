---
chinese: 金融常识 (jīnróng chángshí)
prerequisites:
  - "[[Percentages (Vocab)]]"
  - "[[Percentage Calculations (Vocab)]]"
  - "[[Simple and Compound Interest (Vocab)]]"
leads_to:
  - "[[Additional Financial Literacy — Australia (Life)]]"
  - "[[Additional Financial Literacy — UK (Life)]]"
  - "[[Additional Financial Literacy — US (Life)]]"
tags:
  - subject/mathematics
  - domain/number
  - syllabus/0580-E1-16
  - type/life-card
  - topic/finance
  - topic/financial-literacy
  - misconception/apr-vs-apy
  - misconception/advertised-vs-guaranteed-rate
  - misconception/equal-installment-vs-equal-principal
  - misconception/insurance-illustrated-vs-guaranteed-return
---

# Financial Literacy 金融常识

## What this card is

A **life card**. None of this is on any maths syllabus. All of it is in your phone's banking app, your parents' mortgage statement, and every insurance salesperson's brochure. Banking, investing, loans and insurance use a surprisingly small vocabulary, dressed up with decorative adjectives and technically-true footnotes. This card strips the decoration so you can hear what's actually being claimed.

The underlying maths is nothing new — it's percentages, multipliers, and compound interest, all of which live in [[Percentages (Vocab)|Percentages]], [[Percentage Calculations (Vocab)|Percentage Calculations]], and [[Simple and Compound Interest (Vocab)|Simple and Compound Interest]]. What's new is the **language**, and the places where the language and the maths don't match.

### 中文锚点

金融产品的 *语言* 常与 *数学实质* 不对应。广告打出的是 *年化 / 演示 / 预期*，合同里落字的是 *实际 / 预定 / 保证*。学会辨认这两层差别，就是金融常识的核心。

> [!info] A note on types
> This is the first `type/life-card` in the vault. Life cards live in their natural mathematical domain (`domain/number` here) but carry no syllabus tag. They are written for the student who needs to read a real-world document, not pass an exam.

> [!tip] Going abroad? Read the regional companion.
> This card covers universal concepts and Chinese-specific vocabulary. If you're heading overseas for study or work, pair it with the companion card for your destination — the banking apps, tax forms, and insurance vocabulary you'll meet there are **different**, sometimes radically so (US healthcare in particular).
>
> - 🇺🇸 [[Additional Financial Literacy — US (Life)]] — FICO, US healthcare vocab, 401(k)/IRA/HSA, W-2/1099, F-1 tax corner
> - 🇬🇧 [[Additional Financial Literacy — UK (Life)]] — ISA ecosystem, NI, PAYE + tax codes, Plan 2/5 student loan, NHS
> - 🇦🇺 [[Additional Financial Literacy — Australia (Life)]] — compulsory Super, HECS-HELP, franking credits, LHC loading, offset accounts

## 1. Rate family — 利率 vs 年利率 vs 年化

The most common word on any bank app is *rate*. The Chinese and English both distinguish **quoting period** (annual / monthly / daily) from **normalization** (the "annualized" projection).

| 中文 | Pinyin | English | What it's quoting |
|------|--------|---------|-------------------|
| 利率 | lìlǜ | interest rate | Generic — ask for the period |
| 年利率 | nián lìlǜ | annual rate | Rate *per year* |
| 月利率 | yuè lìlǜ | monthly rate | Rate *per month* — credit cards, consumer loans |
| 日利率 | rì lìlǜ | daily rate | Penalty interest, margin loans, payday loans |
| 年化 / 年化利率 / 年化收益率 | nián huà | annualized (rate / yield) | A *projection* to a year, not a promise |
| 定价利率 | dìngjià lìlǜ | benchmark / pricing rate | The reference rate (LPR in China) |

> [!warning] 月利率 × 12 ≠ 年利率 in practice
> Consumer loan ads often quote *月费率 0.6%* and expect you to multiply by 12 to get 7.2% — but that ignores compounding *and* the fact that fees are charged on the full principal even as you repay it. The **real** APR on "12期 0.6%/月" is closer to **13.2%**. See the credit-card callout in §5.

> [!tip] What 年化 actually means
> 年化 is a **convention for quoting**, not a forecast. "七日年化收益率 3.2%" means "if the last 7 days' rate of return continued unchanged for a full year, the total return would be 3.2%". Tomorrow's seven-day rate may be lower; next week's may be higher. It is a *sliding window projection*, not what you will earn this year.

## 2. Nominal vs Effective — APR vs APY

The single most profitable confusion in retail finance. Loans are quoted in APR to make the rate look low; deposits are quoted in APY to make the yield look high. Always compare APY to APY.

| English | 中文 | What it tells you |
|---------|------|-------------------|
| APR (Annual Percentage Rate) | 名义年利率 | Periodic rate × periods per year — assumes **no** compounding |
| APY / AER | 实际年利率 / 年百分收益率 | Actual growth factor after compounding |
| Nominal rate | 名义利率 | = APR when used for loans |
| Effective rate | 实际利率 | = APY when used for deposits |

**Formula bridge.** If $r$ is the nominal annual rate compounded $m$ times per year, the effective annual rate is:

$$\text{APY} \;=\; \left(1 + \frac{r}{m}\right)^m - 1$$

**Worked example.** $5\%$ nominal compounded monthly:

$$\text{APY} \;=\; \left(1 + \frac{0.05}{12}\right)^{12} - 1 \;\approx\; 0.05116 \;=\; 5.12\%$$

Small gap at 5%; wide gap at high rates or when compounding is daily. A credit card at *18% APR* compounded daily has an APY closer to **19.7%**.

## 3. Returns — the advertising layer

"Return" has at least four names in Chinese finance, each meaning something different.

| 中文 | Pinyin | English | What it means |
|------|--------|---------|---------------|
| 收益率 | shōuyì lǜ | rate of return | Return as a percentage of principal — ask for the period |
| 年化收益率 | niánhuà shōuyì lǜ | annualized return | Period return scaled to a year |
| 七日年化收益率 | qī rì niánhuà shōuyì lǜ | 7-day annualized return | Last 7 days' return, projected to a year |
| 万份收益 | wàn fèn shōuyì | per-10,000 daily income | Yesterday's yuan earned per ¥10,000 held |
| 预期收益率 | yùqī shōuyì lǜ | expected rate of return | *Expected*, not promised |
| 业绩比较基准 | yèjì bǐjiào jīzhǔn | performance benchmark | The target the fund *aims at* — honest version of "expected" |

> [!warning] 七日年化 and 万份收益 — the two faces of 余额宝
> Money market funds like 余额宝 advertise **七日年化收益率** (advertising-friendly percentage) alongside **万份收益** (what you actually earned yesterday). Only 万份收益 is a fact — it's yesterday's yuan per ¥10,000 held. 七日年化 is a projection that changes every day.

> [!info] 预期 vs 业绩比较基准 — a real regulatory shift
> Chinese 理财产品 used to advertise *预期收益率* as if it were a near-promise. After the 2018 资管新规 (asset-management rules), banks largely moved to *业绩比较基准* — a benchmark the fund *aims* at, clearly not a promise. Same product, more honest wording. If an older document you're reading uses 预期收益率, treat it with suspicion.

## 4. Fees — 费率 family

Fees are almost always quoted as an annual percentage of assets under management. They look small per year and compound viciously over time.

| 中文 | Pinyin | English | When paid |
|------|--------|---------|-----------|
| 费率 | fèilǜ | fee rate | Umbrella term — specify which fee |
| 管理费 | guǎnlǐ fèi | management fee | Paid to fund manager, daily accrued |
| 托管费 | tuōguǎn fèi | custodian fee | Paid to the bank holding the assets |
| 申购费 | shēngòu fèi | subscription fee (front-end load) | When you buy |
| 赎回费 | shúhuí fèi | redemption fee (back-end load) | When you sell, often waived after 2 years |
| 销售服务费 | xiāoshòu fúwù fèi | sales service fee (trailing) | Ongoing — funds C-shares |
| 手续费 | shǒuxù fèi | service charge / processing fee | Transactional — transfers, wires, installments |

> [!warning] The fee-compounding trap
> A $1.5\%$ annual management fee sounds small. Compounded over 30 years against a $6\%$ gross return, it reduces the investor's final balance by about **36%**. Mathematically: the investor compounds at $4.5\%$ while the fund compounds at $6\%$, so the gap is $(1.045/1.06)^{30} \approx 0.64$. Fees are the most linear-looking, exponentially-expensive line item in any financial product.

## 5. Loans — 等额本息 vs 等额本金

Canonical Chinese home-loan trap. Same 贷款金额 (loan amount), same 利率 (rate), same 贷款期限 (term) — but two repayment schedules with very different total interest.

| 中文 | English | Monthly payment shape | Total interest |
|------|---------|-----------------------|----------------|
| 等额本息 | Equal monthly payment (EMI) | **Flat** — same every month | **Higher** |
| 等额本金 | Equal principal, declining payment | **High at start, falls every month** | **Lower** |

**Worked example.** Loan of ¥1,000,000 at $4.5\%$ annual over 30 years:

| Method | First month | Last month | Total interest |
|--------|------------:|-----------:|---------------:|
| 等额本息 | ¥5,067 | ¥5,067 | ¥823,000 |
| 等额本金 | ¥6,528 | ¥2,788 | ¥676,000 |

**Gap: ¥147,000.** Banks default to 等额本息 on most mortgages because the flat payment is easier to budget; 等额本金 requires the borrower to carry a higher payment for the first 10–15 years but saves six figures of interest over the life of the loan.

> [!tip] Which to choose
> 等额本息 if your income will stay flat or grow slowly; 等额本金 if you can handle the high early payments and want lower total cost. The choice is a **budget question**, not a maths question — the maths says 等额本金 always wins in total interest paid.

> [!warning] Credit-card 分期 — the rate-as-fee deception
> When a credit card offers "12期分期 手续费 0.6%/月", this is **not** a 7.2% annual rate. The fee is charged on the *original* principal every month — but you've partially repaid the loan, so you're paying fees on money you no longer owe. The effective APR is roughly:
> $$\text{APR} \;\approx\; \frac{2 \times m \times f}{m+1}$$
> where $f$ is the total fee rate and $m$ is the number of periods. For 12 periods at 7.2% total fee: $\text{APR} \approx 13.3\%$. Almost double the advertised "rate".

## 6. Currency and macro

Short pointer section — all standard [[Percentage Calculations (Vocab)|percentage-change]] machinery.

| 中文 | Pinyin | English | Typical quote |
|------|--------|---------|---------------|
| 汇率 | huìlǜ | exchange rate | USD/CNY = 7.10 → 1 USD buys 7.10 CNY |
| 通货膨胀 / 通胀 | tōnghuò péngzhàng | inflation | CPI same-period YoY % change |
| 通缩 | tōngsuō | deflation | Negative CPI change |
| CPI | — | Consumer Price Index | 消费者物价指数 |
| 升值 / 贬值 | shēng zhí / biǎn zhí | appreciation / depreciation | Of a currency against another |
| 实际收益率 | shíjì shōuyì lǜ | real rate of return | Nominal return *minus* inflation |

**Real vs nominal.** If a deposit pays $3\%$ and inflation is $2.5\%$, the **real** return is only $\approx 0.5\%$. Negative real rates (deposit rate < inflation) are a silent wealth transfer from savers to borrowers.

## 7. Insurance — 保险 — "disclosed, not hidden, almost always misread"

The part of the financial system where the gap between language and substance is widest. Nothing in a well-written policy is technically untrue — and almost nothing is read the way the buyer thinks.

### Core vocabulary

| 中文 | Pinyin | English | What it *actually* is |
|------|--------|---------|-----------------------|
| 保费 | bǎofèi | premium | What **you pay** every year |
| 保额 | bǎo'é | sum insured / face amount | Max they pay out on claim |
| 保单 | bǎodān | policy | The contract itself |
| 保险期间 | bǎoxiǎn qījiān | policy term | Years of coverage |
| 免赔额 | miǎnpéi'é | deductible | Your share before they pay |
| 理赔 | lǐpéi | claim settlement | The payout process |
| 退保 | tuìbǎo | surrender | Canceling the policy early |
| 现金价值 | xiànjīn jiàzhí | cash / surrender value | What you get back if you 退保 |
| 犹豫期 | yóuyù qī | free-look period | 10–15 days to cancel with full refund |

### Rates and returns — the trap surface

| 中文 | Pinyin | English | What it means |
|------|--------|---------|---------------|
| 预定利率 | yùdìng lìlǜ | guaranteed / assumed rate | Growth rate the contract **promises** on reserves |
| 演示利率 | yǎnshì lìlǜ | illustrated rate | The *hypothetical* high/mid/low rate in the brochure |
| 分红 | fēnhóng | dividend (non-guaranteed) | Bonus paid in good years — **not guaranteed** |
| 万能账户结算利率 | wànnéng zhànghù jiésuàn lìlǜ | universal-account credit rate | Monthly rate credited to the investment account |
| 保底利率 | bǎodǐ lìlǜ | floor / minimum rate | Floor on the universal-account credit rate |
| IRR | — | internal rate of return | Single rate equating your premium cash-outflows with your benefit cash-inflows |

### Product names to recognise

| 中文 | Pinyin | English | One-line mechanism |
|------|--------|---------|--------------------|
| 定期寿险 | dìngqī shòuxiǎn | term life | Pays only if you die within term |
| 终身寿险 | zhōngshēn shòuxiǎn | whole life | Pays whenever you die; always pays |
| 增额终身寿 | zēng'é zhōngshēn shòu | increasing whole life | Savings vehicle dressed as life insurance |
| 重疾险 | zhòngjí xiǎn | critical illness | Lump sum on listed diagnoses |
| 医疗险 | yīliáo xiǎn | medical insurance | Reimburses hospital costs |
| 年金险 | niánjīn xiǎn | annuity | Pays you back in scheduled installments |
| 分红险 | fēnhóng xiǎn | participating (par) insurance | 预定利率 floor + non-guaranteed 分红 |
| 万能险 | wànnéng xiǎn | universal life | Protection + separate investment account |
| 投连险 | tóulián xiǎn | investment-linked | Policyholder bears **all** investment risk |

### The four deceptions, without any lying

> [!warning] 1. Illustrated rate ≠ guaranteed rate
> 分红险 brochures display **演示利率** at low / mid / high scenarios (commonly 2.5% / 4% / 6%). The legal promise is the **预定利率** alone — typically 2.0%–2.5% in 2026 China. The 高档 演示 is a marketing display of a scenario the company has no obligation to deliver. *分红不保证* ("dividends not guaranteed") is printed on page 47.

> [!warning] 2. 预定利率 ≠ your IRR
> "增额终身寿 with a 3.0% 预定利率" does **not** mean you earn 3.0% on premiums paid. The 3.0% is the rate at which the *insurance reserve* grows. After front-end fees, mortality charges, and commissions, the **IRR on premiums vs benefits** is typically:
> - Year 5: negative (surrender value < total premiums)
> - Year 10: ~1.5%
> - Year 20: ~2.3%
> - Year 40: ~2.7% — approaching but not reaching 3.0%
>
> If you want 3.0%, buy a 3.0% bond — not an insurance product that grows a hidden reserve at 3.0%.

> [!warning] 3. 现金价值 < 累计保费 in early years
> Policyholders discover this at the worst possible moment. For the first 3–5 years of most savings-insurance products, if you 退保 (surrender), the 现金价值 is a fraction — sometimes as little as 30–50% — of the 保费 you've paid in. This is how commissions are funded; it's fully disclosed; it's almost never read.

> [!warning] 4. 万能险 "结算利率" is monthly and non-guaranteed
> A 万能账户 showing "当月结算利率 4.5%" is **monthly** figure re-annualized, and can change month-to-month down to the 保底利率 (often 2.0% or 2.5%). The only guaranteed rate is the 保底. Everything above it is a policy decision the company makes each month.

> [!tip] The honest version of insurance
> Insurance is for events so costly you can't absorb them: long life (outliving savings → 年金险), early death with dependents (→ 定期寿险), catastrophic illness (→ 重疾险 / 医疗险). Those are real risks and real transfers. The **savings-product** face of insurance (增额终身寿, 分红险, 万能险, 投连险) solves a smaller problem (tax-deferred illiquid saving) at a higher cost than bonds or index funds. Useful for some buyers — *rarely* the one being sold to.

## 8. Product types — quick glossary

Named, not explained — just so the words are on your map.

| 中文 | Pinyin | English |
|------|--------|---------|
| 活期（存款） | huóqī | demand / current deposit |
| 定期（存款） | dìngqī | fixed-term deposit |
| 结构性存款 | jiégòuxìng cúnkuǎn | structured deposit |
| 国债 | guózhài | government bond |
| 企业债 | qǐyè zhài | corporate bond |
| 货币基金 | huòbì jījīn | money market fund (余额宝-type) |
| 债券基金 | zhàiquàn jījīn | bond fund |
| 股票基金 | gǔpiào jījīn | equity fund |
| 混合基金 | hùnhé jījīn | mixed / balanced fund |
| 指数基金 / ETF | zhǐshù jījīn | index fund / ETF |
| 理财产品 | lǐcái chǎnpǐn | wealth management product |
| 信托 | xìntuō | trust |
| 股票 / 债券 | gǔpiào / zhàiquàn | stock / bond |

Risk ladder, roughly ascending: 活期 → 国债 → 定期 → 货币基金 → 债券基金 → 混合基金 → 股票基金 → 股票 → 信托 / 投连险. Return expectations rise with risk; so does the loss in a bad year.

## Connections

- **Prerequisite:** [[Percentages (Vocab)|Percentages]] — the operator and the "of" preposition
- **Prerequisite:** [[Percentage Calculations (Vocab)|Percentage Calculations]] — multiplier method, percentage change, reverse percentage
- **Prerequisite:** [[Simple and Compound Interest (Vocab)|Simple and Compound Interest]] — the math engine underneath APR / APY / IRR
- **Related:** [[Laws of Indices]] — $(1 + r)^n$ and logs for solving for $n$ in retirement-goal problems
- **Leads to — reserved:** [[Exponential Growth and Decay]] — continuous compounding and $Pe^{rt}$; the mathematical limit of APY as compounding frequency → ∞

## Closing note

The shortest rule that covers every section of this card: **compare like to like**. APY to APY. Real return to real return. IRR to IRR. 年化 to 年化, over the same window. When a product makes this hard — when the rate is quoted in a way that can't be directly compared — that is itself the signal.
