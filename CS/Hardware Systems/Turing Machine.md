---
chinese: 图灵机 (Túlíng jī)
prerequisites:
  - "[[Recursion]]"
  - "[[Turing at Bletchley]]"
  - "[[von Neumann the Martian]]"
leads_to:
  - "[[Von Neumann machine]]"
  - "[[P vs NP]]"
  - "[[Gödel's Incompleteness Theorems]]"
  - "[[The Turing Test]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/theory-of-computation
  - domain/computer-architecture
  - level/A-Level
  - level/university
  - type/deep
  - type/theorem
  - type/proof
  - misconception/turing-machine-is-a-real-machine
  - misconception/halting-problem-is-just-hard
  - misconception/turing-built-the-first-computer
---

# Turing Machine 图灵机

> *In 1936, before a single electronic computer existed, a 24-year-old asked a question nobody had pinned down: what does it actually mean to **compute** something? His answer wasn't a circuit. It was a person — a clerk stripped down to almost nothing, with an endless strip of paper, one symbol in view, a handful of moods, and a fixed rule-book. That imaginary clerk is the most important machine never built. Every device you own is a physical approximation of it.*

## Definition — the machine made of rules

The word **computer** used to be a *job title*. Until the 1940s, a "computer" was a person — very often a woman — who sat with paper and pencil and worked through a calculation by following fixed steps. Turing's move was to ask: *what is the absolute minimum such a person needs in order to compute anything at all?* Strip away intuition, creativity, memory of the outside world. What's left?

A **Turing machine** is that minimum, made precise. It has just five ingredients:

- An infinite **tape** divided into **cells**, each holding one symbol from a finite alphabet (think `0`, `1`, and a *blank*). The tape is the machine's entire memory and scratch paper at once.
- A **read/write head** parked over exactly one cell. It can read that cell's symbol, overwrite it, and then shuffle one cell **left** or **right**.
- A finite set of **states** — the clerk's possible "moods." Finite is the key word: however long the computation, the machine is only ever in one of a fixed, bounded set of internal conditions.
- A **transition function** $\delta$ — the rule-book. Given *(current state, symbol under the head)*, it dictates *(symbol to write, direction to move, next state)*. This finite table **is the entire program**.
- A **start state** and one or more **halting states**. When the machine enters a halting state, it stops, and whatever is left on the tape is the answer.

> **The metaphor:** a Turing machine is *a clerk with an infinite notebook who has forgotten everything in the world except which of finitely many moods he is in and the single symbol his pencil is touching.* Every decision he ever makes is a lookup in a fixed table. That is all computation is.

Formally it's a 7-tuple $M = (Q, \Sigma, \Gamma, \delta, q_0, b, F)$ — states $Q$, input alphabet $\Sigma$, tape alphabet $\Gamma$, transition function $\delta$, start state $q_0$, blank symbol $b$, halting states $F$ — but the five plain-English ingredients above *are* that tuple. Don't let the notation hide how little machinery this is.

## 中文锚点

**图灵机**是 1936 年阿兰·图灵为了定义「**什么叫可计算**」而设想的抽象机器——不是电路，而是把一个用纸笔做计算的「人」抽象到极简。它由五部分组成：一条**无限长的纸带**（分成格子，每格一个符号，如 `0`/`1`/空白），一个能**读、写、左右移动**的**读写头**，一组**有限的状态**（机器的「心情」），一张**转移函数表** $\delta$（规则手册：看到「当前状态 + 当前符号」，就决定「写什么、往哪移、进入哪个状态」），以及一个**起始状态**和若干**停机状态**。这张有限的规则表**就是整个程序**。

惊人之处有三：(1) 这么简陋的机器能算出任何「可计算」的东西；(2) 存在一台**通用图灵机**，把别的机器的「规则表」当作纸带上的数据读进来就能模拟它——这正是「程序即数据」、现代存储程序计算机的雏形；(3) 有些问题**任何**图灵机都解不了——**停机问题**就是第一个被证明「不可判定」的问题。图灵机是 [[CPU Architecture and the Fetch-Execute Cycle|取指执行周期]] 的理论祖先：图灵 (1936，理论) → 冯·诺依曼 (1945，架构) → 真实 CPU。

![[turing-machine-anatomy.svg|697]]
*The whole machine: an unbounded tape of symbols, a head that reads/writes one cell and steps left or right, and a finite control holding the current state and the rule-book. Nothing else.*

## The transition function — the program is a table

Everything the machine will ever do is frozen into $\delta$. Each rule has the shape

