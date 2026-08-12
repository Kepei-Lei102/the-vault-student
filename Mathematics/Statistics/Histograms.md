---
chinese: 频率直方图 (pínlǜ zhífāng tú)
prerequisites:
  - "[[Classifying Data]]"
  - "[[Statistical Charts]]"
  - "[[Averages and Spread]]"
  - "[[Cumulative Frequency]]"
leads_to:
  - "[[Box Plots]]"
  - "[[Interpreting Data]]"
tags:
  - subject/mathematics
  - domain/statistics
  - level/GCSE
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-S4
  - syllabus/0580-E9-7
  - syllabus/9709-5-1
  - type/concept
  - type/visual-tool
  - misconception/bar-chart-vs-histogram
  - misconception/frequency-vs-frequency-density
---

# Histograms 频率直方图

## Definition

### Formal

A **histogram** is a chart for **continuous grouped data** where the **area** of each bar represents the frequency (not the height). Bars have no gaps — because the data is continuous, every value falls into exactly one class interval. When class widths are unequal, the vertical axis shows **frequency density** rather than frequency:

$$\text{frequency density} = \dfrac{\text{frequency}}{\text{class width}}$$

### Intuitive

A histogram looks like a bar chart at first glance, but the underlying idea is fundamentally different. In a bar chart, you read frequency from the **height** of each bar. In a histogram, you read frequency from the **area** of each bar.

Why does this matter? Because classes can have different widths. If you just used height for frequency, wide classes would dominate the chart visually — even when they contain fewer data values. The comparison below uses the same data both ways:

![[histogram-height-vs-area.svg|700]]

On the left (wrong), the bar for $20 \leq t < 40$ is wide and prominent — your eye reads it as "important" — yet it only contains 6 values. On the right (correct), frequency density shrinks that bar down because those 6 values are spread thinly across 20 minutes. The class $5 \leq t < 10$ (15 values packed into just 5 minutes) correctly stands out as the densest region.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| histogram | 频率直方图 / 直方图 | pínlǜ zhífāng tú / zhífāng tú |
| frequency density | 频率密度 | pínlǜ mìdù |
| frequency | 频数 | pínshu |
| class width | 组距 | zǔ jù |
| class interval | 组距区间 | zǔ jù qūjiān |
| class boundary | 组界 | zǔ jiè |
| continuous data | 连续数据 | liánxù shùjù |
| area | 面积 | miànjī |
| dimensional analysis | 量纲分析 | liángāng fēnxī |

> [!tip] 直方图 — "straight square diagram"
> 直 = straight, 方 = square/rectangular, 图 = diagram. The name describes what you see: rectangles standing upright. Compare with 条形图 (bar chart): 条 = strip, 形 = shape — "strip-shape diagram." The names distinguish the two: rectangles (histogram) vs strips (bar chart).

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $f$ | Frequency — the number of data values in a class |
| $w$ | Class width $= \text{upper boundary} - \text{lower boundary}$ |
| $\text{fd}$ | Frequency density $= \dfrac{f}{w}$ |
| Area of bar | $= \text{fd} \times w = f$ (the frequency) |

> [!warning] The golden rule
> **Area = Frequency.** This is the single most important fact about histograms. Everything else follows from it: why we use frequency density, why bars have no gaps, why wider classes have shorter bars.

### Why "Area = Frequency" works — Unit Algebra (Dimensional Analysis 量纲分析)

The formula $f = \text{fd} \times w$ isn't arbitrary — the **units** force it to be true. Watch the units cancel:

$$\underbrace{\text{frequency density}}_{\text{count per cm}} \times \underbrace{\text{class width}}_{\text{cm}} = \underbrace{\text{frequency}}_{\text{count}}$$

$$\dfrac{\text{count}}{\text{cm}} \times \text{cm} = \text{count}$$

This is the same pattern you see everywhere in physics:

