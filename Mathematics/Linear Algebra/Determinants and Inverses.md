---
chinese: 行列式与逆矩阵 (hánglièshì yǔ nì jǔzhèn)
prerequisites:
  - "[[Matrix]]"
  - "[[Identity Matrix]]"
  - "[[Matrix Transformations]]"
leads_to:
  - "[[Invariant Points and Lines]]"
  - "[[Eigenvalues and Eigenvectors]]"
  - "[[Linear Systems in 3D]]"
tags:
  - subject/mathematics
  - domain/matrices
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/IB-AI
  - curriculum/AP
  - syllabus/9231-1-4
  - type/definition
  - type/proof
  - notation/determinant
  - notation/inverse-matrix
  - misconception/det-not-additive
  - misconception/det-scalar-multiple
  - misconception/inverse-product-order
  - misconception/adjugate-transpose
---

# Determinants and Inverses 行列式与逆矩阵

> *A matrix is a machine that moves the plane. Two questions matter about any machine: **how much does it distort what it touches**, and **can what it did be undone**? Remarkably, a single number answers both. That number is the determinant — and the whole of this topic is learning to read it.*

## Definition

### Formal

For a $2 \times 2$ matrix $\mathbf{M} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the **determinant** is

$$\det \mathbf{M} = ad - bc.$$

A square matrix is **singular** if $\det \mathbf{M} = 0$ and **non-singular** if $\det \mathbf{M} \neq 0$.

The **inverse** of a square matrix $\mathbf{M}$, written $\mathbf{M}^{-1}$, is the matrix satisfying

$$\mathbf{M}\mathbf{M}^{-1} = \mathbf{M}^{-1}\mathbf{M} = \mathbf{I}.$$

A matrix has an inverse **if and only if it is non-singular** — and the sections below show why those two conditions are the same fact.

### Intuitive

Recall from [[Matrix Transformations]] that a $2\times2$ matrix moves every point of the plane, and that its columns are the images of the two basis vectors $(1,0)$ and $(0,1)$. So the matrix sends the unit square to the parallelogram spanned by its columns.

- The **determinant is the area of that parallelogram, with a sign**: how much the machine scales area, and whether it flips the plane over while doing so.
- The **inverse is the undo button**: the matrix that moves every point back where it came from.

The two meet at zero. If $\det \mathbf{M} = 0$, the unit square is crushed to a segment — the whole plane lands on a single line. Two different points now share one image, so "where did this point come from?" has no unique answer, and no undo machine can exist. **A matrix is invertible exactly when it doesn't destroy information**, and the determinant is the number that reports whether it did.

(If you are reaching for paper to draw the parallelogram — good instinct, and you can hold off: it is drawn out step by step two sections down, in *The 2×2 determinant — area with a memory*, together with what "flipped over" and "crushed" look like.)

### 中文锚点 (Chinese Anchor)

这一对名字，中英文各讲了故事的一半：

- **行列式** 的字面意思是"由**行**与**列**构成的式子" —— 中文名告诉你它是**怎么算出来**的（把行和列的元素按规则乘起来加减）。
- 英文 **determinant** 来自 *determine*（决定）—— 英文名告诉你它是**干什么用**的：这个数**决定**矩阵是否可逆（determinant *determines* invertibility）。

两个名字合在一起，才是完整的概念：按行列算出一个数，这个数决定矩阵的命运。

**逆矩阵** 的"逆"与逆运算的"逆"同源：$\mathbf{M}^{-1}$ 之于 $\mathbf{M}$，如同 $\div 3$ 之于 $\times 3$ —— 撤销上一步。**奇异矩阵**（singular）即 $\det = 0$、不可逆的矩阵。

中国教材里 $3\times3$ 行列式常用**对角线法则**（Sarrus 法则：三条主对角线相加、三条副对角线相减）。它只对 $3\times3$ 成立，$4\times4$ 以上完全失效；下文的**余子式展开**（cofactor expansion）才是对任何阶数都成立的原理。法则是技巧，展开是原理——技巧失效时退回原理。

三个配套术语，下文逐一登场：**余子式**（minor，划掉一行一列后剩下的行列式）、**代数余子式**（cofactor，余子式带上棋盘格正负号）、**伴随矩阵**（adjugate，代数余子式矩阵的转置）。

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Determinant (operator) | $\det \mathbf{M}$ | "det M" | The 9231 syllabus states this notation is used |
| Determinant (bars) | $\lvert \mathbf{M} \rvert$, $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ | "det M" | Bars around the array replace the brackets |
| Inverse | $\mathbf{M}^{-1}$ | "M inverse" | Defined by $\mathbf{M}\mathbf{M}^{-1} = \mathbf{I}$ |
| Adjugate | $\operatorname{adj} \mathbf{M}$ | "adjugate of M" | The matrix with $\mathbf{M}\operatorname{adj}\mathbf{M} = (\det\mathbf{M})\mathbf{I}$ — swap-and-negate for 2×2, the transposed cofactors for 3×3 |
| Minor, cofactor | $M_{ij}$, $C_{ij}$ | "the minor / cofactor of entry $i,j$" | $C_{ij} = (-1)^{i+j} M_{ij}$ — defined in the 3×3 sections below |
| Identity | $\mathbf{I}$ | "the identity" | Also stated by the syllabus; see [[Identity Matrix]] |

