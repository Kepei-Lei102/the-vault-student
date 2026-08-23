---
chinese: 特征值与特征向量 (tèzhēngzhí yǔ tèzhēng xiàngliàng)
prerequisites:
  - "[[Invariant Points and Lines]]"
  - "[[Determinants and Inverses]]"
  - "[[Matrix Transformations]]"
  - "[[Cross Product]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/matrices
  - domain/transformations
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-9231
  - curriculum/Edexcel-IAL
  - curriculum/IB-AI
  - syllabus/9231-2-2
  - type/definition
  - type/theorem
  - type/technique
  - type/proof
  - notation/matrix
  - notation/lambda
  - misconception/eigenvector-scaling-freedom
  - misconception/zero-vector-vs-zero-eigenvalue
  - misconception/d-must-match-p
  - misconception/substituting-matrix-into-determinant
---

# Eigenvalues and Eigenvectors 特征值与特征向量

> *Spin a globe. Every city on Earth sweeps through space — Chengdu, London, São Paulo, all of them dragged along circles. Except two points. The poles do not move, and the axis through them is the one direction the spin keeps. Euler proved that **every** rotation of 3-D space, however tumbled, has such an axis — you cannot turn a globe without holding it somewhere.*
>
> *The axis is an eigenvector: a direction the transformation refuses to change. Find the kept directions of a matrix and you have found its skeleton — along them, the matrix is not a swirl of numbers but a plain stretch. Everything in the hunt below is a way of asking one question: **what does this matrix keep, and by how much does it stretch what it keeps?***

Watch it happen before any algebra — one matrix hits a fan of directions, and two of them refuse to turn:

![[eigen-see-it-run.mp4]]

## Definition

### Formal

Let $\mathbf{A}$ be a square matrix. A non-zero vector $\mathbf{e}$ is an **eigenvector** of $\mathbf{A}$, with **eigenvalue** $\lambda$, if

$$\mathbf{A}\mathbf{e} = \lambda\mathbf{e}.$$

The matrix sends $\mathbf{e}$ to a scalar multiple of itself: same line through the origin, length scaled by $\lambda$ (and flipped if $\lambda < 0$). The **characteristic equation** of $\mathbf{A}$ is $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$; its roots are the eigenvalues.

Two boundary rules, both load-bearing:

- $\mathbf{e} = \mathbf{0}$ is **never** an eigenvector. The zero vector satisfies $\mathbf{A}\mathbf{0} = \lambda\mathbf{0}$ for *every* $\lambda$, so admitting it would make the definition say nothing. An eigenvector must be a genuine direction.
- $\lambda = 0$ is a **perfectly good eigenvalue**. It says $\mathbf{A}\mathbf{e} = \mathbf{0}$ — the matrix crushes a whole direction to the origin — which happens exactly when $\mathbf{A}$ is singular.

### Intuitive

Recall the rails of [[Invariant Points and Lines]]: a line through the origin that a transformation maps onto itself, every point *sliding along* the line rather than leaving it. Watch a single point on a rail: it slides, and because the transformation is linear the slide is a uniform stretch — $(1,1) \mapsto (3,3)$ means everything on that rail triples its distance from the origin.

An eigenvector is a rail remembered *with its stretch factor*. The rail answers "which direction survives?"; the eigenvalue answers "and what happens along it?". Together they turn a matrix from four (or nine) tangled numbers into a short list of plain instructions: *stretch this direction by $3$, that one by $2$.* Everything below is the payoff of that translation — it is what makes $\mathbf{A}^{50}$ computable by hand.

### 中文锚点 (Chinese Anchor)

**特征向量**是矩阵"不肯转动"的方向：$\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$，向量 $\mathbf{e}$ 变换后还在原来那条过原点的直线上，只是长度伸缩了 $\lambda$ 倍——**特征值**就是这个伸缩倍数（$\lambda<0$ 表示还调了个头）。找它们的思路只有一句话：把 $\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$ 改写成 $(\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}$，要它有非零解，矩阵 $\mathbf{A} - \lambda\mathbf{I}$ 就必须是**奇异**（singular，行列式为零）的，所以解 $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$（**特征方程** characteristic equation）先拿到 $\lambda$，再回代求方向。**对角化**是这套东西的回报：换到特征向量的视角，矩阵就变成纯粹的"各方向各自拉伸"，算高次幂 $\mathbf{A}^n$ 从苦工变成一步——这正是考题最爱的地方。凯莱–哈密顿定理（矩阵满足自己的特征方程）则给了降幂和求逆的第二条路。国内高中不学这些——线性代数是大学课程（也是考研的重头戏），所以别指望"以前学过"，这里就是第一次见面；好在它建立在你刚学过的不变直线上：**特征向量就是不变直线的方向，特征值就是沿线的伸缩倍数**，新的只是名字和算法。

## The bridge — rails, grown up

| [[Invariant Points and Lines]] said | This topic says | Relationship |
|---|---|---|
| invariant line through the origin | eigenvector (any non-zero vector along it) | same object; vector replaces gradient |
| points *slide along* the rail | slide is a uniform stretch by $\lambda$ | the eigenvalue is the slide, quantified |
| line of invariant points ($\mathbf{M}\mathbf{p} = \mathbf{p}$) | eigenvector with $\lambda = 1$ | pins are the stretch-by-one special case |
| gradient quadratic $bm^2 + (a-d)m - c = 0$ | characteristic equation $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ | two quadratics, complementary questions |

The last row deserves a moment. For $\begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}$, the gradient quadratic gives $m = 1$ and $m = 2$ — the *directions* — while the characteristic equation (worked below) gives $\lambda = 3$ and $\lambda = 2$ — the *stretches*. And they pair up crosswise: the rail $y = x$ (gradient $1$) carries stretch $3$, while the rail $y = 2x$ (gradient $2$) carries stretch $2$. One quadratic finds where the rails are, the other finds what happens on them; an eigenvector-with-eigenvalue is both answers stapled together.

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| eigenvalue | $\lambda$ | "lambda" | occasionally $\mu$ or $m$ in exam papers when $\lambda$ is taken |
| eigenvector | $\mathbf{e}$, $\mathbf{v}$, $\mathbf{x}$ | "the eigenvector" | any non-zero scalar multiple is the same eigenvector |
| diagonalising pair | $\mathbf{Q}, \mathbf{D}$ or $\mathbf{P}, \mathbf{D}$ | — | the 9231 syllabus writes $\mathbf{Q}\mathbf{D}\mathbf{Q}^{-1}$; its own mark schemes write $\mathbf{P}$, $\mathbf{D}$. Same thing — use whichever letter the question uses |
| characteristic equation | $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ | — | some texts use $\det(\lambda\mathbf{I} - \mathbf{A}) = 0$; same roots (the two determinants differ by a factor $(-1)^n$) |

