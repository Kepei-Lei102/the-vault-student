---
chinese: 线性图像 (xiànxìng túxiàng)
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Algebraic Expressions (Vocab)]]"
leads_to:
  - "[[Gradient (Vocab)]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Sketching Curves (Vocab)]]"
  - "[[Linear Equations (Vocab)]]"
  - "[[Graphical Inequalities (Vocab)]]"
  - "[[Travel Graphs (Vocab)]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A11
  - syllabus/0580-E3-2
  - syllabus/9709-1-3
  - type/vocabulary
  - misconception/plotting-vs-sketching
---

# Linear Graphs 线性图像

## Definition

A **linear graph** (线性图像) is the graph of a linear equation — an equation whose graph is a **straight line**. The most common form is $y = mx + c$, where $m$ and $c$ are constants. Every point $(x, y)$ on the line satisfies the equation; every point off the line does not.

### 中文锚点

线性图像 = 直线图像。方程 $y = mx + c$ 在笛卡尔坐标系中画出来就是一条直线。每一个点都满足这个方程。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| linear | 线性 (xiànxìng) | "Of a line"; the equation has only $x$ and $y$ to the first power, no $x^2$, no $xy$ |
| plot | 描点画图 | Make a table of values, mark the points, join them |
| sketch | 草图 / 勾画 | Show the key features without precise plotting |
| $x$-intercept | $x$ 截距 (jiéjù) | Where the line crosses the $x$-axis; $y = 0$ there |
| $y$-intercept | $y$ 截距 | Where the line crosses the $y$-axis; $x = 0$ there |
| intercept | 截距 | A point where a graph crosses an axis |
| table of values | 数值表 | Columns of $x$ and the resulting $y$ used to plot |
| straight line | 直线 (zhíxiàn) | The defining shape of a linear graph |

> [!tip] "Plot" vs "sketch" — the exam distinction
> **Plot** means: make a table of values, use graph paper, mark each point exactly, join them with a ruler. You need accuracy.
> **Sketch** means: show the key features — intercepts, general direction, any special points — without needing precise measurements. A sketch should still be *qualitatively correct* (correct sign of gradient, correct intercepts). 9260 exams use both words and they carry different mark schemes.

---

## Finding Intercepts

Intercepts are the easiest points to find on any linear graph, and they're often enough to sketch the line (two points determine a line).

**$y$-intercept:** Set $x = 0$ in the equation. In $y = mx + c$, this gives $y = c$. So the $y$-intercept is always $(0, c)$.

**$x$-intercept:** Set $y = 0$ and solve for $x$. In $y = mx + c$, this gives $0 = mx + c$, so $x = -\dfrac{c}{m}$.

**Example:** $y = 2x - 6$. The $y$-intercept is $(0, -6)$; the $x$-intercept is $(3, 0)$. Join these two points with a ruler — done.

---

## Plotting from a Table of Values

When asked to "plot" (not just sketch), build a table:

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|-----|------|------|-----|-----|-----|
| $y = 2x + 1$ | $-3$ | $-1$ | $1$ | $3$ | $5$ |

Plot each $(x, y)$ pair on graph paper, then join with a straight edge. If the points don't line up, check your arithmetic — **a linear equation must give collinear points.**

> [!warning] Use a ruler!
> Examiners mark down "wobbly" or freehand straight lines. A linear graph must be drawn with a ruler or straight edge. This is a common, avoidable mark loss.

---

## Exam Notes

### OxAQA 9260 / Cambridge 0580

**Syllabus ref:** A11 (9260), E3.2 (0580). "Draw straight-line graphs from given equations; interpret the meaning of intercepts." Usually paired with [[Gradient (Vocab)]] and [[Equation of a Straight Line (Vocab)]] for full coordinate-geometry questions.

---

## Beyond the Syllabus

At A-Level and beyond, linear graphs become the foundation of:
- **Linear algebra** — systems of linear equations become matrix equations $A\mathbf{x} = \mathbf{b}$
- **Linear regression** in statistics — fitting a best-fit line to noisy data (see [[Scatter Diagrams]])
- **Tangent lines** in calculus — locally, every smooth curve looks linear (see [[Tangents and Normals]])

## Connections

- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — the plane we draw lines on
- **Prerequisite:** [[Algebraic Expressions (Vocab)]] — the equation $y = mx + c$
- **Leads to:** [[Gradient (Vocab)]] — the $m$ in $y = mx + c$ measures steepness
- **Leads to:** [[Equation of a Straight Line (Vocab)]] — full treatment of line equations
- **Leads to:** [[Sketching Curves (Vocab)\|Sketching Curves]] — curves extend the same plot-and-join technique
- **Leads to:** [[Linear Equations (Vocab)|Linear Equations]] — solving $mx + c = 0$ finds the $x$-intercept
