---
chinese: 变化率 (biànhuàlǜ) / 率
prerequisites:
  - "[[Proportion (Vocab)]]"
  - "[[Ratio (Vocab)]]"
leads_to:
  - "[[Average Speed (Vocab)]]"
  - "[[Connected Rates of Change]]"
  - "[[Units of Measure (Vocab)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/Cambridge-0580
  - curriculum/OxAQA-9260
  - syllabus/0580-E1-12
  - syllabus/9260-N19
  - type/vocabulary
  - notation/compound-units
---

# Rates 率

## Definition

A **rate** is a ratio of two *different* quantities, usually expressed as "*A* per *B*" with **compound units**:

| Quantity | Compound unit | Symbol |
|---|---|---|
| Speed | distance per time | km/h, m/s |
| Density | mass per volume | g/cm³, kg/m³ |
| Pressure | force per area | N/m² (= Pa, pascal) |
| Exchange rate | currency per currency | USD/GBP, RMB/USD |
| Population density | people per area | persons/km² |
| Wage rate | money per time | \$/hour |

The "/" is read "**per**". A **constant** speed of $60$ km/h covers 60 km in one hour, or 15 km in a quarter-hour. An **average** speed of 60 km/h means total distance divided by total time is 60 km/h; the speed can vary during the journey. A speedometer reading describes the speed at that instant, not a promise about the next hour.

### 中文锚点

买米时，一袋500克卖12元，另一袋900克卖18元。只看价签，第一袋便宜；可你买到的米也少。把它们都换成“每100克多少钱”，就是2.4元和2元，第二袋反而更划算。“每”字做的事，就是先把比较的分量统一，让你看清同样一份东西究竟要花多少钱。

---

## Key Vocabulary

| English | 中文 | Compound unit |
|---------|------|---------------|
| speed | 速度 / 速率 | km/h, m/s |
| velocity | 速度 (with direction) | m/s (signed) |
| density | 密度 | $\rho = \dfrac{m}{V}$ |
| pressure | 压强 | $P = \dfrac{F}{A}$ |
| exchange rate | 汇率 | money per money |
| best buy | 最划算 | which has the lowest *cost rate* (\$/unit) |

---

## Three Standard Rate Calculations

### 1. Speed = distance / time

$$v = \frac{d}{t}.$$

**Trigger: total journey distance and time → tool: average speed = total distance / total time.** A car travels $240$ km in $3$ hours. Average speed = $\dfrac{240}{3} = 80$ km/h.

The rearrangements: $d = vt$, $t = d/v$. (See [[Average Speed (Vocab)]] for the harmonic-mean trap when speed varies.)

### 2. Density = mass / volume

$$\rho = \frac{m}{V}.$$

**Trigger: mass per volume → tool: density = mass / volume.** A metal block has mass $216$ g and volume $24$ cm³. Density = $\dfrac{216}{24} = 9$ g/cm³ (consistent with copper).

### 3. Pressure = force / area

$$P = \frac{F}{A}.$$

**Trigger: the same force spread over different areas → tool: pressure = force / area.** A $600$ N person stands on snowshoes covering $0.4$ m². Pressure = $\dfrac{600}{0.4} = 1500$ N/m² ($= 1500$ Pa). Without snowshoes (foot area $\approx 0.04$ m²), pressure spikes to $15{,}000$ Pa — and you sink. Snowshoes are an applied-pressure problem.

> [!tip] The "rate triangle" memory aid
> For any rate $R = \dfrac{A}{B}$, the relationship $A = R \times B$, $B = A / R$ comes from the triangle:
>
> ```
>      A
>     ─────
>     R | B
> ```
>
> Cover the unknown; what's left is the formula. Cover $A$ → $R \times B$. Cover $B$ → $A / R$. Cover $R$ → $A / B$. The same triangle works for $d = vt$, $m = \rho V$, $F = PA$.

---

## Best-Buy Comparisons

The classic rate-comparison problem: "Which is the best buy — $500$ g for £2.40 or $750$ g for £3.40?"

**Trigger: unequal pack sizes hide the price comparison → tool: compare one common quantity.** Assume the products have the same quality and both quantities are useful to you.

**Method 1 — cost per unit (rate).**
- $\dfrac{2.40}{500} = 0.0048$ £/g.
- $\dfrac{3.40}{750} = 0.00453$ £/g.

The second is cheaper per gram → **second is the better buy**.

**Method 2 — units per pound.**
- $\dfrac{500}{2.40} = 208$ g/£.
- $\dfrac{750}{3.40} = 220$ g/£.

The second gives more grams per pound → second is better. Same answer, different rate direction.

> [!tip] Pick the rate that's natural for the comparison
> "Best buy" works either way. **Cost per unit** is most common in supermarkets (lower is better). **Units per cost** (grams per pound) is what bargain-hunters intuitively want (higher is better). Either rate gives the same conclusion; pick the one with the cleaner arithmetic.

---

## Exchange Rates

If \$1 = ¥7.20 (an illustrative USD to RMB rate, not a current quote), then:

**Trigger: the wanted currency must remain after units cancel → tool: multiply by the conversion factor in the appropriate direction.**

- Converting USD → RMB: multiply by 7.20. (US\$50 × 7.20 = ¥360.)
- Converting RMB → USD: divide by 7.20. (¥720 ÷ 7.20 = US\$100.)

