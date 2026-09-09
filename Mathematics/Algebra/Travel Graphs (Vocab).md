---
chinese: 行程图 (xíngchéngtú) / 距离-时间图 / 速度-时间图
prerequisites:
  - "[[Cartesian Coordinates (Vocab)]]"
  - "[[Gradient (Vocab)]]"
  - "[[Linear Graphs (Vocab)]]"
  - "[[Average Speed (Vocab)]]"
leads_to:
  - "[[Area Under a Graph (Vocab)]]"
  - "[[Kinematics Calculus]]"
  - "[[Differentiation]]"
  - "[[Integration]]"
  - "[[Newton's Laws of Motion]]"
  - "[[SUVAT]]"
tags:
  - subject/mathematics
  - domain/algebra
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E2-9
  - syllabus/0625-1-2
  - syllabus/9702-2-1
  - syllabus/9260-A17
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/Edexcel-IAL
  - curriculum/OxAQA-9660
  - syllabus/0606-14-15
  - syllabus/9709-4-2
  - syllabus/IAL-M1-3-1
  - type/vocabulary
  - type/application
  - misconception/horizontal-on-dt-vs-st
  - misconception/gradient-on-st-is-acceleration
---

# Travel Graphs 行程图

## Definition

A **travel graph** is a graph that records *motion over time*. The horizontal axis is always **time**. The vertical axis is whichever quantity you care about — distance from a start point, or speed. The two standard travel graphs are:

- **Distance–time graph** (d–t graph): vertical = distance from start. *Gradient* = **speed**.
- **Speed–time graph** (s–t graph): vertical = speed. *Gradient* = **acceleration**. *Area under the graph* = **distance travelled**.

Travel graphs let you read off a journey's speed, acceleration, and distance without doing any calculation — purely by looking at gradients and areas.

### 中文锚点

行程图 (xíngchéngtú) 是记录**运动随时间变化**的图像。横轴永远是时间 $t$，纵轴是距离 $s$ 或速度 $v$。两类标准图：

- **距离-时间图** (d-t 图)：纵轴是距离。**斜率 = 速度** (sùdù)。
- **速度-时间图** (s-t 图 / v-t 图)：纵轴是速度。**斜率 = 加速度** (jiāsùdù)。**图下面积 = 距离**。

注意：在 d-t 图上，水平线段表示**静止** (jìngzhǐ)；在 s-t 图上，水平线段表示**匀速** (yúnsù) — 这两个完全不同！

---

## Key Vocabulary

| English | 中文 | Meaning |
|---------|------|---------|
| distance–time graph | 距离-时间图 | $s$ vs $t$; gradient is speed |
| speed–time graph | 速度-时间图 / $v$-$t$ 图 | $v$ vs $t$; gradient is acceleration, area is distance |
| velocity | 速度 (sùdù) | Speed *with direction*; signed quantity |
| speed | 速率 (sùlǜ) / 速度 | Magnitude of velocity (always non-negative) |
| acceleration | 加速度 (jiāsùdù) | Rate of change of velocity ($\text{m/s}^2$) |
| deceleration | 减速 (jiǎnsù) / 负加速度 | Acceleration in the opposite direction; negative on s-t graph |
| stationary | 静止 (jìngzhǐ) | Not moving — horizontal line on a d-t graph |
| constant speed | 匀速 (yúnsù) | Speed unchanging — horizontal line on an s-t graph (or straight line on d-t) |
| uniform acceleration | 匀加速 (yún jiāsù) | Acceleration constant — straight line on s-t graph |
| origin | 原点 (yuándiǎn) | $(0, 0)$ — start of the journey, $t = 0$ |

---

## Distance–Time Graphs

The story:

| What you see on a d-t graph | What it means |
|---|---|
| Straight line, positive gradient | Constant speed, moving away from start |
| Steeper straight line | Faster constant speed |
| Horizontal line | **Stationary** — distance not changing |
| Straight line, negative gradient | Constant speed, **returning toward start** |
| Curve, gradient increasing | **Accelerating** (speeding up) |
| Curve, gradient decreasing | **Decelerating** (slowing down) |

**Speed = gradient = $\dfrac{\text{change in distance}}{\text{change in time}} = \dfrac{\Delta s}{\Delta t}$.** This is exactly the gradient formula from [[Linear Graphs (Vocab)]] — only the labels have changed.

> [!warning] Horizontal line means **stationary**, not "slow"
> A common 0580 mark loss: a student sees a horizontal segment on a d-t graph and writes "moving slowly." Wrong — gradient zero means *speed zero*, i.e. **stopped**. The object is sitting still. Slow movement would be a small-but-nonzero gradient (a very gentle rise).

---

## Speed–Time Graphs

The story:

| What you see on an s-t graph | What it means |
|---|---|
| Horizontal line above the axis | **Constant speed** (not stationary!) |
| Horizontal line at $v = 0$ | Stationary (only when on the axis) |
| Straight line, positive gradient | Uniform acceleration |
| Straight line, negative gradient | Uniform deceleration |
| Curve | Non-uniform (changing) acceleration |
| Steeper line | Larger acceleration |

**Acceleration = gradient = $\dfrac{\Delta v}{\Delta t}$.** Units: $\text{m/s}^2$.

**Distance travelled = area under the s-t graph.** This is the §A17 Extended bullet — see [[Area Under a Graph (Vocab)]] for how to estimate the area when the graph is curvy.

