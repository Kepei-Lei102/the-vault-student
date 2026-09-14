---
chinese: 交变电流 (jiāobiàn diànliú) — 有效值、整流与滤波、相量与阻抗
prerequisites:
  - "[[Electromagnetic Induction]]"
  - "[[Resistance]]"
  - "[[Capacitors]]"
  - "[[Simple Harmonic Motion]]"
  - "[[Complex Numbers]]"
  - "[[Internal Resistance]]"
  - "[[Potential Dividers]]"
leads_to:
  - "[[Resonance]]"
tags:
  - subject/physics
  - domain/electricity
  - domain/electromagnetism
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-9702
  - curriculum/Cambridge-0625
  - curriculum/A-Level
  - syllabus/9702-21-1
  - syllabus/9702-21-2
  - syllabus/0625-4-2
  - type/deep
  - misconception/rms-is-the-average
  - misconception/mean-power-is-half-because-half-the-time
  - misconception/the-capacitor-blocks-the-ripple
  - misconception/the-diode-only-deletes-the-negative-half
---

# Alternating Current 交变电流

> *The current in the wall changes direction a hundred times a second and spends, on average, no time at all flowing anywhere. Yet the kettle boils. This card is about the number that explains that, the four diodes that turn the slosh into a one-way flow, and the moment — just past the syllabus — when the imaginary number stops being a game and becomes the working language of every circuit that hums.*

## Definition

### Formal

An **alternating current** (a.c.) is a current whose direction reverses periodically; the mains supply is **sinusoidal**, $I = I_0 \sin \omega t$ and $V = V_0 \sin \omega t$, where $I_0$, $V_0$ are the **peak** values, $\omega = 2\pi f$ is the angular frequency, $f = 1/T$ the **frequency** and $T$ the **period**. The **root-mean-square** value is the steady (d.c.) value that would deliver the same mean power to a resistor; for a sinusoid $I_{\text{rms}} = I_0/\sqrt2$ and $V_{\text{rms}} = V_0/\sqrt2$, and the **mean power** in a resistive load is **half the peak power**, $\langle P \rangle = \tfrac12 I_0^2 R = I_{\text{rms}}^2 R$.

**Rectification** converts a.c. to d.c.: a single diode passes only one half of each cycle (**half-wave**); four diodes in a **bridge** steer both halves through the load in the same direction (**full-wave**). A capacitor across the load **smooths** the output, discharging through the load between peaks; the ripple is small when the time constant $RC$ is large compared with the period.

### Intuitive

A d.c. current is a river; an a.c. current is a tide. Nothing travels far — an electron in a mains wire shuffles back and forth over a fraction of a millimetre — but energy still arrives, because a resistor does not care which way the charge moves: it heats on $I^2$, and a square is positive both ways. That is why the sensible way to name an a.c. is not its average (zero) or its peak (only reached for an instant) but the d.c. that would heat equally: the r.m.s. value. Rectification is turning the tide into a river with one-way gates (diodes); smoothing is adding a reservoir (the capacitor) that keeps the river running between tides.

### 中文锚点

墙上插座里的电不是朝一个方向流的，而是来回**晃**：在中国，电流每秒换向一百次（每秒五十个周期，50 Hz），电压在 +311 V 和 −311 V 之间摆动。那为什么标签上写的是 220 V？因为 220 V 是**有效值**（root-mean-square，r.m.s.）：能让同一只电热壶烧得一样热的**稳恒直流**电压。发热看的是电流的**平方**，而 $\sin^2$ 在一个周期内的平均值恰好是二分之一，所以有效值等于峰值除以根号二：$311/1.414 = 220\ \text{V}$。你见过的每一个"交流电压"（中国 220 V、日本 110 V、美国 120 V）都是有效值，峰值是它的根号二倍。这张卡先用电脑把这个平均值真的算一遍，然后是考试要考的东西：从图上读周期、频率、峰值；用 $x = x_0 \sin\omega t$；电阻上的平均功率是峰值功率的一半；用一个二极管（**半波**）或四个二极管（**桥式**，**全波**）**整流**，再用电容给起伏的输出**滤波**——纹波的大小取决于 $RC$ 和周期谁大。最后是超出考纲、连人教版选择性必修二第三章《交变电流》也只是点到为止的那部分：工程师如何用**复数**处理交流电。正弦量是一根**旋转箭头**（**相量**）的影子；乘以虚数单位就是把箭头转四分之一圈；电容和电感各自把电流朝相反方向推四分之一圈；于是整个电路的微分方程塌缩成一道代数题，"电阻"变成复数，叫**阻抗**。在 [[Complex Numbers]] 里还像数学家的游戏的虚数，就在这一刻成了每个电气工程师的日常工具——而这张卡把它验证了一遍：复数捷径和老老实实做数值积分解出来的微分方程，在每一个频率上（包括谐振点）都对到四位有效数字。

| English | 中文 | 一句话 |
|---|---|---|
| Alternating current / direct current | 交流电 / 直流电 | 周期性换向 / 单向 |
| Peak value $I_0$, $V_0$ | 峰值（最大值） | 正弦量的振幅 |
| Root-mean-square (r.m.s.) value | 有效值 | 发热效果相同的直流值；正弦时为峰值/√2 |
| Period $T$, frequency $f$, angular frequency $\omega$ | 周期、频率、角频率 | $\omega = 2\pi f = 2\pi/T$ |
| Mean power | 平均功率 | 电阻上为峰值功率的一半 |
| Rectification (half-wave / full-wave) | 整流（半波 / 全波） | 一个二极管 / 四个二极管的桥 |
| Smoothing, ripple | 滤波、纹波 | 负载两端并联电容；$RC \gg T$ 纹波小 |
| Phasor | 相量 | 旋转箭头；正弦量是它的投影 |
| Impedance $Z$, reactance $X$ | 阻抗、电抗 | 复数形式的"电阻"；$X_L = \omega L$，$X_C = 1/\omega C$ |
| Phase difference $\phi$ | 相位差 | 电压与电流箭头之间的夹角 |

---

## Part I — What alternates, and the four numbers that describe it

