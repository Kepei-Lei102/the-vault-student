---
chinese: 上界与下界 (shàngjiè yǔ xiàjiè)
prerequisites:
  - "[[Rounding (Vocab)]]"
leads_to:
  - "[[Differentiation]]"
  - "[[Error Analysis]]"
  - "[[Error Propagation]]"
  - "[[Accuracy vs Precision]]"
  - "[[Calibration of Instruments]]"
  - "[[Floating-Point Arithmetic]]"
teach_together:
  - "[[Estimation (Vocab)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-N11
  - syllabus/0580-E1-10
  - type/definition
  - type/vocabulary
  - notation/inequality
  - misconception/bounds-are-not-approximations
---

# Upper and Lower Bounds 上界与下界

## Definition

### Formal

When a measurement $x$ is rounded to a given degree of accuracy, there is a range of values that would round to the stated result. The **error interval** is

$$\text{Lower Bound} \leqslant x < \text{Upper Bound}$$

The **lower bound** (LB) is the smallest value that rounds up to the stated value.
The **upper bound** (UB) is the smallest value that would round up to the *next* stated value.

> [!important] Strict inequality at the top
> The upper bound uses $<$, not $\leqslant$. A value exactly equal to the upper bound would round *up* to the next value, not back down to the stated one.

### Intuitive — The Ruler Analogy 直尺类比

Imagine measuring a pencil with a ruler marked in centimetres. You read **7 cm**. That doesn't mean the pencil is *exactly* 7.000… cm. It means the pencil is somewhere between 6.5 cm (the halfway point below 7) and 7.5 cm (the halfway point above 7).

The pencil could be 6.5 cm (that rounds up to 7), or 7.49999… cm (that still rounds down to 7), but it cannot be exactly 7.5 cm (that rounds up to 8, or to 7 — depending on convention, but the exam assumes it rounds **up**).

$$6.5 \leqslant \text{length} < 7.5$$

> [!tip] Why does this matter?
> Every physical measurement is an approximation. When you multiply or divide measurements, the errors combine. Bounds tell you the *worst case* — how far off your answer could be. This is the mathematical foundation of **error analysis** in physics, engineering, and computer science.

### 中文锚点 (Chinese Anchor)

上界与下界：**四舍五入产生误差区间**。

当一个值被四舍五入后，我们只知道它在一个范围内，不知道精确值。

| 中文 | English | Symbol / Example |
|------|---------|-----------------|
| 上界 (shàngjiè) | Upper Bound | UB — the ceiling of the error interval |
| 下界 (xiàjiè) | Lower Bound | LB — the floor of the error interval |
| 误差区间 (wùchā qūjiān) | Error Interval | $\text{LB} \leqslant x < \text{UB}$ |
| 四舍五入 (sìshě wǔrù) | Rounding | "discard 4 and below, keep 5 and above" |
| 有效数字 (yǒuxiào shùzì) | Significant Figures | s.f. |
| 精确度 (jīngquèdù) | Degree of Accuracy | How finely a value is measured |
| 截断 (jiéduàn) | Truncation | Always rounding down (different from rounding!) |

> [!example] 四舍五入 literally means "discard below 5, enter at 5"
> This is *exactly* the rounding rule: digits 0–4 round down, digits 5–9 round up. The Chinese name IS the algorithm. Compare with English where "rounding" gives no hint about the rule.

## Notation

| Symbol | Meaning | Example |
|--------|---------|---------|
| LB | Lower bound | LB = 6.5 |
| UB | Upper bound | UB = 7.5 |
| $\leqslant$ | Less than or equal to | $6.5 \leqslant x$ |
| $<$ | Strictly less than | $x < 7.5$ |
| $x = 7 \pm 0.5$ | Plus-or-minus notation (physics style) | Means $6.5 \leqslant x < 7.5$ |
| d.p. | Decimal places | Rounded to 1 d.p. |
| s.f. | Significant figures | Rounded to 3 s.f. |

> [!note] Plus-or-minus notation
> In physics and engineering, you'll see $x = 7 \pm 0.5$ instead of the error interval. The $\pm$ notation is symmetric and uses $\pm \frac{1}{2} \times \text{unit}$ where "unit" is the place value of the rounding. The two notations carry the same information.

## Visual Summary

![[error-interval-number-line.svg|700]]

## Key Facts

### 1. Finding Bounds from Rounded Values

