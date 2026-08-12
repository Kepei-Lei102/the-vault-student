---
chinese: OxfordAQA 9660 公式表对照 (gōngshì biǎo duìzhào)
prerequisites: []
leads_to: []
tags:
  - subject/mathematics
  - domain/exam-strategy
  - level/A-Level
  - curriculum/OxAQA-9660
  - type/reference
  - type/exam-technique
---

# OxAQA 9660 Reference — what's given, what's yours

## What this card is for

For students taking **Oxford International AQA (OxfordAQA) 9660 International AS / A-Level Mathematics**: what does the formula booklet hand you on exam day, and what do you have to bring in your head?

Verified against the official *International AS and A-Level Mathematics: Formulae and Statistical Tables* booklet (Oxford International AQA Examinations, 2016, 26 pages).

> [!info] OxAQA 9660 has the most generous formula booklet of any major international A-Level board
> Compare:
> - **OxAQA 9660** gives $\sin^{-1}, \cos^{-1}, \tan^{-1}$ derivatives **and** the full inverse-trig + inverse-hyperbolic integral table **and** $\sinh, \cosh, \tanh$ derivatives **and** $\int \sec x$, $\int \csc x$ in two equivalent forms. *All in the standard Pure Mathematics section.*
> - **Cambridge MF19** gives $\tan^{-1}$ derivative + $\arctan$-family integrals; *not* the $\sin^{-1}/\cos^{-1}$ derivatives or hyperbolics (those live on 9231 Further Math).
> - **Edexcel IAL** gives $\int \sec x$, $\int \csc x$ but *not* the $\arctan$ integral on Pure papers; inverse-hyperbolic integrals live on FP3.
> - **AP Calculus** gives no formula booklet at all.
>
> Net effect: **a 9660 student's "must memorise" list is the shortest of any major calculus exam.** The booklet covers most of what 9709 students must memorise (including $\sin^{-1}$ stuff that lives only on 9231 for Cambridge candidates).

The pedagogical point: studying for OxAQA 9660 is largely about *technique* and *recognition*, not *recall*. Almost every formula you'd care to memorise is in the booklet. Time spent on rote memorisation is largely wasted; time spent on practice problems and pattern-recognition is what scores.

### 中文锚点

**OxAQA 9660 公式表是国际 A-Level 数学考试中最慷慨的**：

- 反三角函数 $\sin^{-1}, \cos^{-1}, \tan^{-1}$ 的导数都在表上
- 反三角函数所有积分都在表上 (剑桥 MF19 没给 $\arcsin$；Edexcel 把这些放到 FP3)
- 双曲函数及其反函数的导数 + 积分都在表上 (剑桥放到 9231 Further，Edexcel 放到 FP3)
- $\int \sec x$, $\int \csc x$ 给出两种等价形式
- 三维旋转矩阵也在表上

**结论**：9660 学生需要背的内容最少。备考重点是「技巧 + 形状识别」，不是「死记硬背」。

---

## How to use this card

For each section below:

1. **Read the "given on the 9660 booklet" list first.** These are formulas you should *understand*, *be familiar with*, and *practice with* — but you don't need to memorise them.
2. **Read the "must memorise" list second.** A short list, but every item earns its keep.
3. **Spend more practice time on the must-memorise list and on technique problems.**

> [!info] Other boards have different sheets
> See [[MF19 Reference (9709)]] for Cambridge 9709 + 9231 (less generous than 9660 — keeps $\sin^{-1}$ family for Further Math), [[Edexcel IAL Reference]] for Pearson Edexcel IAL (less generous on Pure inverse-trig integrals; gives $\sec/\csc$ integrals like 9660 does), [[AP Calculus Reference]] for AP AB / BC (no booklet at all).

---

## Pure Mathematics — what's given on the 9660 booklet

### Series and summations

- **Arithmetic series:** $u_n = a + (n-1)d$, $S_n = \tfrac{1}{2}n(a+l) = \tfrac{1}{2}n[2a + (n-1)d]$
- **Geometric series:** $u_n = ar^{n-1}$, $S_n = \dfrac{a(1-r^n)}{1-r}$, $S_\infty = \dfrac{a}{1-r}$ for $\lvert r \rvert < 1$
- **Standard summations:** $\sum_{r=1}^n r = \tfrac{1}{2}n(n+1)$, $\sum r^2 = \tfrac{1}{6}n(n+1)(2n+1)$, $\sum r^3 = \tfrac{1}{4}n^2(n+1)^2$
- **Binomial series** (positive-integer $n$ in $(a+b)^n$ form, *and* rational $n$ in $(1+x)^n$ form with convergence $\lvert x \rvert < 1$)
- **Maclaurin series:** $e^x$, $\ln(1+x)$, $\sin x$, $\cos x$ — full general-term forms, with convergence ranges

