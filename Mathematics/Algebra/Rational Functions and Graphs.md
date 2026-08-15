---
chinese: 有理函数及其图像 (yǒulǐ hánshù jí qí túxiàng)
prerequisites:
  - "[[Quadratic Equations]]"
  - "[[Polynomial Division]]"
  - "[[Modulus Function]]"
  - "[[Differentiation]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/algebra
  - level/A-Level
  - curriculum/A-Level
  - curriculum/Cambridge-9231
  - curriculum/AP
  - syllabus/9231-1-2
  - type/deep
  - type/definition
  - type/proof
  - notation/asymptote
  - misconception/curves-never-cross-asymptotes
  - misconception/asymptote-means-unreachable-value
  - misconception/discriminant-leading-coefficient-zero
  - misconception/one-over-f-flips-everything
---

# Rational Functions and Graphs 有理函数及其图像

> *Here is a function with a hole in its diet: $y = \dfrac{4x^2+x+1}{2x^2-7x+3}$ takes the value $5$, takes the value $0.2$, takes every value you like above $\tfrac15$ or below $-3$ — and **never, for any $x$ on the entire real line, takes any value between them**. There is a horizontal band of forbidden heights, and the curve leaps it.*
>
> *Stranger still, you can find that band with no calculus at all — a quadratic discriminant does it — and the band's two edges turn out to be exactly the curve's turning values. One method, three questions answered at once. That economy is what this topic is really teaching, underneath the sketching.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| rational function | 有理函数 | a polynomial divided by a polynomial |
| asymptote | 渐近线 | a line the curve approaches ever more closely |
| vertical asymptote | 垂直渐近线 | where the denominator dies and $y$ blows up |
| horizontal asymptote | 水平渐近线 | the height the curve settles at as $x \to \pm\infty$ |
| oblique asymptote | 斜渐近线 | a slanted settling line, when the numerator is one degree heavier |
| branch | 分支 | one connected piece of the curve between asymptotes |
| stationary point | 驻点 | where the gradient is zero |
| set of values / range | 值域 | the heights the function actually attains |

## What a rational function is, and where its drama lives

A **rational function** is one polynomial divided by another. This page handles the syllabus's stated territory — numerator and denominator of degree at most 2 — which is already enough for every behaviour that matters.

All the drama comes from the denominator's zeros and from what happens far away:

- **Where the denominator is zero** (and the numerator is not), the function has no value and the curve has a **vertical asymptote**: approaching from one side, $y \to +\infty$ or $-\infty$.
- **Far away**, the highest powers dominate and the curve settles toward a line — horizontal or slanted.

The far-away behaviour is not three separate rules but one act of [[Polynomial Division|division]]:

| Degrees | Divide and see | Far-away behaviour |
|---|---|---|
| top < bottom | $\dfrac{x+1}{x^2+3} \to$ small | horizontal asymptote $y = 0$ |
| top = bottom | $\dfrac{4x^2+x+1}{2x^2-7x+3} = 2 + \dfrac{15x-5}{2x^2-7x+3}$ | horizontal asymptote $y = 2$ — the ratio of leading coefficients |
| top = bottom + 1 | $\dfrac{x^2+3}{x-1} = x + 1 + \dfrac{4}{x-1}$ | **oblique asymptote** $y = x+1$ — the quotient |

The pattern in one sentence: **divide out, and the quotient is the asymptote; the remainder term is the part that dies at infinity.** Nothing here is new machinery — it is long division doing geometry.

![[rational-oblique-asymptote.svg|760]]

> [!warning] Curves cross their own asymptotes — horizontal and oblique ones, freely
> "The curve never touches the asymptote" is folklore imported from vertical asymptotes, where it *is* true (the function has no value there at all). A horizontal or oblique asymptote only describes where the curve is heading **as $x \to \pm\infty$** — in the middle of the picture the curve may cross it, and often does. Our specimen crosses $y = 2$ at $x = \tfrac13$: set $f(x) = 2$ and a perfectly ordinary solution falls out. An asymptote is a destination, not a fence.

