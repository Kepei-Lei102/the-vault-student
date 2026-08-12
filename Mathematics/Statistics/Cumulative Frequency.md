---
chinese: 累积频数 (lěijī pínshu)
prerequisites:
  - "[[Classifying Data]]"
  - "[[Averages and Spread]]"
  - "[[Statistical Charts]]"
  - "[[Scatter Diagrams]]"
leads_to:
  - "[[Box Plots]]"
  - "[[Histograms]]"
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
  - syllabus/0580-E9-6
  - syllabus/9709-5-1
  - type/concept
  - type/visual-tool
  - misconception/plotting-cumulative-frequency
  - misconception/reading-quartiles
---

# Cumulative Frequency 累积频数

## Definition

### Formal

The **cumulative frequency** of a value $x$ is the total number of data values that are **less than or equal to** $x$. A **cumulative frequency table** adds a running total column to a grouped frequency table, and a **cumulative frequency curve** (or **ogive**) plots this running total as a smooth S-shaped curve.

### Intuitive

Imagine you're queueing for a ride at a theme park and the sign says "estimated wait from this point: 45 minutes." That sign doesn't tell you how many people are behind you or in front — it tells you the **running total** of people ahead of you in the queue. Cumulative frequency works the same way: instead of asking "how many people scored between 40 and 50?", you ask "how many people scored **up to** 50?"

This running total is surprisingly powerful. Once you have it, you can read off the **median**, **quartiles**, and **percentiles** directly from a smooth curve — no sorting needed, no matter how large the data set.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| cumulative frequency | 累积频数 | lěijī pínshu |
| cumulative frequency curve / ogive | 累积频数曲线 | lěijī pínshu qūxiàn |
| upper class boundary | 组上界 | zǔ shàngjiè |
| percentile | 百分位数 | bǎifēnwèi shù |
| quartile | 四分位数 | sìfēnwèi shù |
| median | 中位数 | zhōngwèishù |
| interquartile range | 四分位距 | sìfēnwèi jù |

> [!tip] 累积 — "accumulate"
> 累 = to accumulate / pile up, 积 = to gather / amass. 累积频数 = "accumulated frequency." The same 累积 appears in other contexts: 累积误差 (accumulated error), 日积月累 (accumulate day by day, month by month — a common idiom about gradual progress).

---

## Notation

| Symbol | Meaning |
|--------|---------|
| cf | Cumulative frequency — the running total |
| $n$ | Total frequency (the final cumulative frequency value) |
| $Q_1$ | Lower quartile — the value at $\dfrac{n}{4}$ on the cf axis |
| $Q_2$ | Median — the value at $\dfrac{n}{2}$ on the cf axis |
| $Q_3$ | Upper quartile — the value at $\dfrac{3n}{4}$ on the cf axis |
| IQR | Interquartile range $= Q_3 - Q_1$ |
| $P_k$ | $k$th percentile — the value at $\dfrac{kn}{100}$ on the cf axis |

---

## Key Facts / Properties

### Building a Cumulative Frequency Table

Start with a grouped frequency table. Add a third column where each entry is the **running total** of all frequencies up to and including that class.

**Example:** Heights of 80 students:

| Height $h$ (cm) | Frequency | Cumulative frequency |
|-----------------|-----------|---------------------|
| $140 \leq h < 150$ | 6 | 6 |
| $150 \leq h < 160$ | 14 | $6 + 14 = 20$ |
| $160 \leq h < 170$ | 24 | $20 + 24 = 44$ |
| $170 \leq h < 180$ | 22 | $44 + 22 = 66$ |
| $180 \leq h < 190$ | 10 | $66 + 10 = 76$ |
| $190 \leq h < 200$ | 4 | $76 + 4 = 80$ |

The final cumulative frequency must equal the total number of data values ($n = 80$). If it doesn't, you've made an arithmetic error — go back and check.

### Plotting the Cumulative Frequency Curve

**Critical rule: plot each cumulative frequency at the UPPER class boundary**, not the midpoint, not the lower boundary.

Why? The cumulative frequency of 20 means "20 students have height **less than** 160 cm." This count is complete at the **end** of the class interval $[150, 160)$, so the point goes at $h = 160$.

| Plot point ($x$) | Plot point ($y$) |
|-------------------|------------------|
| 150 | 6 |
| 160 | 20 |
| 170 | 44 |
| 180 | 66 |
| 190 | 76 |
| 200 | 80 |

> [!warning] Upper boundary, not midpoint
> The single most common mistake in cumulative frequency: plotting at the **midpoint** of each class. This shifts the entire curve to the left and gives wrong readings for median and quartiles. Always plot at the **upper class boundary**.

**Drawing the curve:**