The rate is a *factor*; same trick as any unit conversion. Banks usually quote a *spread* (different buy and sell rates) — the difference is their margin.

---

## Common Mistakes

1. **Forgetting compound units.** A speed of $20$ — but $20$ what? km/h, m/s, mph? Without the unit the number is meaningless.
2. **Unit conversion errors.** $60$ km/h is *not* the same as $60$ m/s. Conversion: $1$ km/h = $\dfrac{1000 \text{ m}}{3600 \text{ s}} = \dfrac{1}{3.6}$ m/s. So $60$ km/h $\approx 16.67$ m/s. Always ensure speed and distance/time use matching units.
3. **Reciprocal direction confusion.** Best buy "lowest \$/unit" or "highest unit/\$" — they agree, but make sure you compare in *one consistent* direction.
4. **Mixing rates inappropriately.** Average density of a mixed object isn't always the simple mean of densities (think of an ice cube in water — different densities give different volume-vs-mass profiles).

---

## Exam Notes

### Cambridge 0580 Core and Extended — 2025–27

**C1.12 / E1.12, Rates:** use rates of pay, currency exchange, flow and fuel consumption; apply other rates such as pressure, density and population density; calculate average speed. The syllabus supplies required formulas for those **other measures of rate**, but expects students to know the speed–distance–time relationship. Best-value comparisons also sit under **C1.11 / E1.11, Ratio and proportion**. “N19” belongs to OxfordAQA, not Cambridge.

Representative applications (constructed examples):

- **Pay:** £12 per hour for 3.5 hours gives £42. *Trigger: rate and duration → tool: multiply; hours cancel.*
- **Flow:** 18 litres in 3 minutes gives 6 L/min. *Trigger: volume per minute → tool: divide volume by elapsed time.*
- **Fuel:** 24 litres over 360 km gives $24/360\times100\approx6.67$ L/100 km. *Trigger: the unit says per 100 km → tool: scale to that common distance.* A lower L/100 km is better fuel economy; a higher km/L is better. Keep the rate direction fixed when comparing.

Show the setup, consistent units and final answer. **Mark allocations depend on the question and its mark scheme**; there is no universal “fraction + arithmetic + unit = three marks” rule.

### OxfordAQA 9260 — Core content within both tiers

**N19** explicitly includes common rates, pay and best-buy problems. **G14** also requires conversions involving standard and compound units, with speed and density as examples. The calculations above support rate interpretation; [[Units of Measure (Vocab)]] develops unit conversions.

### Cambridge 0606 and A-Level mathematics

For **0606**, this is supporting IGCSE arithmetic and compound-unit fluency, not a separately listed elementary-rates topic. **9709**, **9231**, **Edexcel IAL** and **OxfordAQA 9660** also use these skills within further work. In particular, average speed belongs in mechanics and derivatives describe instantaneous rates: dividing two totals is not a substitute for differentiation. [[Average Speed (Vocab)]], [[Differentiation]] and [[Connected Rates of Change]] develop those distinctions.

### IB Mathematics AA / AI — first-assessment-2021 guides

Both guides explicitly list ratio/proportion, SI and derived units, and speed = distance/time under **prior learning** (AA pp. 26–27; AI pp. 24–25). These are usable knowledge, not material to discard as “not examined”. Topic 5 goes on to derivatives and rates of change; those calculus outcomes require more than elementary rate arithmetic. [AA guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf), [AI guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-applications-and-interpretation-guide-en.pdf).

### AP Calculus AB / BC

The CED includes average and instantaneous rates, applied rate interpretation and related rates, especially **Unit 4**. Elementary compound-unit arithmetic supports that work; the calculus requirements are developed in [[Differentiation]] and [[Connected Rates of Change]]. Neither course has a separate supermarket best-buy unit. This is a scope distinction, not a claim that rate reasoning is absent from AP.

**Where this elementary treatment is not a separate named topic:** the higher courses above do not list the IGCSE package of pay, shopping and density as a standalone unit. Their prerequisite arithmetic and their assessed calculus/mechanics applications still matter. No extra higher-course syllabus tags are inferred from the word “rate”.

---

## Connections

- **Prerequisite:** [[Proportion (Vocab)]] — rates are proportions ("for every 1 hour, 60 km")
- **Sibling:** [[Average Speed (Vocab)]] — the *time-varying speed* case where naive averaging fails (harmonic-mean trap)
- **Forward:** [[Travel Graphs (Vocab)]] — speed as gradient of distance-time graph
- **Forward:** [[Connected Rates of Change]] — calculus version: $\dfrac{dV}{dt} = \dfrac{dV}{dr}\cdot\dfrac{dr}{dt}$
- **Application:** *physics* — every physical quantity with a "per" is a rate; pressure, density, current, frequency, all of it

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $v = \dfrac{d}{t}$ | `v = \dfrac{d}{t}` | speed formula |
| $\rho = \dfrac{m}{V}$ | `\rho = \dfrac{m}{V}` | density (use `\rho`) |
| $P = \dfrac{F}{A}$ | `P = \dfrac{F}{A}` | pressure |
| km/h, m/s | `\text{km/h}` | use `\text{}` for unit text |
