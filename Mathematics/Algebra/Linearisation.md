---
chinese: 线性化 (xiànxìnghuà)
prerequisites:
  - "[[Logarithms]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Exponential Growth and Decay]]"
  - "[[Direct and Inverse Proportion (Vocab)]]"
  - "[[Graphs of Functions]]"
  - "[[Proportion (Vocab)]]"
leads_to:
  - "[[Differential Equations]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE-extension
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/AP
  - syllabus/0606-7-4
  - type/deep
  - type/technique
  - type/application
  - notation/log-log
  - notation/semi-log
  - misconception/log-of-A-vs-A
  - misconception/gradient-in-original-units
---

# Linearisation 线性化

## Definition

**Linearisation** is the trick of changing variables so that a non-linear relationship becomes a *straight line*. The most common change of variables — and the only one Cambridge 0606 asks for — is **taking logarithms of one or both axes**.

If your data fits a power law

$$y = A x^n,$$

then plotting $\log y$ against $\log x$ gives a **straight line** of gradient $n$ and $y$-intercept $\log A$.

If your data fits an exponential

$$y = A b^x,$$

then plotting $\log y$ against $x$ gives a **straight line** of gradient $\log b$ and $y$-intercept $\log A$.

Why is this useful? Because the human eye is *very good* at spotting straight lines and *very bad* at spotting whether a curve is a quadratic, a cubic, or a power-of-2.7 — they all look like "some upward bend." Once the data is on a straight line, you can read off the constants with a ruler. This is exactly how 19th- and 20th-century scientists discovered every empirical power law in physics, chemistry, and biology — long before nonlinear regression existed in any computer.

### 中文锚点

**线性化 (xiànxìnghuà)** = 把一个非线性关系，通过**取对数**（或别的代换），变成**直线**。

两个标准型：

| 原始模型 | 取对数 | 直线方程 | $x$ 轴 | $y$ 轴 | 斜率 | 截距 |
|---|---|---|---|---|---|---|
| 幂函数 $y = Ax^n$ | $\lg y = \lg A + n \lg x$ | $Y = c + n X$ | $\lg x$ | $\lg y$ | $n$ | $\lg A$ |
| 指数函数 $y = Ab^x$ | $\lg y = \lg A + x \lg b$ | $Y = c + (\lg b) X$ | $x$ | $\lg y$ | $\lg b$ | $\lg A$ |

考试套路：给一组实验数据，要求**判断是哪种模型**（$y = Ax^n$ 还是 $y = Ab^x$？），然后**画出合适的对数坐标图**，再**从图上斜率和截距求 $A, n$ 或 $A, b$**。

---

## Why It Works — the algebra

### Power law $y = Ax^n$

This is three small steps, each one a single move you already know.

**Step 1 — take $\log$ of both sides.** $y$ and $Ax^n$ are equal numbers, so $\log y$ and $\log(Ax^n)$ are equal too (applying the same function to equal numbers keeps them equal). Pick whatever base — $10$, $e$, anything; the algebra is identical:

$$\log y = \log\bigl(A x^n\bigr).$$

**Step 2 — break the right side using the product law.** $\log$ of a product splits into a sum, $\log(P \cdot Q) = \log P + \log Q$ (see [[Logarithms]]):

$$\log y = \log A + \log\bigl(x^n\bigr).$$

**Step 3 — pull the exponent out using the power law.** $\log(x^n) = n \log x$ (the exponent on the inside becomes a multiplier on the outside):

$$\log y = \log A + n \log x.$$

That's the full derivation. Three lines.

**Now stare at the result next to $y = mx + c$:**

$$\underbrace{\log y}_{\;Y\;} \;=\; \underbrace{\log A}_{\;c\;} \;+\; \underbrace{n}_{\;m\;}\cdot \underbrace{\log x}_{\;X\;}.$$

Let $Y = \log y$, $X = \log x$, $c = \log A$. Then $\log A$ is *just a number* (some constant set by $A$), and $n$ is *just a number* (the exponent of the original power). The equation reads $Y = mX + c$ — literally the equation of a straight line. The shape is forced; there is no other way for the points to land.

