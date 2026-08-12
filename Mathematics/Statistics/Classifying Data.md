---
chinese: 数据分类 (shùjù fēnlèi)
prerequisites:
  - "[[Relative and Expected Frequency]]"
leads_to:
  - "[[Averages and Spread]]"
  - "[[Statistical Charts]]"
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
  - syllabus/9260-S1
  - syllabus/9260-S3
  - syllabus/0580-E9-1
  - type/definition
  - type/vocabulary
  - misconception/discrete-vs-continuous
  - misconception/qualitative-vs-quantitative
---

# Classifying Data 数据分类

## Definition

### Formal

**Data** is information collected through observation, measurement, or experiment. Data can be classified along two independent axes:

1. **By nature:** qualitative (categorical) vs quantitative (numerical)
2. **By type of number:** discrete vs continuous (applies to quantitative data only)

A third classification — **primary vs secondary** — describes how the data was obtained, not what the data looks like.

### Intuitive

Before you can draw a chart, calculate an average, or spot a trend, you need to know **what kind of data you have** — because the type of data determines which tools are appropriate.

Think of it as sorting your toolbox before building something. You wouldn't use a hammer on a screw. Similarly, you wouldn't draw a histogram for shoe sizes or calculate a mean for favourite colours.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| data | 数据 | shùjù |
| qualitative data | 定性数据 | dìngxìng shùjù |
| quantitative data | 定量数据 | dìngliàng shùjù |
| discrete data | 离散数据 | lísàn shùjù |
| continuous data | 连续数据 | liánxù shùjù |
| primary data | 原始数据 / 一手数据 | yuánshǐ shùjù / yīshǒu shùjù |
| secondary data | 二手数据 | èrshǒu shùjù |
| categorical | 分类的 | fēnlèi de |
| numerical | 数值的 | shùzhí de |
| variable | 变量 | biànliàng |
| frequency | 频率 / 频数 | pínlǜ / pínshu |

> [!tip] 离散 vs 连续 — the Chinese is more transparent than the English
> 离散 literally means "separated / scattered" — values are spread apart with gaps. 连续 means "continuous / unbroken" — values flow without gaps. If the Chinese makes more sense to you, use it as your anchor.

---

## Notation

| Symbol / Term | Meaning |
|---------------|---------|
| Variable | A quantity that can change — what you're measuring or observing |
| Value | A specific data point — one observation |
| Frequency | How many times a particular value occurs |
| Class / Class interval | A range used to group continuous data (e.g., $10 \leq x < 20$) |
| Tally | A counting method using groups of 5 (four vertical strokes crossed by a diagonal) |
| $[a, b]$ | **Closed interval** — includes both endpoints: $a \leq x \leq b$ |
| $[a, b)$ | **Half-open interval** — includes $a$, excludes $b$: $a \leq x < b$ |
| $(a, b)$ | **Open interval** — excludes both endpoints: $a < x < b$ |

---

## Key Facts / Properties

### The Classification Tree

```
                        Data
                ┌────────┴────────┐
          Qualitative        Quantitative
          (categorical)       (numerical)
                             ┌─────┴─────┐
                          Discrete    Continuous
```

Every piece of data falls into exactly one leaf of this tree. The first question is always: **can you do arithmetic with it?**

### Qualitative (Categorical) Data

Data that describes a **quality or category** — not a number you can do arithmetic with.

| Example | Values | Why qualitative |
|---------|--------|----------------|
| Eye colour | brown, blue, green, hazel | No ordering, no arithmetic |
| Favourite subject | maths, physics, English | Categories, not numbers |
| Blood type | A, B, AB, O | Labels, not measurements |
| Transport to school | walk, bus, car, cycle | Categories |
| Grade | A*, A, B, C, D, E | Ordered categories, but you can't calculate "A + B" |

> [!warning] Numbers that are really categories
> **Shirt size** (S, M, L, XL) — ordered categories, not numbers.
> **Football shirt number** — the number 10 isn't "twice as much" as 5. It's a label.
> **Postcode / zip code** — digits that name a place, not a quantity.
> **Phone number** — adding two phone numbers gives nonsense.
>
> The test: **does arithmetic make sense?** If not, the data is qualitative even if it looks like numbers.

### Quantitative (Numerical) Data

Data that is **measured or counted** as a number — arithmetic makes sense.

Quantitative data splits further into **discrete** and **continuous**.

#### Discrete Data

Values that can only take **specific, separated values** — usually whole numbers from counting.

| Example | Possible values | Why discrete |
|---------|----------------|-------------|
| Number of students | 0, 1, 2, 3, … | You can't have 2.7 students |
| Shoe size (UK) | 3, 3.5, 4, 4.5, … | Fixed steps of 0.5 — no size 4.3 |
| Number of pets | 0, 1, 2, 3, … | Counting whole animals |
| Dice score | 1, 2, 3, 4, 5, 6 | Finite list of exact values |
| Goals scored | 0, 1, 2, 3, … | No half-goals |

