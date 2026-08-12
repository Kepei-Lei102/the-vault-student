---
chinese: 最优化 (zuìyōuhuà) / 最值问题
prerequisites:
  - "[[Differentiation]]"
  - "[[Stationary Points]]"
  - "[[Chain Rule]]"
  - "[[Quadratic Equations]]"
  - "[[Tangents and Normals]]"
leads_to:
  - "[[Extreme Value Theorem]]"
teach_together:
  - "[[Connected Rates of Change]]"
tags:
  - subject/mathematics
  - domain/calculus
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-14-8
  - syllabus/0606-14-9
  - type/deep
  - type/technique
  - type/application
  - notation/second-derivative
  - misconception/forgot-to-classify
  - misconception/forgot-endpoints
  - misconception/two-variables-still
---

# Optimisation 最优化

## Definition

**Optimisation** is the use of calculus to find the *largest* or *smallest* value of a quantity, subject to constraints. The classic exam form: "An open-top box is made by cutting squares of side $x$ from a $20 \times 30$ sheet of cardboard and folding up the sides. Find the value of $x$ that maximises the volume."

The recipe is the same every time:

1. **Identify the objective** — what quantity do you want to maximise or minimise? Call it $f$.
2. **Express $f$ in terms of one variable** — use any constraints (fixed perimeter, fixed volume, geometric relationships) to eliminate other variables until $f$ depends on a single $x$.
3. **Differentiate and set to zero** — solve $\dfrac{df}{dx} = 0$ to find *critical points* (candidates for max/min).
4. **Classify each critical point** — use the **second derivative test** ($f''$) or a sign-of-$f'$ chart to decide whether each critical point is a max, min, or neither.
5. **Check endpoints** if the domain is a closed interval — the absolute max/min could occur at the boundary instead of at a critical point.
6. **Translate the answer back** — the question asked for $x$ *or* for the maximum value $f(x)$ *or* for both. Read the question carefully.

Steps 1, 2, and 6 are the *modelling* part — they belong as much to algebra as calculus. Steps 3–5 are the calculus.

> [!info] "Optimisation" is one of the biggest words in modern science
> When a 0606 student hears "optimisation" they think *find the max of a cubic*. When a research engineer hears it they think **training a neural network**. The word means the same thing in both worlds — *find the input that makes the objective extreme* — but the modern application is staggeringly bigger. Every AI model you've ever interacted with (Claude, GPT, image generators, recommendation systems, self-driving perception, AlphaFold) was *trained* by an optimisation algorithm: the loss function is the objective, the model's billions of parameters are the variables, and a derivative-based search (gradient descent) tries to find the global minimum.
>
> The 0606 framework — set $f' = 0$, classify with $f''$ — is the *one-variable, exact-arithmetic* version. Modern AI runs the *billion-variable, approximate, iterative* version, but the conceptual bridge is right there: same calculus, scaled up by a factor of $10^9$. When you set $\frac{dV}{dx} = 0$ to find the best box, you're doing what a Tesla's autopilot training run does on every minibatch. The Beyond Syllabus section unpacks the modern picture; the framework on this card is the foundation.

This card stays inside the 0606 framing but cashes in on the bridge wherever it appears.

### 中文锚点

**最优化 (zuìyōuhuà)** = 用微积分求**极值** (jízhí) — 最大值或最小值。

考试套路（六步走）：
1. **确定目标函数 (mùbiāo hánshù)** $f$
2. **用约束 (yuēshù) 消去多余变量**，让 $f$ 只含一个 $x$
3. **求导，令 $f'(x) = 0$，解出临界点**
4. **用二阶导数 $f''$ 判别**：$f'' > 0$ → 极小值，$f'' < 0$ → 极大值，$f'' = 0$ → 失效（用别的方法）
5. **检查端点** — 如果是闭区间，最值可能在端点
6. **回答原问题** — 题目要的是 $x$ 还是 $f(x)$？读清楚

---

## The Second Derivative Test

After you've found a critical point $x = a$ where $f'(a) = 0$, you need to decide whether it's a local maximum, a local minimum, or neither. The **second derivative test** is the cleanest tool:

$$
\boxed{
\begin{aligned}
f''(a) > 0 \;&\Rightarrow\; \text{local minimum at } x = a \quad (\smile, \text{concave up}) \\
f''(a) < 0 \;&\Rightarrow\; \text{local maximum at } x = a \quad (\frown, \text{concave down}) \\
f''(a) = 0 \;&\Rightarrow\; \text{test is inconclusive — use first derivative or higher.}
\end{aligned}}
$$

![[second-derivative-test-three-cases.svg]]

Above: at every critical point ($f' = 0$, horizontal tangent), the *curvature* decides which kind of extremum you have. Concave up (the curve smiles, $\smile$) → the tangent sits at the bottom of a bowl, so you're at a *minimum*. Concave down ($\frown$) → tangent is the top of a hill, so you're at a *maximum*. Curvature = $f''$, so the sign of $f''$ at the critical point answers the question directly.

### Why the test works — Taylor intuition

Near $x = a$, the Taylor expansion is

$$f(x) \approx f(a) + f'(a)(x-a) + \tfrac{1}{2} f''(a)(x-a)^2 + \cdots$$

At a critical point, $f'(a) = 0$, so the first-order term vanishes:

$$f(x) - f(a) \approx \tfrac{1}{2} f''(a)(x-a)^2.$$

The right side is a (small) parabola in $(x-a)$, opening *up* if $f''(a) > 0$ and *down* if $f''(a) < 0$. That's the entire test in one line: locally, $f$ looks like a parabola, and $f''(a)$ decides the parabola's direction. Maximum when the parabola opens down; minimum when it opens up. The bigger machinery — what Taylor expansion *is*, why polynomial approximations exist for any smooth function, and how higher-order terms repair the test when $f''(a) = 0$ — is the subject of [[Taylor Series]] (AP Calculus BC, A-Level Further, IB AA HL).

### When $f''(a) = 0$ — the test fails

Consider $f(x) = x^4$. Then $f'(x) = 4x^3$, so $f'(0) = 0$ — a critical point. But $f''(x) = 12x^2$, so $f''(0) = 0$ too. Test inconclusive.

But $x^4$ has an obvious minimum at $0$ (the function is non-negative everywhere). The test failed not because the function lacks an extremum but because the parabolic approximation is *too crude* — $x^4$ is "flatter than a parabola" near zero. You need to look at higher derivatives (the *fourth* derivative settles it for $x^4$ — see [[Taylor Series]]), or use the first-derivative-sign test instead.

> [!info] First Derivative Test — the fallback
> When the second derivative test is inconclusive (or you'd rather not compute $f''$), use the **sign chart of $f'$**:
>
> - $f'$ changes from $+$ to $-$ across $a$ → local **maximum** at $a$ (function was rising, now falling)
> - $f'$ changes from $-$ to $+$ across $a$ → local **minimum** at $a$ (function was falling, now rising)
> - $f'$ keeps the same sign across $a$ → **not an extremum** (a horizontal point of inflection, like $f(x) = x^3$ at $x=0$)
>
> The first derivative test catches *every* extremum, even when the second derivative test fails. The second derivative test is faster *when it works*; the first derivative test always works.

---

## The Closed-Interval Method (cashes [[Extreme Value Theorem]])

When the domain is a closed interval $[a, b]$ and the function is continuous, the absolute max and absolute min are *guaranteed* to exist (this is the Extreme Value Theorem, see [[Extreme Value Theorem]]). They can occur in only two places:

- at a **critical point** inside $(a, b)$, or
- at an **endpoint**, $x = a$ or $x = b$.

So the recipe is:

1. Find all critical points in $(a, b)$.
2. List those critical points plus the two endpoints.
3. Evaluate $f$ at every point in the list.
4. The largest value is the absolute maximum; the smallest is the absolute minimum.

> [!warning] Endpoints can win — don't skip them
> The absolute extreme of a function on a closed interval might *not* be at a critical point. For $f(x) = x$ on $[0, 1]$, $f'(x) = 1$ everywhere — no critical points — and the max ($1$) and min ($0$) are both at endpoints. Always check endpoints when the question gives a closed interval.

---

## Worked Examples

> [!info] These examples are not toy problems — they're real engineering
> The three examples below are textbook problems for a reason: they are *literally what people do for a living*. Packaging engineers solve "largest box from a fixed sheet" every day (cut waste = profit margin); brewery and aerospace tank designers solve "minimum surface area for fixed volume" every time they spec a vessel (less metal = lighter, cheaper, less heat loss); civil engineers and farmers solve "best rectangle for fixed perimeter" when laying out fields, parking lots, or building footprints. Calculus is where mathematics becomes *a way of asking the world to be efficient*.
>
> When you start with calculus, you start seeing optimisation everywhere — soda can dimensions, parcel-shipping pricing brackets, the way phones balance battery against thinness, even the *shape* of soap bubbles (which minimise surface area for fixed volume — the answer is "a sphere," and bubbles solve the calculus instantly with physics). Once you have the framework, the world looks different.

### Example 1 — the canonical open-top box (packaging)

> A rectangular sheet of metal $20 \text{ cm} \times 30 \text{ cm}$ has a square of side $x$ cut from each corner. The four flaps are folded up to make an open-top box. Find the value of $x$ (in cm) that maximises the volume, and find the maximum volume.

**Step 1 — objective.** Volume of the box: $V = (\text{length})(\text{width})(\text{height})$.

**Step 2 — express in one variable.** After cutting and folding, length $= 30 - 2x$, width $= 20 - 2x$, height $= x$. So

$$V(x) = x(20 - 2x)(30 - 2x) = x(600 - 100x + 4x^2) = 4x^3 - 100x^2 + 600x.$$

**Domain:** $0 < x < 10$ (the smaller side $20 - 2x$ must be positive, so $x < 10$; and $x > 0$).

**Step 3 — differentiate and set to zero.**

$$V'(x) = 12x^2 - 200x + 600 = 4(3x^2 - 50x + 150).$$

Solve $3x^2 - 50x + 150 = 0$ using the quadratic formula:

$$x = \frac{50 \pm \sqrt{2500 - 1800}}{6} = \frac{50 \pm \sqrt{700}}{6} = \frac{50 \pm 10\sqrt{7}}{6} = \frac{25 \pm 5\sqrt{7}}{3}.$$

Numerically: $\sqrt{7} \approx 2.6458$, so $x \approx 12.74$ or $x \approx 3.92$. Only $x \approx 3.92$ lies in $(0, 10)$ — discard the other.

**Step 4 — classify.** Compute the second derivative:

$$V''(x) = 24x - 200.$$

At $x \approx 3.92$: $V''(3.92) \approx 24(3.92) - 200 \approx -106 < 0$. **Local maximum.** ✓

**Step 5 — evaluate.** $x = \dfrac{25 - 5\sqrt{7}}{3} \approx 3.924$.

$$V(3.924) \approx 4(3.924)^3 - 100(3.924)^2 + 600(3.924) \approx 60.43 - 1539.7 + 2354.4 \approx 1056.3 \text{ cm}^3.$$

**Step 6 — answer.** The volume is maximised at $\boxed{x \approx 3.92 \text{ cm}}$, giving $V_\text{max} \approx 1056 \text{ cm}^3$.

> [!info] Why this problem is famous
> Every calculus syllabus on Earth includes some variant of "open box from a sheet." It's a perfect demonstration of optimisation because: (a) the volume is a tractable cubic in $x$, (b) the answer is *not* an obvious "nice" number — it requires the quadratic formula, which means students who try to guess will fail, (c) the constraints (positive side lengths) genuinely matter and reject one of the two critical points. It tests modelling *and* calculus *and* algebra simultaneously.

### Example 2 — cylinder of minimum surface area (vessel design)

> A closed cylindrical tin can hold $1$ litre ($1000$ cm³) of liquid. Find the dimensions (radius $r$ and height $h$) that minimise the total surface area.

**Step 1 — objective.** Total surface area = top + bottom + curved side: $S = 2\pi r^2 + 2\pi r h$.

**Step 2 — constraint.** Volume fixed: $\pi r^2 h = 1000$, so $h = \dfrac{1000}{\pi r^2}$.

Substitute:

$$S(r) = 2\pi r^2 + 2\pi r \cdot \frac{1000}{\pi r^2} = 2\pi r^2 + \frac{2000}{r}.$$

**Domain:** $r > 0$.

**Step 3 — differentiate.**

$$S'(r) = 4\pi r - \frac{2000}{r^2}.$$

Set to zero: $4\pi r = \dfrac{2000}{r^2}$, so $r^3 = \dfrac{500}{\pi}$, giving

$$r = \sqrt[3]{\frac{500}{\pi}} \approx 5.42 \text{ cm}.$$

**Step 4 — classify.**

$$S''(r) = 4\pi + \frac{4000}{r^3} > 0 \quad \text{for all } r > 0.$$

Always positive → critical point is a **minimum**. ✓

**Step 5 — find $h$.**

$$h = \frac{1000}{\pi r^2} = \frac{1000}{\pi (5.42)^2} \approx 10.84 \text{ cm}.$$

Notice: $h \approx 2r$. The optimal can has **height equal to diameter** — a beautiful result, and the reason every soup can looks roughly cubic when you stand it next to a ruler. (Real cans are slightly off-optimal because they include features the maths ignores: the lip seal, label area, stacking ratio, manufacturing tolerances.)

> [!info] Why $h = 2r$ for the optimum is *intuitive*
> A sphere — the lowest-surface-area shape for a given volume — has equal "extent" in every direction. The closed cylinder is forced to be axially symmetric (radius vs. height), and the optimum tries to be "as sphere-like as possible" subject to that constraint. "Height = diameter" makes the cylinder look like a cube circumscribed around a sphere — the closest a cylinder can come to spherical symmetry. Exam-friendly version: always check whether the answer is "everything equal" — it usually is, and it tells you you've solved the problem.

### Example 3 — fence around a field (land-use)

> A farmer wants to fence off a rectangular field along a straight river. He has $200$ m of fencing and only needs to fence three sides (the river is the fourth). Find the dimensions that maximise the field's area.

**Step 1 — objective.** Area $A = xy$ where $x$ is the side parallel to the river and $y$ is each of the two perpendicular sides.

**Step 2 — constraint.** Total fence used: $x + 2y = 200$, so $x = 200 - 2y$.

$$A(y) = (200 - 2y) \cdot y = 200y - 2y^2.$$

**Domain:** $0 < y < 100$.

**Step 3 — differentiate.** $A'(y) = 200 - 4y$. Set to zero: $y = 50$ m.

**Step 4 — classify.** $A''(y) = -4 < 0$. **Local max.** ✓

**Step 5 — find $x$.** $x = 200 - 2(50) = 100$ m.

**Answer.** $x = 100$ m, $y = 50$ m, $A_\text{max} = 5000$ m². The river-side dimension is *twice* the perpendicular dimension — the fence-saving from sharing one side with the river makes the optimal field longer than wide.

> [!tip] AM-GM as a calculus-free shortcut for these problems
> Many fixed-perimeter / fixed-area / fixed-volume optimisations can be solved without calculus using the *AM-GM inequality*: $\dfrac{a + b}{2} \ge \sqrt{ab}$ with equality iff $a = b$. For Example 3, write the area as $A = xy$ subject to $x + 2y = 200$; let $u = x, v = 2y$, then $u + v = 200$ and $A = \tfrac{uv}{2}$. AM-GM says $\tfrac{u+v}{2} \ge \sqrt{uv}$, so $uv \le 100^2 = 10000$, with equality when $u = v = 100$. Hence $A \le 5000$, achieved at $x = 100, y = 50$. *Calculus optional.* (See Beyond Syllabus for the general AM-GM machinery.)

---

## Common Mistakes

1. **Forgetting to express the objective in one variable.** Differentiating $f(x, y)$ before eliminating $y$ via the constraint produces partial derivatives — content out-of-scope for 0606 (and a different theory). Use the constraint *first* to reduce to one variable.
2. **Forgetting to classify the critical point.** "$f'(a) = 0$" alone doesn't tell you whether it's a max, a min, or a horizontal inflection. Always run the second derivative test (or the sign-chart method) before claiming "max" or "min."
3. **Forgetting to check endpoints on a closed interval.** The absolute extreme might lie at $x = a$ or $x = b$ rather than at an interior critical point. List all candidates *including* endpoints, then pick.
4. **Misreading the question.** "Find the value of $x$ at maximum" wants a coordinate. "Find the maximum value" wants $f(x_\text{max})$. "Find the dimensions" wants both $x$ and any derived quantities (height, width). Translate the answer back into the language of the original question.
5. **Domain errors.** Many word problems have implicit positivity constraints ($x > 0$, side lengths positive, etc.) that may eliminate one of the critical points. Always state and check the domain.
6. **Sign errors in $f''$.** A misplaced minus sign turns a max into a min. Triple-check the differentiation; if the answer feels wrong (e.g. the "minimum" volume is negative), suspect a sign error.

---

## Exam Notes

### Cambridge 0606

**Syllabus refs:** §14.8 (practical maxima and minima problems) and §14.9 (first and second derivative tests, points of inflection NOT included). Exam patterns:

- **Pattern A — geometry word problem.** Open box, closed cylinder, fence around a field, cone inscribed in a sphere, ladder against a wall. Usually 6–8 marks: 2 for setting up the objective, 2–3 for differentiating and solving, 1 for the second derivative test, 1 for the final answer in correct units.
- **Pattern B — given a function, find its max/min.** "$f(x) = x^3 - 6x^2 + 9x$ on $[0, 4]$. Find the maximum value of $f$." Closed-interval method: critical points + endpoints, evaluate, pick the largest.
- **Pattern C — cost or revenue function.** "A factory's daily cost is $C(x) = \ldots$ where $x$ is units produced. Find the production level that minimises cost." Same recipe, economic dressing.

> [!tip] 0606 markscheme is generous on classification — use the second derivative test
> Cambridge gives 1 mark for "use of $f''$ to confirm max/min" even if the rest of the problem is tightly scored. Don't skip step 4: it's a free mark, and it's the step that proves you understood the question. The first-derivative-sign chart works too but is more verbose; $f''$ is faster.

### A-Level / IB AA / AP Calculus

A-Level extends the same framework to:

- **Constrained optimisation in 2 variables** via *Lagrange multipliers* (A-Level Further, IB AA HL, AP BC) — the partial-derivative generalisation when you can't easily eliminate a variable.
- **Optimisation under inequality constraints** — the KKT conditions, foundational for linear programming and convex optimisation.
- **Implicit-function optimisation** — when the objective and constraint can't be solved for one variable explicitly; differentiate implicitly and solve the system.

AP Calculus AB/BC: identical 0606 framework, plus careful insistence on the *closed-interval method* (cashes the [[Extreme Value Theorem]]) for absolute max/min questions.

---

## Beyond Syllabus

### AM-GM and the inequality approach

The **arithmetic-geometric mean inequality** says that for non-negative reals,

$$\frac{a_1 + a_2 + \cdots + a_n}{n} \ge \sqrt[n]{a_1 a_2 \cdots a_n}$$

with equality if and only if all $a_i$ are equal. For two variables this is $\dfrac{a+b}{2} \ge \sqrt{ab}$.

Many fixed-sum-and-maximise-product (or fixed-product-and-minimise-sum) problems are AM-GM in disguise. The *equality condition* "all variables equal" is often the optimum — which is why Example 2's answer was $h = 2r$ (the cylinder's height "equal to" its diameter once you account for the symmetry) and Example 3's was $x = 2y$ (the river side "equal to" the two perpendicular sides combined).

In competition mathematics (USAMO, Putnam, IMO), AM-GM and its generalisations (Cauchy-Schwarz, power-mean, rearrangement inequality) are *the* way to solve optimisation problems without calculus. They're faster, more elegant, and often expose *why* the equality case is what it is.

### Lagrange Multipliers — constrained optimisation in higher dimensions

When the constraint can't be eliminated easily (e.g. "maximise $f(x, y, z)$ subject to $g(x, y, z) = c$"), substitute-and-reduce fails. Lagrange's idea (1788): at the optimum, the gradient of $f$ must be parallel to the gradient of $g$ — otherwise, you could move along the constraint surface in a direction that increases $f$. The condition is

$$\nabla f = \lambda \, \nabla g$$

for some scalar $\lambda$ (the *multiplier*). Combined with the constraint $g = c$, this is a system of equations in the unknowns $(x, y, z, \lambda)$ — solve it and you have the candidates.

This is the gateway to *constrained optimisation*: economics (utility maximisation subject to a budget), physics (the principle of stationary action), machine learning (regularised regression), and operations research all run on Lagrange's idea.

### Convex Optimisation, Gradient Descent, and the Training of AI

Modern AI runs on optimisation. Every model — language model, image classifier, protein-structure predictor, autonomous-driving stack — has a **loss function** (how badly it's doing on training data) and **billions of parameters** (the model's weights). Training the model = finding the parameters that minimise the loss. That's exactly the optimisation problem on this card, just with $10^9$ variables instead of $1$.

The algorithm: **gradient descent**. Start anywhere, compute $\nabla f$ (the multi-variable analogue of $f'$), step in the direction that decreases $f$ the fastest, repeat. It's the high-dimensional version of "follow $f'$ downhill until $f' = 0$." When the loss landscape is **convex** ($f'' \ge 0$ everywhere, generalised to many variables) the method is guaranteed to find the *global* minimum — the lowest possible loss, the best possible model. There's no "wrong valley" the algorithm could get stuck in.

Modern deep-learning loss landscapes are *not* convex. Neural networks have countless local minima and saddle points spread across millions of dimensions, and gradient descent can in principle get stuck in a *local* minimum that's far from the global optimum. A huge amount of practical art goes into making it work anyway — good initialisations, momentum (Adam, RMSProp), batch normalisation, learning-rate schedules, dropout. The empirical fact that deep learning *does* work despite being non-convex is one of the most active and beautiful open questions in modern mathematics. (Current best guess: the loss landscapes of large neural networks have a lot of *near-equivalent* local minima, so gradient descent finds a "good enough" one. But nobody has a complete theory yet.)

So when you set $f' = 0$ on this card to find a max or min — you are doing, in miniature and with exact arithmetic, *what an entire training run of Claude or GPT does*, scaled up by a factor of a billion variables and a few weeks of GPU time. The principle is the same. The 0606 calculus is the foundation; the modern application is one of the great achievements of human computation.

### Calculus of Variations — optimisation over functions

What if you want to optimise *over a whole function*, not over a single variable? The classic problem: among all curves connecting two points, which one allows a bead to slide down it (under gravity, no friction) in the *shortest time*? (Answer: the cycloid — Bernoulli, 1696. Not the straight line.)

This is the **brachistochrone problem**, and it launched the **calculus of variations** — calculus where the unknown is a function $y(x)$ and the objective $\int F(x, y, y')\, dx$ is a *functional*. The Euler-Lagrange equation,

$$\frac{\partial F}{\partial y} - \frac{d}{dx}\!\left(\frac{\partial F}{\partial y'}\right) = 0,$$

is the analogue of "$f'(x) = 0$" for functionals. It's the foundation of **classical mechanics** (the principle of least action: the actual trajectory of a particle minimises a quantity called *action* over all possible paths), **general relativity** (geodesics in spacetime), **optics** (Fermat's principle: light takes the path of least time), and the **finite-element method** in engineering simulation.

The everyday optimisation on this card is the tip of an iceberg that goes all the way down to "what equation does the universe minimise?"

---

## Connections

- **Prerequisite:** [[Differentiation]] — finding critical points needs the derivative
- **Prerequisite:** [[Stationary Points]] — the *what* of "$f' = 0$"; this card is the *what next*
- **Prerequisite:** [[Chain Rule]] — most word problems require the chain rule when expressing the objective in one variable
- **Sibling:** [[Connected Rates of Change]] — same chain-rule machinery applied to *time* derivatives instead of optimisation
- **Uses:** [[Extreme Value Theorem]] — the closed-interval method *cashes* EVT's guarantee that max/min exist on a continuous-on-closed-interval function
- **Application:** *physics — principle of least action* — the trajectory a particle takes is the one that extremises a quantity called *action*; calculus of variations
- **Application:** *economics* — marginal analysis (set marginal cost = marginal revenue), utility maximisation under budget constraint
- **Application:** *machine learning* — every neural network is trained by minimising a loss function via gradient descent; convexity, local minima, saddle points all matter
- **Beyond high school:** *Lagrange multipliers* (constrained), *KKT conditions* (inequality constraints), *convex optimisation* (interior-point methods), *calculus of variations* (Euler-Lagrange equation)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $f'(x)$ | `f'(x)` | First derivative |
| $f''(x)$ | `f''(x)` | Second derivative — Lagrange notation |
| $\dfrac{d^2 y}{dx^2}$ | `\dfrac{d^2 y}{dx^2}` | Second derivative — Leibniz notation |
| $\smile$ | `\smile` | Concave-up symbol — minimum |
| $\frown$ | `\frown` | Concave-down symbol — maximum |
| $\nabla f = \lambda \nabla g$ | `\nabla f = \lambda \nabla g` | Lagrange multiplier condition |
| $\dfrac{a+b}{2} \ge \sqrt{ab}$ | `\dfrac{a+b}{2} \ge \sqrt{ab}` | AM-GM inequality (two variables) |
