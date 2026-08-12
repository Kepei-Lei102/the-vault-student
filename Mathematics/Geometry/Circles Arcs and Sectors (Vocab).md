---
chinese: 圆、弧和扇形 (yuán, hú hé shànxíng)
prerequisites:
  - "[[Circle Vocabulary (Vocab)]]"
  - "[[Angle Properties (Vocab)]]"
leads_to:
  - "[[Radians]]"
  - "[[Surface Area and Volume (Vocab)]]"
  - "[[Compound Shapes (Vocab)]]"
  - "[[Area and Perimeter (Vocab)]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - syllabus/9260-G16
  - syllabus/9260-G18
  - syllabus/9260-G18-Ext
  - syllabus/0580-E5-3
  - type/vocabulary
  - notation/pi
  - misconception/arc-vs-chord
  - misconception/sector-vs-segment
  - misconception/leave-pi-exact
---

# Circles, Arcs and Sectors 圆、弧和扇形

## Definition

Once you know what a circle's parts are called (see [[Circle Vocabulary (Vocab)]]), this card is the **measurement layer**: how long is an arc, how big is a sector, how do you handle segments and composite shapes. The four formulas to know cold: circumference, area, arc length, sector area.

### 中文锚点

圆的周长 $C = 2\pi r$，面积 $A = \pi r^2$。弧长按角度比例分：$s = \frac{\theta}{360°} \cdot 2\pi r$；扇形面积 $A_{扇} = \frac{\theta}{360°} \cdot \pi r^2$。中国学生这些公式早就熟了 — 这张卡的重点是 **英文术语** 和 **精确答案留 $\pi$**。

## Core Formulas (Degrees)

| Quantity | Formula | English name |
|----------|---------|--------------|
| Circumference | $C = 2\pi r = \pi d$ | circumference / perimeter of the circle |
| Area of circle | $A = \pi r^2$ | area |
| Arc length | $s = \dfrac{\theta}{360°} \cdot 2\pi r$ | arc length |
| Sector area | $A_{\text{sec}} = \dfrac{\theta}{360°} \cdot \pi r^2$ | sector area |
| Perimeter of sector | $P_{\text{sec}} = s + 2r$ | perimeter of the sector (arc + two radii) |
| Segment area | $A_{\text{seg}} = A_{\text{sec}} - A_{\triangle}$ | segment area (sector minus triangle) |

where $\theta$ is the angle at the centre (in degrees) and $A_\triangle$ is the area of the triangle formed by the two radii and the chord.

> [!info] Why the $\theta/360$ factor?
> A full circle is $360°$. A sector at angle $\theta$ is just the fraction $\theta/360$ of the whole — so its arc is that fraction of the circumference and its area is that fraction of the full area. Same logic both times. If you can write "fraction of the circle," you can always rebuild these formulas.

![[sector-formulas.svg]]

Left: the sector — two radii of length $r$ bound an arc $s$, with central angle $\theta$. Right: a segment is what's left of a sector after you subtract the triangle formed by the two radii and the chord. (For more parts of a circle — diameter, chord, tangent — see [[Circle Vocabulary (Vocab)]].)

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| arc | 弧 (hú) | A portion of the circumference |
| arc length | 弧长 (húcháng) | The *distance along* the curved arc, not the straight-line chord |
| chord | 弦 (xián) | Straight line segment joining two points on the circle |
| sector | 扇形 (shànxíng) | "Pizza slice" — bounded by two radii and an arc |
| segment | 弓形 (gōngxíng) | "Crust piece" — bounded by a chord and an arc |
| minor / major | 劣 / 优 | Smaller / larger of two arcs or segments ($< 180°$ vs $> 180°$) |
| central angle | 圆心角 (yuánxīnjiǎo) | The angle $\theta$ at the centre subtending the arc |
| subtend | 所对 | "The arc subtends an angle of $\theta$ at the centre" = the arc is the one this angle opens onto |
| inscribed angle | 圆周角 (yuánzhōujiǎo) | An angle at the circumference subtending the same arc |
| circumference | 周长 (zhōucháng) | Perimeter of the whole circle |
| perimeter (of a sector) | 扇形周长 | Arc length **plus** the two radii — don't forget the radii |
| exact value | 精确值 | Answer with $\pi$ (and surds) kept as symbols |

