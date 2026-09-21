---
chinese: 实验数据的记录与处理 (shíyàn shùjù de jìlù yǔ chǔlǐ)
aliases:
  - Reading Scales
  - Best-Fit Line
  - Gradient from a Graph
  - Results Tables
prerequisites:
  - "[[Planning an Experiment]]"
  - "[[Significant Figures]]"
  - "[[Repeated Measurements]]"
  - "[[Calibration of Instruments]]"
leads_to:
  - "[[Linearisation]]"
tags:
  - subject/physics
  - domain/measurement
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - syllabus/0625-P4
  - syllabus/0625-P5
  - type/deep
  - misconception/join-the-dots
  - misconception/line-must-pass-through-origin
  - misconception/small-gradient-triangle
  - misconception/parallax-is-an-explanation
---

# Recording and Analysing Experimental Data 实验数据的记录与处理

> *In 1662 Robert Boyle published a table. He had trapped air in the short arm of a J-shaped glass tube, poured mercury into the long arm, and written down, for twenty-five settings, how much space the air took up and how much mercury was pressing on it. Beside the measured pressures he added one more column: "What the pressure should be according to the Hypothesis". Anyone could run an eye down the two columns and see that they agreed to within the little he could not measure. It is among the first published tables of experimental data, and everything done with a table since is in it: headed columns, a calculated column beside the measured ones, and a judgement about whether two sets of numbers agree.*

## Definition

### Formal

To **record** data is to write each observation down as it is made, to the precision the instrument gives and no more, with its quantity and unit, in a table planned before the experiment begins. To **analyse** data is to turn the table into a conclusion: process the numbers, plot a graph with a **best-fit line**, read from the line its **gradient** and **intercept** (or values by **interpolation** and **extrapolation**), identify **anomalous** results, and decide whether two results agree **within the limits of experimental accuracy**.

### Intuitive

Every reading is a little wrong, and you cannot know which way. A table keeps the readings honest, by showing what was actually seen. A graph lets them vote: a line drawn through many points is pulled up by some and down by others, their errors largely cancel, and one reading that is badly wrong stands out from the rest where you can deal with it.

### 中文锚点

每天早上称一次体重，数字总在跳：今天 52.3，明天 51.8，后天又是 52.6。只看其中一天，根本说不清自己是胖了还是瘦了，因为每个读数都带着一点说不准的偏差：喝没喝水，秤放得平不平，眼睛是不是正对着指针。可是把一个月的数字一个点一个点画在方格纸上，再用尺子画一条从这片点中间穿过去的直线，让点子在线的上下两边差不多一样多，情况就清楚了：偏高的和偏低的互相抵消，那条线比任何一个点都可靠，体重的变化趋势就看这条线的斜率。哪天要是称出 58.0，它会孤零零地远离那条线，一眼就能看出这个读数有问题，应该回头检查，而不是让它把整条线拽歪。单个读数会骗你，很多读数排成的一条线却很难骗你：这就是要把数据记成表格、再画成图的原因。

### 术语对照 (Terms)

最小分度 smallest division · 估读到半格 read to the nearest half division · 视差 parallax · 视线垂直于刻度 line of sight perpendicular to the scale · 凹液面（弯月面） meniscus · 零点误差 zero error · 表头 column heading · 最佳拟合线 best-fit line · 斜率 gradient · 截距 intercept · 内插 interpolation · 外推 extrapolation · 异常值 anomalous result · 在实验误差范围内相等 equal within the limits of experimental accuracy

---

## Part I — Taking a reading

**Read to half a division.** Find the value of the smallest division of the scale. If the pointer or edge sits on a mark, read the mark. If it sits between two marks, decide whether it is nearer a mark or nearer the middle, and record it **to the nearest half division**.

![[experimental-data-reading-scales.svg|860]]

Half a division is the finest judgement the eye makes reliably, and it is worth making: reading to the nearest whole division leaves a typical rounding error of 0.29 of a division, and reading to the nearest half brings that down to 0.14.

**Write down what the instrument can resolve, every time.** A ruler marked in millimetres and read to half a millimetre gives lengths to 0.05 cm, so a reading exactly on the 4.7 cm mark is written **4.70 cm**. The final zero is information: it says you looked and the half was not there. For the same reason all the readings in one column have the same number of decimal places. A digital meter has done the judging for you: copy every digit it shows, including a final zero.

