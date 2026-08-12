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

The "/" is read "**per**". A speed of $60$ km/h means *for every hour, you travel 60 km* — but you don't have to travel *for* an hour to have that speed; the rate captures the instantaneous proportion.

### 中文锚点

**率 (lǜ)** = 两个不同量的比，常带**复合单位 (fùhé dānwèi)**。

| 量 | 单位 | 中文 |
|---|---|---|
| 速率 (sùlǜ) | km/h, m/s | speed |
| 密度 (mìdù) | g/cm³ | density |
| 压强 (yāqiáng) | N/m² (帕 Pa) | pressure |
| 汇率 (huìlǜ) | USD/CNY | exchange rate |

"/" 读作 **"每"** (měi) 或 "per"。$60$ km/h 即"每小时 $60$ 公里"。

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

Example: a car travels $240$ km in $3$ hours. Speed = $\dfrac{240}{3} = 80$ km/h.

The rearrangements: $d = vt$, $t = d/v$. (See [[Average Speed (Vocab)]] for the harmonic-mean trap when speed varies.)

### 2. Density = mass / volume

$$\rho = \frac{m}{V}.$$

Example: a metal block has mass $216$ g and volume $24$ cm³. Density = $\dfrac{216}{24} = 9$ g/cm³ (consistent with copper).

### 3. Pressure = force / area

$$P = \frac{F}{A}.$$

Example: a $600$ N person stands on snowshoes covering $0.4$ m². Pressure = $\dfrac{600}{0.4} = 1500$ N/m² ($= 1500$ Pa). Without snowshoes (foot area $\approx 0.04$ m²), pressure spikes to $15{,}000$ Pa — and you sink. Snowshoes are an applied-pressure problem.

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

If \$1 = ¥7.20 (USD to RMB rate), then:

- Converting USD → RMB: multiply by 7.20. ($50 USD × 7.20 = ¥360.)
- Converting RMB → USD: divide by 7.20. (¥720 ÷ 7.20 = $100.)

The rate is a *factor*; same trick as any unit conversion. Banks usually quote a *spread* (different buy and sell rates) — the difference is their margin.

---

## Common Mistakes

1. **Forgetting compound units.** A speed of $20$ — but $20$ what? km/h, m/s, mph? Without the unit the number is meaningless.
2. **Unit conversion errors.** $60$ km/h is *not* the same as $60$ m/s. Conversion: $1$ km/h = $\dfrac{1000 \text{ m}}{3600 \text{ s}} = \dfrac{1}{3.6}$ m/s. So $60$ km/h $\approx 16.67$ m/s. Always ensure speed and distance/time use matching units.
3. **Reciprocal direction confusion.** Best buy "lowest \$/unit" or "highest unit/\$" — they agree, but make sure you compare in *one consistent* direction.
4. **Mixing rates inappropriately.** Average density of a mixed object isn't always the simple mean of densities (think of an ice cube in water — different densities give different volume-vs-mass profiles).

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** N19 — solve problems involving rates: speed, density, pressure; comparison of "best buy" type problems. Standard patterns:

- "A train travels $360$ km in $4$ hours. Calculate its average speed in km/h."
- "Box A: $500$ g for \$2.40. Box B: $1.2$ kg for \$5.50. Which is the better buy? Show your working."
- "An object of mass $48$ g has volume $20$ cm³. Calculate its density."

> [!tip] Always show the rate calculation explicitly
> Write the rate as a fraction with units, do the division, write the answer with units. The markscheme awards: 1 mark for the correct fraction, 1 for the arithmetic, 1 for the unit. Skipping units costs the unit mark even when the number is right.

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
