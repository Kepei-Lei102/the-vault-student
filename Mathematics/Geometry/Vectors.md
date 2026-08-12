---
chinese: 向量 (xiàngliàng)
prerequisites:
  - "[[Pythagoras Theorem]]"
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Triangles (Vocab)]]"
  - "[[Similarity]]"
leads_to:
  - "[[Vector Geometry]]"
  - "[[3D Vectors]]"
  - "[[Cross Product]]"
  - "[[Matrix]]"
  - "[[Matrix Transformations]]"
  - "[[Equilibrium]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Complex Numbers]]"
  - "[[Vectors in Physics]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE-extension
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - curriculum/IB-AI
  - syllabus/9260-G22
  - syllabus/0580-E7-2
  - syllabus/0606-13-1
  - syllabus/0606-13-3
  - syllabus/9709-3-7
  - syllabus/9702-1-4
  - type/definition
  - type/theorem
  - type/proof
  - notation/column-vector
  - notation/bold-vector
  - notation/arrow-vector
  - notation/i-j
  - misconception/vector-vs-scalar
  - misconception/vector-equals-points
  - misconception/magnitude-is-signed
  - misconception/direction-of-minus-v
---

# Vectors 向量

## Definition

### Formal

A **vector** is a mathematical object with two pieces of information:

1. **Magnitude** — a non-negative real number (its length or size)
2. **Direction** — an orientation in space

Two vectors are **equal** when they have the same magnitude AND the same direction. Position does not matter — a vector can be slid freely without changing its identity.

A **scalar** is an ordinary number (just magnitude, no direction).

### Intuitive — An Arrow With Amnesia

Think of a vector as an arrow that has forgotten where it started. All that survives is "how long" and "which way." You can pick the arrow up, move it anywhere on the page, and as long as you don't rotate or stretch it, it's still the same vector.

This is why two parallel arrows of the same length, drawn in different places, represent the **same vector**. The arrow's starting point is just a visual handle — the mathematics lives in the displacement from start to end.

Contrast this with a **point**, which is a location, and a **scalar**, which is a bare number. A vector is a structured thing: number + arrow.

### 中文锚点 (Chinese Anchor)

向量：**既有大小又有方向的量。**

| 中文 | English | Notes |
|------|---------|-------|
| 向量 | vector | Also 矢量 (shǐliàng) in physics contexts |
| 标量 | scalar | 纯粹的数，没有方向 |
| 大小 / 模 | magnitude / modulus | Physicists say 大小; mathematicians write $\lvert \vec{a} \rvert$ and call it 模 |
| 方向 | direction | |
| 起点 / 终点 | start / end (initial / terminal point) | Start of the arrow / end of the arrow |
| 零向量 | zero vector | $\vec{0}$, magnitude 0, no defined direction |
| 单位向量 | unit vector | Magnitude 1, written $\hat{a}$ |
| 位置向量 | position vector | Start pinned at origin — covered in [[Vector Geometry]] |
| 共线 | collinear | Three points on one line — covered in [[Vector Geometry]] |

Chinese physics introduces 矢量 before English maths introduces vectors, so the student already has the *idea*. What they need is the English vocabulary and the unified Cambridge / A-Level notation.

## Notation

Vectors are written four different ways — the student must read all four and choose one to write.

