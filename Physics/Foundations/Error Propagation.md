---
chinese: 误差传播 (wùchā chuánbō)
prerequisites:
  - "[[Chain Rule]]"
  - "[[Product Rule]]"
  - "[[Power Rule]]"
  - "[[Logarithms]]"
  - "[[Differentiation]]"
  - "[[Upper and Lower Bounds]]"
  - "[[Physical Quantities and Units]]"
  - "[[Calibration of Instruments]]"
leads_to:
  - "[[Significant Figures]]"
  - "[[Linearisation for Lab Analysis]]"
  - "[[Combination of Uncertainties]]"
  - "[[Stories/The 1919 Eclipse]]"
  - "[[Repeated Measurements]]"
  - "[[The 1919 Eclipse]]"
teach_together:
  - "[[Accuracy vs Precision]]"
tags:
  - subject/physics
  - subject/mathematics
  - domain/experimental-physics
  - domain/measurement
  - domain/calculus
  - level/A-Level
  - level/IB
  - level/AP
  - level/IGCSE
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-Mechanics
  - curriculum/AP-Physics-C-EM
  - syllabus/9702-1-3
  - syllabus/0625-P5
  - syllabus/IB-Physics-PRAC-2
  - syllabus/AP-Physics-1-SP-1
  - type/deep
  - type/theorem
  - type/proof
  - notation/Delta
  - notation/derivative
  - notation/ln
  - misconception/percentage-equals-absolute
  - misconception/errors-subtract-when-quantities-subtract
  - misconception/significant-figures-are-uncertainty
---

# Error Propagation 误差传播

## Hunter trace — why does a 5% radius give a 15% volume?

You measure a steel ball-bearing with vernier calipers. The radius reads $r = 6.00~\text{mm}$, with an uncertainty of $\pm 0.30~\text{mm}$ — about **5%**. You compute the volume,

$$V = \tfrac{4}{3}\pi r^3 \approx 904~\text{mm}^3.$$

How accurately do you know the volume? A first instinct says "also 5%, the cube is just arithmetic." A better instinct says "more, because cubing amplifies." A textbook tells you the answer is **15%**, exactly three times the uncertainty in $r$. Why three? Why exactly?

That "three" is no coincidence — it is the exponent in $r^3$ wearing a lab coat. Every rule on a Physics error-propagation sheet — *absolute errors add for sums, percentage errors add for products, exponent multiplies percentage for powers* — is one application of the **chain rule on the logarithm**. One trick. One sentence. The whole sheet falls out.

This card builds that one trick, then watches the sheet fall out.

## Definition

When a quantity $z$ is computed from measured quantities $x_1, x_2, \dots$ — each carrying its own uncertainty $\Delta x_i$ — the uncertainty $\Delta z$ that propagates into $z$ is set by the function $z = f(x_1, x_2, \dots)$ and the input uncertainties. **Error propagation** is the procedure for getting $\Delta z$ from the $\Delta x_i$.

In all of this, "uncertainty" and "error" are used interchangeably for the *spread* of a measurement — not for "mistake." Random measurement spread, instrumental limit, half the smallest division on a ruler. The propagation rules are agnostic about the source.

### 中文锚点

**误差传播 (wùchā chuánbō)**：测量量 $x$ 有不确定度 $\Delta x$，由它算出的量 $z = f(x)$ 也有不确定度 $\Delta z$；求出 $\Delta z$ 的过程就叫误差传播。

物理实验里有三条 *表面上* 看起来不相关的规则：

| 运算 | 误差规则 | 中文术语 |
|---|---|---|
| $z = x \pm y$ | **绝对误差相加**：$\Delta z = \Delta x + \Delta y$ | 加减用绝对误差 |
| $z = xy$ 或 $z = x/y$ | **百分比误差相加**：$\dfrac{\Delta z}{z} = \dfrac{\Delta x}{x} + \dfrac{\Delta y}{y}$ | 乘除用百分比误差 |
| $z = x^n$ | **指数乘以百分比误差**：$\dfrac{\Delta z}{z} = \lvert n \rvert \dfrac{\Delta x}{x}$ | 幂次方相对误差放大 $n$ 倍 |

