---
chinese: 卡西欧 fx-991 使用指南 (kǎxī'ōu)
prerequisites:
  - "[[Calculator Skills (Vocab)]]"
  - "[[Order of Operations (Vocab)]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/A-Level
  - curriculum/IB-AA
  - type/reference
  - calculator/casio-fx991
---

# Casio fx-991 Reference 卡西欧 fx-991 使用指南

## Scope

This is a model-specific reference for the **Casio fx-991** family — the dominant non-graphing scientific calculator for **Cambridge IGCSE 0580/0606**, **A-Level Maths/Further Maths (9709, OxAQA 9260)**, and **IB Mathematics SL** (where graphing isn't strictly required). For *general* calculator principles (BIDMAS, brackets, DEG mode, sanity-check habit), see [[Calculator Skills (Vocab)]].

**Models covered:**

| Model | Year | Display | Notes |
|---|---|---|---|
| **fx-991EX ClassWiz** | 2015 | high-resolution dot matrix | most common globally; the workhorse for the past decade |
| **fx-991CW** | 2022 | high-resolution dot matrix | newer ClassWiz; revised menu structure (more "modern" but unfamiliar to teachers) |
| **fx-991CN X** | 2018 | same as EX | Chinese-market version — same engine + a few extras (unit conversion, larger LCM/GCD, Chinese UI) |
| fx-991ES Plus | 2008 | lower-res | older; phasing out but still in some Asian schools |

This card uses **fx-991EX ClassWiz** as the default since it's the most-encountered model. The fx-991CW reorganises menus but the underlying capabilities are the same; differences are noted below where they matter.

### 中文锚点

**Casio fx-991 系列** 是 Cambridge / A-Level / IB SL 学生的主力计算器。本卡列出常用功能、按键序列、及考试技巧。

主流型号：
- **fx-991EX ClassWiz** (2015)：最常见
- **fx-991CW** (2022)：新版 ClassWiz，菜单结构改了
- **fx-991CN X** (2018)：中国大陆版，引擎相同，多了单位换算等
- fx-991ES Plus (2008)：老款，正在淘汰

---

## Mode Menu — choose your tool

Press `MENU` (top-row, near the screen) on the EX, or `HOME` on the CW. Available modes:

| Mode (icon) | What it does | When to use |
|---|---|---|
| **Calculate** (1) | normal arithmetic | default for almost everything |
| **Statistics** (6) | 1-var and 2-var stats; regression (linear, quadratic, exponential, log) | Cambridge §9 statistics; A-Level S1 |
| **Table** (3) | tabulate $f(x)$ over a range | sketching a curve, finding sign changes |
| **Equation/Func** | solve linear systems (2-3 unknowns), polynomial (degree 2-4) | Cambridge §5; A-Level quadratic/cubic |
| **Inequality** | solve quadratic/cubic inequalities | 0606 §2.5, §4.5 |
| **Complex** | $i$ arithmetic, polar form | A-Level Further, IB HL |
| **Base-N** | binary, octal, hex arithmetic | CS / electronics |
| **Matrix** | matrix operations up to 4×4 | A-Level FP1 / IB HL |
| **Vector** | vector operations in 2D/3D | A-Level / IB HL |
| **Ratio** | $a:b = c:d$ proportion solver | rare but useful for Cambridge proportion |
| **Distribution** | normal, binomial, Poisson PDF/CDF | IB / AP Stats |
| **Spreadsheet** | mini-spreadsheet for data tables | uncommon |

> [!tip] Set the angle mode FIRST every time you open the calculator
> Press `SHIFT + MENU` (= SETUP) and choose **Angle Unit → Degree**. The display shows "D" in the top bar. For A-Level / IB calculus questions involving radians, switch to `Radian` (display shows "R"). Cambridge 0580/0606 trig is *always* in degrees; A-Level mostly radians.

---

## Core Operations

### Brackets and the natural-display fraction button

The fx-991EX uses **Natural Display** (the $\frac{a+b}{c+d}$ template that lets you see the expression as you type). Two buttons matter:

- $\boxed{a\frac{b}{c}}$ — mixed-fraction template (top-left, near the cursor pad). Press to enter a fraction; the cursor sits in the numerator, then arrow-down for denominator.
- $\boxed{S \leftrightarrow D}$ — toggle between fraction-form (or surd-form) and decimal. Use after computing to reveal exact answer if the calculator hides it as a long decimal.

**Example.** Compute $\dfrac{2.7 + 4.6}{0.45 - 0.18}$.

Press: $\boxed{a\frac{b}{c}}$ → type `2.7 + 4.6` → arrow-down → type `0.45 - 0.18` → `=`.

Result displays as the fraction; press `S↔D` for the decimal $\approx 27.04$.

### Powers, roots, reciprocals

| Operation | Keys |
|---|---|
| $x^2$ | `x²` (dedicated button) |
| $x^3$ | `SHIFT + x²` |
| $x^y$ general power | `^` (top row, near `x²`) |
| $\sqrt{x}$ | `√` (left column) |
| $\sqrt[3]{x}$ | `SHIFT + √` |
| $\sqrt[n]{x}$ | `SHIFT + ^` (n-th root template) |
| $\dfrac{1}{x}$ | `x⁻¹` (or `^` then `(-1)`) |
| $10^x$ | `SHIFT + log` |
| $e^x$ | `SHIFT + ln` |

### Trig and log

| Operation | Keys |
|---|---|
| $\sin\theta$ | `sin` then angle |
| $\sin^{-1}(x)$ | `SHIFT + sin` |
| $\log_{10} x$ | `log` |
| $\ln x$ | `ln` |
| $\log_b x$ (any base) | `log` template — type base in subscript box |

> [!warning] $\log_b$ template needs the **base subscript filled in**
> The fx-991EX has a logarithm template `log_□(□)` accessed via `log` button on the EX (or `log_□` on the CW). The base goes in the small subscript; the argument in the main bracket. Without filling the base, the calculator defaults to $\log_{10}$ — a silent error if you wanted $\log_2$.

### Memory: Ans, M, A–F variables

- $\boxed{\text{Ans}}$ — last computed result. Press as the *first key* of a new expression to reuse: `Ans + 5 =` adds 5 to the last result.
- $\boxed{\text{M+}}$ / $\boxed{\text{M-}}$ — add/subtract to the persistent memory `M`.
- $\boxed{\text{STO}}$ + variable letter (`A`, `B`, `C`, `D`, `E`, `F`, `M`, `X`, `Y`) — store current result.
- $\boxed{\text{ALPHA}}$ + variable letter — recall a stored value into an expression. Useful for chained computations involving the same constant.

---

## Specialty Modes

### Equation/Func mode — solve polynomials and linear systems

Press `MENU` → `Equation/Func` (icon varies). Two main sub-modes:

- **Polynomial** — solve $ax^2 + bx + c = 0$, $ax^3 + bx^2 + cx + d = 0$, $ax^4 + \ldots = 0$ (degree 2–4). Enter coefficients; calculator returns roots, including complex ones (in $a + bi$ form if the calculator is in Complex display).
- **Linear System** — solve $\{a_1 x + b_1 y = c_1; a_2 x + b_2 y = c_2\}$ (2 unknowns) or 3 unknowns. Enter the coefficient matrix; calculator returns $x, y, z$.

> [!tip] The Equation mode is the fastest way to solve a quadratic
> When 0606 asks "solve $3x^2 - 5x - 2 = 0$", you can:
> 1. Use the quadratic formula by hand (slow but always works).
> 2. Enter `MENU → Equation/Func → Polynomial → degree 2`, type `3, -5, -2`, press `=` for $x_1 = 2$, press `=` for $x_2 = -\tfrac{1}{3}$.
>
> The second approach is exam-legal and saves time. **But** show working — Cambridge marks method, not just final answer. Use the calculator to *check* your hand-computed answer.

### Statistics mode — single-variable and regression

Press `MENU → Statistics`. Choose:

- **1-var stats** — enter a list of values; calculator returns mean ($\bar x$), standard deviation ($\sigma_x$, $s_x$), sum, sum of squares, n, min, max, median, quartiles.
- **2-var regression** — enter $(x, y)$ pairs; pick a regression type from the menu:

| Regression type | Equation | When to use |
|---|---|---|
| **a + bx** (or **A + Bx**) | $y = a + bx$ | linear regression — Cambridge §9.5 line of best fit |
| **_ + bx + cx²** | $y = a + bx + cx^2$ | quadratic regression |
| **a · b^x** | $y = a \cdot b^x$ | exponential growth/decay |
| **a · x^b** | $y = a x^b$ | power law (cashes [[Linearisation]]) |
| **a + b·ln x** | $y = a + b \ln x$ | logarithmic |

After entering data, press `OPTN` (or `Tools` on CW) to access regression coefficients and the correlation coefficient $r$.

### SOLVE — find roots of any equation

Type an equation using `ALPHA + )` for the equals sign. Press `SHIFT + CALC` (= SOLVE). Calculator prompts for an initial guess of $x$, then iterates (Newton's method internally) to find a root.

**Example.** Solve $x^3 + x = 5$.

Type `X^3 + X = 5` (the X is `ALPHA + )` — wait, that's the equals sign on EX; X variable is `ALPHA + ` and the X letter, varies by model — check your specific model's chart). Press `SOLVE`. Initial guess: $1$. Calculator returns $x \approx 1.5159$.

> [!warning] SOLVE finds *one* root, near your guess
> For multi-root equations, you must seed different initial guesses to find each root. Sketch the function first to see how many roots there are and roughly where, *then* SOLVE around each.

---

## Display Modes

`SHIFT + MENU` (SETUP) → display options:

| Mode | What you see |
|---|---|
| **MathIO** (Natural Display) | $\frac{a}{b}$, $\sqrt{2}$, $\pi$ rendered as on paper |
| **LineIO** | one-line text (e.g., `1/2 + 1/3` instead of stacked fractions) |
| **Norm 1** | switches to scientific notation when number $> 10^{10}$ |
| **Norm 2** | switches to scientific notation when number $> 10^{10}$ but with finer threshold |
| **Fix n** | always display $n$ decimal places |
| **Sci n** | always display in scientific notation with $n$ s.f. |

**Default for exams: MathIO + Norm 1.** Always reset to this if you discover the calculator has been left in Fix or Sci mode.

---

## Cambridge / A-Level / IB Exam Tips

### Cambridge 0580 / 0606

- Most questions can be done entirely in **Calculate** mode with the natural-display fraction.
- For "solve a quadratic" → use **Equation/Func → Polynomial** to verify your hand-solved answer.
- For "find $x$ when $\sin x = 0.7$" → check **DEG** mode, type `sin⁻¹(0.7)`. Cambridge expects degrees.
- For "estimate $\sqrt{83}$" → don't use the calculator; use mental estimation ([[Estimation (Vocab)]]).

### A-Level (Cambridge 9709, OxAQA 9260)

- Trig involving radians → set **RAD**.
- For statistics S1 — use **Statistics** mode for mean, SD, regression $r$.
- For numerical SOLVE on transcendental equations (e.g., $x = \cos x$) → SOLVE mode.

### IB Mathematics SL / HL

- IB allows the fx-991 (it's a non-CAS scientific calculator). HL students sometimes prefer a graphing calculator (TI-Nspire / Casio fx-CG50), but the fx-991 covers everything except graphing.
- **Distribution** mode is gold for IB stats: `Normal CD` for $P(a < X < b)$ when $X \sim N(\mu, \sigma^2)$; `Inverse Normal` for percentile-to-z-score; `Binomial PD` and `Binomial CD` for $X \sim B(n, p)$.

---

## Common Gotchas

1. **Forgetting DEG/RAD mode.** The single most common calculator error in Cambridge IGCSE.
2. **Negative-sign vs subtraction.** $\boxed{(-)}$ for unary minus; $\boxed{-}$ for subtraction. The two have *different* display widths.
3. **Pressing `S↔D` to find a long answer was actually exact.** $\sqrt{8}$ displays as $2\sqrt{2}$ (Math mode); pressing `S↔D` shows $2.828427\ldots$. Read which form the question wants — often "exact" means leave as $2\sqrt 2$.
4. **Forgetting to clear the display between problems.** Press `AC` (All Clear) to reset; otherwise old `Ans` may pollute new computations.
5. **Statistics mode persistence.** Returning from Statistics to Calculate mode does *not* clear the data list. To start fresh, re-enter Statistics mode and use `Edit → Delete All`.
6. **fx-991CW menu reorganisation.** The CW (2022) moved `SOLVE`, `Equation/Func`, and several functions into a new structure. If you're using a CW and a tutorial says "press SHIFT + CALC", the CW equivalent might be in a different menu. The capability is there; only the navigation differs.

---

## Connections

- **Prerequisite:** [[Calculator Skills (Vocab)]] — calculator-agnostic principles (BIDMAS, brackets, sanity-check)
- **Sibling:** [[TI-84 CE Reference]] — the AP-default calculator
- **Application:** every Cambridge 0580/0606 calculator-paper question, every A-Level Pure / Stats question
- **Beyond:** *graphing calculators* — fx-CG50 (Casio's graphing model) covers IB HL graph-required tasks; Cambridge does not require graphing

---

## LaTeX Reference

(For typing buttons in vault notes referring to the calculator.)

| Button | LaTeX | Notes |
|---|---|---|
| $\boxed{S \leftrightarrow D}$ | `\boxed{S \leftrightarrow D}` | decimal-fraction toggle |
| $\boxed{a\dfrac{b}{c}}$ | `\boxed{a\dfrac{b}{c}}` | mixed-fraction template |
| $\boxed{(-)}$ | `\boxed{(-)}` | unary minus |
| $\boxed{\text{Ans}}$ | `\boxed{\text{Ans}}` | last answer |
| $\boxed{\text{SOLVE}}$ | `\boxed{\text{SOLVE}}` | numerical equation solver |
