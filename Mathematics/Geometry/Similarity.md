---
chinese: 相似 (xiāngsì)
prerequisites:
  - "[[Triangles (Vocab)]]"
  - "[[Angles in Parallel Lines (Vocab)]]"
  - "[[Congruence]]"
  - "[[Transformations (Vocab)]]"
  - "[[Fractions (Vocab)]]"
  - "[[Circle Theorems I]]"
  - "[[Circle Theorems II]]"
  - "[[Polygon Angles (Vocab)]]"
  - "[[Ratio (Vocab)]]"
leads_to:
  - "[[Trigonometric Ratios]]"
  - "[[Pythagoras Theorem]]"
  - "[[Matrix Transformations]]"
  - "[[Geometrical Proof]]"
  - "[[Vector Geometry]]"
  - "[[Connected Rates of Change]]"
  - "[[Scale Drawings (Vocab)]]"
  - "[[Vectors]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE-extension
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/9260-G7
  - syllabus/9260-G17
  - syllabus/0580-E4-4
  - type/definition
  - type/theorem
  - type/proof
  - notation/similar
  - notation/triangle
  - misconception/aaa-fails-for-congruence-but-works-for-similarity
  - misconception/scale-factor-for-area-volume
  - misconception/wrong-vertex-order
---

# Similarity 相似

## Definition

### Formal

Two figures are **similar** if one can be mapped onto the other by a sequence of rigid motions (translations, rotations, reflections) composed with a single **enlargement** by a positive scale factor $k$. Equivalently:

> Corresponding angles are equal **and** corresponding sides are in the same ratio $k$.

For two triangles this is written:

$$\triangle ABC \sim \triangle DEF$$

The vertex order encodes the correspondence $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$. The statement asserts six facts simultaneously:

$$\angle A = \angle D, \quad \angle B = \angle E, \quad \angle C = \angle F$$
$$\frac{DE}{AB} = \frac{EF}{BC} = \frac{FD}{CA} = k$$

The number $k$ is the **scale factor** (also called the **ratio of similitude**).

### Intuitive

Same shape, possibly different size. Take a photo of a triangle and print it larger — every angle stays the same, every length gets multiplied by the same factor. Congruence is the special case $k = 1$: a photo printed at 100%.

### 中文锚点

**相似 (xiāngsì) vs 全等 (quánděng).** 相似 = 形状相同，大小可不同；全等 = 相似 且 $k = 1$.

Chinese students meet 相似三角形 systematically in 初中 (middle school). Three conditions taught: 两角对应相等 (AA), 两边成比例夹角相等 (SAS), 三边对应成比例 (SSS). Also meet 平行线分线段成比例定理 (Basic Proportionality Theorem) before high school.

English exam vocabulary to watch: "similar" (not "same"), "scale factor" (not "ratio" alone — be precise), "corresponding sides", "enlargement".

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Similarity | $\sim$ | "is similar to" | Same shape, possibly different size |
| Congruence | $\cong$ | "is congruent to" | Special case of similar with $k = 1$ |
| Scale factor | $k$ | — | Cambridge/OxAQA; also written $r$ in some texts |
| Scale factor (中文) | 相似比 | "similarity ratio" | Chinese textbooks |
| Ratio statement | $AB : DE = 2 : 3$ | "$AB$ to $DE$ is 2 to 3" | Means $\dfrac{AB}{DE} = \dfrac{2}{3}$ |

> [!warning] Vertex order matters
> Writing $\triangle ABC \sim \triangle DEF$ simultaneously asserts $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$. If you write $\triangle ABC \sim \triangle EDF$ instead, you've asserted a *different* correspondence — and probably a false one. Always match vertex order to the correspondence you mean.

## The Four Similarity Conditions for Triangles

For two triangles to be similar, you need **one** of the following. Each is sufficient on its own.

### 1. AA — Two pairs of equal angles

If $\angle A = \angle D$ and $\angle B = \angle E$, then $\triangle ABC \sim \triangle DEF$.

**Why it works.** Angle sum in a triangle is $180°$, so the third pair is forced equal too. Once all angles match, the triangles are enlargements of each other — there is a unique "shape" with those three angles, up to scaling.

### 2. SSS — Three pairs of sides in the same ratio

If $\dfrac{DE}{AB} = \dfrac{EF}{BC} = \dfrac{FD}{CA}$, then $\triangle ABC \sim \triangle DEF$.

**Why it works.** Scale $\triangle DEF$ down by the common ratio. The result has the same three side lengths as $\triangle ABC$, so it is congruent to $\triangle ABC$ by the SSS congruence condition. Since $\triangle DEF$ is obtained from $\triangle ABC$ by an enlargement followed by a rigid motion, the triangles are similar.