$$\delta(\text{state},\ \text{symbol}) = (\text{new symbol},\ \text{move},\ \text{new state})$$

Read one row aloud: *"If I am in state $B$ and the cell under me holds a `1`, then write a `0`, move Left, and switch to state $B$."* That's it — a single unconditional reflex. A Turing machine has no loops, no variables, no arithmetic built in. **Loops emerge** because a rule can send the machine back to a state it has been in before; **arithmetic emerges** because you can write a table whose reflexes, fired in sequence, happen to add. The richness is in the *trajectory*, never in any single rule.

This is exactly the spirit of the [[CPU Architecture and the Fetch-Execute Cycle|fetch–execute cycle]]: a real CPU also does nothing but "read the thing under the pointer, react according to a fixed rule, advance." The Turing machine is that idea with every inessential part sanded off.

## The blank — the most underrated symbol

The tape alphabet always includes a special **blank**. It is easy to skip past, and it is quietly doing essential work:

- **It marks where the input ends.** With only `0`s and `1`s, the machine could never tell "the data stopped here" from "a long run of zeros." The blank is the punctuation that turns a finite input into a well-defined object sitting on an infinite tape.
- **It is unbounded scratch space that costs nothing.** The tape is infinite, yet at any moment **only finitely many cells are non-blank** — every configuration is *almost everywhere blank*. That one property is what lets an infinite tape still carry a **finite amount of information**, and it is what makes a Turing machine a legitimate object of [[Information Theory|information theory]] rather than an infinity hiding answers somewhere in its tail.
- **It is the tape's "nothing here"** — the empty cell, the ground state.

That thread runs further than it looks: Shannon's measure of information generalises to **von Neumann entropy** for quantum states (the same von Neumann — see [[Von Neumann machine]]), the step from the classical **bit** to the **qubit**. The humblest symbol on the tape is one end of a line that reaches all the way to quantum information.

> [!tip] The game you already know is `0 / 1 / blank`
> A **Go** board is a Turing tape's alphabet made visible: every point is black, white, or **empty** — three symbols, exactly like `0`, `1`, and blank. And Go's **Ko rule** (you may not recreate the previous whole-board position) is a glimpse of something deeper — legality can depend on *history*, not just the stone under your eye, which is precisely why a Turing machine needs a **state** and not only a tape. Three symbols and a rule about the past: enough for a game no one has solved, and enough for a model of all computation.

## A machine you can run by hand — binary increment

