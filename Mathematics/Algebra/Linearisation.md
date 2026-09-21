---
chinese: 线性化 (xiànxìnghuà)
prerequisites:
  - "[[Logarithms]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Exponential Growth and Decay]]"
  - "[[Direct and Inverse Proportion (Vocab)]]"
  - "[[Graphs of Functions]]"
  - "[[Proportion (Vocab)]]"
  - "[[Planning an Experiment]]"
  - "[[Recording and Analysing Experimental Data]]"
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
  - syllabus/9709-2-2
  - syllabus/9709-3-2
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

**Linearisation** is the trick of changing variables so that a non-linear relationship becomes a *straight line*. The most common change of variables — though far from the only useful choice — is **taking logarithms of one or both axes**.

If your data fits a power law

$$y = A x^n,$$

then plotting $\log y$ against $\log x$ gives a **straight line** of gradient $n$ and $y$-intercept $\log A$.

If your data fits an exponential

$$y = A b^x,$$

then plotting $\log y$ against $x$ gives a **straight line** of gradient $\log b$ and $y$-intercept $\log A$.

Why is this useful? Because the human eye is *very good* at spotting straight lines and *very bad* at spotting whether a curve is a quadratic, a cubic, or a power-of-2.7 — they all look like "some upward bend." Once the data is on a straight line, you can read off the constants with a ruler. Straightened plots also make model parameters and departures from a proposed relationship easier to inspect.

### 中文锚点

**线性化**是换一套坐标，让原本弯曲的关系变成直线。关键不是机械地取对数，而是先把模型改写成“一个量 = 常数 × 另一个量 + 常数”，再让这两个量充当纵、横坐标。比如观察细菌数量：如果每小时都按同一倍数增长，原始曲线会越来越陡；对数量取对数后，每小时的增量就相同了，于是图像变成直线。对数把“相乘的倍数”变成了“相加的差值”。幂函数则要对两个坐标都取对数，这样直线的斜率正好就是原来的指数。换坐标也改变了斜率和截距的含义：截距若是 $\lg A$，还要算 $10^{\lg A}$ 才能找回 $A$。实验数据接近直线，是支持某个模型的证据；光凭这一点，既不能证明模型一定正确，也不能排除其他模型。

---

## Why It Works — the algebra

### Power law $y = Ax^n$

Assume $x>0$, $y>0$, $A>0$. Use one logarithm base $q>0$, $q\ne1$ throughout. For measured quantities, logs apply to numerical values in stated units (equivalently, ratios to reference units); changing units can change the intercept.

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

| $x$ | $y = 2x^3$ | $\lg x$ | $\lg y$ |
|---|---|---|---|
| $1$ | $2$ | $0$ | $0.301$ |
| $10$ | $2{,}000$ | $1$ | $3.301$ |
| $100$ | $2{,}000{,}000$ | $2$ | $6.301$ |

In the raw $(x, y)$ columns the numbers explode — $1, 10, 100$ on the left, $2, 2{,}000, 2{,}000{,}000$ on the right. No straight line on Earth could fit that. But the $(\lg x, \lg y)$ columns are equally spaced: $\lg x$ goes up by $1$ each row, $\lg y$ goes up by *exactly* $3$ each row. The gradient is $\Delta(\lg y) / \Delta(\lg x) = 3/1 = 3 = n$ ✓, and the intercept (the $\lg y$ value when $\lg x = 0$) is $0.301 = \lg A$ ✓.

**Read off the constants.** Plot $Y$ against $X$, draw the line, then $n$ is the gradient and $\log A$ is the $y$-intercept. For base 10, recover $A = 10^{\lg A}$; in base $q$, recover $A=q^c$.

> [!info] The deep reason this works — logs translate ratios into differences
> A power law has the property that *multiplying* $x$ by some factor *multiplies* $y$ by a related factor: if you replace $x$ with $kx$, then $y$ becomes $A(kx)^n = k^n \cdot Ax^n = k^n y$. So multiplicative changes in $x$ become multiplicative changes in $y$.
>
> Logarithms turn multiplications into additions ($\log(ab) = \log a + \log b$). So in log coordinates, "multiplicative-in-$x$ → multiplicative-in-$y$" becomes "additive-in-$\log x$ → additive-in-$\log y$" — and "constant additive change in $Y$ for constant additive change in $X$" is *the definition of a straight line*. The log is a translator that converts the language of *ratios* into the language of *differences*, and straight lines are exactly what differences look like.

### Exponential $y = Ab^x$

Assume $A>0$ and $b>0$; $b=1$ gives a constant function. The same three moves apply, but only the vertical coordinate is logged.

**Step 1 — log of both sides.**

$$\log y = \log\bigl(A b^x\bigr).$$

**Step 2 — product law.** $\log(A \cdot b^x) = \log A + \log(b^x)$:

$$\log y = \log A + \log\bigl(b^x\bigr).$$

