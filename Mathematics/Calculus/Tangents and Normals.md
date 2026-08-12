---
chinese: 切线与法线 (qiēxiàn yǔ fǎxiàn)
prerequisites:
  - "[[Differentiation]]"
  - "[[Power Rule]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Perpendicular Lines (Vocab)]]"
  - "[[Gradient (Vocab)]]"
  - "[[Implicit Differentiation]]"
  - "[[Parametric Differentiation]]"
  - "[[Quotient Rule]]"
leads_to:
  - "[[Connected Rates of Change]]"
  - "[[Optimisation]]"
  - "[[Integration]]"
  - "[[Vectors]]"
  - "[[3D Vectors]]"
  - "[[Numerical Methods]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0606
  - syllabus/9260-A14
  - syllabus/0606-14-5
  - syllabus/9709-1-7
  - type/application
  - type/vocabulary
  - notation/derivative
  - misconception/normal-is-not-the-tangent
---

# Tangents and Normals 切线与法线

## Definition

### Formal

At a point $P = (a, f(a))$ on the curve $y = f(x)$:

The **tangent** at $P$ is the straight line through $P$ with gradient equal to $f'(a)$:

$$y - f(a) = f'(a)(x - a)$$

The **normal** at $P$ is the straight line through $P$ **perpendicular** to the tangent:

$$y - f(a) = -\dfrac{1}{f'(a)}(x - a) \qquad \text{(provided } f'(a) \neq 0\text{)}$$

The tangent and normal are always perpendicular to each other at $P$. They form a local coordinate frame for the curve at that point.

### Intuitive — Riding the Curve

Imagine you're cycling along a curve. At any point:

- The **tangent** is the direction you're currently heading — if you let go of the handlebars, you'd fly off in a straight line along the tangent.
- The **normal** is the direction straight to your side — perpendicular to your motion. If there's a centripetal force pulling you around the curve (like gravity on a roller coaster), it acts along the normal.

The tangent tells you **where you're going**. The normal tells you **where the curve is bending you toward**.

![[tangent-normal-diagram.svg|700]]

### 中文锚点 (Chinese Anchor)

切线与法线：**切 = 刚好碰到，法 = 垂直**。

| 中文 | English | Key idea |
|------|---------|----------|
| 切线 (qiēxiàn) | Tangent line | 切 = to cut/touch; the line that just touches the curve |
| 法线 (fǎxiàn) | Normal line | 法 = method/rule/perpendicular; the line at 90° to the tangent |
| 斜率 (xiélǜ) | Gradient / slope | The steepness of the line |
| 垂直 (chuízhí) | Perpendicular | Two lines meeting at 90° |
| 切点 (qiēdiǎn) | Point of tangency | The point where the tangent touches the curve |

> [!tip] Why 法 means "perpendicular"
> 法 (fǎ) primarily means "law" or "method," but in mathematical Chinese it also means "normal/perpendicular" — as in 法线 (normal line) and 法向量 (normal vector). This comes from the idea that the "standard" or "canonical" direction at a point on a surface is the perpendicular one. Same root as French *normale* → English *normal*, which literally means "at right angles."

## Notation

| Symbol | Meaning |
|--------|---------|
| $f'(a)$ or $\left.\dfrac{dy}{dx}\right\rvert_{x=a}$ | Gradient of the curve (= gradient of the tangent) at $x = a$ |
| $m_T$ | Gradient of the tangent |
| $m_N$ | Gradient of the normal |
| $m_T \times m_N = -1$ | Perpendicular gradient relationship |
| $-\dfrac{1}{m_T}$ | The negative reciprocal — always gives the perpendicular gradient |

> [!important] The perpendicular gradient rule
> If two lines are perpendicular, the product of their gradients is $-1$:
>
> $$m_1 \times m_2 = -1 \qquad \Leftrightarrow \qquad m_2 = -\dfrac{1}{m_1}$$
>
> **Why?** Take a line with gradient $m$. Rotating it 90° anticlockwise maps the direction vector $\begin{pmatrix} 1 \\ m \end{pmatrix}$ to $\begin{pmatrix} -m \\ 1 \end{pmatrix}$. The new gradient is $\dfrac{1}{-m} = -\dfrac{1}{m}$. Multiply: $m \times \left(-\dfrac{1}{m}\right) = -1$. ∎
>
> See [[Perpendicular Lines (Vocab)|Perpendicular Lines]] for the full treatment.

## Key Facts

### 1. The Three-Step Method for Tangents

At point $(a, f(a))$ on $y = f(x)$:

1. **Differentiate** to find $f'(x)$
2. **Substitute** $x = a$ to find the gradient: $m_T = f'(a)$
3. **Use** $y - y_1 = m(x - x_1)$ with the point and gradient

