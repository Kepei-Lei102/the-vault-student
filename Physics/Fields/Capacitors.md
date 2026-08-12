---
chinese: 电容器 (diànróngqì)
prerequisites:
  - "[[Electric Field]]"
  - "[[Electric Current]]"
  - "[[Exponential Growth and Decay]]"
leads_to:
  - "[[Maxwell's Equations]]"
tags:
  - subject/physics
  - domain/electromagnetism
  - level/A-Level
  - level/university
  - curriculum/Cambridge-9702
  - curriculum/A-Level
  - curriculum/AP-Physics-2
  - curriculum/AP-Physics-C-EM
  - syllabus/9702-19
  - type/deep
  - type/derivation
  - notation/capacitance-C
  - notation/time-constant-RC
  - misconception/capacitor-stores-net-charge
  - misconception/energy-is-QV-not-half
  - misconception/capacitance-depends-on-Q-or-V
---

# Capacitors 电容器

> *A capacitor stores energy by pulling charge apart. Strip electrons off one plate, pile them onto another, and the electric field in the gap holds the two apart under tension — a stretched spring made of charge. That stored jolt is the camera flash, the defibrillator's shock, the smoothing in every power supply — and, one tiny capacitor per bit, the working memory of the machine you are reading this on.*

## Definition

A **capacitor** is two conductors (the **plates**) separated by an insulator. Move charge $+Q$ onto one plate and $-Q$ onto the other, and a potential difference $V$ appears between them. Across all capacitors, that stored charge is **proportional** to the voltage, and the constant of proportionality is the **capacitance**:

$$\boxed{\;C = \dfrac{Q}{V}\;}\qquad\text{unit: the farad, } 1\ \text{F} = 1\ \text{C V}^{-1}.$$

**The farad in SI base units.** Chase that unit all the way down and it is a small exercise in dimensional homogeneity ([[Physical Quantities and Units]]). A volt is a joule per coulomb ($\text{V}=\text{J}\,\text{C}^{-1}$), a coulomb is an ampere-second ($\text{C}=\text{A}\,\text{s}$), and a joule is $\text{kg}\,\text{m}^2\,\text{s}^{-2}$, so

$$1\ \text{F} = \frac{\text{C}}{\text{V}} = \frac{\text{C}}{\text{J}/\text{C}} = \frac{\text{C}^2}{\text{J}} = \frac{(\text{A}\,\text{s})^2}{\text{kg}\,\text{m}^2\,\text{s}^{-2}} = \boxed{\;\text{kg}^{-1}\,\text{m}^{-2}\,\text{s}^{4}\,\text{A}^2\;}$$

Four base units, and notice the **second appears to the fourth power** — a fingerprint of how deeply time and current are baked into capacitance: it measures the charge (amperes $\times$ seconds) you can bank per volt.

The farad is enormous — real capacitors run from picofarads ($10^{-12}$) to the microfarads ($10^{-6}$) in your charger, so a $1$ F capacitor is already a "supercapacitor."

Two ideas trip people up immediately, so state them plainly:

- **A capacitor stores no *net* charge.** One plate is $+Q$, the other $-Q$; they sum to zero. What it stores is charge *separation* — and the **energy** locked in the field between the plates.
- **$C$ does not depend on $Q$ or $V$.** Double the charge and the voltage doubles too; their ratio is fixed. Capacitance is a property of the *geometry and materials* alone, exactly as a spring's stiffness $k$ is a property of the spring, not of how hard you happen to be pulling it.

### A capacitor is an electrical spring

That last comparison is not a loose metaphor — the two systems obey the *same algebra*, which is why everything you already know about springs transfers straight across:

| Spring (mechanics) | Capacitor (electricity) | Relationship |
|---|---|---|
| force $F$ | voltage $V$ | the "effort" that builds up |
| extension $x$ | charge $Q$ | the "amount" you have moved |
| stiffness $k$ ($F=kx$) | inverse capacitance $1/C$ ($V = Q/C$) | stiff spring ↔ small capacitor |
| stored energy $\tfrac12 kx^2$ | stored energy $\tfrac12 \dfrac{Q^2}{C}$ | area under a straight line |

Hold onto this row — the energy formula and the whole $LC$-oscillation story below fall out of it for free ([[Simple Harmonic Motion]]).

### 中文锚点

