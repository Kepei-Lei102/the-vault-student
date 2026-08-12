---
chinese: 圆定理（二）(yuán dìnglǐ èr)
prerequisites:
  - "[[Circle Vocabulary (Vocab)]]"
  - "[[Circle Theorems I]]"
  - "[[Angle Properties (Vocab)]]"
  - "[[Triangles (Vocab)]]"
  - "[[Pythagoras Theorem]]"
  - "[[Congruence]]"
leads_to:
  - "[[Geometrical Proof]]"
  - "[[Similarity]]"
  - "[[Coordinate Geometry of the Circle]]"
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
  - notation/tangent
  - misconception/tangent-not-perpendicular
  - misconception/alternate-segment-confusion
---

# Circle Theorems II 圆定理（二）

This card covers the four **tangent and chord** circle theorems — the ones involving tangent lines, chord perpendiculars, and the alternate segment. Together with [[Circle Theorems I]], these complete the eight classical theorems tested at 9260 Extension.

## Why These Theorems Exist

[[Circle Theorems I]] relied on one master idea: **equal radii create isosceles triangles**. The theorems in this card rely on a second master idea: **a tangent touches a circle at exactly one point, and at that point the tangent is "as perpendicular to the radius as possible."** Everything about tangents — equal tangents from an external point, the alternate segment theorem — follows from this single perpendicularity fact.

The chord-bisection theorem (Theorem 3 below) is slightly different: it relies on the **reflection symmetry** of a circle about any diameter. Drop a perpendicular from the centre to a chord, and you can "fold" the circle along that perpendicular — the two halves of the chord match, so they must be equal.

![[circle-theorems-ii-overview.svg|700]]

## 中文锚点

本张卡片涉及圆的**切线**与**弦**相关的四个定理。中国中学课程对这些定理并不陌生，但英国考试特别强调**推理链**和**定理名称的英文陈述**。四个定理：

1. **切线垂直于过切点的半径**（tangent ⊥ radius at the point of tangency）
2. **从外一点引出的两条切线长度相等**（tangents from an external point are equal）
3. **圆心到弦的垂线平分弦**（perpendicular from centre bisects chord）
4. **弦切角定理**：切线与弦所成的角等于另一段弧上的圆周角（alternate segment theorem）

在英国考试中，最难的是第四条 **alternate segment theorem**，学生常常不知道哪个角等于哪个角。掌握这张卡的关键是**画图、标注、用字母明确说出两个相等的角**。

---

## Theorem 1 — Tangent Perpendicular to Radius

> **A tangent to a circle is perpendicular to the radius drawn to the point of tangency.**

In symbols: if $T$ is the point where line $\ell$ touches the circle with centre $O$, then:

$$OT \perp \ell \quad \Leftrightarrow \quad \angle OTP = 90° \text{ for any point } P \text{ on } \ell$$

### Intuitive explanation

Imagine you're standing at the centre $O$ and a line is drifting past the circle. When the line just barely touches the circle (becomes tangent), the closest point on the line to $O$ is exactly the point of tangency $T$. The shortest distance from a point to a line is always along the perpendicular — so $OT$ must be perpendicular to the tangent.

Equivalently: if $OT$ were *not* perpendicular, you could draw a shorter line from $O$ to $\ell$, and that shorter line would enter the circle — meaning $\ell$ cuts through the circle, not just touches it. Contradiction.

### Proof (by contradiction)

**Setting up the proof.** First, rewrite the theorem as an **"if ... then ..."** statement so we can see exactly what to negate:

> **If** a line $\ell$ is tangent to a circle at point $T$, **then** $\ell$ is perpendicular to the radius $OT$.

Call this "**if** $P$, **then** $Q$." Proof by contradiction works by assuming **$P$ is true** but **$Q$ is false**, then deriving a logical impossibility. So:

- $P$: $\ell$ is tangent to the circle at $T$ (touches the circle at exactly one point).
- $Q$: $\ell \perp OT$.
- **not $Q$**: $\ell$ is NOT perpendicular to $OT$.

