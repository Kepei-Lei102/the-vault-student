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

If the sample space is **finite** and all outcomes are **equally likely**, the probability of event $A$ is:

$$P(A) = \dfrac{n(A)}{n(S)} = \dfrac{\text{number of outcomes in } A}{\text{total number of outcomes}}$$

where $S$ is the **sample space** — the set of all possible outcomes.

### Intuitive

Probability answers the question: **"how likely is this to happen?"**

In an elementary finite model where every listed outcome has positive probability:

- $P(A) = 0$ means "impossible — no listed outcome belongs to $A$"
- $P(A) = 1$ means "certain — it will definitely happen"
- $P(A) = 0.5$ means "even chance — equally likely to happen or not"

For continuous distributions, probability zero need not mean an empty event; the distinction is explained below. Everything else falls somewhere on this scale. The closer to 1, the more likely; the closer to 0, the less likely.

### 中文锚点 (Chinese Anchor)

袋子里有九颗红珠子、一颗蓝珠子，大小手感都一样。摇匀后闭眼摸一颗，你当然更容易摸到红的——因为十颗里有九颗都能让“摸到红珠子”这件事发生。每次摸完放回，再摇匀重摸，也不等于前九次必须摸到红的、第十次才轮到蓝的。概率说的是在这样的条件下，哪种结果更容易出现，不是在给每一次结果排班。

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
| $P(A) = 0$ | Zero probability; impossible in the finite positive-outcome model | $P(\text{rolling 7 on a standard die}) = 0$ |
| $P(A) = 1$ | Probability one; the complement has probability zero | $P(\text{rolling 1–6 on a standard die}) = 1$ |
| $n(A)$ | Number of outcomes in event $A$ | See [[Cardinality]] |
| $n(S)$ | Total number of outcomes in sample space | |

### Expressing probability

Probability can be written as a fraction, decimal, or percentage:

$$P(\text{rolling a 6}) = \dfrac{1}{6} \approx 0.167 \approx 16.7\%$$

In exams, fractions are usually preferred (exact). If the question says "give your answer as a decimal," round as instructed.

## Key Facts / Properties

### The Probability Scale

For the elementary finite positive-outcome model:

$$\underbrace{0}_{\text{impossible}} \longleftarrow \underbrace{0.5}_{\text{even chance}} \longrightarrow \underbrace{1}_{\text{certain}}$$

Every probability lives on this scale. No probability is negative. No probability exceeds 1.

> [!info] Why is probability between 0 and 1?
> In a finite equally likely model, $P(A) = \dfrac{n(A)}{n(S)}$, and $n(A)$ is always between 0 (no outcomes match) and $n(S)$ (all outcomes match). So the fraction is always between 0 and 1. This is a direct consequence of the fact that every event is a [[Subset|subset]] of the sample space: $A \subseteq S$ implies $0 \leq n(A) \leq n(S)$. More generally, probability is non-negative, the whole sample space has probability one, and probabilities add for disjoint events. Since $A$ and its complement split that whole, $P(A)$ cannot exceed one.

### The Complement Rule