> [!warning] Notation trap — the bars are not absolute value
> $\lvert \mathbf{M} \rvert$ **can be negative**, and the sign carries real information (the transformation flips the plane over). Students trained on $\lvert x \rvert \geq 0$ discard the sign by reflex — resist it. When a question needs a genuinely non-negative quantity (an area), it will wrap the determinant in true absolute-value bars: area factor $= \lvert \det \mathbf{M} \rvert$.
>
> And there is **no such thing as matrix division**: never write $\frac{\mathbf{A}}{\mathbf{B}}$. It fails to say which of $\mathbf{B}^{-1}\mathbf{A}$ and $\mathbf{A}\mathbf{B}^{-1}$ you mean — and because matrix multiplication is not commutative, those are different matrices.

## Where matrices came from — the array before the name, the number before the array

A matrix can feel like a tool that arrived from nowhere: a grid of numbers with a strange multiplication rule which then, suspiciously, turns out to run the whole of physics and computing. The feeling is an artefact of **teaching order**. Historically everything arrived in the reverse sequence, and every piece was the answer to a question someone was already asking.

- **The array came first, and had no name.** 《九章算术》(*The Nine Chapters on the Mathematical Art*, compiled by the first century AD) devotes its eighth chapter, 方程, to simultaneous linear equations: the coefficients are laid out as a rectangular array of counting rods and eliminated column by column — the method the West would rediscover as Gaussian elimination some 1,700 years later. The matrix as a *thing to compute with* is that old; the word is not.
- **The number came next — from asking whether equations have an answer.** Seki Takakazu in Japan (1683) and Leibniz in Europe (1693) found, independently, that one number computed from the coefficients decides whether a system of linear equations has a unique solution. That number is the determinant, born as a *test for solvability* — which is exactly the singular/non-singular test of this card, in different clothes. Cramer (1750) wrote the solutions themselves as ratios of determinants; Cauchy (1812) systematised the theory and proved that determinants multiply, $\det(\mathbf{AB}) = \det\mathbf{A}\,\det\mathbf{B}$.
- **The name came last.** Sylvester coined *matrix* in 1850 — Latin for *womb* — for the array out of which all those determinants are born (every minor is the determinant of a piece of it). Eight years later Cayley's *A Memoir on the Theory of Matrices* gave the array its algebra: addition, the inverse, and multiplication — which he did not so much invent as *transcribe*. Substitute one linear change of variables into another and the coefficients that fall out are exactly row-times-column, in exactly the order that makes $\mathbf{AB}$ mean "$\mathbf{B}$ first, then $\mathbf{A}$". The rule that feels arbitrary is the only rule that composes transformations correctly.
- **Then seventy years of obscurity, and two explosions.** Matrix algebra stayed a specialist's tool until 1925, when Heisenberg wrote quantum mechanics as arrays of numbers obeying a strange non-commutative multiplication — and Max Born recognised the strange multiplication as the matrix product he had learned as a student. Heisenberg had never heard of a matrix; the theory was named *matrix mechanics* anyway. Then the computer: Turing's 1948 paper on rounding errors in matrix processes made large-scale elimination trustworthy on a machine, and from there matrices became the native language of computer graphics (every rotation on your screen), of the web (Google's original PageRank is an eigenvector of a matrix with a row for every page), and of AI (a neural-network layer *is* a matrix multiplication; a GPU is a matrix-multiplying engine).

So the honest order is **question → number → array → algebra → applications**. The card keeps to it: the determinant is read as the answer to *does this transformation destroy information?* before it is drilled as a formula, and the multiplication rule is treated as what composition of transformations forces, not as a convention to memorise.

## The 2×2 determinant — area with a memory

Why is the area of the parallelogram $ad - bc$? Put the column vectors $(a, c)$ and $(b, d)$ in a bounding rectangle and subtract everything that isn't parallelogram:

![[determinant-area-derivation.svg|760]]

The bounding rectangle has area $(a+b)(c+d)$. Peeling away two rectangles ($bc$ each) and four triangles (pairing into $ac$ and $bd$) leaves

$$(a+b)(c+d) - 2bc - ac - bd = ad - bc.$$

So $\det \mathbf{M}$ is the area of the image of the unit square — and since every region of the plane is (in the limit) a mosaic of tiny squares, **every** area gets scaled by the same factor. One number, the whole plane's distortion.

**The sign is the memory.** Walk the unit square anticlockwise: $O \to (1,0) \to (1,1) \to (0,1)$. If the image parallelogram is still walked anticlockwise, $\det > 0$; if the walk now runs clockwise, the transformation has flipped the plane over and $\det < 0$. Reflections do exactly this — a mirror image is walked the other way round.

![[determinant-sign-and-collapse.svg|920]]

Reading the standard transformations through their determinants:

| Transformation | Matrix | $\det$ | What the number says |
|---|---|---|---|
| Rotation by $\theta$ | $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ | $\cos^2\theta + \sin^2\theta = 1$ | areas kept, no flip |
| Reflection in $y = x$ | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | $-1$ | areas kept, plane flipped |
| Enlargement, factor $k$ | $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ | $k^2$ | lengths scale by $k$, areas by $k^2$ |
| Stretch, factor $k$, parallel to $x$-axis | $\begin{pmatrix} k & 0 \\ 0 & 1 \end{pmatrix}$ | $k$ | one direction scaled, the other kept |
| Shear ($x$-axis fixed) | $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ | $1$ | everything moves, area doesn't — the surprise of the family |

**Watch it happen by hand — take $\theta = \tfrac{\pi}{2}$.** The rotation matrix becomes $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and $\det = 0 \cdot 0 - (-1)(1) = 1$. Now push the unit square through it, corner by corner: $(1,0) \to (0,1)$, $\ (1,1) \to (-1,1)$, $\ (0,1) \to (-1,0)$. The image is a unit square standing in the second quadrant — area $1$, as the determinant said — and walking its corners in the order the originals were walked, $O \to (0,1) \to (-1,1) \to (-1,0)$, still runs **anticlockwise**. No flip; $\det > 0$. ✓

Do the same to the reflection in $y = x$, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$: $(1,0) \to (0,1)$, $\ (1,1) \to (1,1)$, $\ (0,1) \to (1,0)$. The image is the *same* unit square, area $1$ — but its corners are now walked $O \to (0,1) \to (1,1) \to (1,0)$, which is **clockwise**. The plane has been turned over, and $\det = 0 \cdot 0 - 1 \cdot 1 = -1$ reports it. Two computations, both by hand, and both readings of the determinant — the size and the sign — confirmed against a picture you can draw in ten seconds.

**Determinants multiply.** Applying $\mathbf{B}$ then $\mathbf{A}$ scales area by $\det \mathbf{B}$, then by $\det \mathbf{A}$ — scale factors compose by multiplying, so

$$\det(\mathbf{A}\mathbf{B}) = \det \mathbf{A} \cdot \det \mathbf{B}.$$

Two consequences fall out at once: $\det(\mathbf{A}^{-1}) = \dfrac{1}{\det \mathbf{A}}$ (undoing a scaling by $k$ is scaling by $1/k$ — and it is also why a singular matrix can have no inverse: nothing multiplies $0$ back to $1$), and a product $\mathbf{A}\mathbf{B}$ is non-singular exactly when both factors are.

## The 2×2 inverse — derived, then packaged

We want $\mathbf{M}^{-1}$ with $\mathbf{M}\mathbf{M}^{-1} = \mathbf{I}$. Rather than guess it, set the goal precisely. A product whose **off-diagonal entries are zero** and whose **diagonal entries are equal** is a multiple of $\mathbf{I}$ — and a multiple of $\mathbf{I}$ is one division away from $\mathbf{I}$ itself. So the hunt is: *kill the off-diagonals, then hope the diagonals agree.*

Try an unknown $\begin{pmatrix} p & q \\ r & s \end{pmatrix}$ and multiply:

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} p & q \\ r & s \end{pmatrix} = \begin{pmatrix} ap + br & aq + bs \\ cp + dr & cq + ds \end{pmatrix}.$$

