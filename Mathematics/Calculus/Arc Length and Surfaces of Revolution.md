---
chinese: 弧长与旋转曲面面积 (húcháng yǔ xuánzhuǎn qūmiàn miànjī)
prerequisites:
  - "[[Integration]]"
  - "[[Pythagoras Theorem]]"
  - "[[Parametric Differentiation]]"
  - "[[Polar Coordinates]]"
  - "[[Hyperbolic Functions]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/calculus
  - domain/geometry
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/AP
  - syllabus/9231-2-4
  - type/technique
  - type/proof
  - notation/integral
  - misconception/2piy-dx
  - misconception/root-outside-the-sum
---

# Arc Length and Surfaces of Revolution 弧长与旋转曲面面积

> *How long is a winding mountain road? The map's ruler lies — it measures the crow's flight. The odometer knows: it measures the road by rolling along it, adding up thousands of tiny, almost-straight steps. Every formula on this page is that odometer written in calculus: chop the curve into slivers so short they are straight, measure each with [[Pythagoras Theorem|Pythagoras]], add them all with an integral.*

## Definition

### Formal

For a curve traced from one point to another, the **arc length** is

$$s = \int ds, \qquad ds = \sqrt{dx^2 + dy^2}$$

— the integral of the straight-line length of infinitesimal steps. Rotating the curve about the $x$-axis sweeps each sliver into a thin band; the **surface of revolution** has area

$$S = \int 2\pi y \, ds$$

(replace $y$ by $x$ for rotation about the $y$-axis). Everything else in the topic is $ds$ changing costume to match how the curve is described.

### Intuitive

$ds$ is one tiny step of the odometer. Zoom in far enough and any smooth curve is straight, so the step is the hypotenuse of a right triangle with legs $dx$ and $dy$ — Pythagoras, applied infinitely often.

Watch it happen — the clip below is the whole argument with no algebra: one chord is the map's ruler and lies short; doubling the chords walks the total up onto the road's true length; and magnifying one strip shows *why* — the arc flattens onto its chord, so Pythagoras on the chord, summed over every chord, becomes the integral.

![[arc-length-odometer.mp4]]

For the surface: each straight sliver, swung around the axis, sweeps a thin hoop of circumference $2\pi y$ (its distance from the axis sets the radius) and width $ds$ — *width along the slope, not along the axis*, which is the whole subtlety of the topic and the source of its classic error.

### 中文锚点 (Chinese Anchor)

弯路有多长？地图上的直尺量的是**直线距离**（英文里正是 as the crow flies），汽车的**里程表**才知道真相：它把路切成无数几乎笔直的小段，每段用**勾股定理**量斜边 $ds = \sqrt{dx^2 + dy^2}$，再全部加起来——这就是弧长积分。曲线怎么给，$ds$ 就换什么衣服：直角坐标下 $ds = \sqrt{1 + (y')^2}\,dx$；参数方程下 $ds = \sqrt{\dot x^2 + \dot y^2}\,dt$（这件其实是"本体"，直角坐标只是 $t = x$ 的特例）；极坐标下 $ds = \sqrt{r^2 + (r')^2}\,d\theta$。**旋转曲面面积**再多一步：每一小段绕轴转一圈，扫出一条细箍，周长 $2\pi y$（离轴多远，半径就是多少），宽是 $ds$，所以 $S = \int 2\pi y\,ds$。**最经典的错误**是把宽写成 $dx$：斜着的一段扫出的箍，宽是斜长 $ds$，不是它在轴上的投影 $dx$——拿圆锥一验就露馅（正确公式给 $\pi r l$，错的给 $\pi r h$）。考试三件套：把 $ds$ 穿对衣服、根号里先配方凑成完全平方再开根（出题人几乎总把曲线设计成能凑出完全平方）、答案要**精确值**。

## The costumes of $ds$ — one formula, three coordinate systems

*Tool: factor the appropriate differential out of $\sqrt{dx^2 + dy^2}$.*

**Cartesian** ($y$ given as a function of $x$): factor out $dx$ —

