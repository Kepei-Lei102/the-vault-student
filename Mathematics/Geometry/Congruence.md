---
chinese: 全等 (quánděng)
prerequisites:
  - "[[Triangles (Vocab)]]"
  - "[[Angle Properties (Vocab)]]"
  - "[[Pythagoras Theorem]]"
  - "[[Transformations (Vocab)]]"
leads_to:
  - "[[Similarity]]"
  - "[[Geometrical Proof]]"
  - "[[Circle Theorems II]]"
  - "[[Vector Geometry]]"
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
  - syllabus/0580-E4-1
  - type/definition
  - type/theorem
  - type/proof
  - notation/congruent
  - notation/triangle
  - misconception/aaa-is-not-congruence
  - misconception/ssa-ambiguous
  - misconception/wrong-vertex-order
---
# Congruence 全等

## Definition

### Formal

Two figures are **congruent** if one can be mapped onto the other by a sequence of **rigid motions** — translations, rotations, and reflections. Equivalently, corresponding sides and corresponding angles are all equal.

For two triangles, this is written:

$$\triangle ABC \cong \triangle DEF$$

The vertex **order matters**: $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$. Writing $\triangle ABC \cong \triangle DEF$ simultaneously asserts **six** equalities:

$$AB = DE, \quad BC = EF, \quad CA = FD$$
$$\angle A = \angle D, \quad \angle B = \angle E, \quad \angle C = \angle F$$

### Intuitive

Two figures are congruent when they are **the same shape AND the same size**. You could cut one out of paper and slide it on top of the other so every point matches — possibly after flipping or rotating the paper first. Nothing about the figure changes except where it is in space.

Contrast with [[Similarity]]: similar figures are the same *shape* but may be different *sizes* (one is a scaled copy of the other). Congruent is the special case of similar where the scale factor equals $1$.

### 中文锚点

**全等 = 完全相等**。形状相同，大小相同 — 一个图形经过平移、旋转、翻折（不缩放）可以与另一个完全重合。

中文数学课早就熟悉 **SSS、SAS、ASA、RHS** 四个判定条件，通常叫做「边边边」「边角边」「角边角」「斜边直角边」。英文考试的新负担主要是三件事：

1. 用符号 $\cong$ 表示全等（像等号上加了一个波浪号 $\sim$，意思是「形状相等 + 大小相等」）；
2. 顶点对应顺序：$\triangle ABC \cong \triangle DEF$ 暗示 $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$ — 写错顺序等于写错答案；
3. 在证明题里必须**说出**用的是哪一个判定条件（"by SAS…"），这是 mark scheme 的 1 分。

---

## Notation

| Convention | Symbol | Read as | Notes |
|---|---|---|---|
| Congruent to | $\cong$ | "is congruent to" | `\cong` — the $\sim$ part means "same shape"; the $=$ part means "same size" |
| Similar to | $\sim$ | "is similar to" | Same shape, possibly different size |
| Equal (lengths / angles) | $=$ | "equals" | Used on individual sides/angles |
| Triangle | $\triangle$ | "triangle" | Always precede vertex letters: $\triangle ABC$ |
| Corresponds to | $\leftrightarrow$ | "corresponds to" | Informal shorthand for vertex matching |

> [!warning] Notation trap
> Do **not** write $\triangle ABC = \triangle DEF$. Triangles are figures, not numbers — they are *congruent*, not *equal*. In Chinese both might be translated as "等", but the English distinction is strict and marked.

---

## The Four Congruence Conditions

![[congruence-four-conditions.svg|720]]

Two triangles are congruent if **any** of the following four conditions holds. Each condition fixes enough information to force the triangle to be unique (up to reflection).

### 1. SSS — Side, Side, Side

> **If three sides of one triangle are equal to the three corresponding sides of another, the triangles are congruent.**

**Why SSS works.** Place segment $AB$ on a baseline. The third vertex $C$ must sit at distance $b = CA$ from $A$ and at distance $a = CB$ from $B$ — i.e., on the intersection of two circles centred at $A$ and $B$ with radii $b$ and $a$. Two circles intersect in at most **two** points, and those two points are mirror images across $AB$. So once the three side lengths are given, the triangle is unique up to a reflection — and congruence allows reflection, so the triangle is essentially unique.