### 3. SAS — Two sides in ratio with equal included angle

If $\dfrac{DE}{AB} = \dfrac{EF}{BC}$ **and** $\angle B = \angle E$ (the included angles), then $\triangle ABC \sim \triangle DEF$.

**Why it works.** Same argument: scale $\triangle DEF$ down until $D'E' = AB$ and $E'F' = BC$. The scaled triangle matches $\triangle ABC$ by SAS congruence.

### 4. RHS — Right angle, hypotenuse, and one side in ratio

If both triangles have a right angle, and the ratios $\dfrac{\text{hyp}_2}{\text{hyp}_1} = \dfrac{\text{leg}_2}{\text{leg}_1}$ match, then similar. Follows from Pythagoras + SSS similarity.

> [!tip] AAA fails for congruence but works for similarity
> Three equal angles *don't* guarantee congruent triangles — two equilateral triangles with $60°$ angles can be hand-sized or football-field-sized (see [[Congruence]]). But that difference in size is exactly what similarity *allows*. Three equal angles guarantee similar triangles, which is the same information as AA (since the third angle is forced by $\angle A + \angle B + \angle C = 180°$). So for similarity, AAA collapses to AA. This is the cleanest way to see that similarity is the "natural" relaxation of congruence: it throws away the size condition and keeps the shape.

## Scale Factor Laws

If two similar figures have linear scale factor $k$, then:

$$\boxed{\text{lengths scale by } k, \quad \text{areas scale by } k^2, \quad \text{volumes scale by } k^3}$$

![[similarity-scaling-laws.svg|697]]

### Proof — Areas scale by $k^2$

Start with a rectangle of dimensions $a \times b$, so area $= ab$. Enlarge by factor $k$. New dimensions $ka \times kb$, new area $= (ka)(kb) = k^2 \cdot ab$.

Any region can be approximated to arbitrary accuracy by a grid of small rectangles. Every rectangle scales the same way, so total area scales by $k^2$.

### Proof — Volumes scale by $k^3$

Same argument in 3D. A box of dimensions $a \times b \times c$ has volume $abc$; enlarged by $k$, it becomes $ka \times kb \times kc$ with volume $k^3 abc$. Any solid decomposes into tiny boxes, so volume scales by $k^3$.

> [!info] The strict proof is integration
> "Approximating by a grid of rectangles" is exactly the Riemann-sum idea that defines the [[Integration|integral]]. The rigorous proof — valid for any region with a well-defined area, not just rectangles — is the change-of-variables formula:
> $$\iint_{kR} 1 \, dA = k^2 \iint_R 1 \, dA$$
> where $kR$ denotes the region $R$ enlarged by factor $k$. The factor $k^2$ falls out of the Jacobian determinant of the scaling map. The 3D version gives $k^3$ via a triple integral. The same machinery justifies the scaling law for *any* shape — spheres, cones, irregular blobs — not just rectangles and boxes. Students meet this formally in first-year university calculus. (See [[Integration]] — to be written.)

### Using the laws in both directions

| Given | Find | Key step |
|---|---|---|
| Linear ratio $k$ | Area ratio | Square it: $k^2$ |
| Linear ratio $k$ | Volume ratio | Cube it: $k^3$ |
| Area ratio | Linear ratio | Square root: $\sqrt{\cdot}$ |
| Volume ratio | Linear ratio | Cube root: $\sqrt[3]{\cdot}$ |
| Volume ratio | Area ratio | Cube root, then square: $(\sqrt[3]{\cdot})^2$ |

> [!info] Beyond syllabus — The square-cube law
> Galileo wrote about this in *Two New Sciences* (1638). If you double the linear size of an animal, its weight (which scales with volume) increases by factor $8$, but its bone cross-sectional area (which supports that weight) only increases by factor $4$. Large animals need *proportionally thicker* bones — that's why elephants have columnar legs and mice have twiggy ones, and why a mouse scaled to elephant size would collapse under its own weight.
>
> The same logic governs heat loss (surface area, $k^2$) vs. heat generation (volume, $k^3$), which explains why small mammals eat constantly and large mammals can go longer between meals. It's literally the scaling laws the student just proved, applied to a living system.

## Basic Proportionality Theorem (BPT)

Also called **Thales' Intercept Theorem** or 平行线分线段成比例定理.

**Statement.** If a line parallel to side $BC$ of $\triangle ABC$ cuts $AB$ at $D$ and $AC$ at $E$, then:

$$\frac{AD}{DB} = \frac{AE}{EC} \qquad \text{equivalently} \qquad \frac{AD}{AB} = \frac{AE}{AC}$$

