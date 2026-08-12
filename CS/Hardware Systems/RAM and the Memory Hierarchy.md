---
chinese: 内存与存储层级 (nèicún yǔ cúnchǔ céngjí)
prerequisites:
  - "[[Logic Gates]]"
  - "[[Flip-Flops]]"
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
leads_to:
  - "[[Operating Systems]]"
  - "[[Secondary Storage]]"
  - "[[Arrays]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/IB-CS-A1-1
  - syllabus/0478-3-3
  - syllabus/0478-3-1
  - syllabus/9618-3-1
  - syllabus/9618-4-1
  - type/deep
  - misconception/ram-vs-storage
  - misconception/static-means-nonvolatile
  - misconception/random-means-stochastic
  - misconception/cache-is-buyable-ram
---

# RAM and the Memory Hierarchy 内存与存储层级

> *Memory has exactly one job: hold a bit steady until you ask for it back. There are two physical ways to do that job, and they are opposites — a tiny leaky bucket, or a small self-locking switch. One is cheap but forgetful; the other never forgets but costs six times the silicon. **Every layer of a computer's memory, from the registers in the core to the gigabytes of main memory, is one of those two cells — chosen by whether you needed it fast or needed it cheap.** The whole memory hierarchy is that single trade-off, stacked.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| RAM (random-access memory) | 随机存取存储器 / 内存 | working memory; any address reached in equal time |
| volatile | 易失性 | loses its contents when power is cut |
| DRAM (dynamic RAM) | 动态随机存取存储器 | 1 capacitor per bit; must be **refreshed** |
| capacitor | 电容 | stores a bit as a small electric charge |
| refresh | 刷新 | re-topping the leaking charge thousands of times a second |
| SRAM (static RAM) | 静态随机存取存储器 | 1 latch per bit; holds itself, no refresh |
| flip-flop / latch | 触发器 / 锁存器 | a circuit with two stable states — the unit of *remembering* |
| cache | 高速缓存 | small fast SRAM that keeps recently-used data near the CPU |
| memory hierarchy | 存储层级 | registers → cache → RAM → disk, fast-small to slow-large |

## What "RAM" actually means

**RAM** is the computer's *working memory*: the read/write store that holds the program currently running **and** the data it is working on (the [[CPU Architecture and the Fetch-Execute Cycle|stored-program]] idea — code and data live together in one memory). Two properties define it.

**Random access.** The "random" in RAM is *not* the everyday "random" (随机 as in *stochastic*). It means **arbitrary** — any address can be read or written in the same tiny time, with no winding to get there. Contrast the [[Turing Machine]]'s tape, where the head must shuffle cell-by-cell: that is *sequential* access. Real machines approximate a **random-access machine**, which is exactly why algorithm analysis can assume an array lookup `a[i]` costs $O(1)$ (see [[Big-O Notation]]).

> [!tip] Westworld — lose the timestamp, not the memory
> Random access reaches any cell directly, so an address says *where* a bit lives but nothing about *when* it was written — chronology is separate metadata (a timestamp, a pointer), never a property of the cell. That is the cleanest way to read the device driving *Westworld*'s second season: Bernard's memories are neither destroyed nor shuffled — he simply loses the **timestamps**, so every scene stays perfectly accessible yet refuses to fall into order, and neither he nor the viewer can tell past from present until the end. Wrecking the *index* ruins the story while the *data* sits untouched — deleting a book versus tearing the page numbers off an intact one. (Reassembling the order "by the end" is the slow, **sequential** opposite of random access: inferring the sequence from the contents themselves.)

**Volatile.** RAM forgets everything the instant power is cut (易失性). That is why a forced restart loses unsaved work, and why a computer needs *non-volatile* storage (an SSD, a hard disk, ROM for the boot firmware) to keep anything between power cycles. Volatility is not a flaw — it is the price of the speed and rewritability that make RAM useful while the machine is on.

> [!tip] Random Access Memories
> Daft Punk named their 2013 album *Random Access Memories* after exactly this. The pun does real work: the record reaches *directly* for scattered fragments of 1970s–80s music — disco, Giorgio Moroder, live session players — rather than looping a sampler; human memory as **random-access, not sequential tape**. Every time you jump straight to an address without winding there, you are doing what the title promises.

> [!warning] RAM is not "storage", and RAM is not ROM
> Everyday speech blurs three different things. **RAM** = fast, volatile, read/write working memory (gigabytes). **ROM** (read-only memory, 只读存储器) = non-volatile firmware the machine boots from. **Secondary storage** (SSD/HDD, 外存) = large, slow, non-volatile, where files live. "I have 16 GB of memory and 1 TB of storage" names the RAM and the disk — two completely different technologies. The focus below is RAM and the fast layers above it; the ROM family and the disks live at [[Secondary Storage]].

