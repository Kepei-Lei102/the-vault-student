---
chinese: 空间平面 (kōngjiān píngmiàn)
prerequisites:
  - "[[3D Vectors and the Scalar Product]]"
  - "[[Vector Equations of Lines]]"
  - "[[Cross Product]]"
leads_to:
  - "[[Linear Systems in 3D]]"
tags:
  - subject/mathematics
  - domain/geometry
  - domain/linear-algebra
  - level/A-Level
  - level/IB-AA-HL
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/9231-1-6
  - type/technique
  - type/definition
  - notation/vector
  - notation/normal-form
  - notation/parametric
  - misconception/normal-not-in-plane
  - misconception/p-is-not-distance
  - misconception/line-plane-angle-complement
  - misconception/dropping-abs-in-distance
  - misconception/checking-direction-not-point
---

# Planes in 3D 空间平面

## Definition

### Formal

A **plane** is the set of all points whose position vector $\mathbf{r}$ satisfies

$$\mathbf{r} \cdot \mathbf{n} = p,$$

where $\mathbf{n}$ is a fixed nonzero vector — the **normal** (法向量), perpendicular to the plane — and $p$ is a constant. Writing $\mathbf{r} = (x, y, z)$ and $\mathbf{n} = (a, b, c)$ unpacks it into the **Cartesian form** $ax + by + cz = p$. Equivalently, a plane through the point $\mathbf{a}$ spanned by two non-parallel direction vectors $\mathbf{b}, \mathbf{c}$ is everything reachable as

$$\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}, \qquad \lambda, \mu \in \mathbb{R}.$$

A line needed *one* parameter; a plane is a two-parameter, two-dimensional flat sheet.

### Intuitive

**The normal is the flagpole; the plane is a floor of equal shadow.** Take the line through the origin along $\mathbf{n}$ and project any point of space onto it — that's the point's "height" measured along the flagpole. The equation $\mathbf{r}\cdot\mathbf{n} = p$ says: *the plane collects every point whose shadow lands at the same mark on the flagpole.* One direction to be perpendicular to, one number to pin the height — that is all a flat sheet is. And the sheet is **infinite**: a plane has no edges, no shape, no area — every parallelogram drawn on this page (and every patch in the animations) is just a finite *window* onto an endless sheet. The only two things that distinguish one plane from another are which way it faces ($\mathbf{n}$) and where it stands along its own normal ($p$) — a house number, not a house size. Every distance and angle formula on this page is this one picture, re-read. Watch the definition assemble itself — points auditioning for the equation, the parametric costume wandering without ever leaving the sheet, and the dial $p$ sliding the plane along its flagpole:

![[planes-in-3d-assembly.mp4]]

### 中文锚点

国内教材把平面方程分成几种标准形式，对照如下：

| 国内叫法 | 形式 | Cambridge 术语 |
|---|---|---|
| 一般式 | $ax + by + cz = d$ | Cartesian form |
| 点法式 | $a(x{-}x_0) + b(y{-}y_0) + c(z{-}z_0) = 0$ | $(\mathbf{r} - \mathbf{a})\cdot\mathbf{n} = 0$ 的展开 |
| 参数式 | $\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}$ | parametric / vector form |

点法式和 $\mathbf{r}\cdot\mathbf{n} = p$ 是同一句话：$(\mathbf{r}-\mathbf{a})\cdot\mathbf{n} = 0$ 说"从 $\mathbf{a}$ 出发到平面上任何点的位移都垂直于法向量"，展开即 $\mathbf{r}\cdot\mathbf{n} = \mathbf{a}\cdot\mathbf{n} = p$。国内高考不考空间向量的叉积（法向量靠解方程组凑），Cambridge 9231 里 [[Cross Product|叉积]] 是求法向量的标准工具——两条路，同一个 $\mathbf{n}$。

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Normal form | $\mathbf{r}\cdot\mathbf{n} = p$ | "r dot n equals p" | Cambridge's letter is $p$; many books write $d$ |
| Cartesian | $ax + by + cz = p$ | — | Same equation, coordinates spelled out |
| Parametric | $\mathbf{r} = \mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}$ | — | $\mathbf{b}, \mathbf{c}$ non-parallel, both *in* the plane |
| Unit normal | $\hat{\mathbf{n}} = \mathbf{n}/\lvert\mathbf{n}\rvert$ | "n hat" | Makes $\mathbf{r}\cdot\hat{\mathbf{n}}$ a genuine distance |

