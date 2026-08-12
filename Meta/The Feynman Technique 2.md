---
chinese: 费曼学习法 (Fèimàn xuéxí fǎ)
prerequisites:
  - "[[Von Neumann machine]]"
  - "[[Chain of Thought]]"
leads_to:
  - "[[The Love of Wisdom]]"
tags:
  - subject/methodology
  - subject/philosophy
  - subject/computer-science
  - domain/cognition
  - domain/learning
  - level/A-Level
  - level/university
  - level/life
  - type/methodology
  - type/meta
  - type/cross-domain
---

# The Feynman Technique 费曼学习法

> *"What I cannot create, I do not understand."*
> — the line still on Richard Feynman's blackboard the day he died.
>
> *To understand something is to be able to **rebuild** it — not to recite it back. The test isn't "can I repeat the words?" It's "can I construct it from scratch, and hand it on?"*

## What this card is for

There are two completely different things a mind can do with a piece of knowledge, and almost every bad study session confuses them. You can **copy** it — hold the words and play them back — or you can **interpret** it — read it as instructions and *build* the thing it describes. They feel similar from the inside (both produce the right answer on an easy quiz) and they are nothing alike when the question is new.

This card is the test that tells them apart. It is the same interpret-vs-copy distinction that sits at the heart of [[Von Neumann machine|self-reproduction]] and [[Turing Machine|the universal machine]] — turned into a learning method. The vault is built on it, which is why it lives in `Meta/`: the principle first, the famous trick second.

**The bilingual hook.** Chinese already names both halves: **死记硬背** (sǐ jì yìng bèi — "dead-memorise, hard-recite") is the *copy* pass; **融会贯通** (róng huì guàn tōng — "melt-together, thread-through") is the *interpret* pass. Every culture that teaches knows the gap; the Feynman Technique is just a reliable way to find which side of it you are standing on.

## The principle — understanding is the *interpret* pass

A [[Von Neumann machine|self-reproducing machine]] uses its blueprint φ two ways: it **interprets** φ to build a body, and it **copies** φ unread to pass on. A learner faces the same fork with every idea:

- **Copy** — you can reproduce the statement. The definition, the formula, the proof, word for word. The data is in there. Whether you *understand* it is completely undetermined.
- **Interpret** — you can run the idea as a program: derive the formula when you forget it, apply it to a case you've never seen, explain *why* it's true, notice when it *doesn't* apply. You can build from it.

Feynman's blackboard states the test in five words: **what I cannot create, I do not understand.** If you can only copy — recite, recognise, pattern-match — you are carrying the blueprint without being able to run it. The moment you're asked to *construct* (a fresh problem, an explanation to a confused friend), copy-only knowledge fails, and the failure is the diagnosis.

> The trap is that **copy disguises itself as understanding.** Re-reading your notes, highlighting, watching the lecture again — these light up *recognition* ("yes, I've seen this"), which feels like knowing and is really just confirming the copy is still on file. Cognitive science calls it the **fluency illusion**. Recognition is copy; reconstruction is interpret; only the second is understanding.

## The method — the Feynman Technique

The principle, operationalised. Four steps, and step 2 is the whole engine:

1. **Pick the concept.** Write its name at the top of a blank page.
2. **Explain it in plain language, as if teaching someone who's never met it** — out loud or on paper, *from memory*, no looking. This is the forced **interpret** pass: you cannot teach what you can only copy.
3. **Watch where you stall.** The sentence you can't finish, the step you "just know follows," the word you used without being able to define — that is precisely the seam where you were copying, not understanding. **The gap is the gold.**
4. **Go back to the source, fill the gap, simplify, and find an analogy.** Then run step 2 again. Loop until the explanation is plain, gapless, and yours.

This is the vault's own convention applied to itself (state the principle, then present the named trick as the principle *sorted* — same as LIATE or SOHCAHTOA). When the four steps feel mechanical, fall back on the principle: *try to create it; the failure to create is the map of what you don't understand.*

## Why it works — teaching is the highest-fidelity test

Teaching is the most demanding **interpret** pass there is, because your audience supplies new inputs your copy never anticipated. To answer a child's "but *why*?" you must run the idea, not replay it. This is why the research backs the method: the **testing effect** (Roediger & Karpicke, 2006 — retrieval practice beats re-reading by a wide margin) and Bjork's **desirable difficulties** both say the same thing — *learning happens when you reconstruct, not when you review.* The Feynman Technique is just retrieval practice with the bar set at "explain it simply," which is retrieval plus compression plus gap-detection in one move.

![[feynman-two-passes.svg|697]]

## Three states of knowledge

The von Neumann logic predicts exactly three outcomes — and they are the three kinds of "knowing" every teacher recognises:

- **Copy only → inert knowledge.** You can recite; you can't apply. The formula memorised, the problem unsolvable. (死记硬背.)
- **Interpret only → sterile knowledge.** You genuinely *get it* — for yourself — but can't produce a clean account anyone else can pick up. You built understanding in your own head but can't emit a transmissible blueprint. (The brilliant student who is a hopeless explainer.)
- **Interpret + copy → self-replicating knowledge.** You can both *build* from it (solve the novel case) **and** *hand on* a faithful description the next person can themselves interpret. This is mastery: **understanding that reproduces in another mind.**

That third state is the target, and it is not a metaphor. A [[Turing Machine|quine]] — a program that prints its own source — is knowledge in exactly that form: a description that can both *run* (interpret) and *copy* itself. A **self-hosting compiler** (a compiler whose source it can itself compile) is another. Both are the formal ideal of what a well-understood idea is: something you can execute *and* reproduce.

## The teacher as universal constructor

