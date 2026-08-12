---
chinese: 冯·诺依曼机 (Féng·Nuòyīmàn jī)
prerequisites:
  - "[[Turing Machine]]"
leads_to:
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[The Feynman Technique]]"
  - "[[von Neumann the Martian]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/IGCSE
  - level/A-Level
  - level/university
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-3-1
  - syllabus/9618-4-1
  - type/deep
  - type/concept
  - misconception/von-neumann-invented-it-alone
  - misconception/stored-program-needs-rom
  - misconception/von-neumann-vs-harvard-is-historical
---

# Von Neumann machine 冯·诺依曼机

> *Before 1945, "reprogramming" a computer meant rewiring it — unplugging cables and resetting switches for days. Then a report proposed something that sounds obvious now and was electric then: put the program in the **same memory as the data**, written as ordinary numbers, and you can change what the machine does by changing those numbers. One memory. One machine. Tell it what to be. This is the idea that made Turing's universal machine buildable — and it is the shape of almost every computer ever built since.*

## Definition — the stored-program computer

A **von Neumann machine** (or **stored-program computer**) is a machine in which **the program and the data live together in one read/write memory**, and the processor works by repeatedly reading the next instruction *out of that memory* and carrying it out. Instructions are not wired into the hardware — they are **numbers stored in memory**, indistinguishable in form from the data they operate on.

That one decision is the whole architecture. From it follow the parts the [[CPU Architecture and the Fetch-Execute Cycle|FDE card]] traces in detail — the control unit, the ALU, the registers, the buses — and the loop those parts run. This card is about the **idea itself**: why storing the program *as data* was the leap, what it unlocked, and what it cost.

The contrast that makes it sharp:

| | **Fixed-program machine** | **Stored-program (von Neumann) machine** |
|---|---|---|
| Where the program lives | in the **wiring** (plugboards, switches) | in **memory**, as numbers |
| To run a different task | **rewire** the machine (hours to days) | **load different numbers** (moments) |
| Can a program build a program? | no | **yes** — code is data |
| Example | ENIAC (1945) | EDVAC (proposed 1945), and ~everything after |

## 中文锚点

**冯·诺依曼机**（**存储程序计算机** stored-program computer）的核心思想只有一句：**程序和数据放在同一块可读写的存储器里**，指令本身就是**存储器中的数字**，与数据在形式上毫无区别。处理器不断地从存储器里**取出下一条指令并执行**——这就是 [[CPU Architecture and the Fetch-Execute Cycle|取指执行周期]] 跑的那个循环。

革命性在于「**程序即数据**」：换任务不用重新接线，只要往存储器里写入不同的数字即可（对比 ENIAC 那种靠插线板的「固定程序」机器，换个问题要接线好几天）。由此衍生出汇编器、编译器、加载器（**会生成程序的程序**）、自举（bootstrapping）、自修改代码——也带来安全隐患：数据若能被当成指令执行，畸形数据就能劫持程序（缓冲区溢出、代码注入）。这正是图灵 1936 年「通用机」（[[Turing Machine]]）的**可建造版本**：喂入不同的「描述」 = 装入不同的程序。谱系：图灵（理论）→ 冯·诺依曼（架构）→ 真实 CPU。

## The leap — from rewiring to reloading

In 1945 the state of the art was **ENIAC**: eighteen thousand vacuum tubes at the University of Pennsylvania, built by **J. Presper Eckert** and **John Mauchly**. It could compute artillery tables a thousand times faster than a person — but to give it a *new* task you reprogrammed it physically, plugging cables and setting switches across its panels. Setting up a new problem could take days. The machine was breathtakingly fast at the calculation and agonisingly slow to *re-aim*.

The team already saw the fix, and in June 1945 it was written down — in the **_First Draft of a Report on the EDVAC_**, the document that defined the design of ENIAC's successor. Its proposal: store the instructions in the machine's memory, **as numbers, alongside the data**. To change the task, you no longer rewire — you load a different program, the same way you load different data. The machine becomes *re-aimable at the speed of memory*.

