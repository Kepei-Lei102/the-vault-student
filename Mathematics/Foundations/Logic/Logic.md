---
chinese: 逻辑 (luójí)
prerequisites:
  - "[[Set]]"
  - "[[Set Operations]]"
  - "[[Chain of Thought]]"
leads_to:
  - "[[Algebraic Proof]]"
  - "[[Geometrical Proof]]"
  - "[[Proof by Contradiction]]"
  - "[[Proof by Induction]]"
  - "[[Proof by Contrapositive]]"
  - "[[Proof by Exhaustion]]"
  - "[[Disproof by Counterexample]]"
  - "[[Recursion]]"
  - "[[Logic Gates]]"
  - "[[Boolean Algebra]]"
  - "[[Information Theory]]"
  - "[[Lewis Carroll the Mathematician]]"
  - "[[The Boolean-to-Silicon Bridge]]"
tags:
  - subject/mathematics
  - domain/logic
  - level/IGCSE
  - level/pre-IB
  - level/pre-AP
  - curriculum/OxAQA-9260
  - curriculum/Cambridge-0580
  - curriculum/Cambridge-0606
  - curriculum/IB-AA
  - curriculum/AP
  - type/definition
  - type/methodology
  - notation/implies
  - notation/iff
  - notation/for-all
  - notation/there-exists
  - notation/negation
  - misconception/converse-vs-implication
  - misconception/if-vs-only-if
---

# Logic 逻辑

## Definition

### Formal

**Logic** is the study of valid reasoning — the rules that determine when a conclusion follows from given statements. A **proposition** (命题) is a statement that is either true or false, but not both.

The core objects of logic are:

$$\underbrace{p, q, r, \ldots}_{\text{propositions}} \quad \underbrace{\lnot, \land, \lor, \Rightarrow, \Leftrightarrow}_{\text{connectives}} \quad \underbrace{\forall, \exists}_{\text{quantifiers}}$$

These combine to form **compound propositions** whose truth depends entirely on the truth of their parts and the rules of each connective.

### Intuitive — The Grammar of Mathematics

Every language has grammar — rules that tell you how to combine words into sentences that make sense. Logic is the grammar of mathematics. Just as you can't write a correct English sentence without knowing what "and," "or," "if," and "not" mean, you can't write a correct proof without knowing what $\land$, $\lor$, $\Rightarrow$, and $\lnot$ mean.

When you write "if $x > 3$ then $x^2 > 9$," you're using logic — specifically, an implication ($\Rightarrow$). When you say "$\sqrt{2}$ is irrational" and prove it by contradiction, you're using the logical law $\lnot(\lnot p) \equiv p$. When you write a set-builder expression like $\{x : x \in \mathbb{Z} \text{ and } x > 0\}$, you're using the connective $\land$ (and).

Logic has been there all along, hiding inside every proof in this vault. This card makes it visible.

### 中文锚点 (Chinese Anchor)

逻辑：**数学的语法。** 它告诉你怎样把"真"和"假"的判断组合成可靠的推理。

| 中文 | English | Key idea |
|------|---------|----------|
| 命题 (mìngtí) | Proposition | A statement that is either true or false |
| 真 (zhēn) | True (T) | The statement holds |
| 假 (jiǎ) | False (F) | The statement does not hold |
| 否定 (fǒudìng) | Negation | "Not $p$" — flips truth value |
| 且 / 并且 (qiě / bìngqiě) | And (conjunction) | Both must be true |
| 或 (huò) | Or (disjunction) | At least one must be true |
| 如果…那么 (rúguǒ…nàme) | If…then (implication) | $p$ guarantees $q$ |
| 当且仅当 (dāng qiě jǐn dāng) | If and only if (biconditional) | Both directions hold |
| 对所有 (duì suǒyǒu) | For all (universal) | Every element satisfies the condition |
| 存在 (cúnzài) | There exists (existential) | At least one element satisfies |

## Notation

