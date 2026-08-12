---
chinese: 正比例和反比例 (zhèng bǐlì hé fǎn bǐlì)
prerequisites:
  - "[[Ratio (Vocab)]]"
  - "[[Laws of Indices]]"
  - "[[Changing the Subject (Vocab)]]"
  - "[[Percentages (Vocab)]]"
leads_to:
  - "[[Exponential Growth and Decay]]"
  - "[[Linearisation]]"
  - "[[Proportion (Vocab)]]"
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
  - syllabus/9260-A18
  - syllabus/9260-A18-Ext
  - syllabus/9260-N20
  - syllabus/0580-E2-8
  - type/vocabulary
  - notation/proportional-to
  - misconception/direct-vs-inverse
  - misconception/constant-k
---

# Direct and Inverse Proportion 正比例和反比例

## Definition

Two variables are in **proportion** when one is a fixed multiple of the other (or a fixed multiple of some power of the other). Exam language distinguishes two flavours: **direct** (one rises, the other rises in lockstep) and **inverse** (one rises, the other falls). Both are expressed with the same Greek-style notation: $\propto$, read "is proportional to."

### 中文锚点

正比例：$y = kx$，即 **$y$ 与 $x$ 成正比**。反比例：$y = \dfrac{k}{x}$，即 **$y$ 与 $x$ 成反比**。中国学生对这两个关系非常熟悉 — 难点是英文术语：$\propto$ 读作 "is proportional to"，$k$ 叫 **constant of proportionality (比例常数)**。

## Core Forms

| English statement | Symbolic | Equation | 中文 |
|-------------------|----------|----------|------|
| $y$ is directly proportional to $x$ | $y \propto x$ | $y = kx$ | 正比例 |
| $y$ is inversely proportional to $x$ | $y \propto \dfrac{1}{x}$ | $y = \dfrac{k}{x}$ | 反比例 |
| $y$ is proportional to $x^2$ | $y \propto x^2$ | $y = kx^2$ | $y$ 与 $x^2$ 成正比 |
| $y$ is proportional to $\sqrt{x}$ | $y \propto \sqrt{x}$ | $y = k\sqrt{x}$ | $y$ 与 $\sqrt{x}$ 成正比 |
| $y$ is inversely proportional to $x^2$ | $y \propto \dfrac{1}{x^2}$ | $y = \dfrac{k}{x^2}$ | $y$ 与 $x^2$ 成反比 |

The constant $k$ is the **constant of proportionality** (比例常数). It never changes within a single problem — it's the single number that converts the proportional statement into an actual equation.

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| proportional to | 成…比 / 与…成比例 | The phrase linking two quantities — always followed by "to" |
| directly proportional | 成正比 (zhèng bǐ) | Both rise together; $y = kx$ |
| inversely proportional | 成反比 (fǎn bǐ) | One rises, the other falls; $y = k/x$ |
| in direct proportion | 成正比例 | Same as "directly proportional" |
| in inverse proportion | 成反比例 | Same as "inversely proportional" |
| constant of proportionality | 比例常数 | The fixed $k$; sometimes called "the constant $k$" |
| varies as | 随…变化 | "$y$ **varies as** $x$" = "$y$ is directly proportional to $x$" (older wording, still used) |
| varies inversely as | 随…反向变化 | "$y$ varies inversely as $x$" = inverse proportion |
| varies directly as the square of | 与…的平方成正比 | $y \propto x^2$ |

> [!warning] "Inversely proportional" ≠ "negatively correlated"
> Inverse proportion is a precise relationship: $y = k/x$, so $xy = k$ stays constant. "Negative correlation" is a loose statistical idea ("when $x$ goes up, $y$ tends to go down"). An exam question saying "$y$ is inversely proportional to $x$" gives you the *exact equation* $y = k/x$ — not just a vague direction.

> [!warning] Find $k$ first, then answer the question
> Every proportion problem follows the same pattern:
> 1. Write the equation: $y = kx$, $y = k/x$, $y = kx^2$, etc.
> 2. Plug in the one pair of values given to solve for $k$.
> 3. Use the full equation with $k$ filled in to answer what's asked.
>
> Students who skip Step 2 and try to set up a ratio directly usually get the algebra wrong on inverse or squared forms.

> [!tip] Exam phrasing
> - "**$y$ is directly proportional to $x$. When $x = 4$, $y = 20$. Find $y$ when $x = 9$.**" → $y = kx$; $20 = 4k$, so $k = 5$; then $y = 5(9) = 45$.
> - "**$y$ is inversely proportional to the square of $x$.**" → $y = k/x^2$. Common A-level phrasing.
> - "**Express $y$ in terms of $x$.**" → Give the equation $y = kx^2$ (or whatever), with numerical $k$ substituted.
> - "**$P$ is proportional to $V^3$ and $P = 250$ when $V = 5$. Find $P$ when $V = 2$.**" → Same three-step pattern.

## Graph recognition

