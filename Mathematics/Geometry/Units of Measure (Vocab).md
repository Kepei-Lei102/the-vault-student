---
chinese: 度量单位 (dùliàng dānwèi)
prerequisites:
  - "[[Rates (Vocab)]]"
leads_to:
  - "[[Area and Perimeter (Vocab)]]"
  - "[[Surface Area and Volume (Vocab)]]"
  - "[[Physical Quantities and Units]]"
tags:
  - subject/mathematics
  - domain/geometry
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/0580-E5-1
  - syllabus/9260-G14
  - type/vocabulary
  - notation/SI-units
---

# Units of Measure 度量单位

## Definition

A **unit of measure** is a standard quantity used to express measurements (length, mass, time, area, volume, etc.). The **SI (Système International)** is the global standard; the named conversion content in Cambridge 0580 is metric. Imperial units below are useful context, not a separate UK version of the syllabus.

The big mathematical fact: when you change units, you *multiply by a conversion factor*, not by an arbitrary number. Length conversion factors are exact powers of $10$ in metric; area scales by the *square* of length; volume by the *cube*.

### 中文锚点

**度量单位 (dùliàng dānwèi)** = unit of measure. **国际单位制 (guójì dānwèizhì)** = SI (the global metric system).

| 量 | 常用单位 | 中文 |
|---|---|---|
| 长度 (chángdù) | 米 (m) | length, metre |
| 质量 (zhìliàng) | 千克 (kg) | mass, kilogram |
| 时间 (shíjiān) | 秒 (s) | time, second |
| 面积 (miànjī) | 平方米 (m²) | area |
| 体积 (tǐjī) | 立方米 (m³) | volume |
| 容积 (róngjī) | 升 (L) = 1000 cm³ | capacity (liquids) |

---

## Length — the metric ladder

Each step is a factor of $10$ (or sometimes $1000$):

| Unit | Symbol | In metres |
|---|---|---|
| millimetre | mm | $10^{-3}$ m |
| centimetre | cm | $10^{-2}$ m |
| metre | m | $1$ m |
| kilometre | km | $10^{3}$ m |

Chains:
- $1$ km = $1000$ m
- $1$ m = $100$ cm
- $1$ cm = $10$ mm

So $1$ km = $1000 \times 100 \times 10 = 1{,}000{,}000$ mm. Worth knowing: $1$ km = $10^6$ mm and $1$ km = $10^5$ cm.

### Imperial / US length — additional context

| Unit | In inches |
|---|---|
| inch (in) | $1$ |
| foot (ft) | $12$ |
| yard (yd) | $36$ ($= 3$ ft) |
| mile (mi) | $63{,}360$ ($= 1760$ yd) |

Cross-conversions: $1$ in $= 2.54$ cm; $1$ mi $\approx 1.609$ km. Do not assume an unfamiliar conversion factor; use the one supplied for the task.

---

## Mass

| Unit | In kg |
|---|---|
| milligram (mg) | $10^{-6}$ kg |
| gram (g) | $10^{-3}$ kg |
| kilogram (kg) | $1$ kg |
| tonne (t) | $10^3$ kg |

Chains: $1$ kg = $1000$ g = $10^6$ mg. $1$ tonne = $1000$ kg.

> [!info] Tonne vs ton
> A *tonne* is $1000$ kg. The US customary *ton* = $2000$ pounds $\approx 907$ kg ("short ton") or *long ton* = $2240$ pounds $\approx 1016$ kg.

---

## Volume / Capacity

Volume in metric scales like length-cubed, but the *unit names* don't always match cleanly:

| Unit | In m³ | Equivalent |
|---|---|---|
| millilitre (mL) | $10^{-6}$ m³ | = $1$ cm³ |
| litre (L) | $10^{-3}$ m³ | = $1000$ cm³ = $1$ dm³ |
| cubic metre (m³) | $1$ m³ | = $1000$ L |

The useful bridge is **$1$ litre = $1000$ cm³**.

> [!warning] Volume conversion factors are *cubed* length factors
> $1$ m = $100$ cm, so $1$ m³ = $100^3 = 10^6$ cm³ — *not* $100$ cm³. This is one of the most common 0580 mistakes. Whenever you convert volumes, *cube* the length conversion.
>
> Same applies to area: $1$ m² = $100^2 = 10{,}000$ cm² — *not* $100$ cm².

---

## Compound Units — units made of other units

Many physical quantities have *compound* units — combinations of basic units.

| Quantity | Unit | Compound form |
|---|---|---|
| Speed | km/h, m/s | length / time |
| Density | g/cm³, kg/m³ | mass / volume |
| Pressure | N/m² (= Pa) | force / area |
| Acceleration | m/s² | length / time² |
| Population density | persons/km² | count / area |

The "/" is read **per**. To convert compound units, convert each piece independently (with attention to powers).

**Example.** $36$ km/h to m/s.

$$36 \text{ km/h} = 36 \times \frac{1000 \text{ m}}{1 \text{ km}} \times \frac{1 \text{ h}}{3600 \text{ s}} = 36 \times \frac{1000}{3600} \text{ m/s} = 10 \text{ m/s}.$$

