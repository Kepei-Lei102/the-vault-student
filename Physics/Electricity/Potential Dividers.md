---
chinese: 分压器 (fēnyāqì) — 电位器、传感器电路与家用电安全
prerequisites:
  - "[[Resistance]]"
  - "[[Kirchhoff's Laws]]"
  - "[[Internal Resistance]]"
leads_to:
  - "[[Alternating Current]]"
  - "[[Sensors and Control Systems]]"
tags:
  - subject/physics
  - domain/electricity
  - level/IGCSE
  - level/A-Level
  - level/IB
  - curriculum/Cambridge-0625
  - curriculum/Cambridge-9702
  - curriculum/IB-Physics
  - syllabus/9702-10-3
  - syllabus/0625-4-3
  - syllabus/0625-4-4
  - type/deep
  - misconception/the-divider-formula-survives-a-load
  - misconception/a-thermistor-measures-temperature-by-itself
  - misconception/the-fuse-protects-the-person
---

# Potential Dividers 分压器

> *Every sensor you have ever used is two resistors in series. A supply across the pair, a tap between them, and the tap voltage is the supply shared in the ratio of the resistances. Make one resistor change with temperature, or light, or the angle of a thumbstick, and the tap voltage is a number a computer can read. That is the whole trick, and it runs the world.*

## Definition

### Formal

A **potential divider** is two (or more) resistances in series across a supply of p.d. $E$; the same current flows through both, so the supply is shared in proportion to the resistances. With the output taken across $R_2$:

$$V_{\text{out}} = E \cdot \frac{R_2}{R_1 + R_2}, \qquad \frac{V_1}{V_2} = \frac{R_1}{R_2}.$$

A **potentiometer** is a potential divider made of one uniform resistance wire (or track) with a sliding contact: the tap voltage is $E \cdot \dfrac{\text{tapped length}}{\text{whole length}}$, continuously adjustable. Used with a galvanometer in a **null method**, it compares an unknown e.m.f. with a known one while drawing no current from the unknown.

### Intuitive

Two resistors in series are two lengths of the same pipe in a row. The pressure drops along each in proportion to how long it is; tap in between and you read whatever fraction of the total drop has happened so far. A slider on a wire is the tap you can move. A thermistor in one arm is a pipe whose length changes with temperature: as it shortens, the tap moves nearer the supply and the reading rises.

### 中文锚点

游戏手柄的摇杆里有两个**电位器**——左右一个、上下一个：推摇杆就是在转一根碳膜电阻条上的滑片，滑片取到的电压从 0 变到满，芯片读这个电压就知道你推了多远；摇杆用久了"漂移"，正是那条碳膜被磨出了一道沟槽。这就是**分压器**：两个电阻串联接在电源上，中间引出一根线，电流一样，所以电压按电阻之比分——$V_{\text{out}} = E\,R_2/(R_1+R_2)$，或者说 $V_1 : V_2 = R_1 : R_2$。把其中一个电阻换成**热敏电阻**（温度升高电阻变小）或**光敏电阻**（变亮电阻变小），中间那根线上的电压就跟着温度、光线变——手机电池边上测温的小探头、天黑自动亮的路灯、恒温器，全是这个电路加一个开关或一个模数转换器。这张卡讲四件事：**公式从哪来**（同一电流，$V=IR$，两式相除）；**它最常见的坑**——一接上负载（比如一个电阻不大的电压表），输出电压就掉，因为负载和 $R_2$ 并联把下臂的电阻拉低了；**电位差计当天平用**（9702 §10.3 要考的"零示法"：调到检流计指零，这时不从待测电池取电流，内阻上没有电压损失，读到的就是它真正的电动势）；最后是 0625 要考的**家用电安全**——火线、零线、地线各干什么，保险丝为什么装在火线上、怎么选额定电流，金属外壳为什么要接地或者做成双重绝缘。

| English | 中文 | 一句话 |
|---|---|---|
| Potential divider | 分压器 | 串联的两个电阻按电阻之比分电压 |
| Potentiometer | 电位器 / 电位差计 | 一根电阻丝加一个滑片：连续可调的分压器；同一个词也指用它比较电动势的仪器 |
| Thermistor (NTC) | 热敏电阻（负温度系数） | 温度升高，电阻下降 |
| Light-dependent resistor (LDR) | 光敏电阻 | 光变亮，电阻下降 |
| Loading | 负载效应 | 接上负载后输出电压下降 |
| Null method | 零示法 / 补偿法 | 检流计读零时不取电流，测得真实电动势 |
| Galvanometer | 检流计 | 灵敏的电流计，零点在中央 |
| Live / neutral / earth | 火线 / 零线 / 地线 | 230 V / 回路 / 接大地的安全线 |
| Fuse · trip switch | 保险丝 · 断路器 | 电流过大就熔断 / 跳闸 |
| Double insulation | 双重绝缘 | 塑料外壳，不需要地线 |