**What "plot $\log y$ against $\log x$" means at the per-point level.** For each data pair $(x, y)$, compute *new* coordinates $X = \log x$ and $Y = \log y$, and put a dot at $(X, Y)$ on graph paper labelled "$\log x$ horizontal, $\log y$ vertical." The original data lay on a curve $y = Ax^n$; the *transformed* dots line up on $Y = c + mX$. Same data, different coordinates, totally different shape.

> [!info] Numerical sanity check — see the line emerge
> Take $y = 2x^3$ (so $A = 2$, $n = 3$) and three points:
>
> | $x$ | $y = 2x^3$ | $\lg x$ | $\lg y$ |
> |---|---|---|---|
> | $1$ | $2$ | $0$ | $0.301$ |
> | $10$ | $2{,}000$ | $1$ | $3.301$ |
> | $100$ | $2{,}000{,}000$ | $2$ | $6.301$ |
>
> In the raw $(x, y)$ columns the numbers explode — $1, 10, 100$ on the left, $2, 2{,}000, 2{,}000{,}000$ on the right. No straight line on Earth could fit that. But the $(\lg x, \lg y)$ columns are equally spaced: $\lg x$ goes up by $1$ each row, $\lg y$ goes up by *exactly* $3$ each row. The gradient is $\Delta(\lg y) / \Delta(\lg x) = 3/1 = 3 = n$ ✓, and the intercept (the $\lg y$ value when $\lg x = 0$) is $0.301 = \lg A$ ✓.

**Read off the constants.** Plot $Y$ against $X$, draw the line, then $n$ is the gradient and $\log A$ is the $y$-intercept. Recover $A = 10^{\log A}$ at the end.

> [!info] The deep reason this works — logs translate ratios into differences
> A power law has the property that *multiplying* $x$ by some factor *multiplies* $y$ by a related factor: if you replace $x$ with $kx$, then $y$ becomes $A(kx)^n = k^n \cdot Ax^n = k^n y$. So multiplicative changes in $x$ become multiplicative changes in $y$.
>
> Logarithms turn multiplications into additions ($\log(ab) = \log a + \log b$). So in log coordinates, "multiplicative-in-$x$ → multiplicative-in-$y$" becomes "additive-in-$\log x$ → additive-in-$\log y$" — and "constant additive change in $Y$ for constant additive change in $X$" is *the definition of a straight line*. The log is a translator that converts the language of *ratios* into the language of *differences*, and straight lines are exactly what differences look like.

### Exponential $y = Ab^x$

Same three moves — but watch which side gets logged: only $y$, not $x$.

**Step 1 — log of both sides.**

$$\log y = \log\bigl(A b^x\bigr).$$

**Step 2 — product law.** $\log(A \cdot b^x) = \log A + \log(b^x)$:

$$\log y = \log A + \log\bigl(b^x\bigr).$$

**Step 3 — power law.** Here the *exponent* is $x$ itself (the variable!), and the *base* is the constant $b$. The power law $\log(b^x) = x \log b$ pulls $x$ out as a coefficient:

$$\log y = \log A + (\log b) \, x.$$

**Now compare to $y = mx + c$:**

$$\underbrace{\log y}_{\;Y\;} \;=\; \underbrace{\log A}_{\;c\;} \;+\; \underbrace{\log b}_{\;m\;} \cdot \underbrace{x}_{\;X\;}.$$

The crucial difference from the power-law case: $X = x$ here, *not* $\log x$. We only logged the $y$-axis. That's why this is called a **semi-log** plot — only one axis got the log treatment, because only one side of the equation needed a power law applied.

**Why is this a straight line?** Because once again, after relabelling, we have $Y = mX + c$ with $m = \log b$ and $c = \log A$ — both constants set by the model parameters. Plot $\log y$ on the vertical and $x$ on the horizontal, and the data lines up. Gradient $= \log b$ (recover $b = 10^{\log b}$); intercept $= \log A$ (recover $A = 10^{\log A}$).

