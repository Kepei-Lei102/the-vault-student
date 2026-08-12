---
chinese: 百分数计算 (bǎifēnshù jìsuàn)
prerequisites:
  - "[[Percentages (Vocab)]]"
  - "[[Four Operations (Vocab)]]"
  - "[[Fractions (Vocab)]]"
leads_to:
  - "[[Simple and Compound Interest (Vocab)]]"
  - "[[Exponential Growth and Decay]]"
  - "[[Financial Literacy (Life)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-N15
  - syllabus/0580-E1-13
  - type/vocabulary
  - misconception/chain-percent-changes
  - misconception/reverse-percent-subtraction
---

# Percentage Calculations 百分数计算

## Definition

**Percentage calculations** (百分数计算) are the family of operations that use a percentage as the *tool*: increasing or decreasing a quantity by a given percentage, chaining multiple changes, computing the percentage change between two values, and recovering the original value given the final value and the change (*reverse percentage*). The underlying mathematics is fraction-multiplication; what differs is the English exam language.

### 中文锚点

增加百分之 $X$ ≡ ×$(1 + X/100)$；减少百分之 $X$ ≡ ×$(1 - X/100)$。连续变化：乘数相乘。逆运算：除以乘数以还原原值。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| percentage increase | 百分数增加 | Exam command; new = old plus the % of the old |
| percentage decrease | 百分数减少 | new = old minus the % of the old |
| multiplier | 乘数 / 系数 (xìshù) | Single factor that applies the change: +15% ↔ ×1.15 |
| percentage change | 百分数变化 | $\dfrac{\text{new} - \text{old}}{\text{old}} \times 100\%$; the sign gives direction |
| reverse percentage | 逆百分数 / 还原 | Given final value + %-change, recover the original |
| original value | 原值 / 原价 | The quantity *before* the change; the target of reverse % |
| final value | 末值 / 现价 / 新值 | The quantity *after* the change |
| increase **by** vs increase **to** | 增加了 vs 增加到 | *By* = size of change; *to* = final value (see callout) |

> [!warning] "Increase **by** $X\%$" vs "increase **to** $X\%$"
> *Increase by 20%* adds 20% of the original — final value is $120\%$ of original. *Increase to 120%* states that the final value is $120\%$ of the original directly. Same answer, different English. But *increase to 20%* means the final value is only $20\%$ of the original — that's a decrease. Prepositions matter.

## Increase and Decrease — the Multiplier Method

Use a **single multiplier** whenever possible. It keeps calculations short, handles chain changes cleanly, and is the only sensible method without a calculator.

| Change | English phrasing | Multiplier |
|--------|------------------|------------|
| Increase by $15\%$ | "raise by 15%", "add 15%" | $\times 1.15$ |
| Increase by $7.5\%$ | "grows by 7.5%" | $\times 1.075$ |
| Decrease by $25\%$ | "discount of 25%", "reduce by 25%" | $\times 0.75$ |
| Decrease by $2\%$ | "falls by 2%" | $\times 0.98$ |
| Double | "increase by 100%" | $\times 2$ |
| Halve | "decrease by 50%" | $\times 0.5$ |
| Unchanged | "no change" | $\times 1$ |

**Formulas.**

$$\text{new} \;=\; \text{old} \times \left(1 + \frac{X}{100}\right) \qquad \text{(increase by } X\%\text{)}$$

$$\text{new} \;=\; \text{old} \times \left(1 - \frac{X}{100}\right) \qquad \text{(decrease by } X\%\text{)}$$

## Chain Percentage Changes

When two or more changes happen in sequence, **multiply the multipliers** — do not add or subtract the percentages.

> [!warning] Chain-change trap
> A $+50\%$ increase followed by a $-40\%$ decrease is **not** a net $+10\%$ change. The multiplier is $1.5 \times 0.6 = 0.9$, so the net effect is a $-10\%$ decrease. Students instinctively add and subtract the percentages; always multiply the multipliers and convert at the end.

**Worked example.** A share price rises by $20\%$, then falls by $20\%$. Net change?

$$1.20 \times 0.80 \;=\; 0.96 \quad\Rightarrow\quad \text{net change} = -4\%$$

Order does not matter — multiplication is commutative — but the result is always a net decrease when an equal-percentage gain and loss are combined. The same reason a $50\%$ loss requires a $100\%$ gain just to recover the original value: $0.5 \times 2 = 1$.

## Percentage Change

Given an old value and a new value, the percentage change is:

$$\text{percentage change} \;=\; \frac{\text{new} - \text{old}}{\text{old}} \times 100\%$$

- Positive result ⇒ percentage **increase**
- Negative result ⇒ percentage **decrease**
- Called **percentage error** when comparing a measured value to a true value; called **relative change** in stats

| English phrasing | Computation |
|------------------|-------------|
| "Calculate the percentage increase" | $\frac{\text{new}-\text{old}}{\text{old}} \times 100\%$; expect positive |
| "Find the percentage decrease" | Same formula; expect negative — give the magnitude |
| "What is the percentage change?" | Same formula; include the sign or direction |
| "Express the difference as a percentage of the original" | Same formula — *of the original* names the denominator |

