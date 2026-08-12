---
chinese: 卡诺图
prerequisites:
  - "[[Boolean Algebra]]"
  - "[[Logic Gates]]"
  - "[[Gray Code]]"
leads_to:
  - "[[Half-Adder and Full-Adder]]"
  - "[[Flip-Flops]]"
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
  - type/visual-tool
  - notation/AND-dot
  - notation/OR-plus
  - notation/NOT-bar
  - misconception/karnaugh-groups-any-size
  - misconception/karnaugh-forgets-wraparound
  - misconception/karnaugh-non-maximal-groups
---

# Karnaugh Maps 卡诺图

> **A Karnaugh map is Boolean algebra you do with your eyes.** It rearranges the truth table so that the two terms which *combine into one* are always neighbours — and then minimising a circuit becomes what your visual cortex was built for: circling the biggest rectangles of 1s.

## Definition

A **Karnaugh map** (K-map) is a truth table redrawn as a grid, with the input combinations arranged so that **any two cells sharing an edge differ in exactly one input variable**. That single design rule is the whole trick. [[Boolean Algebra]] can already minimise an expression — but it needs cleverness: you have to *spot* which term to factor first. The K-map removes the cleverness. Because neighbouring cells differ by one variable, the algebraic step that collapses two terms into one becomes a purely visual act: **draw a loop around them.**

Invented by Maurice Karnaugh at Bell Labs in 1953, it is the workhorse of hand-minimisation for up to about four variables — the sweet spot where a human eye out-performs algebra.

### 中文锚点

**卡诺图 (kǎnuò tú)** = 把真值表重画成一张方格图，格子的排列保证**相邻两格只有一个变量不同**。于是[[Boolean Algebra|布尔代数]]里"两项合并、消去一个变量"这一步，变成了肉眼可见的操作：**把相邻的 1 圈起来**。

| English | 中文 | 一句话 |
|---|---|---|
| Karnaugh map | 卡诺图 | 相邻格只差一个变量的真值表 |
| Gray code order | 格雷码顺序 | 00→01→11→10，每步只翻一位 |
| grouping / looping | 圈组 / 画圈 | 把相邻的 1 圈成 $2^k$ 的矩形 |
| minterm | 最小项 | 真值表里输出为 1 的那一格 |
| don't-care | 无关项 (记作 X/×) | 可当 0 也可当 1，哪个方便用哪个 |
| adjacency | 相邻 | 只差一位 → 可以合并消元 |

中文数字逻辑课就叫"卡诺图化简"，考点和 9618 §15.2 完全一致：**画图、圈最大组、写出最简与或式**。

---

## The one identity it automates

The entire method rests on a single law from [[Boolean Algebra]] — the **adjacency law**:

$$XY + X\overline{Y} = X(Y + \overline{Y}) = X\cdot 1 = X.$$

Read it carefully: two product terms that are **identical except for one variable** — appearing as $Y$ in one and $\overline{Y}$ in the other — merge into a single term with that variable *deleted*. That is the only move minimisation ever makes; everything else is finding opportunities to make it.

A Karnaugh map is an arrangement of the truth table engineered so that **"differ in exactly one variable" means "sit next to each other."** Then merging is just: see two adjacent 1s, loop them, drop the variable that changed. Loop four in a rectangle and you have applied the law twice, dropping two variables. A loop of $2^k$ cells drops $k$ variables at once.

---

## Building the map — Gray-code axes

The magic is entirely in the **ordering of the axis labels**. You do *not* count up in plain binary $00, 01, 10, 11$ — because $01 \to 10$ flips *two* bits, so those neighbours would differ in two variables and the adjacency law wouldn't apply. Instead the labels run in **Gray code** ([[Gray Code]]): $00, 01, 11, 10$ — every step changes exactly one bit, including the wrap from the last back to the first.

![[karnaugh-map-anatomy.svg|697]]

Two consequences of that ordering, both load-bearing:

- **Every edge is a one-variable step.** Horizontal neighbour, vertical neighbour — always exactly one input flips. That is what makes a loop legal.
- **The map has no true edges — opposite sides wrap.** The **leftmost and rightmost columns are neighbours**: in the 3-variable map, columns $00$ and $10$ differ in exactly one bit, so a loop can run *off the right edge and reappear on the left*. The **top and bottom rows** wrap the same way. This is the single most-missed adjacency in §15.2 — a pair split across the left and right edges is exactly as legal as a pair in the middle, and in a 4-variable map **all four corners are mutually adjacent** and can be looped as one group of four.

