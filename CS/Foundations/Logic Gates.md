---
chinese: 逻辑门 (luójí mén)
prerequisites:
  - "[[Logic]]"
  - "[[Set Operations]]"
  - "[[Truth Table (Vocab)]]"
leads_to:
  - "[[Half-Adder and Full-Adder]]"
  - "[[Boolean Algebra]]"
  - "[[Karnaugh Maps]]"
  - "[[Flip-Flops]]"
  - "[[Recursion]]"
  - "[[Number Bases]]"
  - "[[Bitwise Operations]]"
  - "[[Pipelining and Simultaneous Multithreading]]"
  - "[[CPU Architecture and the Fetch-Execute Cycle]]"
  - "[[RAM and the Memory Hierarchy]]"
  - "[[Lewis Carroll the Mathematician]]"
  - "[[The Boolean-to-Silicon Bridge]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/logic
  - domain/digital-circuits
  - level/IGCSE
  - level/A-Level
  - curriculum/Cambridge-0478
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - syllabus/IB-CS-A1-2
  - syllabus/0478-10-1
  - syllabus/0478-10-2
  - syllabus/0478-10-3
  - syllabus/0478-10-4
  - syllabus/9618-3-2
  - syllabus/9618-15-2
  - type/deep
  - type/definition
  - type/theorem
  - type/proof
  - notation/AND-dot
  - notation/OR-plus
  - notation/NOT-bar
  - notation/XOR-circled-plus
  - notation/Sheffer-stroke
  - misconception/NAND-is-just-a-shortcut
  - misconception/XOR-is-OR
  - misconception/gates-store-state
  - misconception/circuit-equals-truth-table-uniquely
---

# Logic Gates 逻辑门

## Definition

A **logic gate** is a physical device — a tiny patch of silicon — that takes one or more electrical inputs and produces an electrical output, where each signal is interpreted as either **1** (high voltage, typically ~3.3 V or 5 V) or **0** (low voltage, ~0 V).

Every gate computes a *fixed Boolean function*. Give it the same inputs twice and you get the same output — gates are memoryless and deterministic. The function each gate computes is exactly one of the **logical connectives** you already met in [[Logic]] — AND, OR, NOT, and their cousins — translated from chalkboard truth-functional symbols ($\land, \lor, \lnot$) into hardware.

This is the bridge. Logic on paper is propositions about truth and falsity; logic in silicon is voltages about high and low. **The rules are identical**, and that identity is what makes a computer possible.

### 中文锚点

**逻辑门 (luójí mén)** = 硬件层面实现布尔运算的电子元件。

| English | 中文 | Connective | What it computes |
|---|---|---|---|
| AND | 与门 (yǔ mén) | $A \cdot B$, $A \land B$ | 1 iff *both* inputs are 1 |
| OR | 或门 (huò mén) | $A + B$, $A \lor B$ | 1 iff *at least one* input is 1 |
| NOT | 非门 (fēi mén) | $\overline{A}$, $\lnot A$ | flips 1 ↔ 0 |
| NAND | 与非门 (yǔ fēi mén) | $\overline{A \cdot B}$ | the negation of AND |
| NOR | 或非门 (huò fēi mén) | $\overline{A + B}$ | the negation of OR |
| XOR | 异或门 (yìhuò mén) | $A \oplus B$ | 1 iff *exactly one* input is 1 |

中文计算机课早就讲过这些符号，但中文教材偏重"记住真值表"。本卡的英文版本要求学生学会**两个深的事情**:
1. **从真值表反向构造电路** (从结果倒推到原因 — 这是 hunter 的核心动作)
2. **理解 NAND 的万能性** — 一种门就能搭出全部数字电路，是 Intel/AMD CPU 真正的物理基础

这两件事中文物理教材几乎不讲，是英语 0478/9618 试卷的真正考点。

---

## The six standard gates

Each gate has a **symbol** (distinctive shape used in circuit diagrams), a **truth table** (its complete behavioural specification), and a **Boolean expression** (algebraic shorthand).

![[logic-gates-six-symbols.svg|720]]

### AND — both must be true

$$F = A \cdot B \qquad \text{or} \qquad F = A \land B$$

| $A$ | $B$ | $A \cdot B$ |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