> [!tip] Why power → log–log, exponential → semi-log
> The pattern is: **log the side(s) where the variable is in an exponent**. In $y = Ax^n$, the variable is $x$ inside an exponent, so logging the right side pulls $n$ out — but to make the resulting $\log x$ behave linearly we have to also use $\log x$ on the horizontal axis. In $y = Ab^x$, the variable is $x$ inside an exponent already (the exponent *is* $x$), so logging the right side pulls $x$ out as a clean linear term — no need to log the horizontal axis. One log on the vertical is enough.

### The names of the two coordinate systems

| Plot | English name | What it linearises |
|---|---|---|
| $\log y$ vs $\log x$ | **log–log plot** | power law $y = Ax^n$ |
| $\log y$ vs $x$ | **semi-log plot** (or "log-linear") | exponential $y = Ab^x$ |

A power law on linear–linear axes looks like a curving sweep. On log–log paper, it's a straight line. An exponential on linear–linear axes looks like a curving sweep. On semi-log paper, *that* one's a straight line. Each model has its own coordinate system that "straightens it out" — and the *converse* is also true: if your data straightens on log–log, it's a power law; if it straightens on semi-log, it's an exponential. The choice of axes is the diagnostic.

![[linearisation-loglog-semilog.svg]]

Above: top row is a power law $y = 1.3\,x^{1.5}$ — curved on linear axes (left), straight on log–log (right). Bottom row is an exponential $N = 5.0 \cdot 1.5^{t}$ — curved on linear axes (left), straight on semi-log (right). The gradient and intercept of each straight-line plot directly hand you $A$ and $n$ (or $A$ and $b$).

> [!info] Why this is the most exam-tested log application at A-Level
> Logarithms only show up on 0606 in three or four flavours: solve $a^x = b$, simplify with the log laws, and *this*. Linearisation is where the log laws actually *do work* — the product/power laws are what convert $\log(Ax^n)$ into $\log A + n \log x$. Every step of the technique is a one-line application of a law you already know. That's why it shows up year after year: it's the cleanest test of whether you understand what the laws *for*.

---

## The Workflow — fitting a model to data

You're given a table of data and asked: "find $A$ and $n$." The recipe:

1. **Decide which model is being assumed.** The question usually tells you (e.g. "the relationship $y = Ax^n$ holds…"). If not, try plotting both ways and see which one straightens.
2. **Compute the log column(s).** For $y = Ax^n$: a column of $\log x$ and a column of $\log y$. For $y = Ab^x$: keep $x$ as is, compute a column of $\log y$.
3. **Plot the linearised data.** $\log y$ on the vertical, $\log x$ (or $x$) on the horizontal. Use the scale that fits the range — sometimes $\log y$ ranges from $0.3$ to $1.8$, sometimes from $-2$ to $5$.
4. **Draw the line of best fit.** By eye is fine for 0606. The line should pass close to all the points, with roughly equal spread above and below.
5. **Read off gradient and intercept.** Use the standard $\dfrac{\Delta Y}{\Delta X}$ formula on two well-separated points *on your line of best fit* (not raw data points!). Read the intercept where the line meets $X = 0$.
6. **Translate back to original constants.** Gradient $\to n$ (or $\log b \to b = 10^{\text{gradient}}$). Intercept $\to \log A \to A = 10^{\text{intercept}}$.

> [!tip] Use two points *on your line*, not from the data
> A common 0606 mark-loss: students compute the gradient between two raw data points instead of two points on the best-fit line. The data is noisy — the best-fit line averages out the noise, which is *exactly* what you want. Pick two points on the line itself (well-separated for accuracy) and compute the gradient from those.

---

## Worked Examples

### Example 1 — Power law (0606-style)

> The variables $x$ and $y$ are related by $y = Ax^n$, where $A$ and $n$ are constants. Some experimental values are recorded in the table below. By plotting a suitable straight-line graph, find the values of $A$ and $n$ correct to 2 significant figures.

| $x$ | $2$ | $5$ | $10$ | $20$ | $50$ |
|---|---|---|---|---|---|
| $y$ | $3.6$ | $14.1$ | $40.0$ | $113.1$ | $447.2$ |