| Convention | Example | Where it's used | Read as |
|------------|---------|-----------------|---------|
| **Bold letter** | $\mathbf{a}$, $\mathbf{v}$ | Printed textbooks, exam papers | "vector a" |
| **Arrow above** | $\vec{a}$, $\vec{AB}$ | Handwriting (can't bold a letter in pen) | "vector a" / "vector from A to B" |
| **Column vector** | $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$ | Calculation, Cambridge 0580/9260 default | "three, minus two" |
| **i–j notation** | $3\mathbf{i} - 2\mathbf{j}$ | 0606, A-Level, Physics | "three i minus two j" |

The column vector $\begin{pmatrix} x \\ y \end{pmatrix}$ and the i–j form $x\mathbf{i} + y\mathbf{j}$ encode the same information. $\mathbf{i}$ is the unit vector along the $x$-axis and $\mathbf{j}$ is the unit vector along the $y$-axis.

$$\begin{pmatrix} 3 \\ -2 \end{pmatrix} = 3\mathbf{i} - 2\mathbf{j}$$

The **magnitude** of $\mathbf{a}$ is written $\lvert \mathbf{a} \rvert$ or $\lvert \vec{a} \rvert$ — absolute-value bars. An unbolded $a$ with no bars usually means a scalar.

For a directed line segment from point $A$ to point $B$:

$$\vec{AB} = \text{displacement from } A \text{ to } B$$

and the **reverse** is the negative:

$$\vec{BA} = -\vec{AB}$$

> [!warning] Notation Trap
> **9260 does not require i–j notation.** The syllabus explicitly says *"use of $\mathbf{i}$ and $\mathbf{j}$ notation is not required."* But Cambridge 0606 and all A-Level/IB work use i–j fluently. This card teaches both because any 9260 student who continues to A-Level will need i–j by Year 12. For the May 2026 exam: column vectors suffice.

> [!warning] Notation Trap
> $\vec{AB}$ is a **vector** (an arrow, a displacement). $AB$ with no arrow is a **length** (a scalar). Writing $\vec{AB} = 5$ is wrong — the left side is a vector, the right side is a number. Write $\lvert \vec{AB} \rvert = 5$ instead.

## Key Facts / Properties

### 1. Addition — Triangle Law (start-to-end chain)

To add two vectors $\mathbf{a}$ and $\mathbf{b}$, place the start of $\mathbf{b}$ at the end of $\mathbf{a}$. The sum $\mathbf{a} + \mathbf{b}$ is the vector from the start of $\mathbf{a}$ to the end of $\mathbf{b}$.

![[vectors-triangle-law.svg]]

In components:

$$\begin{pmatrix} a_1 \\ a_2 \end{pmatrix} + \begin{pmatrix} b_1 \\ b_2 \end{pmatrix} = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \end{pmatrix}$$

**Why chain them?** Think of vectors as journeys. $\mathbf{a}$ is "walk 3 east, 2 north." $\mathbf{b}$ is "walk 1 east, 4 north." Doing $\mathbf{a}$ then $\mathbf{b}$ leaves you at $(4, 6)$ from where you started — which is exactly $\mathbf{a} + \mathbf{b}$.

### 2. Addition — Parallelogram Law

If both vectors share the same starting point, complete the parallelogram. The diagonal from that shared starting point is $\mathbf{a} + \mathbf{b}$.

![[vectors-parallelogram-law.svg]]

The parallelogram law and the triangle law give the same answer — they are just two ways of drawing the same computation. Parallelogram is more symmetric (you can see both $\mathbf{a}+\mathbf{b}$ and $\mathbf{b}+\mathbf{a}$ in one picture), triangle is faster for chains of three or more vectors.

> [!info] Beyond syllabus — Why vector addition is commutative
> **Claim:** $\mathbf{a} + \mathbf{b} = \mathbf{b} + \mathbf{a}$
>
> **Proof (geometric):** Draw $\mathbf{a}$ from $O$ to $P$, then $\mathbf{b}$ from $P$ to $Q$. Now draw $\mathbf{b}$ from $O$ to $R$, then $\mathbf{a}$ from $R$ to $Q'$. Because $OP$ and $RQ'$ are copies of $\mathbf{a}$ (same length and direction) and $PQ$ and $OR$ are copies of $\mathbf{b}$, the figure $OPQR$ is a parallelogram, so $Q = Q'$. Both paths end at the same point, therefore the sums are equal. $\blacksquare$
>
> **Claim:** $(\mathbf{a} + \mathbf{b}) + \mathbf{c} = \mathbf{a} + (\mathbf{b} + \mathbf{c})$ (associativity).
>
> **Proof:** Both sides describe the journey $O \to P \to Q \to R$ where $\vec{OP} = \mathbf{a}$, $\vec{PQ} = \mathbf{b}$, $\vec{QR} = \mathbf{c}$. The bracketing just says "pause here" — the endpoint is the same. $\blacksquare$

### 3. Subtraction — "Go Back Along b"

$$\mathbf{a} - \mathbf{b} = \mathbf{a} + (-\mathbf{b})$$

To compute $\mathbf{a} - \mathbf{b}$, flip $\mathbf{b}$ (same length, opposite direction) and add.

Equivalently, if $\mathbf{a}$ and $\mathbf{b}$ share the same starting point, then $\mathbf{a} - \mathbf{b}$ is the vector **from the end of $\mathbf{b}$ to the end of $\mathbf{a}$**:

![[vectors-subtraction.svg]]

This is the single most useful picture in vector geometry. Memorise it: **subtraction points from the end of the second vector to the end of the first.**

In components:

$$\begin{pmatrix} a_1 \\ a_2 \end{pmatrix} - \begin{pmatrix} b_1 \\ b_2 \end{pmatrix} = \begin{pmatrix} a_1 - b_1 \\ a_2 - b_2 \end{pmatrix}$$

### 4. Scalar Multiplication

Multiplying a vector by a positive scalar $k$ stretches or shrinks it by factor $k$ **without changing direction**. A negative scalar additionally reverses the direction.

![[vectors-scalar-multiplication.svg]]

In components:

$$k \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} = \begin{pmatrix} k a_1 \\ k a_2 \end{pmatrix}$$

