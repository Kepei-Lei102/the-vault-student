---
chinese: 散点图 (sǎndiǎn tú)
prerequisites:
  - "[[Classifying Data]]"
  - "[[Statistical Charts]]"
  - "[[Averages and Spread]]"
leads_to:
  - "[[Cumulative Frequency]]"
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
  - syllabus/9260-S8
  - syllabus/0580-E9-5
  - type/concept
  - type/visual-tool
  - misconception/correlation-vs-causation
  - misconception/extrapolation-reliability
---

# Scatter Diagrams 散点图

## Definition

### Formal

A **scatter diagram** (also called a scatter plot or scatter graph) is a graph that shows the relationship between two variables by plotting data as points on a coordinate grid. Each point represents one individual or observation — its $x$-coordinate is the value of one variable, and its $y$-coordinate is the value of the other.

The pattern of the points reveals whether the variables are **correlated** — that is, whether a change in one variable is associated with a change in the other.

### Intuitive

Every other chart you've seen so far deals with **one variable at a time**: how many students like football, how heights are distributed, what the average test score is. A scatter diagram is different — it asks: **"Do these two things change together?"**

Plot one variable on each axis, mark a dot for each person (or item), and step back. If the cloud of dots slopes upward, the variables tend to increase together. If it slopes downward, one increases as the other decreases. If the dots look like someone sneezed on the page — there's no relationship.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| scatter diagram / scatter plot | 散点图 | sǎndiǎn tú |
| bivariate data | 二元数据 / 双变量数据 | èryuán shùjù / shuāng biànliàng shùjù |
| correlation | 相关性 | xiāngguān xìng |
| positive correlation | 正相关 | zhèng xiāngguān |
| negative correlation | 负相关 | fù xiāngguān |
| no correlation | 无相关 / 不相关 | wú xiāngguān / bù xiāngguān |
| line of best fit | 最佳拟合线 | zuìjiā nǐhé xiàn |
| interpolation | 内插法 | nèichā fǎ |
| extrapolation | 外推法 | wàituī fǎ |
| independent variable | 自变量 | zì biànliàng |
| dependent variable | 因变量 | yīn biànliàng |
| outlier | 异常值 / 离群值 | yìcháng zhí / líqún zhí |

> [!tip] 散点图 — the name tells you what it is
> 散 = scattered, 点 = dots/points, 图 = diagram. "A diagram of scattered dots." Compare with 正相关 (正 = positive) and 负相关 (负 = negative) — the Chinese terms are direct and transparent.