- The top-right must vanish: $aq + bs = 0$. The cheapest choice is $q = -b,\ s = a$, since then $aq + bs = -ab + ab = 0$.
- The bottom-left must vanish: $cp + dr = 0$. Same trick: $p = d,\ r = -c$ gives $cd - cd = 0$.

That fixes all four unknowns — the diagonal of $\mathbf{M}$ **swapped**, the off-diagonal **negated** — and the two diagonal entries come out as $ap + br = ad - bc$ and $cq + ds = -bc + ad$. **They agree.** Both are $\det \mathbf{M}$, so the product is $(ad - bc)\,\mathbf{I}$, and one division finishes it:

$$\boxed{\ \mathbf{M}^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}, \qquad ad - bc \neq 0.\ }$$

So swap-and-negate is *discovered*, not remembered: it is simply the cheapest way to make both off-diagonals cancel, and the agreement of the two diagonal entries is what makes the leftover a scalar. (That agreement is not luck. The reason is in the adjugate callout of the $3\times3$ section below, and it holds at every size.) The companion matrix $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ has a name — the **adjugate** of $\mathbf{M}$, written $\operatorname{adj}\mathbf{M}$ — and its defining property is exactly what was just verified:

$$\mathbf{M}\,\operatorname{adj}\mathbf{M} = (\det \mathbf{M})\,\mathbf{I}.$$

When the recipe feels arbitrary, fall back on the goal: the adjugate undoes $\mathbf{M}$'s mixing but overshoots every area by a factor of $\det \mathbf{M}$; the division rescales.