| Symbol | Name | LaTeX | Read as | Example |
|--------|------|-------|---------|---------|
| $\lnot p$ | Negation | `\lnot p` | "not $p$" | $\lnot(x > 3) \equiv x \leq 3$ |
| $p \land q$ | Conjunction | `p \land q` | "$p$ and $q$" | $x > 0 \land x < 5$ |
| $p \lor q$ | Disjunction | `p \lor q` | "$p$ or $q$" (inclusive) | $x < 0 \lor x > 10$ |
| $p \Rightarrow q$ | Implication | `p \Rightarrow q` | "if $p$ then $q$" | $x > 3 \Rightarrow x^2 > 9$ |
| $p \Leftrightarrow q$ | Biconditional | `p \Leftrightarrow q` | "$p$ if and only if $q$" | $x^2 = 4 \Leftrightarrow x = \pm 2$ |
| $\forall$ | Universal quantifier | `\forall` | "for all" / "for every" | $\forall x \in \mathbb{R},\ x^2 \geq 0$ |
| $\exists$ | Existential quantifier | `\exists` | "there exists" | $\exists x \in \mathbb{R},\ x^2 = 2$ |

> [!info] Notation across curricula
> IGCSE exams (0580, 9260) use English words ("if…then," "and," "or") rather than symbols. The symbols $\Rightarrow$, $\Leftrightarrow$, $\forall$, $\exists$ appear at A-Level, IB, and university. This card teaches both because the *thinking* is the same — the notation just makes it precise.

## Key Facts

### 1. Truth Tables — The Complete Story

A **truth table** lists every possible combination of truth values and the resulting truth of the compound proposition. This is how we *define* the connectives — there's no ambiguity.

| $p$ | $q$ | $\lnot p$ | $p \land q$ | $p \lor q$ | $p \Rightarrow q$ | $p \Leftrightarrow q$ |
|-----|-----|-----------|-------------|------------|--------------------|-----------------------|
| **T** | **T** | F | **T** | **T** | **T** | **T** |
| **T** | F | F | F | **T** | F | F |
| F | **T** | **T** | F | **T** | **T** | F |
| F | F | **T** | F | F | **T** | **T** |

**WHY the truth table is the definition:** In ordinary English, "or" is ambiguous (does "soup or salad" mean you can have both?). In mathematics, we can't tolerate ambiguity. The truth table removes it completely — $p \lor q$ is true when *at least one* is true (inclusive or), full stop.

### 2. Implication — The Hardest Connective

$p \Rightarrow q$ means: **"whenever $p$ is true, $q$ is also true."** It says nothing about what happens when $p$ is false.

**WHY "false implies anything" is true:** Look at row 3 of the truth table — when $p$ is false, $p \Rightarrow q$ is true regardless of $q$. This feels wrong at first, but consider a concrete example:

"If it rains, I will bring an umbrella."

On a sunny day ($p$ = false), you haven't broken your promise whether you bring an umbrella or not. The promise only fails when it rains ($p$ = true) and you don't bring one ($q$ = false). That's exactly what the truth table says.

This is called **vacuous truth** — the same principle that makes $\emptyset \subseteq A$ true for every set $A$ (see [[Subset]]). When the condition is never satisfied, the implication is never violated.

**The four related statements:**

| Name | Form | Example |
|------|------|---------|
| **Implication** | $p \Rightarrow q$ | If it rains, I bring an umbrella |
| **Converse** | $q \Rightarrow p$ | If I bring an umbrella, it rains |
| **Inverse** | $\lnot p \Rightarrow \lnot q$ | If it doesn't rain, I don't bring an umbrella |
| **Contrapositive** | $\lnot q \Rightarrow \lnot p$ | If I don't bring an umbrella, it doesn't rain |

**Critical fact:** An implication and its contrapositive are logically equivalent ($p \Rightarrow q \equiv \lnot q \Rightarrow \lnot p$). The converse and inverse are NOT equivalent to the original — confusing implication with its converse is one of the most common errors in all of mathematics.

**WHY the contrapositive works:** Build the truth tables for both and check — they match in every row. Alternatively: if "rain → umbrella" is a rule you never break, then "no umbrella → no rain" must also be true (because if it were raining, you *would* have an umbrella). The information flows both ways, just through different doors.

**The material equivalence of implication:**

$$p \Rightarrow q \equiv \lnot p \lor q$$

This is one of the most important identities in logic. Read it as: "if $p$ then $q$" means the same as "either $p$ is false, or $q$ is true (or both)." Check the truth table — columns for $p \Rightarrow q$ and $\lnot p \lor q$ match in every row.

**WHY this matters:** It explains the "false implies anything" row. When $p$ is false, $\lnot p$ is true, so $\lnot p \lor q$ is true regardless of $q$. It also connects implication to the connectives you already know ($\lnot$ and $\lor$), which means implication isn't really a new operation — it's a shorthand. In circuit design, this identity lets you build an "if…then" gate from just a NOT gate and an OR gate.