**Step 3 — power law.** Here the *exponent* is $x$ itself (the variable!), and the *base* is the constant $b$. The power law $\log(b^x) = x \log b$ pulls $x$ out as a coefficient:

$$\log y = \log A + (\log b) \, x.$$

**Now compare to $y = mx + c$:**

$$\underbrace{\log y}_{\;Y\;} \;=\; \underbrace{\log A}_{\;c\;} \;+\; \underbrace{\log b}_{\;m\;} \cdot \underbrace{x}_{\;X\;}.$$

The crucial difference from the power-law case: $X = x$ here, *not* $\log x$. We only logged the $y$-axis. That's why this is called a **semi-log** plot — only one axis got the log treatment, because only one side of the equation needed a power law applied.

**Why is this a straight line?** Because once again, after relabelling, we have $Y = mX + c$ with $m = \log b$ and $c = \log A$ — both constants set by the model parameters. Plot $\log y$ on the vertical and $x$ on the horizontal, and the data lines up. Gradient $= \log_q b$ (recover $b=q^m$); intercept $= \log_q A$ (recover $A=q^c$).

> [!tip] Why power → log–log, exponential → semi-log
> **Derive the transformed equation, then name its variables.** For $y=Ax^n$, taking logs produces $n\log x$, so choose $X=\log x$. For $y=Ab^x$, it produces $x\log b$, so choose $X=x$. In both cases choose $Y=\log y$. The algebra selects the axes.

### The names of the two coordinate systems

| Plot | English name | What it linearises |
|---|---|---|
| $\log y$ vs $\log x$ | **log–log plot** | power law $y = Ax^n$ |
| $\log y$ vs $x$ | **semi-log plot** (or "log-linear") | exponential $y = Ab^x$ |

A general power law curves on linear axes (the constant and $n=1$ cases are exceptions), but becomes straight on log–log axes. A positive exponential becomes straight on semi-log axes. Exact straightness over an interval is equivalent to the corresponding model there; finite noisy data only support a model, and several models can look similar over a short range.

![[linearisation-loglog-semilog.svg]]

Above: top row is a power law $y = 1.3\,x^{1.5}$ — curved on linear axes (left), straight on log–log (right). Bottom row is an exponential $N = 5.0 \cdot 1.5^{t}$ — curved on linear axes (left), straight on semi-log (right). The gradient and intercept of each straight-line plot directly hand you $A$ and $n$ (or $A$ and $b$).

> [!info] Why the log laws matter
> Product and power laws turn multiplicative structure into an additive straight-line equation. Derive that equation first; the labels on the new axes then follow from it.

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

**Step 3 — gradient. Tool: $\Delta Y/\Delta X$.** These teaching data are rounded from an almost exact power law. An endpoint estimate illustrates the arithmetic below; with genuinely noisy experimental data, first fit a line and use two well-separated points on that line.

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
> An exponent can suggest a physical model: Kepler's third law gives $T\propto a^{3/2}$ for orbits around a fixed dominant mass, with $a$ the semi-major axis. But an exponent alone does not identify the mechanism. Units, assumptions and independent evidence must also agree.

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

**Lesson.** If neither linearisation works, the model is something else (polynomial of degree $> 1$ but not a clean power, logistic, etc.). Start from any supplied model; other transformations may be needed.

---

## Beyond Logs — other linearisations

Logs aren't the only change of variables that linearises. For example:

| Model | Substitute | Linear in |
|---|---|---|
| $y = a + \dfrac{b}{x}$ | $X = \dfrac{1}{x}$ | $(X, y)$ |
| $\dfrac{1}{y} = a + b x$ | $Y = \dfrac{1}{y}$ | $(x, Y)$ |
| $y^2 = a + bx$ | $Y = y^2$ | $(x, Y)$ |
| $y = ax^n + b$ (with $n$ given) | $X = x^n$ | $(X, y)$ |

The pattern is *always*: pick a substitution that turns the model into "(linear function of new variables) = constant + constant × (other new variable)." Then plot in the new variables. The linearisation trick generalises to *any* model where one transformation makes things linear.

