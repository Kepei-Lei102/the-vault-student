---
chinese: 基尔霍夫定律 (Jī'ěrhuòfū dìnglǜ)
prerequisites:
  - "[[Electric Current]]"
  - "[[Resistance]]"
leads_to:
  - "[[Internal Resistance]]"
  - "[[Potential Dividers]]"
  - "[[Linear Systems in 3D]]"
tags:
  - subject/physics
  - domain/electricity
  - level/IGCSE
  - level/A-Level
  - level/AP
  - level/IB
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - curriculum/IB-Physics
  - syllabus/9702-10-2
  - syllabus/0625-4-3
  - type/deep
  - misconception/current-is-used-up
  - misconception/parallel-resistances-add
  - misconception/the-nearer-resistor-gets-more-current
---

# Kirchhoff's Laws 基尔霍夫定律

> *Two sentences, written by a 21-year-old student in 1845, are the whole of circuit theory. Everything else — series, parallel, the potential divider, the internal resistance of a cell, the simulator that checks every chip before it is made — is those two sentences applied. And neither is a new law of physics: one is "charge is conserved", the other is "energy is conserved", each said about a wire.*

## Definition

### Formal

**Kirchhoff's first law (the junction rule).** At any junction in a circuit, the sum of the currents flowing *into* the junction equals the sum of the currents flowing *out*:

$$\sum I_{\text{in}} = \sum I_{\text{out}}.$$

It is a consequence of the **conservation of charge**: charge is neither created nor destroyed, and a junction stores none, so whatever arrives per second must leave per second.

**Kirchhoff's second law (the loop rule).** Around any closed loop in a circuit, the sum of the electromotive forces equals the sum of the potential differences across the components:

$$\sum \mathcal{E} = \sum IR,$$

or equivalently, the algebraic sum of all the e.m.f.s and p.d.s around the loop is zero. It is a consequence of the **conservation of energy**: a charge carried once around a closed path and back to its starting point has gained, from the sources, exactly the energy it lost in the components — otherwise the circuit would be a machine for making energy from nothing.

### Intuitive

Think of the circuit as a hill walk with water. The **junction rule** is the river fork: what flows into the fork per second flows out of it per second, split between the branches; the fork itself holds no water. The **loop rule** is the height: a pump (the cell) lifts every litre by a fixed height (the e.m.f.); every stretch of pipe it flows through drops it back (a p.d.); after one full circuit it is back at the level it started, so the total lift must equal the total drop. Potential is height. A loop is a walk that comes home.

### 中文锚点

看你家的电路。所有的灯是**并联**的：关掉客厅的灯，卧室的灯不会灭——因为每盏灯自己占一条支路，两端直接接在同样的 220 V 上。一个插线板上插了电水壶、吹风机、电暖器，插线板发烫、保险丝熔断：因为**总电流等于各支路电流之和**——这就是**基尔霍夫第一定律**（节点电流定律）：流进一个节点的电流之和等于流出的电流之和。它不是一条新的物理定律，它就是"电荷守恒"：电荷不会凭空多出或消失，一根导线也存不住电荷，所以每秒进来多少就得每秒出去多少。**第二定律**（回路电压定律）讲的是能量：把电路想成爬山——电源像一台水泵，把每一库仑电荷"抬高"一段（电动势 $\mathcal{E}$，每库仑得到的能量）；每经过一个电阻，电荷就"往下掉"一段（电势差 $IR$，每库仑交出去的能量）；绕一圈回到原点，**抬高的总高度必须等于掉下来的总高度**——$\sum \mathcal{E} = \sum IR$。否则电荷绕一圈回来还多了能量，那就是永动机。这两句话就是整个电路理论：**串联**的公式（$R = R_1 + R_2$）是回路定律加"串联电流处处相同"推出来的；**并联**的公式（$1/R = 1/R_1 + 1/R_2$）是节点定律加"并联电压处处相同"推出来的；下一张卡的**电源内阻**是把电池里那个小电阻也放进回路里算一遍；**分压器**是回路定律用在两个串联电阻上。考试里所有"求电流、求电阻、求内阻"的题，做法都是同一套：**标出每条支路的电流，在节点上用第一定律，绕回路用第二定律，方程数够了就解。** 本卡的五道真题全是这样做的。

| English | 中文 | 一句话 |
|---|---|---|
| Junction (node) | 节点 | 三条或更多导线相接的点——它**存不住**电荷 |
| Loop | 回路 | 从一点出发绕回原点的闭合路径 |
| First law (junction rule) | 第一定律（节点电流定律） | $\sum I_{\text{in}} = \sum I_{\text{out}}$——电荷守恒 |
| Second law (loop rule) | 第二定律（回路电压定律） | $\sum \mathcal{E} = \sum IR$——能量守恒 |
| e.m.f. $\mathcal{E}$ | 电动势 | 电源给每库仑电荷的能量（"抬高"） |
| p.d. $V = IR$ | 电势差 | 每库仑电荷在元件上交出的能量（"落差"） |
| Series | 串联 | 同一条路，电流相同，电压相加 |
| Parallel | 并联 | 分几条路，电压相同，电流相加 |

---

## Part I — Two laws that cannot be false

### The first law is charge conservation with nowhere to hide

[[Electric Current]] established two facts this law rests on. Current is a *rate* — coulombs per second passing a point — and charge is *conserved*: no process anyone has observed creates or destroys net charge. Add one more: **a wire, or a junction of wires, does not accumulate charge.** If more charge arrived at a junction each second than left, charge would pile up there, its electric field would grow, and within nanoseconds that field would push the excess out. In a steady circuit nothing piles up anywhere. So the rate in must equal the rate out — not approximately, not on average, but exactly, at every junction, at every instant.

That is the whole proof, and it is why the exam asks you to *state* the law and *name the conservation law behind it* as two separate marks: "sum of currents into a junction = sum of currents out" (or "the algebraic sum of currents at a junction is zero"), then "conservation of charge".

![[kirchhoff-two-laws.svg|820]]

A consequence worth saying aloud, because it is the commonest wrong belief in the subject: **current is not used up.** The 3.0 A in the figure splits into 1.2, 0.8 and 1.0 A; nothing has been consumed. What *is* used up is energy per charge — which is the second law's business.

### The second law is energy conservation, walked round a loop

[[Resistance]] defined the two voltages. **E.m.f.** is the energy a source gives *to* each coulomb it pushes round the circuit; **p.d.** is the energy each coulomb gives *up* in a component. Both are joules per coulomb — heights, in the hill picture. Now take one coulomb and walk it round any closed loop. Through the cell it climbs by $\mathcal{E}$. Through each resistor it drops by $IR$. When it arrives back where it started it must be at the same *potential* it left from — potential is a property of the point, like the height of a place on a map, not of the route taken to reach it. So the climbs must equal the drops:

$$\sum \mathcal{E} = \sum IR .$$

![[kirchhoff-potential-hill.mp4]]

The animation walks a coulomb round a 6 V cell and two resistors: up 6 V, down 2 V, down 4 V, home at zero. If the sum did not close, the coulomb would return with more energy than it left with, and a circuit would be a perpetual-motion machine; the loop rule is the statement that it is not.

> [!tip] The sign convention, once and for all
> Pick a direction to walk the loop (any direction; clockwise is conventional). Walking through a **source from its − terminal to its +** counts the e.m.f. as **positive** (you climbed); the other way, negative. Walking through a **resistor in the direction of its current** counts the p.d. as a **drop**, $-IR$ (you descended); against the current, $+IR$. Add everything up and set it to zero. If you did not know a current's direction in advance, guess one and label it; a negative answer means the current flows the other way, and nothing else needs redoing. The exam rarely needs more than one loop, but the convention is what keeps a two-loop problem from becoming a sign lottery.

## Part II — Series and parallel, derived

Cambridge's LO says *derive*, not *recall*, and the derivation is where the understanding lives.

### Series — one road, one current

Two resistors in series carry the **same current** $I$. That is not an extra assumption: apply the first law at the point between them, where one wire comes in and one goes out — what enters $R_1$'s far end must leave into $R_2$. Now apply the loop rule to the circuit containing them and a source $\mathcal{E}$:

$$\mathcal{E} = IR_1 + IR_2 = I(R_1 + R_2).$$

A single resistor that drew the same current from the same e.m.f. would satisfy $\mathcal{E} = IR$. So

$$R = R_1 + R_2 + \cdots$$

Resistances in series **add**, and the combination is always *larger* than any member: the coulomb has to fight through both.

### Parallel — several roads, one height

Two resistors in parallel have the **same p.d.** $V$ across them: both are connected between the same two points, and the potential of a point is the potential of a point. The total current splits at the junction by the first law, $I = I_1 + I_2$, and each branch obeys $V = I_k R_k$:

$$I = \frac{V}{R_1} + \frac{V}{R_2} \quad\Longrightarrow\quad \frac{I}{V} = \frac{1}{R_1} + \frac{1}{R_2}.$$

A single equivalent resistor would have $I/V = 1/R$. So

$$\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots, \qquad\text{and for two:}\quad R = \frac{R_1 R_2}{R_1 + R_2}.$$

The combination is always *smaller* than the smallest member — adding a road, even a narrow one, can only make the whole easier to pass. Two equal resistors in parallel halve; a 10 Ω beside a 15 Ω gives 6 Ω; a huge resistor in parallel with a small one barely changes it.

> [!warning] What "the same" means
> **Series: the same current, different p.d.s** (bigger $R$ takes the bigger share, $V \propto R$). **Parallel: the same p.d., different currents** (bigger $R$ takes the smaller share, $I \propto 1/R$). Students who mix these up write $I_1 = I_2$ for parallel branches or $V_1 = V_2$ for series ones, and every later line inherits the error. Say which quantity is shared *before* writing anything.

### E.m.f. sources, and the resistor hiding inside them

Cells in series add their e.m.f.s — the loop rule, walked through two lifts. And every real source has a resistance of its own, $r$, in series with its e.m.f.: the loop rule through a cell driving an external resistance $R$ reads $\mathcal{E} = IR + Ir$, so the **terminal p.d.** $V = IR$ is less than $\mathcal{E}$ by $Ir$. [[Internal Resistance]] takes this on; here it is simply one more $IR$ term in the loop, and four of the five worked questions below contain it.

## Part III — Solving a circuit: the procedure

Every circuit question on every board is the same procedure:

1. **Label the currents.** One symbol per branch; the first law reduces the count (three branches meeting at a junction need only two symbols).
2. **Write what is shared.** Series → same $I$. Parallel → same $V$. Say it in words on the page; it is usually a mark.
3. **Apply the first law at junctions** and **the loop rule round loops** until you have as many independent equations as unknowns. Two resistors in parallel across a cell is usually one junction equation and one loop.
4. **Reach for the combination formulas as a shortcut**, not a substitute — they *are* the two laws pre-applied, and the exam sometimes asks you to show it.
5. **Check the sign and the size.** A negative current means a guessed direction was wrong. A parallel combination bigger than its smallest member is arithmetic gone wrong.

*Triggers to notice:* "current in the cell" → the total, before any junction; "p.d. across the parallel pair" → one number for both branches; "voltmeter reads less than the e.m.f." → internal resistance is in the loop; "state and explain the effect of adding a resistor in parallel" → total resistance falls, so cell current rises, so the $Ir$ drop grows.

## Worked examples — real Paper 2 questions, every tool named

### June 2024 Paper 23 Q5 — derive the parallel formula, find $r$ [2 + 3 + 4]

![[kirchhoff-circuit-j24.svg|520]]

A cell of e.m.f. 1.50 V and internal resistance $r$ drives $R_1 = 10\ \Omega$ and $R_2 = 15\ \Omega$ in parallel; a voltmeter across the pair reads 1.38 V.

*(b)(i) Use Kirchhoff's laws to show $1/R_T = 1/R_1 + 1/R_2$.* The two marks are the two laws by name: **first law at the junction**, $I = I_1 + I_2$; then the shared p.d., $V/R_T = V/R_1 + V/R_2$, and cancel $V$. Write both lines — the scheme wants the junction statement *and* the division.

*(b)(ii) Calculate $r$.* *Tool: combination formula — the trigger is a parallel pair with a known p.d.* $R_T = \dfrac{10 \times 15}{25} = 6.0\ \Omega$. *Tool: $I = V/R$ on the external circuit* — $I = 1.38/6.0 = 0.23\ \text{A}$. *Tool: the loop rule with $r$ inside* — $\mathcal{E} = V + Ir$, so $r = (1.50 - 1.38)/0.23 = \mathbf{0.52\ \Omega}$. The scheme also accepts the potential-divider form $V = \mathcal{E}R_T/(R_T + r)$: the same loop rule, rearranged.

*(c) A third resistor is added in parallel. Effect on the cell current, and on the voltmeter reading?* *Tool: the parallel rule's direction, then the loop.* Total resistance **falls** (a new road), so with $\mathcal{E}$ unchanged the cell current **rises**; a bigger current means a bigger $Ir$ drop inside the cell, so the terminal p.d. the voltmeter reads **falls**. Four marks, two chains of two — each answer needs its *because*.

### November 2025 Paper 21 Q5 — state the first law; an NTC thermistor in parallel [1 + 3 + 4]

![[kirchhoff-circuit-n25.svg|520]]

A cell ($\mathcal{E} = 1.50$ V, $r = 0.12\ \Omega$) drives $R = 6.00\ \Omega$ in parallel with a thermistor T. At some temperature the current in $R$ is 0.200 A.

*(a)* "Sum of currents into a junction = sum of currents out." One mark; the algebraic-sum form is also accepted.

*(b)(ii) Explain why the current in R falls as the thermistor warms.* *Tool: the chain of the loop rule, one link per mark.* T's resistance falls (NTC), so the circuit's total resistance falls → the cell current **rises**, so the p.d. across $r$ rises → the terminal p.d. **falls**; $R$ is fixed, so its current falls. Three marks for three links, in that order. A student who writes "more current goes through the thermistor so less goes through R" has the picture backwards: the parallel branches do not compete for a fixed current; the terminal p.d. is what changes.

*(c)(i) The current in the cell.* *Tool: shared p.d. in parallel, then the loop rule for $r$.* Terminal p.d. $= 6.00 \times 0.200 = 1.20$ V. So the p.d. across $r$ is $1.50 - 1.20 = 0.30$ V, and $I_{\text{cell}} = 0.30/0.12 = \mathbf{2.5\ \text{A}}$. *(ii) The thermistor's resistance.* *Tool: the first law at the junction.* $I_T = 2.5 - 0.200 = 2.3$ A, and $R_T = 1.20/2.3 = \mathbf{0.52\ \Omega}$. Notice the order: the p.d. came from the branch you *knew*, the cell current from the loop, the unknown branch from the junction.

### March 2021 Paper 22 Q6 — a lamp and a resistor, with a graph [1 + 3 + 2 + 2]

![[kirchhoff-circuit-m21.svg|520]]

A 12.0 V battery with internal resistance $r$ drives a filament lamp in parallel with a resistor. The battery current is 3.6 A, the resistor's 2.1 A, and the lamp's $I$–$V$ characteristic is given.

*(b)(i) Resistance of the lamp.* *Tool: the first law* — $I_{\text{lamp}} = 3.6 - 2.1 = 1.5$ A. *Tool: read the characteristic at that current* — 4.4 V. *Tool: $R = V/I$, the chord of [[Resistance]]* — $4.4/1.5 = \mathbf{2.9\ \Omega}$. Three marks, three tools; the middle one is reading a graph, which is where the marks are lost.

*(ii) Internal resistance.* *Tool: the loop rule with $r$ inside* — $12.0 = 4.4 + 3.6\,r$, so $r = \mathbf{2.1\ \Omega}$. (The 4.4 V is the terminal p.d., shared by both parallel branches.)

*(iii) Time for the stored energy to fall from 470 kJ to 240 kJ.* *Tool: $P = \mathcal{E}I$ — the e.m.f. is the energy per coulomb the battery gives, and $I$ the coulombs per second.* $t = 230{,}000/(12 \times 3.6) = \mathbf{5300\ \text{s}}$. Note it is the *e.m.f.*, not the terminal p.d., that prices the battery's stored energy: the $Ir$ share is spent inside the battery, but it is still spent.

### June 2023 Paper 21 Q7 — one loop, three resistors, a thermistor's mood [2 + 2 + 2 + 3]

A 9.6 V battery of negligible internal resistance in series with 3400 Ω, 5800 Ω and a thermistor; the voltmeter across the 3400 Ω and the thermistor together reads 6.0 V.

*(a) Current in the 5800 Ω.* *Tool: the loop rule* — the 5800 Ω must carry the rest of the e.m.f., $9.6 - 6.0 = 3.6$ V, so $I = 3.6/5800 = \mathbf{6.2 \times 10^{-4}\ \text{A}}$. *(b) The thermistor's resistance.* *Tool: series — same current, resistances add* — $9.6 = 6.2 \times 10^{-4}(3400 + 5800 + R)$, so $R = \mathbf{6.3\ \text{k}\Omega}$. *(c) Energy after 330 C has passed.* *Tool: $\mathcal{E} = W/Q$* — $9.6 \times 330 = 3170$ J spent, leaving $\mathbf{2.3 \times 10^4}$ J. *(d) The thermistor's resistance rises. State the change in its temperature, its current, its p.d.* *Tool: NTC, then series.* Temperature **down** (that is what raising an NTC's resistance means); total resistance up, so the current **down**; but the thermistor's share of the fixed 9.6 V is $\propto$ its resistance, so its p.d. goes **up** even as the current falls. That last mark is the series rule read correctly: $V \propto R$ along one road.

### AP Physics C: E&M 2019 (Set 1) Q2 — two batteries, three branches, both rules at once [3 + 2 + 1 + 2 + 3]

![[kirchhoff-circuit-ap2019.svg|520]]

Two 6.0 V batteries and three resistors — 150 Ω, 200 Ω, 100 Ω — one per branch between the same two junctions; the branch currents $I_1$, $I_2$, $I_3$ are labelled as drawn. This is the multi-loop question Cambridge never sets and AP sets constantly, and it is the procedure of Part III with nothing skipped.

*(a)(i) Using Kirchhoff's rules, write — do not solve — equations for the three currents.* *Tool: one junction, two loops.* Three points, one per equation: the junction at the top, $I_1 + I_3 = I_2$ (both batteries push up into the rail; the 200 Ω carries the sum down); the left loop, $6 - 150\,I_1 - 200\,I_2 = 0$; the right loop, $6 - 100\,I_3 - 200\,I_2 = 0$. The outer loop, $6 - 150\,I_1 + 100\,I_3 - 6 = 0$, is also accepted for the third point — any two *different* loops will do, because the third is their difference. The guideline adds a line worth knowing: full credit for two loop equations written in *loop currents* instead.

*(ii) The current in the 200 Ω.* *Tool: substitute the two loop equations into the junction.* $I_1 = 0.04 - 1.33\,I_2$ and $I_3 = 0.06 - 2\,I_2$, so $0.10 - 4.33\,I_2 = 0$ and $I_2 = \mathbf{0.023\ \text{A}}$. (The guideline gives the point for the combination *or* for saying you solved the system on the calculator — AP allows the tool; Cambridge would not.) *(iii) Power in the 200 Ω:* $I^2R = 0.023^2 \times 200 = \mathbf{0.107\ \text{W}}$.

*(b)* The batteries are replaced by one battery $\varepsilon$ in the 150 Ω branch and a 50 Ω resistor in the 100 Ω branch; a voltmeter across the 200 Ω reads 4.4 V. *Current in the 50 Ω?* *Tool: parallel → the 4.4 V is across the 100 + 50 branch too.* $I = 4.4/150 = \mathbf{0.029\ \text{A}}$. *(c) The battery's e.m.f.* *Tool: the junction, then the loop through the battery.* $I_1 = 4.4/200 + 0.029 = 0.051$ A, and $\varepsilon = 0.051 \times 150 + 4.4 = \mathbf{12.1\ \text{V}}$; the alternate route in the guideline, $R_T = 150 + (200 \parallel 150) = 236\ \Omega$ and $\varepsilon = I_1 R_T$, is the same loop rule with the combination formula doing the middle step.

*(d)* swaps the 200 Ω for a capacitor, then for an inductor, at steady state — the RC and LR loops of [[Capacitors]]; the loop rule still governs, with a component whose p.d. depends on stored charge or on $\mathrm{d}I/\mathrm{d}t$.

**What AP marks that Cambridge does not:** the *system* — you are expected to set up three simultaneous equations from a diagram with no hints about which loop to take, and then solve them. Every step is still the two laws; there are simply more of them at once.

### Cambridge 0625 June 2022 Paper 42 Q9 — a three-position switch [1 + 2 + 2 + 3]

A 12 V supply, a motor of 2.0 Ω, a resistor of 3.0 Ω, and a switch that can connect to A (open circuit), B (motor alone) or C (motor and resistor in series).

*(a)* At A: no complete loop, **0 A**. At B: *tool $I = V/R$* — $12/2.0 = \mathbf{6.0\ \text{A}}$. At C: *tool: series adds* — $R = 5.0\ \Omega$, $I = 12/5.0 = \mathbf{2.4\ \text{A}}$. *(b) The same two resistors in parallel.* *Tool: product over sum* — $\dfrac{2.0 \times 3.0}{5.0} = \mathbf{1.2\ \Omega}$; the scheme gives one mark for the formula, one for the substitution, one for the answer — and checks that it is smaller than 2.0.

## Where this is the working tool

**Every chip, before it exists.** A modern processor is simulated, transistor by transistor, before a single wafer is made, and the simulator — SPICE, written at Berkeley in 1973, and every descendant — does one thing: it writes the first law at every node of the circuit as an equation, and solves the resulting system. A billion transistors is a billion-node system of Kirchhoff equations, solved thousands of times per simulated nanosecond. [[Linear Systems in 3D]] shows the same structure at three unknowns; nodal analysis is that, at scale, and it is the reason the world's electronics work the first time they are switched on.

**Your house.** Every socket and every light is a branch in parallel across the same 220 V, which is why one lamp failing leaves the rest lit, and why every appliance gets the same voltage regardless of what else is on. The price is the first law at the consumer unit: the current the supply delivers is the *sum* of every branch, and an extension lead running a kettle, a heater and a hairdryer is a junction summing three currents into one flex rated for one. The fuse is the first law's enforcer.

**Battery packs.** A single lithium cell gives about 3.7 V. The original Tesla Roadster carried 6,831 laptop cells arranged as 69 in parallel, then 99 of those groups in series: the series rule adds the voltages to about 375 V, and the parallel rule shares the current so that no cell carries more than a laptop's worth. Every electric car, laptop and phone pack is a series-of-parallel arrangement chosen by exactly these two rules — and the balancing electronics inside it exist because the first law guarantees the total, not the share each cell takes.

## Misconceptions

1. **"Current is used up going round the circuit."** It is not; charge is conserved and the first law says so at every junction. What is used up is energy per coulomb, and that is the second law's ledger.
2. **"The resistor nearest the cell gets the current first, so it gets more."** In series, every component carries the same current at the same instant; the circuit settles in nanoseconds and there is no "first". Position in a series loop is irrelevant.
3. **"Resistances in parallel add."** They add as *conductances*: $1/R = 1/R_1 + 1/R_2$. The combination is always less than the smallest branch — if your answer is not, it is wrong before you check the arithmetic.
4. **"Parallel branches share a fixed current."** They share a fixed *p.d.*; the total current is whatever the branches draw, and adding a branch increases it. This is the error behind "more current goes to the thermistor, so less to R".
5. **"The loop rule needs a loop through the battery."** Any closed loop works, including one through two parallel branches and no source: then $\sum \mathcal{E} = 0$ and the rule says the two branches have equal p.d. — which is where "same p.d. in parallel" comes from.
6. **"Voltage flows."** Current flows; potential is a height at a point. A voltmeter compares two heights; it does not measure anything moving.

## Beyond syllabus

### 1845 — a student's exercise

Gustav Kirchhoff published the two laws in 1845, at 21, while still a student at Königsberg — they were his answer to a seminar problem set by his teacher Franz Neumann on currents in a flat conducting plate. Ohm's law was only eighteen years old and still disputed; Kirchhoff took it as given, added the two conservation statements, and showed that together they determine the current in every branch of *any* network. Two years later he proved the general result — that a network with $n$ nodes and $b$ branches always yields exactly enough independent equations — using what is now recognised as the first application of graph theory to a physical problem ([[Graphs]] would call his independent loops a *cycle basis*). He went on to co-invent spectroscopy with Bunsen and to state the law of thermal radiation that led Planck to the quantum. The circuit laws were his warm-up.

### When the loop rule fails, and what is really true

The loop rule says potential is a height — a function of position — and that is only true when the electric field is *conservative*. [[Electromagnetic Induction]] is the case where it is not: a changing magnetic flux through the loop induces an e.m.f. *around* the loop that belongs to no component, and $\sum V$ round a closed path is then $-\,\mathrm{d}\Phi/\mathrm{d}t$, not zero. Two voltmeters across the same two points can read different values, depending on which side of the loop their leads run. The honest statement, [[Maxwell's Equations]]' Faraday law, contains Kirchhoff's second law as the special case $\mathrm{d}\Phi/\mathrm{d}t = 0$ — which every d.c. circuit satisfies, and which is why the exam never has to mention it.

### Nodal analysis — the two laws as one matrix

Write the first law at every node with each branch current expressed as (p.d.)/(resistance), and the unknowns become the node potentials; the equations are linear, and the whole circuit is $\mathbf{G}\mathbf{v} = \mathbf{i}$ for a conductance matrix $\mathbf{G}$. That is what SPICE solves, what [[Linear Systems in 3D]] does by hand for three nodes, and what makes circuit design a branch of linear algebra. Thévenin's theorem — any two-terminal network of sources and resistors is equivalent to one e.m.f. in series with one resistance — is the same linearity read as a promise, and it is why the "internal resistance" of a *whole power supply* is a meaningful number.

## Exam Notes

### Cambridge 9702 — §10.2 (AS Paper 2, with Paper 1 MCQs)

- **All seven LOs of §10.2 are this card:** recall the first law *and* that it follows from conservation of charge; recall the second law *and* that it follows from conservation of energy; **derive** the series formula from the laws; use it; **derive** the parallel formula; use it; use the laws to solve simple circuit problems. "Derive" is examined exactly as June 2024 P23 Q5(b)(i): name the law, write the shared quantity, cancel.
- **Formula sheet:** the series and parallel combination rules are printed on the Paper 1/2 sheet; the laws themselves are not — they are stated in words, one mark each, with a second mark for the conservation law behind each.
- **§10.1** (e.m.f. and terminal p.d., the *effect* of internal resistance) and **§10.3** (potential dividers, potentiometer, thermistor and LDR dividers) are [[Internal Resistance]] and [[Potential Dividers]]. The four A-Level questions above already use $\mathcal{E} = V + Ir$ as one loop term; the dedicated treatment lives there.
- Recurring shapes: state-the-law (1); state its conservation law (1); derive series or parallel (2); a cell with $r$ and a parallel pair — find $I$, $r$, or a branch resistance (3–4); "state and explain the effect of adding a resistor in parallel" (2 + 2); an NTC thermistor's chain of consequences (3); an energy-from-e.m.f. arithmetic (2).

### Cambridge 0625 IGCSE — §4.3.2 (Paper 3/4) 

- **Core:** the current is the same at every point in a series circuit; construct and use series and parallel circuits; combined e.m.f. of cells in series; combined resistance of resistors **in series**; in a parallel circuit the source current is larger than any branch current, and the combined resistance is *less* than either resistor; the advantages of lamps in parallel (independent switching; each gets the full p.d.; one failing leaves the others lit).
- **Supplement:** recall and use the junction rule ("sum of currents into a junction = sum out", named as the first law in all but name), the series p.d. rule (total p.d. = sum of the p.d.s), the parallel p.d. rule (same across every branch); **calculate** the combined resistance of **two** resistors in parallel. Three resistors in parallel, and the derivations, are A-Level.
- §4.3.1 (circuit symbols and component behaviour) and §4.3.3 (the potential divider and its $R_1/R_2 = V_1/V_2$) sit with [[Potential Dividers]]; §4.4 electrical safety is [[Electrical Safety]].

### AP Physics 2 (§11.2, §11.5–11.7) and AP Physics C: E&M (§11.2, §11.5–11.7)

- Simple and compound d.c. circuits, equivalent resistance in series and parallel, and both Kirchhoff rules by name — *loop rule* $\sum \Delta V = 0$ and *junction rule* $\sum I_{\text{in}} = \sum I_{\text{out}}$. AP asks multi-loop circuits more often than Cambridge: two sources, three branches, solve the simultaneous equations — the 2019 Set 1 Q2 worked above is the standard shape, and its scoring guideline gives one point per equation (junction, loop, a *different* loop) before any arithmetic. The sign-convention callout above is written for exactly that. AP-C adds nothing conceptually here; its extra weight falls on the RC circuits of [[Capacitors]].

### IB Physics — B.5.4

- Series and parallel rules and Kirchhoff's laws, in the same breath as internal resistance and potential dividers; this card carries the first half of that row, [[Internal Resistance]] and [[Potential Dividers]] the rest.

### Not examined on…

- **Cambridge 9709 / 9231** — no circuits in the maths boards; the linear-algebra shadow of nodal analysis appears in [[Linear Systems in 3D]] as an application, not a syllabus row.

## Quick reference

| Ask | Answer |
|---|---|
| First law | $\sum I_{\text{in}} = \sum I_{\text{out}}$ at a junction — conservation of charge (a junction stores none) |
| Second law | $\sum \mathcal{E} = \sum IR$ round a closed loop — conservation of energy (potential is a height) |
| Series | same $I$; $V$s add; $R = R_1 + R_2 + \cdots$ (bigger than any) |
| Parallel | same $V$; $I$s add; $1/R = 1/R_1 + 1/R_2 + \cdots$ (smaller than any); two: $R_1R_2/(R_1+R_2)$ |
| Cell with $r$ | $\mathcal{E} = V + Ir$, one more loop term; $V = IR$ is the terminal p.d. |
| Add a branch in parallel | $R_{\text{total}}$ ↓ → $I_{\text{cell}}$ ↑ → $Ir$ ↑ → terminal p.d. ↓ |
| Sign convention | walk the loop; − to + through a source is $+\mathcal{E}$; with the current through $R$ is $-IR$; sum to zero |
| Procedure | label currents → say what is shared → junctions + loops → solve → check sign and size |

## Connections

- **Builds on:** [[Electric Current]] — charge conservation and "current is not used up", the first law's whole content; [[Resistance]] — e.m.f. and p.d. as energy per coulomb, the two heights the loop rule adds, and $V = IR$ for each drop.
- **Leads to:** [[Internal Resistance]] — the $Ir$ term the loop rule puts inside every real source, and what it does to the terminal p.d.; [[Potential Dividers]] — the loop rule on two series resistors, read out as a voltage, with a thermistor or LDR as one leg; [[Linear Systems in 3D]] — nodal analysis as a linear system, the form every circuit simulator solves.
- **Application:** [[Sensors and Control Systems]] — the thermistor and LDR whose changing resistance the November 2025 question walks through the loop, read as a voltage in the computing card's sensing chain; [[Electromagnetic Induction]] — where the loop rule stops being true and Faraday's law takes over.
- **Kindred:** [[Capacitors]] — the RC circuit is the loop rule with a component whose p.d. depends on stored charge, giving the exponential; [[Graphs]] — Kirchhoff's 1847 proof that a network's independent loops number $b - n + 1$ is the first use of graph theory in physics; [[Choosing Effective Equations]] — KCL at every node and KVL round every loop as the circuit's invariants, the forward-reading discipline in electrical clothing.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $\sum I_{\text{in}} = \sum I_{\text{out}}$ | `\sum I_{\text{in}} = \sum I_{\text{out}}` | first law |
| $\sum \mathcal{E} = \sum IR$ | `\sum \mathcal{E} = \sum IR` | second law; $\mathcal{E}$ is `\mathcal{E}` |
| $\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$ | `\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2}` | parallel |
| $\mathcal{E} = V + Ir$ | `\mathcal{E} = V + Ir` | the loop through a real cell |
