---
chinese: 变换 (biànhuàn)
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Equation of a Straight Line (Vocab)]]"
  - "[[Quadrilaterals (Vocab)]]"
  - "[[Symmetry (Vocab)]]"
leads_to:
  - "[[Matrix Transformations]]"
  - "[[Graphs of Functions]]"
  - "[[Congruence]]"
  - "[[Similarity]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-G21
  - syllabus/0580-E7-1
  - type/vocabulary
  - misconception/enlargement-negative-sf
  - misconception/rotation-direction
---

# Transformations 变换

## Definition

A **transformation** maps every point in the plane to a new position according to a fixed rule. At IGCSE, there are four transformations to know, each described by specific information.

### 中文锚点

变换 = 把图形上的每个点按规则移到新位置。四种变换：平移（translation）、反射（reflection）、旋转（rotation）、放大/缩小（enlargement）。每种变换的"描述"需要不同的信息——考试最常考"完整描述变换"。

---

## The Four Transformations

### 1. Translation 平移

Slides every point the same distance in the same direction. Described by a **column vector**:

$$\begin{pmatrix} a \\ b \end{pmatrix}$$

where $a$ = horizontal shift (positive = right) and $b$ = vertical shift (positive = up).

**To describe:** "Translation by the vector $\begin{pmatrix} a \\ b \end{pmatrix}$."

### 2. Reflection 反射

Flips every point across a **mirror line**. Each point and its image are equidistant from the line, on opposite sides.

**To describe:** "Reflection in the line $\_\_\_$." Common mirror lines: $x$-axis ($y = 0$), $y$-axis ($x = 0$), $y = x$, $y = -x$, or any line $x = k$ / $y = k$.

### 3. Rotation 旋转

Turns every point around a fixed **centre** by a given **angle** in a given **direction**.

**To describe — three pieces of information:**
1. **Centre** of rotation (a point)
2. **Angle** of rotation
3. **Direction** — clockwise or anticlockwise

"Rotation of $90°$ anticlockwise about the origin $(0, 0)$."

### 4. Enlargement 放大/缩小

Scales every point away from (or toward) a fixed **centre** by a **scale factor** $k$.

**To describe — two pieces of information:**
1. **Centre** of enlargement
2. **Scale factor** $k$

| Scale factor | Effect |
|---|---|
| $k > 1$ | Shape gets bigger |
| $0 < k < 1$ | Shape gets smaller (a "reduction") |
| $k < 0$ | Shape gets bigger/smaller AND inverted (rotated $180°$ through the centre) |
| $k = -1$ | Same size, rotated $180°$ — equivalent to a half-turn |

> [!warning] "Enlargement" can make things smaller
> In everyday English, "enlarge" means "make bigger." In maths, an enlargement with $0 < k < 1$ makes the shape **smaller**. And $k < 0$ flips it through the centre. The word is misleading — it just means "scaling from a centre."

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| transformation | 变换 | A mapping of points in the plane |
| image | 像 (xiàng) | The result after the transformation |
| object | 原像 (yuánxiàng) | The original shape before transformation |
| invariant | 不变的 (bùbiàn de) | A point or property that doesn't change |
| congruent | 全等的 | Same shape AND same size — translations, reflections, rotations produce congruent images |
| similar | 相似的 | Same shape, possibly different size — enlargements produce similar images |
| scale factor | 比例因子 / 缩放系数 | The multiplier $k$ in an enlargement |
| column vector | 列向量 (liè xiàngliàng) | Used to describe translations |
| mirror line / line of reflection | 对称轴 / 镜线 | The line a reflection flips across |
| centre of rotation | 旋转中心 | The fixed point everything rotates around |
| centre of enlargement | 放大中心 | The fixed point rays are drawn from |

---

## Describing Transformations Fully

The most common exam question: **"Describe fully the single transformation that maps A onto B."**

The word **"fully"** means you must state:

| Transformation | Required information |
|---|---|
| Translation | Vector |
| Reflection | Mirror line equation |
| Rotation | Centre, angle, direction |
| Enlargement | Centre, scale factor |

Missing any piece loses marks. And you must name the transformation type — "it moves 3 right and 2 up" without the word "translation" is incomplete.

---

## Common Mistakes

1. **Forgetting the direction for rotation.** "$90°$ rotation about $(0,0)$" is incomplete — you must say clockwise or anticlockwise. ($180°$ is the exception — direction doesn't matter.)
2. **Negative scale factor confusion.** $k = -2$ means the image is twice the size AND on the opposite side of the centre. Students often draw it twice the size on the same side.
3. **Writing "move" instead of "translation."** The exam wants the mathematical name.
4. **Not giving the mirror line as an equation.** "Reflected in the $y$-axis" is fine, but "reflected in that diagonal line" is not — you need $y = x$ or $y = -x$ or whatever the equation is.

---

## Exam Notes

### OxAQA 9260 / Cambridge 0580

**Syllabus ref:** G21 (9260) / E5.1 (0580). "Describe fully" questions are worth 2–3 marks and appear on almost every paper. At Extension, expect: combined transformations (one followed by another), negative scale factors, and finding the centre of enlargement by drawing rays. The connection to [[Matrix Transformations]] is 9260 Extension / 0606 territory.

---

## Connections

- **Prerequisite:** [[Cartesian Coordinates (Vocab)]] — transformations are described on the coordinate plane
- **Prerequisite:** [[Equation of a Straight Line (Vocab)]] — mirror lines are equations of lines
- **Leads to:** [[Matrix Transformations]] — reflections, rotations, and enlargements can all be represented as $2 \times 2$ matrices
- **Leads to:** [[Graphs of Functions]] — graph transformations ($y = f(x-a)$, $y = -f(x)$, etc.) are the function-world analogue of geometric transformations
- **Parallel:** [[Quadrilaterals (Vocab)]] — symmetry properties of quadrilaterals are described via reflections and rotations