### 3. Biconditional — Both Directions

$p \Leftrightarrow q$ means $(p \Rightarrow q) \land (q \Rightarrow p)$. Both directions must hold. Read it as "$p$ if and only if $q$" (abbreviated **iff**).

**Example:** "$x^2 = 9 \Leftrightarrow x = 3$" is **FALSE.** The $\Rightarrow$ direction fails: $x^2 = 9$ doesn't guarantee $x = 3$ (what about $x = -3$?). The correct biconditional is $x^2 = 9 \Leftrightarrow x = \pm 3$.

In definitions, we always use biconditionals (even if we write "is" instead of "iff"): "A number is even *if and only if* it is divisible by 2."

### 4. Negation Rules — How to Negate Correctly

Negation flips truth values, but for compound statements you must apply specific rules:

| Original | Negation | Rule name |
|----------|----------|-----------|
| $p \land q$ | $\lnot p \lor \lnot q$ | De Morgan's law |
| $p \lor q$ | $\lnot p \land \lnot q$ | De Morgan's law |
| $\forall x,\ P(x)$ | $\exists x,\ \lnot P(x)$ | Quantifier negation |
| $\exists x,\ P(x)$ | $\forall x,\ \lnot P(x)$ | Quantifier negation |
| $p \Rightarrow q$ | $p \land \lnot q$ | Implication negation |

**WHY negating $\forall$ gives $\exists$:** To disprove "every student passed" ($\forall x,\ P(x)$), you only need ONE who failed ($\exists x,\ \lnot P(x)$). To disprove "some student passed" ($\exists x,\ P(x)$), you need EVERY student to have failed ($\forall x,\ \lnot P(x)$). The quantifiers swap, just like $\land$ and $\lor$ swap under De Morgan's. It's the same pattern at different levels.

**WHY negating $\Rightarrow$ gives $\land$:** The implication $p \Rightarrow q$ fails in exactly one case: $p$ is true AND $q$ is false. So $\lnot(p \Rightarrow q) \equiv p \land \lnot q$. To disprove "if it rains, I bring an umbrella," you need a day when it rained AND I didn't bring one.

### 5. Quantifiers — "For All" and "There Exists"

Quantifiers turn open sentences (like "$x^2 \geq 0$") into propositions.

**Universal quantifier** $\forall$: "$\forall x \in \mathbb{R},\ x^2 \geq 0$" — this is a claim about EVERY real number. To prove it, you must argue for an arbitrary $x$. To disprove it, one counterexample suffices.

**Existential quantifier** $\exists$: "$\exists x \in \mathbb{R},\ x^2 = 2$" — this claims at least one such $x$ exists. To prove it, exhibit one (e.g., $x = \sqrt{2}$). To disprove it, you must show NO $x$ works.

**Where you've already used these:**
- Set-builder notation: $\{x : x \in \mathbb{Z} \text{ and } x > 0\}$ implicitly uses $\exists$ — "the set of $x$ such that there exists an element satisfying..."
- Subset definition: $A \subseteq B \iff \forall x,\ (x \in A \Rightarrow x \in B)$ — every element of $A$ is also in $B$
- Empty set is a subset of everything: $\forall A,\ \emptyset \subseteq A$ — true by vacuous truth (see [[Subset]])

### 6. Logic ↔ Set Theory ↔ Logic Gates — The Three-Way Parallel

The connection between logic, set theory, and digital circuits is not analogy — it's isomorphism. The same abstract structure appears in three different costumes:

| Logic | Set theory | Logic gate / Code | English |
|-------|-----------|-------------------|---------|
| $\lnot p$ | $A'$ | NOT gate / `!p` | Not / complement |
| $p \land q$ | $A \cap B$ | AND gate / `p && q` | And / intersection |
| $p \lor q$ | $A \cup B$ | OR gate / `p \|\| q` | Or / union |
| $p \Rightarrow q$ | $A \subseteq B$ | NOT-OR / `!p \|\| q` | Implies / subset |
| $p \Leftrightarrow q$ | $A = B$ | XNOR gate / `p == q` | Iff / equality |
| $\lnot(p \land q)$ | $(A \cap B)'$ | NAND gate | Not both |
| $\lnot(p \lor q)$ | $(A \cup B)'$ | NOR gate | Neither |
| $\forall x \in A,\ P(x)$ | — | `for` loop (all pass) | For all in $A$ |
| $\exists x \in A,\ P(x)$ | $\{x \in A : P(x)\} \neq \emptyset$ | `while` loop (find one) | There exists in $A$ |

