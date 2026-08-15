---
chinese: 变换的组合 (biànhuàn de zǔhé)
prerequisites:
  - "[[Matrix]]"
  - "[[Identity Matrix]]"
  - "[[Matrix Transformations]]"
leads_to:
  - "[[Invariant Points and Lines]]"
tags:
  - subject/mathematics
  - domain/matrices
  - domain/transformations
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - syllabus/9260-G26
  - syllabus/9231-1-4
  - type/definition
  - misconception/matrix-multiplication-order
---

# Combination of Transformations 变换的组合

## Definition

### Formal

If transformation $\mathbf{A}$ is applied first, then transformation $\mathbf{B}$ is applied second, the **combined transformation** is represented by the matrix product:

$$\mathbf{BA}$$

Note the **reverse order**: the matrix applied first goes on the **right**.

### Intuitive

Imagine a conveyor belt: you put a shape on at the right end. It hits matrix $\mathbf{A}$ first (closest to the shape), then matrix $\mathbf{B}$ (further left). So the order in the product reads right-to-left, like the shape's journey through the machines.

### 中文锚点 (Chinese Anchor)

变换的组合：先做变换$\mathbf{A}$，再做变换$\mathbf{B}$，合起来等于$\mathbf{BA}$（注意顺序相反！）。

关键是看隐藏的括号：

$$\mathbf{B}\mathbf{A}\begin{pmatrix} x \\ y \end{pmatrix} = \mathbf{B}\left(\mathbf{A}\begin{pmatrix} x \\ y \end{pmatrix}\right)$$

先算括号里面的——$\mathbf{A}$先作用于点，得到新点，再被$\mathbf{B}$作用。所以"先$\mathbf{A}$后$\mathbf{B}$"写成$\mathbf{BA}$，因为$\mathbf{A}$永远紧贴着点（在括号最里层）。

## Key Facts / Properties

### Why the Order is Reversed

Starting from a point $\mathbf{p}$:

1. Apply $\mathbf{A}$ first: $\mathbf{p'} = \mathbf{A}\mathbf{p}$
2. Apply $\mathbf{B}$ to the result: $\mathbf{p''} = \mathbf{B}\mathbf{p'} = \mathbf{B}(\mathbf{A}\mathbf{p}) = (\mathbf{BA})\mathbf{p}$

So "$\mathbf{A}$ first, then $\mathbf{B}$" = matrix $\mathbf{BA}$.

### Worked Example

**Reflect in the $x$-axis, then rotate 90° anticlockwise.**

Reflection in $x$-axis: $\mathbf{A} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$

Rotation 90° anticlockwise: $\mathbf{B} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$

Combined ($\mathbf{A}$ first, then $\mathbf{B}$):

$$\mathbf{BA} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 \cdot 1 + (-1) \cdot 0 & 0 \cdot 0 + (-1)(-1) \\ 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 0 + 0 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

Result: $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ — this is reflection in $y = x$.

So: reflect in $x$-axis then rotate 90° anticlockwise = reflect in $y = x$.

### Does Order Matter?

**Yes.** Doing $\mathbf{A}$ then $\mathbf{B}$ gives $\mathbf{BA}$, but doing $\mathbf{B}$ then $\mathbf{A}$ gives $\mathbf{AB}$, and in general $\mathbf{AB} \neq \mathbf{BA}$.

Using the same example in reverse order ($\mathbf{B}$ first, then $\mathbf{A}$):

$$\mathbf{AB} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$$

This is reflection in $y = -x$ — a **different** result.

### Identifying the Combined Transformation

After multiplying, compare the resulting matrix to the standard transformation matrices from [[Matrix Transformations]]:

| Result matrix | Transformation |
|---|---|
| $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ | Identity (the two transformations "cancel out") |
| $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | Reflection in $y = x$ |
| $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$ | Rotation 180° |
| ... | See full table in [[Matrix Transformations]] |

### Self-Inverse Transformations

Some transformations, when applied twice, return to the original. For these, $\mathbf{M}^2 = \mathbf{I}$:

- Reflection in any line → always self-inverse ($\mathbf{M}^2 = \mathbf{I}$)
- Rotation 180° → self-inverse ($\mathbf{M}^2 = \mathbf{I}$)
- Rotation 90° → **not** self-inverse ($\mathbf{M}^2 \neq \mathbf{I}$, but $\mathbf{M}^4 = \mathbf{I}$)

## Common Misconceptions (Teaching Notes)

### 1. Writing the matrices in the wrong order

This is **the** most common error. Students write "A then B" as $\mathbf{AB}$ when it should be $\mathbf{BA}$.

**Fix:** Always start from the point and work outward:

$$\underbrace{\mathbf{B}}_{\text{second}} \underbrace{\mathbf{A}}_{\text{first}} \begin{pmatrix} x \\ y \end{pmatrix}$$

The first transformation to act on the point is the one nearest to it.

### 2. "The answer should be one of the standard transformations"

Not always. At 9260, combined transformations will produce results from the standard set (since the spec restricts to rotations, reflections, enlargements), but students should recognise that this is a feature of the specific transformations in the 9260 syllabus, not a universal rule.

### 3. Forgetting that the combined matrix is a single matrix

Some students multiply, identify the transformation, but then forget to state the single matrix when asked. The exam may ask: "Find the single matrix that represents…" — the answer is the product, written as one matrix.

## Exam Notes

### OxAQA 9260

- Extension tier only (G26)
- "Combination of transformations" means finding the matrix product
- Exam questions typically:
  - "Transformation $\mathbf{P}$ is … and transformation $\mathbf{Q}$ is … Find the matrix for $\mathbf{P}$ followed by $\mathbf{Q}$."
  - "Describe the single transformation represented by $\mathbf{QP}$."
  - "Show that applying transformation $\mathbf{M}$ twice returns to the original."
- Both Paper 1E and Paper 2E (calculators allowed)
- Uses matrix multiplications (stated in spec notes for G26)
- **i** and **j** notation is **not** required

## Connections

- **Parents:** [[Matrix]], [[Matrix Transformations]]
- **Partner:** [[Identity Matrix]] — for any transformation matrix $\mathbf{M}$, $\mathbf{MI} = \mathbf{IM} = \mathbf{M}$ (combining with "do nothing" changes nothing)
- **Geometric partner:** [[Transformations (Vocab)|Transformations]] — the same combinations described without matrices
- **Algebra link:** Non-commutativity of matrix multiplication (from [[Matrix]]) is what makes order matter here

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{BA}$ | `\mathbf{BA}` | A first, then B |
| $\mathbf{M}^2$ | `\mathbf{M}^2` | Transformation M applied twice |
| $\mathbf{M}^2 = \mathbf{I}$ | `\mathbf{M}^2 = \mathbf{I}` | Self-inverse transformation |
