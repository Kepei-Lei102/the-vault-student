---
chinese: 拉格朗日恒等式 (Lāgélǎngrì héngděngshì)
prerequisites:
  - "[[3D Vectors and the Scalar Product]]"
  - "[[Cross Product]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/linear-algebra
  - domain/inequalities
  - level/university
  - type/theorem
  - type/proof
  - notation/summation
  - misconception/equality-case
  - misconception/correlation-is-agreement
---

# Lagrange's Identity 拉格朗日恒等式

Two arrows of fixed lengths open like a pair of scissors. Their alignment changes; so does the area between them. What stays fixed?

In three dimensions, the answer is

$$\underbrace{(\mathbf a\cdot\mathbf b)^2}_{\text{squared alignment}}+\underbrace{\lVert\mathbf a\times\mathbf b\rVert^2}_{\text{squared area}}=\lVert\mathbf a\rVert^2\lVert\mathbf b\rVert^2.$$

That is the familiar $\cos^2\theta+\sin^2\theta=1$ relationship in vector form. But the more surprising result survives when an arrow has **a thousand coordinates**, where the usual cross product is unavailable.

## Definition

### Formal

For any real vectors $\mathbf a=(a_1,\ldots,a_n)$ and $\mathbf b=(b_1,\ldots,b_n)$,

$$\boxed{\left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right)-\left(\sum_{i=1}^n a_i b_i\right)^2=\sum_{1\le i<j\le n}(a_i b_j-a_j b_i)^2.}$$

This is **Lagrange's identity**. It is an equality, with no approximation and no requirement that the vectors be non-zero.

### Intuitive

Pick any two coordinate positions, $i$ and $j$. The number $a_i b_j-a_j b_i$ measures the signed area spanned by the two vectors when projected onto that coordinate plane. Square those areas and add them: the result is exactly the gap between the product of squared lengths and the squared dot product.

**Perfect alignment leaves no area. Any departure from a common line leaves a non-negative gap.** Opposite directions also lie on a common line: the square forgets the sign of alignment.

### 中文锚点

把两根筷子的一端放在同一点，像剪刀一样慢慢张开。筷子的长度没变，但在张到直角之前，越张开，它们围出的平行四边形就越宽；同时，一根沿着另一根方向留下的“影子”变短了。拉格朗日恒等式说，这两种变化正好互相补齐：把“对齐的程度”和“张开的面积”各自平方，再加起来，总量不变。到直角时，影子消失，面积最大；继续张开，影子转到反方向，平方之后仍然是正数。它把同一个动作的两面，接成了一笔始终对得上的账。

## Notation — count each pair once

| Symbol | Meaning |
|---|---|
| $\lVert\mathbf a\rVert^2=\sum a_i^2$ | Squared Euclidean length |
| $\mathbf a\cdot\mathbf b=\sum a_i b_i$ | Dot product |
| $\sum_{i<j}$ | Sum over each distinct pair of coordinate positions once |
| $a_i b_j-a_j b_i$ | A $2\times2$ determinant; signed projected area |

For $n=3$, the pairs are $(1,2),(1,3),(2,3)$. For $n=4$, there are six pairs. Generally there are $\binom n2=n(n-1)/2$ terms. For $n=1$, the sum is empty and equals zero.

> [!warning] Coordinates, not observations in a plane
> A vector with $n$ coordinates can represent $n$ measurements. The coordinate-plane areas in the identity then refer to pairs of entries in those vectors. They are not the triangles you happen to see on a scatter plot of the original data.

## 1. Prove it by collecting pairs

The trigger is the difference of **a product of sums of squares** and **a squared sum of products**. Expand them together: their matching terms are meant to cancel.

**Step 1 — Tool: distributivity.** Expand the first product, separating equal indices from unequal ones:

$$\left(\sum_i a_i^2\right)\left(\sum_j b_j^2\right)=\sum_i a_i^2b_i^2+\sum_{i<j}(a_i^2b_j^2+a_j^2b_i^2).$$

Each unordered pair $\{i,j\}$ contributes twice to the original product: once as $(i,j)$ and once as $(j,i)$. That explains the two terms in each bracket.