![[similarity-bpt.svg|689]]

**Proof via AA similarity.**

Step 1. $\angle A$ is common to $\triangle ADE$ and $\triangle ABC$.

Step 2. $DE \parallel BC$, so $\angle ADE = \angle ABC$ (corresponding angles, as in [[Angles in Parallel Lines (Vocab)|Angles in Parallel Lines]]).

Step 3. Two pairs of equal angles ⇒ $\triangle ADE \sim \triangle ABC$ by AA.

Step 4. Therefore $\dfrac{AD}{AB} = \dfrac{AE}{AC}$. Cross-multiply / rearrange to get $\dfrac{AD}{DB} = \dfrac{AE}{EC}$. $\blacksquare$

### Corollary — Midsegment Theorem

If $D$ and $E$ are midpoints of $AB$ and $AC$, then $DE \parallel BC$ **and** $DE = \frac{1}{2}BC$.

### Application — Altitude to the hypotenuse

In a right triangle, dropping the altitude from the right angle to the hypotenuse creates **two smaller triangles, each similar to the original**. This gives:
- **Geometric mean relation:** $h^2 = pq$, where $p$, $q$ are the segments of the hypotenuse and $h$ is the altitude.
- **Similar-triangles proof of Pythagoras:** $a^2 = pc$ and $b^2 = qc$, so $a^2 + b^2 = (p + q)c = c^2$. (See [[Pythagoras Theorem]].)

## Worked Examples

### Example 1 (9260 level) — Find the missing side

$\triangle ABC \sim \triangle PQR$ with $AB = 6$ cm, $BC = 8$ cm, $PQ = 9$ cm. Find $QR$.

**Solution.** Vertex correspondence gives $\dfrac{PQ}{AB} = \dfrac{QR}{BC}$, so
$$\frac{9}{6} = \frac{QR}{8} \quad \Rightarrow \quad QR = \frac{9 \times 8}{6} = 12 \text{ cm}.$$

Scale factor $k = \dfrac{9}{6} = 1.5$, so every length in $\triangle PQR$ is $1.5$ times the corresponding length in $\triangle ABC$.

### Example 2 (9260 Extension / 0580 Extended) — Volume scaling

Two similar cones have volumes $V_1 = 54$ cm³ and $V_2 = 128$ cm³. The radius of the first cone is $3$ cm. Find the radius of the second.

**Solution.** Volumes are in ratio $\dfrac{V_2}{V_1} = \dfrac{128}{54} = \dfrac{64}{27}$.

Cube-root to get the linear scale factor: $k = \sqrt[3]{\dfrac{64}{27}} = \dfrac{4}{3}$.

So radius of cone 2 is $3 \times \dfrac{4}{3} = 4$ cm.

### Example 3 (0606-level reasoning) — BPT application

In $\triangle ABC$, $D$ is on $AB$ and $E$ on $AC$ with $DE \parallel BC$. Given $AD = 4$, $DB = 6$, $AE = 3$. Find $AC$.

**Solution.** BPT gives $\dfrac{AD}{DB} = \dfrac{AE}{EC}$, so $\dfrac{4}{6} = \dfrac{3}{EC}$, giving $EC = \dfrac{18}{4} = 4.5$.

Therefore $AC = AE + EC = 3 + 4.5 = 7.5$.

## Common Misconceptions (Teaching Notes)

### 1. Using $k$ for area or $k^2$ for volume (off-by-one error)

**What students do.** Enlargement scale factor is $2$. Area becomes $2\times$ the original (should be $4\times$); volume becomes $4\times$ (should be $8\times$).

**Fix.** "Lengths are 1D, areas are 2D, volumes are 3D — the exponent matches the dimension." Drill with a unit square → $k \times k$ square, unit cube → $k \times k \times k$ cube.

### 2. Computing differences instead of ratios

**What students do.** Given $AB = 6$, $DE = 9$, they write "scale factor $= 9 - 6 = 3$" (wrong) instead of "$9 \div 6 = 1.5$".

**Fix.** Similarity is about **how many times bigger**, not **how much bigger**. Contrast with translations (which *do* use differences). The Chinese 比 character (ratio) is the mental anchor.

### 3. Wrong vertex correspondence / writing ratios upside-down

**What students do.** $\triangle ABC \sim \triangle DEF$ but they write $\dfrac{AB}{EF}$ or $\dfrac{CA}{DE}$ — mixing up which vertex in one triangle matches which in the other.

**Fix.** Always rewrite the correspondence in a vertical stack:
```
A - D
B - E
C - F
```
Side $AB$ matches side $DE$, side $BC$ matches $EF$, etc.

### 4. Assuming triangle-family shortcuts transfer to similarity

