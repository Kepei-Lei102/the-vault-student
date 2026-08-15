---
chinese: 不变点与不变直线 (bùbiàn diǎn yǔ bùbiàn zhíxiàn)
prerequisites:
  - "[[Matrix Transformations]]"
  - "[[Combination of Transformations]]"
  - "[[Determinants and Inverses]]"
leads_to:
  - "[[Eigenvalues and Eigenvectors]]"
tags:
  - subject/mathematics
  - domain/matrices
  - domain/transformations
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/IB-AI
  - curriculum/AP
  - syllabus/9231-1-4
  - type/definition
  - type/technique
  - notation/matrix
  - misconception/invariant-line-vs-invariant-points
  - misconception/no-invariant-lines
  - misconception/vertical-invariant-line
---

# Invariant Points and Lines 不变点与不变直线

> *Select this sentence and press italic. Every letter leans — yet the line the letters sit on does not move a hair's breadth. The lean is a matrix (a shear, applied by your computer to every glyph), and the baseline is the one line of points that matrix refuses to touch.*
>
> *Every transformation has such refusals, and they are the fastest way to understand it. Watching what a machine moves tells you a thousand things; asking what it **keeps** tells you the one thing that organises the rest. This card is the systematic hunt for what stays.*

## Definition

### Formal

Recall from [[Matrix Transformations]] that a matrix moves every point of the plane, and the **image** of a point is where it lands: the image of $\mathbf{p} = \binom{x}{y}$ is $\mathbf{M}\mathbf{p} = \binom{x'}{y'}$, primes marking the image throughout. Then, for a transformation represented by the matrix $\mathbf{M}$:

- A point $P$ with position vector $\mathbf{p}$ is an **invariant point** if $\mathbf{M}\mathbf{p} = \mathbf{p}$ — its image is itself.
- A line $\ell$ is an **invariant line** if the image of every point of $\ell$ lies on $\ell$: points may move, but only *along* the line.
- A line $\ell$ is a **line of invariant points** if every point of $\ell$ is individually fixed: $\mathbf{M}\mathbf{p} = \mathbf{p}$ for all $\mathbf{p}$ on $\ell$.

Every line of invariant points is an invariant line. The converse fails, and the gap between the two is a reliable source of exam marks.

### Intuitive

**Pins versus rails.** A line of invariant points is a row of *pins*: every point nailed down, nothing moves. An invariant line is a *rail*: a train on it may slide along, but it never leaves the track. The exam phrase "invariant line" promises only the rail; if the question says "line of invariant points", it is claiming the pins.

The italic baseline is pins: each point of it maps to itself. The other horizontal lines of the paragraph are rails: a shear slides their points sideways, by more the further they sit from the baseline, but each horizontal line lands on itself.

Watch the two behaviours side by side. Three marked lines go through the same machine, $\mathbf{M} = \begin{pmatrix} 2 & 2 \\ 0 & 1 \end{pmatrix}$: the amber line's dots **freeze** (pins), the green line's dots **slide along it** (a rail), and the red line simply swings away (neither). Then the undo runs — the rails slide back, and the pins never noticed either trip:

![[invariant-lines-flow.mp4]]

### 中文锚点 (Chinese Anchor)

中文教材里 $\mathbf{M}\mathbf{p} = \mathbf{p}$ 的点通常叫**不动点**（fixed point）——"不动"二字比英文 *invariant*（不变）更直白。剑桥的术语体系要区分三层：

- **invariant point 不动点**：$\mathbf{M}\mathbf{p} = \mathbf{p}$，这个点钉死不动。
- **line of invariant points 不动点线**：整条线上**每个点都钉死**（"钉子线"）。
- **invariant line 不变直线**：线上的点可以**沿线滑动**，但永远不离开这条线（"轨道线"）。

考试大坑就在后两者：不变直线 ≠ 不动点线。轨道上的火车在动，轨道本身没动——"线不变"说的是轨道，不是火车。

## The full transformation kit — any rotation, the stretch, the shear

[[Matrix Transformations]] carries the base set — quadrant rotations, axis and diagonal reflections, enlargements, and the column trick that builds any such matrix (*column 1 is the image of $(1,0)$; column 2 is the image of $(0,1)$*). Three additions complete the kit that Further-level and university work assume.

