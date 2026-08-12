---
chinese: 代数证明 (dàishù zhèngmíng)
prerequisites:
  - "[[Logic]]"
  - "[[Chain of Thought]]"
  - "[[Laws of Indices]]"
  - "[[Surds]]"
  - "[[Factors and Multiples (Vocab)]]"
  - "[[Algebraic Expressions (Vocab)]]"
  - "[[Angles in Parallel Lines (Vocab)]]"
  - "[[Collecting Like Terms (Vocab)]]"
  - "[[Expanding Brackets (Vocab)]]"
  - "[[Factorising (Vocab)]]"
leads_to:
  - "[[Geometrical Proof]]"
  - "[[Proof by Contradiction]]"
  - "[[Proof by Induction]]"
  - "[[Proof by Exhaustion]]"
  - "[[Disproof by Counterexample]]"
tags:
  - subject/mathematics
  - domain/algebra
  - domain/logic
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - syllabus/9260-A8
  - type/proof
  - type/exam-technique
  - misconception/proof-by-example
  - misconception/circular-reasoning
---

# Algebraic Proof 代数证明

## Definition

An **algebraic proof** (代数证明) is a chain of logical steps, written in algebra, that shows a mathematical statement must be true **for all cases** — not just for a few examples.

The key word is **all**. Checking that $2 + 4 = 6$ is even doesn't prove "the sum of two even numbers is always even." A proof must work for *every possible* pair of even numbers simultaneously.

### 中文锚点

代数证明 = 用代数推导证明一个数学命题对所有情况都成立。不是举例子，而是用字母代替数字，让论证覆盖所有可能。

---

## §1 The Toolkit — Representing Numbers Algebraically

The first step of any algebraic proof is translating English into algebra. These representations appear in almost every 9260 proof question.

> [!important] $n \in \mathbb{Z}$ — unless stated otherwise, $n$ is an **integer**
> Throughout this card (and in almost every IGCSE proof question), letters like $n$, $m$, $k$ represent **integers** ($\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$). The representations below — $2n$ for even, $2n+1$ for odd, etc. — only work because $n$ is an integer. If $n = 1.5$, then $2n = 3$ is not even! Always state "$n$ is an integer" or "$n \in \mathbb{Z}$" in your proof setup.

| English statement | Algebraic form | Why |
|-------------------|---------------|-----|
| Any integer | $n$, where $n \in \mathbb{Z}$ | A letter stands for *every* integer at once |
| Any even number | $2n$ | An integer multiplied by 2 is always even |
| Any odd number | $2n + 1$ | One more than an even number is always odd |
| Two consecutive integers | $n$ and $n + 1$ | They differ by 1 |
| Three consecutive integers | $n$, $n+1$, $n+2$ | |
| Two consecutive even numbers | $2n$ and $2n + 2$ | |
| Two consecutive odd numbers | $2n + 1$ and $2n + 3$ | |
| A multiple of 3 | $3k$ | |
| A number that leaves remainder 1 when divided by 3 | $3k + 1$ | |
| The square of an even number | $(2n)^2 = 4n^2$ | A multiple of 4 |
| The square of an odd number | $(2n+1)^2 = 4n^2 + 4n + 1$ | One more than a multiple of 4 |

> [!tip] Two unknowns for two independent choices
> "The sum of **any** two even numbers" needs **two different** letters: $2m + 2n$, NOT $2n + 2n = 4n$. Using the same letter forces them to be equal — $4n$ only represents sums like $2 + 2$, $4 + 4$, $6 + 6$. Use $m$ and $n$ for independent choices.

---

## §2 Proof Structure

Every algebraic proof follows the same skeleton (from [[Logic]] and [[Chain of Thought]]):

1. **State what you're proving** — the claim, in words and/or algebra.
2. **Set up** — represent the general case using letters.
3. **Transform** — use algebra to manipulate the expression step by step.
4. **Conclude** — explain why the final form proves the claim.

The conclusion must link back to the claim. If you're proving "the result is always even," your final line must say *why* the expression is even (e.g., "which is $2 \times (\ldots)$, a multiple of 2, so it is even").

> [!warning] "It works for examples" is NOT a proof
> Testing $n = 1, 2, 3$ and getting the right answer is **verification**, not proof. The 9260 mark scheme gives zero marks for numerical examples unless the question says "Verify." A proof must work for the general case.

---

## §3 Worked Examples

### Example 1 — Prove that the sum of any two odd numbers is even