> [!warning] Notation Trap
> In $\mathbf{r}\cdot\mathbf{n} = p$, the number $p$ is **not** the distance from the origin unless $\mathbf{n}$ is a *unit* vector — it is the distance *scaled by $\lvert\mathbf{n}\rvert$*. The true origin-to-plane distance is $p/\lvert\mathbf{n}\rvert$ (derived below). Books that write $d$ for the constant make this trap crueller.

## One plane, three costumes

Meet the running example of this whole page:

$$\Pi:\quad 2x + y + 2z = 6, \qquad \mathbf{n} = \begin{pmatrix}2\\1\\2\end{pmatrix},\quad \lvert\mathbf{n}\rvert = 3.$$

It crosses the axes at $A(3, 0, 0)$, $B(0, 6, 0)$, $C(0, 0, 3)$ (set the other two variables to zero each time). Here is the same plane in each costume, with the conversions worked both ways.

**Cartesian → normal form** is free: read off $\mathbf{n} = (2, 1, 2)$ and $p = 6$, so $\mathbf{r}\cdot\mathbf{n} = 6$.

**Cartesian → parametric:** take one point and two in-plane vectors. From the intercepts, $\mathbf{b} = \vec{AB} = (-3, 6, 0)$ and $\mathbf{c} = \vec{AC} = (-3, 0, 3)$:

$$\mathbf{r} = \begin{pmatrix}3\\0\\0\end{pmatrix} + \lambda\begin{pmatrix}-3\\6\\0\end{pmatrix} + \mu\begin{pmatrix}-3\\0\\3\end{pmatrix}.$$

**Parametric → Cartesian** is the [[Cross Product]]'s signature job — the normal must be perpendicular to both spanning vectors, and that is exactly what the cross product builds. Recall the recipe: write $\mathbf{i}, \mathbf{j}, \mathbf{k}$ across the top, the two vectors underneath, and expand along the top row with the alternating signs $+, -, +$ — each unit vector is paired with the $2\times 2$ determinant that remains after deleting its own row and column:

$$\mathbf{b}\times\mathbf{c} = \begin{vmatrix}\mathbf{i} & \mathbf{j} & \mathbf{k}\\ -3 & 6 & 0\\ -3 & 0 & 3\end{vmatrix} = \mathbf{i}\,(6\cdot 3 - 0\cdot 0) \;-\; \mathbf{j}\,\big((-3)\cdot 3 - 0\cdot(-3)\big) \;+\; \mathbf{k}\,\big((-3)\cdot 0 - 6\cdot(-3)\big) = \begin{pmatrix}18\\9\\18\end{pmatrix} = 9\begin{pmatrix}2\\1\\2\end{pmatrix}.$$

(Watch the middle sign: the $\mathbf{j}$ term is *subtracted*, and its little determinant came out negative, so the two minus signs cancel — the classic slip is losing exactly one of them.)

The loop closes: the cross product recovers $\mathbf{n} = (2,1,2)$ (any scalar multiple of a normal is a normal — divide out the 9). Then $p = \mathbf{a}\cdot\mathbf{n} = (3,0,0)\cdot(2,1,2) = 6$. This same computation *is* the recipe for a **plane through three points**: two edge vectors, cross them, dot with any of the three points.

![[planes-3d-anatomy.svg|720]]

### Why $\mathbf{r}\cdot\mathbf{n} = p$ means "equal shadow"

Recall from [[3D Vectors and the Scalar Product]] that $\mathbf{r}\cdot\hat{\mathbf{n}}$ is the **component of $\mathbf{r}$ along $\hat{\mathbf{n}}$** — the length of $\mathbf{r}$'s shadow on the flagpole. Dividing the plane equation by $\lvert\mathbf{n}\rvert = 3$:

$$\mathbf{r}\cdot\hat{\mathbf{n}} = \frac{6}{3} = 2.$$

Check it on the three intercepts: $A\cdot\hat{\mathbf{n}} = \tfrac{1}{3}(6+0+0) = 2$; $B\cdot\hat{\mathbf{n}} = \tfrac{1}{3}(0+6+0) = 2$; $C\cdot\hat{\mathbf{n}} = \tfrac{1}{3}(0+0+6) = 2$. Three very different points — one shadow. *That* is what a plane is, and the animation below rotates the picture so you can watch every projection land on the same mark:

![[planes-in-3d-shadow.mp4]]

## Distance from a point to a plane — the shadow gap

First, pin down what the lowercase $p$ actually *is*, because the distance formula runs on it. $p$ is **the plane's own shadow number**: compute $\mathbf{a}\cdot\mathbf{n}$ for *any* point $\mathbf{a}$ of the plane and you get the same value — that shared value is $p$ (for the running plane $2x + y + 2z = 6$, it's the $6$). And $p$ is a *dial*: fix the tilt $\mathbf{n}$ and turn $p$, and the plane **slides along its own flagpole** — same orientation, different station, origin-distance $p/\lvert\mathbf{n}\rvert$ (the assembly animation above turns exactly this dial in its last act). 

Now the formula writes itself. If every point of $\Pi$ has shadow $2$ on the flagpole, then a point $P$ with shadow $5$ must stand a perpendicular distance $5 - 2 = 3$ from the plane. That single sentence is the whole distance formula:

$$\boxed{\;\operatorname{dist}(P, \Pi) = \frac{\lvert \mathbf{a}\cdot\mathbf{n} - p\rvert}{\lvert\mathbf{n}\rvert}\;}$$

— the gap between $P$'s flagpole mark and the plane's, converted to true length. (The absolute value: $P$ may stand on either side.)

**Concretely.** Take $P(3, 3, 3)$. Its shadow number is $\mathbf{a}\cdot\mathbf{n} = 6 + 3 + 6 = 15$, against the plane's $p = 6$:

$$\operatorname{dist} = \frac{\lvert 15 - 6\rvert}{3} = 3.$$

**The foot of the perpendicular** — the exam's favourite follow-up — is found by *walking* from $P$ along the normal until you land on the plane. Parametrise the walk $\mathbf{r} = P + t\,\mathbf{n} = (3+2t,\; 3+t,\; 3+2t)$ and substitute into $\Pi$:

$$2(3+2t) + (3+t) + 2(3+2t) = 15 + 9t \stackrel{!}{=} 6 \quad\Longrightarrow\quad t = -1.$$

So the foot is $F = (3,3,3) - (2,1,2) = (1, 2, 1)$ — check: $2 + 2 + 2 = 6$ ✓ — and the walk's length is $\lvert t\rvert\,\lvert\mathbf{n}\rvert = 1 \cdot 3 = 3$, agreeing with the formula. One more step of the same walk gives the **reflection** of $P$ in the plane: $P + 2t\,\mathbf{n} = (-1, 1, -1)$ (a standard IB extension).

![[planes-3d-shadow-distance.svg|720]]

## A line and a plane — three relationships

A line $\mathbf{r} = \mathbf{a} + \lambda\mathbf{d}$ and a plane $\mathbf{r}\cdot\mathbf{n} = p$ can relate in exactly three ways, and one dot product — $\mathbf{d}\cdot\mathbf{n}$ — does the sorting:

| $\mathbf{d}\cdot\mathbf{n}$ | Point test | Relationship |
|---|---|---|
| $\neq 0$ | — | Meets the plane in **exactly one point** |
| $= 0$ | $\mathbf{a}\cdot\mathbf{n} = p$ | **Lies in** the plane |
| $= 0$ | $\mathbf{a}\cdot\mathbf{n} \neq p$ | **Parallel** to the plane, never meets |

Why does one number decide? Put the line's general point into the shadow reading:

$$\mathbf{r}(\lambda)\cdot\mathbf{n} = (\mathbf{a} + \lambda\mathbf{d})\cdot\mathbf{n} = \mathbf{a}\cdot\mathbf{n} + \lambda\,(\mathbf{d}\cdot\mathbf{n}).$$

The line's shadow is a *straight-line function of $\lambda$*, and $\mathbf{d}\cdot\mathbf{n}$ is its **slope**. Slope $\neq 0$: as $\lambda$ runs, the shadow sweeps past every mark on the flagpole exactly once — including the plane's mark $p$ — so the line meets the plane exactly once. Slope $= 0$: the line runs *level*, its shadow stuck at $\mathbf{a}\cdot\mathbf{n}$ forever — either the plane's own mark (lies in) or the wrong one (parallel). All three, on the running plane $\Pi: 2x + y + 2z = 6$:

**Meets.** $L_1: \mathbf{r} = (1, 0, 0) + \lambda(0, 2, 1)$. Here $\mathbf{d}\cdot\mathbf{n} = 0 + 2 + 2 = 4 \neq 0$: one intersection. Substitute the general point $(1,\; 2\lambda,\; \lambda)$:
$$2(1) + 2\lambda + 2\lambda = 2 + 4\lambda \stackrel{!}{=} 6 \quad\Longrightarrow\quad \lambda = 1,$$
landing at $(1, 2, 1)$ — the same landmark the perpendicular walk found, reached by a different road.

**Lies in.** $L_2: \mathbf{r} = (3, 0, 0) + \lambda(-3, 6, 0)$. Now $\mathbf{d}\cdot\mathbf{n} = -6 + 6 + 0 = 0$ *and* the anchor $(3,0,0)$ satisfies $6 = 6$ ✓ — the line is the edge $AB$, living inside $\Pi$. Both checks are compulsory: **direction alone proves nothing.**

**Parallel.** $L_3: \mathbf{r} = (1, 1, 5) + \lambda(1, 2, -2)$. Again $\mathbf{d}\cdot\mathbf{n} = 2 + 2 - 4 = 0$, but the anchor gives $2 + 1 + 10 = 13 \neq 6$: parallel, forever a distance $\lvert 13 - 6\rvert/3 = 7/3$ away.

![[planes-in-3d-line-cases.mp4]]

### The angle between a line and a plane — the complement trap

The dot product with $\mathbf{n}$ measures the angle to the *flagpole*, but the question asks for the angle to the *floor* — and those are complements. Hence the one formula on this page with a **sine**:

$$\sin\theta = \frac{\lvert\mathbf{d}\cdot\mathbf{n}\rvert}{\lvert\mathbf{d}\rvert\,\lvert\mathbf{n}\rvert}.$$

For $L_1$ above: $\sin\theta = \dfrac{4}{\sqrt{5}\cdot 3} = \dfrac{4\sqrt 5}{15}$, so $\theta \approx 36.6°$. (Sanity check the two extremes: a line *along* the normal has $\sin\theta = 1$, $\theta = 90°$ — it stabs the floor vertically ✓; a line *in* the plane has $\mathbf{d}\cdot\mathbf{n} = 0$, $\theta = 0°$ ✓.)

## Two planes — angle and line of intersection

Two non-parallel planes meet in a **line** (two tilted floors meet along a crease). Everything about the crease comes from the two normals.

**The angle between the planes** is the angle between their normals (tilt the flagpoles toward each other and the floors tilt by the same amount):

$$\cos\theta = \frac{\lvert\mathbf{n}_1\cdot\mathbf{n}_2\rvert}{\lvert\mathbf{n}_1\rvert\,\lvert\mathbf{n}_2\rvert}$$

with the absolute value picking the acute answer, which is what mark schemes want.

**The direction of the crease** must lie in *both* planes, hence be perpendicular to *both* normals — a job description the [[Cross Product]] answers by name: $\mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2$.

**Worked.** Intersect the running plane $\Pi_1: 2x + y + 2z = 6$ with $\Pi_2: x + y + z = 4$, $\mathbf{n}_2 = (1,1,1)$.

- *Angle:* $\cos\theta = \dfrac{\lvert 2+1+2 \rvert}{3\sqrt 3} = \dfrac{5\sqrt 3}{9}$, so $\theta \approx 15.8°$.
- *Direction:* $\mathbf{n}_1\times\mathbf{n}_2 = (2,1,2)\times(1,1,1) = (-1,\; 0,\; 1)$.
- *A point on the crease:* set $z = 0$ in both equations — $2x + y = 6$ and $x + y = 4$ — giving $x = 2$, $y = 2$. So

$$\ell:\quad \mathbf{r} = \begin{pmatrix}2\\2\\0\end{pmatrix} + t\begin{pmatrix}1\\0\\-1\end{pmatrix}.$$

*Verify in both planes* (30 seconds, marks-proof): $2(2{+}t) + 2 + 2(-t) = 6$ ✓ for every $t$; $(2{+}t) + 2 + (-t) = 4$ ✓. (If setting $z=0$ yields no solution, the crease is level in $z$ — set $x = 0$ or $y = 0$ instead.)

![[planes-in-3d-two-planes.mp4]]

