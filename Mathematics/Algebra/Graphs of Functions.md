---
chinese: 函数图像 (hánshù túxiàng)
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Function]]"
  - "[[Sketching Curves (Vocab)]]"
  - "[[Completing the Square]]"
  - "[[Quadratic Equations]]"
  - "[[Composite Function]]"
  - "[[Exponential Graphs (Vocab)]]"
  - "[[Remainder and Factor Theorems]]"
  - "[[Transformations (Vocab)]]"
leads_to:
  - "[[Modulus Function]]"
  - "[[Cubic Graphs]]"
  - "[[Trigonometric Graphs]]"
  - "[[Linearisation]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - syllabus/9260-A12
  - syllabus/0580-E2-10
  - syllabus/0606-4-4
  - syllabus/9709-1-2
  - type/definition
  - type/visual-tool
  - notation/f-of-x
  - notation/asymptote
  - misconception/shift-direction
  - misconception/stretch-vs-translate
  - misconception/inside-vs-outside
---

# Graphs of Functions 函数图像

## Definition

The **graph of a function** $f$ is the set of all points $(x, f(x))$ plotted on the Cartesian plane. Every input $x$ in the domain gives exactly one output $y = f(x)$, so the graph passes the **vertical line test**: no vertical line crosses the curve more than once.

Two tasks show up again and again on exams:

1. **Recognise the shape** from the equation (is this a parabola, a hyperbola, an exponential?).
2. **Transform** a known parent graph — shift, stretch, reflect — to produce a new one.

This card catalogues the **parent graphs** you must recognise on sight, then builds the transformation framework $y = af(b(x - c)) + d$ that turns any one parent into a family of related curves.

### 中文锚点

**函数图像 (hánshù túxiàng)** = function graph. **母函数 (mǔ hánshù)** = parent function (the bare, untransformed version). **图像变换 (túxiàng biànhuàn)** = graph transformation. Key operations: **平移 (píngyí)** translation, **伸缩 (shēnsuō)** stretch, **反射 (fǎnshè)** reflection. Chinese textbooks often present transformations in the $y - k = f(x - h)$ "shifted-equation" form; English exams almost always write them as $y = f(x - h) + k$. The maths is identical.

---

## The Parent Graph Catalogue

Six shapes cover almost every IGCSE and A-Level graph question. Memorise their shape, their intercepts, their asymptotes (if any), and *why* they look the way they do.

![[graphs-of-functions-parents.svg|697]]

### 1. Linear $y = x$

**Shape:** straight line through the origin with gradient 1.
**Key features:** passes through $(0, 0)$ and $(1, 1)$; no curvature; symmetric about the origin (odd function).
**Why:** $y$ moves by the same amount as $x$ — constant rate of change. This is the simplest possible function shape.

### 2. Quadratic $y = x^2$

**Shape:** parabola, opening upward, vertex at the origin.
**Key features:** $y \geq 0$ for all $x$; axis of symmetry $x = 0$; doubles back on itself (fails the horizontal line test — not one-to-one).
**Why:** $x^2$ is non-negative, so the output is never below the $x$-axis. $(-x)^2 = x^2$ means left and right inputs give the same output — hence the mirror symmetry.

### 3. Cubic $y = x^3$

**Shape:** S-shaped curve rising from bottom-left to top-right, flattening at the origin.
**Key features:** passes through the origin; odd function ($(-x)^3 = -x^3$) so symmetric about the origin; has a **point of inflection** at $(0, 0)$ (it flattens but does not turn).
**Why:** $x^3$ keeps the sign of $x$, so negative inputs give negative outputs. The flattening at zero happens because $x^3$ grows much slower than $x$ near zero (e.g. $0.1^3 = 0.001$).

### 4. Reciprocal $y = \dfrac{1}{x}$

**Shape:** two hyperbola branches, one in the first quadrant, one in the third.
**Key features:** $y$-axis ($x = 0$) is a **vertical asymptote**; $x$-axis ($y = 0$) is a **horizontal asymptote**; never crosses either axis.
**Why:** division by zero is undefined, so $x = 0$ is excluded — and as $x$ approaches 0 the output blows up (vertical asymptote). As $\lvert x \rvert \to \infty$ the reciprocal squeezes to zero (horizontal asymptote). Odd function: $1/(-x) = -1/x$, so the two branches are reflections of each other through the origin.

### 5. Square root $y = \sqrt{x}$

