---
chinese: 三元线性方程组 (sānyuán xiànxìng fāngchéngzǔ)
prerequisites:
  - "[[Matrix]]"
  - "[[Determinants and Inverses]]"
  - "[[Planes in 3D]]"
  - "[[Simultaneous Equations (Vocab)]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/matrices
  - domain/geometry
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-9231
  - curriculum/IB-AI
  - syllabus/9231-2-2
  - type/definition
  - type/technique
  - notation/matrix
  - misconception/singular-means-no-solution
  - misconception/stopping-at-two-equations
  - misconception/inconsistent-means-parallel
---

# Linear Systems in 3D 三元线性方程组

> *Stand in the corner of a room. Two walls meet in a vertical line; the floor cuts that line in a single point, and that point — the corner — is pinned by all three surfaces at once. Now pick up an open book and look at its pages: three pages, no corner anywhere, because all of them pass through the same spine. Now look at a Toblerone box: three long faces, each pair meeting in an edge, the three edges perfectly parallel — and no point on all three faces at all.*
>
> *Three equations in three unknowns are three planes, and solving the system is asking which of these rooms you are standing in. One determinant and one elimination answer it.*

## Definition

### Formal

A system of three linear equations in three unknowns, and its matrix form — the syllabus asks for the translation in **both directions**:

$$\begin{cases} a_1 x + b_1 y + c_1 z = d_1 \\ a_2 x + b_2 y + c_2 z = d_2 \\ a_3 x + b_3 y + c_3 z = d_3 \end{cases} \qquad\Longleftrightarrow\qquad \underbrace{\begin{pmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{pmatrix}}_{\mathbf{A}} \underbrace{\begin{pmatrix} x \\ y \\ z \end{pmatrix}}_{\mathbf{x}} = \underbrace{\begin{pmatrix} d_1 \\ d_2 \\ d_3 \end{pmatrix}}_{\mathbf{b}}$$

Each **row** of $\mathbf{A}\mathbf{x} = \mathbf{b}$ is one equation; each equation is one **plane** in 3-D space ([[Planes in 3D]] — the coefficients $(a_i, b_i, c_i)$ are that plane's normal vector). The system is called **consistent** if at least one point satisfies all three equations, **inconsistent** if none does.

### Intuitive

A solution is a point lying on all three planes simultaneously — a point where the room's three surfaces meet. Generic planes pin exactly one such point (the corner of the room). But planes can conspire: share a spine like the pages of a book, or fence off a Toblerone prism whose faces never all meet. The algebra mirrors the geometry exactly, and the whole topic is a two-question protocol: **does the determinant vanish?** and, if it does, **do the equations survive elimination in agreement or in contradiction?**

### 中文锚点 (Chinese Anchor)

三个三元一次方程就是空间里的**三张平面**，解方程组就是问：**有没有一个点同时落在三张平面上？** 一般情况是三张平面把一个点"钉"住——比如房间的墙角，两面墙加地板，交出唯一一个角点，这时方程组有唯一解，对应系数矩阵的**行列式不为零**。行列式等于零时，平面的摆法出了状况，命运只剩两种：要么三张平面像**打开的书页**共用一条书脊（无穷多组解，解排成一条直线——这个构型英文叫 sheaf，中文叫平面束）；要么像**三棱柱**（Toblerone 巧克力盒）的三个侧面，两两相交出三条平行的棱，却没有一个公共点（无解，inconsistent）。所以判别流程只有两步：先算行列式，不为零就是唯一解；为零就把三个方程消元到底——若消出同一个方程，是书页，有无穷多解；若消出矛盾（比如 $0 = 9$），是棱柱或平行平面，无解。国内教材里这些通常写成"方程组**有解／无解**、解**唯一／不唯一**"，高考只考二元和特殊三元，**用行列式判别、按几何构型分类**是大学线性代数的做法，也是 9231 的做法——但道理不过是"数墙角"而已。

## The bridge — one object, three languages

| Algebra | Matrix | Geometry |
|---|---|---|
| one equation $ax + by + cz = d$ | one row of $\mathbf{A}\mathbf{x} = \mathbf{b}$ | one plane, normal $(a, b, c)$ |
| a solution $(x, y, z)$ | a vector $\mathbf{x}$ with $\mathbf{A}\mathbf{x} = \mathbf{b}$ | a point on all three planes |
| equations proportional (RHS too) | one row a multiple of another | the same plane written twice |
| eliminating a variable | combining rows | slicing the configuration |

Keep all three columns live: exam questions ask in one language and expect the answer in another ("solve" is algebra; "interpret geometrically" is the right-hand column; the marks are for crossing over).

## Question 1 — the determinant

Recall from [[Determinants and Inverses]]: $\det \mathbf{A} \neq 0$ means $\mathbf{A}^{-1}$ exists, and then

$$\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$$

is *the* solution — exactly one, always, whatever $\mathbf{b}$ is. Geometrically the three planes pin a single point: **the room's corner, the generic case.** A question that says "*show the system has a unique solution*" wants one determinant computed and declared non-zero; no elimination, no solving, done.

$\det \mathbf{A} = 0$ means the matrix crushes 3-D space flat, and two fates become possible — but the determinant **cannot tell you which**. The three normals have become coplanar (that is what the vanishing scalar triple product of the rows says, [[Cross Product]] §scalar triple product), so the planes have lost the independence needed to pin a point. Whether they still share anything depends on the *right-hand sides* — which the determinant never looked at.

## Question 2 — eliminate, and read the verdict

When $\det \mathbf{A} = 0$, the move is exactly what it sounds like: **eliminate one unknown and see what is going on.** The discipline the mark scheme insists on: **use all three equations, and reduce to *one* equation in two unknowns** — combine equations two different ways (e.g. eq₂ − 4·eq₁ and eq₃ − 7·eq₁) so every equation participates, then compare what survives:

- **The two combinations are the same equation.** The third plane brought no new demand: all three pass through one line. **Consistent — infinitely many solutions**, the line of a **sheaf** (or, if two of the original equations were outright proportional, a coincident pair cut by the third — same algebra, slightly different picture).
- **The two combinations contradict** (e.g. $y + 2z = 1$ and $y + 2z = 2$, or the naked $0 = 9$). No point satisfies everything. **Inconsistent — no solutions**: a **prism**, or parallel planes.

Both fates are drawn below — the decision as a flowchart, and every configuration pictured under the census.

Stopping at two equations in two unknowns proves nothing — a real mark scheme awards it M1 A0, because two equations in two unknowns generically *look* solvable; the content is in whether the two independent eliminations **agree**.

To tell the inconsistent geometries apart, look at the **normals**: parallel planes have proportional normal vectors $(a, b, c)$; a prism's three normals are coplanar but no two are parallel — the planes lean like the three faces of the Toblerone box, pairwise meeting in three parallel edges.

![[linear-systems-decision.svg|740]]

## The census — every way three planes can stand

| $\det \mathbf{A}$ | Configuration | Solutions | The tell |
|---|---|---|---|
| $\neq 0$ | three planes pin a point (the corner) | exactly one | the generic case — nothing else to check |
| $= 0$ | **sheaf** 平面束: three distinct planes, one common line | infinitely many (a line) | eliminations agree; no two rows proportional |
| $= 0$ | two planes coincident, third crosses them | infinitely many (a line) | two full rows (RHS included) proportional |
| $= 0$ | three planes coincident | infinitely many (a plane) | all rows proportional, RHS included |
| $= 0$ | **prism** 三棱柱: pairwise meeting, three parallel edge-lines | none | eliminations contradict; no two normals parallel |
| $= 0$ | two (or three) parallel distinct planes | none | proportional normals, RHS breaking the proportion |
| $= 0$ | two coincident planes, third parallel | none | one proportion holds fully, one only in the normals |

![[linear-systems-configurations.svg|860]]

## Worked cases — real Paper 2 questions, every tool named

### Case 1 — the parameter hunt (unique or not)

*The system $6x - ay = 3,\quad 2x - y = 1,\quad x + 5y + 4z = 2$ is given. Find the value of $a$ for which the system does not have a unique solution, and determine the consistency of the system in each case.*

*Tool: Question 1 — the determinant, expanded along the column of zeros ([[Determinants and Inverses]]).*

$$\det \mathbf{A} = \begin{vmatrix} 6 & -a & 0 \\ 2 & -1 & 0 \\ 1 & 5 & 4 \end{vmatrix} = 4\,(6\cdot(-1) - (-a)\cdot 2) = 8a - 24,$$

zero exactly when $a = 3$. So for $a \neq 3$: unique solution, consistent, three planes pinning a point — say so and stop.

*Tool: Question 2 — eliminate and compare.* For $a = 3$ the first equation is $6x - 3y = 3$, which is the second equation multiplied by $3$ — **the same plane written twice** (the row proportion includes the right-hand side: $(6, -3, 0 \mid 3) = 3\,(2, -1, 0 \mid 1)$). Two distinct demands remain for three unknowns: $2x - y = 1$ and $x + 5y + 4z = 2$ — two planes meeting in a line. **Consistent, infinitely many solutions.** (Answer both branches; the question asked "in each case".)

### Case 2 — show singular, then name the shape

*Show that the system $x + 2y + 3z = 1,\quad 4x + 5y + 6z = 1,\quad 7x + 8y + 9z = 1$ does not have a unique solution, and interpret the system geometrically.*

*Tool: Question 1.* $\det \mathbf{A} = 1(45 - 48) - 2(36 - 42) + 3(32 - 35) = -3 + 12 - 9 = 0$ — no unique solution. (The $1$-to-$9$ matrix is the classic singular matrix: each row rises by the same step, $\text{row}_3 - \text{row}_2 = \text{row}_2 - \text{row}_1$, and that dependence *is* the zero determinant.)

*Tool: Question 2 — all three equations, down to one equation.*

$$\text{eq}_2 - 4\,\text{eq}_1:\ \ -3y - 6z = -3 \ \Rightarrow\ y + 2z = 1, \qquad \text{eq}_3 - 7\,\text{eq}_1:\ \ -6y - 12z = -6 \ \Rightarrow\ y + 2z = 1.$$

Both eliminations deliver **the same equation** — the sheaf's certificate. **The three planes form a sheaf**: they intersect in a common line. (The mark scheme accepts "the three planes intersect along a common line", or a clear sketch; the vocabulary *sheaf* is worth owning anyway.)

*Going one step beyond the asked marks — describe the line.* Set $z = t$: then $y = 1 - 2t$, and eq₁ gives $x = 1 - 2(1 - 2t) - 3t = t - 1$. The spine of the book:

$$\mathbf{r} = \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} + t\begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} \qquad \text{(check: the direction dots to zero with every normal ✓)}$$

