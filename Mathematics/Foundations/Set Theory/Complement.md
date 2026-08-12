---
chinese: 补集 (bǔjí)
prerequisites:
  - "[[Set]]"
  - "[[Element]]"
  - "[[Universal Set]]"
leads_to:
  - "[[Venn Diagram]]"
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
  - notation/complement
  - misconception/complement-without-universal
---

# Complement 补集

> Part of the [[Set Operations]] family. See also: [[Union]], [[Intersection]].

## Definition

### Formal

$$A' = \{x : x \in \xi \text{ and } x \notin A\}$$

The complement of $A$ is the set of all elements in the [[Universal Set]] $\xi$ that are **not** in $A$.

### Intuitive

The complement of $A$ is **everything else**. Imagine the universal set as a room full of people. Set $A$ is a group standing in a circle. The complement $A'$ is everyone else in the room — those NOT in the circle.

Without the room ($\xi$), "everyone else" has no meaning. Complement always requires a universal set.

### 中文锚点

补集：$A'$（或 $\complement_U A$）— 在全集中，不属于 $A$ 的所有元素。

> [!info] Chinese notation
> Chinese textbooks write $\complement_U A$ (读作 "$A$ 关于 $U$ 的补集"). Cambridge and IB use $A'$. Some texts use $\bar{A}$. All mean the same thing.

## Notation

| Context | Symbol | LaTeX |
|---------|--------|-------|
| Cambridge / IB | $A'$ | `A'` |
| Chinese textbooks | $\complement_U A$ | `\complement_U A` |
| Some university texts | $\bar{A}$ | `\bar{A}` |
| Some university texts | $A^c$ | `A^c` |

## Example

$$\xi = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}, \quad A = \{2, 4, 6, 8, 10\}$$
$$A' = \{1, 3, 5, 7, 9\}$$

## Key Properties

| Property | Formula | Meaning |
|----------|---------|---------|
| Complement law | $A \cup A' = \xi$ | Together they cover everything |
| Complement law | $A \cap A' = \emptyset$ | They share nothing |
| Double complement | $(A')' = A$ | "Not not $A$" = $A$ |
| Universal complement | $\xi' = \emptyset$ | Nothing is outside everything |
| Empty complement | $\emptyset' = \xi$ | Everything is outside nothing |

## De Morgan's Laws

$$(A \cup B)' = A' \cap B'$$
$$(A \cap B)' = A' \cup B'$$

Complementing a union gives the intersection of the complements, and vice versa. The operations **swap**.

See [[Set Operations]] for the full treatment and the Boolean algebra connection.

## Counting

$$n(A') = n(\xi) - n(A)$$

See [[Cardinality]].

## Common Misconceptions (Teaching Notes)

### 1. Computing complement without $\xi$

$A'$ has **no meaning** unless the universal set is defined. Students who skip reading $\xi$ in the question will get the complement wrong every time.

### 2. Thinking complement means "opposite"

The complement is not the "opposite" of $A$ in any arithmetic sense. $A = \{2, 4, 6\}$ does not mean $A' = \{-2, -4, -6\}$. The complement is determined entirely by $\xi$.

### 3. Forgetting the double complement

$(A')' = A$ — this simple fact trips students up in multi-step problems where they complement twice.

## Exam Notes

### Cambridge 0580 (Core and Extended)

- **E1.2 / C1.2 Sets** is a single objective — *understand and use set language, notation and Venn diagrams* — and $A'$ sits in the **Core** notation list, one of only five symbols a Core candidate must read: $n(A)$, $A'$, $\xi$, $A \cup B$, $A \cap B$. Core Venn diagrams are limited to **two** sets and to *describing* sets; Extended goes to **three** sets, adds *representing relationships between sets*, and brings in $\in$, $\notin$, $\subseteq$, $\not\subseteq$, $\emptyset$ and set-builder definitions such as $\{x : a \leqslant x \leqslant b\}$.
- Question shapes, in order of frequency: **shade the region** on a given Venn diagram; read a completed Venn diagram and compute $n(A')$ via $n(A') = n(\xi) - n(A)$; complete a Venn diagram from a worded description and then answer a probability part from it.
- **The mark-loser** is writing $A'$ without first reading what $\xi$ is in *that* question — Misconception 1 above is a syllabus-level warning, not a pedantic one.
- **Not on the syllabus:** De Morgan's laws are never named at 0580. The De Morgan section above is enrichment — but the shading questions are exactly where it pays, because it tells you instantly that $(A \cup B)'$ and $A' \cap B'$ shade the same region.

### OxAQA 9260

- **N9 Sets**, Core content, with the notation list identical to 0580 Core — *use language and notation of sets including $n(A)$, $A'$, $A \cup B$, $A \cap B$, $\xi$* — plus *understand and use Venn diagrams to solve problems*. No extension content is attached to N9, so a 9260 candidate meets complement at exactly Core depth.

### Cambridge 0606 / 9709 / 9231

- Set language is **not** a topic on any of them. Where $A'$ reappears is probability: at 9709 §5.3 the complement is the single most profitable line in the paper, because *"at least one"* questions are almost always cheaper as $1 - P(\text{none})$. Learn the operation here; spend it in [[Probability Basics]].

### IB AA / AI

- Neither guide has a standalone set-theory topic. The notation survives inside **probability** — complementary events $P(A') = 1 - P(A)$ and Venn diagrams used as a probability tool — so an IB student needs the operation fluently but will never be asked to define it.

### AP

- **AP Calculus AB/BC:** not examined, in any form. **AP Statistics:** the same content in different clothes — the **complement rule** $P(A^c) = 1 - P(A)$, written $A^c$ rather than $A'$. Reading both notations for the same idea is the only real transfer cost.

## Connections

- **Requires:** [[Universal Set]] — complement is defined relative to $\xi$
- **Combined with:** [[Union]], [[Intersection]] → see [[Set Operations]]
- **Counting:** [[Cardinality]] — $n(A') = n(\xi) - n(A)$
- **Visual:** [[Venn Diagram]] — complement is everything outside $A$'s circle but inside the rectangle
- **Logic:** $A' \leftrightarrow$ NOT $A$ → [[Boolean Algebra]]
- **Probability:** $P(A') = 1 - P(A)$ → [[Probability Basics]]
- **CS bridge:** Complement doesn't have a direct Python operator for sets, but `xi - A` (set difference) gives $A'$ when `xi` is the universal set

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $A'$ | `A'` | Complement (Cambridge/IB) |
| $\bar{A}$ | `\bar{A}` | Complement (overline) |
| $A^c$ | `A^c` | Complement (superscript c) |
| $\complement_U A$ | `\complement_U A` | Complement (Chinese notation) |
| $\xi$ | `\xi` | Universal set |
| $\emptyset$ | `\emptyset` | Empty set |