Key magnitude identity:

$$\lvert k\mathbf{a} \rvert = \lvert k \rvert \cdot \lvert \mathbf{a} \rvert$$

The $\lvert k \rvert$ is necessary because magnitude is non-negative, but $k$ might be negative.

### 5. Magnitude — Pythagoras in Disguise

If $\mathbf{a} = \begin{pmatrix} x \\ y \end{pmatrix}$, then

$$\boxed{\lvert \mathbf{a} \rvert = \sqrt{x^2 + y^2}}$$

**Why?** Draw the vector from the origin to the point $(x, y)$. It is the hypotenuse of a right triangle with legs $x$ (horizontal) and $y$ (vertical). [[Pythagoras Theorem]] gives the length directly. Magnitude of a vector is **literally Pythagoras's theorem with new clothes**.

In 3D (0606, A-Level extension):

$$\lvert \mathbf{a} \rvert = \sqrt{x^2 + y^2 + z^2}$$

### 6. Unit Vectors

A **unit vector** $\hat{\mathbf{a}}$ is a vector of magnitude 1 pointing in the same direction as $\mathbf{a}$:

$$\hat{\mathbf{a}} = \frac{\mathbf{a}}{\lvert \mathbf{a} \rvert}$$

The unit vector captures the **direction only**. Any vector can be decomposed into magnitude × direction:

$$\mathbf{a} = \lvert \mathbf{a} \rvert \cdot \hat{\mathbf{a}}$$

The standard unit vectors $\mathbf{i} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $\mathbf{j} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ (and $\mathbf{k} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$ in 3D) are the building blocks of every vector on the plane.

