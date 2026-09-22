---
chinese: 晶体管开关与数字信号 (jīngtǐguǎn kāiguān yǔ shùzì xìnhào)
aliases:
  - CMOS
  - MOSFET
  - Digital Abstraction
  - Noise Margin
prerequisites:
  - "[[Electric Field]]"
  - "[[Capacitors]]"
  - "[[Logic Gates]]"
leads_to:
  - "[[How a Chip Is Made]]"
tags:
  - subject/physics
  - domain/electronics
  - domain/digital-circuits
  - level/university
  - type/deep
  - type/derivation
  - notation/noise-margin
  - misconception/digital-means-two-physical-voltages
  - misconception/threshold-means-fully-on
---

# The Transistor as a Switch — How Analog Becomes Digital 晶体管开关与数字信号

> *A computer is an analog machine engineered to keep its promises about two categories.*

## Definition

### Formal

A **MOSFET** (metal–oxide–semiconductor field-effect transistor) controls the conductance of a semiconductor channel using an electric field from an insulated **gate**. Its terminals are gate, source, drain and body. The channel carries current between source and drain; the gate controls it.

**CMOS** means *complementary MOS*: circuits combine n-channel and p-channel devices. In a static CMOS logic gate, complementary transistor networks connect the output toward either the positive supply or ground.

The **digital abstraction** assigns ranges of continuous voltages to logical 0 and 1, then requires each gate to produce a valid output for every valid input combination, after enough settling time and within its specified operating conditions.

### Intuitive — a bit is a promise about a range

Your laptop never produces a mathematically perfect 0 V. Wires pick up interference; current causes voltage drops; components differ. If a computer needed an exact voltage at every stage, it would be hopeless.

Instead, the receiver accepts a *band* of low voltages as 0 and a separate band of high voltages as 1. The next gate uses its own power supply to produce a fresh output close to a supply rail. A slightly battered signal can therefore become a clean signal again.

That is the missing link between [[Electric Field]] and [[Logic Gates]]: **field control makes switches; carefully arranged switches restore voltage levels; restored levels make long chains of Boolean reasoning possible.**

### 中文锚点

传话时，前一个人说的“八点”带点口音，你听懂后，会用自己的声音清楚地说一遍，而不是连口音也照搬。数字电路传递信号也有点像这样：它认的是电压落在哪一段范围里，不要求每次都一模一样；只要仍在能可靠辨认的范围内，下一级就借助自己的电源，重新给出一个干净的高电平或低电平。这样，小小的偏差就不必一站一站积累下去。当然，如果原话已经含糊到分不清“八点”还是“九点”，大声复述也救不回来；电压越过了容许范围，数字电路同样不能保证猜对。

## Notation

| Symbol | Meaning | Keep distinct |
|---|---|---|
| $V_{DD}$ | Positive supply voltage, measured relative to ground | Not the number 1; logic 1 is a category |
| $V_{GS}=V_G-V_S$ | Gate-to-source voltage | A gate voltage alone does not specify it |
| $V_{DS}=V_D-V_S$ | Drain-to-source voltage | Supplies the lateral field driving channel current |
| $V_{th}$ | MOSFET threshold voltage | A device parameter, not the gate's input guarantee |
| $V_{IL},V_{IH}$ | Highest guaranteed LOW input; lowest guaranteed HIGH input | The gap between them is not a valid third logic value |
| $V_{OL},V_{OH}$ | Highest guaranteed LOW output; lowest guaranteed HIGH output | Specified at particular supply, load and temperature conditions |
| $C_L,R_{on}$ | Effective load capacitance and conducting-path resistance | Approximate models, not fixed universal constants |

## 1. Make a conducting path with a field

Silicon forms a crystal of covalent bonds. Some electrons can move through it; a missing electron in the valence-band population behaves as a mobile positive **hole**. A hole is a useful description of electron motion, not a tiny proton wandering through silicon.

**Doping** introduces controlled impurities. Donors make electrons the majority mobile carriers in **n-type** material; acceptors make holes the majority in **p-type** material. The bulk material remains approximately electrically neutral: “n-type” does not mean a negatively charged block.