> [!warning] Arc length ≠ chord length
> The **arc** is the curved path along the circle; the **chord** is the straight line between the same two endpoints. Arc length is always longer than chord length (except when both are zero). Exam phrasing: "find the length of the arc $AB$" means the curve, not the chord $AB$.

> [!warning] Sector vs segment — the classic trap
> **Sec**tor has the **c**entre — two radii to the centre. **Seg**ment doesn't — a chord instead. Drawing both quickly on scrap paper before answering saves silly errors.

> [!warning] Leave $\pi$ exact unless told otherwise
> A question asking for "the exact area" or "area in terms of $\pi$" forbids decimals. Write $18\pi \text{ cm}^2$, not $56.5 \text{ cm}^2$. If a question says "give your answer correct to 3 significant figures," *then* compute numerically. When unsure, give both: the exact form first, then the decimal in brackets.

> [!tip] Exam phrasing
> - "**Find the length of arc $AB$.**" → Use the arc length formula; answer in length units.
> - "**Find the perimeter of the sector.**" → Arc length $+$ $2r$. Missing the radii is a classic lost mark.
> - "**Find the area of the shaded region.**" → Usually segment area = sector area − triangle area, or compound shape = circle area − sector.
> - "**Leave your answer in terms of $\pi$.**" → Do not convert to a decimal. $12\pi$ stays $12\pi$.
> - "The minor arc **subtends** an angle of $60°$ at the centre." → The central angle is $60°$; use $\theta = 60$ in the formulas.

## Worked snapshot

A sector of a circle with radius $r = 6\text{ cm}$ has a central angle of $\theta = 120°$.

- Arc length: $s = \dfrac{120}{360} \cdot 2\pi(6) = \dfrac{1}{3} \cdot 12\pi = 4\pi \text{ cm}$.
- Sector area: $A_{\text{sec}} = \dfrac{120}{360} \cdot \pi(6)^2 = \dfrac{1}{3} \cdot 36\pi = 12\pi \text{ cm}^2$.
- Perimeter of the sector: $P = 4\pi + 2(6) = (4\pi + 12) \text{ cm}$.

Final answers in *exact* form unless the question demands a decimal.

## Exam Notes

### OxAQA 9260

**G16** — Circumference $C = 2\pi r = \pi d$, area $A = \pi r^2$, including composite shapes. Every 9260 paper has at least one circle question; most demand exact answers.

**G18 Ext** — Arc lengths, sector areas, angles of sectors. Typical task: "A sector has radius $r$ and area $A$; find the central angle," or "find the perimeter of the shaded region," which usually combines sector with triangle or rectangle.

### Cambridge 0580 Extended

**E5.3** — Circumference, area, arc length, sector area. 2–4 marks per question; examiner rewards showing the fraction $\theta/360$ explicitly before substituting.

### Cambridge 0606

Arc/sector formulas reappear in **7.1 (Circular Measure)** using **radians** instead of degrees: $s = r\theta$ and $A_{\text{sec}} = \frac{1}{2} r^2 \theta$. Same geometry, cleaner formulas — see [[Radians]].

## Connections

- **Prerequisite:** [[Circle Vocabulary (Vocab)]] — radius, diameter, chord, sector, segment defined there.
- **Prerequisite:** [[Angle Properties (Vocab)]] — angles summing to $360°$ at a point.
- **Leads to:** [[Radians]] — same formulas with angle in radians become $s = r\theta$ and $A = \frac{1}{2} r^2 \theta$.
- **Used in:** [[Surface Area and Volume (Vocab)|Surface Area and Volume]] — a cone's curved surface unrolls into a sector.
- **Used in:** [[Compound Shapes (Vocab)|Compound Shapes]] — many composite-area problems combine sectors with triangles or rectangles.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\pi$ | `\pi` | Keep symbolic for exact answers |
| $\theta$ | `\theta` | Central angle |
| $r$ | `r` | Radius |
| $\dfrac{\theta}{360°}$ | `\dfrac{\theta}{360°}` | Fraction of the full circle |
| $2\pi r$ | `2\pi r` | Circumference |
| $\pi r^2$ | `\pi r^2` | Area |