*Intuition.* Two switches in series — the bulb lights only when *both* are closed.

### OR — at least one must be true

$$F = A + B \qquad \text{or} \qquad F = A \lor B$$

| $A$ | $B$ | $A + B$ |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

*Intuition.* Two switches in parallel — the bulb lights when *either* is closed (or both).

> [!warning] The "or" is inclusive
> In everyday English, "tea or coffee?" usually means *one or the other, not both*. In logic and digital circuits, "or" means **at least one, possibly both** (inclusive OR). For the exclusive version — *exactly one, not both* — we have a separate gate: XOR.

### NOT — flip the input

$$F = \overline{A} \qquad \text{or} \qquad F = \lnot A$$

| $A$ | $\overline{A}$ |
|:-:|:-:|
| 0 | 1 |
| 1 | 0 |

The only single-input gate among the six. Symbol: a triangle followed by a small circle (the "bubble"). The bubble alone means negation; you'll meet it again on NAND and NOR.

### NAND — "not AND"

$$F = \overline{A \cdot B}$$

| $A$ | $B$ | $\overline{A \cdot B}$ |
|:-:|:-:|:-:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

*Read this carefully:* NAND is the **negation of AND**. Output is 0 only when both inputs are 1; output is 1 in every other case. The Boolean symbol is the AND with an overbar on top (or equivalently AND followed by NOT).

NAND is the **single most important gate in this card** — see the universality section below.

### NOR — "not OR"

$$F = \overline{A + B}$$

| $A$ | $B$ | $\overline{A + B}$ |
|:-:|:-:|:-:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

Output is 1 only when *both* inputs are 0; output is 0 in every other case. The OR's evil twin.

### XOR — exclusive OR

$$F = A \oplus B$$

| $A$ | $B$ | $A \oplus B$ |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

XOR is 1 when the inputs **differ**, 0 when they **match**. The everyday "tea or coffee, not both" version of "or." It's also the **adder bit without carry** — when you add two bits, the sum-bit (modulo 2) is the XOR (see [[Half-Adder and Full-Adder]] for the full arithmetic story).

> [!warning] XOR is not OR
> Students misread $A \oplus B$ as $A + B$ all the time. The give-away difference is the bottom-right cell: $1 \oplus 1 = 0$ but $1 + 1 = 1$. If both inputs are 1, OR says yes, XOR says no.

---

## Reading a circuit forward — building a truth table

When you see a circuit diagram, you can find its truth table by propagating values from inputs to outputs. The procedure is the same for any circuit, no matter how complicated:

1. **List every input combination.** For $n$ inputs, there are $2^n$ rows.
2. **For each combination, walk the gates in order from inputs to outputs.** At each gate, look up the output from the truth table.
3. **Write the final output column.** That's the truth table of the whole circuit.

*Example.* The circuit $F = (A \cdot B) + \overline{C}$ has three inputs and one output. Step through all eight rows:

| $A$ | $B$ | $C$ | $A \cdot B$ | $\overline{C}$ | $F = (A \cdot B) + \overline{C}$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 1 |

That's it. The truth table is the *behavioural fingerprint* of the circuit; two circuits with the same truth table are functionally identical even if their gate-layouts look completely different.

---

## Reading a circuit backward — building a circuit from a truth table

This is the harder direction, and it's where the hunter's edge shows up. Given an arbitrary truth table — any function of $n$ Boolean inputs you can write down — can you always build a circuit that computes it?

**Yes. The Disjunctive Normal Form (DNF) algorithm proves it.**

### The DNF algorithm

Given a target truth table:

1. **Find every row where the output is 1.**
2. **For each such row, write a Boolean term that is 1 *only* on that row.** This is achieved by ANDing together each input (or its negation, if the input is 0 in that row). For example, the row $A=1, B=0, C=1$ contributes the term $A \cdot \overline{B} \cdot C$ — this is 1 *only* when $A=1, B=0, C=1$, and 0 otherwise.
3. **OR all these terms together.** Each term lights up on its single row; the OR collects them. The result is 1 on exactly the rows you wanted, 0 on the others.

That's the entire algorithm. Three operations: AND, OR, NOT. **They suffice for any truth table.**