**Shape:** half-parabola lying on its side, starting at the origin and rising to the right.
**Key features:** domain $x \geq 0$ (you cannot square-root a negative in the real numbers); passes through $(0, 0)$, $(1, 1)$, $(4, 2)$, $(9, 3)$; slope becomes gentler as $x$ grows.
**Why:** this is the **inverse** of $y = x^2$ restricted to $x \geq 0$, so its graph is the reflection of that half-parabola across the line $y = x$. The slowing slope reflects the fact that big input changes produce small output changes (e.g. going from $x = 100$ to $x = 121$ only changes $y$ from 10 to 11).

### 6. Exponential $y = a^x$ (with $a > 1$)

**Shape:** rises steeply left-to-right, passes through $(0, 1)$, asymptote $y = 0$ on the left.
**Key features:** $y > 0$ for all $x$; horizontal asymptote $y = 0$ as $x \to -\infty$; no $x$-intercept; $y$-intercept always $(0, 1)$ because $a^0 = 1$.
**Why:** repeated multiplication by $a > 1$ grows; repeated division (i.e. $a^{-n}$) shrinks but never hits zero. The $(0, 1)$ anchor is a direct consequence of $a^0 = 1$ — true for *every* base, so all exponential parents pass through this point. If $0 < a < 1$, the curve decays instead (same shape reflected in the $y$-axis).

> [!info] Beyond syllabus — the seventh parent, logarithm
> $y = \log_a x$ (for $a > 1$) is the **inverse** of the exponential, so its graph is the reflection of $y = a^x$ across $y = x$: vertical asymptote at $x = 0$, passes through $(1, 0)$, rises slowly to the right. Full treatment in [[Logarithms]].

---

## Key Features to Label

When the exam says "sketch $y = f(x)$, showing clearly...", it usually wants some subset of:

| Feature | English | 中文 | How to find |
|---------|---------|------|-------------|
| $y$-intercept | where curve crosses $y$-axis | $y$轴截距 | Set $x = 0$, compute $f(0)$ |
| $x$-intercept(s) / roots | where curve crosses $x$-axis | $x$轴截距 / 根 | Solve $f(x) = 0$ |
| Vertex / turning point | local max or min | 顶点 / 转折点 | Complete the square, or solve $f'(x) = 0$ |
| Axis of symmetry | vertical line through vertex | 对称轴 | For $y = ax^2 + bx + c$, $x = -\dfrac{b}{2a}$ |
| Vertical asymptote | where $f$ blows up | 铅直渐近线 | Find $x$ where denominator = 0 |
| Horizontal asymptote | end behaviour as $x \to \pm\infty$ | 水平渐近线 | Take $\lim_{x \to \pm\infty} f(x)$ |
| Point of inflection | curvature flips sign | 拐点 | Solve $f''(x) = 0$ (A-Level) |

Vocabulary cheat-sheet: [[Sketching Curves (Vocab)]] has the full list with Chinese translations.

---

## The Transformation Framework

Every transformed graph can be written as

$$y = a\,f\bigl(b(x - c)\bigr) + d$$

from a parent $y = f(x)$. Four knobs, four effects:

| Knob | Effect on graph | Name |
|------|-----------------|------|
| $d$ (outside, added) | Shift **up** by $d$ | Vertical translation |
| $c$ (inside, subtracted) | Shift **right** by $c$ | Horizontal translation |
| $a$ (outside, multiplier) | Stretch **vertically** by factor $\lvert a \rvert$; if $a < 0$, also reflect in $x$-axis | Vertical stretch / reflection |
| $b$ (inside, multiplier) | Stretch **horizontally** by factor $\dfrac{1}{\lvert b \rvert}$; if $b < 0$, also reflect in $y$-axis | Horizontal stretch / reflection |

**Outside is intuitive. Inside is backwards.** This is the single most important rule to internalise — and the reason half of graph-transformation questions go wrong.

### Why "inside is backwards" — the proof

Take a point $(x_0, y_0)$ on the parent graph, so $y_0 = f(x_0)$.

**Outside (intuitive).** On the transformed graph $y = f(x) + d$, the same input $x_0$ produces output $y_0 + d$. So $(x_0, y_0) \mapsto (x_0, y_0 + d)$: the whole graph shifts up by $d$. ✓

**Inside (counter-intuitive).** On the transformed graph $y = f(x - c)$, which input $x$ reproduces the original output $y_0$? We need $x - c = x_0$, so $x = x_0 + c$. So $(x_0, y_0) \mapsto (x_0 + c, y_0)$: the graph shifts **right** by $c$, even though $c$ is *subtracted* inside the function.

