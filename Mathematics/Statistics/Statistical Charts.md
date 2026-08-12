---
chinese: 统计图表 (tǒngjì túbiǎo)
prerequisites:
  - "[[Classifying Data]]"
  - "[[Averages and Spread]]"
  - "[[Relative and Expected Frequency]]"
leads_to:
  - "[[Scatter Diagrams]]"
  - "[[Cumulative Frequency]]"
  - "[[Histograms]]"
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
  - syllabus/9260-S6
  - syllabus/0580-E9-4
  - type/concept
  - type/visual-tool
  - misconception/bar-chart-vs-histogram
  - misconception/pie-chart-angle
---

# Statistical Charts 统计图表

## Definition

### Formal

A **statistical chart** (or statistical diagram) is a visual representation of data. Different types of data require different types of chart — choosing the wrong chart is like using the wrong tool.

This card covers charts for **categorical and discrete data**: bar charts, pie charts, pictograms, stem-and-leaf diagrams, and frequency polygons. Charts for continuous data ([[Histograms]], [[Cumulative Frequency]], [[Box Plots]]) and bivariate data ([[Scatter Diagrams]]) have their own cards.

### Intuitive

A table of numbers tells you everything but shows you nothing. A chart shows you patterns, comparisons, and outliers at a glance — things you'd miss staring at rows of figures. The skill is choosing the right chart for the data and the question you're asking.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| chart / diagram | 图表 | túbiǎo |
| bar chart | 条形图 | tiáoxíng tú |
| pie chart | 饼图 | bǐng tú |
| pictogram | 象形图 | xiàngxíng tú |
| stem-and-leaf diagram | 茎叶图 | jīng yè tú |
| frequency polygon | 频率多边形 | pínlǜ duōbiānxíng |
| frequency | 频数 | pínshu |
| axis (plural: axes) | 轴 | zhóu |
| scale | 刻度 | kèdù |
| key / legend | 图例 | túlì |

> [!tip] 茎叶图 — stem and leaf
> 茎 = stem (of a plant), 叶 = leaf. The Chinese name is a direct translation. 饼图 (bǐng = pancake/cake) for pie chart is also delightfully literal.

---

## Notation

| Term | Meaning |
|------|---------|
| Frequency | How many times a value or category occurs |
| Frequency density | $\dfrac{\text{frequency}}{\text{class width}}$ — used for histograms, NOT for bar charts |
| Class width | The range of values in a grouped interval |
| Sector | A "slice" of a pie chart — an angle at the centre |
| Key | An explanation of what symbols or colours represent in the chart |

---

## Key Facts / Properties

### Choosing the Right Chart

| Data type | Good chart choices | Why |
|-----------|-------------------|-----|
| **Categorical** (eye colour, transport) | Bar chart, pie chart, pictogram | Shows frequency or proportion of each category |
| **Discrete numerical** (goals scored, dice results) | Bar chart, stem-and-leaf | Shows frequency of each value; gaps between bars for discrete |
| **Grouped continuous** (height, time) | Histogram, frequency polygon, cumulative frequency | No gaps between bars — data is continuous |
| **Two variables** (height vs weight) | Scatter diagram | Shows relationship between variables |
| **Comparing distributions** | Back-to-back stem-and-leaf, frequency polygon overlay, box plots | Side-by-side comparison |
| **Parts of a whole** (budget breakdown) | Pie chart | Shows proportions — must add to 100% |

> [!tip] Interactive exploration
> All the charts in this card are shown as static SVG diagrams. If you want to experiment — change the data and see the chart update live — try building them in Python with `matplotlib` in a Jupyter notebook. See [[Jupyter Notebooks]] for how to get started.

### Bar Charts 条形图

A bar chart uses **rectangular bars** to show the frequency (or relative frequency) of each category or value.

**Rules for drawing:**
- Bars have **equal width**
- Height = frequency (or relative frequency)
- **Gaps between bars** — this distinguishes a bar chart from a histogram
- Bars can be vertical or horizontal
- Label both axes; give the chart a title

![[bar-chart-example.svg|700]]

**Reading bar charts:** read the height of each bar from the frequency axis. Common exam questions ask you to read values, find totals, or compare categories.

#### Compound (Stacked) and Grouped Bar Charts

- **Grouped bar chart:** bars for different groups sit **side by side** for each category — good for comparing groups
- **Compound (stacked) bar chart:** bars are **stacked on top of each other** — good for showing totals and proportions within each category

### Pie Charts 饼图

A pie chart uses **sectors** (slices) of a circle to show proportions. The angle of each sector is proportional to the frequency.

$$\text{Angle for category} = \dfrac{\text{frequency of category}}{\text{total frequency}} \times 360°$$

**Example:** 60 students were asked about their favourite sport:

| Sport | Frequency | Angle |
|-------|-----------|-------|
| Football | 20 | $\dfrac{20}{60} \times 360° = 120°$ |
| Tennis | 15 | $\dfrac{15}{60} \times 360° = 90°$ |
| Swimming | 10 | $\dfrac{10}{60} \times 360° = 60°$ |
| Basketball | 15 | $\dfrac{15}{60} \times 360° = 90°$ |
| **Total** | **60** | **360°** |

![[pie-chart-example.svg|700]]

**Checking your work:** the angles must sum to exactly $360°$. If they don't, you've made an arithmetic error.

> [!warning] Pie charts need the total
> A common exam question gives you a pie chart where you know one angle and its frequency, and asks you to find others. The key: find the **total frequency** first.
>
> If the football sector is 120° and represents 20 students:
> $$\dfrac{120°}{360°} = \dfrac{1}{3} \quad \Rightarrow \quad \text{total} = 20 \times 3 = 60$$
> Then you can find any other category from its angle.

#### Reverse Pie Chart Problems

Given: basketball angle = 90°, total = 60 students. Find the frequency.

$$\dfrac{90°}{360°} \times 60 = 15 \text{ students}$$

Given: swimming frequency = 10, swimming angle = 60°. Find the total.

$$\text{total} = \dfrac{10}{60°} \times 360° = 60 \text{ students}$$

> [!warning] When NOT to use a pie chart
> Pie charts only make sense when the categories are **parts of a whole** that add up to 100%. If the categories overlap (a student can like both football AND tennis), a pie chart is misleading. Also, pie charts become unreadable with more than 5–6 categories — use a bar chart instead.

### Pictograms 象形图

A pictogram uses **symbols** (icons) to represent data. Each symbol represents a fixed number of items, defined in a **key**.

**Example:** Key: 🏀 = 10 students

| Sport | Pictogram |
|-------|-----------|
| Football | 🏀🏀 = 20 students |
| Tennis | 🏀½ = 15 students |
| Swimming | 🏀 = 10 students |

Pictograms are visually engaging but imprecise — half-symbols are hard to read exactly. They are mostly used at primary level or in media graphics, rarely in GCSE exams.

### Stem-and-Leaf Diagrams 茎叶图

A stem-and-leaf diagram splits each data value into a **stem** (the leading digits) and a **leaf** (the last digit). It preserves all the original data values — unlike grouped frequency tables.

**Example:** Test scores: 23, 25, 31, 34, 35, 37, 41, 42, 45, 48, 52, 56

| Stem | Leaves |
|------|--------|
| 2 | 3 5 |
| 3 | 1 4 5 7 |
| 4 | 1 2 5 8 |
| 5 | 2 6 |

**Key:** 3 | 4 means 34

> [!warning] The key is not optional
> Without a key, "3 | 4" could mean 3.4, 34, or 340. It feels obvious when you've just written the diagram — but someone reading it later (or an examiner) has no way to know without the key. **Always write the key.** This is the single most commonly lost mark on stem-and-leaf questions.

**Rules for drawing:**
- Leaves must be in **ascending order** (left to right)
- One digit per leaf — if data is 234, the stem is 23 and the leaf is 4
- Always include a **key** explaining how to read the diagram
- Leaves should be evenly spaced (aligned in columns) so you can see the shape

**Why use stem-and-leaf?**
- You can read **every original value** (unlike grouped tables)
- You can find the **median** directly: count to the middle value
- You can see the **shape** of the distribution (skew, clusters, gaps)
- You can find the **mode** (the most repeated leaf) and **range** (largest − smallest)

**Finding the median:** There are 12 values, so the median is between the 6th and 7th values. Counting through: 23, 25, 31, 34, 35, **37**, **41**, 42, 45, 48, 52, 56. Median $= \dfrac{37 + 41}{2} = 39$.

#### Back-to-Back Stem-and-Leaf Diagrams

Used to **compare two data sets** sharing the same stems.

**Example:** Test scores for Class A and Class B:

| Class A (leaves reversed) | Stem | Class B |
|---------------------------|------|---------|
| 5 3 | 2 | 1 4 |
| 7 5 4 1 | 3 | 2 5 8 |
| 8 5 2 1 | 4 | 0 3 7 |
| 6 2 | 5 | 1 5 |

**Key:** Class A: 5 | 3 means 35. Class B: 3 | 2 means 32.

Note: Class A leaves go **right to left** (descending toward the stem). Class B leaves go **left to right** (ascending away from the stem). This makes direct comparison easy — both distributions "grow outward" from the shared stem.

### Frequency Polygons 频率多边形

A frequency polygon is a **line graph** of frequencies, plotted at the **midpoint** of each class interval.