> [!warning] Notation trap
> An eigenvector is only defined **up to scale**: if $\mathbf{e}$ works then so does $k\mathbf{e}$ for any $k \neq 0$, so $\begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix}$ and $\begin{pmatrix} \frac{2}{3} \\ 0 \\ 1 \end{pmatrix}$ are the *same answer*. Clear fractions and pick small integers. Edexcel IAL is the one board that may ask you to **normalise** (divide by the length so $\lvert \mathbf{e} \rvert = 1$); Cambridge never does.

## The hunt, part 1 — eigenvalues from the characteristic equation

**Why the determinant appears.** Move everything in $\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$ to one side:

$$\mathbf{A}\mathbf{e} - \lambda\mathbf{e} = \mathbf{0} \quad\Longrightarrow\quad (\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}.$$

(The $\mathbf{I}$ is forced: $\mathbf{A} - \lambda$ is meaningless — you cannot subtract a number from a matrix — so $\lambda$ enters wearing the identity as a coat.) Now recall from [[Determinants and Inverses]]: if $\mathbf{A} - \lambda\mathbf{I}$ were non-singular, it would have an inverse, and multiplying by it would force $\mathbf{e} = \mathbf{0}$ — the one vector the definition forbids. A non-zero solution exists **only if the matrix collapses**:

$$\boxed{\ \det(\mathbf{A} - \lambda\mathbf{I}) = 0.\ }$$

This is the singularity test of [[Determinants and Inverses]] turned into a *search*: for which $\lambda$ does $\mathbf{A} - \lambda\mathbf{I}$ collapse? Each collapse value is an eigenvalue, and the direction it crushes to zero is the eigenvector that comes with it.

**And know now what the formula booklet does for you here: nothing.** MF19 prints no characteristic equation, no diagonalisation identity, no Cayley–Hamilton ([[MF19 Reference (9231)]]). Everything on this page is carried in your head — the consolation is that the box above is most of it.

### The $2\times2$ case — worked in place

**The ask, stated the way an exam would state it:** *find the eigenvalues of* $\mathbf{A} = \begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}$ (the rails matrix of [[Invariant Points and Lines]]) — that is, find every value of $\lambda$ at which $\mathbf{A} - \lambda\mathbf{I}$ collapses.

*Tool: the characteristic equation.*

$$\det\begin{pmatrix} 4-\lambda & -1 \\ 2 & 1-\lambda \end{pmatrix} = (4-\lambda)(1-\lambda) - (-1)(2) = \lambda^2 - 5\lambda + 6 = 0,$$

so $\lambda = 2$ or $\lambda = 3$. Notice what the quadratic's coefficients are. The $5$ is $4 + 1$, the sum down the main diagonal — a quantity meeting you for the first time here, and worth its name: the **trace** of a matrix, written $\operatorname{tr}\mathbf{A}$, is simply the sum of its diagonal entries. The $6$ is $4\cdot1 - (-1)\cdot2$, the familiar **determinant**. That is general for $2\times2$:

$$\lambda^2 - (\operatorname{tr}\mathbf{A})\,\lambda + \det\mathbf{A} = 0,$$

and by the same Vieta reading as [[Symmetric Functions of Roots]]: **the eigenvalues sum to the trace and multiply to the determinant** — true at every size, and the fastest sanity check in the topic. ($2 + 3 = 5$ ✓, $2 \times 3 = 6$ ✓.) The product form also re-proves the boundary rule above: $\det\mathbf{A} = \lambda_1\lambda_2\cdots$, so $\mathbf{A}$ is singular exactly when some eigenvalue is $0$.

![[eigen-characteristic-collapse.svg|760]]

### The $3\times3$ case — expand along the zeros, keep it factored

*Tool: cofactor expansion, choosing the row or column with the most zeros ([[Determinants and Inverses]]).* A real exam case: show that $\mathbf{A} = \begin{pmatrix} -1 & 3 & 4 \\ 0 & 1 & 0 \\ 0 & -2 & 5 \end{pmatrix}$ has eigenvalues $-1$, $1$ and $5$.

$$\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} -1-\lambda & 3 & 4 \\ 0 & 1-\lambda & 0 \\ 0 & -2 & 5-\lambda \end{vmatrix}.$$

The first **column** has two zeros — expand down it, and only one cofactor survives:

$$(-1-\lambda)\begin{vmatrix} 1-\lambda & 0 \\ -2 & 5-\lambda \end{vmatrix} = (-1-\lambda)(1-\lambda)(5-\lambda) = 0 \quad\Longrightarrow\quad \lambda = -1,\ 1,\ 5. \qquad\blacksquare$$

**Do not multiply out.** The determinant arrived already factored; expanding it into $-\lambda^3 + 5\lambda^2 + \lambda - 5$ and then re-factorising a cubic is undoing your own work. On a "show that the eigenvalues are…" question the factored line *is* the answer — and the mark scheme explicitly refuses two shortcuts: checking that each given value satisfies the equation (that verifies, it doesn't *find*), and row-reducing $\mathbf{A}$ first (row operations change the eigenvalues — they preserve solution sets of systems, not the transformation itself).

**The triangular gift.** If $\mathbf{A}$ is upper or lower triangular, $\mathbf{A} - \lambda\mathbf{I}$ is too — and a triangular determinant is just the product of its diagonal. (Why: expand down the first column; only the top entry is non-zero, and its cofactor is again triangular, so the expansion peels off one diagonal entry at a time until none are left.) So **the eigenvalues are simply the diagonal entries**. A matrix like $\begin{pmatrix} a & 1 & 1 \\ 0 & 2a & -1 \\ 0 & 0 & -3a \end{pmatrix}$ hands you $\lambda = a,\ 2a,\ -3a$ by inspection; examiners award this in one mark and expect no working. When a printed matrix has that staircase of zeros, read the diagonal before doing anything else.

## The hunt, part 2 — eigenvectors

With $\lambda$ in hand, the eigenvector is any non-zero solution of $(\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}$. For $2\times2$ this is one line of algebra: the two equations agree (they must — you chose $\lambda$ to *make* the matrix singular, exactly as the invariant-points equations agreed in [[Invariant Points and Lines]]), so read the direction off either.

For the rails matrix $\mathbf{A} = \begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}$, take $\lambda = 3$ and write the unknown eigenvector as $\mathbf{e} = \begin{pmatrix} x \\ y \end{pmatrix}$:

$$(\mathbf{A} - 3\mathbf{I})\mathbf{e} = \begin{pmatrix} 1 & -1 \\ 2 & -2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x - y \\ 2x - 2y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.$$

Read it row by row, by hand: the top row says $x - y = 0$, the bottom says $2x - 2y = 0$ — the same line twice, $y = x$. Pick any non-zero point of that line as the answer: $\mathbf{e} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, the rail $y = x$, as promised. For $\lambda = 2$: $\begin{pmatrix} 2 & -1 \\ 2 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \mathbf{0}$ says $2x - y = 0$ twice over, so $y = 2x$ and $\mathbf{e} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ on the rail $y = 2x$.

> [!warning] The calculator will not hand you an eigenvector
> The simultaneous-equation solver on a standard exam calculator *refuses* this system — it reports infinitely many solutions, which is correct (a whole rail solves it) and useless. Finding the eigenvector is a by-hand read, and a one-line one: the two rows agree by construction, so read the direction off either. Where the calculator does earn its keep is the check afterwards: multiply $\mathbf{A}\mathbf{e}$ in matrix mode and confirm it returns $\lambda\mathbf{e}$.

![[eigen-rails-stretch.svg|860]]

### The $3\times3$ shortcut — a cross product finds the kernel

*Tool: [[Cross Product]] — perpendicular to both inputs.* The equation $(\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}$ says, row by row, that **each row of $\mathbf{A} - \lambda\mathbf{I}$ dots to zero with $\mathbf{e}$** — the eigenvector is perpendicular to every row. For a genuine eigenvalue of a $3\times3$ with distinct eigenvalues, the three rows span a plane, so $\mathbf{e}$ is the common perpendicular of that plane — which is exactly what a cross product of two (independent) rows delivers:

$$\mathbf{e} = \mathbf{r}_1 \times \mathbf{r}_2 \quad \text{(any two independent rows of } \mathbf{A} - \lambda\mathbf{I}).$$

Two points of technique before running it. **Which two rows?** Any two of the three that are genuinely different directions — you need two, three are on offer, so skip whichever is least convenient: a zero row says $0 = 0$ and carries no information, and a row that is a multiple of another adds nothing new. **And what kind of multiplication is this?** Not a matrix product — recall from [[Cross Product]] that $\times$ here is the vector cross product, which the mark schemes write as the $\mathbf{i}, \mathbf{j}, \mathbf{k}$ determinant:

$$\begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} \times \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} = \begin{pmatrix} a_2 b_3 - a_3 b_2 \\ a_3 b_1 - a_1 b_3 \\ a_1 b_2 - a_2 b_1 \end{pmatrix}.$$

Continuing the exam case above — $\mathbf{A}$ the $3\times3$ matrix whose eigenvalues $-1, 1, 5$ were just shown — take $\lambda = 1$:

$$\mathbf{A} - \mathbf{I} = \begin{pmatrix} -2 & 3 & 4 \\ 0 & 0 & 0 \\ 0 & -2 & 4 \end{pmatrix}, \qquad \begin{pmatrix} -2 \\ 3 \\ 4 \end{pmatrix} \times \begin{pmatrix} 0 \\ -2 \\ 4 \end{pmatrix} = \begin{pmatrix} 3\cdot4 - 4\cdot(-2) \\ 4\cdot0 - (-2)\cdot4 \\ (-2)(-2) - 3\cdot0 \end{pmatrix} = \begin{pmatrix} 20 \\ 8 \\ 4 \end{pmatrix} \sim \begin{pmatrix} 5 \\ 2 \\ 1 \end{pmatrix}.$$

(The zero row was skipped — cross the two informative ones. The $\sim$ is the scaling freedom: divide by $4$.) The same trick on $\lambda = -1$ gives $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ and on $\lambda = 5$ gives $\begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix}$; solving the equations directly is never wrong, but the cross product turns a page of elimination into three lines, and Cambridge mark schemes present it as the primary method. Always spend five seconds on the check that catches everything: multiply $\mathbf{A}\mathbf{e}$ and confirm you get $\lambda\mathbf{e}$.

## What the definition alone can prove

The syllabus asks you to *use* $\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$ to prove properties, and the proofs are all the same move: apply $\mathbf{A}$ again, or apply $\mathbf{A}^{-1}$, and watch $\lambda$ pop out as a scalar. A real exam question, verbatim: *given that $m$ is an eigenvalue of the non-singular matrix $\mathbf{A}$ with eigenvector $\mathbf{e}$, show that $\mathbf{e}$ is an eigenvector of $\mathbf{A}^3$ with eigenvalue $m^3$.*

*Tool: the definition, applied repeatedly; scalars commute past matrices.*

$$\mathbf{A}^3\mathbf{e} = \mathbf{A}^2(\mathbf{A}\mathbf{e}) = \mathbf{A}^2(m\mathbf{e}) = m\,\mathbf{A}(\mathbf{A}\mathbf{e}) = m\,\mathbf{A}(m\mathbf{e}) = m^2(\mathbf{A}\mathbf{e}) = m^3\mathbf{e}. \qquad\blacksquare$$

The same one-line pattern gives the whole family — same eigenvectors every time, only the eigenvalue transforms:

| Matrix | Eigenvalue | One-line reason |
|---|---|---|
| $\mathbf{A}^n$ | $\lambda^n$ | apply $\mathbf{A}$ repeatedly, as above |
| $\mathbf{A}^{-1}$ | $\lambda^{-1}$ | multiply $\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$ by $\mathbf{A}^{-1}$, divide by $\lambda$ (non-zero since $\mathbf{A}$ is non-singular) |
| $k\mathbf{A}$ | $k\lambda$ | $(k\mathbf{A})\mathbf{e} = k(\mathbf{A}\mathbf{e}) = k\lambda\mathbf{e}$ |
| $\mathbf{A} + k\mathbf{I}$ | $\lambda + k$ | $(\mathbf{A} + k\mathbf{I})\mathbf{e} = \lambda\mathbf{e} + k\mathbf{e}$ |
| $p(\mathbf{A})$, any polynomial | $p(\lambda)$ | combine the rows above |