---

## Part I — The formula, and where it comes from

![[potential-dividers-circuit.svg|900]]

*Tool: [[Kirchhoff's Laws]], both of them.* The junction rule says that with nothing connected at the tap, the current $I$ through $R_1$ is the current through $R_2$. The loop rule says the two drops add up to the supply: $E = IR_1 + IR_2$, so $I = E/(R_1 + R_2)$. Then the drop across $R_2$ is

$$V_{\text{out}} = IR_2 = E \cdot \frac{R_2}{R_1 + R_2},$$

and dividing $V_1 = IR_1$ by $V_2 = IR_2$ kills the current: $V_1/V_2 = R_1/R_2$. That ratio form is the one 0625 prints; the fraction form is the one you use. Two limits check it: $R_2 \to 0$ gives $V_{\text{out}} \to 0$ (a short takes no voltage); $R_2 \gg R_1$ gives $V_{\text{out}} \to E$ (the big resistor takes almost all of it). The larger resistance takes the larger share — always.

A **variable** divider replaces the pair by a single track with a slider: a uniform wire has resistance proportional to length ([[Resistance]], $R = \rho L/A$), so the tapped fraction of the length is the tapped fraction of the voltage. Turn the knob to the end and you have $0$ or $E$; anywhere between and you have anything between. The syllabus calls this "the action of a variable potential divider"; the shop calls it a potentiometer, and a car's fuel gauge, a volume knob and both axes of a thumbstick are the same component.

![[potential-dividers-slider.mp4]]

*The clip: the slider moves along the wire and the tap voltage follows the tapped fraction; then the top arm becomes a thermistor, and warming it moves the voltage without anyone touching a slider.*

---

## Part II — Sensors: making one arm change

Replace one resistor by a component whose resistance responds to the world, and the tap voltage becomes a measurement.

**The thermistor.** The NTC kind every syllabus means has a resistance that *falls* as temperature rises — from around $10\ \text{k}\Omega$ at $25\ °\text{C}$ to a few hundred ohms in boiling water, roughly exponentially. Put it in the *top* arm with a fixed resistor below, and warming it takes a smaller share, so $V_{\text{out}}$ across the fixed resistor *rises* with temperature. Put it in the *bottom* arm and $V_{\text{out}}$ across it *falls* instead. The exam will ask which; work it from "the larger resistance takes the larger share".

![[potential-dividers-thermistor-circuit.svg|900]]

*The circuit, read at three temperatures: cold, the thermistor is 33 kΩ and takes most of the 5 V, leaving 1.2 V for the fixed resistor; at room temperature the two are equal and split it 2.5 V each; hot, the thermistor has shrunk to 2.5 kΩ and the fixed resistor takes 4.0 V.*

Now run the temperature continuously, and try three different fixed resistors against the same thermistor:

![[potential-dividers-sensor-curve.svg|860]]

*$V_{\text{out}}$ against temperature. The curve is steepest — the sensor most sensitive — around the temperature where the fixed resistor equals the thermistor's resistance, and flat far from it. So choosing the fixed resistor is choosing the temperature you care about: 1 kΩ for hot water, 10 kΩ for a room, 100 kΩ for a freezer.*

**The light-dependent resistor** has a resistance that falls as light intensity rises — megohms in the dark, a few hundred ohms in daylight. Same circuit, same logic: the LDR's share shrinks as the light comes up, and the fixed resistor is chosen for the light level at which the switch should flip.

Why a divider at all, rather than reading the thermistor's resistance directly? Because the things that *use* the measurement — a comparator, a microcontroller's analogue input, a transistor — read **voltages**, not resistances. The divider converts a resistance into a voltage against a fixed reference, and that voltage can be compared with a threshold ("above 25 °C, switch the fan on") or digitised. A thermostat is a thermistor divider and a switch; the temperature sensor beside your phone's battery is a thermistor divider and an analogue-to-digital converter; a streetlight is an LDR divider and a relay. [[Sensors and Control Systems]] takes the story from the tap voltage onward.

---

## Part III — The catch: loading

The formula assumes the tap draws no current. Connect anything across $V_{\text{out}}$ — a lamp, the next stage of a circuit, even a voltmeter — and that thing is in **parallel** with $R_2$. The lower arm's resistance falls, its share falls, and $V_{\text{out}}$ drops below the formula's value. A $10\ \text{k}\Omega$/$10\ \text{k}\Omega$ divider on 9 V promises 4.5 V; load it with $10\ \text{k}\Omega$ and the lower arm becomes $5\ \text{k}\Omega$ against $10\ \text{k}\Omega$, so it delivers 3.0 V; load it with $1\ \text{k}\Omega$ and it delivers 0.75 V.

![[potential-dividers-loading.svg|860]]

*What the tap actually delivers, against the resistance of whatever is connected across it (log scale). Far right: a 10 MΩ voltmeter barely disturbs the divider and reads 4.50 V, the formula's promise. Moving left, the load's resistance falls toward $R_2$'s and below: the load in parallel with $R_2$ drags the lower arm's resistance down, its share of the 9 V falls with it, and the tap sags to 3.0 V at a 10 kΩ load and 0.75 V at 1 kΩ. The dashed line is the formula; the red curve is reality; the gap between them is the loading effect.*

Two consequences run through every practical circuit:

- **Voltmeters must have very high resistance.** A $10\ \text{M}\Omega$ meter across that divider reads 4.50 V, within a hundredth; an old $1\ \text{k}\Omega$-per-volt moving-coil meter would read something else entirely and *change the circuit it was measuring*. This is the [[Internal Resistance]] argument from the other side: there, the source's own resistance sagged the terminal p.d.; here, the divider's Thévenin resistance ($R_1 \parallel R_2$) is a source resistance the load sees.
- **A divider is a signal, not a power supply.** It can set a *voltage* for something that draws almost no current — a comparator input, a transistor base, a chip's reference pin. It cannot run a motor: the motor loads it to nothing and the resistors heat up. To *drive* a load at a chosen voltage you use a regulator or a transistor controlled by the divider, which is what every real circuit does.

> [!tip] The exam's version of loading
> Cambridge's favourite: a switch connects a third resistor in parallel with one arm (the June 2023 IGCSE question below). Closing it lowers that arm's resistance, and the voltmeter across it falls — from 7.5 V to a value you compute by redoing the divider with the parallel combination. Reason it before calculating: the arm got smaller, so its share got smaller.

---

## Part IV — The potentiometer as a balance: the null method

A voltmeter across a cell reads the *terminal* p.d., which is below the e.m.f. by $Ir$ the moment the meter draws current ([[Internal Resistance]]). To read the e.m.f. itself you need a method that draws **no current** at the instant of reading. That is what "recall and use the principle of the potentiometer as a means of comparing potential differences" and "the use of a galvanometer in null methods" are asking for.

![[potential-dividers-null.svg|900]]

A driver cell of known e.m.f. $E_0$ sends a steady current down a uniform wire $AB$, so the p.d. per centimetre along it is constant. The unknown cell $X$ is connected, **positive to positive** — its positive terminal to $A$, the same end the driver's positive feeds — from $A$ through a **galvanometer** (a sensitive centre-zero ammeter) to a sliding contact on the wire.

Look at the lower loop, $A \to X \to G \to C \to$ back along the wire to $A$. It contains two sources pushing **against** each other: cell $X$ with its e.m.f. $E$, and the section $AC$ of the wire, across which the driver maintains a p.d. $V_{AC}$ with the same polarity. *Tool: the loop rule.* The current through the galvanometer is set by the *difference*: $I_G = (E - V_{AC}) / (r_X + R_G)$. If $E > V_{AC}$ the current flows one way, if $E < V_{AC}$ the other, and the needle tells you which. Slide until it reads **zero**: at that point $C$ the two sources cancel exactly, $E = V_{AC}$, no current flows through $X$, its internal resistance drops nothing, and

$$E = E_0 \cdot \frac{AC}{AB}.$$

So yes — the two cells are back to back, and the balance point is where they cancel; the galvanometer is the balance's pointer, and a "null" reading is the pointer at centre. The wire's resistance never appears — only the *ratio of lengths*, which is why the method is a comparison and why it is accurate: a length is easy to measure well and a galvanometer's zero is easy to see. The June 2025 question below turns the screw: if the *driver* cell has internal resistance, the p.d. across the whole wire is less than $E_0$, so each centimetre carries less, and the balance point moves *further along* to make up the same $E$.

The same principle, replacing the galvanometer by an amplifier that adjusts the tap automatically until the difference is zero, is how a digital voltmeter and an analogue-to-digital converter actually read a voltage without disturbing it. The null method is not a museum piece; it is the reason the meter in Part III can be $10\ \text{M}\Omega$.

---

## Part V — Where the divider meets the wall: mains safety

The IGCSE puts electrical safety beside the divider, and the link is real: the house wiring is a supply with a load across it, and everything that goes wrong is a current going where the divider did not intend.

![[potential-dividers-mains.svg|900]]

- **Three wires.** The **live** (line) wire carries the supply — 230 V r.m.s. in China, the UK and most of the world; 110–120 V in the Americas and Japan — and its potential swings between about $+325$ V and $-325$ V fifty times a second ([[Alternating Current]]). The **neutral** returns the current at about 0 V. The **earth** is a wire to the ground itself, at 0 V, which normally carries nothing at all.
- **The switch goes in the live wire.** Switch the neutral instead and the appliance stops working but its insides stay at 230 V, waiting for a hand. Switching the live leaves nothing live beyond the switch. Every plug's fuse is in the live wire for the same reason.
- **The fuse** is a short thin wire that melts when the current exceeds its rating, breaking the circuit before the cable overheats. Choose the **next standard rating above the normal current**: a 2 kW heater at 230 V draws 8.7 A, so 3 A and 5 A fuses would melt in normal use and a 13 A fuse would allow 12 A of fault current to flow without melting — 10 A is right. A **trip switch** (circuit breaker) is a resettable fuse, an electromagnet that opens the contacts above a set current.
- **The earth wire and the metal case.** If a live wire inside a metal-cased appliance touches the case, the case is at 230 V. With an earth wire bolted to it, a large current flows live → case → earth, and the fuse melts: the case is made safe by being *shorted to ground*. Without one, the case sits live; a person touching it completes the circuit through their body, and the 30 mA that can stop a heart is far below any fuse rating. **The fuse protects the wiring; the earth wire protects the person.**
- **Double insulation.** An appliance in a plastic case with no exposed metal — the ⧈ symbol on the label — cannot have a live case, so it needs no earth wire; its fuse still protects the cable. Hair dryers, phone chargers and power tools are built this way.
- **The four hazards** the syllabus lists are the four ways a current escapes the circuit: damaged insulation (live conductor exposed), overheating cables (too much current for the copper, melting insulation), damp conditions (water lowers the resistance of a path through a person), and overloaded sockets (many appliances drawing through one cable rated for one).

---

## Worked examples — real papers from three boards, every mark point named

### Cambridge 9702 June 2023 Paper 21 Q7 — the thermistor divider [2 + 2 + 2 + 3]

A 9.6 V battery of negligible internal resistance drives a $5800\ \Omega$ resistor, a $3400\ \Omega$ resistor and a thermistor in series; a voltmeter across the $3400\ \Omega$ resistor and the thermistor together reads 6.0 V.

*(a) Current in the 5800 Ω resistor.* *Tool: the loop rule* — the $5800\ \Omega$ resistor has the rest of the e.m.f.: $9.6 - 6.0 = 3.6$ V, so $I = 3.6/5800 = 6.2 \times 10^{-4}$ A. *(b) Resistance of the thermistor.* *Tool: $V = IR$ on the 6.0 V pair* — $6.0 = 6.2 \times 10^{-4}(3400 + R)$, $R = 6.3\ \text{k}\Omega$ (or on the whole loop: $9.6 = I(3400 + 5800 + R)$, same answer). *(c) Energy left after 330 C has passed.* $\Delta E = \mathcal{E}Q = 9.6 \times 330 = 3170$ J, so $2.6 \times 10^4 - 3170 = 2.3 \times 10^4$ J. *(d) The thermistor's resistance increases; state the change to its temperature, its current, its p.d.* Temperature **decreases** (NTC); the total resistance rose, so the current **decreases**; and the thermistor is now a larger share of the loop, so its p.d. **increases** — "the larger resistance takes the larger share", even though the current fell.

### Cambridge 9702 June 2022 Paper 21 Q6(c) — the LDR divider [1 + 2 + 2]

A 9.0 V battery, an LDR and a fixed $1800\ \Omega$ resistor in series; the voltmeter across the fixed resistor reads 5.4 V. *(i)* $I = 5.4/1800 = 3.0 \times 10^{-3}$ A. *(ii)* *Tool: the divider ratio* — $5.4/9.0 = 1800/(1800 + R_L)$, so $R_L = 1200\ \Omega$ (or $(9.0 - 5.4)/3.0 \times 10^{-3}$). *(iii) The light intensity increases; explain the change in the voltmeter reading by reference to the current.* The LDR's resistance **decreases** (B1); the total resistance falls so the current **increases**, and the fixed resistor's p.d. $IR$ **increases** (B1). Both marks are for the chain, not the conclusion.

### Cambridge 9702 June 2025 Paper 23 Q7 — the potentiometer, and a null method [3 + 1 + 2 + 2]

A nichrome wire of length 150 cm, area $2.45 \times 10^{-7}\ \text{m}^2$, resistivity $1.12 \times 10^{-6}\ \Omega\,\text{m}$; a 1.2 V driver cell; cell $X$ balanced at 64 cm. *(a)* $R = \rho L/A = 6.86\ \Omega$ — three significant figures demanded, and the length in metres. *(b)(i) What is meant by a null method:* a method in which the **galvanometer reading is zero** (B1). *(ii)* $E/1.2 = 64/150$, $E = 0.51$ V. *(iii) The driver cell now has internal resistance; effect on the null point.* The terminal p.d. across the wire is **lower** (B1), so a longer length is needed to balance the same $E$: the null point **moves to the right** (B1). Note what is *not* affected — the unknown cell's own internal resistance never mattered, because at balance it carries no current.

### Cambridge 9702 November 2022 Paper 21 Q5(c)–(d) — a potentiometer driving two lamps [1 + 2 + 2 + 2]

A 12.0 V battery across a linear potentiometer $AB$; lamp $P$ from $A$ to the slider, lamp $Q$ from the slider to $B$; slider at the midpoint, battery current 1.78 A; the lamps share a given $I$–$V$ characteristic. *(i)* Each lamp has 6.0 V across it, and the characteristic gives $I_P = 1.55$ A. *(ii)* $P = VI \times 2 = 6.0 \times 1.55 \times 2 = 19$ W. *(iii) The potentiometer's resistance between A and B:* the battery current splits between the lamps' path and the potentiometer's own track — *tool: the junction rule* — so the track carries $1.78 - 1.55 = 0.23$ A across 12.0 V: $R = 52\ \Omega$. *(d) Slider moved to end A.* Lamp $P$ now has both ends at the same potential: its p.d. falls to zero and it goes out; lamp $Q$ has the full 12 V and brightens. This is the divider with the slider at the extreme, read as two lamps rather than one voltmeter.

### Cambridge 0625 June 2023 Paper 41 Q7 — the divider, and a switch that loads it [2 + 1 + 3 + 2]

Three $40\ \Omega$ resistors: $R_1$ and $R_2$ in series across a battery, a voltmeter across $R_1$, and $R_3$ across $R_2$ through an open switch. *(a) What is meant by a potential divider:* two of — it **splits the e.m.f.** of the source; between **components in series**; **in proportion to their resistances**. *(b)(i)* The voltmeter reads 7.5 V across one of two equal resistors, so the e.m.f. is **15 V**. *(ii) Switch closed; resistance of the whole circuit.* $R_2 \parallel R_3 = 20\ \Omega$ (C1); total $40 + 20 = 60\ \Omega$ (A). *(c) Voltmeter reading with the switch closed.* *Tool: the ratio* — $R_1$ is now 40 of 60, so it takes $15 \times 40/60 = 10$ V (or $I = 0.25$ A and $V = 0.25 \times 40$). The lower arm was loaded, its share fell from half to a third, and $R_1$'s rose from 7.5 V to 10 V. Part III in five marks.

### Cambridge 0625 March 2024 Paper 42 Q7 — symbol, formula, charge [1 + 2 + 2]

*(a)* The potential-divider symbol: a resistor with an arrow-headed tap. *(b)(i)* $V_{\text{out}}$ across a $1.0\ \text{k}\Omega$ resistor in series with $R = 3.0\ \text{k}\Omega$ on 6.0 V: $6.0 \times 1/(1 + 3) = 1.5$ V — the scheme's route is $V_{\text{out}}/V_R = R_{\text{out}}/R$. *(ii)* At 1.7 mA for 300 s, $Q = It = 0.51$ C.

### Cambridge 0625 November 2024 Paper 41 Q6 — LDR and thermistor in one divider [2 + 1 + 1 + 3]

An LDR and a thermistor in series across a supply of e.m.f. $E$; the voltmeter across the LDR. *(a) Define p.d.:* **work done per unit charge** through the component. *(b) The p.d. across the thermistor:* $E$ minus the voltmeter reading — the loop rule in one line. *(c) The LDR's resistance decreases and the thermistor's increases: (i) what changed in the room?* Brighter **and** cooler — both conditions, one mark. *(ii) The voltmeter reading and why.* It **decreases**; the e.m.f. is constant, the LDR is now a smaller fraction of the total resistance, so it takes a smaller fraction of $E$ — the scheme accepts $R_1/R_2 = V_1/V_2$ stated as the reason.

### Cambridge 0625 June 2025 Paper 41 Q4(b) — choosing a fuse [2 + 2]

A 2.0 kW heater on a 230 V mains. *(i)* $I = P/V = 2000/230 \approx 8.7$ A. *(ii) Which of 3 A, 5 A, 10 A, 13 A?* **10 A**, and one reason: a smaller fuse melts in normal use; a larger one lets too much current flow without melting; the rating must be *above* the normal current. Two marks for the number *and* the reason together.

### IB Physics HL May 2018 TZ2 Paper 2 Q4 — the potentiometer, IB style [2 + 2 + 2]

A 12 V cell across a 1.0 m wire of resistance $80\ \Omega$; cell $X$ balanced at $AC = 0.35$ m. *(a) What is meant by e.m.f.:* the **work done per unit charge** in moving charge round the circuit — the scheme refuses "the p.d. across the terminals" unless "with no current flowing" is added, which is exactly [[Internal Resistance]]'s distinction. *(b)(i) Show $R_{AC} = 28\ \Omega$:* resistance is proportional to length, $0.35 \times 80$. *(ii) Determine E:* the driver current is $12/80 = 0.15$ A, so $E = 0.15 \times 28 = 4.2$ V — or, in one step, $E = 12 \times 28/80$. Same physics as the 9702 question, with the resistance made explicit instead of cancelling.

### IB Physics HL November 2020 Paper 2 Q5(c) — a divider versus a series rheostat [1 + 3]

A non-ohmic component $X$ on a 4.0 V cell, first in series with a variable resistor, then across the slider of a potentiometer. *(i) The range of current the ammeter can measure as the slider moves from Q to P:* **0 to 60 mA** — the divider reaches *zero* volts at one end, which a series rheostat never can (it can only add resistance, never remove the cell). *(ii) The power, without calculation:* the potentiometer draws its own current through the section of track in parallel with $X$, so the cell's current exceeds the 20 mA in $X$ and the total power is **greater** than with the rheostat. That is the trade the divider makes: full control of the voltage, at the price of a standing current through the track.

---

## Where this is the working tool

- **Every analogue input on a microcontroller.** An Arduino's `analogRead` returns a number from 0 to 1023 proportional to a pin voltage; a thermistor, an LDR, a potentiometer or a flex sensor becomes a reading by being one arm of a divider against a fixed resistor. Choosing that fixed resistor to match the sensor at the operating point (the left plot in Part II) is the first design decision in every such circuit.
- **Thumbsticks and knobs.** A game controller's stick is two potentiometers at right angles, read as two voltages; the wheel of a scroll mouse, the throttle of an electric bike, the volume of a guitar amplifier are single ones. "Stick drift" is the carbon track worn where it rests, so the divider's ratio at the centre is no longer half.
- **Battery temperature.** The thermistor pressed against a phone's battery, read through a divider by the charge controller, is what stops fast charging when the cell is hot and what refuses to charge below 0 °C — the same physics as [[Internal Resistance]]'s cold-battery shutdown, measured rather than suffered.
- **The oscilloscope's 10× probe** is a $9\ \text{M}\Omega$ resistor in the probe tip against the scope's $1\ \text{M}\Omega$ input: a divider that shows the scope a tenth of the signal so that a 300 V waveform can be looked at, and loads the circuit under test ten times less than a bare lead.
- **Reference voltages.** A regulator chip sets its output by comparing a divider tap on that output with an internal 1.25 V reference and adjusting until they match — the null method with an amplifier for a galvanometer, running continuously inside every phone charger.
- **The house.** Live, neutral, earth, the fuse in the live, the earth to the case: Part V is the one section of this card that a student will meet with a screwdriver.

---

## Misconceptions

1. **"$V_{\text{out}} = E R_2/(R_1 + R_2)$ is what the load gets."** It is what the *tap* would give with nothing attached. Any load is in parallel with $R_2$ and pulls the output down; the formula holds only for loads much larger than $R_2$.
2. **"The thermistor measures the temperature."** A thermistor's *resistance* changes; on its own nothing reads it. The divider turns that resistance into a voltage against a fixed reference, and the voltage is what a comparator or an ADC reads.
3. **"Bigger resistance, bigger current, bigger voltage."** In a series divider the current is the same through both arms, so the arm with the *larger* resistance takes the *larger* p.d. — even when a change that raises its resistance lowers the current, its p.d. rises (the June 2023 question, part d).
4. **"A potentiometer is just a variable resistor."** Wired with three terminals it is a divider whose output runs from 0 to $E$; wired with two it is a rheostat, which can only add resistance in series and can never bring the load's voltage to zero (the IB November 2020 question).
5. **"The fuse protects you."** It protects the *cable* from fire. The current that kills is tens of milliamps, far below any fuse rating; what protects the person is the earth wire (or double insulation), which makes a fault current large enough to blow the fuse *instead* of flowing through a hand.
6. **"The switch can go in either wire."** In the neutral it stops the appliance and leaves it live inside; the live wire is the only correct place for both the switch and the fuse.

---

## Hands-on

1. **Build the divider.** Two resistors, a battery, a multimeter: predict $V_{\text{out}}$ from the formula, measure it, then clip a third resistor across the lower arm and watch it fall. Compute the new value with the parallel combination and match it — Part III in ten minutes.
2. **Make a thermometer.** A $10\ \text{k}\Omega$ thermistor and a $10\ \text{k}\Omega$ resistor on 5 V (an Arduino or a phone charger through a USB breakout will do). Read the tap with the meter; hold the thermistor between finger and thumb; put it in iced water. Then swap the fixed resistor for $1\ \text{k}\Omega$ and see the sensitivity move to a different temperature range, as in the left plot.
3. **Open a controller.** A worn game controller's thumbstick module has two potentiometers with three pins each; with the stick centred, the middle pin against either outer pin reads about half the supply — or, if it drifts, doesn't.
4. **Read a plug.** Take the back off a fused plug: brown to the fuse and the live pin, blue to neutral, green-and-yellow to the longer earth pin. Find the fuse rating and check it against the appliance's power on the label, as in the June 2025 question.

---

## Exam Notes

### Cambridge 9702 — §10.3 Potential dividers (AS Paper 2, and Paper 3 practical)

- **The LO list:** the principle of a potential divider circuit; the principle of the **potentiometer** as a means of **comparing** potential differences; the use of a **galvanometer in null methods**; thermistors and LDRs in dividers to give a p.d. dependent on temperature and light intensity.
- **Question shapes:** find a current from the p.d. across one arm, then the unknown resistance (2 + 2); state the direction of change of a quantity when the sensor's resistance changes and *explain by reference to the current* (2–3); the potentiometer with a length ratio (2) and a qualitative twist about internal resistance moving the null point (2); occasionally two lamps or a slider at an extreme (November 2022). Paper 3 sets the wire potentiometer as a practical.
- With §10.1 ([[Internal Resistance]]) and §10.2 ([[Kirchhoff's Laws]]) this completes Topic 10.

### Cambridge 0625 — §4.3.3 and §4.4 (Paper 4 Extended; §4.4 Core on Paper 3 too)

- **§4.3.3:** the p.d. across a conductor rises with its resistance at constant current (Core); describe the action of a **variable potential divider** and recall and use $R_1/R_2 = V_1/V_2$ (Supplement). Thermistors (NTC only) and LDRs are §4.3.1 components whose *behaviour* you must know.
- **§4.4:** the four hazards; live, neutral and earth and why the switch is in the live; **fuses and trip switches** with the choice of rating; earthing or **double insulation** of the case; a fuse without an earth protecting the circuit and cabling of a double-insulated appliance.
- **Question shapes:** "what is meant by a potential divider" (2); a numerical divider with a switch that adds a parallel resistor (3–5); an LDR/thermistor divider with a qualitative change (3–4); choose the fuse and justify (2); why earth / why the switch in the live (2 each).

### IB Physics — B.5.4

- Potential dividers with thermistors and LDRs, and the potentiometer as a comparator, sit in B.5.4 alongside the series/parallel rules and internal resistance; the two Paper 2 questions above show the register — the potentiometer with the wire's resistance made explicit, and the divider contrasted with a series rheostat on range and power.

### Not examined on…

- **AP Physics 2 and AP Physics C (E&M)** — no potentiometer, no thermistor or LDR sensor circuits, no mains safety; a two-resistor divider appears only as an ordinary series circuit under [[Kirchhoff's Laws]]'s rows.
- **Cambridge 9709 / 9231 and the other maths boards** — nothing.
- **0478 / 9618 Computer Science** — the *use* of sensor readings by a controller is [[Sensors and Control Systems]]; the divider itself is not examined.

---

## Quick reference

| Ask | Answer in one line |
|---|---|
| the formula | $V_{\text{out}} = E\,R_2/(R_1 + R_2)$; equivalently $V_1 : V_2 = R_1 : R_2$ |
| which arm takes more | the larger resistance, always — same current, $V = IR$ |
| thermistor / LDR | NTC: resistance falls as it warms; LDR: resistance falls as it brightens; the sensor's *share* of $E$ falls with it |
| loading | a load across $V_{\text{out}}$ is parallel to $R_2$, lowers its share; keep $R_{\text{load}} \gg R_2$; voltmeters $\sim 10\ \text{M}\Omega$ |
| potentiometer | a uniform track with a slider: $V = E \cdot (\text{tapped length} / \text{whole})$, from 0 to $E$ |
| null method | slide until the galvanometer reads zero; $E = E_0 \cdot AC/AB$; no current drawn, so internal resistance of $X$ is bypassed |
| driver cell has $r$ | p.d. across the wire falls, so the null point moves further along |
| fuse rating | the next standard value above the normal current; in the live wire |
| earth wire | holds a metal case at 0 V; a fault current blows the fuse instead of flowing through a person |
| double insulation | plastic case, no earth needed; fuse still protects the cable |

---

## Connections

- **Parents:** [[Resistance]] — $R = \rho L/A$, the reason a uniform wire's tapped length is its tapped voltage, and the thermistor and LDR characteristics; [[Kirchhoff's Laws]] — the junction rule (same current, no current at the tap) and the loop rule (the two drops sum to $E$) that derive the formula in two lines; [[Internal Resistance]] — why a voltmeter reads below the e.m.f., which is the null method's reason to exist, and why the driver cell's $r$ moves the balance point.
- **Children:** [[Alternating Current]] — the 230 V that swings between $\pm 325$ V, and the transformer that made it 230 V; [[Sensors and Control Systems]] — what happens after the tap: comparators, ADCs, the control loop.
- **Cross-domain:** [[Decouple and Recouple]] — the divider as an interface, converting a resistance the world changes into a voltage a chip can read, the two sides coupled only through that one number; [[Input and Output Devices]] — the joystick and the sensor as the electronics of an input device; [[The True IO Bound]] — the ADC that reads the tap is the point where the physical world becomes bytes.
- **Misconception traps cleared:** the divider formula survives a load; a thermistor measures temperature by itself; bigger resistance means bigger current; a potentiometer is just a variable resistor; the fuse protects the person; the switch can go in either wire.

## Sources

- Cambridge 9702 syllabus 2028–30, §10.3; Cambridge 0625 syllabus 2026–28, §4.3.3 and §4.4. Question papers and mark schemes: 9702/21 June 2023 Q7, 9702/21 June 2022 Q6, 9702/23 June 2025 Q7, 9702/21 November 2022 Q5; 0625/41 June 2023 Q7, 0625/42 March 2024 Q7, 0625/41 November 2024 Q6, 0625/41 June 2025 Q4; IB Physics HL Paper 2 May 2018 TZ2 Q4 and November 2020 Q5.
- Thermistor curve: the Steinhart–Hart / β-parameter model with $R_{25} = 10\ \text{k}\Omega$, $B = 3950$ K — the commonest hobby NTC.
- Mains figures: 230 V r.m.s. (GB/T 156-2017 in China; BS 7671 in the UK), peak $230\sqrt{2} \approx 325$ V; the 30 mA threshold is the IEC 60479 ventricular-fibrillation figure that residual-current devices are set to.
