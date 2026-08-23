---
chinese: 矩阵 (jǔzhèn)
prerequisites:
  - "[[Four Operations (Vocab)]]"
  - "[[Vectors]]"
leads_to:
  - "[[Identity Matrix]]"
  - "[[Matrix Transformations]]"
  - "[[Combination of Transformations]]"
  - "[[Determinants and Inverses]]"
  - "[[Linear Systems in 3D]]"
tags:
  - subject/mathematics
  - domain/matrices
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - syllabus/9260-G23
  - syllabus/9231-1-4
  - type/definition
  - type/vocabulary
  - notation/matrix
  - misconception/matrix-multiplication-order
  - misconception/matrix-commutativity
---

# Matrix 矩阵

## Definition

### Formal

A **matrix** is a rectangular array of numbers arranged in rows and columns, enclosed in brackets.

A matrix with $m$ rows and $n$ columns is called an $m \times n$ matrix (read "$m$ by $n$"). The number in row $i$, column $j$ is called the **entry** (or **element**) $a_{ij}$.

At OxAQA 9260, only $2 \times 2$ and $2 \times 1$ matrices are required.

### Intuitive

Think of a matrix as a grid of numbers — like a mini spreadsheet. A $2 \times 2$ matrix is a 2-by-2 grid, and a $2 \times 1$ matrix is just a column of two numbers (which represents a point or vector in 2D).

### 中文锚点 (Chinese Anchor)

矩阵：按行和列排列的数的矩形阵列。中文"矩"意为矩形——名字本身就在告诉你它长什么样。

矩阵乘法的核心口诀：**行乘列，加起来**。左边矩阵取一行，右边矩阵取一列，对应相乘再相加，得到一个数。

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} ax + by \\ cx + dy \end{pmatrix}$$

## Notation

| Convention | Example | Read as | Notes |
|---|---|---|---|
| $2 \times 2$ matrix | $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ | "a two-by-two matrix" | Round brackets standard at IGCSE |
| $2 \times 1$ column matrix | $\begin{pmatrix} x \\ y \end{pmatrix}$ | "a column vector / column matrix" | Represents a point or vector |
| Matrix name | $\mathbf{A}$, $\mathbf{B}$, $\mathbf{M}$ | "matrix A" | Bold uppercase in print; underlined in handwriting |
| Entry notation | $a_{ij}$ | "a-i-j" | Row $i$, column $j$ |

## Key Facts / Properties

### Scalar Multiplication

Multiply every entry by the scalar:

$$k \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} ka & kb \\ kc & kd \end{pmatrix}$$

### Matrix Multiplication ($2 \times 2$ by $2 \times 2$)

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} e & f \\ g & h \end{pmatrix} = \begin{pmatrix} ae + bg & af + bh \\ ce + dg & cf + dh \end{pmatrix}$$

**Pattern:** Each entry is a **row × column** dot product.

- Top-left: (row 1 of first) · (col 1 of second) = $ae + bg$
- Top-right: (row 1 of first) · (col 2 of second) = $af + bh$
- Bottom-left: (row 2 of first) · (col 1 of second) = $ce + dg$
- Bottom-right: (row 2 of first) · (col 2 of second) = $cf + dh$

### Matrix Multiplication ($2 \times 2$ by $2 \times 1$)

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} ax + by \\ cx + dy \end{pmatrix}$$

This is the key operation for transformations: the matrix acts on a point $(x, y)$.

### Properties of Multiplication

| Property | Holds? | Note |
|---|---|---|
| Associative | Yes | $\mathbf{A}(\mathbf{BC}) = (\mathbf{AB})\mathbf{C}$ |
| Commutative | **No** | $\mathbf{AB} \neq \mathbf{BA}$ in general |
| Distributive | Yes | $\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{AB} + \mathbf{AC}$ |

## Common Misconceptions (Teaching Notes)

### 1. "Multiply matching positions"

Students instinctively try entry-by-entry multiplication (Hadamard product). This is **not** how matrix multiplication works. Drill the row-by-column pattern early.

**Fix:** Walk through the "row of first × column of second" pattern with fingers tracing across the first matrix and down the second.

### 2. "AB = BA"

Students assume multiplication is commutative because it is for numbers. Show a concrete counterexample:

$$\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix}$$

$$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}$$

Different results. This matters critically for [[Combination of Transformations]].

### 3. Size confusion

Students forget which sizes can multiply. The rule: **columns of first = rows of second**.

- $2 \times 2$ by $2 \times 2$ → $2 \times 2$ ✓
- $2 \times 2$ by $2 \times 1$ → $2 \times 1$ ✓
- $2 \times 1$ by $2 \times 2$ → ✗ (1 column ≠ 2 rows)

At 9260 this is simple — only the first two cases appear.

## Exam Notes

### OxAQA 9260

- Only $2 \times 2$ and $2 \times 1$ matrices at Extension tier
- **Not assessed** at Core tier — matrices are Extension-only (G23–G26)
- Multiplication of $2 \times 2$ by $2 \times 2$, $2 \times 2$ by $2 \times 1$, and scalar multiplication are all required
- Both Paper 1E and Paper 2E may include matrix questions (calculators allowed on both)
- **i** and **j** notation is **not** required (stated in spec)
- Expect questions combining matrix multiplication with transformation identification — see [[Matrix Transformations]]

## Connections

- **Core concept:** [[Identity Matrix]] — the matrix equivalent of multiplying by 1
- **Application:** [[Matrix Transformations]] — matrices encode geometric transformations
- **Combination:** [[Combination of Transformations]] — multiply matrices to combine transformations
- **Related:** [[Vectors]] — a $2 \times 1$ matrix is essentially a column vector
- **Related:** [[Transformations (Vocab)|Transformations]] — matrices give an algebraic way to describe the same transformations

> [!info] Beyond syllabus — "Why do we learn matrices?"
> Students often ask why matrices matter. Here are three concrete answers, escalating in scope:
>
> 1. **Computer graphics.** Every rotation, reflection, and zoom on your phone screen is a matrix multiplication. Games, animations, and filters all run on matrices — thousands of them per second.
> 2. **Solving systems of equations.** Two equations with two unknowns? That's a $2 \times 2$ matrix problem. Real-world systems (engineering, economics, logistics) can have hundreds of unknowns — matrices are the only practical way to solve them.
> 3. **Artificial intelligence.** Neural networks are built on matrix multiplications. The Transformer architecture (behind ChatGPT, image generators, etc.) is fundamentally a sequence of matrix operations. Linear algebra is the language AI thinks in.
>
> At 9260 you only see $2 \times 2$ matrices. But the same ideas scale — a $1000 \times 1000$ matrix works exactly the same way, just bigger.
>
> And if the whole thing feels like a tool that arrived from nowhere — a grid with a strange multiplication rule — that feeling has a history, and it is told in [[Determinants and Inverses]] §"Where matrices came from": the counting-board arrays of the 九章算术, Leibniz's determinant, Sylvester's *womb*, Cayley's algebra, and the physicist who reinvented matrices in 1925 without knowing they existed.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ | `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` | 2×2 matrix (round brackets) |
| $\begin{pmatrix} x \\ y \end{pmatrix}$ | `\begin{pmatrix} x \\ y \end{pmatrix}` | Column vector / 2×1 matrix |
| $\mathbf{A}$ | `\mathbf{A}` | Bold matrix name |
| $a_{ij}$ | `a_{ij}` | Entry at row i, column j |
