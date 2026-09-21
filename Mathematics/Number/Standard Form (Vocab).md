---
chinese: 标准式 (biāozhǔn shì) / 科学记数法 (kēxué jìshù fǎ)
prerequisites:
  - "[[Laws of Indices]]"
  - "[[Powers and Roots (Vocab)]]"
  - "[[Decimals (Vocab)]]"
leads_to:
  - "[[Estimation (Vocab)]]"
  - "[[Physical Quantities and Units]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/Cambridge-0580
  - syllabus/9260-N8
  - syllabus/0580-E1-8
  - type/vocabulary
  - misconception/standard-form-range
---

# Standard Form 标准式

## Definition

**Standard form** (标准式), also called **scientific notation** (科学记数法), writes a positive number as:

$$a \times 10^n \qquad \text{where } 1 \leq a < 10 \text{ and } n \text{ is an integer}$$

Numbers at least 10 have positive $n$; numbers between 0 and 1 have negative $n$; numbers from 1 up to, but not including, 10 have $n=0$. For a negative number, write the minus sign separately (for example $-4.7\times10^{-3}$). Zero has no normalised form with $1\leq a<10$.

| Number | Standard form | $n$ |
|--------|--------------|-----|
| $56\,000$ | $5.6 \times 10^4$ | $+4$ |
| $3\,200\,000$ | $3.2 \times 10^6$ | $+6$ |
| $0.0047$ | $4.7 \times 10^{-3}$ | $-3$ |
| $0.000\,000\,91$ | $9.1 \times 10^{-7}$ | $-7$ |

### 中文锚点

一座城市有六百万人，把它写成“六个一百万”，是不是比盯着一长串零更容易看清大小？科学记数法做的就是这种分工：前面的数说有几份，后面的十的幂说每份有多大。零没有丢，只是被收进了“每份多大”里。这样比较两个城市的人口时，我们先看每份有多大，再看有几份，就不容易因为数错一个零而差了十倍。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| standard form | 标准式 (biāozhǔn shì) | Cambridge/OxAQA term |
| scientific notation | 科学记数法 | Same thing; used in IB, AP, and sciences |
| coefficient / significand | 系数 / 有效数 | The $a$ part ($1 \leq a < 10$) |
| exponent / power | 指数 (zhǐshù) | The $n$ in $10^n$ |
| order of magnitude | 数量级 (shùliàng jí) | The power of 10; used for rough comparisons |

> [!info] Coefficient, significand and mantissa
> **Coefficient** or **significand** names the $a$ part here. You may also encounter *mantissa*, but that word has another established meaning: the fractional part of a logarithm. Check which convention is being used.

> [!warning] $a$ must be between 1 and 10
> $56 \times 10^3$ is NOT standard form ($56 \geq 10$). Neither is $0.56 \times 10^5$ ($0.56 < 1$). The correct form is $5.6 \times 10^4$. These other expressions have the same value but are not normalised.

## Calculating in Standard Form

**Tool: index laws. Trigger: a product of powers of the same base.** Multiply the coefficients and add the indices; renormalise if the coefficient reaches 10.
$$(3 \times 10^4) \times (2 \times 10^5) = 6 \times 10^9$$

**Tool: index laws. Trigger: a quotient of powers of 10.** Divide the coefficients and subtract the indices.
$$(8 \times 10^7) \div (4 \times 10^3) = 2 \times 10^4$$

**Tool: a common scale. Trigger: addition combines counts only when their bundle sizes match.** Convert to the same power of 10 first, then add/subtract the coefficients.
$$(3.2 \times 10^5) + (4.8 \times 10^4) = (3.2 \times 10^5) + (0.48 \times 10^5) = 3.68 \times 10^5$$

## Exam Notes

### Cambridge 0580 — C1.8 / E1.8

Both tiers require conversion into and out of standard form and calculations with it. **Core calculation with standard form is expected only on Paper 3**; conversion remains part of the Core content. Extended includes the same operations. Keep the coefficient in the stated range and interpret calculator notation such as `5.6E4` as $5.6\times10^4$. E1.9 concerns estimation, not standard form.

### OxfordAQA 9260 — N8

Core N8 requires calculation with and interpretation of standard form, including calculator displays. Extension includes Core content. Conversion and arithmetic are both relevant; the examples above are original teaching examples, not quoted past-paper questions.

### IB Mathematics AA and AI — SL 1.1, also included at HL

Both guides explicitly require operations in scientific notation. Their SL 1.1 guidance rejects calculator/computer notation as the final written form: write $5.2\times10^{30}$ rather than `5.2E30`. This is shared AA/AI content, not an HL-only extension.

### Later courses — assumed notation

Cambridge 0606/9709/9231, Edexcel IAL Mathematics/Further Mathematics and OxfordAQA 9660 build on earlier numerical skills; this is not a separate new theorem or unit in those specifications. AP Calculus AB/BC and AP Statistics likewise use numerical representations without a standalone scientific-notation outcome. Correct notation can still be needed inside a problem: absence of a dedicated unit does not mean the notation is forbidden or irrelevant. No formula-sheet entry is required.

## Connections

- **Prerequisite:** [[Laws of Indices]] — $10^n$ uses index laws for calculation
- **Prerequisite:** [[Powers and Roots (Vocab)]] — understanding powers of 10
- **Leads to:** [[Estimation (Vocab)]] — estimating often means working with orders of magnitude
- **Parallel:** [[Rounding (Vocab)]] — significant figures and standard form often appear together

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $a \times 10^n$ | `a \times 10^n` | Standard form |
| $10^{-3}$ | `10^{-3}` | Negative index for small numbers |
