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
  - curriculum/IB-AI
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

For a positive measurement $x$ rounded to the nearest specified unit, with exact halfway cases rounded upward, there is a range of values that would round to the stated result. The **error interval** is

$$\text{Lower Bound} \leqslant x < \text{Upper Bound}$$

The **lower bound** (LB) is the included lower endpoint of this rounding interval.
The **upper bound** (UB) is the smallest value that would round up to the *next* stated value.

> [!important] Strict inequality at the top
> The upper bound uses $<$, not $\leqslant$. A value exactly equal to the upper bound would round *up* to the next value, not back down to the stated one.

### Intuitive — The Ruler Analogy 直尺类比

Imagine measuring a pencil with a ruler marked in centimetres. You read **7 cm**. That doesn't mean the pencil is *exactly* 7.000… cm. It means the pencil is somewhere between 6.5 cm (the halfway point below 7) and 7.5 cm (the halfway point above 7).

The pencil could be 6.5 cm (that rounds up to 7), or 7.49999… cm (that still rounds down to 7), but it cannot be exactly 7.5 cm (which rounds to 8 under the stated halfway-up convention).

$$6.5 \leqslant \text{length} < 7.5$$

> [!tip] Why does this matter?
> Rounding hides information. When you multiply or divide rounded measurements, the possible values combine. These intervals describe rounding alone; other instrument errors require additional information. Bounds tell you the *worst case* — how far off your answer could be. This is the mathematical foundation of **error analysis** in physics, engineering, and computer science.

### 中文锚点 (Chinese Anchor)

行李秤只显示整公斤，屏幕上写着二十，并不说明箱子恰好重二十公斤。轻一点、重一点的箱子，四舍五入后都可能显示同一个数。显示屏像把一小段重量装进了同一个抽屉：看见“二十”，能找回的是这个抽屉的范围，找不回原来那个精确重量。上界和下界就是抽屉的两边；至于秤本身准不准，那是另外一件要检查的事。

## Notation

| Symbol | Meaning | Example |
|--------|---------|---------|
| LB | Lower bound | LB = 6.5 |
| UB | Upper bound | UB = 7.5 |
| $\leqslant$ | Less than or equal to | $6.5 \leqslant x$ |
| $<$ | Strictly less than | $x < 7.5$ |
| $x = 7 \pm 0.5$ | A centre and a half-width | Does not by itself specify endpoint inclusion or probability |
| d.p. | Decimal places | Rounded to 1 d.p. |
| s.f. | Significant figures | Rounded to 3 s.f. |

> [!note] Plus-or-minus notation needs a meaning
> $7\pm0.5$ gives a centre and a half-width, but does not encode the open upper endpoint. In measurement work it may describe a bound, a standard uncertainty or a coverage interval. State the intended meaning; these are not interchangeable.

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

| Operation | Upper bound | Lower bound |
|-----------|------|------|
| $a + b$ | UB($a$) + UB($b$) | LB($a$) + LB($b$) |
| $a - b$ | UB($a$) − LB($b$) | LB($a$) − UB($b$) |
| $a \times b$ | UB($a$) × UB($b$) | LB($a$) × LB($b$) |
| $a \div b$ | UB($a$) ÷ LB($b$) | LB($a$) ÷ UB($b$) |
| $a^2$ | UB($a$)² | LB($a$)² |

> [!tip] WHY does subtraction flip the bound?
> If you're computing $a - b$ and want the **biggest** answer, you want $a$ as big as possible AND $b$ as small as possible — because subtracting a smaller number gives a bigger result. That's why subtraction and division use **opposite** bounds for the two operands.

> [!info] Check signs, zero and endpoint inclusion
> The product, quotient and square shortcuts in this table assume positive inputs; the quotient needs a denominator bounded away from zero. For a product with arbitrary signs, compare all four endpoint products. A squared interval crossing zero has lower bound 0. A quotient whose denominator can approach zero need not have finite bounds.
>
> A bound can be a limiting value that is never attained. For subtraction or division, check whether the endpoint values needed to reach it are actually included.

### 3. Truncation vs Rounding — A Crucial Distinction

**Rounding** goes to the *nearest* value: half-unit below and above.
**Truncation** discards digits, moving toward zero. For a positive value, the stated truncated value is the lower bound; for a negative value the direction reverses. It is not the same as flooring.

| Method | Stated value | LB | UB | Error interval |
|--------|-------------|----|----|----------------|
| Rounded to nearest integer | 7 | 6.5 | 7.5 | $6.5 \leqslant x < 7.5$ |
| Truncated to an integer | 7 | 7 | 8 | $7 \leqslant x < 8$ |

> [!example] Truncation, floor and halfway choices
> In Python, `math.trunc(-3.7)` is `-3`, while `math.floor(-3.7)` is `-4`. The expression `floor(x + 0.5)` implements nearest-integer rounding with halfway cases toward positive infinity, assuming the addition is exact; it is not a universal replacement for `round()`. Python's built-in `round()` uses ties to even. Different conventions change which interval endpoints are included. [Python documentation](https://docs.python.org/3/library/math.html#math.trunc)

