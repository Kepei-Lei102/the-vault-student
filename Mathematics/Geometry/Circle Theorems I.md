---
chinese: 圆定理（一）(yuán dìnglǐ yī)
prerequisites:
  - "[[Circle Vocabulary (Vocab)]]"
  - "[[Angle Properties (Vocab)]]"
  - "[[Angles in Parallel Lines (Vocab)]]"
  - "[[Triangles (Vocab)]]"
  - "[[Polygon Angles (Vocab)]]"
  - "[[Sine and Cosine Rules]]"
  - "[[Trigonometric Ratios]]"
leads_to:
  - "[[Circle Theorems II]]"
  - "[[Geometrical Proof]]"
  - "[[Similarity]]"
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
  - syllabus/9260-G8
  - syllabus/0580-C4-7
  - syllabus/0580-E4-7
  - type/theorem
  - type/proof
  - notation/angle
  - misconception/centre-vs-circumference
  - misconception/cyclic-quad-adjacent-angles
---

# Circle Theorems I 圆定理（一）

This card covers the four **angle-based** circle theorems — the ones that relate angles subtended by arcs. These are the theorems tested most heavily at 9260 Extension and the ones students need to chain together in multi-step proofs.

## Why Circle Theorems Exist

A circle is the most symmetric curve in the plane: every point is equidistant from the centre, every diameter is a line of symmetry, and any rotation about the centre maps the circle onto itself. This extreme symmetry forces angles inscribed in the circle to obey strict rules. The four theorems below are all consequences of one master fact: **equal radii create isosceles triangles**, and isosceles triangles constrain angles.

That's the key insight. Every proof in this card starts by drawing radii and exploiting the isosceles triangles they create.

![[circle-theorems-i-overview.svg|700]]

## 中文锚点

圆定理是英国课程的重点，中国初中虽然学过"圆周角等于圆心角的一半"等内容，但英国考试对**定理名称**和**证明推理链**的要求远高于中国中考。四个定理：

1. **圆心角 = 2 × 圆周角**（同弧）
2. **半圆上的圆周角 = 90°**（直径对的角是直角）
3. **同弧上的圆周角相等**
4. **圆内接四边形对角互补**（对角之和 = 180°）

每个定理都要能用英文陈述、画图标注、写出证明推理。

---

## Theorem 1 — Angle at the Centre

> **The angle subtended by an arc at the centre is twice the angle subtended by the same arc at any point on the circumference.**

In symbols: if $A$ and $B$ are points on the circle and $O$ is the centre, then for any point $P$ on the **major arc**:

$$\angle AOB = 2 \times \angle APB$$

### Intuitive explanation

Point $P$ is "further away" from the arc $AB$ than the centre $O$ is. The further you move from an arc, the smaller the angle it subtends (think of how a building looks smaller from far away). But the relationship isn't just "smaller" — it's exactly half, because the radii $OA$ and $OB$ create isosceles triangles that force a precise 2:1 ratio.

### Proof

![[circle-theorems-i-proof.svg|700]]

**Case 1: Centre lies inside $\angle APB$**

Draw the diameter from $P$ through $O$ to point $D$ on the circle. This splits the configuration into two isosceles triangles.

**Left triangle $OAP$:** $OA = OP = r$, so $\angle OAP = \angle OPA = \alpha$.
By the exterior angle theorem on triangle $OAP$:

$$\angle AOD = \alpha + \alpha = 2\alpha$$

**Right triangle $OBP$:** $OB = OP = r$, so $\angle OBP = \angle OPB = \beta$.
By the exterior angle theorem on triangle $OBP$:

$$\angle BOD = \beta + \beta = 2\beta$$

Adding both results:

$$\angle AOB = \angle AOD + \angle BOD = 2\alpha + 2\beta = 2(\alpha + \beta) = 2 \times \angle APB$$

$$\boxed{\angle AOB = 2 \times \angle APB}$$

**Case 2: Centre lies outside $\angle APB$** — the same argument works, but with subtraction instead of addition: $\angle AOB = 2\alpha - 2\beta$.

> [!tip] The "draw-a-diameter" trick
> This is the most important proof technique in circle geometry: **draw the diameter through the awkward point**. It splits the problem into two isosceles triangles, and the exterior angle theorem does the rest. You'll see this trick again in Theorems 2, 3, and 4.

