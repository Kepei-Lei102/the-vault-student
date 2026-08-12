---
chinese: 箱线图 (xiāngxiàn tú)
prerequisites:
  - "[[Averages and Spread]]"
  - "[[Cumulative Frequency]]"
  - "[[Classifying Data]]"
  - "[[Histograms]]"
  - "[[Statistical Charts]]"
leads_to:
  - "[[Interpreting Data]]"
tags:
  - subject/mathematics
  - domain/statistics
  - level/GCSE
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - syllabus/9260-S4
  - syllabus/9709-5-1
  - type/concept
  - type/visual-tool
  - misconception/box-plot-symmetry
  - misconception/whisker-length
---

# Box Plots 箱线图

## Definition

### Formal

A **box plot** (also called a **box-and-whisker diagram**) is a graphical display of the **five-number summary** of a data set:

$$\text{minimum}, \quad Q_1, \quad \text{median}, \quad Q_3, \quad \text{maximum}$$

The **box** spans from $Q_1$ to $Q_3$ (the interquartile range), with a line inside at the **median**. **Whiskers** extend from the box to the minimum and maximum values. Together, these five values divide the data into four quarters, each containing approximately 25% of the values.

### Intuitive

A box plot is a snapshot of how your data is spread out. The box in the middle captures the middle 50% of the data — if you're "typical," you're somewhere inside the box. The line inside the box is the median — the exact middle value. The whiskers reach out to the extremes, showing the full range.

What makes box plots powerful is that they compress a whole data set into five numbers you can draw in seconds — and when you put two box plots side by side, you can instantly compare two groups.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| box plot / box-and-whisker diagram | 箱线图 / 箱形图 | xiāngxiàn tú / xiāngxíng tú |
| five-number summary | 五数概括 | wǔ shù gàikuò |
| whisker | 须 / 触须 | xū / chùxū |
| median | 中位数 | zhōngwèi shù |
| lower quartile ($Q_1$) | 下四分位数 | xià sìfēnwèi shù |
| upper quartile ($Q_3$) | 上四分位数 | shàng sìfēnwèi shù |
| interquartile range (IQR) | 四分位距 | sìfēnwèi jù |
| outlier | 异常值 / 离群值 | yìcháng zhí / líqún zhí |
| skew / skewness | 偏态 | piāntài |

> [!tip] 箱线图 — "box-line diagram"
> 箱 = box, 线 = line/wire, 图 = diagram. The "lines" are the whiskers. The alternative name 箱形图 (xiāngxíng tú) means "box-shape diagram." Both are widely used in Chinese statistics textbooks.

---

## Notation

| Symbol | Meaning |
|--------|---------|
| Min | Smallest value in the data set (or smallest non-outlier, if using outlier rules) |
| $Q_1$ | Lower quartile — 25th percentile |
| $Q_2$ or Median | Middle value — 50th percentile |
| $Q_3$ | Upper quartile — 75th percentile |
| Max | Largest value in the data set (or largest non-outlier, if using outlier rules) |
| IQR | Interquartile range $= Q_3 - Q_1$ |

> [!warning] The four quarters
> Each section of a box plot (left whisker, left half of box, right half of box, right whisker) contains approximately **25%** of the data — but the sections have different **widths**. A long section means data is spread out (sparse); a short section means data is concentrated (dense). The width does **not** show how many values are in that section.

---

## Key Facts / Properties

### The Five-Number Summary

Every box plot is built from exactly five numbers:

$$\text{Min} \quad \leq \quad Q_1 \quad \leq \quad \text{Median} \quad \leq \quad Q_3 \quad \leq \quad \text{Max}$$

These split the ordered data into four groups, each containing roughly a quarter of the values.

**Example:** 15 students' test scores (already sorted):

$$23, \; 31, \; 35, \; 42, \; 48, \; 52, \; 55, \; 58, \; 63, \; 67, \; 71, \; 76, \; 80, \; 85, \; 92$$