Spin a coil in a magnetic field and the induced e.m.f. comes out as a sine wave — that derivation is in [[Electromagnetic Induction]], and every power station on Earth except a solar farm is that coil, turned by steam or water. So the mains is sinusoidal by birth, not by design:

$$V = V_0 \sin \omega t, \qquad I = I_0 \sin \omega t, \qquad \omega = 2\pi f = \frac{2\pi}{T}.$$

Four numbers describe it, and the exam reads them off a graph:

| Quantity | How to read it | China's mains |
|---|---|---|
| **Period** $T$ | one full cycle, peak to next peak or zero-crossing to the next *same-direction* zero-crossing | 20 ms |
| **Frequency** $f = 1/T$ | cycles per second | 50 Hz |
| **Peak value** $V_0$ | the maximum; the **peak-to-peak** value is $2V_0$ | 311 V |
| **r.m.s. value** | see Part II — the number on the label | 220 V |

The syllabus phrase *"equations of the form $x = x_0 \sin \omega t$"* means one skill: given the equation, read off $x_0$ and turn $\omega$ into $f$ and $T$; given the graph, do the reverse. $V = 240 \sin 314t$ is a 240-volt-peak supply at $314/2\pi = 50$ Hz.

> [!info] Where the 50 comes from
> A two-pole generator makes one cycle per turn, so 50 Hz means the turbine spins at 3000 rpm; the Americas chose 60 Hz (3600 rpm) in the 1890s, Europe 50, and the choice froze when the first grids were built. Japan is the oddity: 50 Hz in the east, 60 Hz in the west, because Tokyo bought German generators and Osaka bought American ones, and the two halves of the country are still joined only through frequency converters. Nothing about 50 is physically special; it is high enough that lamps do not visibly flicker and low enough that the iron in transformers does not waste too much energy per cycle.

The 0625 requirement is the difference between the two kinds of current: **d.c. flows in one direction** (a battery); **a.c. reverses direction periodically** (the mains, a generator with slip rings). A graph of a.c. crosses the time axis; a graph of d.c. does not.

---

## Part II — Root-mean-square: the number that boils the kettle

### Why the mean is useless

Average $I = I_0 \sin \omega t$ over a cycle and you get zero: as much charge goes left as right. Yet the kettle boils, so the mean current is the wrong number. The right one comes from asking what the resistor feels. Power in a resistor is $P = I^2 R$, and $I^2$ is positive whichever way the current flows — so the mean power is $R$ times the **mean of $I^2$**, and the natural "size" of an a.c. is the square root of that: **root** of the **mean** of the **square**, in that order, read backwards.

$$I_{\text{rms}} = \sqrt{\langle I^2 \rangle}\,, \qquad \langle P \rangle = I_{\text{rms}}^2 R.$$

The definition the scheme wants in words: *the r.m.s. value of an alternating current is the value of the **steady (direct) current** that would produce the **same heating effect** (the same power) in the same resistor.* Two marks, two ideas: steady current, same heating.

### Why $\sqrt 2$

For a sinusoid, $I^2 = I_0^2 \sin^2 \omega t$, and the double-angle identity gives $\sin^2 \omega t = \tfrac12(1 - \cos 2\omega t)$. The cosine term averages to zero over a cycle (it is a sinusoid at twice the frequency), so

$$\langle I^2 \rangle = \tfrac12 I_0^2 \quad\Longrightarrow\quad \boxed{\,I_{\text{rms}} = \frac{I_0}{\sqrt 2}\,,\qquad V_{\text{rms}} = \frac{V_0}{\sqrt 2}\,}.$$

The picture says the same thing without the identity: $\sin^2$ swings between 0 and 1 and is symmetrical about $\tfrac12$ — every bump above the half-line has a matching dip below it.

> [!info] The same half, by calculus
> "Mean over a cycle" is an integral divided by the period ([[Integration]]: the average value of a function is $\frac1T\int_0^T f\,\mathrm dt$), so
> $$\langle I^2\rangle = \frac{1}{T}\int_0^T I_0^2 \sin^2\omega t\,\mathrm dt = \frac{I_0^2}{T}\int_0^T \frac{1 - \cos 2\omega t}{2}\,\mathrm dt = \frac{I_0^2}{T}\left[\frac t2 - \frac{\sin 2\omega t}{4\omega}\right]_0^T = \frac{I_0^2}{T}\cdot\frac T2 = \frac{I_0^2}{2},$$
> because $\sin 2\omega T = \sin 4\pi = 0$. There is also a way that needs no identity at all: $\sin^2 + \cos^2 = 1$ at every instant, so $\int_0^T \sin^2 + \int_0^T \cos^2 = T$; and the two integrals are equal, since $\cos$ is just $\sin$ shifted by a quarter period and a shift does not change an integral over a whole period. Each is therefore $T/2$, and the mean of $\sin^2$ is $\tfrac12$. The $\sqrt2$ is the square root of that half — nothing more.

![[alternating-current-rms.svg|1000]]

*Top row: a 2.6 A peak sinusoid, its mean (zero, useless), its square, and the mean of the square — exactly half of $6.76\ \text{A}^2$, so the r.m.s. value is $\sqrt{3.38} = 1.84$ A. Bottom row: the June 2021 Paper 42 square wave. Its square is constant, so r.m.s. equals peak: $\sqrt 2$ is a property of the sine, not of alternating current in general. The script `alternating-current-rms.py` computes both averages numerically.*

### Mean power is half the peak power

At the instant of the peak, the resistor dissipates $P_0 = I_0^2 R$; averaged over the cycle it dissipates $\tfrac12 I_0^2 R$:

$$\boxed{\langle P \rangle = \tfrac12 P_{\max} = \tfrac12 I_0 V_0 = I_{\text{rms}} V_{\text{rms}}.}$$

This is the reason the r.m.s. value is *the* value: write every power formula from [[Resistance]] — $P = IV = I^2R = V^2/R$ — with r.m.s. values in place of d.c. ones and they are all true for the mean power. The label on the kettle (220 V, 2000 W) is an r.m.s. voltage and a mean power; the peak power, $4000$ W, is reached for an instant twice per cycle and nobody prints it.

