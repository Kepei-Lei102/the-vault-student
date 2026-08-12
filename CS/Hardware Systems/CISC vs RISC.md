---
chinese: 复杂指令集与精简指令集 (fùzá zhǐlìngjí yǔ jīngjiǎn zhǐlìngjí)
prerequisites:
  - "[[Assembly Language]]"
  - "[[Pipelining and Simultaneous Multithreading]]"
  - "[[Interrupt Handling]]"
leads_to:
  - "[[Compilers and Interpreters]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/A-Level
  - curriculum/Cambridge-9618
  - syllabus/9618-15-1
  - type/deep
  - misconception/reduced-means-weak
  - misconception/x86-runs-cisc-inside
  - misconception/reduced-means-few-instructions
  - misconception/one-side-won
---

# CISC vs RISC 复杂指令集与精简指令集

> *[[Assembly Language]] ended on a quiet bombshell: every processor family speaks its own language. This card is about the war over what those languages should be — the longest-running design argument in computing. One camp said an instruction should be a **sentence**: let `MULT` fetch both numbers from memory, multiply them, and store the result, all in one majestic command. The other said an instruction should be a **syllable**: do one small thing, in one tick, every time, and let the compiler stack syllables. The sentence-camp built the chips your desktop still runs; the syllable-camp built the chip in your phone, your earbuds, and the ¥2 microcontroller from [[Embedded Systems]]. And the ending nobody predicted: **the hardware quietly converged** — today's "CISC" processor is a RISC engine wearing a CISC costume, and the instruction set turns out to be a contract, not a blueprint.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| instruction set architecture (ISA) | 指令集架构 | the contract between software and silicon: which instructions exist, and what they promise |
| CISC (Complex Instruction Set Computer) | 复杂指令集计算机 | few-but-mighty: rich, variable-length instructions that may each take many cycles |
| RISC (Reduced Instruction Set Computer) | 精简指令集计算机 | simple-and-fast: fixed-length instructions aiming at one cycle each |
| load/store architecture | 加载/存储架构 | RISC's discipline: only load and store touch memory; everything else works in registers |
| microcode | 微码 | CISC's secret: a tiny interpreter inside the CPU that unrolls big instructions into small steps |
| micro-ops (μops) | 微操作 | what a modern x86 decoder slices its CISC instructions into — RISC-like internally |
| fixed-length instruction | 定长指令 | every instruction the same size — the pipeline's favourite food |
| general-purpose registers | 通用寄存器 | RISC's large working set (16–32+), vs classic CISC's handful |
| backward compatibility | 向后兼容 | the reason x86 still honours instructions designed in 1978 |

## Two philosophies of the dictionary

The disagreement is older than both acronyms, and it is really about **who does the work** — hardware or compiler:

| | **CISC** (x86 lineage, 1970s) | **RISC** (ARM, MIPS, RISC-V, 1980s) |
|---|---|---|
| An instruction is… | a *sentence* — may load from memory, compute, and store, all in one | a *syllable* — one small action, registers only |
| Length | **variable** (1–15 bytes on x86) | **fixed** (typically 4 bytes) |
| Cycles per instruction | often many | aiming at **one** |
| Memory access | many instructions may touch memory | **load/store only** — everything else register-to-register |
| Registers | few (the 8086 had 8, most with special jobs) | many (16–32+, general-purpose) |
| Decoding | complex, via a **microcode** layer | simple, hardwired |
| Code size | dense — fewer, fatter instructions | larger — more, thinner instructions |
| Who's clever? | the **hardware** (rich instructions close the "semantic gap") | the **compiler** (stacks simple instructions well) |

Both philosophies were *right for their decade*. CISC was born when memory cost gold and humans wrote assembly by hand — so instructions were made dense and expressive, one line doing the work of four. RISC was born (Berkeley and Stanford, early 1980s) from a data-driven observation: **compilers had taken over the writing**, and when researchers measured real programs, the complex instructions were barely used — compilers emitted the simple ones almost exclusively. So why spend silicon decoding grandeur nobody used? Strip the set to what compilers actually emit, make every instruction the same shape, and spend the freed silicon on **registers and pipeline**.

![[cisc-risc-philosophies.svg|697]]

## Why pipelines love RISC — the named connection

Recall the assembly line of [[Pipelining and Simultaneous Multithreading]]: fetch, decode, execute, write-back all running simultaneously on *different* instructions. That factory has two requirements that read like RISC's design sheet:

- **You must know where the next instruction starts before decoding the current one.** Fixed-length instructions make the next fetch address pure arithmetic (PC + 4); variable-length CISC makes it a puzzle — you cannot even *find* instruction boundaries until you have partly decoded, which strangles a wide fetch.
- **Stages must take equal, short times.** Single-cycle register-to-register instructions march in lockstep; one 40-cycle memory-to-memory monster is a truck parked on the assembly line — everything behind it bubbles.

