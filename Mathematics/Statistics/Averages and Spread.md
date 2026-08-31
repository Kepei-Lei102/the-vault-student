---
chinese: 平均数与离散程度 (píngjūnshù yǔ lísàn chéngdù)
prerequisites:
  - "[[Classifying Data]]"
  - "[[Greek Letters (Vocab)]]"
leads_to:
  - "[[Statistical Charts]]"
  - "[[Scatter Diagrams]]"
  - "[[Cumulative Frequency]]"
  - "[[Box Plots]]"
  - "[[Histograms]]"
  - "[[Interpreting Data]]"
  - "[[Normal Distribution]]"
  - "[[Non-Parametric Tests]]"
tags:
  - subject/mathematics
  - domain/statistics
  - level/GCSE
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/Edexcel-IAL
  - curriculum/OxAQA-9660
  - curriculum/AP-Statistics
  - curriculum/IB-AA
  - curriculum/IB-AI
  - syllabus/9260-S5
  - syllabus/0580-E9-3
  - syllabus/9709-5-1
  - type/concept
  - type/vocabulary
  - misconception/mean-vs-average
  - misconception/median-of-grouped-data
---

# Averages and Spread 平均数与离散程度

## Definition

### Formal

An **average** (measure of central tendency) is a single value that represents the "centre" or "typical value" of a data set. The three averages at GCSE level are:

- **Mean** ($\bar{x}$) — the sum of all values divided by the number of values
- **Median** — the middle value when all values are arranged in order
- **Mode** — the most frequently occurring value

A **measure of spread** describes how spread out the data is. The main measures are:

- **Range** — the difference between the highest and lowest values
- **Interquartile range (IQR)** — the range of the middle 50% of values

### Intuitive

Averages answer: **"What's a typical value?"** Spread answers: **"How much do the values vary?"**

Two data sets can have the same mean but look completely different. Test scores of {50, 50, 50} and {0, 50, 100} both average 50, but the first set has no variation and the second has huge variation. You need **both** an average and a measure of spread to describe data properly — one tells you *where* the data sits, the other tells you *how tightly* it clusters.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| average | 平均数 | píngjūnshù |
| mean | 平均值 / 算术平均数 | píngjūnzhí / suànshù píngjūnshù |
| median | 中位数 | zhōngwèishù |
| mode | 众数 | zhòngshù |
| range | 极差 / 全距 | jíchā / quánjù |
| interquartile range | 四分位距 | sìfēnwèi jù |
| quartile | 四分位数 | sìfēnwèishù |
| frequency | 频数 | pínshu |
| cumulative frequency | 累积频数 | lěijī pínshu |
| spread / dispersion | 离散程度 | lísàn chéngdù |
| outlier | 异常值 / 离群值 | yìcháng zhí / líqún zhí |

> [!tip] 中位数 — the name tells you what it is
> 中 = middle, 位 = position, 数 = number. The "middle-position number." Similarly, 众数 (众 = crowd/many) = "the number that appears most in the crowd." Chinese mathematical terminology is often more transparent than English.

> [!warning] 离散程度 vs 离散数据 — same character, different meaning
> 离散程度 (lísàn chéngdù, "degree of dispersion") is the standard Chinese textbook term for **spread**. But 离散 also appears in 离散数据 (lísàn shùjù, "discrete data") — see [[Classifying Data]]. Same characters, unrelated concepts: one describes how spread out data is, the other describes a type of data with gaps between values. The alternative term **分散程度** (fēnsàn chéngdù) avoids this collision and is also widely used. Be aware of both.

---

## Notation

| Symbol    | Meaning                                               |
| --------- | ----------------------------------------------------- |
| $\bar{x}$ | Mean of a data set (read "x bar")                     |
| $\sum x$  | Sum of all values                                     |
| $n$       | Number of data values                                 |
| $f$       | Frequency — how many times a value occurs             |
| $\sum fx$ | Sum of (frequency × value) — used in frequency tables |
| $\sum f$  | Total frequency — same as $n$                         |
| $Q_1$     | Lower quartile (25th percentile)                      |
| $Q_2$     | Median (50th percentile)                              |
| $Q_3$     | Upper quartile (75th percentile)                      |
| IQR       | Interquartile range: $Q_3 - Q_1$                      |

