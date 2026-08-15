---
chinese: 梯形法则 (tīxíng fǎzé)
prerequisites:
  - "[[Travel Graphs (Vocab)]]"
  - "[[Quadrilaterals (Vocab)]]"
  - "[[Sketching Curves (Vocab)]]"
leads_to:
  - "[[Integration]]"
  - "[[Fundamental Theorem of Calculus]]"
  - "[[Kinematics Calculus]]"
  - "[[Linear Momentum]]"
  - "[[SUVAT]]"
  - "[[Work, Energy and Power]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE-extension
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-9709
  - syllabus/0580-E2-9
  - syllabus/9709-2-5
  - syllabus/9260-A17
  - type/vocabulary
  - type/technique
  - notation/trapezium-rule
  - misconception/over-vs-under-estimate
---

# Area Under a Graph 梯形法则

## Definition

When a graph isn't a simple shape (rectangle, triangle, trapezium) the area under the curve can't be read off by formula. The **trapezium rule** estimates that area by chopping the region into thin **trapezia** of equal width and adding their areas.

For $n$ strips of width $h$ with ordinates ($y$-values) $y_0, y_1, y_2, \ldots, y_n$:

$$
\boxed{\;\text{Area} \;\approx\; \tfrac{h}{2}\!\left[\,y_0 + 2\bigl(y_1 + y_2 + \cdots + y_{n-1}\bigr) + y_n\,\right]\;}
$$

The rule says: "*half the strip width* times *(the first ordinate, plus twice every middle ordinate, plus the last ordinate)*." The first and last ordinates count once; every interior one counts twice — because every interior ordinate is shared between two adjacent trapezia.

The most common application: a **speed–time graph** that's curvy. The area under the curve is the distance travelled, but with a curved boundary you can't compute it exactly (yet) — the trapezium rule gives a numerical estimate.

### 中文锚点

**梯形法则 (tīxíng fǎzé)** = 用一系列**梯形 (tīxíng)** 来近似曲线下的面积。把区间分成 $n$ 个**等宽**的小区间（宽度为 $h$），每个小区间上画一个梯形（用直线连接相邻的两个 $y$ 值），然后把所有梯形的面积加起来。

公式：

$$\text{面积} \approx \tfrac{h}{2}\bigl[y_0 + 2(y_1+y_2+\cdots+y_{n-1}) + y_n\bigr].$$

**第一和最后一个 $y$ 值算一次，中间所有 $y$ 值都算两次** —— 这是因为中间每个 $y$ 值是两个相邻梯形共用的边。

---

## Key Vocabulary

| English | 中文 | Meaning |
|---------|------|---------|
| trapezium | 梯形 (tīxíng) | Quadrilateral with one pair of parallel sides — see [[Quadrilaterals (Vocab)]] |
| trapezium rule | 梯形法则 | The numerical method on this card |
| ordinate | 纵坐标 (zòng zuòbiāo) | A $y$-value used as a strip height |
| strip | 条 / 区间 | One of the equal-width slices the area is divided into |
| strip width | 条宽 / 步长 | $h$ — the width of one strip; total width $/ n$ |
| over-estimate | 高估 / 偏大 | An approximation that's bigger than the true value |
| under-estimate | 低估 / 偏小 | An approximation that's smaller than the true value |
| ordinates | 纵坐标 (plural) | The set of $y$-values $y_0, y_1, \ldots, y_n$ at the strip boundaries |

> [!info] Why "trapezium" and not "rectangle"
> A simpler method — the **rectangle rule** — uses rectangles of constant height. Trapezia win because the *top edge* of a trapezium connects two consecutive ordinates with a straight line, *tracking the curve more closely*. For the same number of strips, trapezia are dramatically more accurate. Even more accurate: **Simpson's rule**, which fits a parabola through three consecutive ordinates — but that's beyond 0580 (and a beautiful card for later).

---

## Worked Example

> Estimate the area under the curve $y = x^2$ between $x = 0$ and $x = 4$ using the trapezium rule with **4 strips**.

**Step 1 — strip width.** $h = (4-0)/4 = 1$.

**Step 2 — ordinates** at $x = 0, 1, 2, 3, 4$:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $y = x^2$ | $0$ | $1$ | $4$ | $9$ | $16$ |

**Step 3 — apply the rule.**

