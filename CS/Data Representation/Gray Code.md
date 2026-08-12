---
chinese: 格雷码 (géléimǎ)
prerequisites:
  - "[[Number Bases]]"
  - "[[Bitwise Operations]]"
leads_to:
  - "[[Karnaugh Maps]]"
  - "[[Clock Domains and Metastability]]"
  - "[[Secondary Storage]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/digital-circuits
  - domain/data-representation
  - level/A-Level
  - level/university
  - type/deep
  - type/technique
  - notation/XOR-circled-plus
  - misconception/gray-is-just-another-value
  - misconception/gray-code-is-unique
  - misconception/gray-needs-more-bits
---

# Gray Code 格雷码

> *Ordinary counting lies if you catch it mid-step. Going from $7$ to $8$, binary flips **four** bits at once — $0111 \to 1000$ — and for one flicker, while the bits are still moving, the wires can read out **any** number at all. Gray code is counting under a single vow: **never change more than one bit at a time.** That one rule quietly rescues a spinning motor shaft, a cache's queue pointer, and a thousand-year-old Chinese ring puzzle from the exact same disaster.*

## Definition

A **Gray code** is an ordering of the $2^n$ binary strings of length $n$ such that **any two consecutive strings differ in exactly one bit** (Hamming distance $1$). The standard one — the **binary-reflected Gray code** — is also cyclic: the last string and the first also differ in one bit, so you can count round and round forever, flipping a single bit each step.

It is *not* a new number system. The Gray string `1110` does not mean "fourteen"; it is a **re-encoding** — the same $n$ bits, in a different order, chosen so that neighbours are always one flip apart. Same information, same bit-width; only the *sequence* changes.

The point is physical. In the real world, bits **do not change simultaneously** — gates switch at slightly different times, sensors cross thresholds at slightly different angles. So if a value is *read while it is changing*, a multi-bit transition can be caught half-done and report a number that was never intended. Gray code guarantees only **one** bit is ever in flight, so a mid-transition read is at worst the old value or the new one — never garbage.

> [!info] Whose code? — an eponymy footnote
> Named for **Frank Gray**, a Bell Labs physicist, who used the "reflected binary code" in a 1947 patent to cut errors in pulse-code transmission. But the pattern is far older: Émile **Baudot** used a form of it in 1870s telegraphy, and the [[Stigler's Law of Eponymy|Chinese rings puzzle]] below embodies it by the 17th century. A mild case of [[Stigler's Law of Eponymy]] — the code is named after neither its first nor its last discoverer.

### 中文锚点

| English                   | 中文                | 一句话              |
| ------------------------- | ----------------- | ---------------- |
| Gray code                 | 格雷码 (géléimǎ)     | 相邻两个数只差**一位**    |
| reflected binary code     | 反射二进制码            | 用"镜像"递归构造出来      |
| Hamming distance          | 汉明距离              | 两个二进制串不同的位数      |
| rotary / absolute encoder | 绝对式旋转编码器          | 读轴角度的传感器，用格雷码防跳变 |
| Chinese rings             | 九连环 (jiǔliánhuán) | 解法的状态序列就是一段格雷码   |

核心一句话：普通二进制进位时会**多位同时翻转**，读取过程中可能读到乱码；格雷码规定**每步只翻一位**，所以中途读到的至多是"旧值或新值"，绝不会是凭空的错值。

---

## Counting in Gray

Here is 3-bit binary next to the 3-bit Gray code. Read down the Gray column and check: **every step flips exactly one bit** — and so does the wrap from the last row back to the first.

| Value | Binary | Gray | bit that flipped |
|:-:|:-:|:-:|:-:|
| 0 | 000 | 000 | — |
| 1 | 001 | 001 | bit 0 |
| 2 | 010 | 011 | bit 1 |
| 3 | 011 | 010 | bit 0 |
| 4 | 100 | 110 | bit 2 |
| 5 | 101 | 111 | bit 0 |
| 6 | 110 | 101 | bit 1 |
| 7 | 111 | 100 | bit 0 |

Now watch the dangerous step, $3 \to 4$. In binary, `011` $\to$ `100` — **all three bits flip together.** In Gray, `010` $\to$ `110` — **one bit flips.**

![[gray-vs-binary-transition.svg|697]]

**Why this is not a curiosity — the rotary encoder.** A motor shaft's angle is read by an **absolute encoder**: a disc patterned with concentric rings, one sensor per bit, giving the angle as a binary number. Suppose the shaft sits right on the boundary between $3$ (`011`) and $4$ (`100`). If the three sensors don't switch at the *exact* same instant — and they never do — you can momentarily read `111` ($7$) or `000` ($0$): the shaft appears to teleport to the far side of the dial. A control loop fed that spike does something violent. Pattern the disc in **Gray code** and only one ring changes at any boundary, so the worst misread is $3$ or $4$ — the true answer or its neighbour, never a wild jump.