For a simplified **enhancement-mode NMOS**, put two strongly n-type regions — source and drain — in a p-type body. Place a conductive gate over the intervening surface, separated from it by a thin insulator. Tie the body to the source for this first model.

![[transistor-field-and-cmos.svg|760]]

*Left: a conceptual planar NMOS cross-section, with the body tied to the source. The field changes the carrier population near the surface. Right: two complementary controlled paths make an inverter; the rectangles are switch-model symbols, not a fabrication layout.*

With a sufficiently positive $V_{GS}$, the electric field repels holes from the surface and attracts electrons. The surface becomes an electron-rich **inversion layer**, joining source to drain. A positive $V_{DS}$ then drives electrons from source toward drain; **conventional current** runs in the opposite direction.

The gate did not pour these electrons through the insulator. It changed the electric potential and hence the channel's carrier population. The voltage source connected to the drain/source circuit supplies the energy carried by the channel current.

A **PMOS** uses the complementary structure and a hole channel. It conducts strongly when its gate is sufficiently *below its source*: $V_{SG}=V_S-V_G$ exceeds the magnitude of its negative threshold. In an inverter, its source sits at $V_{DD}$, so a LOW gate turns it on.

> [!warning] “No gate current” needs a time scale
> An ideal gate insulator blocks steady conduction, but the gate is also a capacitor. Changing its voltage requires moving charge into or out of the gate electrode: $I=dQ/dt$. Real devices also leak. A MOSFET has a high input resistance, not an input that costs no energy to switch.

**Two meanings of gate:** the MOSFET's *gate terminal* controls one device; a *logic gate* is a circuit, often containing several transistors, that computes a Boolean function.

## 2. On and off are useful approximations

For an enhancement NMOS, increasing $V_{GS}$ makes the channel progressively more conductive. There is no microscopic click at $V_{th}$.

- **Below threshold:** the simplest model says off. Real devices still carry subthreshold and other leakage currents.
- **Above threshold, small $V_{DS}$:** the device behaves approximately like a gate-controlled resistor. This is the **linear**, **triode** or **ohmic** region.
- **Above threshold, larger $V_{DS}$:** the drain end of the inversion layer becomes depleted; the device enters **saturation**, where the simplest long-channel model makes current nearly independent of $V_{DS}$.

The name *saturation* is dangerous here. **A strongly conducting MOSFET used as a low-resistance closed switch is usually in its linear region**, once the voltage drop across it is small. MOSFET saturation does not mean “fully on with almost zero voltage drop.” A bipolar transistor uses *saturation* differently.

Nor is threshold voltage a promise of enough current for your load. A power MOSFET's quoted threshold may be measured at a tiny drain current; selecting a switch requires its on-resistance specification at the actual gate drive.

> [!tip] Start with differences, not labels
> If $V_G=3$ V and $V_S=2.5$ V, then $V_{GS}=0.5$ V. Calling the gate “HIGH” does not magically give it a 3 V gate-to-source drive. This is why source placement matters.

## 3. CMOS: pull up or pull down

Connect a PMOS from $V_{DD}$ to the output and an NMOS from the output to ground. Join their gate terminals to the input. Tie the PMOS body to $V_{DD}$ and the NMOS body to ground.

At the input rails, the ideal switch model gives:

| Input | PMOS pull-up | NMOS pull-down | Output |
|---|---|---|---|
| LOW, near 0 | Conducting | Off | HIGH, near $V_{DD}$ |
| HIGH, near $V_{DD}$ | Off | Conducting | LOW, near 0 |

**The output is the inverse of the input.** Importantly, the off transistor interrupts the direct supply-to-ground path. With a purely capacitive load, an ideal settled inverter draws no steady current. Real leakage and any external DC load change that conclusion.

In the transition region both devices may conduct. The output is then determined by their current balance and the load, and current can flow directly from supply to ground. Leaving an ordinary CMOS input floating or slowly wandering in this region is poor design.

### Build NAND from four transistors