**Checking habit:** an inverse is self-checking — multiply back and confirm $\mathbf{I}$. Ten seconds, catches nearly every slip.

## The 3×3 determinant — cofactor expansion

For a $3 \times 3$ matrix, pick any row (or column). Each entry in it gets multiplied by its **minor** — the $2\times2$ determinant left when you delete that entry's row and column — and the products are combined with alternating signs from the checkerboard

$$\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}.$$

Expanding along the top row:

$$\det \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = a \begin{vmatrix} e & f \\ h & i \end{vmatrix} - b \begin{vmatrix} d & f \\ g & i \end{vmatrix} + c \begin{vmatrix} d & e \\ g & h \end{vmatrix}.$$

A minor with its checkerboard sign attached is called a **cofactor**: $C_{ij} = (-1)^{i+j} M_{ij}$, where $M_{ij}$ is the minor of the entry in row $i$, column $j$.

**Any row, any column.** The same recipe runs along the middle row $(d, e, f)$, the bottom row $(g, h, i)$, or *down* any column — $(a, d, g)$ down the first, $(b, e, h)$ the second, $(c, f, i)$ the third. Six routes, and **every one gives the same number**. That is a theorem (Laplace's expansion, proved in first-year linear algebra), not a coincidence — verify it once on the worked matrix below and then trust it. The only thing that changes between routes is the signs, and they always come off the checkerboard, so the middle row and the middle column each *start with a minus*:

$$\det = -d \begin{vmatrix} b & c \\ h & i \end{vmatrix} + e \begin{vmatrix} a & c \\ g & i \end{vmatrix} - f \begin{vmatrix} a & b \\ g & h \end{vmatrix} \qquad \text{(along the middle row)}.$$

And yes — the whole point of having a choice is **zeros**. Each zero entry deletes an entire $2\times2$ computation, so you *pick* the row or column that already carries the most of them. (You can also *manufacture* zeros — adding a multiple of one row to another leaves the determinant unchanged, which is how computers do it — but that is a university technique; at this level, choose well and expand.)

This is the same expansion, sign pattern and all, that computes a [[Cross Product]] — the $\mathbf{i}, \mathbf{j}, \mathbf{k}$ top-row layout there is a $3\times3$ determinant being expanded along its first row.

The meaning survives the climb in dimension: a $3\times3$ matrix sends the unit cube to a parallelepiped, and $\lvert \det \mathbf{M} \rvert$ is its **volume** — the volume scale factor of the transformation, with the sign now recording handedness (whether a right-handed set of axes stays right-handed). Sanity-check on a diagonal matrix: $\operatorname{diag}(2, 3, 5)$ stretches the axes by $2, 3, 5$, and its determinant is $30$, the volume of the box. [[Cross Product]] §"scalar triple product" is the same fact wearing vector clothing: $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$ *is* the $3\times3$ determinant with rows $\mathbf{a}, \mathbf{b}, \mathbf{c}$.

> [!info] Beyond syllabus — what a determinant really is
> The pattern continues: an $n \times n$ determinant is the (signed) $n$-dimensional volume scale factor, and cofactor expansion works at every size. In fact one can *define* the determinant abstractly as the only function of a matrix's columns that is linear in each column, flips sign when two columns swap, and gives $\mathbf{I}$ the value $1$ — three properties any honest "signed volume" must have, and they pin the formula down uniquely. That derivation is first-year university linear algebra; everything on this card is the $2$- and $3$-dimensional shadow of it.

## The 3×3 inverse — minors, cofactors, adjugate

Recall that the $2\times2$ inverse was $\mathbf{M}^{-1} = \dfrac{1}{\det\mathbf{M}}\operatorname{adj}\mathbf{M}$, with the adjugate the swap-and-negate companion satisfying $\mathbf{M}\operatorname{adj}\mathbf{M} = (\det\mathbf{M})\mathbf{I}$. **The same formula holds for $3\times3$.** The only thing that changes is how the adjugate is *built*, because "swap and negate" is a $2\times2$ shortcut for something more general. Three named objects, one per step:

- The **minor** $M_{ij}$ of the entry in row $i$, column $j$ is the $2\times2$ determinant left when you delete row $i$ and column $j$ (余子式).
- The **cofactor** $C_{ij} = (-1)^{i+j} M_{ij}$ is the minor with its checkerboard sign attached (代数余子式).
- The **adjugate** $\operatorname{adj}\mathbf{A}$ is the matrix of cofactors, **transposed**: entry $(i, j)$ of $\operatorname{adj}\mathbf{A}$ is $C_{ji}$ (伴随矩阵; older books call it the *classical adjoint*).

Then, for non-singular $\mathbf{A}$:

$$\boxed{\ \mathbf{A}^{-1} = \frac{1}{\det \mathbf{A}}\operatorname{adj}\mathbf{A}.\ }$$

**Check that this really is the $2\times2$ rule in disguise.** For $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ the "minor" of an entry is the single number left when its row and column are deleted: $M_{11} = d$, $M_{12} = c$, $M_{21} = b$, $M_{22} = a$. Attach the checkerboard signs — $C_{11} = d$, $C_{12} = -c$, $C_{21} = -b$, $C_{22} = a$ — and transpose: $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$. Swap-and-negate was the adjugate all along.

> [!info] Why the transpose — the adjugate is a cofactor expansion in disguise
> Multiply row $i$ of $\mathbf{A}$ against column $j$ of $\operatorname{adj}\mathbf{A}$. Because of the transpose, column $j$ of the adjugate holds the cofactors of **row $j$** of $\mathbf{A}$, so the product is $\sum_k a_{ik} C_{jk}$: the entries of row $i$ paired with the cofactors of row $j$.
>
> - If $i = j$, that is precisely the cofactor expansion of $\det \mathbf{A}$ along row $i$. Every diagonal entry of $\mathbf{A}\operatorname{adj}\mathbf{A}$ equals $\det\mathbf{A}$ — which is why the $2\times2$ diagonal entries "happened" to agree.
> - If $i \neq j$, it is the cofactor expansion along row $j$ of the matrix you get by **replacing row $j$ with a copy of row $i$** — a matrix with two identical rows. Such a determinant is $0$: swapping the two identical rows must flip its sign, yet changes nothing, and the only number equal to its own negative is $0$. Every off-diagonal entry vanishes.
>
> Hence $\mathbf{A}\operatorname{adj}\mathbf{A} = (\det\mathbf{A})\mathbf{I}$ at every size — the transpose is exactly what lines the right cofactors up against the right row.

The full computation is Worked Example 1 below — nine minors, every one shown. It is honest work, not deep work: the danger is never the idea, always one sign slip among nine. Which is why an unofficial last step exists: **multiply one row back** against $\mathbf{A}$ and check you get a row of $\mathbf{I}$.

## Undoing a sequence — $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$

**The principle first: to undo a sequence of actions, undo the *last* action first.** Socks then shoes is undone by shoes-off then socks-off. Since $\mathbf{A}\mathbf{B}$ means "$\mathbf{B}$ first, then $\mathbf{A}$" ([[Combination of Transformations]]), the undo must peel $\mathbf{A}$ off first:

$$(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1}) = \mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1} = \mathbf{A}\,\mathbf{I}\,\mathbf{A}^{-1} = \mathbf{I}. \qquad \blacksquare$$

