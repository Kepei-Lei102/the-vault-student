---
chinese: 展开括号 (zhǎnkāi kuòhào)
prerequisites:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Collecting Like Terms (Vocab)]]"
leads_to:
  - "[[Factorising (Vocab)]]"
  - "[[Linear Equations (Vocab)]]"
  - "[[Algebraic Fractions (Vocab)]]"
  - "[[Algebraic Proof]]"
  - "[[Binomial Theorem]]"
  - "[[Remainder and Factor Theorems]]"
  - "[[Completing the Square]]"
  - "[[Polynomial Division]]"
  - "[[Quadratic Equations]]"
  - "[[Simultaneous Equations (Vocab)]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A4
  - syllabus/0580-E2-2
  - type/vocabulary
  - misconception/sign-errors-expanding
---

# Expanding Brackets 展开括号

## Definition

To **expand** (展开) means to remove brackets by multiplying every term inside the bracket by the term outside (single bracket) or by every term in the other bracket (double bracket). The formal name is the **distributive law** (分配律).

### 中文锚点

给三个人买同样的午餐，每份都有一个三明治和一杯饮料。如果没有套餐优惠，算三份午餐的钱，和分别算三个三明治、三杯饮料的钱，结果一样。把一份拆开算，只是换了分组，饮料并没有少买。所以括号外的“3”要照顾到里面的每一项，不能只乘三明治、把饮料落下。这就是展开括号背后的分配律。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| expand | 展开 (zhǎnkāi) | Remove brackets by multiplying |
| distribute | 分配 (fēnpèi) | Spread the multiplier across every term |
| distributive law | 分配律 (fēnpèi lǜ) | $a(b + c) = ab + ac$ |
| double brackets | 双括号 | $(x + a)(x + b)$ — multiply every pair |
| FOIL | — | **F**irst, **O**uter, **I**nner, **L**ast — a mnemonic for double brackets |
| product | 乘积 (chéngjī) | The result of multiplying |

---

## WHY — The Distributive Law

$$a(b + c) = ab + ac$$

**Why it works for a nonnegative integer multiplier:** $a$ copies of $(b + c)$ means $a$ copies of $b$ plus $a$ copies of $c$. Think of $3 \times 12 = 3 \times (10 + 2) = 30 + 6 = 36$ — you already use distribution with numbers. The same distributive law applies to real algebraic quantities; the repeated-copy picture is its whole-number starting point.

---

## Patterns

**Trigger: a multiplier acts on a whole sum. Tool: distribute to every term.**

**Single bracket:** $\quad 3(2x - 5) = 6x - 15$

**Trigger: each term in one sum multiplies the entire other sum. Tool: distribute twice, then collect like terms.**

**Double bracket:** $\quad (x + 3)(x - 2) = x^2 - 2x + 3x - 6 = x^2 + x - 6$

**Squaring a bracket:** $\quad (x + a)^2 = x^2 + 2ax + a^2$

> [!warning] $(x + a)^2 \neq x^2 + a^2$
> This is one of the most common algebra mistakes at every level. The middle term $2ax$ must not be forgotten. Try $x = 3$, $a = 4$: $(3+4)^2 = 49$ but $9 + 16 = 25$. Not the same.

**Difference of two squares:** $\quad (a + b)(a - b) = a^2 - b^2$

The middle terms cancel: $ab - ab = 0$. This identity is used constantly in factorising and in [[Surds]] (conjugate pairs).

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** C2.2 / E2.2 — "expand products of algebraic expressions". Core stops at single brackets and two brackets in one variable, e.g. $(2x+1)(x-4)$; **Extended adds products of more than two brackets**, e.g. $(x-2)(x+3)(2x+1)$ — expand two, then multiply the result by the third. It also supports equations, proof and simplification. The instruction "Expand and simplify" means expand, then collect like terms.

### OxAQA 9260

**Syllabus ref:** A4 — expanding up to two linear expressions; the Extension tier adds products of **two or three binomials** (the Pascal's-triangle shortcut for repeated brackets lives with [[Binomial Theorem]]).

### Cambridge 0606 / 9709 / 9231

0606 §2.4 and 9709 §1.1 explicitly include factorisation as a method for solving quadratics. Expanding and collecting terms support those manipulations; 9709 §1.5 separately examines binomial expansion. 9231 assumes the relevant 9709 pure content. These syllabuses do not justify a claim that a basic algebra step can never be asked on its own.

### Edexcel IAL / OxfordAQA 9660

Edexcel IAL P1 §1.10 explicitly includes expanding brackets, collecting like terms and factorising polynomials up to degree three; P1 §1.5 includes quadratic solution by factorisation. OxfordAQA 9660 P1.1 likewise names polynomial manipulation and quadratic factorisation. These are examinable algebra, not merely optional background.

### IB AA / AI and AP Calculus

The IB AA and AI guides for first assessment 2021 list expansion and factorisation under **prior learning**, which examination questions may assume. [IB AA guide, prior learning](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-analysis-approaches-guide.pdf); [IB AI guide, prior learning](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-applications-interpretation-guide.pdf).

AP Calculus AB/BC assumes fluent algebra; Topic 1.6 uses algebraic manipulation for limits, including factoring and cancellation with domain awareness. **Scope boundary:** elementary expansion/factorisation is not a separate new unit in those IB/AP courses; its assumed status does not make it unassessable. No marks or question frequency are implied here.

---

## Connections

- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — terms, coefficients, variables
- **Prerequisite:** [[Collecting Like Terms (Vocab)]] — simplify after expanding
- **Leads to:** [[Factorising (Vocab)]] — the reverse process
- **Leads to:** [[Algebraic Proof]] — expanding is the core "Transform" move
- **Leads to:** [[Binomial Theorem]] — generalises $(a + b)^n$ for any $n$
- **Parallel:** [[Surds]] — difference of two squares rationalises $(\sqrt{a} + b)(\sqrt{a} - b)$