> [!info] Meeting $\sum$ for the first time
> If statistics is your first mathematics topic, $\sum$ (capital sigma) may be the first Greek letter you meet inside a formula. It stands for **S**um — the capital S of the Greek alphabet — and its lowercase partner $\sigma$ measures **s**pread. That pattern holds widely: capital Greek letters name operations, lowercase ones name quantities. The full alphabet, with pronunciations and the letter collisions to watch for, is in [[Greek Letters (Vocab)]].

---

## Key Facts / Properties

### Mean

$$\bar{x} = \dfrac{\sum x}{n}$$

The mean uses **every** value in the data set. This is both its strength (it captures all the information) and its weakness (extreme values pull it up or down).

**Example:** Scores: 3, 5, 7, 8, 12

$$\bar{x} = \dfrac{3 + 5 + 7 + 8 + 12}{5} = \dfrac{35}{5} = 7$$

> [!warning] The mean doesn't have to be a possible data value
> Five students score 3, 4, 5, 6, 7 on a test. The mean is 5 — a real score. But scores of 2, 3, 3, 4, 8 give a mean of 4 — fine. Scores of 1, 2, 4, 5 give a mean of 3 — also fine. But a die with results 1, 2, 3, 4, 5, 6 has a mean of 3.5 — and you can never roll 3.5. The mean is a mathematical construct, not necessarily a value that actually occurs.

#### Mean from a Frequency Table (Ungrouped)

When data is presented in a frequency table, use:

$$\bar{x} = \dfrac{\sum fx}{\sum f}$$

**Example:**

| Score ($x$) | Frequency ($f$) | $fx$ |
|-------------|----------------|------|
| 1 | 3 | 3 |
| 2 | 7 | 14 |
| 3 | 5 | 15 |
| 4 | 4 | 16 |
| 5 | 1 | 5 |
| **Total** | **20** | **53** |

$$\bar{x} = \dfrac{53}{20} = 2.65$$

#### Estimated Mean from a Grouped Frequency Table

When data is grouped, you don't know the exact values — only which interval they fall in. Use the **midpoint** of each class as the representative value.

$$\text{Estimated mean} = \dfrac{\sum f \times \text{midpoint}}{\sum f}$$

**Example:**

| Height $h$ (cm) | Frequency ($f$) | Midpoint ($m$) | $fm$ |
|-----------------|----------------|----------------|------|
| $140 \leq h < 150$ | 4 | 145 | 580 |
| $150 \leq h < 160$ | 9 | 155 | 1395 |
| $160 \leq h < 170$ | 12 | 165 | 1980 |
| $170 \leq h < 180$ | 5 | 175 | 875 |
| **Total** | **30** | | **4830** |

$$\text{Estimated mean} = \dfrac{4830}{30} = 161 \text{ cm}$$

