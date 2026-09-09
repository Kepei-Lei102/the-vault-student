---
chinese: 驻点 / 极值点 (zhùdiǎn / jízhídiǎn)
prerequisites:
  - "[[Differentiation]]"
  - "[[Power Rule]]"
  - "[[Completing the Square]]"
leads_to:
  - "[[Sketching Curves (Vocab)]]"
  - "[[Optimisation]]"
  - "[[Second Derivative Test]]"
  - "[[Kinematics Calculus]]"
  - "[[Mean Value Theorem]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-A15
  - syllabus/0580-E2-12
  - syllabus/0606-14-6
  - syllabus/9709-1-7
  - curriculum/Cambridge-9709
  - curriculum/Edexcel-IAL
  - curriculum/OxAQA-9660
  - curriculum/AP-Calculus-BC
  - syllabus/IAL-P2-7-1
  - syllabus/AP-BC-5-2
  - syllabus/AP-BC-5-3
  - syllabus/AP-BC-5-6
  - type/definition
  - type/method
  - notation/derivative
  - misconception/stationary-means-not-moving
---

# Stationary Points 驻点 / 极值点

## Definition

### Formal

A **stationary point** of a function $f(x)$ is a point where the derivative is zero:

$$f'(a) = 0$$

At a stationary point, the tangent to the curve is horizontal (gradient = 0).

There are three types of stationary point:

| Type | What happens to $f(x)$ | What $f'(x)$ does |
|---|---|---|
| Local maximum | $f(x)$ reaches a peak | $f'(x)$ changes from $+$ to $-$ |
| Local minimum | $f(x)$ reaches a trough | $f'(x)$ changes from $-$ to $+$ |
| Stationary point of inflection | $f(x)$ flattens but doesn't turn | $f'(x)$ doesn't change sign |

### Intuitive

Think of walking along a hilly road.

- At the **top of a hill** (local maximum), you were going up, then you stop, then you go down. The moment you're at the very top, the ground is flat — zero gradient.
- At the **bottom of a valley** (local minimum), you were going down, then you stop, then you go up. Again, the ground is momentarily flat.
- At a **flat section on a slope** (stationary point of inflection), the road briefly levels out but then keeps going the same direction — you were climbing, you pause, you keep climbing.

In every case, the gradient is zero at that exact moment. "Stationary" means the function has momentarily stopped rising or falling.

### 中文锚点 (Chinese Anchor)

**驻点** (zhùdiǎn)："驻"是停留、驻足的意思——函数在这里"停了一下"，斜率为零。

三种驻点：

- **极大值** (jídàzhí)：函数先升后降，到了山顶。$f'(x)$从正变负。
- **极小值** (jíxiǎozhí)：函数先降后升，到了谷底。$f'(x)$从负变正。
- **拐点**（水平拐点）：函数"停了一下"但没有转弯，继续朝同一方向走。$f'(x)$不变号。

关键判断：$f'(x) = 0$只告诉你"这里是平的"，不告诉你是山顶还是谷底。要判断类型，需要看$f'(x)$的变号情况，或者用$f''(x)$。

## Notation

| Symbol | Meaning | Example |
|---|---|---|
| $f'(a) = 0$ | Stationary point at $x = a$ | $f'(2) = 0$ means stationary at $x = 2$ |
| $f''(a) > 0$ | Concave up at $x = a$ → minimum | See second derivative test |
| $f''(a) < 0$ | Concave down at $x = a$ → maximum | See second derivative test |
| $f''(a) = 0$ | Inconclusive — need further investigation | Could be inflection or flat max/min |

## Key Facts / Properties

### Finding Stationary Points — The Method

**Step 1:** Differentiate to find $f'(x)$.

**Step 2:** Solve $f'(x) = 0$.

