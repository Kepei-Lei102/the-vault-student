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

> **Every circuit so far forgets.** Hand an adder new inputs and it computes the new answer with no memory of the old one — a gate is a function of the *present*. To store a bit, a circuit's output must depend on its *past*, and the trick that buys a past is shameless: **feed the output back into the input.** The circuit that results — the flip-flop — is the atom of computer memory. Every register, every counter, every byte of cache is rows and rows of it.

## Definition

Everything built from [[Logic Gates]] so far — De Morgan rewrites, Karnaugh-minimised alarms, the [[Half-Adder and Full-Adder|full adder]] — is **combinational logic** (组合逻辑): the outputs are a pure Boolean function of the current inputs. Same inputs, same outputs, always; the truth table is the entire story, and the circuit has no memory of anything.

A **flip-flop** is the simplest circuit that breaks this rule. It has **two stable states**, it stays in whichever state it was last put, and its inputs are used not to *compute* the output but to *change the state*. It is **sequential logic** (时序逻辑): the output depends on the history of the inputs, not just their present values. One flip-flop stores exactly **one bit**.

The structural difference is visible at a glance: in a combinational circuit, signals flow one way, inputs to outputs. In a flip-flop, there is a **feedback loop** — an output wired back to an input. The loop is not a bug. The loop *is* the memory.

### 中文锚点

| English | 中文 | 一句话 |
|---|---|---|
| flip-flop | 触发器 (chùfāqì) | "触"一下就"发"生翻转 — 受触发而改变状态的电路 |
| latch | 锁存器 (suǒcúnqì) | 锁 + 存 — 把一位**锁**住并**存**着（中文比英文更直白） |
| combinational logic | 组合逻辑 | 输出只由当前输入**组合**而成，无记忆 |
| sequential logic | 时序逻辑 | 有"时"有"序" — 输出依赖输入的历史 |
| set / reset | 置位 / 复位 | S 把 Q 置成 1；R 把 Q 复成 0 |
| toggle | 翻转 | JK 独有：$J=K=1$ 时 Q 取反 |
| clock | 时钟 (shízhōng) | 全机共享的节拍，所有触发器踩着它同步更新 |

核心一句话：**组合电路计算，时序电路记忆**；记忆的本质是一个"输出咬住自己输入"的反馈环。

---

## The loop that remembers

Start with the smallest possible self-reference: wire a NOT gate's output straight back to its own input.

![[feedback-loop-paradox-memory.svg|660]]

The wire demands $Q = \overline{Q}$ — a bit equal to its own opposite. **No stable state satisfies this.** It is the liar's sentence soldered into silicon, the same odd loop that shattered set theory in [[Stories/Russell's Paradox in the Post]] — and the physical circuit does exactly what the logic predicts: it can't settle, so it **oscillates**, flipping as fast as the gate can propagate. (Engineers, ever practical, gave the paradox a job: a loop of an *odd* number of inverters is a **ring oscillator**, used on real chips as a clock source and a speed gauge.)

Now add a second NOT gate to the loop. The demand becomes $Q = \overline{\overline{Q}} = Q$ — satisfied by **both** $Q=0$ and $Q=1$. Two inverters in a loop have **two stable states**, each holding the other up: the left gate drives the right, the right drives the left right back, forever, for as long as the power is on. This is **bistability**, and it is precisely the cross-coupled inverter pair at the heart of the SRAM cell in [[RAM and the Memory Hierarchy]].

> **Odd loops are paradoxes; even loops are memories.** An odd number of inversions has no consistent state (it oscillates); an even number has two (it remembers). Self-reference isn't the villain of the Russell story after all — it just needed an even number of negations.

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