> [!info] Beyond 0606 (in scope for 9709 P3 / A-Level / IB / AP) — The cosine rule is a dot product identity
> The [[Sine and Cosine Rules|cosine rule]] $c^2 = a^2 + b^2 - 2ab\cos C$ is really a statement about vectors. If $\mathbf{a}$ and $\mathbf{b}$ are two sides of a triangle emanating from the same starting point with angle $C$ between them, and $\mathbf{c} = \mathbf{b} - \mathbf{a}$ is the third side:
>
> $$\lvert \mathbf{c} \rvert^2 = \lvert \mathbf{b} - \mathbf{a} \rvert^2 = \lvert \mathbf{b} \rvert^2 - 2\mathbf{a}\cdot\mathbf{b} + \lvert \mathbf{a} \rvert^2 = a^2 + b^2 - 2ab\cos C$$
>
> where $\mathbf{a} \cdot \mathbf{b} = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \cos C$ is the **dot product** (also called **scalar product**, in scope for 9709 P3 §3.7 / A-Level / IB). One algebraic expansion of a magnitude gives the entire law of cosines. This is the A-Level bridge waiting on the other side of Vectors.

## Where Vectors Apply — Physics and Beyond

### The vector / scalar divide

Almost every quantity the student meets in physics is either a vector or a scalar, and the notation you learn here is exactly the notation physics uses.

| Vector quantities (magnitude + direction) | Scalar quantities (magnitude only) |
|---|---|
| Displacement $\mathbf{s}$ | Distance $d$ |
| Velocity $\mathbf{v}$ | Speed $\lvert \mathbf{v} \rvert$ |
| Acceleration $\mathbf{a}$ | Time $t$ |
| Force $\mathbf{F}$ | Mass $m$ |
| Momentum $\mathbf{p} = m\mathbf{v}$ | Energy $E$ |
| Electric field $\mathbf{E}$, magnetic field $\mathbf{B}$ | Temperature $T$ |
| Angular velocity $\boldsymbol{\omega}$ | Charge $q$ |

The **bold/arrow vs. italic** convention in physics is exactly the maths convention — Newton's second law is $\mathbf{F} = m\mathbf{a}$ (both sides are vectors, $m$ is a scalar). A textbook writing $F = ma$ without bolding is either implicitly 1D or sloppy.

### Velocity composition (Cambridge 0606 13.4)

A boat steers at 5 m/s due north across a river whose current flows east at 3 m/s. The boat's velocity relative to the ground is

$$\mathbf{v}_{\text{ground}} = \mathbf{v}_{\text{boat}} + \mathbf{v}_{\text{current}} = \begin{pmatrix} 3 \\ 5 \end{pmatrix}$$

with speed $\sqrt{3^2 + 5^2} = \sqrt{34} \approx 5.83$ m/s and bearing $\tan^{-1}(3/5) \approx 031°$ from north. This is a direct Cambridge 0606 13.4 question — and simultaneously a GCSE/A-Level physics question. **Same vector addition, two exam papers.**

> [!tip] Deeper physics applications
> [[Equilibrium]] ($\sum \mathbf{F} = \mathbf{0}$ — 力的平衡, the single most important vector application in mechanics), resolving forces into $\mathbf{i}$/$\mathbf{j}$ components, relative velocity, projectiles — these are all vector problems dressed in physics language. They belong in a dedicated physics folder when the vault grows that way. For now, remember: **every time you see a force, velocity, or field in physics, it IS a vector, and the operations on this card are the operations you use.**

### Why this section matters for the student

A Chinese student who has taken Chinese physics already knows all of this intuitively using 矢量. The vault's job is to tell them: *the 矢量 in 物理 IS the vector in 数学. Notation is unified. The maths of the physics IS the maths.* Once this translation clicks, most vector problems feel like physics problems they have already solved.

## Why Vectors Matter — College and Beyond

Vectors are a **hinge topic**. Every student who continues mathematics, science, engineering, computer science, or economics will run into them over and over for the rest of their life. A partial, very incomplete list of what the next few years open up:

- **Linear algebra** — the subject that begins the moment a column vector gains a second column and becomes a [[Matrix|matrix]]. Linear algebra is *the* language of 20th-21st century mathematics. Solving systems of equations, transforming shapes, fitting lines to data — all become matrix-times-vector.
- **Computer graphics** — every pixel on screen in a 3D game or animated film is a vector transformed by a matrix. Rotations, perspective, lighting — all vectors.
- **Machine learning and AI** — a sentence becomes a vector (embedding), an image becomes a vector of pixel values, a neural network is a long chain of matrix-vector multiplications. "Similarity" between two pieces of data is the angle between their vectors (dot product). ChatGPT is, mechanically, vectors times matrices times vectors, trillions of times.
- **Physics and engineering** — forces on bridges, currents in circuits, fluid flow, quantum states — all vectors or vector fields. Chinese 高考 physics already uses vectors; university physics adds vector calculus (gradient, divergence, curl).
- **Economics and data science** — a country's economy in a given year is a vector of indicators (GDP, inflation, unemployment, ...); data science works with millions of such vectors at once.
- **Robotics** — a robot's state is a vector (position, orientation, joint angles); controlling it is linear algebra.
- **Navigation and GPS** — the phone in your pocket computes your position using vectors from four or more satellites.

In short: everything that an engineer, scientist, economist, or programmer does in the real world eventually reduces to vectors and their generalisation — matrices. **This card is the doorway.** The next card, [[Vector Geometry]], walks through it; after that, [[Matrix]] and [[Matrix Transformations]] go further.

## Special Cases

### Zero vector $\mathbf{0}$

$\mathbf{0} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ has magnitude 0 and **no defined direction**. Arithmetic works as expected: $\mathbf{a} + \mathbf{0} = \mathbf{a}$, $0 \cdot \mathbf{a} = \mathbf{0}$.

### Equal and opposite vectors

$\mathbf{a}$ and $-\mathbf{a}$ have the same magnitude but opposite directions. In component form, negate every entry.

### Equal vectors in different locations

$\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ drawn from $(0,0)$ to $(2,3)$ is the **same vector** as $\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ drawn from $(1,1)$ to $(3,4)$. The starting point does not matter; only the displacement does.

## Worked Examples

### Example 1 (9260 level): Basic arithmetic with column vectors

Given $\mathbf{a} = \begin{pmatrix} 4 \\ -1 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} -2 \\ 3 \end{pmatrix}$, compute $2\mathbf{a} - 3\mathbf{b}$ and its magnitude.

**Solution.**

$$2\mathbf{a} = \begin{pmatrix} 8 \\ -2 \end{pmatrix}, \qquad 3\mathbf{b} = \begin{pmatrix} -6 \\ 9 \end{pmatrix}$$

$$2\mathbf{a} - 3\mathbf{b} = \begin{pmatrix} 8 - (-6) \\ -2 - 9 \end{pmatrix} = \begin{pmatrix} 14 \\ -11 \end{pmatrix}$$

Magnitude:
$$\lvert 2\mathbf{a} - 3\mathbf{b} \rvert = \sqrt{14^2 + (-11)^2} = \sqrt{196 + 121} = \sqrt{317} \approx 17.8$$

### Example 2 (0606 level): i–j components and unit vector

Given $\mathbf{a} = 3\mathbf{i} + 4\mathbf{j}$ and $\mathbf{b} = -\mathbf{i} + 2\mathbf{j}$:

(i) Find $\mathbf{a} - 2\mathbf{b}$ in component form.

(ii) Find the magnitude $\lvert \mathbf{a} \rvert$.

(iii) Find the unit vector in the direction of $\mathbf{a}$.

**Solution.**

(i) $2\mathbf{b} = -2\mathbf{i} + 4\mathbf{j}$, so
$$\mathbf{a} - 2\mathbf{b} = (3 - (-2))\mathbf{i} + (4 - 4)\mathbf{j} = 5\mathbf{i}$$

(ii) $\lvert \mathbf{a} \rvert = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$.

(iii) $\hat{\mathbf{a}} = \dfrac{\mathbf{a}}{\lvert \mathbf{a} \rvert} = \tfrac{1}{5}(3\mathbf{i} + 4\mathbf{j}) = \tfrac{3}{5}\mathbf{i} + \tfrac{4}{5}\mathbf{j}$.

