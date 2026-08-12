---
chinese: 三维向量与数量积 (sānwéi xiàngliàng yǔ shùliàng jī)
prerequisites:
  - "[[Vectors]]"
  - "[[Trigonometric Ratios]]"
  - "[[Pythagoras Theorem]]"
  - "[[Magnitude of a Vector (Vocab)]]"
leads_to:
  - "[[Vector Equations of Lines]]"
  - "[[Cross Product]]"
  - "[[Planes in 3D]]"
tags:
  - subject/mathematics
  - domain/geometry
  - domain/linear-algebra
  - level/A-Level
  - level/pre-IB
  - level/pre-AP
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/9709-3-7
  - syllabus/9231-1-6
  - type/technique
  - notation/vector
  - notation/dot-product
  - misconception/dot-product-vs-multiplication
  - misconception/forgetting-cosine-direction
  - misconception/zero-vs-perpendicular
---

# 3D Vectors and the Scalar Product 三维向量与数量积

## Definition

### Formal

A **3D vector** is an ordered triple $\mathbf{v} = (v_1, v_2, v_3)$ representing a displacement in three-dimensional space, equivalently written

$$\mathbf{v} = v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k} \qquad \text{or} \qquad \mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix},$$

where $\mathbf{i}, \mathbf{j}, \mathbf{k}$ are the standard unit vectors along the $x$, $y$, $z$ axes respectively. The **magnitude** is $|\mathbf{v}| = \sqrt{v_1^2 + v_2^2 + v_3^2}$ — Pythagoras in three dimensions.

The **scalar product** (also called *dot product* or *inner product*) of two 3D vectors $\mathbf{a}, \mathbf{b}$ is a *number* (not a vector) defined by either of two equivalent formulas:

$$\boxed{\;\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 \;=\; |\mathbf{a}|\,|\mathbf{b}|\,\cos\theta\;}$$

where $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$. The equivalence of the two formulas is the **load-bearing identity** of the entire chapter — it's what makes the dot product useful, because the algebraic side (left) is easy to compute from coordinates, while the geometric side (right) gives the angle.

### Intuitive

Everything you already know from [[Vectors]] in 2D extends to 3D with no surprises: addition, subtraction, scalar multiplication, magnitude. The only structural new thing is the **third axis** — depth, $z$ — which gives objects in space room to be *not* in the same plane as each other. That's where the geometry gets interesting: two lines in 2D are either parallel, equal, or intersecting; in 3D they can also be **skew** — neither parallel nor intersecting, just passing by each other in space. (Detailed in the companion card [[Vector Equations of Lines]].)

The new operation is the **scalar product**, $\mathbf{a} \cdot \mathbf{b}$. It is *not* the same as ordinary multiplication — for one thing, its inputs are vectors and its output is a number. The point of the operation is the second formula above: **the dot product extracts the cosine of the angle between two vectors**, with the magnitudes mixed in. Three consequences:

1. **Perpendicularity test.** If $\mathbf{a}, \mathbf{b}$ are non-zero, then $\mathbf{a} \cdot \mathbf{b} = 0 \iff \theta = 90°$. So you can check perpendicularity by computing one number.
2. **Angle measurement.** Rearranging: $\cos\theta = \dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}| |\mathbf{b}|}$. This is the *primary* way to find the angle between two vectors (and, in the companion card, between two lines).
3. **Computer-graphics workhorse.** Surface lighting in every 3D game is $\text{brightness} = \mathbf{n} \cdot \mathbf{L}$ where $\mathbf{n}$ is the surface normal and $\mathbf{L}$ is the light direction. The cosine of the angle between them sets the pixel's brightness. Pixar, Unreal, every shader does this.

### 中文锚点

**三维向量**（sānwéi xiàngliàng）：在三维空间里的有向位移，写作 $\mathbf{v} = v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$ 或列向量 $(v_1, v_2, v_3)^T$。

