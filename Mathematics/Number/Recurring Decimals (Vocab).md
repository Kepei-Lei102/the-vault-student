---
chinese: 循环小数 (xúnhuán xiǎoshù)
prerequisites:
  - "[[Decimals (Vocab)]]"
  - "[[Fractions (Vocab)]]"
  - "[[Linear Equations (Vocab)]]"
leads_to:
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Number Sets (Vocab)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE-extension
  - level/A-Level
  - curriculum/Cambridge-0580
  - syllabus/0580-E1-4
  - syllabus/9260-N12
  - type/vocabulary
  - type/technique
  - notation/recurring-decimal
  - misconception/0.999-vs-1
---

# Recurring Decimals 循环小数

## Definition

A **recurring decimal** (also called a *repeating decimal*) is a decimal whose digits eventually settle into a *repeating block* and continue that block forever:

$$\tfrac{1}{3} = 0.333\ldots = 0.\overline{3}, \qquad \tfrac{1}{7} = 0.\overline{142857}, \qquad \tfrac{5}{6} = 0.8\overline{3}.$$

The bar (or dots in UK convention) marks the **repeating block** — the sequence of digits that cycles forever. The block can start *immediately* after the decimal point (a *purely repeating* decimal) or after a few non-repeating digits (a *mixed* recurring decimal, like $0.8\overline{3}$).

**Key fact:** every recurring decimal is a *rational* number — it equals $p/q$ for some integers — and the conversion is done by the **"$10x - x$" trick**.

### 中文锚点

**循环小数 (xúnhuán xiǎoshù)** = 数字到某一位后出现重复模式，永远循环下去。

记号：

| 写法 | 例 |
|---|---|
| **横线** (英美主流) | $0.\overline{3}$ — 整体加横线表示循环节 |
| **小圆点** (英国传统) | $0.\dot{3}$ — 在循环节首末打点 |

每个循环小数 = 有理数（即可写成 $p/q$）。**"$10x-x$" 技巧**把循环小数变成分数。

著名等式：$0.\overline{9} = 1$（不是"接近 1"，是**等于** 1）。

---

## The "10x − x" Conversion Trick

The technique that turns *any* recurring decimal into a fraction. The shift-and-subtract idea: multiply by a power of 10 to align the repeating blocks, then subtract to *cancel* the infinitely-repeating tail.

### Example 1 — purely repeating

> Convert $0.\overline{3}$ to a fraction.

Let $x = 0.\overline{3} = 0.333\ldots$.

Multiply by $10$ (one digit in the repeat): $10x = 3.333\ldots = 3.\overline{3}$.

Subtract: $10x - x = 3.\overline{3} - 0.\overline{3}$. The infinitely-repeating tail cancels exactly:

$$9x = 3 \;\;\Longrightarrow\;\; x = \tfrac{3}{9} = \tfrac{1}{3}. \;\checkmark$$

### Example 2 — two-digit repeating block

> Convert $0.\overline{72}$ to a fraction.

Let $x = 0.\overline{72} = 0.727272\ldots$.

Multiply by $100$ (two digits in the repeat): $100x = 72.\overline{72}$.

Subtract: $100x - x = 99x = 72$, so $x = \tfrac{72}{99} = \tfrac{8}{11}$.

> [!tip] Multiply by $10^k$ where $k$ = length of repeat
> One digit cycle ($0.\overline{3}$) → multiply by $10$. Two-digit cycle ($0.\overline{72}$) → multiply by $100$. $k$-digit cycle → multiply by $10^k$. The shift exactly aligns the repeat with itself, so subtraction cancels the infinite tail.

### Example 3 — mixed (non-repeating prefix)

> Convert $0.1\overline{6}$ to a fraction.

Let $x = 0.1\overline{6} = 0.16666\ldots$.

The repeating block has length $1$, but it's offset by *one* non-repeating digit. Two-step trick:
- $10x = 1.\overline{6}$ (shift to push the repeat against the decimal point)
- $100x = 16.\overline{6}$ (shift one more, to align the two repeats)

Subtract: $100x - 10x = 90x = 16.\overline{6} - 1.\overline{6} = 15$.

$$x = \tfrac{15}{90} = \tfrac{1}{6}.$$

(Check: $1/6 = 0.16666\ldots$ ✓)

> [!info] The general formula
> For $0.\overline{d_1 d_2 \ldots d_k}$ (purely repeating, $k$-digit block): the value is $\dfrac{d_1 d_2 \ldots d_k}{\underbrace{99\ldots9}_{k\text{ nines}}}$.
>
> So $0.\overline{3} = \tfrac{3}{9}$, $0.\overline{72} = \tfrac{72}{99}$, $0.\overline{142857} = \tfrac{142857}{999999} = \tfrac{1}{7}$. The denominator is *all 9s*, one nine per repeating digit. Beautiful.