| Formula | Unit algebra |
|---------|-------------|
| distance = speed × time | $\dfrac{\text{m}}{\text{s}} \times \text{s} = \text{m}$ |
| force = mass × acceleration | $\text{kg} \times \dfrac{\text{m}}{\text{s}^2} = \dfrac{\text{kg} \cdot \text{m}}{\text{s}^2}$ (newton) |
| frequency = density × width | $\dfrac{\text{count}}{\text{cm}} \times \text{cm} = \text{count}$ |

The technique of tracking units through a calculation is called **dimensional analysis** (量纲分析, liángāng fēnxī). It's a powerful self-check: if the units don't work out, the formula must be wrong.

> [!tip] The deep connection — this is integration
> Each bar's area is $\text{fd} \times w$ — a "height × width" product. That's exactly the area of a rectangle in a **Riemann sum** (see [[Differentiation]]). As class widths shrink toward zero and the number of bars grows toward infinity, the sum of rectangular areas becomes an integral:
>
> $$\sum \text{fd}_i \times w_i \quad \longrightarrow \quad \int f(x) \, dx$$
>
> The histogram is a Riemann sum; the smooth probability density function is the integral. This is why the "area = frequency" rule works — it's integration in disguise. The units confirm it: $\int \dfrac{\text{count}}{\text{cm}} \, d(\text{cm}) = \text{count}$.

---

## Key Facts / Properties

### Equal vs Unequal Class Widths

**Equal class widths:** When all classes have the same width, frequency density is just frequency ÷ a constant. The bars' heights are proportional to frequency, so the histogram looks like a bar chart with no gaps. You *can* label the $y$-axis as "frequency" in this special case — but it's better practice to always use "frequency density."

**Unequal class widths:** When classes have different widths, you **must** use frequency density on the $y$-axis. Using frequency directly would make wide classes look disproportionately important.

### Building a Histogram from a Table

**Step 1:** Calculate frequency density for each class.

**Example:** Times (minutes) taken by 50 students to complete a puzzle:

| Time $t$ (min) | Frequency ($f$) | Class width ($w$) | Frequency density ($\text{fd} = \dfrac{f}{w}$) |
|-----------------|-----------------|-------------------|------------------------------------------------|
| $0 \leq t < 5$ | 8 | 5 | $\dfrac{8}{5} = 1.6$ |
| $5 \leq t < 10$ | 15 | 5 | $\dfrac{15}{5} = 3.0$ |
| $10 \leq t < 20$ | 18 | 10 | $\dfrac{18}{10} = 1.8$ |
| $20 \leq t < 40$ | 6 | 20 | $\dfrac{6}{20} = 0.3$ |
| $40 \leq t < 60$ | 3 | 20 | $\dfrac{3}{60-40} = 0.15$ |
| **Total** | **50** | | |

**Step 2:** Draw the bars. Each bar spans the full class interval on the $x$-axis (no gaps), and its height equals the frequency density.

![[histogram-unequal-classes.svg|700]]

**Step 3:** Check — the total area of all bars should equal $n$ (the total frequency).

$$\text{Total area} = (5 \times 1.6) + (5 \times 3.0) + (10 \times 1.8) + (20 \times 0.3) + (20 \times 0.15) = 8 + 15 + 18 + 6 + 3 = 50 \checkmark$$

### Reading a Histogram

To find the frequency for a class from a histogram:

$$f = \text{frequency density} \times \text{class width} = \text{area of bar}$$

**Example:** A bar spans $30 \leq x < 50$ (width = 20) with frequency density = 0.8. The frequency is $0.8 \times 20 = 16$.

### Estimating Frequency for a Sub-Interval

Sometimes an exam asks: "Estimate how many values fall between 12 and 15" when the class is $10 \leq t < 20$.

**Method:** Assume values are evenly distributed within the class.

$$\text{estimate} = \text{frequency density} \times \text{sub-interval width} = 1.8 \times (15 - 12) = 1.8 \times 3 = 5.4 \approx 5$$