1. Plot the points at (upper boundary, cumulative frequency)
2. **Add a starting point** at the lower boundary of the first class with cf = 0. In our example: $(140, 0)$. This anchors the curve to the axis.
3. Join the points with a **smooth S-shaped curve** (not straight lines between points — the data is continuous, so the curve should be smooth)
4. The curve should be **non-decreasing** — it can flatten but never go down

![[cumulative-frequency-curve.svg|700]]

### Reading Values from the Curve

#### Median ($Q_2$)

1. Calculate $\dfrac{n}{2}$. In our example: $\dfrac{80}{2} = 40$
2. Draw a horizontal line from 40 on the cf axis to the curve
3. Draw a vertical line down to the $x$-axis
4. Read the value: **median ≈ 168 cm**

#### Lower Quartile ($Q_1$)

1. Calculate $\dfrac{n}{4}$. In our example: $\dfrac{80}{4} = 20$
2. Read across and down: **$Q_1$ ≈ 160 cm**

#### Upper Quartile ($Q_3$)

1. Calculate $\dfrac{3n}{4}$. In our example: $\dfrac{3 \times 80}{4} = 60$
2. Read across and down: **$Q_3$ ≈ 177 cm**

#### Interquartile Range

$$\text{IQR} = Q_3 - Q_1 \approx 177 - 160 = 17 \text{ cm}$$

#### Percentiles

To find the $k$th percentile, go to $\dfrac{kn}{100}$ on the cf axis and read across.

**Example:** The 90th percentile means 90% of data is below this value.

$$P_{90}: \dfrac{90 \times 80}{100} = 72 \text{ on the cf axis} \longrightarrow P_{90} \approx 187 \text{ cm}$$

> [!info] Quartiles ARE percentiles
> $Q_1 = P_{25}$, $Q_2 = P_{50}$ (the median), $Q_3 = P_{75}$. Quartiles divide data into quarters; percentiles divide into hundredths. Same idea, different granularity.

> [!tip] Real-world example: US News college rankings
> The US News Best Colleges rankings list each university's **25th, 50th, and 75th percentile SAT scores** — that's $Q_1$, $Q_2$, and $Q_3$. If a university reports SAT scores of 1320 / 1450 / 1530, it means: 25% of admitted students scored below 1320, half scored below 1450 (the median), and 75% scored below 1530. The IQR ($1530 - 1320 = 210$ points) tells you how spread out the middle half of students are — a small IQR means the university admits a very consistent cohort, while a large IQR means wider variation. This is exactly the same reading you do from a cumulative frequency curve, just presented as numbers instead of a graph.

### Using Cumulative Frequency to Estimate "How Many"

You can also use the curve in reverse — to estimate how many values fall below (or above) a given threshold.

**Example:** How many students are taller than 175 cm?

1. Go to 175 on the $x$-axis
2. Read up to the curve, then across to the cf axis: cf ≈ 58
3. So 58 students are shorter than or equal to 175 cm
4. Therefore $80 - 58 = 22$ students are taller than 175 cm

### Shape of the Curve

The S-shape (sigmoid) of a cumulative frequency curve tells you about the distribution:

- **Steep section** = many data values concentrated here (high frequency)
- **Flat section** = few data values here (low frequency)
- **Point of inflection** (where the curve changes from concave to convex) = approximately where the mode/peak of the distribution is

> [!info] Beyond syllabus — the S-curve everywhere
> The cumulative frequency curve's S-shape appears throughout mathematics and science: the **logistic function** (逻辑斯蒂函数, luójísīdì hánshù) in population growth, the **cumulative distribution function** (CDF) in probability, the **sigmoid activation function** in neural networks. The shape emerges whenever something accumulates gradually — slow at first, fast in the middle, slow at the end. Recognising this shape is a transferable skill. The logistic function is formally taught in **AP Calculus BC** (Unit 7.9) as a differential equation: $\dfrac{dy}{dt} = ky(a - y)$, where $a$ is the carrying capacity. It is not in AP Statistics, standard IB, or A-Level — but the S-shape itself is universal.

---

## Common Misconceptions

### 1. "Plot at the midpoint of each class"

"The class is $160 \leq h < 170$, so I plot at 165." ✗

**Fix:** Plot at the **upper class boundary** (170 in this case). The cumulative frequency tells you how many values are below the top of the interval, not the middle. Plotting at the midpoint shifts your entire curve left, making all your readings (median, quartiles) inaccurate.

### 2. "Join the points with straight lines"

"I connected all the points with a ruler." ✗

**Fix:** The data is continuous, so the curve should be **smooth** — a gentle S-shape drawn freehand. Straight-line segments create corners where the gradient changes abruptly, which doesn't reflect continuous data. (Some mark schemes accept a polygon, but a smooth curve is expected for full marks.)

