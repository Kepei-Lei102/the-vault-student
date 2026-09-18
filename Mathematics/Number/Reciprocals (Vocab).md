---
chinese: 倒数 (dàoshù)
prerequisites:
  - "[[Fractions (Vocab)]]"
  - "[[Inverse Operations (Vocab)]]"
leads_to:
  - "[[Algebraic Fractions (Vocab)]]"
  - "[[Inverse Function]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - syllabus/9260-N3
  - curriculum/Cambridge-0580
  - syllabus/0580-E1-1
  - type/vocabulary
  - notation/reciprocal
  - misconception/zero-reciprocal
---

# Reciprocals 倒数

## Definition

The **reciprocal** (also called the *multiplicative inverse*) of a non-zero number $x$ is the number you multiply $x$ by to get $1$:

$$x \cdot \frac{1}{x} = 1.$$

The reciprocal of $x$ is written $\dfrac{1}{x}$ or $x^{-1}$.

| Number | Reciprocal | Check |
|---|---|---|
| $5$ | $\dfrac{1}{5} = 0.2$ | $5 \times 0.2 = 1$ ✓ |
| $\dfrac{2}{3}$ | $\dfrac{3}{2}$ (flip) | $\dfrac{2}{3} \times \dfrac{3}{2} = 1$ ✓ |
| $-4$ | $-\dfrac{1}{4}$ | $-4 \times -\tfrac{1}{4} = 1$ ✓ |
| $1$ | $1$ (its own reciprocal) | $1 \times 1 = 1$ ✓ |
| $-1$ | $-1$ (its own reciprocal) | $(-1)(-1) = 1$ ✓ |
| $0$ | **undefined** | nothing times $0$ equals $1$ |

For a fraction $\tfrac{p}{q}$ with $p\ne0$ and $q\ne0$, the reciprocal is $\tfrac{q}{p}$ — *swap numerator and denominator*. That's the universal mnemonic: **flip the fraction**.

### 中文锚点

**倒数 (dàoshù)** = reciprocal / 乘法逆元 (chéngfǎ nìyuán). 一个数 $x$ 的倒数是 $\dfrac{1}{x}$，使得 $x \cdot \dfrac{1}{x} = 1$。

| 数 | 倒数 |
|---|---|
| $5$ | $\dfrac{1}{5}$ |
| $\dfrac{p}{q}$ | $\dfrac{q}{p}$（**翻转分子分母**） |
| $0$ | **不存在** (zero has no reciprocal) |
| $1$ 和 $-1$ | 自己 |

注：**0 没有倒数** —— 因为 $0$ 乘任何数都是 $0$，永远等不了 $1$。这就是为什么除以 $0$ 没有定义。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| reciprocal | 倒数 | the number whose product with $x$ is $1$ |
| multiplicative inverse | 乘法逆元 | formal name; same thing |
| flip the fraction | 翻分数 | the rule for $\tfrac{p}{q} \to \tfrac{q}{p}$ |
| dividing by | 除以 | dividing by $x$ = multiplying by $\dfrac{1}{x}$ |

> [!info] Why $0$ has no reciprocal
> Suppose $0$ had a reciprocal, called $r$. By definition $0 \cdot r = 1$. But $0$ times *anything* is $0$, so $0 \cdot r = 0 \ne 1$. Contradiction — no such $r$ exists. This is the deep reason **division by zero is undefined** in ordinary real and complex arithmetic: division by $x$ *is* multiplication by $1/x$, and when $x = 0$, $1/x$ doesn't exist.

---

## Worked Examples

### Example 1 — find the reciprocal

> Find the reciprocal of: (a) $7$; (b) $\dfrac{3}{8}$; (c) $-\dfrac{5}{2}$; (d) $0.4$; (e) $1\tfrac{2}{3}$.

**Answers.**
(a) $\dfrac{1}{7}$.
(b) Flip: $\dfrac{8}{3}$.
(c) Flip and keep the sign: $-\dfrac{2}{5}$.
(d) $0.4 = \dfrac{2}{5}$, so reciprocal is $\dfrac{5}{2} = 2.5$.
(e) Convert mixed to improper: $1\tfrac{2}{3} = \tfrac{5}{3}$. Reciprocal: $\dfrac{3}{5}$.

### Example 2 — using reciprocals to divide

> Compute $\dfrac{4}{5} \div \dfrac{2}{3}$.

Dividing by $\tfrac{2}{3}$ is the same as multiplying by its reciprocal $\tfrac{3}{2}$:

$$\frac{4}{5} \div \frac{2}{3} = \frac{4}{5} \times \frac{3}{2} = \frac{12}{10} = \frac{6}{5}.$$

This is the standard "Keep, Change, Flip" rule for fraction division — and it is *literally* the multiplication-by-reciprocal definition of division.

### Example 3 — chain of reciprocals

