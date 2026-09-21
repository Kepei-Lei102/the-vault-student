---
chinese: 分数 (fēnshù)
prerequisites:
  - "[[Four Operations (Vocab)]]"
  - "[[Factors and Multiples (Vocab)]]"
leads_to:
  - "[[Percentages (Vocab)]]"
  - "[[Ratio (Vocab)]]"
  - "[[Algebraic Fractions (Vocab)]]"
  - "[[Surds]]"
  - "[[Similarity]]"
  - "[[Average Speed (Vocab)]]"
  - "[[Calculator Skills (Vocab)]]"
  - "[[Decimals (Vocab)]]"
  - "[[Percentage Calculations (Vocab)]]"
  - "[[Reciprocals (Vocab)]]"
  - "[[Recurring Decimals (Vocab)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-N12
  - syllabus/9260-N7
  - syllabus/0580-E1-6
  - syllabus/0580-E1-4
  - type/vocabulary
  - misconception/fraction-division
---

# Fractions 分数

## Definition

For a positive integer $b$, a **fraction** (分数) $\dfrac{a}{b}$ counts $a$ units of size $\dfrac1b$. It can exceed one whole: $\dfrac74$ counts seven quarter-units. More generally, $a/b$ denotes division, with $b\ne0$. The top number is the **numerator** (分子) and the bottom is the **denominator** (分母).

$$\dfrac{\text{numerator (分子)}}{\text{denominator (分母)}} = \dfrac{\text{how many parts}}{\text{how many equal parts per whole}}$$

### 中文锚点

一张披萨切成八块一样大的，你拿了三块。现在把每块都再切成两半，你手里变成六小块，整张披萨变成十六小块，可你并没有多拿一口。$\frac38$ 和 $\frac6{16}$ 说的是同一份：块数翻了一倍，每块也小了一半。分数记下的，正是你用多大的“一块”来数，以及数了多少块。

> [!warning] Reading order: English vs Chinese
> English reads **top first**: "three quarters" ($\frac{3}{4}$). Chinese reads **bottom first**: "四分之三" (sì fēn zhī sān) — literally "of four parts, three." This reversal catches bilingual students on listening tasks.

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| fraction | 分数 (fēnshù) | General term |
| numerator | 分子 (fēnzǐ) | Top number |
| denominator | 分母 (fēnmǔ) | Bottom number; literally "fraction mother" |
| proper fraction | 真分数 (zhēn fēnshù) | Numerator < denominator: $\dfrac{3}{5}$ |
| improper fraction | 假分数 (jiǎ fēnshù) | Numerator ≥ denominator: $\dfrac{7}{4}$ |
| mixed number | 带分数 (dài fēnshù) | Integer + fraction: $1\dfrac{3}{4}$ |
| equivalent fractions | 等值分数 | $\dfrac{2}{4} = \dfrac{1}{2}$ — same value, different form |
| simplify / cancel | 约分 (yuēfēn) | Divide numerator and denominator by their HCF |
| lowest terms / simplest form | 最简分数 | HCF of numerator and denominator is 1 |
| common denominator | 公分母 (gōng fēnmǔ) | Shared denominator for adding/subtracting |
| reciprocal | 倒数 (dàoshù) | Flip the fraction: reciprocal of $\dfrac{2}{3}$ is $\dfrac{3}{2}$ |
| convert | 转化 (zhuǎnhuà) | Between fractions, decimals, percentages |

## Key Operations

**Adding/Subtracting:** Find a common denominator, then add/subtract numerators.

$$\dfrac{2}{3} + \dfrac{1}{4} = \dfrac{8}{12} + \dfrac{3}{12} = \dfrac{11}{12}$$

**Multiplying:** Multiply numerators together, multiply denominators together.

$$\dfrac{2}{3} \times \dfrac{4}{5} = \dfrac{8}{15}$$

**Dividing — recover the missing multiplier.** Let $q=\dfrac23\div\dfrac45$. By the meaning of division, $q\times\dfrac45=\dfrac23$. Multiply **both sides of that equation** by $\dfrac54$:

$$q\times\underbrace{\dfrac45\times\dfrac54}_{1}=\dfrac23\times\dfrac54,
\qquad q=\dfrac{10}{12}=\dfrac56.$$

The reciprocal turns the divisor into $1$, leaving the unknown multiplier alone. This requires a nonzero divisor.

Once that reason is clear, the mnemonic is **K**eep, **F**lip, **C**hange — KFC, like the chicken restaurant 🍗: keep the first fraction, flip the second, change $\div$ to $\times$.

## Exam Notes

### OxAQA 9260
**N7 (Core and Extension)** requires exact calculation with fractions; **N12** covers equivalent fractions and conversion between fractions, terminating decimals and percentages. Conversion from recurring decimals is Extension content and is developed in [[Recurring Decimals (Vocab)]].

### Cambridge 0580 — Core and Extended
**C1.4 / E1.4** cover fraction notation, equivalent forms and conversion; **C1.5 / E1.5** cover ordering. The arithmetic itself belongs to **C1.6 / E1.6**, including improper fractions and mixed numbers. Fraction calculations can appear on both calculator and non-calculator papers. Read whether an answer must be a simplified fraction, a mixed number or a decimal.

### Other boards — assumed arithmetic
**Cambridge 0606 / 9709 / 9231, Edexcel IAL and OxAQA 9660** use numerical fraction arithmetic within algebra and later work, rather than prescribing it as a separate elementary unit. **IB AA / AI (first assessment 2021)** explicitly include fraction arithmetic in *Prior learning*. **AP Calculus AB / BC** assumes prior algebra, including rational functions; numerical fractions remain a working skill, with no standalone fraction-arithmetic unit. [[Algebraic Fractions (Vocab)]] and partial fractions add algebraic scope beyond these numerical rules.

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — add, subtract, multiply, divide
- **Prerequisite:** [[Factors and Multiples (Vocab)]] — HCF for simplifying, LCM for common denominator
- **Leads to:** [[Ratio (Vocab)]] — ratios are fractions in disguise
- **Leads to:** [[Algebraic Fractions (Vocab)]] — same rules but with algebra
- **Leads to:** [[Surds]] — rationalising denominators uses fraction manipulation
- **Parallel:** [[Laws of Indices]] — $a^{-1} = \dfrac{1}{a}$ is the reciprocal

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{a}{b}$ | `\dfrac{a}{b}` | Display fraction (always use `\dfrac`) |
| $1\dfrac{3}{4}$ | `1\dfrac{3}{4}` | Mixed number |
