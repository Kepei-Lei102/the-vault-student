---
chinese: 处理器架构与取指执行周期 (chǔlǐqì jiàgòu yǔ qǔzhǐ zhíxíng zhōuqī)
prerequisites:
  - "[[Logic Gates]]"
  - "[[Number Bases]]"
  - "[[Von Neumann machine]]"
leads_to:
  - "[[Pipelining and Simultaneous Multithreading]]"
  - "[[Assembly Language]]"
  - "[[RAM and the Memory Hierarchy]]"
  - "[[Clock Domains and Metastability]]"
  - "[[Input and Output Devices]]"
  - "[[Embedded Systems]]"
  - "[[Interrupt Handling]]"
  - "[[Operating Systems]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/0478-3-1
  - syllabus/9618-4-1
  - syllabus/IB-CS-A1-1
  - type/deep
  - misconception/pc-holds-the-instruction
  - misconception/cpu-runs-high-level-code
  - misconception/von-neumann-is-a-component
  - misconception/mar-mdr-confusion
---

# CPU Architecture and the Fetch-Execute Cycle 处理器架构与取指执行周期

> *A CPU does exactly one thing, a few billion times a second: it fetches the next instruction from memory, works out what it means, and carries it out. Everything else — every app, every game, every model — is that one loop, repeated. This card opens the box and names the parts: the registers that hold the work in progress, the buses that move it, and the **stored-program** idea that lets a machine be reprogrammed instead of rewired.*

## Definition — the stored-program machine

A **CPU** (central processing unit, 中央处理器) is the component that executes instructions. Almost every computer ever built follows the **von Neumann architecture**: a single main memory holds **both the program and the data**, and the CPU repeatedly **fetches**, **decodes**, and **executes** instructions from it. The CPU has four kinds of part:

- **Control Unit (CU, 控制单元)** — the conductor; it fetches and decodes each instruction and sends the control signals that make everything else happen.
- **Arithmetic Logic Unit (ALU, 算术逻辑单元)** — does the actual arithmetic and logic (built from [[Logic Gates]] — an adder is just gates).
- **Registers (寄存器)** — a handful of tiny, ultra-fast storage cells *inside* the CPU that hold the instruction and data currently being worked on.
- **Buses (总线)** — the wires that carry addresses, data, and control signals between the CPU and memory.

The deep idea — **the program is just data in memory** — is what makes a computer *general-purpose*: to make it do something new you load a different program, you don't rewire it. That is the physical embodiment of Turing's 1936 *universal machine* (→ [[Turing Machine]]), given a buildable architecture by von Neumann in 1945 (→ [[Von Neumann machine]]).

### 中文锚点

**处理器架构（冯·诺依曼架构 von Neumann）**：一块**主存储器同时存放程序和数据**（stored-program，存储程序），CPU 不断地**取指（fetch）→ 译码（decode）→ 执行（execute）**。CPU 四大部分：**控制单元 CU**（指挥）、**算术逻辑单元 ALU**（运算，由 [[Logic Gates|逻辑门]] 搭成）、**寄存器**（CPU 内部极快的小存储）、**总线**（地址/数据/控制）。

**核心思想**：*程序就是存储器里的数据* —— 换程序即可改变功能，无需重新接线。这正是图灵 1936 年"通用机"（[[Turing Machine]]）的物理实现，由冯·诺依曼 1945 年给出可建造的架构（[[Von Neumann machine]]）。

**取指-执行周期**的寄存器层面（见下文）：`PC→MAR`、读内存`→MDR→CIR`、`PC+1`、译码、执行。常见误区：**PC 存的是下一条指令的*地址*，不是指令本身**。

## The von Neumann model — components and buses

![[vonneumann-cpu.svg|720]]

The CPU and main memory (RAM) are separate; they talk over three **buses**:

| Bus | Direction | Carries | Width matters because… |
|-----|-----------|---------|------------------------|
| **Address bus** (地址总线) | one-way (CPU → memory) | the address to read/write | $n$ lines address $2^n$ locations — a 32-bit address bus reaches 4 GB |
| **Data bus** (数据总线) | two-way (bidirectional) | the data or instruction itself | wider bus = more bits moved per transfer (often = the word size) |
| **Control bus** (控制总线) | two-way | control signals (read/write, clock tick, interrupt) | coordinates *when* and *which way* data moves |