And here is the race, run live — same clock, same stages, one fat MULT parking in EXECUTE:

![[cisc-risc-pipeline.mp4]]

That is why the syllabus pairs "pipelining and registers" with RISC by name: the many registers are what *let* every instruction be register-to-register (load/store discipline), and the uniform instructions are what let the pipeline stay full. RISC was never "reduced" for simplicity's own sake — it was **shaped for the pipeline**.

## Interrupt handling on the two — the trade nobody mentions first

[[Interrupt Handling]]'s golden rule was *finish the current instruction, then answer the door*. Now notice what that rule costs on each side:

- **On RISC, the rule is cheap.** Every instruction finishes in a cycle or so — the doorbell never waits long, and the scene to protect is small and uniform. Interrupt latency is short and, crucially, *predictable* — one reason RISC cores own the [[Embedded Systems]] world, where the airbag's deadline is the whole point.
- **On CISC, the rule bites.** What if the interrupt arrives mid-way through one grand instruction — a string-copy moving thousands of bytes? Waiting for it to finish could take thousands of cycles: unacceptable latency. So CISC processors must make long instructions **interruptible and resumable** — pausing partway, saving *extra internal state* (how far did the copy get?), and restarting cleanly afterwards. It works, but the interrupt machinery grows complicated exactly in proportion to the instructions' grandeur.

One sentence for the exam: *RISC finishes the short current instruction and responds quickly with a small saved state; CISC must either tolerate longer latency or support interrupting partially-completed instructions, saving additional state.*

## The plot twist: convergence

The war's ending is the best part. In the mid-1990s, x86 — the definitive CISC — faced a choice: keep the instruction set (a mountain of the world's software stood on it) or keep up with RISC pipelines. Intel's answer (Pentium Pro, 1995) was both: **keep the CISC contract outside, build a RISC engine inside.** A decoder at the front of the chip slices each fat x86 instruction into small, uniform **micro-ops**, which then flow through exactly the kind of wide, register-rich, pipelined core RISC pioneered. (A RISC front end has a decoder too — turning instruction bits into control signals is universal — but it is a thin, hardwired mapping. The x86 decoder must *translate* first — sentence into syllables — and only then do the ordinary bit-to-signals wiring.) Meanwhile ARM, the definitive RISC, grew multimedia extensions and denser encodings when markets demanded them.

Say the trade out loud, because it is the whole point. The **reward is compatibility**: every binary compiled since 1978 kept running, unmodified, on each new chip — and that mountain of working software is the moat no rival ISA has crossed on the desktop. The **price is the translating decoder**, and the bill arrives in **watts**.

![[cisc-risc-classroom-comic.png|697]]

![[cisc-risc-convergence.svg|697]]

So the honest modern statement is: **the ISA is a compatibility contract, not an engine blueprint.** Under the hood, everyone converged on the same wide, out-of-order, deeply pipelined machine. What still differs — and still matters — is the *cost of the contract*: x86's variable-length decode is a permanent tax — finding instruction boundaries burns power and limits decoder width — and it is a real part of why x86 never made it into your pocket, and why only Intel's newest manufacturing generations (the 18A-process chips of 2025–26) have finally pulled x86's battery appetite close to territory ARM laptops had held for years. Fixed-length RISC, by contrast, lets a designer bolt on very wide decoders almost for free — one enabler of Apple's M-series performance-per-watt. The war didn't end with a winner; it ended with **niches**: the legacy-software mountain runs on x86, and everything battery-powered — phones, earbuds, the ¥2 MCU, most of the world's processors by count — runs RISC.

## Worked example — the §15.1 three-parter

> *(a) State **three** differences between RISC and CISC processors. [3]*
> *(b) Explain why **pipelining** is more effective in RISC processors. [3]*
> *(c) Describe **one** difference in how interrupts are handled on RISC and CISC processors. [2]*

*Tool for (a): the philosophy table — pick contrasting pairs, state both sides.*
RISC has fewer, simpler instructions; CISC has many complex ones ✓. RISC instructions are fixed-length and aim at one cycle; CISC instructions vary in length and may take many cycles ✓. RISC is load/store (only dedicated instructions touch memory, using many registers); CISC instructions may operate on memory directly (fewer registers) ✓.

*Tool for (b): the two pipeline requirements — boundaries and lockstep.*
Fixed-length instructions mean the processor always knows where the next instruction begins, so fetching and decoding overlap cleanly ✓; single-cycle instructions keep every stage busy in lockstep, avoiding stalls ✓; multi-cycle CISC instructions of unpredictable length cause pipeline bubbles and complicate decoding ✓.

