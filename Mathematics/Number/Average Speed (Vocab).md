---
chinese: 平均速度 (píngjūn sùdù)
prerequisites:
  - "[[Rates (Vocab)]]"
  - "[[Fractions (Vocab)]]"
  - "[[Time Calculations (Vocab)]]"
leads_to:
  - "[[Travel Graphs (Vocab)]]"
  - "[[Kinematics Calculus]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E1-12
  - type/vocabulary
  - misconception/mean-of-speeds
---

# Average Speed 平均速度

## Definition

The **average speed** over a journey is the *total distance* divided by the *total time*:

$$\boxed{\;\text{average speed} \;=\; \frac{\text{total distance}}{\text{total time}}.\;}$$

Crucially: the average speed is **not** the arithmetic mean of the individual speeds along the way. This is the most common mistake on this topic, and the trap has a name — the **harmonic-mean trap**.

### 中文锚点

**平均速度 (píngjūn sùdù)** = **总路程** (zǒng lùchéng) ÷ **总时间** (zǒng shíjiān)。

公式：

$$\text{平均速度} = \frac{\text{总距离}}{\text{总时间}}.$$

**最常见的错误**：平均速度 ≠ 各段速度的算术平均 (suànshù píngjūn)。这是 0580 的经典陷阱。

---

## The Harmonic-Mean Trap

### Worked Example — the trap in action

> A car travels from A to B at $60$ km/h, then back from B to A at $40$ km/h. What is the average speed for the whole round trip?

**Wrong instinct.** $\dfrac{60 + 40}{2} = 50$ km/h. ❌ This is the *arithmetic mean* of the speeds, but the question asks for the *speed of the round trip as a whole*.

**Right method.** Use total distance / total time.

Let the one-way distance be $d$ km. Then:
- Outward time: $\dfrac{d}{60}$ hours.
- Return time: $\dfrac{d}{40}$ hours.
- Total distance: $2d$ km.
- Total time: $\dfrac{d}{60} + \dfrac{d}{40} = \dfrac{2d + 3d}{120} = \dfrac{5d}{120} = \dfrac{d}{24}$ hours.

Average speed: $\dfrac{2d}{d/24} = 2d \times \dfrac{24}{d} = 48$ km/h.

**Answer:** $\boxed{48 \text{ km/h}}$ — *not* $50$.

> [!info] Why the average is *less* than the arithmetic mean
> The car spends *more time* at the slower speed (return leg takes $d/40$ vs outward leg's $d/60$). More time at the slower value drags the average down. The correct average is the **harmonic mean** of the two speeds:
>
> $$\text{harmonic mean} = \frac{2}{\frac{1}{60} + \frac{1}{40}} = \frac{2 \cdot 60 \cdot 40}{60 + 40} = \frac{4800}{100} = 48 \text{ km/h.}$$
>
> The harmonic mean is *always* less than the arithmetic mean (with equality only when the two values are identical). This is a special case of the AM-GM-HM inequality. So whenever a journey has *equal-distance* legs at different speeds, the average speed is *strictly less* than the simple average of the speeds.

### Why "equal distance" matters

The harmonic mean shows up because the two legs have *equal distance, unequal time*. If instead they had **equal time** at different speeds (say, 1 hour at 60 km/h and 1 hour at 40 km/h), then:

- Total distance: $60 + 40 = 100$ km.
- Total time: $2$ h.
- Average speed: $50$ km/h. ✓

**Equal time → arithmetic mean works.** **Equal distance → harmonic mean is correct.** Read the question carefully to know which case you're in.

---

## Worked Examples

### Example 1 — straightforward

> A cyclist rides $30$ km in $2$ hours. What is the average speed?

$$\text{avg speed} = \frac{30}{2} = 15 \text{ km/h.}$$

### Example 2 — multi-segment journey

> A train travels $90$ km at $60$ km/h, then $120$ km at $80$ km/h. Find the average speed for the whole journey.

- First leg: time = $\dfrac{90}{60} = 1.5$ h.
- Second leg: time = $\dfrac{120}{80} = 1.5$ h.
- Total distance: $90 + 120 = 210$ km.
- Total time: $1.5 + 1.5 = 3$ h.
- Average speed: $\dfrac{210}{3} = 70$ km/h.

(Note: the simple mean $\dfrac{60 + 80}{2} = 70$ km/h *happens to match* here — only because the times happened to be equal. Coincidence, not pattern.)

### Example 3 — including a stop

> A car drives $40$ km in $30$ min, stops for $10$ min, then drives another $20$ km in $20$ min. Find the average speed for the whole journey (including the stop).

- Total distance: $40 + 20 = 60$ km.
- Total time: $30 + 10 + 20 = 60$ min $= 1$ h.
- Average speed: $\dfrac{60}{1} = 60$ km/h.

The stop counts in the total time. (If the question said "average *moving* speed," exclude the stop and use $50$ min $= 5/6$ h, giving $72$ km/h.)

> [!warning] Read whether to include rest periods
> "Average speed for the whole journey" includes stops. "Average speed while moving" doesn't. Cambridge problems usually mean the former — but the wording matters.

---

## Common Mistakes

1. **Averaging the speeds.** $\dfrac{60 + 40}{2} = 50$ for a round trip is wrong (correct: 48). Use total-distance / total-time.
2. **Forgetting to include stops in total time.** A stop adds to time but not distance — drops the average.
3. **Unit mismatch.** Distance in km, time in minutes — convert one before dividing. ($90$ km in $30$ min → $90 / 0.5 = 180$ km/h, *not* $90 / 30$.)
4. **Confusing average speed with mean speed.** They're typically different terms in physics: *average speed* = total distance / total time; *mean speed* over an interval (in calculus) = $\dfrac{1}{T}\int_0^T |v(t)|\,dt$. At 0580 they're equivalent if $v$ is piecewise constant.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E1.12 (Rates) — solve problems involving average speed. Standard patterns:

- "A train travels at $90$ km/h for $40$ minutes, then at $120$ km/h for $1$ hour. Find the average speed for the whole journey."
- "A car travels from town A to town B at $50$ km/h and returns at $70$ km/h. Find the average speed for the round trip." (Harmonic-mean case.)
- "Convert $25$ m/s to km/h." (Unit-conversion stretch — multiply by $3.6$.)

### A-Level / IB / AP

A-Level extends to:

- **Time-varying speeds** via calculus: average speed = $\dfrac{1}{T}\int_0^T |v(t)|\,dt$. See [[Kinematics Calculus]].
- **Average velocity vs average speed** — average *velocity* is $\dfrac{\text{displacement}}{\text{time}}$, can be zero for a round trip; average *speed* is total distance / time, never less than $\lvert$average velocity$\rvert$.

---

## Connections

- **Prerequisite:** [[Rates (Vocab)]] — speed is the prototype rate
- **Sibling:** [[Travel Graphs (Vocab)]] — average speed = gradient of the chord on a distance-time graph (vs instantaneous = tangent)
- **Forward:** [[Kinematics Calculus]] — calculus formalises average vs instantaneous via integrals
- **Beyond syllabus:** *AM-GM-HM inequality* — harmonic mean ≤ geometric mean ≤ arithmetic mean, with equality only when all values agree

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $v = \dfrac{d}{t}$ | `v = \dfrac{d}{t}` | basic speed |
| $\bar{v} = \dfrac{\text{total } d}{\text{total } t}$ | average speed |
| $\dfrac{2}{1/v_1 + 1/v_2}$ | `\dfrac{2}{1/v_1 + 1/v_2}` | harmonic mean of two speeds |