![[graphs-of-functions-inside-backwards.svg|697]]

The same logic gives the horizontal stretch rule: on $y = f(bx)$, the original output $y_0$ reappears when $bx = x_0$, i.e. $x = x_0/b$. So every point's $x$-coordinate is **divided** by $b$ — a horizontal stretch by factor $1/b$.

> [!tip] The memory shortcut
> **Outside moves the graph the way you'd expect.** $+d$ outside → up by $d$. $\times a$ outside → taller by $a$.
> **Inside moves the graph the opposite way.** $-c$ inside → shift **right** (positive direction). $\times b$ inside → **narrower** by factor $b$ (squeezed, not widened).

### Reflections

| Transformation | Effect |
|---------------|--------|
| $y = -f(x)$ | Reflect in the $x$-axis (flip outputs) |
| $y = f(-x)$ | Reflect in the $y$-axis (flip inputs) |
| $y = f^{-1}(x)$ | Reflect in the line $y = x$ (inverse function) |
| $y = \lvert f(x) \rvert$ | Reflect negative-output portions in the $x$-axis — see [[Modulus Function]] |
| $y = f(\lvert x \rvert)$ | Keep the right half, mirror it onto the left (forces even symmetry) |

---

## Composing Transformations — Order Matters

Graph transformations obey the same order-matters logic as [[Composite Function|composing functions]]. If you apply $f$ then $g$, you get a different result from applying $g$ then $f$ — the same is true of stacking transformations. The composite-function chain diagram makes the point crisply:

![[composite-function-chain.svg|697]]

The same idea applies here: $y = 3f(x - 2) + 5$ is "shift right 2, then stretch, then shift up" — a *specific* ordered stack. Do it in a different order and you get a different graph.

If the question says "starting from $y = f(x)$, apply transformations in this order: shift right 2, stretch vertically by 3, shift up 5," you get

$$y = 3f(x - 2) + 5.$$

But if the equation is given as $y = 3f(x - 2) + 5$ and you are asked to *describe* the transformations, the order to state them in is:

1. **Inside first** — horizontal moves (apply $-2$ before applying $f$).
2. **Outside second** — vertical moves (apply $\times 3$ then $+5$ after $f$).

Why? Because that's the order the expression is evaluated: plug in $x$, subtract 2, apply $f$, multiply by 3, add 5. Transformations follow the order of operations.

> [!warning] The "stretch then translate vs translate then stretch" trap
> $y = f(x - 2) + 3$ is not the same as $y = f(x) + 3$ then shifted right by 2 — well, actually in *that* case it is, because vertical and horizontal transformations commute with each other. But $y = f(3(x - 2))$ is NOT the same as "stretch horizontally by $1/3$, then shift right 2" — because $f(3(x - 2)) = f(3x - 6)$, so the shift inside is actually 2 (after factoring out the 3), not 6. **Always factor the inside** to read the shift cleanly.

---

## Sketching Workflow

For any transformed graph $y = a f(b(x - c)) + d$:

1. **Identify the parent** $y = f(x)$. Draw it lightly (just the shape).
2. **Apply inside transformations** — horizontal stretch by $1/b$, then shift right by $c$.
3. **Apply outside transformations** — vertical stretch by $a$ (reflect if $a < 0$), then shift up by $d$.
4. **Mark the key features on the new graph**:
   - New $y$-intercept: plug in $x = 0$.
   - New $x$-intercepts: solve the full equation.
   - Transformed asymptotes: apply the horizontal/vertical shifts to the parent's asymptotes.

Never try to plot random points from a transformed equation — it's slow and error-prone. The transformation machinery is always faster.

---

## Worked Examples

### Example 1 — Quadratic in vertex form

Sketch $y = 2(x - 3)^2 - 5$, showing the vertex and the $y$-intercept.

**Parent:** $y = x^2$, vertex at origin.
**Inside:** $x \mapsto x - 3$ shifts right by 3.
**Outside:** multiply by 2 (narrower, taller), then subtract 5 (shift down 5).

Vertex of parent $(0, 0) \mapsto (3, 0) \mapsto (3, -5)$.
$y$-intercept: set $x = 0$: $y = 2(9) - 5 = 13$. So $(0, 13)$.

Sketch: parabola opening upward, vertex $(3, -5)$, passing through $(0, 13)$. Axis of symmetry $x = 3$.

### Example 2 — Reciprocal with shifted asymptotes

