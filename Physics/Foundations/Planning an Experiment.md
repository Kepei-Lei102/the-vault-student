---
chinese: 实验设计 (shíyàn shèjì)
prerequisites:
  - "[[Accuracy vs Precision]]"
  - "[[Repeated Measurements]]"
  - "[[Calibration of Instruments]]"
  - "[[Significant Figures]]"
  - "[[Physical Quantities and Units]]"
leads_to:
  - "[[Linearisation]]"
  - "[[Sound]]"
  - "[[Recording and Analysing Experimental Data]]"
tags:
  - subject/physics
  - domain/experimental-physics
  - domain/measurement
  - domain/foundations
  - level/IGCSE
  - level/A-Level
  - level/IB
  - level/AP
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - curriculum/AP-Physics-1
  - curriculum/AP-Physics-C-Mechanics
  - syllabus/0625-P1
  - syllabus/0625-P2
  - syllabus/0625-P3
  - syllabus/0625-P6
  - syllabus/0625-P7
  - type/deep
  - misconception/control-variable-is-the-apparatus
  - misconception/repeat-the-experiment
  - misconception/conclusion-from-theory
  - misconception/two-readings-are-enough
---

# Planning an Experiment 实验设计

> *In 1747, on HMS Salisbury, the surgeon James Lind took twelve sailors with scurvy, "as similar as I could have them", put them in the same part of the ship on the same diet, and gave each pair one thing different: cider, vinegar, sea water, a quart of dilute acid, a paste of garlic and mustard, or two oranges and a lemon. Six days later the two on citrus were fit for duty. Lind knew no chemistry and had the wrong theory of the disease. What he had was a plan: change one thing, keep the rest the same, and look. Every experiment you will ever design is that plan, and every mark you will ever lose on one is a place where you forgot a piece of it.*

## Definition

### Formal

To **plan an experiment** is to write down, before touching any apparatus, a procedure that a stranger could follow and that would answer one question of the form *how does X affect Y?* A valid plan fixes three kinds of variable. The **independent variable** is the one the experimenter changes; the **dependent variable** is the one observed or measured, which may change as a result; the **control variables** are every other quantity that could affect the dependent variable, and they are kept constant. An experiment is **valid** (a *fair test*) if it tests what it says it tests: only the independent and dependent variables change. The plan then names an **instrument** for every quantity, a **method** in order, the **range** and **number** of values of the independent variable, the **repeats**, the **table** the readings go into, and the **analysis** that turns the table into a conclusion.

### Intuitive

A plan is a chain, and each link exists because the one before demanded it. The question names two quantities, so you need two instruments. You will change one of them, so you must say how, and how many times, and over what span. Something else could change the answer behind your back, so you must say what, and hold it still. The numbers have to go somewhere, so you draw the table, and a table with no units is a table of nothing. And the numbers have to become a sentence, so you say which graph you will plot or which columns you will compare.

Nothing here is a convention invented for an exam. Each rule is a claim about what happens to your answer if you break it, and the claims can be measured: bunch your five wire lengths into the middle of the wire and the gradient you report is uncertain by 10 %; spread the same five lengths along the whole wire and it is 2 %. Let the kettle cool between trials and insulation that really cuts heat loss by 71 % will seem to cut it by 78 %, or by 61 %, depending only on which beaker you happened to start with.

### 中文锚点

你想知道两个保温杯哪个更保温，于是各倒一杯热水，过半小时摸一摸。可是第一杯是水刚烧开时倒的，第二杯是五分钟后倒的；一个杯子装满了，另一个只装了一半；一个放在窗边，一个放在屋子中间的桌上。半小时后两杯水温度不同——这个差别是杯子造成的，还是水温、水量、位置造成的？你分不清，这次比较就白做了。实验设计的核心只有这一个念头：**想知道甲对乙有没有影响，就只让甲变，其他一切可能影响乙的东西都按住不动**；这样乙的变化才只能归到甲头上。被你主动改变的量叫自变量，被你测量的量叫因变量，被你按住不动的量叫控制变量。其余的每一条规矩——每个量要有对应的仪器、自变量要取足够多又分得够开的值、每个读数要多测几次再取平均、表格的表头要写明物理量和单位——都是同一个念头往下推出来的：让最后那个结论除了"甲影响了乙"之外，找不到别的解释。

---

## Part I — The three kinds of variable