The **shift rule** ($\mathbf{A} + k\mathbf{I}$) is the exam's favourite disguise: a question that diagonalises $\mathbf{A} - 2\mathbf{I}$ wants you to notice it has *the same eigenvectors as $\mathbf{A}$*, with every eigenvalue lowered by $2$ — no new hunt required.

## Diagonalisation — the matrix in its own coordinates

### Why $\mathbf{A}\mathbf{Q} = \mathbf{Q}\mathbf{D}$ — numbers first, then the reason

The hunt just gave the rails matrix $\mathbf{A} = \begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}$ its full eigen-list: $\lambda = 3$ with $\mathbf{e}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, and $\lambda = 2$ with $\mathbf{e}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$. Pack the eigenvectors as the **columns** of a matrix $\mathbf{Q}$, and the eigenvalues, **in matching order**, down a diagonal matrix $\mathbf{D}$:

$$\mathbf{Q} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \mathbf{D} = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}.$$

Now compute both products and compare them:

$$\mathbf{A}\mathbf{Q} = \begin{pmatrix} 4 & -1 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 3 & 4 \end{pmatrix}, \qquad \mathbf{Q}\mathbf{D} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 3 & 4 \end{pmatrix}.$$

Equal — and the *why* is visible column by column. The first column of $\mathbf{A}\mathbf{Q}$ is $\mathbf{A}\mathbf{e}_1 = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3\mathbf{e}_1$, because $\mathbf{e}_1$ *is* the stretch-by-$3$ direction; the first column of $\mathbf{Q}\mathbf{D}$ is $\mathbf{Q}$'s first column scaled by the $3$ sitting in $\mathbf{D}$'s first slot. Same for the second columns: $\mathbf{A}\mathbf{e}_2 = \begin{pmatrix} 2 \\ 4 \end{pmatrix} = 2\mathbf{e}_2$ on the left, column two scaled by $2$ on the right. Both sides compute the same thing — *each eigenvector, stretched by its own $\lambda$* — by two different routes.

That is the whole proof; in general, with eigenvectors as columns and eigenvalues in matching order,

$$\mathbf{A}\mathbf{Q} = \begin{pmatrix} \mathbf{A}\mathbf{e}_1 & \mathbf{A}\mathbf{e}_2 & \mathbf{A}\mathbf{e}_3 \end{pmatrix} = \begin{pmatrix} \lambda_1\mathbf{e}_1 & \lambda_2\mathbf{e}_2 & \lambda_3\mathbf{e}_3 \end{pmatrix} = \mathbf{Q}\mathbf{D}.$$

(The middle step is the definition applied to each column. The last step is what the numbers just showed: multiplying $\mathbf{Q}$ *on the right* by a diagonal matrix scales its **columns** — column $i$ by $\lambda_i$. Multiplying on the left would scale rows; that is why $\mathbf{D}$ must sit on the right.) With distinct eigenvalues the eigenvectors are independent, $\mathbf{Q}$ is invertible, and

$$\boxed{\ \mathbf{A} = \mathbf{Q}\mathbf{D}\mathbf{Q}^{-1}.\ }$$

Read right to left, this is a **detour with a purpose**: $\mathbf{Q}^{-1}$ translates a vector into eigenvector coordinates, $\mathbf{D}$ does the only thing the matrix ever really does — stretch each kept direction by its factor — and $\mathbf{Q}$ translates back. The matrix was a plain stretch all along; we were just looking at it in the wrong coordinates.

![[eigen-diagonalisation-detour.svg|760]]

### The payoff — powers

Squaring makes the detour collapse in the middle:

$$\mathbf{A}^2 = \mathbf{Q}\mathbf{D}\,\underbrace{\mathbf{Q}^{-1}\mathbf{Q}}_{\mathbf{I}}\,\mathbf{D}\mathbf{Q}^{-1} = \mathbf{Q}\mathbf{D}^2\mathbf{Q}^{-1}, \qquad\text{and in general}\qquad \mathbf{A}^n = \mathbf{Q}\mathbf{D}^n\mathbf{Q}^{-1},$$

where $\mathbf{D}^n$ costs nothing: a diagonal matrix powers **entry by entry**, $\mathbf{D}^n = \operatorname{diag}(\lambda_1^n, \lambda_2^n, \lambda_3^n)$. Multiply once by hand to believe it —

$$\mathbf{D}^2 = \begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 9 & 0 \\ 0 & 4 \end{pmatrix}$$

— every off-diagonal slot is a row of zeros meeting a column of zeros, so each diagonal entry only ever multiplies itself. Fifty applications of the matrix, priced as two real matrix multiplications and some exponents.

### Worked in place — a mystery resolved

*Tool: diagonalisation for powers.* [[Proof by Induction]] proves that $\mathbf{M} = \begin{pmatrix} 4 & -1 \\ 6 & -1 \end{pmatrix}$ satisfies $\mathbf{M}^n = \begin{pmatrix} 3\cdot2^n - 2 & 1 - 2^n \\ 6\cdot2^n - 6 & 3 - 2^{n+1} \end{pmatrix}$ — and remarks that the $2^n$ and the constants are eigenvalues showing through. Here is the machinery that *produces* that formula rather than merely verifying it.

**Step 1 — eigenvalues.** $\lambda^2 - (\operatorname{tr}\mathbf{M})\lambda + \det\mathbf{M} = \lambda^2 - 3\lambda + 2 = (\lambda - 1)(\lambda - 2)$, so $\lambda = 1, 2$.

**Step 2 — eigenvectors.** $\lambda = 1$: $\begin{pmatrix} 3 & -1 \\ 6 & -2 \end{pmatrix}\mathbf{e} = \mathbf{0}$ gives $y = 3x$, $\mathbf{e}_1 = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$. $\lambda = 2$: $\begin{pmatrix} 2 & -1 \\ 6 & -3 \end{pmatrix}\mathbf{e} = \mathbf{0}$ gives $y = 2x$, $\mathbf{e}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$.

**Step 3 — assemble and invert.** $\mathbf{Q} = \begin{pmatrix} 1 & 1 \\ 3 & 2 \end{pmatrix}$, $\det\mathbf{Q} = -1$, so $\mathbf{Q}^{-1} = \begin{pmatrix} -2 & 1 \\ 3 & -1 \end{pmatrix}$ (swap-and-negate, [[Determinants and Inverses]]).

