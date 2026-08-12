---
chinese: TI-84 CE 使用指南
prerequisites:
  - "[[Calculator Skills (Vocab)]]"
  - "[[Order of Operations (Vocab)]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/number
  - level/AP
  - curriculum/AP
  - type/reference
  - calculator/ti-84-ce
---

# TI-84 Plus CE Reference

## Scope

This is a model-specific reference for the **Texas Instruments TI-84 Plus CE** — the dominant graphing calculator in **AP Calculus AB / BC**, **AP Statistics**, and **AP Physics 1 / 2** since around 2015. The CE is a colour-screen, lightweight successor to the TI-84 Plus and TI-83 Plus; the menu structure is mostly unchanged from the TI-84 Plus, so pre-2015 tutorials transfer directly. For *general* calculator principles, see [[Calculator Skills (Vocab)]].

**Why TI-84 CE for AP:** College Board's calculator policy approves a list (TI-83/84 family, TI-Nspire, Casio fx-9750/9860/CG, HP), but in practice US classrooms standardise on TI-84 Plus CE because (a) it's TI's flagship for high school, (b) AP review materials use it, and (c) AP Classroom video lessons demo on it. Buying a TI-Nspire or Casio is fine but means doing a translation step from every example you'll see online.

**Other TI models you might encounter:**

| Model | Notes |
|---|---|
| **TI-84 Plus CE** | colour screen, USB charging, current default (~2015–) |
| TI-84 Plus | monochrome, AAA batteries, identical menu structure |
| TI-83 Plus | older monochrome; same menus |
| **TI-Nspire CX II** | tablet-style; CAS version (Nspire CAS) is *banned* on AP Calc but allowed on AP Stats/Physics |
| TI-89 Titanium | CAS-capable; *banned on AP Calc* |

The non-CAS TI-Nspire CX II is allowed on AP Calc; CAS versions of any model are not. The TI-84 CE is non-CAS.

### 中文锚点

**TI-84 Plus CE** 是美国 AP 考试的标准计算器（AP Calculus AB/BC、AP Statistics、AP Physics）。本卡列出基础操作、菜单导航、考试技巧。

颜色屏幕，USB 充电，2015 年后的标准款。CAS 系列（如 TI-89, TI-Nspire CAS）在 AP Calc 是**禁用**的；TI-84 CE 是非 CAS，所有 AP 都允许。

---

## The Five Most-Used Menus

The TI-84 CE has dozens of menus, but five do most of the work:

| Menu | Key | What it's for |
|---|---|---|
| **Y= editor** | `Y=` (top-left, near screen) | enter functions to graph or tabulate |
| **GRAPH** | `GRAPH` (top row) | display the graph |
| **2nd CALC** (Calculate) | `2nd + TRACE` | numeric tools on a graph: zero, intersect, max, min, $\frac{dy}{dx}$, $\int f\,dx$ |
| **MATH** | `MATH` | numeric methods: nDeriv (numeric derivative), fnInt (numeric integral), MathPrint, MATH NUM (abs, round) |
| **STAT** | `STAT` | enter lists; STAT CALC for regressions; STAT TESTS for hypothesis testing |

Master these five, and the rest of the calculator is bonus. Press `2nd + MODE` (= QUIT) to back out of any menu and return to the home screen.

---

## Core Operations

### Arithmetic with brackets

Type expressions on the home screen as you would write them, *with brackets where needed*. The display preserves your input across multiple lines (scroll up with the up-arrow to recall and edit).

**Example.** Compute $\dfrac{(2.7 + 4.6)^2 \times 1.83}{0.45 - 0.18}$.

Press: `(2.7 + 4.6)^2 * 1.83 / (0.45 - 0.18)` then `ENTER`. Result: $361.567\ldots$.

To recall: press `2nd + ENTER` to bring back the previous expression for editing.

### Fractions and exact answers

The TI-84 CE has a **MathPrint** mode (default since 2010) that displays fractions and exponents naturally. Toggle:

- `MODE` → set **MathPrint** (option visible in the second screen of MODE menu).
- For a one-shot fraction display, press `MATH → 1: ▶Frac` after computing — converts decimal answer to fraction.

**Example.** Compute $\dfrac{1}{3} + \dfrac{1}{4}$:
- Type `1/3 + 1/4` → ENTER → displays `0.5833333333`.
- Press `MATH → 1: ▶Frac → ENTER` → displays `7/12`.

> [!info] TI-84 CE doesn't auto-simplify surds
> Unlike the Casio fx-991, the TI-84 CE returns $\sqrt{8} = 2.828\ldots$ rather than $2\sqrt{2}$. There's no built-in symbolic simplifier (that's a CAS feature, not on the CE). For exact-form answers requiring surds, work them by hand.

### Powers, roots, and logs

| Operation | Keys |
|---|---|
| $x^2$ | `x²` (dedicated key) |
| $x^y$ | `^` |
| $\sqrt{x}$ | `2nd + x²` |
| $\sqrt[3]{x}$ | `MATH → 4:³√(` |
| $\sqrt[n]{x}$ | `MATH → 5:ˣ√(` (use as `n MATH 5 x`) |
| $10^x$ | `2nd + LOG` |
| $e^x$ | `2nd + LN` |
| $\log_{10} x$ | `LOG` |
| $\ln x$ | `LN` |
| $\log_b x$ (any base) | `MATH → A:logBASE(` (input as `logBASE(x, b)`) |

