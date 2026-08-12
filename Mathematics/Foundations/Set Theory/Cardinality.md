---
chinese: 基数/元素个数 (jīshù / yuánsù gèshù)
prerequisites:
  - "[[Set]]"
  - "[[Element]]"
  - "[[Intersection]]"
  - "[[Union]]"
leads_to:
  - "[[Venn Diagram]]"
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
  - notation/cardinality
  - misconception/cardinality-vs-set
---

# Cardinality 基数

## Definition

### Formal

The **cardinality** of a set $A$, written $n(A)$ or $\lvert A \rvert$, is the number of distinct elements in $A$.

$$A = \{2, 4, 6, 8\} \implies n(A) = 4$$

### Intuitive

Cardinality is just counting: how many things are in the bag? Open the set, count the elements, that's the cardinality.

### 中文锚点 (Chinese Anchor)

基数（或元素个数）：集合中不同元素的数量。

- $n(A)$ 读作 "集合 $A$ 的元素个数"
- 中文教材有时写作 $\text{card}(A)$，但 $n(A)$ 最常见
- IGCSE 只用 $n(A)$ 记法

## Notation

| Context | Symbol | Example |
|---------|--------|---------|
| IGCSE / Cambridge | $n(A)$ | $n(\{a, b, c\}) = 3$ |
| IB / university | $\lvert A \rvert$ | $\lvert \{a, b, c\} \rvert = 3$ |
| Some textbooks | $\text{card}(A)$ | $\text{card}(\{a, b, c\}) = 3$ |
| Chinese textbooks | $n(A)$ or $\lvert A \rvert$ | Both used |

> [!info] Which notation to use?
> At IGCSE level, always use $n(A)$. At IB and above, $\lvert A \rvert$ is standard. Teach both — the concept is identical.

## Key Facts

### Basic examples

| Set | Cardinality | Notes |
|-----|-------------|-------|
| $\{1, 2, 3\}$ | $n = 3$ | |
| $\{a\}$ | $n = 1$ | A **singleton** set |
| $\emptyset$ | $n = 0$ | The empty set — see [[Empty Set]] |
| $\{1, 1, 2, 2, 3\}$ | $n = 3$ | Duplicates don't count — this is $\{1, 2, 3\}$ |

### The inclusion-exclusion principle (two sets)

For two sets $A$ and $B$ within universal set $\xi$:

$$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$

Why subtract $n(A \cap B)$? Because elements in the overlap get counted twice — once in $n(A)$ and once in $n(B)$. Subtracting corrects the double-count.

This is the single most important formula for Venn diagram problems. See [[Venn Diagram]] and [[Set Operations]].

### The inclusion-exclusion principle (three sets)

$$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C)$$

Extended only — three-set Venn diagrams.

### Complement counting

$$n(A') = n(\xi) - n(A)$$

The number of elements NOT in $A$ equals the total minus those in $A$. See [[Complement]] and [[Universal Set]].

## Common Misconceptions (Teaching Notes)

### 1. Counting duplicates

$n(\{1, 1, 2, 3, 3, 3\}) = 3$, not 6. A set removes duplicates first, then you count.

### 2. Confusing $n(A)$ with the set itself

$n(A)$ is a **number**. $A$ is a **set**. Students sometimes write $n(A) = \{3\}$ instead of $n(A) = 3$.

### 3. Forgetting to subtract the intersection

In $n(A \cup B) = n(A) + n(B) - n(A \cap B)$, students frequently forget the $- n(A \cap B)$ and get a number that's too big. Draw the Venn diagram — the overlap is visually obvious.

### 4. Not reading the universal set

"Find $n(A')$" requires knowing $n(\xi)$. Students who skip reading $\xi$ can't answer complement questions.

## Exam Notes

### Cambridge 0580

- $n(A)$ notation is required for both Core and Extended
- **Core:** two-set Venn diagrams, basic inclusion-exclusion
- **Extended:** three-set Venn diagrams, inclusion-exclusion with three sets
- Very common question type: "Given $n(\xi) = 40$, $n(A) = 15$, $n(B) = 20$, $n(A \cap B) = 8$. Find $n((A \cup B)')$."
- Typical marks: 3–6 per question (multi-step)

## Connections

- **Parent concepts:** [[Set]], [[Element]]
- **Key formula partner:** [[Set Operations]] — inclusion-exclusion
- **Visual:** [[Venn Diagram]] — filling in regions uses cardinality
- **Special case:** [[Empty Set]] — $n(\emptyset) = 0$
- **Complement:** [[Complement]], [[Universal Set]] — $n(A') = n(\xi) - n(A)$
- **Counting:** [[Subset]] — a set with $n$ elements has $2^n$ subsets; [[Indices]]
- **Probability:** [[Probability Basics]] — $P(A) = \dfrac{n(A)}{n(\xi)}$ for equally likely outcomes
- **CS bridge:** `len(my_set)` in Python

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $n(A)$ | `n(A)` | Cardinality (IGCSE notation) |
| $\lvert A \rvert$ | `\lvert A \rvert` | Cardinality (IB/university notation) |
| $\cup$ | `\cup` | Union — used in inclusion-exclusion |
| $\cap$ | `\cap` | Intersection — the overlap |
| $A'$ | `A'` | Complement |
| $\xi$ | `\xi` | Universal set |
| $\dfrac{a}{b}$ | `\frac{a}{b}` or `\dfrac{a}{b}` | Fraction (`\dfrac` for inline) |
| $\implies$ | `\implies` | Implies |
