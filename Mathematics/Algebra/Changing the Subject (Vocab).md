---
chinese: 变换主元 (biànhuàn zhǔyuán)
prerequisites:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Inverse Operations (Vocab)]]"
  - "[[Linear Equations (Vocab)]]"
leads_to:
  - "[[Simultaneous Equations (Vocab)]]"
  - "[[Inverse Function]]"
  - "[[Direct and Inverse Proportion (Vocab)]]"
  - "[[Logarithms]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-A2
  - syllabus/0580-E2-5
  - type/vocabulary
  - misconception/square-root-both-sides-forgetting-pm
---

# Changing the Subject 变换主元

## Definition

The **subject** of a formula is the variable that stands alone on one side, expressed in terms of everything else. In $v = u + at$, the subject is $v$. **Changing the subject** means rearranging the formula so a *different* variable stands alone.

Make $t$ the subject: $\;v = u + at \;\Rightarrow\; v - u = at \;\Rightarrow\; t = \dfrac{v - u}{a}$

The formula hasn't changed — it still describes the same relationship. You've just turned it around to answer a different question.

### 中文锚点

变换主元 = 把公式变形，让另一个变量单独在等号一边。方法和解方程一模一样："两边做相同的运算"，用逆运算一步步剥离。英文说 "make $x$ the subject" = "把 $x$ 变成主元"。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| subject (of a formula) | 主元 (zhǔyuán) | The isolated variable on one side |
| rearrange | 变形 / 移项 (yíxiàng) | Rewrite the formula with a different subject |
| isolate | 隔离 (gélí) | Get the target variable alone |
| transpose | 移项 (yíxiàng) | Move a term to the other side (older UK usage) |
| make $x$ the subject | 把 $x$ 变成主元 | The standard exam phrasing |
| inverse operation | 逆运算 (nì yùnsuàn) | Undo: $+$ undone by $-$, $\times$ by $\div$, square by $\sqrt{}$ |

---

## The Principle

Rearranging a formula uses exactly the same logic as solving an equation: **undo operations in reverse order** using [[Inverse Operations (Vocab)]]. The only difference is that the answer contains letters, not numbers.

> [!tip] WHY "reverse order"?
> Operations are applied to the variable in a specific order (like layers). To unwrap the variable, you peel layers off from the outside in — last applied, first undone. This is the same idea behind [[Inverse Function]] (applying $f^{-1}$ undoes $f$) and behind how a computer evaluates an expression (stack-based, last-in-first-out).

### Harder rearrangements — when the target appears more than once

If the variable you want appears in **two or more places**, collect it first, then factor it out.

**Example:** Make $x$ the subject of $\;y = \dfrac{3x + 1}{x - 2}$.

$$y(x - 2) = 3x + 1 \;\Rightarrow\; yx - 2y = 3x + 1 \;\Rightarrow\; yx - 3x = 1 + 2y$$

$$x(y - 3) = 1 + 2y \;\Rightarrow\; x = \dfrac{1 + 2y}{y - 3}$$

The key move: **factor out $x$** from the left side. This is [[Factorising (Vocab)]] in disguise — common factor extraction, applied to a formula instead of a polynomial.

### Rearrangements involving squares and roots

**Example:** Make $r$ the subject of $\;A = \pi r^2$.

$$r^2 = \dfrac{A}{\pi} \;\Rightarrow\; r = \sqrt{\dfrac{A}{\pi}}$$

We take the positive root because $r$ is a radius (length). In pure algebra, $r = \pm\sqrt{A/\pi}$ — context decides.

### Beyond IGCSE — when exponentials and logarithms enter

At 0606, A-Level, and IB, rearrangements routinely involve exponentials and logarithms as inverse operations — $\ln$ undoes $e^x$ the way $\sqrt{}$ undoes squaring. For instance, making $t$ the subject of $P = P_0 e^{kt}$ requires taking $\ln$ of both sides:

$$\frac{P}{P_0} = e^{kt} \;\Rightarrow\; \ln\!\left(\frac{P}{P_0}\right) = kt \;\Rightarrow\; t = \frac{1}{k}\ln\!\left(\frac{P}{P_0}\right)$$

This gets considerably harder once you are solving differential equations, where rearranging to isolate a variable can involve separating variables, integrating both sides, and then exponentiating back — a multi-step unwrapping that builds directly on the principle you learn here. The core logic ("undo operations in reverse order") is the same; the operations just get more powerful.

---

## Common Mistakes

1. **Not applying an operation to every term.** When multiplying both sides by $(x-2)$, the **entire** right side gets multiplied, not just part of it.
2. **Forgetting $\pm$ when square-rooting.** $x^2 = 9 \Rightarrow x = \pm 3$ in general. But if context demands positive (length, time), take the positive root only.
3. **Target variable appears twice — panicking instead of collecting.** The strategy is always: get all terms with the target on one side, everything else on the other, then factor. It's mechanical once you see the pattern.

---

## Exam Notes

### Cambridge 0580 Extended

**Syllabus ref:** E2.5 #7 (Equations): "change the subject of formulas" — the syllabus's own difficulty markers are exactly the two escalations to drill: *the subject appears twice* (requiring factorising it out) and *there is a power or root of the subject*. (Core C2.5 #4 keeps it to subject-once, no powers.) Appears as "Make $x$ the subject of…" for 2–4 marks; a common 3-mark shape: a fraction, then a square root.

### OxAQA 9260

**Syllabus ref:** A2: "transform simple formulae" (core) escalating to "transform complex formulae **including when the subject appears twice**" (extension) — the same two-step ladder in the board's own words.

### Where it is *not* examined

Never a standalone question beyond IGCSE — 0606, 9709 and the A-Level boards assume rearrangement silently inside every solve-for-$x$ step.

---

## Connections

- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — the language of terms and operations
- **Prerequisite:** [[Inverse Operations (Vocab)]] — every rearrangement step is an inverse operation
- **Leads to:** [[Simultaneous Equations (Vocab)]] — substitution method requires rearranging one equation first
- **Leads to:** [[Inverse Function]] — finding $f^{-1}(x)$ is literally "make $x$ the subject of $y = f(x)$, then swap $x$ and $y$"
- **Parallel:** [[Factorising (Vocab)]] — factoring out the target variable when it appears twice