### Logarithms, exponentials, complex numbers

- $a^x = e^{x \ln a}$
- $\{r(\cos\theta + i\sin\theta)\}^n = r^n(\cos n\theta + i\sin n\theta)$ (de Moivre)
- $e^{i\theta} = \cos\theta + i\sin\theta$
- $n$-th roots of unity: $z = e^{2\pi k i / n}$, $k = 0, 1, \ldots, n-1$

### Trigonometry — sum, product, cosine rule

- **Cosine rule:** $a^2 = b^2 + c^2 - 2bc\cos A$
- **Sum formulas:** $\sin(A \pm B), \cos(A \pm B), \tan(A \pm B)$
- **Sum-to-product (factor formulas):** $\sin A \pm \sin B$, $\cos A \pm \cos B$ all four

### Hyperbolic functions

- $\cosh^2 x - \sinh^2 x = 1$
- $\sinh 2x = 2\sinh x \cosh x$, $\cosh 2x = \cosh^2 x + \sinh^2 x$
- Inverse hyperbolics in log form: $\cosh^{-1} x = \ln(x + \sqrt{x^2-1})$ for $x \geq 1$, $\sinh^{-1} x = \ln(x + \sqrt{x^2+1})$, $\tanh^{-1} x = \tfrac{1}{2}\ln\dfrac{1+x}{1-x}$ for $\lvert x \rvert < 1$

### Conics

Standard form, parametric form (where applicable), foci, directrices, asymptotes for: ellipse, parabola, hyperbola, rectangular hyperbola.

### Vectors

- Resolved part of $\mathbf{a}$ in direction of $\mathbf{b}$: $\dfrac{\mathbf{a}\cdot\mathbf{b}}{\lvert\mathbf{b}\rvert}$
- Position vector of point dividing AB in ratio $\lambda:\mu$: $\dfrac{\mu\mathbf{a} + \lambda\mathbf{b}}{\lambda + \mu}$
- **Vector (cross) product:** $\mathbf{a}\times\mathbf{b} = \lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\sin\theta\,\hat{\mathbf{n}}$ with the determinant form
- Cartesian equation of a line through $A$ with direction $\mathbf{b}$
- Cartesian + vector equations of planes (point + normal, point + two direction vectors, three points)

### Matrix transformations

- 2D anticlockwise rotation matrix $\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$
- 2D reflection in $y = x\tan\theta$
- **3D rotation matrices** about each axis (x, y, z) — usually Further Math territory; 9660 puts them in standard Pure

### Differentiation — extended table

| $f(x)$ | $f'(x)$ |
|---|---|
| $\sin^{-1} x$ | $\dfrac{1}{\sqrt{1-x^2}}$ |
| $\cos^{-1} x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ |
| $\tan^{-1} x$ | $\dfrac{1}{1+x^2}$ |
| $\tan kx$ | $k\sec^2 kx$ |
| $\csc x$ | $-\csc x \cot x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ |
| $\tanh x$ | $\mathrm{sech}^2 x$ |
| $\sinh^{-1} x$ | $\dfrac{1}{\sqrt{1+x^2}}$ |
| $\cosh^{-1} x$ | $\dfrac{1}{\sqrt{x^2-1}}$ |
| $\tanh^{-1} x$ | $\dfrac{1}{1-x^2}$ |
| $\dfrac{f(x)}{g(x)}$ (quotient rule) | $\dfrac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$ |

> [!tip] Two surprises here vs. Cambridge / Edexcel
> **First surprise:** $\sin^{-1}$ and $\cos^{-1}$ derivatives are on the standard 9660 booklet. On MF19 they're on a Further-page (essentially 9231 territory), and Edexcel doesn't give them at all. *9660 students don't need to memorise these.*
>
> **Second surprise:** All the hyperbolic + inverse-hyperbolic derivatives. These are FP3 territory on Edexcel and 9231 territory on Cambridge. 9660 makes them standard Pure content.

### Integration — extended table (the big one)