The first machines to actually **run** a stored program came a few years later — the **Manchester "Baby"** (1948), the first to execute a program held in electronic memory, and Cambridge's **EDSAC** (1949), the first practical one. But the conceptual line in the sand is 1945: *the program is data*.

## Why it is revolutionary — code is data

Storing instructions as ordinary numbers sounds like a filing decision. It is the most consequential idea in computing, because once **code and data are the same kind of thing**, programs can operate on programs:

- **Reprogram by loading, not rewiring.** The machine is *general-purpose* in practice, not just in theory — you change its behaviour at the speed of writing to memory. This is the buildable form of Turing's [[Turing Machine|universal machine]]: feeding a different *description* becomes loading a different *program*.
- **Programs that write programs.** An **assembler** turns mnemonic text into machine-code numbers; a **compiler** turns a high-level language into them; a **loader** drops them into memory and jumps in. All of these are just programs whose *output is more program* — only possible because the output (code) is data the producer can write. The whole software toolchain rests on this.
- **Bootstrapping.** A tiny program can load a bigger one, which loads a bigger one — the machine pulling itself up by reading new code into memory. "Booting" is this word, shortened.
- **Self-modifying code.** A program can rewrite *its own* instructions while running. Early programmers used this for speed and for tricks impossible otherwise; modern systems mostly forbid it (it wrecks caching and security), but the *capability* is inherent in the architecture.
- **The shadow: if data can become code, malformed data can hijack the machine.** A **buffer overflow** that spills attacker-controlled bytes into a region the CPU later *executes* is the dark twin of code-is-data — the same unity that lets a compiler emit a program lets a virus smuggle one in. The defence (the **NX / "no-execute" bit**, **DEP**, **W^X** — memory is either writable *or* executable, never both) is a deliberate, partial retreat *toward* the Harvard split: a small wall put back between code and data, for safety.

> The power and the peril are the *same fact*. A machine that cannot tell its instructions from its data can be reprogrammed by anyone who can write to its memory — which is exactly what you want from a compiler and exactly what you fear from an attacker.

### The same idea, animated

Watch one machine run an **ADD** program, then get reprogrammed into a **MULTIPLY** program by changing a *single number* in memory — no rewiring, same data. The bytes don't know whether they are code or data; only the CPU's reading decides. Pause on any step:

![[von-neumann-stored-program.mp4]]

## The five "organs"

The _First Draft_ did not describe transistors or gates. It described five **organs** — the word is deliberate, borrowed from biology:

- **Central Arithmetic (CA)** — what we now call the ALU.
- **Central Control (CC)** — the control unit, which sequences everything.
- **Memory (M)** — the one store holding both instructions and data.
- **Input (I)** and **Output (O)** — the machine's senses and voice.

The biological language was not decoration. Von Neumann modelled the logical elements on the **idealised neuron** of McCulloch and Pitts (their 1943 paper *A Logical Calculus of the Ideas Immanent in Nervous Activity*), which had shown that networks of simple threshold units could compute logical functions. So the *first written computer architecture was explicitly brain-inspired* — a detail that closes a long loop, because today we run brain-inspired **neural networks** on von Neumann machines, and the mismatch between the two (every weight must cross the bus) is precisely why specialised hardware exists. (The component-level realisation of these organs in a modern CPU — registers, buses, the FDE cycle — is the [[CPU Architecture and the Fetch-Execute Cycle|FDE card]].)

## The von Neumann bottleneck

The defining strength is also the defining weakness. Because instructions *and* data share one memory reached over (classically) one shared path, the processor constantly waits on that single channel — instructions and data cannot both move at once. **John Backus** named this the **von Neumann bottleneck** in his 1977 Turing Award lecture, *"Can Programming Be Liberated from the von Neumann Style?"*