### 3. "The median is at cf = $\dfrac{n+1}{2}$"

"There are 80 values, so the median is at $\dfrac{81}{2} = 40.5$." ✗ (for cumulative frequency curves)

**Fix:** For **cumulative frequency curves**, use $\dfrac{n}{2}$, not $\dfrac{n+1}{2}$. The $\dfrac{n+1}{2}$ formula is for **listed data** (raw, ungrouped values). Since the curve is an estimate for grouped data, the simpler $\dfrac{n}{2}$ is standard and what mark schemes expect. See [[Averages and Spread]] for when each formula applies.

### 4. "Forgetting the starting point at cf = 0"

"I started plotting from the first class." ✗

**Fix:** Add a point at (lower boundary of first class, 0). Without this, your curve floats in the air and doesn't connect to the axis, making it hard to read values for the first class interval.

### 5. "The curve can go down"

"My curve dips in the middle because the frequency dropped." ✗

**Fix:** Cumulative frequency is a **running total** — it can only stay the same or increase. If your curve goes down, you've made an error in the table. Even if one class has zero frequency, the cumulative frequency stays flat through that interval (it doesn't decrease).

---

## Worked Examples

### Example 1: Full cumulative frequency problem

The table shows the masses (kg) of 60 parcels:

| Mass $m$ (kg) | Frequency |
|----------------|-----------|
| $0 < m \leq 2$ | 5 |
| $2 < m \leq 4$ | 12 |
| $4 < m \leq 6$ | 18 |
| $6 < m \leq 8$ | 15 |
| $8 < m \leq 10$ | 7 |
| $10 < m \leq 12$ | 3 |

**(a)** Complete the cumulative frequency table.

| Mass $m$ (kg) | Frequency | Cumulative frequency |
|----------------|-----------|---------------------|
| $0 < m \leq 2$ | 5 | 5 |
| $0 < m \leq 4$ | 12 | 17 |
| $0 < m \leq 6$ | 18 | 35 |
| $0 < m \leq 8$ | 15 | 50 |
| $0 < m \leq 10$ | 7 | 57 |
| $0 < m \leq 12$ | 3 | 60 ✓ |

Check: the last value equals $n = 60$. ✓

**(b)** Plot the cumulative frequency curve.

Plot these points and join with a smooth curve:

$(0, 0)$, $(2, 5)$, $(4, 17)$, $(6, 35)$, $(8, 50)$, $(10, 57)$, $(12, 60)$

**(c)** Use the curve to estimate the median.

$\dfrac{n}{2} = \dfrac{60}{2} = 30$. Read across from 30 on the cf axis → **median ≈ 5.5 kg**

**(d)** Estimate $Q_1$ and $Q_3$.

$\dfrac{n}{4} = 15$ → $Q_1 \approx 3.8$ kg

$\dfrac{3n}{4} = 45$ → $Q_3 \approx 7.4$ kg

**(e)** Estimate the interquartile range.

$$\text{IQR} = Q_3 - Q_1 \approx 7.4 - 3.8 = 3.6 \text{ kg}$$

**(f)** Estimate how many parcels weigh more than 9 kg.

From the curve: cf at $m = 9$ is approximately 54. So $60 - 54 = 6$ parcels weigh more than 9 kg.

### Example 2: Comparing two distributions

Two schools take the same test. Their cumulative frequency curves are drawn on the same axes.

School A: median = 55, IQR = 20
School B: median = 62, IQR = 12

**Compare the two distributions.**

School B has a **higher median** (62 vs 55), so students at School B performed better on average. School B also has a **smaller IQR** (12 vs 20), so results at School B were more consistent — less spread between the top and bottom performers. School A had more variation in results.

> [!info] The two-comparison rule
> When comparing distributions in exams, always give **two comparisons**: one about average (median) and one about spread (IQR). Use the data to support each statement. "School B did better" alone is not enough — say *how much* better and back it up with numbers.

### Example 3: Reading a percentile

Using the parcel data from Example 1, estimate the 80th percentile.

$$P_{80}: \dfrac{80 \times 60}{100} = 48 \text{ on the cf axis}$$

Read across from 48 → $P_{80} \approx 7.8$ kg

This means approximately 80% of parcels weigh 7.8 kg or less.

---

## Exam Notes

### OxAQA 9260

- S4 (Extension): construct and interpret cumulative frequency diagrams; use them to estimate the median, quartiles, interquartile range, and percentiles
- Typical question: given a grouped frequency table → complete the cf table → draw the cf curve → read median and quartiles → calculate IQR → possibly compare with another distribution
- "Use your graph to estimate..." means read from the curve — show your construction lines (horizontal to curve, vertical down to axis)
- Mark scheme: points plotted at upper class boundaries (1 mark), smooth curve through points (1 mark), correct median reading with tolerance ± half a small square (1 mark)
- Often paired with a box plot question: "Using the values from your curve, draw a box plot for this data"