**Step 4 — power and multiply out.**

$$\mathbf{M}^n = \mathbf{Q}\begin{pmatrix} 1 & 0 \\ 0 & 2^n \end{pmatrix}\mathbf{Q}^{-1} = \begin{pmatrix} 1 & 2^n \\ 3 & 2^{n+1} \end{pmatrix}\begin{pmatrix} -2 & 1 \\ 3 & -1 \end{pmatrix} = \begin{pmatrix} 3\cdot2^n - 2 & 1 - 2^n \\ 6\cdot2^n - 6 & 3 - 2^{n+1} \end{pmatrix}. \qquad\blacksquare$$

Induction *verifies* a formula someone hands you; diagonalisation *explains where it came from* — every entry is a mix of $1^n$ and $2^n$ weighted by eigenvector bookkeeping, and nothing else could appear.

### The exam's two favourite twists

- **Power inside the diagonalisation.** *Find $\mathbf{P}$ and $\mathbf{D}$ such that $\mathbf{A}^7 = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$.* No new work: $\mathbf{A}^7$ has the same eigenvectors, eigenvalues raised to the $7$th (the property table). One real paper's answer: eigenvalues $-1, 1, 2$ of an upper-triangular $\mathbf{A}$ become $\mathbf{D} = \operatorname{diag}(-1,\ 1,\ 128)$ — the examiner wants to see $128$, i.e. the entries *evaluated*, not $\mathbf{D}$ left as "$\operatorname{diag}(-1,1,2)$ to the power $7$".
- **Shift inside the diagonalisation.** *Find $\mathbf{P}$ and $\mathbf{D}$ such that $\mathbf{A} - 2\mathbf{I} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$.* Same eigenvectors again; eigenvalues drop by $2$ (the shift rule). For the $3\times3$ case worked above, $\mathbf{D} = \operatorname{diag}(-3, -1, 3)$ with $\mathbf{P} = \begin{pmatrix} 1 & 5 & 2 \\ 0 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix}$ — columns in the same order as the diagonal, always.

> [!info] Beyond syllabus — when diagonalisation fails
> The syllabus promises real, distinct eigenvalues, and distinctness is what guarantees enough independent eigenvectors to fill $\mathbf{Q}$. Outside that guarantee two things can break. A **rotation** of the plane has characteristic equation $\lambda^2 - 2\cos\theta\,\lambda + 1 = 0$ with no real roots for most $\theta$ — no real direction survives a turn, exactly the "none" row of the census in [[Invariant Points and Lines]] (the roots are the complex pair $e^{\pm i\theta}$, and [[Complex Numbers]] is where rotation eigenvalues live happily). A **shear** $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $\lambda = 1$ twice but only *one* eigenvector direction — too few rails to build $\mathbf{Q}$, so no diagonalisation exists at all. Repeated eigenvalues are where linear algebra gets genuinely subtle, and where the university course picks up.

## The Cayley–Hamilton theorem — a matrix obeys its own equation

**Statement.** Every square matrix satisfies its own characteristic equation: if $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ expands to $\lambda^3 + b\lambda^2 + c\lambda + d = 0$, then

$$\mathbf{A}^3 + b\mathbf{A}^2 + c\mathbf{A} + d\mathbf{I} = \mathbf{0} \qquad \text{(the zero matrix — and the constant rides on } \mathbf{I}\text{)}.$$

Read the statement again and it sounds like it cannot possibly be saying anything — *a matrix satisfies its own equation*, pure 废话文学, the mathematical cousin of "it is what it is." Hold on to that feeling, because it is exactly the trap. The characteristic equation is a fact about *numbers* $\lambda$; the theorem's claim is a different and genuinely surprising one — rebuild the polynomial out of **matrix powers**, constant riding on $\mathbf{I}$, and all nine entries' worth of arithmetic cancel to the zero matrix. The next two blocks take it seriously: first check it really is true, then see why the "obvious" one-line proof of it is fake.

**Verify it for the general $2\times2$** — the syllabus takes the theorem on trust, but trust is cheap to check at size two. With $\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and characteristic equation $\lambda^2 - (a+d)\lambda + (ad - bc) = 0$:

$$\mathbf{A}^2 - (a+d)\mathbf{A} + (ad-bc)\mathbf{I} = \begin{pmatrix} a^2+bc & ab+bd \\ ca+dc & cb+d^2 \end{pmatrix} - \begin{pmatrix} a^2+ad & ab+bd \\ ca+dc & ad+d^2 \end{pmatrix} + \begin{pmatrix} ad-bc & 0 \\ 0 & ad-bc \end{pmatrix} = \mathbf{0}. \checkmark$$

> [!warning] The one-line "proof" that proves nothing
> It is tempting to argue: "substitute $\lambda = \mathbf{A}$ into $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$, giving $\det(\mathbf{A} - \mathbf{A}) = \det\mathbf{0} = 0$ — done." This is nonsense wearing a gown: the characteristic *polynomial* is a polynomial in a **number** $\lambda$, and what Cayley–Hamilton asserts is that a completely different object — the polynomial re-built with **matrix** powers and $\mathbf{I}$ carrying the constant — equals the zero matrix. The substitution conflates a scalar $0$ with a matrix $\mathbf{0}$ and skips the entire content of the theorem. (For diagonalisable matrices an honest proof is two lines with the machinery above: $p(\mathbf{A}) = \mathbf{Q}\,p(\mathbf{D})\,\mathbf{Q}^{-1}$, and $p(\mathbf{D})$ is diagonal with entries $p(\lambda_i) = 0$.)

Why examiners love it: the theorem is a **power-trading machine**. The characteristic equation, rearranged, expresses $\mathbf{A}^3$ in terms of $\mathbf{A}^2$, $\mathbf{A}$, $\mathbf{I}$ — so any polynomial in $\mathbf{A}$, however high its degree, can be ground down to a quadratic in $\mathbf{A}$. Two standard uses:

**Use 1 — successive powers.** A matrix with eigenvalues $2, 5, -2$ has characteristic equation $(\lambda-2)(\lambda-5)(\lambda+2) = \lambda^3 - 5\lambda^2 - 4\lambda + 20 = 0$, so

$$\mathbf{A}^3 = 5\mathbf{A}^2 + 4\mathbf{A} - 20\mathbf{I}.$$