![[von-neumann-vs-harvard.svg|720]]
*The defining tradeoff. Left: the von Neumann machine — one memory holds both program and data, reached by one bus; simple and flexible, but instructions and data compete for the same channel (the bottleneck). Right: the Harvard machine — separate memories and buses for code and data, so the CPU can fetch an instruction and a data word at once; faster, but rigid.*

The rival design, the **Harvard architecture**, splits code and data into separate memories with separate buses, letting the CPU fetch an instruction and a data word simultaneously. Pure Harvard is rigid and rare for general computers — but a **modified Harvard** lives inside nearly every modern chip (the split L1 instruction/data caches). How the cache hierarchy fights the bottleneck — the *memory wall* — is the story of [[CPU Architecture and the Fetch-Execute Cycle|the FDE card's beyond-syllabus]] and [[Pipelining and Simultaneous Multithreading]].

## The credit it never fully got

The name "von Neumann architecture" is itself a small injustice — a textbook case of [[Stigler's Law of Eponymy]] (no discovery is named after its real first discoverer).

The _First Draft_ carried **only von Neumann's name** on its cover. He was a consultant to the ENIAC/EDVAC project, a mathematician of staggering range (the Manhattan Project, game theory, quantum foundations), and he wrote the clearest synthesis of the stored-program idea anyone had produced. But the machine those ideas grew from was built by **Eckert and Mauchly**, who had been circling the stored-program concept themselves — and when Herman Goldstine circulated the draft widely under von Neumann's name alone, it became **published prior art** that later helped *invalidate Eckert and Mauchly's patents* on the electronic computer. The two men who built ENIAC lost the credit, and much of the legal claim, to the consultant who wrote the report.

The honest picture is messy. Von Neumann did not claim sole invention, and the idea had many parents — Turing's 1936 universality, Eckert and Mauchly's hardware, Konrad Zuse's parallel work in Germany, the long shadow of Babbage. But the *label* froze a single name onto a collective achievement. The vault keeps the difficult parts difficult: the architecture is real and magnificent, and the name on it is not the whole truth — which is exactly the lesson of [[Stigler's Law of Eponymy]] and the [[Stories/Turing at Bletchley|forgotten Polish codebreakers]].

## Common Misconceptions

> [!warning] "Von Neumann single-handedly invented the computer."
> No. He wrote the clearest *synthesis* of the stored-program idea (the 1945 EDVAC draft), but the hardware was Eckert and Mauchly's, the universality was Turing's, and the draft's circulation under his name alone cost the actual builders their credit and patents. See [[Stigler's Law of Eponymy]].

> [!warning] "Stored-program means the program is in ROM."
> The opposite. The point is that the program sits in the **same read/write memory as the data**, so it can be loaded, replaced, and even modified. A program burned into read-only memory is closer to the *fixed-program* machine the architecture was invented to escape.

> [!warning] "Von Neumann vs Harvard is just old history."
> The split is alive inside the chip you are reading this on. Almost every modern CPU is a **modified Harvard** at the cache level (separate L1 instruction and data caches) sitting on a unified von Neumann main memory — and the **NX bit** that stops data from being executed is a security-driven Harvard wall. The tradeoff never went away; it moved deeper.

> [!warning] "The von Neumann machine is a kind of CPU."
> It is a **whole-machine organisation** — how memory, processing, and I/O relate — not a component. (The components themselves are in the [[CPU Architecture and the Fetch-Execute Cycle|FDE card]].)

## Exam Notes

The **examinable** content — "the von Neumann architecture: one memory for program and data; ALU, CU, registers, buses; the fetch-decode-execute cycle" — is delivered and closed by the [[CPU Architecture and the Fetch-Execute Cycle]] card (IGCSE 0478 §3.1, AS 9618 §4.1). This card is the **history and the why** behind that one syllabus phrase, and is the best material for the higher-mark "explain the significance of the stored-program concept" style questions.