$$
\text{Area} \approx \tfrac{1}{2}\bigl[0 + 2(1 + 4 + 9) + 16\bigr] = \tfrac{1}{2}\bigl[0 + 28 + 16\bigr] = \tfrac{1}{2}(44) = 22.
$$

**Compare to exact.** The exact area $\int_0^4 x^2\, dx = \dfrac{x^3}{3}\Big|_0^4 = \dfrac{64}{3} \approx 21.33$. So the trapezium rule with 4 strips overestimated by less than $0.7$ — about $3\%$ off. With more strips, the error shrinks fast.

> [!info] More strips → better estimate
> Doubling the strip count typically *quarters* the error of the trapezium rule. With $n = 8$ strips the same calculation gives $\approx 21.5$ — within $0.2$ of the true value. This is why "use the trapezium rule with $n$ strips" questions get more accurate as $n$ grows.

> [!info] The trapezium rule is calculus in training wheels — meet the Riemann sum
> Strictly, a **Riemann sum** approximates the area under a curve using *rectangles*. There are two natural choices for each rectangle's height — the **left** ordinate or the **right** ordinate of the strip — giving the *left Riemann sum*
> $L_n = h(y_0 + y_1 + y_2 + \cdots + y_{n-1})$
> and the *right Riemann sum*
> $R_n = h(y_1 + y_2 + \cdots + y_n).$
>
> The trapezium rule is **literally the average** of the two:
>
> $$T_n = \tfrac{1}{2}(L_n + R_n) = \tfrac{h}{2}\bigl[y_0 + 2(y_1 + \cdots + y_{n-1}) + y_n\bigr].$$
>
> Try the algebra: $L_n$ counts $y_0, y_1, \ldots, y_{n-1}$ once each, and $R_n$ counts $y_1, \ldots, y_{n-1}, y_n$ once each. Add them: $y_0$ appears once (only in $L_n$), $y_n$ appears once (only in $R_n$), and every interior ordinate appears twice. Halve the result, factor the $h$ — and out drops the trapezium-rule formula. The mysterious "interior ordinates count twice" rule is just *the rule appearing twice — once in $L$, once in $R$*.
>
> The deeper claim — Riemann's 1854 thesis. As $h \to 0$ ($n \to \infty$), the left and right Riemann sums squeeze together (for any continuous function), and their common limit is *defined* to be the integral $\int_a^b f(x)\,dx$. The trapezium rule, being their average, also converges to this limit, and faster than either Riemann sum alone (because it averages out their leading errors). Every numerical-integration scheme — trapezium, Simpson, Gaussian quadrature — is a clever choice of finite sum chasing the same limit.
>
> So **the trapezium rule is calculus's prequel.** Every time a 0580 student adds up $\tfrac{h}{2}[y_0 + 2(\cdots) + y_n]$, they're computing exactly the kind of finite sum that, in the limit, *defines what integration means*. See [[Integration]] for the limit version and [[Fundamental Theorem of Calculus]] for the shortcut that bypasses the limit when the function is given by a formula.

---

## Over- vs Under-Estimate — read it off the curvature

The trapezium rule replaces the actual curve with **straight chords** between consecutive ordinates. Whether those chords sit *above* or *below* the curve depends on the curve's **concavity**:

| Curve shape | Chord position | Trapezium rule gives |
|---|---|---|
| **Concave up** (smiling, $\smile$) | chord *above* the curve | **Over**estimate |
| **Concave down** (frowning, $\frown$) | chord *below* the curve | **Under**estimate |
| Straight line | chord *equals* the curve | Exact |

For the $y = x^2$ example above, the parabola is concave up everywhere, so the trapezium rule overestimates ($22 > 21.33$ ✓).

> [!tip] How to remember it without thinking
> Picture the chord. For a "valley" curve ($\smile$) the chord is the top of the trapezium and sits *above* the curve, so the trapezium covers extra area not under the curve → **over**estimate. For a "hill" curve ($\frown$) the chord is below the curve, so the trapezium *misses* a sliver of area near the top → **under**estimate. Concavity points to the chord; the chord points to the answer.

---

## Common Misconceptions