Sketch $y = \dfrac{2}{x - 1} + 3$, showing both asymptotes.

**Parent:** $y = 1/x$, asymptotes $x = 0$ and $y = 0$.
**Inside:** $x \mapsto x - 1$ shifts right by 1. Vertical asymptote moves: $x = 0 \mapsto x = 1$.
**Outside:** multiply by 2 (vertical stretch, but the asymptote stays at $y = 0$), then add 3. Horizontal asymptote moves: $y = 0 \mapsto y = 3$.

$y$-intercept: $x = 0$ gives $y = \frac{2}{-1} + 3 = 1$. Point $(0, 1)$.
$x$-intercept: $\frac{2}{x - 1} + 3 = 0 \Rightarrow \frac{2}{x - 1} = -3 \Rightarrow x - 1 = -\frac{2}{3} \Rightarrow x = \frac{1}{3}$. Point $(1/3, 0)$.

Sketch: two branches, asymptotes $x = 1$ (vertical) and $y = 3$ (horizontal), passing through $(0, 1)$ and $(1/3, 0)$.

### Example 3 — Exponential decay with lift

Sketch $y = 4 \cdot 2^{-x} + 1$, showing the $y$-intercept and horizontal asymptote.

**Parent:** $y = 2^x$, asymptote $y = 0$, $y$-intercept $(0, 1)$.
**Inside:** $x \mapsto -x$ reflects in the $y$-axis → $y = 2^{-x}$, now decay. Still passes $(0, 1)$, asymptote still $y = 0$.
**Outside:** multiply by 4 → $y$-intercept becomes $(0, 4)$. Add 1 → shift up 1, so asymptote moves to $y = 1$ and $y$-intercept becomes $(0, 5)$.

Sketch: decay curve from top-left, passing through $(0, 5)$, asymptote $y = 1$.

### Example 4 — Identifying transformations from a graph

A graph looks like $y = \sqrt{x}$ but starts at $(2, -1)$ instead of $(0, 0)$, and at $x = 6$ the value is $y = 3$. Find the equation.

**Parent:** $y = \sqrt{x}$.
**Shifts:** starts at $(2, -1)$ instead of $(0, 0)$, so shift right 2 and down 1: $y = \sqrt{x - 2} - 1$.
**Vertical stretch:** at $x = 6$, parent-minus-shift gives $\sqrt{6 - 2} - 1 = 2 - 1 = 1$, but the question says $y = 3$. So output is scaled by factor 2 (applied to the $\sqrt{x - 2}$ part, *before* subtracting 1): $y = 2\sqrt{x - 2} - 1$.

Check: at $x = 6$, $y = 2\sqrt{4} - 1 = 4 - 1 = 3$. ✓
At $x = 2$, $y = 2\sqrt{0} - 1 = -1$. ✓

---

## Misconceptions

> [!warning] "$f(x + 3)$ shifts the graph right because $+3$ means positive direction"
> **WRONG.** $f(x + 3)$ shifts **left** by 3. Think: which $x$ reproduces the parent's value at $x_0$? $x + 3 = x_0 \Rightarrow x = x_0 - 3$ — every point moves 3 units left. Inside is backwards.

> [!warning] "$y = f(3x)$ stretches the graph horizontally by a factor of 3"
> **WRONG.** $y = f(3x)$ **compresses** the graph by factor 3 (makes it narrower). The stretch factor is $1/3$, not 3. Same "inside is backwards" rule.

> [!warning] "$y = -f(x)$ and $y = f(-x)$ are the same"
> **WRONG.** $y = -f(x)$ reflects in the **$x$-axis** (flips outputs); $y = f(-x)$ reflects in the **$y$-axis** (flips inputs). Easy to see on $y = x^3$: $-x^3$ is the mirror across the $x$-axis; $(-x)^3 = -x^3$ gives the same result only because $x^3$ is odd. On $y = x^2$, $f(-x) = x^2$ (unchanged — already even) while $-f(x) = -x^2$ flips it upside down.

> [!warning] "The vertex of $y = a(x - h)^2 + k$ is at $(-h, k)$"
> **WRONG.** The vertex is at $(h, k)$ — *positive* $h$. The formula is written with a minus sign *because* the vertex ends up at the positive value $h$. This is the inside-is-backwards rule in action.

---

## Exam Notes

### Cambridge 0580 Extended (priority curriculum)