**Step 1 — model.** Given $y = Ax^n$ → plot $\log y$ against $\log x$.

**Step 2 — log table.** (Using $\lg = \log_{10}$.)

| $x$ | $\lg x$ | $y$ | $\lg y$ |
|---|---|---|---|
| $2$ | $0.301$ | $3.6$ | $0.556$ |
| $5$ | $0.699$ | $14.1$ | $1.149$ |
| $10$ | $1.000$ | $40.0$ | $1.602$ |
| $20$ | $1.301$ | $113.1$ | $2.054$ |
| $50$ | $1.699$ | $447.2$ | $2.650$ |

**Step 3 — gradient.** Pick two well-separated points (rounding to read off a graph; here we use first and last for a clean computation):

$$
n = \frac{\lg y_5 - \lg y_1}{\lg x_5 - \lg x_1} = \frac{2.650 - 0.556}{1.699 - 0.301} = \frac{2.094}{1.398} \approx 1.50.
$$

So $n \approx \boxed{1.5}$.

**Step 4 — intercept.** The line passes through, say, $(\lg x, \lg y) = (1.000, 1.602)$. Substitute into $\lg y = \lg A + n \lg x$:

$$
1.602 = \lg A + (1.5)(1.000) \implies \lg A = 0.102 \implies A = 10^{0.102} \approx 1.27.
$$

So $A \approx \boxed{1.3}$.

**Final answer.** $y \approx 1.3 \, x^{1.5}$. (Indeed: $1.3 \cdot 10^{1.5} = 1.3 \cdot 31.62 \approx 41.1$, very close to the observed $40.0$. ✓)

> [!info] Why this $A$ and $n$ are *insightful*, not just numbers
> A power $n = 1.5 = 3/2$ usually means a square-root times a linear factor — common in physics: kinetic energy at constant momentum scales as $v^{3/2}$ in some wave systems; Kepler's third law gives orbital period $T \propto a^{3/2}$ where $a$ is semi-major axis. When linearisation hands you $n = 3/2$ or $n = 2$ or $n = -1$, that's a *signature* — the underlying physics is telling you something about the system's geometry. Half-integer exponents almost always indicate "energy related to amplitude squared" or "geometric mean of two scales."

### Example 2 — Exponential (0606-style)

> A bacterial colony grows according to $N = A b^t$, where $t$ is time in hours and $N$ is the count in millions. Measurements are recorded in the table below. Find $A$ and $b$ correct to 2 significant figures.

| $t$ (h) | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $N$ | $5.0$ | $7.5$ | $11.3$ | $16.9$ | $25.3$ |

**Step 1 — model.** $N = A b^t$ → plot $\lg N$ against $t$ (semi-log).

**Step 2 — log table.**

| $t$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $\lg N$ | $0.699$ | $0.875$ | $1.053$ | $1.228$ | $1.403$ |

**Step 3 — gradient = $\lg b$.**

$$
\lg b = \frac{\lg N_5 - \lg N_1}{t_5 - t_1} = \frac{1.403 - 0.699}{4 - 0} = \frac{0.704}{4} = 0.176.
$$

So $b = 10^{0.176} \approx \boxed{1.5}$.

**Step 4 — intercept = $\lg A$.** At $t = 0$: $\lg N = 0.699$, so $\lg A = 0.699$, giving $A = 10^{0.699} \approx \boxed{5.0}$.

**Final answer.** $N \approx 5.0 \cdot (1.5)^t$. The colony multiplies by $1.5$ every hour, doubling every $\dfrac{\ln 2}{\ln 1.5} \approx 1.71$ hours.

### Example 3 — Which form? (the diagnostic)

If the question doesn't tell you which model holds, the test is simple: plot both linearisations, see which one is straight.

**Suppose the same data was $(x, y) = (1, 2), (2, 4), (3, 8), (4, 16), (5, 32)$.**

