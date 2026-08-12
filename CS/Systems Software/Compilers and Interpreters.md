---
chinese: 编译器与解释器 (biānyìqì yǔ jiěshìqì)
prerequisites:
  - "[[Assembly Language]]"
  - "[[CISC vs RISC]]"
  - "[[Operating Systems]]"
  - "[[Recursion]]"
leads_to:
  - "[[Stacks and Queues]]"
  - "[[The Call Stack]]"
tags:
  - subject/computer-science
  - domain/systems-software
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - syllabus/0478-4-2
  - syllabus/9618-5-2
  - syllabus/9618-16-2
  - type/deep
  - misconception/interpreter-translates-line-by-line
  - misconception/compiled-means-faster-development
  - misconception/java-must-be-one-or-the-other
  - misconception/assembler-is-a-small-compiler
  - misconception/rpn-right-to-left
---

# Compilers and Interpreters 编译器与解释器

> *[[Assembly Language]] left the ladder one rung short. A processor executes only its own machine code — yet almost nobody writes machine code, or even assembly. Every program you have ever used began as a **high-level language**: human-shaped text full of names, formulas, and structure that no CPU can execute. Somebody has to translate — and it turns out there are two great ways to do it, as different as translating a novel and interpreting at a summit. Translate the whole book once, and every reading afterwards is fast — but you must finish the whole translation before anyone reads a word. Or interpret live, sentence by sentence — start instantly, stop at the first confusing line — and accept that every reading costs the translation again. That one trade-off runs through this whole card, and the exam questions almost write themselves from it.*

## 中文锚点

| English | 中文 | one-line meaning |
|---|---|---|
| high-level / low-level language | 高级语言 / 低级语言 | human-shaped, machine-independent code vs the processor's own instructions |
| translator | 翻译程序 | any program turning source code into something executable |
| assembler | 汇编器 | the 1-to-1 transcriber: assembly mnemonics → machine code |
| compiler | 编译器 | translates the **whole** program once into machine code |
| interpreter | 解释器 | reads, checks and **executes** the source one statement at a time |
| executable / object code | 可执行文件 / 目标代码 | the compiler's saved output — runs without the source |
| bytecode / intermediate code | 字节码 / 中间代码 | half-compiled code for a virtual machine (Java's move) |
| disassembler | 反汇编器 | the reverse gear: machine code back into assembly mnemonics |
| IDE | 集成开发环境 | editor + translator + debugger in one workshop |
| lexical / syntax analysis | 词法分析 / 语法分析 | source → tokens; tokens → grammatical structure |
| Backus–Naur Form (BNF) | 巴科斯范式 | a notation for writing a language's grammar as rules |
| Reverse Polish Notation (RPN) | 逆波兰表示法 | operators *after* operands — no brackets, no precedence, stack-ready |

## Three translators, two philosophies

**The assembler** you have met: assembly is machine code wearing names, so the assembler is a **transcriber** — one mnemonic, one instruction, the 1-to-1 rule of [[Assembly Language]]. Mechanical, almost humble.

High-level languages break the 1-to-1 deal on purpose: one line — `total = price * qty + tax` — *designs into* many instructions, and the translator must choose registers, order operations, and lay out memory. Hence the programmer's comeback — a boast that lands twice, because 高级 means both *high-level* and *high-class*, and both readings are accurate: the higher the language, the further from the machine, and the fancier it sounds.

![[premier-language-comic.png|700]]

*First class rides high above the machinery — but nothing moves until the engine room below the waterline turns the fancy line into shovelfuls of machine code. The 高级 in 高级语言 is doing exactly the work it does on this ship.*

One glance at who translates what, and in which direction:

| translator | direction | what survives afterwards |
|---|---|---|
| **assembler** | assembly → machine code | the machine-code program, transcribed 1-to-1 |
| **compiler** | high-level → machine code | a saved **executable** — runs forever without the source |
| **interpreter** | high-level → **actions** | nothing — it executes; no translated version ever exists |

Going back *up* the ladder is a different machine: a **disassembler** turns machine code back into assembly mnemonics — how you inspect a program you have no source for. (A **memory dump** is not a translation at all: it is a raw printout of memory contents in [[Number Bases|hex]] — a snapshot to *read*, which a disassembler can then make sense of.) But nothing climbs reliably all the way back to the high-level source — the names and comments were discarded in translation — which is exactly why shipping only the executable keeps your source private.

Two philosophies compete for the high-level job:

- **The compiler translates the whole book once.** It reads the entire program, checks it, and produces a complete **machine-code executable** saved to disk. Translation happens *once, before running*; running afterwards involves no translator at all — the executable is a native citizen of the processor.
- **The interpreter is the live interpreter at the summit.** It reads one statement, checks it, **executes it immediately** — and here is the point the A-Level LO makes verbatim: *without producing a translated version*. Nothing is saved. The interpreter doesn't emit machine code for your line; it *performs* your line, by calling its own built-in routines (your `print(x)` triggers the interpreter's already-compiled printing machinery). Close the session and nothing remains but the source.

