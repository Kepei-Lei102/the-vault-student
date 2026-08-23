---
chinese: 代数表达式 (dàishù biǎodáshì)
prerequisites:
  - "[[Four Operations (Vocab)]]"
  - "[[Powers and Roots (Vocab)]]"
  - "[[Inverse Operations (Vocab)]]"
  - "[[Order of Operations (Vocab)]]"
leads_to:
  - "[[Collecting Like Terms (Vocab)]]"
  - "[[Expanding Brackets (Vocab)]]"
  - "[[Factorising (Vocab)]]"
  - "[[Linear Equations (Vocab)]]"
  - "[[Indices in Algebra (Vocab)]]"
  - "[[Algebraic Proof]]"
  - "[[Function]]"
  - "[[Remainder and Factor Theorems]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Sequences]]"
  - "[[Changing the Subject (Vocab)]]"
  - "[[Completing the Square]]"
  - "[[Linear Graphs (Vocab)]]"
  - "[[Linear Inequalities (Vocab)]]"
  - "[[Polynomial Division]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A1
  - syllabus/9260-A2
  - syllabus/9260-A3
  - syllabus/0580-E2-1
  - type/vocabulary
  - misconception/expression-vs-equation
---

# Algebraic Expressions 代数表达式

## Definition

An **algebraic expression** (代数表达式) is a combination of numbers, variables (letters), and operations — but **no equals sign**. For example, $3x + 2$ is an expression; $3x + 2 = 11$ is not (that's an equation).

### 中文锚点

代数表达式 = 用字母和数字组成的算式，没有等号。$3x^2 - 5x + 1$ 是表达式。加了等号就变成方程。

---

## The Big Four — Expression vs Equation vs Formula vs Identity

This distinction is a classic exam question at every level.

| English | 中文 | Has $=$ ? | Meaning | Example |
|---------|------|-----------|---------|---------|
| **expression** | 表达式 (biǎodáshì) | No | A calculation with letters | $3x + 2$ |
| **equation** | 方程 (fāngchéng) | Yes | True for **particular** value(s) of $x$ | $3x + 2 = 11$ |
| **formula** | 公式 (gōngshì) | Yes | Links **two or more** variables; describes a relationship | $A = \pi r^2$ |
| **identity** | 恒等式 (héngděngshì) | Yes ($\equiv$) | True for **all** values of the variable | $2(x+3) \equiv 2x + 6$ |

> [!tip] How to tell them apart in an exam
> **No equals sign?** → Expression. **Equals sign, one variable, specific solution?** → Equation. **Equals sign, multiple variables, describes a rule?** → Formula. **True for ALL values?** → Identity (use $\equiv$).

---

## Parts of an Expression

| English | 中文 | Meaning | In $5x^2 - 3x + 7$ |
|---------|------|---------|---------------------|
| **term** | 项 (xiàng) | A piece separated by $+$ or $-$ | Three terms: $5x^2$, $-3x$, $7$ |
| **coefficient** | 系数 (xìshù) | The number multiplying a variable | Coefficient of $x^2$ is $5$; of $x$ is $-3$ |
| **constant** | 常数 (chángshù) | A term with no variable | $7$ |
| **variable** | 变量 (biànliàng) | The letter(s) representing unknowns | $x$ |

> [!warning] "Coefficient of $x$" includes the sign
> In $5x^2 - 3x + 7$, the coefficient of $x$ is $-3$, not $3$. The minus sign belongs to the term.

---

## Substitution

To **substitute** (代入, dàirù) means to replace a variable with a number and evaluate.

If $x = 4$: $\quad 5x^2 - 3x + 7 = 5(16) - 3(4) + 7 = 80 - 12 + 7 = 75$

Common exam phrasing: "Find the value of … when $x = \ldots$" or "Evaluate … for $x = \ldots$"

---

## Exam Notes

### OxAQA 9260

**Syllabus ref:** A1–A3. Letters as generalised numbers, substitution — and, verbatim in A3 core content, "understand and use the concepts of expressions, equations, formulae, identities, inequalities, terms and factors": on this board the vocabulary distinction itself is directly examinable.

### Cambridge 0580 Extended

**Syllabus ref:** E2.1 (Introduction to algebra): know that letters represent generalised numbers, and substitute numbers into expressions and formulas. The expression/equation/formula/identity *distinction* is not named as an LO — the terms are simply used throughout the papers and assumed understood, which is exactly why the vocabulary is worth securing early.

### Where it is *not* examined

Never tested standalone beyond IGCSE: 0606, 9709, Edexcel IAL and OxAQA 9660 all assume this vocabulary from the first page.

---

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — the operations inside expressions
- **Prerequisite:** [[Powers and Roots (Vocab)]] — index notation in terms like $5x^2$
- **Leads to:** [[Collecting Like Terms (Vocab)]] — simplifying expressions
- **Leads to:** [[Expanding Brackets (Vocab)]] — removing brackets from expressions
- **Leads to:** [[Factorising (Vocab)]] — reverse of expanding
- **Leads to:** [[Algebraic Proof]] — expressions become the language of proof
- **Leads to:** [[Function]] — $f(x)$ is a named expression with a domain

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\equiv$ | `\equiv` | Identity symbol — "identically equal to" |
| $5x^2$ | `5x^2` | Coefficient × variable to a power |
