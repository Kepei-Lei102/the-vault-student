---
chinese: 中断处理 (zhōngduàn chǔlǐ)
prerequisites:
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[Input and Output Devices]]"
  - "[[Embedded Systems]]"
leads_to:
  - "[[Operating Systems]]"
  - "[[CISC vs RISC]]"
tags:
  - subject/computer-science
  - domain/computer-architecture
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-4-1
  - syllabus/9618-4-1
  - syllabus/9618-16-1
  - type/deep
  - misconception/interrupt-stops-mid-instruction
  - misconception/isr-runs-in-parallel
  - misconception/interrupts-are-only-hardware
  - misconception/polling-is-always-worse
---

# Interrupt Handling 中断处理

> *You are deep in a novel when the doorbell rings. You do not throw the book away, and you do not finish the remaining two hundred pages first. You do something so practised you never think about it: you finish the **sentence**, slide a **bookmark** into the page, answer the door, deal with it, come back, open to the bookmark, and read on — as if nothing had happened. A CPU does exactly this, thousands of times a second, and the bookmark has a name you already know: the **program counter**. This card is about the doorbell, the bookmark, and the discipline of being interruptible — which is nothing less than how a machine that can only do one thing at a time appears to care about everything at once.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| interrupt | 中断 | a signal that makes the CPU suspend its current program and attend to something else |
| interrupt service routine (ISR) | 中断服务程序 | the short program that handles one specific interrupt |
| interrupt vector table | 中断向量表 | the table mapping each interrupt number to its ISR's address |
| polling | 轮询 | the alternative: the CPU asks every device "anything yet?" forever |
| context saving | 现场保护 | pushing PC + registers to the stack before the ISR — literally "protecting the scene" |
| priority | 优先级 | the rank deciding which of two simultaneous interrupts is served first |
| nested interrupts | 嵌套中断 | a higher-priority interrupt interrupting an ISR itself |
| interrupt masking | 中断屏蔽 | temporarily refusing (most) interrupts during critical work |
| NMI (non-maskable interrupt) | 不可屏蔽中断 | the one signal that cannot be refused — reserved for catastrophe |
| timer interrupt | 时钟中断 | the metronome interrupt that drives multitasking |
| exception | 异常 | an interrupt raised by the running program's own error |
| system call | 系统调用 | a *deliberate* software interrupt — the program knocking on the OS's door |

## The seam this card opens

Recall the speed gulf from [[Input and Output Devices]]: the CPU lives in nanoseconds, devices in milliseconds, and **polling** — asking every device "anything yet?" millions of times for every real event — squanders the fast partner on secretarial work. The fix named there: the device stays silent until it genuinely needs attention, then **raises the interrupt line on the control bus** — the very wire drawn in [[CPU Architecture and the Fetch-Execute Cycle]] — and the CPU responds with *save state → ISR → restore state*.

That one sentence is the whole idea. This card slows it down to exam speed: **what can ring the bell, exactly when the CPU listens, and precisely how it leaves and returns without losing its place.**

## What can ring the bell — the causes

The syllabus wants causes *classified*, and the classification is worth having because each family answers a different "why":

| Family | Examples | Why it must interrupt |
|---|---|---|
| **I/O device events** | key pressed, mouse moved, printer out of paper, disk transfer complete, network packet arrived | the event is *rare* and *unpredictable* — polling for it wastes almost every ask |
| **Timer** | the clock chip fires every few milliseconds | someone must wake the OS regularly, or one program could hold the CPU forever |
| **Hardware fault** | power failing, memory error detected | catastrophe cannot wait its turn — some of these are **non-maskable** |
| **Program error (exception)** | division by zero, illegal instruction, touching memory you don't own | the running program *cannot continue* — control must go somewhere sane |
| **Software interrupt (system call)** | a program *asks* the OS for a file, more memory, the screen | the deliberate case: the program rings the bell on itself to enter the kernel politely |

Notice the last two rows: **not every interrupt comes from hardware.** A program can be the source of its own interruption — by accident (exception) or on purpose (system call). The doorbell can be rung from inside the house.

> [!tip] "But I click the mouse hundreds of times a minute when I'm gaming!"
> You do — and to the CPU that is still almost never. Six hundred frantic clicks a minute is one event every 100 ms, and a 5 GHz core runs **half a billion cycles between your clicks**. Even a pro StarCraft player at 400 APM is ringing the bell about seven times a second — a doorbell that, on the CPU's clock, stays silent for geological ages. "Rare" is always measured on the *processor's* timescale, not yours; that is why polling for a human is such spectacular waste, and why the interrupt earns its keep even at your wildest click rate.

## The mechanism — six steps, one bookmark

![[interrupt-fde-cycle.svg|697]]

Here is the full sequence, the exam's favourite six-marker, told once with every step earning its place:

1. **The signal is raised.** A device pulls the interrupt line on the control bus. Nothing else happens yet — the CPU is mid-instruction and pays no attention.
2. **The current instruction completes.** The CPU *never* abandons an instruction halfway — an instruction is atomic, finished or not-started, exactly as you finish the sentence before answering the door. (Half-executed instructions would leave registers in states no ISR could safely restore.)
3. **The check.** At the end of **every** fetch–decode–execute cycle, the CPU examines the interrupt flag. The cycle you learned is really fetch → decode → execute → ***check*** — a fourth beat so routine it is drawn as part of the loop, and the honest answer to "*when* are interrupts detected?"
4. **The scene is protected (现场保护).** If the flag is set (and not masked), the CPU pushes its state onto [[The Stack|the stack]]: the program counter — the bookmark itself — plus the working registers and status flags. Everything needed to stand in this exact spot again.
5. **The vector table is consulted.** Each interrupt source has a number; the number indexes the **interrupt vector table** in memory, which holds the *address* of the matching **ISR**. The CPU loads that address into the PC and jumps. (A table, not wiring — adding a new device means writing one address into memory, the stored-program idea paying out again.)
6. **The ISR runs, then returns.** The routine does its short, specific job — read the scan code, acknowledge the disk — and ends with a return-from-interrupt instruction: the saved state pops off the stack, the PC gets its old value back, and the original program resumes **as if nothing had happened**. It never knows it was paused.

The program's ignorance is the design's triumph: interruption is invisible to the interrupted. Every program you have ever run was suspended thousands of times mid-flight, and none of them ever noticed.

And here is the whole sequence in motion — the cycle ticking, the bell, the bookmark flying to the stack, the vector jump, and the seamless return:

![[interrupt-cycle.mp4]]

## When two bells ring at once — priority, nesting, masking

![[interrupt-priority-timeline.svg|697]]

One doorbell was easy. Real machines have dozens, and the interesting rules are about *contention*:

- **Priority.** Every interrupt source carries a rank. When two arrive together, the higher rank is served first; the lower waits its turn in a queue. Power-failure outranks disk; disk outranks keyboard. (Rank by *cost of delay*, not by frequency.)
- **Nesting.** What if a *higher*-priority interrupt arrives while an ISR is already running? The ISR is itself interrupted — its own scene is pushed onto the stack, the more urgent routine runs, then the stack unwinds scene by scene. The stack can hold a whole pile of protected scenes, which is precisely why the save-area is a *stack* and not a single slot.
- **Masking.** Some work must not be interrupted — an ISR updating the very queue that interrupts use, for example. The CPU can temporarily **mask** (disable) interrupts for a few instructions. Requests raised meanwhile are not lost; they wait, flagged, until the mask lifts.
- **NMI.** And one signal ignores the mask entirely: the **non-maskable interrupt**, reserved for events where "not now" is meaningless — the power is dying, memory is corrupt. If the alarm is a fire alarm, you answer mid-sentence after all.

Look closely and you will see **two different data structures quietly running this show** — and telling them apart is the mark of real understanding. Interrupts *waiting to be served* sit in a **priority queue**: new arrivals join by rank, and the highest rank is served next, whatever order the bells rang in. Programs and ISRs *already suspended* pile on [[The Stack|the stack]]: strictly last-suspended, first-resumed, no exceptions. One structure decides **who rings next**; the other decides **who resumes next** — jump-the-line for the waiting, perfect symmetry for the waited-on.

![[interrupt-stack-queue.svg|697]]

## The metronome — how interrupts became multitasking

Now the largest consequence, and the bridge out of this card. No program ever *volunteers* to give up the CPU — a loop would happily run forever. So the operating system arranges a standing appointment: the **timer interrupt**, a clock chip ringing every few milliseconds, unconditionally.

Its ISR is the **scheduler**. Each tick: protect the current program's scene, decide who runs next, restore *that* program's scene instead. Do this a hundred times a second across a dozen programs and you get the great illusion of the modern computer — everything running "at once" on hardware that only ever runs one thing. Multitasking is not an extra ability the CPU has; **it is the timer interrupt, applied relentlessly**. The kernel spends its life as an interrupt handler — this is 9618 §16.1's "low-level scheduling," and the fuller story of scheduling policies belongs to [[Operating Systems]].

The retro-gaming version is too good to skip: on the NES, the graphics chip interrupted the CPU at every screen refresh — sixty times a second — and games ran their *entire logic* inside that ISR. *Super Mario Bros.* is, structurally, an interrupt service routine.

![[interrupt-magician-comic.png|640]]

## The price tag

The tap on the shoulder is not free, and the honest costs explain several design rules:

- **Context switching costs time.** Saving and restoring a scene is dozens of memory operations, plus the refilling of caches and pipelines that the switch disturbed ([[Pipelining and Simultaneous Multithreading]] explains why a drained pipeline stings). Interrupt too often and the CPU spends its life bookmarking instead of reading.
- **So ISRs are kept minimal.** The working rule: do the urgent sliver (grab the byte, acknowledge the device, set a flag), *defer* everything else to ordinary scheduled code. An ISR that dawdles is holding every lower-priority bell silent.
- **Latency is the real-time currency.** The delay from signal to ISR — interrupt latency — is what an [[Embedded Systems|embedded controller]] budgets when the airbag allows ~25 ms: the deadline includes the time to *notice*. It is also why a sleeping microcontroller can spend years at nanoamps: **sleep-until-interrupt** costs nothing while it waits, then wakes in microseconds. The interrupt is the embedded world's entire idiom — the loop sleeps, the world knocks.
- **And the bus has opinions.** Recall the I/O card's surprise: USB devices cannot seize a shared bus, so the *bus controller* polls them on a precise schedule and interrupts the CPU only with real data — "the bus polls, the CPU is interrupted." The two mechanisms are teammates, not rivals; [[Input and Output Devices]] holds that story, along with DMA's version — one interrupt at the *end* of a bulk transfer instead of one per byte.

## Worked example 1 — the six-marker

> *An interrupt is generated while a program is running. Describe the steps taken by the processor to handle the interrupt.* **[6]**

*Tool: the six-step mechanism — signal, finish, check, protect, vector, return.*

The device raises the interrupt line on the control bus ✓. The processor **completes the instruction it is currently executing** ✓, then detects the interrupt at the end of the fetch–decode–execute cycle ✓. It **saves the current state** — the program counter and registers — onto the stack ✓. It identifies the source, uses the **interrupt vector table** to find the address of the matching **interrupt service routine**, and jumps to it ✓. When the ISR finishes, the saved state is **restored from the stack** and the original program **resumes from exactly where it stopped** ✓.

Six marks, six sentences, and the two most-dropped are the quiet ones: *finishes the current instruction* and *checked at the end of each cycle*. Examiners read "the CPU stops immediately" as evidence you have never met step 2.

## Worked example 2 — classify, then justify

> *(a) State **two** different causes of an interrupt.* **[2]**
> *(b) A printer generates an interrupt when it runs out of paper. Explain **one benefit** of using an interrupt rather than polling for this.* **[2]**
> *(c) Explain why interrupts are given **priorities**.* **[2]*

*Tool: the causes table + the speed-gulf argument + rank-by-cost-of-delay.*

**(a)** Any two families: an I/O device signalling an event (printer out of paper) ✓; a timer signal ✓; a hardware fault such as power failure; a program error such as division by zero; a system call. *(Two different families — two device examples score one.)*

**(b)** Out-of-paper is rare and unpredictable, so with polling the CPU would ask the printer continuously and almost every answer would be "no" — wasted work ✓. With an interrupt the CPU does useful work until the event actually happens, and responds only then ✓.

**(c)** Several interrupts can occur at the same time (or during another ISR) ✓; priorities ensure the most urgent — where delay is most costly, like power failure — is handled first, while the rest wait safely ✓.

## Misconceptions

> [!warning] "The interrupt stops the CPU immediately, mid-instruction."
> Never. The current instruction always completes; the check happens at the **end of each fetch–decode–execute cycle**. You finish the sentence, then answer the door. (An instruction abandoned halfway would leave a scene no one could restore.)

> [!warning] "The ISR runs alongside my program."
> One core runs one instruction stream. During the ISR, your program is *paused* — state on the stack, going nowhere. The appearance of simultaneity is time-slicing, the same illusion the timer interrupt builds multitasking from.

> [!warning] "Interrupts come from hardware."
> Also from software — twice over. A program's own error raises an **exception** (division by zero), and a program deliberately interrupts itself with a **system call** to ask the OS for service. The doorbell rings from inside the house as often as outside.

> [!warning] "Interrupts are simply better than polling."
> Usually — for rare, unpredictable events. But each interrupt buys a context switch, so at very high event rates (a network card at millions of packets a second) systems deliberately fall back to *scheduled polling* — batching thousands of events per look. And a tight polling loop has perfectly *predictable* timing, which some hard-real-time controllers prize over efficiency. The trade is rare-events-favour-interrupts, floods-favour-polling — name the trade, not a winner.

## Beyond the syllabus

**Apollo's 1202, now legible.** Recall from [[Embedded Systems]]: during the Apollo 11 descent, a misconfigured radar flooded the guidance computer with spurious signals. You can now read the save exactly — the flood was an **interrupt storm**, each pulse demanding its context switch until no time remained for real work. The computer's response was priority made policy: shed every task below the deadline-critical ones, keep the engine burning, and raise alarm 1202 — *overloaded, but doing exactly what it should*. The mechanism in this card, graded under the harshest exam ever set.