---

## Theorem 2 — Angle in a Semicircle

> **The angle subtended by a diameter at any point on the circumference is $90°$.**

Equivalently: if $AB$ is a diameter and $P$ is any point on the circle (not $A$ or $B$), then $\angle APB = 90°$.

### Intuitive explanation

A diameter subtends an angle of $180°$ at the centre (it's a straight line through $O$). By Theorem 1, the angle at the circumference is half this: $180° \div 2 = 90°$. That's it — Theorem 2 is a special case of Theorem 1.

### Proof

![[circle-theorems-ii-proof-semicircle.svg|700]]

$AB$ is a diameter, so $\angle AOB = 180°$ (angles on a straight line).

By Theorem 1: $\angle APB = \dfrac{1}{2} \times 180° = 90°$

$$\boxed{\angle APB = 90°}$$

> [!tip] Thales' theorem
> This result is historically called **Thales' theorem** (c. 600 BCE), making it one of the oldest named theorems in mathematics. Thales supposedly proved it by noting that any triangle inscribed in a semicircle must be right-angled — the same argument we just gave, though he probably used a different proof.

### The Converse

The converse is equally useful: **if $\angle APB = 90°$ and $A$, $P$, $B$ lie on a circle, then $AB$ is a diameter.** This means you can locate the centre of a circle by finding a right angle — the hypotenuse of the right-angled triangle must be a diameter.

---

## Theorem 3 — Angles in the Same Segment

> **Angles subtended by the same arc at the circumference are equal.**

If $P$ and $Q$ are both on the major arc of chord $AB$, then $\angle APB = \angle AQB$.

### Intuitive explanation

Both $P$ and $Q$ are "looking at" the same arc $AB$ from the same side. By Theorem 1, both angles equal half the central angle $\angle AOB$. Since they're both half of the same thing, they must be equal to each other.

### Proof

![[circle-theorems-iii-proof-segment.svg|700]]

By Theorem 1:

$$\angle APB = \dfrac{1}{2} \angle AOB \qquad \text{and} \qquad \angle AQB = \dfrac{1}{2} \angle AOB$$

Therefore:

$$\boxed{\angle APB = \angle AQB}$$

> [!warning] Same segment, not same circle
> The points must be on the **same arc** (same segment). If $P$ is on the major arc and $Q$ is on the minor arc, their angles are NOT equal — they are **supplementary** (they add to $180°$). This is Theorem 4.

---

## Theorem 4 — Cyclic Quadrilateral (Opposite Angles)

> **The opposite angles of a cyclic quadrilateral are supplementary** (they add up to $180°$).

A **cyclic quadrilateral** (圆内接四边形) is a quadrilateral whose four vertices all lie on a circle.

If $ABCD$ is a cyclic quadrilateral, then:

$$\angle A + \angle C = 180° \qquad \text{and} \qquad \angle B + \angle D = 180°$$

### Intuitive explanation

Vertices $A$ and $C$ are on opposite sides of chord $BD$. Together, the arcs they "see" cover the entire circle — one sees the major arc, the other sees the minor arc. Since the full circle subtends $360°$ at the centre, the two half-angles at the circumference must sum to $180°$.

### Proof

![[circle-theorems-iv-proof-cyclic.svg|700]]

Let the arc $BCD$ (the arc from $B$ to $D$ passing through $C$) subtend angle $2\alpha$ at the centre.
Let the arc $BAD$ (the arc from $B$ to $D$ passing through $A$) subtend angle $2\beta$ at the centre.

These two arcs make up the full circle:

$$2\alpha + 2\beta = 360°$$

By Theorem 1:
- $\angle A = \alpha$ (angle at circumference subtended by arc $BCD$)
- $\angle C = \beta$ (angle at circumference subtended by arc $BAD$)

Therefore:

$$\angle A + \angle C = \alpha + \beta = \dfrac{360°}{2} = 180°$$

$$\boxed{\angle A + \angle C = 180°}$$

The same argument gives $\angle B + \angle D = 180°$.

### The Converse

**If the opposite angles of a quadrilateral sum to $180°$, then the quadrilateral is cyclic** (a circle passes through all four vertices). This converse is tested at 9260 — examiners ask "Show that $ABCD$ is a cyclic quadrilateral" and you prove it by showing opposite angles are supplementary.

---

## How the Four Theorems Connect

All four theorems are really **one theorem and three corollaries**:

| Theorem | Relationship to Theorem 1 |
|---------|--------------------------|
| 1. Angle at centre = 2× circumference | **The master theorem** |
| 2. Angle in semicircle = 90° | Special case: central angle = 180° |
| 3. Same segment angles equal | Both are half of the same central angle |
| 4. Cyclic quad opposite angles = 180° | Two circumference angles whose central angles sum to 360° |

Understanding Theorem 1 deeply means you understand all four. The exam tests them as separate theorems, but mathematically they're one idea.

---

## Worked Examples

### Example 1 (9260): Finding angles using Theorems 1 and 3

Points $A$, $B$, $C$, $D$ lie on a circle with centre $O$. $\angle AOB = 104°$.

**(a)** Find $\angle ACB$.

By Theorem 1 (angle at centre = 2× circumference):

$$\angle ACB = \dfrac{1}{2} \times 104° = 52°$$

**(b)** Find $\angle ADB$.

By Theorem 3 (angles in the same segment are equal):

$$\angle ADB = \angle ACB = 52°$$

### Example 2 (9260): Cyclic quadrilateral + same segment

$A$, $B$, $C$, $D$ lie on a circle. $\angle BAD = 106°$ and $\angle ADB = 30°$.

**(a)** Find $\angle BCD$.

By Theorem 4 (opposite angles of cyclic quadrilateral):

$$\angle BCD = 180° - 106° = 74°$$

**(b)** Find $\angle ACB$.

By Theorem 3 (angles in same segment — both $\angle ACB$ and $\angle ADB$ are subtended by arc $AB$ on the same side):

$$\angle ACB = \angle ADB = 30°$$

This is the typical 9260 pattern: **Theorem 4 gives you one angle, Theorem 3 transfers it elsewhere.**

### Example 3 (9260): Semicircle + Pythagoras

$AB$ is a diameter of a circle with radius 5 cm. $C$ lies on the circumference and $AC = 6$ cm. Find $BC$.

By Theorem 2: $\angle ACB = 90°$ (angle in semicircle).

Triangle $ACB$ is right-angled at $C$ with hypotenuse $AB = 2 \times 5 = 10$ cm.

By [[Pythagoras Theorem]]:

$$BC = \sqrt{AB^2 - AC^2} = \sqrt{100 - 36} = \sqrt{64} = 8 \text{ cm}$$

(This is the 6-8-10 triple, a scaled version of 3-4-5.)

### Example 3 (0606 / A-Level): Multi-theorem chain

$A$, $B$, $C$, $D$ lie on a circle. $AB$ is a diameter. $\angle CAB = 32°$.

**(a)** Find $\angle ACB$.

$\angle ACB = 90°$ (Theorem 2: angle in semicircle)

**(b)** Find $\angle ABC$.

$\angle ABC = 180° - 90° - 32° = 58°$ (angles in a triangle)

**(c)** Find $\angle ADB$.

$\angle ADB = 90°$ (Theorem 2: angle in semicircle, since $AB$ is a diameter)

**(d)** Find $\angle ADC$.

$\angle ADC = \angle ADB + \angle BDC$

$\angle BDC = \angle BAC = 32°$ (Theorem 3: angles in same segment, both subtended by arc $BC$)

$\angle ADC = 90° + 32° = 122°$

**Check:** $\angle ABC + \angle ADC = 58° + 122° = 180°$ ✓ (Theorem 4: cyclic quadrilateral)

---

## Common Misconceptions (Teaching Notes)

### 1. Confusing the angle at the centre with the reflex angle

**Wrong:** Student reads $\angle AOB$ as the reflex angle ($> 180°$) instead of the acute/obtuse angle, or vice versa.

**Fix:** Always check which arc you're working with. The angle at the centre and the angle at the circumference must be subtended by the **same arc**. Draw the arc clearly and label it. If the circumference angle is on the major arc, the central angle is the one "inside" the same arc — which will be the minor (non-reflex) central angle.

### 2. Cyclic quadrilateral — thinking ADJACENT angles sum to 180°

**Wrong:** "Angle A + Angle B = 180°" (these are adjacent, not opposite).

**Fix:** It's **opposite** angles that sum to $180°$. Draw the quadrilateral, label it clearly, and identify which pairs are opposite. In $ABCD$: $A$ is opposite $C$, $B$ is opposite $D$.

### 3. Applying circle theorems when points aren't on the circle

**Wrong:** Student assumes a point is on the circumference when it's actually inside or outside the circle.

**Fix:** Circle theorems only apply to points ON the circle (for circumference angles) or at the CENTRE (for central angles). Always check the diagram — if a point is not explicitly on the circle, don't apply the theorems.

### 4. Forgetting to state the theorem in "Give reasons" questions

**Wrong:** Student writes the correct angle but doesn't name the theorem.

**Fix:** The mark scheme requires a **reason**. Use the exact phrasing:
- "angle at centre = twice angle at circumference"
- "angle in a semicircle = 90°"
- "angles in the same segment are equal"
- "opposite angles of a cyclic quadrilateral are supplementary"

These phrases are what examiners look for. Abbreviations or vague descriptions ("circle theorem") will not earn the reason mark.

---

## Exam Notes

### OxAQA 9260

**Syllabus ref: G8.** All four theorems in this card are required, along with their converses. Questions typically involve:
- Finding 2–3 missing angles using a chain of theorems (4–6 marks)
- "Give a reason for each step" — name the theorem precisely
- "Show that" questions using the converse of Theorem 4 (prove a quadrilateral is cyclic)
- Combined with [[Angles in Parallel Lines (Vocab)|parallel line rules]] when a tangent or chord creates parallel lines

The 9260 is notably more demanding than 0580 on circle theorems — it requires all eight theorems (four here, four in [[Circle Theorems II]]) and expects multi-step proof chains.

### Cambridge 0580

**Core (C4.7):** Only Theorem 2 (angle in semicircle = 90°) is required at Core level, plus tangent ⊥ radius (covered in [[Circle Theorems II]]).

**Extended (E4.7):** Adds chord properties (perpendicular bisector, equal chords equidistant from centre) — but notably does NOT require Theorems 1, 3, or 4. The 0580 Extended is significantly less demanding than 9260 on circle theorems.

### A-Level

Circle theorems appear in A-Level Pure Mathematics, typically in the context of coordinate geometry (equation of a circle $x^2 + y^2 = r^2$ and the general form). The angle-in-semicircle theorem is used to prove that the angle between a line from $(-r, 0)$ to a point on the circle and a line from $(r, 0)$ to the same point is always $90°$ — connecting the geometric theorem to coordinate proof.

### IB AA

Circle theorems are not explicitly in the IB syllabus, but the underlying ideas appear in the geometry option (HL) and are assumed knowledge for many proof-based questions.

---

## Connections

- **Prerequisites:** [[Circle Vocabulary (Vocab)]] — all terminology (arc, chord, segment, etc.) used in theorem statements
- **Prerequisites:** [[Angle Properties (Vocab)]] — angles on a straight line ($180°$), angles in a triangle, exterior angle theorem (used in proofs)
- **Prerequisites:** [[Angles in Parallel Lines (Vocab)]] — alternate angles appear when parallel North lines meet circles (bearings + circle problems)
- **Prerequisites:** [[Triangles (Vocab)]] — isosceles triangle properties (the engine of every proof)
- **Leads to:** [[Circle Theorems II]] — tangent ⊥ radius, tangents from external point, perpendicular bisector of chord, alternate segment theorem
- **Leads to:** [[Geometrical Proof]] — chaining circle theorems to prove geometric results
- **Leads to:** [[Similarity]] — the same-segment theorem guarantees similar triangles in many configurations
- **Application:** [[Sine and Cosine Rules]] — the circumradius formula $\dfrac{a}{\sin A} = 2R$ is proved using Theorem 1
- **Application:** [[Pythagoras Theorem]] — Theorem 2 creates right-angled triangles inscribed in circles

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\angle AOB$ | `\angle AOB` | Central angle |
| $\angle APB$ | `\angle APB` | Inscribed (circumference) angle |
| $90°$ | `90°` | Right angle (Theorem 2) |
| $180°$ | `180°` | Supplementary (Theorem 4) |
| $360°$ | `360°` | Full turn (used in Theorem 4 proof) |
| $\boxed{\text{result}}$ | `\boxed{\text{result}}` | Final proof result |