## The discriminant method — the range without calculus

Here is the topic's best idea, and the syllabus names it: *determination of the set of values taken by the function, e.g. by the use of a discriminant.*

**Flip the question.** Instead of "what is $y$ for this $x$?", ask: **for which $y$ does a real $x$ exist at all?** Set $y$ equal to the function and clear the denominator:

$$y = \frac{4x^2+x+1}{2x^2-7x+3} \quad\Longrightarrow\quad (2y-4)\,x^2 - (7y+1)\,x + (3y-1) = 0$$

Read this as **a quadratic in $x$ whose coefficients contain $y$**. A height $y$ is attained by the curve exactly when this quadratic has a real root — that is, when its [[Quadratic Equations|discriminant]] is non-negative:

$$(7y+1)^2 - 4(2y-4)(3y-1) \geq 0 \quad\Longrightarrow\quad 5(y+3)(5y-1) \geq 0 \quad\Longrightarrow\quad y \leq -3 \ \text{ or } \ y \geq \tfrac15$$

![[rational-forbidden-band.svg|860]]

**Three answers from one computation:**

1. **The set of values**: everything except the open band $-3 < y < \tfrac15$.
2. **The turning values, free of charge**: at the band's edges the discriminant is *zero* — the horizontal line $y = -3$ meets the curve at exactly one (repeated) $x$, which is what it means to sit level at a turning point. So $y = -3$ and $y = \tfrac15$ are the stationary values, found without differentiating. (The repeated root of the quadratic then hands you the $x$-coordinate too.)
3. **A sketch's skeleton**: which horizontal strips contain curve and which are empty.

> [!warning] The one care the method demands: the leading coefficient can vanish
> At $y = 2$ the "$x^2$" coefficient $2y - 4$ is zero, and the equation is not a quadratic but linear — $-15x + 5 = 0$, giving $x = \tfrac13$. A discriminant argument does not apply to a linear equation, so **test this value separately**: here $y = 2$ *is* attained (it is the asymptote-crossing from the callout above). The degenerate value is always the horizontal asymptote's height — here $y = 2$ — which is a satisfying consistency check rather than a coincidence: near that height, one of the quadratic's two roots is finite and the other has marched off to infinity, so the $x^2$ term has nothing left to do.

## Sketching — a workflow, worked on a real question

**9231 Paper 13, November 2024, Q6** — the same paper whose Q3, Q4 and Q5 anchor [[Symmetric Functions of Roots]], [[Summation of Series]] and [[Polar Coordinates]]. Four consecutive questions, four cards.

> *The curve $C$ has equation $y = \dfrac{4x^2+x+1}{2x^2-7x+3}$.*
> *(a) Find the equations of the asymptotes of $C$.* [2]

**Tool: factorise the denominator; divide for the far field.** $2x^2-7x+3 = (2x-1)(x-3)$, so vertical asymptotes $x = \tfrac12$ and $x = 3$. Equal degrees, so the horizontal asymptote is the ratio of leading coefficients: $y = \tfrac42 = 2$.

> *(b) Find the coordinates of any stationary points on $C$.* [4]

**Tool: the quotient rule — or the discriminant method above.** The official route differentiates:

$$\frac{\mathrm dy}{\mathrm dx} = \frac{(2x^2-7x+3)(8x+1) - (4x^2+x+1)(4x-7)}{(2x^2-7x+3)^2}$$

The numerator collapses (it is worth trusting the collapse and collecting carefully) to $-10(x-1)(3x+1)$, giving stationary points at

$$\left(-\tfrac13,\ \tfrac15\right) \quad\text{and}\quad (1,\ -3)$$

— precisely the band edges the discriminant found. On the actual paper, doing (b) by the discriminant is legitimate and faster *if* you also recover the $x$-values from the repeated root; the derivative route is the safe default when the question says "stationary".

> *(c) Sketch $C$, stating the coordinates of any intersections with the axes.* [5]