![[congruence-sss-construction.svg|600]]

The animation above is exactly this argument with a ruler and compass. Draw $AB$. Open the compass to length $b$ and sweep an arc around $A$ — every point on this arc is at distance $b$ from $A$. Open the compass to length $a$ and sweep an arc around $B$ — every point on that arc is at distance $a$ from $B$. The two arcs meet at one point above $AB$ (and another below by reflection): that point is the only place $C$ can possibly be.

#### Why "SSSS" does NOT work for quadrilaterals — triangles are rigid, quadrilaterals are not

![[congruence-ssss-square-rhombus.svg|720]]

Take a square and imagine gripping two opposite corners and pushing them towards each other. The four sides don't change length — but the shape slides into a rhombus, and then into a nearly flat rhombus, and in the limit collapses to a line segment. All three of these have four equal sides, yet they are obviously not congruent: the angles are different and the shape is different.

**Why triangles are different.** In a triangle, once the three side lengths are fixed, the position of the third vertex is pinned by the intersection of two circles (the SSS argument above) — there is nowhere for it to slide to. But a quadrilateral has one extra degree of freedom: the angle at one corner can open or close without forcing any side to change length. Shapes with this sliding flexibility are called **non-rigid**; shapes without it are **rigid**. Triangles are the only polygon that is rigid from side lengths alone.

**The practical consequence.** To make a quadrilateral rigid — for example, a wooden gate or a bridge truss — engineers **triangulate** it: add a diagonal brace that splits the quadrilateral into two triangles. Each triangle is then rigid by SSS, and the whole structure cannot deform. This is exactly why steel bridges, cranes, bicycle frames, and the Eiffel Tower are built out of triangles, not squares.

> [!info] Beyond-syllabus — rigidity theory
> The general study of which frameworks are rigid belongs to a subject called **rigidity theory**, with applications in robotics, protein folding, and origami. **Cauchy's rigidity theorem (1813)** states that a convex polyhedron made of rigid faces joined along hinged edges is globally rigid — you cannot flex it. A flat triangle is the 2D shadow of this idea.

### 2. SAS — Side, Angle, Side

> **If two sides and the included angle of one triangle are equal to the corresponding two sides and included angle of another, the triangles are congruent.**

The word **"included"** is load-bearing: the angle must sit *between* the two sides whose lengths you know.

**Why SAS works.** Place vertex $V$ at the origin and draw one side of length $a$ along a baseline. The angle at $V$ is fixed at $\theta$, so the direction of the second side is determined. That second side has fixed length $b$, so its far endpoint is determined. The third side of the triangle is forced: it is the unique segment joining the two non-$V$ endpoints. With every choice pinned down, the triangle is unique.

![[congruence-sas-construction.svg|600]]

In the construction: side $a$ goes down first, then the protractor at $V$ pins the included angle $\theta$, then side $b$ is drawn out at that angle. Both endpoints are now nailed down — the third side $BC$ has nowhere to go but the unique segment joining them.

### 3. ASA (and AAS) — Angle, Side, Angle

> **If two angles and a corresponding side of one triangle are equal to the two angles and corresponding side of another, the triangles are congruent.**

The side can be **between** the two angles (ASA) or **opposite** one of them (AAS). Both work because the third angle is forced by the $180°$ angle sum of a triangle, so knowing any two angles is the same as knowing all three.

**Why ASA works.** Draw the known side $AB$. The angle at $A$ determines the ray $A \to C$. The angle at $B$ determines the ray $B \to C$. Since the two angles at $A$ and $B$ sum to less than $180°$ (the triangle is non-degenerate), the two rays meet at exactly one point on one side of $AB$. So $C$ is uniquely determined.

![[congruence-asa-construction.svg|600]]

The animation makes the rigidity visual: once the side $AB$ and the two base angles $\alpha$ and $\beta$ are fixed, the two rays from $A$ and $B$ have fixed directions, and two non-parallel lines in a plane meet at exactly one point — that point is $C$.