**Step 2 — Tool: square of a sum.** Do the same for the dot product:

$$\left(\sum_i a_i b_i\right)^2=\sum_i a_i^2b_i^2+2\sum_{i<j}a_i b_i a_j b_j.$$

**Step 3 — Tool: subtraction followed by a perfect square.** The diagonal sums cancel. Each remaining pair becomes

$$a_i^2b_j^2+a_j^2b_i^2-2a_i b_i a_j b_j=(a_i b_j-a_j b_i)^2.$$

Adding those pairwise squares proves the identity. $\square$

The mechanism is small: **cancel the diagonal; pair the off-diagonal terms**. Increasing the dimension adds more pairs, but introduces no new kind of algebra.

## 2. Read the geometry in two and three dimensions

### Two dimensions — one area

For $\mathbf a=(a_1,a_2)$ and $\mathbf b=(b_1,b_2)$, there is only one pair:

$$\lVert\mathbf a\rVert^2\lVert\mathbf b\rVert^2-(\mathbf a\cdot\mathbf b)^2=(a_1b_2-a_2b_1)^2.$$

The determinant on the right is the signed area of the parallelogram. See [[Determinants and Inverses]] for its area interpretation.

### Three dimensions — three projected areas

The cross product has components

$$\mathbf a\times\mathbf b=(a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1).$$

Squaring and adding produces precisely the three squares in Lagrange's identity. The middle component has the opposite sign to the $(1,3)$ minor, which disappears on squaring.

Thus **the square of the parallelogram's area equals the sum of the squares of its three coordinate-plane projection areas**. This is an area version of Pythagoras: add squared projections, not ordinary areas.

![[lagrange-identity-geometry.svg|760]]
*Left: two unit vectors at $60^\circ$ span area $\sin60^\circ$. Right: as their angle changes, the squared dot product and squared area always sum to 1. Beyond $90^\circ$, the dot product is negative, but its square is positive.*

![[lagrange-identity-manim.mp4]]
*Follow the same two arrows through alignment, a right angle and opposite alignment; then watch the identity become an inequality and a statement about data.*

## 3. Cauchy–Schwarz, including exactly when equality holds

Every term on the right is a square of a real number, so the sum cannot be negative:

$$\boxed{|\mathbf a\cdot\mathbf b|\le\lVert\mathbf a\rVert\,\lVert\mathbf b\rVert.}$$

This is the **Cauchy–Schwarz inequality** for real Euclidean vectors. The identity tells us both that the bound holds and **how far from equality** we are, in squared form.

When does equality hold? A sum of non-negative squares is zero exactly when every square is zero:

$$a_i b_j-a_j b_i=0\qquad\text{for every }i<j.$$

If $\mathbf a\ne\mathbf0$, choose an index $k$ with $a_k\ne0$. The condition for the pair containing $k$ and any other index $j$ gives

$$a_kb_j-a_jb_k=0\quad\Longrightarrow\quad b_j=\frac{b_k}{a_k}a_j.$$

The same factor $b_k/a_k$ works for **every coordinate**. Therefore $\mathbf b=\lambda\mathbf a$. Conversely, proportional vectors make every minor zero. If either vector is zero, equality also holds.

**Equality means the two vectors are linearly dependent**: non-zero vectors point along the same line, possibly in opposite directions; zero vectors are included without inventing a direction for them.

> [!tip] Why an angle can be defined in any real dimension
> For non-zero vectors, Cauchy–Schwarz puts $(\mathbf a\cdot\mathbf b)/(\lVert\mathbf a\rVert\lVert\mathbf b\rVert)$ in $[-1,1]$. We can therefore define its inverse cosine as the angle. The algebra proves this definition is possible; we did not assume an angle first to prove the inequality.

## 4. Worked example — a bound that gives its own equality case

Suppose $x^2+y^2+z^2=9$. Find the greatest possible value of $2x-y+2z$.

**Tool: recognise a dot product. Trigger: a linear expression with a fixed sum of squares.** Use $\mathbf a=(2,-1,2)$ and $\mathbf b=(x,y,z)$. Both have length 3.

**Tool: Cauchy–Schwarz.**

$$|2x-y+2z|\le 3\times3=9.$$