**Tool: assemble what is already known, then fix each branch's sign.** Intersections: $x = 0$ gives $\left(0, \tfrac13\right)$; the numerator $4x^2+x+1$ has discriminant $-15 < 0$, so the curve **never crosses the $x$-axis**. Three branches:

- **Left** ($x < \tfrac12$): comes in along $y = 2$ from below, dips to the minimum $\left(-\tfrac13, \tfrac15\right)$, rises through $\left(0,\tfrac13\right)$, crosses $y=2$ at $x=\tfrac13$, and climbs to $+\infty$ at the asymptote.
- **Middle** ($\tfrac12 < x < 3$): a downward tongue from $-\infty$ up to its maximum $(1, -3)$ and back — entirely below $y = -3$'s level or touching it, consistent with the forbidden band.
- **Right** ($x > 3$): falls from $+\infty$ and settles onto $y = 2$ from above.

![[rational-n24-curve.svg|880]]

The five marks are distributed across exactly these features — asymptotes drawn and labelled, branch shapes approaching them correctly, turning points marked, the axis intersection stated. A sketch that is "roughly right" but missing labels leaves marks on the table; the syllabus's own wording asks for *significant features: turning points, asymptotes and intersections with the axes*.

## The four relatives

The second learning objective: relate the graph of $y = f(x)$ to those of $y^2 = f(x)$, $y = \dfrac{1}{f(x)}$, $y = \lvert f(x)\rvert$ and $y = f(\lvert x\rvert)$. None of these is a fresh sketch — each is a **rule applied to the sketch you already have**:

| Relative | The rule | The details that carry marks |
|---|---|---|
| $y^2 = f(x)$ | exists only where $f \geq 0$; there, plot $\pm\sqrt{f}$ | symmetric in the $x$-axis; heights are square-rooted, so big values are tamed and values below 1 are lifted; meets $y=0$ *vertically* where $f$ crosses zero |
| $y = \dfrac{1}{f}$ | reciprocal pointwise | zeros of $f$ become vertical asymptotes and vice versa; horizontal asymptote $y = c$ becomes $y = \tfrac1c$; where $f$ has a max, $\tfrac1f$ has a min (same $x$); the sign of each branch is preserved |
| $y = \lvert f(x)\rvert$ | reflect everything below the axis upward | from [[Modulus Function]]; creases appear where $f$ crossed zero — here $f$ never does, so the reflected middle tongue simply flips to sit above |
| $y = f(\lvert x\rvert)$ | keep $x \geq 0$, mirror it to the left | the original left half is *discarded*; the result is always symmetric in the $y$-axis |

![[rational-four-relatives.svg|900]]

> *(d) Sketch the curve with equation $y = \left\lvert \dfrac{4x^2+x+1}{2x^2-7x+3} \right\rvert$ and state the set of values of $k$ for which $\left\lvert \dfrac{4x^2+x+1}{2x^2-7x+3} \right\rvert = k$ has 4 distinct real solutions.* [2]

**Tool: the $\lvert f\rvert$ rule, then count crossings of a sliding horizontal line.** The middle tongue reflects up: it now *descends* from $+\infty$ to a **minimum at $(1, 3)$** and returns to $+\infty$. The left branch (all positive already) spans $\left[\tfrac15, \infty\right)$; the right branch spans $(2, \infty)$.

Slide the line $y = k$ upward and count intersections: for $k > 3$ the line cuts the reflected tongue **twice**, the left branch once (on its climb to the asymptote), and the right branch once — four. At $k = 3$ exactly, the line is *tangent* to the tongue, and the count drops to three. So:

$$\boxed{\ k > 3\ }$$

— strict inequality, and the tangency at $k = 3$ is precisely why. (Checking the boundary case is the whole of the second mark.)

## Where the forbidden band meets the world

Rational functions are not exam furniture — they are the standard shape of **response curves**, wherever an effect saturates or resonates.

**Saturation.** An enzyme is a biological machine that processes one specific molecule — its **substrate** (底物: the *raw material* the enzyme works on, not 受体, which is a receptor). The processing rate follows the Michaelis–Menten law

$$v = \frac{V_{\max}\,S}{K_m + S}$$