**模长**（magnitude / 模）：$|\mathbf{v}| = \sqrt{v_1^2 + v_2^2 + v_3^2}$（三维勾股定理）。

**数量积 / 点积 / 内积**（scalar product / dot product / inner product，简称**点积**）：

$$\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3 = |\mathbf{a}||\mathbf{b}|\cos\theta$$

两个等号是数量积的**核心恒等式**。左边可以**算**，右边可以**用**。

**两大用途：**
1. **判垂直**：$\mathbf{a} \cdot \mathbf{b} = 0$ 当且仅当 $\mathbf{a} \perp \mathbf{b}$（前提非零向量）。
2. **求夹角**：$\cos\theta = \dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}$。

中文教材也称为"内积"或"标积"。注意它输出**一个数**，不是向量（"数量积"的"数量"就是 scalar 的意思）。和**叉积**（cross product / 外积 / 向量积）不一样——叉积输出一个垂直向量，9709 P3 不考，9231 才考。

---

## §1 The 3D Extension

All the algebra from [[Vectors]] carries over to 3D unchanged. Add and subtract componentwise; scalar-multiply componentwise; magnitude via Pythagoras with one more squared term.

### Standard basis $\mathbf{i}, \mathbf{j}, \mathbf{k}$

The three unit vectors along the coordinate axes:

$$\mathbf{i} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \mathbf{j} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \mathbf{k} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}.$$

Every 3D vector decomposes uniquely as $\mathbf{v} = v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$. The $\mathbf{i}\mathbf{j}\mathbf{k}$ notation is preferred in physics and engineering; the column-vector notation is preferred in linear algebra. Both notations mean the same thing — 9709 P3 uses both interchangeably and you should be fluent in switching.

### Magnitude

$$|\mathbf{v}| = \sqrt{v_1^2 + v_2^2 + v_3^2}.$$

**Derivation.** Draw the box with corners at $(0, 0, 0)$ and $(v_1, v_2, v_3)$. The face diagonal in the $xy$-plane has length $\sqrt{v_1^2 + v_2^2}$ by [[Pythagoras Theorem|Pythagoras]] in 2D. The space diagonal (which *is* $|\mathbf{v}|$) has length $\sqrt{(\text{face diag})^2 + v_3^2} = \sqrt{v_1^2 + v_2^2 + v_3^2}$ by Pythagoras applied again. **Pythagoras twice.**

![[3d-vector-box-diagonal.svg|640]]

### Unit vector

For non-zero $\mathbf{v}$, the **unit vector in the direction of $\mathbf{v}$** is $\hat{\mathbf{v}} = \dfrac{\mathbf{v}}{|\mathbf{v}|}$. Same formula as 2D, no change.

### Worked arithmetic example

Let $\mathbf{a} = 2\mathbf{i} + 3\mathbf{j} - \mathbf{k}$ and $\mathbf{b} = \mathbf{i} - 2\mathbf{j} + 4\mathbf{k}$.

- $\mathbf{a} + \mathbf{b} = 3\mathbf{i} + \mathbf{j} + 3\mathbf{k}$
- $\mathbf{a} - \mathbf{b} = \mathbf{i} + 5\mathbf{j} - 5\mathbf{k}$
- $2\mathbf{a} = 4\mathbf{i} + 6\mathbf{j} - 2\mathbf{k}$
- $|\mathbf{a}| = \sqrt{4 + 9 + 1} = \sqrt{14}$
- $|\mathbf{b}| = \sqrt{1 + 4 + 16} = \sqrt{21}$
- Unit vector in direction of $\mathbf{a}$: $\hat{\mathbf{a}} = \dfrac{1}{\sqrt{14}}(2\mathbf{i} + 3\mathbf{j} - \mathbf{k})$

These computations are mechanical once the 2D versions feel natural. *The only new feature is the third component carrying along through every step.*

---

## §2 The Scalar Product — Definition and the Two Formulas

The scalar product is what makes 3D vectors *useful for geometry*. Without it, you'd have vector arithmetic but no way to talk about angles or perpendicularity.