The single shared path between CPU and memory is the architecture's one weakness — the **von Neumann bottleneck** (see Beyond Syllabus).

## The registers — where the work in progress lives

Registers are the fastest storage in the machine — faster than cache, far faster than RAM — because they sit *inside* the CPU. The five (plus a status register) you must know:

| Register | Name | Holds |
|----------|------|-------|
| **PC** | Program Counter (程序计数器) | the **address of the *next* instruction** — *not* the instruction |
| **MAR** | Memory Address Register (存储器地址寄存器) | the address currently being read from / written to |
| **MDR** | Memory Data Register (存储器数据寄存器) | the data or instruction just read from (or about to be written to) memory |
| **CIR** | Current Instruction Register (当前指令寄存器) | the instruction currently being decoded and executed |
| **ACC** | Accumulator (累加器) | the working value — the result of the latest ALU operation |
| **Status register** | flags (状态寄存器) | condition flags — carry, zero, negative, **overflow** (→ [[Overflow and Underflow]]) |

> **The single most common mistake:** the **PC holds an *address*, the CIR holds the *instruction*.** The PC is a bookmark ("read next from here"); the CIR is the page you're currently reading. And **MAR vs MDR**: the MAR is the *address* (which mailbox), the MDR is the *contents* (what's in it).

## The fetch–decode–execute cycle, register by register

This is the loop. Follow the data moving between registers — that register-transfer view is exactly what the exam wants.

**Fetch** — *get the next instruction:*
1. `PC → MAR` — copy the next-instruction address from the PC into the MAR.
2. The CU asserts **read** on the control bus; memory puts the contents of `memory[MAR]` on the data bus → `→ MDR`.
3. `MDR → CIR` — move the fetched instruction into the Current Instruction Register.
4. `PC → PC + 1` — increment the PC so it points at the instruction *after* this one.

**Decode** — *work out what it means:*
5. The CU splits the instruction in the CIR into an **opcode** (what operation) and an **operand** (what to operate on — usually a memory address or a value).

**Execute** — *do it.* The exact steps depend on the opcode. Three canonical cases:
- **`LOAD x`** — operand `x → MAR`; read; `memory[x] → MDR → ACC`.
- **`ADD x`** — operand `x → MAR`; read; `memory[x] → MDR`; the **ALU** adds MDR to ACC; result `→ ACC` (status flags updated).
- **`STORE x`** — `ACC → MDR`; operand `x → MAR`; the CU asserts **write**; `MDR → memory[x]`.

Then the cycle repeats from the (now incremented) PC — billions of times a second.

> **Jumps are where the PC earns its name.** A branch instruction like `JMP x` simply does `operand x → PC`: the next fetch reads from `x` instead of the next-in-line address. That one move is the entire basis of loops, `if`, and function calls — and it is exactly the *control hazard* the [[Pipelining and Simultaneous Multithreading|pipeline]] has to predict, because the CPU wants to fetch the next instruction *before* it knows where the jump leads.

## Clock speed, cores, and cache (briefly)

Three numbers on every spec sheet, all about how fast and how parallel this cycle runs:

- **Clock speed** (时钟频率) — how many cycles per second. 3 GHz ≈ three billion ticks per second; each fetch/decode/execute step is paced by the clock.
- **Cores** (核心) — a core is *one* complete fetch-execute engine. A quad-core CPU has four, running four instruction streams at once.
- **Cache** (高速缓存) — small, fast memory between the CPU and RAM that keeps recently-used instructions/data close, so the CPU waits on the slow main memory less often.

*Raising the clock, adding cores, and the deep tricks that keep one core busy (pipelining, out-of-order, SMT) are the whole story of [[Pipelining and Simultaneous Multithreading]] — this card is the model those tricks accelerate.*

## Instruction sets and machine code

