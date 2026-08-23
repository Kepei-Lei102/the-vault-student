---
chinese: 叉积 (chā jī)
prerequisites:
  - "[[3D Vectors and the Scalar Product]]"
  - "[[Vectors]]"
  - "[[Trigonometric Ratios]]"
  - "[[Magnitude of a Vector (Vocab)]]"
leads_to:
  - "[[Planes in 3D]]"
  - "[[Torque]]"
  - "[[Angular Momentum]]"
  - "[[Lorentz Force]]"
  - "[[Maxwell's Equations]]"
  - "[[Eigenvalues and Eigenvectors]]"
tags:
  - subject/mathematics
  - domain/geometry
  - domain/linear-algebra
  - level/A-Level
  - level/pre-IB
  - curriculum/A-Level-Further
  - curriculum/IB-AA
  - syllabus/9231-1-6
  - type/definition
  - type/theorem
  - type/proof
  - notation/cross-product
  - notation/determinant
  - misconception/cross-output-is-scalar
  - misconception/forgetting-anticommutativity
  - misconception/cross-is-associative
  - misconception/sin-vs-cos-mixup
---

# Cross Product 叉积

## Definition

### Formal

The **cross product** (also *vector product*) of two 3D vectors $\mathbf{a}, \mathbf{b}$ is a **new vector** — written $\mathbf{a} \times \mathbf{b}$ — defined by two requirements:

$$\boxed{\;|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}|\,|\mathbf{b}|\,\sin\theta,\qquad \mathbf{a}\times\mathbf{b}\ \perp\ \mathbf{a}\ \text{and}\ \mathbf{b}\;}$$

where $\theta \in [0, \pi]$ is the angle between $\mathbf{a}$ and $\mathbf{b}$. Two vectors are perpendicular to a whole *plane*, so the magnitude rule alone leaves a two-way choice of direction; the **right-hand rule** breaks the tie. Curl the fingers of your right hand from $\mathbf{a}$ toward $\mathbf{b}$; your thumb points along $\mathbf{a} \times \mathbf{b}$.

In components, with the standard basis $\mathbf{i}, \mathbf{j}, \mathbf{k}$:

$$\mathbf{a} \times \mathbf{b} = (a_2 b_3 - a_3 b_2)\,\mathbf{i} - (a_1 b_3 - a_3 b_1)\,\mathbf{j} + (a_1 b_2 - a_2 b_1)\,\mathbf{k}.$$

### Intuitive

The [[3D Vectors and the Scalar Product|dot product]] answers *"how much do these two vectors line up?"* — and returns a number. The cross product answers a different question: ***"these two vectors span a flat patch of space — give me the vector that stands up out of that patch, and make it longer when the patch is bigger."***

So the cross product packs **two pieces of geometry into one vector**:

- Its **length** is the *area* of the parallelogram the two vectors span ($|\mathbf{a}||\mathbf{b}|\sin\theta$ is exactly base $\times$ height).
- Its **direction** is the *orientation* of that patch — the normal, with a sign telling you which face is "up."

That is why it lives only in 3D: you need a third dimension for the result to point *out of* the plane the two inputs share. The dot product works in any dimension; the cross product is a creature of three-dimensional space (with one exotic exception in 7D, noted at the very end).

### 中文锚点

**叉积**（chā jī），又叫**向量积**（vector product）或**外积**（wài jī）。它和[[3D Vectors and the Scalar Product|数量积（点积）]]是三维空间里的一对"双胞胎"，但结果完全不同：

- **点积** $\mathbf{a}\cdot\mathbf{b}$ 输出**一个数**（标量），衡量两向量的**对齐程度**，公式带 $\cos\theta$，在 $0°$ 时最大。
- **叉积** $\mathbf{a}\times\mathbf{b}$ 输出**一个向量**，这个向量**垂直于**原来两个向量张成的平面，长度等于 $|\mathbf{a}||\mathbf{b}|\sin\theta$（即平行四边形的面积），公式带 $\sin\theta$，在 $90°$ 时最大。

记忆口诀：**点积管"齐不齐"（对齐 → cos），叉积管"开不开"（张开成面 → sin）。** 方向靠**右手定则**（yòushǒu dìngzé）：右手四指从 $\mathbf{a}$ 弯向 $\mathbf{b}$，大拇指指向 $\mathbf{a}\times\mathbf{b}$。

## Bridge — the two products of $\mathbb{R}^3$, side by side

The cross product is best learned *against* the dot product you already know. They are the two fundamental ways to multiply vectors in 3D, and almost every property is a mirror image:

| Feature | Dot product $\mathbf{a}\cdot\mathbf{b}$ | Cross product $\mathbf{a}\times\mathbf{b}$ |
|---|---|---|
| Output type | **scalar** (a number) | **vector** |
| Geometric size | $\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\cos\theta$ | $\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\sin\theta$ |
| Peaks when | $\theta = 0°$ (**aligned**) | $\theta = 90°$ (**perpendicular**) |
| Zero when | $\theta = 90°$ (perpendicular) | $\theta = 0°$ or $180°$ (**parallel**) |
| Measures | alignment / projection | spanned area / "how perpendicular" |
| Order swap | $\mathbf{a}\cdot\mathbf{b} = \mathbf{b}\cdot\mathbf{a}$ (**commutative**) | $\mathbf{a}\times\mathbf{b} = -\,\mathbf{b}\times\mathbf{a}$ (**anti**commutative) |
| Lives in | any dimension $\mathbb{R}^n$ | only $\mathbb{R}^3$ (and $\mathbb{R}^7$) |

The two are bolted together by one gorgeous identity (proved below):

$$|\mathbf{a} \times \mathbf{b}|^2 + (\mathbf{a} \cdot \mathbf{b})^2 = |\mathbf{a}|^2|\mathbf{b}|^2,$$

which is nothing but $\sin^2\theta + \cos^2\theta = 1$ wearing a disguise. **The dot product is the cosine half of vector multiplication; the cross product is the sine half.** Knowing one tells you a lot about the other.

![[cross-product-dot-vs-cross.svg]]
*Left: $\mathbf{a}\times\mathbf{b}$ is the vector that stands up out of the parallelogram spanned by $\mathbf{a}$ and $\mathbf{b}$ — perpendicular to both, with length equal to that parallelogram's area. Right: the two products as functions of the angle. The dot product (blue) is largest when the vectors align ($0°$) and vanishes when they are perpendicular; the cross-product magnitude (magenta) does the exact opposite — largest at $90°$, zero when the vectors are parallel. They are equal at $45°$, and $\sin^2\theta + \cos^2\theta = 1$ ties them together for every angle.*

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Cross / vector product | $\mathbf{a} \times \mathbf{b}$ | "a cross b" | The $\times$ is mandatory; never write $\mathbf{a}\mathbf{b}$ |
| Determinant mnemonic | $\det\!\begin{pmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{pmatrix}$ | "the determinant" | Formal device for recalling the component formula |
| Magnitude (area) | $\lvert \mathbf{a}\times\mathbf{b}\rvert$ | "mod a cross b" | Equals the parallelogram area |
| Scalar triple product | $\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})$ | "a dot b cross c" | A scalar; equals the parallelepiped volume |

> [!warning] Notation Trap — $\times$ is not "times"
> In $\mathbf{a} \times \mathbf{b}$ the cross is a *named operation on vectors*, not ordinary multiplication. And it is a different animal from the dot: $\mathbf{a}\cdot\mathbf{b}$ gives a number, $\mathbf{a}\times\mathbf{b}$ gives a vector. Writing "$\mathbf{a}\times\mathbf{b} = 12$" is a type error — the answer must be a vector. Conversely "$\mathbf{a}\cdot\mathbf{b} = 2\mathbf{i}+\mathbf{k}$" is a type error the other way.

## Key Facts / Properties

### The component (determinant) formula

To compute $\mathbf{a}\times\mathbf{b}$ from coordinates, expand the symbolic determinant along its top row:

$$\mathbf{a} \times \mathbf{b} = \det\!\begin{pmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{pmatrix} = \mathbf{i}\begin{vmatrix}a_2&a_3\\ b_2&b_3\end{vmatrix} - \mathbf{j}\begin{vmatrix}a_1&a_3\\ b_1&b_3\end{vmatrix} + \mathbf{k}\begin{vmatrix}a_1&a_2\\ b_1&b_2\end{vmatrix}$$

where each $2\times2$ determinant is the "cross-multiply and subtract" rule $\begin{vmatrix}p&q\\ r&s\end{vmatrix} = ps - qr$. Multiplying out:

$$\mathbf{a} \times \mathbf{b} = (a_2 b_3 - a_3 b_2)\,\mathbf{i} - (a_1 b_3 - a_3 b_1)\,\mathbf{j} + (a_1 b_2 - a_2 b_1)\,\mathbf{k}.$$

**Watch the middle sign.** The $\mathbf{j}$ component carries a leading minus, which flips $(a_1 b_3 - a_3 b_1)$ into $(a_3 b_1 - a_1 b_3)$. This alternating $+,-,+$ is the single most common slip — the determinant layout exists precisely to make you remember it.

### Why is the result perpendicular to both inputs?

The definition *demands* $\mathbf{a}\times\mathbf{b}\perp\mathbf{a}$. Here is the one-line check that the component formula delivers it. Take the dot product with $\mathbf{a}$:

$$(\mathbf{a}\times\mathbf{b})\cdot\mathbf{a} = a_1(a_2 b_3 - a_3 b_2) + a_2(a_3 b_1 - a_1 b_3) + a_3(a_1 b_2 - a_2 b_1).$$

Expand and pair the six terms:

$$= \underbrace{a_1 a_2 b_3 - a_2 a_1 b_3}_{0} + \underbrace{a_3 a_1 b_2 - a_1 a_3 b_2}_{0} + \underbrace{a_2 a_3 b_1 - a_3 a_2 b_1}_{0} = 0. \quad \square$$

Every term cancels with a twin. So $\mathbf{a}\times\mathbf{b}$ is perpendicular to $\mathbf{a}$; by the identical argument it is perpendicular to $\mathbf{b}$. The result really does stand up out of the plane of the two inputs.

### Why is the length $|\mathbf{a}||\mathbf{b}|\sin\theta$? — Lagrange's identity

This is the engine room. Square the magnitude of the component formula and grind:

$$|\mathbf{a}\times\mathbf{b}|^2 = (a_2 b_3 - a_3 b_2)^2 + (a_3 b_1 - a_1 b_3)^2 + (a_1 b_2 - a_2 b_1)^2.$$

Multiplying everything out and re-collecting (this is **Lagrange's identity**) gives the clean form:

$$|\mathbf{a}\times\mathbf{b}|^2 = (a_1^2+a_2^2+a_3^2)(b_1^2+b_2^2+b_3^2) - (a_1 b_1 + a_2 b_2 + a_3 b_3)^2 = |\mathbf{a}|^2|\mathbf{b}|^2 - (\mathbf{a}\cdot\mathbf{b})^2.$$

Now substitute the dot product's geometric form $\mathbf{a}\cdot\mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta$:

$$|\mathbf{a}\times\mathbf{b}|^2 = |\mathbf{a}|^2|\mathbf{b}|^2 - |\mathbf{a}|^2|\mathbf{b}|^2\cos^2\theta = |\mathbf{a}|^2|\mathbf{b}|^2(1 - \cos^2\theta) = |\mathbf{a}|^2|\mathbf{b}|^2\sin^2\theta.$$

Since $0\le\theta\le\pi$, $\sin\theta\ge0$, so the square root is clean:

$$\boxed{\;|\mathbf{a}\times\mathbf{b}| = |\mathbf{a}|\,|\mathbf{b}|\,\sin\theta.\;}\quad\square$$

Rearranged, the same calculation *is* the bridge identity $|\mathbf{a}\times\mathbf{b}|^2 + (\mathbf{a}\cdot\mathbf{b})^2 = |\mathbf{a}|^2|\mathbf{b}|^2$ — the Pythagorean splitting of $|\mathbf{a}|^2|\mathbf{b}|^2$ into a "sine part" (cross) and a "cosine part" (dot).

> [!tip] The length is an area
> $|\mathbf{a}||\mathbf{b}|\sin\theta$ is base $\times$ perpendicular height for the parallelogram with edges $\mathbf{a}$ and $\mathbf{b}$ — take $\mathbf{a}$ as the base of length $|\mathbf{a}|$, and $|\mathbf{b}|\sin\theta$ is the height of $\mathbf{b}$ above that base. **So $|\mathbf{a}\times\mathbf{b}|$ literally measures the area of the patch the two vectors span**, and $\tfrac12|\mathbf{a}\times\mathbf{b}|$ is the area of the triangle. This is the cross product's most-used everyday meaning.

### Properties — the mirror table

For all vectors and scalar $\lambda$:

| Property | Statement | Mirror with dot product |
|---|---|---|
| **Anticommutative** | $\mathbf{a}\times\mathbf{b} = -\,\mathbf{b}\times\mathbf{a}$ | dot is *commutative* |
| **Distributive** | $\mathbf{a}\times(\mathbf{b}+\mathbf{c}) = \mathbf{a}\times\mathbf{b} + \mathbf{a}\times\mathbf{c}$ | same as dot |
| **Scalar-compatible** | $(\lambda\mathbf{a})\times\mathbf{b} = \lambda(\mathbf{a}\times\mathbf{b})$ | same as dot |
| **Self-cross is zero** | $\mathbf{a}\times\mathbf{a} = \mathbf{0}$ | dot gives $\lvert\mathbf{a}\rvert^2$ |
| **NOT associative** | $\mathbf{a}\times(\mathbf{b}\times\mathbf{c}) \neq (\mathbf{a}\times\mathbf{b})\times\mathbf{c}$ in general | dot can't even be chained |
| **Basis (cyclic)** | $\mathbf{i}\times\mathbf{j}=\mathbf{k},\ \mathbf{j}\times\mathbf{k}=\mathbf{i},\ \mathbf{k}\times\mathbf{i}=\mathbf{j}$ | dot: all cross-pairs give $0$ |

The basis rule is worth memorising as a **cycle** $\mathbf{i}\to\mathbf{j}\to\mathbf{k}\to\mathbf{i}$: going *forward* round the cycle gives $+$, going *backward* gives $-$ (so $\mathbf{j}\times\mathbf{i} = -\mathbf{k}$). And $\mathbf{a}\times\mathbf{a}=\mathbf{0}$ is immediate from the magnitude rule — the angle is $0$, so $\sin\theta = 0$.

### Why anticommutativity? — the headline jewel

The dot product doesn't care about order: $\cos\theta$ is the same whether you measure the angle from $\mathbf{a}$ to $\mathbf{b}$ or the reverse. The cross product *does* care, and the reason is the right-hand rule. Curling your fingers from $\mathbf{a}$ to $\mathbf{b}$ points your thumb one way; curling from $\mathbf{b}$ to $\mathbf{a}$ is the opposite rotation, so your thumb flips. **Same plane, same area, opposite "up."** Hence $\mathbf{a}\times\mathbf{b} = -\,\mathbf{b}\times\mathbf{a}$.

This is not a quirk — it is the cross product *honestly reporting orientation*. A spanned patch of space has two faces, and which one you call the front depends on the order you name the edges. The minus sign is the bookkeeping of that choice. (It is also exactly why the cross product is non-associative and why it generalises to the *wedge product* of differential forms — see Beyond Syllabus.)

## Special Cases

### The scalar triple product — volume

Combining a cross and a dot, $\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})$ is a **scalar** equal to the signed **volume of the parallelepiped** with edges $\mathbf{a}, \mathbf{b}, \mathbf{c}$. It equals the $3\times3$ determinant whose rows are the three vectors:

$$\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c}) = \det\!\begin{pmatrix}a_1&a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{pmatrix}.$$

A clean corollary: $\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c}) = 0 \iff$ the three vectors are **coplanar** (the box is flat, zero volume). This is the standard test for whether three vectors lie in one plane, and it is the engine behind finding the common perpendicular of two skew lines.

### The vector triple product — BAC-CAB

The non-associativity is tamed by a memorable expansion:

$$\mathbf{a}\times(\mathbf{b}\times\mathbf{c}) = \mathbf{b}\,(\mathbf{a}\cdot\mathbf{c}) - \mathbf{c}\,(\mathbf{a}\cdot\mathbf{b}),$$

nicknamed **"BAC minus CAB."** Note the result lies in the plane of $\mathbf{b}$ and $\mathbf{c}$ (it must — it's perpendicular to $\mathbf{b}\times\mathbf{c}$, which is the normal of that plane).

### The "2D cross product" is a scalar

In 2D there is no room for a perpendicular vector, so the cross product collapses to the single scalar $a_1 b_2 - a_2 b_1$ — the signed area of the parallelogram (positive if $\mathbf{b}$ is anticlockwise from $\mathbf{a}$). It is really the $\mathbf{k}$-component of the 3D cross product of the two vectors embedded in the $z=0$ plane. Useful for orientation tests in computational geometry (which way does a polygon turn?).

## Worked Examples

### Example 1 (foundational): compute a cross product

Let $\mathbf{a} = 2\mathbf{i} + 3\mathbf{j} - \mathbf{k}$ and $\mathbf{b} = \mathbf{i} - 2\mathbf{j} + 4\mathbf{k}$. Find $\mathbf{a}\times\mathbf{b}$.

$$\mathbf{a}\times\mathbf{b} = \det\!\begin{pmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ 2&3&-1\\ 1&-2&4\end{pmatrix}$$

- $\mathbf{i}$: $\begin{vmatrix}3&-1\\ -2&4\end{vmatrix} = (3)(4)-(-1)(-2) = 12 - 2 = 10$
- $\mathbf{j}$: $-\begin{vmatrix}2&-1\\ 1&4\end{vmatrix} = -\big[(2)(4)-(-1)(1)\big] = -(8+1) = -9$
- $\mathbf{k}$: $\begin{vmatrix}2&3\\ 1&-2\end{vmatrix} = (2)(-2)-(3)(1) = -4 - 3 = -7$

$$\mathbf{a}\times\mathbf{b} = 10\,\mathbf{i} - 9\,\mathbf{j} - 7\,\mathbf{k}.$$

**Self-check (always do this):** dot the answer with $\mathbf{a}$: $(10)(2)+(-9)(3)+(-7)(-1) = 20 - 27 + 7 = 0$. ✓ Perpendicular, as required.

### Example 2 (9231 / IB HL): area of a triangle

Find the area of the triangle with vertices $A(1,0,1)$, $B(2,1,3)$, $C(0,2,2)$.

Form two edge vectors from $A$:

$$\vec{AB} = (1,1,2),\qquad \vec{AC} = (-1,2,1).$$

$$\vec{AB}\times\vec{AC} = \det\!\begin{pmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ 1&1&2\\ -1&2&1\end{pmatrix} = \mathbf{i}(1-4) - \mathbf{j}(1+2) + \mathbf{k}(2+1) = (-3, -3, 3).$$

The parallelogram area is $|(-3,-3,3)| = \sqrt{9+9+9} = 3\sqrt3$, so the **triangle area is $\tfrac12 \cdot 3\sqrt3 = \dfrac{3\sqrt3}{2}\approx 2.60$**.

### Example 3 (9231 / IB HL): normal to a plane

Find a vector normal to the plane through the three points of Example 2, then write the plane's equation.

$\vec{AB}\times\vec{AC} = (-3,-3,3)$ is already perpendicular to both edges, hence normal to the plane. Scale it down to $\mathbf{n} = (1, 1, -1)$ (dividing by $-3$ — any nonzero multiple is still a valid normal). The plane has equation $\mathbf{n}\cdot\mathbf{r} = \mathbf{n}\cdot\mathbf{a}$ using point $A(1,0,1)$:

$$x + y - z = (1)(1)+(1)(0)+(-1)(1) = 0 \quad\Rightarrow\quad x + y - z = 0.$$

(Check $B$: $2+1-3=0$ ✓; $C$: $0+2-2=0$ ✓.) The cross product is the standard tool for *building* a plane's normal from two vectors lying in it — the bridge into [[Planes in 3D]].

### Example 4 (physics application): torque

A spanner applies force $\mathbf{F} = (0, 0, 40)\ \text{N}$ at the end of a lever arm $\mathbf{r} = (0.3, 0, 0)\ \text{m}$ from the bolt. The torque is

$$\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F} = \det\!\begin{pmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ 0.3&0&0\\ 0&0&40\end{pmatrix} = (0\cdot40 - 0\cdot0)\mathbf{i} - (0.3\cdot40 - 0)\mathbf{j} + 0\,\mathbf{k} = (0, -12, 0)\ \text{N·m}.$$

Magnitude $12\ \text{N·m}$, directed along $-\mathbf{j}$ — the axis the bolt turns about. Note that if you pushed *along* the spanner ($\mathbf{F}\parallel\mathbf{r}$), the cross product would vanish: pushing toward the pivot produces no turning, exactly as the $\sin\theta$ factor predicts.

## Common Misconceptions (Teaching Notes)

### 1. Reporting a scalar for the cross product

Students fresh from the dot product write "$\mathbf{a}\times\mathbf{b} = 10$." **The output of a cross product is a vector.** A bare number is the wrong *type* of object.

**Fix.** Drill the type signature side by side: *dot eats two vectors → number; cross eats two vectors → vector.* If your cross-product answer isn't a vector, you've made an error before you finished.

### 2. Forgetting anticommutativity (the sign)

Computing $\mathbf{b}\times\mathbf{a}$ when the question asked for $\mathbf{a}\times\mathbf{b}$, and not flipping the sign — or losing the middle-term minus in the determinant.

**Fix.** Always expand in the fixed row order ($\mathbf{a}$ above $\mathbf{b}$ in the determinant) so the layout enforces the right order, and write the $+,-,+$ signs *before* filling in the $2\times2$ minors. If the question's order is reversed, negate the whole vector at the end.

### 3. Treating the cross product as associative

Writing $\mathbf{a}\times\mathbf{b}\times\mathbf{c}$ as if the brackets don't matter. They do: $\mathbf{a}\times(\mathbf{b}\times\mathbf{c})\neq(\mathbf{a}\times\mathbf{b})\times\mathbf{c}$ in general.

**Fix.** Never write a triple cross without brackets. If you need to evaluate one, use the BAC-CAB expansion, which makes the bracketing explicit.

### 4. Mixing up $\sin$ and $\cos$

Using $|\mathbf{a}||\mathbf{b}|\cos\theta$ for the cross-product magnitude (that's the dot product), or $\cos\theta$ when extracting an angle from a cross product.

**Fix.** Anchor on the *peaks*: the cross product is largest when the vectors are perpendicular (a $90°$ corner spans the biggest parallelogram), and **zero when parallel** (a squashed-flat parallelogram has no area). "Biggest at $90°$" $\Rightarrow \sin$. The dot product is the opposite — biggest when aligned $\Rightarrow \cos$.

### 5. Thinking the cross product works in 2D or higher dimensions

Trying to cross two 2D vectors and expecting a 2D vector back, or crossing two vectors in $\mathbb{R}^4$.

**Fix.** The genuine vector cross product is a 3D-only operation (the magnitude/perpendicular definition only pins down a unique vector in three dimensions). In 2D, embed into the $z=0$ plane and read off the scalar $a_1b_2 - a_2b_1$. In higher dimensions, the right generalisation is the *wedge product* (Beyond Syllabus), not a vector.

## Exam Notes

> The cross product is **not** on Cambridge 9709 (the plain A-Level Mathematics route — Papers 1–6). It is a *Further* and *IB HL* topic. Treat it as enrichment for a strong 9709 student and as core material for the courses below.

### A-Level Further (Cambridge 9231)

**Syllabus ref:** Further Pure Mathematics 1 (Paper 1), Vectors. Examinable content: the vector product $\mathbf{a}\times\mathbf{b}$, its magnitude as area, the **scalar triple product** for volume and coplanarity, normals to planes, the line of intersection of two planes, and the **common perpendicular / shortest distance between two skew lines** (where the cross product does the heavy lifting). Typical question: "find the area of triangle $ABC$" (3–4 marks) or "find the shortest distance between the skew lines $\ell_1, \ell_2$" (5–6 marks, set up $\mathbf{d}_1\times\mathbf{d}_2$ then project the connecting vector onto it).

### IB AA HL

**Topic AHL 3.16 — Vector product.** Definition of $\mathbf{v}\times\mathbf{w}$, its properties, and the geometric interpretation $|\mathbf{v}\times\mathbf{w}|$ as area. Paired with **AHL 3.17** (equations of planes, intersections, angles between planes and lines). Vectors-and-planes is the single longest chapter in AA HL and appears on every Paper 1 and Paper 2. The formula booklet gives the component formula and the area-of-triangle result; the right-hand rule and the proofs are expected to be understood, not looked up.

> **AA SL does not cover the cross product** — vectors are an HL-only topic in Analysis and Approaches.

### A-Level Further (Edexcel / AQA / OCR)

The vector product sits in **Further Pure** content across all UK boards (Edexcel places it in Further Pure 1 / Core Pure; the legacy FP3 module is the older home). Same content as 9231: vector product, scalar triple product, planes, skew-line distance.

### AP

**Not on AP Calculus AB or BC** (vectors barely feature on AP Calc, and the cross product not at all). It *does* appear constantly in **AP Physics** as applied machinery — torque ($\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}$, AP Physics 1 & C-Mechanics), angular momentum ($\mathbf{L}=\mathbf{r}\times\mathbf{p}$), and the magnetic force ($\mathbf{F}=q\mathbf{v}\times\mathbf{B}$, AP Physics 2 & C-E&M) — though AP Physics usually asks for magnitudes and right-hand-rule directions rather than full component cross products.

### Beyond high school — University

The cross product is a first-week tool in **multivariable calculus** (normals, surface area, the curl $\nabla\times\mathbf{F}$), **classical mechanics** (rotational dynamics, the entire angular-momentum story), **electromagnetism** (the Lorentz force, Poynting vector $\mathbf{E}\times\mathbf{B}$), and **computer graphics** (surface normals for lighting, exactly the dot-product lighting model's partner). It is also the entry point to **exterior algebra** and **Lie algebras** — see Beyond Syllabus.

## Connections

- **Parent / sibling:** [[3D Vectors and the Scalar Product]] — the dot product is the cosine half of vector multiplication; the cross product is the sine half. This card is the companion that completes the pair, and the dot card's "Beyond Syllabus" already previews it.
- **Sibling:** [[Vector Equations of Lines]] — the third member of the 3D-geometry trilogy; the shortest distance between skew lines uses $\mathbf{d}_1\times\mathbf{d}_2$.
- **Extension:** [[Planes in 3D]] — building a plane's normal from two in-plane vectors is the canonical cross-product application; the scalar triple product gives the line of intersection.
- **Proof ingredient:** [[Trigonometric Ratios]] — the $\sin\theta$ in the magnitude, and the Pythagorean identity $\sin^2+\cos^2=1$ that links cross to dot.
- **Application — physics:** [[Forces and Equilibrium]] — its "Moments / Torques" section is the 2D moment of a force; the cross product $\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}$ is the full 3D generalisation. [[Vectors in Physics]] catalogues torque and the other vector quantities.
- **Physics bridge:** [[Torque]] and [[Angular Momentum]] — the rotational-dynamics cards where $\mathbf{r}\times\mathbf{F}$ and $\mathbf{r}\times\mathbf{p}$ become the central objects.
- **Physics bridge — electromagnetism:** [[Lorentz Force]] — the magnetic force $\mathbf{F}=q\mathbf{v}\times\mathbf{B}$ is a cross product, and [[Maxwell's Equations]] — two of the four are built on the curl $\nabla\times$. This is where the cross product's right-handedness becomes the right-hand rule of every physics classroom.
- **Historical sibling:** [[Stories/The Argument for i]] — Hamilton's 1843 quaternions are where the cross product was *born*: the vector part of multiplying two pure quaternions *is* the cross product, and $\mathbf{i}\times\mathbf{j}=\mathbf{k}$ mirrors his $ij=k$.
- **For 9231 students:** [[MF19 Reference (9231)]] — and the answer is sharp: the **scalar** product is printed in MF19's Pure pages, the **vector** product appears nowhere in the booklet at all. Everything on this page is memorise-and-derive.

---

## Beyond Syllabus

### Where the cross product came from — Hamilton's quaternions

**Nobody set out to invent the cross product.** It was a by-product of a different quest. Complex numbers multiply *2D* rotations beautifully (multiply the moduli, add the arguments), so through the 1830s mathematicians asked the obvious sequel: *is there a number system that multiplies points in 3D?* William Rowan Hamilton hunted for it for over a decade — his children reportedly asked him at breakfast, *"Papa, can you multiply triples yet?"* The answer turned out to be no: you cannot do it in three dimensions. On 16 October 1843 Hamilton realised you have to jump to **four**, and invented the **quaternions** $\mathbb{H}$, numbers $w + x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$ with $\mathbf{i}^2=\mathbf{j}^2=\mathbf{k}^2=\mathbf{ijk}=-1$. (The full story — and why he carved that rule into Brougham Bridge with a pocket-knife — is in [[Stories/The Argument for i]] §Act IV.)

The cross product fell out of the wreckage. Take two *pure* quaternions (no real part) $\mathbf{p}=(a_1,a_2,a_3)$ and $\mathbf{q}=(b_1,b_2,b_3)$ and multiply them as quaternions; the answer splits perfectly into a scalar piece and a vector piece:

$$\mathbf{p}\,\mathbf{q} = \underbrace{-\,\mathbf{p}\cdot\mathbf{q}}_{\text{scalar part}} \;+\; \underbrace{\mathbf{p}\times\mathbf{q}}_{\text{vector part}}.$$

**The dot product and the cross product are the two halves of one quaternion multiplication.** This answers "which came first, dot or cross?" — *neither.* They were born together, as the scalar and vector parts of a single product. Hamilton's rule $\mathbf{ij}=\mathbf{k}$ is literally the basis rule $\mathbf{i}\times\mathbf{j}=\mathbf{k}$, and the non-commutativity $\mathbf{ij}=-\mathbf{ji}$ is exactly the cross product's anticommutativity.

In the **1880s**, Josiah Willard Gibbs (at Yale) and Oliver Heaviside (in England), working independently, found the full quaternion machinery clumsy for physics and surgically *split* it into the two standalone operations we teach today — the dot product $\mathbf{a}\cdot\mathbf{b}$ and the cross product $\mathbf{a}\times\mathbf{b}$ (Grassmann's 1844 exterior algebra was the parallel ancestor Gibbs credited). The payoff was immediate: Heaviside used this new vector calculus to compress Maxwell's original **twenty** equations of electromagnetism into the **four** we use now. That is also where $\mathbf{F}=q\mathbf{v}\times\mathbf{B}$ got its modern shape.

> [!tip] The right-hand rule comes *before* the E&M hand-rules
> A common question: in electromagnetism, does the right-hand rule come from the physics or the maths? **The maths.** The cross product is right-handed purely because Hamilton chose $\mathbf{i}, \mathbf{j}, \mathbf{k}$ to cycle right-handedly ($\mathbf{i}\times\mathbf{j}=\mathbf{k}$, not $-\mathbf{k}$). E&M then *inherited* that handedness when Gibbs and Heaviside wrote the force laws as cross products. Fleming's left-hand and right-hand rules (1890s) are classroom mnemonics layered on top — the left-hand rule just bookkeeps the sign convention for the direction of conventional current in a motor. Underneath both is one orientation choice made in 1843, for reasons that had nothing to do with electricity.

### Why only 3D (and the 7D oddity)

A vector cross product needs the spanned plane to have a *unique* perpendicular direction — true in $\mathbb{R}^3$, false in $\mathbb{R}^2$ (no room) and $\mathbb{R}^4$ and up (too much room — infinitely many perpendiculars). A deep theorem (related to Hurwitz's classification of division algebras, the same result that caps Hamilton's tower at the octonions $\mathbb{O}$) shows a genuine vector cross product exists in **exactly two dimensions: 3 and 7**. The 7D cross product comes from the octonions, just as the 3D one comes from the quaternions. Everywhere else, the honest generalisation is below.

### The wedge product — the cross product done right

In higher dimensions the orientation-and-area content of $\mathbf{a}\times\mathbf{b}$ is carried by the **wedge product** $\mathbf{a}\wedge\mathbf{b}$, an element of *exterior algebra* called a **bivector** — an oriented patch of area that does *not* pretend to be a vector. In 3D there's a coincidence: a plane and its normal line are interchangeable (each is the perpendicular complement of the other), and the **Hodge star** $\star(\mathbf{a}\wedge\mathbf{b}) = \mathbf{a}\times\mathbf{b}$ converts the bivector into the familiar normal vector. This is *why* the cross product seems to behave like a vector but flips sign under reflections in a way ordinary vectors don't — it is secretly a bivector wearing a vector costume, a so-called **pseudovector**. Torque and angular momentum are pseudovectors for exactly this reason.

### Curl and angular velocity

Two of physics' most important cross products:

- **Angular velocity:** a rigid body spinning with angular velocity $\boldsymbol{\omega}$ gives every point velocity $\mathbf{v} = \boldsymbol{\omega}\times\mathbf{r}$ — the cross product converts "rate of turning" into "actual speed at radius $\mathbf{r}$."
- **Curl:** the vector operator $\nabla\times\mathbf{F}$ measures the local rotation (circulation per unit area) of a vector field, and is the star of two of Maxwell's four equations. It is a cross product with the gradient operator standing in for one of the vectors.

> [!info] Electromagnetism bridge
> The cross product is load-bearing in electromagnetism. The magnetic force on a moving charge, $\mathbf{F}=q\mathbf{v}\times\mathbf{B}$, is the [[Lorentz Force]] — a pure cross product, and the original reason Gibbs and Heaviside needed this notation. Two of [[Maxwell's Equations]] (Faraday's law and Ampère's law) are statements about the curl $\nabla\times\mathbf{E}$ and $\nabla\times\mathbf{B}$. The right-hand rule you meet in every magnetism lesson is just this card's orientation convention, inherited intact.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{a}\times\mathbf{b}$ | `\mathbf{a}\times\mathbf{b}` | Cross / vector product |
| $\mathbf{a}\cdot\mathbf{b}$ | `\mathbf{a}\cdot\mathbf{b}` | Dot product (for contrast) |
| $\theta$ | `\theta` | Angle between the vectors, $0\le\theta\le\pi$ |
| $\det\!\begin{pmatrix}\cdots\end{pmatrix}$ | `\det\!\begin{pmatrix}...\end{pmatrix}` | Determinant mnemonic |
| $\begin{vmatrix}p&q\\ r&s\end{vmatrix}$ | `\begin{vmatrix}p&q\\ r&s\end{vmatrix}` | $2\times2$ determinant $ps-qr$ |
| $\boldsymbol{\tau}$ | `\boldsymbol{\tau}` | Torque vector |
| $\boldsymbol{\omega}$ | `\boldsymbol{\omega}` | Angular velocity vector |
| $\nabla\times\mathbf{F}$ | `\nabla\times\mathbf{F}` | Curl of a vector field |
| $\mathbf{a}\wedge\mathbf{b}$ | `\mathbf{a}\wedge\mathbf{b}` | Wedge product (bivector) |
| $\star$ | `\star` | Hodge star |
| $\mathbb{H}$ | `\mathbb{H}` | Quaternions |