1. **Counting the endpoints twice.** $y_0$ and $y_n$ count *once* each. Only the *interior* ordinates $y_1, \ldots, y_{n-1}$ count twice. A favourite trap on 0580 markschemes.
2. **Using strips of unequal width.** The formula above *assumes* equal-width strips. For unequal widths you'd compute each trapezium's area individually and sum — slower, but possible.
3. **Confusing $n$ ordinates with $n$ strips.** $n$ strips have $n + 1$ ordinates (the boundaries). "Use 4 strips" → tabulate 5 $y$-values. "Use 5 ordinates" → 4 strips.
4. **Treating the answer as exact.** The trapezium rule is an *estimate*. Exam phrasing "estimate the area" = trapezium rule. Exam phrasing "find the area" + curve given by a formula = use [[Integration]] (Extended / 0606+).
5. **Forgetting units.** If the graph is an s-t graph (speed in m/s, time in s), the area has units (m/s)·s = m. Always tag the answer with the right unit.

---

## Exam Notes

**Cambridge 0580 §E2.9 (Extended).** The 2025–27 syllabus asks for *distance travelled as area under a speed–time graph* — but with "areas will involve **linear sections of the graph only**": you compute *exact* areas of the triangles and trapezia the graph is built from (the $\tfrac{1}{2}(a+b)h$ building block), no $n$-strip estimation. The full trapezium *rule* on a curved graph is not 0580 content — it enters at A-Level.

**Cambridge 9709 (A-Level) — Paper 3.** The rule's true exam home: "understand and use the trapezium rule to estimate the value of a definite integral, **including use of sketch graphs in simple cases to determine whether the trapezium rule gives an over-estimate or an under-estimate**" — the boxed formula *and* the concavity table above are this LO, almost verbatim. (The syllabus lists it under Pure Mathematics 2, whose content Paper 3 carries; **Paper 2 is the AS-only route and Paper 3 is the A Level one**, so an A Level candidate meets this on Paper 3 and never sits Paper 2.) Typical shape: 3–4 marks for tabulating ordinates and applying the rule, plus a mark for the over/under judgement from a sketch.

**Forward to 0606 / A-Level.** [[Integration]] gives the exact area when the curve is given by a formula. The trapezium rule remains essential whenever the function isn't elementary or only data is available — used routinely in physics labs, engineering, statistics (CDFs), and any Monte Carlo / numerical setting.

**Beyond 0580.** [[Fundamental Theorem of Calculus]] explains *why* "area under the curve" equals "antiderivative evaluated at the endpoints" — the trapezium rule is a numerical sneak-preview of this theorem, replacing the limit-of-rectangles definition with a tractable approximation.

---

## Connections

- **Prerequisite:** [[Travel Graphs (Vocab)]] — the most common context in which the trapezium rule is asked at 0580 (area under s-t graph = distance)
- **Prerequisite:** [[Quadrilaterals (Vocab)]] — area of a trapezium = $\tfrac{1}{2}(a+b)h$ is the building block formula
- **Application:** *physics* — distance from speed-time, work done from force-distance, impulse from force-time
- **Leads to:** [[Integration]] — the exact analogue when a formula is available
- **Leads to:** [[Fundamental Theorem of Calculus]] — explains why area-under-curve problems are solvable in closed form for nice functions
- **Beyond syllabus:** *Riemann sums* — the trapezium rule is the average of the left and right Riemann sums (see callout above); as $h \to 0$ all such sums converge to the same integral, which is Riemann's 1854 *definition* of integrability
- **Beyond syllabus:** *Simpson's rule* (parabolic strips, fourth-order accuracy), *Romberg integration* (combining trapezium estimates at different strip counts via Richardson extrapolation), *Gaussian quadrature* (optimal sampling points) — the numerical-integration family tree

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $h$ | `h` | Strip width (also called "step size") |
| $y_0, y_1, \ldots, y_n$ | `y_0, y_1, \ldots, y_n` | Ordinates at the strip boundaries |
| $\tfrac{h}{2}\!\left[y_0 + 2(y_1 + \cdots + y_{n-1}) + y_n\right]$ | trapezium rule | The boxed formula |
| $\smile$ | `\smile` | Concave-up symbol (mnemonic) |
| $\frown$ | `\frown` | Concave-down symbol (mnemonic) |
| $\int_a^b f(x)\,dx$ | `\int_a^b f(x)\,dx` | The exact integral the rule approximates |