Quick rule: km/h $\div 3.6$ = m/s. (And m/s $\times 3.6$ = km/h.)

---

## Worked Examples

### Example 1 — length conversion

> Convert $4.5$ km to mm.

$4.5$ km $= 4.5 \times 10^6$ mm $= 4{,}500{,}000$ mm.

### Example 2 — area conversion

> A field has area $0.5$ km². What is its area in m²?

$1$ km = $1000$ m, so $1$ km² = $10^6$ m². Area: $0.5 \times 10^6 = 500{,}000$ m².

### Example 3 — volume conversion

> A bottle holds $750$ mL. What volume is this in cm³?

$1$ mL = $1$ cm³. So $750$ mL = $750$ cm³.

### Example 4 — compound unit

> A metal's density is $7.5$ g/cm³. Express this in kg/m³.

$7.5 \dfrac{\text{g}}{\text{cm}^3} = 7.5 \times \dfrac{10^{-3} \text{ kg}}{10^{-6} \text{ m}^3} = 7.5 \times 10^3 \dfrac{\text{kg}}{\text{m}^3} = 7500 \text{ kg/m}^3$.

The factor $10^3$ comes from "kg conversion gives $10^{-3}$, m³ conversion gives $10^{-6}$, divide gives $10^{3}$."

---

## Common Mistakes

1. **Linear factor used for area / volume.** $1$ m = $100$ cm, but $1$ m² = $10{,}000$ cm² and $1$ m³ = $1{,}000{,}000$ cm³. *Cube the factor* for volume conversions.
2. **Mixing mL and cm³.** They're equal — but that's because $1$ mL is *defined* as $1$ cm³. Don't think they need a conversion factor.
3. **Forgetting that compound-unit conversions need both parts.** km/h to m/s requires *both* the km→m conversion and the h→s conversion.
4. **Tonne vs ton confusion.** A tonne is $1000$ kg. A US short ton is about $907$ kg. If “ton” is ambiguous, establish which definition is intended.

---

## Exam Notes

### Cambridge 0580 — Core and Extended

**C5.1 / E5.1** explicitly require metric mass, length, area, volume and capacity, including squared-unit conversion and volume–capacity conversion. This is Core content as well as Extended content. **C1.12 / E1.12** add rates, including speed and density; the speed–distance–time relationship must be known, while formulas for the other listed measures of rate are supplied as specified in that section.

Practise cm² to m², cm³ to litres, and km/h to m/s. Write the conversion factor so the method is inspectable; a method mark depends on the particular scheme and is not guaranteed by writing a factor alone. Imperial conversion constants are not a named memorisation requirement of C5.1/E5.1.

### OxfordAQA 9260

**G14 Core** explicitly includes standard units of length, area, volume/capacity, mass, time and money, conversion between related units, and compound units such as speed and density. Its time conventions include both 12- and 24-hour clocks; see [[Time Calculations (Vocab)]]. The volume and area factors here apply directly.

### Later mathematics and physics

Cambridge 0606, 9709 and 9231, Edexcel IAL and OxfordAQA 9660 use unit conversion as prior knowledge in applied problems, rather than introducing a separate imperial-unit syllabus through this topic. For IB mathematics, treat these conversions as foundational skills; no claim of a newly covered IB outcome is made here. AP Calculus AB/BC explicitly includes **Mathematical Practice 4.B, use appropriate units of measure**, especially when interpreting rates and accumulated quantities.

### Where the boundary lies

The imperial table is enrichment, not an additional 0580 unit-conversion requirement. This is arithmetic with units; SI base-unit definitions, dimensional analysis and physics-board requirements belong to [[Physical Quantities and Units]]. No advanced mechanics or calculus outcome is completed merely by knowing conversion factors.

---

## Connections

- **Prerequisite:** [[Rates (Vocab)]] — compound units are rates
- **Forward:** [[Area and Perimeter (Vocab)]] — area uses squared lengths
- **Forward:** [[Surface Area and Volume (Vocab)]] — volume uses cubed lengths
- **Application:** *physics* — every formula has consistent units; unit-checking is the most powerful sanity-check in physics labs
- **Application:** *engineering* — engineering drawings specify units (mm, in, μm); mismatches cause expensive failures (Mars Climate Orbiter, 1999, was lost because of a metric-imperial mismatch)
- **Application:** [[Histograms]] — frequency density has units (count per unit width), and the unit-algebra perspective is what makes "area = frequency" come out cleanly
- **Forward (Physics):** [[Physical Quantities and Units]] — the systematic *algebra of units*; derive formula structure from $[F] = [m][a]$, validate physics answers by unit-checking, and use it as the most powerful "did I write the right formula?" test in Mechanics (9709 M1, AP Physics, IB). Includes the seven SI base units, the prefix table from pico to tera, and the pendulum + Trinity worked examples for dimensional analysis as a research tool.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| m, cm, mm, km | `\text{m}, \text{cm}` | always wrap units in `\text{}` |
| m² | `\text{m}^2` | squared length |
| m³ | `\text{m}^3` | cubed length |
| g/cm³ | `\text{g/cm}^3` | compound unit |
| Pa | `\text{Pa}` | pascal = N/m² |
