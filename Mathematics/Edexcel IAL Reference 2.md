---
chinese: Edexcel IAL 公式表对照 (gōngshì biǎo duìzhào)
prerequisites: []
leads_to: []
tags:
  - subject/mathematics
  - domain/exam-strategy
  - level/A-Level
  - curriculum/Edexcel-IAL
  - type/reference
  - type/exam-technique
---

# Edexcel IAL Reference — what's given, what's yours

## What this card is for

For students taking **Pearson Edexcel International Advanced Level (IAL) Mathematics, Further Mathematics, or Pure Mathematics**: what does Edexcel hand you on exam day, and what do you have to bring in your head?

Verified against the official *Mathematical Formulae and Statistical Tables* booklet (Issue 2, January 2021), 34 pages, used for IAL examinations from January 2019 onwards.

> [!info] Cumulative inheritance — read the small print
> Each paper says *"candidates sitting [Paper X] may also require those formulae listed under [earlier papers]"*. Concretely:
> - **P2** also gets **P1**'s booklet content
> - **P3** also gets **P1 + P2**
> - **P4** also gets **P1 + P2 + P3**
> - **M1** also gets **P1 + P2** (since 2021 update)
> - **S1** also gets **P1 + P2** (since 2021 update)
> - **FP1** gets **P1 + P2**; **FP2** gets **FP1 + P1 + P2 + P3 + P4**; **FP3** gets **FP1 + FP2 + all P** (i.e. everything)
>
> So a P3 candidate has access to P1's + P2's + P3's listed formulas during the exam. The P1 booklet section is *empty* — P1 doesn't have any free formulas. Everything in P1 is yours to memorise.

The pedagogical point: Edexcel IAL's booklet is **less generous than Cambridge MF19** (which gives the inverse-trig integrals on the standard P3 page) but **vastly more generous than AP Calculus** (which gives nothing). The standard derivative table — $\sin'$, $\cos'$, $\ln'$, etc. — is *not* on the Edexcel booklet at all. You memorise those, plus integration of $1/x$, plus everything in P1's section. The booklet only kicks in seriously at P3 and above.

### 中文锚点

**Edexcel IAL 公式表**：考试时发，但比 Cambridge MF19 给得少，比 AP Calc 给得多。

- **P1**：公式表上是空的（P1 没有「免费」公式）；标准函数的导数（$\sin', \cos', \ln', e^x$ 等）必须自己背。
- **P2**：等差/等比数列、对数换底、二项级数、梯形法。
- **P3**：三角函数加法公式、积化和差、$\tan kx$ / $\sec x$ / $\cot x$ / $\csc x$ 的导数、$\int \sec^2 kx$ / $\int \tan x$ / $\int \cot x$。
- **P4**：$\int \sec x$ / $\int \csc x$ 用 Weierstrass-lite 形式给出（**这点比 MF19 还慷慨** —— 9709 学生 sec x 要自己推）；分部积分公式。

**结论**：背的东西比 9709 多（基础导数表全靠记忆），比 AP 少（trig 加法公式、级数等都给出）。

---

## How to use this card

For each paper section below:

1. **Read the "given on the IAL booklet" list first.** These are formulas you should *understand*, *be familiar with*, and *practice with* — but you don't need to memorise them.
2. **Read the "must memorise" list second.** These are the formulas, identities, and definitions that Edexcel IAL expects you to bring into the exam room.
3. **Spend more practice time on the must-memorise list.** Drilling them is pure marks.

> [!info] Other boards have different sheets
> See [[MF19 Reference (9709)]] for Cambridge 9709 + 9231 (more generous than IAL on P3 integration), and [[AP Calculus Reference]] for AP AB / BC (no formula sheet at all). What's free here may need memorising on a different paper, and what you have to memorise here may be free elsewhere.

---

## Pure Mathematics P1

### Given on the IAL booklet — P1

**Nothing.** The P1 section of the booklet is empty. *Every formula a P1 student needs is theirs to memorise or re-derive.*

### Must memorise — for Edexcel IAL P1