| $f(x)$ | $\displaystyle \int f(x)\,dx$ |
|---|---|
| $\tan x$ | $\ln \lvert \sec x \rvert$ |
| $\cot x$ | $\ln \lvert \sin x \rvert$ |
| $\csc x$ | $-\ln \lvert \csc x + \cot x \rvert = \ln \lvert\tan(\tfrac{x}{2})\rvert$ |
| $\sec x$ | $\ln \lvert \sec x + \tan x \rvert = \ln \lvert\tan(\tfrac{x}{2} + \tfrac{\pi}{4})\rvert$ |
| $\sec^2 kx$ | $\dfrac{1}{k}\tan kx$ |
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ |
| $\tanh x$ | $\ln \lvert \cosh x \rvert$ |
| $\dfrac{1}{\sqrt{a^2 - x^2}}$ | $\sin^{-1}\dfrac{x}{a}$ for $\lvert x \rvert < a$ |
| $\dfrac{1}{a^2 + x^2}$ | $\dfrac{1}{a}\tan^{-1}\dfrac{x}{a}$ |
| $\dfrac{1}{\sqrt{x^2 - a^2}}$ | $\cosh^{-1}\dfrac{x}{a}$ or $\ln \lvert x + \sqrt{x^2 - a^2} \rvert$ for $x > a$ |
| $\dfrac{1}{\sqrt{a^2 + x^2}}$ | $\sinh^{-1}\dfrac{x}{a}$ or $\ln \lvert x + \sqrt{x^2 + a^2} \rvert$ |
| $\dfrac{1}{a^2 - x^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{a+x}{a-x}\right\rvert = \dfrac{1}{a}\tanh^{-1}\dfrac{x}{a}$ for $\lvert x \rvert < a$ |
| $\dfrac{1}{x^2 - a^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x-a}{x+a}\right\rvert$ |
| $\int u\dfrac{dv}{dx}\,dx$ | $uv - \int v\dfrac{du}{dx}\,dx$ (integration by parts) |

> [!tip] The 9660 student's exam-day strength
> Look at how much of the [[Standard Integrals]] table is in the booklet above. Compare to [[MF19 Reference (9709)|Cambridge MF19]] (no $\arcsin$, no inverse-hyperbolic) and [[Edexcel IAL Reference|IAL Pure]] (no $\arctan$ on P3/P4 booklet). *A 9660 candidate has every standard inverse-trig and inverse-hyperbolic integral printed on the day.* The exam tests whether you can *apply* them under transformation (substitution, completing the square) — not whether you remember them.

### Calculus applications

- Polar area: $A = \tfrac{1}{2}\int r^2\,d\theta$
- Arc length (Cartesian and parametric)
- Surface of revolution (Cartesian and parametric)
- Trapezium rule, mid-ordinate rule, Simpson's rule
- Euler's method for ODEs $\dfrac{dy}{dx} = f(x, y)$: $y_{r+1} = y_r + h f(x_r, y_r)$
- Newton-Raphson iteration: $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$

### Mechanics

- Motion in a circle: transverse velocity $v = r\dot{\theta}$, transverse acceleration $r\ddot{\theta}$, radial acceleration $-r\dot{\theta}^2 = -v^2/r$
- (That's effectively all that's printed for Mechanics specifically — most of M1/M2 content lives in your head.)

### Probability and Statistics

- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- $P(A \cap B) = P(A)\cdot P(B \mid A)$
- Bayes' theorem (full form)
- Expectation algebra: $E(aX + b) = aE(X) + b$, $\mathrm{Var}(aX + b) = a^2 \mathrm{Var}(X)$
- Covariance $\mathrm{Cov}(X, Y) = E(XY) - \mu_X \mu_Y$
- Standard discrete distributions (Binomial, Poisson, Geometric — formulas given)
- Normal PDF, Standard tables for cumulative Binomial, Poisson, Normal, $t$, $\chi^2$, $F$ distributions

---

## Must memorise — for OxAQA 9660 Pure Mathematics

A short list, given how much the booklet provides.

- **Standard derivatives** $\dfrac{d}{dx}(x^n) = nx^{n-1}$, $\sin' = \cos$, $\cos' = -\sin$, $\tan' = \sec^2$, $(e^x)' = e^x$, $(\ln x)' = 1/x$ — *not* on the booklet (the booklet starts at the $\sin^{-1}$ row of derivatives). Memorise these six.
- **Standard integrals** corresponding to the above: $\int x^n = x^{n+1}/(n+1)$, $\int e^x = e^x$, $\int 1/x = \ln \lvert x \rvert$, $\int \sin = -\cos$, $\int \cos = \sin$, $\int \sec^2 = \tan$. Same six, read backwards.
- **Chain rule** $\dfrac{d}{dx}f(g(x)) = f'(g(x))g'(x)$. Not on the booklet. Memorise.
- **Product rule** $(uv)' = u'v + uv'$. Not on the booklet (only the quotient rule is given). Memorise.
- **Implicit differentiation** as a *technique* (treat $y$ as $y(x)$, apply chain rule). Method, not formula.
- **Pythagorean identities** $\sin^2 + \cos^2 = 1$, $1 + \tan^2 = \sec^2$, $1 + \cot^2 = \csc^2$ — *not* on the booklet (the sum formulas are, but the basic Pythagorean are assumed).
- **Volume of revolution** $V = \pi\int y^2\,dx$ — not on the booklet, memorise.
- **SUVAT** for uniform-acceleration motion: $v = u + at$, $s = ut + \tfrac{1}{2}at^2$, $v^2 = u^2 + 2as$, $s = \tfrac{1}{2}(u + v)t$, $s = vt - \tfrac{1}{2}at^2$ — Mechanics; *none* on the 9660 booklet.

That's it. Compare to ~70 items for AP Calculus — for OxAQA 9660 Pure, the must-memorise list is roughly **15-20 items** (including SUVAT). The booklet does the rest.

---

## Net comparison across boards

| Topic | Cambridge MF19 (9709) | Edexcel IAL Pure | OxAQA 9660 | AP Calc BC |
|---|---|---|---|---|
| Standard derivative table | ✅ given (P3) | ❌ memorise | ❌ memorise (basics not on sheet) | ❌ memorise |
| $\sin^{-1}, \cos^{-1}$ derivatives | ❌ memorise (or 9231 page) | ❌ memorise | ✅ given | ❌ memorise |
| $\tan^{-1}$ derivative | ✅ given | ❌ memorise | ✅ given | ❌ memorise |
| Chain rule | ❌ memorise | ❌ memorise | ❌ memorise | ❌ memorise |
| Product rule | ✅ given | ❌ memorise | ❌ memorise | ❌ memorise |
| Quotient rule | ✅ given | ✅ given | ✅ given | ❌ memorise |
| $\int \tan x$ | ❌ memorise | ✅ given | ✅ given | ❌ memorise |
| $\int \sec x$ | ❌ memorise (Weierstrass-lite) | ✅ given | ✅ given | ❌ memorise |
| $\int 1/(x^2 + a^2) \to \arctan$ | ✅ given | ❌ memorise | ✅ given | ❌ memorise |
| $\int 1/\sqrt{a^2 - x^2} \to \arcsin$ | ❌ off-syllabus | ❌ FP3 only | ✅ given | ❌ memorise |
| Hyperbolic + inverse-hyperbolic integrals | ❌ 9231 only | ❌ FP3 only | ✅ given (Pure) | ❌ off-syllabus AB+BC |
| SUVAT | ✅ 4-of-5 given (P4 mechanics) | ❌ memorise | ❌ memorise | n/a |

**Headline:** 9660 is the most generous. AP is the least. Edexcel and Cambridge sit between, with the surprise that *they're generous in different places* — Cambridge gives $\arctan$ but not $\sec x$; Edexcel gives $\sec x$ but not $\arctan$.

---

## Connections

- **Sister cards for other boards:**
  - [[MF19 Reference (9709)]] — Cambridge 9709
  - [[Edexcel IAL Reference]] — Pearson Edexcel International A-Level
  - [[AP Calculus Reference]] — AP AB / BC (no formula sheet)
- **Per-card cross-references:** All the calculus cards now have or will have 9660 callouts: [[Standard Integrals]], [[Differentiation Rules]], [[Implicit Differentiation]], [[Parametric Differentiation]], [[Integration]], [[Integration by Parts]], [[Integration by Substitution]].
- **Topic map:** [[OxAQA-9660-Topic-Map]] — paper-by-paper coverage tracker.

---

## Receipts

- **Source:** *International AS and A-Level Mathematics: Formulae and Statistical Tables*, Oxford International AQA Examinations, 2016, 26 pages.
- **Specification:** Oxford International AQA International A-Level Mathematics (9660) — for topic-coverage / syllabus-side claims.