**How to draw:**
1. Calculate the midpoint of each class interval
2. Plot frequency against midpoint
3. Join the points with straight lines
4. Optionally, extend to the axis at both ends (using the midpoints of the "empty" classes before and after)

**Example:** Using the height data from [[Averages and Spread]]:

| Height $h$ (cm) | Frequency | Midpoint |
|-----------------|-----------|----------|
| $140 \leq h < 150$ | 4 | 145 |
| $150 \leq h < 160$ | 9 | 155 |
| $160 \leq h < 170$ | 12 | 165 |
| $170 \leq h < 180$ | 5 | 175 |

Plot points: (145, 4), (155, 9), (165, 12), (175, 5) and join with straight lines.

![[frequency-polygon-example.svg|700]]

**Why use frequency polygons?**
- You can **overlay two or more** frequency polygons on the same axes to compare distributions — much easier than comparing two histograms
- They show the **shape** of the distribution clearly (symmetric, skewed, bimodal)
- They connect to the idea of a **probability density curve** at higher levels

---

## Common Misconceptions

### 1. "A bar chart and a histogram are the same thing"

"Both have bars, so they're the same chart." ✗

**Fix:** They are fundamentally different:

| | Bar chart | Histogram |
|---|---|---|
| **Data type** | Categorical or discrete | Continuous (grouped) |
| **Gaps between bars?** | Yes | No — data is continuous |
| **Bar width** | All equal (arbitrary) | Represents class width |
| **Bar height** | Frequency | Frequency density ($\dfrac{f}{\text{class width}}$) |
| **Area** | Not meaningful | Area $=$ frequency |

The gaps in a bar chart tell you the data is in separate categories. The absence of gaps in a histogram tells you the data is continuous — every value between the boundaries is possible. See [[Histograms]] for full detail.

### 2. Wrong pie chart angle calculation

"There are 5 categories, so each gets $\dfrac{360°}{5} = 72°$." ✗

**Fix:** Angles are proportional to **frequency**, not the number of categories. A category with 30 out of 60 values gets $\dfrac{30}{60} \times 360° = 180°$, not $72°$. Equal angles only apply if all categories have equal frequency.

### 3. Forgetting the key on a stem-and-leaf diagram

Students draw the diagram correctly but omit the key: "3 | 4 means 34."

**Fix:** Without the key, "3 | 4" could mean 3.4, 34, or 340. The key is **essential** — examiners will deduct marks without it.

### 4. Unordered leaves in stem-and-leaf

"Leaves can be in any order." ✗

**Fix:** Leaves **must** be in ascending order within each stem. This is what makes it possible to read off the median, mode, and distribution shape. Unordered leaves defeat the purpose of the diagram.

### 5. Drawing a frequency polygon through the tops of histogram bars

"Just connect the top-left corners of each bar." ✗

**Fix:** Plot the frequency at the **midpoint** of each class interval, not at the edge. The point represents the centre of the interval. If you connect bar edges, you shift the entire distribution sideways.

### 6. Using a pie chart when categories overlap

"I'll make a pie chart showing students who like football, basketball, and swimming." ✗ (if students can like multiple sports)

**Fix:** Pie charts require categories that are **mutually exclusive** and **exhaustive** — every item belongs to exactly one category, and the categories account for everything. If a student can like both football and swimming, the slices would overlap and the total would exceed 100%. Use a bar chart instead.

---

## Worked Examples

### Example 1: Pie chart from a table

A survey of 90 students' favourite colours:

| Colour | Frequency |
|--------|-----------|
| Red | 25 |
| Blue | 30 |
| Green | 20 |
| Yellow | 15 |

**(a)** Calculate the angle for each sector.

| Colour | Frequency | Angle |
|--------|-----------|-------|
| Red | 25 | $\dfrac{25}{90} \times 360° = 100°$ |
| Blue | 30 | $\dfrac{30}{90} \times 360° = 120°$ |
| Green | 20 | $\dfrac{20}{90} \times 360° = 80°$ |
| Yellow | 15 | $\dfrac{15}{90} \times 360° = 60°$ |
| **Total** | **90** | **360°** ✓ |

**(b)** What fraction of students chose blue? $\dfrac{30}{90} = \dfrac{1}{3}$

### Example 2: Reading a pie chart

In a pie chart, the sector for "bus" has an angle of 144° and represents 36 students.

**(a)** Find the total number of students.

$$\text{total} = \dfrac{36}{144°} \times 360° = \dfrac{36 \times 360}{144} = 90 \text{ students}$$

**(b)** The "walk" sector has an angle of 80°. How many students walk?

$$\dfrac{80°}{360°} \times 90 = 20 \text{ students}$$

### Example 3: Stem-and-leaf diagram

The masses (kg) of 15 parcels: 12, 15, 18, 21, 23, 24, 24, 27, 31, 33, 35, 38, 41, 42, 45