This is already in [[Differentiation]] (9260 A14). The tangent card adds the normal.

### 2. The Normal — One Extra Step

After finding $m_T = f'(a)$:

$$m_N = -\dfrac{1}{f'(a)}$$

Then use $y - f(a) = m_N(x - a)$.

> [!warning] Special cases
> - If $f'(a) = 0$ (horizontal tangent), the normal is **vertical**: $x = a$.
> - If the curve has a vertical tangent (undefined $f'(a)$), the normal is **horizontal**: $y = f(a)$.
>
> Don't try to use $-\dfrac{1}{0}$ — recognise the geometry instead.

### 3. Where the Tangent/Normal Meets the Curve Again

A common exam question: "Find where the tangent (or normal) at $P$ meets the curve again."

**Method:** Set the equation of the tangent/normal equal to $f(x)$ and solve. You already know one root ($x = a$, the point of tangency), so factor it out.

**Example:** If $y = x^2$ and the tangent at $(1, 1)$ is $y = 2x - 1$:

Set $x^2 = 2x - 1$ → $x^2 - 2x + 1 = 0$ → $(x-1)^2 = 0$

Only $x = 1$ — the tangent touches but doesn't cross here (it's a double root). This is *why* it's a tangent: the line meets the curve with multiplicity 2 at the point of tangency.

### 4. Finding a Point Given a Gradient

"Find the point(s) on $y = f(x)$ where the gradient is $k$."

**Method:** Solve $f'(x) = k$ for $x$, then find the corresponding $y$-value(s).

This can be combined with "find the equation of the tangent/normal at that point."

### 5. The Tangent as a Linear Approximation

Near $x = a$, the tangent gives a good approximation to the curve:

$$f(x) \approx f(a) + f'(a)(x - a) \qquad \text{for } x \text{ close to } a$$

This is the **linear approximation** (or **linearisation**) — the foundation of [[Connected Rates of Change]] and [[Error Analysis|error propagation]]. It's why the tangent matters beyond just exam questions: it's the simplest useful model of a curve near a point.

## Common Misconceptions (Teaching Notes)

### 1. "The normal has the same gradient as the tangent"

**Wrong:** Students compute $f'(a)$ and use it for both lines.

**Right:** The normal gradient is $-\dfrac{1}{f'(a)}$. It must be the negative reciprocal.

**Fix:** Draw the tangent and normal every time. If both lines look like they go in the same direction, something is wrong — they must form a cross (+) at the point.

### 2. "The normal gradient is $\dfrac{1}{f'(a)}$" (forgetting the negative)

**Wrong:** $m_N = \dfrac{1}{f'(a)}$

**Right:** $m_N = -\dfrac{1}{f'(a)}$

**Why:** Without the negative sign, the lines aren't perpendicular. Two perpendicular lines have gradients of opposite sign (one goes "uphill," the other "downhill"). The only exception is horizontal/vertical.

### 3. "A tangent only touches the curve at one point"

**Wrong for curves in general.** This is true for circles (where a tangent touches at exactly one point), but a tangent to a cubic or higher-degree curve can cross the curve elsewhere.

**What makes it a tangent:** At the point of tangency, the line and the curve share the same gradient. Locally, they touch. What happens far away doesn't affect the tangent property.

### 4. Confusing "tangent to the curve" with "tangent ratio (trigonometry)"

Two completely different meanings of the word "tangent":

| Context | Meaning | Symbol |
|---------|---------|--------|
| Calculus | Line that just touches a curve | Tangent line |
| Trigonometry | $\tan \theta = \dfrac{\text{opposite}}{\text{adjacent}}$ | $\tan$ |

They share the same Latin root (*tangere* = to touch), but in different senses. The trig tangent is historically related to the length of a line segment tangent to a unit circle — but that etymology doesn't help at IGCSE.

## Worked Examples

### Example 1 — Tangent and Normal (0606 14.5)

> Find the equations of the tangent and the normal to $y = x^3 - 3x + 2$ at the point where $x = 2$.

**Solution:**

**Step 1: Find the point.**
$y = 8 - 6 + 2 = 4$. Point is $(2, 4)$.

**Step 2: Differentiate.**
$\dfrac{dy}{dx} = 3x^2 - 3$

**Step 3: Find gradient at $x = 2$.**
$m_T = 3(4) - 3 = 9$

**Step 4: Tangent equation.**
$y - 4 = 9(x - 2)$ → $\boxed{y = 9x - 14}$

**Step 5: Normal equation.**
$m_N = -\dfrac{1}{9}$

$y - 4 = -\dfrac{1}{9}(x - 2)$ → $9y - 36 = -(x - 2)$ → $\boxed{9y + x = 38}$

**Check:** At $x = 2$: tangent gives $y = 18 - 14 = 4$ ✓. Normal gives $9(4) + 2 = 38$ ✓.

---

### Example 2 — Where the Normal Meets the Curve Again (0606 14.5)

> The normal to $y = x^2 - 4x + 7$ at the point $(3, 4)$ meets the curve again at $Q$. Find the coordinates of $Q$.

**Solution:**

$\dfrac{dy}{dx} = 2x - 4$. At $x = 3$: $m_T = 2$.

$m_N = -\dfrac{1}{2}$

Normal: $y - 4 = -\dfrac{1}{2}(x - 3)$ → $y = -\dfrac{1}{2}x + \dfrac{11}{2}$

Set equal to the curve: $x^2 - 4x + 7 = -\dfrac{1}{2}x + \dfrac{11}{2}$

$x^2 - 4x + 7 + \dfrac{1}{2}x - \dfrac{11}{2} = 0$

$x^2 - \dfrac{7}{2}x + \dfrac{3}{2} = 0$ → $2x^2 - 7x + 3 = 0$

$(2x - 1)(x - 3) = 0$ → $x = \dfrac{1}{2}$ or $x = 3$

We know $x = 3$ is the original point. So $Q$ has $x = \dfrac{1}{2}$.

$y = \left(\dfrac{1}{2}\right)^2 - 4\left(\dfrac{1}{2}\right) + 7 = \dfrac{1}{4} - 2 + 7 = \dfrac{21}{4}$

$$\boxed{Q = \left(\dfrac{1}{2},\ \dfrac{21}{4}\right)}$$

---

### Example 3 — Finding a Point Given a Gradient (0606 14.5)

> The curve $y = 2x^3 - 9x^2 + 12x$ has tangent gradient $0$ at two points. Find the equations of the normals at these points.

**Solution:**

$\dfrac{dy}{dx} = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x-1)(x-2)$

$f'(x) = 0$ when $x = 1$ or $x = 2$.

At $x = 1$: $y = 2 - 9 + 12 = 5$. Tangent is horizontal ($m_T = 0$), so the normal is **vertical**: $\boxed{x = 1}$.

At $x = 2$: $y = 16 - 36 + 24 = 4$. Tangent is horizontal ($m_T = 0$), so the normal is **vertical**: $\boxed{x = 2}$.

These are the [[Stationary Points]] — the normals there are always vertical lines.

---

### Example 4 — Tangent as Approximation (Beyond syllabus preview)

> Use the tangent to $y = \sqrt{x}$ at $x = 100$ to estimate $\sqrt{102}$.

**Solution:**

$f(x) = x^{1/2}$, so $f'(x) = \dfrac{1}{2}x^{-1/2} = \dfrac{1}{2\sqrt{x}}$

At $x = 100$: $f(100) = 10$, $f'(100) = \dfrac{1}{20}$

Linear approximation: $f(102) \approx f(100) + f'(100) \times (102 - 100) = 10 + \dfrac{1}{20} \times 2 = 10.1$

Actual value: $\sqrt{102} = 10.0995...$ — the tangent approximation is off by only $0.0005$.

**Why this works:** Near $x = 100$, the curve $y = \sqrt{x}$ is almost indistinguishable from its tangent. The further you go from the point, the worse the approximation. This is the core idea behind [[Connected Rates of Change]] and differential equations.

## Exam Notes

### OxAQA 9260 (Extension)

**Syllabus ref:** A14 — "gradient = gradient of tangent; equation of tangent at a point"

- Tangent equations are explicitly tested. Normal equations are **not** in the 9260 spec — but the perpendicular gradient rule appears in the geometry section (A11 Ext: perpendicular lines), so normals can appear in a geometry context.
- Polynomials only (no trig, no $e^x$).
- The method is already in [[Differentiation]]; this card adds the normal and deeper worked examples.

### Cambridge 0606

**Syllabus ref:** 14.5 — "find gradients, tangents and normals"

- Both tangent AND normal equations are required.
- Can involve any function in the 0606 differentiation scope: polynomials, trig, $e^x$, $\ln x$, products, quotients, composites.
- "Find where the normal meets the curve again" is a classic 0606 question type.
- Often combined with 14.6 (stationary points): "find the stationary point, then find the normal there."

### AP / IB / A-Level

- Tangent and normal equations are prerequisite skills for: related rates, optimisation, curve sketching.
- The linear approximation $f(x) \approx f(a) + f'(a)(x - a)$ appears formally in AP Calculus as "linearisation."
- **IB Mathematics AA HL:** tangent lines used in Newton's method for finding roots (iterative approximation).
- **A-Level Further Mathematics:** tangent and normal concepts extend to parametric curves and implicit differentiation.

## Connections

**Prerequisites:**
- [[Differentiation]] — $f'(a)$ gives the tangent gradient (the whole reason tangents and normals exist)
- [[Power Rule]] — the workhorse for computing $f'(x)$ for polynomials
- [[Equation of a Straight Line (Vocab)|Equation of a Straight Line]] — $y - y_1 = m(x - x_1)$ for writing the tangent/normal equation
- [[Perpendicular Lines (Vocab)|Perpendicular Lines]] — $m_1 m_2 = -1$ for the normal gradient

**Leads to:**
- [[Connected Rates of Change]] — the tangent as a linear approximation leads to $\delta y \approx \dfrac{dy}{dx} \cdot \delta x$
- [[Optimisation]] — at stationary points, the tangent is horizontal → used to find max/min
- [[Integration]] — the reverse: given the gradient function, recover the curve
- [[Vectors]] — the tangent direction at a point on a curve IS a direction vector; the normal is perpendicular to it
- [[3D Vectors]] — in 3D, tangent and normal vectors define the **osculating plane** of a space curve; two lines in 3D that are not parallel might still never meet (skew lines), and the shortest distance between them involves normals

**Related cards:**
- [[Stationary Points]] — where the tangent is horizontal ($f'(x) = 0$), the normal is vertical
- [[Error Analysis]] — the tangent gives the linear approximation, which is the basis of error propagation ($\Delta f \approx f'(x) \cdot \Delta x$)
- [[Circle Tangent Problems]] — tangent to a circle (no calculus needed — uses the radius-tangent perpendicularity theorem, 0606 8.3)

## Beyond Syllabus

### AP / IB / A-Level depth

**Normal lines and the radius of curvature**

At a point on a curve, the normal points toward (or away from) the **centre of curvature** — the centre of the circle that best fits the curve locally. The radius of this circle is:

$$R = \dfrac{\left(1 + (f'(x))^2\right)^{3/2}}{\lvert f''(x) \rvert}$$

This is the **radius of curvature**. A small $R$ means tight bending (like a sharp turn); a large $R$ means gentle bending (like a gentle hill). At a point of inflection, $f''(x) = 0$ and $R \to \infty$ — the curve straightens momentarily.

The normal line always passes through the centre of curvature. This is why the normal is geometrically fundamental — it points in the direction the curve is bending.

**Tangent and normal vectors — the bridge to [[Vectors]]**

For a curve $y = f(x)$, the tangent direction at $(a, f(a))$ is the vector:

$$\mathbf{t} = \begin{pmatrix} 1 \\ f'(a) \end{pmatrix}$$

and the normal direction is:

$$\mathbf{n} = \begin{pmatrix} -f'(a) \\ 1 \end{pmatrix}$$

(Check: $\mathbf{t} \cdot \mathbf{n} = -f'(a) + f'(a) = 0$ ✓ — they're perpendicular.)

In 3D, curves have a **tangent vector**, a **normal vector**, and a **binormal vector** (perpendicular to both). These three vectors form the **Frenet–Serret frame** — a moving coordinate system that rides along the curve. This is how roller coasters, flight paths, and robot arms are analysed.

> [!info] Forward link — When 3D vectors cross
> In 2D, two lines either meet, are parallel, or are the same line. In 3D, there's a fourth possibility: **skew lines** — lines that aren't parallel but never meet (they pass each other at different "heights").
>
> The shortest distance between two skew lines involves the cross product of their direction vectors — which gives a vector perpendicular to both lines. This is essentially the 3D generalisation of the normal concept. See [[3D Vectors]] and [[Vector Geometry]] when those cards are built.

### Historical note — Why "normal" means "perpendicular"

The Latin *normalis* means "made according to a carpenter's square" — i.e., at right angles. A carpenter's square (a T-shaped tool) creates 90° angles. So the "normal" to a curve is the "square" direction — the one that's at right angles to the tangent.

This usage predates calculus: Apollonius of Perga (c. 200 BC) studied normals to conic sections. Newton and Leibniz inherited the terminology when they generalised it to all curves.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $f'(a)$ | `f'(a)` | Gradient at $x = a$ |
| $\left.\dfrac{dy}{dx}\right\rvert_{x=a}$ | `\left.\dfrac{dy}{dx}\right\rvert_{x=a}` | Leibniz notation evaluated at a point |
| $-\dfrac{1}{f'(a)}$ | `-\dfrac{1}{f'(a)}` | Normal gradient |
| $m_1 m_2 = -1$ | `m_1 m_2 = -1` | Perpendicular condition |
| $\begin{pmatrix} 1 \\ f'(a) \end{pmatrix}$ | `\begin{pmatrix} 1 \\ f'(a) \end{pmatrix}` | Tangent direction vector |
| $\mathbf{t}$, $\mathbf{n}$ | `\mathbf{t}`, `\mathbf{n}` | Tangent and normal unit vectors |