Check: $\lvert \hat{\mathbf{a}} \rvert = \sqrt{(3/5)^2 + (4/5)^2} = \sqrt{9/25 + 16/25} = \sqrt{1} = 1$. ✓

## Common Misconceptions (Teaching Notes)

### 1. Treating a vector like a point

Students write $\mathbf{a} = (3, 2)$ and then ask "where is that on the axes?" as if $\mathbf{a}$ were a location.

**Fix:** Emphasise the arrow. Draw $\mathbf{a}$ as an arrow from *somewhere* — anywhere — of length $\sqrt{13}$, pointing up and to the right. Then draw the *same* $\mathbf{a}$ starting from a different point. Students need to see that a vector is the same object no matter where it is drawn, whereas a point is fixed. Position vectors (in [[Vector Geometry]]) ARE vectors — but vectors with a conventional starting point (the origin).

### 2. Forgetting that magnitude is non-negative

Students write $\lvert -\mathbf{a} \rvert = -\lvert \mathbf{a} \rvert$ or leave a negative inside a square root without the modulus.

**Fix:** Remind them magnitude is a length, and lengths can't be negative. $\lvert -\mathbf{a} \rvert = \lvert \mathbf{a} \rvert$ — the minus flips the direction but not the length. Same reasoning as $\lvert -5 \rvert = 5$ for numbers.

### 3. Adding magnitudes instead of vectors

$\lvert \mathbf{a} + \mathbf{b} \rvert \ne \lvert \mathbf{a} \rvert + \lvert \mathbf{b} \rvert$ in general (equality only when $\mathbf{a}$ and $\mathbf{b}$ are parallel and point the same way).

**Fix:** Make them draw it. $\mathbf{a} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$, $\mathbf{b} = \begin{pmatrix} 0 \\ 4 \end{pmatrix}$: magnitudes are 3 and 4, but $\mathbf{a} + \mathbf{b} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ has magnitude 5, not 7. This is the **triangle inequality**: $\lvert \mathbf{a} + \mathbf{b} \rvert \le \lvert \mathbf{a} \rvert + \lvert \mathbf{b} \rvert$.

### 4. Direction of $\vec{AB}$ vs $\vec{BA}$

Students confuse which way a displacement points.

**Fix:** The letters read like a journey. $\vec{AB}$ = start at $A$, end at $B$. $\vec{BA}$ = start at $B$, end at $A$. They are **negatives** of each other: $\vec{AB} = -\vec{BA}$.

### 5. Using $\vec{AB}$ as a length

Writing "$\vec{AB} = 5$" or "$\vec{AB} + \vec{BC} = 10$" — confusing a vector with its magnitude.

**Fix:** Train the bars. If you want the length, write $\lvert \vec{AB} \rvert = 5$. A vector never equals a number.

## Exam Notes

### Memorise? — per board (A-Level / IAL / 9660 / AP)

The four-board exam-strategy table for vectors at A-Level scope (basic vector arithmetic / dot product / 3D extensions). Same legend as [[Standard Integrals]]: ✅ given on booklet, 📝 must memorise, 🛠 derive, ⚪ off-syllabus. Sources: [[MF19 Reference (9709)]], [[Edexcel IAL Reference]], [[OxAQA 9660 Reference]], [[AP Calculus Reference]].

