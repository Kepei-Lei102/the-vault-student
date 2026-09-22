---
chinese: 现代 CPU 与课本模型 (xiàndài CPU yǔ kèběn móxíng)
prerequisites:
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Pipelining and Simultaneous Multithreading]]"
  - "[[RAM and the Memory Hierarchy]]"
leads_to: []
tags:
  - subject/cs
  - domain/hardware
  - domain/computer-architecture
  - level/A-Level
  - level/IB-HL
  - level/university
  - curriculum/Cambridge-9618
  - curriculum/Cambridge-0478
  - curriculum/IB-CS
  - type/theory
  - type/hands-on
  - type/visual-tool
  - notation/ipc
  - misconception/clock-speed-is-speed
  - misconception/the-textbook-cycle-is-what-happens
  - misconception/out-of-order-changes-the-answer
  - misconception/branch-prediction-is-the-compilers-job
  - misconception/more-cores-make-one-program-faster
---

# The Modern CPU vs the Textbook Model 现代 CPU 与课本模型

> Take a million random numbers between 0 and 255, and add up the ones that are 128 or more. Now sort the list first and do exactly the same. On the laptop this card was written on, the sorted version runs three times faster. Same numbers, same additions, same result. The textbook CPU, one instruction after another through fetch, decode and execute, has no way to explain that. The real one does.

## What this is for

[[CPU Architecture and the Fetch-Execute Cycle]] gives the model every syllabus examines: a control unit, one ALU, a handful of registers, three buses, one instruction at a time. [[Pipelining and Simultaneous Multithreading]] shows how the fast core overlaps instructions, and names superscalar, out-of-order and speculative execution. This card measures the gap between the two. It runs three experiments on a real processor, simulates the same program on three machines, and explains what a modern core does with the freedom it has: anything at all, as long as nobody outside can tell. That last clause is the idea the whole card turns on, and it is the reason your code can be three times slower than the same code with the data in a different order.

## Definition

### Formal

The **architecture** of a processor is its contract: the instruction set, the registers a program can name, and the rule that instructions take effect one after another in program order. The textbook fetch–decode–execute model is that contract. The **microarchitecture** is the engine that honours it: a modern core fetches and decodes several instructions per cycle, renames registers to remove false dependencies, holds hundreds of instructions in flight in a **reorder buffer**, issues each one as soon as its operands are ready regardless of its position in the program, executes past branches on a **predicted** path, and **commits** results in program order so that the visible state is always one a sequential machine could have produced. Its performance is measured in **instructions per cycle** (IPC), not clock speed, and is lost to three things above all: mispredicted branches, chains of dependent instructions, and cache misses.

### Intuitive

The textbook CPU is one cook: read the next line of the recipe, do it, read the next. A modern core is a restaurant kitchen at full service: twenty orders in progress, the chef starting the sauce before the ticket that needs it is confirmed, whatever is ready cooked first, and yet the plates leave the pass in ticket order, so the dining room never sees the chaos. That last rule is the whole trick. Inside, the core may run instructions early, out of order and on a guess; outside, the results look exactly as if one cook had followed the recipe line by line. When a guess is wrong, the half-cooked dish is thrown away, and the diner notices only a longer wait. That wait is the one thing measurable from outside, and this card measures it.

### 中文锚点 (Chinese Anchor)

课本里的 CPU 是厨房里的一个厨师：读一行菜谱，照着做，再读下一行。现代的处理器核心是一间正在高峰期运转的餐厅后厨。二十份订单同时在做；主厨提前看单，凭着前一百张单子猜下一桌会点什么，还没等那张单确认，酱汁已经先熬上了；什么食材备好了就先做什么，等着烤箱的先放到一边；可是盘子从出菜口出去的顺序，和单子进来的顺序完全一致，餐厅里的客人永远不知道厨房里有多乱。窍门全在最后这条规矩上。核心在里面想怎么干都行，提前干、打乱顺序干、凭猜测先干，只要它放出来的结果，看起来就像一位厨师照着菜谱一行一行做出来的。猜错了，它就把做到一半的菜倒掉重来，客人能察觉的只是多等了一会儿。这一会儿，恰恰是从外面唯一能量出来的东西，这张卡片量的就是它。

