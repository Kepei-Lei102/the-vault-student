---
chinese: 平均速率 (píngjūn sùlǜ)
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

# Average Speed 平均速率

## Definition

The **average speed** over a journey is the *total distance* divided by the *total time*:

$$\boxed{\;\text{average speed} \;=\; \frac{\text{total distance}}{\text{total time}}.\;}$$

Crucially: the average speed is **not generally** the arithmetic mean of the individual speeds along the way. This is the most common mistake on this topic, and the trap has a name — the **harmonic-mean trap**.

### 中文锚点

**平均速率**是总路程除以总时间。骑车去同一家店，去时快、回来慢，慢的那一段用时更长，不能把两个速率直接相加再除以二。途中停下来买水，路程没有增加，时间却继续累计，所以全程平均速率会降低。这里说的是走了多远；**平均速度**还要看位移，回到出发点时位移为零，平均速度也为零，但平均速率可以大于零。

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
> For positive speeds, the harmonic mean is no greater than the arithmetic mean, with equality only when the two values are identical. This is a special case of the AM-GM-HM inequality. So whenever a journey has *equal-distance* legs at different speeds, the average speed is *strictly less* than the simple average of the speeds.

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

(Note: the simple mean $\dfrac{60 + 80}{2} = 70$ km/h *happens to match* here — only because the times happened to be equal. This is the equal-time rule, not a general rule for averaging speeds.)

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
4. **Confusing average speed with average velocity.** The time average of speed, $\frac{1}{T}\int_0^T |v(t)|\,dt$, **is** total distance divided by total time, including for continuously varying motion. Average velocity uses displacement instead. An unweighted mean of speed readings is a different calculation unless the sampling gives each reading equal time weight.

---

## Exam Notes

### Cambridge 0580 and OxfordAQA 9260

**0580 C1.12 / E1.12** explicitly require average-speed problems and knowledge of the speed–distance–time formula. This is Core as well as Extended. The syllabus's example is 45 km in 3 hours 45 minutes: convert to 3.75 hours before dividing, giving 12 km/h. For a multi-stage journey, total the distances and elapsed times; include a stop when the stated interval includes it.

**9260 G14 Core** covers standard and compound units, including speed. Its unit-conversion requirements apply to these calculations; the harmonic-mean formula is a derived shortcut here, not a separate formula claimed for memorisation.

### Cambridge 0606, 9709 and 9231

**0606 §14.14–14.15** extend motion to differentiation, integration and motion graphs; **9709 §4.2** likewise distinguishes distance/speed from displacement/velocity and requires calculus for straight-line motion, restricted to Paper 1 techniques. Compute total distance by splitting at reversals or integrating speed, then divide by the interval length. **9231** assumes earlier mechanics and extends it, notably variable-force motion in §3.5; this elementary ratio is background rather than a new Further Mathematics technique.

### Edexcel IAL and OxfordAQA 9660

**Edexcel IAL M1 §3.1** includes straight-line motion and motion graphs; total journey distance and time supply the average. **OxfordAQA 9660 M1.1 explicitly names average speed**, with calculus motion following in M1.2. Do not substitute displacement for distance on a return journey.

### AP and IB connections

**AP Calculus AB/BC Topics 8.1–8.2** connect average values and particle motion: the average value of speed is $\frac{1}{T}\int_0^T |v(t)|\,dt$. This is exactly the same distance-over-time quantity, not a competing definition. AP Physics 1 and Physics C: Mechanics use the distance/displacement and speed/velocity distinction in kinematics.

**IB Physics A.1** likewise distinguishes these quantities. For the IB mathematics calculus treatment of motion, see [[Kinematics Calculus]]; no separate harmonic-mean learning outcome is claimed here.

### Where it is not a new topic

The harmonic-mean shortcut is a consequence of equal distances, not a replacement for total distance divided by total time. Calculus is **not** part of the 0580 treatment. Advanced algebra or statistics courses do not acquire a motion requirement merely because “mean” appears in the title.

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
| $\bar{v} = \dfrac{\text{total } d}{\text{total } t}$ | `\bar{v}` | average speed (state that this is speed, not velocity) |
| $\dfrac{2}{1/v_1 + 1/v_2}$ | `\dfrac{2}{1/v_1 + 1/v_2}` | harmonic mean of two speeds |
