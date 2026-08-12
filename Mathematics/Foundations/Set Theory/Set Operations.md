---
chinese: 集合运算 (jíhé yùnsuàn)
prerequisites:
  - "[[Set]]"
  - "[[Element]]"
  - "[[Subset]]"
  - "[[Universal Set]]"
  - "[[Empty Set]]"
leads_to:
  - "[[Venn Diagram]]"
  - "[[Boolean Algebra]]"
  - "[[Probability Basics]]"
  - "[[Logic]]"
  - "[[Combined Probability]]"
  - "[[Logic Gates]]"
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
  - notation/intersection
  - notation/complement
  - misconception/union-vs-intersection
  - misconception/complement-without-universal
---

# Set Operations 集合运算

This note covers the three core operations: **Union** ($\cup$), **Intersection** ($\cap$), and **Complement** ($'$). Each can also be found as a standalone note: [[Union]], [[Intersection]], [[Complement]].

## Union 并集

### Formal

$$A \cup B = \{x : x \in A \text{ or } x \in B \text{ (or both)}\}$$

### Intuitive

Union means **combine everything**. Dump both bags into one pile, remove duplicates. If it's in $A$, or in $B$, or in both — it's in the union.

### 中文锚点

并集：$A \cup B$ — 属于 $A$ **或**属于 $B$ 的所有元素。"或"在数学中包含"同时属于两者"的情况。

### Example

$$A = \{1, 2, 3\}, \quad B = \{2, 3, 4, 5\}$$
$$A \cup B = \{1, 2, 3, 4, 5\}$$

---

## Intersection 交集

### Formal

$$A \cap B = \{x : x \in A \text{ and } x \in B\}$$

### Intuitive

Intersection means **only the overlap**. What's in bag $A$ AND also in bag $B$? Just the things they share.

### 中文锚点

交集：$A \cap B$ — **同时**属于 $A$ 和 $B$ 的所有元素。

### Example

$$A = \{1, 2, 3\}, \quad B = \{2, 3, 4, 5\}$$
$$A \cap B = \{2, 3\}$$

If $A \cap B = \emptyset$, the sets are **disjoint** (互斥/不相交) — they share no elements.

---

## Complement 补集

### Formal

$$A' = \{x : x \in \xi \text{ and } x \notin A\}$$

### Intuitive

The complement of $A$ is **everything else** — all the elements in the universe ($\xi$) that are NOT in $A$. It only makes sense when you know what $\xi$ is.

### 中文锚点

补集：$A'$（或 $\complement_U A$）— 在全集中，不属于 $A$ 的所有元素。

> [!info] Chinese notation difference
> Chinese textbooks often write the complement as $\complement_U A$ (读作 "$A$ 关于 $U$ 的补集"). Cambridge and IB use $A'$. The concept is identical.

### Example

$$\xi = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}, \quad A = \{2, 4, 6, 8, 10\}$$
$$A' = \{1, 3, 5, 7, 9\}$$

---

## Key Properties

### Identity laws

$$A \cup \emptyset = A \qquad A \cap \xi = A$$

Union with nothing changes nothing. Intersection with everything changes nothing.

### Domination laws

$$A \cup \xi = \xi \qquad A \cap \emptyset = \emptyset$$

### Complement laws

$$A \cup A' = \xi \qquad A \cap A' = \emptyset$$

Together, $A$ and $A'$ cover the whole universe with no overlap.

### Double complement

