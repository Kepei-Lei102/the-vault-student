---
chinese: 无理根式 (wúlǐ gēnshì)
prerequisites:
  - "[[Powers and Roots (Vocab)]]"
  - "[[Laws of Indices]]"
  - "[[Factors and Multiples (Vocab)]]"
  - "[[Prime Factorisation (Vocab)]]"
  - "[[Fractions (Vocab)]]"
  - "[[Number Sets (Vocab)]]"
  - "[[Pythagoras Theorem]]"
leads_to:
  - "[[Completing the Square]]"
  - "[[Trigonometric Ratios]]"
  - "[[Algebraic Proof]]"
  - "[[Proof by Contradiction]]"
  - "[[Euler's Number]]"
  - "[[Exact Trigonometric Values]]"
  - "[[Heptadecagon]]"
  - "[[Quadratic Equations]]"
  - "[[Sine and Cosine Rules]]"
tags:
  - subject/mathematics
  - domain/number
  - domain/algebra
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-N7
  - syllabus/9260-N7-Ext
  - syllabus/0580-E1-18
  - type/definition
  - type/proof
  - notation/surd
  - notation/fractional-index
  - misconception/surd-approximation
  - misconception/rationalising
---

# Surds 无理根式

## Definition

A **surd** (无理根式) is a root that cannot be simplified to a rational number. In other words, it's a root that stays irrational.

$$\sqrt{2}, \quad \sqrt{3}, \quad \sqrt[3]{5}, \quad 3\sqrt{7} \qquad \text{are all surds}$$

$$\sqrt{4} = 2, \quad \sqrt[3]{27} = 3, \quad \sqrt{0.25} = 0.5 \qquad \text{are NOT surds (they simplify to rationals)}$$

A surd is an **exact value**. Writing $\sqrt{2}$ is exact; writing $1.414$ is an approximation. Exams often say *"Give your answer in surd form"* — this means: leave the root symbol in your answer, do not use a decimal.

### 中文锚点

无理根式 = 不能化简为有理数的根。$\sqrt{2}$ 是无理根式，$\sqrt{4} = 2$ 不是。考试要求"用根式表达"意味着保留根号，不要用小数。

> [!info] Why "surd"? — A story of translation
> The ancient Greeks discovered that $\sqrt{2}$ could not be expressed as a ratio of integers — the legend says Hippasus was drowned at sea for revealing this (probably apocryphal, but a great story). Greek mathematicians called these numbers *alogos* (ἄλογος, "without ratio" or "speechless"). Arabic scholars translated this as *asamm* (أصم, "deaf" or "mute"). When European scholars later translated the Arabic texts into Latin, they used *surdus* ("deaf") — and the English word **surd** stuck. So a surd is literally a number that "refuses to speak" as a clean fraction — a 2,500-year-old metaphor passed through three languages.

---

## §1 Simplifying Surds

### The key rule: $\sqrt{ab} = \sqrt{a} \times \sqrt{b}$

> **WHY:** This is Law 4 of indices in disguise. $\sqrt{ab} = (ab)^{1/2} = a^{1/2} \cdot b^{1/2} = \sqrt{a} \cdot \sqrt{b}$.

To **simplify** a surd, factor out the largest perfect square:

$$\sqrt{72} = \sqrt{36 \times 2} = \sqrt{36} \times \sqrt{2} = 6\sqrt{2}$$

**Method:** Use prime factorisation to find perfect square factors.

$$72 = 2^3 \times 3^2 = (2^2 \times 3^2) \times 2 = 36 \times 2$$

Pairs of prime factors come out of the root; lone factors stay inside.

### Worked examples

$$\sqrt{50} = \sqrt{25 \times 2} = 5\sqrt{2}$$

$$\sqrt{200} = \sqrt{100 \times 2} = 10\sqrt{2}$$

$$\sqrt{48} = \sqrt{16 \times 3} = 4\sqrt{3}$$

$$\sqrt{12} + \sqrt{27} = 2\sqrt{3} + 3\sqrt{3} = 5\sqrt{3}$$

> [!warning] You can only add/subtract **like surds**
> $2\sqrt{3} + 3\sqrt{3} = 5\sqrt{3}$ — same root, so combine the coefficients. But $\sqrt{2} + \sqrt{3}$ **cannot** be simplified further. Surds add like algebra: $2x + 3x = 5x$, but $x + y$ stays as $x + y$.

---

## §2 Multiplying and Dividing Surds