| English | 中文 | 一句话 |
|---|---|---|
| capacitor / capacitance | 电容器 / 电容 (diànróng) | 储存**分离电荷**和电场能量的元件；$C=Q/V$ |
| farad | 法拉 (fǎlā) | 电容的单位，$1\text{F}=1\text{C/V}$，极大 |
| permittivity / dielectric | 介电常数 / 电介质 | 极板间填充物，$\varepsilon_r$ 倍地增大电容 |
| time constant | 时间常数 (shíjiān chángshù) | $\tau = RC$，充放电快慢的尺度 |

核心一句话：电容器不存**净**电荷（两极板 $+Q$、$-Q$ 相加为零），它存的是**电荷的分离**与极板间**电场的能量**；$C=Q/V$ 只由几何与介质决定，与 $Q$、$V$ 无关——就像弹簧的劲度只由弹簧本身决定。

---

## What sets the capacitance — the parallel-plate capacitor

For two flat plates of area $A$ a distance $d$ apart, the capacitance follows from the field. A charge $Q$ spread over area $A$ gives surface density **$\sigma = Q/A$**, and the uniform field between the plates ([[Electric Field]]) is

$$E = \frac{\sigma}{\varepsilon_0} = \frac{Q}{\varepsilon_0 A}.$$

The voltage is that field times the gap, $V = Ed = \dfrac{Qd}{\varepsilon_0 A}$, so

$$\boxed{\;C = \frac{Q}{V} = \frac{\varepsilon_0 \varepsilon_r A}{d}\;}$$

Two permittivities appear, and they play different roles. **$\varepsilon_0$** is the **permittivity of free space** — a fundamental constant of nature, $\varepsilon_0 \approx 8.85\times10^{-12}\ \text{F m}^{-1}$, that fixes *how strong an electric field a given charge produces in vacuum*. It is the same $\varepsilon_0$ that sits under [[Coulomb's Law|Coulomb's law]] and [[Gauss's Law|Gauss's law]] — the universe's baseline "stiffness" of empty space against being filled with field. **$\varepsilon_r$** (the **relative permittivity**, or *dielectric constant*) is a **dimensionless** multiplier for whatever fills the gap: $\varepsilon_r = 1$ for vacuum, ${\approx}\,2$–$7$ for plastics and glass, into the thousands for special ceramics. So $\varepsilon_0$ is the absolute floor and $\varepsilon_r$ says how many times better than vacuum your filler is. Read the formula off the geometry:

- **Bigger plates ($A\uparrow$)** — more room to park charge at a given voltage → more capacitance.
- **Smaller gap ($d\downarrow$)** — the plates pull on each other's charge more strongly, so more charge sits there for the same $V$ → more capacitance.
- **A dielectric ($\varepsilon_r > 1$)** — the insulator's molecules polarise, their own field partly cancels the plates' field, so the voltage drops for a given $Q$ and $C$ rises. It also lets the capacitor survive a higher voltage before the gap breaks down.

![[capacitor-parallel-plate.svg|620]]

This is *the* lesson to carry into computing: capacitance is bought with **area** and lost to **distance**. A DRAM chip must cram a capacitor behind every bit, so its designers fight for capacitance in almost no area — deep **trench** or stacked cells that fold a large plate area into a tiny footprint ([[RAM and the Memory Hierarchy]]).

### What a real capacitor actually looks like

Almost no real capacitor is two bare plates facing each other across an air gap — that shape squanders space, and the point is to *maximise area*. So manufacturers take two long, thin metal foils with a flexible insulating film between them and **roll the whole sandwich into a cylinder** — which is exactly why so many capacitors are little cans with two legs. A film capacitor the size of your thumb hides *metres* of wound foil. The other dominant form — the **multilayer ceramic capacitor (MLCC)**, the speck soldered by the hundred inside every phone — plays the same trick by **stacking** dozens of interleaved plate layers rather than rolling them. Different packaging, one idea: fold a huge plate area $A$ into a tiny volume.

![[capacitor-real-construction.svg|660]]

---

## Energy stored — and why the one-half

Charging a capacitor is not free, and the cost is not simply $QV$. The subtlety is that the voltage **climbs as you charge**: the first electrons cross an empty, easy gap, but each later one must be pushed against the repulsion of those already there. To move an extra $\mathrm{d}q$ when the voltage is already $v = q/C$ costs $v\,\mathrm{d}q$, so the total work is

