---
chinese: 条件概率 (tiáojiàn gàilǜ)
prerequisites:
  - "[[Probability Basics]]"
  - "[[Combined Probability]]"
  - "[[Venn Diagram]]"
leads_to:
  - "[[Discrete Random Variables]]"
tags:
  - subject/mathematics
  - domain/probability
  - level/GCSE
  - level/IGCSE
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - syllabus/9260-S18
  - syllabus/0580-E8-4
  - syllabus/9709-5-3
  - type/concept
  - notation/P-notation
  - notation/set-notation
  - misconception/conditional-vs-unconditional
---

# Conditional Probability

## Definition

### Formal

The **conditional probability** of $A$ given $B$ is:

$$P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} \qquad \text{where } P(B) > 0$$

This reads: "the probability of $A$, given that $B$ has already happened."

### Intuitive

Conditional probability asks: **"Now that I know something happened, how does that change the odds?"**

When you learn that $B$ happened, you're no longer looking at the entire sample space $S$ — you're zooming in on just the outcomes inside $B$. The conditional probability $P(A \mid B)$ measures what fraction of $B$'s outcomes also belong to $A$.

Think of it as a camera zoom: $B$ becomes your new "whole world," and you ask what proportion of that world overlaps with $A$.

### 中文 Anchor

| English | 中文 | Pinyin |
|---------|------|--------|
| conditional probability | 条件概率 | tiáojiàn gàilǜ |
| given that | 在……条件下 | zài…tiáojiàn xià |
| reduced sample space | 缩小的样本空间 | suōxiǎo de yàngběn kōngjiān |
| dependent events | 相依事件 | xiāngyī shìjiàn |

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $P(A \mid B)$ | Probability of $A$ **given** $B$ has happened |
| $P(B \mid A)$ | Probability of $B$ **given** $A$ has happened — **not the same** as $P(A \mid B)$ |
| $P(A \cap B)$ | Probability of both $A$ and $B$ — see [[Combined Probability]] |

The vertical bar $\mid$ reads **"given"**. Everything after the bar is what you already know.

---

## Key Facts / Properties

### Why the Formula Works — Reducing the Sample Space

> [!info] Why $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$?
> Imagine 100 students. 40 study French ($F$), 30 study Spanish ($S$), and 10 study both.
>
> Unconditionally: $P(F) = \dfrac{40}{100} = 0.4$
>
> Now someone tells you: "This student studies Spanish." You're no longer choosing from all 100 students — you're choosing from the **30 who study Spanish**. Of those 30, how many also study French? The 10 who study both.
>
> $$P(F \mid S) = \dfrac{10}{30} = \dfrac{1}{3}$$
>
> Using the formula: $P(F \mid S) = \dfrac{P(F \cap S)}{P(S)} = \dfrac{10/100}{30/100} = \dfrac{10}{30} = \dfrac{1}{3}$ ✓
>
> The formula works because dividing by $P(B)$ **rescales** the sample space — it makes $B$ the new "whole" (denominator), and $A \cap B$ is the part of that new whole you care about (numerator).

### The General Multiplication Rule

Rearranging the conditional probability formula:

$$P(A \cap B) = P(A) \times P(B \mid A)$$

or equivalently:

$$P(A \cap B) = P(B) \times P(A \mid B)$$

This is the **general multiplication rule** — it works for **all** events, not just independent ones. Every tree diagram uses this rule: the second branch is always a conditional probability.

**Example — without replacement:** A bag has 4 red and 6 blue counters. Two are picked without replacement.

$$P(R_1 \cap R_2) = P(R_1) \times P(R_2 \mid R_1) = \dfrac{4}{10} \times \dfrac{3}{9} = \dfrac{12}{90} = \dfrac{2}{15}$$

The $\dfrac{3}{9}$ is $P(R_2 \mid R_1)$ — the probability of red on the second pick, **given** that the first pick was red (so one red marble is gone).

