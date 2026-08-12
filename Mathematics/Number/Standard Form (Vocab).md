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
  - curriculum/Cambridge-0580
  - syllabus/9260-N8
  - syllabus/0580-E1-8
  - type/vocabulary
  - misconception/standard-form-range
---

# Standard Form 标准式

## Definition

**Standard form** (标准式), also called **scientific notation** (科学记数法), writes any number as:

$$a \times 10^n \qquad \text{where } 1 \leq a < 10 \text{ and } n \text{ is an integer}$$

Large numbers get a positive $n$; small numbers get a negative $n$.

| Number | Standard form | $n$ |
|--------|--------------|-----|
| $56\,000$ | $5.6 \times 10^4$ | $+4$ |
| $3\,200\,000$ | $3.2 \times 10^6$ | $+6$ |
| $0.0047$ | $4.7 \times 10^{-3}$ | $-3$ |
| $0.000\,000\,91$ | $9.1 \times 10^{-7}$ | $-7$ |

### 中文锚点

标准式 = $a \times 10^n$ 的形式，其中 $1 \leq a < 10$。大数用正指数，小数用负指数。中文更常说"科学记数法"。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| standard form | 标准式 (biāozhǔn shì) | Cambridge/OxAQA term |
| scientific notation | 科学记数法 | Same thing; used in IB, AP, and sciences |
| mantissa | 尾数 (wěishù) | The $a$ part ($1 \leq a < 10$). See etymology note below |
| exponent / power | 指数 (zhǐshù) | The $n$ in $10^n$ |
| order of magnitude | 数量级 (shùliàng jí) | The power of 10; used for rough comparisons |

> [!info] Why "mantissa"?
> The word *mantissa* is Latin for "makeweight" or "something added" — the small extra piece a shopkeeper would throw in to round up a sale. In the days of **logarithm tables** (before calculators), every logarithm had two parts: the *characteristic* (the integer part, which told you the order of magnitude) and the *mantissa* (the decimal part, which you looked up in a table). When scientific notation came along, the word was borrowed for the $a$ part — the "significant content" that you multiply by the power of 10. The Chinese 尾数 (wěishù, "tail number") captures the same idea: it's the precise bit that comes after the big-picture power of 10.

> [!warning] $a$ must be between 1 and 10
> $56 \times 10^3$ is NOT standard form ($56 \geq 10$). Neither is $0.56 \times 10^5$ ($0.56 < 1$). The correct form is $5.6 \times 10^4$. Exam mark schemes are strict about this.

## Calculating in Standard Form

**Multiplying:** Multiply the $a$-parts, add the indices.
$$(3 \times 10^4) \times (2 \times 10^5) = 6 \times 10^9$$

**Dividing:** Divide the $a$-parts, subtract the indices.
$$(8 \times 10^7) \div (4 \times 10^3) = 2 \times 10^4$$

**Adding/Subtracting:** Convert to the same power of 10 first, then add/subtract.
$$(3.2 \times 10^5) + (4.8 \times 10^4) = (3.2 \times 10^5) + (0.48 \times 10^5) = 3.68 \times 10^5$$

## Exam Notes

### OxAQA 9260 / Cambridge 0580
**Syllabus ref:** N8 (9260), E1.9 (0580). Calculator display shows standard form as `5.6E4`. Students must convert between ordinary numbers and standard form in both directions. Common question: "Write $0.00032$ in standard form."

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
