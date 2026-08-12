---
chinese: 计数问题 (jìshù wèntí)
prerequisites:
  - "[[Permutations and Combinations]]"
  - "[[Factorial Notation]]"
leads_to:
  - "[[Binomial Theorem]]"
tags:
  - subject/mathematics
  - domain/combinatorics
  - domain/probability
  - level/pre-IB
  - level/pre-AP
  - curriculum/Cambridge-0606
  - syllabus/0606-11-3
  - type/strategy
  - misconception/overcounting
---

# Counting Problems

## Definition

### Formal

A **counting problem** asks: "In how many ways can something be arranged or selected, given certain constraints?"

The answer always uses one or both of:

- **Permutations** (${}^nP_r$) — when order matters
- **Combinations** (${}^nC_r$) — when order doesn't matter

along with the **multiplication principle** (if task A has $m$ ways and task B has $n$ ways, and they are independent, then doing both has $m \times n$ ways) and the **addition principle** (if the task can be done in mutually exclusive cases, add the counts).

See [[Permutations and Combinations]] for the formulas and [[Factorial Notation]] for the machinery.

### Intuitive

Counting problems are puzzles. The challenge isn't the arithmetic — it's figuring out **how to break the problem into pieces** and which tool fits each piece.

The two big questions every time:

1. **Does order matter?** → permutation or combination?
2. **Are there constraints?** → handle the constraint first, then count the rest.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| counting problem | 计数问题 | jìshù wèntí |
| arrangement | 排列 | páiliè |
| selection / combination | 选择 / 组合 | xuǎnzé / zǔhé |
| constraint / restriction | 约束条件 | yuēshù tiáojiàn |
| multiplication principle | 乘法原理 | chéngfǎ yuánlǐ |
| addition principle | 加法原理 | jiāfǎ yuánlǐ |
| case analysis | 分类讨论 | fēnlèi tǎolùn |
| reduction | 化简 / 约化 | huàjiǎn / yuēhuà |
| decomposition | 分解 | fēnjiě |
| complement | 补集 / 余事件 | bǔjí / yú shìjiàn |

---

## Key Facts / Properties

### Strategy: How to Approach a Counting Problem

Every counting problem follows the same thinking process. The core skill is **reduction** — taking a complex problem and systematically breaking it into simpler, independent pieces. Each step below is a different way to reduce the problem until what remains is straightforward arithmetic.

**Step 0 — Consider the complement.** Before diving in, ask: *"Would it be easier to count what I DON'T want?"* If the condition says "at least," "not," or "except," the complement $(\text{Total} - \text{unwanted})$ is often far simpler. This is not a trick — it is one of the most powerful strategies in all of combinatorics and probability. See [[Combined Probability]] and [[Probability Basics]].

**Step 1 — Identify what you're counting.** Arrangements (order matters) or selections (order doesn't)?

**Step 2 — Spot the constraints.** Are certain items fixed in position? Must some items be together? Must some items be apart? Is there a condition on who can go where?

**Step 3 — Handle the constraint first.** Place the restricted items before counting the rest. This is the most important principle in counting problems. You are performing **decomposition** — isolating the hardest part, solving it, and then dealing with the rest independently.

**Step 4 — Multiply independent choices.** If choices don't affect each other, use the multiplication principle. This works precisely *because* the earlier steps decomposed the problem into independent stages.

**Step 5 — Add mutually exclusive cases.** If the problem splits into separate cases that don't overlap, add the counts.

**Step 6 — Check with a small example.** If the numbers are small enough, list the outcomes and verify your formula matches.

### The Multiplication Principle

If a task can be split into stages, and the number of choices at each stage doesn't depend on the previous choices:

$$\text{Total ways} = (\text{ways for stage 1}) \times (\text{ways for stage 2}) \times \cdots$$

**Example:** A password has 3 digits (0–9) followed by 2 letters (A–Z).

$$\text{Passwords} = 10 \times 10 \times 10 \times 26 \times 26 = 676{,}000$$

Each position is independent — the choice of first digit doesn't restrict the second digit.

### The Addition Principle

If a task can happen in **mutually exclusive** cases (Case A or Case B, never both):

$$\text{Total ways} = (\text{ways for Case A}) + (\text{ways for Case B})$$

**Example:** From 5 men and 4 women, choose a committee of 3 that is either all men or all women.