This is an **estimate** because we're assuming uniform distribution within the class — the actual distribution might not be uniform, but this is the standard exam method.

### Histogram vs Bar Chart — the Complete Comparison

| Feature | Bar chart | Histogram |
|---------|-----------|-----------|
| **Data type** | Categorical or discrete | Continuous (grouped) |
| **Gaps between bars?** | Yes — categories are separate | No — data is continuous |
| **What the height shows** | Frequency | Frequency density |
| **What represents frequency** | Height of bar | **Area** of bar |
| **Bar width** | All equal (arbitrary, cosmetic) | Represents the class width (carries information) |
| **$y$-axis label** | Frequency | Frequency density |
| **When all widths are equal** | — | Looks similar, but the principle is still area = frequency |

> [!info] Why no gaps?
> Gaps in a bar chart signal separate categories — "football" and "basketball" are distinct, with nothing in between. In a histogram, the data is continuous — there is no gap between "10 cm" and "10.0001 cm." The bars must touch to show this continuity. A gap would imply that range of values is impossible, which is false for continuous data.

### Finding the Modal Class

The **modal class** is the class with the highest frequency density (the tallest bar), **not** the class with the highest frequency. A very wide class could have high frequency simply because it covers a large range — the frequency density corrects for this.

**From our example:** The tallest bar is $5 \leq t < 10$ (fd = 3.0), so the modal class is $5 \leq t < 10$.

---

## Common Misconceptions

### 1. "A histogram is just a bar chart with no gaps"

"They look the same — just push the bars together." ✗

**Fix:** The visual similarity hides a fundamental difference. In a bar chart, **height = frequency**. In a histogram, **area = frequency**. When class widths are unequal, treating a histogram like a bar chart gives completely wrong readings. The no-gaps rule is a consequence of continuous data, not the defining feature.

### 2. "The tallest bar has the highest frequency"

"That bar is the tallest, so that class has the most values." ✗ (if class widths are unequal)

**Fix:** The tallest bar has the highest **frequency density**. To find the class with the highest frequency, calculate the **area** of each bar ($\text{fd} \times w$). A short but wide bar can contain more data values than a tall but narrow bar.

### 3. "Frequency density = frequency"

"I'll just use frequency on the $y$-axis." ✗ (if class widths are unequal)

**Fix:** Frequency density = $\dfrac{f}{w}$. It only equals frequency when the class width is 1 — which is rare for continuous data. Using raw frequency on the $y$-axis with unequal widths produces a misleading chart where wider classes appear more important than they are.

### 4. "I can add up the heights to find the total"

"The heights are 1.6, 3.0, 1.8, 0.3, 0.15 — total is 6.85 students?" ✗

**Fix:** Heights are frequency densities, not frequencies. You must add up the **areas** (fd × width), not the heights. The total of the areas equals $n$, the total frequency.

### 5. "The modal class is the class with the highest frequency"

"Class $10 \leq t < 20$ has frequency 18, which is the highest, so it's the modal class." ✗

**Fix:** That class has frequency 18 spread over a width of 10, giving fd = 1.8. Class $5 \leq t < 10$ has frequency 15 in a width of 5, giving fd = 3.0 — a much higher **concentration** of values. The modal class is the one with the highest frequency density. Think of it this way: if you randomly landed in a 1-minute window somewhere in the data, you'd be most likely to find a value in the class where data is most **densely packed**.

---

## Worked Examples

### Example 1: Drawing a histogram with unequal class widths

The table shows the masses (kg) of 100 packages:

| Mass $m$ (kg) | Frequency |
|----------------|-----------|
| $0 < m \leq 5$ | 20 |
| $5 < m \leq 10$ | 30 |
| $10 < m \leq 15$ | 25 |
| $15 < m \leq 25$ | 15 |
| $25 < m \leq 50$ | 10 |

**(a)** Calculate the frequency density for each class.

