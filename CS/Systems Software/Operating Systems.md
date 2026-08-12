---
chinese: 操作系统 (cāozuò xìtǒng)
prerequisites:
  - "[[Interrupt Handling]]"
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[RAM and the Memory Hierarchy]]"
  - "[[Secondary Storage]]"
  - "[[Embedded Systems]]"
leads_to:
  - "[[Compilers and Interpreters]]"
  - "[[File Systems]]"
tags:
  - subject/computer-science
  - domain/systems-software
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-4-1
  - syllabus/9618-5-1
  - syllabus/9618-15-1
  - syllabus/9618-16-1
  - type/deep
  - misconception/os-is-the-whole-bundle
  - misconception/multitasking-is-simultaneous
  - misconception/virtual-memory-is-free-ram
  - misconception/kernel-is-an-app
---

# Operating Systems 操作系统

> *Strip a computer of its software and what remains is a savage place: a processor that executes whatever the Program Counter points at, memory that belongs to whoever writes to it first, a disk that is just billions of numbered blocks, and devices that answer only to exact register pokes. Programming that machine means driving the disk motor yourself. Every program you have ever written lived somewhere kinder — a world of windows, files, and the serene belief that your program had the whole machine to itself. That kinder world is a fiction, and this card is about the program that writes it: the* operating system, *part **government** (it owns every resource and rations them out) and part **illusionist** (every program gets a private machine that does not exist). It is also the payoff of a promise: [[Interrupt Handling]] ended with a kernel woken by a timer tick — this card is what the kernel* does *with the wake-up.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| operating system (OS) | 操作系统 | the resource-managing, illusion-providing program between hardware and everything else |
| system vs application software | 系统软件 / 应用软件 | runs the machine vs does the user's actual task |
| firmware | 固件 | software burned into hardware — the boot code that runs before any OS |
| kernel | 内核 | the OS's core: the only code with full authority over the hardware |
| process | 进程 | a program *in execution* — the recipe actually cooking |
| multitasking / scheduling | 多任务 / 调度 | many processes sharing one CPU by rapid turn-taking |
| process states | 进程状态 | running / ready / blocked — the three lives of a process |
| virtual memory / paging | 虚拟内存 / 分页 | the illusion of more memory than exists, in fixed-size pages |
| disk thrashing | 磁盘抖动 | the illusion collapsing: more time swapping pages than working |
| utility software | 实用程序 | the OS's toolbox: formatter, defragmenter, backup, virus checker… |
| program library / DLL | 程序库 / 动态链接库 | pre-built code that programs borrow instead of rewriting |
| virtual machine (VM) | 虚拟机 | the illusion recursed: a software computer running inside the real one |

## Why a computer needs one

Two answers, and the exam wants both flavours:

**The government answer — resources are scarce and contested.** One CPU, finite RAM, one disk arm, one network card — and dozens of programs wanting all of them at once. Without an authority, the first program to grab the sound card keeps it; a buggy program scribbles over another's memory; nothing guarantees your keystrokes reach the window you're looking at. The OS owns every resource and **rations them**: CPU time by scheduling, memory by allocation and protection, devices by queues and drivers. Its constitution is [[Interrupt Handling]]: hardware interrupts are how events reach the government, and the timer interrupt is how it takes power back from whoever holds the CPU.

**The illusionist answer — bare hardware is unusable.** The disk knows nothing of files, only numbered blocks ([[Secondary Storage]]); the processor knows nothing of windows, only instructions ([[CPU Architecture and the Fetch-Execute Cycle]]). The OS wraps the savage machine in **abstractions**: files instead of blocks, processes instead of raw CPU, a large private address space instead of contested RAM. The user interface is the last abstraction of the stack — the LO's phrasing is exact: *the user interface hides the complexities of the hardware.*