> [!tip] What the dot product *means* — alignment between two vectors
> Before the formulas, here is what the dot product is *for*: **it measures how much two vectors line up in the same direction.** The output is a signed scalar that smoothly tracks the angle between them:
>
> | Angle $\theta$ | $\mathbf{a}\cdot\mathbf{b}$ | Reading |
> |---|---|---|
> | $0°$ (parallel, same way) | $+\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert$ | **full alignment** — degenerates to direct product of magnitudes |
> | acute ($0° < \theta < 90°$) | positive, less than $\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert$ | partial alignment |
> | $90°$ (perpendicular) | $0$ | **no alignment** |
> | obtuse ($90° < \theta < 180°$) | negative, $\geq -\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert$ | partial anti-alignment |
> | $180°$ (anti-parallel) | $-\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert$ | **full opposition** |
>
> So the dot product is a *signed alignment indicator*, scaled by the two magnitudes. When two unit vectors point the same way, $\mathbf{a}\cdot\mathbf{b} = 1$; when they're perpendicular, it's $0$; when they point opposite ways, it's $-1$. *That's why the dot product is the natural definition of "similarity" between two vectors* — in $\mathbb{R}^{768}$ ML embeddings, in $\mathbb{R}^3$ physics, anywhere two vectors live.
>
> The two formulas below are just two ways to *compute* this alignment indicator — one algebraic (from coordinates), one geometric (from magnitudes and angle). The equivalence proof in the next subsection shows they agree.

### Component formula

$$\mathbf{a} \cdot \mathbf{b} = a_1 b_1 + a_2 b_2 + a_3 b_3.$$

Multiply matching components and add. The result is a **scalar** (a number), not a vector. (That's why "scalar product" — the *output* is a scalar.)

**Quick example.** $\mathbf{a} = (2, 3, -1)$, $\mathbf{b} = (1, -2, 4)$. $\mathbf{a} \cdot \mathbf{b} = 2 \cdot 1 + 3 \cdot (-2) + (-1)(4) = 2 - 6 - 4 = -8$.

### Geometric formula

$$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}|\,|\mathbf{b}|\,\cos\theta$$

where $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$ when they start from the same point ($0 \leq \theta \leq \pi$).

**Reading the formula:** the dot product is **positive** when the vectors point in similar directions ($\theta < 90°$, $\cos\theta > 0$); **zero** when perpendicular ($\theta = 90°$); **negative** when pointing in opposing directions ($\theta > 90°$).

![[3d-vector-alignment-indicator.svg|900]]

