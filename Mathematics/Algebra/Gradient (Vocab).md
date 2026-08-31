---
chinese: 斜率 (xiélǜ)
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Linear Graphs (Vocab)]]"
leads_to:
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Tangents and Normals]]"
  - "[[Differentiation]]"
  - "[[Parallel Lines (Vocab)]]"
  - "[[Perpendicular Lines (Vocab)]]"
  - "[[Travel Graphs (Vocab)]]"
tags:
  - subject/mathematics
  - domain/algebra
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-A11
  - syllabus/0580-E3-3
  - syllabus/9709-1-3
  - type/vocabulary
  - notation/delta
  - misconception/rise-over-run-order
---

# Gradient 斜率

## Definition

The **gradient** (斜率) of a straight line measures its **steepness** — how much $y$ changes for each unit that $x$ increases. For any two points $(x_1, y_1)$ and $(x_2, y_2)$ on the line:

$$\text{gradient} = \frac{\text{rise}}{\text{run}} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

The key property: for a **straight line**, this ratio is the **same no matter which two points you pick**. That constancy is exactly what "straight" means.

### 中文锚点

斜率 = 直线的"陡度"。从一个点移动到另一个点时，$y$ 的变化 ($\Delta y$) 除以 $x$ 的变化 ($\Delta x$)。直线的斜率处处相等 — 这就是"直"的含义。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| gradient | 斜率 (xiélǜ) | British term, standard in 0580/9260 |
| slope | 斜率 | American term, same meaning |
| rise | 纵向变化 | Vertical change, $\Delta y = y_2 - y_1$ |
| run | 横向变化 | Horizontal change, $\Delta x = x_2 - x_1$ |
| rate of change | 变化率 | What gradient means in applied contexts |
| steepness | 陡度 | Informal synonym |
| $\Delta$ (delta) | 变化量 | Greek capital D, means "change in"; $\Delta x$ = "change in $x$" |

> [!tip] Why $\Delta$?
> $\Delta$ is the Greek capital letter **delta**, the letter D. Mathematicians use it as a shorthand for **"difference"** or **"change in"**. So $\Delta y$ reads as "delta $y$" and means "the change in $y$". You'll see this notation everywhere in physics and calculus.

---

## Sign and Direction

The sign of the gradient tells you which way the line goes as you read left to right:

| Gradient | Line direction | Shape | Example |
|----------|----------------|-------|---------|
| $m > 0$ | **Uphill** (positive slope) | ↗ | $y = 2x + 1$ |
| $m < 0$ | **Downhill** (negative slope) | ↘ | $y = -3x + 4$ |
| $m = 0$ | **Horizontal** | → | $y = 5$ |
| undefined | **Vertical** | ↑ | $x = 2$ |

> [!warning] Vertical lines have no gradient — not zero, undefined
> For a vertical line, $x_2 = x_1$, so $\Delta x = 0$ and you'd be dividing by zero. Vertical lines **have no gradient** (it is undefined, not zero). A horizontal line has gradient **zero**. Don't confuse the two.

---

## Worked Example

Find the gradient of the line through $A(2, -1)$ and $B(5, 8)$.

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{8 - (-1)}{5 - 2} = \frac{9}{3} = 3$$

The line rises 3 units for every 1 unit right — a positive gradient of 3.

> [!warning] Order consistency
> You can choose which point is $(x_1, y_1)$ and which is $(x_2, y_2)$ — but whatever order you pick, **stick with it for both numerator and denominator**. Doing $\dfrac{y_2 - y_1}{x_1 - x_2}$ flips the sign and gives the wrong answer. A common slip.

---

## Why It's Constant on a Straight Line

Take any two pairs of points on a line. The triangles formed by their rises and runs are **similar** — same angle, just different sizes. Similar triangles have proportional sides, so $\dfrac{\text{rise}}{\text{run}}$ comes out the same. **This is what "straight" means** in coordinate geometry: the ratio of change is constant.

The moment the gradient starts varying from point to point, you no longer have a line — you have a **curve**. Measuring the gradient of a curve at a single point is the foundational idea of [[Differentiation]] (the derivative is "instantaneous gradient").

---

## Exam Notes

### Cambridge 0580

**Syllabus ref: C3.3 / E3.3** ("Gradient of linear graphs"), and the tier split is the audit-worthy fact: **Core finds the gradient "from a grid only"** — count squares, rise over run — while **Extended adds calculating it from the coordinates of two points** with no grid drawn. The rate-of-change *interpretation* lives with the graphs-in-practical-situations rows (travel graphs and their gradients), not in E3.3's own wording.

**Typical phrasing:** "Find the gradient of the line joining $A$ and $B$." "A line has gradient $-2$ and passes through $(1, 5)$…". Usually paired with [[Equation of a Straight Line (Vocab)]].

### OxAQA 9260

**Syllabus ref: A11.** Same two skills, one tier: gradient from a graph and from two points.

### Cambridge 9709

**§1.3 (coordinate geometry)** assumes the two-point gradient fluently — it appears inside every line-equation, parallel/perpendicular ($m_1 m_2 = -1$) and tangent/normal question rather than as a question of its own, and from [[Differentiation]] onward "gradient" means the derivative evaluated at a point.

---

## Beyond the Syllabus

**Gradient becomes derivative.** In calculus, you zoom in on a curve until a tiny piece of it looks straight, then measure the gradient of that piece. This limit — $\dfrac{dy}{dx} = \lim_{\Delta x \to 0} \dfrac{\Delta y}{\Delta x}$ — is the **derivative**, the central object of differential calculus (see [[Differentiation]], [[Tangents and Normals]]).

**Gradient generalises to higher dimensions.** For a surface $z = f(x, y)$, the "gradient" becomes a **vector** $\nabla f = \left(\dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}\right)$ that points in the direction of steepest ascent. This is the foundation of **gradient descent** — the optimisation algorithm that trains every neural network in modern machine learning.

**Rate of change in physics.** Position vs time graph → gradient is **velocity**. Velocity vs time graph → gradient is **acceleration**. Any graph's gradient has a physical interpretation as a rate.

## Connections

- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — two points in the plane
- **Prerequisite:** [[Linear Graphs (Vocab)]] — straight lines are where gradient lives
- **Leads to:** [[Equation of a Straight Line (Vocab)]] — gradient is the $m$ in $y = mx + c$
- **Leads to:** [[Tangents and Normals]] — a tangent's gradient = the curve's gradient at that point
- **Leads to:** [[Differentiation]] — the derivative generalises gradient to curves