**The general rotation.** Rotating anticlockwise by $\theta$ sends $(1, 0) \to (\cos\theta, \sin\theta)$ and $(0,1) \to (-\sin\theta, \cos\theta)$ — read both straight off the unit circle. Columns in place:

$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

**The stretch.** A stretch parallel to the $x$-axis with scale factor $k$ sends $(x, y) \to (kx, y)$: matrix $\begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix}$. (Parallel to the $y$-axis: $\begin{pmatrix} 1 & 0 \\ 0 & k \end{pmatrix}$.) Unlike an enlargement it scales *one* direction only — and unlike an enlargement, its determinant is $k$, not $k^2$.

**The shear.** A shear fixes one line and slides everything else *parallel to it*, by an amount proportional to the distance from the fixed line. Cambridge specifies a shear by naming the fixed line and the image of one point: "shear, $x$-axis fixed, with $(0,1)$ mapped to $(k, 1)$" is

$$\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}, \qquad (x, y) \mapsto (x + ky,\ y).$$

Its determinant is $1$: **a shear moves almost every point of the plane and changes no area at all** — the italic lean loses no ink.

![[stretch-shear-invariants.svg|920]]

Two facts from [[Determinants and Inverses]] complete the kit and run through every exam question:

- **Area scale factor $= \lvert \det \mathbf{M} \rvert$** — with the modulus, since a determinant may be negative while an area may not.
- **$\mathbf{A}\mathbf{B}$ means $\mathbf{B}$ first, then $\mathbf{A}$** ([[Combination of Transformations]]), and $\mathbf{M}^{-1}$ is the transformation that undoes $\mathbf{M}$ — "find a matrix mapping the image back onto the object" is a one-word question.

## Invariant points — solve $(\mathbf{M} - \mathbf{I})\mathbf{p} = \mathbf{0}$

An invariant point satisfies $\mathbf{M}\mathbf{p} = \mathbf{p}$, i.e. $(\mathbf{M} - \mathbf{I})\mathbf{p} = \mathbf{0}$.

The origin always qualifies — $\mathbf{M}\mathbf{0} = \mathbf{0}$ for every matrix, which is why matrix transformations are always centred there. So the real question is whether anything *else* is fixed, and the answer is governed by a determinant:

- If $\det(\mathbf{M} - \mathbf{I}) \neq 0$, then $\mathbf{M} - \mathbf{I}$ is non-singular, $(\mathbf{M} - \mathbf{I})\mathbf{p} = \mathbf{0}$ forces $\mathbf{p} = \mathbf{0}$, and **the origin is the only invariant point**.
- If $\det(\mathbf{M} - \mathbf{I}) = 0$, the matrix $\mathbf{M} - \mathbf{I}$ collapses the plane onto a line — its two equations degenerate into one — and **a whole line of invariant points** appears through the origin.

Recall from [[Determinants and Inverses]] that a singular matrix is one that crushes the plane; here the crush is the good news, because everything it crushes to zero is a point that never moved.

**Worked in place** — the transformation $\begin{pmatrix} 6 & 5 \\ 2 & 3 \end{pmatrix}$:

$$(\mathbf{M} - \mathbf{I})\mathbf{p} = \begin{pmatrix} 5 & 5 \\ 2 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \quad\Longrightarrow\quad \begin{cases} 5x + 5y = 0 \\ 2x + 2y = 0 \end{cases}$$

Both equations say the same thing — $y = -x$ — and *they had to*: $\det(\mathbf{M} - \mathbf{I}) = 10 - 10 = 0$. The line of invariant points is $y = -x$. (Check one: $(1, -1) \mapsto (6 - 5,\ 2 - 3) = (1, -1)$ ✓.) **If your two equations give different lines, the arithmetic is wrong** — agreement isn't luck, it's the singularity.

## Invariant lines through the origin — the gradient quadratic

A line through the origin with gradient $m$ is the set of points $(t, mt)$. Because the transformation is linear, checking *one* non-zero point suffices: if $\mathbf{M}\mathbf{v}$ lands on the line, then $\mathbf{M}(t\mathbf{v}) = t\,\mathbf{M}\mathbf{v}$ lands on it too. So take the point $(1, m)$ — the point of the line one unit along in $x$ — and demand that **its image** stay on $y = mx$.

