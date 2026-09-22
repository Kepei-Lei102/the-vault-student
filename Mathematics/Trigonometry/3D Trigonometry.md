---
chinese: 立体三角学 (lìtǐ sānjiǎoxué)
prerequisites:
  - "[[Trigonometric Ratios]]"
  - "[[Sine and Cosine Rules]]"
  - "[[Pythagoras Theorem]]"
  - "[[Solids (Vocab)]]"
  - "[[Bearings (Vocab)]]"
leads_to:
  - "[[Magnitude of a Vector (Vocab)]]"
  - "[[Vector Geometry]]"
tags:
  - subject/mathematics
  - domain/trigonometry
  - level/IGCSE-extension
  - level/A-Level
  - curriculum/Cambridge-0580
  - syllabus/0580-E6-6
  - syllabus/9260-G19
  - type/deep
  - type/technique
  - type/application
  - misconception/3d-angle-by-eye
---

# 3D Trigonometry 立体三角学

## Definition

**3D trigonometry** is the application of standard trig (Pythagoras, SOH-CAH-TOA, sine rule, cosine rule) to triangles drawn *inside three-dimensional solids* — cuboids, pyramids, prisms. The challenge isn't new trigonometry; it's **identifying the right triangle in 3D**, where the geometry is harder to see and the relevant angles can hide.

The master technique: **find a 2D right triangle inside the 3D solid by "dropping a perpendicular,"** then apply familiar 2D trig to that triangle. The art is choosing *which* perpendicular to drop.

This card covers:
1. **Length of the space diagonal** of a cuboid
2. **Angle between a line and a plane**
3. **Angle between two planes**
4. **Sine and cosine rules in 3D** (applied within a triangle that lies in 3D space)

### 中文锚点

**立体三角学 (lìtǐ sānjiǎoxué)** = 在三维立体（长方体、棱锥、棱柱等）中应用三角函数。新东西不多——还是勾股、SOH-CAH-TOA、正弦/余弦定理；难点在**找对那个直角三角形**。

核心技巧：**作辅助线 (zuò fǔzhùxiàn) "drop a perpendicular"** —— 把 3D 问题变成 2D 直角三角形。

四个标准问题：

| 类型 | 中文 | 方法 |
|---|---|---|
| 体对角线长度 | 求**体对角线** (tǐ duìjiǎoxiàn) | 两次勾股 (gōugǔ liǎng cì) |
| 直线与平面的夹角 | 线面角 (xiànmiànjiǎo) | 投影到平面，找直角三角形 |
| 两平面的夹角 | 二面角 (èrmiànjiǎo) | 在交线上各作垂线 |
| 立体内三角形的边角 | 正余弦定理 | 把 3D 中的三角形当 2D 用 |

---

## Setup 1 — Cuboid Space Diagonal

The **space diagonal** of a cuboid is the line from one corner to the *opposite* corner (passing through the interior). For a cuboid with edge lengths $a, b, c$:

$$\boxed{\;d = \sqrt{a^2 + b^2 + c^2}\;}$$

**Derivation (two applications of Pythagoras):**

1. The diagonal of the *base* (a $a \times b$ rectangle) has length $\sqrt{a^2 + b^2}$ by Pythagoras in 2D.
2. The space diagonal sits in the right triangle formed by the base diagonal (length $\sqrt{a^2 + b^2}$) and the cuboid's height $c$. Pythagoras gives $d^2 = (a^2 + b^2) + c^2 = a^2 + b^2 + c^2$.

The "$\sqrt{a^2 + b^2 + c^2}$" formula is the 3D Pythagoras — generalising naturally to any number of dimensions (the magnitude of a 3D vector $\begin{pmatrix} a \\ b \\ c \end{pmatrix}$, see [[Magnitude of a Vector (Vocab)]]).

---

## Setup 2 — Angle Between a Line and a Plane

The **angle between a line and a plane** is defined as the angle between the line and its **projection onto the plane**.

**Construction:**
1. Take the line, say from point $A$ to point $B$ (where $B$ lies *off* the plane).
2. Drop a perpendicular from $B$ to the plane — the foot of the perpendicular is some point $B'$ in the plane.
3. The projection of the line $AB$ onto the plane is the segment $AB'$.
4. The angle between the line and the plane is $\angle BAB'$ — the angle at $A$ in the right triangle $ABB'$.