## Notation

| Term | Meaning | Notes |
|---|---|---|
| IPC | instructions completed (retired) per clock cycle | the real measure of a core's speed; the textbook machine is far below 1 |
| latency | cycles from issuing an instruction to its result being usable | a dependent instruction must wait this long |
| throughput | how many of an instruction can *start* per cycle | independent instructions overlap; latency stops mattering |
| reorder buffer (ROB) | the list of every instruction in flight, in program order | results wait here until everything before them has committed |
| micro-op (µop) | the internal operation an instruction is decoded into | one x86 instruction may be several; most ARM instructions are one |
| register renaming | mapping the named registers onto a larger physical file | removes "false" dependencies where two instructions only reuse a name |
| mispredict penalty | cycles lost when a branch guess was wrong | 10–20 on a modern core; every instruction fetched on the wrong path is discarded |
| cache line | the unit the memory system moves, 64 or 128 bytes | one miss fetches the whole line, which is why sequential access is cheap |
| ns per operation | what the experiments below measure | at 3.2 GHz one cycle is 0.31 ns |

> [!warning] Notation trap
> "Cycle" in the syllabus means one fetch–decode–execute cycle, one instruction. "Cycle" in this card means one tick of the clock, during which a modern core may complete six instructions or none. The syllabus's "clock speed" measures the ticks; only IPC says what a tick was worth.

## Part I — The contract and the engine

![[modern-cpu-contract-and-engine.svg|1000]]

The left side is the syllabus, and it is not wrong. It is the **specification** a program is written against: there are registers with these names, instructions do these things, and each instruction completes before the next begins. Every compiler, every operating system and every exam question relies on exactly that.

The right side is what a 2020s core builds to satisfy the specification faster than the specification describes. The numbers are for the core in the Apple M1 family, which is unusually wide but not unusual in shape; AMD's and Intel's cores draw the same diagram with smaller numbers. Read it top to bottom.

1. **The front end** fetches and decodes eight instructions per cycle into micro-ops, following the **branch predictor**'s guess about where the program is going. It runs a hundred or more instructions ahead of anything that has actually finished.
2. **Rename.** A program can name 32 registers; the core has about 400 physical ones. Each instruction that writes a register is given a fresh physical register, so two instructions that merely *reuse* a name, say both writing `r1` for unrelated purposes, no longer have to wait for each other. Only true dependencies remain: a value actually needed by a later instruction.
3. **The reorder buffer** holds every instruction in flight, about 630 of them, in program order. This is the kitchen's ticket rail.
4. **The schedulers** issue any instruction whose operands are ready to any free execution unit: six integer ALUs, four load/store units, four floating-point and vector units, two branch units. Instruction 400 may execute before instruction 3 if instruction 3 is waiting on memory.
5. **Commit** retires instructions from the head of the reorder buffer, in program order, making their results architecturally visible. If the head instruction was on a mispredicted path, or raised an exception, everything behind it is discarded and the core restarts from the correct instruction. Because commit is in order, an exception always appears to happen at exactly one instruction with everything before it done and nothing after it started, which is what the operating system in [[Interrupt Handling]] requires.

The engine, then, is an elaborate way of running a sequential program as if it were parallel, while promising that you will never catch it doing so. The promise is kept at the commit stage; everything above it is free to cheat.

## Part II — Three measurements on one laptop

`modern-cpu-lab.c` runs three experiments. Each runs the same instructions twice and changes only how the engine can treat them. The numbers below are from an Apple M1 Max at 3.2 GHz, compiled with `cc -O1`.

![[modern-cpu-measurements.svg|1000]]

