---
chinese: 指数定律 (zhǐshù dìnglǜ)
prerequisites:
  - "[[Powers and Roots (Vocab)]]"
  - "[[Four Operations (Vocab)]]"
  - "[[Factors and Multiples (Vocab)]]"
leads_to:
  - "[[Surds]]"
  - "[[Completing the Square]]"
  - "[[Algebraic Proof]]"
  - "[[Power Rule]]"
  - "[[Exponential Growth and Decay]]"
  - "[[Euler's Number]]"
  - "[[Binomial Theorem]]"
  - "[[Standard Form (Vocab)]]"
  - "[[Exponential Graphs (Vocab)]]"
  - "[[Direct and Inverse Proportion (Vocab)]]"
  - "[[Indices in Algebra (Vocab)]]"
  - "[[Logarithms]]"
  - "[[Exponential Function]]"
  - "[[Arithmetic and Geometric Progressions]]"
  - "[[Simple and Compound Interest (Vocab)]]"
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
  - syllabus/9260-N6
  - syllabus/9260-N6-Ext
  - syllabus/9260-A6
  - syllabus/0580-E1-7
  - type/definition
  - type/proof
  - notation/index
  - notation/fractional-index
  - misconception/zero-power
  - misconception/negative-index
---

# Laws of Indices 指数定律

## Definition

The **laws of indices** (指数定律) are rules for simplifying expressions involving powers. They all follow from one idea: $a^n$ means **$n$ copies of $a$ multiplied together**.

$$a^n = \underbrace{a \times a \times \cdots \times a}_{n \text{ times}}$$

Every law below is a *consequence* of this definition — none are arbitrary rules to memorise.

> [!info] Where did index notation come from?
> The idea of repeated multiplication is ancient, but writing it as $a^n$ took centuries. Archimedes (~250 BC) noticed that multiplying powers of 10 corresponds to adding the exponents — essentially Law 1 — but never wrote it as notation. The superscript notation $a^n$ was introduced by **René Descartes** in *La Géométrie* (1637), the same book that gave us $x$-$y$ coordinates. Before Descartes, people wrote $aaa$ for $a^3$. Descartes' compact notation made the index laws *visible* — once you write $a^m \times a^n$, the pattern $a^{m+n}$ practically jumps off the page.

### 中文锚点

指数定律 = 处理幂运算的规则。所有规则都来自一个核心想法：$a^n$ 就是 "$a$ 乘以自己 $n$ 次"。理解了这个定义，每一条定律都是自然推出的。

---

## §1 The Seven Laws

### Law 1 — Multiplication: $a^m \times a^n = a^{m+n}$

> **WHY:** $m$ copies of $a$, then $n$ more copies of $a$ — that's $(m + n)$ copies in total.

$$a^m \times a^n = \underbrace{a \times \cdots \times a}_{m} \times \underbrace{a \times \cdots \times a}_{n} = \underbrace{a \times \cdots \times a}_{m+n} = a^{m+n}$$

*Example:* $2^3 \times 2^4 = 2^{3+4} = 2^7 = 128$

### Law 2 — Division: $a^m \div a^n = a^{m-n}$

> **WHY:** $m$ copies on top, $n$ copies on the bottom. Each $a$ on the bottom cancels one $a$ on top ($\dfrac{a}{a} = 1$), so $n$ copies cancel out, leaving $(m - n)$ copies.

$$\dfrac{a^m}{a^n} = \dfrac{\overbrace{a \times a \times a \times \cdots \times a}^{m}}{\underbrace{a \times a \times \cdots \times a}_{n}} = \dfrac{\cancel{a} \times \cancel{a} \times \cdots \times \cancel{a} \times \overbrace{a \times \cdots \times a}^{m-n}}{\cancel{a} \times \cancel{a} \times \cdots \times \cancel{a}} = a^{m-n} \qquad (a \neq 0)$$