**Tool: the equality condition. Trigger: an upper bound alone does not prove it can be reached.** Set $\mathbf b=\lambda\mathbf a$. The length constraint gives $9\lambda^2=9$, hence $\lambda=\pm1$.

For $\lambda=1$, $(x,y,z)=(2,-1,2)$ and the expression is 9. For $\lambda=-1$, it is $-9$. So the maximum is **9**, and the minimum is **−9**.

The identity exposes the gap explicitly:

$$81-(2x-y+2z)^2=(x+2y)^2+(2z-2x)^2+(-z-2y)^2.$$

No guessing: equality forces all three mismatches to vanish.

## 5. Where it works — correlation and fitting sensor readings

When two sensors respond to the same changing input, an engineer may compare their paired readings. Do they rise and fall together, even if their zero points or gains differ? [[Scatter Diagrams|Pearson correlation]] measures that linear association.

First remove the separate averages:

$$a_i=x_i-\bar x,\qquad b_i=y_i-\bar y.$$

For two non-constant data sets, their Pearson coefficient is

$$r=\frac{\sum_i a_i b_i}{\sqrt{\sum_i a_i^2\sum_i b_i^2}}.$$

The denominator removes the overall scales. Lagrange's identity says exactly why this normalisation cannot produce a magnitude greater than 1:

$$\boxed{1-r^2=\frac{\sum_{i<j}(a_i b_j-a_j b_i)^2}{\lVert\mathbf a\rVert^2\lVert\mathbf b\rVert^2}\ge0.}$$

This is a real constraint on the number a spreadsheet or measurement script reports. Equality means every centred reading in one set is the same multiple of its partner: the original data lie exactly on a non-horizontal straight line.

### A small calibration example

Use these **illustrative**, not experimentally collected, paired readings:

| Reading | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Reference $x$ (V) | 1 | 2 | 3 | 4 |
| Sensor $y$ (V) | 2 | 4 | 4 | 6 |

**Tool: centring. Trigger: offsets should not decide whether the variations line up.** The means are $\bar x=2.5$ and $\bar y=4$, giving

$$\mathbf a=(-1.5,-0.5,0.5,1.5),\qquad\mathbf b=(-2,0,0,2).$$

**Tool: dot products and squared lengths.** We get $\mathbf a\cdot\mathbf b=6$, $\lVert\mathbf a\rVert^2=5$ and $\lVert\mathbf b\rVert^2=8$. Hence

$$r=\frac6{\sqrt{40}}\approx0.9487,\qquad r^2=0.9.$$

**Tool: Lagrange's identity as a cross-check.** The six minors, in order $(12,13,14,23,24,34)$, are $(-1,1,0,0,-1,1)$. Their squares sum to 4, agreeing with $5\times8-6^2=4$.

### The same gap is the least-squares residual

Recall that centring has removed the intercept. To fit the centred sensor vector by a multiple $c\mathbf a$ of the reference, minimise

$$\lVert\mathbf b-c\mathbf a\rVert^2=\lVert\mathbf b\rVert^2-2c(\mathbf a\cdot\mathbf b)+c^2\lVert\mathbf a\rVert^2.$$

**Tool: complete the square. Trigger: the unknown coefficient occurs quadratically.**

$$=\lVert\mathbf a\rVert^2\left(c-\frac{\mathbf a\cdot\mathbf b}{\lVert\mathbf a\rVert^2}\right)^2+\lVert\mathbf b\rVert^2-\frac{(\mathbf a\cdot\mathbf b)^2}{\lVert\mathbf a\rVert^2}.$$

The first term can be zero. The second is the minimum residual sum of squares, so

$$c=\frac65=1.2,\qquad \widehat y=\bar y+c(x-\bar x)=1+1.2x,$$

$$\mathrm{SSE}=8-\frac{36}{5}=0.8=8(1-r^2).$$

For ordinary least squares with **one predictor and an intercept**, $r^2$ is the fraction of the centred response sum of squares accounted for by the fitted line. Here 90% is accounted for and 10% remains as residual variation. This identity is not a universal definition of $R^2$ for every possible model.