### Worked example — the majority function

Suppose three judges vote yes/no. The output is 1 if the majority say yes:

| $A$ | $B$ | $C$ | majority |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Four rows have output 1. Each contributes a 3-AND term:

- $A=0, B=1, C=1$ → $\overline{A} \cdot B \cdot C$
- $A=1, B=0, C=1$ → $A \cdot \overline{B} \cdot C$
- $A=1, B=1, C=0$ → $A \cdot B \cdot \overline{C}$
- $A=1, B=1, C=1$ → $A \cdot B \cdot C$

ORed:

$$\text{majority}(A, B, C) = \overline{A} B C + A \overline{B} C + A B \overline{C} + A B C.$$

Build the circuit by drawing four AND gates (each fed by three signals, some via NOT gates) and feeding their outputs into a single 4-input OR gate. Done.

> [!info] DNF is not the most efficient — but it always works
> The DNF circuit for the majority function uses 4 ANDs + 1 OR + 3 NOTs. A clever engineer can simplify (the function turns out to equal $AB + AC + BC$ — three ANDs + one OR, no NOTs). The simplification is the subject of [[Karnaugh Maps]] and [[Boolean Algebra]] (and 9618 §15.2). For now, the message is: **DNF guarantees a circuit exists**, even if it's not minimal.

### Universality of {AND, OR, NOT}

The DNF algorithm has just proved a theorem:

> **Theorem (Universality of basic gates).** Any Boolean function of any number of inputs can be computed by some circuit using only AND, OR, and NOT gates.

This is one of the deepest facts in computer science. It's the reason a computer — which is, at the bottom, a forest of gates wired together — can compute *anything* expressible as a finite-step procedure on bits.

---

## The deep claim — NAND is universal *all by itself*

Here is the move that elevates this card from "list of gates" to a real piece of computer science.

We just saw that AND, OR, NOT together can build any function. But it turns out you don't need three different gate types — **NAND alone suffices**. Every other gate, including AND and OR and NOT, can be built from NAND gates.

> **Theorem (NAND universality).** Any Boolean function can be computed using only NAND gates.

This is not a quirky party trick. It is **the reason real CPUs exist as they do**.

### Proof — build {NOT, AND, OR} from NAND

**NOT from NAND.** Feed the same signal into both inputs of a NAND:

$$\text{NAND}(A, A) = \overline{A \cdot A} = \overline{A}.$$

(Because $A \cdot A = A$ — ANDing a bit with itself gives itself back; check the truth table.)

One NAND gate = one NOT gate.

**AND from NAND.** AND is just NAND followed by NOT. Since NOT is one NAND:

$$\text{AND}(A, B) = \overline{\overline{A \cdot B}} = \text{NAND}(\text{NAND}(A, B), \text{NAND}(A, B)).$$

Two NAND gates = one AND gate.