| Stem | Leaves |
|------|--------|
| 1 | 2 5 8 |
| 2 | 1 3 4 4 7 |
| 3 | 1 3 5 8 |
| 4 | 1 2 5 |

Key: 2 | 3 means 23 kg

**(a)** Find the median: $n = 15$, position $= \dfrac{16}{2} = 8\text{th}$ value → counting through: the 8th value is **27 kg**.

**(b)** Find the mode: **24 kg** (appears twice — the only repeated value).

**(c)** Find the range: $45 - 12 = 33$ kg.

### Example 4: Comparing with a frequency polygon

Two classes take the same test. Overlay their frequency polygons on one set of axes using the midpoint data:

| Score range | Midpoint | Class A freq | Class B freq |
|-------------|----------|-------------|-------------|
| $20 \leq s < 30$ | 25 | 2 | 5 |
| $30 \leq s < 40$ | 35 | 5 | 8 |
| $40 \leq s < 50$ | 45 | 10 | 12 |
| $50 \leq s < 60$ | 55 | 8 | 3 |
| $60 \leq s < 70$ | 65 | 5 | 2 |

From the polygons: Class A's distribution peaks later (at midpoint 45–55) while Class B peaks earlier (at 35–45). Class A performed better overall — the polygon is shifted to the right. This kind of comparison is much harder to see from tables alone.

---

## Exam Notes

### OxAQA 9260

- S4: construct and interpret bar charts, pie charts, pictograms, stem-and-leaf diagrams (including back-to-back), frequency polygons
- S6: read and interpret tables, charts, and graphs
- S7: compare distributions using appropriate statistics and charts
- Typical question structure: data in a table → draw the chart → use it to answer a question (find the median, compare groups, estimate a value)
- Frequency polygons are explicitly listed for 9260 — know how to draw and interpret them
- "Compare two distributions" questions: use back-to-back stem-and-leaf or overlaid frequency polygons, and give TWO comparisons (one average, one spread)

### Cambridge 0580

- E9.2: read and interpret statistical data from tables, charts, and graphs
- E9.4: draw and interpret bar charts, pie charts, pictograms, stem-and-leaf diagrams (including back-to-back)
- Pie chart calculation is a common Paper 2 (non-calculator) question — practise doing $\dfrac{f}{n} \times 360°$ without a calculator
- Paper 4: expect to draw a chart from data given in a table, then answer interpretation questions

### AP / IB / A-Level

- **AP Statistics:** heavy emphasis on reading and interpreting displays of data; dotplots, stemplots (stem-and-leaf), and bar charts are standard; students must be able to **describe distributions** using shape (symmetric/skewed), centre (mean/median), spread (range/IQR/standard deviation), and unusual features (outliers, gaps, clusters)
- **IB Mathematics AI:** real-world data presentation is central; students are expected to use technology (GDC or software) to produce charts
- **A-Level Statistics:** comparative stem-and-leaf, multiple frequency polygons for comparison, choosing and justifying the appropriate diagram

### Beyond high school — University

- The frequency polygon is the discrete ancestor of the **probability density function** (PDF) — as class widths shrink toward zero and the sample size grows, the polygon smooths into a continuous curve. This limiting process connects statistics to calculus.
- **Edward Tufte's** *The Visual Display of Quantitative Information* (1983) is the foundational text on statistical graphics. His principles — maximise the data-ink ratio, avoid chart junk, show the data — have shaped how scientists, journalists, and analysts present data. If you enjoy the design side of statistics, this book is worth reading.

---

## Connections

- **Prerequisite:** [[Classifying Data]] — the type of data determines which chart to use
- **Prerequisite:** [[Averages and Spread]] — charts visualise what averages and spread summarise
- **Leads to:** [[Histograms]] — the continuous-data equivalent of a bar chart; frequency density replaces frequency
- **Leads to:** [[Cumulative Frequency]] — cumulative frequency curves are a different way to display grouped continuous data
- **Leads to:** [[Box Plots]] — another tool for comparing distributions, built from the five-number summary
- **Leads to:** [[Scatter Diagrams]] — charts for bivariate (two-variable) data
- **Data source:** [[Relative and Expected Frequency]] — relative frequency data is often displayed as bar charts or pie charts
- **Comparison:** frequency polygons overlay neatly — useful for comparing distributions from [[Averages and Spread#Which Average and Spread to Use|the "compare two distributions" exam question]]

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\dfrac{f}{n} \times 360°$ | `\dfrac{f}{n} \times 360°` | Pie chart angle formula |
| $\dfrac{\text{frequency}}{\text{class width}}$ | `\dfrac{\text{frequency}}{\text{class width}}` | Frequency density (for histograms) |
| $\leq$ | `\leq` | Class interval boundaries |
