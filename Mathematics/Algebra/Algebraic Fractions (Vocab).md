---
chinese: 代数分式 (dàishù fēnshì)
prerequisites:
  - "[[Fractions (Vocab)]]"
  - "[[Factorising (Vocab)]]"
  - "[[Expanding Brackets (Vocab)]]"
  - "[[Indices in Algebra (Vocab)]]"
  - "[[Factors and Multiples (Vocab)]]"
  - "[[Reciprocals (Vocab)]]"
leads_to:
  - "[[Remainder and Factor Theorems]]"
  - "[[Fractional Equations (Vocab)]]"
  - "[[Integration]]"
  - "[[Partial Fractions]]"
  - "[[Polynomial Division]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/0580-E2-3
  - syllabus/9260-A7
  - type/vocabulary
  - misconception/cancelling-terms-not-factors
  - misconception/wrong-common-denominator
---

# Algebraic Fractions 代数分式

## Definition

An **algebraic fraction** (代数分式) is a fraction whose numerator and/or denominator contains one or more variables:

$$\dfrac{3x}{2} \qquad \dfrac{1}{x+2} \qquad \dfrac{x^2 - 4}{x^2 + 5x + 6}$$

Every technique you already use on [[Fractions (Vocab)|numerical fractions]] — simplifying by cancelling, finding a common denominator, multiplying straight across — works here too. The twist: before you can cancel, you usually have to [[Factorising (Vocab)|factorise]] the top and the bottom.

### 中文锚点

代数分式 = 分子或分母里有字母的分数。核心口诀：**先因式分解，再约分**。只能约分公因式（common factors），不能约分独立的项（separate terms）。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| **algebraic fraction** | 代数分式 (dàishù fēnshì) | Fraction with variables |
| **numerator** | 分子 (fēnzǐ) | The top |
| **denominator** | 分母 (fēnmǔ) | The bottom |
| **common factor** | 公因式 (gōngyīnshì) | A factor appearing in BOTH top and bottom |
| **cancel** | 约分 (yuēfēn) | Divide top and bottom by the same factor |
| **common denominator** | 公分母 (gōngfēnmǔ) | A single denominator that both fractions can use |
| **LCM (lowest common multiple)** | 最小公倍数 (zuìxiǎo gōngbèishù) | The smallest common denominator |
| **improper** | 假分式 | Degree of numerator $\geq$ degree of denominator |
| **proper** | 真分式 | Degree of numerator $<$ degree of denominator |
| **restriction** | 限制 (xiànzhì) | Values of $x$ that make the denominator zero — excluded |

---

## Simplifying — Factorise First, Then Cancel

**The two-step rule:** (1) factorise top and bottom fully; (2) cancel only *common factors*.

$$\dfrac{x^2 - 4}{x^2 + 5x + 6} = \dfrac{(x-2)(x+2)}{(x+2)(x+3)} = \dfrac{x-2}{x+3}$$

The $(x+2)$ is a **common factor** of numerator and denominator, so it cancels. The result is valid *except* at $x = -2$ (where the original was $\tfrac{0}{0}$) and $x = -3$ (where both versions are undefined).

> [!warning] Only cancel FACTORS, never separate TERMS
> $\dfrac{x + 3}{x + 5}$ does **NOT** simplify to $\dfrac{3}{5}$ by "cancelling the $x$'s." The $x$ is added, not multiplied — so it's not a common factor. Try $x = 2$: $\dfrac{5}{7} \neq \dfrac{3}{5}$.
>
> You can only cancel what is a factor of the *entire* top AND the *entire* bottom.

---

## Adding and Subtracting — Find a Common Denominator

Same idea as numerical fractions: rewrite with a common denominator, then combine numerators.

**Example 1 — simple:**
$$\dfrac{2}{x} + \dfrac{3}{y} = \dfrac{2y}{xy} + \dfrac{3x}{xy} = \dfrac{2y + 3x}{xy}$$

**Example 2 — factorise first:**
$$\dfrac{1}{x - 2} + \dfrac{1}{x^2 - 4}$$

Factorise the second denominator: $x^2 - 4 = (x-2)(x+2)$. So LCM of denominators $= (x-2)(x+2)$.

$$= \dfrac{x+2}{(x-2)(x+2)} + \dfrac{1}{(x-2)(x+2)} = \dfrac{x+3}{(x-2)(x+2)}$$

> [!warning] The LCM of $(x-2)$ and $(x+2)$ is NOT $x^2 - 4x + 4$
> Common mistake: multiplying the two denominators without checking if they share a factor. Here $(x-2)$ and $(x+2)$ are coprime (no common factor), so the LCM is their product $(x-2)(x+2) = x^2 - 4$. Always factorise first and take only what's actually needed.