![[compiler-vs-interpreter.svg|700]]

### The trade, priced

| | **compiler** | **interpreter** |
|---|---|---|
| when translation happens | once, before any run | during *every* run, statement by statement |
| execution speed | fast — native code, no translator present | slower — the translation tax is paid every run, every loop iteration |
| start-up | must compile the whole program first (slow for big programs) | starts executing immediately |
| errors | reported **all together** after analysing the whole program; nothing runs until all are fixed | stops at the **first** faulty statement — with the program alive up to that line |
| development loop | edit → recompile → run | edit → run: instant retry — friendlier for learning and experimenting |
| distribution | ship the executable: no translator needed on the user's machine, and the **source stays private** | users need the interpreter installed, and (classically) receive your source |
| portability | recompile for each processor/OS | the same source runs anywhere the interpreter exists |

The justify-the-choice questions on both boards resolve by matching the column to the scenario: a **game shipped to millions** wants compilation (speed, no dependencies, source protected); a **beginner learning to code** or a **script being tinkered with** wants interpretation (instant feedback, stop-at-first-error, no build step); an **embedded controller** ([[Embedded Systems]]) compiles — there is no room for an interpreter on the chip.

### Java's half-and-half — and the virtual machine's other meaning

Put real names on the trade table's columns. **C and C++** live in the compiler column — operating systems, game engines, anything where every nanosecond is billed. **Python and JavaScript** live in the interpreter column: a Python shell or a Jupyter cell *is* the summit interpreter made tangible — type a statement, watch it execute, close the notebook and no translated version exists anywhere. And **Java** planted its flag deliberately in the middle.

The two philosophies hybridise. **Java compiles — but not to machine code.** The compiler produces **bytecode**: instructions for an idealised processor that no silicon implements. Every real machine then runs a **Java Virtual Machine** — an *interpreter for bytecode* — so the same compiled file runs on any platform: *compile once, run anywhere*. The costs split the difference too: bytecode is faster to interpret than raw source (all the parsing is already done) yet still portable. This is the "virtual machine" of language runtimes — a software processor for an invented instruction set — cousin but not twin to [[Operating Systems]]' hardware-emulating VMs. (Python quietly does the same: your `.py` is compiled to bytecode and interpreted by the Python VM. The clean compiler/interpreter dichotomy is a spectrum in the wild — but the *trade-offs* stay exactly as tabled, which is why the exam teaches them.)

## The IDE — the translator's workshop

Nobody uses a bare translator. An **Integrated Development Environment** wraps editor, translator, and debugger into one tool. Both boards inventory this workshop, from two angles — A Level names the **jobs**, IGCSE names the **tools** — and both lists are pure recall marks, so both live here in full.

The four jobs (the A-Level grouping):