$$\text{All men: } \binom{5}{3} = 10 \qquad \text{All women: } \binom{4}{3} = 4$$

$$\text{Total} = 10 + 4 = 14$$

These cases don't overlap (a committee can't be both all men and all women), so we add.

### Constraint First — The Golden Rule

> [!warning] Always handle the constraint first
> The most common mistake in counting problems is counting freely first and then trying to "remove" the invalid cases. Before getting into the constraint, remember **Step 0** — check whether the complement approach would make the whole problem trivial. If not, **place the restricted items first**, then count the remaining items.

### Common Problem Types

#### Type 1: Items that must be together

**Treat them as a single block**, then arrange the blocks. Then arrange the items within the block. This is **reduction** — you reduce $n$ items to $(n-k+1)$ items by gluing $k$ together.

![[counting-block-method.svg|700]]

**Example:** 6 people sit in a row. Two specific friends must sit next to each other.

1. Treat the two friends as one block → 5 "items" to arrange: $5! = 120$
2. The two friends can swap within the block: $2! = 2$
3. Total: $5! \times 2! = 120 \times 2 = 240$

#### Type 2: Items that must NOT be together

**Method — count all, subtract the "together" cases:**

$$\text{Not together} = \text{Total} - \text{Together}$$

**Example:** Same 6 people, but the two friends must NOT sit next to each other.

1. Total arrangements: $6! = 720$
2. Together (from Type 1): $240$
3. Not together: $720 - 240 = 480$

**Alternative — gap method:** Arrange the other items first, creating gaps, then place the restricted items in the gaps. This is often cleaner for "must not be adjacent" problems.

![[counting-gap-method.svg|700]]

1. Arrange the other 4 people: $4! = 24$
2. This creates 5 gaps (including the ends): _ P _ P _ P _ P _
3. Choose 2 of these 5 gaps for the friends: ${}^5P_2 = 20$ (order matters — the friends are distinct)
4. Total: $4! \times {}^5P_2 = 24 \times 20 = 480$ ✓

#### Type 3: Fixed positions

**Place the fixed item first**, then count the remaining arrangements. The constraint **reduces** one position to exactly 1 choice, leaving the rest free.

![[counting-fixed-position.svg|700]]

**Example:** 5 people sit in a row. The oldest must sit in the middle seat.

1. Fix the oldest in the middle: 1 way
2. Arrange the remaining 4 in the other seats: $4! = 24$
3. Total: $1 \times 24 = 24$

#### Type 4: Choosing with conditions

**Split into cases** based on the condition.

**Example:** From 6 boys and 4 girls, choose a team of 5 with at least 2 girls.

The cases are:

| Girls | Boys | Ways |
|-------|------|------|
| 2 | 3 | $\binom{4}{2} \times \binom{6}{3} = 6 \times 20 = 120$ |
| 3 | 2 | $\binom{4}{3} \times \binom{6}{2} = 4 \times 15 = 60$ |
| 4 | 1 | $\binom{4}{4} \times \binom{6}{1} = 1 \times 6 = 6$ |

$$\text{Total} = 120 + 60 + 6 = 186$$

**Check:** The complement (0 or 1 girl) gives $\binom{4}{0}\binom{6}{5} + \binom{4}{1}\binom{6}{4} = 6 + 60 = 66$. Total teams $= \binom{10}{5} = 252$. So "at least 2 girls" $= 252 - 66 = 186$. ✓

> [!tip] "At least" → consider the complement (Step 0!)
> "At least 2" means "not 0 and not 1." Sometimes it's faster to calculate $\text{Total} - \text{fewer than 2}$ instead of listing all valid cases. This mirrors the complement strategy from [[Probability Basics]] and [[Combined Probability]].

![[counting-complement.svg|700]]

#### Type 5: Digits and number formation

![[counting-digit-constraint.svg|700]]

**Example:** How many 4-digit numbers greater than 5000 can be formed from {1, 3, 5, 7, 9} without repetition?

1. **Constraint first** — the first digit must be 5, 7, or 9 (to be ≥ 5000): **3 choices**
2. Remaining 3 digits chosen from the remaining 4 digits, order matters: ${}^4P_3 = 24$
3. Total: $3 \times 24 = 72$

---

## Worked Examples

### Example 1: Letters of a word

How many arrangements of the letters in MATHS are there?

5 distinct letters, arrange all of them: $5! = 120$

How many start with M?