| Relationship | Equation | Graph shape |
|--------------|----------|-------------|
| $y \propto x$ | $y = kx$ | Straight line through the origin, gradient $k$ |
| $y \propto x^2$ | $y = kx^2$ | Parabola through the origin |
| $y \propto \dfrac{1}{x}$ | $y = \dfrac{k}{x}$ | Hyperbola with asymptotes at the axes |
| $y \propto \dfrac{1}{x^2}$ | $y = \dfrac{k}{x^2}$ | Steeper hyperbola in the first/second quadrant |

Direct proportion is the **simplest kind of linear function**: the graph of $y = kx$ is a straight line, and forcing it through the origin is what makes it *proportional* rather than just *linear*. A line like $y = 2x + 3$ is linear but not proportional — the $+3$ breaks the rule. In that sense, proportion is linear-ness plus the extra constraint "both zero at the same time."

![[proportion-graphs.svg]]

Top row: $y\propto x$ is a straight line through the origin; $y\propto 1/x$ is a hyperbola that hugs both axes. Bottom row: the linearisation trick for $y\propto\sqrt{x}$ — see the worked example below.

## Worked example — the linearisation trick

> **An object's period $T$ is claimed to be proportional to $\sqrt{L}$, where $L$ is its length.** Measurements taken: $(L, T) = (1, 3), (4, 6), (9, 9), (16, 12)$.
> **(a)** Plot $T$ against $L$. What shape do you see?
> **(b)** Plot $T$ against $\sqrt{L}$. What shape do you see? What does this tell you?
> **(c)** Hence state the value of $k$ in $T = k\sqrt{L}$.

**(a)** Plotting $T$ against $L$ gives a curve — it rises quickly at first, then flattens. It *might* be $\sqrt{L}$ shape, or it could be $\log L$, or $L^{0.4}$, or something else. The eye can't reliably tell curves apart.

**(b)** Plotting $T$ against $\sqrt{L}$ uses the new horizontal values $\sqrt{1}, \sqrt{4}, \sqrt{9}, \sqrt{16} = 1, 2, 3, 4$. The points become $(1, 3), (2, 6), (3, 9), (4, 12)$ — a **perfect straight line through the origin**. This is strong evidence that $T \propto \sqrt{L}$.

**(c)** Gradient of that straight line = $\dfrac{12 - 0}{4 - 0} = 3$. So $k = 3$ and $T = 3\sqrt{L}$.

> [!tip] Why this trick works — and when to use it
> If $y = k\sqrt{x}$, substitute $u = \sqrt{x}$ to get $y = ku$. That is a straight line in the $(u, y)$ plane with gradient $k$ and $y$-intercept $0$. Same idea works for any $y = kx^n$: plot $y$ against $x^n$ and you should get a straight line if the claimed power is correct. It's the simplest case of the wider A-Level technique of plotting against a transformed variable to straighten out curved data — at A-Level and beyond, this generalises to taking logs of both sides (see [[Laws of Logarithms]] family). Many physics experiments live or die by this step.

## Exam Notes

### OxAQA 9260

**N20** — Direct and inverse proportion, repeated proportional change. Questions range from contextual ("a car's stopping distance is proportional to the square of its speed") to purely algebraic. Repeated proportional change (compound-style multipliers) is also tested here — see [[Percentage Calculations (Vocab)|Percentage Calculations]] and [[Simple and Compound Interest (Vocab)]] for the iterative tools.

**A18 Ext** — Express direct and inverse variation algebraically; find unknown quantities. The algebraic framing of the same idea, now expected at GCSE-Extended / A-Level feeder level.

### Cambridge 0580 Extended

**E2.8** — Proportion (algebraic). Use $\propto$ notation and the equation $y = kx^n$ or $y = k/x^n$; find $k$ from one pair, then compute. 3–4 marks typical.

### Cambridge 0606

Inverse and direct proportion show up in applied differentiation and integration problems (rates, volumes). The vocabulary is identical; the context is denser.

## Connections

- **Prerequisite:** [[Ratio (Vocab)]] — "part-to-whole" reasoning that proportion generalises.
- **Prerequisite:** [[Laws of Indices]] — squared, cubed, and reciprocal powers appear in $y \propto x^n$.
- **Prerequisite:** [[Changing the Subject (Vocab)]] — rearranging $y = kx^n$ to solve for $x$ or $k$.
- **Leads to:** [[Exponential Growth and Decay]] — proportion says "rate $\propto$ quantity" when integrated gives the exponential.
- **Related:** [[Exponential Graphs (Vocab)]] — the $y = kx^n$ family sits next to the $y = a \cdot b^x$ family on the graph-shape chart.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\propto$ | `\propto` | "is proportional to" |
| $y = kx$ | `y = kx` | Direct proportion |
| $y = \dfrac{k}{x}$ | `y = \dfrac{k}{x}` | Inverse proportion |
| $y = kx^n$ | `y = kx^n` | General direct form |
| $k$ | `k` | Constant of proportionality |
