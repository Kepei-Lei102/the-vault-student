---
chinese: 汇编语言 (huìbiān yǔyán)
prerequisites:
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Number Bases]]"
  - "[[Bitwise Operations]]"
leads_to:
  - "[[CISC vs RISC]]"
  - "[[Compilers and Interpreters]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-3-1
  - syllabus/0478-4-2-1
  - syllabus/9618-4-2
  - syllabus/9618-4-3
  - syllabus/9618-20-1
  - type/deep
  - misconception/cpu-reads-mnemonics
  - misconception/assembly-is-compiled
  - misconception/one-assembly-language
  - misconception/assembly-is-always-faster
---

# Assembly Language 汇编语言

> *Your computer has never run a single line of Python. Not one. It has never run C, or Java, or anything a human has ever shown you. Everything you have ever written was, before it ran, quietly converted into the only language the machine has ever spoken — patterns of bits, fetched and executed by the cycle you already know. **Assembly language is that language with names on**: one human-readable line per machine instruction, one-to-one, nothing hidden. It is the last floor of the software tower where you can still see every register move — the CPU with the case off. This card teaches you to read it, trace it, and translate it — and to meet the small, honest program that does the translating.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| machine code | 机器码 | the raw numeric instructions the CPU fetches and executes — the only language it runs |
| assembly language | 汇编语言 | machine code with mnemonic names — **one line per instruction, one-to-one** |
| mnemonic | 助记符 | the human-readable opcode name: `LDD`, `ADD`, `JMP` |
| opcode / operand | 操作码 / 操作数 | *what to do* / *what to do it to* — the two halves of every instruction |
| assembler | 汇编器 | the translator from mnemonics to machine code — the simplest translator there is |
| two-pass assembler | 两遍汇编器 | reads the source twice: pass 1 collects labels, pass 2 emits code |
| symbol table | 符号表 | pass 1's product: each label and the address it stands for |
| label | 标号 | a name for an address, so jumps say `JMP LOOP` instead of `JMP 107` |
| addressing mode | 寻址方式 | *how* the operand names its data: the value itself, an address, an address-of-an-address… |
| immediate / direct / indirect / indexed | 立即 / 直接 / 间接 / 变址寻址 | the four "where is it?" answers, one indirection at a time |
| trace table | 跟踪表 | the exam's X-ray: registers and memory, written down after every instruction |

## The one language — and its costume

Recall from [[CPU Architecture and the Fetch-Execute Cycle]] that an instruction is a number: some bits of **opcode** (*what to do*) and some bits of **operand** (*what to do it to*), fetched into the CIR and decoded by the control unit. A real program in memory looks like this:

```
0x1E04   0x2105   0x0A06 …
```

Nobody can write that; nobody can debug it. So the earliest programmers did the obvious human thing: they gave each opcode a *name* — a **mnemonic** — and wrote `LDD 4` instead of `0x1E04`. That naming layer is assembly language, and the deep fact about it is the **one-to-one rule**: each assembly line *is* one machine instruction, renamed. Nothing is added, optimised, or restructured on the way down. This is exactly what makes assembly different from a high-level language: a single Python line may become hundreds of machine instructions chosen by a compiler ([[Compilers and Interpreters]] tells that story); an assembly line becomes precisely one, chosen by you.

![[asm-tower.svg|697]]

That one-to-one honesty is why assembly still matters even in a Python world: it is the last language in which **you can see everything the machine does** — every register, every memory touch, every jump. Reading it is reading the CPU's diary.

## The Cambridge machine — registers and instruction set

Cambridge examines a clean teaching machine: an **ACC** (accumulator — the working register everything passes through) and an **IX** (index register — a pointer for walking arrays), plus the PC and friends from the FDE card. Its instruction set is small enough to learn whole, and the syllabus explicitly wants it **grouped** — the groups are half the marks:

| Group | Instructions | What they do |
|---|---|---|
| **Data movement** | `LDM #n` · `LDD <addr>` · `LDI <addr>` · `LDX <addr>` · `LDR #n` · `MOV <reg>` · `STO <addr>` | load the ACC (four different ways — see addressing modes), load the IX, copy ACC↔IX, store ACC to memory |
| **Input / output** | `IN` · `OUT` | read one character into ACC; write ACC as one character |
| **Arithmetic** | `ADD <addr>` / `ADD #n` · `SUB <addr>` / `SUB #n` · `INC <reg>` · `DEC <reg>` | add/subtract into ACC; nudge ACC or IX by one |
| **Compare** | `CMP <addr>` / `CMP #n` · `CMI <addr>` | compare ACC with a value — sets a flag, changes nothing else |
| **Conditional / unconditional jumps** | `JMP <addr>` · `JPE <addr>` · `JPN <addr>` | go there always / if the comparison matched / if it didn't |
| **Bit manipulation** | `AND` · `OR` · `XOR` (`#n` or `<addr>`) · `LSL #n` · `LSR #n` | the [[Bitwise Operations]] toolkit, applied to the ACC — masking and shifting on register contents |
| **Control** | `END` | return control to the operating system |

Two habits to wire in now: **`CMP` does nothing visible** — it only sets a flag that the next `JPE`/`JPN` reads (the pair is a single thought split across two instructions); and **`#` always means "the number itself"** — its absence always means "an address."

## Addressing modes — five answers to "where is it?"

The same `LD` idea comes in several costumes, and the difference between them is the single most examined idea in §4.2. Each mode adds **one more level of indirection** — one more hop before you reach the data:

![[asm-addressing-modes.svg|697]]

- **Immediate — `LDM #5`:** the operand *is* the data. ACC ← 5. Zero hops.
- **Direct — `LDD 5`:** the operand is an *address*. ACC ← contents of cell 5. One hop.
- **Indirect — `LDI 5`:** the operand is the address *of the address*. Read cell 5, treat what you find as the real address, load from there. Two hops — this is a pointer, met in the wild.
- **Indexed — `LDX 5`:** ACC ← contents of (5 + IX). The base address plus a movable offset — set `IX` to 0, 1, 2… and `LDX BASE` walks an array without rewriting the program. (This is what the IX register is *for*.)
- **Relative:** the operand is an offset from *here* (the current PC) rather than from address zero — `JMP +3` means "skip three ahead." It makes code **relocatable**: the block still works wherever the OS loads it.

*Tool for every modes question: count the hops.* "Immediate" is zero, "direct" is one, "indirect" is two, "indexed" is one-hop-plus-IX — say the hop count and the examiner's mark scheme lights up.

## Worked trace 1 — three instructions, no surprises

> *Trace the program. Memory before: cell 20 holds 7, cell 21 holds 5.*
> ```
> 10  LDD 20      ; ACC ← contents of 20
> 11  ADD 21      ; ACC ← ACC + contents of 21
> 12  STO 22      ; cell 22 ← ACC
> 13  END
> ```

*Tool: the trace table — one row per instruction, write only what changed.*

| after | ACC | cell 20 | cell 21 | cell 22 |
|---|---|---|---|---|
| `LDD 20` | **7** | 7 | 5 | – |
| `ADD 21` | **12** | 7 | 5 | – |
| `STO 22` | 12 | 7 | 5 | **12** |

Three rows, one addition, and the discipline that matters: **a cell keeps its value until an instruction writes it** — `LDD` copies, it does not move.

## Worked trace 2 — the loop, where marks are won and lost

> *Trace the program and state the output. `NUM` is cell 200 holding 3; `COUNT` is cell 201.*
> ```
>        LDM  #0        ; ACC ← 0
>        STO  201       ; COUNT ← 0
> LOOP:  LDD  201       ; ACC ← COUNT
>        INC  ACC       ; ACC ← ACC + 1
>        STO  201       ; COUNT ← ACC
>        LDD  201
>        CMP  200       ; compare COUNT with NUM (3)
>        JPN  LOOP      ; not equal? go round again
>        OUT            ; (with 51 in ACC this prints '3')
>        END
> ```

