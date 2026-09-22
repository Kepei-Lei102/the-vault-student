---
chinese: 触发器
prerequisites:
  - "[[Logic Gates]]"
  - "[[Boolean Algebra]]"
  - "[[Karnaugh Maps]]"
leads_to:
  - "[[RAM and the Memory Hierarchy]]"
  - "[[Clock Domains and Metastability]]"
tags:
  - subject/computer-science
  - domain/logic
  - domain/digital-circuits
  - level/A-Level
  - curriculum/Cambridge-9618
  - curriculum/A-Level
  - syllabus/9618-15-2
  - type/deep
  - type/technique
  - notation/Q-and-Q-bar
  - notation/AND-dot
  - notation/OR-plus
  - misconception/sr-11-means-set-and-reset
  - misconception/flip-flop-table-is-stateless
  - misconception/clock-is-just-another-input
---

# Flip-Flops 触发器

> **Every circuit so far forgets.** Hand an adder new inputs and it computes the new answer with no memory of the old one — a gate is a function of the *present*. To store a bit, a circuit's output must depend on its *past*, and the trick that buys a past is shameless: **feed the output back into the input.** The circuit that results — the flip-flop — is the atom of computer memory. Every register, every counter, cache uses closely related bistable SRAM cells.

## Definition

Everything built from [[Logic Gates]] so far — De Morgan rewrites, Karnaugh-minimised alarms, the [[Half-Adder and Full-Adder|full adder]] — is **combinational logic** (组合逻辑): the outputs are a pure Boolean function of the current inputs. Same inputs, same outputs, always; the truth table is the entire story, and the circuit has no memory of anything.

A **flip-flop** is the simplest circuit that breaks this rule. It has **two stable states**, it stays in whichever state it was last put, and its inputs are used not to *compute* the output but to *change the state*. It is **sequential logic** (时序逻辑): the output depends on the history of the inputs, not just their present values. One flip-flop stores exactly **one bit**.

The structural difference is visible at a glance: in a combinational circuit, signals flow one way, inputs to outputs. In a flip-flop, there is a **feedback loop** — an output wired back to an input. The loop is not a bug. The loop *is* the memory.

### 中文锚点

按一下空调的开机键，手松开了，空调还在运行。按键的动作已经结束，设备却记住了“开着”这个状态。能存住一个比特，意义就在这里：**现在有没有人按键，不再是决定状态的唯一依据。** 在最基本的电子记忆电路里，输出会反馈到输入，让电路在通电时维持两种稳定状态中的一种；要换状态，得靠新的控制信号。信号可以一闪而过，它留下的状态却能保留下来。

### 术语对照

| English | 中文 | 一句话 |
|---|---|---|
| flip-flop | 触发器 (chùfāqì) | 时钟边沿触发的存储元件 |
| latch | 锁存器 (suǒcúnqì) | 锁 + 存 — 把一位**锁**住并**存**着（中文比英文更直白） |
| combinational logic | 组合逻辑 | 输出只由当前输入**组合**而成，无记忆 |
| sequential logic | 时序逻辑 | 有"时"有"序" — 输出依赖输入的历史 |
| set / reset | 置位 / 复位 | S 把 Q 置成 1；R 把 Q 复成 0 |
| toggle | 翻转 | 状态取反；JK 在 $J=K=1$ 时翻转 |
| clock | 时钟 (shízhōng) | 一个时钟域内的同步节拍 |

---

## The loop that remembers

Start with the smallest possible self-reference: wire a NOT gate's output straight back to its own input.

![[feedback-loop-paradox-memory.svg|660]]

