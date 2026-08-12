---
chinese: 组合概率 (zǔhé gàilǜ)
prerequisites:
  - "[[Probability Basics]]"
  - "[[Set Operations]]"
  - "[[Venn Diagram]]"
  - "[[Permutations and Combinations]]"
leads_to:
  - "[[Conditional Probability]]"
  - "[[Discrete Random Variables]]"
  - "[[Information Theory]]"
tags:
  - subject/mathematics
  - domain/probability
  - level/GCSE
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-S14
  - syllabus/9260-S15
  - syllabus/9260-S16
  - syllabus/9260-S17
  - syllabus/0580-E8-3
  - syllabus/9709-5-3
  - type/concept
  - notation/P-notation
  - notation/set-notation
  - misconception/addition-vs-multiplication
  - misconception/independent-vs-mutually-exclusive
---

# Combined Probability

## Definition

### Formal

For any two events $A$ and $B$ in a sample space $S$:

**Addition rule (OR):**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Multiplication rule for independent events (AND):**

$$P(A \cap B) = P(A) \times P(B) \quad \text{(only if } A \text{ and } B \text{ are independent)}$$

### Intuitive

Combined probability answers two types of question:

- **"OR" questions** — "What is the probability of $A$ **or** $B$ (or both)?" → **add**, but subtract the overlap.
- **"AND" questions** — "What is the probability of $A$ **and** $B$ both happening?" → **multiply**. For independent events, multiply the original probabilities. For dependent events (e.g., without replacement), multiply along branches of a tree diagram — the second probability adjusts. See [[Conditional Probability]] for the formal version.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| combined probability | 组合概率 | zǔhé gàilǜ |
| addition rule | 加法法则 | jiāfǎ fǎzé |
| multiplication rule | 乘法法则 | chéngfǎ fǎzé |
| independent events | 独立事件 | dúlì shìjiàn |
| dependent events | 相关事件 | xiāngguān shìjiàn |
| with replacement | 有放回 | yǒu fànghuí |
| without replacement | 无放回 | wú fànghuí |
| tree diagram | 树形图 | shùxíngtú |
| sample space diagram | 样本空间图 | yàngběn kōngjiān tú |

---

## Notation

