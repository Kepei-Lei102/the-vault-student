---
chinese: 一次不等式 (yīcì bùděngshì)
prerequisites:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Linear Equations (Vocab)]]"
  - "[[Ordering and Inequalities Notation (Vocab)]]"
  - "[[Set-Builder Notation]]"
leads_to:
  - "[[Graphical Inequalities (Vocab)]]"
  - "[[Modulus Function]]"
  - "[[Quadratic Inequalities]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A23
  - syllabus/0580-E2-6
  - type/vocabulary
  - misconception/flip-inequality-when-dividing-negative
---

# Linear Inequalities 一次不等式

## Definition

A **linear inequality** (一次不等式) looks like a linear equation but with an inequality sign instead of $=$. It describes a **range** of values rather than a single solution.

$$2x + 3 > 7 \qquad \Rightarrow \qquad x > 2$$

The solution is not a point but an **interval** — every number greater than $2$ works.

### 中文锚点

不等式 = 含有 $<, >, \leq, \geq$ 的式子。解不等式和解方程一样"两边做同样的事"，但有一条关键规则：**两边乘以或除以负数时，不等号要反向**。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| inequality | 不等式 (bùděngshì) | A statement that two expressions are not equal |
| strict inequality | 严格不等式 | $<$ or $>$ — the boundary value is **not** included |
| weak inequality | 非严格不等式 | $\leq$ or $\geq$ — the boundary value **is** included |
| solve | 解 (jiě) | Find the range of values that satisfy the inequality |
| number line | 数轴 (shùzhóu) | Used to represent the solution set visually |
| open circle ○ | 空心圆 | Marks a value that is **not** included ($<$ or $>$) |
| closed circle ● | 实心圆 | Marks a value that **is** included ($\leq$ or $\geq$) |
| integer values | 整数值 | "List the integer values of $n$ that satisfy…" |
| double inequality | 双重不等式 | $3 < x \leq 7$ — $x$ is trapped between two bounds |

---

## Solving — Same as Equations, With One Extra Rule

Solve an inequality exactly as you solve an equation: add, subtract, multiply, divide both sides by the same thing. **Except:**

> [!warning] THE rule — reverse the sign when multiplying or dividing by a negative
> $$-2x > 6 \;\Rightarrow\; x < -3$$
> The inequality **flips** from $>$ to $<$.

> [!tip] WHY does the sign flip?
> Multiplying by $-1$ reflects the number line: numbers that were "to the right" (larger) land "to the left" (smaller). If $a > b$, then $-a < -b$. Try it: $5 > 3$, but $-5 < -3$. The reflection reverses the order. This is the same reason the number line "mirrors" around zero.

**Example — double inequality:** Solve $-3 \leq 2x - 1 < 7$.

Work on all three parts at once: add $1$ throughout, then divide by $2$:

$$-2 \leq 2x < 8 \;\Rightarrow\; -1 \leq x < 4$$

On a number line: closed circle at $-1$, open circle at $4$, solid line between them.

**Example — "list the integers":** List the integer values of $n$ satisfying $-1 \leq n < 4$.

$n = -1, 0, 1, 2, 3$ (not $4$ — the circle at $4$ is open).

---

## Common Mistakes

1. **Forgetting to flip when dividing by a negative.** The #1 error. $-3x \geq 12$ gives $x \leq -4$, not $x \geq -4$.
2. **Including the boundary on the wrong end.** In $-1 \leq x < 4$, the $-1$ is included (closed circle, $\leq$) but $4$ is not (open circle, $<$). Read the symbols.
3. **Number line notation mix-up.** Open circle = not included ($<, >$). Closed circle = included ($\leq, \geq$). Some textbooks use arrows; 9260/0580 use circles.

---

## Exam Notes

### OxAQA 9260 / Cambridge 0580

**Syllabus ref:** A23 (9260) / E2.6 (0580). Questions typically: (a) solve a linear inequality [1–2 marks], (b) represent on a number line [1 mark], (c) list integer values [1 mark]. Double inequalities are common. The question "list the integers that satisfy $-2 < n \leq 3$" is almost guaranteed on every paper.

### Cambridge 0606 Additional Maths

Assumed from 0580 and not examined on its own — but it is the last line of most 0606 inequality questions: a quadratic, modulus or cubic inequality is *reduced* to a linear one and then finished exactly as above ([[Quadratic Inequalities]], [[Modulus Function]]).

---

## Connections

- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — the language of terms and operations
- **Leads to:** [[Graphical Inequalities (Vocab)]] — extending 1D inequalities to 2D regions on the coordinate plane
- **Parallel:** [[Quadratic Equations]] — quadratic inequalities (A-Level) combine this sign-flipping rule with parabola sketching