$$P(A') = 1 - P(A)$$

The probability of something **not** happening equals 1 minus the probability of it happening.

**Why it works:** $A$ and $A'$ together cover every possible outcome (they are **exhaustive**) and they don't overlap (they are **mutually exclusive**). So $P(A) + P(A') = 1$.

For finite equally likely outcomes, the same proof can be written using counts: $A \cup A' = S$ and $A \cap A' = \emptyset$, so $n(A) + n(A') = n(S)$. Dividing through by $n(S)$ gives the complement rule.

> [!tip] When to use the complement
> Use $P(A') = 1 - P(A)$ when "not $A$" is easier to calculate than $A$. Classic example:
>
> "What is the probability of rolling **at least one 6** in four independent rolls of a fair die?"
>
> Direct calculation is messy (one 6, or two 6s, or three, or four...). But the complement "no sixes at all" is simple:
>
> $$P(\text{no sixes in 4 rolls}) = \left(\dfrac{5}{6}\right)^4$$
>
> $$P(\text{at least one 6}) = 1 - \left(\dfrac{5}{6}\right)^4 \approx 0.518$$

### Sum of All Probabilities = 1

If $S = \{o_1, o_2, \ldots, o_n\}$ is the sample space, then:

$$P(o_1) + P(o_2) + \cdots + P(o_n) = 1$$

For a finite sample space, the probabilities of its individual outcomes add up to 1. This is because *something* must happen.

### Mutually Exclusive Events

Two events are **mutually exclusive** if they cannot both happen at the same time:

$$A \cap B = \emptyset \quad \Longrightarrow \quad P(A \text{ and } B) = 0$$

For mutually exclusive events, the addition rule simplifies to:

$$P(A \cup B) = P(A) + P(B)$$

Example: rolling a die — "getting a 2" and "getting a 5" are mutually exclusive (you can't roll both at once). So $P(2 \text{ or } 5) = \dfrac{1}{6} + \dfrac{1}{6} = \dfrac{2}{6} = \dfrac{1}{3}$.

> [!warning] Account for the overlap
> Disjoint events have no overlap, so their probabilities add directly. In general, subtract the probability of their intersection to avoid double-counting it. A nonempty intersection can have probability zero in more general models; disjointness is the set condition $A\cap B=\emptyset$. The general rule is $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ — see [[Combined Probability]].

### Exhaustive Events

Events are **exhaustive** if at least one of them must happen — together they cover the entire sample space $S$ (the set of all possible outcomes).

$$A_1 \cup A_2 \cup \cdots \cup A_k = S$$

If events are both mutually exclusive and exhaustive, their probabilities add to exactly 1.

### Theoretical vs Experimental Probability

| Type | How it's calculated | Example |
|---|---|---|
| **Theoretical** | $\dfrac{\text{favourable outcomes}}{\text{total outcomes}}$ — for finite equally likely outcomes | $P(\text{heads}) = \dfrac{1}{2}$ for a fair coin |
| **Experimental** (relative frequency) | $\dfrac{\text{times it happened}}{\text{total trials}}$ — uses data | Flipped 100 times, got 47 heads → $\dfrac{47}{100} = 0.47$ |

The counting formula assumes finite equally likely outcomes; a theoretical model can also assign unequal probabilities. Relative frequency estimates a probability from data. With independent repetitions under the same conditions, more trials generally give a more stable estimate; each additional trial need not move it closer. See [[Relative and Expected Frequency]] for the full treatment.

## Worked Examples

### Example 1: Bag of marbles

A bag contains 5 red, 3 blue, and 2 green marbles. One marble is picked so each of the ten is equally likely.

**Tool: count equally likely outcomes. Trigger: one uniform draw from ten marbles.**

**Sample space:** $n(S) = 5 + 3 + 2 = 10$

(a) $P(\text{red}) = \dfrac{5}{10} = \dfrac{1}{2}$

(b) $P(\text{blue}) = \dfrac{3}{10}$

**Tool: complement. Trigger: “not green” is the opposite of one simple event.**

(c) $P(\text{not green}) = 1 - P(\text{green}) = 1 - \dfrac{2}{10} = \dfrac{8}{10} = \dfrac{4}{5}$

**Tool: add disjoint-event probabilities. Trigger: a marble has exactly one colour.**

(d) $P(\text{red or blue}) = \dfrac{5}{10} + \dfrac{3}{10} = \dfrac{8}{10} = \dfrac{4}{5}$

(These are mutually exclusive — a marble can't be both red and blue.)

### Example 2: Playing cards

A standard deck has 52 cards: 4 suits (hearts, diamonds, clubs, spades) × 13 ranks (A, 2–10, J, Q, K).

**Tool: count equally likely outcomes. Trigger: assume a uniform draw from all 52 cards.**

(a) $P(\text{ace}) = \dfrac{4}{52} = \dfrac{1}{13}$

(b) $P(\text{heart}) = \dfrac{13}{52} = \dfrac{1}{4}$

**Tool: inclusion–exclusion. Trigger: the ace of hearts belongs to both events.**

(c) $P(\text{ace or heart})$ — careful! These are **not** mutually exclusive (the ace of hearts is both).

$$P(\text{ace or heart}) = P(\text{ace}) + P(\text{heart}) - P(\text{ace and heart}) = \dfrac{4}{52} + \dfrac{13}{52} - \dfrac{1}{52} = \dfrac{16}{52} = \dfrac{4}{13}$$

(This uses the general addition rule from [[Combined Probability]] — included here as a preview.)

### Example 3: Probability from a frequency table

| Score | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Frequency | 8 | 12 | 10 | 15 | 9 | 6 |

A die was rolled 60 times. Estimate the probability of rolling a 4.

**Tool: relative frequency. Trigger: observed trials provide an estimate, not a stated fair-die model.**

$$P(4) \approx \dfrac{15}{60} = \dfrac{1}{4} = 0.25$$

This is experimental probability (relative frequency). For a fair die, theoretical probability would be $\dfrac{1}{6} \approx 0.167$. This difference alone does not establish bias; sampling variation can produce it even for a fair die.

## Common Misconceptions (Teaching Notes)

### 1. "Probability can be greater than 1" or "probability can be negative"

Students sometimes calculate $P(A) = \dfrac{8}{5}$ and don't notice the problem. If $P(A) > 1$ or $P(A) < 0$, something went wrong.

**Fix:** "Probability is always between 0 and 1. If your answer is outside this range, check your working — you've probably divided wrong or miscounted."

### 2. "If an event hasn't happened for a while, it's 'due'"

The gambler's fallacy. Under an independent fair-flip model, a coin that has landed heads 10 times in a row still has $P(\text{heads}) = 0.5$ on the next flip. The coin has no memory.

**Fix:** "Each trial is independent. The coin doesn't know what happened before. In this model, past results do not change the next-flip probability. Dependence or evidence that the coin is biased would change the analysis."

### 3. Confusing "equally likely" with "50-50"

Students assume every situation is 50-50: "either it rains or it doesn't, so $P(\text{rain}) = 0.5$." That's wrong — having two possible outcomes doesn't make them equally likely.

**Fix:** "Equally likely means each outcome has the same chance. Rolling a die: 6 outcomes, each equally likely, so each is $\dfrac{1}{6}$. But 'rain or no rain' are not equally likely just because there are two options."

### 4. Adding probabilities for non-mutually-exclusive events

Students compute $P(\text{ace or heart}) = \dfrac{4}{52} + \dfrac{13}{52} = \dfrac{17}{52}$ — overcounting because they didn't subtract the overlap.

**Fix:** "Before adding, ask: can both happen at the same time? If yes, you're double-counting the overlap and need to subtract $P(A \cap B)$." Connect to [[Venn Diagram]] regions.

### 5. Treating every zero probability as impossibility

In a finite model where every elementary outcome has positive probability, a zero-probability event contains no outcomes. Rolling 7 on a standard six-sided die is impossible; six consecutive 6s on independent fair rolls are merely rare: $(1/6)^6\approx0.0000214$.

For a continuous uniform position on $[0,1]$, however, any particular point has probability zero. Probabilities are areas over intervals, and a point has zero width. A result still occurs somewhere. Probability one similarly means that the exceptions have probability zero, not necessarily that no exceptions exist. See [[Continuous Random Variables]].

The distinction depends on the model, not on the student's year group. Even a finite probability model can include an elementary outcome assigned zero weight; the positive-weight condition above matters.

## Exam Notes

### Cambridge 0580 and OxfordAQA 9260

- **0580 C8.1/E8.1:** probability scale, single events and complements. Core does **not** require probability notation; Extended does. C8.2/E8.2 uses relative frequency; E8.3 develops combined events. State the event, count under an equally likely model, or divide observed frequency by total trials as appropriate.
- **9260 S9–S13:** vocabulary/scale, theoretical and experimental probability, comparison of data with a model, variation between trials and the value of larger samples. **S14–S16:** sample spaces, mutually exclusive/exhaustive outcomes and Venn diagrams. S9 alone does not cover all these outcomes. Combined and conditional calculations continue in S17–S18.

### A-Level mathematics

- **9709 §5.3 (Probability & Statistics 1):** evaluate probabilities, use addition/multiplication appropriately, distinguish exclusivity from independence and calculate conditional probabilities. Explicit use of the general union formula is not required; diagrams and sample spaces can supply the reasoning. Counting connects to §5.2.
- **Edexcel IAL S1 §3:** elementary probability, complements, sample spaces, addition/multiplication, independence and conditional probability. **OxfordAQA 9660 S1.1 (§3.2.2):** probability rules, independent/mutually exclusive events and conditional probability; set notation is not essential.
- **9231:** assumes 9709 knowledge; elementary probability is a prerequisite for Further Statistics, not a separate new unit. **0606:** no probability topic.

### IB Mathematics AA and AI

Both guides, **SL4.5–SL4.6** (also required at HL), cover outcomes/sample spaces, equally likely counting, relative frequency, complements, expected counts, diagrams, combined events, independence and conditional probability. There is no named HL requirement to memorise Kolmogorov's axioms. [AA guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-analysis-and-approaches-guide-en.pdf); [AI guide](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-applications-and-interpretation-guide-en.pdf).

### AP

**AP Statistics, revised course effective fall 2026, Topics 2.3–2.5:** simulation and long-run frequency, sample space, probability bounds, complements and mutually exclusive events; 2.6–2.7 continue conditional probability and independence. Explain which event and denominator the context requires. **AP Calculus AB/BC:** no elementary probability unit; using integration on a density is an application of calculus, not a separate probability-course requirement. [Current course description](https://apcentral.collegeboard.org/media/pdf/ap-statistics-course-and-exam-description.pdf).

### Formula status and scope

The elementary counting rule needs finite equally likely outcomes. Complement and union identities work more generally. Derive them from the sample space and overlap rather than relying on a particular board supplying them. The continuous zero-probability distinction is an enrichment bridge here; it becomes explicit in continuous distributions.

## Connections

> [!info] Why probability matters — your brain is a prediction engine
> Catching a ball or crossing a road involves anticipating uncertain outcomes. Probability offers a model for such decisions; this does not mean the brain literally evaluates the formulas above. In quality control, a manufacturer can instead make the calculation explicitly: sample items at random, count defects, and use that relative frequency to estimate the process defect probability. A small sample leaves uncertainty; a changed process needs fresh evidence.
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
- **For 9709 students:** [[MF19 Reference (9709)]] — which formulas are on the MF19 exam sheet vs need memorising. (Other boards have their own sheets.)

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
