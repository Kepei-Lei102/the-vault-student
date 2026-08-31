---
chinese: 指数函数图像 (zhǐshù hánshù túxiàng)
prerequisites:
  - "[[Laws of Indices]]"
  - "[[Sketching Curves (Vocab)]]"
  - "[[Exponential Growth and Decay]]"
leads_to:
  - "[[Graphs of Functions]]"
  - "[[Logarithms]]"
  - "[[Exponential Function]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-A12
  - syllabus/9260-A12-Ext
  - syllabus/0580-E2-10
  - type/vocabulary
  - notation/exponential
  - notation/asymptote
  - misconception/exponential-vs-polynomial
---

# Exponential Graphs 指数函数图像

## Definition

An **exponential graph** is the curve of $y = a \cdot b^x$, where the variable $x$ sits in the *exponent* rather than the base. The key shape facts: the curve never touches the $x$-axis, it passes through $(0, a)$, and it either rises steeply (growth, $b > 1$) or falls toward zero (decay, $0 < b < 1$).

On exams, "exponential" is a *shape word* — like "parabola" or "cubic" — and the examiner expects you to recognise it from the equation alone.

### 中文锚点

**指数函数 (zhǐshù hánshù)** = exponential function. The variable is the 指数 (exponent), not the 底 (base). This is the exact contrast that matters: 幂函数 (power function, $y = x^n$) has the variable in the base; 指数函数 has it in the exponent. Chinese exams often test both on the same paper — English exams do too, using the words "exponential" vs "polynomial" to distinguish them.

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| exponential (adj. or noun) | 指数的, 指数函数 | Variable is in the exponent: $y = b^x$ |
| base (of an exponential) | 底 (dǐ) | The fixed number $b$ in $b^x$ |
| exponent / index / power | 指数 / 幂 | The variable $x$ in $b^x$ — three English words, one concept |
| growth | 增长 | Curve rises; $b > 1$ |
| decay | 衰减 | Curve falls toward zero; $0 < b < 1$ |
| asymptote | 渐近线 | Line the curve approaches but never reaches |
| horizontal asymptote | 水平渐近线 | Here always $y = 0$ (the $x$-axis) |
| initial value | 初始值 | Value at $x = 0$; equals $a$ in $y = a \cdot b^x$ |
| $y$-intercept | $y$轴截距 | Same as initial value for this family |
| growth factor | 增长因子 | The base $b$ when $b > 1$ |
| decay factor | 衰减因子 | The base $b$ when $0 < b < 1$ |
| natural exponential | 自然指数函数 | $y = e^x$ — special base $e \approx 2.718$, see [[Euler's Number]] |

> [!warning] $y = 2^x$ is NOT $y = x^2$
> The single most common confusion. $y = x^2$ is a **parabola** (quadratic, polynomial) — variable is in the *base*. $y = 2^x$ is an **exponential** — variable is in the *exponent*. At $x = 10$: $10^2 = 100$, but $2^{10} = 1024$. Exponential wins every growth race eventually, and examiners will ask you to compare them.

![[exponential-vs-polynomial.svg]]

Left: $y = 2^x$ with its asymptote $y = 0$ — the curve approaches the $x$-axis as $x \to -\infty$ but never touches. Right: $y = 2^x$ vs $y = x^2$. They meet at $(2, 4)$ and again at $(4, 16)$. For $x < 2$ and between the crossings, $x^2$ is ahead; past $x = 4$, the exponential pulls away and never looks back.

> [!warning] "Asymptote" is a precise word
> An asymptote is a line the curve gets arbitrarily close to but never meets. For $y = b^x$ the $x$-axis ($y = 0$) is a horizontal asymptote: as $x \to -\infty$ the curve approaches zero from above but never equals zero. Don't write "the curve hits the asymptote" — it *doesn't*, that's the whole point.

> [!tip] Exam phrasing
> - "**Sketch** $y = 2^x$, showing the $y$-intercept and the asymptote." → Mark $(0, 1)$; draw $y = 0$ as a dashed line; curve above it, rising right.
> - "State the equation of the **horizontal asymptote**." → $y = 0$ (write the equation, not just the number).
> - "$y = ab^x$ passes through $(0, 5)$ and $(2, 45)$. **Find $a$ and $b$**." → $a$ is the $y$-intercept; plug in the second point to solve for $b$.

## Standard Shapes

| Equation | Shape | $y$-intercept | Asymptote | Notes |
|----------|-------|---------------|-----------|-------|
| $y = b^x$, $b > 1$ | **Growth** — rising curve | $(0, 1)$ | $y = 0$ | Steeper for larger $b$ |
| $y = b^x$, $0 < b < 1$ | **Decay** — falling curve | $(0, 1)$ | $y = 0$ | Mirror image of growth across $y$-axis |
| $y = b^{-x}$, $b > 1$ | Decay (same as $(1/b)^x$) | $(0, 1)$ | $y = 0$ | Reflection of $b^x$ across $y$-axis |
| $y = a \cdot b^x$ | Scaled exponential | $(0, a)$ | $y = 0$ | $a$ shifts the initial value |
| $y = e^x$ | Natural growth | $(0, 1)$ | $y = 0$ | Base $e \approx 2.718$; see [[Euler's Number]] |
| $y = e^{-x}$ | Natural decay | $(0, 1)$ | $y = 0$ | Base $1/e \approx 0.368$ |

> [!info] Why the asymptote is always $y = 0$
> $b^x$ is never negative and never zero for any real $x$ — positive bases raised to any power stay positive. So the graph never crosses or touches the $x$-axis. As $x \to -\infty$ (for growth) or $x \to +\infty$ (for decay), the output shrinks toward but never reaches zero.

## Exam Notes

### OxAQA 9260

**A12 Ext** — Recognise and sketch $y = k^x$ for $k > 0$ alongside linear, quadratic, cubic, and reciprocal shapes. Typical task: "Match each equation to its graph" or "Sketch $y = 3^x$ and $y = 3^{-x}$ on the same axes." Students who cannot verbalise "asymptote at $y = 0$" lose easy marks.

### Cambridge 0580 Extended

**E2.10** — Recognise, sketch, and interpret graphs of exponential functions, and draw/interpret graphs of exponential growth and decay problems (E1.17 context: depreciation, population). Usually 2–3 marks: shape, $y$-intercept, asymptote. Two fine-print facts from the syllabus itself: the examined family is $y = ar^x + b$ — **the $+b$ lifts the asymptote to $y = b$**, so read the equation before writing $y = 0$ — and **knowledge of $e$ is not required** at 0580; the natural exponential waits for 0606.

### Cambridge 0606

**6.1** — Properties and graphs of $y = e^x$ and $y = \ln x$, "including the asymptotic nature of the graphs" — and the syllabus asks you to **state the equations of any asymptotes**, on graphs limited to $y = ke^{nx} + a$ and $y = k\ln(ax+b)$ with integer constants. Same trap as 0580, one level up: the $+a$ makes the horizontal asymptote $y = a$. Also required: $e^x$ and $\ln x$ as inverses of each other (the reflection across $y = x$).

### Beyond IGCSE

Not examined as a recognition task above 0606 — A Level and beyond assume these shapes fluently and test them inside calculus, logarithms, and modelling ([[Exponential Growth and Decay]] carries that story).

## Connections

- **Prerequisite:** [[Laws of Indices]] — $b^{-x} = 1/b^x$ and $b^0 = 1$ power the shape facts.
- **Application of:** [[Exponential Growth and Decay]] — this vocab card is the graph-recognition tool; the deep card is the model behind it.
- **Special case:** [[Euler's Number]] — $y = e^x$ is the canonical natural exponential.
- **Leads to:** [[Graphs of Functions]] — transformations $y = af(b(x-c)) + d$ applied to $e^x$ and $b^x$.
- **Leads to:** [[Logarithms]] — the inverse $y = \log_b x$ reflects the exponential across $y = x$.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $y = b^x$ | `y = b^x` | General exponential |
| $y = e^x$ | `y = e^x` | Natural exponential |
| $y = a \cdot b^x$ | `a \cdot b^x` | Scaled form |
| $b > 1$ | `b > 1` | Growth condition |
| $0 < b < 1$ | `0 < b < 1` | Decay condition |