> [!info] Can skew lines be perpendicular?
> Yes — and the dot product doesn't even notice they're skew. The dot product reads **directions only** — position never enters $a_1b_1 + a_2b_2 + a_3b_3$ — so it assigns an angle to *any* pair of lines, meeting or not, and the perpendicularity test $\mathbf{d}_1\cdot\mathbf{d}_2 = 0$ works just as well on lines that never touch. A highway overpass crossing the road beneath at right angles is exactly this: **skew** (different heights, they never meet) yet **perpendicular**. Whether two lines cross at $90°$ or merely pass over each other at $90°$ is a fact about their *anchor points*; the dot product is blind to it. ([[Planes in 3D]] finishes the story: for the skew-line distance formula, perpendicular directions are the *friendliest* case of all — it's **parallel**, not perpendicular, that breaks the machinery.)

### Equivalence — the load-bearing identity

The two formulas give the *same* number. The proof uses the **law of cosines** applied to the triangle with sides $\mathbf{a}, \mathbf{b}, \mathbf{a} - \mathbf{b}$:

$$|\mathbf{a} - \mathbf{b}|^2 = |\mathbf{a}|^2 + |\mathbf{b}|^2 - 2|\mathbf{a}||\mathbf{b}|\cos\theta.$$

Expanding the left side via the component formula:

$$|\mathbf{a} - \mathbf{b}|^2 = (a_1 - b_1)^2 + (a_2 - b_2)^2 + (a_3 - b_3)^2 = |\mathbf{a}|^2 - 2(a_1 b_1 + a_2 b_2 + a_3 b_3) + |\mathbf{b}|^2.$$

Equating the two expressions and cancelling the $|\mathbf{a}|^2 + |\mathbf{b}|^2$ pieces:

$$-2(a_1 b_1 + a_2 b_2 + a_3 b_3) = -2|\mathbf{a}||\mathbf{b}|\cos\theta$$
$$\Rightarrow a_1 b_1 + a_2 b_2 + a_3 b_3 = |\mathbf{a}||\mathbf{b}|\cos\theta. \quad \square$$

**The two formulas are the same algebraic statement.** Compute the dot product via the component formula; use it via the geometric formula. That's the whole point.

> [!info] The dot product is the law of cosines in disguise
> Read the derivation again: the dot product *is* the law of cosines, rearranged. Every 2D-trigonometric fact you knew about the law of cosines lifts to 3D via the dot product. That's why the dot product is everywhere — it's the natural multidimensional generalisation of the simplest non-trivial trigonometric identity.

### Properties

For all vectors $\mathbf{a}, \mathbf{b}, \mathbf{c}$ and scalar $\lambda$:

| Property | Statement |
|---|---|
| **Commutative** | $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$ |
| **Distributive** | $\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}$ |
| **Scalar-compatible** | $(\lambda\mathbf{a}) \cdot \mathbf{b} = \lambda(\mathbf{a} \cdot \mathbf{b})$ |
| **Self-product** | $\mathbf{a} \cdot \mathbf{a} = \|\mathbf{a}\|^2$ |
| **Basis** | $\mathbf{i}\cdot\mathbf{i} = \mathbf{j}\cdot\mathbf{j} = \mathbf{k}\cdot\mathbf{k} = 1$; $\mathbf{i}\cdot\mathbf{j} = \mathbf{j}\cdot\mathbf{k} = \mathbf{k}\cdot\mathbf{i} = 0$ |

All proofs are one-line from the component formula. The basis-vector identities make $\mathbf{i}, \mathbf{j}, \mathbf{k}$ an **orthonormal basis** — unit-length, mutually perpendicular.

> [!warning] The scalar product is NOT ordinary multiplication
> $(\mathbf{a} \cdot \mathbf{b}) \cdot \mathbf{c}$ doesn't make sense — the left side is a scalar, you can't dot it with a vector. There's no "associative" property for dot products of three or more vectors because the operation doesn't even type-check that way. Always think: *dot product takes two vectors and returns a scalar*. After one dot product, you've left vector-land and entered scalar-land.

---

## §3 Three Headline Applications

### 1. Perpendicularity test

$$\mathbf{a} \perp \mathbf{b} \iff \mathbf{a} \cdot \mathbf{b} = 0$$

(assuming both vectors are non-zero — the zero vector is technically perpendicular to *everything* by convention but the implication direction requires non-zero).

**Worked example.** Are $\mathbf{a} = (2, 1, -1)$ and $\mathbf{b} = (1, -1, 1)$ perpendicular?
$\mathbf{a} \cdot \mathbf{b} = 2 \cdot 1 + 1 \cdot (-1) + (-1)(1) = 2 - 1 - 1 = 0$. **Yes.** ✓

### 2. Angle between vectors

Rearrange the geometric formula:

$$\boxed{\;\cos\theta = \dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}\;}$$

Then $\theta = \arccos\!\left(\dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}\right)$. This is the **canonical formula** for the angle between two vectors in 3D. Every 9709 P3 §3.7 question about angles uses it.

**Worked example.** Find the angle between $\mathbf{a} = (1, 2, 2)$ and $\mathbf{b} = (3, 0, 4)$.