> [!warning] The mains peak is 311 V, not 220 V
> Insulation, capacitors and semiconductors in a mains appliance must survive the **peak**, $220\sqrt2 = 311$ V — and in a 240 V country, 340 V. That is why the capacitor inside a phone charger is rated 400 V although the "mains" is 220 V. Every a.c. voltage you are ever quoted — 220 V in China, 120 V in the US, 110 V in Japan, 12 V from a doorbell transformer — is an r.m.s. value unless it says otherwise.

---

## Part III — Rectification: one-way gates

Electronics runs on d.c.; the wall delivers a.c.; something in between must turn the tide into a river. The component is the **diode** ([[Resistance]] §I–V characteristics): near-zero resistance one way, near-infinite the other.

**Half-wave.** One diode in series with the load passes the positive half-cycles and blocks the negative ones. The output is a train of humps with gaps of equal length between them: half the input's energy is simply refused.

**Full-wave — the bridge.** Four diodes in a diamond. Whichever supply terminal is positive, exactly two diodes conduct and route the current *through the load in the same direction*; the other two are reverse-biased. The negative half-cycles are not deleted but *flipped up*.

![[alternating-current-bridge.svg|960]]

*The same bridge in both half-cycles. Follow the green path: from the positive terminal, through one diode to the top of the load, down through $R$, and back through the diagonally opposite diode. The polarity of the load never changes — which is the whole point, and the one-mark question ("draw an arrow for the current in $R$").*

![[alternating-current-rectification.mp4]]

*Watch the three stages: one diode lighting green on the positive halves only; the bridge switching its conducting pair every half-cycle while the amber dot rides through the load top-to-bottom both times; then the capacitor joining the load and the output becoming a sawtooth whose teeth shrink when $RC$ is raised.*

The examined skills are graphical: draw the output for a given input (humps of height $V_0$, every half-cycle for full-wave, every other one for half-wave), draw the power in the load ($P \propto V^2$, so a train of humps *all* above the axis, peaking with the voltage), and answer the sharp question from June 2023: **how does the r.m.s. of the full-wave output compare with the r.m.s. of the input?** They are equal. Rectification changes the *sign* of half the cycles; $V^2$ does not see signs; the mean of $V^2$ is unchanged; so is its root. (For half-wave the mean of $V^2$ halves, and the r.m.s. falls to $V_0/2$.)

![[alternating-current-rectification.svg|1000]]

*Left and middle: half-wave and full-wave outputs against the dotted input. Right: the full-wave output with a smoothing capacitor across the load, for three values of $RC$ relative to the period. The amber curve reproduces the June 2025 Paper 44 question — a ripple of 33 % of the peak when $RC = 0.9\,T$.*

---

## Part IV — Smoothing: the reservoir

Put a capacitor across the load — *across*, in parallel with $R$, never in series with it:

![[alternating-current-smoothing-circuit.svg|960]]

*Left, near a peak: the conducting pair feeds both the resistor and the capacitor, which charges to $V_0$. Right, just after the peak: the supply's voltage is falling faster than the capacitor's, so every diode is reverse-biased and switched off (grey), and the capacitor's only path is the red one — down through $R$. That closed loop, with nothing else in it, is the $RC$ discharge.*

On each rising edge the supply charges it to $V_0$; after the peak, the supply voltage falls faster than the capacitor is willing to, the diodes go reverse-biased, and the capacitor is left **discharging through the load alone** — the exponential from [[Capacitors]]:

$$V = V_0\, e^{-t/RC}.$$

The discharge lasts until the next hump climbs back above the capacitor voltage and recharges it. So the output is a sawtooth of small **ripple** riding on a nearly steady level, and the size of the ripple is set by one comparison:

$$\text{ripple small} \iff RC \gg T \quad(\text{full-wave: the gap between peaks is } T/2).$$

Bigger $C$ or bigger $R$ means a longer time constant, a slower discharge, and a smaller ripple. The syllabus asks for exactly that dependence in words, and the schemes reward the chain: *larger time constant → capacitor discharges less between peaks → smaller drop in p.d. → smaller ripple*. The trade-off engineers pay: a large capacitor is recharged in short, violent pulses near each peak, and it must be rated for the peak, not the r.m.s.

The Paper 4 calculation follows one recipe (worked below on June 2022 and June 2025): read the **discharge time** off the graph (from a peak to where the decay meets the next rising hump), read the **minimum voltage**, and put both into $V_{\min} = V_0 e^{-t_d/RC}$. The script `alternating-current-rectifier.py` simulates the circuit honestly — ideal diodes, exponential discharge, recharge when the hump overtakes — and finds that the scheme's graphical shortcut is within 3 % of the exact answer: a 33 % ripple needs $RC = 0.88\,T$ (the scheme reads 0.90), and the June 2022 numbers give $C = 269\ \mu\text{F}$ (the scheme: 270).

---

## Part V — Where this is the working tool

- **Every charger in your bag.** Mains in, 5 V d.c. out. The chain is: bridge rectifier (Part III) → smoothing capacitor charged to 311 V (Part IV) → a transistor chopping that into a.c. at 50–150 kHz → a thumbnail-sized transformer → a second rectifier and capacitor. The detour through high frequency is explained in [[Electromagnetic Induction]]: Faraday's law pays per rate of change, so a thousand-fold higher frequency needs a thousand-fold smaller core.
- **Why the grid is a.c. at all.** Only a.c. can be transformed, and only transforming lets the same power travel at high voltage and low current, with $I^2R$ loss in the wires cut by the square of the step-up — the argument worked in [[Internal Resistance]] and [[Electromagnetic Induction]]. Edison lost the War of the Currents on this one fact ([[The War of the Currents]]).
- **Why d.c. is coming back for the longest lines.** An a.c. cable has capacitance to the ground and inductance along its length, so it stores and returns energy every cycle without delivering it — the *reactive power* of the Beyond section — and at 50 Hz the current crowds into the outer 9 mm of a copper conductor (the *skin effect*, also below). Over 600 km, or under the sea, the losses win, and the modern answer is **HVDC**: rectify at one end with semiconductor valves the size of a building, invert at the other. China's 1100 kV Changji–Guquan line carries 12 GW over 3300 km as d.c.
- **The hum.** A transformer or a fluorescent ballast hums at **100 Hz**, not 50: the iron is pulled by the field twice per cycle, once for each polarity — the same $\sin^2$ that gave the mean power its factor of a half.
- **The 380 V on the factory wall.** Industrial supplies are three-phase: three sinusoids 120° apart. Between any phase and neutral is 220 V; between two phases the phasors subtract to $220\sqrt3 = 380$ V. The reason is in the Beyond section, and it is the same picture as the phasor clip.

