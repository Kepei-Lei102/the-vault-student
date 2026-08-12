---
chinese: 向量几何 (xiàngliàng jǐhé)
prerequisites:
  - "[[Vectors]]"
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Similarity]]"
  - "[[Congruence]]"
  - "[[3D Trigonometry]]"
  - "[[Magnitude of a Vector (Vocab)]]"
leads_to:
  - "[[Matrix Transformations]]"
  - "[[3D Vectors]]"
  - "[[Vector Equations of Lines]]"
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
  - syllabus/0580-E7-4
  - syllabus/0606-13-2
  - syllabus/0606-13-4
  - syllabus/9709-3-7
  - type/theorem
  - type/proof
  - notation/position-vector
  - misconception/section-formula-weights
  - misconception/direction-of-AB
---

# Vector Geometry 向量几何

## Definition

### Formal

**Vector geometry** is the practice of using vectors to prove and solve problems about points, lines, and regions in the plane (and in 3D). A geometric configuration is encoded as a set of vectors; a geometric claim becomes an algebraic identity about those vectors.

### Intuitive — Geometry Without a Protractor

Classical Euclidean geometry reasons from angles and lengths using [[Congruence]], [[Similarity]], and the parallel postulate. Vector geometry reasons from **displacements**. Instead of "triangles ABC and DEF are congruent by SAS," we write "$\vec{AB} = \vec{DE}$ and $\vec{AC} = \vec{DF}$" and the conclusion follows by algebra. The same theorem, two different languages — and the vector language is usually shorter.

### 中文锚点 (Chinese Anchor)

向量几何：**用向量的代数运算来证明和求解几何问题。**

Chinese physics already treats displacement (位移), velocity (速度), and force (力) as vectors. What's new here is the idea that **positions themselves** (not just motions between positions) can be represented as vectors — and that a whole diagram of points and lines can be turned into a single algebraic expression.

## The Bridge: Cartesian Coordinates ↔ Position Vectors

This is the single most important conceptual move in this card. The student has been using Cartesian coordinates since middle school — $P = (3, 4)$ means "3 right, 4 up from origin." A **position vector** takes exactly that information and packages it as a vector whose *start is pinned at the origin*.

$$P = (3, 4) \quad \longleftrightarrow \quad \vec{OP} = \begin{pmatrix} 3 \\ 4 \end{pmatrix} = 3\mathbf{i} + 4\mathbf{j}$$

**Left side** is a *point* — a location. **Right side** is a *vector* — an arrow from $O$ to that location. The numbers are identical. The *meaning* differs: a point has no direction, a vector does.

| Cartesian coordinates | Position vectors |
|---|---|
| $P = (3, 4)$ | $\vec{OP} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ |
| "Point $P$ is at $(3,4)$" | "The position vector of $P$ is $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$" |
| Static — just names a location | Dynamic — a displacement from the origin |
| Cannot be added: $(1,2) + (3,4)$ means nothing geometric | Can be added: $\vec{OP} + \vec{OQ}$ is the parallelogram diagonal |
| Gives distances via $\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ | Gives distances via $\lvert \vec{AB} \rvert = \lvert \mathbf{b} - \mathbf{a} \rvert$ |

Both systems describe the same plane. Coordinates are fine for naming points; vectors are fine for **doing algebra with displacements between points**. Vector geometry is what happens when you switch from the left column to the right column. Every formula in this card can be re-derived from coordinate geometry alone, but the vector formulas are shorter and generalise to 3D without change.

**Convention.** In this card, lowercase bold letters $\mathbf{a}$, $\mathbf{b}$, $\mathbf{p}$ are the position vectors of capital-letter points $A$, $B$, $P$ respectively: $\mathbf{a} = \vec{OA}$, $\mathbf{b} = \vec{OB}$, etc.

![[vectors-position-vectors.svg]]

## Key Facts / Properties

### 1. The master identity — $\vec{AB}$ from position vectors

$$\boxed{\vec{AB} = \mathbf{b} - \mathbf{a}}$$

**Why?** Walk from $A$ to $B$ via the origin: $\vec{AB} = \vec{AO} + \vec{OB} = -\vec{OA} + \vec{OB} = -\mathbf{a} + \mathbf{b} = \mathbf{b} - \mathbf{a}$. Just a triangle law around the origin.