**Step 3:** Find the $y$-coordinates by substituting back into $f(x)$ (not $f'(x)$!).

**Step 4:** Determine the nature (type) of each stationary point.

### Determining the Nature — Two Methods

#### Method 1: First Derivative Test (sign change)

Check the sign of $f'(x)$ just before and just after the stationary point.

| $f'(x)$ before | $f'(x)$ after | Nature |
|---|---|---|
| $+$ (increasing) | $-$ (decreasing) | **Maximum** — went up then down |
| $-$ (decreasing) | $+$ (increasing) | **Minimum** — went down then up |
| $+$ (increasing) | $+$ (increasing) | **Stationary point of inflection** — paused, kept going |
| $-$ (decreasing) | $-$ (decreasing) | **Stationary point of inflection** — paused, kept going |

> [!tip] Why this works
> The derivative tells you whether the function is rising or falling. If the derivative changes sign through zero, the function changed direction — that's a turning point (max or min). If it doesn't change sign, the function just paused.

**How to check signs in practice:** Pick a convenient $x$-value slightly less than $a$ and slightly more than $a$. Substitute into $f'(x)$. You only need the sign, not the exact value.

#### Method 2: Second Derivative Test

Evaluate $f''(a)$ at the stationary point:

| $f''(a)$ | Nature | Why |
|---|---|---|
| $f''(a) < 0$ | **Maximum** | Gradient is decreasing → was positive, becomes negative → peak |
| $f''(a) > 0$ | **Minimum** | Gradient is increasing → was negative, becomes positive → trough |
| $f''(a) = 0$ | **Inconclusive** | Could be max, min, or inflection — must use Method 1 |

> [!info] Why the second derivative test works
> $f''(x)$ measures the rate of change of the gradient. At a stationary point, $f'(a) = 0$.
>
> If $f''(a) > 0$, the gradient is *increasing* at $x = a$. Since the gradient is zero at $a$ and increasing, it must have been negative just before and positive just after: that's a minimum.
>
> If $f''(a) < 0$, the gradient is *decreasing*. It was positive just before and negative just after: that's a maximum.
>
> Think of the physics parallel from [[Differentiation]]: if velocity is zero and acceleration is positive, you were moving backwards and are about to move forwards — you're at the bottom of your path.

> [!warning] When $f''(a) = 0$ — the test fails
> $f''(a) = 0$ does **not** mean it's a point of inflection. It means the test is inconclusive. You must fall back to the first derivative test (Method 1).
>
> Example: $f(x) = x^4$ has $f'(0) = 0$ and $f''(0) = 0$, but $x = 0$ is a **minimum** (not an inflection point). The first derivative test confirms this: $f'(x) = 4x^3$ is negative before 0 and positive after 0.

### The Physics Parallel

Continuing the displacement–velocity–acceleration story from [[Differentiation]]:

| Calculus | Physics | At a stationary point |
|---|---|---|
| $f(x)$ | Displacement | The position where you stop |
| $f'(x) = 0$ | Velocity = 0 | You've momentarily stopped moving |
| $f''(x)$ | Acceleration | Tells you what happens next |

When you throw a ball upward, at the very top it has zero velocity ($f'(t) = 0$). Gravity is still pulling it down ($f''(t) < 0$, negative acceleration). So the top is a **maximum** of height — exactly what $f''(t) < 0$ tells us.

### Sketching Curves Using Stationary Points

At 9260 (A15), you need to sketch curves when you know the stationary points. The full strategy:

1. **Find stationary points** — solve $f'(x) = 0$, get coordinates, determine nature
2. **Find the $y$-intercept** — substitute $x = 0$ into $f(x)$
3. **Find roots if possible** — solve $f(x) = 0$ (factorise or use other methods)
4. **Check end behaviour** — what happens as $x \to +\infty$ and $x \to -\infty$?
5. **Plot and connect** — mark all known points, draw a smooth curve through them respecting the gradient information

| Leading term | As $x \to +\infty$ | As $x \to -\infty$ | Shape |
|---|---|---|---|
| $+x^2$ | $\to +\infty$ | $\to +\infty$ | U-shape (smile) |
| $-x^2$ | $\to -\infty$ | $\to -\infty$ | ∩-shape (frown) |
| $+x^3$ | $\to +\infty$ | $\to -\infty$ | Bottom-left to top-right |
| $-x^3$ | $\to -\infty$ | $\to +\infty$ | Top-left to bottom-right |

### Points of Inflection — Scope Warning

> [!warning] Syllabus differences
> - **9260 A15:** includes "points of inflection" — students should know that a stationary point of inflection exists (where $f'(x) = 0$ but the gradient doesn't change sign)
> - **0606 14.6:** "points of inflection NOT included" — only maxima and minima
> - **0580 E2.12:** basic stationary points — maxima and minima only
>
> At A-Level/IB/AP, "point of inflection" has a broader meaning: any point where the *concavity* changes ($f''(x)$ changes sign). A **stationary** point of inflection also has $f'(x) = 0$; a **non-stationary** point of inflection has $f'(x) \ne 0$. At 9260, only the stationary kind matters.

### "Local" vs "Global"

A **local** maximum is the highest point *nearby* — the function might be higher somewhere else. A **global** maximum is the highest point on the entire domain.

Example: $f(x) = x^3 - 3x$ has a local maximum at $x = -1$ where $f(-1) = 2$, and a local minimum at $x = 1$ where $f(1) = -2$. But as $x \to +\infty$, $f(x) \to +\infty$, so there is no global maximum.

For polynomials of degree 3 or higher, stationary points are always local (never global) because the function eventually escapes to $\pm\infty$. Quadratics have one stationary point that is both local and global.

## Worked Examples

### Example 1 (9260 level): Find and classify the stationary points of $y = x^3 - 6x^2 + 9x + 1$

**Step 1: Differentiate.**

$$\dfrac{dy}{dx} = 3x^2 - 12x + 9$$

**Step 2: Solve $\dfrac{dy}{dx} = 0$.**

$$3x^2 - 12x + 9 = 0$$
$$x^2 - 4x + 3 = 0$$
$$(x - 1)(x - 3) = 0$$
$$x = 1 \quad \text{or} \quad x = 3$$

**Step 3: Find $y$-coordinates.**

At $x = 1$: $y = 1 - 6 + 9 + 1 = 5$ → point $(1, 5)$

At $x = 3$: $y = 27 - 54 + 27 + 1 = 1$ → point $(3, 1)$

**Step 4: Determine nature using the second derivative.**

$$\dfrac{d^2y}{dx^2} = 6x - 12$$

At $x = 1$: $f''(1) = 6 - 12 = -6 < 0$ → **Maximum** ✓

At $x = 3$: $f''(3) = 18 - 12 = 6 > 0$ → **Minimum** ✓

**Answer:** Local maximum at $(1, 5)$, local minimum at $(3, 1)$.

### Example 2 (9260 level): Show that $y = x^3 - 3x^2 + 3x + 2$ has a stationary point of inflection

$$\dfrac{dy}{dx} = 3x^2 - 6x + 3 = 3(x^2 - 2x + 1) = 3(x - 1)^2$$

Setting $\dfrac{dy}{dx} = 0$: $3(x-1)^2 = 0$ → $x = 1$.

**Second derivative test:** $\dfrac{d^2y}{dx^2} = 6x - 6$, so $f''(1) = 0$. Inconclusive!

**First derivative test:** $f'(x) = 3(x-1)^2 \geq 0$ for all $x$. The gradient is positive before $x = 1$ and positive after $x = 1$ (it equals zero only *at* $x = 1$). The sign doesn't change.

Therefore $x = 1$ is a **stationary point of inflection**. At this point $y = 1 - 3 + 3 + 2 = 3$, so the inflection is at $(1, 3)$.

> [!tip] How to recognise this pattern
> When $f'(x)$ factorises as a perfect square like $k(x - a)^2$, the gradient touches zero but doesn't go negative — it "bounces" off zero. This always gives a stationary point of inflection.

### Example 3 (9260 sketch): Sketch $y = 2x^3 - 3x^2 - 12x + 4$

**Stationary points:**

$\dfrac{dy}{dx} = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x-2)(x+1)$

$f'(x) = 0$ when $x = 2$ or $x = -1$.

$\dfrac{d^2y}{dx^2} = 12x - 6$

At $x = -1$: $f''(-1) = -18 < 0$ → maximum. $y = -2 - 3 + 12 + 4 = 11$. Maximum at $(-1, 11)$.

At $x = 2$: $f''(2) = 18 > 0$ → minimum. $y = 16 - 12 - 24 + 4 = -16$. Minimum at $(2, -16)$.

**$y$-intercept:** $y = 4$ when $x = 0$.

**End behaviour:** Leading term is $+2x^3$, so $y \to +\infty$ as $x \to +\infty$ and $y \to -\infty$ as $x \to -\infty$.

**Sketch:** The curve comes from bottom-left, rises to the maximum at $(-1, 11)$, falls through the $y$-intercept $(0, 4)$ to the minimum at $(2, -16)$, then rises to top-right.

## Common Misconceptions (Teaching Notes)

### 1. "$f'(x) = 0$ means it's a maximum or minimum"

Not always — it could be a stationary point of inflection. $f'(x) = 0$ only tells you the gradient is zero. You must check the *nature* of the stationary point using either the first or second derivative test.

**Fix:** "Zero gradient means stationary. Stationary means stopped — but it might start going the same direction again."

### 2. Substituting into $f'(x)$ instead of $f(x)$ for the $y$-coordinate

Students find $f'(a) = 0$ and report the stationary point as $(a, 0)$. The $y$-coordinate comes from $f(a)$, not $f'(a)$.

**Fix:** Emphasise: "$f'(x) = 0$ gives you the $x$-value. Go back to $f(x)$ for the $y$-value." Circle or underline the original equation as a reminder.

### 3. "The second derivative test always works"

It doesn't work when $f''(a) = 0$. Students either panic or wrongly assume inflection.

**Fix:** Teach both methods. The first derivative test (sign change) *always* works. The second derivative test is faster but has a known failure case. "If the second derivative test says nothing ($f''(a) = 0$), fall back to the sign change method."

### 4. Confusing stationary points with roots

Students mix up $f(x) = 0$ (roots — where the curve crosses the $x$-axis) and $f'(x) = 0$ (stationary points — where the curve is flat). These are completely different equations about completely different things.

**Fix:** "Roots: *where* is the curve at height zero? Stationary points: *where* is the curve flat?" Draw both on the same graph.

### 5. "A local maximum must be above a local minimum"

In Example 3 above, the maximum is at $y = 11$ and the minimum is at $y = -16$. This happens to have the maximum above the minimum. But consider $y = -x^3 + 12x$ — the local minimum at $x = -2$ gives $y = -16$ and the local maximum at $x = 2$ gives $y = 16$. Students sometimes expect this, but there's no rule requiring it.

**Fix:** The terms "maximum" and "minimum" are *local* — they describe the shape of the curve nearby, not the actual $y$-values.

## Exam Notes

### OxAQA 9260

- A15: find maxima, minima, and points of inflection; sketch curves using known stationary points
- Extension tier only
- Both Paper 1E and Paper 2E
- Typical questions:
  - "Find the stationary points of $y = ...$ and determine their nature"
  - "Show that the curve $y = ...$ has a maximum at ..."
  - "Sketch the curve, showing the coordinates of any stationary points"
- The second derivative test is the expected method (cleaner, faster)
- But know the first derivative test — it's needed when $f''(a) = 0$
- Only polynomials (degree 2 or 3) — no trig, no exponentials
- Points of inflection: rare at 9260 but in the spec; the "perfect square derivative" pattern ($f'(x) = k(x-a)^2$) is the most likely exam scenario

### Cambridge 0580

- E2.12: find stationary points (maxima and minima) — basic level
- No points of inflection required
- Expect quadratics and simple cubics only

### Cambridge 0606

- 14.6: find stationary points and determine their nature
- "Points of inflection NOT included" — this means the exam will never set a function whose stationary point is an inflection
- Still need the second derivative test — but it's always used for genuine maxima and minima, so $f''(a) = 0$ shouldn't arise on a 0606 paper
- Scope extends to rational powers (e.g., $y = x + \dfrac{4}{x}$) — requires rewriting as $y = x + 4x^{-1}$ before differentiating

### Cambridge 9709 — §1.7 (Paper 1)

- Locate stationary points and **determine their nature**; the second derivative test is the expected tool, with the first-derivative sign check accepted. Increasing/decreasing intervals come from the sign of $\dfrac{dy}{dx}$. Points of inflexion are not listed in §1.7 and are not set at Paper 1.
- Functions go beyond polynomials: $x^n$ for any rational $n$ and chain-rule composites such as $(2x - 1)^{-2}$ — the mark scheme gives a method mark for the derivative and separate marks for *each* stationary point's coordinates and nature.
- The same LO feeds the optimisation questions of [[Optimisation]] (the "show that the maximum volume is…" family).

### Edexcel IAL — P2.7.1

- Maxima, minima and stationary points; **increasing and decreasing functions** phrased as "find the set of values of $x$ for which $f$ is increasing". Nature via the second derivative or a sign table — either is credited. Inflexion is not in P2; it enters at P3/P4 through the second derivative's own behaviour.

### OxAQA 9660 — P1.3

- Max/min via the **second derivative test, named explicitly** in the spec, alongside tangents, normals and increasing/decreasing. Expect a polynomial or a simple rational-power function, and expect the nature to be asked for every point found.

### AP Calculus BC — Unit 5

- **5.2** Extreme Value Theorem and the distinction between **global and local** extrema: on a closed interval, compare the critical points *and the endpoints* (the candidates test) — this card's worked examples stop at local extrema, so treat the endpoint check as the one extra step AP demands.
- **5.3–5.5** the first derivative test and the candidates test; **5.6–5.7** concavity and the second derivative test, with **non-stationary inflection points** (where $f''$ changes sign but $f' \ne 0$) in scope — beyond every Cambridge board above.

### IB Mathematics AA

- HL: as AP, with optimisation in context; the second derivative test and inflexion points are both examined.

### Not examined on…

- **Cambridge 9231** — nothing beyond 9709.
- **Cambridge 0580** never sets a point of inflexion; **0606** says so in its own words ("points of inflection NOT included").

## Connections

- **Parent:** [[Differentiation]] — stationary points are defined by $f'(x) = 0$
- **Tool:** [[Power Rule]] — used to differentiate polynomials before solving $f'(x) = 0$
- **Companion:** [[Second Derivative Test]] — formal treatment of $f''(x)$ for determining nature (0606 depth)
- **Application:** [[Optimisation]] — real-world max/min problems using stationary points (0606 14.8)
- **Application:** [[Sketching Curves (Vocab)\|Sketching Curves]] — stationary points are key features when drawing graphs
- **Builds on:** [[Limit]] — the derivative that defines stationary points is itself a limit
- **Physics:** velocity = 0 at a turning point; acceleration determines if it's a max or min of displacement

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $f'(a) = 0$ | `f'(a) = 0` | Stationary point condition |
| $f''(a) > 0$ | `f''(a) > 0` | Minimum (second derivative test) |
| $f''(a) < 0$ | `f''(a) < 0` | Maximum (second derivative test) |
| $\dfrac{dy}{dx}$ | `\dfrac{dy}{dx}` | First derivative (Leibniz) |
| $\dfrac{d^2y}{dx^2}$ | `\dfrac{d^2y}{dx^2}` | Second derivative (Leibniz) |
| $\geq$ | `\geq` | Greater than or equal to |
| $\to +\infty$ | `\to +\infty` | Tends to positive infinity |