*Concrete example:* $\dfrac{5^7}{5^3} = \dfrac{\cancel{5} \times \cancel{5} \times \cancel{5} \times 5 \times 5 \times 5 \times 5}{\cancel{5} \times \cancel{5} \times \cancel{5}} = 5^4 = 625$

### Law 3 — Power of a power: $(a^m)^n = a^{mn}$

> **WHY:** $n$ groups of "$m$ copies of $a$" — that's $m \times n$ copies in total.

$$(a^m)^n = \underbrace{a^m \times a^m \times \cdots \times a^m}_{n} = a^{\overbrace{m + m + \cdots + m}^{n}} = a^{mn}$$

*Example:* $(3^2)^4 = 3^{2 \times 4} = 3^8 = 6561$

### Law 4 — Power of a product: $(ab)^n = a^n b^n$

> **WHY:** $n$ copies of $(ab)$ — rearrange the $a$'s together and the $b$'s together.

$$(ab)^n = \underbrace{(ab)(ab) \cdots (ab)}_{n} = \underbrace{a \cdot a \cdots a}_{n} \times \underbrace{b \cdot b \cdots b}_{n} = a^n b^n$$

*Example:* $(2 \times 5)^3 = 2^3 \times 5^3 = 8 \times 125 = 1000$

### Law 5 — Power of a quotient: $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$

> **WHY:** Same logic as Law 4 but with division.

$$\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n} \qquad (b \neq 0)$$

*Example:* $\left(\dfrac{3}{4}\right)^2 = \dfrac{9}{16}$

### Law 6 — Zero index: $a^0 = 1$

> **WHY (pattern argument):** Watch the powers of 2 descend:
>
> | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
> |-------|-------|-------|-------|-------|
> | 16    | 8     | 4     | 2     | **?** |
>
> Each step divides by 2. So $2^0 = 2 \div 2 = 1$.
>
> **WHY (from Law 2):** $a^n \div a^n = a^{n-n} = a^0$. But any non-zero number divided by itself is 1. So $a^0 = 1$.

$$a^0 = 1 \qquad (a \neq 0)$$

> [!warning] $0^0$ is undefined
> The expression $0^0$ has no agreed-upon value: the "zero index" law says it should be 1, but "$0$ to any power" suggests 0. Most exam boards avoid asking about this edge case, but if pressed, say it is **undefined** (or "indeterminate" at university level).

### Law 7 — Negative index: $a^{-n} = \dfrac{1}{a^n}$

> **WHY (pattern argument):** Continue the pattern from Law 6 downward:
>
> | $2^2$ | $2^1$ | $2^0$ | $2^{-1}$ | $2^{-2}$ |
> |-------|-------|-------|----------|----------|
> | 4     | 2     | 1     | $\dfrac{1}{2}$ | $\dfrac{1}{4}$ |
>
> Each step divides by 2. So $2^{-1} = 1 \div 2 = \dfrac{1}{2}$ and $2^{-2} = \dfrac{1}{2} \div 2 = \dfrac{1}{4}$.
>
> **WHY (from Law 2):** $a^0 \div a^n = a^{0-n} = a^{-n}$. But $a^0 = 1$, so $a^{-n} = \dfrac{1}{a^n}$.

$$a^{-n} = \dfrac{1}{a^n} \qquad (a \neq 0)$$

*Example:* $5^{-3} = \dfrac{1}{5^3} = \dfrac{1}{125}$

> [!tip] Negative index = reciprocal
> A negative index doesn't make the answer negative — it **flips** the number. $2^{-3} = \dfrac{1}{8}$, not $-8$.

---

## §2 Fractional Indices (Extension)

Fractional indices complete the picture by connecting powers to roots.

### $a^{1/n} = \sqrt[n]{a}$

> **WHY (from Law 3):** Let $x = a^{1/n}$. Then $x^n = (a^{1/n})^n = a^{n/n} = a^1 = a$. So $x$ is the number whose $n$th power gives $a$ — that's exactly $\sqrt[n]{a}$.

