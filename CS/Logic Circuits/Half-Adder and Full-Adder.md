---
chinese: 半加器与全加器
prerequisites:
  - "[[Logic Gates]]"
  - "[[Number Bases]]"
  - "[[Boolean Algebra]]"
  - "[[Karnaugh Maps]]"
leads_to:
  - "[[Arithmetic Logic Unit]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/logic
  - domain/digital-circuits
  - level/A-Level
  - curriculum/Cambridge-9618
  - curriculum/A-Level
  - syllabus/9618-15-2
  - type/deep
  - type/technique
  - notation/AND-dot
  - notation/OR-plus
  - notation/XOR-circled-plus
  - notation/NOT-bar
  - misconception/half-adder-has-carry-in
  - misconception/xor-is-the-whole-adder
  - misconception/ripple-carry-is-instant
---

# Half-Adder and Full-Adder 半加器与全加器

> **A computer has no "add" instinct.** Arithmetic is not a primitive it was born knowing — it is *built*, one bit-column at a time, out of the handful of gates from [[Logic Gates]]. Adding two bits is one XOR (the digit you write) and one AND (the carry you push left). Everything a machine ever calculates is a tower stacked on that single idea.

## Definition

An **adder** is a combinational circuit that performs binary addition. To see what it must do, add two binary numbers on paper, column by column, right to left, carrying when a column overflows — the same place-value arithmetic you use in denary, now in base 2 ([[Number Bases]]):

$$
\begin{array}{r}
 \;\;0110 \\
+\,0011 \\
\hline
 \;1001
\end{array}
\qquad (6 + 3 = 9)
$$

Each column takes **three** inputs — the two number-bits and a **carry** coming in from the column to its right — and produces **two** outputs — the **sum** digit written below, and the **carry-out** pushed to the column on its left. Build one circuit that does a single column, chain copies of it, and you can add numbers of any width. That single-column circuit is the **full adder**; its simpler cousin, which ignores the incoming carry, is the **half adder**.

### 中文锚点

竖式加法算到十位时，你不能只盯着十位上的两个数，还得看看个位有没有进上来一个 1。电脑做二进制加法也一样：半加器只管把两个比特相加，全加器还把右边传来的进位一起算上。二进制逢二进一，所以两个 1 相加，本位写 0，往左送一个 1。把这样的小电路一列列接起来，每列管好自己、把进位交给左邻居，一串很长的数就加起来了。

### Vocabulary

| English | 中文 | 一句话 |
|---|---|---|
| half adder | 半加器 (bàn jiāqì) | 加**两**个 1 位，无进位输入 |
| full adder | 全加器 (quán jiāqì) | 加**三**个 1 位（含低位进位 $C_{in}$） |
| sum | 和 (hé) | 写在本列下面的那一位 |
| carry-out | 进位 (jìnwèi) | 推给左边一列的那一位 |
| ripple-carry adder | 串行进位加法器 | $n$ 个全加器串起来，进位一级级上传 |

---

## The half adder — two bits, no carry-in

Add two single bits $A$ and $B$. There are only four cases, and one rule you already know: $1 + 1 = 10_2$ — a sum digit of $0$ and a carry of $1$.

| $A$ | $B$ | Carry $= A\cdot B$ | Sum $= A \oplus B$ |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Look at the two output columns and read off the gates from [[Logic Gates]]:

- **Sum** is $1$ when the inputs *differ* — that is **XOR**: $\;\text{Sum} = A \oplus B$.
- **Carry** is $1$ only when *both* are $1$ — that is **AND**: $\;\text{Carry} = A \cdot B$.

$$\boxed{\;\text{Sum} = A \oplus B \qquad \text{Carry} = A \cdot B\;}$$

![[half-adder-circuit.svg|540]]

That is the whole half adder: one XOR, one AND, sharing the same two inputs. It is called *half* an adder because of what it **cannot** do — it has no input for a carry arriving from the column on its right. It can only ever add the very first (rightmost) column of a sum, where there is no carry yet. For every other column you need one more input.