This formula is the most-used identity in all of vector geometry. Circle it in the student's notes. **"Head minus tail"** in English, **"终点减起点"** in Chinese.

### 2. Parallel vectors

Two non-zero vectors $\mathbf{u}$ and $\mathbf{v}$ are **parallel** if and only if one is a scalar multiple of the other:

$$\mathbf{u} \parallel \mathbf{v} \iff \mathbf{v} = k \mathbf{u} \text{ for some scalar } k \ne 0$$

If $k > 0$ they point the same way; if $k < 0$ they point opposite ways (still called parallel in vector language — the lines they sit on are parallel).

> [!tip] Test for parallel vectors
> To show $\begin{pmatrix} 6 \\ 9 \end{pmatrix}$ and $\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ are parallel: check whether their components are in the same ratio. $6/2 = 3$ and $9/3 = 3$ — same ratio, so $\begin{pmatrix} 6 \\ 9 \end{pmatrix} = 3\begin{pmatrix} 2 \\ 3 \end{pmatrix}$. Parallel.

### 3. Collinearity — three points on a line

Three points $A$, $B$, $C$ are **collinear** (lie on a single straight line) if and only if $\vec{AB}$ and $\vec{AC}$ are parallel — that is,

$$\vec{AC} = k \cdot \vec{AB} \quad \text{for some scalar } k$$

**Why?** If $C$ lies on the line through $A$ and $B$, the displacement from $A$ to $C$ is a scaled version of the displacement from $A$ to $B$ (same direction, different length). If it's not a scalar multiple, $C$ is off the line.

This test — "prove two vectors are scalar multiples and share a point" — is the standard 9260/0606 exam technique for collinearity.

### 4. Midpoint of a line segment

If $M$ is the midpoint of $AB$, then

$$\mathbf{m} = \frac{\mathbf{a} + \mathbf{b}}{2}$$

**Why?** The midpoint of two numbers is their average. Same idea in vectors — the midpoint of two positions is the vector average of the two position vectors. This is also the special case of the section formula below when $m = n = 1$.

### 5. Ratio division of a line (section formula)

If $P$ divides $AB$ in the ratio $m : n$ (meaning $AP : PB = m : n$), then

$$\mathbf{p} = \mathbf{a} + \frac{m}{m+n} \vec{AB} = \mathbf{a} + \frac{m}{m+n}(\mathbf{b} - \mathbf{a})$$

which rearranges to the classical **section formula**:

$$\boxed{\mathbf{p} = \frac{n\mathbf{a} + m\mathbf{b}}{m + n}}$$

**Why this is memorable.** The section formula is a weighted average of the two endpoints, but the weights **swap**: the $m$ end (close to $A$) sits with $\mathbf{b}$, and the $n$ end sits with $\mathbf{a}$. Intuition: when $m$ is small, $P$ is close to $A$, so $\mathbf{p}$ should be close to $\mathbf{a}$ — which happens exactly when the coefficient of $\mathbf{a}$ is close to 1, i.e., when $n/(m+n)$ is close to 1, i.e., when $m$ is small.

> [!info] Beyond syllabus — Centroid and centre of mass
> For a triangle $ABC$ with position vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$, the **centroid** (where the medians meet) is
> $$\mathbf{g} = \frac{\mathbf{a} + \mathbf{b} + \mathbf{c}}{3}$$
> This is the average of the three vertices — the same averaging idea as the midpoint, extended. In physics, if three equal masses sit at the vertices, the centre of mass is at $\mathbf{g}$. The vector-average formula generalises immediately to $n$ points.

### 6. Velocity vectors (Cambridge 0606 13.4)

In mechanics, a moving object's instantaneous velocity is a vector $\mathbf{v}$ whose magnitude is speed and whose direction is the direction of motion. Two velocities compose by vector addition:

$$\mathbf{v}_{\text{resultant}} = \mathbf{v}_1 + \mathbf{v}_2$$

**Example.** A boat heads at 5 m/s due north across a river whose current flows east at 3 m/s. Ground velocity $\mathbf{v}_{\text{ground}} = \begin{pmatrix} 3 \\ 5 \end{pmatrix}$; ground speed $\sqrt{34} \approx 5.83$ m/s; bearing $\tan^{-1}(3/5) \approx 031°$ from north.

