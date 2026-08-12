---
chinese: 概率基础 (gàilǜ jīchǔ)
prerequisites:
  - "[[Set]]"
  - "[[Venn Diagram]]"
  - "[[Set Operations]]"
leads_to:
  - "[[Relative and Expected Frequency]]"
  - "[[Combined Probability]]"
  - "[[Conditional Probability]]"
tags:
  - subject/mathematics
  - domain/probability
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-S9
  - syllabus/0580-E8-1
  - syllabus/9709-5-3
  - type/definition
  - type/vocabulary
  - notation/probability
  - misconception/probability-as-certainty
---

# Probability Basics 概率基础

## Definition

### Formal

The **probability** of an event $A$, written $P(A)$, is a number between 0 and 1 inclusive that measures how likely the event is to occur:

$$0 \leq P(A) \leq 1$$

If all outcomes are **equally likely**, the probability of event $A$ is:

$$P(A) = \dfrac{n(A)}{n(S)} = \dfrac{\text{number of outcomes in } A}{\text{total number of outcomes}}$$

where $S$ is the **sample space** — the set of all possible outcomes.

### Intuitive

Probability answers the question: **"how likely is this to happen?"**

- $P(A) = 0$ means "impossible — it will never happen"
- $P(A) = 1$ means "certain — it will definitely happen"
- $P(A) = 0.5$ means "even chance — equally likely to happen or not"

Everything else falls somewhere on this scale. The closer to 1, the more likely; the closer to 0, the less likely.

### 中文锚点 (Chinese Anchor)

**概率** (gàilǜ)："概"是大概，"率"是比率——大概的比率，某件事发生的可能性有多大。

$$P(A) = \dfrac{\text{A发生的情况数}}{\text{所有可能的情况数}}$$

概率的范围：$0 \leq P(A) \leq 1$。0是不可能，1是一定发生，0.5是一半一半。

> [!tip] 概率与集合的关系
> 概率用的是集合语言！事件$A$其实就是样本空间$S$的一个[[Subset|子集]]。$P(A) = \dfrac{n(A)}{n(S)}$和我们在集合论里学的$n(A)$（[[Cardinality|基数]]）是同一个概念。

## Vocabulary — The Language of Probability

This is where international students struggle most. The words matter as much as the maths.

| Term | Meaning | Example (rolling a die) | 中文 |
|---|---|---|---|
| **Experiment** / **Trial** | An action with uncertain outcomes | Rolling a die once | 实验 / 试验 |
| **Outcome** | One possible result of an experiment | Rolling a 4 | 结果 |
| **Sample space** ($S$) | The set of ALL possible outcomes | $S = \{1, 2, 3, 4, 5, 6\}$ | 样本空间 |
| **Event** | A subset of the sample space — one or more outcomes we're interested in | "Rolling an even number" = $\{2, 4, 6\}$ | 事件 |
| **Equally likely** | Every outcome has the same probability | A fair die: each face has $P = \dfrac{1}{6}$ | 等可能的 |
| **Random** | The outcome cannot be predicted | Picking a card without looking | 随机的 |
| **Fair** | No outcome is favoured (= equally likely) | A fair coin: $P(\text{heads}) = P(\text{tails}) = 0.5$ | 公平的 |
| **Biased** | Some outcomes are more likely than others | A weighted coin | 有偏的 |

> [!warning] "Random" ≠ "equal"
> "Random" means unpredictable, not that all outcomes are equally likely. A biased coin is still random — you can't predict the next flip — but heads and tails are not equally likely. Students often confuse these.

### Events as Sets

This is where probability connects directly to [[Set|set theory]]:

| Probability language | Set language | Symbol |
|---|---|---|
| Sample space | Universal set | $S$ (probability) or $\xi$ (Cambridge set theory) |
| Event | Subset of the universal set | $A \subseteq S$ |
| "A happens" | Outcome is an element of $A$ | $\text{outcome} \in A$ |
| "A doesn't happen" | Complement | $A'$ |
| "A or B happens" | Union | $A \cup B$ |
| "A and B both happen" | Intersection | $A \cap B$ |
| Impossible event | Empty set | $\emptyset$ |
| Certain event | The whole sample space | $S$ |

> [!info] Why probability uses set notation
> This isn't a coincidence. Probability theory was formally built on set theory by Andrey Kolmogorov in 1933. Every probability rule has a set theory rule behind it. You already know the set rules from [[Set Operations]] — probability just adds numbers to them.