### Trig and angle modes

`MODE` → set **DEGREE** or **RADIAN**. AP Calculus uses radians by default; AP Stats/Physics is mostly unitless. Always check before doing trig.

| Operation | Keys |
|---|---|
| $\sin\theta$, $\cos\theta$, $\tan\theta$ | dedicated keys |
| $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$ | `2nd + sin/cos/tan` |
| Angle conversion | `2nd + APPS` (= ANGLE menu) — degrees↔radians, decimal↔DMS |

---

## Graphing — the AP signature feature

### Plot $y = f(x)$

1. `Y=` → at `Y1=`, type the function (e.g., `X^2 - 3X + 2`). The variable button is `X,T,θ,n` (next to ALPHA).
2. `WINDOW` → set $x_{\min}, x_{\max}, y_{\min}, y_{\max}$. For a quick sensible window, press `ZOOM → 6:ZStandard` ($-10$ to $10$).
3. `GRAPH` → display.
4. `TRACE` → walk the cursor along the curve, showing $(x, y)$ values. Type a specific $x$ value to jump there.

### `2nd + CALC` — the AP gold mine

After graphing, press `2nd + TRACE` (= CALC) for numeric operations:

| Option | What it computes |
|---|---|
| **1: value** | $f(x)$ at a specific $x$ |
| **2: zero** | a root of $f(x) = 0$ within a bracket you specify |
| **3: minimum** | local minimum within a bracket |
| **4: maximum** | local maximum within a bracket |
| **5: intersect** | intersection of $Y_1$ and $Y_2$ within a bracket |
| **6: dy/dx** | numeric derivative at a specific $x$ |
| **7: ∫f(x)dx** | numeric definite integral over a specified $[a, b]$ |

> [!tip] AP Calc FRQ — definite integrals on the calculator
> AP Calculus FRQ (free-response) explicitly *requires* you to evaluate definite integrals on the calculator for many problems. The setup: type $f(x)$ into $Y_1$, graph it, then `2nd CALC → 7:∫f(x)dx`, lower limit, upper limit. The calculator returns the integral numerically. Faster than `MATH → 9:fnInt(` for visual sanity-checking.
>
> Equivalent on the home screen: `MATH → 9:fnInt(` typed as `fnInt(X^2, X, 0, 5)` — same numeric answer without graphing. Use whichever is faster for the question.

### `MATH` — numeric calculus tools

| Option | Function |
|---|---|
| `MATH 1: ▶Frac` | convert decimal answer to fraction |
| `MATH 8: nDeriv(` | numeric derivative; `nDeriv(f(X), X, x_value)` |
| `MATH 9: fnInt(` | numeric integral; `fnInt(f(X), X, a, b)` |
| `MATH NUM 1: abs(` | absolute value |
| `MATH NUM 5: int(` | integer part (round down) |
| `MATH NUM 4: round(` | round to specified decimal places |

---

## Statistics — AP Stats workhorse

### Entering data

`STAT → 1:Edit`. Lists $L_1, L_2, \ldots, L_6$ are pre-set. Type values into a column; press `ENTER` after each. To clear a list: arrow up to highlight the list name (e.g., $L_1$), `CLEAR`, `ENTER`.

### 1-variable statistics

`STAT → CALC → 1:1-Var Stats`. Choose the list (e.g., $L_1$). Calculator returns:

| Symbol | Meaning |
|---|---|
| $\bar x$ | mean |
| $\sigma_x$ | population standard deviation |
| $S_x$ | sample standard deviation |
| $n$ | count |
| min, Q1, Med, Q3, max | five-number summary |

### Linear regression

`STAT → CALC → 4:LinReg(ax+b)`. Choose $X_{\text{list}} = L_1$, $Y_{\text{list}} = L_2$. Calculator returns $a$, $b$, $r$ (correlation), $r^2$.

> [!tip] Turn on `DiagnosticOn` to see $r$ and $r^2$
> By default, regression on the TI-84 CE hides the correlation coefficients. To show them: `2nd + 0` (= CATALOG), arrow down to `DiagnosticOn`, `ENTER`, `ENTER` to confirm. Once on, every regression henceforth shows $r, r^2$. AP Stats requires $r$ in many free-response questions.

### Other regression types

`STAT → CALC` menu has several regression types:

| Option | Equation |
|---|---|
| 4: LinReg(ax+b) | $y = ax + b$ |
| 5: QuadReg | $y = ax^2 + bx + c$ |
| 6: CubicReg | $y = ax^3 + bx^2 + cx + d$ |
| 9: LnReg | $y = a + b\ln x$ |
| 0: ExpReg | $y = ab^x$ |
| A: PwrReg | $y = ax^b$ (power law — cashes [[Linearisation]]) |

Each takes $L_1, L_2$ inputs and returns the parameters.

### Distributions for AP Stats