The ideal Boolean model demands $Q = \overline{Q}$: no **binary** value satisfies it. This resembles the self-reference in [[Stories/Russell's Paradox in the Post]], but it does not by itself predict a physical oscillator. A real inverter has continuously varying voltages and can sit near its switching threshold. Oscillation requires suitable gain and delay; a ring oscillator commonly uses an odd chain of three or more inverters. [TI's unbuffered inverter documentation](https://www.ti.com/product/SN74LVC1GU04-Q1) explicitly distinguishes digital switching from operation in the analogue linear region.

Now add a second NOT gate to the loop. The demand becomes $Q = \overline{\overline{Q}} = Q$ — satisfied by **both** $Q=0$ and $Q=1$. Two inverters in a loop have **two stable states**, each holding the other up: the left gate drives the right, the right drives the left right back, forever, for as long as the power is on. This is **bistability**, and it is precisely the cross-coupled inverter pair at the heart of the SRAM cell in [[RAM and the Memory Hierarchy]].

> **Count the inversions to find the binary fixed points.** An odd inverter loop has none; an even loop permits two. Whether a physical circuit oscillates, holds a bit or sits at an intermediate voltage also depends on its analogue dynamics. The useful memory here is the regenerative, cross-coupled pair.

One problem remains: the two-inverter loop is stable but **sealed** — it has no inputs. It will hold a bit forever, but you have no way to tell it *which* bit. To write into the loop, you need a handle.

---

## The SR flip-flop — a loop with handles

Replace each NOT with a **NOR** gate ([[Logic Gates]]). A NOR with one input held at $0$ collapses into a NOT of the other — $\overline{x + 0} = \overline{x}$, the identity law of [[Boolean Algebra]] under a bar — so while both new inputs sit at $0$, this circuit is exactly the two-inverter loop. But now each gate has a spare input you can raise to seize control: **S** (set) and **R** (reset).

![[sr-latch-nor.svg|697]]

The two gates obey

$$Q = \overline{R + \overline{Q}} \qquad \overline{Q} = \overline{S + Q}$$

— each output is fed back into the *other* gate. Work through the four input combinations:

| $S$ | $R$ | $Q_{\text{next}}$ | Meaning |
|:-:|:-:|:-:|---|
| 0 | 0 | $Q$ | **hold** — the inverter loop, remembering |
| 1 | 0 | 1 | **set** — force the stored bit to 1 |
| 0 | 1 | 0 | **reset** — force the stored bit to 0 |
| 1 | 1 | — | **invalid** — never allowed |

Note the table's strangest feature, the very thing that makes it sequential: **the output column contains $Q$ itself.** A combinational truth table lists constants; a flip-flop's table says "whatever it was before." That single self-referencing entry is the memory.

**Why $S=R=1$ is forbidden.** Feed $1$ into both NORs and both outputs are forced to $0$ — so $Q$ and $\overline{Q}$ are *both* $0$, and the label $\overline{Q}$ is now a lie. Worse: when $S$ and $R$ return to $0$ together, both gates are released at once and the loop's final state is decided by which gate happens to switch a picosecond faster — a **race condition**. The stored bit ends up chosen by manufacturing noise, not by logic. A memory element that answers at random is worse than none, so the state is banned by decree.

Watch all four moods in turn — and watch the chip lose its mind on the last one, when you ask a thing called $Q$ and a thing called "not-$Q$" to both be $0$ at once:

![[sr-flip-flop-four-moods.svg|660]]

> [!info] The NAND twin
> Cross-couple two **NAND** gates instead and you get the same latch with everything upside-down: the inputs are **active-low** ($0$ asserts them, $S=R=1$ is the hold state, and $S=R=0$ is the forbidden one). Exam papers draw both versions; before answering, check which gate is used and therefore which level is "active." The structure — two gates, cross-coupled, spare input as handle — is identical.

---

## The clock — a million flip-flops marching in step

A real processor holds millions of flip-flops, and chaos follows if each updates whenever its inputs happen to twitch. So the machine imposes a shared drumbeat: the **clock** (时钟), a signal ticking billions of times per second. Gate $S$ and $R$ behind AND gates with the clock, and the flip-flop goes deaf between beats — inputs can change all they like, but the state updates only when the clock says *now*.

This beat is what the "GHz" on a CPU's spec sheet counts, and it is what makes "the state of the machine after step $n$" a meaningful phrase: on each tick, enabled registers in one synchronous clock domain update on their specified edges through the fetch–execute cycle.

---

## The JK flip-flop — the forbidden state, fixed

The SR flip-flop works, but that invalid row is an unexploded shell in the truth table. The **JK flip-flop** removes it with one elegant move: **before acting, ask the output for permission.** Feed the outputs back a *second* time, into the input gates themselves — $J$ is ANDed with $\overline{Q}$, and $K$ is ANDed with $Q$:

$$S_{\text{internal}} = J \cdot \overline{Q} \cdot clk \qquad R_{\text{internal}} = K \cdot Q \cdot clk$$

![[jk-flip-flop.svg|660]]

The feedback acts as a chaperone. If $Q=1$ already, then $\overline{Q}=0$ blocks the set path — you cannot set what is already set; only reset can get through. If $Q=0$, the reverse. **The internal SR core can never see $S=R=1$**, no matter what you feed $J$ and $K$, because the two feedback wires guarantee at most one path is open.

| $J$ | $K$ | $Q_{\text{next}}$ | Meaning |
|:-:|:-:|:-:|---|
| 0 | 0 | $Q$ | hold |
| 0 | 1 | 0 | reset |
| 1 | 0 | 1 | set |
| 1 | 1 | $\overline{Q}$ | **toggle** — the new trick |

The once-forbidden input pair now does something genuinely new: with $J=K=1$, whichever action would *change* the state is exactly the one the chaperone allows through, so every clock pulse **flips the bit**. Set becomes reset becomes set. The failure mode became a feature.

**Toggle is the seed of counting.** A toggling flip-flop's output flips once per clock pulse — one full output cycle per *two* clock cycles. It is a **frequency divider**: out comes exactly half the beat that went in.

![[jk-toggle-timing.svg|660]]

Chain the stages — each flip-flop's output clocking the next — and stage 1 flips half as often as stage 0, stage 2 half as often again: $\tfrac{1}{2}, \tfrac{1}{4}, \tfrac{1}{8}, \dots$ Read the stages together and they are **counting in binary** — place value ticking over in base 2 ([[Number Bases]]), each stage one power of 2. A binary counter is nothing but toggling flip-flops holding hands.

> [!info] Why real flip-flops trigger on the clock *edge*
> If the JK merely listens "while the clock is high," then with $J=K=1$ it toggles over and over for the whole half-cycle — the **race-around condition** — and the final value is anyone's guess. Real designs act only at the clock's rising (or falling) **edge**, the designated transition, with setup and hold timing requirements, so the intended operation is one toggle per beat (historically via a **master–slave** pair: one latch reads while the other publishes). The strict jargon: a *latch* is level-sensitive, a *flip-flop* is edge-triggered — though Cambridge papers say "flip-flop" for both, and so should your exam answers.

**A note on the name.** J and K stand for nothing. An engineer at Hughes Aircraft in the 1950s, Eldred Nelson, labelled the input pairs of the flip-flops in a patent alphabetically — one pair happened to land on J and K, and the name stuck. The oft-repeated story that they honour Jack Kilby is folklore: Kilby's integrated circuit came years later.

---

## The role of flip-flops as data storage

One flip-flop stores one bit, holding it as long as the power is on and rewriting it on demand. Here is where those stored bits are useful:

- **Registers.** A CPU register is a row of flip-flops sharing one clock — a 32-bit register is 32 of them side by side. The program counter, the accumulator, the instruction register of [[CPU Architecture and the Fetch-Execute Cycle]] are all just flip-flop rows.
- **Static RAM.** The SRAM cell of [[RAM and the Memory Hierarchy]] *is* the two-inverter bistable loop with access transistors as its handles — which is why SRAM needs no refresh (the loop holds itself) yet still forgets at power-off (the loop needs power to keep reinforcing). Your CPU's cache commonly uses these SRAM cells, which share the bistability principle but are not clocked flip-flops.
- **Counters and timers.** Toggling chains count clock pulses — program counters stepping, timers timing, the machinery of *when*.
- **Status flags.** The carry, zero, and overflow flags the ALU raises are single flip-flops each, remembering one fact about the last calculation.

The two halves of 9618 §15.2 are literally the two ingredients of a processor: **combinational circuits compute** (the adder — the ALU's heart), **sequential circuits remember** (the flip-flop — the registers and cache). Glue them together under one clock, and the datapath computes on the beat while the flip-flops carry the results forward to the next beat. That loop — compute, store, repeat — *is* a computer running.

---

## The D-type — capture one bit on an edge

Recall that the SR latch offers separate set and reset inputs. Driving them from **D** and its inverse removes the forbidden input combination in the ideal logic model. With an enable signal this gives a **D latch**: while enabled it is transparent, and when disabled it holds its value. This wiring alone does **not** make an edge-triggered device.

An **edge-triggered D flip-flop** adds timing structure, such as two latches enabled on opposite clock phases. Its behaviour is: **on the active clock edge, $Q := D$; between active edges, hold Q.** The data must satisfy setup and hold timing around that edge. This is the one-bit capture operation used throughout synchronous registers and pipeline stages. Register-file implementations can differ; SRAM cells use a bistable storage core rather than a clocked D flip-flop per bit.

---

## Worked examples

**1 — Derive the SR truth table from the circuit.** *Trigger: cross-coupled NOR gates → apply the NOR rule to the forced output first, then feed it back.* The gates give $Q = \overline{R + \overline{Q}}$ and $\overline{Q} = \overline{S + Q}$.
- $S=1, R=0$: bottom gate sees a $1$, so $\overline{Q} = \overline{1 + Q} = 0$; the top gate then sees $R=0, \overline{Q}=0$, so $Q = \overline{0+0} = 1$. **Set.** ✓
- $S=0, R=1$: symmetric — $Q = 0$, $\overline{Q} = 1$. **Reset.** ✓
- $S=0, R=0$: each NOR has one input at $0$, so each acts as a NOT of the fed-back signal: $Q = \overline{\overline{Q}}$, $\overline{Q} = \overline{Q}$ — the two-inverter loop, consistent with **both** states. Whichever state it was in, it keeps. **Hold.** ✓
- $S=1, R=1$: both gates see a $1$, both outputs forced to $0$ — $Q = \overline{Q} = 0$. **Invalid.**

**2 — Show that it remembers.** *Trigger: a set pulse ends → compare the forced state during the pulse with the hold state after it.* Start with $Q=0$. Pulse $S$: $S=1$ briefly, then back to $0$. During the pulse, $Q$ is driven to $1$ (case one above). After the pulse, inputs are $S=R=0$ — hold — and the loop sustains $Q=1$ on its own. *The pulse is gone; the bit remains.* That persistence, of a signal that no longer exists anywhere at the inputs, is the definition of memory.

**3 — JK toggling.** *Trigger: both JK inputs high at successive active edges → use $Q_{next}=\overline{Q}$ for an edge-triggered device.* $J=K=1$, $Q$ starts at $0$. First clock pulse: $Q=0$ blocks the reset path ($K \cdot Q = 0$) and opens the set path ($J \cdot \overline{Q} = 1$) — $Q$ becomes $1$. Second pulse: now $Q=1$ blocks set and opens reset — $Q$ becomes $0$. Two clock pulses, one full cycle of $Q$: the output runs at **half the clock frequency**, on its way to becoming the least-significant bit of a binary counter.

---

## Exam Notes

### Cambridge 9618 — A Level §15.2

Understand **SR and JK flip-flops**, draw a logic circuit, derive a truth table, and explain their role as data-storage elements. Include the previous state when the result depends on it. For a **NOR SR** latch, S=R=1 forces both outputs low; for its **active-low NAND** counterpart, the forbidden pair is both inputs low. Name the implementation before calling an input combination invalid. The JK hold/set/reset/toggle behaviour needs a properly timed implementation; a level-gated feedback sketch alone does not guarantee one toggle per pulse.

### AQA 7517 — §4.6.4.1

The **edge-triggered D-type flip-flop as a memory unit** is explicitly required. Its internal operation is explicitly excluded. Know what is sampled, when Q updates, and what is held between active edges; do not substitute a detailed SR/JK construction for the required D-type behaviour. [AQA specification](https://www.aqa.org.uk/subjects/computer-science/a-level/computer-science-7517/specification/subject-content/fundamentals-of-computer-systems).

### OCR H446 — §1.4.3(e)

Explicitly includes the logic associated with **D-type flip-flops**, alongside half and full adders. The D-type section above is therefore exam content for OCR, although it extends beyond Cambridge's named SR/JK pair. [OCR specification](https://www.ocr.org.uk/Images/170844-specification-accredited-a-level-gce-computer-science-h446.pdf).

### Where it is not a named requirement

**Cambridge 0478 §10**, **IB Computer Science 2027 A1.2.3–A1.2.5**, and **Pearson Edexcel IAL Computer Science (first teaching 2026) §5.3** cover combinational or Boolean logic without naming flip-flops or their state tables. IB's scope also includes Boolean algebra and simplification; it does not “stop at gates and truth tables”. Memory concepts elsewhere in these courses do not by themselves require constructing an SR, JK or D-type circuit. [Pearson specification](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/computer-science/2026/specification-and-sample-assessments/ial-computer-science-specification.pdf).

**AP CSA** (2025–26 CED) and **AP CSP** (Fall 2023 CED) do not require flip-flop circuit construction or sequential-circuit timing tables. These are hardware enrichment beyond their programming logic.

---

## Connections

- **Parent:** [[Logic Gates]] — the NOR and NAND being cross-coupled, and the warning planted there that gates alone are *stateless*; the flip-flop is the promised circuit that remembers.
- **The other half of §15.2:** [[Half-Adder and Full-Adder]] — adders compute, flip-flops remember; a processor is the two glued together under one clock. [[Boolean Algebra]] and [[Karnaugh Maps]] — a flip-flop's next-state logic is a Boolean function you design and minimise with exactly those tools.
- **The bridge cashed:** [[RAM and the Memory Hierarchy]] — the SRAM cell's cross-coupled inverter loop *is* the bistable core above; no refresh needed, volatile all the same. [[CPU Architecture and the Fetch-Execute Cycle]] — registers are flip-flop rows, and the clock that steps them is the machine's heartbeat.
- **The self-reference thread:** [[Stories/Russell's Paradox in the Post]] — the odd loop ($Q = \overline{Q}$) has no Boolean fixed point; the cross-coupled even loop permits two. The analogy concerns logical consistency, not a prediction of analogue circuit dynamics.
- **Counting:** [[Number Bases]] — a chain of toggling flip-flops counts in binary, each stage carrying one power of 2.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $Q,\ \overline{Q}$ | `Q,\ \overline{Q}` | the stored bit and its complement |
| $Q_{\text{next}}$ | `Q_{\text{next}}` | state after the clock pulse |
| $\overline{R + \overline{Q}}$ | `\overline{R + \overline{Q}}` | NOR of $R$ and $\overline{Q}$ — the SR top gate |
| $J \cdot \overline{Q} \cdot clk$ | `J \cdot \overline{Q} \cdot clk` | JK internal set — $J$ chaperoned by $\overline{Q}$ |
| $K \cdot Q \cdot clk$ | `K \cdot Q \cdot clk` | JK internal reset — $K$ chaperoned by $Q$ |
| $Q := D$ | `Q := D` | D-type capture on the clock edge |
