---
chinese: 并集 (bìngjí)
prerequisites:
  - "[[Set]]"
  - "[[Element]]"
leads_to:
  - "[[Venn Diagram]]"
  - "[[Cardinality]]"
  - "[[Boolean Algebra]]"
  - "[[Probability Basics]]"
tags:
  - subject/mathematics
  - domain/set-theory
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0580
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/AP
  - syllabus/0580-E1-2
  - curriculum/OxAQA-9260
  - syllabus/9260-N9
  - type/definition
  - type/vocabulary
  - notation/union
---

# Union 并集

> Part of the [[Set Operations]] family. See also: [[Intersection]], [[Complement]].

## Definition

### Formal

$$A \cup B = \{x : x \in A \text{ or } x \in B \text{ (or both)}\}$$

### Intuitive

Union means **combine everything**. Dump both bags into one pile, remove duplicates. If it's in $A$, or in $B$, or in both — it's in the union.

### 中文锚点

并集：$A \cup B$ — 属于 $A$ **或**属于 $B$ 的所有元素。

注意："或"在数学中是**包含性的**（inclusive or）— 同时属于两者也算。

## Notation

| Symbol     | LaTeX      | Read as                         |
| ---------- | ---------- | ------------------------------- |
| $A \cup B$ | `A \cup B` | "$A$ union $B$" or "$A$ or $B$" |

Mnemonic: $\cup$ looks like a **cup** — it **collects** everything.

## Examples

$$A = \{1, 2, 3\}, \quad B = \{2, 3, 4, 5\}$$
$$A \cup B = \{1, 2, 3, 4, 5\}$$

Note: 2 and 3 appear in both sets but only once in the union — sets don't hold duplicates.

$$C = \{a, b\}, \quad D = \{x, y\}$$
$$C \cup D = \{a, b, x, y\}$$

When sets share nothing ($C \cap D = \emptyset$), the union is simply all elements side by side.

## Key Properties

| Property | Formula | Meaning |
|----------|---------|---------|
| Commutative | $A \cup B = B \cup A$ | Order doesn't matter |
| Associative | $(A \cup B) \cup C = A \cup (B \cup C)$ | Grouping doesn't matter |
| Identity | $A \cup \emptyset = A$ | Union with nothing changes nothing |
| Domination | $A \cup \xi = \xi$ | Union with everything is everything |
| Complement | $A \cup A' = \xi$ | A set and its complement cover the universe |
| Idempotent | $A \cup A = A$ | Unioning with yourself changes nothing |

## Counting

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

You must subtract the overlap — otherwise elements in both sets get counted twice. See [[Cardinality]].

## Exam Notes

### Cambridge 0580 (Core and Extended)

- **E1.2 / C1.2 Sets** is a single objective, and $A \cup B$ is on the **Core** notation list alongside $n(A)$, $A'$, $\xi$ and $A \cap B$ — those five are all a Core candidate must read. Core Venn diagrams are limited to **two** sets and to *describing* sets; Extended goes to **three** sets, adds *representing relationships between sets*, and brings in $\in$, $\notin$, $\subseteq$, $\not\subseteq$, $\emptyset$ and set-builder definitions such as $\{x : a \leqslant x \leqslant b\}$.
- The counting formula $n(A \cup B) = n(A) + n(B) - n(A \cap B)$ is standard Extended work, and the three-set Venn diagram is where it earns its keep: fill the **centre first**, then the pairwise overlaps by subtraction, then the singles, then the outside. Filling from the outside in is the reliable way to double-count.
- Question shapes: shade $A \cup B$ or a compound region; complete a two- or three-set Venn diagram from worded totals and read off $n(A \cup B)$; then a probability part from the same diagram.

### OxAQA 9260

- **N9 Sets**, Core content, with the notation list identical to 0580 Core — *use language and notation of sets including $n(A)$, $A'$, $A \cup B$, $A \cap B$, $\xi$* — plus *understand and use Venn diagrams to solve problems*.

### Cambridge 0606 / 9709 / 9231

- Set language is **not** a topic on any of them, and there is a specific trap worth knowing at 9709. Its §5.3 notes say in as many words that **explicit use of the general formula $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ is not required** — 9709 handles combined events through tree diagrams, sample spaces and conditional probability instead. The *counting* version above is 0580 material and stays useful; the *probability* version is genuinely off-syllabus at 9709, so a candidate reaching for it has usually missed a cheaper tree-diagram route. (It is examinable elsewhere — see [[Combined Probability]].)

### IB AA / AI

- No standalone set-theory topic in either guide. $A \cup B$ survives inside **probability**, where the addition rule $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ *is* named — the opposite of the 9709 position, and worth flagging to any student moving between the two systems.

### AP

- **AP Calculus AB/BC:** not examined. **AP Statistics:** the **general addition rule** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ is a named formula, together with its mutually-exclusive special case. Notation differs only in the complement ($A^c$ for $A'$).

## Connections

- **Combined with:** [[Intersection]], [[Complement]] → see [[Set Operations]] for the full picture
- **Visual:** [[Venn Diagram]] — union is everything inside at least one circle
- **Logic:** $A \cup B \leftrightarrow A$ OR $B$ → [[Boolean Algebra]]
- **Probability:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ → [[Combined Probability]]
- **CS bridge:** `A | B` or `A.union(B)` in Python

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\cup$ | `\cup` | Union |
| $\bigcup$ | `\bigcup` | Big union (for many sets) |
| $A \cup B \cup C$ | `A \cup B \cup C` | Chain unions |
