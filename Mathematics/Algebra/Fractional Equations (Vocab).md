---
chinese: 分式方程 (fēnshì fāngchéng)
prerequisites:
  - "[[Linear Equations (Vocab)]]"
  - "[[Algebraic Fractions (Vocab)]]"
  - "[[Factorising (Vocab)]]"
leads_to:
  - "[[Quadratic Equations]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/0580-E2-5
  - syllabus/9260-A19
  - type/vocabulary
  - misconception/extraneous-solution
  - misconception/forgetting-to-check-denominator
---

# Fractional Equations 分式方程

## Definition

A **fractional equation** (分式方程) is an equation where the unknown appears in at least one denominator:

$$\dfrac{2}{x - 1} + \dfrac{3}{x + 2} = 1$$

These are NOT the same as [[Linear Equations (Vocab)|linear equations with numerical fractions]] like $\dfrac{x+1}{2} = 5$ (where $x$ is only on top). The unknown in a denominator creates two new concerns: **clearing the fraction** and **checking for extraneous solutions**.

### 中文锚点

分式方程 = 未知数出现在分母里的方程。解法：两边同乘分母的最小公倍数（LCM），把方程变成整式方程。关键警告：**必须验根** — 让原分母为零的值必须舍去，即使它让新方程成立。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| **fractional equation** | 分式方程 (fēnshì fāngchéng) | Unknown in a denominator |
| **clear fractions** | 去分母 (qù fēnmǔ) | Multiply both sides by the LCM of denominators |
| **LCM of denominators** | 分母的最小公倍数 | Smallest expression both denominators divide into |
| **extraneous solution** | 增根 (zēng gēn) | A value that solves the cleared equation but NOT the original — it must be rejected |
| **valid solution** | 有效解 (yǒuxiào jiě) | Satisfies the original equation AND keeps every denominator non-zero |
| **excluded value** | 排除值 / 禁止值 | A value of $x$ that makes some denominator zero — always forbidden |

---

## The Technique — Clear, Solve, Check

**Step 1 — Identify excluded values.** Look at every denominator and note the $x$-values that would make it zero. These are permanently off-limits.

**Step 2 — Multiply both sides by the LCM of denominators.** This clears the fractions. You now have a [[Linear Equations (Vocab)|linear]] or [[Quadratic Equations|quadratic]] equation.

**Step 3 — Solve the cleared equation.**

**Step 4 — Check each answer.** Discard any that match an excluded value from Step 1.

> [!tip] Why clearing fractions works
> If $A = B$ is true, then $A \cdot k = B \cdot k$ is also true — multiplying both sides by the same non-zero quantity preserves equality. The LCM is the smallest $k$ that wipes every denominator simultaneously.

---

## Worked Example 1 — Reduces to Linear

$$\dfrac{3}{x} + \dfrac{5}{2x} = 1$$

**Step 1 — excluded values:** $x \neq 0$.

**Step 2 — multiply both sides by $2x$** (the LCM of $x$ and $2x$):
$$2x \cdot \dfrac{3}{x} + 2x \cdot \dfrac{5}{2x} = 2x \cdot 1$$
$$6 + 5 = 2x$$
$$x = \dfrac{11}{2}$$

**Step 4 — check:** $\dfrac{11}{2} \neq 0$ ✓. Verify in the original: $\dfrac{3}{11/2} + \dfrac{5}{11} = \dfrac{6}{11} + \dfrac{5}{11} = 1$ ✓

---

## Worked Example 2 — Reduces to Quadratic (and extraneous root check matters)

$$\dfrac{1}{x - 3} + \dfrac{1}{x + 3} = \dfrac{6}{x^2 - 9}$$

**Step 1 — excluded values:** $x^2 - 9 = (x-3)(x+3)$, so $x \neq 3$ and $x \neq -3$.

**Step 2 — LCM of denominators is $(x-3)(x+3)$.** Multiply through:
$$(x+3) + (x-3) = 6$$
$$2x = 6 \;\Rightarrow\; x = 3$$

**Step 4 — check:** $x = 3$ is an excluded value — it makes the first denominator zero. ❌ **Reject it.** The equation has **no solution**.

