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

For a positive integer exponent $n$, a **power** (幂) is repeated multiplication: $a^n = \underbrace{a \times a \times \cdots \times a}_{n \text{ times}}$. A **root** reverses that operation. For odd positive $n$, $\sqrt[n]{a}$ is the unique real number whose $n$th power is $a$. For even positive $n$ and $a\ge0$, the radical denotes the **nonnegative principal root**; a negative radicand has no real even root.

$$3^4 = 81 \qquad \sqrt[4]{81} = 3$$

### 中文锚点

用小方砖铺一块正方形地面，每边排5块，就有5排、每排5块，一共25块。“5的平方”就是从边长算出总数；反过来，如果告诉你一共用了25块，还要铺成正方形，你就在找“每边该排几块”。平方根把刚才的问题倒过来问：已知铺出来有多大，找回那条边有多长。

## Key Vocabulary

| English          | 中文                 | Notes                                                                                |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------ |
| power            | 幂 (mì)             | $5^3$ is "5 to the power of 3." *"You underestimate my power!"* — Anakin, definitely |
| base             | 底数 (dǐshù)         | The number being multiplied: in $5^3$, the base is 5                                 |
| index / exponent | 指数 (zhǐshù)        | The number of times: in $5^3$, the index is 3. Plural: **indices**                   |
| squared          | 平方 (píngfāng)      | $n^2$ — "5 squared" = 25. See below for WHY it's called "squared"                    |
| cubed            | 立方 (lìfāng)        | $n^3$ — "5 cubed" = 125. See below for WHY it's called "cubed"                       |
| square root      | 平方根 (píngfāng gēn) | $\sqrt{25} = 5$. The symbol $\sqrt{\phantom{x}}$ denotes the **nonnegative principal** root       |
| cube root        | 立方根 (lìfāng gēn)   | $\sqrt[3]{125} = 5$. Cube roots can be negative: $\sqrt[3]{-8} = -2$                 |
| $n$th root       | $n$ 次根             | $\sqrt[n]{a}$ — generalises square and cube roots                                    |
| perfect square   | 完全平方数              | $0, 1, 4, 9, 16, 25, \ldots$ — integers that are squares of integers                    |
| perfect cube     | 完全立方数              | $0, 1, 8, 27, 64, 125, \ldots$                                                          |

> [!info] WHY "squared" and "cubed"?
> The names come from geometry. A **square** with side length $n$ has area $n \times n = n^2$. A **cube** with side length $n$ has volume $n \times n \times n = n^3$. So "5 squared" literally means "the area of a square with side 5," and "5 cubed" means "the volume of a cube with side 5." The Chinese names reveal the same origin: 平方 means "flat square" (area — 2D), 立方 means "standing cube" (volume — 3D). There is no standard geometric name for $n^4$ and beyond, because we run out of physical dimensions — so we just say "to the power of 4."

> [!warning] $\sqrt{25} = 5$, not $\pm 5$
> The square root **symbol** $\sqrt{\phantom{x}}$ always gives the nonnegative (principal) root. The equation $x^2 = 25$ has two solutions ($x = \pm 5$), but $\sqrt{25} = 5$ only. This distinction matters in exam answers: "Find $\sqrt{49}$" → 7. "Solve $x^2 = 49$" → $x = \pm 7$.

## Exam Notes

### OxfordAQA 9260

**N5 Core** includes positive integer powers and associated real roots, including higher roots; the named bases are **2, 3, 4 and 5**. **N6** develops index laws (integer powers in Core, fractional powers in Extension). A radical with an even index denotes the nonnegative root; solving an even-power equation can require both signs. No fixed mark allocation follows from the topic alone.

### Cambridge 0580 — Core and Extended

**C1.3 and E1.3** both include squares, cubes and corresponding roots. Recall includes squares/roots associated with integers **1–15**, and cubes/cube roots associated with **1, 2, 3, 4, 5 and 10**. **C1.1/E1.1** also includes square and cube numbers. Papers 1/2 are non-calculator and Papers 3/4 calculator under the 2025–27 syllabus; the knowledge is not an Extended-only Paper 2 requirement.

### Further mathematics courses — scope boundary

**Cambridge 0606:** indices and surds remain assumed IGCSE knowledge; they were removed as a separately assessed subject-content topic in the 2025–27 syllabus. **9709** assumes elementary surd manipulation as prior knowledge and uses index laws in later algebra and logarithms; **9231** assumes these arithmetic tools within further topics. **Edexcel IAL P1** and **OxfordAQA 9660 Pure** develop indices/surds; their scope extends beyond this elementary vocabulary.

**IB AA and AI:** elementary arithmetic is prerequisite knowledge, while exponents are used explicitly in Number and Algebra; AA SL1.5 develops integer exponent laws and introduces logarithms. **AP Calculus AB/BC:** algebraic powers and radicals are assumed preparation and used throughout functions and calculus; they are not a standalone square/cube-recall unit. A root of a polynomial equation is a related but different use of the word “root.”

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — multiplication as the building block
- **Leads to:** [[Laws of Indices]] — rules for combining powers, WHY $a^0 = 1$
- **Leads to:** [[Surds]] — irrational roots like $\sqrt{2}$, rationalisation
- **Parallel:** [[Prime Factorisation (Vocab)]] — index form ($2^3 \times 3^2$) uses powers
- **Used in:** [[Differentiation]] — the power rule $\dfrac{d}{dx}(x^n) = nx^{n-1}$ operates on indices

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $a^n$ | `a^n` | Power |
| $\sqrt{a}$ | `\sqrt{a}` | Square root |
| $\sqrt[3]{a}$ | `\sqrt[3]{a}` | Cube root |
| $\sqrt[n]{a}$ | `\sqrt[n]{a}` | $n$th root |
