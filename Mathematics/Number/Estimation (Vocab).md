---
chinese: 估算 (gūsuàn)
prerequisites:
  - "[[Rounding (Vocab)]]"
  - "[[Standard Form (Vocab)]]"
leads_to: []
teach_together:
  - "[[Upper and Lower Bounds]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E1-9
  - syllabus/9260-N11
  - type/vocabulary
  - notation/approx
---

# Estimation 估算

## Definition

**Estimation** is the deliberate use of *approximate* values to predict the size of an answer, often by replacing awkward inputs with nearby convenient numbers before computing. The goal is *not* the exact answer — it's a quick check that an exact computation is *plausible*.

The pattern is: **simplify-then-compute**. If a question specifies 1 significant figure, use it; otherwise choose approximations that make the arithmetic easy while preserving the relevant scale.

$$\frac{49.2 \times 7.8}{0.21} \;\approx\; \frac{50 \times 8}{0.2} \;=\; \frac{400}{0.2} \;=\; 2000.$$

(Exact answer: $1827.4...$; the estimate of $2000$ is in the right order of magnitude.)

The **approximation symbol** $\approx$ ("is approximately equal to") replaces $=$ when you're estimating.

### 中文锚点

四杯饮料，每杯十九块八。还没走到收银台，你就能想：一杯算二十，四杯大约八十。要是屏幕跳出八百，你不必先算出准确的七十九块二，也知道哪里出了问题。估算就是先抓住这个“应该差不多有多大”：把难算的数换成附近好算的数，让脑子里先有个底，算得快，还能给计算器的结果把把关。

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| estimate | 估算 / 估计 | a deliberate approximation |
| approximate | 近似 | "approximately"; symbol $\approx$ |
| order of magnitude | 数量级 (shùliàngjí) | the *power of 10* an answer sits at; e.g. $1{,}500$ has order of magnitude $10^3$ |
| sanity check | 合理性检验 | does the exact answer's size match my estimate? |
| 1 significant figure | 一位有效数字 | round to leftmost nonzero digit (e.g. $0.0327 \to 0.03$) |

---

## Worked Examples

### Example 1 — straightforward estimation

> Estimate $\dfrac{407 \times 0.21}{1.95}$.

**Tool: round then compute. Trigger: the inputs lie near simple one-significant-figure values.** Round each to 1 s.f.: $407 \to 400$, $0.21 \to 0.2$, $1.95 \to 2$.

$$\frac{400 \times 0.2}{2} = \frac{80}{2} = 40.$$

(Exact: $43.83\ldots$; estimate of 40 is excellent.)

### Example 2 — square roots and powers

> Estimate $\sqrt{83}$.

**Tool: a nearby perfect square. Trigger: 83 is close to $9^2$.** Nearest perfect square: $81 = 9^2$. So $\sqrt{83} \approx 9$. (Exact: $9.11\ldots$; close.)

> [!tip] Estimating roots — use the closest perfect square / cube
> $\sqrt{50} \approx 7$ (since $49 = 7^2$). $\sqrt[3]{30} \approx 3$ (since $27 = 3^3$). A nearby perfect power is a useful first estimate; refine it if the purpose requires greater accuracy.

---

## Why Estimate? — the sanity-check culture

A useful habit is to **estimate the size** of an answer *before* trusting your calculator. Calculators don't catch typing errors; estimation does.

If you compute $\dfrac{407 \times 0.21}{1.95}$ on a calculator and get $440$, the estimate of $40$ should ring an alarm. (A typing or scaling error is worth checking.)

This is the same instinct that catches sign errors, units errors, and "off by a factor of 1000" disasters in physics labs and engineering. Pre-calculator generations of scientists relied on slide rules and mental estimation; the habit hasn't gone away just because computers are fast.

---

## Common Mistakes

1. **Ignoring the requested approximation.** To 1 s.f., $49.2$ becomes $50$, not $40$. When no rounding rule is specified, convenient nearby values can be appropriate; the estimate still needs to preserve the scale.
2. **Round and divide by a *rounded zero*.** Don't round $0.21$ to $0$ in a denominator — you'd be dividing by zero. Round to the nearest 1-s.f. *non-zero* value: $0.2$.
3. **Confusing decimal places with significant figures.** When 1 s.f. is requested, $0.0327 \to 0.03$ (1 s.f., one nonzero digit), not $0.0$ (1 d.p.).
4. **Trusting the estimate as the final answer.** An estimate is a *sanity check*. Compute exactly when an exact answer is asked for; report the estimate when "estimate" is asked.

---

## Exam Notes

### Cambridge 0580 — C1.9 / E1.9 Estimation (Core and Extended alike)

Three learning objectives, shared by both tiers: **(1)** *round values to a specified degree of accuracy* — "includes decimal places and significant figures" — and **(2)** *make estimates for calculations involving numbers, quantities and measurements*, the syllabus's own example being *"by writing each number correct to 1 significant figure, estimate the value of …"*. **(3)** round answers appropriately for the context. Illustrative practice phrasings:

- "By writing each number correct to 1 significant figure, estimate the value of $\dfrac{6.91 \times 38.7}{0.052}$." — round *first*, then compute; show the approximation before computing.
- "Write 5764 correct to the nearest thousand." — the syllabus's own instance of LO 1.
- "Estimate the area of the lake on the map." — a measurement estimate, LO 2.

### OxAQA 9260 — N11 Rounding, estimation and bounds

Core: *round numbers and measures to an appropriate degree of accuracy (e.g. to a specified number of decimal places or significant figures)* and *apply and interpret limits of accuracy*. Extension adds *calculate and use upper and lower bounds* — [[Upper and Lower Bounds]].

### IB

Mathematics: Applications and Interpretation SL 1.6 lists **estimation** explicitly alongside decimal places, significant figures, bounds and percentage error; AA does not name it as a topic.

### Where it is *not* examined

Not a syllabus item at 0606, 9709 or 9231, nor as a separate topic in AP Calculus AB/BC or AP Statistics — by A-Level the habit is assumed. *Fermi estimation* ("how many piano tuners in Chicago?") is the grown-up version of LO 2 and a genuinely useful thinking skill, but it is enrichment, not a mark on any of these papers.

---

## Connections

- **Prerequisite:** [[Rounding (Vocab)]] — the rounding rules underlying every estimation step
- **Sibling:** [[Upper and Lower Bounds]] — the *rigorous* version of "approximate"; bounds give intervals, estimates give one number
- **Application:** *physics labs* — order-of-magnitude estimates verify experimental results
- **Application:** *engineering* — slide-rule arithmetic and "back-of-the-envelope" calculations are estimation in disguise

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\approx$ | `\approx` | approximately equal |
| $\sim$ | `\sim` | "of the same order"; informal |