> [!tip] Denominator is always the *original*
> *Of the original* / *of the old value* names the denominator. Dividing by the new value is a common student error and gives a different — wrong — number.

> [!info] 同比 vs 环比 — Chinese news vocabulary (bonus)
> Chinese financial reporting uses two period-comparison terms that appear daily in 财经新闻 (cáijīng xīnwén, *financial news*). Both are direct applications of the percentage-change formula above — what differs is which period plays the role of *old*.
>
> | 中文 | Pinyin | English equivalent | *Old* in the formula |
> |------|--------|--------------------|----------------------|
> | 同比 | tóngbǐ | year-over-year (YoY) | Same period in the previous year (Q1 2026 vs Q1 2025) |
> | 环比 | huánbǐ | period-over-period (PoP); month-over-month (MoM); quarter-over-quarter (QoQ) | Immediately preceding period (Q1 2026 vs Q4 2025) |
>
> Not on any maths syllabus — included here because students hear these terms every day and the underlying maths is exactly this section. A headline like *"CPI 同比上涨 2.3%，环比下降 0.1%"* becomes readable once the two denominators are named.

## Reverse Percentage

**Reverse percentage** (逆百分数 / 还原): given the final value *after* a percentage change, recover the original. Divide the final value by the multiplier — *never* apply the percentage change in the opposite direction.

> [!warning] "Subtract the same percentage" — common student error
> If a shirt is $\$60$ after a $20\%$ discount, the original price is **not** $\$60 + 20\% \text{ of } \$60 = \$72$. That adds $20\%$ of the *discounted* value, not the *original*. Correct: $\$60 \div 0.8 = \$75$. Check: $\$75 \times 0.8 = \$60$. ✓

**Template.** If $Y$ results from $X$ after a $+p\%$ change:

$$Y = X \times \left(1 + \frac{p}{100}\right) \;\;\Rightarrow\;\; X = \frac{Y}{1 + p/100}$$

After a $-p\%$ change, divide by $(1 - p/100)$.

**Worked examples.**

1. A restaurant bill including $12.5\%$ service charge is $\$81$. Bill before service?
   $$\text{original} \;=\; \frac{81}{1.125} \;=\; \$72$$

2. After a $15\%$ pay rise, a salary is $\$34{,}500$. Salary before?
   $$\text{original} \;=\; \frac{34{,}500}{1.15} \;=\; \$30{,}000$$

3. A population shrinks by $8\%$ in a year and now stands at $23{,}000$. Original?
   $$\text{original} \;=\; \frac{23{,}000}{0.92} \;\approx\; 25{,}000$$

## Exam Notes

### OxAQA 9260
**Syllabus ref:** N15 — increase, decrease, simple and compound interest (**Core**); reverse percentages, compound-interest formula (**Extension**). This card covers the increase / decrease / chain / reverse portion. Simple and compound interest sit in their own card — see [[Simple and Compound Interest (Vocab)|Simple and Compound Interest]].

Common 9260 commands: *calculate*, *find the percentage change*, *express as a percentage*, *find the original*. Reverse percentage is a regular Extension-paper item; students who attempt to "subtract the same percentage back" lose every mark in a 3–4 mark part.

### Cambridge 0580 Extended
**Syllabus ref:** E1.13 — percentages, including increase, decrease, and reverse percentage. Simple and compound interest live at the same syllabus code but are covered in [[Simple and Compound Interest (Vocab)|Simple and Compound Interest]]. Papers 2 and 4 both test percentage increase and reverse percentage, often in money, population, and measurement contexts.

### Cambridge 0606
Reverse percentage is assumed knowledge. It resurfaces inside exponential and logarithmic equations — e.g., a compound-interest-style problem ending in *"find $n$ such that..."* routes through [[Laws of Indices]] and logs.

### A-Level
Not a standalone topic, but percentage-change reasoning underpins financial maths, relative error in stats, and any applied modelling involving rates or growth.

## Connections

- **Prerequisite:** [[Percentages (Vocab)]] — percentage-as-operator, conversion between fraction / decimal / percentage
- **Prerequisite:** [[Four Operations (Vocab)]] — multiplier method relies on straightforward multiplication and division
- **Prerequisite:** [[Fractions (Vocab)]] — a multiplier is a fraction in disguise
- **Leads to:** [[Simple and Compound Interest (Vocab)|Simple and Compound Interest]] — the canonical repeated-percentage application; principal, rate, term, and the closed-form $P(1+r/100)^n$
- **Used in:** [[Upper and Lower Bounds]] — percentage error and relative error use the "$\dfrac{\text{new} - \text{old}}{\text{old}} \times 100\%$" machinery
- **Used in:** [[Ratio (Vocab)]] — percentages and ratios are both ways of expressing part-to-whole; "of" + ratio share grammar

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\times$ | `\times` | Multiplication for multipliers in working |
| $\dfrac{a}{b}$ | `\dfrac{a}{b}` | Display-size fraction for percentage-change formula |
| $\%$ | `\%` | Backslash required — bare `%` starts a LaTeX comment |
| $\approx$ | `\approx` | "Approximately equal" — useful after division that doesn't round cleanly |