### Multiplication

$$\sqrt{a} \times \sqrt{b} = \sqrt{ab} \qquad \text{and} \qquad (\sqrt{a})^2 = a$$

*Examples:*

$$\sqrt{3} \times \sqrt{5} = \sqrt{15}$$

$$\sqrt{6} \times \sqrt{6} = 6$$

$$(2\sqrt{3})^2 = 4 \times 3 = 12$$

### Expanding brackets with surds

Treat surds like algebra — expand, then simplify:

$$(\sqrt{3} + 1)(\sqrt{3} - 2) = 3 - 2\sqrt{3} + \sqrt{3} - 2 = 1 - \sqrt{3}$$

$$(3 + \sqrt{5})(3 - \sqrt{5}) = 9 - 5 = 4 \qquad \text{(difference of two squares!)}$$

### Division

$$\dfrac{\sqrt{a}}{\sqrt{b}} = \sqrt{\dfrac{a}{b}} \qquad (b \neq 0)$$

*Example:* $\dfrac{\sqrt{18}}{\sqrt{2}} = \sqrt{\dfrac{18}{2}} = \sqrt{9} = 3$

---

## §3 Rationalising the Denominator

**Rationalising** means rewriting a fraction so there are **no surds in the denominator**.

> **WHY bother?** A surd in the denominator makes it harder to compare sizes, combine fractions, or estimate values. $\dfrac{1}{\sqrt{2}}$ is harder to work with than $\dfrac{\sqrt{2}}{2}$ — the second form immediately shows the value is "half of $\sqrt{2}$."

### Type 1: Single surd denominator — multiply by $\dfrac{\sqrt{a}}{\sqrt{a}}$

$$\dfrac{1}{\sqrt{3}} = \dfrac{1}{\sqrt{3}} \times \dfrac{\sqrt{3}}{\sqrt{3}} = \dfrac{\sqrt{3}}{3}$$

$$\dfrac{5}{\sqrt{2}} = \dfrac{5\sqrt{2}}{2}$$

$$\dfrac{4}{3\sqrt{5}} = \dfrac{4\sqrt{5}}{3 \times 5} = \dfrac{4\sqrt{5}}{15}$$

> **WHY it works:** $\sqrt{a} \times \sqrt{a} = a$ — the surd cancels itself when squared. We're multiplying by $\dfrac{\sqrt{a}}{\sqrt{a}} = 1$, so the value doesn't change.

### Type 2: Binomial denominator — multiply by the **conjugate**

The **conjugate** of $(a + \sqrt{b})$ is $(a - \sqrt{b})$. Their product eliminates the surd via difference of two squares:

$$(a + \sqrt{b})(a - \sqrt{b}) = a^2 - (\sqrt{b})^2 = a^2 - b$$

*Example:*

$$\dfrac{1}{3 + \sqrt{2}} = \dfrac{1}{3 + \sqrt{2}} \times \dfrac{3 - \sqrt{2}}{3 - \sqrt{2}} = \dfrac{3 - \sqrt{2}}{9 - 2} = \dfrac{3 - \sqrt{2}}{7}$$

*Example:*

$$\dfrac{4}{\sqrt{5} - 1} = \dfrac{4(\sqrt{5} + 1)}{(\sqrt{5})^2 - 1^2} = \dfrac{4\sqrt{5} + 4}{4} = \sqrt{5} + 1$$

> [!tip] Spotting the conjugate
> Flip the sign between the two terms. Conjugate of $(2 + \sqrt{3})$ is $(2 - \sqrt{3})$. Conjugate of $(\sqrt{7} - 5)$ is $(\sqrt{7} + 5)$. The surd part stays; the sign changes.

---

## §4 Why is $\sqrt{2}$ Irrational?

$\sqrt{2}$ cannot be written as $\dfrac{p}{q}$ for any integers $p, q$. This was first proved by the ancient Greeks (possibly Hippasus, ~5th century BC) using **proof by contradiction** — assume it's rational, then derive an impossible conclusion.

The full proof is the showcase example in [[Proof by Contradiction]]. The same technique extends to $\sqrt{3}$, $\sqrt{5}$, and in general $\sqrt{n}$ whenever $n$ is not a perfect square.

---

## §5 Common Misconceptions (Teaching Notes)

1. **Treating $\sqrt{2}$ as approximate.** $\sqrt{2}$ is exact. It is not "about 1.414" — it is the precise length of the diagonal of a unit square. Writing the decimal is an approximation; the surd is the truth.

