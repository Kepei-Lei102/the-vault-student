---
chinese: 流水线与同时多线程 (liúxiànxiàn yǔ tóngshí duō xiànchéng)
prerequisites:
  - "[[Logic Gates]]"
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Dual-Core Craft]]"
leads_to:
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

> *A modern CPU core is a factory floor, not a single craftsman. Its whole genius is to never let a workstation sit idle — and when one thread can't keep the floor busy, it quietly invites a second one in. The GPU makes the opposite bet: thousands of identical workers, all doing the exact same step at once. Two philosophies of speed, both born from one fact — the clock stopped getting faster around 2005.*

## Definition — three ideas, one goal (keep the silicon busy)

A processor's work is the **fetch–execute cycle**: fetch an instruction, decode it, execute it, repeat, billions of times a second. Every trick in this card attacks the same waste — **execution units standing idle** — from a different angle:

- **Pipelining** (流水线) — overlap the *stages* of consecutive instructions, like a laundromat running wash, dry, and fold loads at once. It raises **throughput** (instructions finished per second), not **latency** (time for any one instruction). This is the heart of §15.1.
- **Simultaneous Multithreading / SMT** (同时多线程; Intel brands it *Hyper-Threading*) — keep two instruction streams alive on one core, so when thread A stalls, thread B's instructions fill the idle units. One physical core pretends to be two logical ones.
- **The GPU** — the opposite design. Instead of one very clever core hiding latency, use **thousands of simple lanes** running *one* instruction on *many* data items at once (**SIMD**, 单指令多数据). It trades latency for raw throughput.

The unifying question across all three: *given that the clock can't go faster, how do we get more useful work done per tick?*

### 中文锚点

**流水线**（liúxiànxiàn, pipelining）：把连续指令的各个**阶段**（取指 fetch、译码 decode、执行 execute…）**重叠**起来——像洗衣店同时洗一批、烘一批、叠一批。它提升的是**吞吐量**（throughput，每秒完成的指令数），而**不是单条指令的延迟**（latency）。这是 9618 §15.1 的核心。

**冒险/停顿**（hazards）：遇到**分支**（branch，跳转）时下一条指令未知 → 用**分支预测**（branch prediction）先猜着填满流水线，猜错就清空（flush）。更进一步是**乱序执行**（out-of-order）与**投机执行**（speculative execution，投机/推测执行）。

**同时多线程**（tóngshí duō xiànchéng, SMT / 超线程 Hyper-Threading）：一个物理核心同时保留**两个线程**的状态，A 线程停顿时用 B 线程的指令填满空闲单元——典型提速仅 **15–30%**，并非翻倍。

**GPU 与 SIMD**：CPU 把晶体管花在"让**一个**线程尽量快"（深流水线、乱序、大缓存）；GPU 把晶体管花在"**吞吐量**"——上千条简单**车道**对一组数据执行**同一条指令**（SIMD），靠线程多来掩盖延迟。对应 Flynn 分类（SISD / SIMD / MIMD）。

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
> This card teaches the cycle at the level pipelining needs. The full register-transfer story of §4.1 — the **PC, MAR, MDR, CIR, ACC** registers, the address/data/control buses, and instruction sets — is its own card, reserved as [[CPU Architecture and the Fetch-Execute Cycle]]. Here we care about the *stages*, because the stages are what we overlap.

## Pipelining — the laundromat that runs the world

Here is the waste. If you run instructions one at a time, while the EX unit is working, the IF unit, the decoder, and the memory unit all sit idle. Four-fifths of your expensive silicon is doing nothing on every tick.

The fix is the **laundromat insight**. You have a washer, a dryer, and a folding table. The naïve way: wash load 1, dry load 1, fold load 1, *then* start load 2 — three machines, only one ever running. The smart way: the moment load 1 leaves the washer for the dryer, load 2 goes *into* the washer. Now wash, dry, and fold all run at once, on three different loads. You didn't make any single load finish faster; you made a *finished load come out every dry-cycle* instead of every three.