| Formula | 9709 | IAL | 9660 | AP |
|---|:---:|:---:|:---:|:---:|
| **Magnitude** $\lvert \mathbf{a} \rvert = \sqrt{a_1^2 + a_2^2 + a_3^2}$ | 📝 | 📝 | 📝 | 📝 |
| **Dot product (component)** $\mathbf{a}\cdot\mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3$ | ✅ | 📝 | ✅ (via "resolved part") | ⚪ off-syllabus AB; 📝 BC |
| **Dot product (geometric)** $\mathbf{a}\cdot\mathbf{b} = \lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\cos\theta$ | ✅ | 📝 | ✅ | ⚪ AB; 📝 BC |
| **Resolved part** of $\mathbf{a}$ in direction $\mathbf{b}$ = $\dfrac{\mathbf{a}\cdot\mathbf{b}}{\lvert\mathbf{b}\rvert}$ | 🛠 | 📝 | ✅ | ⚪ |
| **Vector equation of a line** $\mathbf{r} = \mathbf{a} + t\mathbf{d}$ | 📝 | 📝 | ✅ | 📝 BC |
| **Cartesian equation of a line** $\dfrac{x - a_1}{b_1} = \dfrac{y - a_2}{b_2} = \dfrac{z - a_3}{b_3}$ | 📝 | 📝 | ✅ | ⚪ |
| **Cross product** $\mathbf{a}\times\mathbf{b} = \lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\sin\theta\,\hat{\mathbf{n}}$ | ⚪ 9231 only | ⚪ FP3 only | ✅ | ⚪ |
| **Cross product (determinant)** | ⚪ 9231 only | ⚪ FP3 only | ✅ | ⚪ |
| **Plane equation** $\mathbf{n}\cdot\mathbf{r} = d$ (point + normal) | 🛠 from dot product | ⚪ FP3 | ✅ | ⚪ |
| **Plane through 3 points** $\mathbf{r} = (1-\lambda-\mu)\mathbf{a} + \lambda\mathbf{b} + \mu\mathbf{c}$ | 🛠 from dot product | ⚪ FP3 | ✅ | ⚪ |
| **Section formula** $\dfrac{\mu\mathbf{a} + \lambda\mathbf{b}}{\lambda + \mu}$ for AB ratio $\lambda:\mu$ | 📝 | 📝 | ✅ | ⚪ |
| **Triple scalar product** $\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})$ | ⚪ 9231 only | ⚪ FP3 only | ⚪ uni level | ⚪ |
| **2D rotation matrix** $\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$ | ⚪ 9231 only | ✅ FP1 | ✅ | ⚪ |
| **3D rotation matrices** about each axis | ⚪ 9231 only | ⚪ FP3 only | ✅ | ⚪ |

> [!info] OxAQA 9660 dominates the vectors table — by a wider margin than any other topic
> Look at the column counts: 9660 gives ✅ on **eleven** rows here. MF19 gives ✅ on **two** rows (dot product, geometric form). IAL gives only **one** ✅ at Pure level (dot product, both forms). AP gives **none**. *9660 is the only board where 3D vectors, cross product, plane equations, and 3D rotations live on standard Pure rather than Further Math territory.* This is the topic where the cross-board generosity asymmetry is most extreme.
>
> **Why this matters for cross-board students:** if you're studying for IAL or 9709 *and* might do an AP exam later, the vector content you'd need to memorise for AP is roughly the *Pure-only* content of IAL or 9709 — which is mostly just dot product. The 3D / cross product / plane content is where 9660 students get free what others derive on the day.
>
> **Magnitude of a vector** is universal memorisation — appearing on no booklet, but trivially derivable from the dot product (since $\mathbf{a}\cdot\mathbf{a} = \lvert\mathbf{a}\rvert^2$). The fact that the most basic formula isn't on any sheet is one of those small ironies.

---

### OxAQA 9260

Syllabus: **G22** (Core). The specification lists:

- Understand and use vector notation
- Calculate and represent graphically: $\mathbf{a} + \mathbf{b}$, $\mathbf{a} - \mathbf{b}$, $k\mathbf{a}$
- Understand and use commutative and associative properties of vector addition
- Solve simple geometrical problems in 2D using vector methods
- **Use of $\mathbf{i}$ and $\mathbf{j}$ notation is not required**

What's tested: column-vector arithmetic; representing vectors on a grid; short geometric arguments (covered in [[Vector Geometry]]). No dot product, no 3D.