> [!warning] This is the archetype of an extraneous solution
> The cleared equation was honest — $2x = 6$ really does follow from the multiplication. But the multiplication itself is only valid when $x \neq \pm 3$. At $x = 3$ the original equation is undefined, so that value cannot be a solution no matter what the cleared equation says.

---

## Worked Example 3 — Proper Quadratic Case

$$\dfrac{2}{x - 1} + \dfrac{3}{x + 2} = 1$$

**Step 1 — excluded:** $x \neq 1$, $x \neq -2$.

**Step 2 — LCM is $(x-1)(x+2)$:**
$$2(x+2) + 3(x-1) = (x-1)(x+2)$$
$$2x + 4 + 3x - 3 = x^2 + x - 2$$
$$5x + 1 = x^2 + x - 2$$
$$x^2 - 4x - 3 = 0$$

**Step 3 — [[Quadratic Equations|quadratic formula]]:**
$$x = \dfrac{4 \pm \sqrt{16 + 12}}{2} = \dfrac{4 \pm 2\sqrt{7}}{2} = 2 \pm \sqrt{7}$$

**Step 4 — check:** $2 + \sqrt{7} \approx 4.65$ and $2 - \sqrt{7} \approx -0.65$. Neither is $1$ or $-2$ ✓. Both are valid solutions.

---

## Common Mistakes

> [!warning] Forgetting the extraneous check
> The most exam-costly error. Students clear fractions, solve, and stop. If an answer hits an excluded value, they still write it down. **Always** list excluded values before solving and compare answers against the list at the end.

> [!warning] Dropping a fraction you didn't multiply by
> When the LCM is $(x-1)(x+2)$, every term on both sides must be multiplied by that full expression. Partial multiplication — multiplying only the left side, or only some terms — breaks the equation.

> [!warning] Cancelling before clearing
> $\dfrac{2}{x-1} = \dfrac{3}{x+2}$ does NOT simplify by "cancelling the $x$'s." You must cross-multiply: $2(x+2) = 3(x-1)$, giving $2x + 4 = 3x - 3$, so $x = 7$.

---

## Exam Phrasing

- "**Solve** $\dfrac{1}{x} + \dfrac{1}{x-2} = \dfrac{3}{4}$"
- "**Find the value(s) of $x$** for which $\ldots$"
- "Solve the equation, giving your answer **in exact form**" — keep surds rather than rounding
- "Solve the equation, giving your answer **to 2 decimal places**" — use a calculator on the final quadratic

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E2.5.3, in the syllabus's own words: "solve fractional equations with numerical and **linear** algebraic denominators." The word *linear* is a real boundary — denominators like $2x+1$ and $x+2$ are examined (the syllabus's own examples are $\frac{x}{2x+1} = 4$ and $\frac{2}{x+2} + \frac{3}{2x-1} = 1$), quadratic denominators are not. Typically 3–5 marks: one for clearing fractions correctly, one for simplifying, one or two for solving, one for the final answer (and implicitly for rejecting any extraneous root).

### OxAQA 9260

**Syllabus ref:** A19. Same technique; fractional equations reduce to linear or quadratic, which are then solved by standard means.

### Cambridge 0606 (Assumed)

0606 uses fractional equations freely inside larger problems — intersections of rational curves with lines, equations arising from rate problems, partial-fractions setups. Not tested standalone, but the extraneous-root discipline remains essential. The same is true from 9709 upward: fully assumed, never a question of its own.

---

## Connections

- **Prerequisite:** [[Linear Equations (Vocab)]] — the cleared equation is often linear
- **Prerequisite:** [[Algebraic Fractions (Vocab)]] — you need to find the LCM of denominators and spot common factors like $x^2 - 9 = (x-3)(x+3)$
- **Prerequisite:** [[Factorising (Vocab)]] — the cleared quadratic is solved by factorising (or the formula)
- **Leads to:** [[Quadratic Equations]] — the cleared equation is often quadratic
- **Parallel:** [[Simultaneous Equations (Vocab)]] — non-linear simultaneous systems often contain fractional equations
- **Parallel:** [[Function]] — domain restrictions ($x \neq$ any value that makes a denominator zero) come from the same place as excluded values here

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{a}{b}$ | `\dfrac{a}{b}` | Display-size fraction |
| $\neq$ | `\neq` | "Not equal to" — for stating excluded values |
| $\pm$ | `\pm` | Plus-or-minus (quadratic formula output) |