**E2.10 Graphs of Functions** — sketch and interpret $y = ax^n$ for $n = -2, -1, 0, 1, 2, 3$, and simple exponentials $y = a \cdot b^x$. Tables of values may be required.
**E2.11 Sketching Curves** — shape recognition for linear, quadratic, cubic, reciprocal, exponential. See [[Sketching Curves (Vocab)]].

Typical question: "On the same axes, sketch $y = x^2$ and $y = 2(x-1)^2 + 3$. State the coordinates of the vertex of the second curve." Worth 3–4 marks.

### Cambridge 0606 (priority curriculum)

**§4.4 Cubic Graphs** — sketch $y = (x - a)(x - b)(x - c)$ style cubics from factored form, including the modulus $y = \lvert f(x) \rvert$ version. Full treatment in [[Cubic Graphs]] when that card is written.
**§1.4 Modulus** — the graph of $y = \lvert f(x) \rvert$ is a direct transformation of $y = f(x)$: flip negative parts upward. See [[Modulus Function]].
**§10.2–10.3 Trig Graphs** — transformation framework applied to $\sin$, $\cos$, $\tan$: $y = a\sin(bx) + c$ and $y = a\cos b(x - c)$. See [[Trigonometric Graphs]].

The $y = af(b(x-c)) + d$ framework is the engine behind all three of the above — master it here and those cards become mechanical.

### OxAQA 9260

**A12 Graphs of Functions** — recognise, sketch, and interpret graphs of linear, quadratic, cubic, reciprocal functions; exponential at Extension tier. Shape recognition is explicitly examined; transformation questions appear in the Extension.

### Cambridge 9709

**§1.2 (Functions), in the syllabus's own words:** "understand and use the transformations of the graph of $y = f(x)$ given by $y = f(x) + a$, $y = f(x+a)$, $y = af(x)$, $y = f(ax)$ **and simple combinations of these**" — with the guidance adding that answers should use the terms *translation*, *reflection* and *stretch*, and that questions "may involve algebraic or trigonometric functions, or other graphs with given features." So at 9709 the framework itself is the examined object: describe-the-transformation questions want the named word plus its data (translation by $\begin{pmatrix}-a\\0\end{pmatrix}$, stretch factor $\tfrac1a$ in the $x$-direction), and the combination questions stop at *simple* pairings.

### IB AA / AP Precalculus

The same framework, same vocabulary: IB AA Topic 2 (with the reciprocal transformation $y = \tfrac{1}{f(x)}$ added at HL), AP Precalculus Unit 1. Students arriving from IGCSE are expected to recognise the parent graphs without hesitation and compose transformations — that is the bar.

---

## Connections

- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — the $(x, y)$ plane.
- **Prerequisite:** [[Function]] — what a function is, domain and range, vertical line test.
- **Prerequisite:** [[Sketching Curves (Vocab)]] — vocabulary and key-feature terminology.
- **Prerequisite:** [[Completing the Square]] — needed to read vertex form of a parabola.
- **Application:** [[Quadratic Equations]] — roots, discriminant, vertex-form sketching.
- **Parallel idea:** [[Composite Function]] — stacking graph transformations *is* function composition; both are order-sensitive.
- **Application:** [[Exponential Function]] — the $y = e^x$ parent and its transformations.
- **Application:** [[Logarithms]] — $y = \ln x$ as reflection of $y = e^x$ in $y = x$.
- **Leads to:** [[Modulus Function]] — $y = \lvert f(x) \rvert$ as a transformation of $f(x)$.
- **Leads to:** [[Cubic Graphs]] — the 0606 §4.4 application; $y = k(x-a)(x-b)(x-c)$.
- **Leads to:** [[Trigonometric Graphs]] — $y = a\sin(bx + c) + d$ as the transformation framework applied to $\sin, \cos, \tan$.
- **Leads to:** [[Linearisation]] — 0606 §7.4: transform $y = Ax^n$ or $y = Ab^x$ into straight-line form by taking logs.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $f(x)$ | `f(x)` | Function notation |
| $y = f(x)$ | `y = f(x)` | Graph equation |
| $y = af(b(x-c)) + d$ | `y = af(b(x-c)) + d` | General transformation template |
| $y = \lvert f(x) \rvert$ | `y = \lvert f(x) \rvert` | Modulus of a function |
| $f^{-1}(x)$ | `f^{-1}(x)` | Inverse function |
| $\lim_{x \to \infty}$ | `\lim_{x \to \infty}` | Limit at infinity (for asymptotes) |
| $(h, k)$ | `(h, k)` | Vertex / turning-point coordinates |