### 4. Degree of Accuracy from Context

Use the stated precision or the instrument/context. Written digits alone do not prove how a number was obtained.

| Stated value | Implied accuracy | Reasoning |
|---|---|---|
| 7 cm | Nearest cm **if stated or established** | Could otherwise be exact or an estimate |
| 7.0 cm | Nearest mm (1 d.p.) | Trailing zero = measured to 0.1 |
| 7.00 cm | Nearest 0.01 cm (2 d.p.) | Two trailing zeros |
| 400 people | Exact if reliably counted; possibly rounded if reported approximately | Discrete quantities can still be estimated |
| 400 m | Ambiguous — read the question | Could be nearest 1 m, nearest 10 m, or nearest 100 m |

> [!warning] Rounding is only one source of uncertainty
> A reliable count can be exact, but crowd estimates are still estimates. A measuring device may have a calibration offset larger than its last displayed digit. A rounding interval is not a complete uncertainty budget.

### 5. Percentage rounding uncertainty

$$\text{Rounding half-width as \% of stated value} = \dfrac{\text{UB} - \text{LB}}{2 \times \text{stated value}} \times 100\% = \dfrac{\text{half-unit}}{\text{stated value}} \times 100\%$$

| Measurement | Half-unit | % error |
|---|---|---|
| 7 cm (nearest cm) | 0.5 | $\dfrac{0.5}{7} \times 100\% \approx 7.1\%$ |
| 70 cm (nearest cm) | 0.5 | $\dfrac{0.5}{70} \times 100\% \approx 0.71\%$ |

**For a fixed absolute half-width, a larger measured value has a smaller percentage uncertainty.** This is why timing several pendulum swings can reduce the fractional effect of a fixed timing uncertainty. The expression above uses the stated value as denominator; an error defined relative to a true/reference value is a different ratio.

> [!info] Bounds and uncertainty propagation
> Exact interval arithmetic gives bounds under stated input limits. [[Error Propagation]] derives first-order uncertainty estimates; products use approximations when relative uncertainties are small. A statistical standard uncertainty, or a root-sum-of-squares combination under independence assumptions, is not a guaranteed worst-case bound.

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

**Right:** Keep **exact** bounds through the calculation. If a final answer needs rounded values, label them as approximations; if it must still enclose every possible value, round the lower endpoint downward and the upper endpoint upward.

## Worked Examples

### Example 1 — Finding Bounds (9260 N11, 0580 C1.10 / E1.10)

> A length is measured as $12.4$ cm, correct to 1 decimal place. Write down the error interval.

**Tool: half the rounding unit. Trigger: “correct to 1 decimal place” specifies the lost interval.**

The degree of accuracy is 1 d.p., so the unit is $0.1$ and the half-unit is $0.05$.

$$\text{LB} = 12.4 - 0.05 = 12.35$$
$$\text{UB} = 12.4 + 0.05 = 12.45$$

$$\boxed{12.35 \leqslant x < 12.45}$$

### Example 2 — Bounds in Multiplication (9260 N11 Ext, 0580 E1.10)

> A rectangle has length $8.3$ cm and width $5.7$ cm, both correct to 1 decimal place. Calculate the upper and lower bounds of its area.

**Tool: monotonicity of a positive product. Trigger: increasing either positive side increases area.**

First, find bounds for each measurement:
- Length: $8.25 \leqslant l < 8.35$
- Width: $5.65 \leqslant w < 5.75$

For the **largest** area: use UB × UB.
$$\text{UB(area)} = 8.35 \times 5.75 = 48.0125 \text{ cm}^2$$

For the **smallest** area: use LB × LB.
$$\text{LB(area)} = 8.25 \times 5.65 = 46.6125 \text{ cm}^2$$

$$\boxed{46.6125 \leqslant \text{area} < 48.0125}$$

Note: the stated area is $8.3 \times 5.7 = 47.31$ cm². The exact interval above has width $1.4$ cm²; its endpoints are approximately $46.61$ and $48.01$ cm², which must not replace the exact interval endpoints. Both input lengths contribute to the area uncertainty.

### Example 3 — Bounds in Division (9260 N11 Ext, 0580 E1.10)

> The distance between two towns is $120$ km, correct to the nearest $10$ km. A car travels this distance in $1.5$ hours, correct to the nearest $0.1$ hour. Calculate the upper and lower bounds of the average speed.

**Tool: numerator up, denominator down. Trigger: positive speed is distance divided by time.**

Bounds for distance (nearest 10 km): $115 \leqslant d < 125$
Bounds for time (nearest 0.1 h): $1.45 \leqslant t < 1.55$

Speed $= \dfrac{\text{distance}}{\text{time}}$

**Largest speed:** use UB(distance) ÷ LB(time) — biggest top, smallest bottom.
$$\text{UB(speed)} = \dfrac{125}{1.45} \approx 86.2 \text{ km/h}$$

**Smallest speed:** use LB(distance) ÷ UB(time).
$$\text{LB(speed)} = \dfrac{115}{1.55} = 74.19354... \approx 74.2 \text{ km/h}$$