The image of $(1, m)$ is just the matrix applied to it, row-times-column as always:

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} 1 \\ m \end{pmatrix} = \begin{pmatrix} a \cdot 1 + b \cdot m \\ c \cdot 1 + d \cdot m \end{pmatrix} = \begin{pmatrix} a + bm \\ c + dm \end{pmatrix}.$$

For this image to lie on $y = mx$, its $y$-coordinate must be $m$ times its $x$-coordinate — $y_{\text{image}} = m\,x_{\text{image}}$ — which reads

$$c + dm = m(a + bm) \quad\Longrightarrow\quad \boxed{\ b m^2 + (a - d)m - c = 0.\ }$$

**Do not memorise this quadratic — re-derive it in the exam in one line** (image of $(1, m)$, demand gradient $m$). What *is* worth carrying is what its root count means, because each case is a geometry, not an algebra accident:

| Real roots | Geometry | Example |
|---|---|---|
| two | two invariant directions | most stretches, reflections, and mixed maps |
| one (repeated) | a single kept direction, counted twice | a shear — its fixed axis is the double root |
| none | the transformation keeps no direction at all | any rotation other than $180°$ |

**The vertical blind spot.** The form $y = mx$ cannot describe the line $x = 0$, so the quadratic never reports it. Check it separately, and the check is instant: $x = 0$ is invariant exactly when the image of $(0, 1)$ — which is column 2 of the matrix — has $x$-coordinate zero, i.e. **when $b = 0$**. Make "look at $b$ first" a habit and the blind spot never costs a mark.

**Worked in place** — the transformation $\begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}$: here $b = -1 \neq 0$ (no vertical line), and

$$-m^2 + (4 - 1)m - 2 = 0 \quad\Longrightarrow\quad m^2 - 3m + 2 = 0 \quad\Longrightarrow\quad m = 1 \text{ or } 2.$$

The invariant lines through the origin are $y = x$ and $y = 2x$. Check: $(1,1) \mapsto (3, 3)$ ✓ on $y = x$; $(1, 2) \mapsto (2, 4)$ ✓ on $y = 2x$ — both points *slid along* their lines rather than staying put: rails, not pins.

![[invariant-lines-vs-points.svg|920]]

## Invariant lines in general — allowing an intercept

The full hunt takes $y = mx + n$. Every point of that line has the form $(t,\ mt + n)$ — pick any $x$-value $t$, and the line hands you $y = mt + n$. Transform that general point, exactly as before, and call the image $(x', y')$:

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} t \\ mt + n \end{pmatrix} = \begin{pmatrix} at + b(mt + n) \\ ct + d(mt + n) \end{pmatrix}.$$

Now expand each coordinate and gather the terms in $t$ separately from the constants — the split that makes the next step work:

$$x' = at + b(mt + n) = (a + bm)\,t + bn, \qquad y' = ct + d(mt + n) = (c + dm)\,t + dn.$$

The line is invariant if the image is *back on the line*: $y' = mx' + n$, and not just for one $t$ but **for every $t$**, since every point of the line must land on it. Substitute the two expressions:

$$\underbrace{(c + dm)\,t + dn}_{y'} = m\big[\underbrace{(a + bm)\,t + bn}_{x'}\big] + n = m(a + bm)\,t + mbn + n.$$

Two expressions in $t$ that agree for *every* $t$ must agree coefficient by coefficient — the $t$-terms match and the constants match, separately:

- **Coefficient of $t$:** $c + dm = m(a + bm)$ — the same gradient quadratic as before. Intercepts don't change which *directions* can survive.
- **Constant term:** $dn = mbn + n$, i.e. $n\,(d - mb - 1) = 0$.

So for each gradient $m$ from the quadratic, either $n = 0$ (only the through-origin line survives) or $d - mb = 1$, in which case the constant equation holds for *every* $n$ — **the entire family of parallel lines with that gradient is invariant**.

**Worked in place** — the transformation $\begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}$: the gradient quadratic is $0 \cdot m^2 + (2-1)m - 1 = 0$, so $m = 1$. The family test: $d - mb = 1 - 0 = 1$ ✓ — so **every line of gradient 1 is invariant**. Directly: $(t,\ t + n) \mapsto (2t,\ 2t + n)$, and the image still satisfies $y = x + n$. A whole ruled sheet of parallel rails, none of them (except $y = x$) through the origin.