For a two-input NAND:

- The **NMOS pull-down devices are in series**. Both $A$ and $B$ must be HIGH to connect the output to ground.
- The **PMOS pull-up devices are in parallel**. Either LOW input provides a path to the positive supply.

Thus only $A=B=1$ produces 0. For NOR, exchange series and parallel: either HIGH input can pull down, while both inputs must be LOW to pull up. This is De Morgan’s laws in [[Boolean Algebra]] made into conducting paths.

NAND and NOR are economical *static complementary CMOS* structures; adding an inverter gives AND or OR. Their universality is a mathematical construction result, not a claim that every processor is physically built only from NANDs. Real standard-cell libraries also contain inverters, XORs, multiplexers, flip-flops and compound gates. [SkyWater's open cell catalogue](https://github.com/google/skywater-pdk-libs-sky130_fd_sc_hd/tree/main/cells) makes the variety visible.

## 4. The digital contract — why noise need not accumulate

A logic family specifies **four** voltage boundaries. Consider an illustrative 3.3 V family; these are teaching numbers, not a real part's data sheet:

| Input accepted as | Input requirement | Output promised after settling |
|---|---|---|
| LOW | $0\le V_{in}\le0.8$ V | If the Boolean result is LOW: $0\le V_{out}\le0.2$ V |
| HIGH | $2.0\le V_{in}\le3.3$ V | If the Boolean result is HIGH: $3.1\le V_{out}\le3.3$ V |

The output bands fit **inside** the corresponding input bands. That spare room is the **noise margin**:

$$\boxed{NM_L=V_{IL}-V_{OL},\qquad NM_H=V_{OH}-V_{IH}.}$$

**Why subtract these particular numbers?** The worst LOW output starts at the *top* of its promised band. Added positive noise can raise it only as far as the receiver's LOW ceiling. The worst HIGH output starts at the *bottom* of its promised band; negative noise may lower it only as far as the HIGH floor.

![[transistor-voltage-contract.svg|760]]

*Left: the receiver accepts wider bands than the transmitter promises to deliver. Right: an illustrative inverter transfer curve, not a measured device. The flatter outer regions restore valid levels; the steep middle makes small input changes consequential.*

The **voltage transfer characteristic** plots settled $V_{out}$ against $V_{in}$. Near either rail, small input changes cause little output change. In the middle, the magnitude of the slope can exceed 1: small differences are amplified. A steep transition separates the two useful operating regions; it does not make every possible input safe.

There is **no guaranteed logic interpretation** for $V_{IL}<V_{in}<V_{IH}$. The voltage still exists physically. One device might respond HIGH, another LOW, and temperature can change the outcome. It is not a stable, specified “half-bit.”

Crucially, $V_{th}$ belongs to one transistor. $V_{IL}$ and $V_{IH}$ belong to the **whole gate's interface specification**. Do not substitute one for the others. [MIT's digital-abstraction lecture](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c3/c3s1/) develops this distinction between physical voltages and reliable logic ranges.

### Worked example — a battered LOW

A transmitter can output up to 0.2 V for LOW; a disturbance adds 0.45 V before the next inverter.

1. **Tool: worst-case voltage addition. Trigger: the disturbance raises a LOW signal.** The receiving input is at most $0.2+0.45=0.65$ V.
2. **Tool: the input contract. Trigger: we need a guaranteed interpretation.** Since $0.65\le0.8$, the receiver must accept LOW. Its output therefore settles HIGH, at least 3.1 V.
3. **Tool: noise-margin subtraction.** $NM_L=0.8-0.2=0.6$ V; $NM_H=3.1-2.0=1.1$ V. The 0.45 V disturbance fits inside the LOW margin.

Now change the disturbance to 0.9 V: the input may reach 1.1 V, in the unspecified band. The contract no longer promises recovery. **Signal restoration tolerates bounded damage; it cannot reconstruct arbitrary lost information.**

The same argument repeats along a chain: valid input → valid output → valid input, provided each interconnection's disturbance stays within its margin and each stage is allowed to settle. This is an invariant, not an assumption that errors mysteriously disappear.

