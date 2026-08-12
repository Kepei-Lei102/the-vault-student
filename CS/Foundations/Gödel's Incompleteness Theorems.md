---
chinese: 哥德尔不完备定理 (Gēdé'ěr bù wánbèi dìnglǐ)
prerequisites:
  - "[[Turing Machine]]"
  - "[[Russell's Paradox in the Post]]"
leads_to:
  - "[[The Love of Wisdom]]"
tags:
  - subject/computer-science
  - subject/mathematics
  - subject/philosophy
  - domain/mathematical-logic
  - domain/theory-of-computation
  - level/A-Level
  - level/university
  - type/deep
  - type/theorem
  - type/proof
  - type/cross-domain
  - misconception/godel-means-math-is-broken
  - misconception/godel-applies-to-everything
  - misconception/godel-proves-minds-beat-machines
---

# Gödel's Incompleteness Theorems 哥德尔不完备定理

> *In 1928 David Hilbert asked mathematics to prove itself: to lay down a finite list of axioms from which **every** mathematical truth could, in principle, be derived — complete, consistent, and mechanically checkable. In 1931 a 25-year-old named Kurt Gödel proved the dream impossible, with a single sentence that says of itself "I cannot be proved." Truth, he showed, will always outrun proof. It is the most important theorem in logic, and the closest mathematics has come to looking in a mirror.*

## The dream Gödel broke

For two thousand years, "proven" was mathematics' gold standard, but no one had asked whether *everything* true could be proven. By the 1920s **David Hilbert** turned that into a concrete program. He wanted to put all of mathematics on an unshakeable foundation: a formal system with

- a finite, mechanical list of **axioms** and rules of inference,
- **completeness** — every true statement is provable,
- **consistency** — no contradiction is provable (you can never prove both $S$ and $\lnot S$),
- and ideally **decidability** — a procedure to decide any statement's truth (the *Entscheidungsproblem*).

It was a magnificent, optimistic vision: mathematics as a closed machine that, given enough time, settles every question. Hilbert's faith was total — his 1930 retirement address ended *"Wir müssen wissen. Wir werden wissen."* ("We must know. We will know.") He gave that speech in Königsberg. The day before, at a conference in the same city, Gödel had quietly announced the result that proved him wrong forever.

## 中文锚点

**哥德尔不完备定理**（1931）粉碎了希尔伯特的梦想——用一套有限公理证明出**所有**数学真理。它有两条：

- **第一不完备定理**：任何**一致的**（不自相矛盾）、**能表达算术**的、公理可机械列举的形式系统，都是**不完备的**——存在**真但无法在系统内证明**的命题。
- **第二不完备定理**：这样的系统**无法证明自身的一致性**。

**机制**：**哥德尔编码**把每个符号、公式、证明都编成一个数（"命题即数据"，正是 [[Turing Machine|图灵机]] 通用机的逻辑）。于是"可证性"变成一个**算术谓词**，系统能谈论自己。再构造一句自指命题 **G**：*"G 在本系统内不可证。"* 若 G 可证，则系统证出一句假命题（不一致）；故若系统一致，G **为真却不可证**——**真理超出可证性**。

它**不是**说"数学崩塌了"或"什么都证不了"；它只说：没有任何**单一**系统能证明关于算术的**全部**真理。与 [[Turing Machine|停机问题]] 是同一把"对角线"利刃的两面。

## The vocabulary, made precise

The theorems are about **formal systems**, so four words must be exact:

- A **formal system** $F$ is a fixed alphabet, a set of **axioms** (starting statements taken for granted), and mechanical **rules of inference**. A **proof** is a finite chain of statements, each an axiom or following from earlier ones by a rule. *"Provable in $F$"* means: there exists such a chain ending in the statement.
- $F$ is **consistent** if it never proves both a statement and its negation. (An inconsistent system proves *everything*, so it is useless — consistency is the bare minimum.)
- $F$ is **complete** if, for every statement $S$ in its language, it proves $S$ or proves $\lnot S$ — it leaves no question open.
- $F$ is **effectively axiomatized** if a machine could, in principle, list its axioms and check whether a proof is valid. (This is the [[Turing Machine|computability]] condition — the axioms can't be an infinite cheat-sheet of all truths.)

Gödel's theorems apply to any $F$ that is consistent, effectively axiomatized, and **strong enough to express elementary arithmetic** (addition and multiplication of whole numbers — e.g. **Peano Arithmetic**, $PA$). That last condition is the doorway through which self-reference walks in.

## The First Incompleteness Theorem

> **Any consistent, effectively axiomatized formal system $F$ capable of expressing arithmetic is *incomplete*: there is a true statement of arithmetic that $F$ can neither prove nor disprove.**

You cannot patch the hole. Add the missing statement as a new axiom and the *bigger* system has its own unprovable truth. There is no finite (or even mechanically-listable) set of axioms from which all arithmetic truths follow. Hilbert's completeness is not merely hard — it is **impossible**.

![[godel-truth-vs-provability.svg|600]]
*What the theorem really says: in a sound system, everything provable is true, but not everything true is provable. **PROVABLE in $F$** sits *strictly inside* **TRUE** — and the Gödel sentence $G$ lives in the gap, true but out of reach. (Its negation $\lnot G$ is false, and also unprovable.)*

## How the sentence is built — the mechanism

The proof is one of the great pieces of reasoning in human history, and its engine is **self-reference made rigorous.** Three moves.

**1 — Gödel numbering: statements become numbers.** Gödel assigned every symbol a number, every formula (a string of symbols) a number, and every *proof* (a list of formulas) a number — via a clever prime-factorisation code. Now here is the hinge: a claim *about* formulas becomes a claim *about numbers*. In particular, *"the formula with Gödel number $n$ is provable in $F$"* turns into an ordinary **arithmetic predicate** $\mathrm{Prov}(n)$. A system that can talk about numbers can now talk about *its own proofs.* (This is exactly the [[Turing Machine|universal machine]]'s trick — *a description is itself just data* — applied to logic instead of computation.)

**2 — The self-referential sentence.** Using this, Gödel constructs a sentence $G$ that asserts of its *own* Gödel number that it is **not provable**:

$$G \;\equiv\; \text{“the sentence with Gödel number } \ulcorner G \urcorner \text{ is not provable in } F\text{.”}$$

There is no magic or vicious circle here — $G$ is a perfectly finite, concrete arithmetic statement; it just so happens that the number it talks about is its own. In plain words: **$G$ says "I am not provable."**

**3 — The fork that has no escape.** Now ask the only question that matters: *is $G$ provable in $F$?* Go slowly — one move per line.

- **Suppose $F$ proves $G$.** Then $G$ is provable. But $G$ *says* it is not provable. So $F$ has proved a **false** statement about arithmetic. A system that proves falsehoods about numbers is broken — inconsistent. So if $F$ is consistent, this case **cannot happen.**
- **Therefore $F$ does not prove $G$.** But that is *exactly what $G$ asserts.* So **$G$ is true.**
- **And $F$ cannot prove $\lnot G$ either**, because $\lnot G$ would be false ($G$ is true), and a consistent, sound system does not prove false things.

The result: **$G$ is true, but $F$ can neither prove nor disprove it.** And notice the vertigo — *we, standing outside $F$, can see that $G$ is true*, precisely by following the argument above. Truth has outrun provability. (Gödel's original used a slightly stronger assumption called $\omega$-consistency; **Rosser** sharpened it in 1936 so plain consistency suffices. The soundness version above is the cleanest to feel.)

![[godel-self-reference.svg|620]]
*The construction in one picture: Gödel numbering lets $F$ encode a sentence $G$ that refers to its own provability and asserts "$G$ is not provable in $F$." The fork is inescapable — if $F$ proves $G$, it has proved a falsehood (inconsistent); so if $F$ is consistent, $G$ is true and unprovable.*

## The same diagonal — Cantor, Gödel, Turing

$G$ is the **Liar paradox** ("this sentence is false") rebuilt with a flaw removed. The Liar collapses into nonsense because "false" can't be pinned down inside the language. Gödel's genius was to swap **"false"** for **"not provable"** — a notion that *can* be defined arithmetically — turning a paradox into a theorem. The self-referential engine is the same **diagonalisation** Cantor used to show the reals are uncountable, and the same one [[Turing Machine|Turing]] used for the halting problem:

- **Cantor:** a list of all reals → a real not on the list.
- **Gödel:** a system proving all truths → a truth it cannot prove.
- **Turing:** a program deciding all halting → a program it cannot decide.

One idea — *feed a system a description of itself and force it to contradict its own verdict* — three of the deepest limits in mathematics. (Computation's hard edge and logic's hard edge are literally the same edge; see the halting route below.)

## The Second Incompleteness Theorem

Gödel then turned the knife. The statement *"$F$ is consistent"* — call it $\mathrm{Con}(F)$ — is itself expressible in arithmetic (roughly: *"$F$ never proves $0=1$"*). And the entire argument above can be **formalised inside $F$**, yielding $F \vdash \big(\mathrm{Con}(F) \rightarrow G\big)$: *if $F$ could prove its own consistency, it could prove $G$.* But $F$ **cannot** prove $G$. Therefore:

> **No consistent system $F$ capable of arithmetic can prove its own consistency.**

This is the precise death of Hilbert's program. Hilbert wanted a *finitary* proof that mathematics is consistent — and the second theorem says a system strong enough to matter can never certify its own soundness from the inside. To trust arithmetic's consistency you must step *outside* it, into a stronger system — whose consistency is, in turn, unprovable from within. The ground never bottoms out. ([[Laws and Theorems]] makes this the centerpiece of how mathematical truth differs from physical law: a theorem is permanent *given* its axioms, but the axioms — and the system's very consistency — are chosen on faith.)

## The halting route — computation gives the same limit

There is a second, completely independent path to incompleteness, and it runs through the previous bay. Recall from [[Turing Machine|the halting problem]] that no algorithm can decide, for every program, whether it halts. Now suppose some formal system $F$ could prove *every* true statement of the form *"program $M$ halts on input $w$."* Then you could **decide halting**: to test whether $M$ halts, mechanically grind out all of $F$'s proofs in parallel, searching for either "$M$ halts" or "$M$ runs forever" — one must eventually appear. That would solve the halting problem, which is **impossible**. So $F$ must fail to prove some true halting statement: a concrete, true claim about a Turing machine that no consistent system can prove. **Undecidability *forces* incompleteness.** The two great limits of the 20th century are one limit, seen from two doors.

## True but unprovable — does it ever happen "for real"?

$G$ can feel like a logician's stunt — a sentence engineered to be unprovable. The deep question is whether *natural* mathematics, the kind people actually care about, ever hits the wall. It does.

- **Goodstein's theorem (1944).** Build a "Goodstein sequence" from any starting number by a simple base-bumping rule; the numbers rocket up almost unimaginably fast. Goodstein's theorem says **every such sequence eventually crashes back to 0.** It is *true* — provable using infinite ordinals — yet **Kirby and Paris proved in 1982 that it is unprovable in Peano Arithmetic.** A plain statement about ordinary whole numbers, true, and beyond $PA$'s reach. This is Gödel's abstract $G$ made flesh.
- **The Paris–Harrington theorem (1977)** — a strengthened finite Ramsey statement — was the first such "natural" example.
- **Set theory's version: independence.** The **Continuum Hypothesis** (is there a size of infinity strictly between the integers and the reals?) was shown *independent* of the standard axioms $ZFC$ — Gödel (1940) and Cohen (1963) proved $ZFC$ can neither prove nor disprove it. A precise, famous question that our foundational system simply **cannot settle**. (Independence is incompleteness's set-theoretic face.)

## What it does — and does not — mean

Gödel's theorems are the most *misquoted* results in mathematics. Hold the line on what they actually say.

- **They do NOT say "mathematics is inconsistent" or "broken."** Incompleteness is not inconsistency. Arithmetic is almost certainly consistent; it simply cannot prove *every* truth, nor certify its own consistency. Virtually all working mathematics is untouched.
- **They do NOT say "nothing can be proved."** An enormous amount is provable. The claim is narrow and exact: no *single* effectively-given consistent system proves *all* arithmetic truths.
- **They apply ONLY to systems that encode arithmetic.** Weaker systems can be complete *and* decidable: **Presburger arithmetic** (addition only, no multiplication) and Tarski's axioms for **Euclidean geometry** are both complete. Strength is what invites the paradox; multiplication is the spark.
- **Do not confuse this with Gödel's *Completeness* Theorem (1929).** Gödel proved both, a year apart, and the names sound contradictory. The *completeness* theorem says first-order **logic** is complete — every logically valid formula is provable. The *incompleteness* theorems say no system of **arithmetic** is complete — some arithmetic truths are unprovable. Different targets (logical validity vs arithmetic truth); no contradiction.

> [!warning] "Gödel proved the human mind beats any computer."
> This is the **Lucas–Penrose argument**: we can "see" that $G$ is true, but the machine/system cannot prove it — so minds transcend mechanism. It is famous and **widely rejected**. The flaw: we can only see $G$ is true *by assuming $F$ is consistent* — and by the **second theorem**, neither a machine *nor a human* can prove the consistency of the system they reason in. A human mind, if it is a formal system, has its *own* unprovable $G$ it cannot see past either. Gödel himself drew a careful disjunction, not the bold claim. The theorem limits *every* sufficiently strong reasoner — silicon or carbon.

> [!warning] The pop-philosophy abuse
> Incompleteness gets conscripted to "prove" relativism, that truth is subjective, that God exists (or doesn't), that science is bankrupt. All misuse. It is a precise theorem about formal systems strong enough to do arithmetic — not a cosmic licence for "anything goes." When someone invokes Gödel to win an argument about *anything other than mathematical logic*, reach for your wallet.

## The man who mapped the limits of reason

**Kurt Gödel** (1906–1978) was a quiet, precise Platonist who believed mathematical truths are *discovered*, not invented — which is what let him treat "truth" and "provability" as genuinely different things while his Vienna Circle contemporaries collapsed them together. In **Königsberg, September 1930**, he mentioned his result almost in passing during a discussion; nearly no one present understood it — except [[Stories/von Neumann the Martian|John von Neumann]], who grasped it instantly and within weeks had independently derived the *second* theorem, only to find Gödel already had it. A day later, in the same city, Hilbert broadcast *"we will know."* The torch had already passed, and the dream was already dead.

Gödel fled Nazi Europe in 1940 and settled at Princeton's Institute for Advanced Study, where his closest friend was **Einstein** — who said, in his last years, that he came to the Institute mainly "to have the privilege of walking home with Gödel." (For Einstein's 70th birthday Gödel produced a rotating-universe solution to general relativity containing *closed timelike curves* — mathematically valid time travel, offered as a gift.) At his 1947 citizenship hearing he announced he had found a logical flaw in the U.S. Constitution that would permit a legal dictatorship; Einstein and Morgenstern barely steered him off the topic before the judge.

The same relentless logic that found the limits of reason eventually turned inward. Gödel's lifelong hypochondria and fear of poisoning deepened into a conviction that he could eat only food his wife Adele prepared. When she was hospitalised for six months in 1977, he essentially stopped eating, and died in January 1978 weighing roughly 30 kg, the certificate reading *"malnutrition and inanition."* The man who proved that no system can guarantee its own consistency was, in the end, undone by the failure of his own. He is buried in Princeton; the theorem is immortal.

## Common Misconceptions

> [!warning] "Incompleteness means arithmetic is inconsistent / contains contradictions."
> The opposite. The theorem *assumes* consistency and concludes *incompleteness*. A consistent system is precisely the kind that must leave some truths unproven. Inconsistency would be far worse — it would prove everything.

> [!warning] "A more powerful system / a computer could finish the job."
> Adding axioms or compute power doesn't help: any consistent, arithmetic-capable system you build has its *own* true-but-unprovable sentence. The limit is structural, not a matter of effort or hardware — exactly as the [[Turing Machine|halting problem]] is undecidable for *any* computer.

> [!warning] "True but unprovable is a contradiction."
> "Provable in $F$" and "true" are different properties. Provability is about chains of symbols inside a system; truth is about what actually holds for the numbers. Gödel's achievement was to show these two notions, long treated as one, genuinely come apart.

## Exam Notes

Like the rest of this trio ([[Turing Machine]], [[The Turing Test]], [[P vs NP]]), Gödel's theorems are **not named on Cambridge IGCSE 0478 or A-Level 9618** — they are theory-of-computation / mathematical-logic enrichment. They earn their place as the logical twin of the halting problem and the philosophical capstone of the Foundations bay:

- **A-Level / IB further mathematics, Theory of Knowledge.** Incompleteness is a standard TOK touchstone for "the limits of mathematical knowledge" — and this card is the version that states it *correctly* rather than via the usual pop-misquotes.
- **University** — a fixture of mathematical logic, theory of computation, and philosophy of mathematics; the standard route is via computability (Turing) then Gödel numbering, exactly the lineage built here. Boolos, Burgess & Jeffrey's *Computability and Logic* is the classic text.
- **General literacy** — Gödel's name is invoked constantly and almost always wrongly. Knowing the real statement, its conditions, and its limits is the difference between understanding a deep result and parroting a slogan.

## Connections

- **Prerequisite / twin:** [[Turing Machine]] — same diagonalisation; the halting problem gives an independent route to incompleteness, and Gödel numbering is the universal machine's "code is data" trick in logical dress.
- **Sibling enrichment (the Turing-review trio):** [[The Turing Test]] — *can a machine think?*; [[P vs NP]] — *what can be solved efficiently?*; this card — *what can be proved at all?* The three hard edges seeded by one 1936 machine.
- **The epistemology:** [[Laws and Theorems]] — uses the second theorem as the proof that mathematical certainty is *conditional* on chosen axioms a system can't self-justify; the cleanest statement of "deductive truth has a floor it cannot see beneath."
- **The prequel:** [[Stories/Russell's Paradox in the Post]] — the foundations crisis began here. Russell's 1902 paradox broke Frege's logicism and forced the axiomatic rebuild (Zermelo's ZFC, Russell's type theory); Hilbert's program was the attempt to make that rebuild *provably* safe — exactly what these theorems show is impossible. The same self-referential diagonal, one generation apart.
- **The human thread:** [[Stories/von Neumann the Martian]] — von Neumann was in the room at Königsberg and grasped it first; the set-theory and foundations world this came from is his too.
- **The axiomatic method — and an escapee:** [[Congruence]] discusses Hilbert's axiomatisation of Euclidean **geometry** (SAS as his Axiom IV.6). Geometry is one of the *complete, decidable* systems that **escapes** incompleteness (Tarski proved it) — precisely because it cannot encode arithmetic. The same Hilbert, two dreams, two fates.

## Glossary / Notation Reference

| Symbol / term | Meaning |
|------|---------|
| formal system $F$ | a fixed alphabet + axioms + mechanical inference rules |
| **consistent** | $F$ never proves both $S$ and $\lnot S$ (the minimum requirement) |
| **complete** | for every statement $S$, $F$ proves $S$ or proves $\lnot S$ (leaves nothing open) |
| effectively axiomatized | a machine can list the axioms and check proofs (the computability condition) |
| $PA$ | Peano Arithmetic — the standard axioms of the whole numbers |
| Gödel numbering $\ulcorner S \urcorner$ | the unique number coding the statement (or proof) $S$ |
| $\mathrm{Prov}(n)$ | the arithmetic predicate "the statement numbered $n$ is provable in $F$" |
| $G$ | the self-referential sentence: "$G$ is not provable in $F$" — true but unprovable |
| $\mathrm{Con}(F)$ | the arithmetic statement "$F$ is consistent" — unprovable in $F$ (second theorem) |
| $ZFC$ | Zermelo–Fraenkel set theory with Choice — the standard foundation of mathematics |