| Mass $m$ (kg) | Frequency | Width | Frequency density |
|----------------|-----------|-------|-------------------|
| $0 < m \leq 5$ | 20 | 5 | $\dfrac{20}{5} = 4.0$ |
| $5 < m \leq 10$ | 30 | 5 | $\dfrac{30}{5} = 6.0$ |
| $10 < m \leq 15$ | 25 | 5 | $\dfrac{25}{5} = 5.0$ |
| $15 < m \leq 25$ | 15 | 10 | $\dfrac{15}{10} = 1.5$ |
| $25 < m \leq 50$ | 10 | 25 | $\dfrac{10}{25} = 0.4$ |

**(b)** What is the modal class?

The class with the highest frequency density is $5 < m \leq 10$ (fd = 6.0). Even though this class also happens to have the highest raw frequency (30), imagine if it didn't — the modal class is determined by density, not frequency. The class $10 < m \leq 15$ has frequency 25 in the same width, giving fd = 5.0 — close, but $5 < m \leq 10$ is more densely packed.

**(c)** Verify the total area.

$$5(4.0) + 5(6.0) + 5(5.0) + 10(1.5) + 25(0.4) = 20 + 30 + 25 + 15 + 10 = 100 \checkmark$$

### Example 2: Reading a histogram

A histogram shows the heights of plants. One bar spans $20 \leq h < 35$ (width 15) with frequency density 2.4.

**(a)** Find the frequency for this class.

$$f = \text{fd} \times w = 2.4 \times 15 = 36 \text{ plants}$$

**(b)** Estimate how many plants have height between 25 and 30 cm.

$$\text{estimate} = 2.4 \times (30 - 25) = 2.4 \times 5 = 12 \text{ plants}$$

### Example 3: Completing a histogram from partial information

A histogram shows the ages of visitors to a museum. The table is partially complete:

| Age $a$ (years) | Frequency | Width | Frequency density |
|------------------|-----------|-------|-------------------|
| $0 \leq a < 10$ | | 10 | 1.2 |
| $10 \leq a < 20$ | 24 | 10 | |
| $20 \leq a < 30$ | | 10 | 3.0 |
| $30 \leq a < 50$ | | 20 | 1.0 |

**(a)** Complete the table.

- $0 \leq a < 10$: $f = 1.2 \times 10 = 12$
- $10 \leq a < 20$: $\text{fd} = \dfrac{24}{10} = 2.4$
- $20 \leq a < 30$: $f = 3.0 \times 10 = 30$
- $30 \leq a < 50$: $f = 1.0 \times 20 = 20$

**(b)** Find the total number of visitors.

$$12 + 24 + 30 + 20 = 86 \text{ visitors}$$

**(c)** Estimate the number of visitors aged between 15 and 25.

This spans two classes, so split the estimate:

- From $15 \leq a < 20$: $\text{fd} \times \text{width} = 2.4 \times 5 = 12$
- From $20 \leq a < 25$: $3.0 \times 5 = 15$
- Total estimate: $12 + 15 = 27$ visitors

---

## Exam Notes

### OxAQA 9260

- S4 (Extension): construct and interpret histograms with unequal class intervals; use frequency density on the $y$-axis
- Typical question: given a partially complete table and/or histogram → calculate missing frequency densities or frequencies → complete the histogram → find the modal class → estimate frequency for a sub-interval
- Mark scheme: bars drawn at correct positions with correct heights (frequency density), no gaps between bars, $y$-axis labeled "frequency density"
- "Estimate the number of..." = use the area of the relevant portion of a bar (assuming uniform distribution within the class)

### Cambridge 0580

- E9.7: construct and interpret histograms with equal and unequal intervals; frequency density
- Paper 4: high-frequency topic. Often 5–7 marks. The grid is usually provided — check the scale carefully
- Common format: a histogram is drawn with one bar missing → complete the table → draw the missing bar → answer interpretation questions
- The relationship $\text{area} = \text{frequency}$ is the key — every calculation goes through it
- Sometimes combined with cumulative frequency: "use the histogram to complete the cumulative frequency table"

