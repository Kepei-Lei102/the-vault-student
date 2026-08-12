---
chinese: 布尔代数
prerequisites:
  - "[[Logic Gates]]"
  - "[[Logic]]"
  - "[[Set Operations]]"
  - "[[Complement]]"
  - "[[Intersection]]"
  - "[[Union]]"
leads_to:
  - "[[Karnaugh Maps]]"
  - "[[Half-Adder and Full-Adder]]"
  - "[[Flip-Flops]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - domain/logic
  - domain/digital-circuits
  - level/A-Level
  - curriculum/Cambridge-9618
  - curriculum/A-Level
  - syllabus/9618-15-2
  - type/deep
  - type/theorem
  - type/proof
  - notation/AND-dot
  - notation/OR-plus
  - notation/NOT-bar
  - misconception/boolean-plus-is-arithmetic-plus
  - misconception/demorgan-forgets-to-flip-operator
  - misconception/minimal-form-is-unique
---

# Boolean Algebra 布尔代数

> **Two circuits that look nothing alike can compute the very same thing.** Boolean algebra is the rulebook of legal moves that carries one expression into another *without changing a single row of the truth table* — and the reason you ever bother is always the same: **fewer gates.**

## Definition

**Boolean algebra** is the algebra of the two values $\{0, 1\}$ under three operations — **AND** ($\cdot$), **OR** ($+$), and **NOT** ($\overline{\phantom{A}}$) — the same three that [[Logic Gates]] gave you as silicon. The gates *evaluate* an expression (inputs in, one bit out). The algebra does something different and more powerful: it lets you **transform** an expression into a different-looking one that is guaranteed to compute the identical function.

That guarantee is the whole point. [[Logic Gates]] proved (via the DNF algorithm) that *some* circuit exists for any truth table — but the circuit it hands you is usually bloated. Boolean algebra is how you shrink it. Every identity below is a promise: "replace the left-hand pattern with the right-hand pattern anywhere it appears, and the truth table does not move."

### 中文锚点