**1. Predictability.** A million numbers, an `if (a[i] >= 128)` on each. Unsorted, the branch is a coin toss and the predictor is wrong half the time: $3.86$ ns per element. Sorted, the branch is *false, false, false … true, true, true*, the predictor learns the pattern in a few iterations and is wrong once: $1.27$ ns per element. Three times faster for the same work. The lost time is the mispredict penalty: on each wrong guess, everything the front end had fetched on the wrong path, dozens of instructions, is thrown away and fetching restarts.

> [!info] What happened at -O2
> Compile the same file with `-O2` and the two timings collapse to the same value, because the compiler has replaced the branch with a **conditional move**: compute both possibilities and select one, with no jump for the predictor to guess. The compiler did the predictor's job for it. This is why the experiment's branch body writes to a small table through a computed address: a store that only happens on one path cannot be turned into a select, so the branch survives and the effect is visible. Modern performance is a negotiation between the compiler and the core, and a good compiler removes branches the way a good cook takes decisions off the chef's plate.

**2. Dependence.** Four hundred million floating-point additions. As one running sum, each addition needs the previous result, so the chain runs at the add unit's **latency**, about three cycles: $1.02$ ns per add. Split into eight independent sums, the additions overlap and the core runs at the units' **throughput**, several per cycle: $0.127$ ns per add, eight times faster. The instructions are identical. What changed is that the engine had independent work to fill its units with, which is the entire purpose of the reorder buffer. This is the number the textbook model cannot express at all: it has one ALU and no notion of two additions happening at once.

**3. Locality.** Sixteen million loads, each fetching the next address from the previous one. Walking the array in order, the hardware prefetcher sees the pattern and has the next cache line ready: $1.49$ ns per load. Following a random permutation of the same array, every load misses every cache and waits for main memory: $145.6$ ns per load. A hundred times slower, and no amount of out-of-order execution hides it, because each load depends on the one before. [[RAM and the Memory Hierarchy]] describes the caches; this is what they are worth.

Three ratios, three, eight and a hundred, and none of them appears in the textbook model, where every instruction costs one cycle.

## Part III — One program on three machines

`modern-cpu-simulator.py` is a small cycle-level simulator. It takes the branch experiment as an instruction stream, four thousand iterations of *load, compare, branch, (add), increment*, and runs it on three machines with the same latencies: a load takes four cycles, everything else one.

- **Textbook:** one instruction at a time, each through all five stages before the next starts.
- **In-order pipeline:** one instruction issued per cycle, a stall when an instruction needs a result that is not ready, a static "branch not taken" guess with a three-cycle flush when wrong.
- **Out-of-order:** six instructions fetched per cycle into a 128-entry window, issued when ready, committed in order, with a two-bit branch predictor and a flush of the whole window on a misprediction.

![[modern-cpu-simulator.svg|900]]

| machine | unsorted data | sorted data |
|---|---|---|
| textbook | IPC $0.18$ | IPC $0.18$ |
| in-order pipeline, static guess | IPC $0.50$, $1\,957$ mispredicts | IPC $0.50$, $1\,957$ mispredicts |
| out-of-order, 2-bit predictor | IPC $0.92$, $2\,007$ mispredicts | IPC $4.46$, $3$ mispredicts |

Read the last row. The same core is five times faster on sorted data, because a predictor that learns can only learn a pattern that exists. Read the middle row: the pipeline does not care about sorting, because its guess never changes, which is the difference between a static and a dynamic predictor. And read the first column: on unpredictable data the out-of-order core is barely twice the in-order pipeline, because every mispredict throws away a window it spent cycles filling. Speculation is a bet, and the simulator shows both sides of it.

The Manim clip below takes eight instructions through the two lanes cycle by cycle: a load that misses, the in-order machine waiting behind it, the out-of-order machine running the independent instructions during the wait, the results still committing in order, and then a mispredicted branch and what it costs.

