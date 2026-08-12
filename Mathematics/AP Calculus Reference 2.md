---
chinese: AP 微积分考试公式表对照 (gōngshì biǎo duìzhào)
prerequisites: []
leads_to: []
tags:
  - subject/mathematics
  - domain/exam-strategy
  - level/AP
  - curriculum/AP
  - type/reference
  - type/exam-technique
---

# AP Calculus Reference (AB + BC) — what's given, what's yours

## What this card is for

For students taking **AP Calculus AB** or **AP Calculus BC** — what does the College Board hand you on exam day, and what do you have to bring in your head?

The short answer: **almost nothing is handed to you, and almost everything is in your head.** This is the structural difference between AP Calculus and Cambridge 9709 — see [[MF19 Reference (9709)]] for the contrast.

> [!warning] AP Calculus is a *no-formula-sheet* exam
> Unlike Cambridge 9709 (which gives you the comprehensive [[MF19 Reference (9709)|MF19 booklet]]) or A-Level Edexcel (which gives a substantial formula booklet), the AP Calculus AB and BC exams provide **no calculus reference sheet**. The College Board's structural decision: students should *internalise* derivatives and integrals as part of learning, not look them up. The Course and Exam Description (CED, 2020 onwards) is explicit that "memorising an algorithm" is *not* the goal — but the corresponding formulas absolutely *are* expected to be at recall speed.
>
> Verified against the official *AP Calculus AB and BC Course and Exam Description*: no formula-sheet appendix; Calculator Policy notes about which graphing calculators are permitted; no general formula booklet.

The pedagogical point: AP grades calculus *understanding*, not lookup. The exam expects you to differentiate $\sec x$, integrate $1/(x^2+1)$, write the Maclaurin series for $\sin x$, and apply the chain rule, *all from memory*, in real time, without a sheet. That's the opportunity cost of the no-sheet design — the exam room is a memory test as much as a reasoning test.

### 中文锚点

**AP 微积分考试不发公式表。** 这是 AP 与剑桥 9709 最大的结构性差别：

- **9709**：考试时发 MF19 公式表，大部分公式都在表上，考的是「会不会用」。
- **AP Calc AB / BC**：考试时只能带计算器；公式全靠脑子。考的是「能不能背 + 会不会用」。

**核心后果**：备考 AP 的时间分配跟备考 9709 完全不同。AP 学生需要把整个微分、积分、级数公式表背下来；9709 学生只要熟练使用 MF19 即可。

如果你既考 9709 又考 AP（可能性不大但有），把 MF19 当作「学习时的脚手架」、把 AP 的「全部记忆」当作「最终目标」—— AP 准备好了，9709 自然没问题（反过来不一定）。

---

## What IS provided on AP exam day

A short list, all *non-calculus*:

- **A graphing calculator** that the student brings (must be on the [AP-approved list](https://apstudents.collegeboard.org/exam-calculator-policy/calculus-policy)). Most AP students bring a TI-84 or TI-Nspire CX. See [[TI-84 CE Reference]] for the calculator-side cheatsheet.
- **A pencil, eraser, and exam booklet.** That's it.

That's the entire on-day allowance. **No printed formulas. No reference card. No statistical tables.** Multiple-choice and free-response sections both run on memorised content + calculator-supported computation.

---

## Master list — Differentiation (must memorise for AB and BC)

The full standard-derivatives table. Every entry is required-on-the-day for AB; BC adds inverse-trig, hyperbolic, and parametric variants.

### Foundational (AB and BC)

| $f(x)$ | $f'(x)$ |
|---|---|
| $c$ (constant) | $0$ |
| $x^n$ | $n x^{n-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $1/x$ |
| $\log_a x$ | $1/(x \ln a)$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\csc x$ | $-\csc x \cot x$ |
| $\cot x$ | $-\csc^2 x$ |

### Inverse-trig (AB and BC — yes, AB requires these)

| $f(x)$ | $f'(x)$ |
|---|---|
| $\arcsin x$ | $\dfrac{1}{\sqrt{1 - x^2}}$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1 - x^2}}$ |
| $\arctan x$ | $\dfrac{1}{1 + x^2}$ |
| $\mathrm{arccsc}\, x$ | $-\dfrac{1}{\lvert x \rvert \sqrt{x^2 - 1}}$ |
| $\mathrm{arcsec}\, x$ | $\dfrac{1}{\lvert x \rvert \sqrt{x^2 - 1}}$ |
| $\mathrm{arccot}\, x$ | $-\dfrac{1}{1 + x^2}$ |

### Differentiation rules (must memorise)

- **Chain rule:** $\dfrac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$
- **Product rule:** $(uv)' = u'v + uv'$
- **Quotient rule:** $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$
- **Chain rule, Leibniz:** $\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$
- **Implicit differentiation:** treat $y$ as $y(x)$, apply chain rule on every $y$-term — see [[Implicit Differentiation]]
- **Parametric (BC only):** $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ — see [[Parametric Differentiation]]
- **Second-derivative parametric (BC only — Topic 9.2):** $\dfrac{d^2 y}{dx^2} = \dfrac{1}{dx/dt}\cdot\dfrac{d}{dt}\!\left(\dfrac{dy}{dx}\right)$
- **Inverse-function rule:** $(f^{-1})'(y) = 1/f'(x)$ where $y = f(x)$ — see [[Implicit Differentiation]]

---

## Master list — Integration (must memorise for AB and BC)

### Foundational (AB and BC)

| $f(x)$ | $\displaystyle \int f(x) \, dx$ |
|---|---|
| $x^n$, $n \neq -1$ | $\dfrac{x^{n+1}}{n+1} + C$ |
| $1/x$ | $\ln \lvert x \rvert + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\dfrac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\sec x \tan x$ | $\sec x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |
| $\csc x \cot x$ | $-\csc x + C$ |

### Inverse-trig integrals (AB and BC)

| $f(x)$ | $\displaystyle \int f(x) \, dx$ |
|---|---|
| $\dfrac{1}{1 + x^2}$ | $\arctan x + C$ |
| $\dfrac{1}{\sqrt{1 - x^2}}$ | $\arcsin x + C$ |
| $\dfrac{1}{\lvert x \rvert \sqrt{x^2 - 1}}$ | $\mathrm{arcsec}\, x + C$ |
| $\dfrac{1}{x^2 + a^2}$ | $\dfrac{1}{a}\arctan\dfrac{x}{a} + C$ |
| $\dfrac{1}{\sqrt{a^2 - x^2}}$ | $\arcsin\dfrac{x}{a} + C$ |

### Special trig integrals (AB and BC)

| $f(x)$ | $\displaystyle \int f(x) \, dx$ |
|---|---|
| $\tan x$ | $\ln \lvert \sec x \rvert + C = -\ln \lvert \cos x \rvert + C$ |
| $\cot x$ | $\ln \lvert \sin x \rvert + C$ |
| $\sec x$ | $\ln \lvert \sec x + \tan x \rvert + C$ |
| $\csc x$ | $-\ln \lvert \csc x + \cot x \rvert + C$ |

### Patterns (must memorise — not formulas, but recognition)

- $\displaystyle \int \dfrac{f'(x)}{f(x)}\,dx = \ln \lvert f(x) \rvert + C$
- $\displaystyle \int u\,dv = uv - \int v\,du$ (integration by parts)
- $\displaystyle \int f(g(x)) g'(x)\,dx = \int f(u)\,du$ ($u$-substitution)
- **Linear-inside rule:** $\int g(ax + b)\,dx = \dfrac{1}{a}G(ax + b) + C$ where $G' = g$.

For full discussion of these, see [[Standard Integrals]].

---

## BC-only additions

### Sequences and series (Unit 10)

| Series | Formula |
|---|---|
| Geometric series sum (finite) | $\sum_{k=0}^{n-1} ar^k = \dfrac{a(1 - r^n)}{1 - r}$ |
| Geometric series sum (infinite, $\lvert r \rvert < 1$) | $\sum_{k=0}^{\infty} ar^k = \dfrac{a}{1 - r}$ |
| Maclaurin series, $e^x$ | $\sum_{n=0}^{\infty} \dfrac{x^n}{n!} = 1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \cdots$ |
| Maclaurin series, $\sin x$ | $\sum_{n=0}^{\infty} \dfrac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \cdots$ |
| Maclaurin series, $\cos x$ | $\sum_{n=0}^{\infty} \dfrac{(-1)^n x^{2n}}{(2n)!} = 1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \cdots$ |
| Maclaurin series, $\dfrac{1}{1-x}$ ($\lvert x \rvert < 1$) | $\sum_{n=0}^{\infty} x^n = 1 + x + x^2 + \cdots$ |
| Maclaurin series, $\ln(1+x)$ ($-1 < x \leq 1$) | $\sum_{n=1}^{\infty} \dfrac{(-1)^{n+1} x^n}{n} = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \cdots$ |
| Maclaurin series, $\arctan x$ ($\lvert x \rvert \leq 1$) | $\sum_{n=0}^{\infty} \dfrac{(-1)^n x^{2n+1}}{2n + 1} = x - \dfrac{x^3}{3} + \dfrac{x^5}{5} - \cdots$ |
| Lagrange error bound | $\lvert R_n(x) \rvert \leq \dfrac{M}{(n+1)!}\lvert x - c \rvert^{n+1}$ where $M = \max\lvert f^{(n+1)}\rvert$ |

### Convergence tests (Unit 10)

- $n$-th term test, integral test, comparison test, limit comparison test, alternating series test, ratio test, root test
- Power-series interval of convergence via the ratio test
- $p$-series convergence ($\sum 1/n^p$ converges iff $p > 1$)

### Parametric, polar, and vector-valued (Unit 9)

- **Velocity / speed (parametric):** $\mathbf{v}(t) = (\dot{x}, \dot{y})$, $\lvert\mathbf{v}\rvert = \sqrt{\dot{x}^2 + \dot{y}^2}$
- **Arc length (parametric):** $L = \int_a^b \sqrt{\dot{x}^2 + \dot{y}^2}\,dt$
- **Polar coordinates:** $x = r\cos\theta$, $y = r\sin\theta$, $r^2 = x^2 + y^2$, $\tan\theta = y/x$
- **Polar area:** $A = \dfrac{1}{2}\int_\alpha^\beta r^2\,d\theta$
- **Polar arc length:** $L = \int_\alpha^\beta \sqrt{r^2 + (dr/d\theta)^2}\,d\theta$

### Differential equations (Unit 7, AB introduces, BC extends)

- **Slope fields** — graphical interpretation
- **Separation of variables:** $\int g(y)\,dy = \int f(x)\,dx$
- **Logistic growth (BC):** $\dfrac{dy}{dt} = ky(L - y)$ → solution $y = \dfrac{L}{1 + Ce^{-kLt}}$
- **Euler's method (BC, sometimes):** $y_{n+1} = y_n + h\,f(x_n, y_n)$

---

## Common formulas not on syllabus but useful

These are *outside* AP Calc but worth knowing for cross-domain use (AP Physics, AP Statistics, college):

- **Hyperbolic:** $\sinh x = (e^x - e^{-x})/2$, $\cosh x = (e^x + e^{-x})/2$, $\tanh x = \sinh x / \cosh x$
- **Cross product / curl:** AP Calc doesn't cover; AP Physics C does
- **Multivariable partial derivatives** — beyond AP, university level

---

## Net memorise-list summary for AP students

The honest scope:

- **Differentiation:** the full standard-derivatives table (12 foundational + 6 inverse-trig = 18 entries) + 6 differentiation rules. **24 items at recall speed.**
- **Integration:** the full standard-integrals table (10 foundational + 5 inverse-trig + 4 special trig = 19 entries) + 4 patterns. **23 items at recall speed.**
- **BC additions:** ~9 series formulas + 7 convergence tests + 6 parametric/polar formulas + 4 differential-equations methods. **~26 additional items.**

**Grand total for AP Calc BC: ~70 distinct memorable formulas/patterns.** That's the price of a no-formula-sheet exam, and why AP students do flashcard drills the week before the exam in a way Cambridge 9709 students don't.

> [!tip] How to actually do this
> Don't try to brute-force-memorise 70 things. Memorise *patterns*: the chain rule, the linear-inside rule, $f'/f \to \ln$, $u$-substitution, integration by parts. Most of the table is recoverable from a few patterns + a small base of derivatives. Then drill the *base* (sin → cos, cos → -sin, $\sec^2 \to \tan$, etc.) and the patterns are doors into the rest.

---

## Connections

- **Sister card for Cambridge 9709:** [[MF19 Reference (9709)]] — the comparison is structural. MF19 has *most* of the AP must-memorise list printed on it, free; AP gives you nothing. Studying for both means working in MF19-mode while preparing AP-mode in your head.
- **Per-card cross-references:** Most of the calculus cards in the vault now have or will have an AP callout: [[Standard Integrals]], [[Differentiation Rules]], [[Implicit Differentiation]], [[Parametric Differentiation]], [[L'Hôpital's Rule]], [[Integration]], [[Integration by Parts]], [[Integration by Substitution]], etc.
- **Topic map:** [[AP-Calculus-BC-Topic-Map|AP Calc BC Topic Map]] — the unit-by-unit coverage tracker. Use this to navigate vault content by AP unit.
- **Calculator-side companion:** [[TI-84 CE Reference]] — what your graphing calculator can do for you in the exam, when memory falters.

---

## Receipts

- **Source:** *AP Calculus AB and BC Course and Exam Description* (College Board, 2020 onwards). Verified 2026-05-07: no formula-sheet appendix in the CED.
- **Calculator policy:** [https://apstudents.collegeboard.org/exam-calculator-policy/calculus-policy](https://apstudents.collegeboard.org/exam-calculator-policy/calculus-policy)
- **Free-response question history:** released annually at AP Central; the cumulative pattern of "what's actually tested" beats "what's on syllabus" for most students' time-allocation decisions.