The **half-unit rule**: go half a unit *below* for the lower bound, half a unit *above* for the upper bound.

| Rounded value | Degree of accuracy | Unit | Half-unit | LB | UB | Error interval |
|---|---|---|---|---|---|---|
| 7 | Nearest integer | 1 | 0.5 | 6.5 | 7.5 | $6.5 \leqslant x < 7.5$ |
| 3.8 | 1 d.p. | 0.1 | 0.05 | 3.75 | 3.85 | $3.75 \leqslant x < 3.85$ |
| 5.63 | 2 d.p. | 0.01 | 0.005 | 5.625 | 5.635 | $5.625 \leqslant x < 5.635$ |
| 400 | Nearest 10 | 10 | 5 | 395 | 405 | $395 \leqslant x < 405$ |
| 2000 | Nearest 100 | 100 | 50 | 1950 | 2050 | $1950 \leqslant x < 2050$ |
| 4.30 | 3 s.f. | 0.01 | 0.005 | 4.295 | 4.305 | $4.295 \leqslant x < 4.305$ |

> [!warning] Significant figures — watch the trailing zeros
> "4.30 to 3 s.f." is NOT the same as "4.3 to 2 s.f." The trailing zero matters — it tells you the degree of accuracy is to the nearest 0.01, not the nearest 0.1.
>
> - $4.30$ to 3 s.f.: unit = 0.01, so $4.295 \leqslant x < 4.305$
> - $4.3$ to 2 s.f.: unit = 0.1, so $4.25 \leqslant x < 4.35$

### 2. Bounds in Calculations — The Combination Rules

When you combine rounded values using arithmetic, the bounds interact. The key principle is: **find the combination that gives the biggest/smallest possible answer**.

| Operation | To get the **largest** result | To get the **smallest** result |
|-----------|------|------|
| $a + b$ | UB($a$) + UB($b$) | LB($a$) + LB($b$) |
| $a - b$ | UB($a$) − LB($b$) | LB($a$) − UB($b$) |
| $a \times b$ | UB($a$) × UB($b$) | LB($a$) × LB($b$) |
| $a \div b$ | UB($a$) ÷ LB($b$) | LB($a$) ÷ UB($b$) |
| $a^2$ | UB($a$)² | LB($a$)² |

> [!tip] WHY does subtraction flip the bound?
> If you're computing $a - b$ and want the **biggest** answer, you want $a$ as big as possible AND $b$ as small as possible — because subtracting a smaller number gives a bigger result. That's why subtraction and division use **opposite** bounds for the two operands.

> [!info] The $a \times b$ rule assumes $a, b > 0$
> If $a$ or $b$ could be negative (rare in IGCSE), the logic reverses. For exam purposes, assume all measurements are positive unless stated otherwise.

### 3. Truncation vs Rounding — A Crucial Distinction

**Rounding** goes to the *nearest* value: half-unit below and above.
**Truncation** always rounds *down*: the stated value IS the lower bound.

| Method | Stated value | LB | UB | Error interval |
|--------|-------------|----|----|----------------|
| Rounded to nearest integer | 7 | 6.5 | 7.5 | $6.5 \leqslant x < 7.5$ |
| Truncated to nearest integer | 7 | 7 | 8 | $7 \leqslant x < 8$ |

> [!example] Computer truncation and the `floor(x + 0.5)` trick
> Most programming languages give you a `floor()` function (round down) but not always a reliable "round to nearest." Since flooring always truncates, how do you round properly?
>
> **The trick:** to round $x$ to the nearest integer, compute `floor(x + 0.5)`.
>
> Why it works: adding 0.5 shifts the boundary. If $x = 3.7$, then $x + 0.5 = 4.2$, and $\lfloor 4.2 \rfloor = 4$ ✓. If $x = 3.2$, then $x + 0.5 = 3.7$, and $\lfloor 3.7 \rfloor = 3$ ✓. The 0.5 shift turns truncation into rounding — the same half-unit idea from bounds, applied in code.
>
> For more on how computers represent numbers with finite precision, accumulated rounding errors, and why $0.1 + 0.2 \neq 0.3$ in most languages, see **[[Floating-Point Arithmetic]]**.

### 4. Degree of Accuracy from Context

Sometimes the exam tells you the degree of accuracy. Sometimes you have to infer it.