**What students do.** "All equilateral triangles are similar" → "all isosceles triangles are similar" (false — the apex angle can vary).

**Fix.** For a family of triangles to all be similar, the *shape* must be fixed. Equilateral fixes all three angles at $60°$, so yes. Isosceles only fixes that two sides are equal — the apex angle is free. Right-angled fixes one angle at $90°$, still not similar in general.

### 5. AAA vs AA

**What students do.** Write "AAA" as the reason for similarity on an exam, or confuse with the AAA-is-not-congruence rule.

**Fix.** AAA and AA convey the same information for triangles (angle sum is $180°$). Most syllabuses accept "AA" as the standard name to distinguish from the congruence mis-attempt. Use AA. 

### 6. Similarity of non-triangles

**What students do.** Apply the three-condition logic to quadrilaterals, assuming "three sides in ratio + one angle" is enough.

**Fix.** The similarity conditions (AA, SSS, SAS) work **only for triangles**. For quadrilaterals, two shapes can have matching angles or matching side ratios without being similar — both must hold. Most IGCSE problems stick to triangles; flag the exception if they appear.

## Exam Notes

### OxAQA 9260

**G7** (Core and Extension): understand similarity; calculate lengths in similar figures. Extension-tier questions require identifying the similar triangles and setting up the ratio from the correspondence.

**G17 Ext** (Extension only): relationships between lengths, areas and volumes in similar figures. Expect problems like "two similar cans have radii $3$ cm and $5$ cm; the smaller can holds $150$ mL — how much does the larger hold?" (volume ratio $= (5/3)^3$).

Common trap: the question gives an area or volume ratio and asks for a length; students forget to take square or cube roots.

### Cambridge 0580 Extended

**E4.4** (Similarity): use the relationship between lengths, areas and volumes of similar shapes. Core tier is "identify similar figures"; Extended tier adds the scaling laws. Frequently paired with mensuration (E5) — cones, spheres, composite solids.

### Cambridge 0606

Not a standalone topic. Similarity is *assumed from 0580* and used silently in circle geometry and coordinate proofs. If a 0606 question says "it can be shown that $\triangle PQR \sim \triangle XYZ$", the student needs to apply the scale-factor laws without being taught them again.

### A-Level

Similarity reappears in:
- **Pure:** transformations and matrices — enlargement as a $2 \times 2$ matrix $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$.
- **Further Pure:** similar triangles in proofs of the sine and cosine rules, circle-geometry lemmas.
- **Mechanics:** dimensional analysis is essentially the scaling-law argument applied to physics quantities.

### IB AA / AI

IB AA SL/HL uses similarity implicitly throughout geometry and trigonometry. HL Topic 3 (Geometry & Trigonometry) expects fluent scale-factor reasoning. IB AI touches similarity in the context of modelling (e.g. scale models, map projections).

## Connections

- **Sibling:** [[Congruence]] — same shape **and** size; congruence is the $k = 1$ case of similarity.
- **Parent:** [[Transformations (Vocab)]] — enlargement is the fourth transformation; similarity is what enlargement preserves.
- **Prerequisite concept:** [[Fractions (Vocab)]] — ratios and proportion are the computational backbone.
- **Application:** [[Trigonometric Ratios]] — $\sin$, $\cos$, $\tan$ of an angle are well-defined precisely *because* all right triangles with that angle are similar. Without similarity, trigonometry doesn't work.
- **Proof ingredient:** [[Pythagoras Theorem]] — the cleanest proof of $a^2 + b^2 = c^2$ uses the three similar triangles formed by the altitude on the hypotenuse.
- **Extension:** [[Matrix Transformations]] — enlargement from the origin by factor $k$ is the matrix $kI$. Similar matrices in linear algebra (matrices $A$ and $B$ with $A = P^{-1}BP$) borrow the name — "same linear map in a different basis" is the linear-algebra analogue of "same shape in a different coordinate system".
- **Reverse/Dual:** [[Scale Drawings (Vocab)|Scale Drawings]] — the applied version; maps, blueprints, scale models.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\sim$ | `\sim` | "is similar to" |
| $\cong$ | `\cong` | "is congruent to" |
| $\triangle ABC$ | `\triangle ABC` | Triangle |
| $\dfrac{a}{b}$ | `\dfrac{a}{b}` | Display-style fraction — use in inline math for clarity |
| $\angle A$ | `\angle A` | Angle |
| $\sqrt[3]{x}$ | `\sqrt[3]{x}` | Cube root |
| $\blacksquare$ | `\blacksquare` | End of proof |
| $k$, $k^2$, $k^3$ | `k`, `k^2`, `k^3` | Scale factors for length, area, volume |