The CU can only decode instructions from a fixed repertoire — the CPU's **instruction set**. Each **machine-code** instruction is just **binary** (→ [[Number Bases]]): a few bits of **opcode** followed by an **operand**.

```
  opcode    operand
 ┌──────┬──────────────┐
 │ 0010 │ 0000 1101 01 │   e.g. "LOAD the value at address 53"
 └──────┴──────────────┘
```

Humans write **assembly** (`LOAD 53`) — a one-to-one readable form of machine code — and an *assembler* turns it into the binary the CU executes. High-level languages (Python, Java) are translated, in many steps, down to this same machine code: **the CPU never runs your source code; it only ever runs machine code** (the full assembly treatment is reserved for [[Assembly Language]]).

## Worked Example — trace a 3-instruction program

A program in memory computes `C = A + B`. Addresses 0–2 hold the instructions; A=`5` at address 50, B=`3` at 51, C at 52.

| Addr | Instruction |
|------|-------------|
| 0 | `LOAD 50` |
| 1 | `ADD 51` |
| 2 | `STORE 52` |

Tracing the registers (PC starts at 0):

| Step | Action | PC | MAR | MDR | CIR | ACC |
|------|--------|----|----|----|----|----|
| Fetch | `PC→MAR`, read, `→MDR→CIR`, `PC+1` | 1 | 0 | `LOAD 50` | `LOAD 50` | — |
| Exec | `50→MAR`, read `memory[50]→MDR→ACC` | 1 | 50 | 5 | `LOAD 50` | **5** |
| Fetch | next instruction | 2 | 1 | `ADD 51` | `ADD 51` | 5 |
| Exec | `51→MAR`, read `3→MDR`, ALU `5+3` | 2 | 51 | 3 | `ADD 51` | **8** |
| Fetch | next instruction | 3 | 2 | `STORE 52` | `STORE 52` | 8 |
| Exec | `ACC→MDR`, `52→MAR`, write | 3 | 52 | 8 | `STORE 52` | 8 |

After three cycles, `memory[52] = 8`. That is a CPU computing `5 + 3` — and *every* program is this, scaled up.

### The same trace, animated

Watch the registers fill and the values ride the buses through all three instructions, with the phase (FETCH / DECODE / EXECUTE) called out at each step. Pause on any micro-step:

![[fde-cycle.mp4]]

## Common Misconceptions

- **"The PC holds the next instruction."** No — it holds its **address**. The instruction itself lands in the **CIR**. (PC = bookmark; CIR = the page.)
- **"MAR and MDR are interchangeable."** No — **MAR = address** (which location), **MDR = data** (its contents). Read/write always loads the MAR first.
- **"The CPU runs my Python / Java directly."** No — it executes only **machine code**; translators (compilers/interpreters/assemblers) convert high-level code down to it.
- **"Von Neumann is a part of the CPU."** No — it's the **architecture** (stored-program; one memory for code + data), not a component. Its rival is the **Harvard** architecture (separate code/data memories).
- **"A higher clock speed always means a faster computer."** Not necessarily — performance is clock × **IPC** × cores, and IPC depends on all the tricks in [[Pipelining and Simultaneous Multithreading]].

## Exam Notes

### Cambridge 0478 (IGCSE) — §3.1
The core IGCSE hardware topic. You should be able to:
- State that the CPU follows the **von Neumann architecture** and name its parts (**CU, ALU, registers, buses**).
- Name and give the purpose of each register — **PC, MAR, MDR, CIR, ACC** — and the three **buses** (address / data / control), including that address-bus width sets how much memory can be addressed.
- **Describe the fetch–decode–execute cycle** in register-transfer terms (the `PC→MAR→…` steps above) — a very common extended-answer question.
- Explain how **cores, cache, and clock speed** affect performance (§3.1.3), and what **instruction sets / machine code** are (§3.1.4). *(Embedded systems, §3.1.5, is a separate topic.)*

### Cambridge 9618 (A Level) — §4.1
Everything above at more depth, plus: the **status register** and its flags, the role of each register *within* the cycle, and how the buses coordinate a transfer. (Assembly language and addressing modes are **§4.2** → [[Assembly Language]].) The performance half (pipelining, parallel processing) is **§15.1** → [[Pipelining and Simultaneous Multithreading]].