*Tool: multiply through by $\mathbf{A}$, then substitute the expression for $\mathbf{A}^3$ back in — the degree never rises above what you already know.*

$$\mathbf{A}^4 = 5\mathbf{A}^3 + 4\mathbf{A}^2 - 20\mathbf{A} = 5(5\mathbf{A}^2 + 4\mathbf{A} - 20\mathbf{I}) + 4\mathbf{A}^2 - 20\mathbf{A} = \boxed{29\mathbf{A}^2 - 100\mathbf{I}}$$

— a real exam answer, and note the exam's phrasing "*express $\mathbf{A}^4$ in the form $a\mathbf{A}^2 + b\mathbf{A} + c\mathbf{I}$*": the $\mathbf{I}$ must be there (writing $+\,c$ bare adds a number to a matrix).

**Use 2 — the inverse without cofactors.** Multiply the characteristic equation through by $\mathbf{A}^{-1}$ instead: from $\mathbf{A}^3 - 5\mathbf{A}^2 - 4\mathbf{A} + 20\mathbf{I} = \mathbf{0}$,

$$\mathbf{A}^2 - 5\mathbf{A} - 4\mathbf{I} + 20\mathbf{A}^{-1} = \mathbf{0} \quad\Longrightarrow\quad \mathbf{A}^{-1} = \tfrac{1}{20}\left(-\mathbf{A}^2 + 5\mathbf{A} + 4\mathbf{I}\right).$$

One matrix squaring replaces the entire minors–cofactors–adjugate ritual of [[Determinants and Inverses]] — the trade is a bargain whenever the characteristic equation is already on the page. (It works exactly when $\mathbf{A}^{-1}$ exists: the constant term is $\pm\det\mathbf{A}$, and dividing by it is possible precisely when no eigenvalue is zero.)

## Worked example — standalone, every tool named

*A real Paper 2 question, complete. The matrix $\mathbf{P} = \begin{pmatrix} a & 1 & 1 \\ 0 & 2a & -1 \\ 0 & 0 & -3a \end{pmatrix}$ has non-zero eigenvalues.* (MF19 supplies nothing anywhere below — not the characteristic equation, not the root–coefficient relations that build it in (b), not the diagonalisation identity in (c). All memory.)

**(a) State, in terms of $a$, the eigenvalues of $\mathbf{P}$.** [1]

*Tool: the triangular gift — eigenvalues of a triangular matrix are its diagonal entries.* The process, run once so it is yours: $\mathbf{P} - \lambda\mathbf{I}$ is still upper triangular, so its determinant is the product of its diagonal,

$$\det(\mathbf{P} - \lambda\mathbf{I}) = (a-\lambda)(2a-\lambda)(-3a-\lambda) = 0 \quad\Longrightarrow\quad \lambda = a,\ 2a,\ -3a.$$

In the exam: it is one mark and the word is "state" — just write $\lambda = a,\ 2a,\ -3a$, no working expected. ("Non-zero eigenvalues" is the question quietly telling you $a \neq 0$.)

**(b) Find $\mathbf{P}^{-1}$, using the characteristic equation.** [4]

*Tool: eigenvalues → characteristic equation via the symmetric functions.* $\operatorname{tr} = a + 2a - 3a = 0$; pairwise sum $= 2a^2 - 3a^2 - 6a^2 = -7a^2$; product $= -6a^3$. So (matching $(\lambda - a)(\lambda - 2a)(\lambda + 3a) = 0$ expanded):

$$\lambda^3 - 7a^2\lambda + 6a^3 = 0.$$

*Tool: Cayley–Hamilton, multiplied through by $\mathbf{P}^{-1}$.* $\mathbf{P}^3 - 7a^2\mathbf{P} + 6a^3\mathbf{I} = \mathbf{0}$, so $\mathbf{P}^2 - 7a^2\mathbf{I} + 6a^3\mathbf{P}^{-1} = \mathbf{0}$, giving

$$\mathbf{P}^{-1} = \frac{1}{6a^3}\left(7a^2\mathbf{I} - \mathbf{P}^2\right), \qquad \mathbf{P}^2 = \begin{pmatrix} a^2 & 3a & -2a-1 \\ 0 & 4a^2 & a \\ 0 & 0 & 9a^2 \end{pmatrix} \ \Longrightarrow\ \mathbf{P}^{-1} = \frac{1}{6a^3}\begin{pmatrix} 6a^2 & -3a & 2a+1 \\ 0 & 3a^2 & -a \\ 0 & 0 & -2a^2 \end{pmatrix}.$$

*(Check: the diagonal of $\mathbf{P}^{-1}$ is $\frac{1}{a}, \frac{1}{2a}, -\frac{1}{3a}$ — the reciprocals of the eigenvalues, on the same diagonal, exactly as the property table demands of a triangular matrix.)*

**(c) The $3\times3$ matrix $\mathbf{A}$ has eigenvalues $1, 2, 3$ with corresponding eigenvectors $\begin{pmatrix} a \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 2a \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ -3a \end{pmatrix}$. Find $\mathbf{A}$ in terms of $a$.** [5]

*Tool: diagonalisation run forwards — $\mathbf{A} = \mathbf{Q}\mathbf{D}\mathbf{Q}^{-1}$ builds a matrix from its eigen-data.* The eigenvector matrix is exactly $\mathbf{P}$ from part (a) — the question's quiet gift, since its inverse is already on the page. And why is $\mathbf{D} = \operatorname{diag}(1, 2, 3)$? Because $\mathbf{D}$'s diagonal holds **the eigenvalues, in the order their eigenvectors were packed as columns**: the question paired eigenvalue $1$ with the first listed eigenvector (column 1 of $\mathbf{P}$), $2$ with the second, $3$ with the third — so slot $(1,1)$ holds $1$, slot $(2,2)$ holds $2$, slot $(3,3)$ holds $3$. Column $i$ and entry $ii$ always describe the same rail:

$$\mathbf{A} = \mathbf{P}\begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}\mathbf{P}^{-1} = \begin{pmatrix} a & 2 & 3 \\ 0 & 4a & -3 \\ 0 & 0 & -9a \end{pmatrix} \cdot \frac{1}{6a^3}\begin{pmatrix} 6a^2 & -3a & 2a+1 \\ 0 & 3a^2 & -a \\ 0 & 0 & -2a^2 \end{pmatrix} = \begin{pmatrix} 1 & \dfrac{1}{2a} & -\dfrac{4a+1}{6a^2} \\[2mm] 0 & 2 & \dfrac{1}{3a} \\[2mm] 0 & 0 & 3 \end{pmatrix}.$$