**The tap became a message.** The physical interrupt *wire* is disappearing: on modern PCIe systems a device signals by *writing to a special memory address* — a *message-signaled interrupt* — so the tap on the shoulder is itself now a packet on the bus. The idea survives its own hardware, which is how you know it was the idea that mattered.

**Many cores, many doorbells.** Recall that a modern CPU has several cores ([[Pipelining and Simultaneous Multithreading]]) — so *whose* shoulder does a device tap? A dedicated **interrupt controller** sits between the bells and the cores like a switchboard operator: each core has its own local controller (and its own mask, and its own private **timer** — every core gets its own metronome and schedules its own work), while a shared routing stage decides which core receives each device's interrupts. The routing is a real performance lever: pin the network card's interrupts to the core whose cache already holds the connection data, and the packets land warm. Best of all, the cores can ring **each other**: an *inter-processor interrupt* is one core tapping another's shoulder — "I changed the memory map, flush your translations" (the OS's dramatic name for this: *TLB shootdown*) or "you have a new task, reschedule." The doorbell system, given many readers, became a small telephone exchange.

**The idea escaped the hardware entirely.** Operating systems offer programs *signals* (a Ctrl-C is an interrupt delivered to a process); language runtimes offer *event handlers*; and every GUI program is one big vector table — "when the user clicks *this*, run *that*." The interrupt pattern — don't watch, be told — became one of software's deepest habits. Even the async/await style in modern languages is the bookmark trick, rebuilt in software: suspend here, protect the scene, resume when the slow thing finishes.

**One last look at the wire.** The interrupt line is an *asynchronous* signal from a device with its own clock, landing in a CPU that samples on the beat — exactly the danger studied in [[Clock Domains and Metastability]]. Real interrupt inputs pass through synchronizer flip-flops before the flag is trusted. Even the doorbell needs debouncing.

## Exam Notes

| Board | Where it appears | What they want |
|---|---|---|
| **Cambridge 0478 IGCSE** (§4.1.4) | Paper 1 | The **role and operation** of interrupts at IGCSE depth: what an interrupt is (a signal to the processor needing immediate attention), *causes* (two or three from different families), and the operation — current task paused, state saved, ISR services the interrupt, task resumes. Often paired with the OS material of §4.1; the polling contrast from §3.2 (buffers + interrupts moving data) is fair game together. |
| **Cambridge 9618 A-Level** (§4.1) | Paper 1/3 | The named LO bullets verbatim: **possible causes**, **applications**, **use of an ISR**, **when interrupts are detected during the F-E cycle** (end of each cycle, after the current instruction completes — the discriminating mark), and **how they are handled** (save state → vector to ISR → restore). Worked example 1 is the staple form. |
| **Cambridge 9618 A-Level** (§16.1) | Paper 3 | The kernel **as an interrupt handler**: the timer interrupt driving **low-level scheduling** — each tick runs the scheduler, saving one process's context and restoring another's. Pre-emptive multitasking = the timer interrupt applied relentlessly. Scheduling *policies* (round robin, SJF…) are examined with [[Operating Systems]] material. |
| **Cambridge 9618** (§15.1) | Paper 3 | One bullet compares **interrupt handling on RISC vs CISC** processors — held for [[CISC vs RISC]], where it belongs with the pipeline story. |
| **IB CS** | — | Not separately named. Interrupts surface inside A1.3's operating-systems scenarios; the mechanism vocabulary here answers them, but no IB statement demands the register-level trace. |
| **AP CSA** | — | Not examined (Java-only). |

**The two marks candidates drop:** "finishes the current instruction first" and "detected at the end of each F-E cycle." Both are step-2/step-3 of the mechanism — the quiet steps. Rehearse them by name.

## Connections

- **Builds on:** [[CPU Architecture and the Fetch-Execute Cycle]] — the control bus carries the signal, and the cycle's hidden fourth beat is where it is heard; [[Input and Output Devices]] — the speed gulf that makes polling wasteful, the buffer + interrupt partnership, DMA's one-interrupt finale, and the USB "the bus polls, the CPU is interrupted" resolution; [[Embedded Systems]] — sleep-until-interrupt as the idiom of every sealed controller, and latency as the real-time budget.
- **Leads to:** [[Operating Systems]] — the kernel as a lifelong interrupt handler: scheduling policies, system calls as the door into privileged mode; [[CISC vs RISC]] — how instruction-set philosophy changes what "finish the current instruction" costs.
- **Kindred:** [[Clock Domains and Metastability]] — the interrupt line is an asynchronous signal entering a clocked world, and it is synchronized like one; [[Pipelining and Simultaneous Multithreading]] — what a context switch really disturbs.