![[transistor-restoration.mp4]]

*Watch the voltage bands, not just the bit labels: a disturbed LOW is restored through two inverters; then an excessive disturbance leaves the guarantee. Finally, follow the charge that makes restoration take time and energy.*

## 5. Why a switch cannot switch instantly

The next gate's input, the wiring and device junctions all contribute capacitance. To raise an output voltage, the pull-up must charge that **load capacitance**. To lower it, the pull-down must discharge it.

Recall from [[Capacitors]] that $Q=CV$. Approximate the pull-up by a constant resistance $R$ connected to $V_{DD}$, with an initially uncharged capacitor $C$ to ground. Then

$$I=\frac{V_{DD}-V}{R}=C\frac{dV}{dt}.$$

Separate and integrate with $V(0)=0$:

$$\int_0^V\frac{dV'}{V_{DD}-V'}=\int_0^t\frac{dt'}{RC}
\quad\Longrightarrow\quad
\boxed{V(t)=V_{DD}\left(1-e^{-t/(RC)}\right).}$$

The **time constant** is $\tau=RC$. At $t=\tau$, the output has reached about 63.2% of its final value. Reaching half the supply takes $t_{50}=RC\ln2\approx0.693RC$.

This is a load-charging estimate. Real propagation delay is measured between specified input and output crossings and depends on input slew, transistor behaviour, load and operating conditions. A MOSFET is not a fixed resistor throughout a transition.

**Fan-out** is how many inputs an output drives. Even when their steady input currents are tiny, their capacitances add. More loads generally mean more charge, longer delay or a larger driver. A stronger driver itself presents more input capacitance to the previous stage: the cost moves upstream.

## 6. Why chips get hot

During a complete charge from 0 to $V_{DD}$, a constant-voltage supply delivers

$$E_{supply}=\int V_{DD}I\,dt=V_{DD}\int dQ
=V_{DD}(CV_{DD})=CV_{DD}^{\,2}.$$

But the capacitor stores only

$$E_C=\int_0^{CV_{DD}}\frac{Q}{C}\,dQ=\tfrac12CV_{DD}^{\,2}.$$

The other half was dissipated in the charging path. Discharging through the pull-down dissipates the stored half. Therefore one full LOW → HIGH → LOW cycle dissipates $CV_{DD}^{\,2}$ in this ordinary resistive-switching model.

If a node has, on average, $\alpha$ LOW → HIGH events per clock cycle at clock frequency $f$,

$$\boxed{P_{load}=\alpha CV_{DD}^{\,2}f.}$$

Here $\alpha$ counts **charging events**, not every edge. If you count both rising and falling transitions, a factor of one-half enters instead. State the convention before comparing formulas.

This load term is not total chip power. Internal nodes also charge; both transistors can briefly conduct; leakage draws power even without switching. [Texas Instruments' CMOS power report](https://www.ti.com/lit/an/scaa035b/scaa035b.pdf) separates load charging, internal switching and static contributions.

### Worked example — time and heat from one capacitor

Use an illustrative $R=1.0\text{ k}\Omega$, $C=10\text{ pF}$ and $V_{DD}=3.3$ V.

1. **Tool: $RC$. Trigger: a resistance charges a capacitive load.** $\tau=10$ ns, so $t_{50}=6.93$ ns. To reach the example HIGH-input threshold of 2.0 V requires $t=-RC\ln(1-2/3.3)=9.32$ ns.
2. **Tool: supply energy $CV^2$. Trigger: one complete output charge.** $E_{supply}=108.9$ pJ; the stored energy is 54.45 pJ. After discharge the full 108.9 pJ has become heat in the resistive paths.
3. **Tool: energy per event × event rate.** At $f=10$ MHz and $\alpha=0.2$, there are two million charging events each second. The load-switching power is $217.8\,\mu\text{W}$.
4. **Tool: ratio at fixed $C,\alpha,f$. Trigger: comparing supply choices.** Reducing 3.3 V to 2.5 V multiplies this power by $(2.5/3.3)^2\approx0.574$. It may also weaken the drive and slow the circuit; energy savings do not guarantee unchanged speed.

![[transistor-delay-and-energy.svg|760]]

## Real-world use — your laptop's heat and your sensor's output

**Clock gating** stops selected blocks from switching when idle, reducing their activity factor. **Voltage and frequency scaling** trades performance against switching energy and power. These are physical reasons a processor changes its operating point with workload; a bit is abstract, but repeatedly moving its charge is not.

**A sensor talking to a microcontroller** must satisfy a voltage contract. “3.3 V logic” and “5 V logic” are not enough information: compare the source's guaranteed output levels with the receiver's required input levels, under the actual conditions. For example, the [TI SN74HC04 data sheet](https://www.ti.com/lit/ds/symlink/sn74hc04.pdf), §6.3, requires at least 3.15 V for HIGH at a 4.5 V supply. A nominal 3.3 V source may have a lower guaranteed HIGH output under load. Check both sides, and separately check the receiver's permitted input voltage: logical compatibility does not imply electrical tolerance.

**An SSD** deliberately changes a memory transistor's threshold by storing charge. [[Quantum Tunnelling]] explains the programming/erasing connection. A normal logic MOSFET does not need tunnelling to carry its useful channel current; leakage and flash programming are different roles for quantum physics.

## Try it — keep the analog voltage until the last step

This deliberately invented inverter curve makes the distinction inspectable. It is continuous and restores the example's valid bands; it is **not SPICE, a measured chip, or a device-physics model**.

```python
from math import exp, log

VDD, VIL, VIH = 3.3, 0.8, 2.0

def inverter(v):
    if not 0 <= v <= VDD:
        raise ValueError("This toy model only covers the supply range")
    if v <= VIL:
        return VDD - 0.2 * v / VIL
    if v >= VIH:
        return 0.2 * (VDD - v) / (VDD - VIH)
    return 3.1 - 2.9 * (v - VIL) / (VIH - VIL)

def logic(v):
    return 0 if 0 <= v <= VIL else 1 if VIH <= v <= VDD else None

v = 0.2 + 0.45
for stage in range(3):
    print(stage, round(v, 4), logic(v))
    v = inverter(v)
# 0 0.65 0; 1 3.1375 1; 2 0.025 0

R, C = 1000, 10e-12
print("t50/ns:", R * C * log(2) / 1e-9)
print("V at one time constant:", VDD * (1 - exp(-1)))
```

Try starting at 1.1 V. The function still returns a numerical output, but `logic(1.1)` returns `None`: **a prediction from this particular toy curve is not a guarantee for a real component**. Then increase $C$ tenfold and predict both delay and switching energy before calculating.

The companion [Python lab](transistor-lab.py) also checks the CMOS NAND/NOR paths and the numerical examples.

## Beyond Syllabus — the analog model underneath the switch

### Where the square law comes from

Recall that gate voltage attracts channel charge. In a simple long-channel NMOS, with constant threshold, constant mobility and negligible body effect, the magnitude of inversion charge per unit area at local channel potential $V$ is approximately $C_{ox}(V_{GS}-V_{th}-V)$, where $C_{ox}$ is oxide capacitance **per unit area**.

Drift speed is mobility $\mu$ times the lateral field. For channel width $W$, length $L$ and steady current $I_D$, multiplying charge per area × width × speed gives

$$I_D\,dx=\mu C_{ox}W(V_{GS}-V_{th}-V)\,dV.$$

Integrate from source to drain and write $\beta=\mu C_{ox}W/L$:

$$\boxed{I_D=\beta\left[(V_{GS}-V_{th})V_{DS}-\tfrac12V_{DS}^2\right].}$$

This applies for $V_{GS}>V_{th}$ and $0\le V_{DS}\le V_{GS}-V_{th}$. At small $V_{DS}$, the quadratic term is small, so $R_{on}\approx1/[\beta(V_{GS}-V_{th})]$.

At the drain-end pinch-off boundary $V_{DS}=V_{GS}-V_{th}$, the model gives $I_{D,sat}=\tfrac12\beta(V_{GS}-V_{th})^2$. Beyond it, the ideal model holds this current constant. **Pinch-off does not mean the current stops:** carriers travel through the drain-end high-field region. Useful channel transport here is drift, not tunnelling. [MIT's gradual-channel derivation](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/eeb94eab00ebb62a3fde0eec1484bc08_MIT6_012F09_lec11_gradual.pdf) develops the more complete model.

Real short-channel devices need additional physics, including velocity saturation and electrostatic effects. Fin-shaped and gate-all-around structures improve gate control of the channel; a modern process-node name is not a literal measurement of every transistor's gate length. The square law is a teaching model, not a modern CPU simulator.

### Why a clock does not abolish the transition region

Recall that a gate needs time to settle. A chain's total delay limits how soon a register may safely sample its result. Inputs arriving too close to a storage element's sampling edge can lead to **metastability**; noise margins alone do not solve that timing problem. [[Flip-Flops]] connects the voltage-level story to setup and hold timing.

## Exam Notes

**The detailed MOSFET/CMOS treatment is enrichment.** No transistor transfer-curve, noise-margin or CMOS switching-power outcome is specified in the checked Cambridge 0625/9702, IB Physics (first assessment 2025), or AP Physics 1, 2 and C course descriptions. Their circuit, field, capacitor and energy tools support the derivations; that does not make transistor engineering a named requirement.

For CS, distinguish the **Boolean interface** from its physical implementation:

| Course | What is specified | What this adds |
|---|---|---|
| Cambridge 0478 (2026–28) | §10: six gates, circuits, expressions and truth tables; §3.3.3: flash storage, including transistor control/floating gates | Why voltage-controlled channels and reliable logic levels work; detailed flash operation belongs with [[Secondary Storage]] and [[Quantum Tunnelling]] |
| Cambridge 9618 (2027–29) | §3.2 gates/circuits; §15.2 Boolean algebra, Karnaugh maps, adders and flip-flops | Device physics, CMOS networks, voltage contracts and switching energy |
| IB CS (first assessment 2027) | A1.2.3–A1.2.5: gates, truth tables, simplification and diagrams, including XNOR | The analog implementation underneath those logical operations |
| AP CSA | Java programming; transistor circuits are not a specified topic | Enrichment only |

For a logic-circuit question, use the stated Boolean behaviour. For the engineering examples above, identify the supply, load, input/output guarantees and time scale before calculating. Neither a MOSFET's threshold nor a toy simulation certifies a real interface.

## Connections

- **[[Electric Field]]** — voltage changes charge distribution without charge crossing the gate insulator.
- **[[Capacitors]]** — storing charge makes switching take time and energy; supplies the $Q=CV$ and $\tfrac12CV^2$ foundations.
- **[[Logic Gates]] and [[Boolean Algebra]]** — the Boolean functions whose physical contracts CMOS implements.
- **[[Flip-Flops]]** — combining gates with feedback makes storage; timing brings additional obligations.
- **[[Quantum Tunnelling]]** — leakage in scaled devices and deliberate charge transfer in flash memory.
- **[[The Boolean-to-Silicon Bridge]]** — the historical route from logical operations to switching circuits.
- **[[The GPU — From Triangles to Tensors]]** — doing more operations at once still faces charge movement, bandwidth and power constraints.
- **[[Change the Representation]]** — interpreting voltage bands as bits preserves the distinction useful for computation while discarding harmless analog detail.

## LaTeX Reference

| Expression | LaTeX |
|---|---|
| $V_{GS}=V_G-V_S$ | `V_{GS}=V_G-V_S` |
| $NM_L=V_{IL}-V_{OL}$ | `NM_L=V_{IL}-V_{OL}` |
| $V(t)=V_{DD}(1-e^{-t/(RC)})$ | `V(t)=V_{DD}(1-e^{-t/(RC)})` |
| $P=\alpha CV_{DD}^{\,2}f$ | `P=\alpha CV_{DD}^{\,2}f` |