## The one job, two ways

A memory cell must store one bit and give it back on demand. The two physical answers are genuinely opposite, and almost everything else follows from the choice:

- **A leaky bucket** — store the bit as *charge on a capacitor*. Tiny and cheap, but it forgets in milliseconds. This is **DRAM**.
- **A self-locking switch** — store the bit as the *state of a latch* that feeds back on itself. Big and expensive, but it holds forever (while powered). This is **SRAM**.

Hold this pair in mind; the comparison at the end writes itself.

## DRAM — a bit is a drop of charge

A **DRAM** cell is the simplest memory humans build: **one transistor and one capacitor** (a *1T1C* cell). The **capacitor** holds the bit — charged ≈ 1, empty ≈ 0. The **transistor** is just a switch: when the cell's **word line** (row-select) goes high, the transistor connects the capacitor to the vertical **bit line** so it can be read or written.

![[dram-cell.svg|697]]

How a capacitor stores charge in the electric field between two plates — the relation $Q = CV$, and *why* the charge bleeds away — is the domain of electromagnetism ([[Capacitors]]). Here we need only one fact, and it is the fact that names the technology: **a charged capacitor slowly leaks.** A DRAM storage capacitor is fantastically small (a capacitance of *femtofarads*, $10^{-15}$ F), so the few electrons that hold a "1" drain away through tiny leakage currents in a matter of milliseconds — the charge decays exponentially, the same $V_0\,e^{-t/\tau}$ curve as [[Exponential Growth and Decay]].

That leak forces the defining behaviour: **refresh**.

![[dram-store-leak-refresh.svg|697]]

Left alone, every cell would slide below the **sense threshold** (the voltage that still reads as a "1") and the data would rot. So the memory controller **reads and rewrites every row thousands of times a second** — the industry standard, set by **JEDEC** (the Joint Electron Device Engineering Council), guarantees a full refresh at least every **~64 ms**. This is what *dynamic* means: the cell only stays alive because it is being **dynamically** topped up, like a bucket brigade endlessly refilling billions of leaking buckets. Refresh costs power and steals cycles when the CPU wants access — a real tax DRAM pays for being cheap.

**Reading, writing, and refreshing — how the cell tells 0 from 1.** This answers the natural question: *during refresh, how does the circuit know whether a cell held a 1 or a 0?* First the bit line is **precharged to exactly half the supply voltage** ($V_{DD}/2$) — parked on the fence between 0 and 1. Then the word line opens the transistor and the cell's capacitor **shares its charge** with the bit line: a stored 1 nudges the line a hair *up*, a stored 0 a hair *down*. The **sense amplifier** compares the line against that half-way reference, decides which way it moved, and drives it the rest of the way to a full 1 or full 0 — that decision *is* the read. And because the amplifier now holds the line at the full rail, it **rewrites the cell to full strength in the same motion** — so sensing the bit also restores it. That is why **reading DRAM is destructive** (charge-sharing drains the cell) yet self-healing (the sense amp refills it). **Writing** is the same machinery in reverse: drive the bit line hard to the value you want, open the word line, and the capacitor is filled or emptied to match. And **refresh** is just a read with the answer thrown away — every row is sensed and rewritten, thousands of times a second, purely to keep the charge above the fence.

![[dram-read-sense.svg|697]]

**The pay-off for all this trouble: density.** One transistor plus one capacitor is the smallest memory cell anyone knows how to make, so DRAM packs the most bits per square millimetre and the fewest dollars per gigabyte. That is precisely why **main memory is DRAM** — it is how you get *gigabytes* cheaply. The cost is latency: precharging long bit lines, sensing a femtofarad of charge, and dodging refresh all take time, so a random DRAM access is *slow* by CPU standards — hundreds of clock cycles (the "~200 ticks" the [[Pipelining and Simultaneous Multithreading|out-of-order core]] works so hard to hide).

## SRAM — a bit that holds itself

An **SRAM** cell throws density away to buy speed. It stores the bit not as charge but as the **state of a bistable latch**: typically **six transistors** (a *6T* cell) — two **inverters wired in a loop** (four transistors) plus two access transistors.

![[sram-cell.svg|697]]

