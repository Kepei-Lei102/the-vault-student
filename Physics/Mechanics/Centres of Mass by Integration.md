---
chinese: 用积分求质心 (yòng jīfēn qiú zhìxīn)
prerequisites:
  - "[[Centre of Mass]]"
  - "[[Integration]]"
  - "[[Areas and Volumes by Integration]]"
leads_to: []
tags:
  - subject/physics
  - subject/mathematics
  - domain/mechanics
  - domain/calculus
  - level/A-Level
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/AP-Physics-C-Mech-2-1
  - type/deep
  - type/proof
  - misconception/formula-sheet-results-are-arbitrary
---

# Centres of Mass by Integration 用积分求质心

> *The formula sheet hands you six little facts — $\tfrac23$ of a median, $\tfrac38 r$, $\tfrac12 r$, two sine formulas, $\tfrac34 h$ — and asks you to trust them. You don't have to. Every one falls to the same single move: slice the body into pieces whose centre of mass you already know, and add the slices up with an integral. Two of them fall to arguments so pretty you won't even need the integral.*

## 中文锚点

公式表印了六个"标准结果"——三角形沿中线离顶点 $\tfrac23$ 处、实心半球 $\tfrac38 r$、半球壳 $\tfrac12 r$、圆弧 $\dfrac{r\sin\alpha}{\alpha}$、扇形 $\dfrac{2r\sin\alpha}{3\alpha}$、圆锥离顶点 $\tfrac34 h$——但从不告诉你它们从哪来。这张卡片把它们一个一个**亲手推**出来，而且全部只用同一招：**切片**。把物体切成一叠你已经知道质心在哪的薄片——三角形切成平行细条（每条的质心在中点）、圆锥和半球切成圆盘（每盘的质心在圆心）、扇形切成一把细三角形（每片的质心在距尖端 $\tfrac23 r$ 处）——然后"对切片取矩"：$\bar{x} = \dfrac{\int x\,dm}{\int dm}$，分子是每片的位置乘质量加起来，分母是总质量。积分在这里不是新工具，就是[[Integration|把无穷多片加起来]]的那个老朋友。最妙的是有两个结果根本不用积分：**扇形**是一把细三角形，每片质心都在距尖端 $\tfrac23 r$ 处，所以整个扇形等价于一条半径缩成 $\tfrac23 r$ 的圆弧——扇形公式就是圆弧公式乘 $\tfrac23$，你把两条公式对照看，果然如此；**半球壳**则靠阿基米德的"帽盒定理"：球面被两个平行平面截出的面积只跟两平面的间距成正比，跟截在哪无关——所以壳的质量沿高度**均匀分布**，质心自然在半高 $\tfrac12 r$。定理比积分还快，这就是为什么这两条值得亲手推一遍：推过之后，公式表不再是六句要背的咒语，而是六个你随时能重建的老朋友。

| English | 中文 | one-line meaning |
|---|---|---|
| slice / element | 切片 / 微元 | the thin piece whose own centre of mass is known |
| strip | 细条 | the lamina's slice: a thin rectangle, centre at its midpoint |
| disc | 圆盘 | the solid-of-revolution's slice, centre on the axis |
| ring / band | 圆环 / 环带 | the shell's slice, centre on the axis by symmetry |
| $dm$ | 质量微元 | the slice's mass — area, arc length or volume times density |
| centroid | 形心 | the centre of mass of a uniform shape — geometry only |
| hat-box theorem | 帽盒定理 | equal-height bands of a sphere have equal area |

## The one move

[[Centre of Mass]] defines the point by a sum, $M\bar{x} = \sum m_i x_i$. For a continuous body the pieces become infinitely many and infinitely thin, and the sum becomes exactly the kind [[Integration]] was built to do:

$$\bar{x} = \frac{\int x \, dm}{\int dm}$$

The craft — the *only* craft — is choosing the slice, and the rule for choosing is: **cut so that each slice's own centre of mass is somewhere you already know.** Cut a triangle into strips parallel to a side and each strip is a thin rectangle, centre at its midpoint. Cut a cone into discs and each disc's centre sits on the axis. A good slice turns a two-dimensional problem into a one-dimensional integral; a bad slice leaves you integrating something whose centre of mass you don't know, which is the same problem again, smaller. Then $dm$ is the slice's mass — for a uniform body, its length, area or volume, since the density is a common factor that cancels top and bottom (the same cancellation [[Centre of Mass]] uses for laminae).

Everything below is that one move, six times — with two delightful exceptions where a *theorem* beats the integral to the answer.

