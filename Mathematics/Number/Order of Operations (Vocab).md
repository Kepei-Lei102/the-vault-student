---
chinese: 运算顺序 (yùnsuàn shùnxù)
prerequisites:
  - "[[Four Operations (Vocab)]]"
leads_to:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Calculator Skills (Vocab)]]"
  - "[[Casio fx-991 Reference]]"
  - "[[TI-84 CE Reference]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-N2
  - syllabus/9260-N3
  - syllabus/0580-E1-6
  - type/vocabulary
  - misconception/left-to-right-always
---

# Order of Operations 运算顺序

## Definition

The **order of operations** is the agreed set of rules that determines which calculations to perform first in an expression. Without these rules, $2 + 3 \times 4$ would be ambiguous.

### 中文锚点

运算顺序：先括号，再指数，然后乘除（从左到右），最后加减（从左到右）。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| BIDMAS | — | **B**rackets, **I**ndices, **D**ivision, **M**ultiplication, **A**ddition, **S**ubtraction |
| BODMAS | — | Same as BIDMAS; **O**rders = **I**ndices |
| PEMDAS | — | American version: **P**arentheses, **E**xponents, **M**D, **A**S |
| brackets / parentheses | 括号 (kuòhào) | Calculated first; $(2 + 3) \times 4 = 20$ |
| indices / exponents | 指数 (zhǐshù) | Powers: $2^3 = 8$; calculated after brackets |
| precedence | 优先级 (yōuxiān jí) | Which operation "wins" when there's no bracket |
| evaluate | 求值 (qiú zhí) | "Evaluate $3 + 2^2 \times 5$" = calculate following the rules |

> [!warning] Common trap — "MD" and "AS" are equal priority
> BIDMAS does **not** mean division comes before multiplication. D and M have equal precedence — work left to right. Same for A and S. So $8 \div 4 \times 2 = 2 \times 2 = 4$, not $8 \div 8 = 1$.

> [!warning] Implied parentheses — invisible brackets you must see
> 🟢<(-\_-)> *"Hidden, the brackets are. See them, you must."* — Yoda, probably
>
> Some notation contains **hidden brackets** that BIDMAS doesn't show you:
>
> - **Fraction bars:** $\dfrac{3 + 4}{2}$ means $(3 + 4) \div 2$, not $3 + 4 \div 2$. The fraction bar groups the entire numerator and denominator — it IS a pair of brackets.
> - **Exponents:** $2^{3+1}$ means $2^{(3+1)}$. Everything in the superscript is grouped.
> - **Square roots:** $\sqrt{9 + 16}$ means $\sqrt{(9+16)} = 5$, not $\sqrt{9} + 16 = 19$.
> - **Function notation:** $f(x+1)$ means "evaluate $f$ at the input $(x+1)$" — the parentheses group the input. See [[Composite Function]] for how $fg(x) = f(g(x))$, where $g(x)$ must be evaluated first (inner brackets).
>
> All of these create grouping that acts like brackets even though no $( \ )$ is written. Train yourself to see them.

## Exam Notes

### OxAQA 9260
**Syllabus ref:** N2–N3 — apply operations in correct order; use inverse operations.
Calculator questions still test this: students must enter expressions correctly.

### Cambridge 0580 Extended
**Syllabus ref:** E1.6 — order of operations including brackets and powers.
Paper 2 (non-calculator) relies heavily on correct manual application.

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — the operations being ordered
- **Leads to:** [[Algebraic Expressions (Vocab)]] — same rules apply to expressions with variables
- **Parallel:** [[Logic]] — precedence is a kind of grammar; $\lnot$ binds tighter than $\land$, just as indices bind tighter than multiplication

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $(\ )$ | `( )` | Parentheses / brackets |
| $[\ ]$ | `[ ]` | Square brackets (nested grouping) |
| $x^n$ | `x^n` | Index / exponent |