Fix M in the first position. Arrange the remaining 4 letters: $4! = 24$

How many have the vowel A in the middle?

Fix A in position 3. Arrange the remaining 4 letters in the other 4 positions: $4! = 24$

### Example 2: Seating with a block constraint

7 students sit in a row. Three specific students (A, B, C) must sit together. How many arrangements?

1. Treat {A, B, C} as one block → 5 items to arrange: $5! = 120$
2. A, B, C can arrange within their block: $3! = 6$
3. Total: $120 \times 6 = 720$

### Example 3: Committee with exclusion

From 8 people, choose a committee of 4. Two specific people (X and Y) cannot both be on the committee. How many valid committees?

**Method — total minus both included:**

1. Total committees: $\binom{8}{4} = 70$
2. Committees with both X and Y: choose the remaining 2 from the other 6: $\binom{6}{2} = 15$
3. Valid: $70 - 15 = 55$

### Example 4: Digit problem

Using digits {0, 1, 2, 3, 4, 5} without repetition, how many 3-digit even numbers can be formed?

**Constraint analysis:** The number must be 3 digits (first digit ≠ 0) and even (last digit is 0, 2, or 4).

**Case 1: Last digit = 0**
- First digit: 5 choices (1, 2, 3, 4, 5)
- Middle digit: 4 choices (remaining digits)
- Total: $5 \times 4 = 20$

**Case 2: Last digit = 2 or 4**
- Last digit: 2 choices (2 or 4)
- First digit: 4 choices (can't be 0, can't be the last digit)
- Middle digit: 4 choices (remaining)
- Total: $2 \times 4 \times 4 = 32$

**Total even 3-digit numbers:** $20 + 32 = 52$

**Check (for Case 2):** If last digit = 2, first digit choices are {1, 3, 4, 5} (4 choices), middle from remaining 4 digits. So $4 \times 4 = 16$. Similarly for last digit = 4: $4 \times 4 = 16$. Total Case 2: $16 + 16 = 32$. ✓

---

## Common Misconceptions

### 1. Not handling the zero in digit problems

"4-digit numbers from {0, 1, 2, 3}: first digit has 4 choices." ✗

**Fix:** A 4-digit number can't start with 0 (that would make it a 3-digit number). The first digit has only 3 choices: {1, 2, 3}. Always check whether 0 is in the digit set and handle it as a constraint on the leading position.

### 2. Forgetting internal arrangements of a block

"3 people must sit together in a row of 7. There are $5!$ arrangements." ✗

**Fix:** $5!$ counts the arrangements of the 5 "items" (4 individuals + 1 block). But the 3 people inside the block can also rearrange among themselves: $3! = 6$ ways. Total: $5! \times 3! = 720$.

### 3. Using permutations when combinations are needed (or vice versa)

"Choose 3 from 8 for a committee: ${}^8P_3 = 336$." ✗

**Fix:** A committee is a group — the order of selection doesn't matter. Use ${}^8C_3 = 56$. The permutation answer overcounts by $3! = 6$, because it treats {A, B, C} and {B, A, C} as different.

**Quick check:** If your answer seems surprisingly large, ask: "Am I counting the same group multiple times because of ordering?"

### 4. Double-counting in case analysis

When splitting into cases, the cases must be **mutually exclusive** — no overlap. If they overlap, you're counting some outcomes twice.

**Fix:** Before adding cases, check: "Is there any outcome that belongs to more than one case?" If yes, restructure your cases.

### 5. Overcounting with the complement method

"Arrangements where A and B are NOT next to each other = Total − (arrangements where A is next to B on the left)." ✗

**Fix:** "A and B together" means A-B **or** B-A. If you only subtract one ordering, you've missed half the "together" cases. Always remember the internal arrangements when using the complement.

---

## Exam Notes

### Cambridge 0606

- 11.3: solve problems on arrangement and selection
- **No repetition** — the spec says "where repetition is not allowed"
- **No circular permutations** — all arrangements are in a line (or choosing from a group)
- Expect: word arrangement problems, seating problems, committee selection with conditions, digit formation
- Common question structure: "How many ways..." followed by a constraint ("if the two oldest must sit together", "if the number must be even")
- Both Paper 1 and Paper 2; typically 4–6 marks

### Not in 0580 or 9260

Counting problems of this type are not in the Cambridge 0580 or OxAQA 9260 specification. However, the multiplication principle underlies sample space counting in [[Combined Probability]], which is tested in both.