| Stated value | Implied accuracy | Reasoning |
|---|---|---|
| 7 cm | Nearest cm (integer) | No decimal places shown |
| 7.0 cm | Nearest mm (1 d.p.) | Trailing zero = measured to 0.1 |
| 7.00 cm | Nearest 0.01 cm (2 d.p.) | Two trailing zeros |
| 400 people | **Exact** | You can't have half a person |
| 400 m | Ambiguous — read the question | Could be nearest 1 m, nearest 10 m, or nearest 100 m |

> [!warning] Discrete vs continuous
> **Counting** (people, cars, coins) gives exact values — no error interval needed.
> **Measuring** (length, mass, time) always produces an approximation — error interval applies.

### 5. Maximum Percentage Error

$$\text{Maximum \% error} = \dfrac{\text{UB} - \text{LB}}{2 \times \text{stated value}} \times 100\% = \dfrac{\text{half-unit}}{\text{stated value}} \times 100\%$$

| Measurement | Half-unit | % error |
|---|---|---|
| 7 cm (nearest cm) | 0.5 | $\dfrac{0.5}{7} \times 100\% \approx 7.1\%$ |
| 70 cm (nearest cm) | 0.5 | $\dfrac{0.5}{70} \times 100\% \approx 0.71\%$ |

**Larger measurements have smaller percentage errors.** This is why scientists use longer rulers, heavier masses, and more precise instruments — the same absolute error becomes a smaller fraction of the measurement.

> [!info] Error propagation — this gets its own card in Physics
> The bounds combination rules above (UB×UB, LB÷UB, etc.) are the *worst-case* method. In physics, you learn a more precise version called **[[Error Analysis|error propagation]]**:
>
> - Addition/subtraction: absolute uncertainties add ($\Delta(a \pm b) = \Delta a + \Delta b$)
> - Multiplication/division: *percentage* uncertainties add ($\dfrac{\Delta(ab)}{ab} = \dfrac{\Delta a}{a} + \dfrac{\Delta b}{b}$)
>
> This is explicitly taught in **Cambridge A-Level Physics 9702** (§1.2), **IB Physics** (Topic 1, formulas on Data Booklet), and **AP Physics 1/2** (lab component). The maths bounds method is the non-calculus precursor — same instinct, simpler rules. The full treatment lives in the [[Error Analysis]] card.

## Common Misconceptions (Teaching Notes)

### 1. "The upper bound uses ≤"

**Wrong:** $6.5 \leqslant x \leqslant 7.5$

**Right:** $6.5 \leqslant x < 7.5$

**Why:** A value of exactly 7.5 rounds UP to 8 (by the "5 rounds up" convention), so 7.5 is NOT a valid value for something that rounded to 7. The lower bound uses $\leqslant$ because 6.5 rounds UP to 7 — it IS a valid value.

### 2. "Both bounds use the same direction for subtraction"

**Wrong:** LB($a - b$) = LB($a$) − LB($b$)

**Right:** LB($a - b$) = LB($a$) − UB($b$)

**Why:** To get the *smallest* difference, you want $a$ as small as possible (use LB) and $b$ as *large* as possible (use UB). Subtracting a bigger number gives a smaller result.

This is the same logic as: "your bank balance is smallest when your income is at its lowest and your spending is at its highest."

### 3. "4.30 and 4.3 have the same bounds"

**Wrong:** Treating trailing zeros as meaningless.

**Right:** 4.30 (3 s.f.) means $4.295 \leqslant x < 4.305$, but 4.3 (2 s.f.) means $4.25 \leqslant x < 4.35$.

**Why:** Writing 4.30 instead of 4.3 communicates that you measured to the nearest 0.01, not the nearest 0.1. The trailing zero carries information about the precision of the measurement.

### 4. "You can round the bounds"

**Wrong:** Stating bounds as $6.5 \leqslant x < 7.5$ then saying "the upper bound is approximately 7."

**Right:** Bounds must be stated as **exact** values. The whole point of bounds is to capture the exact range — rounding the bounds defeats the purpose.

## Worked Examples

### Example 1 — Finding Bounds (9260 N11 Ext, 0580 E1.10)

> A length is measured as $12.4$ cm, correct to 1 decimal place. Write down the error interval.

**Solution:**

The degree of accuracy is 1 d.p., so the unit is $0.1$ and the half-unit is $0.05$.

$$\text{LB} = 12.4 - 0.05 = 12.35$$
$$\text{UB} = 12.4 + 0.05 = 12.45$$