That is the same reason [[Karnaugh Maps]] lay their axes in Gray order (so neighbouring cells differ in one variable and therefore *combine*), and the same reason [[Clock Domains and Metastability|asynchronous FIFO]] pointers are Gray-coded before crossing between clocks (so a pointer sampled mid-change is only ever off by one, never corrupt). One idea, three places.

---

## Construction — reflect and prefix

Why "*reflected*" binary code? Because you build it with a mirror. Start from the 1-bit code $[\,0,\ 1\,]$ and grow each larger code from the one below it ([[Recursion|recursively]]):

1. Take the $n$-bit list. **Prefix every entry with `0`** — this is the first half.
2. **Reflect** (reverse) the $n$-bit list, and **prefix every entry with `1`** — this is the second half.
3. Concatenate. You now have the $(n{+}1)$-bit Gray code.

![[gray-reflect-construction.svg|660]]

$$[\,0,\,1\,] \;\to\; [\,00,\,01,\,11,\,10\,] \;\to\; [\,000,001,011,010,\;110,111,101,100\,]$$

**Why it can only ever flip one bit.** Inside each half, the one-bit property is inherited from the smaller code. At the **seam** where the halves meet, the last entry of the first half is `0` + (last of the small code) and the first entry of the second half is `1` + (last of the small code) — identical except for the new leading bit, so they differ in exactly one bit. The reflection is precisely what puts two *copies of the same string* back-to-back at the join, so the prefix bit is the only thing that changes. The same argument on the outer wrap (`1`+first vs `0`+first) makes the code cyclic.

---

## Conversion — the XOR trick

You rarely build Gray codes by hand; you convert. Both directions are pure [[Bitwise Operations|XOR]], because XOR is the "did this bit change?" operator.

**Binary $\to$ Gray.** Each Gray bit is the XOR of a binary bit with its *left-hand* (more significant) neighbour — imagining a phantom $0$ above the top bit:

$$g_i = b_i \oplus b_{i+1} \qquad\Longleftrightarrow\qquad G = B \oplus (B \gg 1)$$

The whole-word form is the fast way to do it by hand: **shift a copy of $B$ one place right, then XOR the two.** Convert $B = 1011$ (denary $11$):

```
   B           =  1 0 1 1
   B >> 1       =  0 1 0 1      a 0 shifts in at the top, so each
 ──────────────────────────     column pairs a bit with its left neighbour
   B ⊕ (B>>1)   =  1 1 1 0   =  Gray(11)
```

Column by column that is $g_3 = 1\oplus0 = 1$, $g_2 = 0\oplus1 = 1$, $g_1 = 1\oplus0 = 1$, $g_0 = 1\oplus1 = 0$. Each Gray bit is really asking "did the value change at this place?", which is exactly what keeps consecutive numbers one flip apart.

**Gray $\to$ Binary.** Going back, you *cannot* just XOR neighbours again — every binary bit depends on all the Gray bits above it. So run a **cumulative XOR from the top down**: copy the top bit unchanged, then each next binary bit is *the binary bit you just found* XOR *the current Gray bit*.

$$b_{n-1}=g_{n-1}, \qquad b_i = b_{i+1} \oplus g_i \qquad\Longleftrightarrow\qquad b_i = g_i \oplus g_{i+1} \oplus \cdots \oplus g_{n-1}$$

Convert $G = 1110$ straight back:

```
   b3 = g3               =  1
   b2 = b3 ⊕ g2 = 1 ⊕ 1  =  0
   b1 = b2 ⊕ g1 = 0 ⊕ 1  =  1
   b0 = b1 ⊕ g0 = 1 ⊕ 0  =  1     →  1011 = 11
```

Round-trip complete: $1011 \to 1110 \to 1011$. The two directions are inverses, as they must be — XOR undoes itself.

---

## The shape underneath — a walk on the hypercube

Give every $n$-bit string a corner of an $n$-dimensional **hypercube**, and join two corners with an edge whenever they differ in one bit. Then a Gray code is nothing but a **path that visits every corner exactly once, always stepping along an edge** — a *Hamiltonian path* on the cube. The cyclic Gray code is a Hamiltonian *cycle*: a closed tour of all $2^n$ corners.

![[gray-hypercube-path.svg|697]]