- Log–log: $\lg x = 0, 0.30, 0.48, 0.60, 0.70$; $\lg y = 0.30, 0.60, 0.90, 1.20, 1.51$. The points are *not* equally spaced in $\lg x$, but they are equally spaced in $\lg y$ — the points curve upward on log–log paper. **Not** a power law.
- Semi-log: $x = 1, 2, 3, 4, 5$ (equally spaced); $\lg y = 0.30, 0.60, 0.90, 1.20, 1.51$ (almost equally spaced). The points are very close to a straight line. **Exponential.**

(In fact the data is exactly $y = 2^x$, which is $A = 1, b = 2$. The semi-log slope is $\lg 2 \approx 0.301$, perfectly matching what we read off.)

**Lesson.** If neither linearisation works, the model is something else (polynomial of degree $> 1$ but not a clean power, logistic, etc.). For 0606, the question always picks one of the two standard models for you.

---

## Beyond Logs — other linearisations (beyond syllabus)

Logs aren't the only change of variables that linearises. Three others worth knowing for A-Level / IB / AP:

| Model | Substitute | Linear in |
|---|---|---|
| $y = a + \dfrac{b}{x}$ | $X = \dfrac{1}{x}$ | $(X, y)$ |
| $\dfrac{1}{y} = a + b x$ | $Y = \dfrac{1}{y}$ | $(x, Y)$ |
| $y^2 = a + bx$ | $Y = y^2$ | $(x, Y)$ |
| $y = ax^n + b$ (with $n$ given) | $X = x^n$ | $(X, y)$ |

The pattern is *always*: pick a substitution that turns the model into "(linear function of new variables) = constant + constant × (other new variable)." Then plot in the new variables. The linearisation trick generalises to *any* model where one transformation makes things linear.