**OR from NAND.** Use [[Logic|De Morgan's Law]]: $A + B = \overline{\overline{A} \cdot \overline{B}}$. Each $\overline{A}, \overline{B}$ is one NAND (NOT trick), and the outer $\overline{\,\cdot\,}$ is one NAND. Total:

$$\text{OR}(A, B) = \text{NAND}(\text{NAND}(A, A), \text{NAND}(B, B)).$$

Three NAND gates = one OR gate.

Since we just built {NOT, AND, OR} entirely from NANDs, and {NOT, AND, OR} can build any Boolean function (DNF theorem), **so can NAND alone**. NAND is *universal*: one gate type to build everything.

![[logic-gates-nand-universality.svg|720]]

> [!tip] NOR is also universal — by symmetric reasoning
> The same proof, with NORs in place of NANDs, shows that **NOR is also universal**. So is the converse pair. The two universal gates are NAND and NOR; everything else needs at least two distinct gate types.

### Why this is a fact about silicon, not just paper

Real CPUs are built almost entirely from NAND gates (or NOR gates — both work). Intel and AMD don't manufacture chips with a delicate mix of six gate types; they manufacture **a few hundred million NAND transistors** and wire them up. Why?

- **Manufacturing simplicity.** One transistor pattern is dramatically cheaper to mass-produce than six.
- **Yield.** Fewer distinct components means fewer ways for a fab to go wrong.
- **CMOS reality.** In CMOS — the dominant chip technology since the 1980s — NAND and NOR are the *natural* gates. The reason is physics: every CMOS gate is a team of two complementary transistor types, **PMOS** pulling the output high and **NMOS** pulling it low, and that arrangement inherently *inverts* — so AND = NAND + NOT, and the NOT costs extra transistors. (What a transistor actually is, and why doped silicon can act as a voltage-controlled switch at all: [[Semiconductors]].)

So the universality of NAND isn't a piece of trivia: it's the **engineering reason** modern computers look the way they do. Every photograph of a die shows you a forest of NANDs.

---

## The hunter's payoff — what this card teaches you to trace

Two causal traces, the moves a hunter who knows logic gates should be able to do on demand:

1. **Forward trace — output from inputs.** Given any circuit, walk it gate-by-gate from inputs to output. The procedure is mechanical: at each gate, look up the truth table, write down the output, move on. This is exactly the "evaluation" move from [[Logic]] but with hardware semantics.

2. **Backward trace — circuit from output.** Given a desired truth table (or English description like *"output is 1 when at least two of three inputs are 1"*), construct a circuit. The DNF algorithm is the universal hammer. Real engineers then minimise using Boolean algebra, but the existence of *some* circuit is always guaranteed.

These two traces are the bread and butter of every 0478 §10 exam question. They also generalise: replace "logic gate" with "function" and you've described how to evaluate any code (forward) and how to design code from a specification (backward). The same hunter moves apply.

---

## Worked examples

### Example 1 — Forward trace (truth table from circuit)

A circuit is described in words: *"The output $F$ is 1 if input $A$ is 0 AND input $B$ is 1, OR if input $C$ is 1."*

In Boolean: $F = \overline{A} \cdot B + C$.

The truth table (eight rows for three inputs):

| $A$ | $B$ | $C$ | $\overline{A}$ | $\overline{A} \cdot B$ | $\overline{A} B + C$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |

The final column is what matters; the middle columns are scaffolding.

### Example 2 — Backward trace (circuit from truth table via DNF)

A burglar alarm should sound (output 1) when *both* a window sensor $W$ and a motion sensor $M$ fire, **OR** when a panic button $P$ is pressed (regardless of the sensors). Truth table for $W, M, P$ → alarm:

| $W$ | $M$ | $P$ | alarm |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Five rows have output 1. DNF assembly:

$$\text{alarm} = \overline{W}\,\overline{M}\,P + \overline{W} M P + W \overline{M} P + W M \overline{P} + W M P.$$

This *works* — but it's ugly. Boolean simplification (factor out $P$ from four terms, then notice $W M$ swallows what's left) gives the obvious answer:

$$\text{alarm} = W M + P.$$

Two gates: one AND, one OR. (And the unsimplified DNF result is also correct — it's just wasteful.) The lesson: **DNF guarantees you can build the circuit; simplification is a separate problem with its own techniques.**

### Example 3 — Build OR using only NAND gates

Take the recipe from the universality proof:

$$\text{OR}(A, B) = \text{NAND}(\text{NAND}(A, A), \text{NAND}(B, B)).$$

In words: feed $A$ to both inputs of a NAND (this is NOT $A$). Feed $B$ to both inputs of another NAND (this is NOT $B$). Feed those two outputs into a third NAND.

Verify by truth table:

| $A$ | $B$ | $\overline{A}$ | $\overline{B}$ | $\text{NAND}(\overline{A}, \overline{B})$ |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 |

The last column is the OR truth table. ✓ Three NANDs replicate one OR — and we used zero ANDs, zero ORs, zero NOTs in the construction. *The universality is real.*

---

## Beyond syllabus — gates as the bottom of the computational stack

### The Sheffer stroke

In pure mathematical logic, the operator we call NAND has its own name: the **Sheffer stroke**, written $A \mid B$. Henry Sheffer proved in 1913 that this single connective is sufficient to express all of propositional logic — well before silicon gates existed. Sheffer was working in symbolic logic; he had no idea his result would, 50 years later, become the engineering choice for every CPU on Earth.

This is one of the cleanest examples in the vault of **mathematics anticipating its physical realisation**: Sheffer's 1913 paper is the abstract version of Intel's 1970s manufacturing decision, separated by 60 years and zero communication.

### Half-adders, full-adders, and arithmetic from gates

Recall that XOR computes the *sum-modulo-2* of two bits. Pair that with AND, which computes the *carry-out* (because $1+1 = 10_2$, carrying a 1), and you have a **half-adder**:

| $A$ | $B$ | Sum ($A \oplus B$) | Carry ($A \cdot B$) |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Chain half-adders together (with a "carry-in" input on each) and you get a **full-adder**; chain $n$ full-adders together and you have an **$n$-bit ripple-carry adder** — a circuit that adds two $n$-bit binary numbers. Every arithmetic logic unit (ALU) in every CPU starts here. The complete development belongs to [[Half-Adder and Full-Adder]]; for now, the message is: **arithmetic is built out of gates**, not the other way round.

### Reversible computing and quantum gates

Classical NAND **destroys information**: from the output bit alone you cannot reconstruct the two input bits. (Output 1 could come from inputs $00$, $01$, or $10$, three possibilities collapsed to one.) Information loss in physical computation costs energy — Landauer's principle (1961) says erasing one bit at temperature $T$ dissipates at least $k_B T \ln 2$ joules of heat. Real-world CPUs sweat for exactly this reason.

**Reversible gates** keep all the information by outputting more bits. The **Toffoli gate** (a controlled-controlled-NOT) is reversible *and* universal — every classical computation can be done reversibly, at the cost of carrying extra bits along. Reversible computing is also the bridge to **quantum gates**: quantum circuits must be reversible (because quantum evolution is unitary), so the universal quantum gates are reversible cousins of NAND. The standard quantum-universal set is $\{H, T, \text{CNOT}\}$ — Hadamard, π/8, and controlled-NOT. The Toffoli gate itself is universal for *classical* reversible computing but needs supplementation in the quantum case.

The vault won't cover quantum gates in full, but the through-line is clear: **classical Boolean gates → reversible classical gates → quantum gates** is a three-step ladder, and all three rungs are versions of the same underlying idea — composing simple operations to compute anything.

### Karnaugh maps and minimisation

Recall that DNF guarantees a circuit but doesn't minimise it. **Karnaugh maps** (introduced by Maurice Karnaugh in 1953) are a visual technique for systematically simplifying Boolean expressions of up to 4–6 variables. The procedure: arrange the truth table on a 2D grid where adjacent cells differ in exactly one input, then group the 1-cells into rectangular blocks; each block becomes a simplified product term. Karnaugh maps are the workhorse of 9618 §15.2 and they're a great visual companion to the DNF + Boolean algebra route. The dedicated card is [[Karnaugh Maps]].

---

## Formula sheet and exam notes

| Board | Logic gates examined? | Boolean algebra examined? | Karnaugh maps? |
|---|---|---|---|
| Cambridge 0478 | Yes — §10 directly | No (saved for 9618) | No |
| Cambridge 9618 | Yes — §3.2 (basic) and §15.2 (advanced) | Yes — §15.2 | Yes — §15.2 |
| IB Computer Science | Yes — A1.2 "logic gates processing encoded data" | No named statement — gate behaviour + truth tables only | No |
| AP CSA | **No** — AP CSA is Java/OOP, not circuit-level | No | No |
| AQA / OCR / Edexcel A-Level CS | Yes, similar to Cambridge | Yes | Yes |

Exam notes:
- **0478 §10 questions are highly stereotyped:** either "draw the truth table for this circuit" (forward trace) or "draw a circuit for this truth table / description" (backward trace via DNF or simplification). The vault's hunter framing maps directly: master both directions.
- **9618 §3.2 expects familiarity with the six standard gates** plus the ability to read a complex multi-input circuit. §15.2 raises the bar to Boolean simplification and Karnaugh maps.
- **IB CS A1.2** frames gates as *processing encoded data* — expect a circuit fed by binary values from a data-representation context (the same forward/backward traces as 0478, wearing an IB scenario); the six standard gates and truth tables are the working set.
- The **NAND-universality proof** is not directly examined on either board, but it's a 5-mark question on every UK A-Level paper that asks "Explain how AND can be built from only NAND gates." Knowing this prepares you for that question and for first-year university digital-electronics modules.

---

## Connections

- **Mathematical foundation:** [[Logic]] — the same connectives ($\land$, $\lor$, $\lnot$) live as AND, OR, NOT in hardware. Logic gates are the *physical realisation* of propositional logic; this card is what makes [[Logic]] more than chalkboard symbol-pushing.

- **CS application:** [[Bitwise Operations]] — these same gates applied to *every bit of a whole word at once* (AND/OR/XOR/NOT as masks), plus shifts; how the gates become an everyday programming tool.

- **Mathematical extensions:**
   - [[Truth Table (Vocab)]] — the lookup-table notation used throughout this card.
   - [[Set Operations]] — AND/OR are isomorphic to intersection/union on sets; the Boolean algebra of $\{0, 1\}$ and the Boolean algebra of sets are the same algebra.
   - [[Boolean Algebra]] — formal manipulation of AND/OR/NOT expressions; the *minimisation* problem that DNF leaves open.
   - [[Karnaugh Maps]] — visual minimisation technique for up to 4–6 variables.

- **Forward into computer science:**
   - [[Half-Adder and Full-Adder]] — arithmetic from gates; XOR + AND combine into a single-bit adder, then chained for multi-bit arithmetic.
   - [[Recursion]] — a different way of building complex things from simple parts; the dual to "compose gates from simpler gates."

- **Physics floor:** [[Semiconductors]] — the layer beneath the lowest layer here: doping, the p-n junction, and the MOSFET as a voltage-controlled switch. Understand that, and PMOS/NMOS stop being magic names — in principle you could build a working gate from sand upward. No CS syllabus asks for it; it is the floor every card in this bay stands on.

- **History bridge:** [[Stories/The Boolean-to-Silicon Bridge]] — Sheffer 1913 (the algebraic universality of the stroke), Shannon's 1937 MIT Master's thesis (the first to realise Boolean algebra could describe switching circuits, often called *the most important Master's thesis of the twentieth century*), and von Neumann + Turing on the universality of computation. Three classical milestones; one through-line.

- **Beyond all boards:**
   - **Reversible computing** — Landauer, Toffoli, Bennett. Classical NAND destroys information; reversible gates preserve it.
   - **Quantum gates** — Hadamard, T, CNOT; the universal set for quantum circuits. All quantum gates are reversible.
   - **Cellular automata and Wolfram universality** — Rule 110 is Turing-complete using only nearest-neighbour rules; a different route to universality than NAND.

- **Misconception traps cleared:** NAND is **not** "just a shortcut" for AND-followed-by-NOT — it's *the* universal gate. XOR is **not** OR — they differ on $1 \oplus 1$. Logic gates are **stateless** — they don't remember past inputs (that's the job of [[Flip-Flops]], in 9618 §15.2). And two circuits with the same truth table are functionally identical even if they look completely different — the truth table is the canonical invariant.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $A \cdot B$ | `A \cdot B` | AND, multiplicative convention |
| $A \land B$ | `A \land B` | AND, logic convention |
| $A + B$ | `A + B` | OR, additive convention |
| $A \lor B$ | `A \lor B` | OR, logic convention |
| $\overline{A}$ | `\overline{A}` | NOT, overbar convention |
| $\lnot A$ | `\lnot A` | NOT, logic convention |
| $A \oplus B$ | `A \oplus B` | XOR — circled plus |
| $\overline{A \cdot B}$ | `\overline{A \cdot B}` | NAND |
| $\overline{A + B}$ | `\overline{A + B}` | NOR |
| $A \mid B$ | `A \mid B` | Sheffer stroke (= NAND in formal logic) |
| $A \downarrow B$ | `A \downarrow B` | Peirce arrow (= NOR in formal logic) |
| De Morgan: $\overline{A + B} = \overline{A} \cdot \overline{B}$ | `\overline{A + B} = \overline{A} \cdot \overline{B}` | Used in the NAND-from-OR proof |
| De Morgan: $\overline{A \cdot B} = \overline{A} + \overline{B}$ | `\overline{A \cdot B} = \overline{A} + \overline{B}` | The dual |