Read the question and underline two nouns. *"Investigate how the **thickness of insulation** affects the **rate of cooling** of hot water."* The first is what you change, the second is what you measure. Everything else in the room that could change the second one is a candidate control variable, and you find them by asking one question: **if this were different between two trials, could the dependent variable change even though the independent variable did not?** For the cooling beaker: the volume of water (more water, slower cooling), the starting temperature (hotter water loses heat faster), the room temperature, draughts, whether there is a lid, the beaker itself.

Three traps sit here, all visible in published mark schemes.

- **A control variable is a quantity, not an object.** "Use the same beaker" names apparatus; "keep the volume of water the same" names a variable. When a question says *"state one variable to keep constant"*, the scheme for November 2024 reads *"one suitable variable, not referencing apparatus"*.
- **What the set-up already fixes does not count.** In the falling-ball-in-oil question of June 2026, the scheme ignores "type of oil" and "distance between the lines": the question gave one cylinder of oil with two lines drawn on it, so they cannot vary. A control variable is something that *could* have changed in your hands.
- **The variable you chose cannot also be a control.** If the question lets you pick which factor to investigate (ball diameter, drop height, mass), every other factor on that list becomes a control variable, and the one you picked does not.

| Term | 中文 | Meaning |
|---|---|---|
| independent variable | 自变量 | the quantity the experimenter changes |
| dependent variable | 因变量 | the quantity observed or measured, which may change in response |
| control variable | 控制变量 | a quantity that could affect the dependent variable and is kept constant |
| valid / fair test | 有效 / 公平测试 | only the independent and dependent variables change |
| range | 范围 | the smallest to the largest value used or measured |
| anomaly | 异常值 | a result outside the general pattern of the others |
| repeatability | 重复性 | the same experimenter, same method and apparatus, gets the same result again |
| reproducibility | 再现性 | a different experimenter, or different apparatus or method, gets the same result |

**What an uncontrolled variable does, measured.** The script beside this note cools water under 0, 2, 4, 6 and 8 mm of insulation. With every trial started at 80 °C, 8 mm cuts the rate of cooling by **71 %**. Now boil the kettle once and work down the bench, so that each trial is poured 4 °C cooler than the last. Done thin-first, the same insulation appears to cut the rate by **78 %**; done thick-first, by **61 %**. Same insulation, same thermometer, same student; the conclusion moved by seventeen percentage points because of the order of the beakers. That is what "fair test" is protecting you from.

![[planning-an-experiment-confound.svg|760]]

## Part II — The chain

![[planning-an-experiment-skeleton.svg|900]]

**1. Apparatus: one instrument per quantity.** List every quantity your method mentions, and beside each write the thing that measures it. Rate of cooling is temperature over time, so a **thermometer and a stopwatch**; resistance is $V/I$, so a **voltmeter and an ammeter**; speed down a ramp is distance over time and the slope is an angle, so a **metre rule, a stopwatch and a protractor**. A plan that measures an angle and never mentions a protractor has lost its first mark. Choose the instrument whose smallest division suits the size of the thing: a metre rule (1 mm) for the length of a wire, a micrometer (0.01 mm) for its diameter, a measuring cylinder narrow enough that the volume you want spans many divisions. [[Calibration of Instruments]] and [[Significant Figures]] carry what each instrument can honestly report.

**2. Method: set, measure, change, repeat.** In order, as instructions: set the first value of the independent variable and measure it; do whatever makes the dependent variable happen; measure the dependent variable; **change the independent variable and repeat**. The phrase in bold is a marking point by itself on nearly every scheme, and "change the variable" is not enough: say *how* (add another layer of insulation, move the crocodile clip to a new length, adjust the variable resistor).

**3. Enough data: at least five values, widely spread, each repeated.** These are three separate decisions and they buy three different things.

![[planning-an-experiment-range.svg|900]]