This beat is what the "GHz" on a CPU's spec sheet counts, and it is what makes "the state of the machine after step $n$" a meaningful phrase: on each tick, every register in the computer — program counter, accumulator, all of them — steps forward *together* through the fetch–execute cycle.

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
> If the JK merely listens "while the clock is high," then with $J=K=1$ it toggles over and over for the whole half-cycle — the **race-around condition** — and the final value is anyone's guess. Real designs act only at the clock's rising (or falling) **edge**, an instant with no width, so exactly one toggle happens per beat (historically via a **master–slave** pair: one latch reads while the other publishes). The strict jargon: a *latch* is level-sensitive, a *flip-flop* is edge-triggered — though Cambridge papers say "flip-flop" for both, and so should your exam answers.

**A note on the name.** J and K stand for nothing. An engineer at Hughes Aircraft in the 1950s, Eldred Nelson, labelled the input pairs of the flip-flops in a patent alphabetically — one pair happened to land on J and K, and the name stuck. The oft-repeated story that they honour Jack Kilby is folklore: Kilby's integrated circuit came years later.

---

## The role of flip-flops as data storage

One flip-flop stores one bit, holding it as long as the power is on and rewriting it on demand. This is the LO in one sentence — and here is where those bits actually live:

- **Registers.** A CPU register is a row of flip-flops sharing one clock — a 32-bit register is 32 of them side by side. The program counter, the accumulator, the instruction register of [[CPU Architecture and the Fetch-Execute Cycle]] are all just flip-flop rows.
- **Static RAM.** The SRAM cell of [[RAM and the Memory Hierarchy]] *is* the two-inverter bistable loop with access transistors as its handles — which is why SRAM needs no refresh (the loop holds itself) yet still forgets at power-off (the loop needs power to keep reinforcing). Your CPU's cache is megabytes of flip-flops.
- **Counters and timers.** Toggling chains count clock pulses — program counters stepping, timers timing, the machinery of *when*.
- **Status flags.** The carry, zero, and overflow flags the ALU raises are single flip-flops each, remembering one fact about the last calculation.