## The census — what each transformation keeps

Every row of this table is derivable from the two methods above; the table is what the topic *feels like* once the methods are internalised.

| Transformation | Invariant points | Invariant lines |
|---|---|---|
| Rotation, $\theta \neq 0°, 180°$ | origin only | none — nothing survives the turn |
| Rotation by $180°$ | origin only | every line through $O$ |
| Reflection in $y = x$ | the mirror $y = x$ (pins) | the mirror, and every line $y = -x + n$ perpendicular to it |
| Enlargement, factor $k \neq 1$ | origin only | every line through $O$ |
| Stretch $\begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix}$, $k \neq 1$ | the $y$-axis (pins) | the $y$-axis, and every horizontal line $y = n$ |
| Shear, $x$-axis fixed | the $x$-axis (pins) | every horizontal line $y = n$ |

Spot-check the reflection row with the machinery: $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ gives quadratic $m^2 - 1 = 0$, $m = \pm 1$. For $m = -1$: $d - mb = 0 - (-1)(1) = 1$ ✓ family — every $y = -x + n$ is a rail (each such line meets the mirror at right angles and reflects onto itself). For $m = +1$: $d - mb = -1 \neq 1$, so only $y = x$ itself — and that one is pins, not rails.

## Worked Examples

### Example 1 (the whole topic in one question): 9231/13 November 2024 Q1

> $\mathbf{M}$ represents a stretch parallel to the $x$-axis, scale factor $k$ ($k \neq 0$), followed by a shear, $x$-axis fixed, with $(0,1)$ mapped to $(k, 1)$.
> **(a)** Show that $\mathbf{M} = \begin{pmatrix} k & k \\ 0 & 1 \end{pmatrix}$. **[4]**
> **(b)** The transformation represented by $\mathbf{M}$ has a line of invariant points. Find, in terms of $k$, the equation of this line. **[3]**
> **(c)** The unit square $S$ is transformed by $\mathbf{M}$ onto the parallelogram $P$. Find, in terms of $k$, a matrix which transforms $P$ onto $S$. **[1]**
> **(d)** Given that the area of $P$ is $3k^2$ units$^2$, find the possible values of $k$. **[2]**

**(a)** *Tool: build each matrix by columns, then compose in the right order.* The stretch sends $(1,0) \to (k, 0)$ and $(0,1) \to (0,1)$: $\ \mathbf{S} = \begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix}$. The shear fixes $(1,0)$ and sends $(0,1) \to (k,1)$: $\ \mathbf{H} = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$. "Stretch **followed by** shear" puts the shear on the *left* — the later transformation is applied to the output of the earlier:

$$\mathbf{M} = \mathbf{H}\mathbf{S} = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}\begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} k & k \\ 0 & 1 \end{pmatrix}. \ \blacksquare$$

(The mark scheme awards the final mark only if it is clear *which* matrix is which transformation — name them as you build them.)

**(b)** *Tool: pins means $\mathbf{M}\mathbf{p} = \mathbf{p}$, solved honestly.*

$$\begin{pmatrix} k & k \\ 0 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix} \quad\Longrightarrow\quad kx + ky = x, \qquad y = y.$$

The second equation is vacuous — that is the singularity of $\mathbf{M} - \mathbf{I}$ showing up as a free row, and the reason a whole line exists. The first gives

$$y = \frac{1 - k}{k}\,x.$$

(The animation in the Intuitive section is this very matrix with $k = 2$: its pinned amber line is $y = \frac{1-2}{2}x = -\tfrac12 x$, and the $x$-axis — $y = 0$, gradient $\frac{1-k}{k}$ only when $k = 1$ — is a rail there, not pins. Same question, seen moving.)

**(c)** *Tool: "maps $P$ back onto $S$" is one word — the inverse.* By swap-and-negate ([[Determinants and Inverses]]), $\det \mathbf{M} = k$:

$$\mathbf{M}^{-1} = \frac{1}{k}\begin{pmatrix} 1 & -k \\ 0 & k \end{pmatrix} = \begin{pmatrix} \tfrac{1}{k} & -1 \\ 0 & 1 \end{pmatrix}.$$

