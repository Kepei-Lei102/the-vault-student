---
chinese: 小数 (xiǎoshù)
prerequisites:
  - "[[Fractions (Vocab)]]"
  - "[[Number Sets (Vocab)]]"
leads_to:
  - "[[Recurring Decimals (Vocab)]]"
  - "[[Standard Form (Vocab)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E1-4
  - syllabus/9260-N12
  - type/vocabulary
  - notation/decimal-point
  - misconception/place-value
---

# Decimals 小数

## Definition

A **decimal** is a number written using the **decimal point** to extend place value below 1. The digits to the *left* of the decimal point are the integer part; the digits to the *right* represent fractional parts that get smaller as you move right.

For $235.467$:

| Place | Hundreds | Tens | Units | . | Tenths | Hundredths | Thousandths |
|---|---|---|---|---|---|---|---|
| Power of 10 | $10^2$ | $10^1$ | $10^0$ | | $10^{-1}$ | $10^{-2}$ | $10^{-3}$ |
| Digit | $2$ | $3$ | $5$ | | $4$ | $6$ | $7$ |

So $235.467 = 200 + 30 + 5 + 0.4 + 0.06 + 0.007$. Each step right divides place value by 10.

A decimal is **terminating** if it ends after a finite number of digits (e.g. $0.25$). A decimal is **recurring** if a digit-pattern repeats forever (e.g. $0.\overline{3} = 0.333\ldots$). Both are *rational* — see [[Recurring Decimals (Vocab)]] for the conversion trick.

### 中文锚点

**小数 (xiǎoshù)** = decimal number. **小数点 (xiǎoshùdiǎn)** = decimal point.

| 中文 | English | 例 |
|---|---|---|
| 整数部分 (zhěngshù bùfèn) | integer part | $235$ in $235.467$ |
| 小数部分 (xiǎoshù bùfèn) | decimal part | $.467$ in $235.467$ |
| 十分位 (shí fēn wèi) | tenths place | first digit after decimal |
| 百分位 (bǎi fēn wèi) | hundredths place | second digit after |
| 千分位 (qiān fēn wèi) | thousandths place | third digit after |
| 有限小数 (yǒuxiàn xiǎoshù) | terminating decimal | $0.25$ |
| 无限小数 (wúxiàn xiǎoshù) | non-terminating decimal | $0.333\ldots$ or $\pi$ |
| 循环小数 (xúnhuán xiǎoshù) | recurring (repeating) decimal | $0.\overline{142857}$ |

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| decimal point | 小数点 | the dot separating integer from fractional part |
| place value | 数位 (shùwèi) | the value contributed by a digit's position |
| decimal place (d.p.) | 小数位 (xiǎoshù wèi) | digit count *after* the point; "$3.14159$ to 2 d.p." = $3.14$ |
| significant figure (s.f.) | 有效数字 | counts digits *from the first non-zero*; "$3.14159$ to 3 s.f." = $3.14$ |
| terminating decimal | 有限小数 | finite digits after the point |
| recurring / repeating decimal | 循环小数 | digits eventually repeat forever |
| rounding | 四舍五入 (sìshě wǔrù) | adjust to the nearest place value (5 rounds up) |

> [!info] Decimal place vs significant figure — different counts
> "$0.00305$" — to **2 d.p.** is $0.00$ (decimal places counted from the point), to **2 s.f.** is $0.0031$ (significant figures counted from the first non-zero digit). Two completely different operations on the same number. Always read the question carefully — Cambridge papers ask for one or the other, not both.