> [!tip] Tree diagrams are conditional probability in disguise
> Every tree diagram branch after the first stage is a conditional probability:
>
> - First branch: $P(R_1) = \dfrac{4}{10}$ — unconditional
> - Second branch after red: $P(R_2 \mid R_1) = \dfrac{3}{9}$ — conditional on first being red
> - Second branch after blue: $P(R_2 \mid B_1) = \dfrac{4}{9}$ — conditional on first being blue
>
> When you "multiply along branches," you're applying the general multiplication rule: $P(R_1) \times P(R_2 \mid R_1)$.
>
> For a full worked tree diagram with all branches and probabilities, see [[Combined Probability#Tree Diagrams]].

### Independence — the Formal Definition

Two events are **independent** if and only if:

$$P(A \mid B) = P(A)$$

This says: knowing $B$ happened **doesn't change** your assessment of $A$. The information is irrelevant.

When this holds, the general multiplication rule simplifies:

$$P(A \cap B) = P(A) \times P(B \mid A) = P(A) \times P(B)$$

This is the formula from [[Combined Probability]] — it's the **special case** where conditioning doesn't matter.

**How to test independence:** Given $P(A)$, $P(B)$, and $P(A \cap B)$, check whether $P(A \cap B) = P(A) \times P(B)$. If yes → independent. If no → dependent.

### Reading Conditional Probability from a Two-Way Table

Two-way tables make conditional probability visual. Read the condition as "restrict to this row (or column)."

**Example:** 200 students surveyed about sport and music.

|  | Plays sport | Doesn't play sport | Total |
|---|---|---|---|
| **Plays music** | 45 | 35 | 80 |
| **Doesn't play music** | 75 | 45 | 120 |
| **Total** | 120 | 80 | 200 |

$P(\text{music} \mid \text{sport}) = \dfrac{45}{120} = \dfrac{3}{8}$ — restrict to the "Plays sport" column (120 students), then count how many play music (45).

$P(\text{sport} \mid \text{music}) = \dfrac{45}{80} = \dfrac{9}{16}$ — restrict to the "Plays music" row (80 students), then count how many play sport (45).

Notice: $\dfrac{3}{8} \neq \dfrac{9}{16}$ — the order matters. $P(A \mid B) \neq P(B \mid A)$ in general.

### Reading Conditional Probability from a Venn Diagram

To find $P(A \mid B)$ from a [[Venn Diagram|Venn diagram]]:

1. **Zoom in** to circle $B$ — ignore everything outside $B$
2. The answer is: $\dfrac{\text{overlap region } (A \cap B)}{\text{all of } B}$

Using the French/Spanish example: circle $S$ has 30 students total (10 overlap + 20 Spanish only). The overlap is 10. So $P(F \mid S) = \dfrac{10}{30}$.

The diagram below illustrates the same idea with the tea/coffee example from Example 4. Notice how circle $C$ (the condition) stays solid while everything else fades — conditioning means $C$ becomes your "new universe":

![[venn-conditional-probability.svg|700]]

---

## Worked Examples

### Example 1: From the formula

$P(A) = 0.6$, $P(B) = 0.5$, $P(A \cap B) = 0.2$. Find $P(A \mid B)$ and $P(B \mid A)$.

$$P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{0.2}{0.5} = 0.4$$

$$P(B \mid A) = \dfrac{P(A \cap B)}{P(A)} = \dfrac{0.2}{0.6} = \dfrac{1}{3} \approx 0.333$$

**Check:** These are different, as expected. Knowing $B$ happened gives a 40% chance of $A$. Knowing $A$ happened gives a 33% chance of $B$.

### Example 2: Tree diagram — dependent events

A bag contains 5 red and 3 green balls. Two balls are drawn without replacement. Find $P(\text{second is green} \mid \text{first is red})$.

After drawing red first: 4 red and 3 green remain (7 total).

$$P(G_2 \mid R_1) = \dfrac{3}{7}$$

To find $P(\text{red first and green second})$:

$$P(R_1 \cap G_2) = P(R_1) \times P(G_2 \mid R_1) = \dfrac{5}{8} \times \dfrac{3}{7} = \dfrac{15}{56}$$

### Example 3: Two-way table

A school has 150 students. 90 are right-handed. Of the right-handed students, 60 like maths. Of the left-handed students, 20 like maths.

|  | Likes maths | Doesn't like maths | Total |
|---|---|---|---|
| **Right-handed** | 60 | 30 | 90 |
| **Left-handed** | 20 | 40 | 60 |
| **Total** | 80 | 70 | 150 |

(a) $P(\text{likes maths} \mid \text{right-handed}) = \dfrac{60}{90} = \dfrac{2}{3}$

(b) $P(\text{right-handed} \mid \text{likes maths}) = \dfrac{60}{80} = \dfrac{3}{4}$

(c) Are "likes maths" and "right-handed" independent?

Check: $P(\text{maths}) \times P(\text{right}) = \dfrac{80}{150} \times \dfrac{90}{150} = \dfrac{7200}{22500} = 0.32$

$P(\text{maths} \cap \text{right}) = \dfrac{60}{150} = 0.4$

$0.32 \neq 0.4$ → **not independent**. Right-handed students are more likely to like maths than the school average.

### Example 4: Venn diagram conditional probability

In a group of 50 people: 20 like tea ($T$), 25 like coffee ($C$), and 8 like both.

Find $P(T \mid C)$ — "given someone likes coffee, what's the probability they also like tea?"

$$P(T \mid C) = \dfrac{P(T \cap C)}{P(C)} = \dfrac{8/50}{25/50} = \dfrac{8}{25} = 0.32$$

Equivalently from the Venn diagram: zoom into circle $C$ (25 people). Of those, 8 are in the overlap. So $\dfrac{8}{25}$.

---

## Common Misconceptions

### 1. Thinking $P(A \mid B) = P(B \mid A)$

"The probability of rain given clouds equals the probability of clouds given rain." ✗

**Fix:** These are different questions with different denominators:

$$P(\text{rain} \mid \text{clouds}) = \dfrac{P(\text{rain} \cap \text{clouds})}{P(\text{clouds})} \qquad P(\text{clouds} \mid \text{rain}) = \dfrac{P(\text{rain} \cap \text{clouds})}{P(\text{rain})}$$

The numerator is the same, but the denominators differ. When it rains, there are almost certainly clouds — so $P(\text{clouds} \mid \text{rain}) \approx 1$. But clouds don't always bring rain — so $P(\text{rain} \mid \text{clouds})$ is much lower.

### 2. Confusing $P(A \mid B)$ with $P(A \cap B)$

"$P(A \mid B) = 0.2$ means there's a 20% chance both happen." ✗

**Fix:** $P(A \mid B) = 0.2$ means: **if you already know $B$ happened**, there's a 20% chance $A$ also happens. The "both happen" probability is $P(A \cap B) = P(B) \times P(A \mid B)$ — you need to multiply by $P(B)$.

### 3. Not adjusting the denominator for "without replacement"

"There are 10 balls. I drew a red one. $P(\text{next is red}) = \dfrac{3}{10}$." ✗

**Fix:** After removing one red ball, there are 9 balls left, not 10. The conditional probability uses the **reduced** sample space:

$$P(\text{red}_2 \mid \text{red}_1) = \dfrac{3}{9} = \dfrac{1}{3}$$

### 4. Assuming conditional probability means causation

"$P(\text{wet grass} \mid \text{sprinkler on}) = 0.9$, so the sprinkler **causes** wet grass." ✗

**Fix:** Conditional probability measures **association**, not causation. The grass could be wet because it rained, regardless of the sprinkler. $P(A \mid B)$ tells you how often $A$ occurs among cases where $B$ is true — it says nothing about whether $B$ caused $A$.

> [!info] Beyond syllabus — Why causation is so hard
> For centuries, statistics could only measure association ("these things tend to happen together"), never causation ("this thing *makes* that thing happen"). The distinction matters enormously — ice cream sales and drowning rates both rise in summer, but banning ice cream won't prevent drowning.
>
> In 2000, computer scientist Judea Pearl published *Causality: Models, Reasoning, and Inference*, which gave mathematics a formal language for causal reasoning using directed graphs (causal diagrams). This was a breakthrough: for the first time, researchers could rigorously distinguish "seeing" (observing a correlation) from "doing" (intervening to change an outcome). Pearl later wrote *The Book of Why* (2018) as an accessible introduction.
>
> Pearl's work earned him the Turing Award (the "Nobel Prize of computer science") and transformed fields from medicine to economics to AI. The fact that "$P(A \mid B)$ does not imply $B$ causes $A$" is not just a GCSE misconception — it's a problem that took humanity's best minds decades to solve properly. If you find the distinction between correlation and causation fascinating, this is one of the great intellectual stories of our time.

### 5. Forgetting that $P(B)$ must be greater than zero

You cannot condition on an event that has zero probability — $P(A \mid B)$ is undefined when $P(B) = 0$ because you would be dividing by zero. This rarely matters at GCSE level, but it's the reason the formula has the requirement $P(B) > 0$.

---

## Exam Notes

### OxAQA 9260

- S18 (Extension): conditional probabilities including tree diagrams and other representations
- The formula $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$ is implicit — students should understand the concept and apply it, especially through tree diagrams and Venn diagrams
- Expect "without replacement" problems as the main context for conditional probability
- Common question pattern: draw a tree diagram → identify conditional branches → calculate a combined probability → sometimes work backwards ("given that the second ball was blue, find the probability the first was red")
- Often combined with S16 (Venn diagrams) — "from the Venn diagram, find $P(A \mid B)$"

### Cambridge 0580

- E8.4: conditional probability
- **Scope note:** 0580 expects conditional probability to be understood conceptually and through tree diagrams / Venn diagrams. The formal $P(A \mid B)$ notation may or may not appear — the concept matters more than the symbol
- "Without replacement" is the standard context
- Both Paper 2 and Paper 4

### AP / IB / A-Level

- **AP Statistics:** formal conditional probability notation; multiplication rule $P(A \cap B) = P(A) \times P(B \mid A)$; independence test via $P(A \mid B) = P(A)$
- **IB Mathematics AA HL:** Bayes' theorem $P(A \mid B) = \dfrac{P(B \mid A) \times P(A)}{P(B)}$ for "reversing" conditional probabilities
- **A-Level Statistics (S1):** conditional probability formula is core content; tree diagrams with conditional branches; Venn diagram questions asking for $P(A \mid B)$

### Beyond high school — University

- Bayes' theorem becomes central in machine learning, medical diagnostics, and spam filtering — "given the test result, what is the probability the patient is actually sick?"
- The "base rate fallacy" — people overestimate $P(\text{sick} \mid \text{positive test})$ because they ignore how rare the disease is. This is a famous example of why $P(A \mid B) \neq P(B \mid A)$.
- Conditional expectation $E[X \mid Y]$ extends the idea to random variables — the foundation of regression analysis
- **A secret history:** updating a probability as evidence arrives — Bayesian inference — was turned into an industrial codebreaking weapon by Alan Turing at Bletchley Park (his "Banburismus" method), years before statisticians embraced it, then classified for decades. The story is in [[Stories/Turing at Bletchley]].

---

## Connections

- **Foundation:** [[Combined Probability]] — the addition and multiplication rules; tree diagrams; Venn diagrams for probability
- **Foundation:** [[Probability Basics]] — sample space, complement rule, mutually exclusive events
- **Set theory:** [[Intersection]] — $P(A \cap B)$ is the numerator of the conditional probability formula
- **Diagrams:** [[Venn Diagram]] — "zoom into circle $B$" is the visual meaning of conditioning
- **Counting:** [[Permutations and Combinations]] — counting restricted outcomes often involves conditional reasoning
- **Extends to:** Bayes' theorem (AP / IB / university) — "reversing" a conditional probability
- **For 9709 students:** [[MF19 Reference (9709)]] — which formulas on this card are on the MF19 exam sheet vs need memorising. (Other boards have their own sheets.)

> [!info] Beyond syllabus — The Monty Hall problem
> You're on a game show. Three doors: behind one is a car, behind the other two are goats. You pick Door 1. The host (who knows what's behind each door) opens Door 3, revealing a goat. Should you switch to Door 2?
>
> **Yes — switching wins $\dfrac{2}{3}$ of the time.**
>
> This is counterintuitive because people treat it as a fresh 50-50 choice. But the host's action is **not random** — he always opens a door with a goat. His choice gives you **information**, which changes the conditional probabilities:
>
> - $P(\text{car behind Door 2} \mid \text{host opens Door 3}) = \dfrac{2}{3}$
> - $P(\text{car behind Door 1} \mid \text{host opens Door 3}) = \dfrac{1}{3}$
>
> Your original choice had a $\dfrac{1}{3}$ chance of being right. The host didn't change that — he just concentrated the remaining $\dfrac{2}{3}$ onto one door. This problem has famously confused mathematicians and is a perfect example of why conditional probability requires careful thinking about what information you have.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $P(A \mid B)$ | `P(A \mid B)` | Conditional probability — "given" |
| $P(A \cap B)$ | `P(A \cap B)` | Joint probability — "and" |
| $\dfrac{P(A \cap B)}{P(B)}$ | `\dfrac{P(A \cap B)}{P(B)}` | Conditional probability formula |
| $P(A) \times P(B \mid A)$ | `P(A) \times P(B \mid A)` | General multiplication rule |