$$\boxed{12.35 \leqslant x < 12.45}$$

### Example 2 — Bounds in Multiplication (9260 N11 Ext, 0580 E1.10)

> A rectangle has length $8.3$ cm and width $5.7$ cm, both correct to 1 decimal place. Calculate the upper and lower bounds of its area.

**Solution:**

First, find bounds for each measurement:
- Length: $8.25 \leqslant l < 8.35$
- Width: $5.65 \leqslant w < 5.75$

For the **largest** area: use UB × UB.
$$\text{UB(area)} = 8.35 \times 5.75 = 48.0125 \text{ cm}^2$$

For the **smallest** area: use LB × LB.
$$\text{LB(area)} = 8.25 \times 5.65 = 46.6125 \text{ cm}^2$$

$$\boxed{46.6125 \leqslant \text{area} < 48.0125}$$

Note: the stated area is $8.3 \times 5.7 = 47.31$ cm². The actual area could be anywhere from $46.61$ to $48.01$ — a spread of about $1.4$ cm². The multiplication magnified the individual errors.

### Example 3 — Bounds in Division (9260 N11 Ext, 0580 E1.10)

> The distance between two towns is $120$ km, correct to the nearest $10$ km. A car travels this distance in $1.5$ hours, correct to the nearest $0.1$ hour. Calculate the upper and lower bounds of the average speed.

**Solution:**

Bounds for distance (nearest 10 km): $115 \leqslant d < 125$
Bounds for time (nearest 0.1 h): $1.45 \leqslant t < 1.55$

Speed $= \dfrac{\text{distance}}{\text{time}}$

**Largest speed:** use UB(distance) ÷ LB(time) — biggest top, smallest bottom.
$$\text{UB(speed)} = \dfrac{125}{1.45} \approx 86.2 \text{ km/h}$$

**Smallest speed:** use LB(distance) ÷ UB(time).
$$\text{LB(speed)} = \dfrac{115}{1.55} = 74.19354... \approx 74.2 \text{ km/h}$$

$$\boxed{74.2 \leqslant \text{speed} < 86.2 \text{ km/h (to 1 d.p.)}}$$

The stated speed is $\dfrac{120}{1.5} = 80$ km/h. But the *actual* speed could be anywhere in a $12$ km/h range — division with rounded values can produce significant uncertainty.

### Example 4 — Bounds with Subtraction (Exam-style)

> Two rods have lengths $15.0$ cm and $9.4$ cm, both correct to 1 decimal place. They are placed end to end. Calculate the lower bound of the difference in their lengths.

**Solution:**

Bounds:
- Rod A: $14.95 \leqslant a < 15.05$
- Rod B: $9.35 \leqslant b < 9.45$

Difference $= a - b$.

For the **lower bound** of a difference: use LB($a$) − UB($b$).

$$\text{LB(difference)} = 14.95 - 9.45 = \boxed{5.50 \text{ cm}}$$

> [!warning] Check: the stated difference is $15.0 - 9.4 = 5.6$ cm, but the actual difference could be as low as $5.50$ cm. Notice how the lower bound of a subtraction can be noticeably less than the stated answer.

## Exam Notes

### OxAQA 9260 (Extension)

**Syllabus ref:** N11 Ext — "Calculate and use upper and lower bounds."

- This is Extension-only content (grades 4–9). Core students don't need bounds.
- Expect 3–5 mark questions asking you to combine bounds in calculations.
- Common contexts: speed/distance/time, area/volume, density.
- The question will usually say "correct to [degree of accuracy]" — read this carefully.
- **Command word:** "Calculate" means show working, not just state the answer. Show both LB and UB calculations explicitly.

### Cambridge 0580 (Extended)

**Syllabus ref:** E1.10 — "Give appropriate upper and lower bounds for data given to a specified accuracy."

- Same content as 9260 N11 Ext. The skill set is identical.
- Often appears in Paper 2 or Paper 4.
- May ask for the error interval using inequality notation: $\text{LB} \leqslant x < \text{UB}$.
- 0580 sometimes asks: "Write down the upper bound" — this is a 1-mark question. Don't overthink it.

### AP / IB / A-Level

At higher levels, bounds connect directly to **[[Error Analysis]]** in physics:

- **Cambridge A-Level Physics 9702** (§1.2) — teaches propagation rules: absolute uncertainties add for $\pm$, percentage uncertainties add for $\times \div$. The bounds combination table above is the IGCSE version of this.
- **IB Physics SL/HL** (Topic 1) — same propagation rules, formulas provided on the Data Booklet. Required for the Internal Assessment.
- **AP Physics 1/2** — propagation taught through lab component, using quadrature (root-sum-of-squares) for tighter bounds.
- **Significant figures** — IB Physics requires stating answers to the correct number of s.f., justified by the precision of the input data.

> [!info] Forward link — [[Floating-Point Arithmetic]]
> Every floating-point number in a computer is stored with finite precision. The **machine epsilon** ($\varepsilon$) is the smallest number such that $1 + \varepsilon \neq 1$ in the computer's arithmetic. For `float64` (the standard), $\varepsilon \approx 2.2 \times 10^{-16}$. This means every computed number has an error interval, just like every physical measurement. The study of how these errors accumulate is called **numerical analysis**.
>
> Catastrophic cancellation occurs when you subtract two nearly-equal numbers: the relative error explodes. For example, computing $\sqrt{x^2 + 1} - x$ for large $x$ loses almost all significant figures. The fix? Rationalise: $\dfrac{1}{\sqrt{x^2+1}+x}$, which is numerically stable. Bounds thinking helps you spot when this matters. Full treatment in the [[Floating-Point Arithmetic]] card.

## Connections

**Prerequisites:**
- [[Rounding (Vocab)|Rounding]] — you need to understand decimal places and significant figures before you can find bounds

**Leads to:**
- [[Estimation (Vocab)|Estimation]] — bounds give you the *exact* worst case; estimation gives you a quick approximate check
- [[Differentiation]] — error propagation ($\Delta f \approx f'(x) \cdot \Delta x$) is the calculus generalisation of bounds
- [[Error Analysis]] — the physics card covering full uncertainty propagation (A-Level 9702, IB, AP)
- [[Floating-Point Arithmetic]] — the CS card covering how computers store and round numbers

**Related concepts:**
- [[Percentages (Vocab)|Percentages]] — maximum percentage error uses percentage calculations
- [[Set]] — an error interval is a set of possible values (interval notation from set theory)
- [[Probability Basics]] — in measurement theory, the true value is modelled as a random variable uniformly distributed over the error interval

## Beyond Syllabus — Measurement Theory

> [!info] Beyond syllabus — How Scientists Actually Handle Uncertainty 科学家如何处理不确定性
>
> At IGCSE, we treat the error interval as a hard box: the true value is *somewhere* inside, and we don't know where. This is called **worst-case analysis**. The full story is in the [[Error Analysis]] card, but here's a preview of the layers:
>
> 1. **Systematic vs random error** (Cambridge IGCSE Physics onward) — A ruler that's 1% too long gives a **systematic error** (always in the same direction). Slightly different readings each time give **random error** (sometimes too high, sometimes too low). Bounds capture random error; systematic errors require calibration.
>
> 2. **Propagation rules** (A-Level / IB / AP Physics) — Instead of the worst-case UB×UB method, physics uses: absolute uncertainties add for $\pm$, percentage uncertainties add for $\times \div$. AP Physics goes further with **quadrature** (root-sum-of-squares), which gives tighter bounds by assuming errors are independent.
>
> 3. **Statistical uncertainty** (university) — Instead of "between 6.5 and 7.5 cm," scientists say "$7.0 \pm 0.3$ cm with 95% confidence." This means there's a 95% probability the true value falls within that range, based on repeated measurements and the normal distribution.
>
> 4. **Heisenberg's uncertainty principle** (university physics) — A fundamental limit: $\Delta x \cdot \Delta p \geqslant \dfrac{\hbar}{2}$. You cannot simultaneously know both the position and momentum of a particle to arbitrary precision. This isn't about instrument quality — it's a law of nature.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\leqslant$ | `\leqslant` | Lower bound inequality |
| $<$ | `<` | Upper bound (strict) |
| $\pm$ | `\pm` | Plus-or-minus |
| $\Delta x$ | `\Delta x` | Error / change in $x$ |
| $\varepsilon$ | `\varepsilon` | Machine epsilon |
| $\dfrac{\partial f}{\partial x}$ | `\dfrac{\partial f}{\partial x}` | Partial derivative |
| $\hbar$ | `\hbar` | Reduced Planck constant |
| $\geqslant$ | `\geqslant` | Greater than or equal to |