*Tool: trace the loop round by round — never "see the pattern and skip ahead"; the mark scheme pays per row.*

| round | ACC after `INC` | COUNT (cell 201) | `CMP 200` | `JPN LOOP`? |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 ≠ 3 | jump — again |
| 2 | 2 | 2 | 2 ≠ 3 | jump — again |
| 3 | 3 | 3 | 3 = 3 | no jump — fall through |

And the whole loop, traced live — highlight, registers and memory moving together:

![[asm-trace.mp4]]

The loop exits with COUNT = 3, and the two instincts this rehearses are exactly the examined ones: the **`CMP`/`JPN` pair** is one decision in two lines, and the **label** `LOOP:` is nothing mystical — it is a name for an address, which is the perfect bridge to what the assembler actually does.

## The assembler — and why it must read your program twice

The assembler's job sounds trivial: swap each mnemonic for its opcode number, each label for its address — a dictionary lookup per line. And it *would* be one pass, except for one wrinkle your own loop just created:

```
       JPE  DONE     ; ← what number is DONE? No idea yet —
       …             ;    it's defined three lines LATER.
DONE:  END
```

A **forward reference**: the program uses a name before defining it. Reading top-to-bottom once, the assembler meets `JPE DONE` while `DONE` is still meaningless — it cannot emit the instruction. The fix is the **two-pass assembler**, and both passes are named marks:

![[asm-two-pass.svg|697]]

- **Pass 1 — read everything, translate nothing.** Walk the source keeping a running address counter; every time a label is *defined* (`LOOP:`, `DONE:`), record **label → address** in the **symbol table**. Ignore what instructions mean; just count where they will sit.
- **Pass 2 — translate everything, using the table.** Walk the source again, now emitting machine code: mnemonics become opcodes via the (fixed) opcode table, labels become addresses via the symbol table built in pass 1. `JPE DONE` assembles cleanly because `DONE` is now a known number.

The exam's favourite exercise is *being* the assembler: given a short program, produce the symbol table (pass 1) and then the machine code with addresses substituted (pass 2). Its favourite question about the exercise: **why two passes?** — and the answer is the forward reference, in one sentence.

## Misconceptions

> [!warning] "The CPU reads the mnemonics."
> The CPU has never seen a letter of assembly in its life — it fetches *numbers*. `LDD` exists for you; by run time the assembler has replaced every trace of it. If you remember one image: assembly is the label on the box, machine code is what's in the box, and the CPU only ever opens boxes.

> [!warning] "The assembler is a compiler."
> Both translate, but the **ratio** is the whole difference: an assembler maps one line to one instruction — no choices, no optimisation, a renaming. A compiler maps one line to *however many instructions it decides* — it designs machine code; an assembler transcribes it. (That design story is [[Compilers and Interpreters]].)

> [!warning] "Assembly language — singular."
> Every processor family has its own: x86's, ARM's, RISC-V's, and Cambridge's little teaching machine each speak differently, because assembly names *that CPU's* instruction set. Learning one teaches you the *shape* of all of them — registers, modes, jumps — but the words don't transfer. (Why the instruction sets themselves differ so much is [[CISC vs RISC]].)

> [!warning] "Hand-written assembly is always fastest."
> Fifty years ago, yes. Today an optimising compiler beats nearly all humans nearly all the time — it never tires, tracks forty registers at once, and knows pipeline tricks ([[Pipelining and Simultaneous Multithreading]]) no one can juggle by hand. Humans still hand-write the exceptional slivers: cryptographic routines that must run in constant time, SIMD hot loops, the first boot instructions of an OS, and interrupt handlers on tiny [[Embedded Systems]]. Everything else: trust the compiler, and *read* its assembly when you must know the truth.

## Exam Notes

### Cambridge 9618 A-Level — §4.2 (+ §4.3 in register form)