**布尔代数 (bù'ěr dàishù)** = 在 $\{0,1\}$ 上，用 **与 ($\cdot$)、或 ($+$)、非 ($\overline{\phantom{A}}$)** 三种运算构成的代数。核心动作不是"算出一个值"，而是**在真值表不变的前提下把表达式变形、化简**——用更少的门实现同一个功能。

| English | 中文 | 一句话 |
|---|---|---|
| identity law | 同一律 | 加 0 / 乘 1，什么都不变 |
| null (annihilator) law | 零律 | 加 1 全是 1；乘 0 全是 0 |
| idempotent law | 幂等律 | 自己和自己运算还是自己 |
| complement law | 互补律 | 一个量和它的反：或得 1，与得 0 |
| involution | 对合律（双重否定） | 否定两次转回来 |
| De Morgan's laws | 德摩根定律 | **拆杠翻号**：拆开长横线就要把 $\cdot$ 换成 $+$（反之亦然） |
| duality | 对偶原理 | 把 $+\leftrightarrow\cdot$、$0\leftrightarrow1$ 全换掉，定理仍成立——所以定律成对出现 |
| minimisation | 化简 | 用定律把 DNF 那种臃肿电路压到最少门数 |

中文教材通常只要求"记住真值表 + 会画门电路"，而 A-Level 9618 §15.2 真正的考点是**用代数定律化简**，以及判断两个电路是否等价。

---

## Almost arithmetic — but not quite

Your instincts from ordinary algebra are *mostly* right here, which is exactly why the two places they break will bite you. The symbols $+$ and $\cdot$ were chosen on purpose: commutativity, associativity, and AND-distributes-over-OR all look identical to school algebra.

But there is no subtraction and no division (there is no "$-1$" — the only inverse is NOT, and it works differently), and **two laws have no arithmetic analogue at all:**

$$1 + 1 = 1 \qquad\text{(not 2 — "true OR true" is just true)}$$
$$A + A = A,\qquad A \cdot A = A \qquad\text{(idempotence — a bit ORed or ANDed with itself is unchanged)}$$

Hold onto this: **$+$ is OR, not addition.** The single most common slip in the whole topic is writing $A + A = 2A$. There is no $2$ in this world.

---

## The laws

Every law comes in a **pair** — an AND-form and an OR-form — for a reason made precise in the Duality section below. Read them in pairs; you are only ever memorising half.

**Constants and single variables.**

| Law | AND-form | OR-form |
|---|:-:|:-:|
| Identity | $A \cdot 1 = A$ | $A + 0 = A$ |
| Null (annihilator) | $A \cdot 0 = 0$ | $A + 1 = 1$ |
| Idempotent | $A \cdot A = A$ | $A + A = A$ |
| Complement | $A \cdot \overline{A} = 0$ | $A + \overline{A} = 1$ |
| Involution | | $\overline{\overline{A}} = A$ |

**Structure.**

| Law | AND-form | OR-form |
|---|:-:|:-:|
| Commutative | $A \cdot B = B \cdot A$ | $A + B = B + A$ |
| Associative | $(A \cdot B)\cdot C = A \cdot(B \cdot C)$ | $(A + B)+ C = A +(B + C)$ |
| Distributive | $A \cdot(B + C) = A B + A C$ | $A +(B \cdot C) = (A + B)(A + C)$ |

That **second distributive law**, $A + BC = (A+B)(A+C)$, is the one with no arithmetic twin — in school algebra $2 + 3\cdot4 \neq (2+3)(2+4)$. In Boolean algebra it holds, and it does real work (you'll watch it collapse a term in the minimisation below).

**Absorption and consensus** — the workhorses of simplification, because each one *deletes* something:

$$A + AB = A \qquad\qquad A(A+B) = A \qquad\text{(absorption)}$$
$$A + \overline{A}B = A + B \qquad\qquad A(\overline{A}+B) = AB \qquad\text{(absorption, 2nd form)}$$
$$AB + \overline{A}C + BC = AB + \overline{A}C \qquad\text{(consensus — the middle term is redundant)}$$

### Why they hold — two proofs instead of a table

You can verify any of these by truth table (check every row), but the algebra itself is more illuminating. Two examples:

**Absorption, $A + AB = A$.** Factor and use the laws already above:
$$A + AB = A\cdot 1 + A\cdot B = A(1 + B) = A \cdot 1 = A.$$
(Identity, then distributive, then the *null law* $1+B=1$, then identity again.) Intuitively: if $A$ is already true the whole thing is true; if $A$ is false then $AB$ is false too — so $B$ never gets a vote. The $B$ is dead weight.

**Second absorption, $A + \overline{A}B = A + B$.** This one shows the surprising distributive law earning its keep:
$$A + \overline{A}B = (A + \overline{A})(A + B) = 1 \cdot (A + B) = A + B.$$
(Distributive OR-over-AND, then complement $A+\overline{A}=1$, then identity.) The $\overline{A}$ simply evaporates.

---

## De Morgan's laws — the flagship

Everything above is bookkeeping compared with the one identity you will reach for again and again:

$$\boxed{\;\overline{A \cdot B} = \overline{A} + \overline{B} \qquad\qquad \overline{A + B} = \overline{A} \cdot \overline{B}\;}$$

**The principle first.** A long overbar is a claim about a *combination*. To negate "**both** $A$ and $B$ are true," you only need **one** of them false — so NOT-AND becomes an OR of the negations. To negate "**at least one** of $A$, $B$ is true," you need **all** of them false — so NOT-OR becomes an AND of the negations. Negation trades "all" for "any," which is exactly the swap $\cdot \leftrightarrow +$.

**The mnemonic, as that principle sorted:** *break the bar, flip the operator.* When you split one long overbar into two short ones, the $\cdot$ underneath must flip to $+$ (or vice versa). The two moves are locked together — **splitting the bar without flipping the operator is the single most common mistake in §15.2.** When the mnemonic feels ambiguous, fall back on the principle: "not all" $=$ "at least one not."

**Proof by truth table** (first form; the second is its dual):

| $A$ | $B$ | $\overline{A \cdot B}$ | $\overline{A} + \overline{B}$ |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

The two columns agree on every row — the definition of *equal* Boolean functions.

**A proof that doesn't enumerate.** Four rows settle the two-variable case, but the *general* law $\overline{A_1 A_2 \cdots A_n} = \overline{A_1} + \overline{A_2} + \cdots + \overline{A_n}$ has $2^n$ rows — too many to check by hand. Here is the argument that never looks at a table and works for any $n$. It rests on one fact: in a Boolean algebra **every element has a *unique* complement** — the *only* $\overline{X}$ satisfying both $X \cdot \overline{X} = 0$ and $X + \overline{X} = 1$. (Uniqueness is quick: if $Y$ and $Z$ both complement $X$, then $Y = Y\cdot 1 = Y(X + Z) = YX + YZ = 0 + YZ = YZ$, and symmetrically $Z = YZ$, so $Y = Z$.)

So to prove $\overline{A \cdot B} = \overline{A} + \overline{B}$, it is enough to show that $\overline{A} + \overline{B}$ *acts as* the complement of $AB$ — that it kills $AB$ under AND and fills to $1$ under OR. Uniqueness then forces it to **be** $\overline{AB}$:

$$(AB)(\overline{A} + \overline{B}) = (A\overline{A})B + A(B\overline{B}) = 0\cdot B + A\cdot 0 = 0,$$
$$AB + (\overline{A} + \overline{B}) = (\overline{A} + \overline{B} + A)(\overline{A} + \overline{B} + B) = (1 + \overline{B})(\overline{A} + 1) = 1 \cdot 1 = 1.$$

The second line applies the OR-over-AND distributive law $X + YZ = (X+Y)(X+Z)$ with $X = \overline{A}+\overline{B}$, then $A + \overline{A} = 1$ and the null law. Product $0$, sum $1$ — so $\overline{A} + \overline{B}$ is *the* complement of $AB$, i.e. $\overline{A} + \overline{B} = \overline{A \cdot B}$. No rows; and the same argument (or a one-line induction on the two-input case) gives the $n$-variable law. It also says *why* the law is true rather than just *that* it is: an OR-of-negations is exactly the thing that annihilates an AND and completes it to $1$ — the definition of its complement. The second form $\overline{A + B} = \overline{A}\cdot\overline{B}$ falls out by the dual argument.

This is one law wearing three costumes across the vault: on sets it is $(A \cap B)' = A' \cup B'$ (see [[Set Operations]] and [[Complement]]); on propositions it is $\lnot(p \land q) \equiv \lnot p \lor \lnot q$; the single treatment that proves all three are the *same law* lives in [[Logic]]. Here we care about the fourth costume — **circuits.**

### What De Morgan looks like as a circuit

De Morgan is what *licenses gate substitution* — the reason [[Logic Gates]] could build everything from NAND alone. Read it geometrically as **bubble-pushing**: an inversion bubble sitting on a gate's output can be "pushed" back through the gate onto its inputs, and as it passes through, **the gate flips** (AND $\leftrightarrow$ OR).

![[de-morgan-bubble-pushing.svg|697]]

A NAND *is* an OR fed by inverted inputs; a NOR *is* an AND fed by inverted inputs. Same silicon, two ways to read it. This is the everyday tool of the hardware engineer: it lets you convert any AND/OR/NOT circuit into an all-NAND (or all-NOR) circuit — the form a fab actually manufactures.

> [!tip] Every programmer uses De Morgan too
> When you rewrite the condition `if (!(ready && loaded))` as `if (!ready || !loaded)`, that is De Morgan's first law in code — $\overline{A \cdot B} = \overline{A} + \overline{B}$ with `&&` for $\cdot$ and `||` for $+$. Flipping a compound condition and pushing the `!` inward is the same bubble-push, done in software. (Cambridge 9618 tests the circuit form; AP CSA touches the code form.)

---

## Duality — why the laws come in pairs

Look back at the tables: every law had two forms. That is not a coincidence, it is a **theorem about the whole system**.

> **The Duality Principle.** Take any true Boolean identity. Swap every $\cdot$ with $+$ and every $0$ with $1$ (leave the variables and the overbars alone). The result is *also* a true identity — its **dual**.

Identity's dual is identity; null's dual is null; the two distributive laws are each other's duals; De Morgan's two forms are duals. You proved the whole right-hand column for free the moment you proved the left.

**Why it holds:** the axioms Boolean algebra is built on are themselves self-dual — they were *stated* in dual pairs (an AND-axiom beside its OR-mirror, with $0$ beside $1$). Any proof is a chain of axiom applications; mirror every step and you get a valid proof of the mirrored statement. The symmetry of the foundations propagates to every theorem on top. (Careful: duality swaps $\cdot\leftrightarrow+$ and $0\leftrightarrow1$ *only*; it does **not** touch NOT, and it is a statement about *identities*, not about the value of a single expression.)

---

## Minimisation — the payoff

Here is the debt [[Logic Gates]] left unpaid. The DNF algorithm builds a circuit for any truth table, but a bloated one. Boolean algebra pays it off. Take the **burglar-alarm** function — sound the alarm when both the window sensor $W$ and motion sensor $M$ fire, *or* whenever the panic button $P$ is pressed. DNF reads five 1-rows straight off the truth table:

$$\text{alarm} = \overline{W}\,\overline{M}\,P + \overline{W} M P + W \overline{M} P + W M \overline{P} + W M P.$$

Five 3-input AND gates feeding a 5-input OR, plus inverters — well over a dozen gate-equivalents. Now watch the algebra dismantle it:

$$
\begin{aligned}
\text{alarm} &= \underbrace{\overline{W}\,\overline{M}\,P + \overline{W} M P + W \overline{M} P + W M P}_{\text{the four terms containing }P} + W M \overline{P} \\[4pt]
&= P\big(\overline{W}\,\overline{M} + \overline{W} M + W \overline{M} + W M\big) + W M \overline{P} && \text{(factor out } P) \\[4pt]
&= P\big(\overline{W}(\overline{M}+M) + W(\overline{M}+M)\big) + W M \overline{P} && \text{(factor } \overline{W},W) \\[4pt]
&= P\big(\overline{W}\cdot 1 + W \cdot 1\big) + W M \overline{P} && \text{(complement: } \overline{M}+M=1) \\[4pt]
&= P(\overline{W} + W) + W M \overline{P} = P\cdot 1 + WM\,\overline{P} && \text{(complement again)} \\[4pt]
&= P + \overline{P}(WM) = P + WM && \text{(2nd absorption: } A+\overline{A}B = A+B)
\end{aligned}
$$

$$\boxed{\;\text{alarm} = WM + P\;}$$

**One AND, one OR.** From a dozen-plus gates to *two* — same truth table, every row.

![[boolean-minimisation-before-after.svg|697]]

Fewer gates is not tidiness for its own sake. Each gate you delete is **less silicon area** (more circuits per wafer, cheaper chips), **less propagation delay** (the signal crosses fewer gates, so the circuit runs faster), and **less power and heat** (fewer transistors switching — the same energy story that haunts the [[RAM and the Memory Hierarchy|memory wall]] and Landauer's limit in [[Logic Gates]]). Minimisation is a direct lever on cost, speed, and heat.

> [!warning] Algebra needs cleverness; the systematic tool is the map
> The derivation above *worked*, but only because we spotted which term to factor first. There is no mechanical recipe for "always find the minimum this way" — a different first move can stall. The **systematic**, look-at-it-and-group method is the [[Karnaugh Maps|Karnaugh map]], which turns minimisation into a visual pattern-match and is the actual workhorse of 9618 §15.2. Boolean algebra is *why* the map's groupings are legal; the map is *how* you find them without cleverness.

---

## Standard forms

Two canonical shapes an expression can be forced into — both are just vocabulary for "which operator is on the outside," and both are needed before you can talk about Karnaugh maps.

- **Sum of Products (SOP)** — an OR of AND-terms, e.g. $WM + P$ or the DNF above. "Sum" $=$ OR ($+$), "product" $=$ AND ($\cdot$). Every DNF is an SOP; the *minimal* SOP is what minimisation hunts for.
- **Product of Sums (POS)** — an AND of OR-terms, e.g. $(A + B)(A + \overline{C})$. The dual shape; you get it by reading the truth table's **0-rows** instead of its 1-rows.

A **canonical** form lists every variable in every term (each term is a *minterm* for SOP, a *maxterm* for POS); a **minimal** form is what's left after the laws have done their work. Duality is exactly the bridge between the SOP and POS worlds.

---

## Worked examples

**1 — Convert to NAND-only via De Morgan.** Simplify and re-express $F = \overline{A} + \overline{B} + C$ for a NAND fab. Group the two bars with De Morgan *backwards*: $\overline{A} + \overline{B} = \overline{A B}$. So $F = \overline{AB} + C$. That is a NAND ($\overline{AB}$) ORed with $C$ — and an OR is itself two NOTs into a NAND (from [[Logic Gates]]). The bar-grouping is the move; De Morgan made a two-inverter-plus-OR mess into one NAND.

**2 — Prove two circuits are equivalent.** Are $F_1 = A\overline{B} + AB$ and $F_2 = A$ the same circuit? Factor $F_1 = A(\overline{B} + B) = A \cdot 1 = A = F_2$. Yes — the $B$ input on the left circuit is *decorative*, and you can delete two gates. (This is the kind of "are these equivalent?" question 9618 asks.)

**3 — Consensus in action.** Simplify $F = AB + \overline{A}C + BC$. The consensus law says the term $BC$ (built from the two "outer" literals $B$ and $C$, with $A$ appearing complemented in one parent and plain in the other) is redundant: $F = AB + \overline{A}C$. Sanity-check by cases: if $A=1$, $F = B + C\cdot0 + BC = B$, and $AB+\overline{A}C = B$; if $A=0$, $F = 0 + C + BC = C$, and $AB+\overline A C = C$. Agrees — the middle term never changed an answer.

---

## Beyond syllabus — the algebra behind the algebra

**It is a *lattice*, and there are bigger ones.** The $\{0,1\}$ system here is the *two-element* Boolean algebra $\mathbb{B}$. In general a **Boolean algebra** is any complemented distributive lattice — and the algebra of subsets of a set (with $\cup, \cap, {}'$) is another one. **Stone's Representation Theorem** (1936) says *every* Boolean algebra is isomorphic to a field of sets. That is the deep reason logic, set theory, and switching circuits keep turning out to be "the same" (the three-costume observation in [[Logic]]): they are all shadows of one abstract structure, and Stone's theorem is the proof, not the analogy.

**Minimisation is genuinely hard.** For 3–4 variables a Karnaugh map is easy by eye. In general, finding the provably-smallest circuit is *not* easy: the exact method (Quine–McCluskey) blows up exponentially, and the underlying decision problem is **NP-hard** — a cousin of the barriers in [[P vs NP]]. So the reason we teach a visual map and clever factoring, rather than a push-button "give me the minimum" formula, is not laziness: for large circuits, no cheap universal formula is believed to exist.

**Where it came from.** George Boole wrote *The Laws of Thought* in 1854 as pure logic, with no machine in sight. Claude Shannon's 1937 MIT master's thesis was the lightning bolt that connected it to switching circuits — the moment this algebra became the design language of every computer. That story is [[Stories/The Boolean-to-Silicon Bridge]].

---

## Exam Notes

### Cambridge 9618 (A Level, §15.2)
The examinable core. You must (1) know the Boolean identities — De Morgan, distributive, absorption, the constant/complement laws; (2) **simplify a given Boolean expression** using them, showing steps; (3) decide whether **two logic circuits are equivalent** (simplify both, compare); (4) move between a logic circuit, its Boolean expression, and its truth table. De Morgan and absorption carry most marks. The systematic minimiser examined alongside the identities is the [[Karnaugh Maps|Karnaugh map]]; the stateful elements ([[Flip-Flops|flip-flops]]) are the *other* half of §15.2 and a separate axis.

### Cambridge 0478 (IGCSE)
Logic **gates** are examined (§10), but Boolean **algebra** — the identities and simplification — is **not**. IGCSE stops at drawing circuits and truth tables; the algebra is an A-Level escalation. (See [[Logic Gates]].)

### Other A-Level boards (AQA / OCR / Edexcel)
All examine Boolean simplification and De Morgan, very similarly to 9618. A standard 5–6 mark question: "simplify this expression" or "show these two circuits are equivalent."

### AP
AP CSA is Java/OOP, not circuit design, so it does **not** examine Boolean algebra as such — but topic 2.6 ("comparing Boolean expressions") uses **De Morgan informally** to rewrite compound `if` conditions: `!(a && b)` becomes `!a || !b`. Worth knowing in that code form.

### IB Computer Science
Not a named statement: IB's A1.2 logic content stops at **gates and truth tables** ("logic gates processing encoded data") — the algebraic layer here is the Cambridge 9618 §15.2 extension. As with AP, De Morgan still earns its keep informally whenever IB code rewrites a compound condition.

---

## Connections

- **Parent:** [[Logic Gates]] — the gates (AND/OR/NOT/NAND/NOR/XOR) whose expressions this algebra transforms; the algebra here pays off the *minimisation* debt Logic Gates leaves open after DNF.
- **Foundations:** [[Logic]] — propositional logic; the single treatment proving De Morgan is *the same law* across logic, sets, and circuits. [[Set Operations]] (with [[Union]], [[Intersection]], [[Complement]]) — the isomorphic algebra of sets; $\cap \leftrightarrow \cdot$, $\cup \leftrightarrow +$, ${}' \leftrightarrow \overline{\phantom{A}}$.
- **Leads to:** [[Karnaugh Maps]] — the *systematic* visual minimiser these laws justify; the workhorse of §15.2. [[Half-Adder and Full-Adder]] — arithmetic circuits designed and simplified with exactly these identities.
- **Application in code:** [[Bitwise Operations]] — the same laws applied to every bit of a word at once; and everyday `if`-condition rewriting (De Morgan in software).
- **Depth / honest edge:** [[P vs NP]] — exact minimisation of a general Boolean function is NP-hard, which is *why* we teach maps and cleverness rather than a magic formula.
- **History:** [[Stories/The Boolean-to-Silicon Bridge]] — Boole (1854) → Shannon (1937) → silicon; how a book of logic became the design language of computers.

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|---|---|---|
| $A \cdot B$ | `A \cdot B` | AND (product); often written $AB$ |
| $A + B$ | `A + B` | OR (sum) — **not** arithmetic addition |
| $\overline{A}$ | `\overline{A}` | NOT (overbar); the bar can span a whole subexpression |
| $\overline{A \cdot B}$ | `\overline{A \cdot B}` | NAND — one long bar over a product |
| $\overline{A + B}$ | `\overline{A + B}` | NOR — one long bar over a sum |
| $\overline{\overline{A}} = A$ | `\overline{\overline{A}} = A` | involution (double negation) |
| $A + \overline{A} = 1$ | `A + \overline{A} = 1` | complement law |
| $A + BC = (A+B)(A+C)$ | `A + BC = (A+B)(A+C)` | OR-over-AND distributive (no arithmetic twin) |
| $A + \overline{A}B = A + B$ | `A + \overline{A}B = A + B` | 2nd absorption |
| $\overline{A \cdot B} = \overline{A} + \overline{B}$ | `\overline{A \cdot B} = \overline{A} + \overline{B}` | De Morgan (1st) — break the bar, flip the operator |
| $\overline{A + B} = \overline{A} \cdot \overline{B}$ | `\overline{A + B} = \overline{A} \cdot \overline{B}` | De Morgan (2nd), its dual |