> Find the reciprocal of the reciprocal of $7$.

Reciprocal of $7$ is $\tfrac{1}{7}$. Reciprocal of $\tfrac{1}{7}$ is $7$.

**Pattern:** taking the reciprocal *twice* gives back the original. Like minus signs (two negatives cancel), or inverse functions ($f^{-1}(f(x)) = x$). The reciprocal is its own inverse operation — *involutive*, in the formal terminology.

---

## Common Mistakes

1. **Saying $0$'s reciprocal is $0$ or $\infty$.** Neither. The bare symbol $\dfrac{1}{0}$ is **undefined, period** — there is no real number that, multiplied by $0$, gives $1$.
   - The "$\infty$" answer comes from a *different* question: not "what is $\dfrac{1}{0}$?" but "what does $\dfrac{1}{x}$ do as $x$ approaches $0$?" That's a **limit**, and the answer depends on *which function* and *from which side*: $\dfrac{1}{x} \to +\infty$ as $x \to 0^+$, but $\dfrac{1}{x} \to -\infty$ as $x \to 0^-$. Same "$\dfrac{1}{0}$" shape, *opposite* limits — because the function is doing different things on the two sides.
   - Worse: $\dfrac{\sin x}{x} \to 1$ as $x \to 0$ (a $\tfrac{0}{0}$ form, but the limit is $1$). And $\dfrac{x^2}{x} \to 0$ as $x \to 0$ (also $\tfrac{0}{0}$, but the limit is $0$). The same indeterminate form gives wildly different answers depending on the function.
   - **Lesson.** $\dfrac10$ is undefined in real and complex arithmetic, including calculus. A limit describes nearby values of a function; it does not assign a value to division by zero. The notation “$0/0$ form” describes a limit whose numerator and denominator both tend to zero, not a number equal to a chosen answer.
2. **Dropping the minus sign.** Reciprocal of $-5$ is $-\tfrac{1}{5}$, *not* $\tfrac{1}{5}$.
3. **Reciprocal vs negative.** Reciprocal of $5$ is $\tfrac{1}{5}$ ($= 0.2$). *Negative* of $5$ is $-5$. Different operations, different results.
4. **Forgetting to convert mixed numbers.** Reciprocal of $1\tfrac{2}{3}$ is *not* "$1\tfrac{3}{2}$" — convert to improper $\tfrac{5}{3}$ first, then flip to $\tfrac{3}{5}$.

---

## Beyond Syllabus — different kinds of inverse

Recall that a reciprocal undoes multiplication. An inverse function instead undoes **composition**: $f^{-1}$ is not generally $1/f$. A nonsingular square matrix has an inverse under matrix multiplication. In modular arithmetic, $a$ has a multiplicative inverse modulo $n$ exactly when $\gcd(a,n)=1$; that last topic is enrichment here, not a blanket A-Level/IB/AP requirement.

## Exam Notes

### Cambridge 0580 — C1.1 / E1.1 Types of number

Both Core and Extended explicitly require identifying and using **reciprocals**. The reference is C1.1/E1.1, not “N1”. Recognise the reciprocal of a negative number, decimal or mixed number; verify the product is one. Fraction division uses the same multiplicative-inverse idea.

### OxfordAQA 9260 — N3 Core

N3 explicitly includes reciprocals in conventional notation for operations, alongside brackets, powers and roots. This is Core content, also assumed on Extension; no Extension-only reciprocal rule is introduced.

### Later mathematics courses

Cambridge 0606 and 9709, IB mathematics, and AP Calculus use this as prior numerical/algebraic knowledge rather than a new standalone reciprocal-arithmetic unit. Cambridge 9231 §1.1 explicitly includes polynomial transformations whose new roots are reciprocals of old roots; that is an application with nonzero roots, not a different definition.

**Not implied by these placements:** modular inverses are not a required reciprocal-arithmetic outcome of 0580 C1.1/E1.1 or 9260 N3. The lens equation and optical power are physical applications, not mathematics-board requirements.

---

## Connections

- **Prerequisite:** [[Fractions (Vocab)]] — fractions and their flipping
- **Prerequisite:** [[Inverse Operations (Vocab)]] — division undoes multiplication via reciprocal
- **Sibling:** [[Algebraic Fractions (Vocab)]] — same reciprocal rule for $\dfrac{f(x)}{g(x)} \to \dfrac{g(x)}{f(x)}$
- **Forward:** [[Inverse Function]] — the function-level analogue
- **Beyond syllabus:** *modular inverses* (RSA cryptography), *matrix inverses* (linear algebra)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{1}{x}$ | `\dfrac{1}{x}` | reciprocal of $x$ |
| $x^{-1}$ | `x^{-1}` | exponent notation for reciprocal |
| $\dfrac{p}{q}$ | `\dfrac{p}{q}` | fraction; reciprocal is $\dfrac{q}{p}$ |
