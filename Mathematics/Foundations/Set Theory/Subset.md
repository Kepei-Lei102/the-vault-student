---
chinese: 子集 (zǐjí)
prerequisites:
  - "[[Set]]"
  - "[[Element]]"
leads_to:
  - "[[Empty Set]]"
  - "[[Universal Set]]"
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
  - notation/subset
  - notation/not-subset
  - notation/proper-subset
  - misconception/element-vs-subset
  - misconception/subset-symbol-ambiguity
---

# Subset 子集

## Definition

### Formal

A set $A$ is a **subset** of a set $B$ if every element of $A$ is also an element of $B$. We write:

$$A \subseteq B$$

This means: for all $x$, if $x \in A$ then $x \in B$.

If $A$ is a subset of $B$ but $A \neq B$ (i.e., $B$ has at least one element not in $A$), then $A$ is a **proper subset** of $B$:

$$A \subset B$$

If $A$ is **not** a subset of $B$, we write:

$$A \nsubseteq B$$

This means: there exists at least one element in $A$ that is not in $B$.

### Intuitive

If sets are bags, then $A \subseteq B$ means everything in bag $A$ is also in bag $B$. Bag $A$ might be identical to bag $B$ (that's still a subset), or it might be smaller. The only thing that would break it is finding something in $A$ that isn't in $B$.

A **proper** subset means $A$ fits inside $B$ but $B$ has extra stuff — they're not the same bag.

### 中文锚点 (Chinese Anchor)

子集：如果集合 $A$ 中的**每一个**元素都属于集合 $B$，则 $A$ 是 $B$ 的子集。

- $A \subseteq B$ 读作 "$A$ 是 $B$ 的子集"（或 "$A$ 包含于 $B$"）
- $A \subset B$ 读作 "$A$ 是 $B$ 的真子集"
- 中文教材通常用 $\subseteq$ 表示子集，$\subsetneq$ 或 $\subset$ 表示真子集
- 中英文符号用法基本一致

## Notation

| Symbol | Meaning | Example |
|--------|---------|---------|
| $A \subseteq B$ | $A$ is a subset of $B$ (could be equal) | $\{1, 2\} \subseteq \{1, 2, 3\}$ ✓ |
| $A \subset B$ | $A$ is a proper subset of $B$ (not equal) | $\{1, 2\} \subset \{1, 2, 3\}$ ✓ |
| $A \nsubseteq B$ | $A$ is not a subset of $B$ | $\{1, 4\} \nsubseteq \{1, 2, 3\}$ ✓ |

> [!info] Cross-curriculum note
> Always teach the strict distinction: $\subseteq$ (subset, could be equal) vs. $\subset$ (proper subset, strictly smaller). This is precise and universally accepted. Some Cambridge papers blur this — they'll accept either — but the strict version never causes problems anywhere.

## Key Facts

### Every set is a subset of itself

$$A \subseteq A \text{ is always true}$$

This follows directly from the definition: every element of $A$ is in $A$. Trivially true, but students find it strange at first.

### The empty set is a subset of every set

$$\emptyset \subseteq A \text{ is always true, for any set } A$$

This is an example of **vacuous truth** (空真). It's a tricky concept — here are three ways to explain it:

> [!note] Explanation 1: The courtroom
> To prove $\emptyset \nsubseteq A$, you'd need to present evidence: an element of $\emptyset$ that's not in $A$. But $\emptyset$ has no elements — you can't produce a single witness. Case dismissed. The claim $\emptyset \subseteq A$ wins by default.

> [!note] Explanation 2: The checklist
> To verify $\emptyset \subseteq A$, go through every element of $\emptyset$ and check if it's in $A$. Pick up the first element... there isn't one. You're done. Every element (all zero of them) passed the check. ✓

> [!note] Explanation 3: The rule that can't be broken
> "$\emptyset \subseteq A$" means "nothing in $\emptyset$ violates membership in $A$." A rule that has zero opportunities to be broken is never broken. An empty classroom has no students failing the exam — so technically, every student passed.

See [[Empty Set]] for more on vacuous truth.

### Counting subsets

A set with $n$ elements has exactly $2^n$ subsets (including $\emptyset$ and the set itself). See [[Indices]] for more on powers.

| Set | Elements | Subsets | Count |
|-----|----------|---------|-------|
| $\{a\}$ | 1 | $\emptyset, \{a\}$ | $2^1 = 2$ |
| $\{a, b\}$ | 2 | $\emptyset, \{a\}, \{b\}, \{a, b\}$ | $2^2 = 4$ |
| $\{a, b, c\}$ | 3 | $\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, \{a,b,c\}$ | $2^3 = 8$ |

> [!tip] CS Connection
> $2^n$ subsets — this is the **power set**. In CS, this connects directly to binary: each element is either "in" (1) or "out" (0), giving $n$ binary choices = $2^n$ combinations.

## Common Misconceptions (Teaching Notes)

### 1. Confusing $\in$ and $\subseteq$

This is the #1 error. Drill it relentlessly:

| Statement | Correct? | Why |
|-----------|----------|-----|
| $1 \in \{1, 2, 3\}$ | ✓ | 1 is an **object** inside the set |
| $\{1\} \subseteq \{1, 2, 3\}$ | ✓ | {1} is a **set** whose elements are all in {1, 2, 3} |
| $1 \subseteq \{1, 2, 3\}$ | ✗ | 1 is not a set — $\subseteq$ compares **sets** |
| $\{1\} \in \{1, 2, 3\}$ | ✗ | the set {1} is not an element of {1, 2, 3} — the number 1 is |

The rule: $\in$ relates an **object** to a **set**. $\subseteq$ relates a **set** to a **set**.

### 2. "The empty set can't be a subset — it has nothing in it!"

See the three explanations above. Pick whichever one clicks with the student.

### 3. Confusing "subset" with "smaller"

$A \subseteq B$ does **not** mean $A$ is smaller than $B$. It means $A$ is **contained** in $B$. In particular, $A \subseteq A$ — a set is a subset of itself. Only **proper** subset ($\subset$) guarantees $A \neq B$.

### 4. Order of the symbol

$A \subseteq B$ means $A$ is inside $B$ — the "open" side of $\subseteq$ faces the bigger set. Students sometimes reverse it. Mnemonic: $\subseteq$ looks like $\leq$ — the small thing is on the left.

## Exam Notes

### Cambridge 0580 Extended

- Notation required: $\subseteq$ and $\nsubseteq$
- Proper subset ($\subset$) is not in the 0580 notation list, but is accepted and never penalised
- Typical question: "Is $B \subseteq A$? Give a reason." — student must check if every element of $B$ is in $A$
- Often appears alongside Venn diagrams: if one circle is entirely inside another, that's a subset relationship

### OxAQA 9260

- The $\subseteq$ and $\nsubseteq$ notation is **not** in the 9260 notation list and is **not formally assessed**
- The concept of subset is still implicit in Venn diagram reasoning (N9) — e.g., when one set is entirely contained in another
- Useful background knowledge but students will not be asked to use the notation on the 9260 paper

## Connections

- **Parent concepts:** [[Set]], [[Element]]
- **Sibling:** [[Empty Set]] — the empty set is a subset of everything
- **Leads to:** [[Universal Set]], [[Set Operations]], [[Venn Diagram]]
- **Counting:** [[Cardinality]] — $2^{n(A)}$ subsets; [[Indices]] — why $2^n$
- **Logic bridge:** $A \subseteq B$ is equivalent to "if $x \in A$ then $x \in B$" — this is an implication ([[Boolean Algebra]])
- **CS bridge:** `A.issubset(B)` or `A <= B` in Python

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\subseteq$ | `\subseteq` | Subset or equal |
| $\nsubseteq$ | `\nsubseteq` | Not a subset |
| $\subset$ | `\subset` | Proper subset (strictly smaller) |
| $\subsetneq$ | `\subsetneq` | Proper subset (alternative, used in CN textbooks) |
| $\supseteq$ | `\supseteq` | Superset or equal (reverse direction) |
| $\supset$ | `\supset` | Proper superset |
| $\in$ | `\in` | Element of (compare with $\subseteq$) |
| $\emptyset$ | `\emptyset` | Empty set |
| $2^n$ | `2^n` | Superscript / exponent |
| $\neq$ | `\neq` | Not equal |
| $\forall$ | `\forall` | Universal quantifier ("for all", beyond 0580) |
