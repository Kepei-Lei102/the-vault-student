---
chinese: 图像下的面积 (túxiàng xià de miànjī)
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

# Area Under a Graph 图像下的面积

## Definition

When a graph isn't a simple shape (rectangle, triangle, trapezium) the area under the curve can't be read off by formula. The **trapezium rule** estimates that area by chopping the region into thin **trapezia** of equal width and adding their areas.

For a curve on or above the horizontal axis, split the interval into $n$ strips of width $h$ with boundary ordinates ($y$-values) $y_0, y_1, y_2, \ldots, y_n$:

$$
\boxed{\;\text{Area} \;\approx\; \tfrac{h}{2}\!\left[\,y_0 + 2\bigl(y_1 + y_2 + \cdots + y_{n-1}\bigr) + y_n\,\right]\;}
$$

The rule says: "*half the strip width* times *(the first ordinate, plus twice every middle ordinate, plus the last ordinate)*." The first and last ordinates count once; every interior one counts twice — because every interior ordinate is shared between two adjacent trapezia.

Below the axis, the same formula estimates a **signed integral**. For total geometric area across an axis crossing, split at the crossing and add the positive areas.

The most common application: a **speed–time graph** that's curvy. The area under the curve is the distance travelled, but with a curved boundary you can't compute it exactly (yet) — the trapezium rule gives a numerical estimate.

### 中文锚点

骑车时，码表每隔十秒记一次速度，怎样估算这一段骑了多远？把相邻两次速度在图上用直线连起来，就等于暂且假设这十秒里速度是均匀变化的。把两次速度取平均，再乘上十秒，就得到这一小段路程的估计值；在图上，这正好是一个梯形的面积。把一小段一小段的路程加起来，便是梯形法则在做的事。它仍然只是估计：如果你在两次记录之间猛蹬了一下又刹车，那条直线就没能记下这段变化。

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
> Left- and right-endpoint rectangle sums use just one end of each strip. The trapezium rule joins both ends, so it is exact on a straight segment and cancels the leading endpoint error for smooth curves. It is **not always more accurate than every rectangle method**: midpoint rectangles can be better. Simpson’s rule fits quadratic pieces; its advantage also depends on the curve’s smoothness.

---

## Worked Example

> Estimate the area under the curve $y = x^2$ between $x = 0$ and $x = 4$ using the trapezium rule with **4 strips**.

**Step 1 — tool: equal subdivision.** Four equal strips across a width of four select $h = (4-0)/4 = 1$.

**Step 2 — tool: evaluate the function.** Four strips need five boundary heights, at $x = 0, 1, 2, 3, 4$:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $y = x^2$ | $0$ | $1$ | $4$ | $9$ | $16$ |

**Step 3 — tool: trapezium rule.** The requested straight-chord approximation gives:

$$
\text{Area} \approx \tfrac{1}{2}\bigl[0 + 2(1 + 4 + 9) + 16\bigr] = \tfrac{1}{2}\bigl[0 + 28 + 16\bigr] = \tfrac{1}{2}(44) = 22.
$$

**Compare to exact.** The exact area $\int_0^4 x^2\, dx = \dfrac{x^3}{3}\Big|_0^4 = \dfrac{64}{3} \approx 21.33$. So the trapezium rule with 4 strips overestimated by less than $0.7$ — about $3\%$ off. With more strips, the error shrinks fast.

> [!info] More strips → better estimate
> For a sufficiently smooth curve in the small-strip regime, doubling the strip count typically *quarters* the error. It is a smoothness-dependent trend, not a guarantee for every dataset or curve. With $n = 8$ strips the same calculation gives $\approx 21.5$ — within $0.2$ of the true value. This is why "use the trapezium rule with $n$ strips" questions get more accurate as $n$ grows.

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
> The deeper claim: As $h \to 0$ ($n \to \infty$), the left and right Riemann sums converge to the same value (for a continuous function on the closed interval), and their common limit is *defined* to be the integral $\int_a^b f(x)\,dx$. The trapezium rule, being their average, also converges to this limit; for sufficiently smooth functions, averaging cancels the leading endpoint errors and usually gives faster convergence than the left or right sum alone. Every numerical-integration scheme — trapezium, Simpson, Gaussian quadrature — is a clever choice of finite sum chasing the same limit.
>
> So **the trapezium rule is calculus's prequel.** Every time you add up $\tfrac{h}{2}[y_0 + 2(\cdots) + y_n]$, they're computing exactly the kind of finite sum that, in the limit, *defines what integration means*. See [[Integration]] for the limit version and [[Fundamental Theorem of Calculus]] for the shortcut that evaluates the integral when a suitable antiderivative is available.

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