- **The LO list verbatim:** the assembly↔machine-code relationship (one-to-one); the **two-pass assembler** — describe the stages *and* apply them to a given program (symbol table, then substitution); **trace** a given program; know the instruction **groups** (data movement, I/O, arithmetic, unconditional/conditional jumps, compare); use the **addressing modes** (immediate, direct, indirect, indexed, relative).
- **Where marks live:** trace tables (one row per instruction, only changed cells; loops traced round by round); the `CMP`→`JPE`/`JPN` flag relationship; `#` vs no-`#`; hop-counting the modes (`LDD` vs `LDI` is the classic discriminator); and the forward-reference sentence answering "why two passes?"
- **§4.3 lands here in practice:** `AND`/`OR`/`XOR`/`LSL`/`LSR` **on register contents** — masking a bit flag, shifting for ×2 — with the full mechanics (and the rotate-vs-shift distinction §4.3 names as cyclic shifts) in [[Bitwise Operations]].

### Cambridge 0478 IGCSE — §3.1.4

- Concept depth only: machine code and assembly as **low-level languages**, the mnemonic idea (`LDA`, `ADD`, `STO` as readable stand-ins), and that an **assembler** translates to machine code. No tracing, no modes, no two-pass machinery — those are the A-Level's. One reliable mark: assembly is *specific to the processor*; high-level languages are portable.

### IB / AP

- **IB CS:** not examined — the 2027 course's programming strand is high-level (Java/Python) throughout; A1.2's "processing" stays at gates. This card is enrichment for IB students who ask what the JVM stands on.
- **AP CSA:** not examined (Java only). The mental model transfers anyway: the JVM's bytecode is exactly this idea one floor up.

## Beyond the syllabus

> [!info] Real assembly, one glance
> Cambridge's machine is invented, but the shape is universal. The same add-two-numbers in x86 (`mov eax, [a]` / `add eax, [b]` / `mov [c], eax`) and ARM (`LDR R0, a` / `LDR R1, b` / `ADD R0, R0, R1` / `STR R0, c`) is recognisably the same three thoughts — load, add, store — with different accents. The tool the whole industry uses to *read* compiler output is Compiler Explorer ("godbolt"): type C on the left, watch the assembly appear on the right, and see precisely what your abstractions cost. It is the FDE card's promise made interactive.

> [!info] The games were written here
> Recall the NES line from [[Interrupt Handling]]: *Super Mario Bros.* ran inside the screen-refresh interrupt — and all of it, every jump and Goomba, was **hand-written 6502 assembly**, roughly forty kilobytes of it. RollerCoaster Tycoon (1999) was written almost entirely in x86 assembly by one person. The entire Apollo Guidance Computer flew on hand-assembled code whose printed listings, stacked, stood taller than Margaret Hamilton — the famous photograph is of *assembly language*. For decades, "programmer" simply meant this.

> [!info] Assembly as X-ray, not as pen
> The modern reason to read assembly is diagnostic: performance engineers read compiler output to find the loop that didn't vectorise; security researchers read it because *attackers* do (malware ships as machine code — disassembly is how defenders read it back); and embedded developers still count cycles in ISRs where a microsecond is the budget. Writing assembly is now a specialty; **reading** it is the retained superpower — the ability to open the box and check what the machine was actually told.

## Connections

- **Builds on:** [[CPU Architecture and the Fetch-Execute Cycle]] — the registers and cycle every instruction here drives; instructions-as-numbers is that card's opcode/operand story, completed; [[Number Bases]] — hex as machine code's native costume; [[Bitwise Operations]] — the AND/OR/XOR/shift instructions' full mechanics.
- **Leads to:** [[CISC vs RISC]] — why instruction sets themselves disagree, and the war over what an instruction should be; [[Compilers and Interpreters]] — the translators that *design* machine code instead of transcribing it, where the one-to-one rule breaks and the interesting choices begin.
- **Kindred:** [[Embedded Systems]] — where hand-written assembly still earns its keep (boot code, tight ISRs); [[Interrupt Handling]] — the return-from-interrupt and state-saving this card's instructions implement; [[Von Neumann machine]] — code-as-numbers is the stored-program idea, and assembly is its human handle.
