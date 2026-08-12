---
chinese: 勾股定理 (gōugǔ dìnglǐ) / 毕达哥拉斯定理 (Bìdágēlāsī dìnglǐ)
prerequisites:
  - "[[Powers and Roots (Vocab)]]"
leads_to:
  - "[[Trigonometric Ratios]]"
  - "[[Sine and Cosine Rules]]"
  - "[[3D Trigonometry]]"
  - "[[Vectors]]"
  - "[[Surds]]"
  - "[[Congruence]]"
  - "[[Geometrical Proof]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/AP
  - syllabus/9260-G19
  - syllabus/0580-E6-1
  - type/theorem
  - notation/squared
  - misconception/c-is-always-the-longest
  - misconception/forgetting-the-square-root
---

# Pythagoras' Theorem 勾股定理

## Definition

### Formal

In a **right-angled triangle**, the square of the hypotenuse equals the sum of the squares of the other two sides:

$$a^2 + b^2 = c^2$$

where $c$ is the length of the **hypotenuse** (the side opposite the right angle) and $a$, $b$ are the lengths of the other two sides.

**Converse:** If three lengths satisfy $a^2 + b^2 = c^2$, then the triangle is right-angled.

### Intuitive — Squares on the Sides

Imagine building a physical square on each side of a right-angled triangle. The area of the big square (on the hypotenuse) equals the combined area of the two smaller squares. That's it — the theorem is about **area**. The algebra $a^2 + b^2 = c^2$ is just a shorthand for this geometric fact.

This makes "squared" literal: $a^2$ IS the area of a square with side $a$ (see [[Powers and Roots (Vocab)]] for WHY the word "squared" comes from geometry).

### 中文锚点 (Chinese Anchor)

勾股定理：**直角三角形中，斜边的平方等于两直角边平方之和。**

| 中文 | English | Key idea |
|------|---------|----------|
| 勾 (gōu) | Shorter leg | The shorter side of the right angle (historically = 3) |
| 股 (gǔ) | Longer leg | The longer side of the right angle (historically = 4) |
| 弦 (xián) | Hypotenuse | The side opposite the right angle (historically = 5) |
| 直角三角形 (zhíjiǎo sānjiǎoxíng) | Right-angled triangle | A triangle with one 90° angle |
| 斜边 (xiébiān) | Hypotenuse | Literally "slanting side" — the longest side |

> [!info] 勾三股四弦五
> The Chinese name predates Pythagoras. The *Zhoubi Suanjing* (《周髀算经》, ~1000 BCE) records the 3-4-5 relationship: 勾 = 3, 股 = 4, 弦 = 5. The theorem is called 勾股定理 in China, not 毕达哥拉斯定理, reflecting this independent discovery.

## Notation

| Symbol | Meaning | Notes |
|--------|---------|-------|
| $c$ | Hypotenuse | Always the side **opposite** the right angle — the longest side |
| $a$, $b$ | The other two sides | Sometimes called "legs" or "catheti" |
| $\square$ | Right angle marker | The small square drawn in the corner |

## Key Facts

### 1. Using the Theorem — Finding a Side

**Finding the hypotenuse:** given the two shorter sides.

$$c = \sqrt{a^2 + b^2}$$

**Example:** $a = 5$, $b = 12$ → $c = \sqrt{25 + 144} = \sqrt{169} = 13$

**Finding a shorter side:** given the hypotenuse and the other side.

$$a = \sqrt{c^2 - b^2}$$

**Example:** $c = 10$, $b = 6$ → $a = \sqrt{100 - 36} = \sqrt{64} = 8$

> [!warning] Don't forget the square root
> Students often calculate $a^2 + b^2$ and write it as the answer. The answer is $\sqrt{a^2 + b^2}$, not $a^2 + b^2$. The theorem gives you the square of the hypotenuse — you still need to take the root.

### 2. Pythagorean Triples

A **Pythagorean triple** is a set of three positive integers $(a, b, c)$ where $a^2 + b^2 = c^2$. These give "nice" answers with no surds.

| Triple | Check |
|--------|-------|
| $(3, 4, 5)$ | $9 + 16 = 25$ ✓ |
| $(5, 12, 13)$ | $25 + 144 = 169$ ✓ |
| $(8, 15, 17)$ | $64 + 225 = 289$ ✓ |
| $(7, 24, 25)$ | $49 + 576 = 625$ ✓ |

**Scaling rule:** If $(a, b, c)$ is a triple, then so is $(ka, kb, kc)$ for any positive integer $k$. So $(3, 4, 5) \to (6, 8, 10) \to (9, 12, 15) \to \ldots$

**WHY this matters in exams:** Recognising a triple saves time. If you see a right-angled triangle with sides 6 and 8, you know immediately $c = 10$ without calculation. Examiners frequently use triples (or scaled triples) to keep the arithmetic clean.

### 3. The Converse — Testing for Right Angles

The converse is just as useful as the theorem itself:

**If** $a^2 + b^2 = c^2$ (where $c$ is the longest side), **then** the triangle is right-angled.

