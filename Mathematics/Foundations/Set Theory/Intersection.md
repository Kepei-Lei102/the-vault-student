---
chinese: 交集 (jiāojí)
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
  - notation/intersection
---

# Intersection 交集

> Part of the [[Set Operations]] family. See also: [[Union]], [[Complement]].

## Definition

### Formal

$$A \cap B = \{x : x \in A \text{ and } x \in B\}$$

### Intuitive

Intersection means **only the overlap**. What's in bag $A$ AND also in bag $B$? Just the things they share. If they share nothing, the intersection is empty.

### 中文锚点

交集：$A \cap B$ — **同时**属于 $A$ 和 $B$ 的所有元素。

## Notation

| Symbol | LaTeX | Read as |
|--------|-------|---------|
| $A \cap B$ | `A \cap B` | "$A$ intersect $B$" or "$A$ and $B$" |

Mnemonic: $\cap$ looks like an upside-down cup (a **cap** or hat) — it only keeps what fits **under** both.

## Examples

$$A = \{1, 2, 3, 4\}, \quad B = \{3, 4, 5, 6\}$$
$$A \cap B = \{3, 4\}$$

$$C = \{a, b\}, \quad D = \{x, y\}$$
$$C \cap D = \emptyset$$

When two sets share no elements, they are **disjoint** (互斥/不相交).

## Key Properties

| Property    | Formula                                 | Meaning                                      |
| ----------- | --------------------------------------- | -------------------------------------------- |
| Commutative | $A \cap B = B \cap A$                   | Order doesn't matter                         |
| Associative | $(A \cap B) \cap C = A \cap (B \cap C)$ | Grouping doesn't matter                      |
| Identity    | $A \cap \xi = A$                        | Intersection with everything changes nothing |
| Domination  | $A \cap \emptyset = \emptyset$          | Intersection with nothing is nothing         |
| Complement  | $A \cap A' = \emptyset$                 | No element is both in $A$ and not in $A$     |
| Idempotent  | $A \cap A = A$                          | Intersecting with yourself changes nothing   |

## Disjoint Sets

Two sets $A$ and $B$ are **disjoint** if $A \cap B = \emptyset$.

In a [[Venn Diagram]], disjoint sets are drawn as circles that do not overlap.

This is important in [[Probability Basics]]: if events $A$ and $B$ are disjoint (mutually exclusive), then $P(A \cup B) = P(A) + P(B)$ — no need to subtract the overlap because there is none.

## Exam Notes

### Cambridge 0580 (Core and Extended)

- **E1.2 / C1.2 Sets** is a single objective — *understand and use set language, notation and Venn diagrams* — and $A \cap B$ is on the **Core** notation list, one of only five symbols a Core candidate must read: $n(A)$, $A'$, $\xi$, $A \cup B$, $A \cap B$. Core Venn diagrams are limited to **two** sets and to *describing* sets; Extended goes to **three** sets, adds *representing relationships between sets*, and brings in $\in$, $\notin$, $\subseteq$, $\not\subseteq$, $\emptyset$ and set-builder definitions such as $\{x : a \leqslant x \leqslant b\}$.
- **The intersection is where three-set Venn questions are won.** Fill the centre — $n(A \cap B \cap C)$ — *first*, then work outwards by subtraction. Filling from the outside in double-counts the overlaps, which is the single most common way these questions go wrong.
- Disjointness has its own exam phrasing: a question that says two sets "have no elements in common" is telling you $A \cap B = \emptyset$ and expecting non-overlapping circles.

### OxAQA 9260

- **N9 Sets**, Core content, with the notation list identical to 0580 Core — *use language and notation of sets including $n(A)$, $A'$, $A \cup B$, $A \cap B$, $\xi$* — plus *understand and use Venn diagrams to solve problems*.

### Cambridge 0606 / 9709 / 9231

- Set language is **not** a topic on any of them, but $\cap$ survives into probability and is examined hard there. At 9709 §5.3, $P(A \cap B)$ is the tool for **two** named tests: events are independent when $P(A \cap B) = P(A)\,P(B)$ (the syllabus names exactly this comparison), and conditional probability is $P(A \mid B) = P(A \cap B)/P(B)$. Note the contrast with [[Union]]: the *intersection* formulas are required at 9709 while the general **union** formula explicitly is not.

### IB AA / AI

- No standalone set-theory topic in either guide. $A \cap B$ appears inside **probability** — independence, conditional probability and Venn diagrams as a probability tool — so an IB student uses the operation constantly without ever being asked to define it.

### AP

- **AP Calculus AB/BC:** not examined. **AP Statistics:** the same content in different clothes — the **multiplication rule** $P(A \cap B) = P(A)\,P(B \mid A)$, independence as $P(A \cap B) = P(A)P(B)$, and "mutually exclusive" for disjoint. The notation is identical; only $A^c$ for $A'$ differs.

## Connections

- **Combined with:** [[Union]], [[Complement]] → see [[Set Operations]] for the full picture
- **Visual:** [[Venn Diagram]] — intersection is the overlapping region
- **Counting:** [[Cardinality]] — $n(A \cap B)$ is the overlap you subtract in inclusion-exclusion
- **Logic:** $A \cap B \leftrightarrow A$ AND $B$ → [[Boolean Algebra]]
- **Probability:** $P(A \cap B)$ — "probability of both" → [[Combined Probability]]
- **CS bridge:** `A & B` or `A.intersection(B)` in Python

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\cap$ | `\cap` | Intersection |
| $\bigcap$ | `\bigcap` | Big intersection (for many sets) |
| $\emptyset$ | `\emptyset` | Empty set (result of disjoint intersection) |