$$W = \int_0^Q v\,\mathrm{d}q = \int_0^Q \frac{q}{C}\,\mathrm{d}q = \frac{Q^2}{2C}.$$

Using $Q = CV$ this is the same energy three ways:

$$\boxed{\;W = \tfrac12 QV = \tfrac12 CV^2 = \tfrac{1}{2}\frac{Q^2}{C}\;}$$

The **one-half** is the area of a triangle under the straight $Q$–$V$ line — the identical reason a spring stores $\tfrac12 kx^2$ and not $Fx$. Charge and voltage rise together in lockstep, so the *average* voltage during charging is only half the final voltage, and you pay $\tfrac12 QV$, not $QV$.

![[capacitor-energy-triangle.svg|697]]

> [!info] Where does the energy actually live? — in the field
> The stored energy is not "on the plates"; it sits in the **electric field** in the gap, with an energy **density** $u = \tfrac12 \varepsilon_0 E^2$ (joules per cubic metre). Multiply by the gap volume $Ad$ and you recover $\tfrac12 CV^2$ exactly. This is a genuinely deep idea: *the field itself carries energy.* Once a field can hold energy in empty space, it is a short step to a field that carries energy *away* as it changes — a light wave. That thread is picked up by [[Maxwell's Equations]].

---

## Charging and discharging — the RC circuit

Put a capacitor and a resistor in a loop. This is where the capacitor comes alive in time, and where a single first-order differential equation governs everything.

**Discharge.** A charged capacitor drives a current through the resistor, $I = V/R = Q/(RC)$. But that current *is* the rate at which the plate is losing charge, $I = -\dfrac{\mathrm{d}Q}{\mathrm{d}t}$. Equate them:

$$\frac{\mathrm{d}Q}{\mathrm{d}t} = -\frac{Q}{RC}.$$

A quantity whose rate of change is proportional to itself decays **exponentially** ([[Exponential Growth and Decay]]):

$$\boxed{\;Q(t) = Q_0\,e^{-t/RC}\;}\qquad V \text{ and } I \text{ fall the same way.}$$

> [!info] Why *exponentially*? — the same law as radioactive decay
> The exponential is not a quirk of circuits; it is what **"the rate of loss is proportional to how much is left"** *always* produces. Divide the equation through by $Q$:
> $$\frac{1}{Q}\frac{\mathrm{d}Q}{\mathrm{d}t} = -\frac{1}{RC}.$$
> The **fractional** rate of loss is *constant*. Every second the capacitor sheds the same *percentage* of whatever charge is still there — not the same amount. A high capacitor drives a big current and loses charge fast; a nearly-empty one drives a feeble current and crawls. A quantity that loses a fixed fraction per unit time can only be an exponential.
> This is *exactly* the logic of **radioactive decay** ([[Radioactive Decay]]). A carbon-14 nucleus keeps no clock and has no memory — in any given second it carries a fixed **probability** of decaying, regardless of how long it has already survived. So a huge population sheds a constant fraction per second and the count falls as $N_0 e^{-\lambda t}$: the identical curve, with $1/\lambda$ playing the part of $RC$. Charge on a plate and a bucket of C-14 atoms are utterly different things obeying one equation, because both are **memoryless** — the rate depends only on *how much is there now*, never on the past. (Half-life and time constant are one idea in two costumes: $t_{1/2} = RC\ln 2$.)

**Charging** from a supply $\mathcal{E}$ through $R$ is the mirror image, an approach to the final charge $Q_\infty = C\mathcal{E}$:

$$Q(t) = Q_\infty\left(1 - e^{-t/RC}\right).$$

![[rc-charge-discharge.svg|620]]

The product $\boxed{\tau = RC}$ is the **time constant** — the natural clock of the circuit. In one $\tau$ the charge falls to $1/e \approx 37\%$ of its start (or rises to $63\%$); after about $5\tau$ the process is all but complete. Big $R$ or big $C$ → slow; small → fast.

> [!info] The debt this pays — why DRAM must refresh
> This exact leak is the beating heart of computer memory. A **DRAM** cell stores one bit as charge on a capacitor of a few tens of femtofarads; no insulator is perfect, so that charge bleeds away through an effective resistance with its own $\tau = RC$. Left alone, a stored $1$ decays toward $0$ and the bit is lost. That is *why* DRAM must be **read and rewritten every few milliseconds** — the "refresh" whose sawtooth you met in [[RAM and the Memory Hierarchy]] is this discharge curve, caught and reset before it crosses the threshold. The same $RC$ also sets the tick of a **555 timer** and the ring-oscillator clocks of [[Clock Domains and Metastability]]: charge a capacitor through a resistor, trip a switch at a set voltage, dump, repeat.

---

## Combining capacitors

Capacitors add **opposite** to resistors — worth pinning down, because the swap catches everyone.

- **Parallel** (plates share the same voltage): the charges simply add, $Q = Q_1 + Q_2 = (C_1+C_2)V$, so
$$C_\text{parallel} = C_1 + C_2 + \cdots$$
Intuitively, wiring plates in parallel just makes one bigger plate — more area, more capacitance.

- **Series** (same charge $Q$ is pushed through each, and the voltages stack): $V = \dfrac{Q}{C_1} + \dfrac{Q}{C_2}$, so
$$\frac{1}{C_\text{series}} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots$$
Stacking capacitors in series is like widening the gap $d$ — less capacitance than either alone.

The mnemonic writes itself once you see *why*: parallel = more area = add directly; series = more gap = add reciprocals.

---

## Worked examples

**1 — Sizing a parallel-plate capacitor.** Plates of $A = 0.02\ \text{m}^2$, gap $d = 1.0\ \text{mm}$, vacuum. $C = \varepsilon_0 A/d = (8.85\times10^{-12})(0.02)/(10^{-3}) \approx 1.8\times10^{-10}\ \text{F} = 177\ \text{pF}$. Slide in a dielectric with $\varepsilon_r = 5$ and it jumps to $\approx 0.89\ \text{nF}$ — same box, five times the storage.

**2 — Energy and the one-half.** Charge a $100\ \mu\text{F}$ capacitor to $12\ \text{V}$. Charge $Q = CV = (100\times10^{-6})(12) = 1.2\ \text{mC}$; energy $W = \tfrac12 CV^2 = \tfrac12(100\times10^{-6})(12)^2 = 7.2\ \text{mJ}$. Note $QV = 14.4\ \text{mJ}$ — exactly twice $W$, the one-half made concrete.

**3 — Discharge timing.** That $100\ \mu\text{F}$ capacitor discharges through $R = 10\ \text{k}\Omega$. Time constant $\tau = RC = (10^4)(10^{-4}) = 1.0\ \text{s}$. Time to fall to **half** charge: $Q_0/2 = Q_0 e^{-t/\tau}\Rightarrow t = \tau\ln 2 \approx 0.69\ \text{s}$. To fall to $37\%$ takes exactly one $\tau = 1.0\ \text{s}$; to be "fully" discharged (${<}1\%$) takes $\approx 5\ \text{s}$.

**4 — Series vs parallel.** Two $2\ \mu\text{F}$ capacitors: in **parallel**, $C = 2+2 = 4\ \mu\text{F}$; in **series**, $\tfrac1C = \tfrac12+\tfrac12 = 1 \Rightarrow C = 1\ \mu\text{F}$. The parallel pair stores four times the series pair's energy at the same voltage.

---

## Exam Notes

### Cambridge 9702 (A Level, Topic 19)
Directly and fully examinable, end to end. **§19.1:** $C = Q/V$, the parallel-plate and (data-sheet) spherical formulas, and series $\tfrac1C=\sum\tfrac1{C_i}$ / parallel $C=\sum C_i$. **§19.2:** energy $W = \tfrac12 QV = \tfrac12 CV^2$ as the **area under the $Q$–$V$ graph** (a favourite "explain the one-half" question). **§19.3:** discharge $Q = Q_0 e^{-t/RC}$ and the time constant $\tau = RC$. It also underpins the **§21.2** smoothing capacitor in a rectifier. Expect a graph-reading or a log-linearisation of the exponential.

### AP Physics 2
**§10.6** capacitors ($C = Q/V$, $C = \varepsilon_0 A/d$, energy $\tfrac12 CV^2$) and **§11.8** RC circuits (qualitative charging/discharging, $\tau = RC$) — algebra-based, no calculus required for the exponential.

### AP Physics C: E&M
**Unit 10** (Conductors and Capacitors, §10.3) with the full energy set $U = \tfrac12 CV^2 = \tfrac12 Q^2/C$; **§11.8** treats the RC circuit as a **first-order ODE** (derive the exponential, as above); **§13.6** extends to the **LC circuit**, a second-order ODE with $\omega = 1/\sqrt{LC}$ — undamped oscillation identical in form to a mass on a spring ([[Simple Harmonic Motion]]).

### IB Physics / IGCSE 0625
**Not in the current IB syllabus** — capacitance was dropped from the HL course in the 2023 guide (first exams 2025), so it is enrichment for an IB student, not exam content. Not part of 0625 core physics either. This is a Cambridge-A-Level and AP topic.

---

## Connections

- **Parents:** [[Electric Field]] — the uniform field $E=\sigma/\varepsilon_0$ between the plates that *is* the capacitor; [[Electric Potential]] — the $V$ in $C=Q/V$; [[Exponential Growth and Decay]] — the maths of the $RC$ charge/discharge.
- **The spring analogy:** [[Simple Harmonic Motion]] — a capacitor + [[Electromagnetic Induction|inductor]] ($LC$) sloshes energy back and forth exactly as a mass–spring does, with $\tfrac12 Q^2/C$ playing the role of $\tfrac12 kx^2$; the electrical twin of the oscillator.
- **The same decay law:** [[Radioactive Decay]] — a memoryless, constant-probability-per-second process gives the identical $e^{-t/\tau}$ fall, with half-life $t_{1/2}=RC\ln 2$ the twin of the time constant; [[Coulomb's Law]] — where the same $\varepsilon_0$ first appears, as the strength of the field a charge makes.
- **The application (cross-domain):** [[RAM and the Memory Hierarchy]] — one capacitor holds one **DRAM** bit, and its $RC$ leak is *why* DRAM refreshes; [[Clock Domains and Metastability]] — $RC$ timing behind ring-oscillator clocks; [[How a Chip Is Made]] — the trench/stacked capacitor etched into silicon.
- **Where it leads:** [[Maxwell's Equations]] — the energy density $\tfrac12\varepsilon_0 E^2$ says the field holds energy, the seed of light carrying energy through empty space.
- **History:** [[Stories/Franklin's Coin Flip]] — the Leyden jar, this card's ancestor, read correctly for the first time by Franklin as equal and opposite charges held apart by glass (and the origin of "+/−" themselves); [[Stories/The War of the Currents]] — the human prologue to the whole electromagnetism story (induction, AC, the grid).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $C = \dfrac{Q}{V}$ | `C = \dfrac{Q}{V}` | definition of capacitance (farads) |
| $1\,\text{F} = \text{kg}^{-1}\text{m}^{-2}\text{s}^{4}\text{A}^2$ | `\text{kg}^{-1}\text{m}^{-2}\text{s}^{4}\text{A}^2` | the farad in SI base units |
| $\varepsilon_0 \approx 8.85\times10^{-12}\,\text{F m}^{-1}$ | `8.85\times10^{-12}` | permittivity of free space (a constant); $\varepsilon_r$ is dimensionless |
| $C = \dfrac{\varepsilon_0\varepsilon_r A}{d}$ | `\dfrac{\varepsilon_0\varepsilon_r A}{d}` | parallel-plate capacitance |
| $W = \tfrac12 CV^2 = \tfrac12\dfrac{Q^2}{C}$ | `\tfrac12 CV^2 = \tfrac12\dfrac{Q^2}{C}` | energy stored (the one-half) |
| $u = \tfrac12\varepsilon_0 E^2$ | `\tfrac12\varepsilon_0 E^2` | energy density in the field |
| $Q(t) = Q_0 e^{-t/RC}$ | `Q_0 e^{-t/RC}` | discharge through a resistor |
| $\tau = RC$ | `\tau = RC` | time constant ($1/e$ time) |
| $I = \dfrac{\mathrm{d}Q}{\mathrm{d}t}$ | `\dfrac{\mathrm{d}Q}{\mathrm{d}t}` | current as rate of charge flow |
| $\dfrac{1}{C_s}=\sum\dfrac{1}{C_i}$ | `\dfrac{1}{C_s}=\sum\dfrac{1}{C_i}` | series (parallel: $C=\sum C_i$) |
