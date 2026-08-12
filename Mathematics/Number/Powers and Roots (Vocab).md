---
chinese: 幂与根 (mì yǔ gēn)
prerequisites:
  - "[[Four Operations (Vocab)]]"
  - "[[Prime Factorisation (Vocab)]]"
leads_to:
  - "[[Laws of Indices]]"
  - "[[Surds]]"
  - "[[Pythagoras Theorem]]"
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Standard Form (Vocab)]]"
  - "[[Trigonometric Ratios]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-N5
  - syllabus/0580-E1-1
  - syllabus/0580-E1-3
  - type/vocabulary
  - misconception/square-root-two-answers
---

# Powers and Roots 幂与根

## Definition

A **power** (幂) is repeated multiplication: $a^n = \underbrace{a \times a \times \cdots \times a}_{n \text{ times}}$. A **root** is the inverse: $\sqrt[n]{a}$ asks "what number, raised to the $n$th power, gives $a$?"

$$3^4 = 81 \qquad \sqrt[4]{81} = 3$$

### 中文锚点

幂 = 重复乘法。根 = 幂的逆运算。$a^n$ 读作"$a$ 的 $n$ 次幂"。$\sqrt[n]{a}$ 读作"$a$ 的 $n$ 次根"。

## Key Vocabulary

| English          | 中文                 | Notes                                                                                |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------ |
| power            | 幂 (mì)             | $5^3$ is "5 to the power of 3." *"You underestimate my power!"* — Anakin, definitely |
| base             | 底数 (dǐshù)         | The number being multiplied: in $5^3$, the base is 5                                 |
| index / exponent | 指数 (zhǐshù)        | The number of times: in $5^3$, the index is 3. Plural: **indices**                   |
| squared          | 平方 (píngfāng)      | $n^2$ — "5 squared" = 25. See below for WHY it's called "squared"                    |
| cubed            | 立方 (lìfāng)        | $n^3$ — "5 cubed" = 125. See below for WHY it's called "cubed"                       |
| square root      | 平方根 (píngfāng gēn) | $\sqrt{25} = 5$. The symbol $\sqrt{\phantom{x}}$ denotes the **positive** root       |
| cube root        | 立方根 (lìfāng gēn)   | $\sqrt[3]{125} = 5$. Cube roots can be negative: $\sqrt[3]{-8} = -2$                 |
| $n$th root       | $n$ 次根             | $\sqrt[n]{a}$ — generalises square and cube roots                                    |
| perfect square   | 完全平方数              | $1, 4, 9, 16, 25, \ldots$ — integers that are squares of integers                    |
| perfect cube     | 完全立方数              | $1, 8, 27, 64, 125, \ldots$                                                          |

> [!info] WHY "squared" and "cubed"?
> The names come from geometry. A **square** with side length $n$ has area $n \times n = n^2$. A **cube** with side length $n$ has volume $n \times n \times n = n^3$. So "5 squared" literally means "the area of a square with side 5," and "5 cubed" means "the volume of a cube with side 5." The Chinese names reveal the same origin: 平方 means "flat square" (area — 2D), 立方 means "standing cube" (volume — 3D). There is no standard geometric name for $n^4$ and beyond, because we run out of physical dimensions — so we just say "to the power of 4."

> [!warning] $\sqrt{25} = 5$, not $\pm 5$
> The square root **symbol** $\sqrt{\phantom{x}}$ always gives the positive (principal) root. The equation $x^2 = 25$ has two solutions ($x = \pm 5$), but $\sqrt{25} = 5$ only. This distinction matters in exam answers: "Find $\sqrt{49}$" → 7. "Solve $x^2 = 49$" → $x = \pm 7$.

## Exam Notes

### OxAQA 9260
**Syllabus ref:** N5 — squares, cubes, square roots, cube roots; recognise powers of 2, 3, 5.
Both papers allow calculators, but "without a calculator" sub-questions may appear.

### Cambridge 0580 Extended
**Syllabus ref:** E1.3 — squares, cubes, and corresponding roots.
Paper 2 (non-calculator) expects recall of perfect squares up to $15^2 = 225$ and perfect cubes up to $5^3 = 125$.

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — multiplication as the building block
- **Leads to:** [[Laws of Indices]] — deep card: rules for combining powers, WHY $a^0 = 1$
- **Leads to:** [[Surds]] — deep card: irrational roots like $\sqrt{2}$, rationalisation
- **Parallel:** [[Prime Factorisation (Vocab)]] — index form ($2^3 \times 3^2$) uses powers
- **Used in:** [[Differentiation]] — the power rule $\dfrac{d}{dx}(x^n) = nx^{n-1}$ operates on indices

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $a^n$ | `a^n` | Power |
| $\sqrt{a}$ | `\sqrt{a}` | Square root |
| $\sqrt[3]{a}$ | `\sqrt[3]{a}` | Cube root |
| $\sqrt[n]{a}$ | `\sqrt[n]{a}` | $n$th root |
