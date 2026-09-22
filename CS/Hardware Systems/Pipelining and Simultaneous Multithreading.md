---
chinese: 流水线与同时多线程 (liúshuǐxiàn yǔ tóngshí duō xiànchéng)
prerequisites:
  - "[[Logic Gates]]"
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Dual-Core Craft]]"
leads_to:
  - "[[The Modern CPU vs the Textbook Model]]"
  - "[[The GPU — From Triangles to Tensors]]"
  - "[[Concurrency]]"
  - "[[Floating-Point Representation]]"
  - "[[CISC vs RISC]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - domain/parallel-computing
  - level/A-Level
  - curriculum/Cambridge-9618
  - curriculum/Cambridge-0478
  - curriculum/IB-CS
  - syllabus/9618-15-1
  - syllabus/9618-4-1
  - syllabus/0478-3
  - syllabus/IB-CS-A1-1
  - type/deep
  - misconception/clock-speed-is-everything
  - misconception/pipelining-speeds-one-instruction
  - misconception/hyperthreading-doubles-performance
  - misconception/gpu-is-a-faster-cpu
---

# Pipelining and Simultaneous Multithreading 流水线与同时多线程

> *A modern CPU core is a factory floor, not a single craftsman. Its whole genius is to never let a workstation sit idle — and when one thread can't keep the floor busy, it quietly invites a second one in. A GPU groups many arithmetic lanes to work on similar calculations. Both designs seek useful work per tick; power limits made this especially important as easy clock-speed scaling slowed around 2005.*

## Definition — three ideas, one goal (keep the silicon busy)

A processor's work is the **fetch–execute cycle**: fetch an instruction, decode it, execute it, repeat, billions of times a second. Every trick in this card attacks the same waste — **execution units standing idle** — from a different angle:

- **Pipelining** (流水线) — overlap the *stages* of consecutive instructions, like a laundromat running wash, dry, and fold loads at once. It raises **throughput** (instructions finished per second), not **latency** (time for any one instruction). This is the heart of §15.1.
- **Simultaneous Multithreading / SMT** (同时多线程; Intel brands it *Hyper-Threading*) — keep two instruction streams alive on one core, so when thread A stalls, thread B's instructions fill the idle units. One physical core pretends to be two logical ones.
- **The GPU** — emphasise throughput using many arithmetic lanes. Within an execution group, an instruction can act on many data items; different groups can progress independently. The SIMT model is developed in [[The GPU — From Triangles to Tensors]].

The unifying question across all three: *when clock speed alone is not enough, how do we get more useful work done per tick?*

### 中文锚点

你有四筐衣服要洗，每一筐都要洗半小时、烘半小时、叠半小时。没有人会等第一筐叠完了才开始洗第二筐。洗衣机一空出来，第二筐就放进去，过一会儿就有三筐衣服同时转起来，洗、烘、叠各占一筐。仔细看看到底赚到了什么。任何一筐衣服从头到尾还是要一个半小时，哪一步都没有变快。可是现在每隔半小时就有一筐做完，而不是每隔一个半小时。处理器处理指令也是这个办法：取这条指令的同时，在译码前一条，在执行再往前一条。麻烦出在下一筐要看这一筐的结果的时候：如果非得等这筐烘干了才知道接下来该洗哪一筐，洗衣机就只能空着，除非你先猜一筐放进去，而猜错了就得把它拿出来重来。

#### 术语对照 (Terms)

| English | 中文 | one-line meaning |
|---|---|---|
| pipelining | 流水线 | overlapping the stages (fetch 取指, decode 译码, execute 执行) of successive instructions |
| throughput / latency | 吞吐量 / 延迟 | instructions finished per second / time for one instruction; pipelining raises the first only |
| hazard / stall | 冒险 / 停顿 | the next instruction is not yet known or not yet ready |
| branch prediction / flush | 分支预测 / 清空 | guess the branch and keep the pipeline full; empty it when the guess is wrong |
| out-of-order / speculative execution | 乱序执行 / 投机（推测）执行 | run what is ready first; run ahead of a decision |
| simultaneous multithreading (SMT), Hyper-Threading | 同时多线程 / 超线程 | one core holds two threads' state and fills one's stalls with the other's work; workload-dependent gain, not double |
| SIMD, GPU | 单指令多数据 / 图形处理器 | one instruction applied to many data at once; transistors spent on throughput, not on one fast thread |
| Flynn's taxonomy | Flynn 分类 | SISD, SIMD, MISD, MIMD |