**Relative velocity** — the velocity of object $A$ as seen by object $B$ — is

$$\mathbf{v}_{A \text{ rel } B} = \mathbf{v}_A - \mathbf{v}_B$$

Subtraction again — the "head minus tail" identity in disguise.

This content appears in Cambridge 0606 13.4, A-Level Mechanics, and GCSE/A-Level physics. Unified vector framework, three exam boards.

## Strategy: Vector Proofs in Three Steps

Every "prove that ..." question in 0580 E7.4 / 9260 G22 / 0606 13 follows the same template.

1. **Express every displacement as $\mathbf{b} - \mathbf{a}$** using the master identity. Turn the diagram into algebra.
2. **Simplify** using vector arithmetic (addition, scalar multiplication).
3. **Read the geometric conclusion** from the algebraic form:
   - $\vec{XY} = k \cdot \vec{ZW}$ → $XY$ is parallel to $ZW$
   - same plus shared point → points are collinear
   - $\vec{XM} = \vec{MY}$ → $M$ is the midpoint of $XY$
   - ratio of scalars → ratio of lengths

The exam mark scheme rewards showing each step explicitly.

## Worked Examples

### Example 1 (9260 level): Collinearity

Points $A(1, 2)$, $B(4, 5)$, $C(10, 11)$ are given. Show that $A$, $B$, $C$ are collinear.

![[vectors-example-1.svg]]

**Solution.**

Position vectors: $\mathbf{a} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $\mathbf{b} = \begin{pmatrix} 4 \\ 5 \end{pmatrix}$, $\mathbf{c} = \begin{pmatrix} 10 \\ 11 \end{pmatrix}$.

Step 1 — master identity:
$$\vec{AB} = \mathbf{b} - \mathbf{a} = \begin{pmatrix} 4-1 \\ 5-2 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}, \qquad \vec{AC} = \mathbf{c} - \mathbf{a} = \begin{pmatrix} 9 \\ 9 \end{pmatrix}$$

Step 2 — simplify:
$$\vec{AC} = 3 \vec{AB}$$

Step 3 — read the conclusion: the two vectors are parallel and share the point $A$, so $A$, $B$, $C$ are collinear. $\blacksquare$

### Example 2 (0580 / 9260 level): Parallelogram diagonals

$OABC$ is a parallelogram with $\vec{OA} = \mathbf{a}$ and $\vec{OC} = \mathbf{c}$. $M$ is the midpoint of diagonal $OB$. Show that $M$ is also the midpoint of diagonal $AC$.

![[vectors-example-2.svg]]

**Solution.**

Since $OABC$ is a parallelogram, $\vec{OB} = \vec{OA} + \vec{AB} = \vec{OA} + \vec{OC} = \mathbf{a} + \mathbf{c}$.

$M$ is the midpoint of $OB$:
$$\vec{OM} = \tfrac{1}{2}\vec{OB} = \tfrac{1}{2}(\mathbf{a} + \mathbf{c})$$