- **Quadratic formula** $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ — not given.
- **Discriminant** $\Delta = b^2 - 4ac$, with three sign cases.
- **Coordinate geometry:** distance, midpoint, gradient, line forms ($y = mx + c$, $y - y_1 = m(x - x_1)$).
- **Perpendicular gradient:** $m_1 m_2 = -1$.
- **Sine rule, cosine rule** in their basic form.
- **Area of triangle** $\tfrac{1}{2}ab\sin C$.
- **Circle equation** $(x - a)^2 + (y - b)^2 = r^2$.
- **Sequences and series basics:** notation, $\Sigma$, recurrence.
- **Standard derivatives** $\dfrac{d}{dx}(x^n) = nx^{n-1}$, $\dfrac{d}{dx}(\sin x) = \cos x$, etc. — **memorise the full elementary table** — see [[Differentiation Rules]].
- **Linearity, sums, constant multiples** of differentiation and integration.
- **Power Rule for integration** $\int x^n\,dx = \dfrac{x^{n+1}}{n+1} + C$.

---

## Pure Mathematics P2 (also requires P1)

### Given on the IAL booklet — P2

**Arithmetic series:**
$$u_n = a + (n - 1)d, \qquad S_n = \tfrac{1}{2}n(a + l) = \tfrac{1}{2}n[2a + (n - 1)d]$$

**Geometric series:**
$$u_n = ar^{n-1}, \qquad S_n = \dfrac{a(1 - r^n)}{1 - r}, \qquad S_\infty = \dfrac{a}{1 - r} \;\; \text{for }\lvert r \rvert < 1$$

**Logarithms — change of base:**
$$\log_a x = \dfrac{\log_b x}{\log_b a}$$

**Binomial series (positive integer $n$):**
$$(a + b)^n = a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + b^n$$

**Trapezium rule:**
$$\int_a^b y\,dx \approx \tfrac{1}{2}h\bigl[(y_0 + y_n) + 2(y_1 + \cdots + y_{n-1})\bigr], \quad h = \dfrac{b - a}{n}$$

### Must memorise — for Edexcel IAL P2

- **Index laws** ($a^m \cdot a^n = a^{m+n}$, etc.) — base-level algebra, not on booklet.
- **Logarithm laws** $\log(ab) = \log a + \log b$, $\log(a/b) = \log a - \log b$, $\log(a^n) = n\log a$ — *not on the booklet*; the change-of-base formula is given but the basic laws aren't.
- **Trig identities** $\sin^2 + \cos^2 = 1$, $1 + \tan^2 = \sec^2$, $1 + \cot^2 = \csc^2$ — none on P2 booklet.
- **Double-angle formulas** $\sin 2x = 2\sin x \cos x$, $\cos 2x = \cos^2 x - \sin^2 x$ etc. — *not on P2 booklet* (they appear on P3 booklet via the sum formulas).
- **Domain / range / inverse function** procedures — methods, not formulas.

---

## Pure Mathematics P3 (also requires P1 + P2)

### Given on the IAL booklet — P3

**Logarithms and exponentials:** $e^{x \ln a} = a^x$.

**Trigonometric identities — sum formulas (double-angle implicit):**
$$\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$$
$$\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$$
$$\tan(A \pm B) = \dfrac{\tan A \pm \tan B}{1 \mp \tan A \tan B}$$

**Sum-to-product (factor formulas):**
$$\sin A + \sin B = 2\sin\dfrac{A+B}{2}\cos\dfrac{A-B}{2}$$
$$\sin A - \sin B = 2\cos\dfrac{A+B}{2}\sin\dfrac{A-B}{2}$$
$$\cos A + \cos B = 2\cos\dfrac{A+B}{2}\cos\dfrac{A-B}{2}$$
$$\cos A - \cos B = -2\sin\dfrac{A+B}{2}\sin\dfrac{A-B}{2}$$

**Differentiation table — extended derivatives:**