> [!warning] Why "estimated"?
> You assumed every value in $150 \leq h < 160$ is at the midpoint 155. But they could be clustered near 150 or near 159 — you can't tell from grouped data. The midpoint assumption gives the best single estimate, but it's an **approximation**. This is why grouping data loses information — see [[Classifying Data#Grouped vs Ungrouped Data]].

#### Reverse Mean Problems

A common exam question gives you the mean and asks you to find a missing value.

**Strategy:** Use $\sum x = \bar{x} \times n$ to find the total, then solve.

**Example:** Five numbers have a mean of 8. Four of the numbers are 5, 7, 9, 11. Find the fifth.

$$\sum x = 8 \times 5 = 40$$

$$5 + 7 + 9 + 11 + x = 40$$

$$x = 40 - 32 = 8$$

#### Combined Mean

When two groups merge, the combined mean is:

$$\bar{x}_{\text{combined}} = \dfrac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2}$$

This is a **weighted** average — the larger group pulls the combined mean toward its own mean.

**Example:** Class A (20 students, mean 65) and Class B (30 students, mean 72):

$$\bar{x}_{\text{combined}} = \dfrac{20 \times 65 + 30 \times 72}{20 + 30} = \dfrac{1300 + 2160}{50} = \dfrac{3460}{50} = 69.2$$

> [!warning] The combined mean is NOT the mean of the two means
> $\dfrac{65 + 72}{2} = 68.5 \neq 69.2$. The combined mean is pulled toward 72 because Class B is **larger**. Taking the mean of the means only works when both groups have the **same** size.

### Median

The median is the **middle value** when data is arranged in ascending order.

For $n$ values arranged in order:

$$\text{Median position} = \dfrac{n + 1}{2}$$

- If $n$ is **odd**: the median is the single middle value
- If $n$ is **even**: the median is the mean of the two middle values

**Example (odd $n$):** 3, 5, 7, 8, 12 → $n = 5$, position $= \dfrac{6}{2} = 3\text{rd}$ → median $= 7$

**Example (even $n$):** 3, 5, 7, 8, 10, 12 → $n = 6$, positions $= 3\text{rd}$ and $4\text{th}$ → median $= \dfrac{7 + 8}{2} = 7.5$

#### Median from a Frequency Table

Use cumulative frequency to find which value sits at the $\dfrac{n+1}{2}$ position.

**Example:** Using the score table above ($n = 20$):

| Score | Frequency | Cumulative frequency |
|-------|-----------|---------------------|
| 1 | 3 | 3 |
| 2 | 7 | 10 |
| 3 | 5 | 15 |
| 4 | 4 | 19 |
| 5 | 1 | 20 |

Position $= \dfrac{21}{2} = 10.5\text{th}$, so the median is the mean of the 10th and 11th values.

The 10th value falls in the "2" row (cumulative frequency reaches 10). The 11th value falls in the "3" row (cumulative frequency reaches 15). So median $= \dfrac{2 + 3}{2} = 2.5$.

#### Median Class for Grouped Data

For grouped data, you can't find the exact median — only identify the **class interval** that contains it.

**Method:** Use $\dfrac{n}{2}$ (not $\dfrac{n+1}{2}$) for grouped data, then build a cumulative frequency column and find the class where the cumulative frequency first **exceeds** this value.

**Example:** Using the height table above ($n = 30$):

| Height $h$ (cm) | Frequency | Cumulative frequency |
|-----------------|-----------|---------------------|
| $140 \leq h < 150$ | 4 | 4 |
| $150 \leq h < 160$ | 9 | 13 |
| $160 \leq h < 170$ | 12 | 25 ← first to pass 15 |
| $170 \leq h < 180$ | 5 | 30 |

Step 1: $\dfrac{n}{2} = \dfrac{30}{2} = 15$

Step 2: Read down the cumulative frequency column — which class first reaches or exceeds 15?
- After $140 \leq h < 150$: cumulative frequency = 4 (not yet)
- After $150 \leq h < 160$: cumulative frequency = 13 (not yet)
- After $160 \leq h < 170$: cumulative frequency = 25 (passed 15!)

Step 3: The **median class** is $160 \leq h < 170$.

> [!warning] Why $\dfrac{n}{2}$ not $\dfrac{n+1}{2}$?
> For raw data, $\dfrac{n+1}{2}$ gives the exact position. For grouped data, we don't have exact positions — we're working with a continuous distribution approximation. Using $\dfrac{n}{2}$ is the convention for grouped/continuous data. For large $n$ the difference is negligible anyway.

### Mode

The mode is the value that occurs **most often**. It's the only average that:

- Can be used for **qualitative** (categorical) data — "the most common eye colour is brown"
- Can have **more than one** value — if two values tie, the data is **bimodal**
- Can have **no value** — if every value occurs once, there is no mode

For grouped data, the **modal class** is the class with the highest frequency. You cannot give an exact mode from grouped data.

> [!tip] When to use mode
> Mode is most useful when data is categorical (favourite colour, transport type) or when you want the single most popular option. For numerical data, the mean or median is usually more informative.

### Range

$$\text{Range} = \text{highest value} - \text{lowest value}$$

The range is simple to calculate but **highly sensitive to outliers** — one extreme value can make the range misleadingly large.

**Example:** Scores: 45, 48, 50, 52, 55 → range $= 55 - 45 = 10$

Add one outlier: 45, 48, 50, 52, 55, **98** → range $= 98 - 45 = 53$

One unusual value more than quintupled the range. This is why the range alone is a poor measure of spread.

### Interquartile Range (IQR)

$$\text{IQR} = Q_3 - Q_1$$

The IQR measures the spread of the **middle 50%** of the data, ignoring the top and bottom quarters. It is **resistant to outliers**.

There are **three common methods** for finding quartiles. They can give different answers on the same data — know which one your exam expects, and (the good news below) how forgiving the mark schemes actually are.

#### Method 1: Median of halves (Cambridge 0580, OxAQA 9260)

1. Find the median and split the data into a **lower half** and an **upper half**
2. $Q_1$ = median of the lower half
3. $Q_3$ = median of the upper half

If $n$ is odd, **exclude** the overall median from both halves.

**Example:** 2, 3, 5, 7, 8, 9, 11, 12, 15 ($n = 9$)

- Median (middle value) $= 8$ (the 5th value)
- Lower half: 2, 3, 5, 7 → $Q_1 = \dfrac{3 + 5}{2} = 4$
- Upper half: 9, 11, 12, 15 → $Q_3 = \dfrac{11 + 12}{2} = 11.5$
- IQR $= 11.5 - 4 = 7.5$

#### Method 2: Position formula (Cambridge 9709, for listed data)

$$Q_1 \text{ position} = \dfrac{n + 1}{4}, \qquad Q_3 \text{ position} = \dfrac{3(n + 1)}{4}$$

If the position is not a whole number, interpolate between the two nearest values. This is the convention 9709 mark schemes themselves compute with: a real Paper 5 stem-and-leaf question with $n = 15$ takes the lower quartile as the $4$th value and the upper as the $12$th — positions $\frac{16}{4}$ and $\frac{3 \times 16}{4}$.

**Same example:** $n = 9$

- $Q_1$ position $= \dfrac{10}{4} = 2.5\text{th}$ → halfway between 2nd (3) and 3rd (5) → $Q_1 = 4$ ✓
- $Q_3$ position $= \dfrac{30}{4} = 7.5\text{th}$ → halfway between 7th (11) and 8th (12) → $Q_3 = 11.5$ ✓

Here both methods agree. They don't always.

#### When the two methods disagree

**Example:** 1, 3, 5, 7, 9, 11 ($n = 6$)

**Method 1 (halves):**
- Median $= \dfrac{5 + 7}{2} = 6$
- Lower half: 1, 3, 5 → $Q_1 = 3$
- Upper half: 7, 9, 11 → $Q_3 = 9$
- IQR $= 9 - 3 = 6$

**Method 2 (formula):**
- $Q_1$ position $= \dfrac{7}{4} = 1.75\text{th}$ → $Q_1 = 1 + 0.75 \times (3 - 1) = 2.5$
- $Q_3$ position $= \dfrac{21}{4} = 5.25\text{th}$ → $Q_3 = 9 + 0.25 \times (11 - 9) = 9.5$
- IQR $= 9.5 - 2.5 = 7$

Different answers! The discrepancy is small for large data sets but noticeable for small ones.

#### Method 3: Linear interpolation in a grouped table (Edexcel IAL, OxAQA 9660)

When the data arrives **grouped** into classes, individual values are gone and both methods above are unusable. The Edexcel-family convention: quartile positions are $\dfrac{n}{4}$ and $\dfrac{3n}{4}$ (**no** $+1$), and you interpolate *within* the class that holds that position, assuming the values spread evenly through it:

$$Q_1 = L + \frac{\frac{n}{4} - F}{f} \times w \qquad \begin{array}{l} L = \text{lower boundary of the class holding the position} \\ F = \text{cumulative frequency before the class} \\ f, w = \text{the class's frequency and width} \end{array}$$

Straight from a real S1 mark scheme ($n = 80$, so the position is $20$; the class $4.5$–$6.5$ holds it, with $15$ values before and $9$ inside): $Q_1 = 4.5 + \frac{20 - 15}{9} \times 2 = 5.61$. The method mark is for the **interpolation expression itself** — writing it is the skill being examined — and the scheme *condones* the $\frac{n+1}{4}$ variant (it accepts $5.66$, the position-$20.25$ answer, as well).

> [!warning] Which method does your exam use — checked against the papers, not the syllabus
> **Cambridge 0580 / OxAQA 9260:** taught and marked as Method 1 (halves). And the schemes are deliberately forgiving: a real 0580 Paper 2 scheme accepts "$6.5$ **or** $6.75$ **or** $7$" for one lower quartile — one value per convention. Use halves; you cannot lose the mark to a convention.
>
> **Cambridge 9709:** Method 2 on listed/stem-leaf data — but the schemes print an *acceptance band* (one real question allows any $79 \leqslant Q_1 \leqslant 82$), inside which the halves answer also lands. Grouped data goes through the [[Cumulative Frequency|cumulative frequency curve]], reading at $\frac{n}{4}$, $\frac{n}{2}$, $\frac{3n}{4}$.
>
> **Edexcel IAL / OxAQA 9660 (S1):** Method 3 is *required* for grouped tables — the interpolation expression is the method mark. For listed data, values from the list ("cao" — no tolerance). These are also the boards that love $Q_3 - Q_2$ vs $Q_2 - Q_1$ as a **skewness** test, so quartiles feed the next part.
>
> **Calculators and software:** the fx-991's 1-variable stats and the TI-84 both return halves-method quartiles; Excel, Python and R interpolate instead — R alone offers **9 quantile algorithms**. Thirty-second verification, in the spirit of trusting nothing: key in $1, 3, 5, 7, 9, 11$. If your machine says $Q_1 = 3$, it thinks in halves; if $2.5$, it interpolates. For large $n$ every method converges — the fuss is only ever about small data.

### Skewed Data

Data is **skewed** when it is not symmetrical — most values cluster on one side, with a long "tail" stretching out to the other.

- **Positively skewed** (right-skewed): the tail stretches toward **high** values. Most data is low, with a few very high values pulling the mean up. Example: income data — most people earn moderate amounts, a few earn millions.
- **Negatively skewed** (left-skewed): the tail stretches toward **low** values. Most data is high, with a few very low values pulling the mean down. Example: exam scores on an easy test — most students score well, a few score very low.
- **Symmetrical**: data is evenly distributed around the centre. The mean and median are approximately equal.

For skewed data: **mean gets pulled toward the tail**, but **median stays near the centre**. This is why the median is the better average for skewed distributions.

> [!tip] Quick check for skew
> If mean > median → likely **positive skew** (tail on the right).
> If mean < median → likely **negative skew** (tail on the left).
> If mean ≈ median → likely **symmetrical**.

### Which Average and Spread to Use

| Situation | Best average | Why |
|-----------|-------------|-----|
| Symmetrical numerical data, no outliers | **Mean** | Uses all values; most informative |
| Skewed data or outliers present | **Median** | Not pulled toward the tail like the mean |
| Categorical (qualitative) data | **Mode** | Only average that works for categories |
| "Most popular" or "most common" | **Mode** | Directly answers the question |
| Need to use every data point | **Mean** | Only average that uses all values |

| Situation | Best spread | Why |
|-----------|------------|-----|
| Quick comparison, no outliers | **Range** | Simple to calculate |
| Outliers present, or comparing distributions | **IQR** | Ignores extreme values |

> [!info] Beyond syllabus — The effect of outliers, visualised
> Imagine a village of 100 people with an average income of £30,000. A billionaire moves in. The **mean** income jumps to roughly £10,000,000 — completely unrepresentative. The **median** barely changes, maybe from £30,000 to £30,100. The **mode** doesn't change at all. This is why news reports about "average income" should always specify *which* average — and why economists usually prefer the median for income data.

> [!info] Beyond syllabus — Weighted mean in real life
> Your school report doesn't just average all your marks equally — some components are worth more than others. If coursework is worth 30% and the exam is worth 70%, a coursework score of 80 and an exam score of 60 gives:
>
> $$\text{Weighted mean} = \dfrac{0.3 \times 80 + 0.7 \times 60}{0.3 + 0.7} = \dfrac{24 + 42}{1} = 66$$
>
> Not $\dfrac{80 + 60}{2} = 70$. The exam pulls the result down because it carries more weight. This is exactly the same principle as the combined mean formula — each group's contribution is proportional to its size (or weight).

---

## Common Misconceptions

### 1. "Average means mean"

"Find the average" — student immediately calculates the mean. ✗

**Fix:** "Average" is a general term that includes mean, median, and mode. In everyday English, "average" usually implies the mean, but in an exam, **read the question carefully** — it will specify which average. If it says "the average," it usually means mean, but if it says "an appropriate average," you need to choose and justify.

### 2. Forgetting to order data before finding the median

"The data is 7, 3, 9, 1, 5. The middle value is 9." ✗

**Fix:** The median requires data in **ascending order** first: 1, 3, 5, 7, 9. The median is 5, not 9. This is the single most common error with medians — and the easiest to avoid.

### 3. Confusing the median position with the median value

"There are 20 values, so the median position is $\dfrac{21}{2} = 10.5$. The median is 10.5." ✗

**Fix:** 10.5 tells you **where** to look (between the 10th and 11th values), not **what** the median is. You still need to find the 10th and 11th values and average them.

### 4. Using the midpoint as the exact answer for grouped data

"The estimated mean is 161 cm, so the average student is exactly 161 cm tall." ✗

**Fix:** The estimated mean from grouped data is an **approximation**. The word "estimated" is not optional — write it. The real mean could be higher or lower depending on how values are distributed within each class. Exam markers look for the word "estimated" in your answer.

### 5. "The range tells you about the spread of all the data"

"The range is 53, so the data is very spread out." ✗ (misleading)

**Fix:** The range only looks at **two values** — the highest and lowest. It tells you nothing about how the data is distributed between them. A range of 53 could mean the data is evenly spread, or it could mean 99% of the data is clustered together with one outlier pulling the range wide. The IQR is a much better measure of the typical spread.

### 6. Combined mean = mean of the means

"Class A has mean 65 and Class B has mean 72, so the combined mean is $\dfrac{65+72}{2} = 68.5$." ✗

**Fix:** This only works if both classes have the **same number** of students. If they don't, the larger class has more influence. Use $\bar{x}_{\text{combined}} = \dfrac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2}$.

---

## Worked Examples

### Example 1: Mean, median, mode, range from raw data

Data: 4, 7, 2, 8, 7, 5, 3, 7, 9, 1

**(a) Mean:**

$$\bar{x} = \dfrac{4 + 7 + 2 + 8 + 7 + 5 + 3 + 7 + 9 + 1}{10} = \dfrac{53}{10} = 5.3$$

**(b) Median:** First, order: 1, 2, 3, 4, 5, 7, 7, 7, 8, 9

$n = 10$ → position $= \dfrac{11}{2} = 5.5\text{th}$ → median $= \dfrac{5 + 7}{2} = 6$

**(c) Mode:** 7 appears 3 times (most frequent) → mode $= 7$

**(d) Range:** $9 - 1 = 8$

### Example 2: Estimated mean from grouped data

| Time $t$ (minutes) | Frequency | Midpoint | $f \times m$ |
|-------------------|-----------|----------|-------------|
| $0 \leq t < 10$ | 5 | 5 | 25 |
| $10 \leq t < 20$ | 12 | 15 | 180 |
| $20 \leq t < 30$ | 18 | 25 | 450 |
| $30 \leq t < 40$ | 10 | 35 | 350 |
| $40 \leq t < 60$ | 5 | 50 | 250 |
| **Total** | **50** | | **1255** |

$$\text{Estimated mean} = \dfrac{1255}{50} = 25.1 \text{ minutes}$$

**Modal class:** $20 \leq t < 30$ (highest frequency: 18)

**Median class:** $\dfrac{50}{2} = 25\text{th}$ value. Cumulative frequencies: 5, 17, 35, … The 25th value falls in $20 \leq t < 30$.

> [!warning] Unequal class widths
> The last class ($40 \leq t < 60$) has width 20, while the others have width 10. The modal class is still identified by the highest **frequency**, but if you're drawing a histogram, you need **frequency density** — see [[Histograms]]. For the estimated mean, unequal widths don't change the calculation — you still use midpoints.

### Example 3: Reverse mean problem

The mean of 12 numbers is 7.5. When one number is removed, the mean of the remaining 11 numbers is 7.

**(a)** Find the number that was removed.

$$\text{Original total} = 12 \times 7.5 = 90$$

$$\text{New total} = 11 \times 7 = 77$$

$$\text{Removed number} = 90 - 77 = 13$$

**(b)** Was the removed number above or below the original mean? → **Above** (13 > 7.5), which is why the mean decreased when it was removed.

### Example 4: Choosing the best average

A company has 20 employees with the following annual salaries:

- 17 employees earn £25,000
- 2 employees earn £45,000
- 1 employee (the director) earns £150,000

Mean: $\dfrac{17 \times 25{,}000 + 2 \times 45{,}000 + 1 \times 150{,}000}{20} = \dfrac{665{,}000}{20} = £33{,}250$

Median: the 10th and 11th values are both £25,000, so median $= £25{,}000$

Mode: £25,000 (17 out of 20 employees)

The mean (£33,250) is misleadingly high — 17 out of 20 employees earn less than it. The **median** (£25,000) or **mode** (£25,000) better represents the "typical" salary. The director's salary is an **outlier** that pulls the mean upward.

---

## Exam Notes

### OxAQA 9260

- S5: calculate and interpret the mean, median, mode, and range for a set of data; find the modal class and calculate an estimated mean for grouped data
- Reverse mean problems are common — "the mean of $n$ numbers is $k$, find the missing value"
- Combined mean problems: merging two groups — use $\dfrac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2}$
- "Compare two distributions" questions expect TWO comparisons: one average AND one measure of spread, with context. Example: "On average, Class A scored higher (mean 65 vs 58) but with less consistency (IQR 12 vs 20)"
- S6/S7 (interpreting data): expect questions where you read values from tables, then calculate averages — combine with this card

### Cambridge 0580

- E9.3: calculate the mean, median, mode, and range for individual and discrete frequency distributions; calculate an estimate of the mean for grouped frequency distributions; identify the modal class
- Paper 2 (non-calculator): simpler data, exact arithmetic. Paper 4 (calculator): larger data sets, grouped frequency tables
- "State the type of average you have calculated and give a reason for your choice" — this justification is worth marks

### Cambridge 9709 — Paper 5 (Probability & Statistics 1), §5.1

*"Understand and use different measures of central tendency (mean, median, mode) and variation (range, interquartile range, standard deviation)"* — *"e.g. in comparing and contrasting sets of data"*. Expect a stem-and-leaf, box plot or cumulative-frequency graph first ([[Histograms]], [[Box Plots]], [[Cumulative Frequency]]) and then the measures read or calculated from it; the standard deviation is from $\sqrt{\dfrac{\sum x^2}{n} - \bar x^2}$ (the $n$ form, not $n-1$), often with the totals $\sum x$ and $\sum x^2$ given or coded ($\sum(x - a)$, $\sum(x-a)^2$). The comparison sentence wants one average **and** one spread, in context, as for 9260.

### Edexcel IAL — Statistics 1, §2.2–2.4

Mean, median and mode from lists and frequency tables (§2.2); range, interpercentile ranges, variance and standard deviation, including **coding** $y = \dfrac{x - a}{b}$ and the un-coding of $\bar y$ and $s_y$ (§2.3); skewness read from the relative positions of mean, median and mode or from a box plot, and outliers by whatever rule the question states (§2.4). IAL uses the same $n$-denominator standard deviation as 9709.

### OxAQA 9660 — Statistics 1, §S1.2

Measures of centre and spread — mean, median, mode, range, interquartile range, variance and standard deviation — from raw and grouped data, with the same comparison-sentence expectation.

### AP Statistics / IB

- **The variance and standard deviation, for all of the above:** the **variance** ($\sigma^2$ or $s^2$) is the mean of the squared deviations from the mean — spread in squared units; the **standard deviation** is its square root, back in the data's units. Population form $\sigma = \sqrt{\dfrac{\sum(x - \bar{x})^2}{n}} = \sqrt{\dfrac{\sum x^2}{n} - \bar{x}^2}$; the **sample** form divides by $n - 1$ (Bessel's correction — the reason is the seesaw of [[t-Tests]]: the deviations are measured from a mean that was itself fitted to the data).
- **AP Statistics** (Unit 1): the five-number summary (min, $Q_1$, median, $Q_3$, max) for box plots; outliers by the $1.5 \times \text{IQR}$ rule; the population / sample distinction ($\mu, \sigma$ vs $\bar x, s$) with the $n-1$ sample standard deviation throughout.
- **IB AA and AI** (SL 4.3): measures of central tendency and dispersion from lists and frequency tables, the effect of constant changes on them, and — especially in AI — choosing the *appropriate* average for a context.

