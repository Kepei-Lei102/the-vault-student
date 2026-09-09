---
chinese: 内阻 (nèizǔ) — 电源内部的电阻
prerequisites:
  - "[[Electric Current]]"
  - "[[Resistance]]"
  - "[[Kirchhoff's Laws]]"
leads_to:
  - "[[Potential Dividers]]"
  - "[[Alternating Current]]"
tags:
  - subject/physics
  - domain/electricity
  - level/A-Level
  - level/AP
  - level/IB
  - curriculum/Cambridge-9702
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - curriculum/IB-Physics
  - syllabus/9702-10-1
  - type/deep
  - misconception/emf-is-a-force
  - misconception/terminal-pd-equals-emf
  - misconception/internal-resistance-is-a-separate-component
  - misconception/maximum-power-is-maximum-efficiency
---

# Internal Resistance 内阻

> *Every source of electrical energy is also a resistor. You cannot buy a battery without one, and you cannot open the case and take it out — which is why the voltage on the label is a promise the battery keeps only when nothing is asking for current.*

## Definition

### Formal

The **electromotive force (e.m.f.)** $\mathcal{E}$ of a source is the energy transferred from other forms to electrical energy per unit charge, in driving charge around a complete circuit: $\mathcal{E} = W/Q$, in volts.

The **internal resistance** $r$ of a source is the resistance of the source itself — of the electrolyte, the electrodes, the plates and the connections inside the case — which the current must pass through on its way out. It behaves as a resistor in **series** with an ideal e.m.f., so that when a current $I$ flows the potential difference across the terminals, the **terminal p.d.** $V$, is less than the e.m.f. by the p.d. dropped across $r$:

$$V = \mathcal{E} - Ir, \qquad \text{equivalently} \qquad \mathcal{E} = I(R + r)$$

for an external resistance $R$. The quantity $Ir$ is called the **lost volts**: the energy per coulomb spent heating the source instead of the circuit.

### Intuitive

A battery is a pump. Its e.m.f. is the height the pump can lift water when nothing is flowing. Its internal resistance is a narrow pipe *inside the pump*: the harder you draw, the more of the lift is spent forcing water through that pipe, and the less height reaches the tap. With the tap closed you measure the full lift. Open it wide and the pressure at the tap sags — not because the pump got weaker but because you are finally paying for the pipe.

### 中文锚点

冬天在户外拍照，手机明明显示还有 20% 电，一开相机就直接关机；揣回口袋捂五分钟，又能开机了。汽车打火那一瞬间，仪表盘和大灯会暗一下。这两件事背后是同一个物理原理：**电源自己也是一个电阻。** 电池标着 3.7 V、1.5 V，那是**电动势**（e.m.f.，$\mathcal{E}$）——不通电流时每库仑电荷能得到的能量。可电流一旦流起来，它得先穿过电池内部的电解液和电极，这一段有电阻，叫**内阻** $r$；电流越大，内部消耗的电压 $Ir$（**内电压**，国际课程叫 lost volts）越多，真正送到接线柱上的**路端电压** $V = \mathcal{E} - Ir$ 就越低。手机在低温下内阻飙升，相机一开、电流一大，路端电压跌破关机线，于是"20% 的电"关机了；捂暖，内阻下降，它又活了。汽车启动电机要抽一两百安，12.6 V 的电瓶瞬间只剩 9 到 10 V，灯就暗了。这张卡讲三件事：**内阻从哪来**（化学反应和离子迁移都有"摩擦"）、**怎么测**（改变外电阻，画路端电压对电流的直线：截距是电动势，斜率是 $-r$，这是 A-Level 实验课的经典题）、**它决定了什么**（短路电流、最大输出功率——外电阻等于内阻时输出最大，但效率只有一半；电压表为什么要内阻大；电池"健康度"很大程度上由内阻决定）。

| English | 中文 | 一句话 |
|---|---|---|
| Electromotive force (e.m.f.) | 电动势 | 电源把每库仑电荷"抬"到多高——不通电流时的路端电压 |
| Internal resistance $r$ | 内阻 | 电源自己内部的电阻，和电动势串联 |
| Terminal p.d. $V$ | 路端电压 / 端电压 | 接线柱之间真正能用的电压：$V = \mathcal{E} - Ir$ |
| Lost volts $Ir$ | 内电压 / 损失电压 | 花在电源内部发热上的那部分 |
| Short-circuit current $\mathcal{E}/r$ | 短路电流 | 外电阻为零时的电流——只由内阻决定 |
| Closed-circuit Ohm's law | 闭合电路欧姆定律 | $I = \mathcal{E}/(R + r)$，人教版必修三的叫法 |
| Maximum power transfer | 最大功率传输 | 外电阻等于内阻时输出功率最大，效率 50% |
| Null method | 零示法 / 补偿法 | 电流为零时读数——测电动势不受内阻影响 |