## Skew lines — the parallel-plane sandwich

[[Vector Equations of Lines]] classified line pairs: parallel, intersecting, or **skew** — passing in space without meeting. The natural follow-up is *how far apart* two skew lines are, and the honest reason this question lives on the planes page:

> **Two skew lines always fit in a unique pair of parallel planes** — one containing each line, both with normal $\mathbf{n} = \mathbf{d}_1\times\mathbf{d}_2$ (perpendicular to both directions, so each plane can hold its line). The shortest distance between the lines *is* the gap between the planes: the shadow gap, again.

$$\boxed{\;\operatorname{dist}(\ell_1, \ell_2) = \frac{\lvert(\mathbf{a}_2 - \mathbf{a}_1)\cdot(\mathbf{d}_1\times\mathbf{d}_2)\rvert}{\lvert\mathbf{d}_1\times\mathbf{d}_2\rvert}\;}$$

**Worked.** $\ell_1: \mathbf{r} = (1,2,0) + s(1,0,1)$ and $\ell_2: \mathbf{r} = (0,0,4) + t(1,1,0)$.

- $\mathbf{n} = \mathbf{d}_1\times\mathbf{d}_2 = (1,0,1)\times(1,1,0) = (-1,\; 1,\; 1)$.
- The sandwich, explicitly: the plane through $\mathbf{a}_1$ with this normal has $p_1 = \mathbf{a}_1\cdot\mathbf{n} = -1+2+0 = 1$; through $\mathbf{a}_2$, $p_2 = 0+0+4 = 4$. Two parallel planes, marks $1$ and $4$ on the same flagpole.
- Distance $= \dfrac{\lvert 4 - 1\rvert}{\sqrt 3} = \sqrt 3$.

**The common perpendicular** — the unique segment meeting both lines at right angles — runs along $\mathbf{n}$ between the two feet. Write general points $F_1 = (1{+}s,\; 2,\; s)$ and $F_2 = (t,\; t,\; 4)$ and demand $F_2 - F_1 \parallel \mathbf{n}$:

$$\begin{pmatrix}t-1-s\\ t-2\\ 4-s\end{pmatrix} = k\begin{pmatrix}-1\\1\\1\end{pmatrix} \quad\Longrightarrow\quad \begin{cases} t - 1 - s = -k\\ t - 2 = k\\ 4 - s = k \end{cases}$$

From the last two equations, $t - 2 = 4 - s$, so $t = 6 - s$; substituting into the first gives $s = 3$, then $t = 3$, $k = 1$. The feet are $F_1 = (4, 2, 3)$ and $F_2 = (3, 3, 4)$; indeed $F_2 - F_1 = (-1, 1, 1)$ with length $\sqrt 3$ ✓ (matching the distance — the two methods must agree), and it dots to zero against both $\mathbf{d}_1$ and $\mathbf{d}_2$ ✓✓. The common perpendicular as a line:

$$\mathbf{r} = (4, 2, 3) + u(-1, 1, 1).$$

![[planes-in-3d-skew-sandwich.mp4]]

(An equivalent route sets $\vec{F_1F_2}\cdot\mathbf{d}_1 = 0$ and $\vec{F_1F_2}\cdot\mathbf{d}_2 = 0$ — two equations in $s, t$. Same answer, slightly messier algebra; the $\parallel\mathbf{n}$ route above knows the direction in advance.)

> [!info] The formula's best case — and its one true enemy
> Recall that skew lines can be **perpendicular**: the dot product reads directions only, so $\mathbf{d}_1\cdot\mathbf{d}_2 = 0$ needs no meeting point — the overpass crossing the road beneath at right angles (the full story lives in [[3D Vectors and the Scalar Product]] §2). For the sandwich construction that is the *most comfortable* case of all: $\lvert\mathbf{d}_1\times\mathbf{d}_2\rvert = \lvert\mathbf{d}_1\rvert\lvert\mathbf{d}_2\rvert\sin 90°$ is as large as it gets, so the formula is at its most stable. Its one true enemy is the opposite extreme — **parallel** lines, where $\mathbf{d}_1\times\mathbf{d}_2 = \mathbf{0}$ and the formula divides by zero; the distance between parallel lines is a point-to-line problem instead ([[Vector Equations of Lines]] §4 holds that machinery).

## Capstone — a full 9231-style question