### Beyond high school — University

- The mean is the value that minimises the sum of **squared** deviations: $\bar{x} = \arg\min_c \sum(x_i - c)^2$. The median minimises the sum of **absolute** deviations: $\text{median} = \arg\min_c \sum \lvert x_i - c \rvert$. This deep connection to **optimisation** is why the mean is sensitive to outliers (squaring amplifies large deviations) and the median is not.
- Other means exist: the **geometric mean** ($\sqrt[n]{x_1 \cdot x_2 \cdots x_n}$) is used for growth rates and ratios; the **harmonic mean** ($\dfrac{n}{\sum \dfrac{1}{x_i}}$) is used for rates and speeds. The arithmetic mean $\geq$ geometric mean $\geq$ harmonic mean — this is the **AM-GM-HM inequality**, a fundamental result in analysis.
- **Robust statistics** formally studies estimators that resist the influence of outliers. The median is a simple example; the **trimmed mean** (discard the top and bottom $k\%$, then average) is another.

---

## Connections

- **Prerequisite:** [[Classifying Data]] — the type of data determines which averages are valid (mean for quantitative, mode for qualitative)
- **Leads to:** [[Statistical Charts]] — charts visualise what averages summarise; bar chart heights relate to mode, line of best fit relates to mean
- **Leads to:** [[Cumulative Frequency]] — reading $Q_1$, $Q_2$, $Q_3$ from cumulative frequency curves is the standard method for large data sets
- **Leads to:** [[Box Plots]] — the five-number summary (min, $Q_1$, median, $Q_3$, max) is directly built from concepts in this card
- **Leads to:** [[Scatter Diagrams]] — the mean point $(\bar{x}, \bar{y})$ always lies on the line of best fit
- **Application:** [[Relative and Expected Frequency]] — expected frequency uses probability as a kind of theoretical mean
- **Foundation:** [[Probability Basics]] — expected value in probability is a weighted mean of outcomes
- **Story:** [[You Never Expect the Change of Needs]] — mean vs spread decided by speedrunners: a constant input delay can be practised away, but jitter never can, so "smoother" is a low-variance verdict — this card's central distinction, wearing a game controller

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\bar{x}$ | `\bar{x}` | Mean |
| $\sum x$ | `\sum x` | Sum of values |
| $\sum fx$ | `\sum fx` | Sum of frequency × value |
| $\sum f$ | `\sum f` | Total frequency |
| $\dfrac{\sum fx}{\sum f}$ | `\dfrac{\sum fx}{\sum f}` | Mean from frequency table |
| $Q_1, Q_2, Q_3$ | `Q_1, Q_2, Q_3` | Quartiles |
| $\dfrac{n+1}{2}$ | `\dfrac{n+1}{2}` | Median position |
| $\sigma$ | `\sigma` | Standard deviation (population) |
| $\sigma^2$ | `\sigma^2` | Variance (population) |
| $\lvert x_i - c \rvert$ | `\lvert x_i - c \rvert` | Absolute deviation |