**Look from straight in front.** If the pointer stands a little way in front of its scale and your eye is off to one side, the pointer appears against the wrong mark. This is **parallax error**. With a pointer 2 mm from the scale and the eye 15 cm off line at a reading distance of 30 cm, the reading moves by a whole millimetre; for the thread of a thermometer, 4 mm behind the front of the glass, by two. The cure is always the same sentence: **keep the line of sight perpendicular to the scale** (at eye level with the reading). Better, remove the gap: lay a ruler so that its scale touches the object, or use a meter with a mirror behind the pointer and line the pointer up with its own reflection.

**Special cases worth knowing.**
- **Liquid in a measuring cylinder** curves up at the glass. Read the level of the **bottom of the meniscus**, with your eye level with it.
- **Zero error.** Before measuring, check what the instrument reads when it should read zero. A balance showing 0.3 g when empty, or a ruler with a worn end, adds the same amount to every reading; subtract it, or start the measurement from the 1.0 cm mark and subtract 1.0 cm. [[Calibration of Instruments]] explains why repeating can never reveal this kind of error.
- **Short times and small lengths.** Measure many and divide: time 20 oscillations, measure the thickness of 50 sheets. The hand-and-eye error is shared between them, as [[Planning an Experiment]] shows with numbers.
- **Readings from a diagram.** When a drawing is labelled "one-quarter full size", measure the drawing with your ruler and multiply by four.

---

## Part II — The table

Draw the table **before** the first reading, so that every number has a place to go the moment it exists. The conventions are few and they are marked:

| $m$ / g | $t$ for 20 oscillations / s | $T$ / s |
|---|---|---|
| 100 | 8.06 | 0.403 |
| 200 | 11.32 | 0.566 |
| 300 | 13.84 | 0.692 |

- **Each heading is a quantity and its unit, separated by a solidus**: $t$ / s, $l$ / cm. The heading means "the quantity divided by the unit", which is why the entries below it are pure numbers.
- **No units in the body of the table.**
- **The independent variable goes in the first column**, the measured quantities next, calculated quantities last.
- **Raw readings are recorded, including the repeats**, not just their mean. A table that shows only processed values hides the evidence.
- **Measured values**: decimal places fixed by the instrument, the same down the whole column. **Calculated values**: the same number of significant figures as the least precise raw value used ([[Significant Figures]]). Above, 8.06 s has three, so $T$ has three.
- Qualitative observations ("the lamp is dimmer", "the image is blurred") are recorded in words, at the time.

---

## Part III — Drawing the graph

The column headings go straight onto the axes. Then there are six decisions, in this order.

1. **Which way round.** The independent variable (the one you chose) along the $x$-axis, the dependent variable up the $y$-axis, unless the question says otherwise. "Plot $l$ against $m$" means $l$ on the $y$-axis.
2. **Labels.** Quantity and unit on each axis, exactly as in the table: $m$ / g.
3. **Scales.** The plotted points should spread over **more than half the grid in both directions**, and one large (2 cm) square should stand for **1, 2 or 5** units, or those times a power of ten. Never 3, 4, 7 or 9: with those every point needs a division sum to place and another to read. Scales must be linear, with no breaks. Start at the origin if the question says so or if you need the intercept; otherwise starting elsewhere is allowed and often uses the grid better.
4. **Points.** A small, sharp **cross** (× or +) or a dot in a circle, placed to within **half a small square**. A blob hides its own position.
5. **The best-fit line.** One **thin, straight line drawn with a ruler** (or one smooth curve, freehand, if the points clearly curve), placed by eye so that the points are **balanced on either side along its whole length**. It does not have to pass through any point, and it does not have to pass through the origin. Use a transparent ruler so that you can see the points on both sides. Extend the line across the range you will need.
6. **Anything odd.** A point clearly off the trend is dealt with before the line is drawn: Part V.

![[experimental-data-good-and-bad-graph.svg|860]]

Both graphs above show the same five readings of the length of a spring. The lower one is what the first three marks of a graph question are given for: sensible scales that fill the grid, points plotted accurately, a thin well-judged line.

**Never join the dots.** Each point is wrong by a little, in an unknown direction. A zig-zag through them claims that every wobble is real physics. The straight line claims that the physics is simple and the wobbles are measurement, which is nearly always the truth, and it is the line, not the points, that you then measure.

---

## Part IV — Reading the graph

### Gradient

$$\text{gradient} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

Choose two points **on the line** (not data points, unless they happen to lie on it), **far apart**: the triangle's hypotenuse should cover **more than half of the line you drew**. Draw the triangle on the graph and write the read-off values beside it; showing how the gradient was found is itself a mark. Read each coordinate to half a small square. Give the answer to two or three significant figures, with its unit, which is the $y$-unit divided by the $x$-unit.