## The fetch–execute cycle — the loop being sped up

Everything a CPU does is the repetition of one loop. The textbook three beats are **fetch** (read the next instruction from memory), **decode** (work out what it asks for), **execute** (do it — an add, a compare, a memory access). Hardware designers split this finer; the classic teaching model is a **five-stage** pipeline:

| Stage | Name | What happens |
|-------|------|--------------|
| IF | Instruction Fetch | read the instruction at the program counter |
| ID | Instruction Decode | decode it; read the registers it needs |
| EX | Execute | the ALU does the arithmetic/logic (built from [[Logic Gates]]) |
| MEM | Memory access | read or write data memory, if needed |
| WB | Write Back | write the result into a register |

The **clock speed** is simply how fast this loop ticks: 3 GHz means three billion stage-ticks per second. One instruction passing through all five stages takes five ticks — that is its **latency**, and pipelining does *not* shorten it.

> [!info] Scope — where the register detail lives
> For the **PC, MAR, MDR, CIR, ACC** registers, the address/data/control buses, and instruction sets, see [[CPU Architecture and the Fetch-Execute Cycle]]. Pipelining overlaps the *stages* of that cycle.

## Pipelining — the laundromat that runs the world

Here is the waste. If you run instructions one at a time, while the EX unit is working, the IF unit, the decoder, and the memory unit all sit idle. Four-fifths of your expensive silicon is doing nothing on every tick.

The fix is the **laundromat insight**. You have a washer, a dryer, and a folding table. The naïve way: wash load 1, dry load 1, fold load 1, *then* start load 2 — three machines, only one ever running. The smart way: the moment load 1 leaves the washer for the dryer, load 2 goes *into* the washer. Now wash, dry, and fold all run at once, on three different loads. You didn't make any single load finish faster; you made a *finished load come out every dry-cycle* instead of every three.

In an ideal single-issue pipeline with equal one-tick stages and no stalls: as instruction 1 moves IF → ID, instruction 2 enters IF behind it; a tick later instruction 3 enters, and so on. After the pipeline **fills**, one instruction **completes every single tick**.

![[pipeline-staircase.svg|720]]

The diagram is the whole idea. Sequentially (top), 3 instructions over a 5-stage cycle take $3 \times 5 = 15$ ticks. Pipelined (bottom), they take $5 + (3-1) = 7$ ticks — and the gap only widens as instructions pile up.

**The throughput law (same ideal model).** Push $N$ instructions through a $k$-stage pipeline:

$$\text{ticks} = \underbrace{k}_{\text{fill the pipe}} + \underbrace{(N-1)}_{\text{one done per tick after that}}, \qquad \text{speed-up} = \frac{Nk}{k + (N-1)} \xrightarrow{\;N \to \infty\;} k.$$

So a 5-stage pipeline approaches a **5× speed-up** in that ideal model — not by working faster, but by never letting a stage idle. This is also *why* clock speeds could climb for decades: splitting the work into more, smaller stages means each stage does less, so the clock can tick faster. (It is not free forever — deeper pipelines pay more on every stall, below.)

> **Throughput vs latency — the one thing students miss.** Pipelining makes *no single instruction faster*. Instruction 1 still takes its 5 ticks end-to-end (often a hair *more*, from the latches between stages). What changes is that instructions now *finish* one-per-tick instead of one-per-five. It is a throughput win, paid for in a small latency cost — the exact trade a busy kitchen makes when it plates many orders by overlapping prep, not by cooking any one dish faster.

## When the pipeline chokes — hazards and bubbles

The laundromat works because the loads are independent. Instructions are not always so polite, and when they depend on each other the pipeline must **stall** — insert a **bubble** (a wasted tick). Three kinds of trouble:

- **Data hazard** — instruction 2 needs the result instruction 1 hasn't written back yet (`x = a + b;  y = x + c;`). The hardware fix is **forwarding** (bypass the result straight from the EX output to the next EX input instead of waiting for WB); when even that isn't enough, it stalls.
- **Control hazard** — a **branch** (`if`, loop, function call). Until the branch *executes*, the CPU doesn't know which instruction comes next — but the pipeline wants to fetch the next instruction *now*. This is the expensive one.
- **Structural hazard** — two instructions want the same unit (e.g. one memory port) on the same tick.

The control hazard is so costly that CPUs **guess**. A **branch predictor** bets on which way the branch will go and keeps fetching down the predicted path, so the pipeline stays full. A correct prediction can keep useful work flowing. A wrong prediction requires the wrong-path work to be discarded and fetching to restart. The penalty depends on where the branch resolves and on the implementation; it is not automatically equal to the total pipeline depth. Deeper pipelines buy a higher clock but a steeper misprediction penalty; chip designers spend enormous effort balancing the two.

