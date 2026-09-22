---
chinese: 公式变形 (gōngshì biànxíng)
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

# Changing the Subject 公式变形

## Definition

The **subject** of a formula is the variable that stands alone on one side, expressed in terms of everything else. In $v = u + at$, the subject is $v$. **Changing the subject** means rearranging the formula so a *different* variable stands alone.

Make $t$ the subject: $\;v = u + at \;\Rightarrow\; v - u = at \;\Rightarrow\; t = \dfrac{v - u}{a}$

Here $a\ne0$; if $a=0$, the original equation says $v=u$ and does not determine $t$.

The formula hasn't changed — it still describes the same relationship. You've just turned it around to answer a different question.

### 中文锚点

先把打车费想简单一点：固定起步费，再加上每公里的钱。平时你拿路程算车费；现在口袋里只有这么多钱，想问的却是“够坐多远？”先扣掉起步费，再用剩下的钱除以每公里的价格，就能反过来算路程。收费关系一点没变，只是原来拿来算答案的数，现在成了你要找的答案。公式变形就是这样，把原先的计算倒着拆开，让想知道的那个量单独留在等号一边。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| subject (of a formula) | 公式中被单独表示的量 | The isolated variable on one side |
| rearrange | 变形 / 移项 (yíxiàng) | Rewrite the formula with a different subject |
| isolate | 隔离 (gélí) | Get the target variable alone |
| transpose | 移项 (yíxiàng) | Move a term to the other side (older UK usage) |
| make $x$ the subject | 把公式变形成 $x = \cdots$ | The standard exam phrasing |
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

The original fraction requires $x\ne2$; the rearranged one requires $y\ne3$. Indeed, setting $y=3$ in the original would require $-6=1$, so no such solution exists.

The key move: **factor out $x$** from the left side. This is [[Factorising (Vocab)]] in disguise — common factor extraction, applied to a formula instead of a polynomial.

### Rearrangements involving squares and roots

**Example:** Make $r$ the subject of $\;A = \pi r^2$.

$$r^2 = \dfrac{A}{\pi} \;\Rightarrow\; r = \sqrt{\dfrac{A}{\pi}}$$

We take the non-negative root (with $A\ge0$) because $r$ is a radius (length). In pure algebra, $r = \pm\sqrt{A/\pi}$ — context decides.

### Beyond IGCSE — when exponentials and logarithms enter

At 0606, A-Level, and IB, rearrangements routinely involve exponentials and logarithms as inverse operations — $\ln$ undoes $e^x$ the way $\sqrt{}$ undoes squaring. For instance, making $t$ the subject of $P = P_0 e^{kt}$ requires $P_0\ne0$, $P/P_0>0$ and $k\ne0$. Then take $\ln$ after dividing by $P_0$:

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

### Later study

Rearrangement is reused inside later algebra, functions and calculus problems; it does not disappear when the question has a different topic heading.

---

## Connections

- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — the language of terms and operations
- **Prerequisite:** [[Inverse Operations (Vocab)]] — every rearrangement step is an inverse operation
- **Leads to:** [[Simultaneous Equations (Vocab)]] — substitution method requires rearranging one equation first
- **Leads to:** [[Inverse Function]] — finding $f^{-1}(x)$ is literally "make $x$ the subject of $y = f(x)$, then swap $x$ and $y$"
- **Parallel:** [[Factorising (Vocab)]] — factoring out the target variable when it appears twice