The loop is the whole idea. Inverter A drives inverter B, and B drives A right back. Feed a "1" into the loop and A holds B holding A — the two inverters reinforce each other into a **stable state**. There are exactly **two** such self-consistent states (storing 0 and storing 1), and the cell sits in one of them, locked, **for as long as the power is on**. This is a **flip-flop** — the stateful element that plain [[Logic Gates|logic gates]] could not provide on their own (gates are *stateless*; the cross-coupled loop is what lets a circuit *remember*, the bridge into 9618's flip-flops, §15.2).

The two internal nodes are always **complementary** — never both the same — so the cell holds a value *and* its opposite. By the convention used in the diagrams here, the **right** node is $Q$ and the **left** node is $\bar{Q}$ ("NOT Q"): storing a **1** means $Q=1,\ \bar{Q}=0$; storing a **0** means $Q=0,\ \bar{Q}=1$. That built-in complement is exactly what lets both a read and a write act on **two** bit lines at once.

Because the bit is held by active feedback rather than a fading charge:

- **No refresh.** The cell holds itself — that is what *static* means (静态: stable while powered, in contrast to DRAM's need to be dynamically refreshed).
- **Non-destructive, fast reads.** Reading just senses the latch's output; nothing is emptied, nothing must be rewritten. Access is a handful of cycles, not hundreds.

**Reading and writing — and why writing is the clever part.** To **read**, both bit lines are precharged high, the word line opens the two access transistors, and whichever node holds **0** ($Q$ or $\bar{Q}$) tugs *its* bit line down; a sense amplifier spots which of the two dipped — the $Q$ side or the $\bar{Q}$ side — and that is the stored bit. To **write**, you cannot ask politely — you must **overpower the loop**. The bit-line drivers are built *stronger* than the cell's internal transistors, so when they force the two bit lines to the target values — the $Q$-side line to the new $Q$, the $\bar{Q}$-side line to its complement — and the word line opens, they win the tug-of-war, flip both internal nodes, and the feedback immediately **re-locks around the new state**. (The cell is deliberately sized so a read is too weak to disturb it but a write is strong enough to override it — the whole art of the 6T cell.)

![[sram-read-write.mp4]]

**Why SRAM is still volatile.** If it holds itself, why does cutting power lose the data? Because "holds itself" means *holds itself while energized*: the two inverters keep one node at the supply rail and the other at ground only by continuously **passing current** — the bit lives in a powered standoff, not in any permanent physical mark. Remove the power and there is no energy to sustain the feedback; both nodes sag to 0 V and the state evaporates. SRAM forgets the *instant* power drops (DRAM takes milliseconds) — but neither keeps anything without power, which is why every volatile layer needs a non-volatile one beneath it.

The cost is the mirror image of DRAM's: **six transistors per bit** instead of (effectively) one means SRAM is bulky, power-hungry, and *expensive* per bit — you get *megabytes*, not gigabytes. So SRAM is spent only where speed is worth the silicon: the **CPU registers** and the **cache**.

### The comparison writes itself

| | **DRAM** (dynamic) | **SRAM** (static) |
|---|---|---|
| stores a bit as | charge on a **capacitor** | state of a **flip-flop** (latch) |
| cell size | **1 transistor + 1 capacitor** | **~6 transistors** |
| refresh? | **yes** — every ~64 ms | **no** — holds itself |
| read | **destructive** (must rewrite) | non-destructive |
| speed | slow (hundreds of cycles) | **fast** (a few cycles) |
| density / cost per bit | **high density, cheap** | low density, expensive |
| volatile? | yes | yes |
| used for | **main memory** (GBs) | **cache + registers** (MBs) |

Both are volatile. The whole table is downstream of one decision — *capacitor or latch* — exactly as promised.

## The memory hierarchy — the trade-off, stacked

You cannot have memory that is big, fast, **and** cheap — the physics of the two cells forbids it. So computers refuse to choose: they stack many memories, each a different point on the trade-off, and let the fast-but-small layers stand in front of the big-but-slow ones.

The reason this works at all is **locality of reference** — the empirical fact that programs do not touch memory at random:

- **Temporal locality** — a byte used now is likely to be used again soon (a loop counter, a hot variable).
- **Spatial locality** — a byte used now means its *neighbours* are likely next (scanning an array, executing the next instruction).

[[Recursion]] already met this: a tight loop fits in cache and reuses the same cells (every access a *hit*), while pointer-chasing through scattered objects keeps *missing* and waiting on slow DRAM — the deep reason the packed-array ECS layout in [[Stories/Dual-Core Craft]] runs so much faster. Keep the small working set in fast SRAM and you get the **illusion of a memory as large as the disk and almost as fast as a register.**

![[memory-hierarchy.svg|697]]

| layer | technology | typical size | typical latency |
|---|---|---|---|
| registers | fastest SRAM, in the datapath | 16 × 64-bit GPRs + 16–32 vector regs (x86-64) | in-cycle |
| **L1 cache** (split I/D) | SRAM, per core | ~32–48 KB each | ~4–5 cycles (~1 ns) |
| **L2 cache** | SRAM, per core | ~256 KB–2 MB | ~12–15 cycles |
| **L3 cache** | SRAM, shared + sliced | ~8–64 MB | ~40+ cycles (varies) |
| **main memory** | **DRAM** | ~8–64 GB | ~70 ns (hundreds of cycles) |
| SSD | flash — [[Secondary Storage]] | ~1–4 TB | ~50 µs |
| HDD | magnetic | ~4 TB+ | ~5 ms |

Going **down**: bigger, cheaper per bit, slower. Going **up**: smaller, costlier per bit, faster — and the top three to four layers are SRAM, main memory is DRAM, and only the bottom two are non-volatile. When the CPU needs a byte it checks L1, then L2, then L3, then DRAM, stopping at the first **hit**; a **miss** falls to the next layer down. Because locality keeps the hit rate above ~95%, the *average* access feels nearly as fast as L1 even though most bytes live in slow DRAM. This whole tower — caches, prefetchers, out-of-order execution — exists to hide the **memory wall**: the widening gap between fast CPUs and slow DRAM (see [[Pipelining and Simultaneous Multithreading]]).

> [!info] Beyond syllabus — if it's all SRAM, what makes the levels different?
> Registers, L1, L2 and L3 are all **SRAM**, so the difference is *design point*, not technology.
> - **Registers** aren't addressed like memory — a few are named *directly in each instruction* (x86-64 exposes **16 general-purpose 64-bit registers**, plus **16–32 vector registers** for SIMD, plus control/debug registers). They are **multi-ported** (several read and written in one cycle), wired straight into the ALU, and built from the fastest, largest transistors — which is why there can only ever be a handful.
> - **L1** trades a little speed for capacity and is **split** into L1-I (instructions) and L1-D (data) — a modified-Harvard split ([[CPU Architecture and the Fetch-Execute Cycle]]) — reached by *address* through a tag lookup, private to one core.
> - **L2** is bigger and slightly slower, usually still per-core; **L3** is **shared** across all cores and physically **sliced** around the chip.
> - That slicing is why L2/L3 latency is a *range*, not a single number: on a many-core CPU, an SoC, or a chiplet design, the slice you need may sit far across the on-chip interconnect (a ring or mesh). A near slice is fast; a far one costs more — **non-uniform cache access (NUCA)**. The "~40 cycles" above is the near case.

> [!warning] Three traps
> **"Static" does not mean non-volatile.** SRAM holds its bit *only while powered* — both SRAM and DRAM lose everything at power-off. "Static" vs "dynamic" is purely about *needing refresh or not*, never about persistence.
> **Cache is not "extra RAM you can buy."** It is SRAM the hardware manages automatically and invisibly; programs cannot allocate it, and you cannot add it like a memory stick. Likewise, **more RAM is not automatically faster** — extra DRAM only helps if you were running out and paging to disk; beyond that it sits unused.
> **"Random" is not "stochastic."** Random access means *any address in equal time*, the opposite of sequential tape — nothing to do with randomness.

## Exam Notes

### Cambridge 0478 (IGCSE) — §3.3 primary storage, §3.1.3 cache

- State **RAM vs ROM** crisply: RAM is *volatile, read/write*, holds the programs/data **currently in use**; ROM is *non-volatile, read-only*, holds the start-up/boot instructions (firmware, e.g. the BIOS). "Volatile" = contents lost when power is off.
- Know **DRAM vs SRAM** and the differences the board asks for: DRAM uses **capacitors**, needs **constant refreshing**, is slower and cheaper, and is used for **main memory**; SRAM uses **flip-flops**, needs **no refreshing**, is faster and more expensive, and is used for **cache**. The 0478 cache point (§3.1.3) is exactly this: cache is fast SRAM between the CPU and RAM that holds frequently/recently used data so the CPU waits on slow RAM less often — more cache → fewer trips to RAM → better performance.
- **Virtual memory** (§3.3.4) — when RAM is full, the OS uses part of the *secondary storage* as if it were extra RAM, paging data in and out. It is slow (disk speeds) and is a *stopgap*, not real RAM — the full machinery (paging, replacement, thrashing) lives in [[Operating Systems]].

### Cambridge 9618 (A-Level) — §3.1 components, §4.1 cache, §15.2 flip-flops

- §3.1 / §4.1: explain how **cache** improves performance and how **more cache or a larger/faster RAM** affects a system. Use the hierarchy: registers → L1/L2/L3 cache (SRAM) → main memory (DRAM); the closer and faster the memory, the smaller and dearer it is. Tie performance to the **hit rate** and the cost of a **miss** to DRAM.
- §15.2 connection: the SRAM cell *is* a **flip-flop** (a bistable latch built from cross-coupled gates) — *why* such a circuit matters (it is how a computer remembers a bit) is the whole story above; the systematic treatment of **SR / JK / D-type** flip-flops belongs to sequential logic ([[Flip-Flops]]), simplified with the algebra and maps of [[Boolean Algebra]] and [[Karnaugh Maps]].

### IB Computer Science — A1.1 Computer hardware and operation

Memory sits inside A1.1 (computer fundamentals): the RAM/ROM distinction, cache, and the memory hierarchy are core vocabulary for explaining CPU performance, and the RAM-vs-storage distinction recurs whenever A1.1 asks what happens to data at power-off. The 9618-style mechanism language above (capacitor + refresh for DRAM, flip-flop for SRAM) is beyond what IB requires but is exactly the kind of justified explanation its extended responses reward.

> [!info] Beyond syllabus — why these cells are the way they are
> The capacitor's $Q = CV$ and its $RC$ leak (full story in [[Capacitors]]); the **sense amplifier** that resolves a femtofarad of charge into a clean 0/1; the **6T** SRAM cell as two inverters in positive feedback (the simplest bistable element); the **memory wall** and why the entire cache hierarchy is a workaround for it. None of this is examined, but it is the *reason* the exam facts are true — and it is where the bridge to electromagnetism ([[Capacitors]]) and to digital logic ([[Logic Gates]] → flip-flops) actually lives.

## Connections

- **Prerequisites:** [[Logic Gates]] — stateless gates, and the cross-coupled loop that becomes the SRAM flip-flop; [[CPU Architecture and the Fetch-Execute Cycle]] — the registers/RAM/buses this memory feeds.
- **Two cells:** [[Capacitors]] — the DRAM bit (electromagnetism); the flip-flop / bistable latch of [[Logic Gates]] — the SRAM bit.
- **Built on / contrasts:** [[Turing Machine]] — sequential tape vs random access; [[Big-O Notation]] — why $O(1)$ array access assumes a random-access machine; [[Exponential Growth and Decay]] — the $V_0 e^{-t/\tau}$ leak that forces refresh.
- **Application:** [[Pipelining and Simultaneous Multithreading]] — the memory wall and how out-of-order execution hides DRAM latency; [[Recursion]] — cache locality of loops vs scattered calls; [[Stories/Dual-Core Craft]] — cache-friendly ECS data layout.
- **Leads to:** [[Arrays]] — the software convention laid over this flat sea of numbered cells: $\text{base} + i \times \text{size}$ turns random access into indexing, and row-major layout turns locality of reference into measurable speed; [[Operating Systems]] — its virtual-memory machinery extending the hierarchy onto the disk (paging) when DRAM runs out; [[Secondary Storage]] — the non-volatile layers beneath (HDD, flash, optical, and the ROM family), where the sense-amplifier's analog-to-bit decision reappears on every medium; [[How a Chip Is Made]] — how these transistors and capacitors are etched into silicon.

## Glossary

| term | 中文 | meaning |
|---|---|---|
| volatile | 易失性 | loses contents when power is removed |
| refresh | 刷新 | periodic read-and-rewrite that restores leaking DRAM charge |
| sense amplifier | 灵敏放大器 | circuit that resolves a tiny bit-line voltage into a clean 0/1 |
| bistable latch | 双稳态锁存器 | circuit with two self-holding stable states — stores one bit |
| locality of reference | 引用局部性 | programs reuse recent data (temporal) and nearby data (spatial) |
| cache hit / miss | 命中 / 未命中 | data found / not found in a given cache level |

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $Q = CV$ | `Q = CV` | charge stored on a capacitor (full treatment in [[Capacitors]]) |
| $\tau = RC$ | `\tau = RC` | time constant; sets how fast the DRAM cell leaks |
| $V_0\,e^{-t/\tau}$ | `V_0\,e^{-t/\tau}` | exponential decay of the stored charge between refreshes |
| $10^{-15}\,\text{F}$ | `10^{-15}\,\text{F}` | femtofarad — order of a DRAM storage capacitor |
| $O(1)$ | `O(1)` | constant-time access — the random-access assumption |