> [!tip] Roll the map into a closed surface
> The flat rectangle is just how the map is *printed* — its edges are an illusion. Roll it so the **left edge meets the right edge** and you get a **cylinder**: the horizontal wrap is now physical, and there is no left or right side any more, so a group straddling those columns is obviously fine. For a 4-variable map, curl that cylinder around so its **top rim meets its bottom rim**, and the tube closes into a **torus** (a donut) — on which there are *no edges at all*, every cell has four honest neighbours, and "adjacency" is simply "touching." The instinct to picture a seamless, edgeless ball is exactly the right instinct; the precise shape is a donut rather than a sphere, only because opposite edges join *straight across* instead of pinching to a point. Either way, the lesson is the same: **there is no such thing as an outer edge on a Karnaugh map.**

---

## The grouping rules

To read the minimal **sum-of-products** ([[Boolean Algebra|SOP]]) off the map, cover every 1 with loops, obeying:

1. **Rectangles only, size a power of two** — a loop must contain $1, 2, 4, 8, 16, \dots$ cells in a rectangular block (counting wrap-around). A group of 3, or an L-shape, is illegal: it doesn't correspond to a single product term.
2. **As large as possible.** Every doubling of a group drops one more variable, so a bigger loop is a *simpler* term. A group of 8 in a 4-variable map is a single literal; a group of 1 is a full 4-literal minterm.
3. **As few loops as possible.** Fewer loops = fewer OR-ed terms = fewer gates.
4. **Loops may overlap**, and **should** when overlapping lets each loop grow larger (idempotence, $X + X = X$, says re-covering a 1 costs nothing).
5. **Every 1 must be covered** by at least one loop; **no 0 may be covered.**

**Reading a loop into a term:** look at which variables stay *constant* across all its cells — those survive (in true or complemented form); the variables that *change* are the ones the adjacency law deleted, so they drop out.

---

## Worked example — the majority function

The same function [[Logic Gates]] built by DNF: three judges vote, output 1 when the majority say yes. Its minterms are $\overline{A}BC,\ A\overline{B}C,\ AB\overline{C},\ ABC$. DNF gave a bloated four-AND circuit; algebra can grind it down; the map gives the answer at a glance.

![[karnaugh-map-majority.svg|560]]

Place the four 1s and look for the biggest rectangles. There is no group of 4 (the 1s don't fill a rectangle), but there are three overlapping **pairs**, all sharing the centre cell $ABC$:

- the vertical pair (both values of $A$, with $B=C=1$) → $A$ drops → term $\mathbf{BC}$
- one horizontal pair ($A=1$, $C=1$, $B$ changes) → $B$ drops → term $\mathbf{AC}$
- the other horizontal pair ($A=1$, $B=1$, $C$ changes) → $C$ drops → term $\mathbf{AB}$

$$\text{majority}(A,B,C) = AB + AC + BC.$$

Exactly the answer [[Logic Gates]] quoted — reached here without a single algebraic manipulation, just by seeing rectangles. Three cards, one function: DNF proves a circuit *exists*, Boolean algebra *grinds* it minimal, the K-map *sees* it minimal.

---

## Four variables — bigger loops, wrapping edges

With four inputs the map is $4\times 4$, both axes Gray-coded. This is where the two ideas the 3-variable map couldn't show come alive: **large groups collapsing to a single literal**, and **wrap-around groups**.

![[karnaugh-map-4var.svg|560]]

Here $F(A,B,C,D)$ minimises to $A + \overline{B}\,\overline{D}$:

- the whole **bottom half** is a group of **8** — across it only $A$ stays constant (at 1), while $B, C, D$ all change, so all three drop: the group is the single literal $\mathbf{A}$.
- the **four corners** form a legal group of **4** by wrap-around (top edge joins bottom, left joins right). Across them $B=0$ and $D=0$ hold while $A, C$ change: the term is $\mathbf{\overline{B}\,\overline{D}}$.

$$F = A + \overline{B}\,\overline{D}.$$

Two loops, two terms — from what would have been a ten-minterm DNF.

---

## Don't-care conditions

Sometimes certain input combinations **can never occur** (e.g. a BCD digit is only $0000$–$1001$; the patterns $1010$–$1111$ are meaningless). Their output is genuinely irrelevant — mark it **X**. When looping, you may treat each **X as 0 or 1, whichever grows your groups**. Don't-cares are free real estate: an X you fold into a group of 8 helped delete a variable and cost nothing, because that input never happens anyway. Ignoring them is a common way to hand in a non-minimal answer.

---

## Products of sums — group the zeros

To get the minimal **product-of-sums** ([[Boolean Algebra|POS]]) instead, loop the **0s** exactly as you looped the 1s. That yields the minimal SOP for $\overline{F}$; one application of **De Morgan** ([[Boolean Algebra]]) turns $\overline{F}$ back into $F$ as a POS. When a truth table has far fewer 0s than 1s, this is the cheaper route — and it is where the [[Boolean Algebra|duality]] between SOP and POS becomes something you can *see*.

---

## Beyond the syllabus — where the eye gives out

The K-map is a human tool with a hard ceiling. At **5–6 variables** you need stacked or three-dimensional maps and the adjacencies get hard to see; past that the method collapses. The systematic successor is the **Quine–McCluskey** algorithm — the same idea (merge terms differing in one bit) done as an exhaustive table a computer can run, producing the **prime implicants** (the maximal legal groups) and then selecting a minimal cover.

And that selection is the catch flagged in [[Boolean Algebra]]: choosing the smallest set of prime implicants is the **minimum-cover problem, which is NP-hard** ([[P vs NP]]). So the ladder is honest all the way up — the K-map works by eye only because 3–4 variables is small; there is no cheap, universal "give me the minimum" button, which is *why* real EDA tools use heuristics, not a formula. The map is the small, beautiful, tractable corner of a genuinely hard problem.

---

## Common traps

> [!warning] Three ways to lose marks in §15.2
> - **Non-power-of-two or non-rectangular loops.** A group of 3, or a bent/L-shaped loop, is illegal — it isn't a single product term. Only $1, 2, 4, 8, 16$ in rectangles.
> - **Forgetting the wrap-around.** The edges are adjacent; the four corners form a group. A student who treats the map as a flat grid misses the biggest loops and writes a non-minimal answer.
> - **Groups that aren't maximal.** Two separate pairs where one group of four was available gives a correct-but-not-minimal expression — and "minimal" is what the mark scheme rewards. Always grow each loop as large as the 1s (and don't-cares) allow.