---

### How does the socket know how much current to give?

It does not, and it never has to. Every appliance in the house is connected **in parallel** across the same two wires, live and neutral, so each one sees the full 220 V regardless of what else is plugged in, and each draws the current its own resistance allows: $I = V/R$, or equivalently $I = P/V$ from the label. A 2 kW kettle has $R = V^2/P = 24\ \Omega$ and takes 9.1 A; a lamp with 4.8 kΩ takes 0.05 A; the live wire carries the sum. Nothing upstream decides the share — the appliances decide it, each on its own.

![[alternating-current-socket.svg|960]]

*The socket is not a divider, because a divider needs the loads in series. In parallel, adding the kettle does not change the lamp's voltage or its current; it only adds 9.1 A to the wire that feeds them all.*

What makes this work is that the supply is a **stiff** voltage source: its internal resistance — the substation transformer plus the house wiring, a tenth of an ohm or so — is tiny compared with any appliance, so the drop across it is a volt in two hundred. That drop is the only sense in which the wiring *is* a divider, and it is the same loading effect as in [[Potential Dividers]] and the same $\mathcal E - Ir$ as in [[Internal Resistance]]: switch on the kettle and the lamps dim by half a percent, which you cannot see; start a large motor on a long rural line and they dim visibly, because that line's $r$ is not small. Two safety limits close the loop — the **fuse or breaker** opens if the sum exceeds what the wire can carry, and the wire's own $I^2r$ heating is the reason the limit exists.

The generator finds out last. Its rotor spins at 3000 rpm, and a sudden extra load takes energy out of that spin before any boiler has responded, so the grid **frequency sags** — by a few hundredths of a hertz for a kettle, by a few tenths for a city — and governors open the steam valves to pull it back to 50.00 Hz. The frequency is the one signal every generator on the grid shares, and it is how the supply learns, a cycle late, how much current the sockets have already taken.

---

## Worked examples — real Paper 4 and Paper 2 questions, every mark named

### Cambridge 9702 June 2021 Paper 42 Q10 — r.m.s. from the heating effect [2 + 1 + 1 + 2 + 2]

*(a) By reference to heating effect, explain what is meant by the r.m.s. value of an alternating current.* **Tool: the definition** — *the steady (direct) current* [M1] *that produces the same heating effect as the alternating current* [A1]. Both halves are needed: "the average" scores nothing, "the equivalent d.c." without heating scores one.

*(b)(i) A sinusoidal current with peaks at ±2.6 A: peak and r.m.s.* **Trigger: sinusoid → divide by $\sqrt2$.** Peak 2.6 A; r.m.s. $= 2.6/\sqrt2 = 1.8$ A [A1].
*(b)(ii) A square wave switching between +2.0 A and −2.0 A.* **Trigger: not a sinusoid → go back to the definition.** $I^2 = 4.0\ \text{A}^2$ at every instant, so the mean of $I^2$ is $4.0$ and the r.m.s. is 2.0 A: **peak 2.0 A, r.m.s. 2.0 A** [A1]. The plotted check is the bottom row of the r.m.s. figure.

*(c) The supply is $V = 240 \sin kt$ at 50 Hz. (i) Find $k$.* **Tool: $\omega = 2\pi f$** — $k = 2\pi \times 50$ [C1] $= 310\ \text{rad s}^{-1}$ [A1] (two significant figures, as asked; $314$ is the three-figure value).
*(ii) A heater on this supply has mean power 3.2 kW; find its resistance.* **Trigger: mean power with a peak given → either $V_{\text{rms}}^2/R$ or $V_0^2/2R$**, both accepted [C1]: $R = (240/\sqrt2)^2/3200 = 240^2/(2 \times 3200) = 9.0\ \Omega$ [A1]. Using $240^2/3200 = 18\ \Omega$ — treating the peak as r.m.s. — is the standard error and loses both marks.

### Cambridge 9702 June 2022 Paper 41 Q5 — the bridge, the axes, the capacitor [1 + 1 + 1 + 3 + 1 + 2 + 3]

Four diodes and a 1.2 kΩ load; $V_{\text{IN}} = 6.0 \sin 25\pi t$.

*(a) Rectification means* **conversion of a.c. to d.c.** [B1]; four diodes give **full-wave** [B1]. *(b)(i) Label the output polarity.* Follow the diodes: the terminal the arrows point *toward* is + [B1]. *(b)(ii) Label the axes of the output graph.* **Tool: read $V_0$ and $\omega$ from the equation.** $V_0 = 6.0$ V, so the voltage ticks are 4 and 8 V [B1]; $\omega = 25\pi$, so $T = 2\pi/25\pi = 0.08$ s [C1], and the time ticks run 0.02, 0.04, … 0.12 s [A1] — with humps every $T/2 = 0.04$ s because the rectification is full-wave.

*(c) A capacitor smooths the output; the ripple is 10 % of the peak. (i)* Capacitor symbol **in parallel with the 1.2 kΩ resistor** [B1] — in series it would block the d.c. *(ii) Sketch the smoothed output* [2]: from each peak, a line of decreasing negative gradient down to where it meets the next rising hump [B1], the drop being 10 % of the peak [B1]. *(iii) Calculate $C$.* **Tool: the RC discharge, $V = V_0 e^{-t/RC}$, with the discharge time read off the graph.** The output falls from 6.0 V to $0.90 \times 6.0 = 5.4$ V [C1] over the discharge time, which on the graph is about 0.034 s of each 0.04 s half-period [C1]; $5.4 = 6.0\, e^{-0.034/(1200\,C)}$ gives $C = 2.7 \times 10^{-4}$ F [A1]. The simulation in `alternating-current-rectifier.py` returns 269 µF for the same specification.