**(d)** *Tool: area scale factor $= \lvert \det \mathbf{M} \rvert$ — modulus mandatory.* The unit square has area 1, so $P$ has area $\lvert k \rvert$:

$$\lvert k \rvert = 3k^2 \quad\Longrightarrow\quad \lvert k \rvert (3 \lvert k \rvert - 1) = 0 \quad\Longrightarrow\quad k = \pm\tfrac{1}{3} \quad (k \neq 0).$$

The mark scheme's own margin note: solving $k = 3k^2$ without the modulus — losing $k = -\tfrac13$ — earns only partial credit. The modulus is not decoration; it is half the answer.

### Example 2 (reading a composition, then hunting rails): 9231/13 June 2026 Q2

> $\mathbf{M} = \begin{pmatrix} \tfrac{1}{2}\sqrt{2} & -\tfrac{1}{2}\sqrt{2} \\ \tfrac{1}{2}\sqrt{2} & \tfrac{1}{2}\sqrt{2} \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
> **(a)** $\mathbf{M}$ represents a sequence of two transformations. Give full details of each, and make clear the order. **[4]**
> **(b)** Find the equations of the invariant lines, through the origin, of the transformation represented by $\mathbf{M}$. **[5]**

**(a)** *Tool: read a product right-to-left.* The right factor acts first: $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ is a **shear, $x$-axis fixed, $(0,1) \mapsto (2,1)$**. The left factor is $R_\theta$ with $\cos\theta = \sin\theta = \tfrac{1}{2}\sqrt{2}$: a **rotation of $45°$ anticlockwise about the origin**. Order: shear first, then rotation.

**(b)** *Tool: multiply out, then the gradient quadratic on $(1, m)$.*

$$\mathbf{M} = \begin{pmatrix} \tfrac{\sqrt2}{2} & \tfrac{\sqrt2}{2} \\ \tfrac{\sqrt2}{2} & \tfrac{3\sqrt2}{2} \end{pmatrix}, \qquad (1, m) \mapsto \tfrac{\sqrt2}{2}\left(1 + m,\ 1 + 3m\right).$$

On $y = mx$: $\ 1 + 3m = m(1 + m) \Longrightarrow m^2 - 2m - 1 = 0 \Longrightarrow m = 1 \pm \sqrt{2}$.

The invariant lines are $y = (1 + \sqrt 2)x$ and $y = (1 - \sqrt 2)x$.

**Worth pausing on:** the shear's own invariant lines (all horizontal) and the rotation's (none) tell you *nothing* about the composite's — invariance belongs to the whole machine, not to its parts. The parts each keep their own secrets; the product keeps different ones.

## Where the invariant line meets the world

- **Italic type, honestly computed.** When a font has no hand-drawn italic, the renderer *synthesises* one by applying exactly the shear matrix of this card to every glyph outline — CSS's `skewX(α)` is the matrix $\begin{pmatrix} 1 & \tan\alpha \\ 0 & 1 \end{pmatrix}$, applied by the browser to the text box. The baseline is the shear's line of invariant points, which is *why italic text stays on the line*: the one line the matrix cannot move is the one typography cannot afford to lose. Every `transform:` in CSS and every SVG `transform="matrix(a,b,c,d,e,f)"` is this card's $2\times2$ (plus a shift) running in your browser right now.
- **Mode 7, the matrix as game engine.** The Super Nintendo's famous "Mode 7" (F-Zero, Super Mario Kart) drew its racetracks by applying a $2\times2$ matrix — rotation composed with scaling, updated *per scanline* — to a flat texture, faking a 3D camera years before consoles could afford real 3D. The compositions of this card, run sixty times a second in 1990s silicon.
- **The direction a system keeps** is one of engineering's standing questions: the axes along which a stressed beam merely stretches (rather than twisting), the modes in which a bridge deck prefers to vibrate. Those are invariant lines of the relevant matrices, hunted with grown-up versions of the gradient quadratic — the machinery of [[Eigenvalues and Eigenvectors]].