### IB Computer Science — A1.1 Computer hardware and operation
The CPU, its components, and the **fetch–decode–execute cycle** sit at the centre of A1.1. The register-transfer trace and the von Neumann model are the working vocabulary for A1.1 questions on how a processor executes instructions; cores/cache/clock speed answer the "factors affecting performance" strand. IB does not require the Cambridge register mnemonics (PC/MAR/MDR/CIR/ACC) by name, but naming them and tracing a transfer is exactly the justified detail its extended responses reward.

### AP
**AP CS Principles** treats the CPU at a high level (the fetch-execute idea, not register names). **AP CSA** does not cover hardware architecture. *(No formula-sheet relevance — this is a model, not a formula card.)*

## Connections

- **Prerequisite:** [[Logic Gates]] — the ALU and the registers are built from gates; an adder *is* gates. [[Number Bases]] — machine-code instructions and addresses are binary.
- **The modern realisation:** [[Pipelining and Simultaneous Multithreading]] — the same fetch-execute cycle, accelerated (overlapped, reordered, run on many units and cores). This card is the model; that card is the speed.
- **The ancestors (reserved):** [[Turing Machine]] — the 1936 *theoretical* universal machine (what is computable); [[Von Neumann machine]] — the 1945 *architectural* ancestor (the stored-program idea this card runs on). The lineage Turing → von Neumann → the FDE CPU.
- **Extends to (reserved):** [[Assembly Language]] — the human-readable form of the machine code the CU decodes (9618 §4.2). [[The Modern CPU vs the Textbook Model]] — how far a real core has grown past this 5-register picture.
- **Uses:** [[Overflow and Underflow]] — the status-register carry/overflow flags are set by the ALU here.
- **History:** [[Stories/The Boolean-to-Silicon Bridge]] — Turing's universal machine, von Neumann's 1945 EDVAC report, and the road to silicon.

## Beyond Syllabus

### The von Neumann bottleneck
Because instructions *and* data share one memory and (classically) one bus, the CPU often sits idle waiting for memory — the **von Neumann bottleneck**. As CPUs outran memory speed, this became the dominant performance problem (the *memory wall* in [[Pipelining and Simultaneous Multithreading]]). The whole cache hierarchy exists to soften it.

### Harvard architecture — the rival
A **Harvard architecture** keeps instructions and data in *separate* memories with *separate* buses, so the CPU can fetch an instruction and a data word at the same time. Pure Harvard is rare for general computers, but a **modified Harvard** lives inside almost every modern chip: the **L1 cache is split** into separate instruction and data caches (recall the `L1-I` in the [[Pipelining and Simultaneous Multithreading|pipeline diagrams]]) sitting on top of one unified main memory. Microcontrollers and DSPs often go full Harvard.

### Microcode — a CPU inside the CPU
On complex (CISC) chips, one machine instruction may itself be carried out by a tiny built-in program of **microcode** — the control unit running its own even-lower-level steps. It is the seam where [[Pipelining and Simultaneous Multithreading|x86's complex instructions get cracked into RISC-like micro-ops]], and a preview of the [[CISC vs RISC]] story.

### The lineage, in one line
**Turing (1936)** proved one *universal* machine could compute anything computable, given the right description on its tape. **von Neumann (1945)** made that description *live in the same memory as the data* — the stored-program computer. Every fetch-execute cycle you traced above is that 80-year-old idea, ticking. (→ [[Turing Machine]], [[Von Neumann machine]].)

## LaTeX / Notation Reference

| Symbol | Meaning |
|--------|---------|
| PC | Program Counter — address of the next instruction |
| MAR | Memory Address Register — address being accessed |
| MDR | Memory Data Register — data/instruction in transit (also MBR) |
| CIR | Current Instruction Register — instruction being executed |
| ACC | Accumulator — working value / ALU result |
| CU / ALU | Control Unit / Arithmetic Logic Unit |
| $2^n$ | locations addressable by an $n$-line address bus |