---

## $0.\overline{9} = 1$ — the famous one

Apply the trick to $0.\overline{9}$:

Let $x = 0.\overline{9}$. Then $10x = 9.\overline{9}$. Subtract: $9x = 9$, so $x = 1$.

**$0.\overline{9} = 1$ exactly.** Not "approximately." The two notations represent the *same number*.

> [!info] This is real — and three other proofs of the same fact
> $0.\overline{9} = 1$ unsettles students because the decimal "looks like" it's missing something. Three other proofs:
>
> 1. **Fraction trick.** $\tfrac{1}{3} = 0.\overline{3}$. Multiply both sides by 3: $1 = 0.\overline{9}$.
> 2. **Geometric series.** $0.\overline{9} = 0.9 + 0.09 + 0.009 + \ldots = \dfrac{0.9}{1 - 0.1} = \dfrac{0.9}{0.9} = 1$. (See [[Arithmetic and Geometric Progressions]] §sum to infinity.)
> 3. **Real numbers axiomatically.** If $0.\overline{9} \ne 1$, what's the difference? Whatever it is, it must be smaller than every $10^{-n}$ (since the difference is less than $10^{-n}$ at every truncation step). The only non-negative real less than every $10^{-n}$ is $0$. So the difference is $0$ — they're equal.
>
> The decimal $0.\overline{9}$ is just an unusual *name* for the number $1$, like $\frac{4}{4}$ or $2 - 1$ or $\sin(\pi/2)$. In real-number arithmetic, it *is* $1$.

---

## Common Mistakes

1. **Treating $0.\overline{9}$ as "less than 1."** It equals $1$ exactly — proven above.
2. **Wrong multiplier for mixed recurring decimals.** $0.1\overline{6}$ needs *two* multiplications (by $10$ and by $100$), not just one. The $10$ pushes past the non-repeating prefix; the $100$ aligns the repeat.
3. **Forgetting to simplify.** $0.\overline{3} = \tfrac{3}{9}$ is correct but not in lowest terms; reduce to $\tfrac{1}{3}$.
4. **Counting repeat length wrong.** $0.123\overline{45}$ has a *2-digit* repeating block (the "$45$"), so multiply by $100$ to align — *not* $1000$.

---

## Exam Notes

### Cambridge 0580 (Extended)

**Syllabus ref:** E1.4 Extended — convert recurring decimals to fractions. Standard patterns:

- "Show that $0.\overline{45} = \dfrac{5}{11}$." (Apply $10x - x$ technique.)
- "Convert $0.4\overline{1}$ to a fraction in lowest terms."
- "Without a calculator, evaluate $0.\overline{3} + 0.\overline{6}$." (Convert each to $\tfrac{1}{3}$ and $\tfrac{2}{3}$, sum to $1 = 0.\overline{9}$.)

### A-Level / IB

A-Level builds on this with the formal sum-to-infinity treatment of geometric series — see [[Arithmetic and Geometric Progressions]]. Recurring decimals are the simplest non-trivial geometric series: $0.\overline{3} = \sum_{n=1}^{\infty} 3 \cdot 10^{-n}$, a GP with first term $0.3$ and common ratio $0.1$.

---

## Connections

- **Prerequisite:** [[Decimals (Vocab)]] — basic place-value reading
- **Prerequisite:** [[Linear Equations (Vocab)]] — the algebra of "let $x = \ldots$, then ..."
- **Sibling:** [[Number Sets (Vocab)]] — recurring decimals are exactly the rationals (so this card *proves* part of $\mathbb{Q}$'s decimal characterisation)
- **Forward:** [[Arithmetic and Geometric Progressions]] — the "sum to infinity" formula explains the trick at A-Level depth
- **Beyond syllabus:** *p-adic numbers* — a different "completion" of $\mathbb{Q}$ where infinite-to-the-left decimals make sense; recurring patterns appear there too with completely different meaning

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $0.\overline{3}$ | `0.\overline{3}` | bar notation (preferred internationally) |
| $0.\dot{3}$ | `0.\dot{3}` | dot notation (UK style) |
| $0.\overline{142857}$ | `0.\overline{142857}` | $1/7$, six-digit repeat |
| $0.1\overline{6}$ | `0.1\overline{6}` | mixed recurring with one non-repeating prefix digit |