---

## Part I — Where the resistance comes from

A cell makes its e.m.f. chemically: at one electrode a reaction pushes electrons out, at the other a reaction takes them in, and the two reactions can only continue if ions drift through the electrolyte between them to keep the charge balanced. Every step of that has friction. Ions move slowly through a liquid or a paste; the electrode surfaces have a finite rate at which the reaction can proceed; the current collectors and terminals are metal with resistance of their own. Add them up and the cell is, unavoidably, a resistor — one you cannot separate from its e.m.f. because both live in the same chemistry.

That origin explains the three facts about $r$ that matter in practice:

| Fact | Why |
|---|---|
| **It rises in the cold.** | Ion mobility falls with temperature; a lithium cell at $-10\,°\text{C}$ can have several times its room-temperature $r$. This is the phone-dies-in-winter effect. |
| **It rises with age and use.** | Electrode surfaces degrade and the electrolyte dries or decomposes; a worn cell may still show a healthy e.m.f. but a large $r$. "Battery health" is, in large part, a measurement of $r$. |
| **It is smaller for bigger cells.** | More electrode area in parallel means more paths for the reaction, just as thicker wire has less resistance. A car battery's $r$ is thousands of times smaller than a button cell's. |

Typical values, so that later numbers have a scale:

| Source | Internal resistance (order of magnitude) |
|---|---|
| Laboratory bench power supply | $\sim 0.01\ \Omega$ (deliberately made tiny) |
| Car battery (12 V lead–acid) | $\sim 0.005$ – $0.02\ \Omega$ |
| Lithium-ion cell (18650) | $\sim 0.03$ – $0.1\ \Omega$ |
| AA alkaline cell, fresh | $\sim 0.15$ – $0.3\ \Omega$ |
| 9 V "PP3" battery | $\sim 1$ – $2\ \Omega$ |
| A lemon with two metal electrodes | $\sim$ thousands of ohms — which is why it lights nothing |

---

## Part II — The equation, derived twice

### From energy, per coulomb

Follow one coulomb around the circuit in the figure. Inside the cell the chemistry hands it $\mathcal{E}$ joules. Before it can leave, it has to push through the cell's own resistance $r$, where it gives up $Ir$ joules as heat. What emerges at the terminals is $\mathcal{E} - Ir$ joules per coulomb — and that, by definition, is the terminal p.d. It then spends exactly that much crossing the external resistor: $V = IR$. Energy is conserved on every lap:

$$\underbrace{\mathcal{E}}_{\text{supplied per coulomb}} \;=\; \underbrace{IR}_{\text{to the circuit}} \;+\; \underbrace{Ir}_{\text{lost inside the cell}}$$

Multiply through by $I$ and the same sentence is about power: $\mathcal{E}I = I^2R + I^2r$. The source generates $\mathcal{E}I$; the circuit gets $I^2R$; the rest heats the battery. A phone that is warm while fast-charging is $I^2 r$ made tangible.

### From Kirchhoff's second law

