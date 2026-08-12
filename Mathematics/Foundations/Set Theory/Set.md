---
chinese: 集合 (jíhé)
prerequisites: []
leads_to:
  - "[[Element]]"
  - "[[Subset]]"
  - "[[Empty Set]]"
  - "[[Set Operations]]"
  - "[[Venn Diagram]]"
  - "[[Cardinality]]"
  - "[[Set-Builder Notation]]"
  - "[[Natural Numbers]]"
  - "[[Function]]"
  - "[[Logic]]"
  - "[[Chain of Thought]]"
  - "[[Complement]]"
  - "[[Intersection]]"
  - "[[Number Sets (Vocab)]]"
  - "[[Probability Basics]]"
  - "[[Union]]"
  - "[[Universal Set]]"
tags:
  - subject/mathematics
  - domain/set-theory
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0580
  - curriculum/IB-AA
  - curriculum/IB-AI
  - curriculum/AP
  - curriculum/OxAQA-9260
  - syllabus/0580-E1-2
  - syllabus/9260-N9
  - type/definition
  - type/vocabulary
  - notation/curly-braces
  - notation/empty-set
  - notation/universal-set
  - misconception/set-vs-list
  - misconception/empty-set-confusion
  - misconception/notation-mixing
---

# Set 集合

## Definition

### Formal

A **set** is a well-defined, unordered collection of distinct objects, called **elements** (or **members**).

"Well-defined" means: for any object, we can determine with certainty whether it belongs to the set or not.

### Intuitive

A set is a bag of things — but a strange bag: it doesn't care what order you put things in, and it refuses to hold duplicates. If you throw in a second copy of something, the bag just ignores it.

### 中文锚点 (Chinese Anchor)

集合：一组**确定的**、**互不相同的**对象组成的整体。

与英文关键区别：
- 中文教材常写 "由…组成的整体"，英文强调 "well-defined"（确定性）
- 两边都要求互异性（no duplicates）和无序性（unordered）
- 概念本质相同，只是表述习惯不同

## Notation

| Convention | Example | Read as | Notes |
|---|---|---|---|
| Roster / List | $\{1, 2, 3\}$ | "the set containing 1, 2, 3" | Most common at IGCSE |
| Set-builder | $\{x \mid x > 0, x \in \mathbb{Z}\}$ | "the set of all x such that x is a positive integer" | 0606 and above |
| Named set | $A = \{1, 2, 3\}$ | "A is the set…" | Capital letters by convention |

> [!warning] Notation Trap
> Cambridge (IGCSE/A-Level) uses $\xi$ (xi) for the universal set.
> IB and most other curricula use $U$.
> Chinese textbooks use $U$ (全集).
> Flag this on day one — students will encounter both.

## Key Properties

1. **Unordered:** $\{1, 2, 3\} = \{3, 1, 2\}$
2. **No duplicates:** $\{1, 1, 2\} = \{1, 2\}$
3. **Well-defined:** "The set of tall people" is **not** a valid set. "The set of people over 180cm" **is**.

## Common Misconceptions (Teaching Notes)

### 1. "Isn't it just a list?"

Students who code (especially Python) confuse sets with lists/arrays. This is actually a useful bridge: Python has a `set` type that enforces uniqueness and ignores order — behaves exactly like a mathematical set. Use it.

```python
my_list = [1, 1, 2, 3, 3]  # keeps duplicates, has order
my_set = {1, 1, 2, 3, 3}   # becomes {1, 2, 3}
```

### 2. Empty set confusion

$\emptyset \neq \{\emptyset\}$

- $\emptyset$ is an empty bag — nothing inside.
- $\{\emptyset\}$ is a bag containing one item: an empty bag.

This trips students up at every level. Revisit when teaching [[Empty Set]] and [[Subset]].

### 3. Notation mixing

Chinese math uses $\{ \}$ too, so the symbol transfer is smooth. But watch for:
- Writing $\in$ backwards (mirror error)
- Confusing $\subset$ (proper subset) and $\subseteq$ (subset or equal)
- Cambridge uses $\subset$ to mean $\subseteq$ in some papers — check the syllabus notation list

## Exam Notes

### Cambridge 0580

- Sets appear in **Paper 2** (Extended) and **Paper 4** (Extended)
- Mostly Venn diagram problems + set notation
- Typical questions: "List the elements of…", "Find $n(A \cap B)$"
- Usually 2–3 marks per sub-question
- Sets are a tool for other topics (probability, number classification) — students need fluency, not deep theory

### Oxford AQA 9260

- Sets appear in both **Paper 1E** and **Paper 2E** (both allow calculators)
- Same core concepts: $n(A)$, $A'$, $\cup$, $\cap$, $\xi$, Venn diagrams
- Formal notation ($\in$, $\emptyset$, $\subseteq$) is not in the 9260 notation list but understanding them builds stronger foundations

## Connections

- **Components:** [[Element]], [[Subset]], [[Empty Set]], [[Universal Set]]
- **Operations:** [[Union]], [[Intersection]], [[Complement]], [[Set Operations]]
- **Notation:** [[Set-Builder Notation]], [[Cardinality]]
- **Visual tools:** [[Venn Diagram]]
- **Number systems:** [[Natural Numbers]], [[Number Sets (Vocab)|Number Sets]] ($\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$)
- **Functions:** [[Function]] — a set is the foundation; functions are mappings between sets
- **Logic bridge:** [[Boolean Algebra]] (via [[Set Operations]]: $\cap \leftrightarrow$ AND, $\cup \leftrightarrow$ OR, $' \leftrightarrow$ NOT)
- **CS bridge:** [[Python Sets]], [[Data Structures]]

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\{\ \}$ | `\{\ \}` | Curly braces (escaped in LaTeX) |
| $\emptyset$ | `\emptyset` | Empty set |
| $\in$ | `\in` | Element of |
| $\notin$ | `\notin` | Not element of |
| $\subset$ | `\subset` | Proper subset |
| $\subseteq$ | `\subseteq` | Subset or equal |
| $\cup$ | `\cup` | Union |
| $\cap$ | `\cap` | Intersection |
| $\xi$ | `\xi` | Xi (Cambridge universal set) |
| $\mathbb{N}$ | `\mathbb{N}` | Natural numbers (blackboard bold) |
| $\mathbb{Z}$ | `\mathbb{Z}` | Integers (blackboard bold) |
| $\mathbb{Q}$ | `\mathbb{Q}` | Rationals (blackboard bold) |
| $\mathbb{R}$ | `\mathbb{R}` | Reals (blackboard bold) |
| $\mid$ | `\mid` | "Such that" in set-builder |
| $\leftrightarrow$ | `\leftrightarrow` | Corresponds to / if and only if |