- **Range buys the gradient.** Five lengths of wire between 0.40 m and 0.60 m give a gradient uncertain by **9.8 %**; five lengths between 0.10 m and 1.00 m, with the same meters and the same noise, give **2.2 %**. A best-fit line is a see-saw: readings bunched near the pivot cannot stop it rocking. Use as much of the available span as the apparatus allows.
- **Number buys the shape.** Two widely spread readings pin the gradient almost as well as five (**2.4 %**), and that is precisely the danger, because two points lie on a perfect straight line whatever the truth is. A filament lamp measured at 1 V and 6 V gives a flawless line; measured at six voltages, it shows a curve, and a resistance that has doubled from 9.8 Ω to 20.0 Ω. At least **five** values of the independent variable is the working minimum to tell a line from a curve, and it is the number the mark schemes name.
- **Repeats buy reliability.** Repeating each reading three times and averaging takes the 2.2 % to **1.3 %**, the $1/\sqrt{N}$ of [[Repeated Measurements]], and it is the only way an anomaly can be recognised as one. The wording matters: *"repeat each measurement and take an average"* scores; *"repeat the experiment"* is ignored, because it does not say what is done with the second set.

**4. The table.** One column for each measured quantity and one for each calculated quantity, independent variable first. Every heading is **quantity / unit**: `thickness / mm`, `θ / °C`, `t / s`, `rate of cooling / °C per s`. Units go in the heading and never in the body. If you chose weight as your variable the heading is `W / N`, and `m / kg` under a column called weight loses the mark. Leave room for the repeats and the mean.

**5. The analysis.** Say what you will do with the numbers, in one of two accepted forms: **plot a graph of [dependent] against [independent]** with both axes named, or **compare the readings in the table to see whether a change in X produces a change in Y**. "Compare the readings" with nothing after it is insufficient. A line graph is for a continuous independent variable; a **bar chart** is right only when the variable is a category, such as the metal a container is made from. And the conclusion must come from the readings: a prediction from theory ("thicker insulation traps more air, so it will cool more slowly") is ignored, however correct, because the question asked how you would *find out*.

**6. Read it back.** Two separate examiner reports end with the same advice: read the plan through and ask whether the experiment described could be carried out, and whether it is the experiment that was asked for. This is the only proofreading step in physics that routinely finds marks.

## Part III — Techniques, hazards and improving a method

A plan is judged on its choices, and the other practical questions ask for the same choices one at a time: *suggest a technique*, *state a precaution*, *identify a source of inaccuracy and an improvement*. A **technique** is something you do, not something you own: "use a set square" is apparatus, "hold a set square against the rule to check that it is vertical" is a technique.

| Situation | Technique that earns the mark | Why it works |
|---|---|---|
| reading any scale | view the scale **perpendicularly**, eye level with the mark | removes parallax error |
| length of a spring, height of a pointer | set square from the rule to the point; rule clamped vertical | the reading is taken at the true position |
| a small distance (paper, wire, one marble) | measure **many together** and divide | the scale's division is shared between them |
| a short time (one swing) | time **ten or twenty** swings and divide | the reaction error is shared: 10 % for one swing, 0.5 % for twenty |
| oscillations | count from the centre, use a fiducial marker | the bob is fastest there, so the moment is sharpest |
| liquid in a measuring cylinder | read the **bottom of the meniscus**, cylinder on the bench | the bench is level; your hand is not |
| temperature of a liquid | **stir**, wait for the reading to steady, bulb in the middle | the liquid is not at one temperature until mixed |
| optics with pins | pins **far apart**, upright, viewed at their bases | a longer baseline fixes the ray's direction |
| lens and screen | move the screen back and forth through the sharpest image | brackets the focus rather than guessing it |
| circuits | switch off between readings | the wire heats, and its resistance with it |

**Hazards** follow the same one-to-one habit: a hazard, and the precaution that answers *that* hazard. Hot water: keep the beaker away from the bench edge, stand while pouring. A stretched wire or loaded spring: eye protection, and something soft under the masses. Mains or high currents: switch off before changing the circuit, do not touch a hot resistance wire. A ray-box bulb: let it cool. "Be careful" and "wear goggles" attached to nothing score nothing.

**Evaluating and improving.** The question *"suggest one source of inaccuracy and an improvement"* is marked as a matched pair, and the improvement must cure the fault you named. *The graduations on the measuring cylinder are too far apart* pairs with *use a narrower cylinder, or more marbles so the volume change is larger*. *It is hard to stop the watch exactly as the trolley passes the line* pairs with *use light gates, or a longer distance so the time is larger*. Sort the fault first: a **random** error (reaction time, judging a fuzzy image) is reduced by repeats and averaging; a **systematic** one (a zero error, a ruler that starts 2 mm in, heat lost through the sides every time) is untouched by repeats and needs a changed method, as [[Accuracy vs Precision]] sets out. Two values "agree within the limits of experimental accuracy" at this level if they differ by no more than about **10 %**.