> The plane $\Pi$ passes through $A(3,0,0)$, $B(0,6,0)$, $C(0,0,3)$.
> (a) Find a Cartesian equation of $\Pi$. (b) The line $L$ passes through $P(3,3,3)$ and meets $\Pi$ perpendicularly at $F$; find $F$ and the distance $PF$. (c) Find the acute angle between $\Pi$ and the plane $x + y + z = 4$.

Every part is worked above — (a) cross the edge vectors: $2x + y + 2z = 6$; (b) walk the normal: $F = (1,2,1)$, $PF = 3$; (c) dot the normals: $15.8°$. A real Paper 1 question chains the pieces exactly like this, typically for 10–12 marks, and the chain is always the same three tools: **cross for a normal, dot for an angle, substitute-and-solve for a meeting point.**

## Worked example — standalone, every tool named

Fresh numbers, nothing borrowed from the running plane — and worked in the discipline Kevin Houston's *How to Think Like a Mathematician* teaches: **before each step, name the fact you are about to use.** In the exam this habit is worth real marks (the examiner sees method even when arithmetic slips) and it is the fastest way to notice you've grabbed the wrong tool.

> The plane $\Sigma$ passes through $A(1, 0, 2)$, $B(3, 1, 1)$, $C(2, 2, 0)$, and the line $L$ has equation $\mathbf{r} = (1,1,1) + \lambda(1,2,2)$.
> (a) Find a Cartesian equation of $\Sigma$. (b) Find the distance from $P(4, 3, 5)$ to $\Sigma$, and the foot of the perpendicular from $P$. (c) Find the acute angle between $L$ and $\Sigma$.

**(a)** — *Tool: plane through three points — the normal is $\vec{AB}\times\vec{AC}$.*

$$\vec{AB} = \begin{pmatrix}2\\1\\-1\end{pmatrix}, \quad \vec{AC} = \begin{pmatrix}1\\2\\-2\end{pmatrix}, \quad \vec{AB}\times\vec{AC} = \begin{pmatrix}1(-2)-(-1)2\\ -\big(2(-2)-(-1)1\big)\\ 2(2)-1(1)\end{pmatrix} = \begin{pmatrix}0\\3\\3\end{pmatrix} = 3\begin{pmatrix}0\\1\\1\end{pmatrix}.$$

*Tool: normal form — $p = \mathbf{a}\cdot\mathbf{n}$ for any point $\mathbf{a}$ of the plane.* Take $\mathbf{n} = (0,1,1)$ and $A$: $p = 0 + 0 + 2 = 2$, so

$$\Sigma:\quad y + z = 2 \qquad \text{(check on } B: 1+1=2\ \checkmark, \; C: 2+0=2\ \checkmark).$$

**(b)** — *Tool: the shadow gap — $\operatorname{dist}(P, \Sigma) = \dfrac{\lvert\mathbf{a}\cdot\mathbf{n} - p\rvert}{\lvert\mathbf{n}\rvert}$.* With $P(4,3,5)$ and $\lvert\mathbf{n}\rvert = \sqrt{2}$:

$$\operatorname{dist} = \frac{\lvert(3 + 5) - 2\rvert}{\sqrt 2} = \frac{6}{\sqrt 2} = 3\sqrt 2.$$

*Tool: the foot by walking the normal — parametrise $\mathbf{r} = P + t\,\mathbf{n}$ and land on the plane.*

$$(3 + t) + (5 + t) = 2 \quad\Longrightarrow\quad t = -3 \quad\Longrightarrow\quad F = (4,\, 0,\, 2)$$