### Cambridge 0580

- E9.6: construct and use cumulative frequency diagrams; estimate and interpret the median, percentiles, quartiles, and interquartile range
- Paper 4: almost always appears — high frequency topic. Expect a 6–8 mark question combining cf table, cf curve, and readings
- The grid is usually provided with pre-drawn axes. Check the scale carefully before plotting — a common error is misreading the axis scale
- "Estimate the number of..." questions = use the curve in reverse (value → cf, then subtract from $n$ if asking for "more than")

### AP / IB / A-Level

- **AP Statistics:** cumulative relative frequency plots ("ogives") are standard; students must interpret percentile ranks and use ogives to describe distributions. The AP exam uses **cumulative relative frequency** (0 to 1 or 0% to 100%) rather than raw cumulative frequency.
- **IB Mathematics AI:** cumulative frequency is part of the descriptive statistics toolkit; students use GDC to generate ogives and read percentiles. IB often asks students to estimate the number of data values within a given range using the curve.
- **A-Level Statistics:** cumulative frequency is foundational for the **cumulative distribution function** (CDF) — the theoretical version of the ogive. For a continuous random variable $X$, the CDF is $F(x) = P(X \leq x)$, which is the probability analogue of cumulative frequency.

### Beyond high school — University

- The cumulative frequency curve is the **empirical CDF** — the data-driven version of the theoretical cumulative distribution function $F(x) = P(X \leq x)$. As the sample size grows and the class widths shrink, the stepped/curved empirical CDF converges to the smooth theoretical CDF. This convergence is formalised by the **Glivenko–Cantelli theorem** (sometimes called the "fundamental theorem of statistics").
- **Kolmogorov–Smirnov test:** compares the empirical CDF of your data with a theoretical distribution by measuring the maximum vertical distance between the two curves. If the distance is small, the data plausibly came from that distribution. This test is used in practice to check normality and compare samples.
- **Survival analysis** in medicine uses a related concept: the **survival function** $S(t) = 1 - F(t) = P(T > t)$, which is a "reverse" cumulative frequency — it counts down instead of up, tracking the proportion of patients surviving past time $t$. The **Kaplan–Meier estimator** is the standard way to construct this curve from real clinical trial data.

> [!tip] Interactive exploration
> Cumulative frequency curves and percentile readings can be explored interactively using Python/Jupyter — try `matplotlib.pyplot.step()` for empirical CDFs and `numpy.percentile()` for exact percentile calculations. See [[Jupyter Notebooks]].

---

## Connections

- **Prerequisite:** [[Classifying Data]] — cumulative frequency requires continuous grouped data with class boundaries
- **Prerequisite:** [[Averages and Spread]] — median, quartiles, and IQR are defined here; cumulative frequency provides a graphical method to find them for large data sets
- **Prerequisite:** [[Statistical Charts]] — the cumulative frequency curve is another chart type for continuous data
- **Leads to:** [[Box Plots]] — the five-number summary (min, $Q_1$, $Q_2$, $Q_3$, max) read from a cumulative frequency curve is used directly to draw a box plot
- **Leads to:** [[Histograms]] — histograms and cumulative frequency curves are complementary views of the same grouped continuous data. The histogram shows the shape of the distribution; the cumulative frequency curve makes it easy to read percentiles.
- **Related:** [[Scatter Diagrams]] — both deal with continuous data, but scatter diagrams explore relationships between two variables while cumulative frequency summarises one variable
- **Related:** [[Relative and Expected Frequency]] — relative frequency is frequency ÷ total; cumulative relative frequency is the cumulative version, directly connecting to probability

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $Q_1$ | `Q_1` | Lower quartile — at $\dfrac{n}{4}$ on cf axis |
| $Q_2$ | `Q_2` | Median — at $\dfrac{n}{2}$ on cf axis |
| $Q_3$ | `Q_3` | Upper quartile — at $\dfrac{3n}{4}$ on cf axis |
| $P_k$ | `P_k` | $k$th percentile — at $\dfrac{kn}{100}$ on cf axis |
| $\dfrac{n}{2}$ | `\dfrac{n}{2}` | Position for median on cf curve |
| $\dfrac{3n}{4}$ | `\dfrac{3n}{4}` | Position for upper quartile |
| $\leq$ | `\leq` | "Less than or equal to" — used in class boundaries |
| $F(x)$ | `F(x)` | Cumulative distribution function (AP/university) |