![[modern-cpu-out-of-order.mp4]]

## Part IV — Why it is allowed to cheat

Two ideas make the engine legal.

**Renaming removes false dependencies.** Consider

```
r1 = load a
r2 = r1 + 1
r1 = load b        (reuses the name r1)
r3 = r1 * 2
```

The third instruction does not depend on the first two; it only reuses the name `r1`. On the textbook machine that reuse would force it to wait. The engine gives the second `r1` a different physical register, and now instructions 3 and 4 can run while instruction 1 is still waiting on memory. The only dependencies left are the true ones, where a value is actually needed: instruction 2 on 1, instruction 4 on 3.

**In-order commit preserves the illusion.** The reorder buffer lets instructions *execute* in any order but *retire* in program order. Instruction 4 may finish before instruction 2, but its result sits in the buffer until 1, 2 and 3 have committed. So at every moment the architecturally visible state (the named registers, memory) is one that the textbook machine would have reached after some prefix of the program. A debugger stopping the program sees that state; an interrupt arriving sees that state; a mispredicted branch, discovered when it reaches the head of the buffer, discards everything behind it and leaves that state. Nothing that was speculated ever became visible.

Stores need one more rule, since a store to memory cannot be undone by discarding a buffer entry: stores wait in a **store buffer** and reach memory only at commit. A later load that needs the stored value reads it from the buffer instead, a trick called forwarding, and if the core guesses wrongly that a load and an earlier store touch different addresses it replays the load. Every one of these mechanisms exists to keep one promise: from outside, the program ran in order.

> [!info] The one place the promise leaked
> In 2018 the Spectre and Meltdown attacks showed that "nothing speculated ever became visible" was true of registers and memory but not of the *cache*. An instruction executed on a wrong path was discarded, but the cache line it had fetched stayed fetched, and a program that timed its own memory accesses could tell which line that was, and so read a secret it was never allowed to read. [[Pipelining and Simultaneous Multithreading]]'s Beyond section tells that story; the point here is that it was a hole in the *contract*, not in any one chip, and every core built since carries fences to patch it.

## Where this is the working tool

**Writing fast code.** Every rule of thumb in performance work is one of the three measurements in disguise. Keep branches predictable or remove them; that is why sorted data, and code that avoids `if` inside hot loops, runs faster. Give the core independent work; that is why a numerical loop uses several accumulators and why compilers unroll loops. Keep data contiguous and walk it in order; that is why an array of records beats a linked list by a hundred to one, and why game engines lay out their entities as arrays of components. [[The GPU — From Triangles to Tensors]] takes the same three lessons to their extreme: no branches, thousands of independent threads, coalesced memory.

**Reading a benchmark.** A processor's headline clock is the least informative number on the box. A 2005 core at $3.8$ GHz with an IPC near $1$ is slower than a 2021 core at $3.2$ GHz with an IPC of $4$; Example 5 does the arithmetic. This is also why a phone chip at $3$ GHz can outrun a desktop chip at $4$: width and prediction, not frequency.

**Compilers.** `-O2` turned the branch into a conditional move, unrolled loops and reordered independent work; a compiler is a static out-of-order engine that runs once, before the program does. The two engines cooperate, and understanding either requires knowing what the other will do.

**Profilers.** Modern cores expose **performance counters**: cycles, instructions, mispredicted branches, cache misses. A profiler reads them and tells you which of the three walls your program hit. IPC well below the core's width, and a mispredict or miss count to match, is the diagnosis; the cure is in the paragraph above.

**Hands-on.** `modern-cpu-lab.c` compiles with any C compiler: `cc -O1 -o lab modern-cpu-lab.c && ./lab`, then again with `-O2` to watch the branch vanish. `modern-cpu-simulator.py` runs in a second; change the reorder-buffer size to 8 and watch the out-of-order core lose most of its advantage, or change the load latency to 40 to see what a cache miss does to all three machines. Predict each before you run it.

