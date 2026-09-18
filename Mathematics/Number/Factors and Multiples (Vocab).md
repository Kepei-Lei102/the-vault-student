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

**N4, Core:** identify and use factors/divisors, multiples, common factors/multiples, HCF, LCM and prime factorisation, including product notation. The specification's note explicitly includes prime factors written in index form. These are not Extension-only requirements.

### Cambridge 0580 Core and Extended

**C1.1 / E1.1:** both tiers include common factors/multiples and tasks finding the HCF or LCM of two numbers, as well as prime factorisation. Typical work: express a number as prime factors, choose the shared smallest powers for HCF or the union of greatest powers for LCM, and interpret the result in context. “Common factor” alone does not answer a request for the **highest** one.

### Beyond IGCSE

**0606:** IGCSE mathematics is assumed; inherited content not separately listed is not tested directly, though it may be needed inside another topic (the syllabus's §3 preamble). **9709 / 9231:** factor arithmetic is prerequisite knowledge, not a standalone HCF/LCM topic. The tracked IAL/9660 and AP Calculus maps likewise have algebraic factorisation rather than standalone HCF/LCM rows. For IB AA/AI and AP Statistics, use this as prerequisite arithmetic support; detailed current-guide placement has not been verified here. Euclid's algorithm and number-theoretic proofs are further topics, not implied requirements of the two IGCSE rows above.

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