---

## The full adder — three bits in, two bits out

A real column adds **three** things: $A$, $B$, and the **carry-in** $C_{in}$ from the previous column. Three inputs, so $2^3 = 8$ rows:

| $A$ | $B$ | $C_{in}$ | $C_{out}$ | Sum |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

Stare at the two output columns and each turns out to be a function you have already met:

- **Sum $= A \oplus B \oplus C_{in}$.** The sum bit is $1$ when an *odd* number of the three inputs are $1$ — that is exactly what a chain of XORs computes (**parity**). Check the table: rows with one or three $1$s give Sum $=1$.
- **$C_{out} = AB + AC_{in} + BC_{in}$.** You carry when *at least two* of the three inputs are $1$. **That is the majority function** — the very circuit [[Logic Gates]] built by DNF and [[Karnaugh Maps]] minimised by eye to $AB+AC+BC$. It looked like a toy about three judges voting; here is the job it was really holding down all along: **the carry bit of every adder in every computer.** Same three cards, one function, and now it earns its keep.

$$\boxed{\;\text{Sum} = A \oplus B \oplus C_{in} \qquad C_{out} = AB + AC_{in} + BC_{in}\;}$$

### Two half adders make a full adder

You do not have to build the full adder from scratch — one useful construction assembles it from **two half adders and one OR gate**:

![[full-adder-circuit.svg|620]]

1. **First half adder** adds $A$ and $B$: it produces a partial sum $s_1 = A\oplus B$ and a carry $c_1 = A\cdot B$.
2. **Second half adder** adds that partial sum to the carry-in: $\;\text{Sum} = s_1 \oplus C_{in} = A\oplus B\oplus C_{in}$ (correct), and a second carry $c_2 = s_1 \cdot C_{in}$.
3. **OR the two carries:** $\;C_{out} = c_1 + c_2 = AB + (A\oplus B)C_{in}$.

Why is an **OR** enough — could both carries be $1$ at once? No. If $c_1 = AB = 1$ then $A=B=1$, which makes $A\oplus B = 0$, forcing $c_2 = 0$. At most one of the two carries is ever hot, so OR-ing them (rather than adding them and starting an infinite regress of carries) is exactly right. And $AB + (A\oplus B)C_{in}$ is just the majority function wearing its two-half-adder costume.

---

## Chaining them — the ripple-carry adder

One full adder handles one column. To add two $n$-bit numbers, place $n$ full adders side by side and **wire each stage's $C_{out}$ into the next stage's $C_{in}$.** The rightmost stage has nothing to its right, so its carry-in is $0$ (a half adder would do there). This is a **ripple-carry adder**.

![[ripple-carry-adder.svg|680]]

Watch $7 + 1 = 8$ ripple, the binary version of the odometer rolling $0999 \to 1000$:

$$
\begin{array}{r}
 \;\;0111 \\
+\,0001 \\
\hline
 \;1000
\end{array}
$$

The carry born in column 0 ($1+1$) is $1$; it forces column 1 to carry, which forces column 2, which forces column 3 — a single $1$ sweeping left through all four stages and flipping every bit to $0$ behind it, until the final stage writes the new leading $1$. That cascade is the adder *working*, and it is also its Achilles heel.

> [!warning] Addition is not instant — the carry has to travel
> Each full adder cannot finish until its carry-in has settled, and that carry came from the stage below, whose carry came from the stage below *that*. In the worst case (like $7+1$) the carry ripples through **all $n$ stages one after another**, so an $n$-bit ripple adder's delay grows with $n$. Since arithmetic sits on the CPU's **critical path**, this delay helps set the clock speed. Real processors avoid the wait with a **carry-lookahead adder**, which computes every column's carry *in parallel* from the inputs directly (each column "generates" a carry if $A\cdot B$, or "propagates" one if $A\oplus B$) — trading many more gates for a delay that grows like $\log n$ instead of $n$. The ripple adder is the one you draw; the lookahead adder is the one in your laptop.

