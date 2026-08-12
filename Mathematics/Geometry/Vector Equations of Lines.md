---
chinese: 直线的向量方程 (zhíxiàn de xiàngliàng fāngchéng)
prerequisites:
  - "[[3D Vectors and the Scalar Product]]"
  - "[[Vectors]]"
  - "[[Vector Geometry]]"
  - "[[Simultaneous Equations (Vocab)]]"
leads_to:
  - "[[Planes in 3D]]"
tags:
  - subject/mathematics
  - domain/geometry
  - domain/linear-algebra
  - level/A-Level
  - level/pre-IB
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/9709-3-7
  - syllabus/9231-1-6
  - type/technique
  - notation/vector
  - notation/parametric
  - notation/symmetric-form
  - misconception/mixing-position-and-direction
  - misconception/forgetting-third-equation
  - misconception/wrong-angle-convention
  - misconception/foot-of-perpendicular-setup
---

# Vector Equations of Lines 直线的向量方程

## Definition

### Formal

A **line in 3D space** can be specified by a single point on the line plus a direction. If $\mathbf{a}$ is the position vector of a known point on the line, and $\mathbf{d}$ is a non-zero direction vector along the line, then the **vector equation of the line** is

$$\boxed{\;\mathbf{r} = \mathbf{a} + t\,\mathbf{d}, \qquad t \in \mathbb{R}\;}$$

The parameter $t$ ranges over all real numbers; each value of $t$ gives the position vector $\mathbf{r}$ of a different point on the line. The line is the *set* of all such $\mathbf{r}$.

Equivalently, writing $\mathbf{r} = (x, y, z)^T$, $\mathbf{a} = (a_1, a_2, a_3)^T$, $\mathbf{d} = (d_1, d_2, d_3)^T$, the **parametric form**:

$$x = a_1 + t\,d_1, \qquad y = a_2 + t\,d_2, \qquad z = a_3 + t\,d_3.$$

### Intuitive

A line in 3D doesn't have a single equation like $y = mx + c$ does in 2D, because *two* numbers ($x$ and $y$) collapse to one constraint ($y - mx - c = 0$), but in 3D you have *three* coordinates and need *two* simultaneous constraints to pin down a line. So instead of an implicit equation, we use a **parametric** description: "start at $\mathbf{a}$, walk for time $t$ in direction $\mathbf{d}$."

This is, geometrically, the way a particle traces out its trajectory under constant velocity — and that's no coincidence. The vector equation of a line is just *uniform straight-line motion* viewed as a curve.

Two natural questions immediately follow:

1. **Given two points $A$ and $B$, what's the vector equation of the line through them?** Take $\mathbf{a} = \vec{OA}$ as the "start" and $\mathbf{d} = \vec{AB} = \mathbf{b} - \mathbf{a}$ as the direction. (See [[Vector Geometry]] for the master identity $\vec{AB} = \mathbf{b} - \mathbf{a}$.) Equation: $\mathbf{r} = \mathbf{a} + t(\mathbf{b} - \mathbf{a})$.
2. **How do two lines relate in 3D?** Three categories: **parallel**, **intersecting**, or **skew**. The third is a 3D-only phenomenon — two lines that neither meet nor run alongside each other, just pass by in space. Distinguishing among the three is the §3 of this card and the central exam-question shape.

### 中文锚点

**直线的向量方程**（zhíxiàn de xiàngliàng fāngchéng）：

$$\mathbf{r} = \mathbf{a} + t\,\mathbf{d}, \quad t \in \mathbb{R}$$

其中 $\mathbf{a}$ 是直线上一个已知点的位置向量，$\mathbf{d}$ 是直线的**方向向量**（direction vector），$t$ 是参数。

**几何理解**：从 $\mathbf{a}$ 出发，沿方向 $\mathbf{d}$ 走 $t$ 步。$t$ 取遍所有实数时，$\mathbf{r}$ 描出整条直线。