$$(A')' = A$$

Complementing twice brings you back. "Not not $A$" is just $A$.

### Commutative laws

$$A \cup B = B \cup A \qquad A \cap B = B \cap A$$

Order doesn't matter.

### Associative laws

$$(A \cup B) \cup C = A \cup (B \cup C) \qquad (A \cap B) \cap C = A \cap (B \cap C)$$

Grouping doesn't matter — you can chain operations without worrying about brackets.

### Distributive laws

$$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$

Union distributes over intersection, and intersection distributes over union. This mirrors the Boolean algebra equivalents ($\text{OR}$ distributes over $\text{AND}$, and vice versa) — see [[Boolean Algebra]].

> [!tip] Verify with Venn diagrams
> These are easier to believe than to memorise. Draw a three-set Venn diagram, shade both sides of the equation, and confirm they match. This is a good exercise for students.

### De Morgan's Laws

$$(A \cup B)' = A' \cap B' \qquad (A \cap B)' = A' \cup B'$$

"Not (A or B)" = "not A and not B." "Not (A and B)" = "not A or not B."

These are essential for Venn diagram shading problems and connect directly to [[Boolean Algebra]]:

| Set operation | Boolean logic | English |
|---------------|---------------|---------|
| $A \cup B$ | $A$ OR $B$ | Either or both |
| $A \cap B$ | $A$ AND $B$ | Both |
| $A'$ | NOT $A$ | Everything except |
| $(A \cup B)'$ | NOT ($A$ OR $B$) = NOT $A$ AND NOT $B$ | Neither |
| $(A \cap B)'$ | NOT ($A$ AND $B$) = NOT $A$ OR NOT $B$ | Not both |

## Common Misconceptions (Teaching Notes)

### 1. Confusing $\cup$ and $\cap$

The #1 error. Mnemonics:

- $\cup$ looks like a **cup** (U shape) — it **collects** everything → Union
- $\cap$ looks like an upside-down cup (a **cap**/hat) — it only keeps what fits **under** both → Intersection

Or: $\cup$ = "**or**" (inclusive), $\cap$ = "**and**"

### 2. Thinking union means "add the numbers"

$\{1, 2, 3\} \cup \{4, 5\} \neq \{5, 7, 8\}$. Union combines elements, it doesn't perform arithmetic.

### 3. Forgetting that union includes the overlap

$A \cup B$ includes elements that are in BOTH — not just the ones exclusive to each. This is "inclusive or."

### 4. Computing complement without checking $\xi$

$A'$ has no meaning unless $\xi$ is defined. Students who skip reading the universal set will get the complement wrong every time.

### 5. De Morgan's — getting the swap wrong

Students remember "the complement distributes" but forget that $\cup$ and $\cap$ **swap**. Drill with Venn diagrams: shade $(A \cup B)'$ and separately shade $A' \cap B'$ — they're identical.

## Exam Notes

### Cambridge 0580 Core

- Required notation: $A \cup B$, $A \cap B$, $A'$
- Two-set Venn diagrams only
- Typical: "List the elements of $A \cap B'$" or "Shade the region representing $A' \cup B$"

### Cambridge 0580 Extended

- Three-set Venn diagrams
- Compound expressions: $(A \cup B) \cap C'$, $(A \cap B \cap C)'$
- Combined with cardinality: "Find $n((A \cup B)')$"
- De Morgan's is not explicitly named but is tested through shading and listing

## Connections

- **Parent concepts:** [[Set]], [[Element]], [[Subset]], [[Universal Set]], [[Empty Set]]
- **Counting:** [[Cardinality]] — inclusion-exclusion formula
- **Visual:** [[Venn Diagram]] — every region corresponds to a set expression
- **Logic:** [[Boolean Algebra]] — $\cup \leftrightarrow$ OR, $\cap \leftrightarrow$ AND, $' \leftrightarrow$ NOT
- **Probability:** [[Probability Basics]], [[Combined Probability]] — $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **CS bridge:** Python: `A | B` (union), `A & B` (intersection); [[Python Sets]]

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\cup$ | `\cup` | Union |
| $\cap$ | `\cap` | Intersection |
| $A'$ | `A'` | Complement (Cambridge/IB) |
| $\bar{A}$ | `\bar{A}` | Complement (alternative notation) |
| $\complement_U A$ | `\complement_U A` | Complement (Chinese textbooks) |
| $\xi$ | `\xi` | Universal set (Cambridge) |
| $\emptyset$ | `\emptyset` | Empty set |
| $\subseteq$ | `\subseteq` | Subset |
| $\text{or}$ | `\text{or}` | Text in math mode |
| $\text{and}$ | `\text{and}` | Text in math mode |
| $\qquad$ | `\qquad` | Wide space between expressions |