中国高中物理课本通常只列这三条规则，不解释为什么。**英文 A-Level / IB / AP 物理也只列这三条规则**。这张卡的目标就是说清楚：三条规则不是三件事，是**对数微分**这一件事的三个面。

A common misreading — even by exam-savvy students — is that "subtraction subtracts errors." It doesn't. $z = x - y$ obeys $\Delta z = \Delta x + \Delta y$ (absolute errors *add*), because errors are unsigned worst-case bounds and the subtraction could conspire either way. More on this in the Misconceptions section.

---

## The master rule — first-order Taylor

If $z$ depends on a single measured quantity $x$ via $z = f(x)$, then a small change $\Delta x$ in $x$ produces a small change in $z$ given by the linear approximation:

$$\boxed{\; \Delta z \approx \lvert f'(x) \rvert \, \Delta x \;}$$

This is just $\dfrac{dz}{dx}$ pretending to be $\dfrac{\Delta z}{\Delta x}$ — the [[Chain Rule]] running through the chain $\Delta x \to \Delta z$. It is exact in the limit $\Delta x \to 0$ and an excellent approximation whenever $\Delta x$ is small compared with $x$ — which is the regime experimental physics lives in (we typically want 1–10% uncertainties, not 100%).

For a multivariable $z = f(x_1, x_2, \dots, x_n)$, the same idea gives

$$\Delta z \approx \sum_{i=1}^{n} \left\lvert \dfrac{\partial f}{\partial x_i} \right\rvert \Delta x_i,$$

with partial derivatives in place of the ordinary derivative. The absolute-value bars are doing serious work: each input could push $z$ up or down, and the worst-case bound takes them all in the *same* direction. **This is why errors add and never cancel.**

> [!tip] Two conventions for combining errors
> The "worst-case bound" above is the version Cambridge 9702 and IB Physics assume by default at school level — uncertainties combine by **addition** of absolute values.
>
> In real lab work and in university, when errors are random and *independent*, they combine **in quadrature** ($\Delta z = \sqrt{\sum (\partial f / \partial x_i)^2 (\Delta x_i)^2}$). Independent random errors partly cancel, so the quadrature sum is smaller than the worst-case sum.
>
> Exam expectation through 9702 / IB Physics / AP: use the worst-case (add absolutes). Quadrature is a beyond-syllabus refinement. The *rules* below — sum, product, power — have the same algebraic form in both conventions; only the way you ultimately combine the contributions differs.

That single line $\Delta z \approx \lvert f'(x) \rvert \, \Delta x$ is **the master rule**. The three propagation rules are special cases. Let's derive them.

---

## Rule 1 — Sum / difference: absolute errors add

If $z = x + y$ or $z = x - y$, then $\partial z / \partial x = \pm 1$ and $\partial z / \partial y = \pm 1$, so taking absolute values:

$$\boxed{\; \Delta z = \Delta x + \Delta y \;} \qquad \text{(for } z = x \pm y\text{)}$$

**Absolute errors add — in both cases.** The minus sign in $z = x - y$ does not propagate to the error: $y$ could have been measured too high *or* too low, and so could $x$, so in the worst case the difference $x - y$ is wrong by the sum of both spreads.

> [!warning] Sums and differences are democratic
> $z = 100.0 \pm 0.2$ minus $y = 99.5 \pm 0.3$ gives $z - y = 0.5 \pm 0.5$. The absolute uncertainty is tiny, but as a **percentage** it is 100% — the difference of two nearly-equal numbers loses precision catastrophically. This is the lab origin of "**catastrophic cancellation**" in [[Numerical Precision]] — and the reason Physics avoids designing measurements that need a small difference of two large numbers (subtract column heights of a manometer ✗, measure the height difference directly ✓).

### When this is the only rule you need

Anything purely additive: total length = sum of segment lengths; total mass = container + contents; current at a node ($I_1 = I_2 + I_3$); displacement = final position $-$ initial position.

---

## Rule 2 — Product / quotient: percentage errors add

For $z = xy$, the master rule with partial derivatives gives

$$\Delta z \approx y\,\Delta x + x\,\Delta y.$$

Divide both sides by $z = xy$:

$$\dfrac{\Delta z}{z} \approx \dfrac{y\,\Delta x}{xy} + \dfrac{x\,\Delta y}{xy} = \dfrac{\Delta x}{x} + \dfrac{\Delta y}{y}.$$

So:

$$\boxed{\; \dfrac{\Delta z}{z} = \dfrac{\Delta x}{x} + \dfrac{\Delta y}{y} \;} \qquad \text{(for } z = xy \text{ or } z = x/y\text{)}$$

**Percentage errors add.** The same result holds for quotients $z = x/y$: identical algebra, with the worst-case sign convention again forcing the signs to align. The geometric picture is the [[Product Rule]] rectangle — the right strip is the "$y$ contribution," the top strip is the "$x$ contribution," and the corner $\Delta x \, \Delta y$ vanishes to second order (which is exactly the "$\Delta z$ is small" hypothesis underneath the whole framework).

### The shortcut: logarithmic differentiation

There is a slicker route to the same answer, and it is the route that *generalises* to powers and to any function at all. Take logs of both sides of $z = xy$:

$$\ln z = \ln x + \ln y.$$

Differentiate. Using $\dfrac{d}{du}(\ln u) = \dfrac{1}{u}$ on each term (the chain rule on $\ln$ — see [[Logarithms]] §"Why $(\ln x)' = 1/x$"):

$$\dfrac{dz}{z} = \dfrac{dx}{x} + \dfrac{dy}{y}.$$

Replace $d$ with $\Delta$ (the small-change interpretation) and take absolute values:

$$\dfrac{\Delta z}{z} = \dfrac{\Delta x}{x} + \dfrac{\Delta y}{y}.$$

For a quotient $z = x/y$, the only change is one minus sign in $\ln z = \ln x - \ln y$, which the absolute-value convention promptly erases. **The rule is the same.**

The deeper reason logarithms are perfect for this job: **logs turn products into sums.** Multiplication of two uncertain quantities is hard; addition of two uncertain quantities is easy (Rule 1). The log moves us from the hard world to the easy world, we apply the easy rule, and the answer comes back as a *percentage* error because $d(\ln z) = dz/z$ is by definition the fractional change in $z$.

---

## Rule 3 — Power: exponent multiplies percentage error

For $z = x^n$, the same logarithmic trick:

$$\ln z = n \ln x \quad\Longrightarrow\quad \dfrac{dz}{z} = n \, \dfrac{dx}{x}.$$

Taking absolute values:

$$\boxed{\; \dfrac{\Delta z}{z} = \lvert n \rvert \, \dfrac{\Delta x}{x} \;} \qquad \text{(for } z = x^n \text{)}$$

**The exponent multiplies the percentage error.** This is the resolution of the hunter trace: $V = \tfrac{4}{3}\pi r^3$, so $\Delta V / V = 3 \, \Delta r / r$. Five percent in $r$ gives **fifteen percent** in $V$. The "three" is the exponent. Always.

![[error-propagation-amplification.svg]]

The rule works for any exponent — integer, fractional, negative:

- $V \propto r^3$: 5% in $r$ → 15% in $V$ (cube)
- $A \propto r^2$: 5% in $r$ → 10% in $A$ (square)
- $T \propto L^{1/2}$ for a pendulum: 4% in $L$ → 2% in $T$ (square root **halves** the percentage)
- $E \propto v^2$: 5% in $v$ → 10% in $E$ (kinetic energy)
- $R \propto L^{-1}$: 5% in $L$ → 5% in $R$ (reciprocals do not change percentage, the sign flips but absolute value bars erase it)

The *fractional* exponents earn special attention: $\lvert n \rvert < 1$ means the percentage error **shrinks**. Measuring period to get gravitational acceleration ($g = 4\pi^2 L / T^2$, with $T$ appearing squared in the denominator, so $\Delta g / g = \Delta L / L + 2\,\Delta T / T$) is one of the few experiments where time, the easy thing to measure precisely, also enjoys the shrinking advantage when re-arranged for $L$.

---

## The unifier — logarithmic differentiation

All three rules — sum/diff, product/quotient, power — come from one move. Even general functions like $z = \sin x$, $z = e^x$, or $z = \sqrt{1+x^2}$ propagate uncertainty via the same master rule $\Delta z \approx \lvert f'(x) \rvert \Delta x$. The "Physics error rules" are just the three special cases that the syllabus pre-computed for you.

> [!info] Why does the syllabus single these out?
> Real lab formulas overwhelmingly take the shape
>
> $$z = k\, x_1^{a_1}\, x_2^{a_2}\, \cdots \, x_n^{a_n}$$
>
> — a *constant times a product of powers* (sometimes called a **monomial** or a **power law**). Pendulum period $T = 2\pi (L/g)^{1/2}$, Coulomb force $F = k q_1 q_2 / r^2$, resistance $R = \rho L / A$, refractive index $n = \sin i / \sin r$ (well, almost — once you've measured the sines). For *any* such form, logarithmic differentiation gives one clean line:
>
> $$\dfrac{\Delta z}{z} = \lvert a_1 \rvert \dfrac{\Delta x_1}{x_1} + \lvert a_2 \rvert \dfrac{\Delta x_2}{x_2} + \cdots + \lvert a_n \rvert \dfrac{\Delta x_n}{x_n}.$$
>
> The constant $k$ disappears (its log is a constant, derivative zero — measurement-uncertainty-free quantities don't contribute). This *one formula* is the entire syllabus' worth of error-propagation rules. Memorise this one and you can throw the three-rule list away.

---

## Worked example 1 — Sphere volume (the hunter trace, resolved)

> A steel ball-bearing has radius $r = 6.00 \pm 0.30~\text{mm}$ measured with vernier calipers. Find the percentage uncertainty in its volume $V = \tfrac{4}{3}\pi r^3$.

**Step 1.** Take logs:

$$\ln V = \ln\left(\tfrac{4}{3}\pi\right) + 3 \ln r.$$

**Step 2.** Differentiate (the constant term drops out):

$$\dfrac{\Delta V}{V} = 3 \, \dfrac{\Delta r}{r}.$$

**Step 3.** Plug in:

$$\dfrac{\Delta r}{r} = \dfrac{0.30}{6.00} = 0.050 = 5\% \;\Longrightarrow\; \dfrac{\Delta V}{V} = 3 \times 5\% = 15\%.$$

The volume is $V \approx 904~\text{mm}^3 \pm 15\%$, i.e. $V = 904 \pm 136~\text{mm}^3$, which one would round and report as $V = (9.0 \pm 1.4) \times 10^2~\text{mm}^3$ — the uncertainty governs the precision of the digits we are allowed to print.

> [!warning] Why "three times" and not "thirty-three percent"?
> A common slip: "5% in $r$ means $r$ could be off by 5%, so $r^3$ could be off by $1.05^3 \approx 1.157$, which is 15.7%." Close, but **not** the first-order rule. The first-order rule says $\Delta V / V = 3 \times 5\% = 15.0\%$. The 0.7% discrepancy is the second-order Taylor term $\binom{3}{2}(\Delta r / r)^2 = 3 \times 0.0025 = 0.75\%$ — exactly the "$\Delta x \, \Delta y$ corner" of the product-rule rectangle that the linear approximation throws away.
>
> At 5% input error, the second-order term is ~1% — small. At 30% input error, it would be ~30% of the first-order answer — large. The linear rule degrades when uncertainties get big. Most Physics problems sit in the 1–10% regime where linearisation is fine.

---

## Worked example 2 — Pendulum period

> A simple pendulum's period is $T = 2\pi \sqrt{L/g}$. Suppose $L = 1.000 \pm 0.005~\text{m}$ (a 0.5% uncertainty from a metre rule with $\pm 5~\text{mm}$) and we treat $g$ as known. Find the percentage uncertainty in $T$.

**Take logs:**

$$\ln T = \ln(2\pi) + \tfrac{1}{2}\ln L - \tfrac{1}{2}\ln g.$$

**Differentiate:**

$$\dfrac{\Delta T}{T} = \tfrac{1}{2}\,\dfrac{\Delta L}{L} = \tfrac{1}{2} \times 0.5\% = 0.25\%.$$

A square root *halves* the percentage uncertainty. This is the same square-root advantage that makes the pendulum a precise timekeeper despite an unavoidable length uncertainty — and it works in both directions:

> [!info] Inverted — measuring $g$ from a pendulum
> Solve for $g$: $g = 4\pi^2 L / T^2$. Take logs and differentiate:
>
> $$\dfrac{\Delta g}{g} = \dfrac{\Delta L}{L} + 2\,\dfrac{\Delta T}{T}.$$
>
> The 2 is the punishment for $T$ being squared. $T$ is the *easier* quantity to measure precisely — a stopwatch reads to $\pm 0.01~\text{s}$, while a metre rule reads to $\pm 1~\text{mm}$ — so even with the factor of 2, the $T$ contribution can be kept tiny. A typical schoolroom result: $\Delta L / L \approx 0.5\%$ and $\Delta T / T \approx 0.1\%$ over 20 swings (recall that **timing $N$ swings then dividing by $N$ divides the random timing error by $N$** — see [[Repeated Measurements]]), so $\Delta g / g \approx 0.7\%$, easily good enough to confirm $g = 9.81~\text{m s}^{-2}$ to two significant figures.

---

## Common misconceptions

### 1. "Errors subtract when quantities subtract"

**The mistake:** $z = x - y$, so $\Delta z = \Delta x - \Delta y$.

**Why it's wrong:** The error bars $\Delta x$ and $\Delta y$ are *worst-case unsigned bounds*. The real measurement could be biased high or low in either direction. The worst case for $z = x - y$ is when $x$ is biased *high* by $\Delta x$ and $y$ is biased *low* by $\Delta y$ (or vice versa), making the difference off by $\Delta x + \Delta y$, not $\Delta x - \Delta y$.

**Fix:** Teach the rule as "errors **never cancel** when combined by the worst-case bound — they only ever add." The minus signs in $z = x - y$ live in the *value* of $z$, not in $\Delta z$.

### 2. "Percentage error and absolute error are interchangeable"

**The mistake:** Adding a percentage uncertainty to an absolute uncertainty, or applying Rule 1 (absolute add) to a quotient.

**Why it's wrong:** Rule 1 is for sums; Rule 2 is for products. They use *different units of error* — absolute (with the same units as the quantity) versus dimensionless ratio (percentage). Mixing them gives nonsense like "$5~\text{m} + 3\%$."

**Fix:** Before combining errors, always convert to the *form the rule expects*: sums → absolute; products → percentage. The first move in any error-propagation problem is "is the top-level operation a sum/difference (absolute) or a product/quotient/power (percentage)?"

### 3. "Significant figures *are* the uncertainty"

**The mistake:** "$L = 1.23~\text{m}$ means the uncertainty is in the third decimal place, so $\Delta L = 0.005~\text{m}$."

**Why it's wrong:** Significant-figure convention *encodes* a guess at uncertainty (~ $\pm$ half the last digit), but it is not a substitute for actually quoting $\Delta L$. The convention is too coarse — it cannot distinguish $\Delta L = 0.001~\text{m}$ from $\Delta L = 0.009~\text{m}$, both of which would be written "1.23 m." Worse, it lets a student avoid thinking about *where* the uncertainty comes from (instrument, technique, repeated reading spread).

**Fix:** Always quote a measurement as $\text{value} \pm \text{uncertainty}$ in the working — at least until reporting the final answer. Then, when rounding the final answer, *match the precision of the value to the precision of the uncertainty* (one or two significant figures of $\Delta$, value rounded to the same decimal place). See [[Significant Figures]] for the rounding convention.

### 4. "Cubing the error gives the error in the cube"

**The mistake:** "Volume = $r^3$, so $\Delta V = (\Delta r)^3$."

**Why it's wrong:** This conflates the *quantity* being cubed with the *error bar* being cubed. The error bar is small; cubing a small number makes it tiny. The actual relationship is linear: $\Delta V / V = 3 \, \Delta r / r$, which makes $\Delta V$ about three times the size of what naive proportionality would suggest, not a millionth.

**Fix:** Drive home the logarithmic-differentiation derivation. Once a student has *seen* the chain $\ln V = 3 \ln r \Rightarrow \Delta V / V = 3 \, \Delta r / r$, they cannot un-see the structure: **the exponent multiplies the percentage error, not the absolute error.**

---

## Exam Notes

### Cambridge 9702 (A-Level Physics)

§1.3 (As level, Paper 1 / 2). Examined every session. Expect:

- One MCQ checking whether you apply the right rule (sum vs product) for a given formula.
- A structured-question rider: "given $L = \dots \pm \dots$ and $T = \dots \pm \dots$, calculate the value of $g$ and its absolute uncertainty." Standard expected steps: (i) compute percentage uncertainties, (ii) combine using the propagation rules, (iii) convert back to absolute, (iv) round to match the uncertainty.
- Paper 3 (Practical) and Paper 5 (Planning and Analysis): error propagation features in *every* question. P5 especially asks for percentage uncertainty in gradient or intercept of a linearised graph — closely tied to [[Linearisation for Lab Analysis]].

Worst-case (absolute) addition is the expected convention. Quadrature is **not** required.

### IB Physics (2025 syllabus — first exams 2025)

PRAC.2 within the Tools strand: "Tools 1 — Experimental techniques." Tested via the Internal Assessment and via Paper 1B/2 short-answer questions on uncertainty.

IB's framing is slightly more explicit about random vs systematic, and IB asks students to consider *propagated absolute uncertainty in a graphical analysis* — slope and intercept uncertainties from max/min gradient lines, which is the closest a typical exam comes to a real statistical treatment.

Worst-case addition is the default; the IB Data Booklet does not list quadrature.

### AP Physics 1 / 2

Science Practice 1 ("Modelling and Representations") + Science Practice 4 ("Data Analysis"). The CED does not assign error propagation to a specific Unit number — it is woven through the lab requirement (≥25% of instructional time on hands-on labs).

AP Physics expects students to:
- Identify dominant sources of uncertainty in a measurement.
- Estimate fractional uncertainty in a derived quantity using the same rules as 9702 (the CED uses the same "absolute errors add for sums, fractional for products" framing).
- Comment on whether two values agree "within uncertainty."

AP Physics C (Mechanics and E&M) treats this as background — error analysis appears in the free-response lab questions but rarely as a standalone item. Calculus-based: students may use the master rule $\Delta z = \lvert f'(x) \rvert \Delta x$ directly rather than memorising the three special cases.

### Cambridge 0625 (IGCSE Physics)

Formal error propagation by the three rules is **not** a 0625 topic — it appears for the first time at AS level (9702 §1.3), so a student meeting this card at IGCSE is getting a head start rather than closing a row. What 0625 does ask, on the practical papers, is to record measurements to an appropriate degree of precision and to judge whether results agree **within ±10%**, the limit of experimental accuracy it fixes at this level. Flag it in the lesson: 0625 students need only Rule 1 (absolute errors add in sums) and the awareness that a derived quantity like a volume carries a larger fractional uncertainty than any of the lengths it came from.

---

## Connections

- **Parent:** [[Upper and Lower Bounds]] — the IGCSE-Maths formalisation of "what's the worst the answer could be." Error propagation is the calculus-flavoured version of bounds for continuous functions.
- **Master rule:** [[Chain Rule]] — the first-order Taylor identity $\Delta z \approx \lvert f'(x) \rvert \Delta x$ *is* the chain rule applied to the chain $\Delta x \to \Delta z$.
- **Engine for products:** [[Product Rule]] — the geometric origin of $\Delta(xy) \approx y\,\Delta x + x\,\Delta y$ is the product-rule rectangle.
- **Engine for powers:** [[Power Rule]] — the rule $\Delta z / z = n \, \Delta x / x$ for $z = x^n$ is a power-rule derivative divided through by $z$, equivalently the logarithmic-differentiation move.
- **Algebraic tool:** [[Logarithms]] — the reason the percentage-error rules look so clean is that $\dfrac{d(\ln z)}{dz} = \dfrac{1}{z}$, so $d(\ln z) = dz/z$ literally *is* the fractional change in $z$. Logs turn products into sums; that's why percentage errors add.
- **Sibling:** [[Accuracy vs Precision]] — error propagation handles *random* uncertainty; accuracy/precision frames where the uncertainty came from.
- **Extension:** [[Combination of Uncertainties]] — the quadrature convention and how it differs from worst-case addition; how the central-limit theorem rescues random errors.
- **Extension:** [[Linearisation for Lab Analysis]] — when the formula $z = f(x)$ is non-monomial, the standard lab move is to plot a linearised form and read uncertainty from the gradient's confidence band.
- **Reverse:** [[Repeated Measurements]] — averaging $N$ readings divides the random uncertainty by $\sqrt{N}$ (for independent errors). This is *reducing* uncertainty rather than propagating it, but the framework is the same.
- **Cross-domain (Calculus):** [[Tangents and Normals]] — the linear approximation $f(x + \Delta x) \approx f(x) + f'(x)\Delta x$ is the formal name for "first-order Taylor"; error propagation is its lab application.

- **For 9702 students:** [[MF19 Reference (9709)]] handles maths formulas; **9702 has no separate data booklet entry for error propagation rules** — the three rules must be memorised (or, better, derived on the fly from $\ln z$).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\Delta x$ | `\Delta x` | Absolute uncertainty in $x$ — same units as $x$. |
| $\dfrac{\Delta x}{x}$ | `\dfrac{\Delta x}{x}` | Fractional / percentage uncertainty — dimensionless. Multiply by 100 to read as a percent. |
| $\lvert n \rvert$ | `\lvert n \rvert` | Absolute value — must use `\lvert / \rvert` inside table cells (literal `|` breaks the row). |
| $f'(x)$ | `f'(x)` | Derivative for the master rule $\Delta z \approx \lvert f'(x) \rvert \Delta x$. |
| $\dfrac{\partial f}{\partial x_i}$ | `\dfrac{\partial f}{\partial x_i}` | Partial derivative — for the multivariable propagation formula. |
| $\ln z = \cdots$ | `\ln z` | Natural log for the logarithmic-differentiation trick. Always typeset $\ln$ with a backslash (`\ln`), not as the letters l-n. |
| $\propto$ | `\propto` | "Is proportional to" — for power-law scaling claims like $V \propto r^3$. |
| $\sqrt{\sum (\cdots)^2}$ | `\sqrt{\sum (\cdots)^2}` | Quadrature sum — beyond-syllabus for school but standard in university. |
