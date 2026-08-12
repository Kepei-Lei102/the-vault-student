---
chinese: 因数与倍数 (yīnshù yǔ bèishù)
prerequisites:
  - "[[Four Operations (Vocab)]]"
leads_to:
  - "[[Prime Factorisation (Vocab)]]"
  - "[[Algebraic Fractions (Vocab)]]"
  - "[[Algebraic Proof]]"
  - "[[Factorising (Vocab)]]"
  - "[[Fractions (Vocab)]]"
  - "[[Laws of Indices]]"
  - "[[Number Sets (Vocab)]]"
  - "[[Ratio (Vocab)]]"
  - "[[Surds]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-N4
  - syllabus/0580-E1-1
  - type/vocabulary
  - misconception/factor-vs-multiple
---

# Factors and Multiples 因数与倍数

## Definition

A **factor** of $n$ is an integer that divides $n$ exactly (no remainder). A **multiple** of $n$ is the result of multiplying $n$ by any positive integer.

$$d \text{ is a factor of } n \iff n \div d \text{ has remainder } 0$$

### 中文锚点

因数：能整除 $n$ 的数。倍数：$n$ 乘以正整数的结果。因数往小找，倍数往大找。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| factor | 因数 (yīnshù) | 1, 2, 3, 4, 6, 12 are the factors of 12 |
| multiple | 倍数 (bèishù) | 5, 10, 15, 20, … are multiples of 5 |
| common factor | 公因数 (gōng yīnshù) | A factor shared by two or more numbers |
| common multiple | 公倍数 (gōng bèishù) | A multiple shared by two or more numbers |
| HCF (highest common factor) | 最大公因数 (zuìdà gōng yīnshù) | Largest factor shared; also called GCD |
| LCM (lowest common multiple) | 最小公倍数 (zuìxiǎo gōng bèishù) | Smallest positive multiple shared |
| divisible (by) | 能被…整除 | "$n$ is divisible by $d$" means $d$ is a factor of $n$ |
| divisor | 除数 (chúshù) | Same as factor in this context |

> [!tip] Finding HCF and LCM
> **Short method:** List factors or multiples. **Efficient method:** Use prime factorisation (see [[Prime Factorisation (Vocab)]]). HCF = product of shared primes (lowest powers). LCM = product of all primes (highest powers). There is also a useful identity: $\text{HCF}(a,b) \times \text{LCM}(a,b) = a \times b$.

## Exam Notes

### OxAQA 9260
**Syllabus ref:** N4 — identify and use HCF/LCM; use prime factorisation to find them.

### Cambridge 0580 Extended
**Syllabus ref:** E1.1 — HCF and LCM, including by prime factorisation.

> [!warning] Exam phrasing trap
> "Find the **highest** common factor" — students sometimes give a common factor that isn't the highest. Always check you've found the largest one.

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — division and multiplication
- **Leads to:** [[Prime Factorisation (Vocab)]] — systematic way to find all factors
- **Used in:** [[Algebraic Fractions (Vocab)]] — simplifying fractions = dividing by HCF
- **Parallel:** [[Cardinality]] — HCF/LCM problems often combine with Venn diagrams

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\lvert$ | `\mid` | "Divides": $3 \mid 12$ means 3 is a factor of 12 |
| $\nmid$ | `\nmid` | "Does not divide": $5 \nmid 12$ |