---

## Subtraction for free

Here is the payoff that made [[Two's Complement]] the universal choice: **the same adder subtracts, with almost no extra hardware.** To compute $A - B$, two's complement says negate $B$ (invert every bit, then add $1$) and add. The adder already adds; the "$+1$" is free because the rightmost stage has a spare carry-in.

So put an XOR gate on each $B$ bit, controlled by one shared **"subtract" line** — recall from [[Logic Gates]] that XOR-ing with $1$ *inverts* and XOR-ing with $0$ passes through. Feed that same subtract line into the bottom carry-in:

- **subtract $= 0$:** every $B$ bit passes unchanged, carry-in $=0$ → the circuit computes $A + B$.
- **subtract $= 1$:** every $B$ bit is inverted and carry-in $=1$ → the circuit computes $A + \overline{B} + 1 = A - B$.

**One circuit, both operations, chosen by a single wire** — the arithmetic heart of every ALU. And the overflow signal falls out for free: for signed numbers, overflow is exactly *carry-in $\neq$ carry-out at the top (sign) bit* — the condition [[Overflow and Underflow]] states in full.

---

## Beyond the syllabus — the whole of arithmetic

The full adder is the seed; every other operation grows from it.

- **Multiplication** is shift-and-add: to compute $A \times B$, add shifted copies of $A$ wherever $B$ has a $1$-bit. A hardware multiplier is a grid of full adders (a **carry-save** array), which is why multiply costs more silicon and more time than add.
- **The ALU** (arithmetic-logic unit) bolts the adder/subtractor beside the bitwise-logic block from [[Bitwise Operations]] and a shifter, with a multiplexer choosing which result leaves — the datapath component the fetch–execute cycle drives.
- **Everything else** — comparison ($A - B$ then check the sign and zero flags), counting, address calculation, floating-point mantissa arithmetic — is addition in disguise. Land the full adder and you have, quite literally, built the thing that does the maths.

The through-line of the whole [[Logic Gates|gates]] → [[Boolean Algebra|algebra]] → [[Karnaugh Maps|maps]] → adders arc: a computer is a machine that *does arithmetic by doing logic*, and the full adder is where the two finally become the same thing.

---

## Worked examples

**1 — Trace a full-adder row.** *Trigger: two bits plus carry-in → use the full-adder sum/parity and carry/majority rules.* Inputs $A=1, B=0, C_{in}=1$. Sum $= 1\oplus 0\oplus 1 = 0$; $C_{out} = $ majority$(1,0,1) = 1$ (two of the three are $1$). So $1 + 0 + 1 = 10_2$ — write $0$, carry $1$. Matches row six of the table. ✓

**2 — Build a full adder, count the gates.** *Trigger: build a three-input column from two-input modules → cascade two half adders, then combine their carries.* Two half adders (2 XOR + 2 AND) + one OR $= $ **2 XOR, 2 AND, 1 OR = five gates**. (A from-scratch DNF build of $C_{out}$ alone would use more; the two-half-adder route is the economical one — this is minimisation from [[Boolean Algebra]] paying off.)

**3 — 4-bit subtraction $5 - 3$.** *Trigger: subtraction using an adder → use two’s-complement negation, keeping only four result bits.* In 4-bit two's complement $5 = 0101$, $3 = 0011$, so $\overline{3} = 1100$. Set subtract $=1$: the adder computes $0101 + 1100 + 1 = 10010$. Drop the carry out of 4 bits → $0010 = 2$. And $5 - 3 = 2$. ✓ One adder, a flipped control line, no subtractor in sight.

---

## Exam Notes

### Cambridge 9618 — A Level §15.2

Produce truth tables for logic circuits including **half adders and full adders**. Derive sum and carry from binary addition, distinguish carry-in from carry-out, and trace a supplied circuit. The two-half-adders-plus-OR construction is a useful way to understand the full adder; the syllabus does not separately mandate that particular construction. Ripple-carry timing and carry-lookahead design are enrichment, not named requirements.

### AQA 7517 — §4.6.4.1

Recognise and trace both adder circuits; **construct the half-adder circuit**. The specification distinguishes those demands: do not turn “trace a full adder” into an unsupported requirement to reproduce its construction from memory. [AQA specification](https://www.aqa.org.uk/subjects/computer-science/a-level/computer-science-7517/specification/subject-content/fundamentals-of-computer-systems).

### OCR H446 — §1.4.3(e)

The logic associated with **half and full adders** is explicitly included. Practise deriving the output bits and tracing the gates, alongside Boolean algebra and truth tables. [OCR specification](https://www.ocr.org.uk/Images/170844-specification-accredited-a-level-gce-computer-science-h446.pdf).

### IB Computer Science — first assessment 2027

**A1.2.3–A1.2.5** cover gates, truth tables and logic diagrams, including Boolean algebra and simplification. They do not name an adder as a circuit to memorise. A supplied adder can still be a legitimate application of those assessed gate-and-table skills; “not named” does not mean a circuit using XOR and AND cannot appear.

### Where it is not a named requirement

**Cambridge 0478 §10** requires combinational gates, diagrams, expressions and truth tables, not half/full adders as named devices. **Pearson Edexcel IAL Computer Science (first teaching 2026), §5.3**, likewise specifies Boolean expressions and truth tables without naming adders. Do not confuse that qualification with a blanket claim about “Edexcel A Level”. [Pearson specification](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/computer-science/2026/specification-and-sample-assessments/ial-computer-science-specification.pdf).

**AP CSA** (2025–26 CED) and **AP CSP** (Fall 2023 CED) examine programming logic, not hardware adder design. Boolean expressions are still assessed; the circuit construction is enrichment.

---

## Connections

- **Parent:** [[Logic Gates]] — the XOR (sum) and AND (carry) the adder wires together; Logic Gates previews the half adder and hands off the full arithmetic story.
- **The reused function:** [[Karnaugh Maps]] — the carry-out *is* the majority function minimised there; [[Boolean Algebra]] — the two-half-adder build is minimisation in action, and $C_{out}=AB+(A\oplus B)C_{in}$ is the algebra of majority.
- **The number system:** [[Number Bases]] — binary and place value, the base-2 system the circuit adds in; [[Two's Complement]] — binary addition, and why one adder also subtracts (invert + carry-in $1$); [[Overflow and Underflow]] — final carry-out detects unsigned addition overflow; signed overflow compares the carry into and out of the sign bit.
- **The application:** [[Arithmetic Logic Unit]] — the adder/subtractor is its arithmetic core; [[CPU Architecture and the Fetch-Execute Cycle]] — where the ALU sits in the datapath; [[Bitwise Operations]] — the logic block beside the adder in an ALU.
- **History:** [[Stories/The Boolean-to-Silicon Bridge]] — Boole → Shannon → the circuits that made arithmetic physical.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $A \oplus B$ | `A \oplus B` | XOR — the sum bit of a half adder |
| $A \cdot B$ | `A \cdot B` | AND — the carry bit of a half adder |
| $A \oplus B \oplus C_{in}$ | `A \oplus B \oplus C_{in}` | full-adder sum (parity of three bits) |
| $AB + AC_{in} + BC_{in}$ | `AB + AC_{in} + BC_{in}` | full-adder carry-out (majority of three bits) |
| $A + \overline{B} + 1$ | `A + \overline{B} + 1` | subtraction $A-B$ via two's complement |
| $C_{in},\ C_{out}$ | `C_{in},\ C_{out}` | carry into / out of a stage |
| $10_2$ | `10_2` | binary two — a sum digit $0$ with a carry $1$ |