One line, powered entirely by associativity — the brackets may regroup, as long as the order never changes. The result extends to any length, reversing the whole queue:

$$(\mathbf{A}\mathbf{B}\mathbf{C})^{-1} = \mathbf{C}^{-1}\mathbf{B}^{-1}\mathbf{A}^{-1},$$

and the syllabus notes explicitly that products of more than two matrices may be required.

## Worked Examples

### Example 1 (the full 3×3 ritual): invert $\mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$

*Tool: the determinant first — no det, no inverse, and the zeros pick the expansion route.*

Column 1 has a zero, so expand down column 1 (checkerboard signs $+, -, +$):

$$\det \mathbf{A} = 1\begin{vmatrix} 1 & 4 \\ 6 & 0 \end{vmatrix} - 0 + 5\begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix} = 1(0 - 24) + 5(8 - 3) = -24 + 25 = 1.$$

Non-singular — and with $\det \mathbf{A} = 1$, the inverse will be the adjugate itself, no division needed.

*Cross-check: any row, any column.* Along the top row instead: $1\begin{vmatrix} 1 & 4 \\ 6 & 0 \end{vmatrix} - 2\begin{vmatrix} 0 & 4 \\ 5 & 0 \end{vmatrix} + 3\begin{vmatrix} 0 & 1 \\ 5 & 6 \end{vmatrix} = 1(-24) - 2(-20) + 3(-5) = -24 + 40 - 15 = 1$. Same number by a different route — as the theorem promised, and a free check on the arithmetic.

*Tool: minors → cofactors → transpose.* A minor is what survives when you strike out one row and one column. Three of the nine, drawn:

![[determinant-minors-crossout.svg|920]]

All nine, each written as the $2\times2$ determinant that survives the strike-out — entry $(i, j)$ of this grid deletes row $i$ and column $j$ of $\mathbf{A}$:

$$\text{minors} = \begin{pmatrix} \begin{vmatrix} 1 & 4 \\ 6 & 0 \end{vmatrix} & \begin{vmatrix} 0 & 4 \\ 5 & 0 \end{vmatrix} & \begin{vmatrix} 0 & 1 \\ 5 & 6 \end{vmatrix} \\[8pt] \begin{vmatrix} 2 & 3 \\ 6 & 0 \end{vmatrix} & \begin{vmatrix} 1 & 3 \\ 5 & 0 \end{vmatrix} & \begin{vmatrix} 1 & 2 \\ 5 & 6 \end{vmatrix} \\[8pt] \begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix} & \begin{vmatrix} 1 & 3 \\ 0 & 4 \end{vmatrix} & \begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix} \end{pmatrix} = \begin{pmatrix} 0-24 & 0-20 & 0-5 \\ 0-18 & 0-15 & 6-10 \\ 8-3 & 4-0 & 1-0 \end{pmatrix} = \begin{pmatrix} -24 & -20 & -5 \\ -18 & -15 & -4 \\ 5 & 4 & 1 \end{pmatrix}$$