A CPU pipeline does exactly this with instruction stages: as instruction 1 moves IF → ID, instruction 2 enters IF behind it; a tick later instruction 3 enters, and so on. After the pipeline **fills**, one instruction **completes every single tick**.

![[pipeline-staircase.svg|720]]

The diagram is the whole idea. Sequentially (top), 3 instructions over a 5-stage cycle take $3 \times 5 = 15$ ticks. Pipelined (bottom), they take $5 + (3-1) = 7$ ticks — and the gap only widens as instructions pile up.

**The throughput law.** Push $N$ instructions through a $k$-stage pipeline:

$$\text{ticks} = \underbrace{k}_{\text{fill the pipe}} + \underbrace{(N-1)}_{\text{one done per tick after that}}, \qquad \text{speed-up} = \frac{Nk}{k + (N-1)} \xrightarrow{\;N \to \infty\;} k.$$

So a 5-stage pipeline approaches a **5× speed-up** for free — not by working faster, but by never letting a stage idle. This is also *why* clock speeds could climb for decades: splitting the work into more, smaller stages means each stage does less, so the clock can tick faster. (It is not free forever — deeper pipelines pay more on every stall, below.)

> **Throughput vs latency — the one thing students miss.** Pipelining makes *no single instruction faster*. Instruction 1 still takes its 5 ticks end-to-end (often a hair *more*, from the latches between stages). What changes is that instructions now *finish* one-per-tick instead of one-per-five. It is a throughput win, paid for in a small latency cost — the exact trade a busy kitchen makes when it plates many orders by overlapping prep, not by cooking any one dish faster.

## When the pipeline chokes — hazards and bubbles

The laundromat works because the loads are independent. Instructions are not always so polite, and when they depend on each other the pipeline must **stall** — insert a **bubble** (a wasted tick). Three kinds of trouble:

- **Data hazard** — instruction 2 needs the result instruction 1 hasn't written back yet (`x = a + b;  y = x + c;`). The hardware fix is **forwarding** (bypass the result straight from the EX output to the next EX input instead of waiting for WB); when even that isn't enough, it stalls.
- **Control hazard** — a **branch** (`if`, loop, function call). Until the branch *executes*, the CPU doesn't know which instruction comes next — but the pipeline wants to fetch the next instruction *now*. This is the expensive one.
- **Structural hazard** — two instructions want the same unit (e.g. one memory port) on the same tick.

The control hazard is so costly that CPUs **guess**. A **branch predictor** bets on which way the branch will go and keeps fetching down the predicted path, so the pipeline stays full. Guess right (and modern predictors are right **>99%** of the time) and you paid nothing. Guess wrong and you must **flush** every wrongly-fetched instruction and refill the pipe — and in a deep pipeline that is *k* wasted ticks. Deeper pipelines buy a higher clock but a steeper misprediction penalty; chip designers spend enormous effort balancing the two.

## Going wider and out of order — the modern fast core

Once a pipeline reliably finishes one instruction per tick, the next question is greedy: *can we finish more than one?* Three escalating tricks turn a simple pipeline into a modern high-performance core, and all three are the same idea — **find independent work to keep more units busy**:

1. **Superscalar** — build *several* pipelines side by side, so multiple instructions enter each stage per tick. Now the core can retire 2, 4, or more instructions per cycle: its **IPC** (instructions per cycle) rises above 1.
2. **Out-of-order execution (OOO)** — if instruction 3 is stuck waiting on a slow memory load, but instructions 4 and 5 are independent and ready, *run them now* and slot the results back into program order later. The core reorders work behind the scenes to dodge stalls.
3. **Speculative execution** — don't just *predict* a branch and keep fetching; actually *execute* past it on the guess, holding the results provisionally. If the guess was right, commit them; if wrong, discard them as if they never happened.