![[experimental-data-manim.mp4]]
*A ruler line is swung and slid until the five points balance about it. The gradient is then read nine times from a small triangle and nine times from a large one, with the same half-square reading errors each time: the small triangle's answers spread over 21 %, the large triangle's over 2 %.*

Why large? Every read-off is uncertain by about half a small square. That fixed uncertainty is divided by the base of the triangle, so a base four and a half times longer gives a gradient four and a half times more certain:

![[experimental-data-triangle-size.svg|820]]

| Triangle | Gradient / cm g⁻¹ | Spread |
|---|---|---|
| between two neighbouring points, base 100 g | 0.0409 ± 0.0014 | 3.4 % |
| over most of the line, base 450 g | 0.0409 ± 0.0003 | 0.8 % |

### Intercept

The **intercept** is where the line crosses an axis, read off to half a small square, extending the line (**extrapolating**) if necessary. The $y$-intercept is only at the left-hand edge if the $x$-axis starts at zero. Intercepts mean something. In the spring graph the line meets $m = 0$ at $l = 1.9$ cm: the length of the spring with nothing hanging on it. Forcing that line through the origin "because no load means no length" would change the gradient by 13 %, and no spring has zero length.

A straight line is $y = mx + c$: **linear**. Only a straight line **through the origin** shows that $y$ is **directly proportional** to $x$. The spring's *length* is linear in the load; its *extension* is proportional to it.

### Interpolation and extrapolation

Reading a value from the line **between** measured points is **interpolation**, and it is trustworthy: the line is supported on both sides. Reading **beyond** the measured range is **extrapolation**, and it assumes that the pattern continues. It often does not: a spring stretched past its limit of proportionality, a wire that heats up, a cooling curve that flattens out at room temperature.

---

## Part V — Judging the results

### Anomalous results

An **anomalous** result is one that does not fit the pattern of the others: a repeat far from its fellows, or a plotted point far from a line that the rest sit on. The procedure is: **identify it** (circle it), **check it** (misread scale? digits swapped? wrong mass on the hanger?), **repeat that measurement** if you can, and if it cannot be explained or repeated, **leave it out** of the mean or the best-fit line **and say that you have**. Never delete it from the table: the record stays complete.

![[experimental-data-anomaly.svg|820]]

Here the 400 g length has been misread by 3 cm. Ignored, the gradient is 0.0409 cm/g, the true value. If the line is dragged towards it, the gradient becomes 0.0379, an error of 7 % caused by one reading.

One caution. A result is anomalous because it disagrees with the *other data*, not because it disagrees with what you expected. Discarding readings for the second reason is how wrong theories survive.

### Do two results agree?

Two values of the same quantity, obtained by different methods, never come out identical. At this level they are taken to be **equal within the limits of experimental accuracy if they are within 10 % of each other**:

$$\text{percentage difference} = \frac{\text{difference between the two values}}{\text{one of the values}} \times 100\,\%.$$

The answer needs both halves: **the calculation, and then a statement that matches it.** Using either value as the denominator is accepted; if the result is close to 10 %, say so.

### Conclusions

A conclusion is a statement about the relationship, **justified by the data**. "The graph is a straight line through the origin, so $V$ is directly proportional to $l$" is justified by the shape of the line. "When the mass doubles from 200 g to 400 g the extension doubles from 8.1 cm to 16.4 cm" quotes values from the table. "$l$ increases as $m$ increases" is true of nearly everything and earns little.

---

## Where it is the working tool