**Setup:** Let the two odd numbers be $2m + 1$ and $2n + 1$ (different letters — they're independent).

**Transform:**

$$(2m + 1) + (2n + 1) = 2m + 2n + 2 = 2(m + n + 1)$$

**Conclude:** $2(m + n + 1)$ is $2 \times \text{(integer)}$, which is even. $\square$

### Example 2 — Prove that the difference between the squares of consecutive integers is always odd

**Setup:** Let the consecutive integers be $n$ and $n + 1$.

**Transform:**

$$(n+1)^2 - n^2 = n^2 + 2n + 1 - n^2 = 2n + 1$$

**Conclude:** $2n + 1$ is always odd (one more than an even number). $\square$

### Example 3 — Prove that $n^2 - n$ is always even

**Transform (Method 1 — factorising):**

$$n^2 - n = n(n - 1)$$

This is the product of two consecutive integers. One of any two consecutive integers must be even, so the product is always even. $\square$

**Transform (Method 2 — case analysis):**

- If $n$ is even: $n = 2k$, so $n^2 - n = 4k^2 - 2k = 2(2k^2 - k)$ — even. ✓
- If $n$ is odd: $n = 2k+1$, so $n^2 - n = (2k+1)^2 - (2k+1) = 4k^2 + 4k + 1 - 2k - 1 = 4k^2 + 2k = 2(2k^2 + k)$ — even. ✓

Both cases give an even result. $\square$

> [!tip] Two methods — one factoring, one exhaustion
> Example 3 shows that many proof questions have multiple valid approaches. The factoring method is slicker; the case analysis method is more mechanical but always works when you can split into exhaustive cases. The 9260 mark scheme accepts both.

### Example 4 — "Show that" with algebraic fractions

> Show that $\dfrac{x + 3}{x - 2} - \dfrac{x - 1}{x + 2} = \dfrac{8x + 4}{(x-2)(x+2)}$

**Transform:**

$$\text{LHS} = \dfrac{(x+3)(x+2) - (x-1)(x-2)}{(x-2)(x+2)}$$

Expand numerator:

$$(x+3)(x+2) = x^2 + 5x + 6$$
$$(x-1)(x-2) = x^2 - 3x + 2$$

Subtract:

$$(x^2 + 5x + 6) - (x^2 - 3x + 2) = 8x + 4$$

**Conclude:**

$$\text{LHS} = \dfrac{8x + 4}{(x-2)(x+2)} = \text{RHS} \qquad \square$$

> [!tip] LHS / RHS notation
> Writing "LHS = … = RHS" is standard exam practice for "Show that" questions and the mark scheme accepts it. It makes the chain of reasoning crystal clear: you start from one side and arrive at the other. **Never** work from both sides toward the middle — always go LHS → RHS (or occasionally RHS → LHS if one side is simpler).

### Example 5 — Prove that the sum of any three consecutive integers is a multiple of 3

**Setup:** Let the three consecutive integers be $n$, $n+1$, $n+2$.

**Transform:**

$$n + (n+1) + (n+2) = 3n + 3 = 3(n + 1)$$

**Conclude:** $3(n + 1)$ is $3 \times \text{(integer)}$, which is a multiple of 3. $\square$

### Example 6 — Disproof by counterexample

> "The square of any prime number is odd." Is this true?

**Counterexample:** $2$ is prime, and $2^2 = 4$ is even. The statement is false. $\square$

One counterexample is enough to destroy a universal claim. See [[Disproof by Counterexample]] for more.

---

## §4 Common Mistakes in Proofs (Teaching Notes)

1. **Proof by example.** Showing it works for $n = 1, 2, 3$ is not a proof. A proof must use a general $n$. The 9260 mark scheme awards zero marks for substituting specific numbers.

2. **Using the same letter for independent quantities.** "Any two even numbers" must be $2m$ and $2n$ with different letters. Using $2n + 2n = 4n$ accidentally forces them to be equal.

3. **Circular reasoning.** In a "Show that" question, you must not start by assuming the result. Work from the left-hand side (or the given information) to reach the right-hand side. Never write the conclusion first and work backwards without reversing the logic.

4. **Not completing the conclusion.** Getting to $2(m + n + 1)$ but not writing "which is a multiple of 2, so it is even" loses the final mark. The algebra alone isn't enough — you must link it to the claim.

5. **Confusing "show that" with "verify."** "Show that" means build the chain from scratch. "Verify" means substitute and check. Read the command word.

6. **Expanding but not simplifying.** Students sometimes expand brackets correctly but stop before collecting like terms — leaving the examiner to do the simplification. Finish the algebra.

7. **Attempting to prove a false statement.** Before diving into a proof, consider: is the statement actually true? A quick mental check with small numbers can prevent wasted time. If you find a counterexample, the proof doesn't exist — present the counterexample instead.

---

## §5 Types of Proof at IGCSE and Beyond

| Proof type | Method | Exam level | Example |
|-----------|--------|------------|---------|
| **Direct proof** | Transform LHS into RHS using valid algebra | 9260 Core | "Prove the sum of two odds is even" |
| **Disproof by counterexample** | Find one case where the statement fails | 9260 Core | "Is every prime odd? No — 2 is prime and even" |
| **Proof by exhaustion** | Check every possible case | 9260 Extension | "Prove $n^2 - n$ is even" (check even $n$ and odd $n$) |
| **Proof by contradiction** | Assume the statement is false → derive impossibility | A-Level / IB | "Prove $\sqrt{2}$ is irrational" (see [[Proof by Contradiction]]) |
| **[[Proof by Induction\|Proof by induction]]** | Base case + "if true for $k$, then true for $k+1$" | A-Level / IB | "Prove $\sum_{r=1}^{n} r = \dfrac{n(n+1)}{2}$" |

At 9260, you need **direct proof**, **counterexample**, and a touch of **exhaustion**. [[Proof by Contradiction]] and [[Proof by Induction]] open at A-Level — previewed here so the ladder is visible.

---

## §6 Exam Notes

### OxAQA 9260

**Syllabus ref:** A8 — "Argue mathematically to show algebraic expressions are equivalent; use algebra to support and construct arguments and proofs."

This is the only IGCSE-level syllabus that explicitly assesses algebraic proof. Proof questions appear on both Paper 1E and Paper 2E. Typical questions:

- "Prove that the sum of three consecutive even numbers is always a multiple of 6."
- "Show that $(2n+1)^2 - (2n-1)^2$ is a multiple of 8."
- "Is it true that $n^2 + n + 1$ is always prime? Explain your answer."

**Mark scheme patterns:** (1) set up general form, (2) expand/simplify, (3) state conclusion with reason. The conclusion mark is often independent — students who get the algebra wrong can still earn it if the reasoning is correct for what they've written.

QWC (Quality of Written Communication) marks are allocated on selected proof questions. These reward clear chains with signal words like "therefore," "hence," "since."

### Cambridge 0580

Algebraic proof is **not** a standalone topic in 0580. However, "Show that" questions appear on Paper 4 and require the same chain-of-reasoning skills. The difference: 0580 "show that" questions are embedded in longer problems (geometry, algebra), not standalone proof tasks.

### Cambridge 0606

0606 uses proof structure for **trigonometric identities** (10.6) — proving $\sin x \tan x + \cos x \equiv \sec x$ etc. The technique is the same: start from one side, transform to match the other.

### A-Level / IB / AP

At these levels proof becomes a named, assessed skill — but *which* proofs are named differs by board:

- **Cambridge 9709:** no standalone proof topic; the skills live inside "show that" work.
- **Cambridge 9231 (Further):** [[Proof by Induction]] is the named technique (FP1 §1.7) — the direct continuation of this card's set-up/transform/conclude discipline.
- **UK domestic boards (Edexcel/AQA/OCR):** A-Level Maths names proof by deduction, exhaustion, and counterexample at AS, adding contradiction at A2 (the $\sqrt{2}$ and infinitude-of-primes classics); Further Maths adds induction.
- **IB AA:** SL proves by direct deduction; **HL Topic 1 names induction, contradiction, and counterexample**.
- **AP Calculus:** no formal proof topic — "justify your answer" free-response prompts carry the reasoning load.

The algebraic proof skills from 9260 are the foundation — everything above builds on knowing how to set up, transform, and conclude.

---

## §7 Connections

- **Prerequisite:** [[Logic]] — proof structures (direct, contradiction, exhaustion)
- **Prerequisite:** [[Chain of Thought]] — command words ("Show that" vs "Prove" vs "Verify")
- **Prerequisite:** [[Laws of Indices]] — index manipulation appears in proof simplification
- **Prerequisite:** [[Surds]] — surd manipulation in "show that" questions
- **Prerequisite:** [[Factors and Multiples (Vocab)]] — "multiple of" and "divisible by" language
- **Leads to:** [[Geometrical Proof]] — same proof skeleton, geometric theorems as tools
- **Leads to:** [[Proof by Contradiction]] — assume ¬P → contradiction → P (√2 irrationality)
- **Leads to:** [[Proof by Induction]] — base case + inductive step → true for all $n$
- **Leads to:** [[Proof by Exhaustion]] — check every case
- **Leads to:** [[Disproof by Counterexample]] — one failure kills a universal claim
- **Parallel:** [[Completing the Square]] — algebraic technique that appears in proof contexts

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\square$ | `\square` | End-of-proof marker (the "tombstone" or "Halmos square") |
| Q.E.D. | `\text{Q.E.D.}` | *Quod erat demonstrandum* — Latin for "which was to be demonstrated." Euclid's original Greek was ὅπερ ἔδει δεῖξαι (*hoper edei deixai*). Both $\square$ and Q.E.D. are acceptable in exams. Student mnemonic: **Q**uite **E**asily **D**one. 😏 |
| $\in$ | `\in` | "Belongs to" / "is an element of" (see [[Set Theory]]) |
| $\mathbb{Z}$ | `\mathbb{Z}` | The set of integers ($\mathbb{Z}$ from German *Zahlen* = numbers) |
| $\therefore$ | `\therefore` | "Therefore" |
| $\because$ | `\because` | "Because" |
| $\equiv$ | `\equiv` | "Is identically equal to" (for identities) |
| $\Rightarrow$ | `\Rightarrow` | "Implies" |
| $\forall$ | `\forall` | "For all" (see [[Logic]]) |