(Read one in words to fix the habit: for the entry in row 2, column 3 — the $4$ — strike out row 2 and column 3; what remains is $\begin{pmatrix} 1 & 2 \\ 5 & 6 \end{pmatrix}$, whose determinant is $6 - 10 = -4$.)

Checkerboard signs, then transpose:

$$\text{cofactors} = \begin{pmatrix} -24 & 20 & -5 \\ 18 & -15 & 4 \\ 5 & -4 & 1 \end{pmatrix} \quad\Longrightarrow\quad \operatorname{adj} \mathbf{A} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}$$

$$\mathbf{A}^{-1} = \frac{1}{1}\operatorname{adj} \mathbf{A} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}.$$

*Tool: the self-check — one row is enough.* Row 1 of $\mathbf{A}$ against the columns of $\mathbf{A}^{-1}$:

$$(1, 2, 3) \cdot (-24, 20, -5) = -24 + 40 - 15 = 1, \quad (1,2,3)\cdot(18,-15,4) = 0, \quad (1,2,3)\cdot(5,-4,1) = 0. \checkmark$$

The first row of $\mathbf{I}$, as required.

### Example 2 (9231 style — the parameter determinant): 9231/13 June 2024 Q1

> The matrix $\mathbf{A} = \begin{pmatrix} k & 1 & 0 \\ 6 & 5 & 2 \\ -1 & 3 & -k \end{pmatrix}$, where $k$ is a real constant.
> **(a)** Show that $\mathbf{A}$ is non-singular. **[3]**
> **(b)** Given that $\mathbf{A}^{-1} = \begin{pmatrix} 3 & 0 & -1 \\ 1 & 0 & 0 \\ -\tfrac{23}{2} & \tfrac{1}{2} & 3 \end{pmatrix}$, find the value of $k$. **[2]**

**(a)** *Tool: "non-singular for all $k$" means "$\det \mathbf{A} = 0$ has no real solution" — compute the determinant and refuse it every root.* Expanding along the top row (its zero kills the third cofactor):

$$\det \mathbf{A} = k\begin{vmatrix} 5 & 2 \\ 3 & -k \end{vmatrix} - 1\begin{vmatrix} 6 & 2 \\ -1 & -k \end{vmatrix} = k(-5k - 6) - (-6k + 2) = -5k^2 - 2.$$

Since $k^2 \geq 0$, we have $\det \mathbf{A} = -5k^2 - 2 \leq -2 < 0$ for every real $k$. The determinant is never zero, so $\mathbf{A}$ is non-singular. $\blacksquare$

**(b)** Two honest routes, both two lines — knowing the cheaper one is the exam skill.

*Route 1 — Tool: one entry of $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$.* The $(1,1)$ entry of the product is row 1 of $\mathbf{A}$ times column 1 of $\mathbf{A}^{-1}$:

$$(k, 1, 0) \cdot \left(3,\, 1,\, -\tfrac{23}{2}\right) = 3k + 1 = 1 \quad\Longrightarrow\quad k = 0.$$

*Route 2 — Tool: determinants are reciprocal, $\det(\mathbf{A}^{-1}) = 1/\det \mathbf{A}$.* Expand $\det(\mathbf{A}^{-1})$ along its middle row (two zeros — one cofactor survives):

$$\det(\mathbf{A}^{-1}) = -1 \cdot \begin{vmatrix} 0 & -1 \\ \tfrac12 & 3 \end{vmatrix} = -\tfrac12 \quad\Longrightarrow\quad \det \mathbf{A} = -2 \quad\Longrightarrow\quad -5k^2 - 2 = -2 \quad\Longrightarrow\quad k = 0.$$

Both routes are on the mark scheme. Route 1 needs no cleverness; Route 2 is the reciprocal law earning its keep.

## Where the determinant meets the world

The determinant's biggest job in real computation is not solving equations — it is **answering "which side?" billions of times per second.**

- **The orientation test.** Three points $A, B, C$ in the plane: does the path $A \to B \to C$ turn left or turn right? Form the matrix whose columns are the vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ — its determinant is positive for a left turn, negative for a right turn, zero when the points are collinear. That is the sign-is-orientation fact from this card used raw, and it is the workhorse predicate of computational geometry: convex hulls, "is this point inside the polygon?", collision detection, a robot or a self-driving planner asking *which side of the boundary am I on?* — all reduce to reading the sign of a small determinant.
- **Back-face culling.** A 3D model is a mesh of triangles, and at any moment roughly half of them face away from the camera. The graphics pipeline decides which — per triangle, per frame — with an orientation determinant: projected to the screen, a triangle whose vertices wind clockwise is facing away, and is skipped before any expensive shading happens. The sign of a $2\times2$ determinant, evaluated millions of times a frame, is why your game runs at twice the speed it otherwise would.
- **An honest note about inverses.** Production numerical code almost never computes $\mathbf{A}^{-1}$ explicitly — solving $\mathbf{A}\mathbf{x} = \mathbf{b}$ by elimination is faster and more accurate than forming the inverse and multiplying. The inverse you compute by hand here is for *structure* (undoing transformations, proving identities like $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$); the determinant, by contrast, is used raw and constantly, because a sign is the cheapest answer a computer can give.