**Every measured constant in physics is a gradient.** The spring constant, the resistance of a wire, the acceleration of free fall, the Hubble constant in [[Hubble's Law and the Expanding Universe]]: each is the slope of a best-fit line through scattered points, because a slope uses all the data at once and is untouched by any error that shifts every reading equally. A zero error moves the whole line up and leaves its gradient alone, which is one more reason to take the gradient and not the ratio of one pair of readings.

**The ozone hole was missed because of an automatic anomaly rule.** In the early 1980s the software processing a NASA satellite's ozone measurements flagged values below a set limit as probable instrument errors. The extremely low springtime readings over Antarctica were flagged and set aside, year after year. Joseph Farman's team, reading a ground instrument by hand at Halley Bay since 1957, published the hole in 1985; the satellite data, re-examined, had contained it all along. An anomaly is a question to be answered, and the answer is sometimes that the world has changed.

**Calibration curves.** A hospital laboratory measuring glucose, or a factory checking the thickness of paint, measures several known samples first, plots reading against true value, draws the best-fit line, and then reads every unknown off that line by **interpolation**. Reporting a result from beyond the ends of the calibration line is forbidden, for the reason given under extrapolation.

**Computer fitting is the same idea made exact.** A spreadsheet's trendline chooses the straight line that makes the sum of the squares of the vertical distances from the points as small as possible (least squares), which is a precise version of "balanced on either side". For the spring data it gives 0.0409 cm/g, and a careful line drawn by eye gives the same to two significant figures.

---

## Hands-on

**A spring you own.** Hang a rubber band or a slinky from a door handle, add identical coins one at a time in a small bag, and measure the length each time with a ruler held against it, eye level with the bottom of the bag. Table first, then a graph on squared paper with every rule in Part III. Is it straight? (A rubber band is not, and the curve is real physics.) Find the gradient with a small triangle and again with a large one.

**See parallax.** Hold a pencil upright 3 cm in front of a ruler fixed to the wall. Read where the pencil's edge falls from straight ahead, then with your head 20 cm to the left, then 20 cm to the right. Then touch the pencil to the ruler and repeat.

**Run the numbers.** `python3 experimental-data-lab.py` reproduces every figure here. Move the anomalous point to the middle of the range and find out why the gradient then barely changes; shrink the gradient triangle and watch the spread grow.

---

## Worked examples — every tool named

### Example 1 — one question, the whole chain (Cambridge 0625, June 2024 Paper 62, Q1)

*A student finds the spring constant of a spring by two methods. **Method 1:** a 500 g mass oscillates on the spring; the stop-watch shows 17.76 s for 20 oscillations. (a) Record $t$ and calculate the period $T$. (b) Suggest how the procedure can be improved. (c) Calculate $k_1 = 19.7/T^2$. **Method 2:** the stretched length $l$ is measured for five masses. For 500 g, a drawing at one-quarter full size shows a length $L$ between two dotted lines. (d) Measure $L$ and find $l$. The other readings are $m$ / g = 400, 300, 200, 100 with $l$ / cm = 18.3, 14.3, 10.0, 6.1. (e) Plot $l$ against $m$, starting both axes at the origin; draw the best-fit line; find the gradient $G$, showing on the graph the values used; calculate $k_2 = 1/G$. (f) Two quantities can be considered equal within the limits of experimental accuracy if they are within 10 % of each other. State whether $k_1$ and $k_2$ can be considered equal, supporting your statement with a calculation. [13]*

**(a)** *Trigger: a digital display. Tool: copy every digit; many-and-divide.* $t = 17.76$ s, so $T = 17.76/20 = 0.888$ s.

**(b)** Time a greater number of oscillations (the reaction-time error is then shared among more of them), or repeat and average.

**(c)** $k_1 = 19.7/0.888^2 = 25.0$ N/m.

**(d)** *Trigger: "one-quarter full size".* The drawing measures $L = 5.6$ cm, so $l = 4 \times 5.6 = 22.4$ cm, recorded to the same 0.1 cm as the rest of the column.

**(e)** *Tools: Part III for the three graph marks, Part IV for the gradient.* Axes labelled $m$ / g and $l$ / cm; 100 g and 5 cm to a large square, which on a grid six squares by five spreads the points over two-thirds of each axis; five crosses; one thin straight line, which passes through none of the points exactly and meets the $l$-axis at 1.9 cm. With a triangle from $m = 50$ g to $m = 500$ g, drawn on the graph:
$$G = \frac{22.4 - 4.0}{500 - 50} = \frac{18.4}{450} = 0.0409\ \text{cm/g}, \qquad k_2 = \frac{1}{G} = 24.4.$$
The published scheme accepts $k_2$ from 23.5 to 26.4, and gives the gradient mark for "any indication on the graph as to how the gradient was found" together with a correct $\Delta y/\Delta x$. A candidate who forces the line through the origin gets $G = 0.046$ and $k_2 = 21.6$, outside the range.

**(f)** *Tool: the 10 % test, calculation first.* Difference $= 25.0 - 24.4 = 0.6$; $0.6/25.0 \times 100 = 2.4\,\%$. This is less than 10 %, so the two values can be considered equal within the limits of experimental accuracy. One mark is for a calculation that uses both values, the other for a statement that matches it.

### Example 2 — which reading is anomalous, and why? (Cambridge 0625, June 2026 Paper 63, Q3(d))

*A student takes repeat readings of the current for three resistors in parallel: 0.85 A, 0.58 A, 0.90 A, 0.80 A. Identify the anomalous reading and suggest one reason for the anomaly. [2]*

*Trigger: three values close together and one far away.* **0.58 A.** A reason must be something that could actually produce that number: the digits were written down the wrong way round (0.85 recorded as 0.58); or one resistor had come disconnected, so only two were in parallel and the current was smaller. "The ammeter was misread" is not accepted, being a restatement and not a cause. With 0.58 left out the mean is 0.85 A; with it included, 0.78 A.

### Example 3 — why is the scale viewed perpendicularly? (the marking point that recurs across Papers 5 and 6)

*Describe one precaution you would take to obtain an accurate reading of the volume of water in a measuring cylinder / the temperature on a thermometer / the position of a pointer on a scale.*

*Trigger: "precaution" with a scale and a gap.* **View the scale perpendicularly (line of sight at right angles to the scale, eye level with the reading)**; for a liquid, **read the bottom of the meniscus**. The schemes state "ignore descriptions of parallax": writing "to avoid parallax error" names the problem and does not describe an action. The mark is for what you do with your eye.

### Example 4 — choosing scales (constructed)

*Temperatures between 18.5 °C and 29.0 °C are to be plotted on an axis six large squares long. Choose the scale.*

*Trigger: a range that does not start near zero. Tool: the 1–2–5 rule first, then the half-grid rule.* Try starting at zero: the axis must reach 29, so 5 °C per square, and the data then cover $10.5/30 = 35\,\%$ of the axis, which fails. Nothing requires the origin here, so start at **18 °C with 2 °C per large square**: the axis runs from 18 to 30, the data cover $10.5/12 = 88\,\%$ of it, and each small square is 0.2 °C, which makes 18.5 and 29.0 easy to place. A scale of 2.5 °C per square would also fit, and is not allowed: the rule about 1, 2 and 5 comes first because it controls plotting errors, and the grid is then used as well as that rule permits.

### Example 5 — a borderline 10 % (constructed)

*Two methods give the density of a block as 2.61 g/cm³ and 2.90 g/cm³. Do they agree?*

$0.29/2.90 = 10.0\,\%$; $0.29/2.61 = 11.1\,\%$. The two ways of calculating straddle the boundary. State the calculation used and the conclusion that matches it, and add the honest remark: the values are at the limit of agreement, so the method with the larger uncertainty (usually the volume, found from three lengths) should be repeated more carefully before anything is claimed.

---

## Common Misconceptions (Teaching Notes)

### 1. "Join the points"
A dot-to-dot line treats every measurement error as a fact about nature. One straight line (or one smooth curve) through the scatter is the claim that the physics is simple and the readings are imperfect.

### 2. "The line must go through the origin" (or "through the first and last points")
Only if the data say so. The spring's line meets the axis at its unstretched length. The first and last points are no more reliable than the others, and using them alone throws away the rest.

### 3. "Any two points will do for the gradient"
Two points close together magnify the read-off error: 3.4 % against 0.8 % for the same line. Two *data* points that are not on the line give the gradient of a different line.

### 4. "To avoid parallax error"
That is a reason, not a precaution. The precaution is "line of sight perpendicular to the scale".

### 5. "4.7 cm and 4.70 cm are the same"
As numbers, yes. As records, the second says the scale was read to half a millimetre and the first does not.

### 6. "An anomalous result is one that disagrees with the theory"
It is one that disagrees with the rest of the data. It must be recorded, investigated, and its exclusion stated.

---

## Exam Notes

### Cambridge 0625 (IGCSE) — practical skills, Paper 5 (Practical Test) and Paper 6 (Alternative to Practical)

The syllabus's "Presentation of data" section fixes the conventions used above, and mark schemes follow it closely. **Readings:** to half of the smallest division; decimal places and unit reflecting the instrument. **Tables:** heading as quantity / unit with the solidus, no units in the body, repeats recorded, calculated values to the least number of significant figures in the raw data. **Graphs:** axes labelled quantity / unit; scales using more than half the grid in both directions and based on 1, 2 or 5 units (or 10, 20, 50) to 2 cm; points as +, × or ⊙, plotted to half a small square; best-fit line "a single, thin, smooth, straight line or curve, drawn by inspection", with "a roughly even distribution of points either side of the line over its entire length", ignoring points identified as anomalous. **Gradient:** a triangle whose hypotenuse extends over **at least half the length of the line**, marked on the graph; two or three significant figures; units consistent with the axes. **Intercepts and read-offs:** to half a small square. **Agreement:** ±10 %. A typical graph part carries three marks for the graph (scales; plots; line) and one for the gradient method. Extended candidates may also be asked for the gradient of a curve by drawing a tangent.

### Cambridge 9702 (A Level) — Paper 3 and Paper 5

The same conventions, tightened. Column headings with quantity and unit in accepted form ($I$ / mA); raw readings to the same precision; points occupying **at least half the grid in both directions**; no awkward scales; the gradient triangle's hypotenuse **more than half the length of the drawn line**, with read-offs to half a small square. In addition, 9702 requires **uncertainties**: half the range of repeated readings as the absolute uncertainty, percentage uncertainties, and on Paper 5 error bars with a worst acceptable line. Those are taught in [[Repeated Measurements]] and [[Error Propagation]], and the straightening of curved relationships in [[Linearisation]].

### IB Physics and AP Physics

**IB Physics** (first assessment 2025) assesses these skills through the scientific investigation and in Paper 1B data-analysis questions: tables with units and uncertainties, best-fit lines, gradients and intercepts with their uncertainties from maximum and minimum lines. **AP Physics 1, 2 and C** experimental-design questions ask which quantities to graph to obtain a straight line and how to find the unknown from its slope. Neither uses the ±10 % convention, which is specific to Cambridge IGCSE.

---

## Connections

- **Builds on:** [[Planning an Experiment]] — the chain from question to conclusion, of which this is the last three links; [[Significant Figures]] — how many digits a reading has earned; [[Repeated Measurements]] — means, spread and what repeating can and cannot fix; [[Calibration of Instruments]] — zero error and its correction.
- **Extends into:** [[Linearisation]] — choosing what to plot so that a curve becomes a straight line; [[Error Propagation]] — how the uncertainty in a gradient carries through a calculation; [[Accuracy vs Precision]] — random against systematic error, and which of them a graph can expose.
- **Mathematics:** [[Gradient (Vocab)]] — rise over run; [[Equation of a Straight Line (Vocab)]] — $y = mx + c$; [[Scatter Diagrams]] — the statistician's line of best fit, through the mean point; [[Direct and Inverse Proportion (Vocab)]] — why only a line through the origin means "proportional".
- **Where gradients earn their keep:** [[Hooke's Law for Springs]], [[Resistance]], [[Hubble's Law and the Expanding Universe]], [[Specific Heat Capacity]] (the initial-gradient method).

---

## Beyond Syllabus

### What "balanced on either side" means exactly
Recall that the best-fit line is judged by eye. The standard exact version, **least squares**, chooses the gradient $m$ and intercept $c$ that minimise $\sum (y_i - mx_i - c)^2$, the total of the squared vertical misses. Setting the derivatives to zero gives two results worth knowing: the line always passes through the **mean point** $(\bar x, \bar y)$, and its gradient is $\sum (x_i-\bar x)(y_i - \bar y)\big/\sum (x_i - \bar x)^2$. The second formula shows why points at the **ends** of the range control the gradient (their $x_i - \bar x$ is large) while a point in the middle barely affects it, which is the answer to the question in "Run the numbers".

### The uncertainty in a gradient
At A Level and beyond, each point carries an **error bar**, and two more lines are drawn: the steepest and the shallowest that still pass through all the bars. Half the difference between their gradients is the uncertainty in the gradient. A point whose bar the best-fit line misses is the formal definition of anomalous.

### Why squared paper at all?
A graph is a calculating machine that works by eye. Human vision is extremely good at judging whether points lie on a straight line and very poor at seeing the same thing in a column of numbers. That is why so much effort goes into finding what to plot so that the expected law comes out straight, the subject of [[Linearisation]].

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $\dfrac{\Delta y}{\Delta x}$ | `\dfrac{\Delta y}{\Delta x}` | gradient from a triangle on the line |
| $y = mx + c$ | `y = mx + c` | straight line: gradient $m$, intercept $c$ |
| $T = t/N$ | `T = t/N` | period from the time for $N$ oscillations |
| $\dfrac{\lvert a - b\rvert}{a}\times100\,\%$ | `\dfrac{\lvert a - b\rvert}{a}\times100\,\%` | percentage difference for the 10 % test |
| $\sum (y_i - mx_i - c)^2$ | `\sum (y_i - mx_i - c)^2` | what least squares makes as small as possible |