The three tricks, side by side — all chasing the same prize, *find independent work to keep every unit busy*:

![[superscalar-ooo-speculative.svg|760]]

> [!info] Beyond the textbook CPU model
> Cambridge's CPU is deliberately spare — one **CU**, one **ALU**, a handful of named registers, three buses. A real modern core has *several* fetch and decode units, **many** parallel execution units (multiple ALUs plus separate floating-point, load, store, and branch units — the row in the diagram above), a reorder buffer to track the out-of-order work, and a branch predictor that is itself a small learning machine. The gap between the exam model and the silicon in your phone is wide enough to be its own card — reserved as [[The Modern CPU vs the Textbook Model]].

This is what a "fast core" really is: a deep, **superscalar**, **out-of-order**, **speculative** engine whose entire purpose is to scavenge enough independent instructions to keep its execution units fed. It is also why **clock speed alone is a terrible measure** of a CPU — a 3 GHz core today does several times the work per tick of a 3 GHz core from 2005, because its IPC is far higher.

### Watch the engine fill itself

The panels above are one cycle each; the real magic is *cycle after cycle*. The animation below traces a RISC core doing exactly that: the front-end streams ops into the **op queue**, the **out-of-order scheduler** fires every *ready* op into every free unit, a **not-yet-ready op waits while younger ops pass it** (out-of-order), a **cache-missed load** ties up Load/Store while the ALUs keep cycling, and the **branch predictor** keeps the front-end fed. Watch the *"units busy this cycle"* gauge climb.

A clean teaching core first — 4-wide fetch, 6 execution units:

![[core-pipeline-fill-simplified.mp4]]

…then the *same engine* scaled to an **Apple-Firestorm-style** core — 8-wide decode, a 630-entry reorder buffer, and 12 execution units (6 ALU + 4 SIMD + 2 load/store). The shape is identical; only the *width* changed — which is exactly the lesson of the cross-CPU comparisons in hardware deep-dives: every modern core, ARM or x86, has converged on the same out-of-order engine:

![[core-pipeline-fill-firestorm.mp4]]

> [!info] What this foreshadows — [[CISC vs RISC]]
> Line three of those cross-CPU diagrams is the punchline: Apple (ARM), AMD (x86), and Intel (x86) draw *almost the same picture*. Decode width differs (ARM's fixed-length instructions decode 8-wide; x86's variable-length ones top out at ~4–5 and are cracked into RISC-like micro-ops first), but underneath, all three run the same wide out-of-order engine you just watched. **The hardware has converged; the ecosystem hasn't** — that's the [[CISC vs RISC]] card.

## Simultaneous Multithreading — two streams, one core

Even a brilliant out-of-order core hits a wall: sometimes a *single* thread simply has no independent work left to run. A **cache miss** to main memory takes ~200 ticks; if every instruction in the queue depends on that load, the whole expensive core sits idle, twiddling its thumbs for 200 ticks.

**SMT** is the elegant fix. Keep the architectural state — the registers, the program counter — of **two threads** on the same core, and let the scheduler pull instructions from *either* stream into the shared execution units. The key insight: **instructions from two independent threads have no data dependencies between them**, so they can never stall *each other*. When thread A blocks on its cache miss, thread B's instructions pour into the idle units and get real work done in the shadow of the stall.

To the operating system, one SMT core looks like **two logical processors** ("8 cores, 16 threads" on a spec sheet means 8 physical cores with SMT). But be honest about the payoff:

> [!warning] SMT is not a second core
> The two logical threads **share one core's execution units, caches, and ports** — they are not two independent cores. Typical real-world gain is **+15–30%**, and on workloads that already saturate the units (or thrash the shared cache) it can be **zero or even negative**. "Hyper-Threading doubles your performance" is the single most common myth here. It fills *bubbles*; it does not duplicate hardware.