### AP / IB / A-Level

- **AP Statistics:** histograms are fundamental to describing distributions. Students must describe shape (symmetric, skewed left/right, unimodal, bimodal), centre, spread, and unusual features. AP uses **relative frequency histograms** where bar areas sum to 1 (or 100%) — this connects directly to probability.
- **IB Mathematics AI:** histograms appear in the descriptive statistics section; students use technology (GDC) to generate them. IB often asks students to comment on the shape of the distribution and relate it to measures of central tendency.
- **A-Level Statistics:** histograms are the graphical representation of a **probability density function** (PDF). The condition "total area = 1" for a PDF is the continuous analogue of "all probabilities sum to 1." The transition from histogram → PDF is a key conceptual step in A-Level.

### Beyond high school — University

- As noted in the Unit Algebra section above, a histogram is a **Riemann sum**. As class widths shrink toward zero and sample size grows toward infinity, it converges to the **probability density function** (PDF) of the underlying distribution. This is the bridge from descriptive statistics to probability theory — the histogram is the "empirical PDF" just as the cumulative frequency curve is the "empirical CDF" (**cumulative distribution function** — the probability version of the cumulative frequency curve, where the $y$-axis runs from 0 to 1 instead of 0 to $n$). The relationship is: $\text{CDF}(x) = \int_{-\infty}^{x} \text{PDF}(t) \, dt$, and conversely $\text{PDF}(x) = \dfrac{d}{dx}\text{CDF}(x)$ — differentiation and integration connecting two views of the same data.
- **Kernel density estimation** (KDE) is a modern alternative to histograms. Instead of hard-edged rectangular bars, KDE places a smooth "kernel" (usually a Gaussian bell curve) at each data point and sums them up. The result is a smooth density curve that avoids the arbitrary choice of class boundaries. In Python: `seaborn.kdeplot()` or `scipy.stats.gaussian_kde()`.
- The choice of class width (bin width) is a miniature version of the **bias-variance tradeoff** from machine learning. Too few, wide bins → smoothed out, loses detail (high bias / underfitting). Too many, narrow bins → noisy, random spikes (high variance / overfitting). The **Freedman–Diaconis rule** ($\text{bin width} = 2 \times \dfrac{\text{IQR}}{\sqrt[3]{n}}$) balances these using the IQR and sample size.

> [!tip] Interactive exploration
> Histograms can be explored interactively using Python/Jupyter — try `matplotlib.pyplot.hist()` with the `bins` parameter to see how changing bin width affects the shape. Compare with `seaborn.kdeplot()` for smooth density estimation. See [[Jupyter Notebooks]].

---

## Connections

- **Prerequisite:** [[Classifying Data]] — histograms require continuous grouped data with class boundaries
- **Prerequisite:** [[Statistical Charts]] — histograms are the continuous-data counterpart of bar charts; the bar-chart-vs-histogram distinction is defined there
- **Prerequisite:** [[Averages and Spread]] — estimated mean from grouped data uses the same class structure; modal class is identified from frequency density
- **Prerequisite:** [[Cumulative Frequency]] — cumulative frequency curves and histograms are complementary views of the same data; cf tells you "how many below X" while a histogram shows the shape of the distribution
- **Leads to:** [[Box Plots]] — another way to display the distribution of continuous data, using the five-number summary
- **Beyond syllabus:** connects to [[Differentiation]] — the PDF (the smooth limit of a histogram) is the derivative of the CDF (cumulative distribution function)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{f}{w}$ | `\dfrac{f}{w}` | Frequency density formula |
| $\text{fd}$ | `\text{fd}` | Frequency density abbreviation |
| $\leq$ | `\leq` | Class boundary notation |
| $\sqrt[3]{n}$ | `\sqrt[3]{n}` | Cube root — used in Freedman–Diaconis rule |
| $\checkmark$ | `\checkmark` | Verification tick |