![[lagrange-identity-correlation.svg|760]]
*The fitted line and its four vertical residuals. Their squared lengths sum to $0.8\ \mathrm{V}^2$. The algebraic mismatch and the visible fitting error are the same quantity after division by $\lVert\mathbf a\rVert^2=5\ \mathrm{V}^2$.*

**Correlation is not agreement.** A sensor reporting $y=100+2x$ has $r=1$ for any non-constant input, yet disagrees systematically with the reference. Offsets, gain error and measurement uncertainty still need checking. Nor does correlation establish causation.

## 6. Hands-on — test the gap, then break the assumptions

Run this with Python and NumPy. Predict the result before changing `y`.

```python
import numpy as np
from itertools import combinations

x = np.array([1., 2., 3., 4.])
y = np.array([2., 4., 4., 6.])
a, b = x - x.mean(), y - y.mean()
aa, bb, ab = a @ a, b @ b, a @ b
gap = sum((a[i]*b[j] - a[j]*b[i])**2
          for i, j in combinations(range(len(a)), 2))
assert np.isclose(aa*bb - ab**2, gap)
if aa == 0 or bb == 0:
    print("Correlation is undefined: a data set is constant.")
else:
    r = ab / np.sqrt(aa*bb)
    fitted = y.mean() + (ab/aa)*a
    sse = np.sum((y - fitted)**2)
    assert np.isclose(sse, gap/aa)
    print(f"r={r:.6f}, r²={r*r:.6f}, SSE={sse:.6f}")
```

Output: `r=0.948683, r²=0.900000, SSE=0.800000`.

Try `y = 100 + 2*x` (perfect positive association), `y = 100 - 2*x` (perfect negative association), then `y = np.ones(4)` (no variation, so no defined correlation). For nearly proportional large vectors, subtracting two almost equal floating-point quantities can lose accuracy; a tiny negative computed gap is rounding, not a counterexample to the theorem.

## 7. Beyond syllabus — Gram determinants and Binet–Cauchy

Recall that a $2\times2$ determinant measures signed area. Put the two vectors into the columns of an $n\times2$ matrix $A$. Its **Gram matrix** records all pairwise dot products:

$$A^TA=\begin{pmatrix}\mathbf a\cdot\mathbf a&\mathbf a\cdot\mathbf b\\\mathbf b\cdot\mathbf a&\mathbf b\cdot\mathbf b\end{pmatrix}.$$

Its determinant is exactly the left-hand side of Lagrange's identity. Thus

$$\det(A^TA)=\sum_{i<j}\det(A_{ij})^2,$$

where $A_{ij}$ consists of rows $i,j$ of $A$. This reads: **squared area equals the sum of squared coordinate-projection areas**, even in $n$ dimensions. One geometric justification: subtract from $\mathbf b$ its projection onto non-zero $\mathbf a$; base times the length of the perpendicular remainder gives the parallelogram area, whose square is the Gram determinant. If $\mathbf a=0$, both are zero.

The two-column **Binet–Cauchy identity** allows different vectors on the two sides:

$$\begin{aligned}(\mathbf a\cdot\mathbf c)(\mathbf b\cdot\mathbf d)-(\mathbf a\cdot\mathbf d)(\mathbf b\cdot\mathbf c)\\=\sum_{i<j}(a_i b_j-a_j b_i)(c_i d_j-c_j d_i).\end{aligned}$$

To prove it, expand the two products on the left. Terms with $i=j$ cancel. Grouping $(i,j)$ with $(j,i)$ leaves

$$a_i b_j c_i d_j+a_j b_i c_j d_i-a_i b_j d_i c_j-a_j b_i d_j c_i,$$

which factors into the corresponding summand on the right. Setting $\mathbf c=\mathbf a$ and $\mathbf d=\mathbf b$ recovers Lagrange's identity.

The broader Cauchy–Binet theorem replaces the two-column matrices by matrices with more columns and sums products of larger minors. That is the route from area to volume; it is not an ordinary higher-dimensional cross product.

## Common misconceptions