> [!warning] On an s-t graph, *horizontal* means *constant speed*, not stopped
> The same horizontal-line shape means opposite things on the two graphs. A horizontal line on a d-t graph = stationary. A horizontal line on an s-t graph (above the axis) = moving at a constant speed. The difference: on a d-t graph the *quantity is distance*, so unchanging distance means unchanging position. On an s-t graph the *quantity is speed*, so unchanging speed means moving steadily — not stopped. Read the axis label first, then interpret.

---

## Worked Example — reading a journey from a d-t graph

A cyclist's journey from home is recorded:

| Time (min) | $0$ | $10$ | $20$ | $30$ | $50$ |
|---|---|---|---|---|---|
| Distance from home (km) | $0$ | $5$ | $5$ | $15$ | $15$ |

**Segment 1 — $0$ to $10$ min.** Distance increases $0 \to 5$ km. Speed = $\dfrac{5 \text{ km}}{10 \text{ min}} = 0.5$ km/min = **30 km/h**.

**Segment 2 — $10$ to $20$ min.** Distance constant at $5$ km. Gradient $= 0$. **Stationary** for 10 minutes (a snack break, perhaps).

**Segment 3 — $20$ to $30$ min.** Distance increases $5 \to 15$ km. Speed = $\dfrac{10 \text{ km}}{10 \text{ min}} = 1$ km/min = **60 km/h** (faster than segment 1).

**Segment 4 — $30$ to $50$ min.** Distance constant at $15$ km. Stationary again — at the destination.

The whole story comes from gradients alone.

---

## Common Misconceptions

1. **Mixing up d-t and s-t shapes.** Always read the *vertical-axis label* before interpreting. A horizontal line means very different things on the two graphs.
2. **Confusing "back to start" with "stationary."** On a d-t graph, a *negative gradient* (line going down) means returning toward home, not stopping. A horizontal line means stopping.
3. **Computing area under a d-t graph.** The area under a d-t graph has no physical meaning. It's the *area under an s-t graph* that gives distance.
4. **Forgetting unit conversion.** km/min and km/h differ by a factor of $60$. Read the axis units carefully — many exam questions force a conversion at the end.

---

## Exam Notes

**Cambridge 0580 §E2.9.** Read information off a travel graph. Compute speed (or acceleration) as a gradient between two named points. Identify segments where the object is stationary, accelerating, or moving at constant speed. Convert between units (km/h ↔ m/s; the factor is $\div 3.6$). Sketch a journey from a verbal description.

**OxfordAQA 9260 §A17 (graphs in real contexts).** The core bullet is this card — plot and interpret distance–time and speed–time graphs, and solve kinematic problems (distance, speed, acceleration) from them. The **Extension** bullet — estimate gradients of curves and areas under non-linear graphs — is [[Area Under a Graph (Vocab)]]: tangent for an instantaneous speed, trapezium strips for a distance.

**Cambridge 0606 §14.15, 9709 §4.2 (Paper 4), Edexcel IAL M1.3.1, OxfordAQA 9660 M1.1.** Every mechanics paper opens on the same three graphs — $s$–$t$, $v$–$t$, $a$–$t$ — and marks the same two readings: gradient of $s$–$t$ is velocity, gradient of $v$–$t$ is acceleration, area under $v$–$t$ is displacement. The step up from IGCSE is *sign*: a velocity–time graph below the axis is motion the other way, and area below the axis subtracts. [[SUVAT]] carries the constant-acceleration algebra those graphs feed; [[Kinematics Calculus]] the general case.

**Physics — Cambridge 0625 §1.2, 9702 §2.1.** The same readings in the physics boards' words: *speed–time graphs, deceleration, free fall* (0625 Core), and *graph methods* named outright in 9702 §2.1 (area under $v$–$t$ = displacement; gradients as velocity and acceleration). The physics papers add the qualitative case — a curve of decreasing gradient is a falling body reaching terminal velocity.

**Not examined on…** Cambridge 9231 (assumed from 9709) and AP Calculus (assumed; its motion questions are [[Kinematics Calculus]] outright).

---

## Connections

- **Prerequisite:** [[Gradient (Vocab)]] — gradient is what gives a travel graph its meaning
- **Prerequisite:** [[Linear Graphs (Vocab)]] — straight-line travel graphs are linear graphs in disguise
- **Sibling:** [[Area Under a Graph (Vocab)]] — the §A17 Ext bullet on estimating distance from a curved s-t graph (trapezium rule)
- **Leads to:** [[Kinematics Calculus]] — gradient → derivative; area → integral; the calculus version of this card
- **Application:** *physics* — every motion problem in O-Level / A-Level Physics is a travel graph in disguise; SUVAT equations come from constant-acceleration s-t graphs
- **Application:** *driving exam visualisations* — police stopping-distance and braking charts are s-t graphs annotated with deceleration values

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $s$ | `s` | Displacement / distance from origin |
| $v$ | `v` | Speed (or velocity) |
| $a$ | `a` | Acceleration |
| $\dfrac{\Delta s}{\Delta t}$ | `\dfrac{\Delta s}{\Delta t}` | Gradient on a d-t graph = speed |
| $\dfrac{\Delta v}{\Delta t}$ | `\dfrac{\Delta v}{\Delta t}` | Gradient on an s-t graph = acceleration |
| $\text{m/s}^2$ | `\text{m/s}^2` | Units of acceleration |