$$a^{1/2} = \sqrt{a} \qquad a^{1/3} = \sqrt[3]{a} \qquad a^{1/n} = \sqrt[n]{a}$$

### $a^{m/n} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$

> **WHY:** $a^{m/n} = a^{m \cdot (1/n)} = (a^m)^{1/n} = \sqrt[n]{a^m}$. Equally, $a^{m/n} = a^{(1/n) \cdot m} = (a^{1/n})^m = (\sqrt[n]{a})^m$. Both routes give the same answer.

$$8^{2/3} = (\sqrt[3]{8})^2 = 2^2 = 4 \qquad \text{or} \qquad 8^{2/3} = \sqrt[3]{8^2} = \sqrt[3]{64} = 4$$

> [!tip] Root first, power second
> When computing $a^{m/n}$ without a calculator, **root first** (the $1/n$ part) keeps numbers small. Computing $8^{2/3}$: root first gives $\sqrt[3]{8} = 2$, then $2^2 = 4$. Power first gives $8^2 = 64$, then $\sqrt[3]{64} = 4$. Same answer, harder arithmetic.

### Negative fractional indices

Combine Laws 7 and the fractional rule:

$$a^{-m/n} = \dfrac{1}{a^{m/n}} = \dfrac{1}{(\sqrt[n]{a})^m}$$

*Example:* $27^{-2/3} = \dfrac{1}{27^{2/3}} = \dfrac{1}{(\sqrt[3]{27})^2} = \dfrac{1}{3^2} = \dfrac{1}{9}$

### Solving $x^{a/b} = c$ — the reciprocal-power trick

Once fractional indices are in your hand, an entire family of "find $x$" equations collapses to a single calculator move. Given $x^{a/b} = c$, **raise both sides to the reciprocal power $b/a$**:

$$x^{a/b} = c \;\Longrightarrow\; \left(x^{a/b}\right)^{b/a} = c^{b/a} \;\Longrightarrow\; x = c^{b/a}.$$

The exponents $(a/b)(b/a) = 1$ by Law 3, so the left side becomes $x^1 = x$. The right side is just $c$ raised to a (usually clean) fractional power, which any scientific calculator evaluates directly via the $y^x$ / $x^y$ / $\,\hat{}\,$ key.

*Quick demo:* $x^{2/3} = 4 \;\Rightarrow\; x = 4^{3/2} = (\sqrt 4)^3 = 2^3 = 8$. One step, no two-stage "take cube root, then square."

The same move handles negative fractional exponents: $x^{-2/3} = 4 \;\Rightarrow\; x = 4^{-3/2} = \dfrac{1}{4^{3/2}} = \dfrac{1}{8}$.

> [!tip] Why this trick is calculator-proof
> The conventional approach to $x^{a/b} = c$ is two steps: "take the $b$-th root, then raise to the $a$-th power" (or vice versa). Students often get confused about which to do first, lose sign information on intermediate values, or punch the steps in the wrong order on the calculator. The reciprocal-power move sidesteps all of this — **type $c$, hit the power key, type $b/a$, hit equals.** One operation, no ambiguity. Especially useful when $a/b$ is something like $-3/5$ or $7/4$ where the "root then power" approach gets messy mentally but the single power $c^{b/a}$ is still a clean calculator entry.
>
> Standard caveat: the move assumes the principal real root exists — positive base $c$, or an odd denominator on $b/a$ after reduction. Negative bases with fractional exponents are genuinely ambiguous (this is exactly why 0580/0606/A-Level steer clear of them).
>
> See **Example 6** below for two full worked problems using this technique.

---

## §3 Summary Table

