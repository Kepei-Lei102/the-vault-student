---
chinese: 时钟域与亚稳态 (shízhōngyù yǔ yàwěntài)
prerequisites:
  - "[[Flip-Flops]]"
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Gray Code]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/computer-architecture
  - domain/digital-circuits
  - level/A-Level
  - level/university
  - type/deep
  - notation/frequency-multiply-divide
  - misconception/one-cpu-one-clock
  - misconception/multiplier-uses-a-multiplier
  - misconception/metastability-is-a-bug-you-can-fix
  - misconception/synchronizer-works-on-buses
---

# Clock Domains and Metastability 时钟域与亚稳态

> *You picture a computer keeping time to a single drumbeat. It doesn't. Inside one chip a dozen clocks run at once, each at its own tempo, most of them deaf to the others — and the hardest, subtlest engineering in the whole machine lives in the handful of wires where one clock's world touches another's. Cross that boundary carelessly and a flip-flop does the one thing the [[Flip-Flops|last card]] warned about: it hangs between $0$ and $1$ and picks by chance.*

## Definition

A **clock domain** (时钟域) is a region of logic all driven by the *same* clock signal. Inside one domain, timing can be checked against a shared reference: the designer must account for clock skew and verify that each path meets setup and hold requirements, so the domain can step forward in lockstep — exactly the disciplined march the [[Flip-Flops|flip-flop]] and [[CPU Architecture and the Fetch-Execute Cycle|register]] rely on.

A real chip is **not** one domain. It is many — cores, cache interconnect, memory controller, PCIe, USB — each ticking at its own frequency, because each has its own best speed. **Clock domain crossing** (CDC, 跨时钟域) is what happens when a signal made in one domain has to be read in another, and it is the source of the most maddening class of hardware bug there is: the kind that works 99.999% of the time.

Two questions organise the whole topic:

1. **Where do all these different frequencies come from?** — one crystal, a tree of multipliers and dividers.
2. **What goes wrong at the seams, and how is it made safe?** — metastability, and the synchronizer.

### 中文锚点

| English | 中文 | 一句话 |
|---|---|---|
| clock domain | 时钟域 (shízhōngyù) | 由**同一个**时钟驱动的一片逻辑 |
| clock domain crossing | 跨时钟域 (kuà shízhōngyù) | 信号从一个时钟域进入另一个 |
| metastability | 亚稳态 (yàwěntài) | 触发器卡在 0 与 1 之间，结局随机 |
| synchronizer | 同步器 (tóngbùqì) | 两级触发器，给亚稳态时间平息 |
| phase-locked loop (PLL) | 锁相环 (suǒxiànghuán) | 用反馈把参考频率**倍频**上去 |
| base clock / multiplier | 基准时钟 / 倍频 (bèipín) | 核心频率 = 基准 × 倍频系数 |
| jitter / skew | 抖动 / 偏斜 | 时钟边沿在时间上的抖动 / 到达的先后差 |

核心一句话：一颗晶振 → 锁相环倍频 + 分频 → 许多时钟域；**域内同步，域间危险**；跨域靠同步器把亚稳态的概率压到几乎为零。

---

## One crystal, many clocks — the clock tree

Why not run the whole chip off one fast clock and be done with it? Three reasons, each fatal on its own:

- **Power.** Dynamic power grows with frequency: $P \propto C V^2 f$. Running a block faster than it needs to burns energy for nothing. The memory bus, USB, and the display controller have no reason to run at core GHz — so they don't.
- **Physics.** Distributing a single multi-GHz edge across a whole chip so it arrives *everywhere at once* is impossible past a point — the speed of the signal across the die and the variation in wire delay (**clock skew**) blow the timing budget. Smaller domains are easier to keep in step.
- **Independence.** A CPU core wants to change its own speed on the fly (turbo up under load, idle down to save battery — **dynamic voltage and frequency scaling**) without dragging the memory controller or PCIe along.

So a chip runs **one** (or a few) cheap, extremely stable references — a **quartz crystal oscillator**, typically a low frequency like 25 MHz, or a 100 MHz **base clock** (BCLK) derived from it — and builds every other clock from it: **multiply up** with PLLs, **divide down** with counters.

![[clock-tree.svg|660]]

One reference in; a whole forest of frequencies out, each feeding its own domain. The crystal is the single source of truth for time; everything else is that truth scaled.

---

## The PLL — and why the multiplier *is* a divider

Here is the twist your intuition should snag on. A [[Flip-Flops|toggle flip-flop]] can only ever *halve* a frequency; a chain of them **divides** by any integer. Flip-flops cannot *multiply* a clock. So how does a 100 MHz base clock become a 4.5 GHz core?