This is the hardware answer to [[Stories/Dual-Core Craft]]: a single physical core, made to look like two and kept relentlessly busy, is why one good core can carry so much — and why a famously single-threaded game leans on one or two fast SMT cores rather than on core *count*.

## The GPU — the opposite bet (SIMD)

Everything above spends transistors making **one thread** fast: deep pipelines, branch predictors, out-of-order machinery, big caches. That is the CPU's bet — minimise **latency** for a few very clever cores. The **GPU** makes the opposite bet — maximise **throughput** with thousands of *simple* cores — and **Flynn's taxonomy** is the cleanest way to see the choice. Classify any machine by how many **instruction streams** and **data streams** it runs at once:

| | **Single data** | **Multiple data** |
|---|---|---|
| **Single instruction** | **SISD** — a classic single core | **SIMD** — one instruction, many data: a GPU lane / CPU vector unit |
| **Multiple instruction** | *(MISD — rare; fault-tolerant pipelines)* | **MIMD** — many independent cores: multi-core CPUs, clusters |

![[cpu-vs-gpu-latency-throughput.svg|697]]

A GPU is the **SIMD** cell taken to an extreme. Its cores are grouped, and a whole group (NVIDIA calls it a **warp** of 32 lanes; AMD a **wavefront**) executes the *same single instruction* on 32 different data elements at once — one decoder driving 32 ALUs. It doesn't hide memory latency with clever OOO logic; it hides latency by having *so many* warps ready that whenever one group stalls, another instantly runs. Cleverness is replaced by sheer numbers.

The catch is **branch divergence**. If the 32 lanes of a warp hit an `if` and some go one way while others go the other, the hardware must run *both* paths with the inactive lanes **masked off** — so a branchy workload wastes most of the SIMD width. GPUs therefore love **regular, branch-free, data-parallel** work: matrix multiplication, image filtering, and the dense linear algebra under neural networks (and, yes, the large language model reading this card). They are slower than a CPU on a single sequential, branchy thread, and that is by design.

> [!info] Why GPUs sort with networks, not merge sort
> [[Parallel and External Sorting]] notes that GPUs sort using **bitonic sorting networks** — a *fixed*, data-independent pattern of compare-and-swap operations — rather than merge sort. Now you can see why: a fixed pattern has **no data-dependent branches**, so all 32 lanes of a warp do the same compare-swap in lockstep with zero divergence. The "best" algorithm depends on the machine, and SIMD is the reason.

## Worked Examples

**1 — Pipeline throughput.** A 5-stage pipeline runs a loop of 100 instructions. Sequential cost: $100 \times 5 = 500$ ticks. Pipelined: $5 + (100 - 1) = 104$ ticks. Speed-up $= 500/104 \approx \mathbf{4.8\times}$, already near the 5× ceiling — and for 10,000 instructions it is $50{,}000 / 10{,}004 \approx 5.0\times$. *More instructions amortise the fill cost.*

**2 — Branch-misprediction penalty.** A 15-stage pipeline mispredicts a branch. Every instruction fetched on the wrong path — up to **15** of them — must be flushed, costing ~15 wasted ticks before useful work resumes. If 20% of instructions are branches and the predictor is wrong 5% of the time, that's $0.20 \times 0.05 = 1\%$ of branches mispredicting, each costing ~15 ticks — a measurable but survivable drag, and exactly why >99% prediction accuracy is worth so much silicon.

**3 — SMT hiding a cache miss.** Thread A issues a load that misses to DRAM (~200 ticks). Without SMT the core idles for all 200. With SMT, thread B — independent, so it cannot depend on A's load — feeds ~200 ticks of useful instructions into the otherwise-idle units. The stall became someone else's productive time.

**4 — RISC vs CISC, in one line.** **RISC** (ARM, RISC-V) uses many *simple, fixed-length* instructions — easy to pipeline, because every instruction marches through the same stages. **CISC** (x86) has fewer, *complex, variable-length* instructions; modern x86 chips cope by **decoding each one into RISC-like micro-ops** internally and pipelining *those*. Pipelining is so valuable that even the CISC survivor became RISC-like under the hood.