**Why AAS reduces to ASA.** If two angles are given and one non-included side, then the third angle is $180°$ minus the sum of the two known angles. That third angle sits between the other angle and the known side — so we now have a two-angle-included-side configuration, which is ASA.

### 4. RHS — Right angle, Hypotenuse, Side

> **If two right-angled triangles have equal hypotenuses and one pair of equal legs, the triangles are congruent.**

This is the **only** condition involving SSA (Side, Side, Angle with the angle *not* between the two sides) that actually produces congruence — because the right angle is a special case that forces the configuration.

**Why RHS works — reducing RHS to SSS via Pythagoras.** The claim is that two right-angled triangles with the same hypotenuse and same one-leg are congruent. We prove this by showing the *other* leg is forced, so we secretly have all three sides — and SSS then finishes the job.

*Proof that RHS ⟹ SSS.*

1. Let $\triangle ABC$ and $\triangle DEF$ be two right-angled triangles with right angles at $A$ and $D$ respectively.
2. Suppose the hypotenuses are equal: $BC = EF = h$.
3. Suppose one pair of legs is equal: $AB = DE = a$.
4. By [[Pythagoras Theorem]] applied to $\triangle ABC$: $\; AC^2 = BC^2 - AB^2 = h^2 - a^2$, so $AC = \sqrt{h^2 - a^2}$.
5. By [[Pythagoras Theorem]] applied to $\triangle DEF$: $\; DF^2 = EF^2 - DE^2 = h^2 - a^2$, so $DF = \sqrt{h^2 - a^2}$.
6. Therefore $AC = DF$ — the third pair of sides is equal.
7. Now all three pairs of sides are equal: $AB = DE$, $BC = EF$, $AC = DF$.
8. By **SSS**, $\triangle ABC \cong \triangle DEF$. $\blacksquare$

![[congruence-rhs-construction.svg|600]]

The construction tells the same story visually: draw the known leg $a$, raise the perpendicular at the right angle, then sweep an arc of length $h$ (the hypotenuse) from the far end of the leg. The arc meets the perpendicular at exactly one point above the baseline — that point is $C$. The "other leg" $AC$ was never given to us, but Pythagoras (and the geometry) forces it to take a unique value.

So RHS is really **SSS in disguise** — the right angle plus Pythagoras automatically supplies the missing third side. That is the structural reason RHS is the only "SSA-shaped" condition that works.

> [!info] RHS works, SSA doesn't — why the right angle is special
> The reason the right angle saves RHS is that a leg of a right-angled triangle is always **shorter than the hypotenuse**. So the circle of possible third-vertex positions meets the ray from the right angle at exactly one point (on the correct side). Remove the right angle and that guarantee breaks — see the SSA ambiguous case below.

---

## The Two Conditions That Do NOT Work

### AAA — Angle, Angle, Angle

Three equal angles give [[Similarity]], not congruence. Two equilateral triangles of different sizes have all three angles equal to $60°$ but obviously aren't the same triangle — one might fit in your hand and the other fill a football field.

![[congruence-aaa-counterexample.svg|600]]

Angles only specify **shape**; to pin down **size** you need at least one length.

### SSA — Side, Side, non-included Angle (the ambiguous case)

Giving two sides and an angle that is *not* between them can produce **two non-congruent triangles**, one triangle, or zero triangles — depending on the numbers. This is the same **ambiguous case** you meet in the Sine Rule (see [[Sine and Cosine Rules]]).

Watch what goes wrong. We fix angle $A$, draw side $AC$, then sweep a compass from $C$ with radius $a = CB$. The compass arc crosses the base ray **twice** — giving two entirely different triangles $\triangle ACB_1$ (red) and $\triangle ACB_2$ (green) that share the same three measurements.

![[congruence-ssa-ambiguous-animated.svg|697]]

**What goes wrong.** Say you're given angle $A$, side $b$ (adjacent to $A$), and side $a$ (opposite $A$). Draw angle $A$; fix the endpoint of side $b$ at $C$. The third vertex $B$ must lie at distance $a$ from $C$ — i.e., on a circle of radius $a$ centred at $C$. That circle can hit the other ray of angle $A$ at **two** points, giving two different triangles (one acute-angled at $B$, one obtuse-angled at $B$).