- **For coding:** context-sensitive prompts — the editor suggests completions that fit *where you are* (type `person.` and see that object's methods; autocomplete for keywords and your own names).
- **For initial error detection:** dynamic syntax checks — the red squiggle *as you type*, a live mini-parse running between keystrokes, catching the missing bracket before any translate button is pressed.
- **For presentation:** prettyprint (automatic indentation and colour-coding by token role — comments grey, keywords bold; readable structure for free) and expand/collapse of code blocks (fold the finished function away; navigate a thousand lines as an outline).
- **For debugging:** **single stepping** (execute one statement at a time, watching the state change), **breakpoints** (run at full speed *until* the marked line, then freeze), and the **variables/expressions report window** (inspect any value, or watch a chosen expression re-evaluate as you step) — the interpreter's stop-anywhere superpower, offered even for compiled languages.

The seven tools (the IGCSE list — these exact names, each with its purpose):

| tool | its job |
|---|---|
| **code editor** | where the source is written — the workbench itself |
| **run-time environment** | run the program inside the IDE — no separate setup, output right there |
| **translator(s)** | the compiler and/or interpreter, one button away |
| **error diagnostics** | reports *what* went wrong and *where* — line numbers, messages, highlights |
| **auto-completion** | suggests the rest of the name or keyword you started typing |
| **auto-correction** | fixes small slips — mismatched case, an unclosed bracket — as you type |
| **prettyprint** | automatic indentation and colour-coding by token role |

Same workshop, inventoried twice: *error diagnostics* is the four jobs' "initial error detection", *prettyprint* is "presentation", the *run-time environment* is where "debugging" happens. Learn the seven names and the four jobs come free.

## Inside the compiler — the four stages

A2 opens the compiler's lid. Watch one statement travel through — `area = 3 * (w + 2)`:

![[compiler-four-stages.svg|700]]

1. **Lexical analysis** — the source is read as characters and chopped into **tokens**: the atoms of the language (`area` → identifier, `=` → assignment operator, `3` → constant, `(` → punctuation…). Whitespace and comments are discarded here — this is *why* the translator never cares about your spacing — and identifiers are entered into the **symbol table** that later stages (and [[Assembly Language]]'s two-pass assembler, in miniature) rely on.
2. **Syntax analysis** — the token stream is checked against the language's **grammar** (next section) and assembled into a tree reflecting its structure: the `*` owning `3` and the bracketed sum, the `=` owning `area` and the whole expression. A token sequence that fits no grammar rule dies here — this is where "syntax error" actually lives. (Semantic checks — using an undeclared name, adding a string to a number — ride along at this stage.)
3. **Code generation** — the tree is walked and equivalent **object code** is emitted: load `w`, add 2, multiply by 3, store in `area` — the [[Assembly Language]] world, produced mechanically, with real registers chosen.
4. **Optimisation** — the code is improved without changing its meaning: compute constant expressions at compile time (`60 * 60 * 24` becomes `86400` — *constant folding*), hoist unchanging work out of loops, delete code that can never run. The program you wrote for clarity becomes the program the machine deserves. ([[CISC vs RISC]]'s bet, honoured: the whole RISC philosophy assumed a compiler this clever.)

## Writing the grammar down — BNF

Stage 2 checked tokens "against the grammar" — but what *is* a grammar, concretely? A set of rules, and **Backus–Naur Form** is the notation for writing them. Three symbols do everything: `::=` means *is defined as*, `|` means *or*, and `<angle brackets>` name the things being defined:

```
<digit>    ::= 0|1|2|3|4|5|6|7|8|9
<integer>  ::= <digit> | <digit><integer>
<signed>   ::= <integer> | +<integer> | -<integer>
```

Read the second rule twice — it is the important one. An integer is *a digit, or a digit followed by an integer*: the rule refers to itself, and that **recursion** ([[Recursion]], wearing grammar's clothes) is how three lines describe the infinite set of all integers. `407` parses as `<digit 4><integer 07>` → `<digit 0><integer 7>` → `<digit 7>` — the recursion unwinding exactly like the base-case descent it is.

The examined skills: **read** a BNF definition and decide whether a given string is valid (trace it against the rules, greedily and honestly); **write** BNF for a small language ("define `<variable>` as a letter followed by up to two digits"); and know that **syntax diagrams** (railroad diagrams — boxes for the named things, circles for literal symbols, loops for repetition) express exactly the same rules pictorially. One grammar, two costumes.

## Reverse Polish Notation — expressions without brackets

Ordinary ("infix") notation puts operators *between* operands — and immediately needs brackets and precedence rules to say what `2 + 3 * 4` means. **RPN** (postfix) puts each operator **after** its operands, and the entire apparatus of brackets and precedence evaporates: the order of symbols *is* the order of work.

$$(2 + 3) \times 4 \;\;\longrightarrow\;\; 2\;3\;+\;4\;\times$$

**Evaluation is a stack discipline** ([[Stacks and Queues]] doing its signature work), one rule long: *read left to right — push numbers; on an operator, pop two, apply, push the result.*

| read | action | stack |
|---|---|---|
| `2` | push | 2 |
| `3` | push | 2, 3 |
| `+` | pop 3 and 2 → 5, push | 5 |
| `4` | push | 5, 4 |
| `×` | pop 4 and 5 → 20, push | 20 |

One pass, no lookahead, no brackets — which is exactly why translators love it: the syntax tree from stage 2, read leaves-first (post-order), *is* the RPN, and generating stack code from it is mechanical. Watch a longer one run:

![[compiler-rpn-stack.mp4]]

**The order discipline** (where the marks are lost): for `-` and `÷` the two pops are not symmetric — the **first pop is the right-hand operand, the second pop is the left**: reading `8 5 -`, you pop 5 then 8 and compute $8 - 5 = 3$, never $5 - 8$. And converting infix → RPN by hand: bracket the infix fully according to precedence, then move each operator to just after its bracket's contents — $a + b \times c$ → $a\;(b\;c\;\times)\;+$ → `a b c × +`.

## Worked examples

### Example 1 (0478 / 9618 AS — justify the translator)

> A company sells photo-editing software to the public. A university teaches first-year programming. For each, state with justification whether a compiler or an interpreter is more appropriate.

*Tool: the trade table, matched to the scenario.*
**The company: a compiler.** The product runs fast as native code; customers need no translator installed; and shipping only the executable keeps the source code private. **The university: an interpreter.** Students get instant run-after-edit feedback with no build step, and execution stops at the first faulty statement with the program alive up to that line — errors surface one at a time, in running context, which is how beginners learn.

### Example 2 (9618 A2 — the four stages on one line)

> Describe what happens to the statement `total = rate * 60` at each stage of compilation.

*Tool: the pipeline, stage by stage.*
**Lexical analysis:** the characters become tokens — identifier `total`, operator `=`, identifier `rate`, operator `*`, constant `60`; spacing is discarded; `total` and `rate` are recorded in the symbol table. **Syntax analysis:** the tokens are checked against the grammar and built into a tree — `=` at the root with `total` and the `*` expression beneath it; an illegal sequence (say `total = * rate`) would be rejected here. **Code generation:** the tree becomes object code — load `rate`, multiply by 60, store to `total`. **Optimisation:** the code is tightened without changing meaning — were the right side `60 * 60`, the compiler would fold it to `3600` at compile time rather than compute it on every run.

### Example 3 (9618 A2 — RPN, both directions)

> (a) Convert $(7 - 3) \times (2 + 4)$ to RPN. (b) Evaluate the RPN expression `6 2 + 5 1 - ×` showing the stack.

*Tool: operators move to just after their operands.*
(a) $7\;3\;-\;2\;4\;+\;\times$.

*Tool: push numbers; operator pops two (first pop = right operand), pushes result.*
(b) push 6, push 2 → `+` pops 2, 6 → push **8** → push 5, push 1 → `-` pops 1, 5 → $5 - 1 =$ push **4** → `×` pops 4, 8 → push **32**. Answer: **32** — and note the `-` step: second pop on the left.

## Common Misconceptions (Teaching Notes)

### 1. "An interpreter translates the program line by line"

Half wrong, and the A2 LO exists to catch it: an interpreter **executes** line by line *without producing a translated version* — it performs each statement using its own routines and saves nothing. **Fix:** the summit interpreter — the delegates' words cause actions in the room, but no translated document exists afterwards. If a translated copy were saved, you'd have a compiler.

### 2. "Compiled means faster"

Faster **execution** — slower **development loop** (edit → recompile → run, and no fixing anything until *every* reported error is cleared). **Fix:** always attach the noun: fast *running* vs fast *iterating*, and let the scenario say which one is being bought.

### 3. "So is Java compiled or interpreted?"

Yes. Compiled to **bytecode**, which a virtual machine interprets — deliberately capturing halfway benefits (parse once, run anywhere). **Fix:** the two philosophies are endpoints of a spectrum, not a partition of the world; exam answers should name *what is compiled into what*, and *what interprets it*.

### 4. "The assembler is just a small compiler"

Different species: the assembler **transcribes** 1-to-1 (each mnemonic *is* an instruction); the compiler **designs** 1-to-many (choose instructions, registers, order). **Fix:** [[Assembly Language]]'s rule — if the translation involves *decisions*, it's compilation.

### 5. "RPN is evaluated right-to-left" / operands grabbed backwards

RPN's whole point is a single **left-to-right** pass; and on `-` or `÷`, the *first* pop is the **right** operand. **Fix:** drill `8 5 -` = 3 aloud ("pop 5, pop 8, eight minus five") — one rehearsed example inoculates the habit.

## Exam Notes

### Cambridge 0478 — §4.2 (IGCSE)

- **§4.2.1–2:** high-level vs low-level languages (machine-independence, readability, one-to-many vs one-to-one) and why each is used; assembly + the assembler at IGCSE depth ([[Assembly Language]] carries the deep version). **§4.2.3–4:** compiler and interpreter *operation* described, and the advantages/disadvantages both ways — the trade table is the whole answer bank, and the syllabus's own summary sentence is quotable as-is: *an interpreter is mostly used when developing a program, and a compiler is used to translate the final program*. **§4.2.5:** the IDE's role plus its **seven named functions verbatim** — code editors, run-time environment, translators, error diagnostics, auto-completion, auto-correction, prettyprint — each *with its purpose*, not as a bare list (the seven-tool table above is the mark scheme's shape).

### Cambridge 9618 — §5.2 (AS)

- The **need** for each of the three translators; compiler-vs-interpreter benefits, drawbacks, and *justify for a scenario*; **Java (console mode)** as the named partially-compiled-partially-interpreted case — say "bytecode" and "virtual machine" and you have the marks; the **IDE features by their four jobs** (coding / initial error detection / presentation / debugging — the syllabus's own grouping, worth reproducing verbatim).

### Cambridge 9618 — §16.2 (A2)

- The interpreter LO in its exact shape: executes **without producing a translated version**. The **four compilation stages** named and described with what each consumes and produces (characters → tokens → tree → object code → better object code); Example 2's shape is the standard question. **BNF**: read, validate a string, write small grammars — recursion in rules is expected, not exotic. **RPN**: convert both directions and **evaluate showing the stack** — Paper 3 bankers, and the stack trace table is the mark scheme's shape.

### Other boards

- **AP CSA:** Java-only and assumes the toolchain — the compile step appears as vocabulary (compiler errors vs runtime errors), no translator theory. **IB CS 2027:** translators are not a named statement list; this card is depth behind their programming units.

## Beyond the syllabus

> [!info] JIT — the interpreter that learns to compile
> The modern engines running JavaScript and Java bytecode dissolve the dichotomy from the interpreter's side: start interpreting instantly (the interpreter's virtue), *watch* which functions run hot, and **compile just those to native code mid-run** — optimised using facts only visible at runtime ("this variable has been an integer ten thousand times — compile for integers, keep a trapdoor in case"). That is **Just-In-Time compilation**, and it is why the language inside your browser, once a byword for slowness, now runs within sight of C. The trade table's two columns turn out to be *phases*, not species.

> [!info] Bootstrapping — who compiles the compiler?
> A compiler is a program — so what translated *it*? Today: the previous compiler. The C compiler is written in C; each version compiles the next — a chain of [[Von Neumann machine]] code-as-data stretching back to some ancestor first assembled by hand. Writing a language's compiler *in that language* is called **self-hosting**, and it is the traditional proof a language has grown up. (The chain has a dark corollary — Ken Thompson's famous "Trusting Trust" lecture shows a corrupted compiler could invisibly corrupt every program it builds, including its own next version. Trust, too, bootstraps.)

> [!info] Why inventing a language got cheap — the front/back split
> Modern compiler suites (LLVM, GCC) split at the middle: a **front end** per language (lexing, parsing, the language's rules) feeding one shared **intermediate representation**, and a **back end** per processor (code generation, optimisation) consuming it. Write one new front end and your brand-new language instantly compiles, optimised, for x86, ARM and RISC-V; write one new back end and every language arrives on your new chip. The four stages didn't just describe one program — they became an industry's plug interface, and it is why the 2010s could afford a Cambrian explosion of languages (Swift, Rust, Julia, Zig) where the 1980s could not.

## Connections

- **Builds on:** [[Assembly Language]] — the assembler, the 1-to-1 rule this card's translators break on purpose, and the machine-code destination of stage 3; [[CISC vs RISC]] — RISC's founding bet was that compilers, not humans, write the assembly: this card is the bet's other half, honoured in stage 4; [[Operating Systems]] — the bay's government: it loads what the compiler produced, supplies the libraries the linker leans on, and hosts the hardware-level VMs this card's bytecode VMs are cousins of; [[Recursion]] — BNF's self-referring rules are recursion writing grammar.
- **Leads to:** [[Stacks and Queues]] — RPN's engine: the pop-two-push-one discipline as a named, disciplined structure; [[The Call Stack]] — the call stack every running program lives on, frames and all.
- **Kindred:** [[Von Neumann machine]] — code-as-data is what makes translators possible at all: a compiler is a program whose *output* is a program; [[Embedded Systems]] — where compilation is the only option on the chip.