| Law | Rule | Condition | Verbal shortcut |
|-----|------|-----------|-----------------|
| 1 | $a^m \times a^n = a^{m+n}$ | same base | multiply → add indices |
| 2 | $a^m \div a^n = a^{m-n}$ | same base, $a \neq 0$ | divide → subtract indices |
| 3 | $(a^m)^n = a^{mn}$ | — | power of power → multiply indices |
| 4 | $(ab)^n = a^n b^n$ | — | power of product → distribute |
| 5 | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ | $b \neq 0$ | power of quotient → distribute |
| 6 | $a^0 = 1$ | $a \neq 0$ | zero power = 1 |
| 7 | $a^{-n} = \dfrac{1}{a^n}$ | $a \neq 0$ | negative power = reciprocal |
| Ext | $a^{m/n} = (\sqrt[n]{a})^m$ | $a > 0$ (if $n$ even) | fraction power = root then power |

---

## §4 Worked Examples

### Example 1 — Simplify $(5x^3)^2$

$$(5x^3)^2 = 5^2 \times (x^3)^2 = 25x^6 \qquad \text{(Laws 4, 3)}$$

### Example 2 — Simplify $\dfrac{12a^5}{3a^{-2}}$

$$\dfrac{12a^5}{3a^{-2}} = 4a^{5-(-2)} = 4a^7 \qquad \text{(Laws 2, 7)}$$

### Example 3 — Evaluate $16^{-3/4}$

$$16^{-3/4} = \dfrac{1}{16^{3/4}} = \dfrac{1}{(\sqrt[4]{16})^3} = \dfrac{1}{2^3} = \dfrac{1}{8}$$

### Example 4 — Solve $2^x = 32$

$$32 = 2^5 \qquad \Rightarrow \qquad 2^x = 2^5 \qquad \Rightarrow \qquad x = 5$$

### Example 5 — Solve $9^x = 27$

$$9 = 3^2, \quad 27 = 3^3 \qquad \Rightarrow \qquad (3^2)^x = 3^3 \qquad \Rightarrow \qquad 3^{2x} = 3^3 \qquad \Rightarrow \qquad x = \dfrac{3}{2}$$

### Example 6 — Solve $x^{2/3} = 9$ (reciprocal-power trick)

Raise both sides to the reciprocal power $3/2$:

$$x^{2/3} = 9 \;\Longrightarrow\; x = 9^{3/2} = (\sqrt 9)^3 = 3^3 = 27.$$

Check: $27^{2/3} = (\sqrt[3]{27})^2 = 3^2 = 9$. ✓

The same move on a negative fractional exponent — **solve $x^{-3/4} = 8$**:

$$x = 8^{-4/3} = \dfrac{1}{8^{4/3}} = \dfrac{1}{(\sqrt[3]{8})^4} = \dfrac{1}{2^4} = \dfrac{1}{16}.$$

On a calculator: $8 \;\hat{}\; (-4 \div 3) = 0.0625 = 1/16$. ✓

**Contrast with Examples 4 and 5.** Those examples solve $b^x = c$ where the **exponent** is the unknown — solved by rewriting both sides with the same base. This example solves $x^{a/b} = c$ where the **base** is the unknown — solved by raising both sides to the reciprocal power. Two structurally distinct problem types, two different moves. Recognising which type a problem is is the first step; the calculator does the rest.

---

## §5 Common Misconceptions (Teaching Notes)

1. **Adding indices when multiplying different bases.** $2^3 \times 3^2 \neq 6^5$. Law 1 requires the **same base**. $2^3 \times 3^2 = 8 \times 9 = 72$ — just multiply the values.

2. **Thinking $a^0 = 0$.** The pattern and the division argument both show $a^0 = 1$. It's the most tested misconception on exams.

3. **Negative index makes a negative answer.** $2^{-3} = \dfrac{1}{8}$, NOT $-8$. The negative index creates a **reciprocal**, not a negative number.

4. **Forgetting to apply the power to the coefficient.** $(3x^2)^3 = 3^3 x^6 = 27x^6$, NOT $3x^6$. The power distributes to everything inside the bracket (Law 4).

5. **Wrong order with fractional indices.** $8^{2/3} \neq 8^2 \div 3$. The denominator is the root, the numerator is the power: $8^{2/3} = (\sqrt[3]{8})^2 = 4$.