## Common Misconceptions (Teaching Notes)

### 1. "$\det(\mathbf{A} + \mathbf{B}) = \det \mathbf{A} + \det \mathbf{B}$"

False, and one matrix kills it: $\det(\mathbf{I} + \mathbf{I}) = \det(2\mathbf{I}) = 4$, but $\det \mathbf{I} + \det \mathbf{I} = 2$.

**Fix:** the determinant respects *products*, never sums — areas under two machines run in sequence multiply; areas under "add the machines" do nothing geometric at all. When tempted to distribute det over $+$, recall there is no picture for it.

### 2. "$\det(k\mathbf{A}) = k \det \mathbf{A}$"

$k\mathbf{A}$ scales *every row*, and each row scaling multiplies the determinant by $k$: so $\det(k\mathbf{A}) = k^2 \det \mathbf{A}$ for $2\times2$ and $k^3 \det \mathbf{A}$ for $3\times3$.

**Fix:** geometry again — $k\mathbf{A}$ includes an enlargement by $k$, and an enlargement scales area by $k^2$, volume by $k^3$. The exponent is the dimension.

### 3. "$(\mathbf{A}\mathbf{B})^{-1} = \mathbf{A}^{-1}\mathbf{B}^{-1}$"

Keeping the order feels natural and is wrong — the undo must reverse it.

**Fix:** socks and shoes, then the one-line proof: multiply $(\mathbf{A}\mathbf{B})(\mathbf{A}^{-1}\mathbf{B}^{-1})$ and watch it *fail* to collapse (nothing cancels in the middle), then $(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1})$ collapse beautifully. The failed attempt teaches more than the successful one.

### 4. Adjugate without the transpose

The most common $3\times3$ hand-slip: computing all nine cofactors correctly, then forgetting to transpose before dividing.

**Fix:** make the self-check non-optional — one row of $\mathbf{A}\mathbf{A}^{-1}$ takes ten seconds, and an un-transposed adjugate fails it immediately.

### 5. "The bars mean it's positive"

Writing $\lvert \mathbf{M} \rvert = -3$ and "correcting" it to $3$.

**Fix:** the bars are determinant notation, not absolute value; the sign is data (a flip happened). Area questions add real absolute-value bars *around* the determinant — $\lvert \det \mathbf{M} \rvert$ — precisely because the determinant itself may be negative.

## Exam Notes

### Cambridge 9231 — Further Pure 1, §1.4

A matrix question is a fixture of Paper 1 — every recent paper has one, typically 8–12 marks across parts. The determinant/inverse marks concentrate in these shapes:

- **"Show that $\mathbf{A}$ is non-singular"** with a parameter: compute the determinant (a quadratic in $k$), then argue it has no real root — completing the square or "negative definite" reasoning as in Example 2(a). The conclusion sentence ("never zero, hence non-singular") carries a mark; don't stop at the expression.
- **Given the inverse, find the parameter:** one entry of $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$ is the cheapest tool (Example 2(b), Route 1); $\det(\mathbf{A}^{-1}) = 1/\det \mathbf{A}$ is the elegant alternative the mark scheme also accepts.
- **Inverse of a product:** $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$, including three-factor versions — the syllabus flags the extension explicitly.
- **Undoing a transformation:** "find the matrix that maps the image back" is one word long in this language: $\mathbf{M}^{-1}$. See [[Invariant Points and Lines]] for the transformation half of §1.4, where this composes with area scale factors (and the modulus trap that lives there).
- Matrices in questions may be non-square ("at most 3 rows and columns" per the syllabus) — non-square matrices multiply but never have determinants or inverses.
- Calculators are permitted and many compute a $3\times3$ inverse — which is exactly why the papers ask for *structure* (parameters, proofs, products) rather than raw computation. The hand method still matters: "show that" questions demand visible cofactors, and the structure is the content.

### Edexcel IAL — Further Pure 1 §5–6 and Further Pure 3 §6

Edexcel splits this card across two units, and the split is the thing to know:

- **FP1 (WFM01)** — §5.4 "evaluation of $2\times2$ determinants; singular and non-singular matrices"; §5.5 "inverse of $2\times2$ matrices; use of the relation $(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$"; §6.4 "the inverse (when it exists) of a given transformation or combination of transformations", with the guidance note *idea of the determinant as an area scale factor*. **$2\times2$ only** at this unit — an FP1 candidate needs the first half of this card and can leave the $3\times3$ machinery for later.
- **FP3 (WFM03)** — §6.4–6.6 lift everything to $3\times3$: determinants, inverses, $(\mathbf{AB})^{-1}$, and the inverse of a transformation in three dimensions. FP3 §6.3 also asks for the **transpose** and $(\mathbf{AB})^{\mathsf T} = \mathbf{B}^{\mathsf T}\mathbf{A}^{\mathsf T}$ — the same socks-and-shoes reversal for a different operation — and §6.7–6.8 go on to eigenvalues and diagonalisation ([[Eigenvalues and Eigenvectors]]).
- The spec's own notation list gives both $\det \mathbf{M}$ and $\lvert \mathbf{M} \rvert$; either is accepted.

### IB Mathematics: Applications and Interpretation HL

Matrices live in **AI HL only** — there are none in Analysis and Approaches at either level. AHL 1.14 covers matrix operations, "determinants and inverses of $n \times n$ matrices *with technology*, and by hand for $2\times2$", and solving systems as $\mathbf{A}\mathbf{x} = \mathbf{b}$; AHL 3.9 covers geometric transformations by matrices, their compositions, and "the geometric interpretation of the determinant of a transformation matrix" — the area scale factor. The exam culture is the opposite of Cambridge's: the $3\times3$ inverse is a calculator keystroke, and the marks are for *setting up* the matrix model and *reading* what the determinant means. AHL 1.15 continues to eigenvalues.

### AP Precalculus — Unit 4 (not assessed)

Unit 4 of the AP Precalculus framework carries this material — 4.11 *The Inverse and Determinant of a Matrix* ($2\times2$), 4.12 *Linear Transformations and Matrices*, 4.13–4.14 matrices as functions and as models — but **Unit 4 is not assessed on the AP exam**. It is course content, not test content: useful if a school teaches it, no marks riding on it. No other AP course examines matrices.

### Where it is *not* examined

None of **Cambridge 9709**, **0580** or **0606** carries matrices in its current syllabus, and **OxAQA 9260** stops at matrix multiplication and transformations (G23–G26) without determinants or inverses. **IB AA** has no matrices at all. A student on any of these boards meets this card as enrichment or as preparation for Further/university work, not for an exam.

### Beyond high school — University

The determinant scales to $n \times n$ as signed $n$-volume, but cofactor expansion becomes catastrophically slow (it hides $n!$ products); real computation uses elimination, $O(n^3)$. The determinant then reappears everywhere: the Jacobian determinant measures local volume distortion in multivariable change-of-variables, $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ is the characteristic equation that produces [[Eigenvalues and Eigenvectors]], and Cramer's rule writes each unknown of a linear system as a ratio of two determinants — beautiful, and never used for computation, for the same $n!$ reason.

## Connections

- **Parent:** [[Matrix]] — the operations, and the non-commutativity that makes inverse order matter.
- **Defining partner:** [[Identity Matrix]] — the inverse is *defined* by reaching $\mathbf{I}$; "undo" has no meaning without "do nothing".
- **Geometric context:** [[Matrix Transformations]] — columns as images of basis vectors is what makes det-as-area readable.
- **Composition:** [[Combination of Transformations]] — $\mathbf{A}\mathbf{B}$ as "B then A" is why the inverse reverses to $\mathbf{B}^{-1}\mathbf{A}^{-1}$.
- **Continues in:** [[Invariant Points and Lines]] — the other half of the same topic, the transformation geometry: what the machine *keeps*, now that this card has measured what it *distorts*.
- **Same expansion elsewhere:** [[Cross Product]] — the $\mathbf{i}, \mathbf{j}, \mathbf{k}$ formula is a $3\times3$ cofactor expansion, and the scalar triple product is det-as-volume in vector clothing.
- **Extension:** [[Eigenvalues and Eigenvectors]] — $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ turns the singularity test into a search: *for which $\lambda$ does $\mathbf{A} - \lambda\mathbf{I}$ collapse?*
- **For 9231 students:** [[MF19 Reference (9231)]] — nothing from this card is on the formula sheet; the $2\times2$ inverse formula and the cofactor method live in your head.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\det \mathbf{M}$ | `\det \mathbf{M}` | determinant as operator |
| $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ | `\begin{vmatrix} a & b \\ c & d \end{vmatrix}` | determinant with bars |
| $\mathbf{M}^{-1}$ | `\mathbf{M}^{-1}` | inverse |
| $\operatorname{adj} \mathbf{A}$ | `\operatorname{adj} \mathbf{A}` | adjugate |
| $M_{ij}$, $C_{ij}$ | `M_{ij}`, `C_{ij}` | minor and cofactor of entry $(i, j)$ |
| $(-1)^{i+j}$ | `(-1)^{i+j}` | the checkerboard sign |
| $\operatorname{diag}(2,3,5)$ | `\operatorname{diag}(2,3,5)` | diagonal matrix shorthand |
| $\blacksquare$ | `\blacksquare` | end of proof |