The right angle in RHS kills the ambiguity because it forces one of the two possible $B$'s to land at infinity — there is only ever one triangle.

---

## Using Congruence in Proofs — CPCTC

In proof questions, congruence is rarely the final answer. Instead, it's a **stepping stone**:

1. Identify two triangles that share some equal parts.
2. Prove they are congruent using one of SSS, SAS, ASA/AAS, or RHS — and **name the condition**.
3. Deduce that *other* corresponding parts are equal (sides, angles, or derived quantities).

This last move is often called **CPCTC** in American texts: "Corresponding Parts of Congruent Triangles are Congruent." In UK / Cambridge / OxAQA exams it's usually written as a plain sentence: "so $\angle X = \angle Y$ (corresponding angles of congruent triangles)."

> [!tip] The "name the condition" mark
> On proof questions, 9260 and 0580 mark schemes almost always have a dedicated mark for **stating the congruence rule used**. Writing "the triangles are congruent" is not enough. You must write "the triangles are congruent by **SAS**" (or SSS, ASA, RHS). Students lose this mark more often than any other.

**Classic examples already in the vault.** The proofs of two [[Circle Theorems II]] results — *tangents from an external point are equal* and *perpendicular from centre bisects chord* — both hinge on **RHS congruence**. Skim back through them now with fresh eyes: the congruence step is the keystone of each proof.

---

## Worked Examples

### Example 1 (9260 Extension) — Isosceles triangle base angles

> Prove that in an isosceles triangle, the angles opposite the two equal sides are equal.

**Set up.** Let $\triangle ABC$ have $AB = AC$. We want to show $\angle ABC = \angle ACB$.

**Construction.** Let $M$ be the midpoint of $BC$ and draw the segment $AM$.

**Congruence argument.** Consider triangles $ABM$ and $ACM$:

- $AB = AC$ (given — the equal sides of the isosceles triangle).
- $AM = AM$ (common side).
- $BM = CM$ (since $M$ is the midpoint of $BC$).

By **SSS**, $\triangle ABM \cong \triangle ACM$.

**Conclusion.** Corresponding angles of congruent triangles are equal:

$$\angle ABM = \angle ACM$$

That is, $\angle ABC = \angle ACB$. $\blacksquare$

**Bonus.** The same argument shows $\angle AMB = \angle AMC$. These angles sit on the line $BC$, so they are supplementary — each is $90°$. So $AM \perp BC$. The line from the apex to the midpoint of the base is also the altitude. Neat.

### Example 2 (9260 Extension) — Perpendicular bisector

> Point $P$ lies on the perpendicular bisector of segment $AB$. Prove that $PA = PB$.

**Set up.** Let $M$ be the midpoint of $AB$, so $PM \perp AB$ and $AM = BM$.

**Congruence argument.** Consider triangles $PMA$ and $PMB$:

- $AM = BM$ (definition of midpoint).
- $PM = PM$ (common side).
- $\angle PMA = \angle PMB = 90°$ (given).

By **SAS**, $\triangle PMA \cong \triangle PMB$.

**Conclusion.** $PA = PB$ (corresponding sides of congruent triangles). $\blacksquare$

**What this proves in one line.** Every point on the perpendicular bisector of a segment is equidistant from the two endpoints. This is a basic building block of [[Geometrical Proof]] and underlies the *circumcentre* of a triangle.

### Example 3 (A-Level style) — Proving a quadrilateral is a parallelogram

> $ABCD$ is a quadrilateral in which $AB \parallel CD$ and $AB = CD$. Prove that $AD \parallel BC$ (so $ABCD$ is a parallelogram).

**Set up.** Draw the diagonal $AC$, cutting the quadrilateral into $\triangle ABC$ and $\triangle CDA$.

**Congruence argument.** Consider $\triangle ABC$ and $\triangle CDA$:

- $AB = CD$ (given).
- $AC = CA$ (common side).
- $\angle BAC = \angle DCA$ (alternate angles since $AB \parallel CD$ — see [[Angles in Parallel Lines (Vocab)]]).