The **right triangle** $ABB'$ has:
- $AB$ = the original line (the "slant" or hypotenuse)
- $AB'$ = the projection (one leg, in the plane)
- $BB'$ = the perpendicular (other leg, perpendicular to the plane)

Once you have this right triangle, apply SOH-CAH-TOA: $\sin\theta = \dfrac{BB'}{AB}$ and $\cos\theta = \dfrac{AB'}{AB}$.

> [!warning] The angle is at $A$ — the foot of the line *in* the plane
> The angle between line and plane is measured at the *intersection* of the line with the plane, not at the high point. In the construction, $A$ is the foot in the plane and $\angle BAB'$ is the angle. This is also why the angle is always between $0°$ and $90°$ — it's the smallest angle from line to plane, achieved by projecting straight down.

---

## Setup 3 — Angle Between Two Planes

The **angle between two planes** (also called the **dihedral angle**) is harder to construct because two planes meet along a *line*, and you have to be careful where you measure.

**Construction:**
1. Find the **line of intersection** of the two planes.
2. From a point on that line, draw a line *in each plane* that is perpendicular to the line of intersection.
3. The angle between those two perpendiculars is the angle between the planes.

Equivalent: imagine slicing through both planes with a third plane perpendicular to the line of intersection. That slice intersects each plane in a line, and the angle between those two lines is the dihedral angle.

**Example.** A book opened to some angle has two cover-planes meeting at the spine. The dihedral angle is what you'd measure by laying a protractor flat *across* the spine — it's the angle of the book's "openness."

---

## Setup 4 — Sine and Cosine Rules in 3D

**Once you've identified a triangle inside the 3D solid**, you can apply the standard 2D rules to *that triangle's vertices and sides* — the triangle is 2D internally, even though its corners live in 3D.

- **Sine rule:** $\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C}$
- **Cosine rule:** $a^2 = b^2 + c^2 - 2bc\cos A$
- **Area rule:** $\text{Area} = \tfrac{1}{2} ab \sin C$

The 3D-specific step is *finding the side lengths* and *angles* — usually via Pythagoras in some sub-rectangle of the solid. Once you have all the sides, the rules apply unchanged.

---

## Worked Example — Cuboid with Multiple Quantities

> A cuboid has dimensions $4 \times 3 \times 12$ cm. Find:
> (a) the length of the space diagonal,
> (b) the angle between the space diagonal and the base ($4 \times 3$ rectangle).

![[3d-trig-cuboid.svg]]

The red line is the space diagonal $A \to G$. Its projection onto the base is the amber dashed diagonal $A \to C$ (length $5$). The green vertical edge $C \to G$ (length $12$) is the perpendicular. The right triangle $A$-$C$-$G$ — extracted into 2D in your workings — gives both the diagonal length (Pythagoras) and the angle to the base (SOH-CAH-TOA).

### (a) Space diagonal

Two applications of Pythagoras:
- Base diagonal: $\sqrt{4^2 + 3^2} = \sqrt{25} = 5$ cm.
- Space diagonal: $\sqrt{5^2 + 12^2} = \sqrt{169} = 13$ cm. ✓

(Notice the $5$-$12$-$13$ Pythagorean triple — Cambridge loves these for clean numbers.)

### (b) Angle to the base

Set up the right triangle: the space diagonal is the hypotenuse ($13$ cm); its projection onto the base is the base diagonal ($5$ cm); the perpendicular is the cuboid's height ($12$ cm).

$$\tan\theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{\text{height}}{\text{base diagonal}} = \frac{12}{5}.$$

$$\theta = \tan^{-1}\!\left(\frac{12}{5}\right) \approx 67.4°.$$

**Answer.** Space diagonal = $13$ cm; angle to base $\approx 67.4°$.

> [!info] Why the angle is so steep
> A $4 \times 3 \times 12$ cuboid is *much* taller than it is wide. The space diagonal sweeps mostly *upward*, so it makes a large angle ($> 45°$) with the base. If the cuboid were a cube ($a = b = c$), the angle would be $\tan^{-1}(\sqrt 2) \approx 54.7°$. The taller the cuboid, the steeper the diagonal.

---

## Worked Example — Square-Based Pyramid

> A square-based pyramid has base side $6$ cm and slant edges (apex to base corners) all $9$ cm. Find:
> (a) the perpendicular height $h$ from apex to base,
> (b) the angle between a slant edge and the base,
> (c) the angle between a face and the base.