The answer is a **phase-locked loop (PLL)** — and the beautiful part is that a PLL multiplies *by putting a frequency divider in its own feedback path*:

![[pll-multiplier.svg|660]]

- A **voltage-controlled oscillator (VCO)** produces some high frequency $f_{out}$.
- A **÷N counter** — flip-flops, the exact divider from the last topic — divides it down to $f_{out}/N$.
- A **phase detector** compares that divided-down signal against the reference $f_{ref}$ and nudges the VCO until the two line up.

When the loop **locks**, the two phase-detector inputs match, so $f_{out}/N = f_{ref}$, which means

$$\boxed{\,f_{out} = N \times f_{ref}\,}$$

**That $N$ is the "multiplier."** The base-clock-times-multiplier you see quoted for a CPU — say a 100 MHz BCLK and a $\times 45$ core ratio giving 4.5 GHz — is a PLL with $N = 45$ in its feedback divider. When an overclocker changes the multiplier in an unlocked ("K") chip, they are literally changing $N$ — the divide ratio of a flip-flop counter buried inside the loop. The frequency divider you just learned is not a footnote to clock generation; **used backwards, inside a loop, it is the thing that sets the multiply ratio.**

> [!info] Two ways to overclock
> Raising the **base clock** speeds up *everything* derived from it at once (cores, cache, sometimes the buses) — powerful but destabilising, because every domain is pushed together. Raising a single **multiplier** speeds up just that one domain (usually the cores) and leaves the rest at spec. That separation — one knob per domain — is only possible *because* each domain has its own PLL hanging off the shared reference.

---

## Clock domains and the crossing problem

Within a domain, the tools of the [[Flip-Flops|flip-flop]] card guarantee correctness: a signal launched by one edge is required to be stable (to meet **setup and hold** — quiet for a moment before the edge and a moment after) by the time the next edge samples it. The designer's timing tools check every path and certify it.

Cross a boundary and that guarantee evaporates. There are two cases, and they are night and day:

- **Related clocks** — both derived from the *same* PLL, one an integer division of the other (say a domain at $f$ and another at $f/2$). Their edges are **phase-locked**: they line up predictably, and you always know exactly when an edge in one coincides with an edge in the other. Crossing between them still needs care, but the timing is *deterministic* — this is the case your intuition of "they sync every so often" describes exactly.