Here is the deepest reading, and it is the point of this whole vault. A [[Von Neumann machine|universal constructor]] takes a blueprint and builds the thing — *and* equips the offspring to build in turn. A **great teacher is a universal constructor for ideas**: they take a description, build understanding in a student, and the student leaves holding a blueprint they can both *use* and *pass on*. The lesson succeeded not when the student can repeat it, but when the student could now teach it.

That is why a vault of *proofs and derivations* — knowledge in interpretable, rebuildable form — is worth more than a vault of *facts*. Facts are copy; derivations are interpret. A card that shows *why* a rule works hands the reader a constructor, not just a result. The vault is, structurally, an attempt to store knowledge in **self-replicating** form: cards a student — or an LLM tutor reading them — can interpret *and* re-transmit. Every "always explain WHY" in its design is a vote for the interpret pass.

## The same gap, in other rooms

The interpret-vs-copy line runs through every kind of learning:

- **Mathematics (this vault's home turf).** Memorising the quadratic formula is *copy*; being able to **complete the square and derive it** is *interpret*. The vault's house rule — *always show why* — is a standing bet on the interpret pass: a derivation hands you a constructor, a bare result hands you only a fact.
- **Code.** Reading a tutorial and nodding along is *copy* (recognition); **reimplementing it from a blank file** is *interpret*. The notorious "I followed every step but still can't build anything myself" is copy mistaken for understanding. The apex case is a [[Turing Machine|self-hosting compiler]] — a program able to rebuild itself from its own source.
- **Language.** A phrasebook is *copy* — fixed sentences recited; **fluency** is *interpret* — generating sentences you've never heard. Precisely 死记硬背 vs 融会贯通.
- **Music.** Sight-reading the notes on the page is *copy*; **improvising in the style** is *interpret* — you've internalised the grammar, not just the piece.

Same gap, four rooms. In each, the test is identical: take away the page and ask the learner to *create*.

## Honest edges

- **Feynman didn't name "the Feynman Technique."** The tidy four-step packaging was assembled and popularised by others (notably Scott Young) and pinned to his name afterwards — a small [[Stories/Stigler's Law of Eponymy]] case. What's genuinely his is the *principle*: the blackboard dictum, and his habit of demanding a freshman-level explanation ("I couldn't reduce it to the freshman level… that means we really don't understand it"). The principle is Feynman; the numbered list is folklore.
- **You can fake the interpret pass.** Explain to a too-easy audience, or hand-wave the hard step in a confident voice, and you'll feel fluent while the gap survives. The method only works if you are honest about step 3 — and the safest audience is one that asks "why?", because they force inputs you can't pre-load.
- **Copy is not worthless.** You cannot interpret a blueprint you don't have. Memorising vocabulary, theorems, the multiplication table — that's the copy you later learn to *run*. The error isn't copying; it's *stopping* at copy and mistaking it for understanding. (Mnemonics, in this vault, are always "the principle, pre-sorted" — a copy you can re-derive — never the principle itself.)

## How to use it (and self-audit)

- **Close the book and teach the wall.** If you can't explain it from a blank page, you don't yet understand it — you recognise it. Recognition ≠ recall.
- **Hunt your own stalls.** Each "...and then it just works out" is a flag planted on a gap. Don't smooth past it; dig there.
- **Demand the analogy.** If you can't map the idea to something concrete, the interpret pass is incomplete. (This card's own analogy — interpret vs copy — *is* that move.)
- **Use the why-chain.** Keep asking "why?" of your own explanation until you hit either bedrock (an axiom, a definition, a [[Laws and Theorems|law]]) or a gap. Pairs with [[Forward Reading and Problem Discovery]]: that card is *trace causality forward to discover*; this one is *trace your own explanation back to find the hole.*
- **The one-line test before any exam:** for each topic, ask not "have I seen this?" but **"could I rebuild it on a blank page, and teach it?"** If no, you have a copy, not an understanding.

## Connections

- **Parent idea:** [[Von Neumann machine]] — interpret-vs-copy is the logic of self-reproduction; this card is that logic applied to learning. [[Stories/von Neumann the Martian]] tells the human version (self-replication on every scale).
- **Formal ideal:** [[Turing Machine]] — the quine and the universal machine are descriptions that can both run and reproduce; "self-replicating knowledge" made exact.
- **The same question, about machines:** [[The Turing Test]] — Searle's Chinese Room *is* the interpret-vs-copy distinction asked of a computer (perfect symbol-copying with no understanding); whether interpretation emerges from scaled-up prediction is the open version of this card's thesis.
- **Sibling methods:** [[Chain of Thought]] — structure the reasoning; [[Forward Reading and Problem Discovery]] — trace causality to *discover*; this card — test whether you can *rebuild*. [[Laws and Theorems]] — knowing whether a step rests on an axiom or a law is the bedrock the why-chain bottoms out on.
- **Cognitive grounding:** the testing effect / retrieval practice (Roediger & Karpicke 2006); Bjork's desirable difficulties; the fluency illusion.
- **The vault itself:** every "explain WHY" and every derivation is a bet on the interpret pass — knowledge stored so a reader (human or LLM) can rebuild and re-teach it.

## LaTeX / Notation Reference

This card is conceptual; the only formal vocabulary is the von Neumann pair it borrows.

| Term | Means |
|------|-------|
| φ (the description) | the thing you've learned — a formula, proof, or idea held in memory |
| **copy** pass | reproduce φ verbatim — recite, recognise (死记硬背) |
| **interpret** pass | run φ — derive, apply, explain, teach (融会贯通) |
| inert knowledge | copy only — can recite, cannot apply |
| sterile knowledge | interpret only — understands, cannot transmit |
| self-replicating knowledge | interpret + copy — can build *and* hand on (the goal) |