![[3d-trig-pyramid.svg]]

**Setup.** Call the apex $V$, the centre of the base $O$, and the four base corners $A, B, C, D$. The slant edge $VA$ (red), the perpendicular height $VO$ (green), and the projection $OA$ (amber dashed) form the right triangle $V$-$O$-$A$ — that's the 2D triangle you'd redraw in your working space.

### (a) Perpendicular height

The right triangle is $V$-$O$-$A$ (where $A$ is any corner): $VA = 9$ (slant edge), $OA$ = half the base diagonal = $\tfrac{1}{2}(6\sqrt 2) = 3\sqrt 2$, and $VO = h$ (perpendicular height).

Pythagoras: $h^2 = 9^2 - (3\sqrt 2)^2 = 81 - 18 = 63$, so $h = \sqrt{63} = 3\sqrt{7} \approx 7.94$ cm.

### (b) Angle between slant edge and base

The slant edge is $VA$. Its projection onto the base is $OA$. The angle is in the right triangle $V$-$O$-$A$ at corner $A$:

$$\sin\theta = \frac{VO}{VA} = \frac{3\sqrt 7}{9} = \frac{\sqrt 7}{3}, \quad \theta = \sin^{-1}\!\left(\frac{\sqrt 7}{3}\right) \approx 61.9°.$$

### (c) Angle between a face and the base

Pick the face $V$-$A$-$B$ (a triangular face). Its line of intersection with the base is the edge $AB$. From a point on $AB$ (say its midpoint $M$), draw perpendiculars to $AB$ in each plane:
- In the base plane: from $M$ to the centre $O$. Length $OM = 3$ cm (half of the base side $6$).
- In the face plane: from $M$ to the apex $V$. Length $VM$ is the *slant height* of the face. $V$ sits $h = 3\sqrt 7$ above $O$ and $M$ lies in the base $3$ cm from $O$, so in the right triangle $V$-$O$-$M$, $VM = \sqrt{h^2 + 3^2} = \sqrt{63 + 9} = \sqrt{72} = 6\sqrt 2$ cm. (The face triangle gives the same number by a different right triangle: $VA = 9$ and $AM = 3$, so $VM = \sqrt{9^2 - 3^2} = \sqrt{72}$.)

The angle is between $OM$ (length $3$) and $VM$ (length $6\sqrt 2$), measured at $M$ in the right triangle $V$-$O$-$M$.

$$\cos\phi = \frac{OM}{VM} = \frac{3}{6\sqrt 2} = \frac{1}{2\sqrt 2}, \quad \phi \approx 69.3°.$$

> [!tip] Always sketch in 3D first, then extract the 2D triangle
> 0580 examiners draw a wireframe of the solid and label all corners. Your job: **redraw the 2D right triangle on a separate piece of working space**, label its sides, and apply Pythagoras / SOH-CAH-TOA to *that flat triangle*. Trying to "do trig in 3D" by inspection without extracting the 2D triangle is how mistakes happen. Cambridge markschemes specifically reward the explicit 2D-triangle sketch.

---

## Common Mistakes

1. **Eyeballing the angle in the 3D drawing.** The drawing's *visible* angle isn't the *true* angle — it's distorted by projection. Always extract the 2D right triangle and compute.
2. **Confusing slant edge with slant height.** In a pyramid: a *slant edge* connects apex to a base corner; a *slant height* connects apex to the midpoint of a base edge (the foot of perpendicular in the face). They're different lengths, and they appear in different angle-calculation problems.
3. **Wrong perpendicular.** For "angle between line and plane," drop a perpendicular from the line *to the plane*. For "angle between two planes," draw perpendiculars *from a point on the line of intersection*, one in each plane.
4. **Using the projection's length where you wanted the perpendicular's length.** In the cuboid example, $\tan\theta = \tfrac{\text{height}}{\text{base diagonal}}$. If you used the *space diagonal* instead of the base diagonal, you'd get the wrong angle.
5. **Forgetting Pythagoras-twice for space diagonal.** The single formula $d = \sqrt{a^2 + b^2 + c^2}$ encodes the two applications. You can use it directly, but if you derive from scratch you must do *both* steps.

---

## Exam Notes

### Cambridge 0580 (IGCSE)