### Cambridge 0580 Extended

Syllabus: **E7.2** (add/subtract/scalar) and **E7.3** (magnitude $\sqrt{x^2+y^2}$). The geometric applications in E7.4 are covered in [[Vector Geometry]].

Mark scheme pattern: column arithmetic gets 1 mark per correct component; magnitude gets 2 marks (1 for $\sqrt{x^2+y^2}$, 1 for the final number).

### Cambridge 0606

Syllabus: **13.1** (all four notations including $\mathbf{i}$–$\mathbf{j}$) and **13.3** (magnitude). Topic 13.2 (position/unit vectors applied) and 13.4 (velocity vectors) are in [[Vector Geometry]].

### A-Level

Vectors appear in **Mechanics** (kinematics, forces, equilibrium) and **Pure Mathematics** (coordinate geometry, scalar product, lines in 3D). The magnitude and unit-vector formulas carry over unchanged; 3D adds a $\mathbf{k}$ component. A-Level adds the **scalar (dot) product** — see the Beyond-syllabus callout above.

### IB AA / AI

**Topic 3 — Geometry and trigonometry** (both AA and AI). IB treats vectors more heavily than Cambridge: vector equations of lines, scalar product, angle between vectors. AA HL extends to 3D lines and planes.

## Connections

- **Parent:** [[Cartesian Coordinates (Vocab)]] — vectors live on the coordinate plane
- **Proof ingredient:** [[Pythagoras Theorem]] — magnitude $\sqrt{x^2+y^2}$ is literally the hypotenuse length
- **Proof ingredient:** [[Triangles (Vocab)]] — triangle law of addition is just "close the triangle"
- **Extensions:** [[Vector Geometry]] — position vectors, collinearity, ratio division, geometric proofs using vectors (the natural next card)
- **Extensions:** [[3D Vectors]] — adding the $\mathbf{k}$ component for 0606 / A-Level
- **Application:** [[Matrix]] — a $2 \times 1$ matrix IS a column vector; matrix algebra IS vector algebra extended
- **Application:** [[Matrix Transformations]] — matrices transform position vectors to new position vectors
- **Reverse / Component:** [[Similarity]] — similar triangles are built by scaling a single vector (scalar multiplication)
- **Bridge:** [[Sine and Cosine Rules]] — the cosine rule is the magnitude of $\mathbf{b} - \mathbf{a}$ expanded
- **Physics bridge:** velocity, force, momentum, fields — all vectors. Physics notation mirrors maths notation exactly.
- **Physics bridge — reserved:** [[Equilibrium]] — forces summing to zero ($\sum \mathbf{F} = \mathbf{0}$); the canonical application of vector addition in mechanics. Full card to be written when the physics folder is opened.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{a}$ | `\mathbf{a}` | Printed vector notation |
| $\vec{a}$ | `\vec{a}` | Handwritten vector notation |
| $\vec{AB}$ | `\vec{AB}` | Directed line segment from $A$ to $B$ |
| $\begin{pmatrix} x \\ y \end{pmatrix}$ | `\begin{pmatrix} x \\ y \end{pmatrix}` | Column vector |
| $\mathbf{i}, \mathbf{j}, \mathbf{k}$ | `\mathbf{i}` etc. | Standard unit vectors |
| $\hat{\mathbf{a}}$ | `\hat{\mathbf{a}}` | Unit vector in direction of $\mathbf{a}$ |
| $\lvert \mathbf{a} \rvert$ | `\lvert \mathbf{a} \rvert` | Magnitude (use `\lvert` / `\rvert` not `|` in tables) |
| $\mathbf{a} \cdot \mathbf{b}$ | `\mathbf{a} \cdot \mathbf{b}` | Dot product (A-Level) |
| $\parallel$ | `\parallel` | "is parallel to" |
| $\mathbf{0}$ | `\mathbf{0}` | Zero vector |