*Tool for (c): finish-the-current-instruction, priced on each side.*
A RISC processor simply completes the (short) current instruction, so interrupt latency is small and the saved state uniform ✓; a CISC processor may be mid-way through a long instruction and must either wait or interrupt it partway, saving additional internal state so it can resume ✓.

## Misconceptions

> [!warning] "Reduced means weaker."
> RISC machines compute everything CISC machines do — the *programs* are computationally identical ([[Turing Machine]] guarantees it). "Reduced" prices the *instructions*, not the machine: each does less, so the machine can do each faster, and the compiler composes them. The fastest supercomputers and every phone flagship are RISC.

> [!warning] "Reduced means a short instruction list."
> Modern ARM has hundreds of instructions. What is reduced is the **complexity per instruction** — fixed length, register-to-register, one memory idea (load/store), pipeline-friendly timing. RISC is a discipline, not a diet.

> [!warning] "x86 is still CISC inside."
> Only the *contract* is CISC. Since the mid-1990s the silicon decodes each x86 instruction into RISC-like micro-ops and runs them on a wide pipelined core — a RISC engine in a CISC trench coat. What CISC costs today is the *decoder*, not the execution engine.

> [!warning] "One side won."
> Neither, and both: the philosophies converged in the engine room and split the world by niche — legacy software on x86, batteries on ARM/RISC-V. The exam wants the classical differences; the honest footnote is that they describe *contracts and costs*, not two different kinds of engine.

## Exam Notes

### Cambridge 9618 A-Level — §15.1 (the processor half)

- **The LO bullets verbatim:** differences between RISC and CISC (the philosophy table — quote contrasting *pairs*); **interrupt handling on CISC and RISC processors** (the finish-the-instruction trade above — this is the bullet [[Interrupt Handling]] reserved for this card); the **importance of pipelining and registers in RISC** (the two pipeline requirements + load/store needing a large register file).
- §15.1's other residents live elsewhere: the four architectures **SISD/SIMD/MISD/MIMD** and massively parallel computing are in [[Pipelining and Simultaneous Multithreading]]; **virtual machines** remain the row's open item.
- Mark-scheme habit: answer in *pairs* ("RISC does X **whereas** CISC does Y") — single-sided statements often earn nothing.

### Other boards

- **Cambridge 0478:** not examined — IGCSE stops at machine code and the assembler ([[Assembly Language]] §3.1.4 note).
- **IB CS / AP CSA:** not named in either; enrichment for the student who asks why their phone chip and laptop chip disagree.

## Beyond the syllabus

> [!info] The semantic gap, and the instruction that evaluated polynomials
> CISC's high-water mark: DEC's VAX (1977) shipped `POLY` — one instruction that evaluated an entire polynomial — plus instructions for queue insertion and string editing, all in the name of closing the "semantic gap" between assembly and high-level languages. The RISC researchers' measurement was brutal: compilers almost never emitted them, and `POLY` could even be *slower* than the equivalent simple-instruction loop. A design lesson the vault generalises happily: **build for measured behaviour, not imagined elegance.**

> [!info] Microcode: the interpreter hiding in the hardware
> How does a CISC chip run a grand instruction? Recall the control unit from [[CPU Architecture and the Fetch-Execute Cycle]] — in classic CISC, that control unit is itself a tiny stored program: each big instruction triggers a sequence of **microcode** steps from an internal ROM. There is, in other words, an *interpreter inside the CPU* — and patchable microcode is how vendors ship fixes for hardware bugs (the Meltdown/Spectre era made "microcode update" household vocabulary). RISC's hardwired decode removed the interpreter; x86's μop decoder brought it back in modern dress.

> [!info] RISC-V: the contract goes open-source
> The newest chapter: RISC-V (Berkeley again, 2010s) is a RISC ISA that is *free* — no licence to implement it. The contract insight made explicit: if the ISA is just an interface, it can be a public standard, and anyone may build the engine. It is already the default teaching ISA and a rising embedded force — the closest computing has to a constitution written in public.

## Connections

- **Builds on:** [[Assembly Language]] — the instructions whose very shape this war contested, and the one-per-ISA fact it explains; [[Pipelining and Simultaneous Multithreading]] — the machinery RISC was shaped to feed, and the shared home of §15.1's Flynn taxonomy.
- **Leads to:** [[Compilers and Interpreters]] — RISC's founding bet was that compilers, not humans, write the assembly; the translator that made "reduced" viable deserves its own card.
- **Kindred:** [[Interrupt Handling]] — the finish-the-instruction rule this card prices on both architectures; [[Embedded Systems]] — where RISC's predictable latency and battery thrift rule, and the ARM SoC blurring the boundary; [[Turing Machine]] — why the two camps compute exactly the same set of things, however they phrase it.
