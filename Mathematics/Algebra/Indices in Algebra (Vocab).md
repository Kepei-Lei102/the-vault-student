---
chinese: 代数中的指数 (dàishù zhōng de zhǐshù)
prerequisites:
  - "[[Laws of Indices]]"
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Collecting Like Terms (Vocab)]]"
leads_to:
  - "[[Algebraic Fractions (Vocab)]]"
  - "[[Binomial Theorem]]"
  - "[[Substitution Equations]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/0580-E2-4
  - syllabus/9260-A6
  - type/vocabulary
  - misconception/only-raising-variable
  - misconception/coefficient-not-raised
---

# Indices in Algebra 代数中的指数

## Definition

**Indices in algebra** (代数中的指数) is the same [[Laws of Indices]] you use on numbers, now applied to terms with variables: $3x^2$, $\dfrac{5}{y^3}$, $(2x^3)^4$. The rules are identical — coefficients combine by ordinary arithmetic, and variable powers combine by the index laws.

### 中文锚点

代数指数 = 指数定律用在字母上。规则完全一样：$x^a \cdot x^b = x^{a+b}$。但注意系数要单独处理：$3x^2 \cdot 4x^3 = 12x^5$（系数相乘 $3 \times 4 = 12$，指数相加 $2 + 3 = 5$）。

---

## The Five Rules — Recap

For any base $x$ and real indices $a, b$:

$$\boxed{\;x^a \cdot x^b = x^{a+b} \qquad \dfrac{x^a}{x^b} = x^{a-b} \qquad (x^a)^b = x^{ab}\;}$$

$$\boxed{\;x^0 = 1 \qquad x^{-a} = \dfrac{1}{x^a} \qquad x^{1/n} = \sqrt[n]{x}\;}$$

See [[Laws of Indices]] for full proofs and intuition. This card focuses on applying them to algebraic expressions.

---

## Key Vocabulary

| English | 中文 | Example |
|---------|------|---------|
| **base** | 底数 (dǐshù) | In $3x^5$, the base is $x$ |
| **index / exponent / power** | 指数 (zhǐshù) | In $3x^5$, the index is $5$ |
| **coefficient** | 系数 (xìshù) | In $3x^5$, the coefficient is $3$ |
| **like terms** | 同类项 (tónglèixiàng) | Terms with the *same variable to the same power* — $3x^2$ and $-7x^2$ are like; $3x^2$ and $5x^3$ are not |
| **simplify** | 化简 (huàjiǎn) | Use the laws to rewrite in shortest form |
| **evaluate** | 求值 (qiúzhí) | Substitute a number and compute |

---

## Worked Patterns

### Multiplying

$$3x^2 \cdot 4x^5 = (3 \times 4)(x^2 \cdot x^5) = 12 x^7$$

Coefficients multiply, indices add.

### Dividing

$$\dfrac{15 x^7}{3 x^2} = 5 x^{5}$$

Coefficients divide, indices subtract.

### Power of a product

$$(2x^3)^4 = 2^4 \cdot (x^3)^4 = 16 x^{12}$$

> [!warning] The coefficient must also be raised
> $(2x^3)^4 \neq 2x^{12}$. Every factor inside the bracket is raised to the power, *including the $2$*. Try $x = 1$: $(2)^4 = 16$, not $2$.

### Power of a quotient

$$\left(\dfrac{3x^2}{y}\right)^3 = \dfrac{3^3 \cdot (x^2)^3}{y^3} = \dfrac{27 x^6}{y^3}$$

### Negative indices → reciprocal

$$4x^{-3} = \dfrac{4}{x^3} \qquad \dfrac{5}{y^{-2}} = 5y^2$$

> [!warning] The negative index only attaches to the variable
> $4x^{-3}$ is $4 \cdot x^{-3} = \dfrac{4}{x^3}$, not $\dfrac{1}{4x^3}$. The coefficient $4$ stays on top.

### Fractional indices → roots

$$x^{1/2} = \sqrt{x} \qquad 8 x^{2/3} = 8\sqrt[3]{x^2} \qquad (9x^4)^{1/2} = 3x^2$$

---

## Like Terms and Indices — Crucial Distinction

Adding vs multiplying is where students stumble.

| Operation | Example | Rule |
|-----------|---------|------|
| **Adding like terms** | $3x^2 + 5x^2 = 8x^2$ | Indices stay the same |
| **Multiplying** | $3x^2 \cdot 5x^2 = 15x^4$ | Indices add |

> [!warning] $x^2 + x^3$ does NOT simplify
> These are **unlike terms**. No index rule applies to addition — you can only factorise: $x^2 + x^3 = x^2(1 + x)$.

---

## Common Mistakes

> [!warning] Only raising the variable, not the coefficient
> $(3x^2)^4$ — the most common slip is writing $3x^8$. Wrong. Both $3$ and $x^2$ get raised to the fourth: $3^4 \cdot x^8 = 81 x^8$.

> [!warning] Dropping the minus sign on negative bases
> $(-x)^2 = x^2$ (positive). But $-x^2$ (with no bracket) means $-(x^2)$, which is negative when $x \neq 0$. The bracket matters.

> [!warning] Confusing $2^x$ and $x^2$
> $2^x$ is an exponential (variable in the exponent) — see [[Exponential Graphs (Vocab)]]. $x^2$ is a power (variable in the base). Different families.

---

## Exam Phrasing

- "**Simplify**" — use the rules to shorten
- "**Express in the form** $a x^n$" — tells you the target shape (one coefficient, one power)
- "**Write as a single power of $x$**" — combine into $x^{\text{something}}$

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E2.4. Indices on algebraic terms, including negative and fractional. Typical question: "Simplify $\dfrac{6x^4 y^2}{2x y^5}$." Answer: $\dfrac{3x^3}{y^3}$. Always 1–3 marks.

### OxAQA 9260

**Syllabus ref:** A6 extends index work into algebra. The rules themselves are the same five as [[Laws of Indices]].

### Cambridge 0606 Additional Maths

Not examined directly — the 0606 specification states that 0580 content (indices and surds included) is **assumed** and "will not be tested directly but may be needed" — so these rules appear silently inside every 0606 simplification.

---

## Connections

- **Prerequisite:** [[Laws of Indices]] — the five rules themselves, proved
- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — terms, coefficients, variables
- **Prerequisite:** [[Collecting Like Terms (Vocab)]] — the addition side of algebra
- **Parallel:** [[Expanding Brackets (Vocab)]] — $x^2(x + 3) = x^3 + 3x^2$ uses the product rule
- **Leads to:** [[Algebraic Fractions (Vocab)]] — simplifying $\dfrac{x^a}{x^b}$
- **Leads to:** [[Binomial Theorem]] — the general expansion of $(a + b)^n$

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $x^{n}$ | `x^{n}` | Use braces for multi-character exponents |
| $\sqrt[n]{x}$ | `\sqrt[n]{x}` | $n$th root |
| $\dfrac{a}{b}$ | `\dfrac{a}{b}` | Display-size fraction |