[[Kirchhoff's Laws]] gives the same line in one step. Walk the loop: one rise of $\mathcal{E}$ through the cell, one drop of $Ir$ through its internal resistance, one drop of $IR$ through the load. The sum of e.m.f.s equals the sum of p.d.s, so $\mathcal{E} = Ir + IR$, and the current a source can drive is

$$I = \frac{\mathcal{E}}{R + r}.$$

The Chinese syllabus calls this the *closed-circuit Ohm's law* (闭合电路欧姆定律), which is a good name: it is $V = IR$ applied to the *whole* loop, with the source's resistance counted honestly.

![[internal-resistance-circuit.svg|760]]

### E.m.f. and terminal p.d. — the distinction in energy terms

Both are measured in volts and both are energies per unit charge, which is why students confuse them. They differ in *which* energy. The e.m.f. is the energy **given** to each coulomb by the source, converted from chemical (or light, or mechanical) energy. The terminal p.d. is the energy per coulomb actually **delivered** to the external circuit. They are equal only when no current flows — the open-circuit condition — because only then is nothing spent inside. As soon as the circuit closes, $V < \mathcal{E}$ by exactly the energy per coulomb dissipated in $r$. A voltmeter of very high resistance across a lone cell reads $\mathcal{E}$ (to within the tiny current it draws); the same voltmeter across the cell while it drives a lamp reads $V$.

> [!info] What the number on the label means
> The "1.5 V", "3.7 V" or "12 V" printed on a cell is its **nominal** voltage — a round number near the *average* terminal p.d. over a discharge at a modest rated load — not its e.m.f. when full. A fresh alkaline AA reads about 1.6 V open-circuit and is counted flat at 0.9 V; a lithium-ion cell is 4.2 V full, 3.0 V at cut-off, and "3.7 V" in between; a car battery is 12.7 V fully charged, the "12" being six lead–acid cells at a nominal 2 V each. The label also carries a hidden condition: the datasheet's **maximum continuous discharge current** — 10 A, say, for a good 18650 — which is really a *minimum load resistance*. Below it the lost volts $Ir$ grow past what the device can tolerate, the terminal p.d. drops through the cut-off, and the "voltage on the label" is no longer being delivered. A cell's rating is a promise about $\mathcal{E}$ made under a condition about $R$.

> [!tip] The only thing you can touch
> $\mathcal{E}$ and $r$ are a *model* of what is inside the case, and the model has two parameters. All you can ever measure from outside are terminal p.d.s and currents. That is why every determination of $r$ is indirect: you change the load, watch how $V$ responds, and infer the two numbers from the line. There is no experiment that "reads" $r$ directly, any more than there is a meter for the height of a pump.

### The straight line — and the experiment behind it

Write the equation as $V = \mathcal{E} - rI$ and it is $y = c + mx$: a plot of terminal p.d. against current is a **straight line** with intercept $\mathcal{E}$ and gradient $-r$. That single sentence is the most-examined fact in this topic and the standard AS practical: a cell, a variable resistor, an ammeter in series and a voltmeter across the cell's terminals; change the resistor, record $I$ and $V$, plot, read off.

![[internal-resistance-vi-line.svg|820]]

Three features of the line carry meaning:

- **The intercept on the $V$ axis** is the e.m.f. — the terminal p.d. extrapolated to zero current, where no volts are lost.
- **The gradient** is $-r$. A steeper line is a cell that sags more per ampere — a higher internal resistance.
- **The intercept on the $I$ axis** is the **short-circuit current** $\mathcal{E}/r$, the most the cell can ever supply, reached when the external resistance is zero and *all* the e.m.f. is dropped across $r$. For the battery in the figure that is $7.4/8.0 \approx 0.92$ A; for a car battery with $\mathcal{E} = 12.6$ V and $r = 0.01\ \Omega$ it is over a thousand amperes, which is why a spanner dropped across the terminals welds itself in place. The same arithmetic is why a shorted battery **burns**: with $R = 0$ the entire output $\mathcal{E}^2/r$ is dissipated inside the cell. A lithium-ion 18650 at 3.7 V with $r = 0.05\ \Omega$ drives 74 A through itself and turns 270 W of heat loose in a can the size of a finger; the electrolyte boils, the separator fails, and the reaction feeds on its own heat — thermal runaway. The internal resistance that limits the short-circuit current is also the resistor the current heats.

![[internal-resistance-sag.mp4]]

*The clip runs the experiment: as the load resistance falls the current rises, the red share of the e.m.f. — the lost volts — grows, and the yellow point slides down the line. At $R = r$ exactly half the e.m.f. is spent inside the cell; towards a short circuit the terminal p.d. collapses and the cell is heating only itself.*

> [!warning] Practical honesty
> The line is straight only while $r$ stays constant. Draw a large current for long and the cell warms, its chemistry shifts and $r$ changes — so real data curve slightly at the high-current end, and a good experiment takes each reading quickly and opens the switch between readings. Never take the short-circuit reading directly: it is read off the graph, not measured.

---

## Part III — What the internal resistance decides

### Maximum power transfer

How much power can a source deliver to a load? With $I = \mathcal{E}/(R + r)$, the power in the load is

$$P = I^2 R = \frac{\mathcal{E}^2 R}{(R + r)^2}.$$

Small $R$ means large current but almost no voltage across the load; large $R$ means nearly the full e.m.f. but almost no current. Somewhere between is a maximum. *Tool: differentiate and set to zero* — the derivative of $R/(R+r)^2$ is $\dfrac{(R+r)^2 - 2R(R+r)}{(R+r)^4} = \dfrac{r - R}{(R+r)^3}$, which vanishes at

$$R = r, \qquad P_{\max} = \frac{\mathcal{E}^2}{4r}.$$

The load draws the most power when its resistance **matches** the internal resistance. This is the **maximum power transfer theorem**, and the figure shows its sting: at $R = r$ the current is $\mathcal{E}/2r$, so the load and the cell dissipate equal amounts — the efficiency, $R/(R + r)$, is exactly **50 %**.

![[internal-resistance-power-transfer.svg|820]]

So there are two different design goals, and they pull in opposite directions:

- **Match the load to $r$ when power matters and efficiency does not** — a radio transmitter feeding an aerial, an audio amplifier driving a loudspeaker, a microphone into a preamplifier, a signal source into a 50 Ω cable. Here the source's power is cheap and the *signal* delivered is what you want; engineers call this **impedance matching**, and the whole radio-frequency world is built on it.
- **Make $R \gg r$ when energy matters** — every power supply, every grid generator, every battery driving a motor. A power station whose load matched its internal resistance would waste half its output heating itself. Real generators and supplies are built with $r$ as close to zero as possible, and loads are always far larger.

### The voltmeter is a load too

A voltmeter across a source draws a current $\mathcal{E}/(R_{\text{meter}} + r)$ and therefore reads $\mathcal{E} - Ir$, not $\mathcal{E}$. The only way to read the e.m.f. itself is to draw *no* current. Two answers to that:

1. **A voltmeter of very high resistance.** Then $I$ is negligible and the reading is $\mathcal{E}$ to within a tiny error — the reason the ideal voltmeter of [[Resistance]] has infinite resistance, and the reason a digital multimeter (typically $10\ \text{M}\Omega$) reads a cell's e.m.f. correctly while a cheap analogue meter loads it visibly.
2. **A null method.** In a potentiometer circuit a slider on a wire is moved until a galvanometer reads exactly zero; at that point no current flows through the cell under test, so the p.d. balanced against it is its e.m.f., internal resistance or not. This is why the potentiometer measures e.m.f. *exactly* when a voltmeter can only approximate it — and why, in the June 2025 question below, a driver cell's internal resistance moves the null point while the test cell's would not.

---

## Worked examples — real papers, every tool named

### Cambridge 9702 June 2021 Paper 23 Q5 — define, explain, read the graph, sketch [2 + 3 + 3 + 2]

*(a) Define the e.m.f. of a source.* Two marks: **energy per unit charge** (B1) and **transferred by the source driving charge around the complete circuit** (B1) — "energy transferred from other forms to electrical" also earns the second. Say both halves; "the voltage of the battery" earns nothing.

*(b) The circuit has a battery of e.m.f. $E$ and internal resistance $r$, a variable resistor, a voltmeter across the terminals and an ammeter. A graph of terminal p.d. against current is a straight line from 7.4 V at $I = 0$ down to zero at about 0.92 A. Explain why $V$ is not constant.* *Tool: $V = E - Ir$.* There is a p.d. across the internal resistance (B1); changing the current changes that p.d. (B1); so $V = E$ minus the p.d. across $r$ varies while $E$ stays constant (B1). The scheme wants all three links in the chain, not the formula alone.

*(c)(i) The e.m.f.* Intercept on the $V$ axis: $E = 7.4$ V. *(ii) The maximum current.* Intercept on the $I$ axis: $0.92$ A. *(iii) The internal resistance.* *Tool: $r = E/I_{\max}$ or minus the gradient* (C1): $r = 7.4/0.92 = 8.0\ \Omega$ (A1).

*(d) Sketch a line for a battery with lower e.m.f. and lower internal resistance.* Lower e.m.f. → a lower intercept on the $V$ axis (B1); lower $r$ → a **shallower** negative gradient (B1). The dashed line in the figure above is one correct answer. The common error is drawing a parallel line lower down, which changes $E$ but not $r$.

### Cambridge 9702 June 2024 Paper 21 Q6(c) — one number, three routes [3]

*A cell of e.m.f. 1.50 V drives two resistors, 10 Ω and 15 Ω in series. The terminal p.d. is 1.35 V. Calculate the internal resistance.* The scheme accepts three routes, and they are worth seeing side by side because each is a different reading of the same loop:

- *Tool: current from the external circuit, then lost volts.* $I = 1.35/(10 + 15) = 0.054$ A (C1); $r = (E - V)/I$ (C1) $= 0.15/0.054 = 2.8\ \Omega$ (A1).
- *Tool: the whole loop as one resistor.* $R_{\text{total}} = E/I = 1.50/0.054 = 27.8\ \Omega$; subtract the external $25\ \Omega$: $r = 2.8\ \Omega$.
- *Tool: the potential-divider ratio.* The e.m.f. is shared between $r$ and the external $25\ \Omega$ in proportion to resistance: $\dfrac{0.15}{1.35} = \dfrac{r}{25}$, so $r = 2.8\ \Omega$ — the fastest, and the one [[Potential Dividers]] will make second nature.

### AP Physics C: E&M 2015 Q2 — the experiment, linearised [15 points]

*A student connects a battery of e.m.f. $\varepsilon$ and internal resistance $r$ to a variable resistor $R$ with a voltmeter across $R$, and records $V$ for six values of $R$ (0.50 Ω → 5.6 V, 1.0 → 7.4, 2.0 → 9.4, 3.0 → 10.6, 5.0 → 10.9, 10 → 11.4).*

*(a)(i) Derive $V$ in terms of $R$, $\varepsilon$, $r$.* *Tool: the loop rule* $\varepsilon = Ir + IR$, so $I = \varepsilon/(r + R)$ and $V = IR = \dfrac{\varepsilon R}{r + R}$ (2 points). *(ii) Rewrite as $1/V$ against $1/R$.* Invert: $\dfrac{1}{V} = \dfrac{r + R}{\varepsilon R} = \dfrac{r}{\varepsilon}\cdot\dfrac{1}{R} + \dfrac{1}{\varepsilon}$ (1 point). This is the move the whole question turns on: a curve in $V$–$R$ becomes a **straight line** in $1/V$–$1/R$, with gradient $r/\varepsilon$ and intercept $1/\varepsilon$. *Trigger:* whenever a formula has the unknowns inside a fraction like $R/(R + r)$, invert it and look for $y = mx + c$.

![[internal-resistance-ap2015.svg|760]]

*(b) Plot, label, scale, draw the best line* (4 points — one each for labels with units, scale, points, line). *(c) From the line: (i) $\varepsilon$* — intercept $1/\varepsilon \approx 0.080\ \text{V}^{-1}$ gives $\varepsilon \approx 12.5$ V (a least-squares fit gives 12.2 V; either is within the line's tolerance); *(ii) $r$* — the gradient must be taken from the **line, not from data points** (the guideline says so explicitly): $m \approx 0.046\ \Omega/\text{V}$, so $r = m\varepsilon \approx 0.58\ \Omega$ (fit: 0.60 Ω). *(d) Maximum current* $= \varepsilon/r \approx 21$ A (2 points). *(e) To measure $\varepsilon$ with the battery removed from the circuit, which voltmeter — low or high internal resistance?* **High** (1 point): the meter is itself the load, reads the p.d. across its own resistance, and the higher that resistance the smaller the current and the closer the reading to $\varepsilon$ (1 point). Part IV of this card, in one sentence.

### IB Physics HL May 2019 TZ1 Paper 2 Q1(d)–(e) — an electric bicycle, and the battery inside it [2 + 1 + 2]

*(d) The bicycle's meter shows a terminal p.d. of 12 V and a current of 6.5 A while the motor runs. The e.m.f. of the battery is 16 V. Determine the internal resistance.* *Tool: lost volts.* 4 V is dropped across the battery (or: total circuit resistance $= 16/6.5 = 2.46\ \Omega$ against an external $12/6.5 = 1.85\ \Omega$); $r = 4.0/6.5 = 0.62\ \Omega$.

*(e) The battery is ten identical cells: two parallel rows of five in series. Calculate (i) the e.m.f. of one cell* — cells in series add: $16/5 = 3.2$ V. *(ii) the internal resistance of one cell.* *Tool: series adds, parallel halves.* Each row has $5r_c$; two such rows in parallel give $5r_c/2 = 2.5\,r_c = 0.62$, so $r_c = 0.25\ \Omega$. The arrangement is the point: parallel rows *lower* the battery's internal resistance, which is exactly why a battery meant to deliver amperes is built wide as well as tall.

### IB Physics HL May 2021 TZ2 Paper 2 Q6 — a solar panel as a practical cell [2 + 3 + 3]

*A photovoltaic cell is modelled as a practical cell with internal resistance. At maximum sunlight: operating current 0.90 A, output p.d. 14.5 V, e.m.f. 21.0 V, panel 350 mm × 450 mm.*

*(a) Explain why the output p.d. and the e.m.f. differ.* There is a p.d. across (energy dissipated in) the internal resistance, **when there is a current** — the second half is a separate mark, and it is the physics: with no current the two would be equal.

*(b) Calculate the internal resistance.* *Tool: $\mathcal{E} = V + Ir$.* $21.0 = 14.5 + 0.90\,r$, so $r = 6.5/0.90 = 7.2\ \Omega$ (3 marks; the scheme awards all three for the bald correct answer).

*(c) With 680 W m⁻² incident, determine the efficiency (electrical power out ÷ solar power in).* Power in $= 680 \times 0.35 \times 0.45 = 107$ W; power out $= VI = 14.5 \times 0.90 = 13.1$ W; efficiency $= 0.12$, or **12 %**. Notice that the internal resistance eats $I^2 r = 5.8$ W on top of that — about a third as much again as the panel delivers. Real panels chase the load that maximises $VI$ continuously; that controller is the MPPT in "Where this is the working tool".

### Cambridge 9702 June 2025 Paper 23 Q7(b)(iii) — the null point moves [2]

*A potentiometer wire is driven by a 1.2 V cell of negligible internal resistance; cell X's e.m.f. is found from a null point 64 cm along the 150 cm wire (0.51 V). The driver cell is replaced by one of the same e.m.f. but with internal resistance that is not negligible. State and explain the effect on the null point.* *Tool: lost volts in the driver.* The driver now loses $Ir$ inside itself, so the p.d. across the wire is **lower** than 1.2 V (B1); a longer length is needed to balance the same 0.51 V, so the null point moves **to the right** (B1). Contrast the case the question does *not* ask: internal resistance in cell **X** would move nothing, because at balance no current flows through X.

---

## Where this is the working tool

**The starter motor.** A car's 12.6 V lead–acid battery has $r \approx 0.02\ \Omega$. The starter draws something like 150 A. The terminal p.d. during cranking is $12.6 - 150 \times 0.02 \approx 9.6$ V — which is why the headlights dim and the radio resets — and the battery dissipates $I^2 r = 450$ W inside itself for those two seconds. On a January morning $r$ may have doubled and the same starter gets 6–7 V: the engine turns over slowly and then not at all. Nothing about the *charge* in the battery changed overnight; the internal resistance did.

**Battery health.** Your phone's "maximum capacity" figure, an electric car's state-of-health, a warehouse's decision to retire a forklift battery: all are largely measurements of internal resistance, because $r$ climbs steadily as a cell ages while the open-circuit e.m.f. barely moves. A battery management system pulses a known current and reads the voltage sag — this card's experiment, run by a chip a thousand times a day. The phone that dies at 20 % is a cell whose $r$ has grown until the sag under the camera flash's current crosses the shutdown threshold.

**Jump-starting, in the right order.** A flat battery has a huge $r$; a good one a tiny $r$. Connect them in parallel and the good battery supplies the cranking current through *its* small $r$ while the flat one merely sits there. Engineers who size battery packs for electric vehicles put cells in parallel rows precisely to bring $r$ down, as the IB bicycle question above computes.

**High-voltage transmission.** Thévenin's theorem (below) says the grid seen from your socket is one e.m.f. and one internal resistance — and most of that resistance is *wire*. The power lost warming the line is $I^2 R_{\text{wire}}$, so the way to deliver a given power $P = VI$ with small loss is to send it at high voltage and low current: for fixed $P$ and $R_{\text{wire}}$ the loss scales as $P^2 R_{\text{wire}}/V^2$. Ten megawatts down a 5 Ω line at 10 kV means 1000 A and **5 MW** lost in the wire — half the power; the same ten megawatts at 400 kV means 25 A and **3 kW** lost. That factor of sixteen hundred is the entire reason for pylons, and for the transformers at each end that raise the voltage for the journey and lower it again for the house ([[Alternating Current]]). The wires are the grid's internal resistance, and the grid's answer to $Ir$ is to make $I$ small.

**Impedance matching.** Every aerial, every microphone, every audio power amplifier and every high-frequency cable is designed around the maximum power transfer theorem — the load is *made* to look like the source's internal resistance so that the signal power delivered is greatest, efficiency be hanged. Its opposite governs the grid: a generator's internal resistance is made as small as engineering allows, and no load ever comes near it.

**Solar maximum-power-point tracking (MPPT).** A photovoltaic panel's "internal resistance" is not constant — it depends on illumination and temperature — so the load resistance that extracts maximum power keeps changing. The controller between panel and battery continuously adjusts the effective load to sit at the peak of the power curve, which is the IB 2021 question turned into a product.

---

## Misconceptions

1. **"The e.m.f. is a force."** It is an energy per unit charge, in volts — the name is a nineteenth-century relic. Nothing in $V = \mathcal{E} - Ir$ has the units of a newton.
2. **"The terminal p.d. equals the e.m.f."** Only at zero current. Any current at all costs $Ir$; a battery driving a load always shows *less* than its label.
3. **"Internal resistance is a component I could remove."** It is the resistance of the source's own material and chemistry; $\mathcal{E}$ and $r$ are two parameters of one object and are never seen separately. You infer $r$ from how $V$ responds to $I$ — never by reading it.
4. **"A flat battery has no e.m.f."** Usually its e.m.f. is nearly normal and its $r$ has become large. That is why a flat battery reads fine on a high-resistance voltmeter and collapses the moment you ask for current.
5. **"Maximum power transfer means the best design."** It means 50 % efficiency. Match $R$ to $r$ for signals; make $R \gg r$ for energy. Confusing the two would build a power station that heats itself as much as the city.
6. **"A steeper $V$–$I$ line means a bigger e.m.f."** The gradient is $-r$; the e.m.f. is the intercept. A cell can have a large e.m.f. and a shallow line, or a small e.m.f. and a steep one.

---

## Beyond syllabus

### Thévenin's theorem — every source is $\mathcal{E}$ and $r$

The two-parameter model is far more general than a battery. **Thévenin's theorem** (1883, though Helmholtz had it in 1853) states that *any* network of sources and resistors, seen from two terminals, is equivalent to a single e.m.f. $\mathcal{E}_{\text{Th}}$ in series with a single resistance $r_{\text{Th}}$ — the open-circuit voltage and the resistance seen with every source replaced by a wire. A wall socket, a signal generator, a microphone, a solar array, a whole power grid at a substation: each has an internal resistance in exactly this card's sense, and each sags under load by exactly $Ir_{\text{Th}}$. The maximum power transfer theorem is then a statement about any source whatsoever, and "impedance matching" is Thévenin plus a load. (Norton's theorem is the same statement told with a current source in parallel with $r$; the two are interchangeable by $I_N = \mathcal{E}_{\text{Th}}/r_{\text{Th}}$.)

### When the line is not straight

Real sources deviate from the model in instructive ways. A **fuel cell** or a real photovoltaic cell has a $V$–$I$ curve with three regions: a steep initial drop (the reaction's activation barrier), a nearly straight middle (ohmic — this card), and a collapse at high current when reactants cannot reach the electrodes fast enough (concentration loss). A **lithium cell** has an internal resistance that depends on frequency: a fast pulse sees only the metal and electrolyte, a sustained current also pays for the slow diffusion of lithium into the electrodes. Battery engineers measure the whole frequency response — electrochemical impedance spectroscopy — and read the cell's state of health from its shape. In every case the straight line of Part II is the first-order model, and the deviations are where the chemistry shows.

---

## Hands-on

Everything here needs a cell, a digital multimeter, one resistor and a kitchen.

1. **Measure a cell's internal resistance with one resistor.** Read the open-circuit voltage $V_0$ of an AA cell with the multimeter (it draws almost nothing, so this is $\mathcal{E}$). Connect a known resistor — $R = 4.7\ \Omega$ is a good size — across the cell and read the terminal p.d. $V$ while it is connected. Then $I = V/R$ and $r = (V_0 - V)/I$. A fresh alkaline AA gives something near $0.2\ \Omega$; a used one from the TV remote may give $1\ \Omega$ or more. Disconnect quickly: $I^2 r$ is warming the cell while you read.
2. **Watch $r$ rise in the cold.** Put the same cell in the freezer for twenty minutes and repeat. The open-circuit voltage will barely change; $r$ will have risen noticeably. This is the phone-in-winter effect on your kitchen table.
3. **Fit the line properly.** With a few resistors (or a variable one) collect five or six $(I, V)$ pairs and fit them:

   ```python
   import numpy as np
   I = np.array([0.05, 0.10, 0.20, 0.30, 0.45])   # A
   V = np.array([1.53, 1.51, 1.47, 1.43, 1.37])   # V  (a fresh AA, say)
   m, c = np.polyfit(I, V, 1)                    # V = c + m I
   print(f"e.m.f. = {c:.3f} V, internal resistance = {-m:.3f} ohm, "
         f"short-circuit current = {c/-m:.1f} A")
   ```

   The gradient is $-r$ and the intercept is $\mathcal{E}$, exactly as in the figure. Try the AP 2015 data with $1/V$ against $1/R$ and recover 12.2 V and 0.60 Ω.
4. **Feel maximum power transfer.** With the cell's $r$ known, connect loads of about $r/3$, $r$ and $3r$ and compute $VI$ for each. The middle one wins, and it is also the one that warms the cell most.

---

## Exam Notes

### Cambridge 9702 — §10.1 Practical circuits (AS Paper 2, Paper 1 MCQs, and Paper 3)

- **LOs 3–5:** define e.m.f. as energy transferred per unit charge in driving charge around a complete circuit; **distinguish e.m.f. from p.d. in terms of energy** (source-side conversion *to* electrical vs component-side conversion *from* it); understand the effect of internal resistance on terminal p.d. LOs 1–2, circuit symbols and diagrams, are exercised in every circuit question.
- **Paper 2 shapes:** *define e.m.f.* (2 marks, both halves); *explain why the terminal p.d. is not constant / less than the e.m.f.* (3 marks, the chain of reasoning); *use a $V$–$I$ graph* — intercept, gradient, short-circuit current; *calculate $r$* from an e.m.f., a terminal p.d. and an external circuit (June 2024 P21 Q6 and P23 Q5 are twins); *sketch* a line for a cell with different $\mathcal{E}$ or $r$; the potentiometer *null point* argument (June 2025 P23 Q7).
- **Paper 3 (practical):** the $V$–$I$ experiment on a cell with a variable resistor is a standard Paper 3 task, marked on plotting, the straight line, gradient and intercept with units, and the discussion of why readings should be taken quickly.
- **Paper 1 MCQs** favour the short-circuit current, the lost volts at a given current, and the "which graph shows a larger $r$" comparison.

### AP Physics 2 (Unit 11) and AP Physics C: Electricity and Magnetism (Unit 11)

- Neither course has a separate learning objective for internal resistance; it appears **inside the circuit units** as a "non-ideal battery" — a resistor in series with an ideal e.m.f. — in 11.2 Simple Circuits and 11.5 Compound DC Circuits, and in experimental-design free-response questions.
- **AP C:** the 2015 Q2 above is the archetype — derive $V(R)$, **linearise**, plot, read $\varepsilon$ and $r$ from the line, and reason about the voltmeter's own resistance. 2022 Set 1 Q1(e) asks how replacing an ideal battery with a non-ideal one changes the slope and intercept of an experimental graph.
- **AP 2:** questions ask qualitatively how a non-ideal battery changes a measured resistance or a dissipated power (2017 Q, 2018 Q, 2024 Q3(d): replacing an ideal battery with one of internal resistance *reduces* the power in a load, because the terminal p.d. falls). Justify with $V = \varepsilon - Ir$ in words.

### IB Physics — B.5.1 and B.5.4 (Papers 1 and 2)

- B.5.1 defines e.m.f. and p.d. and asks for *real* vs ideal meters; B.5.4 lists **internal resistance, $\varepsilon = I(R + r)$** alongside series/parallel rules and potential dividers.
- Paper 2 shapes are the two above: *explain why terminal p.d. ≠ e.m.f.* (two marks — the p.d. across $r$, **when current flows**), *determine $r$* from readings, and cells combined in series-and-parallel arrays. IB likes a real source: a photovoltaic cell, a bicycle battery. The data booklet gives $\varepsilon = I(R + r)$.

### Not examined on…

- **Cambridge 0625 IGCSE** — §4.2.3 defines e.m.f. and p.d. and (Extended) uses $\mathcal{E} = W/Q$, but internal resistance and terminal p.d. are absent; the IGCSE cell is ideal.
- **9709 and 9231 Mathematics** — none; the maximum-power derivation is a routine [[Optimisation]] exercise in the maths syllabi but never framed as circuits.
- **AP Physics 1** — circuits are not in the course.
- **Computer science boards** — none.

---

## Quick reference

| Ask | Answer in one line |
|---|---|
| e.m.f. | energy transferred to each coulomb by the source, driving it round the complete circuit |
| terminal p.d. | energy per coulomb delivered to the external circuit: $V = \mathcal{E} - Ir$ |
| lost volts | $Ir$ — spent heating the source |
| closed-circuit law | $I = \mathcal{E}/(R + r)$ |
| $V$–$I$ graph | straight line; intercept $\mathcal{E}$, gradient $-r$, $I$-intercept $\mathcal{E}/r$ |
| short-circuit current | $\mathcal{E}/r$ — read off the graph, never measured |
| power bookkeeping | $\mathcal{E}I = I^2R + I^2r$ |
| maximum power in the load | at $R = r$; $P_{\max} = \mathcal{E}^2/4r$; efficiency then 50 % |
| efficiency | $R/(R + r)$ |
| cells in series / parallel | e.m.f.s add, $r$ adds / e.m.f. same, $r$ divides |
| measuring $\mathcal{E}$ exactly | draw no current: a very high-resistance voltmeter, or a null method |
| $r$ in the cold / with age | rises / rises — the e.m.f. barely changes |
| the label voltage | nominal, an average over discharge at a rated load — not the e.m.f. when full |
| why a short burns the cell | all of $\mathcal{E}^2/r$ is dissipated inside it |
| why the grid runs at 400 kV | wire loss $= P^2 R_{\text{wire}}/V^2$ — high $V$, low $I$, small $Ir$ |

---

## Connections

- **Parents:** [[Electric Current]] (current as the rate the source must sustain); [[Resistance]] (p.d. and e.m.f. defined as energies per unit charge, the ideal meters); [[Kirchhoff's Laws]] (the loop rule that makes $\mathcal{E} = IR + Ir$ one line).
- **Children:** [[Potential Dividers]] (the ratio route to $r$, and the sensor circuits that close Topic 10); [[Alternating Current]] (a source's internal *impedance*, and the transformer as the grid's way of keeping $I r$ small).
- **Cross-domain:** [[Optimisation]] — $P(R)$ maximised by calculus, the derivative that gives $R = r$; [[Work, Energy and Power]] — $\mathcal{E}I = I^2R + I^2r$ as an energy audit per second; [[Electromagnetic Induction]] — a generator is a source with internal resistance too, and its terminal p.d. sags under load for the same reason; [[Capacitors]] — a capacitor discharging through its own series resistance is the same model with a falling e.m.f.; [[Decouple and Recouple]] — a battery pack's parallel rows as decoupling the current from any one cell's $r$.
- **Misconception traps cleared:** e.m.f. is a force; terminal p.d. equals e.m.f.; $r$ is a removable component; a flat battery has no e.m.f.; maximum power is maximum efficiency; a steeper line is a bigger e.m.f.

## LaTeX reference

| Symbol | Meaning |
|---|---|
| $\mathcal{E}$ | e.m.f. of the source (V) — written $E$ on Cambridge papers, $\varepsilon$ on AP and IB |
| $r$ | internal resistance (Ω) |
| $V$ | terminal p.d. (V) |
| $R$ | external (load) resistance (Ω) |
| $I = \mathcal{E}/(R + r)$ | current in the closed circuit |
| $P = \mathcal{E}^2 R/(R + r)^2$ | power delivered to the load |