By **SAS**, $\triangle ABC \cong \triangle CDA$.

**Conclusion.** $\angle BCA = \angle DAC$ (corresponding angles of congruent triangles). These are alternate angles between lines $AD$ and $BC$ cut by transversal $AC$, so $AD \parallel BC$. $\blacksquare$

This is exactly the style of proof that shows up in 9260 Extension Geometrical Proof questions.

---

## Common Misconceptions (Teaching Notes)

### 1. Writing the vertex order backwards

When a student writes $\triangle ABC \cong \triangle EFD$ but means $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$, they've just asserted six equalities that are actually wrong.

![[congruence-vertex-order.svg|720]]

On the left, each corresponding pair shares a colour — $A$ and $D$ are blue, $B$ and $E$ are purple, $C$ and $F$ are green — so the statement $\triangle ABC \cong \triangle DEF$ exactly captures the intended correspondence. On the right, the claim $\triangle ABC \cong \triangle EFD$ would pair blue $A$ with purple $E$, purple $B$ with green $F$, green $C$ with blue $D$ — the colours clash, and the six side-angle equalities that follow from the statement are all pointing at the wrong sides. The mark scheme treats this as a wrong answer even if the triangles really are congruent.

**Fix:** Drill the habit — before writing $\triangle XYZ \cong \triangle \_\_\_$, look at the first triangle's vertices and ask "where does each one go?" Write the corresponding vertex directly under the original one. Only then commit to the $\cong$ statement.

### 2. Forgetting the "included" word in SAS

Students say "two sides and an angle — that's SAS, right?" without checking whether the angle is between the two sides.

**Fix:** Teach the sentence *"the angle must be between the two sides"* as a reflex. Walk through the SSA ambiguous-case diagram once so they see with their own eyes that two different triangles can have the same two sides and non-included angle.

### 3. Claiming AAA proves congruence

Students see three equal angles and conclude the triangles are congruent. The right conclusion is that they are **similar** — same shape, possibly different size.

**Fix:** Use the two-equilateral-triangles counterexample (one small, one large). All three angles are $60°$ in each — AAA is satisfied — but the triangles are clearly not the same triangle. So AAA cannot prove congruence.

### 4. Applying RHS to a non-right triangle

Students sometimes invoke "RHS" whenever they see a hypotenuse and a side. But RHS requires the **right angle** — without it, what you actually have is SSA, which may be ambiguous.

**Fix:** Before citing RHS, explicitly mark the right angle on the diagram. If there's no right angle, RHS is not available — you need a different condition.

### 5. Confusing congruence with similarity

"全等" (congruent) and "相似" (similar) often get swapped under exam pressure.

**Fix:** A memorable mnemonic: **C**ongruent = **C**opy (identical copy), Similar = Scaled. Reinforce with the symbols: $\cong$ has an equals sign (same size) plus a tilde (same shape); $\sim$ has only the tilde (just same shape).

### 6. Naming only one triangle

Some students write "the triangles are congruent by SAS" but never explicitly list the three equal parts. The mark scheme needs to see the three parts (and why each one is equal).

**Fix:** Teach the standard proof pattern:
1. "Consider triangles $\square$ and $\square$:"
2. List the three equal parts in a vertical stack, each with a reason in brackets.
3. Conclude "by [SSS / SAS / ASA / RHS], $\triangle \square \cong \triangle \square$."
4. Only then deduce the required equal parts.

---

## Exam Notes

### OxAQA 9260

**Syllabus reference:** G7 (Congruence and Similarity). At core level, the student must *understand* the concept of congruence; at **Extension** level, they must know the four conditions SSS, SAS, ASA (incl. AAS), RHS, and use them in proofs.

**Typical questions.** Two-part format is common: (a) prove two triangles are congruent, (b) use the congruence to deduce a further fact about a figure (equal lengths, parallel sides, angle bisection, perpendicularity).

**Mark pattern.** On a 4-mark proof question, expect: 1 mark for identifying the three equal parts, 1 mark for stating reasons, 1 mark for naming the congruence condition, 1 mark for the final deduction.