> [!tip] 二元 — why "two origins"?
> 二 = two, 元 = element / origin / fundamental unit. In Chinese maths, 元 means "unknown" or "variable" (it's the same 元 in 一元方程, a single-variable equation). So 二元数据 = "two-variable data." You'll meet 二元 again in 二元一次方程组 (system of linear equations in two unknowns). The alternative 双变量 (shuāng = pair/double, 变量 = variable) is more self-explanatory but less formal.

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $x$ | Independent variable — the one you control or choose first (horizontal axis) |
| $y$ | Dependent variable — the one you measure or observe (vertical axis) |
| $(\bar{x}, \bar{y})$ | The mean point — always lies on the line of best fit |
| $r$ | Correlation coefficient (beyond GCSE — see AP/IB section) |

---

## Key Facts / Properties

### Bivariate Data

**Bivariate data** consists of pairs of values $(x, y)$ collected from the same individual or observation. Examples:

- (hours studied, test score) for each student
- (temperature, ice cream sales) for each day
- (age of car, value of car) for each car

The **independent variable** (the one you think of as the "cause" or "input") goes on the $x$-axis. The **dependent variable** (the one you think of as the "effect" or "output") goes on the $y$-axis.

> [!info] Which axis?
> Ask: "Which variable do I choose or control?" That goes on the $x$-axis. "Which variable responds or is measured?" That goes on the $y$-axis. Temperature doesn't depend on ice cream sales — so temperature is $x$ and sales is $y$.

### Types of Correlation

| Type | Description | What the scatter looks like |
|------|-------------|----------------------------|
| **Positive correlation** | As $x$ increases, $y$ tends to increase | Dots slope upward (bottom-left to top-right) |
| **Negative correlation** | As $x$ increases, $y$ tends to decrease | Dots slope downward (top-left to bottom-right) |
| **No correlation** | No clear pattern between $x$ and $y$ | Dots scattered randomly — no visible trend |

![[scatter-correlation-types.svg|700]]

### Strength of Correlation

| Strength | What the scatter looks like |
|----------|-----------------------------|
| **Strong** | Points cluster tightly around an imaginary line |
| **Moderate** | Points follow a general trend but with noticeable spread |
| **Weak** | Points show a vague trend with lots of spread |

Describe correlation using **both** direction and strength: "strong positive correlation," "weak negative correlation," etc.

### Line of Best Fit (最佳拟合线)

A **line of best fit** is a straight line drawn through the data that best represents the overall trend. At GCSE level, this is drawn **by eye** (not calculated).

**Rules for drawing a line of best fit:**

1. The line should follow the **general direction** of the points
2. There should be roughly equal numbers of points **above and below** the line — this is the **primary check**. If you have 6 non-outlier points slightly above, you should have about 5–7 slightly below.
3. The line does **not** have to pass through the origin $(0, 0)$
4. The line does **not** have to pass through any of the data points
5. **Ignore outliers** when drawing the line — don't let one rogue point drag the line off course

> [!info] The mean point $(\bar{x}, \bar{y})$ as a guide
> Mathematically, the true line of best fit always passes through the mean point $(\bar{x}, \bar{y})$. Some textbooks and exams (particularly IB and AP) ask you to calculate and plot this point first, then draw your line through it. At **Cambridge GCSE/IGCSE level**, the mark scheme typically checks whether your line has roughly equal spread of points above and below — the mean point is not explicitly required. Still, calculating $(\bar{x}, \bar{y})$ and checking your line passes near it is a useful self-check: if your line misses the mean point by a lot, something is off.

### Using the Line of Best Fit

Once you have a line, you can use it to **estimate** values:

- **Interpolation** (内插法): estimating a value **within** the range of the data. This is reliable because you have data points nearby.
- **Extrapolation** (外推法): estimating a value **outside** the range of the data. This is unreliable because you're assuming the trend continues beyond where you have evidence.

**Example:** You collected data for temperatures between 15°C and 30°C. Using your line of best fit to estimate ice cream sales at 22°C is **interpolation** (reliable). Estimating sales at 40°C is **extrapolation** (unreliable — the relationship might change at extreme temperatures).

### Correlation ≠ Causation (相关≠因果)

This is one of the most important ideas in statistics.

**Correlation** means two variables change together. **Causation** means one variable *causes* the other to change. Correlation does not prove causation.

**Classic example:** Ice cream sales and drowning deaths are positively correlated. Does ice cream cause drowning? No — both increase because of a **hidden third variable** (温度/temperature: hot weather causes both more swimming and more ice cream eating). This hidden variable is called a **confounding variable** (混杂变量, hùnzá biànliàng) or **lurking variable**.

Other examples of correlation without causation:

- Shoe size and reading ability in children (confounding variable: age)
- Number of firefighters at a scene and damage caused (confounding variable: fire size)
- Per capita cheese consumption and number of people who die tangled in bedsheets (coincidence / spurious correlation)

> [!info] Beyond syllabus — the formal test
> At GCSE, you describe correlation informally ("strong positive"). At higher levels, the **Pearson correlation coefficient** $r$ gives a precise number from $-1$ to $+1$. See the AP/IB section below.

### Outliers

An **outlier** on a scatter diagram is a point that doesn't fit the general pattern — it lies far from the other points and far from the line of best fit.

When you spot an outlier:

1. **Don't remove it without reason** — it might be a genuine observation
2. **Don't let it distort your line of best fit** — draw the line ignoring the outlier
3. **Comment on it in exam answers** — state that there is an outlier and suggest a possible reason (measurement error, unusual circumstances, data entry mistake)

---

## Common Misconceptions

### 1. "Correlation means one thing causes the other"

"Ice cream sales and drowning are correlated, so ice cream must be dangerous." ✗

**Fix:** Correlation shows **association**, not causation. Always consider whether a third variable could explain the link. At GCSE, use phrases like "this suggests that..." or "there appears to be a relationship..." rather than "this proves that..."

### 2. "The line of best fit must go through the origin"

"The line starts at $(0, 0)$ because that's where the axes start." ✗

**Fix:** The line of best fit passes through $(\bar{x}, \bar{y})$, not necessarily through the origin. It only passes through the origin if the data genuinely suggests that when $x = 0$, $y = 0$ — which is not always the case. A car's age being 0 doesn't mean it has zero value.

### 3. "The line of best fit must touch every data point"

"I drew my line through all the points." ✗

**Fix:** The line represents the **overall trend**. Most points will be near the line, not on it. Trying to connect every point gives a jagged zigzag, not a trend line. Roughly equal points above and below is the goal.

### 4. "I can use the line to predict any value"

"My data covers ages 10–16, so I'll use it to predict the height of a 40-year-old." ✗

**Fix:** This is **extrapolation** — predicting beyond the range of your data. The relationship may not hold outside the observed range. Growth patterns at ages 10–16 do not continue unchanged to age 40. Only use the line for **interpolation** (within the data range), and flag any extrapolation as unreliable.

### 5. "No correlation means no relationship"

"The scatter shows no correlation, so there's no connection between these variables." ✗

**Fix:** No **linear** correlation means no straight-line relationship. The variables could still have a **non-linear** (curved) relationship. For example, the relationship between speed and fuel efficiency is often U-shaped — no linear correlation, but a strong curved one.

---

## Worked Examples

### Example 1: Drawing a scatter diagram and line of best fit

A teacher records the number of hours studied and the test score (%) for 8 students:

| Student | Hours ($x$) | Score ($y$) |
|---------|-------------|-------------|
| A | 2 | 35 |
| B | 5 | 60 |
| C | 3 | 45 |
| D | 7 | 75 |
| E | 1 | 25 |
| F | 6 | 70 |
| G | 4 | 55 |
| H | 8 | 80 |

**(a)** Plot the scatter diagram.

Hours studied is the independent variable ($x$-axis). Test score is the dependent variable ($y$-axis). Plot each pair as a point.

**(b)** Describe the correlation.

**Strong positive correlation** — as hours studied increases, test score tends to increase. The points cluster tightly around a line.

**(c)** Draw a line of best fit.

First, find the mean point:

$$\bar{x} = \dfrac{2 + 5 + 3 + 7 + 1 + 6 + 4 + 8}{8} = \dfrac{36}{8} = 4.5$$

$$\bar{y} = \dfrac{35 + 60 + 45 + 75 + 25 + 70 + 55 + 80}{8} = \dfrac{445}{8} = 55.625$$

Mark $(\bar{x}, \bar{y}) = (4.5, 55.6)$ on the diagram as a self-check. Draw a straight line following the trend, ensuring roughly equal points above and below the line, passing close to the mean point.

**(d)** Use your line to estimate the score of a student who studied for 4 hours.

Read up from $x = 4$ to the line, then across to the $y$-axis. Estimated score ≈ **50–52%**. This is interpolation (4 is within the range 1–8), so it is reliable.

**(e)** Would it be appropriate to use the line to predict the score of a student who studied for 20 hours?

**No** — this is extrapolation. The data only covers 1–8 hours, and the relationship is unlikely to continue unchanged (you can't score more than 100%, and there are diminishing returns to studying).

### Example 2: Interpreting correlation

A scatter diagram shows the age of cars (years) against their value (£). The points form a pattern sloping downward from left to right, with moderate spread.

**(a)** Describe the correlation.

**Moderate negative correlation** — as the age of a car increases, its value tends to decrease.

**(b)** One point represents a 15-year-old car worth £25,000 while most 15-year-old cars are worth under £3,000. Comment on this point.

This is an **outlier**. Possible reason: it could be a classic or rare car whose value increases with age — not following the typical depreciation pattern.

**(c)** A student says: "Getting older causes cars to lose value." Comment on this statement.

While the negative correlation supports this idea, **correlation does not prove causation**. It's more accurate to say that the features associated with age — higher mileage, more wear, older technology — tend to reduce value. Some old cars (classics, low-mileage) actually gain value.

---

## Exam Notes

### OxAQA 9260

- S8: construct and interpret scatter diagrams; identify correlation (positive, negative, none); draw a line of best fit by eye; use it for interpolation
- Typical question: given a table of bivariate data → plot the scatter → describe the correlation → draw a line of best fit → use the line to estimate a value → comment on reliability
- "Comment on reliability" = is it interpolation or extrapolation? Is the correlation strong enough to make a prediction useful?
- Mark scheme language: use "strong/moderate/weak" and "positive/negative/no" — both components needed for full marks
- Outliers: if asked about an unusual point, state it is an outlier and suggest a reason — don't just say "it doesn't fit"

### Cambridge 0580

- E9.5: understand and interpret scatter diagrams; draw a line of best fit; understand correlation (positive, negative, zero); distinguish between interpolation and extrapolation
- Paper 4 commonly provides a partial scatter diagram and asks you to complete it, draw the line, and make predictions
- Calculator paper: the mean point calculation is usually straightforward but check your arithmetic
- The word "trend" in a question means describe the correlation
- "Use your line to estimate..." means read a value from the line, not from the data points

### AP / IB / A-Level

- **AP Statistics:** the Pearson product-moment correlation coefficient $r$ quantifies linear correlation on a scale from $-1$ (perfect negative) through $0$ (none) to $+1$ (perfect positive):

$$r = \dfrac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \cdot \sum (y_i - \bar{y})^2}}$$