- **Cambridge 0478 / 9618** — be able to state that a von Neumann machine holds **program and data in the same memory** and that this is what makes a stored-program computer *general-purpose*. The one-line exam answer: *"instructions are stored as data, so the computer can run any program loaded into memory without being rewired."*
- **IB CS (2027)** — the von Neumann *model* is A1.1 working vocabulary, delivered (with the IB tags) by [[CPU Architecture and the Fetch-Execute Cycle]]; this card's historical and theoretical depth — First Draft, EDVAC, code-as-data — is **not separately examined**.
- **A-Level depth / university** — the **von Neumann bottleneck**, the **Harvard** alternative, and the code-as-data consequences (compilers, bootstrapping, security) are standard in any first architecture course.

## Connections

- **Prerequisite (theory):** [[Turing Machine]] — the 1936 *universal* machine; the von Neumann machine is its **buildable, electronic** form, with the "description on the tape" moved into read/write memory beside the data.
- **Leads to (the realisation):** [[CPU Architecture and the Fetch-Execute Cycle]] — the components and the loop that *run* the stored program; then [[Pipelining and Simultaneous Multithreading]] — how the architecture is made fast, and how the bottleneck is fought.
- **Built from:** [[Logic Gates]] — the "organs" (CA/CC) are assemblies of gates; the brain-inspired threshold logic of the _First Draft_ is the same universality that [[Logic Gates|NAND]] embodies.
- **The credit theme:** [[Stigler's Law of Eponymy]] — "von Neumann architecture" as a named-after-the-wrong-person classic; the forgotten builders.
- **History:** [[Stories/von Neumann the Martian]] — the man himself: the breadth, the self-replication/DNA prophecy, and the death the most rational mind could not out-think; [[Stories/The Boolean-to-Silicon Bridge]] — the 1945 EDVAC report in the full Sheffer-to-silicon arc; [[Stories/Turing at Bletchley]] — the theorist whose universal machine this architecture realises.

## Beyond Syllabus

> [!info] The neuron loop — and why AI hardware leaves von Neumann behind
> The _First Draft_ described its logic in the language of McCulloch-Pitts neurons (1943). Eighty years later we run actual neural networks on von Neumann machines — and hit a wall: every one of billions of weights must be hauled across the bus between memory and processor for every calculation. The **bottleneck becomes the dominant cost** of AI. The escapes all loosen the von Neumann constraint: **GPUs** throw enormous memory bandwidth and thousands of ALUs at it (→ [[Pipelining and Simultaneous Multithreading]]); **in-memory / neuromorphic** computing tries to compute *inside* the memory, abolishing the separation the architecture is built on. The brain that inspired the design is now the reason we are designing past it.

> [!info] Non-von-Neumann models
> Not every computer is von Neumann. **Dataflow** machines run an instruction the moment its inputs are ready, with no single program counter. **Quantum** computers are a different model entirely (superposition and interference, not stored numbers fetched in sequence). And the **Harvard** family never fully went away — it rules microcontrollers and DSPs, where fetching code and data at once matters more than flexibility. The von Neumann machine won not because it is fastest, but because *one memory for everything* is the most flexible and cheapest thing to build — and flexibility, given Moore's law, beat specialisation for fifty years.

## LaTeX / Notation Reference

This card is conceptual; the only formal vocabulary is the _First Draft_'s organ names and the architecture terms.

| Term | Means | Modern name |
|------|-------|-------------|
| CA | Central Arithmetic | ALU (arithmetic-logic unit) |
| CC | Central Control | CU (control unit) |
| M | Memory | main memory / RAM (one store for code + data) |
| I / O | Input / Output | I/O subsystem |
| stored-program | program held in M as data | the defining property |
| von Neumann bottleneck | one shared CPU-memory channel | the memory wall ([[Pipelining and Simultaneous Multithreading]]) |
| Harvard architecture | separate code and data memories/buses | modified Harvard = split L1 cache |
