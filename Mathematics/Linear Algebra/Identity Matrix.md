---
chinese: 单位矩阵 (dānwèi jǔzhèn)
prerequisites:
  - "[[Matrix]]"
leads_to:
  - "[[Matrix Transformations]]"
  - "[[Combination of Transformations]]"
  - "[[Determinants and Inverses]]"
tags:
  - subject/mathematics
  - domain/matrices
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - syllabus/9260-G24
  - syllabus/9231-1-4
  - type/definition
  - type/vocabulary
  - notation/identity-matrix
  - misconception/identity-vs-zero-matrix
---

# Identity Matrix 单位矩阵

## Definition

### Formal

The **identity matrix** $\mathbf{I}$ is the $2 \times 2$ matrix:

$$\mathbf{I} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

It has the property that for any $2 \times 2$ matrix $\mathbf{A}$:

$$\mathbf{AI} = \mathbf{IA} = \mathbf{A}$$

and for any column vector $\begin{pmatrix} x \\ y \end{pmatrix}$:

$$\mathbf{I} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix}$$

### Intuitive

The identity matrix is the "do nothing" matrix — it's the matrix equivalent of multiplying by 1. When you multiply any matrix by $\mathbf{I}$, you get back exactly what you started with.

In transformation terms: applying $\mathbf{I}$ to a shape leaves every point exactly where it is.

### 中文锚点 (Chinese Anchor)

单位矩阵：矩阵里的"1"。

就像 $5 \times 1 = 5$（乘1不变），矩阵也有一个"乘了等于没乘"的矩阵，就是单位矩阵 $\mathbf{I}$。

对角线上是1，其余位置是0。

## Notation

| Convention | Symbol | Notes |
|---|---|---|
| Identity matrix | $\mathbf{I}$ | Bold uppercase I; sometimes $\mathbf{I}_2$ to specify $2 \times 2$ |
| Handwriting | $\underline{I}$ | Underlined in handwriting to indicate a matrix |

> [!warning] Don't confuse with the number 1
> $\mathbf{I}$ is a matrix, not a number. Writing $\mathbf{A} \times 1 = \mathbf{A}$ is wrong notation — the correct statement is $\mathbf{AI} = \mathbf{A}$.

## Key Facts / Properties

### Structure

The identity matrix has:
- **1s on the main diagonal** (top-left to bottom-right)
- **0s everywhere else**

### Key Properties

| Property | Statement | Comparison |
|---|---|---|
| Left identity | $\mathbf{IA} = \mathbf{A}$ | Like $1 \times a = a$ |
| Right identity | $\mathbf{AI} = \mathbf{A}$ | Like $a \times 1 = a$ |
| Commutative with all | $\mathbf{AI} = \mathbf{IA}$ | $\mathbf{I}$ is one of the rare matrices that commutes with everything |
| Self-multiplying | $\mathbf{I}^2 = \mathbf{I}$ | Like $1^2 = 1$ |
| As a transformation | Leaves all points unchanged | The "do nothing" transformation |

### Verification

$$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1 \cdot a + 0 \cdot c & 1 \cdot b + 0 \cdot d \\ 0 \cdot a + 1 \cdot c & 0 \cdot b + 1 \cdot d \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

## Common Misconceptions (Teaching Notes)

### 1. "The identity matrix is all 1s"

Students sometimes write $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ as the identity. Show that this fails:

$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 6 & 8 \end{pmatrix} \neq \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix}$$

The off-diagonal entries **must** be 0.

### 2. Confusing identity with zero matrix

The **zero matrix** $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ is the additive identity ($\mathbf{A} + \mathbf{0} = \mathbf{A}$).

The **identity matrix** $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ is the multiplicative identity ($\mathbf{AI} = \mathbf{A}$).

At 9260 only the multiplicative identity is required.

## Exam Notes

### OxAQA 9260

- Only the $2 \times 2$ identity matrix is required (G24)
- Extension tier only
- Often appears in context: "What single matrix represents no transformation?" → $\mathbf{I}$
- Inverse matrices and determinants are **not in the 9260 spec** — don't expect "find the inverse" questions
- Expect questions where recognising $\mathbf{I}$ simplifies a calculation

## Connections

- **Parent:** [[Matrix]] — the identity is a special case of a $2 \times 2$ matrix
- **Application:** [[Matrix Transformations]] — $\mathbf{I}$ represents the identity transformation (no change)
- **Combination:** [[Combination of Transformations]] — $\mathbf{MI} = \mathbf{IM} = \mathbf{M}$ for any transformation matrix $\mathbf{M}$
- **Number analogy:** The number 1 is the identity for multiplication; $\mathbf{I}$ plays the same role for matrices

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{I}$ | `\mathbf{I}` | Identity matrix (bold) |
| $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ | `\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}` | Explicit 2×2 identity |