## Going wider and out of order — the modern fast core

Once a pipeline reliably finishes one instruction per tick, the next question is greedy: *can we finish more than one?* Three escalating tricks turn a simple pipeline into a modern high-performance core, and all three are the same idea — **find independent work to keep more units busy**:

1. **Superscalar** — build *several* pipelines side by side, so multiple instructions enter each stage per tick. Now the core can retire 2, 4, or more instructions per cycle: its **IPC** (instructions per cycle) rises above 1.
2. **Out-of-order execution (OOO)** — if instruction 3 is stuck waiting on a slow memory load, but instructions 4 and 5 are independent and ready, *run them now* and slot the results back into program order later. The core reorders work behind the scenes to dodge stalls.
3. **Speculative execution** — don't just *predict* a branch and keep fetching; actually *execute* past it on the guess, holding the results provisionally. If the guess was right, commit them; if wrong, discard them as if they never happened.

The three tricks, side by side — all chasing the same prize, *find independent work to keep every unit busy*:

![[superscalar-ooo-speculative.svg|760]]

> [!info] Beyond the textbook CPU model
> Cambridge's CPU is deliberately spare — one **CU**, one **ALU**, a handful of named registers, three buses. A real modern core has *several* fetch and decode units, **many** parallel execution units (multiple ALUs plus separate floating-point, load, store, and branch units — the row in the diagram above), a reorder buffer to track the out-of-order work, and a branch predictor that is itself a small learning machine. Compare [[The Modern CPU vs the Textbook Model]] for the gap between that simple model and the silicon in your phone.

This is what a "fast core" really is: a deep, **superscalar**, **out-of-order**, **speculative** engine whose entire purpose is to scavenge enough independent instructions to keep its execution units fed. It is also why **clock speed alone is a terrible measure** of a CPU — a 3 GHz core today does several times the work per tick of a 3 GHz core from 2005, because its IPC is far higher.

### Watch the engine fill itself

The panels above are one cycle each; the real magic is *cycle after cycle*. The animation below traces a RISC core doing exactly that: the front-end streams ops into the **op queue**, the **out-of-order scheduler** fires every *ready* op into every free unit, a **not-yet-ready op waits while younger ops pass it** (out-of-order), a **cache-missed load** ties up Load/Store while the ALUs keep cycling, and the **branch predictor** keeps the front-end fed. Watch the *"units busy this cycle"* gauge climb.

A clean teaching core first — 4-wide fetch, 6 execution units:

![[core-pipeline-fill-simplified.mp4]]

…then the *same engine* scaled to an **Apple-Firestorm-style** core — 8-wide decode, a 630-entry reorder buffer, and 12 execution units (6 ALU + 4 SIMD + 2 load/store). The shape is identical; only the *width* changed — which is exactly the lesson of the cross-CPU comparisons in hardware deep-dives: every modern core, ARM or x86, has converged on the same out-of-order engine:

![[core-pipeline-fill-firestorm.mp4]]

> [!info] What this foreshadows — [[CISC vs RISC]]
> Line three of those cross-CPU diagrams is the punchline: Apple (ARM), AMD (x86), and Intel (x86) draw *almost the same picture*. Decode width differs across particular designs (AArch64 uses fixed-length encodings; x86 uses variable-length encodings and commonly decodes into internal micro-operations), but underneath, all three run the same wide out-of-order engine you just watched. **The hardware has converged; the ecosystem hasn't** — that's the [[CISC vs RISC]] card.

## Simultaneous Multithreading — two streams, one core

Even a brilliant out-of-order core hits a wall: sometimes a *single* thread simply has no independent work left to run. A **cache miss** to main memory takes ~200 ticks; if every instruction in the queue depends on that load, the whole expensive core sits idle, twiddling its thumbs for 200 ticks.

**SMT** is the elegant fix. Keep the architectural state — the registers, the program counter — of **two threads** on the same core, and let the scheduler pull instructions from *either* stream into the shared execution units. The key insight: **a second thread may have ready work when the first does not**. Threads can still contend for shared resources, and communicating threads may have dependencies. When thread A blocks on its cache miss, thread B's instructions pour into the idle units and get real work done in the shadow of the stall.

To the operating system, one SMT core looks like **two logical processors** ("8 cores, 16 threads" on a spec sheet means 8 physical cores with SMT). But be honest about the payoff:

> [!warning] SMT is not a second core
> The two logical threads **share one core's execution units, caches, and ports** — they are not two independent cores. The gain depends on the workload and processor; on workloads that already saturate the units (or thrash the shared cache) it can be **zero or even negative**. "Hyper-Threading doubles your performance" is the single most common myth here. It fills *bubbles*; it does not duplicate hardware.

This is the hardware answer to [[Stories/Dual-Core Craft]]: a single physical core, made to look like two and kept relentlessly busy, is why one good core can carry so much — and why a famously single-threaded game leans on one or two fast SMT cores rather than on core *count*.

## The GPU — throughput across groups

A CPU often devotes substantial machinery to low-latency progress through complicated instruction streams. A GPU emphasises throughput across many arithmetic lanes. Both use caches and parallel execution; neither is literally one worker versus a crowd.

**Flynn's taxonomy** counts instruction and data streams at a chosen level:

| | Single data | Multiple data |
|---|---|---|
| Single instruction | **SISD** — a simple sequential processor model | **SIMD** — a vector instruction acts on multiple elements |
| Multiple instructions | **MISD** — uncommon; different operations on one data stream | **MIMD** — independently executing CPU cores or cluster nodes |

![[cpu-vs-gpu-latency-throughput.svg|697]]

*The diagram contrasts design priorities. A whole GPU contains many independently scheduled groups; it is not one instruction stream driving every lane on the chip.*