6. **Confusing $(a^m)^n$ with $a^m \times a^n$.** $(a^m)^n = a^{mn}$ (multiply indices) but $a^m \times a^n = a^{m+n}$ (add indices). The bracket makes the difference.

7. **Applying Law 1 to addition.** $a^m + a^n \neq a^{m+n}$. The laws only work with multiplication and division, NOT addition and subtraction. There is no "law of indices" for $2^3 + 2^4$.

---

## §6 Exam Notes

### OxAQA 9260

**Syllabus ref:** N6 (Core) — index laws for integer powers. N6 (Extension) — fractional powers. A6 — index laws applied in algebraic expressions.

Both papers allow calculators, but expect students to simplify expressions like $(5x^3)^2$ and $12a^5 \div 3a^{-2}$ algebraically. Solving equations like $2^x = 32$ and $9^x = 27$ by equating bases appears regularly.

### Cambridge 0580 Extended

**Syllabus ref:** E1.7 — positive, zero, negative, and fractional indices. E2.4 — simplification of algebraic expressions using index laws.

Paper 2 (non-calculator): simplify expressions, evaluate without calculator. Paper 4: solve equations involving indices. Typical question: "Simplify $6x^7 y^4 \times 5x^{-5} y$."

### Cambridge 0606

Index laws are **assumed knowledge** from 0580. Not directly tested but needed throughout — particularly for differentiation (the [[Power Rule]] requires rewriting expressions using indices before differentiating, e.g. $\dfrac{1}{x^2} = x^{-2}$).

### AP / IB / A-Level

Index laws are foundational and assumed. At this level, they appear inside logarithm rules ($\log a^n = n \log a$ comes from the index laws), differentiation, and exponential equations. The leap to irrational indices ($a^{\sqrt{2}}$, $a^{\pi}$) and the formal definition via $a^x = e^{x \ln a}$ happen in university analysis.

> [!info] Beyond syllabus — Why does $a^{\pi}$ even make sense?
> The seven laws are proved for integer indices, then extended to fractions via roots. But what about $2^{\pi}$? You can't multiply 2 by itself $\pi$ times. The answer: define $a^x = e^{x \ln a}$ using the exponential function, then verify that all seven laws still hold. This is the rigorous university definition. At IGCSE/IB level, we treat irrational indices as "the limit of rational approximations" — $2^{3.14} \approx 2^{314/100}$, and the calculator handles the rest.

---

## §7 Connections

- **Prerequisite:** [[Powers and Roots (Vocab)]] — defines base, index, square root, cube root
- **Prerequisite:** [[Four Operations (Vocab)]] — multiplication and division underpin the laws
- **Prerequisite:** [[Factors and Multiples (Vocab)]] — HCF/LCM of indices in prime factorisation
- **Leads to:** [[Surds]] — rationalising denominators uses negative and fractional indices
- **Leads to:** [[Algebraic Proof]] — index laws feature in algebraic proof questions
- **Leads to:** [[Power Rule]] — $\dfrac{d}{dx}(x^n) = nx^{n-1}$ requires rewriting using index laws
- **Leads to:** [[Exponential Growth and Decay]] — exponential functions build on index laws
- **Leads to:** [[Binomial Theorem]] — expansion of $(a+b)^n$ uses index manipulation
- **Leads to:** [[Standard Form (Vocab)]] — $a \times 10^n$ is an index law application
- **Parallel:** [[Prime Factorisation (Vocab)]] — writing numbers in index form
- **Parallel:** [[Order of Operations (Vocab)]] — indices come before multiplication in BIDMAS

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $a^n$ | `a^n` | Power / index notation |
| $a^{-n}$ | `a^{-n}` | Negative index |
| $a^{m/n}$ | `a^{m/n}` | Fractional index |
| $\sqrt[n]{a}$ | `\sqrt[n]{a}` | $n$th root (= $a^{1/n}$) |
| $\dfrac{a^m}{a^n}$ | `\dfrac{a^m}{a^n}` | Division of powers |
| $(a^m)^n$ | `(a^m)^n` | Power of a power |