> [!tip] The gap test
> Between any two consecutive discrete values, there are **no possible values**. Between 2 pets and 3 pets, there is nothing. Between shoe size 5 and 5.5, there is no valid size.

#### Continuous Data

Values that can take **any value within a range** — including all decimals.

| Example | Why continuous |
|---------|--------------|
| Height (cm) | Could be 170, 170.3, 170.31, 170.314… — no gaps |
| Mass (kg) | Any positive real number |
| Time (seconds) | Can be measured to any precision |
| Temperature (°C) | Can take any value on the number line |
| Distance (km) | Any non-negative real number |

> [!tip] The zoom test
> If you zoom in between any two continuous values, you can always find another value between them. Between 170.3 cm and 170.4 cm, there's 170.35. Between 170.35 and 170.36, there's 170.355. The gaps never appear — this is the mathematical property of **density** of the real numbers.

> [!info] Beyond syllabus — Is the universe discrete or continuous?
> Mathematics treats height, time, and distance as continuous — any real number is possible. But physics tells a different story. At the smallest scales, energy comes in **quanta** (discrete packets). Planck's constant ($h \approx 6.626 \times 10^{-34}$ J·s) sets a fundamental granularity: below a certain scale, the universe itself appears to be discrete. Whether space and time are truly continuous or just appear so at our scale is still an open question in physics.
>
> **Computer science faces the same problem from the other direction.** Computers are inherently discrete — everything is stored as bits (0s and 1s). So how do they handle continuous data?
>
> - **Images:** a camera samples continuous light into a grid of pixels. Each pixel's colour is stored with a fixed **bit depth** — 8-bit colour gives $2^8 = 256$ levels per channel, 16-bit gives $2^{16} = 65{,}536$. More bits = finer gradations = closer to "continuous," but never truly continuous.
> - **Audio:** a microphone captures continuous sound waves, but the computer **samples** them at a fixed rate (e.g., 44,100 samples per second for CD quality). Each sample is rounded to the nearest value the bit depth allows. Higher sample rate + higher bit depth = more faithful reproduction.
>
> The difference between the true continuous value and the nearest discrete value the computer can store is called the **quantisation error** (量化误差, liànghuà wùchā). This is "arbitrarily close" in action: with enough bits and enough samples, the quantisation error becomes negligibly small — the discrete approximation becomes indistinguishable from the continuous original — but it never actually *becomes* continuous. The gap between discrete and continuous is fundamental, and every digital device you use is a compromise across it.

