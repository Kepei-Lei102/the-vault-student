---
chinese: 方位角 (fāngwèijiǎo)
prerequisites:
  - "[[Angle Properties (Vocab)]]"
  - "[[Angles in Parallel Lines (Vocab)]]"
leads_to:
  - "[[Sine and Cosine Rules]]"
  - "[[3D Trigonometry]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-G12
  - syllabus/0580-E4-3
  - type/vocabulary
  - misconception/bearing-from-vs-to
---

# Bearings 方位角

## Definition

A **bearing** (方位角) is a way of describing direction using a three-figure angle measured **clockwise from North**. Bearings are used in navigation, surveying, and geography — and they are one of the most distinctively "English-curriculum" topics at IGCSE.

### The three rules

1. **Measured from North** (the vertical "up" direction at the starting point)
2. **Measured clockwise**
3. **Always written as three figures** — so due East is $090°$, not $90°$

### 中文锚点

方位角 = 从正北方向顺时针量到目标方向的角度，必须写成三位数。这个概念在中国数学课不常出现，但在英国考试中非常常见。关键：方位角是从**出发点**的北方量的，不是从目标点。

---

## Why Bearings Exist

Ordinary words like "turn left" or "head northeast" are too vague when precision matters. A ship captain in open ocean has no roads or landmarks — "a bit to the right of north" could mean anything from $010°$ to $050°$ depending on who says it. Bearings collapse every possible direction into **a single number**, removing all ambiguity.

The system solves three problems at once:

1. **Universality.** Anyone with a compass and the same reference (true north or magnetic north) reads the same angle, regardless of language. A Chinese navigator and an English pilot both understand $135°$.
2. **Mathematical composability.** Once direction is just an angle $\theta$, you can compute with it — displacement components become $d\sin\theta$ and $d\cos\theta$, and problems reduce to trigonometry. This is exactly why bearing questions at IGCSE always lead into [[Trigonometric Ratios]] or [[Sine and Cosine Rules]].
3. **Compactness.** Three digits encode $360$ possible directions (to the nearest degree). The three-figure convention ($045°$ not $45°$) exists to prevent miscommunication — in noisy radio conditions, "forty-five" could be confused with "four five zero" or other fragments, but "zero four five" is unambiguous.

The military adopted bearings for artillery (where "a little to the left" gets people killed), aviation took them for flight paths and air traffic control, and surveying uses them to define legal land boundaries. Even hiking relies on them when trails disappear and you navigate by map and compass alone.

> [!tip] 为什么选"从北顺时针"？
> 北方是最容易确定的参考方向（指南针天然指向南北），而顺时针与钟表一致，是人类最直觉的旋转方向。这两个选择让方位角系统既自然又实用。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| bearing | 方位角 | Three-figure clockwise angle from North |
| three-figure bearing | 三位数方位角 | Always three digits: $045°$, $120°$, $270°$ |
| clockwise | 顺时针 (shùnshízhēn) | The direction of measurement |
| North | 北 (běi) | The reference direction; drawn as a vertical line upward |
| "the bearing of B from A" | 从 A 到 B 的方位角 | Measured at point **A**, looking toward B |
| back bearing | 反方位角 | The bearing for the return journey; differs by $180°$ |

---

## Cardinal Directions as Bearings

| Direction | Bearing |
|-----------|---------|
| North | $000°$ |
| East | $090°$ |
| South | $180°$ |
| West | $270°$ |
| North-East | $045°$ |
| South-West | $225°$ |

---

## Key Skills

### "The bearing of B from A"

This phrase means: **stand at A, face North, turn clockwise until you face B.** The angle you've turned is the bearing. The measurement happens at the **starting point** (A), not the destination.

### Back bearings

If the bearing of B from A is $\theta$, the bearing of A from B (the return journey) is:

$$\theta + 180° \quad \text{if } \theta < 180° \qquad \text{or} \qquad \theta - 180° \quad \text{if } \theta \geq 180°$$

> [!tip] WHY ± 180°?
> At point B, North points the same direction as at A (all North lines are parallel). The direction from B back to A is exactly opposite to the direction from A to B — and "opposite" on a compass means $180°$ apart. The parallel North lines mean the co-interior / alternate angle rules from [[Angles in Parallel Lines (Vocab)]] apply directly.

### Bearings + trigonometry

Most bearing questions at Extension involve a triangle formed by two points and the North line. You then apply [[Trigonometric Ratios]] (right-angled) or [[Sine and Cosine Rules]] (non-right-angled) to find distances or angles.

---

## Common Mistakes

1. **"Bearing of B from A" — measuring at the wrong point.** The bearing is measured at **A** (the "from" point), not at B. Drawing the North line at A is the first step.
2. **Forgetting to write three figures.** $45°$ must be written $045°$. This is a "free mark lost" situation.
3. **Measuring anticlockwise.** Bearings are always clockwise. If you naturally find an anticlockwise angle of $60°$, the bearing is $360° - 60° = 300°$.
4. **Back bearing errors.** Adding $180°$ to $250°$ gives $430°$, which is more than $360°$ — subtract $360°$ to get $070°$. Or equivalently, subtract $180°$: $250° - 180° = 070°$.

---

## Exam Notes

### OxAQA 9260 / Cambridge 0580

**Syllabus ref:** G12 (9260) / E4.7 (0580). Bearings appear as standalone "find the bearing" questions (2 marks) and as part of trigonometry problems (4–6 marks). At Extension, expect: multi-leg journeys (A → B → C), combined with sine/cosine rules, and "find the bearing of the return journey." Always draw a North line at every point mentioned.

---

## Connections

- **Prerequisite:** [[Angle Properties (Vocab)]] — angles on a line, angles at a point
- **Prerequisite:** [[Angles in Parallel Lines (Vocab)]] — parallel North lines create alternate/co-interior angle patterns
- **Leads to:** [[Sine and Cosine Rules]] — bearing problems generate non-right triangles
- **Leads to:** [[3D Trigonometry]] — bearings extend to elevation angles in 3D problems
- **Parallel:** [[Trigonometric Ratios]] — bearing + distance = right-angled trig in the simplest cases