**Our assumption for contradiction: $\ell$ is tangent to the circle at $T$, AND $\ell$ is not perpendicular to $OT$.**

From this single assumption, we will show $\ell$ must cross the circle at a second point — contradicting the fact that $\ell$ is a tangent (touches only at $T$).

![[circle-theorems-ii-proof-tangent.svg|700]]

**Step 1.** Since $\ell$ is not perpendicular to $OT$, we can drop a perpendicular from $O$ to the line $\ell$, and its foot $N$ is a **different point** from $T$. (If the foot coincided with $T$, then $ON = OT$ would itself be perpendicular to $\ell$ — but we assumed it isn't.) So $N \neq T$.

**Step 2.** By construction, $\angle ONT = 90°$. So triangle $ONT$ is right-angled at $N$, with hypotenuse $OT$. By [[Pythagoras Theorem]]:

$$OT^2 = ON^2 + NT^2$$

Since $N \neq T$ gives $NT > 0$, we have $NT^2 > 0$, so:

$$ON^2 < OT^2 \quad \Longrightarrow \quad ON < OT$$

**Step 3.** But $OT = r$ (the radius). Therefore:

$$ON < r$$

This means the point $N$ lies **strictly inside** the circle (its distance from the centre is less than the radius).

**Step 4.** Any straight line that passes through a point inside a circle must cross the circle at **two** distinct points. (Geometrically: the line enters the disk at one boundary point and exits at another.) So our line $\ell$ crosses the circle at two points, not one.

**Contradiction.** This contradicts $P$ — the assumption that $\ell$ is a tangent (touches the circle at only one point).

**Conclusion.** Our extra assumption "not $Q$" must be false. Therefore $Q$ is true:

$$\boxed{OT \perp \ell}$$

> [!tip] Why this theorem is the workhorse
> Every tangent problem starts by marking the right angle at the point of tangency. As soon as you draw the radius to a tangent point, you get a right-angled triangle — and all the Pythagoras, trigonometry, and angle-sum tools open up.

---

## Theorem 2 — Tangents from an External Point

> **The two tangents drawn from an external point to a circle are equal in length.**

In symbols: if $P$ is a point outside the circle and $PA$, $PB$ are tangents touching the circle at $A$ and $B$, then:

$$PA = PB$$

### Intuitive explanation

From an external point $P$, the two tangent segments are the two "arms" of a symmetric kite $PAOB$ (where $O$ is the centre). The kite has a line of symmetry along $PO$ — so flipping the figure along $PO$ swaps $A$ and $B$, which means $PA = PB$.

### Proof

![[circle-theorems-ii-proof-twotangents.svg|700]]

**Step 1.** Draw the radii $OA$ and $OB$ to the tangent points, and draw $OP$.

**Step 2.** By Theorem 1, $\angle OAP = \angle OBP = 90°$ (tangent $\perp$ radius).

**Step 3.** Consider triangles $OAP$ and $OBP$:
- $OA = OB = r$ (equal radii)
- $OP = OP$ (common side)
- $\angle OAP = \angle OBP = 90°$

By the **RHS congruence** rule (Right angle, Hypotenuse, Side), triangles $OAP$ and $OBP$ are congruent.

**Step 4.** Corresponding sides of congruent triangles are equal:

$$\boxed{PA = PB}$$

### Bonus — things that follow for free

Since $\triangle OAP \cong \triangle OBP$:
- $\angle APO = \angle BPO$ — the line $PO$ **bisects** $\angle APB$
- $\angle AOP = \angle BOP$ — the line $PO$ bisects $\angle AOB$

So $PO$ is the **axis of symmetry** of the whole kite $PAOB$.

> [!tip] Kite recognition
> $PAOB$ is always a kite: two pairs of equal adjacent sides ($PA = PB$ and $OA = OB$), with the axis of symmetry along the diagonal $PO$.

---

## Theorem 3 — Perpendicular from Centre Bisects Chord

> **The perpendicular from the centre of a circle to a chord bisects the chord.**
>
> **Equivalently:** the perpendicular bisector of any chord passes through the centre.

In symbols: if $AB$ is a chord and $M$ is the foot of the perpendicular from $O$ to $AB$, then:

$$AM = MB$$

### Intuitive explanation

A circle is symmetric about every diameter. If you drop a perpendicular from the centre $O$ to a chord $AB$, you can **fold** the circle along that perpendicular — the fold maps $A$ onto $B$ because both are the same distance from the fold line. So $AM = MB$.

### Proof

![[circle-theorems-ii-proof-chord.svg|700]]

**Step 1.** Let $M$ be the foot of the perpendicular from $O$ to chord $AB$, so $\angle OMA = \angle OMB = 90°$.

**Step 2.** Draw the radii $OA$ and $OB$.

**Step 3.** Consider right-angled triangles $OMA$ and $OMB$:
- $OA = OB = r$ (equal radii — the hypotenuses)
- $OM = OM$ (common side)
- $\angle OMA = \angle OMB = 90°$

By **RHS congruence**, triangles $OMA$ and $OMB$ are congruent.

**Step 4.** Corresponding sides: $AM = MB$.

$$\boxed{AM = MB}$$

### The converse

The converse is equally useful in exam problems:

> **The line from the centre to the midpoint of a chord is perpendicular to that chord.**

Proof: swap the RHS argument for SSS — $OA = OB$, $OM = OM$, $AM = MB$ gives $\triangle OMA \cong \triangle OMB$, so $\angle OMA = \angle OMB$. These are supplementary (they sit on the line $AB$), so each is $90°$.

> [!info] Beyond syllabus — the perpendicular bisector is unique
> Any point equidistant from $A$ and $B$ lies on the perpendicular bisector of $AB$. Since $OA = OB$ (radii), the centre $O$ lies on the perpendicular bisector of every chord. This is the principle behind the **circumcentre** of a triangle: the three perpendicular bisectors of the sides all meet at the centre of the circle through the three vertices.

---

## Theorem 4 — Alternate Segment Theorem

> **The angle between a tangent and a chord drawn from the point of tangency equals the angle in the alternate segment.**

In symbols: let $TA$ be a tangent at $T$, and $TB$ be a chord. Then:

$$\angle ATB = \angle TCB$$

where $C$ is any point on the arc on the **opposite side** of chord $TB$ from the tangent.

### What "alternate segment" means

The chord $TB$ divides the circle into two segments. The tangent $TA$ "points into" one segment. The **alternate** segment is the other one — the segment on the far side of the chord from the tangent direction. The inscribed angle in that alternate segment is the one that equals the tangent-chord angle.

### Intuitive explanation

Imagine sliding point $C$ along the arc until it coincides with the tangent direction — in the limit, the chord $TC$ becomes the tangent $TA$, so the inscribed angle $\angle TCB$ continuously becomes the tangent-chord angle $\angle ATB$. The "same segment theorem" from [[Circle Theorems I]] keeps inscribed angles equal as $C$ moves around the arc, and the alternate segment theorem extends that equality all the way to the tangent.

### Proof

![[circle-theorems-ii-proof-alternate.svg|700]]

**Step 1.** Draw the diameter $TD$ through the tangent point $T$.

**Step 2.** By Theorem 1 (tangent $\perp$ radius): $\angle ATD = 90°$.

So $\angle ATB = 90° - \angle DTB$. Call this angle $\theta$, so $\angle DTB = 90° - \theta$.

**Step 3.** By the **semicircle angle theorem** ([[Circle Theorems I]] Theorem 2): $\angle TBD = 90°$ (angle in semicircle).

In triangle $TBD$:
$$\angle BDT = 180° - 90° - (90° - \theta) = \theta$$

**Step 4.** By the **same segment theorem** ([[Circle Theorems I]] Theorem 3), any inscribed angle standing on chord $TB$ and on the same arc as $D$ equals $\angle BDT$:

$$\angle TCB = \angle BDT = \theta = \angle ATB$$

$$\boxed{\angle ATB = \angle TCB}$$

> [!tip] Identifying the "alternate" segment
> **The angle you want is on the OPPOSITE side of the chord from the tangent direction.** In exam diagrams, always mark the tangent-chord angle first, then follow the chord into the "other" region of the circle — the inscribed angle you find there is the equal one.

---

## How the Four Theorems Connect

| Theorem | Key move | What it unlocks |
|---------|----------|-----------------|
| 1. Tangent ⊥ radius | Draw radius to tangent point → right angle | Pythagoras, trig, right-angled triangle toolkit |
| 2. Equal tangents from external point | Use Theorem 1 + RHS congruence | Kite shape, symmetric tangent figures |
| 3. Perpendicular from centre bisects chord | Drop perpendicular → RHS congruence | Chord length ↔ distance from centre ↔ radius |
| 4. Alternate segment theorem | Diameter + semicircle + same segment | Tangent problems linking chord angles to arcs |

Theorems 1 and 2 are about **tangents meeting radii**. Theorem 3 is about **chords meeting perpendiculars from the centre**. Theorem 4 **links tangents to inscribed angles** — it's the bridge back to [[Circle Theorems I]].

---

## Worked Examples

### Example 1 (9260 level) — Tangents from external point

> From an external point $P$, two tangents $PA$ and $PB$ touch a circle with centre $O$ at points $A$ and $B$. Given $PA = 12$ cm and $OA = 5$ cm, find: (a) $PB$, (b) $OP$.

**Solution:**

(a) By Theorem 2, tangents from an external point are equal:
$$PB = PA = 12 \text{ cm}$$

(b) By Theorem 1, $\angle OAP = 90°$. Triangle $OAP$ is right-angled at $A$, with $OA = 5$ (radius) and $PA = 12$ (tangent). By [[Pythagoras Theorem]]:

$$OP = \sqrt{OA^2 + PA^2} = \sqrt{25 + 144} = \sqrt{169} = 13 \text{ cm}$$

### Example 2 (9260 level) — Chord and perpendicular

> A chord $AB$ of a circle has length $16$ cm. The distance from the centre $O$ to the chord is $6$ cm. Find the radius.

**Solution:**

Drop perpendicular from $O$ to $AB$, meeting $AB$ at $M$. By Theorem 3, $AM = MB = 8$ cm.

Triangle $OMA$ is right-angled at $M$ with legs $OM = 6$ and $AM = 8$. By Pythagoras:

$$OA = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10 \text{ cm}$$

Radius $= 10$ cm.

### Example 3 (9260 Extension level) — Alternate segment in a chain

> In the diagram, $TA$ is tangent to the circle at $T$, and $B$, $C$ are points on the circle with $\angle ATB = 35°$ and $\angle BTC = 40°$. Find $\angle BCT$ and $\angle BAT'$ where $T'$ is a point on the tangent opposite to $A$.

**Solution:**

By the **alternate segment theorem** (Theorem 4), the tangent-chord angle equals the inscribed angle in the alternate segment:

$$\angle BCT = \angle ATB = 35°$$

For the other side: $\angle BT'A$ on the tangent on the opposite side of $T$ — this angle equals the inscribed angle in the *other* segment of chord $TB$, which by same-segment theorem sums with $\angle BCT$ along a cyclic quadrilateral. A cleaner approach: the tangent-chord angles on opposite sides of a chord sum to $180°$, so the inscribed angle in the segment on the tangent-direction side is $180° - 35° = 145°$.

This chaining — alternate segment → same segment → cyclic quadrilateral — is exactly what 9260 Extension problems demand.

---

## Common Misconceptions (Teaching Notes)

### 1. Forgetting to mark the right angle at the tangent point

Students draw the tangent and radius but don't mark the $90°$, then miss that the triangle is right-angled and they can use Pythagoras.

**Fix:** Make the habit explicit — *"whenever you see a tangent, immediately draw the radius to the tangent point and mark the right angle with a little square."* Then ask: "What right-angled-triangle tool can you use now?"

### 2. Confusing "equal tangents" with "equal chords"

Students sometimes apply Theorem 2 to a secant or a chord: they see two line segments from an external point and assume both are equal.

**Fix:** Equal tangents requires **both** lines to be tangent (touching the circle at exactly one point). If a line crosses the circle at two points, it's a secant — not a tangent — and Theorem 2 does not apply.

### 3. Misidentifying the "alternate segment"

Students look at the tangent-chord angle and then pick an inscribed angle in the same segment (on the same side of the chord as the tangent). This is wrong — the inscribed angle must be in the *other* segment.

**Fix:** Teach the phrase "**other side of the chord**." Draw the chord, shade the segment the tangent is pointing into, and the alternate segment is the unshaded one. The equal angle lives in the unshaded segment.

### 4. Assuming perpendicular-to-chord passes through centre without proof

Conversely, students sometimes assert "this perpendicular goes through the centre because it's perpendicular to the chord" without justification. The perpendicular bisector passes through the centre; a random perpendicular does not.

**Fix:** Be careful with which version of Theorem 3 you use. *Perpendicular from centre bisects chord.* *Perpendicular bisector passes through centre.* The direction of inference matters.

---

## Exam Notes

### OxAQA 9260

Syllabus reference: **G8** (Circle Theorems). The 9260 specification requires all four tangent/chord theorems. Typical question patterns:

- Tangents from external point + Pythagoras (common)
- Chord length ↔ distance from centre problems
- Alternate segment theorem in multi-step chains ("prove that angle $X$ equals angle $Y$")
- Combined with [[Circle Theorems I]] in proof chains

**Mark pattern:** Each theorem application worth 1 mark, plus 1 mark for stating the theorem name in proof questions. Alternate segment problems often worth 4–5 marks.

### Cambridge 0580 Extended

Syllabus reference: **E4.7** (Circle Theorems). Required theorems at Extended:
- Tangent perpendicular to radius (Theorem 1) ✓
- Tangents from an external point are equal (Theorem 2) ✓
- Perpendicular from centre to chord bisects the chord (Theorem 3) ✓
- **Alternate segment theorem (Theorem 4) is NOT on 0580 Extended**

Paper 4 typically has one circle theorem problem worth 3–5 marks.

### Cambridge 0580 Core

Syllabus reference: **C4.7**. Only Theorem 1 (tangent $\perp$ radius) is required at Core — combined with Pythagoras for tangent length calculations.

### A-Level

Not explicitly in the Pure Mathematics specifications, but circle theorems are prerequisites for the coordinate geometry of circles (AS Pure 1): finding tangent lines to circles uses Theorem 1 directly ("the tangent at $(a,b)$ is perpendicular to the radius at $(a,b)$, so its gradient is the negative reciprocal of the radius gradient").

### IB AA / AI

Circle theorems appear in the Geometry and Trigonometry topic (SL 3 / HL 3) as background for inscribed angles and cyclic quadrilaterals. Alternate segment theorem is not explicitly tested but underlies trigonometric identities involving chord-tangent configurations.

---

## Connections

- **Parent:** [[Circle Vocabulary (Vocab)]] — all terminology used here
- **Sibling:** [[Circle Theorems I]] — angle-based theorems (same exam topic)
- **Proof ingredients:** [[Pythagoras Theorem]], [[Congruence]] (RHS), [[Triangles (Vocab)]]
- **Applications:** [[Geometrical Proof]] — chaining theorems in multi-step problems
- **Extension:** [[Similarity]] — tangent-secant length relationships (power of a point)
- **Beyond high school:** The *power of a point* theorem generalises Theorem 2 — for any external point $P$ and any secant through $P$ cutting the circle at $X, Y$: $PX \cdot PY$ is constant, equal to $PT^2$ for the tangent $PT$.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\perp$ | `\perp` | Perpendicular |
| $\angle$ | `\angle` | Angle symbol — always precede with space |
| $\triangle$ | `\triangle` | Triangle — used in congruence statements |
| $\cong$ | `\cong` | Congruent to — for triangles |
| $\overline{AB}$ | `\overline{AB}` | Segment notation (optional; use sparingly) |
| $\boxed{x}$ | `\boxed{x}` | Box final proof result |