## Part IV — The twelve contexts

Practical papers draw their experiments from a stated list. Each is a place where the chain above has a standard shape.

| Context | Independent → dependent (typical) | The instrument pair | The standard control or technique |
|---|---|---|---|
| length, volume, force | — | rule, measuring cylinder, newton-meter | perpendicular viewing; displacement for irregular solids ([[Density and Pressure]]) |
| small distances, short times | — | micrometer; stopwatch | many-and-divide |
| a derived quantity | load → extension; $V$ → $I$; time → speed | rule and masses; meters; stopwatch and rule | gradient of the line, not one pair of readings ([[Hooke's Law for Springs]], [[Resistance]], [[SUVAT]]) |
| a relationship between two variables | length of wire → p.d. or resistance | voltmeter, ammeter, metre rule | same wire, same current, switch off between readings |
| comparing measured quantities | angle of incidence → angle of reflection | protractor, pins or ray box | thin pencil lines, pins far apart ([[Reflection and Refraction]]) |
| comparing derived quantities | density of two objects | balance, measuring cylinder | within 10 % counts as the same |
| cooling and heating | insulation, lid, surface area, start temperature → rate of cooling | thermometer, stopwatch | volume, start temperature, room temperature ([[Heat Transfer]], [[Specific Heat Capacity]]) |
| springs and balances | load → extension; moments about a pivot | rule, masses | zero the rule on the unloaded spring ([[Forces and Equilibrium]]) |
| timing motion or oscillations | length → period; slope → speed | stopwatch, rule, protractor | time many swings; release from rest each time ([[Simple Harmonic Motion]]) |
| electric circuits | length, diameter, current → $R$; current → brightness | ammeter in series, voltmeter in parallel | temperature of the wire ([[Electric Current]], [[Kirchhoff's Laws]]) |
| optics | object distance → image distance; colour → focal length | metre rule, screen, lens, pins | darkened room, object and lens at the same height ([[Lenses and Image Formation]]) |
| an unfamiliar procedure | whatever the stem says | whatever measures its two nouns | the chain, unchanged |

The last row is the point of the others. The papers say outright that the method "may not be familiar", and the candidates who struggle are the ones who had memorised eleven experiments instead of one chain.

## Where it is the working tool

- **Every medicine you have taken.** A clinical trial is Lind's plan with the controls tightened: the independent variable is drug or placebo, the dependent variable is recovery, and the control "everything else about the patients" is achieved by assigning people to the two groups **at random**, so that no hidden difference can line up with the treatment the way the cooling kettle lined up with the insulation. Double-blinding controls one more variable, the expectations of patient and doctor. No drug is licensed on a prediction from theory.
- **A/B testing.** When a shopping site shows half its visitors a green button and half a blue one and counts the purchases, it is running a one-variable experiment on millions of people a day; the engineering effort goes almost entirely into making sure nothing else differs between the two halves.
- **Engineering test rigs.** A wind tunnel exists to make air speed the *only* thing that changes. A tyre manufacturer tests compounds on the same car, same track, same driver, same temperature window, alternating runs so that the track warming through the day cannot masquerade as a better tyre, which is the thin-first, thick-first problem solved by interleaving.
- **The failure, for honesty.** In 1989 two chemists announced fusion in a jar of heavy water at room temperature. Laboratories worldwide tried to reproduce it and could not; the excess heat traced to uncontrolled variables in the calorimetry and a missing control run with ordinary water. The result was repeatable in one lab and not **reproducible** anywhere else, and that distinction, a vocabulary item on a school syllabus, is what ended it.

## Hands-on

Run `planning-an-experiment-sim.py`. It prints the four experiments this note quotes: the six wire plans and the uncertainty each leaves in the gradient; the lamp measured at two voltages and at six; the cooling beakers with the start temperature held and drifting, in both orders; and the pendulum timed over one, ten and twenty swings with a 0.1 s reaction error at each press (10 %, 1.0 %, 0.5 %). Change `SIGMA_R` to model worse meters, or the lengths in a plan, and watch the price change. Then do one for real, in a kitchen: two mugs, a kettle, a kitchen thermometer and a phone timer will reproduce the confounder in half an hour if you pour the second mug five minutes after the first.

![[planning-an-experiment-manim.mp4]]

*Two films. First, five noisy readings and their best-fit line, drawn again and again: bunched lengths make the line rock, spread lengths hold it still. Then five cooling trials done in order while the kettle cools, each point landing off the true curve, thin-first and thick-first.*

## Worked examples — every tool named

### Example 1 — the seven marks, all visible (Cambridge 0625, March 2024 Paper 62, Q4)

*A student investigates how the thickness of insulation surrounding a beaker affects the rate of cooling of hot water. Available: a glass beaker, a supply of hot water, a lid, strips of insulation. Plan the experiment: list additional apparatus; explain how to do it, including the measurements needed to find the rate of cooling; state the key variables to keep constant; draw a table; explain how to use the readings to reach a conclusion.* [7]

*Trigger: the bullet points in the question are the chain, in order; answer them in order.*

*Tool: one instrument per quantity.* Rate of cooling is temperature change over time: **a thermometer and a stopwatch** (1).
*Tool: set, measure, change, repeat.* Wrap one layer of insulation round the beaker and measure its thickness with a ruler. Pour in hot water, fit the lid, record the starting temperature and start the stopwatch; record the temperature after 5 minutes (1). **Repeat with two, three, four and five layers** (1).
*Tool: the control-variable question.* Keep the **volume of water** and the **starting temperature** the same each time (1, and a second control is one of the "additional" marks).
*Tool: quantity / unit.* Table headed `thickness / mm`, `start temperature / °C`, `final temperature / °C`, `time / s`, `rate of cooling / °C per s` (1).
*Tool: the two accepted analyses.* Plot a line graph of rate of cooling against thickness; if the line falls, thicker insulation slows the cooling (1).
*Tool: enough data.* Use at least five thicknesses, and repeat each and average; rate of cooling = temperature drop ÷ time (1 for any one).

The scheme's seven points are apparatus, method, repeat for new value, control variable, table, analysis, additional point, and they are the same seven on every planning question from 2023 to 2026.

### Example 2 — a circuit to complete, and a control that hides (Cambridge 0625, June 2024 Paper 63, Q4)

*Plan an experiment to investigate how the diameter of a wire affects its resistance, $R = V/I$. Wires of different known diameters are available.* [7]

*Tool: instrument per quantity.* $R$ needs $V$ and $I$: a **voltmeter and an ammeter** (1). *Tool: series and parallel.* Ammeter in series with the wire, voltmeter across the wire, correct symbols (1). Method: record the diameter, measure p.d. and current, repeat for each new diameter (1). *Tool: the control-variable question. What else changes the resistance of a wire?* Its **length**, its **material** and its **temperature** (1; a second one is the additional mark). Table: `diameter / mm`, `V / V`, `I / A`, `R / Ω` (1). Analysis: plot $R$ against diameter, or compare down the table (1). Additional: five diameters, or repeats and an average (1).

The report on this question notes that most candidates found length; few found temperature, which is the control the method itself threatens, since the current heats the wire. "Switch off between readings" is how the plan keeps its own promise.

### Example 3 — the method must be followable (Cambridge 0625, June 2025 Paper 63, Q4)

*Plan an experiment to investigate how the concentration of a gel affects the angle at which light is refracted on passing from air into the gel. Gel blocks of labelled concentration (in g/cm³), a ray-lamp and paper are available.* [7]

Apparatus: a **protractor and a ruler**, both (1). Method: place the block on paper and draw round it; shine a ray at the block; **mark the ray going in and the ray coming out**, remove the block, join the points through the block and measure the angle of refraction from the normal (1). Repeat for each concentration (1). Control: the **angle of incidence** (1). Table: `concentration / g/cm³`, `angle of refraction / °` (1). Analysis: line graph of angle against concentration (1). Additional: five concentrations, or repeat each angle and average (1).

The examiners' comments read like the chain's failure log: many omitted the ruler; many gave no means of tracing the emerging ray, so the angle could not have been measured; many left the units off the concentration heading; only the strongest asked for five values, and fewer still for repeated angle readings. Every one is a link unnoticed, and reading the plan back would have found each.

### Example 4 — choose your own variable (Cambridge 0625, June 2026 Paper 62, Q4)

*A metal ball is released above a cylinder of oil and timed between two lines on the glass. A selection of balls and a ruler are available. Plan an experiment to investigate how one variable affects the time $t$. State the variable chosen.* [7]

*Trigger: "one variable" of your choosing turns every other candidate into a control.* Choose **diameter of the ball**. Apparatus: stopwatch, and a micrometer for the diameter. Method: measure the diameter, release the ball from rest at a fixed height above the oil, time it from line 1 to line 2, repeat with balls of different diameter. Controls: **same material (so the density is the same), same release height**; "same oil" and "same distance between the lines" are ignored, because the apparatus fixes them. Table: `d / mm`, `t / s`, with columns for repeats and the mean. Conclusion: plot $t$ against $d$. Additional: five balls, or **repeat each timing and average**; "repeat the experiment" is ignored. If the chosen variable had been the *material* of the ball, the graph would have to be a bar chart, and if *weight*, the heading `W / N`.

### Example 5 — a source of inaccuracy inside the plan (Cambridge 0625, November 2024 Paper 63, Q4)

*Plan an experiment to compare the effect of different angles of slope on the average speed of a trolley between two points on a ramp. Average speed = distance ÷ time.* [7]

Apparatus: **stopwatch, metre rule, protractor**, all three (1). Method: set the angle and measure it; release the trolley from rest at a marked start; time it between the two marked points and measure the distance between them; repeat for different angles (1). *Tool: random or systematic?* A source of inaccuracy: it is **difficult to start and stop the watch exactly as the trolley passes the marks**, a random error (1). Control: the **distance between the points**, and the distance from the start to the first point (1). Table: `angle / °`, `time / s`, `speed / m/s` (1). Analysis: compare angle with speed, or plot speed against angle (1). Additional: five angles, repeats and an average, or a second control (1).

### Example 6 — the same chain at A Level, with the analysis made algebraic (Cambridge 9702, November 2025 Paper 52, Q1)

*A model wind turbine of swept area $A$ drives a current $I$ through a resistor $R$ when air of speed $v$, pressure $P$ and temperature $T$ passes it. It is suggested that $\dfrac{I^2R}{Q} = \dfrac{APv^3}{2T}$, where $Q$ is a constant. Plan a laboratory experiment to test the relationship between $I$ and $v$ and determine $Q$.* [15]

*Trigger: a suggested relationship with a constant to find means "which straight line?"*
**Defining the problem:** vary $v$, measure $I$; keep $A$ and $R$ constant (2), and $P$ and $T$ (an additional-detail mark). **Method:** a labelled diagram with a fan on the bench in line with the turbine; a circuit with the resistor and an ammeter in series across the turbine's terminals; vary $v$ by changing the fan's speed or its distance, measured with an **anemometer**; $T$ with a thermometer (4). *Tool: [[Linearisation]], rearrange to $y = mx$.* $I^2 = \dfrac{QAP}{2TR}\,v^3$, so **plot $I^2$ against $v^3$**; the relationship is valid if the graph is a **straight line through the origin**; then $Q = \dfrac{2TR \times \text{gradient}}{AP}$ (3). Or plot $\lg I$ against $\lg v$ and look for gradient 1.5. **Additional detail** (6 from a list of ten): a precaution *with its reason* (a guard because of the moving blades); clamp the turbine; $T = t + 273$; find $A$ from the blade length, measured on several blades and averaged; **wait for the current to steady**; measure $R$ with an ohmmeter in a separate circuit; check $P$ and $T$ before and after.

The 0625 chain has not changed; the A Level adds that the analysis must name the axes that make the law a straight line, and that each precaution carries its reason.

### Example 7 — the best question from another board: a slope that weighs a block (AP Physics 1, 2025 Free Response Q3, parts A and B)

*A uniform metre stick pivots at its centre, with a spring scale fixed at one end. A block of unknown mass $m_0$ can hang from any of a row of holes. Describe a procedure to collect data from which $m_0$ can be found from the slope of a linear graph, including steps to reduce uncertainty; then describe the graph and its analysis.*

*Trigger: "a linear graph whose slope gives $m_0$" is an instruction to find the physics first.* *Tool: moments about the pivot, from [[Forces and Equilibrium]].* With the block at distance $d$ from the pivot and the scale at distance $D$, balance gives $F D = m_0 g\, d$. **Procedure:** hang the block from a hole, measure $d$, hold the stick horizontal and read $F$; **repeat for each hole**, and repeat each reading several times (both procedure points). **Analysis:** plot $F$ against $d$; the slope is $m_0 g / D$, so $m_0 = \text{slope} \times D / g$ (both analysis points). The scoring guide accepts any pair of axes with the right functional dependence. The independent variable is $d$, the dependent is $F$, the control is $D$ and the stick's horizontality: the same chain, in another board's vocabulary.

## Common Misconceptions (Teaching Notes)

### 1. "Keep the beaker the same"

Apparatus named where a variable was asked for. **Fix:** for each object, ask what *about it* matters: not "the same beaker" but "the same volume of water"; not "the same wire" but "the same length and material". If the set-up already fixes it, it is not a control.

### 2. "Repeat the experiment"

It sounds like diligence and scores nothing. **Fix:** say what is repeated and what is done with the results: "repeat each time measurement three times and calculate the mean". The mean is the point; a repeat that is never averaged only uses up the afternoon.

### 3. The conclusion written before the experiment

"The thicker the insulation, the slower the cooling, because air is a poor conductor." True, and ignored. **Fix:** the plan ends with a procedure for reading the data: which graph, or which columns compared. The physics explains a result; it cannot stand in for one.

### 4. "Two readings are enough for a line"

Two readings are enough for *a* line and useless for deciding whether a line is the truth. **Fix:** show the lamp: two points, perfect line, wrong conclusion. Five values is the floor because it is the fewest that can expose a curve or an anomaly.

### 5. Five readings, all in the middle

Students choose convenient values: 40, 45, 50, 55, 60 cm. **Fix:** the see-saw. Spread the values over the whole span the apparatus allows; the simulation's 9.8 % against 2.2 % is the argument.

### 6. A precaution with no hazard, an improvement with no fault

"Wear goggles." "Use better equipment." **Fix:** always write the pair: *hazard, so precaution*; *fault, so cure*. If the second half would not fix the first half, neither scores.

## Exam Notes

### Cambridge 0625 (IGCSE) — practical assessment, Paper 5 (Practical Test) or Paper 6 (Alternative to Practical)

Either paper is 40 marks and **20 % of the qualification**, testing AO3 experimental skills only; both draw on the same twelve experimental contexts (Part IV) and the same skills: selecting and safely using techniques and apparatus, **planning**, making and recording observations, interpreting and evaluating data, and evaluating methods and suggesting improvements, using the ASE language of measurement (true value, measurement error, accuracy, precision, repeatability, reproducibility, validity, range, anomaly, independent and dependent variable; the wording need not be recalled). On every Paper 6 from 2023 to 2026 the **final question is a seven-mark plan** with the structure of Example 1: apparatus · method · repeat for a new value · control variable · table with quantities and units · analysis (a named graph or a stated comparison) · one additional point (five sets of data, repeats with an average, or a second control). Variants ask for a circuit diagram to be drawn or completed, a variable to be chosen, a source of inaccuracy, or say that safety need not be discussed. The bullet points in the stem map onto the marks one to one. Elsewhere on the paper the single marks are for a technique (perpendicular viewing is by far the commonest), a control variable "not referencing apparatus", a matched inaccuracy and improvement, and a judgement of whether two values agree within 10 %. Reading scales and tables belong with [[Significant Figures]] and [[Calibration of Instruments]]; best-fit lines, gradients and intercepts with [[Gradient (Vocab)]] and [[Scatter Diagrams]].

### Cambridge 9702 (A Level) — Paper 5, Planning, analysis and evaluation

Question 1 of Paper 5 is a **15-mark plan** for testing a given relationship: defining the problem (2: the independent and dependent variables, and what is held constant), methods of data collection (4: a labelled diagram, the instruments, how the independent variable is varied), method of analysis (3: the graph that linearises the relationship, the condition for validity, the constant from gradient or intercept) and additional detail including safety (6 from about ten). Example 6 is the pattern. Paper 3's practical test examines the 0625 skills with uncertainties attached; the formal rules are in [[Error Propagation]].

### IB Physics — the scientific investigation (internal assessment)

The internally assessed investigation is marked on research design, data analysis, conclusion and evaluation. Research design is this note: a focused question naming the independent and dependent variables, controls with the *method* of controlling each, and a sufficient range and number of values with repeats. There is no written planning question on the external papers.

### AP Physics 1 and AP Physics C — the Experimental Design and Analysis free-response question

Each exam carries one ten-point question of this type (Example 7): describe a procedure that would collect the data, include a step that **reduces experimental uncertainty** (several values of the independent variable, or repeated trials), say which quantities to graph to obtain a **linear** relationship, and relate the slope or intercept to the quantity sought. The vocabulary of control variables is not required; the design is judged on whether the described measurements could produce the described graph.

### Where it is *not* examined

- **0625 Papers 1–4** are theory papers; none asks for a plan.
- **AP Physics 2** has the same experimental-design question type as AP Physics 1; its contexts are fluids, thermal physics, circuits and optics, and the chain is unchanged.
- **Calculation of uncertainties** is not part of the 0625 plan: the ±10 % judgement is the whole of it.

---

## Connections

- **Builds on:** [[Accuracy vs Precision]] — random against systematic error, the sorting step before any improvement; [[Repeated Measurements]] — why the mean of $N$ readings is better by $\sqrt N$, and why timing twenty swings is a different trick from averaging; [[Calibration of Instruments]] — zero errors, the systematic fault repeats cannot cure; [[Significant Figures]] — what each instrument can honestly report in the table.
- **Extends into:** [[Linearisation]] — choosing the axes that turn a suggested law into a straight line, which is the whole of the A Level analysis section; [[Error Propagation]] — putting numbers on the uncertainty of the final result.
- **The next three links of the chain:** [[Recording and Analysing Experimental Data]] — reading a scale to half a division, the table, the graph with its best-fit line, the gradient triangle, anomalies and the 10 % test.
- **The contexts:** [[Heat Transfer]], [[Specific Heat Capacity]], [[Resistance]], [[Hooke's Law for Springs]], [[Simple Harmonic Motion]], [[Reflection and Refraction]], [[Lenses and Image Formation]], [[Density and Pressure]], [[Forces and Equilibrium]] — each supplies the physics that tells you *which* variables need controlling.
- **Maths bridge:** [[Scatter Diagrams]] and [[Gradient (Vocab)]] — best-fit lines and reading a gradient; [[Hypothesis Tests]] — the formal version of "could this difference be chance?".
- **Meta:** [[Forward Reading and Problem Discovery]] — asking "what else could have caused this?" is forward reading for causes, the hunter's habit applied to your own bench.

---

## Beyond Syllabus

### Randomisation: controlling what you cannot name
Recall that a control variable is anything that could change the dependent variable behind your back. The list is never complete: you controlled volume and start temperature, and did not think of the draught from the door. R. A. Fisher's answer, in the 1920s, was to stop trying to list them: do the trials in a **random order**, or assign subjects to treatments at random, and any unknown drifting influence is scattered across all values of the independent variable instead of lining up with it. The thin-first and thick-first cooling runs are the two worst orders; a shuffled order turns the kettle's bias into a little extra scatter, which repeats then average away. It is the single idea that separates a modern trial from Lind's.

### Blinding, and the experimenter as a variable
When a person judges the outcome, the person is part of the apparatus. Timing a swing you expect to be slower, you press a little late. Blind measurement, where whoever reads the instrument does not know which trial it is, is the control for that variable, and light gates are the school-laboratory version: they have no expectations.

### Why the gradient, and not one good reading
A single pair $(V, I)$ gives a resistance; so does the gradient of five pairs. The gradient is better for a reason beyond averaging: a constant systematic offset, such as a voltmeter reading 0.05 V high, shifts every point up by the same amount, which moves the **intercept** and leaves the gradient untouched. Plotting a line is a way of making a whole class of systematic error fall out of the answer, which is why practical papers at every level ask for the constant from a gradient.

### Factorial designs
"Change one variable at a time" is the rule for a first experiment, and it cannot see **interactions**: insulation may matter a great deal with a lid and hardly at all without one. A factorial design varies two factors together in all combinations (lid on or off × each thickness), and the interaction shows as lines on the graph that are not parallel. Agriculture, drug trials and chip fabrication all run this way; the one-variable fair test is its one-dimensional slice.

---

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $R = V/I$ | `R = V/I` | the derived quantity behind most circuit plans |
| $1/\sqrt{N}$ | `1/\sqrt{N}` | how the uncertainty of a mean falls with $N$ repeats |
| $I^2 \propto v^3$ | `I^2 \propto v^3` | a suggested law, linearised by plotting $I^2$ against $v^3$ |
| $m_0 = \text{slope} \times D/g$ | `m_0 = \text{slope} \times D/g` | a constant recovered from a gradient |