where $S$ is the substrate concentration, $V_{\max}$ is the **maximum possible rate** — the speed when every enzyme molecule is busy — and $K_m$, the *Michaelis constant*, is the concentration at which the rate reaches **half** of $V_{\max}$ (small $K_m$ = the enzyme saturates easily). It is a rational function of $S$, and its horizontal asymptote at $V_{\max}$ *is* the biology: once every machine is occupied, more raw material cannot buy more speed. That is why doubling a drug dose does not double its effect, and the same saturating shape prices everything from drug design to fermentation tanks.

**Resonance.** An audio equaliser's frequency response — the curve a producer drags around in a plug-in window — is the magnitude of a rational function $H$ of frequency; designing the filter *is* choosing its numerator and denominator. The figure's right panel is a real one: a **peaking EQ** boosting $+12$ dB at $1\,$kHz, drawn at two settings of the **Q** knob. Q is resonance sharpness, and underneath the knob it is literally *how close the denominator's roots sit to producing a vertical asymptote* — push Q up and the boost narrows and steepens toward a spike; the far-field flatness on both sides is a horizontal asymptote at $0$ dB. Anyone who has swept a filter has been sketching rational functions by ear.

![[rational-real-world.svg|880]]

## Common misconceptions (teaching notes)

### 1. "A curve can never cross an asymptote"

True for vertical asymptotes, false in general — and students who hold it will "correct" a right answer.

**Fix:** have them solve $f(x) = 2$ on the specimen. A clean $x = \tfrac13$ appears, and the sketch shows the crossing. Then restate what an asymptote claims: it describes the *ends* of the journey, not the middle.

### 2. "The horizontal asymptote's value is never attained"

The subtler version of the same error — conflating "asymptote" with "excluded value". The excluded values are the forbidden band, and the asymptote height can lie *outside* it.

**Fix:** the discriminant method makes this concrete: $y = 2$ fails the *quadratic* test only because it is not a quadratic there — the separate linear check shows it is attained. Excluded heights come from the discriminant being negative, not from being an asymptote.

### 3. Forgetting the degenerate case in the discriminant method

Applying $b^2 - 4ac \geq 0$ blindly when the leading coefficient $2y-4$ can vanish.

**Fix:** make "check the $y$ that kills the $x^2$ coefficient" a fixed final step of the method — it is always the horizontal asymptote's height, so it is easy to know in advance which value needs the separate test.

### 4. "$1/f$ turns the graph upside down"

Reciprocal confused with negation. $1/f$ preserves signs: positive branches stay positive.

**Fix:** three anchor values — $f = 2 \Rightarrow \tfrac1f = \tfrac12$ (same side, squashed), $f = \tfrac15 \Rightarrow 5$ (same side, stretched), $f \to 0^+ \Rightarrow \tfrac1f \to +\infty$. Big and small swap; sides do not.

### 5. In $y^2 = f(x)$, drawing curve where $f < 0$

The square of a real number cannot be negative, so those stretches are empty — the same "no curve here" discipline as the $r \geqslant 0$ convention in [[Polar Coordinates]].

**Fix:** shade the regions where $f < 0$ *first*, before plotting anything, and only then take square roots in what survives.

## Exam Notes

### Cambridge 9231 Further Mathematics — **Further Pure 1, Paper 1**

**§1.2** appears on most Paper 1 variants, typically as one substantial question of 8–13 marks. Two learning objectives:

- **Sketch simple rational functions** (degrees at most 2 over at most 2), *including determination of oblique asymptotes* and *the set of values taken by the function, e.g. by the use of a discriminant*. The syllabus's own sketch checklist: *turning points, asymptotes and intersections with the axes* — and *detailed plotting will not be required*.
- **Understand and use the relationships** between $y = f(x)$ and $y^2 = f(x)$, $y = \dfrac1{f(x)}$, $y = \lvert f(x)\rvert$, $y = f(\lvert x\rvert)$ — *including use of such sketch graphs in the course of solving equations or inequalities*, which is where the sliding-line count of part (d) lives.