![[com-integration-see-it-run.mp4]]

*All six, integrated before your eyes: the slice sweeps through each body — the animation is the integral — and the two no-integral arguments (the fan of triangles, Archimedes' hat-box) get their chapters. The closing frame is the formula sheet, earned.*

## The laminae and curves

![[com-integration-laminae.svg|780]]

### 1. Triangular lamina — strips parallel to a side

Measure $x$ from the apex toward the opposite side, height $h$. A strip at depth $x$ is parallel to that side, and similar triangles make its width proportional to $x$ — so its mass element is $dm \propto x\,dx$, and its own centre of mass is at its midpoint, which lies on the median. All the action is along the median:

$$\bar{x} = \frac{\int_0^h x \cdot x \, dx}{\int_0^h x \, dx} = \frac{h^3/3}{h^2/2} = \frac{2h}{3}$$

**Two-thirds of the way from the apex** — the formula-sheet phrase "$\tfrac23$ along median from vertex", earned in two lines. (Equivalently $\tfrac13$ up from the side: the centroid sits low, because the strips get wider toward the base and the wide strips outvote the narrow ones. Weighted averages lean toward the heavy voters — that intuition checks every result on this page.)

### 2. Circular arc — beads on a wire

A uniform arc of radius $r$ spanning angle $2\alpha$, symmetric about the $x$-axis. Slice it into beads: the bead at angle $\theta$ has length $r\,d\theta$ and sits at $x = r\cos\theta$. Total length $2\alpha r$:

$$\bar{x} = \frac{\int_{-\alpha}^{\alpha} (r\cos\theta)\, r\,d\theta}{2\alpha r} = \frac{r^2 \cdot 2\sin\alpha}{2\alpha r} = \frac{r\sin\alpha}{\alpha}$$

Sanity-check the ends: as $\alpha \to 0$ the arc shrinks to a point at distance $r$, and $\sin\alpha/\alpha \to 1$. ✓ For a semicircular arc, $\alpha = \tfrac{\pi}{2}$ gives $\bar{x} = 2r/\pi \approx 0.64r$ — well off the wire itself, as [[Centre of Mass]] warned it may be.

### 3. Circular sector — no integral needed

Here is the first of the two results that are prettier than their integrals. Slice the sector into a **fan of thin triangles**, each with its apex at the centre. Every one of those triangles has its centre of mass $\tfrac23 r$ from the apex — result 1, just proved. So the sector is equivalent to its own arc, **shrunk to radius $\tfrac23 r$**, and the answer is result 2 with $r$ replaced:

$$\bar{x} = \frac{\left(\tfrac23 r\right)\sin\alpha}{\alpha} = \frac{2r\sin\alpha}{3\alpha}$$

Put the two formula-sheet lines side by side — arc $\dfrac{r\sin\alpha}{\alpha}$, sector $\dfrac{2r\sin\alpha}{3\alpha}$ — and the mysterious extra $\tfrac23$ is no longer a coincidence to memorise: **the sector formula *is* the arc formula, times the triangle result.** Three facts collapse into one. (The honest double integral $\displaystyle\iint s\cos\theta \; \cdot s\,ds\,d\theta$ gives the identical answer; it was checked symbolically for this card, and the fan argument is how you should *remember* it.) The semicircular lamina, $\alpha = \tfrac{\pi}{2}$: $\bar{x} = \dfrac{4r}{3\pi} \approx 0.42r$.

## The solids

![[com-integration-solids.svg|780]]

### 4. Solid cone or pyramid — discs

Measure $x$ from the vertex down the axis, height $h$. The disc at depth $x$ has radius proportional to $x$, hence area — and mass — proportional to $x^2$, with its centre on the axis:

$$\bar{x} = \frac{\int_0^h x \cdot x^2\,dx}{\int_0^h x^2\,dx} = \frac{h^4/4}{h^3/3} = \frac{3h}{4}$$

**Three-quarters from the vertex** — even lower than the triangle's two-thirds, because in a solid the slices grow like $x^2$ rather than $x$: the heavy voters near the base are heavier still. Notice the derivation never used circularity, only *cross-sectional area $\propto x^2$* — which is why the formula sheet can say "cone **or pyramid**" in one breath: every pyramid, square, hexagonal or lopsided, scales the same way.

### 5. Solid hemisphere — discs again

Discs perpendicular to the axis of symmetry, at height $x$ above the flat face; by Pythagoras the disc's radius is $\sqrt{r^2 - x^2}$, so its mass $\propto (r^2 - x^2)\,dx$:

$$\bar{x} = \frac{\int_0^r x(r^2-x^2)\,dx}{\int_0^r (r^2-x^2)\,dx} = \frac{r^4/4}{2r^3/3} = \frac{3r}{8}$$

Low again, and for the same reason: the fat discs live near the flat face.

### 6. Hemispherical shell — Archimedes beats the integral

The second gem. The honest route slices the shell into rings: the ring at colatitude $\theta$ has radius $r\sin\theta$, width $r\,d\theta$, height $r\cos\theta$, and the integral delivers $\bar{x} = \tfrac12 r$. Fine. But look at what the integral is quietly telling you — that suspiciously clean $\tfrac12$ — and there is a reason behind it that Archimedes knew twenty-two centuries ago.

**The hat-box theorem:** cut a sphere by two parallel planes a distance $d$ apart, and the area of the band between them is $2\pi r d$ — *depending only on the spacing $d$, not on where the cut falls.* Near the pole the band is a small circle but meets the cutting planes at a shallow slant, so it is wide; near the equator it is a large circle met steeply, so it is narrow. The two effects cancel **exactly** (both are governed by the same $\sin\theta$, once as the ring's radius and once, inverted, as the slant of its width — that cancellation is the whole proof, and it is why the ring integral above had a constant integrand). Consequence: the shell's mass is **spread uniformly over height**. And the centre of mass of anything spread uniformly from $0$ to $r$ is at the midpoint:

$$\bar{x} = \frac{r}{2}$$

No integral, one theorem, and an explanation for why the answer is the only clean fraction on the sheet. (The same theorem is why a sphere and its circumscribing cylinder have equal lateral areas — the fact Archimedes had carved on his tombstone.)

## The results, assembled

| Uniform body | Slice used | Centre of mass |
|---|---|---|
| Triangular lamina | strips ∥ a side, width $\propto x$ | $\tfrac23$ along median from vertex |
| Circular arc, angle $2\alpha$ | beads $r\,d\theta$ | $\dfrac{r\sin\alpha}{\alpha}$ from centre |
| Circular sector, angle $2\alpha$ | fan of triangles → arc at $\tfrac23 r$ | $\dfrac{2r\sin\alpha}{3\alpha}$ from centre |
| Solid cone / pyramid | discs, area $\propto x^2$ | $\tfrac34 h$ from vertex |
| Solid hemisphere | discs, radius $\sqrt{r^2-x^2}$ | $\tfrac38 r$ from centre |
| Hemispherical shell | bands — uniform in height (hat-box) | $\tfrac12 r$ from centre |

Every entry was re-derived symbolically while this card was written, and the two shortcut arguments were checked against their honest integrals. Cross-check from an unexpected direction: Pappus's theorem ([[Centre of Mass]] §Beyond) says rotating the semicircular lamina about its diameter sweeps a sphere, so $2\pi\bar{R}\cdot\tfrac{\pi r^2}{2}$ must equal $\tfrac43\pi r^3$ — solve, and out falls $\bar{R} = \tfrac{4r}{3\pi}$, the sector result at $\alpha = \tfrac{\pi}{2}$. Three independent routes, one answer; that agreement, not authority, is why you can trust the sheet.

## Worked example — the AP Physics C shape

> A thin rod of length $L$ lies along the $x$-axis from the origin. Its linear density increases linearly from zero at the origin: $\lambda(x) = \lambda_0 \dfrac{x}{L}$. Find the centre of mass.

*Trigger: non-uniform density means neither symmetry nor standard results apply — this is what the integral definition is actually for.* The mass element is $dm = \lambda(x)\,dx$:

$$\bar{x} = \frac{\int_0^L x\,\lambda_0\tfrac{x}{L}\,dx}{\int_0^L \lambda_0\tfrac{x}{L}\,dx} = \frac{\lambda_0 L^2/3}{\lambda_0 L/2} = \frac{2L}{3}$$

Two-thirds of the way along — leaning toward the heavy end, as the weighted-average intuition demands, and *identical in structure to the triangle*: a rod whose density grows like $x$ carries the same mass distribution as a triangle's strips. Two problems, one integral. This exact shape — a rod with $\lambda \propto x$, sometimes $\lambda \propto x^2$ — is AP Physics C's standard way of asking this card's question; total-mass-first ($M = \int dm$, then $\bar{x} = \frac{1}{M}\int x\,dm$) is the layout the scoring guidelines reward.

## Common Misconceptions (Teaching Notes)

### 1. "The formula-sheet results are arbitrary facts to memorise"

They are one idea — slice, then average — applied six times, and two of them aren't even integrals (the sector is the arc shrunk to $\tfrac23 r$; the shell is uniform in height by the hat-box theorem). A student who has derived them once can rebuild any of them from a blank page, which is a stronger position than trusting a sheet — and the exam-day payoff is *checking*: if your recalled hemisphere fraction is $\tfrac38$ or $\tfrac83$, the two-line disc integral settles it.

### 2. "Slice any way you like — it's all the same integral"

Only a slice whose own centre of mass is known turns the problem one-dimensional. Slice a cone *parallel to its axis* and each slice is a strange lens-shaped slab whose centre of mass is itself unknown — you have made the problem worse. The slicing direction is a genuine decision, and it is always: perpendicular to the axis you are measuring along.

### 3. "Solid and hollow are close enough"

The hemisphere pair on the sheet says otherwise: solid $\tfrac38 r$, shell $\tfrac12 r$ — a 33% disagreement between two objects with the same silhouette. Mass distribution, not outline, decides the centre of mass; the solid's discs pile mass near the flat face while the shell's bands spread it evenly. Read the words *solid* and *shell* in a question as load-bearing.

## Exam Notes

### Cambridge 9231 (Further Mechanics, Paper 3) — §3.2

The syllabus states that **proofs of the MF19 results are not required** — the results are given, and [[Centre of Mass]] shows how the exam actually spends them (composite tables, toppling). This card is therefore *insurance and understanding* for 9231: the derivations let you verify a half-remembered entry under exam conditions, and the composite-body questions do sometimes join a cone to a hemisphere, where knowing *why* $\tfrac34 h$ measures from the vertex and $\tfrac38 r$ from the centre prevents the classic measured-from-the-wrong-end error.

### Edexcel IAL — Further Mechanics M3

M3.5.1's own words: "the use of **integration** and/or symmetry to determine the centre of mass of a uniform body **will be required**." This card is that requirement: strips, discs and shells as above, including solids of revolution. (Contrast M2.2, where the specification says integration is *not* required and results may be quoted — the M2 student uses [[Centre of Mass]]; the M3 student needs this card too.)

### AP Physics C: Mechanics — Unit 2.1

The course description names $\mathbf{r}_{\text{cm}} = \frac{1}{M}\int \mathbf{r}\,dm$ for continuous mass distributions explicitly. The favourite free-response shape is the **non-uniform rod** worked above ($\lambda \propto x$ or $x^2$); set out total mass first, then the moment integral. The standard solids appear as setups rather than as memorised results — AP gives no formula sheet for these.

### Where it is *not* examined

- **OxfordAQA 9660** — the specification states "integration methods are not required" for centres of mass; symmetry, particle systems and composite bodies ([[Centre of Mass]]) are the whole requirement.
- **Cambridge 9709, 9702, 0625, IB Physics, AP Physics 1** — none asks for any centre-of-mass integral; see [[Centre of Mass]] §Exam Notes for what each does ask.

## Connections

- **Parent:** [[Centre of Mass]] — the definition, the theorem that makes the point matter, and the composite-table craft these results plug into.
- **Builds on:** [[Integration]] — the sum of infinitely many slices; [[Areas and Volumes by Integration]] — the same discs and shells, one power of $x$ earlier.
- **Kindred:** [[Moment of Inertia]] — the sibling integral $\int r^2\,dm$: same slicing craft, one more power of $r$, and the same standard-bodies table waiting at the end; [[Arc Length and Surfaces of Revolution]] — Pappus's theorems, which this card uses as an independent cross-check.
- **For 9231 students:** [[MF19 Reference (9709)]] — the six results as printed; this card is where they come from.

## LaTeX Reference

| symbol | LaTeX | meaning here |
|---|---|---|
| $\bar{x} = \dfrac{\int x\,dm}{\int dm}$ | `\bar{x} = \dfrac{\int x\,dm}{\int dm}` | the one move |
| $dm$ | `dm` | mass of a slice |
| $\lambda(x)$ | `\lambda(x)` | linear density (AP rod) |
| $\dfrac{r\sin\alpha}{\alpha}$ | `\dfrac{r\sin\alpha}{\alpha}` | arc result |
| $\dfrac{2r\sin\alpha}{3\alpha}$ | `\dfrac{2r\sin\alpha}{3\alpha}` | sector result |
| $2\pi r d$ | `2\pi r d` | hat-box band area |