**De Morgan's laws in all three:**

| Law | Logic | Set theory | Circuit identity |
|-----|-------|-----------|-----------------|
| 1st | $\lnot(p \land q) \equiv \lnot p \lor \lnot q$ | $(A \cap B)' = A' \cup B'$ | NAND = OR of NOTs |
| 2nd | $\lnot(p \lor q) \equiv \lnot p \land \lnot q$ | $(A \cup B)' = A' \cap B'$ | NOR = AND of NOTs |

**WHY this parallel exists:** A set IS the collection of things that make a proposition true. $A = \{x : P(x)\}$ — the set $A$ contains exactly those elements for which $P(x)$ is true. So operations on propositions (logic) translate directly into operations on their truth sets (set theory). A logic gate is a physical device that computes a truth table in hardware — electricity flowing = **T**, no electricity = F. De Morgan's laws work in all three worlds because they ARE the same law expressed in three languages.

**WHY this matters for CS:** Every `if` statement in code is an implication. Every `for` loop checking a condition on all items is a universal quantifier. Boolean algebra — the foundation of digital circuits — IS propositional logic with voltage levels instead of truth values. Hardware designers use De Morgan's laws daily to simplify circuits: replacing AND-of-NOTs with NOR saves transistors. The NAND gate alone is **universal** — you can build every other gate from just NANDs, which is why modern processors are essentially billions of NAND gates.

> [!tip] This is why Set Theory comes first in the vault
> The Set Theory cluster teaches $\cup$, $\cap$, $'$, and De Morgan's laws using concrete sets. This card reveals that those were logic all along: OR, AND, NOT, and the negation rules. Logic gates reveal they're also electronics. Same structure, three notations.

### 7. Proof Structures as Logical Patterns

Every proof type from [[Chain of Thought]] has a logical skeleton:

| Proof type | Logical skeleton |
|-----------|-----------------|
| **Direct proof** | Assume $p$. Show $p \Rightarrow q$. Conclude $q$. |
| **Proof by contradiction** | Assume $\lnot q$. Derive a contradiction. Conclude $q$. |
| **Proof by contrapositive** | To prove $p \Rightarrow q$, prove $\lnot q \Rightarrow \lnot p$ instead. |
| **Proof by exhaustion** | Split into cases: $(p_1 \lor p_2 \lor \cdots \lor p_n)$. Prove each $p_i \Rightarrow q$. |
| **Disproof by counterexample** | To disprove $\forall x,\ P(x)$, exhibit one $x$ where $\lnot P(x)$. |

**WHY contradiction works:** If assuming $\lnot q$ leads to a statement that is both true and false (a contradiction), then $\lnot q$ must be false — so $q$ is true. This relies on the law of excluded middle: every proposition is either true or false, with no third option.

## Common Misconceptions (Teaching Notes)

### 1. Confusing an implication with its converse

**Wrong:** Student proves $q \Rightarrow p$ and claims they've proved $p \Rightarrow q$.

**Example:** To show "if $n$ is a multiple of 4, then $n$ is even," a student writes "6 is even but not a multiple of 4." This tests the converse, not the original. The implication is about what happens when $n$ IS a multiple of 4.

**Fix:** Always identify the hypothesis ($p$) and conclusion ($q$). The proof must start from $p$ and arrive at $q$, never the reverse.

### 2. Thinking "or" means "one or the other, not both"

**Wrong:** Student interprets $p \lor q$ as exclusive or.

**Reality:** Mathematical "or" is always inclusive: $p \lor q$ is true when both are true. "Soup or salad" in a restaurant is exclusive or — but that's English, not logic. If a question says "$x \in A \cup B$," the element could be in both.

### 3. "If $p$ then $q$" means "$q$ causes $p$"

**Wrong:** Student thinks implication describes a causal relationship.

**Reality:** $p \Rightarrow q$ is about truth values, not causation. "$2 + 2 = 4 \Rightarrow \text{Paris is in France}$" is a true implication (T → T = T), but addition doesn't cause geography. In exams, implications usually DO have a logical connection — but formally, they don't need one.

### 4. Negating by just adding "not" in front

**Wrong:** Student negates "all cats are black" as "all cats are not black."

