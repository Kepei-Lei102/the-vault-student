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

野餐前，要把6个三明治和9杯饮料装进几个内容相同的袋子。分成3袋，每袋2个三明治、3杯饮料，原来两堆东西里藏着的“三份相同组合”就显出来了。因式分解也是在找这样的组合：把 $6x+9$ 写成 $3(2x+3)$，总量没变，只是把“三份”提到了外面，让重复的结构一眼可见。

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

When the leading coefficient isn't 1, the "find two numbers" approach gets awkward. The **cross method** is a systematic search for integer-coefficient factors of a quadratic $ax^2 + bx + c$. Not every quadratic has such factors; the quadratic formula or completing the square remains available.

**Example:** Factorise $6x^2 + 17x + 5$.

**Step 1 — trigger: integer coefficients and a leading coefficient other than 1. Tool: factor-pair search.** Write down the ways to split $a = 6$ and $c = 5$:

$$6 = 1 \times 6 = 2 \times 3 \qquad 5 = 1 \times 5$$

**Step 2 — trigger: the middle coefficient must also match. Tool: expand the candidate product and compare its cross terms.** Try each combination:

$$\begin{array}{ccc} 2 & & 1 \\ & \times & \\ 3 & & 5 \end{array} \qquad \Rightarrow \quad 2 \times 5 + 3 \times 1 = 10 + 3 = 13 \quad \text{✗}$$

$$\begin{array}{ccc} 2 & & 5 \\ & \times & \\ 3 & & 1 \end{array} \qquad \Rightarrow \quad 2 \times 1 + 3 \times 5 = 2 + 15 = 17 \quad \text{✓}$$

**Step 3 — tool: reconstruct and verify by expansion.** Each row gives a bracket:

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

**Syllabus ref: C2.2 / E2.2** (the algebraic-manipulation block, alongside expanding). The tier split is sharp and worth knowing: **Core stops at extracting common factors** — item 3, "e.g. $9x^2 + 15xy = 3x(3x+5y)$" — while **Extended adds the whole standard catalogue** as item 4: grouping ($ax + bx + kay + kby$), the difference of two squares ($a^2x^2 - b^2y^2$), the perfect square ($a^2 + 2ab + b^2$), the general quadratic ($ax^2+bx+c$), and the common-factor cubic ($ax^3+bx^2+cx$). That list *is* the syllabus's own definition of what you are expected to recognise, so it doubles as a revision checklist. Note also the syllabus's standing gloss, printed beside the row: **"Factorise means factorise fully"** — so a partially factorised expression does not satisfy that instruction; credit depends on the particular mark scheme.

### OxfordAQA 9260

**Syllabus ref: A5.** Core includes common factors, monic quadratics $x^2+bx+c$ and difference of squares. Extension includes the general quadratic $ax^2+bx+c$. This differs from Cambridge 0580 Core, where the factorisation requirement is common factors only.

### Cambridge 0606 / 9709 / 9231

0606 §2.4 and 9709 §1.1 explicitly include factorisation as a method for solving quadratics. Expanding and collecting terms support those manipulations; 9709 §1.5 separately examines binomial expansion. 9231 assumes the relevant 9709 pure content. These syllabuses do not justify a claim that a basic algebra step can never be asked on its own.

### Edexcel IAL / OxfordAQA 9660

Edexcel IAL P1 §1.10 explicitly includes expanding brackets, collecting like terms and factorising polynomials up to degree three; P1 §1.5 includes quadratic solution by factorisation. OxfordAQA 9660 P1.1 likewise names polynomial manipulation and quadratic factorisation. These are examinable algebra, not merely optional background.

### IB AA / AI and AP Calculus

The IB AA and AI guides for first assessment 2021 list expansion and factorisation under **prior learning**, which examination questions may assume. [IB AA guide, prior learning](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-analysis-approaches-guide.pdf); [IB AI guide, prior learning](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-applications-interpretation-guide.pdf).

AP Calculus AB/BC assumes fluent algebra; Topic 1.6 uses algebraic manipulation for limits, including factoring and cancellation with domain awareness. **Scope boundary:** elementary expansion/factorisation is not a separate new unit in those IB/AP courses; its assumed status does not make it unassessable. No marks or question frequency are implied here.

---

## Connections

- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — terms, coefficients
- **Prerequisite:** [[Collecting Like Terms (Vocab)]] — simplify first, then factorise
- **Prerequisite:** [[Expanding Brackets (Vocab)]] — factorising is the reverse process
- **Prerequisite:** [[Factors and Multiples (Vocab)]] — HCF concept transfers from numbers to algebra
- **Leads to:** [[Algebraic Proof]] — factorising is often the key step that reveals "multiple of 3" etc.
- **Leads to:** [[Algebraic Fractions (Vocab)]] — factorise numerator and denominator to cancel
- **Parallel:** [[Surds]] — difference of two squares rationalises conjugate pairs