### AP / IB / A-Level

- **AP Statistics:** counting rules (multiplication, permutations, combinations) for computing probabilities
- **IB Mathematics AA HL:** combinatorics problems with constraints; links to binomial theorem and probability distributions
- **A-Level Further Mathematics:** more complex counting including circular arrangements, items with repetition, and the inclusion-exclusion principle

### Beyond high school — University

- Circular permutations: $(n-1)!$ instead of $n!$ — fixing one position to remove rotational symmetry
- Arrangements with repetition: $\dfrac{n!}{n_1! \cdot n_2! \cdot \ldots}$ for words with repeated letters (e.g., MISSISSIPPI)
- The inclusion-exclusion principle generalises the complement method to multiple overlapping constraints
- Generating functions provide a systematic algebraic approach to counting problems — see [[Permutations and Combinations#Beyond high school — University]]

---

## Connections

- **Foundation:** [[Permutations and Combinations]] — the formulas (${}^nP_r$, ${}^nC_r$) and the decision framework (order matters or not)
- **Foundation:** [[Factorial Notation]] — the arithmetic behind the formulas
- **Application:** [[Combined Probability]] — counting outcomes is the numerator and denominator of $P(A) = \dfrac{n(A)}{n(S)}$
- **Application:** [[Relative and Expected Frequency]] — expected frequency uses theoretical probability, which often requires counting
- **Extends to:** [[Binomial Theorem]] — $\binom{n}{r}$ appears as the coefficient in $(a+b)^n$
- **Thinking skill:** [[Logic]] — the discipline of processing information exactly as given, without adding assumptions
- **For 9709 students:** [[MF19 Reference (9709)]] — which formulas on this card are on the MF19 exam sheet vs need memorising. (Other boards have their own sheets.)

> [!info] Beyond syllabus — Counting is harder than it looks
> Counting problems look simple — after all, you're "just counting." But professional mathematicians consider combinatorics one of the most creative areas of mathematics. There's rarely a single formula that solves every problem; instead, you need to find the right way to decompose the problem, choose the right tool, and verify your answer. This is why counting problems are a favourite in mathematics competitions — they test ingenuity, not memorisation.
>
> The same skills transfer directly to computer science, where counting algorithms, data structures, and optimisation problems all require careful combinatorial reasoning.

> [!info] Beyond syllabus — Counting trains reading comprehension
> A less obvious benefit of counting problems is that they train the same skill demanded by difficult reading tests (IELTS, SAT, GRE): **processing information exactly as given** — no more, no less. A counting question gives you a set of constraints and asks you to work with *only* those constraints. Add an assumption that isn't there, and you get the wrong answer. Ignore a constraint that is there, and you also get the wrong answer. This is precisely what reading comprehension at a high level requires — extracting what the text actually says, without hallucinating extra information or missing what's stated. The discipline is the same: read carefully, identify exactly what is and isn't given, and reason from there. See [[Logic]].

> [!info] Beyond syllabus — Defining what is not (鬼谷子)
> The complement method — "count what you don't want, subtract" — has a philosophical parallel in the Chinese classic 鬼谷子 (Guǐgǔzi, ~4th century BC). 鬼谷子 is a treatise on persuasion, strategy, and (frankly) manipulation — it catalogues the ways people control, deceive, and exploit one another. Terrible ways to treat human beings, listed one by one. But here is the deep move: if 鬼谷子 believes he has listed *all* of them — every form of manipulation, every way to use people as instruments — then what is left over? What remains, by complement, is what love could be.
>
> This is exactly the mathematical strategy: when something is too vast or subtle to define directly, define everything it is *not*, and what survives is the answer. In set theory: $A' = \xi \setminus A$. In probability: $P(A) = 1 - P(A')$. In logic: proof by contradiction. In reading comprehension: eliminating wrong answers. In philosophy: defining love by exhausting what love is not. The complement is not a trick — it is one of the deepest problem-solving moves there is, and it connects mathematics to questions far beyond the exam.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| ${}^nP_r$ | `{}^nP_r` | Permutation |
| ${}^nC_r$ or $\binom{n}{r}$ | `{}^nC_r` or `\binom{n}{r}` | Combination |
| $n!$ | `n!` | Factorial |
| $\dfrac{n!}{r!(n-r)!}$ | `\dfrac{n!}{r!(n-r)!}` | Combination formula expanded |