- **Unrelated clocks** — clocks with no guaranteed phase relationship. They may have different frequencies or even the same nominal frequency from independent oscillators. Their relative edge timing cannot be treated as fixed, so an incoming transition can land inside the receiver's setup/hold window. **Different numerical frequencies alone do not prove asynchrony**: clocks derived with a controlled relationship can run at different rates and still be timed synchronously. [AMD's clock-relationship definition](https://docs.amd.com/r/en-US/ug949-vivado-design-methodology/Synchronous)

And when a flip-flop is sampled mid-change, it does the thing the last card dramatised.

---

## Metastability — the coin flip, returned

When a flip-flop's input changes within its setup/hold window, the device can be knocked into **metastability** (亚稳态): its output hangs at neither a clean $0$ nor a clean $1$, hovering at an in-between voltage, and only after an unpredictable delay does it topple — to $0$ or to $1$, *chosen by chance*.

This is not a new phenomenon. **It is the released $S=R=1$ race from [[Flip-Flops]], wearing work clothes.** A bistable element has two stable valleys — storing $0$ and storing $1$ — with a knife-edge ridge between them:

![[metastability-synchronizer.svg|680]]

Sample the flip-flop cleanly and it drops into a valley at once. Sample it at the worst instant and you balance it *on the ridge*, like a ball set exactly on a hilltop. It cannot stay there — but nothing bounds how long it teeters before rolling, and you cannot predict which side it rolls to. Small analogue differences, noise and device behaviour determine the outcome; digital logic does not provide a bounded resolution time.

> **You cannot design metastability away.** It is fundamental, the same way the SR race is fundamental — any device that decides between two states in bounded time can be caught between them. The honest engineering goal is never "eliminate it"; it is "make the probability of it *lasting long enough to matter* small enough to meet the system's reliability target."

---

## The synchronizer — buying time with a second flip-flop

The fix is almost insultingly simple: **give the metastable state time to settle before anyone looks at it.** Chain two flip-flops in the receiving domain — a **two-flip-flop synchronizer**:

- The **first** flip-flop samples the incoming signal. It *may* go metastable.
- The next receiving edge supplies a **settling interval**, reduced by register delays, routing and the second register's setup requirement. The first stage should drive the synchronizer chain rather than unrelated downstream logic.
- The **second** flip-flop then samples the (now almost-certainly-resolved) value and passes it into the domain as a trustworthy signal.

The probability that the first flip-flop is *still* metastable after time $t$ falls off **exponentially**, so the reliability — the **mean time between failures** — is roughly

$$\text{MTBF} \approx \frac{e^{\,t/\tau}}{T_0 \, f_{clk} \, f_{data}}$$

where $\tau$ is the flip-flop's settling time constant, $f_{clk}$ and $f_{data}$ are the sampling and data rates, and $T_0$ is a device constant. The exponential in the numerator is the whole game: increasing the available settling time by $\Delta t$ multiplies the modelled MTBF by $e^{\Delta t/\tau}$. Whether two stages suffice depends on the device, clock and transition rates, physical timing and reliability target; use characterised device data and timing analysis. The cost is added receiving-clock latency and a residual failure probability. A short pulse can still be missed completely; event transfer may need a toggle or handshake. [Intel: settling time and MTBF](https://cdrdv2-public.intel.com/650346/wp-01082-quartus-ii-metastability.pdf)

> [!warning] A synchronizer works for **one bit** — never a bus
> Each flip-flop resolves *independently*. Put a two-flip-flop synchronizer on every wire of an 8-bit bus and the bits will resolve on their own schedules — you can latch some bits from the old value and some from the new in the same cycle, and read a number that was never actually sent. Multi-bit data needs a different tool.

---

## Crossing many bits — Gray code and the async FIFO

The bus problem has a clean root: when several bits change at once, a mid-transition sample can read *any* mixture of old and new. Watch a 3-bit binary counter step from $3$ to $4$:

$$011 \to 100 \qquad (\text{all three bits flip at once})$$

Sample during that flip and you might read $111$ (7) or $000$ (0) or anything between — values the counter never held. The repair is to **change only one bit at a time**, which is exactly the property of **[[Gray Code]]** — the same one-bit-apart ordering that made neighbouring cells adjacent in [[Karnaugh Maps]]. In Gray code the step is

$$010 \to 110 \qquad (\text{one bit flips})$$

so an isolated adjacent transition changes only one bit. After synchronisation, it can be interpreted as the old or new count rather than an arbitrary mixture. This relies on registered Gray outputs and suitable path-delay/skew constraints; Gray encoding does not itself eliminate metastability or make arbitrary multi-step data changes safe.

This is how a real cross-domain queue works — the **asynchronous FIFO**, the standard way to move a stream of data between two unrelated clocks:

- The writer (domain A) pushes data and advances a **write pointer**; the reader (domain B) pops and advances a **read pointer**.
- Each side must see the *other's* pointer to know if the FIFO is full or empty — a genuine clock-domain crossing. So the pointers are kept in **Gray code** and passed through synchronizers: adjacent source counts change one bit. With suitable timing constraints and synchronizers, the receiver obtains a delayed pointer suitable for conservative full/empty decisions; it may skip source counts, and the design must allow for that delay.
- The queue itself absorbs the rate mismatch: bursts can fill and drain it. A finite FIFO cannot absorb a sustained rate mismatch forever: full/empty handling and flow control are still required.

For a single control signal — "go", "done" — a lighter **request/acknowledge handshake** (each side synchronizes the other's one-bit flag) does the job without a whole FIFO.

---

## Beyond the syllabus — the wider picture

- **GALS — globally asynchronous, locally synchronous.** The modern chip's actual philosophy: build islands of clean synchronous logic (the domains) and let them float asynchronously relative to each other, joined only through synchronizers and FIFOs. The synchronous discipline is kept where it is cheap (inside a domain) and abandoned where it is impossible (across the whole die).
- **Jitter and skew.** Even *one* clock is imperfect: **skew** is the same edge arriving at different places at slightly different times; **jitter** is the edge itself wandering cycle-to-cycle. Both eat into the timing budget, and fighting them is why clocks are distributed through carefully balanced **H-tree** networks.
- **The clockless road not taken.** Fully **asynchronous (clockless) logic** does away with the global clock entirely — no domains, no crossings, potentially lower power. It has never won the mainstream, because the synchronous model's one gift — *a single edge that says "now"* — makes design, testing, and reasoning about a billion transistors tractable. We keep the clock because it keeps us sane.
- **The signature bug.** A missing or wrong synchronizer produces the worst kind of failure: rare, non-deterministic, unreproducible on the bench, and dependent on temperature and voltage. "It fails once a week and we can't catch it" is the classic fingerprint of an unprotected clock-domain crossing.

---

## Worked examples

### 1 — Base clock and multiplier

**Trigger: a locked PLL with a specified divider → use its feedback equality.** A 100 MHz reference and divider $N=43$ give $f_{out}/43=100$ MHz, hence $f_{out}=4.3$ GHz. A second PLL with $N=32$ gives 3.2 GHz. **Tool boundary:** these frequencies alone do not tell us whether their phase relationship is guaranteed. Inspect the clock architecture and timing constraints before classifying the crossing as synchronous or asynchronous.

### 2 — Why not synchronize each bus wire?

**Trigger: several bits of one value change together → preserve word coherence.** A four-bit bus changes from $0111$ to $1000$. Independent synchronizers can deliver some new bits and some old bits, for example $1111$, a value the sender never sent. **Tool: a handshake with data held stable, or an asynchronous FIFO.** Gray coding is useful for an adjacent-count pointer: binary 7 and 8 encode as $0100$ and $1100$, one bit apart. It is not a general repair for arbitrary bus values that jump by several counts.

### 3 — More settling time, not a magic number of stages

**Trigger: compare two synchronizer designs with other factors fixed → take an MTBF ratio.** Suppose characterised data gives $\tau=50$ ps and an added stage provides **800 ps of usable settling time** after timing overheads. Then

$$\frac{\mathrm{MTBF}_{new}}{\mathrm{MTBF}_{old}}=e^{800/50}=e^{16}\approx8.89\times10^6.$$

This is a large improvement, but the ratio alone does not supply an absolute lifetime. **Tool boundary:** absolute MTBF also needs $T_0$, actual settling time, receiving frequency and input transition rate. “Two stages” is not a universal reliability certificate.

---

## Exam Notes

### Cambridge 9618 and 0478

**Clock-domain crossing, synchronizer design and metastability calculations are enrichment.** 9618 §4.1 examines the system clock and performance factors including clock speed; §15.2 examines SR/JK flip-flop circuits, truth tables and their storage role. The 2027–29 syllabus does **not** explicitly require setup/hold timing or the MTBF formula. 0478 §3.1 covers CPU architecture and performance, not CDC design. Use [[Flip-Flops]] and [[CPU Architecture and the Fetch-Execute Cycle]] for those examined foundations.

### IB Computer Science — first assessment 2027

A1.1 includes CPU components, GPUs, primary memory, the fetch–decode–execute cycle and additional hardware outcomes; it does not stop at the CPU alone. It does not specify PLLs, metastability, synchronizer chains or Gray-coded FIFO crossings. These explain implementation issues beyond those outcomes, rather than closing a separate syllabus row.

### Where it is not examined

The clock-crossing mechanisms and calculations above are not specified outcomes in Cambridge 0478 (2026–28), 9618 (2027–29), IB CS (2027) or AP Computer Science A. They belong to digital-design and computer-organisation study, and to practical FPGA/SoC engineering.

---

## Connections

- **Parent:** [[Flip-Flops]] — metastability *is* the released $S=R=1$ race; and the $\div N$ counter that sets a PLL's multiply ratio is the frequency divider built there. Two ideas from one card, both cashed here.
- **The safe-crossing trick:** [[Gray Code]] — one-bit-at-a-time counting makes a mid-flight sample harmless; [[Karnaugh Maps]] — the same single-bit-adjacency that made map neighbours combine.
- **The clock in action:** [[CPU Architecture and the Fetch-Execute Cycle]] — the clock that steps the registers each cycle; [[Pipelining and Simultaneous Multithreading]] — the frequency that pipelining races against, and the per-core scaling that gives each core its own domain.
- **A domain of its own:** [[RAM and the Memory Hierarchy]] — core and memory interfaces can occupy different clock domains; the actual clock relationship determines how their crossings must be handled.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $f_{out} = N \times f_{ref}$ | `f_{out} = N \times f_{ref}` | PLL multiply — $N$ is the feedback-divider ratio (the "multiplier") |
| $P \propto C V^2 f$ | `P \propto C V^2 f` | dynamic power grows with frequency — why domains run slow when they can |
| $\text{MTBF} \approx \dfrac{e^{\,t/\tau}}{T_0 f_{clk} f_{data}}$ | `\dfrac{e^{t/\tau}}{T_0 f_{clk} f_{data}}` | synchronizer reliability — exponential in settling time $t$ |
| $011 \to 100$ | `011 \to 100` | binary: many bits flip at once (glitch risk on crossing) |
| $010 \to 110$ | `010 \to 110` | Gray: exactly one bit flips (safe crossing) |