### Cambridge 0580 Extended

**Syllabus reference:** E4.1 (similar and congruent shapes). At 0580 Extended, formal congruence conditions (SSS/SAS/ASA/RHS) are **not examined** — students just need to identify when figures are congruent ("tick the congruent pair") and state that corresponding sides and angles are equal.

**Contrast with 9260:** this is a real difference between the two boards. OxAQA pushes into proofs that Cambridge 0580 avoids. Students who moved from 0580 to 9260 mid-course need explicit teaching on SSS/SAS/ASA/RHS — they will not have seen it.

### Cambridge 0606

Congruence is not a standalone 0606 topic, but the conditions are assumed background when 0606 uses triangle geometry in trigonometry and coordinate geometry problems.

### A-Level

Congruence is assumed GCSE knowledge and appears implicitly in A-Level Pure (coordinate geometry of circles, vector proofs of geometric results) and in Further Pure (rigorous Euclidean geometry). No standalone A-Level topic, but every proof of a circle theorem or a triangle-centre result leans on it.

### IB AA / AI

Part of the Geometry and Trigonometry topic. Congruence appears in proofs related to inscribed angles, the unit circle, and vector methods. At HL, it underpins formal geometric proofs in the optional "Geometry" topic.

> [!info] Beyond high school — congruence as an equivalence relation
> "Congruent" is an **equivalence relation** on the set of geometric figures: every figure is congruent to itself; if $A \cong B$ then $B \cong A$; if $A \cong B$ and $B \cong C$ then $A \cong C$. This is the same algebraic structure that underlies set equality, modular arithmetic ($a \equiv b \pmod n$ uses the same $\equiv$ for the same reason), and the isomorphism relation in abstract algebra. Congruence classes — sets of mutually congruent figures — are the right objects to *count* when you ask "how many triangles are there with integer side lengths at most $10$?" You count congruence classes, not individually placed triangles.
>
> At university, **SAS is not a theorem but an axiom (公理 gōnglǐ)**. An *axiom* (公理) is a statement taken as true without proof — a starting rule from which other statements are *derived*. In Chinese maths texts the corresponding word is 公理, literally "public / shared principle". Hilbert's axiomatisation (公理化 gōnglǐhuà) of Euclidean geometry takes SAS (his Axiom IV.6) as a postulate, from which SSS, ASA, and the rest are *proved*. So when we say "SAS works because you can construct the triangle uniquely," we're really appealing to an informal version of the axiom.

---

## Connections

- **Parent:** [[Triangles (Vocab)]] — the vocabulary and types used throughout
- **Prerequisite ingredient:** [[Pythagoras Theorem]] — RHS is really SSS via Pythagoras
- **Prerequisite idea:** [[Transformations (Vocab)]] — congruence = reachable by rigid motion
- **Sibling:** [[Similarity]] — same shape, possibly different size; AAA proves similarity not congruence
- **Application:** [[Circle Theorems II]] — tangents from an external point, perpendicular bisects chord (both use RHS)
- **Application:** [[Geometrical Proof]] — congruence is the single most-used proof tool at 9260 Extension
- **Ambiguous cousin:** [[Sine and Cosine Rules]] — the SSA ambiguous case reappears when solving triangles with the sine rule
- **Language sibling:** the word "congruent" in number theory ($a \equiv b \pmod n$) is the same equivalence-relation idea in an algebraic setting

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\cong$ | `\cong` | Congruent to — equals with a tilde |
| $\sim$ | `\sim` | Similar to |
| $\triangle$ | `\triangle` | Triangle — precede vertex letters |
| $\angle$ | `\angle` | Angle — precede with a space |
| $\perp$ | `\perp` | Perpendicular |
| $\parallel$ | `\parallel` | Parallel |
| $\leftrightarrow$ | `\leftrightarrow` | Corresponds to — informal vertex matching |
| $\sqrt{\cdot}$ | `\sqrt{\cdot}` | Square root (for the Pythagoras-RHS argument) |
| $\blacksquare$ | `\blacksquare` | End-of-proof marker |