- $\mathbf{a} \cdot \mathbf{b} = 1 \cdot 3 + 2 \cdot 0 + 2 \cdot 4 = 3 + 0 + 8 = 11$.
- $|\mathbf{a}| = \sqrt{1 + 4 + 4} = 3$.
- $|\mathbf{b}| = \sqrt{9 + 0 + 16} = 5$.
- $\cos\theta = \dfrac{11}{15}$, so $\theta = \arccos(11/15) \approx 42.8°$ (or $0.747$ rad).

### 3. Resolved part (vector projection)

The **resolved part of $\mathbf{a}$ in the direction of $\mathbf{b}$** is the scalar

$$\text{proj}_{\mathbf{b}} \mathbf{a} = \dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|}.$$

(Sometimes called the *component of $\mathbf{a}$ along $\mathbf{b}$*, or *signed length of the shadow of $\mathbf{a}$ on $\mathbf{b}$*.) Geometrically: drop a perpendicular from the head of $\mathbf{a}$ onto the line through $\mathbf{b}$. The foot of that perpendicular, measured as a *signed* distance along $\mathbf{b}$, is the resolved part.

In physics, $\mathbf{F} \cdot \mathbf{d}$ is the **work done** by force $\mathbf{F}$ moving along displacement $\mathbf{d}$ — it's literally the resolved part of force in the direction of motion, times the distance. The "$\cos\theta$" factor is why work depends on the *angle* between force and motion, not just their magnitudes. (See [[Work, Energy and Power]] for the physics.)

---

## §4 Common Misconceptions

### 1. Treating the dot product as ordinary multiplication

Writing $\mathbf{a} \cdot \mathbf{b} \cdot \mathbf{c}$ as if it were associative — but the inner $\mathbf{a} \cdot \mathbf{b}$ produces a scalar, and you can't dot a scalar with a vector.

**Fix.** Type-check: *dot product eats two vectors, outputs a scalar*. After one dot product, you've left vector-land. If you see $(\mathbf{a} \cdot \mathbf{b}) \cdot \mathbf{c}$ in your working, recognise it as nonsense and back up.

### 2. Sign confusion when extracting the angle

Computing $\mathbf{a} \cdot \mathbf{b} = -8$ and concluding "$\theta = \arccos(-8 / \ldots)$ which is greater than $90°$." Sometimes students panic at the negative and absolute-value it. *Don't.* The negative is real and meaningful — it tells you the angle is obtuse.

**Fix.** $\arccos$ returns a value in $[0, \pi]$, automatically handling positive and negative inputs. Trust the calculator's output. If you get $\theta > 90°$, that means the vectors point in opposing-ish directions — which is the actual geometric fact.

### 3. Zero dot product vs zero vector

Computing $\mathbf{a} \cdot \mathbf{b} = 0$ and concluding "one of the vectors must be zero." Not true — two perpendicular non-zero vectors give zero dot product.

**Fix.** $\mathbf{a} \cdot \mathbf{b} = 0$ has *three* possible causes: $\mathbf{a} = \mathbf{0}$, $\mathbf{b} = \mathbf{0}$, or $\mathbf{a} \perp \mathbf{b}$. *Check the vectors are non-zero first* before concluding perpendicularity.

### 4. Wrong cosine formula direction

Writing $\cos\theta = \mathbf{a} \cdot \mathbf{b}$ (forgetting to divide by the magnitudes), or $\cos\theta = \dfrac{|\mathbf{a}||\mathbf{b}|}{\mathbf{a} \cdot \mathbf{b}}$ (inverting).

**Fix.** Memorise the *direction* of the formula: dot product divided by *product of magnitudes*. Both sides should be dimensionless when the vectors carry units. The dot product carries units of (length)², the magnitudes each carry units of length — so the ratio is dimensionless, matching $\cos\theta \in [-1, 1]$.

### 5. Forgetting the sign of the resolved part

The resolved part of $\mathbf{a}$ in the direction of $\mathbf{b}$ can be *negative* if $\mathbf{a}$ points the "wrong way" along $\mathbf{b}$'s direction. Students sometimes report only the magnitude, losing the sign.