---

## Multiplying and Dividing

**Multiplying:** factorise everything, cancel common factors across the whole expression, then multiply what's left.

$$\dfrac{x^2 - 1}{x + 3} \cdot \dfrac{x + 3}{x - 1} = \dfrac{(x-1)(x+1)}{(x+3)} \cdot \dfrac{(x+3)}{(x-1)} = x + 1$$

**Dividing:** flip the second fraction and multiply (same rule as numerical fractions).

$$\dfrac{x^2 - 9}{x} \div \dfrac{x - 3}{2x} = \dfrac{(x-3)(x+3)}{x} \cdot \dfrac{2x}{(x-3)} = 2(x+3)$$

---

## Restrictions — The Hidden Footnote

Every time a variable sits in a denominator, there are **excluded values** — the values of $x$ that make the denominator zero.

For $\dfrac{x+1}{(x-2)(x+3)}$: the function is undefined at $x = 2$ and $x = -3$.

Exam questions rarely ask for these explicitly at IGCSE level, but they matter in [[Function|function]] work (domain restrictions) and in calculus (vertical asymptotes).

---

## Solving Equations with Algebraic Fractions

The trick: **multiply both sides by the LCM of the denominators** to clear fractions, then solve the resulting [[Linear Equations (Vocab)|linear]] or [[Quadratic Equations|quadratic]] equation.

$$\dfrac{2}{x-1} + \dfrac{3}{x+2} = 1$$

Multiply by $(x-1)(x+2)$:
$$2(x+2) + 3(x-1) = (x-1)(x+2)$$
$$2x + 4 + 3x - 3 = x^2 + x - 2$$
$$5x + 1 = x^2 + x - 2 \;\Rightarrow\; x^2 - 4x - 3 = 0$$

Solve by the [[Quadratic Equations|quadratic formula]]: $x = 2 \pm \sqrt{7}$. (Both valid — check neither makes a denominator zero.)

---

## Exam Phrasing

- "**Simplify** $\dfrac{x^2 + 5x + 6}{x^2 - 9}$" — factorise, cancel
- "**Write as a single fraction**" — find common denominator, combine
- "**Express in its simplest form**" — fully factorise and cancel all common factors
- "**Solve** $\dfrac{1}{x} + \dfrac{1}{x+1} = \dfrac{1}{2}$" — clear fractions, then solve

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E2.3. Simplify, add/subtract, multiply/divide algebraic fractions. Expect 3–5 marks across one or two sub-parts. "Give your answer as a single fraction in its simplest form" is the standard instruction.

### OxAQA 9260

**Syllabus ref:** A7. Same operations; same techniques. Regularly appears as a build-up to function or equation-solving questions.

### Cambridge 0606 (Assumed knowledge)

Algebraic fractions sit underneath [[Remainder and Factor Theorems]] (rational expressions after polynomial division), composite functions, and many differentiation questions. Not tested standalone, but used daily.

### A-Level (Forward Bridge)

At A-Level the reverse operation takes over: **partial fractions** — splitting $\dfrac{5x - 4}{(x-1)(x-2)}$ into $\dfrac{1}{x-1} + \dfrac{4}{x-2}$ — examined on Cambridge 9709 P3 §3.1 and Edexcel IAL P4 §2.1, and the key that unlocks [[Integration|integrals]] like $\int \dfrac{1}{x^2 - 1}\, dx$.

### Where it is *not* examined

Beyond IGCSE the manipulation itself earns no marks of its own — 0606, 9709, Edexcel IAL and OxAQA 9660 all assume it silently inside rational-function, calculus and partial-fractions questions.

---

## Connections

- **Prerequisite:** [[Fractions (Vocab)]] — same four operations, just with variables
- **Prerequisite:** [[Factorising (Vocab)]] — you cannot simplify without factorising first
- **Prerequisite:** [[Expanding Brackets (Vocab)]] — needed when numerators multiply out
- **Prerequisite:** [[Indices in Algebra (Vocab)]] — $\dfrac{x^a}{x^b} = x^{a-b}$ is one simplification tool
- **Leads to:** [[Remainder and Factor Theorems]] — polynomial division produces rational expressions
- **Parallel:** [[Linear Equations (Vocab)]] — clearing fractions in an equation produces a linear (or quadratic) equation to solve
- **Leads to:** [[Integration]] — partial fractions are essential for integrating rational functions

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{a}{b}$ | `\dfrac{a}{b}` | Display-size fraction |
| $\div$ | `\div` | Division sign |
| $\cdot$ | `\cdot` | Multiplication dot |