**两条直线在 3D 里的关系**（9709 P3 §3.7 核心）：
- **平行** (parallel)：$\mathbf{d}_2 = k\mathbf{d}_1$，方向向量成比例。
- **相交** (intersecting)：方向不同 + 联立方程有唯一解。
- **异面** (skew，"歪斜")：方向不同 + 联立方程**无解**。这是 3D 独有的情形——两条直线既不平行也不相交，就这样擦肩而过。
- **重合** (coincident)：方向相同 + 共享至少一个点 → 实际上是同一条线。

**两条直线的夹角**：用方向向量的点积，但取绝对值（因为直线没有"方向"，两个夹角 $\theta$ 和 $\pi - \theta$ 都对，约定取较小的那个）：

$$\cos\theta = \dfrac{|\mathbf{d}_1 \cdot \mathbf{d}_2|}{|\mathbf{d}_1||\mathbf{d}_2|}, \quad 0 \leq \theta \leq 90°.$$

---

## §1 Vector Equation of a Line

### From a point and a direction

Given a point $A$ with position vector $\mathbf{a}$ and a direction vector $\mathbf{d} \neq \mathbf{0}$:

$$\mathbf{r} = \mathbf{a} + t\mathbf{d}.$$

At $t = 0$: $\mathbf{r} = \mathbf{a}$ (you're at $A$). At $t = 1$: $\mathbf{r} = \mathbf{a} + \mathbf{d}$ (one step along the direction). At negative $t$: you're walking backwards.

![[vector-line-anatomy.svg|640]]

**Non-uniqueness.** The same line has *infinitely many* vector equations — pick any other point on the line as the "start," or scale the direction vector by any non-zero constant. Two equations $\mathbf{r} = \mathbf{a}_1 + t\mathbf{d}_1$ and $\mathbf{r} = \mathbf{a}_2 + s\mathbf{d}_2$ describe the same line iff $\mathbf{d}_2 = k\mathbf{d}_1$ (parallel directions) *and* $\mathbf{a}_2 - \mathbf{a}_1$ is parallel to $\mathbf{d}_1$ (the shift between starting points is along the line).

### From two points

Given points $A$ and $B$ with position vectors $\mathbf{a}, \mathbf{b}$: take the direction $\mathbf{d} = \mathbf{b} - \mathbf{a} = \vec{AB}$. The vector equation:

$$\mathbf{r} = \mathbf{a} + t(\mathbf{b} - \mathbf{a}).$$

At $t = 0$: at $A$. At $t = 1$: at $B$. So the segment $AB$ corresponds to $t \in [0, 1]$, and the full line corresponds to $t \in \mathbb{R}$.

### Parametric form

Expanding componentwise:

$$x = a_1 + t\,d_1, \quad y = a_2 + t\,d_2, \quad z = a_3 + t\,d_3.$$

Each component is a linear function of $t$. Three scalar equations sharing the single parameter $t$.

### Cartesian / symmetric form

Solve each component for $t$ (assuming all $d_i \neq 0$):

$$t = \dfrac{x - a_1}{d_1} = \dfrac{y - a_2}{d_2} = \dfrac{z - a_3}{d_3}.$$

This is the **symmetric form** — two equations (chaining three equal ratios), no parameter. Useful when you want a closed system of constraints; less useful when one of the $d_i = 0$ (in which case the corresponding component is constant, $x = a_1$ say, and the symmetric form is broken).

For 9709 P3 the parametric form is standard. Symmetric form appears in IB AA HL and university-level treatments.

### Worked example — line through two points

Find the vector equation of the line through $A(1, -2, 3)$ and $B(4, 0, -1)$.

Direction $\mathbf{d} = \vec{AB} = (4-1,\; 0-(-2),\; -1-3) = (3, 2, -4)$.

Vector equation: $\mathbf{r} = \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix} + t\begin{pmatrix} 3 \\ 2 \\ -4 \end{pmatrix}$.

Parametric form: $x = 1 + 3t$, $y = -2 + 2t$, $z = 3 - 4t$.

Symmetric form: $\dfrac{x - 1}{3} = \dfrac{y + 2}{2} = \dfrac{z - 3}{-4}$.

---

## §2 Parallel, Intersecting, Skew — The Line-Line Classification

In 3D space, two lines can be in one of four positional relationships:

| Configuration | Direction vectors | Algebraic test |
|---|---|---|
| **Coincident** (same line) | $\mathbf{d}_2 = k\mathbf{d}_1$ | share at least one point — equate parametric forms, solution exists |
| **Parallel** (distinct lines, same direction) | $\mathbf{d}_2 = k\mathbf{d}_1$ | share no points — equate parametric forms, system inconsistent |
| **Intersecting** | $\mathbf{d}_2 \not\propto \mathbf{d}_1$ | share exactly one point — equate parametric forms, *unique* solution |
| **Skew** | $\mathbf{d}_2 \not\propto \mathbf{d}_1$ | share no points — equate parametric forms, system inconsistent |

**The 3D-only feature is skew.** In 2D, two non-parallel lines *must* intersect (they live in the same plane, and any two non-parallel lines in a plane meet). In 3D, there's a third option: they can pass each other in space without meeting. Think of two airplane flight paths at different altitudes that cross above the same point on the ground — they never touch in 3D space.

![[line-pair-classification.svg|900]]

### The decision procedure

Given $L_1: \mathbf{r} = \mathbf{a}_1 + t\mathbf{d}_1$ and $L_2: \mathbf{r} = \mathbf{a}_2 + s\mathbf{d}_2$ (note the *different* parameter names — using the same parameter is a common error):

**Step 1: parallel check.** Are $\mathbf{d}_1$ and $\mathbf{d}_2$ parallel? Try to find $k$ with $\mathbf{d}_2 = k\mathbf{d}_1$ (compare ratios of components).
- **If parallel:** test whether $\mathbf{a}_2 - \mathbf{a}_1$ is also parallel to $\mathbf{d}_1$ — if yes, lines are coincident (same line); if no, lines are parallel but distinct.

**Step 2: intersection test (when not parallel).** Set $\mathbf{a}_1 + t\mathbf{d}_1 = \mathbf{a}_2 + s\mathbf{d}_2$. Componentwise this gives **three equations in two unknowns** $(t, s)$. Solve any two of them for $(t, s)$, then **substitute into the third equation** to check consistency.
- **If consistent:** lines intersect at the unique point given by $\mathbf{a}_1 + t\mathbf{d}_1$ (or equivalently $\mathbf{a}_2 + s\mathbf{d}_2$).
- **If inconsistent:** lines are skew.

> [!warning] The third-equation check is where marks are won and lost
> The most common 9709 P3 §3.7 trap: a student solves two of the three component equations for $(t, s)$, gets a unique answer, and concludes the lines intersect *without checking the third equation*. Two non-parallel lines in 3D *almost always* fail the third-equation check — they're almost always **skew**. **Always check all three components.** This step is usually worth 1–2 marks on its own.

### Worked example — intersecting vs skew

$L_1: \mathbf{r} = (1, 0, -1)^T + t(2, 1, 1)^T$
$L_2: \mathbf{r} = (4, 1, 0)^T + s(1, 1, -2)^T$

**Parallel?** $\mathbf{d}_1 = (2, 1, 1)$, $\mathbf{d}_2 = (1, 1, -2)$. Ratios $2/1, 1/1, 1/(-2)$ — not equal. Not parallel.

**Intersection test.** Equate parametric forms component by component:
- $x$: $1 + 2t = 4 + s$, so $s = 2t - 3$.
- $y$: $t = 1 + s$, so $s = t - 1$.

From the first two: $2t - 3 = t - 1 \Rightarrow t = 2, s = 1$.

**Check the $z$-equation:** $-1 + 1\cdot 2 = 1$ on the left; $0 + (-2)\cdot 1 = -2$ on the right. $1 \neq -2$. **Inconsistent.**

**Conclusion:** the lines are **skew**.

If the third equation *had* been consistent — say if $L_2$ had been $(4, 1, 3)^T + s(1, 1, -2)^T$ — then $t = 2$ would give the intersection point on $L_1$: $(1+4, 0+2, -1+2) = (5, 2, 1)$. Sanity-check by also computing the point on $L_2$ at $s = 1$: $(4+1, 1+1, 3-2) = (5, 2, 1)$. ✓

---

## §3 Angle Between Two Lines