### Cambridge 9702 June 2023 Paper 42 Q7 — draw the bridge, then think about r.m.s. [1 + 2 + 1 + 3 + 2 + 1]

*(a)* Full-wave [B1]. Complete the three missing diodes so all four point the same way round the diamond (the scheme's "pointing left") [B1 + B1]; arrow for the current in $R$ [B1] — it is fixed by the diode directions, whichever half-cycle you imagine. *(b)(i) Sketch $V_{\text{OUT}}$ for two periods* [3]: minimum 0, maximum $+V_0$ [B1]; peaks at $t = 0, 0.5T, T, 1.5T, 2T$ with zeros half-way between [B1]; the shape of $|\sin|$, not triangles [B1]. *(ii) Sketch $P$ against $t$* [2]: a sinusoidal curve with its troughs sitting on the axis [B1] — because $P \propto V^2 \propto \sin^2$, which is itself a raised cosine at double frequency — peaks with the voltage, zeros with it [B1]. *(iii) Compare the r.m.s. of $V_{\text{OUT}}$ with that of $V_{\text{IN}}$.* **Trigger: r.m.s. is built from $V^2$, and $V^2$ ignores sign.** The $V^2$–$t$ graph (equivalently the power graph) is identical with or without rectification, so the r.m.s. values are the **same** [B1]. Students who answer "smaller, because the negative parts are removed" have confused the mean with the r.m.s.

### Cambridge 9702 June 2025 Paper 44 Q8 — the time constant in terms of $T$ [2 + 3 + 3 + 2]

*(a) Complete the bridge so that A is positive with respect to B* [2]: four diodes, one per gap, correct symbols [B1], all four pointing from B's side round to A's [B1]. *(b) With a smoothing capacitor the ripple is 33 % of $V_0$. (i) Draw the smoothed p.d. from $0.5T$ to $2T$* [3]: exponential decays from the peaks at $0.5T$, $T$, $1.5T$ that end where they meet the next rising hump [B1]; the rising parts following the dotted hump up to the next peak [B1]; the minimum at $\tfrac23 V_0$ [B1]. *(ii) Use your line to find the time constant in terms of $T$.* **Tool: read the discharge time, then $V_{\min} = V_0 e^{-t_d/\tau}$.** From the graph the decay from $V_0$ to $\tfrac23 V_0$ takes about $\tfrac{11}{30}T$ [C1]; $\tfrac23 = e^{-(11T/30)/\tau}$ [C1]; $\ln\tfrac23 = -\tfrac{11T}{30\tau}$, so $\tau = 0.90\,T$ [A1]. (The simulation gives $0.88\,T$ for an exact 33 % ripple; the scheme accepts the graphical reading.) *(iii) The load resistance is increased.* **Trigger: $\tau = RC$ grows.** Time constant increased [B1] → the line shows a larger minimum, i.e. a smaller difference between maximum and minimum [B1]. Note the direction: a *heavier* load (smaller $R$) makes the ripple *worse*, which is why a power supply's ripple is specified at full load.

### Cambridge 0625 June 2022 Paper 42 Q8 — a.c. graph, period, and average current [1 + 1 + 3]

*A 60 Hz a.c. supply; (a) the period.* $T = 1/60 = 0.017$ s [B1]. *(b)(i) Component A, which lets current through one way, is a* **diode** [B1]. *(ii) $1.5 \times 10^{17}$ electrons pass A in each period; the average current.* **Tool: $I = Q/t$** [C1]: $Q = 1.5 \times 10^{17} \times 1.6 \times 10^{-19} = 0.024$ C [C1]; $I = 0.024/0.017 = 1.4$ A [A1]. The physics being tested: through a diode the current is one-way, so the *average* over a period is a meaningful number — the question quietly assumes a half-wave rectified current, which is why the electrons all pass in one direction.

---

## Misconceptions

- **"R.m.s. is the average current."** The average of a sinusoidal current is zero. R.m.s. is the root of the average of the *square* — the d.c. with the same heating. **Fix:** make them compute $\langle I \rangle$ and $\langle I^2 \rangle$ side by side on the r.m.s. figure; the first line lies on the axis.
- **"Mean power is half because the current is only flowing half the time."** The current flows all the time (except at two instants per cycle). The half comes from $\langle \sin^2 \rangle = \tfrac12$, the average height of the $\sin^2$ curve. **Fix:** the square-wave case — current always at full magnitude, mean power equals peak power, no half.
- **"$V_{\text{rms}} = V_0/\sqrt2$ for any a.c."** Only for a sinusoid. For a square wave the r.m.s. equals the peak; for a triangle wave it is $V_0/\sqrt3$. **Fix:** the definition first, the $\sqrt2$ second.
- **"The capacitor blocks the ripple."** The capacitor does not filter anything out; it *stores charge at the peaks and releases it between them*, so the load sees a slowly falling voltage instead of a hump that falls to zero. Placed in series it would block the d.c. entirely. **Fix:** draw the discharge path — capacitor, load, back — with the diodes reverse-biased.
- **"A bridge rectifier removes the negative half-cycles."** It *reverses* them. Half the energy is thrown away by a half-wave rectifier; none by a bridge — which is exactly why the two r.m.s. values in June 2023 Q7 are equal.
- **"Increasing the load resistance makes the ripple worse."** The opposite: larger $R$ means a larger $RC$, a slower discharge, a smaller ripple. The ripple is worst when the supply is *working hardest*.

---

## Hands-on

- **Run the averages.** `python3 alternating-current-rms.py` prints $\langle I \rangle$, $\langle I^2 \rangle$ and the r.m.s. for the sinusoid and the square wave, and draws the figure. Change the waveform to a triangle and check $V_0/\sqrt3$.
- **Design a smoothing capacitor.** `python3 alternating-current-rectifier.py` simulates the bridge with ideal diodes and a real $RC$ discharge, inverts "ripple 10 %" to a capacitance, and checks the two Paper 4 answers. Change the load to see the ripple grow.
- **Redeem $i$.** `python3 alternating-current-impedance.py` integrates the RLC differential equation with a fourth-order Runge–Kutta stepper until the transient dies, fits the steady-state amplitude and phase, and prints them beside $V_0/Z$ from complex impedance at nine frequencies. They agree to four significant figures, resonance included.
- **See a real a.c.** Never probe the mains. A 9 V a.c. "wall wart" (the older, heavy kind) or the output of a bicycle dynamo is safe; feed it through a 10 kΩ:1 kΩ divider ([[Potential Dividers]]) into a computer's microphone input and any free oscilloscope app shows the sine, the period and the peak — and, with a diode and a capacitor on a breadboard, the humps and the ripple.

---

## Exam Notes

### Cambridge 9702 — Topic 21, Paper 4 only

- **§21.1:** period, frequency, peak value; $x = x_0 \sin \omega t$; *recall and use* $I_{\text{rms}} = I_0/\sqrt2$ and $V_{\text{rms}} = V_0/\sqrt2$ for a sinusoid; mean power in a resistive load is half the maximum power. The written definition of r.m.s. (steady current, same heating) is a recurring two-marker (June 2021 Q10). The transformer half of the old §21.1 bullet lives in [[Electromagnetic Induction]].
- **§21.2:** distinguish half-wave and full-wave graphically; explain one diode (half-wave) and four (bridge); analyse a single smoothing capacitor *including the effect of the values of $C$ and $R$*. Questions are almost always the bridge: complete the diodes, mark the polarity, sketch the output and the smoothed output, then the $RC$ calculation with the discharge time read off the graph (June 2022 Q5, June 2023 Q7, June 2025 Q8 above). This is A-Level content: not on Paper 1 or Paper 2.

### Cambridge 0625 — §4.2.2 and §4.5.2 (Core and Extended)

- **§4.2.2:** *know the difference between direct current and alternating current* — one direction versus periodic reversal; recognise each from a current–time graph. Often one mark inside a circuits question, as in June 2022 Paper 42 Q8.
- **§4.5.2:** the a.c. generator and its e.m.f.–time graph, which this card's Part I inherits from [[Electromagnetic Induction]]; the 0625 questions on period from a graph or from a frequency are the same skill at IGCSE depth. No r.m.s., no rectification at IGCSE.

### IB Physics — D.4.2

The AC generator and the effect of rotation frequency on the output (amplitude and frequency both scale with rotation rate — [[Electromagnetic Induction]] Part "the a.c. generator"). The 2023 guide has no r.m.s. or rectification outcome; both were dropped from the old Topic 11.

### Not examined on…

- **AP Physics 2** — circuits are d.c. only; a.c. does not appear.
- **AP Physics C (E&M)** — the CED excludes a.c. circuit analysis; the LC oscillator appears (the Beyond section's $\omega_0 = 1/\sqrt{LC}$ is that topic) but not phasors, impedance or rectification.
- **Cambridge 9709 / 9231** — the maths of this card ($\langle \sin^2 \rangle = \tfrac12$, the auxiliary equation with complex roots) is theirs, in [[Trigonometric Identities]] and [[Second-Order Differential Equations]], but a.c. is never the context.
- **The Chinese senior curriculum** (人教版选择性必修二 第三章) examines 有效值, 变压器 and 远距离输电 much as 9702 does, without rectification; its 电容和电感对交变电流的影响 is qualitative — the "capacitor passes high frequency, inductor passes low" statement that the impedance section below turns into numbers.

---

## Quick reference

| Result | Formula | Condition |
|---|---|---|
| Sinusoidal supply | $V = V_0 \sin \omega t$, $\omega = 2\pi f = 2\pi/T$ | |
| r.m.s. value | $I_{\text{rms}} = I_0/\sqrt2$, $V_{\text{rms}} = V_0/\sqrt2$ | sinusoid only; square wave: r.m.s. = peak |
| Mean power in $R$ | $\langle P\rangle = I_{\text{rms}}^2 R = V_{\text{rms}}^2/R = \tfrac12 I_0 V_0 = \tfrac12 P_{\max}$ | resistive load |
| Half-wave output | humps every $T$, r.m.s. $= V_0/2$ | one diode |
| Full-wave output | humps every $T/2$, r.m.s. $= V_0/\sqrt2$ (unchanged) | four-diode bridge |
| Smoothing | $V = V_0 e^{-t/RC}$ between peaks; ripple small when $RC \gg T$ | capacitor across the load |
| Reactance | $X_L = \omega L$, $X_C = 1/\omega C$ | beyond syllabus |
| Series impedance | $Z = R + j\left(\omega L - \dfrac{1}{\omega C}\right)$, $\lvert Z\rvert = \sqrt{R^2 + (X_L - X_C)^2}$, $\tan\phi = (X_L - X_C)/R$ | beyond syllabus |
| Resonance | $\omega_0 = 1/\sqrt{LC}$, $Q = \omega_0 L/R$ | beyond syllabus |
| Mean power with phase | $\langle P \rangle = V_{\text{rms}} I_{\text{rms}} \cos\phi$ | beyond syllabus |

---

## Beyond Syllabus — the imaginary number, redeemed

### The equation you cannot avoid

Put a resistor, an inductor and a capacitor in series with a sinusoidal supply. Kirchhoff's loop rule ([[Kirchhoff's Laws]]) with the three voltages — $IR$ across the resistor, $L\,\mathrm dI/\mathrm dt$ across the inductor ([[Electromagnetic Induction]]: an inductor's e.m.f. is proportional to the *rate of change* of current), $Q/C$ across the capacitor — gives

$$L\frac{\mathrm d^2 Q}{\mathrm dt^2} + R\frac{\mathrm dQ}{\mathrm dt} + \frac{Q}{C} = V_0 \cos\omega t.$$

This is exactly the forced, damped oscillator of [[Second-Order Differential Equations]] and [[Damped Oscillations]] — mass $\leftrightarrow L$, friction $\leftrightarrow R$, spring $\leftrightarrow 1/C$. Solving it the honest way means guessing a particular integral $A\cos\omega t + B\sin\omega t$, differentiating twice, and solving two simultaneous equations for $A$ and $B$. It works, and it is miserable, and it has to be redone for every circuit.

### Euler's trick: the derivative becomes a multiplication

Recall from [[Euler's Formula and De Moivre's Theorem]] that $e^{j\theta} = \cos\theta + j\sin\theta$ (engineers write $j$ for $\sqrt{-1}$ because $i$ is taken by current). So $\cos\omega t$ is the **real part** of $e^{j\omega t}$ — the shadow on the real axis of an arrow of length 1 turning at $\omega$. That arrow is the **phasor** in the clip:

![[alternating-current-phasor.mp4]]

Now the trick. Feed the equation the complex drive $V_0 e^{j\omega t}$ instead of $V_0\cos\omega t$, and look for a response of the same shape, $Q = \hat Q\, e^{j\omega t}$ with $\hat Q$ a complex constant. Differentiating $e^{j\omega t}$ just multiplies it by $j\omega$; differentiating twice multiplies by $(j\omega)^2 = -\omega^2$. The differential equation becomes an *algebraic* one:

$$\left(-\omega^2 L + j\omega R + \frac1C\right)\hat Q = V_0.$$

Write it for the current, $\hat I = j\omega \hat Q$, and divide through:

$$\boxed{\;\hat I = \frac{V_0}{Z}, \qquad Z = R + j\omega L + \frac{1}{j\omega C} = R + j\left(\omega L - \frac{1}{\omega C}\right).\;}$$

$Z$ is the **impedance**: a complex number that plays the part of resistance. Its magnitude $\lvert Z\rvert$ is the ratio of peak voltage to peak current; its argument is the phase by which the voltage leads the current. The real current is the real part of $\hat I e^{j\omega t}$ — take the shadow at the end, once, and the whole calculation in between is algebra. Because the physical equation is linear and real, the real part of a complex solution *is* a solution: that single fact licenses the whole method, and it is the redemption the epigraph promised. The number that was invented to solve $x^2 + 1 = 0$ turns out to be **the quarter turn**: multiplying by $j$ rotates a phasor by 90°, and a quarter turn is precisely what an inductor and a capacitor each do to the current.

### Reading the three elements off the picture

| Element | Impedance | What it does to the current | Why |
|---|---|---|---|
| Resistor | $R$ | in phase with $V$ | $V = IR$ instant by instant |
| Inductor | $j\omega L$ | **lags** $V$ by 90° | the e.m.f. is $L\,\mathrm dI/\mathrm dt$; the current is still rising when the voltage peaks |
| Capacitor | $\dfrac{1}{j\omega C} = -\dfrac{j}{\omega C}$ | **leads** $V$ by 90° | $I = C\,\mathrm dV/\mathrm dt$; the current is largest when the voltage is changing fastest, at $V = 0$ |

Impedances in series add; in parallel their reciprocals add — the rules of [[Resistance]] carry over unchanged, now with complex arithmetic. The inductor's reactance $\omega L$ grows with frequency, the capacitor's $1/\omega C$ shrinks: an inductor passes d.c. and blocks high frequency, a capacitor the reverse. That is the sentence the Chinese textbook states qualitatively; here it is a number at every frequency. The magnitude and phase of a series $Z$ are Pythagoras and a tangent on the phasor triangle in the clip's second scene, $\lvert Z\rvert = \sqrt{R^2 + (\omega L - 1/\omega C)^2}$ and $\tan\phi = (\omega L - 1/\omega C)/R$.

### Verified: the shortcut against the differential equation

A claim this convenient deserves a check. The script beside this card takes $R = 10\ \Omega$, $L = 10$ mH, $C = 1\ \mu$F, integrates the differential equation numerically for sixty cycles at each of nine frequencies until the start-up transient has died, fits the steady-state current, and puts it beside $V_0/Z$:

![[alternating-current-resonance.svg|1000]]

*The purple curves are $\lvert V_0/Z\rvert$ and $-\arg Z$ from four lines of complex arithmetic; the red rings are the differential equation integrated by brute force. At every frequency they agree to four significant figures. The 0.001 mA discrepancy at 8 kHz is the integrator's step size, not physics.*

### Resonance — where the two quarter turns cancel

When $\omega L = 1/\omega C$ the two reactances cancel, $Z = R$ is purely real, the current is in phase with the voltage and as large as it can be:

$$\omega_0 = \frac{1}{\sqrt{LC}}, \qquad f_0 = \frac{1}{2\pi\sqrt{LC}} = 1592 \text{ Hz for the values above.}$$

The sharpness of the peak is the **quality factor** $Q = \omega_0 L/R$ (10 here): the curve's width at $1/\sqrt2$ of the peak is $f_0/Q$, 159 Hz. This is how a radio picks one station out of the whole spectrum — a variable capacitor tunes $f_0$ onto the carrier, and $Q$ decides how much of the neighbours leaks through — and it is why [[Resonance]] and [[Damped Oscillations]] are the same card wearing different components: the damping dial there is $R$ here.

### Power with a phase: what the utility actually bills

With a phase angle between $V$ and $I$, the instantaneous power $V_0 I_0 \sin\omega t\,\sin(\omega t - \phi)$ averages to

$$\langle P\rangle = V_{\text{rms}} I_{\text{rms}} \cos\phi,$$

and $\cos\phi$ is the **power factor**. A pure inductor or capacitor has $\phi = 90°$ and *absorbs no mean power at all*: it borrows energy for a quarter cycle and hands it back. But the current still flows, still heats the cables, still needs copper. Engineers keep the two accounts apart as the **complex power** $S = \hat V \hat I^{\,*} = P + jQ_{\text{r}}$: real power $P$ (watts, what the kettle uses) and reactive power $Q_{\text{r}}$ (volt-amperes reactive, what sloshes). A factory full of motors is inductive, its power factor 0.7 or worse, and the utility charges it for the extra current or makes it install a bank of capacitors to cancel the inductance — 无功补偿, the same cancellation as resonance, done deliberately at 50 Hz.

### Three phases: why 380 V, and why motors turn

Generate three sinusoids 120° apart on three wires, and their phasors form an equilateral triangle: they **sum to zero**, so the return wire carries no current and can be thin or omitted. Between a phase and the neutral is 220 V; between two phases the phasor difference has length $220 \times 2\sin 60° = 220\sqrt3 = 380$ V — the number on the factory wall. And three coils fed with three phases make a magnetic field that *rotates* at the supply frequency, dragging a rotor after it with no brushes, no commutator, no sparks: Tesla's induction motor, most of the world's mechanical power, is a phasor diagram made of iron.

### Filters: the smoothing capacitor, seen from the other side

Treat the load and its smoothing capacitor as a potential divider ([[Potential Dividers]]) between $R$ and $1/j\omega C$. The fraction of an input at frequency $\omega$ that reaches the output is the **transfer function**

$$H(j\omega) = \frac{1}{1 + j\omega RC}, \qquad \lvert H\rvert = \frac{1}{\sqrt{1 + (\omega RC)^2}},$$

which is 1 for d.c. and falls as $1/\omega$ above the corner $\omega_c = 1/RC$. The ripple of Part IV is the 100 Hz component of the rectified hump; the capacitor is a **low-pass filter** that lets the d.c. through and attenuates the ripple by roughly $\omega RC$. The same one-line division, with $R$ and $C$ swapped, gives a high-pass filter; with an inductor, a band-pass; and every audio equaliser, every 5G front end and every anti-aliasing stage in front of a converter is a chain of these, designed on the Argand diagram and sketched on a Bode plot of $\lvert H\rvert$ in decibels against $\log\omega$.

### Skin effect: why the biggest a.c. lines are d.c.

A changing current makes a changing field inside its own conductor, which by Lenz drives eddy currents that cancel the current at the centre and reinforce it at the surface. The current lives within a **skin depth** of the surface,

$$\delta = \sqrt{\frac{2\rho}{\omega\mu}} \approx 9\ \text{mm for copper at 50 Hz},$$

so a 40 mm grid conductor uses only its outer shell and its a.c. resistance is well above its d.c. value; at 1 MHz the skin is 65 µm, which is why radio-frequency wire is braided from hundreds of insulated strands (Litz wire). Add the reactive power of a long cable's capacitance and inductance, and above about 600 km overland — or for any undersea link — the transmission that Edison lost the argument over returns as HVDC, rectified and inverted with semiconductors that did not exist in 1890.

### Steinmetz, 1893

The method above was introduced to engineers by **Charles Proteus Steinmetz**, a four-foot-tall German socialist refugee who arrived in New York in 1889 with no money and a mathematics degree, and who told the International Electrical Congress in Chicago in 1893 that alternating-current problems become "simple algebra" if one writes voltages as complex numbers. Before him, every a.c. circuit was solved by trigonometric grind or by graphical construction; after his book *Theory and Calculation of Alternating Current Phenomena* (1897), it was the way the whole industry worked — the story continues in [[The War of the Currents]], where the a.c. side needed exactly this mathematics to win.

---

## Connections

- **Prerequisites:** [[Electromagnetic Induction]] — the generator that makes the sine, and the inductor's $L\,\mathrm dI/\mathrm dt$; [[Resistance]] — $P = I^2R$ and the diode's characteristic; [[Capacitors]] — the $RC$ discharge that sets the ripple; [[Simple Harmonic Motion]] — the sinusoid as the projection of circular motion, which is what a phasor is; [[Complex Numbers]] — the Argand plane the phasor lives on.
- **Leads to:** [[Resonance]] — the peak in the impedance curve, and its mechanical twin.
- **Same mathematics:** [[Second-Order Differential Equations]] (the forced oscillator; Case 3 complex roots is the transient this card waits sixty cycles to kill) and [[Damped Oscillations]] (the damping dial is $R$); [[Euler's Formula and De Moivre's Theorem]] — $e^{j\omega t}$ as the rotating arrow; [[Trigonometric Identities]] — $\sin^2 = \tfrac12(1 - \cos 2\theta)$, the origin of the $\sqrt2$.
- **Applications:** [[Internal Resistance]] and [[Electromagnetic Induction]] — the high-voltage transmission argument this card's Part V completes; [[Potential Dividers]] — the $RC$ filter as a complex divider; [[Kirchhoff's Laws]] — the loop rule that writes the differential equation.
- **Stories:** [[The War of the Currents]] — why the grid alternates, and Steinmetz's mathematics on the winning side; [[The Argument for i]] — the number's own biography, up to the point where this card picks it up.

