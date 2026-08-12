---
chinese: 定律与定理 (dìnglǜ yǔ dìnglǐ)
prerequisites:
  - "[[Torque]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Chain of Thought]]"
  - "[[Angular Momentum]]"
leads_to: []
tags:
  - subject/physics
  - subject/mathematics
  - subject/philosophy
  - domain/epistemology
  - domain/philosophy-of-science
  - level/A-Level
  - level/IB
  - level/AP
  - level/life
  - type/methodology
  - type/meta
  - type/philosophical
  - misconception/laws-are-proven
  - misconception/physics-is-just-applied-math
---

# Laws and Theorems 定律与定理

> *A theorem is true forever. A law is true until next Tuesday's experiment.*
>
> *We use two different words on purpose — and the words remember a distinction we often forget.*

## What this card is for

Build the rotational-dynamics trio — [[Torque]], [[Moment of Inertia]], [[Angular Momentum]] — and somewhere along the way a strange feeling arrives: it's as if physics is *legislating* a definition (torque) on purpose, so that everything downstream comes out mirroring Newton's laws. The derivations are airtight, yet the "root" feels *chosen* rather than discovered.

That feeling is correct, and it points at a genuine fault line between how **mathematics** and **physics** establish truth. This card makes the fault line explicit and turns it into a thinking tool: *math proves theorems from axioms; physics promotes observations to laws, then deduces.* The whole rest of the card is unpacking that one sentence and learning to use it.

## 中文锚点

中文把这条裂缝**直接写进了字里**。物理叫**定律**（dìnglǜ），数学叫**定理**（dìnglǐ）—— 同样是"定"（确定下来），但后一个字不同：

- **律** = 法律、纪律、规律 —— *被规定、被遵守的规则*。牛顿**定律**、能量守恒**定律**。
- **理** = 道理、真理、原理 —— *被论证出来的真理*。勾股**定理**、中值**定理**。

所以一个 **定律** 是"观察到自然在遵守的规律"，一个 **定理** 是"从前提严格证明出来的真理"。英文的 *law* 和 *theorem* 背着**完全相同**的区别 —— 这张卡片就是把这条裂缝讲清楚，并把它变成一种思考工具。

## Two ways to be true