**Fix.** Resolved part is a *signed* scalar. Report the actual value of $\dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|}$ including sign.

---

## §5 Exam Notes

### Cambridge 9709 (A-Level)

**Syllabus refs:** Paper 3 §3.7 — vectors in 3D, scalar product, angle between vectors. Also lays the groundwork for vector equations of lines (covered in [[Vector Equations of Lines]]).

**Typical question shape:**
- *Find the angle between vectors $\mathbf{a}$ and $\mathbf{b}$.* (3–4 marks: dot product, magnitudes, arccos)
- *Show that vectors $\mathbf{a}$ and $\mathbf{b}$ are perpendicular.* (1–2 marks: compute dot product, show $= 0$)
- *Find a unit vector perpendicular to $\mathbf{a}$ that lies in the $xy$-plane.* (3 marks: setup + solve linear system)

**Tip.** When asked for an *angle*, give the value in the standard $[0°, 180°]$ range (or radians $[0, \pi]$). Don't second-guess the sign — let $\arccos$ handle it.

### Cambridge 9231 Further Pure 1

The scalar product is assumed knowledge and worked hard in FP1 §1.6: every angle (line–line, line–plane, plane–plane) and every distance formula there is a projection — $\mathbf{r}\cdot\hat{\mathbf{n}}$ doing the measuring. [[Cross Product]] joins it at that level, and [[Planes in 3D]] is where the two operate together.

### A-Level (Edexcel / AQA / OCR / MEI)

All A-Level boards include 3D vectors and the scalar product in A2 Pure. Same content as 9709 P3 §3.7. OCR's MEI Further Pure adds the **cross product** (vector product) $\mathbf{a} \times \mathbf{b}$ — a vector output perpendicular to both inputs, with magnitude $|\mathbf{a}||\mathbf{b}|\sin\theta$. Cross product is not on 9709 P3 (it appears at 9231 Further Pure level).

### IB AA HL

**Topic 3 (Geometry and Trigonometry).** Includes scalar product, vector equation of a line, **and** planes — equations of planes via point-normal form $\mathbf{n} \cdot (\mathbf{r} - \mathbf{a}) = 0$, intersection of plane and line, intersection of two planes (giving a line); [[Planes in 3D]] holds that whole toolkit. The IB AA HL formula booklet gives the scalar product formula and the standard line equation but expects you to derive plane intersections.

**AA SL** does not cover 3D vectors — entire topic is HL-only.

### AP Calculus

**Vectors are NOT on AP Calculus AB or BC.** Vectors appear in AP Physics (Mechanics + E&M) and in university-level Multivariable Calculus. AP students preparing for university STEM should learn vectors anyway — they're prerequisite for nearly every quantitative undergrad subject.

### Beyond high school — University

Vectors and dot products are the entry point to:

- **Linear algebra** — the dot product generalises to an **inner product** on abstract vector spaces. The inner product structure is what defines "angles" and "perpendicularity" in any vector space.
- **Calculus of vector fields** — gradient $\nabla f$, divergence $\nabla \cdot \mathbf{F}$, curl $\nabla \times \mathbf{F}$. All built on dot/cross products.
- **Differential geometry** — manifolds, metrics, tangent spaces. The inner product on each tangent space defines lengths and angles on curved spaces (the foundation of general relativity).
- **Quantum mechanics** — inner products of complex vectors, $\langle \psi | \phi \rangle$. The dot product generalises to **Hermitian inner product** with complex conjugation.
- **Machine learning** — every "similarity" measure between two pieces of data (cosine similarity in NLP embeddings, kernel methods in SVMs) is a dot product on a high-dimensional vector representation.

---

## Connections