**If** $a^2 + b^2 > c^2$, the triangle is **acute** (all angles < 90°).

**If** $a^2 + b^2 < c^2$, the triangle is **obtuse** (one angle > 90°).

**Example:** A triangle has sides 7, 10, 12. Is it right-angled?

$7^2 + 10^2 = 49 + 100 = 149$, but $12^2 = 144$. Since $149 > 144$, the triangle is **acute** (not right-angled, and no angle exceeds 90°).

### 4. Pythagoras in the Coordinate Plane — the Distance Formula

The distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ IS Pythagoras:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**WHY:** Draw a horizontal line from $(x_1, y_1)$ to $(x_2, y_1)$ and a vertical line up to $(x_2, y_2)$. You've made a right-angled triangle. The horizontal leg has length $\lvert x_2 - x_1 \rvert$, the vertical leg has length $\lvert y_2 - y_1 \rvert$, and the hypotenuse is the distance you want. Apply Pythagoras.

### 5. Pythagoras in 3D

For a cuboid with dimensions $l$, $w$, $h$, the space diagonal is:

$$d = \sqrt{l^2 + w^2 + h^2}$$

**WHY:** Apply Pythagoras twice. First, find the diagonal of the base: $d_{\text{base}} = \sqrt{l^2 + w^2}$. Then form a right-angled triangle with this base diagonal and the height $h$: $d = \sqrt{d_{\text{base}}^2 + h^2} = \sqrt{l^2 + w^2 + h^2}$.

This is a common 9260 Extension question: "Find the length of the space diagonal of a cuboid" or "Find the angle the space diagonal makes with the base."

## Proofs — WHY It Works

### Proof 1 — 赵爽弦图 (Zhào Shuǎng's Diagram)

This is the most elegant visual proof, from China (~3rd century CE).

![[pythagoras-proof-zhao-shuang.svg|700]]

**Construction:** Take four identical right-angled triangles with legs $a$, $b$ and hypotenuse $c$. Arrange them inside a large square of side $(a + b)$:

$$\text{Large square area} = (a + b)^2$$

The four triangles leave a tilted square of side $c$ in the middle:

$$\text{Large square area} = 4 \times \dfrac{1}{2}ab + c^2 = 2ab + c^2$$

Setting them equal:

$$(a + b)^2 = 2ab + c^2$$

$$a^2 + 2ab + b^2 = 2ab + c^2$$

$$a^2 + b^2 = c^2 \qquad \square$$

**WHY this proof is beautiful:** It uses nothing but area. No algebra was needed historically — the diagram alone makes the equality visible. The $2ab$ cancels from both sides, and what remains is the theorem. This is the proof that was known in China centuries before Pythagoras.

### Proof 2 — Rearrangement (Algebraic)

![[pythagoras-proof-rearrangement.svg|700]]

Start with the same four triangles, but arrange them differently inside a square of side $c$:

The square has area $c^2$. Remove the four triangles (total area $4 \times \dfrac{1}{2}ab = 2ab$). What remains is a square of side $(b - a)$:

$$c^2 = 2ab + (b - a)^2 = 2ab + b^2 - 2ab + a^2 = a^2 + b^2 \qquad \square$$

### Proof 3 — Similar Triangles (Euclid's Approach)

![[pythagoras-proof-similar-triangles.svg|700]]

Drop a perpendicular from the right angle to the hypotenuse, splitting the triangle into two smaller triangles. Both smaller triangles are similar to the original (AA similarity — they share an angle with the original, and both have a right angle).

From similarity:
- $\dfrac{a}{c} = \dfrac{d}{a}$ → $a^2 = cd$ (where $d$ is the projection of side $a$ onto the hypotenuse)
- $\dfrac{b}{c} = \dfrac{e}{b}$ → $b^2 = ce$ (where $e$ is the projection of side $b$)

Adding: $a^2 + b^2 = cd + ce = c(d + e) = c \cdot c = c^2 \qquad \square$

**WHY this proof matters at A-Level:** It introduces the altitude-on-hypotenuse technique, which generates two key results that appear in many problems: $a^2 = cd$ and $b^2 = ce$ (the geometric mean relationships).

> [!info] How many proofs exist?
> Over 400 distinct proofs of Pythagoras' theorem have been published, including one by US President James Garfield (using a trapezium, 1876). It is probably the most-proved theorem in all of mathematics. The diversity of proofs shows how deeply the result is woven into geometry, algebra, and analysis.

## Common Misconceptions (Teaching Notes)

### 1. Applying Pythagoras to non-right-angled triangles

**Wrong:** Student uses $a^2 + b^2 = c^2$ on a triangle that doesn't have a right angle.

**Fix:** Always check for the right angle first. If there's no right angle, you need the cosine rule instead (see [[Sine and Cosine Rules]]).

### 2. Calling any side $c$

**Wrong:** Student labels a shorter side as $c$ and gets a negative number under the square root.

**Fix:** $c$ is ALWAYS the hypotenuse — the side **opposite** the right angle. It must be the longest side. If your calculation gives $c^2 = a^2 - b^2$ and you get a negative result, you've mislabelled the sides.