**Recurring shapes:** find the asymptotes (2); stationary points by differentiation or discriminant (3–4); the labelled sketch (3–5); one relative sketched from it plus a "for which $k$…" count (2–4). The relative most often asked is $\lvert f \rvert$ or $y^2 = f$; the count question hinges on a tangency at the boundary value, so **always test the boundary $k$ separately** — the strict-vs-inclusive inequality is routinely the final mark.

- **MF19 prints nothing for this section** — no asymptote rules, no discriminant method. See [[MF19 Reference (9231)]].
- The quotient-rule numerator in (b)-type parts is deliberately collapse-prone; expand *and collect* before factorising, and expect a common factor.

### AP

**AP Precalculus** covers this ground closely in **Unit 1** (Polynomial and Rational Functions, §1.7–1.11): vertical, horizontal *and slant* asymptotes, end behaviour via the degree comparison, and one idea Cambridge does not examine — **holes** (removable discontinuities, where a factor cancels top and bottom, so the curve is missing a single point rather than owning an asymptote). **AP Calculus** then re-derives asymptotes as limits: a vertical asymptote is $\lim_{x\to a} f = \pm\infty$, a horizontal one is $\lim_{x\to\pm\infty} f = L$. The four-relatives material and the discriminant range method are not AP topics — they are the genuinely Further-flavoured part of this page.

### Where this is *not* examined

**Not on Cambridge 9709** in this generality — P1 sketches quadratics and P3 handles rational expressions through [[Partial Fractions]] for calculus, but general curve-sketching of rational functions with the four relatives is Further-only. **Not on IB AA** (asymptote work appears there only for simple reciprocal and exponential shapes). Edexcel and AQA Further place the same material in their FP/Core Pure papers.

> [!info] Beyond syllabus — poles, and the view from the complex plane
> Engineering calls a vertical asymptote's location a **pole**, and the name opens a door. Allow $x$ to be complex, and our specimen's denominator $2x^2-7x+3$ has its roots — the poles — on the real axis at $\tfrac12$ and $3$. The EQ filter of the real-world section has its poles just *off* the real axis, and the distance from the pole to the axis sets how sharp the resonance is: the filter designer's "Q" knob literally slides a pair of complex roots toward or away from the axis. The whole subject of which rational functions make *stable* systems — every pole safely in the left half of the [[Complex Numbers|complex plane]] — is control theory's bread and butter, and it is this page's asymptote analysis, grown up.

## Connections

- **Built on:** [[Polynomial Division]] — the quotient *is* the far-field asymptote, oblique ones included; [[Quadratic Equations]] — the discriminant, promoted from solving quadratics to mapping a curve's attainable heights; [[Modulus Function]] — the reflection rules that $\lvert f\rvert$ and $f(\lvert x\rvert)$ apply wholesale.
- **Sibling:** [[Cubic Graphs]] — the polynomial half of Further curve-sketching; there the drama is turning points, here it is asymptotes.
- **Same discipline:** [[Polar Coordinates]] — "no curve where the defining quantity is negative" appears there as the $r \geqslant 0$ convention and here in $y^2 = f(x)$.
- **Where the ideas grow:** [[Partial Fractions]] — the same divide-and-decompose instinct pointed at integration; [[Complex Numbers]] — poles move into the plane and become resonance and stability.
- **For 9231 students:** [[MF19 Reference (9231)]] — nothing on this section is printed.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{4x^2+x+1}{2x^2-7x+3}$ | `\dfrac{4x^2+x+1}{2x^2-7x+3}` | display-size fraction for rational functions |
| $y^2 = f(x)$ | `y^2 = f(x)` | the square-both-sides relative |
| $\lvert f(x) \rvert$ | `\lvert f(x) \rvert` | required inside tables — a bare `\|` breaks the row |
| $x \to \pm\infty$ | `x \to \pm\infty` | far-field behaviour |
| $b^2 - 4ac$ | `b^2 - 4ac` | the discriminant, applied to a quadratic *in $x$ with $y$ in its coefficients* |