- **Direct prerequisite:** [[Vectors]] — the 2D foundation. This card extends to 3D with the same algebra, plus introduces the dot product.
- **Direct prerequisite:** [[Trigonometric Ratios]] — for $\cos\theta$ and $\arccos$.
- **Direct prerequisite:** [[Pythagoras Theorem]] — for the 3D magnitude formula (Pythagoras twice).
- **Direct prerequisite:** [[Magnitude of a Vector (Vocab)]] — the vocab card on what magnitude means.
- **Sibling / next:** [[Vector Equations of Lines]] — Card B of the §3.7 pair. Uses the dot product extensively for the angle between two lines, perpendicular-from-point-to-line, and the intersection-vs-skew classification.
- **Application:** [[Work, Energy and Power]] — work is $\mathbf{F} \cdot \mathbf{d}$, the canonical physics use of the dot product.
- **Application — physics:** Lighting in 3D graphics — surface brightness via $\mathbf{n} \cdot \mathbf{L}$ between surface normal and light direction.
- **Sibling / companion:** [[Cross Product]] — the vector-valued partner to the dot product, with magnitude $|\mathbf{a}||\mathbf{b}|\sin\theta$ and direction perpendicular to both inputs (right-hand rule). The *sine half* of vector multiplication to this card's *cosine half*. 9231 FP1 / IB AA HL territory.
- **Closes:** Half of 9709 P3 §3.7. The remaining half (vector equations of lines, intersection/parallel/skew, angle between lines) is in [[Vector Equations of Lines]].
- **For 9709 students:** [[MF19 Reference (9709)]] — the dot product component formula and the $\cos\theta$ formula are both on the MF19 sheet. The vector equation of a line is also on the sheet.

---

## Beyond Syllabus

### Where the dot product came from

The *geometry* of the dot product is ancient — projecting one length onto another, and the law of cosines (which this card showed the dot product secretly *is*), go back to Euclid. But the dot product as a *named operation on vectors* is surprisingly young, and it has the same birth certificate as the cross product. When William Rowan Hamilton multiplied two pure **quaternions** in 1843, the answer split into a scalar part and a vector part: $\mathbf{p}\mathbf{q} = -\,\mathbf{p}\cdot\mathbf{q} + \mathbf{p}\times\mathbf{q}$. **The dot product is (minus) the scalar half of a quaternion product; the cross product is the vector half.** Neither came first — they were born together. In the 1880s Gibbs and Heaviside split that single quaternion operation into the two standalone products we now teach (Grassmann's 1844 exterior algebra was the parallel root), because the split form was far easier for physics — Heaviside used it to reduce Maxwell's twenty equations to four. So the "$\cos\theta$ half" and the "$\sin\theta$ half" of vector multiplication are two pieces of one 1843 idea. See [[Cross Product]] for the full split and [[Stories/The Argument for i]] §Act IV for the human story.

### The cross product — vector-valued companion

> [!info] Now its own card — [[Cross Product]]
> The full treatment (component/determinant formula, the perpendicularity and Lagrange-identity proofs, anticommutativity, the scalar triple product, worked examples, the quaternion origin story) lives in [[Cross Product]]. The summary below is the appetiser.

The **cross product** $\mathbf{a} \times \mathbf{b}$ takes two 3D vectors and produces a *new vector* perpendicular to both, with magnitude $|\mathbf{a}||\mathbf{b}|\sin\theta$ (note $\sin$, not $\cos$). Direction is given by the **right-hand rule**: curl right-hand fingers from $\mathbf{a}$ toward $\mathbf{b}$; thumb points in the direction of $\mathbf{a} \times \mathbf{b}$.

In components:

$$\mathbf{a} \times \mathbf{b} = (a_2 b_3 - a_3 b_2)\mathbf{i} - (a_1 b_3 - a_3 b_1)\mathbf{j} + (a_1 b_2 - a_2 b_1)\mathbf{k}.$$

Useful in physics (torque $\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$, angular momentum $\mathbf{L} = \mathbf{r} \times \mathbf{p}$, magnetic force $\mathbf{F} = q\mathbf{v} \times \mathbf{B}$) and computer graphics (surface normals from two edge vectors). 9231 Further Pure level / IB HL.

The dot and cross products are the two **fundamental products** on $\mathbb{R}^3$. They appear together in identities like

$$|\mathbf{a} \times \mathbf{b}|^2 + (\mathbf{a} \cdot \mathbf{b})^2 = |\mathbf{a}|^2|\mathbf{b}|^2$$

(this is $\sin^2\theta + \cos^2\theta = 1$ in disguise, multiplied through by $|\mathbf{a}|^2|\mathbf{b}|^2$). Beautiful identity worth knowing.

### Why "scalar" and "inner"?

"**Scalar product**" because the output is a scalar (number), not a vector. "**Inner product**" comes from the more abstract setting where you can also have an "*outer product*" $\mathbf{a} \otimes \mathbf{b}$ that produces a matrix (the rank-1 matrix $\mathbf{a}\mathbf{b}^T$). The naming distinguishes the two types of multiplicative operation. Standard linear-algebra naming.

The notation $\mathbf{a} \cdot \mathbf{b}$ is the most common; $\langle \mathbf{a}, \mathbf{b} \rangle$ is the abstract / pure-math notation; $\mathbf{a}^T \mathbf{b}$ is the matrix-style notation (column vector times row vector gives a $1 \times 1$ matrix, which we identify with a scalar).

### Cauchy-Schwarz inequality

From $\cos\theta \in [-1, 1]$:

$$|\mathbf{a} \cdot \mathbf{b}| \leq |\mathbf{a}|\,|\mathbf{b}|,$$

with equality iff $\mathbf{a}$ and $\mathbf{b}$ are parallel. This is the **Cauchy-Schwarz inequality** in $\mathbb{R}^3$. Generalises to abstract inner-product spaces, where it's one of the most-used results in analysis. The Cauchy-Schwarz inequality is essentially "the dot product can't be bigger than the product of magnitudes" — a deep statement once you generalise.

### Dot product in $\mathbb{R}^n$

The same component formula $\mathbf{a} \cdot \mathbf{b} = \sum a_i b_i$ works in any dimension. In $\mathbb{R}^n$ (where the "geometric angle" is harder to visualise), the formula *defines* the angle:

$$\cos\theta := \dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}.$$