## Common Misconceptions

- **"Higher GHz = faster computer."** Performance $\approx$ clock $\times$ **IPC** $\times$ cores. Clock speed stalled near 3–4 GHz around 2005 (→ [[Stories/Dual-Core Craft]]), yet chips kept getting much faster by raising IPC (superscalar, OOO) and adding cores. A GHz number compares only two otherwise-identical cores.
- **"Pipelining makes each instruction faster."** No — it raises **throughput**, not latency. Each instruction still walks all $k$ stages (slightly *slower*, even). You finish one per tick; you don't finish any one sooner.
- **"Hyper-Threading doubles performance / gives twice the cores."** No — SMT shares one core's units; gain is typically **+15–30%**, sometimes negative. Two *logical* CPUs, one *physical* core.
- **"A GPU is just a faster CPU."** No — it's a different bet (throughput over latency, SIMD over branches). It is *worse* on one sequential branchy thread; it wins only on wide, regular, data-parallel work.
- **"More cores → proportionally faster."** **Amdahl's law** (→ [[Parallel and External Sorting]]): the serial fraction caps the speed-up no matter how many cores you add.

## Exam Notes

### Cambridge 9618 (A Level) — §15.1 (+ foundation in §4.1)
The on-syllabus home. For **§15.1** be able to:
- **Explain how pipelining improves performance** — overlapping the fetch/decode/execute stages of successive instructions so that, once the pipeline is full, *one instruction completes per clock cycle*; it raises throughput, not the speed of a single instruction.
- State **parallel-processing categories** — **SISD, SIMD, MISD, MIMD** (Flynn). Understand the 2×2 (instruction streams × data streams); a GPU/vector unit is SIMD, a multi-core CPU is MIMD. *Understand the grid — don't merely memorise the four acronyms.*
- Distinguish **RISC vs CISC** and know what **multi-core** and **massively parallel** systems are.
- (**Virtual machines**, the other half of §15.1, is separate-card territory.)

**§4.1** supplies the foundation used here — the **fetch–decode–execute cycle** and the roles of **cores, cache, and clock speed**. The register-transfer detail (PC/MAR/MDR/CIR/ACC, buses, instruction sets) is examined separately → [[CPU Architecture and the Fetch-Execute Cycle]].

### Cambridge 0478 (IGCSE) — §3
Lighter: the CPU, the **fetch–execute cycle**, and how **cores, cache, and clock speed** affect performance — the foundation section of this card. Pipelining and SMT are beyond 0478, but the cycle and the cores/cache/clock intuition are exactly on it.

### IB Computer Science — A1.1 Computer hardware and operation
The performance strand of A1.1 (what makes a processor fast) is exactly this card's territory: cores, cache, clock speed, and the pipelining/parallelism that let one core do more per cycle. IB keeps this at the conceptual level — the *idea* that overlapping stages and running independent work in parallel raise throughput — rather than the stage-by-stage hazard analysis; the laundromat intuition and the throughput-vs-latency distinction are the parts an A1.1 answer needs.

### AP
**AP CS Principles** touches parallel & distributed computing at a high level (the speed-up from running independent portions in parallel) — that intuition lives in [[Parallel and External Sorting]] (Amdahl). **AP CSA** does not cover processor architecture.

### A-Level (AQA / OCR)
Cover pipelining, Flynn's taxonomy, and parallel processing with the same concepts; OCR also names the stages and the von Neumann bottleneck. The treatment here is board-portable.

## Connections

