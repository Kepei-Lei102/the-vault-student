---
chinese: 向量的模 (xiàngliàng de mó)
prerequisites:
  - "[[Vectors]]"
  - "[[Pythagoras Theorem]]"
  - "[[3D Trigonometry]]"
leads_to:
  - "[[Vector Geometry]]"
  - "[[Complex Numbers]]"
  - "[[Vectors in Physics]]"
  - "[[3D Vectors and the Scalar Product]]"
  - "[[Cross Product]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE-extension
  - level/A-Level
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/0580-E7-3
  - type/vocabulary
  - notation/vector-magnitude
---

# Magnitude of a Vector 向量的模

## Definition

The **magnitude** of a vector is its *length* — the size of the arrow without regard to direction. For a vector $\mathbf{a}$ written in component form $\begin{pmatrix} x \\ y \end{pmatrix}$, the magnitude is

$$\boxed{\;\lvert \mathbf{a} \rvert \;=\; \sqrt{x^2 + y^2}\;}$$

(the **2D** version). This is just **Pythagoras** applied to the right triangle whose legs are the components: $x$ horizontally and $y$ vertically.

For a 3D vector $\begin{pmatrix} x \\ y \\ z \end{pmatrix}$:

$$\lvert \mathbf{a} \rvert = \sqrt{x^2 + y^2 + z^2}.$$

The magnitude is *always non-negative*, and equals $0$ only for the zero vector $\mathbf{0}$.

### 中文锚点

**向量的模 (xiàngliàng de mó)** = **向量的长度** (length of a vector)。

公式 (2D)：

$$\lvert \mathbf{a} \rvert = \sqrt{x^2 + y^2}.$$

3D 版：$\lvert \mathbf{a} \rvert = \sqrt{x^2 + y^2 + z^2}$。

记号：$\lvert \mathbf{a} \rvert$ 或 $\| \mathbf{a} \|$。零向量的模为 $0$，其他向量的模都 $> 0$。

注意：模就是用**勾股定理 (gōugǔ dìnglǐ)** 求的斜边长度。$x$ 是水平分量，$y$ 是垂直分量，斜边即向量的模。

---

## Key Vocabulary

| English | 中文 | Notes |
|---|---|---|
| magnitude | 模 / 长度 | the length, $\lvert \mathbf{a} \rvert$ |
| component | 分量 (fēnliàng) | the $x$, $y$ (and $z$) numbers |
| unit vector | 单位向量 (dānwèi xiàngliàng) | a vector of magnitude $1$, $\hat{\mathbf{a}}$ |
| direction | 方向 (fāngxiàng) | the angle the vector makes; magnitude alone doesn't capture this |

---

## Worked Examples

### Example 1 — basic 2D magnitude

> Find the magnitude of $\mathbf{a} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$.

$\lvert \mathbf{a} \rvert = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.

### Example 2 — vector between two points

> Find the magnitude of $\overrightarrow{AB}$ where $A = (1, 2)$ and $B = (4, 6)$.

$\overrightarrow{AB} = B - A = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$.
$\lvert \overrightarrow{AB} \rvert = \sqrt{3^2 + 4^2} = 5$.

This is just the **distance formula** $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ in disguise — see [[Length and Midpoint (Vocab)]].

### Example 3 — 3D vector

> Find $\lvert \mathbf{v} \rvert$ where $\mathbf{v} = \begin{pmatrix} 2 \\ -3 \\ 6 \end{pmatrix}$.

$\lvert \mathbf{v} \rvert = \sqrt{2^2 + (-3)^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$.

> [!info] Why $(-3)^2 = 9$ in the formula
> The components are *squared* before adding. Squaring removes the sign, so a vector and its negative ($\mathbf{a}$ and $-\mathbf{a}$) have the *same* magnitude. This makes intuitive sense — flipping the direction of an arrow doesn't change its length.

---

## Unit Vectors

A **unit vector** is a vector of magnitude $1$. Given any non-zero vector $\mathbf{a}$, you can construct the *unit vector in the same direction* by dividing $\mathbf{a}$ by its own magnitude:

$$\hat{\mathbf{a}} = \frac{\mathbf{a}}{\lvert \mathbf{a} \rvert}.$$

Reading this: the hat ($\hat{}$) marks "unit vector"; dividing by the magnitude *normalises* the length to $1$ while preserving direction.

**Example.** For $\mathbf{a} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ with $\lvert \mathbf{a} \rvert = 5$:
$$\hat{\mathbf{a}} = \frac{1}{5}\begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} 0.6 \\ 0.8 \end{pmatrix}.$$
Check: $\sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = \sqrt{1} = 1$ ✓.