*(Check: the answer is triangular with diagonal $1, 2, 3$ — its eigenvalues, read by the triangular gift. Both hunts, run in both directions, in one exam question.)*

## Why the biggest eigenvalue owns the long run

Write any starting vector in eigenvector coordinates: $\mathbf{x} = c_1\mathbf{e}_1 + c_2\mathbf{e}_2$ (possible whenever the eigenvectors span, which distinct eigenvalues guarantee). Apply $\mathbf{A}$ $n$ times — each piece stretches independently, because that is all the matrix ever does to its rails:

$$\mathbf{A}^n\mathbf{x} = c_1\lambda_1^n\mathbf{e}_1 + c_2\lambda_2^n\mathbf{e}_2 = \lambda_1^n\left(c_1\mathbf{e}_1 + c_2\left(\tfrac{\lambda_2}{\lambda_1}\right)^n\mathbf{e}_2\right).$$

If $\lvert\lambda_1\rvert > \lvert\lambda_2\rvert$, the ratio $(\lambda_2/\lambda_1)^n \to 0$: every trace of $\mathbf{e}_2$ fades, and **every starting direction (with $c_1 \neq 0$) swings onto the dominant rail**. Repeatedly applying a matrix is a compass that finds the largest eigenvalue's eigenvector — the clip below runs it live.

![[eigen-power-iteration.mp4]]

## Where this is the working tool

- **Every Google search, at the origin of the company.** PageRank models the web as a matrix: entry $(i,j)$ is the chance a random clicker on page $j$ moves to page $i$. A page's importance is defined circularly — you matter if important pages link to you — and the fixed point of that circularity is precisely the equation $\mathbf{A}\mathbf{x} = \mathbf{x}$: **the ranking is an eigenvector with $\lambda = 1$**. Google computes it by power iteration, the collapse-onto-the-dominant-rail of the section above, run on a matrix with billions of rows: start anywhere, multiply, repeat until the direction settles. The 1998 paper that launched the company is, mathematically, this section at scale.
- **Why soldiers break step on bridges.** A structure's small vibrations are governed by a matrix built from its stiffness and mass; the eigenvectors are its **modes** — the handful of shapes in which it naturally sways — and the eigenvalues set each mode's natural frequency. Push a bridge at a frequency close to one of its eigenvalues and that mode's amplitude feeds on every push (resonance); the Albert Bridge in London still carries a sign ordering troops to break step. Engineers certify buildings and aircraft by computing eigenvalues and checking that no motor, gust pattern, or footfall rhythm lands on one.
- **Why deep neural networks were nearly untrainable.** Training a deep network pushes a signal — and, backwards, its gradient — through many layers, and near a fixed point that is repeated multiplication by roughly the same matrix. The $\lambda^n$ law of the previous section takes over: dominant eigenvalue above $1$ and the gradient explodes, below $1$ and it vanishes — the **vanishing/exploding gradient problem** that stalled deep learning for decades, and the reason modern weight initialisations deliberately pin the spectrum near $1$. And the transformer pipeline inside an LLM — embed the tokens into vectors, act, un-embed to choose the next token — is the detour diagram with *learned* translations: not literally $\mathbf{Q}\mathbf{D}\mathbf{Q}^{-1}$ (the middle is not diagonal and nothing is linear), but the same move — hard in your coordinates, easy in the right ones, translate back.
- **The name on the door of quantum mechanics.** The German *eigen* means "own, characteristic" — an *Eigenvektor* is the matrix's own vector. The word survived translation because quantum mechanics made it famous: measurable quantities (energy, momentum, spin) are operators, and **the values an experiment can actually return are exactly the operator's eigenvalues**. The discrete energy levels of the hydrogen atom — the reason atoms glow in sharp colours rather than smears — are an eigenvalue list, which is where the "quantum" in the theory's name comes from.

## Common Misconceptions (Teaching Notes)

### 1. "My eigenvector doesn't match the answer key"

A student finds $\begin{pmatrix} 20 \\ 8 \\ 4 \end{pmatrix}$, the key says $\begin{pmatrix} 5 \\ 2 \\ 1 \end{pmatrix}$, and they conclude they are wrong. Any non-zero multiple is the same eigenvector — the object is the *direction*, not the arrow.

**Fix:** check parallelism (is one a multiple of the other?), not equality. And teach the tidy habit: clear common factors before writing the final answer, because $\mathbf{Q}^{-1}$ is far kinder with small integers.

### 2. Writing $\mathbf{e} = \mathbf{0}$, or rejecting $\lambda = 0$

The two zeros get confused in both directions: a student "solves" $(\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}$ with the zero vector (a column of zeros in $\mathbf{Q}$ scores M0 — the mark scheme says so in as many words), or refuses $\lambda = 0$ as "not allowed".

**Fix:** the slogan — *the vector may never be zero, the value may.* $\lambda = 0$ just means the matrix is singular; a zero *vector* means you have said nothing at all.

### 3. $\mathbf{D}$ shuffled out of order with $\mathbf{P}$

Eigenvalues in $\mathbf{D}$, eigenvectors in $\mathbf{P}$ — but in independently chosen orders. The product $\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ then rebuilds a *different* matrix, one with the right eigenvalues attached to the wrong rails.

**Fix:** column discipline. Column $i$ of $\mathbf{P}$ and entry $ii$ of $\mathbf{D}$ describe the same rail; write them as pairs, never as two separate lists. Any *consistent* reordering of the pairs is fine (mark schemes accept "correctly matched permutations").

### 4. Verifying instead of finding

Asked to *show* the eigenvalues are $-1, 1, 5$, a student substitutes each value into $\det(\mathbf{A} - \lambda\mathbf{I})$ and shows each gives $0$. The mark scheme rejects this: checking three roots of a cubic does not show they are the *only* three, and the question is testing the characteristic-equation method.

**Fix:** "show that the eigenvalues are…" always means *derive the characteristic equation and factorise it*. Verification earns its keep afterwards, as the private sanity check on $\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$.

### 5. Row-reducing before hunting

Row operations preserve the solution set of a linear *system*, so students trained on elimination try to simplify $\mathbf{A}$ first. But row operations do **not** preserve eigenvalues — they change the transformation itself ($\det$ survives at most up to the recorded factors; the trace, and with it the characteristic polynomial, does not survive at all).

