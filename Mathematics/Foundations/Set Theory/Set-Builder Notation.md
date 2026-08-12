---
chinese: 集合描述法 (jíhé miáoshù fǎ)
prerequisites:
  - "[[Set]]"
  - "[[Element]]"
  - "[[Number Sets (Vocab)]]"
leads_to:
  - "[[Function]]"
  - "[[Linear Inequalities (Vocab)]]"
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
  - notation/set-builder
  - misconception/reading-set-builder
---

# Set-Builder Notation 描述法

## Definition

### Formal

**Set-builder notation** defines a set by stating a property that its elements must satisfy:

$$\{x : P(x)\} \quad \text{or} \quad \{x \mid P(x)\}$$

Read as: "the set of all $x$ such that $P(x)$ is true."

The colon $:$ and the vertical bar $\mid$ both mean "such that" — they are interchangeable.

### Intuitive

Instead of listing every element, you describe a **rule** for membership. It's like a bouncer at a door: "you can come in if and only if you meet this condition."

Roster notation: $\{2, 4, 6, 8, 10\}$ — here's the guest list.
Set-builder notation: $\{x : x \text{ is even}, 1 < x \leq 10\}$ — here's the entry rule.

### 中文锚点 (Chinese Anchor)

描述法（或特征性质描述法）：用元素的**共同特征**来描述集合。

- $\{x \mid P(x)\}$ 读作 "满足条件 $P(x)$ 的所有 $x$ 的集合"
- 竖线 $\mid$ 或冒号 $:$ 均表示 "使得"（such that）
- 中文教材常用竖线 $\mid$，Cambridge 两种都用

## Reading Set-Builder Notation

Breaking down the parts:

$$\{\ \underbrace{x}_{\text{variable}}\ :\ \underbrace{x > 0,\ x \in \mathbb{Z}}_{\text{conditions}}\ \}$$

| Part | Role | In this example |
|------|------|-----------------|
| $x$ | The variable (placeholder for elements) | Any value we're testing |
| $:$ or $\mid$ | "such that" | Divider between variable and conditions |
| $x > 0$ | A condition the element must satisfy | Must be positive |
| $x \in \mathbb{Z}$ | Domain restriction | Must be an integer |

Result: $\{1, 2, 3, 4, 5, \ldots\}$ — the positive integers.

## Common Patterns

### Numbers with a property

$$A = \{x : x \text{ is a prime number}\} = \{2, 3, 5, 7, 11, \ldots\}$$

### Numbers in a range

$$B = \{x : 1 \leq x \leq 5, x \in \mathbb{Z}\} = \{1, 2, 3, 4, 5\}$$

### With a formula

$$C = \{x : x = 2n, n \in \mathbb{N}\} = \{0, 2, 4, 6, 8, \ldots\}$$

Note: $\mathbb{N}$ includes 0 in this vault. See [[Natural Numbers]].

### Ordered pairs (Extended / 0606)

$$D = \{(x, y) : y = 2x + 1\}$$

This defines a set of coordinate points — it's a bridge to [[Function]] and graphing.

## Converting Between Notations

| Roster | Set-builder | Notes |
|--------|-------------|-------|
| $\{1, 2, 3, 4, 5\}$ | $\{x : 1 \leq x \leq 5, x \in \mathbb{Z}\}$ | Finite, easy to list |
| $\{0, 2, 4, 6, \ldots\}$ | $\{x : x = 2n, n \in \mathbb{N}\}$ | Infinite — must use set-builder |
| $\{1, 4, 9, 16, 25\}$ | $\{x : x = n^2, n \in \mathbb{Z}, 1 \leq n \leq 5\}$ | Pattern-based |

> [!tip] When to use which?
> - **Roster** for small, finite sets where listing is clearer
> - **Set-builder** for infinite sets, large sets, or when the defining property matters more than the list
> - Exams often ask you to convert one to the other

## Common Misconceptions (Teaching Notes)

### 1. Not knowing how to read the notation

Students see $\{x : x^2 < 25, x \in \mathbb{Z}\}$ and freeze. Teach them to:
1. Identify the variable ($x$)
2. Read the condition ($x^2 < 25$)
3. Check the domain ($x \in \mathbb{Z}$ — integers)
4. List: $x = -4, -3, -2, -1, 0, 1, 2, 3, 4$

### 2. Forgetting the domain restriction

$\{x : x^2 < 25\}$ without specifying $x \in \mathbb{Z}$ is the interval $(-5, 5)$ on the real line — infinitely many values. The domain restriction completely changes the set.

### 3. Confusing $:$ and $\mid$ with division

$\{x \mid x > 3\}$ — the vertical bar is NOT division or absolute value here. Context matters: inside $\{\ \}$ after a variable, it means "such that."

### 4. Treating it as an equation

$\{x : x + 3 = 7\} = \{4\}$ — this set has exactly one element. Students sometimes write the answer as $x = 4$ instead of the set $\{4\}$.

## Exam Notes

### Cambridge 0580

- **Core:** set definitions given in words or roster: $A = \{a, b, c, \ldots\}$, $C = \{x : a \leq x \leq b\}$
- **Extended:** must interpret and use set-builder notation with conditions
- Example definition from syllabus: $A = \{x : x \text{ is a natural number}\}$, $B = \{(x, y) : y = mx + c\}$

### OxAQA 9260

- Set-builder notation is **not explicitly listed** in the 9260 specification (N9)
- Sets in 9260 are typically defined by roster or verbal description
- Still valuable for building understanding, especially when linking to inequalities (A23) and function domains (A9)

## Connections

- **Parent:** [[Set]], [[Element]]
- **Notation sibling:** Roster notation (listing) is the alternative — both live in [[Set]]
- **Domain:** [[Number Sets (Vocab)|Number Sets]] — $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ define what $x$ can be
- **Leads to:** [[Function]] — $f : A \to B$ uses set-builder ideas for domain/range
- **Leads to:** [[Linear Inequalities (Vocab)|Linear Inequalities]], [[Graphical Inequalities (Vocab)|Graphical Inequalities]] — conditions become regions
- **CS bridge:** List comprehensions in Python: `{x for x in range(11) if x % 2 == 0}`

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\{x : \ldots\}$ | `\{x : \ldots\}` | Set-builder with colon |
| $\{x \mid \ldots\}$ | `\{x \mid \ldots\}` | Set-builder with bar |
| $\in$ | `\in` | Element of (domain restriction) |
| $\mathbb{N}$ | `\mathbb{N}` | Natural numbers (includes 0) |
| $\mathbb{Z}$ | `\mathbb{Z}` | Integers |
| $\mathbb{Q}$ | `\mathbb{Q}` | Rationals |
| $\mathbb{R}$ | `\mathbb{R}` | Reals |
| $\leq$ | `\leq` | Less than or equal |
| $\geq$ | `\geq` | Greater than or equal |
| $n^2$ | `n^2` | Superscript |
| $x^2$ | `x^2` | Squared |
