---
chinese: 比例尺图 (bǐlìchǐ tú)
prerequisites:
  - "[[Ratio (Vocab)]]"
  - "[[Proportion (Vocab)]]"
  - "[[Similarity]]"
leads_to: []
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E4-3
  - syllabus/9260-G12
  - type/vocabulary
  - notation/scale-ratio
---

# Scale Drawings 比例尺图

## Definition

A **scale drawing** is a representation of a real-world object, drawn in a *fixed proportion* to its true size — every distance on the drawing is the same fraction of the corresponding real distance. Maps, blueprints, and engineering drawings are all scale drawings.

The relationship is captured by a **scale**, expressed in three equivalent ways:

1. As a **ratio** with the same units: "$1 : 50{,}000$" means 1 unit on the drawing = 50,000 units in reality.
2. As a **representative fraction**: $\dfrac{1}{50{,}000}$ — the drawing is 50,000 times smaller than reality.
3. As a **statement of correspondence**: "1 cm represents 500 m" or "1 inch = 1 mile" — direct unit-conversion form.

All three express the same scale; choose whichever is convenient for the problem.

### 中文锚点

**比例尺图 (bǐlìchǐ tú)** = 按一定比例缩小（或放大）画出的实物图。**比例尺 (bǐlìchǐ)** = scale.

| 形式 | 中文 | 示例 |
|---|---|---|
| 比 | 比例尺 $1:50000$ | 图上 $1$ 厘米代表实际 $50000$ 厘米 = $500$ 米 |
| 分数 | 缩小 $\dfrac{1}{50000}$ | "缩小为原来的五万分之一" |
| 文字陈述 | "$1$ cm 代表 $500$ m" | direct unit form |

注意：比例尺**两边单位必须一致**（都是 cm 或都是 m）才能写成纯数字比 $1 : n$。

---

## Three Forms — convertible

A geological survey map at scale $1 : 25{,}000$ means:

- **Ratio form:** $1 : 25{,}000$ (the small "1" is on the *map*, the big "25,000" is in *reality*).
- **Fraction:** $\dfrac{1}{25{,}000}$ — the map is one twenty-five-thousandth of reality.
- **Statement form:** "1 cm on the map = 25,000 cm in reality = 250 m."

To convert ratio → statement, just pick a convenient unit for the "1" side and convert the other side. To convert statement → ratio, ensure both sides use the *same* unit, then read off the multiplier.

> [!warning] Both sides of the ratio must use the same unit
> "$1 : 50{,}000$" with no unit on either side implicitly means "1 unit : 50,000 same units." If the drawing is in cm and reality is in cm, we have a clean numeric ratio. But "1 cm : 500 m" is *not* a numeric ratio — convert to common units first (1 cm : 50,000 cm) to get the numeric form $1 : 50{,}000$.

---

## Worked Examples

### Example 1 — using the scale to find a real distance

> A map has scale $1 : 25{,}000$. Two towns are $8$ cm apart on the map. What is the real distance?

Real distance = $8$ cm × $25{,}000$ = $200{,}000$ cm = $2{,}000$ m = $2$ km.

### Example 2 — going the other way

> A house is $15$ m wide. On a plan with scale $1 : 100$, what width should be drawn?

Drawing width = $15$ m ÷ $100$ = $0.15$ m = $15$ cm.

### Example 3 — area scaling

> A field of area $400$ m² appears on a map with scale $1 : 1000$. What is the field's area on the map?

Lengths scale by $\dfrac{1}{1000}$. Areas scale by $\left(\dfrac{1}{1000}\right)^2 = \dfrac{1}{1{,}000{,}000}$.

Map area = $400$ m² ÷ $1{,}000{,}000$ = $0.0004$ m² = $4$ cm². (Cross-check: a $20 \text{ m} \times 20 \text{ m}$ field becomes $2 \text{ cm} \times 2 \text{ cm} = 4$ cm² on the map. ✓)

> [!info] Length scales by $k$, area by $k^2$, volume by $k^3$
> If the scale (length ratio) is $1 : k$, then the *area* ratio is $1 : k^2$ and the *volume* ratio is $1 : k^3$. This is the **square-cube law** in disguise — see [[Similarity]] for the full treatment. The "linear by $k$, area by $k^2$, volume by $k^3$" pattern is universal across geometry: photographs, scale models, biological allometry, all of it.

### Example 4 — comparing two maps

> One map shows the city at $1 : 50{,}000$; another at $1 : 10{,}000$. Which has more detail?

The map with the *smaller denominator* (i.e., $1:10{,}000$) shows things larger and so contains more detail — every real metre takes 10 cm of paper instead of 2. The "$1$ cm represents fewer real units" map is more zoomed in.

This is a common confusion: a $1:1000$ map is *larger-scale* (more detail) than a $1:1{,}000{,}000$ map, even though the number $1{,}000{,}000$ is bigger.

---

## Common Mistakes

1. **Forgetting unit conversion.** "$1$ cm represents $5$ km" must be converted to a unit-consistent ratio: $1$ cm : $500{,}000$ cm = $1 : 500{,}000$.
2. **Multiplying by the wrong direction.** Drawing → real: *multiply* by the scale. Real → drawing: *divide* by the scale.
3. **Forgetting area scales by the square.** A $1:100$ scale model has $\dfrac{1}{10{,}000}$ the surface area of the original (not $\dfrac{1}{100}$).
4. **Forgetting volume scales by the cube.** A $1:100$ scale model has $\dfrac{1}{1{,}000{,}000}$ the volume — and *that's* why a photographed insect can look the size of a dog but its weight scaled to dog-size would be enormous.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E4.3 — read and use scales on maps and diagrams; convert between scale forms; use scales to find real distances. Standard patterns:

- "On a map with scale $1 : 200{,}000$, the distance between two cities is $7.5$ cm. Find the real distance in km."
- "A bedroom in a flat is $4.5$ m by $3.2$ m. Draw a scale plan using a scale of $1 : 50$." (Drawing: $9 \text{ cm} \times 6.4 \text{ cm}$.)
- "A field has actual area $12{,}000$ m². On a map of scale $1 : 1000$, find the area on the map." ($k = 1000$, $k^2 = 10^6$, area = $0.012$ m² = $120$ cm².)

---

## Connections

- **Prerequisite:** [[Ratio (Vocab)]] — scale is a ratio
- **Prerequisite:** [[Proportion (Vocab)]] — drawings preserve proportional structure
- **Sibling:** [[Similarity]] — the formal "$k$, $k^2$, $k^3$" scaling law for similar shapes
- **Application:** *cartography* — every map is a scale drawing; large-scale vs small-scale terminology
- **Application:** *engineering drawings* — blueprints, exploded diagrams, mechanical CAD
- **Application:** *biology* — Galileo's square-cube law (why elephants are not just scaled-up mice)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $1 : 50{,}000$ | `1 : 50{,}000` | scale ratio with thousands separator |
| $\dfrac{1}{50{,}000}$ | `\dfrac{1}{50{,}000}` | representative fraction |
| $k, k^2, k^3$ | `k, k^2, k^3` | length, area, volume scale factors |