**Right:** "There exists a cat that is not black" ($\exists x,\ \lnot P(x)$). The quantifier flips AND the predicate negates. This is the single most important negation rule: $\lnot(\forall x,\ P(x)) \equiv \exists x,\ \lnot P(x)$.

### 5. Treating a single example as proof

**Wrong:** Student checks $n = 2$ and concludes "$n^2 > n$ for all $n$."

**Right:** One example doesn't prove a universal statement. (And in this case, $n = 1$ gives $1 > 1$, which is false — so the statement is actually wrong.) A universal statement requires either a general argument or a check of every case (exhaustion).

## Exam Notes

### OxAQA 9260 (Extension)

**Syllabus ref:** Cross-curricular. Logic underpins A8 (Algebraic Proof) and G9 (Geometrical Proof).

- 9260 does not test formal logic notation ($\Rightarrow$, $\forall$, etc.) directly. Instead, it tests logical *thinking*: constructing algebraic proofs, forming arguments, identifying counterexamples.
- "Show that" and "Prove" questions require valid chains of implication. Knowing the logical skeleton (§7 above) helps you structure these chains.
- Counterexample questions test $\lnot(\forall x,\ P(x)) \equiv \exists x,\ \lnot P(x)$: find ONE case where the claim fails.

### Cambridge 0580 Extended

**Syllabus ref:** Cross-curricular.

- 0580 does not use formal logic notation. Logical thinking is implicit in multi-step problems and "Show that" questions (Paper 4).
- "Explain why" questions require a logical argument in English — essentially a chain of implications expressed in words.

### Cambridge 0606

**Syllabus ref:** Cross-curricular; 0606 makes heavier use of "Hence" chains.

- "Hence" means "use the result you just proved" — a direct application of modus ponens: you've established $p$ and $p \Rightarrow q$, now state $q$.
- Proof by contradiction appears in selected topics (e.g., irrationality proofs).

### AP / IB / A-Level

- **IB Mathematics AA HL:** Formal proof by contradiction and counterexample are explicitly assessed (Topic 1: Number and Algebra). Notation $\Rightarrow$, $\Leftrightarrow$ expected.
- **A-Level Further Mathematics:** Proof by induction, contradiction, and exhaustion are named topics. Logic symbols are standard notation.
- **AP Calculus:** Logical structure tested through epsilon-delta definitions and "justify your answer" free-response prompts. Quantifiers are used implicitly: "for every $\varepsilon > 0$, there exists $\delta > 0$..."

## Connections

**Prerequisites:**
- [[Set]] — Logic vocabulary ("and," "or," "not") first appears in set definitions
- [[Set Operations]] — De Morgan's laws, union = or, intersection = and, complement = not
- [[Chain of Thought]] — Proof structures are logical patterns; this card formalises them

**Leads to:**
- [[Algebraic Proof]] — Applying logical chains to algebraic "Prove" questions (9260 A8)
- [[Geometrical Proof]] — Combining theorems via logical implication chains (9260 G9)

**Parallel concepts:**
- [[Subset]] — $A \subseteq B$ is $\forall x,\ (x \in A \Rightarrow x \in B)$; vacuous truth
- [[Venn Diagram]] — Visual representation of logical operations on sets
- [[Conditional Probability]] — $P(A \lvert B)$ mirrors the logical structure of implication restricted to a condition
- [[Counting Problems]] — "Processing information exactly as given" requires logical precision
- [[Differentiation]] — $\varepsilon$-$\delta$ limits use nested quantifiers ($\forall \varepsilon > 0,\ \exists \delta > 0$)

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $\lnot$ | `\lnot` | Negation ("not") |
| $\land$ | `\land` | Conjunction ("and") |
| $\lor$ | `\lor` | Disjunction ("or") |
| $\Rightarrow$ | `\Rightarrow` | Implication ("if…then") |
| $\Leftrightarrow$ | `\Leftrightarrow` | Biconditional ("iff") |
| $\implies$ | `\implies` | Implication with spacing (proof contexts) |
| $\iff$ | `\iff` | Biconditional with spacing (proof contexts) |
| $\forall$ | `\forall` | Universal quantifier ("for all") |
| $\exists$ | `\exists` | Existential quantifier ("there exists") |
| $\equiv$ | `\equiv` | Logical equivalence |
| $\lnot(\forall x)$ | `\lnot(\forall x)` | Negated universal |
| $\exists x,\ \lnot P(x)$ | `\exists x,\ \lnot P(x)` | "There exists $x$ such that not $P(x)$" |