> [!info] Beyond syllabus — Continuous data is always rounded
> When we write "height = 170.3 cm," what we really mean is "height is between 170.25 cm and 170.35 cm." Every measurement of continuous data is an approximation — limited by the measuring instrument. The true value has infinitely many decimal places. This connects to [[Power Rule#Upper and lower bounds|upper and lower bounds]] in the Number topic.

### Primary vs Secondary Data

This classification is about **how you got the data**, not what it looks like.

| | Primary data | Secondary data |
|---|---|---|
| **Collected by** | You (first-hand) | Someone else (second-hand) |
| **Method** | Surveys, experiments, observations | Books, websites, databases, government records |
| **Control** | You choose what to collect and how | You use what's available |
| **Timeliness** | Current — collected for your specific purpose | May be outdated or collected for a different purpose |
| **Cost** | Usually more expensive and time-consuming | Usually cheaper and faster |
| **Reliability** | You know the methodology | You must trust the source |

**Examples:**
- You survey your class about screen time → **primary**
- You look up average screen time from a government report → **secondary**
- A scientist measures river pollution levels → **primary** (for that scientist)
- You use that scientist's data in your geography project → **secondary** (for you)

> [!warning] The same data can be both
> Data is primary or secondary **relative to the person using it**. The scientist who collected the river data calls it primary. The student who downloads it calls it secondary.

> [!info] Beyond syllabus — Secondary data and hidden bias
> Secondary data is convenient, but it comes with risks you don't face with primary data:
>
> - **Selection bias:** the original collector chose *what* to measure and *who* to include. A survey of "internet users" excludes people without internet — which skews results for questions about the general population.
> - **Measurement bias:** the original collector chose *how* to measure. If a country defines "unemployment" differently from another country, comparing their unemployment data is misleading.
> - **Publication bias:** data that supports interesting conclusions is more likely to be published. Studies finding "no effect" often stay in desk drawers — so the secondary data you can find overrepresents dramatic results.
> - **Outdated context:** a 2015 survey about smartphone usage tells you about 2015, not today.
>
> The critical habit: **always ask "who collected this, why, and how?"** before trusting secondary data. That includes this very article you're reading right now — who is the author, why did they write it, how did they gather their information? This is the foundation of **source evaluation** — a skill that matters far beyond statistics exams.

### Grouped vs Ungrouped Data

When there are many different values, data is often organised into **groups** (also called **classes** or **class intervals**).

| Ungrouped | Grouped |
|-----------|---------|
| Individual values listed | Values collected into intervals |
| Used when there are few distinct values | Used when data is spread over a wide range |
| Exact values known | Exact values lost — only the interval is known |

**Grouped continuous data** uses inequality notation:

$$10 \leq h < 20$$

This means: $h$ is at least 10 but strictly less than 20. A value of exactly 20 goes in the **next** group.

The **class width** is $20 - 10 = 10$.

> [!warning] Where does the boundary value go?
> With $10 \leq h < 20$ and $20 \leq h < 30$: a measurement of exactly 20 goes in the **second** group. The $<$ sign on the right means "up to but not including." Always check which side has $\leq$ and which has $<$.
>
> The notation $[a, b)$ is called a **half-open** (or **half-closed**) interval: the square bracket $[$ means **closed** (endpoint included), the round bracket $)$ means **open** (endpoint excluded). So $[10, 20)$ is another way of writing $10 \leq h < 20$.
>
> **Why $\leq$ on the left and $<$ on the right?** This convention ensures every value lands in exactly one group — no overlaps, no gaps. It's the same reason programming languages and mathematical indexing use **half-open ranges**: Python's `range(10, 20)` gives 10 through 19; array slicing `a[0:n]` gives indices 0 through $n-1$. The pattern $a \leq x < b$ is everywhere because it tiles perfectly: $[10, 20)$ then $[20, 30)$ then $[30, 40)$ — the end of one interval is the start of the next, with no ambiguity. See [[Upper and Lower Bounds]] for the full treatment of boundary conventions and error intervals.

---

## Common Misconceptions

### 1. "If it has numbers, it's quantitative"

"Shirt numbers in football are quantitative because they're numbers." ✗

**Fix:** The test is not "does it look like a number?" but "does arithmetic make sense?" Player number 7 + player number 10 ≠ player number 17. Shirt numbers are **labels** — qualitative data. The same applies to phone numbers, postcodes, bus routes, and ID numbers.

### 2. "Discrete means whole numbers only"

"Shoe sizes can be 5.5, so shoe size must be continuous." ✗

**Fix:** Discrete means **separated values with gaps between them** — not necessarily integers. Shoe sizes go 5, 5.5, 6, 6.5, … — there is no shoe size 5.3 or 5.7. The values are fixed and countable, with gaps between consecutive values. That's discrete.

### 3. "Continuous means it has decimals"

"The answer was 3.7, so it must be continuous data." ✗

**Fix:** Discrete data can have decimal values (shoe sizes). Continuous data might be rounded to whole numbers (height recorded as 170 cm). The question is not "does it have decimals?" but **"could the value theoretically be any number in a range?"** Height could be 170.000001 cm — it's continuous. Shoe size cannot be 5.000001 — it's discrete.

### 4. "Money is continuous because it has decimals"

"Prices are continuous — £4.99 has decimals." ✗

**Fix:** This one is genuinely debatable, and examiners aren't always consistent. In practice, money comes in fixed denominations (pence/cents), so it's **discrete** — you can't pay £4.993. But the underlying quantity it represents (value, purchasing power) is continuous. **For GCSE exams:** treat money as **discrete** unless the question explicitly says otherwise.

### 5. "Age is discrete because we say 'I'm 15'"

"Age is always a whole number, so it's discrete." ✗

**Fix:** We **report** age in whole numbers by convention, but age itself changes continuously — right now you are 15 years, 7 months, 3 days, 4 hours, 12 minutes and some seconds old. Age is **continuous data that we conventionally round down**. Time flows without gaps.

### 6. Confusing qualitative with "bad data"

"Qualitative data isn't as good as quantitative data." ✗

**Fix:** Different, not worse. Qualitative data answers different questions — "What categories exist?" vs "How much?" You can't calculate a mean eye colour, but you can find the **mode** (most common category). Each type of data has appropriate analysis tools.

---

## Worked Examples

### Example 1: Classify each variable

| Variable | Qualitative or Quantitative? | If quantitative: Discrete or Continuous? |
|----------|------------------------------|------------------------------------------|
| Number of books in a bag | Quantitative | Discrete — count whole books |
| Colour of car | Qualitative | — |
| Time to run 100 m | Quantitative | Continuous — any positive time value |
| Number of text messages sent | Quantitative | Discrete — count whole messages |
| Temperature of a drink | Quantitative | Continuous — any value on thermometer |
| Favourite food | Qualitative | — |
| Mass of a bag of rice | Quantitative | Continuous — any positive mass |
| Score on a test (out of 40) | Quantitative | Discrete — 0, 1, 2, …, 40 |

### Example 2: Identify the type of data collection

A student is investigating how far students in her school travel to get to school.

(a) She gives a questionnaire to all Year 10 students. → **Primary** — she collected it herself.

(b) She looks up the average distance students travel to school from a government website. → **Secondary** — collected by someone else.

(c) Is "distance to school" discrete or continuous? → **Continuous** — distance can be any positive value (3.2 km, 3.27 km, etc.).

(d) She groups the data into classes: $0 \leq d < 2$, $2 \leq d < 4$, $4 \leq d < 6$, etc. What is the class width? → $2$ km.

### Example 3: The tricky cases

Classify each as discrete or continuous:

| Variable | Answer | Reasoning |
|----------|--------|-----------|
| Number of goals in a match | Discrete | Counted; no half-goals |
| Speed of a car | Continuous | Could be any value — 60.0, 60.1, 60.12… |
| UK shoe size | Discrete | Fixed values: 3, 3.5, 4, 4.5, … (has decimals but still discrete!) |
| Amount of rainfall (mm) | Continuous | Any non-negative value |
| Number of rainy days | Discrete | Counted; whole days |
| Salary (£) | Discrete | Paid in pence — £34,521.47 but not £34,521.473 |

---

## Exam Notes

### OxAQA 9260

- S1: classify and interpret data in various forms — qualitative, quantitative, discrete, continuous
- This is foundational vocabulary that appears **throughout** the statistics section — every chart, average, and diagram question implicitly requires knowing what type of data you're working with
- Typical question: "State whether this data is discrete or continuous. Explain your answer."
- The explanation matters — a correct classification with no reasoning may not get full marks

### Cambridge 0580

- E9.1: classify and tabulate data
- Often tested through frequency tables and choosing the right chart: "Why would a bar chart be suitable for this data?" requires knowing it's categorical/discrete
- Frequency tables for grouped continuous data: know the notation $a \leq x < b$

### AP / IB / A-Level

- **AP Statistics:** data types are foundational — categorical vs quantitative determines which inferential tests are appropriate (chi-squared for categorical, t-tests for quantitative); levels of measurement (nominal, ordinal, interval, ratio) add further precision
- **IB Mathematics AA/AI:** data classification in the Statistics & Probability topic; AI SL emphasises real-world data interpretation, so knowing data types is essential for choosing the right analysis
- **A-Level Statistics (S1):** classification of variables; sampling methods (random, stratified, systematic, cluster, quota) are tested in detail — primary vs secondary data connects to sampling methodology

### Beyond high school — University

- The four **levels of measurement** (Stevens' typology, 1946) refine our two-way split: **nominal** (categories, no order — eye colour), **ordinal** (categories with order — grades), **interval** (equal spacing, no true zero — temperature in °C), **ratio** (equal spacing, true zero — mass, height). Most GCSE "qualitative" maps to nominal/ordinal; "quantitative" maps to interval/ratio.
- The discrete/continuous distinction becomes mathematically precise in measure theory: discrete random variables have **countable** support (possibly infinite — the natural numbers are countable); continuous random variables have **uncountable** support and are described by probability density functions rather than probability mass functions.

---

## Connections

- **Leads to:** [[Averages and Spread]] — the type of data determines which averages are meaningful (mean for quantitative, mode for qualitative)
- **Leads to:** [[Statistical Charts]] — the type of data determines which chart to use (bar chart for discrete/categorical, histogram for continuous)
- **Leads to:** [[Scatter Diagrams]] — both variables must be quantitative and continuous (or at least treated as such)
- **Leads to:** [[Histograms]] — specifically for grouped continuous data with unequal class widths
- **Leads to:** [[Cumulative Frequency]] — requires continuous grouped data
- **Data collection:** [[Relative and Expected Frequency]] — relative frequency tables are one way to summarise experimental data
- **Grouping:** grouped data and class intervals connect to [[Histograms]] and [[Cumulative Frequency]]
- **Foundation:** the classification of data into types parallels how [[Set|sets]] classify objects into groups — both are about organising information by shared properties

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\leq$ | `\leq` | "Less than or equal to" — closed endpoint |
| $<$ | `<` | "Strictly less than" — open endpoint |
| $10 \leq x < 20$ | `10 \leq x < 20` | Half-open class interval |
| $[a, b)$ | `[a, b)` | Half-open interval notation |
| $[a, b]$ | `[a, b]` | Closed interval notation |
| $(a, b)$ | `(a, b)` | Open interval notation |
| $2^8 = 256$ | `2^8 = 256` | Bit depth levels |
| $h \approx 6.626 \times 10^{-34}$ | `h \approx 6.626 \times 10^{-34}` | Planck's constant |