## Worked examples

### Example 1: IPC from a run

*A program of $2.4 \times 10^9$ instructions runs in $0.5$ s on a $3.2$ GHz core. What is its IPC, and what fraction of a six-wide core's capacity is that?*

**Trigger:** "instructions", "time" and "clock" together mean cycles $=$ time $\times$ frequency. **Tool: IPC $=$ instructions $/$ cycles.**

Cycles $= 0.5 \times 3.2 \times 10^9 = 1.6 \times 10^9$; IPC $= 2.4 \times 10^9 / 1.6 \times 10^9 = 1.5$. A six-wide core could in principle retire six per cycle, so the program uses a quarter of the engine; the rest is lost to waiting, and the performance counters say what for.

### Example 2: what a mispredict costs

*A loop body is five instructions containing one branch. The branch is mispredicted with probability $p$ and a mispredict costs $15$ cycles. If the core would otherwise average $4$ IPC, what is the effective IPC at $p = 0.5$ and at $p = 0.02$?*

**Trigger:** an average cost per iteration mixes a base cost with a penalty times its probability. **Tool: expected cycles per iteration $=$ base $+$ $p \times$ penalty**, which is [[Probability Basics]]'s expected value.

Base cost is $5/4 = 1.25$ cycles per iteration. At $p = 0.5$: $1.25 + 0.5 \times 15 = 8.75$ cycles, so IPC $= 5/8.75 = 0.57$. At $p = 0.02$: $1.25 + 0.3 = 1.55$ cycles, IPC $= 3.2$. A predictor that is right $98\,\%$ of the time keeps most of the core's width; one that is right half the time throws almost all of it away, which is what the unsorted run measured.

### Example 3: how many chains saturate a unit

*A floating-point add has a latency of $3$ cycles and the core can start $4$ adds per cycle. How many independent running sums are needed to reach full throughput, and what throughput does a single sum achieve?*

**Trigger:** latency against throughput is a pipeline-fill question: to keep $4$ units busy for $3$ cycles each you need $4 \times 3$ adds in flight. **Tool: chains needed $=$ latency $\times$ throughput** (Little's law, the same bookkeeping as [[Pipelining and Simultaneous Multithreading]]'s laundromat).

$3 \times 4 = 12$ independent chains saturate the units. One chain achieves $1/3$ of an add per cycle against a possible $4$: a factor of $12$. The measurement in Part II found a factor of $8$ with eight chains, which is what the formula predicts for eight: $8/3 = 2.7$ adds per cycle against $1/3$.

### Example 4: the memory wall in seconds

*A program follows $10^8$ pointers. How long does it take if the pointers are laid out sequentially, and if they are random, using the measured $1.49$ and $145.6$ ns per load?*

**Trigger:** total time $=$ count $\times$ time per operation, with the per-operation time set by the access pattern. **Tool: the measured latencies.**

Sequential: $10^8 \times 1.49\ \text{ns} = 0.15$ s. Random: $10^8 \times 145.6\ \text{ns} = 14.6$ s. Same pointers, same instructions; the layout costs a hundredfold, which is more than any difference between a slow and a fast processor.

### Example 5: clock speed against IPC

*Core A runs at $3.8$ GHz and averages $1.0$ instructions per cycle. Core B runs at $3.2$ GHz and averages $4.0$. Which finishes a $10^{10}$-instruction program first, and by what factor?*

**Trigger:** the syllabus's "factors affecting performance" question, answered with the missing factor. **Tool: time $=$ instructions $/$ (IPC $\times$ frequency).**

A: $10^{10} / (1.0 \times 3.8 \times 10^9) = 2.63$ s. B: $10^{10} / (4.0 \times 3.2 \times 10^9) = 0.78$ s. B is $3.4$ times faster despite the slower clock. The exam answer "a higher clock speed means more instructions per second" is true only between cores of equal IPC, which is to say between the same core at two frequencies.