- **“The right side is a sum over all ordered pairs.”** Use $i<j$, or put a factor $\tfrac12$ before the sum over all $i,j$; otherwise every non-zero square is counted twice.
- **“Equality means identical vectors.”** Proportional is enough, including a negative factor; either zero vector also gives equality.
- **“A positive gap proves a positive dot product.”** Squaring erased that sign. Keep the unsquared dot product to distinguish positive and negative correlation.
- **“The formula works unchanged for complex coordinates.”** The displayed version assumes real entries. Complex inner products need conjugation and squared moduli; ordinary squares need not be non-negative.
- **“This is the Lagrange multiplier method.”** Different result, same mathematician's name. There is no constraint multiplier in the proof above.

## Exam Notes

### A-Level — vector companion, with a boundary

Cambridge **9231 §1.6** examines the component and geometric forms of the vector product and their use in geometry. **Edexcel IAL FP3 §5.1** examines vector and scalar triple products. The three-dimensional identity helps check those calculations; neither specification names the general $n$-dimensional identity or its proof as a required result.

Cambridge **9709 P3 §3.7** and OxfordAQA **9660 P2.10** examine scalar products; 9709 explicitly excludes the vector product. Their vector requirements do not turn the general identity into a separate examinable theorem. Use [[MF19 Reference (9709)]] and [[Edexcel IAL Reference]] for which vector formulas are supplied and which must be recalled; the general theorem here is enrichment, not an extra memorisation demand.

### IB and AP — applications versus proof

In IB Mathematics AA (first assessment 2021), **AHL 3.13/3.16** cover scalar/vector products. AA and AI **SL 4.4** cover Pearson correlation and linear regression. The general identity and its proof are enrichment beyond those outcomes; knowing the coefficient's interpretation is a different requirement from proving its bound.

AP Statistics **Unit 5, Regression Analysis** in the course effective Fall 2026 covers correlation and linear regression. Lagrange's identity supplies an explanation of their algebra, not a named course theorem. AP Calculus AB/BC does not list this identity; the BC **Lagrange error bound** is an unrelated Taylor-series result.

### Where the general theorem is not prescribed

It is not a named required result in Cambridge **0580, 0606, 9709 or 9231**, OxfordAQA **9260 or 9660**, **Edexcel IAL Mathematics/Further Mathematics**, **IB AA/AI**, or **AP Calculus AB/BC and AP Statistics** in the specifications above. Ordinary algebra, vector geometry or correlation may still be examined. An unfamiliar identity can also be supplied in a question: “not prescribed” does not mean “can never appear”.

## Connections

- **Parents:** [[3D Vectors and the Scalar Product]], [[Cross Product]] — alignment and area are the two geometric ingredients.
- **Matrix view:** [[Determinants and Inverses]] — the small determinants are projected areas; the Gram determinant packages the whole area.
- **Application:** [[Scatter Diagrams]] — Pearson correlation is a normalised dot product of centred data.
- **Further use:** [[Fourier Series]] — projection onto perpendicular directions underlies least-squares approximation there too.
- **Proof habit:** [[Chain of Thought]] — a fixed sum of squares selects Cauchy–Schwarz; a difference of matching products selects cancellation.

## Sources and further reading

- [NIST Dataplot: correlation](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm) and [SciPy: Pearson correlation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html) — the computational formula and the constant-input boundary.
- [Robert Greene, UCLA: Cauchy–Schwarz using Lagrange's identity](https://www.math.ucla.edu/~greene/CauchySchwartz%20and%20other%20stuff%20Math120A.pdf).
- [IB Mathematics AA guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf) and [AI guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-applications-and-interpretation-guide-en.pdf), first assessment 2021.
- [College Board: AP Statistics course description, effective Fall 2026](https://apcentral.collegeboard.org/media/pdf/ap-statistics-course-and-exam-description.pdf), Unit 5.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\lVert\mathbf a\rVert$ | `\lVert\mathbf a\rVert` | Vector length |
| $\sum_{i<j}$ | `\sum_{i<j}` | Each coordinate pair once |
| $\mathbf a\cdot\mathbf b$ | `\mathbf a\cdot\mathbf b` | Dot product |
| $\det(A^TA)$ | `\det(A^TA)` | Gram determinant |
| $\widehat y$ | `\widehat y` | Fitted response |
