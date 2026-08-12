---
chinese: 韦恩图 (wéi'ēn tú)
prerequisites:
  - "[[Set]]"
  - "[[Element]]"
  - "[[Subset]]"
  - "[[Universal Set]]"
  - "[[Set Operations]]"
  - "[[Cardinality]]"
  - "[[Complement]]"
  - "[[Empty Set]]"
  - "[[Intersection]]"
  - "[[Union]]"
leads_to:
  - "[[Probability Basics]]"
  - "[[Combined Probability]]"
  - "[[Conditional Probability]]"
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
  - type/visual-tool
  - type/vocabulary
  - misconception/venn-region-counting
  - misconception/venn-shading
---

# Venn Diagram 韦恩图

## Definition

### Formal

A **Venn diagram** is a visual representation of sets and their relationships. Sets are drawn as closed curves (usually circles) inside a rectangle that represents the [[Universal Set]] $\xi$. The spatial relationships between the curves show intersections, unions, and complements.

### Intuitive

A Venn diagram is a map of sets. The rectangle is the whole world ($\xi$). Each circle is a set. Where circles overlap, elements belong to multiple sets. Where circles don't overlap, elements belong to only one set. Everything outside the circles (but inside the rectangle) belongs to no set — it's in the complement.

### 中文锚点 (Chinese Anchor)

韦恩图（又称文氏图）：用封闭曲线表示集合之间关系的图形。

- 矩形 = 全集 $\xi$（或 $U$）
- 圆/椭圆 = 各个集合
- 重叠区域 = 交集
- 中文教材和英文教材的韦恩图画法完全一致

## Anatomy of a Venn Diagram

### Two-set diagram — 4 regions

![[venn-2-sets-regions.svg]]

For sets $A$ and $B$ inside $\xi$, there are exactly **4 regions**:

| Region | Set notation | Meaning |
|--------|-------------|---------|
| 1 | $A \cap B'$ | In $A$ only (not in $B$) |
| 2 | $A \cap B$ | In both $A$ and $B$ |
| 3 | $A' \cap B$ | In $B$ only (not in $A$) |
| 4 | $(A \cup B)'$ | In neither — outside both circles |

> [!tip] The 4-region rule
> Every element in $\xi$ lives in exactly one of these 4 regions. The regions are **mutually exclusive** (no overlap) and **exhaustive** (they cover everything). So:
> $$n(\xi) = n(A \cap B') + n(A \cap B) + n(A' \cap B) + n((A \cup B)')$$

### Three-set diagram — 8 regions

![[venn-3-sets-regions.svg]]

For sets $A$, $B$, and $C$ inside $\xi$, there are exactly **8 regions** (Extended only):

| Region | Set notation |
|--------|-------------|
| ① | $A \cap B' \cap C'$ — only $A$ |
| ② | $A \cap B \cap C'$ — $A$ and $B$ only |
| ③ | $A' \cap B \cap C'$ — only $B$ |
| ④ | $A \cap B' \cap C$ — $A$ and $C$ only |
| ⑤ | $A \cap B \cap C$ — all three |
| ⑥ | $A' \cap B \cap C$ — $B$ and $C$ only |
| ⑦ | $A' \cap B' \cap C$ — only $C$ |
| ⑧ | $(A \cup B \cup C)'$ — none |

> [!tip] Why 8?
> Each element has 3 yes/no choices: in $A$? in $B$? in $C$? That gives $2^3 = 8$ combinations. See [[Indices]].

## How to Solve Venn Diagram Problems

### Strategy: work from the inside out

1. **Start with the innermost region** — the centre overlap ($A \cap B$ for two sets, $A \cap B \cap C$ for three)
2. **Work outward** — fill in the "only" regions by subtracting what's already placed
3. **Fill the outside last** — $n((A \cup B)') = n(\xi)$ minus everything inside the circles
4. **Check:** all regions should add up to $n(\xi)$

### Example (two sets)

$\xi = \{1, 2, 3, \ldots, 10\}$, $A = \{1, 2, 3, 4, 5\}$, $B = \{3, 4, 5, 6, 7\}$

1. $A \cap B = \{3, 4, 5\}$ → centre = 3 elements
2. $A$ only: $\{1, 2\}$ → 2 elements
3. $B$ only: $\{6, 7\}$ → 2 elements
4. Outside: $\{8, 9, 10\}$ → 3 elements
5. Check: $2 + 3 + 2 + 3 = 10 = n(\xi)$ ✓

## Shading Regions

A common exam task: "Shade the region representing $X$." The approach:

1. Identify each set in the expression
2. Apply operations step by step
3. The final result is the region to shade

| Expression | What to shade |
|------------|---------------|
| $A \cup B$ | Everything inside at least one circle |
| $A \cap B$ | Only the overlap |
| $A'$ | Everything outside $A$'s circle (including outside both) |
| $A \cap B'$ | The part of $A$ that doesn't overlap with $B$ |
| $(A \cup B)'$ | Everything outside both circles |
| $A' \cap B'$ | Same as $(A \cup B)'$ — De Morgan's Law! |
| $(A \cap B)'$ | Everything EXCEPT the overlap |
| $A' \cup B'$ | Same as $(A \cap B)'$ — De Morgan's Law! |

> [!info] Cambridge shading convention
> In Cambridge 0580, the **required** region is shaded. Some other curricula shade the **unwanted** region instead. Always read the question: "shade" vs. "shade the region that is NOT in..."

## Common Misconceptions (Teaching Notes)

### 1. Not starting from the centre

Students try to fill in $n(A)$ first, then $n(B)$, then the intersection — but this double-counts the overlap. Always start with $A \cap B$ and work outward.

### 2. Writing $n(A) = 15$ inside the $A$-only region

If $n(A) = 15$ and $n(A \cap B) = 6$, the "$A$ only" region has $15 - 6 = 9$, not 15. The number in each region is the number of elements in THAT REGION ONLY, not the total of the set.

### 3. Forgetting the outside region

The rectangle matters. Elements in $\xi$ but not in any named set go outside the circles. Students who forget this get $n(\xi)$ wrong.

### 4. Three-set overlap confusion

In three-set diagrams, $A \cap B$ includes the centre ($A \cap B \cap C$). The region that is "$A$ and $B$ but not $C$" is $A \cap B \cap C'$. Students often place elements in the wrong overlapping leaf.

### 5. Confusing "shade $A \cup B$" with "shade $A \cap B$"

Draw both side by side. Union = "colour everything that's in at least one." Intersection = "colour only what's in both." The $\cup$/$\cap$ confusion from [[Set Operations]] shows up visually here.

## Exam Notes

### Cambridge 0580 Core

- **Two-set** Venn diagrams only
- Tasks: shade regions, list elements, find cardinalities
- Usually 3–5 marks per question

### Cambridge 0580 Extended

- **Two and three-set** Venn diagrams
- Combined with cardinality algebra: "Given $n(A) = 12$, $n(B) = 15$, $n(A \cap B) = x$, $n(\xi) = 30$. Find $x$."
- Shading of compound expressions: $(A \cap B') \cup C$
- Usually 4–6 marks, multi-step

## Connections

- **Parent concepts:** [[Set]], [[Set Operations]], [[Universal Set]], [[Cardinality]]
- **Key formula:** Inclusion-exclusion — see [[Cardinality]]
- **Logic:** [[Boolean Algebra]] — De Morgan's Laws become visible in Venn diagrams
- **Probability:** [[Probability Basics]], [[Combined Probability]] — Venn diagrams for $P(A \cup B)$, $P(A \mid B)$
- **CS bridge:** SQL: INNER JOIN ↔ $\cap$, UNION ↔ $\cup$, NOT IN ↔ complement

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\cup$ | `\cup` | Union |
| $\cap$ | `\cap` | Intersection |
| $A'$ | `A'` | Complement |
| $\xi$ | `\xi` | Universal set (Cambridge) |
| $n(A)$ | `n(A)` | Cardinality |
| $\emptyset$ | `\emptyset` | Empty set (disjoint sets) |
| $\subseteq$ | `\subseteq` | Subset (circle inside circle) |
| $2^n$ | `2^n` | Number of regions: $2^{\text{sets}}$ |