The angle between two lines is the angle between their direction vectors — but with a twist. Lines have **no orientation**: the line through points $A$ and $B$ is the same set as the line through $B$ and $A$, so the direction vector can be taken either way. Reversing $\mathbf{d}$ flips $\theta$ to $\pi - \theta$, so the cosine flips sign.

**Convention.** Take the *acute* angle between the lines. Algebraically, use the **absolute value** of the dot product:

$$\boxed{\;\cos\theta = \dfrac{\lvert\mathbf{d}_1 \cdot \mathbf{d}_2\rvert}{\lvert\mathbf{d}_1\rvert\,\lvert\mathbf{d}_2\rvert}, \qquad 0 \leq \theta \leq 90°.\;}$$

(Compare to the angle between two *vectors* — see [[3D Vectors and the Scalar Product]] §3 — which can range over $[0°, 180°]$ and where the absolute value is **not** used. Vectors have orientation, lines don't.)

**This angle doesn't care whether the lines meet.** The formula reads only the two *direction* vectors — position never enters — so it assigns an angle to skew lines just as happily as to intersecting ones. In particular, **skew lines can be perpendicular**: $\mathbf{d}_1\cdot\mathbf{d}_2 = 0$ with no common point, like a highway overpass crossing the road beneath at right angles (the full callout lives in [[3D Vectors and the Scalar Product]] §2; what it means for the skew-distance formula is at the end of [[Planes in 3D]] §"Skew lines — the parallel-plane sandwich").

### Worked example — angle between two lines

Continuing with the lines above, find the angle between $L_1$ and $L_2$.

$\mathbf{d}_1 \cdot \mathbf{d}_2 = 2\cdot 1 + 1\cdot 1 + 1\cdot(-2) = 2 + 1 - 2 = 1.$

$\lvert\mathbf{d}_1\rvert = \sqrt{4+1+1} = \sqrt{6}$, $\lvert\mathbf{d}_2\rvert = \sqrt{1+1+4} = \sqrt{6}$.

$\cos\theta = \dfrac{|1|}{\sqrt{6}\cdot\sqrt{6}} = \dfrac{1}{6}$, so $\theta = \arccos(1/6) \approx 80.4°$. ✓ within $[0°, 90°]$.

> [!info] Lines don't have direction; vectors do
> The reason for the absolute value in the line-angle formula but *not* in the vector-angle formula is that **lines are sets, not arrows**. The line $\{(1+2t, t, -1+t) : t \in \mathbb{R}\}$ is the same set whether you parametrise with $t$ or with $-t$ — you'd just be walking the line backwards. So the direction vector $\mathbf{d}$ and its negative $-\mathbf{d}$ describe the same line, and the angle between two lines must be the same whether you flip either direction. Taking $\lvert\cos\rvert$ enforces this.

---

## §4 Foot of Perpendicular and Distance from a Point to a Line

Standard 9709 P3 §3.7 extension question: given a point $P$ (not on a line $L$) and the line $L: \mathbf{r} = \mathbf{a} + t\mathbf{d}$, find:

1. The **foot of the perpendicular** from $P$ to $L$ — the point $F$ on $L$ closest to $P$.
2. The **perpendicular distance** $\lvert PF\rvert$ from $P$ to $L$.

### The perpendicularity condition

$F$ is the foot of perpendicular iff $\vec{PF}$ is perpendicular to the line, i.e. $\vec{PF} \cdot \mathbf{d} = 0$.

Parametrise: any point $F$ on $L$ has position vector $\mathbf{r}(t) = \mathbf{a} + t\mathbf{d}$. The displacement from $P$ to $F$ is $\vec{PF} = \mathbf{r}(t) - \mathbf{p} = (\mathbf{a} - \mathbf{p}) + t\mathbf{d}$.

Setting $\vec{PF} \cdot \mathbf{d} = 0$:

$$[(\mathbf{a} - \mathbf{p}) + t\mathbf{d}] \cdot \mathbf{d} = 0 \;\Rightarrow\; (\mathbf{a} - \mathbf{p}) \cdot \mathbf{d} + t\,(\mathbf{d}\cdot\mathbf{d}) = 0 \;\Rightarrow\; t = \dfrac{(\mathbf{p} - \mathbf{a})\cdot \mathbf{d}}{\mathbf{d}\cdot\mathbf{d}}.$$

Plug this $t$ back into $\mathbf{r}(t)$ to get the foot $F$. The distance is then $\lvert\vec{PF}\rvert = \lvert F - P\rvert$.

### Worked example

Find the foot of perpendicular from $P = (5, 1, 4)$ to the line $L: \mathbf{r} = (1, 0, -1)^T + t(2, 1, 1)^T$.

$\mathbf{p} - \mathbf{a} = (5-1, 1-0, 4-(-1)) = (4, 1, 5)$.

$(\mathbf{p} - \mathbf{a}) \cdot \mathbf{d} = 4\cdot 2 + 1\cdot 1 + 5\cdot 1 = 14$.

$\mathbf{d} \cdot \mathbf{d} = 4 + 1 + 1 = 6$.

$t = 14/6 = 7/3$.

Foot $F = \mathbf{a} + t\mathbf{d} = (1, 0, -1) + (7/3)(2, 1, 1) = (1 + 14/3,\; 7/3,\; -1 + 7/3) = (17/3,\; 7/3,\; 4/3)$.

Distance $\lvert \vec{PF}\rvert$:
$\vec{PF} = F - P = (17/3 - 5,\; 7/3 - 1,\; 4/3 - 4) = (2/3,\; 4/3,\; -8/3)$.
$\lvert\vec{PF}\rvert = \sqrt{(2/3)^2 + (4/3)^2 + (8/3)^2} = \sqrt{(4 + 16 + 64)/9} = \sqrt{84/9} = \dfrac{2\sqrt{21}}{3}$.

---

## §5 Common Misconceptions

### 1. Mixing up position vector and direction vector

A student writes the line as $\mathbf{r} = \vec{AB} + t\,\vec{OA}$ — using a direction as the starting point and the start as the direction. The result is some other line entirely.

**Fix.** The structure is *position* $+ t \cdot$ *direction*. **Position vectors** $\vec{OA}, \vec{OB}$ point from the origin to specific named points on the line. **Direction vectors** $\vec{AB} = \mathbf{b} - \mathbf{a}$ are *displacements* between two points on the line. Mentally label them when writing the equation: $\mathbf{r} = (\text{position of a point on the line}) + t \cdot (\text{direction along the line})$.

### 2. Reusing the same parameter for two lines

Writing $L_1: \mathbf{r} = \mathbf{a}_1 + t\mathbf{d}_1$ and $L_2: \mathbf{r} = \mathbf{a}_2 + t\mathbf{d}_2$ — using $t$ for both. Then equating them and trying to solve. *Wrong* — the two parameters are independent. The point where $L_1$ has parameter $t_1$ does not generally correspond to the point where $L_2$ has the same parameter value.

**Fix.** **Use different letters for different lines** — typically $t$ for $L_1$ and $s$ for $L_2$. When testing intersection, you're solving for both $t$ and $s$ simultaneously.

### 3. Forgetting the third-equation consistency check

Solving two components for $(t, s)$, getting a unique answer, and concluding "the lines intersect" without checking the third component. *Almost certainly wrong* — two non-parallel lines in 3D are skew with probability 1, intersecting only when the third equation happens to be consistent.

**Fix.** *Always check all three components.* Solve two for $(t, s)$, then verify by substituting into the third. If the third equation is consistent, lines intersect; if not, lines are skew. **This step is worth 1–2 marks on the mark scheme.**

### 4. Wrong angle convention

Writing $\cos\theta = \dfrac{\mathbf{d}_1 \cdot \mathbf{d}_2}{\lvert\mathbf{d}_1\rvert\lvert\mathbf{d}_2\rvert}$ for the angle between two *lines* (without the absolute value) and getting an obtuse angle (e.g. $130°$). The angle between two lines should be in $[0°, 90°]$.

**Fix.** **Lines need $|\cdot|$**: $\cos\theta = \dfrac{\lvert\mathbf{d}_1 \cdot \mathbf{d}_2\rvert}{\lvert\mathbf{d}_1\rvert\lvert\mathbf{d}_2\rvert}$. Vectors don't need $|\cdot|$. The difference is that lines have no orientation. Memorise the policy: *line angle → absolute value; vector angle → no absolute value*.

### 5. Setting up the foot of perpendicular wrong

Writing $\vec{PF}$ as $\mathbf{p} - \mathbf{r}(t)$ instead of $\mathbf{r}(t) - \mathbf{p}$ — or vice versa. Either is fine *as a vector*, but if you mix conventions mid-problem the sign of $t$ flips and you get a different answer.

**Fix.** *Pick one convention and stick to it.* Standard choice: $\vec{PF} = F - P = \mathbf{r}(t) - \mathbf{p}$. Then the perpendicularity condition $\vec{PF} \cdot \mathbf{d} = 0$ gives $t = \dfrac{(\mathbf{p} - \mathbf{a})\cdot \mathbf{d}}{\mathbf{d}\cdot\mathbf{d}}$.

### 6. Confusing line equation with segment

The vector equation $\mathbf{r} = \mathbf{a} + t(\mathbf{b} - \mathbf{a})$ describes the *entire line through $A$ and $B$* for $t \in \mathbb{R}$, not just the segment $AB$. The segment corresponds to $t \in [0, 1]$.

**Fix.** Read the question. *"Line through $A$ and $B$"* → $t \in \mathbb{R}$. *"Segment $AB$"* or *"line from $A$ to $B$"* → $t \in [0, 1]$. *"Ray from $A$ through $B$"* → $t \in [0, \infty)$.

---

## §6 Exam Notes

### Cambridge 9709 (A-Level)

**Syllabus refs:** Paper 3 §3.7 — *vectors*. Specifically: vector equations of lines in 3D, finding lines from a point and direction or from two points, parallel/intersecting/skew classification, angle between two lines.

**Typical question shape (10–14 marks, often as one of the long-answer questions):**
1. *Find the vector equation of the line through $A$ and $B$.* (2 marks)
2. *Show that lines $L_1$ and $L_2$ are not parallel and do not intersect (i.e. they are skew).* (4–5 marks — the intersection test with the third-equation consistency check)
3. *Find the angle between $L_1$ and $L_2$.* (3–4 marks — dot product, magnitudes, $|\cos|$ formula, $\arccos$)
4. *Find the position vector of the foot of the perpendicular from $P$ to $L_1$, and hence the perpendicular distance from $P$ to $L_1$.* (4–5 marks)

**Tip.** When asked to *show* lines are skew, both the *not parallel* check (different direction vectors, not proportional) and the *not intersecting* check (third-equation fails) are required. Mark schemes typically award marks for each step explicitly.

### Cambridge 9231 Further Pure 1 (§1.6)

FP1 assumes everything on this card and extends it one dimension up: line–plane intersections and angles, the foot of a perpendicular dropped onto a *plane*, and the skew-line questions upgraded from *classify* (this page's job) to *measure* — the shortest distance between skew lines and an equation of their common perpendicular. The plane machinery lives at [[Planes in 3D]]; the classification procedure here — especially the third-equation consistency check — is still where every FP1 skew question starts.

### A-Level (Edexcel / AQA / OCR / MEI)

All A-Level boards include vector equations of lines in A2 Pure. Same content as 9709 P3 §3.7. Edexcel and AQA also include **equations of planes** ($\mathbf{n} \cdot (\mathbf{r} - \mathbf{a}) = 0$) and *line-plane intersection* ([[Planes in 3D]] covers the toolkit); OCR MEI Further Pure adds *plane-plane intersection* yielding a line.

### IB AA HL

**Topic 3 (Geometry and Trigonometry).** Includes everything in this card *plus* the equation of a plane in three forms (vector, parametric, Cartesian $ax + by + cz = d$), line-plane intersection, plane-plane intersection (the line of intersection of two planes), and angles between line-plane and plane-plane. Heavier than 9709 P3 §3.7.

AA SL does not cover 3D vector geometry.

### AP Calculus

**Not on AP Calculus AB or BC.** Vectors appear in AP Physics and in university Multivariable Calculus / Linear Algebra.

### Beyond high school — University

3D vector geometry extends to:

- **Planes** — the one-dimension-up sibling: point-normal form, distances, intersections, the skew-line sandwich. The full treatment is at [[Planes in 3D]].
- **Linear algebra** — lines and planes generalise to *affine subspaces* of $\mathbb{R}^n$. Any $k$-dimensional subspace can be written as $\mathbf{a} + \text{span}(\mathbf{d}_1, \ldots, \mathbf{d}_k)$. Lines are the $k = 1$ case.
- **Computer graphics** — every 3D model is a mesh of triangles, every triangle has three vertices each with a position vector. Lighting calculations use point-to-plane distances and ray-plane intersections (rays = lines). Real-time ray-tracing (in modern GPUs) literally solves the line-plane intersection problem millions of times per second.
- **Robotics and aerospace** — flight paths, robot arm trajectories, satellite orbits all parametrise as $\mathbf{a}(t) + t\mathbf{d}(t)$ or more general curves. The vector-equation formalism is foundational.

---

## Connections

- **Direct prerequisite:** [[3D Vectors and the Scalar Product]] — Card A of the §3.7 pair. The dot product appears throughout this card (angle formula, perpendicularity for foot-of-perpendicular). Read first.
- **Direct prerequisite:** [[Vectors]] — the 2D foundation.
- **Direct prerequisite:** [[Vector Geometry]] — for the master identity $\vec{AB} = \mathbf{b} - \mathbf{a}$ used in the "line from two points" construction.
- **Direct prerequisite:** [[Simultaneous Equations (Vocab)]] — the intersection test is a small linear system in $(t, s)$.
- **Sibling:** [[Coordinate Geometry of the Circle]] — the 2D analogue: circles in the plane have implicit Cartesian equations $(x - a)^2 + (y - b)^2 = r^2$; lines in 3D have explicit parametric equations $\mathbf{r} = \mathbf{a} + t\mathbf{d}$. Different geometric objects, different representation strategies, same coordinate-geometry mindset.
- **Closes:** Half of 9709 P3 §3.7 (the other half is in Card A). Together they take §3.7 from 🟡 → 🟢. **P3 now at 9/9 = 100% green.**
- **For 9709 students:** [[MF19 Reference (9709)]] — the line equation $\mathbf{r} = \mathbf{a} + t\mathbf{d}$ is on the MF19 sheet. The angle formula and the foot-of-perpendicular formula are *not* — you must derive them from the dot product.

---

## Beyond Syllabus

### Equation of a plane — the IB AA HL extension

A plane in 3D is specified by a point $\mathbf{a}$ on the plane and a **normal vector** $\mathbf{n}$ perpendicular to the plane. The defining condition for a point $\mathbf{r}$ to lie on the plane: $\vec{(\mathbf{r} - \mathbf{a})} \perp \mathbf{n}$, i.e.

$$\boxed{\;\mathbf{n} \cdot (\mathbf{r} - \mathbf{a}) = 0\;} \qquad \text{or equivalently} \qquad \mathbf{n}\cdot\mathbf{r} = \mathbf{n}\cdot\mathbf{a} = d.$$

The Cartesian form: if $\mathbf{n} = (n_1, n_2, n_3)$ and $d = \mathbf{n}\cdot\mathbf{a}$, then $n_1 x + n_2 y + n_3 z = d$ — a single linear equation in three variables, the natural 3D analogue of $ax + by = c$ in 2D.

Lines and planes are *complementary*: lines have one direction vector and need two equations to pin them down (or one parametric description); planes have one normal vector and need one equation (or two parametric directions). The pattern generalises: in $\mathbb{R}^n$, a $k$-dimensional affine subspace needs $n - k$ Cartesian equations or $k$ parametric directions to specify.

### Distance from a point to a plane

If $\Pi$ is a plane $\mathbf{n}\cdot\mathbf{r} = d$ and $P$ has position vector $\mathbf{p}$, the perpendicular distance is

$$\text{dist}(P, \Pi) = \dfrac{\lvert \mathbf{n}\cdot\mathbf{p} - d\rvert}{\lvert\mathbf{n}\rvert}.$$

Derivation: the foot of perpendicular from $P$ lies along the normal from $P$; parametrise $\mathbf{r} = \mathbf{p} + t\mathbf{n}$, substitute into the plane equation, solve for $t$, the distance is $\lvert t\mathbf{n}\rvert = \lvert t\rvert \lvert\mathbf{n}\rvert$.

### Line-plane intersection

Substitute the line's parametric form $\mathbf{r} = \mathbf{a} + t\mathbf{d}$ into the plane's equation $\mathbf{n}\cdot\mathbf{r} = d$:

$$\mathbf{n}\cdot(\mathbf{a} + t\mathbf{d}) = d \;\Rightarrow\; t = \dfrac{d - \mathbf{n}\cdot\mathbf{a}}{\mathbf{n}\cdot\mathbf{d}}.$$

If $\mathbf{n}\cdot\mathbf{d} \neq 0$ (line not parallel to plane), the unique solution gives the intersection point. If $\mathbf{n}\cdot\mathbf{d} = 0$ and $\mathbf{n}\cdot\mathbf{a} = d$ (line lies in plane), every $t$ is a solution. If $\mathbf{n}\cdot\mathbf{d} = 0$ but $\mathbf{n}\cdot\mathbf{a} \neq d$ (line parallel to plane, not in it), no solution.

The same trichotomy as the line-line classification: unique intersection, infinitely many (subsumed), or none (parallel/skew).

### The cross product perspective

The direction vector of the line of intersection of two planes (with normals $\mathbf{n}_1, \mathbf{n}_2$) is $\mathbf{n}_1 \times \mathbf{n}_2$ — the cross product. *That's* what the cross product is good for here: producing a vector perpendicular to two given vectors.

Cross product also lets you compute distances cleanly. **Distance from a point $P$ to a line $\mathbf{r} = \mathbf{a} + t\mathbf{d}$**:

$$\text{dist}(P, L) = \dfrac{\lvert \vec{AP} \times \mathbf{d}\rvert}{\lvert\mathbf{d}\rvert}.$$

This is the area of the parallelogram with sides $\vec{AP}$ and $\mathbf{d}$, divided by the length of $\mathbf{d}$ — i.e., the perpendicular height. Much cleaner than the foot-of-perpendicular approach for distance-only questions; equivalent for finding the foot.

### Skew lines and the common perpendicular

Two skew lines $L_1, L_2$ have a **unique common perpendicular** — a single line that meets both at right angles. The length of this common perpendicular is the *minimum distance* between the two skew lines, computable via:

$$\text{dist}(L_1, L_2) = \dfrac{\lvert (\mathbf{a}_2 - \mathbf{a}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2) \rvert}{\lvert\mathbf{d}_1 \times \mathbf{d}_2\rvert}.$$

The numerator is the **scalar triple product**, geometrically the volume of the parallelepiped spanned by $\mathbf{a}_2 - \mathbf{a}_1, \mathbf{d}_1, \mathbf{d}_2$; the denominator is the area of the base parallelogram. Volume / area = height = distance. *Beautiful formula, IB AA HL territory.*

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{r} = \mathbf{a} + t\mathbf{d}$ | `\mathbf{r} = \mathbf{a} + t\mathbf{d}` | Vector equation of a line |
| $\vec{AB}$ | `\vec{AB}` | Displacement from $A$ to $B$ |
| $t \in \mathbb{R}$ | `t \in \mathbb{R}` | Parameter ranges over all reals |
| $\dfrac{x - a_1}{d_1} = \dfrac{y - a_2}{d_2} = \dfrac{z - a_3}{d_3}$ | (as written) | Symmetric (Cartesian) form |
| $\cos\theta = \dfrac{\lvert\mathbf{d}_1\cdot\mathbf{d}_2\rvert}{\lvert\mathbf{d}_1\rvert\lvert\mathbf{d}_2\rvert}$ | (as written) | Angle between two **lines** — note the $\lvert\cdot\rvert$ |
| $\mathbf{n}\cdot(\mathbf{r} - \mathbf{a}) = 0$ | `\mathbf{n}\cdot(\mathbf{r} - \mathbf{a}) = 0` | Equation of a plane (beyond syllabus) |
| $\mathbf{d}_1 \times \mathbf{d}_2$ | `\mathbf{d}_1 \times \mathbf{d}_2` | Cross product (beyond syllabus) |