**Mathematics is deductive.** Agree on a few axioms, and everything else is *proven* from them. Truth means *provability*: a theorem, once proven, is permanent — given its axioms. The certainty is real but conditional. The axioms themselves are *chosen*, not handed down (Euclid's parallel postulate, the axiom of choice, and the continuum hypothesis are all genuinely optional — drop or swap them and you get different, equally consistent mathematics), and Gödel showed any system rich enough to do arithmetic cannot prove its own consistency from the inside. But *within* a chosen system, deduction reigns and a theorem never expires.

**Physics has an empirical root and a deductive superstructure.** A physical law is a regularity observed so robustly that we *promote it to a premise* — and then we reason on top of it exactly like mathematicians, deducing consequences with full rigour. The root is observation; the building above it is proof. Crucially, the root is held only *provisionally*: a law stands until an experiment contradicts it (this falsifiability is, for Popper, what makes it science at all). When that happens the law isn't erased so much as **demoted** — Newton's laws weren't shown to be *false* by relativity and quantum mechanics; they were shown to be the *limiting case* of something deeper, exact for slow, heavy, everyday things and wrong for the fast and the tiny.

![[laws-and-theorems-two-towers.svg|697]]

## The tell: physics caught in the act (torque)

The rotational-dynamics trio is the clean specimen of this structure. We **define** torque as $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$ — a choice, not a measurement. But it is not a *free* choice: it is the unique definition that makes $\boldsymbol{\tau} = d\mathbf{L}/dt$ come out as a flawless mirror of $\mathbf{F} = d\mathbf{p}/dt$. So the sequence runs:

1. **Observe** and promote: $\mathbf{F} = m\mathbf{a}$ (the empirical root).
2. **Legislate** the definitions: torque, moment of inertia, angular momentum — chosen so the rotational story will parallel the linear one.
3. **Deduce** the entire apparatus ($\tau = I\alpha$, $L = I\omega$, conservation of angular momentum) as a deductive superstructure — *theorems*, given Newton.

The "the root is defined" feeling is exactly right: you are watching a deductive layer being bolted onto an empirical one, with a definition as the bolt. None of the rigour is fake; it's just that the rigour lives *above* the promoted observation, not underneath it.

## "Defined" and "fundamental" blur even at the bottom

It is tempting to tidy this into "maths is all definition, physics is all observation," but the boundary leaks. Newton's own $\mathbf{F} = m\mathbf{a}$ half-*defines* force (force is whatever accelerates a mass) while half-*asserting* an empirical claim (that a given push yields proportional acceleration across different bodies). Ernst Mach spent much of *The Science of Mechanics* (1883) exposing the circularity — force is defined through mass, mass is operationalised through force — and the worry has never fully gone away. Even the empirical bedrock has stipulation mixed into it. The lesson is not "physics is secretly maths"; it's that **every framework blends what we *decide to call things* with what the world then *does*** — and a careful thinker keeps a running tally of which clauses are definitions and which are claims about reality.

## What "law" meant at the origin

The word itself is a fossil of all this. The modern sense of a "law of nature" is a 17th-century invention with a frankly **juridical and theological** core. René Descartes, in the *Principia Philosophiae* (1644), deliberately transposed a *legal* metaphor into physics: God as the legislator, passive matter as a subject *subjected to* decrees it must obey, and his laws of motion as rules God had "established and made to act." Newton and Boyle inherited the framing — the laws of nature were the statutes the Divine Lawgiver had imposed on the particles of matter. The Latin *lex* itself means something "laid down" (we still say *lay down the law*), with roots reaching back to the Stoic and Roman *lex naturae*.

That is precisely why physics says **law** and not **theorem**: a theorem is something *proven*; a law was, at its birth, a *decree that nature obeys*. The theology has been quietly dropped, but the grammar survives intact — we still say the universe *obeys* its laws, as though matter could disobey.

> [!info] Do laws *govern* nature, or merely *describe* it? — a live debate
> Philosophers of science are still split, and the split is the same prescriptive-vs-descriptive tension the word carries. **The Humean / regularity camp** (after David Hume; sharpened into David Lewis's "best-system" account): a law is *nothing but* an exceptionally reliable pattern — nature doesn't "obey" anything, the regularities simply *are*, and "law" is just our name for the most economical summary of them. **The governing / necessitarian camp** (Dretske, Tooley, and Armstrong, c. 1977–83): laws are real features of the world that *make* matter behave as it does — the regularity is the symptom, the law is the cause. Where you land changes what you'd even expect a "final theory" to be: a perfect *summary*, or a set of *governing decrees*. Both cases are serious; the vault doesn't adjudicate it for you, only flags that the comfortable word "law" quietly takes a side.

## When the scaffolding becomes load-bearing (Noether)

There is a twist that stops "physics is just bookkeeping bolted onto Newton" from being the whole truth. Angular momentum *begins* as a mimic of linear momentum — but through Emmy Noether's theorem (1918) it turns out to encode a fact *deeper* than Newton: that **space has no preferred direction**. And it is conserved in arenas Newton cannot enter at all — a photon carries angular momentum, an electron has spin-$\tfrac12$, quantum fields conserve it, none of which obey $\mathbf{F} = m\mathbf{a}$. The deductive superstructure ended up revealing something *more* fundamental than the empirical premise it was built to imitate.

This is the general pattern, and it is the engine of the whole enterprise: **today's law is often tomorrow's theorem.** Kepler's laws became *theorems* of Newton's. Newton's laws are now *theorems* — the classical limit of quantum field theory and general relativity. Each generation's bedrock becomes the next generation's superstructure, derived from a deeper promoted observation. The empirical root keeps sinking; what was "just a law you had to accept" gets *explained*, and a new, deeper law takes its place at the bottom.

## How to use this — the methodology

1. **Sort the claim.** Meeting any physics result, ask: *is this empirical bedrock, or deductive superstructure?* A bedrock law you ultimately test against the world; a derived result you check by re-deriving. When something seems wrong, this tells you *where to push* — argue with the premise, or argue with the algebra, but know which you're doing.
2. **Hunt the legislated definition.** When a quantity feels "made up" — torque, entropy, action, the wavefunction — ask: *is it primitive, or forced by wanting some structure to hold?* Forced definitions are not arbitrary; they are the load-bearing choices, and **finding the constraint that forces them is usually the real understanding.** ("Torque is defined so the rotational law mirrors the linear one" *is* the insight, not a footnote to it.)
3. **Respect what each word promises.** *Law* flags **provisional** — don't be shocked when it bends; it's a promoted observation, not a proof. *Theorem* flags **permanent-given-axioms** — don't expect it to bend to data; if a theorem and an experiment disagree, either the axioms don't model the world or the experiment is flawed, but *never* the proof.
4. **Expect the floor to drop.** Treat every law as a possible theorem-in-waiting of some deeper law. That isn't cynicism about physics — it's the precise shape of physical progress: the search for the premise from which today's premises will one day follow.

## Connections

- **Trigger and worked example:** [[Torque]], [[Moment of Inertia]], [[Angular Momentum]] — the trio where you can watch physics legislate a definition and deduce the rest; [[Newton's Laws of Motion]] — the empirical root the whole rotational superstructure rests on, and itself a *law* (promoted observation), not a theorem.
- **Sibling Meta cards:** [[Forward Reading and Problem Discovery]] (causal tracing — the empirical mode of thought), [[Why Probability and Statistics]] (tools, not beliefs — the same "hold it provisionally" discipline applied to data), [[Chain of Thought]] (the deductive chain itself, the move that builds every superstructure).
- **The mechanism in the wild:** [[Stories/Aristotle to Apollo]] — a "law" of falling bodies that survived two thousand years and was then falsified on the Moon; [[Stories/The 1919 Eclipse]] — Newton's law of gravity quietly *demoted* inside Newton's own Royal Society. Both are the falsify-and-demote move this card describes, dramatised.
- **A third kind of truth — the statistical law:** [[Stories/Boltzmann's Tombstone]] — the second law of thermodynamics ("entropy never decreases") is not a theorem proved from axioms, nor a brute empirical decree, but a statement true at odds so overwhelming it is indistinguishable from certainty. Boltzmann's $S = k\log W$ is the vault's cleanest case study in what *kind* of truth a physical law can have.

## Receipts / further reading

- René Descartes, *Principia Philosophiae* (1644) — laws of motion as decrees God established; the juridical metaphor made literal.
- Ernst Mach, *Die Mechanik in ihrer Entwicklung* / *The Science of Mechanics* (1883) — the force–mass circularity in Newton's definitions.
- Karl Popper, *The Logic of Scientific Discovery* (1934/1959) — falsifiability as the mark of an empirical law.
- Emmy Noether, "Invariante Variationsprobleme" (1918) — every continuous symmetry yields a conservation law.
- David Lewis, *Counterfactuals* (1973) and the Mill–Ramsey–Lewis "best-system" view — laws as the best summary of the regularities; against Fred Dretske (1977), Michael Tooley (1977), and D. M. Armstrong, *What Is a Law of Nature?* (1983) — laws as relations that govern.
- Eugene Wigner, "The Unreasonable Effectiveness of Mathematics in the Natural Sciences" (1960) — why the deductive superstructure fits the world so eerily well.
- Stanford Encyclopedia of Philosophy, "Laws of Nature" — a standing survey of the whole debate.