$$ds = \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\, dx \qquad\Longrightarrow\qquad s = \int_a^b \sqrt{1 + (y')^2}\, dx.$$

**Parametric** ($x(t)$, $y(t)$): factor out $dt$ —

$$ds = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt.$$

This is the *primary* form — the odometer's own view, a position changing with time — and the Cartesian formula is just the costume it wears when the parameter happens to be $x$ itself ($\frac{dx}{dx} = 1$ gives the $1$ under the root).

**Polar** ($r$ given as a function of $\theta$): the curve is the parametric curve $x = r\cos\theta$, $y = r\sin\theta$ with parameter $\theta$. Differentiate both (product rule), square, add — and watch the cross terms kill each other:

$$\dot x = r'\cos\theta - r\sin\theta, \quad \dot y = r'\sin\theta + r\cos\theta \qquad\Longrightarrow\qquad \dot x^2 + \dot y^2 = (r')^2 + r^2$$

(the $\pm 2rr'\sin\theta\cos\theta$ terms cancel; $\cos^2 + \sin^2 = 1$ twice). Hence the polar costume:

$$s = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\; d\theta.$$

> [!tip] The examiner's perfect square
> Raw arc-length integrands are usually unintegrable — so exam curves are engineered to make $1 + (y')^2$ or $r^2 + (r')^2$ collapse into a **perfect square** under the root. Expect it, hunt for it, and treat a root that refuses to simplify as a sign of an arithmetic slip upstream. The catenary is the archetype: $y = \cosh x$ has $1 + \sinh^2 x = \cosh^2 x$ ([[Hyperbolic Functions]]), so $s = \int \cosh x\, dx = \sinh b - \sinh a$ — the curve whose *length* is as clean as its formula, which is why it shows up in every syllabus.

### Worked — a real Paper 2 question, complete

*The curve $C$ has polar equation $r = e^{3\theta/4}$ for $0 \leq \theta \leq \pi$. Find the length of $C$, giving your answer in exact form.* [4]

*Tool: the polar costume.* $\dfrac{dr}{d\theta} = \tfrac{3}{4}e^{3\theta/4}$, so

$$r^2 + \left(\frac{dr}{d\theta}\right)^2 = e^{3\theta/2} + \tfrac{9}{16}e^{3\theta/2} = \tfrac{25}{16}\,e^{3\theta/2}$$

— the perfect square arrives on schedule. Root it and integrate:

$$s = \int_0^\pi \tfrac{5}{4} e^{3\theta/4}\, d\theta = \tfrac{5}{4}\cdot\tfrac{4}{3}\Big[e^{3\theta/4}\Big]_0^\pi = \boxed{\ \tfrac{5}{3}\left(e^{3\pi/4} - 1\right)\ }$$

("Exact form" bars the calculator decimal; the mark scheme's A1 says *must be exact*.)

## Surfaces of revolution — and why the width is $ds$, not $dx$

Swing the sliver around the $x$-axis: it sweeps a thin band — a slice of a cone (a **frustum**), not a cylinder, because the sliver is tilted. The band's area is (circumference at its radius) × (its *slant* width):

$$dS = 2\pi y \, ds \qquad\Longrightarrow\qquad S = \int 2\pi y\, \sqrt{1 + (y')^2}\, dx \quad\text{(or the parametric costume with } dt\text{)}.$$

**Why not $2\pi y\,dx$?** Because a tilted ribbon is wider than its shadow. The cone catches the error red-handed: rotate $y = \frac{r}{h}x$ for $0 \leq x \leq h$. The truth (unroll the cone flat) is $\pi r l$ with slant $l = \sqrt{r^2 + h^2}$; the formula with $ds$ delivers exactly that, while $\int 2\pi y\,dx$ gives $\pi r h$ — too small, always, because every shadow is shorter than its ribbon. For area under a curve the analogous slant correction *vanishes* in the limit (the error is second-order); for arc length and surfaces it is first-order and **never** goes away. That asymmetry is the deepest fact in the topic.

Watch the argument in three dimensions — the curve spun into its surface, one tilted sliver swung into its band with the shadow cylinder sitting inside it, and the cone test with the cone unrolled into its sector ($\pi r l$ against the shadow's $\pi r h$):

![[surface-revolution-ribbon.mp4]]

![[arc-length-sliver.svg|760]]

> [!info] Beyond syllabus — Archimedes' hat-box
> Run the sphere: $x^2 + y^2 = a^2$ rotated gives, over any band $x \in [c, c+w]$, the surface area $2\pi a w$ — **depending only on the width $w$, not on where the band sits**. The steep bits near the poles sit *nearer* the axis (a smaller hoop) but are *more tilted* (a wider band), and the two effects cancel *exactly*. Archimedes knew: a sphere and its enclosing cylinder have equal-height bands of equal area (his tombstone carried the figure). It is also why the total is the famous $4\pi a^2$ — and why equal-area world maps (the Lambert cylindrical projection) work at all.

### Worked — a real Paper 2 surface question, the hard end

*The curve $y = \tanh x$, from $x = 0$ to $x = \frac12\ln 3$, is rotated through one revolution about the $x$-axis. (i) Use the substitution $u = \sqrt{1 + \operatorname{sech}^4 x}$ to show that $S = \pi\displaystyle\int_{5/4}^{\sqrt 2} \frac{u^2}{u^2 - 1}\, du$. (ii) Hence find $S$ exactly.*

*Tool: the surface formula, Cartesian costume.* $y' = \operatorname{sech}^2 x$, so

$$S = 2\pi \int_0^{\frac12\ln 3} \tanh x\, \sqrt{1 + \operatorname{sech}^4 x}\; dx.$$

*Tool: the given substitution — differentiate it, and hunt the integrand's pieces.* From $u^2 = 1 + \operatorname{sech}^4 x$: $\ 2u\,du = -4\operatorname{sech}^4 x \tanh x \, dx$, so $\tanh x\,dx = -\dfrac{u\,du}{2(u^2 - 1)}$ (using $\operatorname{sech}^4 x = u^2 - 1$). Limits ([[Hyperbolic Functions]] arithmetic): $x = 0 \Rightarrow u = \sqrt 2$; $x = \frac12\ln 3 \Rightarrow \cosh x = \frac{2}{\sqrt3} \Rightarrow \operatorname{sech}^4 x = \frac{9}{16} \Rightarrow u = \frac54$. Substituting (the minus sign flips the limits back to increasing order):

$$S = 2\pi\int_{\sqrt2}^{5/4} u \cdot \left(-\frac{u}{2(u^2-1)}\right) du = \pi\int_{5/4}^{\sqrt 2} \frac{u^2}{u^2 - 1}\, du. \qquad\blacksquare$$

*(ii) Tool: split off the polynomial part, then partial fractions ([[Standard Integrals]]).* $\dfrac{u^2}{u^2-1} = 1 + \dfrac{1}{u^2-1} = 1 + \tfrac12\left(\dfrac{1}{u-1} - \dfrac{1}{u+1}\right)$:

$$S = \pi\left[u + \tfrac12\ln\frac{u-1}{u+1}\right]_{5/4}^{\sqrt2} = \pi\left(\sqrt2 - \tfrac54 + \ln 3 + \ln(\sqrt2 - 1)\right) = \boxed{\ \pi\left(\sqrt2 - \tfrac54 + \ln\big(3(\sqrt2 - 1)\big)\right)\ }$$

using $\frac{\sqrt2-1}{\sqrt2+1} = (\sqrt2-1)^2$ at the top limit and $\frac{1/4}{9/4} = \frac19$ at the bottom ($\approx 1.198$ — positive and modest, as a small band ought to be). This is the syllabus's warning made flesh: *"questions may require techniques from A Level Mathematics applied to more difficult cases"* — the surface formula opened the door, but hyperbolic identities, substitution discipline and partial fractions carried the marks.

## Where this is the working tool

- **Your phone's run tracker computes parametric arc length, live.** GPS hands it positions $(x(t), y(t))$ a few times a second; the app sums $\sqrt{\Delta x^2 + \Delta y^2}$ — the parametric $ds$ with real data instead of formulas. Every "5.2 km" on a fitness screen is this topic running in production.
- **The catenary's length is a purchase order.** Suspension-bridge main cables and high-voltage transmission lines hang as catenaries ($y = a\cosh\frac{x}{a}$); the steel or aluminium ordered is the *arc length*, not the span — and thanks to the perfect square, engineers get it in closed form, $s = a\sinh\frac{x}{a}$ per half-span.
- **Surface area is what paint, plating and heat-loss actually see.** A turned chair leg, a rocket nose cone, a vacuum flask — anything made on a lathe is a surface of revolution, and coating cost, chrome-plating current and radiative heat loss all scale with $\int 2\pi y\,ds$. CAD software evaluates precisely these integrals (numerically) every time it reports "surface area".

## Common Misconceptions (Teaching Notes)

### 1. $S = \int 2\pi y \, dx$

The shadow instead of the ribbon — the single most common error in the topic, and it *feels* right by analogy with volumes ($\pi y^2 dx$ works!).

**Fix:** the cone test, thirty seconds: the wrong formula gives $\pi r h$, reality (unroll it) says $\pi r l$. And the reason volumes escape: the discs' volume error is second-order and vanishes in the limit; the bands' width error is first-order and does not. Slant matters for *length-like* quantities, never for *bulk*.

### 2. The root taken term by term

$\sqrt{\dot x^2 + \dot y^2}$ mangled into $\dot x + \dot y$, or $\sqrt{1 + (y')^2}$ into $1 + y'$ — Pythagoras does not distribute.

**Fix:** the root only ever simplifies through a **perfect square inside** — and exam curves are built to provide one. Compute $\dot x^2 + \dot y^2$ fully, *then* factor, *then* root.

### 3. Polar arc length with the wrong ingredients

Reaching for $\frac{dy}{dx}$ on a polar curve, or quoting $r^2 + r'^2$ with $r'$ meaning $\frac{dr}{dx}$.

**Fix:** in polar costume everything is a function of $\theta$: the formula is $\sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$, derived in one line from the parametric form — re-derive it (the cross-terms cancel) rather than trusting memory. And remember the boundary: **polar surfaces of revolution are explicitly not required** — arc length is polar's only duty here.

### 4. Exact-form answers surrendered to the calculator

$\frac53(e^{3\pi/4} - 1)$ reported as $16.14$. The A1 dies.

**Fix:** "exact form" is an instruction about the *shape* of the answer; the calculator's only legal role is the plausibility check afterwards.

## Exam Notes

### Cambridge 9231 (Further Pure 2, Paper 2 — §2.4)

- Arc length in all three costumes (Cartesian, parametric, polar); surfaces of revolution about either axis in Cartesian or parametric form only — **polar surfaces are excluded by the syllabus in so many words**, so a polar curve question wanting area is asking for the sector formula ([[Polar Coordinates]]), not a surface.
- The syllabus's boundary note is a warning label: harder 9709 techniques (integration by parts for $\int e^x \sin x$, the $t = \tan\frac{x}{2}$ substitution) may sit *inside* these questions. The formula is one mark; the integration is the question.
- Recent real questions: a four-mark standalone polar arc length (exact form demanded), and a multi-part surface question with a *given* substitution — where "use the substitution" means differentiate it, express the integrand's pieces in $u$, and justify the new limits with visible working (the scheme withholds the A1 if the limit conversion is unevidenced).
- **MF19 gives none of these formulas** — not $\sqrt{1 + (y')^2}$, not the parametric or polar $ds$, not $2\pi y\, ds$. Four short formulas, all memory; the derivations above are the safety net.

### Edexcel IAL (Further Pure 3 — WFM03, §4.6)

Arc length and surface-area-of-revolution for Cartesian and parametric curves — same formulas, no polar duty at all (polar coordinates live in IAL FP2 with the sector area only).

### AP Calculus BC

Arc length of Cartesian curves (Unit 8) and of parametric/vector curves (Unit 9) is examined — the same $ds$ costumes, calculator-active variants included. Surfaces of revolution are **not** on the AP exam. IB AA/AI carry neither.

### Where it is *not* examined

Not on Cambridge 9709 or OxAQA 9660 (volumes of revolution yes, lengths and surfaces no), not in IB at any level — a genuinely Further/BC-tier topic.

## Connections

- **Parent:** [[Integration]] — the summing machine; and [[Pythagoras Theorem]] — the length of one sliver, applied infinitely often.
- **Costume suppliers:** [[Parametric Differentiation]] ($\dot x$, $\dot y$), [[Polar Coordinates]] (the $r, \theta$ frame and the sector-area sibling), [[Hyperbolic Functions]] — the catenary's perfect square and the surface question's sech-arithmetic.
- **Sibling:** [[Areas and Volumes by Integration]] (and the disc/washer section of [[Integration]]) — bulk by slicing where this topic does boundary by walking; the first-order/second-order error asymmetry of Misconception 1 is the honest frontier between the two.
- **Tool:** [[Standard Integrals]] — the partial-fraction and completing-the-square finishes that the harder cases demand.
- **For 9231 students:** [[MF19 Reference (9231)]] — none of the four formulas is on the sheet.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $ds = \sqrt{dx^2 + dy^2}$ | `ds = \sqrt{dx^2 + dy^2}` | the odometer step |
| $\sqrt{1 + (y')^2}$ | `\sqrt{1 + (y')^2}` | Cartesian costume |
| $\sqrt{\dot x^2 + \dot y^2}$ | `\sqrt{\dot x^2 + \dot y^2}` | parametric costume (dots allowed in tables only) |
| $\sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}$ | `\sqrt{r^2 + (\frac{dr}{d\theta})^2}` | polar costume |
| $S = \int 2\pi y\, ds$ | `S = \int 2\pi y\, ds` | the ribbon, not the shadow |
| $\operatorname{sech} x$ | `\operatorname{sech} x` | Cambridge's hyperbolic secant |