| $f(x)$ | $f'(x)$ |
|---|---|
| $\tan kx$ | $k\sec^2 kx$ |
| $\sec x$ | $\sec x \tan x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\csc x$ | $-\csc x \cot x$ |
| $\dfrac{f(x)}{g(x)}$ (quotient rule) | $\dfrac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$ |

**Integration table — extended integrals:**

| $f(x)$ | $\displaystyle \int f(x)\,dx$ |
|---|---|
| $\sec^2 kx$ | $\dfrac{1}{k}\tan kx$ |
| $\tan x$ | $\ln \lvert \sec x \rvert$ |
| $\cot x$ | $\ln \lvert \sin x \rvert$ |

### Must memorise — for Edexcel IAL P3

- **Standard derivatives** $\sin'$, $\cos'$, $\ln'$, $e^{x\,\prime}$, $\tan'$ — *not on the booklet* (the extended ones $\sec, \cot, \csc$ are given, but the basics aren't!). Memorise.
- **Chain rule** $\dfrac{d}{dx}f(g(x)) = f'(g(x)) g'(x)$ — *not on the booklet*. Pure memorisation.
- **Product rule** $(fg)' = f'g + fg'$ — *not on the booklet* (the quotient rule IS, but not the product rule). Memorise.
- **Implicit differentiation** as a *technique* — not a formula. Method.
- **Standard integrals** $\int \cos x = \sin x$, $\int \sin x = -\cos x$, $\int e^x = e^x$, $\int 1/x = \ln \lvert x \rvert$ — *not on the booklet*. Memorise.
- **Integration of $\sin^2 x$ / $\cos^2 x$** via double-angle — the double-angle identity is given (via the sum formula), so this is method-recall + formula application.
- **No $\arctan$ integral on P3 booklet.** $\int \dfrac{1}{x^2 + a^2} \to \arctan$ does *not* appear in the IAL P3 booklet (contrast with [[MF19 Reference (9709)|Cambridge MF19]] where it IS given). For IAL students this lives at FP3 (further pure 3) only — see below. **For Pure-only students taking IAL P3+P4: $\int 1/(x^2+a^2)$ is yours to memorise or re-derive.**

---

## Pure Mathematics P4 (also requires P1 + P2 + P3)

### Given on the IAL booklet — P4

**Binomial series for rational $n$:**
$$(1 + x)^n = 1 + nx + \dfrac{n(n-1)}{1\cdot 2}x^2 + \cdots, \quad \lvert x \rvert < 1$$

(Repeats the P2 form with the convergence condition.)

**Integration table — special trig:**

| $f(x)$ | $\displaystyle \int f(x)\,dx$ |
|---|---|
| $\csc x$ | $-\ln \lvert \csc x + \cot x \rvert$ or $\ln\lvert\tan(x/2)\rvert$ |
| $\sec x$ | $\ln \lvert \sec x + \tan x \rvert$ or $\ln\lvert\tan(\tfrac{x}{2}+\tfrac{\pi}{4})\rvert$ |

**Integration by parts:**
$$\int u\dfrac{dv}{dx}\,dx = uv - \int v\dfrac{du}{dx}\,dx$$

> [!tip] More generous than MF19 here
> Cambridge MF19 does *not* give $\int \sec x$ or $\int \csc x$ — those are 9709 P3 students' to memorise (or derive via the Weierstrass-lite trick). Edexcel IAL's P4 booklet *gives both*, in two equivalent forms (the standard $\ln\lvert\sec x + \tan x\rvert$ and the half-angle $\ln\lvert\tan(\tfrac{x}{2} + \tfrac{\pi}{4})\rvert$). One small win for IAL students.

### Must memorise — for Edexcel IAL P4

- **Substitution method** for integration — not a formula, technique.
- **No $\arctan$ integral on the IAL P4 booklet either.** If your problem reduces to $\int 1/(x^2 + a^2)$, you derive via $u = x/a$ from the standard $\arctan$ derivative — which itself isn't on the booklet either. Net effect: P3+P4 students taking *just* Pure Mathematics need to know $\arctan$ both as a derivative *and* as an integral by heart.
- **Reduction formulas** — derived case-by-case via integration by parts; the parts formula is given.
- **Volumes of revolution** $V = \pi \int y^2\,dx$ — not on the booklet, memorise.

---

## Further Pure Mathematics — additions for FP students

### Given on FP1 booklet — selected highlights

- $\sum_{r=1}^n r^2 = \tfrac{1}{6}n(n+1)(2n+1)$
- $\sum_{r=1}^n r^3 = \tfrac{1}{4}n^2(n+1)^2$
- Newton-Raphson iteration $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$
- Conics standard forms (parabola, rectangular hyperbola)
- $2 \times 2$ rotation and reflection matrices

### Given on FP2 booklet (cumulative)

- Polar area $A = \tfrac{1}{2}\int r^2\,d\theta$
- $e^{i\theta} = \cos\theta + i\sin\theta$
- de Moivre's theorem $\{r(\cos\theta + i\sin\theta)\}^n = r^n(\cos n\theta + i\sin n\theta)$
- $n$-th roots of unity $z = e^{2\pi k i / n}$, $k = 0, 1, \ldots, n - 1$
- Maclaurin's and Taylor's series with general $r$-th term

### Given on FP3 booklet (cumulative — the big one)

- $\cosh^2 x - \sinh^2 x = 1$
- $\sinh 2x = 2\sinh x \cosh x$, $\cosh 2x = \cosh^2 x + \sinh^2 x$
- Inverse hyperbolics $\mathrm{arsinh}\,x = \ln(x + \sqrt{1 + x^2})$, $\mathrm{arcosh}\,x = \ln(x + \sqrt{x^2 - 1})$ (for $x > 1$)
- Inverse-trig and inverse-hyperbolic integrals (this is where $\arcsin / \arctan / \mathrm{arsinh} / \mathrm{arcosh}$ integrals finally appear):
  - $\int \dfrac{1}{\sqrt{a^2 - x^2}}\,dx = \arcsin\dfrac{x}{a}$
  - $\int \dfrac{1}{a^2 + x^2}\,dx = \dfrac{1}{a}\arctan\dfrac{x}{a}$
  - $\int \dfrac{1}{\sqrt{x^2 - a^2}}\,dx = \mathrm{arcosh}\dfrac{x}{a} = \ln\lvert x + \sqrt{x^2 - a^2}\rvert$ ($x > a$)
  - $\int \dfrac{1}{\sqrt{a^2 + x^2}}\,dx = \mathrm{arsinh}\dfrac{x}{a} = \ln\lvert x + \sqrt{x^2 + a^2}\rvert$
  - $\int \dfrac{1}{a^2 - x^2}\,dx = \dfrac{1}{2a}\ln\left\lvert\dfrac{a + x}{a - x}\right\rvert = \dfrac{1}{a}\mathrm{artanh}\dfrac{x}{a}$ ($\lvert x \rvert < a$)
  - $\int \dfrac{1}{x^2 - a^2}\,dx = \dfrac{1}{2a}\ln\left\lvert\dfrac{x - a}{x + a}\right\rvert$
- Vector triple product, cross product
- $3 \times 3$ matrix inverse and determinant
- Eigenvalues, eigenvectors, diagonalisation

> [!warning] The arctan integral lives on FP3, not P3
> If you're taking IAL Pure (P1–P4) only — *no Further Math* — the inverse-trig integrals are entirely yours to memorise. They're given on FP3, but FP3 is a Further Mathematics paper. **Pure-only IAL students get the smallest formula-sheet integral list of any major board.**

---

## Mechanics — selected highlights

**M1, M2** booklets: largely empty. The motion-with-uniform-acceleration formulas (SUVAT) are *not* given on the IAL Mechanics booklets at any level. **Memorise**:
- $v = u + at$, $s = ut + \tfrac{1}{2}at^2$, $v^2 = u^2 + 2as$, $s = \tfrac{1}{2}(u + v)t$, $s = vt - \tfrac{1}{2}at^2$
- Newton's laws $F = ma$ and the impulse-momentum forms.

**M3** booklet adds:
- Motion in a circle: $v = r\dot{\theta}$, transverse acc $r\ddot{\theta}$, radial acc $-r\dot{\theta}^2 = -v^2/r$.
- Centres of mass for solid hemisphere ($\tfrac{3}{8}r$ from centre), hemispherical shell ($\tfrac{1}{2}r$), solid cone ($\tfrac{1}{4}h$ above base), conical shell ($\tfrac{1}{3}h$).
- Universal law of gravitation $F = Gm_1m_2/d^2$.

---

## Statistics — selected highlights

**S1 booklet** gives:
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- $P(A \cap B) = P(A)P(B \mid A)$
- Bayes' theorem (full form)
- Discrete RV expectation and variance formulas
- Normal distribution PDF (full $\frac{1}{\sigma\sqrt{2\pi}}\exp(-\frac{1}{2}(\frac{x-\mu}{\sigma})^2)$ form)

**Must memorise (S1):** standard normal table reading rules; binomial PMF $\binom{n}{r}p^r(1-p)^{n-r}$ (the formula isn't given as a one-liner); geometric PMF; chi-square procedure (S2); regression-line procedures (the Sxx, Syy, Sxy formulas ARE given).

---

## Net memorise-list summary for Edexcel IAL students

For a typical **Pure-Mathematics-only** (P1–P4) candidate:

- **Standard derivative table** (basic 6: $\sin, \cos, \tan, e^x, \ln, x^n$) — memorise; not on booklet
- **Standard integral table** (the same 6 read backwards, plus $1/x \to \ln \lvert x \rvert$) — memorise
- **Chain rule, product rule** — memorise
- **All trig identities** in P1–P2 zone (Pythagorean, double-angle, half-angle) — memorise
- **All log laws** in basic form — memorise
- **SUVAT** — memorise
- **Inverse-trig integrals** ($\arctan$, $\arcsin$ family) — memorise (or derive on the day; they're not on Pure-only booklet)
- **Volumes of revolution** — memorise

For a **Further Mathematics** candidate (FP1–FP3 added): inverse-trig and inverse-hyperbolic integrals are given on FP3, dramatically reducing the memorise stack — but FP1's series sums and FP2's complex-roots / Maclaurin-Taylor general forms still need familiarity.

**Headline contrast:** if you take just Pure Mathematics IAL (P1–P4), your formula booklet is *less generous* than Cambridge MF19's main P3 page on inverse-trig integrals (the booklet keeps these for FP3 students only). If you take IAL Further Mathematics, FP3's booklet *exceeds* MF19 in scope (full inverse-hyperbolic integral table, vector triple product, $3 \times 3$ matrix inverse).

---

## Connections

- **Sister cards for other boards:**
  - [[MF19 Reference (9709)]] — Cambridge 9709. *More generous than IAL on P3 integration* (gives $\arctan$ integral directly).
  - [[AP Calculus Reference]] — AP AB / BC. *No formula sheet at all*; everything is yours.
  - *Forthcoming:* [[OxAQA 9660 Reference]] for International A-Level via OxfordAQA.
- **Per-card cross-references:** All the calculus cards now have or will have IAL callouts: [[Standard Integrals]], [[Differentiation Rules]], [[Implicit Differentiation]], [[Parametric Differentiation]], [[Integration]], [[Integration by Parts]], [[Integration by Substitution]].
- **Topic map:** [[Edexcel-IAL-Topic-Map]] — paper-by-paper coverage tracker.

---

## Receipts

- **Source:** *Mathematical Formulae and Statistical Tables for Pearson Edexcel International AS/AL in Mathematics, Further Mathematics and Pure Mathematics* (Issue 2, January 2021). 34 pages. First examination from January 2019.
- **Specification:** Pearson Edexcel International A-Level Mathematics (YMA01) — for topic-coverage / syllabus-side claims. (Different document; the spec says *what* is examined, the formula book says *what's given on the day*.)

