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

An **inverse operation** (逆运算) undoes what another operation did. Every operation has a partner that reverses its effect.

| Operation | Inverse | Example |
|-----------|---------|---------|
| Addition ($+$) | Subtraction ($-$) | $5 + 3 = 8 \;\Rightarrow\; 8 - 3 = 5$ |
| Subtraction ($-$) | Addition ($+$) | $10 - 4 = 6 \;\Rightarrow\; 6 + 4 = 10$ |
| Multiplication ($\times$) | Division ($\div$) | $6 \times 4 = 24 \;\Rightarrow\; 24 \div 4 = 6$ |
| Division ($\div$) | Multiplication ($\times$) | $20 \div 5 = 4 \;\Rightarrow\; 4 \times 5 = 20$ |
| Squaring ($n^2$) | Square root ($\sqrt{\phantom{x}}$) | $5^2 = 25 \;\Rightarrow\; \sqrt{25} = 5$ |
| Cubing ($n^3$) | Cube root ($\sqrt[3]{\phantom{x}}$) | $3^3 = 27 \;\Rightarrow\; \sqrt[3]{27} = 3$ |

### 中文锚点

逆运算 = 把另一个运算"倒回去"的运算。加法的逆是减法，乘法的逆是除法，平方的逆是开平方。

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

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| inverse | 逆 (nì) | The "opposite" operation |
| undo | 撤销 (chèxiāo) | Informal: inverse operations "undo" each other |
| cancel / cancellation | 消去 (xiāoqù) | When an operation and its inverse meet: $+5 - 5 = 0$ |
| self-inverse | 自逆 (zì nì) | An operation that is its own inverse: negation ($-(-x) = x$), reciprocal ($1/(1/x) = x$) |

## Exam Notes

### OxAQA 9260 / Cambridge 0580
Not directly examined as a standalone topic, but inverse operations are the foundation of equation solving (A19–A22) and rearranging formulae (A2). Students who struggle with algebra almost always have a gap here.

## Connections

- **Prerequisite:** [[Four Operations (Vocab)]] — the operations being inverted
- **Leads to:** [[Inverse Function]] — $f^{-1}$ undoes $f$, the function-level version of this idea
- **Parallel:** [[Laws of Indices]] — negative indices ($a^{-n} = 1/a^n$) are the multiplicative inverse applied to powers

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\sqrt{a}$ | `\sqrt{a}` | Inverse of squaring |
| $\sqrt[3]{a}$ | `\sqrt[3]{a}` | Inverse of cubing |