**Syllabus ref:** E6.6, Extended content only: "Carry out calculations and solve problems in three dimensions using Pythagoras' theorem and trigonometry, including calculating the angle between a line and a plane." The Core paper has no three-dimensional row; C6 stops at right-angled triangles and bearings. Standard exam patterns:

- "A cuboid measures $a \times b \times c$. Find (i) the space diagonal, (ii) the angle between the space diagonal and the base."
- "A square pyramid has base side $s$ and slant edge $\ell$. Find the perpendicular height and the angle between a slant edge and the base."
- "A triangular prism has cross-section [given]. Find the angle between [some line] and [some face]."
- "Find the area of triangle $XYZ$ where $X, Y, Z$ are corners of the cuboid." (Apply Pythagoras to find $XY, YZ, XZ$; then cosine rule for an angle; then $\tfrac{1}{2}ab\sin C$ for area.)

The angle between two *planes* (Setup 3) is not named in E6.6; it appears on 0580 papers only as an angle between a line and a plane in disguise (the slant height of a face against the base), so a candidate who can find the line-plane angle has the whole row.

> [!tip] Always show the 2D right-triangle sketch
> Markschemes credit "showing the 2D triangle drawn separately" as a method mark. Don't just compute — sketch the extracted triangle, label its sides with values you've found, and write the trig ratio used. This is a 2-mark improvement on most 3D trig questions.

### OxfordAQA 9260 (IGCSE)

**Syllabus ref:** G19. Core content: "know the formula for Pythagoras' theorem $a^2 + b^2 = c^2$ and the trigonometric ratios" and apply them in right-angled triangles. Extension content: "including 3D figures". So every question on this card is Extension on 9260, with the same cuboid, pyramid and prism shapes as 0580; the angle between a line and a plane is not named separately but is examined inside the 3D figures.

### Cambridge 9709 (A Level), Paper 3 vectors

Three-dimensional angles reappear in 9709 §3.7 by the vector route: "use formulae to calculate the scalar product of two vectors, and use scalar products in problems involving lines and points", with the note that "questions may involve 3D objects such as cuboids, tetrahedra (pyramids), etc." The angle between two edges or diagonals of a cuboid is then $\cos\theta = \dfrac{\mathbf{a}\cdot\mathbf{b}}{\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert}$ ([[Vector Geometry]]); the syllabus covers lines only, so the angle between a line and a plane and the angle between two planes are not examined on 9709. The vector product is also excluded.

### Where this is *not* examined

Cambridge 0606 (Additional Mathematics) has no three-dimensional trigonometry row; its only mention of three dimensions is the assessment objective "recognise and use spatial relationships in two and three dimensions", and its trigonometry content is identities, equations and graphs. No IB or AP mathematics row is claimed for this card.

---

## Connections

- **Prerequisite:** [[Pythagoras Theorem]] — used twice for the space diagonal
- **Prerequisite:** [[Trigonometric Ratios]] — SOH-CAH-TOA on the extracted 2D triangle
- **Prerequisite:** [[Sine and Cosine Rules]] — for non-right triangles in 3D
- **Sibling:** [[Solids (Vocab)]] — the 3D shapes inside which we work
- **Forward:** [[Magnitude of a Vector (Vocab)]] — 3D vector magnitude $\sqrt{x^2 + y^2 + z^2}$ is exactly the space-diagonal formula
- **Forward:** [[Vector Geometry]] — vectors give the algebraic shortcut for 3D angles via the dot product
- **Application:** *engineering* — every CAD model relies on 3D angle calculations; structural engineering computes load angles in 3D; aerospace deals with attitude and orientation in 3D
- **Application:** *crystallography* — angles between crystal faces (dihedral angles) determine mineral identity
- **Beyond syllabus:** *spherical trigonometry* — extends to triangles drawn on the surface of a sphere; foundation of celestial navigation and GPS

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $d = \sqrt{a^2 + b^2 + c^2}$ | `\sqrt{a^2 + b^2 + c^2}` | 3D Pythagoras (space diagonal) |
| $\sin\theta = \dfrac{\text{height}}{\text{slant}}$ | `\sin\theta = \dfrac{\text{height}}{\text{slant}}` | line-plane angle |
| $\angle (line, plane)$ | dihedral / line-plane angle | always between $0°$ and $90°$ |
| $a^2 = b^2 + c^2 - 2bc\cos A$ | cosine rule | applies to any triangle, including ones in 3D |
