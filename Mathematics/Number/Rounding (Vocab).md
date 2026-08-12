---
chinese: 取近似值 (qǔ jìnsì zhí)
prerequisites:
  - "[[Four Operations (Vocab)]]"
leads_to:
  - "[[Estimation (Vocab)]]"
  - "[[Upper and Lower Bounds]]"
  - "[[Significant Figures]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-N11
  - syllabus/0580-E1-9
  - type/vocabulary
  - misconception/significant-figures-zero
---

# Rounding 取近似值

## Definition

**Rounding** (取近似值) replaces a number with a simpler nearby value. The two main methods are **decimal places** (d.p.) and **significant figures** (s.f.).

### Decimal places (d.p.) 小数位

Count digits **after** the decimal point.

$$3.14159 \approx 3.14 \quad \text{(2 d.p.)} \qquad 0.00673 \approx 0.007 \quad \text{(1 d.p.?)}$$

Wait — that last one is wrong. $0.00673$ to 1 d.p. is $0.0$ (which is essentially 0). The instruction probably meant 1 significant figure: $0.007$. This confusion is why exams specify carefully.

### Significant figures (s.f.) 有效数字

Count digits from the **first non-zero digit**.

| Number | 1 s.f. | 2 s.f. | 3 s.f. |
|--------|--------|--------|--------|
| $3472$ | $3000$ | $3500$ | $3470$ |
| $0.005081$ | $0.005$ | $0.0051$ | $0.00508$ |
| $20.06$ | $20$ | $20$ | $20.1$ |

### 中文锚点

取近似值 = 用更简单的数代替原来的数。小数位 (d.p.) = 小数点后有几位。有效数字 (s.f.) = 从第一个非零数字开始数。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| round / round off | 取近似值 / 四舍五入 | 四舍五入 literally means "discard 4, enter 5" — the Chinese rounding rule |
| decimal place (d.p.) | 小数位 (xiǎoshù wèi) | Digits after the point |
| significant figure (s.f.) | 有效数字 (yǒuxiào shùzì) | Digits that carry meaning, starting from the first non-zero |
| truncate / truncation | 截断 (jiéduàn) | Cut off digits without rounding (always round down) |
| correct to | 精确到 (jīngquè dào) | "Correct to 2 d.p." = round to 2 decimal places |
| nearest | 最近的 | "To the nearest 10" = round to tens |

> [!warning] Leading zeros are NOT significant
> In $0.00508$: the zeros before 5 are placeholders, not significant. The number has 3 significant figures (5, 0, 8). But the zero between 5 and 8 IS significant — it's trapped between non-zero digits.

> [!warning] Trailing zeros: context matters
> $2500$ could be 2 s.f. or 4 s.f. — you can't tell without context. This ambiguity is one reason standard form exists: $2.5 \times 10^3$ (2 s.f.) vs $2.500 \times 10^3$ (4 s.f.).

> [!info] Beyond syllabus — Rounding in programming
> Most programming languages give you three functions: `floor()` (always round down), `ceil()` (always round up), and `round()` — but `round()` sometimes behaves unexpectedly (Python's "banker's rounding" rounds 0.5 to the nearest *even* number!).
>
> The classic trick: to round $x$ to the nearest integer using only `floor`, compute `floor(x + 0.5)`. Adding 0.5 shifts the halfway boundary so that truncation becomes rounding. For ceiling: `floor(x) + 1` if $x$ is not already an integer, or just `ceil(x)`.
>
> Full details and worked examples in [[Upper and Lower Bounds]] §Beyond syllabus.

## Exam Notes

### OxAQA 9260 / Cambridge 0580
**Syllabus ref:** N11 (9260), E1.9 Estimation (0580). Virtually every calculation paper specifies "Give your answer correct to 3 significant figures" or "2 decimal places." Losing marks for wrong rounding is the most avoidable mistake on the paper.

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — need to compute before rounding
- **Leads to:** [[Estimation (Vocab)]] — rounding to 1 s.f. is the first step of estimation
- **Leads to:** [[Upper and Lower Bounds]] — rounding creates error intervals
- **Parallel:** [[Standard Form (Vocab)]] — s.f. and standard form often appear together

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\approx$ | `\approx` | "Approximately equal to" |