2. **Adding unlike surds.** $\sqrt{2} + \sqrt{3} \neq \sqrt{5}$. Check: $\sqrt{5} \approx 2.24$ but $\sqrt{2} + \sqrt{3} \approx 1.41 + 1.73 = 3.14$. Surds only combine when the root is the same.

3. **Forgetting to simplify.** $\sqrt{18}$ is correct but not simplified. Always check for perfect square factors: $\sqrt{18} = 3\sqrt{2}$.

4. **Wrong rationalisation with binomials.** For $\dfrac{1}{2 + \sqrt{3}}$, students multiply by $\dfrac{\sqrt{3}}{\sqrt{3}}$ instead of the conjugate $\dfrac{2 - \sqrt{3}}{2 - \sqrt{3}}$. The single-surd trick only works when the denominator is a single surd term.

5. **Squaring a surd and keeping the root.** $(\sqrt{3})^2 = 3$, not $\sqrt{9}$ or $\sqrt{3}^2$. The whole point of squaring a surd is that the root disappears.

6. **Thinking $\sqrt{a^2 + b^2} = a + b$.** This is false. $\sqrt{9 + 16} = \sqrt{25} = 5$, not $3 + 4 = 7$. The square root does NOT distribute over addition. (This connects to [[Pythagoras Theorem]] — the hypotenuse is $\sqrt{a^2 + b^2}$, not $a + b$.)

---

## §6 Exam Notes

### OxAQA 9260

**Syllabus ref:** N7 (Extension) — calculate exactly with surds, manipulation, simplification, rationalising a denominator.

Extension paper: simplify surds, rationalise denominators (both types), leave answers in exact form. Frequently appears alongside [[Pythagoras Theorem]] (exact lengths) and [[Completing the Square]] (exact roots of quadratics).

### Cambridge 0580 Extended

**Syllabus ref:** E1.18 — surds, simplification, rationalising the denominator.

Paper 2 (non-calculator): simplify surds, rationalise single-surd denominators. Paper 4: surds in context (geometry, quadratics). Typical question: "Express $\dfrac{6}{\sqrt{3}}$ in the form $a\sqrt{3}$."

### Cambridge 0606

Surds are **assumed knowledge** from 0580. Not directly tested but needed throughout — particularly when solving quadratics by completing the square and giving exact answers.

### AP / IB / A-Level

Surds are foundational. At A-Level, rationalising denominators with binomial surds is explicitly assessed. IB AA HL includes proof of irrationality of $\sqrt{2}$ as a required proof. The concept extends to **algebraic surds** like $\sqrt{x + 1}$ in calculus (domain restrictions, differentiation via chain rule).

---

## §7 Connections

- **Prerequisite:** [[Powers and Roots (Vocab)]] — defines square root, cube root, $n$th root
- **Prerequisite:** [[Laws of Indices]] — fractional indices ($a^{1/2} = \sqrt{a}$) underpin all surd manipulation
- **Prerequisite:** [[Factors and Multiples (Vocab)]] — finding perfect square factors
- **Prerequisite:** [[Prime Factorisation (Vocab)]] — prime factorisation reveals which factors come out of the root
- **Leads to:** [[Completing the Square]] — exact roots of quadratics often involve surds
- **Leads to:** [[Trigonometric Ratios]] — exact values: $\sin 45° = \dfrac{\sqrt{2}}{2}$, $\cos 30° = \dfrac{\sqrt{3}}{2}$
- **Leads to:** [[Algebraic Proof]] — surd manipulation appears in proof questions
- **Leads to:** [[Proof by Contradiction]] — the $\sqrt{2}$ irrationality proof is the classic example
- **Used in:** [[Pythagoras Theorem]] — exact lengths are surds ($\sqrt{a^2 + b^2}$)
- **Used in:** [[Differentiation]] — rewriting $\sqrt{x} = x^{1/2}$ before differentiating

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\sqrt{a}$ | `\sqrt{a}` | Square root |
| $\sqrt[n]{a}$ | `\sqrt[n]{a}` | $n$th root |
| $a\sqrt{b}$ | `a\sqrt{b}` | Simplified surd form |
| $\dfrac{1}{\sqrt{a}}$ | `\dfrac{1}{\sqrt{a}}` | Before rationalising |
| $\dfrac{\sqrt{a}}{a}$ | `\dfrac{\sqrt{a}}{a}` | After rationalising |
