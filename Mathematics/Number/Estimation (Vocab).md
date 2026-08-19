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

**Estimation** is the deliberate use of *approximate* values to predict the size of an answer, typically by rounding each input to **1 significant figure** before computing. The goal is *not* the exact answer — it's a quick check that an exact computation is *plausible*.

The pattern is: **round-then-compute**. Round each number to 1 s.f., do the easy arithmetic in your head, write the estimate.

$$\frac{49.2 \times 7.8}{0.21} \;\approx\; \frac{50 \times 8}{0.2} \;=\; \frac{400}{0.2} \;=\; 2000.$$

(Exact answer: $1827.4...$; the estimate of $2000$ is in the right order of magnitude.)

The **approximation symbol** $\approx$ ("is approximately equal to") replaces $=$ when you're estimating.

### 中文锚点

**估算 (gūsuàn)** = 用近似值估计答案的大小。常见做法：每个数**先取一位有效数字 (yī wèi yǒuxiào shùzì)**，再口算。

| 例 | 估算 |
|---|---|
| $49.2 \times 7.8$ | $\approx 50 \times 8 = 400$ |
| $\dfrac{407}{1.95}$ | $\approx \dfrac{400}{2} = 200$ |
| $\sqrt{83}$ | $\approx \sqrt{81} = 9$ |

约等号 $\approx$ = approximately equal.

---

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

Round each to 1 s.f.: $407 \to 400$, $0.21 \to 0.2$, $1.95 \to 2$.

$$\frac{400 \times 0.2}{2} = \frac{80}{2} = 40.$$

(Exact: $43.84\ldots$; estimate of 40 is excellent.)

### Example 2 — square roots and powers

> Estimate $\sqrt{83}$.

Nearest perfect square: $81 = 9^2$. So $\sqrt{83} \approx 9$. (Exact: $9.11\ldots$; close.)

> [!tip] Estimating roots — use the closest perfect square / cube
> $\sqrt{50} \approx 7$ (since $49 = 7^2$). $\sqrt[3]{30} \approx 3$ (since $27 = 3^3$). Always round the *radicand* to the nearest perfect $n$th-power before the root operation.

---

## Why Estimate? — the sanity-check culture

In Cambridge exams, estimation appears as its own marked task ("estimate $X$"). But the deeper habit is **always know the order of magnitude** of an answer *before* trusting your calculator. Calculators don't catch typing errors; estimation does.

If you compute $\dfrac{407 \times 0.21}{1.95}$ on a calculator and get $440$, the estimate of $40$ should ring an alarm. (You probably forgot the decimal in $0.21$.)

This is the same instinct that catches sign errors, units errors, and "off by a factor of 1000" disasters in physics labs and engineering. Pre-calculator generations of scientists relied on slide rules and mental estimation; the habit hasn't gone away just because computers are fast.

---

## Common Mistakes

1. **Over-rounding.** Rounding $49.2$ to $40$ (or $50$ → $0$) defeats the purpose. Rule: round to *one significant figure*, not "the nearest convenient number."
2. **Round and divide by a *rounded zero*.** Don't round $0.21$ to $0$ in a denominator — you'd be dividing by zero. Round to the nearest 1-s.f. *non-zero* value: $0.2$.
3. **Confusing decimal places with significant figures.** Estimation rounds to s.f., not d.p. — $0.0327 \to 0.03$ (1 s.f., one nonzero digit), not $0.0$ (1 d.p.).
4. **Trusting the estimate as the final answer.** An estimate is a *sanity check*. Compute exactly when an exact answer is asked for; report the estimate when "estimate" is asked.

---

## Exam Notes

### Cambridge 0580 — C1.9 / E1.9 Estimation (Core and Extended alike)

Two learning objectives, identical at both tiers: **(1)** *round values to a specified degree of accuracy* — "includes decimal places and significant figures" — and **(2)** *make estimates for calculations involving numbers, quantities and measurements*, the syllabus's own example being *"by writing each number correct to 1 significant figure, estimate the value of …"*. Standard exam phrasings:

- "By writing each number correct to 1 significant figure, estimate the value of $\dfrac{6.91 \times 38.7}{0.052}$." — round *first*, then compute; the mark is for the rounding shown.
- "Write 5764 correct to the nearest thousand." — the syllabus's own instance of LO 1.
- "Estimate the area of the lake on the map." — a measurement estimate, LO 2.

### OxAQA 9260 — N11 Rounding, estimation and bounds

Core: *round numbers and measures to an appropriate degree of accuracy (e.g. to a specified number of decimal places or significant figures)* and *apply and interpret limits of accuracy*. Extension adds *calculate and use upper and lower bounds* — [[Upper and Lower Bounds]], this card's peer.

### IB

Mathematics: Applications and Interpretation SL 1.6 lists **estimation** explicitly alongside decimal places, significant figures, bounds and percentage error; AA does not name it as a topic.

### Where it is *not* examined

Not a syllabus item at 0606, 9709 or 9231, nor on any AP course — by A-Level the habit is assumed. *Fermi estimation* ("how many piano tuners in Chicago?") is the grown-up version of LO 2 and a genuinely useful thinking skill, but it is enrichment, not a mark on any of these papers.

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