> [!info] Linearisation in physics — three places it shows up
> 1. **Hubble’s law.** Plot recession speed $v$ vertically against distance $d$ horizontally on ordinary axes: the gradient of $v=H_0d$ is $H_0$. On log–log axes, $\log v=\log H_0+\log d$: the gradient is **1**, while the intercept encodes the numerical $H_0$ in stated units. Taking logs does not remove peculiar-velocity scatter.
> 2. **Allometric scaling in biology.** Animal metabolic rate vs body mass: on log–log paper a classic approximate model has slope $3/4$ (Kleiber's law); the fitted exponent depends on the organisms and conditions. Without logs, an elephant and a mouse couldn't even share the same chart.
> 3. **Lens equation.** $\dfrac{1}{f} = \dfrac{1}{u} + \dfrac{1}{v}$ — already linear in the *reciprocals*. Plot $1/v$ against $1/u$ and read off $1/f$ as the intercept. This is a homework standard in optics labs.
>
> Whenever an empirical relationship has a *power*, an *exponential*, or a *reciprocal* in it, linearisation is the first move. Computers have made nonlinear regression cheap, but the *insight* — "this is a power law of exponent $3/2$" — comes most clearly from a straight line.

The distance–velocity derivation and calibration limits are developed in [[Hubble's Law and the Expanding Universe]].

---

## Common Mistakes

1. **Reporting $\log A$ as $A$.** The intercept is $\log A$, *not* $A$ itself. Always exponentiate at the end: $A = 10^{\text{intercept}}$ (if using base $10$) or $A = e^{\text{intercept}}$ (if using $\ln$).
2. **Computing gradient from raw $(x, y)$ instead of $(\log x, \log y)$.** The whole point is that the *transformed* data is on a line. Gradients on the original plot will vary across the data — they're not what the question is asking for.
3. **Mixing $\lg$ and $\ln$ mid-problem.** Pick one and stick with it. If you take $\lg y$ at the start, every "log" in the working is $\lg$ until the end. Switching halfway turns gradients and intercepts into garbage (because $\ln 10 \approx 2.303$, the conversion factor).
4. **Assuming the wrong model.** If the question doesn't specify, *check* — inspect the plots and residuals; a short or noisy dataset may not distinguish the alternatives.
5. **Reading gradient from raw data points instead of from the line of best fit.** Use *line* points (well-separated), not data points.
6. **Forgetting the $y$-intercept matters.** The gradient gives you $n$ (or $\log b$); the intercept gives you $A$. Both are needed to specify the model. Common loss-of-marks: students nail the gradient but never compute $A$.

---

## Exam Notes

### Cambridge 0606 — §7.4

The 2025–2027 syllabus requires interpreting a supplied relationship by reducing it to straight-line form. It explicitly includes $y=Ax^n$ and $y=Ab^x$, **and other transformations**, such as $y^2=Ax^3+B$, $e^{2y}=Ax^2+B$ and $y^3=A\ln x+B$. For the last example, plot $Y=y^3$ against $X=\ln x$: gradient $A$, intercept $B$. Taking logs of both sides indiscriminately would not help.

State the transformed variables, identify the gradient and intercept algebraically, and recover the original constants. For a graph question, use the best-fit line and a large gradient triangle. Keep guard digits; follow the requested precision rather than assuming one universal decimal-place or mark-allocation rule. The examples above are original teaching problems, not transcriptions of past papers.

### Cambridge 9709 — Pure Mathematics 2 §2.2 and Pure Mathematics 3 §3.2

Both log/exp sections include using logarithms to transform a relationship into straight-line form and determining unknown constants. These are **Paper 2 and Paper 3**, not Pure Mathematics 1. The log laws select the axes; an intercept representing a logarithm must be exponentiated. Cambridge 9231 assumes the relevant 9709 mathematics; it does not add a separate logarithmic-graph-fitting topic.

### Edexcel IAL — Pure Mathematics 3 §3.3

The specification explicitly requires estimating the parameters of power and exponential relationships using logarithmic graphs. The two derivations above explain the required transformations and parameter recovery.

### IB Mathematics: Analysis and Approaches

In the first-assessment-2021 guide, SL 2.9 covers exponential/logarithmic functions and SL 4.4 covers linear regression. These support the algebra and data interpretation, but do **not** establish a separate mandatory log–log/semi-log fitting unit or an HL-only nonlinear-regression requirement. Treat this technique as a useful modelling extension. [IB AA guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf)

### AP — distinguish the course and the year

**AP Statistics through the May 2026 exam:** former Topic 2.9 covered transformations for departures from linearity. **For 2026–2027 onward, that topic has been removed.** It remains useful enrichment, not a current required topic. [College Board: AP Statistics revisions](https://apcentral.collegeboard.org/courses/ap-statistics/future-revisions)

**AP Calculus AB/BC Topic 4.6** uses “linearization” for a *local tangent-line approximation*, $f(x)\approx f(a)+f'(a)(x-a)$. That is a different operation from changing axes to straighten a model; the word alone does not imply this graph-fitting technique is required.

### Where this particular technique is not prescribed

**Cambridge 0580, OxfordAQA 9260 and OxfordAQA 9660** do not name this logarithmic graph-fitting technique as a separate requirement in the specifications checked. Their graph skills, and 9660's logarithms/exponential modelling, are related foundations. This is not a claim that those boards never supply a transformed graph to interpret.

---

## Connections

- **Prerequisite:** [[Logarithms]] — every step of the algebra is a log law (product, power); without solid logs the technique is opaque
- **Prerequisite:** [[Equation of a Straight Line (Vocab)]] — the *output* of linearisation is $Y = c + mX$, which is just $y = mx + c$ in different letters
- **Prerequisite:** [[Recording and Analysing Experimental Data]] — the straight-line graph itself: scales, best-fit line, the large gradient triangle and the meaning of the intercept.
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