## Common Misconceptions (Teaching Notes)

### 1. "Clock speed measures how fast a processor is"

It measures how often the clock ticks. What a tick achieves is IPC, and that varies by a factor of five between cores of the same era and by a factor of thirty between the textbook machine and a modern one on the same program (Part III). The 9618 list of performance factors is right that clock speed matters; it matters as one factor among several, and the least decisive.

### 2. "The fetch–decode–execute cycle is what the hardware does, one instruction at a time"

It is what the hardware *promises*. What it does is fetch eight at once, execute out of order and guess. The cycle is a specification, and every result the program can see is consistent with it, which is the only sense in which it "happens".

### 3. "Out-of-order execution could change the program's answer"

It cannot, because commit is in order and only true dependencies are respected. An instruction that needs a value waits for that value; an instruction that merely reuses a register name is renamed. The reordering is invisible except in the clock.

### 4. "Branch prediction is something the compiler does"

The compiler can *remove* branches (the conditional move at `-O2`) and can lay out code so that the likely path is the fall-through, but the predictor is hardware, learns at run time from the branch's own history, and is what made the sorted run fast. The two cooperate; neither replaces the other.

### 5. "More cores make a program faster"

More cores run more *programs*, or the parallel parts of one. A single sequential program runs on one core and gains nothing from the others; its speed is that core's IPC times the clock. The 0478 statement that cores "can affect performance" is true of a system with several things to do, and the exam expects that qualification.

## Exam Notes

### Cambridge 9618 (A Level), §4.1 and §15.1

§4.1 asks candidates to "show understanding of how factors contribute to the performance of the computer system", listing "processor type and number of cores, the bus width, clock speed, cache memory". Every one appears in this card with a measurement attached: the clock in the notation, cores in Misconception 5, cache in Part II's third experiment, and the missing factor, IPC, in Example 5. §15.1 asks for "the importance / use of pipelining and registers in RISC processors" and the four Flynn architectures, SISD, SIMD, MISD and MIMD; [[Pipelining and Simultaneous Multithreading]] and [[CISC vs RISC]] carry those rows, and this card's Part IV explains why RISC's many registers matter: renaming has more names to work with. Out-of-order execution, branch prediction, reorder buffers and register renaming are not named in the syllabus and are not examined.

### Cambridge 0478 (IGCSE), §3.1

Point 3: "understand what is meant by a core, cache and clock in a CPU and explain how they can affect the performance of a CPU". The expected answer is the qualitative one, and Misconception 5 states the qualification an examiner rewards. Nothing else here is examined.

### IB Computer Science (2027 guide), A1.1

A1.1.4 asks for cache levels and "the relevance of the terms cache miss and cache hit", which Part II's third experiment puts a number on; A1.1.5 is the fetch, decode and execute cycle; A1.1.6, HL only, is "the process of pipelining in multi-core architectures", with fetch, decode, execute and write-back stages and cores working "independently and in parallel". This card's engine is beyond the guide, and its Part I is the honest answer to a student who asks what the cycle looks like in silicon.

### Where this is *not* examined

AP Computer Science A examines Java, not hardware. No board examines out-of-order execution, register renaming or branch prediction, and no board asks a student to measure anything; this card is enrichment written because the measurements are cheap, repeatable on any laptop, and explain a factor of a hundred that the syllabus model has no room for.

## Beyond the syllabus

> [!info] The other axis: doing more per instruction
> Recall that the engine gains speed by finding independent instructions. Vector (SIMD) units gain it another way: one instruction adds eight or sixteen numbers at once. The floating-point experiment compiled at `-O2` would be vectorised as well as unrolled, and the eight-chain loop would become two instructions per iteration. [[The GPU — From Triangles to Tensors]] is that idea built into a whole processor.