### Case 3 — same planes, different fate: the right-hand side decides

*The system $x - y + 2z = 4,\quad x - y - 3z = b,\quad x - y + 7z = 13$ is given. (i) For $b = -5$, solve the system and interpret geometrically. (ii) Show that for $b \neq -5$ the system is inconsistent, and interpret geometrically.*

All three normals are $(1, -1, k)$ — coplanar (no $x$–$y$ tilt ever differs), so $\det \mathbf{A} = 0$ for *every* $b$: the determinant has said all it will ever say, and the right-hand side now decides everything.

*Tool: Question 2, subtracting pairs (the $x - y$ block eliminates itself).*

$$\text{eq}_1 - \text{eq}_2:\ \ 5z = 4 - b, \qquad \text{eq}_3 - \text{eq}_1:\ \ 5z = 9.$$

**(i)** $b = -5$: both say $z = \tfrac{9}{5}$ — agreement, the sheaf again. Back-substitute: $x - y = 4 - 2\cdot\tfrac{9}{5} = \tfrac{2}{5}$. The solutions are the whole line $z = \tfrac{9}{5},\ x - y = \tfrac{2}{5}$ — set $y = t$: $\ \mathbf{r} = \left(\tfrac{2}{5},\, 0,\, \tfrac{9}{5}\right) + t\,(1, 1, 0)$. **Three planes with a common line.**

