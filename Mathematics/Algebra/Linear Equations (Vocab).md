---
chinese: 一次方程 (yīcì fāngchéng)
prerequisites:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Inverse Operations (Vocab)]]"
  - "[[Expanding Brackets (Vocab)]]"
  - "[[Linear Graphs (Vocab)]]"
leads_to:
  - "[[Simultaneous Equations (Vocab)]]"
  - "[[Linear Inequalities (Vocab)]]"
  - "[[Changing the Subject (Vocab)]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Quadratic Equations]]"
  - "[[Fractional Equations (Vocab)]]"
  - "[[Modulus Function]]"
  - "[[Recurring Decimals (Vocab)]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-A19
  - syllabus/0580-E2-5
  - type/vocabulary
  - misconception/sign-error-moving-terms
  - misconception/dividing-before-isolating
---

# Linear Equations 一次方程

## Definition

A **linear equation** (一次方程) is an equation where the highest power of the unknown is $1$ — no $x^2$, no $\sqrt{x}$, no $\dfrac{1}{x}$. It contains an equals sign and one (or more) unknowns.

$$3x + 5 = 14 \qquad \qquad 2(x - 1) = x + 7$$

The **solution** (also called the **root**) is the value of $x$ that makes both sides equal. Linear equations in one unknown have exactly one solution (unless the equation is degenerate — see below).

### 中文锚点

一次方程 = 未知数的最高次数是 1 的方程。"解方程"就是找出让两边相等的 $x$ 值。方法是"天平法"：两边做同样的事，一步一步把 $x$ 单独留在一边。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| **equation** | 方程 (fāngchéng) | Has an $=$ sign (unlike an expression) |
| **linear** | 一次的 / 线性的 (yīcì de) | Highest power of the unknown is $1$ |
| **solve** | 解 (jiě) | Find the value(s) of the unknown |
| **unknown** | 未知数 (wèizhīshù) | The letter whose value we are finding |
| **solution / root** | 解 / 根 (jiě / gēn) | The value that satisfies the equation |
| **satisfy** | 满足 (mǎnzú) | A value "satisfies" the equation if it makes it true |
| **balance method** | 平衡法 (pínghéng fǎ) | Do the same thing to both sides |
| **isolate** | 分离 (fēnlí) | Get the unknown alone on one side |
| **rearrange** | 整理 (zhěnglǐ) | Reshuffle the equation into a useful form |
| **verify / check** | 验证 (yànzhèng) | Substitute the answer back to confirm |

---

## The Balance Method

An equation is a **balanced scale**. Whatever you do to the left, you must do to the right — otherwise the scale tips and the equation becomes false.

**The four legal moves (applied to both sides):**
1. Add the same quantity
2. Subtract the same quantity
3. Multiply by the same non-zero quantity
4. Divide by the same non-zero quantity

> [!tip] Undo operations in reverse order
> To isolate $x$ in $3x + 5 = 14$, peel back the operations in the opposite order they were applied. The expression "multiplied $x$ by 3, then added 5" — so undo by first subtracting 5, then dividing by 3. This is exactly the [[Inverse Operations (Vocab)|inverse-operations]] idea.

---

## Standard Forms and Strategies

| Form | Example | Strategy |
|------|---------|----------|
| $ax + b = c$ | $3x + 5 = 14$ | Subtract $b$, divide by $a$ |
| $ax + b = cx + d$ | $5x - 2 = 2x + 7$ | Collect $x$ on one side, numbers on the other |
| With brackets | $2(x - 1) = x + 7$ | [[Expanding Brackets (Vocab)\|Expand]] first, then solve |
| With fractions | $\dfrac{x+1}{2} = \dfrac{x-3}{5}$ | Multiply both sides by the LCM of denominators (here $\times 10$) |
| Unknown on both sides + fractions | $\dfrac{2x-1}{3} = \dfrac{x+4}{2}$ | Cross-multiply: $(2x-1)\cdot 2 = (x+4)\cdot 3$ |

**Worked example (brackets + fractions):**

$$\frac{3(x - 2)}{4} = \frac{x + 1}{2}$$

Multiply both sides by $4$: $\; 3(x-2) = 2(x+1)$
Expand: $\; 3x - 6 = 2x + 2$
Collect: $\; x = 8$. Check: $\dfrac{3(6)}{4} = \dfrac{9}{2}$ ✓ $\dfrac{9}{2} = \dfrac{9}{2}$ ✓

---

## Degenerate Cases (know these exist)

| Equation | Simplifies to | Meaning |
|----------|---------------|---------|
| $2x + 3 = 2x + 5$ | $3 = 5$ (false) | **No solution** — the unknown cancels and you're left with a lie |
| $2(x + 1) = 2x + 2$ | $0 = 0$ (always true) | **Infinitely many solutions** — every $x$ works (it's an [[Algebraic Expressions (Vocab)\|identity]]) |

---

## Common Mistakes

> [!warning] Sign errors when moving terms
> "Move $-3x$ to the other side and it becomes $+3x$." Correct — but students forget to flip *every* sign on the term: $-3x + 5 \neq +3x + 5$ after subtraction. Writing out the balance step explicitly ($+3x$ on both sides) prevents the error.

> [!warning] Dividing before isolating
> In $3x + 5 = 14$, dividing everything by 3 first gives $x + \dfrac{5}{3} = \dfrac{14}{3}$ — technically correct, but now you've introduced ugly fractions. The cleaner move: subtract 5 first, then divide.

> [!warning] Dropping the denominator
> $\dfrac{x+1}{2} = 5$ does **not** mean $x + 1 = 5$. Multiply both sides by 2: $x + 1 = 10$, so $x = 9$.

---

## Exam Phrasing

- "**Solve** the equation $3x + 5 = 14$." — Find $x$.
- "**Find the value of $x$** such that $\ldots$" — Same instruction, different wording.
- "Given that $f(x) = \ldots$, find the value(s) of $x$ for which $f(x) = 0$." — Solve $f(x) = 0$.
- "Show that $x = \ldots$ satisfies $\ldots$" — Substitute and verify both sides equal.

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E2.5. Linear equations in one unknown. Typically 2–3 marks. Common traps: brackets ("expand and solve"), fractions ("multiply through by LCM first"), unknown on both sides.

### OxAQA 9260

**Syllabus ref:** A19. Linear equations in one unknown, algebraically. A20 mentions solving by reading from a graph (approximate solutions).

### Cambridge 0606 (Assumed knowledge)

0606 assumes mastery of 0580 linear equations. They appear as sub-steps inside larger problems — solving for stationary points, finding where two curves meet, rearranging after expanding. No longer assessed standalone, but required daily.

---

## Connections

- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — an equation is two expressions joined by $=$
- **Prerequisite:** [[Inverse Operations (Vocab)]] — the machinery behind the balance method
- **Prerequisite:** [[Expanding Brackets (Vocab)]] — needed whenever brackets appear
- **Leads to:** [[Simultaneous Equations (Vocab)]] — two linear equations at once
- **Leads to:** [[Linear Inequalities (Vocab)]] — same balance method, but $\div$ by a negative flips the sign
- **Leads to:** [[Changing the Subject (Vocab)]] — same moves, applied to a formula with several letters
- **Leads to:** [[Equation of a Straight Line (Vocab)]] — $y = mx + c$ is a linear equation in two variables
- **Parallel:** [[Quadratic Equations]] — the non-linear cousin (power 2)

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{a}{b}$ | `\dfrac{a}{b}` | Display-size fraction in inline math |
| $\Rightarrow$ | `\Rightarrow` | "Implies" — useful in multi-step solutions |