> [!info] Beyond syllabus — the invariant line grows up: eigenvectors
> Recall the worked matrix $\begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}$ with rails $y = x$ and $y = 2x$. Look *along* each rail: $(1,1) \mapsto (3,3)$ — every point of $y = x$ is stretched by $3$; $(1,2) \mapsto (2,4)$ — every point of $y = 2x$ is stretched by $2$. An invariant direction together with its stretch factor is an **eigenvector** with its **eigenvalue** ($3$ and $2$ here), and the gradient quadratic you solved is the characteristic equation in disguise. A line of invariant points is simply the eigenvalue-$1$ case — stretch factor one, pins.
>
> [[Proof by Induction]] proves a formula for $\begin{pmatrix} 4 & -1 \\ 6 & -1 \end{pmatrix}^n$ whose entries are built from $2^n$ and constants — that matrix's two eigenvalues, $2$ and $1$, showing through the algebra. Diagonalisation, powers, and the full theory live at [[Eigenvalues and Eigenvectors]].

## Common Misconceptions (Teaching Notes)

### 1. "Invariant line" read as "line of invariant points"

The distinction *is* the topic, and questions test it directly — N24's Q1 asks for a **line of invariant points** and the gradient-quadratic method (which finds rails) is the wrong tool for it.

**Fix:** pins versus rails, said out loud before every question: *"Am I asked where nothing moves, or where movement is trapped?"* Pins ⇒ solve $\mathbf{M}\mathbf{p} = \mathbf{p}$. Rails ⇒ the gradient quadratic. Then note the one-way street: every pin-line is also a rail, never the reverse.

### 2. "No real roots — I must have made a mistake"

The gradient quadratic for a rotation by $45°$ has negative discriminant, and students erase correct work.

**Fix:** the algebra is reporting geometry, not failing at it. *Should* a rotation keep any direction? Turn a page $45°$ — which line on it points where it used to? None. The quadratic said exactly that. No real roots is an answer, not an error.

### 3. Vertical blindness

$y = mx$ never finds $x = 0$, and matrices with $b = 0$ are common in exams precisely because their $y$-axis behaviour is invisible to the standard method.