## Notation

| Symbol | Meaning | Example |
|---|---|---|
| $P(A)$ | Probability of event $A$ | $P(\text{heads}) = 0.5$ |
| $P(A')$ | Probability of "not $A$" (complement) | $P(\text{not heads}) = 0.5$ |
| $P(A) = 0$ | Event $A$ is impossible | $P(\text{rolling 7 on a standard die}) = 0$ |
| $P(A) = 1$ | Event $A$ is certain | $P(\text{rolling 1–6 on a standard die}) = 1$ |
| $n(A)$ | Number of outcomes in event $A$ | See [[Cardinality]] |
| $n(S)$ | Total number of outcomes in sample space | |

### Expressing probability

Probability can be written as a fraction, decimal, or percentage:

$$P(\text{rolling a 6}) = \dfrac{1}{6} \approx 0.167 \approx 16.7\%$$

In exams, fractions are usually preferred (exact). If the question says "give your answer as a decimal," round as instructed.

## Key Facts / Properties

### The Probability Scale

$$\underbrace{0}_{\text{impossible}} \longleftarrow \underbrace{0.5}_{\text{even chance}} \longrightarrow \underbrace{1}_{\text{certain}}$$

Every probability lives on this scale. No probability is negative. No probability exceeds 1.

> [!info] Why is probability between 0 and 1?
> Because $P(A) = \dfrac{n(A)}{n(S)}$, and $n(A)$ is always between 0 (no outcomes match) and $n(S)$ (all outcomes match). So the fraction is always between 0 and 1. This is a direct consequence of the fact that every event is a [[Subset|subset]] of the sample space: $A \subseteq S$ implies $0 \leq n(A) \leq n(S)$.

### The Complement Rule

$$P(A') = 1 - P(A)$$

The probability of something **not** happening equals 1 minus the probability of it happening.

**Why it works:** $A$ and $A'$ together cover every possible outcome (they are **exhaustive**) and they don't overlap (they are **mutually exclusive**). So $P(A) + P(A') = 1$.

In set theory terms: $A \cup A' = S$ and $A \cap A' = \emptyset$, so $n(A) + n(A') = n(S)$. Dividing through by $n(S)$ gives the complement rule.

> [!tip] When to use the complement
> Use $P(A') = 1 - P(A)$ when "not $A$" is easier to calculate than $A$. Classic example:
>
> "What is the probability of rolling **at least one 6** in four rolls of a die?"
>
> Direct calculation is messy (one 6, or two 6s, or three, or four...). But the complement "no sixes at all" is simple:
>
> $$P(\text{no sixes in 4 rolls}) = \left(\dfrac{5}{6}\right)^4$$
>
> $$P(\text{at least one 6}) = 1 - \left(\dfrac{5}{6}\right)^4 \approx 0.518$$

### Sum of All Probabilities = 1

If $S = \{o_1, o_2, \ldots, o_n\}$ is the sample space, then:

$$P(o_1) + P(o_2) + \cdots + P(o_n) = 1$$

All probabilities in the sample space add up to 1. This is because *something* must happen.

### Mutually Exclusive Events

Two events are **mutually exclusive** if they cannot both happen at the same time:

$$A \cap B = \emptyset \quad \Longleftrightarrow \quad P(A \text{ and } B) = 0$$

For mutually exclusive events, the addition rule simplifies to:

$$P(A \cup B) = P(A) + P(B)$$

Example: rolling a die — "getting a 2" and "getting a 5" are mutually exclusive (you can't roll both at once). So $P(2 \text{ or } 5) = \dfrac{1}{6} + \dfrac{1}{6} = \dfrac{2}{6} = \dfrac{1}{3}$.

> [!warning] Only add when mutually exclusive
> $P(A \text{ or } B) = P(A) + P(B)$ **only** works when $A$ and $B$ can't overlap. If they can overlap, you're double-counting the intersection. The general rule is $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ — see [[Combined Probability]].

### Exhaustive Events

Events are **exhaustive** if at least one of them must happen — together they cover the entire sample space $S$ (the set of all possible outcomes).

$$A_1 \cup A_2 \cup \cdots \cup A_k = S$$

If events are both mutually exclusive and exhaustive, their probabilities add to exactly 1.

### Theoretical vs Experimental Probability

| Type | How it's calculated | Example |
|---|---|---|
| **Theoretical** | $\dfrac{\text{favourable outcomes}}{\text{total outcomes}}$ — uses reasoning | $P(\text{heads}) = \dfrac{1}{2}$ for a fair coin |
| **Experimental** (relative frequency) | $\dfrac{\text{times it happened}}{\text{total trials}}$ — uses data | Flipped 100 times, got 47 heads → $\dfrac{47}{100} = 0.47$ |

Theoretical probability assumes equally likely outcomes and gives an exact answer. Experimental probability comes from actual trials and gives an estimate that improves with more trials. See [[Relative and Expected Frequency]] for the full treatment.

## Worked Examples

### Example 1: Bag of marbles

A bag contains 5 red, 3 blue, and 2 green marbles. One marble is picked at random.

**Sample space:** $n(S) = 5 + 3 + 2 = 10$

(a) $P(\text{red}) = \dfrac{5}{10} = \dfrac{1}{2}$

(b) $P(\text{blue}) = \dfrac{3}{10}$

(c) $P(\text{not green}) = 1 - P(\text{green}) = 1 - \dfrac{2}{10} = \dfrac{8}{10} = \dfrac{4}{5}$

(d) $P(\text{red or blue}) = \dfrac{5}{10} + \dfrac{3}{10} = \dfrac{8}{10} = \dfrac{4}{5}$

(These are mutually exclusive — a marble can't be both red and blue.)

### Example 2: Playing cards

A standard deck has 52 cards: 4 suits (hearts, diamonds, clubs, spades) × 13 ranks (A, 2–10, J, Q, K).

(a) $P(\text{ace}) = \dfrac{4}{52} = \dfrac{1}{13}$

(b) $P(\text{heart}) = \dfrac{13}{52} = \dfrac{1}{4}$

(c) $P(\text{ace or heart})$ — careful! These are **not** mutually exclusive (the ace of hearts is both).

$$P(\text{ace or heart}) = P(\text{ace}) + P(\text{heart}) - P(\text{ace and heart}) = \dfrac{4}{52} + \dfrac{13}{52} - \dfrac{1}{52} = \dfrac{16}{52} = \dfrac{4}{13}$$

(This uses the general addition rule from [[Combined Probability]] — included here as a preview.)

### Example 3: Probability from a frequency table

| Score | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Frequency | 8 | 12 | 10 | 15 | 9 | 6 |

A die was rolled 60 times. Estimate the probability of rolling a 4.

$$P(4) \approx \dfrac{15}{60} = \dfrac{1}{4} = 0.25$$

This is experimental probability (relative frequency). For a fair die, theoretical probability would be $\dfrac{1}{6} \approx 0.167$. The difference suggests this die may be biased — or we need more trials.

## Common Misconceptions (Teaching Notes)

### 1. "Probability can be greater than 1" or "probability can be negative"

Students sometimes calculate $P(A) = \dfrac{8}{5}$ and don't notice the problem. If $P(A) > 1$ or $P(A) < 0$, something went wrong.

**Fix:** "Probability is always between 0 and 1. If your answer is outside this range, check your working — you've probably divided wrong or miscounted."

### 2. "If an event hasn't happened for a while, it's 'due'"

The gambler's fallacy. A fair coin that has landed heads 10 times in a row still has $P(\text{heads}) = 0.5$ on the next flip. The coin has no memory.

**Fix:** "Each trial is independent. The coin doesn't know what happened before. Past results don't change future probabilities."

### 3. Confusing "equally likely" with "50-50"

Students assume every situation is 50-50: "either it rains or it doesn't, so $P(\text{rain}) = 0.5$." That's wrong — having two possible outcomes doesn't make them equally likely.

**Fix:** "Equally likely means each outcome has the same chance. Rolling a die: 6 outcomes, each equally likely, so each is $\dfrac{1}{6}$. But 'rain or no rain' are not equally likely just because there are two options."

### 4. Adding probabilities for non-mutually-exclusive events

Students compute $P(\text{ace or heart}) = \dfrac{4}{52} + \dfrac{13}{52} = \dfrac{17}{52}$ — overcounting because they didn't subtract the overlap.

**Fix:** "Before adding, ask: can both happen at the same time? If yes, you're double-counting the overlap and need to subtract $P(A \cap B)$." Connect to [[Venn Diagram]] regions.

### 5. Confusing $P(A) = 0$ with "unlikely"

$P(A) = 0$ means **impossible**, not just unlikely. $P(\text{rolling a 7}) = 0$ on a standard die. But $P(\text{rolling six 6s in a row}) = \left(\dfrac{1}{6}\right)^6 \approx 0.00002$ — very unlikely, but not impossible.

**Fix:** "Zero means never. A tiny number means rarely. There's a difference."

> [!info] Beyond syllabus — does $P(A) = 0$ really mean impossible?
> At IGCSE: yes, treat it that way. But at university, the answer is surprisingly **no**. Pick a random real number between 0 and 1. The probability of picking *exactly* 0.5 is $P = 0$ — there are infinitely many choices, so any single number has zero probability. But picking 0.5 isn't impossible — it could happen.
>
> This only occurs with **continuous** distributions (infinitely many outcomes). For anything at IGCSE — dice, coins, cards, marbles — the sample space is finite, and $P(A) = 0$ genuinely means impossible. The distinction matters in university-level measure theory, but not here.

## Exam Notes

### OxAQA 9260

- S9: understand and use the vocabulary of probability; probability scale 0 to 1
- Notation: $P(A)$, complement $P(A')$
- Both Paper 1E and Paper 2E
- Questions typically: "Find the probability of...", probability from frequency tables, showing probabilities sum to 1
- Often combined with Venn diagrams (link to [[Venn Diagram]] and [[Set Operations]])
- Mutually exclusive and exhaustive are key vocabulary (S15)

### Cambridge 0580

- E8.1: probability scale, notation, single events, complement
- Same core content as 9260 S9
- Expect questions involving listing outcomes, using frequency tables, and applying the complement rule
- Probability of combined events is in E8.3 — see [[Combined Probability]]

### AP / IB / A-Level

- **AP Statistics:** adds formal sample space notation, introduces probability as a long-run relative frequency
- **IB Mathematics:** formal axiomatic definition (Kolmogorov axioms) at HL
- **A-Level:** links to combinatorics for counting outcomes — connects to [[Permutations and Combinations]]

## Connections

> [!info] Why probability matters — your brain is a prediction engine
> The human brain is, at its core, a machine for predicting what happens next. Every time you catch a ball, cross a road, or decide whether to trust someone, your brain is running a probability calculation — estimating likely outcomes from incomplete information.
>
> Probability and statistics are the mathematical language for what your brain does intuitively. But intuition has limits: we overreact to small samples, confuse correlation with causation, and misjudge rare events (see [[Relative and Expected Frequency]] and [[Conditional Probability]] for examples). These natural blind spots are exactly why the formal framework exists — and why fields from medicine to AI depend on getting probability right.
>
> The deepest question — "can we go beyond prediction to understand *why* things happen?" — is what Judea Pearl's work on causal inference tries to answer (see [[Conditional Probability#4. Assuming conditional probability means causation|the causation misconception]]). Probability tells us what *is likely*. Causality tells us what *would happen if*. Together, they describe how we make sense of an uncertain world.

- **Foundation:** [[Set|Set Theory cluster]] — probability is built on sets; events are subsets, complement/union/intersection carry over directly
- **Key tools:** [[Venn Diagram]] — used to visualise probability problems with overlapping events
- **Key tools:** [[Cardinality]] — $n(A)$ and $n(S)$ are the counting tools behind $P(A) = \dfrac{n(A)}{n(S)}$
- **Next:** [[Relative and Expected Frequency]] — experimental probability and expected number of occurrences
- **Next:** [[Combined Probability]] — what happens when events combine (and, or, independent, tree diagrams)
- **Next:** [[Conditional Probability]] — probability when you already know something happened
- **Counting:** [[Permutations and Combinations]] — systematic ways to count $n(A)$ and $n(S)$ for complex problems
- **For 9709 students:** [[MF19 Reference (9709)]] — which formulas on this card are on the MF19 exam sheet vs need memorising. (Other boards have their own sheets.)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $P(A)$ | `P(A)` | Probability of event $A$ |
| $P(A')$ | `P(A')` | Probability of complement |
| $P(A \cup B)$ | `P(A \cup B)` | Probability of $A$ or $B$ |
| $P(A \cap B)$ | `P(A \cap B)` | Probability of $A$ and $B$ |
| $\emptyset$ | `\emptyset` | Impossible event |
| $\leq$ | `\leq` | Less than or equal to |
| $\dfrac{n(A)}{n(S)}$ | `\dfrac{n(A)}{n(S)}` | Theoretical probability formula |