- **Prerequisite:** [[Logic Gates]] — gates build the adders and the ALU; this card pipelines the **datapath** those gates form. The execution stage *is* combinational logic doing arithmetic.
- **Sibling (reserved):** [[CPU Architecture and the Fetch-Execute Cycle]] — the register-transfer-level §4.1 card (PC, MAR, MDR, CIR, ACC, buses, instruction sets) that this card sits on top of.
- **Application / cross-domain:** [[Parallel and External Sorting]] — multi-core and **Amdahl's law** from the algorithm's side; its GPU/bitonic-sort note is this card's SIMD section seen in practice. [[Big-O Notation]] — Amdahl's ceiling is the asymptotic limit of parallel speed-up.
- **Story:** [[Stories/Dual-Core Craft]] — *why* one fast core does so much, the multicore-wall history (Dennard scaling, Herb Sutter's "free lunch is over"), and the SMT / "Dual-Core Craft" meme in full.
- **Leads to (reserved):** [[Concurrency]] — once many cores/threads share work, coordinating them safely is its own subject. [[Floating-Point Representation]] — the FPU and vector units these pipelines feed.
- **Extensions (reserved enrichment):** [[The Modern CPU vs the Textbook Model]] — the exam's spare CU/ALU/registers/buses model vs a real core's many fetch/decode/execution units (the "lone ALU, multiplied"). [[The GPU — From Triangles to Tensors]] — the GPU's invention, its SIMT architecture, and its rise to the engine of modern AI.
- *No exam formula-sheet relevance — this is an architecture/throughput concept, not a formula card.*

## Beyond Syllabus

### Spectre and Meltdown — when speculation became a security hole (2018)
Speculative execution runs instructions on a *guess* and discards the wrong ones — but "discard" only undoes the **architectural** state (registers, memory). The discarded work still left footprints in the **cache**, and by timing later memory accesses an attacker could read those footprints — leaking passwords and keys *across security boundaries*, straight out of the speculative machinery in nearly every CPU built since the 1990s. **Spectre** and **Meltdown** were the first time a pure *performance* trick turned into a *security* catastrophe at planetary scale. The mitigations cost real performance, and — honest edge — speculation was *patched and fenced*, **not removed**: it is far too valuable to give up.

### The memory wall and the cache hierarchy
CPUs got fast faster than DRAM got *close*. A main-memory access costs **hundreds of cycles** — an eternity to a core that retires several instructions per cycle. The whole tower of **L1/L2/L3 caches**, hardware **prefetchers**, OOO execution, and SMT exists to hide that gap. This is the deep reason the data-oriented / ECS layouts in [[Stories/Dual-Core Craft]] matter: packed, sequential arrays **feed the pipeline**; pointer-chasing through scattered objects **starves** it, and no clock speed saves you from a cache miss.

### Dennard scaling and the multicore wall
Until ~2005, each chip generation shrank transistors *and* raised the clock for free — **Dennard scaling**. When it broke (the power density became unmanageable), the only way to spend a denser transistor budget was **more cores**, not faster ones — the pivot Herb Sutter called the end of "the free lunch" (→ [[Stories/Dual-Core Craft]]). This card is the hardware living underneath that history: pipelining, OOO, and SMT are how a *single* core kept improving after its clock stopped climbing.

### Branch predictors are tiny machine-learning models
A modern branch predictor (Intel's and AMD's are **TAGE**- and **perceptron**-based) *learns* each branch's behaviour at runtime, reaching **>99%** accuracy on real code. It is, quite literally, a small online-learning model sitting in the CPU's front end, trained continuously on the program's own control flow — a neural net guarding the mouth of the pipeline.

## LaTeX / Notation Reference

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| $k$ | `k` | number of pipeline stages |
| $N$ | `N` | number of instructions pushed through |
| $k + (N-1)$ | `k + (N-1)` | pipelined cost in ticks (fill + one-per-tick) |
| IPC | `\text{IPC}` | instructions per cycle (retired) — the "width" of a core |
| SISD/SIMD/MIMD | — | Flynn's taxonomy: (single/multiple) instruction × (single/multiple) data |
| SMT | — | simultaneous multithreading (Intel: Hyper-Threading) |