Here is a complete, real Turing machine: it takes a binary number on the tape and **adds 1 to it**. (This is precisely what a CPU's program counter does every cycle — `PC + 1` in the [[CPU Architecture and the Fetch-Execute Cycle|FDE]] trace is a binary increment in hardware.) Two states do the whole job:

| State | reads `0` | reads `1` | reads blank `_` |
|-------|-----------|-----------|------------------|
| **A** *(find the right end)* | `0`, R, A | `1`, R, A | `_`, L, **B** |
| **B** *(add one, ripple the carry)* | `1`, –, **HALT** | `0`, L, B | `1`, –, **HALT** |

State **A** just walks right until it falls off the end of the number; state **B** walks back left turning `1`s into `0`s (each is a carry) until it meets a `0` or a blank, which it turns into a `1` and halts. Run it on `1011` (which is 11):

| Step | State | Tape (head in **bold**) | Rule fired |
|------|-------|--------------------------|------------|
| 0 | A | **`1`**`011` | start at the left |
| 1–4 | A | `1011`**`_`** | walk right to the blank |
| 5 | B | `101`**`1`** | hit blank, step Left into B |
| 6 | B | `10`**`1`**`0` | read `1` -> write `0`, carry, move L |
| 7 | B | `1`**`0`**`00` | read `1` -> write `0`, carry, move L |
| 8 | HALT | `1`**`1`**`00` | read `0` -> write `1`, no more carry |

The tape now reads `1100` = 12. The machine added 1, carries and all, using two moods and a four-row rule-book. Notice there is no "addition" anywhere in the rules — addition is what the *path through the table* happens to spell out.

## The Universal Turing Machine — where the computer comes from

Here is the hinge of the whole subject. A machine's rule-table is *itself just a finite string of symbols*. So there is nothing stopping you from writing the description of machine $M$ **onto the tape** of another machine, right next to $M$'s input.

Turing proved you can build one fixed machine $U$ — a **Universal Turing Machine** — that reads such a description and *simulates* it:

$$U(\langle M \rangle,\ w) \;=\; M(w)$$

Give $U$ the encoding $\langle M\rangle$ of any Turing machine and an input $w$, and $U$ computes exactly what $M$ would have computed. **One machine to run them all.**

This is the most consequential idea in computing, and it is the reason the phrase **"the program is just data in memory"** in [[CPU Architecture and the Fetch-Execute Cycle|the FDE card]] is not a slogan but a theorem. You do not build a new machine for each task; you build *one* universal machine and feed it a different description on the tape. That is why your laptop runs a browser, a game, and a compiler without being rewired between them. Turing's 1936 $U$ is the great-grandparent; von Neumann's 1945 stored-program architecture (→ [[Von Neumann machine]]) is the buildable version, where the description and the data finally live in the *same* memory.

> [!info] The lineage in one line
> **Turing (1936)** proved one universal machine can compute anything computable, given the right description on its tape. **von Neumann (1945)** put that description in the same memory as the data. **Every CPU since** is that idea, electrified. (→ [[Von Neumann machine]], [[CPU Architecture and the Fetch-Execute Cycle]].)

## The Church–Turing thesis — what "computable" *means*

In the same eighteen months of 1936, three people defined "computable" three completely different ways: Turing with his machines, **Alonzo Church** with the **lambda calculus** (pure functions), and **Stephen Kleene** with the **general recursive functions** (build-up from base cases). The shock was that **all three define exactly the same class of functions** — each can simulate the others. (The recursion side of this is developed in [[Recursion]]; the lambda calculus appears there too.)

The **Church–Turing thesis** is the claim that this shared class *is* the intuitive notion of "effectively computable" — anything a human could in principle work out by following a finite mechanical procedure, a Turing machine can compute, and vice versa.

It is called a **thesis**, not a theorem, on purpose. The equivalence of the three formal models *is* a theorem (proved). But the identification of that formal class with the fuzzy, intuitive idea of "what can be mechanically computed" is not something you can prove — it's a claim about a pre-mathematical notion. Ninety years of every new model of computation (quantum included) computing nothing *outside* this class is the evidence. So far it has never been broken.

The payoff: **computability is absolute.** "Computable" doesn't depend on your programming language, your hardware, or your era. A problem no Turing machine can solve is a problem *nothing* can solve — and that brings us to the first such problem.

## The halting problem — the first thing no computer can do

Some inputs make our binary-increment machine halt; could a machine make a *mistake* and run forever? More urgently: could we write one program that, looking at *any* program, tells us in advance whether it will halt or loop forever? That would be the ultimate debugger. Turing proved, in the very same 1936 paper, that **it cannot exist**. The proof is short, and it is one of the most beautiful arguments in mathematics.

We argue **by contradiction**. The shape is *"if a halting-decider exists, then a contradiction follows."* The thing we will deny at the end is the existence of the decider.

1. **Suppose** there is a program $H$ that always halts and always answers correctly: $H(P, x)$ returns **HALTS** if program $P$ would halt on input $x$, and **LOOPS** if $P$ would run forever on $x$.
2. Using $H$, build a new program $D$ (for "diagonal") that takes a single program $P$ as its input and does this: it runs $H(P, P)$ — asking "does $P$ halt when fed *its own description*?" — and then deliberately does the **opposite**. If $H$ says $P$ halts on $P$, then $D$ **loops forever**. If $H$ says $P$ loops on $P$, then $D$ **halts**.
3. $D$ is a perfectly ordinary program, so we may feed it *its own description*. Ask the one question that breaks everything: **does $D$ halt on input $D$?**
4. **Case one: suppose $D(D)$ halts.** Then by step 2, when $D$ ran $H(D, D)$ it must have been told "LOOPS" — that is the only branch on which $D$ halts. But $H$ is never wrong, so $D(D)$ must actually loop. It both halts and loops. Contradiction.
5. **Case two: suppose $D(D)$ loops.** Then by step 2, $H(D, D)$ must have answered "HALTS" — the only branch on which $D$ loops. But $H$ is never wrong, so $D(D)$ must actually halt. Again it both halts and loops. Contradiction.
6. Every possibility leads to a contradiction. The only assumption we made was that $H$ exists. Therefore $\boxed{\text{no such } H \text{ can exist}}$ — the halting problem is **undecidable**.

The trick — feed a machine a description of *itself* and make it disagree with its own verdict — is the same **diagonal argument** Cantor used to show the real numbers cannot be listed. Turing turned that piece of set theory into a fact about *machines*: there are perfectly precise yes/no questions ("does this program halt?") that **no algorithm can ever answer in general**. Not "we haven't found the algorithm yet" — *there is no such algorithm, and there never will be.* Mathematics has a hard edge, and Turing found it with a machine made of paper.

![[halting-problem-comic.png|697]]
*The proof has a sense of humour. **H** is the would-be oracle; **D** is the troublemaker built to do the **opposite** of whatever H predicts. Ask H about D running on *itself*, and no answer it gives can avoid coming true backwards — so H melts down.*

The same collision, drawn as a precise diagram:

![[halting-problem-contradiction.svg|697]]
*Assume a perfect decider $H$; use it to build a contrarian $D$ that does the opposite of $H$'s verdict; then ask $D$ about itself. Every branch refutes itself — so $H$ never existed.*

## The same machine, animated — the busy beaver

The clip below runs a real Turing machine called the **3-state busy beaver**: the most productive 3-state, 2-symbol machine that still eventually stops. Watch the head read, write, and step while the finite control changes state and the rule-book row that fires lights up. It starts on a blank tape and — astonishingly — halts after exactly **14 steps**, leaving **six** `1`s behind. Pause on any step:

![[turing-busy-beaver.mp4]]

The busy beaver is the halting problem made tangible. Define $BB(n)$ = the most steps any $n$-state machine can run *and still halt*. $BB(1)=1$, $BB(2)=6$, $BB(3)=14$, $BB(4)=107$ — and then it explodes: $BB(5) = 47{,}176{,}870$ (only proven in 2024, after decades), and $BB(6)$ is already larger than numbers that come up in any physics. The function $BB(n)$ is **uncomputable** — it grows faster than *any* program could ever predict, because computing it would let you solve the halting problem. A three-state machine that halts in 14 steps and one that would take longer than the age of the universe look identical from the outside. That is the halting problem, staring back.

## Common Misconceptions

> [!warning] "A Turing machine is a real, physical machine."
> It is a *mathematical object* — an imaginary clerk used to define computation. Turing never built one and never meant to; the 1936 paper was pure logic, written to settle a problem about formal proof (the *Entscheidungsproblem*). Real computers are *approximations* of it, with finite memory standing in for the infinite tape.

> [!warning] "The halting problem just means halting is hard to check."
> It means something far stronger: **no algorithm can decide it in general, ever** — not a faster computer, not more memory, not a cleverer programmer. It is *undecidable*, not merely difficult. (You can often check specific programs by hand; what's impossible is one method that works for *all* of them.)

> [!warning] "Turing built the first computer."
> No. In 1936 he defined *what computation is*. The wartime [[Stories/Turing at Bletchley|Bombe]] was a special-purpose codebreaking device, not a general computer, and **Colossus** (built by Tommy Flowers, for a different cipher) and the stored-program machines came later. Turing's gift was the *theory* every later machine implements.

> [!warning] "More states or more tapes make a Turing machine more powerful."
> They make it faster or more convenient, never more *capable*. A machine with many tapes, or a two-way infinite tape, or random extra symbols computes exactly the same class of functions as the bare one-tape model. This robustness is part of why the Church–Turing thesis is believable.

## Exam Notes

The Turing machine is **not a named topic** on Cambridge IGCSE 0478 or A-Level 9618 — those treat the *real* processor (the [[CPU Architecture and the Fetch-Execute Cycle|von Neumann model and FDE cycle]]), not the theory of computation. It is included here as the **conceptual ancestor** of everything in the architecture bay, and because it is unavoidable the moment a student goes further:

- **IB CS (2027)** — **not a named statement** anywhere in the published outline: A1.1's computer-organisation strand stops at CPU, memory and the fetch-decode-execute cycle, and no theory-of-computation topic exists. Enrichment behind "general-purpose," exactly as for Cambridge.
- **AP Computer Science Principles** — Big Idea 4 explicitly includes that *some problems cannot be solved by any algorithm* (undecidable problems). The halting problem is the canonical example; this card is the full version of that one bullet.
- **University (first-year CS / "Theory of Computation")** — the Turing machine, the Church–Turing thesis, decidability, and the halting problem are core. Cross-links to formal languages, the Chomsky hierarchy, and complexity (P vs NP) start here.
- **General literacy** — "Turing-complete" is said of any system (a language, a spreadsheet, even some games) powerful enough to simulate a universal Turing machine. It means: *as capable as computation gets.*

For 0478/9618 students this card is enrichment — but it is the single best answer to "why is a computer called *general*-purpose?", which the syllabus does ask.

## Connections

- **Prerequisite / sibling:** [[Recursion]] — the Church–Turing thesis is seeded there; the general-recursive-functions and lambda-calculus halves of the 1936 equivalence live in its beyond-syllabus section. Turing machines are the *machine* third.
- **Operator counterpart:** [[Logic Gates]] — Sheffer's NAND-universality (one *operator* suffices for all logic) is the structural twin of Turing's universality (one *machine* suffices for all computation). Two universality theorems, two decades apart.
- **Leads to (the lineage):** [[Von Neumann machine]] — the 1945 stored-program architecture that made the universal machine buildable; then [[CPU Architecture and the Fetch-Execute Cycle]] — the universal machine ticking in silicon, one fetch–execute step at a time.
- **History:** [[Stories/The Boolean-to-Silicon Bridge]] — Act III is Turing's 1936 machine in its full context (Sheffer -> Wittgenstein -> Turing -> Shannon -> silicon); [[Stories/Turing at Bletchley]] — the man, the war, the codebreaking, and the tragedy the equations leave out.

## Beyond Syllabus

> [!info] Variants that change nothing — and why that matters
> Add a second tape, make the tape infinite in both directions, allow the machine to *guess* (a **nondeterministic** Turing machine that can branch and accept if *any* branch does) — every one of these computes the **same class of functions** as the plain model. A nondeterministic machine can be *exponentially faster* on some problems, but a deterministic machine can always simulate it given enough time. The model is astonishingly **robust**: almost any reasonable definition of "mechanical computation" you write down turns out equivalent. That robustness is the empirical backbone of the Church–Turing thesis.

> [!info] The doorway to P vs NP
> Once "computable" is settled, the next question is "computable *how fast*?" Measuring a Turing machine's steps as a function of input size is exactly [[Big-O Notation|Big-O]] complexity. The class **P** is what a deterministic machine solves in polynomial time; **NP** is what a *nondeterministic* one does. Whether $P = NP$ — whether every problem whose solution is easy to *check* is also easy to *solve* — is the largest open question in computer science, and it is phrased entirely in the language of this card. The hardest problems *inside* NP — the **NP-complete** ones, and the **NP-hard** problems beyond — are where the drama concentrates; the full development is its own card: [[P vs NP]].

> [!info] The same diagonal — Gödel's incompleteness
> Turing's proof is the twin of **Gödel's first incompleteness theorem** (1931): in any consistent formal system rich enough to describe arithmetic, there are **true statements it cannot prove**. The engine is the same self-referential **diagonalisation** — Gödel built a sentence that says *"I am not provable,"* Turing built a machine that does the opposite of whatever it is predicted to do. The halting problem even gives an *independent* route to incompleteness: encode "machine $M$ halts" as a statement of arithmetic; if some formal system could prove every true halting fact, you could decide the halting problem — which is impossible, so some true statements must be unprovable. Computation's hard edge and logic's hard edge are the same edge. Full treatment: [[Gödel's Incompleteness Theorems]].

> [!info] Turing's *other* machine — the Turing Test
> The same man posed a second question that founded a field: not "what can a machine compute?" but "**can a machine think** — or at least convince you that it does?" His 1950 *Imitation Game* — now the **Turing Test** — sidesteps the metaphysics: if you cannot tell the machine from a human across a conversation, on what principled grounds do you deny it thinks? Seventy years on, large language models routinely hold conversations most judges cannot distinguish from a person's — so the test, *as Turing framed it*, is arguably **already passed**. What that does and does not prove is its own card: [[The Turing Test]].

> [!info] Oracles and degrees of unsolvability
> The halting problem is undecidable, but you can imagine a machine handed a magic black box (an **oracle**) that answers it for free. Such a machine is more powerful — yet *it* has its own halting problem that *it* cannot solve. Undecidability comes in an infinite tower of levels (the *Turing degrees*). There is no top.

## LaTeX / Notation Reference

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| $\delta$ | `\delta` | transition function: $(\text{state},\text{symbol}) \to (\text{symbol},\text{move},\text{state})$ |
| $\Sigma$ | `\Sigma` | input alphabet (symbols allowed in the input) |
| $\Gamma$ | `\Gamma` | tape alphabet (input symbols plus blank and any scratch symbols) |
| $Q$ | `Q` | the finite set of states |
| $q_0$ | `q_0` | the start state |
| $F$ | `F` | the set of halting / accepting states |
| $\langle M \rangle$ | `\langle M \rangle` | the *encoding* of machine $M$ as a string — what a universal machine reads |
| $U(\langle M\rangle, w)$ | `U(\langle M\rangle, w)` | a universal machine simulating $M$ on input $w$ |
| $BB(n)$ | `BB(n)` | the busy-beaver function: max steps an $n$-state machine runs and still halts (uncomputable) |