1. **Counting the endpoints twice.** $y_0$ and $y_n$ count *once* each. Only the *interior* ordinates $y_1, \ldots, y_{n-1}$ count twice.
2. **Using strips of unequal width.** The formula above *assumes* equal-width strips. For unequal widths you'd compute each trapezium's area individually and sum — slower, but possible.
3. **Confusing $n$ ordinates with $n$ strips.** $n$ strips have $n + 1$ ordinates (the boundaries). "Use 4 strips" → tabulate 5 $y$-values. "Use 5 ordinates" → 4 strips.
4. **Treating the answer as exact.** The trapezium rule is generally an *estimate*, though it is exact for straight segments. The requested method and available information select the tool: a formula alone does not guarantee an elementary antiderivative, and “estimate” alone does not specify which numerical method to use.
5. **Forgetting units.** If the graph is a speed–time graph (speed in m/s, time in s), the area has units (m/s)·s = m. Always tag the answer with the right unit.

---

## Exam Notes

### Cambridge 0580 Extended — §E2.9

Distance is the area under a speed–time graph, but the 2025–27 syllabus restricts the assessed areas to **linear sections**. Add exact rectangles, triangles and trapezia. An $n$-strip approximation to a curved boundary is enrichment here, not a 0580 requirement.

### OxfordAQA 9260 — A17 Extension

Calculate or estimate areas under graphs, including quadratic and other non-linear graphs, and interpret them in context. Straight-chord strips provide an estimation method; this outcome does not explicitly prescribe the named trapezium rule.

### Cambridge 9709 — Pure Mathematics 2, §2.5 (Paper 2)

Use the trapezium rule to estimate a definite integral, and use a sketch to decide over- or under-estimation in simple cases. **Paper 2 is an AS-only route.** Pure Mathematics 3 assumes Paper 1; it does not automatically import every Paper 2 outcome. The trapezium rule is not a prescribed §3.5 outcome on Paper 3. “Paper 2 is largely a subset of Paper 3” does not mean it is wholly a subset.

### Pearson Edexcel IAL — P2 §8.3

Approximate area using the trapezium rule. Increasing the number of strips, improving accuracy and estimating error may be required. Keep the distinction between strip count and ordinate count explicit.

### OxfordAQA 9660 — P1.4

Use the trapezium rule, interpret ordinates, judge over- or under-estimation graphically, and refine by increasing the number of steps. P2.9 separately requires mid-ordinate and Simpson’s rules; this card’s passing mention does not teach that entire outcome.

### AP Calculus AB and BC — Topic 6.2, LIM-5.A

Approximate definite integrals using left, right, midpoint and trapezoidal sums, including **nonuniform partitions**, and reason about over- or under-estimation. For unequal widths, add the individual contributions $\tfrac12(x_{i+1}-x_i)(y_i+y_{i+1})$; do not force a common $h$. This card teaches the trapezoidal component, not every method in Topic 6.2.

### IB Mathematics — Applications and Interpretation, SL content shared with HL

The [guide’s calculus content](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-applications-interpretation-guide.pdf) requires trapezoidal area estimates from a function or table using equal-width intervals. The [Analysis and Approaches guide](https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/subject-guides/mathematics-analysis-approaches-guide.pdf) instead lists trapezoidal and Simpson techniques as enrichment alongside integration. These are the guides for the courses first assessed in 2021, not the forthcoming replacement courses.

### Where the named rule is not prescribed

The trapezium rule is not a named required outcome in Cambridge **0580, 0606 or 9231**, nor in **9709 Pure Mathematics 3**, or **IB Analysis and Approaches**. Area and integration themselves remain important on those courses; exclusion of one numerical rule is not exclusion of the concept. See [[Integration]] for antiderivatives and signed areas.

---

## Connections

- **Prerequisite:** [[Travel Graphs (Vocab)]] — distance from speed–time area; the 0580 requirement uses linear segments
- **Prerequisite:** [[Quadrilaterals (Vocab)]] — area of a trapezium = $\tfrac{1}{2}(a+b)h$ is the building block formula
- **Application:** *physics* — distance from speed-time, work done from force-distance, impulse from force-time
- **Leads to:** [[Integration]] — antiderivatives and the exact integral that numerical sums approximate
- **Leads to:** [[Fundamental Theorem of Calculus]] — explains why area-under-curve problems are solvable in closed form for nice functions
- **Beyond syllabus:** *Riemann sums* — the trapezium rule is the average of the left and right Riemann sums (see callout above); as $h \to 0$ all such sums converge to the same integral, for continuous functions on a closed interval
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
