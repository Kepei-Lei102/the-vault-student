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

$$3.14159\approx3.14\quad\text{(2 d.p.)},\qquad 0.00673\approx0.0\quad\text{(1 d.p.)}.$$

The same $0.00673$ is $0.007$ to **1 significant figure**. Decimal places specify a fixed position; significant figures start at the first nonzero digit.

### Significant figures (s.f.) 有效数字

Count digits from the **first non-zero digit**.

| Number | 1 s.f. | 2 s.f. | 3 s.f. |
|--------|--------|--------|--------|
| $3472$ | $3000$ | $3500$ | $3470$ |
| $0.005081$ | $0.005$ | $0.0051$ | $0.00508$ |
| $20.06$ | $2\times10^1$ | $2.0\times10^1$ | $20.1$ |

### 中文锚点

朋友问你还有多远，你看着导航上的“397米”，说“差不多400米”，对方就能判断该走一会儿还是得打车。那几米的差别，对眼前这个决定并不重要，省掉反而好理解。可如果你是在告诉外卖员门牌号，就不能把397号也说成400号了。取近似值，就是看清眼前要做什么，再决定哪些细节可以先放下。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| round / round off | 取近似值 / 四舍五入 | 四舍五入 literally means "discard 4, enter 5" — the Chinese rounding rule |
| decimal place (d.p.) | 小数位 (xiǎoshù wèi) | Digits after the point |
| significant figure (s.f.) | 有效数字 (yǒuxiào shùzì) | Digits that carry meaning, starting from the first non-zero |
| truncate / truncation | 截断 (jiéduàn) | Discard digits; at integer precision, move towards zero (not always down) |
| correct to | 精确到 (jīngquè dào) | "Correct to 2 d.p." = round to 2 decimal places |
| nearest | 最近的 | "To the nearest 10" = round to tens |

> [!warning] Leading zeros are NOT significant
> In $0.00508$: the zeros before 5 are placeholders, not significant. The number has 3 significant figures (5, 0, 8). But the zero between 5 and 8 IS significant — it's trapped between non-zero digits.

> [!warning] Trailing zeros: context matters
> $2500$ could be 2 s.f. or 4 s.f. — you can't tell without context. This ambiguity is one reason standard form exists: $2.5 \times 10^3$ (2 s.f.) vs $2.500 \times 10^3$ (4 s.f.).

> [!info] Beyond syllabus — Rounding in programming
> Most programming languages give you three functions: `floor()` (always round down), `ceil()` (always round up), and `round()` — but `round()` sometimes behaves unexpectedly (Python's "banker's rounding" rounds 0.5 to the nearest *even* number!).
>
> The classic trick: to round $x$ to the nearest integer using only `floor`, compute `floor(x + 0.5)`. This uses floor, not truncation, and sends exact halfway ties towards positive infinity. It is not Python’s ties-to-even rule, nor a universal rule for negative halfway cases. For ceiling: `floor(x) + 1` if $x$ is not already an integer, or just `ceil(x)`.
>
> Full details and worked examples in [[Upper and Lower Bounds#3. Truncation vs Rounding — A Crucial Distinction|Upper and Lower Bounds]].

## Exam Notes

### Cambridge 0580 (Core and Extended)
**Syllabus ref:** C1.9 and E1.9, Estimation: round to a specified degree of accuracy, "includes decimal places and significant figures", and round an answer sensibly for its context. The standing instruction on every paper is stricter than most candidates notice: non-exact answers are to be given "correct to 3 significant figures, or 1 decimal place for angles in degrees", unless the question says otherwise, and "to earn accuracy marks, candidates should avoid rounding figures until they have their final answer". Rounding early is the most avoidable way to lose marks on the paper.

### OxAQA 9260
**Syllabus ref:** N11 (Core): round numbers and measures to an appropriate degree of accuracy, including decimal places and significant figures. The specification adds that students "should know not to round values during intermediate steps of a calculation".

### Where this is assumed, not examined
Cambridge 0606, 9709 and 9231 set no question on rounding as such, and each states its own accuracy rule on the front of the paper (usually 3 significant figures). The skill is assumed throughout.

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — need to compute before rounding
- **Leads to:** [[Estimation (Vocab)]] — choose a convenient precision to estimate at the scale the task needs
- **Leads to:** [[Upper and Lower Bounds]] — rounding creates error intervals
- **Parallel:** [[Standard Form (Vocab)]] — s.f. and standard form often appear together

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\approx$ | `\approx` | "Approximately equal to" |
