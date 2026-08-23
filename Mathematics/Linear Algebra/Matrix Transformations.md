---
chinese: 矩阵变换 (jǔzhèn biànhuàn)
prerequisites:
  - "[[Matrix]]"
  - "[[Identity Matrix]]"
  - "[[Transformations (Vocab)]]"
  - "[[Vector Geometry]]"
  - "[[Similarity]]"
  - "[[Vectors]]"
leads_to:
  - "[[Combination of Transformations]]"
  - "[[Determinants and Inverses]]"
  - "[[Invariant Points and Lines]]"
  - "[[Eigenvalues and Eigenvectors]]"
tags:
  - subject/mathematics
  - domain/matrices
  - domain/transformations
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - syllabus/9260-G25
  - syllabus/9231-1-4
  - type/definition
  - type/vocabulary
  - notation/matrix
  - misconception/reflection-axis-confusion
  - misconception/rotation-direction
---

# Matrix Transformations 矩阵变换

## Definition

### Formal

A **matrix transformation** is a geometric transformation of the $x$-$y$ plane that can be represented by multiplying a position vector by a $2 \times 2$ matrix:

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$

where $(x, y)$ is the original point and $(x', y')$ is the image.

At 9260, all transformations are centred on the origin.

### Intuitive

Every $2 \times 2$ matrix encodes a rule for moving points around the plane. To find where a point ends up, you multiply the matrix by the point's coordinates (written as a column). The matrix is the machine; the column vector is the input; the result is the output.

### 中文锚点 (Chinese Anchor)

矩阵变换：用一个$2 \times 2$矩阵乘以坐标来实现几何变换。

每种变换（旋转、反射、放大）都对应一个特定的矩阵。

## The Unit Square

The **unit square** has vertices at:

$$O = \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \quad A = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad B = \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad C = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

To find a transformation matrix, apply it to the unit square. The key shortcut:

$$\text{If } \mathbf{M} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \text{ then } \mathbf{M} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} a \\ c \end{pmatrix} \text{ and } \mathbf{M} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} b \\ d \end{pmatrix}$$

So **column 1** is the image of $(1, 0)$ and **column 2** is the image of $(0, 1)$.

> [!tip] Quick method for finding any transformation matrix
> 1. Where does $(1, 0)$ go? → Write as column 1.
> 2. Where does $(0, 1)$ go? → Write as column 2.
> Done.

## Transformation Matrices (9260 Required Set)

### Rotations (anticlockwise about the origin)

| Transformation | Matrix | $(1,0) \to$ | $(0,1) \to$ |
|---|---|---|---|
| Rotation 90° anticlockwise | $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | $(0, 1)$ | $(-1, 0)$ |
| Rotation 180° | $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$ | $(-1, 0)$ | $(0, -1)$ |
| Rotation 270° anticlockwise (= 90° clockwise) | $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ | $(0, -1)$ | $(1, 0)$ |

### Reflections

| Transformation | Matrix | $(1,0) \to$ | $(0,1) \to$ |
|---|---|---|---|
| Reflection in $x$-axis ($y = 0$) | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | $(1, 0)$ | $(0, -1)$ |
| Reflection in $y$-axis ($x = 0$) | $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ | $(-1, 0)$ | $(0, 1)$ |
| Reflection in $y = x$ | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | $(0, 1)$ | $(1, 0)$ |
| Reflection in $y = -x$ | $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ | $(0, -1)$ | $(-1, 0)$ |

### Enlargements (centred on the origin)

| Transformation | Matrix | $(1,0) \to$ | $(0,1) \to$ |
|---|---|---|---|
| Enlargement scale factor $k$ | $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ | $(k, 0)$ | $(0, k)$ |

Note: this is the same as $k\mathbf{I}$, i.e., scalar multiplication of the identity matrix.

## Key Facts / Properties

### How to Identify a Transformation from its Matrix

1. **Diagonal with equal entries, zeros elsewhere** → Enlargement (scale factor = diagonal entry)
2. **$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$** → Identity (no change) — special case of enlargement with $k = 1$
3. **Off-diagonal pattern with zeros on diagonal** → Likely a reflection in $y = x$ or $y = -x$, or a rotation
4. **All entries are 0, ±1** → Rotation or reflection

### Quick Recognition Table

| Matrix pattern | Transformation |
|---|---|
| $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ | Rotation by $\theta$ anticlockwise (general form — not required at 9260 but helps understanding) |
| Diagonal: $(a, a)$ | Enlargement, SF $= a$ |
| Diagonal: $(1, -1)$ | Reflection in $x$-axis |
| Diagonal: $(-1, 1)$ | Reflection in $y$-axis |
| Anti-diagonal: $(1, 1)$ | Reflection in $y = x$ |
| Anti-diagonal: $(-1, -1)$ | Reflection in $y = -x$ |

### The Origin Never Moves

Every matrix transformation maps the origin to itself:

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

This is why 9260 restricts all transformations to be centred on the origin.

## Common Misconceptions (Teaching Notes)

### 1. Rotation direction confusion

"90° rotation" without specifying direction is ambiguous. The 9260 spec uses 90°, 180°, 270° **about the origin** — the convention is **anticlockwise** unless stated otherwise.

**Fix:** Always label the direction. Draw coordinate axes and physically rotate a piece of paper to show the direction.

### 2. Confusing reflection axes

Students mix up reflection in $x = 0$ (the $y$-axis) and reflection in $y = 0$ (the $x$-axis).

**Fix:** The axis name tells you what **stays the same**:
- Reflect in $y$-axis → $y$ stays, $x$ flips → $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$
- Reflect in $x$-axis → $x$ stays, $y$ flips → $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$

### 3. "Rotation 90° clockwise = rotation 90° anticlockwise"

These give different matrices. At 9260:
- 90° anticlockwise = $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$
- 90° clockwise (= 270° anticlockwise) = $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$

Note the sign swap in the off-diagonal entries.

### 4. Forgetting to write the matrix — describing the transformation instead

9260 may ask: "Write down the matrix that represents…" Students must give the $2 \times 2$ matrix, not a verbal description.

## Exam Notes

### OxAQA 9260

- Extension tier only (G25)
- Transformations are **restricted to**:
  - Rotations of 90°, 180°, 270° about the origin
  - Reflections in lines $x = 0$, $y = 0$, $y = x$, $y = -x$
  - Enlargements centred on the origin
- Representation by a $2 \times 2$ matrix acting on the unit square
- Students must be able to:
  - **Given a transformation** → write the matrix
  - **Given a matrix** → identify the transformation
  - **Apply** a matrix to specific points or the unit square
- Both Paper 1E and Paper 2E (calculators allowed)

## Connections

- **Parent:** [[Matrix]] — transformation matrices are specific $2 \times 2$ matrices
- **Partner:** [[Identity Matrix]] — represents the "no change" transformation
- **Leads to:** [[Combination of Transformations]] — multiply matrices to combine transformations
- **Geometric partner:** [[Transformations (Vocab)|Transformations]] — the same transformations described without matrices (G21)
- **Vectors:** [[Vectors]] — the column vector being transformed is a position vector

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | `\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}` | Rotation 90° anticlockwise |
| $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$ | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | Rotation 180° |
| $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ | `\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}` | Rotation 270° anticlockwise |
| $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | `\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}` | Reflection in $x$-axis |
| $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ | `\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}` | Reflection in $y$-axis |
| $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | `\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}` | Reflection in $y = x$ |
| $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ | `\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}` | Reflection in $y = -x$ |
| $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ | `\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}` | Enlargement SF $k$ |