**Fix:** the pre-flight check — before writing the quadratic, look at $b$ (column 2's top entry). $b = 0$ means the image of $(0,1)$ is still vertical, so $x = 0$ is invariant: write it down *first*, then hunt gradients.

### 4. Expecting the parts to explain the product

In Example 2 the shear keeps every horizontal line and the rotation keeps nothing, so students guess the composite keeps horizontals, or nothing.

**Fix:** compute one image. The composite sent $(1, 1)$ somewhere neither parent would have — invariance is a property of the assembled machine. Multiply first, hunt second.

### 5. Showing invariance by checking a single point

One point on the line landing on the line proves nothing (the whole plane's worth of lines passes through one point).

**Fix:** invariance is a *for-all* claim — transform the general point $(t, mt + n)$, or use linearity to reduce to one point *plus the origin* for lines through $O$. The converse direction is cheap: to show a line is **not** invariant, one escaping point is a complete proof. Knowing which direction needs generality is the logical content of the topic.

## Exam Notes

### Cambridge 9231 — Further Pure 1, §1.4

The matrix question is a fixture of Paper 1, and its transformation half concentrates the marks:

- **"Give full details of each transformation"** means *all* the parameters: a rotation needs centre, angle, and direction; a stretch needs direction and factor; a shear needs the fixed line and the image of a named point; a reflection needs its mirror line. A named-but-unparameterised transformation scores partially at best — and in a composition, the mark scheme requires it to be clear **which matrix is which transformation**.
- **Order in compositions:** the syllabus states $\mathbf{A}\mathbf{B}$ is "$\mathbf{B}$ followed by $\mathbf{A}$" — read products right-to-left, and expect one mark to hinge on saying the order explicitly.
- **Invariant-line questions run 3–5 marks:** derive the condition from the image of $(1, m)$ or $(t, mt + n)$ rather than quoting a formula — the derivation *is* the method marks. Quote gradients exactly ($1 \pm \sqrt2$, not decimals).
- **The area trap:** area scale factor is $\lvert \det \mathbf{M} \rvert$; a mark scheme has explicitly downgraded answers that dropped the modulus and lost a negative case.
- The syllabus names rotation, reflection, enlargement, stretch and shear as required vocabulary, and warns that "other 2D transformations may be included" — the methods here (columns to build, $(\mathbf{M}-\mathbf{I})\mathbf{p} = \mathbf{0}$ for pins, the gradient condition for rails) need no catalogue, which is the point of learning methods over catalogues.

### Edexcel IAL — Further Pure 1 §6 (and FP3 §6.1–6.2)

FP1 §6.1–6.4 examines the **transformation kit** of this card almost line for line: linear transformations of column vectors and their matrices; "reflection in coordinate axes and lines $y = \pm x$, rotation through **any angle** about $(0,0)$, stretches parallel to the $x$-axis and $y$-axis, and enlargement about centre $(0,0)$"; combinations, with the spec stating outright that "$\mathbf{AB}$ is $\mathbf{B}$ followed by $\mathbf{A}$"; and the inverse of a transformation, with the determinant as area scale factor. Two honest differences from Cambridge:

- **Shears are not in the IAL list.** They can still appear as "identify this transformation" only if defined in the question; the named set is reflection, rotation, stretch, enlargement.
- **Invariant points and lines are not in the IAL specification at all** — the words do not occur in it. The pins-and-rails machinery of this card is Cambridge 9231 (and UK Further Maths) territory; an IAL candidate needs the kit sections and can treat the invariance sections as the eigenvector preview they are. FP3 §6.1–6.2 later extend the transformations to three dimensions.

### IB Mathematics: Applications and Interpretation HL

AHL 3.9 (AI HL only — Analysis and Approaches has no matrices): "geometric transformations of points in two dimensions using matrices: reflections, horizontal and vertical stretches, enlargements, translations and rotations; compositions of the above; geometric interpretation of the determinant of a transformation matrix." Note *translations* in that list — a translation is not a $2\times2$ matrix (it fixes no origin) and IB handles it by adding a vector after the matrix. Invariant lines are not named; IB reaches the same idea through **eigenvectors** in AHL 1.15, which is exactly the callout above with the vocabulary swapped.

### AP Precalculus — Unit 4 (not assessed)

4.12 *Linear Transformations and Matrices* and 4.13 *Matrices as Functions* cover the transformation kit — but Unit 4 is **not assessed on the AP exam**. Course content only.

### Where it is *not* examined

**Cambridge 9709, 0580 and 0606** carry no matrices in their current syllabuses; **OxAQA 9260** stops at the base transformation set of [[Matrix Transformations]] (quadrant rotations, axis and diagonal reflections, enlargements — no general rotation, stretch, shear, or invariance); **IB AA** has none. For those students this card is the bridge to Further and university work, not exam material.

### Beyond high school — University

Invariant lines through the origin are eigenvector directions, and the topic reappears as the *first* question asked of every linear operator: in 3D (invariant planes join the hunt), in differential equations (straight-line solutions of systems), in iterated maps (the directions that survive repetition — see the callout above). The census table of this card is the $2\times2$ nursery of spectral theory.

## Connections

- **Parent:** [[Matrix Transformations]] — the base transformation set and the column trick this card builds on.
- **Composition:** [[Combination of Transformations]] — right-to-left reading, needed for every "sequence of transformations" part.
- **Measuring partner:** [[Determinants and Inverses]] — the other half of the same topic: that card measures what the machine distorts (area, orientation, undo-ability); this one finds what it keeps. The singularity test $\det(\mathbf{M} - \mathbf{I}) = 0$ is its determinant put to geometric work.
- **Extension:** [[Eigenvalues and Eigenvectors]] — invariant directions with their stretch factors; the gradient quadratic grows into the characteristic equation.
- **Already whispering:** [[Proof by Induction]] — the matrix-power example whose answer's $2^n$ structure is an eigenvalue showing through.
- **For 9231 students:** [[MF19 Reference (9231)]] — nothing from this card is on the formula sheet; the rotation matrix and both invariance methods live in your head (or better: get re-derived on the spot).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{M}\mathbf{p} = \mathbf{p}$ | `\mathbf{M}\mathbf{p} = \mathbf{p}` | invariant-point condition |
| $R_\theta$ | `R_\theta` | rotation matrix shorthand |
| $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ | `\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}` | general rotation |
| $\lvert \det \mathbf{M} \rvert$ | `\lvert \det \mathbf{M} \rvert` | area scale factor (modulus mandatory) |
| $(t,\ mt + n)$ | `(t,\ mt + n)` | general point of $y = mx + n$ |
| $\blacksquare$ | `\blacksquare` | end of proof |