$$\boxed{\frac{2300}{31}<\text{speed}<\frac{2500}{29}\quad\mathrm{km/h}.}$$

Both endpoints are excluded: reaching either requires an excluded upper input endpoint. The bounds round to 74.2 and 86.2 km/h, but inserting those rounded numbers into an exact interval would exclude valid speeds. For a conservative interval with one-decimal endpoints, round **outward**: $74.1<\text{speed}<86.3$ km/h.

The stated speed is $\dfrac{120}{1.5} = 80$ km/h. But the *actual* speed could be anywhere in an approximately $12$ km/h range — division with rounded values can produce significant uncertainty.

### Example 4 — Bounds with Subtraction (Exam-style)

> Two rods have lengths $15.0$ cm and $9.4$ cm, both correct to 1 decimal place. Calculate the lower bound of the difference in their lengths.

**Tool: opposite endpoints. Trigger: increasing the subtracted length decreases the difference.**

Bounds:
- Rod A: $14.95 \leqslant a < 15.05$
- Rod B: $9.35 \leqslant b < 9.45$

Difference $= a - b$.

For the **lower bound** of a difference: use LB($a$) − UB($b$).

$$\text{LB(difference)} = 14.95 - 9.45 = \boxed{5.50 \text{ cm}}$$

> [!warning] Check: the stated difference is $15.0 - 9.4 = 5.6$ cm, but the actual difference is strictly greater than $5.50$ cm and can approach it arbitrarily closely. Notice how the lower bound of a subtraction can be noticeably less than the stated answer.

## Exam Notes

### Cambridge 0580 — Core C1.10 and Extended E1.10

**Core** requires upper and lower bounds for a value rounded to a specified accuracy; it explicitly excludes finding bounds on the results of calculations with rounded data. **Extended** includes both individual bounds and bounds of calculations, with area/perimeter and speed given as examples. Distinguish an endpoint from an attainable value, and keep exact bounds until final reporting. The four worked examples are original teaching examples, not quoted past papers.

### OxfordAQA 9260 — N11

Core includes applying and interpreting limits of accuracy. Extension adds calculating and using upper and lower bounds. It is therefore misleading to say Core students have no limits-of-accuracy work. Match the operation and context to the tier; no fixed question frequency or mark allocation is promised.

### IB Mathematics — AI SL 1.6, included at HL

AI explicitly includes bounds of rounded numbers, approximation and percentage errors, including a maximum-percentage-error area example. AA has numerical approximation as prior learning, but does not prescribe this same named bounds unit; do not transfer the AI outcome wholesale to AA.

### Other mathematics courses and the physics bridge

Cambridge 0606/9709/9231, Edexcel IAL Mathematics/Further Mathematics and OxfordAQA 9660 assume earlier numerical skills; there is no separate rounding-interval unit to claim from the title alone. AP Calculus AB/BC error bounds for approximation and AP Statistics confidence intervals are different topics, not this rounding rule.

Cambridge Physics **9702 §1.3** explicitly requires simple addition of absolute or percentage uncertainties. Current IB Physics locates propagation in **Skills in the study of physics → Processing uncertainties**, not the old Topic 1. AP Physics 1, 2 and both C courses assess experimental reasoning; do not claim that quadrature is a prescribed calculation rule across them. See [[Error Propagation]] for the distinct uncertainty models and their course boundaries.

## Connections

**Prerequisites:**
- [[Rounding (Vocab)|Rounding]] — you need to understand decimal places and significant figures before you can find bounds

**Leads to:**
- [[Estimation (Vocab)|Estimation]] — bounds give you the *exact* worst case; estimation gives you a quick approximate check
- [[Differentiation]] — error propagation ($\Delta f \approx f'(x) \cdot \Delta x$) is the calculus generalisation of bounds
- [[Error Propagation]] — first-order propagation and the assumptions behind uncertainty rules
- [[Floating-Point Representation]] — how computers store a finite set of representable values

**Related concepts:**
- [[Percentages (Vocab)|Percentages]] — maximum percentage error uses percentage calculations
- [[Set]] — an error interval is a set of possible values (interval notation from set theory)
- [[Probability Basics]] — a uniform model inside an interval is an additional modelling assumption, not a consequence of rounding

## Beyond Syllabus — What an interval does not tell you

Recall that a rounding interval lists values consistent with a displayed number and a rounding rule. It says nothing by itself about how likely those values are. A uniform distribution inside the interval may be a useful model when supported by the available information, but the rounding operation does not establish it.

Other uncertainty sources can coexist: calibration bias, noise and sampling. A frequentist 95% confidence procedure covers the fixed true parameter in 95% of repeated applications under its assumptions; that is not automatically a 95% probability attached to a particular realised interval. [[Sampling and Estimation]] develops that distinction.

Computer arithmetic adds another boundary. For binary64, machine epsilon is the gap from 1 to the next representable value, $2^{-52}$; it is not the rounding error of every computed result. Exact operations can occur, and spacing varies with magnitude. [[Floating-Point Representation]] supplies the representation; numerical-analysis arguments supply error bounds for a particular computation. [NumPy floating-point limits](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html)

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