- $r^2$ (the **coefficient of determination**) tells you what percentage of the variation in $y$ is explained by the linear relationship with $x$. If $r = 0.9$, then $r^2 = 0.81$, meaning 81% of the variation in $y$ is explained by $x$.
- **Least-squares regression** (最小二乘法, zuìxiǎo èrchéng fǎ): the calculated line of best fit that minimises $\sum (y_i - \hat{y}_i)^2$ — the sum of squared vertical distances from points to the line. AP, IB HL, and A-Level all require students to find the regression line $y = ax + b$ by formula or calculator. The key exam skill is **interpreting** the gradient and $y$-intercept in context (e.g., "for each additional hour studied, the predicted score increases by 8 marks").
- **IB Mathematics AA HL / AI HL:** least-squares regression line calculated by formula or GDC; the mean point $(\bar{x}, \bar{y})$ **must** lie on the line (this is where it becomes an explicit exam requirement)
- **A-Level Statistics:** hypothesis testing for correlation using $r$ against critical values; Spearman's rank correlation for non-linear or ordinal data

### Beyond high school — University

- **Anscombe's quartet** (1973) is a famous set of four data sets that have identical summary statistics ($\bar{x}$, $\bar{y}$, $r$, regression line) but completely different scatter plots — one is linear, one is curved, one has an outlier, one is clustered. It demonstrates why you should **always plot the data** before fitting a model. The modern update is the **Datasaurus Dozen** (2017) — twelve data sets with identical statistics, one of which is shaped like a dinosaur.
- **Multiple regression and the normal equations:** the single-variable regression line generalises to many variables. The normal equations $X^T X \hat{\beta} = X^T y$ use linear algebra (matrix multiplication, projection onto subspaces) to find the best-fit plane/hyperplane. This is where statistics meets linear algebra and calculus.
- **Regression is the heart of machine learning.** When you fit a line of best fit, you are doing the simplest form of **regression** (回归, huíguī) — finding a model that predicts $y$ from $x$. Not all relationships are linear — some are quadratic, exponential, logarithmic, or something else entirely. Modern AI scales this up: neural networks are essentially regression with millions of parameters, fitting incredibly complex curves to data. The core idea is identical: minimise the distance between your predictions and the observed data.

