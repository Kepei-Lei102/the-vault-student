---
chinese: 排列与组合 (páiliè yǔ zǔhé)
prerequisites:
  - "[[Probability Basics]]"
  - "[[Factorial Notation]]"
leads_to:
  - "[[Counting Problems]]"
  - "[[Binomial Theorem]]"
  - "[[Combined Probability]]"
  - "[[Discrete Random Variables]]"
tags:
  - subject/mathematics
  - domain/probability
  - domain/combinatorics
  - level/pre-IB
  - level/pre-AP
  - level/A-Level
  - curriculum/Cambridge-0606
  - curriculum/Cambridge-9709
  - curriculum/A-Level
  - curriculum/IB-AA
  - syllabus/0606-11-1
  - syllabus/0606-11-2
  - syllabus/9709-5-2
  - type/definition
  - type/vocabulary
  - notation/factorial
  - notation/nPr
  - notation/nCr
  - misconception/permutation-vs-combination
---

# Permutations and Combinations 排列与组合

## Definition

### Formal

A **permutation** is an ordered arrangement of objects. The number of ways to arrange $r$ objects chosen from $n$ distinct objects is:

$${}^nP_r = \dfrac{n!}{(n-r)!}$$

A **combination** is an unordered selection of objects. The number of ways to choose $r$ objects from $n$ distinct objects (ignoring order) is:

$${}^nC_r = \binom{n}{r} = \dfrac{n!}{r!(n-r)!}$$

where **factorial** notation means:

$$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1$$

with the special case $0! = 1$.

### Intuitive

The core question is: **does the order matter?**

Take the same 3 people — Alice, Bob, and Charlie:

- **Permutation** (order matters): they're posing for a **photo** in a line. Alice-Bob-Charlie and Charlie-Alice-Bob are **different photos**. That's $3! = 6$ arrangements.
- **Combination** (order doesn't matter): they're forming a **team**. Alice-Bob-Charlie and Charlie-Alice-Bob are **the same team**. That's just 1 group.

Same 3 people, but the permutation counts 6 while the combination counts 1 — because the combination merges all $3! = 6$ rearrangements into one.

The relationship between them is always this:

$${}^nC_r = \dfrac{{}^nP_r}{r!}$$

Every combination corresponds to $r!$ permutations (all the ways you could rearrange the same $r$ objects). So combinations are always fewer — you divide by the number of rearrangements to remove the overcounting.

### 中文锚点 (Chinese Anchor)

**排列** (páiliè)："排"是排队，"列"是排列——把东西排成一队，**顺序重要**。
**组合** (zǔhé)："组"是分组，"合"是合在一起——把东西放在一组里，**顺序不重要**。

判断方法：问自己"调换位置，结果一样吗？"

- 一样 → 组合（选委员会：AB和BA是同一组人）
- 不一样 → 排列（排名次：第一名和第二名不能换）

$$\text{排列} = {}^nP_r = \dfrac{n!}{(n-r)!} \qquad \text{组合} = {}^nC_r = \dfrac{n!}{r!(n-r)!}$$

组合比排列少，因为组合把"重复的排列方式"($r!$种)都合并了。

## Factorial Notation

See [[Factorial Notation]] for the full treatment — definition, table of values, why $0! = 1$ (three reasons), and the connection to recursion.

**Quick reminder:** $n! = n \times (n-1) \times \cdots \times 2 \times 1$, with $0! = 1$. The factorial $n!$ counts the number of ways to arrange $n$ objects in a line.

## Key Facts / Properties

### The Multiplication Principle (Counting Principle)

If task A can be done in $m$ ways and task B can be done in $n$ ways, then doing A **then** B can be done in $m \times n$ ways.

This extends to any number of tasks: $m \times n \times p \times \cdots$

This is the foundation of all counting. Permutations and combinations are just special applications of this principle.

### Permutations — When Order Matters

**Choosing and arranging $r$ objects from $n$:**

$${}^nP_r = \dfrac{n!}{(n-r)!} = \underbrace{n \times (n-1) \times (n-2) \times \cdots \times (n-r+1)}_{r \text{ factors}}$$

> [!info] Why $\dfrac{n!}{(n-r)!}$?
> Start with all $n!$ arrangements. But we only care about the first $r$ positions — the remaining $(n-r)$ objects can be in any order and we don't care. Dividing by $(n-r)!$ removes those unwanted arrangements.
>
> Equivalently: $n$ choices for first position, $(n-1)$ for second, ..., $(n-r+1)$ for the $r$-th position. Multiply them together: that's $r$ consecutive descending numbers starting from $n$.
>
> **Small example:** Choose and arrange 2 from {A, B, C, D}. The ordered pairs are: AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC — that's 12.
> Formula: ${}^4P_2 = \dfrac{4!}{2!} = \dfrac{24}{2} = 12$. ✓ Or just $4 \times 3 = 12$ (4 choices for first, 3 for second).

**Special case:** ${}^nP_n = n!$ — arranging all $n$ objects uses all of them, so $(n-n)! = 0! = 1$.

### Combinations — When Order Doesn't Matter

**Choosing $r$ objects from $n$ (order irrelevant):**

$${}^nC_r = \binom{n}{r} = \dfrac{n!}{r!(n-r)!}$$

> [!info] Why divide by $r!$?
> Start with the permutation count ${}^nP_r$ — this counts every ordered arrangement. But in a combination, the order among the $r$ chosen objects doesn't matter. Each group of $r$ objects can be arranged in $r!$ ways, and all those arrangements represent the same combination. So divide by $r!$ to remove the overcounting:
>
> $${}^nC_r = \dfrac{{}^nP_r}{r!} = \dfrac{n!}{r!(n-r)!}$$
>
> **Small example:** Choose 2 from {A, B, C, D} (order doesn't matter). The permutations gave us 12 ordered pairs. But {A,B} and {B,A} are the same group — each pair appears $2! = 2$ times. So combinations $= \dfrac{12}{2} = 6$: {A,B}, {A,C}, {A,D}, {B,C}, {B,D}, {C,D}.
> Formula: ${}^4C_2 = \dfrac{4!}{2! \cdot 2!} = \dfrac{24}{4} = 6$. ✓

### Key Properties of ${}^nC_r$

| Property | Formula | Why |
|---|---|---|
| Symmetry | $\binom{n}{r} = \binom{n}{n-r}$ | Choosing $r$ to include = choosing $(n-r)$ to exclude |
| Choose none | $\binom{n}{0} = 1$ | One way to choose nothing |
| Choose all | $\binom{n}{n} = 1$ | One way to choose everything |
| Choose one | $\binom{n}{1} = n$ | $n$ single items to pick |
| Pascal's rule | $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ | Each item is either included or not — see [[Binomial Theorem]] |

### Permutations vs Combinations — The Decision

| Ask yourself... | If yes → | Formula |
|---|---|---|
| Does the order of selection matter? | Permutation | ${}^nP_r$ |
| Is it just about which items are chosen? | Combination | ${}^nC_r$ |

**Quick test:** "Would swapping two selected items create a different outcome?"

- Yes → permutation (passwords, race results, seating arrangements)
- No → combination (committees, teams, card hands)

### Connection to Probability

Combinations are essential for calculating probabilities when outcomes involve choosing from a group:

$$P(\text{event}) = \dfrac{\text{number of favourable outcomes}}{\text{total number of outcomes}} = \dfrac{{}^nC_r \text{ (favourable)}}{{}^nC_r \text{ (total)}}$$

Example: What's the probability of being dealt exactly 2 hearts from 5 cards?

$$P = \dfrac{\binom{13}{2} \cdot \binom{39}{3}}{\binom{52}{5}}$$

Choose 2 hearts from 13, choose 3 non-hearts from 39, divide by total ways to choose 5 from 52. This is why we put permutations and combinations in the Probability cluster — they're the counting tools behind $P(A) = \dfrac{n(A)}{n(S)}$ from [[Probability Basics]].

## Worked Examples

### Example 1: Permutation — race finishers

8 runners in a race. How many ways can they finish 1st, 2nd, and 3rd?

Order matters (1st ≠ 2nd ≠ 3rd), so this is a permutation.

$${}^8P_3 = \dfrac{8!}{(8-3)!} = \dfrac{8!}{5!} = 8 \times 7 \times 6 = 336$$

### Example 2: Combination — committee selection

From 10 students, choose a committee of 4. How many different committees are possible?

Order doesn't matter (a committee is a group, not a ranking), so this is a combination.

$${}^{10}C_4 = \binom{10}{4} = \dfrac{10!}{4! \cdot 6!} = \dfrac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = \dfrac{5040}{24} = 210$$

### Example 3: Why the distinction matters

From the letters A, B, C, D, E:

(a) How many 3-letter **codes** can be formed? (Order matters — ABC ≠ BCA)

$${}^5P_3 = 5 \times 4 \times 3 = 60$$

(b) How many 3-letter **groups** can be chosen? (Order doesn't matter — {A,B,C} = {B,C,A})

$${}^5C_3 = \dfrac{60}{3!} = \dfrac{60}{6} = 10$$

The combination is exactly $\dfrac{1}{3!} = \dfrac{1}{6}$ of the permutation count. Each group of 3 letters has $3! = 6$ arrangements, and the combination count merges all 6 into one.

### Example 4: Probability using combinations

A bag contains 6 red and 4 blue marbles. If 3 are picked at random, what is the probability that exactly 2 are red?

Total ways to pick 3 from 10: $\binom{10}{3} = 120$

Favourable: pick 2 red from 6 **and** 1 blue from 4: $\binom{6}{2} \times \binom{4}{1} = 15 \times 4 = 60$

$$P(\text{exactly 2 red}) = \dfrac{60}{120} = \dfrac{1}{2}$$

## Common Misconceptions (Teaching Notes)

### 1. Using permutations when combinations are needed (and vice versa)

The most common error. Students default to one formula without checking whether order matters.

**Fix:** Always ask: "If I swap two items, does it count as a different outcome?" Make students write "order matters → P" or "order doesn't matter → C" before computing.

### 2. "Combinations are always smaller than permutations"

This is actually true (for $r > 1$), but students sometimes think they're similar in size. In fact, ${}^nP_r = r! \times {}^nC_r$, so permutations grow much faster.

**Fix:** Show the ratio: ${}^{10}P_4 = 5040$ but ${}^{10}C_4 = 210$. The permutation count is $4! = 24$ times larger.

### 3. Forgetting that $0! = 1$

Students write $0! = 0$, which breaks every formula. The most common place this appears: ${}^nC_0 = \dfrac{n!}{0! \cdot n!}$ — if they use $0! = 0$, they get division by zero.

**Fix:** Refer to the three reasons in the Factorial Notation section. Make them memorable.

### 4. Calculator errors with large factorials

$20!$ is already $2.4 \times 10^{18}$. Students try to compute $n!$ directly then divide, hitting overflow. The trick is to cancel before computing.

**Fix:** Teach the "telescoping" method: $\dfrac{10!}{7!} = 10 \times 9 \times 8 = 720$. Cancel the common tail rather than computing full factorials.

### 5. Confusing ${}^nC_r$ notation with $\binom{n}{r}$

These are the same thing — two notations for the same number. Students sometimes think they're different operations.

**Fix:** "${}^nC_r$ and $\binom{n}{r}$ are two ways to write the same thing. Your calculator might use one or the other. The formula is the same."

## Exam Notes

### Cambridge 9709 — Paper 5 (Probability & Statistics 1), §5.2

Two learning objectives, and a 5–8 mark question on almost every Paper 5:

- **Understand the terms permutation and combination, and solve simple problems involving selections** — committees, teams, "how many ways to choose $r$ from $n$", including "at least / at most" splits.
- **Solve problems about arrangements of objects in a line**, including **repetition** — the syllabus's own example is *the number of ways of arranging the letters of the word NEEDLESS* ($\tfrac{8!}{3!\,2!}$) — and **restriction** — *several people standing in a line if two particular people must, or must not, stand next to each other* (glue them into one block; complement for "must not"). The notes warn that *"questions may include cases such as people sitting in two (or more) rows"*, and promise that *"questions about objects arranged in a circle will not be included"*.
- Show the product or the ${}^nC_r$ / ${}^nP_r$ expression, not just the answer — the M1 is for the method; and when a question says "at least", list the cases or use the complement explicitly.

### Cambridge 0606

- 11.1: recognize the difference between a permutation and a combination and know when each applies
- 11.2: know and use factorial notation $n!$; know ${}^nP_r$ and ${}^nC_r$ formulas; know that $0! = 1$
- 11.3: solve problems on arrangement and selection — see [[Counting Problems]]
- "No circular permutations" — arrangements in a circle are not in scope
- "No repetition" — all objects are distinct
- Both Paper 1 and Paper 2
- Typical questions: "How many ways can ... be arranged/chosen?", "How many committees...", sometimes linked to probability

### AP / IB

- **AP Statistics:** combinations appear inside binomial probability $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$; counting is not examined on its own.
- **IB Mathematics AA HL** (Topic 1, counting principles): permutations and combinations *including* circular arrangements and cases with repetition — the two things Cambridge excludes. **AA SL** and **AI** do not examine counting principles.

### Where it is *not* examined

**Cambridge 0580** and **OxAQA 9260** do not test permutations or combinations directly — students list outcomes or count systematically. **Cambridge 9231** adds nothing beyond 9709 (no multinomial coefficients, derangements or inclusion–exclusion on that syllabus). **Edexcel IAL** has no permutations-and-combinations topic in any of its Statistics units — its formula book lists $n!$ and $\binom{n}{r}$ only for the binomial distribution — and **OxAQA 9660** likewise. Where these appear elsewhere in the world, they are almost always in the probability unit, so a student meeting them there should read this card first and [[Counting Problems]] second.

### Beyond high school — University

- Combinatorics becomes its own field of mathematics, connecting to graph theory, coding theory, and discrete mathematics
- Generating functions provide algebraic machinery for solving counting problems
- Pólya enumeration handles symmetry (e.g., "how many distinct necklaces can you make with 5 beads?")

## Connections

- **Foundation:** [[Probability Basics]] — $P(A) = \dfrac{n(A)}{n(S)}$ requires counting, which is what permutations and combinations do
- **Application:** [[Counting Problems]] — worked problems using these tools (0606 11.3)
- **Key link:** [[Binomial Theorem]] — $\binom{n}{r}$ appears as the coefficient in $(a+b)^n$; Pascal's rule builds Pascal's triangle / 杨辉三角
- **Application:** [[Combined Probability]] — counting outcomes for complex events
- **Set theory:** [[Cardinality]] — $n(A)$ is the bridge between counting and probability
- **For 9709 students:** [[MF19 Reference (9709)]] — which formulas on this card are on the MF19 exam sheet vs need memorising. (Other boards have their own sheets.)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $n!$ | `n!` | Factorial |
| ${}^nP_r$ | `{}^nP_r` | Permutation (Cambridge style) |
| ${}^nC_r$ | `{}^nC_r` | Combination (Cambridge style) |
| $\binom{n}{r}$ | `\binom{n}{r}` | Combination (binomial coefficient style) |
| $\dfrac{n!}{r!(n-r)!}$ | `\dfrac{n!}{r!(n-r)!}` | Combination formula expanded |