> [!info] Linearisation in physics — three places it shows up
> 1. **Hubble's law.** Distance vs recession velocity of galaxies on a *linear* plot looks scattered; on a log–log plot you can see two regimes ("nearby" linear, "far" with cosmological corrections), and the slope hands you the Hubble constant.
> 2. **Allometric scaling in biology.** Animal metabolic rate vs body mass: on log–log paper the data falls on a line with slope $3/4$ (Kleiber's law). Without logs, an elephant and a mouse couldn't even share the same chart.
> 3. **Lens equation.** $\dfrac{1}{f} = \dfrac{1}{u} + \dfrac{1}{v}$ — already linear in the *reciprocals*. Plot $1/v$ against $1/u$ and read off $1/f$ as the intercept. This is a homework standard in optics labs.
>
> Whenever an empirical relationship has a *power*, an *exponential*, or a *reciprocal* in it, linearisation is the first move. Computers have made nonlinear regression cheap, but the *insight* — "this is a power law of exponent $3/2$" — comes most clearly from a straight line.

---

## Common Mistakes

1. **Reporting $\log A$ as $A$.** The intercept is $\log A$, *not* $A$ itself. Always exponentiate at the end: $A = 10^{\text{intercept}}$ (if using base $10$) or $A = e^{\text{intercept}}$ (if using $\ln$).
2. **Computing gradient from raw $(x, y)$ instead of $(\log x, \log y)$.** The whole point is that the *transformed* data is on a line. Gradients on the original plot will vary across the data — they're not what the question is asking for.
3. **Mixing $\lg$ and $\ln$ mid-problem.** Pick one and stick with it. If you take $\lg y$ at the start, every "log" in the working is $\lg$ until the end. Switching halfway turns gradients and intercepts into garbage (because $\ln 10 \approx 2.303$, the conversion factor).
4. **Assuming the wrong model.** If the question doesn't specify, *check* — both linearisations take five seconds, and only one will be straight.
5. **Reading gradient from raw data points instead of from the line of best fit.** Use *line* points (well-separated), not data points.
6. **Forgetting the $y$-intercept matters.** The gradient gives you $n$ (or $\log b$); the intercept gives you $A$. Both are needed to specify the model. Common loss-of-marks: students nail the gradient but never compute $A$.

---

## Exam Notes

### Cambridge 0606

**Syllabus ref:** §7.4. The format is consistent year after year:

- Question gives a model: "$y = Ax^n$" or "$y = Ab^x$" (occasionally a variant like $y = a + b/x$).
- Question gives a small data table (typically 4–6 rows).
- Question asks for: a suitable straight-line graph, the values of the constants, and sometimes a prediction at an unseen $x$.
- Marks are typically allocated: 1–2 for the log table, 2–3 for the plot/best-fit line, 1 for the gradient, 1 for the intercept, 1–2 for the constants $A$ and $n$ (or $A$ and $b$).

> [!tip] If the model is given, you don't need to "discover" which logs to take
> Cambridge always tells you the model. Reading "the relationship $y = Ax^n$ holds" → take $\lg$ of both sides → plot $\lg y$ vs $\lg x$. Reading "the model is $y = Ab^x$" → plot $\lg y$ vs $x$. The model is the road sign; just follow it.

> [!warning] Use enough decimal places in the log column
> 0606 markschemes often want $\lg$ values to *three* decimal places. Two isn't enough — small differences in $\lg y$ feed into the gradient with high leverage, and rounding to $0.55$ instead of $0.556$ can shift the gradient by $5\%$ or more. Calculate to four, report to three.

### A-Level / 9709

A-Level extends linearisation to:

- **Other transformations** (the table above) — $1/x$, $y^2$, etc.
- **Differential equation modelling** — given $\dfrac{dy}{dt} = ky$, the solution is exponential, and fitting $y$ vs $t$ data via log linearisation extracts $k$.
- **Error analysis** — the spread of linearised data quantifies how good the model is. Log axes change *what* error means (relative vs absolute) — a fact that becomes important in physics labs.

### IB AA / AP

IB AA SL covers the technique under "Modelling." HL extends to nonlinear regression (with calculator support), but the linearisation by logs remains the conceptual foundation.

AP Calculus and AP Statistics both make linearisation explicit. AP Stats has a whole unit on transformations to achieve linearity — log–log for power, semi-log for exponential, plus the residual analysis to confirm the choice.

---

## Connections

- **Prerequisite:** [[Logarithms]] — every step of the algebra is a log law (product, power); without solid logs the technique is opaque
- **Prerequisite:** [[Equation of a Straight Line (Vocab)]] — the *output* of linearisation is $Y = c + mX$, which is just $y = mx + c$ in different letters
- **Prerequisite:** [[Exponential Growth and Decay]] — the $y = Ab^x$ model on which semi-log plots act
- **Prerequisite:** [[Direct and Inverse Proportion (Vocab)]] — power laws $y = Ax^n$ generalise direct ($n=1$) and inverse ($n=-1$) proportion
- **Application:** *physics labs* — fitting $T = 2\pi\sqrt{\ell/g}$ (pendulum) by linearising as $T^2 = 4\pi^2 \ell / g$ and plotting $T^2$ vs $\ell$ to find $g$ from the gradient
- **Application:** *biology* — Kleiber's law (metabolic rate $\propto \text{mass}^{3/4}$), allometry, dose-response curves
- **Application:** *economics* — Cobb-Douglas production functions $Q = A K^\alpha L^\beta$ are linearised by logs to estimate $\alpha$ and $\beta$ from data
- **Beyond high school:** *log–log spectra* in signal processing, *Bode plots* in control theory, *power-law distributions* (Pareto, Zipf) in network science — all rely on the same trick: a straight line on log axes is the signature of an underlying power

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\lg x$ | `\lg x` | Common log, base $10$ — Chinese / European convention |
| $\log x$ | `\log x` | Default base $10$ in Cambridge convention |
| $\ln x$ | `\ln x` | Natural log, base $e$ |
| $y = Ax^n$ | `y = Ax^n` | Power law model |
| $y = Ab^x$ | `y = Ab^x` | Exponential model |
| $\lg y = \lg A + n \lg x$ | `\lg y = \lg A + n \lg x` | Linearised power law |
| $\lg y = \lg A + x \lg b$ | `\lg y = \lg A + x \lg b` | Linearised exponential |
| $Y = c + mX$ | `Y = c + mX` | Generic linear form after substitution |