> [!info] Simultaneous multithreading, seen from here
> Recall that the engine is often idle on a cache miss even with a full reorder buffer. SMT feeds the same execution units from two independent instruction streams, so that one thread's miss is the other thread's opportunity. Nothing about the engine changes; it simply has two ticket rails. The M1's cores do not do it and Intel's do, a design choice about whether the width is better spent on one thread's speculation or two threads' independence.

> [!info] Why 630 and not 6 300
> Recall that a wider window finds more independent work. It also costs more: every entry must be checked every cycle against every result, which grows with the square of the width, and power grows with it. A window of 630 at 3 GHz is roughly where that trade-off stood in 2020; the textbook window of one is where it stood in 1975, and the pipelines of the 1990s, at a dozen, were the step between.

## Connections

- **Built on:** [[CPU Architecture and the Fetch-Execute Cycle]] (the contract), [[Pipelining and Simultaneous Multithreading]] (the overlap this card measures and the names it uses), [[RAM and the Memory Hierarchy]] (the caches the third experiment prices).
- **Beside:** [[CISC vs RISC]] (why the engine decodes into micro-ops, and why renaming likes many registers), [[Interrupt Handling]] (precise exceptions are what in-order commit provides), [[The GPU — From Triangles to Tensors]] (the same three lessons taken to their limit).
- **The mathematics used:** [[Probability Basics]] (expected cost of a mispredict), [[Pipelining and Simultaneous Multithreading]]'s Little's-law bookkeeping for chains and units.
- **Story:** [[Dual-Core Craft]] (why game engines lay data out for the cache, and the end of the free lunch).

## Sources

- Hennessy, J. L., & Patterson, D. A. (2019). *Computer Architecture: A Quantitative Approach* (6th ed.). Morgan Kaufmann. Chapter 3: instruction-level parallelism, Tomasulo's algorithm, branch prediction, speculation.
- Tomasulo, R. M. (1967). An efficient algorithm for exploiting multiple arithmetic units. *IBM Journal of Research and Development*, 11, 25–33. Register renaming and dynamic scheduling, invented for the IBM 360/91.
- Smith, J. E., & Pleszkun, A. R. (1988). Implementing precise interrupts in pipelined processors. *IEEE Transactions on Computers*, 37, 562–573. The reorder buffer.
- Yeh, T.-Y., & Patt, Y. N. (1991). Two-level adaptive training branch prediction. *MICRO-24*, 51–61. Predictors that learn from history.
- Kocher, P., et al. (2019). Spectre attacks: exploiting speculative execution. *IEEE S&P 2019*; Lipp, M., et al. (2018). Meltdown. *USENIX Security 2018*.
- Frumusanu, A. (2020). Apple announces the Apple Silicon M1. *AnandTech*, 17 November 2020. The Firestorm core's decode width, reorder-buffer size and execution-unit counts quoted in Part I are from that analysis and from Johnson, D. (2021), *Apple M1 microarchitecture research* (dougallj.github.io).
- The measurements are from `modern-cpu-lab.c` compiled with Apple clang 21 at `-O1` on an Apple M1 Max (performance cores at $3.2$ GHz), run 2026-09-22; the simulator results are from `modern-cpu-simulator.py`, whose output is saved in `modern-cpu-simulator.json`.

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\text{IPC} = \dfrac{N_{\text{instructions}}}{N_{\text{cycles}}}$ | `\text{IPC} = \dfrac{N_{\text{instructions}}}{N_{\text{cycles}}}` | Instructions per cycle |
| $t = \dfrac{N}{\text{IPC} \times f}$ | `t = \dfrac{N}{\text{IPC} \times f}` | Run time from instruction count, IPC and clock $f$ |
| $\bar c = c_0 + p \times c_{\text{miss}}$ | `\bar c = c_0 + p \times c_{\text{miss}}` | Expected cycles per iteration with mispredict probability $p$ |
| chains $= L \times T$ | `\text{chains} = L \times T` | Independent chains needed: latency $\times$ throughput |