**(ii)** $b \neq -5$: the two eliminations demand $5z = 4 - b$ *and* $5z = 9$ with $4 - b \neq 9$ — a contradiction, **no solutions**. Geometrically: no two normals are parallel (the $k$'s differ), so no planes are parallel — each pair still meets in a line, but the three lines of intersection are parallel and never concur. **The three planes form a triangular prism.**

This case is the deepest lesson in the topic: *the determinant never changed*. Consistency is not a property of $\mathbf{A}$ alone — it is a property of $\mathbf{A}$ *and* $\mathbf{b}$, of the walls *and* where you put them.

## Where this is the working tool

- **$\mathbf{A}\mathbf{x} = \mathbf{b}$ is, by volume, the most-solved problem in computing.** Simulating a bridge under load, a wing in airflow, tomorrow's weather, or a phone's antenna means chopping the object into millions of small elements whose interactions are linear — one gigantic linear system per time-step, solved by refined descendants of exactly the elimination above (the $O(n^3)$ elimination that [[Determinants and Inverses]] notes made matrices computable). A supercomputer's headline benchmark, LINPACK, is literally "how fast can you solve $\mathbf{A}\mathbf{x} = \mathbf{b}$".
- **A CT scanner solves an inconsistent system on purpose.** Each X-ray beam through the body contributes one linear equation (the densities along its path sum to the measured attenuation); a scan collects hundreds of thousands of equations in the unknown pixel densities. Measurement noise makes the system *inconsistent* — no image satisfies every reading exactly — and the machine answers with **least squares**: the image that misses all the equations by the least total amount. Inconsistency, which the exam treats as an endpoint ("no solutions"), is where real engineering starts negotiating.
- **Circuit analysis is this topic wearing physics clothing.** Kirchhoff's laws turn any resistor network into a linear system — one equation per loop and junction, the currents as unknowns — and a circuit simulator is a linear-system solver in a trench coat. The [[Electric Current]] side of the vault meets this algebra from the other direction.

## Common Misconceptions (Teaching Notes)

### 1. "det = 0, so there's no solution"

The determinant vanishing only removes *uniqueness*. The system may still have infinitely many solutions (sheaf) — or none (prism). Half the exam marks live precisely in this distinction.

**Fix:** the two-question protocol as a reflex. Question 1 (determinant) sorts unique from not-unique; only Question 2 (eliminate, compare) sorts consistent from inconsistent. Case 3 above is the cure hardwired: same determinant, both fates.

### 2. Stopping at two equations in two unknowns

Elimination once, then "two equations, two unknowns — solvable, so consistent." But the two survivors may contradict, and if you only formed one of them you never found out. The mark scheme's M1 A0 is written for exactly this script.

**Fix:** two independent eliminations, every equation used, reduced to *one* relation — then the comparison (agree / contradict) *is* the answer.

### 3. "Inconsistent means some planes are parallel"

The prism has **no** parallel planes — every pair meets happily in a line; the three lines are parallel instead, so the meeting point never happens. Students who equate "no solution" with "parallel walls" mislabel every prism question.

**Fix:** the Toblerone box. Then the normals test: parallel planes need proportional *normals*; a prism's normals are coplanar but pairwise unaligned.

### 4. Calling a coincident pair a sheaf

In Case 1's $a = 3$ branch, $6x - 3y = 3$ and $2x - y = 1$ *look* like different equations but are the same plane — a proportion that includes the right-hand side. Two planes, not three; the picture is "one plane cut by another", not three pages of a book.

**Fix:** whenever the determinant dies, scan the rows *with their right-hand sides* for proportional pairs before classifying. Proportional including RHS → coincident; proportional in normals only → parallel.

## Exam Notes

### Cambridge 9231 (Further Pure 2, Paper 2 — §2.2)

- The topic's regular shapes, all from real papers: *find the parameter value for which there is no unique solution, then determine consistency in each case*; *show the determinant is zero and interpret geometrically*; *solve the consistent singular system* (answer expected as a point-plus-direction line or with one unknown as parameter); *change only the right-hand side and re-classify* (the sheaf-to-prism flip of Case 3).
- Vocabulary the schemes accept: "sheaf" or "the three planes intersect along a common line" (a clear sketch also earns the mark); "triangular prism" for the pairwise-parallel-lines picture.
- The M1 A0 trap in the schemes' own words: eliminations must "use all three equations to reduce to one equation with two unknowns" — reducing to two equations and stopping earns method only.
- Calculators solve unique systems directly, so pure "solve" marks are rare; the marks are in classification, the geometry words, and parameter work. MF19 offers nothing here (as for all of §2.2 — [[MF19 Reference (9231)]]).

### IB AI HL

AHL 1.14 includes solving systems of up to three linear equations as $\mathbf{A}\mathbf{x} = \mathbf{b}$ with technology, naming the unique / infinitely-many / no-solution trichotomy; the AI flavour is recognising the situation from calculator output rather than hand elimination, and the geometric interpretation is lighter than Cambridge's.

### Where it is *not* examined

Not on Cambridge 9709 or Edexcel IAL Mathematics (both stop at two equations in two unknowns — IAL P1 solves simultaneous equations "by substitution", and even IAL Further's FP3 matrices unit runs determinants → inverses → eigenvalues without ever classifying systems); not on OxAQA 9660 (no matrix content); not on AP Calculus or AP Precalculus; IB AA has no matrices at any level. Like its sibling topic, a Further-Mathematics marker.

## Connections

- **Parent:** [[Planes in 3D]] — supplies the planes, their normals, and the two-planes-meet-in-a-line fact; its three-floors-pin-a-corner picture is Question 1's geometry, and the sheaf/prism configurations named there get their full algebra here.
- **Proof ingredient:** [[Determinants and Inverses]] — Question 1 *is* the singularity test, and $\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$ is the unique-case solution; the vanishing determinant as coplanar rows is the scalar triple product of [[Cross Product]].
- **Sibling:** [[Eigenvalues and Eigenvectors]] — the other half of the same syllabus section, and the same engine underneath: an eigenvector solves the singular system $(\mathbf{A} - \lambda\mathbf{I})\mathbf{e} = \mathbf{0}$, which is this topic's "infinitely many solutions" case with $\mathbf{b} = \mathbf{0}$ (a homogeneous system is always consistent — the origin is on every plane through the origin — so the only question is whether it has *more* than the trivial solution, and $\det = 0$ says yes: the eigenvector line is a sheaf spine through the origin).
- **Foundation:** [[Matrix]], [[Simultaneous Equations (Vocab)]] — the $2\times2$ story this card lifts one dimension.
- **For 9231 students:** [[MF19 Reference (9231)]] — nothing from this topic is on the formula sheet.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\mathbf{A}\mathbf{x} = \mathbf{b}$ | `\mathbf{A}\mathbf{x} = \mathbf{b}` | the matrix form |
| $\det \mathbf{A}$ | `\det \mathbf{A}` | Question 1 |
| $\begin{vmatrix} \cdot \end{vmatrix}$ | `\begin{vmatrix} ... \end{vmatrix}` | determinant bars |
| $\mathbf{r} = \mathbf{a} + t\mathbf{d}$ | `\mathbf{r} = \mathbf{a} + t\mathbf{d}` | the sheaf's line, point plus direction |
| $\text{eq}_2 - 4\,\text{eq}_1$ | `\text{eq}_2 - 4\,\text{eq}_1` | naming an elimination step |
