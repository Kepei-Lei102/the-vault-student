---
chinese: 草图绘制 (cǎotú huìzhì)
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Linear Graphs (Vocab)]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Completing the Square]]"
  - "[[Quadratic Equations]]"
  - "[[Stationary Points]]"
leads_to:
  - "[[Graphs of Functions]]"
  - "[[Exponential Graphs (Vocab)]]"
  - "[[Area Under a Graph (Vocab)]]"
  - "[[Cubic Graphs]]"
  - "[[Quadratic Inequalities]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A16
  - syllabus/0580-E2-11
  - type/vocabulary
---

# Sketching Curves 草图绘制

## Definition

A **sketch** is a freehand drawing that shows the *key features* of a curve — general shape, intercepts, turning points, asymptotes — without being to scale. Contrast with **plot**, which demands accurate, point-by-point drawing on graph paper.

On an exam, "sketch" almost always means: draw the correct shape, label the intercepts as coordinates, mark any turning points as coordinates, and draw in any asymptotes. Graph paper is not required.

### 中文锚点

**草图 (cǎotú)** = sketch, rough drawing. **精确绘制 (jīngquè huìzhì)** = accurate plot. On a Chinese-language exam you might see 作图 (draw) or 画出 (draw out); in English "sketch" and "plot" are *different* instructions — don't treat them as synonyms.

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| sketch | 草图, 画略图 | Rough shape + key features; no graph paper |
| plot | 精确绘制, 描点画图 | Accurate, to scale, on graph paper |
| root (of $f(x)$) | 根, 零点 | Value of $x$ where $f(x) = 0$ |
| zero | 零点 | Synonym of root |
| x-intercept | $x$轴截距 | Point where curve crosses $x$-axis — same as root |
| y-intercept | $y$轴截距 | Point where curve crosses $y$-axis; equals $f(0)$ |
| turning point | 转折点, 极值点 | Where the curve changes direction (local max or min) |
| stationary point | 驻点 | Where $\dfrac{dy}{dx} = 0$ (max, min, or inflection) |
| point of inflection | 拐点 | Where curvature changes sign |
| maximum / minimum | 极大值 / 极小值 | Top of hill / bottom of valley |
| vertex (of parabola) | 顶点 | The single turning point of a quadratic |
| axis of symmetry | 对称轴 | Vertical line the curve reflects across |
| asymptote | 渐近线 | Line the curve approaches but never reaches |
| parabola | 抛物线 | Shape of $y = ax^2 + bx + c$ |
| cubic curve | 三次曲线 | Shape of $y = ax^3 + \ldots$ |
| hyperbola (reciprocal) | 双曲线 (反比例曲线) | Shape of $y = \dfrac{k}{x}$ |
| exponential curve | 指数曲线 | Shape of $y = k^x$ |

> [!warning] "Sketch" ≠ "Plot"
> Examiners choose the word deliberately. **Sketch** = show shape + labelled features, freehand is fine. **Plot** = use graph paper, mark specific coordinates accurately, join smoothly. If you plot when sketch was asked, you waste time; if you sketch when plot was asked, you lose marks for inaccuracy.

> [!tip] Standard command phrasings
> - "**State** the coordinates of the turning point." → Give $(x, y)$.
> - "Write down the equation of the **axis of symmetry**." → Give $x = h$, not just $h$.
> - "**Find the exact roots**." → "Exact" forbids decimals — use surds or fractions.
> - "**Identify the asymptotes**." → State the line equations (e.g., $y = 0$ and $x = 0$ for $y = k/x$).
> - "Sketch, **showing clearly the coordinates of** any intercepts with the axes." → Label every axis crossing as $(x, y)$ on your sketch.

## Standard Curve Shapes

| Equation | Shape | Key features to label |
|----------|-------|-----------------------|
| $y = mx + c$ | straight line | gradient $m$, $y$-intercept $(0, c)$ |
| $y = ax^2 + bx + c, \ a > 0$ | parabola opening up | vertex (minimum), axis of symmetry $x = -\dfrac{b}{2a}$ |
| $y = ax^2 + bx + c, \ a < 0$ | parabola opening down | vertex (maximum), axis of symmetry |
| $y = a(x-h)^2 + k$ | parabola in vertex form | vertex $(h, k)$ directly readable |
| $y = ax^3$, $a > 0$ | cubic rising left→right | passes through origin, shape like a stretched $S$ |
| $y = \dfrac{k}{x}, \ k > 0$ | hyperbola (Q1, Q3) | asymptotes $x = 0$ and $y = 0$ |
| $y = k^x, \ k > 1$ | exponential growth | passes $(0, 1)$; asymptote $y = 0$ |
| $y = k^{-x}, \ k > 1$ | exponential decay | passes $(0, 1)$; asymptote $y = 0$ |

> [!info] Turning point vs stationary point
> **Turning point** — the curve actually *changes direction* (goes up then down, or vice versa). Always a local max or min.
> **Stationary point** — just means $\dfrac{dy}{dx} = 0$. Every turning point is stationary, but a stationary point can also be a **point of inflection** where the curve momentarily flattens without turning (e.g., $y = x^3$ at the origin). Exam vocabulary is strict: don't call an inflection point a "turning point".

## Exam Notes

### OxAQA 9260

**A16** — Sketch quadratic curves; identify roots, $y$-intercept, and turning point from the equation. Expect a prompt like "Sketch $y = x^2 - 4x + 3$, showing the coordinates of the turning point and any points where the curve meets the axes."

### Cambridge 0580 Extended

**E2.11** — Sketch familiar functions: linear, quadratic, cubic, reciprocal $(k/x)$, exponential $(a^x)$. Usually a 2–3 mark question: one mark for correct shape, one for intercepts, one for asymptotes (if any).

## Connections

- **Used by:** [[Quadratic Equations]] — roots from the formula go straight onto the sketch as $x$-intercepts.
- **Used by:** [[Completing the Square]] — vertex form $(x-h)^2 + k$ hands you the turning point $(h, k)$ for free.
- **Used by:** [[Stationary Points]] — for cubics and beyond, find turning points via $\dfrac{dy}{dx} = 0$, then plug back into the sketch.
- **Leads to:** [[Graphs of Functions]] — the deep card on graph transformations $y = af(b(x - c)) + d$.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $f(x)$ | `f(x)` | Function notation |
| $y = ax^2 + bx + c$ | `ax^2+bx+c` | Standard quadratic |
| $y = a(x-h)^2 + k$ | `a(x-h)^2+k` | Vertex form |
| $\dfrac{dy}{dx}$ | `\dfrac{dy}{dx}` | Gradient function |
| $(h, k)$ | `(h, k)` | Coordinate pair for vertex |