![[regression-types.svg|700]]

- **Overfitting and underfitting** (过拟合 guò nǐhé / 欠拟合 qiàn nǐhé): an underfit model is too simple — like drawing a straight line through clearly curved data. An overfit model is too complex — like drawing a wiggly curve that passes through every single data point perfectly but fails on new data (it memorised the noise instead of learning the pattern). The art of machine learning is finding the right complexity in between. This connects back to the GCSE idea: your line of best fit should capture the trend, not chase every point.

![[overfit-underfit.svg|700]]
- **Correlation ≠ causation — and why this matters for AI.** Large language models (including the one helping build this vault) learn from vast amounts of data by finding statistical correlations — patterns like "these words tend to appear near those words." They are extraordinarily good at finding correlations, but they do **not** understand causation. They can tell you that umbrella sales and rain are correlated, but they cannot reason about *why* — they have no internal model of weather causing people to buy umbrellas. This is exactly why critical thinking remains essential when using AI: the model finds patterns, but **you** must judge whether those patterns reflect genuine causal relationships. The skill you're learning in this card — asking "is this correlation or causation?" — is the same skill you need when evaluating any AI output. (See also [[Probability Basics]] and [[Conditional Probability]] — the probability framework is the mathematical foundation underneath all of this.)

> [!tip] Interactive exploration
> Scatter diagrams and lines of best fit can be explored interactively using Python/Jupyter — try `matplotlib.pyplot.scatter()` and `numpy.polyfit()` to generate and fit your own data. See [[Jupyter Notebooks]].

---

## Connections

- **Prerequisite:** [[Classifying Data]] — scatter diagrams require quantitative bivariate data
- **Prerequisite:** [[Statistical Charts]] — scatter diagrams are a type of statistical chart for two-variable data
- **Prerequisite:** [[Averages and Spread]] — the mean point $(\bar{x}, \bar{y})$ anchors the line of best fit
- **Leads to:** [[Cumulative Frequency]] — another way to visualise and analyse continuous data
- **Related:** [[Set Theory/Venn Diagram]] — Venn diagrams show overlap between categories; scatter diagrams show the relationship between continuous variables
- **Beyond syllabus:** connects to [[Differentiation]] — the gradient of the line of best fit is related to the rate of change of $y$ with respect to $x$

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\bar{x}$ | `\bar{x}` | Mean of $x$ values |
| $\bar{y}$ | `\bar{y}` | Mean of $y$ values |
| $(\bar{x}, \bar{y})$ | `(\bar{x}, \bar{y})` | Mean point — always on the line of best fit |
| $r$ | `r` | Pearson correlation coefficient ($-1$ to $+1$) |
| $r^2$ | `r^2` | Coefficient of determination |
| $\hat{y}$ | `\hat{y}` | Predicted $y$ value from the line |
| $\sum$ | `\sum` | Summation — used in the formula for $r$ |
| $\dfrac{a}{b}$ | `\dfrac{a}{b}` | Display-style fraction |