NVIDIA's **SIMT** model exposes threads, grouped into **32-thread warps**. A warp instruction acts on active threads, while other warps may execute different instructions. AMD's wavefront widths depend on architecture and mode. Modern independent thread scheduling also means that a programmer must use the required synchronisation rather than assume implicit lockstep. [NVIDIA execution model](https://docs.nvidia.com/cuda/cuda-programming-guide/03-advanced/advanced-kernel-programming.html).

**Branch divergence** occurs when threads in a group take different paths. Masked execution can leave lanes inactive while another path runs; the cost depends on path lengths, predication and available work. Scheduling another ready warp can hide a memory wait, but cannot shorten the memory access itself.

Sorting networks have a regular communication and comparison pattern that can suit GPU work, but GPUs also run merge sorts and radix sorts. There is no universal “GPU sorting algorithm.” Follow [[The GPU — From Triangles to Tensors]] for the graphics pipeline, memory reuse, matrix units and CPU–GPU cooperation; [[Parallel and External Sorting]] explains the algorithmic choices.

## Massively parallel processing — divide the world into pieces

A **massively parallel system** uses a very large number of processors to work on parts of a problem concurrently. A common design is a cluster of nodes, each with processors and local memory, joined by a fast interconnect. Nodes exchange messages and synchronise when one stage needs another's results. “Massively parallel” describes scale; Flynn's categories describe instruction and data streams. A distributed simulation commonly uses MIMD, while its individual nodes may also use SIMD accelerators.

**Weather forecasting makes the machinery concrete.** Divide the atmosphere into a grid and give each node a region. Nodes update their regions together, then exchange boundary conditions with neighbouring regions because air crosses the boundaries. More processors can reduce computation time, but communication, synchronisation and the remaining serial work limit the speed-up. A task whose next step depends on the previous result cannot simply be split a thousand ways. [[Parallel and External Sorting]] derives that limit with Amdahl's law.

## Worked Examples

These are original teaching examples, not past-paper questions.

**1 — Pipeline throughput.** A five-stage, single-issue pipeline processes 100 instructions. Assume equal one-tick stages, no hazards and no stalls. **Trigger:** independent instructions can overlap. **Tool:** fill cost plus one completion per later tick. Sequential cost: $100(5)=500$ ticks; pipelined cost: $5+99=104$ ticks. Speed-up $500/104\approx4.8$. With 10,000 instructions it is $50{,}000/10{,}004\approx5.0$; more instructions amortise the fill cost.

**2 — Branch-misprediction penalty.** Assume each misprediction adds 15 cycles, 20% of instructions are branches, and 5% of those branches are mispredicted. **Trigger:** an event rate and its cost are given. **Tool:** expected added cycles per instruction. $0.20(0.05)=0.01$ of **all instructions** incur the penalty, giving $0.01(15)=0.15$ added CPI. If base CPI is 1 and penalties do not overlap, CPI becomes 1.15. The 15-cycle penalty is an assumption, not something inferred from pipeline depth.

**3 — SMT hiding a cache miss.** Thread A waits 200 cycles for a load and has no other ready work. **Trigger:** idle resources and independent ready work in B. **Tool:** schedule B on otherwise-unused execution resources. B can make progress during A's wait; how much depends on its instructions and resource needs. Without SMT, out-of-order work from A could also hide some latency if such work existed.

**4 — RISC and CISC.** **Trigger:** compare instruction encodings and implementation. **Tool:** separate the instruction set from the internal engine. Regular encodings can simplify decoding, but RISC does not universally mean fixed-length: RISC-V compressed instructions are a counterexample. Modern x86 processors commonly decode into internal micro-operations. Both families can use wide, out-of-order pipelines; see [[CISC vs RISC]].

## Common Misconceptions

- **"Higher GHz = faster computer."** For one instruction stream, instruction throughput is clock rate times achieved **IPC**; useful multicore speed-up also depends on parallel work. Easy clock-speed scaling slowed around 2005 (→ [[Stories/Dual-Core Craft]]), yet chips kept getting much faster by raising IPC (superscalar, OOO) and adding cores. A GHz number compares only two otherwise-identical cores.
- **"Pipelining makes each instruction faster."** No — it raises **throughput**, not latency. Each instruction still walks all $k$ stages (slightly *slower*, even). You finish one per tick; you don't finish any one sooner.
- **"Hyper-Threading doubles performance / gives twice the cores."** No — SMT shares one core's units; gain is workload-dependent and can be negative. Two *logical* CPUs, one *physical* core.
- **"A GPU is just a faster CPU."** No — it's a different bet (throughput over latency, SIMD over branches). It is *worse* on one sequential branchy thread; it is most effective when sufficient parallel work and useful data reuse keep its resources busy.
- **"More cores → proportionally faster."** **Amdahl's law** (→ [[Parallel and External Sorting]]): the serial fraction caps the speed-up no matter how many cores you add.

## Exam Notes

### Cambridge 9618 (A Level) — §15.1 (+ foundation in §4.1)
The on-syllabus home. For **§15.1** be able to:
- **Explain how pipelining improves performance** — overlapping the fetch/decode/execute stages of successive instructions so that, in the ideal single-issue model, once full, *one instruction completes per clock cycle*; it raises throughput, not the speed of a single instruction.
- State **parallel-processing categories** — **SISD, SIMD, MISD, MIMD** (Flynn). Understand the 2×2 (instruction streams × data streams); a vector operation is SIMD, while independent CPU cores are MIMD; GPU groups require care about the level being described. *Understand the grid — don't merely memorise the four acronyms.*
- Distinguish **RISC vs CISC** and know what **multi-core** and **massively parallel** systems are.
- **Virtual machines** — their operation, uses, benefits and limitations — are taught in [[Operating Systems]].

**§4.1** supplies the foundation used here — the **fetch–decode–execute cycle** and the roles of **cores, cache, and clock speed**. The register-transfer detail (PC/MAR/MDR/CIR/ACC, buses, instruction sets) is examined separately → [[CPU Architecture and the Fetch-Execute Cycle]].

### Cambridge 0478 (IGCSE) — §3
Lighter: the CPU, the **fetch–execute cycle**, and how **cores, cache, and clock speed** affect performance — the foundation section of this card. Pipelining and SMT are beyond 0478, but the cycle and the cores/cache/clock intuition are exactly on it.

### IB Computer Science — first assessment 2027
**A1.1.1 and A1.1.5 (SL/HL)** cover CPU components and the fetch–decode–execute cycle. **A1.1.2 (SL/HL)** names GPU architecture, role and uses; **A1.1.3 (HL only)** compares CPU/GPU design and cooperation. [[The GPU — From Triangles to Tensors]] develops those GPU outcomes. Pipeline hazards, out-of-order scheduling and SMT are explanatory enrichment; the guide does not name them as required A1.1 algorithms.

### AP
**AP CSP Topic 4.3** requires conceptual sequential, parallel and distributed computing, execution time, speed-up and its limits; [[Parallel and External Sorting]] develops those ideas. Pipeline internals and SMT are beyond that named scope. **AP CSA (Fall 2025 CED)** does not prescribe processor architecture. [AP CSP course description](https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-course-and-exam-description.pdf).

### A-Level — OCR and AQA
**OCR H446 §1.1.1(d)** explicitly requires pipelining; §1.1.2 covers RISC/CISC, GPUs and multicore/parallel systems. Its named requirements do not justify importing the entire Cambridge Flynn list. **AQA 7517 §4.7.3.7** names cores, cache, clock speed, word length and bus widths as performance factors; it does not explicitly prescribe pipelining, SMT or Flynn's four categories. These mechanisms remain useful enrichment. [OCR specification](https://www.ocr.org.uk/Images/170844-specification-accredited-a-level-gce-computer-science-h446.pdf) · [AQA specification](https://filestore.aqa.org.uk/resources/computing/specifications/AQA-7516-7517-SP-2015.PDF).

## Connections

- **Prerequisite:** [[Logic Gates]] — gates build the adders and the ALU; this card pipelines the **datapath** those gates form. The execution stage *is* combinational logic doing arithmetic.
- **Sibling:** [[CPU Architecture and the Fetch-Execute Cycle]] — the register-transfer mechanism (PC, MAR, MDR, CIR, ACC, buses and instruction sets).
- **Application / cross-domain:** [[Parallel and External Sorting]] — multi-core and **Amdahl's law** from the algorithm's side; its GPU/bitonic-sort note is this card's SIMD section seen in practice. [[Big-O Notation]] — Amdahl's ceiling is the asymptotic limit of parallel speed-up.
- **Story:** [[Stories/Dual-Core Craft]] — *why* one fast core does so much, the multicore-wall history (Dennard scaling, Herb Sutter's "free lunch is over"), and the SMT / "Dual-Core Craft" meme in full.
- **Leads to:** [[Concurrency]] — once many cores/threads share work, coordinating them safely is its own subject. [[Floating-Point Representation]] — the FPU and vector units these pipelines feed.
- **Extensions:** [[The Modern CPU vs the Textbook Model]] — the exam's spare CU/ALU/registers/buses model vs a real core's many fetch/decode/execution units (the "lone ALU, multiplied"). [[The GPU — From Triangles to Tensors]] — the GPU's invention, its SIMT architecture, and its rise to the engine of modern AI.
- *No exam formula-sheet relevance — this is an architecture/throughput concept, not a formula card.*

## Beyond Syllabus

### Spectre and Meltdown — when speculation became a security hole (2018)
Speculative execution runs instructions on a *guess* and discards the wrong ones — but "discard" only undoes the **architectural** state (registers, memory). The discarded work still left footprints in the **cache**, and by timing later memory accesses an attacker could read those footprints — leaking passwords and keys *across security boundaries*, straight out of the speculative machinery in nearly every CPU built since the 1990s. **Spectre** and **Meltdown** were the first time a pure *performance* trick turned into a *security* catastrophe at planetary scale. The mitigations cost real performance, and — honest edge — speculation was *patched and fenced*, **not removed**: it is far too valuable to give up.

### The memory wall and the cache hierarchy
CPUs got fast faster than DRAM got *close*. A main-memory access costs **hundreds of cycles** — an eternity to a core that retires several instructions per cycle. The whole tower of **L1/L2/L3 caches**, hardware **prefetchers**, OOO execution, and SMT exists to hide that gap. This is the deep reason the data-oriented / ECS layouts in [[Stories/Dual-Core Craft]] matter: packed, sequential arrays **feed the pipeline**; pointer-chasing through scattered objects **starves** it, and no clock speed saves you from a cache miss.

### Dennard scaling and the multicore wall
Until ~2005, each chip generation shrank transistors *and* raised the clock for free — **Dennard scaling**. When it broke (the power density became unmanageable), the only way to spend a denser transistor budget was **more cores**, not faster ones — the pivot Herb Sutter called the end of "the free lunch" (→ [[Stories/Dual-Core Craft]]). This card is the hardware living underneath that history: pipelining, OOO, and SMT are how a *single* core kept improving after its clock stopped climbing.

### Branch predictors are tiny machine-learning models
Some branch-prediction designs learn from past outcomes. A perceptron-based predictor combines history bits with learned weights; other designs use tables and tagged histories. Accuracy depends on both design and workload. The useful connection is adaptive prediction, not the claim that every branch predictor is a neural network.

## LaTeX / Notation Reference

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| $k$ | `k` | number of pipeline stages |
| $N$ | `N` | number of instructions pushed through |
| $k + (N-1)$ | `k + (N-1)` | pipelined cost in ticks (fill + one-per-tick) |
| IPC | `\text{IPC}` | instructions per cycle (retired) — the "width" of a core |
| SISD/SIMD/MIMD | — | Flynn's taxonomy: (single/multiple) instruction × (single/multiple) data |
| SMT | — | simultaneous multithreading (Intel: Hyper-Threading) |