(check: $0 + 2 = 2$ ✓, and the walk's length $\lvert t\rvert\,\lvert\mathbf{n}\rvert = 3\sqrt2$ agrees with the formula — two tools, one answer).

**(c)** — *Tool: line–plane angle — the one with the sine, $\sin\theta = \dfrac{\lvert\mathbf{d}\cdot\mathbf{n}\rvert}{\lvert\mathbf{d}\rvert\,\lvert\mathbf{n}\rvert}$.* With $\mathbf{d} = (1,2,2)$, $\lvert\mathbf{d}\rvert = 3$:

$$\sin\theta = \frac{\lvert 0 + 2 + 2\rvert}{3\sqrt 2} = \frac{2\sqrt 2}{3} \quad\Longrightarrow\quad \theta \approx 70.5°.$$

Five steps, five named tools — and naming them is what catches the classic wrong-grab (reaching for $\cos$ in part (c) when the line–plane angle wants $\sin$).

## Common Misconceptions (Teaching Notes)

### 1. Putting the normal *in* the plane

Students asked for a plane through three points try to use $\mathbf{n}$ as a direction *inside* the plane, or quote in-plane vectors as the normal.

**Fix:** the flagpole picture — the normal sticks *out of* the floor; the spanning vectors lie *on* it. Mechanical check: an in-plane vector must dot to zero with $\mathbf{n}$ (test $\mathbf{b}\cdot\mathbf{n} = -6+6+0 = 0$ ✓).

### 2. Reading $p$ as the distance from the origin

$2x + y + 2z = 6$ does **not** put the plane $6$ from the origin — it's $6/\lvert\mathbf{n}\rvert = 2$ away.

**Fix:** the shadow is measured in units of $\hat{\mathbf{n}}$, so divide by $\lvert\mathbf{n}\rvert$ first. Multiplying the whole equation by 10 changes $p$ to 60 but moves the plane nowhere — $p$ alone can't be a distance.

### 3. Using cosine for the line–plane angle

The reflex $\cos\theta = \ldots$ computes the angle to the *normal*, and the mark scheme wanted the complement.

**Fix:** the one-sine rule: of the four angle formulas in 3D geometry (line–line, line–plane, plane–plane, all cosine-with-dot), **line–plane is the odd one out with sine** — because the question asks for the angle to the floor and the dot product measures against the flagpole. Sanity-check with the extremes ($\mathbf{d} \parallel \mathbf{n} \Rightarrow 90°$).

### 4. Direction test without the point test

Seeing $\mathbf{d}\cdot\mathbf{n} = 0$ and announcing "the line lies in the plane."

**Fix:** $\mathbf{d}\cdot\mathbf{n} = 0$ only says the line runs *level* — it distinguishes {lies-in or parallel} from {meets}, and the **anchor-point check** settles which ($L_2$ vs $L_3$ above differ only there). Two checks, always.

### 5. Dropping the absolute value in distances

$\mathbf{a}\cdot\mathbf{n} - p$ comes out negative and gets reported as a negative distance, or the sign is silently lost mid-working and a later part inherits the error.

**Fix:** the *signed* value is meaningful — its sign says which side of the plane you're on (the reflection trick uses exactly this) — but a distance is its magnitude. Keep the sign while working, wrap in $\lvert\ \rvert$ when answering.

## Exam Notes

### Cambridge 9231 Further Pure 1 (§1.6)

- The full menu is this page: all three plane forms + conversions "as necessary in solving problems"; line–plane relationships (lies in / parallel / meets, with the intersection point); foot of the perpendicular from a point to a plane; angle line–plane and plane–plane; the line of intersection of two planes; shortest distance between skew lines **and an equation of the common perpendicular** (the hardest standard ask — the worked $F_1, F_2$ method above is exactly what's expected).
- The vector product is assumed as a tool throughout ([[Cross Product]] holds it, including the $\sin\theta\,\hat{\mathbf{n}}$ and determinant forms the syllabus lists).
- Typical shape: a 10–14 mark structured question chaining plane-from-points → intersection/foot → angle or distance, as in the capstone.
- **Formula sheet:** MF19 gives *nothing* for planes — every formula on this page lives in your head (the shadow picture regenerates them all).

> [!tip] Draw it — even clumsily
> Every animation on this page is doing what your pencil should do in the exam: a plane is a slanted parallelogram, a normal is one arrow sticking out of it, a line is a stick. Ten seconds of rough sketch sorts *meets* from *parallel*, catches sign errors in distances, and tells you whether the angle you computed is the one with the floor or the one with the flagpole. The drawing isn't decoration — it's the cheapest error-check you're allowed to bring into the exam.

### IB AA HL (AHL 3.17–3.18)

- AHL 3.17: vector equation of a plane in both forms, and the Cartesian equation. AHL 3.18: intersections of line–plane and plane–plane, angles between them. Same toolkit; IB is fonder of **reflections** of points in planes (the "one more step of the walk" above) and of intersections of *three* planes in the linear-systems costume.
- Skew-line common perpendicular is 9231 territory, not IB's; the skew *distance* can appear in HL as a "shortest distance" problem.

### Edexcel IAL / A-Level Further (FP3 §5 / Core Pure)

- Edexcel's Further Pure carries planes, point-to-plane distance, line-of-intersection and skew-line distance with the same techniques; Core Pure (A-Level Further) covers the plane forms and intersections. The $\bigl(\mathbf{a}_2{-}\mathbf{a}_1\bigr)\cdot\hat{\mathbf{n}}$ distance pattern is identical across boards.

### Where it is *not* examined

- **9709**: P3 vectors (§3.7) stop at *lines* — no planes anywhere on 9709.
- **0606 / IGCSE**: vectors stay 2D.
- **AP Calculus**: no 3D vector geometry (that's multivariable calculus, beyond BC).

## Connections

- **Parent:** [[3D Vectors and the Scalar Product]] — the dot product *is* the shadow-reading this whole page runs on; [[Vector Equations of Lines]] — the one-parameter sibling, whose skew classification this page finishes with a distance.
- **Tool:** [[Cross Product]] — builds every normal here (plane through three points, line of intersection, skew-line sandwich); its scalar triple product is the numerator of the skew-distance formula in disguise.
- **The trilogy closes:** point (position vector) → line (one parameter) → plane (two parameters) — each object is "anchor + span," with one more direction of freedom each time.
- **Application:** [[Matrix]] — a system of three linear equations *is* three planes; solving it is asking where they meet (the configurations live under Beyond Syllabus).
- **For 9231 students:** [[MF19 Reference (9231)]] — no plane formulas are given; memorise or re-derive from the shadow picture.

## Beyond Syllabus

### Three planes — the configurations

Two planes meet in a line (or are parallel); *three* planes are where geometry meets algebra. The possibilities: a single point (the generic case — three floors pin one corner), a common line (a **sheaf**, like pages of an open book), a triangular **prism** (each pair meets, but the three crease lines are parallel — no common point), or parallel/coincident degeneracies. Solving $3\times 3$ linear systems is exactly classifying which configuration you're in — the [[Matrix]] determinant is zero precisely in the degenerate cases. The full algebra — the determinant-then-eliminate protocol, the census of configurations, and the real exam cases — lives at [[Linear Systems in 3D]].

### Hyperplanes — the idea that scales

Recall the counting: a line in 2D is $ax + by = c$ (one equation, one dimension lost), a plane in 3D is $ax+by+cz = p$. In $n$ dimensions, one linear equation carves out an $(n-1)$-dimensional **hyperplane** — same normal, same shadow reading, no new ideas. This is the workhorse of machine learning: a linear classifier (perceptron, SVM) is nothing but a hyperplane $\mathbf{w}\cdot\mathbf{x} = b$ in feature space, sorting points by *which side of the plane* they fall on — the signed version of misconception 5, monetised. The "margin" an SVM maximises is a point-to-hyperplane distance, computed with exactly this page's formula.

### The Hesse normal form

Dividing $\mathbf{r}\cdot\mathbf{n} = p$ by $\lvert\mathbf{n}\rvert$ (and fixing the sign so the right side is $\geq 0$) gives $\mathbf{r}\cdot\hat{\mathbf{n}} = p^\ast$ where $p^\ast$ *is* the origin distance — the **Hesse normal form**. Its virtue: plugging any point into the left side minus $p^\ast$ returns the *signed distance* directly, no division needed. Computer graphics engines store planes this way for exactly that reason — frustum culling tests millions of "which side is this vertex on?" queries per frame.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{r}\cdot\mathbf{n} = p$ | `\mathbf{r}\cdot\mathbf{n} = p` | Normal form |
| $\hat{\mathbf{n}}$ | `\hat{\mathbf{n}}` | Unit normal |
| $\lambda, \mu$ | `\lambda, \mu` | Plane parameters |
| $\mathbf{n}_1\times\mathbf{n}_2$ | `\mathbf{n}_1\times\mathbf{n}_2` | Line-of-intersection direction |
| $\vec{AB}$ | `\vec{AB}` | Edge vector between named points |
| $\begin{pmatrix}2\\1\\2\end{pmatrix}$ | `\begin{pmatrix}2\\1\\2\end{pmatrix}` | Column vector |
| $\stackrel{!}{=}$ | `\stackrel{!}{=}` | "Must equal" — the demand step |
| $\operatorname{dist}$ | `\operatorname{dist}` | Distance function |