---

## Exam Notes

### Cambridge 9618 (A Level, §15.2)
Directly examined, for **2-, 3-, and 4-variable** maps. Expect: fill a K-map from a truth table or a Boolean expression; loop it; write the **minimal sum-of-products**; and sometimes handle **don't-care** conditions. Marks are for *maximal* groups (a non-minimal but correct expression is penalised) and for covering every 1. Gray-code axis ordering and wrap-around adjacency are the two things most often slipped. Pairs with algebraic simplification ([[Boolean Algebra]]) — the map is faster, the algebra is the justification.

### Cambridge 0478 (IGCSE)
Not examined — IGCSE stops at gates and truth tables ([[Logic Gates]]). Karnaugh maps are an A-Level escalation.

### Other A-Level boards (AQA / OCR / Edexcel)
All examine K-maps up to four variables, essentially identically; some also want Quine–McCluskey by name.

### AP
Neither AP CSA nor AP CSP covers circuit minimisation. This is a Cambridge/UK-A-Level and first-year-university (digital logic) topic.

### IB Computer Science
Not examined: A1.2 stops at gates and truth tables, and no IB statement asks for minimisation. For an IB student this card is pure enrichment — the systematic tool behind the "simplify this circuit" instinct.

---

## Connections

- **Parent:** [[Boolean Algebra]] — the K-map is its adjacency law $XY+X\overline{Y}=X$ made visual; the map *finds* the simplification, the algebra *justifies* why the loop is legal.
- **Foundation:** [[Logic Gates]] — a minimal SOP is a two-level AND–OR circuit of gates; the majority function here is the one Logic Gates built by DNF.
- **Ordering:** [[Gray Code]] — the reflected-binary sequence ($00,01,11,10$) that makes each step a one-variable move; the reason the axes are labelled the way they are.
- **Leads to:** [[Half-Adder and Full-Adder]] — the sum and carry outputs are Boolean functions you design and minimise with exactly this method; [[Flip-Flops]] — sequential design reduces each flip-flop's next-state logic with K-maps.
- **Depth / honest edge:** [[P vs NP]] — exact minimisation (selecting prime implicants) is NP-hard, which is why the eye-method has a ceiling and machines use heuristics.
- **History:** [[Stories/The Boolean-to-Silicon Bridge]] — Boole → Shannon → the circuit-design era the K-map belongs to.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $XY + X\overline{Y} = X$ | `XY + X\overline{Y} = X` | the adjacency law the map automates |
| $\overline{A}BC$ | `\overline{A}BC` | a minterm (one 1-cell); overbar = that input is 0 |
| $AB + AC + BC$ | `AB + AC + BC` | minimal SOP of the majority function |
| $A + \overline{B}\,\overline{D}$ | `A + \overline{B}\,\overline{D}` | minimal SOP of the 4-variable example |
| $2^k$ | `2^k` | legal loop sizes: a $2^k$-cell loop drops $k$ variables |
| X (don't-care) | `\text{X}` | output irrelevant; loop it as 0 or 1, whichever helps |