And the honest boundary: some computers genuinely run **without** an OS — the ¥2 microcontroller in a toaster runs one sealed program on bare metal ([[Embedded Systems]]'s control ring). An OS earns its cost precisely when the machine must run *many, changing, mutually-suspicious* programs. General-purpose = OS; sealed single purpose = maybe none.

## The layer cake — hardware, firmware, OS, applications

![[os-layer-cake.svg|697]]

- **Hardware** — the physical machine.
- **Firmware** — software stored *in* the hardware (flash ROM on the board): the code that runs first at power-on. The **bootstrap**: the CPU wakes pointing at firmware (BIOS/UEFI on a PC); firmware checks the hardware, finds the disk, loads the OS's loader into RAM, and jumps — each stage pulling in a bigger one, the system hoisting itself by its own straps. Firmware is the bridge in 0478's trio: *hardware runs firmware; firmware loads software.*
- **Operating system** — the kernel plus its services, loaded by firmware, resident until shutdown.
- **System vs application software:** system software runs and maintains the machine itself (the OS, utilities, translators); **application software does the user's actual task** (browser, word processor, game). The test: *would you still need it if you used the computer for something completely different?* System software: yes. Application: no.

## The management portfolio

The syllabus names the OS's key tasks; each is a mechanism, not a bullet point.

### Process management — sharing one CPU

A **program** is a recipe on the shelf; a **process** is that recipe *actually cooking* — code plus its live state (its registers, its memory, its open files). One CPU core runs one instruction stream, so multiple processes share by **turn-taking so fast it looks parallel**: multitasking. The machinery is [[Interrupt Handling]]'s finale, now given its full name: the **kernel acts as an interrupt handler** — the timer interrupt fires many times a second, the kernel's ISR runs, and *low-level scheduling* decides who gets the CPU next.

Every process lives in one of **three states**:
![[os-process-states.svg|697]]

- **Running** — on the CPU right now (one per core).
- **Ready** — able to run, waiting in the queue for its turn.
- **Blocked** — *cannot* use the CPU even if offered: waiting for something outside it (a disk read, a keypress, a network packet). The arrows are the story: running → ready when the time slice expires (the scheduler's tap on the shoulder); running → blocked when the process *asks* for I/O; blocked → ready when the interrupt announces the I/O finished. A blocked process costs no CPU — that is the whole point ([[Input and Output Devices]]'s interrupts-not-polling, at process scale).

**The scheduling policies** — 9618 names four; each has a function and a benefit:

| policy | how it picks | benefit | price |
|---|---|---|---|
| **First come, first served (FCFS)** | strict arrival order, run to completion | simple, no starvation, fair by queue | one long job makes everyone wait (the supermarket trolley ahead of your single item) |
| **Shortest job first (SJF)** | shortest total job next | minimises *average* waiting time (provably) | needs job lengths in advance; long jobs can starve |
| **Shortest remaining time (SRT)** | SJF made preemptive — a new shorter job interrupts the current one | best average response for short jobs | more switching; long jobs starve harder |
| **Round robin (RR)** | everyone gets a fixed **time slice**, in rotation | responsive — no job waits long for *a* turn; fits interactive systems | frequent switching has overhead; slice length is a tuning war |

Watch all three states and the rotation run:

![[os-round-robin.mp4]]

### Memory management — sharing the RAM, and faking more of it

The OS allocates each process its memory, **protects** it (process A physically cannot read B's — the government's police power), and reclaims it on exit. Then the deep trick, promised by [[RAM and the Memory Hierarchy]] and [[Secondary Storage]]: **virtual memory**. Each process is given the *illusion* of a large private memory; behind the curtain, the OS keeps only the actively-used parts in RAM and parks the rest on disk.

Two ways to slice a program for this — and the difference between them is the examined point:

- **Paging** — memory chopped into **fixed-size** blocks (pages, typically 4 KiB), placed into any free RAM frame. Physical, uniform, invisible to the program. Simple for the OS (any page fits any frame); a page's neighbours in the program needn't be neighbours in RAM.
- **Segmentation** — memory divided into **variable-size logical units** (the code, the stack, a data table) matching the *program's* structure. Meaningful pieces, natural protection per segment — but variable sizes leave awkward gaps as segments come and go.

*(Modern systems page; the difference between fixed-physical and variable-logical division is the examined idea.)*

![[os-paging-thrashing.svg|697]]

**Page replacement:** when RAM is full and a needed page is on disk (a **page fault**), the OS must evict some page to make room — ideally one not used recently, betting on the locality that makes caches work. **Disk thrashing** is the bet failing wholesale: too many processes, too little RAM, every page brought in evicts a page needed a moment later — the machine spends its life swapping instead of working, the disk light burns solid, and *adding work now subtracts progress*. The illusion of infinite memory is a loan, and thrashing is the repossession.

### File management — names over blocks

The disk stores numbered blocks; the OS builds the entire world of **files and folders** on top: names, hierarchical directories, extensions, permissions, timestamps — and the bookkeeping of which blocks belong to which file ([[File Systems]] carries the deep story). Creating, copying, moving, deleting; controlling which user may touch what.

### Hardware (input/output/peripheral) management

Every device speaks its own dialect; the OS carries a **driver** per device to translate, runs transfers through **buffers**, and hears completion via **interrupts** — the whole [[Input and Output Devices]] mechanism, now under one authority that also *shares* the devices (two programs printing at once get a queue, not interleaved pages).

### Security management

The government's border control: user accounts and **authentication** (passwords and their modern relatives), **permissions** on files and actions, isolation between users and processes, and the audit trail (logs). Utilities like the virus checker plug into this task.

### The user interface

The final layer of the illusion, in two classic costumes: the **command-line interface** (CLI — terse, scriptable, precise; the power user's lever) and the **graphical user interface** (GUI — windows, icons, menus, pointer; discoverable, gentle to beginners, heavier on resources), plus the modern additions (touch, voice). One OS, several faces — all doing the same thing underneath: turning human intent into system calls.

> [!info] The CLI's renaissance — an interface finds its native speaker
> The GUI won the mass market for a deep reason: it matches human perception — recognition over recall, spatial memory, things you can *see* and point at. The CLI survived among professionals for an equally deep one: it is **text in, text out**, which makes it *composable* (chain small tools into pipelines) and *scriptable* (yesterday's session is today's program). Then AI arrived and the balance shifted: a language model reads and writes text natively, so the CLI's one great cost — memorising terse commands and flags — evaporates when an assistant composes them for you, while its great strength — every action expressible, repeatable, and chainable as text — is exactly what an AI agent needs to act on a computer. The interface built for humans-imitating-machines turns out to be the natural habitat for machines-assisting-humans; the GUI was built for human eyes, and the CLI, it turns out, for AI hands.

## The toolbox — utility software

Utilities are system software with one maintenance job each. 9618 names six; know each one's *purpose*:

| utility | job |
|---|---|
| **disk formatter** | prepare a disk for use: lay down a blank file system (and erase what was there) |
| **virus checker** | scan files/activity against known signatures and suspicious behaviour; quarantine |
| **defragmentation software** | re-gather each file's scattered blocks into runs, so an HDD's arm travels less ([[Secondary Storage]]'s geometry — and the same card's warning: **never defragment an SSD**; no arm to save, wear to pay) |
| **disk contents analysis / repair** | report what fills the disk; find and fix damaged structures (lost blocks, broken directory entries) |
| **file compression** | shrink files for storage/transfer — [[Compression]]'s algorithms in a utility's clothes |
| **back-up software** | scheduled copies elsewhere, often incremental (only what changed) — [[Secondary Storage]]'s "storage is a lease" made policy |

> [!warning] The blurry boundary — and the exam's clean line
> In real life the OS/utility seam has all but vanished: modern systems *bundle* their utilities (the virus checker is Windows Defender, defragmentation runs on a schedule you never see, compression hides inside the file manager) — so "part of the OS" and "utility provided with the OS" describe the same download. Real life accepts the blur. **The exam's discriminator stays clean, and it is two questions.** *Could the machine still boot and run programs without it?* The OS proper: no — it is the always-resident manager. A utility: yes — things would just get slower, messier, or riskier. *Is its job maintaining the machine, or doing the user's end-task?* Maintaining → system software (OS or utility); the user's task → application. So: kernel scheduling = OS; defragmenter = utility (system software, on-demand, survivable); word processor = application. Answer with the questions, not with what your laptop happens to bundle.

## Program libraries — never write it twice

Software is built *on* software: a **program library** is a collection of pre-written, pre-tested routines (mathematics, graphics, networking) that developers call instead of reinventing — faster development, fewer bugs, expert-grade implementations of hard things. The refinement is **when the borrowed code joins**: linked in at build time (static — a private copy inside your executable), or loaded at run time from a **Dynamic Link Library (DLL)** — one shared copy on disk serving every program that needs it. DLL benefits, per the syllabus: smaller executables, shared memory-resident code, and **fix-once-fix-everywhere** (patch the DLL, every program benefits without recompiling). The price (beyond the LO, honest): a missing or wrong-version DLL breaks programs that expected it — "DLL hell", the reason installers ship so much.

> [!info] How a shop ended DLL hell — the Steam lesson
> Ask anyone who gamed on a PC in the 2000s: the ritual was download, launch, and *"the program can't start because XYZ.dll is missing."* Steam largely ended it — not by changing Windows, but by changing *distribution*: every game on the platform declares its dependencies, and Steam silently installs the right runtime libraries with the game, patches centrally, and verifies files on demand. The same move quietly won a bigger war: piracy shrank not because copying got harder but because **buying got smoother** — one click, auto-updates, saves in the cloud, no DLL roulette — while the pirated copy kept all the friction. Valve's Gabe Newell said it plainly: piracy is a *service* problem, not a price problem. If you expect customers to pay, make paying the smoothest path there is — a lesson about software, and not only about software.

## Virtual machines — the illusion, recursed

The OS's whole craft is giving each *process* a private pretend machine. A **virtual machine** takes the trick one level up: software that emulates an *entire computer* — virtual CPU, memory, disk, devices — so faithfully that a complete **guest OS** runs inside it, unaware, while the **host** system carries it as just another set of processes.

- **Roles (give examples):** run Windows software on a Mac; test an app across many OS versions on one desk; let one physical server carry many isolated virtual servers (the shape of the entire cloud — "renting a server" nearly always means renting a VM); contain malware for safe study; keep a legacy system alive after its hardware dies.
- **Benefits:** isolation (a crashed or infected guest can't touch the host), consolidation (fewer physical machines), snapshots (freeze a machine, restore it after disaster), hardware independence.
- **Limitations:** overhead — a guest runs slower than the same OS on real hardware, and each guest duplicates a whole OS's memory appetite; imperfect access to exotic hardware; and a licence per guest is still a licence.

*(One name, two ideas: these system VMs virtualise hardware. The "virtual machines" inside language runtimes — bytecode interpreters — are [[Compilers and Interpreters]]' story.)*

## Worked examples

### Example 1 (9618 §16.1 — scheduling, priced)

> Three jobs arrive at $t = 0$ in the order P1 (needs 10 ms), P2 (2 ms), P3 (4 ms). For **FCFS** and **SJF**, give each job's waiting time and the average.

*Tool: the policy definitions — FCFS runs in arrival order; SJF sorts by length.*
FCFS order P1→P2→P3: waits are 0, 10, 12 → average $\tfrac{0+10+12}{3} = 7.3$ ms.
SJF order P2→P3→P1: waits are 0 (P2), 2 (P3), 6 (P1) → average $\tfrac{0+2+6}{3} = 2.7$ ms.

*Tool: the trade, in context.* SJF nearly triples the queue's throughput of finished short jobs — the provable average-wait winner — but P1, the longest job, waits longest, and in a stream of arriving short jobs it could starve. FCFS never starves anyone and never needs to know lengths in advance.

### Example 2 (9618 §16.1 — explain thrashing)

> A computer with 8 GB of RAM runs smoothly with 20 processes. When a user opens ten more large applications, the disk activity light stays on continuously and *every* program slows to a crawl — including tiny ones. Explain.

*Tool: virtual memory → page faults → the thrashing spiral.* The thirty processes' working sets no longer fit in RAM together. Each process, when scheduled, immediately needs pages that were evicted to disk to make room for others (page faults); servicing each fault evicts pages the *next* process needs. The OS now spends nearly all time transferring pages between disk and RAM — disk busy constantly, CPU mostly waiting — so every process, however small, queues behind the swapping. That is **disk thrashing**: the cure is fewer simultaneous processes or more RAM, not a faster CPU.

### Example 3 (0478 — why an OS at all)

> A desktop computer runs many programs; a washing machine's controller runs none but its own. Explain why the desktop requires an operating system and the washing machine's controller does not.

*Tool: the government answer + the sealed ring.* The desktop runs many changing programs that must share one CPU, one memory, and the devices — it needs an authority to schedule the processor, allocate and protect memory, manage files and I/O, and present an interface; without one, programs would conflict over every resource. The washing machine runs a single fixed program with the hardware to itself ([[Embedded Systems]]): nothing contends, nothing changes, so the program can own the bare metal — an OS would add cost and complexity for no benefit.

## Common Misconceptions (Teaching Notes)

### 1. "The OS is everything that came with the computer"

The browser, the calculator, the bundled games are *applications* that shipped alongside. **Fix:** apply the classification test — system software runs the machine (OS, utilities, translators); applications do a user task. Bundling is marketing, not architecture.

### 2. "Multitasking means the programs run at the same time"

On one core, **exactly one instruction stream runs at any instant** — the rest are ready or blocked. The simultaneity is an illusion manufactured by the timer interrupt and fast switching (and even on eight cores, dozens of processes still share by turns). **Fix:** the three-state diagram — at most one *running* per core, and the state names describe everyone else honestly.

### 3. "Virtual memory means free extra RAM"

The extension is *borrowed from the disk*, thousands of times slower than RAM. Light borrowing is invisible; heavy borrowing is **thrashing** — the machine grinding on swaps. **Fix:** Example 2's spiral, plus the loan metaphor: virtual memory is credit, locality is your income, thrashing is the repossession.

### 4. "The kernel is a program running alongside mine, using up a core"

The kernel is not a process taking turns — it is the **turn-giver**: code that runs *on events* (interrupts, system calls) in the brief moments between everyone else's slices, then hands the CPU straight back. **Fix:** [[Interrupt Handling]]'s picture — the kernel is the ISR-and-scheduler machinery, dormant until a bell rings. (When the bells never stop, kernel time does become real overhead — but as service, not as a competing job.)

## Exam Notes

### Cambridge 0478 — §4.1 (IGCSE)

- **§4.1.1–2:** define system vs application software with examples; the **basic functions of an OS** — the management list at IGCSE depth (memory, files, processes/multitasking, peripherals, security, user interface) with one-line whys. **§4.1.3:** the hardware–firmware–software relationship — firmware as software-in-hardware, the boot chain: hardware runs firmware, firmware loads the OS, the OS runs applications. (§4.1.4 interrupts: [[Interrupt Handling]]'s row, already yours.)
- Typical asks: "state three tasks carried out by an operating system"; classify given programs as system/application; explain what firmware is and why it is needed at start-up.

### Cambridge 9618 — §5.1 (AS)

- Why a computer needs an OS; the **key management tasks** (memory, file, security, hardware/I-O/peripheral, process — say *mechanism*, not just the noun: "memory management: allocates memory to processes and protects each process's space"); the **six named utilities** with purposes; **program libraries** — why developers build on them, and **DLL** benefits specifically (shared one copy, smaller executables, fix-once-fix-everywhere).

### Cambridge 9618 — §16.1 + §15.1 (A2)

- **§16.1:** the resource-maximising and complexity-hiding purposes; **process states** (running/ready/blocked) with the *transition causes*; the **four scheduling policies** with function *and* benefit each; **the kernel as interrupt handler** driving low-level scheduling ([[Interrupt Handling]] + this card's process section); **paging vs segmentation** (fixed-physical vs variable-logical), page replacement, and **how disk thrashing occurs** (Example 2's spiral is the mark scheme's shape).
- **§15.1 (the VM bullets):** the concept of a virtual machine (guest system on emulated hardware), **examples of the role** (testing, consolidation/cloud, legacy, isolation), and benefits vs limitations (isolation and snapshots vs overhead and imperfect hardware access).

### Other boards

- **AP CSP:** operating systems appear only as background computing-systems vocabulary — no management-task depth. **IB CS 2027:** A1's hardware statements stop at CPU/memory/FDE; OS process/memory machinery is not a named statement list — treat this card as the deeper story behind their systems fundamentals.

## Beyond the syllabus

> [!info] The mode bit — how the illusion is enforced
> What stops a rogue program from simply *taking* the disk or another process's memory? One bit. The CPU runs in two modes: **user mode** (privileged instructions and raw device access forbidden — the hardware itself refuses) and **kernel mode** (everything allowed). Applications run in user mode; the only doorway into kernel mode is a **system call** — a deliberate, controlled trap into OS code at an OS-chosen address ([[Interrupt Handling]]'s software-interrupt cousin). Every file open, every network packet, every pixel your program "draws" is actually a polite request across that boundary. The government's monopoly on force, implemented in silicon.

> [!info] Containers — the VM's lightweight rival
> A virtual machine carries a whole guest OS just to isolate one application. **Containers** (Docker, and the Kubernetes fleets built on it) share the host's kernel and isolate only the process's *view* of it — its own filesystem, network, process list — at a fraction of the memory and startup cost. The trade: weaker isolation (one kernel, shared) for radical density (hundreds of containers where a machine fits a handful of VMs). Modern cloud practice layers them: VMs for hard security boundaries, containers for packaging inside them.

> [!info] Many cores, many threads — and why the pros take over
> On a multi-core machine the scheduler's job goes two-dimensional: each core runs its own queue (with its own timer interrupt), a balancer migrates work between queues, and **affinity** tries to keep a process on the core whose caches still remember it ([[Interrupt Handling]]'s multi-core section, now with a scheduler attached). The unit being juggled is really the **thread** — processes can contain several instruction streams sharing one memory — and a real desktop scheduler (Linux's CFS lineage, now EEVDF) additionally juggles priorities, fairness debts, and interactivity boosts, because a 50 ms lag is invisible in a compile job and infuriating in a keystroke.
>
> And here is the honest twist: serious software often **takes scheduling back**. The OS scheduler is a *general-purpose government* — fair to everyone, expert in nothing: it cannot know that your game must finish a frame in 16 ms, or that these two tasks share data and should never sit on distant cores. So performance-critical programs ask the OS for a few real cores and run **a private economy on top**: a **thread pool** (one worker thread per core, and the *program* deals its own small tasks onto them — ten thousand jobs on eight threads, without ten thousand OS context switches); **pinning** (nail a thread to a core for cache warmth and steady latency — games, audio workstations, trading systems); **async event loops** (one thread juggling thousands of waiting I/O operations itself, sidestepping the scheduler entirely — the architecture of every modern server); and **user-space "green" threads** (Go's goroutines: millions of cheap tasks scheduled by the language runtime onto a handful of OS threads, because the runtime knows the program's intent and the kernel never can). The recursion is pleasing: programs found the OS's turn-taking too generic, so they built *their own little OS* inside — the same move [[Stories/Dual-Core Craft]] shows a game engine making for determinism's sake. Real-time systems go further still ([[Embedded Systems]]): they don't want *fair* at all, they want *guaranteed-by-the-deadline* — a different mathematics for the airbag's kind of promise.

## Connections

- **Builds on:** [[Interrupt Handling]] — the constitution: the timer tick that takes the CPU back, the kernel as interrupt handler, the ISR/scheduler machinery this card names and completes; [[CPU Architecture and the Fetch-Execute Cycle]] — the one instruction stream being shared; [[RAM and the Memory Hierarchy]] — the memory being allocated, protected, and extended (its virtual-memory preview cashed here); [[Secondary Storage]] — the blocks under the files, the swap space under the paging, and the defrag/SSD warning the utilities table inherits.
- **Leads to:** [[Compilers and Interpreters]] — the bay's next resident: 9618 §5.2's translators and §16.2's compilation stages, plus the *other* kind of virtual machine; [[File Systems]] — the file-management section's deep story (how names become blocks).
- **Kindred:** [[Embedded Systems]] — the honest contrast: the machine that needs no OS, and the real-time scheduling contract when it needs a small one; [[Input and Output Devices]] — drivers, buffers, and the interrupt-driven I/O the hardware-management section governs; [[Compression]] — the file-compression utility's engine.