Let $M'$ be the midpoint of $AC$. Its position vector is the average of $\mathbf{a}$ and $\mathbf{c}$:
$$\vec{OM'} = \tfrac{1}{2}(\mathbf{a} + \mathbf{c})$$

$\vec{OM} = \vec{OM'}$, so $M = M'$. The diagonals of a parallelogram bisect each other. $\blacksquare$

This is a **vector proof** of a classical Euclidean theorem. Vectors reduce a geometry-of-shapes argument to a one-line algebra identity.

### Example 3 (0606 / A-Level level): Ratio division

Points $A$ and $B$ have position vectors $\mathbf{a}$ and $\mathbf{b}$. Point $P$ divides $AB$ in the ratio $2 : 3$. Express $\vec{OP}$ in terms of $\mathbf{a}$ and $\mathbf{b}$.

**Solution.**

$AP : PB = 2 : 3$, so $P$ is $\tfrac{2}{5}$ of the way from $A$ to $B$:

$$\vec{OP} = \mathbf{a} + \tfrac{2}{5}\vec{AB} = \mathbf{a} + \tfrac{2}{5}(\mathbf{b} - \mathbf{a}) = \tfrac{3}{5}\mathbf{a} + \tfrac{2}{5}\mathbf{b}$$

Or directly from the section formula with $m = 2$, $n = 3$:

$$\vec{OP} = \frac{3\mathbf{a} + 2\mathbf{b}}{5}$$

Same answer. Notice the 3 sits with $\mathbf{a}$ and the 2 sits with $\mathbf{b}$ — the weights are **swapped** relative to the ratio. Sanity check: as $m \to 0$, the formula gives $\vec{OP} \to \mathbf{a}$, which is correct because $P$ coincides with $A$. ✓

### Example 4 (0606 level): Compound problem

In triangle $OAB$, $\vec{OA} = \mathbf{a}$ and $\vec{OB} = \mathbf{b}$. $M$ is the midpoint of $AB$, and $N$ lies on $OM$ such that $ON : NM = 2 : 1$. Show that $N$ is the **centroid** of triangle $OAB$ (the intersection of the three medians).

**Solution.**

Midpoint $M$: $\quad \mathbf{m} = \tfrac{1}{2}(\mathbf{a} + \mathbf{b})$.

$N$ divides $OM$ in the ratio $2 : 1$, so $N$ is $\tfrac{2}{3}$ of the way from $O$ to $M$:
$$\mathbf{n} = \tfrac{2}{3}\mathbf{m} = \tfrac{2}{3} \cdot \tfrac{1}{2}(\mathbf{a} + \mathbf{b}) = \tfrac{\mathbf{a} + \mathbf{b}}{3}$$

The centroid formula for triangle $OAB$ (with vertices $O$, $A$, $B$ having position vectors $\mathbf{0}$, $\mathbf{a}$, $\mathbf{b}$) is
$$\mathbf{g} = \frac{\mathbf{0} + \mathbf{a} + \mathbf{b}}{3} = \frac{\mathbf{a} + \mathbf{b}}{3}$$

$\mathbf{n} = \mathbf{g}$, so $N$ is the centroid. $\blacksquare$

Bonus observation: $N$ is $\tfrac{2}{3}$ of the way from vertex $O$ along the median to $M$. The **2:1 centroid property** of medians — each median is divided by the centroid in the ratio 2:1 from vertex to opposite side — falls out naturally.

## Common Misconceptions (Teaching Notes)

### 1. Section formula — which weight goes with which vector

Students with $AP : PB = 2 : 3$ write $\mathbf{p} = \tfrac{2\mathbf{a} + 3\mathbf{b}}{5}$ — putting the 2 with $\mathbf{a}$ because "2 comes first." Wrong.

**Fix:** The weights **swap**. Always do a sanity check: "if the ratio collapses so $P = A$, does my formula give $\mathbf{p} = \mathbf{a}$?" With $AP:PB = 0:k$, $P = A$. Plug $m = 0$ into $\mathbf{p} = (n\mathbf{a} + m\mathbf{b})/(m+n)$: get $\mathbf{p} = \mathbf{a}$. ✓ If your formula fails this check, the weights are swapped.

### 2. Confusing points with position vectors

Students write things like "$P = 3\mathbf{a} + 2\mathbf{b}$" treating the point $P$ as a vector.

**Fix:** Be pedantic. The point is $P$; its position vector is $\vec{OP}$ or $\mathbf{p}$. Write $\vec{OP} = 3\mathbf{a} + 2\mathbf{b}$. This matters because points and vectors are different types — in programming terms, one is a location and the other is a displacement, and you can add two displacements but you cannot add two locations.

### 3. Forgetting that $\vec{AB} = \mathbf{b} - \mathbf{a}$ is "end minus start"

Students write $\vec{AB} = \mathbf{a} - \mathbf{b}$ instead.

**Fix:** Mnemonic: **"end minus start"** (终点减起点). Double-check with a number line — if $A = 1$ and $B = 5$, the displacement from $A$ to $B$ is $+4$, not $-4$, so it's $B - A = 5 - 1$.

### 4. Direction of $\vec{AB}$ vs $\vec{BA}$

Students confuse which way a displacement points.

**Fix:** The letters read like a journey: $\vec{AB}$ starts at $A$, ends at $B$; $\vec{BA}$ is the reverse. They are negatives: $\vec{BA} = -\vec{AB}$. In component form, this swaps signs on every component.

## Exam Notes

### OxAQA 9260

Syllabus: **G22** (Core) — "solve simple geometrical problems in 2D using vector methods."

Typical question: "Given that $\vec{OA} = \mathbf{a}$ and $\vec{OC} = \mathbf{c}$, find $\vec{AC}$ in terms of $\mathbf{a}$ and $\mathbf{c}$. Given that $M$ is the midpoint of $AC$, find $\vec{OM}$. Show that $X$, $M$, $Y$ are collinear."

Strategy: apply the three-step vector proof strategy above. Each displacement gets 1 mark; the final collinearity/midpoint conclusion gets 1–2 marks.

### Cambridge 0580 Extended

Syllabus: **E7.4** — "position vectors; represent and use vectors to prove geometrical results (parallel, collinear, similar, ratio)."

Classic question structure: a diagram with $\mathbf{a}$ and $\mathbf{b}$ marked, then parts (a)(i), (a)(ii), … asking for $\vec{AB}$, $\vec{AM}$, $\vec{OM}$, building towards "hence show that $X$, $Y$, $Z$ are collinear" or "hence find the ratio $AP : PB$." Mark allocation: 1 mark per vector expression, 2–3 marks for the concluding geometric claim.

### Cambridge 0606

Syllabus: **13.2** (position vectors, unit vectors applied in geometry) and **13.4** (velocity vectors — composition, resolution, relative velocity).

Topic 13.4 is the distinctive 0606 content: vectors as physical velocities (boat in current, plane in wind), resolving into components along given directions, finding resultant speed and bearing. This is a direct hand-off to A-Level Mechanics.

### A-Level

Vector geometry at A-Level extends to:
- **Scalar (dot) product** $\mathbf{a} \cdot \mathbf{b} = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \cos\theta$, giving the angle between two vectors
- **Vector equations of lines** $\mathbf{r} = \mathbf{a} + t\mathbf{d}$
- **3D geometry** — lines and planes in space
- **Mechanics** — forces in equilibrium, resolving into components

### IB AA / AI

**Topic 3 — Geometry and trigonometry.** IB goes further than Cambridge: scalar product, angle between vectors, applications to geometry. AA HL extends to 3D lines and planes.

## Connections

- **Parent:** [[Vectors]] — every tool here (addition, subtraction, scalar multiplication, magnitude) is from the Vectors card
- **Bridge:** [[Cartesian Coordinates (Vocab)]] — position vectors ARE coordinates wearing vector clothes
- **Proof technique:** [[Geometrical Proof]] — classical Euclidean arguments translated into vector algebra
- **Application:** [[Matrix Transformations]] — matrices act on position vectors to produce rotations, reflections, enlargements
- **Extensions:** [[3D Vectors]] — same algebra, third component $z$
- **Related tools:** [[Similarity]] — scalar multiplication is the vector form of enlargement; [[Congruence]] — equal vectors encode side-and-angle equality
- **Physics bridge:** velocity, force, momentum, torque — vector geometry is the mathematical backbone of mechanics

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\vec{OP}$ | `\vec{OP}` | Position vector of point $P$ |
| $\mathbf{p}$ | `\mathbf{p}` | Shorthand for position vector (bold, lowercase of point label) |
| $\vec{AB} = \mathbf{b} - \mathbf{a}$ | `\vec{AB} = \mathbf{b} - \mathbf{a}` | Master identity — "end minus start" |
| $\mathbf{p} = \dfrac{n\mathbf{a} + m\mathbf{b}}{m+n}$ | `\dfrac{n\mathbf{a} + m\mathbf{b}}{m+n}` | Section formula (weights swap!) |
| $\mathbf{g} = \dfrac{\mathbf{a}+\mathbf{b}+\mathbf{c}}{3}$ | `\dfrac{\mathbf{a}+\mathbf{b}+\mathbf{c}}{3}` | Centroid of triangle |
| $\mathbf{v}_{A \text{ rel } B}$ | `\mathbf{v}_{A \text{ rel } B}` | Relative velocity |
| $\parallel$ | `\parallel` | "is parallel to" |
