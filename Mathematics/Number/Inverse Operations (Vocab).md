---
chinese: 逆运算 (nì yùnsuàn)
prerequisites:
  - "[[Four Operations (Vocab)]]"
leads_to:
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Linear Equations (Vocab)]]"
  - "[[Inverse Function]]"
  - "[[Changing the Subject (Vocab)]]"
  - "[[Reciprocals (Vocab)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-N3
  - type/vocabulary
---

# Inverse Operations 逆运算

## Definition

An **inverse operation** (逆运算) undoes what another operation did. A unique undo is possible only when the original action has not lost information; the allowed inputs matter.

| Operation | Inverse | Example |
|-----------|---------|---------|
| Addition ($+$) | Subtraction ($-$) | $5 + 3 = 8 \;\Rightarrow\; 8 - 3 = 5$ |
| Subtraction ($-$) | Addition ($+$) | $10 - 4 = 6 \;\Rightarrow\; 6 + 4 = 10$ |
| Multiplication ($\times$) | Division ($\div$) | $6 \times 4 = 24 \;\Rightarrow\; 24 \div 4 = 6$ |
| Division ($\div$) | Multiplication ($\times$) | $20 \div 5 = 4 \;\Rightarrow\; 4 \times 5 = 20$ |
| Squaring ($n^2$, for $n\ge0$) | Square root ($\sqrt{\phantom{x}}$) | $5^2 = 25 \;\Rightarrow\; \sqrt{25} = 5$ |
| Cubing ($n^3$) | Cube root ($\sqrt[3]{\phantom{x}}$) | $3^3 = 27 \;\Rightarrow\; \sqrt[3]{27} = 3$ |

### 中文锚点

出门时先穿袜子，再穿鞋；回家要脱掉它们，就得先脱鞋，再脱袜子。想回到原来的样子，不能照着刚才的顺序再做一遍，而要从最后一步往回拆。逆运算也是这样：把刚才做的动作倒着一步步撤回去，找回起初的那个数。

> [!tip] Why this matters
> Solving equations is built entirely on inverse operations. To isolate $x$ in $3x + 5 = 20$, you undo the $+5$ (subtract 5), then undo the $\times 3$ (divide by 3). The whole "balance method" is just applying inverse operations to both sides.

> [!warning] Zero breaks the pattern
> Multiplication and division are inverses — *except when zero is involved*.
>
> **Multiplying by 0 destroys information:** $7 \times 0 = 0$ and $3 \times 0 = 0$ both give 0. You can't undo it — which original number was it? This is why $\dfrac{0}{0}$ is undefined (not 1).
>
> **Dividing by 0 is undefined:** there is no number $x$ such that $0 \times x = 5$, so $5 \div 0$ has no answer. Your calculator says "Error" for a reason.
>
> These aren't just edge cases — they're the reason "$a \neq 0$" appears as a condition throughout the [[Laws of Indices]] and algebra in general.

> [!warning] Squaring also loses information unless you restrict the inputs
> Both $5$ and $-5$ square to $25$. The principal square root returns $5$, so $\sqrt{x^2}=|x|$, not always $x$. Square root undoes squaring on **nonnegative inputs**. Multiplying or dividing by a fixed number has an inverse only when that fixed number is nonzero.

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| inverse | 逆 (nì) | The "opposite" operation |
| undo | 撤销 (chèxiāo) | Informal: inverse operations "undo" each other |
| cancel / cancellation | 消去 (xiāoqù) | When an operation and its inverse meet: $+5 - 5 = 0$ |
| self-inverse | 自逆 (zì nì) | An operation that is its own inverse: negation ($-(-x) = x$), reciprocal ($1/(1/x) = x$, $x\ne0$) |

## Exam Notes

### OxAQA 9260
**N3 (Core and Extension)** explicitly names relationships between operations, including inverses and cancellation. This is directly prescribed content, as well as a tool for solving equations and rearranging formulas. Undo the last operation first, and preserve equality by applying each step to both sides.

### Cambridge 0580 — Core and Extended
**C1.6 / E1.6** prescribe the four operations; **C2.5 / E2.5** require equation solving and changing the subject. Inverses supply the method. When solving $x^2=25$, both $x=5$ and $x=-5$ are possible; evaluating $\sqrt{25}$ asks for the nonnegative root only.

### Other boards — arithmetic tool versus inverse functions
**Cambridge 0606 / 9709 / 9231, Edexcel IAL, OxAQA 9660, IB AA / AI and AP Calculus AB / BC** use arithmetic inverses throughout their algebra; none sets a standalone unit on memorising pairs of inverse arithmetic operations. This does **not** exclude [[Inverse Function]], where existence, domains and functional notation are distinct examinable questions. IB AA / AI (first assessment 2021) place elementary arithmetic and simple equation solving in *Prior learning*; AP Calculus expects prior algebra and functions.

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — the operations being inverted
- **Leads to:** [[Inverse Function]] — $f^{-1}$ undoes $f$, the function-level version of this idea
- **Parallel:** [[Laws of Indices]] — negative indices ($a^{-n} = 1/a^n$) are the multiplicative inverse applied to powers

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\sqrt{a}$ | `\sqrt{a}` | Inverse of squaring on nonnegative inputs |
| $\sqrt[3]{a}$ | `\sqrt[3]{a}` | Inverse of cubing |