The two halves of 9618 §15.2 are literally the two ingredients of a processor: **combinational circuits compute** (the adder — the ALU's heart), **sequential circuits remember** (the flip-flop — the registers and cache). Glue them together under one clock, and the datapath computes on the beat while the flip-flops carry the results forward to the next beat. That loop — compute, store, repeat — *is* a computer running.

---

## Beyond the syllabus — the D-type, the bit that registers actually keep

Recall that the SR flip-flop's forbidden state needed a rule ("never raise both") and the JK needed a chaperone. The **D-type flip-flop** deletes the problem by construction: it has a single data input **D**, wired so that $S = D$ and $R = \overline{D}$ through one inverter. $S$ and $R$ now *cannot* agree — the forbidden state is unreachable by design.

Its behaviour is one line: **on each clock edge, $Q := D$.** Whatever bit is on the wire when the beat lands is captured and held until the next beat — a camera shutter for one bit. No modes, no forbidden rows, nothing to memorise. That simple-mindedness is exactly why the D-type, not SR or JK, is the flip-flop that real hardware is made of: register files, pipeline stages, and shift registers (a row of D-types passing a bit down the line each beat, one gear of serial-to-parallel conversion) are all D-types by the million. SR is the concept, JK is the exam classic, D is the industry.

---

## Worked examples

**1 — Derive the SR truth table from the circuit** (the exam task). The gates give $Q = \overline{R + \overline{Q}}$ and $\overline{Q} = \overline{S + Q}$.
- $S=1, R=0$: bottom gate sees a $1$, so $\overline{Q} = \overline{1 + Q} = 0$; the top gate then sees $R=0, \overline{Q}=0$, so $Q = \overline{0+0} = 1$. **Set.** ✓
- $S=0, R=1$: symmetric — $Q = 0$, $\overline{Q} = 1$. **Reset.** ✓
- $S=0, R=0$: each NOR has one input at $0$, so each acts as a NOT of the fed-back signal: $Q = \overline{\overline{Q}}$, $\overline{Q} = \overline{Q}$ — the two-inverter loop, consistent with **both** states. Whichever state it was in, it keeps. **Hold.** ✓
- $S=1, R=1$: both gates see a $1$, both outputs forced to $0$ — $Q = \overline{Q} = 0$. **Invalid.**

**2 — Show that it remembers.** Start with $Q=0$. Pulse $S$: $S=1$ briefly, then back to $0$. During the pulse, $Q$ is driven to $1$ (case one above). After the pulse, inputs are $S=R=0$ — hold — and the loop sustains $Q=1$ on its own. *The pulse is gone; the bit remains.* That persistence, of a signal that no longer exists anywhere at the inputs, is the definition of memory.

**3 — JK toggling.** $J=K=1$, $Q$ starts at $0$. First clock pulse: $Q=0$ blocks the reset path ($K \cdot Q = 0$) and opens the set path ($J \cdot \overline{Q} = 1$) — $Q$ becomes $1$. Second pulse: now $Q=1$ blocks set and opens reset — $Q$ becomes $0$. Two clock pulses, one full cycle of $Q$: the output runs at **half the clock frequency**, on its way to becoming bit 1 of a binary counter.

---

## Exam Notes

### Cambridge 9618 (A Level, §15.2)
Directly examined, as the sequential half of the section. You must be able to: (1) **draw the logic circuit** of an SR flip-flop (cross-coupled NOR or NAND) and of a JK flip-flop; (2) **derive its truth table** — for SR: hold / set / reset / invalid, and for JK: hold / set / reset / toggle, with the output column written in terms of the current $Q$; (3) **explain why $S=R=1$ is not allowed** (outputs no longer complementary; unpredictable final state) and how the JK's feedback removes it; (4) **describe the role of flip-flops as data storage elements** — one flip-flop stores one bit; registers and SRAM are built from them. Watch the NAND-built variant: its inputs are active-low, so the hold and forbidden rows swap.

### Cambridge 0478 (IGCSE)
Not examined — IGCSE logic stops at gates and truth tables ([[Logic Gates]]). Flip-flops are the A-Level step up.

### Other A-Level boards (AQA / OCR)
OCR examines the **D-type** flip-flop by name (the beyond-syllabus section here is exam-front there); AQA A-Level treats sequential circuits similarly at the edge of its spec. The SR-then-JK route is distinctly Cambridge.

### AP
Not covered — neither AP CSA nor AP CSP builds circuits. Flip-flops reappear in first-year university digital-logic and computer-organisation courses, exactly in the form above.

### IB Computer Science
Not a named statement — A1.2's logic content stops at gates and truth tables, and sequential (stateful) circuits are beyond every IB statement. For an IB student this card is enrichment: the answer to "so how do gates *remember*?" that A1.1's RAM quietly assumes.

---

## Connections

- **Parent:** [[Logic Gates]] — the NOR and NAND being cross-coupled, and the warning planted there that gates alone are *stateless*; the flip-flop is the promised circuit that remembers.
- **The other half of §15.2:** [[Half-Adder and Full-Adder]] — adders compute, flip-flops remember; a processor is the two glued together under one clock. [[Boolean Algebra]] and [[Karnaugh Maps]] — a flip-flop's next-state logic is a Boolean function you design and minimise with exactly those tools.
- **The bridge cashed:** [[RAM and the Memory Hierarchy]] — the SRAM cell's cross-coupled inverter loop *is* the bistable core above; no refresh needed, volatile all the same. [[CPU Architecture and the Fetch-Execute Cycle]] — registers are flip-flop rows, and the clock that steps them is the machine's heartbeat.
- **The self-reference thread:** [[Stories/Russell's Paradox in the Post]] — the odd loop ($Q = \overline{Q}$) is Russell's paradox in silicon and cannot settle; the even loop is a memory. The ouroboros destroys set theory or stores a bit, depending on how many times the tail is negated.
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