**Fix:** eigenvalues belong to the matrix as a *transformation*, not to its system-solving behaviour. The only legal simplification is the one the topic hands you: expand the determinant along whatever row or column already has zeros.

## Exam Notes

### Cambridge 9231 (Further Pure 2, Paper 2 — §2.2)

- **A banker, not a maybe:** an eigenvalue question appears in essentially every recent Paper 2, usually 10–13 marks late in the paper, assembled from the same parts: characteristic equation or triangular read-off → eigenvectors (the cross-product route is the mark scheme's primary method) → one twist. The twist rotates through: diagonalise $\mathbf{A}^n$ or $\mathbf{A} + k\mathbf{I}$ (properties table), find $\mathbf{A}^{-1}$ or reduce $\mathbf{A}^4$ via Cayley–Hamilton, prove a property from $\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$, or rebuild $\mathbf{A}$ from given eigen-data.
- Eigenvalues are guaranteed **real and distinct** (syllabus restriction), and $2\times2$ or $3\times3$ only — the shear/rotation pathologies above are beyond the paper.
- Mark-scheme hygiene, all verbatim from recent schemes: forming $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ is the M1 (checking given values or row-reducing $\mathbf{A}$ scores M0); a zero column in $\mathbf{P}$ is M0; $\mathbf{D}$ entries must be evaluated numbers ($128$, not $2^7$ left as a power of an unpowered $\mathbf{D}$); "in the form $a\mathbf{A}^2 + b\mathbf{A} + c\mathbf{I}$" answers must carry the $\mathbf{I}$.
- **MF19 gives nothing for this topic** — no characteristic equation, no diagonalisation formula ([[MF19 Reference (9231)]]). The whole §2.2 kit lives in your head; the compensation is that it is small.

### Edexcel IAL (Further Pure 3 — WFM03, §6.7–6.8)

Same core (eigenvalues and eigenvectors of $2\times2$ and $3\times3$), two house differences: eigenvectors may need to be **normalised** (scaled to unit length — divide by the vector's modulus), and diagonalisation is phrased for **symmetric matrices** via an *orthogonal* $\mathbf{P}$ with $\mathbf{P}^{\mathsf T}\mathbf{A}\mathbf{P} = \mathbf{D}$ — the transpose replacing the inverse, legitimate because for an orthogonal matrix (columns of unit length, mutually perpendicular) $\mathbf{P}^{\mathsf T} = \mathbf{P}^{-1}$. Symmetric matrices are exactly the ones whose eigenvectors come out mutually perpendicular, which is what makes the orthogonal $\mathbf{P}$ possible.

### IB AI HL

AHL 1.15: eigenvalues and eigenvectors of $2\times2$ matrices, characteristic polynomial, diagonalisation with real distinct eigenvalues, and powers via $\mathbf{M}^n = \mathbf{P}\mathbf{D}^n\mathbf{P}^{-1}$ — applied (Markov-chain transition matrices and coupled systems are the AI flavour), with technology carrying the arithmetic. Not in AA at either level.

### Where it is *not* examined

Not on Cambridge 9709 (no matrices anywhere in the syllabus), not on OxAQA 9660 (likewise — no matrix content at all), not on AP Calculus or AP Precalculus (Precalculus Unit 4 stops at determinants and inverses), not in IB AA. This topic is a Further-Mathematics marker: if the course has "Further" in the name, expect it; otherwise don't.

## Connections

- **Parent:** [[Invariant Points and Lines]] — the rails; an eigenvector is an invariant direction carrying its stretch factor, and the gradient quadratic is the characteristic equation asked sideways.
- **Proof ingredient:** [[Determinants and Inverses]] — $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$ *is* the singularity test, run as a search; cofactor expansion computes it, and swap-and-negate inverts $\mathbf{Q}$.
- **Tool:** [[Cross Product]] — two rows of $\mathbf{A} - \lambda\mathbf{I}$, crossed, produce the $3\times3$ eigenvector in one move.
- **Tool:** [[Symmetric Functions of Roots]] — trace and determinant are the elementary symmetric functions of the eigenvalues; the sanity checks and the exam's build-the-characteristic-equation-from-its-roots step are Vieta in matrix clothing.
- **Sibling:** [[Linear Systems in 3D]] — the same syllabus section's other half, and the same engine underneath: hunting an eigenvector *is* solving the singular system $(\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}$, whose solution line is a sheaf spine through the origin.
- **Explains:** [[Proof by Induction]] — the matrix-power formula its Example 4 proves by dominoes is manufactured here by diagonalisation, $2^n$ and $1^n$ visible from the start.
- **Kinship:** [[Second-Order Differential Equations]] — the auxiliary equation is a characteristic equation in disguise: each root $\lambda$ contributes a mode $e^{\lambda t}$ that the system merely rescales, exactly as a matrix rescales its rails, and "general solution = mix of modes" is $\mathbf{x} = c_1\mathbf{e}_1 + c_2\mathbf{e}_2$ wearing calculus clothing.
- **For 9231 students:** [[MF19 Reference (9231)]] — nothing from this topic is on the formula sheet; know what that obliges you to carry.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\lambda$ | `\lambda` | eigenvalue |
| $\mathbf{A}\mathbf{e} = \lambda\mathbf{e}$ | `\mathbf{A}\mathbf{e} = \lambda\mathbf{e}` | the defining equation |
| $\det(\mathbf{A} - \lambda\mathbf{I})$ | `\det(\mathbf{A} - \lambda\mathbf{I})` | characteristic polynomial |
| $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ | `\begin{vmatrix} ... \end{vmatrix}` | determinant bars |
| $\mathbf{Q}\mathbf{D}\mathbf{Q}^{-1}$ | `\mathbf{Q}\mathbf{D}\mathbf{Q}^{-1}` | diagonalised form ($\mathbf{P}$ in mark schemes) |
| $\operatorname{diag}(\lambda_1, \lambda_2, \lambda_3)$ | `\operatorname{diag}(...)` | diagonal matrix shorthand |
| $\operatorname{tr}\mathbf{A}$ | `\operatorname{tr}\mathbf{A}` | trace — diagonal sum |
| $\mathbf{P}^{\mathsf T}$ | `\mathbf{P}^{\mathsf T}` | transpose (IAL orthogonal diagonalisation) |
| $\sim$ | `\sim` | "scales to" — eigenvector up to multiple |