> [!info] "Decimal" vs "denary" vs "binary" — same digits, different meanings
> A **decimal** is a number written in **base 10** — using ten digits ($0$–$9$) and place values that are powers of ten ($\ldots, 100, 10, 1, \tfrac{1}{10}, \tfrac{1}{100}, \ldots$). The British call this **denary** when they want to be unambiguous; *denary* and *decimal* mean the same thing as a number system. ("Denary" is mostly British/Commonwealth — the US almost always says "decimal" or "base 10". British computer-science texts and exam papers use "denary" specifically to distinguish the *number system* from "decimal" in the everyday sense of "the digits after the dot".)
>
> The same character set — digits and a "." — can mean something *completely different* in **binary** (base 2). In binary you only have two digits, $0$ and $1$, and place values are powers of *two*:
>
> $$101.011_2 \;=\; 1\cdot 4 + 0\cdot 2 + 1\cdot 1 + 0\cdot\tfrac{1}{2} + 1\cdot\tfrac{1}{4} + 1\cdot\tfrac{1}{8} \;=\; 5.375_{10}.$$
>
> The "$.$" is a *radix point* — same dot, but it separates "ones place" from "halves place" (rather than tenths place). The string "$101.011$" looks decimal but means $5.375$ in our usual base-10 reading. Subscripts ($_2$ vs $_{10}$) are the standard way to disambiguate in writing.
>
> Computers store numbers in binary. Every floating-point number on your laptop, every pixel value in an image, every bit of every WiFi packet is "decimal in base 2." The fact that the same notation works in any base is why mathematicians sometimes prefer "denary" — it makes clear we mean the *base*, not the *notation*.

---

## Worked Examples

### Converting fraction to decimal

> Express $\dfrac{3}{8}$ as a decimal.

Long division: $3 \div 8 = 0.375$. Terminating, because the denominator $8 = 2^3$ has only the prime factor $2$.

> [!tip] Which fractions terminate?
> A fraction in lowest terms gives a *terminating* decimal **if and only if** its denominator's prime factors are only $2$ and/or $5$. Otherwise it recurs. $\tfrac{3}{8}$ terminates ($8 = 2^3$). $\tfrac{1}{6}$ recurs ($6 = 2 \times 3$, the $3$ forces recurrence). $\tfrac{1}{7}$ recurs ($7$ has no $2$s or $5$s at all). The "decimal-friendliness" of a fraction is decided entirely by its denominator's prime factorisation.

### Reading place value

> What is the value of the digit $7$ in $24.071$?

Position: third digit after the point → **thousandths**. Value: $\dfrac{7}{1000} = 0.007$.

### Comparing decimals

> Which is larger: $0.42$ or $0.418$?

Compare digit by digit from the *left*: tenths match ($4 = 4$), hundredths $2 > 1$. So $0.42 > 0.418$.

> [!warning] Don't compare by digit count
> $0.42$ has 2 decimal places, $0.418$ has 3 — but $0.42 > 0.418$. *More digits doesn't mean larger.* Pad with trailing zeros if it helps: $0.420$ vs $0.418$ → $420 > 418$ → $0.42 > 0.418$.

---

## Common Mistakes

1. **"Longer decimal = larger".** $0.42 > 0.418$ even though $0.418$ has more digits. Pad and compare.
2. **Decimal places vs significant figures.** Distinct concepts; read the question.
3. **Rounding errors.** "Round to 2 d.p." means look at the *3rd* decimal digit. $0.345 \to 0.35$ (round up because of the $5$).
4. **Place-value drift.** Forgetting that the digit *just after* the point is *tenths* not *hundredths*; off-by-one errors are common.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E1.4 (Fractions, Decimals and Percentages) — order quantities by magnitude; convert between fractions, decimals, and percentages. Standard patterns:

- "Convert $\dfrac{5}{8}$ to a decimal."
- "Round $7.4592$ to (a) 2 decimal places (b) 3 significant figures."
- "Place these in ascending order: $0.5, \dfrac{7}{16}, 47\%, 0.493$."

---

## Connections

- **Prerequisite:** [[Fractions (Vocab)]] — decimals are place-value fractions of $10^k$
- **Sibling:** [[Recurring Decimals (Vocab)]] — when a decimal *doesn't* terminate
- **Forward:** [[Standard Form (Vocab)]] — scientific notation for very large / very small decimals
- **Forward:** [[Rounding (Vocab)]] — the rules for d.p. vs s.f.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $0.\overline{3}$ | `0.\overline{3}` | recurring decimal |
| $0.\dot{3}$ | `0.\dot{3}` | dot notation (UK convention) |
| d.p. | `d.p.` | decimal places |
| s.f. | `s.f.` | significant figures |