### 3. Forgetting to take the square root

**Wrong:** "$a^2 + b^2 = 25 + 144 = 169$, so the hypotenuse is 169."

**Fix:** $c^2 = 169$, so $c = \sqrt{169} = 13$. The theorem gives you $c^2$, not $c$.

### 4. Not simplifying surds

**Wrong:** "$c = \sqrt{50}$" left as final answer.

**Fix:** Simplify: $\sqrt{50} = \sqrt{25 \times 2} = 5\sqrt{2}$. See [[Surds]] for the full technique. Some exam questions explicitly say "give your answer in the form $a\sqrt{b}$."

### 5. Applying 3D Pythagoras in one step when the question wants two

**Wrong:** Student jumps straight to $d = \sqrt{l^2 + w^2 + h^2}$ without showing the two-step process.

**Fix:** In "Show that" questions, you must show both applications of Pythagoras separately. Find the base diagonal first, then the space diagonal.

## Exam Notes

### OxAQA 9260 (Extension)

**Syllabus ref:** G19 — Pythagoras' theorem in 2D; Extension includes 3D figures.

- Pythagoras appears on almost every paper, either standalone or embedded in multi-step problems.
- Common question types: find a missing side, find a distance between two points, space diagonal of a cuboid, combined with trigonometry.
- Extension: 3D problems — finding lengths and angles within prisms, pyramids, and cuboids. These always involve applying Pythagoras twice (once in a face, once in a cross-section).
- The converse is testable: "Show that triangle ABC is right-angled."

### Cambridge 0580 Extended

**Syllabus ref:** E6.1 — Pythagoras' theorem in 2D.

- Paper 2 (non-calculator): expect integer answers (Pythagorean triples) or simple surds.
- Paper 4 (calculator): expect decimal answers, often combined with trigonometry.
- 0580 does not explicitly test 3D Pythagoras at Extended level, but it can appear in compound problems.

### AP / IB / A-Level

- **IB Mathematics AA/AI:** Pythagoras is assumed knowledge (prior learning). It underpins the distance formula, vector magnitudes, and trigonometric identities.
- **A-Level:** $\cos^2\theta + \sin^2\theta = 1$ IS Pythagoras applied to the unit circle. This identity (and the two derived from it) appears throughout A-Level Pure and Further Mathematics.
- **AP Calculus:** Arc length formula $\int \sqrt{1 + \left(\dfrac{dy}{dx}\right)^2}\, dx$ is Pythagoras applied to infinitesimal right-angled triangles along a curve — see [[Differentiation]] for the infinitesimal mindset.

> [!info] Beyond syllabus — Pythagoras meets everything
> Pythagoras' theorem is arguably the most connected result in all of mathematics. The identity $\cos^2\theta + \sin^2\theta = 1$ is Pythagoras on the unit circle. The distance formula is Pythagoras in coordinates. The magnitude of a vector $\lvert \mathbf{v} \rvert = \sqrt{v_x^2 + v_y^2}$ is Pythagoras again. In physics, $E^2 = (pc)^2 + (mc^2)^2$ (Einstein's energy-momentum relation) has the same structure. In machine learning, the Euclidean distance used to measure similarity between data points is — you guessed it — Pythagoras. One theorem, discovered independently by multiple civilisations, appearing wherever geometry meets algebra.

## Connections

**Prerequisites:**
- [[Powers and Roots (Vocab)]] — squares and square roots; "squared" literally means area of a square

**Leads to:**
- [[Trigonometric Ratios]] — SOH-CAH-TOA requires a right-angled triangle; Pythagoras finds the missing side
- [[Sine and Cosine Rules]] — generalise Pythagoras to non-right-angled triangles; cosine rule reduces to Pythagoras when angle = 90°
- [[3D Trigonometry]] — apply Pythagoras twice to find lengths in 3D
- [[Vectors]] — magnitude $\lvert \mathbf{v} \rvert = \sqrt{v_x^2 + v_y^2}$ is Pythagoras
- [[Surds]] — many Pythagoras answers are irrational ($\sqrt{2}$, $5\sqrt{3}$, etc.)

**Parallel concepts:**
- [[Similarity]] — Euclid's proof (Proof 3) uses similar triangles
- [[Differentiation]] — arc length formula is Pythagoras on infinitesimal triangles
- [[Matrix Transformations]] — distance-preserving transformations (reflections, rotations) preserve Pythagoras

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $a^2 + b^2 = c^2$ | `a^2 + b^2 = c^2` | The theorem |
| $\sqrt{a^2 + b^2}$ | `\sqrt{a^2 + b^2}` | Finding the hypotenuse |
| $\sqrt{c^2 - b^2}$ | `\sqrt{c^2 - b^2}` | Finding a shorter side |
| $\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ | `\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}` | Distance formula |
| $\sqrt{l^2 + w^2 + h^2}$ | `\sqrt{l^2 + w^2 + h^2}` | 3D space diagonal |