`2nd + VARS` (= DISTR) accesses probability distributions.

| Option | Use |
|---|---|
| `1:normalpdf(` | $\phi(x)$ — bell-curve density |
| `2:normalcdf(` | $P(a < X < b)$ when $X \sim N(\mu, \sigma)$ — *the* AP Stats workhorse |
| `3:invNorm(` | inverse: given a probability, find the cutoff |
| `A:binompdf(` | $P(X = k)$ when $X \sim \text{Bin}(n, p)$ |
| `B:binomcdf(` | $P(X \le k)$ when $X \sim \text{Bin}(n, p)$ |
| `D:poissonpdf(`, `E:poissoncdf(` | Poisson |

**Common AP Stats syntax:** `normalcdf(lower, upper, μ, σ)`. For the standard normal, `normalcdf(-1.96, 1.96, 0, 1)` returns $\approx 0.95$.

---

## Equation Solver

`MATH → C: Solver` (on TI-84 CE; was `MATH → 0` on older 84s). Lets you solve an equation numerically:

1. Enter the equation in the form $0 = f(x)$. (Convert $f(x) = g(x)$ to $0 = f(x) - g(x)$.)
2. Provide an initial guess for $x$.
3. `ALPHA + ENTER` (= SOLVE) — calculator iterates and returns the root.

This is the TI-84 CE equivalent of Casio's `SHIFT + SOLVE`.

---

## AP Exam Tips

### AP Calculus AB / BC

- **Set RADIAN mode at the start of every session.** AP Calc is radians by default.
- **Definite integrals on the calculator** are AP-required for several FRQ each year. Practice both `2nd CALC 7:∫f(x)dx` (graph-based) and `MATH 9:fnInt(` (home-screen).
- **Numeric derivatives** for "find $f'(2)$ where $f(x) = \ldots$" are fastest via `nDeriv`.
- The **Y= editor** is essential for problems involving multiple curves: enter $f(x)$ as $Y_1$, $g(x)$ as $Y_2$, find their intersection with `2nd CALC 5:intersect`.

### AP Statistics

- **Lists** are the foundation. Get fluent at entering data, clearing lists, viewing them.
- **`normalcdf` and `invNorm`** appear on roughly half of AP Stats FRQs.
- **DiagnosticOn** must be enabled (one-time setup; persists until calculator reset).
- For two-sample inference, the `STAT → TESTS` menu has every named test (`2-SampTTest`, `2-PropZTest`, `χ²-Test`, etc.).

### AP Physics 1 / 2

- Trig in degrees for AP Physics 1; the conventions vary by problem in AP Physics 2.
- Statistics mode is rare on Physics; mostly arithmetic + powers + roots.
- Resetting the calculator between AP Calc, AP Stats, AP Physics sessions is sometimes prudent — make sure the angle mode and stat list state aren't leaking between subjects.

> [!warning] Calculator reset before the AP exam — *don't* unless instructed
> Some teachers tell students to do a full memory reset before the exam (`2nd + +` → MEM → 7:Reset → 1:All Memory). This *erases* all programs, lists, and saved settings. If you have programs you wrote (e.g., a quadratic-formula program), they're gone. Reset only if specifically required.

---

## Common Gotchas

1. **DEGREE vs RADIAN mode.** AP Calc = radians. Sin($30$) in radian mode is *not* $0.5$.
2. **`(-)` vs `−`.** Two distinct buttons. The unary minus `(-)` is below the `3` key; subtraction `−` is on the right column. Mixing them produces syntax errors.
3. **No exact surds.** $\sqrt{8} = 2.828$, not $2\sqrt{2}$. Switch to hand calculation when an exact form is requested.
4. **Forgetting to enable DiagnosticOn.** Your linear regression will lack $r$ until you turn this on (one-time only).
5. **Regression on tiny lists.** Need at least 2 points for linear regression, more for quadratic. Calculator returns an error otherwise.
6. **Y= functions persisting between problems.** Always check the Y= editor at the start of a new question. Old functions from problem 3 will still be plotted on problem 5's graph if you don't `CLEAR` them.

---

## Connections

- **Prerequisite:** [[Calculator Skills (Vocab)]] — calculator-agnostic principles
- **Sibling:** [[Casio fx-991 Reference]] — the A-Level / IB / Cambridge equivalent
- **Application:** every AP Calc and AP Stats free-response question involving numeric computation
- **Beyond:** *TI-Nspire CX II* — the next-generation TI calculator; menu structure is completely different but capabilities exceed TI-84 CE; sometimes preferred for IB HL

---

## LaTeX Reference

(For typing buttons in vault notes referring to the calculator.)

| Button / sequence | Notes |
|---|---|
| `2nd + TRACE` | CALC menu |
| `2nd CALC 7:∫f(x)dx` | numeric definite integral |
| `MATH 9:fnInt(` | home-screen numeric integral |
| `MATH 8:nDeriv(` | home-screen numeric derivative |
| `STAT CALC 4:LinReg(ax+b)` | linear regression |
| `2nd VARS 2:normalcdf(` | normal CDF for AP Stats |
| `Y=` | function editor |
| `(-)` | unary minus (distinct from `−`) |