- **Min** $= 23$
- **$Q_1$** $= 42$ (median of the lower half: $23, 31, 35, \mathbf{42}, 48, 52, 55$ — the 4th of 7 values)
- **Median** $= 58$ (the 8th value)
- **$Q_3$** $= 76$ (median of the upper half: $63, 67, 71, \mathbf{76}, 80, 85, 92$ — the 4th of 7 values)
- **Max** $= 92$

> [!info] Which quartile method?
> There are several methods for calculating quartiles (see [[Averages and Spread]]). For large data sets, the differences are negligible. For GCSE/9260 exams, if the data is presented as a cumulative frequency curve, read $Q_1$ and $Q_3$ directly from the curve at $\dfrac{n}{4}$ and $\dfrac{3n}{4}$.

### Drawing a Box Plot

![[box-plot-anatomy.svg|700]]

**Step 1:** Find the five-number summary (from raw data, a table, or a cumulative frequency curve).

**Step 2:** Draw a number line covering the full range of the data.

**Step 3:** Draw the box from $Q_1$ to $Q_3$, with a vertical line at the median.

**Step 4:** Draw whiskers from the box to the minimum and maximum.

**Step 5:** If using outlier rules (see below), draw whiskers to the most extreme non-outlier values, and mark outliers as individual points (usually crosses or circles).

### Reading a Box Plot

From a box plot you can directly read:

- **Median** — the line inside the box
- **Range** $= \text{Max} - \text{Min}$ (tip of right whisker $-$ tip of left whisker)
- **IQR** $= Q_3 - Q_1$ (width of the box)
- **Skewness** — from the symmetry of the plot (see below)

You **cannot** read from a box plot:

- The **mean** (box plots don't show it)
- The **mode** or **modal class**
- The **exact number of data points** (each quarter looks different but holds the same proportion)
- Individual data values (except min, $Q_1$, median, $Q_3$, max)

### Identifying Skewness

The shape of a box plot reveals the skewness of the distribution:

**Symmetric:** The median is centred in the box; whiskers are roughly equal length.

**Positive skew (skewed right):** The median is closer to $Q_1$; the right whisker is longer. The "tail" stretches toward high values. Think: salary data — most people earn modest amounts, a few earn very high salaries.

**Negative skew (skewed left):** The median is closer to $Q_3$; the left whisker is longer. The "tail" stretches toward low values. Think: exam scores on an easy test — most students do well, a few do very poorly.

> [!tip] Memory aid
> "The skew points to the tail." Positive skew = tail to the right (positive direction). Negative skew = tail to the left (negative direction).

### Outliers — the 1.5 × IQR Rule

An **outlier** is a data value that is unusually far from the rest of the data. The standard rule:

$$\text{A value is an outlier if it is:}$$
$$\text{below } Q_1 - 1.5 \times \text{IQR} \quad \text{or} \quad \text{above } Q_3 + 1.5 \times \text{IQR}$$

These boundaries are called **fences**:

- **Lower fence** $= Q_1 - 1.5 \times \text{IQR}$
- **Upper fence** $= Q_3 + 1.5 \times \text{IQR}$

When outlier rules are applied:
- Whiskers extend to the most extreme values **inside** the fences (not to the actual min/max)
- Outliers are plotted as individual points beyond the whiskers

**Example:** Using the test scores above: $Q_1 = 42$, $Q_3 = 76$, IQR $= 76 - 42 = 34$.

- Lower fence $= 42 - 1.5 \times 34 = 42 - 51 = -9$
- Upper fence $= 76 + 1.5 \times 34 = 76 + 51 = 127$

All values fall within the fences, so there are no outliers in this data set.

> [!info] When is the outlier rule required?
> The 9260 specification says "box plots" without specifying outlier rules. Cambridge 0580 does not include box plots at all. The $1.5 \times \text{IQR}$ rule is standard in AP Statistics and IB. In a 9260 exam, if outliers are relevant, the question will tell you — otherwise, draw whiskers to the actual min and max.

### Box Plots from Cumulative Frequency Curves

This is a very common exam combination. The steps:

**Step 1:** Read $Q_1$, median, and $Q_3$ from the cumulative frequency curve (at $\dfrac{n}{4}$, $\dfrac{n}{2}$, $\dfrac{3n}{4}$).

**Step 2:** Read the minimum from the start of the data range (usually the lower boundary of the first class) and the maximum from the end (upper boundary of the last class).

**Step 3:** Draw the box plot on the same horizontal scale as the cumulative frequency curve (or on a scale given in the question).

> [!warning] Min and Max from grouped data
> When data is grouped, you cannot see the actual minimum and maximum values — only the class boundaries. Use the **lower boundary of the first class** as the minimum and the **upper boundary of the last class** as the maximum, unless the question provides the actual values.

### Comparing Distributions

Box plots are at their most powerful when placed **parallel** (sharing the same scale) to compare two or more groups. A comparison should address:

1. **Average (centre):** compare the medians — "On average, Group B scored higher (median 65 vs 58)."
2. **Spread (consistency):** compare the IQRs — "Group A's scores were more spread out (IQR 28 vs 17), meaning less consistent."
3. **Context:** relate the numbers back to the situation — "This suggests Group B's revision strategy was more effective and produced more uniform results."

> [!warning] Exam technique — TWO comparisons
> "Compare these distributions" always requires **two** comparisons: one about the centre (median) and one about the spread (IQR or range). A single comparison earns only half marks. Always use the data — state the actual values, don't just say "higher" or "more spread out."

---

## Common Misconceptions

### 1. "The wider section contains more data"

"The right whisker is longer, so there are more values in that quarter." ✗

**Fix:** Every section (each whisker, each half of the box) contains approximately 25% of the data. A longer section means the data in that quarter is more **spread out**, not that there is more of it. Think of it as density: a short section = data tightly packed; a long section = data sparsely spread.

### 2. "The median should be in the middle of the box"

"The median line isn't centred — the box plot must be wrong." ✗

**Fix:** The median is only in the centre of the box when the data is perfectly symmetric. In skewed data, the median is pulled toward the denser side. An off-centre median is a feature, not a flaw — it tells you the data is skewed.

### 3. "The box shows the range"

"The width of the box is the range of the data." ✗

**Fix:** The box spans from $Q_1$ to $Q_3$ — its width is the **IQR**, not the range. The range is from whisker tip to whisker tip (or from the leftmost outlier to the rightmost outlier, if outliers are shown).

### 4. "I can read the mean from the box plot"

"The median line is the mean." ✗

**Fix:** The line in the box is the **median**, not the mean. For symmetric data, mean ≈ median, so the distinction barely matters. For skewed data, the mean is pulled toward the tail while the median stays in the denser region. Box plots do not show the mean at all (some software adds a diamond or cross for the mean, but this is non-standard).

### 5. "Outliers are errors that should be removed"

"That point is an outlier — it must be a mistake, delete it." ✗

**Fix:** An outlier is a value that is **unusual**, not necessarily **wrong**. It could be a genuine extreme value (a 2-metre-tall student is unusual but real), a data entry error (recording 180 kg instead of 18 kg), or a measurement from a different population (an adult's score mixed in with children's data). Always **investigate** outliers before deciding what to do — removing real data distorts your analysis.

---

## Worked Examples

### Example 1: Drawing a box plot from raw data

The number of hours 12 students spent revising for a test:

$$2, \; 5, \; 7, \; 8, \; 10, \; 12, \; 14, \; 15, \; 18, \; 22, \; 25, \; 30$$

**(a)** Find the five-number summary.

- $n = 12$
- Min $= 2$
- $Q_1 =$ median of lower half ($2, 5, 7, 8, 10, 12$) $= \dfrac{7 + 8}{2} = 7.5$
- Median $= \dfrac{12 + 14}{2} = 13$ (average of 6th and 7th values)
- $Q_3 =$ median of upper half ($14, 15, 18, 22, 25, 30$) $= \dfrac{18 + 22}{2} = 20$
- Max $= 30$

Five-number summary: **2, 7.5, 13, 20, 30**

**(b)** Determine whether there are any outliers.

IQR $= Q_3 - Q_1 = 20 - 7.5 = 12.5$

- Lower fence $= 7.5 - 1.5 \times 12.5 = 7.5 - 18.75 = -11.25$
- Upper fence $= 20 + 1.5 \times 12.5 = 20 + 18.75 = 38.75$

All values fall within $[-11.25, \; 38.75]$, so there are no outliers.

**(c)** Describe the shape of the distribution.

The median (13) is closer to $Q_1$ (7.5) than to $Q_3$ (20). The right whisker ($Q_3$ to Max: $30 - 20 = 10$) is shorter than the IQR, but the right half of the box ($Q_3 - \text{Median} = 7$) is larger than the left half ($\text{Median} - Q_1 = 5.5$). The distribution shows a slight **positive skew** — the data stretches toward higher values.

### Example 2: Reading from a box plot and comparing

Two parallel box plots show journey times (minutes) for Route A and Route B:

| | Min | $Q_1$ | Median | $Q_3$ | Max |
|---|-----|-------|--------|-------|-----|
| Route A | 15 | 22 | 28 | 38 | 52 |
| Route B | 20 | 25 | 30 | 33 | 40 |

**(a)** Find the IQR for each route.

- Route A: IQR $= 38 - 22 = 16$ minutes
- Route B: IQR $= 33 - 25 = 8$ minutes

**(b)** Compare the two distributions.

Route B has a slightly higher median journey time (30 vs 28 minutes), so on average Route B is marginally slower. However, Route B is much more **consistent** — its IQR of 8 minutes is half that of Route A (16 minutes), and its range ($40 - 20 = 20$) is much smaller than Route A's ($52 - 15 = 37$). If you need a **predictable** journey time, Route B is the better choice.

### Example 3: Box plot from a cumulative frequency curve

A cumulative frequency curve for the heights (cm) of 60 plants has already been drawn. From the curve:

- At $\dfrac{n}{4} = 15$: $Q_1 = 12$ cm
- At $\dfrac{n}{2} = 30$: median $= 18$ cm
- At $\dfrac{3n}{4} = 45$: $Q_3 = 23$ cm
- Lower boundary of first class: 5 cm
- Upper boundary of last class: 35 cm

**(a)** Draw a box plot for this data.

Five-number summary: $5, \; 12, \; 18, \; 23, \; 35$

The box spans from 12 to 23 (IQR = 11 cm), with the median line at 18. Whiskers extend from 5 to 12 (left) and 23 to 35 (right).

**(b)** Comment on the skewness.

Median $-$ $Q_1$ $= 18 - 12 = 6$. $Q_3$ $-$ Median $= 23 - 18 = 5$. These are similar, suggesting the box is roughly symmetric. However, the right whisker ($35 - 23 = 12$) is much longer than the left whisker ($12 - 5 = 7$), indicating a slight **positive skew** — a few plants grew to unusual heights.

---

## Exam Notes

### OxAQA 9260

- S4 (Extension): construct and interpret box plots; use them to compare distributions
- Typical question: given a cumulative frequency curve or a set of data → draw a box plot → compare with a second distribution → comment on centre and spread
- Mark scheme: correct five-number summary (1 mark each for $Q_1$, median, $Q_3$, usually read from a cf curve); correctly drawn box with whiskers on a linear scale; comparison with two valid statements (one about average, one about spread) with context
- The outlier rule ($1.5 \times \text{IQR}$) is not typically tested in 9260 but may appear as a defined term in the question — follow whatever definition the question provides
- Common follow-up: "Explain which class performed better, using values from the box plots to support your answer"

### Cambridge 0580

- Box plots are **not** part of the 0580 Extended syllabus. If you encounter them in practice, it's likely from a different specification (9260, IB, or AP).

### AP / IB / A-Level

- **AP Statistics:** box plots (called "boxplots" in AP style) are a core tool for exploratory data analysis. The $1.5 \times \text{IQR}$ rule for outliers is required. AP distinguishes between **standard box plots** (whiskers to min/max) and **modified box plots** (whiskers to fences, outliers plotted individually). The modified version is strongly preferred and the default on graphing calculators (TI-83/84).
- **IB Mathematics AI SL/HL:** box-and-whisker diagrams are part of the descriptive statistics syllabus. Students are expected to use technology (GDC) to generate them and interpret them in context.
- **A-Level Statistics:** box plots are used for comparing distributions and identifying outliers. The interquartile range and outlier identification using $Q_1 - 1.5 \times \text{IQR}$ / $Q_3 + 1.5 \times \text{IQR}$ fences are standard.

### Beyond high school — University

![[violin-and-notched-boxplot.svg|700]]

- **Violin plots** combine a box plot with a **kernel density estimation** (KDE, see [[Histograms]]) mirrored on each side, showing the full shape of the distribution rather than just five summary numbers. This reveals features that box plots hide — bimodality, gaps, and non-standard shapes. The diagram above uses a bimodal distribution (two peaks at 35 and 65) to show the difference: the standard box plot looks perfectly ordinary, but the violin immediately exposes the two clusters. In Python: `seaborn.violinplot()`.
- **Notched box plots** add a notch (an indentation) around the median. The notch represents an approximate **confidence interval** for the median: if the notches of two box plots don't overlap, there is strong evidence that the medians differ significantly — a quick visual significance test without running a formal hypothesis test. The notch width is $\pm 1.58 \times \dfrac{\text{IQR}}{\sqrt{n}}$.
- The $1.5 \times \text{IQR}$ rule was proposed by John Tukey in 1977 as part of his influential *Exploratory Data Analysis* (EDA) approach. The factor 1.5 is deliberately arbitrary — a judgment call, not a theorem. Tukey also defined "far outliers" beyond $3 \times \text{IQR}$. For normally distributed data, $1.5 \times \text{IQR}$ captures approximately 99.3% of values, so roughly 0.7% would be flagged as outliers by chance. The rule works well in practice, which is why it stuck — but there is no mathematical proof that 1.5 is "correct."

> [!tip] Interactive exploration
> Box plots can be explored interactively using Python/Jupyter — try `matplotlib.pyplot.boxplot()` or `seaborn.boxplot()` to generate box plots from data arrays. Compare with `seaborn.violinplot()` to see the full distribution shape. See [[Jupyter Notebooks]].

---

## Connections

- **Prerequisite:** [[Averages and Spread]] — the five-number summary ($Q_1$, median, $Q_3$, IQR) is defined here; box plots are the visual representation of these summary statistics
- **Prerequisite:** [[Cumulative Frequency]] — quartiles and percentiles are read from cumulative frequency curves, then used directly to draw box plots; this is the most common exam workflow
- **Prerequisite:** [[Classifying Data]] — box plots require quantitative data (discrete or continuous); understanding data types prevents misapplication
- **Complements:** [[Histograms]] — histograms show the shape of a distribution in detail (frequency density); box plots compress the same information into five numbers, sacrificing detail for easy comparison
- **Leads to:** [[Interpreting Data]] — box plots are a primary tool for comparing distributions and drawing inferences
- **Beyond syllabus:** connects to [[Scatter Diagrams]] — grouped box plots (one per category along the $x$-axis) combine categorical and quantitative data, similar to how scatter diagrams show bivariate quantitative data

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $Q_1$ | `Q_1` | Lower quartile |
| $Q_3$ | `Q_3` | Upper quartile |
| IQR | `\text{IQR}` | Interquartile range |
| $Q_3 - Q_1$ | `Q_3 - Q_1` | IQR formula |
| $Q_1 - 1.5 \times \text{IQR}$ | `Q_1 - 1.5 \times \text{IQR}` | Lower fence |
| $Q_3 + 1.5 \times \text{IQR}$ | `Q_3 + 1.5 \times \text{IQR}` | Upper fence |
| $\dfrac{n}{4}$ | `\dfrac{n}{4}` | Position for $Q_1$ on cf curve |
| $\dfrac{3n}{4}$ | `\dfrac{3n}{4}` | Position for $Q_3$ on cf curve |
| $\leq$ | `\leq` | Less than or equal to |