## Sources

- Cambridge International AS & A Level Physics 9702 syllabus 2028–30, §21.1–21.2; Cambridge IGCSE Physics 0625 syllabus 2026–28, §4.2.2, §4.5.2.
- Cambridge 9702 June 2021 Paper 42 Q10, June 2022 Paper 41 Q5, June 2023 Paper 42 Q7, June 2025 Paper 44 Q8, and 0625 June 2022 Paper 42 Q8, with their published mark schemes.
- The three scripts beside this card: `alternating-current-rms.py`, `alternating-current-rectifier.py`, `alternating-current-impedance.py`; the Manim source `alternating-current-phasor.py`.
- C. P. Steinmetz, *Complex Quantities and Their Use in Electrical Engineering*, Proc. International Electrical Congress, Chicago (1893); *Theory and Calculation of Alternating Current Phenomena* (1897).
- Horowitz and Hill, *The Art of Electronics* (3rd ed., 2015), ch. 1 — impedance, filters, rectification and ripple, with the same design shortcuts as the schemes.
- State Grid Corporation of China, Changji–Guquan ±1100 kV UHVDC project (commissioned 2019) — 12 GW, 3293 km.

## LaTeX Reference

| Symbol | LaTeX | Meaning |
|---|---|---|
| $I_{\text{rms}}$ | `I_{\text{rms}}` | root-mean-square current |
| $\langle P \rangle$ | `\langle P \rangle` | mean power |
| $\omega$ | `\omega` | angular frequency $2\pi f$ |
| $Z$, $\lvert Z \rvert$ | `Z`, `\lvert Z \rvert` | impedance and its magnitude |
| $X_L$, $X_C$ | `X_L`, `X_C` | inductive, capacitive reactance |
| $\hat I$ | `\hat I` | complex (phasor) amplitude |
| $e^{j\omega t}$ | `e^{j\omega t}` | the rotating unit phasor |
| $\phi$ | `\phi` | phase angle between $V$ and $I$ |
| $\delta$ | `\delta` | skin depth |