This is the founding identity of $n$-dimensional geometry. Machine-learning embeddings live in $\mathbb{R}^{768}$ or $\mathbb{R}^{4096}$ (or higher), and the *only* meaningful notion of "similarity" between two embeddings is **cosine similarity** — exactly this formula. Search engines, recommendation systems, neural-network attention mechanisms (in GPT and others) all use cosine similarity.

So the 9709 P3 dot product is the entry point to a multi-trillion-dollar industry.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{v}$ | `\mathbf{v}` | Bold for vectors |
| $\mathbf{i}, \mathbf{j}, \mathbf{k}$ | `\mathbf{i}, \mathbf{j}, \mathbf{k}` | Standard basis in 3D |
| $\begin{pmatrix} a \\ b \\ c \end{pmatrix}$ | `\begin{pmatrix} a \\ b \\ c \end{pmatrix}` | Column vector |
| $\lvert \mathbf{v} \rvert$ | `\lvert \mathbf{v} \rvert` | Magnitude |
| $\hat{\mathbf{v}}$ | `\hat{\mathbf{v}}` | Unit vector |
| $\mathbf{a} \cdot \mathbf{b}$ | `\mathbf{a} \cdot \mathbf{b}` | Dot/scalar product |
| $\mathbf{a} \times \mathbf{b}$ | `\mathbf{a} \times \mathbf{b}` | Cross product (beyond syllabus) |
| $\arccos$ | `\arccos` | Inverse cosine for angle extraction |
| $\theta$ | `\theta` | Conventional name for angle between vectors |
| $\langle \mathbf{a}, \mathbf{b}\rangle$ | `\langle \mathbf{a}, \mathbf{b}\rangle` | Inner-product notation (beyond syllabus) |