| Symbol | Meaning | Set theory parallel |
|--------|---------|-------------------|
| $P(A \cup B)$ | Probability of $A$ **or** $B$ (or both) | [[Union]] |
| $P(A \cap B)$ | Probability of $A$ **and** $B$ (both happen) | [[Intersection]] |
| $P(A')$ | Probability of **not** $A$ | [[Complement]] |
| $P(A \mid B)$ | Probability of $A$ **given** $B$ has happened | See [[Conditional Probability]] |

---

## Key Facts / Properties

### The General Addition Rule

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

> [!info] Why subtract $P(A \cap B)$?
> Think about it with a [[Venn Diagram|Venn diagram]]. When you add $P(A) + P(B)$, the overlapping region — the outcomes where **both** $A$ and $B$ happen — gets counted **twice**: once inside $P(A)$ and once inside $P(B)$.
>
> Subtracting $P(A \cap B)$ removes the double-count, so every outcome is counted exactly once.
>
> In set theory terms: $n(A \cup B) = n(A) + n(B) - n(A \cap B)$. This is exactly the same formula you used in [[Set Operations]] — probability inherits it because events are sets.

**Special case — mutually exclusive events:** If $A \cap B = \emptyset$ (the events can't both happen), then $P(A \cap B) = 0$, and the formula simplifies to:

$$P(A \cup B) = P(A) + P(B)$$

This is the simplified version from [[Probability Basics]].

### Independent Events

Two events are **independent** if one happening does not change the probability of the other:

$$A \text{ and } B \text{ are independent} \quad \Longleftrightarrow \quad P(A \cap B) = P(A) \times P(B)$$

> [!info] Why multiply for independent events?
> Imagine rolling a die and flipping a coin. The coin doesn't know what the die did — neither result affects the other.
>
> The die has 6 outcomes. For **each** die outcome, the coin has 2 outcomes. So there are $6 \times 2 = 12$ equally likely outcomes in total.
>
> If $A$ = "die shows 6" (1 out of 6) and $B$ = "coin shows heads" (1 out of 2), then the outcome "6 and heads" is 1 out of $6 \times 2 = 12$:
>
> $$P(A \cap B) = \dfrac{1}{12} = \dfrac{1}{6} \times \dfrac{1}{2} = P(A) \times P(B)$$
>
> Multiplication counts the proportion of total outcomes that satisfy both conditions — it works because the two experiments don't interfere with each other.

**The key test for independence:** If knowing that $B$ happened doesn't change your calculation of $P(A)$, they are independent. In formal notation: $P(A \mid B) = P(A)$ — see [[Conditional Probability]].

**Where does this formula come from?** The general multiplication rule for *any* two events is:

$$P(A \cap B) = P(A) \times P(B \mid A)$$

where $P(B \mid A)$ is the [[Conditional Probability|conditional probability]] of $B$ given $A$. When $A$ and $B$ are independent, $P(B \mid A) = P(B)$ (knowing $A$ doesn't help), so the formula simplifies to $P(A) \times P(B)$. The "multiply for independent events" rule is a special case — the general version uses conditional probability and works for **all** events, dependent or not. This is exactly what tree diagrams do: the second branch is always $P(\text{second} \mid \text{first})$.

### With Replacement vs Without Replacement

| Scenario | Independent? | Why |
|----------|-------------|-----|
| **With replacement** — put the item back before the next pick | Yes | The sample space resets to its original state. The second pick doesn't "know" about the first. |
| **Without replacement** — keep the item out | No | The sample space changes. There are fewer items left, so probabilities shift. |

Example: A bag has 3 red and 2 blue marbles.

**With replacement:** $P(\text{red, then red}) = \dfrac{3}{5} \times \dfrac{3}{5} = \dfrac{9}{25}$

**Without replacement:** $P(\text{red, then red}) = \dfrac{3}{5} \times \dfrac{2}{4} = \dfrac{6}{20} = \dfrac{3}{10}$

The second fraction changes because the sample space shrank: after removing one red marble, there are 2 red out of 4 total.

### Sample Space Diagrams

A **sample space diagram** lists every possible outcome systematically. For two combined events, use a grid:

**Example:** Roll a die and spin a spinner {1, 2, 3}. Add the results.

|  | **Spinner 1** | **Spinner 2** | **Spinner 3** |
|---|---|---|---|
| **Die 1** | 2 | 3 | 4 |
| **Die 2** | 3 | 4 | 5 |
| **Die 3** | 4 | 5 | 6 |
| **Die 4** | 5 | 6 | 7 |
| **Die 5** | 6 | 7 | 8 |
| **Die 6** | 7 | 8 | 9 |

Total outcomes: $6 \times 3 = 18$. To find $P(\text{sum} = 6)$, count the 6s in the grid: three cells show 6, so $P(\text{sum} = 6) = \dfrac{3}{18} = \dfrac{1}{6}$.

### Tree Diagrams

A **tree diagram** shows probabilities branching at each stage.

**Rules for reading tree diagrams:**

1. **Multiply along branches** (AND) — to get the probability of a specific path
2. **Add across paths** (OR) — to get the probability of an event that can happen in multiple ways
3. Branches at each node must add to 1 (something must happen at each stage)

**Example:** Bag with 3 red, 2 blue. Pick two marbles **without replacement**.

```
First pick          Second pick         Outcome         Probability
                 ┌── 2/4 Red ────── RR ────── 3/5 × 2/4 = 6/20
          ┌─ 3/5 Red
          │      └── 2/4 Blue ───── RB ────── 3/5 × 2/4 = 6/20
Start ────┤
          │      ┌── 3/4 Red ────── BR ────── 2/5 × 3/4 = 6/20
          └─ 2/5 Blue
                 └── 1/4 Blue ───── BB ────── 2/5 × 1/4 = 2/20
```

Check: $\dfrac{6}{20} + \dfrac{6}{20} + \dfrac{6}{20} + \dfrac{2}{20} = \dfrac{20}{20} = 1$ ✓

$P(\text{one of each colour}) = P(RB) + P(BR) = \dfrac{6}{20} + \dfrac{6}{20} = \dfrac{12}{20} = \dfrac{3}{5}$

> [!tip] "At least one" problems — use the complement
> For questions like "at least one red marble," it's often easier to calculate $1 - P(\text{no red at all})$:
>
> $$P(\text{at least one red}) = 1 - P(BB) = 1 - \dfrac{2}{20} = \dfrac{18}{20} = \dfrac{9}{10}$$
>
> This connects directly to the complement rule from [[Probability Basics]]. The same strategy appears in [[Counting Problems#Strategy: How to Approach a Counting Problem|counting problems]] (Step 0: "count what you don't want") — it is one of the most versatile moves in all of mathematics.

### Venn Diagrams for Probability

A [[Venn Diagram|Venn diagram]] can show probabilities instead of set sizes. The regions must add to 1 (since they partition the sample space).

**Strategy for filling a probability Venn diagram:**

1. Start with the **intersection** $P(A \cap B)$ — write this in the overlap region
2. Subtract to find $P(A \text{ only}) = P(A) - P(A \cap B)$
3. Subtract to find $P(B \text{ only}) = P(B) - P(A \cap B)$
4. The **outside region** $= 1 - P(A \cup B) = 1 - [P(A \text{ only}) + P(B \text{ only}) + P(A \cap B)]$
5. **Check:** all four regions add to 1

This is exactly the same four-region structure from the [[Venn Diagram]] card in the Set Theory cluster, but with probabilities instead of counts.

---

## Worked Examples

### Example 1: General addition rule

In a class of 30 students, 18 study French, 12 study Spanish, and 5 study both.

A student is picked at random. Find $P(\text{French or Spanish})$.

$$P(F \cup S) = P(F) + P(S) - P(F \cap S) = \dfrac{18}{30} + \dfrac{12}{30} - \dfrac{5}{30} = \dfrac{25}{30} = \dfrac{5}{6}$$

**Check:** The 5 students studying both would be double-counted without the subtraction. The Venn diagram has regions: 13 (French only) + 5 (both) + 7 (Spanish only) + 5 (neither) = 30. ✓

### Example 2: Tree diagram — without replacement

A box contains 4 red and 6 blue counters. Two counters are taken at random without replacement. Find the probability that both are the same colour.

**Tree diagram approach:**

$$P(RR) = \dfrac{4}{10} \times \dfrac{3}{9} = \dfrac{12}{90}$$

$$P(BB) = \dfrac{6}{10} \times \dfrac{5}{9} = \dfrac{30}{90}$$

$$P(\text{same colour}) = P(RR) + P(BB) = \dfrac{12}{90} + \dfrac{30}{90} = \dfrac{42}{90} = \dfrac{7}{15}$$

Note: the second fractions change because one counter was removed (without replacement → dependent events).

### Example 3: Sample space diagram

Two fair dice are rolled. Find $P(\text{total} > 10)$.

The sample space has $6 \times 6 = 36$ equally likely outcomes. The totals greater than 10 are:

| Total | Combinations | Count |
|-------|-------------|-------|
| 11 | (5,6), (6,5) | 2 |
| 12 | (6,6) | 1 |

$$P(\text{total} > 10) = \dfrac{3}{36} = \dfrac{1}{12}$$

### Example 4: Venn diagram with probabilities

$P(A) = 0.6$, $P(B) = 0.5$, $P(A \cap B) = 0.2$. Fill in a Venn diagram and find $P(\text{neither } A \text{ nor } B)$.

| Region | Calculation | Probability |
|--------|-----------|-------------|
| $A$ only | $0.6 - 0.2$ | $0.4$ |
| $A \cap B$ | given | $0.2$ |
| $B$ only | $0.5 - 0.2$ | $0.3$ |
| Outside | $1 - (0.4 + 0.2 + 0.3)$ | $0.1$ |

$$P(\text{neither}) = P(A' \cap B') = P((A \cup B)') = 1 - P(A \cup B) = 1 - 0.9 = 0.1$$

Notice: $P(\text{neither})$ uses De Morgan's law — "not $A$ and not $B$" is the same as "not ($A$ or $B$)". See [[Complement]].

---

## Common Misconceptions

### 1. Adding probabilities when you should multiply

"Roll a die twice. $P(\text{6 both times}) = \dfrac{1}{6} + \dfrac{1}{6} = \dfrac{2}{6}$" ✗

**Fix:** "OR" means add. "AND" means multiply. The question says "6 **and** 6" — both must happen:

$$P(\text{6 both times}) = \dfrac{1}{6} \times \dfrac{1}{6} = \dfrac{1}{36}$$

### 2. Confusing independent with mutually exclusive

These are **opposite** ideas, not synonyms:

| Concept | Meaning | $P(A \cap B)$ |
|---------|---------|---------------|
| **Independent** | One happening doesn't affect the other | $= P(A) \times P(B)$ (usually $> 0$) |
| **Mutually exclusive** | Both **cannot** happen together | $= 0$ |

If $A$ and $B$ are mutually exclusive and both have non-zero probability, they **cannot** be independent. Knowing that $A$ happened tells you $B$ definitely didn't happen — that's the opposite of "no effect."

### 3. Forgetting to adjust fractions for without replacement

"Bag with 4 red, 6 blue. $P(\text{two red}) = \dfrac{4}{10} \times \dfrac{4}{10}$" ✗

**Fix:** Without replacement means the bag changed after the first pick:

$$P(\text{two red}) = \dfrac{4}{10} \times \dfrac{3}{9} = \dfrac{12}{90} = \dfrac{2}{15}$$

Not $\dfrac{4}{10}$ again — one red marble is already out.

### 4. Not subtracting the overlap in the addition rule

"18 study French, 12 study Spanish. $P(F \text{ or } S) = \dfrac{18}{30} + \dfrac{12}{30} = 1$" ✗

**Fix:** If some students study both, adding counts them twice. Always check: do any outcomes belong to **both** events? If so, subtract the overlap:

$$P(F \cup S) = P(F) + P(S) - P(F \cap S)$$

### 5. Assuming events are independent without checking

Students default to multiplying probabilities for any "AND" question. But $P(A \cap B) = P(A) \times P(B)$ **only works for independent events**.

**Fix:** Ask: "Does the first event change the conditions for the second?" If yes (e.g., without replacement, or selecting from a changed pool), the events are **dependent**, and you need conditional probability — see [[Conditional Probability]].

---

## Exam Notes

### OxAQA 9260

- S14: sample space diagrams for single events and two successive events — list outcomes systematically
- S15: mutually exclusive events; $P(A \cup B) = P(A) + P(B)$ when $A \cap B = \emptyset$; exhaustive outcomes sum to 1
- S16: use Venn diagrams to calculate probabilities — treat the diagram as having probabilities instead of counts
- S17 (Extension): independent combined events, tree diagrams, $P(A \cap B) = P(A) \times P(B)$
- Tree diagrams and Venn diagrams are heavily tested — expect 4–6 mark questions combining both
- "Without replacement" problems are common and test whether students correctly adjust fractions

### Cambridge 0580

- E8.3: combined events, sample space diagrams, tree diagrams (with and without replacement), Venn diagrams
- Scope is very similar to 9260 — all the same tools are required
- Expect two-stage experiments (e.g., two picks from a bag, two spins)
- Both Paper 2 and Paper 4

### AP / IB / A-Level

- **AP Statistics:** addition rule, multiplication rule, independence test $P(A \cap B) = P(A) \times P(B)$; mutually exclusive test $P(A \cap B) = 0$
- **IB Mathematics AA HL:** formal notation with conditional probability; Bayes' theorem extends tree diagrams
- **A-Level Statistics:** S1/S2 covers combined events with Venn diagrams and tree diagrams; conditional probability formula $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$ is core content

---

## Connections

- **Foundation:** [[Probability Basics]] — vocabulary, complement rule, mutually exclusive definition
- **Set theory:** [[Set Operations]] — the addition rule *is* the inclusion-exclusion principle from set theory
- **Diagrams:** [[Venn Diagram]] — same four-region structure, now holding probabilities instead of counts
- **Extends to:** [[Conditional Probability]] — handles dependent events formally with $P(A \mid B)$
- **Counting:** [[Permutations and Combinations]] — counting outcomes for the numerator and denominator of $P(A)$
- **Relates to:** [[Relative and Expected Frequency]] — experimental approach to estimating combined probabilities
- **For 9709 students:** [[MF19 Reference (9709)]] — which formulas on this card are on the MF19 exam sheet vs need memorising. (Other boards have their own sheets.)

> [!info] Beyond syllabus — The birthday problem
> How many people do you need in a room before there's a 50% chance two share a birthday? Most people guess around 183 (half of 365). The actual answer: just **23 people**.
>
> This is solved using the complement and multiplication rule for independent events:
>
> $$P(\text{no shared birthday among } n \text{ people}) = \dfrac{365}{365} \times \dfrac{364}{365} \times \dfrac{363}{365} \times \cdots \times \dfrac{365 - n + 1}{365}$$
>
> At $n = 23$, this product drops below 0.5, so $P(\text{at least one match}) > 0.5$.
>
> The surprise comes from the number of **pairs** — 23 people form $\binom{23}{2} = 253$ pairs, and each pair is a chance for a match. This is a famous example of how combined probability can be deeply unintuitive.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $P(A \cup B)$ | `P(A \cup B)` | Probability of $A$ or $B$ |
| $P(A \cap B)$ | `P(A \cap B)` | Probability of $A$ and $B$ |
| $P(A')$ | `P(A')` | Probability of not $A$ |
| $P(A \mid B)$ | `P(A \mid B)` | Probability of $A$ given $B$ |
| $\dfrac{3}{5} \times \dfrac{2}{4}$ | `\dfrac{3}{5} \times \dfrac{2}{4}` | Tree diagram branch multiplication |
