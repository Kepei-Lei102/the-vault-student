---
chinese: 因式分解 (yīnshì fēnjiě)
prerequisites:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Collecting Like Terms (Vocab)]]"
  - "[[Expanding Brackets (Vocab)]]"
  - "[[Factors and Multiples (Vocab)]]"
leads_to:
  - "[[Algebraic Proof]]"
  - "[[Algebraic Fractions (Vocab)]]"
  - "[[Fractional Equations (Vocab)]]"
  - "[[Quadratic Equations]]"
  - "[[Remainder and Factor Theorems]]"
  - "[[Partial Fractions]]"
  - "[[Completing the Square]]"
  - "[[Simultaneous Equations (Vocab)]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A5
  - syllabus/0580-E2-2
  - type/vocabulary
  - misconception/incomplete-factorisation
---

# Factorising 因式分解

## Definition

To **factorise** (因式分解) means to write an expression as a **product of factors**. It is the reverse of expanding. If expanding is "opening" brackets, factorising is "putting them back."

$$6x + 9 = 3(2x + 3)$$

### 中文锚点

因式分解 = 把一个表达式写成几个因式的乘积。和展开相反。先找公因式（HCF），提出来。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| factorise | 因式分解 (yīnshì fēnjiě) | Write as a product of factors |
| common factor | 公因式 (gōng yīnshì) | A factor shared by every term |
| HCF | 最高公因数 | Highest Common Factor — the largest common factor to extract |
| difference of two squares | 两个平方的差 | $a^2 - b^2 = (a+b)(a-b)$ |
| grouping | 分组 (fēnzǔ) | Split 4 terms into two pairs, factor each pair |
| quadratic factorisation | 二次因式分解 | $x^2 + bx + c = (x + p)(x + q)$ where $pq = c$, $p + q = b$ |
| fully factorised | 完全因式分解 | No further factoring is possible |

---

## The Three Methods (IGCSE Level)

**1. Common factor** — always try this first.

$$6x^2 + 9x = 3x(2x + 3)$$

Find the HCF of all terms ($3x$), write it outside, divide each term by it.

**2. Difference of two squares** — recognise $a^2 - b^2$.

$$x^2 - 49 = (x + 7)(x - 7)$$

> [!tip] WHY does this work?
> Expand $(x+7)(x-7) = x^2 - 7x + 7x - 49 = x^2 - 49$. The middle terms always cancel. This is the same identity from [[Expanding Brackets (Vocab)]].

**3. Quadratic trinomial** — find two numbers that multiply to $c$ and add to $b$.

$$x^2 + 5x + 6 = (x + 2)(x + 3)$$

because $2 \times 3 = 6$ and $2 + 3 = 5$.

### The Cross Method 交叉相乘法

When the leading coefficient isn't 1, the "find two numbers" approach gets awkward. The **cross method** is a systematic way to handle any quadratic $ax^2 + bx + c$.

**Example:** Factorise $6x^2 + 17x + 5$.

**Step 1 — List factor pairs.** Write down the ways to split $a = 6$ and $c = 5$:

$$6 = 1 \times 6 = 2 \times 3 \qquad 5 = 1 \times 5$$

**Step 2 — Arrange in a cross and multiply diagonally.** Try each combination:

$$\begin{array}{ccc} 2 & & 1 \\ & \times & \\ 3 & & 5 \end{array} \qquad \Rightarrow \quad 2 \times 5 + 3 \times 1 = 10 + 3 = 13 \quad \text{✗}$$

$$\begin{array}{ccc} 2 & & 5 \\ & \times & \\ 3 & & 1 \end{array} \qquad \Rightarrow \quad 2 \times 1 + 3 \times 5 = 2 + 15 = 17 \quad \text{✓}$$

**Step 3 — Read off the brackets.** Each row gives a bracket:

$$6x^2 + 17x + 5 = (2x + 5)(3x + 1)$$

> [!tip] WHY this works
> The cross multiplication gives the two parts of the middle term: $(2x)(1) + (5)(3x) = 2x + 15x = 17x$. You're really doing FOIL in reverse — the diagonal products are the Outer and Inner terms.

---

## Common Mistakes

1. **Incomplete factorisation:** $12x^2 + 18x = 2(6x^2 + 9x)$ — yes, $2$ is a factor, but $3x$ is still common inside. Fully factorised: $6x(2x + 3)$.
2. **Forgetting $a^2 - b^2$ applies to non-obvious squares:** $4x^2 - 25 = (2x)^2 - 5^2 = (2x+5)(2x-5)$.
3. **Sign errors in quadratic factorisation:** For $x^2 - x - 6$, you need $p \times q = -6$ and $p + q = -1$. That's $(x - 3)(x + 2)$, not $(x + 3)(x - 2)$.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref: C2.2 / E2.2** (the algebraic-manipulation block, alongside expanding). The tier split is sharp and worth knowing: **Core stops at extracting common factors** — item 3, "e.g. $9x^2 + 15xy = 3x(3x+5y)$" — while **Extended adds the whole standard catalogue** as item 4: grouping ($ax + bx + kay + kby$), the difference of two squares ($a^2x^2 - b^2y^2$), the perfect square ($a^2 + 2ab + b^2$), the general quadratic ($ax^2+bx+c$), and the common-factor cubic ($ax^3+bx^2+cx$). That list *is* the syllabus's own definition of what you are expected to recognise, so it doubles as a revision checklist. Note also the syllabus's standing gloss, printed beside the row: **"Factorise means factorise fully"** — so partial factorisation loses the mark even when the question does not repeat the word.

### OxfordAQA 9260

**Syllabus ref: A5.** Same skill, tested directly and as a sub-step in solving quadratics, simplifying algebraic fractions, and proof.

### Cambridge 0606

Not a standalone question type: factorising is assumed, and appears as the first-choice method for solving quadratics (alongside the formula and completing the square). The syllabus carries the same instruction verbatim in its notes to candidates — when asked to *factorise*, factorise **fully**.

---

## Connections

- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — terms, coefficients
- **Prerequisite:** [[Collecting Like Terms (Vocab)]] — simplify first, then factorise
- **Prerequisite:** [[Expanding Brackets (Vocab)]] — factorising is the reverse process
- **Prerequisite:** [[Factors and Multiples (Vocab)]] — HCF concept transfers from numbers to algebra
- **Leads to:** [[Algebraic Proof]] — factorising is often the key step that reveals "multiple of 3" etc.
- **Leads to:** [[Algebraic Fractions (Vocab)]] — factorise numerator and denominator to cancel
- **Parallel:** [[Surds]] — difference of two squares rationalises conjugate pairs