> [!info] Unit vectors are everywhere in physics
> A unit vector "points in a direction without committing to a length" — exactly what you want when describing forces, velocities, or fields. The standard basis vectors $\hat{\mathbf{i}}, \hat{\mathbf{j}}, \hat{\mathbf{k}}$ are the unit vectors along the $x$, $y$, $z$ axes. Any vector $\begin{pmatrix} x \\ y \\ z \end{pmatrix}$ can be written $x\hat{\mathbf{i}} + y\hat{\mathbf{j}} + z\hat{\mathbf{k}}$ — the components-as-coefficients form preferred in physics.

---

## Common Mistakes

1. **Forgetting to square negative components.** $\begin{pmatrix} -3 \\ 4 \end{pmatrix}$ has magnitude $\sqrt{(-3)^2 + 4^2} = \sqrt{25} = 5$, *not* $\sqrt{-9 + 16} = \sqrt{7}$.
2. **Forgetting the square root.** Magnitude is $\sqrt{x^2 + y^2}$, *not* $x^2 + y^2$.
3. **Confusing $\lvert \mathbf{a} \rvert$ with $\mathbf{a}$ itself.** $\lvert \mathbf{a} \rvert$ is a *number* (length); $\mathbf{a}$ is the vector. Don't write $\lvert \mathbf{a} \rvert$ where you mean $\mathbf{a}$.
4. **Incorrect distance-formula application.** $\overrightarrow{AB} = B - A$ (final minus initial). Reversing gives $\overrightarrow{BA} = -\overrightarrow{AB}$, which has the *same* magnitude (distance is undirected).

---

## Exam Notes

### Cambridge 0580 / 0606

**Syllabus ref:** E7.3 (0580) and §13.3 (0606). Standard patterns:

- "Find the magnitude of the vector $\begin{pmatrix} 5 \\ -12 \end{pmatrix}$." ($\sqrt{25 + 144} = 13$.)
- "A and B are points with position vectors $\mathbf{a} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 4 \\ 6 \end{pmatrix}$. Find $\lvert \overrightarrow{AB} \rvert$." ($\overrightarrow{AB} = \mathbf{b} - \mathbf{a} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$, magnitude $5$.)
- "Find a unit vector in the direction of $\begin{pmatrix} 6 \\ -8 \end{pmatrix}$." (Magnitude $10$, unit vector $\begin{pmatrix} 0.6 \\ -0.8 \end{pmatrix}$.)

### A-Level / IB / AP

A-Level extends to:

- **Dot product** for two vectors $\mathbf{a} \cdot \mathbf{b} = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \cos\theta$ — links magnitude to angle between vectors.
- **Cross product** in 3D — magnitude $\lvert \mathbf{a} \times \mathbf{b} \rvert = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \sin\theta$ measures parallelogram area.
- **$n$-dimensional norms** — the same Pythagorean formula generalises to $\mathbb{R}^n$ and is foundational in linear algebra and machine learning.

---

## Connections

- **Prerequisite:** [[Vectors]] — vector basics, components, addition
- **Prerequisite:** [[Pythagoras Theorem]] — magnitude *is* Pythagoras applied to components
- **Sibling:** [[Length and Midpoint (Vocab)]] — distance formula in 2D = vector magnitude
- **Forward:** [[Vector Geometry]] — applications using magnitudes in geometry problems
- **Forward:** [[Complex Numbers]] — magnitude of $z = a + bi$ is $\sqrt{a^2 + b^2}$, exactly the same Pythagoras formula
- **Application:** *physics* — speed = magnitude of velocity; force magnitude = $\lvert \mathbf{F} \rvert$
- **Beyond syllabus:** *Euclidean norm* in $\mathbb{R}^n$, *$L^p$ norms* generalising Pythagoras, *unit-vector formulations* in physics and machine learning

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\lvert \mathbf{a} \rvert$ | `\lvert \mathbf{a} \rvert` | magnitude (preferred — avoids the bare-pipe table-collision) |
| $\| \mathbf{a} \|$ | `\| \mathbf{a} \|` | alternate "norm" notation, common in linear algebra |
| $\hat{\mathbf{a}}$ | `\hat{\mathbf{a}}` | unit vector in direction of $\mathbf{a}$ |
| $\mathbf{a} = \begin{pmatrix} x \\ y \end{pmatrix}$ | `\begin{pmatrix} x \\ y \end{pmatrix}` | column-vector form |
| $\sqrt{x^2 + y^2 + z^2}$ | `\sqrt{x^2 + y^2 + z^2}` | 3D magnitude |