This is the honest reason Gray codes exist and matter: "change one bit" *means* "move to an adjacent corner," so counting in Gray is a continuous stroll through the cube of all states, never a leap across it. Binary counting, by contrast, regularly jumps clear across the cube (corner `011` to corner `100` is a body-diagonal — three edges at once).

> [!info] Beyond the syllabus — the same walk, everywhere
> - **The Tower of Hanoi.** Count in Gray code and, at each step, the single bit that flips names the disk you must move in the optimal Hanoi solution (bit $0$ = the smallest disk). The puzzle *is* a Gray-code counter in disguise.
> - **九连环, the Chinese rings.** In this classic puzzle you take rings on and off a bar under a one-at-a-time constraint; the sequence of legal configurations traces a Gray code. The mathematics of "only one thing may change per move" is centuries old and was played with by hand long before it was named.
> - **Telecommunications.** Digital radio maps bit-patterns to signal points (QAM/PSK). Assign them in **Gray order** and the nearest-neighbour points — the ones noise most easily confuses — differ in a single bit, so the commonest error corrupts only one bit, not several.
> - **Genetic algorithms.** Encoding parameters in Gray code removes "Hamming cliffs" (where adjacent values like $7$ and $8$ differ in every bit), so a one-bit mutation makes a one-step change in value, and the search moves smoothly.

Count in Gray, and the single flipping bit *is* the instruction: in the Tower of Hanoi it names the one disc to lift, and in **九连环** it names the one ring to slip free. Two puzzles centuries and a continent apart, both running the same one-bit-at-a-time sequence.

![[gray-hanoi-and-chinese-rings.png|697]]

---

## Worked examples

**1 — Build the 3-bit code.** From $[00,01,11,10]$: prefix `0` → $000,001,011,010$; reflect to $[10,11,01,00]$ and prefix `1` → $110,111,101,100$; concatenate → $000,001,011,010,110,111,101,100$. Every neighbour, and the wrap, differs in one bit.

**2 — The encoder save.** Reading angle across the $3\to4$ boundary: binary discs risk `011`→(`111` or `000`)→`100`, a phantom jump to $7$ or $0$; a Gray disc reads `010`→`110`, one clean bit-flip, no phantom. The single-bit vow is the whole safety guarantee.

*(Both conversion directions are worked in full, with the shift-and-XOR layout, in the Conversion section above.)*

---

## Exam Notes

### Cambridge 9618 (A Level, §15.2)
Gray code is the (usually unnamed) ordering along the axes of a [[Karnaugh Maps|Karnaugh map]] — `00, 01, 11, 10`, not `00, 01, 10, 11`. Knowing *why* that order is used — so physically adjacent cells differ in one variable and can be grouped — is knowing why K-maps work at all. The conversion algorithms and encoders are enrichment, but the one-bit-adjacency idea is directly load-bearing for the examined K-map technique.

### Cambridge 0478 / AP / IB CS
Not examined on any of them — the IB 2027 guide's logic content (A1.2) stops at gates processing binary data, with no Karnaugh maps, so Gray code doesn't even get the unnamed-axis appearance it has on 9618. It surfaces first in real digital design and embedded work.

### Where it surfaces
Absolute rotary/linear encoders, clock-domain-crossing FIFOs, Gray-coded modulation in comms, and error-tolerant counters — Gray code is a working engineer's everyday tool wherever a multi-bit value is read asynchronously.

---

## Connections

- **Parents:** [[Number Bases]] — the binary strings Gray code re-orders; [[Bitwise Operations]] — the XOR that converts both ways ("did this bit change?").
- **What it powers:** [[Karnaugh Maps]] — the Gray-ordered axes that make neighbouring cells combine; [[Clock Domains and Metastability]] — Gray-coded FIFO pointers cross between clocks safely because only one bit is ever in flight; [[Secondary Storage]] — MLC/TLC/QLC flash numbers its charge levels in Gray order, so a cell that drifts one level over corrupts one bit, not four.
- **How it's built:** [[Recursion]] — the reflect-and-prefix construction is recursion with a mirror.
- **History:** [[Stigler's Law of Eponymy]] — named for Frank Gray, but older than him (Baudot, the Chinese rings).

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $g_i = b_i \oplus b_{i+1}$ | `g_i = b_i \oplus b_{i+1}` | binary → Gray, bit by bit |
| $G = B \oplus (B \gg 1)$ | `G = B \oplus (B \gg 1)` | binary → Gray, whole word |
| $b_i = b_{i+1} \oplus g_i$ | `b_i = b_{i+1} \oplus g_i` | Gray → binary, cumulative XOR from the top |
| $011 \to 100$ | `011 \to 100` | binary: three bits flip at once |
| $010 \to 110$ | `010 \to 110` | Gray: one bit flips |
