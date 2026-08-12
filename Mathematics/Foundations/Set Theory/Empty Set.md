---
chinese: 空集 (kōngjí)
prerequisites:
  - "[[Set]]"
  - "[[Element]]"
  - "[[Subset]]"
leads_to:
  - "[[Set Operations]]"
  - "[[Venn Diagram]]"
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
  - type/definition
  - type/vocabulary
  - notation/empty-set
  - misconception/empty-set-confusion
  - misconception/empty-set-vs-zero
---

# Empty Set 空集

## Definition

### Formal

The **empty set** (or **null set**) is the unique set that contains no elements. It is denoted:

$$\emptyset \quad \text{or} \quad \{ \}$$

Formally: there is no $x$ such that $x \in \emptyset$.

### Intuitive

The empty set is an empty bag. It's still a bag — it exists as a container — it just has nothing inside. Think of an empty box: the box is real, but if you open it, there's nothing there.

### 中文锚点 (Chinese Anchor)

空集：不含任何元素的集合，记作 $\emptyset$ 或 $\{ \}$。

- 中文教材常强调："空集是集合"（不是"什么都没有"）
- 空集是**唯一的** — 只有一个空集，就像只有一个数字 0
- 符号 $\emptyset$ 来自挪威/丹麦字母 Ø，不是希腊字母 φ (phi)

## Notation

| Symbol | LaTeX | Meaning | Notes |
|--------|-------|---------|-------|
| $\emptyset$ | `\emptyset` | The empty set | Preferred in most curricula |
| $\{ \}$ | `\{ \}` | The empty set (alternative) | More explicit — visibly empty braces |
| $\varnothing$ | `\varnothing` | The empty set (variant) | Rounder version, sometimes preferred |

> [!warning] Not Zero, Not Nothing
> $\emptyset$ is **not** the number $0$. It is not "nothing." It is a **set** — a valid mathematical object — that happens to contain no elements.
>
> $0$ is a number. $\emptyset$ is a set. They live in different categories entirely.

## Key Facts

### The empty set is a subset of every set

$$\emptyset \subseteq A \quad \text{for any set } A$$

See [[Subset]] for three different explanations of why this works (vacuous truth).

### The empty set is unique

There is only one empty set. If you define $X = \{x : x \neq x\}$ and $Y = \{x : x > x\}$, both are empty — and they're the **same** set, because two sets are equal when they have exactly the same elements (which is none).

### Cardinality of the empty set

$$n(\emptyset) = 0$$

The empty set has zero elements. See [[Cardinality]].

### The empty set has exactly one subset

$$\text{Subsets of } \emptyset = \{ \emptyset \}$$

That's $2^0 = 1$ subset: just the empty set itself. See [[Subset]] and [[Indices]].

## Common Misconceptions (Teaching Notes)

### 1. $\emptyset$ vs. $\{\emptyset\}$

This is the classic trap:

| Expression | What is it? | How many elements? |
|------------|-------------|-------------------|
| $\emptyset$ | The empty set | 0 |
| $\{\emptyset\}$ | A set containing the empty set | 1 |
| $\{\{\emptyset\}\}$ | A set containing a set containing the empty set | 1 |

$\emptyset$ is an empty bag. $\{\emptyset\}$ is a bag with one item inside — and that item happens to be an empty bag. The outer bag is **not** empty.

### 2. "There's no such thing as an empty set"

Students sometimes reject it as meaningless. Counter-examples help:

- "The set of months with 32 days" → $\emptyset$
- "The set of prime numbers between 14 and 16" → $\emptyset$ (15 = 3×5, not prime)
- "The set of students who scored above 100% on the test" → $\emptyset$

These are all well-defined sets that happen to be empty. The set is valid; it just has no members.

### 3. Writing $\emptyset$ as $\{0\}$

$\{0\}$ is a set containing the number zero — it has one element! It is **not** empty. The number $0$ and the empty set $\emptyset$ are completely different things.

### 4. Writing $\{\emptyset\}$ when they mean $\emptyset$

Common notation error. Remind students: if the answer is "no elements," write $\emptyset$ or $\{ \}$, not $\{\emptyset\}$.

## Exam Notes

### Cambridge 0580 Extended

- $\emptyset$ is in the required notation list
- Appears in: "Find $A \cap B$" where $A$ and $B$ have no common elements → answer is $\emptyset$
- Venn diagram context: non-overlapping regions correspond to empty intersections
- Core (C1.2) does **not** require the $\emptyset$ symbol — only Extended

### OxAQA 9260

- The $\emptyset$ notation is **not** in the 9260 notation list and is **not formally assessed**
- The concept still appears implicitly: "there are no elements in $A \cap B$" is common in Venn diagram problems (N9)
- Students may write "no members" or "none" rather than $\emptyset$ on the 9260 paper

## Connections

- **Parent concepts:** [[Set]], [[Element]], [[Subset]]
- **Properties:** [[Cardinality]] — $n(\emptyset) = 0$
- **Operations:** [[Set Operations]] — $A \cap A' = \emptyset$; $A \cup \emptyset = A$
- **Visual:** [[Venn Diagram]] — empty intersections
- **Number parallel:** [[Indices]] — $2^0 = 1$ (number of subsets of $\emptyset$)
- **Logic:** Vacuous truth — any statement about "all elements of $\emptyset$" is true
- **CS bridge:** `set()` in Python creates an empty set (not `{}`, which creates an empty dict!)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\emptyset$ | `\emptyset` | Empty set (standard) |
| $\varnothing$ | `\varnothing` | Empty set (rounder variant) |
| $\{ \}$ | `\{ \}` | Empty braces |
| $\{\emptyset\}$ | `\{\emptyset\}` | Set containing the empty set (NOT empty!) |
| $n(\emptyset)$ | `n(\emptyset)` | Cardinality of empty set |
| $\subseteq$ | `\subseteq` | Subset — $\emptyset \subseteq A$ always |
| $\cap$ | `\cap` | Intersection — relevant for empty results |
